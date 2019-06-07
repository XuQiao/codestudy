import pytest
import datetime
import gdax
import time
import matplotlib.pyplot as plt
import numpy as np
from okex.core import OKExAPI

def get_history_gdax(object='BTC-USD'):
    client = gdax.PublicClient()
    history = client.get_product_historic_rates(object, granularity=60)
    history = list(reversed(history))
    time = [array[0] for array in history]
    timestr = [datetime.datetime.fromtimestamp(dtime) for dtime in time]
    price = [array[3] for array in history]
#    plt.plot(timestr, price)
#    plt.gcf().autofmt_xdate()
    return (time, price)

def get_history_okex():
    client = OKExAPI(apikey='',secret='')
    client.get('exchange_rate')
    ticker_price = client.get('future_ticker',symbol='btc_usd',contract_type='quarter',future=True)
    history = client.get('future_kline',symbol='btc_usd',contract_type='next_week',type='1min')
    history = list(reversed(history))
    time = [array[0]/1000 for array in history]
    timestr = [datetime.datetime.fromtimestamp(dtime) for dtime in time]
    price = [array[3] for array in history]
#    plt.plot(timestr, price)
#    plt.gcf().autofmt_xdate()
#    plt.xlim(datetime.datetime.now()-datetime.timedelta(days=1)),datetime.datetime.now(),
#    plt.show()
    return (time, price)

#shift the time series by time lag t, -200 ms < t < 200 ms, 1 hour = 60 min = 60 * 60 s = 1e6 * 60 * 60 ms
def shiftandinterpolate(At, A, Bt, B, lag):
    assert(len(At)==len(A))
    assert(len(Bt)==len(B))
    #shift time series A by lag t
    At_lag = np.array(At) + lag
    Atint = []
    Aint = []
    iter_start = 1

    #Interpolate on time series A, applying B
    for i in range(len(Bt)):
        time_B = Bt[i]
        if time_B <= At_lag[0] or time_B > At_lag[len(At_lag)-1]:
            price_int = B[i]
            Atint.append(time_B)
            Aint.append(price_int)

        for i in range(iter_start, len(At_lag)-1):
            time_A = At_lag[i]
            time_A_next = At_lag[i+1]

            if time_B >= time_A and time_B < time_A_next:   #find the time interval where B locates at A
                price = A[i]
                price_next = A[i+1]
            # Two point interpolations
                price_int = ((price_next - price) * time_B + (price * time_A_next - price_next * time_A)) / (time_A_next - time_A)
                Atint.append(time_B)
                Aint.append(price_int)
                iter_start = i - 2
                break
#    plt.plot(Atint, np.array(Aint)*0.9)
#    plt.show()
    return (Atint, Aint)

def MLE(A, B):
    sumLS = 0
    for i in range(len(B)):
        price_B = B[i]
        price_A = A[i]
        diff2 = (price_B - price_A) * (price_B - price_A)
        sumLS = sumLS + diff2
    return sumLS

#calculate the cross correlation
def cross_corr(A, B):
    meanA = np.mean(A)
    meanB = np.mean(B)
    sigmaA = np.std(A)
    sigmaB = np.std(B)

    #cross product
    crosssum = 0
    for i in range(len(B)):
        price_B = B[i]
        price_A = A[i]
        crosssum = crosssum + (price_A - meanA) * (price_B - meanB)

    denom = np.sqrt(sigmaA*sigmaB);

    #crosssum = crosssum / len(B)
    if denom:
        return crosssum / denom

def main():
        #for a grid of lags from -100 ms to 100ms, we loop to see how our delayed A cross correlates with B, and select the maximum correlation from the results the print out the best estimated lag
        #max_crosscorr = 0;
        #true_lag_cross = 0;
        #min_ls = 0;
        #true_lag_mle = 0;
    gdax = get_history_gdax()
    #gdax_eth = get_history_gdax('ETH-USD')
    okex = get_history_okex()
    At = gdax[0]
    A = gdax[1]
    Bt = okex[0]
    B = okex[1]
    crosscorr = []
    ls = []
    lags = np.arange(-1.,1.,0.01)
    for lag in lags:
        Atint = shiftandinterpolate(At, A, Bt, B, lag)[0]
        Aint = shiftandinterpolate(At, A, Bt, B, lag)[1]
        if(len(Aint) < len(B)):
            Aint.append(B[len(B)-1])
        if(len(Aint) > len(B)):
            del(Aint[-1])

        corr = cross_corr(Aint, B)
        mle = MLE(Aint, B)
        crosscorr.append(corr)
        ls.append(mle)
        print(corr, mle)

    true_lag_cross = np.max(crosscorr)
    true_lag_mle = np.min(ls)
    lag_0 = lags[np.argmax(crosscorr)]
    lag_1 = lags[np.argmin(ls)]
    print("B is lagged by {0} s using cross correlation, the correlation is {1}".format(lag_0,true_lag_cross))
    print("B is lagged by {0} s using least square, the MLE is {1}".format(lag_1, true_lag_mle))


if __name__ == '__main__':
    main()
