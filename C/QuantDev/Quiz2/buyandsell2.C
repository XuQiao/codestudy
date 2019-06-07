#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>
using namespace std;
//profit[t][i] = max(profit[t][i-1], max(price[i] – price[j] + profit[t-1][j]))

float maxProfit(int N, float prices[]){
    float profit[N];
    for (int i=0; i<N; i++)
        profit[i] = 0;
 
    /* Get the maximum profit with only one transaction
       allowed. After this loop, profit[i] contains maximum
       profit from price[i..n-1] using at most one trans. */
    int max_price = prices[N-1];
    for (int i=N-2;i>=0;i--)
    {
        // max_price has maximum of price[i..n-1]
        if (prices[i] > max_price)
            max_price = prices[i];
 
        // we can get profit[i] by taking maximum of:
        // a) previous maximum, i.e., profit[i+1]
        // b) profit by buying at price[i] and selling at
        //    max_price
        profit[i] = max(profit[i+1], max_price-prices[i]);
    }
 
    /* Get the maximum profit with two transactions allowed
       After this loop, profit[n-1] contains the result */
    int min_price = prices[0];
    for (int i=1; i<N; i++)
    {
        // min_price is minimum price in price[0..i]
        if (prices[i] < min_price)
            min_price = prices[i];
 
        // Maximum profit is maximum of:
        // a) previous maximum, i.e., profit[i-1]
        // b) (Buy, Sell) at (min_price, price[i]) and add
        //    profit of other trans. stored in profit[i]
        profit[i] = max(profit[i-1], profit[i] + (prices[i]-min_price) );
    }
    int sum = profit[N-1];

    return sum;
}

float maxProfit(int N, int k, float prices[]){
    // table to store results of subproblems
    // profit[t][i] stores maximum profit using
    // atmost t transactions up to day i (including
    // day i)
    float profit[k+1][N+1];
 
    // For day 0, you can't earn money
    // irrespective of how many times you trade
    for (int i = 0; i <= k; i++)
        profit[i][0] = 0;
 
    // profit is 0 if we don't do any transation
    // (i.e. k =0)
    for (int j= 0; j <= N; j++)
        profit[0][j] = 0;
 
    // fill the table in bottom-up fashion
    for (int i = 1; i <= k; i++)
    {
        for (int j = 1; j < N; j++)
        {
            float max_so_far = prices[0];
 
            for (int m = 0; m < j; m++)
                max_so_far = max(max_so_far,prices[j] - prices[m] + profit[i-1][m]);
 
            profit[i][j] = max(profit[i][j-1], max_so_far);
        }
    }
 
    return profit[k][N-1];
}

int main(int argc, char *argv[]){
    float prices[] = {1,2,3,7,4,8,2,9,10,3,5,1};
    int N = sizeof(prices)/sizeof(float);
    int k = 3;
	std::cout << "max profit for 2 transactions is " << maxProfit(N,prices) << std::endl;
	std::cout << "max profit for " << k << " transactions is " << maxProfit(N,k, prices) << std::endl;
}
