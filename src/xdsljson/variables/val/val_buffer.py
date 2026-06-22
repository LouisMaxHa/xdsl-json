from __future__ import annotations

from collections.abc import Sequence

from xdsl.builder import Builder
from xdsl.dialects import arith
from xdsl.dialects.builtin import DYNAMIC_INDEX, MemRefType, StridedLayoutAttr
from xdsl.dialects.memref import DimOp, ReinterpretCastOp, ViewOp
from xdsl.ir import Attribute, SSAValue

from xdsljson.trace import trace_step
from xdsljson.utils import ssa_val
from xdsljson.utils.enum_scalars import Scalar
from xdsljson.utils.ssa_dim import dimensions_to_ssa
from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.ty.ty_buffer import TyBuffer
from xdsljson.variables.val.val import ValNode
from xdsljson.variables.val.val_memref import ValMemref
from xdsljson.variables.val.val_SSA import ValSSA


class ValBuffer(ValNode):
    addr: SSAValue
    ty: TyBuffer

    # ──────────── Init ────────────
    def __init__(
        self, ty: TyBuffer, addr: SSAValue
    ):
        assert addr.type == ty.get_type(), f"addr SSAValue type {addr.type} \
            does not match expected {ty.get_type()}"

        self.addr = addr
        self.ty = ty

        assert len(self.ty.dimensions) >= 1

    def __repr__(self) -> str:
        return f"ValBuffer(addr, {self.ty!r})"

    @staticmethod
    @trace_step("ValBuffer.init_from", display_entry=True)
    def init_from(
        type: TyNode, source: ValNode, builder: Builder
    ) -> ValBuffer:
        assert isinstance(type, TyBuffer)
        assert isinstance(source, (ValMemref, ValSSA))
        return ValBuffer(type, source.get_SSA([], builder))

    # ──────────── Getter ────────────
    def get_ty(self) -> TyBuffer:
        return self.ty

    def get_type(self) -> MemRefType:
        return self.ty.get_type()

    def get_base(self) -> TyNode:
        return self.ty.base

    def get_dim(self, builder: Builder) -> Sequence[SSAValue]:
        return dimensions_to_ssa(
            self.ty.dimensions,
            self.addr,
            builder
        )

    def _get_SSA(self, builder: Builder) -> SSAValue:
        return self.addr

    # ──────────── Load ────────────
    @trace_step("{repr(self)}.load")
    def _load(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        builder: Builder,
    ) -> ValNode:
        assert index == []
        return self

    # ──────────── Store ────────────
    @trace_step("{repr(self)}.store")
    def _store(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        source: ValNode,
        builder: Builder,
    ) -> None:
        raise NotImplementedError


    # ──────────── n_elements ────────────
    """Nombre d'éléments struct = taille buffer / taille struct (octets)."""
    def get_size(self, builder: Builder) -> SSAValue | int:
        assert len(self.ty.dimensions) >= 1
        struct_size = self.ty.base.struct.SIZE

        # Static size
        n_bytes = self.ty.get_bytes_size()
        if n_bytes is not None:
            assert n_bytes % struct_size == 0
            n_elements =  n_bytes // struct_size
            return n_elements


        # TODO: multiples dim
        assert len(self.ty.dimensions) == 1, "TODO: Only supported for one element"

        # Size (bytes)
        n_bytes_op = DimOp.from_source_and_index(
            self.get_SSA([], builder),
            ssa_val.val_to_SSAValue(0, Scalar.idx, builder)
        )
        builder.insert(n_bytes_op)
        n_bytes = n_bytes_op.result

        # Size (elements)
        struct_size = ssa_val.val_to_SSAValue(struct_size, Scalar.idx, builder)
        div_op = arith.DivUIOp(n_bytes, struct_size)
        builder.insert(div_op)
        return div_op.result


    def build_view(
        self,
        field_name: str,
        builder: Builder,
    ) -> ValMemref | ValBuffer:
        from xdsljson.variables.factory import Factory

        # Load infos
        struct = self.ty.base.struct
        field = struct.FIELDS[field_name]
        field_info = struct.FIELDS[field_name]
        field_type = field_info.TYPE.get_type()
        row_count = self.get_size(builder)
        assert struct.SIZE % field.SIZE == 0


        # ──────────── Get dimensions
        # Offset
        offset_ssa = ssa_val.val_to_SSAValue(field.OFFSET, Scalar.idx, builder)

        # Size after flatten
        row_count = self.get_size(builder)
        stride_size = struct.SIZE // field.SIZE
        if isinstance(row_count, int):
            flat_size = row_count * stride_size
            flat_size_ssa = []
            resulting_size = row_count

        else:
            flat_size = DYNAMIC_INDEX
            resulting_size = DYNAMIC_INDEX
            stride_ssa = ssa_val.val_to_SSAValue(stride_size, Scalar.idx, builder)
            flat_size_op = arith.MuliOp(row_count, stride_ssa)
            builder.insert(flat_size_op)
            flat_size_ssa = [flat_size_op.result]

        # ──────────── Flatten

        view_op = ViewOp(
            self.get_SSA([], builder),
            offset_ssa,
            flat_size_ssa,
            MemRefType(
                field_type,
                #[flat_size] On ne doit donner les dimensions que si dynamique
                [flat_size]
            ),
        )
        builder.insert(view_op)
        flat_view = view_op.result

        # ──────────── Add strides
        cast_op = ReinterpretCastOp.from_dynamic(
            flat_view,
            [0],
            [row_count],
            [stride_size],
            # TODO: Pourquoi re-indiquer les strides dans le result type ?????
            MemRefType(
                field_type,
                [resulting_size],
                StridedLayoutAttr(
                    [stride_size],
                    0
                )
            ),
        )
        builder.insert(cast_op)

        dimension = row_count if isinstance(row_count, int) else None
        return Factory.generic_memref(
            [dimension],
            field_info.TYPE,
            cast_op.result
        )
