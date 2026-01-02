# League Eagle

**League Eagle** is an AI-powered fantasy football assistant that helps NFL fantasy league players dominate their leagues through intelligent trade analysis, real-time stats, and expert-backed insights.

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


## Current Goal

- * Phase 1: ESPN Fantasy API (League Data)
- Phase 2: ESPN NFL API (Player Stats & Info)
- Phase 3: Fantasy Expert API (Expert Analysis)
- Phase 4: Validate Use Cases
- Phase 5: BE Construction
- Phase 6: Front-End Design
- Phase 7: FE Construction
- Phase 8: Integration
- Phase 9: Testing 


## Setup Instructions ESPN Fantasy API

1. Open terminal and go to the subfolder (e.g., espn_api).
2. Create venv (only once):
   python -m venv venv
3. Activate venv:
   .\venv\Scripts\Activate.ps1
   (If permission error, run: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned)
4. Install dependencies:
   pip install -r requirements.txt
5. Run the script:
   python script.py
6. Deactivate venv when done:
   deactivate

# Alternatively, run without activating:
.\venv\Scripts\python script.py

This keeps Python packages isolated inside the subfolder.
