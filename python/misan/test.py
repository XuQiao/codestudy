<<<<<<< HEAD
import numpy as np
import random
wokp=[0]*1000
def make1Step(oldList):
    #newList = oldList.copy()
    newList = list(oldList)
    for i in range(len(oldList)):
        flag = random.random()
        if flag > 0.5:
            newList[i] = oldList[i] + 1
        else:
            newList[i] = oldList[i] - 1
    return newList
def congen(shock):
    gen=[100]*len(shock)
    for i in range(len(shock)-1):
        gen[i+1]=gen[i]+shock[i]
    return gen

def annatrans(semidat):
    trans=[0]*(500)
    for i in range(len(trans)):
        trans[i]=semidat[i*2-1]+semidat[i*2]
    return trans
def delta(yeardat):
    change=[0]*(len(yeardat)-1)
    for i in range(len(change)):
        change[i]=yeardat[i+1]-yeardat[i]
    return change
c1=make1Step(wokp)
csy=congen(c1)
cy=annatrans(csy)
deltacy=np.array(delta(cy))
y1=make1Step(wokp)
ysy=congen(y1)
yy=annatrans(ysy)
deltayy=np.array(delta(yy))
A=np.vstack([deltayy,np.ones(len(deltayy))]).T
m=np.linalg.lstsq(A,deltacy)[0]
m
print m
=======
import matplotlib.pyplot as plt
from pprint import pprint
from okex.client import OkexClient, OkexTradeClient, OKexFuture

proxies = {
#    'http': 'socks5h://127.0.0.1:1080',
#    'https': 'socks5h://127.0.0.1:1080'
}

client = OkexClient(None, None, proxies)

symbol = 'btc_usdt'

tickers = client.ticker(symbol)
trades = client.trades(symbol,since_tid=7622718804)
depths = client.depth(symbol,size=3)
kline15min = client.kline(symbol,type='15min',size=3)

#api_key = 'a43d3588-1630-4ae9-b406-df03dc926e5d'
#secret_key = '93B884AD49BBA50A17490CA9D8DAEF94'

#authClient = OkexTradeClient(api_key, secret_key, proxies=proxies)
#balances = authClient.balances()

#history = authClient.history('btc_usdt', 1, 500)

pprint(tickers)
pprint(trades)
pprint(depths)
pprint(kline15min)
#pprint(balances)
#pprint(history)

symbol = 'btc_usd'
contractType = 'next_quarter'

Futureclient = OKexFuture(None, None)
fkline15min = Futureclient.future_kline(symbol,type='15min',contractType=contractType,size=3)
pprint(fkline15min)
>>>>>>> 69d8500eba6fefb339f8d2ecebdb1c25ae3461bd
