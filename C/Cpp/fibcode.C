#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

int largestfib(vector<int> &fib, int n, bool fill){
    if(fill){
        fib.push_back(1);
        fib.push_back(2);
    }
    if(n == 1 || n == 2){
        return n - 1;
    }
    int i = 1;
    while(fib[i] <= n){
        if(fill){
            fib.push_back(fib[i - 1] + fib[i]);
        }
        i = i + 1;
    }
    i = i - 1;
    return i;
}

vector<int> getfibcode(int n){
    int remainder = n;
    vector<int> fib;
    int i = 0;
    int k = largestfib(fib, n, 1);
    vector<int> results(k + 1, 0);
    while ( remainder > 0) {
        i = largestfib(fib, remainder, 0);
        results[i] = 1;
        remainder = remainder - fib[i];
    }   
    return results;
}

int main(int argc, char** argv){
    int n = atoi(argv[1]);
    vector<int> results = getfibcode(n);
    for(int i = 0;i<results.size() ; i++){
        cout << results[i] << "\t";
    }
    cout<<endl;
}
