"""C++ namespace LProp_CurveUtils (OCCT package LProp)"""

from typing import overload


class DirectAccess:
    """
    Direct access policy: calls D0/D1/D2/D3 methods on the curve object.
    Works with occ::handle<T> and by-value curve types.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DirectAccess) -> None: ...
