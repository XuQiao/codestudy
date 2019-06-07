import numpy as np
M = 500
ind_names = np.array(['F','T'])
N = 1000
sampler = np.random.randint(0,len(ind_names),N)
import string
import random
def rands(n):
    choices = string.ascii_uppercase
    return ''.join([random.choice(choices) for _ in xrange(n)])
tickers = np.array([rands(5) for _ in xrange(N)])
import pandas
industries= pandas.Series(ind_names[sampler],index=tickers,name='industry')
df=pandas.DataFrame({'Momentum':np.random.randn(500) / 200 + 0.03, 'Value':np.random.randn(500)/ 200 + 0.08, 'ShortInterest':np.random.randn(500) /200 - 0.02},index=tickers[:500])
by_industry  = df.groupby(industries)
by_industry.mean()
by_industry.describe()
by_industry
def zscore(group):
    return (group-group.mean())/group.std()
df_stand=by_industry.apply(zscore)
df_stand.groupby(industries).agg(['mean','std'])
ind_rank = by_industry.rank(ascending=False)
ind_rank.groupby(industries).agg(['min','max'])
by_industry.apply(lambda x:zscore(x.rank()))
by_industry.apply(lambda x:zscore(x.rank())).describe()
pyfinance1.py
