#include <iostream>

using namespace std;

int main(){
//only one variable is allowed
//A: d10 - f8, B: d1 - f3

    cout << "A\t" << "B" << endl; 
    for(int pos = 0; pos < 81; pos ++) {
        if (pos / 3 / 3 / 3 % 3== pos / 3 % 3) continue;
        cout << char(pos / 3 / 3 / 3 % 3 + 'd')  << pos / 3 / 3 % 3 + 8 << "\t" <<  
                char(pos / 3 % 3 + 'd')  << pos % 3 + 1 << endl; 
    }
}
