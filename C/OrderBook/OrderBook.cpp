#include <iostream>
#include "OrderBook.h"

int OrderBook::add(string position, int size, float price){
    Order order = Order(currentID, position, size, price);
    orders.push_back(order);
    currentID ++;
    return 0;
}

int OrderBook::remove(int id){
    if (id >= 0 && id < currentID){
        orders.erase(orders.begin() + id);
    }
    return 0;
}


float OrderBook::get_price(string position, int k){ //kth price
    return 1;
}
float OrderBook::get_size(string position, int k){ //kth price
    return 1;
}
int OrderBook::cancel(int id){}
int OrderBook::modify_size(int id, int size){
    Order* order = &orders[id];
    order->size = size;
    return 0;
}

int OrderBook::modify_price(int id, float price){
    Order* order = &orders[id];
    order->price = price;
    return 0;
}

int OrderBook::modify_pos(int id){
    Order* order = &orders[id];
    order->pos = !order->pos;
    return 0;
}

int OrderBook::print(int id_begin, int id_end){
    cout << "ID number" << " Position" << " Price " << " Size" << endl;
    for (int id = id_begin; id < id_end; id ++ ) {
        Order order = orders[id];
        string pos = (order.pos)?" b":" s";
        cout << order.id << pos << " " << order.price << " " << order.size << endl;
    }
    return 0;
}
