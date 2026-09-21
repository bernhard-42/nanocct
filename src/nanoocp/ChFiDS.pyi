"""OCCT package ChFiDS (toolkit TKFillet)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BRepAdaptor
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Law
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class ChFiDS_ChamfMethod(enum.IntEnum):
    ChFiDS_Sym = 0

    ChFiDS_TwoDist = 1

    ChFiDS_DistAngle = 2

ChFiDS_Sym: ChFiDS_ChamfMethod = ChFiDS_ChamfMethod.ChFiDS_Sym

ChFiDS_TwoDist: ChFiDS_ChamfMethod = ChFiDS_ChamfMethod.ChFiDS_TwoDist

ChFiDS_DistAngle: ChFiDS_ChamfMethod = ChFiDS_ChamfMethod.ChFiDS_DistAngle

class ChFiDS_ChamfMode(enum.IntEnum):
    """this enumeration defines several modes of chamfer"""

    ChFiDS_ClassicChamfer = 0

    ChFiDS_ConstThroatChamfer = 1

    ChFiDS_ConstThroatWithPenetrationChamfer = 2

ChFiDS_ClassicChamfer: ChFiDS_ChamfMode = ChFiDS_ChamfMode.ChFiDS_ClassicChamfer

ChFiDS_ConstThroatChamfer: ChFiDS_ChamfMode = ChFiDS_ChamfMode.ChFiDS_ConstThroatChamfer

ChFiDS_ConstThroatWithPenetrationChamfer: ChFiDS_ChamfMode = ...

class ChFiDS_ErrorStatus(enum.IntEnum):
    """--- Purpose status concerning the cause of the error"""

    ChFiDS_Ok = 0

    ChFiDS_Error = 1

    ChFiDS_WalkingFailure = 2

    ChFiDS_StartsolFailure = 3

    ChFiDS_TwistedSurface = 4

ChFiDS_Ok: ChFiDS_ErrorStatus = ChFiDS_ErrorStatus.ChFiDS_Ok

ChFiDS_Error: ChFiDS_ErrorStatus = ChFiDS_ErrorStatus.ChFiDS_Error

ChFiDS_WalkingFailure: ChFiDS_ErrorStatus = ChFiDS_ErrorStatus.ChFiDS_WalkingFailure

ChFiDS_StartsolFailure: ChFiDS_ErrorStatus = ChFiDS_ErrorStatus.ChFiDS_StartsolFailure

ChFiDS_TwistedSurface: ChFiDS_ErrorStatus = ChFiDS_ErrorStatus.ChFiDS_TwistedSurface

class ChFiDS_State(enum.IntEnum):
    """
    This enum describe the different kinds of extremities
    of a fillet. OnSame, Ondiff and AllSame are
    particular cases of BreakPoint for a corner with 3
    edges and three faces :
    - AllSame means that the three concavities are on the
    same side of the Shape,
    - OnDiff means that the edge of the fillet has a
    concave side different than the two other edges,
    - OnSame means that the edge of the fillet has a
    concave side different than one of the two other edges
    and identical to the third edge.
    """

    ChFiDS_OnSame = 0

    ChFiDS_OnDiff = 1

    ChFiDS_AllSame = 2

    ChFiDS_BreakPoint = 3

    ChFiDS_FreeBoundary = 4

    ChFiDS_Closed = 5

    ChFiDS_Tangent = 6

ChFiDS_OnSame: ChFiDS_State = ChFiDS_State.ChFiDS_OnSame

ChFiDS_OnDiff: ChFiDS_State = ChFiDS_State.ChFiDS_OnDiff

ChFiDS_AllSame: ChFiDS_State = ChFiDS_State.ChFiDS_AllSame

ChFiDS_BreakPoint: ChFiDS_State = ChFiDS_State.ChFiDS_BreakPoint

ChFiDS_FreeBoundary: ChFiDS_State = ChFiDS_State.ChFiDS_FreeBoundary

ChFiDS_Closed: ChFiDS_State = ChFiDS_State.ChFiDS_Closed

ChFiDS_Tangent: ChFiDS_State = ChFiDS_State.ChFiDS_Tangent

class ChFiDS_TypeOfConcavity(enum.IntEnum):
    ChFiDS_Concave = 0

    ChFiDS_Convex = 1

    ChFiDS_Tangential = 2

    ChFiDS_FreeBound = 3

    ChFiDS_Other = 4

    ChFiDS_Mixed = 5

ChFiDS_Concave: ChFiDS_TypeOfConcavity = ChFiDS_TypeOfConcavity.ChFiDS_Concave

ChFiDS_Convex: ChFiDS_TypeOfConcavity = ChFiDS_TypeOfConcavity.ChFiDS_Convex

ChFiDS_Tangential: ChFiDS_TypeOfConcavity = ChFiDS_TypeOfConcavity.ChFiDS_Tangential

ChFiDS_FreeBound: ChFiDS_TypeOfConcavity = ChFiDS_TypeOfConcavity.ChFiDS_FreeBound

ChFiDS_Other: ChFiDS_TypeOfConcavity = ChFiDS_TypeOfConcavity.ChFiDS_Other

ChFiDS_Mixed: ChFiDS_TypeOfConcavity = ChFiDS_TypeOfConcavity.ChFiDS_Mixed

class ChFiDS_ElSpine(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """Elementary Spine for cheminements and approximations."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_ElSpine) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    @overload
    def FirstParameter(self) -> float: ...

    @overload
    def FirstParameter(self, P: float) -> None: ...

    @overload
    def LastParameter(self) -> float: ...

    @overload
    def LastParameter(self, P: float) -> None: ...

    def GetSavedFirstParameter(self) -> float: ...

    def GetSavedLastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Trim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        """

    def Resolution(self, R3d: float) -> float: ...

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def IsPeriodic(self) -> bool: ...

    def SetPeriodic(self, I: bool) -> None: ...

    def Period(self) -> float: ...

    def EvalD0(self, theAbsC: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter theAbsC on the curve."""

    def EvalD1(self, theAbsC: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """Computes the point and first derivative at parameter theAbsC."""

    def EvalD2(self, theAbsC: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """Computes the point and first two derivatives at parameter theAbsC."""

    def EvalD3(self, theAbsC: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """Computes the point and first three derivatives at parameter theAbsC."""

    def SaveFirstParameter(self) -> None: ...

    def SaveLastParameter(self) -> None: ...

    def SetOrigin(self, O: float) -> None: ...

    def FirstPointAndTgt(self, P: nanoocp.gp.gp_Pnt, T: nanoocp.gp.gp_Vec) -> None: ...

    def LastPointAndTgt(self, P: nanoocp.gp.gp_Pnt, T: nanoocp.gp.gp_Vec) -> None: ...

    def NbVertices(self) -> int: ...

    def VertexWithTangent(self, Index: int) -> nanoocp.gp.gp_Ax1: ...

    def SetFirstPointAndTgt(self, P: nanoocp.gp.gp_Pnt, T: nanoocp.gp.gp_Vec) -> None: ...

    def SetLastPointAndTgt(self, P: nanoocp.gp.gp_Pnt, T: nanoocp.gp.gp_Vec) -> None: ...

    def AddVertexWithTangent(self, anAx1: nanoocp.gp.gp_Ax1) -> None: ...

    def SetCurve(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    def Previous(self) -> ChFiDS_SurfData: ...

    def ChangePrevious(self) -> ChFiDS_SurfData: ...

    def Next(self) -> ChFiDS_SurfData: ...

    def ChangeNext(self) -> ChFiDS_SurfData: ...

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

class ChFiDS_Spine(nanoocp.Standard.Standard_Transient):
    """
    Contains information necessary for construction of
    a 3D fillet or chamfer:

    - guideline composed of edges of the solid, tangents
    between them, and borders by faces tangents
    between them.

    Tools for construction of the Sp
    by propagation from an edge of solid
    are provided in the Builder of Fil3d.

    The Spine contains among others the
    information about the nature of extremities
    of the fillet ( on free border , on section or closed ).

    IMPORTANT NOTE: the guideline represented
    in this way is not C2, although the path
    claims it. Several palliative workarounds
    (see the methods at the end) are planned,
    but they are not enough. It is necessary to change
    the approach and double the Spine of line C2 with
    the known consequences for management of
    interactions between KPart Blend in Fil3d.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Tol: float) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_Spine) -> None: ...

    def SetEdges(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """store edges composing the guideline"""

    def SetOffsetEdges(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """store offset edges composing the offset guideline"""

    def PutInFirst(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """store the edge at the first position before all others"""

    def PutInFirstOffset(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """store the offset edge at the first position before all others"""

    def NbEdges(self) -> int: ...

    def Edges(self, I: int) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def OffsetEdges(self, I: int) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def SetFirstStatus(self, S: ChFiDS_State) -> None:
        """
        stores if the start of a set of edges starts on a
        section of free border or forms a closed contour
        """

    def SetLastStatus(self, S: ChFiDS_State) -> None:
        """
        stores if the end of a set of edges starts on a
        section of free border or forms a closed contour
        """

    def AppendElSpine(self, Els: ChFiDS_ElSpine | None) -> None: ...

    def AppendOffsetElSpine(self, Els: ChFiDS_ElSpine | None) -> None: ...

    @overload
    def ElSpine(self, IE: int) -> ChFiDS_ElSpine: ...

    @overload
    def ElSpine(self, E: nanoocp.TopoDS.TopoDS_Edge) -> ChFiDS_ElSpine: ...

    @overload
    def ElSpine(self, W: float) -> ChFiDS_ElSpine: ...

    def ChangeElSpines(self) -> nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_ElSpine]: ...

    def ChangeOffsetElSpines(self) -> nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_ElSpine]: ...

    def Reset(self, AllData: bool = False) -> None: ...

    @overload
    def SplitDone(self) -> bool: ...

    @overload
    def SplitDone(self, B: bool) -> None: ...

    def Load(self) -> None:
        """
        prepare the guideline depending on the edges that
        are elementary arks (take parameters from
        a single curvilinear abscissa); to be able to call
        methods on the geometry (first,last,value,d1,d2)
        it is necessary to start with preparation otherwise an
        exception will be raised
        """

    def Resolution(self, R3d: float) -> float: ...

    def IsClosed(self) -> bool: ...

    @overload
    def FirstParameter(self) -> float: ...

    @overload
    def FirstParameter(self, IndexSpine: int) -> float:
        """
        gives the total length of all arcs before the
        number IndexSp
        """

    @overload
    def LastParameter(self) -> float: ...

    @overload
    def LastParameter(self, IndexSpine: int) -> float:
        """
        gives the total length till the ark with number
        IndexSpine (inclus)
        """

    def SetFirstParameter(self, Par: float) -> None: ...

    def SetLastParameter(self, Par: float) -> None: ...

    def Length(self, IndexSpine: int) -> float:
        """gives the length of ark with number IndexSp"""

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    @overload
    def Absc(self, U: float) -> float: ...

    @overload
    def Absc(self, U: float, I: int) -> float: ...

    @overload
    def Absc(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> float: ...

    @overload
    def Parameter(self, AbsC: float, Oriented: bool = True) -> float: ...

    @overload
    def Parameter(self, Index: int, AbsC: float, Oriented: bool = True) -> float: ...

    def Value(self, AbsC: float) -> nanoocp.gp.gp_Pnt: ...

    def D0(self, AbsC: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    def D1(self, AbsC: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    def D2(self, AbsC: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    def SetCurrent(self, Index: int) -> None: ...

    def CurrentElementarySpine(self, Index: int) -> nanoocp.BRepAdaptor.BRepAdaptor_Curve:
        """sets the current curve and returns it"""

    def CurrentIndexOfElementarySpine(self) -> int: ...

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def FirstStatus(self) -> ChFiDS_State:
        """
        returns if the set of edges starts on a free boundary
        or if the first vertex is a breakpoint or if the set is
        closed
        """

    def LastStatus(self) -> ChFiDS_State:
        """returns the state at the end of the set"""

    def Status(self, IsFirst: bool) -> ChFiDS_State: ...

    def GetTypeOfConcavity(self) -> ChFiDS_TypeOfConcavity:
        """returns the type of concavity in the connection"""

    def SetStatus(self, S: ChFiDS_State, IsFirst: bool) -> None: ...

    def SetTypeOfConcavity(self, theType: ChFiDS_TypeOfConcavity) -> None:
        """sets the type of concavity in the connection"""

    def IsTangencyExtremity(self, IsFirst: bool) -> bool:
        """
        returns if the set of edges starts (or end) on
        Tangency point.
        """

    def SetTangencyExtremity(self, IsTangency: bool, IsFirst: bool) -> None: ...

    def FirstVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def LastVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def SetFirstTgt(self, W: float) -> None: ...

    def SetLastTgt(self, W: float) -> None: ...

    def HasFirstTgt(self) -> bool: ...

    def HasLastTgt(self) -> bool: ...

    @overload
    def SetReference(self, W: float) -> None:
        """set a parameter reference for the approx."""

    @overload
    def SetReference(self, I: int) -> None:
        """
        set a parameter reference for the approx, at the
        middle of edge I.
        """

    @overload
    def Index(self, W: float, Forward: bool = True) -> int: ...

    @overload
    def Index(self, E: nanoocp.TopoDS.TopoDS_Edge) -> int: ...

    def UnsetReference(self) -> None: ...

    def SetErrorStatus(self, state: ChFiDS_ErrorStatus) -> None: ...

    def ErrorStatus(self) -> ChFiDS_ErrorStatus: ...

    def Mode(self) -> ChFiDS_ChamfMode:
        """Return the mode of chamfers used"""

    def GetTolesp(self) -> float:
        """Return tolesp parameter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ChFiDS_ChamfSpine(ChFiDS_Spine):
    """
    Provides data specific to chamfers
    distances on each of faces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Tol: float) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_ChamfSpine) -> None: ...

    def SetDist(self, Dis: float) -> None: ...

    def GetDist(self) -> float: ...

    def SetDists(self, Dis1: float, Dis2: float) -> None: ...

    def Dists(self) -> tuple[float, float]: ...

    def GetDistAngle(self) -> tuple[float, float]: ...

    def SetDistAngle(self, Dis: float, Angle: float) -> None: ...

    def SetMode(self, theMode: ChFiDS_ChamfMode) -> None: ...

    def IsChamfer(self) -> ChFiDS_ChamfMethod:
        """Return the method of chamfers used"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ChFiDS_CircSection:
    """A Section of fillet."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_CircSection) -> None: ...

    @overload
    def Set(self, C: nanoocp.gp.gp_Circ, F: float, L: float) -> None: ...

    @overload
    def Set(self, C: nanoocp.gp.gp_Lin, F: float, L: float) -> None: ...

    @overload
    def Get(self, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Get(self, C: nanoocp.gp.gp_Lin) -> tuple[float, float]: ...

class ChFiDS_CommonPoint:
    """
    point start/end of fillet common to 2 adjacent filets
    and to an edge on one of 2 faces participating
    in the construction of the fillet
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ChFiDS_CommonPoint) -> None: ...

    def Reset(self) -> None:
        """default value for all fields"""

    def SetVertex(self, theVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Sets the values of a point which is a vertex on
        the initial facet of restriction of one
        of the surface.
        """

    def SetArc(self, Tol: float, A: nanoocp.TopoDS.TopoDS_Edge, Param: float, TArc: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the values of a point which is on the arc
        A, at parameter Param.
        """

    def SetParameter(self, Param: float) -> None:
        """Sets the value of the parameter on the spine"""

    def SetPoint(self, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Set the 3d point for a commonpoint that is not
        a vertex or on an arc.
        """

    def SetVector(self, theVector: nanoocp.gp.gp_Vec) -> None:
        """Set the output 3d vector"""

    def SetTolerance(self, Tol: float) -> None:
        """This method set the fuzziness on the point."""

    def Tolerance(self) -> float:
        """This method returns the fuzziness on the point."""

    def IsVertex(self) -> bool:
        """
        Returns TRUE if the point is a vertex on the initial
        restriction facet of the surface.
        """

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the information about the point when it is
        on the domain of the first patch, i-e when the function
        IsVertex returns True.
        Otherwise, an exception is raised.
        """

    def IsOnArc(self) -> bool:
        """
        Returns TRUE if the point is a on an edge of the initial
        restriction facet of the surface.
        """

    def Arc(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the arc of restriction containing the
        vertex.
        """

    def TransitionOnArc(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the transition of the point on the arc
        returned by Arc().
        """

    def ParameterOnArc(self) -> float:
        """
        Returns the parameter of the point on the
        arc returned by the method Arc().
        """

    def Parameter(self) -> float:
        """Returns the parameter on the spine"""

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """Returns the 3d point"""

    def HasVector(self) -> bool:
        """Returns TRUE if the output vector is stored."""

    def Vector(self) -> nanoocp.gp.gp_Vec:
        """Returns the output 3d vector"""

class ChFiDS_FaceInterference:
    """interference face/fillet"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_FaceInterference) -> None: ...

    def SetInterference(self, LineIndex: int, Trans: nanoocp.TopAbs.TopAbs_Orientation, PCurv1: nanoocp.Geom2d.Geom2d_Curve | None, PCurv2: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    def SetTransition(self, Trans: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def SetFirstParameter(self, U1: float) -> None: ...

    def SetLastParameter(self, U1: float) -> None: ...

    def SetParameter(self, U1: float, IsFirst: bool) -> None: ...

    def LineIndex(self) -> int: ...

    def SetLineIndex(self, I: int) -> None: ...

    def Transition(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def PCurveOnFace(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def PCurveOnSurf(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangePCurveOnFace(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangePCurveOnSurf(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Parameter(self, IsFirst: bool) -> float: ...

class ChFiDS_FilSpine(ChFiDS_Spine):
    """
    Provides data specific to the fillets -
    vector or rule of evolution (C2).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Tol: float) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_FilSpine) -> None: ...

    def Reset(self, AllData: bool = False) -> None: ...

    @overload
    def SetRadius(self, Radius: float, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """initializes the constant vector on edge E."""

    @overload
    def SetRadius(self, Radius: float, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """initializes the vector on Vertex V."""

    @overload
    def SetRadius(self, UandR: nanoocp.gp.gp_XY, IinC: int) -> None:
        """initializes the vector on the point of parameter W."""

    @overload
    def SetRadius(self, Radius: float) -> None:
        """initializes the constant vector on all spine."""

    @overload
    def SetRadius(self, C: nanoocp.Law.Law_Function | None, IinC: int) -> None:
        """initializes the rule of evolution on all spine."""

    @overload
    def UnSetRadius(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """resets the constant vector on edge E."""

    @overload
    def UnSetRadius(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """resets the vector on Vertex V."""

    @overload
    def IsConstant(self) -> bool:
        """
        returns true if the radius is constant
        all along the spine.
        """

    @overload
    def IsConstant(self, IE: int) -> bool:
        """
        returns true if the radius is constant
        all along the edge E.
        """

    @overload
    def Radius(self) -> float:
        """
        returns the radius if the fillet is constant
        all along the spine.
        """

    @overload
    def Radius(self, IE: int) -> float: ...

    @overload
    def Radius(self, E: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """
        returns the radius if the fillet is constant
        all along the edge E.
        """

    def AppendElSpine(self, Els: ChFiDS_ElSpine | None) -> None: ...

    def Law(self, Els: ChFiDS_ElSpine | None) -> nanoocp.Law.Law_Composite: ...

    def ChangeLaw(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.Law.Law_Function:
        """returns the elementary law"""

    def MaxRadFromSeqAndLaws(self) -> float:
        """returns the maximum radius if the fillet is non-constant"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ChFiDS_Map:
    """Encapsulation of IndexedDataMapOfShapeListOfShape."""

    @overload
    def __init__(self) -> None:
        """Create an empty Map"""

    @overload
    def __init__(self, theOther: ChFiDS_Map) -> None: ...

    def Fill(self, S: nanoocp.TopoDS.TopoDS_Shape, T1: nanoocp.TopAbs.TopAbs_ShapeEnum, T2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        Fills the map with the subshapes of type T1 as keys
        and the list of ancestors of type T2 as items.
        """

    def Contains(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def FindFromKey(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def __call__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def __call__(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def FindFromIndex(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class ChFiDS_Regul:
    """Storage of a curve and its 2 faces or surfaces of support."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_Regul) -> None: ...

    def SetCurve(self, IC: int) -> None: ...

    def SetS1(self, IS1: int, IsFace: bool = True) -> None: ...

    def SetS2(self, IS2: int, IsFace: bool = True) -> None: ...

    def IsSurface1(self) -> bool: ...

    def IsSurface2(self) -> bool: ...

    def Curve(self) -> int: ...

    def S1(self) -> int: ...

    def S2(self) -> int: ...

class ChFiDS_SurfData(nanoocp.Standard.Standard_Transient):
    """
    data structure for all information related to the
    fillet and to 2 faces vis a vis
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_SurfData) -> None: ...

    def Copy(self, Other: ChFiDS_SurfData | None) -> None: ...

    def IndexOfS1(self) -> int: ...

    def IndexOfS2(self) -> int: ...

    def IsOnCurve1(self) -> bool: ...

    def IsOnCurve2(self) -> bool: ...

    def IndexOfC1(self) -> int: ...

    def IndexOfC2(self) -> int: ...

    def Surf(self) -> int: ...

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def InterferenceOnS1(self) -> ChFiDS_FaceInterference: ...

    def InterferenceOnS2(self) -> ChFiDS_FaceInterference: ...

    def VertexFirstOnS1(self) -> ChFiDS_CommonPoint: ...

    def VertexFirstOnS2(self) -> ChFiDS_CommonPoint: ...

    def VertexLastOnS1(self) -> ChFiDS_CommonPoint: ...

    def VertexLastOnS2(self) -> ChFiDS_CommonPoint: ...

    def ChangeIndexOfS1(self, Index: int) -> None: ...

    def ChangeIndexOfS2(self, Index: int) -> None: ...

    def ChangeSurf(self, Index: int) -> None: ...

    def SetIndexOfC1(self, Index: int) -> None: ...

    def SetIndexOfC2(self, Index: int) -> None: ...

    def ChangeOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def SetOrientation(self, theValue: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Python addition: sets the value ChangeOrientation() returns by reference in C++.
        """

    def ChangeInterferenceOnS1(self) -> ChFiDS_FaceInterference: ...

    def ChangeInterferenceOnS2(self) -> ChFiDS_FaceInterference: ...

    def ChangeVertexFirstOnS1(self) -> ChFiDS_CommonPoint: ...

    def ChangeVertexFirstOnS2(self) -> ChFiDS_CommonPoint: ...

    def ChangeVertexLastOnS1(self) -> ChFiDS_CommonPoint: ...

    def ChangeVertexLastOnS2(self) -> ChFiDS_CommonPoint: ...

    def Interference(self, OnS: int) -> ChFiDS_FaceInterference: ...

    def ChangeInterference(self, OnS: int) -> ChFiDS_FaceInterference: ...

    def Index(self, OfS: int) -> int: ...

    def Vertex(self, First: bool, OnS: int) -> ChFiDS_CommonPoint:
        """
        returns one of the four vertices whether First is true
        or wrong and OnS equals 1 or 2.
        """

    def ChangeVertex(self, First: bool, OnS: int) -> ChFiDS_CommonPoint:
        """
        returns one of the four vertices whether First is true
        or wrong and OnS equals 1 or 2.
        """

    def IsOnCurve(self, OnS: int) -> bool: ...

    def IndexOfC(self, OnS: int) -> int: ...

    @overload
    def FirstSpineParam(self) -> float: ...

    @overload
    def FirstSpineParam(self, Par: float) -> None: ...

    @overload
    def LastSpineParam(self) -> float: ...

    @overload
    def LastSpineParam(self, Par: float) -> None: ...

    @overload
    def FirstExtensionValue(self) -> float: ...

    @overload
    def FirstExtensionValue(self, Extend: float) -> None: ...

    @overload
    def LastExtensionValue(self) -> float: ...

    @overload
    def LastExtensionValue(self, Extend: float) -> None: ...

    def Simul(self) -> nanoocp.Standard.Standard_Transient: ...

    def SetSimul(self, S: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def ResetSimul(self) -> None: ...

    @overload
    def Get2dPoints(self, First: bool, OnS: int) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    def Get2dPoints(self, P2df1: nanoocp.gp.gp_Pnt2d, P2dl1: nanoocp.gp.gp_Pnt2d, P2df2: nanoocp.gp.gp_Pnt2d, P2dl2: nanoocp.gp.gp_Pnt2d) -> None: ...

    def Set2dPoints(self, P2df1: nanoocp.gp.gp_Pnt2d, P2dl1: nanoocp.gp.gp_Pnt2d, P2df2: nanoocp.gp.gp_Pnt2d, P2dl2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def TwistOnS1(self) -> bool: ...

    @overload
    def TwistOnS1(self, T: bool) -> None: ...

    @overload
    def TwistOnS2(self) -> bool: ...

    @overload
    def TwistOnS2(self, T: bool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ChFiDS_Stripe(nanoocp.Standard.Standard_Transient):
    """Data characterising a band of fillet."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_Stripe) -> None: ...

    def Reset(self) -> None:
        """Reset everything except Spine."""

    def SetOfSurfData(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.ChFiDS.ChFiDS_SurfData]: ...

    def Spine(self) -> ChFiDS_Spine: ...

    @overload
    def OrientationOnFace1(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def OrientationOnFace1(self, Or1: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def OrientationOnFace2(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def OrientationOnFace2(self, Or2: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Choix(self) -> int: ...

    @overload
    def Choix(self, C: int) -> None: ...

    def ChangeSetOfSurfData(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.ChFiDS.ChFiDS_SurfData]: ...

    def ChangeSpine(self) -> ChFiDS_Spine: ...

    def FirstParameters(self) -> tuple[float, float]: ...

    def LastParameters(self) -> tuple[float, float]: ...

    def ChangeFirstParameters(self, Pdeb: float, Pfin: float) -> None: ...

    def ChangeLastParameters(self, Pdeb: float, Pfin: float) -> None: ...

    def FirstCurve(self) -> int: ...

    def LastCurve(self) -> int: ...

    def ChangeFirstCurve(self, Index: int) -> None: ...

    def ChangeLastCurve(self, Index: int) -> None: ...

    def FirstPCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def LastPCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangeFirstPCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangeLastPCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def FirstPCurveOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def FirstPCurveOrientation(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def LastPCurveOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def LastPCurveOrientation(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def IndexFirstPointOnS1(self) -> int: ...

    def IndexFirstPointOnS2(self) -> int: ...

    def IndexLastPointOnS1(self) -> int: ...

    def IndexLastPointOnS2(self) -> int: ...

    def ChangeIndexFirstPointOnS1(self, Index: int) -> None: ...

    def ChangeIndexFirstPointOnS2(self, Index: int) -> None: ...

    def ChangeIndexLastPointOnS1(self, Index: int) -> None: ...

    def ChangeIndexLastPointOnS2(self, Index: int) -> None: ...

    def Parameters(self, First: bool) -> tuple[float, float]: ...

    def SetParameters(self, First: bool, Pdeb: float, Pfin: float) -> None: ...

    def Curve(self, First: bool) -> int: ...

    def SetCurve(self, Index: int, First: bool) -> None: ...

    def PCurve(self, First: bool) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangePCurve(self, First: bool) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def Orientation(self, OnS: int) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def Orientation(self, First: bool) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def SetOrientation(self, Or: nanoocp.TopAbs.TopAbs_Orientation, OnS: int) -> None: ...

    @overload
    def SetOrientation(self, Or: nanoocp.TopAbs.TopAbs_Orientation, First: bool) -> None: ...

    def IndexPoint(self, First: bool, OnS: int) -> int: ...

    def SetIndexPoint(self, Index: int, First: bool, OnS: int) -> None: ...

    def SolidIndex(self) -> int: ...

    def SetSolidIndex(self, Index: int) -> None: ...

    def InDS(self, First: bool, Nb: int = 1) -> None:
        """Set nb of SurfData's at end put in DS"""

    def IsInDS(self, First: bool) -> int:
        """Returns nb of SurfData's at end being in DS"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ChFiDS_StripeMap:
    """encapsulation of IndexedDataMapOfVertexListOfStripe"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiDS_StripeMap) -> None: ...

    def Add(self, V: nanoocp.TopoDS.TopoDS_Vertex, F: ChFiDS_Stripe | None) -> None: ...

    def Extent(self) -> int: ...

    def FindFromKey(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Stripe]: ...

    @overload
    def __call__(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Stripe]: ...

    @overload
    def __call__(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Stripe]: ...

    def FindFromIndex(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Stripe]: ...

    def FindKey(self, I: int) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Clear(self) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.ChFiDS
ChFiDS_HData = nanoocp.NCollection.NCollection_HSequence[nanoocp.ChFiDS.ChFiDS_SurfData]
ChFiDS_ListOfHElSpine = nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_ElSpine]
ChFiDS_ListOfStripe = nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Stripe]
ChFiDS_Regularities = nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Regul]
ChFiDS_SecArray1 = nanoocp.NCollection.NCollection_Array1[nanoocp.ChFiDS.ChFiDS_CircSection]
ChFiDS_SecHArray1 = nanoocp.NCollection.NCollection_HArray1[nanoocp.ChFiDS.ChFiDS_CircSection]
ChFiDS_SequenceOfSurfData = nanoocp.NCollection.NCollection_Sequence[nanoocp.ChFiDS.ChFiDS_SurfData]
