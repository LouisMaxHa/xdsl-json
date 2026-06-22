from collections.abc import Sequence
from typing import TypeGuard

from xdsl.ir import Attribute, SSAValue


def all_ssavalues(
    seq: Sequence[str | SSAValue[Attribute]],
) -> TypeGuard[Sequence[SSAValue[Attribute]]]:
    return all(isinstance(x, SSAValue) for x in seq)

def all_int(
    seq: Sequence[int | None],
) -> TypeGuard[Sequence[int]]:
    return all(isinstance(x, int) for x in seq)

