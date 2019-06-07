#include <iostream>
#include <fstream>

using namespace std;

int backpack(int A[], int n, int N){
    int m = 0;
    int *B;
    if(N == 0){
        B = 0;
        return 0;
    }
    for(int i = 0; i <= N ; i++){
        for(int j = 0; j < n ; j++){
            if(A[j] <= i){
                m = backpack(A, n, i - A[j]);
                cout << " i = " << i << ", j = " << j << ", m = " << m << endl;
                if((m + 1) >= backpack(A, n, i - 1)){  //found a better solution
                    m = backpack(A, n, i - 1) + 1;
                }
            }
        }
    }
    return m;
}

int main(){
    int A[] = {1, 2, 5, 10};
	int n = sizeof(A)/sizeof(A[0]); 
    int N = 9;
	cout << backpack(A, n, N) << endl;
    return 0;
}
