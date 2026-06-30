from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated, Literal

from pydantic import Field
from xdsl.builder import Builder

from xdsljson.operations.codegen import OpNode
from xdsljson.trace import trace_step
from xdsljson.operations.op_define_struct import DefineStructOp
from xdsljson.operations.op_function import FunctionOp
from xdsljson.variables.memory import structs_type
from xdsljson.variables.val.val import ValNode

# Définition de struct ou de function
ModuleStatement = Annotated[DefineStructOp | FunctionOp, Field(discriminator="op")]


class ModuleJsonOp(OpNode):
    """Racine JSON de type module : enregistre les structs puis génère les fonctions."""

    op: Literal["module"] = "module"
    body: Sequence[ModuleStatement]

    def __init__(self, body=None, **data):
        super().__init__(body=body or [], **data)

    @trace_step("ModuleJsonOp")
    def codegen(self, builder: Builder) -> Sequence[ValNode]:
        structs_type.clear()
        for item in self.body:
            item.codegen(builder)
        return []
