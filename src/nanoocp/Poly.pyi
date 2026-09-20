"""OCCT package Poly (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Standard
import nanoocp.gp


Poly_MeshPurpose_NONE: int = 0

Poly_MeshPurpose_Calculation: int = 1

Poly_MeshPurpose_Presentation: int = 2

Poly_MeshPurpose_Active: int = 4

Poly_MeshPurpose_Loaded: int = 8

Poly_MeshPurpose_AnyFallback: int = 16

Poly_MeshPurpose_USER: int = 32

class Poly_Triangle:
    """
    Describes a component triangle of a triangulation (Poly_Triangulation object).
    A Triangle is defined by a triplet of nodes within [1, Poly_Triangulation::NbNodes()] range.
    Each node is an index in the table of nodes specific to an existing
    triangulation of a shape, and represents a point on the surface.
    """

    @overload
    def __init__(self) -> None:
        """Constructs a triangle and sets all indices to zero."""

    @overload
    def __init__(self, theN1: int, theN2: int, theN3: int) -> None:
        """
        Constructs a triangle and sets its three indices,
        where these node values are indices in the table of nodes specific to an existing
        triangulation of a shape.
        """

    @overload
    def __init__(self, theOther: Poly_Triangle) -> None: ...

    @overload
    def Set(self, theN1: int, theN2: int, theN3: int) -> None:
        """Sets the value of the three nodes of this triangle."""

    @overload
    def Set(self, theIndex: int, theNode: int) -> None:
        """
        Sets the value of node with specified index of this triangle.
        Raises Standard_OutOfRange if index is not in 1,2,3
        """

    def Get(self) -> tuple[int, int, int]:
        """Returns the node indices of this triangle."""

    def Value(self, theIndex: int) -> int:
        """
        Get the node of given Index.
        Raises OutOfRange from Standard if Index is not in 1,2,3
        """

    @overload
    def __call__(self, Index: int) -> int: ...

    @overload
    def __call__(self, Index: int) -> int: ...

    def ChangeValue(self, theIndex: int) -> int:
        """
        Get the node of given Index.
        Raises OutOfRange if Index is not in 1,2,3
        """

    def SetValue(self, theIndex: int, theValue: int) -> None:
        """
        Python addition: sets the value ChangeValue(theIndex) returns by reference in C++.
        """

    def __getitem__(self, arg: int, /) -> int:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: int, arg1: int, /) -> None:
        """
        Python addition: sets the value operator()(Index) returns by reference in C++.
        """

class NCollection_AliasedArray__:
    """
    Defines an array of values of configurable size.
    For instance, this class allows defining an array of 32-bit or 64-bit integer values with
    bitness determined in runtime. The element size in bytes (stride) should be specified at
    construction time. Indexation starts from 0 index. As actual type of element varies at runtime,
    element accessors are defined as templates. Memory for array is allocated with the given
    alignment (template parameter).
    """

    @overload
    def __init__(self, theStride: int) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: NCollection_AliasedArray__) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, theStride: int, theLength: int) -> None:
        """Constructor"""

    def Stride(self) -> int:
        """Returns an element size in bytes."""

    def Size(self) -> int:
        """Size query"""

    def Length(self) -> int:
        """Length query (the same as Size())"""

    def IsEmpty(self) -> bool:
        """Return TRUE if array has zero length."""

    def Lower(self) -> int:
        """Lower bound"""

    def Upper(self) -> int:
        """Upper bound"""

    def IsDeletable(self) -> bool:
        """myDeletable flag"""

    def IsAllocated(self) -> bool:
        """IsAllocated flag - for naming compatibility"""

    def SizeBytes(self) -> int:
        """Return buffer size in bytes."""

    def Assign(self, theOther: NCollection_AliasedArray__) -> NCollection_AliasedArray__:
        """
        Copies data of theOther array to this.
        This array should be pre-allocated and have the same length as theOther;
        otherwise exception Standard_DimensionMismatch is thrown.
        """

    def Move(self, theOther: NCollection_AliasedArray__) -> NCollection_AliasedArray__:
        """
        Move assignment.
        This array will borrow all the data from theOther.
        The moved object will keep pointer to the memory buffer and
        range, but it will not free the buffer on destruction.
        """

    def Resize(self, theLength: int, theToCopyData: bool) -> None:
        """
        Resizes the array to specified bounds.
        No re-allocation will be done if length of array does not change,
        but existing values will not be discarded if theToCopyData set to FALSE.
        @param theLength new length of array
        @param theToCopyData flag to copy existing data into new array
        """

class Poly_ArrayOfNodes(NCollection_AliasedArray__):
    """
    Defines an array of 3D nodes of single/double precision configurable at construction time.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor of double-precision array."""

    @overload
    def __init__(self, theLength: int) -> None:
        """Constructor of double-precision array."""

    @overload
    def __init__(self, theOther: Poly_ArrayOfNodes) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, theBegin: nanoocp.gp.gp_Pnt, theLength: int) -> None: ...

    @overload
    def __init__(self, theBegin: nanoocp.BVH.BVH_Vec3f, theLength: int) -> None:
        """
        Constructor wrapping pre-allocated C-array of values without copying them.
        """

    def IsDoublePrecision(self) -> bool:
        """Returns TRUE if array defines nodes with double precision."""

    def SetDoublePrecision(self, theIsDouble: bool) -> None:
        """
        Sets if array should define nodes with double or single precision.
        Raises exception if array was already allocated.
        """

    def Assign(self, theOther: Poly_ArrayOfNodes) -> Poly_ArrayOfNodes:
        """
        Copies data of theOther array to this.
        The arrays should have the same length,
        but may have different precision / number of components (data conversion will be applied in
        the latter case).
        """

    def Move(self, theOther: Poly_ArrayOfNodes) -> Poly_ArrayOfNodes:
        """Move assignment."""

    @overload
    def Value(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """A generalized accessor to point."""

    @overload
    def Value(self, theIndex: int) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def SetValue(self, theIndex: int, theValue: nanoocp.gp.gp_Pnt) -> None:
        """A generalized setter for point."""

    @overload
    def SetValue(self, theIndex: int, theValue: nanoocp.gp.gp_Pnt) -> None: ...

    def __getitem__(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """operator[] - alias to Value"""

class Poly_ArrayOfUVNodes(NCollection_AliasedArray__):
    """
    Defines an array of 2D nodes of single/double precision configurable at construction time.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor of double-precision array."""

    @overload
    def __init__(self, theLength: int) -> None:
        """Constructor of double-precision array."""

    @overload
    def __init__(self, theOther: Poly_ArrayOfUVNodes) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, theBegin: nanoocp.gp.gp_Pnt2d, theLength: int) -> None: ...

    @overload
    def __init__(self, theBegin: nanoocp.BVH.BVH_Vec2f, theLength: int) -> None:
        """
        Constructor wrapping pre-allocated C-array of values without copying them.
        """

    def IsDoublePrecision(self) -> bool:
        """Returns TRUE if array defines nodes with double precision."""

    def SetDoublePrecision(self, theIsDouble: bool) -> None:
        """
        Sets if array should define nodes with double or single precision.
        Raises exception if array was already allocated.
        """

    def Assign(self, theOther: Poly_ArrayOfUVNodes) -> Poly_ArrayOfUVNodes:
        """
        Copies data of theOther array to this.
        The arrays should have the same length,
        but may have different precision / number of components (data conversion will be applied in
        the latter case).
        """

    def Move(self, theOther: Poly_ArrayOfUVNodes) -> Poly_ArrayOfUVNodes:
        """Move assignment."""

    @overload
    def Value(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """A generalized accessor to point."""

    @overload
    def Value(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    def SetValue(self, theIndex: int, theValue: nanoocp.gp.gp_Pnt2d) -> None:
        """A generalized setter for point."""

    @overload
    def SetValue(self, theIndex: int, theValue: nanoocp.gp.gp_Pnt2d) -> None: ...

    def __getitem__(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """operator[] - alias to Value"""

class Poly_Triangulation(nanoocp.Standard.Standard_Transient):
    """
    Provides a triangulation for a surface, a set of surfaces, or more generally a shape.

    A triangulation consists of an approximate representation of the actual shape,
    using a collection of points and triangles.
    The points are located on the surface.
    The edges of the triangles connect adjacent points with a straight line that approximates the
    true curve on the surface.

    A triangulation comprises:
    - A table of 3D nodes (3D points on the surface).
    - A table of triangles.
    Each triangle (Poly_Triangle object) comprises a triplet of indices in the table of 3D nodes
    specific to the triangulation.
    - An optional table of 2D nodes (2D points), parallel to the table of 3D nodes.
    2D point are the (u, v) parameters of the corresponding 3D point on the surface approximated
    by the triangulation.
    - An optional table of 3D vectors, parallel to the table of 3D nodes, defining normals to the
    surface at specified 3D point.
    - An optional deflection, which maximizes the distance from a point on the surface to the
    corresponding point on its approximate triangulation.

    In many cases, algorithms do not need to work with the exact representation of a surface.
    A triangular representation induces simpler and more robust adjusting, faster performances, and
    the results are as good.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty triangulation."""

    @overload
    def __init__(self, theTriangulation: Poly_Triangulation) -> None:
        """Copy constructor for triangulation."""

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Triangles: nanoocp.NCollection.NCollection_Array1[nanoocp.Poly.Poly_Triangle]) -> None:
        """
        Constructs a triangulation from a set of triangles. The
        triangulation is initialized with 3D points from Nodes and triangles
        from Triangles.
        """

    @overload
    def __init__(self, theNbNodes: int, theNbTriangles: int, theHasUVNodes: bool, theHasNormals: bool = False) -> None:
        """
        Constructs a triangulation from a set of triangles.
        The triangulation is initialized without a triangle or a node,
        but capable of containing specified number of nodes and triangles.
        @param[in] theNbNodes      number of nodes to allocate
        @param[in] theNbTriangles  number of triangles to allocate
        @param[in] theHasUVNodes   indicates whether 2D nodes will be associated with 3D ones,
        (i.e. to enable a 2D representation)
        @param[in] theHasNormals   indicates whether normals will be given and associated with nodes
        """

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], UVNodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Triangles: nanoocp.NCollection.NCollection_Array1[nanoocp.Poly.Poly_Triangle]) -> None:
        """
        Constructs a triangulation from a set of triangles. The
        triangulation is initialized with 3D points from Nodes, 2D points from
        UVNodes and triangles from Triangles, where
        coordinates of a 2D point from UVNodes are the
        (u, v) parameters of the corresponding 3D point
        from Nodes on the surface approximated by the
        constructed triangulation.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Copy(self) -> Poly_Triangulation:
        """Creates full copy of current triangulation"""

    @overload
    def Deflection(self) -> float:
        """Returns the deflection of this triangulation."""

    @overload
    def Deflection(self, theDeflection: float) -> None:
        """
        Sets the deflection of this triangulation to theDeflection.
        See more on deflection in Polygon2D
        """

    @overload
    def Parameters(self) -> Poly_TriangulationParameters:
        """Returns initial set of parameters used to generate this triangulation."""

    @overload
    def Parameters(self, theParams: Poly_TriangulationParameters) -> None:
        """Updates initial set of parameters used to generate this triangulation."""

    def Clear(self) -> None:
        """Clears internal arrays of nodes and all attributes."""

    def HasGeometry(self) -> bool:
        """Returns TRUE if triangulation has some geometry."""

    def NbNodes(self) -> int:
        """Returns the number of nodes for this triangulation."""

    def NbTriangles(self) -> int:
        """Returns the number of triangles for this triangulation."""

    def HasUVNodes(self) -> bool:
        """
        Returns true if 2D nodes are associated with 3D nodes for this triangulation.
        """

    def HasNormals(self) -> bool:
        """Returns true if nodal normals are defined."""

    def Node(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns a node at the given index.
        @param[in] theIndex node index within [1, NbNodes()] range
        @return 3D point coordinates
        """

    def SetNode(self, theIndex: int, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets a node coordinates.
        @param[in] theIndex node index within [1, NbNodes()] range
        @param[in] thePnt   3D point coordinates
        """

    def UVNode(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns UV-node at the given index.
        @param[in] theIndex node index within [1, NbNodes()] range
        @return 2D point defining UV coordinates
        """

    def SetUVNode(self, theIndex: int, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Sets an UV-node coordinates.
        @param[in] theIndex node index within [1, NbNodes()] range
        @param[in] thePnt   UV coordinates
        """

    def Triangle(self, theIndex: int) -> Poly_Triangle:
        """
        Returns triangle at the given index.
        @param[in] theIndex triangle index within [1, NbTriangles()] range
        @return triangle node indices, with each node defined within [1, NbNodes()] range
        """

    def SetTriangle(self, theIndex: int, theTriangle: Poly_Triangle) -> None:
        """
        Sets a triangle.
        @param[in] theIndex triangle index within [1, NbTriangles()] range
        @param[in] theTriangle triangle node indices, with each node defined within [1, NbNodes()]
        range
        """

    @overload
    def Normal(self, theIndex: int) -> nanoocp.gp.gp_Dir:
        """
        Returns normal at the given index.
        @param[in] theIndex node index within [1, NbNodes()] range
        @return normalized 3D vector defining a surface normal
        """

    @overload
    def Normal(self, theIndex: int, theVec3: nanoocp.BVH.BVH_Vec3f) -> None:
        """
        Returns normal at the given index.
        @param[in]  theIndex node index within [1, NbNodes()] range
        @param[out] theVec3  3D vector defining a surface normal
        """

    @overload
    def SetNormal(self, theIndex: int, theNormal: nanoocp.BVH.BVH_Vec3f) -> None:
        """
        Changes normal at the given index.
        @param[in] theIndex node index within [1, NbNodes()] range
        @param[in] theVec3  normalized 3D vector defining a surface normal
        """

    @overload
    def SetNormal(self, theIndex: int, theNormal: nanoocp.gp.gp_Dir) -> None:
        """
        Changes normal at the given index.
        @param[in] theIndex  node index within [1, NbNodes()] range
        @param[in] theNormal normalized 3D vector defining a surface normal
        """

    def MeshPurpose(self) -> int:
        """Returns mesh purpose bits."""

    def SetMeshPurpose(self, thePurpose: int) -> None:
        """Sets mesh purpose bits."""

    def CachedMinMax(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns cached min - max range of triangulation data,
        which is VOID by default (e.g, no cached information).
        """

    def SetCachedMinMax(self, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Sets a cached min - max range of this triangulation.
        The bounding box should exactly match actual range of triangulation data
        without a gap or transformation, or otherwise undefined behavior will be observed.
        Passing a VOID range invalidates the cache.
        """

    def HasCachedMinMax(self) -> bool:
        """
        Returns TRUE if there is some cached min - max range of this triangulation.
        """

    def UpdateCachedMinMax(self) -> None:
        """
        Updates cached min - max range of this triangulation with bounding box of nodal data.
        """

    def MinMax(self, theBox: nanoocp.Bnd.Bnd_Box, theTrsf: nanoocp.gp.gp_Trsf, theIsAccurate: bool = False) -> bool:
        """
        Extends the passed box with bounding box of this triangulation.
        Uses cached min - max range when available and:
        - input transformation theTrsf has no rotation part;
        - theIsAccurate is set to FALSE;
        - no triangulation data available (e.g. it is deferred and not loaded).
        @param[in][out] theBox   bounding box to extend by this triangulation
        @param[in] theTrsf  optional transformation
        @param[in] theIsAccurate  when FALSE, allows using a cached min - max range of this
        triangulation
        even for non-identity transformation.
        @return FALSE if there is no any data to extend the passed box (no both triangulation and
        cached min - max range).
        """

    def IsDoublePrecision(self) -> bool:
        """
        Returns TRUE if node positions are defined with double precision; TRUE by default.
        """

    def SetDoublePrecision(self, theIsDouble: bool) -> None:
        """
        Set if node positions should be defined with double or single precision for 3D and UV nodes.
        Raises exception if data was already allocated.
        """

    def ResizeNodes(self, theNbNodes: int, theToCopyOld: bool) -> None:
        """
        Method resizing internal arrays of nodes (synchronously for all attributes).
        @param[in] theNbNodes    new number of nodes
        @param[in] theToCopyOld  copy old nodes into the new array
        """

    def ResizeTriangles(self, theNbTriangles: int, theToCopyOld: bool) -> None:
        """
        Method resizing an internal array of triangles.
        @param[in] theNbTriangles  new number of triangles
        @param[in] theToCopyOld    copy old triangles into the new array
        """

    def AddUVNodes(self) -> None:
        """If an array for UV coordinates is not allocated yet, do it now."""

    def RemoveUVNodes(self) -> None:
        """Deallocates the UV nodes array."""

    def AddNormals(self) -> None:
        """If an array for normals is not allocated yet, do it now."""

    def RemoveNormals(self) -> None:
        """Deallocates the normals array."""

    def ComputeNormals(self) -> None:
        """Compute smooth normals by averaging triangle normals."""

    def MapNodeArray(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        Returns the table of 3D points for read-only access or NULL if nodes array is undefined.
        Poly_Triangulation::Node() should be used instead when possible.
        Returned object should not be used after Poly_Triangulation destruction.
        """

    def MapTriangleArray(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Poly.Poly_Triangle]:
        """
        Returns the triangle array for read-only access or NULL if triangle array is undefined.
        Poly_Triangulation::Triangle() should be used instead when possible.
        Returned object should not be used after Poly_Triangulation destruction.
        """

    def MapUVNodeArray(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d]:
        """
        Returns the table of 2D nodes for read-only access or NULL if UV nodes array is undefined.
        Poly_Triangulation::UVNode() should be used instead when possible.
        Returned object should not be used after Poly_Triangulation destruction.
        """

    def MapNormalArray(self) -> nanoocp.NCollection.NCollection_HArray1__float:
        """
        Returns the table of per-vertex normals for read-only access or NULL if normals array is
        undefined. Poly_Triangulation::Normal() should be used instead when possible. Returned object
        should not be used after Poly_Triangulation destruction.
        """

    def InternalTriangles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Poly.Poly_Triangle]:
        """
        Returns an internal array of triangles.
        Triangle()/SetTriangle() should be used instead in portable code.
        """

    def InternalNodes(self) -> Poly_ArrayOfNodes:
        """
        Returns an internal array of nodes.
        Node()/SetNode() should be used instead in portable code.
        """

    def InternalUVNodes(self) -> Poly_ArrayOfUVNodes:
        """
        Returns an internal array of UV nodes.
        UBNode()/SetUVNode() should be used instead in portable code.
        """

    def InternalNormals(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.BVH.BVH_Vec3f]:
        """
        Return an internal array of normals.
        Normal()/SetNormal() should be used instead in portable code.
        """

    def NbDeferredNodes(self) -> int:
        """
        @name late-load deferred data interface
        Returns number of deferred nodes that can be loaded using LoadDeferredData().
        Note: this is estimated values, which might be different from actually loaded values.
        Always check triangulation size of actually loaded data in code to avoid out-of-range issues.
        """

    def NbDeferredTriangles(self) -> int:
        """
        Returns number of deferred triangles that can be loaded using LoadDeferredData().
        Note: this is estimated values, which might be different from actually loaded values
        Always check triangulation size of actually loaded data in code to avoid out-of-range issues.
        """

    def HasDeferredData(self) -> bool:
        """
        Returns TRUE if there is some triangulation data that can be loaded using LoadDeferredData().
        """

    def LoadDeferredData(self, theFileSystem: nanoocp.OSD.OSD_FileSystem = None) -> bool:
        """
        Loads triangulation data into itself
        from some deferred storage using specified shared input file system.
        """

    def DetachedLoadDeferredData(self, theFileSystem: nanoocp.OSD.OSD_FileSystem = None) -> Poly_Triangulation:
        """
        Loads triangulation data into new Poly_Triangulation object
        from some deferred storage using specified shared input file system.
        """

    def UnloadDeferredData(self) -> bool:
        """Releases triangulation data if it has connected deferred storage."""

class Poly:
    """
    This package provides classes and services to
    handle:
    * 3D triangular polyhedrons.
    * 3D polygons.
    * 2D polygon.
    * Tools to dump, save and restore those objects.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Poly) -> None: ...

    @staticmethod
    def Catenate(lstTri: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangulation]) -> Poly_Triangulation:
        """
        Computes and stores the link from nodes to
        triangles and from triangles to neighbouring
        triangles.
        This tool is obsolete, replaced by Poly_CoherentTriangulation
        Algorithm to make minimal loops in a graph
        Join several triangulations to one new triangulation object.
        The new triangulation is just a mechanical sum of input
        triangulations, without node sharing. UV coordinates are
        dropped in the result.
        """

    @staticmethod
    def ComputeNormals(Tri: Poly_Triangulation) -> None:
        """
        Compute node normals for face triangulation
        as mean normal of surrounding triangles
        """

    @staticmethod
    def PointOnTriangle(P1: nanoocp.gp.gp_XY, P2: nanoocp.gp.gp_XY, P3: nanoocp.gp.gp_XY, P: nanoocp.gp.gp_XY, UV: nanoocp.gp.gp_XY) -> float:
        """
        Computes parameters of the point P on triangle
        defined by points P1, P2, and P3, in 2d.
        The parameters U and V are defined so that
        P = P1 + U * (P2 - P1) + V * (P3 - P1),
        with U >= 0, V >= 0, U + V <= 1.
        If P is located outside of triangle, or triangle
        is degenerated, the returned parameters correspond
        to closest point, and returned value is square of
        the distance from original point to triangle (0 if
        point is inside).
        """

    @staticmethod
    def Intersect(theTri: Poly_Triangulation, theAxis: nanoocp.gp.gp_Ax1, theIsClosest: bool, theTriangle: Poly_Triangle) -> tuple[bool, float]:
        """
        Computes the intersection between axis and triangulation.
        @param[in] theTri   input triangulation
        @param[in] theAxis  intersecting ray
        @param[in] theIsClosest  finds the closest intersection when TRUE, finds the farthest
        otherwise
        @param[out] theTriangle  intersected triangle
        @param[out] theDistance  distance along ray to intersection point
        @return TRUE if intersection takes place, FALSE otherwise.
        """

    @staticmethod
    def IntersectTriLine(theStart: nanoocp.gp.gp_XYZ, theDir: nanoocp.gp.gp_Dir, theV0: nanoocp.gp.gp_XYZ, theV1: nanoocp.gp.gp_XYZ, theV2: nanoocp.gp.gp_XYZ) -> tuple[int, float]:
        """
        Computes the intersection between a triangle defined by three vertexes and a line.
        @param[in] theStart  picking ray origin
        @param[in] theDir    picking ray direction
        @param[in] theV0     first triangle node
        @param[in] theV1     second triangle node
        @param[in] theV2     third triangle node
        @param[out] theParam  param on line of the intersection point
        @return 1 if intersection was found, 0 otherwise.
        """

class Poly_CoherentLink:
    """
    Link between two mesh nodes that is created by existing triangle(s).
    Keeps reference to the opposite node of each incident triangle.
    The referred node with index "0" is always on the left side of the link,
    the one with the index "1" is always on the right side.
    It is possible to find both incident triangles using the method
    Poly_CoherentTriangulation::FindTriangle().
    <p>
    Any Link can store an arbitrary pointer that is called Attribute.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, iNode0: int, iNode1: int) -> None:
        """
        Constructor. Creates a Link that has no reference to 'opposite nodes'.
        This constructor is useful to create temporary object that is not
        inserted into any existing triangulation.
        """

    @overload
    def __init__(self, theTri: Poly_CoherentTriangle, iSide: int) -> None:
        """
        Constructor, takes a triangle and a side. A link is created always such
        that myNode[0] < myNode[1]. Unlike the previous constructor, this one
        assigns the 'opposite node' fields. This constructor is used when a
        link is inserted into a Poly_CoherentTriangulation structure.
        @param theTri
        Triangle containing the link that is created
        @param iSide
        Can be 0, 1 or 2. Index of the node
        """

    @overload
    def __init__(self, theOther: Poly_CoherentLink) -> None: ...

    def Node(self, ind: int) -> int:
        """
        Return the node index in the current triangulation.
        @param ind
        0 or 1 making distinction of the two nodes that constitute the Link.
        Node(0) always returns a smaller number than Node(1).
        """

    def OppositeNode(self, ind: int) -> int:
        """
        Return the opposite node (belonging to the left or right incident triangle)
        index in the current triangulation.
        @param ind
        0 or 1 making distinction of the two involved triangles: 0 on the left,
        1 on the right side of the Link.
        """

    def IsEmpty(self) -> bool:
        """
        Query the status of the link - if it is an invalid one.
        An invalid link has Node members equal to -1.
        """

    def Nullify(self) -> None:
        """Invalidate this Link."""

class Poly_CoherentTriPtr:
    """
    Implementation of both list node for Poly_CoherentTriangle type and
    round double-linked list of these nodes.
    """

    class Iterator:
        """
        Iterator class for this list of triangles. Because the list is round,
        an iteration can be started from any member and it finishes before taking
        this member again. The iteration sense is always forward (Next).
        """

        @overload
        def __init__(self) -> None:
            """Empty constructor"""

        @overload
        def __init__(self, thePtr: Poly_CoherentTriPtr) -> None:
            """Constructor"""

        @overload
        def __init__(self, theOther: Poly_CoherentTriPtr.Iterator) -> None: ...

        def First(self) -> Poly_CoherentTriangle:
            """Query the triangle that started the current iteration."""

        def More(self) -> bool:
            """Query if there is available triangle pointer on this iteration"""

        def Next(self) -> None:
            """Go to the next iteration."""

        def Value(self) -> Poly_CoherentTriangle:
            """Get the current iterated triangle"""

        def ChangeValue(self) -> Poly_CoherentTriangle:
            """Get the current iterated triangle (mutable)"""

        def PtrValue(self) -> Poly_CoherentTriPtr:
            """Get the current iterated pointer to triangle"""

    def GetTriangle(self) -> Poly_CoherentTriangle:
        """Query the stored pointer to Triangle."""

    def SetTriangle(self, pTri: Poly_CoherentTriangle) -> None:
        """Initialize this instance with a pointer to triangle."""

    def Next(self) -> Poly_CoherentTriPtr:
        """Query the next pointer in the list."""

    def Previous(self) -> Poly_CoherentTriPtr:
        """Query the previous pointer in the list."""

    def Append(self, pTri: Poly_CoherentTriangle, theA: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """
        Append a pointer to triangle into the list after the current instance.
        @param pTri
        Triangle that is to be included in the list after this one.
        @param theA
        Allocator where the new pointer instance is created.
        """

    def Prepend(self, pTri: Poly_CoherentTriangle, theA: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """
        Prepend a pointer to triangle into the list before the current instance.
        @param pTri
        Triangle that is to be included in the list before this one.
        @param theA
        Allocator where the new pointer instance is created.
        """

    @staticmethod
    def Remove(thePtr: Poly_CoherentTriPtr, theA: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """
        Remove a pointer to triangle from its list.
        @param thePtr
        This class instance that should be removed from its list.
        @param theA
        Allocator where the current pointer instance was created.
        """

    @staticmethod
    def RemoveList(thePtr: Poly_CoherentTriPtr, arg1: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """Remove the list containing the given pointer to triangle."""

class Poly_CoherentNode(nanoocp.gp.gp_XYZ):
    """
    Node of coherent triangulation. Contains:
    <ul>
    <li>Coordinates of a 3D point defining the node location</li>
    <li>2D point coordinates</li>
    <li>List of triangles that use this Node</li>
    <li>Integer index, normally the index of the node in the original
    triangulation</li>
    </ul>
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, thePnt: nanoocp.gp.gp_XYZ) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Poly_CoherentNode) -> None: ...

    def SetUV(self, theU: float, theV: float) -> None:
        """Set the UV coordinates of the Node."""

    def GetU(self) -> float:
        """Get U coordinate of the Node."""

    def GetV(self) -> float:
        """Get V coordinate of the Node."""

    def SetNormal(self, theVector: nanoocp.gp.gp_XYZ) -> None:
        """Define the normal vector in the Node."""

    def HasNormal(self) -> bool:
        """Query if the Node contains a normal vector."""

    def GetNormal(self) -> nanoocp.gp.gp_XYZ:
        """Get the stored normal in the node."""

    def SetIndex(self, theIndex: int) -> None:
        """Set the value of node Index."""

    def GetIndex(self) -> int:
        """Get the value of node Index."""

    def IsFreeNode(self) -> bool:
        """
        Check if this is a free node, i.e., a node without a single
        incident triangle.
        """

    def Clear(self, arg0: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """Reset the Node to void."""

    def AddTriangle(self, theTri: Poly_CoherentTriangle, theA: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """Connect a triangle to this Node."""

    def RemoveTriangle(self, theTri: Poly_CoherentTriangle, theA: nanoocp.NCollection.NCollection_BaseAllocator) -> bool:
        """Disconnect a triangle from this Node."""

    def TriangleIterator(self) -> Poly_CoherentTriPtr.Iterator:
        """Create an iterator of incident triangles."""

class Poly_CoherentTriangle:
    """
    Data class used in Poly_CoherentTriangultion.
    Implements a triangle with references to its neighbours.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, iNode0: int, iNode1: int, iNode2: int) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Poly_CoherentTriangle) -> None: ...

    def Node(self, ind: int) -> int:
        """Query the node index in the position given by the parameter 'ind'"""

    def IsEmpty(self) -> bool:
        """Query if this is a valid triangle."""

    @overload
    def SetConnection(self, iConn: int, theTr: Poly_CoherentTriangle) -> bool:
        """
        Create connection with another triangle theTri.
        This method creates both connections: in this triangle and in theTri. You
        do not need to call the same method on triangle theTr.
        @param iConn
        Can be 0, 1 or 2 - index of the node that is opposite to the connection
        (shared link).
        @param theTr
        Triangle that is connected on the given link.
        @return
        True if successful, False if the connection is rejected
        due to improper topology.
        """

    @overload
    def SetConnection(self, theTri: Poly_CoherentTriangle) -> bool:
        """
        Create connection with another triangle theTri.
        This method creates both connections: in this triangle and in theTri.
        This method is slower than the previous one, because it makes analysis
        what sides of both triangles are connected.
        @param theTri
        Triangle that is connected.
        @return
        True if successful, False if the connection is rejected
        due to improper topology.
        """

    @overload
    def RemoveConnection(self, iConn: int) -> None:
        """
        Remove the connection with the given index.
        @param iConn
        Can be 0, 1 or 2 - index of the node that is opposite to the connection
        (shared link).
        """

    @overload
    def RemoveConnection(self, theTri: Poly_CoherentTriangle) -> bool:
        """
        Remove the connection with the given Triangle.
        @return
        True if successfuol or False if the connection has not been found.
        """

    def NConnections(self) -> int:
        """Query the number of connected triangles."""

    def GetConnectedNode(self, iConn: int) -> int:
        """
        Query the connected node on the given side.
        Returns -1 if there is no connection on the specified side.
        """

    def GetConnectedTri(self, iConn: int) -> Poly_CoherentTriangle:
        """
        Query the connected triangle on the given side.
        Returns NULL if there is no connection on the specified side.
        """

    def GetLink(self, iLink: int) -> Poly_CoherentLink:
        """
        Query the Link associate with the given side of the Triangle.
        May return NULL if there are no links in the triangulation.
        """

    def FindConnection(self, arg0: Poly_CoherentTriangle) -> int:
        """
        Returns the index of the connection with the given triangle, or -1 if not found.
        """

class Poly_CoherentTriangulation(nanoocp.Standard.Standard_Transient):
    """
    Triangulation structure that allows to:
    <ul>
    <li>Store the connectivity of each triangle with up to 3 neighbouring ones and with the
    corresponding 3rd nodes on them,</li> <li>Store the connectivity of each node with all triangles
    that share this node</li> <li>Add nodes and triangles to the structure,</li> <li>Find all
    triangles sharing a single or a couple of nodes</li> <li>Remove triangles from structure</li>
    <li>Optionally create Links between pairs of nodes according to the current triangulation.</li>
    <li>Convert from/to Poly_Triangulation structure.</li>
    </ul>

    This class is useful for algorithms that need to analyse and/or edit a triangulated mesh -- for
    example for mesh refining. The connectivity model follows the idea that all Triangles in a mesh
    should have coherent orientation like on a surface of a solid body. Connections between more than
    2 triangles are not supported.

    @section Poly_CoherentTriangulation Architecture
    The data types used in this structure are:
    <ul>
    <li><b>Poly_CoherentNode</b>: Inherits go_XYZ therefore provides the full public API of gp_XYZ.
    Contains references to all incident triangles. You can add new nodes but you cannot remove
    existing ones. However each node that has no referenced triangle is considered as "free" (use the
    method IsFreeNode() to check this). Free nodes are not available to further processing,
    particularly they are not exported in Poly_Triangulation.
    </li>
    <li><b>Poly_CoherentTriangle</b>: Main data type. Refers three Nodes, three connected Triangles,
    three opposite (connected) Nodes and three Links. If there is boundary then 1, 2 or 3 references
    to Triangles/connected Nodes/Links are assigned to NULL (for pointers) or -1 (for integer node
    index).

    You can find a triangle by one node using its triangle iterator or by
    two nodes - creating a temporary Poly_CoherentLink and calling the method FindTriangle().

    Triangles can be removed but they are never deleted from the containing array. Removed triangles
    have all nodes equal to -1. You can use the method IsEmpty() to check that.
    </li>
    <li><b>Poly_CoherentLink</b>: Auxiliary data type. Normally the array of Links is empty, because
    for many algorithms it is sufficient to define only Triangles. You can explicitly create the
    Links at least once, calling the method ComputeLinks(). Each Link is oriented couple of
    Poly_CoherentNode (directed to the ascending Node index). It refers two connected triangulated
    Nodes - on the left and on the right, therefore a Poly_CoherentLink instance refers the full set
    of nodes that constitute a couple of connected Triangles. A boundary Link has either the first
    (left) or the second (right) connected node index equal to -1.

    When the array of Links is created, all subsequent calls to AddTriangle and RemoveTriangle try to
    preserve the connectivity Triangle-Link in addition to the connectivity Triangle-Triangle.
    Particularly, new Links are created by method AddTriangle() and existing ones are removed by
    method RemoveTriangle(), in each case whenever necessary.

    Similarly to Poly_CoherentTriangle, a Link can be removed but not destroyed separately from
    others. Removed Link can be recogniosed using the method IsEmpty(). To destroy all Links, call
    the method ClearLinks(), this method also nullifies Link references in all Triangles.
    </li>
    All objects (except for free Nodes and empty Triangles and Links) can be visited by the
    corresponding Iterator. Direct access is provided only for Nodes (needed to resolve Node indexed
    commonly used as reference). Triangles and Links can be retrieved by their index only internally,
    the public API provides only references or pointers to C++ objects. If you need a direct access
    to Triangles and Links, you can subclass Poly_CoherentTriangulation and use the protected API for
    your needs.

    Memory management: All data objects are stored in NCollection_DynamicArray containers that prove
    to be efficient for the performance. In addition references to triangles are stored in ring
    lists, with an instance of such list per Poly_CoherentNode. These lists are allocated in a memory
    allocator that is provided in the constructor of Poly_CoherentTriangulation. By default the
    standard OCCT allocator (aka NCollection_BaseAllocator) is used. But if you need to increase the
    performance you can use NCollection_IncAllocator instead.
    </ul>
    """

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator = None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theTriangulation: Poly_Triangulation, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator = None) -> None:
        """
        Constructor. It does not create Links, you should call ComputeLinks
        following this constructor if you need these links.
        """

    @overload
    def __init__(self, theOther: Poly_CoherentTriangulation) -> None: ...

    class IteratorOfTriangle(NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentTriangle):
        """
        Subclass Iterator - allows to iterate all triangles skipping those that
        have been removed.
        """

        @overload
        def __init__(self, theTri: Poly_CoherentTriangulation) -> None:
            """Constructor"""

        @overload
        def __init__(self, theOther: Poly_CoherentTriangulation.IteratorOfTriangle) -> None: ...

        def Next(self) -> None:
            """Make step"""

    class IteratorOfNode(NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentNode):
        """
        Subclass Iterator - allows to iterate all nodes skipping the free ones.
        """

        @overload
        def __init__(self, theTri: Poly_CoherentTriangulation) -> None:
            """Constructor"""

        @overload
        def __init__(self, theOther: Poly_CoherentTriangulation.IteratorOfNode) -> None: ...

        def Next(self) -> None:
            """Make step"""

    class IteratorOfLink(NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentLink):
        """Subclass Iterator - allows to iterate all links skipping invalid ones."""

        @overload
        def __init__(self, theTri: Poly_CoherentTriangulation) -> None:
            """Constructor"""

        @overload
        def __init__(self, theOther: Poly_CoherentTriangulation.IteratorOfLink) -> None: ...

        def Next(self) -> None:
            """Make step"""

    class TwoIntegers:
        """Couple of integer indices (used in RemoveDegenerated())."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, i0: int, i1: int) -> None: ...

        @overload
        def __init__(self, theOther: Poly_CoherentTriangulation.TwoIntegers) -> None: ...

    def GetTriangulation(self) -> Poly_Triangulation:
        """Create an instance of Poly_Triangulation from this object."""

    def RemoveDegenerated(self, theTol: float, pLstRemovedNode: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_CoherentTriangulation.TwoIntegers] = None) -> bool:
        """
        Find and remove degenerated triangles in Triangulation.
        @param theTol
        Tolerance for the degeneration case. If any two nodes of a triangle have
        the distance less than this tolerance, this triangle is considered
        degenerated and therefore removed by this method.
        @param pLstRemovedNode
        Optional parameter. If defined, then it will receive the list of arrays
        where the first number is the index of removed node and the second -
        the index of remaining node to which the mesh was reconnected.
        """

    def GetFreeNodes(self, lstNodes: nanoocp.NCollection.NCollection_List[int]) -> bool:
        """
        Create a list of free nodes. These nodes may appear as a result of any
        custom mesh decimation or RemoveDegenerated() call. This analysis is
        necessary if you support additional data structures based on the
        triangulation (e.g., edges on the surface boundary).
        @param lstNodes
        <tt>[out]</tt> List that receives the indices of free nodes.
        """

    def MaxNode(self) -> int:
        """Query the index of the last node in the triangulation"""

    def MaxTriangle(self) -> int:
        """Query the index of the last triangle in the triangulation"""

    def SetDeflection(self, theDefl: float) -> None:
        """Set the Deflection value as the parameter of the given triangulation."""

    def Deflection(self) -> float:
        """
        Query the Deflection parameter (default value 0. -- if never initialized)
        """

    def SetNode(self, thePnt: nanoocp.gp.gp_XYZ, iN: int = -1) -> int:
        """
        Initialize a node
        @param thePoint
        3D Coordinates of the node.
        @param iN
        Index of the node. If negative (default), the node is added to the
        end of the current array of nodes.
        @return
        Index of the added node.
        """

    def Node(self, i: int) -> Poly_CoherentNode:
        """Get the node at the given index 'i'."""

    def ChangeNode(self, i: int) -> Poly_CoherentNode:
        """Get the node at the given index 'i'."""

    def NNodes(self) -> int:
        """
        Query the total number of active nodes (i.e. nodes used by 1 or more
        triangles)
        """

    def Triangle(self, i: int) -> Poly_CoherentTriangle:
        """Get the triangle at the given index 'i'."""

    def NTriangles(self) -> int:
        """
        Query the total number of active triangles (i.e. triangles that refer
        nodes, non-empty ones)
        """

    def NLinks(self) -> int:
        """Query the total number of active Links."""

    def RemoveTriangle(self, theTr: Poly_CoherentTriangle) -> bool:
        """Removal of a single triangle from the triangulation."""

    def RemoveLink(self, theLink: Poly_CoherentLink) -> None:
        """Removal of a single link from the triangulation."""

    def AddTriangle(self, iNode0: int, iNode1: int, iNode2: int) -> Poly_CoherentTriangle:
        """
        Add a triangle to the triangulation.
        @return
        Pointer to the added triangle instance or NULL if an error occurred.
        """

    def ReplaceNodes(self, theTriangle: Poly_CoherentTriangle, iNode0: int, iNode1: int, iNode2: int) -> bool:
        """
        Replace nodes in the given triangle.
        @return
        True if operation succeeded.
        """

    def AddLink(self, theTri: Poly_CoherentTriangle, theConn: int) -> Poly_CoherentLink:
        """
        Add a single link to triangulation, based on a triangle and its side index.
        This method does not check for coincidence with already present links.
        @param theTri
        Triangle that contains the link to be added.
        @param theConn
        Index of the side (i.e., 0, 1 0r 2) defining the added link.
        """

    def ComputeLinks(self) -> int:
        """(Re)Calculate all links in this Triangulation."""

    def ClearLinks(self) -> None:
        """Clear all Links data from the Triangulation data."""

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator:
        """
        Query the allocator of elements, this allocator can be used for other
        objects
        """

    def Clone(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator) -> Poly_CoherentTriangulation:
        """Create a copy of this Triangulation, using the given allocator."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentTriangle:
    """
    Helper class that allows to use NCollection iterators as STL iterators.
    NCollection iterator can be extended to STL iterator of any category by
    adding necessary methods: STL forward iterator requires IsEqual method,
    STL bidirectional iterator requires Previous method, and STL random access
    iterator requires Offset and Differ methods. See NCollection_DynamicArray as
    example of declaring custom STL iterators.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentTriangle) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentTriangle]) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentTriangle], theOther: "NCollection_DynamicArray<Poly_CoherentTriangle>::DynamicIterator<false>") -> None: ...

    @overload
    def Init(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentTriangle]) -> None: ...

    @overload
    def Init(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentTriangle]) -> None: ...

    def More(self) -> bool: ...

    @overload
    def Initialize(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentTriangle]) -> None: ...

    @overload
    def Initialize(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentTriangle]) -> None: ...

    def ValueIter(self) -> "NCollection_DynamicArray<Poly_CoherentTriangle>::DynamicIterator<false>": ...

    def ChangeValueIter(self) -> "NCollection_DynamicArray<Poly_CoherentTriangle>::DynamicIterator<false>": ...

    def EndIter(self) -> "NCollection_DynamicArray<Poly_CoherentTriangle>::DynamicIterator<false>": ...

    def ChangeEndIter(self) -> "NCollection_DynamicArray<Poly_CoherentTriangle>::DynamicIterator<false>": ...

    def Next(self) -> None: ...

    def Value(self) -> Poly_CoherentTriangle: ...

    def ChangeValue(self) -> Poly_CoherentTriangle: ...

    def __eq__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentTriangle) -> bool: ...

    def __ne__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentTriangle) -> bool: ...

class NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentNode:
    """
    Helper class that allows to use NCollection iterators as STL iterators.
    NCollection iterator can be extended to STL iterator of any category by
    adding necessary methods: STL forward iterator requires IsEqual method,
    STL bidirectional iterator requires Previous method, and STL random access
    iterator requires Offset and Differ methods. See NCollection_DynamicArray as
    example of declaring custom STL iterators.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentNode) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentNode]) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentNode], theOther: "NCollection_DynamicArray<Poly_CoherentNode>::DynamicIterator<false>") -> None: ...

    @overload
    def Init(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentNode]) -> None: ...

    @overload
    def Init(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentNode]) -> None: ...

    def More(self) -> bool: ...

    @overload
    def Initialize(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentNode]) -> None: ...

    @overload
    def Initialize(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentNode]) -> None: ...

    def ValueIter(self) -> "NCollection_DynamicArray<Poly_CoherentNode>::DynamicIterator<false>": ...

    def ChangeValueIter(self) -> "NCollection_DynamicArray<Poly_CoherentNode>::DynamicIterator<false>": ...

    def EndIter(self) -> "NCollection_DynamicArray<Poly_CoherentNode>::DynamicIterator<false>": ...

    def ChangeEndIter(self) -> "NCollection_DynamicArray<Poly_CoherentNode>::DynamicIterator<false>": ...

    def Next(self) -> None: ...

    def Value(self) -> Poly_CoherentNode: ...

    def ChangeValue(self) -> Poly_CoherentNode: ...

    def __eq__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentNode) -> bool: ...

    def __ne__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentNode) -> bool: ...

class NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentLink:
    """
    Helper class that allows to use NCollection iterators as STL iterators.
    NCollection iterator can be extended to STL iterator of any category by
    adding necessary methods: STL forward iterator requires IsEqual method,
    STL bidirectional iterator requires Previous method, and STL random access
    iterator requires Offset and Differ methods. See NCollection_DynamicArray as
    example of declaring custom STL iterators.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentLink) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentLink]) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentLink], theOther: "NCollection_DynamicArray<Poly_CoherentLink>::DynamicIterator<false>") -> None: ...

    @overload
    def Init(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentLink]) -> None: ...

    @overload
    def Init(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentLink]) -> None: ...

    def More(self) -> bool: ...

    @overload
    def Initialize(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentLink]) -> None: ...

    @overload
    def Initialize(self, theList: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Poly.Poly_CoherentLink]) -> None: ...

    def ValueIter(self) -> "NCollection_DynamicArray<Poly_CoherentLink>::DynamicIterator<false>": ...

    def ChangeValueIter(self) -> "NCollection_DynamicArray<Poly_CoherentLink>::DynamicIterator<false>": ...

    def EndIter(self) -> "NCollection_DynamicArray<Poly_CoherentLink>::DynamicIterator<false>": ...

    def ChangeEndIter(self) -> "NCollection_DynamicArray<Poly_CoherentLink>::DynamicIterator<false>": ...

    def Next(self) -> None: ...

    def Value(self) -> Poly_CoherentLink: ...

    def ChangeValue(self) -> Poly_CoherentLink: ...

    def __eq__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentLink) -> bool: ...

    def __ne__(self, theOther: NCollection_Iterator__NCollection_DynamicArray__Poly_CoherentLink) -> bool: ...

class Poly_Connect:
    """
    Provides an algorithm to explore, inside a triangulation, the
    adjacency data for a node or a triangle.
    Adjacency data for a node consists of triangles which
    contain the node.
    Adjacency data for a triangle consists of:
    -   the 3 adjacent triangles which share an edge of the triangle,
    -   and the 3 nodes which are the other nodes of these adjacent triangles.
    Example
    Inside a triangulation, a triangle T
    has nodes n1, n2 and n3.
    It has adjacent triangles AT1, AT2 and AT3 where:
    - AT1 shares the nodes n2 and n3,
    - AT2 shares the nodes n3 and n1,
    - AT3 shares the nodes n1 and n2.
    It has adjacent nodes an1, an2 and an3 where:
    - an1 is the third node of AT1,
    - an2 is the third node of AT2,
    - an3 is the third node of AT3.
    So triangle AT1 is composed of nodes n2, n3 and an1.
    There are two ways of using this algorithm.
    -   From a given node you can look for one triangle that
    passes through the node, then look for the triangles
    adjacent to this triangle, then the adjacent nodes. You
    can thus explore the triangulation step by step (functions
    Triangle, Triangles and Nodes).
    -   From a given node you can look for all the triangles
    that pass through the node (iteration method, using the
    functions Initialize, More, Next and Value).
    A Connect object can be seen as a tool which analyzes a
    triangulation and translates it into a series of triangles. By
    doing this, it provides an interface with other tools and
    applications working on basic triangles, and which do not
    work directly with a Poly_Triangulation.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an uninitialized algorithm."""

    @overload
    def __init__(self, theTriangulation: Poly_Triangulation) -> None:
        """
        Constructs an algorithm to explore the adjacency data of
        nodes or triangles for the triangulation T.
        """

    @overload
    def __init__(self, theOther: Poly_Connect) -> None: ...

    def Load(self, theTriangulation: Poly_Triangulation) -> None:
        """
        Initialize the algorithm to explore the adjacency data of
        nodes or triangles for the triangulation theTriangulation.
        """

    def Triangulation(self) -> Poly_Triangulation:
        """Returns the triangulation analyzed by this tool."""

    def Triangle(self, N: int) -> int:
        """
        Returns the index of a triangle containing the node at
        index N in the nodes table specific to the triangulation analyzed by this tool
        """

    def Triangles(self, T: int) -> tuple[int, int, int]:
        """
        Returns in t1, t2 and t3, the indices of the 3 triangles
        adjacent to the triangle at index T in the triangles table
        specific to the triangulation analyzed by this tool.
        Warning
        Null indices are returned when there are fewer than 3
        adjacent triangles.
        """

    def Nodes(self, T: int) -> tuple[int, int, int]:
        """
        Returns, in n1, n2 and n3, the indices of the 3 nodes
        adjacent to the triangle referenced at index T in the
        triangles table specific to the triangulation analyzed by this tool.
        Warning
        Null indices are returned when there are fewer than 3 adjacent nodes.
        """

    def Initialize(self, N: int) -> None:
        """
        Initializes an iterator to search for all the triangles
        containing the node referenced at index N in the nodes
        table, for the triangulation analyzed by this tool.
        The iterator is managed by the following functions:
        -   More, which checks if there are still elements in the iterator
        -   Next, which positions the iterator on the next element
        -   Value, which returns the current element.
        The use of such an iterator provides direct access to the
        triangles around a particular node, i.e. it avoids iterating on
        all the component triangles of a triangulation.
        Example
        Poly_Connect C(Tr);
        for
        (C.Initialize(n1);C.More();C.Next())
        {
        t = C.Value();
        }
        """

    def More(self) -> bool:
        """
        Returns true if there is another element in the iterator
        defined with the function Initialize (i.e. if there is another
        triangle containing the given node).
        """

    def Next(self) -> None:
        """
        Advances the iterator defined with the function Initialize to
        access the next triangle.
        Note: There is no action if the iterator is empty (i.e. if the
        function More returns false).-
        """

    def Value(self) -> int:
        """
        Returns the index of the current triangle to which the
        iterator, defined with the function Initialize, points. This is
        an index in the triangles table specific to the triangulation
        analyzed by this tool
        """

class Poly_MakeLoops:
    """
    Make loops from a set of connected links. A link is represented by
    a pair of integer indices of nodes.
    """

    class LinkFlag(enum.IntEnum):
        """Orientation flags that can be attached to a link"""

        LF_None = 0

        LF_Fwd = 1

        LF_Rev = 2

        LF_Both = 3

        LF_Reversed = 4

    class ResultCode(enum.IntEnum):
        RC_LoopsDone = 1

        RC_HangingLinks = 2

        RC_Failure = 4

    class Link:
        """The Link structure"""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theNode1: int, theNode2: int) -> None: ...

        @overload
        def __init__(self, theOther: Poly_MakeLoops.Link) -> None: ...

        def Reverse(self) -> None: ...

        def IsReversed(self) -> bool: ...

        def Nullify(self) -> None: ...

        def IsNull(self) -> bool: ...

        def __eq__(self, theOther: Poly_MakeLoops.Link) -> bool: ...

        def __hash__(self) -> int: ...

        @property
        def node1(self) -> int: ...

        @node1.setter
        def node1(self, arg: int, /) -> None: ...

        @property
        def node2(self) -> int: ...

        @node2.setter
        def node2(self, arg: int, /) -> None: ...

        @property
        def flags(self) -> int: ...

        @flags.setter
        def flags(self, arg: int, /) -> None: ...

    class Hasher:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: Poly_MakeLoops.Hasher) -> None: ...

        @overload
        def __call__(self, theLink: Poly_MakeLoops.Link) -> int: ...

        @overload
        def __call__(self, theLink1: Poly_MakeLoops.Link, theLink2: Poly_MakeLoops.Link) -> bool: ...

    class Helper:
        """The abstract helper class"""

        def GetAdjacentLinks(self, theNode: int) -> nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_MakeLoops.Link]:
            """returns the links adjacent to the given node"""

        def OnAddLink(self, arg0: int, arg1: Poly_MakeLoops.Link) -> None:
            """hook function called from AddLink in _DEBUG mode"""

    class HeapOfInteger:
        """
        This class implements a heap of integers. The most effective usage
        of it is first to add there all items, and then get top item and remove
        any items till it becomes empty.
        """

        @overload
        def __init__(self, theNbPreAllocated: int = 1) -> None: ...

        @overload
        def __init__(self, theOther: Poly_MakeLoops.HeapOfInteger) -> None: ...

        def Clear(self) -> None: ...

        def Add(self, theValue: int) -> None: ...

        def Top(self) -> int: ...

        def Contains(self, theValue: int) -> bool: ...

        def Remove(self, theValue: int) -> None: ...

        def IsEmpty(self) -> bool: ...

    def Reset(self, theHelper: Poly_MakeLoops.Helper, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator = None) -> None:
        """It is to reset the algorithm to the initial state."""

    def AddLink(self, theLink: Poly_MakeLoops.Link) -> None:
        """
        Adds a link to the set. theOrient defines which orientations of the link
        are allowed.
        """

    def ReplaceLink(self, theLink: Poly_MakeLoops.Link, theNewLink: Poly_MakeLoops.Link) -> None:
        """Replace one link with another (e.g. to change order of nodes)"""

    def SetLinkOrientation(self, theLink: Poly_MakeLoops.Link, theOrient: Poly_MakeLoops.LinkFlag) -> Poly_MakeLoops.LinkFlag:
        """
        Set a new value of orientation of a link already added earlier.
        It can be used with LF_None to exclude the link from consideration.
        Returns the old value of orientation.
        """

    def FindLink(self, theLink: Poly_MakeLoops.Link) -> Poly_MakeLoops.Link:
        """Find the link stored in algo by value"""

    def Perform(self) -> int:
        """Does the work. Returns the collection of result codes"""

    def GetNbLoops(self) -> int:
        """Returns the number of loops in the result"""

    def GetLoop(self, theIndex: int) -> nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_MakeLoops.Link]:
        """Returns the loop of the given index"""

    def GetNbHanging(self) -> int:
        """Returns the number of detected hanging chains"""

    def GetHangingLinks(self, theLinks: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_MakeLoops.Link]) -> None:
        """Fills in the list of hanging links"""

class Poly_MakeLoops3D(Poly_MakeLoops):
    @overload
    def __init__(self, theHelper: Poly_MakeLoops3D.Helper, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """
        Constructor. If helper is NULL then the algorithm will
        probably return a wrong result
        """

    @overload
    def __init__(self, theOther: Poly_MakeLoops3D) -> None: ...

    class Helper(Poly_MakeLoops.Helper):
        """The abstract helper class"""

        def GetFirstTangent(self, theLink: Poly_MakeLoops.Link, theDir: nanoocp.gp.gp_Dir) -> bool:
            """returns the tangent vector at the first node of a link"""

        def GetLastTangent(self, theLink: Poly_MakeLoops.Link, theDir: nanoocp.gp.gp_Dir) -> bool:
            """returns the tangent vector at the last node of a link"""

        def GetNormal(self, theNode: int, theDir: nanoocp.gp.gp_Dir) -> bool:
            """returns the normal to the surface at a given node"""

class Poly_MakeLoops2D(Poly_MakeLoops):
    @overload
    def __init__(self, theLeftWay: bool, theHelper: Poly_MakeLoops2D.Helper, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator) -> None:
        """
        Constructor. If helper is NULL then the algorithm will
        probably return a wrong result
        """

    @overload
    def __init__(self, theOther: Poly_MakeLoops2D) -> None: ...

    class Helper(Poly_MakeLoops.Helper):
        """The abstract helper class"""

        def GetFirstTangent(self, theLink: Poly_MakeLoops.Link, theDir: nanoocp.gp.gp_Dir2d) -> bool:
            """returns the tangent vector at the first node of a link"""

        def GetLastTangent(self, theLink: Poly_MakeLoops.Link, theDir: nanoocp.gp.gp_Dir2d) -> bool:
            """returns the tangent vector at the last node of a link"""

class Poly_MergeNodesTool(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary tool for merging triangulation nodes for visualization purposes.
    Tool tries to merge all nodes within input triangulation, but split the ones on sharp corners at
    specified angle.
    """

    def __init__(self, theSmoothAngle: float, theMergeTolerance: float = 0.0, theNbFacets: int = -1) -> None:
        """
        Constructor
        @param[in] theSmoothAngle smooth angle in radians or 0.0 to disable merging by angle
        @param[in] theMergeTolerance node merging maximum distance
        @param[in] theNbFacets estimated number of facets for map preallocation
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def MergeNodes(theTris: Poly_Triangulation, theTrsf: nanoocp.gp.gp_Trsf, theToReverse: bool, theSmoothAngle: float, theMergeTolerance: float = 0.0, theToForce: bool = True) -> Poly_Triangulation:
        """
        Merge nodes of existing mesh and return the new mesh.
        @param[in] theTris triangulation to add
        @param[in] theTrsf transformation to apply
        @param[in] theToReverse reverse triangle nodes order
        @param[in] theSmoothAngle merge angle in radians
        @param[in] theMergeTolerance linear merge tolerance
        @param[in] theToForce return merged triangulation even if it's statistics is equal to input
        one
        @return merged triangulation or NULL on no result
        """

    def MergeTolerance(self) -> float:
        """
        Return merge tolerance; 0.0 by default (only 3D points with exactly matching coordinates are
        merged).
        """

    def SetMergeTolerance(self, theTolerance: float) -> None:
        """Set merge tolerance."""

    def MergeAngle(self) -> float:
        """
        Return merge angle in radians; 0.0 by default (normals with non-exact directions are not
        merged).
        """

    def SetMergeAngle(self, theAngleRad: float) -> None:
        """Set merge angle."""

    def ToMergeOpposite(self) -> bool:
        """
        Return TRUE if nodes with opposite normals should be merged; FALSE by default.
        """

    def SetMergeOpposite(self, theToMerge: bool) -> None:
        """Set if nodes with opposite normals should be merged."""

    def SetUnitFactor(self, theUnitFactor: float) -> None:
        """Setup unit factor."""

    def ToDropDegenerative(self) -> bool:
        """
        Return TRUE if degenerate elements should be discarded; TRUE by default.
        """

    def SetDropDegenerative(self, theToDrop: bool) -> None:
        """Set if degenerate elements should be discarded."""

    def ToMergeElems(self) -> bool:
        """Return TRUE if equal elements should be filtered; FALSE by default."""

    def SetMergeElems(self, theToMerge: bool) -> None:
        """Set if equal elements should be filtered."""

    def computeTriNormal(self) -> nanoocp.BVH.BVH_Vec3f:
        """Compute normal for the mesh element."""

    def AddTriangulation(self, theTris: Poly_Triangulation, theTrsf: nanoocp.gp.gp_Trsf = ..., theToReverse: bool = False) -> None:
        """
        Add another triangulation to created one.
        @param[in] theTris triangulation to add
        @param[in] theTrsf transformation to apply
        @param[in] theToReverse reverse triangle nodes order
        """

    def Result(self) -> Poly_Triangulation:
        """
        Prepare and return result triangulation (temporary data will be truncated to result size).
        """

    def AddElement(self, theElemNodes: nanoocp.gp.gp_XYZ, theNbNodes: int) -> None:
        """
        Add new triangle or quad.
        @param[in] theElemNodes element nodes
        @param[in] theNbNodes number of element nodes, should be 3 or 4
        """

    def ChangeElementNode(self, theIndex: int) -> nanoocp.gp.gp_XYZ:
        """
        Change node coordinates of element to be pushed.
        @param[in] theIndex node index within current element, in 0..3 range
        """

    def PushLastElement(self, theNbNodes: int) -> None:
        """Add new triangle or quad with nodes specified by ChangeElementNode()."""

    def PushLastTriangle(self) -> None:
        """Add new triangle with nodes specified by ChangeElementNode()."""

    def PushLastQuad(self) -> None:
        """Add new quad with nodes specified by ChangeElementNode()."""

    def ElementNodeIndex(self, theIndex: int) -> int:
        """Return current element node index defined by PushLastElement()."""

    def NbNodes(self) -> int:
        """Return number of nodes."""

    def NbElements(self) -> int:
        """Return number of elements."""

    def NbDegenerativeElems(self) -> int:
        """Return number of discarded degenerate elements."""

    def NbMergedElems(self) -> int:
        """Return number of merged equal elements."""

    def ChangeOutput(self) -> Poly_Triangulation:
        """
        Setup output triangulation for modifications.
        When set to NULL, the tool could be used as a merge map for filling in external mesh
        structure.
        """

class Poly_Polygon2D(nanoocp.Standard.Standard_Transient):
    """
    Provides a polygon in 2D space (for example, in the
    parametric space of a surface). It is generally an
    approximate representation of a curve.
    A Polygon2D is defined by a table of nodes. Each node is
    a 2D point. If the polygon is closed, the point of closure is
    repeated at the end of the table of nodes.
    """

    @overload
    def __init__(self, theNbNodes: int) -> None:
        """Constructs a 2D polygon with specified number of nodes."""

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """Constructs a 2D polygon defined by the table of points, <Nodes>."""

    @overload
    def __init__(self, theOther: Poly_Polygon2D) -> None: ...

    def Copy(self) -> Poly_Polygon2D:
        """Creates a copy of current polygon."""

    @overload
    def Deflection(self) -> float:
        """
        Returns the deflection of this polygon.
        Deflection is used in cases where the polygon is an
        approximate representation of a curve. Deflection
        represents the maximum distance permitted between any
        point on the curve and the corresponding point on the polygon.
        By default the deflection value is equal to 0. An algorithm
        using this 2D polygon with a deflection value equal to 0
        considers that it is working with a true polygon and not with
        an approximate representation of a curve. The Deflection
        function is used to modify the deflection value of this polygon.
        The deflection value can be used by any algorithm working with 2D polygons.
        For example:
        -   An algorithm may use a unique deflection value for all
        its polygons. In this case it is not necessary to use the
        Deflection function.
        -   Or an algorithm may want to attach a different
        deflection to each polygon. In this case, the Deflection
        function is used to set a value on each polygon, and
        later to fetch the value.
        """

    @overload
    def Deflection(self, theDefl: float) -> None:
        """Sets the deflection of this polygon."""

    def NbNodes(self) -> int:
        """
        Returns the number of nodes in this polygon.
        Note: If the polygon is closed, the point of closure is
        repeated at the end of its table of nodes. Thus, on a closed
        triangle, the function NbNodes returns 4.
        """

    def Nodes(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns the table of nodes for this polygon."""

    def ChangeNodes(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns the table of nodes for this polygon."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Poly_Polygon3D(nanoocp.Standard.Standard_Transient):
    """
    This class Provides a polygon in 3D space. It is generally an approximate representation of a
    curve. A Polygon3D is defined by a table of nodes. Each node is a 3D point. If the polygon is
    closed, the point of closure is repeated at the end of the table of nodes. If the polygon is an
    approximate representation of a curve, you can associate with each of its nodes the value of the
    parameter of the corresponding point on the curve.
    """

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """Constructs a 3D polygon defined by the table of points, Nodes."""

    @overload
    def __init__(self, theNbNodes: int, theHasParams: bool) -> None:
        """Constructs a 3D polygon with specific number of nodes."""

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Parameters: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Constructs a 3D polygon defined by
        the table of points, Nodes, and the parallel table of
        parameters, Parameters, where each value of the table
        Parameters is the parameter of the corresponding point
        on the curve approximated by the constructed polygon.
        Warning
        Both the Nodes and Parameters tables must have the
        same bounds. This property is not checked at construction time.
        """

    @overload
    def __init__(self, theOther: Poly_Polygon3D) -> None: ...

    def Copy(self) -> Poly_Polygon3D:
        """Creates a copy of current polygon"""

    @overload
    def Deflection(self) -> float:
        """Returns the deflection of this polygon"""

    @overload
    def Deflection(self, theDefl: float) -> None:
        """
        Sets the deflection of this polygon. See more on deflection in Poly_Polygon2D
        """

    def NbNodes(self) -> int:
        """
        Returns the number of nodes in this polygon.
        Note: If the polygon is closed, the point of closure is
        repeated at the end of its table of nodes. Thus, on a closed
        triangle the function NbNodes returns 4.
        """

    def Nodes(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """Returns the table of nodes for this polygon."""

    def ChangeNodes(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """Returns the table of nodes for this polygon."""

    def HasParameters(self) -> bool:
        """
        Returns the table of the parameters associated with each node in this polygon.
        HasParameters function checks if parameters are associated with the nodes of this polygon.
        """

    def Parameters(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns true if parameters are associated with the nodes
        in this polygon.
        """

    def ChangeParameters(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns the table of the parameters associated with each node in this polygon.
        ChangeParameters function returns the array as shared.
        Therefore if the table is selected by reference you can, by simply modifying it,
        directly modify the data structure of this polygon.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Poly_PolygonOnTriangulation(nanoocp.Standard.Standard_Transient):
    """
    This class provides a polygon in 3D space, based on the triangulation
    of a surface. It may be the approximate representation of a
    curve on the surface, or more generally the shape.
    A PolygonOnTriangulation is defined by a table of
    nodes. Each node is an index in the table of nodes specific
    to a triangulation, and represents a point on the surface. If
    the polygon is closed, the index of the point of closure is
    repeated at the end of the table of nodes.
    If the polygon is an approximate representation of a curve
    on a surface, you can associate with each of its nodes the
    value of the parameter of the corresponding point on the
    curve.represents a 3d Polygon
    """

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Constructs a 3D polygon on the triangulation of a shape,
        defined by the table of nodes, <Nodes>.
        """

    @overload
    def __init__(self, theNbNodes: int, theHasParams: bool) -> None:
        """
        Constructs a 3D polygon on the triangulation of a shape with specified size of nodes.
        """

    @overload
    def __init__(self, Nodes: nanoocp.NCollection.NCollection_Array1[int], Parameters: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Constructs a 3D polygon on the triangulation of a shape, defined by:
        -   the table of nodes, Nodes, and the table of parameters, <Parameters>.
        where:
        -   a node value is an index in the table of nodes specific
        to an existing triangulation of a shape
        -   and a parameter value is the value of the parameter of
        the corresponding point on the curve approximated by
        the constructed polygon.
        Warning
        The tables Nodes and Parameters must be the same size.
        This property is not checked at construction time.
        """

    @overload
    def __init__(self, theOther: Poly_PolygonOnTriangulation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Copy(self) -> Poly_PolygonOnTriangulation:
        """Creates a copy of current polygon"""

    @overload
    def Deflection(self) -> float:
        """Returns the deflection of this polygon"""

    @overload
    def Deflection(self, theDefl: float) -> None:
        """
        Sets the deflection of this polygon.
        See more on deflection in Poly_Polygones2D.
        """

    def NbNodes(self) -> int:
        """
        Returns the number of nodes for this polygon.
        Note: If the polygon is closed, the point of closure is
        repeated at the end of its table of nodes. Thus, on a closed
        triangle, the function NbNodes returns 4.
        """

    def Node(self, theIndex: int) -> int:
        """Returns node at the given index."""

    def ChangeNodeArray(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns mutable node-index array."""

    def SetNode(self, theIndex: int, theNode: int) -> None:
        """Sets node at the given index."""

    def HasParameters(self) -> bool:
        """
        Returns true if parameters are associated with the nodes in this polygon.
        """

    def Parameter(self, theIndex: int) -> float:
        """Returns parameter at the given index."""

    def SetParameter(self, theIndex: int, theValue: float) -> None:
        """Sets parameter at the given index."""

    def ChangeParameterArray(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns mutable parameter array."""

    def SetParameters(self, theParameters: nanoocp.NCollection.NCollection_HArray1[float]) -> None:
        """
        Sets the table of the parameters associated with each node in this polygon.
        Raises exception if array size doesn't much number of polygon nodes.
        """

    def Nodes(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """
        Returns the table of nodes for this polygon.
        A node value is an index in the table of nodes specific to an existing triangulation of a
        shape.
        """

    def Parameters(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the table of the parameters associated with each node in this polygon.
        Warning! Use the function HasParameters to check if parameters are associated with the nodes
        in this polygon.
        """

class Poly_TriangulationParameters(nanoocp.Standard.Standard_Transient):
    """Represents initial set of parameters triangulation is built for."""

    @overload
    def __init__(self, theDeflection: float = -1.0, theAngle: float = -1.0, theMinSize: float = -1.0) -> None:
        """
        Constructor.
        Initializes object with the given parameters.
        @param theDeflection linear deflection
        @param theAngle angular deflection
        @param theMinSize minimum size
        """

    @overload
    def __init__(self, theOther: Poly_TriangulationParameters) -> None: ...

    def Copy(self) -> Poly_TriangulationParameters:
        """Creates a copy of current triangulation parameters."""

    def HasDeflection(self) -> bool:
        """Returns true if linear deflection is defined."""

    def HasAngle(self) -> bool:
        """Returns true if angular deflection is defined."""

    def HasMinSize(self) -> bool:
        """Returns true if minimum size is defined."""

    def Deflection(self) -> float:
        """Returns linear deflection or -1 if undefined."""

    def Angle(self) -> float:
        """Returns angular deflection or -1 if undefined."""

    def MinSize(self) -> float:
        """Returns minimum size or -1 if undefined."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Poly
Poly_Array1OfTriangle = nanoocp.NCollection.NCollection_Array1[nanoocp.Poly.Poly_Triangle]
Poly_HArray1OfTriangle = nanoocp.NCollection.NCollection_HArray1[nanoocp.Poly.Poly_Triangle]
Poly_ListOfTriangulation = nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangulation]
