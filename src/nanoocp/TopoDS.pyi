"""OCCT package TopoDS (toolkit TKBRep)"""

import enum
from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc


class TopoDS_TShape(nanoocp.Standard.Standard_Transient):
    """
    A TShape is a topological structure describing a
    set of points in a 2D or 3D space.

    A topological shape is a structure made from other
    shapes. This is a deferred class used to support
    topological objects.

    TShapes are defined by their optional domain
    (geometry) and their components (other TShapes
    with Locations and Orientations). The components
    are stored in a list in the base class.

    A TShape contains the following boolean flags:

    - Free       : Free or Frozen.
    - Modified   : Has been modified.
    - Checked    : Has been checked.
    - Orientable : Can be oriented.
    - Closed     : Is closed (note that only Wires and Shells may be closed).
    - Infinite   : Is infinite.
    - Convex     : Is convex.
    - Locked     : Is locked against modifications.

    Users have no direct access to the classes derived
    from TShape. They handle them with the classes
    derived from Shape.
    """

    class BitLayout(enum.IntEnum):
        """
        Bit layout for compact state storage.
        Bits 0-3 store the TopAbs_ShapeEnum value (0-8).
        Bits 4-11 store boolean flags.
        Bits 12-15 are reserved for future use.
        """

        Bits_ShapeType_Mask = 15

        Bits_ShapeType_Shift = 0

        Bit_Free = 16

        Bit_Modified = 32

        Bit_Checked = 64

        Bit_Orientable = 128

        Bit_Closed = 256

        Bit_Infinite = 512

        Bit_Convex = 1024

        Bit_Locked = 2048

        Bits_Reserved = 61440

    @overload
    def Free(self) -> bool:
        """Returns the free flag."""

    @overload
    def Free(self, theIsFree: bool) -> None:
        """Sets the free flag."""

    @overload
    def Locked(self) -> bool:
        """Returns the locked flag."""

    @overload
    def Locked(self, theIsLocked: bool) -> None:
        """Sets the locked flag."""

    @overload
    def Modified(self) -> bool:
        """Returns the modification flag."""

    @overload
    def Modified(self, theIsModified: bool) -> None:
        """Sets the modification flag."""

    @overload
    def Checked(self) -> bool:
        """Returns the checked flag."""

    @overload
    def Checked(self, theIsChecked: bool) -> None:
        """Sets the checked flag."""

    @overload
    def Orientable(self) -> bool:
        """Returns the orientability flag."""

    @overload
    def Orientable(self, theIsOrientable: bool) -> None:
        """Sets the orientability flag."""

    @overload
    def Closed(self) -> bool:
        """Returns the closedness flag."""

    @overload
    def Closed(self, theIsClosed: bool) -> None:
        """Sets the closedness flag."""

    @overload
    def Infinite(self) -> bool:
        """Returns the infinity flag."""

    @overload
    def Infinite(self, theIsInfinite: bool) -> None:
        """Sets the infinity flag."""

    @overload
    def Convex(self) -> bool:
        """Returns the convexness flag."""

    @overload
    def Convex(self, theIsConvex: bool) -> None:
        """Sets the convexness flag."""

    def ShapeType(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        Returns the type as a term of the ShapeEnum enum:
        VERTEX, EDGE, WIRE, FACE, SHELL, SOLID, COMPSOLID, COMPOUND.
        The type is embedded in the lower 4 bits of the state.
        """

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns a copy of the TShape with no sub-shapes."""

    def NbChildren(self) -> int:
        """
        Returns the number of direct sub-shapes (children).
        @sa TopoDS_Iterator for accessing sub-shapes
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_Shape:
    """
    Describes a shape which
    - references an underlying shape with the potential
    to be given a location and an orientation
    - has a location for the underlying shape, giving its
    placement in the local coordinate system
    - has an orientation for the underlying shape, in
    terms of its geometry (as opposed to orientation in
    relation to other shapes).
    Note: A Shape is empty if it references an underlying
    shape which has an empty list of shapes.
    """

    @overload
    def __init__(self) -> None:
        """Creates a NULL Shape referring to nothing."""

    @overload
    def __init__(self, theOther: TopoDS_Shape) -> None: ...

    def IsNull(self) -> bool:
        """
        Returns true if this shape is null. In other words, it
        references no underlying shape with the potential to
        be given a location and an orientation.
        """

    def Nullify(self) -> None:
        """
        Destroys the reference to the underlying shape
        stored in this shape. As a result, this shape becomes null.
        """

    @overload
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns the shape local coordinate system."""

    @overload
    def Location(self, theLoc: nanoocp.TopLoc.TopLoc_Location, theRaiseExc: bool = False) -> None:
        """
        Sets the shape local coordinate system.
        @param theLoc the new local coordinate system.
        @param theRaiseExc flag to raise exception in case of transformation with scale or negative.
        """

    def Located(self, theLoc: nanoocp.TopLoc.TopLoc_Location, theRaiseExc: bool = False) -> TopoDS_Shape:
        """
        Returns a shape similar to <me> with the local
        coordinate system set to <Loc>.
        @param theLoc the new local coordinate system.
        @param theRaiseExc flag to raise exception in case of transformation with scale or negative.
        @return the located shape.
        """

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the shape orientation."""

    @overload
    def Orientation(self, theOrient: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Sets the shape orientation."""

    def Oriented(self, theOrient: nanoocp.TopAbs.TopAbs_Orientation) -> TopoDS_Shape:
        """
        Returns a shape similar to <me> with the
        orientation set to <Or>.
        """

    @overload
    def TShape(self) -> TopoDS_TShape:
        """Returns a handle to the actual shape implementation."""

    @overload
    def TShape(self, theTShape: TopoDS_TShape) -> None: ...

    def ShapeType(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        Returns the value of the TopAbs_ShapeEnum
        enumeration that corresponds to this shape, for
        example VERTEX, EDGE, and so on.
        Exceptions
        Standard_NullObject if this shape is null.
        """

    @overload
    def Free(self) -> bool:
        """Returns the free flag."""

    @overload
    def Free(self, theIsFree: bool) -> None:
        """Sets the free flag."""

    @overload
    def Locked(self) -> bool:
        """Returns the locked flag."""

    @overload
    def Locked(self, theIsLocked: bool) -> None:
        """Sets the locked flag."""

    @overload
    def Modified(self) -> bool:
        """Returns the modification flag."""

    @overload
    def Modified(self, theIsModified: bool) -> None:
        """Sets the modification flag."""

    @overload
    def Checked(self) -> bool:
        """Returns the checked flag."""

    @overload
    def Checked(self, theIsChecked: bool) -> None:
        """Sets the checked flag."""

    @overload
    def Orientable(self) -> bool:
        """Returns the orientability flag."""

    @overload
    def Orientable(self, theIsOrientable: bool) -> None:
        """Sets the orientability flag."""

    @overload
    def Closed(self) -> bool:
        """Returns the closedness flag."""

    @overload
    def Closed(self, theIsClosed: bool) -> None:
        """Sets the closedness flag."""

    @overload
    def Infinite(self) -> bool:
        """Returns the infinity flag."""

    @overload
    def Infinite(self, theIsInfinite: bool) -> None:
        """Sets the infinity flag."""

    @overload
    def Convex(self) -> bool:
        """Returns the convexness flag."""

    @overload
    def Convex(self, theIsConvex: bool) -> None:
        """Sets the convexness flag."""

    def Move(self, thePosition: nanoocp.TopLoc.TopLoc_Location, theRaiseExc: bool = False) -> None:
        """
        Multiplies the Shape location by thePosition.
        @param thePosition the transformation to apply.
        @param theRaiseExc flag to raise exception in case of transformation with scale or negative.
        """

    def Moved(self, thePosition: nanoocp.TopLoc.TopLoc_Location, theRaiseExc: bool = False) -> TopoDS_Shape:
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        @param thePosition the transformation to apply.
        @param theRaiseExc flag to raise exception in case of transformation with scale or negative.
        @return the moved shape.
        """

    def Reverse(self) -> None:
        """
        Reverses the orientation, using the Reverse method
        from the TopAbs package.
        """

    def Reversed(self) -> TopoDS_Shape:
        """
        Returns a shape similar to <me> with the
        orientation reversed, using the Reverse method
        from the TopAbs package.
        """

    def Complement(self) -> None:
        """
        Complements the orientation, using the Complement
        method from the TopAbs package.
        """

    def Complemented(self) -> TopoDS_Shape:
        """
        Returns a shape similar to <me> with the
        orientation complemented, using the Complement
        method from the TopAbs package.
        """

    def Compose(self, theOrient: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Updates the Shape Orientation by composition with theOrient,
        using the Compose method from the TopAbs package.
        """

    def Composed(self, theOrient: nanoocp.TopAbs.TopAbs_Orientation) -> TopoDS_Shape:
        """
        Returns a shape similar to <me> with the
        orientation composed with theOrient, using the
        Compose method from the TopAbs package.
        """

    def NbChildren(self) -> int:
        """
        Returns the number of direct sub-shapes (children).
        @sa TopoDS_Iterator for accessing sub-shapes
        """

    def IsPartner(self, theOther: TopoDS_Shape) -> bool:
        """
        Returns True if two shapes are partners, i.e. if
        they share the same TShape. Locations and
        Orientations may differ.
        """

    def IsSame(self, theOther: TopoDS_Shape) -> bool:
        """
        Returns True if two shapes are same, i.e. if they
        share the same TShape with the same Locations.
        Orientations may differ.
        """

    def IsEqual(self, theOther: TopoDS_Shape) -> bool:
        """
        Returns True if two shapes are equal, i.e. if they
        share the same TShape with the same Locations and
        Orientations.
        """

    def __eq__(self, theOther: TopoDS_Shape) -> bool: ...

    def IsNotEqual(self, theOther: TopoDS_Shape) -> bool:
        """Negation of the IsEqual method."""

    def __ne__(self, theOther: TopoDS_Shape) -> bool: ...

    def EmptyCopy(self) -> None:
        """
        Replace <me> by a new Shape with the same
        Orientation and Location and a new TShape with the
        same geometry and no sub-shapes.
        """

    def EmptyCopied(self) -> TopoDS_Shape:
        """
        Returns a new Shape with the same Orientation and
        Location and a new TShape with the same geometry
        and no sub-shapes.
        """

    def __hash__(self) -> int: ...

class TopoDS_AlertAttribute(nanoocp.Message.Message_AttributeStream):
    """Alert attribute object storing TopoDS shape in its field"""

    def __init__(self, theShape: TopoDS_Shape, theName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Constructor with shape argument"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetShape(self) -> TopoDS_Shape:
        """Returns contained shape"""

    @staticmethod
    def Send(theMessenger: nanoocp.Message.Message_Messenger, theShape: TopoDS_Shape) -> None:
        """Push shape information into messenger"""

class TopoDS_Builder:
    """
    A Builder is used to create Topological Data Structures.
    It is the root of the Builder class hierarchy.

    There are three groups of methods in the Builder:

    The Make methods create Shapes.

    The Add method includes a Shape in another Shape.

    The Remove method removes a Shape from an other
    Shape.

    The methods in Builder are not static. They can be
    redefined in inherited builders.

    This Builder does not provide methods to Make
    Vertices, Edges, Faces, Shells or Solids. These
    methods are provided in the inherited Builders
    as they must provide the geometry.

    The Add method check for the following rules:

    - Any SHAPE can be added in a COMPOUND.

    - Only SOLID can be added in a COMPSOLID.

    - Only SHELL, EDGE and VERTEX can be added in a SOLID.
    EDGE and VERTEX as to be INTERNAL or EXTERNAL.

    - Only FACE can be added in a SHELL.

    - Only WIRE and VERTEX can be added in a FACE.
    VERTEX as to be INTERNAL or EXTERNAL.

    - Only EDGE can be added in a WIRE.

    - Only VERTEX can be added in an EDGE.

    - Nothing can be added in a VERTEX.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopoDS_Builder) -> None: ...

    def MakeWire(self, W: TopoDS_Wire) -> None:
        """Make an empty Wire."""

    def MakeShell(self, S: TopoDS_Shell) -> None:
        """Make an empty Shell."""

    def MakeSolid(self, S: TopoDS_Solid) -> None:
        """Make a Solid covering the whole 3D space."""

    def MakeCompSolid(self, C: TopoDS_CompSolid) -> None:
        """Make an empty Composite Solid."""

    def MakeCompound(self, C: TopoDS_Compound) -> None:
        """Make an empty Compound."""

    def Add(self, S: TopoDS_Shape, C: TopoDS_Shape) -> None:
        """
        Add the Shape C in the Shape S.
        Exceptions
        - TopoDS_FrozenShape if S is not free and cannot be modified.
        - TopoDS__UnCompatibleShapes if S and C are not compatible.
        """

    def Remove(self, S: TopoDS_Shape, C: TopoDS_Shape) -> None:
        """
        Remove the Shape C from the Shape S.
        Exceptions
        TopoDS_FrozenShape if S is frozen and cannot be modified.
        """

class TopoDS_TWire(TopoDS_TShape):
    """A set of edges connected by their vertices."""

    @overload
    def __init__(self) -> None:
        """Creates an empty TWire."""

    @overload
    def __init__(self, theOther: TopoDS_TWire) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TWire."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_TShell(TopoDS_TShape):
    """A set of faces connected by their edges."""

    @overload
    def __init__(self) -> None:
        """Creates an empty TShell."""

    @overload
    def __init__(self, theOther: TopoDS_TShell) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TShell."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_TSolid(TopoDS_TShape):
    """
    A Topological part of 3D space, bounded by shells,
    edges and vertices.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty TSolid."""

    @overload
    def __init__(self, theOther: TopoDS_TSolid) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TSolid."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_TCompSolid(TopoDS_TShape):
    """A set of solids connected by their faces."""

    @overload
    def __init__(self) -> None:
        """Creates an empty TCompSolid."""

    @overload
    def __init__(self, theOther: TopoDS_TCompSolid) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TCompSolid."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_TCompound(TopoDS_TShape):
    """A TCompound is an all-purpose set of Shapes."""

    @overload
    def __init__(self) -> None:
        """Creates an empty TCompound."""

    @overload
    def __init__(self, theOther: TopoDS_TCompound) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TCompound."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_Wire(TopoDS_Shape):
    """
    Describes a wire which
    - references an underlying wire with the potential to
    be given a location and an orientation
    - has a location for the underlying wire, giving its
    placement in the local coordinate system
    - has an orientation for the underlying wire, in terms
    of its geometry (as opposed to orientation in relation to other shapes).
    """

    @overload
    def __init__(self) -> None:
        """Undefined Wire."""

    @overload
    def __init__(self, theOther: TopoDS_Wire) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_Shell(TopoDS_Shape):
    """
    Describes a shell which
    - references an underlying shell with the potential to
    be given a location and an orientation
    - has a location for the underlying shell, giving its
    placement in the local coordinate system
    - has an orientation for the underlying shell, in terms
    of its geometry (as opposed to orientation in relation to other shapes).
    """

    @overload
    def __init__(self) -> None:
        """Constructs an Undefined Shell."""

    @overload
    def __init__(self, theOther: TopoDS_Shell) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_Solid(TopoDS_Shape):
    """
    Describes a solid shape which
    - references an underlying solid shape with the
    potential to be given a location and an orientation
    - has a location for the underlying shape, giving its
    placement in the local coordinate system
    - has an orientation for the underlying shape, in
    terms of its geometry (as opposed to orientation in
    relation to other shapes).
    """

    @overload
    def __init__(self) -> None:
        """Constructs an Undefined Solid."""

    @overload
    def __init__(self, theOther: TopoDS_Solid) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_CompSolid(TopoDS_Shape):
    """
    Describes a composite solid which
    - references an underlying composite solid with the
    potential to be given a location and an orientation
    - has a location for the underlying composite solid,
    giving its placement in the local coordinate system
    - has an orientation for the underlying composite
    solid, in terms of its geometry (as opposed to
    orientation in relation to other shapes).
    Casts shape S to the more specialized return type, CompSolid.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an Undefined CompSolid."""

    @overload
    def __init__(self, theOther: TopoDS_CompSolid) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_Compound(TopoDS_Shape):
    """
    Describes a compound which
    - references an underlying compound with the
    potential to be given a location and an orientation
    - has a location for the underlying compound, giving
    its placement in the local coordinate system
    - has an orientation for the underlying compound, in
    terms of its geometry (as opposed to orientation in
    relation to other shapes).
    Casts shape S to the more specialized return type, Compound.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an Undefined Compound."""

    @overload
    def __init__(self, theOther: TopoDS_Compound) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_Edge(TopoDS_Shape):
    """
    Describes an edge which
    - references an underlying edge with the potential to
    be given a location and an orientation
    - has a location for the underlying edge, giving its
    placement in the local coordinate system
    - has an orientation for the underlying edge, in terms
    of its geometry (as opposed to orientation in
    relation to other shapes).
    """

    @overload
    def __init__(self) -> None:
        """Undefined Edge."""

    @overload
    def __init__(self, theOther: TopoDS_Edge) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_Face(TopoDS_Shape):
    """
    Describes a face which
    - references an underlying face with the potential to
    be given a location and an orientation
    - has a location for the underlying face, giving its
    placement in the local coordinate system
    - has an orientation for the underlying face, in terms
    of its geometry (as opposed to orientation in relation to other shapes).
    """

    @overload
    def __init__(self) -> None:
        """Undefined Face."""

    @overload
    def __init__(self, theOther: TopoDS_Face) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_FrozenShape(nanoocp.Standard.Standard_DomainError):
    pass

class TopoDS_HShape(nanoocp.Standard.Standard_Transient):
    """Class to manipulate a Shape with handle."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty shape object."""

    @overload
    def __init__(self, aShape: TopoDS_Shape) -> None:
        """Constructs a shape object defined by the shape aShape."""

    @overload
    def __init__(self, theOther: TopoDS_HShape) -> None: ...

    @overload
    def Shape(self, aShape: TopoDS_Shape) -> None:
        """Loads this shape with the shape aShape."""

    @overload
    def Shape(self) -> TopoDS_Shape:
        """Returns a reference to a constant TopoDS_Shape based on this shape."""

    def ChangeShape(self) -> TopoDS_Shape:
        """
        Exchanges the TopoDS_Shape object defining this
        shape for another one referencing the same underlying shape
        Accesses the list of shapes within the underlying
        shape referenced by the TopoDS_Shape object.
        Returns a reference to a TopoDS_Shape based on
        this shape. The TopoDS_Shape can be modified.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_Iterator:
    """
    Iterates on the underlying shape underlying a given
    TopoDS_Shape object, providing access to its
    component sub-shapes. Each component shape is
    returned as a TopoDS_Shape with an orientation,
    and a compound of the original values and the relative values.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty Iterator."""

    @overload
    def __init__(self, S: TopoDS_Shape, cumOri: bool = True, cumLoc: bool = True) -> None:
        """
        Creates an Iterator on <S> sub-shapes.
        Note:
        - If cumOri is true, the function composes all
        sub-shapes with the orientation of S.
        - If cumLoc is true, the function multiplies all
        sub-shapes by the location of S, i.e. it applies to
        each sub-shape the transformation that is associated with S.
        """

    @overload
    def __init__(self, theOther: TopoDS_Iterator) -> None: ...

    def Initialize(self, S: TopoDS_Shape, cumOri: bool = True, cumLoc: bool = True) -> None:
        """
        Initializes this iterator with shape S.
        Note:
        - If cumOri is true, the function composes all
        sub-shapes with the orientation of S.
        - If cumLoc is true, the function multiplies all
        sub-shapes by the location of S, i.e. it applies to
        each sub-shape the transformation that is associated with S.
        """

    def More(self) -> bool:
        """
        Returns true if there is another sub-shape in the
        shape which this iterator is scanning.
        """

    def Next(self) -> None:
        """
        Moves on to the next sub-shape in the shape which
        this iterator is scanning.
        Exceptions
        Standard_NoMoreObject if there are no more sub-shapes in the shape.
        """

    def Value(self) -> TopoDS_Shape:
        """
        Returns the current sub-shape in the shape which
        this iterator is scanning.
        Exceptions
        Standard_NoSuchObject if there is no current sub-shape.
        """

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class TopoDS_LockedShape(nanoocp.Standard.Standard_DomainError):
    pass

class TopoDS_TEdge(TopoDS_TShape):
    """
    A topological part of a curve in 2D or 3D, the
    boundary is a set of oriented Vertices.
    """

    def __init__(self, theOther: TopoDS_TEdge) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TEdge."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_TFace(TopoDS_TShape):
    """
    A topological part of a surface or of the 2D
    space. The boundary is a set of wires and vertices.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty TFace."""

    @overload
    def __init__(self, theOther: TopoDS_TFace) -> None: ...

    def EmptyCopy(self) -> TopoDS_TShape:
        """Returns an empty TFace."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_TVertex(TopoDS_TShape):
    """
    A Vertex is a topological point in two or three dimensions.
    TVertex has no children (sub-shapes).
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopoDS_UnCompatibleShapes(nanoocp.Standard.Standard_DomainError):
    pass

class TopoDS_Vertex(TopoDS_Shape):
    """
    Describes a vertex which
    - references an underlying vertex with the potential
    to be given a location and an orientation
    - has a location for the underlying vertex, giving its
    placement in the local coordinate system
    - has an orientation for the underlying vertex, in
    terms of its geometry (as opposed to orientation in
    relation to other shapes).
    """

    @overload
    def __init__(self) -> None:
        """Undefined Vertex."""

    @overload
    def __init__(self, theOther: TopoDS_Vertex) -> None: ...

    def __hash__(self) -> int: ...

class TopoDS_AlertWithShape(nanoocp.Message.Message_Alert):
    """Alert object storing TopoDS shape in its field"""

    @overload
    def __init__(self, theShape: TopoDS_Shape) -> None:
        """Constructor with shape argument"""

    @overload
    def __init__(self, theOther: TopoDS_AlertWithShape) -> None: ...

    def GetShape(self) -> TopoDS_Shape:
        """Returns contained shape"""

    def SetShape(self, theShape: TopoDS_Shape) -> None:
        """Sets the shape"""

    def SupportsMerge(self) -> bool:
        """Returns false."""

    def Merge(self, theTarget: nanoocp.Message.Message_Alert) -> bool:
        """Returns false."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_ForwardRangeIterator__TopoDS_Iterator:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: TopoDS_Iterator) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__TopoDS_Iterator) -> None: ...

@overload
def Vertex(theShape: TopoDS_Shape) -> TopoDS_Vertex: ...

@overload
def Vertex(theShape: TopoDS_Shape) -> TopoDS_Vertex:
    """
    Casts shape theShape to the more specialized return type, Vertex.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Vertex
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def Edge(theShape: TopoDS_Shape) -> TopoDS_Edge: ...

@overload
def Edge(theShape: TopoDS_Shape) -> TopoDS_Edge:
    """
    Casts shape theShape to the more specialized return type, Edge.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Edge
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def Wire(theShape: TopoDS_Shape) -> TopoDS_Wire: ...

@overload
def Wire(theShape: TopoDS_Shape) -> TopoDS_Wire:
    """
    Casts shape theShape to the more specialized return type, Wire.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Wire
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def Face(theShape: TopoDS_Shape) -> TopoDS_Face: ...

@overload
def Face(theShape: TopoDS_Shape) -> TopoDS_Face:
    """
    Casts shape theShape to the more specialized return type, Face.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Face
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def Shell(theShape: TopoDS_Shape) -> TopoDS_Shell: ...

@overload
def Shell(theShape: TopoDS_Shape) -> TopoDS_Shell:
    """
    Casts shape theShape to the more specialized return type, Shell.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Shell
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def Solid(theShape: TopoDS_Shape) -> TopoDS_Solid: ...

@overload
def Solid(theShape: TopoDS_Shape) -> TopoDS_Solid:
    """
    Casts shape theShape to the more specialized return type, Solid.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Solid
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def CompSolid(theShape: TopoDS_Shape) -> TopoDS_CompSolid: ...

@overload
def CompSolid(theShape: TopoDS_Shape) -> TopoDS_CompSolid:
    """
    Casts shape theShape to the more specialized return type, CompSolid.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_CompSolid
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """

@overload
def Compound(theShape: TopoDS_Shape) -> TopoDS_Compound: ...

@overload
def Compound(theShape: TopoDS_Shape) -> TopoDS_Compound:
    """
    Casts shape theShape to the more specialized return type, Compound.
    @param theShape the shape to be cast
    @return the casted shape as TopoDS_Compound
    @throws Standard_TypeMismatch if theShape cannot be cast to this return type.
    """
