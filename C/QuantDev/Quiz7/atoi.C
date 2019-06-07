#include <iostream>
#include <string>

int atoi(std::string s){
    int i = 0;
    int result = 0;
    int flag = 1;
    while(s[i]){
        char c = s[i];
        if(c == '-'){
            i++;
            flag = -1;
            continue;
        }
        int m = c - '0';
        if(m >= 0 && m <= 9){
            result = result * 10 + m;
        }
        else {
            throw(std::runtime_error("NOT VALID!"));
        }
        i++;
    }
    return result * flag;
}


int main(int argc, char *argv[]){
    if(argc > 2) {
        throw  "ONLY ONE STRING A TIME";
    }
    std::string s = argv[1];
    std::cout << s << std::endl;
    std::cout << "atoi(" << s << ") + 1 = " << atoi(s) + 1 << std::endl;
}
