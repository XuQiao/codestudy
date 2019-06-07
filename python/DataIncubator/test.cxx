#include <iostream>
#include <math.h>
using namespace std;
int main(){
    double l = 0;
    for(long i = 1; i<1e15;i++){
        if(i % int(1e8) ==0 )
        cout << i << endl;
        l += log(i);
    }
    cout << l << endl;
}


