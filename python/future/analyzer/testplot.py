import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
from func import *

def plot(startday, filename, col1, col2, col3):
    now = datetime.now()
    now = time.mktime(now.timetuple())
    df = pd.read_csv(filename,delimiter='\t',index_col=0)
    df = df.dropna(axis=0)
    plt.subplot(211)
    if startday < 0:
        startindex = 0
    else:
        startindex = df['date'].searchsorted(now - startday * 24 * 3600)[0]
    print startindex
    df['date'] = df['date'].apply(lambda x:mdates.date2num(convert_to_localtime(x)))
    #plt.bar(df.iloc[::][col1],df.iloc[::][col2],color='black')
    plt.hist(df.iloc[startindex:][col2], [-1,0,1,2],color='black')
    plt.subplot(212)
#    ax.set_ylim(0,100000)
#    ax2 = plt.subplot(212,sharex=ax)
    plt.scatter(df.iloc[::][col1],df.iloc[::][col3],color='blue')
    xrange1 = mdates.date2num(convert_to_localtime(now-startday*24*3600))
    xrange2 = mdates.date2num(convert_to_localtime(now))
#    plt.xlim(xrange1, xrange2)
#    plt.ylim(7500,12000)
#    ax.axis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.grid(True)
#    for label in ax2.xaxis.get_ticklabels():
#        label.set_rotation(45)
    plt.subplots_adjust(left=0.09, bottom=0.2, right=0.94, top=0.90, wspace=0.12, hspace=0)
    plt.show()
#    a =  df[col2]
#    print len(np.where(a.isnull())[0])
plot(360,'data/btc_usd_matrix_fulltemp_next_quarter_future.csv','date','flag','close')
