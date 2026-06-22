// Get llvm code using `clang -S -emit-llvm emit_llvm.cpp`
// You can try to add `-o3`, clang will not succed to factorize the loop

#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {

  srand((unsigned)time(0));
  int n = (rand()%6) +1;

  int sum= 0;
  for (int i = 0; i < n; i++) {
    sum+= i;
  }
  for (int i = 0; i < n; i++) {
    sum+= n - i;
  }

  std::cout << "Sum: " << sum<< " n " << n << std::endl;

  return 0;
}
