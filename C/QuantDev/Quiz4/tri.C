#include <iostream>
#include <cmath>
struct point{
    float x;
    float y;
    point(float _x, float _y){
        x = _x;
        y = _y;
    }
}; //point struct

bool sameside(point A, point B, point X, point Y) {
    //line (x2-x1)y - (y2-y1)x -(y1x2-y2x1) = 0)
    float sX = (B.x-A.x) * X.y  - (B.y-A.y) * X.x - (A.y*B.x - B.y*A.x);
    float sY = (B.x-A.x) * Y.y  - (B.y-A.y) * Y.x - (A.y*B.x - B.y*A.x);
    if(sX * sY > 0) {
        return 1;
    }
    else {
        return 0;
    }
} //check if X,Y are on the same side of A, B line

float length(point A, point B){
    return sqrt((B.x-A.x)*(B.x-A.x) + (B.y-A.y)*(B.y-A.y));
} //length of AB

float area(point A, point B, point C){
    float a = length(A,B);
    float b = length(B,C);
    float c = length(A,C);
    float p = (a + b + c)/2;
    return sqrt(p*(p-a)*(p-b)*(p-c));
} //area of triangle ABC

int checkpoint1(point A, point B, point C, point X){
    if(sameside(A, B, C, X) && sameside(A, C, B, X) && sameside(B, C, A, X)){
        return 1;
    }
    else {
        return 0;
    }
} // check use same side condition

int checkpoint(point A, point B, point C, point X){
    float eps = 1e-5;
    float S = area(A, B, C);
    float S1 = area(A, B, X);
    float S2 = area(A, C, X);
    float S3 = area(B, C, X);
    std::cout << S << " " << S1 << " " << S2 << " " << S3 << std::endl;
    if(S == 0) {
        return -1;
    }
    if(S1 * S2 * S3 == 0) {
        return 0;
    }
    if(fabs((S - (S1 + S2 + S3))) < eps) {
        return 1;
    }
    else {
        return 0;
    }
} //check use area condition

int main(){
    point A(0,0);
    point B(2,0);
    point C(2,3);
    point X(1,100);
    std::cout << checkpoint(A, B, C, X) << std::endl;
    std::cout << checkpoint1(A, B, C, X) << std::endl;
    return 0;
}
