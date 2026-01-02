import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

league_id = os.getenv("LEAGUE_ID")
team_id = os.getenv("TEAM_ID")
year = os.getenv("YEAR")
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

def fetch_league_data(views=None, output_filename=None):
    """
    Fetch ESPN Fantasy Football league data with optional views.

    Args:
        views: List of view strings or None for base endpoint
        output_filename: Name for output JSON file
    """
    base_url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}"

    if views:
        view_params = "&".join([f"view={view}" for view in views])
        url = f"{base_url}?{view_params}"
    else:
        url = base_url

    cookies = {
        "swid": swid,
        "espn_s2": espn_s2
    }

    print(f"Fetching: {output_filename}")
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        with open(output_filename, 'w') as f:
            json.dump(response.json(), indent=4, fp=f)
        print(f"[SUCCESS] Saved {output_filename}")
    else:
        print(f"[ERROR] Status {response.status_code} for {output_filename}")

    return response.status_code == 200

# Test configurations
test_configs = [
    # Base endpoint (no views)
    (None, "sample_data/base_no_views.json"),

    # Individual views
    (["mMatchup"], "sample_data/view_mMatchup.json"),
    (["mMatchupScore"], "sample_data/view_mMatchupScore.json"),
    (["mTeam"], "sample_data/view_mTeam.json"),
    (["mSettings"], "sample_data/view_mSettings.json"),
    (["mStandings"], "sample_data/view_mStandings.json"),
    (["mRoster"], "sample_data/view_mRoster.json"),
    (["mStatus"], "sample_data/view_mStatus.json"),

    # Common combinations
    (["mTeam", "mRoster"], "sample_data/combined_team_roster.json"),
    (["mMatchup", "mMatchupScore"], "sample_data/combined_matchup_scores.json"),
    (["mTeam", "mStandings"], "sample_data/combined_team_standings.json"),
    (["mTeam", "mRoster", "mStandings"], "sample_data/combined_team_roster_standings.json"),

    # Full combination for complete data
    (["mMatchup", "mMatchupScore", "mTeam", "mRoster", "mStandings", "mSettings"], "sample_data/full_combined.json"),
]

print("=" * 60)
print("ESPN Fantasy API View Testing")
print("=" * 60)

for views, filename in test_configs:
    fetch_league_data(views, filename)
    print()

print("All tests completed!")