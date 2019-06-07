import numpy as np
import pandas as pd
from datetime import datetime
from dateutil import tz
import time
from constants import *
import stockstats as ss
import talib.abstract
from talib.abstract import *

df_future = pd.read_csv('data/btc_usd_fulltemp_next_quarter_future.csv','r',delimiter='\t', index_col=0)
df_spot = pd.read_csv('data/btc_usd_fulltemp_spot.csv','r',delimiter='\t', index_col=0)

def calcfi_back(time, stockdata,startindex,alpha=alpha, t0=t0): # first reach up alpha% or down alpha%
    dates = np.array(stockdata['date'])
    prices = np.array(stockdata['close'])

    index = dates.searchsorted(time)

    if index < startindex:
        return np.nan

    price = prices[index]
    index_f, price_f = next(((i,v) for i,v in enumerate(prices[index:]) if v >= price * (1+alpha) or v <= price * (1-alpha)),(0, 0))
    if dates[index_f+index] - time > t0:
        flag = np.nan
    elif price_f == 0 or index >= stockdata.shape[0] - 1:
        flag = np.nan
    elif price_f > price:
        flag = -1
    elif price_f < price:
        flag = 1
    else:
        flag = np.nan
#    if time_f - time > t0:
#        lag_hours = (time_f - time) / 3600
#        flag = 0
    return flag

def calcfi(stockdata, startindex = 0, alpha=alpha, t0=t0): # first reach up alpha% or down alpha%
    dates = stockdata['date']
    prices = stockdata['close']
    flags = [0] * startindex
    lag_hours = [0] * startindex

    for index in range(startindex, len(dates)):
        date = dates.iat[index]
        price = prices.iat[index]
        flag = 0
        date_f = date
        for index_f in range(index+1, len(dates)):
            date_f = dates.iat[index_f]
            price_f = prices.iat[index_f]
            if price_f >= price * (1 + alpha):
                flag = -1 # should buy
                break
            if price_f <= price * (1 - alpha):
                flag = 1 # should sell
                break
            if date_f - date > t0: #too long so hold
                break
        lag_hour = (date_f - date) / 3600
        if index_f == len(dates)-1:
            flag = np.nan
        flags.append(flag)
#        lag_hours.append(lag_hour)
    return flags

def calcfi_TAlib(df_matrix, df):
    df_matrix[['UPPERBAND','MIDDLEBAND','LOWERBAND']] = BBANDS(df, timeperiod=15, nbdevup=10, nbdevdn=10, matype=0)[['upperband','middleband','lowerband']]
 #   df_matrix['DEMA'] = DEMA(df, timeperiod=30)
 #   df_matrix['EMA'] = EMA(df, timeperiod=30)
    df_matrix['HT_TREADLINE'] = HT_TRENDLINE(df)
    df_matrix['KAMA'] = KAMA(df, timeperiod=30)
    df_matrix['MA'] = MA(df, timeperiod=30)
 #   df_matrix['WMA'] = WMA(df, timeperiod=30)
 #   df_matrix['MIDPOINT'] = MIDPOINT(df, timeperiod=30)
    df_matrix['SAR'] = SAR(df, accerleration=0, maximum=0)
    df_matrix['ADX'] = ADX(df, timeperiod=30)
    df_matrix['ADXR'] = ADXR(df, timeperiod=30)
    df_matrix['APO'] = APO(df, fastperiod=28, slowperiod=46, matype=0)
    df_matrix[['AROONDOWN','AROONUP']] = AROON(df, timeperiod=30)[['aroondown','aroonup']]
    df_matrix['AROONOSC'] = AROONOSC(df, timeperiod=30)
    df_matrix['BOP'] = BOP(df, timeperiod=30)
    df_matrix['CCI'] = CCI(df, timeperiod=30)
    df_matrix['CMO'] = CMO(df, timeperiod=30)
    df_matrix['DX'] = DX(df, timeperiod=30)
    df_matrix[['MACD','MACDSignal','MACDHIST']]= MACD(df, fastperiod=30, slowperiod=50, signalperiod=18)[['macd', 'macdsignal', 'macdhist']]
   # df_matrix[['MACDEXT','MACDSignalEXT','MACDHISTEXT']]= MACD(df, fastperiod=12, slowperiod=26, signalperiod=9, signalmatype=0)[['macd', 'macdsignal', 'macdhist']]
   # df_matrix[['MACDFIX','MACDSignalFIX','MACDHISTFIX']]= MACD(df, signalperiod=9)[['macd', 'macdsignal', 'macdhist']]
    df_matrix['MFI'] = MFI(df, timeperiod=30)
    df_matrix['MINUS_DI'] = MINUS_DI(df, timeperiod=30)
    df_matrix['MINUS_DM'] = MINUS_DM(df, timeperiod=30)
    df_matrix['MOM'] = MOM(df, timeperiod=20)
    df_matrix['PLUS_DI'] = PLUS_DI(df, timeperiod=30)
    df_matrix['PLUS_DM'] = PLUS_DM(df, timeperiod=30)
    df_matrix['PPO'] = PPO(df, fastperiod=12, slowperiod=26, matype=0)
    df_matrix['ROCP'] = ROCP(df, timeperiod=20)
    df_matrix['RSI'] = RSI(df, timeperiod=30)
    df_matrix[['SLOWK','SLOWD']] = STOCH(df, fastk_period=15, slowk_period=13, slowk_matype=0, slowd_period=13, slowd_matype=0)[['slowk','slowd']]
    df_matrix[['FASTK','FASTD']] = STOCHF(df, fastk_period=15, fastd_period=13, fastd_matype=0)[['fastk','fastd']]
    df_matrix[['FASTKRSI','FASTDRSI']] = STOCHRSI(df, timeperiod=14, fastk_period=15, fastd_period=13, fastd_matype=0)[['fastk','fastd']]
    df_matrix['TRIX'] = TRIX(df, timeperiod=30)
    df_matrix['ULTOSC'] = ULTOSC(df, timeperiod1=15, timeperiod2=30, timeperiod3=40)
    df_matrix['WILLR'] = WILLR(df, timeperiod=30)
    df_matrix['AD'] = AD(df)
    df_matrix['ADOSC'] = ADOSC(df, fastperiod=13, slowperiod=20)
    df_matrix['OBV'] = OBV(df, timeperiod=30)
    df_matrix['ATR'] = ATR(df, timeperiod=30)
    #df_matrix['NATR'] = NATR(df, timeperiod=30)
    df_matrix['TRANGE'] = TRANGE(df)

#    for indicator in indicators_TALIB:
#        df_matrix[indicator] = getattr(talib.abstract, indicator)(df)

def last_nonnan(array):
    for index in range(len(array)):
        if np.isnan(array[index]):
            break
    return index

def get_price(time, stockdata):
    dates = np.array(stockdata['date'])
    prices = np.array(stockdata['close'])
    index = dates.searchsorted(time)
    if index >= stockdata.shape[0] - 1:
        index = stockdata.shape[0] - 1
    price = prices[index]
    return price

def get_diff(time, stockdata, startindex):
    dates = np.array(stockdata['date'])
    index = dates.searchsorted(time)
    if index < startindex:
        return 0

    price1 = get_price(time, df_future)
    price2 = get_price(time, df_spot)

    if abs(price1-price2) > 0.3*min(price1, price2, 3000):
        price_diff = np.nan
    else:
        price_diff = price1-price2
    return price_diff

def convert_to_localtime(time):
    localtime = datetime.fromtimestamp(time).replace(tzinfo=from_zone).astimezone(to_zone)
    return localtime

def calcTA(df, startindex):

    df_matrix = df.copy()
    
#    t0 = time.time()

    calcfi_TAlib(df_matrix, df)

    stock = ss.StockDataFrame.retype(df)
    for indicator in indicators:
        df_matrix[indicator] = stock[indicator].tolist()
#    train_time = time.time() - t0
#    print("ss time: %0.3fs" % train_time)
#    t0 = time.time()

#    df_matrix['temp'] = df_matrix['date'].apply(lambda x:calcfi(x, df_matrix, alpha, t0))
#    df_matrix['lag_hours'] = calcfi(df_matrix, startindex, alpha, t0)[1]
#    df_matrix['flag'] = df_matrix['temp'].apply(lambda x:pd.Series(x[1]))
#    df_matrix = df_matrix.drop('temp', axis = 1)

    df_matrix['price_diff'] = df_matrix['date'].apply(lambda x:get_diff(x,df_matrix,startindex))
#    df_matrix['price_diff'] = df_matrix['date'].apply(lambda x:get_diff(x,df_matrix,startindex))
#    df_matrix['price_diff'] = get_diff(df_matrix, startindex)
#    train_time = time.time() - t0
#    print("diff time: %0.3fs" % train_time)
#    t0 = time.time()
    df_matrix = df_matrix.replace([np.inf, -np.inf, r'^\s*$'], np.nan)
    df_matrix = df_matrix.interpolate(method='values',limit_direction='forward')
#    train_time = time.time() - t0
#    print("int time: %0.3fs" % train_time)
#    t0 = time.time()
    df_matrix['flag'] = df_matrix['date'].apply(lambda x:calcfi_back(x,df_matrix,startindex))
#    df_matrix['flag'] = calcfi(df_matrix, startindex)
#    train_time = time.time() - t0
#    print("calcfi time: %0.3fs" % train_time)
#    t0 = time.time()

    return df_matrix
