#include <iostream>
#include "OrderBook.h"

OrderBook::OrderBook(){  //constructor and initialization
    buys.clear(); 
    sells.clear(); 
    orders.clear(); 
}

void OrderBook::add(const int order_id, const char side, const double price, const int size){ //function to add orders
    if (side == 'B')
        buys[price] += size;
    else if(side == 'S') 
        sells[price] += size;
    else std::cout << " WRONG Position ! Invalid Transaction." << std::endl;

    Order order(side, price, size);
    orders.insert(std::make_pair(order_id, order));
}

void OrderBook::modify(const int order_id, const int new_size){ //function to modify orders given order_id
    std::unordered_map<int, Order>::iterator got = orders.find (order_id);
    if ( got == orders.end() ) {
        std::cout << "not found" << std::endl;
    }
    else {

        //retreive information from the hashtable
        char side = got->second.side;
        double price = got->second.price;
        int size = got->second.size;
        if (side == 'B')
            buys[price] += new_size - size;
        else if(side == 'S') 
            sells[price] += new_size - size;
        
        // if some price level has size 0, erase it from the maps
        if (buys[price] == 0) {
            buys.erase(price);
        }
        if (sells[price] == 0) {
            sells.erase(price);
        }
        got->second.size = new_size;
    }
}

void OrderBook::remove(const int order_id){ //function to remove orders given order_id
    //call modify function
    this->modify(order_id, 0);

    std::unordered_map<int, Order>::const_iterator got = orders.find (order_id);
    if ( got == orders.end() ) {
        std::cout << "not found" << std::endl;
    }
    else {
        orders.erase(got);
    }
}


double OrderBook::get_price(const char side, const int level){ //function to get price of price level k
    return get_level(side, level).first;
}

int OrderBook::get_size(const char side, const int level){ //function to get size of price level k
    return get_level(side, level).second;
}

std::pair<double, int> OrderBook::get_level(const char side, int level){ // level'th
    std::map<double, int> table;
    if (side == 'B')
        table = buys;
    else if(side == 'S'){
        table = sells;
        level = table.size() - level + 1;  //sell is the reversed order
    }

    if (level > table.size() || level < 1)
        return std::pair<double, int>(-1, -1);

    //the map is ordered from highest to lowest price
    int count = 0; std::pair<double, int> pair;
    for (auto it = table.rbegin(); it!= table.rend(); ++it ) {
        count ++;
        if(count == level){
            pair = std::pair<double, int>(it->first, it->second);
            break;
        }
    }
    return pair;
}

std::ostream& operator<<(std::ostream&os, const OrderBook& book){ //own written function to display the price level table in the book
    //Usage: cout << *this << endl;
    for (auto it = book.sells.rbegin(); it!= book.sells.rend(); ++it ) {
        os << it->first << "\t" << it->second << std::endl;
    }
    os << std::endl;
    for (auto it = book.buys.rbegin(); it!= book.buys.rend(); ++it ) {
        os << it->first << "\t" << it->second << std::endl;
    }
    return os;
}
