from __future__ import annotations

from enum import StrEnum
from typing import cast

from xdsl.dialects.builtin import (
    Float16Type,
    Float32Type,
    Float64Type,
    Float80Type,
    Float128Type,
    IndexType,
    IntegerType,
    Signedness,
)
from xdsl.ir import Attribute


class ScalarFamily(StrEnum):
    int = "int"
    float = "float"
    idx = "index"


class Scalar(StrEnum):
    i64 = "i64"
    i32 = "i32"
    i16 = "i16"
    i8 = "i8"
    i1 = "i1"
    I64 = "I64"
    I32 = "I32"
    I16 = "I16"
    I8 = "I8"
    I1 = "I1"
    f16 = "f16"
    f32 = "f32"
    f64 = "f64"
    f80 = "f80"
    f128 = "f128"
    idx = "index"

    def byte_size(self) -> int:
        """Taille en octets d'un scalaire MLIR."""
        match self:
            case Scalar.i1 | Scalar.I1:
                return 1
            case Scalar.i8 | Scalar.I8:
                return 1
            case Scalar.i16 | Scalar.I16 | Scalar.f16:
                return 2
            case Scalar.i32 | Scalar.I32 | Scalar.f32:
                return 4
            case Scalar.i64 | Scalar.I64 | Scalar.f64 | Scalar.idx:
                return 8
            case Scalar.f80:
                return 10
            case Scalar.f128:
                return 16

    def get_kind(self) -> ScalarFamily:
        match self:
            case Scalar.i64 | Scalar.i32 | Scalar.i16 | Scalar.i8 \
            | Scalar.i1 | Scalar.I64 | Scalar.I32 | Scalar.I16 \
            | Scalar.I8 | Scalar.I1:
                return ScalarFamily.int
            case Scalar.f16 | Scalar.f32 | Scalar.f64 \
                | Scalar.f80 | Scalar.f128:
                return ScalarFamily.float
            case Scalar.idx:
                return ScalarFamily.idx


    def get_type(self) -> Attribute:
        match self:
            case Scalar.i64:
                return IntegerType(64)
            case Scalar.i32:
                return IntegerType(32)
            case Scalar.i16:
                return IntegerType(16)
            case Scalar.i8:
                return IntegerType(8)
            case Scalar.i1:
                return IntegerType(1)
            case Scalar.I64:
                return IntegerType(64, Signedness.SIGNLESS)
            case Scalar.I32:
                return IntegerType(32, Signedness.SIGNLESS)
            case Scalar.I16:
                return IntegerType(16, Signedness.SIGNLESS)
            case Scalar.I8:
                return IntegerType(8, Signedness.SIGNLESS)
            case Scalar.I1:
                return IntegerType(1, Signedness.SIGNLESS)
            case Scalar.f16:
                return Float16Type()
            case Scalar.f32:
                return Float32Type()
            case Scalar.f64:
                return Float64Type()
            case Scalar.f80:
                return Float80Type()
            case Scalar.f128:
                return Float128Type()
            case Scalar.idx:
                return IndexType()

    @staticmethod
    def from_type(attr: Attribute) -> Scalar | None:
        if isinstance(attr, IntegerType):
            int_type = cast("IntegerType[int, Signedness]", attr)
            width = int_type.bitwidth
            signedness = int_type.signedness.data

            match signedness:
                case Signedness.SIGNED:
                    match width:
                        case 64:
                            return Scalar.i64
                        case 32:
                            return Scalar.i32
                        case 16:
                            return Scalar.i16
                        case 8:
                            return Scalar.i8
                        case 1:
                            return Scalar.i1
                        case _:
                            raise ValueError(f"Not supported {attr}")
                case Signedness.UNSIGNED | Signedness.SIGNLESS:
                    match width:
                        case 64:
                            return Scalar.i64
                        case 32:
                            return Scalar.i32
                        case 16:
                            return Scalar.i16
                        case 8:
                            return Scalar.i8
                        case 1:
                            return Scalar.i1
                        case _:
                            raise ValueError(f"Not supported {attr}")

        if isinstance(attr, Float16Type):
            return Scalar.f16
        if isinstance(attr, Float32Type):
            return Scalar.f32
        if isinstance(attr, Float64Type):
            return Scalar.f64
        if isinstance(attr, Float80Type):
            return Scalar.f80
        if isinstance(attr, Float128Type):
            return Scalar.f128
        if isinstance(attr, IndexType):
            return Scalar.idx

        return None
