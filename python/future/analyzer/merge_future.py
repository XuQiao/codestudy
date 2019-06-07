import os
import time
import pandas as pd
import numpy as np
from constants import *
from func import *

def merge_future():
    t0 = time.time()
    columns = ['date','open','high','low','close','unknown','volume']
    dfs = []
    filename_tot = 'data/'+symbol+'_full_'+contractType+'_future.csv'
    with open(filename_tot, 'r') as f_tot:
        df_tot = pd.read_csv(f_tot, delimiter='\t', index_col=0)

    filename_matrix = 'data/'+symbol+'_matrix_full_'+contractType+'_future.csv'
    with open(filename_matrix, 'r') as f_matrix:
        df_matrix_tot = pd.read_csv(f_matrix, delimiter='\t', index_col=0)

    lastdate = df_matrix_tot.at[df_matrix_tot.index[last_nonnan(df_matrix_tot['flag'])], 'date']

    for i in range(len(types)):
        type = types[i]
        filename = 'data/'+symbol+'_'+type+'_'+contractType+'_future.csv'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                df = pd.read_csv(f, header=None,index_col=0)
                df.columns = columns
                dfs.append(df)
    df_tot = pd.concat(dfs, ignore_index=True)
#    df_tot.drop_duplicates(['date','close'], take_first=True)
    df_tot['date'] = df_tot['date'] / 1000
    df_tot = df_tot.sort_values('date')
    df_tot = df_tot.reset_index(drop=True)
    df_matrix_tot = df_matrix_tot.sort_values('date')
    df_matrix_tot = df_matrix_tot.reset_index(drop=True)

    with open(filename_tot, 'w') as f:
        df_tot.to_csv(f, sep = '\t')

    startindex = df_tot['date'].searchsorted(lastdate)[0]
    startindex1 = df_matrix_tot['date'].searchsorted(lastdate)[0]
#    train_time = time.time() - t0
#    print("train time: %0.3fs" % train_time)

    df_matrix = calcTA(df=df_tot, startindex=0)
#    df_matrix = pd.concat([df_matrix_tot.iloc[:startindex1], df_matrix.iloc[startindex:]], ignore_index=True)
    t0 = time.time()
    df_matrix = df_matrix.sort_values('date')
    df_matrix = df_matrix.reset_index(drop=True)
#    train_time = time.time() - t0
#    print("train time: %0.3fs" % train_time)
#    t0 = time.time()

    with open(filename_matrix, 'w') as f_matrix:
        df_matrix.to_csv(f_matrix, sep = '\t')

