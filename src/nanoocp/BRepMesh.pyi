"""OCCT package BRepMesh (toolkit TKMesh)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BRepAdaptor
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.IMeshData
import nanoocp.IMeshTools
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.BRepMesh
import nanoocp.TColStd


class BRepMesh_DegreeOfFreedom(enum.IntEnum):
    BRepMesh_Free = 0

    BRepMesh_InVolume = 1

    BRepMesh_OnSurface = 2

    BRepMesh_OnCurve = 3

    BRepMesh_Fixed = 4

    BRepMesh_Frontier = 5

    BRepMesh_Deleted = 6

BRepMesh_Free: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_Free

BRepMesh_InVolume: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_InVolume

BRepMesh_OnSurface: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface

BRepMesh_OnCurve: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve

BRepMesh_Fixed: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_Fixed

BRepMesh_Frontier: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_Frontier

BRepMesh_Deleted: BRepMesh_DegreeOfFreedom = BRepMesh_DegreeOfFreedom.BRepMesh_Deleted

class BRepMesh_Vertex:
    """
    Light weighted structure representing vertex
    of the mesh in parametric space. Vertex could be
    associated with 3d point stored in external map.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theUV: nanoocp.gp.gp_XY, theLocation3d: int, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """
        Creates vertex associated with point in 3d space.
        @param theUV position of vertex in parametric space.
        @param theLocation3d index of 3d point to be associated with vertex.
        @param theMovability movability of the vertex.
        """

    @overload
    def __init__(self, theU: float, theV: float, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """
        Creates vertex without association with point in 3d space.
        @param theU U position of vertex in parametric space.
        @param theV V position of vertex in parametric space.
        @param theMovability movability of the vertex.
        """

    @overload
    def __init__(self, theOther: BRepMesh_Vertex) -> None: ...

    def Initialize(self, theUV: nanoocp.gp.gp_XY, theLocation3d: int, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """
        Initializes vertex associated with point in 3d space.
        @param theUV position of vertex in parametric space.
        @param theLocation3d index of 3d point to be associated with vertex.
        @param theMovability movability of the vertex.
        """

    def Coord(self) -> nanoocp.gp.gp_XY:
        """Returns position of the vertex in parametric space."""

    def ChangeCoord(self) -> nanoocp.gp.gp_XY:
        """Returns position of the vertex in parametric space for modification."""

    def Location3d(self) -> int:
        """Returns index of 3d point associated with the vertex."""

    def Movability(self) -> BRepMesh_DegreeOfFreedom:
        """Returns movability of the vertex."""

    def SetMovability(self, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """Sets movability of the vertex."""

    def IsEqual(self, theOther: BRepMesh_Vertex) -> bool:
        """
        Checks for equality with another vertex.
        @param theOther vertex to be checked against this one.
        @return TRUE if equal, FALSE if not.
        """

    def __eq__(self, Other: BRepMesh_Vertex) -> bool:
        """Alias for IsEqual."""

    def __hash__(self) -> int: ...

class BRepMesh_Circle:
    """
    Describes a 2d circle with a size of only 3 double
    numbers instead of gp who needs 7 double numbers.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theLocation: nanoocp.gp.gp_XY, theRadius: float) -> None:
        """
        Constructor.
        @param theLocation location of a circle.
        @param theRadius radius of a circle.
        """

    @overload
    def __init__(self, theOther: BRepMesh_Circle) -> None: ...

    def SetLocation(self, theLocation: nanoocp.gp.gp_XY) -> None:
        """
        Sets location of a circle.
        @param theLocation location of a circle.
        """

    def SetRadius(self, theRadius: float) -> None:
        """
        Sets radius of a circle.
        @param theRadius radius of a circle.
        """

    def Location(self) -> nanoocp.gp.gp_XY:
        """Returns location of a circle."""

    def Radius(self) -> float:
        """Returns radius of a circle."""

class BRepMesh_Triangle:
    """
    Light weighted structure representing triangle
    of mesh consisting of oriented links.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_Triangle) -> None: ...

    def Movability(self) -> BRepMesh_DegreeOfFreedom:
        """Returns movability of the triangle."""

    def SetMovability(self, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """Sets movability of the triangle."""

    def IsEqual(self, theOther: BRepMesh_Triangle) -> bool:
        """
        Checks for equality with another triangle.
        @param theOther triangle to be checked against this one.
        @return TRUE if equal, FALSE if not.
        """

    def __eq__(self, theOther: BRepMesh_Triangle) -> bool:
        """Alias for IsEqual."""

    def __hash__(self) -> int: ...

    @property
    def myMovability(self) -> BRepMesh_DegreeOfFreedom: ...

    @myMovability.setter
    def myMovability(self, arg: BRepMesh_DegreeOfFreedom, /) -> None: ...

class BRepMesh_PairOfIndex:
    """
    This class represents a pair of integer indices to store
    element indices connected to link. It is restricted to
    store more than two indices in it.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: BRepMesh_PairOfIndex) -> None: ...

    def Clear(self) -> None:
        """Clears indices."""

    def Append(self, theIndex: int) -> None:
        """Appends index to the pair."""

    def Prepend(self, theIndex: int) -> None:
        """Prepends index to the pair."""

    def IsEmpty(self) -> bool:
        """Returns is pair is empty."""

    def Extent(self) -> int:
        """Returns number of initialized indices."""

    def FirstIndex(self) -> int:
        """Returns first index of pair."""

    def LastIndex(self) -> int:
        """Returns last index of pair"""

    def Index(self, thePairPos: int) -> int:
        """
        Returns index corresponding to the given position in the pair.
        @param thePairPos position of index in the pair (1 or 2).
        """

    def SetIndex(self, thePairPos: int, theIndex: int) -> None:
        """
        Sets index corresponding to the given position in the pair.
        @param thePairPos position of index in the pair (1 or 2).
        @param theIndex index to be stored.
        """

    def RemoveIndex(self, thePairPos: int) -> None:
        """
        Remove index from the given position.
        @param thePairPos position of index in the pair (1 or 2).
        """

class BRepMesh_OrientedEdge:
    """Light weighted structure representing simple link."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theFirstNode: int, theLastNode: int) -> None:
        """Constructs a link between two vertices."""

    @overload
    def __init__(self, theOther: BRepMesh_OrientedEdge) -> None: ...

    def FirstNode(self) -> int:
        """Returns index of first node of the Link."""

    def LastNode(self) -> int:
        """Returns index of last node of the Link."""

    def IsEqual(self, theOther: BRepMesh_OrientedEdge) -> bool:
        """
        Checks this and other edge for equality.
        @param theOther edge to be checked against this one.
        @return TRUE if edges have the same orientation, FALSE if not.
        """

    def __eq__(self, Other: BRepMesh_OrientedEdge) -> bool:
        """Alias for IsEqual."""

    def __hash__(self) -> int: ...

class BRepMesh_Edge(BRepMesh_OrientedEdge):
    """Light weighted structure representing link of the mesh."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theFirstNode: int, theLastNode: int, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """Constructs a link between two vertices."""

    @overload
    def __init__(self, theOther: BRepMesh_Edge) -> None: ...

    def Movability(self) -> BRepMesh_DegreeOfFreedom:
        """Returns movability flag of the Link."""

    def SetMovability(self, theMovability: BRepMesh_DegreeOfFreedom) -> None:
        """
        Sets movability flag of the Link.
        @param theMovability flag to be set.
        """

    def IsSameOrientation(self, theOther: BRepMesh_Edge) -> bool:
        """
        Checks if the given edge and this one have the same orientation.
        @param theOther edge to be checked against this one.
        \\return TRUE if edges have the same orientation, FALSE if not.
        """

    def IsEqual(self, theOther: BRepMesh_Edge) -> bool:
        """
        Checks for equality with another edge.
        @param theOther edge to be checked against this one.
        @return TRUE if equal, FALSE if not.
        """

    def __eq__(self, Other: BRepMesh_Edge) -> bool:
        """Alias for IsEqual."""

    def __hash__(self) -> int: ...

class BRepMesh_BaseMeshAlgo(nanoocp.IMeshTools.IMeshTools_MeshAlgo):
    """
    Class provides base functionality for algorithms building face triangulation.
    Performs initialization of BRepMesh_DataStructureOfDelaun and nodes map structures.
    """

    def Perform(self, theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs processing of the given face."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ConstrainedBaseMeshAlgo(BRepMesh_BaseMeshAlgo):
    """
    Class provides base functionality to build face triangulation using Dealunay approach.
    Performs generation of mesh using raw data from model.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_DefaultRangeSplitter:
    """
    Default tool to define range of discrete face model and
    obtain grid points distributed within this range.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_DefaultRangeSplitter) -> None: ...

    def Reset(self, theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Resets this splitter. Must be called before first use."""

    def AddPoint(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """Registers border point."""

    def AdjustRange(self) -> None:
        """Updates discrete range of surface according to its geometric range."""

    def IsValid(self) -> bool:
        """Returns True if computed range is valid."""

    def Scale(self, thePoint: nanoocp.gp.gp_Pnt2d, isToFaceBasis: bool) -> nanoocp.gp.gp_Pnt2d:
        """
        Scales the given point from real parametric space
        to face basis and otherwise.
        @param thePoint point to be scaled.
        @param isToFaceBasis if TRUE converts point to face basis,
        otherwise performs reverse conversion.
        @return scaled point.
        """

    def GenerateSurfaceNodes(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]:
        """
        Returns list of nodes generated using surface data and specified parameters.
        By default returns null ptr.
        """

    def Point(self, thePoint2d: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Pnt:
        """
        Returns point in 3d space corresponded to the given
        point defined in parametric space of surface.
        """

    def GetDFace(self) -> nanoocp.IMeshData.IMeshData_Face:
        """Returns face model."""

    def GetSurface(self) -> nanoocp.BRepAdaptor.BRepAdaptor_Surface:
        """Returns surface."""

    def GetRangeU(self) -> tuple[float, float]:
        """Returns U range."""

    def GetRangeV(self) -> tuple[float, float]:
        """Returns V range."""

    def GetDelta(self) -> tuple[float, float]:
        """Returns delta."""

    def GetToleranceUV(self) -> tuple[float, float]: ...

class BRepMesh_UVParamRangeSplitter(BRepMesh_DefaultRangeSplitter):
    """
    Intended to generate internal mesh nodes using UV parameters of boundary discrete points.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_UVParamRangeSplitter) -> None: ...

    def Reset(self, theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Resets this splitter."""

    def GetParametersU(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_IndexedMap[float]]:
        """Returns U parameters."""

    def GetParametersV(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_IndexedMap[float]]:
        """Returns V parameters."""

class BRepMesh_NURBSRangeSplitter(BRepMesh_UVParamRangeSplitter):
    """
    Auxiliary class extending UV range splitter in order to generate
    internal nodes for NURBS surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_NURBSRangeSplitter) -> None: ...

    def AdjustRange(self) -> None:
        """Updates discrete range of surface according to its geometric range."""

    def GenerateSurfaceNodes(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]:
        """
        Returns list of nodes generated using surface data and specified parameters.
        """

class BRepMesh_BoundaryParamsRangeSplitter(BRepMesh_NURBSRangeSplitter):
    """
    Auxiliary class extending UV range splitter in order to generate
    internal nodes for NURBS surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_BoundaryParamsRangeSplitter) -> None: ...

    def AddPoint(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """Registers border point."""

class BRepMesh_CircleInspector:
    """Auxiliary class to find circles shot by the given point."""

    @overload
    def __init__(self, theTolerance: float, theReservedSize: int, theAllocator: nanoocp.NCollection.NCollection_IncAllocator | None) -> None:
        """
        Constructor.
        @param theTolerance tolerance to be used for identification of shot circles.
        @param theReservedSize size to be reserved for vector of circles.
        @param theAllocator memory allocator to be used by internal collections.
        """

    @overload
    def __init__(self, theOther: BRepMesh_CircleInspector) -> None: ...

    @staticmethod
    def Coord(i: int, thePnt: nanoocp.gp.gp_XY) -> float: ...

    @staticmethod
    def Shift(thePnt: nanoocp.gp.gp_XY, theTol: float) -> nanoocp.gp.gp_XY: ...

    def Bind(self, theIndex: int, theCircle: BRepMesh_Circle) -> None:
        """
        Adds the circle to vector of circles at the given position.
        @param theIndex position of circle in the vector.
        @param theCircle circle to be added.
        """

    def Circles(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepMesh.BRepMesh_Circle]]:
        """Resutns vector of registered circles."""

    def Circle(self, theIndex: int) -> BRepMesh_Circle:
        """
        Returns circle with the given index.
        @param theIndex index of circle.
        @return circle with the given index.
        """

    def SetPoint(self, thePoint: nanoocp.gp.gp_XY) -> None:
        """
        Set reference point to be checked.
        @param thePoint bullet point.
        """

    def GetShotCircles(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[int]]:
        """Returns list of circles shot by the reference point."""

    def Inspect(self, theTargetIndex: int) -> nanoocp.NCollection.NCollection_CellFilter_Action:
        """
        Performs inspection of a circle with the given index.
        @param theTargetIndex index of a circle to be checked.
        @return status of the check.
        """

    @staticmethod
    def IsEqual(theIndex: int, theTargetIndex: int) -> bool:
        """Checks indices for equality."""

class BRepMesh_CircleTool:
    """Create sort and destroy the circles used in triangulation."""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_IncAllocator | None) -> None:
        """
        Constructor.
        @param theAllocator memory allocator to be used by internal structures.
        """

    @overload
    def __init__(self, theReservedSize: int, theAllocator: nanoocp.NCollection.NCollection_IncAllocator | None) -> None:
        """
        Constructor.
        @param theReservedSize size to be reserved for vector of circles.
        @param theAllocator memory allocator to be used by internal structures.
        """

    def Init(self, arg0: int) -> None:
        """
        Initializes the tool.
        @param theReservedSize size to be reserved for vector of circles.
        """

    @overload
    def SetCellSize(self, theSize: float) -> None:
        """
        Sets new size for cell filter.
        @param theSize cell size to be set for X and Y dimensions.
        """

    @overload
    def SetCellSize(self, theSizeX: float, theSizeY: float) -> None:
        """
        Sets new size for cell filter.
        @param theSizeX cell size to be set for X dimension.
        @param theSizeY cell size to be set for Y dimension.
        """

    def SetMinMaxSize(self, theMin: nanoocp.gp.gp_XY, theMax: nanoocp.gp.gp_XY) -> None:
        """
        Sets limits of inspection area.
        @param theMin bottom left corner of inspection area.
        @param theMax top right corner of inspection area.
        """

    def IsEmpty(self) -> bool:
        """Returns true if cell filter contains no circle."""

    @overload
    def Bind(self, theIndex: int, theCircle: nanoocp.gp.gp_Circ2d) -> None:
        """
        Binds the circle to the tool.
        @param theIndex index a circle should be bound with.
        @param theCircle circle to be bound.
        """

    @overload
    def Bind(self, theIndex: int, thePoint1: nanoocp.gp.gp_XY, thePoint2: nanoocp.gp.gp_XY, thePoint3: nanoocp.gp.gp_XY) -> bool:
        """
        Computes circle on three points and bind it to the tool.
        @param theIndex index a circle should be bound with.
        @param thePoint1 first point.
        @param thePoint2 second point.
        @param thePoint3 third point.
        @return FALSE in case of impossibility to build a circle
        on the given points, TRUE elsewhere.
        """

    @staticmethod
    def MakeCircle(thePoint1: nanoocp.gp.gp_XY, thePoint2: nanoocp.gp.gp_XY, thePoint3: nanoocp.gp.gp_XY, theLocation: nanoocp.gp.gp_XY) -> tuple[bool, float]:
        """
        Computes circle on three points.
        @param thePoint1 first point.
        @param thePoint2 second point.
        @param thePoint3 third point.
        @param[out] theLocation center of computed circle.
        @param[out] theRadius radius of computed circle.
        @return FALSE in case of impossibility to build a circle
        on the given points, TRUE elsewhere.
        """

    def MocBind(self, theIndex: int) -> None:
        """
        Binds implicit zero circle.
        @param theIndex index a zero circle should be bound with.
        """

    def Delete(self, theIndex: int) -> None:
        """
        Deletes a circle from the tool.
        @param theIndex index of a circle to be removed.
        """

    def Select(self, thePoint: nanoocp.gp.gp_XY) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[int]]:
        """
        Select the circles shot by the given point.
        @param thePoint bullet point.
        """

class BRepMesh_Classifier(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary class intended for classification of points
    regarding internals of discrete face.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_Classifier) -> None: ...

    def Perform(self, thePoint: nanoocp.gp.gp_Pnt2d) -> nanoocp.TopAbs.TopAbs_State:
        """
        Performs classification of the given point regarding to face internals.
        @param thePoint Point in parametric space to be classified.
        @return TopAbs_IN if point lies within face boundaries and TopAbs_OUT elsewhere.
        """

    def RegisterWire(self, theWire: "NCollection_Sequence<gp_Pnt2d const*>", theTolUV: tuple[float, float], theRangeU: tuple[float, float], theRangeV: tuple[float, float]) -> None:
        """
        Registers wire specified by sequence of points for
        further classification of points.
        @param theWire Wire to be registered. Specified by sequence of points.
        @param theTolUV Tolerance to be used for calculations in parametric space.
        @param theUmin Lower U boundary of the face in parametric space.
        @param theUmax Upper U boundary of the face in parametric space.
        @param theVmin Lower V boundary of the face in parametric space.
        @param theVmax Upper V boundary of the face in parametric space.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ConeRangeSplitter(BRepMesh_DefaultRangeSplitter):
    """
    Auxiliary class extending default range splitter in
    order to generate internal nodes for conical surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ConeRangeSplitter) -> None: ...

    def GetSplitSteps(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> tuple[tuple[float, float], tuple[int, int]]:
        """
        Returns split intervals along U and V direction.
        @param theParameters meshing parameters.
        @param[out] theStepsNb number of steps along corresponding direction.
        """

    def GenerateSurfaceNodes(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]:
        """
        Returns list of nodes generated using surface data and specified parameters.
        """

class BRepMesh_Context(nanoocp.IMeshTools.IMeshTools_Context):
    """
    Class implementing default context of BRepMesh algorithm.
    Initializes context by default algorithms.
    """

    @overload
    def __init__(self, theMeshType: nanoocp.IMeshTools.IMeshTools_MeshAlgoType = ...) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_Context) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_CurveTessellator(nanoocp.IMeshTools.IMeshTools_CurveTessellator):
    """
    Auxiliary class performing tessellation of passed edge according to specified parameters.
    """

    @overload
    def __init__(self, theEdge: nanoocp.IMeshData.IMeshData_Edge | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters, theMinPointsNb: int = 2) -> None: ...

    @overload
    def __init__(self, theEdge: nanoocp.IMeshData.IMeshData_Edge | None, theOrientation: nanoocp.TopAbs.TopAbs_Orientation, theFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters, theMinPointsNb: int = 2) -> None:
        """Constructor."""

    def PointsNb(self) -> int:
        """Returns number of tessellation points."""

    def Value(self, theIndex: int, thePoint: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns parameters of solution with the given index.
        @param theIndex index of tessellation point.
        @param theParameter parameters on PCurve corresponded to the solution.
        @param thePoint tessellation point.
        @return True in case of valid result, false elewhere.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_CylinderRangeSplitter(BRepMesh_DefaultRangeSplitter):
    """
    Auxiliary class extending default range splitter in
    order to generate internal nodes for cylindrical surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_CylinderRangeSplitter) -> None: ...

    def Reset(self, theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Resets this splitter. Must be called before first use."""

    def GenerateSurfaceNodes(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]:
        """
        Returns list of nodes generated using surface data and specified parameters.
        """

class BRepMesh_VertexInspector:
    """Class intended for fast searching of the coincidence points."""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_IncAllocator | None) -> None:
        """
        Constructor.
        @param theAllocator memory allocator to be used by internal collections.
        """

    @overload
    def __init__(self, theOther: BRepMesh_VertexInspector) -> None: ...

    @staticmethod
    def Coord(i: int, thePnt: nanoocp.gp.gp_XY) -> float: ...

    @staticmethod
    def Shift(thePnt: nanoocp.gp.gp_XY, theTol: float) -> nanoocp.gp.gp_XY: ...

    def Add(self, theVertex: BRepMesh_Vertex) -> int:
        """
        Registers the given vertex.
        @param theVertex vertex to be registered.
        """

    @overload
    def SetTolerance(self, theTolerance: float) -> None:
        """
        Sets the tolerance to be used for identification of
        coincident vertices equal for both dimensions.
        """

    @overload
    def SetTolerance(self, theToleranceX: float, theToleranceY: float) -> None:
        """
        Sets the tolerance to be used for identification of
        coincident vertices.
        @param theToleranceX tolerance for X dimension.
        @param theToleranceY tolerance for Y dimension.
        """

    def Clear(self) -> None:
        """Clear inspector's internal data structures."""

    def Delete(self, theIndex: int) -> None:
        """
        Deletes vertex with the given index.
        @param theIndex index of vertex to be removed.
        """

    def NbVertices(self) -> int:
        """Returns number of registered vertices."""

    def GetVertex(self, theIndex: int) -> BRepMesh_Vertex:
        """Returns vertex with the given index."""

    def SetPoint(self, thePoint: nanoocp.gp.gp_XY) -> None:
        """Set reference point to be checked."""

    def GetCoincidentPoint(self) -> int:
        """Returns index of point coinciding with regerence one."""

    def GetListOfDelPoints(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[int]]:
        """
        Returns list with indexes of vertices that have movability attribute
        equal to BRepMesh_Deleted and can be replaced with another node.
        """

    def Vertices(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepMesh.BRepMesh_Vertex]]:
        """Returns set of mesh vertices."""

    def ChangeVertices(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepMesh.BRepMesh_Vertex]]:
        """Returns set of mesh vertices for modification."""

    def Inspect(self, theTargetIndex: int) -> nanoocp.NCollection.NCollection_CellFilter_Action:
        """
        Performs inspection of a point with the given index.
        @param theTargetIndex index of a circle to be checked.
        @return status of the check.
        """

    @staticmethod
    def IsEqual(theIndex: int, theTargetIndex: int) -> bool:
        """Checks indices for equality."""

class BRepMesh_DataStructureOfDelaun(nanoocp.Standard.Standard_Transient):
    """
    Describes the data structure necessary for the mesh algorithms in
    two dimensions plane or on surface by meshing in UV space.
    """

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_IncAllocator | None, theReservedNodeSize: int = 100) -> None:
        """
        Constructor.
        @param theAllocator memory allocator to be used by internal structures.
        @param theReservedNodeSize presumed number of nodes in this mesh.
        """

    @overload
    def __init__(self, theOther: BRepMesh_DataStructureOfDelaun) -> None: ...

    def NbNodes(self) -> int:
        """
        @name API for accessing mesh nodes.
        Returns number of nodes.
        """

    def AddNode(self, theNode: BRepMesh_Vertex, isForceAdd: bool = False) -> int:
        """
        Adds node to the mesh if it is not already in the mesh.
        @param theNode node to be added to the mesh.
        @param isForceAdd adds the given node to structure without
        checking on coincidence with other nodes.
        @return index of the node in the structure.
        """

    @overload
    def IndexOf(self, theNode: BRepMesh_Vertex) -> int:
        """
        Finds the index of the given node.
        @param theNode node to find.
        @return index of the given element of zero if node is not in the mesh.
        """

    @overload
    def IndexOf(self, theLink: BRepMesh_Edge) -> int:
        """
        Finds the index of the given link.
        @param theLink link to find.
        @return index of the given element of zero if link is not in the mesh.
        """

    def GetNode(self, theIndex: int) -> BRepMesh_Vertex:
        """
        Get node by the index.
        @param theIndex index of a node.
        @return node with the given index.
        """

    def __call__(self, theIndex: int) -> BRepMesh_Vertex:
        """Alias for GetNode."""

    def SubstituteNode(self, theIndex: int, theNewNode: BRepMesh_Vertex) -> bool:
        """
        Substitutes the node with the given index by new one.
        @param theIndex index of node to be substituted.
        @param theNewNode substituting node.
        @return FALSE in case if new node is already in the structure, TRUE elsewhere.
        """

    def RemoveNode(self, theIndex: int, isForce: bool = False) -> None:
        """
        Removes node from the mesh in case if it has no connected links
        and its type is Free.
        @param theIndex index of node to be removed.
        @param isForce if TRUE node will be removed even if movability
        is not Free.
        """

    def LinksConnectedTo(self, theIndex: int) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[int]]:
        """
        Get list of links attached to the node with the given index.
        @param theIndex index of node whose links should be retrieved.
        @return list of links attached to the node.
        """

    def NbLinks(self) -> int:
        """
        @name API for accessing mesh links.
        Returns number of links.
        """

    def AddLink(self, theLink: BRepMesh_Edge) -> int:
        """
        Adds link to the mesh if it is not already in the mesh.
        @param theLink link to be added to the mesh.
        @return index of the link in the structure.
        """

    def GetLink(self, theIndex: int) -> BRepMesh_Edge:
        """
        Get link by the index.
        @param theIndex index of a link.
        @return link with the given index.
        """

    def LinksOfDomain(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns map of indices of links registered in mesh."""

    def SubstituteLink(self, theIndex: int, theNewLink: BRepMesh_Edge) -> bool:
        """
        Substitutes the link with the given index by new one.
        @param theIndex index of link to be substituted.
        @param theNewLink substituting link.
        @return FALSE in case if new link is already in the structure, TRUE elsewhere.
        """

    def RemoveLink(self, theIndex: int, isForce: bool = False) -> None:
        """
        Removes link from the mesh in case if it has no connected elements
        and its type is Free.
        @param theIndex index of link to be removed.
        @param isForce if TRUE link will be removed even if movability
        is not Free.
        """

    def ElementsConnectedTo(self, theLinkIndex: int) -> BRepMesh_PairOfIndex:
        """
        Returns indices of elements connected to the link with the given index.
        @param theLinkIndex index of link whose data should be retrieved.
        @return indices of elements connected to the link.
        """

    def NbElements(self) -> int:
        """
        @name API for accessing mesh elements.
        Returns number of links.
        """

    def AddElement(self, theElement: BRepMesh_Triangle) -> int:
        """
        Adds element to the mesh if it is not already in the mesh.
        @param theElement element to be added to the mesh.
        @return index of the element in the structure.
        """

    def GetElement(self, theIndex: int) -> BRepMesh_Triangle:
        """
        Get element by the index.
        @param theIndex index of an element.
        @return element with the given index.
        """

    def ElementsOfDomain(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns map of indices of elements registered in mesh."""

    def SubstituteElement(self, theIndex: int, theNewElement: BRepMesh_Triangle) -> bool:
        """
        Substitutes the element with the given index by new one.
        @param theIndex index of element to be substituted.
        @param theNewLink substituting element.
        @return FALSE in case if new element is already in the structure, TRUE elsewhere.
        """

    def RemoveElement(self, theIndex: int) -> None:
        """
        Removes element from the mesh.
        @param theIndex index of element to be removed.
        """

    def Dump(self, theFileNameStr: str) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_IncAllocator:
        """
        @name Auxiliary API
        Returns memory allocator used by the structure.
        """

    def Data(self) -> "BRepMesh_VertexTool":
        """
        Gives the data structure for initialization of cell size and tolerance.
        """

    def ClearDomain(self) -> None:
        """Removes all elements."""

    def ClearDeleted(self) -> None:
        """
        Substitutes deleted items by the last one from corresponding map
        to have only non-deleted elements, links or nodes in the structure.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_Deflection(nanoocp.Standard.Standard_Transient):
    """Auxiliary tool encompassing methods to compute deflection of shapes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepMesh_Deflection) -> None: ...

    @staticmethod
    def ComputeAbsoluteDeflection(theShape: nanoocp.TopoDS.TopoDS_Shape, theRelativeDeflection: float, theMaxShapeSize: float) -> float:
        """
        Returns absolute deflection for theShape with respect to the
        relative deflection and theMaxShapeSize.
        @param theShape shape for that the deflection should be computed.
        @param theRelativeDeflection relative deflection.
        @param theMaxShapeSize maximum size of the whole shape.
        @return absolute deflection for the shape.
        """

    @overload
    @staticmethod
    def ComputeDeflection(theDEdge: nanoocp.IMeshData.IMeshData_Edge | None, theMaxShapeSize: float, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Computes and updates deflection of the given discrete edge."""

    @overload
    @staticmethod
    def ComputeDeflection(theDWire: nanoocp.IMeshData.IMeshData_Wire | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Computes and updates deflection of the given discrete wire."""

    @overload
    @staticmethod
    def ComputeDeflection(theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Computes and updates deflection of the given discrete face."""

    @staticmethod
    def IsConsistent(theCurrent: float, theRequired: float, theAllowDecrease: bool, theRatio: float = 0.1) -> bool:
        """
        Checks if the deflection of current polygonal representation
        is consistent with the required deflection.
        @param[in] theCurrent  Current deflection.
        @param[in] theRequired  Required deflection.
        @param[in] theAllowDecrease  Flag controlling the check. If decrease is allowed,
        to be consistent the current and required deflections should be approximately the same.
        If not allowed, the current deflection should be less than required.
        @param[in] theRatio  The ratio for comparison of the deflections (value from 0 to 1).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_GeomTool:
    """
    Tool class accumulating common geometrical functions as well as
    functionality using shape geometry to produce data necessary for
    tessellation.
    General aim is to calculate discretization points for the given
    curve or iso curve of surface according to the specified parameters.
    """

    @overload
    def __init__(self, theCurve: nanoocp.BRepAdaptor.BRepAdaptor_Curve, theFirstParam: float, theLastParam: float, theLinDeflection: float, theAngDeflection: float, theMinPointsNb: int = 2, theMinSize: float = 1e-07) -> None:
        """
        Constructor.
        Initiates discretization of the given geometric curve.
        @param theCurve curve to be discretized.
        @param theFirstParam first parameter of the curve.
        @param theLastParam last parameter of the curve.
        @param theLinDeflection linear deflection.
        @param theAngDeflection angular deflection.
        @param theMinPointsNb minimum number of points to be produced.
        """

    @overload
    def __init__(self, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theIsoType: nanoocp.GeomAbs.GeomAbs_IsoType, theParamIso: float, theFirstParam: float, theLastParam: float, theLinDeflection: float, theAngDeflection: float, theMinPointsNb: int = 2, theMinSize: float = 1e-07) -> None:
        """
        Constructor.
        Initiates discretization of geometric curve corresponding
        to iso curve of the given surface.
        @param theSurface surface the iso curve to be taken from.
        @param theIsoType type of iso curve to be used, U or V.
        @param theParamIso parameter on the surface specifying the iso curve.
        @param theFirstParam first parameter of the curve.
        @param theLastParam last parameter of the curve.
        @param theLinDeflection linear deflection.
        @param theAngDeflection angular deflection.
        @param theMinPointsNb minimum number of points to be produced.
        """

    @overload
    def __init__(self, theOther: BRepMesh_GeomTool) -> None: ...

    class IntFlag(enum.IntEnum):
        """Enumerates states of segments intersection check."""

        NoIntersection = 0

        Cross = 1

        EndPointTouch = 2

        PointOnSegment = 3

        Glued = 4

        Same = 5

    NoIntersection: BRepMesh_GeomTool.IntFlag = IntFlag.NoIntersection

    Cross: BRepMesh_GeomTool.IntFlag = IntFlag.Cross

    EndPointTouch: BRepMesh_GeomTool.IntFlag = IntFlag.EndPointTouch

    PointOnSegment: BRepMesh_GeomTool.IntFlag = IntFlag.PointOnSegment

    Glued: BRepMesh_GeomTool.IntFlag = IntFlag.Glued

    Same: BRepMesh_GeomTool.IntFlag = IntFlag.Same

    def AddPoint(self, thePoint: nanoocp.gp.gp_Pnt, theParam: float, theIsReplace: bool = True) -> int:
        """
        Adds point to already calculated points (or replaces existing).
        @param thePoint point to be added.
        @param theParam parameter on the curve corresponding to the given point.
        @param theIsReplace if TRUE replaces existing point lying within
        parametric tolerance of the given point.
        @return index of new added point or found with parametric tolerance
        """

    def NbPoints(self) -> int:
        """Returns number of discretization points."""

    @overload
    def Value(self, theIndex: int, theIsoParam: float, thePoint: nanoocp.gp.gp_Pnt, theUV: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float]:
        """
        Gets parameters of discretization point with the given index.
        @param theIndex index of discretization point.
        @param theIsoParam parameter on surface to be used as second coordinate
        of resulting 2d point.
        @param[out] theParam parameter of the point on the iso curve.
        @param[out] thePoint discretization point.
        @param[out] theUV discretization point in parametric space of the surface.
        @return TRUE on success, FALSE elsewhere.
        """

    @overload
    def Value(self, theIndex: int, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, thePoint: nanoocp.gp.gp_Pnt, theUV: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float]:
        """
        Gets parameters of discretization point with the given index.
        @param theIndex index of discretization point.
        @param theSurface surface the curve is lying onto.
        @param[out] theParam parameter of the point on the curve.
        @param[out] thePoint discretization point.
        @param[out] theUV discretization point in parametric space of the surface.
        @return TRUE on success, FALSE elsewhere.
        """

    @staticmethod
    def Normal(theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theParamU: float, theParamV: float, thePoint: nanoocp.gp.gp_Pnt, theNormal: nanoocp.gp.gp_Dir) -> bool:
        """
        @name static API
        Computes normal to the given surface at the specified
        position in parametric space.
        @param theSurface surface the normal should be found for.
        @param theParamU U parameter in parametric space of the surface.
        @param theParamV V parameter in parametric space of the surface.
        @param[out] thePoint 3d point corresponding to the given parameters.
        @param[out] theNormal normal vector at the point specified by the parameters.
        @return FALSE if the normal can not be computed, TRUE elsewhere.
        """

    @staticmethod
    def IntSegSeg(theStartPnt1: nanoocp.gp.gp_XY, theEndPnt1: nanoocp.gp.gp_XY, theStartPnt2: nanoocp.gp.gp_XY, theEndPnt2: nanoocp.gp.gp_XY, isConsiderEndPointTouch: bool, isConsiderPointOnSegment: bool, theIntPnt: nanoocp.gp.gp_Pnt2d) -> BRepMesh_GeomTool.IntFlag:
        """
        Checks intersection between the two segments.
        Checks that intersection point lies within ranges of both segments.
        @param theStartPnt1 start point of first segment.
        @param theEndPnt1 end point of first segment.
        @param theStartPnt2 start point of second segment.
        @param theEndPnt2 end point of second segment.
        @param isConsiderEndPointTouch if TRUE EndPointTouch status will be
        returned in case if segments are touching by end points, if FALSE
        returns NoIntersection flag.
        @param isConsiderPointOnSegment if TRUE PointOnSegment status will be
        returned in case if end point of one segment lies onto another one,
        if FALSE returns NoIntersection flag.
        @param[out] theIntPnt point of intersection.
        @return status of intersection check.
        """

    @staticmethod
    def SquareDeflectionOfSegment(theFirstPoint: nanoocp.gp.gp_Pnt, theLastPoint: nanoocp.gp.gp_Pnt, theMidPoint: nanoocp.gp.gp_Pnt) -> float:
        """Compute deflection of the given segment."""

    @staticmethod
    def CellsCount(theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theVerticesNb: int, theDeflection: float, theRangeSplitter: BRepMesh_DefaultRangeSplitter) -> tuple[int, int]: ...

class BRepMesh_Delaun:
    """Compute the Delaunay's triangulation with the algorithm of Watson."""

    @overload
    def __init__(self, theVertices: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Array1[nanoocp.BRepMesh.BRepMesh_Vertex]]) -> None:
        """Creates the triangulation with an empty Mesh data structure."""

    @overload
    def __init__(self, theOldMesh: BRepMesh_DataStructureOfDelaun | None, theVertices: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Array1[nanoocp.BRepMesh.BRepMesh_Vertex]]) -> None:
        """Creates the triangulation with an existent Mesh data structure."""

    @overload
    def __init__(self, theOldMesh: BRepMesh_DataStructureOfDelaun | None, theVertexIndices: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[int]]) -> None: ...

    @overload
    def __init__(self, theOldMesh: BRepMesh_DataStructureOfDelaun | None, theCellsCountU: int, theCellsCountV: int, isFillCircles: bool) -> None:
        """
        Creates instance of triangulator, but do not run the algorithm automatically.
        """

    @overload
    def __init__(self, theOldMesh: BRepMesh_DataStructureOfDelaun | None, theVertexIndices: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[int]], theCellsCountU: int, theCellsCountV: int) -> None:
        """Creates the triangulation with an existant Mesh data structure."""

    def Init(self, theVertices: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Array1[nanoocp.BRepMesh.BRepMesh_Vertex]]) -> None:
        """Initializes the triangulation with an array of vertices."""

    def InitCirclesTool(self, theCellsCountU: int, theCellsCountV: int) -> None:
        """Forces initialization of circles cell filter using working structure."""

    def RemoveVertex(self, theVertex: BRepMesh_Vertex) -> None:
        """Removes a vertex from the triangulation."""

    def AddVertices(self, theVerticesIndices: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[int]], theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Adds some vertices into the triangulation."""

    def UseEdge(self, theEdge: int) -> bool:
        """
        Modify mesh to use the edge.
        @return True if done
        """

    def Result(self) -> BRepMesh_DataStructureOfDelaun:
        """Gives the Mesh data structure."""

    def ProcessConstraints(self) -> None:
        """Forces insertion of constraint edges into the base triangulation."""

    def Frontier(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Gives the list of frontier edges."""

    def InternalEdges(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Gives the list of internal edges."""

    def FreeEdges(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Gives the list of free edges used only one time"""

    def GetVertex(self, theIndex: int) -> BRepMesh_Vertex:
        """Gives vertex with the given index"""

    def GetEdge(self, theIndex: int) -> BRepMesh_Edge:
        """Gives edge with the given index"""

    def GetTriangle(self, theIndex: int) -> BRepMesh_Triangle:
        """Gives triangle with the given index"""

    def Circles(self) -> "BRepMesh_CircleTool":
        """Returns tool used to build mesh consistent to Delaunay criteria."""

    def Contains(self, theTriangleId: int, theVertex: BRepMesh_Vertex, theSqTolerance: float) -> tuple[bool, int]:
        """
        Test is the given triangle contains the given vertex.
        @param theSqTolerance square tolerance to check closeness to some edge
        @param theEdgeOn If it is != 0 the vertex lies onto the edge index
        returned through this parameter.
        """

    def SetAuxVertices(self, theSupVert: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[int]]) -> None:
        """
        Explicitly sets ids of auxiliary vertices used to build mesh and used by 3rd-party algorithms.
        """

    def RemoveAuxElements(self) -> None:
        """
        Destruction of auxiliary triangles containing the given vertices.
        Removes auxiliary vertices also.
        @param theAuxVertices auxiliary vertices to be cleaned up.
        """

class BRepMesh_DelaunayBaseMeshAlgo(BRepMesh_ConstrainedBaseMeshAlgo):
    """
    Class provides base functionality to build face triangulation using Dealunay approach.
    Performs generation of mesh using raw data from model.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_DelaunayBaseMeshAlgo) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_DiscretAlgoFactory(nanoocp.Standard.Standard_Transient):
    """
    Abstract factory for creating meshing algorithms.
    This class provides a registry-based factory pattern that allows multiple
    meshing algorithms to coexist without symbol collisions.
    It follows the pattern established by Graphic3d_GraphicDriverFactory.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def RegisterFactory(theFactory: BRepMesh_DiscretAlgoFactory | None, theIsPreferred: bool = False) -> None:
        """
        Registers a factory in the global registry.
        @param[in] theFactory     factory to register
        @param[in] theIsPreferred if TRUE, add to the beginning of the list (making it default),
        otherwise add to the end
        """

    @staticmethod
    def UnregisterFactory(theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Unregisters a factory by name.
        @param[in] theName name of the factory to unregister
        """

    @staticmethod
    def DefaultFactory() -> BRepMesh_DiscretAlgoFactory:
        """
        Returns the default (first registered) factory, or NULL if none registered.
        """

    @staticmethod
    def FindFactory(theName: nanoocp.TCollection.TCollection_AsciiString) -> BRepMesh_DiscretAlgoFactory:
        """
        Finds a factory by name.
        @param[in] theName name of the factory to find
        @return factory handle, or NULL if not found
        """

    @staticmethod
    def Factories() -> nanoocp.NCollection.NCollection_List[nanoocp.BRepMesh.BRepMesh_DiscretAlgoFactory]:
        """Returns the global list of registered factories."""

    def CreateAlgorithm(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLinDeflection: float, theAngDeflection: float) -> BRepMesh_DiscretRoot:
        """
        Creates a new meshing algorithm instance.
        @param[in] theShape         shape to be meshed
        @param[in] theLinDeflection linear deflection for meshing
        @param[in] theAngDeflection angular deflection for meshing
        @return new meshing algorithm instance
        """

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the factory name."""

class BRepMesh_DiscretRoot(nanoocp.Standard.Standard_Transient):
    """
    This is a common interface for meshing algorithms
    instantiated by Mesh Factory and implemented by plugins.
    """

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Set the shape to triangulate."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def IsDone(self) -> bool:
        """Returns true if triangualtion was performed and has success."""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Compute triangulation for set shape."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_DiscretFactory:
    """
    Factory for retrieving triangulation algorithms.
    Use BRepMesh_DiscretFactory::Get() static method to retrieve global Factory instance.
    Use BRepMesh_DiscretFactory::Discret() method to retrieve meshing tool.

    This class delegates to BRepMesh_DiscretAlgoFactory registry for algorithm creation.
    @sa BRepMesh_DiscretAlgoFactory
    """

    def __init__(self, theOther: BRepMesh_DiscretFactory) -> None: ...

    @staticmethod
    def Get() -> BRepMesh_DiscretFactory:
        """Returns the global factory instance."""

    def SetDefaultName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Setup meshing algorithm by name.
        Returns TRUE if requested algorithm is available.
        On fail Factory will continue to use previous algorithm.
        @param[in] theName name of the algorithm to use
        """

    def DefaultName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns name of current meshing algorithm."""

    def Discret(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLinDeflection: float, theAngDeflection: float) -> BRepMesh_DiscretRoot:
        """
        Returns triangulation algorithm instance.
        @param[in] theShape         shape to be meshed
        @param[in] theLinDeflection linear deflection to be used for meshing
        @param[in] theAngDeflection angular deflection to be used for meshing
        @return new meshing algorithm instance, or NULL if no algorithm available
        """

class BRepMesh_IncrementalMeshFactory(BRepMesh_DiscretAlgoFactory):
    """
    Factory for creating BRepMesh_IncrementalMesh instances.
    This factory is registered under the name "FastDiscret" and provides
    the default built-in meshing algorithm.
    """

    @overload
    def __init__(self) -> None:
        """Constructor. Registers this factory under the name "FastDiscret"."""

    @overload
    def __init__(self, theOther: BRepMesh_IncrementalMeshFactory) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CreateAlgorithm(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLinDeflection: float, theAngDeflection: float) -> BRepMesh_DiscretRoot:
        """
        Creates a new BRepMesh_IncrementalMesh instance.
        @param[in] theShape         shape to be meshed
        @param[in] theLinDeflection linear deflection for meshing
        @param[in] theAngDeflection angular deflection for meshing
        @return new meshing algorithm instance
        """

class BRepMesh_EdgeDiscret(nanoocp.IMeshTools.IMeshTools_ModelAlgo):
    """
    Class implements functionality of edge discret tool.
    Performs check of the edges for existing Poly_PolygonOnTriangulation.
    In case if it fits specified deflection, restores data structure using
    it, else clears edges from outdated data.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_EdgeDiscret) -> None: ...

    @overload
    @staticmethod
    def CreateEdgeTessellator(theDEdge: nanoocp.IMeshData.IMeshData_Edge | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters, theMinPointsNb: int = 2) -> nanoocp.IMeshTools.IMeshTools_CurveTessellator:
        """Creates instance of free edge tessellator."""

    @overload
    @staticmethod
    def CreateEdgeTessellator(theDEdge: nanoocp.IMeshData.IMeshData_Edge | None, theOrientation: nanoocp.TopAbs.TopAbs_Orientation, theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters, theMinPointsNb: int = 2) -> nanoocp.IMeshTools.IMeshTools_CurveTessellator:
        """Creates instance of edge tessellator."""

    @staticmethod
    def CreateEdgeTessellationExtractor(theDEdge: nanoocp.IMeshData.IMeshData_Edge | None, theDFace: nanoocp.IMeshData.IMeshData_Face | None) -> nanoocp.IMeshTools.IMeshTools_CurveTessellator:
        """Creates instance of tessellation extractor."""

    def __call__(self, theEdgeIndex: int) -> None:
        """Functor API to discretize the given edge."""

    @staticmethod
    def Tessellate3d(theDEdge: nanoocp.IMeshData.IMeshData_Edge | None, theTessellator: nanoocp.IMeshTools.IMeshTools_CurveTessellator | None, theUpdateEnds: bool) -> None:
        """Updates 3d discrete edge model using the given tessellation tool."""

    @staticmethod
    def Tessellate2d(theDEdge: nanoocp.IMeshData.IMeshData_Edge | None, theUpdateEnds: bool) -> None:
        """Updates 2d discrete edge model using tessellation of 3D curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_EdgeTessellationExtractor(nanoocp.IMeshTools.IMeshTools_CurveTessellator):
    """
    Auxiliary class implements functionality retrieving tessellated
    representation of an edge stored in polygon.
    """

    @overload
    def __init__(self, theEdge: nanoocp.IMeshData.IMeshData_Edge | None, theFace: nanoocp.IMeshData.IMeshData_Face | None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_EdgeTessellationExtractor) -> None: ...

    def PointsNb(self) -> int:
        """Returns number of tessellation points."""

    def Value(self, theIndex: int, thePoint: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns parameters of solution with the given index.
        @param theIndex index of tessellation point.
        @param theParameter parameters on PCurve corresponded to the solution.
        @param thePoint tessellation point.
        @return True in case of valid result, false elewhere.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ExtrusionRangeSplitter(BRepMesh_NURBSRangeSplitter):
    """
    Auxiliary class analysing extrusion surface in order to generate internal nodes.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ExtrusionRangeSplitter) -> None: ...

class BRepMesh_FaceChecker(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary class checking wires of target face for self-intersections.
    Explodes wires of discrete face on sets of segments using tessellation
    data stored in model. Each segment is then checked for intersection with
    other ones. All collisions are registered and returned as result of check.
    """

    def __init__(self, theFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> None:
        """Default constructor"""

    class Segment:
        """
        @name mesher API
        Identifies segment inside face.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepMesh_FaceChecker.Segment) -> None: ...

        @property
        def EdgePtr(self) -> nanoocp.IMeshData.IMeshData_Edge: ...

        @EdgePtr.setter
        def EdgePtr(self, arg: nanoocp.IMeshData.IMeshData_Edge, /) -> None: ...

        @property
        def Point1(self) -> nanoocp.gp.gp_Pnt2d: ...

        @Point1.setter
        def Point1(self, arg: nanoocp.gp.gp_Pnt2d, /) -> None: ...

        @property
        def Point2(self) -> nanoocp.gp.gp_Pnt2d: ...

        @Point2.setter
        def Point2(self, arg: nanoocp.gp.gp_Pnt2d, /) -> None: ...

    def Perform(self) -> bool:
        """
        Performs check wires of the face for intersections.
        @return True if there is no intersection, False elsewhere.
        """

    def GetIntersectingEdges(self) -> "NCollection_Shared<NCollection_Map<IMeshData_Edge*, NCollection_DefaultHasher<IMeshData_Edge*>>, void>":
        """Returns intersecting edges."""

    def __call__(self, theWireIndex: int) -> None:
        """Checks wire with the given index for intersection with others."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_FaceDiscret(nanoocp.IMeshTools.IMeshTools_ModelAlgo):
    """
    Class implements functionality starting triangulation of model's faces.
    Each face is processed separately and can be executed in parallel mode.
    Uses mesh algo factory passed as initializer to create instance of triangulation
    algorithm according to type of surface of target face.
    """

    @overload
    def __init__(self, theAlgoFactory: nanoocp.IMeshTools.IMeshTools_MeshAlgoFactory | None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_FaceDiscret) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_FastDiscret:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepMesh_FastDiscret) -> None: ...

class BRepMesh_IncrementalMesh(BRepMesh_DiscretRoot):
    """
    Builds the mesh of a shape with respect of their
    correctly triangulated parts
    """

    @overload
    def __init__(self) -> None:
        """
        @name mesher API
        Default constructor
        """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLinDeflection: float, isRelative: bool = False, theAngDeflection: float = 0.5, isInParallel: bool = False) -> None:
        """
        Constructor.
        Automatically calls method Perform.
        @param theShape shape to be meshed.
        @param theLinDeflection linear deflection.
        @param isRelative if TRUE deflection used for discretization of
        each edge will be <theLinDeflection> * <size of edge>. Deflection
        used for the faces will be the maximum deflection of their edges.
        @param theAngDeflection angular deflection.
        @param isInParallel if TRUE shape will be meshed in parallel.
        """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor.
        Automatically calls method Perform.
        @param theShape shape to be meshed.
        @param theParameters - parameters of meshing
        """

    @overload
    def __init__(self, theOther: BRepMesh_IncrementalMesh) -> None: ...

    @overload
    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs meshing of the shape."""

    @overload
    def Perform(self, theContext: nanoocp.IMeshTools.IMeshTools_Context | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs meshing using custom context;"""

    def Parameters(self) -> nanoocp.IMeshTools.IMeshTools_Parameters:
        """
        @name accessing to parameters.
        Returns meshing parameters
        """

    def ChangeParameters(self) -> nanoocp.IMeshTools.IMeshTools_Parameters:
        """Returns modifiable meshing parameters"""

    def IsModified(self) -> bool:
        """Returns modified flag."""

    def GetStatusFlags(self) -> int:
        """Returns accumulated status flags faced during meshing."""

    @staticmethod
    def IsParallelDefault() -> bool:
        """
        Returns multi-threading usage flag set by default in
        Discret() static method (thus applied only to Mesh Factories).
        """

    @staticmethod
    def SetParallelDefault(isInParallel: bool) -> None:
        """
        Setup multi-threading usage flag set by default in
        Discret() static method (thus applied only to Mesh Factories).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_MeshAlgoFactory(nanoocp.IMeshTools.IMeshTools_MeshAlgoFactory):
    """
    Default implementation of IMeshTools_MeshAlgoFactory providing algorithms
    of different complexity depending on type of target surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_MeshAlgoFactory) -> None: ...

    def GetAlgo(self, theSurfaceType: nanoocp.GeomAbs.GeomAbs_SurfaceType, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.IMeshTools.IMeshTools_MeshAlgo:
        """Creates instance of meshing algorithm for the given type of surface."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_MeshTool(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary tool providing API for manipulation with BRepMesh_DataStructureOfDelaun.
    """

    @overload
    def __init__(self, theStructure: BRepMesh_DataStructureOfDelaun | None) -> None:
        """
        Constructor.
        Initializes tool by the given data structure.
        """

    @overload
    def __init__(self, theOther: BRepMesh_MeshTool) -> None: ...

    class NodeClassifier:
        """
        Helper functor intended to separate points to left and right from the constraint.
        """

        def __init__(self, theConstraint: BRepMesh_Edge, theStructure: BRepMesh_DataStructureOfDelaun | None) -> None: ...

        def IsAbove(self, theNodeIndex: int) -> bool: ...

    def GetStructure(self) -> BRepMesh_DataStructureOfDelaun:
        """Returns data structure manipulated by this tool."""

    def DumpTriangles(self, theFileName: str, theTriangles: nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]) -> None:
        """Dumps triangles to specified file."""

    def AddAndLegalizeTriangle(self, thePoint1: int, thePoint2: int, thePoint3: int) -> None:
        """
        Adds new triangle with specified nodes to mesh.
        Legalizes triangle in case if it violates circle criteria.
        """

    def AddLink(self, theFirstNode: int, theLastNode: int) -> tuple[int, bool]:
        """
        Adds new link to mesh.
        Updates link index and link orientation parameters.
        """

    def Legalize(self, theLinkIndex: int) -> None:
        """Performs legalization of triangles connected to the specified link."""

    def EraseItemsConnectedTo(self, theNodeIndex: int) -> None:
        """
        Erases all elements connected to the specified artificial node.
        In addition, erases the artificial node itself.
        """

    def CleanFrontierLinks(self) -> None:
        """Cleans frontier links from triangles to the right."""

    def EraseTriangles(self, theTriangles: nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger], theLoopEdges: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[int, bool]]) -> None:
        """
        Erases the given set of triangles.
        Fills map of loop edges forming the contour surrounding the erased triangles.
        """

    def EraseTriangle(self, theTriangleIndex: int, theLoopEdges: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[int, bool]]) -> None:
        """
        Erases triangle with the given index and adds the free edges into the map.
        When an edge is suppressed more than one time it is destroyed.
        """

    @overload
    def EraseFreeLinks(self) -> None:
        """Erases all links that have no elements connected to them."""

    @overload
    def EraseFreeLinks(self, theLinks: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[int, bool]]) -> None:
        """
        Erases links from the specified map that have no elements connected to them.
        """

    def GetEdgesByType(self, theEdgeType: BRepMesh_DegreeOfFreedom) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Gives the list of edges with type defined by input parameter."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ModelBuilder(nanoocp.IMeshTools.IMeshTools_ModelBuilder):
    """
    Class implements interface representing tool for discrete model building.

    The following statuses should be used by default:
    Message_Done1 - model has been successfully built.
    Message_Fail1 - empty shape.
    Message_Fail2 - model has not been build due to unexpected reason.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ModelBuilder) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ModelHealer(nanoocp.IMeshTools.IMeshTools_ModelAlgo):
    """
    Class implements functionality of model healer tool.
    Iterates over model's faces and checks consistency of their wires,
    i.e.whether wires are closed and do not contain self - intersections.
    In case if wire contains disconnected parts, ends of adjacent edges
    forming the gaps are connected in parametric space forcibly. The notion
    of this operation is to create correct discrete model defined relatively
    parametric space of target face taking into account connectivity and
    tolerances of 3D space only. This means that there are no specific
    computations are made for the sake of determination of U and V tolerance.
    Registers intersections on edges forming the face's shape and tries to
    amplify discrete representation by decreasing of deflection for the target edge.
    Checks can be performed in parallel mode.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ModelHealer) -> None: ...

    @overload
    def __call__(self, theEdgeIndex: int) -> None: ...

    @overload
    def __call__(self, theDFace: nanoocp.IMeshData.IMeshData_Face | None) -> None:
        """Functor API to discretize the given edge."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ModelPostProcessor(nanoocp.IMeshTools.IMeshTools_ModelAlgo):
    """
    Class implements functionality of model post-processing tool.
    Stores polygons on triangulations to TopoDS_Edge.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ModelPostProcessor) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ModelPreProcessor(nanoocp.IMeshTools.IMeshTools_ModelAlgo):
    """
    Class implements functionality of model pre-processing tool.
    Nullifies existing polygonal data in case if model elements
    have IMeshData_Outdated status.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ModelPreProcessor) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_SelectorOfDataStructureOfDelaun(nanoocp.Standard.Standard_Transient):
    """
    Describes a selector and an iterator on a
    selector of components of a mesh.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theMesh: BRepMesh_DataStructureOfDelaun | None) -> None:
        """
        Constructor.
        Initializes selector by the mesh.
        """

    @overload
    def __init__(self, theOther: BRepMesh_SelectorOfDataStructureOfDelaun) -> None: ...

    def Initialize(self, theMesh: BRepMesh_DataStructureOfDelaun | None) -> None:
        """Initializes selector by the mesh."""

    @overload
    def NeighboursOf(self, theNode: BRepMesh_Vertex) -> None:
        """Selects all neighboring elements of the given node."""

    @overload
    def NeighboursOf(self, theLink: BRepMesh_Edge) -> None:
        """Selects all neighboring elements of the given link."""

    @overload
    def NeighboursOf(self, theElement: BRepMesh_Triangle) -> None:
        """Selects all neighboring elements of the given element."""

    @overload
    def NeighboursOf(self, arg0: BRepMesh_SelectorOfDataStructureOfDelaun) -> None:
        """Adds a level of neighbours by edge to the selector."""

    def NeighboursOfNode(self, theNodeIndex: int) -> None:
        """Selects all neighboring elements of node with the given index."""

    def NeighboursOfLink(self, theLinkIndex: int) -> None:
        """Selects all neighboring elements of link with the given index."""

    def NeighboursOfElement(self, theElementIndex: int) -> None:
        """Selects all neighboring elements by nodes of the given element."""

    def NeighboursByEdgeOf(self, theElement: BRepMesh_Triangle) -> None:
        """Selects all neighboring elements by links of the given element."""

    def AddNeighbours(self) -> None:
        """Adds a level of neighbours by edge the selector."""

    def Nodes(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns selected nodes."""

    def Links(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns selected links."""

    def Elements(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Returns selected elements."""

    def FrontierLinks(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """Gives the list of incices of frontier links."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ShapeTool(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary class providing functionality to compute,
    retrieve and store data to TopoDS and model shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepMesh_ShapeTool) -> None: ...

    @staticmethod
    def MaxFaceTolerance(theFace: nanoocp.TopoDS.TopoDS_Face) -> float:
        """
        Returns maximum tolerance of the given face.
        Considers tolerances of edges and vertices contained in the given face.
        """

    @staticmethod
    def BoxMaxDimension(theBox: nanoocp.Bnd.Bnd_Box) -> float:
        """
        Gets the maximum dimension of the given bounding box.
        If the given bounding box is void leaves the resulting value unchanged.
        @param theBox bounding box to be processed.
        @param theMaxDimension maximum dimension of the given box.
        """

    @staticmethod
    def CheckAndUpdateFlags(theEdge: nanoocp.IMeshData.IMeshData_Edge | None, thePCurve: nanoocp.IMeshData.IMeshData_PCurve | None) -> None:
        """
        Checks same parameter, same range and degenerativity attributes
        using geometrical data of the given edge and updates edge model
        by computed parameters in case of worst case - it can drop flags
        same parameter and same range to False but never to True if it is
        already set to False. In contrary, it can also drop degenerated
        flag to True, but never to False if it is already set to True.
        """

    @staticmethod
    def AddInFace(theFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.Poly.Poly_Triangulation:
        """
        Stores the given triangulation into the given face.
        @param theFace face to be updated by triangulation.
        @param theTriangulation triangulation to be stored into the face.
        """

    @staticmethod
    def NullifyFace(theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Nullifies triangulation stored in the face.
        @param theFace face to be updated by null triangulation.
        """

    @overload
    @staticmethod
    def NullifyEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge, theTriangulation: nanoocp.Poly.Poly_Triangulation | None, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Nullifies polygon on triangulation stored in the edge.
        @param theEdge edge to be updated by null polygon.
        @param theTriangulation triangulation the given edge is associated to.
        @param theLocation face location.
        """

    @overload
    @staticmethod
    def NullifyEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Nullifies 3d polygon stored in the edge.
        @param theEdge edge to be updated by null polygon.
        @param theLocation face location.
        """

    @overload
    @staticmethod
    def UpdateEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge, thePolygon: nanoocp.Poly.Poly_PolygonOnTriangulation | None, theTriangulation: nanoocp.Poly.Poly_Triangulation | None, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Updates the given edge by the given tessellated representation.
        @param theEdge edge to be updated.
        @param thePolygon tessellated representation of the edge to be stored.
        @param theTriangulation triangulation the given edge is associated to.
        @param theLocation face location.
        """

    @overload
    @staticmethod
    def UpdateEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge, thePolygon: nanoocp.Poly.Poly_Polygon3D | None) -> None:
        """
        Updates the given edge by the given tessellated representation.
        @param theEdge edge to be updated.
        @param thePolygon tessellated representation of the edge to be stored.
        """

    @overload
    @staticmethod
    def UpdateEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge, thePolygon1: nanoocp.Poly.Poly_PolygonOnTriangulation | None, thePolygon2: nanoocp.Poly.Poly_PolygonOnTriangulation | None, theTriangulation: nanoocp.Poly.Poly_Triangulation | None, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Updates the given seam edge by the given tessellated representations.
        @param theEdge edge to be updated.
        @param thePolygon1 tessellated representation corresponding to
        forward direction of the seam edge.
        @param thePolygon2 tessellated representation corresponding to
        reversed direction of the seam edge.
        @param theTriangulation triangulation the given edge is associated to.
        @param theLocation face location.
        """

    @staticmethod
    def UseLocation(thePnt: nanoocp.gp.gp_Pnt, theLoc: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.gp.gp_Pnt:
        """
        Applies location to the given point and return result.
        @param thePnt point to be transformed.
        @param theLoc location to be applied.
        """

    @staticmethod
    def UVPoints(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theFirstPoint2d: nanoocp.gp.gp_Pnt2d, theLastPoint2d: nanoocp.gp.gp_Pnt2d, isConsiderOrientation: bool = False) -> bool:
        """
        Gets the strict UV locations of the extremities of the edge using pcurve.
        """

    @overload
    @staticmethod
    def Range(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, isConsiderOrientation: bool = False) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float, float]:
        """Gets the parametric range of the given edge on the given face."""

    @overload
    @staticmethod
    def Range(theEdge: nanoocp.TopoDS.TopoDS_Edge, isConsiderOrientation: bool = False) -> tuple[bool, nanoocp.Geom.Geom_Curve, float, float]:
        """Gets the 3d range of the given edge."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_ShapeVisitor(nanoocp.IMeshTools.IMeshTools_ShapeVisitor):
    """
    Builds discrete model of a shape by adding faces and free edges.
    Computes deflection for corresponded shape and checks whether it
    fits existing polygonal representation. If not, cleans shape from
    outdated info.
    """

    @overload
    def __init__(self, theModel: nanoocp.IMeshData.IMeshData_Model | None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_ShapeVisitor) -> None: ...

    @overload
    def Visit(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Handles TopoDS_Face object."""

    @overload
    def Visit(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Handles TopoDS_Edge object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_SphereRangeSplitter(BRepMesh_DefaultRangeSplitter):
    """
    Auxiliary class extending default range splitter in
    order to generate internal nodes for spherical surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_SphereRangeSplitter) -> None: ...

    def GenerateSurfaceNodes(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]:
        """
        Returns list of nodes generated using surface data and specified parameters.
        """

class BRepMesh_TorusRangeSplitter(BRepMesh_UVParamRangeSplitter):
    """
    Auxiliary class extending UV range splitter in order to generate
    internal nodes for NURBS surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_TorusRangeSplitter) -> None: ...

    def GenerateSurfaceNodes(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]:
        """
        Returns list of nodes generated using surface data and specified parameters.
        """

    def AddPoint(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """Registers border point."""

class BRepMesh_UndefinedRangeSplitter(BRepMesh_NURBSRangeSplitter):
    """
    Auxiliary class provides safe value for surfaces that looks like NURBS
    but has no poles or other characteristics.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_UndefinedRangeSplitter) -> None: ...

class BRepMesh_CustomBaseMeshAlgo(BRepMesh_ConstrainedBaseMeshAlgo):
    """
    Class provides base functionality to build face triangulation using custom triangulation
    algorithm. Performs generation of mesh using raw data from model.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_DelabellaBaseMeshAlgo(BRepMesh_CustomBaseMeshAlgo):
    """
    Class provides base functionality to build face triangulation using Delabella project.
    Performs generation of mesh using raw data from model.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_DelabellaBaseMeshAlgo) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_DelabellaMeshAlgoFactory(nanoocp.IMeshTools.IMeshTools_MeshAlgoFactory):
    """
    Implementation of IMeshTools_MeshAlgoFactory providing Delabella-based
    algorithms of different complexity depending on type of target surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepMesh_DelabellaMeshAlgoFactory) -> None: ...

    def GetAlgo(self, theSurfaceType: nanoocp.GeomAbs.GeomAbs_SurfaceType, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> nanoocp.IMeshTools.IMeshTools_MeshAlgo:
        """Creates instance of meshing algorithm for the given type of surface."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepMesh_Triangulator:
    """Auxiliary tool to generate triangulation"""

    @overload
    def __init__(self, theXYZs: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.gp.gp_XYZ], theWires: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_Sequence[int]], theNorm: nanoocp.gp.gp_Dir) -> None:
        """Constructor. Initialized tool by the given parameters."""

    @overload
    def __init__(self, theOther: BRepMesh_Triangulator) -> None: ...

    @staticmethod
    def ToPolyTriangulation(theNodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], thePolyTriangles: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangle]) -> nanoocp.Poly.Poly_Triangulation:
        """
        Performs conversion of the given list of triangles to Poly_Triangulation.
        """

    def Perform(self, thePolyTriangles: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangle]) -> bool:
        """
        Performs triangulation of source wires and stores triangles the output list.
        """

    def SetMessenger(self, theMess: nanoocp.Message.Message_Messenger | None) -> None:
        """
        Set messenger for output information
        without this Message::DefaultMessenger() will be used
        """
