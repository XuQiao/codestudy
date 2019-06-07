from pandas import DataFrame
df1 = DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = DataFrame({'key':['a','b','d'],'data2':range(3)})
df1
df2
pd.merge(df1,df2)
import pandas as pd
pd.merge(df1,df2)
pd.merge(df1,df2,on='key')
df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
df4 = DataFrame({'rkey':['a','b','d'],'data2':range(3)})
pd.merge(df3,df4,left_on='lkey',right_on='rkey')
pd.merge(df1,df2,how='outer')
df1 = DataFrame({'key':['b','b','a','c','a','b'],'data1': range(6)})
df2 = DataFrame({'key':['a','b','a','b','d'],'data2': range(5)})
df1
df2
pd.merge(df1,df2,on='key',how='left')
pd.merge(df1,df2,how='inner')
pd.merge(df1,df2,how='outer')
left = DataFrame({'key1':['foo','foo','bar'],'key2':['one','two','one'],'lval':[1,2,3]})
right = DataFrame({'key1':['foo','foo','bar','bar'],'key2':['one','one','one','two'],'lval':[4,5,6,7]})
pd.merge(left,right,on=['key1','key2'],how='outer')
left
right
pd.merge(left,right,on=['key1','key2'],how='inner')
pd.merge(left,right,on=['key1','key2'],how='left')
pd.merge(left,right,on=['key1','key2'],how='right')
pd.merge(left,right,on='key1')
pd.merge(left,right,on='key1',suffixes=('_left','_right')(
)
)
pd.merge(left,right,on='key1',suffixes=('_left','_right'))
left1 = DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
right1 = DataFrame({'group_val':[3.5, 7]}, index=['a','b'])
left1
right1
pd.merge(left1,right1,left_on='key',right_index=True)
pd.merge(left1,right1,left_on='key')
pd.merge(left1,right1,left_on='key',right_index=True,how='outer')
lefth = DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada
lefth = DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],'key2':[2000,2001,2002,2001,2002],'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6,2)),index=[['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],[2001,2000,2000,2000,2001,2002]],columns=['event1','event2'])
left
righth
pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)
lefth
pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='outer')
left2= DataFrame([[1.,2.],[3.,4.],[5.,6.]], index=['a','c','e'], columns=['Ohio','Nevada'])
right2 = DataFrame([[7.,8.],[9.,10.], [11.,12.], [13.,14.]],index=['b','c','d','e'],columns=['Missouri','Alabama'])
left2
right2
pd.merge(left2,right2,how='outer',left_index=True,right_index=True)
left2.join(right2,how='outer')
left1.join(right1,on='key')
another = DataFrame([[7.,8.],[9.,10.],[11,12.],[16,17]],index=['a','c','e','f'],columns=['New York','Oregon'])
left2.join([right2,another])
left2.join([right2,another],how='outer')
arr = np.arange(12).reshape((3,4))
arr
np.concatenate([arr,arr], axis=1)
s1 = Series([0,1],index=['a','b'])
from numpy import Series
from pandas import Series
s1 = Series([0,1],index=['a','b'])
s2 = Series([2,3,4],index=['c','d','e'])
s3= Series([5,6],index=['f','g'])
pd.concat([s1,s2,s3])
pd.concat([s1,s2,s3],axis=1)
s4=  pd.concat([s1*5,s3])
pd.concat([s1,s4],axis=1)
s1*5
s4
pd.concat([s1,s4],axis=1,join='inner')
pd.concat([s1,s4],axis=1,join_axes=[['a','c','b','e']])
pd.concat([s1,s1,s3],keys=['one','two','three'])
result
result =  pd.concat([s1,s1,s3],keys=['one','two','three'])
result.unstack()
pd.concat([s1,s2,s3],axis=1,keys=['one','two','three'])
df1 = DataFrame(np.arange(6).reshape(3,2), index=['a','b','c'],columns=['one','two'])
df2 = DataFrame(5 + np.arange(4).reshape(2,2),index=['a','c'], columns=['three','four'])
pd.concat([df1,df2],axis=1,keys=['level1','level2'])
df1
df2
pd.concat({'level1':df1,'level2':df2},axis=1)
pd.concat([df1,df2],axis=1,keys=['level1','level2
pd.concat([df1,df2],axis=1,keys=['level1','level2'],names=['upper','lower'])
df1 = DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
df2 = DataFrame(np.random.randn(2,3),columns=['b','d','a'])
df1
df2
pd.concat([df1,df2],ignore_index=True)
a = Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],index=['f','e','d','c','b','a'])
b=Series([np.arange(len(a),dtype=np.float64),index=['f','e','d','c','b','a'])

)
b=Series(np.arange(len(a),dtype=np.float64),index=['f','e','d','c','b','a'])
b[-1] = np.nan
a
b
np.where(pd.isnull(a),b,a)
b[:-2].combine_first(a[2:])
b[:-2]
df1 = DataFrame({'a':[1.,np.nan,5.,np.nan],'b':[np.nan,2.,np.nan,6.],'c':range(2,18,4)})
df2 = DataFrame({'a':[5.,4,np.nan,3.,7.],'b':[np.nan,3.,4.,6.8.]})
df2 = DataFrame({'a':[5.,4,np.nan,3.,7.],'b':[np.nan,3.,4.,6.,8.]})
df1.combine_first(df2)
df1
df2
data = DataFrame(np.arange(6),reshape((2,3)), index=pd.Index(['Ohio','Colorado'],name='state'),columns = pd.Index(['one','two','three'],name='number'))
data = DataFrame(np.arange(6).reshape((2,3)), index=pd.Index(['Ohio','Colorado'],name='state'),columns = pd.Index(['one','two','three'],name='number'))
data
result=data.stack()
result
result.unstrack(0)
result.unstack(0)
result.unstack('state')
s
s1
s1 = Series([0,1,2,3],index=['a','b','c','d'])
s2=Series([4,5,6],index=['c','d','e'])
data2 = pd.concat([s1,s2],keys=['one','two'])
data2
data2.unstrack()
data2.unstack()
data2.unstack().stack()
data2.unstack().stack(dropna=False)
df = DataFrame({'left': result,'right': result+5},colums = pd.Index(['left','right'],name='side'))
df = DataFrame({'left': result,'right': result+5},columns = pd.Index(['left','right'],name='side'))
df
df.unstack('state')
df.unstack('side')
df.unstack('state').stack('side')
ldata[:10]
!vi pythonio.py
data = DataFrame({'k1':['one'] * 3 + ['two'] * 4, 'k2':[1,1,2,3,3,4,4]})
data
data.duplicated()
data.drop_duplicated()
data.drop_duplicates()
data['v1'] = range(7)
data.drop_duplicates(['k1'])
data.drop_duplicates(['k1','k2'],take_last=True)
data.drop_duplicates(['k1','k2'],keep='last')
data = DataFrame({'food':['bacon','pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami','honey ham','nova lox'],'ounces':[4,3,12,6,7,.5,8,3,5,6]})
data = DataFrame({'food':['bacon','pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami','honey ham','nova lox'],'ounces':[4,3,12,6,7.5,8,3,5,6]})
data
meat_to_animal = {'bacon':'pig','pulled pork':'pig','pastrami':'cow','corned beef':'cow','honey ham':'pig','nova lox':salmon'}
meat_to_animal = {'bacon':'pig','pulled pork':'pig','pastrami':'cow','corned beef':'cow','honey ham':'pig','nova lox':'salmon'}
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data
data['food'].map(lambda x: meat_to_animal[x.lower])
data['food'].map(lambda x: meat_to_animal[x.lower()])
data = Series([1.,-999,2.,-999,-1000,3.])
data
data.replace(-999,np.nan)
data.replace([-999,-1000],np.nan)
data.replace([-999,-1000],[np.nan,0])
data.replace({-999:np.nan,-1000:0})
data = DataFrame(np.arange(12).reshape((3,4)),index=['Ohio','Colorado','New York'],columns=['one','two','three','four'])
data.index.map(str.upper)
data.index=data.index.map(str.upper)
data
data.rename(index=str.title,columns=str.upper)
str
str.title
data.rename(index={'OHIO':'INDIANA},columns={'three':'peekaboo'})
data.rename(index={'OHIO':'INDIANA'},columns={'three':'peekaboo'})
_ = data.rename(index={'Ohio':'INDIANA'},inplace=True)
data
ages=  [20 ,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
cats=pd.cut(ages,bins)
cats
cats.labels
cats.codes
cats.levels
cats.categories
pd.value_counts(cats)
pd.cut(ages,[18,26,36,61,100],right=False)
group_names={'Youth','YoungAdult','MiddleAges','Senior']
group_names=['Youth','YoungAdult','MiddleAges','Senior']
pd.cut(ages,bins,labels = group_names)
data = np.random.randn(20)
pd.cut(data,4,precision=2)
data = np.random.randn(1000)
cats = pd.qcut(data,4)
cats
pd.value_counts(cats)
pd.qcut(data,[0,0.1,0.5,0.9,1.])
pd.value_counts(cats)
cats = pd.value_counts(cats)
pd.value_counts(cats)
cats =pd.qcut(data,[0,0.1,0.5,0.9,1.])
pd.value_counts(cats)
np.random.seed(12345)
data = DataFrame(np.random.randn(1000,4))
data.describe
data.describe()
col=data[3]
col[np.abs(col)>3]
data[(np.abs(col)>3).any(1)]
data[(np.abs(data)>3).any(1)]
data[np.abs(data)>3]=np.sign(data)*3
data.describe()
df = DataFrame(np.arange(5*4),reshape(5,4))
df = DataFrame(np.arange(5*4),reshape((5,4)))
df = DataFrame(np.arange(5*4).reshape((5,4)))
df
sampler  = np.random.permutation(5)
sampler
df
df.take(sampler)
df.take(np.random.permutation(len(df))[:-3])
df.take(np.random.permutation(len(df))[:3])
bag = np.array([5, 7, -1, 6, 4])
sampler = np.random.randint(0,leg(bag), size=10)
sampler = np.random.randint(0,len(bag), size=10)
sampler
draws = bag.take(sampler)
draws
df  = DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})
pd.get_dummies(df['key'])
df['key']
dummiers = pd.get_dummies(df['key'],prefix='key')
df_with_dummy = df[['data']].join(dummies)
df_with_dummy = df[['data1']].join(dummies)
df_with_dummy = df[['data1']].join(dummiers)
df_with_dummy
nmames = ['movie_id','title','genre']
values= np.random.rand(10)
values
bins = [0,.2,0.4,0.6,0.8,1.0]
pd.get_dummies(pd.cut(values,bins))
val = 'a, b, guido'
val.split(',')
pieces = [x.strip() for x in val.split(',')]
pieces
first, second, third = pieces
first+'::'+second+'::'+third
'::'.join(pieces)
'guido' in val
val.index(',')
val.find(':')
val.index(':')
val.count('',')
val.count(',')
val.replace(',','::')
val.replace(',','')
val.replace(',','')
import re
text = "foo    bar\t baz   \tqux"
re.split('\s+',text)
regex= re.compile('\s+')
regex
regex.split(text)
regex.findall(text)
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern,flags = re.IGNORECASE)
m = regex.match('wesm@bright.nex')
m.groups()
regex.findall(text)
data = {'Dave':'dave@google.com','Steve':'steve@gmail.com','Rob':'rob@gmail.com','Wes':np.nan}
data=Series(data)
data
data.isnull()
data.str.contains('gmail')
pattern
data.str.findall(pattern, flags=re.IGNORECASE)
matches=data.str.match(pattern,flags = re.IGNORECASE)
matches
matches.str.get(1)
matches.str[0]
matches.str[:5]
data.str[:5]
import json
db = json.load('pydata-book/ch07/foods-2011-10-03.json')
db = json.load(open('pydata-book/ch07/foods-2011-10-03.json'))
len(db)
db[0].keys)_
db[0].keys()
db[0]['nutrients'][0]
db[0]['nutrients']
nutrients = DataFrame(db[0]['nutrients']
)
nutrients[:7]
info_keys = ['description','group','id','manufacturer']
info = DataFrame(db,columns = info_keys)
info[:5]
db
info
pd.value_counts(info.group)[:10]
pd.value_counts(info.group)[:100]
nutrients = []
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients,ignore_index=True)
nutrients
nutrients.duplicated().sum()
nutrients.duplicated()
nutrients.drop_duplicated()
nutrients.drop_duplicates()
nutrients = nutrients.drop_duplicates()
col_mapping = {'description':'food', 'group':'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
info
nutrients
ndata = pd.merge(nutrients,info,on='id',how='outer')
ndata
ndata.ix[30000]
result = ndata.groupby(['nutrient','fgroup'])['value'].quantile(0.5)
result = ndata.groupby(['description','fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].order().plot(kind='barh')
result['Zinc, Zn'].sort_values().plot(kind='barh')
by_nutrient = ndata.groupby(['group','description'])
get_maximum = lambda x:x.xs(x.value.idxmax())
get_minimum = lambda x:x.xs(x.value.idxmin())
max_foods = by_nutrient.apply(get_maximum)['value','food']
max_foods = by_nutrient.apply(get_maximum)[['value','food']]
max_foods.food = max_foods.food.str[:50]
max_foods.ix['Amino Acid']['food']
max_foods.ix['Amino Acids']['food']
max_foods
max_foods.ix['Amino Acids']['food']
max_foods.ix['Amino Acids']
max_foods.ix['Amino Acids']['food']
%history -f datawrange.py
