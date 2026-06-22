from __future__ import annotations

from collections.abc import Sequence

from xdsl.builder import Builder
from xdsl.dialects import memref
from xdsl.dialects.builtin import MemRefType
from xdsl.ir import Attribute, SSAValue

from xdsljson.trace import trace_step
from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.ty.ty_scalar import TyScalar
from xdsljson.variables.val.val import ValNode
from xdsljson.variables.val.val_SSA import ValSSA


class ValScalar(ValNode):
    addr: SSAValue
    ty: TyScalar

    # ──────────── Init ────────────

    def __init__(self, ty: TyScalar, addr: SSAValue):
        expected = MemRefType(ty.get_type(), [])
        assert addr.type == expected, f"\
        addr SSAValue type {getattr(addr, 'type', None)} \
        does not match expected memref type {expected}"

        self.addr = addr
        self.ty = ty

    def __repr__(self) -> str:
        return f"ValScalar(addr, {self.ty!r})"

    @staticmethod
    @trace_step("ValScalar.init_from", display_entry=True)
    def init_from(
        type: TyNode, source: ValNode, builder: Builder
    ) -> ValScalar:
        assert isinstance(type, TyScalar)
        assert isinstance(source, (ValSSA, ValScalar))

        # Alloc
        op = memref.AllocaOp.get(type.get_type(), shape=[])
        builder.insert(op)

        # Create empty val
        val = ValScalar(
            type,
            op.memref
        )

        # Populate val
        val.store([], source, builder)
        return val

    # ──────────── Getter ────────────
    def get_ty(self) -> TyScalar:
        return self.ty

    def get_type(self) -> Attribute:
        return self.ty.get_type()

    def get_dim(self, builder: Builder) -> Sequence[SSAValue]:
        return []

    def _get_SSA(self, builder: Builder) -> SSAValue:
        op = memref.LoadOp.get(
            self.addr,
            []
        )
        builder.insert(op)
        return op.results[0]

    # ──────────── Load ────────────
    def _load(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        builder: Builder,
    ) -> ValNode:
        assert index == []
        return ValSSA(self.get_SSA(index, builder))


    # ──────────── Store ────────────
    def _store(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        source: ValNode,
        builder: Builder,
    ):
        assert index == []
        assert isinstance(source, (ValSSA, ValScalar))
        ssa = source.get_SSA([], builder)

        # Extract ssa value from memref<ssa value>
        if isinstance(ssa.type, MemRefType):
            op = memref.LoadOp.get( ssa, [])
            builder.insert(op)
            ssa = op.results[0]

        # Store
        op = memref.StoreOp.get(
            ssa,
            self.addr,
            []
        )
        builder.insert(op)
