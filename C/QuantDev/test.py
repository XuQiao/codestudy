import sys
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

def main():
    filename = sys.argv[1] 
    df = pd.read_csv(filename, sep=" ",names=['lag','corr'])

    # ----------- deal with the time ------------------------
    plt.figure()
    #plt.yscale('log')
    plt.scatter(df['lag'], df['corr'], s = 1)
    plt.legend(loc='best')
    plt.savefig('{}corr.png'.format(filename))

# ----------- run it  ----------
if __name__ == "__main__":
    main()
