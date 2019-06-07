void heart(){
    TRandom3 *r;
    r = new TRandom3(0);
    double x[100000],y[100000];
    int ievent = 100000;
    for(int i=0;i<ievent;i++){
    double r1 = 100*r->Rndm();
    x[i] = sin(r1);
    y[i] = TMath::Power(x[i]*x[i],1./3)  + cos(r1);
    }
    TGraph *g = new TGraph(ievent,x,y);
    g->SetFillColor(2);
    g->SetMarkerColor(2);
    g->Draw("AP"); 
}


