#include "../memref_bridge.h"

#include <cstdint>
#include <iostream>

extern "C" {
int64_t _mlir_ciface_xdsl_main(uintptr_t data_ptr);
}

struct xyz {
  int64_t x;
  int64_t y;
  int64_t z;
};

struct Noeuds {
  xyz* coords;
  int64_t size;
};

struct Simulation {
  Noeuds* positions;
  Noeuds* temperatures;
};

int main() {

  // ──────────── Tableaux contenant les informations ────────────
  xyz* coords_positions = new xyz[5];
  for (int i=0; i<5; i++){
    coords_positions[i].x = i * 3 + 0;
    coords_positions[i].y = i * 3 + 1;
    coords_positions[i].z = i * 3 + 2;
  }

  xyz* coords_temperatures = new xyz[5];
  for (int i=0; i<5; i++){
    coords_temperatures[i].x = (i + 5) * 3 + 0;
    coords_temperatures[i].y = (i + 5) * 3 + 1;
    coords_temperatures[i].z = (i + 5) * 3 + 2;
  }

  // ──────────── Description des tableaux ────────────
  Noeuds* noeuds_positions = new Noeuds;
  noeuds_positions->coords = coords_positions;
  noeuds_positions->size = 5;
  
  Noeuds* noeuds_temperatures = new Noeuds;
  noeuds_temperatures->coords = coords_temperatures;
  noeuds_temperatures->size = 5;

  // ──────────── Simulation ────────────
  Simulation* simu = new Simulation;
  simu->positions = noeuds_positions;
  simu->temperatures = noeuds_temperatures;

  uintptr_t simu_ptr = (uintptr_t)simu;

  const int64_t result = _mlir_ciface_xdsl_main(simu_ptr);
  std::cout << " EXPECTED '" 
    << simu->positions->coords[3].y
    << "', got '" << result << "'" << std::endl;
}
