#include <iostream>
#include <fstream>

using namespace std;

void print_array(int A[], int size){
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

int* insert_sort(int A[], int size){
	for(int j = 1; j < size; j++){
		int key = A[j];
		int i = j - 1;
		while(i + 1 > 0 && A[i] > key){
			A[i + 1] = A[i];
			i = i - 1;
		}
		A[i + 1] = key;
	}
	return A;
}

int main(){
	int A[] = {5, 2, 4, 6, 1, 3};
	int size = sizeof(A)/sizeof(A[0]);
//	cout << size << endl;
	print_array(A, size);
	insert_sort(A, size);
	print_array(A, size);
}
