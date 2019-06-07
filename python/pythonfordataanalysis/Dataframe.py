data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000, 2001, 2002, 2001, 2002], 'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
from pandas import DataFrame
from pandas import Series
import pandas as pd
import numpy as np
frame = DataFrame(data)
frame
DataFrame(data, columns=['year','state','pop'])
data
frame
frame2 = DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
frame2
frame2.columns
frame2['state']
frame2['pop']
frame2['debt']
frame2.year
frame2['year']
frame2.ix['three']
frame2.ix['two']
frame2['debt']=16.4
frame2['debt']=16.5
frame2
frame2['debt']=np.arange(5.)
frame2
val = Series([-1.2, -1.5, -1.7], index=['two','four','five'])
val = Series([-1.2, -1.5, -1.7], index=['two','four','five'])
from pandas import Series
val = Series([-1.2, -1.5, -1.7], index=['two','four','five'])
val
frame2['debt']=val
frame2
frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2
frame2.columns
frame2['eastern'] = frame2.state == 'Ohio'
frame2.columns
del frame2['eastern']
frame2.columns
pop = {'Nevada':{2001: 2.4, 2002:2.9}, 'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
pop
frame3 = DataFrame(pop)
frame3
frame2
frame3.T
frame2.T
frame3.T
frame3
DataFrame(pop, index=[2001,2002,2003])
pdata = {'Ohio':frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
pdata
DataFrame(pdata)
frame3.index.name='year'
frame3.columns.name='state'
frame3
frame3.values
frame3.index
frame2.values
obj = Series(range(3), index=['a','b','c'])
index=obj.index
index[1:]
index = pd.Index(np.arange(3))
import pandas as pd
index = pd.Index(np.arange(3))
obj2=Series([1.5,-2.5,0], index=index)
obj2.index is index
index
obj2
frame3
'Ohio' in frame3.columns
2003 in frame3.columns
frame3.columns
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
obj
obj2 = obj.reindex(['a','b','c','d','e'])
obj2
obj.reindex(['a','b','c','d','e'],fill_value=0)
obj3 = Series(['blue','purple','yellow'],index=[0,2,4])
obj3.reindex(range(6), method='ffill')
obj.reindex(['a','b','c','d','e'],fill_value=0)
obj3 = Series(['blue','purple','yellow'],index=[0,2,4])
obj3.reindex(range(6), method='ffill')
frame = DataFrame(np.arange(9).reshape((3,3)), index = ['a','c','d'], columns=['Ohio','Texas', 'California'])
frame2=  frame.reindex(['a','b','c','d'])
states=['Texas','Utah','California']
frame.reindex(columns=states)
frame2=  frame.reindex(['a','b','c','d'],method='ffill',columns=states)
frame.ix[['a','b','c','d'],states]
obj = Series(np.arange(5.),index=['a','b','c','d','e'])
new_obj = obj.drop('c')
new_obj
obj.drop(['d','c'])
data = DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
data.drop(['Colorado','Ohio'])
data.drop('two',axis=1)
data.drop(['two','four'],axis=1)

obj = Series(np.arange(4.),index=['a','b','c','d'])
obj['b']
obj[1]
obj
obj[2:4]
obj[['b','a','d']]
obj[[1,3]]
obj[obj<2]
obj['b':'c']
obj['b':'c'] =5
obj
obj = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
data
data['two']
data[['three','one']]
data[:2]
data[data['three']>5]
data<5
data[data<5]
data[data<5] = 0
data
data.ix[['Colorado','Utha'],[3,0,1]]
obj = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
data
data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
data.ix[['Colorado','Utha'],[3,0,1]]
data.ix[['Colorado','Utha'],[3,0,1]]
data
data.ix[['Colorado','Utaa'],[3,0,1]]
data.ix[['Colorado','Utah'],[3,0,1]]
data.ix[2]
data.ix[:'Utah','two']
data.ix[data.three>5,:3]
s1 = Series([7.3,-2.5,3.4,1.5], index = ['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
s1
s2
s1+s2
df1 = DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
df1
df2
df1+df2
df1 = DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
df1
df2
df1+df2
df1.add(df2,fill_value=0)
df1.reindex(columns=df2.columns,fill_value=0)
arr = np.arange(12.).reshape((3,4))
arr
arr[0]
arr-arr[0]
frame = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
series = frame.ix[0]
frame
series
frame - series
series = Series(range(3),index=['b','e','f'])
frame + series
series3 = frame['d']
frame
series3
frame.sub(series3,axis=0)
frame.sub(series3)
frame
frame = DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
frame
np.abs(frame)
f=lambda x:x.max()-x.min()
frame.apply(f)
frame.apply(f,axis=1)
def f(x):
    return Series([x.min(), x.max()],index=['min','max'])
frame.apply(f)
format = lambda x:'%.2f' % x
frame.applymap(format)
frame['e'].map(format)
obj = Series(range(4), index = ['d','a','b','c'])
obj.sort_index()
obj
frame = DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1,ascending=False)
obj = Series([4, 7, -3 ,2])
obj=Series([4, np.nan, 7, np.nan, -3 ,2])
frame = DataFrame({'b':[4, 7, -3, 2],'a':[0,1,0,1]})
frame
obk = Series([7, -5, 7, 4, 2, 0, 4])
ob = Series([7, -5, 7, 4, 2, 0, 4])
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()
obj.rank(method='first')
obj.rank(ascending=False,method='max')
frame = DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})
frame
frame.rank(axis=1)
obj = Series(range(5),index=['a','a','b','b','c'])
obj
obj.index.is_unique
obj['a']
obj['c']
df = DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
df
df.ix['b']
df = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
df
df.sum()
df.sum(axis=1)
df.mean(axis=1,skipna=False)
df.mean(axis=1)
df.idxmax()
df.cumsum()
df.cumsum(axis=1)
df.describe()
obj = Series(['a','a','b','c'] * 4)
obj.describe()
obj
%run Dataframe.py
from pandas_datareader import data
all_data = {}
for ticker in ['AAPL','IBM','MSFT','GOOG']:
    all_data[ticker] = data.get_data_google(ticker,'1/1/2000','1/1/2010')
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteriterms()})
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
all_data.iteritems()
a,b in for a, b in all_data.iteritems()
a,b for a, b in all_data.iteritems()
[(a,b) for a, b in all_data.iteritems()]
price = DataFrame({tic: data['Close'] for tic, data in all_data.iteriterms()})
price = DataFrame({tic: data['Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volumn'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
returns = price.pct_change()
returns.tail()
returns.MSFT.corr(returns.IBM)
returns.MSFT.cov(returns.IBM)
returns.corr()
returns.cov()
returns.corrwith(return.IBM)
returns.corrwith(returns.IBM)
returns.corrwith(volume)
volume
volume['GOOG']
returns.corrwith(volume,axis=1)
obj = Series(['c','a','d','a','a','b','b','c','c'])
uniques = obj.unique()
uniques
obj.value_counts()
obj.value_counts(obj.values,sort=False)
pd.value_counts(obj.values,sort=False)
mask = obj.isin(['b','c'])
mask
obj[mask]
data = DataFrame(({'Qu1':[1,3,4,3,4],'Qu2':[2,3,1,2,3],'Qu3':[1,5,2,4,4]}))
data
result = data.apply(pd.value.counts).fillna(0)
result
string_data = Series(['aardvark','artichoke',np.nan,'avocado'])
string_data
string_data.isnull()
string_data[0]=None
string_data.isnull()
from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()]
data=  DataFrame([[1.,6.5,3.],[1.,NA,NA],[NA,NA,NA],[NA,6.5,3]])
cleaned = data.dropna()
data
cleaned
cleaned = data.dropna(how='all')
cleaned
data[4]=NA
data
data.dropna(axis=1,how='all')
df = DataFrame(np.random.randn(7,3))
df.ix[:4,1]=NA
df.ix[:2,2] =NA
df
df.dropna(thresh=3)
df.fillna(0)
df.fillna({1:0.5,3:-1})
_ = df.fillna(0,inplace=True)
df
df= DataFrame(np.random.randn(6,3))
df.ix[2:,-1] = NA
df.ix[4:, 2]=NA
df
df.fillna(method='ffill')
df.fillna(method='ffill',limit=2)
df.ix[2:,1] = NA
df
df.drop('-1',axis=1)
df.drop('-1')
df.drop(-1,axis=1)
df.fillna(method='ffill')
df.fillna(method='ffill',limit=2)
df = df.drop(-1,axis=1)
df.fillna(method='ffill',limit=2)
df.fillna(method='ffill',limit=1)
data=Series([1.,NA,3.5,NA,7])
data.fillna(data.mean())
data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
data
data.index
data['b']
data['b':'c']
data.ix['b','d']
data.ix[['b','d']]
data[:,2]
data.unstack()
data.unstack().stacl()
data.unstack().stack()
frame = DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
frame
frame.index.names=['key1','key2']
frame.columns.names['state','color']
frame.columns.names=['state','color']
frame
frame['Ohio']
MultiIndex.from_arrays
frame.swaplevel('key1','key2')
frame.sortlevel(1)
frame.swaplevel(0,1).sortlevel(0)
frame.sum(level='key2')
frame.sum(level='color',axis=1)
frame = DataFrame({'a':range(7),'b':range(7,0,-1), 'c':['one','one','one','two','two','two','two'],'d':[0,1,2,0,1,2,3]})
frame
frame2 = frame.set_index('c','d'])
frame2 = frame.set_index(['c','d'])
frame2
frame2 = frame.set_index(['c','d'],drop=False)
frame2
frame2.reset_index()
ser = Series(np.arange(3))
ser
ser[-1]
ser2 = Series(np.arange(3.),index=['a','b','c'])
ser2[-1]
ser.ix[:1]
ser3=Series(range(3),index=[-5,1,3])
ser3.iget_value(2)
ser3.iloc(2)
ser3.iloc[i]
ser3.iloc[2]
ser3.iat[2]
ser3
ser3.iloc[1]
ser3.iloc[0]
ser3.iloc[3]
ser3.iraw(0)
frame = DataFrame(np.arange(6).reshape(3,2)),index=[2,0,1])
frame = DataFrame(np.arange(6).reshape((3,2)),index=[2,0,1])
frame.irow(0)
frame.iloc[0]
frame
frame.iloc[3]
frame.iloc[2]
pdata = pd.Panel(dict(stk, data.get_data_google(stk,'1/1/2009','6/1/2012')) for stk in ['AAPL','GOOG','MSFT','DELL']))
pdata = pd.Panel(dict((stk, data.get_data_google(stk,'1/1/2009','6/1/2012')) for stk in ['AAPL','GOOG','MSFT','DELL']))
from pandas_datareader import data
pdata = pd.Panel(dict((stk, data.get_data_google(stk,'1/1/2009','6/1/2012')) for stk in ['AAPL','GOOG','MSFT','DELL']))
pdata
pdata = pdata.swapaxes('items','minor')
pdata['Close']
pdata.ix[:,'6/1/2012',"]
pdata.ix[:,'6/1/2012',:]
pdata.ix['Close','5/22/2012':,:]
stacked = pdata.ix['Close','5/22/2012':,:].to_frame()
stacked = pdata.ix[:,'5/22/2012':,:].to_frame()
stacked
stacked.to_panel()
