import requests
import json

status = 0

with open('crypto.txt') as f:
    mylist = f.read().splitlines()
date = '01-01_2021'
date1 = '31-12-2021'
num = 0
try:
    while status == 0:
        list = (mylist[num])
        url = ('https://api.coingecko.com/api/v3/coins/' + list + '/history?date=01-01-2021&localization=false')
        get = requests.get(url).text
        get = json.loads(get)
        print('-----------------------------------------------------')
        print('')
        print('price of ' + list + ' ' + date + ': ', get['market_data']['current_price']['usd'])
        print('MarketCap of ' + list + ' ' + date + ': ', get['market_data']['market_cap']['usd'])
        b = (get['market_data']['current_price']['usd'])

        url = ('https://api.coingecko.com/api/v3/coins/' + list + '/history?date=31-12-2021&localization=false')
        get = requests.get(url).text
        get = json.loads(get)
        print('price of ' + list + ' ' + date1 + ': ', get['market_data']['current_price']['usd'])
        print('MarketCap of ' + list + ' ' + date1 + ': ', get['market_data']['market_cap']['usd'])
        a = (get['market_data']['current_price']['usd'])
        print('Percentage: ', (a/b)*100, '%')
        print('')
        num = num+1
        if num > 15:
            status = 1
except:
    print('ERROR - VERIFY CODE')
    exit()

print('Credits to github.com/xtekky')
