#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
float findlargestpath(vector< vector<float> > value);
void print(vector< vector<float> > value);
int main() {
    int M = 5; //row
    int N = M; //column
    float matrix[][M] = {
        {1,2,3,4,5},
        {6,-1,2,3,0},
        {1,3,-2,4,3},
        {-1,2,5,4,1},
        {6,-3,2,2,4}
    };
    vector< vector<float> > value;
    for(int i = 0;i < M; i++){
        vector<float> vvalue(matrix[i], matrix[i]+M);
        value.push_back(vvalue);
    }
    
    // print(value);
    int L = findlargestpath(value);
    cout << L << endl;
    return 0;
}
/*
down
down
right
down
right
right
down
right
28
*/

float findlargestpath(vector< vector<float> > value) {
    int M = value.size();
    vector< vector<float> > maxvalue(M, std::vector<float> ( M, 0 ) );

    // dp
    maxvalue[0][0] = value[0][0];
    for(int i = 1;i < M; i++) {
        maxvalue[0][i] = maxvalue[0][i-1] + value[0][i];
        maxvalue[i][0] = maxvalue[i-1][0] + value[i][0];
    }
    for(int i = 1;i < M; i++) {
        for(int j = 1;j < M; j++) {
            maxvalue[i][j] = max(maxvalue[i][j-1], maxvalue[i-1][j]) + value[i][j];
           //maxvalue[i][j-1] + maxvalue[i-1][j];
           // cout << i << " " << j << " " << maxvalue[i][j] << endl;
        }
    }

    // get the path by subtracting
    int i = M - 1;
    int j = M - 1;
    std::stack<string> path; 
    while (i + j > 0) {
        if((maxvalue[i][j] - value[i][j]) == maxvalue[i][j-1]) {
            j = j - 1;
            path.push("right");
        }
        else {
            i = i - 1;
            path.push("down");
        }
    }
    while (path.size()) {
        string p = path.top();
        path.pop();
        cout << p << endl;
    }
    // print(maxvalue);

    return maxvalue[M-1][M-1];
}

void print(vector< vector<float> > value) {
    int M = value.size();
    for(int i = 0;i < M; i++) {
        for(int j = 0;j < M; j++) {
        cout << value[i][j] << '\t';
        }
        cout << endl;
    }
}
