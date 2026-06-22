import pprint
from collections.abc import Sequence

from xdsljson.variables.val.val import ValNode


def same_types(
    lhs: Sequence[ValNode],
    rhs: Sequence[ValNode],
) -> bool:
    return (
        len(lhs) == len(rhs)
        and all(
            a.get_type() == b.get_type()
            for a, b in zip(lhs, rhs)
        )
    )

def assert_same_types(
    lhs: Sequence[ValNode],
    rhs: Sequence[ValNode],
) :
    assert len(lhs) == len(rhs)

    for i, l, r in zip(range(len(lhs)), lhs, rhs):
        if l.get_type() != r.get_type():
            print(f"assert_same_type: Missmatch detected at indice {i}")
            print(f"lhs: {repr(l.get_type())}")
            print(f"rhs: {repr(r.get_type())}")
            print("\nVariables:")
            pprint.pprint(vars(l))
            print("\n\n")
            pprint.pprint(vars(r))
            print("\n\n")
            raise ValueError
