from urllib import urlopen
import json

url = urlopen('https://poloniex.com/public?command=returnTicker').read()
result = json.loads(url)

SBD = result['BTC_SBD']['last']
BTC = result['USDT_BTC']['last']
Steem = result['BTC_STEEM']['last']
SBD_USD = float(SBD) * float(BTC)

print "BTC", round(float(BTC),2)
print "Steem", Steem
print "SBD", '{0:.2f}'.format(SBD_USD)
