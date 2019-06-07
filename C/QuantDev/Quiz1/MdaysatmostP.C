#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
/*
Implement a program to nd out whether there exist M days within the last N(N >= M)
trading days that the average closing price of these M days is at most P. Assume we have
collected the history of the closing prices of the last N trading days for a stock. Requirements:
Inputs are positive integer M and N, M <= N; An array of N oat elements containing the
closing prices of the last N trading days; And a oat P. Please design and implement the
program in C, C++, Java or Python to produce the answer in most time/space efficient way.
*/

// Equals to the question that if the M smallest prices average is at most P, so we will find the smallest M elements.

int Left(int N, int i){
    if(2 * i <= N) return 2 * i;
    else return -1;
}

int Right(int N, int i){
    if(2 * i + 1 <= N) return 2 * i + 1;
    else return -1;
}


void Min_heapify(int N, float A[], int i){
    int l = Left(N, i);
    int r = Right(N, i);
    int minimum = 0;
    if(l < N && A[l] < A[i]){
        minimum = l;
    }
    else minimum = i;
    if(r < N && A[r] < A[minimum]){
        minimum = r;
    }
    if(minimum != i){
        A[i] = A[i] + A[minimum];
        A[minimum] = A[i] - A[minimum];
        A[i] = A[i] - A[minimum];
        Min_heapify(N, A, minimum);
    }
}

float Extract(int N, float A[]){
    float min = A[0];
    A[0] = A[N-1];
    Min_heapify(N, A, 0);
    return min;
}

bool atmostP(int N, int M, float price[], float P){
    float sum = 0;
    for(int i = N/2; i >= 0 ; i --){
        Min_heapify(N,price,i);
    }
    for(int i =  0; i < M ; i++){
        float min = Extract(N, price);
     //   std::cout << min << std::endl;
        sum += min;
    }
    if(sum > M * P) return false;
    else return true;
}



int main(int argc, char *argv[]){
    int M = atoi(argv[1]);
    float P= atof(argv[2]);
    float price[] = {15,40,32,61,10,22,4,31};
    int N = sizeof(price)/sizeof(float);
    if ( argc != 3 ) // argc should be 1 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" M P\n";
    else {
        if(atmostP(N, M, price, P))
            std::cout << "Exists" << std::endl;
        else
            std::cout << "Not Exists" << std::endl;
    }
}
