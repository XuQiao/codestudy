#include <iostream>
#include <fstream>

using namespace std;

void print_array(bool A[], int size){
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

bool Xor(bool a, bool b){
	if(a == b) return 0;
	else return 1;
}

bool XorP(bool a, bool b){
	if(a == 1 && b == 1) return 1;
	else return 0;
}

int convert(bool A[], int n){
	int sum = 0;
	for(int j = 0; j < n; j++){
		int i = j;
		int power = 1;
		while(i > 0){
			power = power * 2;
			i = i - 1; 
		}
		sum = sum + A[n - j - 1] * power;
	}
	return sum;
}

bool* add(bool *a, bool *b, int n){
	bool *C = new bool(n+1);
	bool key = 0;
	for(int j = 0; j < n; j++){
		C[j] = Xor(key, Xor(a[j], b[j]));
		key = Xor(key, XorP(a[j], b[j]));
	}
	C[n] = key;
	return C;
}


int main(){
	bool A[] = {0, 1, 1, 0, 1};
	bool B[] = {1, 1, 0, 0, 1};
	int n = sizeof(A)/sizeof(A[0]); 
	print_array(A, n);
	cout << convert(A, n) << endl;
	print_array(B, n);
	cout << convert(B, n) << endl;
	bool *C = add(A, B, n);
	print_array(C, n + 1);
	cout << convert(C, n + 1) << endl;
}
