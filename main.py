import requests
import json
from colorama import Fore, Back, Style

print(Fore.RED+Style.BRIGHT+'''
      ___           ___           ___           ___           ___           ___     
     |\__\         /\  \         /\  \         /\__\         /\__\         |\__\    
     |:|  |        \:\  \       /::\  \       /:/  /        /:/  /         |:|  |   
     |:|  |         \:\  \     /:/\:\  \     /:/__/        /:/__/          |:|  |   
     |:|__|__       /::\  \   /::\~\:\  \   /::\__\____   /::\__\____      |:|__|__ 
 ____/::::\__\     /:/\:\__\ /:/\:\ \:\__\ /:/\:::::\__\ /:/\:::::\__\     /::::\__|
 \::::/~~/~       /:/  \/__/ \:\~\:\ \/__/ \/_|:|~~|~    \/_|:|~~|~       /:/~~/~   
  ~~|:|~~|       /:/  /       \:\ \:\__\      |:|  |        |:|  |       /:/  /     
    |:|  |       \/__/         \:\ \/__/      |:|  |        |:|  |       \/__/      
    |:|  |                      \:\__\        |:|  |        |:|  |                  
     \|__|   github.com/xtekky   \/__/         \|__|         \|__|                  
''')

coin = input(str(Fore.BLUE+'coin (bitcoin, ethereum etc...): '))
date = input(Fore.BLUE+'date (dd-mm-yyyy): ')
curr = input(str(Fore.BLUE+'currency (eur, usd etc...): '))

url = ('https://api.coingecko.com/api/v3/coins/'+coin+'/history?date='+date+'&localization=false')

try:
    get = requests.get(url).text
    get = json.loads(get)
    print(Fore.WHITE+'price of '+coin+' '+date+': ', get['market_data']['current_price'][curr], curr)
    print(Fore.WHITE+'MarketCap of '+coin+' '+date+': ', get['market_data']['market_cap'][curr], curr)
except:
    print('')
    print(Fore.RED+'ERROR 404 - check inputs...')
    exit()
