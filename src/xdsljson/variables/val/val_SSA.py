from __future__ import annotations

from collections.abc import Sequence

from xdsl.builder import Builder
from xdsl.ir import Attribute, SSAValue

from xdsljson.trace import trace_step
from xdsljson.variables.ty.ty import TyNode
from xdsljson.variables.ty.ty_SSA import TySSA
from xdsljson.variables.val.val import ValNode


class ValSSA(ValNode):
    ty: TySSA
    addr: SSAValue


    # ──────────── Init ────────────
    def __init__(self, addr: SSAValue):
        self.ty = TySSA()
        self.addr = addr

    @staticmethod
    @trace_step("ValSSA.init_from", display_entry=True)
    def init_from(
        type: TyNode, source: ValNode, builder: Builder
    ) -> ValSSA:
        raise ValueError("ValSSA should not be used for operations")

    # ──────────── Getter ────────────
    def get_ty(self) -> TySSA:
        return self.ty

    def get_type(self) -> Attribute:
        return self.addr.type

    def get_dim(self, builder: Builder) -> Sequence[SSAValue]:
        raise NotImplementedError("Not implemented")

    def _get_SSA(
        self,
        builder: Builder,
    ) -> SSAValue:
        return self.addr


    # ──────────── Load ────────────
    def _load(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        builder: Builder,
    ) -> ValNode:
        raise ValueError("ValSSA should not be used for operations")


    # ──────────── Store ────────────
    def _store(
        self,
        index: Sequence[str | SSAValue[Attribute]],
        source: ValNode,
        builder: Builder,
    ):
        raise ValueError("ValSSA should not be used for operations")

