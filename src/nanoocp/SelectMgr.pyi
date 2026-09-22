"""OCCT package SelectMgr (toolkit TKV3d)"""

from collections.abc import Sequence
import enum
from typing import overload

import nanoocp.AIS
import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.Graphic3d
from nanoocp.Graphic3d import (
    BVH_Tree__double__3__BVH_BinaryTree as BVH_Tree__double__3__BVH_BinaryTree
)
import nanoocp.Image
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Prs3d
import nanoocp.PrsMgr
import nanoocp.Quantity
import nanoocp.Select3D
import nanoocp.SelectBasics
import nanoocp.Standard
import nanoocp.StdSelect
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.V3d
import nanoocp.gp


class SelectMgr_FilterType(enum.IntEnum):
    """Enumeration defines the filter type."""

    SelectMgr_FilterType_AND = 0

    SelectMgr_FilterType_OR = 1

SelectMgr_FilterType_AND: SelectMgr_FilterType = SelectMgr_FilterType.SelectMgr_FilterType_AND

SelectMgr_FilterType_OR: SelectMgr_FilterType = SelectMgr_FilterType.SelectMgr_FilterType_OR

class SelectMgr_SelectionType(enum.IntEnum):
    """Possible selection types"""

    SelectMgr_SelectionType_Unknown = -1

    SelectMgr_SelectionType_Point = 0

    SelectMgr_SelectionType_Box = 1

    SelectMgr_SelectionType_Polyline = 2

SelectMgr_SelectionType_Unknown: SelectMgr_SelectionType = ...

SelectMgr_SelectionType_Point: SelectMgr_SelectionType = ...

SelectMgr_SelectionType_Box: SelectMgr_SelectionType = ...

SelectMgr_SelectionType_Polyline: SelectMgr_SelectionType = ...

class SelectMgr_StateOfSelection(enum.IntEnum):
    """different state of a Selection in a ViewerSelector..."""

    SelectMgr_SOS_Any = -2

    SelectMgr_SOS_Unknown = -1

    SelectMgr_SOS_Deactivated = 0

    SelectMgr_SOS_Activated = 1

SelectMgr_SOS_Any: SelectMgr_StateOfSelection = SelectMgr_StateOfSelection.SelectMgr_SOS_Any

SelectMgr_SOS_Unknown: SelectMgr_StateOfSelection = SelectMgr_StateOfSelection.SelectMgr_SOS_Unknown

SelectMgr_SOS_Deactivated: SelectMgr_StateOfSelection = ...

SelectMgr_SOS_Activated: SelectMgr_StateOfSelection = ...

class SelectMgr_TypeOfBVHUpdate(enum.IntEnum):
    """
    Keeps track for BVH update state for each SelectMgr_Selection entity in a following way:
    - Add        : 2nd level BVH does not contain any of the selection's sensitive entities and they
    must be added;
    - Remove     : all sensitive entities of the selection must be removed from 2nd level BVH;
    - Renew      : 2nd level BVH already contains sensitives of the selection, but the its complete
    update and removal is required. Therefore, sensitives of the selection with this type of update
    must be removed from 2nd level BVH and added after recomputation.
    - Invalidate : the 2nd level BVH needs to be rebuilt;
    - None       : entities of the selection are up to date.
    """

    SelectMgr_TBU_Add = 0

    SelectMgr_TBU_Remove = 1

    SelectMgr_TBU_Renew = 2

    SelectMgr_TBU_Invalidate = 3

    SelectMgr_TBU_None = 4

SelectMgr_TBU_Add: SelectMgr_TypeOfBVHUpdate = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Add

SelectMgr_TBU_Remove: SelectMgr_TypeOfBVHUpdate = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Remove

SelectMgr_TBU_Renew: SelectMgr_TypeOfBVHUpdate = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Renew

SelectMgr_TBU_Invalidate: SelectMgr_TypeOfBVHUpdate = ...

SelectMgr_TBU_None: SelectMgr_TypeOfBVHUpdate = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_None

class SelectMgr_TypeOfUpdate(enum.IntEnum):
    """
    Provides values for types of update, including
    -   full
    -   partial
    -   none.
    """

    SelectMgr_TOU_Full = 0

    SelectMgr_TOU_Partial = 1

    SelectMgr_TOU_None = 2

SelectMgr_TOU_Full: SelectMgr_TypeOfUpdate = SelectMgr_TypeOfUpdate.SelectMgr_TOU_Full

SelectMgr_TOU_Partial: SelectMgr_TypeOfUpdate = SelectMgr_TypeOfUpdate.SelectMgr_TOU_Partial

SelectMgr_TOU_None: SelectMgr_TypeOfUpdate = SelectMgr_TypeOfUpdate.SelectMgr_TOU_None

class SelectMgr_PickingStrategy(enum.IntEnum):
    """
    Enumeration defines picking strategy - which entities detected by picking line will be accepted,
    considering selection filters.
    """

    SelectMgr_PickingStrategy_FirstAcceptable = 0

    SelectMgr_PickingStrategy_OnlyTopmost = 1

SelectMgr_PickingStrategy_FirstAcceptable: SelectMgr_PickingStrategy = ...

SelectMgr_PickingStrategy_OnlyTopmost: SelectMgr_PickingStrategy = ...

class SelectMgr_TypeOfDepthTolerance(enum.IntEnum):
    """
    Define the type of depth tolerance for considering picked entities to lie on the same depth
    (distance from eye to entity).
    @sa SelectMgr_SortCriterion, SelectMgr_ViewerSelector
    """

    SelectMgr_TypeOfDepthTolerance_Uniform = 0

    SelectMgr_TypeOfDepthTolerance_UniformPixels = 1

    SelectMgr_TypeOfDepthTolerance_SensitivityFactor = 2

SelectMgr_TypeOfDepthTolerance_Uniform: SelectMgr_TypeOfDepthTolerance = ...

SelectMgr_TypeOfDepthTolerance_UniformPixels: SelectMgr_TypeOfDepthTolerance = ...

SelectMgr_TypeOfDepthTolerance_SensitivityFactor: SelectMgr_TypeOfDepthTolerance = ...

class SelectMgr:
    """Auxiliary tools for SelectMgr package."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SelectMgr) -> None: ...

    @staticmethod
    def ComputeSensitivePrs(theStructure: nanoocp.Graphic3d.Graphic3d_Structure | None, theSel: SelectMgr_Selection | None, theLoc: nanoocp.gp.gp_Trsf, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> None:
        """Compute debug presentation for sensitive objects."""

class SelectMgr_Filter(nanoocp.Standard.Standard_Transient):
    """
    The root class to define filter objects for selection.
    Advance handling of objects requires the services of
    filters. These only allow dynamic detection and
    selection of objects which correspond to the criteria defined in each.
    Eight standard filters inheriting SelectMgr_Filter are
    defined in Open CASCADE.
    You can create your own filters by defining new filter
    classes inheriting this framework. You use these
    filters by loading them into an AIS interactive context.
    """

    def IsOk(self, anObj: SelectMgr_EntityOwner | None) -> bool:
        """
        Indicates that the selected Interactive Object
        passes the filter. The owner, anObj, can be either
        direct or user. A direct owner is the corresponding
        construction element, whereas a user is the
        compound shape of which the entity forms a part.
        When an object is detected by the mouse - in AIS,
        this is done through a context selector - its owner
        is passed to the filter as an argument.
        If the object returns true, it is kept; if
        not, it is rejected.
        If you are creating a filter class inheriting this
        framework, and the daughter class is to be used in
        an AIS local context, you will need to implement the
        virtual function ActsOn.
        """

    def ActsOn(self, aStandardMode: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool:
        """
        Returns true in an AIS local context, if this filter
        operates on a type of subshape defined in a filter
        class inheriting this framework.
        This function completes IsOk in an AIS local context.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_CompositionFilter(SelectMgr_Filter):
    """
    A framework to define a compound filter composed of
    two or more simple filters.
    """

    def Add(self, afilter: SelectMgr_Filter | None) -> None:
        """
        Adds the filter afilter to a filter object created by a
        filter class inheriting this framework.
        """

    def Remove(self, aFilter: SelectMgr_Filter | None) -> None:
        """Removes the filter aFilter from this framework."""

    def IsEmpty(self) -> bool:
        """Returns true if this framework is empty."""

    def IsIn(self, aFilter: SelectMgr_Filter | None) -> bool:
        """Returns true if the filter aFilter is in this framework."""

    def StoredFilters(self) -> nanoocp.NCollection.NCollection_List[nanoocp.SelectMgr.SelectMgr_Filter]:
        """Returns the list of stored filters from this framework."""

    def Clear(self) -> None:
        """Clears the filters used in this framework."""

    def ActsOn(self, aStandardMode: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_AndFilter(SelectMgr_CompositionFilter):
    """
    A framework to define a selection filter for two or
    more types of entity.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty selection filter object for two or
        more types of entity.
        """

    @overload
    def __init__(self, theOther: SelectMgr_AndFilter) -> None: ...

    def IsOk(self, anobj: SelectMgr_EntityOwner | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_AndOrFilter(SelectMgr_CompositionFilter):
    """
    A framework to define an OR or AND selection filter.
    To use an AND selection filter call SetUseOrFilter with False parameter.
    By default the OR selection filter is used.
    """

    @overload
    def __init__(self, theFilterType: SelectMgr_FilterType) -> None:
        """Constructs an empty selection filter."""

    @overload
    def __init__(self, theOther: SelectMgr_AndOrFilter) -> None: ...

    def IsOk(self, theObj: SelectMgr_EntityOwner | None) -> bool:
        """Indicates that the selected Interactive Object passes the filter."""

    def SetDisabledObjects(self, theObjects: "NCollection_Shared<NCollection_Map<Standard_Transient const*, NCollection_DefaultHasher<Standard_Transient const*>>, void>" | None) -> None:
        """Disable selection of specified objects."""

    def FilterType(self) -> SelectMgr_FilterType:
        """@return a selection filter type (@sa SelectMgr_FilterType)."""

    def SetFilterType(self, theFilterType: SelectMgr_FilterType) -> None:
        """
        Sets a selection filter type.
        SelectMgr_FilterType_OR selection filter is used be default.
        @param theFilterType the filter type.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_BaseIntersector(nanoocp.Standard.Standard_Transient):
    """
    This class is an interface for different types of selecting intersector,
    defining different selection types, like point, box or polyline
    selection. It contains signatures of functions for detection of
    overlap by sensitive entity and initializes some data for building
    the selecting intersector
    """

    def Build(self) -> None:
        """Builds intersector according to internal parameters"""

    def GetSelectionType(self) -> SelectMgr_SelectionType:
        """Returns selection type of this intersector"""

    def IsScalable(self) -> bool:
        """Checks if it is possible to scale this intersector."""

    def SetPixelTolerance(self, theTol: int) -> None:
        """
        Sets pixel tolerance.
        It makes sense only for scalable intersectors (built on a single point).
        This method does nothing for the base class.
        """

    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: nanoocp.gp.gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Note that this method does not perform any checks on type of the frustum.
        @param[in] theScaleFactor  scale factor for new intersector or negative value if undefined;
        IMPORTANT: scaling makes sense only for scalable ::IsScalable()
        intersectors (built on a single point)!
        @param[in] theTrsf  transformation for new intersector or gp_Identity if undefined
        @param[in] theBuilder  an optional argument that represents corresponding settings for
        re-constructing transformed frustum from scratch;
        could be NULL if reconstruction is not expected furthermore
        @return a copy of the frustum resized according to the scale factor given and transforms it
        using the matrix given
        """

    def CopyWithBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        @param[in] theBuilder  argument that represents corresponding settings for re-constructing
        transformed frustum from scratch;
        should NOT be NULL.
        @return a copy of the frustum with the input builder assigned
        """

    def Camera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Return camera definition."""

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Saves camera definition."""

    def WindowSize(self) -> tuple[int, int]:
        """
        Returns current window size.
        This method doesn't set any output values for the base class.
        """

    def SetWindowSize(self, theWidth: int, theHeight: int) -> None:
        """
        Sets current window size.
        This method does nothing for the base class.
        """

    def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None:
        """
        Sets viewport parameters.
        This method does nothing for the base class.
        """

    def GetNearPnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns near point of intersector.
        This method returns zero point for the base class.
        """

    def GetFarPnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns far point of intersector.
        This method returns zero point for the base class.
        """

    def GetViewRayDirection(self) -> nanoocp.gp.gp_Dir:
        """
        Returns direction ray of intersector.
        This method returns zero direction for the base class.
        """

    def GetMousePosition(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns current mouse coordinates.
        This method returns infinite point for the base class.
        """

    def GetPlanes(self, thePlaneEquations: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BVH.BVH_Vec4d]) -> None:
        """
        Stores plane equation coefficients (in the following form:
        Ax + By + Cz + D = 0) to the given vector.
        This method only clears input vector for the base class.
        """

    @overload
    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given axis-aligned box
        """

    @overload
    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Returns true if selecting volume is overlapped by axis-aligned bounding box
        with minimum corner at point theMinPt and maximum at point theMaxPt
        """

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Intersection test between defined volume and given point"""

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """
        Intersection test between defined volume and given point
        Does not perform depth calculation, so this method is defined as helper function for inclusion
        test. Therefore, its implementation makes sense only for rectangular frustum with box
        selection mode activated.
        """

    def OverlapsPolygon(self, theArrayOfPnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given ordered set of points,
        representing line segments. The test may be considered of interior part or
        boundary line defined by segments depending on given sensitivity type
        """

    def OverlapsSegment(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks if line segment overlaps selecting frustum"""

    def OverlapsTriangle(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given triangle. The test may
        be considered of interior part or boundary line defined by triangle vertices
        depending on given sensitivity type
        """

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> bool: ...

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter
        and radius theRadius
        """

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius,
        boolean theIsFilled and transformation to apply theTrsf.
        The position and orientation of the circle are specified
        via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """

    def DistToGeometryCenter(self, theCOG: nanoocp.gp.gp_Pnt) -> float:
        """
        Measures distance between 3d projection of user-picked
        screen point and given point theCOG.
        It makes sense only for intersectors built on a single point.
        This method returns infinite value for the base class.
        """

    def DetectedPoint(self, theDepth: float) -> nanoocp.gp.gp_Pnt:
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given
        depth. It makes sense only for intersectors built on a single point. This method returns
        infinite point for the base class.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def RaySphereIntersection(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, theLoc: nanoocp.gp.gp_Pnt, theRayDir: nanoocp.gp.gp_Dir) -> tuple[bool, float, float]:
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction
        theRayDir intersects with the sphere with center at theCenter and radius TheRadius
        """

    def RayCylinderIntersection(self, theBottomRadius: float, theTopRadius: float, theHeight: float, theLoc: nanoocp.gp.gp_Pnt, theRayDir: nanoocp.gp.gp_Dir, theIsHollow: bool) -> tuple[bool, float, float]:
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction
        theRayDir intersects with the hollow cylinder (or cone)
        @param[in]  theBottomRadius the bottom cylinder radius
        @param[in]  theTopRadius    the top cylinder radius
        @param[in]  theHeight       the cylinder height
        @param[in]  theLoc          the location of the ray
        @param[in]  theRayDir       the ray direction
        @param[in]  theIsHollow     true if the cylinder is hollow
        @param[out] theTimeEnter    the entering the intersection
        @param[out] theTimeLeave    the leaving the intersection
        """

    def RayCircleIntersection(self, theRadius: float, theLoc: nanoocp.gp.gp_Pnt, theRayDir: nanoocp.gp.gp_Dir, theIsFilled: bool) -> tuple[bool, float]:
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction
        theRayDir intersects with the circle
        @param[in]  theRadius   the circle radius
        @param[in]  theLoc      the location of the ray
        @param[in]  theRayDir   the ray direction
        @param[in]  theIsFilled true if it's a circle, false if it's a circle outline
        @param[out] theTime     the intersection
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_AxisIntersector(SelectMgr_BaseIntersector):
    """
    This class contains representation of selecting axis, created in case of point selection
    and algorithms for overlap detection between this axis and sensitive entities.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: SelectMgr_AxisIntersector) -> None: ...

    def Init(self, theAxis: nanoocp.gp.gp_Ax1) -> None:
        """Initializes selecting axis according to the input one"""

    def Build(self) -> None:
        """
        Builds axis according to internal parameters.
        NOTE: it should be called after Init() method
        """

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """
        Saves camera definition.
        Do nothing for axis intersector (not applicable to this volume).
        """

    def IsScalable(self) -> bool:
        """Returns FALSE (not applicable to this volume)."""

    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: nanoocp.gp.gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        IMPORTANT: Scaling doesn't make sense for this intersector.
        Returns a copy of the intersector transformed using the matrix given.
        Builder is an optional argument that represents corresponding settings for re-constructing
        transformed frustum from scratch. Can be null if reconstruction is not expected furthermore.
        """

    def CopyWithBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Returns a copy of the intersector transformed using the builder configuration given.
        Builder is an argument that represents corresponding settings for re-constructing transformed
        frustum from scratch. In this class, builder is not used and theBuilder parameter is ignored.
        """

    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Intersection test between defined axis and given axis-aligned box"""

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Intersection test between defined axis and given point"""

    def OverlapsPolygon(self, theArrayOfPnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Intersection test between defined axis and given ordered set of points,
        representing line segments. The test may be considered of interior part or
        boundary line defined by segments depending on given sensitivity type
        """

    def OverlapsSegment(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks if selecting axis intersects line segment"""

    def OverlapsTriangle(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Intersection test between defined axis and given triangle. The test may
        be considered of interior part or boundary line defined by triangle vertices
        depending on given sensitivity type
        """

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> bool: ...

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Intersection test between defined axis and given sphere with center theCenter
        and radius theRadius
        """

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius,
        boolean theIsFilled and transformation to apply theTrsf.
        The position and orientation of the circle are specified
        via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """

    def DistToGeometryCenter(self, theCOG: nanoocp.gp.gp_Pnt) -> float:
        """Measures distance between start axis point and given point theCOG."""

    def DetectedPoint(self, theDepth: float) -> nanoocp.gp.gp_Pnt:
        """
        Calculates the point on a axis ray that was detected during the run of selection algo by given
        depth
        """

    def GetNearPnt(self) -> nanoocp.gp.gp_Pnt:
        """Returns near point along axis."""

    def GetFarPnt(self) -> nanoocp.gp.gp_Pnt:
        """Returns far point along axis (infinite)."""

    def GetViewRayDirection(self) -> nanoocp.gp.gp_Dir:
        """Returns axis direction."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_BaseFrustum(SelectMgr_BaseIntersector):
    """
    This class is an interface for different types of selecting frustums,
    defining different selection types, like point, box or polyline
    selection. It contains signatures of functions for detection of
    overlap by sensitive entity and initializes some data for building
    the selecting frustum
    """

    def SetBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> None:
        """
        Nullifies the builder created in the constructor and copies the pointer given
        """

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Saves camera definition and passes it to builder"""

    def SetPixelTolerance(self, theTol: int) -> None: ...

    def SetWindowSize(self, theWidth: int, theHeight: int) -> None: ...

    def WindowSize(self) -> tuple[int, int]: ...

    def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None:
        """Passes viewport parameters to builder"""

    def IsBoundaryIntersectSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, thePlaneNormal: nanoocp.gp.gp_Dir, theBoundaries: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> tuple[bool, bool]:
        """
        Checks whether the boundary of the current volume selection intersects with a sphere or are
        there it's boundaries lying inside the sphere
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_ViewClipRange:
    """
    Class for handling depth clipping range.
    It is used to perform checks in case if global (for the whole view)
    clipping planes are defined inside of SelectMgr_RectangularFrustum class methods.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty clip range."""

    @overload
    def __init__(self, theOther: SelectMgr_ViewClipRange) -> None: ...

    def IsClipped(self, theDepth: float) -> bool:
        """
        Check if the given depth is not within clipping range(s),
        e.g. TRUE means depth is clipped.
        """

    def GetNearestDepth(self, theRange: nanoocp.Bnd.Bnd_Range) -> tuple[bool, float]:
        """
        Calculates the min not clipped value from the range.
        Returns FALSE if the whole range is clipped.
        """

    def SetVoid(self) -> None:
        """Clears clipping range."""

    def AddClippingPlanes(self, thePlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane, thePickRay: nanoocp.gp.gp_Ax1) -> None:
        """
        Add clipping planes. Planes and picking ray should be defined in the same coordinate system.
        """

    def ChangeUnclipRange(self) -> nanoocp.Bnd.Bnd_Range:
        """Returns the main unclipped range; [-inf, inf] by default."""

    def AddClipSubRange(self, theRange: nanoocp.Bnd.Bnd_Range) -> None:
        """Adds a clipping sub-range (for clipping chains)."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_SelectingVolumeManager(nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager):
    """
    This class is used to switch between active selecting volumes depending
    on selection type chosen by the user.
    The sample of correct selection volume initialization procedure:
    @code
    aMgr.InitPointSelectingVolume (aMousePos);
    aMgr.SetPixelTolerance (aTolerance);
    aMgr.SetCamera (aCamera);
    aMgr.SetWindowSize (aWidth, aHeight);
    aMgr.BuildSelectingVolume();
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """Creates instances of all available selecting volume types"""

    @overload
    def __init__(self, theOther: SelectMgr_SelectingVolumeManager) -> None: ...

    def InitPointSelectingVolume(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates, initializes and activates rectangular selecting frustum for point selection
        """

    def InitBoxSelectingVolume(self, theMinPt: nanoocp.gp.gp_Pnt2d, theMaxPt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates, initializes and activates rectangular selecting frustum for box selection
        """

    def InitPolylineSelectingVolume(self, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        Creates, initializes and activates set of triangular selecting frustums for polyline selection
        """

    def InitAxisSelectingVolume(self, theAxis: nanoocp.gp.gp_Ax1) -> None:
        """Creates and activates axis selector for point selection"""

    def InitSelectingVolume(self, theVolume: SelectMgr_BaseIntersector | None) -> None:
        """Sets as active the custom selecting volume"""

    @overload
    def BuildSelectingVolume(self) -> None:
        """Builds previously initialized selecting volume."""

    @overload
    def BuildSelectingVolume(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Deprecated in OCCT: Deprecated method - InitPointSelectingVolume() and Build() methods should be used instead
        """

    @overload
    def BuildSelectingVolume(self, theMinPt: nanoocp.gp.gp_Pnt2d, theMaxPt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Deprecated in OCCT: Deprecated method - InitBoxSelectingVolume() and Build() should be used instead
        """

    @overload
    def BuildSelectingVolume(self, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        Deprecated in OCCT: Deprecated method - InitPolylineSelectingVolume() and Build() should be used instead
        """

    def ActiveVolume(self) -> SelectMgr_BaseIntersector:
        """
        Returns active selecting volume that was built during last
        run of OCCT selection mechanism
        """

    def GetActiveSelectionType(self) -> int: ...

    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: nanoocp.gp.gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_SelectingVolumeManager:
        """
        IMPORTANT: Scaling makes sense only for frustum built on a single point!
        Note that this method does not perform any checks on type of the frustum.

        Returns a copy of the frustum resized according to the scale factor given
        and transforms it using the matrix given.
        There are no default parameters, but in case if:
        - transformation only is needed: @theScaleFactor must be initialized as any negative value;
        - scale only is needed: @theTrsf must be set to gp_Identity.
        Builder is an optional argument that represents corresponding settings for re-constructing
        transformed frustum from scratch. Can be null if reconstruction is not expected furthermore.
        """

    def CopyWithBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_SelectingVolumeManager:
        """
        Returns a copy of the selecting volume manager and its active frustum re-constructed using the
        passed builder. Builder is an argument that represents corresponding settings for
        re-constructing transformed frustum from scratch.
        """

    def Camera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Returns current camera definition."""

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """
        Updates camera projection and orientation matrices in all selecting volumes
        Note: this method should be called after selection volume building
        else exception will be thrown
        """

    def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None:
        """
        Updates viewport in all selecting volumes
        Note: this method should be called after selection volume building
        else exception will be thrown
        """

    def SetPixelTolerance(self, theTolerance: int) -> None:
        """
        Updates pixel tolerance in all selecting volumes
        Note: this method should be called after selection volume building
        else exception will be thrown
        """

    def WindowSize(self) -> tuple[int, int]:
        """Returns window size"""

    def SetWindowSize(self, theWidth: int, theHeight: int) -> None:
        """
        Updates window size in all selecting volumes
        Note: this method should be called after selection volume building
        else exception will be thrown
        """

    @overload
    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given axis-aligned box
        """

    @overload
    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Returns true if selecting volume is overlapped by axis-aligned bounding box
        with minimum corner at point theMinPt and maximum at point theMaxPt
        """

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Intersection test between defined volume and given point"""

    def OverlapsPolygon(self, theArrayOfPts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: int, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given ordered set of points,
        representing line segments. The test may be considered of interior part or
        boundary line defined by segments depending on given sensitivity type
        """

    def OverlapsSegment(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks if line segment overlaps selecting frustum"""

    def OverlapsTriangle(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: int, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given triangle. The test may
        be considered of interior part or boundary line defined by triangle vertices
        depending on given sensitivity type
        """

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> bool:
        """Intersection test between defined volume and given sphere"""

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius,
        boolean theIsFilled and transformation to apply theTrsf.
        The position and orientation of the circle are specified
        via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """

    def DistToGeometryCenter(self, theCOG: nanoocp.gp.gp_Pnt) -> float:
        """
        Measures distance between 3d projection of user-picked
        screen point and given point theCOG
        """

    def DetectedPoint(self, theDepth: float) -> nanoocp.gp.gp_Pnt:
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given
        depth. Throws exception if active selection type is not Point.
        """

    def AllowOverlapDetection(self, theIsToAllow: bool) -> None:
        """
        If theIsToAllow is false, only fully included sensitives will be detected, otherwise the
        algorithm will mark both included and overlapped entities as matched
        """

    def IsOverlapAllowed(self) -> bool: ...

    def ViewClipping(self) -> nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane:
        """Return view clipping planes."""

    def ObjectClipping(self) -> nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane:
        """Return object clipping planes."""

    @overload
    def SetViewClipping(self, theViewPlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None, theObjPlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None, theWorldSelMgr: SelectMgr_SelectingVolumeManager) -> None:
        """
        Valid for point selection only!
        Computes depth range for clipping planes.
        @param[in] theViewPlanes   global view planes
        @param[in] theObjPlanes    object planes
        @param[in] theWorldSelMgr  selection volume in world space for computing clipping plane ranges
        """

    @overload
    def SetViewClipping(self, theOther: SelectMgr_SelectingVolumeManager) -> None:
        """Copy clipping planes from another volume manager."""

    def ViewClipRanges(self) -> SelectMgr_ViewClipRange:
        """Return clipping range."""

    def SetViewClipRanges(self, theRange: SelectMgr_ViewClipRange) -> None:
        """Set clipping range."""

    def GetVertices(self) -> nanoocp.gp.gp_Pnt:
        """
        A set of helper functions that return rectangular selecting frustum data
        """

    def GetNearPickedPnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Valid only for point and rectangular selection.
        Returns projection of 2d mouse picked point or projection
        of center of 2d rectangle (for point and rectangular selection
        correspondingly) onto near view frustum plane
        """

    def GetFarPickedPnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Valid only for point and rectangular selection.
        Returns projection of 2d mouse picked point or projection
        of center of 2d rectangle (for point and rectangular selection
        correspondingly) onto far view frustum plane
        """

    def GetViewRayDirection(self) -> nanoocp.gp.gp_Dir:
        """
        Valid only for point and rectangular selection.
        Returns view ray direction
        """

    def IsScalableActiveVolume(self) -> bool:
        """Checks if it is possible to scale current active selecting volume"""

    def GetMousePosition(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns mouse coordinates for Point selection mode.
        @return infinite point in case of unsupport of mouse position for this active selection
        volume.
        """

    def GetPlanes(self, thePlaneEquations: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BVH.BVH_Vec4d]) -> None:
        """
        Stores plane equation coefficients (in the following form:
        Ax + By + Cz + D = 0) to the given vector
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_BVHThreadPool(nanoocp.Standard.Standard_Transient):
    """
    Class defining a thread pool for building BVH for the list of Select3D_SensitiveEntity within
    background thread(s).
    """

    def __init__(self, theNbThreads: int) -> None:
        """Main constructor"""

    class BVHThread(nanoocp.OSD.OSD_Thread):
        """Thread with back reference to thread pool and thread mutex in it."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: SelectMgr_BVHThreadPool.BVHThread) -> None: ...

        def Assign(self, theCopy: SelectMgr_BVHThreadPool.BVHThread) -> None:
            """Assignment operator."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def AddEntity(self, theEntity: nanoocp.Select3D.Select3D_SensitiveEntity | None) -> None:
        """Queue a sensitive entity to build its BVH"""

    def StopThreads(self) -> None:
        """Stops threads"""

    def WaitThreads(self) -> None:
        """Waits for all threads finish their jobs"""

    def Threads(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.SelectMgr.SelectMgr_BVHThreadPool.BVHThread]:
        """Returns array of threads"""

class SelectMgr_SensitiveEntity(nanoocp.Standard.Standard_Transient):
    """
    The purpose of this class is to mark sensitive entities selectable or not
    depending on current active selection of parent object for proper BVH traverse
    """

    @overload
    def __init__(self, theEntity: nanoocp.Select3D.Select3D_SensitiveEntity | None) -> None:
        """Creates new inactive for selection object with base entity theEntity"""

    @overload
    def __init__(self, theOther: SelectMgr_SensitiveEntity) -> None: ...

    def Clear(self) -> None:
        """Clears up all resources and memory"""

    def BaseSensitive(self) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """Returns related instance of SelectBasics class"""

    def IsActiveForSelection(self) -> bool:
        """
        Returns true if this entity belongs to the active selection
        mode of parent object
        """

    def ResetSelectionActiveStatus(self) -> None:
        """Marks entity as inactive for selection"""

    def SetActiveForSelection(self) -> None:
        """Marks entity as active for selection"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_Selection(nanoocp.Standard.Standard_Transient):
    """
    Represents the state of a given selection mode for a
    Selectable Object. Contains all the sensitive entities available for this mode.
    An interactive object can have an indefinite number of
    modes of selection, each representing a
    "decomposition" into sensitive primitives; each
    primitive has an Owner (SelectMgr_EntityOwner)
    which allows us to identify the exact entity which has
    been detected. Each Selection mode is identified by
    an index. The set of sensitive primitives which
    correspond to a given mode is stocked in a
    SelectMgr_Selection object. By Convention, the
    default selection mode which allows us to grasp the
    Interactive object in its entirety will be mode 0.
    AIS_Trihedron : 4 selection modes
    -   mode 0 : selection of a trihedron
    -   mode 1 : selection of the origin of the trihedron
    -   mode 2 : selection of the axes
    -   mode 3 : selection of the planes XOY, YOZ, XOZ
    when you activate one of modes 1 2 3 4 , you pick AIS objects of type:
    -   AIS_Point
    -   AIS_Axis (and information on the type of axis)
    -   AIS_Plane (and information on the type of plane).
    AIS_PlaneTrihedron offers 3 selection modes:
    -   mode 0 : selection of the whole trihedron
    -   mode 1 : selection of the origin of the trihedron
    -   mode 2 : selection of the axes - same remarks as for the Trihedron.
    AIS_Shape : 7 maximum selection modes, depending
    on the complexity of the shape :
    -   mode 0 : selection of the AIS_Shape
    -   mode 1 : selection of the vertices
    -   mode 2 : selection of the edges
    -   mode 3 : selection of the wires
    -   mode 4 : selection of the faces
    -   mode 5 : selection of the shells
    -   mode 6 : selection of the constituent solids.
    """

    @overload
    def __init__(self, theModeIdx: int = 0) -> None:
        """
        Constructs a selection object defined by the selection mode IdMode.
        The default setting 0 is the selection mode for a shape in its entirety.
        """

    @overload
    def __init__(self, theOther: SelectMgr_Selection) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Destroy(self) -> None: ...

    def Add(self, theSensitive: nanoocp.Select3D.Select3D_SensitiveEntity | None) -> None:
        """
        Adds the sensitive primitive to the list of stored entities in this object.
        Raises NullObject if the primitive is a null handle.
        """

    def Clear(self) -> None:
        """empties the selection from all the stored entities"""

    def IsEmpty(self) -> bool:
        """returns true if no sensitive entity is stored."""

    def Mode(self) -> int:
        """returns the selection mode represented by this selection"""

    def Entities(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.SelectMgr.SelectMgr_SensitiveEntity]:
        """Return entities."""

    def ChangeEntities(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.SelectMgr.SelectMgr_SensitiveEntity]:
        """Return entities."""

    @overload
    def UpdateStatus(self) -> SelectMgr_TypeOfUpdate:
        """
        Returns the flag UpdateFlag.
        This flag gives the update status of this framework
        in a ViewerSelector object:
        -   full
        -   partial, or
        -   none.
        """

    @overload
    def UpdateStatus(self, theStatus: SelectMgr_TypeOfUpdate) -> None: ...

    def UpdateBVHStatus(self, theStatus: SelectMgr_TypeOfBVHUpdate) -> None: ...

    def BVHUpdateStatus(self) -> SelectMgr_TypeOfBVHUpdate: ...

    def GetSelectionState(self) -> SelectMgr_StateOfSelection:
        """Returns status of selection"""

    def SetSelectionState(self, theState: SelectMgr_StateOfSelection) -> None:
        """Sets status of selection"""

    def Sensitivity(self) -> int:
        """Returns sensitivity of the selection"""

    def SetSensitivity(self, theNewSens: int) -> None:
        """
        Changes sensitivity of the selection and all its entities to the given value.
        IMPORTANT: This method does not update any outer selection structures, so for
        proper updates use SelectMgr_SelectionManager::SetSelectionSensitivity method.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_SelectableObject(nanoocp.PrsMgr.PrsMgr_PresentableObject):
    """
    A framework to supply the structure of the object to be selected.
    At the first pick, this structure is created by calling the appropriate algorithm and retaining
    this framework for further picking. This abstract framework is inherited in Application
    Interactive Services (AIS), notably in AIS_InteractiveObject. Consequently, 3D selection should
    be handled by the relevant daughter classes and their member functions in AIS. This is
    particularly true in the creation of new interactive objects.

    Key interface methods to be implemented by every Selectable Object:
    * Presentable Object (PrsMgr_PresentableObject)
    Consider defining an enumeration of supported Display Mode indexes for particular Interactive
    Object or class of Interactive Objects.
    - AcceptDisplayMode() accepting display modes implemented by this object;
    - Compute() computing presentation for the given display mode index;
    * Selectable Object (SelectMgr_SelectableObject)
    Consider defining an enumeration of supported Selection Mode indexes for particular
    Interactive Object or class of Interactive Objects.
    - ComputeSelection() computing selectable entities for the given selection mode index.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ComputeSelection(self, theSelection: SelectMgr_Selection | None, theMode: int) -> None:
        """
        Computes sensitive primitives for the given selection mode - key interface method of
        Selectable Object.
        @param theSelection selection to fill
        @param theMode selection mode to create sensitive primitives
        """

    def AcceptShapeDecomposition(self) -> bool:
        """
        Informs the graphic context that the interactive Object may be decomposed into sub-shapes for
        dynamic selection. The most used Interactive Object is AIS_Shape.
        """

    @overload
    def RecomputePrimitives(self) -> None:
        """
        Re-computes the sensitive primitives for all modes. IMPORTANT: Do not use
        this method to update selection primitives except implementing custom selection manager!
        This method does not take into account necessary BVH updates, but may invalidate the pointers
        it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.
        """

    @overload
    def RecomputePrimitives(self, theMode: int) -> None:
        """
        Re-computes the sensitive primitives which correspond to the <theMode>th selection mode.
        IMPORTANT: Do not use this method to update selection primitives except implementing custom
        selection manager! selection manager! This method does not take into account necessary BVH
        updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from
        outside classes, use method UpdateSelection.
        """

    def AddSelection(self, aSelection: SelectMgr_Selection | None, aMode: int) -> None:
        """
        Adds the selection aSelection with the selection mode
        index aMode to this framework.
        """

    def ClearSelections(self, update: bool = False) -> None:
        """
        Empties all the selections in the SelectableObject
        <update> parameter defines whether all object's
        selections should be flagged for further update or not.
        This improved method can be used to recompute an
        object's selection (without redisplaying the object
        completely) when some selection mode is activated not for the first time.
        """

    def Selection(self, theMode: int) -> SelectMgr_Selection:
        """Returns the selection having specified selection mode or NULL."""

    def HasSelection(self, theMode: int) -> bool:
        """
        Returns true if a selection corresponding to the selection mode theMode was computed for this
        object.
        """

    def Selections(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_Selection]:
        """Return the sequence of selections."""

    def ResetTransformation(self) -> None: ...

    def UpdateTransformation(self) -> None:
        """Recomputes the location of the selection aSelection."""

    def UpdateTransformations(self, aSelection: SelectMgr_Selection | None) -> None:
        """
        Updates locations in all sensitive entities from <aSelection>
        and in corresponding entity owners.
        """

    def HilightSelected(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_EntityOwner]) -> None:
        """Method which draws selected owners ( for fast presentation draw )"""

    def ClearSelected(self) -> None:
        """
        Method which clear all selected owners belonging
        to this selectable object ( for fast presentation draw )
        """

    def ClearDynamicHighlight(self, theMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None) -> None:
        """
        Method that needs to be implemented when the object
        manages selection and dynamic highlighting on its own.
        Clears or invalidates dynamic highlight presentation.
        By default it clears immediate draw of given presentation
        manager.
        """

    def HilightOwnerWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theOwner: SelectMgr_EntityOwner | None) -> None:
        """
        Method which hilight an owner belonging to
        this selectable object (for fast presentation draw)
        """

    def IsAutoHilight(self) -> bool:
        """
        If returns True, the old mechanism for highlighting selected objects is used (HilightSelected
        Method may be empty). If returns False, the HilightSelected method will be fully responsible
        for highlighting selected entity owners belonging to this selectable object.
        """

    def SetAutoHilight(self, theAutoHilight: bool) -> None:
        """Set AutoHilight property to true or false."""

    def GetHilightPresentation(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None) -> nanoocp.Graphic3d.Graphic3d_Structure:
        """
        Creates or returns existing presentation for highlighting detected object.
        @param thePrsMgr presentation manager to create new presentation
        @return existing or newly created presentation (when thePrsMgr is not NULL)
        """

    def GetSelectPresentation(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None) -> nanoocp.Graphic3d.Graphic3d_Structure:
        """
        Creates or returns existing presentation for highlighting selected object.
        @param thePrsMgr presentation manager to create new presentation
        @return existing or newly created presentation (when thePrsMgr is not NULL)
        """

    def ErasePresentations(self, theToRemove: bool) -> None:
        """
        Removes presentations returned by GetHilightPresentation() and GetSelectPresentation().
        """

    def SetZLayer(self, theLayerId: int) -> None:
        """
        Set Z layer ID and update all presentations of the selectable object.
        The layers mechanism allows drawing objects in higher layers in overlay of objects in lower
        layers.
        """

    def UpdateSelection(self, theMode: int = -1) -> None:
        """
        Sets update status FULL to selections of the object. Must be used as the only method of
        UpdateSelection from outer classes to prevent BVH structures from being outdated.
        """

    def SetAssemblyOwner(self, theOwner: SelectMgr_EntityOwner | None, theMode: int = -1) -> None:
        """Sets common entity owner for assembly sensitive object entities"""

    def BndBoxOfSelected(self, theOwners: nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_IndexedMap[nanoocp.SelectMgr.SelectMgr_EntityOwner]] | None) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns a bounding box of sensitive entities with the owners given if they are a part of
        activated selection
        """

    def GlobalSelectionMode(self) -> int:
        """Returns the mode for selection of object as a whole; 0 by default."""

    def GlobalSelOwner(self) -> SelectMgr_EntityOwner:
        """Returns the owner of mode for selection of object as a whole"""

    def GetAssemblyOwner(self) -> SelectMgr_EntityOwner:
        """Returns common entity owner if the object is an assembly"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_EntityOwner(nanoocp.Standard.Standard_Transient):
    """
    A framework to define classes of owners of sensitive primitives.
    The owner is the link between application and selection data structures.
    For the application to make its own objects selectable, it must define owner classes inheriting
    this framework.
    """

    @overload
    def __init__(self, aPriority: int = 0) -> None:
        """Initializes the selection priority aPriority."""

    @overload
    def __init__(self, aSO: SelectMgr_SelectableObject | None, aPriority: int = 0) -> None:
        """
        Constructs a framework with the selectable object
        anSO being attributed the selection priority aPriority.
        """

    @overload
    def __init__(self, theOwner: SelectMgr_EntityOwner | None, aPriority: int = 0) -> None:
        """
        Constructs a framework from existing one
        anSO being attributed the selection priority aPriority.
        """

    @overload
    def __init__(self, theOther: SelectMgr_EntityOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Priority(self) -> int:
        """
        Return selection priority (within range [0-9]) for results with the same depth; 0 by default.
        Example - selection of shapes:
        the owners are selectable objects (presentations) a user can give vertex priority [3], edges
        [2] faces [1] shape [0], so that if during selection one vertex one edge and one face are
        simultaneously detected, the vertex will only be hilighted.
        """

    def SetPriority(self, thePriority: int) -> None:
        """Sets the selectable priority of the owner within range [0-9]."""

    def HasSelectable(self) -> bool:
        """Returns true if there is a selectable object to serve as an owner."""

    def Selectable(self) -> SelectMgr_SelectableObject:
        """Returns a selectable object detected in the working context."""

    def SetSelectable(self, theSelObj: SelectMgr_SelectableObject | None) -> None:
        """Sets the selectable object."""

    def HandleMouseClick(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButton: int, theModifiers: int, theIsDoubleClick: bool) -> bool:
        """
        Handle mouse button click event.
        Does nothing by default and returns FALSE.
        @param thePoint      mouse cursor position
        @param theButton     clicked button
        @param theModifiers  key modifiers
        @param theIsDoubleClick flag indicating double mouse click
        @return TRUE if object handled click
        For all selection schemes, allowing to select an object,
        it's available
        """

    def IsHilighted(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int = 0) -> bool:
        """
        Returns true if the presentation manager highlights selections corresponding to the selection
        mode.
        """

    def HilightWithColor(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int = 0) -> None:
        """
        Highlights selectable object's presentation with display mode in presentation manager with
        given highlight style. Also a check for auto-highlight is performed - if selectable object
        manages highlighting on its own, execution will be passed to
        SelectMgr_SelectableObject::HilightOwnerWithColor method.
        """

    def Unhilight(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int = 0) -> None:
        """
        Removes highlighting from the owner of a detected selectable object in the presentation
        manager. This object could be the owner of a sensitive primitive.
        @param thePrsMgr presentation manager
        @param theMode   obsolete argument for compatibility, should be ignored by implementations
        """

    def Clear(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int = 0) -> None:
        """
        Clears the owners matching the value of the selection
        mode aMode from the presentation manager object aPM.
        """

    def HasLocation(self) -> bool:
        """Returns TRUE if selectable has transformation."""

    def Location(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns transformation of selectable."""

    def SetLocation(self, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Change owner location (callback for handling change of location of selectable object).
        """

    def IsSelected(self) -> bool:
        """@return true if the owner is selected."""

    def SetSelected(self, theIsSelected: bool) -> None:
        """
        Set the state of the owner.
        @param[in] theIsSelected  shows if owner is selected.
        """

    def Select(self, theSelScheme: nanoocp.AIS.AIS_SelectionScheme, theIsDetected: bool) -> bool:
        """
        If the object needs to be selected, it returns true.
        @param[in] theSelScheme  selection scheme
        @param[in] theIsDetected flag of object detection
        """

    @overload
    def State(self) -> int:
        """
        Deprecated in OCCT: Deprecated method - IsSelected() should be used instead

        Returns selection state.
        """

    @overload
    def State(self, theStatus: int) -> None:
        """
        Set the state of the owner.
        The method is deprecated. Use SetSelected() instead.
        """

    def IsAutoHilight(self) -> bool:
        """
        if owner is not auto hilighted, for group contains many such owners will be called one method
        HilightSelected of SelectableObject
        """

    def IsForcedHilight(self) -> bool:
        """
        if this method returns TRUE the owner will always call method Hilight for SelectableObject
        when the owner is detected. By default it always return FALSE.
        """

    def SetZLayer(self, theLayerId: int) -> None:
        """Set Z layer ID and update all presentations."""

    def UpdateHighlightTrsf(self, theViewer: nanoocp.V3d.V3d_Viewer | None, theManager: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theDispMode: int) -> None:
        """
        Implements immediate application of location transformation of parent object to dynamic
        highlight structure
        """

    def IsSameSelectable(self, theOther: SelectMgr_SelectableObject | None) -> bool:
        """
        Returns true if pointer to selectable object of this owner is equal to the given one
        """

    def ComesFromDecomposition(self) -> bool:
        """
        Returns TRUE if this owner points to a part of object and FALSE for entire object.
        """

    def SetComesFromDecomposition(self, theIsFromDecomposition: bool) -> None:
        """
        Sets flag indicating this owner points to a part of object (TRUE) or to entire object (FALSE).
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @overload
    def Set(self, theSelObj: SelectMgr_SelectableObject | None) -> None:
        """
        Deprecated in OCCT: Deprecated method - SetSelectable() should be used instead

        Sets the selectable object.
        """

    @overload
    def Set(self, thePriority: int) -> None:
        """
        Deprecated in OCCT: Deprecated method - SetPriority() should be used instead

        sets the selectable priority of the owner
        """

class SelectMgr_FrustumBuilder(nanoocp.Standard.Standard_Transient):
    """
    The purpose of this class is to provide unified interface for building
    selecting frustum depending on current camera projection and orientation
    matrices, window size and viewport parameters.
    """

    @overload
    def __init__(self) -> None:
        """Creates new frustum builder with empty matrices"""

    @overload
    def __init__(self, theOther: SelectMgr_FrustumBuilder) -> None: ...

    def Camera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Returns current camera"""

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Stores current camera"""

    def SetWindowSize(self, theWidth: int, theHeight: int) -> None:
        """Stores current window width and height"""

    def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None:
        """Stores current viewport coordinates"""

    def InvalidateViewport(self) -> None: ...

    def WindowSize(self) -> tuple[int, int]: ...

    def SignedPlanePntDist(self, theEq: nanoocp.BVH.BVH_Vec3d, thePnt: nanoocp.BVH.BVH_Vec3d) -> float:
        """
        Calculates signed distance between plane with equation
        theEq and point thePnt
        """

    def ProjectPntOnViewPlane(self, theX: float, theY: float, theZ: float) -> nanoocp.gp.gp_Pnt:
        """
        Projects 2d screen point onto view frustum plane:
        theZ = 0 - near plane,
        theZ = 1 - far plane
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_OrFilter(SelectMgr_CompositionFilter):
    """
    A framework to define an or selection filter.
    This selects one or another type of sensitive entity.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty or selection filter."""

    @overload
    def __init__(self, theOther: SelectMgr_OrFilter) -> None: ...

    def IsOk(self, anobj: SelectMgr_EntityOwner | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_Frustum__4(SelectMgr_BaseFrustum):
    """
    This is an internal class containing representation of rectangular selecting frustum, created in
    case of point and box selection, and algorithms for overlap detection between selecting frustum
    and sensitive entities. The principle of frustum calculation:
    - for point selection: on a near view frustum plane rectangular neighborhood of
    user-picked point is created according to the pixel tolerance
    given and then this rectangle is projected onto far view frustum
    plane. This rectangles define the parallel bases of selecting frustum;
    - for box selection: box points are projected onto near and far view frustum planes.
    These 2 projected rectangles define parallel bases of selecting frustum.
    Overlap detection tests are implemented according to the terms of separating axis
    theorem (SAT).
    Vertex order:
    - for triangular frustum: V0_Near, V1_Near, V2_Near,
    V0_Far, V1_Far, V2_Far;
    - for rectangular frustum: LeftTopNear, LeftTopFar,
    LeftBottomNear,LeftBottomFar,
    RightTopNear, RightTopFar,
    RightBottomNear, RightBottomFar.
    Plane order in array:
    - for triangular frustum: V0V1, V1V2, V0V2, Near, Far;
    - for rectangular frustum: Top, Bottom, Left, Right, Near, Far.
    Uncollinear edge directions order:
    - for rectangular frustum: Horizontal, Vertical,
    LeftLower, RightLower,
    LeftUpper, RightUpper;
    - for triangular frustum: V0_Near - V0_Far, V1_Near - V1_Far, V2_Near - V2_Far,
    V1_Near - V0_Near, V2_Near - V1_Near, V2_Near - V0_Near.
    """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_RectangularFrustum(SelectMgr_Frustum__4):
    """
    This class contains representation of rectangular selecting frustum, created in case
    of point and box selection, and algorithms for overlap detection between selecting
    frustum and sensitive entities. The principle of frustum calculation:
    - for point selection: on a near view frustum plane rectangular neighborhood of
    user-picked point is created according to the pixel tolerance
    given and then this rectangle is projected onto far view frustum
    plane. This rectangles define the parallel bases of selecting frustum;
    - for box selection: box points are projected onto near and far view frustum planes.
    These 2 projected rectangles define parallel bases of selecting frustum.
    Overlap detection tests are implemented according to the terms of separating axis
    theorem (SAT).
    """

    @overload
    def __init__(self) -> None:
        """Creates rectangular selecting frustum."""

    @overload
    def __init__(self, theOther: SelectMgr_RectangularFrustum) -> None: ...

    class SelectionRectangle:
        """
        Auxiliary structure to define selection primitive (point or box)
        In case of point selection min and max points are identical.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: SelectMgr_RectangularFrustum.SelectionRectangle) -> None: ...

        def MousePos(self) -> nanoocp.gp.gp_Pnt2d: ...

        def SetMousePos(self, thePos: nanoocp.gp.gp_Pnt2d) -> None: ...

        def MinPnt(self) -> nanoocp.gp.gp_Pnt2d: ...

        def SetMinPnt(self, theMinPnt: nanoocp.gp.gp_Pnt2d) -> None: ...

        def MaxPnt(self) -> nanoocp.gp.gp_Pnt2d: ...

        def SetMaxPnt(self, theMaxPnt: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def Init(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """Initializes volume according to the point and given pixel tolerance"""

    @overload
    def Init(self, theMinPnt: nanoocp.gp.gp_Pnt2d, theMaxPnt: nanoocp.gp.gp_Pnt2d) -> None:
        """Initializes volume according to the selected rectangle"""

    def isIntersectCircle(self, theRadius: float, theCenter: nanoocp.gp.gp_Pnt, theTrsf: nanoocp.gp.gp_Trsf, theVertices: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> bool:
        """Returns True if Frustum (theVertices) intersects the circle."""

    def isSegmentsIntersect(self, thePnt1Seg1: nanoocp.gp.gp_Pnt, thePnt2Seg1: nanoocp.gp.gp_Pnt, thePnt1Seg2: nanoocp.gp.gp_Pnt, thePnt2Seg2: nanoocp.gp.gp_Pnt) -> bool:
        """
        Returns True if Seg1 (thePnt1Seg1, thePnt2Seg1) and Seg2 (thePnt1Seg2, thePnt2Seg2) intersect.
        """

    def Build(self) -> None:
        """
        Builds volume according to internal parameters.
        NOTE: it should be called after Init() method
        """

    def IsScalable(self) -> bool:
        """
        Checks if it is possible to scale this frustum.
        It is true for frustum built on a single point.
        """

    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: nanoocp.gp.gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        IMPORTANT: Scaling makes sense only for frustum built on a single point!
        Note that this method does not perform any checks on type of the frustum.
        Returns a copy of the frustum resized according to the scale factor given
        and transforms it using the matrix given.
        There are no default parameters, but in case if:
        - transformation only is needed: @theScaleFactor must be initialized as any negative value;
        - scale only is needed: @theTrsf must be set to gp_Identity.
        Builder is an optional argument that represents corresponding settings for re-constructing
        transformed frustum from scratch. Can be null if reconstruction is not expected furthermore.
        """

    def CopyWithBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Returns a copy of the frustum using the given frustum builder configuration.
        Returned frustum should be re-constructed before being used.
        @param[in] theBuilder  argument that represents corresponding settings for re-constructing
        transformed frustum from scratch;
        should NOT be NULL.
        @return a copy of the frustum with the input builder assigned
        """

    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given axis-aligned box
        """

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Intersection test between defined volume and given point"""

    def OverlapsPolygon(self, theArrayOfPnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given ordered set of points,
        representing line segments. The test may be considered of interior part or
        boundary line defined by segments depending on given sensitivity type
        """

    def OverlapsSegment(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks if line segment overlaps selecting frustum"""

    def OverlapsTriangle(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given triangle. The test may
        be considered of interior part or boundary line defined by triangle vertices
        depending on given sensitivity type
        """

    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Intersection test between defined volume and given sphere"""

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius,
        boolean theIsFilled and transformation to apply theTrsf.
        The position and orientation of the circle are specified
        via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """

    def DistToGeometryCenter(self, theCOG: nanoocp.gp.gp_Pnt) -> float:
        """
        Measures distance between 3d projection of user-picked
        screen point and given point theCOG.
        It makes sense only for frustums built on a single point.
        """

    def DetectedPoint(self, theDepth: float) -> nanoocp.gp.gp_Pnt:
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given
        depth
        """

    def GetVertices(self) -> nanoocp.gp.gp_Pnt:
        """
        A set of helper functions that return rectangular selecting frustum data
        """

    def GetNearPnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns projection of 2d mouse picked point or projection
        of center of 2d rectangle (for point and rectangular selection
        correspondingly) onto near view frustum plane
        """

    def GetFarPnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns projection of 2d mouse picked point or projection
        of center of 2d rectangle (for point and rectangular selection
        correspondingly) onto far view frustum plane
        """

    def GetViewRayDirection(self) -> nanoocp.gp.gp_Dir:
        """Returns view ray direction."""

    def GetMousePosition(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns current mouse coordinates."""

    def GetPlanes(self, thePlaneEquations: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BVH.BVH_Vec4d]) -> None:
        """
        Stores plane equation coefficients (in the following form:
        Ax + By + Cz + D = 0) to the given vector
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_SelectableObjectSet:
    """
    The purpose of this class is to organize all selectable objects into data structure, allowing to
    build set of BVH trees for each transformation persistence subclass of selectable objects. This
    allow to minify number of updates for BVH trees - for example 2D persistent object subclass
    depends only on camera's projection and the corresponding BVH tree needs to be updated when
    camera's projection parameters change, while another tree for non-persistent objects can be left
    unchanged in this case.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates new empty objects set and initializes BVH tree builders for each subset.
        """

    @overload
    def __init__(self, theOther: SelectMgr_SelectableObjectSet) -> None: ...

    class BVHSubset(enum.IntEnum):
        """
        This enumeration declares names for subsets of selectable objects. Each subset has independent
        BVH tree. The class maintains subsets of selectable objects by their persistence flag. This
        allows to restric rebuilding of the trees for particular subset when the camera change does
        not implicitly require it:
        - BVHSubset_3d refers to the subset of normal world-space 3D objects. Associated BVH tree does
        not depend on the camera's state at all. This subset uses binned BVH builder with 32 bins and
        1 element per leaf.
        - BVHSubset_3dPersistent refers to the subset of 3D persistent selectable objects (rotate,
        pan, zoom persistence). Associated BVH tree needs to be updated when either the camera's
        projection and position change. This subset uses linear BVH builder with 32 levels of depth
        and 1 element per leaf.
        - BVHSubset_2dPersistent refers to the subset of 2D persistent selectable objects. Associated
        BVH tree needs to be updated only when camera's projection changes. Bounding volumes for this
        object subclass is represented directly in eye space coordinates. This subset uses linear BVH
        builder with 32 levels of depth and 1 element per leaf.
        - BVHSubset_ortho3dPersistent refers to the subset of 3D persistent selectable objects
        (rotate, pan, zoom persistence) that contains `Graphic3d_TMF_OrthoPers` persistence mode.
        Associated BVH tree needs to be updated when either the camera's projection and position
        change. This subset uses linear BVH builder with 32 levels of depth and 1 element per leaf.
        - BVHSubset_ortho2dPersistent refers to the subset of 2D persistent selectable objects
        that contains `Graphic3d_TMF_OrthoPers` persistence mode. Associated BVH tree
        needs to be updated only when camera's projection changes. Bounding volumes for this object
        subclass is represented directly in eye space coordinates. This subset uses linear BVH builder
        with 32 levels of depth and 1 element per leaf.
        """

        BVHSubset_3d = 0

        BVHSubset_3dPersistent = 1

        BVHSubset_2dPersistent = 2

        BVHSubset_ortho3dPersistent = 3

        BVHSubset_ortho2dPersistent = 4

        BVHSubsetNb = 5

    BVHSubset_3d: SelectMgr_SelectableObjectSet.BVHSubset = BVHSubset.BVHSubset_3d

    BVHSubset_3dPersistent: SelectMgr_SelectableObjectSet.BVHSubset = BVHSubset.BVHSubset_3dPersistent

    BVHSubset_2dPersistent: SelectMgr_SelectableObjectSet.BVHSubset = BVHSubset.BVHSubset_2dPersistent

    BVHSubset_ortho3dPersistent: SelectMgr_SelectableObjectSet.BVHSubset = BVHSubset.BVHSubset_ortho3dPersistent

    BVHSubset_ortho2dPersistent: SelectMgr_SelectableObjectSet.BVHSubset = BVHSubset.BVHSubset_ortho2dPersistent

    BVHSubsetNb: SelectMgr_SelectableObjectSet.BVHSubset = BVHSubset.BVHSubsetNb

    class Iterator:
        """Class to iterate sequentually over all objects from every subset."""

        @overload
        def __init__(self) -> None:
            """Default constructor without initialization."""

        @overload
        def __init__(self, theSet: SelectMgr_SelectableObjectSet) -> None:
            """Constructs and initializes the iterator."""

        @overload
        def __init__(self, theOther: SelectMgr_SelectableObjectSet.Iterator) -> None: ...

        def __iter__(self) -> SelectMgr_SelectableObjectSet.Iterator:
            """
            Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
            """

        def __next__(self) -> SelectMgr_SelectableObject:
            """Python addition: see __iter__."""

        def Init(self, theSet: SelectMgr_SelectableObjectSet) -> None:
            """Initializes the iterator."""

        def More(self) -> bool:
            """Returns false when there is no more objects to iterate over."""

        def Next(self) -> None:
            """Steps to next selectable object in the set."""

        def Value(self) -> SelectMgr_SelectableObject:
            """Returns current object."""

    def Append(self, theObject: SelectMgr_SelectableObject | None) -> bool:
        """
        Adds the new selectable object to the set. The selectable object is placed into one of the
        predefined subsets depending on its persistence type. After adding an object, this method
        marks the corresponding BVH tree for rebuild.
        @return true if selectable object is added, otherwise returns false (selectable object is
        already in the set).
        """

    def Remove(self, theObject: SelectMgr_SelectableObject | None) -> bool:
        """
        Removes the selectable object from the set. The selectable object is removed from the subset
        it has been placed into. After removing an object, this method marks the corresponding
        BVH tree for rebuild.
        @return true if selectable object is removed, otherwise returns false (selectable object is
        not in the set).
        """

    def ChangeSubset(self, theObject: SelectMgr_SelectableObject | None) -> None:
        """
        Performs necessary updates when object's persistence types changes.
        This method should be called right after changing transformation persistence flags of the
        objects and before updating BVH tree - to provide up-to-date state of the object set.
        """

    def UpdateBVH(self, theCam: nanoocp.Graphic3d.Graphic3d_Camera | None, theWinSize: nanoocp.BVH.BVH_Vec2i) -> None:
        """
        Updates outdated BVH trees and remembers the last state of the
        camera view-projection matrices and viewport (window) dimensions.
        """

    def MarkDirty(self) -> None:
        """Marks every BVH subset for update."""

    def Contains(self, theObject: SelectMgr_SelectableObject | None) -> bool:
        """Returns true if this objects set contains theObject given."""

    @overload
    def IsEmpty(self) -> bool:
        """
        Returns true if the object set does not contain any selectable objects.
        """

    @overload
    def IsEmpty(self, theSubset: SelectMgr_SelectableObjectSet.BVHSubset) -> bool:
        """Returns true if the specified object subset is empty."""

    def GetObjectById(self, theSubset: SelectMgr_SelectableObjectSet.BVHSubset, theIndex: int) -> SelectMgr_SelectableObject:
        """
        Returns object from subset theSubset by theIndex given. The method allows to get selectable
        object referred by the index of an element of the subset's BVH tree.
        """

    def BVH(self, theSubset: SelectMgr_SelectableObjectSet.BVHSubset) -> nanoocp.Graphic3d.BVH_Tree__double__3__BVH_BinaryTree:
        """Returns computed BVH for the theSubset given."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_SelectionImageFiller(nanoocp.Standard.Standard_Transient):
    """
    Abstract class for filling pixel with color.
    This is internal tool for SelectMgr_ViewerSelector::ToPixMap().
    """

    @staticmethod
    def CreateFiller(thePixMap: nanoocp.Image.Image_PixMap, theSelector: SelectMgr_ViewerSelector, theType: nanoocp.StdSelect.StdSelect_TypeOfSelectionImage) -> SelectMgr_SelectionImageFiller:
        """Create filler of specified type."""

    def Fill(self, theCol: int, theRow: int, thePicked: int) -> None:
        """Fill pixel at specified position."""

    def Flush(self) -> None:
        """Flush results into final image."""

class SelectMgr_SortCriterion:
    """
    This class provides data and criterion for sorting candidate
    entities in the process of interactive selection by mouse click
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: SelectMgr_SortCriterion) -> None: ...

    def IsCloserDepth(self, theOther: SelectMgr_SortCriterion) -> bool:
        """Compare with another item by depth, priority and minDist."""

    def IsHigherPriority(self, theOther: SelectMgr_SortCriterion) -> bool:
        """
        Compare with another item using old logic (OCCT version <= 6.3.1) with priority considered
        preceding depth.
        """

    @property
    def Entity(self) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """detected entity"""

    @Entity.setter
    def Entity(self, arg: nanoocp.Select3D.Select3D_SensitiveEntity, /) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt:
        """3D point"""

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt, /) -> None: ...

    @property
    def Normal(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """surface normal or 0 vector if undefined"""

    @Normal.setter
    def Normal(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def Depth(self) -> float:
        """distance from the view plane to the entity"""

    @Depth.setter
    def Depth(self, arg: float, /) -> None: ...

    @property
    def MinDist(self) -> float:
        """distance from the clicked point to the entity on the view plane"""

    @MinDist.setter
    def MinDist(self, arg: float, /) -> None: ...

    @property
    def Tolerance(self) -> float:
        """tolerance used for selecting candidates"""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

    @property
    def SelectionPriority(self) -> int:
        """selection priority"""

    @SelectionPriority.setter
    def SelectionPriority(self, arg: int, /) -> None: ...

    @property
    def DisplayPriority(self) -> int:
        """display priority"""

    @DisplayPriority.setter
    def DisplayPriority(self, arg: int, /) -> None: ...

    @property
    def ZLayerPosition(self) -> int:
        """ZLayer rendering order index, stronger than a depth"""

    @ZLayerPosition.setter
    def ZLayerPosition(self, arg: int, /) -> None: ...

    @property
    def NbOwnerMatches(self) -> int:
        """overall number of entities collected for the same owner"""

    @NbOwnerMatches.setter
    def NbOwnerMatches(self, arg: int, /) -> None: ...

    @property
    def IsPreferPriority(self) -> bool:
        """flag to signal comparison to be done over priority"""

    @IsPreferPriority.setter
    def IsPreferPriority(self, arg: bool, /) -> None: ...

class SelectMgr_ToleranceMap:
    """
    An internal class for calculation of current largest tolerance value which will be applied for
    creation of selecting frustum by default. Each time the selection set is deactivated, maximum
    tolerance value will be recalculated. If a user enables custom precision using
    StdSelect_ViewerSelector3d::SetPixelTolerance, it will be applied to all sensitive entities
    without any checks.
    """

    @overload
    def __init__(self) -> None:
        """Sets tolerance values to -1.0"""

    @overload
    def __init__(self, theOther: SelectMgr_ToleranceMap) -> None: ...

    def Add(self, theTolerance: int) -> None:
        """
        Adds the value given to map, checks if the current tolerance value
        should be replaced by theTolerance
        """

    def Decrement(self, theTolerance: int) -> None:
        """
        Decrements a counter of the tolerance given, checks if the current tolerance value
        should be recalculated
        """

    def Tolerance(self) -> int:
        """Returns a current tolerance that must be applied"""

    def SetCustomTolerance(self, theTolerance: int) -> None:
        """Sets tolerance to the given one and disables adaptive checks"""

    def ResetDefaults(self) -> None:
        """Unsets a custom tolerance and enables adaptive checks"""

    def CustomTolerance(self) -> int:
        """Returns the value of custom tolerance regardless of it validity"""

    def IsCustomTolSet(self) -> bool:
        """Returns true if custom tolerance value is greater than zero"""

class SelectMgr_ViewerSelector(nanoocp.Standard.Standard_Transient):
    """
    A framework to define finding, sorting the sensitive
    primitives in a view. Services are also provided to
    define the return of the owners of those primitives
    selected. The primitives are sorted by criteria such
    as priority of the primitive or its depth in the view
    relative to that of other primitives.
    Note that in 3D, the inheriting framework
    StdSelect_ViewerSelector3d is only to be used
    if you do not want to use the services provided by
    AIS.
    Two tools are available to find and select objects
    found at a given position in the view. If you want to
    select the owners of all the objects detected at
    point x,y,z you use the Init - More - Next - Picked
    loop. If, on the other hand, you want to select only
    one object detected at that point, you use the Init -
    More - OnePicked loop. In this iteration, More is
    used to see if an object was picked and
    OnePicked, to get the object closest to the pick position.
    Viewer selectors are driven by
    SelectMgr_SelectionManager, and manipulate
    the SelectMgr_Selection objects given to them by
    the selection manager.

    Tolerances are applied to the entities in the following way:
    1. tolerance value stored in mytolerance will be used to calculate initial
    selecting frustum, which will be applied for intersection testing during
    BVH traverse;
    2. if tolerance of sensitive entity is less than mytolerance, the frustum for
    intersection detection will be resized according to its sensitivity.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty selector object."""

    @overload
    def __init__(self, theOther: SelectMgr_ViewerSelector) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CustomPixelTolerance(self) -> int:
        """Returns custom pixel tolerance value."""

    def SetPixelTolerance(self, theTolerance: int) -> None:
        """Sets the pixel tolerance <theTolerance>."""

    def Sensitivity(self) -> float:
        """Returns the largest sensitivity of picking"""

    def PixelTolerance(self) -> int:
        """Returns the largest pixel tolerance."""

    def SortResult(self) -> None:
        """Sorts the detected entities by priority and distance."""

    def OnePicked(self) -> SelectMgr_EntityOwner:
        """
        Returns the picked element with the highest priority,
        and which is the closest to the last successful mouse position.
        """

    def ToPickClosest(self) -> bool:
        """
        Return the flag determining precedence of picked depth (distance from eye to entity) over
        entity priority in sorted results; TRUE by default. When flag is TRUE, priority will be
        considered only if entities have the same depth within the tolerance. When flag is FALSE,
        entities with higher priority will be in front regardless of their depth (like x-ray).
        """

    def SetPickClosest(self, theToPreferClosest: bool) -> None:
        """
        Set flag determining precedence of picked depth over entity priority in sorted results.
        """

    def DepthToleranceType(self) -> SelectMgr_TypeOfDepthTolerance:
        """
        Return the type of tolerance for considering two entities having a similar depth (distance
        from eye to entity); SelectMgr_TypeOfDepthTolerance_SensitivityFactor by default.
        """

    def DepthTolerance(self) -> float:
        """
        Return the tolerance for considering two entities having a similar depth (distance from eye to
        entity).
        """

    def SetDepthTolerance(self, theType: SelectMgr_TypeOfDepthTolerance, theTolerance: float) -> None:
        """
        Set the tolerance for considering two entities having a similar depth (distance from eye to
        entity).
        @param[in] theType  type of tolerance value
        @param[in] theTolerance  tolerance value in 3D scale (SelectMgr_TypeOfDepthTolerance_Uniform)
        or in pixels (SelectMgr_TypeOfDepthTolerance_UniformPixels);
        value is ignored in case of
        SelectMgr_TypeOfDepthTolerance_SensitivityFactor
        """

    def NbPicked(self) -> int:
        """Returns the number of detected owners."""

    def ClearPicked(self) -> None:
        """Clears picking results."""

    def Clear(self) -> None:
        """Empties all the tables, removes all selections..."""

    def Picked(self, theRank: int) -> SelectMgr_EntityOwner:
        """
        Returns the entity Owner for the object picked at specified position.
        @param theRank rank of detected object within range 1...NbPicked()
        """

    def PickedData(self, theRank: int) -> SelectMgr_SortCriterion:
        """
        Returns the Entity for the object picked at specified position.
        @param theRank rank of detected object within range 1...NbPicked()
        """

    def PickedEntity(self, theRank: int) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """
        Returns the Entity for the object picked at specified position.
        @param theRank rank of detected object within range 1...NbPicked()
        """

    def PickedPoint(self, theRank: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the 3D point (intersection of picking axis with the object nearest to eye)
        for the object picked at specified position.
        @param theRank rank of detected object within range 1...NbPicked()
        """

    def RemovePicked(self, theObject: SelectMgr_SelectableObject | None) -> bool:
        """Remove picked entities associated with specified object."""

    def Contains(self, theObject: SelectMgr_SelectableObject | None) -> bool: ...

    def EntitySetBuilder(self) -> nanoocp.BVH.BVH_Builder3d:
        """Returns the default builder used to construct BVH of entity set."""

    def SetEntitySetBuilder(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """
        Sets the default builder used to construct BVH of entity set.
        The new builder will be also assigned for already defined objects, but computed BVH trees will
        not be invalidated.
        """

    def Modes(self, theSelectableObject: SelectMgr_SelectableObject | None, theModeList: nanoocp.NCollection.NCollection_List[int], theWantedState: SelectMgr_StateOfSelection = SelectMgr_StateOfSelection.SelectMgr_SOS_Any) -> bool:
        """
        Returns the list of selection modes ModeList found in
        this selector for the selectable object aSelectableObject.
        Returns true if aSelectableObject is referenced inside
        this selector; returns false if the object is not present
        in this selector.
        """

    def IsActive(self, theSelectableObject: SelectMgr_SelectableObject | None, theMode: int) -> bool:
        """
        Returns true if the selectable object
        aSelectableObject having the selection mode aMode
        is active in this selector.
        """

    def IsInside(self, theSelectableObject: SelectMgr_SelectableObject | None, theMode: int) -> bool:
        """
        Returns true if the selectable object
        aSelectableObject having the selection mode aMode
        is in this selector.
        """

    @overload
    def Status(self, theSelection: SelectMgr_Selection | None) -> SelectMgr_StateOfSelection:
        """Returns the selection status Status of the selection aSelection."""

    @overload
    def Status(self, theSelectableObject: SelectMgr_SelectableObject | None) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def ActiveOwners(self, theOwners: nanoocp.NCollection.NCollection_List[nanoocp.SelectMgr.SelectMgr_EntityOwner]) -> None:
        """Returns the list of active entity owners"""

    def AddSelectableObject(self, theObject: SelectMgr_SelectableObject | None) -> None:
        """Adds new object to the map of selectable objects"""

    def AddSelectionToObject(self, theObject: SelectMgr_SelectableObject | None, theSelection: SelectMgr_Selection | None) -> None:
        """Adds new selection to the object and builds its BVH tree"""

    def MoveSelectableObject(self, theObject: SelectMgr_SelectableObject | None) -> None:
        """
        Moves existing object from set of not transform persistence objects
        to set of transform persistence objects (or vice versa).
        """

    def RemoveSelectableObject(self, theObject: SelectMgr_SelectableObject | None) -> None:
        """Removes selectable object from map of selectable ones"""

    def RemoveSelectionOfObject(self, theObject: SelectMgr_SelectableObject | None, theSelection: SelectMgr_Selection | None) -> None:
        """Removes selection of the object and marks its BVH tree for rebuild"""

    def RebuildObjectsTree(self, theIsForce: bool = False) -> None:
        """
        Marks BVH of selectable objects for rebuild. Parameter theIsForce set as true
        guarantees that 1st level BVH for the viewer selector will be rebuilt during this call
        """

    def RebuildSensitivesTree(self, theObject: SelectMgr_SelectableObject | None, theIsForce: bool = False) -> None:
        """
        Marks BVH of sensitive entities of particular selectable object for rebuild. Parameter
        theIsForce set as true guarantees that 2nd level BVH for the object given will be
        rebuilt during this call
        """

    def GetManager(self) -> SelectMgr_SelectingVolumeManager:
        """Returns instance of selecting volume manager of the viewer selector"""

    def SelectableObjects(self) -> SelectMgr_SelectableObjectSet:
        """Return map of selectable objects."""

    def ResetSelectionActivationStatus(self) -> None:
        """Marks all added sensitive entities of all objects as non-selectable"""

    def AllowOverlapDetection(self, theIsToAllow: bool) -> None:
        """
        Is used for rectangular selection only
        If theIsToAllow is false, only fully included sensitives will be detected, otherwise the
        algorithm will mark both included and overlapped entities as matched
        """

    @overload
    def Pick(self, theXPix: int, theYPix: int, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Picks the sensitive entity at the pixel coordinates of
        the mouse <theXPix> and <theYPix>. The selector looks for touched areas and owners.
        """

    @overload
    def Pick(self, theXPMin: int, theYPMin: int, theXPMax: int, theYPMax: int, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Picks the sensitive entity according to the minimum
        and maximum pixel values <theXPMin>, <theYPMin>, <theXPMax>
        and <theYPMax> defining a 2D area for selection in the 3D view aView.
        """

    @overload
    def Pick(self, thePolyline: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theView: nanoocp.V3d.V3d_View | None) -> None:
        """pick action - input pixel values for polyline selection for selection."""

    @overload
    def Pick(self, theAxis: nanoocp.gp.gp_Ax1, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Picks the sensitive entity according to the input axis.
        This is geometric intersection 3D objects by axis
        (camera parameters are ignored and objects with transform persistence are skipped).
        """

    def ToPixMap(self, theImage: nanoocp.Image.Image_PixMap, theView: nanoocp.V3d.V3d_View | None, theType: nanoocp.StdSelect.StdSelect_TypeOfSelectionImage, thePickedIndex: int = 1) -> bool:
        """
        Dump of detection results into image.
        This method performs axis picking for each pixel in the image
        and generates a color depending on picking results and selection image type.
        @param theImage       result image, should be initialized
        @param theView        3D view defining camera position
        @param theType        type of image to define
        @param thePickedIndex index of picked entity (1 means topmost)
        """

    @overload
    def DisplaySensitive(self, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Displays sensitives in view <theView>."""

    @overload
    def DisplaySensitive(self, theSel: SelectMgr_Selection | None, theTrsf: nanoocp.gp.gp_Trsf, theView: nanoocp.V3d.V3d_View | None, theToClearOthers: bool = True) -> None: ...

    def ClearSensitive(self, theView: nanoocp.V3d.V3d_View | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def SetToPrebuildBVH(self, theToPrebuild: bool, theThreadsNum: int = -1) -> None:
        """Enables/disables building BVH for sensitives in separate threads"""

    def QueueBVHBuild(self, theEntity: nanoocp.Select3D.Select3D_SensitiveEntity | None) -> None:
        """Queues a sensitive entity to build its BVH"""

    def WaitForBVHBuild(self) -> None:
        """Waits BVH threads finished building"""

    def ToPrebuildBVH(self) -> bool:
        """
        Returns TRUE if building BVH for sensitives in separate threads is enabled
        """

class SelectMgr_SelectionManager(nanoocp.Standard.Standard_Transient):
    """
    A framework to manage selection from the point of view of viewer selectors.
    These can be added and removed, and selection modes can be activated and deactivated.
    In addition, objects may be known to all selectors or only to some.
    """

    @overload
    def __init__(self, theSelector: SelectMgr_ViewerSelector | None) -> None:
        """Constructs an empty selection manager object."""

    @overload
    def __init__(self, theOther: SelectMgr_SelectionManager) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Selector(self) -> SelectMgr_ViewerSelector:
        """Return the Selector."""

    def Contains(self, theObject: SelectMgr_SelectableObject | None) -> bool:
        """Returns true if the manager contains the selectable object theObject."""

    def Load(self, theObject: SelectMgr_SelectableObject | None, theMode: int = -1) -> None:
        """
        Loads and computes selection mode theMode (if it is not equal to -1) in global context and
        adds selectable object to BVH tree. If the object theObject has an already calculated
        selection with mode theMode and it was removed, the selection will be recalculated.
        """

    def Remove(self, theObject: SelectMgr_SelectableObject | None) -> None:
        """
        Removes selectable object theObject from all viewer selectors it was added to previously,
        removes it from all contexts and clears all computed selections of theObject.
        """

    def Activate(self, theObject: SelectMgr_SelectableObject | None, theMode: int = 0) -> None:
        """
        Activates the selection mode theMode in the selector theSelector for the selectable object
        anObject. By default, theMode is equal to 0. If theSelector is set to default (NULL), the
        selection with the mode theMode will be activated in all the viewers available.
        """

    def Deactivate(self, theObject: SelectMgr_SelectableObject | None, theMode: int = -1) -> None:
        """
        Deactivates mode theMode of theObject in theSelector. If theMode value is set to default (-1),
        all active selection modes will be deactivated. Likewise, if theSelector value is set to
        default (NULL), theMode will be deactivated in all viewer selectors.
        """

    def IsActivated(self, theObject: SelectMgr_SelectableObject | None, theMode: int = -1) -> bool:
        """
        Returns true if the selection with theMode is active for the selectable object theObject and
        selector theSelector. If all parameters are set to default values, it returns it there is any
        active selection in any known viewer selector for object theObject.
        """

    def ClearSelectionStructures(self, theObj: SelectMgr_SelectableObject | None, theMode: int = -1) -> None:
        """
        Removes sensitive entities from all viewer selectors
        after method Clear() was called to the selection they belonged to
        or it was recomputed somehow.
        """

    def RestoreSelectionStructures(self, theObj: SelectMgr_SelectableObject | None, theMode: int = -1) -> None:
        """
        Re-adds newly calculated sensitive entities of recomputed selection
        defined by mode theMode to all viewer selectors contained that selection.
        """

    def RecomputeSelection(self, theObject: SelectMgr_SelectableObject | None, theIsForce: bool = False, theMode: int = -1) -> None:
        """
        Recomputes activated selections of theObject for all known viewer selectors according to
        theMode specified. If theMode is set to default (-1), then all activated selections will be
        recomputed. If theIsForce is set to true, then selection mode theMode for object theObject
        will be recomputed regardless of its activation status.
        """

    def Update(self, theObject: SelectMgr_SelectableObject | None, theIsForce: bool = True) -> None:
        """
        Updates all selections of theObject in all viewer selectors according to its current update
        status. If theIsForce is set to true, the call is equal to recomputation.
        """

    @overload
    def SetUpdateMode(self, theObject: SelectMgr_SelectableObject | None, theType: SelectMgr_TypeOfUpdate) -> None:
        """
        Sets type of update of all selections of theObject to the given theType.
        """

    @overload
    def SetUpdateMode(self, theObject: SelectMgr_SelectableObject | None, theMode: int, theType: SelectMgr_TypeOfUpdate) -> None:
        """
        Sets type of update of selection with theMode of theObject to the given theType.
        """

    def SetSelectionSensitivity(self, theObject: SelectMgr_SelectableObject | None, theMode: int, theNewSens: int) -> None:
        """
        Allows to manage sensitivity of a particular selection of interactive object theObject and
        changes previous sensitivity value of all sensitive entities in selection with theMode
        to the given theNewSensitivity.
        """

    def UpdateSelection(self, theObj: SelectMgr_SelectableObject | None) -> None:
        """Re-adds selectable object in BVHs in all viewer selectors."""

class SelectMgr_SensitiveEntitySet(nanoocp.BVH.BVH_PrimitiveSet3d):
    """
    This class is used to store all calculated sensitive entities of one selectable object.
    It provides an interface for building BVH tree which is used to speed-up
    the performance of searching for overlap among sensitives of one selectable object
    """

    @overload
    def __init__(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: SelectMgr_SensitiveEntitySet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Append(self, theEntity: SelectMgr_SensitiveEntity | None) -> None:
        """Adds new entity to the set and marks BVH tree for rebuild"""

    @overload
    def Append(self, theSelection: SelectMgr_Selection | None) -> None:
        """
        Adds every entity of selection theSelection to the set and marks
        BVH tree for rebuild
        """

    def Remove(self, theSelection: SelectMgr_Selection | None) -> None:
        """
        Removes every entity of selection theSelection from the set
        and marks BVH tree for rebuild
        """

    @overload
    def Box(self, theIndex: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of entity with index theIdx"""

    @overload
    def Box(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns AABB of primitive set."""

    def Center(self, theIndex: int, theAxis: int) -> float:
        """
        Returns geometry center of sensitive entity index theIdx
        along the given axis theAxis
        """

    def Swap(self, theIndex1: int, theIndex2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2"""

    def Size(self) -> int:
        """Returns the amount of entities"""

    def GetSensitiveById(self, theIndex: int) -> SelectMgr_SensitiveEntity:
        """Returns the entity with index theIndex in the set"""

    def Sensitives(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.SelectMgr.SelectMgr_SensitiveEntity]:
        """Returns map of entities."""

    def Owners(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.SelectMgr.SelectMgr_EntityOwner, int]:
        """Returns map of owners."""

    def HasEntityWithPersistence(self) -> bool:
        """Returns map of entities."""

    def HasEntityWithFlipping(self) -> bool:
        """
        Returns true if this set contains sensitive entities with flipping options.
        """

class SelectMgr_Frustum__3(SelectMgr_BaseFrustum):
    """
    This is an internal class containing representation of rectangular selecting frustum, created in
    case of point and box selection, and algorithms for overlap detection between selecting frustum
    and sensitive entities. The principle of frustum calculation:
    - for point selection: on a near view frustum plane rectangular neighborhood of
    user-picked point is created according to the pixel tolerance
    given and then this rectangle is projected onto far view frustum
    plane. This rectangles define the parallel bases of selecting frustum;
    - for box selection: box points are projected onto near and far view frustum planes.
    These 2 projected rectangles define parallel bases of selecting frustum.
    Overlap detection tests are implemented according to the terms of separating axis
    theorem (SAT).
    Vertex order:
    - for triangular frustum: V0_Near, V1_Near, V2_Near,
    V0_Far, V1_Far, V2_Far;
    - for rectangular frustum: LeftTopNear, LeftTopFar,
    LeftBottomNear,LeftBottomFar,
    RightTopNear, RightTopFar,
    RightBottomNear, RightBottomFar.
    Plane order in array:
    - for triangular frustum: V0V1, V1V2, V0V2, Near, Far;
    - for rectangular frustum: Top, Bottom, Left, Right, Near, Far.
    Uncollinear edge directions order:
    - for rectangular frustum: Horizontal, Vertical,
    LeftLower, RightLower,
    LeftUpper, RightUpper;
    - for triangular frustum: V0_Near - V0_Far, V1_Near - V1_Far, V2_Near - V2_Far,
    V1_Near - V0_Near, V2_Near - V1_Near, V2_Near - V0_Near.
    """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class SelectMgr_TriangularFrustum(SelectMgr_Frustum__3):
    """
    This class contains representation of triangular selecting frustum, created in case
    of polyline selection, and algorithms for overlap detection between selecting frustum and
    sensitive entities. Overlap detection tests are implemented according to the terms of separating
    axis theorem (SAT). NOTE: the object of this class can be created only as part of
    SelectMgr_TriangularFrustumSet.
    """

    def __init__(self, theOther: SelectMgr_TriangularFrustum) -> None: ...

    class SelectionTriangle:
        """Auxiliary structure to define selection triangle"""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: SelectMgr_TriangularFrustum.SelectionTriangle) -> None: ...

        @property
        def Points(self) -> list[nanoocp.gp.gp_Pnt2d]: ...

        @Points.setter
        def Points(self, arg: Sequence[nanoocp.gp.gp_Pnt2d], /) -> None: ...

    def Init(self, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theP3: nanoocp.gp.gp_Pnt2d) -> None:
        """Initializes selection triangle by input points"""

    def Build(self) -> None:
        """
        Creates new triangular frustum with bases of triangles with vertices theP1, theP2 and theP3
        projections onto near and far view frustum planes (only for triangular frustums)
        NOTE: it should be called after Init() method
        """

    def IsScalable(self) -> bool:
        """Returns FALSE (not applicable to this volume)."""

    def ScaleAndTransform(self, theScale: int, theTrsf: nanoocp.gp.gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Returns a copy of the frustum transformed according to the matrix given
        """

    def CopyWithBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Returns a copy of the frustum using the given frustum builder configuration.
        Returned frustum should be re-constructed before being used.
        @param[in] theBuilder  argument that represents corresponding settings for re-constructing
        transformed frustum from scratch;
        should NOT be NULL.
        @return a copy of the frustum with the input builder assigned
        """

    def OverlapsBox(self, theMinPnt: nanoocp.BVH.BVH_Vec3d, theMaxPnt: nanoocp.BVH.BVH_Vec3d, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        @name SAT Tests for different objects
        SAT intersection test between defined volume and given axis-aligned box
        """

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Intersection test between defined volume and given point"""

    @overload
    def OverlapsPoint(self, arg0: nanoocp.gp.gp_Pnt) -> bool:
        """Always returns FALSE (not applicable to this selector)."""

    def OverlapsPolygon(self, theArrayOfPnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given ordered set of points,
        representing line segments. The test may be considered of interior part or
        boundary line defined by segments depending on given sensitivity type
        """

    def OverlapsSegment(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks if line segment overlaps selecting frustum"""

    def OverlapsTriangle(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        SAT intersection test between defined volume and given triangle. The test may
        be considered of interior part or boundary line defined by triangle vertices
        depending on given sensitivity type
        """

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> bool: ...

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter
        and radius theRadius
        """

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius,
        boolean theIsFilled and transformation to apply theTrsf.
        The position and orientation of the circle are specified
        via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """

    def Clear(self) -> None:
        """
        Nullifies the handle to corresponding builder instance to prevent memory leaks
        """

    def GetPlanes(self, thePlaneEquations: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BVH.BVH_Vec4d]) -> None:
        """
        Stores plane equation coefficients (in the following form:
        Ax + By + Cz + D = 0) to the given vector
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class SelectMgr_TriangularFrustumSet(SelectMgr_BaseFrustum):
    """
    This class is used to handle polyline selection. The main principle of polyline selection
    algorithm is to split the polygon defined by polyline onto triangles.
    Than each of them is considered as a base for triangular frustum building.
    In other words, each triangle vertex will be projected from 2d screen space to 3d world space
    onto near and far view frustum planes. Thus, the projected triangles make up the bases of
    selecting frustum. When the set of such frustums is created, the function determining selection
    iterates through triangular frustum set and searches for overlap with any frustum.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: SelectMgr_TriangularFrustumSet) -> None: ...

    class SelectionPolyline:
        """Auxiliary structure to define selection polyline"""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: SelectMgr_TriangularFrustumSet.SelectionPolyline) -> None: ...

        @property
        def Points(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d]: ...

        @Points.setter
        def Points(self, arg: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d], /) -> None: ...

    def Init(self, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """Initializes set of triangular frustums by polyline"""

    def Build(self) -> None:
        """
        Meshes polygon bounded by polyline. Than organizes a set of triangular frustums,
        where each triangle's projection onto near and far view frustum planes is considered as a
        frustum base NOTE: it should be called after Init() method
        """

    def IsScalable(self) -> bool:
        """Returns FALSE (not applicable to this volume)."""

    def ScaleAndTransform(self, theScale: int, theTrsf: nanoocp.gp.gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Returns a copy of the frustum with all sub-volumes transformed according to the matrix given
        """

    def CopyWithBuilder(self, theBuilder: SelectMgr_FrustumBuilder | None) -> SelectMgr_BaseIntersector:
        """
        Returns a copy of the frustum using the given frustum builder configuration.
        Returned frustum should be re-constructed before being used.
        @param[in] theBuilder  argument that represents corresponding settings for re-constructing
        transformed frustum from scratch;
        should NOT be NULL.
        @return a copy of the frustum with the input builder assigned
        """

    def OverlapsBox(self, theMinPnt: nanoocp.BVH.BVH_Vec3d, theMaxPnt: nanoocp.BVH.BVH_Vec3d, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """
        Returns TRUE when the point's near-plane projection lies inside the polyline loop.
        """

    def OverlapsPolygon(self, theArrayOfPnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    def OverlapsSegment(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    def OverlapsTriangle(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    def DetectedPoint(self, theDepth: float) -> nanoocp.gp.gp_Pnt:
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given
        depth
        """

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> bool: ...

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter
        and radius theRadius
        """

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """

    def GetPlanes(self, thePlaneEquations: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BVH.BVH_Vec4d]) -> None:
        """
        Stores plane equation coefficients (in the following form:
        Ax + By + Cz + D = 0) to the given vector
        """

    def SetAllowOverlapDetection(self, theIsToAllow: bool) -> None:
        """
        If theIsToAllow is false, only fully included sensitives will be detected, otherwise the
        algorithm will mark both included and overlapped entities as matched
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.BVH
import nanoocp.NCollection
import nanoocp.SelectMgr
SelectMgr_ListOfFilter = nanoocp.NCollection.NCollection_List[nanoocp.SelectMgr.SelectMgr_Filter]
SelectMgr_Mat4 = nanoocp.BVH.BVH_Mat4d
SelectMgr_SequenceOfSelection = nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_Selection]
SelectMgr_Vec3 = nanoocp.BVH.BVH_Vec3d
SelectMgr_Vec4 = nanoocp.BVH.BVH_Vec4d
