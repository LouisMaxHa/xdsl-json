"""Conversion des dimensions statiques/dynamiques en SSA Values."""

from __future__ import annotations

from collections.abc import Sequence

from xdsl.builder import Builder
from xdsl.dialects.memref import DimOp
from xdsl.ir import Attribute, SSAValue

from xdsljson.utils import ssa_val
from xdsljson.utils.enum_scalars import Scalar


def dimensions_to_ssa(
    dimensions: Sequence[int | None],
    ref: SSAValue,
    builder: Builder,
) -> Sequence[SSAValue]:
    """int -> constante index ; None -> memref.dim sur ``ref``."""
    result: list[SSAValue] = []
    for axis, dim in enumerate(dimensions):
        match dim:
            case None:
                axis_ssa = ssa_val.val_to_SSAValue(axis, Scalar.idx, builder)
                op = DimOp.from_source_and_index(ref, axis_ssa)
                builder.insert(op)
                result.append(op.result)

            case int():
                result.append(ssa_val.val_to_SSAValue(dim, Scalar.idx, builder))
    return result


def index_to_ssa(
    index: Sequence[str | SSAValue[Attribute] | int], builder: Builder
) -> Sequence[str | SSAValue[Attribute]]:
    return [
        val
        if isinstance(val, (str, SSAValue))
        else ssa_val.val_to_SSAValue(val, Scalar.idx, builder)
        for val in index
    ]
