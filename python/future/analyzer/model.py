from datetime import datetime
import time
import stockstats as ss
import numpy as np
import pandas as pd
from okex.client import OkexClient, OkexTradeClient, OKexFuture
from constants import *
from func import *
import xgboost as xgb
import pickle

def model(startday):
    df = pd.read_csv('data/btc_usd_full_next_quarter_future.csv','r',delimiter='\t',index_col=0)
    df_spot = pd.read_csv('data/btc_usd_full_spot.csv','r',delimiter='\t',index_col=0)
    df_matrix = pd.read_csv('data/btc_usd_matrix_full_next_quarter_future.csv','r',delimiter='\t',index_col=0)
    df.columns = ['date','open','high','low','close','unknown','volume']

    now = datetime.now()
    now = time.mktime(now.timetuple())
    Futureclient = OKexFuture(None, None)
    client = OkexClient(None, None)

    def pullfutureticker():
        tickers = Futureclient.future_ticker(symbol,contractType,type)
        ticker = tickers['ticker']
        date = tickers['date']

        buy = ticker['buy']
        high = ticker['high']
        last = ticker['last']
        low = ticker['low']
        sell = ticker['sell']
        vol = ticker['vol']
        ticker['date'] = date
        ticker['open'] = (buy + sell)/2

        now_ticker = pd.DataFrame(ticker,index=[0])
        now_ticker.set_index('date')
        now_ticker = now_ticker[['date','open','high','low','last','vol']]
        now_ticker.columns = df.columns
        return now_ticker

    def pullfuturekline(type):
        fkline = Futureclient.future_kline(symbol,type=type,contractType=contractType,size=MAX_SIZE)
       # columns = ['date','open','high','low','close','unknown','volume']
        now_kline = pd.DataFrame(fkline,columns=df.columns)
       # now_kline = now_kline.drop('unknown',axis = 1)
       # now_kline.columns = df.columns
        return now_kline

    def pullspotkline(type):
        if type == '3day':
            return
        kline = client.kline(symbol+'t', type=type)
        now_kline = pd.DataFrame(kline,columns=['date','open','high','low','close','volume'])
        return now_kline

#    t0 = time.time()

    now_dfs = []
    now_dfs_spot = []
    for type in types:
        now_df = pullfuturekline(type)
        now_df_spot = pullspotkline(type)
        now_dfs.append(now_df)
        now_dfs_spot.append(now_df_spot)
    now_df = pd.concat(now_dfs, ignore_index=True)
    now_df_spot = pd.concat(now_dfs_spot, ignore_index=True)
    now_df['date'] = now_df['date'] / 1000
    now_df_spot['date'] = now_df_spot['date'] / 1000
    lastdate = df.at[df.index[-1], 'date']
    lastdate_spot = df_spot.at[df_spot.index[-1], 'date']

    now_df = now_df[now_df['date'] > lastdate]
    now_df_spot = now_df_spot[now_df_spot['date'] > lastdate_spot]

    df_concat = pd.concat([df, now_df],ignore_index=True)
    df_concat_spot = pd.concat([df_spot, now_df_spot],ignore_index=True)

  #  df.drop_duplicates(['date','close'], take_first=True)
    df_concat = df_concat.sort_values('date')
    df_concat = df_concat.reset_index(drop=True)
    df_concat_spot = df_concat_spot.sort_values('date')
    df_concat_spot = df_concat_spot.reset_index(drop=True)

    df_concat.to_csv('data/'+symbol+'_fulltemp_'+contractType+'_future.csv',sep='\t')
    df_concat_spot.to_csv('data/'+symbol+'_fulltemp_'+'spot.csv',sep='\t')

    df_matrix = df_matrix.sort_values('date')
    df_matrix = df_matrix.reset_index(drop=True)

    lastdate = df_matrix.at[df_matrix.index[last_nonnan(df_matrix['flag'])], 'date']
    startindex = df_concat['date'].searchsorted(lastdate)[0]
    startindex1 = df_matrix['date'].searchsorted(lastdate)[0]
#    train_time = time.time() - t0
#    print("pre-process time: %0.3fs" % train_time)
#    t0 = time.time()
    df_update = calcTA(df=df_concat,startindex=0)

#    df_update = pd.concat([df_matrix.iloc[:startindex1], df_update.iloc[startindex:]],ignore_index=True)
#    t0 = time.time()
    df_update = df_update.sort_values('date')
    df_update = df_update.reset_index(drop=True)
    df_update.to_csv('data/'+symbol+'_matrix_fulltemp_'+contractType+'_future.csv',sep='\t')
    lastdate = df_update.at[df_update.index[-1],'date']

    startindex = df_update['date'].searchsorted(now - startday * 24 * 3600)[0]
    X = df_update.iloc[startindex:]
    X_copy = X.drop(['date','flag','open','high','low','close'],axis = 1)

    result = pd.DataFrame({'date':X['date'], 'close':X['close']})
    for model in models:
        filename = 'data/btc_full_next_quarter_'+model+'.sav'
        clf = pickle.load(open(filename, 'rb'))

        if model == 'XGB':
            xgtest2 = xgb.DMatrix(X_copy)
            pred_prob = clf.predict(xgtest2, ntree_limit = clf.best_ntree_limit)
            prob = map(lambda x: x[1]-x[0], pred_prob)
            pred = pd.DataFrame(pred_prob).idxmax(axis=1)
            mapping_dict = {0:-1, 1:1}
            pred = pred.map(mapping_dict).values
        else:
            pred = clf.predict(X_copy)
            pred_prob = clf.predict_proba(X_copy)
            prob = map(lambda x: x[1]-x[0], pred_prob)

        result['flag_'+model] = pred
        result['prob_'+model] = prob

#    train_time = time.time() - t0
#    print("apply time: %0.3fs" % train_time)
#    t0 = time.time()

    def back_test_spot(start, end=9999999999999, df=df, string='',model='_RF'):
        money = init_money
        btc = init_btc
        fmoney = []
        bmoney = []
        timearr = []
        time = start
        while time < end:
            index = df['date'].searchsorted(time)[0]
            index_f = result['date'].searchsorted(time)[0]
            price = result.at[result.index[index_f],'close']
            #df_future = pd.read_csv('data/btc_usd_full_next_quarter_future.csv','r',delimiter='\t', index_col=None)
            #ice = get_price(time, df_future)
            flag = df.at[df.index[index],'flag'+model]
            if 'prob' in df.columns:
                prob = df.at[df.index[index],'prob'+model]
            else:
                prob = flag
            #if flag == -1:
            if prob < -build_point:
                btc += money / price
                money = 0
            #elif flag == -1:
            elif prob > build_point:
                money += btc * price
                btc = 0
            fmoney.append(money + btc * price)
            bmoney.append(btc + money / price)
            timearr.append(time)
            time += 15 * 60
        test = pd.DataFrame({'date': timearr, 'fiat_'+string: fmoney,'btc_'+string: bmoney})
        return test

    def back_test_future(start, end=9999999999999, df=df, string='',beta=0.1, leverage = 20, model = '_RF'):
        money = init_money
        btc = init_btc
        holdbtc = 0
        df_future = pd.read_csv('data/btc_usd_full_next_quarter_future.csv','r',delimiter='\t', index_col=0)
        btc += money / get_price(start, df_future)
        liquidbtc = btc
        money = 0
        time = start
        bmoney = []
        fmoney = []
        liqbtcs = []
        holdbtcs = []
        timearr = []
        statuses = []
        positions = []
        longpositions = []
        longamounts = []
        shortpositions = []
        shortamounts = []
        btcs = []
        while time < end:
            index = df['date'].searchsorted(time)[0]
            index_f = result['date'].searchsorted(time)[0]
            price = result.at[result.index[index_f],'close']
            flag = df.at[df.index[index],'flag'+model]
            if 'prob' in df.columns:
                prob = df.at[df.index[index],'prob'+model]
            else:
                prob = flag
            #if flag == 1:
            amount = liquidbtc * np.random.uniform(0,beta)
            if prob < -build_point and 2.5*beta*(liquidbtc-amount) > (holdbtc+amount): # long
                liquidbtc -= amount
                holdbtc += amount
                btc += amount * leverage
                money -= price * amount * leverage
                statuses.append((price,amount))

            #elif flag == -1:
            elif prob > build_point and 2.5*beta*(liquidbtc-amount) > (holdbtc+amount): # short
                liquidbtc -= amount
                holdbtc += amount
                btc -= amount * leverage
                money += price * amount * leverage
                statuses.append((-price,amount))

            for status in statuses[:]:
                if price > (1+1./leverage) * abs(status[0]) or price < (1-1./leverage) * abs(status[0]):
                    if status[0] > 0:   # close long
                        btc -= status[1] * leverage
                        money += price * status[1] * leverage
                        liquidbtc += status[1] + (price - abs(status[0])) * status[1] * leverage / price
                        holdbtc -= status[1]
                    else: # close short
                        btc += abs(status[0]) * status[1] * leverage / price
                        liquidbtc += status[1] + (abs(status[0]) - price) * status[1] * leverage / price
                        holdbtc -= status[1]
                        money -= abs(status[0]) * status[1] * leverage

                    statuses.remove(status)

            longpositions.append(sum([x[0] * x[1] for x in statuses if x[0] > 0])/sum([x[1] for x in statuses if x[0] > 0]) if sum([x[1] for x in statuses if x[0] > 0])>0 else 0)
            shortpositions.append(sum([x[0] * x[1] for x in statuses if x[0] < 0])/sum([x[1] for x in statuses if x[0] < 0]) if sum([x[1] for x in statuses if x[0] < 0])>0 else 0)
            longamounts.append(sum([x[1] for x in statuses if x[0] > 0]))
            shortamounts.append(sum([x[1] for x in statuses if x[0] < 0]))

            fmoney.append(btc * price + money)
            bmoney.append(btc + money / price)
            liqbtcs.append(liquidbtc)
            holdbtcs.append(holdbtc)
            timearr.append(time)
            positions.append(statuses)

            if btc * price + money < 0:
                break

            time += 15 * 60
        test = pd.DataFrame({'date': timearr, 'fiat_'+string: fmoney,'btc_'+string+model: bmoney, 'longposition':longpositions, 'shortposition':shortpositions, 'longamount':longamounts, 'shortamount': shortamounts,'liqbtc': liqbtcs,'holdbtc': holdbtcs, 'positions': positions})
        return test

    starttime = now - startday * 24 * 3600
    endtime = lastdate
    spot = back_test_spot(starttime, endtime, result, 'spot_back',model='_RF')
    spot_hist = back_test_spot(starttime, endtime, df_update, 'spot_hist',model='')
    future = back_test_future(starttime, endtime, result, 'future_back',model='_RF')
    future_XGB = back_test_future(starttime, endtime, result, 'future_back',model='_XGB')
    future_hist = back_test_future(starttime, endtime, df_update, 'future_hist',model='')
    future_hist = future_hist.drop(['longposition','shortposition','longamount','shortamount','liqbtc','holdbtc','positions'],axis=1)
    future_XGB = future_XGB.iloc[:]['btc_future_back_XGB']
    test = pd.concat([spot, spot_hist, future, future_hist, future_XGB], axis=1, join='outer')
#    test['date'] = test['date'].apply(lambda x:convert_to_localtime(x))

    test.to_csv('data/'+symbol+'_back_'+contractType+'_future.csv',sep='\t')
    result.to_csv('data/'+symbol+'_pred_'+contractType+'_future.csv',sep='\t')
#    train_time = time.time() - t0
#    print("model time: %0.3fs" % train_time)
    return test
