from __future__ import annotations

from dataclasses import dataclass

from xdsl.dialects.builtin import MemRefType
from xdsl.ir import Attribute

from xdsljson.variables.ty.ty import TyNode


@dataclass(frozen=True)
class TySSA(TyNode):
    def get_type(self) -> Attribute:
        raise ValueError("SSAValue can be any type")

    def get_memref_type(self) -> MemRefType:
        raise NotImplementedError("Not implemented")

    def __repr__(self) -> str:
        return "SSA()"
