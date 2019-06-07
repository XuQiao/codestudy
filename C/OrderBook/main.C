#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "OrderBook.h"
std::vector<std::string> split(const std::string &s, char delim);

int main(int argc, char* argv[]){
    if (argc > 2) {
        std::cout << "Usage: " << argv[0] << " <filename> " << std::endl;
        std::cout << "Only one file a time!" << std::endl; //Usage
        return 1;
    }
    std::string filename = argv[1]; //filename passed from command line
    
    std::ifstream infile(filename);
    std::string line; 

    OrderBook *book = new OrderBook(); //main object

    //read in file 
    while (getline(infile, line)) { 
        std::vector<std::string> commands = split(line, ' ');
        if(commands[0] == "add"){
            int order_id = std::stoi(commands[1]);
            char side = commands[2].c_str()[0];
            double price = std::stod(commands[3]);
            int size = std::stoi(commands[4]);
            book->add(order_id, side, price, size);
        }
        else if(commands[0] == "modify"){
            int order_id = std::stoi(commands[1]);
            int new_size = std::stod(commands[2]);
            book->modify(order_id, new_size);
        }
        else if(commands[0] == "remove"){
            int order_id = std::stoi(commands[1]);
            book->remove(order_id);
        }
        else if(commands[0] == "get" && commands[1] == "price"){
            char side = commands[2].c_str()[0];
            int level = std::stoi(commands[3]);
            std::cout << book->get_price(side, level)<< std::endl;
        }
        else if(commands[0] == "get" && commands[1] == "size"){
            char side = commands[2].c_str()[0];
            int level = std::stoi(commands[3]);
            std::cout << book->get_size(side, level) << std::endl;
        }
    }

    delete book;
    return 0;
}

//split the input to be vectors which contains the operations
std::vector<std::string> split(const std::string &s, char delim){
    std::vector<std::string> elems;
    std::stringstream ss;
    ss.str(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}
