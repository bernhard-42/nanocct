"""OCCT package Select3D (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.BVH
from nanoocp.BVH import BVH_Builder3d as Select3D_BVHBuilder3d
import nanoocp.Bnd
from nanoocp.Bnd import BVH_Box__double__3 as Select3D_BndBox3d
import nanoocp.Geom
import nanoocp.Graphic3d
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.SelectBasics
import nanoocp.SelectMgr
import nanoocp.Standard
import nanoocp.TColStd
import nanoocp.TopLoc
import nanoocp.gp
import nanoocp.Select3D


class Select3D_TypeOfSensitivity(enum.IntEnum):
    """
    Provides values for type of sensitivity in 3D.
    These are used to specify whether it is the interior,
    the boundary, or the exterior of a 3D sensitive entity which is sensitive.
    """

    Select3D_TOS_INTERIOR = 0

    Select3D_TOS_BOUNDARY = 1

Select3D_TOS_INTERIOR: Select3D_TypeOfSensitivity = Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR

Select3D_TOS_BOUNDARY: Select3D_TypeOfSensitivity = Select3D_TypeOfSensitivity.Select3D_TOS_BOUNDARY

class Select3D_BVHIndexBuffer(nanoocp.Graphic3d.Graphic3d_Buffer):
    """Index buffer for BVH tree."""

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Select3D_BVHIndexBuffer) -> None: ...

    def HasPatches(self) -> bool: ...

    def Init(self, theNbElems: int, theHasPatches: bool) -> bool:
        """Allocates new empty index array"""

    def Index(self, theIndex: int) -> int:
        """Access index at specified position"""

    def PatchSize(self, theIndex: int) -> int:
        """Access index at specified position"""

    @overload
    def SetIndex(self, theIndex: int, theValue: int) -> None: ...

    @overload
    def SetIndex(self, theIndex: int, theValue: int, thePatchSize: int) -> None:
        """Change index at specified position"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Select3D_Pnt:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Select3D_Pnt) -> None: ...

    @property
    def x(self) -> float: ...

    @x.setter
    def x(self, arg: float, /) -> None: ...

    @property
    def y(self) -> float: ...

    @y.setter
    def y(self, arg: float, /) -> None: ...

    @property
    def z(self) -> float: ...

    @z.setter
    def z(self, arg: float, /) -> None: ...

class Select3D_PointData:
    def __init__(self, theNbPoints: int) -> None: ...

    @overload
    def SetPnt(self, theIndex: int, theValue: Select3D_Pnt) -> None: ...

    @overload
    def SetPnt(self, theIndex: int, theValue: nanoocp.gp.gp_Pnt) -> None: ...

    def Pnt(self, theIndex: int) -> Select3D_Pnt: ...

    def Pnt3d(self, theIndex: int) -> nanoocp.gp.gp_Pnt: ...

    def Size(self) -> int: ...

class Select3D_SensitiveEntity(nanoocp.Standard.Standard_Transient):
    """Abstract framework to define 3D sensitive entities."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def OwnerId(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """Returns pointer to owner of the entity"""

    def Set(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """Sets owner of the entity"""

    def SensitivityFactor(self) -> int:
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small
        sized entities.
        """

    def SetSensitivityFactor(self, theNewSens: int) -> None:
        """Allows to manage sensitivity of a particular sensitive entity"""

    def GetConnected(self) -> Select3D_SensitiveEntity:
        """
        Originally this method intended to return sensitive entity with new location aLocation,
        but currently sensitive entities do not hold a location,
        instead HasLocation() and Location() methods call corresponding entity owner's methods.
        Thus all entities returned by GetConnected() share the same location propagated from
        corresponding selectable object. You must redefine this function for any type of sensitive
        entity which can accept another connected sensitive entity.
        """

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Checks whether sensitive overlaps current selecting volume.
        Stores minimum depth, distance to center of geometry and closest point detected into
        thePickResult
        """

    def NbSubElements(self) -> int:
        """
        Returns the number of sub-entities or elements in sensitive entity.
        Is used to determine if entity is complex and needs to pre-build BVH at the creation of
        sensitive entity step or is light-weighted so the tree can be build on demand with
        unnoticeable delay.
        """

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of a sensitive with transformation applied"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of a sensitive with transformation applied"""

    def BVH(self) -> None:
        """Builds BVH tree for a sensitive if needed"""

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def Clear(self) -> None:
        """Clears up all resources and memory"""

    def HasInitLocation(self) -> bool:
        """
        Returns true if the shape corresponding to the entity has init location
        """

    def InvInitLocation(self) -> nanoocp.gp.gp_GTrsf:
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has
        init location set. Otherwise, returns identity matrix.
        """

    def TransformPersistence(self) -> nanoocp.Graphic3d.Graphic3d_TransformPers:
        """Return transformation persistence."""

    def SetTransformPersistence(self, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> None:
        """Set transformation persistence."""

    def Flipper(self) -> nanoocp.Graphic3d.Graphic3d_Flipper:
        """
        Return flipper metadata describing the runtime flip of the owning group, or null.
        """

    def SetFlippingOptions(self, theIsEnabled: bool, theRefPlane: nanoocp.gp.gp_Ax2) -> None:
        """
        Set flipping options. When enabled, creates a Graphic3d_Flipper for theRefPlane;
        otherwise clears the flipper.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitiveSet(Select3D_SensitiveEntity):
    """
    This class is base class for handling overlap detection of complex sensitive
    entities. It provides an interface for building BVH tree for some set of entities.
    Thereby, each iteration of overlap detection is a traverse of BVH tree in fact.
    To use speed-up hierarchical structure in a custom complex sensitive entity, it is
    necessary to make that custom entity a descendant of this class and organize sub-entities
    in some container which allows referencing to elements by index. Note that methods taking
    index as a parameter are used for BVH build and the range of given index is [0; Size() - 1].
    For example of usage see Select3D_SensitiveTriangulation.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def DefaultBVHBuilder() -> nanoocp.BVH.BVH_Builder3d:
        """Return global instance to default BVH builder."""

    @staticmethod
    def SetDefaultBVHBuilder(theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT
        thread-safe!).
        """

    def Size(self) -> int:
        """Returns the amount of sub-entities of the complex entity"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of sub-entity with index theIdx in sub-entity list
        """

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of sensitive entity index theIdx along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2"""

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Checks whether one or more entities of the set overlap current selecting volume.
        Implements the traverse of BVH tree built for the set
        """

    def BVH(self) -> None:
        """
        Builds BVH tree for sensitive set.
        Must be called manually to build BVH tree for any sensitive set
        in case if its content was initialized not in a constructor,
        but element by element
        """

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def SetBuilder(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Sets the method (builder) used to construct BVH."""

    def MarkDirty(self) -> None:
        """
        Marks BVH tree of the set as outdated. It will be rebuild
        at the next call of BVH()
        """

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the whole set.
        This method should be redefined in Select3D_SensitiveSet descendants
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the whole set.
        This method should be redefined in Select3D_SensitiveSet descendants
        """

    def Clear(self) -> None:
        """Destroys cross-reference to avoid memory leak"""

    def GetLeafNodeSize(self) -> int:
        """Returns a number of nodes in 1 BVH leaf"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitivePoly(Select3D_SensitiveSet):
    """
    Sensitive Entity to make a face selectable.
    In some cases this class can raise Standard_ConstructionError and
    Standard_OutOfRange exceptions from its member Select3D_PointData
    myPolyg.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theIsBVHEnabled: bool, theNbPnts: int = 6) -> None:
        """
        Constructs a sensitive curve or arc object defined by the
        owner theOwnerId, the theIsBVHEnabled flag, and the
        maximum number of points on the curve: theNbPnts.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theIsBVHEnabled: bool) -> None: ...

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, theIsBVHEnabled: bool) -> None:
        """
        Constructs a sensitive face object defined by the
        owner OwnerId, the array of points ThePoints, and
        the sensitivity type Sensitivity.
        The array of points is the outer polygon of the geometric face.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theCircle: nanoocp.gp.gp_Circ, theU1: float, theU2: float, theIsFilled: bool = False, theNbPnts: int = 12) -> None:
        """
        Constructs the sensitive arc object defined by the
        owner theOwnerId, the circle theCircle, the parameters theU1
        and theU2, the boolean theIsFilled and the number of points theNbPnts.
        theU1 and theU2 define the first and last points of the arc on theCircle.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the poly overlaps current selecting volume"""

    def NbSubElements(self) -> int:
        """Returns the amount of segments in poly"""

    def Points3D(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        Returns the 3D points of the array used at construction time.
        @return handle to array of 3D points
        """

    def Points3D__NCollection_HArray1__gp_Pnt(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        Points3D__NCollection_HArray1__gp_Pnt: the C++ overload Points3D(occ::handle<NCollection_HArray1<gp_Pnt>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use Points3D() returning handle by value instead

        Returns the 3D points of the array used at construction time via output parameter.
        @deprecated Use Points3D() returning handle by value instead.
        """

    def ArrayBounds(self) -> tuple[int, int]:
        """Return array bounds."""

    def GetPoint3d(self, thePntIdx: int) -> nanoocp.gp.gp_Pnt:
        """Return point."""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of a polygon. If location
        transformation is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the point set. If location transformation
        is set, it will be applied
        """

    def Size(self) -> int:
        """Returns the amount of segments of the poly"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of segment with index theIdx"""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of sensitive entity index theIdx in the vector along
        the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2 in the vector"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_InteriorSensitivePointSet(Select3D_SensitiveSet):
    """
    This class handles the selection of arbitrary point set with internal type of sensitivity.
    The main principle is to split the point set given onto planar convex polygons and search
    for the overlap with one or more of them through traverse of BVH tree.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """Splits the given point set thePoints onto planar convex polygons"""

    @overload
    def __init__(self, theOther: Select3D_InteriorSensitivePointSet) -> None: ...

    def GetPoints(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        Returns 3d coordinates of vertices of the whole point set.
        @return handle to array of 3D vertex coordinates
        """

    def GetPoints__NCollection_HArray1__gp_Pnt(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        GetPoints__NCollection_HArray1__gp_Pnt: the C++ overload GetPoints(occ::handle<NCollection_HArray1<gp_Pnt>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use GetPoints() returning handle by value instead

        Initializes the given array theHArrayOfPnt by 3d coordinates of vertices of the
        whole point set
        @deprecated Use GetPoints() returning handle by value instead.
        """

    def Size(self) -> int:
        """Returns the length of vector of planar convex polygons"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of planar convex polygon with index theIdx"""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of planar convex polygon with index
        theIdx in the vector along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2 in the vector"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the point set. If location
        transformation is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the point set. If location
        transformation is set, it will be applied
        """

    def NbSubElements(self) -> int:
        """Returns the amount of points in set"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Select3D_SensitiveBox(Select3D_SensitiveEntity):
    """A framework to define selection by a sensitive box."""

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Constructs a sensitive box object defined by the
        owner theOwnerId, and the box theBox.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theXMin: float, theYMin: float, theZMin: float, theXMax: float, theYMax: float, theZMax: float) -> None:
        """
        Constructs a sensitive box object defined by the
        owner theOwnerId, and the coordinates theXmin, theYMin, theZMin, theXMax, theYMax, theZMax.
        theXmin, theYMin and theZMin define the minimum point in
        the front lower left hand corner of the box,
        and theXMax, theYMax and theZMax define the maximum
        point in the back upper right hand corner of the box.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveBox) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NbSubElements(self) -> int:
        """Returns the amount of sub-entities in sensitive"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the box overlaps current selecting volume"""

    def Box(self) -> nanoocp.Bnd.Bnd_Box: ...

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the box. If location
        transformation is set, it will be applied
        """

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns coordinates of the box. If location
        transformation is set, it will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitiveCircle(Select3D_SensitiveEntity):
    """A framework to define sensitive 3D circles."""

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theCircle: nanoocp.gp.gp_Circ, theIsFilled: bool = False) -> None:
        """
        Constructs the sensitive circle object defined by the
        owner theOwnerId, the circle theCircle and the boolean theIsFilled.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theCircle: nanoocp.gp.gp_Circ, theIsFilled: bool, arg3: int) -> None:
        """
        Deprecated in OCCT: Deprecated constructor, theNbPnts parameter will be ignored

        Constructs the sensitive circle object defined by the
        owner theOwnerId, the circle theCircle, the boolean
        theIsFilled and the number of points theNbPnts.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveCircle) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the circle overlaps current selecting volume"""

    def GetConnected(self) -> Select3D_SensitiveEntity:
        """Returns a copy of this sensitive circle"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the circle.
        If location transformation is set, it will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Always returns false"""

    def NbSubElements(self) -> int:
        """Returns the amount of points"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of the circle with transformation applied"""

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """
        The transformation for gp::XOY() with center in gp::Origin(),
        it specifies the position and orientation of the circle.
        """

    def Circle(self) -> nanoocp.gp.gp_Circ:
        """Returns circle"""

    def Radius(self) -> float:
        """Returns circle radius"""

class Select3D_SensitiveCurve(Select3D_SensitivePoly):
    """
    A framework to define a sensitive 3D curve.
    In some cases this class can raise Standard_ConstructionError and
    Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theCurve: nanoocp.Geom.Geom_Curve | None, theNbPnts: int = 17) -> None:
        """
        Constructs a sensitive curve object defined by the
        owner theOwnerId, the curve theCurve, and the
        maximum number of points on the curve: theNbPnts.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None) -> None:
        """
        Constructs a sensitive curve object defined by the
        owner theOwnerId and the set of points ThePoints.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        Creation of Sensitive Curve from Points.
        Warning : This Method should disappear in the next version...
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetConnected(self) -> Select3D_SensitiveEntity:
        """Returns the copy of this"""

class Select3D_SensitiveCylinder(Select3D_SensitiveEntity):
    """A framework to define selection by a sensitive cylinder or cone."""

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool = False) -> None:
        """
        Constructs a sensitive cylinder object defined by the owner theOwnerId,
        @param[in] theBottomRad cylinder bottom radius
        @param[in] theTopRad    cylinder top radius
        @param[in] theHeight    cylinder height
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveCylinder) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the cylinder overlaps current selecting volume"""

    def GetConnected(self) -> Select3D_SensitiveEntity:
        """Returns the copy of this"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the cylinder.
        If location transformation is set, it will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Always returns false"""

    def NbSubElements(self) -> int:
        """Returns the amount of points"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of the cylinder with transformation applied"""

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """Returns cylinder transformation"""

    def TopRadius(self) -> float:
        """Returns cylinder top radius"""

    def BottomRadius(self) -> float:
        """Returns cylinder bottom radius"""

    def Height(self) -> float:
        """Returns cylinder height"""

    def IsHollow(self) -> bool:
        """Returns true if the cylinder is empty inside"""

class Select3D_SensitiveFace(Select3D_SensitiveEntity):
    """
    Sensitive Entity to make a face selectable.
    In some cases this class can raise Standard_ConstructionError and
    Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theType: Select3D_TypeOfSensitivity) -> None: ...

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, theType: Select3D_TypeOfSensitivity) -> None:
        """
        Constructs a sensitive face object defined by the
        owner theOwnerId, the array of points thePoints, and
        the sensitivity type theType.
        The array of points is the outer polygon of the geometric face.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveFace) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetPoints(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        Returns 3d coordinates of vertices of the face.
        @return handle to array of 3D vertex coordinates
        """

    def GetPoints__NCollection_HArray1__gp_Pnt(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        GetPoints__NCollection_HArray1__gp_Pnt: the C++ overload GetPoints(occ::handle<NCollection_HArray1<gp_Pnt>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use GetPoints() returning handle by value instead

        Initializes the given array theHArrayOfPnt by 3d
        coordinates of vertices of the face
        @deprecated Use GetPoints() returning handle by value instead.
        """

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the face overlaps current selecting volume"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the face. If location transformation
        is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the face. If location transformation
        is set, it will be applied
        """

    def BVH(self) -> None:
        """Builds BVH tree for the face"""

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def NbSubElements(self) -> int:
        """Returns the amount of sub-entities (points or planar convex polygons)"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitiveGroup(Select3D_SensitiveSet):
    """
    A framework to define selection of a sensitive group
    by a sensitive entity which is a set of 3D sensitive entities.
    Remark: 2 modes are possible for rectangle selection
    the group is considered selected
    1) when all the entities inside are selected in the rectangle
    2) only one entity inside is selected by the rectangle
    By default the "Match All entities" mode is set.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theIsMustMatchAll: bool = True) -> None:
        """
        Constructs an empty sensitive group object.
        This is a set of sensitive 3D entities. The sensitive
        entities will be defined using the function Add to fill
        the entity owner OwnerId. If MatchAll is false, nothing can be added.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theEntities: nanoocp.NCollection.NCollection_Sequence[nanoocp.Select3D.Select3D_SensitiveEntity], theIsMustMatchAll: bool = True) -> None:
        """
        Constructs a sensitive group object defined by the list
        TheList and the entity owner OwnerId. If MatchAll is false, nothing is done.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveGroup) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Entities(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Select3D.Select3D_SensitiveEntity]:
        """Gets group content"""

    def SubEntity(self, theIndex: int) -> Select3D_SensitiveEntity:
        """Access entity by index [1, NbSubElements()]."""

    def LastDetectedEntity(self) -> Select3D_SensitiveEntity:
        """Return last detected entity."""

    def LastDetectedEntityIndex(self) -> int:
        """Return index of last detected entity."""

    @overload
    def Add(self, theEntities: nanoocp.NCollection.NCollection_Sequence[nanoocp.Select3D.Select3D_SensitiveEntity]) -> None:
        """
        Adds the list of sensitive entities LL to the empty
        sensitive group object created at construction time.
        """

    @overload
    def Add(self, theSensitive: Select3D_SensitiveEntity | None) -> None:
        """
        Adds the sensitive entity aSensitive to the non-empty
        sensitive group object created at construction time.
        """

    def Remove(self, theSensitive: Select3D_SensitiveEntity | None) -> None: ...

    def Clear(self) -> None:
        """
        Removes all sensitive entities from the list used at the
        time of construction, or added using the function Add.
        """

    def IsIn(self, theSensitive: Select3D_SensitiveEntity | None) -> bool:
        """
        Returns true if the sensitive entity aSensitive is in
        the list used at the time of construction, or added using the function Add.
        """

    def SetMatchType(self, theIsMustMatchAll: bool) -> None:
        """
        Sets the requirement that all sensitive entities in the
        list used at the time of construction, or added using
        the function Add must be matched.
        """

    def MustMatchAll(self) -> bool:
        """
        Returns true if all sensitive entities in the list used
        at the time of construction, or added using the function Add must be matched.
        """

    def ToCheckOverlapAll(self) -> bool:
        """
        Returns TRUE if all sensitive entities should be checked within rectangular/polygonal
        selection, FALSE by default. Can be useful for sensitive entities holding detection results as
        class property.
        """

    def SetCheckOverlapAll(self, theToCheckAll: bool) -> None:
        """
        Returns TRUE if all sensitive entities should be checked within rectangular/polygonal
        selection, FALSE by default. Can be useful for sensitive entities holding detection results as
        class property.
        """

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the group overlaps current selecting volume"""

    def NbSubElements(self) -> int:
        """Returns the amount of sub-entities"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def Set(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """Sets the owner for all entities in group"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the group. If location transformation
        is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of entity set. If location transformation
        is set, it will be applied
        """

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of sensitive entity with index theIdx"""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of sensitive entity index theIdx in
        the vector along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2 in the vector"""

    def Size(self) -> int:
        """Returns the length of vector of sensitive entities"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitivePoint(Select3D_SensitiveEntity):
    """A framework to define sensitive 3D points."""

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a sensitive point object defined by the
        owner OwnerId and the point Point.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitivePoint) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NbSubElements(self) -> int:
        """Returns the amount of sub-entities in sensitive"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the point overlaps current selecting volume"""

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point used at the time of construction."""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of point. If location transformation
        is set, it will be applied
        """

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the point. If location
        transformation is set, it will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitivePrimitiveArray(Select3D_SensitiveSet):
    """
    Sensitive for triangulation or point set defined by Primitive Array.
    The primitives can be optionally combined into patches within BVH tree
    to reduce its building time in expense of extra traverse time.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """Constructs an empty sensitive object."""

    @overload
    def __init__(self, theOther: Select3D_SensitivePrimitiveArray) -> None: ...

    def PatchSizeMax(self) -> int:
        """Return patch size limit (1 by default)."""

    def SetPatchSizeMax(self, thePatchSizeMax: int) -> None:
        """
        Assign patch size limit.
        Should be set before initialization.
        """

    def PatchDistance(self) -> float:
        """
        Maximum allowed distance between consequential elements in patch (ShortRealLast() by default).
        Has no effect on indexed triangulation.
        """

    def SetPatchDistance(self, thePatchDistMax: float) -> None:
        """
        Assign patch distance limit.
        Should be set before initialization.
        """

    @overload
    def InitTriangulation(self, theVerts: nanoocp.Graphic3d.Graphic3d_Buffer | None, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theIndexLower: int, theIndexUpper: int, theToEvalMinMax: bool = True, theNbGroups: int = 1) -> bool:
        """
        Initialize the sensitive object from triangualtion.
        The sub-triangulation can be specified by arguments theIndexLower and theIndexUpper
        (these are for iterating theIndices, not to restrict the actual index values!).
        @param theVerts        attributes array containing Graphic3d_TOA_POS with type
        Graphic3d_TOD_VEC3 or Graphic3d_TOD_VEC2
        @param theIndices      index array defining triangulation
        @param theInitLoc      location
        @param theIndexLower   the theIndices range - first value (inclusive), starting from 0 and
        multiple by 3
        @param theIndexUpper   the theIndices range - last  value (inclusive), upto
        theIndices->NbElements-1 and multiple by 3
        @param theToEvalMinMax compute bounding box within initialization
        @param theNbGroups     number of groups to split the vertex array into several parts
        """

    @overload
    def InitTriangulation(self, theVerts: nanoocp.Graphic3d.Graphic3d_Buffer | None, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theToEvalMinMax: bool = True, theNbGroups: int = 1) -> bool:
        """
        Initialize the sensitive object from triangualtion.
        @param theVerts        attributes array containing Graphic3d_TOA_POS with type
        Graphic3d_TOD_VEC3 or Graphic3d_TOD_VEC2
        @param theIndices      index array defining triangulation
        @param theInitLoc      location
        @param theToEvalMinMax compute bounding box within initialization
        @param theNbGroups     number of groups to split the vertex array into several parts
        """

    @overload
    def InitPoints(self, theVerts: nanoocp.Graphic3d.Graphic3d_Buffer | None, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theIndexLower: int, theIndexUpper: int, theToEvalMinMax: bool = True, theNbGroups: int = 1) -> bool:
        """
        Initialize the sensitive object from point set.
        The sub-set of points can be specified by arguments theIndexLower and theIndexUpper
        (these are for iterating theIndices, not to restrict the actual index values!).
        @param theVerts        attributes array containing Graphic3d_TOA_POS with type
        Graphic3d_TOD_VEC3 or Graphic3d_TOD_VEC2
        @param theIndices      index array defining points
        @param theInitLoc      location
        @param theIndexLower   the theIndices range - first value (inclusive), starting from 0
        @param theIndexUpper   the theIndices range - last  value (inclusive), upto
        theIndices->NbElements-1
        @param theToEvalMinMax compute bounding box within initialization
        @param theNbGroups     number of groups to split the vertex array into several parts
        """

    @overload
    def InitPoints(self, theVerts: nanoocp.Graphic3d.Graphic3d_Buffer | None, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theToEvalMinMax: bool = True, theNbGroups: int = 1) -> bool:
        """
        Initialize the sensitive object from point set.
        @param theVerts        attributes array containing Graphic3d_TOA_POS with type
        Graphic3d_TOD_VEC3 or Graphic3d_TOD_VEC2
        @param theIndices      index array to define subset of points
        @param theInitLoc      location
        @param theToEvalMinMax compute bounding box within initialization
        @param theNbGroups     number of groups to split the vertex array into several parts
        """

    @overload
    def InitPoints(self, theVerts: nanoocp.Graphic3d.Graphic3d_Buffer | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theToEvalMinMax: bool = True, theNbGroups: int = 1) -> bool:
        """
        Initialize the sensitive object from point set.
        @param theVerts        attributes array containing Graphic3d_TOA_POS with type
        Graphic3d_TOD_VEC3 or Graphic3d_TOD_VEC2
        @param theInitLoc      location
        @param theToEvalMinMax compute bounding box within initialization
        @param theNbGroups     number of groups to split the vertex array into several parts
        """

    def SetMinMax(self, theMinX: float, theMinY: float, theMinZ: float, theMaxX: float, theMaxY: float, theMaxZ: float) -> None:
        """Assign new not transformed bounding box."""

    def ToDetectElements(self) -> bool:
        """
        Return flag to keep index of last topmost detected element, TRUE by default.
        """

    def SetDetectElements(self, theToDetect: bool) -> None:
        """
        Setup keeping of the index of last topmost detected element (axis picking).
        """

    def ToDetectElementMap(self) -> bool:
        """
        Return flag to keep index map of last detected elements, FALSE by default (rectangle
        selection).
        """

    def SetDetectElementMap(self, theToDetect: bool) -> None:
        """
        Setup keeping of the index map of last detected elements (rectangle selection).
        """

    def ToDetectNodes(self) -> bool:
        """
        Return flag to keep index of last topmost detected node, FALSE by default.
        """

    def SetDetectNodes(self, theToDetect: bool) -> None:
        """
        Setup keeping of the index of last topmost detected node (for axis picking).
        """

    def ToDetectNodeMap(self) -> bool:
        """
        Return flag to keep index map of last detected nodes, FALSE by default (rectangle selection).
        """

    def SetDetectNodeMap(self, theToDetect: bool) -> None:
        """
        Setup keeping of the index map of last detected nodes (rectangle selection).
        """

    def ToDetectEdges(self) -> bool:
        """
        Return flag to keep index of last topmost detected edge, FALSE by default.
        """

    def SetDetectEdges(self, theToDetect: bool) -> None:
        """
        Setup keeping of the index of last topmost detected edge (axis picking).
        """

    def LastDetectedElement(self) -> int:
        """
        Return last topmost detected element or -1 if undefined (axis picking).
        """

    def LastDetectedElementMap(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Return the index map of last detected elements (rectangle selection)."""

    def LastDetectedNode(self) -> int:
        """Return last topmost detected node or -1 if undefined (axis picking)."""

    def LastDetectedNodeMap(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Return the index map of last detected nodes (rectangle selection)."""

    def LastDetectedEdgeNode1(self) -> int:
        """
        Return the first node of last topmost detected edge or -1 if undefined (axis picking).
        """

    def LastDetectedEdgeNode2(self) -> int:
        """
        Return the second node of last topmost detected edge or -1 if undefined (axis picking).
        """

    def GetVertex(self, theIndex: int) -> list[nanoocp.Quantity.NCollection_Vec3__float]:
        """
        Return the three vertex positions of the triangle at the given triangulation index.
        Only meaningful for triangulation-based primitive arrays.
        @param[in] theIndex zero-based triangle index within [0, triangle count)
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Checks whether the sensitive entity is overlapped by current selecting volume.
        """

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def Size(self) -> int:
        """Returns the length of array of triangles or edges"""

    def NbSubElements(self) -> int:
        """Returns the amount of nodes in triangulation"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of triangle/edge with index theIdx"""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of triangle/edge with index theIdx
        in array along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2 in array"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the triangulation. If location
        transformation is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of triangulation. If location transformation
        is set, it will be applied
        """

    def HasInitLocation(self) -> bool:
        """
        Returns true if the shape corresponding to the entity has init location
        """

    def InvInitLocation(self) -> nanoocp.gp.gp_GTrsf:
        """
        Returns inversed location transformation matrix if the shape corresponding
        to this entity has init location set. Otherwise, returns identity matrix.
        """

    def Set(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """Sets the owner for all entities in group"""

    def BVH(self) -> None:
        """Builds BVH tree for sensitive set."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Select3D_SensitiveSegment(Select3D_SensitiveEntity):
    """
    A framework to define sensitive zones along a segment
    One gives the 3D start and end point
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theFirstPnt: nanoocp.gp.gp_Pnt, theLastPnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs the sensitive segment object defined by
        the owner theOwnerId, the points theFirstPnt, theLastPnt
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveSegment) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetStartPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """changes the start Point of the Segment;"""

    def SetEndPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """changes the end point of the segment"""

    @overload
    def StartPoint(self) -> nanoocp.gp.gp_Pnt:
        """gives the 3D start Point of the Segment"""

    @overload
    def StartPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """changes the start Point of the Segment;"""

    @overload
    def EndPoint(self) -> nanoocp.gp.gp_Pnt:
        """gives the 3D End Point of the Segment"""

    @overload
    def EndPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """changes the end point of the segment"""

    def NbSubElements(self) -> int:
        """Returns the amount of points"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the segment overlaps current selecting volume"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the segment. If location transformation
        is set, it will be applied
        """

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the segment. If location
        transformation is set, it will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Select3D_SensitiveSphere(Select3D_SensitiveEntity):
    """A framework to define selection by a sensitive sphere."""

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> None:
        """
        Constructs a sensitive sphere object defined by the owner theOwnerId,
        the center of the sphere and it's radius.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveSphere) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Radius(self) -> float:
        """Returns the radius of the sphere"""

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the sphere overlaps current selecting volume"""

    def GetConnected(self) -> Select3D_SensitiveEntity:
        """Returns the copy of this"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the sphere.
        If location transformation is set, it will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Always returns false"""

    def NbSubElements(self) -> int:
        """Returns the amount of points"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of the sphere with transformation applied"""

    def LastDetectedPoint(self) -> nanoocp.gp.gp_Pnt:
        """Returns the position of detected point on the sphere."""

    def ResetLastDetectedPoint(self) -> None:
        """Invalidate the position of detected point on the sphere."""

class Select3D_SensitiveTriangle(Select3D_SensitiveEntity):
    """
    A framework to define selection of triangles in a view.
    This comes into play in the detection of meshing and triangulation in surfaces.
    In some cases this class can raise Standard_ConstructionError and
    Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePnt0: nanoocp.gp.gp_Pnt, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, theType: Select3D_TypeOfSensitivity = Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR) -> None:
        """
        Constructs a sensitive triangle object defined by the
        owner theOwnerId, the points P1, P2, P3, and the type of sensitivity Sensitivity.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveTriangle) -> None: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the triangle overlaps current selecting volume"""

    def Points3D(self, thePnt0: nanoocp.gp.gp_Pnt, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt) -> None:
        """Returns the 3D points P1, P2, P3 used at the time of construction."""

    def Center3D(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the center point of the sensitive triangle created at construction time.
        """

    def GetConnected(self) -> Select3D_SensitiveEntity:
        """Returns the copy of this"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the triangle. If location transformation is set, it
        will be applied
        """

    def ToBuildBVH(self) -> bool:
        """Returns TRUE if BVH tree is in invalidated state"""

    def NbSubElements(self) -> int:
        """Returns the amount of points"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Select3D_SensitiveTriangulation(Select3D_SensitiveSet):
    """
    A framework to define selection of a sensitive entity made of a set of triangles.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theTrg: nanoocp.Poly.Poly_Triangulation | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theIsInterior: bool = True) -> None:
        """
        Constructs a sensitive triangulation object defined by
        the owner theOwnerId, the triangulation theTrg,
        the location theInitLoc, and the flag theIsInterior.
        """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theTrg: nanoocp.Poly.Poly_Triangulation | None, theInitLoc: nanoocp.TopLoc.TopLoc_Location, theFreeEdges: nanoocp.NCollection.NCollection_HArray1[int] | None, theCOG: nanoocp.gp.gp_Pnt, theIsInterior: bool) -> None:
        """
        Constructs a sensitive triangulation object defined by
        the owner theOwnerId, the triangulation theTrg,
        the location theInitLoc, the array of free edges
        theFreeEdges, the center of gravity theCOG, and the flag theIsInterior.
        As free edges and the center of gravity do not have
        to be computed later, this syntax reduces computation time.
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveTriangulation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LastDetectedTriangle(self, theTriangle: nanoocp.Poly.Poly_Triangle) -> bool:
        """
        Get last detected triangle.
        @param[out] theTriangle  triangle node indexes
        @return TRUE if defined
        """

    def LastDetectedTriangle__list(self, theTriangle: nanoocp.Poly.Poly_Triangle) -> tuple[bool, list[nanoocp.gp.gp_Pnt]]:
        """
        LastDetectedTriangle__list: the C++ overload LastDetectedTriangle(Poly_Triangle &, gp_Pnt[3]); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Get last detected triangle.
        @param[out] theTriangle  triangle node indexes
        @param[out] theTriNodes  triangle nodes (with pre-applied transformation)
        @return TRUE if defined
        """

    def LastDetectedTriangleIndex(self) -> int:
        """
        Return index of last detected triangle within [1..NbTris] range, or -1 if undefined.
        """

    def NbSubElements(self) -> int:
        """Returns the amount of nodes in triangulation"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def Triangulation(self) -> nanoocp.Poly.Poly_Triangulation: ...

    def Size(self) -> int:
        """Returns the length of array of triangles or edges"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of triangle/edge with index theIdx"""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of triangle/edge with index theIdx
        in array along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2 in array"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the triangulation. If location
        transformation is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of triangulation. If location transformation
        is set, it will be applied
        """

    def HasInitLocation(self) -> bool:
        """
        Returns true if the shape corresponding to the entity has init location
        """

    def InvInitLocation(self) -> nanoocp.gp.gp_GTrsf:
        """
        Returns inversed location transformation matrix if the shape corresponding
        to this entity has init location set. Otherwise, returns identity matrix.
        """

    def GetInitLocation(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Checks whether one or more entities of the set overlap current selecting volume.
        """

class Select3D_SensitiveWire(Select3D_SensitiveSet):
    """
    A framework to define selection of a wire owner by an
    elastic wire band.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """
        Constructs a sensitive wire object defined by the
        owner theOwnerId
        """

    @overload
    def __init__(self, theOther: Select3D_SensitiveWire) -> None: ...

    def Add(self, theSensitive: Select3D_SensitiveEntity | None) -> None:
        """Adds the sensitive entity theSensitive to this framework."""

    def NbSubElements(self) -> int:
        """Returns the amount of sub-entities"""

    def GetConnected(self) -> Select3D_SensitiveEntity: ...

    def GetEdges(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Select3D.Select3D_SensitiveEntity]:
        """returns the sensitive edges stored in this wire"""

    def Set(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """Sets the owner for all entities in wire"""

    def GetLastDetected(self) -> Select3D_SensitiveEntity: ...

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the wire. If location
        transformation is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns center of the wire. If location transformation
        is set, it will be applied
        """

    def Size(self) -> int:
        """Returns the length of vector of sensitive entities"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of sensitive entity with index theIdx"""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of sensitive entity index theIdx in
        the vector along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2 in the vector"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
