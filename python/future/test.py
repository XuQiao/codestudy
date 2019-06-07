import pandas as pd
import numpy as np
import talib.abstract
from pprint import pprint
from datetime import datetime
from sklearn.model_selection import train_test_split
import time
now = datetime.now()
now = time.mktime(now.timetuple())
from dateutil import tz
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
from analyzer import constants, pullfuturekline, pullspotkline, merge_future, merge_spot, classification, model, plot, runxgboost

#pullfuturekline()
#pullspotkline()
#merge_spot()
#merge_future()
cv_score, f1_score, precision_score = classification()
cv_score_xgb, f1_score_xgb, precision_score_xgb = runxgboost.run()
test = model(15)

d = pd.read_csv('data/btc_usd_matrix_full_next_quarter_future.csv',sep='\t',index_col=0)
#print d.columns
#print d['macd'][10000:10003]
#print d['MACD'][10000:10003]
#print d['CDL2CROWS'][10000:10003]
df = pd.read_csv('data/btc_usd_full_next_quarter_future.csv',sep='\t',index_col=0)
#print d.iloc[10000:10005][['MA','MACD','MACDSignal','MACDHIST','macd','macds','macdh']].transpose()
#print d.iloc[10000:10005][['boll','boll_ub','boll_lb','UPPERBAND','MIDDLEBAND','LOWERBAND']].transpose()
#cd = talib.abstract.CDL2CROWS(df)
#print cd[28910:28915]
#for index in range(len(d.iloc[10000])):
#    print d.columns[index],'\t', d.iloc[10000][index]
#pprint(d.iloc[10000])
trainall_df = pd.read_csv("data/btc_usd_matrix_full_next_quarter_future.csv",sep='\t',index_col=0)
startday = 360
endday = 0
if startday < 0:
    startindex = 0
else:
    startindex = trainall_df['date'].searchsorted(now - startday * 24 * 3600)[0]
endindex = trainall_df['date'].searchsorted(now - endday * 24 * 3600)[0]
trainall_df = trainall_df.dropna(axis=0)
trainall_df = trainall_df.iloc[startindex:endindex]
trainall_df1 = trainall_df.drop(['flag','open','high','low','close'],axis=1)

X_train, X_test, y_train, y_test = train_test_split(trainall_df1, trainall_df['flag'], test_size = 0.05, shuffle = False)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

def convert_to_localtime(time):
    localtime = datetime.fromtimestamp(time).replace(tzinfo=from_zone).astimezone(to_zone)
    return localtime
print convert_to_localtime(X_test.iloc[0]['date'])
print convert_to_localtime(X_test.iloc[-1]['date'])

    # Data pre-processing and extract features(use Vectorizer)


    # extract features
    #print("Extracting features from the training data using a n-gram or sparse vectorizer")
    #t0 = time()


