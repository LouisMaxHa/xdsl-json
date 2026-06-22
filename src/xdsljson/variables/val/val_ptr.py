from __future__ import annotations

from collections.abc import Sequence

from xdsl.builder import Builder
from xdsl.dialects import builtin, llvm, memref, ptr
from xdsl.dialects.builtin import MemRefType
from xdsl.ir import Attribute, SSAValue

from xdsljson.trace import trace_step
from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.ty.ty_ptr import TyPtr
from xdsljson.variables.val.val import ValNode
from xdsljson.variables.val.val_scalar import ValScalar
from xdsljson.variables.val.val_SSA import ValSSA


class ValPtr(ValNode):
    addr: SSAValue
    ty: TyPtr

    # ──────────── Init ────────────

    def __init__(self, ty: TyPtr, addr: SSAValue):
        expected = MemRefType(ty.get_type(), [])
        assert addr.type == expected, f"\
        addr SSAValue type {getattr(addr, 'type', None)} \
        does not match expected memref type {expected}"

        self.addr = addr
        self.ty = ty

    def __repr__(self) -> str:
        return f"ValPtr(addr, {self.ty!r})"

    @staticmethod
    @trace_step("ValPtr.init_from", display_entry=True)
    def init_from(
        type: TyNode, source: ValNode, builder: Builder
    ) -> ValPtr:
        assert isinstance(type, TyPtr)
        assert isinstance(source, (ValSSA, ValScalar, ValPtr))

        # Alloc
        op = memref.AllocaOp.get(type.get_type(), shape=[])
        builder.insert(op)

        # Create empty addr
        val = ValPtr(
            type,
            op.memref
        )

        # Populate addr
        val.store([], source, builder)
        return val

    # ──────────── Getter ────────────
    def get_ty(self) -> TyPtr:
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
        from xdsljson.variables.factory import Factory
        # Return ptr
        if index == []:
            return ValSSA(self.get_SSA(index, builder))

        # Consume index
        consuming = index[0]
        remaining = index[1::]
        assert consuming == "*"

        # i64 -> llvm.ptr
        ssa_i64 = self._get_SSA(builder)
        op_inttoptr = llvm.IntToPtrOp(ssa_i64)
        builder.insert(op_inttoptr)
        ssa_ptr_llvm = op_inttoptr.results[0]

        # llvm.ptr -> ptr.ptr
        op_cast = builtin.UnrealizedConversionCastOp.get(
            [ssa_ptr_llvm],
            [ptr.PtrType()],
        )
        builder.insert(op_cast)
        ssa_ptr = op_cast.results[0]

        # ptr.ptr -> ssa_deref
        op_load = ptr.FromPtrOp(
            ssa_ptr,
            self.ty.base.get_memref_type()
        )
        builder.insert(op_load)
        ssa_derefed = ValSSA(op_load.results[0])

        # Convert to val
        val = Factory.from_val(
            self.ty.base,
            ssa_derefed,
            builder,
        )

        return val.load(remaining, builder)

    # ──────────── Store ────────────
    def _store(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        source: ValNode,
        builder: Builder,
    ):
        assert index == []
        assert isinstance(source, (ValSSA, ValPtr, ValScalar))
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
