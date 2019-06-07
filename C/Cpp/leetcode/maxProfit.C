#include <iostream>
#include <vector>
int maxprofit(std::vector<int> prices){
    int minprice = prices[0];
    int maxprofit = 0;
    for(int i = 0;i<prices.size(); i++){
        if(prices[i] < minprice){
            minprice = prices[i];
        }
        if(prices[i] - minprice > maxprofit){
            maxprofit = prices[i] - minprice;
        }
    }
    return maxprofit;
}

int main(){
    std::vector<int> prices = {2,1,2,1,0,1,2};//{7,3,8,2,10,1,6};
    std::cout<<"max profit is " << maxprofit(prices) <<std::endl;
}
