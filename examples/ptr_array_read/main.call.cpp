#include "../memref_bridge.h"

#include <cstdint>
#include <iostream>

extern "C" {
int64_t _mlir_ciface_xdsl_main(MemRefType<int64_t, 1> *array, int size);
}

int main() {
  int64_t myData[5] = {10, 11, 12, 13, 14};
  int64_t myDataExpected[5] = {10, 11, 12, 13, 14};
  size_t size = 5;
  MemRefType<int64_t, 1> myMemref = make_memref_1d<int64_t>(myData, 5, 1);


  const int64_t result = _mlir_ciface_xdsl_main(&myMemref, size);
  std::cout << "EXPECTED '" << myDataExpected[2] << "', got '" << result << "'" << std::endl;
  return 0;
}
