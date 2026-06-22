from __future__ import annotations

from dataclasses import dataclass

from xdsl.dialects.builtin import MemRefType
from xdsl.ir import Attribute

from xdsljson.utils.enum_scalars import Scalar
from xdsljson.variables.ty.ty import TyNode


@dataclass(frozen=True)
class TyScalar(TyNode):
    scalar: Scalar

    def get_type(self) -> Attribute:
        return self.scalar.get_type()

    def get_memref_type(self) -> MemRefType:
        return MemRefType(
            self.get_type(),
            []
        )

    def __repr__(self) -> str:
        return f"Scalar({self.scalar})"
