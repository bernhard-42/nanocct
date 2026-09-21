"""OCCT package ShapeFix (toolkit TKShHealing)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeAnalysis
import nanoocp.ShapeBuild
import nanoocp.ShapeConstruct
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS


class ShapeFix:
    """
    This package provides algorithms for fixing
    problematic (violating Open CASCADE requirements) shapes.
    Tools from package ShapeAnalysis are used for detecting the problems. The
    detecting and fixing is done taking in account various
    criteria implemented in BRepCheck package.
    Each class of package ShapeFix deals with one
    certain type of shapes or with some family of problems.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix) -> None: ...

    @staticmethod
    def SameParameter(shape: nanoocp.TopoDS.TopoDS_Shape, enforce: bool, preci: float = 0.0, theProgress: nanoocp.Message.Message_ProgressRange = ..., theMsgReg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None = None) -> bool:
        """
        Runs SameParameter from BRepLib with these adaptations :
        <enforce> forces computations, else they are made only on
        Edges with flag SameParameter false
        <preci>, if not precised, is taken for each EDge as its own
        Tolerance
        Returns True when done, False if an exception has been raised
        In case of exception anyway, as many edges as possible have
        been processed. The passed progress indicator allows user
        to consult the current progress stage and abort algorithm
        if needed.
        """

    @staticmethod
    def EncodeRegularity(shape: nanoocp.TopoDS.TopoDS_Shape, tolang: float = 1e-10) -> None:
        """
        Runs EncodeRegularity from BRepLib taking into account
        shared components of assemblies, so that each component
        is processed only once
        """

    @staticmethod
    def RemoveSmallEdges(shape: nanoocp.TopoDS.TopoDS_Shape, Tolerance: float) -> tuple[nanoocp.TopoDS.TopoDS_Shape, nanoocp.ShapeBuild.ShapeBuild_ReShape]:
        """
        Removes edges which are less than given tolerance from shape
        with help of ShapeFix_Wire::FixSmall()
        """

    @staticmethod
    def FixVertexPosition(theshape: nanoocp.TopoDS.TopoDS_Shape, theTolerance: float, thecontext: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> bool:
        """
        Fix position of the vertices having tolerance more tnan specified one.;
        """

    @staticmethod
    def LeastEdgeSize(theshape: nanoocp.TopoDS.TopoDS_Shape) -> float:
        """Calculate size of least edge;"""

class ShapeFix_Root(nanoocp.Standard.Standard_Transient):
    """
    Root class for fixing operations
    Provides context for recording changes (optional),
    basic precision value and limit (minimal and
    maximal) values for tolerances,
    and message registrator
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor (no context is created)"""

    @overload
    def __init__(self, theOther: ShapeFix_Root) -> None: ...

    def Set(self, Root: ShapeFix_Root | None) -> None:
        """Copy all fields from another Root object"""

    def SetContext(self, context: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> None:
        """Sets context"""

    def Context(self) -> nanoocp.ShapeBuild.ShapeBuild_ReShape:
        """Returns context"""

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def MsgRegistrator(self) -> nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator:
        """Returns message registrator"""

    def SetPrecision(self, preci: float) -> None:
        """Sets basic precision value"""

    def Precision(self) -> float:
        """Returns basic precision value"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance"""

    def MinTolerance(self) -> float:
        """Returns minimal allowed tolerance"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance"""

    def MaxTolerance(self) -> float:
        """Returns maximal allowed tolerance"""

    def LimitTolerance(self, toler: float) -> float:
        """Returns tolerance limited by [myMinTol,myMaxTol]"""

    @overload
    def SendMsg(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity = Message_Gravity.Message_Info) -> None:
        """
        Sends a message to be attached to the shape.
        Calls corresponding message of message registrator.
        """

    @overload
    def SendMsg(self, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity = Message_Gravity.Message_Info) -> None:
        """
        Sends a message to be attached to myShape.
        Calls previous method.
        """

    @overload
    def SendWarning(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg) -> None:
        """
        Sends a warning to be attached to the shape.
        Calls SendMsg with gravity set to Message_Warning.
        """

    @overload
    def SendWarning(self, message: nanoocp.Message.Message_Msg) -> None:
        """Calls previous method for myShape."""

    @overload
    def SendFail(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg) -> None:
        """
        Sends a fail to be attached to the shape.
        Calls SendMsg with gravity set to Message_Fail.
        """

    @overload
    def SendFail(self, message: nanoocp.Message.Message_Msg) -> None:
        """Calls previous method for myShape."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_WireSegment:
    """
    This class is auxiliary class (data storage) used in ComposeShell.
    It is intended for representing segment of the wire
    (or whole wire). The segment itself is represented by
    ShapeExtend_WireData. In addition, some associated data
    necessary for computations are stored:

    * Orientation flag - determines current use of the segment
    and used for parity checking:

    TopAbs_FORWARD and TopAbs_REVERSED - says that segment was
    traversed once in the corresponding direction, and hence
    it should be traversed once more in opposite direction;

    TopAbs_EXTERNAL - the segment was not yet traversed in any
    direction (i.e. not yet used as boundary)

    TopAbs_INTERNAL - the segment was traversed in both
    directions and hence is out of further work.

    Segments of initial bounding wires are created with
    orientation REVERSED (for outer wire) or FORWARD (for inner
    wires), and segments of splitting seams - with orientation
    EXTERNAL.
    """

    @overload
    def __init__(self) -> None:
        """Creates empty segment."""

    @overload
    def __init__(self, wire: nanoocp.ShapeExtend.ShapeExtend_WireData | None, ori: nanoocp.TopAbs.TopAbs_Orientation = TopAbs_Orientation.TopAbs_EXTERNAL) -> None:
        """Creates segment and initializes it with wire and orientation."""

    @overload
    def __init__(self, theOther: ShapeFix_WireSegment) -> None: ...

    def Clear(self) -> None:
        """Clears all fields."""

    def Load(self, wire: nanoocp.ShapeExtend.ShapeExtend_WireData | None) -> None:
        """Loads wire."""

    def WireData(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """Returns wire."""

    @overload
    def Orientation(self, ori: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Sets orientation flag."""

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns orientation flag."""

    def FirstVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns first vertex of the first edge in the wire
        (no dependence on Orientation()).
        """

    def LastVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns last vertex of the last edge in the wire
        (no dependence on Orientation()).
        """

    def IsClosed(self) -> bool:
        """Returns True if FirstVertex() == LastVertex()"""

    def NbEdges(self) -> int:
        """Returns Number of edges in the wire"""

    def Edge(self, i: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns edge by given index in the wire"""

    def SetEdge(self, i: int, edge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Replaces edge at index i by new one."""

    @overload
    def AddEdge(self, i: int, edge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Insert a new edge with index i and implicitly defined
        patch indices (indefinite patch).
        If i==0, edge is inserted at end of wire.
        """

    @overload
    def AddEdge(self, i: int, edge: nanoocp.TopoDS.TopoDS_Edge, iumin: int, iumax: int, ivmin: int, ivmax: int) -> None:
        """
        Insert a new edge with index i and explicitly defined
        patch indices. If i==0, edge is inserted at end of wire.
        """

    def SetPatchIndex(self, i: int, iumin: int, iumax: int, ivmin: int, ivmax: int) -> None:
        """Set patch indices for edge i."""

    def DefineIUMin(self, i: int, iumin: int) -> None: ...

    def DefineIUMax(self, i: int, iumax: int) -> None: ...

    def DefineIVMin(self, i: int, ivmin: int) -> None: ...

    def DefineIVMax(self, i: int, ivmax: int) -> None:
        """
        Modify minimal or maximal patch index for edge i.
        The corresponding patch index for that edge is modified so
        as to satisfy eq. iumin <= myIUMin(i) <= myIUMax(i) <= iumax
        """

    def GetPatchIndex(self, i: int) -> tuple[int, int, int, int]:
        """Returns patch indices for edge i."""

    def CheckPatchIndex(self, i: int) -> bool:
        """
        Checks patch indices for edge i to satisfy equations
        IUMin(i) <= IUMax(i) <= IUMin(i)+1
        """

    def SetVertex(self, theVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def GetVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def IsVertex(self) -> bool: ...

class ShapeFix_ComposeShell(ShapeFix_Root):
    """
    This class is intended to create a shell from the composite
    surface (grid of surfaces) and set of wires.
    It may be either division of the supporting surface of the
    face, or creating a shape corresponding to face on composite
    surface which is missing in CAS.CADE but exists in some other
    systems.

    It splits (if necessary) original face to several ones by
    splitting lines which are joint lines on a supplied grid of
    surfaces (U- and V- isolines of the composite surface).
    There are two modes of work, which differ in the way of
    handling faces on periodic surfaces:

    - if ClosedMode is False (default), when splitting itself is
    done as if surface were not periodic. The periodicity of the
    underlying surface is taken into account by duplicating splitting
    lines in the periodic direction, as necessary to split all
    the wires (whole parametrical range of a face)
    In this mode, some regularization procedures are performed
    (indexation of split segments by patch numbers), and it is
    expected to be more reliable and robust in case of bad shapes

    - if ClosedMode is True, when everything on a periodic surfaces
    is considered as modulo period. This allows to deal with wires
    which are closed in 3d but not in 2d, with wires which may be
    shifted on several periods in 2d etc. However, this mode is
    less reliable since some regularizations do not work for it.

    The work is made basing on pcurves of the edges. These pcurves
    should already exist (for example, in the case of division of
    existing face), then they are taken as is. The existing pcurves
    should be assigned to one surface (face) for all edges,
    this surface (face) will be used only for accessing pcurves,
    and it may have any geometry.

    All the modifications are recorded in the context tool
    (ShapeBuild_ReShape).
    """

    @overload
    def __init__(self) -> None:
        """Creates empty tool."""

    @overload
    def __init__(self, theOther: ShapeFix_ComposeShell) -> None: ...

    def Init(self, Grid: nanoocp.ShapeExtend.ShapeExtend_CompositeSurface | None, L: nanoocp.TopLoc.TopLoc_Location, Face: nanoocp.TopoDS.TopoDS_Face, Prec: float) -> None:
        """
        Initializes with composite surface, face and precision.
        Here face defines both set of wires and way of getting
        pcurves. Precision is used (together with tolerance of edges)
        for handling subtle cases, such as tangential intersections.
        """

    def ClosedMode(self) -> bool:
        """
        Returns (modifiable) flag for special 'closed'
        mode which forces ComposeShell to consider
        all pcurves on closed surface as modulo period.
        This can reduce reliability, but allows to deal
        with wires closed in 3d but open in 2d (missing seam)
        Default is False
        """

    def SetClosedMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ClosedMode() returns by reference in C++.
        """

    def Perform(self) -> bool:
        """Performs the work on already loaded data."""

    def SplitEdges(self) -> None:
        """
        Splits edges in the original shape by grid.
        This is a part of Perform() which does not produce any
        resulting shape; the only result is filled context
        where splittings are recorded.

        NOTE: If edge is split, it is replaced by wire, and
        order of edges in the wire corresponds to FORWARD orientation
        of the edge.
        """

    def Result(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns resulting shell or face (or Null shape if not done)"""

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries status of last call to Perform()
        OK   : nothing done (some kind of error)
        DONE1: splitting is done, at least one new face created
        DONE2: splitting is done, several new faces obtained
        FAIL1: misoriented wire encountered (handled)
        FAIL2: recoverable parity error
        FAIL3: edge with no pcurve on supporting face
        FAIL4: unrecoverable algorithm error (parity check)
        """

    def DispatchWires(self, faces: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape], wires: nanoocp.NCollection.NCollection_Sequence[nanoocp.ShapeFix.ShapeFix_WireSegment]) -> None:
        """
        Creates new faces from the set of (closed) wires. Each wire
        is put on corresponding patch in the composite surface,
        and all pcurves on the initial (pseudo)face are reassigned to
        that surface. If several wires are one inside another, single
        face is created.
        """

    def SetTransferParamTool(self, TransferParam: nanoocp.ShapeAnalysis.ShapeAnalysis_TransferParameters | None) -> None:
        """Sets tool for transfer parameters from 3d to 2d and vice versa."""

    def GetTransferParamTool(self) -> nanoocp.ShapeAnalysis.ShapeAnalysis_TransferParameters:
        """Gets tool for transfer parameters from 3d to 2d and vice versa."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_Edge(nanoocp.Standard.Standard_Transient):
    """
    Fixing invalid edge.
    Geometrical and/or topological inconsistency:
    - no 3d curve or pcurve,
    - mismatching orientation of 3d curve and pcurve,
    - incorrect SameParameter flag (curve deviation is greater than
    edge tolerance),
    - not adjacent curves (3d or pcurve) to the vertices.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeFix_Edge) -> None: ...

    def Projector(self) -> nanoocp.ShapeConstruct.ShapeConstruct_ProjectCurveOnSurface:
        """
        Returns the projector used for recomputing missing pcurves
        Can be used for adjusting parameters of projector
        """

    @overload
    def FixRemovePCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    def FixRemovePCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Removes the pcurve(s) of the edge if it does not match the
        vertices
        Check is done
        Use    : It is to be called when pcurve of an edge can be wrong
        (e.g., after import from IGES)
        Returns: True, if does not match, removed (status DONE)
        False, (status OK) if matches or (status FAIL) if no pcurve,
        nothing done
        """

    def FixRemoveCurve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Removes 3d curve of the edge if it does not match the vertices
        Returns: True, if does not match, removed (status DONE)
        False, (status OK) if matches or (status FAIL) if no 3d curve,
        nothing done
        """

    @overload
    def FixAddPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, isSeam: bool, prec: float = 0.0) -> bool: ...

    @overload
    def FixAddPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location, isSeam: bool, prec: float = 0.0) -> bool: ...

    @overload
    def FixAddPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, isSeam: bool, surfana: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None, prec: float = 0.0) -> bool:
        """See method below for information"""

    @overload
    def FixAddPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location, isSeam: bool, surfana: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None, prec: float = 0.0) -> bool:
        """
        Adds pcurve(s) of the edge if missing (by projecting 3d curve)
        Parameter isSeam indicates if the edge is a seam.
        The parameter <prec> defines the precision for calculations.
        If it is 0 (default), the tolerance of the edge is taken.
        Remark : This method is rather for internal use since it accepts parameter
        <surfana> for optimization of computations
        Use    : It is to be called after FixRemovePCurve (if removed) or in any
        case when edge can have no pcurve
        Returns: True if pcurve was added, else False
        Status :
        OK   : Pcurve exists
        FAIL1: No 3d curve
        FAIL2: fail during projecting
        DONE1: Pcurve was added
        DONE2: specific case of pcurve going through degenerated point on
        sphere encountered during projection (see class
        ShapeConstruct_ProjectCurveOnSurface for more info)
        """

    def FixAddCurve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Tries to build 3d curve of the edge if missing
        Use    : It is to be called after FixRemoveCurve3d (if removed) or in any
        case when edge can have no 3d curve
        Returns: True if 3d curve was added, else False
        Status :
        OK   : 3d curve exists
        FAIL1: BRepLib::BuildCurve3d() has failed
        DONE1: 3d curve was added
        """

    @overload
    def FixVertexTolerance(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    def FixVertexTolerance(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Increases the tolerances of the edge vertices to comprise
        the ends of 3d curve and pcurve on the given face
        (first method) or all pcurves stored in an edge (second one)
        Returns: True, if tolerances have been increased, otherwise False
        Status:
        OK   : the original tolerances have not been changed
        DONE1: the tolerance of first vertex has been increased
        DONE2: the tolerance of last vertex has been increased
        """

    @overload
    def FixReversed2d(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    def FixReversed2d(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Fixes edge if pcurve is directed opposite to 3d curve
        Check is done by call to the function
        ShapeAnalysis_Edge::CheckCurve3dWithPCurve()
        Warning: For seam edge this method will check and fix the pcurve in only
        one direction. Hence, it should be called twice for seam edge:
        once with edge orientation FORWARD and once with REVERSED.
        Returns: False if nothing done, True if reversed (status DONE)
        Status:  OK    - pcurve OK, nothing done
        FAIL1 - no pcurve
        FAIL2 - no 3d curve
        DONE1 - pcurve was reversed
        """

    @overload
    def FixSameParameter(self, edge: nanoocp.TopoDS.TopoDS_Edge, tolerance: float = 0.0) -> bool: ...

    @overload
    def FixSameParameter(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, tolerance: float = 0.0) -> bool:
        """
        Tries to make edge SameParameter and sets corresponding
        tolerance and SameParameter flag.
        First, it makes edge same range if SameRange flag is not set.

        If flag SameParameter is set, this method calls the
        function ShapeAnalysis_Edge::CheckSameParameter() that
        calculates the maximal deviation of pcurves of the edge from
        its 3d curve. If deviation > tolerance, the tolerance of edge
        is increased to a value of deviation. If deviation < tolerance
        nothing happens.

        If flag SameParameter is not set, this method chooses the best
        variant (one that has minimal tolerance), either
        a. only after computing deviation (as above) or
        b. after calling standard procedure BRepLib::SameParameter
        and computing deviation (as above). If <tolerance> > 0, it is
        used as parameter for BRepLib::SameParameter, otherwise,
        tolerance of the edge is used.

        Use    : Is to be called after all pcurves and 3d curve of the edge are
        correctly computed
        Remark : SameParameter flag is always set to True after this method
        Returns: True, if something done, else False
        Status : OK    - edge was initially SameParameter, nothing is done
        FAIL1 - computation of deviation of pcurves from 3d curve has failed
        FAIL2 - BRepLib::SameParameter() has failed
        DONE1 - tolerance of the edge was increased
        DONE2 - flag SameParameter was set to True (only if
        BRepLib::SameParameter() did not set it)
        DONE3 - edge was modified by BRepLib::SameParameter() to SameParameter
        DONE4 - not used anymore
        DONE5 - if the edge resulting from BRepLib has been chosen, i.e. variant b. above
        (only for edges with not set SameParameter)
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """Returns the status (in the form of True/False) of last Fix"""

    def SetContext(self, context: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> None:
        """Sets context"""

    def Context(self) -> nanoocp.ShapeBuild.ShapeBuild_ReShape:
        """Returns context"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_EdgeConnect:
    """
    Rebuilds edges to connect with new vertices, was moved from ShapeBuild.
    Makes vertices to be shared to connect edges,
    updates positions and tolerances for shared vertices.
    Accepts edges bounded by two vertices each.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_EdgeConnect) -> None: ...

    @overload
    def Add(self, aFirst: nanoocp.TopoDS.TopoDS_Edge, aSecond: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Adds information on connectivity between start vertex
        of second edge and end vertex of first edge,
        taking edges orientation into account
        """

    @overload
    def Add(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Adds connectivity information for the whole shape.
        Note: edges in wires must be well ordered
        Note: flag Closed should be set for closed wires
        """

    def Build(self) -> None:
        """Builds shared vertices, updates their positions and tolerances"""

    def Clear(self) -> None:
        """Clears internal data structure"""

class ShapeFix_EdgeProjAux(nanoocp.Standard.Standard_Transient):
    """
    Project 3D point (vertex) on pcurves to find Vertex Parameter
    on parametric representation of an edge
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_EdgeProjAux) -> None: ...

    def Init(self, F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def Compute(self, preci: float) -> None: ...

    def IsFirstDone(self) -> bool: ...

    def IsLastDone(self) -> bool: ...

    def FirstParam(self) -> float: ...

    def LastParam(self) -> float: ...

    def IsIso(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_Face(ShapeFix_Root):
    """
    This operator allows to perform various fixes on face
    and its wires: fixes provided by ShapeFix_Wire,
    fixing orientation of wires, addition of natural bounds,
    fixing of missing seam edge,
    and detection and removal of null-area wires
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Creates a tool and loads a face"""

    @overload
    def __init__(self, theOther: ShapeFix_Face) -> None: ...

    def ClearModes(self) -> None:
        """Sets all modes to default"""

    @overload
    def Init(self, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Loads a whole face already created, with its wires, sense and
        location
        """

    @overload
    def Init(self, surf: nanoocp.Geom.Geom_Surface | None, preci: float, fwd: bool = True) -> None: ...

    @overload
    def Init(self, surf: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None, preci: float, fwd: bool = True) -> None:
        """
        Starts the creation of the face
        By default it will be FORWARD, or REVERSED if <fwd> is False
        """

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def SetPrecision(self, preci: float) -> None:
        """Sets basic precision value (also to FixWireTool)"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance (also to FixWireTool)"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance (also to FixWireTool)"""

    def FixWireMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Wire, by default True.
        """

    def SetFixWireMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixWireMode() returns by reference in C++.
        """

    def FixOrientationMode(self) -> int:
        """
        Returns (modifiable) the fix orientation mode, by default
        True. If True, wires oriented to border limited square.
        """

    def SetFixOrientationMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixOrientationMode() returns by reference in C++.
        """

    def FixAddNaturalBoundMode(self) -> int:
        """
        Returns (modifiable) the add natural bound mode.
        If true, natural boundary is added on faces that miss them.
        Default is False for faces with single wire (they are
        handled by FixOrientation in that case) and True for others.
        """

    def SetFixAddNaturalBoundMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixAddNaturalBoundMode() returns by reference in C++.
        """

    def FixMissingSeamMode(self) -> int:
        """
        Returns (modifiable) the fix missing seam mode, by default
        True. If True, tries to insert seam is missed.
        """

    def SetFixMissingSeamMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixMissingSeamMode() returns by reference in C++.
        """

    def FixSmallAreaWireMode(self) -> int:
        """
        Returns (modifiable) the fix small area wire mode, by default
        False. If True, drops small wires.
        """

    def SetFixSmallAreaWireMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSmallAreaWireMode() returns by reference in C++.
        """

    def RemoveSmallAreaFaceMode(self) -> int:
        """
        Returns (modifiable) the remove face with small area, by default
        False. If True, drops faces with small outer wires.
        """

    def SetRemoveSmallAreaFaceMode(self, theValue: int) -> None:
        """
        Python addition: sets the value RemoveSmallAreaFaceMode() returns by reference in C++.
        """

    def FixIntersectingWiresMode(self) -> int:
        """
        Returns (modifiable) the fix intersecting wires mode
        by default True.
        """

    def SetFixIntersectingWiresMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixIntersectingWiresMode() returns by reference in C++.
        """

    def FixLoopWiresMode(self) -> int:
        """
        Returns (modifiable) the fix loop wires mode
        by default True.
        """

    def SetFixLoopWiresMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixLoopWiresMode() returns by reference in C++.
        """

    def FixSplitFaceMode(self) -> int:
        """
        Returns (modifiable) the fix split face mode
        by default True.
        """

    def SetFixSplitFaceMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSplitFaceMode() returns by reference in C++.
        """

    def AutoCorrectPrecisionMode(self) -> int:
        """
        Returns (modifiable) the auto-correct precision mode
        by default False.
        """

    def SetAutoCorrectPrecisionMode(self, theValue: int) -> None:
        """
        Python addition: sets the value AutoCorrectPrecisionMode() returns by reference in C++.
        """

    def FixPeriodicDegeneratedMode(self) -> int:
        """
        Returns (modifiable) the activation flag for periodic
        degenerated fix. False by default.
        """

    def SetFixPeriodicDegeneratedMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixPeriodicDegeneratedMode() returns by reference in C++.
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns a face which corresponds to the current state
        Warning: The finally produced face may be another one ... but with the
        same support
        """

    def Result(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns resulting shape (Face or Shell if split)
        To be used instead of Face() if FixMissingSeam involved
        """

    def Add(self, wire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Add a wire to current face using BRep_Builder.
        Wire is added without taking into account orientation of face
        (as if face were FORWARD).
        """

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Performs all the fixes, depending on modes
        Function Status returns the status of last call to Perform()
        ShapeExtend_OK   : face was OK, nothing done
        ShapeExtend_DONE1: some wires are fixed
        ShapeExtend_DONE2: orientation of wires fixed
        ShapeExtend_DONE3: missing seam added
        ShapeExtend_DONE4: small area wire removed
        ShapeExtend_DONE5: natural bounds added
        ShapeExtend_FAIL1: some fails during fixing wires
        ShapeExtend_FAIL2: cannot fix orientation of wires
        ShapeExtend_FAIL3: cannot add missing seam
        ShapeExtend_FAIL4: cannot remove small area wire
        """

    @overload
    def FixOrientation(self) -> bool:
        """
        Fixes orientation of wires on the face
        It tries to make all wires lie outside all others (according
        to orientation) by reversing orientation of some of them.
        If face lying on sphere or torus has single wire and
        AddNaturalBoundMode is True, that wire is not reversed in
        any case (supposing that natural bound will be added).
        Returns True if wires were reversed
        """

    @overload
    def FixOrientation(self, MapWires: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Fixes orientation of wires on the face
        It tries to make all wires lie outside all others (according
        to orientation) by reversing orientation of some of them.
        If face lying on sphere or torus has single wire and
        AddNaturalBoundMode is True, that wire is not reversed in
        any case (supposing that natural bound will be added).
        Returns True if wires were reversed
        OutWires return information about out wires + list of
        internal wires for each (for performing split face).
        """

    def FixAddNaturalBound(self) -> bool:
        """
        Adds natural boundary on face if it is missing.
        Two cases are supported:
        - face has no wires
        - face lies on geometrically double-closed surface
        (sphere or torus) and none of wires is left-oriented
        Returns True if natural boundary was added
        """

    def FixMissingSeam(self) -> bool:
        """
        Detects and fixes the special case when face on a closed
        surface is given by two wires closed in 3d but with gap in 2d.
        In that case it creates a new wire from the two, and adds a
        missing seam edge
        Returns True if missing seam was added
        """

    def FixSmallAreaWire(self, theIsRemoveSmallFace: bool) -> bool:
        """
        Detects wires with small area (that is less than
        100*Precision::PConfusion(). Removes these wires if they are internal.
        Returns : True if at least one small wire removed,
        False if does nothing.
        """

    def FixLoopWire(self, aResWires: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Detects if wire has a loop and fixes this situation by splitting on the few parts.
        if wire has a loops and it was split Status was set to value ShapeExtend_DONE6.
        """

    def FixIntersectingWires(self) -> bool:
        """
        Detects and fixes the special case when face has more than one wire
        and this wires have intersection point
        """

    def FixWiresTwoCoincEdges(self) -> bool:
        """
        If wire contains two coincidence edges it must be removed
        Queries on status after Perform()
        """

    def FixSplitFace(self, MapWires: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Split face if there are more than one out wire
        using inrormation after FixOrientation()
        """

    def FixPeriodicDegenerated(self) -> bool:
        """
        Fixes topology for a specific case when face is composed
        by a single wire belting a periodic surface. In that case
        a degenerated edge is reconstructed in the degenerated pole
        of the surface. Initial wire gets consistent orientation.
        Must be used in couple and before FixMissingSeam routine
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Returns the status of last call to Perform()
        ShapeExtend_OK   : face was OK, nothing done
        ShapeExtend_DONE1: some wires are fixed
        ShapeExtend_DONE2: orientation of wires fixed
        ShapeExtend_DONE3: missing seam added
        ShapeExtend_DONE4: small area wire removed
        ShapeExtend_DONE5: natural bounds added
        ShapeExtend_DONE8: face may be splited
        ShapeExtend_FAIL1: some fails during fixing wires
        ShapeExtend_FAIL2: cannot fix orientation of wires
        ShapeExtend_FAIL3: cannot add missing seam
        ShapeExtend_FAIL4: cannot remove small area wire
        """

    def FixWireTool(self) -> ShapeFix_Wire:
        """Returns tool for fixing wires."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_FaceConnect:
    """Rebuilds connectivity between faces in shell"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_FaceConnect) -> None: ...

    def Add(self, aFirst: nanoocp.TopoDS.TopoDS_Face, aSecond: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    def Build(self, shell: nanoocp.TopoDS.TopoDS_Shell, sewtoler: float, fixtoler: float) -> nanoocp.TopoDS.TopoDS_Shell: ...

    def Clear(self) -> None:
        """Clears internal data structure"""

class ShapeFix_FixSmallFace(ShapeFix_Root):
    """Fixing face with small size"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_FixSmallFace) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Perform(self) -> None:
        """Fixing case of spot face"""

    def FixSpotFace(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Fixing case of spot face, if tol = -1 used local tolerance."""

    def ReplaceVerticesInCaseOfSpot(self, F: nanoocp.TopoDS.TopoDS_Face, tol: float) -> bool:
        """Compute average vertex and replacing vertices by new one."""

    def RemoveFacesInCaseOfSpot(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Remove spot face from compound"""

    def FixStripFace(self, wasdone: bool = False) -> nanoocp.TopoDS.TopoDS_Shape:
        """Fixing case of strip face, if tol = -1 used local tolerance"""

    def ReplaceInCaseOfStrip(self, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, tol: float) -> bool:
        """Replace veretces and edges."""

    def RemoveFacesInCaseOfStrip(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Remove strip face from compound."""

    def ComputeSharedEdgeForStripFace(self, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, tol: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """Compute average edge for strip face"""

    def FixSplitFace(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def SplitOneFace(self, F: nanoocp.TopoDS.TopoDS_Face, theSplittedFaces: nanoocp.TopoDS.TopoDS_Compound) -> bool:
        """Compute data for face splitting."""

    def FixFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopoDS.TopoDS_Face: ...

    def FixShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def FixPinFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_FixSmallSolid(ShapeFix_Root):
    """Fixing solids with small size"""

    @overload
    def __init__(self) -> None:
        """Construct"""

    @overload
    def __init__(self, theOther: ShapeFix_FixSmallSolid) -> None: ...

    def SetFixMode(self, theMode: int) -> None:
        """
        Set working mode for operator:
        - theMode = 0 use both WidthFactorThreshold and VolumeThreshold parameters
        - theMode = 1 use only WidthFactorThreshold parameter
        - theMode = 2 use only VolumeThreshold parameter
        """

    def SetVolumeThreshold(self, theThreshold: float = -1.0) -> None:
        """Set or clear volume threshold for small solids"""

    def SetWidthFactorThreshold(self, theThreshold: float = -1.0) -> None:
        """Set or clear width factor threshold for small solids"""

    def Remove(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theContext: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Remove small solids from the given shape"""

    def Merge(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theContext: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Merge small solids in the given shape to adjacent non-small ones"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_FreeBounds:
    """
    This class is intended to output free bounds of the shape
    (free bounds are the wires consisting of edges referenced by the
    only face).
    For building free bounds it uses ShapeAnalysis_FreeBounds class.
    This class complements it with the feature to reduce the number
    of open wires.
    This reduction is performed with help of connecting several
    adjacent open wires one to another what can lead to:
    1. making an open wire with greater length out of several
    open wires
    2. making closed wire out of several open wires

    The connecting open wires is performed with a user-given
    tolerance.

    When connecting several open wires into one wire their previous
    end vertices are replaced with new connecting vertices. After
    that all the edges in the shape sharing previous vertices inside
    the shape are updated with new vertices. Thus source shape can
    be modified.

    Since interface of this class is the same as one of
    ShapeAnalysis_FreeBounds refer to its CDL for details.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape, closetoler: float, splitclosed: bool, splitopen: bool) -> None:
        """
        Builds actual free bounds of the <shape> and connects
        open wires with tolerance <closetoler>.
        <shape> should be a compound of shells.
        """

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape, sewtoler: float, closetoler: float, splitclosed: bool, splitopen: bool) -> None:
        """
        Builds forecasting free bounds of the <shape> and connects
        open wires with tolerance <closetoler>.
        <shape> should be a compound of faces.
        Tolerance <closetoler> should be greater than tolerance
        <sewtoler> used for initializing sewing analyzer, otherwise
        connection of open wires is not performed.
        """

    @overload
    def __init__(self, theOther: ShapeFix_FreeBounds) -> None: ...

    def GetClosedWires(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """Returns compound of closed wires out of free edges."""

    def GetOpenWires(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """Returns compound of open wires out of free edges."""

    def GetShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns modified source shape."""

class ShapeFix_IntersectionTool:
    """
    Tool for fixing selfintersecting wire
    and intersecting wires
    """

    @overload
    def __init__(self, context: nanoocp.ShapeBuild.ShapeBuild_ReShape | None, preci: float, maxtol: float = 1.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: ShapeFix_IntersectionTool) -> None: ...

    def Context(self) -> nanoocp.ShapeBuild.ShapeBuild_ReShape:
        """Returns context"""

    def SplitEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, param: float, vert: nanoocp.TopoDS.TopoDS_Vertex, face: nanoocp.TopoDS.TopoDS_Face, newE1: nanoocp.TopoDS.TopoDS_Edge, newE2: nanoocp.TopoDS.TopoDS_Edge, preci: float) -> bool:
        """
        Split edge on two new edges using new vertex "vert"
        and "param" - parameter for splitting
        The "face" is necessary for pcurves and using TransferParameterProj
        """

    def CutEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, pend: float, cut: float, face: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]:
        """Cut edge by parameters pend and cut"""

    def FixSelfIntersectWire(self, face: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.ShapeExtend.ShapeExtend_WireData, int, int, int]: ...

    def FixIntersectingWires(self, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

class ShapeFix_Shape(ShapeFix_Root):
    """Fixing shape in general"""

    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initislises by shape."""

    @overload
    def __init__(self, theOther: ShapeFix_Shape) -> None: ...

    def Init(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initislises by shape."""

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """Iterates on sub- shape and performs fixes"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns resulting shape"""

    def FixSolidTool(self) -> ShapeFix_Solid:
        """Returns tool for fixing solids."""

    def FixShellTool(self) -> ShapeFix_Shell:
        """Returns tool for fixing shells."""

    def FixFaceTool(self) -> ShapeFix_Face:
        """Returns tool for fixing faces."""

    def FixWireTool(self) -> ShapeFix_Wire:
        """Returns tool for fixing wires."""

    def FixEdgeTool(self) -> ShapeFix_Edge:
        """Returns tool for fixing edges."""

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Returns the status of the last Fix.
        This can be a combination of the following flags:
        ShapeExtend_DONE1: some free edges were fixed
        ShapeExtend_DONE2: some free wires were fixed
        ShapeExtend_DONE3: some free faces were fixed
        ShapeExtend_DONE4: some free shells were fixed
        ShapeExtend_DONE5: some free solids were fixed
        ShapeExtend_DONE6: shapes in compound(s) were fixed
        """

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def SetPrecision(self, preci: float) -> None:
        """Sets basic precision value (also to FixSolidTool)"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance (also to FixSolidTool)"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance (also to FixSolidTool)"""

    def FixSolidMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Solid, by default True.
        """

    def SetFixSolidMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSolidMode() returns by reference in C++.
        """

    def FixFreeShellMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Shell, by default True.
        """

    def SetFixFreeShellMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixFreeShellMode() returns by reference in C++.
        """

    def FixFreeFaceMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Face, by default True.
        """

    def SetFixFreeFaceMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixFreeFaceMode() returns by reference in C++.
        """

    def FixFreeWireMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Wire, by default True.
        """

    def SetFixFreeWireMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixFreeWireMode() returns by reference in C++.
        """

    def FixSameParameterMode(self) -> int:
        """
        Returns (modifiable) the mode for applying
        ShapeFix::SameParameter after all fixes, by default True.
        """

    def SetFixSameParameterMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSameParameterMode() returns by reference in C++.
        """

    def FixVertexPositionMode(self) -> int:
        """
        Returns (modifiable) the mode for applying
        ShapeFix::FixVertexPosition before all fixes, by default False.
        """

    def SetFixVertexPositionMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixVertexPositionMode() returns by reference in C++.
        """

    def FixVertexTolMode(self) -> int:
        """
        Returns (modifiable) the mode for fixing tolerances of vertices on whole shape
        after performing all fixes
        """

    def SetFixVertexTolMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixVertexTolMode() returns by reference in C++.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_Solid(ShapeFix_Root):
    """
    Provides method to build a solid from a shells and
    orients them in order to have a valid solid with finite volume
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor;"""

    @overload
    def __init__(self, solid: nanoocp.TopoDS.TopoDS_Solid) -> None:
        """Initializes by solid."""

    @overload
    def __init__(self, theOther: ShapeFix_Solid) -> None: ...

    def Init(self, solid: nanoocp.TopoDS.TopoDS_Solid) -> None:
        """Initializes by solid ."""

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Iterates on shells and performs fixes
        (calls ShapeFix_Shell for each subshell). The passed
        progress indicator allows user to consult the current
        progress stage and abort algorithm if needed.
        """

    def SolidFromShell(self, shell: nanoocp.TopoDS.TopoDS_Shell) -> nanoocp.TopoDS.TopoDS_Solid:
        """Calls MakeSolid and orients the solid to be "not infinite\""""

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """Returns the status of the last Fix."""

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns resulting solid."""

    def FixShellTool(self) -> ShapeFix_Shell:
        """Returns tool for fixing shells."""

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def SetPrecision(self, preci: float) -> None:
        """Sets basic precision value (also to FixShellTool)"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance (also to FixShellTool)"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance (also to FixShellTool)"""

    def FixShellMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Shell, by default True.
        """

    def SetFixShellMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixShellMode() returns by reference in C++.
        """

    def FixShellOrientationMode(self) -> int:
        """
        Returns (modifiable) the mode for applying analysis and fixes of
        orientation of shells in the solid; by default True.
        """

    def SetFixShellOrientationMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixShellOrientationMode() returns by reference in C++.
        """

    def CreateOpenSolidMode(self) -> bool:
        """
        Returns (modifiable) the mode for creation of solids.
        If mode myCreateOpenSolidMode is equal to true
        solids are created from open shells
        else solids are created from closed shells only.
        ShapeFix_Shell, by default False.
        """

    def SetCreateOpenSolidMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value CreateOpenSolidMode() returns by reference in C++.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        In case of multiconnexity returns compound of fixed solids
        else returns one solid.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_Shell(ShapeFix_Root):
    """Fixing orientation of faces in shell"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Initializes by shell."""

    @overload
    def __init__(self, theOther: ShapeFix_Shell) -> None: ...

    def Init(self, shell: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Initializes by shell."""

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Iterates on subshapes and performs fixes
        (for each face calls ShapeFix_Face::Perform and
        then calls FixFaceOrientation). The passed progress
        indicator allows user to consult the current progress
        stage and abort algorithm if needed.
        """

    def FixFaceOrientation(self, shell: nanoocp.TopoDS.TopoDS_Shell, isAccountMultiConex: bool = True, NonManifold: bool = False) -> bool:
        """
        Fixes orientation of faces in shell.
        Changes orientation of face in the shell, if it is oriented opposite
        to neighbouring faces. If it is not possible to orient all faces in the
        shell (like in case of mebious band), this method orients only subset
        of faces. Other faces are stored in Error compound.
        Modes :
        isAccountMultiConex - mode for account cases of multiconnexity.
        If this mode is equal to true, separate shells will be created
        in the cases of multiconnexity. If this mode is equal to false,
        one shell will be created without account of multiconnexity.By default - true;
        NonManifold - mode for creation of non-manifold shells.
        If this mode is equal to true one non-manifold will be created from shell
        contains multishared edges. Else if this mode is equal to false only
        manifold shells will be created. By default - false.
        """

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns fixed shell (or subset of oriented faces)."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        In case of multiconnexity returns compound of fixed shells
        else returns one shell..
        """

    def NbShells(self) -> int:
        """Returns Number of obtainrd shells;"""

    def ErrorFaces(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """Returns not oriented subset of faces."""

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """Returns the status of the last Fix."""

    def FixFaceTool(self) -> ShapeFix_Face:
        """Returns tool for fixing faces."""

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def SetPrecision(self, preci: float) -> None:
        """Sets basic precision value (also to FixWireTool)"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance (also to FixWireTool)"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance (also to FixWireTool)"""

    def FixFaceMode(self) -> int:
        """
        Returns (modifiable) the mode for applying fixes of
        ShapeFix_Face, by default True.
        """

    def SetFixFaceMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixFaceMode() returns by reference in C++.
        """

    def FixOrientationMode(self) -> int:
        """
        Returns (modifiable) the mode for applying
        FixFaceOrientation, by default True.
        """

    def SetFixOrientationMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixOrientationMode() returns by reference in C++.
        """

    def SetNonManifoldFlag(self, isNonManifold: bool) -> None:
        """Sets NonManifold flag"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_Wire(ShapeFix_Root):
    """
    This class provides a set of tools for repairing a wire.

    These are methods Fix...(), organised in two levels:

    Level 1: Advanced - each method in this level fixes one separate problem,
    usually dealing with either single edge or connection of the
    two adjacent edges. These methods should be used carefully and
    called in right sequence, because some of them depend on others.

    Level 2: Public (API) - methods which group several methods of level 1
    and call them in a proper sequence in order to make some
    consistent set of fixes for a whole wire. It is possible to
    control calls to methods of the advanced level from methods of
    the public level by use of flags Fix..Mode() (see below).

    Fixes can be made in three ways:
    1. Increasing tolerance of an edge or a vertex
    2. Changing topology (adding/removing/replacing edge in the wire
    and/or replacing the vertex in the edge)
    3. Changing geometry (shifting vertex or adjusting ends of edge
    curve to vertices, or recomputing curves of the edge)

    When fix can be made in more than one way (e.g., either
    by increasing tolerance or shifting a vertex), it is chosen
    according to the flags:
    ModifyTopologyMode - allows modification of the topology.
    This flag can be set when fixing a wire on
    the separate (free) face, and should be
    unset for face which is part of shell.
    ModifyGeometryMode - allows modification of the geometry.

    The order of descriptions of Fix() methods in this CDL
    approximately corresponds to the optimal order of calls.

    NOTE: most of fixing methods expect edges in the
    ShapeExtend_WireData to be ordered, so it is necessary to make
    call to FixReorder() before any other fixes

    ShapeFix_Wire should be initialized prior to any fix by the
    following data:
    a) Wire (ether TopoDS_Wire or ShapeExtend_Wire)
    b) Face or surface
    c) Precision
    d) Maximal tail angle and width
    This can be done either by calling corresponding methods
    (LoadWire, SetFace or SetSurface, SetPrecision, SetMaxTailAngle
    and SetMaxTailWidth), or
    by loading already filled ShapeAnalisis_Wire with method Load
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor, creates clear object with default flags"""

    @overload
    def __init__(self, wire: nanoocp.TopoDS.TopoDS_Wire, face: nanoocp.TopoDS.TopoDS_Face, prec: float) -> None:
        """
        Create new object with default flags and prepare it for use
        (Loads analyzer with all the data for the wire and face)
        """

    @overload
    def __init__(self, theOther: ShapeFix_Wire) -> None: ...

    def ClearModes(self) -> None:
        """Sets all modes to default"""

    def ClearStatuses(self) -> None:
        """Clears all statuses"""

    @overload
    def Init(self, wire: nanoocp.TopoDS.TopoDS_Wire, face: nanoocp.TopoDS.TopoDS_Face, prec: float) -> None:
        """
        Load analyzer with all the data for the wire and face
        and drops all fixing statuses
        """

    @overload
    def Init(self, saw: nanoocp.ShapeAnalysis.ShapeAnalysis_Wire | None) -> None:
        """
        Load analyzer with all the data already prepared
        and drops all fixing statuses
        If analyzer contains face, there is no need to set it
        by SetFace or SetSurface
        """

    @overload
    def Load(self, wire: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    @overload
    def Load(self, sbwd: nanoocp.ShapeExtend.ShapeExtend_WireData | None) -> None:
        """Load data for the wire, and drops all fixing statuses"""

    @overload
    def SetFace(self, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Set working face for the wire"""

    @overload
    def SetFace(self, theFace: nanoocp.TopoDS.TopoDS_Face, theSurfaceAnalysis: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None) -> None:
        """Set working face for the wire and surface analysis object"""

    @overload
    def SetSurface(self, theSurfaceAnalysis: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None) -> None:
        """Set surface analysis for the wire"""

    @overload
    def SetSurface(self, surf: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def SetSurface(self, surf: nanoocp.Geom.Geom_Surface | None, loc: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Set surface for the wire"""

    def SetPrecision(self, prec: float) -> None:
        """Set working precision (to root and to analyzer)"""

    def SetMaxTailAngle(self, theMaxTailAngle: float) -> None:
        """Sets the maximal allowed angle of the tails in radians."""

    def SetMaxTailWidth(self, theMaxTailWidth: float) -> None:
        """Sets the maximal allowed width of the tails."""

    def IsLoaded(self) -> bool:
        """Tells if the wire is loaded"""

    def IsReady(self) -> bool:
        """Tells if the wire and face are loaded"""

    def NbEdges(self) -> int:
        """returns number of edges in the working wire"""

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Makes the resulting Wire (by basic Brep_Builder)"""

    def WireAPIMake(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Makes the resulting Wire (by BRepAPI_MakeWire)"""

    def Analyzer(self) -> nanoocp.ShapeAnalysis.ShapeAnalysis_Wire:
        """returns field Analyzer (working tool)"""

    def WireData(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """returns working wire"""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """returns working face (Analyzer.Face())"""

    def ModifyTopologyMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether it is
        allowed to modify topology of the wire during fixing
        (adding/removing edges etc.)
        """

    def SetModifyTopologyMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyTopologyMode() returns by reference in C++.
        """

    def ModifyGeometryMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether the Fix..()
        methods are allowed to modify geometry of the edges and vertices
        """

    def SetModifyGeometryMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyGeometryMode() returns by reference in C++.
        """

    def ModifyRemoveLoopMode(self) -> int:
        """
        Returns (modifiable) the flag which defines whether the Fix..()
        methods are allowed to modify RemoveLoop of the edges
        """

    def SetModifyRemoveLoopMode(self, theValue: int) -> None:
        """
        Python addition: sets the value ModifyRemoveLoopMode() returns by reference in C++.
        """

    def ClosedWireMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether the wire
        is to be closed (by calling methods like FixDegenerated()
        and FixConnected() for last and first edges).
        """

    def SetClosedWireMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ClosedWireMode() returns by reference in C++.
        """

    def PreferencePCurveMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether the 2d (True)
        representation of the wire is preferable over 3d one (in the
        case of ambiguity in FixEdgeCurves).
        """

    def SetPreferencePCurveMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value PreferencePCurveMode() returns by reference in C++.
        """

    def FixGapsByRangesMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether tool
        tries to fix gaps first by changing curves ranges (i.e.
        using intersection, extrema, projections) or not.
        """

    def SetFixGapsByRangesMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value FixGapsByRangesMode() returns by reference in C++.
        """

    def FixReorderMode(self) -> int: ...

    def SetFixReorderMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixReorderMode() returns by reference in C++.
        """

    def FixSmallMode(self) -> int: ...

    def SetFixSmallMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSmallMode() returns by reference in C++.
        """

    def FixConnectedMode(self) -> int: ...

    def SetFixConnectedMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixConnectedMode() returns by reference in C++.
        """

    def FixEdgeCurvesMode(self) -> int: ...

    def SetFixEdgeCurvesMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixEdgeCurvesMode() returns by reference in C++.
        """

    def FixDegeneratedMode(self) -> int: ...

    def SetFixDegeneratedMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixDegeneratedMode() returns by reference in C++.
        """

    def FixSelfIntersectionMode(self) -> int: ...

    def SetFixSelfIntersectionMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSelfIntersectionMode() returns by reference in C++.
        """

    def FixLackingMode(self) -> int: ...

    def SetFixLackingMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixLackingMode() returns by reference in C++.
        """

    def FixGaps3dMode(self) -> int: ...

    def SetFixGaps3dMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixGaps3dMode() returns by reference in C++.
        """

    def FixGaps2dMode(self) -> int:
        """
        Returns (modifiable) the flag for corresponding Fix..() method
        which defines whether this method will be called from the
        method APIFix():
        -1 default
        1 method will be called
        0 method will not be called
        """

    def SetFixGaps2dMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixGaps2dMode() returns by reference in C++.
        """

    def FixReversed2dMode(self) -> int: ...

    def SetFixReversed2dMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixReversed2dMode() returns by reference in C++.
        """

    def FixRemovePCurveMode(self) -> int: ...

    def SetFixRemovePCurveMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixRemovePCurveMode() returns by reference in C++.
        """

    def FixAddPCurveMode(self) -> int: ...

    def SetFixAddPCurveMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixAddPCurveMode() returns by reference in C++.
        """

    def FixRemoveCurve3dMode(self) -> int: ...

    def SetFixRemoveCurve3dMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixRemoveCurve3dMode() returns by reference in C++.
        """

    def FixAddCurve3dMode(self) -> int: ...

    def SetFixAddCurve3dMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixAddCurve3dMode() returns by reference in C++.
        """

    def FixSeamMode(self) -> int: ...

    def SetFixSeamMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSeamMode() returns by reference in C++.
        """

    def FixShiftedMode(self) -> int: ...

    def SetFixShiftedMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixShiftedMode() returns by reference in C++.
        """

    def FixSameParameterMode(self) -> int: ...

    def SetFixSameParameterMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSameParameterMode() returns by reference in C++.
        """

    def FixVertexToleranceMode(self) -> int: ...

    def SetFixVertexToleranceMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixVertexToleranceMode() returns by reference in C++.
        """

    def FixNotchedEdgesMode(self) -> int: ...

    def SetFixNotchedEdgesMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixNotchedEdgesMode() returns by reference in C++.
        """

    def FixSelfIntersectingEdgeMode(self) -> int: ...

    def SetFixSelfIntersectingEdgeMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixSelfIntersectingEdgeMode() returns by reference in C++.
        """

    def FixIntersectingEdgesMode(self) -> int: ...

    def SetFixIntersectingEdgesMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixIntersectingEdgesMode() returns by reference in C++.
        """

    def FixNonAdjacentIntersectingEdgesMode(self) -> int:
        """
        Returns (modifiable) the flag for corresponding Fix..() method
        which defines whether this method will be called from the
        corresponding Fix..() method of the public level:
        -1 default
        1 method will be called
        0 method will not be called
        """

    def SetFixNonAdjacentIntersectingEdgesMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixNonAdjacentIntersectingEdgesMode() returns by reference in C++.
        """

    def FixTailMode(self) -> int: ...

    def SetFixTailMode(self, theValue: int) -> None:
        """
        Python addition: sets the value FixTailMode() returns by reference in C++.
        """

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        This method performs all the available fixes.
        If some fix is turned on or off explicitly by the Fix..Mode() flag,
        this fix is either called or not depending on that flag.
        Else (i.e. if flag is default) fix is called depending on the
        situation: some fixes are not called or are limited if order of
        edges in the wire is not OK, or depending on modes

        The order of the fixes and default behaviour of Perform() are:
        FixReorder
        FixSmall (with lockvtx true if ! TopoMode or if wire is not ordered)
        FixConnected (if wire is ordered)
        FixEdgeCurves (without FixShifted if wire is not ordered)
        FixDegenerated (if wire is ordered)
        FixSelfIntersection (if wire is ordered and ClosedMode is True)
        FixLacking (if wire is ordered)
        """

    @overload
    def FixReorder(self, theModeBoth: bool = False) -> bool:
        """
        Performs an analysis and reorders edges in the wire using class WireOrder.
        Flag <theModeBoth> determines the use of miscible mode if necessary.
        """

    @overload
    def FixReorder(self, wi: nanoocp.ShapeAnalysis.ShapeAnalysis_WireOrder) -> bool:
        """
        Reorder edges in the wire as determined by WireOrder
        that should be filled and computed before
        """

    @overload
    def FixSmall(self, lockvtx: bool, precsmall: float = 0.0) -> int:
        """Applies FixSmall(num) to all edges in the wire"""

    @overload
    def FixSmall(self, num: int, lockvtx: bool, precsmall: float) -> bool:
        """
        Fixes Null Length Edge to be removed
        If an Edge has Null Length (regarding preci, or <precsmall>
        - what is smaller), it should be removed
        It can be with no problem if its two vertices are the same
        Else, if lockvtx is False, it is removed and its end vertex
        is put on the preceding edge
        But if lockvtx is True, this edge must be kept ...
        """

    @overload
    def FixConnected(self, prec: float = -1.0) -> bool:
        """
        Applies FixConnected(num) to all edges in the wire
        Connection between first and last edges is treated only if
        flag ClosedMode is True
        If <prec> is -1 then MaxTolerance() is taken.
        """

    @overload
    def FixConnected(self, num: int, prec: float, theUpdateWire: bool = True) -> bool:
        """
        Fixes connected edges (preceding and current)
        Forces Vertices (end of preceding-begin of current) to be
        the same one
        Tests with starting preci or, if given greater, <prec>
        If <prec> is -1 then MaxTolerance() is taken.
        If <theUpdateWire> is true, synchronizes wire data with context replacements.
        """

    def FixEdgeCurves(self) -> bool:
        """
        Groups the fixes dealing with 3d and pcurves of the edges.
        The order of the fixes and the default behaviour are:
        ShapeFix_Edge::FixReversed2d
        ShapeFix_Edge::FixRemovePCurve (only if forced)
        ShapeFix_Edge::FixAddPCurve
        ShapeFix_Edge::FixRemoveCurve3d (only if forced)
        ShapeFix_Edge::FixAddCurve3d
        FixSeam,
        FixShifted,
        ShapeFix_Edge::FixSameParameter
        """

    @overload
    def FixDegenerated(self) -> bool:
        """
        Applies FixDegenerated(num) to all edges in the wire
        Connection between first and last edges is treated only if
        flag ClosedMode is True
        """

    @overload
    def FixDegenerated(self, num: int) -> bool:
        """
        Fixes Degenerated Edge
        Checks an <num-th> edge or a point between <num>th-1 and <num>th
        edges for a singularity on a supporting surface.
        If singularity is detected, either adds new degenerated edge
        (before <num>th), or makes <num>th edge to be degenerated.
        """

    def FixSelfIntersection(self) -> bool:
        """
        Applies FixSelfIntersectingEdge(num) and
        FixIntersectingEdges(num) to all edges in the wire and
        FixIntersectingEdges(num1, num2) for all pairs num1 and num2
        such that num2 >= num1 + 2
        and removes wrong edges if any
        """

    @overload
    def FixLacking(self, force: bool = False) -> bool:
        """
        Applies FixLacking(num) to all edges in the wire
        Connection between first and last edges is treated only if
        flag ClosedMode is True
        If <force> is False (default), test for connectness is done with
        precision of vertex between edges, else it is done with minimal
        value of vertex tolerance and Analyzer.Precision().
        Hence, <force> will lead to inserting lacking edges in replacement
        of vertices which have big tolerances.
        """

    @overload
    def FixLacking(self, num: int, force: bool = False) -> bool:
        """
        Fixes Lacking Edge
        Test if two adjucent edges are disconnected in 2d (while
        connected in 3d), and in that case either increase tolerance
        of the vertex or add a new edge (straight in 2d space), in
        order to close wire in 2d.
        Returns True if edge was added or tolerance was increased.
        """

    def FixClosed(self, prec: float = -1.0) -> bool:
        """
        Fixes a wire to be well closed
        It performs FixConnected, FixDegenerated and FixLacking between
        last and first edges (independingly on flag ClosedMode and modes
        for these fixings)
        If <prec> is -1 then MaxTolerance() is taken.
        """

    def FixGaps3d(self) -> bool:
        """
        Fixes gaps between ends of 3d curves on adjacent edges
        myPrecision is used to detect the gaps.
        """

    def FixGaps2d(self) -> bool:
        """
        Fixes gaps between ends of pcurves on adjacent edges
        myPrecision is used to detect the gaps.
        """

    def FixSeam(self, num: int) -> bool:
        """
        Fixes a seam edge
        A Seam edge has two pcurves, one for forward. one for reversed
        The forward pcurve must be set as first

        NOTE that correct order of pcurves in the seam edge depends on
        its orientation (i.e., on orientation of the wire, method of
        exploration of edges etc.).
        Since wire represented by the ShapeExtend_WireData is always forward
        (orientation is accounted by edges), it will work correct if:
        1. Wire created from ShapeExtend_WireData with methods
        ShapeExtend_WireData::Wire..() is added into the FORWARD face
        (orientation can be applied later)
        2. Wire is extracted from the face with orientation not composed
        with orientation of the face
        """

    def FixShifted(self) -> bool:
        """
        Fixes edges which have pcurves shifted by whole parameter
        range on the closed surface (the case may occur if pcurve
        of edge was computed by projecting 3d curve, which goes
        along the seam).
        It compares each two consequent edges and tries to connect them
        if distance between ends is near to range of the surface.
        It also can detect and fix the case if all pcurves are connected,
        but lie out of parametric bounds of the surface.
        In addition to FixShifted from ShapeFix_Wire, more
        sophisticated check of degenerate points is performed,
        and special cases like sphere given by two meridians
        are treated.
        """

    def FixNotchedEdges(self) -> bool: ...

    def FixGap3d(self, num: int, convert: bool = False) -> bool:
        """
        Fixes gap between ends of 3d curves on num-1 and num-th edges.
        myPrecision is used to detect the gap.
        If convert is True, converts curves to bsplines to bend.
        """

    def FixGap2d(self, num: int, convert: bool = False) -> bool:
        """
        Fixes gap between ends of pcurves on num-1 and num-th edges.
        myPrecision is used to detect the gap.
        If convert is True, converts pcurves to bsplines to bend.
        """

    def FixTails(self) -> bool: ...

    def StatusReorder(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusSmall(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusConnected(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusEdgeCurves(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusDegenerated(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusSelfIntersection(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusLacking(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusClosed(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusGaps3d(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusGaps2d(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusNotches(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusRemovedSegment(self) -> bool:
        """
        Querying the status of performed API fixing procedures
        Each Status..() methods gives information about the last call to
        the corresponding Fix..() method of API level:
        OK  : no problems detected; nothing done
        DONE: some problem(s) was(were) detected and successfully fixed
        FAIL: some problem(s) cannot be fixed
        """

    def StatusFixTails(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def LastFixStatus(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries the status of last call to methods Fix... of
        advanced level
        For details see corresponding methods; universal statuses are:
        OK  : problem not detected; nothing done
        DONE: problem was detected and successfully fixed
        FAIL: problem cannot be fixed
        """

    def FixEdgeTool(self) -> ShapeFix_Edge:
        """Returns tool for fixing wires."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_ShapeTolerance:
    """Modifies tolerances of sub-shapes (vertices, edges, faces)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_ShapeTolerance) -> None: ...

    def LimitTolerance(self, shape: nanoocp.TopoDS.TopoDS_Shape, tmin: float, tmax: float = 0.0, styp: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> bool:
        """
        Limits tolerances in a shape as follows :
        tmin = tmax -> as SetTolerance (forces)
        tmin = 0   -> maximum tolerance will be <tmax>
        tmax = 0 or not given (more generally, tmax < tmin) ->
        <tmax> ignored, minimum will be <tmin>
        else, maximum will be <max> and minimum will be <min>
        styp = VERTEX : only vertices are set
        styp = EDGE   : only edges are set
        styp = FACE   : only faces are set
        styp = WIRE   : to have edges and their vertices set
        styp = other value : all (vertices,edges,faces) are set
        Returns True if at least one tolerance of the sub-shape has
        been modified
        """

    def SetTolerance(self, shape: nanoocp.TopoDS.TopoDS_Shape, preci: float, styp: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None:
        """
        Sets (enforces) tolerances in a shape to the given value
        styp = VERTEX : only vertices are set
        styp = EDGE   : only edges are set
        styp = FACE   : only faces are set
        styp = WIRE   : to have edges and their vertices set
        styp = other value : all (vertices,edges,faces) are set
        """

class ShapeFix_SplitCommonVertex(ShapeFix_Root):
    """
    Two wires have common vertex - this case is valid in BRep model
    and isn't valid in STEP => before writing into STEP it is necessary
    to split this vertex (each wire must has one vertex)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_SplitCommonVertex) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Perform(self) -> None: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_SplitTool:
    """
    Tool for splitting and cutting edges; includes methods
    used in OverlappingTool and IntersectionTool
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeFix_SplitTool) -> None: ...

    @overload
    def SplitEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, param: float, vert: nanoocp.TopoDS.TopoDS_Vertex, face: nanoocp.TopoDS.TopoDS_Face, newE1: nanoocp.TopoDS.TopoDS_Edge, newE2: nanoocp.TopoDS.TopoDS_Edge, tol3d: float, tol2d: float) -> bool:
        """
        Split edge on two new edges using new vertex "vert"
        and "param" - parameter for splitting
        The "face" is necessary for pcurves and using TransferParameterProj
        """

    @overload
    def SplitEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, param1: float, param2: float, vert: nanoocp.TopoDS.TopoDS_Vertex, face: nanoocp.TopoDS.TopoDS_Face, newE1: nanoocp.TopoDS.TopoDS_Edge, newE2: nanoocp.TopoDS.TopoDS_Edge, tol3d: float, tol2d: float) -> bool:
        """
        Split edge on two new edges using new vertex "vert"
        and "param1" and "param2" - parameter for splitting and cutting
        The "face" is necessary for pcurves and using TransferParameterProj
        """

    @overload
    def SplitEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, fp: float, V1: nanoocp.TopoDS.TopoDS_Vertex, lp: float, V2: nanoocp.TopoDS.TopoDS_Vertex, face: nanoocp.TopoDS.TopoDS_Face, SeqE: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape], context: nanoocp.ShapeBuild.ShapeBuild_ReShape | None, tol3d: float, tol2d: float) -> tuple[bool, int]:
        """
        Split edge on two new edges using two new vertex V1 and V2
        and two parameters for splitting - fp and lp correspondingly
        The "face" is necessary for pcurves and using TransferParameterProj
        aNum - number of edge in SeqE which corresponding to [fp,lp]
        """

    def CutEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, pend: float, cut: float, face: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]:
        """Cut edge by parameters pend and cut"""

class ShapeFix_Wireframe(ShapeFix_Root):
    """Provides methods for fixing wireframe of shape"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_Wireframe) -> None: ...

    def ClearStatuses(self) -> None:
        """Clears all statuses"""

    def Load(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Loads a shape, resets statuses"""

    def FixWireGaps(self) -> bool:
        """
        Fixes gaps between ends of curves of adjacent edges
        (both 3d and pcurves) in wires
        If precision is 0.0, uses Precision::Confusion().
        """

    def FixSmallEdges(self) -> bool:
        """
        Fixes small edges in shape by merging adjacent edges
        If precision is 0.0, uses Precision::Confusion().
        """

    def CheckSmallEdges(self, theSmallEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theEdgeToFaces: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theFaceWithSmall: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theMultyEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Auxiliary tool for FixSmallEdges which checks for small edges and fills the maps.
        Returns True if at least one small edge has been found.
        """

    def MergeSmallEdges(self, theSmallEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theEdgeToFaces: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theFaceWithSmall: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theMultyEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theModeDrop: bool = False, theLimitAngle: float = -1.0) -> bool:
        """
        Auxiliary tool for FixSmallEdges which merges small edges.
        If theModeDrop is equal to true then small edges,
        which cannot be connected with adjacent edges are dropped.
        Otherwise they are kept.
        theLimitAngle specifies maximum allowed tangency
        discontinuity between adjacent edges.
        If theLimitAngle is equal to -1, this angle is not taken into account.
        """

    def StatusWireGaps(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Decodes the status of the last FixWireGaps.
        OK - No gaps were found
        DONE1 - Some gaps in 3D were fixed
        DONE2 - Some gaps in 2D were fixed
        FAIL1 - Failed to fix some gaps in 3D
        FAIL2 - Failed to fix some gaps in 2D
        """

    def StatusSmallEdges(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Decodes the status of the last FixSmallEdges.
        OK - No small edges were found
        DONE1 - Some small edges were fixed
        FAIL1 - Failed to fix some small edges
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ModeDropSmallEdges(self) -> bool:
        """Returns mode managing removing small edges."""

    def SetModeDropSmallEdges(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModeDropSmallEdges() returns by reference in C++.
        """

    def SetLimitAngle(self, theLimitAngle: float) -> None:
        """Set limit angle for merging edges."""

    def LimitAngle(self) -> float:
        """Get limit angle for merging edges."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeFix_WireVertex:
    """
    Fixing disconnected edges in the wire
    Fixes vertices in the wire on the basis of pre-analysis
    made by ShapeAnalysis_WireVertex (given as argument).
    The Wire has formerly been loaded in a ShapeExtend_WireData.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeFix_WireVertex) -> None: ...

    @overload
    def Init(self, wire: nanoocp.TopoDS.TopoDS_Wire, preci: float) -> None: ...

    @overload
    def Init(self, sbwd: nanoocp.ShapeExtend.ShapeExtend_WireData | None, preci: float) -> None:
        """
        Loads the wire, ininializes internal analyzer
        (ShapeAnalysis_WireVertex) with the given precision,
        and performs analysis
        """

    @overload
    def Init(self, sawv: nanoocp.ShapeAnalysis.ShapeAnalysis_WireVertex) -> None:
        """
        Loads all the data on wire, already analysed by
        ShapeAnalysis_WireVertex
        """

    def Analyzer(self) -> nanoocp.ShapeAnalysis.ShapeAnalysis_WireVertex:
        """returns internal analyzer"""

    def WireData(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """returns data on wire (fixed)"""

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """returns resulting wire (fixed)"""

    def FixSame(self) -> int:
        """
        Fixes "Same" or "Close" status (same vertex may be set,
        without changing parameters)
        Returns the count of fixed vertices, 0 if none
        """

    def Fix(self) -> int:
        """
        Fixes all statuses except "Disjoined", i.e. the cases in which a
        common value has been set, with or without changing parameters
        Returns the count of fixed vertices, 0 if none
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.ShapeFix
import nanoocp.TopTools
ShapeFix_SequenceOfWireSegment = nanoocp.NCollection.NCollection_Sequence[nanoocp.ShapeFix.ShapeFix_WireSegment]
