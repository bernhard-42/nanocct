"""OCCT package Geom2dHash (toolkit TKG2d)"""

from typing import overload

import nanoocp.Geom2d


class Geom2dHash_CurveHasher:
    """
    Polymorphic hasher for Geom2d_Curve using RTTI dispatch.
    Used for geometry deduplication.
    """

    @overload
    def __init__(self, theCompTolerance: float = 1e-12, theHashTolerance: float = 1e-07) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dHash_CurveHasher) -> None: ...

    @overload
    def __call__(self, theCurve: nanoocp.Geom2d.Geom2d_Curve) -> int: ...

    @overload
    def __call__(self, theCurve1: nanoocp.Geom2d.Geom2d_Curve, theCurve2: nanoocp.Geom2d.Geom2d_Curve) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...
