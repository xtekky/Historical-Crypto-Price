from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
list = cg.get_coins_list()
print(list)

