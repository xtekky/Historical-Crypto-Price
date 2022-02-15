import requests
import json



with open('crypto.txt') as f:
    mylist = f.read().splitlines()
date = '01-01_2021'
num = 0
z =1
while z == 1:
    list = (mylist[num])
    url = ('https://api.coingecko.com/api/v3/coins/' + list + '/history?date=01-01-2021&localization=false')
    get = requests.get(url).text
    get = json.loads(get)
    print(get)
    num = num+1
    if num > 17:
        z = 2
