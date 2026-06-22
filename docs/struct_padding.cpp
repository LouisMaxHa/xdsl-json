#include <cstddef>
#include <iostream>
struct test {
    char c;
    double d;
};

int main(){
    std::cout << "Sizeof test  : " << sizeof(test) << std::endl;
    std::cout << "Sizeof char  : " << sizeof(char) << std::endl;
    std::cout << "Sizeof double: " << sizeof(double) << std::endl;
    std::cout << std::endl;
    std::cout << "Offset c: " << offsetof(test, c) << std::endl;
    std::cout << "Offset d: " << offsetof(test, d) << std::endl;
}