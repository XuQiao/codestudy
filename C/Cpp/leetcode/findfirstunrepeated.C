#include <iostream>
#include <map>
char first_non_repeated(const char* str, int len){
    std::map<char, int> m;
    for(int j = 0;j<len;j++){
        char s = str[j];
        if(m.find(s) != m.end()){
            m[s] = 1;
        }
        else{
            m[s] = 0;
        }
    }
    for(auto i=m.begin(); i!=m.end(); i++){
        if(i->second==0) return i->first;
    }
    return '@';
}

int main(){
    std::cout<<"first non repeated is: " << first_non_repeated("cbfbadfdfadc",12)<<std::endl;
}
