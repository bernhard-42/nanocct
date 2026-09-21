"""OCCT package TopTools (toolkit TKBRep)"""

import enum
from typing import TextIO, overload

import nanoocp.Message
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS


class TopTools_FormatVersion(enum.IntEnum):
    """Defined TopTools format version"""

    TopTools_FormatVersion_VERSION_1 = 1

    TopTools_FormatVersion_VERSION_2 = 2

    TopTools_FormatVersion_VERSION_3 = 3

    TopTools_FormatVersion_CURRENT = 3

TopTools_FormatVersion_VERSION_1: TopTools_FormatVersion = ...

TopTools_FormatVersion_VERSION_2: TopTools_FormatVersion = ...

TopTools_FormatVersion_VERSION_3: TopTools_FormatVersion = ...

TopTools_FormatVersion_LOWER: int = 1

TopTools_FormatVersion_UPPER: int = 3

class TopTools:
    """
    The TopTools package provides utilities for the
    topological data structure.

    * ShapeMapHasher. Hash a Shape base on the TShape
    and the Location. The Orientation is not used.

    * OrientedShapeMapHasher. Hash a Shape base on the
    TShape ,the Location and the Orientation.

    * Instantiations of TCollection for Shapes :
    MapOfShape
    IndexedMapOfShape
    DataMapOfIntegerShape
    DataMapOfShapeInteger
    DataMapOfShapeReal
    Array1OfShape
    HArray1OfShape
    SequenceOfShape
    HSequenceOfShape
    ListOfShape
    Array1OfListShape
    HArray1OfListShape
    DataMapOfIntegerListOfShape
    DataMapOfShapeListOfShape
    DataMapOfShapeListOfInteger
    IndexedDataMapOfShapeShape
    IndexedDataMapOfShapeListOfShape
    DataMapOfShapeShape
    IndexedMapOfOrientedShape
    DataMapOfShapeSequenceOfShape
    IndexedDataMapOfShapeAddress
    DataMapOfOrientedShapeShape

    * LocationSet: to write sets of locations.

    * ShapeSet: to writes sets of TShapes.

    Package Methods:

    Dump: To dump the topology of a Shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopTools) -> None: ...

    @staticmethod
    def Dump(Sh: nanoocp.TopoDS.TopoDS_Shape) -> object:
        """
        A set of Shapes. Can be dump, wrote or read.
        Dumps the topological structure of <Sh> on the
        stream <S>.
        """

    @staticmethod
    def Dummy(I: int) -> None:
        """
        This is to bypass an extraction bug. It will force
        the inclusion of int.hxx itself
        including Standard_OStream.hxx at the correct
        position.
        """

class TopTools_LocationSet:
    """
    The class LocationSet stores a set of location in
    a relocatable state.

    It can be created from Locations.

    It can create Locations.

    It can be write and read from a stream.
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty set of locations."""

    @overload
    def __init__(self, theOther: TopTools_LocationSet) -> None: ...

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

    def Dump(self) -> object:
        """Dumps the content of me on the stream <OS>."""

    def Write(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> object:
        """
        Writes the content of me on the stream <OS> in a
        format that can be read back by Read.
        """

    def Read(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>. me
        is first cleared.
        """

class TopTools_ShapeMapHasher:
    """Hash tool, used for generating maps of shapes in topology."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopTools_ShapeMapHasher) -> None: ...

    @overload
    def __call__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def __call__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

class TopTools_ShapeSet:
    """
    A ShapeSets contains a Shape and all its
    sub-shapes and locations. It can be dump, write
    and read.

    Methods to handle the geometry can be redefined.
    """

    @overload
    def __init__(self) -> None:
        """Builds an empty ShapeSet."""

    @overload
    def __init__(self, theOther: TopTools_ShapeSet) -> None: ...

    def SetFormatNb(self, theFormatNb: int) -> None:
        """Sets the TopTools_FormatVersion"""

    def FormatNb(self) -> int:
        """Returns the TopTools_FormatVersion"""

    def Clear(self) -> None:
        """
        Clears the content of the set. This method can be
        redefined.
        """

    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Stores <S> and its sub-shape. Returns the index of <S>.
        The method AddGeometry is called on each sub-shape.
        """

    def Shape(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the sub-shape of index <I>."""

    def Index(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """Returns the index of <S>."""

    def Locations(self) -> TopTools_LocationSet: ...

    def ChangeLocations(self) -> TopTools_LocationSet: ...

    @overload
    def DumpExtent(self) -> object:
        """
        Dumps the number of objects in me on the stream <OS>.
        (Number of shapes of each type)
        """

    @overload
    def DumpExtent(self, S: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Dumps the number of objects in me in the string S
        (Number of shapes of each type)
        """

    @overload
    def Dump(self) -> object:
        """
        Dumps the content of me on the stream <OS>.

        Dumps the shapes from first to last.
        For each Shape
        Dump the type, the flags, the subshapes
        calls DumpGeometry(S)

        Dumps the geometry calling DumpGeometry.

        Dumps the locations.
        """

    @overload
    def Dump(self, S: nanoocp.TopoDS.TopoDS_Shape) -> object:
        """
        Dumps on <OS> the shape <S>. Dumps the
        orientation, the index of the TShape and the index
        of the Location.
        """

    @overload
    def Write(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> object:
        """
        Writes the content of me on the stream <OS> in a
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
    def Write(self, S: nanoocp.TopoDS.TopoDS_Shape) -> object:
        """
        Writes on <OS> the shape <S>. Writes the
        orientation, the index of the TShape and the index
        of the Location.
        """

    @overload
    def Read(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the content of me from the stream <IS>. me
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
    def Read(self, S: nanoocp.TopoDS.TopoDS_Shape, IS: TextIO) -> None:
        """Reads from <IS> a shape and returns it in S."""

    def AddGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Stores the geometry of <S>."""

    @overload
    def DumpGeometry(self) -> object:
        """Dumps the geometry of me on the stream <OS>."""

    @overload
    def DumpGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> object:
        """Dumps the geometry of <S> on the stream <OS>."""

    @overload
    def WriteGeometry(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> object:
        """
        Writes the geometry of me on the stream <OS> in a
        format that can be read back by Read.
        """

    @overload
    def WriteGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> object:
        """
        Writes the geometry of <S> on the stream <OS> in a
        format that can be read back by Read.
        """

    @overload
    def ReadGeometry(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Reads the geometry of me from the stream <IS>."""

    @overload
    def ReadGeometry(self, T: nanoocp.TopAbs.TopAbs_ShapeEnum, IS: TextIO, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Reads the geometry of a shape of type <T> from the
        stream <IS> and returns it in <S>.
        """

    def AddShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Inserts the shape <S2> in the shape <S1>. This
        method must be redefined to use the correct
        builder.
        """

    def Check(self, T: nanoocp.TopAbs.TopAbs_ShapeEnum, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        This method is called after each new completed
        shape. <T> is the type. <S> is the shape. In this
        class it does nothing, but it gives the opportunity
        in derived classes to perform extra treatment on
        shapes.
        """

    def NbShapes(self) -> int:
        """Returns number of shapes read from file."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Bnd
import nanoocp.TopTools
TopTools_Array1OfShape = nanoocp.NCollection.NCollection_Array1[nanoocp.TopoDS.TopoDS_Shape]
TopTools_Array2OfShape = nanoocp.NCollection.NCollection_Array2[nanoocp.TopoDS.TopoDS_Shape]
TopTools_DataMapOfShapeBox = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Bnd.Bnd_Box, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_DataMapOfShapeInteger = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_DataMapOfShapeListOfShape = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_DataMapOfShapeShape = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_HArray1OfShape = nanoocp.NCollection.NCollection_HArray1[nanoocp.TopoDS.TopoDS_Shape]
TopTools_HArray2OfShape = nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape]
TopTools_HSequenceOfShape = nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]
TopTools_IndexedDataMapOfShapeListOfShape = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_IndexedDataMapOfShapeReal = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, float, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_IndexedDataMapOfShapeShape = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_IndexedMapOfShape = nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_ListOfListOfShape = nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]]
TopTools_ListOfShape = nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]
TopTools_MapOfShape = nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopTools_SequenceOfShape = nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]
