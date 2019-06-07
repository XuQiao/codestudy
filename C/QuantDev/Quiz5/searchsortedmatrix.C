#include <iostream>
#include <vector>
using namespace std;
int search(vector< vector<int> > value, int goal);
int main() {
    int M = 4; //row
    int N = M; //column
    int matrix[][M] = { {10, 20, 30, 40},
                    {15, 25, 35, 45},
                    {27, 29, 37, 48},
                    {32, 33, 39, 50},
    };
    vector< vector<int> > value;
    for(int i = 0;i < M; i++){
        vector<int> vvalue(matrix[i], matrix[i]+M);
        value.push_back(vvalue);
    }
    
    int L = search(value, 100);
    if(L < 0){
        cout<< "not find" << endl;
    }
    else{
        cout << "row " << L/M << endl;
        cout << "column " << L - L/M * M<< endl;
    }
    return 0;
}

int search(vector< vector<int> > value, int goal) {
    int M = value.size();
    int N = value[0].size();
    int i = 0, j = N - 1;
    while(i < M && j >= 0){
        if(value[i][j] == goal) {
            return i * N + j;
        }
        if(value[i][j] > goal) {
            j --;
        }
        else {
            i ++;
        }
    }

    return -1;
}
