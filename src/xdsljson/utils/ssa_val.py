from __future__ import annotations

from typing import cast

from xdsl.builder import Builder
from xdsl.dialects.arith import ConstantOp
from xdsl.dialects.builtin import (
    AnyFloat,
    FloatAttr,
    IndexType,
    IntegerAttr,
    IntegerType,
)
from xdsl.ir import Attribute, OpResult, SSAValue, SSAValues
from xdsl.rewriter import InsertPoint

from xdsljson.utils.block_entry import function_entry_block
from xdsljson.utils.enum_scalars import Scalar, ScalarFamily

const_heap: dict[tuple[int | float, str], SSAValues[OpResult[Attribute]]] = {}

# TODO: Clear variable end of function


def idx_to_ssavalues(value: int | SSAValue, builder: Builder) -> SSAValue:
    if isinstance(value, SSAValue):
        return value
    return val_to_SSAValue(value, Scalar.idx, builder)


def val_to_SSAValues(
    value: int | float, type: Scalar, builder: Builder
) -> SSAValues[OpResult[Attribute]]:
    key = (value, type.get_type().__str__())

    name = f"const{value}.{type.get_type().__str__()}"

    if key not in const_heap.keys():
        # Create const
        mlir_type = type.get_type()
        match type.get_kind():
            case ScalarFamily.float:
                attr = FloatAttr(float(value), cast(AnyFloat, mlir_type))
                op = ConstantOp(attr)

            case ScalarFamily.int:
                attr = IntegerAttr(int(value), cast(IntegerType, mlir_type))
                op = ConstantOp(attr)

            case ScalarFamily.idx:
                op = ConstantOp.from_int_and_width(
                    int(value), cast(IndexType, mlir_type)
                )

        op.result.name_hint = name

        # Insert it
        entry_block = function_entry_block(builder.insertion_point.block)
        builder.insert_op(op, InsertPoint.at_start(entry_block))
        const_heap[key] = op.results

    return const_heap[key]


def val_to_SSAValue(value: int | float, type: Scalar, builder: Builder) -> SSAValue:
    return val_to_SSAValues(value, type, builder)[0]
