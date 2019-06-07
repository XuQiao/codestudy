#include <iostream>

class Sample{
    public:
        Sample(int);
        void print();
        ~Sample();
    private:
        int number;
};

Sample::Sample(int number):number(number){}

void Sample::print(){
    std::cout << number << std::endl;
}

Sample::~Sample(){
    std::cout << "Delete and exit" << std::endl;
}

