"""OCCT package GeomTools (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Standard


class GeomTools:
    """
    The GeomTools package provides utilities for Geometry.

    * SurfaceSet, CurveSet, Curve2dSet : Tools used
    for dumping, writing and reading.

    * Methods to dump, write, read curves and surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomTools) -> None: ...

    @staticmethod
    def SetUndefinedTypeHandler(aHandler: GeomTools_UndefinedTypeHandler) -> None: ...

    @staticmethod
    def GetUndefinedTypeHandler() -> GeomTools_UndefinedTypeHandler: ...

class GeomTools_Curve2dSet:
    """Stores a set of Curves from Geom2d."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Curves."""

    @overload
    def __init__(self, theOther: GeomTools_Curve2dSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, C: nanoocp.Geom2d.Geom2d_Curve) -> int:
        """
        Incorporate a new Curve in the set and returns
        its index.
        """

    def Curve2d(self, I: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns the Curve of index <I>."""

    def Index(self, C: nanoocp.Geom2d.Geom2d_Curve) -> int:
        """Returns the index of <L>."""

class GeomTools_CurveSet:
    """Stores a set of Curves from Geom."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Curves."""

    @overload
    def __init__(self, theOther: GeomTools_CurveSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, C: nanoocp.Geom.Geom_Curve) -> int:
        """
        Incorporate a new Curve in the set and returns
        its index.
        """

    def Curve(self, I: int) -> nanoocp.Geom.Geom_Curve:
        """Returns the Curve of index <I>."""

    def Index(self, C: nanoocp.Geom.Geom_Curve) -> int:
        """Returns the index of <L>."""

class GeomTools_SurfaceSet:
    """Stores a set of Surfaces from Geom."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Surfaces."""

    @overload
    def __init__(self, theOther: GeomTools_SurfaceSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, S: nanoocp.Geom.Geom_Surface) -> int:
        """
        Incorporate a new Surface in the set and returns
        its index.
        """

    def Surface(self, I: int) -> nanoocp.Geom.Geom_Surface:
        """Returns the Surface of index <I>."""

    def Index(self, S: nanoocp.Geom.Geom_Surface) -> int:
        """Returns the index of <L>."""

class GeomTools_UndefinedTypeHandler(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomTools_UndefinedTypeHandler) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
