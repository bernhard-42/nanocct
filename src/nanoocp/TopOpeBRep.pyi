"""OCCT package TopOpeBRep (toolkit TKBool)"""

import enum
from typing import overload

import nanoocp.BRepAdaptor
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Geom2dAdaptor
import nanoocp.IntPatch
import nanoocp.IntRes2d
import nanoocp.IntSurf
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopOpeBRepDS
import nanoocp.TopOpeBRepTool
import nanoocp.TopoDS
import nanoocp.gp


class TopOpeBRep_TypeLineCurve(enum.IntEnum):
    TopOpeBRep_ANALYTIC = 0

    TopOpeBRep_RESTRICTION = 1

    TopOpeBRep_WALKING = 2

    TopOpeBRep_LINE = 3

    TopOpeBRep_CIRCLE = 4

    TopOpeBRep_ELLIPSE = 5

    TopOpeBRep_PARABOLA = 6

    TopOpeBRep_HYPERBOLA = 7

    TopOpeBRep_OTHERTYPE = 8

TopOpeBRep_ANALYTIC: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_ANALYTIC

TopOpeBRep_RESTRICTION: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_RESTRICTION

TopOpeBRep_WALKING: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_WALKING

TopOpeBRep_LINE: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_LINE

TopOpeBRep_CIRCLE: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_CIRCLE

TopOpeBRep_ELLIPSE: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_ELLIPSE

TopOpeBRep_PARABOLA: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_PARABOLA

TopOpeBRep_HYPERBOLA: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_HYPERBOLA

TopOpeBRep_OTHERTYPE: TopOpeBRep_TypeLineCurve = TopOpeBRep_TypeLineCurve.TopOpeBRep_OTHERTYPE

class TopOpeBRep_P2Dstatus(enum.IntEnum):
    TopOpeBRep_P2DUNK = 0

    TopOpeBRep_P2DINT = 1

    TopOpeBRep_P2DSGF = 2

    TopOpeBRep_P2DSGL = 3

    TopOpeBRep_P2DNEW = 4

TopOpeBRep_P2DUNK: TopOpeBRep_P2Dstatus = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DUNK

TopOpeBRep_P2DINT: TopOpeBRep_P2Dstatus = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DINT

TopOpeBRep_P2DSGF: TopOpeBRep_P2Dstatus = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGF

TopOpeBRep_P2DSGL: TopOpeBRep_P2Dstatus = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGL

TopOpeBRep_P2DNEW: TopOpeBRep_P2Dstatus = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DNEW

class TopOpeBRep:
    """
    This package provides the topological operations
    on the BRep data structure.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep) -> None: ...

    @staticmethod
    def Print(TLC: TopOpeBRep_TypeLineCurve) -> object:
        """
        Prints the name of <TLC> as a String on the
        Stream <S> and returns <S>.
        """

class TopOpeBRep_Bipoint:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, I1: int, I2: int) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_Bipoint) -> None: ...

    def I1(self) -> int: ...

    def I2(self) -> int: ...

class TopOpeBRep_ShapeScanner:
    """
    Find, among the subshapes SS of a reference shape
    RS, the ones which 3D box interferes with the box of
    a shape S (SS and S are of the same type).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_ShapeScanner) -> None: ...

    def __iter__(self) -> TopOpeBRep_ShapeScanner:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Python addition: see __iter__."""

    def Clear(self) -> None: ...

    def AddBoxesMakeCOB(self, S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    @overload
    def Init(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Init(self, X: nanoocp.TopOpeBRepTool.TopOpeBRepTool_ShapeExplorer) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def BoxSort(self) -> nanoocp.TopOpeBRepTool.TopOpeBRepTool_BoxSort: ...

    def ChangeBoxSort(self) -> nanoocp.TopOpeBRepTool.TopOpeBRepTool_BoxSort: ...

    def Index(self) -> int: ...

    def DumpCurrent(self) -> object: ...

class TopOpeBRep_WPointInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_WPointInter) -> None: ...

    def Set(self, P: nanoocp.IntSurf.IntSurf_PntOn2S) -> None: ...

    def ParametersOnS1(self) -> tuple[float, float]: ...

    def ParametersOnS2(self) -> tuple[float, float]: ...

    def Parameters(self) -> tuple[float, float, float, float]: ...

    def ValueOnS1(self) -> nanoocp.gp.gp_Pnt2d: ...

    def ValueOnS2(self) -> nanoocp.gp.gp_Pnt2d: ...

    def Value(self) -> nanoocp.gp.gp_Pnt: ...

    def PPntOn2SDummy(self) -> nanoocp.IntSurf.IntSurf_PntOn2S: ...

class TopOpeBRep_VPointInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_VPointInter) -> None: ...

    def SetPoint(self, P: nanoocp.IntPatch.IntPatch_Point) -> None: ...

    def SetShapes(self, I1: int, I2: int) -> None: ...

    def GetShapes(self) -> tuple[int, int]: ...

    def TransitionOnS1(self) -> nanoocp.IntSurf.IntSurf_Transition: ...

    def TransitionOnS2(self) -> nanoocp.IntSurf.IntSurf_Transition: ...

    def TransitionLineArc1(self) -> nanoocp.IntSurf.IntSurf_Transition: ...

    def TransitionLineArc2(self) -> nanoocp.IntSurf.IntSurf_Transition: ...

    def IsOnDomS1(self) -> bool: ...

    def IsOnDomS2(self) -> bool: ...

    def ParametersOnS1(self) -> tuple[float, float]: ...

    def ParametersOnS2(self) -> tuple[float, float]: ...

    def Value(self) -> nanoocp.gp.gp_Pnt: ...

    def Tolerance(self) -> float: ...

    def ArcOnS1(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ArcOnS2(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ParameterOnLine(self) -> float: ...

    def ParameterOnArc1(self) -> float: ...

    def IsVertexOnS1(self) -> bool:
        """
        Returns TRUE if the point is a vertex on the initial
        restriction facet of the first surface.
        """

    def VertexOnS1(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the information about the point when it is
        on the domain of the first patch, i-e when the function
        IsVertexOnS1 returns True.
        Otherwise, an exception is raised.
        """

    def ParameterOnArc2(self) -> float: ...

    def IsVertexOnS2(self) -> bool:
        """
        Returns TRUE if the point is a vertex on the initial
        restriction facet of the second surface.
        """

    def VertexOnS2(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the information about the point when it is
        on the domain of the second patch, i-e when the function
        IsVertexOnS2 returns True.
        Otherwise, an exception is raised.
        """

    def IsInternal(self) -> bool: ...

    def IsMultiple(self) -> bool:
        """
        Returns True if the point belongs to several intersection
        lines.
        """

    @overload
    def State(self, I: int) -> nanoocp.TopAbs.TopAbs_State:
        """
        get state of VPoint within the domain of geometric shape
        domain <I> (= 1 or 2).
        """

    @overload
    def State(self, S: nanoocp.TopAbs.TopAbs_State, I: int) -> None:
        """
        Set the state of VPoint within the domain of
        the geometric shape <I> (= 1 or 2).
        """

    @overload
    def EdgeON(self, Eon: nanoocp.TopoDS.TopoDS_Shape, Par: float, I: int) -> None:
        """
        set the shape Eon of shape I (1,2) containing the point,
        and parameter <Par> of point on <Eon>.
        """

    @overload
    def EdgeON(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """get the edge of shape I (1,2) containing the point."""

    def EdgeONParameter(self, I: int) -> float:
        """get the parameter on edge of shape I (1,2) containing the point."""

    @overload
    def ShapeIndex(self) -> int:
        """
        returns value of filed myShapeIndex = 0,1,2,3
        0 means the VPoint is on no restriction
        1 means the VPoint is on the restriction 1
        2 means the VPoint is on the restriction 2
        3 means the VPoint is on the restrictions 1 and 2
        """

    @overload
    def ShapeIndex(self, I: int) -> None:
        """set value of shape supporting me (0,1,2,3)."""

    def Edge(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        get the edge of shape I (1,2) containing the point.
        Returned shape is null if the VPoint is not on an edge
        of shape I (1,2).
        """

    def EdgeParameter(self, I: int) -> float:
        """get the parameter on edge of shape I (1,2) containing the point"""

    def SurfaceParameters(self, I: int) -> nanoocp.gp.gp_Pnt2d:
        """get the parameter on surface of shape I (1,2) containing the point"""

    def IsVertex(self, I: int) -> bool: ...

    def Vertex(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def UpdateKeep(self) -> None:
        """set myKeep value according to current states."""

    def Keep(self) -> bool:
        """
        Returns value of myKeep (does not evaluate states)
        False at creation of VPoint.
        Updated by State(State from TopAbs,Integer from Standard)
        """

    def ChangeKeep(self, keep: bool) -> None:
        """updates VPointInter flag "keep" with <keep>."""

    def EqualpP(self, VP: TopOpeBRep_VPointInter) -> bool:
        """
        returns <True> if the 3d points and the parameters of the
        VPoints are same
        """

    def ParonE(self, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]:
        """
        returns <false> if the vpoint is not given on arc <E>,
        else returns <par> parameter on <E>
        """

    @overload
    def Index(self, I: int) -> None: ...

    @overload
    def Index(self) -> int: ...

    @overload
    def Dump(self, I: int, F: nanoocp.TopoDS.TopoDS_Face) -> object: ...

    @overload
    def Dump(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> object: ...

    def PThePointOfIntersectionDummy(self) -> nanoocp.IntPatch.IntPatch_Point: ...

class TopOpeBRep_LineInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_LineInter) -> None: ...

    def SetLine(self, L: nanoocp.IntPatch.IntPatch_Line | None, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> None: ...

    def SetFaces(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def TypeLineCurve(self) -> TopOpeBRep_TypeLineCurve: ...

    def NbVPoint(self) -> int: ...

    def VPoint(self, I: int) -> TopOpeBRep_VPointInter: ...

    def ChangeVPoint(self, I: int) -> TopOpeBRep_VPointInter: ...

    def SetINL(self) -> None: ...

    def INL(self) -> bool: ...

    def SetIsVClosed(self) -> None: ...

    def IsVClosed(self) -> bool: ...

    def SetOK(self, B: bool) -> None: ...

    def OK(self) -> bool: ...

    def SetHasVPonR(self) -> None: ...

    def HasVPonR(self) -> bool: ...

    def SetVPBounds(self) -> None: ...

    def VPBounds(self) -> tuple[int, int, int]: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Bounds(self) -> tuple[float, float]: ...

    def HasVInternal(self) -> bool: ...

    def NbWPoint(self) -> int: ...

    def WPoint(self, I: int) -> TopOpeBRep_WPointInter: ...

    def TransitionOnS1(self) -> nanoocp.IntSurf.IntSurf_TypeTrans: ...

    def TransitionOnS2(self) -> nanoocp.IntSurf.IntSurf_TypeTrans: ...

    def SituationS1(self) -> nanoocp.IntSurf.IntSurf_Situation: ...

    def SituationS2(self) -> nanoocp.IntSurf.IntSurf_Situation: ...

    @overload
    def Curve(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve(self, parmin: float, parmax: float) -> nanoocp.Geom.Geom_Curve: ...

    def Arc(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns the edge of a RESTRICTION line (or a null edge)."""

    def ArcIsEdge(self, I: int) -> bool:
        """
        returns true if Arc() edge (of a RESTRICTION line) is
        an edge of the original face <Index> (1 or 2).
        """

    def LineW(self) -> nanoocp.IntPatch.IntPatch_WLine: ...

    def LineG(self) -> nanoocp.IntPatch.IntPatch_GLine: ...

    def LineR(self) -> nanoocp.IntPatch.IntPatch_RLine: ...

    def HasFirstPoint(self) -> bool: ...

    def HasLastPoint(self) -> bool: ...

    def ComputeFaceFaceTransition(self) -> None: ...

    def FaceFaceTransition(self, I: int) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    @overload
    def Index(self, I: int) -> None: ...

    @overload
    def Index(self) -> int: ...

    def DumpType(self) -> None: ...

    def DumpVPoint(self, I: int, s1: nanoocp.TCollection.TCollection_AsciiString, s2: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def DumpBipoint(self, B: TopOpeBRep_Bipoint, s1: nanoocp.TCollection.TCollection_AsciiString, s2: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetTraceIndex(self, exF1: int, exF2: int) -> None: ...

    def GetTraceIndex(self) -> tuple[int, int]: ...

    def DumpLineTransitions(self) -> object: ...

class TopOpeBRep_FacesIntersector:
    """Describes the intersection of two faces."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_FacesIntersector) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, B1: nanoocp.Bnd.Bnd_Box, B2: nanoocp.Bnd.Bnd_Box) -> None:
        """Computes the intersection of faces S1 and S2."""

    def IsEmpty(self) -> bool: ...

    def IsDone(self) -> bool: ...

    def SameDomain(self) -> bool:
        """
        Returns True if Perform() arguments are two faces with the
        same surface.
        """

    def Face(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns first or second intersected face."""

    def SurfacesSameOriented(self) -> bool:
        """
        Returns True if Perform() arguments are two faces
        SameDomain() and normals on both side.
        Raise if SameDomain is False
        """

    def IsRestriction(self, E: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        returns true if edge <E> is found as same as the edge
        associated with a RESTRICTION line.
        """

    def Restrictions(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """returns the map of edges found as TopeBRepBRep_RESTRICTION"""

    def PrepareLines(self) -> None: ...

    def Lines(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TopOpeBRep.TopOpeBRep_LineInter]: ...

    def NbLines(self) -> int: ...

    def InitLine(self) -> None: ...

    def MoreLine(self) -> bool: ...

    def NextLine(self) -> None: ...

    def CurrentLine(self) -> TopOpeBRep_LineInter: ...

    def CurrentLineIndex(self) -> int: ...

    def ChangeLine(self, IL: int) -> TopOpeBRep_LineInter: ...

    def ForceTolerances(self, tolarc: float, toltang: float) -> None:
        """Force the tolerance values used by the next Perform(S1,S2) call."""

    def GetTolerances(self) -> tuple[float, float]:
        """
        Return the tolerance values used in the last Perform() call
        If ForceTolerances() has been called, return the given values.
        If not, return values extracted from shapes.
        """

class TopOpeBRep_Point2d:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_Point2d) -> None: ...

    def Dump(self, ie1: int = 0, ie2: int = 0) -> None: ...

    def SetPint(self, P: nanoocp.IntRes2d.IntRes2d_IntersectionPoint) -> None: ...

    def HasPint(self) -> bool: ...

    def Pint(self) -> nanoocp.IntRes2d.IntRes2d_IntersectionPoint: ...

    def SetIsVertex(self, I: int, B: bool) -> None: ...

    def IsVertex(self, I: int) -> bool: ...

    def SetVertex(self, I: int, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def Vertex(self, I: int) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def SetTransition(self, I: int, T: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition) -> None: ...

    def Transition(self, I: int) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    def ChangeTransition(self, I: int) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    def SetParameter(self, I: int, P: float) -> None: ...

    def Parameter(self, I: int) -> float: ...

    def SetIsPointOfSegment(self, B: bool) -> None: ...

    def IsPointOfSegment(self) -> bool: ...

    def SetSegmentAncestors(self, IP1: int, IP2: int) -> None: ...

    def SegmentAncestors(self) -> tuple[bool, int, int]: ...

    def SetStatus(self, S: TopOpeBRep_P2Dstatus) -> None: ...

    def Status(self) -> TopOpeBRep_P2Dstatus: ...

    def SetIndex(self, X: int) -> None: ...

    def Index(self) -> int: ...

    def SetValue(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt: ...

    def SetValue2d(self, P: nanoocp.gp.gp_Pnt2d) -> None: ...

    def Value2d(self) -> nanoocp.gp.gp_Pnt2d: ...

    def SetKeep(self, B: bool) -> None: ...

    def Keep(self) -> bool: ...

    def SetEdgesConfig(self, C: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: ...

    def EdgesConfig(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config: ...

    def SetTolerance(self, T: float) -> None: ...

    def Tolerance(self) -> float: ...

    def SetHctxff2d(self, ff2d: TopOpeBRep_Hctxff2d | None) -> None: ...

    def Hctxff2d(self) -> TopOpeBRep_Hctxff2d: ...

    def SetHctxee2d(self, ee2d: TopOpeBRep_Hctxee2d | None) -> None: ...

    def Hctxee2d(self) -> TopOpeBRep_Hctxee2d: ...

class TopOpeBRep_EdgesIntersector:
    """Describes the intersection of two edges on the same surface"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_EdgesIntersector) -> None: ...

    @overload
    def SetFaces(self, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def SetFaces(self, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape, B1: nanoocp.Bnd.Bnd_Box, B2: nanoocp.Bnd.Bnd_Box) -> None: ...

    def ForceTolerances(self, Tol1: float, Tol2: float) -> None: ...

    @overload
    def Dimension(self, D: int) -> None: ...

    @overload
    def Dimension(self) -> int:
        """set working space dimension D = 1 for E &|| W, 2 for E in F"""

    def Perform(self, E1: nanoocp.TopoDS.TopoDS_Shape, E2: nanoocp.TopoDS.TopoDS_Shape, ReduceSegments: bool = True) -> None: ...

    def IsEmpty(self) -> bool: ...

    def HasSegment(self) -> bool:
        """true if at least one intersection segment."""

    def SameDomain(self) -> bool:
        """= mySameDomain."""

    def Edge(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Curve(self, Index: int) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve: ...

    def Face(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Surface(self, Index: int) -> nanoocp.BRepAdaptor.BRepAdaptor_Surface: ...

    def SurfacesSameOriented(self) -> bool: ...

    def FacesSameOriented(self) -> bool: ...

    def ToleranceMax(self) -> float: ...

    def Tolerances(self) -> tuple[float, float]: ...

    def NbPoints(self) -> int: ...

    def NbSegments(self) -> int: ...

    def Dump(self, str: nanoocp.TCollection.TCollection_AsciiString, ie1: int = 0, ie2: int = 0) -> None: ...

    def InitPoint(self, selectkeep: bool = True) -> None: ...

    def MorePoint(self) -> bool: ...

    def NextPoint(self) -> None: ...

    def Points(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TopOpeBRep.TopOpeBRep_Point2d]: ...

    @overload
    def Point(self) -> TopOpeBRep_Point2d: ...

    @overload
    def Point(self, I: int) -> TopOpeBRep_Point2d: ...

    def ReduceSegment(self, P1: TopOpeBRep_Point2d, P2: TopOpeBRep_Point2d, Pn: TopOpeBRep_Point2d) -> bool: ...

    def Status1(self) -> TopOpeBRep_P2Dstatus: ...

class TopOpeBRep_FaceEdgeIntersector:
    """Describes the intersection of a face and an edge."""

    def __init__(self) -> None: ...

    def Perform(self, F: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def IsEmpty(self) -> bool: ...

    def Shape(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns intersected face or edge according to
        value of <Index> = 1 or 2
        """

    def ForceTolerance(self, tol: float) -> None:
        """Force the tolerance values used by the next Perform(S1,S2) call."""

    def Tolerance(self) -> float:
        """
        Return the tolerance value used in the last Perform() call
        If ForceTolerance() has been called, return the given value.
        If not, return value extracted from shapes.
        """

    def NbPoints(self) -> int: ...

    def InitPoint(self) -> None: ...

    def MorePoint(self) -> bool: ...

    def NextPoint(self) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """return the 3D point of the current intersection point."""

    def Parameter(self) -> float:
        """parametre de Value() sur l'arete"""

    def UVPoint(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """parametre de Value() sur la face"""

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """IN ou ON / a la face. Les points OUT ne sont pas retournes."""

    def Transition(self, Index: int, FaceOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition:
        """Index = 1 transition par rapport a la face, en cheminant sur l'arete"""

    @overload
    def IsVertex(self, S: nanoocp.TopoDS.TopoDS_Shape, P: nanoocp.gp.gp_Pnt, Tol: float, V: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

    @overload
    def IsVertex(self, I: int, V: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

    def Index(self) -> int:
        """trace only"""

class TopOpeBRep_ShapeIntersector:
    """
    Intersect two shapes.

    A GeomShape is a shape with a geometric domain, i.e.
    a Face or an Edge.

    The purpose of the ShapeIntersector is to find
    couples of intersecting GeomShape in two Shapes
    (which can be any kind of topologies : Compound,
    Solid, Shell, etc... )

    It is in charge of exploration of the shapes and
    rejection. For this it is provided with two tools:

    - ShapeExplorer from TopOpeBRepTool.
    - ShapeScanner from TopOpeBRep which implements bounding boxes.

    Let S1,S2 the shapes sent to InitIntersection(S1,S2) method:
    - S1 is always SCANNED by a ShapeScanner from TopOpeBRep.
    - S2 is always EXPLORED by a ShapeExplorer from TopOpeBRepTool.
    """

    def __init__(self) -> None: ...

    @overload
    def InitIntersection(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def InitIntersection(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initialize the intersection of shapes S1,S2."""

    def Shape(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        return the shape <Index> ( = 1 or 2) given to
        InitIntersection().
        Index = 1 will return S1, Index = 2 will return S2.
        """

    def MoreIntersection(self) -> bool:
        """
        returns True if there are more intersection
        between two the shapes.
        """

    def NextIntersection(self) -> None:
        """search for the next intersection between the two shapes."""

    def ChangeFacesIntersector(self) -> TopOpeBRep_FacesIntersector:
        """return the current intersection of two Faces."""

    def ChangeEdgesIntersector(self) -> TopOpeBRep_EdgesIntersector:
        """return the current intersection of two Edges."""

    def ChangeFaceEdgeIntersector(self) -> TopOpeBRep_FaceEdgeIntersector:
        """return the current intersection of a Face and an Edge."""

    def CurrentGeomShape(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        return geometric shape <Index> ( = 1 or 2 ) of
        current intersection.
        """

    def GetTolerances(self) -> tuple[float, float]:
        """
        return MAX of intersection tolerances with
        which FacesIntersector from TopOpeBRep was working.
        """

    def DumpCurrent(self, K: int) -> None: ...

    def Index(self, K: int) -> int: ...

    def RejectedFaces(self, anObj: nanoocp.TopoDS.TopoDS_Shape, aReference: nanoocp.TopoDS.TopoDS_Shape, aListOfShape: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

class TopOpeBRep_ShapeIntersector2d:
    """
    Intersect two shapes.

    A GeomShape is a shape with a geometric domain, i.e.
    a Face or an Edge.

    The purpose of the ShapeIntersector2d is to find
    couples of intersecting GeomShape in two Shapes
    (which can be any kind of topologies: Compound,
    Solid, Shell, etc... )

    It is in charge of exploration of the shapes and
    rejection. For this it is provided with two tools:

    - ShapeExplorer from TopOpeBRepTool.
    - ShapeScanner from TopOpeBRep which implements bounding boxes.

    Let S1,S2 the shapes sent to InitIntersection(S1,S2) method:
    - S1 is always SCANNED by a ShapeScanner from TopOpeBRep.
    - S2 is always EXPLORED by a ShapeExplorer from TopOpeBRepTool.
    """

    def __init__(self) -> None: ...

    def InitIntersection(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize the intersection of shapes S1,S2."""

    def Shape(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        return the shape <Index> ( = 1 or 2) given to
        InitIntersection().
        Index = 1 will return S1, Index = 2 will return S2.
        """

    def MoreIntersection(self) -> bool:
        """
        returns True if there are more intersection
        between two the shapes.
        """

    def NextIntersection(self) -> None:
        """search for the next intersection between the two shapes."""

    def ChangeEdgesIntersector(self) -> TopOpeBRep_EdgesIntersector:
        """return the current intersection of two Edges."""

    def CurrentGeomShape(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        return geometric shape <Index> ( = 1 or 2 ) of
        current intersection.
        """

    def DumpCurrent(self, K: int) -> None: ...

    def Index(self, K: int) -> int: ...

class TopOpeBRep_PointClassifier:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_PointClassifier) -> None: ...

    def Init(self) -> None: ...

    def Load(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def Classify(self, F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> nanoocp.TopAbs.TopAbs_State:
        """compute position of point <P> regarding with the face <F>."""

    def State(self) -> nanoocp.TopAbs.TopAbs_State: ...

class TopOpeBRep_FacesFiller:
    """
    Fills a DataStructure from TopOpeBRepDS with the result
    of Face/Face intersection described by FacesIntersector from TopOpeBRep.
    if the faces have same Domain, record it in the DS.
    else record lines and points and attach list of interferences
    to the faces, the lines and the edges.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_FacesFiller) -> None: ...

    def Insert(self, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape, FACINT: TopOpeBRep_FacesIntersector, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """Stores in <DS> the intersections of <S1> and <S2>."""

    def ProcessSectionEdges(self) -> None: ...

    def ChangePointClassifier(self) -> TopOpeBRep_PointClassifier: ...

    def PShapeClassifier(self) -> nanoocp.TopOpeBRepTool.TopOpeBRepTool_ShapeClassifier:
        """return field myPShapeClassifier."""

    def LoadLine(self, L: TopOpeBRep_LineInter) -> None: ...

    def CheckLine(self, L: TopOpeBRep_LineInter) -> bool: ...

    @overload
    def VP_Position(self, FACINT: TopOpeBRep_FacesIntersector) -> None:
        """compute position of VPoints of lines"""

    @overload
    def VP_Position(self, L: TopOpeBRep_LineInter) -> None:
        """compute position of VPoints of line L"""

    @overload
    def VP_Position(self, VP: TopOpeBRep_VPointInter, VPC: TopOpeBRep_VPointInterClassifier) -> None:
        """
        compute position of VP with current faces,
        according to VP.ShapeIndex() .
        """

    def VP_PositionOnL(self, L: TopOpeBRep_LineInter) -> None:
        """compute position of VPoints of non-restriction line L."""

    def VP_PositionOnR(self, L: TopOpeBRep_LineInter) -> None:
        """compute position of VPoints of restriction line L."""

    def ProcessLine(self) -> None:
        """Process current intersection line (set by LoadLine)"""

    def ResetDSC(self) -> None: ...

    def ProcessRLine(self) -> None:
        """
        Process current restriction line, adding restriction edge
        and computing face/edge interference.
        """

    def FillLineVPonR(self) -> None:
        """
        VP processing for restriction line and line sharing
        same domain with section edges:
        - if restriction:
        Adds restriction edges as section edges and compute
        face/edge interference.
        - if same domain:
        If line share same domain with section edges, compute
        parts of line IN/IN the two faces, and compute curve/point
        interference for VP boundaries.
        """

    def FillLine(self) -> None: ...

    def AddShapesLine(self) -> None:
        """
        compute 3d curve, pcurves and face/curve interferences
        for current NDSC. Add them to the DS.
        """

    def GetESL(self, LES: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Get map <mapES > of restriction edges having parts IN one
        of the 2 faces.
        """

    def ProcessVPR(self, FF: TopOpeBRep_FacesFiller, VP: TopOpeBRep_VPointInter) -> None:
        """calling the following ProcessVPIonR and ProcessVPonR."""

    def ProcessVPIonR(self, VPI: TopOpeBRep_VPointInterIterator, trans1: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition, F1: nanoocp.TopoDS.TopoDS_Shape, ShapeIndex: int) -> None:
        """processing ProcessVPonR for VPI."""

    def ProcessVPonR(self, VP: TopOpeBRep_VPointInter, trans1: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition, F1: nanoocp.TopoDS.TopoDS_Shape, ShapeIndex: int) -> None:
        """
        adds <VP>'s geometric point (if not stored) and
        computes (curve or edge)/(point or vertex) interference.
        """

    def ProcessVPonclosingR(self, VP: TopOpeBRep_VPointInter, F1: nanoocp.TopoDS.TopoDS_Shape, ShapeIndex: int, transEdge: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition, PVKind: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind, PVIndex: int, EPIfound: bool, IEPI: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference | None) -> None:
        """VP processing on closing arc."""

    def ProcessVPondgE(self, VP: TopOpeBRep_VPointInter, ShapeIndex: int) -> tuple[bool, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind, int, bool, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference, bool, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]:
        """VP processing on degenerated arc."""

    def ProcessVPInotonR(self, VPI: TopOpeBRep_VPointInterIterator) -> None:
        """processing ProcessVPnotonR for VPI."""

    def ProcessVPnotonR(self, VP: TopOpeBRep_VPointInter) -> None:
        """
        adds <VP>'s geometrical point to the DS (if not stored)
        and computes curve point interference.
        """

    def GetGeometry(self, IT: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference].Iterator, VP: TopOpeBRep_VPointInter) -> tuple[bool, int, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind]:
        """
        Get the geometry of a DS point <DSP>.
        Search for it with ScanInterfList (previous method).
        if found, set <G> to the geometry of the interference found.
        else, add the point <DSP> in the <DS> and set <G> to the
        value of the new geometry such created.
        returns the value of ScanInterfList().
        """

    def MakeGeometry(self, VP: TopOpeBRep_VPointInter, ShapeIndex: int) -> tuple[int, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind]: ...

    def StoreCurveInterference(self, I: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference | None) -> None:
        """
        Add interference <I> to list myDSCIL.
        on a given line, at first call, add a new DS curve.
        """

    @overload
    def GetFFGeometry(self, DSP: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point) -> tuple[bool, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind, int]:
        """
        search for G = geometry of Point which is identical to <DSP>
        among the DS Points created in the CURRENT face/face
        intersection (current Insert() call).
        """

    @overload
    def GetFFGeometry(self, VP: TopOpeBRep_VPointInter) -> tuple[bool, nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind, int]:
        """
        search for G = geometry of Point which is identical to <VP>
        among the DS Points created in the CURRENT face/face
        intersection (current Insert() call).
        """

    def ChangeFacesIntersector(self) -> TopOpeBRep_FacesIntersector: ...

    def HDataStructure(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure: ...

    def ChangeDataStructure(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure: ...

    def Face(self, I: int) -> nanoocp.TopoDS.TopoDS_Face: ...

    @overload
    def FaceFaceTransition(self, L: TopOpeBRep_LineInter, I: int) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    @overload
    def FaceFaceTransition(self, I: int) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    def PFacesIntersectorDummy(self) -> TopOpeBRep_FacesIntersector: ...

    def PDataStructureDummy(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure: ...

    def PLineInterDummy(self) -> TopOpeBRep_LineInter: ...

    def SetTraceIndex(self, exF1: int, exF2: int) -> None: ...

    def GetTraceIndex(self) -> tuple[int, int]: ...

    @staticmethod
    def Lminmax(L: TopOpeBRep_LineInter) -> tuple[float, float]:
        """
        Computes <pmin> and <pmax> the upper and lower bounds of <L>
        enclosing all vpoints.
        """

    @staticmethod
    def LSameDomainERL(L: TopOpeBRep_LineInter, ERL: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Returns <True> if <L> shares a same geometric domain with
        at least one of the section edges of <ERL>.
        """

    @staticmethod
    def IsVPtransLok(L: TopOpeBRep_LineInter, iVP: int, SI12: int, T: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition) -> bool:
        """
        Computes the transition <T> of the VPoint <iVP> on the edge
        of <SI12>. Returns <False> if the status is unknown.
        """

    @staticmethod
    def TransvpOK(L: TopOpeBRep_LineInter, iVP: int, SI: int, isINOUT: bool) -> bool:
        """
        Computes transition on line for VP<iVP> on edge
        restriction of <SI>. If <isINOUT> : returns <true> if
        transition computed is IN/OUT else : returns <true> if
        transition computed is OUT/IN.
        """

    @staticmethod
    def VPParamOnER(vp: TopOpeBRep_VPointInter, Lrest: TopOpeBRep_LineInter) -> float:
        """Returns parameter u of vp on the restriction edge."""

    @staticmethod
    def EqualpPonR(Lrest: TopOpeBRep_LineInter, VP1: TopOpeBRep_VPointInter, VP2: TopOpeBRep_VPointInter) -> bool: ...

class TopOpeBRep_EdgesFiller:
    """
    Fills a TopOpeBRepDS_DataStructure with Edge/Edge
    intersection data described by TopOpeBRep_EdgesIntersector.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_EdgesFiller) -> None: ...

    def Insert(self, E1: nanoocp.TopoDS.TopoDS_Shape, E2: nanoocp.TopoDS.TopoDS_Shape, EI: TopOpeBRep_EdgesIntersector, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def Face(self, I: int, F: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Face(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

class TopOpeBRep_FaceEdgeFiller:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_FaceEdgeFiller) -> None: ...

    def Insert(self, F: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, FEINT: TopOpeBRep_FaceEdgeIntersector, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

class TopOpeBRep_DSFiller:
    """
    Provides class methods to fill a datastructure
    with results of intersections.

    1. Use an Intersector to find pairs of
    intersecting GeomShapes

    2. For each pair fill the DataStructure using the
    appropriate Filler.

    3. Complete the DataStructure to record shapes to
    rebuild (shells, wires)
    """

    def __init__(self) -> None: ...

    def PShapeClassifier(self) -> nanoocp.TopOpeBRepTool.TopOpeBRepTool_ShapeClassifier:
        """
        return field myPShapeClassifier.
        set field myPShapeClassifier.
        """

    def Insert(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None, orientFORWARD: bool = True) -> None:
        """
        Stores in <DS> the intersections of <S1> and <S2>.
        if orientFORWARD = True
        S FORWARD,REVERSED  --> FORWARD
        S EXTERNAL,INTERNAL --> EXTERNAL,INTERNAL
        """

    def InsertIntersection(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None, orientFORWARD: bool = True) -> None:
        """
        Stores in <DS> the intersections of <S1> and <S2>.
        if orientFORWARD = True
        S FORWAR,REVERSED   --> FORWARD
        S EXTERNAL,INTERNAL --> EXTERNAL,INTERNAL
        """

    def Complete(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    def Insert2d(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        Stores in <DS> the intersections of <S1> and <S2>.
        S1 and S2 contain only SameDomain Face
        """

    def InsertIntersection2d(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        S1, S2 set of tangent face
        Launches 2D intersection calculations to correctly
        code the SameDomain faces.
        """

    def IsMadeOf1d(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def IsContext1d(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def Insert1d(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None, orientFORWARD: bool = False) -> None:
        """
        Stores in <DS> the intersections of <S1> and <S2>.
        S1 and S2 are edges or wires.
        S1 edges have a 2d representation in face F1
        S2 edges have a 2d representation in face F2
        F1 is the face which surface is taken as reference
        for 2d description of S1 and S2 edges.
        if orientFORWARD = True
        S FORWARD,REVERSED  --> FORWARD
        S EXTERNAL,INTERNAL --> EXTERNAL,INTERNAL
        """

    def ChangeShapeIntersector(self) -> TopOpeBRep_ShapeIntersector: ...

    def ChangeShapeIntersector2d(self) -> TopOpeBRep_ShapeIntersector2d: ...

    def ChangeFacesFiller(self) -> TopOpeBRep_FacesFiller: ...

    def ChangeEdgesFiller(self) -> TopOpeBRep_EdgesFiller: ...

    def ChangeFaceEdgeFiller(self) -> TopOpeBRep_FaceEdgeFiller: ...

    def GapFiller(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    def CompleteDS(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        Update the data structure with relevant
        information deduced from the intersections.

        Shells containing an intersected face.
        Wires  containing an intersected edge.
        """

    def Filter(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    def Reducer(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    def RemoveUnsharedGeometry(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    def Checker(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    def CompleteDS2d(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        Update the data structure with relevant
        information deduced from the intersections 2d.

        Shells containing an intersected face.
        Wires  containing an intersected edge.

        search for interference identity using edge connexity //NYI
        """

class TopOpeBRep_FFDumper(nanoocp.Standard.Standard_Transient):
    def __init__(self, theOther: TopOpeBRep_FFDumper) -> None: ...

    @overload
    def DumpLine(self, I: int) -> None: ...

    @overload
    def DumpLine(self, L: TopOpeBRep_LineInter) -> None: ...

    @overload
    def DumpVP(self, VP: TopOpeBRep_VPointInter) -> None: ...

    @overload
    def DumpVP(self, VP: TopOpeBRep_VPointInter, ISI: int) -> None: ...

    def ExploreIndex(self, S: nanoocp.TopoDS.TopoDS_Shape, ISI: int) -> int: ...

    def DumpDSP(self, VP: TopOpeBRep_VPointInter, GK: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind, G: int, newinDS: bool) -> None: ...

    def PFacesFillerDummy(self) -> TopOpeBRep_FacesFiller: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRep_FFTransitionTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_FFTransitionTool) -> None: ...

    @overload
    @staticmethod
    def ProcessLineTransition(P: TopOpeBRep_VPointInter, Index: int, EdgeOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    @overload
    @staticmethod
    def ProcessLineTransition(P: TopOpeBRep_VPointInter, L: TopOpeBRep_LineInter) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    @staticmethod
    def ProcessEdgeTransition(P: TopOpeBRep_VPointInter, Index: int, LineOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    @staticmethod
    def ProcessFaceTransition(L: TopOpeBRep_LineInter, Index: int, FaceOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition: ...

    @staticmethod
    def ProcessEdgeONTransition(VP: TopOpeBRep_VPointInter, Index: int, R: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Transition:
        """
        compute transition on "IntPatch_Restriction line" edge <R>
        when crossing edge <E> of face <F> at point <VP>.
        VP is given on edge <E> of face <F> of index <Index> (1 or 2).
        <VP> has been classified by FacesFiller as TopAbs_ON an edge <R>
        of the other face than <F> of current (face/face) intersection.
        Transition depends on the orientation of E in F.
        This method should be provided by IntPatch_Line (NYI)
        """

class TopOpeBRep_GeomTool:
    """Provide services needed by the DSFiller"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_GeomTool) -> None: ...

    @staticmethod
    def MakeCurves(min: float, max: float, L: TopOpeBRep_LineInter, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Curve) -> tuple[nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve]:
        """
        Make the DS curve <C> and the pcurves <PC1,PC2> from
        intersection line <L> lying on shapes <S1,S2>. <min,max> = <L> bounds
        """

    @staticmethod
    def MakeCurve(min: float, max: float, L: TopOpeBRep_LineInter) -> nanoocp.Geom.Geom_Curve: ...

    @staticmethod
    def MakeBSpline1fromWALKING3d(L: TopOpeBRep_LineInter) -> nanoocp.Geom.Geom_Curve: ...

    @staticmethod
    def MakeBSpline1fromWALKING2d(L: TopOpeBRep_LineInter, SI: int) -> nanoocp.Geom2d.Geom2d_Curve: ...

class TopOpeBRep_Hctxee2d(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_Hctxee2d) -> None: ...

    def SetEdges(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, BAS1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, BAS2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> None: ...

    def Edge(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Curve(self, I: int) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve: ...

    def Domain(self, I: int) -> nanoocp.IntRes2d.IntRes2d_Domain: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRep_Hctxff2d(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_Hctxff2d) -> None: ...

    def SetFaces(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def SetHSurfaces(self, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None) -> None: ...

    def SetTolerances(self, Tol1: float, Tol2: float) -> None: ...

    def GetTolerances(self) -> tuple[float, float]: ...

    def GetMaxTolerance(self) -> float: ...

    def Face(self, I: int) -> nanoocp.TopoDS.TopoDS_Face: ...

    def HSurface(self, I: int) -> nanoocp.BRepAdaptor.BRepAdaptor_Surface: ...

    def SurfacesSameOriented(self) -> bool: ...

    def FacesSameOriented(self) -> bool: ...

    def FaceSameOrientedWithRef(self, I: int) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRep_PointGeomTool:
    """Provide services needed by the Fillers"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_PointGeomTool) -> None: ...

    @overload
    @staticmethod
    def MakePoint(IP: TopOpeBRep_VPointInter) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point: ...

    @overload
    @staticmethod
    def MakePoint(P2D: TopOpeBRep_Point2d) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point: ...

    @overload
    @staticmethod
    def MakePoint(FEI: TopOpeBRep_FaceEdgeIntersector) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point: ...

    @overload
    @staticmethod
    def MakePoint(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point: ...

    @staticmethod
    def IsEqual(DSP1: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point, DSP2: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Point) -> bool: ...

class TopOpeBRep_VPointInterClassifier:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_VPointInterClassifier) -> None: ...

    def VPointPosition(self, F: nanoocp.TopoDS.TopoDS_Shape, VP: TopOpeBRep_VPointInter, ShapeIndex: int, PC: TopOpeBRep_PointClassifier, AssumeINON: bool, Tol: float) -> nanoocp.TopAbs.TopAbs_State:
        """
        compute position of VPoint <VP> regarding with face <F>.
        <ShapeIndex> (= 1,2) indicates which (u,v) point of <VP> is used.
        when state is ON, set VP.EdgeON() with the edge containing <VP>
        and associated parameter.
        returns state of VP on ShapeIndex.
        """

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns the edge containing the VPoint <VP> used in the
        last VPointPosition() call. Edge is defined if the state previously
        computed is ON, else Edge is a null shape.
        """

    def EdgeParameter(self) -> float:
        """returns the parameter of the VPoint <VP> on Edge()"""

class TopOpeBRep_VPointInterIterator:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LI: TopOpeBRep_LineInter) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_VPointInterIterator) -> None: ...

    @overload
    def Init(self, LI: TopOpeBRep_LineInter, checkkeep: bool = False) -> None: ...

    @overload
    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentVP(self) -> TopOpeBRep_VPointInter: ...

    def CurrentVPIndex(self) -> int: ...

    def ChangeCurrentVP(self) -> TopOpeBRep_VPointInter: ...

    def PLineInterDummy(self) -> TopOpeBRep_LineInter: ...

class TopOpeBRep_WPointInterIterator:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LI: TopOpeBRep_LineInter) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRep_WPointInterIterator) -> None: ...

    @overload
    def Init(self, LI: TopOpeBRep_LineInter) -> None: ...

    @overload
    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentWP(self) -> TopOpeBRep_WPointInter: ...

    def PLineInterDummy(self) -> TopOpeBRep_LineInter: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopOpeBRep
import nanoocp.TopTools
TopOpeBRep_Array1OfLineInter = nanoocp.NCollection.NCollection_Array1[nanoocp.TopOpeBRep.TopOpeBRep_LineInter]
TopOpeBRep_HArray1OfLineInter = nanoocp.NCollection.NCollection_HArray1[nanoocp.TopOpeBRep.TopOpeBRep_LineInter]
TopOpeBRep_SequenceOfPoint2d = nanoocp.NCollection.NCollection_Sequence[nanoocp.TopOpeBRep.TopOpeBRep_Point2d]
