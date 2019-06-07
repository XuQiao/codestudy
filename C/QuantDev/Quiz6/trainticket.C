#include <iostream>
#include <vector>

int solution(std::vector<int> &A){ 
    int N = A.size();
    std::vector<int> price;
    int reduce = 0;
    for(int i=0; i < N;i++){
        int add1 = 2;//all one day ticket
        int reduce = 0;
        for(int j = 0; j < 7; j ++){
            if(i>j && A[i-j-1]> A[i]-7)
                reduce++;
        }
        int add2 = 7 - reduce*2; //7 day ticket
        if(add2 < 0){
            add2 = 0;
        }

        reduce = 0;
        for(int j = 0; j < 30; j ++){
            if(i>j && A[i-j-1]> A[i]-30)
                reduce++;
        }
        int add3 = 25 - reduce*2; //30 day ticket
        if(add3 < 0){ 
            add3 = 0;
        }

        if(i==0){
            price.push_back(add1);
        }
        else{
            price.push_back(price[i-1]+std::min(std::min(add1,add2),add3));
        }
    }
    return price[N-1];
}


int main(int argc, char *argv[]){
    int A[] = {1, 3, 4, 5, 6, 8, 9};
    int N = sizeof(A) / sizeof(int);
    std::vector<int> vecA(A, A+N);
    for(int i=0; i < N;i++){
        std::cout<<A[i]<<" ";
    }
    std::cout<<std::endl;
    std::cout << "minimum valid price is " << solution(vecA) << std::endl;
}
