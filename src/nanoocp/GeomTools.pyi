"""OCCT package GeomTools (toolkit TKGeomBase)"""

from typing import TextIO, overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Message
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

    @overload
    @staticmethod
    def Dump(S: nanoocp.Geom.Geom_Surface | None) -> str:
        """
        A set of Curves from Geom2d.
        Dumps the surface on the stream.
        """

    @overload
    @staticmethod
    def Dump(C: nanoocp.Geom.Geom_Curve | None) -> str: ...

    @overload
    @staticmethod
    def Dump(C: nanoocp.Geom2d.Geom2d_Curve | None) -> str:
        """Dumps the Curve on the stream."""

    @overload
    @staticmethod
    def Write(S: nanoocp.Geom.Geom_Surface | None) -> str:
        """Writes the surface on the stream."""

    @overload
    @staticmethod
    def Write(C: nanoocp.Geom.Geom_Curve | None) -> str: ...

    @overload
    @staticmethod
    def Write(C: nanoocp.Geom2d.Geom2d_Curve | None) -> str:
        """Writes the Curve on the stream."""

    @staticmethod
    def Read__Geom_Surface(IS: TextIO) -> nanoocp.Geom.Geom_Surface:
        """
        Read__Geom_Surface: the C++ overload Read(occ::handle<Geom_Surface> &, Standard_IStream &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Reads the surface from the stream.
        """

    @staticmethod
    def Read__Geom_Curve(IS: TextIO) -> nanoocp.Geom.Geom_Curve:
        """
        Read__Geom_Curve: the C++ overload Read(occ::handle<Geom_Curve> &, Standard_IStream &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Reads the Curve from the stream.
        """

    @staticmethod
    def Read__Geom2d_Curve(IS: TextIO) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Read__Geom2d_Curve: the C++ overload Read(occ::handle<Geom2d_Curve> &, Standard_IStream &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Reads the Curve from the stream.
        """

    @staticmethod
    def SetUndefinedTypeHandler(aHandler: GeomTools_UndefinedTypeHandler | None) -> None: ...

    @staticmethod
    def GetUndefinedTypeHandler() -> GeomTools_UndefinedTypeHandler: ...

    @staticmethod
    def GetReal(IS: TextIO) -> float:
        """
        Reads the double value from the stream. Zero is read
        in case of error
        """

class GeomTools_Curve2dSet:
    """Stores a set of Curves from Geom2d."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Curves."""

    @overload
    def __init__(self, theOther: GeomTools_Curve2dSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> int:
        """
        Incorporate a new Curve in the set and returns
        its index.
        """

    def Curve2d(self, I: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns the Curve of index <I>."""

    def Index(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> int:
        """Returns the index of <L>."""

    def Dump(self) -> str:
        """Dumps the content of me on the stream <OS>."""

    def Write(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>.
        me is first cleared.
        """

    @staticmethod
    def PrintCurve2d(C: nanoocp.Geom2d.Geom2d_Curve | None, compact: bool = False) -> str:
        """
        Dumps the curve on the stream, if compact is True
        use the compact format that can be read back.
        """

    @staticmethod
    def ReadCurve2d(IS: TextIO) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Reads the curve from the stream. The curve is
        assumed to have been written with the Print
        method (compact = True).
        """

class GeomTools_CurveSet:
    """Stores a set of Curves from Geom."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Curves."""

    @overload
    def __init__(self, theOther: GeomTools_CurveSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, C: nanoocp.Geom.Geom_Curve | None) -> int:
        """
        Incorporate a new Curve in the set and returns
        its index.
        """

    def Curve(self, I: int) -> nanoocp.Geom.Geom_Curve:
        """Returns the Curve of index <I>."""

    def Index(self, C: nanoocp.Geom.Geom_Curve | None) -> int:
        """Returns the index of <L>."""

    def Dump(self) -> str:
        """Dumps the content of me on the stream <OS>."""

    def Write(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>
        me is first cleared.
        """

    @staticmethod
    def PrintCurve(C: nanoocp.Geom.Geom_Curve | None, compact: bool = False) -> str:
        """
        Dumps the curve on the stream, if compact is True
        use the compact format that can be read back.
        """

    @staticmethod
    def ReadCurve(IS: TextIO) -> nanoocp.Geom.Geom_Curve:
        """
        Reads the curve from the stream. The curve is
        assumed to have been written with the Print
        method (compact = True).
        """

class GeomTools_SurfaceSet:
    """Stores a set of Surfaces from Geom."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Surfaces."""

    @overload
    def __init__(self, theOther: GeomTools_SurfaceSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, S: nanoocp.Geom.Geom_Surface | None) -> int:
        """
        Incorporate a new Surface in the set and returns
        its index.
        """

    def Surface(self, I: int) -> nanoocp.Geom.Geom_Surface:
        """Returns the Surface of index <I>."""

    def Index(self, S: nanoocp.Geom.Geom_Surface | None) -> int:
        """Returns the index of <L>."""

    def Dump(self) -> str:
        """Dumps the content of me on the stream <OS>."""

    def Write(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>.
        me is first cleared.
        """

    @staticmethod
    def PrintSurface(S: nanoocp.Geom.Geom_Surface | None, compact: bool = False) -> str:
        """
        Dumps the surface on the stream, if compact is True
        use the compact format that can be read back.
        """

    @staticmethod
    def ReadSurface(IS: TextIO) -> nanoocp.Geom.Geom_Surface:
        """
        Reads the surface from the stream. The surface is
        assumed to have been written with the Print
        method (compact = True).
        """

class GeomTools_UndefinedTypeHandler(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomTools_UndefinedTypeHandler) -> None: ...

    def PrintCurve(self, C: nanoocp.Geom.Geom_Curve | None, compact: bool = False) -> str: ...

    def ReadCurve(self, ctype: int, IS: TextIO) -> nanoocp.Geom.Geom_Curve: ...

    def PrintCurve2d(self, C: nanoocp.Geom2d.Geom2d_Curve | None, compact: bool = False) -> str: ...

    def ReadCurve2d(self, ctype: int, IS: TextIO) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def PrintSurface(self, S: nanoocp.Geom.Geom_Surface | None, compact: bool = False) -> str: ...

    def ReadSurface(self, ctype: int, IS: TextIO) -> nanoocp.Geom.Geom_Surface: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
