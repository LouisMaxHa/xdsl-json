from __future__ import annotations

from collections.abc import Sequence
from sqlite3 import NotSupportedError

from xdsl.builder import Builder
from xdsl.dialects import memref
from xdsl.dialects.builtin import MemRefType
from xdsl.dialects.memref import LoadOp
from xdsl.ir import Attribute, SSAValue
from xdsl.parser import DYNAMIC_INDEX

from xdsljson.trace import trace_step
from xdsljson.utils.ssa_check import all_ssavalues
from xdsljson.utils.ssa_dim import dimensions_to_ssa
from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.ty.ty_memref import TyMemref
from xdsljson.variables.ty.ty_SSA import TySSA
from xdsljson.variables.val.val import ValNode


def get_memref_dim(ty: Attribute) -> str:
    assert isinstance(ty, MemRefType)
    return ty.__repr__().lstrip("memref<").split(", ")[0].split(">")[0]


class ValMemref(ValNode):
    addr: SSAValue
    ty: TyMemref

    # ──────────── Init ────────────
    # Problème avec les structs, j'ai du memref<5xmemref<8xi8>>
    def __init__(self, ty: TyMemref, addr: SSAValue):
        ssa_type = addr.type
        assert isinstance(ssa_type, MemRefType), f"Got {type(addr)}"
        ty_shape = ty.get_type().shape
        ssa_shape = ssa_type.shape
        assert ty_shape == ssa_shape , (
            f"Ty shape {ty_shape} donc match given SSA shape {ssa_shape}".replace(
                str(DYNAMIC_INDEX), "DYNAMIC_INDEX"
            )
        )

        self.addr = addr
        self.ty = ty

    def __repr__(self) -> str:
        return f"ValMemref(addr, {self.ty!r})"

    @staticmethod
    @trace_step("ValMemref.init_from", display_entry=True)
    def init_from(type: TyNode, source: ValNode, builder: Builder) -> ValMemref:
        assert isinstance(type, TyMemref)

        match source.get_ty():
            case TyMemref():
                return ValMemref(type, source.get_SSA([], builder))
            case TySSA():
                return ValMemref(type, source.get_SSA([], builder))
            case _:
                raise NotSupportedError

    # ──────────── Getter ────────────
    def get_ty(self) -> TyMemref:
        return self.ty

    def get_type(self) -> MemRefType:
        return self.ty.get_type()

    def get_base(self) -> TyNode:
        return self.ty.base

    def get_dim(self, builder: Builder) -> Sequence[SSAValue]:
        return dimensions_to_ssa(self.ty.dimensions, self.addr, builder)

    def _get_SSA(self, builder: Builder) -> SSAValue:
        return self.addr

    # ──────────── Load ────────────
    def _load(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        builder: Builder,
    ) -> ValNode:
        from xdsljson.variables.factory import Factory

        if index == []:
            return self

        # Split index
        consuming = index[: len(self.ty.dimensions)]
        remaining = index[len(self.ty.dimensions) :]
        assert all_ssavalues(consuming)

        # Load
        op = LoadOp.get(self.addr, consuming)
        builder.insert(op)
        valNode = Factory.from_SSA(self.ty.base, op.results[0], builder)

        # Recurse
        if remaining:
            return valNode.load(remaining, builder)
        return valNode

    # ──────────── Store ────────────
    def _store(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        source: ValNode,
        builder: Builder,
    ):

        # Split index
        assert len(index) >= len(self.ty.dimensions)
        consuming = index[: len(self.ty.dimensions)]
        remaining = index[len(self.ty.dimensions) :]
        assert all_ssavalues(consuming)

        # Insert
        if remaining == []:
            op = memref.StoreOp.get(source.get_SSA([], builder), self.addr, consuming)
            builder.insert(op)
            return

        self.load(consuming, builder).store(remaining, source, builder)
