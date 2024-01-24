import requests
import json

base_site = "https://itunes.apple.com/search"
r = requests.get(base_site, params = {"term": "michael jackson", "country": "pl", "limit": 20})

#print (r.status_code)
info = r.json()
#print(json.dumps(info['results'][0], indent=4))

info['results'][0]['trackName']
info['results'][0]['releaseDate']

for result in info['results']:
    print(result['trackName'])

for result in info['results']:
    print(result['releaseDate'])