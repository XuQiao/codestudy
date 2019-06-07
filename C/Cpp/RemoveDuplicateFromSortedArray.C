#include <iostream>
#include <algorithm>
using namespace std;
class Solution{
    public:
    int remove(int A[], int n){
       /*
        if(n==0) return 0;
        
        int index = 0;
        for(int i = 1;i < n;i++){
            if(A[index] != A[i])
                A[++index] = A[i];
        }
        return index+1;
        */ //code 1
        // return distance(A, unique(A, A+n)); //code 2
        return remove(A, A+n, A) - A;   //code 3
    }
    
    template<typename InIt, typename OutIt>
    OutIt remove(InIt first, InIt last, OutIt output){
        while(first != last){
            *output++ = *first;
            first = upper_bound(first, last, *first);
        }
        return output;
    } 
     //code 3
};

int main(){
    Solution s;
    const int l = 10;
    int A[l] = {0,1,2,2,3,5,5,6,7,8};
    //int A[l] = {};
    cout<<"A["<<l<<"] = "<<"{";
    for(int i=0;i<l;i++){
        if(i!=l-1)
            cout<<A[i]<<",";
        else
            cout<<A[i];
    }
    cout<<"}"<<endl;
    int length = s.remove(A, l);
    cout<<length<<endl;
    cout<<"A["<<length<<"] = "<<"{";
    for(int i=0;i<length;i++){
        if(i!=length-1)
            cout<<A[i]<<",";
        else
            cout<<A[i];
    }
    cout<<"}"<<endl;
}
