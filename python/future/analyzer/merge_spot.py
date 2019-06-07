import os
import pandas as pd
from constants import *
from func import *

def merge_spot():
    columns = ['date','open','high','low','close','volume']
    dfs = []
    filename_tot = 'data/'+symbol+'_full'+'_spot.csv'
    filename_matrix = 'data/'+symbol+'_matrix_full'+'_spot.csv'

    with open(filename_tot, 'r') as f_tot:
        df_tot = pd.read_csv(f_tot, delimiter='\t', index_col=0)
        df_tot = df_tot.sort_values('date')
        lastdate = df_tot.at[df_tot.index[-1], 'date']

    for i in range(len(types)):
        type = types[i]
        filename = 'data/'+symbol+'_'+type+'_spot.csv'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                df = pd.read_csv(f, header=None,index_col=0)
                df.columns = columns
                dfs.append(df)
    df_tot = pd.concat(dfs, ignore_index=True)
    df_tot['date'] = df_tot['date'] / 1000
    #df_tot.sort_index(inplace=True)
    df_tot = df_tot.sort_values('date')
    df_tot.reset_index(drop=True)
#    startindex = df_tot['date'].searchsorted(lastdate)[0]

    with open(filename_tot, 'w') as f:
        df_tot.to_csv(f, sep = '\t')

#    df_matrix = calcTA(df_tot, 0)

#    with open(filename_matrix, 'w') as f_matrix:
#        df_matrix.to_csv(f_matrix, sep = '\t')
