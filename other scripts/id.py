import requests
import json

url = ('https://api.coingecko.com/api/v3/coins/cardano/history?date=12-12-2021&localization=false')


get = requests.get(url).text
get = json.loads(get)
print(get)
