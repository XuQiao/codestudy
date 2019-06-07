a=1
from pandas import Series, DataFrame
import pandas as pd
obj = Series([4, -7, -5, 3])
obj
obj.value
obj.values
obj.valid
obj.index
obj.values
obj.index
obj = Series([4, -7, -5, 3], index=['d','b','a','c'])
obj2
obj = Series([4, -7, -5, 3], index=['d','b','a','c'])
obj2 = Series([4, -7, -5, 3], index=['d','b','a','c'])
obj2
obj2.index
obj['a']
obj[1]
obj[2]
obj['c']
obj['d']=6
obj[['c','a','d']]
obj2
obj
obj2 = obj
obj2
obj2[obj2>0]
obj2*2
np.exp(obj2)
import numpy as np
np.exp(obj2)
'b' in obj2
'e' in obj2
12 in obj2
sdata = {'Ohio':3500,'Texas':7100}
obj3=Series(sdata)
obj3
stats = ['California','Ohio']
obj4 = Series(sdata,index=states)
obj4 = Series(sdata,index=sttes)
obj4 = Series(sdata,index=stats)
obj4
obj4.isnull
obj4.isnull()
obj4.notnull()
obj3+obj4
obj
obj3
obj4
obj3+obj4
obj4.name='population'
obj4.index.name='state'
obj4
obj4.index=['C','T']
obj4
obj4.index=['C','T','R']
obj4.index=['C'']
obj4.index=['C']
obj4.index=['C','R']
obj4
obj4.index.name='state'
obj4
%save
%save -a serieslearn.py
%save -a 'serieslearn.py'
%save serieslearn.py
%history -f serieslearn.py
