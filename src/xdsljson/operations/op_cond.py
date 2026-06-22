from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Literal

from xdsl.builder import Builder
from xdsl.dialects.scf import IfOp
from xdsl.ir import Attribute, Block

from xdsljson.operations.block import codegenBlock
from xdsljson.operations.codegen import OpNode
from xdsljson.trace import trace_step
from xdsljson.utils.same_types import same_types
from xdsljson.variables.val.val import ValNode

if TYPE_CHECKING:
    from xdsljson.operations.base import BaseValue


class CondOp(OpNode):
    op: Literal["if"] = "if"
    cond: BaseValue
    thenBlock: Sequence[BaseValue]
    elseBlock: Sequence[BaseValue] | None = None

    @trace_step("CondOp")
    def codegen(self, builder: Builder) -> Sequence[ValNode]:
        # Check condition
        conds_ssa = self.cond.codegen(builder)
        assert len(conds_ssa) == 1
        cond_ssa = conds_ssa[0].get_SSA([], builder)

        # Région then : on construit son bloc avec un Builder dédié.
        block_then, result_then  = codegenBlock(self.thenBlock, Block())
        block_else, result_else  = codegenBlock(self.elseBlock, Block())

        # Result type
        return_types: list[Attribute] = []
        if same_types(result_then, result_else):
            return_types = [
                result.get_type()
                for result in result_then
            ]

        # Create IfOp
        if_op = IfOp(
            cond_ssa,
            return_types,
             [block_then],
            [block_else],
        )
        builder.insert(if_op)
        return []
