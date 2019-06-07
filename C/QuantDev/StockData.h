#ifndef _STOCK_DATA_H
#define _STOCK_DATA_H
#include <string>
#include <iostream>

//Simply capsulation to store the stock data tick information
class stock_data{
    public:
        stock_data(const double &_time, const double &_price, const std::string &_exchange);
        ~stock_data(){};
        stock_data(const std::string& t);
        double get_time() const{ return time;}
        double get_price() const{ return price;}
        std::string get_exchange() const{ return exchange;}
        
    private:
        double time;
        std::string ticker;
        double price;
        float size;
        std::string exchange;
};

#endif
