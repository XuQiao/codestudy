#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */

bool ispowerof2(int N){
    return N > 0 && ((N & (N - 1)) == 0);
//    return N/2 == N/2.;
}

int main(int argc, char *argv[]){
    int N = atoi(argv[1]);
    if ( argc != 2 ) // argc should be 1 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" N\n";
    else {
        if(ispowerof2(N))
            std::cout << N << " is power of 2" << std::endl;
        else
            std::cout << N << " is not power of 2" << std::endl;
    }
    return 0;
}
