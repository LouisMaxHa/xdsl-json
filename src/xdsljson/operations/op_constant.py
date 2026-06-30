from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from xdsl.builder import Builder

from xdsljson.operations.codegen import OpNode
from xdsljson.trace import trace_step
from xdsljson.utils import ssa_val
from xdsljson.utils.enum_scalars import Scalar
from xdsljson.variables.val.val import ValNode
from xdsljson.variables.val.val_SSA import ValSSA


class ConstOp(OpNode):
    """Constant value operand."""

    op: Literal["const"] = "const"
    val: float | int
    type: Scalar = Scalar.i64

    def __init__(self, *args, **data):
        val: float | int | None = args[0] if args else data.pop("val", None)
        t: str | Scalar = args[1] if len(args) >= 2 else data.pop("type", "i64")
        if isinstance(t, str):
            t = Scalar(t)

        super().__init__(val=val, type=t, **data)

    @trace_step("ConstOp({self.val}, {self.type})")
    def codegen(self, builder: Builder) -> Sequence[ValNode]:
        return [ValSSA(
            ssa_val.val_to_SSAValue(self.val, self.type, builder)
        )]
