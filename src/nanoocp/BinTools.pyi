"""OCCT package BinTools (toolkit TKBRep)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Message
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class BinTools_FormatVersion(enum.IntEnum):
    """Defined BinTools format version"""

    BinTools_FormatVersion_VERSION_1 = 1

    BinTools_FormatVersion_VERSION_2 = 2

    BinTools_FormatVersion_VERSION_3 = 3

    BinTools_FormatVersion_VERSION_4 = 4

    BinTools_FormatVersion_CURRENT = 4

BinTools_FormatVersion_LOWER: int = 1

BinTools_FormatVersion_UPPER: int = 4

class BinTools_ObjectType(enum.IntEnum):
    """
    Enumeration defining objects identifiers in the shape read/write format.
    """

    BinTools_ObjectType_Unknown = 0

    BinTools_ObjectType_Reference8 = 1

    BinTools_ObjectType_Reference16 = 2

    BinTools_ObjectType_Reference32 = 3

    BinTools_ObjectType_Reference64 = 4

    BinTools_ObjectType_Location = 5

    BinTools_ObjectType_SimpleLocation = 6

    BinTools_ObjectType_EmptyLocation = 7

    BinTools_ObjectType_LocationEnd = 8

    BinTools_ObjectType_Curve = 9

    BinTools_ObjectType_EmptyCurve = 10

    BinTools_ObjectType_Curve2d = 11

    BinTools_ObjectType_EmptyCurve2d = 12

    BinTools_ObjectType_Surface = 13

    BinTools_ObjectType_EmptySurface = 14

    BinTools_ObjectType_Polygon3d = 15

    BinTools_ObjectType_EmptyPolygon3d = 16

    BinTools_ObjectType_PolygonOnTriangulation = 17

    BinTools_ObjectType_EmptyPolygonOnTriangulation = 18

    BinTools_ObjectType_Triangulation = 19

    BinTools_ObjectType_EmptyTriangulation = 20

    BinTools_ObjectType_EmptyShape = 198

    BinTools_ObjectType_EndShape = 199

class BinTools:
    """Tool to keep shapes in binary format"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinTools) -> None: ...

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theFile: str, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes the shape to the file in binary format BinTools_FormatVersion_CURRENT.
        @param[in] theShape  the shape to write
        @param[in] theFile   the path to file to output shape into
        @param theRange      the range of progress indicator to fill in
        """

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theFile: str, theWithTriangles: bool, theWithNormals: bool, theVersion: BinTools_FormatVersion, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes the shape to the file in binary format of specified version.
        @param[in] theShape          the shape to write
        @param[in] theFile           the path to file to output shape into
        @param[in] theWithTriangles  flag which specifies whether to save shape with (TRUE) or without
        (FALSE) triangles;
        has no effect on triangulation-only geometry
        @param[in] theWithNormals    flag which specifies whether to save triangulation with (TRUE) or
        without (FALSE) normals;
        has no effect on triangulation-only geometry
        @param[in] theVersion        the BinTools format version
        @param theRange              the range of progress indicator to fill in
        """

    @staticmethod
    def Read(theShape: nanoocp.TopoDS.TopoDS_Shape, theFile: str, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """Reads a shape from <theFile> and returns it in <theShape>."""

class BinTools_OStream:
    """
    Substitution of OStream for shape writer for fast management of position in the file
    and operation on all writing types.
    """

    def __init__(self, theOther: BinTools_OStream) -> None: ...

    def Position(self) -> int:
        """Returns the current position of the stream"""

    def WriteReference(self, thePosition: int) -> None:
        """
        Writes the reference to the given position (an offset between the current and the given one).
        """

    def WriteShape(self, theType: nanoocp.TopAbs.TopAbs_ShapeEnum, theOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Writes an identifier of shape type and orientation into the stream."""

    @overload
    def PutBools(self, theValue1: bool, theValue2: bool, theValue3: bool) -> None:
        """Writes 3 booleans as one byte to the stream."""

    @overload
    def PutBools(self, theValue1: bool, theValue2: bool, theValue3: bool, theValue4: bool, theValue5: bool, theValue6: bool, theValue7: bool) -> None:
        """Writes 7 booleans as one byte to the stream."""

class BinTools_Curve2dSet:
    """Stores a set of Curves from Geom2d in binary format"""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Curves."""

    @overload
    def __init__(self, theOther: BinTools_Curve2dSet) -> None: ...

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

    @staticmethod
    def WriteCurve2d(C: nanoocp.Geom2d.Geom2d_Curve, OS: BinTools_OStream) -> None:
        """Dumps the curve on the binary stream, that can be read back."""

class BinTools_CurveSet:
    """Stores a set of Curves from Geom in binary format."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Curves."""

    @overload
    def __init__(self, theOther: BinTools_CurveSet) -> None: ...

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

    @staticmethod
    def WriteCurve(C: nanoocp.Geom.Geom_Curve, OS: BinTools_OStream) -> None:
        """
        Dumps the curve on the stream in binary format
        that can be read back.
        """

class BinTools_IStream:
    """
    Substitution of IStream for shape reader for fast management of position in the file (get and
    go) and operation on all reading types.
    """

    def __init__(self, theOther: BinTools_IStream) -> None: ...

    def ReadType(self) -> BinTools_ObjectType:
        """Reads and returns the type."""

    def LastType(self) -> BinTools_ObjectType:
        """Returns the last read type."""

    def ShapeType(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Returns the shape type by the last retrieved type."""

    def ShapeOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the shape orientation by the last retrieved type."""

    def Position(self) -> int:
        """Returns the current position in the stream."""

    def GoTo(self, thePosition: int) -> None:
        """Moves the current stream position to the given one."""

    def IsReference(self) -> bool:
        """Returns true if the last restored type is one of a reference"""

    def ReadReference(self) -> int:
        """Reads a reference IStream using the last restored type."""

    def UpdatePosition(self) -> None:
        """
        Makes up to date the myPosition because myStream was used outside and position is changed.
        """

    def ReadReal(self) -> float:
        """Reads real value from the stream."""

    def ReadInteger(self) -> int:
        """Reads integer value from the stream."""

    def ReadPnt(self) -> nanoocp.gp.gp_Pnt:
        """Reads point coordinates value from the stream."""

    def ReadByte(self) -> int:
        """Reads byte value from the stream."""

    def ReadBool(self) -> bool:
        """Reads boolean value from the stream (stored as one byte)."""

    def ReadShortReal(self) -> float:
        """Reads short real value from the stream."""

    @overload
    def ReadBools(self) -> tuple[bool, bool, bool, bool, bool, bool, bool]:
        """Reads 7 boolean values from one byte"""

    @overload
    def ReadBools(self) -> tuple[bool, bool, bool]:
        """Reads 3 boolean values from one byte"""

    def __bool__(self) -> bool:
        """Returns false if stream reading is failed."""

class BinTools_LocationSet:
    """
    The class LocationSet stores a set of location in
    a relocatable state.

    It can be created from Locations.

    It can create Locations.
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty set of locations."""

    @overload
    def __init__(self, theOther: BinTools_LocationSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, L: nanoocp.TopLoc.TopLoc_Location) -> int:
        """
        Incorporate a new Location in the set and returns
        its index.
        """

    def Location(self, I: int) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns the location of index <I>."""

    def Index(self, L: nanoocp.TopLoc.TopLoc_Location) -> int:
        """Returns the index of <L>."""

    def NbLocations(self) -> int:
        """Returns number of locations."""

class BinTools_ShapeSetBase:
    """A base class for all readers/writers of TopoDS_Shape into/from stream."""

    @overload
    def __init__(self) -> None:
        """A default constructor."""

    @overload
    def __init__(self, theOther: BinTools_ShapeSetBase) -> None: ...

    def IsWithTriangles(self) -> bool:
        """Return true if shape should be stored with triangles."""

    def IsWithNormals(self) -> bool:
        """Return true if shape should be stored triangulation with normals."""

    def SetWithTriangles(self, theWithTriangles: bool) -> None:
        """
        Define if shape will be stored with triangles.
        Ignored (always written) if face defines only triangulation (no surface).
        """

    def SetWithNormals(self, theWithNormals: bool) -> None:
        """
        Define if shape will be stored triangulation with normals.
        Ignored (always written) if face defines only triangulation (no surface).
        """

    def SetFormatNb(self, theFormatNb: int) -> None:
        """Sets the BinTools_FormatVersion."""

    def FormatNb(self) -> int:
        """Returns the BinTools_FormatVersion."""

    def Clear(self) -> None:
        """Clears the content of the set."""

class BinTools_SurfaceSet:
    """Stores a set of Surfaces from Geom in binary format."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Surfaces."""

    @overload
    def __init__(self, theOther: BinTools_SurfaceSet) -> None: ...

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

    @staticmethod
    def WriteSurface(S: nanoocp.Geom.Geom_Surface, OS: BinTools_OStream) -> None:
        """
        Dumps the surface on the stream in binary
        format that can be read back.
        """

class BinTools_ShapeSet(BinTools_ShapeSetBase):
    """Writes topology in OStream in binary format"""

    @overload
    def __init__(self) -> None:
        """
        Builds an empty ShapeSet.
        @param[in] theWithTriangles  flag to write triangulation data
        """

    @overload
    def __init__(self, theOther: BinTools_ShapeSet) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Stores <S> and its sub-shape. Returns the index of <S>.
        The method AddGeometry is called on each sub-shape.
        """

    def Shape(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the sub-shape of index <I>."""

    def Index(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """Returns the index of <S>."""

    def Locations(self) -> BinTools_LocationSet: ...

    def ChangeLocations(self) -> BinTools_LocationSet: ...

    def NbShapes(self) -> int:
        """Returns number of shapes read from file."""

    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Stores the shape <S>."""

    def AddShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Inserts the shape <S2> in the shape <S1>."""

class BinTools_ShapeReader(BinTools_ShapeSetBase):
    """
    Reads topology from IStream in binary format without grouping of objects by types
    and using relative positions in a file as references.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a shape reader."""

    @overload
    def __init__(self, theOther: BinTools_ShapeReader) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def ReadLocation(self, theStream: BinTools_IStream) -> nanoocp.TopLoc.TopLoc_Location:
        """Reads location from the stream."""

class BinTools_ShapeWriter(BinTools_ShapeSetBase):
    """
    Writes topology in OStream in binary format without grouping of objects by types
    and using relative positions in a file as references.
    """

    @overload
    def __init__(self) -> None:
        """
        Builds an empty ShapeSet.
        Parameter <theWithTriangles> is added for XML Persistence
        """

    @overload
    def __init__(self, theOther: BinTools_ShapeWriter) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the set."""

    def WriteLocation(self, theStream: BinTools_OStream, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Writes location to the stream (all the needed sub-information or reference if it is already
        used).
        """
