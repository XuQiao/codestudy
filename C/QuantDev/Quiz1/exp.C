#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>

double exp(double x){
    double eps = 1e-10;
    double term = 1;
    double sum = term;
    for(int i = 1; fabs(term) > eps; i++){
        term = term * x / i;
        sum += term;
    }
    return sum;
}

int main(int argc, char *argv[]){
    double x = atof(argv[1]);
    if ( argc != 2 ) // argc should be 1 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" N\n";
    else {
        std::cout << "exp(" << x << ") = " << exp(x) << std::endl;
    }
}
