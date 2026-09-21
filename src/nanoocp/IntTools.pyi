"""OCCT package IntTools (toolkit TKBO)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BRepAdaptor
import nanoocp.BRepClass3d
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Geom2dHatch
import nanoocp.GeomAPI
import nanoocp.GeomAbs
import nanoocp.GeomAdaptor
import nanoocp.GeomInt
import nanoocp.IntPatch
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class IntTools_Root:
    """
    The class is to describe the root of
    function of one variable for Edge/Edge
    and Edge/Surface algorithms.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, aRoot: float, aType: int) -> None:
        """
        Initializes my by range of parameters
        and type of root
        """

    @overload
    def __init__(self, theOther: IntTools_Root) -> None: ...

    def SetRoot(self, aRoot: float) -> None:
        """Sets the Root's value"""

    def SetType(self, aType: int) -> None:
        """Sets the Root's Type"""

    def SetStateBefore(self, aState: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Set the value of the state before the root
        (at t=Root-dt)
        """

    def SetStateAfter(self, aState: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Set the value of the state after the root
        (at t=Root-dt)
        """

    def SetLayerHeight(self, aHeight: float) -> None:
        """Not used in Edge/Edge algorithm"""

    def SetInterval(self, t1: float, t2: float, f1: float, f2: float) -> None:
        """
        Sets the interval from which the Root was
        found [t1,t2] and the corresponding values
        of the function on the bounds f(t1), f(t2).
        """

    def Root(self) -> float:
        """Returns the Root value"""

    def Type(self) -> int:
        """
        Returns the type of the root
        =0 - Simple (was found by bisection method);
        =2 - Smart when f1=0, f2!=0 or vice versa
        (was found by Fibbonacci method);
        =1 - Pure (pure zero for all t [t1,t2]);
        """

    def StateBefore(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the state before the root"""

    def StateAfter(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the state after the root"""

    def LayerHeight(self) -> float:
        """Not used in Edge/Edge algorithm"""

    def IsValid(self) -> bool:
        """
        Returns the validity flag for the root,
        True if
        myStateBefore==TopAbs_OUT && myStateAfter==TopAbs_IN or
        myStateBefore==TopAbs_OUT && myStateAfter==TopAbs_ON or
        myStateBefore==TopAbs_ON  && myStateAfter==TopAbs_OUT or
        myStateBefore==TopAbs_IN  && myStateAfter==TopAbs_OUT
        For other cases it returns False.
        """

    def Interval(self) -> tuple[float, float, float, float]:
        """
        Returns the values of interval from which the Root was
        found [t1,t2] and the corresponding values
        of the function on the bounds f(t1), f(t2).
        """

class IntTools:
    """
    Contains classes for intersection and classification purposes and accompanying classes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntTools) -> None: ...

    @staticmethod
    def Length(E: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """returns the length of the edge;"""

    @staticmethod
    def RemoveIdenticalRoots(aSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Root], anEpsT: float) -> None:
        """
        Remove from the sequence aSeq the Roots that have
        values ti and tj such as |ti-tj] < anEpsT.
        """

    @staticmethod
    def SortRoots(aSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Root], anEpsT: float) -> None:
        """
        Sort the sequence aSeq of the Roots to arrange the Roots in increasing order.
        """

    @staticmethod
    def FindRootStates(aSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Root], anEpsNull: float) -> None:
        """
        Find the states (before and after) for each Root from the sequence aSeq
        """

    @staticmethod
    def Parameter(P: nanoocp.gp.gp_Pnt, Curve: nanoocp.Geom.Geom_Curve | None) -> tuple[int, float]: ...

    @staticmethod
    def GetRadius(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, t1: float, t3: float) -> tuple[int, float]: ...

    @staticmethod
    def PrepareArgs(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, tMax: float, tMin: float, Discret: int, Deflect: float, anArgs: nanoocp.NCollection.NCollection_Array1[float]) -> int: ...

class IntTools_BaseRangeSample:
    """base class for range index management"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theDepth: int) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_BaseRangeSample) -> None: ...

    def SetDepth(self, theDepth: int) -> None: ...

    def GetDepth(self) -> int: ...

class IntTools_MarkedRangeSet:
    """
    class MarkedRangeSet provides continuous set of ranges marked with flags
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theSortedArray: nanoocp.NCollection.NCollection_Array1[float], theInitFlag: int) -> None:
        """
        Build set of ranges based on the array of progressive sorted values

        Warning:
        The constructor do not check if the values of array are not sorted
        It should be checked before function invocation
        """

    @overload
    def __init__(self, theFirstBoundary: float, theLastBoundary: float, theInitFlag: int) -> None:
        """
        build set of ranges which consists of one range with
        boundary values theFirstBoundary and theLastBoundary
        """

    @overload
    def __init__(self, theOther: IntTools_MarkedRangeSet) -> None: ...

    def SetBoundaries(self, theFirstBoundary: float, theLastBoundary: float, theInitFlag: int) -> None:
        """
        build set of ranges which consists of one range with
        boundary values theFirstBoundary and theLastBoundary
        """

    def SetRanges(self, theSortedArray: nanoocp.NCollection.NCollection_Array1[float], theInitFlag: int) -> None:
        """
        Build set of ranges based on the array of progressive sorted values

        Warning:
        The function do not check if the values of array are not sorted
        It should be checked before function invocation
        """

    @overload
    def InsertRange(self, theFirstBoundary: float, theLastBoundary: float, theFlag: int) -> bool: ...

    @overload
    def InsertRange(self, theRange: IntTools_Range, theFlag: int) -> bool:
        """
        Inserts a new range marked with flag theFlag
        It replace the existing ranges or parts of ranges
        and their flags.
        Returns True if the range is inside the initial boundaries,
        otherwise or in case of some error returns False
        """

    @overload
    def InsertRange(self, theFirstBoundary: float, theLastBoundary: float, theFlag: int, theIndex: int) -> bool: ...

    @overload
    def InsertRange(self, theRange: IntTools_Range, theFlag: int, theIndex: int) -> bool:
        """
        Inserts a new range marked with flag theFlag
        It replace the existing ranges or parts of ranges
        and their flags.
        The index theIndex is a position where the range will be inserted.
        Returns True if the range is inside the initial boundaries,
        otherwise or in case of some error returns False
        """

    def SetFlag(self, theIndex: int, theFlag: int) -> None:
        """Set flag theFlag for range with index theIndex"""

    def Flag(self, theIndex: int) -> int:
        """Returns flag of the range with index theIndex"""

    @overload
    def GetIndex(self, theValue: float) -> int:
        """
        Returns index of range which contains theValue.
        If theValue do not belong any range returns 0.
        """

    @overload
    def GetIndex(self, theValue: float, UseLower: bool) -> int:
        """
        Returns index of range which contains theValue
        If theValue do not belong any range returns 0.
        If UseLower is true then lower boundary of the range
        can be equal to theValue, otherwise upper boundary of the range
        can be equal to theValue.
        """

    def GetIndices(self, theValue: float) -> nanoocp.NCollection.NCollection_Sequence[int]: ...

    def Length(self) -> int:
        """Returns number of ranges"""

    def Range(self, theIndex: int) -> IntTools_Range:
        """
        Returns the range with index theIndex.
        the Index can be from 1 to Length()
        """

class IntTools_Range:
    """
    The class describes the 1-d range
    [myFirst, myLast].
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, aFirst: float, aLast: float) -> None:
        """Initialize me by range boundaries"""

    @overload
    def __init__(self, theOther: IntTools_Range) -> None: ...

    def SetFirst(self, aFirst: float) -> None:
        """Modifier"""

    def SetLast(self, aLast: float) -> None:
        """Modifier"""

    def First(self) -> float:
        """Selector"""

    def Last(self) -> float:
        """Selector"""

    def Range(self) -> tuple[float, float]:
        """Selector"""

class IntTools_CurveRangeSample(IntTools_BaseRangeSample):
    """class for range index management of curve"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_CurveRangeSample) -> None: ...

    def SetRangeIndex(self, theIndex: int) -> None: ...

    def GetRangeIndex(self) -> int: ...

    def IsEqual(self, Other: IntTools_CurveRangeSample) -> bool: ...

    def __eq__(self, Other: IntTools_CurveRangeSample) -> bool: ...

    def GetRange(self, theFirst: float, theLast: float, theNbSample: int) -> IntTools_Range: ...

    def GetRangeIndexDeeper(self, theNbSample: int) -> int: ...

    def __hash__(self) -> int: ...

class IntTools_SurfaceRangeSample:
    """class for range index management of surface"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Other: IntTools_SurfaceRangeSample) -> None: ...

    @overload
    def __init__(self, theRangeU: IntTools_CurveRangeSample, theRangeV: IntTools_CurveRangeSample) -> None: ...

    @overload
    def __init__(self, theIndexU: int, theDepthU: int, theIndexV: int, theDepthV: int) -> None: ...

    def Assign(self, Other: IntTools_SurfaceRangeSample) -> IntTools_SurfaceRangeSample: ...

    def SetRanges(self, theRangeU: IntTools_CurveRangeSample, theRangeV: IntTools_CurveRangeSample) -> None: ...

    def GetRanges(self, theRangeU: IntTools_CurveRangeSample, theRangeV: IntTools_CurveRangeSample) -> None: ...

    def SetIndexes(self, theIndexU: int, theIndexV: int) -> None: ...

    def GetIndexes(self) -> tuple[int, int]: ...

    def GetDepths(self) -> tuple[int, int]: ...

    def SetSampleRangeU(self, theRangeSampleU: IntTools_CurveRangeSample) -> None: ...

    def GetSampleRangeU(self) -> IntTools_CurveRangeSample: ...

    def SetSampleRangeV(self, theRangeSampleV: IntTools_CurveRangeSample) -> None: ...

    def GetSampleRangeV(self) -> IntTools_CurveRangeSample: ...

    def SetIndexU(self, theIndexU: int) -> None: ...

    def GetIndexU(self) -> int: ...

    def SetIndexV(self, theIndexV: int) -> None: ...

    def GetIndexV(self) -> int: ...

    def SetDepthU(self, theDepthU: int) -> None: ...

    def GetDepthU(self) -> int: ...

    def SetDepthV(self, theDepthV: int) -> None: ...

    def GetDepthV(self) -> int: ...

    def GetRangeU(self, theFirstU: float, theLastU: float, theNbSampleU: int) -> IntTools_Range: ...

    def GetRangeV(self, theFirstV: float, theLastV: float, theNbSampleV: int) -> IntTools_Range: ...

    def IsEqual(self, Other: IntTools_SurfaceRangeSample) -> bool: ...

    def GetRangeIndexUDeeper(self, theNbSampleU: int) -> int: ...

    def GetRangeIndexVDeeper(self, theNbSampleV: int) -> int: ...

    def __eq__(self, theOther: IntTools_SurfaceRangeSample) -> bool: ...

class IntTools_BeanFaceIntersector:
    """
    The class BeanFaceIntersector computes ranges of parameters on
    the curve of a bean(part of edge) that bound the parts of bean which
    are on the surface of a face according to edge and face tolerances.
    Warning: The real boundaries of the face are not taken into account,
    Most of the result parts of the bean lays only inside the region of the surface,
    which includes the inside of the face. And the parts which are out of this region can be
    excluded from the result.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Initializes the algorithm

        Warning:
        The parts of the edge which are on
        the surface of the face and belong to
        the whole in the face (if there is)
        is considered as result
        """

    @overload
    def __init__(self, theCurve: nanoocp.BRepAdaptor.BRepAdaptor_Curve, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface, theBeanTolerance: float, theFaceTolerance: float) -> None:
        """Initializes the algorithm"""

    @overload
    def __init__(self, theCurve: nanoocp.BRepAdaptor.BRepAdaptor_Curve, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface, theFirstParOnCurve: float, theLastParOnCurve: float, theUMinParameter: float, theUMaxParameter: float, theVMinParameter: float, theVMaxParameter: float, theBeanTolerance: float, theFaceTolerance: float) -> None:
        """
        Initializes the algorithm
        theUMinParameter, ... are used for
        optimization purposes
        """

    @overload
    def Init(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Initializes the algorithm

        Warning:
        The parts of the edge which are on
        the surface of the face and belong to
        the whole in the face (if there is)
        is considered as result
        """

    @overload
    def Init(self, theCurve: nanoocp.BRepAdaptor.BRepAdaptor_Curve, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface, theBeanTolerance: float, theFaceTolerance: float) -> None:
        """Initializes the algorithm"""

    @overload
    def Init(self, theCurve: nanoocp.BRepAdaptor.BRepAdaptor_Curve, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface, theFirstParOnCurve: float, theLastParOnCurve: float, theUMinParameter: float, theUMaxParameter: float, theVMinParameter: float, theVMaxParameter: float, theBeanTolerance: float, theFaceTolerance: float) -> None:
        """
        Initializes the algorithm
        theUMinParameter, ... are used for
        optimization purposes
        """

    def SetContext(self, theContext: IntTools_Context | None) -> None:
        """Sets the intersection context"""

    def Context(self) -> IntTools_Context:
        """Gets the intersection context"""

    def SetBeanParameters(self, theFirstParOnCurve: float, theLastParOnCurve: float) -> None:
        """Set restrictions for curve"""

    def SetSurfaceParameters(self, theUMinParameter: float, theUMaxParameter: float, theVMinParameter: float, theVMaxParameter: float) -> None:
        """Set restrictions for surface"""

    def Perform(self) -> None:
        """Launches the algorithm"""

    def IsDone(self) -> bool:
        """Returns Done/NotDone state of the algorithm."""

    @overload
    def Result(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Range]: ...

    @overload
    def Result(self, theResults: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Range]) -> None: ...

    def MinimalSquareDistance(self) -> float:
        """Returns the minimal distance found between edge and face"""

class IntTools_CommonPrt:
    """
    The class is to describe a common part
    between two edges in 3D space.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, aCPrt: IntTools_CommonPrt) -> None:
        """Copy constructor"""

    def Assign(self, Other: IntTools_CommonPrt) -> IntTools_CommonPrt: ...

    def SetEdge1(self, anE: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Sets the first edge."""

    def SetEdge2(self, anE: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Sets the second edge."""

    def SetType(self, aType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        Sets the type of the common part
        Vertex or Edge
        """

    @overload
    def SetRange1(self, aR: IntTools_Range) -> None: ...

    @overload
    def SetRange1(self, tf: float, tl: float) -> None:
        """Sets the range of first edge."""

    @overload
    def AppendRange2(self, aR: IntTools_Range) -> None: ...

    @overload
    def AppendRange2(self, tf: float, tl: float) -> None:
        """Appends the range of second edge."""

    def SetVertexParameter1(self, tV: float) -> None:
        """Sets a parameter of first vertex"""

    def SetVertexParameter2(self, tV: float) -> None:
        """Sets a parameter of second vertex"""

    def Edge1(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the first edge."""

    def Edge2(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the second edge"""

    def Type(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Returns the type of the common part"""

    def Range1(self) -> IntTools_Range:
        """Returns the range of first edge"""

    def Range1__float__float(self) -> tuple[float, float]:
        """
        Range1__float__float: the C++ overload Range1(double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the range of first edge.
        """

    def Ranges2(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Range]:
        """Returns the ranges of second edge."""

    def ChangeRanges2(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Range]:
        """Returns the ranges of second edge."""

    def VertexParameter1(self) -> float:
        """Returns parameter of first vertex"""

    def VertexParameter2(self) -> float:
        """Returns parameter of second vertex"""

    def Copy(self, anOther: IntTools_CommonPrt) -> None:
        """Copies me to anOther"""

    def AllNullFlag(self) -> bool:
        """Modifier"""

    def SetAllNullFlag(self, aFlag: bool) -> None:
        """Selector"""

    def SetBoundingPoints(self, aP1: nanoocp.gp.gp_Pnt, aP2: nanoocp.gp.gp_Pnt) -> None:
        """Modifier"""

    def BoundingPoints(self, aP1: nanoocp.gp.gp_Pnt, aP2: nanoocp.gp.gp_Pnt) -> None:
        """Selector"""

class IntTools_Context(nanoocp.Standard.Standard_Transient):
    """
    The intersection Context contains geometrical
    and topological toolkit (classifiers, projectors, etc).
    The intersection Context is for caching the tools
    to increase the performance.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_Context) -> None: ...

    def FClass2d(self, aF: nanoocp.TopoDS.TopoDS_Face) -> IntTools_FClass2d:
        """
        Returns a reference to point classifier
        for given face
        """

    def ProjPS(self, aF: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAPI.GeomAPI_ProjectPointOnSurf:
        """
        Returns a reference to point projector
        for given face
        """

    def ProjPC(self, aE: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.GeomAPI.GeomAPI_ProjectPointOnCurve:
        """
        Returns a reference to point projector
        for given edge
        """

    def ProjPT(self, aC: nanoocp.Geom.Geom_Curve | None) -> nanoocp.GeomAPI.GeomAPI_ProjectPointOnCurve:
        """
        Returns a reference to point projector
        for given curve
        """

    def SurfaceData(self, aF: nanoocp.TopoDS.TopoDS_Face) -> IntTools_SurfaceRangeLocalizeData:
        """
        Returns a reference to surface localization data
        for given face
        """

    def SolidClassifier(self, aSolid: nanoocp.TopoDS.TopoDS_Solid) -> nanoocp.BRepClass3d.BRepClass3d_SolidClassifier:
        """
        Returns a reference to solid classifier
        for given solid
        """

    def Hatcher(self, aF: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.Geom2dHatch.Geom2dHatch_Hatcher:
        """
        Returns a reference to 2D hatcher
        for given face
        """

    def SurfaceAdaptor(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.BRepAdaptor.BRepAdaptor_Surface:
        """Returns a reference to surface adaptor for given face"""

    def OBB(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theFuzzyValue: float = 1e-07) -> nanoocp.Bnd.Bnd_OBB:
        """
        Builds and stores an Oriented Bounding Box for the shape.
        Returns a reference to OBB.
        """

    def UVBounds(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[float, float, float, float]:
        """Computes the boundaries of the face using surface adaptor"""

    def ComputePE(self, theP: nanoocp.gp.gp_Pnt, theTolP: float, theE: nanoocp.TopoDS.TopoDS_Edge) -> tuple[int, float, float]:
        """
        Computes parameter of the Point theP on
        the edge aE.
        Returns zero if the distance between point
        and edge is less than sum of tolerance value of edge and theTopP,
        otherwise and for following conditions returns
        negative value
        1. the edge is degenerated (-1)
        2. the edge does not contain 3d curve and pcurves (-2)
        3. projection algorithm failed (-3)
        """

    def ComputeVE(self, theV: nanoocp.TopoDS.TopoDS_Vertex, theE: nanoocp.TopoDS.TopoDS_Edge, theFuzz: float = 1e-07) -> tuple[int, float, float]:
        """
        Computes parameter of the vertex aV on
        the edge aE and correct tolerance value for
        the vertex on the edge.
        Returns zero if the distance between vertex
        and edge is less than sum of tolerances and the fuzzy value,
        otherwise and for following conditions returns
        negative value:
        1. the edge is degenerated (-1)
        2. the edge does not contain 3d curve and pcurves (-2)
        3. projection algorithm failed (-3)
        """

    def ComputeVF(self, theVertex: nanoocp.TopoDS.TopoDS_Vertex, theFace: nanoocp.TopoDS.TopoDS_Face, theFuzz: float = 1e-07) -> tuple[int, float, float, float]:
        """
        Computes UV parameters of the vertex aV on face aF
        and correct tolerance value for the vertex on the face.
        Returns zero if the distance between vertex and face is
        less than or equal the sum of tolerances and the fuzzy value
        and the projection point lays inside boundaries of the face.
        For following conditions returns negative value
        1. projection algorithm failed (-1)
        2. distance is more than sum of tolerances (-2)
        3. projection point out or on the boundaries of face (-3)
        """

    def StatePointFace(self, aF: nanoocp.TopoDS.TopoDS_Face, aP2D: nanoocp.gp.gp_Pnt2d) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the state of the point aP2D
        relative to face aF
        """

    @overload
    def IsPointInFace(self, aF: nanoocp.TopoDS.TopoDS_Face, aP2D: nanoocp.gp.gp_Pnt2d) -> bool: ...

    @overload
    def IsPointInFace(self, aP3D: nanoocp.gp.gp_Pnt, aF: nanoocp.TopoDS.TopoDS_Face, aTol: float) -> bool:
        """
        Returns true if the point aP2D is
        inside the boundaries of the face aF,
        otherwise returns false
        """

    def IsPointInOnFace(self, aF: nanoocp.TopoDS.TopoDS_Face, aP2D: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Returns true if the point aP2D is
        inside or on the boundaries of aF
        """

    def IsValidPointForFace(self, aP3D: nanoocp.gp.gp_Pnt, aF: nanoocp.TopoDS.TopoDS_Face, aTol: float) -> bool:
        """
        Returns true if the distance between point aP3D
        and face aF is less or equal to tolerance aTol
        and projection point is inside or on the boundaries
        of the face aF
        """

    def IsValidPointForFaces(self, aP3D: nanoocp.gp.gp_Pnt, aF1: nanoocp.TopoDS.TopoDS_Face, aF2: nanoocp.TopoDS.TopoDS_Face, aTol: float) -> bool:
        """
        Returns true if IsValidPointForFace returns true
        for both face aF1 and aF2
        """

    def IsValidBlockForFace(self, aT1: float, aT2: float, aIC: IntTools_Curve, aF: nanoocp.TopoDS.TopoDS_Face, aTol: float) -> bool:
        """
        Returns true if IsValidPointForFace returns true
        for some 3d point that lay on the curve aIC bounded by
        parameters aT1 and aT2
        """

    def IsValidBlockForFaces(self, aT1: float, aT2: float, aIC: IntTools_Curve, aF1: nanoocp.TopoDS.TopoDS_Face, aF2: nanoocp.TopoDS.TopoDS_Face, aTol: float) -> bool:
        """
        Returns true if IsValidBlockForFace returns true
        for both faces aF1 and aF2
        """

    @overload
    def IsVertexOnLine(self, aV: nanoocp.TopoDS.TopoDS_Vertex, aIC: IntTools_Curve, aTolC: float) -> tuple[bool, float]: ...

    @overload
    def IsVertexOnLine(self, aV: nanoocp.TopoDS.TopoDS_Vertex, aTolV: float, aIC: IntTools_Curve, aTolC: float) -> tuple[bool, float]:
        """
        Computes parameter of the vertex aV on
        the curve aIC.
        Returns true if the distance between vertex and
        curve is less than sum of tolerance of aV and aTolC,
        otherwise or if projection algorithm failed
        returns false (in this case aT isn't significant)
        """

    def ProjectPointOnEdge(self, aP: nanoocp.gp.gp_Pnt, aE: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]:
        """
        Computes parameter of the point aP on
        the edge aE.
        Returns false if projection algorithm failed
        other wiese returns true.
        """

    def BndBox(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Bnd.Bnd_Box: ...

    def IsInfiniteFace(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Returns true if the solid <theFace> has
        infinite bounds
        """

    def SetPOnSProjectionTolerance(self, theValue: float) -> None:
        """
        Sets tolerance to be used for projection of point on surface.
        Clears map of already cached projectors in order to maintain
        correct value for all projectors
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntTools_Curve:
    """
    The class is a container of one 3D curve, two 2D curves and two Tolerance values.
    It is used in the Face/Face intersection algorithm to store the results
    of intersection. In this context:
    **the 3D curve** is the intersection curve;
    **the 2D curves** are the PCurves of the 3D curve on the intersecting faces;
    **the tolerance** is the valid tolerance for 3D curve computed as
    maximal deviation between 3D curve and 2D curves (or surfaces in case there are no 2D
    curves);
    **the tangential tolerance** is the maximal distance from 3D curve to the
    end of the tangential zone between faces in terms of their tolerance values.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, the3dCurve3d: nanoocp.Geom.Geom_Curve | None, the2dCurve1: nanoocp.Geom2d.Geom2d_Curve | None, the2dCurve2: nanoocp.Geom2d.Geom2d_Curve | None, theTolerance: float = 0.0, theTangentialTolerance: float = 0.0) -> None:
        """Constructor taking 3d curve, two 2d curves and two tolerance values"""

    @overload
    def __init__(self, theOther: IntTools_Curve) -> None: ...

    def SetCurves(self, the3dCurve: nanoocp.Geom.Geom_Curve | None, the2dCurve1: nanoocp.Geom2d.Geom2d_Curve | None, the2dCurve2: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """Sets the curves"""

    def SetCurve(self, the3dCurve: nanoocp.Geom.Geom_Curve | None) -> None:
        """Sets the 3d curve"""

    def SetFirstCurve2d(self, the2dCurve1: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """Sets the first 2d curve"""

    def SetSecondCurve2d(self, the2dCurve2: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """Sets the second 2d curve"""

    def SetTolerance(self, theTolerance: float) -> None:
        """Sets the tolerance for the curve"""

    def SetTangentialTolerance(self, theTangentialTolerance: float) -> None:
        """Sets the tangential tolerance"""

    def Curve(self) -> nanoocp.Geom.Geom_Curve:
        """Returns 3d curve"""

    def FirstCurve2d(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns first 2d curve"""

    def SecondCurve2d(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns second 2d curve"""

    def Tolerance(self) -> float:
        """Returns the tolerance"""

    def TangentialTolerance(self) -> float:
        """Returns the tangential tolerance"""

    def HasBounds(self) -> bool:
        """Returns TRUE if 3d curve is BoundedCurve"""

    def Bounds(self, theFirstPnt: nanoocp.gp.gp_Pnt, theLastPnt: nanoocp.gp.gp_Pnt) -> tuple[bool, float, float]:
        """
        If the 3d curve is bounded curve the method will return TRUE
        and modify the output parameters with boundary parameters of
        the curve and corresponded 3d points.
        If the curve does not have bounds, the method will return false
        and the output parameters will stay untouched.
        """

    def D0(self, thePar: float, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """
        Computes 3d point corresponded to the given parameter if this
        parameter is inside the boundaries of the curve.
        Returns TRUE in this case.
        Otherwise, the point will not be computed and the method will return FALSE.
        """

    def Type(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """Returns the type of the 3d curve"""

class IntTools_CurveRangeLocalizeData:
    @overload
    def __init__(self, theNbSample: int, theMinRange: float) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_CurveRangeLocalizeData) -> None: ...

    def GetNbSample(self) -> int: ...

    def GetMinRange(self) -> float: ...

    def AddOutRange(self, theRange: IntTools_CurveRangeSample) -> None: ...

    def AddBox(self, theRange: IntTools_CurveRangeSample, theBox: nanoocp.Bnd.Bnd_Box) -> None: ...

    def FindBox(self, theRange: IntTools_CurveRangeSample, theBox: nanoocp.Bnd.Bnd_Box) -> bool: ...

    def IsRangeOut(self, theRange: IntTools_CurveRangeSample) -> bool: ...

    def ListRangeOut(self, theList: nanoocp.NCollection.NCollection_List[nanoocp.IntTools.IntTools_CurveRangeSample]) -> None: ...

class IntTools_EdgeEdge:
    """
    The class provides Edge/Edge intersection algorithm
    based on the intersection between edges bounding boxes.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    @overload
    def __init__(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, aT11: float, aT12: float, theEdge2: nanoocp.TopoDS.TopoDS_Edge, aT21: float, aT22: float) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: IntTools_EdgeEdge) -> None: ...

    @overload
    def SetEdge1(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Sets the first edge"""

    @overload
    def SetEdge1(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, aT1: float, aT2: float) -> None:
        """Sets the first edge and its range"""

    @overload
    def SetRange1(self, theRange1: IntTools_Range) -> None: ...

    @overload
    def SetRange1(self, aT1: float, aT2: float) -> None:
        """Sets the range for the first edge"""

    @overload
    def SetEdge2(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Sets the second edge"""

    @overload
    def SetEdge2(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, aT1: float, aT2: float) -> None:
        """Sets the first edge and its range"""

    @overload
    def SetRange2(self, theRange: IntTools_Range) -> None: ...

    @overload
    def SetRange2(self, aT1: float, aT2: float) -> None:
        """Sets the range for the second edge"""

    def SetFuzzyValue(self, theFuzz: float) -> None:
        """Sets the Fuzzy value"""

    def Perform(self) -> None:
        """Performs the intersection between edges"""

    def IsDone(self) -> bool:
        """Returns TRUE if common part(s) is(are) found"""

    def FuzzyValue(self) -> float:
        """Returns Fuzzy value"""

    def CommonParts(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_CommonPrt]:
        """Returns common parts"""

    def UseQuickCoincidenceCheck(self, bFlag: bool) -> None:
        """Sets the flag myQuickCoincidenceCheck"""

    def IsCoincidenceCheckedQuickly(self) -> bool:
        """Returns the flag myQuickCoincidenceCheck"""

class IntTools_EdgeFace:
    """
    The class provides Edge/Face intersection algorithm to determine
    common parts between edge and face in 3-d space.
    Common parts between Edge and Face can be:
    - Vertices - in case of intersection or touching;
    - Edge - in case of full coincidence of the edge with the face.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty Constructor
        """

    @overload
    def __init__(self, theOther: IntTools_EdgeFace) -> None: ...

    def SetEdge(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        @name Setters/Getters
        Sets the edge for intersection
        """

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the edge"""

    def SetFace(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Sets the face for intersection"""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the face"""

    @overload
    def SetRange(self, theRange: IntTools_Range) -> None: ...

    @overload
    def SetRange(self, theFirst: float, theLast: float) -> None:
        """
        Sets the boundaries for the edge.
        The algorithm processes edge inside these boundaries.
        """

    def Range(self) -> IntTools_Range:
        """Returns intersection range of the edge"""

    def SetContext(self, theContext: IntTools_Context | None) -> None:
        """Sets the intersection context"""

    def Context(self) -> IntTools_Context:
        """Returns the intersection context"""

    def SetFuzzyValue(self, theFuzz: float) -> None:
        """Sets the Fuzzy value"""

    def FuzzyValue(self) -> float:
        """Returns the Fuzzy value"""

    def UseQuickCoincidenceCheck(self, theFlag: bool) -> None:
        """
        Sets the flag for quick coincidence check.
        It is safe to use the quick check for coincidence only if both
        of the following conditions are met:
        - The vertices of edge are lying on the face;
        - The edge does not intersect the boundaries of the face on the given range.
        """

    def IsCoincidenceCheckedQuickly(self) -> bool:
        """Returns the flag myQuickCoincidenceCheck"""

    def Perform(self) -> None:
        """
        @name Performing the operation
        Launches the process
        """

    def IsDone(self) -> bool:
        """
        @name Checking validity of the intersection
        Returns TRUE if computation was successful.
        Otherwise returns FALSE.
        """

    def ErrorStatus(self) -> int:
        """
        Returns the code of completion:
        0 - means successful completion;
        1 - the process was not started;
        2,3 - invalid source data for the algorithm;
        4 - projection failed.
        """

    def CommonParts(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_CommonPrt]:
        """
        @name Obtaining results
        Returns resulting common parts
        """

    def MinimalDistance(self) -> float:
        """Returns the minimal distance found between edge and face"""

class IntTools_PntOnFace:
    """Contains a Face, a 3d point, corresponded UV parameters and a flag"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: IntTools_PntOnFace) -> None: ...

    def Init(self, aF: nanoocp.TopoDS.TopoDS_Face, aP: nanoocp.gp.gp_Pnt, U: float, V: float) -> None:
        """
        Initializes me by aFace, a 3d point
        and it's UV parameters on face
        """

    def SetFace(self, aF: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Modifier"""

    def SetPnt(self, aP: nanoocp.gp.gp_Pnt) -> None:
        """Modifier"""

    def SetParameters(self, U: float, V: float) -> None:
        """Modifier"""

    def SetValid(self, bF: bool) -> None:
        """Modifier"""

    def Valid(self) -> bool:
        """Selector"""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Selector"""

    def Pnt(self) -> nanoocp.gp.gp_Pnt:
        """Selector"""

    def Parameters(self) -> tuple[float, float]:
        """Selector"""

class IntTools_PntOn2Faces:
    """Contains two points PntOnFace from IntTools and a flag"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, aP1: IntTools_PntOnFace, aP2: IntTools_PntOnFace) -> None:
        """Initializes me by two points aP1 and aP2"""

    @overload
    def __init__(self, theOther: IntTools_PntOn2Faces) -> None: ...

    def SetP1(self, aP1: IntTools_PntOnFace) -> None:
        """Modifier"""

    def SetP2(self, aP2: IntTools_PntOnFace) -> None:
        """Modifier"""

    def SetValid(self, bF: bool) -> None:
        """Modifier"""

    def P1(self) -> IntTools_PntOnFace:
        """Selector"""

    def P2(self) -> IntTools_PntOnFace:
        """Selector"""

    def IsValid(self) -> bool:
        """Selector"""

class IntTools_FaceFace:
    """
    This class provides the intersection of
    face's underlying surfaces.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: IntTools_FaceFace) -> None: ...

    def SetParameters(self, ApproxCurves: bool, ComputeCurveOnS1: bool, ComputeCurveOnS2: bool, ApproximationTolerance: float) -> None:
        """Modifier"""

    def Perform(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, theToRunParallel: bool = False) -> None:
        """
        Intersects underliing surfaces of F1 and F2
        Use sum of tolerance of F1 and F2 as intersection
        criteria
        """

    def IsDone(self) -> bool:
        """Returns True if the intersection was successful"""

    def Lines(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Curve]:
        """Returns sequence of 3d curves as result of intersection"""

    def Points(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_PntOn2Faces]:
        """Returns sequence of 3d curves as result of intersection"""

    def Face1(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns first of processed faces"""

    def Face2(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns second of processed faces"""

    def TangentFaces(self) -> bool:
        """Returns True if faces are tangent"""

    def PrepareLines3D(self, bToSplit: bool = True) -> None:
        """
        Provides post-processing the result lines.
        @param[in] bToSplit  split the closed 3D-curves on parts when TRUE,
        remain untouched otherwise
        """

    def SetList(self, ListOfPnts: nanoocp.NCollection.NCollection_List[nanoocp.IntSurf.IntSurf_PntOn2S]) -> None: ...

    def SetContext(self, aContext: IntTools_Context | None) -> None:
        """Sets the intersection context"""

    def SetFuzzyValue(self, theFuzz: float) -> None:
        """Sets the Fuzzy value"""

    def FuzzyValue(self) -> float:
        """Returns Fuzzy value"""

    def Context(self) -> IntTools_Context:
        """Gets the intersection context"""

class IntTools_FClass2d:
    """
    Class provides an algorithm to classify a 2d Point
    in 2d space of face using boundaries of the face.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None:
        """
        Initializes algorithm by the face F
        and tolerance Tol
        """

    def Init(self, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None:
        """
        Initializes algorithm by the face F
        and tolerance Tol
        """

    def PerformInfinitePoint(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns state of infinite 2d point relatively to (0, 0)"""

    def Perform(self, Puv: nanoocp.gp.gp_Pnt2d, RecadreOnPeriodic: bool = True) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns state of the 2d point Puv.
        If RecadreOnPeriodic is true (default value),
        for the periodic surface 2d point, adjusted to period, is
        classified.
        """

    def TestOnRestriction(self, Puv: nanoocp.gp.gp_Pnt2d, Tol: float, RecadreOnPeriodic: bool = True) -> nanoocp.TopAbs.TopAbs_State:
        """
        Test a point with +- an offset (Tol) and returns
        On if some points are OUT an some are IN
        (Caution: Internal use. see the code for more details)
        """

    def IsHole(self) -> bool: ...

class IntTools_ShrunkRange:
    """
    The class provides the computation of
    a working (shrunk) range [t1, t2] for
    the 3D-curve of the edge.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_ShrunkRange) -> None: ...

    def SetData(self, aE: nanoocp.TopoDS.TopoDS_Edge, aT1: float, aT2: float, aV1: nanoocp.TopoDS.TopoDS_Vertex, aV2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def SetContext(self, aCtx: IntTools_Context | None) -> None: ...

    def Context(self) -> IntTools_Context: ...

    def SetShrunkRange(self, aT1: float, aT2: float) -> None: ...

    def ShrunkRange(self) -> tuple[float, float]: ...

    def BndBox(self) -> nanoocp.Bnd.Bnd_Box: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Perform(self) -> None: ...

    def IsDone(self) -> bool:
        """Returns TRUE in case the shrunk range is computed"""

    def IsSplittable(self) -> bool:
        """
        Returns FALSE in case the shrunk range is
        too short and the edge cannot be split,
        otherwise returns TRUE
        """

    def Length(self) -> float:
        """Returns the length of the edge if computed."""

class IntTools_SurfaceRangeLocalizeData:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Other: IntTools_SurfaceRangeLocalizeData) -> None: ...

    @overload
    def __init__(self, theNbSampleU: int, theNbSampleV: int, theMinRangeU: float, theMinRangeV: float) -> None: ...

    def Assign(self, Other: IntTools_SurfaceRangeLocalizeData) -> IntTools_SurfaceRangeLocalizeData: ...

    def GetNbSampleU(self) -> int: ...

    def GetNbSampleV(self) -> int: ...

    def GetMinRangeU(self) -> float: ...

    def GetMinRangeV(self) -> float: ...

    def AddOutRange(self, theRange: IntTools_SurfaceRangeSample) -> None: ...

    def AddBox(self, theRange: IntTools_SurfaceRangeSample, theBox: nanoocp.Bnd.Bnd_Box) -> None: ...

    def FindBox(self, theRange: IntTools_SurfaceRangeSample, theBox: nanoocp.Bnd.Bnd_Box) -> bool: ...

    def IsRangeOut(self, theRange: IntTools_SurfaceRangeSample) -> bool: ...

    def ListRangeOut(self, theList: nanoocp.NCollection.NCollection_List[nanoocp.IntTools.IntTools_SurfaceRangeSample]) -> None: ...

    def RemoveRangeOutAll(self) -> None: ...

    def SetGridDeflection(self, theDeflection: float) -> None:
        """Set the grid deflection."""

    def GetGridDeflection(self) -> float:
        """Query the grid deflection."""

    def SetRangeUGrid(self, theNbUGrid: int) -> None:
        """Set the range U of the grid of points."""

    def GetRangeUGrid(self) -> int:
        """Query the range U of the grid of points."""

    def SetUParam(self, theIndex: int, theUParam: float) -> None:
        """Set the U parameter of the grid points at that index."""

    def GetUParam(self, theIndex: int) -> float:
        """Query the U parameter of the grid points at that index."""

    def SetRangeVGrid(self, theNbVGrid: int) -> None:
        """Set the range V of the grid of points."""

    def GetRangeVGrid(self) -> int:
        """Query the range V of the grid of points."""

    def SetVParam(self, theIndex: int, theVParam: float) -> None:
        """Set the V parameter of the grid points at that index."""

    def GetVParam(self, theIndex: int) -> float:
        """Query the V parameter of the grid points at that index."""

    def SetGridPoint(self, theUIndex: int, theVIndex: int, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """Set the grid point."""

    def GetGridPoint(self, theUIndex: int, theVIndex: int) -> nanoocp.gp.gp_Pnt:
        """Set the grid point."""

    def SetFrame(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float) -> None:
        """Sets the frame area. Used to work with grid points."""

    def GetNBUPointsInFrame(self) -> int:
        """Returns the number of grid points on U direction in frame."""

    def GetNBVPointsInFrame(self) -> int:
        """Returns the number of grid points on V direction in frame."""

    def GetPointInFrame(self, theUIndex: int, theVIndex: int) -> nanoocp.gp.gp_Pnt:
        """Returns the grid point in frame."""

    def GetUParamInFrame(self, theIndex: int) -> float:
        """
        Query the U parameter of the grid points
        at that index in frame.
        """

    def GetVParamInFrame(self, theIndex: int) -> float:
        """
        Query the V parameter of the grid points
        at that index in frame.
        """

    def ClearGrid(self) -> None:
        """Clears the grid of points."""

class IntTools_Tools:
    """
    The class contains handy static functions
    dealing with the geometry and topology.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_Tools) -> None: ...

    @staticmethod
    def ComputeVV(V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> int:
        """
        Computes distance between vertex V1 and vertex V2,
        if the distance is less than sum of vertex tolerances
        returns zero,
        otherwise returns negative value
        """

    @staticmethod
    def HasInternalEdge(aW: nanoocp.TopoDS.TopoDS_Wire) -> bool:
        """
        Returns True if wire aW contains edges
        with INTERNAL orientation
        """

    @staticmethod
    def MakeFaceFromWireAndFace(aW: nanoocp.TopoDS.TopoDS_Wire, aF: nanoocp.TopoDS.TopoDS_Face, aFNew: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Build a face based on surface of given face aF
        and bounded by wire aW
        """

    @staticmethod
    def ClassifyPointByFace(aF: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt2d) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    @staticmethod
    def IsVertex(E: nanoocp.TopoDS.TopoDS_Edge, t: float) -> bool:
        """
        Computes square distance between a point on the edge E
        corresponded to parameter t and vertices of edge E.
        Returns True if this distance is less than square
        tolerance of vertex, otherwise returns false.
        """

    @overload
    @staticmethod
    def IsVertex(E: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex, t: float) -> bool:
        """
        Returns True if square distance between vertex V
        and a point on the edge E corresponded to parameter t
        is less than square tolerance of V
        """

    @overload
    @staticmethod
    def IsVertex(aCmnPrt: IntTools_CommonPrt) -> bool:
        """
        Returns True if IsVertx for middle parameter of fist range
        and first edge returns True
        and if IsVertex for middle parameter of second range and
        second range returns True,
        otherwise returns False
        """

    @overload
    @staticmethod
    def IsVertex(aP: nanoocp.gp.gp_Pnt, aTolPV: float, aV: nanoocp.TopoDS.TopoDS_Vertex) -> bool:
        """
        Returns True if the distance between point aP and
        vertex aV is less or equal to sum of aTolPV and
        vertex tolerance, otherwise returns False
        """

    @staticmethod
    def IsMiddlePointsEqual(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Gets boundary of parameters of E1 and E2.
        Computes 3d points on each corresponded to average parameters.
        Returns True if distance between computed points is less than
        sum of edge tolerance, otherwise returns False.
        """

    @staticmethod
    def IntermediatePoint(aFirst: float, aLast: float) -> float:
        """Returns some value between aFirst and aLast"""

    @staticmethod
    def SplitCurve(aC: IntTools_Curve, aS: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Curve]) -> int:
        """
        Split aC by average parameter if aC is closed in 3D.
        Returns positive value if splitting has been done,
        otherwise returns zero.
        """

    @staticmethod
    def RejectLines(aSIn: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Curve], aSOut: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Curve]) -> None:
        """
        Puts curves from aSIn to aSOut except those curves that
        are coincide with first curve from aSIn.
        """

    @overload
    @staticmethod
    def IsDirsCoinside(D1: nanoocp.gp.gp_Dir, D2: nanoocp.gp.gp_Dir) -> bool:
        """Returns True if D1 and D2 coincide"""

    @overload
    @staticmethod
    def IsDirsCoinside(D1: nanoocp.gp.gp_Dir, D2: nanoocp.gp.gp_Dir, aTol: float) -> bool:
        """Returns True if D1 and D2 coincide with given tolerance"""

    @staticmethod
    def IsClosed(aC: nanoocp.Geom.Geom_Curve | None) -> bool:
        """
        Returns True if aC is BoundedCurve from Geom and
        the distance between first point
        of the curve aC and last point
        is less than 1.e-12
        """

    @staticmethod
    def CurveTolerance(aC: nanoocp.Geom.Geom_Curve | None, aTolBase: float) -> float:
        """
        Returns adaptive tolerance for given aTolBase
        if aC is trimmed curve and basis curve is parabola,
        otherwise returns value of aTolBase
        """

    @staticmethod
    def CheckCurve(theCurve: IntTools_Curve, theBox: nanoocp.Bnd.Bnd_Box) -> bool:
        """
        Checks if the curve is not covered by the default tolerance (confusion).
        Builds bounding box for the curve and stores it into <theBox>.
        """

    @staticmethod
    def IsOnPave(theT: float, theRange: IntTools_Range, theTol: float) -> bool: ...

    @staticmethod
    def VertexParameters(theCP: IntTools_CommonPrt) -> tuple[float, float]: ...

    @staticmethod
    def VertexParameter(theCP: IntTools_CommonPrt) -> float: ...

    @staticmethod
    def IsOnPave1(theT: float, theRange: IntTools_Range, theTol: float) -> bool: ...

    @staticmethod
    def IsInRange(theRRef: IntTools_Range, theR: IntTools_Range, theTol: float) -> bool:
        """Checks if the range <theR> interfere with the range <theRRef>"""

    @staticmethod
    def SegPln(theLin: nanoocp.gp.gp_Lin, theTLin1: float, theTLin2: float, theTolLin: float, thePln: nanoocp.gp.gp_Pln, theTolPln: float, theP: nanoocp.gp.gp_Pnt) -> tuple[int, float, float, float, float]: ...

    @staticmethod
    def ComputeTolerance(theCurve3D: nanoocp.Geom.Geom_Curve | None, theCurve2D: nanoocp.Geom2d.Geom2d_Curve | None, theSurf: nanoocp.Geom.Geom_Surface | None, theFirst: float, theLast: float, theTolRange: float = 1e-09, theToRunParallel: bool = False) -> tuple[bool, float, float]:
        """
        Computes the max distance between points
        taken from 3D and 2D curves by the same parameter
        """

    @staticmethod
    def ComputeIntRange(theTol1: float, theTol2: float, theAngle: float) -> float:
        """
        Computes the correct Intersection range for
        Line/Line, Line/Plane and Plane/Plane intersections
        """

class IntTools_TopolTool(nanoocp.Adaptor3d.Adaptor3d_TopolTool):
    """
    Class redefine methods of TopolTool from Adaptor3d
    concerning sample points
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
        """Initializes me by surface"""

    @overload
    def __init__(self, theOther: IntTools_TopolTool) -> None: ...

    @overload
    def Initialize(self) -> None:
        """
        Redefined empty initializer

        Warning:
        Raises the exception NotImplemented
        """

    @overload
    def Initialize(self, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
        """Initializes me by surface"""

    def ComputeSamplePoints(self) -> None: ...

    def NbSamplesU(self) -> int:
        """Computes the sample-points for the intersections algorithms"""

    def NbSamplesV(self) -> int:
        """Computes the sample-points for the intersections algorithms"""

    def NbSamples(self) -> int:
        """Computes the sample-points for the intersections algorithms"""

    def SamplePoint(self, Index: int, P2d: nanoocp.gp.gp_Pnt2d, P3d: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns a 2d point from surface myS
        and a corresponded 3d point
        for given index.
        The index should be from 1 to NbSamples()
        """

    def SamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None:
        """
        compute the sample-points for the intersections algorithms
        by adaptive algorithm for BSpline surfaces. For other surfaces algorithm
        is the same as in method ComputeSamplePoints(), but only fill arrays of U
        and V sample parameters;
        theDefl is a required deflection
        theNUmin, theNVmin are minimal nb points for U and V.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntTools_WLineTool:
    """
    IntTools_WLineTool provides set of static methods related to walking lines.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntTools_WLineTool) -> None: ...

    @staticmethod
    def NotUseSurfacesForApprox(aF1: nanoocp.TopoDS.TopoDS_Face, aF2: nanoocp.TopoDS.TopoDS_Face, WL: nanoocp.IntPatch.IntPatch_WLine | None, ifprm: int, ilprm: int) -> bool: ...

    @staticmethod
    def DecompositionOfWLine(theWLine: nanoocp.IntPatch.IntPatch_WLine | None, theSurface1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, theSurface2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, theFace1: nanoocp.TopoDS.TopoDS_Face, theFace2: nanoocp.TopoDS.TopoDS_Face, theLConstructor: nanoocp.GeomInt.GeomInt_LineConstructor, theAvoidLConstructor: bool, theTol: float, theNewLines: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line], arg9: IntTools_Context | None) -> bool: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IntSurf
import nanoocp.IntTools
IntTools_ListOfCurveRangeSample = nanoocp.NCollection.NCollection_List[nanoocp.IntTools.IntTools_CurveRangeSample]
IntTools_ListOfSurfaceRangeSample = nanoocp.NCollection.NCollection_List[nanoocp.IntTools.IntTools_SurfaceRangeSample]
IntTools_SequenceOfCommonPrts = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_CommonPrt]
IntTools_SequenceOfCurves = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Curve]
IntTools_SequenceOfPntOn2Faces = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_PntOn2Faces]
IntTools_SequenceOfRanges = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Range]
IntTools_SequenceOfRoots = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntTools.IntTools_Root]
