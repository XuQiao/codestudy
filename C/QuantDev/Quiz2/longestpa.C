#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>
using namespace std;
//"eaaade"

int longest(string x, int n, int m){
    if( n == m ) return 1;
    else if(n + 1 == m && x[n] == x[m]) return 2;
    else if(x[n] == x[m]) return longest(x, n+1 , m-1) + 2;
    else return max( longest(x, n, m-1), longest(x, n+1, m) );
}

int longest1(string x){
   int n = x.length();
   int i, j, cl;
   int L[n][n]; 
   for (i = 0; i < n; i++)
      L[i][i] = 1;
 
   for (cl=2; cl<=n; cl++){
      for (i=0; i<n-cl+1; i++){
            j = i+cl-1;
            if (x[i] == x[j] && cl == 2)
               L[i][j] = 2;
            else if (x[i] == x[j])
               L[i][j] = L[i+1][j-1] + 2;
            else
               L[i][j] = max(L[i][j-1], L[i+1][j]);
        }
    }
    return L[0][n-1];
}

bool ispa(string x){
    int length = x.length();
    if(length <= 1) return true;
    for(int i = 0;i < length;i ++){
        int j = length - i - 1;
        if(x[i] != x[j]){
            return false;
        }
    }
    return true;
}

string longestpa(string x){
    int length = x.length();
    if(length == 1) return x;
    int l = longest(x, 0, length - 1);
cout<<l<<endl;
    int l1 = longest1(x);
cout<<l1<<endl;
    for(int i = 0; i < length;i ++){
        string tmp;
        tmp.assign(x,i,l);
        if(ispa(tmp)) return tmp;
    }
    return  string(1,x[0]);
}

int main(int argc, char *argv[]){
    string x = argv[1];
    int length = x.length();
    if ( argc != 2 ) // argc should be 1 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" N\n";
    else {
        std::cout << "longest palindrome(" << x << ") = " << longestpa(x) << std::endl;
        std::cout << "is palindrome(" << x << ") = " << ispa(x) << std::endl;
    }
}
