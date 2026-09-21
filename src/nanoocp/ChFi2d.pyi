"""OCCT package ChFi2d (toolkit TKFillet)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.TopoDS
import nanoocp.gp


class ChFi2d_ConstructionError(enum.IntEnum):
    """Error that can occur during the fillet construction on planar wire."""

    ChFi2d_NotPlanar = 0

    ChFi2d_NoFace = 1

    ChFi2d_InitialisationError = 2

    ChFi2d_ParametersError = 3

    ChFi2d_Ready = 4

    ChFi2d_IsDone = 5

    ChFi2d_ComputationError = 6

    ChFi2d_ConnexionError = 7

    ChFi2d_TangencyError = 8

    ChFi2d_FirstEdgeDegenerated = 9

    ChFi2d_LastEdgeDegenerated = 10

    ChFi2d_BothEdgesDegenerated = 11

    ChFi2d_NotAuthorized = 12

ChFi2d_NotPlanar: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_NotPlanar

ChFi2d_NoFace: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_NoFace

ChFi2d_InitialisationError: ChFi2d_ConstructionError = ...

ChFi2d_ParametersError: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_ParametersError

ChFi2d_Ready: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_Ready

ChFi2d_IsDone: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_IsDone

ChFi2d_ComputationError: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_ComputationError

ChFi2d_ConnexionError: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_ConnexionError

ChFi2d_TangencyError: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_TangencyError

ChFi2d_FirstEdgeDegenerated: ChFi2d_ConstructionError = ...

ChFi2d_LastEdgeDegenerated: ChFi2d_ConstructionError = ...

ChFi2d_BothEdgesDegenerated: ChFi2d_ConstructionError = ...

ChFi2d_NotAuthorized: ChFi2d_ConstructionError = ChFi2d_ConstructionError.ChFi2d_NotAuthorized

class ChFi2d:
    """
    This package contains the algorithms used to build
    fillets or chamfers on planar wire.

    This package provides two algorithms for 2D fillets:
    ChFi2d_Builder - it constructs a fillet or chamfer
    for linear and circular edges of a face.
    ChFi2d_FilletAPI - it encapsulates two algorithms:
    ChFi2d_AnaFilletAlgo - analytical constructor of the fillet.
    It works only for linear and circular edges,
    having a common point.
    ChFi2d_FilletAlgo - iteration recursive method constructing
    the fillet edge for any type of edges including
    ellipses and b-splines.
    The edges may even have no common point.
    ChFi2d_ChamferAPI - an algorithm for construction of chamfers
    between two linear edges of a plane.

    The algorithms ChFi2d_AnaFilletAlgo and ChFi2d_FilletAlgo may be used directly
    or via the interface class ChFi2d_FilletAPI.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFi2d) -> None: ...

    @staticmethod
    def CommonVertex(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

    @staticmethod
    def FindConnectedEdges(F: nanoocp.TopoDS.TopoDS_Face, V: nanoocp.TopoDS.TopoDS_Vertex, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> ChFi2d_ConstructionError: ...

class ChFi2d_AnaFilletAlgo:
    """
    An analytical algorithm for calculation of the fillets.
    It is implemented for segments and arcs of circle only.
    """

    @overload
    def __init__(self) -> None:
        """
        An empty constructor.
        Use the method Init() to initialize the class.
        """

    @overload
    def __init__(self, theWire: nanoocp.TopoDS.TopoDS_Wire, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        A constructor.
        It expects a wire consisting of two edges of type (any combination of):
        - segment
        - arc of circle.
        """

    @overload
    def __init__(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        A constructor.
        It expects two edges having a common point of type:
        - segment
        - arc of circle.
        """

    @overload
    def __init__(self, theOther: ChFi2d_AnaFilletAlgo) -> None: ...

    @overload
    def Init(self, theWire: nanoocp.TopoDS.TopoDS_Wire, thePlane: nanoocp.gp.gp_Pln) -> None:
        """Initializes the class by a wire consisting of two edges."""

    @overload
    def Init(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """Initializes the class by two edges."""

    def Perform(self, radius: float) -> bool:
        """Calculates a fillet."""

    def Result(self, e1: nanoocp.TopoDS.TopoDS_Edge, e2: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """Retrieves a result (fillet and shrinked neighbours)."""

class ChFi2d_Builder:
    """
    This class contains the algorithm used to build
    fillet on planar wire.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        The face <F> can be build on a closed or an open
        wire.
        """

    @overload
    def __init__(self, theOther: ChFi2d_Builder) -> None: ...

    @overload
    def Init(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Init(self, RefFace: nanoocp.TopoDS.TopoDS_Face, ModFace: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def AddFillet(self, V: nanoocp.TopoDS.TopoDS_Vertex, Radius: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Add a fillet of radius <Radius> on the wire
        between the two edges connected to the vertex <V>.
        <AddFillet> returns the fillet edge. The returned
        edge has sense only if the status <status> is
        <IsDone>
        """

    def ModifyFillet(self, Fillet: nanoocp.TopoDS.TopoDS_Edge, Radius: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        modify the fillet radius and return the new fillet
        edge. this edge has sense only if the status
        <status> is <IsDone>.
        """

    def RemoveFillet(self, Fillet: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        removes the fillet <Fillet> and returns the vertex
        connecting the two adjacent edges to this fillet.
        """

    @overload
    def AddChamfer(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, D1: float, D2: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Add a chamfer on the wire between the two edges
        connected <E1> and <E2>. <AddChamfer> returns the
        chamfer edge. This edge has sense only if the
        status <status> is <IsDone>.
        """

    @overload
    def AddChamfer(self, E: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex, D: float, Ang: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Add a chamfer on the wire between the two edges
        connected to the vertex <V>. The chamfer will make
        an angle <Ang> with the edge <E>, and one of its
        extremities will be on <E> at distance <D>. The
        returned edge has sense only if the status
        <status> is <IsDone>.
        Warning: The value of <Ang> must be expressed in Radian.
        """

    @overload
    def ModifyChamfer(self, Chamfer: nanoocp.TopoDS.TopoDS_Edge, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, D1: float, D2: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        modify the chamfer <Chamfer> and returns the new
        chamfer edge.
        This edge as sense only if the status <status> is
        <IsDone>.
        """

    @overload
    def ModifyChamfer(self, Chamfer: nanoocp.TopoDS.TopoDS_Edge, E: nanoocp.TopoDS.TopoDS_Edge, D: float, Ang: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        modify the chamfer <Chamfer> and returns the new
        chamfer edge. This edge as sense only if the
        status <status> is <IsDone>.
        Warning: The value of <Ang> must be expressed in Radian.
        """

    def RemoveChamfer(self, Chamfer: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        removes the chamfer <Chamfer> and returns the
        vertex connecting the two adjacent edges to this
        chamfer.
        """

    def Result(self) -> nanoocp.TopoDS.TopoDS_Face:
        """returns the modified face"""

    def IsModified(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def FilletEdges(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]:
        """returns the list of new edges"""

    def NbFillet(self) -> int: ...

    def ChamferEdges(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]:
        """returns the list of new edges"""

    def NbChamfer(self) -> int: ...

    def HasDescendant(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def DescendantEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        returns the modified edge if <E> has descendant or
        <E> in the other case.
        """

    def BasisEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the parent edge of <E>
        Warning: If <E>is a basis edge, the returned edge would be
        equal to <E>
        """

    def Status(self) -> ChFi2d_ConstructionError: ...

class ChFi2d_ChamferAPI:
    """A class making a chamfer between two linear edges."""

    @overload
    def __init__(self) -> None:
        """An empty constructor."""

    @overload
    def __init__(self, theWire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """A constructor accepting a wire consisting of two linear edges."""

    @overload
    def __init__(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """A constructor accepting two linear edges."""

    @overload
    def __init__(self, theOther: ChFi2d_ChamferAPI) -> None: ...

    @overload
    def Init(self, theWire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Initializes the class by a wire consisting of two libear edges."""

    @overload
    def Init(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Initializes the class by two linear edges."""

    def Perform(self) -> bool:
        """
        Constructs a chamfer edge.
        Returns true if the edge is constructed.
        """

    def Result(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, theLength1: float, theLength2: float) -> nanoocp.TopoDS.TopoDS_Edge: ...

class ChFi2d_FilletAlgo:
    """
    Algorithm that creates fillet edge: arc tangent to two edges in the start
    and in the end vertices. Initial edges must be located on the plane and
    must be connected by the end or start points (shared vertices are not
    obligatory). Created fillet arc is created with the given radius, that is
    useful in sketcher applications.

    The algorithm is iterative that allows to create fillet on any curves
    of initial edges, that supports projection of point and C2 continuous.
    Principles of algorithm can de reduced to the Newton method:
    1. Splitting initial edge into N segments where probably only 1 root can be
    found. N depends on the complexity of the underlying curve.
    2. On each segment compute value and derivative of the function:
    - argument of the function is the parameter on the curve
    - take point on the curve by the parameter: point of tangency
    - make center of fillet: perpendicular vector from the point of tagency
    - make projection from the center to the second curve
    - length of the projection minus radius of the fillet is result of the
    function
    - derivative of this function in the point is computed by value in
    point with small shift
    3. Using Newton search method take the point on the segment where function
    value is most close to zero. If it is not enough close, step 2 and 3 are
    repeated taking as start or end point the found point.
    4. If solution is found, result is created on point on root of the function (as a start point),
    point of the projection onto second curve (as an end point) and center of arc in found
    center. Initial edges are cut by the start and end point of tangency.
    """

    @overload
    def __init__(self) -> None:
        """
        An empty constructor of the fillet algorithm.
        Call a method Init() to initialize the algorithm
        before calling of a Perform() method.
        """

    @overload
    def __init__(self, theWire: nanoocp.TopoDS.TopoDS_Wire, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        A constructor of a fillet algorithm: accepts a wire consisting of two edges in a plane.
        """

    @overload
    def __init__(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """A constructor of a fillet algorithm: accepts two edges in a plane."""

    @overload
    def __init__(self, theOther: ChFi2d_FilletAlgo) -> None: ...

    @overload
    def Init(self, theWire: nanoocp.TopoDS.TopoDS_Wire, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane.
        """

    @overload
    def Init(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """Initializes a fillet algorithm: accepts two edges in a plane."""

    def Perform(self, theRadius: float) -> bool:
        """
        Constructs a fillet edge.
        Returns true, if at least one result was found
        """

    def NbResults(self, thePoint: nanoocp.gp.gp_Pnt) -> int:
        """
        Returns number of possible solutions.
        <thePoint> chooses a particular fillet in case of several fillets
        may be constructed (for example, a circle intersecting a segment in 2 points).
        Put the intersecting (or common) point of the edges.
        """

    def Result(self, thePoint: nanoocp.gp.gp_Pnt, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, iSolution: int = -1) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns result (fillet edge, modified edge1, modified edge2),
        nearest to the given point <thePoint> if iSolution == -1.
        <thePoint> chooses a particular fillet in case of several fillets
        may be constructed (for example, a circle intersecting a segment in 2 points).
        Put the intersecting (or common) point of the edges.
        """

class FilletPoint:
    """
    Private class. Corresponds to the point on the first curve, computed
    fillet function and derivative on it.
    """

    @overload
    def __init__(self, theParam: float) -> None:
        """Creates a point on a first curve by parameter on this curve."""

    @overload
    def __init__(self, theOther: FilletPoint) -> None: ...

    def setParam(self, theParam: float) -> None:
        """
        Changes the point position by changing point parameter on the first curve.
        """

    def getParam(self) -> float:
        """Returns the point parameter on the first curve."""

    def getNBValues(self) -> int:
        """Returns number of found values of function in this point."""

    def getValue(self, theIndex: int) -> float:
        """Returns value of function in this point."""

    def getDiff(self, theIndex: int) -> float:
        """Returns derivatives of function in this point."""

    def isValid(self, theIndex: int) -> bool:
        """
        Returns true if function is valid (rediuses vectors of fillet do not intersect any curve).
        """

    def getNear(self, theIndex: int) -> int:
        """Returns the index of the nearest value"""

    def setParam2(self, theParam2: float) -> None:
        """Defines the parameter of the projected point on the second curve."""

    def getParam2(self) -> float:
        """Returns the parameter of the projected point on the second curve."""

    def setCenter(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """Center of the fillet."""

    def getCenter(self) -> nanoocp.gp.gp_Pnt2d:
        """Center of the fillet."""

    def appendValue(self, theValue: float, theValid: bool) -> None:
        """Appends value of the function."""

    def calculateDiff(self, arg0: FilletPoint) -> bool:
        """
        Computes difference between this point and the given. Stores difference in myD.
        """

    def FilterPoints(self, arg0: FilletPoint) -> None:
        """Filters out the values and leaves the most optimal one."""

    def Copy(self) -> FilletPoint:
        """
        Returns a pointer to created copy of the point
        warning: this is not the full copy! Copies only: myParam, myV, myD, myValid
        """

    def hasSolution(self, theRadius: float) -> int:
        """Returns the index of the solution or zero if there is no solution"""

    def LowerValue(self) -> float:
        """For debug only"""

    def remove(self, theIndex: int) -> None:
        """Removes the found value by the given index."""

class ChFi2d_FilletAPI:
    """
    An interface class for 2D fillets.
    Open CASCADE provides two algorithms for 2D fillets:
    ChFi2d_Builder - it constructs a fillet or chamfer
    for linear and circular edges of a face.
    ChFi2d_FilletAPI - it encapsulates two algorithms:
    ChFi2d_AnaFilletAlgo - analytical constructor of the fillet.
    It works only for linear and circular edges,
    having a common point.
    ChFi2d_FilletAlgo - iteration recursive method constructing
    the fillet edge for any type of edges including
    ellipses and b-splines.
    The edges may even have no common point.

    The algorithms ChFi2d_AnaFilletAlgo and ChFi2d_FilletAlgo may be used directly
    or via this ChFi2d_FilletAPI class. This class chooses an appropriate algorithm
    analyzing the arguments (a wire or two edges).
    """

    @overload
    def __init__(self) -> None:
        """
        An empty constructor of the fillet algorithm.
        Call a method Init() to initialize the algorithm
        before calling of a Perform() method.
        """

    @overload
    def __init__(self, theWire: nanoocp.TopoDS.TopoDS_Wire, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        A constructor of a fillet algorithm: accepts a wire consisting of two edges in a plane.
        """

    @overload
    def __init__(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """A constructor of a fillet algorithm: accepts two edges in a plane."""

    @overload
    def __init__(self, theOther: ChFi2d_FilletAPI) -> None: ...

    @overload
    def Init(self, theWire: nanoocp.TopoDS.TopoDS_Wire, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane.
        """

    @overload
    def Init(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """Initializes a fillet algorithm: accepts two edges in a plane."""

    def Perform(self, theRadius: float) -> bool:
        """
        Constructs a fillet edge.
        Returns true if at least one result was found.
        """

    def NbResults(self, thePoint: nanoocp.gp.gp_Pnt) -> int:
        """
        Returns number of possible solutions.
        <thePoint> chooses a particular fillet in case of several fillets
        may be constructed (for example, a circle intersecting a segment in 2 points).
        Put the intersecting (or common) point of the edges.
        """

    def Result(self, thePoint: nanoocp.gp.gp_Pnt, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, iSolution: int = -1) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns result (fillet edge, modified edge1, modified edge2),
        nearest to the given point <thePoint> if iSolution == -1
        <thePoint> chooses a particular fillet in case of several fillets
        may be constructed (for example, a circle intersecting a segment in 2 points).
        Put the intersecting (or common) point of the edges.
        """
