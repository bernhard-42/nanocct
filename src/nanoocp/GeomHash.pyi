"""OCCT package GeomHash (toolkit TKG3d)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Poly


class GeomHash_SurfaceHasher:
    """
    Polymorphic hasher for Geom_Surface using RTTI dispatch.
    Used for geometry deduplication.
    """

    @overload
    def __init__(self, theCompTolerance: float = 1e-12, theHashTolerance: float = 1e-07) -> None: ...

    @overload
    def __init__(self, theOther: GeomHash_SurfaceHasher) -> None: ...

    @overload
    def __call__(self, theSurface: nanoocp.Geom.Geom_Surface | None) -> int: ...

    @overload
    def __call__(self, theSurface1: nanoocp.Geom.Geom_Surface | None, theSurface2: nanoocp.Geom.Geom_Surface | None) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...

class GeomHash_CurveHasher:
    """
    Polymorphic hasher for Geom_Curve using RTTI dispatch.
    Used for geometry deduplication.
    """

    @overload
    def __init__(self, theCompTolerance: float = 1e-12, theHashTolerance: float = 1e-07) -> None: ...

    @overload
    def __init__(self, theOther: GeomHash_CurveHasher) -> None: ...

    @overload
    def __call__(self, theCurve: nanoocp.Geom.Geom_Curve | None) -> int: ...

    @overload
    def __call__(self, theCurve1: nanoocp.Geom.Geom_Curve | None, theCurve2: nanoocp.Geom.Geom_Curve | None) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...

class GeomHash_TriangulationHasher:
    @overload
    def __init__(self, theCompTolerance: float = 2.220446049250313e-16, theHashTolerance: float = 2.220446049250313e-16) -> None: ...

    @overload
    def __init__(self, theOther: GeomHash_TriangulationHasher) -> None: ...

    @overload
    def __call__(self, theTri: nanoocp.Poly.Poly_Triangulation | None) -> int: ...

    @overload
    def __call__(self, theTri1: nanoocp.Poly.Poly_Triangulation | None, theTri2: nanoocp.Poly.Poly_Triangulation | None) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...

class GeomHash_Polygon3DHasher:
    @overload
    def __init__(self, theCompTolerance: float = 2.220446049250313e-16, theHashTolerance: float = 2.220446049250313e-16) -> None: ...

    @overload
    def __init__(self, theOther: GeomHash_Polygon3DHasher) -> None: ...

    @overload
    def __call__(self, thePoly: nanoocp.Poly.Poly_Polygon3D | None) -> int: ...

    @overload
    def __call__(self, thePoly1: nanoocp.Poly.Poly_Polygon3D | None, thePoly2: nanoocp.Poly.Poly_Polygon3D | None) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...

class GeomHash_Polygon2DHasher:
    @overload
    def __init__(self, theCompTolerance: float = 2.220446049250313e-16, theHashTolerance: float = 2.220446049250313e-16) -> None: ...

    @overload
    def __init__(self, theOther: GeomHash_Polygon2DHasher) -> None: ...

    @overload
    def __call__(self, thePoly: nanoocp.Poly.Poly_Polygon2D | None) -> int: ...

    @overload
    def __call__(self, thePoly1: nanoocp.Poly.Poly_Polygon2D | None, thePoly2: nanoocp.Poly.Poly_Polygon2D | None) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...

class PolygonOnTriHashKey:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PolygonOnTriHashKey) -> None: ...

    @property
    def Poly(self) -> nanoocp.Poly.Poly_PolygonOnTriangulation: ...

    @Poly.setter
    def Poly(self, arg: nanoocp.Poly.Poly_PolygonOnTriangulation, /) -> None: ...

    @property
    def TriRepId(self) -> int: ...

    @TriRepId.setter
    def TriRepId(self, arg: int, /) -> None: ...

class GeomHash_PolygonOnTriHasher:
    @overload
    def __init__(self, theCompTolerance: float = 2.220446049250313e-16, theHashTolerance: float = 2.220446049250313e-16) -> None: ...

    @overload
    def __init__(self, theOther: GeomHash_PolygonOnTriHasher) -> None: ...

    @overload
    def __call__(self, theKey: PolygonOnTriHashKey) -> int: ...

    @overload
    def __call__(self, theKey1: PolygonOnTriHashKey, theKey2: PolygonOnTriHashKey) -> bool: ...

    @property
    def CompTolerance(self) -> float: ...

    @CompTolerance.setter
    def CompTolerance(self, arg: float, /) -> None: ...

    @property
    def HashTolerance(self) -> float: ...

    @HashTolerance.setter
    def HashTolerance(self, arg: float, /) -> None: ...
