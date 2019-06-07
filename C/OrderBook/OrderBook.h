#include <vector>
#include <string>
#include <map>
#include <unordered_map>

struct Order {
    char side; //buy or sell
    int size; //quantity of the order 
    double price; //price of the order
    Order(const char _side, const double _price, const int _size) { //struct constructor
        side = _side;
        size = _size;
        price = _price;
    }
};


class OrderBook {
    private:
        std::unordered_map<int, Order> orders;  //a hashtable to maintain its id->order correspondence
        std::map<double, int> buys, sells; //two maps to get the levels quickly
    public:
        OrderBook();
        void add(const int order_id, const char side, const double price, const int size);
        void modify(const int order_id, const int new_size);
        void remove(const int order_id);
        double get_price(const char side, const int level);
        int get_size(const char side, const int level);
        
        std::pair<double, int> get_level(const char side, const int level);
        friend std::ostream& operator<<(std::ostream&os, const OrderBook& book);
};

