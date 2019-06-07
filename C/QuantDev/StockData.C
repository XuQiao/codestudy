#include "StockData.h"
#include <sstream>

//constructor function from input numbers
stock_data::stock_data(const double &_time, const double &_price, const std::string &_exchange){
    time = _time;
    price = _price;
    exchange = _exchange;
}

//constructor function from input string
stock_data::stock_data(const std::string &t){ // read information from string
    ticker = "GOOG";
    std::stringstream ss(t);
    ss >> time;
    ss >> price;
    ss >> size;
    ss >> exchange;
}
