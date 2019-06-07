#include <iostream>
#include <algorithm>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

void print_array(int *A, int size){
	cout << "A = {" ;
	for(int i = 0; i < size; i++){
		if(i < size - 1){
			cout << A[i] << ", ";
		}	
		else{
			cout << A[i] << "}" << endl;
		}
	}
}

int myrandom(int i) {return rand() % i;}

// how to sort n pies, if we can reverse the order of first k pies
int *gen_random(int n){
    int *A = new int(n);
    for(int i = 0; i < n; i++){
        A[i] = i;
        cout << A[i] << endl;
    }

    /* initialize random seed: */
    srand (time(NULL));

    random_shuffle (A, A + n);
    return A;
}

void reverse_firstk(int *A, int k, int n){
    cout << "reverse first " << k << " pies " << endl;
    int temp;
    if(k > n) { cout << "k is too large!" << endl;}
    for(int i = 0; i < k/2; i++){
        temp = A[i];
        A[i] = A[k - i - 1];
        A[k - i - 1] = temp;
    }
    print_array(A, n);
}

int find_max_index(int *A, int n){
    int max_index = 0;
    for(int i = 1; i < n; i++){
        if(A[i] > A[max_index]) 
            max_index = i;
    }
    return max_index;
}


void solve(int *A, int n){
    if(n == 2){
        if(A[0] > A[1]) 
          reverse_firstk(A, 2, n);
    }
    else if(n > 2){
        if(find_max_index(A, n) != n - 1){
        reverse_firstk(A, find_max_index(A, n) + 1, n);
        reverse_firstk(A, n, n);
        }
        solve(A, n - 1);
    }
    else { cout << "wrong number!" << endl;}
}

int main(){
    int n = 20;
    int *A = gen_random(n);
    print_array(A, n);
    solve(A, n);
}
