# ESPN Fantasy Football API Documentation

## Overview

This documentation outlines the ESPN Fantasy Football API endpoints and view parameters, detailing what data each view provides and recommended combinations for different use cases.

**Base URL Format:**
```
https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}
```

**Authentication:**
- Requires cookies: `espn_s2` and `swid`
- Both can be obtained from browser cookies after logging into ESPN Fantasy

---

## Individual Views

### 1. `mTeam` - Team Information View

**Purpose:** Provides comprehensive team metadata, owner information, and season records.

**What You Get:**
- ✅ Owner display names (e.g., "ESPNFAN8963221637")
- ✅ Owner first and last names
- ✅ Team names and abbreviations
- ✅ Team logos (URL)
- ✅ Team records (wins, losses, ties)
- ✅ Win percentage
- ✅ Win/loss streak (type and length)
- ✅ Playoff seeding and rankings
- ✅ Total points scored
- ❌ Player rosters
- ❌ Matchup scores

**Use When:**
- You need team standings
- You need owner information
- You want team metadata (names, logos, etc.)

**Example Team Object Keys:**
```json
{
  "id": 1,
  "name": "Team Name",
  "abbrev": "TN",
  "logo": "https://...",
  "owners": ["{owner-id}"],
  "primaryOwner": "{owner-id}",
  "record": {
    "overall": {
      "wins": 10,
      "losses": 4,
      "ties": 0,
      "percentage": 0.714,
      "streakType": "WIN",
      "streakLength": 3
    }
  },
  "currentProjectedRank": 1,
  "playoffSeed": 1
}
```

---

### 2. `mRoster` - Roster View

**Purpose:** Provides current team rosters with detailed player information.

**What You Get:**
- ✅ Complete player rosters
- ✅ Player IDs
- ✅ Player names (first, last, full)
- ✅ Player positions and eligibility
- ✅ Injury status
- ✅ Player rankings
- ✅ Acquisition details (draft, waiver, trade)
- ❌ Owner names
- ❌ Team records
- ❌ Matchup scores

**Use When:**
- You need to see who's on each team
- You want player statistics
- You're building roster management features

**Example Roster Entry:**
```json
{
  "playerId": 4432665,
  "lineupSlotId": 20,
  "acquisitionType": "DRAFT",
  "playerPoolEntry": {
    "player": {
      "id": 4432665,
      "fullName": "Brock Bowers",
      "firstName": "Brock",
      "lastName": "Bowers",
      "defaultPositionId": 4,
      "eligibleSlots": [5, 6, 23, 7, 20, 21],
      "injured": true,
      "injuryStatus": "INJURY_RESERVE"
    }
  }
}
```

---

### 3. `mMatchup` - Matchup View

**Purpose:** Provides matchup schedule with roster snapshots for each game.

**What You Get:**
- ✅ Full season schedule
- ✅ Matchup pairings (home vs away)
- ✅ Rosters for each matchup period
- ✅ Player IDs and names
- ✅ Total points per matchup
- ✅ Winner indication
- ❌ Owner names
- ❌ Detailed player statistics

**Use When:**
- You need historical matchup data
- You want to see lineups from specific weeks
- You're analyzing head-to-head results

**File Size:** ~22 MB (large due to roster snapshots for every matchup)

---

### 4. `mMatchupScore` - Matchup Scoring View

**Purpose:** Provides matchup results with scoring details.

**What You Get:**
- ✅ Matchup scores
- ✅ Points by scoring period
- ✅ Winner indication
- ✅ Detailed stat breakdowns
- ❌ Player names/rosters
- ❌ Owner information

**Use When:**
- You only need scores, not full rosters
- You want a lighter payload than `mMatchup`
- You're building a scoreboard feature

---

### 5. `mStandings` - Standings View

**Purpose:** Provides playoff simulation and standings data.

**What You Get:**
- ✅ Playoff clinch status
- ✅ Simulation results
- ✅ Schedule data
- ❌ Team names/owners (use with `mTeam`)
- ❌ Rosters

**Use When:**
- You need playoff bracket information
- You want simulation/projection data

---

### 6. `mSettings` - League Settings View

**Purpose:** Provides league configuration and scoring settings.

**What You Get:**
- ✅ League name
- ✅ Scoring settings
- ✅ Roster slot configuration
- ✅ Draft settings
- ✅ Trade and waiver settings
- ❌ Team or player data

**Use When:**
- You need to understand league rules
- You're building a league configuration UI

---

### 7. `mStatus` - Status View

**Purpose:** Provides current league status information.

**What You Get:**
- ✅ Current matchup period
- ✅ Latest scoring period
- ✅ League active status
- ✅ Draft status
- ❌ Team or player data

**Use When:**
- You need to know current week/period
- You're checking if the draft is complete

---

## Recommended View Combinations

### Combination 1: `mTeam` + `mRoster`
**Purpose:** Team information with current rosters

**What You Get:**
- ✅ Owner names (display + first/last)
- ✅ Team names, logos, abbreviations
- ✅ Team records and standings
- ✅ Current rosters with player details
- ❌ Matchup history

**Best For:**
- League overview pages
- Team profile pages
- Current standings with rosters

**File Size:** ~21 MB

---

### Combination 2: `mTeam` + `mRoster` + `mStandings`
**Purpose:** Complete team information with playoff data

**What You Get:**
- ✅ Everything from `mTeam` + `mRoster`
- ✅ Playoff clinch status
- ✅ Playoff simulations
- ✅ Historical matchup results

**Best For:**
- Full league dashboard
- Playoff bracket visualization
- Detailed team analysis

**File Size:** ~21 MB

---

### Combination 3: `mMatchup` + `mMatchupScore`
**Purpose:** Complete matchup history with detailed scoring

**What You Get:**
- ✅ All matchups for the season
- ✅ Detailed scoring by stat category
- ✅ Roster snapshots for each week
- ✅ Player performance by week

**Best For:**
- Matchup analysis
- Weekly recaps
- Historical performance tracking

**File Size:** ~28 MB

---

### Full Combination: All Views
**Views:** `mTeam`, `mRoster`, `mStandings`, `mMatchup`, `mMatchupScore`, `mSettings`

**What You Get:**
- ✅ **Everything** - Complete league data

**Best For:**
- Initial data sync
- Comprehensive league analysis
- Building a full-featured fantasy app

**File Size:** ~34 MB

**⚠️ Warning:** Very large payload. Use sparingly and cache aggressively.

---

## Data Availability Matrix

| Data Point | Base | mTeam | mRoster | mMatchup | Team+Roster | Full |
|-----------|------|-------|---------|----------|-------------|------|
| Owner Names | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Owner First/Last | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Team Names | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Team Logos | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Team Records | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Win Rate | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Streak | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Rosters | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Player IDs | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Player Names | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Matchup Scores | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |

---

## Your Original Questions - Answered

### Can I Extract the Following?

1. **Fantasy Owner Names** ✅
   - Use: `mTeam` or `base` endpoint
   - Fields: `members[].displayName`, `members[].firstName`, `members[].lastName`

2. **Fantasy Owner Profile Pictures** ❌
   - **NOT AVAILABLE** in any view tested
   - ESPN does not expose profile pictures via this API

3. **Fantasy Team Record, Win Rate, Streak** ✅
   - Use: `mTeam`
   - Fields: `teams[].record.overall.{wins, losses, ties, percentage, streakType, streakLength}`

4. **Fantasy Rosters** ✅
   - Use: `mRoster` or `mMatchup`
   - Fields: `teams[].roster.entries[]`

5. **Fantasy Player IDs** ✅
   - Use: `mRoster` or `mMatchup`
   - Fields: `teams[].roster.entries[].playerId`

---

## Best Practices

### For Initial Load
```
Use: mTeam + mRoster + mStandings
Reason: Gets all essential data except matchup history
Size: ~21 MB
```

### For Weekly Updates
```
Use: mMatchupScore
Reason: Just scores, no heavy roster data
Size: ~112 KB
```

### For Team Pages
```
Use: mTeam + mRoster
Reason: Team info + current roster
Size: ~21 MB
```

### For Matchup Analysis
```
Use: mMatchup + mMatchupScore (or just mMatchup alone)
Reason: Complete matchup data with lineups
Size: ~22-28 MB
```

---

## API Request Examples

### Python Example
```python
import requests

league_id = "YOUR_LEAGUE_ID"
year = "2025"
espn_s2 = "YOUR_ESPN_S2_COOKIE"
swid = "YOUR_SWID_COOKIE"

# Single view
url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}?view=mTeam"

# Multiple views
url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}?view=mTeam&view=mRoster"

cookies = {
    "swid": swid,
    "espn_s2": espn_s2
}

response = requests.get(url, cookies=cookies)
data = response.json()
```

---

## Notes

- **File sizes** are approximate and will vary by league size and season progress
- **All views** require authentication via cookies for private leagues
- **Public leagues** may not require authentication
- **Rate limiting** may apply - implement appropriate caching
- **Profile pictures** are NOT available through this API endpoint
- **Historical data** from previous seasons can be accessed by changing the `year` parameter

---

## Testing Methodology

This documentation was created by systematically testing:
- Base endpoint (no views)
- 7 individual views
- 4 common view combinations
- 1 full combination with all views

All responses were analyzed programmatically to identify available data fields and structure.

**Test Date:** 2026-01-01
**League Type:** Private
**Season:** 2025
