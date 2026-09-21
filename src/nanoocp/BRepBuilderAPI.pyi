"""OCCT package BRepBuilderAPI (toolkit TKTopAlgo)"""

import enum
from typing import overload

import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class BRepBuilderAPI_EdgeError(enum.IntEnum):
    """
    Indicates the outcome of the
    construction of an edge, i.e. whether it has been successful or
    not, as explained below:
    -      BRepBuilderAPI_EdgeDone No error occurred; The edge is
    correctly built.
    -      BRepBuilderAPI_PointProjectionFailed No parameters were given but
    the projection of the 3D points on the curve failed. This
    happens when the point distance to the curve is greater than
    the precision value.
    -      BRepBuilderAPI_ParameterOutOfRange
    The given parameters are not in the parametric range
    C->FirstParameter(), C->LastParameter()
    -      BRepBuilderAPI_DifferentPointsOnClosedCurve
    The two vertices or points are the extremities of a closed
    curve but have different locations.
    -      BRepBuilderAPI_PointWithInfiniteParameter
    A finite coordinate point was associated with an infinite
    parameter (see the Precision package for a definition of infinite values).
    -      BRepBuilderAPI_DifferentsPointAndParameter
    The distance between the 3D point and the point evaluated
    on the curve with the parameter is greater than the precision.
    -      BRepBuilderAPI_LineThroughIdenticPoints
    Two identical points were given to define a line (construction
    of an edge without curve); gp::Resolution is used for the confusion test.
    """

    BRepBuilderAPI_EdgeDone = 0

    BRepBuilderAPI_PointProjectionFailed = 1

    BRepBuilderAPI_ParameterOutOfRange = 2

    BRepBuilderAPI_DifferentPointsOnClosedCurve = 3

    BRepBuilderAPI_PointWithInfiniteParameter = 4

    BRepBuilderAPI_DifferentsPointAndParameter = 5

    BRepBuilderAPI_LineThroughIdenticPoints = 6

BRepBuilderAPI_EdgeDone: BRepBuilderAPI_EdgeError = BRepBuilderAPI_EdgeError.BRepBuilderAPI_EdgeDone

BRepBuilderAPI_PointProjectionFailed: BRepBuilderAPI_EdgeError = ...

BRepBuilderAPI_ParameterOutOfRange: BRepBuilderAPI_EdgeError = ...

BRepBuilderAPI_DifferentPointsOnClosedCurve: BRepBuilderAPI_EdgeError = ...

BRepBuilderAPI_PointWithInfiniteParameter: BRepBuilderAPI_EdgeError = ...

BRepBuilderAPI_DifferentsPointAndParameter: BRepBuilderAPI_EdgeError = ...

BRepBuilderAPI_LineThroughIdenticPoints: BRepBuilderAPI_EdgeError = ...

class BRepBuilderAPI_FaceError(enum.IntEnum):
    """
    Indicates the outcome of the
    construction of a face, i.e. whether it has been successful or
    not, as explained below:
    -      BRepBuilderAPI_FaceDone No error occurred. The face is
    correctly built.
    -      BRepBuilderAPI_NoFace No initialization of the
    algorithm; only an empty constructor was used.
    -      BRepBuilderAPI_NotPlanar
    No surface was given and the wire was not planar.
    -      BRepBuilderAPI_CurveProjectionFailed
    Not used so far.
    -      BRepBuilderAPI_ParametersOutOfRange
    The parameters given to limit the surface are out of its bounds.
    """

    BRepBuilderAPI_FaceDone = 0

    BRepBuilderAPI_NoFace = 1

    BRepBuilderAPI_NotPlanar = 2

    BRepBuilderAPI_CurveProjectionFailed = 3

    BRepBuilderAPI_ParametersOutOfRange = 4

BRepBuilderAPI_FaceDone: BRepBuilderAPI_FaceError = BRepBuilderAPI_FaceError.BRepBuilderAPI_FaceDone

BRepBuilderAPI_NoFace: BRepBuilderAPI_FaceError = BRepBuilderAPI_FaceError.BRepBuilderAPI_NoFace

BRepBuilderAPI_NotPlanar: BRepBuilderAPI_FaceError = BRepBuilderAPI_FaceError.BRepBuilderAPI_NotPlanar

BRepBuilderAPI_CurveProjectionFailed: BRepBuilderAPI_FaceError = ...

BRepBuilderAPI_ParametersOutOfRange: BRepBuilderAPI_FaceError = ...

class BRepBuilderAPI_ShellError(enum.IntEnum):
    """
    Indicates the outcome of the construction of a face, i.e.
    whether it is successful or not, as explained below:
    -   BRepBuilderAPI_ShellDone No error occurred.
    The shell is correctly built.
    -   BRepBuilderAPI_EmptyShell No initialization of
    the algorithm: only an empty constructor was used.
    -   BRepBuilderAPI_DisconnectedShell not yet used
    -   BRepBuilderAPI_ShellParametersOutOfRange
    The parameters given to limit the surface are out of its bounds.
    """

    BRepBuilderAPI_ShellDone = 0

    BRepBuilderAPI_EmptyShell = 1

    BRepBuilderAPI_DisconnectedShell = 2

    BRepBuilderAPI_ShellParametersOutOfRange = 3

BRepBuilderAPI_ShellDone: BRepBuilderAPI_ShellError = ...

BRepBuilderAPI_EmptyShell: BRepBuilderAPI_ShellError = ...

BRepBuilderAPI_DisconnectedShell: BRepBuilderAPI_ShellError = ...

BRepBuilderAPI_ShellParametersOutOfRange: BRepBuilderAPI_ShellError = ...

class BRepBuilderAPI_WireError(enum.IntEnum):
    """
    Indicates the outcome of wire
    construction, i.e. whether it is successful or not, as explained below:
    -      BRepBuilderAPI_WireDone No
    error occurred. The wire is correctly built.
    -      BRepBuilderAPI_EmptyWire No
    initialization of the algorithm. Only an empty constructor was used.
    -      BRepBuilderAPI_DisconnectedWire
    The last edge which you attempted to add was not connected to the wire.
    -      BRepBuilderAPI_NonManifoldWire
    The wire with some singularity.
    """

    BRepBuilderAPI_WireDone = 0

    BRepBuilderAPI_EmptyWire = 1

    BRepBuilderAPI_DisconnectedWire = 2

    BRepBuilderAPI_NonManifoldWire = 3

BRepBuilderAPI_WireDone: BRepBuilderAPI_WireError = BRepBuilderAPI_WireError.BRepBuilderAPI_WireDone

BRepBuilderAPI_EmptyWire: BRepBuilderAPI_WireError = BRepBuilderAPI_WireError.BRepBuilderAPI_EmptyWire

BRepBuilderAPI_DisconnectedWire: BRepBuilderAPI_WireError = ...

BRepBuilderAPI_NonManifoldWire: BRepBuilderAPI_WireError = ...

class BRepBuilderAPI_PipeError(enum.IntEnum):
    """Errors that can occur at (shell)pipe construction."""

    BRepBuilderAPI_PipeDone = 0

    BRepBuilderAPI_PipeNotDone = 1

    BRepBuilderAPI_PlaneNotIntersectGuide = 2

    BRepBuilderAPI_ImpossibleContact = 3

BRepBuilderAPI_PipeDone: BRepBuilderAPI_PipeError = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeDone

BRepBuilderAPI_PipeNotDone: BRepBuilderAPI_PipeError = ...

BRepBuilderAPI_PlaneNotIntersectGuide: BRepBuilderAPI_PipeError = ...

BRepBuilderAPI_ImpossibleContact: BRepBuilderAPI_PipeError = ...

class BRepBuilderAPI_ShapeModification(enum.IntEnum):
    """
    Lists the possible types of modification to a shape
    following a topological operation: Preserved, Deleted,
    Trimmed, Merged or BoundaryModified.
    This enumeration enables you to assign a "state" to the
    different shapes that are on the list of operands for
    each API function. The MakeShape class then uses this
    to determine what has happened to the shapes which
    constitute the list of operands.
    """

    BRepBuilderAPI_Preserved = 0

    BRepBuilderAPI_Deleted = 1

    BRepBuilderAPI_Trimmed = 2

    BRepBuilderAPI_Merged = 3

    BRepBuilderAPI_BoundaryModified = 4

BRepBuilderAPI_Preserved: BRepBuilderAPI_ShapeModification = ...

BRepBuilderAPI_Deleted: BRepBuilderAPI_ShapeModification = ...

BRepBuilderAPI_Trimmed: BRepBuilderAPI_ShapeModification = ...

BRepBuilderAPI_Merged: BRepBuilderAPI_ShapeModification = ...

BRepBuilderAPI_BoundaryModified: BRepBuilderAPI_ShapeModification = ...

class BRepBuilderAPI_TransitionMode(enum.IntEnum):
    """Option to manage discontinuities in Sweep"""

    BRepBuilderAPI_Transformed = 0

    BRepBuilderAPI_RightCorner = 1

    BRepBuilderAPI_RoundCorner = 2

BRepBuilderAPI_Transformed: BRepBuilderAPI_TransitionMode = ...

BRepBuilderAPI_RightCorner: BRepBuilderAPI_TransitionMode = ...

BRepBuilderAPI_RoundCorner: BRepBuilderAPI_TransitionMode = ...

class BRepBuilderAPI:
    """
    The BRepBuilderAPI package provides an Application
    Programming Interface for the BRep topology data
    structure.

    The API is a set of classes aiming to provide:

    * High level and simple calls for the most common
    operations.

    * Keeping an access on the low-level
    implementation of high-level calls.

    * Examples of programming of high-level operations
    from low-level operations.

    * A complete coverage of modelling:

    - Creating vertices ,edges, faces, solids.

    - Sweeping operations.

    - Boolean operations.

    - Global properties computation.

    The API provides classes to build objects:

    * The constructors of the classes provides the
    different constructions methods.

    * The class keeps as fields the different tools
    used to build the object.

    * The class provides a casting method to get
    automatically the result with a function-like
    call.

    For example to make a vertex <V> from a point <P>
    one can write:

    V = BRepBuilderAPI_MakeVertex(P);

    or

    BRepBuilderAPI_MakeVertex MV(P);
    V = MV.Vertex();

    For tolerances a default precision is used which
    can be changed by the packahe method
    BRepBuilderAPI::Precision.

    For error handling the BRepBuilderAPI commands raise only
    the NotDone error. When Done is false on a command
    the error description can be asked to the command.

    In theory the commands can be called with any
    arguments, argument checking is performed by the
    command.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepBuilderAPI) -> None: ...

    @overload
    @staticmethod
    def Plane(P: nanoocp.Geom.Geom_Plane | None) -> None:
        """Sets the current plane."""

    @overload
    @staticmethod
    def Plane() -> nanoocp.Geom.Geom_Plane:
        """Returns the current plane."""

    @overload
    @staticmethod
    def Precision(P: float) -> None:
        """
        Sets the default precision. The current Precision
        is returned.
        """

    @overload
    @staticmethod
    def Precision() -> float:
        """Returns the default precision."""

class BRepBuilderAPI_Collect:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepBuilderAPI_Collect) -> None: ...

    def Add(self, SI: nanoocp.TopoDS.TopoDS_Shape, MKS: BRepBuilderAPI_MakeShape) -> None: ...

    def AddGenerated(self, S: nanoocp.TopoDS.TopoDS_Shape, Gen: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddModif(self, S: nanoocp.TopoDS.TopoDS_Shape, Mod: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Filter(self, SF: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Modification(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def Generated(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

class BRepBuilderAPI_Command:
    """
    Root class for all commands in BRepBuilderAPI.

    Provides :

    * Managements of the notDone flag.

    * Catching of exceptions (not implemented).

    * Logging (not implemented).
    """

    def __init__(self, theOther: BRepBuilderAPI_Command) -> None: ...

    def IsDone(self) -> bool: ...

    def Check(self) -> None:
        """Raises NotDone if done is false."""

class BRepBuilderAPI_MakeShape(BRepBuilderAPI_Command):
    """
    This is the root class for all shape
    constructions. It stores the result.

    It provides deferred methods to trace the history
    of sub-shapes.
    """

    def __init__(self, theOther: BRepBuilderAPI_MakeShape) -> None: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        This is called by Shape(). It does nothing but
        may be redefined.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a shape built by the shape construction algorithm.
        Raises exception StdFail_NotDone if the shape was not built.
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the shape S has been deleted."""

class BRepBuilderAPI_ModifyShape(BRepBuilderAPI_MakeShape):
    """
    Implements the methods of MakeShape for the
    constant topology modifications. The methods are
    implemented when the modification uses a Modifier
    from BRepTools. Some of them have to be redefined
    if the modification is implemented with another
    tool (see Transform from BRepBuilderAPI for example).
    The BRepBuilderAPI package provides the following
    frameworks to perform modifications of this sort:
    -   BRepBuilderAPI_Copy to produce the copy of a shape,
    -   BRepBuilderAPI_Transform and
    BRepBuilderAPI_GTransform to apply a geometric
    transformation to a shape,
    -   BRepBuilderAPI_NurbsConvert to convert the
    whole geometry of a shape into NURBS geometry,
    -   BRepOffsetAPI_DraftAngle to build a tapered shape.
    """

    def __init__(self, theOther: BRepBuilderAPI_ModifyShape) -> None: ...

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

    def ModifiedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the modified shape corresponding to <S>.
        S can correspond to the entire initial shape or to its subshape.
        Exceptions
        Standard_NoSuchObject if S is not the initial shape or
        a subshape of the initial shape to which the
        transformation has been applied. Raises NoSuchObject from Standard
        if S is not the initial shape or a sub-shape
        of the initial shape.
        """

class BRepBuilderAPI_Copy(BRepBuilderAPI_ModifyShape):
    """
    Duplication of a shape.
    A Copy object provides a framework for:
    -   defining the construction of a duplicate shape,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty copy framework. Use the function
        Perform to copy shapes.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, copyGeom: bool = True, copyMesh: bool = False) -> None:
        """
        Constructs a copy framework and copies the shape S.
        Use the function Shape to access the result.
        If copyMesh is True, triangulation contained in original shape will be
        copied along with geometry (by default, triangulation gets lost).
        If copyGeom is False, only topological objects will be copied, while
        geometry and triangulation will be shared with original shape.
        Note: the constructed framework can be reused to copy
        other shapes: just specify them with the function Perform.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_Copy) -> None: ...

    def Perform(self, S: nanoocp.TopoDS.TopoDS_Shape, copyGeom: bool = True, copyMesh: bool = False) -> None:
        """
        Copies the shape S.
        Use the function Shape to access the result.
        If copyMesh is True, triangulation contained in original shape will be
        copied along with geometry (by default, triangulation gets lost).
        If copyGeom is False, only topological objects will be copied, while
        geometry and triangulation will be shared with original shape.
        """

class BRepBuilderAPI_FastSewing(nanoocp.Standard.Standard_Transient):
    """
    This class performs fast sewing of surfaces (faces). It supposes
    that all surfaces are finite and are naturally restricted by their bounds.
    Moreover, it supposes that stitched together surfaces have the same parameterization
    along common boundaries, therefore it does not perform time-consuming check for
    SameParameter property of edges.

    For sewing, use this function as following:
    - set tolerance value (default tolerance is 1.E-06)
    - add all necessary surfaces (faces)
    - check status if adding is correctly completed.
    - compute -> Perform
    - retrieve the error status if any
    - retrieve the resulted shape
    """

    @overload
    def __init__(self, theTolerance: float = 1e-06) -> None:
        """Creates an object with tolerance of connexity"""

    @overload
    def __init__(self, theOther: BRepBuilderAPI_FastSewing) -> None: ...

    class FS_Statuses(enum.IntEnum):
        """Enumeration of result statuses"""

        FS_OK = 0

        FS_Degenerated = 1

        FS_FindVertexError = 2

        FS_FindEdgeError = 4

        FS_FaceWithNullSurface = 8

        FS_NotNaturalBoundsFace = 16

        FS_InfiniteSurface = 32

        FS_EmptyInput = 64

        FS_Exception = 128

    FS_OK: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_OK

    FS_Degenerated: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_Degenerated

    FS_FindVertexError: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_FindVertexError

    FS_FindEdgeError: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_FindEdgeError

    FS_FaceWithNullSurface: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_FaceWithNullSurface

    FS_NotNaturalBoundsFace: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_NotNaturalBoundsFace

    FS_InfiniteSurface: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_InfiniteSurface

    FS_EmptyInput: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_EmptyInput

    FS_Exception: BRepBuilderAPI_FastSewing.FS_Statuses = FS_Statuses.FS_Exception

    @overload
    def Add(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Adds faces of a shape"""

    @overload
    def Add(self, theSurface: nanoocp.Geom.Geom_Surface | None) -> bool:
        """Adds a surface"""

    def Perform(self) -> None:
        """Compute resulted shape"""

    def SetTolerance(self, theToler: float) -> None:
        """Sets tolerance"""

    def GetTolerance(self) -> float:
        """Returns tolerance"""

    def GetResult(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns resulted shape"""

    def GetStatuses(self) -> int:
        """Returns list of statuses. Print message if theOS != 0"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBuilderAPI_FindPlane:
    """
    Describes functions to find the plane in which the edges
    of a given shape are located.
    A FindPlane object provides a framework for:
    -   extracting the edges of a given shape,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes an empty algorithm. The function Init is then used to define the shape.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, Tol: float = -1.0) -> None:
        """
        Constructs the plane containing the edges of the shape S.
        A plane is built only if all the edges are within a distance
        of less than or equal to tolerance from a planar surface.
        This tolerance value is equal to the larger of the following two values:
        -   Tol, where the default value is negative, or
        -   the largest of the tolerance values assigned to the individual edges of S.
        Use the function Found to verify that a plane is built.
        The resulting plane is then retrieved using the function Plane.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_FindPlane) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, Tol: float = -1.0) -> None:
        """
        Constructs the plane containing the edges of the shape S.
        A plane is built only if all the edges are within a distance
        of less than or equal to tolerance from a planar surface.
        This tolerance value is equal to the larger of the following two values:
        -   Tol, where the default value is negative, or
        -   the largest of the tolerance values assigned to the individual edges of S.
        Use the function Found to verify that a plane is built.
        The resulting plane is then retrieved using the function Plane.
        """

    def Found(self) -> bool:
        """
        Returns true if a plane containing the edges of the
        shape is found and built. Use the function Plane to consult the result.
        """

    def Plane(self) -> nanoocp.Geom.Geom_Plane:
        """
        Returns the plane containing the edges of the shape.
        Warning
        Use the function Found to verify that the plane is built. If
        a plane is not found, Plane returns a null handle.
        """

class BRepBuilderAPI_GTransform(BRepBuilderAPI_ModifyShape):
    """
    Geometric transformation on a shape.
    The transformation to be applied is defined as a gp_GTrsf
    transformation. It may be:
    -      a transformation equivalent to a gp_Trsf transformation, the
    most common case: you should , however, use a BRepAPI_Transform
    object to perform this kind of transformation; or
    -      an affinity, or
    -      more generally, any type of point transformation which may
    be defined by a three row, four column matrix of transformation.
    In the last two cases, the underlying geometry of the
    following shapes may change:
    -      a curve which supports an edge of the shape, or
    -      a surface which supports a face of the shape;
    For example, a circle may be transformed into an ellipse when
    applying an affinity transformation.
    The transformation is applied to:
    -      all the curves which support edges of the shape, and
    -      all the surfaces which support faces of the shape.
    A GTransform object provides a framework for:
    -      defining the geometric transformation to be applied,
    -      implementing the transformation algorithm, and
    -      consulting the result.
    """

    @overload
    def __init__(self, T: nanoocp.gp.gp_GTrsf) -> None:
        """
        Constructs a framework for applying the geometric
        transformation T to a shape. Use the function
        Perform to define the shape to transform.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.gp.gp_GTrsf, Copy: bool = False) -> None:
        """
        Constructs a framework for applying the geometric
        transformation T to a shape, and applies it to the shape S.
        -   If the transformation T is direct and isometric (i.e. if
        the determinant of the vectorial part of T is equal to
        1.), and if Copy equals false (default value), the
        resulting shape is the same as the original but with
        a new location assigned to it.
        -   In all other cases, the transformation is applied to
        a duplicate of S.
        Use the function Shape to access the result.
        Note: the constructed framework can be reused to
        apply the same geometric transformation to other
        shapes: just specify them with the function Perform.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_GTransform) -> None: ...

    def Perform(self, S: nanoocp.TopoDS.TopoDS_Shape, Copy: bool = False) -> None:
        """
        Applies the geometric transformation defined at the
        time of construction of this framework to the shape S.
        -   If the transformation T is direct and isometric (i.e. if
        the determinant of the vectorial part of T is equal to
        1.), and if Copy equals false (default value), the
        resulting shape is the same as the original but with
        a new location assigned to it.
        -   In all other cases, the transformation is applied to a duplicate of S.
        Use the function Shape to access the result.
        Note: this framework can be reused to apply the same
        geometric transformation to other shapes: just specify
        them by calling the function Perform again.
        """

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

    def ModifiedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the modified shape corresponding to <S>."""

class BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeShape):
    """
    Provides methods to build edges.

    The methods have the following syntax, where
    TheCurve is one of Lin, Circ, ...

    Create(C : TheCurve)

    Makes an edge on the whole curve. Add vertices
    on finite curves.

    Create(C : TheCurve; p1,p2 : Real)

    Make an edge on the curve between parameters p1
    and p2. if p2 < p1 the edge will be REVERSED. If
    p1 or p2 is infinite the curve will be open in
    that direction. Vertices are created for finite
    values of p1 and p2.

    Create(C : TheCurve; P1, P2 : Pnt from gp)

    Make an edge on the curve between the points P1
    and P2. The points are projected on the curve
    and the previous method is used. An error is
    raised if the points are not on the curve.

    Create(C : TheCurve; V1, V2 : Vertex from TopoDS)

    Make an edge on the curve between the vertices
    V1 and V2. Same as the previous but no vertices
    are created. If a vertex is Null the curve will
    be open in this direction.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None:
        """
        The general method to directly create an edge is to give
        -      a 3D curve C as the support (geometric domain) of the edge,
        -      two vertices V1 and V2 to limit the curve (definition of the restriction of
        the edge), and
        -      two real values p1 and p2 which are the parameters for the vertices V1 and V2
        on the curve.
        The curve may be defined as a 2d curve in the parametric space of a surface: a
        pcurve. The surface on which the edge is built is then kept at the level of the edge.
        The default tolerance will be associated with this edge.
        Rules applied to the arguments:
        For the curve:
        -      The curve must not be a 'null handle'.
        -      If the curve is a trimmed curve the basis curve is used.
        For the vertices:
        -      Vertices may be null shapes. When V1 or V2 is null the edge is open in the
        corresponding direction and the parameter value p1 or p2 must be infinite
        (remember that Precision::Infinite() defines an infinite value).
        -      The two vertices must be identical if they have the same 3D location.
        Identical vertices are used in particular when the curve is closed.
        For the parameters:
        -      The parameters must be in the parametric range of the curve (or the basis
        curve if the curve is trimmed). If this condition is not satisfied the edge is not
        built, and the Error function will return BRepAPI_ParameterOutOfRange.
        -      Parameter values must not be equal. If this condition is not satisfied (i.e.
        if | p1 - p2 | ) the edge is not built, and the Error function will return
        BRepAPI_LineThroughIdenticPoints.
        Parameter values are expected to be given in increasing order:
        C->FirstParameter()
        - If the parameter values are given in decreasing order the vertices are switched,
        i.e. the "first vertex" is on the point of parameter p2 and the "second vertex" is
        on the point of parameter p1. In such a case, to keep the original intent of the
        construction, the edge will be oriented "reversed".
        - On a periodic curve the parameter values p1 and p2 are adjusted by adding or
        subtracting the period to obtain p1 in the parametric range of the curve, and p2]
        such that [ p1 , where Period is the period of the curve.
        - A parameter value may be infinite. The edge is open in the corresponding
        direction. However the corresponding vertex must be a null shape. If this condition
        is not satisfied the edge is not built, and the Error function will return
        BRepAPI_PointWithInfiniteParameter.
        - The distance between the vertex and the point evaluated on the curve with the
        parameter, must be lower than the precision of the vertex. If this condition is not
        satisfied the edge is not built, and the Error function will return
        BRepAPI_DifferentsPointAndParameter.
        Other edge constructions
        - The parameter values can be omitted, they will be computed by projecting the
        vertices on the curve. Note that projection is the only way to evaluate the
        parameter values of the vertices on the curve: vertices must be given on the curve,
        i.e. the distance from a vertex to the curve must be less than or equal to the
        precision of the vertex. If this condition is not satisfied the edge is not built,
        and the Error function will return BRepAPI_PointProjectionFailed.
        -      3D points can be given in place of vertices. Vertices will be created from the
        points (with the default topological precision Precision::Confusion()).
        Note:
        -      Giving vertices is useful when creating a connected edge.
        -      If the parameter values correspond to the extremities of a closed curve,
        points must be identical, or at least coincident. If this condition is not
        satisfied the edge is not built, and the Error function will return
        BRepAPI_DifferentPointsOnClosedCurve.
        -      The vertices or points can be omitted if the parameter values are given. The
        points will be computed from the parameters on the curve.
        The vertices or points and the parameter values can be omitted. The first and last
        parameters of the curve will then be used.

        Auxiliary methods
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeEdge) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None:
        """
        Defines or redefines the arguments for the construction of an edge.
        This function is currently used after the empty constructor BRepAPI_MakeEdge().
        """

    def IsDone(self) -> bool:
        """Returns true if the edge is built."""

    def Error(self) -> BRepBuilderAPI_EdgeError:
        """
        Returns the construction status
        -   BRepBuilderAPI_EdgeDone if the edge is built, or
        -   another value of the BRepBuilderAPI_EdgeError
        enumeration indicating the reason of construction failure.
        """

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the constructed edge.
        Exceptions StdFail_NotDone if the edge is not built.
        """

    def Vertex1(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the first vertex of the edge. May be Null."""

    def Vertex2(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the second vertex of the edge. May be Null.

        Warning
        The returned vertex in each function corresponds respectively to
        -   the lowest, or
        -   the highest parameter on the curve along which the edge is built.
        It does not correspond to the first or second vertex
        given at the time of the construction, if the edge is oriented reversed.
        Exceptions
        StdFail_NotDone if the edge is not built.
        """

class BRepBuilderAPI_MakeEdge2d(BRepBuilderAPI_MakeShape):
    """
    Provides methods to build edges.

    The methods have the following syntax, where
    TheCurve is one of Lin2d, Circ2d, ...

    Create(C : TheCurve)

    Makes an edge on the whole curve. Add vertices
    on finite curves.

    Create(C : TheCurve; p1,p2 : Real)

    Make an edge on the curve between parameters p1
    and p2. if p2 < p1 the edge will be REVERSED. If
    p1 or p2 is infinite the curve will be open in
    that direction. Vertices are created for finite
    values of p1 and p2.

    Create(C : TheCurve; P1, P2 : Pnt2d from gp)

    Make an edge on the curve between the points P1
    and P2. The points are projected on the curve
    and the previous method is used. An error is
    raised if the points are not on the curve.

    Create(C : TheCurve; V1, V2 : Vertex from TopoDS)

    Make an edge on the curve between the vertices
    V1 and V2. Same as the previous but no vertices
    are created. If a vertex is Null the curve will
    be open in this direction.
    """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeEdge2d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    def IsDone(self) -> bool: ...

    def Error(self) -> BRepBuilderAPI_EdgeError:
        """Returns the error description when NotDone."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Vertex1(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the first vertex of the edge. May be Null."""

    def Vertex2(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the second vertex of the edge. May be Null."""

class BRepBuilderAPI_MakeFace(BRepBuilderAPI_MakeShape):
    """
    Provides methods to build faces.

    A face may be built:

    * From a surface.

    - Elementary surface from gp.

    - Surface from Geom.

    * From a surface and U,V values.

    * From a wire.

    - Find the surface automatically if possible.

    * From a surface and a wire.

    - A flag Inside is given, when this flag is True
    the wire is oriented to bound a finite area on
    the surface.

    * From a face and a wire.

    - The new wire is a perforation.
    """

    @overload
    def __init__(self) -> None:
        """Not done."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Load a face. useful to add wires."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Torus) -> None: ...

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, OnlyPlane: bool = False) -> None:
        """
        Find a surface from the wire and make a face.
        if <OnlyPlane> is true, the computed surface will be
        a plane. If it is not possible to find a plane, the
        flag NotDone will be set.
        """

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, TolDegen: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a plane and a wire."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a cylinder and a wire."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a cone and a wire."""

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a sphere and a wire."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Torus, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a torus and a wire."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """
        Make a face from a Surface and a wire.
        If the surface S is not plane,
        it must contain pcurves for all edges in W,
        otherwise the wrong shape will be created.
        """

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Adds the wire <W> in the face <F>
        A general method to create a face is to give
        -      a surface S as the support (the geometric domain) of the face,
        -      and a wire W to bound it.
        The bounds of the face can also be defined by four parameter values
        umin, umax, vmin, vmax which determine isoparametric limitations on
        the parametric space of the surface. In this way, a patch is
        defined. The parameter values are optional. If they are omitted, the
        natural bounds of the surface are used. A wire is automatically
        built using the defined bounds. Up to four edges and four vertices
        are created with this wire (no edge is created when the
        corresponding parameter value is infinite).
        Wires can then be added using the function Add to define other
        restrictions on the face. These restrictions represent holes. More
        than one wire may be added by this way, provided that the wires do
        not cross each other and that they define only one area on the
        surface. (Be careful, however, as this is not checked).
        Forbidden addition of wires
        Note that in this schema, the third case is valid if edges of the
        wire W are declared internal to the face. As a result, these edges
        are no longer bounds of the face.
        A default tolerance (Precision::Confusion()) is given to the face,
        this tolerance may be increased during construction of the face
        using various algorithms.
        Rules applied to the arguments
        For the surface:
        -      The surface must not be a 'null handle'.
        -      If the surface is a trimmed surface, the basis surface is used.
        -      For the wire: the wire is composed of connected edges, each
        edge having a parametric curve description in the parametric
        domain of the surface; in other words, as a pcurve.
        For the parameters:
        -      The parameter values must be in the parametric range of the
        surface (or the basis surface, if the surface is trimmed). If this
        condition is not satisfied, the face is not built, and the Error
        function will return BRepBuilderAPI_ParametersOutOfRange.
        -      The bounding parameters p1 and p2 are adjusted on a periodic
        surface in a given parametric direction by adding or subtracting
        the period to obtain p1 in the parametric range of the surface and
        such p2, that p2 - p1 <= Period, where Period is the period of the
        surface in this parametric direction.
        -      A parameter value may be infinite. There will be no edge and
        no vertex in the corresponding direction.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a plane."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a cylinder."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a cone."""

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a sphere."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Torus, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a torus."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None:
        """
        Make a face from a Surface. Accepts tolerance value (TolDegen)
        for resolution of degenerated edges.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeFace) -> None: ...

    @overload
    def Init(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Initializes (or reinitializes) the
        construction of a face by creating a new object which is a copy of
        the face F, in order to add wires to it, using the function Add.
        Note: this complete copy of the geometry is only required if you
        want to work on the geometries of the two faces independently.
        """

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None, Bound: bool, TolDegen: float) -> None:
        """
        Initializes (or reinitializes) the construction of a face on
        the surface S. If Bound is true, a wire is
        automatically created from the natural bounds of the
        surface S and added to the face in order to bound it. If
        Bound is false, no wire is added. This option is used
        when real bounds are known. These will be added to
        the face after this initialization, using the function Add.
        TolDegen parameter is used for resolution of degenerated edges
        if calculation of natural bounds is turned on.
        """

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None:
        """
        Initializes (or reinitializes) the construction of a face on
        the surface S, limited in the u parametric direction by
        the two parameter values UMin and UMax and in the
        v parametric direction by the two parameter values VMin and VMax.
        Warning
        Error returns:
        -      BRepBuilderAPI_ParametersOutOfRange
        when the parameters given are outside the bounds of the
        surface or the basis surface of a trimmed surface.
        TolDegen parameter is used for resolution of degenerated edges.
        """

    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Adds the wire W to the constructed face as a hole.
        Warning
        W must not cross the other bounds of the face, and all
        the bounds must define only one area on the surface.
        (Be careful, however, as this is not checked.)
        Example
        // a cylinder
        gp_Cylinder C = ..;
        // a wire
        TopoDS_Wire W = ...;
        BRepBuilderAPI_MakeFace MF(C);
        MF.Add(W);
        TopoDS_Face F = MF;
        """

    def IsDone(self) -> bool:
        """Returns true if this algorithm has a valid face."""

    def Error(self) -> BRepBuilderAPI_FaceError:
        """
        Returns the construction status
        BRepBuilderAPI_FaceDone if the face is built, or
        -   another value of the BRepBuilderAPI_FaceError
        enumeration indicating why the construction failed, in
        particular when the given parameters are outside the
        bounds of the surface.
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the constructed face.
        Exceptions
        StdFail_NotDone if no face is built.
        """

class BRepBuilderAPI_MakePolygon(BRepBuilderAPI_MakeShape):
    """
    Describes functions to build polygonal wires. A
    polygonal wire can be built from any number of points
    or vertices, and consists of a sequence of connected
    rectilinear edges.
    When a point or vertex is added to the polygon if
    it is identic to the previous point no edge is
    built. The method added can be used to test it.
    Construction of a Polygonal Wire
    You can construct:
    -   a complete polygonal wire by defining all its points
    or vertices (limited to four), or
    -   an empty polygonal wire and add its points or
    vertices in sequence (unlimited number).
    A MakePolygon object provides a framework for:
    -   initializing the construction of a polygonal wire,
    -   adding points or vertices to the polygonal wire under construction, and
    -   consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes an empty polygonal wire, to which points or
        vertices are added using the Add function.
        As soon as the polygonal wire under construction
        contains vertices, it can be consulted using the Wire function.
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, Close: bool = False) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, V3: nanoocp.TopoDS.TopoDS_Vertex, Close: bool = False) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, P4: nanoocp.gp.gp_Pnt, Close: bool = False) -> None:
        """
        Constructs a polygonal wire from 2, 3 or 4 points. Vertices are
        automatically created on the given points. The polygonal wire is
        closed if Close is true; otherwise it is open. Further vertices can
        be added using the Add function. The polygonal wire under
        construction can be consulted at any time by using the Wire function.
        Example
        //an open polygon from four points
        TopoDS_Wire W = BRepBuilderAPI_MakePolygon(P1,P2,P3,P4);
        Warning: The process is equivalent to:
        - initializing an empty polygonal wire,
        - and adding the given points in sequence.
        Consequently, be careful when using this function: if the
        sequence of points p1 - p2 - p1 is found among the arguments of the
        constructor, you will create a polygonal wire with two
        consecutive coincident edges.
        """

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, V3: nanoocp.TopoDS.TopoDS_Vertex, V4: nanoocp.TopoDS.TopoDS_Vertex, Close: bool = False) -> None:
        """
        Constructs a polygonal wire from
        2, 3 or 4 vertices. The polygonal wire is closed if Close is true;
        otherwise it is open (default value). Further vertices can be
        added using the Add function. The polygonal wire under
        construction can be consulted at any time by using the Wire function.
        Example
        //a closed triangle from three vertices
        TopoDS_Wire W = BRepBuilderAPI_MakePolygon(V1,V2,V3,true);
        Warning
        The process is equivalent to:
        -      initializing an empty polygonal wire,
        -      then adding the given points in sequence.
        So be careful, as when using this function, you could create a
        polygonal wire with two consecutive coincident edges if
        the sequence of vertices v1 - v2 - v1 is found among the
        constructor's arguments.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakePolygon) -> None: ...

    @overload
    def Add(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Add(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Adds the point P or the vertex V at the end of the
        polygonal wire under construction. A vertex is
        automatically created on the point P.
        Warning
        -   When P or V is coincident to the previous vertex,
        no edge is built. The method Added can be used to
        test for this. Neither P nor V is checked to verify
        that it is coincident with another vertex than the last
        one, of the polygonal wire under construction. It is
        also possible to add vertices on a closed polygon
        (built for example by using a constructor which
        declares the polygon closed, or after the use of the Close function).
        Consequently, be careful using this function: you might create:
        -      a polygonal wire with two consecutive coincident edges, or
        -      a non manifold polygonal wire.
        -      P or V is not checked to verify if it is
        coincident with another vertex but the last one, of
        the polygonal wire under construction. It is also
        possible to add vertices on a closed polygon (built
        for example by using a constructor which declares
        the polygon closed, or after the use of the Close function).
        Consequently, be careful when using this function: you might create:
        -   a polygonal wire with two consecutive coincident edges, or
        -   a non-manifold polygonal wire.
        """

    def Added(self) -> bool:
        """
        Returns true if the last vertex added to the constructed
        polygonal wire is not coincident with the previous one.
        """

    def Close(self) -> None:
        """
        Closes the polygonal wire under construction. Note - this
        is equivalent to adding the first vertex to the polygonal
        wire under construction.
        """

    def FirstVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def LastVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the first or the last vertex of the polygonal wire under construction.
        If the constructed polygonal wire is closed, the first and the last vertices are identical.
        """

    def IsDone(self) -> bool:
        """
        Returns true if this algorithm contains a valid polygonal
        wire (i.e. if there is at least one edge).
        IsDone returns false if fewer than two vertices have
        been chained together by this construction algorithm.
        """

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge built between the last two points or
        vertices added to the constructed polygonal wire under construction.
        Warning
        If there is only one vertex in the polygonal wire, the result is a null edge.
        """

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the constructed polygonal wire, or the already
        built part of the polygonal wire under construction.
        Exceptions
        StdFail_NotDone if the wire is not built, i.e. if fewer than
        two vertices have been chained together by this construction algorithm.
        """

class BRepBuilderAPI_MakeShapeOnMesh(BRepBuilderAPI_MakeShape):
    """
    Builds shape on per-facet basis on the input mesh. Resulting shape has shared
    edges by construction, but no maximization (unify same domain) is applied.
    No generation history is provided.
    """

    @overload
    def __init__(self, theMesh: nanoocp.Poly.Poly_Triangulation | None) -> None:
        """
        Ctor. Sets mesh to process.
        @param[in] theMesh  - Mesh to construct shape for.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeShapeOnMesh) -> None: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds shape on mesh."""

class BRepBuilderAPI_MakeShell(BRepBuilderAPI_MakeShape):
    """
    Describes functions to build a
    shape corresponding to the skin of a surface.
    Note that the term shell in the class name has the same definition
    as that of a shell in STEP, in other words the skin of a shape,
    and not a solid model defined by surface and thickness. If you want
    to build the second sort of shell, you must use
    BRepOffsetAPI_MakeOffsetShape. A shell is made of a series of
    faces connected by their common edges.
    If the underlying surface of a face is not C2 continuous and
    the flag Segment is True, MakeShell breaks the surface down into
    several faces which are all C2 continuous and which are
    connected along the non-regular curves on the surface.
    The resulting shell contains all these faces.
    Construction of a Shell from a non-C2 continuous Surface
    A MakeShell object provides a framework for:
    -      defining the construction of a shell,
    -      implementing the construction algorithm, and
    -      consulting the result.
    Warning
    The connected C2 faces in the shell resulting from a decomposition of
    the surface are not sewn. For a sewn result, you need to use
    BRepOffsetAPI_Sewing. For a shell with thickness, you need to use
    BRepOffsetAPI_MakeOffsetShape.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty shell framework. The Init
        function is used to define the construction arguments.
        Warning
        The function Error will return
        BRepBuilderAPI_EmptyShell if it is called before the function Init.
        """

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, Segment: bool = False) -> None:
        """Constructs a shell from the surface S."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, Segment: bool = False) -> None:
        """
        Constructs a shell from the surface S,
        limited in the u parametric direction by the two
        parameter values UMin and UMax, and limited in the v
        parametric direction by the two parameter values VMin and VMax.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeShell) -> None: ...

    def Init(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, Segment: bool = False) -> None:
        """
        Defines or redefines the arguments
        for the construction of a shell. The construction is initialized
        with the surface S, limited in the u parametric direction by the
        two parameter values UMin and UMax, and in the v parametric
        direction by the two parameter values VMin and VMax.
        Warning
        The function Error returns:
        -      BRepBuilderAPI_ShellParametersOutOfRange
        when the given parameters are outside the bounds of the
        surface or the basis surface if S is trimmed
        """

    def IsDone(self) -> bool:
        """Returns true if the shell is built."""

    def Error(self) -> BRepBuilderAPI_ShellError:
        """
        Returns the construction status:
        -   BRepBuilderAPI_ShellDone if the shell is built, or
        -   another value of the BRepBuilderAPI_ShellError
        enumeration indicating why the construction failed.
        This is frequently BRepBuilderAPI_ShellParametersOutOfRange
        indicating that the given parameters are outside the bounds of the surface.
        """

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the new Shell."""

class BRepBuilderAPI_MakeSolid(BRepBuilderAPI_MakeShape):
    """
    Describes functions to build a solid from shells.
    A solid is made of one shell, or a series of shells, which
    do not intersect each other. One of these shells
    constitutes the outside skin of the solid. It may be closed
    (a finite solid) or open (an infinite solid). Other shells
    form hollows (cavities) in these previous ones. Each
    must bound a closed volume.
    A MakeSolid object provides a framework for:
    -   defining and implementing the construction of a solid, and
    -   consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes the construction of a solid. An empty solid is
        considered to cover the whole space. The Add function
        is used to define shells to bound it.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_CompSolid) -> None:
        """Make a solid from a CompSolid."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Make a solid from a shell."""

    @overload
    def __init__(self, So: nanoocp.TopoDS.TopoDS_Solid) -> None:
        """Make a solid from a solid. useful for adding later."""

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shell, S2: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Make a solid from two shells."""

    @overload
    def __init__(self, So: nanoocp.TopoDS.TopoDS_Solid, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """
        Add a shell to a solid.

        Constructs a solid:
        -   from the solid So, to which shells can be added, or
        -   by adding the shell S to the solid So.
        Warning
        No check is done to verify the conditions of coherence
        of the resulting solid. In particular S must not intersect the solid S0.
        Besides, after all shells have been added using the Add
        function, one of these shells should constitute the outside
        skin of the solid. It may be closed (a finite solid) or open
        (an infinite solid). Other shells form hollows (cavities) in
        the previous ones. Each must bound a closed volume.
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shell, S2: nanoocp.TopoDS.TopoDS_Shell, S3: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """
        Make a solid from three shells.
        Constructs a solid
        -   covering the whole space, or
        -   from shell S, or
        -   from two shells S1 and S2, or
        -   from three shells S1, S2 and S3, or
        Warning
        No check is done to verify the conditions of coherence
        of the resulting solid. In particular, S1, S2 (and S3) must
        not intersect each other.
        Besides, after all shells have been added using the Add
        function, one of these shells should constitute the outside
        skin of the solid; it may be closed (a finite solid) or open
        (an infinite solid). Other shells form hollows (cavities) in
        these previous ones. Each must bound a closed volume.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeSolid) -> None: ...

    def Add(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """
        Adds the shell to the current solid.
        Warning
        No check is done to verify the conditions of coherence
        of the resulting solid. In particular, S must not intersect
        other shells of the solid under construction.
        Besides, after all shells have been added, one of
        these shells should constitute the outside skin of the
        solid. It may be closed (a finite solid) or open (an
        infinite solid). Other shells form hollows (cavities) in
        these previous ones. Each must bound a closed volume.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the solid is built.
        For this class, a solid under construction is always valid.
        If no shell has been added, it could be a whole-space
        solid. However, no check was done to verify the
        conditions of coherence of the resulting solid.
        """

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the new Solid."""

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

class BRepBuilderAPI_MakeVertex(BRepBuilderAPI_MakeShape):
    """
    Describes functions to build BRepBuilder vertices directly
    from 3D geometric points. A vertex built using a
    MakeVertex object is only composed of a 3D point and
    a default precision value (Precision::Confusion()).
    Later on, 2D representations can be added, for example,
    when inserting a vertex in an edge.
    A MakeVertex object provides a framework for:
    -   defining and implementing the construction of a vertex, and
    -   consulting the result.
    """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a vertex from point P.
        Example create a vertex from a 3D point.
        gp_Pnt P(0,0,10);
        TopoDS_Vertex V = BRepBuilderAPI_MakeVertex(P);
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeVertex) -> None: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the constructed vertex."""

class BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeShape):
    """
    Describes functions to build wires from edges. A wire can
    be built from any number of edges.
    To build a wire you first initialize the construction, then
    add edges in sequence. An unlimited number of edges
    can be added. The initialization of construction is done with:
    -   no edge (an empty wire), or
    -   edges of an existing wire, or
    -   up to four connectable edges.
    In order to be added to a wire under construction, an
    edge (unless it is the first one) must satisfy the following
    condition: one of its vertices must be geometrically
    coincident with one of the vertices of the wire (provided
    that the highest tolerance factor is assigned to the two
    vertices). It could also be the same vertex.
    -   The given edge is shared by the wire if it contains:
    -   two vertices, identical to two vertices of the wire
    under construction (a general case of the wire closure), or
    -   one vertex, identical to a vertex of the wire under
    construction; the other vertex not being
    geometrically coincident with another vertex of the wire.
    -   In other cases, when one of the vertices of the edge
    is simply geometrically coincident with a vertex of the
    wire under construction (provided that the highest
    tolerance factor is assigned to the two vertices), the
    given edge is first copied and the coincident vertex is
    replaced in this new edge, by the coincident vertex of the wire.
    Note: it is possible to build non manifold wires using this construction tool.
    A MakeWire object provides a framework for:
    -   initializing the construction of a wire,
    -   adding edges to the wire under construction, and
    -   consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty wire framework, to which edges
        are added using the Add function.
        As soon as the wire contains one edge, it can return
        with the use of the function Wire.
        Warning
        The function Error will return
        BRepBuilderAPI_EmptyWire if it is called before at
        least one edge is added to the wire under construction.
        """

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from an edge."""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Make a Wire from a Wire. useful for adding later."""

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from two edges."""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Add an edge to a wire."""

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, E3: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from three edges."""

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, E3: nanoocp.TopoDS.TopoDS_Edge, E4: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Make a Wire from four edges.
        Constructs a wire
        -   from the TopoDS_Wire W composed of the edge E, or
        -   from edge E, or
        -   from two edges E1 and E2, or
        -   from three edges E1, E2 and E3, or
        -   from four edges E1, E2, E3 and E4.
        Further edges can be added using the function Add.
        Given edges are added in a sequence. Each of them
        must be connectable to the wire under construction,
        and so must satisfy the following condition (unless it is
        the first edge of the wire): one of its vertices must be
        geometrically coincident with one of the vertices of the
        wire (provided that the highest tolerance factor is
        assigned to the two vertices). It could also be the same vertex.
        Warning
        If an edge is not connectable to the wire under
        construction it is not added. The function Error will
        return BRepBuilderAPI_DisconnectedWire, the
        function IsDone will return false and the function Wire
        will raise an error, until a new connectable edge is added.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_MakeWire) -> None: ...

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Adds the edge E to the wire under construction.
        E must be connectable to the wire under construction, and, unless it
        is the first edge of the wire, must satisfy the following
        condition: one of its vertices must be geometrically coincident
        with one of the vertices of the wire (provided that the highest
        tolerance factor is assigned to the two vertices). It could also
        be the same vertex.
        Warning
        If E is not connectable to the wire under construction it is not
        added. The function Error will return
        BRepBuilderAPI_DisconnectedWire, the function IsDone will return
        false and the function Wire will raise an error, until a new
        connectable edge is added.
        """

    @overload
    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Add the edges of <W> to the current wire."""

    @overload
    def Add(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Adds the edges of <L> to the current wire. The
        edges are not to be consecutive. But they are to
        be all connected geometrically or topologically.
        If some of them are not connected the Status give
        DisconnectedWire but the "Maker" is Done() and you
        can get the partial result.
        (i.e. connected to the first edgeof the list <L>)
        """

    def IsDone(self) -> bool:
        """
        Returns true if this algorithm contains a valid wire.
        IsDone returns false if:
        -   there are no edges in the wire, or
        -   the last edge which you tried to add was not connectable.
        """

    def Error(self) -> BRepBuilderAPI_WireError:
        """
        Returns the construction status
        -   BRepBuilderAPI_WireDone if the wire is built, or
        -   another value of the BRepBuilderAPI_WireError
        enumeration indicating why the construction failed.
        """

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the constructed wire; or the part of the wire
        under construction already built.
        Exceptions StdFail_NotDone if a wire is not built.
        """

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the last edge added to the wire under construction.
        Warning
        -   This edge can be different from the original one (the
        argument of the function Add, for instance,)
        -   A null edge is returned if there are no edges in the
        wire under construction, or if the last edge which you
        tried to add was not connectable..
        """

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the last vertex of the last edge added to the
        wire under construction.
        Warning
        A null vertex is returned if there are no edges in the wire
        under construction, or if the last edge which you tried to
        add was not connectableR
        """

class BRepBuilderAPI_NurbsConvert(BRepBuilderAPI_ModifyShape):
    """
    Conversion of the complete geometry of a shape
    (all 3D analytical representation of surfaces and curves)
    into NURBS geometry (except for Planes). For example,
    all curves supporting edges of the basis shape are converted
    into BSpline curves, and all surfaces supporting its faces are
    converted into BSpline surfaces.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a framework for converting the geometry of a
        shape into NURBS geometry. Use the function Perform
        to define the shape to convert.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, Copy: bool = False) -> None:
        """
        Builds a new shape by converting the geometry of the
        shape S into NURBS geometry. Specifically, all curves
        supporting edges of S are converted into BSpline
        curves, and all surfaces supporting its faces are
        converted into BSpline surfaces.
        Use the function Shape to access the new shape.
        Note: the constructed framework can be reused to
        convert other shapes. You specify these with the
        function Perform.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_NurbsConvert) -> None: ...

    def Perform(self, S: nanoocp.TopoDS.TopoDS_Shape, Copy: bool = False) -> None:
        """
        Builds a new shape by converting the geometry of the
        shape S into NURBS geometry.
        Specifically, all curves supporting edges of S are
        converted into BSpline curves, and all surfaces
        supporting its faces are converted into BSpline surfaces.
        Use the function Shape to access the new shape.
        Note: this framework can be reused to convert other
        shapes: you specify them by calling the function Perform again.
        """

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

    def ModifiedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the modified shape corresponding to <S>.
        S can correspond to the entire initial shape or to its subshape.
        Exceptions
        Standard_NoSuchObject if S is not the initial shape or
        a subshape of the initial shape to which the
        transformation has been applied.
        """

class BRepBuilderAPI_Sewing(nanoocp.Standard.Standard_Transient):
    """
    Provides methods to

    - identify possible contiguous boundaries (for control
    afterwards (of continuity: C0, C1, ...))

    - assemble contiguous shapes into one shape.
    Only manifold shapes will be found. Sewing will not
    be done in case of multiple edges.

    For sewing, use this function as following:
    - create an empty object
    - default tolerance 1.E-06
    - with face analysis on
    - with sewing operation on
    - set the cutting option as you need (default True)
    - define a tolerance
    - add shapes to be sewed -> Add
    - compute -> Perform
    - output the resulted shapes
    - output free edges if necessary
    - output multiple edges if necessary
    - output the problems if any
    """

    @overload
    def __init__(self, tolerance: float = 1e-06, option1: bool = True, option2: bool = True, option3: bool = True, option4: bool = False) -> None:
        """
        Creates an object with
        tolerance of connexity
        option for sewing (if false only control)
        option for analysis of degenerated shapes
        option for cutting of free edges.
        option for non manifold processing
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_Sewing) -> None: ...

    def Init(self, tolerance: float = 1e-06, option1: bool = True, option2: bool = True, option3: bool = True, option4: bool = False) -> None:
        """initialize the parameters if necessary"""

    def Load(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Loads the context shape."""

    def Add(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Defines the shapes to be sewed or controlled"""

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Computing
        theProgress - progress indicator of algorithm
        """

    def SewedShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Gives the sewed shape
        a null shape if nothing constructed
        may be a face, a shell, a solid or a compound
        """

    def SetContext(self, theContext: nanoocp.BRepTools.BRepTools_ReShape | None) -> None:
        """set context"""

    def GetContext(self) -> nanoocp.BRepTools.BRepTools_ReShape:
        """return context"""

    def NbFreeEdges(self) -> int:
        """Gives the number of free edges (edge shared by one face)"""

    def FreeEdge(self, index: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """Gives each free edge"""

    def NbMultipleEdges(self) -> int:
        """
        Gives the number of multiple edges
        (edge shared by more than two faces)
        """

    def MultipleEdge(self, index: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """Gives each multiple edge"""

    def NbContigousEdges(self) -> int:
        """Gives the number of contiguous edges (edge shared by two faces)"""

    def ContigousEdge(self, index: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """Gives each contiguous edge"""

    def ContigousEdgeCouple(self, index: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Gives the sections (edge) belonging to a contiguous edge"""

    def IsSectionBound(self, section: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Indicates if a section is bound (before use SectionToBoundary)"""

    def SectionToBoundary(self, section: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Gives the original edge (free boundary) which becomes the
        the section. Remember that sections constitute common edges.
        This information is important for control because with
        original edge we can find the surface to which the section
        is attached.
        """

    def NbDegeneratedShapes(self) -> int:
        """Gives the number of degenerated shapes"""

    def DegeneratedShape(self, index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives each degenerated shape"""

    def IsDegenerated(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Indicates if a input shape is degenerated"""

    def IsModified(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Indicates if a input shape has been modified"""

    def Modified(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives a modifieded shape"""

    def IsModifiedSubShape(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Indicates if a input subshape has been modified"""

    def ModifiedSubShape(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives a modifieded subshape"""

    def Dump(self) -> None:
        """print the information"""

    def NbDeletedFaces(self) -> int:
        """Gives the number of deleted faces (faces smallest than tolerance)"""

    def DeletedFace(self, index: int) -> nanoocp.TopoDS.TopoDS_Face:
        """Gives each deleted face"""

    def WhichFace(self, theEdg: nanoocp.TopoDS.TopoDS_Edge, index: int = 1) -> nanoocp.TopoDS.TopoDS_Face:
        """Gives a modified shape"""

    def SameParameterMode(self) -> bool:
        """Gets same parameter mode."""

    def SetSameParameterMode(self, SameParameterMode: bool) -> None:
        """Sets same parameter mode."""

    def Tolerance(self) -> float:
        """Gives set tolerance."""

    def SetTolerance(self, theToler: float) -> None:
        """Sets tolerance"""

    def MinTolerance(self) -> float:
        """Gives set min tolerance."""

    def SetMinTolerance(self, theMinToler: float) -> None:
        """Sets min tolerance"""

    def MaxTolerance(self) -> float:
        """Gives set max tolerance"""

    def SetMaxTolerance(self, theMaxToler: float) -> None:
        """Sets max tolerance."""

    def FaceMode(self) -> bool:
        """Returns mode for sewing faces By default - true."""

    def SetFaceMode(self, theFaceMode: bool) -> None:
        """Sets mode for sewing faces By default - true."""

    def FloatingEdgesMode(self) -> bool:
        """Returns mode for sewing floating edges By default - false."""

    def SetFloatingEdgesMode(self, theFloatingEdgesMode: bool) -> None:
        """
        Sets mode for sewing floating edges By default - false.
        Returns mode for cutting floating edges By default - false.
        Sets mode for cutting floating edges By default - false.
        """

    def LocalTolerancesMode(self) -> bool:
        """
        Returns mode for accounting of local tolerances
        of edges and vertices during of merging.
        """

    def SetLocalTolerancesMode(self, theLocalTolerancesMode: bool) -> None:
        """
        Sets mode for accounting of local tolerances
        of edges and vertices during of merging
        in this case WorkTolerance = myTolerance + tolEdge1+ tolEdg2;
        """

    def SetNonManifoldMode(self, theNonManifoldMode: bool) -> None:
        """Sets mode for non-manifold sewing."""

    def NonManifoldMode(self) -> bool:
        """
        Gets mode for non-manifold sewing.

        INTERNAL FUNCTIONS ---
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBuilderAPI_Transform(BRepBuilderAPI_ModifyShape):
    """
    Geometric transformation on a shape.
    The transformation to be applied is defined as a
    gp_Trsf transformation, i.e. a transformation which does
    not modify the underlying geometry of shapes.
    The transformation is applied to:
    -   all curves which support edges of a shape, and
    -   all surfaces which support its faces.
    A Transform object provides a framework for:
    -   defining the geometric transformation to be applied,
    -   implementing the transformation algorithm, and
    -   consulting the results.
    """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Constructs a framework for applying the geometric
        transformation T to a shape. Use the function Perform
        to define the shape to transform.
        """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theTrsf: nanoocp.gp.gp_Trsf, theCopyGeom: bool = False, theCopyMesh: bool = False) -> None:
        """
        Creates a transformation from the gp_Trsf <theTrsf>, and
        applies it to the shape <theShape>. If the transformation
        is direct and isometric (determinant = 1) and
        <theCopyGeom> = false, the resulting shape is
        <theShape> on which a new location has been set.
        Otherwise, the transformation is applied on a
        duplication of <theShape>.
        If <theCopyMesh> is true, the triangulation will be copied,
        and the copy will be assigned to the result shape.
        """

    @overload
    def __init__(self, theOther: BRepBuilderAPI_Transform) -> None: ...

    def Perform(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theCopyGeom: bool = False, theCopyMesh: bool = False) -> None:
        """
        Applies the geometric transformation defined at the
        time of construction of this framework to the shape S.
        - If the transformation T is direct and isometric, in
        other words, if the determinant of the vectorial part
        of T is equal to 1., and if theCopyGeom equals false (the
        default value), the resulting shape is the same as
        the original but with a new location assigned to it.
        - In all other cases, the transformation is applied to a duplicate of theShape.
        - If theCopyMesh is true, the triangulation will be copied,
        and the copy will be assigned to the result shape.
        Use the function Shape to access the result.
        Note: this framework can be reused to apply the same
        geometric transformation to other shapes. You only
        need to specify them by calling the function Perform again.
        """

    def ModifiedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the modified shape corresponding to <S>."""

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

class BRepBuilderAPI_VertexInspector:
    """
    Inspector for CellFilter algorithm working with gp_XYZ points in 3d space.
    Used in search of coincidence points with a certain tolerance.
    """

    @overload
    def __init__(self, theTol: float) -> None:
        """Constructor; remembers the tolerance"""

    @overload
    def __init__(self, theOther: BRepBuilderAPI_VertexInspector) -> None: ...

    @staticmethod
    def Coord(i: int, thePnt: nanoocp.gp.gp_XYZ) -> float: ...

    @staticmethod
    def Shift(thePnt: nanoocp.gp.gp_XYZ, theTol: float) -> nanoocp.gp.gp_XYZ: ...

    def Add(self, thePnt: nanoocp.gp.gp_XYZ) -> None:
        """Keep the points used for comparison"""

    def ClearResList(self) -> None:
        """Clear the list of adjacent points"""

    def SetCurrent(self, theCurPnt: nanoocp.gp.gp_XYZ) -> None:
        """Set current point to search for coincidence"""

    def ResInd(self) -> nanoocp.NCollection.NCollection_List[int]:
        """Get list of indexes of points adjacent with the current"""

    def Inspect(self, theTarget: int) -> nanoocp.NCollection.NCollection_CellFilter_Action:
        """Implementation of inspection method"""

# C++ typedef aliases
VectorOfPoint = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.gp.gp_XYZ]
