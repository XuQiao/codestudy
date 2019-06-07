import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint
from okex.client import OkexClient, OkexTradeClient, OKexFuture
import time

symbol = 'btc_usd'
contractType = 'next_quarter'

types = ['1min','5min','15min', '30min','1hour','2hour','4hour','6hour','12hour','1day','3day','1week']
MAX_SIZE=6000

while True:
    for type in types:
        Futureclient = OKexFuture(None, None)


        tickers = Futureclient.future_ticker(symbol,contractType,type)
        ticker = tickers['ticker']

        date = tickers['date']
        buy = ticker['buy']
        high = ticker['high']
        last = ticker['last']
        low = ticker['low']
        sell = ticker['sell']
        vol = ticker['vol']

        df = pd.DataFrame(ticker,index=pd.Series(date))
        df.index.name = 'date'

        with open('data/'+symbol+'_ticker_future.csv','a') as f:
            df.to_csv(f, header=False)

        time.sleep(1)
