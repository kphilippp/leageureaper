# League Reaper

> *"Death to bad trades."*

**League Reaper** is an AI-powered fantasy football assistant that helps NFL fantasy league players dominate their leagues through intelligent trade analysis, real-time stats, and expert-backed insights.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [AWS Infrastructure](#aws-infrastructure)
- [Project Structure](#project-structure)
- [Data Flow](#data-flow)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [License](#license)

---

## Features

### General
- **Player Stats** — View current and historical stats for any NFL player
- **Team Stats** — Comprehensive team performance data
- **Roster Information** — See which players are on which teams
- **Depth Charts** — Updated depth charts for all NFL teams
- **Team News** — Real-time team-specific news and updates

### League-Specific
- **League Dashboard** — View all connected fantasy leagues
- **Team Management** — See all teams within a league
- **Roster Views** — View all players on any team in your league
- **Trade Analyzer** — AI-powered trade suggestions with detailed reasoning
- **Expert Insights** — Analysis based on what professionals are saying (podcasts, articles)

### Core Principles
- All data is always up to date (synced every 15 minutes during season)
- Scalable architecture built for growth
- AI-powered insights using Claude API

---

## Tech Stack

### Application Layer

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | Next.js 14+ (App Router) | SSR, React Server Components, routing |
| **Language** | TypeScript | Type safety across frontend and backend |
| **Styling** | Tailwind CSS | Utility-first CSS framework |
| **State Management** | TanStack Query | Server state, caching, refetching |
| **Backend** | Express.js | REST API, business logic |
| **Validation** | Zod | Schema validation for requests |
| **ORM** | Prisma | Type-safe database access |
| **AI** | Claude API (Anthropic) | Trade analysis, expert synthesis |

### AWS Infrastructure

| Service | Purpose |
|---------|---------|
| **CloudFront** | CDN — global edge caching |
| **ALB** | Application Load Balancer — traffic distribution, SSL termination |
| **ECS Fargate** | Container orchestration — runs Next.js and Express containers |
| **RDS** | Managed PostgreSQL database |
| **ElastiCache** | Managed Redis — caching and sessions |
| **SQS** | Message queue — decouples API from heavy processing |
| **Lambda** | Serverless functions — background job workers |
| **EventBridge** | Cron scheduler — triggers periodic data syncs |
| **ECR** | Docker image registry |
| **Secrets Manager** | Secure credential storage |
| **CloudWatch** | Logging, metrics, and alerting |

### Infrastructure as Code

| Tool | Purpose |
|------|---------|
| **Terraform** | Define and provision all AWS resources |
| **Docker** | Containerize applications |
| **GitHub Actions** | CI/CD pipeline |

---

## Architecture

```
                         ┌─────────────────┐
                         │   CloudFront    │
                         │      (CDN)      │
                         └────────┬────────┘
                                  │
               ┌──────────────────┴──────────────────┐
               │                                     │
               ▼                                     ▼
        ┌─────────────┐                       ┌─────────────┐
        │     ALB     │                       │     ALB     │
        │  (frontend) │                       │  (backend)  │
        └──────┬──────┘                       └──────┬──────┘
               │                                     │
               ▼                                     ▼
        ┌─────────────┐                       ┌─────────────┐
        │ ECS Fargate │                       │ ECS Fargate │
        │  (Next.js)  │ ───── REST API ─────▶ │  (Express)  │
        │             │                       │             │
        │  - SSR      │                       │  - Routes   │
        │  - Pages    │                       │  - Services │
        │  - UI       │                       │  - Prisma   │
        └─────────────┘                       └──────┬──────┘
                                                     │
                    ┌────────────────────────────────┼────────────────────────────┐
                    │                                │                            │
                    ▼                                ▼                            ▼
             ┌─────────────┐                  ┌─────────────┐              ┌─────────────┐
             │ ElastiCache │                  │     RDS     │              │     SQS     │
             │   (Redis)   │                  │ (PostgreSQL)│              │   (Queue)   │
             │             │                  │             │              │             │
             │  - Cache    │                  │  - Players  │              │  - Jobs     │
             │  - Sessions │                  │  - Teams    │              │             │
             └─────────────┘                  │  - Leagues  │              └──────┬──────┘
                                              │  - Users    │                     │
                                              │  - Trades   │                     ▼
                                              └─────────────┘              ┌─────────────┐
                                                     ▲                     │   Lambda    │
                                                     │                     │  (Workers)  │
                                                     │                     │             │
                                                     └─────────────────────│  - Sync     │
                                                                           │  - Analyze  │
                                                                           │  - Ingest   │
                                                                           └─────────────┘
                                                                                  ▲
                                                                                  │
                                                                           ┌─────────────┐
                                                                           │ EventBridge │
                                                                           │   (Cron)    │
                                                                           └─────────────┘
```

---

## AWS Infrastructure

### Compute

| Service | Resource | Purpose |
|---------|----------|---------|
| ECS Fargate | `league-reaper-web` | Next.js frontend with SSR |
| ECS Fargate | `league-reaper-api` | Express.js backend API |
| Lambda | `sync-nfl-stats` | Sync player/team data from NFL APIs |
| Lambda | `process-trade` | Analyze trades using Claude API |
| Lambda | `ingest-podcasts` | Transcribe and embed expert content |

### Data

| Service | Resource | Purpose |
|---------|----------|---------|
| RDS | PostgreSQL 15 | Primary database |
| ElastiCache | Redis 7 | Caching layer |
| S3 | `league-reaper-assets` | Static assets, Lambda code |

### Networking

| Service | Resource | Purpose |
|---------|----------|---------|
| VPC | `league-reaper-vpc` | Isolated network |
| ALB | `league-reaper-frontend-alb` | Frontend load balancer |
| ALB | `league-reaper-backend-alb` | Backend load balancer |
| CloudFront | Distribution | Global CDN |

### Messaging

| Service | Resource | Purpose |
|---------|----------|---------|
| SQS | `trade-analysis-queue` | Queue for trade analysis jobs |
| SQS | `data-sync-queue` | Queue for data sync jobs |
| EventBridge | `nfl-sync-schedule` | Cron trigger every 15 min |

---

## Project Structure

```
league-reaper/
├── apps/
│   ├── web/                       # Next.js frontend
│   │   ├── app/                   # App Router pages
│   │   │   ├── (auth)/            # Auth routes (login, signup)
│   │   │   ├── (dashboard)/       # Protected dashboard routes
│   │   │   │   ├── leagues/       # League views
│   │   │   │   ├── players/       # Player stats
│   │   │   │   ├── teams/         # Team views
│   │   │   │   └── trades/        # Trade analyzer
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx           # Landing page
│   │   ├── components/
│   │   │   ├── ui/                # Base UI components
│   │   │   ├── players/           # Player-specific components
│   │   │   ├── leagues/           # League components
│   │   │   └── trades/            # Trade analyzer components
│   │   ├── lib/
│   │   │   ├── api.ts             # API client
│   │   │   └── utils.ts           # Utility functions
│   │   ├── Dockerfile
│   │   ├── tailwind.config.ts
│   │   └── package.json
│   │
│   └── api/                       # Express backend
│       ├── src/
│       │   ├── routes/
│       │   │   ├── auth.ts        # Authentication routes
│       │   │   ├── leagues.ts     # League endpoints
│       │   │   ├── players.ts     # Player endpoints
│       │   │   ├── teams.ts       # Team endpoints
│       │   │   └── trades.ts      # Trade analysis endpoints
│       │   ├── services/
│       │   │   ├── auth.ts        # Auth logic
│       │   │   ├── cache.ts       # Redis caching
│       │   │   ├── claude.ts      # Claude API integration
│       │   │   ├── nfl.ts         # NFL data fetching
│       │   │   └── trade.ts       # Trade analysis logic
│       │   ├── middleware/
│       │   │   ├── auth.ts        # JWT verification
│       │   │   └── validate.ts    # Request validation
│       │   └── index.ts           # Express app entry
│       ├── Dockerfile
│       └── package.json
│
├── packages/
│   ├── shared-types/              # Shared TypeScript types
│   │   ├── src/
│   │   │   ├── player.ts
│   │   │   ├── team.ts
│   │   │   ├── league.ts
│   │   │   ├── trade.ts
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── db/                        # Prisma database package
│   │   ├── prisma/
│   │   │   ├── schema.prisma      # Database schema
│   │   │   └── migrations/
│   │   ├── src/
│   │   │   └── index.ts           # Prisma client export
│   │   └── package.json
│   │
│   └── validation/                # Zod schemas
│       ├── src/
│       │   ├── player.ts
│       │   ├── trade.ts
│       │   └── index.ts
│       └── package.json
│
├── lambdas/
│   ├── sync-nfl-stats/            # NFL data sync worker
│   │   ├── src/
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   ├── process-trade/             # Trade analysis worker
│   │   ├── src/
│   │   │   └── index.ts
│   │   └── package.json
│   │
│   └── ingest-podcasts/           # Podcast ingestion worker
│       ├── src/
│       │   └── index.ts
│       └── package.json
│
├── infra/
│   └── terraform/
│       ├── main.tf                # Main configuration
│       ├── variables.tf           # Input variables
│       ├── outputs.tf             # Output values
│       ├── vpc.tf                 # VPC configuration
│       ├── ecs.tf                 # ECS clusters and services
│       ├── rds.tf                 # RDS PostgreSQL
│       ├── elasticache.tf         # Redis cluster
│       ├── lambda.tf              # Lambda functions
│       ├── sqs.tf                 # SQS queues
│       ├── eventbridge.tf         # Cron schedules
│       ├── alb.tf                 # Load balancers
│       ├── cloudfront.tf          # CDN distribution
│       └── secrets.tf             # Secrets Manager
│
├── .github/
│   └── workflows/
│       ├── ci.yml                 # Test and lint
│       └── deploy.yml             # Deploy to AWS
│
├── turbo.json                     # Turborepo configuration
├── package.json                   # Root package.json
└── README.md
```

---

## Data Flow

### User Loads Dashboard

```
1. User visits leaguereaper.com
2. CloudFront receives request
3. Request forwarded to Frontend ALB
4. ALB routes to Next.js container (ECS)
5. Next.js needs user's leagues for SSR
6. Next.js calls Express API (Backend ALB → ECS)
7. Express checks Redis cache
8. Cache MISS → Express queries PostgreSQL via Prisma
9. Data returned, cached in Redis
10. Next.js renders HTML with data
11. User sees fully rendered page
```

### User Requests Trade Analysis

```
1. User clicks "Analyze Trade"
2. Frontend POSTs to /api/trades/analyze
3. Express receives request
4. Express creates job, pushes to SQS
5. Express returns { jobId, status: "pending" }
6. Lambda picks up message from SQS
7. Lambda fetches player data from RDS
8. Lambda calls Claude API with context
9. Lambda saves result to RDS
10. Frontend polls /api/trades/{jobId}
11. Eventually returns { status: "complete", analysis: "..." }
```

### Background Data Sync

```
1. EventBridge triggers at scheduled time (every 15 min)
2. Lambda (sync-nfl-stats) invoked
3. Lambda calls Sleeper/ESPN APIs
4. Lambda upserts data to PostgreSQL
5. Lambda invalidates relevant Redis cache keys
6. Lambda completes
```

---

## Getting Started

### Prerequisites

- Node.js 20+
- Docker
- AWS CLI configured
- Terraform

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/league-reaper.git
cd league-reaper

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local

# Start local PostgreSQL and Redis (Docker)
docker-compose up -d

# Run database migrations
npm run db:migrate

# Start development servers
npm run dev
```

### Running Tests

```bash
# Run all tests
npm run test

# Run tests with coverage
npm run test:coverage

# Run specific package tests
npm run test --filter=api
```

---

## Environment Variables

### Frontend (apps/web)

```env
NEXT_PUBLIC_API_URL=http://localhost:4000
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### Backend (apps/api)

```env
# Server
PORT=4000
NODE_ENV=development

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/league_reaper

# Redis
REDIS_URL=redis://localhost:6379

# Auth
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=7d

# External APIs
SLEEPER_API_URL=https://api.sleeper.app/v1
ANTHROPIC_API_KEY=your-claude-api-key

# AWS (for local Lambda testing)
AWS_REGION=us-east-1
SQS_TRADE_QUEUE_URL=http://localhost:4566/queue/trade-analysis
```

---

## Deployment

### Initial Setup

```bash
# Initialize Terraform
cd infra/terraform
terraform init

# Create workspace
terraform workspace new production

# Plan infrastructure
terraform plan -var-file="production.tfvars"

# Apply infrastructure
terraform apply -var-file="production.tfvars"
```

### CI/CD Pipeline

The GitHub Actions workflow handles:

1. **On Pull Request:**
   - Lint and type check
   - Run tests
   - Build Docker images

2. **On Merge to Main:**
   - Build and push Docker images to ECR
   - Update ECS services
   - Run database migrations
   - Invalidate CloudFront cache

---

## Data Sources

| Source | Data | Update Frequency |
|--------|------|------------------|
| Sleeper API | Fantasy league data, rosters | Real-time via OAuth |
| ESPN API | Player stats, team data | Every 15 minutes |
| NFL.com | Depth charts, injuries | Every 15 minutes |
| Podcast Transcripts | Expert analysis | Daily |

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Contact

- **Website:** [leaguereaper.com](https://leaguereaper.com)
- **Twitter:** [@LeagueReaper](https://twitter.com/LeagueReaper)
- **Email:** support@leaguereaper.com

---

