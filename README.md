# xdsljson

This project lets you generate specialized shared libraries using MLIR, based on JSON function descriptions.
The generated libraries can then be called from your codebase without having to write a complex front-end for your solution.

Unlike working directly with MLIR, the JSON description provides an extra level of abstraction.
This solution is designed to be generic, modular, and accessible — make sure you have a good understanding of each operation before using it.

Additionally, the [xDSL](https://xdsl.dev/) Python library lets you easily define your own dialects and passes.
Feel free to check out their interactive tutorials!


## Usage

Currently, this solution takes a JSON file as input, generates a library containing the functions described in that file, and then compiles a `main.call.cpp` file that calls this library.

```bash
git clone git@github.com:LouisMaxHa/xdsl-json.git
cd xdsl-json
make install

# Run example
uv run python src/xdsljson/pipeline/cli.py examples/soa_read/main.json  

# Run tests
uv run python tests/run_tests.py 
```

## Options
- `--tree`, `-T`        : Print the Python AST as a **T**ree
- `--xdsl`, `-x`        : Print the generated **x**DSL code
- `--xdsl_passes`, `-p` : Print the generated xDSL code after each xDSL **p**ass
- `--xdsl_opti`, `-X`   : Print the generated xDSL code after all xDSL passes
- `--mlir`, `-m`        : Print the generated **M**LIR code
- `--mlir_opti`, `-M`   : Print the generated MLIR code after MLIR passes
- `--mlir_llvm`, `-l`   : Print the MLIR code using the LLVM MLIR dialect
- `--llvm`, `-L`        : Print the generated **L**LVM code
- `--cmd`, `-C`         : Print the **c**ommands used during code generation

- `--mlir-bin-dir` : Directory containing the `mlir-opt` executable
- `--project-root` : Change the current directory (used for `./build`)

## Execution trace example

```bash

```

![Tests](docs/images/tests.png)


## Project structure

```text
.
├── docs/             # Documentation
│   ├── diapo/             # Presentation slides
│   ├── cpp_examples/      # C++ code example that calls an MLIR function with an array parameter
│   └── rapport/           # Work in progress
|
├── examples/         # Files to compile
│   ├── memref_bridge.h    # Converts an array to a MemRef-compatible structure
│   └── array-read/        # An example
│       ├── main.json      # MLIR function to generate
│       └── main.call.cpp  # C++ function calling the generated function
│
├── src/xdsljson/     # Project source code
│   ├── operations/        # Operation definitions
│   ├── pipeline/          # Compilation pipeline management
│   ├── utils/             # Utilities
│   └── variables/
│       ├── ty/            # Type definitions
│       ├── val/           # Instance definitions (= types + memory address)
│       ├── factory.py     # Create instances from a type
│       ├── memory.py      # Register and access instances
│       └── var.py         # Association between variable name <-> instance
│
└── tests/
    └── run_tests.py       # Run tests
```
