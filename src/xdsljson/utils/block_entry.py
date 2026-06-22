from xdsl.dialects.func import FuncOp
from xdsl.ir import Block


def function_entry_block(block: Block | None) -> Block:
    """Bloc d'entrée de la fonction englobante (pas un bloc imbriqué scf/while/if)."""
    if block is None:
        raise ValueError("function_entry_block requires a non-null block")

    current: Block | None = block
    while current is not None:
        parent_op = current.parent_op()
        if isinstance(parent_op, FuncOp):
            entry = parent_op.body.blocks.first
            assert entry is not None
            return entry
        current = current.parent_block()

    return block
