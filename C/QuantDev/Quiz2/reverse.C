#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>
#include <sstream>

std::string reverse(std::string sentence){
//std::string sentence = "Your sentence which contains ten words, two of them numbers";
std::stringstream stream(sentence);
std::vector<std::string> words;
std::string w = "";
for ( std::string word; stream >> word; )
{
    words.push_back(word);
}
for(int i=words.size()-1;i>=0;i--){
    w += words[i]+" ";
}
return w;
}

int main(int argc, char *argv[]){
    std::string x = argv[1];
    if ( argc != 2 ) // argc should be 2 for correct execution
    // We print argv[0] assuming it is the program name
        std::cout<<"usage: "<< argv[0] <<" string\n";
    else {
        std::cout <<  "\"" << x << "\" " << " -> \"" << reverse(x) << "\"" << std::endl;
    }
}
