import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint
from okex.client import OkexClient, OkexTradeClient, OKexFuture
import time

client = OkexClient(None, None)

symbol = 'btc_usd'

while True:
    tickers = client.ticker('btc_usdt')
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

    with open('data/'+symbol+'_ticker_spot.csv','a') as f:
        df.to_csv(f, header=False)

    time.sleep(1)
