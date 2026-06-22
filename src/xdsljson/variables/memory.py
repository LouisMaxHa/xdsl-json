from __future__ import annotations

from typing import NamedTuple

from xdsl.dialects.llvm import LLVMStructType

from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.val.val import ValNode


class FIELD_TYPE(NamedTuple):
    NAME: str
    TYPE: TyNode
    OFFSET: int
    SIZE: int


class STRUCTS_TYPE(NamedTuple):
    NAME: str
    LLVM_TYPE: LLVMStructType
    SIZE: int
    FIELDS: dict[str, FIELD_TYPE]


structs_type: dict[str, STRUCTS_TYPE] = {}
variables_heap: dict[str, ValNode] = {}
