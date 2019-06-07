#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include "StockData.h"

std::vector<stock_data> get_from_file(std::string filename, std::string exchangename); //declaration
std::vector<stock_data> shiftandinterpolate(std::vector<stock_data> A, std::vector<stock_data> B, float lag); //shift the time series by time lag t, -200 < t < 200
double cross_corr(std::vector<stock_data> A, std::vector<stock_data> B);
double MLE(std::vector<stock_data> A, std::vector<stock_data> B);

/*
 *  first we acquire our input from the txt file produce from the GeneratSample.py output
 *  Shift one of the time series by some lag and compute the cross correlation with another one
 *  The parameter which can maximize the corrlation length r is adopted
 */

int main(int argc, char *argv[]){
    std::string filename = argv[1];
    if ( argc != 2 ) // argc should be 2 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" <filename>\n";
    else {
        //read in input
        std::vector<stock_data> stockA = get_from_file(argv[1],"A");
        std::vector<stock_data> stockB = get_from_file(argv[1],"B");
        
        //for a grid of lags from -100 ms to 100ms, we loop to see how our delayed A cross correlates with B, and select the maximum correlation from the results the print out the best estimated lag
        double max_crosscorr = 0;
        double true_lag_cross = 0;
        double min_ls = 0;
        double true_lag_mle = 0;
        std::ofstream fout_cross("laggedcorrelation"+filename);
        std::ofstream fout_mle("laggedmle"+filename);
        for(float lag = -100; lag < 100; lag += 1){
            std::vector<stock_data> stockAint = shiftandinterpolate(stockA, stockB, lag);
            //std::vector<stock_data> stockBint = shiftandinterpolate(stockB, stockA, lag);
            double crosscorr = cross_corr(stockAint, stockB);
            double ls = MLE(stockAint, stockB);
            if(max_crosscorr <= crosscorr){
                max_crosscorr = crosscorr;      //finding the maximum
                true_lag_cross = lag;
            }
            if(min_ls >= ls || min_ls == 0){
                min_ls = ls;      //finding the minimum
                true_lag_mle = lag;
            }
            fout_cross << lag << " " << crosscorr <<std::endl;
            fout_mle << lag << " " << ls <<std::endl;
        }
            std::cout << "B is lagged by " << true_lag_cross << "ms using cross correlation" << std::endl;
            std::cout << "B is lagged by " << true_lag_mle << "ms using least square" << std::endl;
            std::cout << "B is Actually lagged by " << 30 << "ms" << std::endl;
    }
    return 0;
}

//iostream, readin from file and store into the stock data format
std::vector<stock_data> get_from_file(std::string filename, std::string exchangename){ //read into a vector
    std::vector<stock_data> stock_stream={};
    std::ifstream input( filename );
    if(input.is_open()){
        std::string line;
        getline( input, line); //skip first line
        for( line; getline( input, line ); ){
            stock_data tick_data(line);
            if(tick_data.get_exchange() == exchangename)
                stock_stream.push_back(tick_data);
        }
    }
    else
        std::cout << "Could not open "<< filename << std::endl;
    input.close();
    return stock_stream;
}

std::vector<stock_data> shiftandinterpolate(std::vector<stock_data> A, std::vector<stock_data> B, float lag){ //shift the time series by time lag t, -200 ms< t < 200 ms, 1 hour = 60 min = 60 * 60 s = 1e6 * 60 * 60 ms

    //shift time series A by lag t
    std::vector<stock_data> Ashift;
    for(std::vector<stock_data>::iterator iter = A.begin(); iter != A.end(); iter++){
    double time = (*iter).get_time();
    double price = (*iter).get_price();
    double time_lag = time + lag / 60 / 60 / 1e6;
    stock_data temp(time_lag, price,"A");
    Ashift.push_back(temp);
    }
    
    //Interpolate on time series A, applying B
    std::vector<stock_data> Aint;
    std::vector<stock_data>::iterator iter_start = Ashift.begin();
    for(std::vector<stock_data>::iterator iter_B = B.begin(); iter_B != B.end(); iter_B++){
    double time_B = (*iter_B).get_time();
    if(time_B < Ashift[0].get_time() || time_B > Ashift[Ashift.size()-1].get_time()){
        double price_int = (*iter_B).get_price();
        stock_data temp(time_B, price_int,"A");
        Aint.push_back(temp);
    }
    for(std::vector<stock_data>::iterator iter_A = iter_start + 1; (iter_A+1) != Ashift.end(); iter_A++){
    double time_A = (*iter_A).get_time();
    double time_A_next = (*(iter_A+1)).get_time();
  //  std::cout << time_A << " "<< time_A_next << std::endl;
  //  std::cout<< time_B << " "<< time_A << " " << time_A_next << std::endl;a
    if(time_B >= time_A && time_B < time_A_next){   //find the time interval where B locates at A
    double price = (*iter_A).get_price();
    double price_next = (*(iter_A+1)).get_price();
  // Two point interpolations
    double price_int = ((price_next - price) * time_B + (price * time_A_next - price_next * time_A)) / (time_A_next - time_A);
    stock_data temp(time_B, price_int,"A");
    Aint.push_back(temp);
    iter_start = iter_A - 2;
    break;
    }
    }
    }
    return Aint;
}

double MLE(std::vector<stock_data> A, std::vector<stock_data> B){
   std::vector<stock_data>::iterator iter_A = A.begin(); 
   double sumLS = 0;
   for(std::vector<stock_data>::iterator iter_B = B.begin(); iter_B != B.end(); iter_B++){
        double price_B = (*iter_B).get_price();
        double price_A = (*iter_A).get_price();
        double diff2 = (price_B - price_A) * (price_B - price_A);
        sumLS += diff2;
        iter_A ++;
   }
   return sumLS;
}

//calculate the 
double cross_corr(std::vector<stock_data> A, std::vector<stock_data> B){
   // std::cout<< A.size() << " " << B.size() << std::endl;
    double meanA = 0;
    double meanB = 0;
    for(std::vector<stock_data>::iterator iter = A.begin(); iter != A.end(); iter++){
        meanA += (*iter).get_price();
    }
    if(A.size())
        meanA /= A.size();
    for(std::vector<stock_data>::iterator iter = B.begin(); iter != B.end(); iter++){
        meanB += (*iter).get_price();
    }
    if(B.size())
        meanB /= B.size();
   double sigmaA = 0;
   double sigmaB = 0;
    for(std::vector<stock_data>::iterator iter = A.begin(); iter != A.end(); iter++)
      sigmaA += ((*iter).get_price() - meanA) * ((*iter).get_price() - meanA);
    for(std::vector<stock_data>::iterator iter = B.begin(); iter != B.end(); iter++)
      sigmaB += ((*iter).get_price() - meanB) * ((*iter).get_price() - meanB);
   double denom = sqrt(sigmaA*sigmaB);

   //cross product
   double crosssum = 0;
   std::vector<stock_data>::iterator iter_A = A.begin(); 
   for(std::vector<stock_data>::iterator iter_B = B.begin(); iter_B != B.end(); iter_B++){
        double price_B = (*iter_B).get_price();
        double price_A = (*iter_A).get_price();
        crosssum += (price_A - meanA) * (price_B - meanB);

        iter_A++;
    }
    //crosssum /= B.size();
    //std::cout<<std::setprecision(10)<<crosssum <<" "<< meanA* meanB<<std::endl;
    if(denom)
    return crosssum / denom;
}
