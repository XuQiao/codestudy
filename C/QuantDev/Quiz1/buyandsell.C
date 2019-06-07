#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>

float maxProfit(int N, float prices[]){
    float sum = 0;
    for(int i = 1; i < N; i ++){
        if(prices[i] > prices[i-1])
            sum += (prices[i] - prices[i-1]);
    }
    return sum;
}

int main(int argc, char *argv[]){
    float prices[] = {1,2,3,7,4,8,2,9,10,3,5,1};
    int N = sizeof(prices)/sizeof(float);
    std::cout << "max profit is " << maxProfit(N, prices) << std::endl;
}
