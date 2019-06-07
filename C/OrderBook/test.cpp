#include "OrderBook.h"
#include <random>

int main(){
    OrderBook book;
    book.init();
    std::default_random_engine generator1;
    std::uniform_real_distribution<double> distribution(0,1);
    std::default_random_engine generator2;
    std::normal_distribution<double> normal_distribution(5.0,0.01);
    for (int i = 0; i < 1000; i ++){
        float rand1 = distribution(generator1); 
        float rand2 = static_cast<int>(distribution(generator1) * 1000); 
        float rand3 = normal_distribution(generator2) * 100; 
        if(rand1<0.5) book.add("b",rand2, rand3);
        else book.add("s",rand2, rand3);
    }
    book.remove(2);
    book.modify_price(3, 1.9);
    book.print(3, 500);
    return 0;
}
