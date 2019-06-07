import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint
from okex.client import OkexClient, OkexTradeClient, OKexFuture
import time
from datetime import datetime
from multiprocessing import Process
from constants import *
import os
from func import *

def pullfuturekline():
    client = OkexClient(None, None)
    columns = ['date','open','high','low','close','unknown','volume']

    now = datetime.now()
    now = time.mktime(now.timetuple())

    #time = now - 40 * 3600
    def UpdateFutureKline(i):
        type = types[i]
        typesize = typesizes[i]
        refreshtime = refreshtimes[i] * typesize

    #    while True:
        Futureclient = OKexFuture(None, None)

        fkline = Futureclient.future_kline(symbol,type=type,contractType=contractType,size=MAX_SIZE)
        df = pd.DataFrame(fkline,columns=columns)
    #    df.index.name = 'date'
        filename = 'data/'+symbol+'_'+type+'_'+contractType+'_future.csv'

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                df_curr=pd.read_csv(f, header=None,index_col=0)
                df_curr.columns = columns

                lastdate = df_curr.iloc[-1]['date']
                print type, convert_to_localtime(lastdate/1000), refreshtime/1000./3600, 'hours' , convert_to_localtime(df.iloc[-1]['date']/1000), convert_to_localtime(now)

                df = df[df['date'] > lastdate]
                if not df.empty:
                    sleeptime = refreshtime
                    df_concat = pd.concat([df_curr,df], ignore_index=True)
                    assert(df_concat.iloc[0]['date'] == df_curr.iloc[0]['date'])
                    assert(df_concat.iloc[0]['date'] <= df.iloc[0]['date'])
                    assert(df_concat.iloc[-1]['date'] >= df_curr.iloc[-1]['date'])
                    assert(df_concat.iloc[-1]['date'] == df.iloc[-1]['date'])

                    with open(filename, 'w') as f:
                        df_concat.to_csv(f, header=False)

                else:
                    sleeptime = lastdate + refreshtime - now

    for m in range(len(types)):
        UpdateFutureKline(m)

    #    time.sleep(sleeptime / 2 / 1000)

    #processes = []

    #for m in range(len(types)):
    #    p = Process(target=UpdateFutureKline, args=(m,))
    #    p.start()
    #    processes.append(p)

    #for p in processes:
    #       p.join()

