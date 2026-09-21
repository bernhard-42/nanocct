"""OCCT package BinTools (toolkit TKBRep)"""

import enum
from typing import BinaryIO, overload

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

BinTools_FormatVersion_VERSION_1: BinTools_FormatVersion = ...

BinTools_FormatVersion_VERSION_2: BinTools_FormatVersion = ...

BinTools_FormatVersion_VERSION_3: BinTools_FormatVersion = ...

BinTools_FormatVersion_VERSION_4: BinTools_FormatVersion = ...

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

BinTools_ObjectType_Unknown: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_Unknown

BinTools_ObjectType_Reference8: BinTools_ObjectType = ...

BinTools_ObjectType_Reference16: BinTools_ObjectType = ...

BinTools_ObjectType_Reference32: BinTools_ObjectType = ...

BinTools_ObjectType_Reference64: BinTools_ObjectType = ...

BinTools_ObjectType_Location: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_Location

BinTools_ObjectType_SimpleLocation: BinTools_ObjectType = ...

BinTools_ObjectType_EmptyLocation: BinTools_ObjectType = ...

BinTools_ObjectType_LocationEnd: BinTools_ObjectType = ...

BinTools_ObjectType_Curve: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_Curve

BinTools_ObjectType_EmptyCurve: BinTools_ObjectType = ...

BinTools_ObjectType_Curve2d: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_Curve2d

BinTools_ObjectType_EmptyCurve2d: BinTools_ObjectType = ...

BinTools_ObjectType_Surface: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_Surface

BinTools_ObjectType_EmptySurface: BinTools_ObjectType = ...

BinTools_ObjectType_Polygon3d: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_Polygon3d

BinTools_ObjectType_EmptyPolygon3d: BinTools_ObjectType = ...

BinTools_ObjectType_PolygonOnTriangulation: BinTools_ObjectType = ...

BinTools_ObjectType_EmptyPolygonOnTriangulation: BinTools_ObjectType = ...

BinTools_ObjectType_Triangulation: BinTools_ObjectType = ...

BinTools_ObjectType_EmptyTriangulation: BinTools_ObjectType = ...

BinTools_ObjectType_EmptyShape: BinTools_ObjectType = ...

BinTools_ObjectType_EndShape: BinTools_ObjectType = BinTools_ObjectType.BinTools_ObjectType_EndShape

class BinTools:
    """Tool to keep shapes in binary format"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinTools) -> None: ...

    @staticmethod
    def PutReal(theValue: float) -> bytes: ...

    @staticmethod
    def PutShortReal(theValue: float) -> bytes: ...

    @staticmethod
    def PutInteger(theValue: int) -> bytes: ...

    @staticmethod
    def PutBool(theValue: bool) -> bytes: ...

    @staticmethod
    def PutExtChar(theValue: str) -> bytes: ...

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the shape to the stream in binary format BinTools_FormatVersion_CURRENT.
        This alias writes shape with triangulation data.
        @param[in] theShape        the shape to write
        @param[in][out] theStream  the stream to output shape into
        @param theRange            the range of progress indicator to fill in
        """

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theWithTriangles: bool, theWithNormals: bool, theVersion: BinTools_FormatVersion, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the shape to the stream in binary format of specified version.
        @param[in] theShape          the shape to write
        @param[in][out] theStream    the stream to output shape into
        @param[in] theWithTriangles  flag which specifies whether to save shape with (TRUE) or without
        (FALSE) triangles;
        has no effect on triangulation-only geometry
        @param[in] theWithNormals    flag which specifies whether to save triangulation with (TRUE) or
        without (FALSE) normals;
        has no effect on triangulation-only geometry
        @param[in] theVersion        the BinTools format version
        @param theRange              the range of progress indicator to fill in
        """

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

    @overload
    @staticmethod
    def Read(theShape: nanoocp.TopoDS.TopoDS_Shape, theStream: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Reads a shape from <theStream> and returns it in <theShape>."""

    @overload
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

    def Add(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> int:
        """
        Incorporate a new Curve in the set and returns
        its index.
        """

    def Curve2d(self, I: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns the Curve of index <I>."""

    def Index(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> int:
        """Returns the index of <L>."""

    def Write(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>. me
        is first cleared.
        """

    @staticmethod
    def WriteCurve2d(C: nanoocp.Geom2d.Geom2d_Curve | None, OS: BinTools_OStream) -> None:
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

    def Add(self, C: nanoocp.Geom.Geom_Curve | None) -> int:
        """
        Incorporate a new Curve in the set and returns
        its index.
        """

    def Curve(self, I: int) -> nanoocp.Geom.Geom_Curve:
        """Returns the Curve of index <I>."""

    def Index(self, C: nanoocp.Geom.Geom_Curve | None) -> int:
        """Returns the index of <L>."""

    def Write(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>. me
        is first cleared.
        """

    @staticmethod
    def WriteCurve(C: nanoocp.Geom.Geom_Curve | None, OS: BinTools_OStream) -> None:
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

    def ReadBools__bool__bool__bool(self) -> tuple[bool, bool, bool]:
        """
        ReadBools__bool__bool__bool: the C++ overload ReadBools(bool &, bool &, bool &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Reads 3 boolean values from one byte
        """

    def ReadBools__bool__bool__bool__bool__bool__bool__bool(self) -> tuple[bool, bool, bool, bool, bool, bool, bool]:
        """
        ReadBools__bool__bool__bool__bool__bool__bool__bool: the C++ overload ReadBools(bool &, bool &, bool &, bool &, bool &, bool &, bool &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Reads 7 boolean values from one byte
        """

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

    def Write(self) -> bytes:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: BinaryIO) -> None:
        """
        Reads the content of me from the stream <IS>. me
        is first cleared.
        """

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

    @overload
    def Write(self, arg1: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the content of me on the stream <OS> in binary
        format that can be read back by Read.

        Writes the locations.

        Writes the geometry calling WriteGeometry.

        Dumps the shapes from last to first.
        For each shape:
        Write the type.
        calls WriteGeometry(S).
        Write the flags, the subshapes.
        """

    @overload
    def Write(self, arg0: nanoocp.TopoDS.TopoDS_Shape) -> bytes:
        """
        Writes on <OS> the shape <S>. Writes the
        orientation, the index of the TShape and the index
        of the Location.
        """

    @overload
    def Read(self, arg0: BinaryIO, arg1: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the binary stream <IS>. me
        is first cleared.

        Reads the locations.

        Reads the geometry calling ReadGeometry.

        Reads the shapes.
        For each shape
        Reads the type.
        calls ReadGeometry(T,S).
        Reads the flag, the subshapes.
        """

    @overload
    def Read(self, arg0: BinaryIO, arg1: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """An empty virtual method for redefinition in shape-reader."""

class BinTools_SurfaceSet:
    """Stores a set of Surfaces from Geom in binary format."""

    @overload
    def __init__(self) -> None:
        """Returns an empty set of Surfaces."""

    @overload
    def __init__(self, theOther: BinTools_SurfaceSet) -> None: ...

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

    def Write(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the content of me on the stream <OS> in
        binary format that can be read back by Read.
        """

    def Read(self, IS: BinaryIO, therange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>. me
        is first cleared.
        """

    @staticmethod
    def WriteSurface(S: nanoocp.Geom.Geom_Surface | None, OS: BinTools_OStream) -> None:
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

    @overload
    def Write(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the content of me on the stream <OS> in binary
        format that can be read back by Read.

        Writes the locations.

        Writes the geometry calling WriteGeometry.

        Dumps the shapes from last to first.
        For each shape:
        Write the type.
        calls WriteGeometry(S).
        Write the flags, the subshapes.
        """

    @overload
    def Write(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bytes:
        """
        Writes on <OS> the shape <S>. Writes the
        orientation, the index of the TShape and the index
        of the Location.
        """

    @overload
    def Read(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the binary stream <IS>. me
        is first cleared.

        Reads the locations.

        Reads the geometry calling ReadGeometry.

        Reads the shapes.
        For each shape
        Reads the type.
        calls ReadGeometry(T,S).
        Reads the flag, the subshapes.
        """

    @overload
    def Read(self, arg0: BinaryIO, arg1: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """An empty virtual method for redefinition in shape-reader."""

    def WriteGeometry(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the geometry of me on the stream <OS> in a
        binary format that can be read back by Read.
        """

    def ReadGeometry(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Reads the geometry of me from the stream <IS>."""

    def ReadFlagsAndSubs(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum, IS: BinaryIO, NbShapes: int) -> None:
        """Reads from <IS> a shape flags and sub-shapes and modifies S."""

    def ReadSubs(self, S: nanoocp.TopoDS.TopoDS_Shape, IS: BinaryIO, NbShapes: int) -> None:
        """
        Reads from <IS> a shape and returns it in S.
        <NbShapes> is the number of tshapes in the set.
        """

    def WriteShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bytes:
        """
        Writes the shape <S> on the stream <OS> in a
        binary format that can be read back by Read.
        """

    def ReadShape(self, T: nanoocp.TopAbs.TopAbs_ShapeEnum, IS: BinaryIO, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Reads a shape of type <T> from the stream <IS> and returns it in <S>."""

    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Stores the shape <S>."""

    def AddShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Inserts the shape <S2> in the shape <S1>."""

    def ReadPolygon3D(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the 3d polygons of me
        from the stream <IS>.
        """

    def WritePolygon3D(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the 3d polygons
        on the stream <OS> in a format that can
        be read back by Read.
        """

    def ReadTriangulation(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the triangulation of me
        from the stream <IS>.
        """

    def WriteTriangulation(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the triangulation
        on the stream <OS> in a format that can
        be read back by Read.
        """

    def ReadPolygonOnTriangulation(self, IS: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the polygons on triangulation of me
        from the stream <IS>.
        """

    def WritePolygonOnTriangulation(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """
        Writes the polygons on triangulation
        on the stream <OS> in a format that can
        be read back by Read.
        """

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

    def Read(self, theStream: BinaryIO, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Reads the shape from stream using previously restored shapes and objects by references.
        """

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

    def Write(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bytes:
        """
        Writes the shape to stream using previously stored shapes and objects to refer them.
        """

    def WriteLocation(self, theStream: BinTools_OStream, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Writes location to the stream (all the needed sub-information or reference if it is already
        used).
        """
