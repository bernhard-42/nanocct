"""OCCT package SelectBasics (toolkit TKV3d)"""

from typing import overload

import nanoocp.BVH
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.gp


class SelectBasics:
    """interface class for dynamic selection"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SelectBasics) -> None: ...

    @staticmethod
    def MaxOwnerPriority() -> int:
        """
        Structure to provide all-in-one result of selection of sensitive for "Matches" method of
        Select3D_SensitiveEntity.
        """

    @staticmethod
    def MinOwnerPriority() -> int: ...

class SelectBasics_PickResult:
    """
    This structure provides unified access to the results of Matches() method in all sensitive
    entities, so that it defines a Depth (distance to the entity along picking ray) and a closest
    Point on entity.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor defining an invalid result."""

    @overload
    def __init__(self, theDepth: float, theDistToCenter: float, theObjPickedPnt: nanoocp.gp.gp_Pnt) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: SelectBasics_PickResult) -> None: ...

    @staticmethod
    def Min(thePickResult1: SelectBasics_PickResult, thePickResult2: SelectBasics_PickResult) -> SelectBasics_PickResult:
        """
        Return closest result between two Pick Results according to Depth value.
        """

    def IsValid(self) -> bool:
        """Return TRUE if result was been defined."""

    def Invalidate(self) -> None:
        """Reset depth value."""

    def Depth(self) -> float:
        """Return depth along picking ray."""

    def SetDepth(self, theDepth: float) -> None:
        """Set depth along picking ray."""

    def HasPickedPoint(self) -> bool:
        """Return TRUE if Picked Point lying on detected entity was set."""

    def PickedPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Return picked point lying on detected entity.
        WARNING! Point is defined in local coordinate system and should be translated into World
        System before usage!
        """

    def SetPickedPoint(self, theObjPickedPnt: nanoocp.gp.gp_Pnt) -> None:
        """Set picked point."""

    def DistToGeomCenter(self) -> float:
        """
        Return distance to geometry center (auxiliary value for comparing results).
        """

    def SetDistToGeomCenter(self, theDistToCenter: float) -> None:
        """Set distance to geometry center."""

    def SurfaceNormal(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """
        Return (unnormalized) surface normal at picked point or zero vector if undefined.
        WARNING! Normal is defined in local coordinate system and should be translated into World
        System before usage!
        """

    @overload
    def SetSurfaceNormal(self, theNormal: nanoocp.Quantity.NCollection_Vec3__float) -> None: ...

    @overload
    def SetSurfaceNormal(self, theNormal: nanoocp.gp.gp_Vec) -> None:
        """Set surface normal at picked point."""

class SelectBasics_SelectingVolumeManager:
    """
    This class provides an interface for selecting volume manager,
    which is responsible for all overlap detection methods and
    calculation of minimum depth, distance to center of geometry
    and detected closest point on entity.
    """

    def GetActiveSelectionType(self) -> int:
        """Return selection type."""

    @overload
    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d, thePickResult: SelectBasics_PickResult) -> bool:
        """Returns true if selecting volume is overlapped by box theBox"""

    @overload
    def OverlapsBox(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum
        corner at point theMinPt and maximum at point theMaxPt
        """

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool:
        """Returns true if selecting volume is overlapped by point thePnt"""

    @overload
    def OverlapsPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """
        Returns true if selecting volume is overlapped by point thePnt.
        Does not perform depth calculation, so this method is defined as
        helper function for inclusion test.
        """

    def OverlapsPolygon(self, theArrayOfPts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: int, thePickResult: SelectBasics_PickResult) -> bool:
        """
        Returns true if selecting volume is overlapped by planar convex polygon, which points
        are stored in theArrayOfPts, taking into account sensitivity type theSensType
        """

    def OverlapsSegment(self, thePt1: nanoocp.gp.gp_Pnt, thePt2: nanoocp.gp.gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool:
        """
        Returns true if selecting volume is overlapped by line segment with start point at thePt1
        and end point at thePt2
        """

    def OverlapsTriangle(self, thePt1: nanoocp.gp.gp_Pnt, thePt2: nanoocp.gp.gp_Pnt, thePt3: nanoocp.gp.gp_Pnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool:
        """
        Returns true if selecting volume is overlapped by triangle with vertices thePt1,
        thePt2 and thePt3, taking into account sensitivity type theSensType
        """

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float, thePickResult: SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsSphere(self, theCenter: nanoocp.gp.gp_Pnt, theRadius: float) -> bool:
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter
        and radius theRadius
        """

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool, thePickResult: SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: nanoocp.gp.gp_Trsf, theIsHollow: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses
        theBottomRad and theTopRad, height theHeight, the boolean theIsHollow and transformation to
        apply theTrsf.
        """

    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool, thePickResult: SelectBasics_PickResult) -> bool: ...

    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: nanoocp.gp.gp_Trsf, theIsFilled: bool) -> bool:
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius,
        the boolean theIsFilled, and transformation to apply theTrsf.
        The position and orientation of the circle are specified
        via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """

    def DistToGeometryCenter(self, theCOG: nanoocp.gp.gp_Pnt) -> float:
        """
        Calculates distance from 3d projection of user-defined selection point
        to the given point theCOG
        """

    def DetectedPoint(self, theDepth: float) -> nanoocp.gp.gp_Pnt:
        """Return 3D point corresponding to specified depth within picking ray."""

    def IsOverlapAllowed(self) -> bool:
        """
        Returns flag indicating if partial overlapping of entities is allowed or should be rejected.
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

    @overload
    def Overlaps(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d, thePickResult: SelectBasics_PickResult) -> bool: ...

    @overload
    def Overlaps(self, theBoxMin: nanoocp.BVH.BVH_Vec3d, theBoxMax: nanoocp.BVH.BVH_Vec3d) -> bool:
        """Deprecated in OCCT: Deprecated alias for OverlapsBox()"""

    @overload
    def Overlaps(self, thePnt: nanoocp.gp.gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...

    @overload
    def Overlaps(self, thePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Deprecated in OCCT: Deprecated alias for OverlapsPoint()"""

    @overload
    def Overlaps(self, theArrayOfPts: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...

    @overload
    def Overlaps(self, theArrayOfPts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: int, thePickResult: SelectBasics_PickResult) -> bool:
        """Deprecated in OCCT: Deprecated alias for OverlapsPolygon()"""

    @overload
    def Overlaps(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool:
        """Deprecated in OCCT: Deprecated alias for OverlapsSegment()"""

    @overload
    def Overlaps(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool:
        """Deprecated in OCCT: Deprecated alias for OverlapsTriangle()"""
