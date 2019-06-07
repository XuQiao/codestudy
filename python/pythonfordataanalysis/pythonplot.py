plot(np.arange(10))
close()
fig = plt.figure()
fig = plt.figure(2)
ax1=fig.add_subplot(2,2,1)
fig = plt.figure()
ax1=fig.add_subplot(2,2,1)
ax1=fig.add_subplot(2,2,2)
ax1=fig.add_subplot(2,2,3)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
from numpy.random import randn
plt.plot(randn(50).cumsum(),'k--')
_ = ax1.hist(randn(100),bins=20,color='k',alpha=0.3)
close()
ax1=fig.add_subplot(2,2,2)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
fig = plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
plt.plot(randn(50).cumsum(),'k--')
_ = ax1.hist(randn(100),bins=20,color='k',alpha=0.3)
ax2 = scatter(np.arange(30),np.arange(30)+3.randn(30))
ax2 = scatter(np.arange(30),np.arange(30)+3*randn(30))
ax2
ax3=fig.add_subplot(2,2,3)
plt.plot(randn(50).cumsum(),'k--')
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))
ax2
fig, axes= plt.subplots(2,3)
axes
import matplotlib.pyplot as plt
plt
fig, axes= plt.subplots(2,3)
axes
axes.ndim
axes[0,1]
axes[0,1].nrows
axes.nrows
subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)
fig,axes=plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(randn(500),bins=50,color='k',alpha=0.5)
plt.subplots_adjust(wspace=0,hspace=0)
ax.plot(x,y,'g--')
plot(x,y,'g--')
axes.plot(x,y,'g--')
ax1.plot(x,y,'g--')
plt.plot(randn(30).cumsum(),'ko--')
close()
close()
close()
close()
plt.plot(randn(30).cumsum(),'ko--')
plot(randn(30).cumsum(),color='k',linestyle='dashed',marker='o')
data=randn(30).cumsum()
plt.plot(data,'k--',label='Default')
plt.plot(data,'k--',drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')
plt.xlim()
plt.xlim([0,10])
fig = plt.figure();ax=fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum())
ticks = ax.set_xticks([0,250,500,750,1000])
labels = ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
fig=plt.figure();ax=fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(),'k',label='one')
ax.plot(randn(1000).cumsum(),'k--',label='two')
ax.plot(randn(1000).cumsum(),'k.',label='three')
ax.legend(loc='best')
ax.text(x,y,'hello world!',family='monospace',fontsize=10)
ax.text(1,2,'hello world!',family='monospace',fontsize=10)
ax.text(-80,2,'hello world!',family='monospace',fontsize=10)
ax.text(2,-80,'hello world!',family='monospace',fontsize=10)
close()
from datetime import datetime
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
data = pd.read_csv('pydata-book/ch08/spx.csv',index_col=0,parse_dates=True)
import pandas as pd
data = pd.read_csv('pydata-book/ch08/spx.csv',index_col=0,parse_dates=True)
spx = data['SPX']
spx.plot(ax=ax,style='k-')
crisis_data = [(datetime(2007,10,10),'Peak of bull market'),(datetime(2008,3,12),'Bear Sterns Fails'),datetime(2008,9,15),'Lehman Bankruptcy']
for date, label in crisis_data:
    ax.annotate(label,xy=(date, spx.asof(date) + 50), xytext=(date, spx.asof(date) + 200), arrowprops=dict(facecolor='black'),horizontalalignment='left',verticalalignment='top')
crisis_data
for date, label in crisis_data:
    ax.annotate(label,xy=(date, spx.asof(date) + 50), xytext=(date, spx.asof(date) + 200), arrowprops=dict(facecolor='black'),horizontalalignment='left',verticalalignment='top')
spx.asof(date)
date
label
crisis_data = [(datetime(2007,10,10),'Peak of bull market'),(datetime(2008,3,12),'Bear Sterns Fails'),(datetime(2008,9,15),'Lehman Bankruptcy')]
for date, label in crisis_data:
    ax.annotate(label,xy=(date, spx.asof(date) + 50), xytext=(date, spx.asof(date) + 200), arrowprops=dict(facecolor='black'),horizontalalignment='left',verticalalignment='top')
ax.set_xlim(['1/1/2017','1/1/2011']
)
ax.set_ylim([600,800])
ax.set_title('Important dates in 2008-2009 financial crisis')
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
rect=plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)
circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)
pgon = plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
close()
close()
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
spx = data['SPX']
spx.plot(ax=ax,style='k-')
ax.set_title('Important dates in 2008-2009 financial crisis')
for date, label in crisis_data:
    ax.annotate(label,xy=(date, spx.asof(date) + 50), xytext=(date, spx.asof(date) + 200), arrowprops=dict(facecolor='black'),horizontalalignment='left',verticalalignment='top')
ax.set_xlim(['1/1/2017','1/1/2011'])
ax.set_xlim(['1/1/2007','1/1/2011'])
ax.set_ylim([600,800])
ax.set_ylim([600,1800])
plt.savefig('figpath.pdf')
plt.savefig('figpath.png',dpi=400,bbox_inches='tight')
from io import  StringIO
buffer = StringIO()
plt.savefig(buffer)
plot_data = buffer.getvalue()
plt.rc('figure',figsize=(10,10))
font_options={'family':'monospace','weight':'bold','size':'small'}
plt.rc('font',**font_options)
font_options={'family':'monospace','weight':'bold','size':'small'}
plt.rc('font',**font_options)
s=Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
import numpy
s=Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
from numpy import *
s=Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
from pandas import *
s=Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
s.plot()
s=Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
s
s
s.plot()
np.random.randn(10).cumsum()
np.arange(0,100,10)
s
s.plot()
df= DataFrame(np.random.randn(10,4).cumsum(0), columns=['A','B','C','D'],index=np.arange(0,100,10))
df
df.plot()
fig.axes=plt.subplots(2,1)
fig.axes=plt.subplots(2,1)
fig,axes=plt.subplots(2,1)
data=Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar',ax=axes[0],color='k',alpha=0.7_
)
data.plot(kind='bar',ax=axes[0],color='k',alpha=0.7)
data.plot(kind='barh',ax=axes[1],color='k',alpha=0.7)
df = DataFrame(np.random.rand(6,4),index=['one','two','three','four','five','six'],columns=pd.Index(['A','B','C','D'],name='Genus'))
df
df.plot(kind='bar')
df.plot(kind='barh',stacked=True,alpha=0.5)
close()
close()
close()
close()
df.values
tips=pd.read_csv('pydata-book/ch08/tips.csv')
party_counts=pd.crosstab(tips.day,tips.size_
)
party_counts=pd.crosstab(tips.day,tips.size)
party_counts
party_counts=pd.crosstab(tips.day,tips.size)
party_counts
party_counts = party_counts.ix[:,2:5]
party_counts
tips
tips['tip_pct'] = tips['tip']/tips['total_bill']
tips['tip_pct'].hist(bins=50)
tips['tip_pct'].plot(kind='kde')
comp1 = np.random.normal(0,1,size=200)
comp2 = np.random.normal(10,2,size=200)
values= Series(np.concatenate([comp1,comp2])
)
values.hist(bins=100,alpha=0.3,color='k',normed=True)
values.plot(kind='kde',style='k--')
values
macrp = pd.read_csv('pydata-book/ch08/macrodata.csv')
data=macrp[['cpi','m1','tbilrate','unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
plt.scatter(trans_data['m1'],trans_data['unemp'])
close
close()
plt.scatter(trans_data['m1'],trans_data['unemp'])
plt.title('Change in log %s vs. log %s' % ('m1', 'unemp'))
scatter_matrix(trans_data,diagonal='kde',color='k',alpha=0.3)
scatter_matrix(trans_data,diagonal='kde',alpha=0.3)
close()
close()
close()
data = pd.read_csv('pydata-book/ch08/Haiti.csv')
data
data[['INCIDENT DATE', 'LATTITUDE','LONGITUDE'][:10]

]
data[['INCIDENT DATE', 'LATTITUDE','LONGITUDE']][:10]
data[['INCIDENT DATE', 'LATITUDE','LONGITUDE']][:10]
data['CATEGORY'][:6]
data.describe()
data = data[(data.LATITUDE>18) & (data.LATITUDE < 20) & (data.LONGITUDE>-75) & (data.LONGITUDE<-70) & data.CATEGORY.notnull()]
data
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
def get_englist(cat):
    code, name = cat.split(',')
    code, name = cat.split('.')
    if '|' in name:
        name = name.split(' | ')[1]
def get_englist(cat):
    code, name = cat.split(',')
    code, name = cat.split('.')
    if '|' in name:
        name = name.split(' | ')[1]
        return code, name.strip()
get_englist('2. Urgences logistiques | Vital Lines')
def get_englist(cat):
    code, name = cat.split('.')
    if '|' in name:
        name = name.split(' | ')[1]
return code, name.strip()
def get_englist(cat):
    code, name = cat.split('.')
    if '|' in name:
        name = name.split(' | ')[1]
    return code, name.strip()
get_englist('2. Urgences logistiques | Vital Lines')
all_cats = get_all_categories(data.CATEGORY)
english_mapping = dict(get_englist(x) for x in all_cats)
english_mapping['2a']
english_mapping['6c']
def get_code(seq):
    return [x.split('.')[0] for x in seq if x]
all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))), index= data.index, columns=code_index)
dummy_frame.ix[:,:6]
for row, cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row, codes] = 1
data = data.join(dummy_frame.add_prefix('category_'))
data.ix[:,10:15]
from mpl_toolkits.basemap import Basemap
from mpl_toolkits import Basemap
