from func import calcfi
import pandas as pd
from constants import *

filename_matrix = 'data/'+symbol+'_matrix_full_'+contractType+'_future.csv'
with open(filename_matrix,'r') as f_matrix:
    df_matrix = pd.read_csv(f_matrix, header = 0,index_col=0,sep='\t')

df_matrix=df_matrix[:100]
df = pd.DataFrame({'date':[1,2,3,4,5,6],'close':[10,20,30,15,5,25]})
df_matrix['flag_true'] = calcfi(df_matrix,25)
print df_matrix[['date','close','flag','flag_true']][::5]
