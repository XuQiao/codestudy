#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>

int indexof(std::string x, std::string sub){
    int pos = -1;
    if(x.size() < sub.size()) return -1;
    for(std::string::iterator it = x.begin(); it != x.end(); it ++){
        std::string::iterator ittemp = it;
        std::string::iterator jt = sub.begin();
        for(; jt != sub.end(); jt++){
            if(*ittemp != *jt) break;
            ittemp ++;
        }
        pos ++;
        if(jt == sub.end()) return pos;
    }
    return -1;
}

int main(int argc, char *argv[]){
    std::string x = argv[1];
    std::string sub = argv[2];
    if ( argc != 3 ) // argc should be 2 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" string, substring\n";
    else {
        int pos = indexof(x, sub);
        if(pos < 0)
            std::cout << "No \"" << sub << "\" in \"" << x << "\"" << std::endl;
        else
            std::cout <<  "\"" << sub << "\" pos " << pos << " in \"" << x << "\"" << std::endl;
    }
}
