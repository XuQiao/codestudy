
import pandas as pd
from pandas import DataFrame, Series
path = 'pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
import json
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'UnKnown'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)

from matplotlib.pyplot import draw, show, ion, close
ion()
show()
close()
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]
cframe = frame[frame.a.notnull()]
import numpy as np
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','NotWindows')
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','NotWindows')
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','NotWindows')
operating_system[:5]
by_tz_os = cframe.groupby(['tz',operating_system])
by_tz_os
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]
agg_counts[:10]
indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind='barh', stacked=True)
close()
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh',stacked=True)
get_ipython().magic(u'save -a 1-10')
