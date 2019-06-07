#include <iostream>
using namespace std;
class A {
public:
    int val;
    A(){ val = 0;}
	A(int n){ val = n; }
	A& GetObj(){
 //       A& obj = *this;
         cout<<"a this = "<<this<<endl;
		return *this;
	}
};
main()  {
    A a;
    cout << a.val << endl;
   // a.GetObj() = 5;
    a.GetObj() = 5;
    A b = a.GetObj();
    A c = a.GetObj();
    A d = a.GetObj();
    cout<<&a<<endl; 
    cout<<&b<<endl; 
    cout<<&c<<endl; 
    cout<<&d<<endl; 
    cout << a.val << endl;
}
