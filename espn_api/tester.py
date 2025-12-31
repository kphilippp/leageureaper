import requests
import os
# since .env is in the root directory, we can load it like this
from dotenv import load_dotenv
load_dotenv()

league_id = os.getenv("LEAGUE_ID")
team_id = os.getenv("TEAM_ID")
year = os.getenv("YEAR")
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")

url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}"
cookies = {
    "swid": swid,
    "espn_s2": espn_s2
}

response = requests.get(url, cookies=cookies)
print(response.json())