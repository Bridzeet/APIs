import requests
import json
import pandas as pd

base_site = "https://itunes.apple.com/search"
r = requests.get(base_site, params = {"term": "michael jackson", "country": "pl", "limit": 20})
print (r.status_code)

info = r.json()
len(info['results'])


info['results'][0]['trackName']
info['results'][0]['releaseDate']

for result in info['results']:
    print(result['trackName'])

for result in info['results']:
    print(result['releaseDate'])


songs_df = pd.DataFrame(info["results"])
print(songs_df)
