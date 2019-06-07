#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <vector>

/*
 matrix class
 */
using namespace std;
class matrix{
    public:
        matrix(size_t n);
        matrix(size_t m, size_t n);

        ~matrix();
        const matrix add(const matrix &m);
        const matrix multiply(const matrix &n);
        print();
    private:
        vector<vector <float>> mData = 0;
        size_t mRows;
        size_t mCols;
};

matrix::matrix(size_t n){
    mRows = n;
    mCols = n;
    mData.resize(n * n);
    for(int i = 0;i < n; i ++){
        mData[i][i] = 1;
    }
}

const matrix matrix:add(const matrix &m){
    if(mRows != m.Rows || mCols != m.Cols)
        try 
    const matrix r;
    r(
}

matrix::print(){
    for(int i = 0;i < mRows; i++){
        for(int j = 0;j < mCols; j++){
            cout << mData[i][j] << " ";
        }
        cout << endl;
    }
}

int main(int argc, char *argv[]){
}
