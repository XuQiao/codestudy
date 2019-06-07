#include <iostream>

using namespace std;
class Solution{
public:
    int removeDuplicates(int A[], int n){
        if(n <= 2) return n;
        int index = 2;
        for(int i=2; i<n; i++){
            if(A[i]!=A[index-2])
                A[index++] = A[i];
        }

        return index;
    }

    int removeDuplicatesAlt1(int A[], int n){
        int index = 0;
        for(int i=0; i<n; ++i){
            if(i > 0 && i < n-1 && A[i] == A[i-1] && A[i] == A[i+1])
                continue;
            A[index++] = A[i];
        }
        return index;
    }
};

int main(){
    Solution s;
    int A[11]={1,2,2,2,3,3,4,5,6,6,6};
    int B[14]={1,1,1,2,2,3,3,3,3,4,5,6,6,6};
    int Alen = s.removeDuplicates(A,11);
    int Blen = s.removeDuplicatesAlt1(B,14);
    cout<<Alen<<endl;
    cout<<Blen<<endl;
    for(int i=0;i<Alen;i++){
        cout<<A[i]<<",";
    }
    cout<<endl;
    for(int i=0;i<Blen;i++){
        cout<<B[i]<<",";
    }
    return 0;
}

