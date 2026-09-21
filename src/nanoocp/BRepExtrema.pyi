"""OCCT package BRepExtrema (toolkit TKTopAlgo)"""

import enum
from typing import overload

import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.Extrema
import nanoocp.IntPatch
from nanoocp.IntPatch import (
    BVH_PairTraverse__double__3__void__double as BVH_PairTraverse__double__3__void__double
)
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp


class BRepExtrema_SupportType(enum.IntEnum):
    BRepExtrema_IsVertex = 0

    BRepExtrema_IsOnEdge = 1

    BRepExtrema_IsInFace = 2

BRepExtrema_IsVertex: BRepExtrema_SupportType = BRepExtrema_SupportType.BRepExtrema_IsVertex

BRepExtrema_IsOnEdge: BRepExtrema_SupportType = BRepExtrema_SupportType.BRepExtrema_IsOnEdge

BRepExtrema_IsInFace: BRepExtrema_SupportType = BRepExtrema_SupportType.BRepExtrema_IsInFace

class BRepExtrema_SolutionElem:
    """
    This class is used to store information relative to the minimum distance between two shapes.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theDist: float, thePoint: nanoocp.gp.gp_Pnt, theSolType: BRepExtrema_SupportType, theVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        This constructor is used when the solution of a distance is a Vertex.
        The different initialized fields are:
        @param theDist    the distance
        @param thePoint   the solution point
        @param theSolType the type of solution
        @param theVertex  and the Vertex
        """

    @overload
    def __init__(self, theDist: float, thePoint: nanoocp.gp.gp_Pnt, theSolType: BRepExtrema_SupportType, theEdge: nanoocp.TopoDS.TopoDS_Edge, theParam: float) -> None:
        """
        This constructor is used when the solution of distance is on an Edge.
        The different initialized fields are:
        @param theDist    the distance
        @param thePoint   the solution point
        @param theSolType the type of solution
        @param theEdge    the Edge
        @param theParam   the parameter to locate the solution
        """

    @overload
    def __init__(self, theDist: float, thePoint: nanoocp.gp.gp_Pnt, theSolType: BRepExtrema_SupportType, theFace: nanoocp.TopoDS.TopoDS_Face, theU: float, theV: float) -> None:
        """
        This constructor is used when the solution of distance is in a Face.
        The different initialized fields are:
        @param theDist    the distance
        @param thePoint   the solution point
        @param theSolType the type of solution
        @param theFace    the Face
        @param theU       U parameter to locate the solution
        @param theV       V parameter to locate the solution
        """

    @overload
    def __init__(self, theOther: BRepExtrema_SolutionElem) -> None: ...

    def Dist(self) -> float:
        """Returns the value of the minimum distance."""

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """Returns the solution point."""

    def SupportKind(self) -> BRepExtrema_SupportType:
        """
        Returns the Support type:
        IsVertex => The solution is a vertex.
        IsOnEdge => The solution belongs to an Edge.
        IsInFace => The solution is inside a Face.
        """

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the vertex if the solution is a Vertex."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the vertex if the solution is an Edge."""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the vertex if the solution is an Face."""

    def EdgeParameter(self) -> float:
        """Returns the parameter value if the solution is on Edge."""

    def FaceParameter(self) -> tuple[float, float]:
        """Returns the parameters U and V if the solution is in a Face."""

class BRepExtrema_DistanceSS:
    """
    This class allows to compute minimum distance between two brep shapes
    (face edge vertex) and is used in DistShapeShape class.
    """

    @overload
    def __init__(self, theS1: nanoocp.TopoDS.TopoDS_Shape, theS2: nanoocp.TopoDS.TopoDS_Shape, theBox1: nanoocp.Bnd.Bnd_Box, theBox2: nanoocp.Bnd.Bnd_Box, theDstRef: float, theDeflection: float = 1e-07, theExtFlag: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, theExtAlgo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        @name Constructor from two shapes
        Computes the distance between two Shapes (face edge vertex).
        @param theS1 - First shape
        @param theS2 - Second shape
        @param theBox1 - Bounding box of first shape
        @param theBox2 - Bounding box of second shape
        @param theDstRef - Initial distance between the shapes to start with
        @param theDeflection - Maximum deviation of extreme distances from the minimum
        one (default is Precision::Confusion()).
        @param theExtFlag - Specifies which extrema solutions to look for
        (default is MINMAX, applied only to point-face extrema)
        @param theExtAlgo - Specifies which extrema algorithm is to be used
        (default is Grad algo, applied only to point-face extrema)
        """

    @overload
    def __init__(self, theOther: BRepExtrema_DistanceSS) -> None: ...

    def IsDone(self) -> bool:
        """
        @name Results
        Returns true if the distance has been computed, false otherwise.
        """

    def DistValue(self) -> float:
        """Returns the distance value."""

    def Seq1Value(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.BRepExtrema.BRepExtrema_SolutionElem]:
        """Returns the list of solutions on the first shape."""

    def Seq2Value(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.BRepExtrema.BRepExtrema_SolutionElem]:
        """Returns the list of solutions on the second shape."""

class BRepExtrema_DistShapeShape:
    """
    This class provides tools to compute minimum distance
    between two Shapes (Compound,CompSolid, Solid, Shell, Face, Wire, Edge, Vertex).
    """

    @overload
    def __init__(self) -> None:
        """create empty tool"""

    @overload
    def __init__(self, Shape1: nanoocp.TopoDS.TopoDS_Shape, Shape2: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, A: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        create tool and computation of the minimum distance (value and pair of points)
        using default deflection in single thread mode.
        Default deflection value is Precision::Confusion().
        @param Shape1 - the first shape for distance computation
        @param Shape2 - the second shape for distance computation
        @param F and @param A are not used in computation and are obsolete.
        @param theRange - the progress indicator of algorithm
        """

    @overload
    def __init__(self, Shape1: nanoocp.TopoDS.TopoDS_Shape, Shape2: nanoocp.TopoDS.TopoDS_Shape, theDeflection: float, F: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, A: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        create tool and computation of the minimum distance
        (value and pair of points) in single thread mode.
        Default deflection value is Precision::Confusion().
        @param Shape1 - the first shape for distance computation
        @param Shape2 - the second shape for distance computation
        @param theDeflection - the presition of distance computation
        @param F and @param A are not used in computation and are obsolete.
        @param theRange - the progress indicator of algorithm
        """

    @overload
    def __init__(self, theOther: BRepExtrema_DistShapeShape) -> None: ...

    def SetDeflection(self, theDeflection: float) -> None:
        """Sets deflection to computation of the minimum distance"""

    def LoadS1(self, Shape1: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """load first shape into extrema"""

    def LoadS2(self, Shape1: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """load second shape into extrema"""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        computation of the minimum distance (value and
        couple of points). Parameter theDeflection is used
        to specify a maximum deviation of extreme distances
        from the minimum one.
        Returns IsDone status.
        theRange - the progress indicator of algorithm
        """

    def IsDone(self) -> bool:
        """True if the minimum distance is found."""

    def NbSolution(self) -> int:
        """Returns the number of solutions satisfying the minimum distance."""

    def Value(self) -> float:
        """Returns the value of the minimum distance."""

    def InnerSolution(self) -> bool:
        """
        True if one of the shapes is a solid and the other shape
        is completely or partially inside the solid.
        """

    def PointOnShape1(self, N: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the Point corresponding to the <N>th solution on the first Shape
        """

    def PointOnShape2(self, N: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the Point corresponding to the <N>th solution on the second Shape
        """

    def SupportTypeShape1(self, N: int) -> BRepExtrema_SupportType:
        """
        gives the type of the support where the Nth solution on the first shape is situated:
        IsVertex => the Nth solution on the first shape is a Vertex
        IsOnEdge => the Nth soluion on the first shape is on a Edge
        IsInFace => the Nth solution on the first shape is inside a face
        the corresponding support is obtained by the method SupportOnShape1
        """

    def SupportTypeShape2(self, N: int) -> BRepExtrema_SupportType:
        """
        gives the type of the support where the Nth solution on the second shape is situated:
        IsVertex => the Nth solution on the second shape is a Vertex
        IsOnEdge => the Nth soluion on the secondt shape is on a Edge
        IsInFace => the Nth solution on the second shape is inside a face
        the corresponding support is obtained by the method SupportOnShape2
        """

    def SupportOnShape1(self, N: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        gives the support where the Nth solution on the first shape is situated.
        This support can be a Vertex, an Edge or a Face.
        """

    def SupportOnShape2(self, N: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        gives the support where the Nth solution on the second shape is situated.
        This support can be a Vertex, an Edge or a Face.
        """

    def ParOnEdgeS1(self, N: int) -> float:
        """
        gives the corresponding parameter t if the Nth solution
        is situated on an Edge of the first shape
        """

    def ParOnEdgeS2(self, N: int) -> float:
        """
        gives the corresponding parameter t if the Nth solution
        is situated on an Edge of the first shape
        """

    def ParOnFaceS1(self, N: int) -> tuple[float, float]:
        """
        gives the corresponding parameters (U,V) if the Nth solution
        is situated on an face of the first shape
        """

    def ParOnFaceS2(self, N: int) -> tuple[float, float]:
        """
        gives the corresponding parameters (U,V) if the Nth solution
        is situated on an Face of the second shape
        """

    def Dump(self) -> object:
        """Prints on the stream o information on the current state of the object."""

    def SetFlag(self, F: nanoocp.Extrema.Extrema_ExtFlag) -> None:
        """
        Sets unused parameter
        Obsolete
        """

    def SetAlgo(self, A: nanoocp.Extrema.Extrema_ExtAlgo) -> None:
        """
        Sets unused parameter
        Obsolete
        """

    def SetMultiThread(self, theIsMultiThread: bool) -> None:
        """
        If isMultiThread == true then computation will be performed in parallel.
        """

    def IsMultiThread(self) -> bool:
        """
        Returns true then computation will be performed in parallel
        Default value is false
        """

class BRepExtrema_ElementFilter:
    """
    Filtering tool used to detect if two given mesh elements
    should be tested for overlapping/intersection or not.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepExtrema_ElementFilter) -> None: ...

    class FilterResult(enum.IntEnum):
        """Result of filtering function."""

        NoCheck = 0

        Overlap = 1

        DoCheck = 2

    NoCheck: BRepExtrema_ElementFilter.FilterResult = FilterResult.NoCheck

    Overlap: BRepExtrema_ElementFilter.FilterResult = FilterResult.Overlap

    DoCheck: BRepExtrema_ElementFilter.FilterResult = FilterResult.DoCheck

    def PreCheckElements(self, arg0: int, arg1: int) -> BRepExtrema_ElementFilter.FilterResult:
        """
        Checks if two mesh elements should be tested for overlapping/intersection
        (used for detection correct/incorrect cases of shared edges and vertices).
        """

class BRepExtrema_ExtCC:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """It calculates all the distances."""

    def Initialize(self, E2: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def Perform(self, E1: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """An exception is raised if the fields have not been initialized."""

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def IsParallel(self) -> bool:
        """Returns True if E1 and E2 are parallel."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the <N>th extremum square distance."""

    def ParameterOnE1(self, N: int) -> float:
        """
        Returns the parameter on the first edge of the <N>th extremum distance.
        """

    def PointOnE1(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance on the edge E1."""

    def ParameterOnE2(self, N: int) -> float:
        """
        Returns the parameter on the second edge of the <N>th extremum distance.
        """

    def PointOnE2(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance on the edge E2."""

    def TrimmedSquareDistances(self, P11: nanoocp.gp.gp_Pnt, P12: nanoocp.gp.gp_Pnt, P21: nanoocp.gp.gp_Pnt, P22: nanoocp.gp.gp_Pnt) -> tuple[float, float, float, float]:
        """
        if the edges is a trimmed curve,
        dist11 is a square distance between the point on E1
        of parameter FirstParameter and the point of
        parameter FirstParameter on E2.
        """

class BRepExtrema_ExtCF:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """It calculates all the distances."""

    def Initialize(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def Perform(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        An exception is raised if the fields have not been initialized.
        Be careful: this method uses the Face only for classify not for the fields.
        """

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the <N>th extremum square distance."""

    def IsParallel(self) -> bool:
        """Returns True if the curve is on a parallel surface."""

    def ParameterOnEdge(self, N: int) -> float:
        """Returns the parameters on the Edge of the <N>th extremum distance."""

    def ParameterOnFace(self, N: int) -> tuple[float, float]:
        """Returns the parameters on the Face of the <N>th extremum distance."""

    def PointOnEdge(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance."""

    def PointOnFace(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance."""

class BRepExtrema_ExtFF:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None:
        """It calculates all the distances."""

    @overload
    def __init__(self, theOther: BRepExtrema_ExtFF) -> None: ...

    def Initialize(self, F2: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def Perform(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        An exception is raised if the fields have not been initialized.
        Be careful: this method uses the Face F2 only for classify, not for the fields.
        """

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the surfaces are parallel."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the <N>th extremum square distance."""

    def ParameterOnFace1(self, N: int) -> tuple[float, float]:
        """Returns the parameters on the Face F1 of the <N>th extremum distance."""

    def ParameterOnFace2(self, N: int) -> tuple[float, float]:
        """Returns the parameters on the Face F2 of the <N>th extremum distance."""

    def PointOnFace1(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance."""

    def PointOnFace2(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance."""

class BRepExtrema_ExtPC:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """It calculates all the distances."""

    @overload
    def __init__(self, theOther: BRepExtrema_ExtPC) -> None: ...

    def Initialize(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def Perform(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """An exception is raised if the fields have not been initialized."""

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def IsMin(self, N: int) -> bool:
        """Returns True if the <N>th extremum distance is a minimum."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the <N>th extremum square distance."""

    def Parameter(self, N: int) -> float:
        """Returns the parameter on the edge of the <N>th extremum distance."""

    def Point(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance."""

    def TrimmedSquareDistances(self, pnt1: nanoocp.gp.gp_Pnt, pnt2: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        if the curve is a trimmed curve,
        dist1 is a square distance between <P> and the point
        of parameter FirstParameter <pnt1> and
        dist2 is a square distance between <P> and the point
        of parameter LastParameter <pnt2>.
        """

class BRepExtrema_ExtPF:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, TheVertex: nanoocp.TopoDS.TopoDS_Vertex, TheFace: nanoocp.TopoDS.TopoDS_Face, TheFlag: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, TheAlgo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """It calculates all the distances."""

    def Initialize(self, TheFace: nanoocp.TopoDS.TopoDS_Face, TheFlag: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, TheAlgo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    def Perform(self, TheVertex: nanoocp.TopoDS.TopoDS_Vertex, TheFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        An exception is raised if the fields have not been initialized.
        Be careful: this method uses the Face only for classify not for the fields.
        """

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the <N>th extremum square distance."""

    def Parameter(self, N: int) -> tuple[float, float]:
        """Returns the parameters on the Face of the <N>th extremum distance."""

    def Point(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the Point of the <N>th extremum distance."""

    def SetFlag(self, F: nanoocp.Extrema.Extrema_ExtFlag) -> None: ...

    def SetAlgo(self, A: nanoocp.Extrema.Extrema_ExtAlgo) -> None: ...

class BRepExtrema_TriangleSet(nanoocp.BVH.BVH_PrimitiveSet3d):
    """Triangle set corresponding to specific face."""

    @overload
    def __init__(self) -> None:
        """Creates empty triangle set."""

    @overload
    def __init__(self, theFaces: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Creates triangle set from the given face."""

    @overload
    def __init__(self, theOther: BRepExtrema_TriangleSet) -> None: ...

    def Size(self) -> int:
        """
        @name methods implementing BVH set interface
        Returns total number of triangles.
        """

    @overload
    def Box(self, theIndex: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns AABB of the given triangle."""

    @overload
    def Box(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns AABB of primitive set."""

    def Center(self, theIndex: int, theAxis: int) -> float:
        """Returns centroid position along specified axis."""

    def Swap(self, theIndex1: int, theIndex2: int) -> None:
        """Swaps indices of two specified triangles."""

    def Clear(self) -> None:
        """Clears triangle set data."""

    def Init(self, theShapes: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """Initializes triangle set."""

    @overload
    def GetVertices(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec3d]:
        """Returns all vertices."""

    @overload
    def GetVertices(self, theIndex: int, theVertex1: nanoocp.BVH.BVH_Vec3d, theVertex2: nanoocp.BVH.BVH_Vec3d, theVertex3: nanoocp.BVH.BVH_Vec3d) -> None:
        """Returns vertices of the given triangle."""

    def GetVtxIndices(self, theIndex: int, theVtxIndices: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """Returns vertex indices of the given triangle."""

    def GetFaceID(self, theIndex: int) -> int:
        """Returns face ID of the given triangle."""

    def GetShapeIDOfVtx(self, theIndex: int) -> int:
        """Returns shape ID of the given vertex index."""

    def GetVtxIdxInShape(self, theIndex: int) -> int:
        """
        Returns vertex index in tringulation of the shape, which vertex belongs,
        with the given vtx ID in whole set.
        """

    def GetTrgIdxInShape(self, theIndex: int) -> int:
        """
        Returns triangle index (before swapping) in tringulation of the shape, which triangle belongs,
        with the given trg ID in whole set (after swapping).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepExtrema_OverlapTool(nanoocp.IntPatch.BVH_PairTraverse__double__3__void__double):
    """
    Tool class for for detection of overlapping of two BVH primitive sets.
    This tool is not intended to be used independently, and is integrated
    in other classes, implementing algorithms based on shape tessellation
    (BRepExtrema_ShapeProximity and BRepExtrema_SelfIntersection).

    Note that input element sets may correspond to different shapes or to
    the same shape. In first case, tessellations of two given shapes will
    be tested for intersection (or overlapping, if tolerance is not zero).
    In second case, tessellation of single shape will be tested for self-
    intersections. Please note that algorithm results are approximate and
    depend greatly on the quality of input tessellation(s).
    """

    @overload
    def __init__(self) -> None:
        """Creates new uninitialized overlap tool."""

    @overload
    def __init__(self, theSet1: BRepExtrema_TriangleSet | None, theSet2: BRepExtrema_TriangleSet | None) -> None:
        """Creates new overlap tool for the given element sets."""

    @overload
    def __init__(self, theOther: BRepExtrema_OverlapTool) -> None: ...

    def LoadTriangleSets(self, theSet1: BRepExtrema_TriangleSet | None, theSet2: BRepExtrema_TriangleSet | None) -> None:
        """Loads the given element sets into the overlap tool."""

    def Perform(self, theTolerance: float = 0.0) -> None:
        """Performs searching of overlapped mesh elements."""

    def IsDone(self) -> bool:
        """Is overlap test completed?"""

    def MarkDirty(self) -> None:
        """Marks test results as outdated."""

    def OverlapSubShapes1(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """
        Returns set of overlapped sub-shapes of 1st shape (currently only faces are detected).
        """

    def OverlapSubShapes2(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """
        Returns set of overlapped sub-shapes of 2nd shape (currently only faces are detected).
        """

    def SetElementFilter(self, theFilter: BRepExtrema_ElementFilter) -> None:
        """Sets filtering tool for preliminary checking pairs of mesh elements."""

    def RejectNode(self, theCornerMin1: nanoocp.BVH.BVH_Vec3d, theCornerMax1: nanoocp.BVH.BVH_Vec3d, theCornerMin2: nanoocp.BVH.BVH_Vec3d, theCornerMax2: nanoocp.BVH.BVH_Vec3d) -> tuple[bool, float]:
        """
        @name Reject/Accept implementations
        Defines the rules for node rejection by bounding box
        """

    def Accept(self, theLeaf1: int, theLeaf2: int) -> bool:
        """Defines the rules for leaf acceptance"""

class BRepExtrema_Poly:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepExtrema_Poly) -> None: ...

    @staticmethod
    def Distance(S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """returns true if OK."""

class BVH_Traverse__double__3__BRepExtrema_TriangleSet__double(nanoocp.IntPatch.BVH_BaseTraverse__double):
    """
    Abstract class implementing the traverse of the single binary tree.
    Selection of the data from the tree is performed by the
    rules defined in the Accept/Reject methods.
    See description of the required methods in the comments above.

    \\tparam NumType Numeric data type
    \\tparam Dimension Vector dimension
    \\tparam BVHSetType Type of set containing the BVH tree (required to access the elements by the
    index) \\tparam MetricType Type of metric to perform more optimal tree descend
    """

    def SetBVHSet(self, theBVHSet: BRepExtrema_TriangleSet) -> None:
        """
        @name Setting the set to access the elements and BVH tree
        Sets the BVH Set containing the BVH tree
        """

    def AcceptMetric(self, arg0: float) -> bool:
        """
        @name Rules for Accept/Reject
        Basing on the given metric, checks if the whole branch may be
        accepted without any further checks.
        Returns true if the metric is accepted, false otherwise.
        """

    def RejectNode(self, theCornerMin: nanoocp.BVH.BVH_Vec3d, theCornerMax: nanoocp.BVH.BVH_Vec3d, theMetric: float) -> bool:
        """
        Rejection of the node by bounding box.
        Metric is computed to choose the best branch.
        Returns true if the node should be rejected, false otherwise.
        """

    def Accept(self, theIndex: int, theMetric: float) -> bool:
        """
        Leaf element acceptance.
        Metric of the parent leaf-node is passed to avoid the check on the
        element and accept it unconditionally.
        Returns true if the element has been accepted, false otherwise.
        """

    @overload
    def Select(self) -> int:
        """
        @name Selection
        Selection of the elements from the BVH tree by the
        rules defined in Accept/Reject methods.
        The method requires the BVHSet containing BVH tree to be set.
        Returns the number of accepted elements.
        """

    @overload
    def Select(self, theBVH: "BVH_Tree<double, 3, BVH_BinaryTree>" | None) -> int:
        """
        Performs selection of the elements from the BVH tree by the
        rules defined in Accept/Reject methods.
        Returns the number of accepted elements.
        """

class BVH_Distance__double__3__NCollection_Vec3__double__BRepExtrema_TriangleSet(BVH_Traverse__double__3__BRepExtrema_TriangleSet__double):
    """
    Abstract class for computation of the min distance between some
    Object and elements of BVH tree.
    To use this class it is required to define two methods:
    - *RejectNode* to compute distance from the object to bounding box
    - *Accept* to compute distance from the object to the element of tree

    \\tparam NumType Numeric data type
    \\tparam Dimension Vector dimension
    \\tparam ObjectType Type of the object to which the distance is required
    \\tparam BVHSetType Type of the set on which BVH is built
    """

    def SetObject(self, theObject: nanoocp.BVH.BVH_Vec3d) -> None:
        """
        @name Setting object for distance computation
        Sets the object to which the distance is required
        """

    def ComputeDistance(self) -> float:
        """
        @name Compute the distance
        Computes the distance between object and BVH tree
        """

    def IsDone(self) -> bool:
        """
        @name Accessing the results
        Returns IsDone flag
        """

    def Distance(self) -> float:
        """Returns the computed distance"""

    def IsMetricBetter(self, theLeft: float, theRight: float) -> bool:
        """
        @name Definition of the rules for tree descend
        Compares the two metrics and chooses the best one
        """

    def RejectMetric(self, theMetric: float) -> bool:
        """Rejects the branch by the metric"""

    def Stop(self) -> bool:
        """Returns the flag controlling the tree descend"""

class BRepExtrema_ProximityDistTool(BVH_Distance__double__3__NCollection_Vec3__double__BRepExtrema_TriangleSet):
    """
    Tool class for computation the proximity distance from first
    primitive set to second one that is the maximal from minimum
    perpendicular distances. If no perpendicular distance is found, the
    minimum distance will be returned.
    This tool is not intended to be used independently, and is integrated
    in other classes, implementing algorithms based on shape tessellation
    (BRepExtrema_ProximityValueTool).

    Please note that algorithm results are approximate and depend greatly
    on the quality of input tessellation(s).
    """

    @overload
    def __init__(self) -> None:
        """Creates new uninitialized tool."""

    @overload
    def __init__(self, theSet1: BRepExtrema_TriangleSet | None, theNbSamples1: int, theAddVertices1: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec3d], theAddStatus1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepExtrema.BRepExtrema_ProximityDistTool.ProxPnt_Status], theSet2: BRepExtrema_TriangleSet | None, theShapeList1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape], theShapeList2: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Creates new tool for the given element sets."""

    @overload
    def __init__(self, theOther: BRepExtrema_ProximityDistTool) -> None: ...

    class ProxPnt_Status(enum.IntEnum):
        ProxPnt_Status_BORDER = 0

        ProxPnt_Status_MIDDLE = 1

        ProxPnt_Status_UNKNOWN = 2

    ProxPnt_Status_BORDER: BRepExtrema_ProximityDistTool.ProxPnt_Status = ProxPnt_Status.ProxPnt_Status_BORDER

    ProxPnt_Status_MIDDLE: BRepExtrema_ProximityDistTool.ProxPnt_Status = ProxPnt_Status.ProxPnt_Status_MIDDLE

    ProxPnt_Status_UNKNOWN: BRepExtrema_ProximityDistTool.ProxPnt_Status = ProxPnt_Status.ProxPnt_Status_UNKNOWN

    class PrjState:
        """
        Struct with information about projection point state from 2nd BVH,
        providing proximity point of 2nd shape
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theTrgIdx: int, thePrjState: "BVH_Tools<double, 3>::BVH_PrjStateInTriangle", theNumberOfFirstNode: int, theNumberOfLastNode: int) -> None: ...

        @overload
        def __init__(self, theOther: BRepExtrema_ProximityDistTool.PrjState) -> None: ...

        def GetTrgIdx(self) -> int: ...

        def GetPrjState(self) -> "BVH_Tools<double, 3>::BVH_PrjStateInTriangle": ...

        def GetNumberOfFirstNode(self) -> int: ...

        def GetNumberOfLastNode(self) -> int: ...

    def LoadTriangleSets(self, theSet1: BRepExtrema_TriangleSet | None, theSet2: BRepExtrema_TriangleSet | None) -> None:
        """Loads the given element sets into the tool."""

    def LoadShapeLists(self, theShapeList1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape], theShapeList2: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Loads the given list of subshapes into the tool."""

    def LoadAdditionalPointsFirstSet(self, theAddVertices1: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec3d], theAddStatus1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepExtrema.BRepExtrema_ProximityDistTool.ProxPnt_Status]) -> None:
        """Loads given additional vertices and their statuses."""

    def Perform(self) -> None:
        """Performs searching of the proximity distance."""

    def RejectNode(self, theCornerMin: nanoocp.BVH.BVH_Vec3d, theCornerMax: nanoocp.BVH.BVH_Vec3d) -> tuple[bool, float]:
        """
        @name Reject/Accept implementations
        Defines the rules for node rejection by bounding box.
        """

    def Accept(self, theSgmIdx: int, arg1: float) -> bool:
        """Defines the rules for leaf acceptance."""

    @staticmethod
    def IsNodeOnBorder(theNodeIdx: int, theTr: nanoocp.Poly.Poly_Triangulation | None) -> bool:
        """Returns true if the node is on the boarder."""

    @staticmethod
    def IsEdgeOnBorder(theTrgIdx: int, theFirstEdgeNodeIdx: int, theSecondEdgeNodeIdx: int, theTr: nanoocp.Poly.Poly_Triangulation | None) -> bool:
        """Returns true if the edge is on the boarder."""

    def ProximityPoints(self, thePoint1: nanoocp.BVH.BVH_Vec3d, thePoint2: nanoocp.BVH.BVH_Vec3d) -> None:
        """
        Returns points on triangles sets, which provide the proximity distance.
        """

    def ProximityPointsStatus(self) -> tuple[BRepExtrema_ProximityDistTool.ProxPnt_Status, BRepExtrema_ProximityDistTool.ProxPnt_Status]:
        """
        Returns status of points on triangles sets, which provide the proximity distance.
        """

    def ProximityDistance(self) -> float:
        """Returns the computed distance"""

class BRepExtrema_VertexInspector:
    """
    Inspector for CellFilter algorithm working with gp_XYZ points in 3d space.
    Used in search of coincidence points with a certain tolerance.
    """

    @overload
    def __init__(self) -> None:
        """Constructor; remembers the tolerance"""

    @overload
    def __init__(self, theOther: BRepExtrema_VertexInspector) -> None: ...

    @staticmethod
    def Coord(i: int, thePnt: nanoocp.gp.gp_XYZ) -> float: ...

    @staticmethod
    def Shift(thePnt: nanoocp.gp.gp_XYZ, theTol: float) -> nanoocp.gp.gp_XYZ: ...

    def Add(self, thePnt: nanoocp.gp.gp_XYZ) -> None:
        """Keep the points used for comparison"""

    def SetTol(self, theTol: float) -> None:
        """Set tolerance for comparison of point coordinates"""

    def SetCurrent(self, theCurPnt: nanoocp.gp.gp_XYZ) -> None:
        """Set current point to search for coincidence"""

    def IsNeedAdd(self) -> bool: ...

    def Inspect(self, theTarget: int) -> nanoocp.NCollection.NCollection_CellFilter_Action:
        """Implementation of inspection method"""

class BRepExtrema_ProximityValueTool:
    """
    Tool class for computation of the proximity value from one BVH
    primitive set to another, solving max(min) problem.
    Handles only edge/edge or face/face cases.
    This tool is not intended to be used independently, and is integrated
    in other classes, implementing algorithms based on shape tessellation
    (BRepExtrema_ShapeProximity and BRepExtrema_SelfIntersection).

    Please note that algorithm results are approximate and depend greatly
    on the quality of input tessellation(s).
    """

    @overload
    def __init__(self) -> None:
        """Creates new uninitialized proximity tool."""

    @overload
    def __init__(self, theSet1: BRepExtrema_TriangleSet | None, theSet2: BRepExtrema_TriangleSet | None, theShapeList1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape], theShapeList2: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Creates new proximity tool for the given element sets."""

    def LoadTriangleSets(self, theSet1: BRepExtrema_TriangleSet | None, theSet2: BRepExtrema_TriangleSet | None) -> None:
        """Loads the given element sets into the proximity tool."""

    def LoadShapeLists(self, theShapeList1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape], theShapeList2: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Loads the given list of subshapes into the proximity tool."""

    def SetNbSamplePoints(self, theSamples1: int = 0, theSamples2: int = 0) -> None:
        """
        Sets number of sample points used for proximity calculation for each shape.
        If number is less or equal zero, all triangulation nodes are used.
        """

    def Perform(self) -> float:
        """Performs the computation of the proximity value."""

    def IsDone(self) -> bool:
        """Is proximity test completed?"""

    def MarkDirty(self) -> None:
        """Marks test results as outdated."""

    def Distance(self) -> float:
        """Returns the computed distance."""

    def ProximityPoints(self, thePoint1: nanoocp.gp.gp_Pnt, thePoint2: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns points on triangles sets, which provide the proximity distance.
        """

    def ProximityPointsStatus(self) -> tuple[BRepExtrema_ProximityDistTool.ProxPnt_Status, BRepExtrema_ProximityDistTool.ProxPnt_Status]:
        """
        Returns status of points on triangles sets, which provide the proximity distance.
        """

class BRepExtrema_SelfIntersection(BRepExtrema_ElementFilter):
    """
    Tool class for detection of self-sections in the given shape.
    This class is based on BRepExtrema_OverlapTool and thus uses
    shape tessellation to detect incorrect mesh fragments (pairs
    of overlapped triangles belonging to different faces). Thus,
    a result depends critically on the quality of mesh generator
    (e.g., BREP mesh is not always a good choice, because it can
    contain gaps between adjacent face triangulations, which may
    not share vertices on common edge; thus false overlap can be
    detected). As a result, this tool can be used for relatively
    fast approximated test which provides sub-set of potentially
    overlapped faces.
    """

    @overload
    def __init__(self, theTolerance: float = 0.0) -> None:
        """Creates uninitialized self-intersection tool."""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theTolerance: float = 0.0) -> None:
        """Creates self-intersection tool for the given shape."""

    @overload
    def __init__(self, theOther: BRepExtrema_SelfIntersection) -> None: ...

    def Tolerance(self) -> float:
        """Returns tolerance value used for self-intersection test."""

    def SetTolerance(self, theTolerance: float) -> None:
        """Sets tolerance value used for self-intersection test."""

    def LoadShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Loads shape for detection of self-intersections."""

    def Perform(self) -> None:
        """Performs detection of self-intersections."""

    def IsDone(self) -> bool:
        """True if the detection is completed."""

    def OverlapElements(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns set of IDs of overlapped sub-shapes (started from 0)."""

    def GetSubShape(self, theID: int) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns sub-shape from the shape for the given index (started from 0)."""

    def ElementSet(self) -> BRepExtrema_TriangleSet:
        """Returns set of all the face triangles of the shape."""

class BRepExtrema_ShapeProximity:
    """
    @brief Tool class for shape proximity detection.

    First approach:
    For two given shapes and given tolerance (offset from the mesh) the algorithm allows
    to determine whether or not they are overlapped. The algorithm input consists of any
    shapes which can be decomposed into individual faces (used as basic shape elements).

    The algorithm can be run in two modes. If tolerance is set to zero, the algorithm
    will detect only intersecting faces (containing triangles with common points). If
    tolerance is set to positive value, the algorithm will also detect faces located
    on distance less than the given tolerance from each other.

    Second approach:
    Compute the proximity value between two shapes (handles only edge/edge or face/face cases)
    if the tolerance is not defined (Precision::Infinite()).
    In this case the proximity value is a minimal thickness of a layer containing both shapes.

    For the both approaches the high performance is achieved through the use of existing
    triangulation of faces. So, poly triangulation (with the desired deflection) should already
    be built. Note that solution is approximate (and corresponds to the deflection used for
    triangulation).
    """

    @overload
    def __init__(self, theTolerance: float = 2e+100) -> None:
        """Creates empty proximity tool."""

    @overload
    def __init__(self, theShape1: nanoocp.TopoDS.TopoDS_Shape, theShape2: nanoocp.TopoDS.TopoDS_Shape, theTolerance: float = 2e+100) -> None:
        """Creates proximity tool for the given two shapes."""

    def Tolerance(self) -> float:
        """Returns tolerance value for overlap test (distance between shapes)."""

    def SetTolerance(self, theTolerance: float) -> None:
        """Sets tolerance value for overlap test (distance between shapes)."""

    def Proximity(self) -> float:
        """Returns proximity value calculated for the whole input shapes."""

    def LoadShape1(self, theShape1: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Loads 1st shape into proximity tool."""

    def LoadShape2(self, theShape2: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Loads 2nd shape into proximity tool."""

    def SetNbSamples1(self, theNbSamples: int) -> None:
        """
        Set number of sample points on the 1st shape used to compute the proximity value.
        In case of 0, all triangulation nodes will be used.
        """

    def SetNbSamples2(self, theNbSamples: int) -> None:
        """
        Set number of sample points on the 2nd shape used to compute the proximity value.
        In case of 0, all triangulation nodes will be used.
        """

    def Perform(self) -> None:
        """Performs search of overlapped faces."""

    def IsDone(self) -> bool:
        """True if the search is completed."""

    def OverlapSubShapes1(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns set of IDs of overlapped faces of 1st shape (started from 0)."""

    def OverlapSubShapes2(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns set of IDs of overlapped faces of 2nd shape (started from 0)."""

    def GetSubShape1(self, theID: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns sub-shape from 1st shape with the given index (started from 0).
        """

    def GetSubShape2(self, theID: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns sub-shape from 1st shape with the given index (started from 0).
        """

    def ElementSet1(self) -> BRepExtrema_TriangleSet:
        """Returns set of all the face triangles of the 1st shape."""

    def ElementSet2(self) -> BRepExtrema_TriangleSet:
        """Returns set of all the face triangles of the 2nd shape."""

    def ProximityPoint1(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point on the 1st shape, which could be used as a reference point
        for the value of the proximity.
        """

    def ProximityPoint2(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point on the 2nd shape, which could be used as a reference point
        for the value of the proximity.
        """

    def ProxPntStatus1(self) -> BRepExtrema_ProximityDistTool.ProxPnt_Status:
        """
        Returns the status of point on the 1st shape, which could be used as a reference point
        for the value of the proximity.
        """

    def ProxPntStatus2(self) -> BRepExtrema_ProximityDistTool.ProxPnt_Status:
        """
        Returns the status of point on the 2nd shape, which could be used as a reference point
        for the value of the proximity.
        """

class BRepExtrema_UnCompatibleShape(nanoocp.Standard.Standard_DomainError):
    pass

class ProxPnt_Status(enum.IntEnum):
    ProxPnt_Status_BORDER = 0

    ProxPnt_Status_MIDDLE = 1

    ProxPnt_Status_UNKNOWN = 2

# C++ typedef aliases
VectorOfPoint = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.gp.gp_XYZ]

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BRepExtrema
import nanoocp.TColStd
BRepExtrema_SeqOfSolution = nanoocp.NCollection.NCollection_Sequence[nanoocp.BRepExtrema.BRepExtrema_SolutionElem]
