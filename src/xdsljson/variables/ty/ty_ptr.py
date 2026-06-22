from __future__ import annotations

from dataclasses import dataclass

from xdsl.dialects.builtin import IntegerType, MemRefType

from xdsljson.variables.ty.ty import TyNode


@dataclass(frozen=True)
class TyPtr(TyNode):
    base: TyNode

    def get_type(self) -> IntegerType:
        # Adresse en i64 à la frontière ABI ; ptr_xdsl n'apparaît qu'au déréférencement.
        return IntegerType(64)

    def get_memref_type(self) -> MemRefType:
        return MemRefType(self.get_type(), [])

    def __repr__(self) -> str:
        return f"Ptr({self.base!r})"
