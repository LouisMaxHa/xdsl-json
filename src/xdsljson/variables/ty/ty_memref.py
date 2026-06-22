from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from xdsl.dialects.builtin import DYNAMIC_INDEX, MemRefType

from xdsljson.variables.ty.ty import TyNode


@dataclass(frozen=True)
class TyMemref(TyNode):
    dimensions: Sequence[int | None]
    base: TyNode

    def get_n_elements(self) -> Sequence[int | None]:
        return self.dimensions

    def get_type(self) -> MemRefType:
        dimension = [d or DYNAMIC_INDEX for d in self.dimensions]

        return MemRefType(self.base.get_type(), dimension)

    def get_memref_type(self) -> MemRefType:
        return self.get_type()

    def __repr__(self) -> str:
        return f"Memref(dims={list(self.dimensions)!r}, base={self.base!r})"
