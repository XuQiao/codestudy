#include <iostream>
#include <vector>
using namespace std;

static const int size = 9;
class sudoko {
    private:
        vector< vector<int> > v;
        bool judge(int i, int j, int x);
    public:
    sudoko() {
       v.resize(size, vector<int> (size, 0));
    }
    void add(int i, int j, int x);
    void add(vector< vector<int> > iv);
    bool solve();
    void print();
};

bool sudoko::judge(int ii, int jj, int x){
    for(int i = 0;i < size; i++) {
        if ((ii != i) && (x == v[i][jj]) 
        || (jj != i) && (x == v[ii][i]))
        {
            return false;
        }
    }
    for(int i = ii/3*3;i < ii/3*3+3; i++) {
    for(int j = jj/3*3;j < jj/3*3+3; j++) {
        if((ii != i) && (jj != j) && (x == v[i][j])){
            return false;
        }
    }
    }
    return true;
}

bool sudoko::solve(){
    int flag = 1;
    for(int i = 0;i < size; i++) {
        for(int j = 0;j < size; j++) {
   //         cout << i << " " << j << " " << v[i][j] << endl;
            if (v[i][j] == 0){
                flag = 0;
                for(int num = 1; num <= size; num ++){
                    if (flag == 0 && judge(i, j, num)) {
                        v[i][j] = num;
                        if(solve()) {
                            return true;
                        }
                    }
                    v[i][j] = 0;    //backtrakcing
                }
                return false;
            }
        }
    }
    if (flag == 1) {
        return true; //success
    }
    return false;
}

void sudoko::add(int i, int j, int x) {
    if(i >= 0 && i < size && j >= 0 && j < size && x >= 0 && x <= size) {
        v[i][j] = x;
    }
}

void sudoko::add(vector< vector<int> > iv) {
    if(iv[0].size() == 3){
        for(int i = 0;i < iv.size(); i++ ) {
            this->add(iv[i][0], iv[i][1], iv[i][2]);
        }
    }
    if(iv[0].size() == 9){
        v = iv;
    }
}

void sudoko::print(){
    cout << "____________________" << endl;
    for(int i = 0;i < size; i++) {
        for(int j = 0;j < size; j++) {
        if(j % 3 == 0){
            cout << "|";
        }
        cout << v[i][j] << ' ';
        }
        if(i % 3 == 2){
            cout << endl << "____________________";
        }
        cout << endl;
    }
}

int main() {
    sudoko sud = sudoko();
    const int pair = 3;
    int matrix[9][9] = {
        
        {5, 0, 0, 0, 0, 0, 0, 4, 2},
        {0, 1, 0, 0, 0, 4, 0, 9, 5},
        {0, 6, 0, 8, 0, 0, 0, 7, 0},
        {0, 0, 6, 0, 0, 2, 0, 8, 0},
        {0, 0, 0, 7, 0, 1, 0, 0, 0},
        {0, 3, 0, 9, 0, 0, 2, 0, 0},
        {0, 4, 0, 0, 0, 8, 0, 2, 0},
        {7, 5, 0, 1, 0, 0, 0, 3, 0},
        {2, 9, 0, 0 ,0, 0, 0, 0, 8}
        /*
        {3, 0, 9, 0, 3, 1, 0, 4, 0},
        {0, 0, 1, 0, 8, 9, 0, 0, 0},
        {0, 5, 3, 0, 2, 0, 0, 0, 1},
        {9, 0, 5, 0, 0, 4, 6, 0, 0},
        {0, 0, 8, 0, 0, 0, 5, 0, 0},
        {0, 0, 7, 9, 0, 0, 4, 0, 2},
        {1, 0, 0, 0, 9, 0, 7, 5, 0},
        {0, 0, 0, 7, 4, 0, 1, 0, 0},
        {0, 8, 0, 2 ,1, 0, 3, 0, 0}
        */
    };
    vector< vector<int> > vectorinv;
    for(int i = 0;i < 9; i++){
        vector<int> vvalue(matrix[i], matrix[i]+size);
        vectorinv.push_back(vvalue);
    }
    sud.add(vectorinv);
    sud.print();
    bool success = sud.solve();
    if(success) {
        sud.print();
    }
    else {
        cout<<"fail!"<<endl;
    }
}
