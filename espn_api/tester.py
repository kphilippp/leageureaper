import requests
import os
# since .env is in the root directory, we can load it like this
from dotenv import load_dotenv
load_dotenv()
# for clean readablility
import json

league_id = os.getenv("LEAGUE_ID")
team_id = os.getenv("TEAM_ID")
year = os.getenv("YEAR")
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")


# BASIC GET REQUEST TO FETCH LEAGUE DATA
# url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}"
# cookies = {
#     "swid": swid,
#     "espn_s2": espn_s2
# }

# response = requests.get(url, cookies=cookies)
# print(json.dumps(response.json(), indent=4))

# REQUEST WITH VIEWS
views=[
    "mMatchup",
    "mMatchupScore",
    "mTeam",
    "mSettings",
    "mStandings"
    "mStatus",
    "mRoster",
    "mNav"
]
url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}"
for view in views:
    url += f"?view={view}"
    if view != views[-1]:
        url += "&"
cookies = {
    "swid": swid,
    "espn_s2": espn_s2
}

response = requests.get(url, cookies=cookies)
with open('league_data.json', 'w') as f:
    f.write(json.dumps(response.json(), indent=4))