"""Builder isolé pour l'inspection de types sans modifier le module généré."""

from __future__ import annotations

from xdsl.builder import Builder
from xdsl.ir import Block
from xdsl.rewriter import InsertPoint

_discard_block = Block()


def discard_builder() -> Builder:
    """Bloc jetable : les opérations y sont insérées, pas dans le module utilisateur."""
    return Builder(InsertPoint.at_end(_discard_block))
