#!/usr/bin/env python3
"""Point d'entrée du compilateur xDSL-JSON."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

_FLAG_ALIASES: dict[str, str] = {
    "T": "tree",
    "x": "xdsl",
    "P": "xdsl_passes",
    "X": "xdsl_opti",
    "m": "mlir",
    "M": "mlir_opti",
    "l": "mlir_llvm",
    "L": "llvm",
    "C": "cmd",
}

def _expand_grouped_trace_flags(argv: Sequence[str]) -> list[str]:
    expanded: list[str] = list(argv)
    for arg in argv:
        if not arg.startswith("-"):
            continue

        if not all(
            letter in _FLAG_ALIASES.keys()
            for letter in arg[1::]
        ):
            continue

        expanded.remove(arg)
        for letter in arg[1::]:
            expanded.append(f"--{_FLAG_ALIASES[letter]}")

    return expanded


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="xdsljson",
        description=(
            "Compile une description JSON/YAML en MLIR, puis en exécutable natif "
            "via la toolchain MLIR/LLVM."
        ),
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Chemin vers le fichier d'entrée (.json, .yaml ou .yml).",
    )
    parser.add_argument(
        "--mlir-bin-dir",
        type=Path,
        default=None,
        help=(
            "Répertoire contenant mlir-opt, mlir-translate, llc et clang++ "
            "(sinon MLIR_BIN_DIR ou PATH)."
        ),
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Racine du projet (pour examples/ et build/).",
    )
    parser.add_argument(
        "-T",
        "--tree",
        action="store_true",
        help="Affiche l'AST Python sous forme d'arbre (trace codegen).",
    )
    parser.add_argument(
        "-x",
        "--xdsl",
        action="store_true",
        help="Affiche l'IR xDSL",
    )
    parser.add_argument(
        "-P",
        "--xdsl_passes",
        action="store_true",
        help="Affiche l'IR xDSL après chaque passes.",
    )
    parser.add_argument(
        "-X",
        "--xdsl_opti",
        action="store_true",
        help="Affiche l'IR xDSL après les passes xDSL.",
    )
    parser.add_argument(
        "-m",
        "--mlir",
        action="store_true",
        help="Affiche le MLIR avant optimisation.",
    )
    parser.add_argument(
        "-M",
        "--mlir_opti",
        action="store_true",
        help="Affiche le MLIR après optimisation.",
    )
    parser.add_argument(
        "-l",
        "--llvm_mlir",
        action="store_true",
        help="Affiche le mlir dialect LLVM.",
    )
    parser.add_argument(
        "-L",
        "--llvm",
        action="store_true",
        help="Affiche le LLVM.",
    )
    parser.add_argument(
        "-C",
        "--cmd",
        action="store_true",
        help="Affiche les commandes mlir-opt, mlir-translate, llc, clang++, etc.",
    )
    if argv is None:
        argv = sys.argv[1:]
    return parser.parse_args(_expand_grouped_trace_flags(argv))

if __name__ == "__main__":
    from xdsljson.pipeline.compiler import main

    raise SystemExit(main())
