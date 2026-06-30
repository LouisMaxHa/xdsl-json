from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from pydantic import Field
from xdsl.builder import Builder

from xdsljson.operations.codegen import OpNode
from xdsljson.trace import trace_step
from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.val.val import ValNode
from xdsljson.variables.var import Var


class VarOp(OpNode, Var):
    op: Literal["var"] = "var"
    name: str
    indices: Sequence[VarOp | int | str] = Field(default_factory=list)
    type: TyNode | None = None

    def __init__(
        self,
        name: str = "",
        indices: Sequence[VarOp | int | str] | None = None,
        type: TyNode | None = None,
        **data,
    ):
        super().__init__(
            name=name,
            indices=indices if indices is not None else [],
            type=type,
            **data,
        )

    # TODO: rename load to avoid confusion with get_SSA that dont use index
    @trace_step("VarOp({self.name}, {self.indices})")
    def codegen(self, builder: Builder) -> Sequence[ValNode]:
        return [Var(self.name, self.indices, self.type).load(builder)]
