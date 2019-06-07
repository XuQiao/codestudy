#include <TGraph.h>
#include "fstream"
#include "iostream"
void plotgvsr(){

ifstream fstr("gvsr.txt");
vector <double> gvec;
vector <double> rvec;
double n;

while(!fstr.eof()){
	fstr>>n;
    gvec.push_back(n);
	fstr>>n;
    rvec.push_back(n);
}
if(gvec.size()==rvec.size()){
const int N=gvec.size();
double g[N],r[N];
//cout<<N<<endl;
for(int i=0;i<N;i++){
g[i]=gvec[i];//cout<<g[i]<<'\t';
r[i]=rvec[i];//cout<<r[i]<<endl;
}
TGraph *gr=new TGraph(N,g,r);
gr->GetXaxis()->SetTitle("X Title");
gr->GetYaxis()->SetTitle("Y Title");
gr->SetTitle("Title");
gr->SetMarkerSize(1);
gr->SetMarkerColor(1);
gr->SetMarkerStyle(20);
gr->Draw("AP");
c1->Print("gvsr.png");
}
fstr.close();

}

