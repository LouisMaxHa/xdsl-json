from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from xdsl.dialects.builtin import MemRefType
from xdsl.ir import Attribute

from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.ty.ty_struct import TyStruct


@dataclass(frozen=True)
class TySOA(TyNode):
    base: TyStruct

    # Number of struct contained
    n_elements: Sequence[int | None]

    def get_count(self) -> Sequence[int | None]:
        return self.n_elements

    def get_sizes(self) -> Sequence[int | None]:
        return [
            n * self.base.struct.SIZE
            if isinstance(n, int) else None
            for n in self.n_elements
        ]

    def get_type(self) -> Attribute:
        raise ValueError("SOA don't have xDSL equivalent")

    def get_memref_type(self) -> MemRefType:
        raise ValueError("SOA don't have equivalent in xDSL")

    def __repr__(self) -> str:
        return f"SOA(base={self.base!r}, n_elements={list(self.n_elements)!r})"
