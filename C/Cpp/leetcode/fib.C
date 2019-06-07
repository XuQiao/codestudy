#include <iostream>
#include <vector>
#include <cassert>
double fib1(int n){ //first method
    if(n<=0) return 0;
    if(n==1) return 1;
    return fib1(n-1) + fib1(n-2);
}

double fib2(int n){ //record table
    if(n<=0) return 0;
    std::vector<double> table;
    table.push_back(0);
    table.push_back(1);
    for(double i=2;i<=n;i++){
        table.push_back(table[i-1]+table[i-2]);
    }
    return table[n];
}

std::vector<double> matrixmulti(std::vector<double> a, std::vector<double> b){
    std::vector<double> c={};
    assert(a.size()== 4 && b.size() == 4);
    c.push_back(a[0]*b[0]+a[1]*b[2]);
    c.push_back(a[0]*b[1]+a[1]*b[3]);
    c.push_back(a[2]*b[0]+a[3]*b[2]);
    c.push_back(a[2]*b[1]+a[3]*b[3]);
    return c;
}

std::vector<double> power1(std::vector<double> a, int n){
    std::vector<double> N = {1, 1 ,1, 0};
    for(double i = 1;i < n;i++){
        a = matrixmulti(a, N);
    }
    return a;
}
std::vector<double> power2(std::vector<double> a, int n){
    if(n==1)  return a;
    std::vector<double> N = {1, 1, 1, 0};
    a = power2(N, n/2);
    a = matrixmulti(a, a);
    if(n % 2 !=0 ) a = matrixmulti(a, N); 
    return a;
}

double fib3(int n){ //matrix
   std::vector<double> N = {1, 0 ,1, 0};
//   return power1(N, n)[0];
   return power2(N, n-1)[0];
}


int main(int argc, char** argv){
    int n = atoi(argv[1]);
//    std::cout<<"fib1 = " << fib1(n) <<std::endl;
    std::cout<<"fib2 = " << fib2(n) <<std::endl;
    std::cout<<"fib3 = " << fib3(n) <<std::endl;
}

