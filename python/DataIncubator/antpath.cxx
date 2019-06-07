#include <iostream>
#include <vector>
#include <math.h>       /* fabs */
#include <iomanip>      // std::setprecision

using namespace std;

struct pathinfo{
public:
    int m;
    int n;
    vector< vector<long>> a; //how many paths for each D, D ranges from [0, 1], and has m*n dintinct values
    pathinfo(int _m, int _n) {
        m = _m;
        n = _n;
        a = vector<vector<long>>(m+1, vector<long>(n+1, 0));
        for (int ii = 0; ii <= m; ii ++) { 
            for (int jj = 0; jj <= n; jj ++) { 
                a[ii][jj] = 0;
            }
        }
    }
};


class antpath{
    int m;
    int n;
public:
    vector<vector <pathinfo>> paths;
    vector<vector <double>> distances;
    antpath(int _m, int _n){
        m = _m;
        n = _n;
        paths = vector<vector<pathinfo>>(m+1, vector<pathinfo>(n+1, pathinfo(m, n)));
        distances = vector<vector<double>>(m+1, vector<double>(n+1, 0));
    }

    vector<vector<pathinfo>> fillallDs() {
        //dp using a conjunction matrix per node
        for (int i = 0; i <= m; i ++){
            pathinfo path = pathinfo(m, n);
            path.a[i][0] += 1;
            paths[i][0] = path;
            distances[i][0] = i * 1. /m;
        }
        for (int j = 0; j <= n; j ++) {
            pathinfo path = pathinfo(m, n);
            path.a[0][j] += 1;
            paths[0][j] = path;
            distances[0][j] = j * 1. /n;
        }
        for (int i = 1; i <= m; i ++) { 
            for (int j = 1; j <= n; j ++) { 
                double D = fabs(i * 1./m - j * 1./n);
                distances[i][j] = D;
                for (int ii = 0; ii <= m; ii ++) { 
                    for (int jj = 0; jj <= n; jj ++) { 
                        paths[i][j].a[ii][jj] = paths[i-1][j].a[ii][jj] + paths[i][j-1].a[ii][jj];
                    }
                }
                for (int ii = 0; ii <= m; ii ++) { 
                    for (int jj = 0; jj <= n; jj ++) { 
                        double D0 = fabs(ii * 1./m - jj * 1./n);
                        if (D > D0) {
                            paths[i][j].a[i][j] += paths[i][j].a[ii][jj];
                            paths[i][j].a[ii][jj] = 0;
                        }
                    }
                }
            }
        }
        return paths;
    }
    void printout(vector<vector <long>> a){
        for (int ii = 0; ii <= m; ii ++) { 
        cout<<"\t";
            for (int jj = 0; jj <= n; jj ++) { 
                cout << a[ii][jj] << "\t";
            }
                cout << endl;
        }
    }
    vector<double> findallDs(int curr_m, int curr_n) {
        vector<double> Ds;
        // directly calculate D without calculating paths, recursively, time consuming
        if (curr_m == 0)
            Ds.push_back(0); // corner case
        else if (curr_n == 0)
            Ds.push_back(0); // corner case
        else {
            for ( auto const &currD: findallDs(curr_m-1, curr_n) ) {
                Ds.push_back(max(currD, fabs((curr_m-1)*1./m-curr_n*1./n)));
            }
            for ( auto const &currD: findallDs(curr_m, curr_n-1) ) {
                Ds.push_back(max(currD, fabs(curr_m*1./m-(curr_n-1)*1./n)));
            }
        }
        return Ds;
    }

public:
    vector<double> getDs() {
        return findallDs(m, n);
    }
};

int main() {
    int m = 23;
    int n = 31;
    antpath Ant = antpath(m, n);
    vector< vector<pathinfo>> Ds = Ant.fillallDs();
    double sumD = 0;
    double sumD2 = 0;
    double sumDcond1 = 0;
    double sumDcond2 = 0;
    double npath = 0;
    for (int ii = 0; ii <= m; ii ++) { 
        for (int jj = 0; jj <= n; jj ++) {
            long path = Ds[m][n].a[ii][jj];
            double distance = Ant.distances[ii][jj];
            sumD += path * distance;
            sumD2 += path * distance * distance;
            sumDcond1 += path * (distance > 0.2?1:0);
            sumDcond2 += path * (distance > 0.6?1:0);
            npath += path;
        }
    }
    /*
    double npath = Ds.size();
    for (auto const &D : Ds) {
        sumD += D;
        sumD2 += D*D;
        if ( D > 0.2)
            sumDcond1 += 1;
        if ( D > 0.6)
            sumDcond2 += 1;
    }
    */
    
/*
    double sumD = Ant.sumD;
    double npath = Ant.npath;
    double sumD2 = Ant.sumD2;
    double sumDcond1 = Ant.sumDcond1;
    double sumDcond2 = Ant.sumDcond2;
*/
    cout << setprecision(11);
    cout << sumD / npath << endl;
    cout << sqrt((sumD2-sumD*sumD/npath) / npath) << endl;
    cout << sumDcond2 / sumDcond1 << endl;
    return 0;
}
