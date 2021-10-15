from urllib import urlopen
import json

url = urlopen('https://poloniex.com/public?command=returnTicker').read()
result = json.loads(url)

BTC = result['USDT_BTC']['last']
Steem = result['BTC_STEEM']['last']

print "BTC", round(float(BTC),2)
print "Steem", Steem
