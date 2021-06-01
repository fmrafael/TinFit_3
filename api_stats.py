import os 
import requests
from datetime import datetime


API_KEY_STATS = os.environ['API_KEY_STATS']

url = "https://api-football-beta.p.rapidapi.com/fixtures"

querystring = {"league":"71","season":"2021", "next":"10","round":"Regular Season - 2"}

headers = {
    'x-rapidapi-key': API_KEY_STATS,
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com"
    }

data_stats = requests.request("GET", url, headers=headers, params=querystring).json()['response']

 
round_date = [datetime.strptime(teams['fixture']['date'][:10],'%Y-%m-%d').strftime('%d/%m/%Y') for teams in data_stats]
 
 
round_name_home = [teams['teams']['home']['name'] for teams in data_stats]
round_logo_home = [teams['teams']['home']['logo'] for teams in data_stats]
round_name_away = [teams['teams']['away']['name'] for teams in data_stats]
round_logo_away = [teams['teams']['away']['logo'] for teams in data_stats]

