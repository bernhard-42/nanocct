"""OCCT package HLRBRep (toolkit TKHLR)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BRepAdaptor
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.HLRAlgo
import nanoocp.HLRTopoBRep
import nanoocp.IntCurveSurface
import nanoocp.IntRes2d
import nanoocp.IntSurf
import nanoocp.Intf
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.math


class HLRBRep_TypeOfResultingEdge(enum.IntEnum):
    """Identifies the type of resulting edge of HLRBRep_Algo"""

    HLRBRep_Undefined = 0

    HLRBRep_IsoLine = 1

    HLRBRep_OutLine = 2

    HLRBRep_Rg1Line = 3

    HLRBRep_RgNLine = 4

    HLRBRep_Sharp = 5

HLRBRep_Undefined: HLRBRep_TypeOfResultingEdge = HLRBRep_TypeOfResultingEdge.HLRBRep_Undefined

HLRBRep_IsoLine: HLRBRep_TypeOfResultingEdge = HLRBRep_TypeOfResultingEdge.HLRBRep_IsoLine

HLRBRep_OutLine: HLRBRep_TypeOfResultingEdge = HLRBRep_TypeOfResultingEdge.HLRBRep_OutLine

HLRBRep_Rg1Line: HLRBRep_TypeOfResultingEdge = HLRBRep_TypeOfResultingEdge.HLRBRep_Rg1Line

HLRBRep_RgNLine: HLRBRep_TypeOfResultingEdge = HLRBRep_TypeOfResultingEdge.HLRBRep_RgNLine

HLRBRep_Sharp: HLRBRep_TypeOfResultingEdge = HLRBRep_TypeOfResultingEdge.HLRBRep_Sharp

class HLRBRep:
    """
    Hidden Lines Removal
    algorithms on the BRep DataStructure.

    The class PolyAlgo is used to remove Hidden lines
    on Shapes with Triangulations.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep) -> None: ...

    @staticmethod
    def MakeEdge(ec: HLRBRep_Curve, U1: float, U2: float) -> nanoocp.TopoDS.TopoDS_Edge: ...

    @staticmethod
    def MakeEdge3d(ec: HLRBRep_Curve, U1: float, U2: float) -> nanoocp.TopoDS.TopoDS_Edge: ...

    @staticmethod
    def PolyHLRAngleAndDeflection(InAngl: float) -> tuple[float, float]: ...

class HLRBRep_ShapeBounds:
    """
    Contains a Shape and the bounds of its vertices,
    edges and faces in the DataStructure.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None, nbIso: int, V1: int, V2: int, E1: int, E2: int, F1: int, F2: int) -> None: ...

    @overload
    def __init__(self, S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None, SData: nanoocp.Standard.Standard_Transient | None, nbIso: int, V1: int, V2: int, E1: int, E2: int, F1: int, F2: int) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_ShapeBounds) -> None: ...

    def Translate(self, NV: int, NE: int, NF: int) -> None: ...

    @overload
    def Shape(self, S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None) -> None: ...

    @overload
    def Shape(self) -> nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner: ...

    @overload
    def ShapeData(self, SD: nanoocp.Standard.Standard_Transient | None) -> None: ...

    @overload
    def ShapeData(self) -> nanoocp.Standard.Standard_Transient: ...

    @overload
    def NbOfIso(self, nbIso: int) -> None: ...

    @overload
    def NbOfIso(self) -> int: ...

    def Sizes(self) -> tuple[int, int, int]: ...

    def Bounds(self) -> tuple[int, int, int, int, int, int]: ...

    def UpdateMinMax(self, theTotMinMax: nanoocp.HLRAlgo.HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    def MinMax(self) -> nanoocp.HLRAlgo.HLRAlgo_EdgesBlock.MinMaxIndices: ...

class HLRBRep_InternalAlgo(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, A: HLRBRep_InternalAlgo | None) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_InternalAlgo) -> None: ...

    @overload
    def Projector(self, P: nanoocp.HLRAlgo.HLRAlgo_Projector) -> None: ...

    @overload
    def Projector(self) -> nanoocp.HLRAlgo.HLRAlgo_Projector:
        """set the projector."""

    def Update(self) -> None:
        """update the DataStructure."""

    @overload
    def Load(self, S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None, SData: nanoocp.Standard.Standard_Transient | None, nbIso: int = 0) -> None: ...

    @overload
    def Load(self, S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None, nbIso: int = 0) -> None:
        """add the shape <S>."""

    def Index(self, S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None) -> int:
        """
        return the index of the Shape <S> and return 0 if
        the Shape <S> is not found.
        """

    def Remove(self, I: int) -> None:
        """remove the Shape of Index <I>."""

    def ShapeData(self, I: int, SData: nanoocp.Standard.Standard_Transient | None) -> None:
        """Change the Shape Data of the Shape of index <I>."""

    def SeqOfShapeBounds(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.HLRBRep.HLRBRep_ShapeBounds]: ...

    def NbShapes(self) -> int: ...

    def ShapeBounds(self, I: int) -> HLRBRep_ShapeBounds: ...

    def InitEdgeStatus(self) -> None:
        """
        init the status of the selected edges depending of
        the back faces of a closed shell.
        """

    @overload
    def Select(self) -> None:
        """select all the DataStructure."""

    @overload
    def Select(self, I: int) -> None:
        """select only the Shape of index <I>."""

    def SelectEdge(self, I: int) -> None:
        """select only the edges of the Shape <S>."""

    def SelectFace(self, I: int) -> None:
        """select only the faces of the Shape <S>."""

    @overload
    def ShowAll(self) -> None:
        """set to visible all the edges."""

    @overload
    def ShowAll(self, I: int) -> None:
        """set to visible all the edges of the Shape <S>."""

    @overload
    def HideAll(self) -> None:
        """set to hide all the edges."""

    @overload
    def HideAll(self, I: int) -> None:
        """set to hide all the edges of the Shape <S>."""

    def PartialHide(self) -> None:
        """
        own hiding of all the shapes of the DataStructure
        without hiding by each other.
        """

    @overload
    def Hide(self) -> None:
        """hide all the DataStructure."""

    @overload
    def Hide(self, I: int) -> None:
        """hide the Shape <S> by itself."""

    @overload
    def Hide(self, I: int, J: int) -> None:
        """hide the Shape <S1> by the shape <S2>."""

    @overload
    def Debug(self, deb: bool) -> None: ...

    @overload
    def Debug(self) -> bool: ...

    def DataStructure(self) -> HLRBRep_Data: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRBRep_Algo(HLRBRep_InternalAlgo):
    """
    Inherited from InternalAlgo to provide methods with Shape from TopoDS.
    A framework to compute a shape as seen in a projection plane. This is done by
    calculating the visible and the hidden parts of the shape.
    HLRBRep_Algo works with three types of entity:
    -   shapes to be visualized
    -   edges in these shapes (these edges are
    the basic entities which will be visualized or hidden), and
    -   faces in these shapes which hide the edges.
    HLRBRep_Algo is based on the principle of comparing each edge of the shape to be
    visualized with each of its faces, and calculating the visible and the hidden parts of each
    edge. For a given projection, HLRBRep_Algo calculates a set of lines characteristic of the
    object being represented. It is also used in conjunction with the
    HLRBRep_HLRToShape extraction utilities, which reconstruct a new, simplified shape
    from a selection of calculation results. This new shape is made up of edges, which
    represent the shape visualized in the projection.
    HLRBRep_Algo takes the shape itself into account whereas HLRBRep_PolyAlgo
    works with a polyhedral simplification of the shape. When you use HLRBRep_Algo, you
    obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce
    computation time but obtain polygonal segments. In the case of complicated
    shapes, HLRBRep_Algo may be time-consuming.
    An HLRBRep_Algo object provides a framework for:
    -   defining the point of view
    -   identifying the shape or shapes to be visualized
    -   calculating the outlines
    -   calculating the visible and hidden lines of the shape.
    Warning
    -   Superimposed lines are not eliminated by this algorithm.
    -   There must be no unfinished objects inside the shape you wish to visualize.
    -   Points are not treated.
    -   Note that this is not the sort of algorithm used in generating shading, which
    calculates the visible and hidden parts of each face in a shape to be visualized by
    comparing each face in the shape with every other face in the same shape.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty framework for the
        calculation of visible and hidden lines of a shape in a projection.
        Use the function:
        -   Projector to define the point of view
        -   Add to select the shape or shapes to be visualized
        -   Update to compute the outlines of the shape, and
        -   Hide to compute the visible and hidden lines of the shape.
        """

    @overload
    def __init__(self, A: HLRBRep_Algo | None) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_Algo) -> None: ...

    @overload
    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape, SData: nanoocp.Standard.Standard_Transient | None, nbIso: int = 0) -> None:
        """add the Shape <S>."""

    @overload
    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape, nbIso: int = 0) -> None:
        """
        Adds the shape S to this framework, and
        specifies the number of isoparameters nbiso desired in visualizing S.
        You may add as many shapes as you wish. Use the function Add once for each shape.
        """

    def Index(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        return the index of the Shape <S> and
        return 0 if the Shape <S> is not found.
        """

    def OutLinedShapeNullify(self) -> None:
        """nullify all the results of OutLiner from HLRTopoBRep."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRBRep_AreaLimit(nanoocp.Standard.Standard_Transient):
    """
    The private nested class AreaLimit represents a
    vertex on the Edge with the state on the left and
    the right.
    """

    @overload
    def __init__(self, V: nanoocp.HLRAlgo.HLRAlgo_Intersection, Boundary: bool, Interference: bool, StateBefore: nanoocp.TopAbs.TopAbs_State, StateAfter: nanoocp.TopAbs.TopAbs_State, EdgeBefore: nanoocp.TopAbs.TopAbs_State, EdgeAfter: nanoocp.TopAbs.TopAbs_State) -> None:
        """The previous and next field are set to NULL."""

    @overload
    def __init__(self, theOther: HLRBRep_AreaLimit) -> None: ...

    @overload
    def StateBefore(self, St: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def StateBefore(self) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def StateAfter(self, St: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def StateAfter(self) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def EdgeBefore(self, St: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def EdgeBefore(self) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def EdgeAfter(self, St: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def EdgeAfter(self) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def Previous(self, P: HLRBRep_AreaLimit | None) -> None: ...

    @overload
    def Previous(self) -> HLRBRep_AreaLimit: ...

    @overload
    def Next(self, N: HLRBRep_AreaLimit | None) -> None: ...

    @overload
    def Next(self) -> HLRBRep_AreaLimit: ...

    def Vertex(self) -> nanoocp.HLRAlgo.HLRAlgo_Intersection: ...

    def IsBoundary(self) -> bool: ...

    def IsInterference(self) -> bool: ...

    def Clear(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRBRep_BCurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_BCurveTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> float: ...

    @staticmethod
    def Continuity(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(myclass) >= <S>
        """

    @staticmethod
    def Intervals(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    @staticmethod
    def IsClosed(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> bool: ...

    @staticmethod
    def IsPeriodic(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> bool: ...

    @staticmethod
    def Period(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> float: ...

    @staticmethod
    def Value(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D0(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D1(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    @staticmethod
    def D2(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    @staticmethod
    def D3(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    @staticmethod
    def DN(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    @staticmethod
    def Resolution(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.gp.gp_Lin: ...

    @staticmethod
    def Circle(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.gp.gp_Circ: ...

    @staticmethod
    def Ellipse(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.gp.gp_Elips: ...

    @staticmethod
    def Hyperbola(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.gp.gp_Hypr: ...

    @staticmethod
    def Parabola(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.gp.gp_Parab: ...

    @staticmethod
    def Bezier(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.Geom.Geom_BezierCurve: ...

    @staticmethod
    def BSpline(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @staticmethod
    def Degree(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> int: ...

    @staticmethod
    def IsRational(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> bool: ...

    @staticmethod
    def NbPoles(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> int: ...

    @staticmethod
    def NbKnots(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> int: ...

    @staticmethod
    def Poles(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, T: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @staticmethod
    def PolesAndWeights(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, T: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def NbSamples(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U0: float, U1: float) -> int: ...

class HLRBRep_BiPnt2D:
    """Contains the colors of a shape."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, thePoint1: nanoocp.gp.gp_XY, thePoint2: nanoocp.gp.gp_XY, S: nanoocp.TopoDS.TopoDS_Shape, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...

    @overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float, S: nanoocp.TopoDS.TopoDS_Shape, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_BiPnt2D) -> None: ...

    def P1(self) -> nanoocp.gp.gp_Pnt2d: ...

    def P2(self) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Shape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Rg1Line(self) -> bool: ...

    @overload
    def Rg1Line(self, B: bool) -> None: ...

    @overload
    def RgNLine(self) -> bool: ...

    @overload
    def RgNLine(self, B: bool) -> None: ...

    @overload
    def OutLine(self) -> bool: ...

    @overload
    def OutLine(self, B: bool) -> None: ...

    @overload
    def IntLine(self) -> bool: ...

    @overload
    def IntLine(self, B: bool) -> None: ...

class HLRBRep_BiPoint:
    """Contains the colors of a shape."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, S: nanoocp.TopoDS.TopoDS_Shape, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_BiPoint) -> None: ...

    def P1(self) -> nanoocp.gp.gp_Pnt: ...

    def P2(self) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Shape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Rg1Line(self) -> bool: ...

    @overload
    def Rg1Line(self, B: bool) -> None: ...

    @overload
    def RgNLine(self) -> bool: ...

    @overload
    def RgNLine(self, B: bool) -> None: ...

    @overload
    def OutLine(self) -> bool: ...

    @overload
    def OutLine(self, B: bool) -> None: ...

    @overload
    def IntLine(self) -> bool: ...

    @overload
    def IntLine(self, B: bool) -> None: ...

class HLRBRep_BSurfaceTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_BSurfaceTool) -> None: ...

    @staticmethod
    def FirstUParameter(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> float: ...

    @staticmethod
    def FirstVParameter(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> float: ...

    @staticmethod
    def LastUParameter(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> float: ...

    @staticmethod
    def LastVParameter(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> float: ...

    @staticmethod
    def NbUIntervals(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, Sh: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    @staticmethod
    def NbVIntervals(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, Sh: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    @staticmethod
    def UIntervals(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, T: nanoocp.NCollection.NCollection_Array1[float], Sh: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @staticmethod
    def VIntervals(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, T: nanoocp.NCollection.NCollection_Array1[float], Sh: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @staticmethod
    def UTrim(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """If <First> >= <Last>"""

    @staticmethod
    def VTrim(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """If <First> >= <Last>"""

    @staticmethod
    def IsUClosed(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def IsVClosed(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def IsUPeriodic(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def UPeriod(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> float: ...

    @staticmethod
    def IsVPeriodic(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def VPeriod(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> float: ...

    @staticmethod
    def Value(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u: float, v: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def D0(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u: float, v: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def D1(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u: float, v: float, P: nanoocp.gp.gp_Pnt, D1u: nanoocp.gp.gp_Vec, D1v: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D2(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u: float, v: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec, D2U: nanoocp.gp.gp_Vec, D2V: nanoocp.gp.gp_Vec, D2UV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D3(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u: float, v: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec, D2U: nanoocp.gp.gp_Vec, D2V: nanoocp.gp.gp_Vec, D2UV: nanoocp.gp.gp_Vec, D3U: nanoocp.gp.gp_Vec, D3V: nanoocp.gp.gp_Vec, D3UUV: nanoocp.gp.gp_Vec, D3UVV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def DN(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u: float, v: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def UContinuity(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def VContinuity(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def UDegree(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @staticmethod
    def NbUPoles(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @staticmethod
    def NbUKnots(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @staticmethod
    def IsURational(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def VDegree(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @staticmethod
    def NbVPoles(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @staticmethod
    def NbVKnots(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @staticmethod
    def IsVRational(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def UResolution(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, R3d: float) -> float: ...

    @staticmethod
    def VResolution(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, R3d: float) -> float: ...

    @staticmethod
    def GetType(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.GeomAbs.GeomAbs_SurfaceType: ...

    @staticmethod
    def Plane(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Pln: ...

    @staticmethod
    def Cylinder(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Cylinder: ...

    @staticmethod
    def Cone(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Cone: ...

    @staticmethod
    def Torus(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Torus: ...

    @staticmethod
    def Sphere(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Sphere: ...

    @staticmethod
    def Bezier(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.Geom.Geom_BezierSurface: ...

    @staticmethod
    def BSpline(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.Geom.Geom_BSplineSurface: ...

    @staticmethod
    def AxeOfRevolution(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Ax1: ...

    @staticmethod
    def Direction(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.gp.gp_Dir: ...

    @staticmethod
    def BasisCurve(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    @overload
    @staticmethod
    def NbSamplesU(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @overload
    @staticmethod
    def NbSamplesU(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, u1: float, u2: float) -> int: ...

    @overload
    @staticmethod
    def NbSamplesV(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int: ...

    @overload
    @staticmethod
    def NbSamplesV(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, v1: float, v2: float) -> int: ...

class HLRBRep_CurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_CurveTool) -> None: ...

class HLRBRep_Curve:
    """
    Defines a 2d curve by projection of  a 3D curve on
    a    plane     with  an     optional   perspective
    transformation.
    """

    @overload
    def __init__(self) -> None:
        """Creates an undefined Curve."""

    @overload
    def __init__(self, theOther: HLRBRep_Curve) -> None: ...

    def Projector(self, Proj: nanoocp.HLRAlgo.HLRAlgo_Projector) -> None: ...

    @overload
    def Curve(self) -> nanoocp.BRepAdaptor.BRepAdaptor_Curve:
        """Returns the 3D curve."""

    @overload
    def Curve(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Sets the 3D curve to be projected."""

    def GetCurve(self) -> nanoocp.BRepAdaptor.BRepAdaptor_Curve:
        """Returns the 3D curve."""

    def Parameter2d(self, P3d: float) -> float:
        """
        Returns the parameter on the 2d curve from the
        parameter on the 3d curve.
        """

    def Parameter3d(self, P2d: float) -> float:
        """
        Returns the parameter on the 3d curve from the
        parameter on the 2d curve.
        """

    def Update(self) -> tuple[float, list[float], list[float]]:
        """Update the minmax and the internal data"""

    def UpdateMinMax(self) -> tuple[float, list[float], list[float]]:
        """Update the minmax returns tol for enlarge;"""

    def Z(self, U: float) -> float:
        """
        Computes the Z coordinate of the point of
        parameter U on the curve in the viewing coordinate system
        """

    def Value3D(self, U: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the 3D point of parameter U on the
        curve.
        """

    @overload
    def D0(self, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """
        Computes the 3D point of parameter U on the
        curve.
        """

    @overload
    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    @overload
    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U on the curve
        with its first derivative.
        """

    @overload
    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve
        with its first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    def Tangent(self, AtStart: bool, P: nanoocp.gp.gp_Pnt2d, D: nanoocp.gp.gp_Dir2d) -> None:
        """
        Depending on <AtStart> computes the 2D point and
        tangent on the curve at sart (or at end). If the first
        derivative is null look after at start (or before at end)
        with the second derivative.
        """

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Raised if the continuity of the current interval
        is not C2.
        """

    def D3(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    def Resolution(self, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def IsRational(self) -> bool: ...

    def Degree(self) -> int: ...

    def NbPoles(self) -> int: ...

    @overload
    def Poles(self, TP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None: ...

    @overload
    def Poles(self, aCurve: nanoocp.Geom.Geom_BSplineCurve | None, TP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None: ...

    @overload
    def PolesAndWeights(self, TP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TW: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def PolesAndWeights(self, aCurve: nanoocp.Geom.Geom_BSplineCurve | None, TP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TW: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def NbKnots(self) -> int: ...

    def Knots(self, kn: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Multiplicities(self, mu: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

class HLRBRep_TheIntConicCurveOfCInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: HLRBRep_TheIntConicCurveOfCInter) -> None: ...

class HLRBRep_TheIntersectorOfTheIntConicCurveOfCInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: HLRBRep_TheIntersectorOfTheIntConicCurveOfCInter) -> None: ...

class HLRBRep_TheIntPCurvePCurveOfCInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_TheIntPCurvePCurveOfCInter) -> None: ...

    def SetMinNbSamples(self, theMinNbSamples: int) -> None:
        """Set / get minimum number of points in polygon for intersection."""

    def GetMinNbSamples(self) -> int: ...

class HLRBRep_CInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: HLRBRep_CInter) -> None: ...

    def SetMinNbSamples(self, theMinNbSamples: int) -> None:
        """Set / get minimum number of points in polygon intersection."""

    def GetMinNbSamples(self) -> int: ...

class HLRBRep_CLPropsATool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_CLPropsATool) -> None: ...

    @staticmethod
    def Value(A: HLRBRep_Curve, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Computes the point <P> of parameter <U> on the
        Curve from HLRBRep <C>.
        """

    @staticmethod
    def D1(A: HLRBRep_Curve, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point <P> and first derivative <V1>
        of parameter <U> on the curve <C>.
        """

    @staticmethod
    def D2(A: HLRBRep_Curve, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point <P>, the first derivative <V1>
        and second derivative <V2> of parameter <U> on the
        curve <C>.
        """

    @staticmethod
    def D3(A: HLRBRep_Curve, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point <P>, the first derivative <V1>,
        the second derivative <V2> and third derivative
        <V3> of parameter <U> on the curve <C>.
        """

    @staticmethod
    def Continuity(A: HLRBRep_Curve) -> int:
        """
        returns the order of continuity of the curve <C>.
        returns 1: first derivative only is computable.
        returns 2: first and second derivative only are computable.
        returns 3: first, second and third are computable.
        """

    @staticmethod
    def FirstParameter(A: HLRBRep_Curve) -> float:
        """returns the first parameter bound of the curve."""

    @staticmethod
    def LastParameter(A: HLRBRep_Curve) -> float:
        """
        returns the last parameter bound of the curve.
        FirstParameter must be less than LastParamenter.
        """

class HLRBRep_EdgeData:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_EdgeData) -> None: ...

    def Set(self, Reg1: bool, RegN: bool, EG: nanoocp.TopoDS.TopoDS_Edge, V1: int, V2: int, Out1: bool, Out2: bool, Cut1: bool, Cut2: bool, Start: float, TolStart: float, End: float, TolEnd: float) -> None: ...

    @overload
    def Selected(self) -> bool: ...

    @overload
    def Selected(self, B: bool) -> None: ...

    @overload
    def Rg1Line(self) -> bool: ...

    @overload
    def Rg1Line(self, B: bool) -> None: ...

    @overload
    def RgNLine(self) -> bool: ...

    @overload
    def RgNLine(self, B: bool) -> None: ...

    @overload
    def Vertical(self) -> bool: ...

    @overload
    def Vertical(self, B: bool) -> None: ...

    @overload
    def Simple(self) -> bool: ...

    @overload
    def Simple(self, B: bool) -> None: ...

    @overload
    def OutLVSta(self) -> bool: ...

    @overload
    def OutLVSta(self, B: bool) -> None: ...

    @overload
    def OutLVEnd(self) -> bool: ...

    @overload
    def OutLVEnd(self, B: bool) -> None: ...

    @overload
    def CutAtSta(self) -> bool: ...

    @overload
    def CutAtSta(self, B: bool) -> None: ...

    @overload
    def CutAtEnd(self) -> bool: ...

    @overload
    def CutAtEnd(self, B: bool) -> None: ...

    @overload
    def VerAtSta(self) -> bool: ...

    @overload
    def VerAtSta(self, B: bool) -> None: ...

    @overload
    def VerAtEnd(self) -> bool: ...

    @overload
    def VerAtEnd(self, B: bool) -> None: ...

    @overload
    def AutoIntersectionDone(self) -> bool: ...

    @overload
    def AutoIntersectionDone(self, B: bool) -> None: ...

    @overload
    def Used(self) -> bool: ...

    @overload
    def Used(self, B: bool) -> None: ...

    @overload
    def HideCount(self) -> int: ...

    @overload
    def HideCount(self, I: int) -> None: ...

    @overload
    def VSta(self) -> int: ...

    @overload
    def VSta(self, I: int) -> None: ...

    @overload
    def VEnd(self) -> int: ...

    @overload
    def VEnd(self, I: int) -> None: ...

    def UpdateMinMax(self, theTotMinMax: nanoocp.HLRAlgo.HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    def MinMax(self) -> nanoocp.HLRAlgo.HLRAlgo_EdgesBlock.MinMaxIndices: ...

    def Status(self) -> nanoocp.HLRAlgo.HLRAlgo_EdgeStatus: ...

    def ChangeGeometry(self) -> HLRBRep_Curve: ...

    def Geometry(self) -> HLRBRep_Curve: ...

    def Curve(self) -> HLRBRep_Curve: ...

    def Tolerance(self) -> float: ...

class HLRBRep_Surface:
    @overload
    def __init__(self) -> None:
        """Creates an undefined surface with no face loaded."""

    @overload
    def __init__(self, theOther: HLRBRep_Surface) -> None: ...

    def Projector(self, Proj: nanoocp.HLRAlgo.HLRAlgo_Projector) -> None: ...

    @overload
    def Surface(self) -> nanoocp.BRepAdaptor.BRepAdaptor_Surface:
        """Returns the 3D Surface."""

    @overload
    def Surface(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Sets the 3D Surface to be projected."""

    def IsSide(self, tolf: float, toler: float) -> bool:
        """returns true if it is a side face"""

    def IsAbove(self, back: bool, A: HLRBRep_Curve, tolC: float) -> bool: ...

    def FirstUParameter(self) -> float: ...

    def LastUParameter(self) -> float: ...

    def FirstVParameter(self) -> float: ...

    def LastVParameter(self) -> float: ...

    def UContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbUIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the surface in U intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def NbVIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the surface in V intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsUPeriodic(self) -> bool: ...

    def UPeriod(self) -> float: ...

    def IsVPeriodic(self) -> bool: ...

    def VPeriod(self) -> float: ...

    def Value(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameters U,V on the surface."""

    def D0(self, U: float, V: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameters U,V on the surface."""

    def D1(self, U: float, V: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point and the first derivatives on
        the surface.
        Raised if the continuity of the current
        intervals is not C1.
        """

    def D2(self, U: float, V: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec, D2U: nanoocp.gp.gp_Vec, D2V: nanoocp.gp.gp_Vec, D2UV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point, the first and second
        derivatives on the surface.
        Raised if the continuity of the current
        intervals is not C2.
        """

    def D3(self, U: float, V: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec, D2U: nanoocp.gp.gp_Vec, D2V: nanoocp.gp.gp_Vec, D2UV: nanoocp.gp.gp_Vec, D3U: nanoocp.gp.gp_Vec, D3V: nanoocp.gp.gp_Vec, D3UUV: nanoocp.gp.gp_Vec, D3UVV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point, the first, second and third
        derivatives on the surface.
        Raised if the continuity of the current
        intervals is not C3.
        """

    def DN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the
        direction U and Nv in the direction V at the point P(U,
        V).
        Raised if the current U interval is not not CNu
        and the current V interval is not CNv.
        Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """
        Returns the type of the surface : Plane, Cylinder,
        Cone, Sphere, Torus, BezierSurface,
        BSplineSurface, SurfaceOfRevolution,
        SurfaceOfExtrusion, OtherSurface
        """

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone: ...

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def UDegree(self) -> int: ...

    def NbUPoles(self) -> int: ...

    def VDegree(self) -> int: ...

    def NbVPoles(self) -> int: ...

    def NbUKnots(self) -> int: ...

    def NbVKnots(self) -> int: ...

    def Axis(self) -> nanoocp.gp.gp_Ax1: ...

class HLRBRep_FaceData:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_FaceData) -> None: ...

    def Set(self, FG: nanoocp.TopoDS.TopoDS_Face, Or: nanoocp.TopAbs.TopAbs_Orientation, Cl: bool, NW: int) -> None:
        """
        <Or> is the orientation of the face. <Cl> is true
        if the face belongs to a closed volume. <NW> is
        the number of wires (or block of edges) of the
        face.
        """

    def SetWire(self, WI: int, NE: int) -> None:
        """
        Set <NE> the number of edges of the wire number
        <WI>.
        """

    def SetWEdge(self, WI: int, EWI: int, EI: int, Or: nanoocp.TopAbs.TopAbs_Orientation, OutL: bool, Inte: bool, Dble: bool, IsoL: bool) -> None:
        """Set the edge number <EWI> of the wire <WI>."""

    @overload
    def Selected(self) -> bool: ...

    @overload
    def Selected(self, B: bool) -> None: ...

    @overload
    def Back(self) -> bool: ...

    @overload
    def Back(self, B: bool) -> None: ...

    @overload
    def Side(self) -> bool: ...

    @overload
    def Side(self, B: bool) -> None: ...

    @overload
    def Closed(self) -> bool: ...

    @overload
    def Closed(self, B: bool) -> None: ...

    @overload
    def Hiding(self) -> bool: ...

    @overload
    def Hiding(self, B: bool) -> None: ...

    @overload
    def Simple(self) -> bool: ...

    @overload
    def Simple(self, B: bool) -> None: ...

    @overload
    def Cut(self) -> bool: ...

    @overload
    def Cut(self, B: bool) -> None: ...

    @overload
    def WithOutL(self) -> bool: ...

    @overload
    def WithOutL(self, B: bool) -> None: ...

    @overload
    def Plane(self) -> bool: ...

    @overload
    def Plane(self, B: bool) -> None: ...

    @overload
    def Cylinder(self) -> bool: ...

    @overload
    def Cylinder(self, B: bool) -> None: ...

    @overload
    def Cone(self) -> bool: ...

    @overload
    def Cone(self, B: bool) -> None: ...

    @overload
    def Sphere(self) -> bool: ...

    @overload
    def Sphere(self, B: bool) -> None: ...

    @overload
    def Torus(self) -> bool: ...

    @overload
    def Torus(self, B: bool) -> None: ...

    @overload
    def Size(self) -> float: ...

    @overload
    def Size(self, S: float) -> None: ...

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def Orientation(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def Wires(self) -> nanoocp.HLRAlgo.HLRAlgo_WiresBlock: ...

    def Geometry(self) -> HLRBRep_Surface: ...

    def Tolerance(self) -> float: ...

class HLRBRep_SLPropsATool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_SLPropsATool) -> None: ...

class HLRBRep_FaceIterator:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_FaceIterator) -> None: ...

    def InitEdge(self, fd: HLRBRep_FaceData) -> None:
        """Begin an exploration of the edges of the face <fd>"""

    def MoreEdge(self) -> bool: ...

    def NextEdge(self) -> None: ...

    def BeginningOfWire(self) -> bool:
        """
        Returns True if the current edge is the first of a
        wire.
        """

    def EndOfWire(self) -> bool:
        """
        Returns True if the current edge is the last of a
        wire.
        """

    def SkipWire(self) -> None:
        """Skip the current wire in the exploration."""

    def Wire(self) -> nanoocp.HLRAlgo.HLRAlgo_EdgesBlock:
        """Returns the edges of the current wire."""

    def Edge(self) -> int: ...

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def OutLine(self) -> bool: ...

    def Internal(self) -> bool: ...

    def Double(self) -> bool: ...

    def IsoLine(self) -> bool: ...

class HLRBRep_InterCSurf(nanoocp.IntCurveSurface.IntCurveSurface_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, theOther: HLRBRep_InterCSurf) -> None: ...

    @overload
    def Perform(self, theCurve: nanoocp.gp.gp_Lin, theSurface: HLRBRep_Surface) -> None:
        """
        Compute the Intersection between the curve and the
        surface
        """

    @overload
    def Perform(self, theCurve: nanoocp.gp.gp_Lin, thePolygon: HLRBRep_ThePolygonOfInterCSurf, theSurface: HLRBRep_Surface) -> None:
        """
        Compute the Intersection between the curve and
        the surface. The Curve is already sampled and
        its polygon : <thePolygon> is given.
        """

    @overload
    def Perform(self, theCurve: nanoocp.gp.gp_Lin, thePolygon: HLRBRep_ThePolygonOfInterCSurf, theSurface: HLRBRep_Surface, thePolyhedron: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def Perform(self, theCurve: nanoocp.gp.gp_Lin, thePolygon: HLRBRep_ThePolygonOfInterCSurf, theSurface: HLRBRep_Surface, thePolyhedron: HLRBRep_ThePolyhedronOfInterCSurf, theBndBSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Compute the Intersection between the curve and
        the surface. The Curve is already sampled and
        its polygon : <thePolygon> is given. The Surface is
        also sampled and <thePolyhedron> is given.
        """

    @overload
    def Perform(self, theCurve: nanoocp.gp.gp_Lin, theSurface: HLRBRep_Surface, thePolyhedron: HLRBRep_ThePolyhedronOfInterCSurf) -> None:
        """
        Compute the Intersection between the curve and
        the surface. The Surface is already sampled and
        its polyhedron : <thePolyhedron> is given.
        """

class HLRBRep_Intersector:
    """
    The Intersector computes 2D intersections of the projections of 3D curves.
    It can also computes the intersection of a 3D line and a surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_Intersector) -> None: ...

    @overload
    def Perform(self, theEdge1: HLRBRep_EdgeData, theDa1: float, theDb1: float) -> None:
        """
        Performs the auto intersection of an edge.
        The edge domain is cut at start with da1*(b-a) and at end with db1*(b-a).
        """

    @overload
    def Perform(self, theNA: int, theEdge1: HLRBRep_EdgeData, theDa1: float, theDb1: float, theNB: int, theEdge2: HLRBRep_EdgeData, theDa2: float, theDb2: float, theNoBound: bool) -> None:
        """
        Performs the intersection between the two edges.
        The edges domains are cut at start with da*(b-a) and at end with db*(b-a).
        """

    @overload
    def Perform(self, theL: nanoocp.gp.gp_Lin, theP: float) -> None: ...

    def SimulateOnePoint(self, theEdge1: HLRBRep_EdgeData, theU: float, theEdge2: HLRBRep_EdgeData, theV: float) -> None:
        """
        Create a single IntersectionPoint (U on theEdge1) (V on theEdge2)
        The point is middle on both curves.
        """

    def Load(self, theSurface: HLRBRep_Surface) -> None: ...

    def IsDone(self) -> bool: ...

    def NbPoints(self) -> int: ...

    def Point(self, N: int) -> nanoocp.IntRes2d.IntRes2d_IntersectionPoint: ...

    def CSPoint(self, N: int) -> nanoocp.IntCurveSurface.IntCurveSurface_IntersectionPoint: ...

    def NbSegments(self) -> int: ...

    def Segment(self, N: int) -> nanoocp.IntRes2d.IntRes2d_IntersectionSegment: ...

    def CSSegment(self, N: int) -> nanoocp.IntCurveSurface.IntCurveSurface_IntersectionSegment: ...

    def Destroy(self) -> None: ...

class HLRBRep_Data(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, NV: int, NE: int, NF: int) -> None:
        """
        Create an empty data structure of <NV> vertices,
        <NE> edges and <NF> faces.
        """

    @overload
    def __init__(self, theOther: HLRBRep_Data) -> None: ...

    def Write(self, DS: HLRBRep_Data | None, dv: int, de: int, df: int) -> None:
        """
        Write <DS> in me with a translation of
        <dv>,<de>,<df>.
        """

    def EDataArray(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRBRep.HLRBRep_EdgeData]: ...

    def FDataArray(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRBRep.HLRBRep_FaceData]: ...

    @overload
    def Tolerance(self, tol: float) -> None:
        """
        Set the tolerance for the rejections during the
        exploration
        """

    @overload
    def Tolerance(self) -> float:
        """
        returns the tolerance for the rejections during
        the exploration
        """

    def Update(self, P: nanoocp.HLRAlgo.HLRAlgo_Projector) -> None:
        """
        end of building of the Data and updating
        all the information linked to the projection.
        """

    def Projector(self) -> nanoocp.HLRAlgo.HLRAlgo_Projector: ...

    def NbVertices(self) -> int: ...

    def NbEdges(self) -> int: ...

    def NbFaces(self) -> int: ...

    def EdgeMap(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def FaceMap(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def InitBoundSort(self, MinMaxTot: nanoocp.HLRAlgo.HLRAlgo_EdgesBlock.MinMaxIndices, e1: int, e2: int) -> None:
        """to compare with only non rejected edges."""

    def InitEdge(self, FI: int, MST: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepTopAdaptor.BRepTopAdaptor_Tool, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Begin an iteration only on visible Edges
        crossing the face number <FI>.
        """

    def MoreEdge(self) -> bool: ...

    def NextEdge(self, skip: bool = True) -> None: ...

    def Edge(self) -> int:
        """Returns the current Edge"""

    def HidingTheFace(self) -> bool:
        """
        Returns true if the current edge to be hidden
        belongs to the hiding face.
        """

    def SimpleHidingFace(self) -> bool:
        """
        Returns true if the current hiding face is not an
        auto-intersected one.
        """

    def InitInterference(self) -> None:
        """
        Intersect the current Edge with the boundary of
        the hiding face. The interferences are given by
        the More, Next, and Value methods.
        """

    def MoreInterference(self) -> bool: ...

    def NextInterference(self) -> None: ...

    def RejectedInterference(self) -> bool:
        """Returns True if the interference is rejected."""

    def AboveInterference(self) -> bool:
        """
        Returns True if the rejected interference is above
        the face.
        """

    def Interference(self) -> nanoocp.HLRAlgo.HLRAlgo_Interference: ...

    def LocalLEGeometry2D(self, Param: float, Tg: nanoocp.gp.gp_Dir2d, Nm: nanoocp.gp.gp_Dir2d) -> float:
        """
        Returns the local description of the projection of
        the current LEdge at parameter <Param>.
        """

    def LocalFEGeometry2D(self, FE: int, Param: float, Tg: nanoocp.gp.gp_Dir2d, Nm: nanoocp.gp.gp_Dir2d) -> float:
        """
        Returns the local description of the projection of
        the current FEdge at parameter <Param>.
        """

    def EdgeState(self, p1: float, p2: float) -> tuple[nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]:
        """
        Returns the local 3D state of the intersection
        between the current edge and the current face at the
        <p1> and <p2> parameters.
        """

    def EdgeOfTheHidingFace(self, E: int, ED: HLRBRep_EdgeData) -> bool:
        """
        Returns the true if the Edge <ED> belongs to the
        Hiding Face.
        """

    def HidingStartLevel(self, E: int, ED: HLRBRep_EdgeData, IL: nanoocp.NCollection.NCollection_List[nanoocp.HLRAlgo.HLRAlgo_Interference]) -> int:
        """
        Returns the number of levels of hiding face above
        the first point of the edge <ED>. The
        InterferenceList is given to compute far away of
        the Interferences and then come back.
        """

    def Compare(self, E: int, ED: HLRBRep_EdgeData) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the state of the Edge <ED> after
        classification.
        """

    def SimplClassify(self, E: int, ED: HLRBRep_EdgeData, Nbp: int, p1: float, p2: float) -> nanoocp.TopAbs.TopAbs_State:
        """
        Simple classification of part of edge [p1, p2].
        Returns OUT if at least 1 of Nbp points of edge is out; otherwise returns IN.
        It is used to check "suspicion" hidden part of edge.
        """

    def Classify(self, E: int, ED: HLRBRep_EdgeData, LevelFlag: bool, param: float) -> tuple[nanoocp.TopAbs.TopAbs_State, int]:
        """Classification of an edge."""

    def IsBadFace(self) -> bool:
        """Returns true if the current face is bad."""

    def Destroy(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRBRep_EdgeBuilder:
    @overload
    def __init__(self, VList: HLRBRep_VertexList) -> None:
        """
        Creates an EdgeBuilder algorithm. <VList>
        describes the edge and the interferences.
        AreaLimits are created from the vertices.
        Builds(IN) is automatically called.
        """

    @overload
    def __init__(self, theOther: HLRBRep_EdgeBuilder) -> None: ...

    def InitAreas(self) -> None:
        """Initialize an iteration on the areas."""

    def NextArea(self) -> None:
        """Set the current area to the next area."""

    def PreviousArea(self) -> None:
        """Set the current area to the previous area."""

    def HasArea(self) -> bool:
        """Returns True if there is a current area."""

    def AreaState(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the state of the current area."""

    def AreaEdgeState(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the edge state of the current area."""

    def LeftLimit(self) -> HLRBRep_AreaLimit:
        """
        Returns the AreaLimit beginning the current area.
        This is a NULL handle when the area is infinite on
        the left.
        """

    def RightLimit(self) -> HLRBRep_AreaLimit:
        """
        Returns the AreaLimit ending the current area.
        This is a NULL handle when the area is infinite on
        the right.
        """

    def Builds(self, ToBuild: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Reinitialize the results iteration to the parts
        with State <ToBuild>. If this method is not called
        after construction the default is <ToBuild> = IN.
        """

    def MoreEdges(self) -> bool:
        """Returns True if there are more new edges to build."""

    def NextEdge(self) -> None:
        """
        Proceeds to the next edge to build. Skip all
        remaining vertices on the current edge.
        """

    def MoreVertices(self) -> bool:
        """
        True if there are more vertices in the current new
        edge.
        """

    def NextVertex(self) -> None:
        """Proceeds to the next vertex of the current edge."""

    def Current(self) -> nanoocp.HLRAlgo.HLRAlgo_Intersection:
        """Returns the current vertex of the current edge."""

    def IsBoundary(self) -> bool:
        """
        Returns True if the current vertex comes from the
        boundary of the edge.
        """

    def IsInterference(self) -> bool:
        """
        Returns True if the current vertex was an
        interference.
        """

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the new orientation of the current vertex."""

    def Destroy(self) -> None: ...

class HLRBRep_EdgeFaceTool:
    """
    The EdgeFaceTool computes the UV coordinates at a
    given parameter on a Curve and a Surface. It also
    compute the signed curvature value in a direction
    at a given u,v point on a surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_EdgeFaceTool) -> None: ...

class HLRBRep_EdgeIList:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_EdgeIList) -> None: ...

    @staticmethod
    def AddInterference(IL: nanoocp.NCollection.NCollection_List[nanoocp.HLRAlgo.HLRAlgo_Interference], I: nanoocp.HLRAlgo.HLRAlgo_Interference, T: HLRBRep_EdgeInterferenceTool) -> None:
        """Add the interference <I> to the list <IL>."""

    @staticmethod
    def ProcessComplex(IL: nanoocp.NCollection.NCollection_List[nanoocp.HLRAlgo.HLRAlgo_Interference], T: HLRBRep_EdgeInterferenceTool) -> None:
        """Process complex transitions on the list IL."""

class HLRBRep_EdgeInterferenceTool:
    """
    Implements the methods required to instantiates
    the EdgeInterferenceList from HLRAlgo.
    """

    @overload
    def __init__(self, DS: HLRBRep_Data | None) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_EdgeInterferenceTool) -> None: ...

    def LoadEdge(self) -> None: ...

    def InitVertices(self) -> None: ...

    def MoreVertices(self) -> bool: ...

    def NextVertex(self) -> None: ...

    def CurrentVertex(self) -> nanoocp.HLRAlgo.HLRAlgo_Intersection: ...

    def CurrentOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def CurrentParameter(self) -> float: ...

    def IsPeriodic(self) -> bool: ...

    def EdgeGeometry(self, Param: float, Tgt: nanoocp.gp.gp_Dir, Nrm: nanoocp.gp.gp_Dir) -> float:
        """
        Returns local geometric description of the Edge at
        parameter <Para>. See method Reset of class
        EdgeFaceTransition from TopCnx for other arguments.
        """

    def ParameterOfInterference(self, I: nanoocp.HLRAlgo.HLRAlgo_Interference) -> float: ...

    def SameInterferences(self, I1: nanoocp.HLRAlgo.HLRAlgo_Interference, I2: nanoocp.HLRAlgo.HLRAlgo_Interference) -> bool:
        """
        True if the two interferences are on the same
        geometric locus.
        """

    def SameVertexAndInterference(self, I: nanoocp.HLRAlgo.HLRAlgo_Interference) -> bool:
        """
        True if the Interference and the current Vertex
        are on the same geometric locus.
        """

    def InterferenceBoundaryGeometry(self, I: nanoocp.HLRAlgo.HLRAlgo_Interference, Tang: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir) -> float:
        """
        Returns the geometry of the boundary at the
        interference <I>. See the AddInterference method
        of the class EdgeFaceTransition from TopCnx for
        the other arguments.
        """

class HLRBRep_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfCInter(nanoocp.math.math_FunctionSetWithDerivatives):
    def __init__(self, theOther: HLRBRep_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfCInter) -> None: ...

    def NbVariables(self) -> int:
        """returns 2."""

    def NbEquations(self) -> int:
        """returns 2."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

class HLRBRep_ExactIntersectionPointOfTheIntPCurvePCurveOfCInter:
    def __init__(self, theOther: HLRBRep_ExactIntersectionPointOfTheIntPCurvePCurveOfCInter) -> None: ...

    @overload
    def Perform(self, Poly1: HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter, Poly2: HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter) -> tuple[int, int, float, float]: ...

    @overload
    def Perform(self, Uo: float, Vo: float, UInf: float, VInf: float, USup: float, VSup: float) -> None: ...

    def NbRoots(self) -> int: ...

    def Roots(self) -> tuple[float, float]: ...

    def AnErrorOccurred(self) -> bool: ...

class HLRBRep_Hider:
    @overload
    def __init__(self, DS: HLRBRep_Data | None) -> None:
        """
        Creates a Hider processing the set of Edges and
        hiding faces described by <DS>. Stores the hidden
        parts in <DS>.
        """

    @overload
    def __init__(self, theOther: HLRBRep_Hider) -> None: ...

    def OwnHiding(self, FI: int) -> None:
        """own hiding the side face number <FI>."""

    def Hide(self, FI: int, MST: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepTopAdaptor.BRepTopAdaptor_Tool, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Removes from the edges, the parts hidden by the
        hiding face number <FI>.
        """

class HLRBRep_HLRToShape:
    """
    A framework for filtering the computation
    results of an HLRBRep_Algo algorithm by extraction.
    From the results calculated by the algorithm on
    a shape, a filter returns the type of edge you
    want to identify. You can choose any of the following types of output:
    -   visible sharp edges
    -   hidden sharp edges
    -   visible smooth edges
    -   hidden smooth edges
    -   visible sewn edges
    -   hidden sewn edges
    -   visible outline edges
    -   hidden outline edges.
    -   visible isoparameters and
    -   hidden isoparameters.
    Sharp edges present a C0 continuity (non G1).
    Smooth edges present a G1 continuity (non G2).
    Sewn edges present a C2 continuity.
    The result is composed of 2D edges in the
    projection plane of the view which the
    algorithm has worked with. These 2D edges
    are not included in the data structure of the visualized shape.
    In order to obtain a complete image, you must
    combine the shapes given by each of the chosen filters.
    The construction of the shape does not call a
    new computation of the algorithm, but only
    reads its internal results.
    The methods of this shape are almost identic to those of the HLRBrep_PolyHLRToShape class.
    """

    @overload
    def __init__(self, A: HLRBRep_Algo | None) -> None:
        """
        Constructs a framework for filtering the
        results of the HLRBRep_Algo algorithm, A.
        Use the extraction filters to obtain the results you want for A.
        """

    @overload
    def __init__(self, theOther: HLRBRep_HLRToShape) -> None: ...

    @overload
    def VCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible sharp edges (of C0-continuity)."""

    @overload
    def VCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible sharp edges (of C0-continuity) of specified shape."""

    @overload
    def Rg1LineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible smooth edges (G1-continuity between two surfaces)."""

    @overload
    def Rg1LineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Return visible smooth edges (G1-continuity between two surfaces) of specified shape.
        """

    @overload
    def RgNLineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible sewn edges (of CN-continuity on one surface)."""

    @overload
    def RgNLineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Return visible sewn edges (of CN-continuity on one surface) of specified shape.
        """

    @overload
    def OutLineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible outline edges ("silhouette")."""

    @overload
    def OutLineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible outline edges ("silhouette") of specified shape."""

    def OutLineVCompound3d(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible outline edges ("silhouette")."""

    @overload
    def IsoLineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible isoparameters."""

    @overload
    def IsoLineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return visible isoparameters of specified shape."""

    @overload
    def HCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden sharp edges (of C0-continuity)."""

    @overload
    def HCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden sharp edges (of C0-continuity) of specified shape."""

    @overload
    def Rg1LineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden smooth edges (G1-continuity between two surfaces)."""

    @overload
    def Rg1LineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Return hidden smooth edges (G1-continuity between two surfaces) of specified shape.
        """

    @overload
    def RgNLineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden sewn edges (of CN-continuity on one surface)."""

    @overload
    def RgNLineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Return hidden sewn edges (of CN-continuity on one surface) of specified shape.
        """

    @overload
    def OutLineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden outline edges ("silhouette")."""

    @overload
    def OutLineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden outline edges ("silhouette") of specified shape."""

    @overload
    def IsoLineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden isoparameters."""

    @overload
    def IsoLineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return hidden isoparameters of specified shape."""

    @overload
    def CompoundOfEdges(self, type: HLRBRep_TypeOfResultingEdge, visible: bool, In3d: bool) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns compound of resulting edges
        of required type and visibility,
        taking into account the kind of space
        (2d or 3d)
        """

    @overload
    def CompoundOfEdges(self, S: nanoocp.TopoDS.TopoDS_Shape, type: HLRBRep_TypeOfResultingEdge, visible: bool, In3d: bool) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        For specified shape
        returns compound of resulting edges
        of required type and visibility,
        taking into account the kind of space
        (2d or 3d)
        """

class HLRBRep_IntConicCurveOfCInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: HLRBRep_IntConicCurveOfCInter) -> None: ...

class HLRBRep_LineTool:
    """
    The LineTool class provides class methods to
    access the methodes of the Line.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_LineTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.gp.gp_Lin) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.gp.gp_Lin) -> float: ...

    @staticmethod
    def Continuity(C: nanoocp.gp.gp_Lin) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(C: nanoocp.gp.gp_Lin, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the line in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    @staticmethod
    def Intervals(C: nanoocp.gp.gp_Lin, T: nanoocp.NCollection.NCollection_Array1[float], Sh: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets the current working interval."""

    @staticmethod
    def IntervalFirst(C: nanoocp.gp.gp_Lin) -> float:
        """
        Returns the first parameter of the current
        interval.
        """

    @staticmethod
    def IntervalLast(C: nanoocp.gp.gp_Lin) -> float:
        """
        Returns the last parameter of the current
        interval.
        """

    @staticmethod
    def IntervalContinuity(C: nanoocp.gp.gp_Lin) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def IsClosed(C: nanoocp.gp.gp_Lin) -> bool: ...

    @staticmethod
    def IsPeriodic(C: nanoocp.gp.gp_Lin) -> bool: ...

    @staticmethod
    def Period(C: nanoocp.gp.gp_Lin) -> float: ...

    @staticmethod
    def Value(C: nanoocp.gp.gp_Lin, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter U on the line."""

    @staticmethod
    def D0(C: nanoocp.gp.gp_Lin, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameter U on the line."""

    @staticmethod
    def D1(C: nanoocp.gp.gp_Lin, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U on the line with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    @staticmethod
    def D2(C: nanoocp.gp.gp_Lin, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    @staticmethod
    def D3(C: nanoocp.gp.gp_Lin, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    @staticmethod
    def DN(C: nanoocp.gp.gp_Lin, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    @staticmethod
    def Resolution(C: nanoocp.gp.gp_Lin, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(C: nanoocp.gp.gp_Lin) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the line in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(C: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Lin: ...

    @staticmethod
    def Circle(C: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Circ: ...

    @staticmethod
    def Ellipse(C: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Elips: ...

    @staticmethod
    def Hyperbola(C: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Hypr: ...

    @staticmethod
    def Parabola(C: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Parab: ...

    @staticmethod
    def Bezier(C: nanoocp.gp.gp_Lin) -> nanoocp.Geom.Geom_BezierCurve: ...

    @staticmethod
    def BSpline(C: nanoocp.gp.gp_Lin) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @staticmethod
    def Degree(C: nanoocp.gp.gp_Lin) -> int: ...

    @staticmethod
    def NbPoles(C: nanoocp.gp.gp_Lin) -> int: ...

    @staticmethod
    def Poles(C: nanoocp.gp.gp_Lin, TP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @staticmethod
    def IsRational(C: nanoocp.gp.gp_Lin) -> bool: ...

    @staticmethod
    def PolesAndWeights(C: nanoocp.gp.gp_Lin, TP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], TW: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def NbKnots(C: nanoocp.gp.gp_Lin) -> int: ...

    @staticmethod
    def KnotsAndMultiplicities(C: nanoocp.gp.gp_Lin, TK: nanoocp.NCollection.NCollection_Array1[float], TM: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @staticmethod
    def NbSamples(C: nanoocp.gp.gp_Lin, U0: float, U1: float) -> int: ...

    @staticmethod
    def SamplePars(C: nanoocp.gp.gp_Lin, U0: float, U1: float, Defl: float, NbMin: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns sample parameters for the line within [U0, U1] range.
        @param[in] C the line
        @param[in] U0 start parameter
        @param[in] U1 end parameter
        @param[in] Defl deflection tolerance (unused for lines)
        @param[in] NbMin minimum number of sample points (unused for lines)
        @return array of 3 sample parameter values
        """

    @staticmethod
    def SamplePars__NCollection_HArray1__double(C: nanoocp.gp.gp_Lin, U0: float, U1: float, Defl: float, NbMin: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        SamplePars__NCollection_HArray1__double: the C++ overload SamplePars(const gp_Lin &, const double, const double, const double, const int, occ::handle<NCollection_HArray1<double>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use SamplePars() returning handle by value instead

        @deprecated Use SamplePars() returning handle by value instead.
        """

class HLRBRep_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfCInter(nanoocp.math.math_FunctionWithDerivative):
    def __init__(self, theOther: HLRBRep_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfCInter) -> None: ...

    def Value(self, Param: float) -> tuple[bool, float]:
        """
        Computes the value of the signed distance between
        the implicit curve and the point at parameter Param
        on the parametrised curve.
        """

    def Derivative(self, Param: float) -> tuple[bool, float]:
        """
        Computes the derivative of the previous function at
        parameter Param.
        """

    def Values(self, Param: float) -> tuple[bool, float, float]:
        """Computes the value and the derivative of the function."""

class HLRBRep_PolyAlgo(nanoocp.Standard.Standard_Transient):
    """
    to remove Hidden lines on Shapes with Triangulations.
    A framework to compute the shape as seen in
    a projection plane. This is done by calculating
    the visible and the hidden parts of the shape.
    HLRBRep_PolyAlgo works with three types of entity:
    -   shapes to be visualized (these shapes must
    have already been triangulated.)
    -   edges in these shapes (these edges are
    defined as polygonal lines on the
    triangulation of the shape, and are the basic
    entities which will be visualized or hidden), and
    -   triangles in these shapes which hide the edges.
    HLRBRep_PolyAlgo is based on the principle
    of comparing each edge of the shape to be
    visualized with each of the triangles produced
    by the triangulation of the shape, and
    calculating the visible and the hidden parts of each edge.
    For a given projection, HLRBRep_PolyAlgo
    calculates a set of lines characteristic of the
    object being represented. It is also used in
    conjunction with the HLRBRep_PolyHLRToShape extraction
    utilities, which reconstruct a new, simplified
    shape from a selection of calculation results.
    This new shape is made up of edges, which
    represent the shape visualized in the projection.
    HLRBRep_PolyAlgo works with a polyhedral
    simplification of the shape whereas
    HLRBRep_Algo takes the shape itself into
    account. When you use HLRBRep_Algo, you
    obtain an exact result, whereas, when you use
    HLRBRep_PolyAlgo, you reduce computation
    time but obtain polygonal segments.
    An HLRBRep_PolyAlgo object provides a framework for:
    -   defining the point of view
    -   identifying the shape or shapes to be visualized
    -   calculating the outlines
    -   calculating the visible and hidden lines of the shape.
    Warning
    -   Superimposed lines are not eliminated by this algorithm.
    -   There must be no unfinished objects inside the shape you wish to visualize.
    -   Points are not treated.
    -   Note that this is not the sort of algorithm
    used in generating shading, which calculates
    the visible and hidden parts of each face in a
    shape to be visualized by comparing each
    face in the shape with every other face in the same shape.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty framework for the
        calculation of the visible and hidden lines of a shape in a projection.
        Use the functions:
        -   Projector to define the point of view
        -   Load to select the shape or shapes to be visualized
        -   Update to compute the visible and hidden lines of the shape.
        Warning
        The shape or shapes to be visualized must have already been triangulated.
        """

    @overload
    def __init__(self, A: HLRBRep_PolyAlgo | None) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_PolyAlgo) -> None: ...

    def NbShapes(self) -> int: ...

    def Shape(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Remove(self, I: int) -> None:
        """remove the Shape of Index <I>."""

    def Index(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        return the index of the Shape <S> and return 0 if
        the Shape <S> is not found.
        """

    def Load(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Loads the shape S into this framework.
        Warning S must have already been triangulated.
        """

    def Algo(self) -> nanoocp.HLRAlgo.HLRAlgo_PolyAlgo: ...

    @overload
    def Projector(self) -> nanoocp.HLRAlgo.HLRAlgo_Projector:
        """
        Sets the parameters of the view for this framework.
        These parameters are defined by an HLRAlgo_Projector object,
        which is returned by the Projector function on a Prs3d_Projector object.
        """

    @overload
    def Projector(self, theProj: nanoocp.HLRAlgo.HLRAlgo_Projector) -> None: ...

    @overload
    def TolAngular(self) -> float: ...

    @overload
    def TolAngular(self, theTol: float) -> None: ...

    @overload
    def TolCoef(self) -> float: ...

    @overload
    def TolCoef(self, theTol: float) -> None: ...

    def Update(self) -> None:
        """
        Launches calculation of outlines of the shape
        visualized by this framework. Used after setting the point of view and
        defining the shape or shapes to be visualized.
        """

    def InitHide(self) -> None: ...

    def MoreHide(self) -> bool: ...

    def NextHide(self) -> None: ...

    def Hide(self, status: nanoocp.HLRAlgo.HLRAlgo_EdgeStatus, S: nanoocp.TopoDS.TopoDS_Shape) -> tuple[nanoocp.HLRAlgo.HLRAlgo_BiPoint.PointsT, bool, bool, bool, bool]: ...

    def InitShow(self) -> None: ...

    def MoreShow(self) -> bool: ...

    def NextShow(self) -> None: ...

    def Show(self, S: nanoocp.TopoDS.TopoDS_Shape) -> tuple[nanoocp.HLRAlgo.HLRAlgo_BiPoint.PointsT, bool, bool, bool, bool]: ...

    def OutLinedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Make a shape with the internal outlines in each
        face.
        """

    @overload
    def Debug(self) -> bool: ...

    @overload
    def Debug(self, theDebug: bool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRBRep_PolyHLRToShape:
    """
    A framework for filtering the computation
    results of an HLRBRep_Algo algorithm by extraction.
    From the results calculated by the algorithm on
    a shape, a filter returns the type of edge you
    want to identify. You can choose any of the following types of output:
    -   visible sharp edges
    -   hidden sharp edges
    -   visible smooth edges
    -   hidden smooth edges
    -   visible sewn edges
    -   hidden sewn edges
    -   visible outline edges
    -   hidden outline edges.
    -   visible isoparameters and
    -   hidden isoparameters.
    Sharp edges present a C0 continuity (non G1).
    Smooth edges present a G1 continuity (non G2).
    Sewn edges present a C2 continuity.
    The result is composed of 2D edges in the
    projection plane of the view which the
    algorithm has worked with. These 2D edges
    are not included in the data structure of the visualized shape.
    In order to obtain a complete image, you must
    combine the shapes given by each of the chosen filters.
    The construction of the shape does not call a
    new computation of the algorithm, but only
    reads its internal results.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a framework for filtering the results
        of the HLRBRep_Algo algorithm, A.
        Use the extraction filters to obtain the results you want for A.
        """

    @overload
    def __init__(self, theOther: HLRBRep_PolyHLRToShape) -> None: ...

    def Update(self, A: HLRBRep_PolyAlgo | None) -> None: ...

    def Show(self) -> None: ...

    def Hide(self) -> None: ...

    @overload
    def VCompound(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def VCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Rg1LineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Sets the extraction filter for visible smooth edges."""

    @overload
    def Rg1LineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def RgNLineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Sets the extraction filter for visible sewn edges."""

    @overload
    def RgNLineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def OutLineVCompound(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def OutLineVCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Sets the extraction filter for visible outlines."""

    @overload
    def HCompound(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def HCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Rg1LineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Rg1LineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Sets the extraction filter for hidden smooth edges."""

    @overload
    def RgNLineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def RgNLineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Sets the extraction filter for hidden sewn edges."""

    @overload
    def OutLineHCompound(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def OutLineHCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Sets the extraction filter for hidden outlines.
        Hidden outlines occur, for instance, in tori. In
        this case, the inner outlines of the torus seen on its side are hidden.
        """

class HLRBRep_ShapeToHLR:
    """
    compute the OutLinedShape of a Shape with an
    OutLiner, a Projector and create the Data
    Structure of a Shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_ShapeToHLR) -> None: ...

    @staticmethod
    def Load(S: nanoocp.HLRTopoBRep.HLRTopoBRep_OutLiner | None, P: nanoocp.HLRAlgo.HLRAlgo_Projector, MST: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepTopAdaptor.BRepTopAdaptor_Tool, nanoocp.TopTools.TopTools_ShapeMapHasher], nbIso: int = 0) -> HLRBRep_Data:
        """
        Creates a DataStructure containing the OutLiner
        <S> depending on the projector <P> and nbIso.
        """

class HLRBRep_SurfaceTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_SurfaceTool) -> None: ...

    @staticmethod
    def FirstUParameter(theSurf: HLRBRep_Surface) -> float: ...

    @staticmethod
    def FirstVParameter(theSurf: HLRBRep_Surface) -> float: ...

    @staticmethod
    def LastUParameter(theSurf: HLRBRep_Surface) -> float: ...

    @staticmethod
    def LastVParameter(theSurf: HLRBRep_Surface) -> float: ...

    @staticmethod
    def NbUIntervals(theSurf: HLRBRep_Surface, theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    @staticmethod
    def NbVIntervals(theSurf: HLRBRep_Surface, theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    @staticmethod
    def UIntervals(theSurf: HLRBRep_Surface, theT: nanoocp.NCollection.NCollection_Array1[float], theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @staticmethod
    def VIntervals(theSurf: HLRBRep_Surface, theT: nanoocp.NCollection.NCollection_Array1[float], theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @staticmethod
    def UTrim(theSurf: HLRBRep_Surface, theFirst: float, theLast: float, theTol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """If <theFirst> >= <theLast>"""

    @staticmethod
    def VTrim(theSurf: HLRBRep_Surface, theFirst: float, theLast: float, theTol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """If <theFirst> >= <theLast>"""

    @staticmethod
    def IsUClosed(theSurf: HLRBRep_Surface) -> bool: ...

    @staticmethod
    def IsVClosed(theSurf: HLRBRep_Surface) -> bool: ...

    @staticmethod
    def IsUPeriodic(theSurf: HLRBRep_Surface) -> bool: ...

    @staticmethod
    def UPeriod(theSurf: HLRBRep_Surface) -> float: ...

    @staticmethod
    def IsVPeriodic(theSurf: HLRBRep_Surface) -> bool: ...

    @staticmethod
    def VPeriod(theSurf: HLRBRep_Surface) -> float: ...

    @staticmethod
    def Value(theSurf: HLRBRep_Surface, theU: float, theV: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def D0(theSurf: HLRBRep_Surface, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def D1(theSurf: HLRBRep_Surface, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D2(theSurf: HLRBRep_Surface, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D3(theSurf: HLRBRep_Surface, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec, theD3U: nanoocp.gp.gp_Vec, theD3V: nanoocp.gp.gp_Vec, theD3UUV: nanoocp.gp.gp_Vec, theD3UVV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def DN(theSurf: HLRBRep_Surface, theU: float, theV: float, theNu: int, theNv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def UResolution(theSurf: HLRBRep_Surface, theR3d: float) -> float: ...

    @staticmethod
    def VResolution(theSurf: HLRBRep_Surface, theR3d: float) -> float: ...

    @staticmethod
    def GetType(theSurf: HLRBRep_Surface) -> nanoocp.GeomAbs.GeomAbs_SurfaceType: ...

    @staticmethod
    def Plane(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Pln: ...

    @staticmethod
    def Cylinder(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Cylinder: ...

    @staticmethod
    def Cone(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Cone: ...

    @staticmethod
    def Torus(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Torus: ...

    @staticmethod
    def Sphere(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Sphere: ...

    @staticmethod
    def Bezier(theSurf: HLRBRep_Surface) -> nanoocp.Geom.Geom_BezierSurface: ...

    @staticmethod
    def BSpline(theSurf: HLRBRep_Surface) -> nanoocp.Geom.Geom_BSplineSurface: ...

    @staticmethod
    def AxeOfRevolution(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Ax1: ...

    @staticmethod
    def Direction(theSurf: HLRBRep_Surface) -> nanoocp.gp.gp_Dir: ...

    @staticmethod
    def BasisCurve(theSurf: HLRBRep_Surface) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    @staticmethod
    def BasisSurface(theSurf: HLRBRep_Surface) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    @staticmethod
    def OffsetValue(theSurf: HLRBRep_Surface) -> float: ...

    @overload
    @staticmethod
    def NbSamplesU(theSurf: HLRBRep_Surface) -> int: ...

    @overload
    @staticmethod
    def NbSamplesU(theSurf: HLRBRep_Surface, theU1: float, theU2: float) -> int: ...

    @overload
    @staticmethod
    def NbSamplesV(theSurf: HLRBRep_Surface) -> int: ...

    @overload
    @staticmethod
    def NbSamplesV(theSurf: HLRBRep_Surface, theV1: float, theV2: float) -> int: ...

class HLRBRep_TheCSFunctionOfInterCSurf(nanoocp.math.math_FunctionSetWithDerivatives):
    def __init__(self, theOther: HLRBRep_TheCSFunctionOfInterCSurf) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def Root(self) -> float: ...

    def AuxillarSurface(self) -> HLRBRep_Surface: ...

    def AuxillarCurve(self) -> nanoocp.gp.gp_Lin: ...

class HLRBRep_TheExactInterCSurf:
    @overload
    def __init__(self, F: HLRBRep_TheCSFunctionOfInterCSurf, TolTangency: float) -> None:
        """initialize the parameters to compute the solution"""

    @overload
    def __init__(self, U: float, V: float, W: float, F: HLRBRep_TheCSFunctionOfInterCSurf, TolTangency: float, MarginCoef: float = 0.0) -> None:
        """
        compute the solution point with the close point
        MarginCoef is the coefficient for extension of UV bounds.
        Ex., UFirst -= MarginCoef*(ULast-UFirst)
        """

    @overload
    def __init__(self, theOther: HLRBRep_TheExactInterCSurf) -> None: ...

    def Perform(self, U: float, V: float, W: float, Rsnld: nanoocp.math.math_FunctionSetRoot, u0: float, v0: float, u1: float, v1: float, w0: float, w1: float) -> None:
        """
        compute the solution
        it's possible to write to optimize:
        IntImp_IntCS inter(S1,C1,Toltangency)
        math_FunctionSetRoot rsnld(Inter.function())
        while ...{
        u=...
        v=...
        w=...
        inter.Perform(u,v,w,rsnld)
        }
        or
        IntImp_IntCS inter(Toltangency)
        inter.SetSurface(S);
        math_FunctionSetRoot rsnld(Inter.function())
        while ...{
        C=...
        inter.SetCurve(C);
        u=...
        v=...
        w=...
        inter.Perform(u,v,w,rsnld)
        }
        """

    def IsDone(self) -> bool:
        """Returns TRUE if the creation completed without failure."""

    def IsEmpty(self) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the intersection point
        The exception NotDone is raised if IsDone is false.
        The exception DomainError is raised if IsEmpty is true.
        """

    def ParameterOnCurve(self) -> float: ...

    def ParameterOnSurface(self) -> tuple[float, float]: ...

    def Function(self) -> HLRBRep_TheCSFunctionOfInterCSurf:
        """
        return the math function which
        is used to compute the intersection
        """

class HLRBRep_TheInterferenceOfInterCSurf(nanoocp.Intf.Intf_Interference):
    @overload
    def __init__(self) -> None:
        """
        Constructs an empty interference between Polygon and
        Polyhedron.
        """

    @overload
    def __init__(self, thePolyg: HLRBRep_ThePolygonOfInterCSurf, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def __init__(self, theLin: nanoocp.gp.gp_Lin, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def __init__(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def __init__(self, thePolyg: HLRBRep_ThePolygonOfInterCSurf, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Constructs and computes an interference between the Polygon
        and the Polyhedron.
        """

    @overload
    def __init__(self, theLin: nanoocp.gp.gp_Lin, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Constructs and computes an interference between the
        Straight Line and the Polyhedron.
        """

    @overload
    def __init__(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Constructs and computes an interference between the
        Straight Lines and the Polyhedron.
        """

    @overload
    def __init__(self, theOther: HLRBRep_TheInterferenceOfInterCSurf) -> None: ...

    @overload
    def Perform(self, thePolyg: HLRBRep_ThePolygonOfInterCSurf, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def Perform(self, theLin: nanoocp.gp.gp_Lin, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def Perform(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    @overload
    def Perform(self, thePolyg: HLRBRep_ThePolygonOfInterCSurf, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Computes an interference between the Polygon and the
        Polyhedron.
        """

    @overload
    def Perform(self, theLin: nanoocp.gp.gp_Lin, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Computes an interference between the Straight Line and the
        Polyhedron.
        """

    @overload
    def Perform(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Computes an interference between the Straight Lines and
        the Polyhedron.
        """

    @overload
    def Interference(self, thePolyg: HLRBRep_ThePolygonOfInterCSurf, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None: ...

    @overload
    def Interference(self, thePolyg: HLRBRep_ThePolygonOfInterCSurf, thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None:
        """
        Compares the boundings between the segment of <thePolyg> and
        the facets of <thePolyh>.
        """

class HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter(nanoocp.Intf.Intf_Polygon2d):
    def __init__(self, theOther: HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter) -> None: ...

    def DeflectionOverEstimation(self) -> float: ...

    def SetDeflectionOverEstimation(self, x: float) -> None: ...

    @overload
    def Closed(self, clos: bool) -> None: ...

    @overload
    def Closed(self) -> bool:
        """Returns True if the polyline is closed."""

    def NbSegments(self) -> int:
        """Give the number of Segments in the polyline."""

    def Segment(self, theIndex: int, theBegin: nanoocp.gp.gp_Pnt2d, theEnd: nanoocp.gp.gp_Pnt2d) -> None:
        """Returns the points of the segment <Index> in the Polygon."""

    def InfParameter(self) -> float:
        """
        Returns the parameter (On the curve)
        of the first point of the Polygon
        """

    def SupParameter(self) -> float:
        """
        Returns the parameter (On the curve)
        of the last point of the Polygon
        """

    def AutoIntersectionIsPossible(self) -> bool: ...

    def ApproxParamOnCurve(self, Index: int, ParamOnLine: float) -> float:
        """
        Give an approximation of the parameter on the curve
        according to the discretization of the Curve.
        """

    def CalculRegion(self, x: float, y: float, x1: float, x2: float, y1: float, y2: float) -> int: ...

    def Dump(self) -> None: ...

class HLRBRep_ThePolygonOfInterCSurf:
    @overload
    def __init__(self, Curve: nanoocp.gp.gp_Lin, NbPnt: int) -> None: ...

    @overload
    def __init__(self, Curve: nanoocp.gp.gp_Lin, Upars: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, Curve: nanoocp.gp.gp_Lin, U1: float, U2: float, NbPnt: int) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_ThePolygonOfInterCSurf) -> None: ...

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the polygon."""

    def DeflectionOverEstimation(self) -> float: ...

    def SetDeflectionOverEstimation(self, x: float) -> None: ...

    @overload
    def Closed(self, flag: bool) -> None: ...

    @overload
    def Closed(self) -> bool: ...

    def NbSegments(self) -> int:
        """Give the number of Segments in the polyline."""

    def BeginOfSeg(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    def EndOfSeg(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    def InfParameter(self) -> float:
        """
        Returns the parameter (On the curve)
        of the first point of the Polygon
        """

    def SupParameter(self) -> float:
        """
        Returns the parameter (On the curve)
        of the last point of the Polygon
        """

    def ApproxParamOnCurve(self, Index: int, ParamOnLine: float) -> float:
        """
        Give an approximation of the parameter on the curve
        according to the discretization of the Curve.
        """

    def Dump(self) -> None: ...

class HLRBRep_ThePolygonToolOfInterCSurf:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_ThePolygonToolOfInterCSurf) -> None: ...

    @staticmethod
    def Bounding(thePolygon: HLRBRep_ThePolygonOfInterCSurf) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the polygon."""

    @staticmethod
    def DeflectionOverEstimation(thePolygon: HLRBRep_ThePolygonOfInterCSurf) -> float: ...

    @staticmethod
    def Closed(thePolygon: HLRBRep_ThePolygonOfInterCSurf) -> bool: ...

    @staticmethod
    def NbSegments(thePolygon: HLRBRep_ThePolygonOfInterCSurf) -> int: ...

    @staticmethod
    def BeginOfSeg(thePolygon: HLRBRep_ThePolygonOfInterCSurf, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    @staticmethod
    def EndOfSeg(thePolygon: HLRBRep_ThePolygonOfInterCSurf, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    @staticmethod
    def Dump(thePolygon: HLRBRep_ThePolygonOfInterCSurf) -> None: ...

class HLRBRep_ThePolyhedronOfInterCSurf:
    @overload
    def __init__(self, Surface: HLRBRep_Surface, Upars: nanoocp.NCollection.NCollection_Array1[float], Vpars: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, Surface: HLRBRep_Surface, nbdU: int, nbdV: int, U1: float, V1: float, U2: float, V2: float) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

    def Destroy(self) -> None: ...

    @overload
    def DeflectionOverEstimation(self, flec: float) -> None: ...

    @overload
    def DeflectionOverEstimation(self) -> float: ...

    def UMinSingularity(self, Sing: bool) -> None: ...

    def UMaxSingularity(self, Sing: bool) -> None: ...

    def VMinSingularity(self, Sing: bool) -> None: ...

    def VMaxSingularity(self, Sing: bool) -> None: ...

    def Size(self) -> tuple[int, int]:
        """get the size of the discretization."""

    def NbTriangles(self) -> int:
        """Give the number of triangles in this double array of"""

    def Triangle(self, Index: int) -> tuple[int, int, int]:
        """
        Give the 3 points of the triangle of address Index in
        the double array of triangles.
        """

    def TriConnex(self, Triang: int, Pivot: int, Pedge: int) -> tuple[int, int, int]:
        """
        Give the address Tricon of the triangle connexe to the
        triangle of address Triang by the edge Pivot Pedge and
        the third point of this connexe triangle. When we are
        on a free edge TriCon==0 but the function return the
        value of the triangle in the other side of Pivot on
        the free edge. Used to turn around a vertex.
        """

    def NbPoints(self) -> int:
        """
        Give the number of point in the double array of
        triangles ((nbdu+1)*(nbdv+1)).
        """

    @overload
    def Point(self, thePnt: nanoocp.gp.gp_Pnt, lig: int, col: int, U: float, V: float) -> None:
        """
        Set the value of a field of the double array of
        points.
        """

    @overload
    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def Point(self, Index: int, P: nanoocp.gp.gp_Pnt) -> None:
        """Give the point of index i in the MaTriangle."""

    def Point__float__float(self, Index: int) -> tuple[nanoocp.gp.gp_Pnt, float, float]:
        """
        Point__float__float: the C++ overload Point(const int, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Give the point of index i in the MaTriangle.
        """

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the MaTriangle."""

    def FillBounding(self) -> None:
        """
        Compute the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    def ComponentsBounding(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]:
        """
        Give the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    def HasUMinSingularity(self) -> bool: ...

    def HasUMaxSingularity(self) -> bool: ...

    def HasVMinSingularity(self) -> bool: ...

    def HasVMaxSingularity(self) -> bool: ...

    def PlaneEquation(self, Triang: int, NormalVector: nanoocp.gp.gp_XYZ) -> float:
        """Give the plane equation of the triangle of address Triang."""

    def Contain(self, Triang: int, ThePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Give the plane equation of the triangle of address Triang."""

    def Parameters(self, Index: int) -> tuple[float, float]: ...

    def IsOnBound(self, Index1: int, Index2: int) -> bool:
        """
        This method returns true if the edge based on points with
        indices Index1 and Index2 represents a boundary edge. It is
        necessary to take into account the boundary deflection for
        this edge.
        """

    def GetBorderDeflection(self) -> float:
        """This method returns a border deflection."""

    def Dump(self) -> None: ...

class HLRBRep_ThePolyhedronToolOfInterCSurf:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_ThePolyhedronToolOfInterCSurf) -> None: ...

    @staticmethod
    def Bounding(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the PolyhedronTool."""

    @staticmethod
    def ComponentsBounding(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]:
        """
        Give the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    @staticmethod
    def DeflectionOverEstimation(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> float:
        """Give the tolerance of the polygon."""

    @staticmethod
    def NbTriangles(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> int:
        """Give the number of triangles in this polyhedral surface."""

    @staticmethod
    def Triangle(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, Index: int) -> tuple[int, int, int]:
        """
        Give the indices of the 3 points of the triangle of
        address Index in the PolyhedronTool.
        """

    @staticmethod
    def Point(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of index i in the polyhedral surface."""

    @staticmethod
    def TriConnex(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, Triang: int, Pivot: int, Pedge: int) -> tuple[int, int, int]:
        """
        Give the address Tricon of the triangle connexe to
        the triangle of address Triang by the edge Pivot Pedge
        and the third point of this connexe triangle.
        When we are on a free edge TriCon==0 but the function return
        the value of the triangle in the other side of Pivot on the free edge.
        Used to turn around a vertex.
        """

    @staticmethod
    def IsOnBound(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf, Index1: int, Index2: int) -> bool:
        """
        This method returns true if the edge based on points with
        indices Index1 and Index2 represents a boundary edge.
        It is necessary to take into account the boundary deflection for this edge.
        """

    @staticmethod
    def GetBorderDeflection(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> float:
        """This method returns a border deflection of the polyhedron."""

    @staticmethod
    def Dump(thePolyh: HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...

class HLRBRep_TheProjPCurOfCInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_TheProjPCurOfCInter) -> None: ...

class HLRBRep_TheQuadCurvExactInterCSurf:
    @overload
    def __init__(self, S: HLRBRep_Surface, C: nanoocp.gp.gp_Lin) -> None:
        """
        Provides the signed distance function : Q(w)
        and its first derivative dQ(w)/dw
        """

    @overload
    def __init__(self, theOther: HLRBRep_TheQuadCurvExactInterCSurf) -> None: ...

    def IsDone(self) -> bool: ...

    def NbRoots(self) -> int: ...

    def Root(self, Index: int) -> float: ...

    def NbIntervals(self) -> int: ...

    def Intervals(self, Index: int) -> tuple[float, float]:
        """
        U1 and U2 are the parameters of
        a segment on the curve.
        """

class HLRBRep_TheQuadCurvFuncOfTheQuadCurvExactInterCSurf(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self, Q: nanoocp.IntSurf.IntSurf_Quadric, C: nanoocp.gp.gp_Lin) -> None:
        """Create the function."""

    @overload
    def __init__(self, theOther: HLRBRep_TheQuadCurvFuncOfTheQuadCurvExactInterCSurf) -> None: ...

    def Value(self, Param: float) -> tuple[bool, float]:
        """
        Computes the value of the signed distance between
        the implicit surface and the point at parameter
        Param on the parametrised curve.
        Value always returns True.
        """

    def Derivative(self, Param: float) -> tuple[bool, float]:
        """
        Computes the derivative of the previous function at
        parameter Param.
        Derivative always returns True.
        """

    def Values(self, Param: float) -> tuple[bool, float, float]:
        """
        Computes the value and the derivative of the function.
        returns True.
        """

class HLRBRep_VertexList:
    @overload
    def __init__(self, T: HLRBRep_EdgeInterferenceTool, I: nanoocp.NCollection.NCollection_List__HLRAlgo_Interference.Iterator) -> None: ...

    @overload
    def __init__(self, theOther: HLRBRep_VertexList) -> None: ...

    def __iter__(self) -> HLRBRep_VertexList:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.HLRAlgo.HLRAlgo_Intersection:
        """Python addition: see __iter__."""

    def IsPeriodic(self) -> bool:
        """Returns True when the curve is periodic."""

    def More(self) -> bool:
        """Returns True when there are more vertices."""

    def Next(self) -> None:
        """Proceeds to the next vertex."""

    def Current(self) -> nanoocp.HLRAlgo.HLRAlgo_Intersection:
        """Returns the current vertex"""

    def IsBoundary(self) -> bool:
        """Returns True if the current vertex is on the boundary of the edge."""

    def IsInterference(self) -> bool:
        """
        Returns True if the current vertex is an
        interference.
        """

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the orientation of the current vertex if
        it is on the boundary of the edge.
        """

    def Transition(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the transition of the current vertex if
        it is an interference.
        """

    def BoundaryTransition(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the transition of the current vertex
        relative to the boundary if it is an interference.
        """

class LProp_CurveUtils_ToolAccess__HLRBRep_CLPropsATool:
    """
    Tool-based access policy: delegates to static Tool methods.
    Used for HLRBRep types where Tool class provides the interface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LProp_CurveUtils_ToolAccess__HLRBRep_CLPropsATool) -> None: ...

class LProp_SurfaceUtils_ToolAccess__HLRBRep_SLPropsATool:
    """
    Tool-based access policy: delegates to static Tool methods.
    Used for HLRBRep types where Tool class provides the interface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LProp_SurfaceUtils_ToolAccess__HLRBRep_SLPropsATool) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BRepTopAdaptor
import nanoocp.HLRBRep
import nanoocp.TopTools
HLRBRep_Array1OfEData = nanoocp.NCollection.NCollection_Array1[nanoocp.HLRBRep.HLRBRep_EdgeData]
HLRBRep_Array1OfFData = nanoocp.NCollection.NCollection_Array1[nanoocp.HLRBRep.HLRBRep_FaceData]
HLRBRep_SeqOfShapeBounds = nanoocp.NCollection.NCollection_Sequence[nanoocp.HLRBRep.HLRBRep_ShapeBounds]
