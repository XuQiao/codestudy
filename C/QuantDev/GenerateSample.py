import sys
import os
from datetime import timedelta
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # ----------- readin file to dataframe-------------------
    filename = sys.argv[1] 
    noiselevel = sys.argv[2]
    fraction = float(sys.argv[3])
    lag = int(sys.argv[4])

    df = pd.read_csv(filename, sep=",")
    #df = df[:8000]
    df['Time'] = pd.to_datetime(df['Time'])

    # ----------- deal with the time ------------------------
    df['Exchange'] = "A"
    df['Time_delta'] = (df['Time'] - df['Time'][0]) / np.timedelta64(1,'D') * 24
    #print(df['Time_delta'][:10])

    #----------- plot the original data ---------------------
    plt.figure()
    #df.plot(x='Time_delta', y='Price', style='o',s=1)
    plt.scatter(df['Time_delta'], df['Price'], s = 1)
    plt.ylabel('stock price')
    plt.xlabel('time in hour(starting from 09:30 2017-04-18')
    plt.legend(loc='best')
    plt.savefig('plotbefore.png')


    #----------- randomly select exchange into B and plot ---
    noiselevel = 'None'
    df_B, df_A = AddingAnotherExchange(df, noiselevel, fraction, lag)
    df = pd.concat([df_A,df_B])
    df = df.sort_values('Time') 
    plt.figure()
    plt.ylabel('stock price')
    plt.xlabel('time in hour(starting from 09:30am 2017-04-18)')
    plt.scatter(df_A['Time_delta'], df_A['Price'], s = 0.5, color='r')
    plt.scatter(df_B['Time_delta'], df_B['Price'], s = 0.5, color='b')
    plt.legend(loc='best')
    plt.legend(['Exchange B','Exchange A'])
    plt.savefig('plotafter{}_frac{}_lag{}.png'.format(noiselevel,fraction,lag))


    # ----------- save to output ---------------------------
    df.to_csv('sampled_{}_frac{}_lag{}.txt'.format(noiselevel,fraction,lag), sep=" ",columns=['Time_delta','Price','Size','Exchange'], index=None)

#  ------------- use dataframe to randomly sample exchange B with fraction given, lag given, add noise in the dataset ------
def AddingAnotherExchange(df, noiselevel = 'Gaus', fraction = 0.35, lag = 30):
    lag = lag / 60 / 60 / 1e6
    meanP = df['Price'].mean()
    if noiselevel == 'None':
        pass
    elif noiselevel == 'Gaus':
        noise_price = np.random.normal(0,0.1,size=len(df))
        noise_time = np.random.normal(0,lag/10,size=len(df))
        noise_time = noise_time.tolist()
        df['Price'] = df['Price'] + noise_price
        df['Time'] = df['Time'] + noise_time
    elif noiselevel == 'Laplace':
        noise_price = np.random.laplace(0,0.1,size=len(df))
        noise_time = np.random.laplace(0,lag/10,size=len(df))
        noise_time = noise_time.tolist()
        df['Price'] = df['Price'] + noise_price
        df['Time'] = df['Time'] + noise_time
    
    df_B = df.sample(frac = fraction, replace = False)
    df_A = df.drop(df_B.index)
    df_B['Exchange'] = 'B'
    df_B['Time_delta'] = df_B['Time_delta'] + lag

    return df_A, df_B

# ----------- run it  ----------
if __name__ == "__main__":
    main()
