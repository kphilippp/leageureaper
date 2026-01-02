# API Basic Response Summary

## League Info
- Game ID: 1
- League ID: 564613067
- Season: 2025
- Scoring Period: 18
- Current Matchup Period: 17
- League Active: True
- League Name: mtcfb

## Members (players/managers)
1. ESPNFAN8963221637 (not manager)
2. AdamMatt6 (not manager)
3. ESPNfan6319703923 (not manager)
4. espnfan4977240100 (not manager)
5. espnfan5474312026 (not manager)
6. ESPNFAN2013252092 (not manager)
7. espnfan5382939783 (not manager)
8. ESPNfan6636257426 (not manager)
9. ESPNFAN4845332233 (not manager)
10. ESPNfan5181402610 (not manager)
11. ESPNFAN8465621163 (not manager)
12. ESPNfan4731240631 (not manager)

## Teams
1. $$$ — Owner: espnfan5474312026
2. DAL — Owner: espnfan5382939783
3. SHT — Owner: ESPNfan4731240631
4. AMAT — Owner: AdamMatt6
5. KPK — Owner: ESPNFAN2013252092
6. 1 — Owner: ESPNfan6319703923
7. win — Owner: ESPNFAN8465621163
8. $$$ — Owner: ESPNfan5181402610
9. DDT — Owner: espnfan4977240100
10. NOA — Owner: ESPNFAN8963221637
11. 🐐 — Owner: ESPNfan6636257426
12. FYC — Owner: ESPNFAN4845332233




# Views
- Views are what you can use to get different information from the API


### Syntax Rules
- First view uses `?view=`
- Additional views use `&view=`
- View names are case-sensitive
- Multiple views are separated by `&`

---

## Available Views

### Core League Data

| View Name     | Description          | What You Get                                 |
|---------------|----------------------|---------------------------------------------|
| `mTeam`       | Basic team information | Team names, IDs, owners, abbreviations      |
| `mRoster`     | Complete team rosters | All players on each team, starting lineup, bench |
| `mMatchup`    | Weekly matchups       | Current week's games, scores, matchup details |
| `mMatchupScore` | Detailed matchup scoring | Individual player scores within matchups    |
| `mSchedule`   | Full season schedule  | All matchups for every week                   |
| `mStandings`  | League standings      | Win/loss records, points for/against, rankings |

### League Configuration

| View Name      | Description         | What You Get                               |
|----------------|---------------------|-------------------------------------------|
| `mSettings`    | League settings     | Scoring rules, roster positions, playoff settings |
| `mDraftDetail` | Draft information   | Draft picks, order, keeper selections     |
| `mLiveScoring` | Live scoring data   | Real-time scoring during games             |

### Player Information

| View Name       | Description          | What You Get                              |
|-----------------|----------------------|------------------------------------------|
| `kona_player_info` | Detailed player data | Player stats, news, outlooks, ownership % |
| `player_wl`       | Player watch list     | Players on team watch lists               |

## Transactions

| View Name | Description | What You Get |
|----------|------------|--------------|
| `mPendingTransactions` | Pending actions | Pending trades, waiver claims not yet processed |
| `mTransactions` | Transaction history | All completed adds, drops, trades |
| `mTransactions2` | Enhanced transactions | More detailed transaction data |

---

## Advanced / Specialized

| View Name | Description | What You Get |
|----------|------------|--------------|
| `mBoxscore` | Individual boxscores | Player-by-player scoring breakdown |
| `mScoreboard` | Scoreboard view | Overview of all matchups with scores |
| `mStatus` | League status | Current state, active periods, status flags |
| `mNav` | Navigation data | UI navigation elements (less useful for API) |
| `modular` | Modular data | Combined view for web interface |
| `mTeams` | Teams collection | Similar to `mTeam` but different structure |

---

## Most Commonly Used Views

For most fantasy applications, you’ll primarily use these:

### Essential 4

1. **`mRoster`** – Get all players on all teams  
2. **`mMatchup`** – Get current week matchups and scores  
3. **`mSettings`** – Get league scoring rules and settings  
4. **`mStandings`** – Get win/loss records  
