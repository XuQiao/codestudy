from datetime import datetime
now = datetime.now()
now
delta = datetime(2011,1,7)-datetime(2008,6,24,8,15)
delta
delta.days
delta.seconds
from datetime import timedelta
start = datetime(2011,1,7)
start + timedelta(12)
start - 2*timedelta(12)
stamp = datetime(2011,1,3)
str(stamp)
stamp.strftime('%Y-%M-%d")
stamp.strftime('%Y-%M-%d')
stamp.strftime('%Y-%m-%d')
value = '2011-01-03'
datetime.strptime(value,'%Y-%m-%d')
datestrs=['7/6/2011','8/6/2011']
[datetime.strptime(x,'%m/%d/%Y') for x in datastrs]
[datetime.strptime(x,'%m/%d/%Y') for x in datestrs]
from dateutil.parser import parse
parse('2011-01-03')
datetime.datetime(2011,1,3,0,0)
parse('6/12/2011',dayfirst=True)
datastrs
datestrs
import pandas as pd
pd.to_datetime(datestrs)
idx=pd.to_datetime(datastrs+[None])
idx=pd.to_datetime(datestrs+[None])
idx
idx[2]
pd.isnull(idx)
dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7),datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
ts=Series(np.random.randn(6),index=dates)
import numpy
ts=Series(np.random.randn(6),index=dates)
from numpy import Series
from pandas import Series
ts=Series(np.random.randn(6),index=dates)
ts
type(ts)
ts+ts[::2]
ts[::2]
ts.index.dtype
stamp = ts.index[0]
stamp
stamp = ts.index[2]
ts[stamp]
ts['1/10/2011']
ts['20110110']
longer_ts = Series(np.random.randn(1000),index=pd.date_range('1/1/2000',period=1000))
longer_ts = Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
longer_ts
longer_ts['2001']
longer_ts['2001-05']
ts[datetime(2011,1,7)]
ts[datetime(2011,1,7):]
ts
ts['1/6/2011':'1/11/2011']
ts.truncate(after='1/9/2011')
dates=pd.date_range('1/1/2000',periods=100,freq='W-Wed')
long_df = DataFrame(np.random.randn(100,4),index=dates,columns=['Colorado','Texas','New York','Ohio'])
from pandas import DataFrame
long_df = DataFrame(np.random.randn(100,4),index=dates,columns=['Colorado','Texas','New York','Ohio'])
long_df.ix['5-2001']
import pandas as pd
dates = pd.DatetimeIndex(['1/1/2000','1/2/2000','1/2/2000','1/2/2000','1/3/2000'])
dup_ts= Series(np.arange(5),index=dates)
dup_ts
dup_ts.index.is_unique
dup_ts['1/3/2000']
dup_ts['1/2/2000']
grouped = dup_ts.groupby(level=0)
grouped
grouped.mean()
grouped.count
grouped.count()
ts
ts.resample('D'_
)
ts.resample('D')
ts
ts.resample('D')
index=pd.date_range('4/1/2012','6/1/2012')
index
pd.date_range(start='4/1/2012',periods=20)
pd.date_range(end='4/1/2012',periods=20)
pd.date_range('1/1/2000','12/1/2000',freq='BM')
pd.date_range('5/2/2000 12:56:31',periods=5)
pd.date_range('5/2/2000 12:56:31',periods=5,normalize=True)
from pandas.tseries.offsets import Hour,Minute
hour=Hour()
hour
four_hours=Hour(4)
hour_
four_hours
pd.date_range('1/1/2000','1/3/2000 23:59', freq='4h'
)
Hour(2) + Minute(30)
pd.date_range('1/2/2000',periods=10,freq='1h30min')
rng = pd.date_range('1/1/2012','9/1/2012',freq='WOM-3FRI')
rng
list(rng)
ts=Series(np.random.randn(4),index=pd.date_range('1/1/2000',periods=4,freq='M')
)
ts
ts.shift(2)
ts.shift(-2)
ts/ts.shift(1)-1
ts.shift(2,freq='M')
ts.shift(3,freq='D')
ts.shift(1,freq='3D')
ts.shift(1,freq='90T')
from pandas.tseries.offsets import Day, MonthEnd
now  = datetime(2011,11,17)
now+3*Day()
now+MonthEnd()
now+MonthEnd(2)
now+MonthEnd(3)
offset =MonthEnd()
offset.rollforward(now)
offset.rollback(now)
ts=Series(np.random.randn(20),index=pd.date_range('1/15/2000',periods=20,freq='4d')
)
ts.groupby(offset.rollforward).mean()
ts.resample('M',how='mean')
ts.resample('M').mean()
import pytz
pytz.common_timezones[-5:]
tz=pytz.timezone('US/Eastern')
tz
rng=pd.date_range('3/9/2-12 9:30',periods=6,freq='D')
ts=Series(np.random.randn(len(rng)),index=rng)
ts
print(ts.index.tz)
pd.data_range('3/9/2012 9:30',periods=10, freq='D',tz='UTC')
pd.date_range('3/9/2012 9:30',periods=10, freq='D',tz='UTC')
ts_utc=ts.tz_localize('UTC')
ts
ts_utc
ts_utc.index
print(ts.index.tz)
ts_utc.tz_convert('US/Eastern')
ts_utc.col
ts_utc.index
ts_utc.index = ts_utc.index+'10Y'
ts_utc.index = ts_utc.index+timedelta(10,0,0)
ts_utc.index
ts_utc.index = ts_utc.index+timedelta(10,0,0)
ts_utc.index
ts_utc.index = ts_utc.index+timedelta(10,0,0,0,)
ts_utc.index = ts_utc.index+timedelta(10,0,0,0,0)
ts_utc.index
ts_utc.index = ts_utc.index+timedelta(10,0,0,0,0)
ts_utc.index
timedelta(YEARLY=10)
rng=pd.date_range('3/9/2012 9:30',periods=6,freq='D')
pd.date_range('3/9/2012 9:30',periods=10, freq='D',tz='UTC')
ts_utc.tz_convert('US/Eastern')
ts
ts.index
ts.index+datetime('0/0/10')
ts.index+datetime(10)
ts.index+datetime(10,0,0)
ts.index+timedelta(days=365)
ts.index+timedelta(days=365)*10
ts.index=ts.index+timedelta(days=365)*10
ts
ts=Series(np.random.randn(len(rng)),index=rng)
ts
ts_utc=ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern')
ts_eastern=ts.tz_localize('US/Eastern')
ts_eastern
ts_eastern.tz_convert('Europe/Berlin')
ts.index.tz_localize('Asia/Shanghai')
stamp=pd.Timestamp('2011-03-12 04:00')
stamp_ut
stamp_utc=stamp.tz_localize('utc')
stamp_utc.tz_convert('US/Eastern')
stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
stamp_moscow
stamp_utc.value
stamp_utc.tz_convert('US/Eastern').value
from pandas.tseries.offsets import Hour
stamp= pd.Timestamp('2012-03-12 01:30',tz='US/Eastern')
stamp
stamp+Hour
stamp+Hour()
stamp= pd.Timestamp('2012-11-04 00:30',tz='US/Eastern')
stamp
stamp+2*Hour()
rng=pd.date_range('3/7/2012 9:30',periods=10,freq='B')
ts=Series(np.random.randn(len(rng)),index=rng)
ts
ts1=ts[:7].tz_localize('Europe/London')
ts1
ts2=ts1[:2].tz_convert('Europe/Moscow')
result=ts1+ts2
result.index
result
p=pd.Period(2007,freq='A-DEC')
p
p+5
p-2
pd.Period('2014',freq='A-DEC')-p
rng=pd.period_range('1/1/2000','6/30/2000',freq='M')
rng
Series(np.random.randn(6),index=rng)
values=['200103','200202','200301']
index=pd.PeriodIndex(values,freq='Q-DEC')
inde
index
p=pd.Period('2007',freq='A-DEC')
p.asfreq('M',how='start')
p.asfreq('M',how='end')
p=pd.Period('2007',freq='A-JUN')
p.asfreq('M','start')
p.asfreq('M','end')
p=pd.Period('2007-08',freq='M')
p.asfreq('A-JUN')
rng=pd.period_range('2006','2009',freq='A-DEC')
ts=Series(np.random.randn(len(rng)),index=rng)
ts
ts.asfreq('M',how='start')
ts.asfreq('B',how='emd')
ts.asfreq('B',how='end')
p=pd.Period('201204',freq='Q-JAN')
p
p.asfreq('D','start')
p.asfreq('D','end')
p4pm = (p.asfreq('B','e') - 1).asfreq('T','s')+16*60
p4pm
p4pm.to_timestamp
p4pm.to_timestamp()
rng = pd.period_range('2011Q3','2012Q4',freq='Q-JAN')
ts=Series(np.arange(len(rng)),index=rng)
ts
new_rng = (rng.asfreq('B','e') - 1).asfreq('T','s')+16 * 60
ts.index= new_rng.to_timestamp()
ts
rng = pd.date_range('1/1/2000',periods= 3,freq='M')
ts=Series(randn(3),index=rng)
pts=ts.to_period()
pts
ts
pts=ts.to_period()
pts
pts.to_timestamp(how='end')
data=pd.read_csv('pydata-book/ch08/macrodata.csv')
data.year
data.quarter
index=pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')
index
data.index=index
data.infl
rng=pd.data_range('1/1/2000',periods=100,freq='D')
rng=pd.date_range('1/1/2000',periods=100,freq='D')
ts=Series(randn(len(rng)),index=rng)
ts.resample('M',how='mean')
ts
ts.plot
ts.plot()
ts.resample('M',how='mean').plot()
close()
close()
ts.resample('M',how='mean',kind='period')
ts.resample('M',how='max',kind='period')
ts.resample('M',kind='period').max().plot()
ts.plot()
ts.resample('M',kind='period').min().plot()
ts.resample('M',kind='period').meann().plot()
ts.resample('M',kind='period').mean().plot()
ts.resample('M',kind='period').ohlc().plot()
ts.resample('M',kind='period').median().plot()
close()
close()
rng=pd.date_range('1/1/2000',periods=12,freq='T')
ts=Series(np.arange(12),index=rng)
ts
ts.resample('5min',how='sum')
ts.resample('5min').sum()
ts.resample('5min',closed='left').sum()
ts.resample('5min',closed='right').sum()
ts.resample('5min',closed='left',label='left').sum()
ts.resample('5min',closed='left',label='left',loffset='-1s').sum()
ts.resample('5min',closed='left',loffset='-1s').sum()
ts.resample('5min',loffset='-1s').sum()
ts.resample('5min',closed='right',loffset='-1s').sum()
ts.resample('5min',closed='right',label='right',loffset='-1s').sum()
ts.resample('5min').ohlc()
ts.resample('5min',closed='right',label='right').ohlc()
rng=pd.data_range('1/1/2000',periods=100,freq='D')
rng=pd.date_range('1/1/2000',periods=100,freq='D')
ts=Series(np.arange(100),index=rng)
ts.groupby(lambda x:x.month).mean()
ts.groupby(lambda x:x.weekday).mean()
frame=DataFrame(np.random.randn(2,4),index=pd.data_range('1/1/2000',periods=2,freq='W-WED'),columns=['Colorado','Texas','New York','Ohio'])
frame=DataFrame(np.random.randn(2,4),index=pd.date_range('1/1/2000',periods=2,freq='W-WED'),columns=['Colorado','Texas','New York','Ohio'])
frame[:5]
frame
df_daily=frame.resample('D')
df_daily
df_daily
df_daily()
print df_daily
df_daily[:]
df_daily
frame.resample('D',fill_method='ffill')
frame.resample('D',fill_method='ffill',limits=2)
frame.resample('D',fill_method='ffill',limit=2)
frame.resample('W-THU',fill_method='ffill')
frame=DataFrame(np.random.randn(24,4),index=pd.period_range('1-2000','12-2001',freq='M'),columns=['Colorado','Texas','New York','Ohio'])
frame[:5]
annual_frame = frame.resample('A-DEC').mean()
annual_frame
annual_frame.resample('Q-DEC',fill_method='ffill')
annual_frame.resample('Q-DEC',fill_method='ffill',convention='start')
annual_frame.resample('Q-MAR',fill_method='ffill')
close_px_all = pd.read_csv('pydata-book/ch09/stock_px.csv',parse_dates=True,index_col=0)
close_px = close_px_all[['AAPL','MSFT','XOM']]
close_px=close_px.resample('B',fill_method='ffill')
close_px
close_px['AAPL'].plot()
close_px.ix['2009'].plot()
close_px['AAPL'].ix['01-2011':'03-2011'].plot()
appl_q = close_px['AAPL'].resample('Q-DEC',fill_method='ffill')
appl_q.ix['2009'].plot()
close()
close()
appl_q.ix['2009'].plot()
close()
appl_q = close_px['AAPL'].resample('Q-DEC',fill_method='ffill')
close_px['AAPL'].ix['01-2011':'03-2011'].plot()
close()
close_px.AAPL.plot()
pd.rolling_mean(close_px.AAPL,250).plot()
pd.rolling(close_px.AAPL,250).mean().plot()
pd.rolling_mean(close_px.AAPL,250).plot()
appl_std250 = pd.rolling_std(close_px.AAPL,250,min_periods=10)
appl_std250 = pd.rolling(close_px.AAPL,250,min_periods=10).std()
appl_std250 = close_px.AAPL.rolling(250,min_periods=10).std()
appl_std250[5:12]
appl_std250.plot()
close()
appl_std250.plot()
expanding_mean = lambda x:rolling_mean(x, len(x), min_periods=1)
close_px.rolling(60).mean().plot(logy=True)
close()
fig_axes = plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True,figsize=(12,7))
aapl_px = close_px.AAPL['2005':'2009']
ma60 = aapl_px.rolling(60,min_periods=50)
ewma60 = pd.ewma(aapl_px,span=60)
ewma60 = aapl_px.ewm(span=60).mean()
ma60 = aapl_px.rolling(60,min_periods=50).mean()
aapl.px.plot(style='k-',ax=axes[0])
aapl_px.plot(style='k-',ax=axes[0])
aapl_px
axes
fig,axes = plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True,figsize=(12,7))
close()
close()
fig,axes = plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True,figsize=(12,7))
aapl_px.plot(style='k-',ax=axes[0])
ma60.plot(style='k--',ax=axes[0])
aapl_px.plot(style='k-',ax=axes[1])
ewma60.plot(style='k--',ax=axes[1])
axes[0].set_title('Simple MA')
axes[1].set_title('Exponentially-weighted MA')
spx_rets=spx_px/spx_px.shift(1)-1
spx_px = close_px_all['SPX']
spx_rets=spx_px/spx_px.shift(1)-1
returns=close_px.pct_change()
corr=returns.AAPL.rolling(spx_rets,125,min_periods=100).corr()
corr=returns.AAPL.rolling_corr(spx_rets,125,min_periods=100)
corr=pd.rolling_corr(returns.AAPL,spx_rets,125,min_periods=100)
corr=returns.AAPL.rolling(window=125,min_periods=100).corr(spx_rets)
close()
corr.plot()
corr=returns.rolling(window=125,min_periods=100).corr(spx_rets)
corr.plot()
close()
from scipy.stats import percentileofscore
score_at_2percent = lambda x:percentileofscore(x,0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
close()
rng = pd.date_range('1/1/2000',periods=100000000,freq='10ms')
ts=Series(np.random.randn(len(rng)),index=rng)
rng = pd.date_range('1/1/2000',periods=10000000,freq='10ms')
ts=Series(np.random.randn(len(rng)),index=rng)
ts
ts.resample('15min').olhc()
ts.resample('15min').ohlc()
%timeit ts.resample('15min').ohlc()
rng = pd.date_range('1/1/2000',periods=10000000,freq='1s')
ts=Series(np.random.randn(len(rng)),index=rng)
%timeit ts.resample('15min').ohlc()
%timeit ts.resample('15s').ohlc()
%history -f timeseries.py
