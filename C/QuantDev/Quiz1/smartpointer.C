#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include "Sample.h"
#include <memory>

/*
 A smart pointer is a class that wraps a 'raw' (or 'bare') C++ pointer, to manage the lifetime of the object being pointed to. There is no single smart pointer type, but all of them try to abstract a raw pointer in a practical way.

Smart pointers should be preferred over raw pointers. If you feel you need to use pointers (first consider if you really do), you would normally want to use a smart pointer as this can alleviate many of the problems with raw pointers, mainly forgetting to delete the object and leaking memory.

With raw pointers, the programmer has to explicitly destroy the object when it is no longer useful.
 */
template <typename T>
class smartp{
    public:
        smartp(T* p);
        ~smartp();
        T& operator*();
        T* operator->();
    private:
        T* ptr;
};

template <typename T>
smartp<T>::smartp(T* p):ptr(p){}

template <typename T>
T& smartp<T>::operator*(){
    return *ptr;
}

template <typename T>
T* smartp<T>::operator->(){
    return ptr;
}

template <typename T>
smartp<T>::~smartp<T>(){
    delete ptr;
}



int main(int argc, char *argv[]){
//    Sample *p = new Sample(1);
//    p->print();
//    delete p;  //has to delete by hand
        
//    std::auto_ptr<Sample> p(new Sample(3));  //C++ auto_ptr
//    p->print();
    smartp<Sample> p(new Sample(2));
    (*p).print();
    p->print();
}
