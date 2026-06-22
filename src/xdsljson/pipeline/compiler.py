"""Orchestration de la compilation JSON/YAML → exécutable natif."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from xdsl.transforms.convert_memref_to_ptr import ConvertMemRefToPtr
from xdsl.transforms.convert_ptr_to_llvm import ConvertPtrToLLVMPass
from xdsl.transforms.convert_ptr_type_offsets import ConvertPtrTypeOffsetsPass
from xdsl.transforms.reconcile_unrealized_casts import ReconcileUnrealizedCastsPass

from xdsljson.pipeline.cli import parse_args
from xdsljson.pipeline.commands import (
    Toolchain,
    build_sample_ast_json,
    compile_llvm_to_object,
    convert_to_llvm,
    init_xdsl,
    link_executable,
    load_input_file,
    run_mlir_opt,
    set_display_cmd,
    xdsl_to_mlir,
)
from xdsljson.trace import configure_trace, enable_trace


def print_if(cond: bool, header: str, path: Path):
    if cond:
        print()
        print("────── " + header)
        print(path.read_text())
        print()

XDSL_OPT_PASSES: list[
    type[
      ConvertMemRefToPtr
    | ConvertPtrTypeOffsetsPass
    | ConvertPtrToLLVMPass
    | ReconcileUnrealizedCastsPass
    ]
] = [
    # ConvertMemRefToPtr,
    # ConvertPtrTypeOffsetsPass,
    # ConvertPtrToLLVMPass,
    # ReconcileUnrealizedCastsPass
]

MLIR_OPT_PASSES: Sequence[str] = [
    "--loop-invariant-code-motion",
    "--cse",
    "--canonicalize",
    "--symbol-dce",
    # `--mem2reg` # incompatible avec memref.alloca et scf.while ??
    "--expand-strided-metadata",
    "--normalize-memrefs",
    "--memref-expand",
    "--fold-memref-alias-ops",
]

MLIR_OPT_LOWER_TO_LLVM: Sequence[str] = [
    "convert-index-to-llvm",
    "lower-affine",
    "convert-scf-to-cf",
    "expand-strided-metadata",
    "normalize-memrefs",
    "memref-expand",
    "fold-memref-alias-ops",
    "finalize-memref-to-llvm",
    "convert-cf-to-llvm",
    "convert-func-to-llvm",
    "convert-arith-to-llvm",
    "reconcile-unrealized-casts",
]

def main(argv: Sequence[str] | None = None) -> int:
    # Read params and configuration
    args = parse_args(argv)
    configure_trace()
    set_display_cmd(args.cmd)
    project_root = args.project_root.resolve()
    toolchain = Toolchain.discover(
        args.mlir_bin_dir,
        project_root=project_root
    )

    # Set build path
    input_path = args.input
    stem = input_path.parent.stem
    build_dir = project_root / "build"
    build_dir.mkdir(parents=True, exist_ok=True)
    path_call      = input_path.with_suffix(".call.cpp")
    path_xdsl      = build_dir / f"{stem}.xdsl.mlir"
    path_mlir      = build_dir / f"{stem}.mlir"
    path_optimized = build_dir / f"{stem}.mlir.opt"
    path_llvm_mlir = build_dir / f"{stem}.llvm.mlir"
    path_llvm      = build_dir / f"{stem}.ll"
    path_librairie = build_dir / f"{stem}.o"
    path_runnable  = input_path.with_suffix(".out")

    # Json -> Pydantic AST
    data = load_input_file(input_path)
    function_ast = build_sample_ast_json(data)

    # Pydantic -> xDSL
    if args.tree:
        print()
        print("────── Python AST")
        enable_trace(True)
    ctx, module, builder = init_xdsl()
    function_ast.codegen(builder)

    # Print
    xdsl_to_mlir(module, path_xdsl)
    print_if(args.xdsl, "xDSL", path_xdsl)

    # xDSL passes
    for passe in XDSL_OPT_PASSES:
        passe().apply(ctx, module)

        if args.xdsl_passes:
            xdsl_to_mlir(module, path_mlir)
            print_if(args.xdsl_passes,
                f"xDSL afte {passe.__name__} passe",
                path_mlir
            )

    # Print
    if args.xdsl_opti:
        xdsl_to_mlir(module, path_mlir)
        print_if(args.xdsl_opti, "xDSL opti", path_mlir)

    # xDSL -> mlir
    xdsl_to_mlir(module, path_mlir)
    print_if(args.mlir, "MLIR", path_mlir)

    # Verify
    module.verify()

    # MLIR passes
    run_mlir_opt(
        toolchain,
        path_mlir,
        path_optimized,
        MLIR_OPT_PASSES
    )
    print_if(args.mlir_opti, "Optimized MLIR", path_optimized)

    # mlir -> llvm mlir
    passes = f"builtin.module({','.join(MLIR_OPT_LOWER_TO_LLVM)})"
    run_mlir_opt(
        toolchain,
        path_optimized,
        path_llvm_mlir,
        [f"--pass-pipeline={passes}"]
    )
    print_if(args.llvm_mlir, "MLIR LLVM dialect", path_llvm_mlir)

    # llvm mlir -> llvm
    convert_to_llvm(
        toolchain,
        path_llvm_mlir,
        path_llvm
    )
    print_if(args.llvm, "LLVM", path_llvm)

    # llvm -> librairie
    compile_llvm_to_object(
        toolchain,
        path_llvm,
        path_librairie
    )

    # librairie + .cpp -> executable
    link_executable(
        toolchain,
        path_call,
        path_librairie,
        path_runnable,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
