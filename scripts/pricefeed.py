import requests as r
import json

result = r.get('https://poloniex.com/public?command=returnTicker').json()

BTC = result['USDT_BTC']['last']

print("BTC:${} ".format(round(float(BTC))))
