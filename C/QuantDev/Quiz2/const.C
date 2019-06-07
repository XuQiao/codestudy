#include <iostream>
using namespace std;
//const &p: reference to a const pointer to a const int:
//const int* const fun: the function returns a const pointer to const int
//function doesn' change input

const int* const fun(const int* const&p) const{
    const int *pt;
    pt = p + 1;
    return pt;
}

int main(){
    const int a = 1;
    const int* const &p = &a;
    cout << *fun(p) << endl;
}
