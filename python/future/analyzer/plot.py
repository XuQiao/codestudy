import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
from datetime import datetime
import pandas as pd
from constants import *
from func import *

def plot(startday, islog = False):
    columns = ['date','open','high','low','close','unknown','volume']
    filename_full = 'data/'+symbol+'_full_'+contractType+'_future.csv'
    filename_matrix = 'data/'+symbol+'_matrix_full_'+contractType+'_future.csv'
    filename_pred = 'data/'+symbol+'_pred_'+contractType+'_future.csv'
    filename_back = 'data/'+symbol+'_back_'+contractType+'_future.csv'
    filename_fulltemp = 'data/'+symbol+'_fulltemp_'+contractType+'_future.csv'
    filename_matrix_temp = 'data/'+symbol+'_matrix_fulltemp_'+contractType+'_future.csv'
    now = datetime.now()
    now = time.mktime(now.timetuple())

    if os.path.exists(filename_full):
        with open(filename_full, 'r') as f:
            df = pd.read_csv(f,header=0, index_col=0, sep ='\t')

    with open(filename_pred,'r') as f_pred:
        df_pred = pd.read_csv(f_pred, header=0, index_col=0, sep='\t')

    with open(filename_matrix,'r') as f_matrix:
        df_matrix = pd.read_csv(f_matrix, header = 0,index_col=0,sep='\t')

    with open(filename_back,'r') as f_back:
        df_back = pd.read_csv(f_back, header = 0,index_col=0,sep='\t')

    with open(filename_fulltemp,'r') as f_temp:
        df_concat = pd.read_csv(f_temp, header = 0,index_col=0,sep='\t')

    with open(filename_matrix_temp,'r') as f_matrix_temp:
        df_matrix_temp = pd.read_csv(f_matrix_temp, header = 0,index_col=0,sep='\t')

    df = df.drop(['unknown'],axis = 1)
    df_pred = df_pred.fillna(0)
    df_back = df_back.fillna(0)
#    df_matrix_temp = df_matrix_temp.fillna(0)
    df_matrix_temp['flag'] = df_matrix_temp['flag'].apply(lambda x:x*1.1)
    df_matrix_temp['date1'] = df_matrix_temp['date']
    df_back['shortposition'] = df_back['shortposition'].apply(lambda x:-x)
    df['date'] = df['date'].apply(lambda x:mdates.date2num(datetime.fromtimestamp(x)))
    df_matrix['date'] = df_matrix['date'].apply(lambda x:mdates.date2num(datetime.fromtimestamp(x)))
    df_pred['date'] = df_pred['date'].apply(lambda x:mdates.date2num(datetime.fromtimestamp(x)))
    df_back['date'] = df_back['date'].apply(lambda x:mdates.date2num(datetime.fromtimestamp(x)))
    df_concat['date'] = df_concat['date'].apply(lambda x:mdates.date2num(datetime.fromtimestamp(x)))
    df_matrix_temp['date'] = df_matrix_temp['date'].apply(lambda x:mdates.date2num(datetime.fromtimestamp(x)))
    #df['date'] = pd.to_datetime(df['date'])
    #df['date'] = pd.to_datetime(df['date'])
    #df['date'] = df['date'].values.astype('float64')
    #df['date'].astype('float64')#['date'].apply(lambda x:np.ndarray.astype(x/1000))
    ohlc = [tuple(x) for x in df_concat.to_records(index=False)]
    ohlc = ohlc[::5]

    #fig = plt.figure()
    ax1 = plt.subplot2grid((9,1), (0,0), rowspan = 5)
    plt.ylabel('Price')
    plt.title('BTC_future_next_quarter')
    candlestick_ohlc(ax1, ohlc, width=0.0004, colorup='#77d879', colordown='#db3f3f')
    xrange1 = mdates.date2num(datetime.fromtimestamp(now-startday*24*3600))
    xrange2 = mdates.date2num(datetime.fromtimestamp(now+0.5*24*3600))
    ax1.scatter('date', 'longposition',color='purple',s = 0.18, data=df_back,label = 'long-pos')
    ax1.scatter('date', 'shortposition',color='black',s = 0.18, data=df_back,label = 'short-pos')
    ax1.set_xlim(xrange1, xrange2)
    price_low = df_matrix_temp['close'][df_matrix_temp['date1'].searchsorted(now-startday*24*3600)[0]:].min()*(1-0.08)
    price_high = df_matrix_temp['close'][df_matrix_temp['date1'].searchsorted(now-startday*24*3600)[0]:].max()*(1+0.08)
    ax1.set_ylim(price_low, price_high)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(15))
    ax1.xaxis.set_minor_locator(mticker.MaxNLocator(5))

    ax1.legend(loc='best',prop={'size':10})
    ax1.grid(True)

    ax2 = plt.subplot2grid((9,1), (5,0), rowspan = 1, sharex = ax1)
    ax2.scatter('date', 'flag', color='red',s=0.1,data=df_matrix_temp,label='history')
    for model in models:
        ax2.plot('date', 'prob_'+model, linewidth = 0.4,data=df_pred,label='prediction_'+model)
    ax2.set_xlim(xrange1, xrange2)
    ax2.set_ylim(-1.25,1.25)
    ax2.legend(loc='best',prop={'size':6})
    ax2.grid(True)

    ax3 = plt.subplot2grid((9,1), (6,0), rowspan = 3, sharex = ax1)
    ax3.plot('date','btc_spot_back',data=df_back,label='spot_back')
    ax3.plot('date','btc_spot_hist',data=df_back,label='spot_history')
    ax3.plot('date','btc_future_back_RF',data=df_back,label='future_back_RF')
    ax3.plot('date','btc_future_back_XGB',data=df_back,label='future_back_XGB')
    ax3.plot('date','btc_future_hist',data=df_back,label='future_history')
    ax3.set_xlim(xrange1, xrange2)
    ax3.legend(loc='best',prop={'size':8})
    if islog:
        ax3.set_yscale('log')
    ax3.grid(True)

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.xlabel('Date')
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    #plt.setp(ax3.get_xticklabels(), visible=False)
    #plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.2, right=0.94, top=0.90, wspace=0.12, hspace=0)
    #plt.show()

    plt.savefig('data/figure.png')
