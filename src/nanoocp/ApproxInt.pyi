"""OCCT package ApproxInt (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Approx
import nanoocp.IntPatch
import nanoocp.IntSurf
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class ApproxInt_KnotTools:
    """
    This class intended to build knots sequence on discrete set of points for further approximation
    into bspline curve.

    Short description of algorithm:
    1) Build discrete curvature on points set.
    2) According to special rules build draft knots sequence.
    3) Filter draft sequence to build output sequence.

    For more details look at:
    Anshuman Razdan - Knot Placement for B-Spline curve Approximation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ApproxInt_KnotTools) -> None: ...

    @staticmethod
    def BuildKnots(thePntsXYZ: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], thePntsU1V1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], thePntsU2V2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], thePars: nanoocp.math.math_Vector, theApproxXYZ: bool, theApproxU1V1: bool, theApproxU2V2: bool, theMinNbPnts: int, theKnots: nanoocp.NCollection.NCollection_DynamicArray[int]) -> None:
        """
        Main function to build optimal knot sequence.
        At least one set from (thePntsXYZ, thePntsU1V1, thePntsU2V2) should exist.
        @param thePntsXYZ - Set of 3d points.
        @param thePntsU1V1 - Set of 2d points.
        @param thePntsU2V2 - Set of 2d points.
        @param thePars - Expected parameters associated with set.
        @param theApproxXYZ - Flag, existence of 3d set.
        @param theApproxU1V1 - Flag existence of first 2d set.
        @param theApproxU2V2 - Flag existence of second 2d set.
        @param theMinNbPnts - Minimal number of points per knot interval.
        @param theKnots - output knots sequence.
        """

    @staticmethod
    def BuildCurvature(theCoords: NCollection_LocalArray__double, theDim: int, thePars: nanoocp.math.math_Vector, theCurv: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """Builds discrete curvature"""

    @staticmethod
    def DefineParType(theWL: nanoocp.IntPatch.IntPatch_WLine | None, theFpar: int, theLpar: int, theApproxXYZ: bool, theApproxU1V1: bool, theApproxU2V2: bool) -> nanoocp.Approx.Approx_ParametrizationType:
        """Defines preferable parametrization type for theWL"""

class ApproxInt_SvSurfaces:
    """
    This class is root class for classes dedicated to calculate
    2d and 3d points and tangents of intersection lines of two surfaces of different types
    for given u, v parameters of intersection point on two surfaces.

    The field myUseSolver is used to manage type of calculation:
    if myUseSolver = true, input parameters u1, v1, u2, v2 are considered as first approximation of
    exact intersection point, then coordinates u1, v1, u2, v2 are refined with help of
    the solver used in intersection algorithm and required values are calculated.
    if myUseSolver = false, u1, v1, u2, v2 are considered as "exact" intersection points on two
    surfaces and required values are calculated directly using u1, v1, u2, v2
    """

    def Compute(self, Pt: nanoocp.gp.gp_Pnt, Tg: nanoocp.gp.gp_Vec, Tguv1: nanoocp.gp.gp_Vec2d, Tguv2: nanoocp.gp.gp_Vec2d) -> tuple[bool, float, float, float, float]:
        """returns True if Tg,Tguv1 Tguv2 can be computed."""

    def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: nanoocp.IntSurf.IntSurf_PntOn2S) -> bool:
        """computes point on curve and parameters on the surfaces"""

    def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec) -> bool: ...

    def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec2d) -> bool: ...

    def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec2d) -> bool: ...

    def SetUseSolver(self, theUseSol: bool) -> None: ...

    def GetUseSolver(self) -> bool: ...

class NCollection_LocalArray__double:
    """
    Auxiliary class optimizing creation of array buffer
    (using stack allocation for small arrays).

    For trivially copyable types the fast memcpy / Standard::Reallocate path
    is used.  For non-trivially-copyable types (Handle, TopLoc_Location, etc.)
    the class uses placement new, move semantics, and explicit destructors
    while keeping Standard::Allocate / Standard::Free for heap management.

    Non-trivially-copyable types must be default-constructible and
    nothrow-move-constructible.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theSize: int) -> None: ...

    def Allocate(self, theSize: int) -> None: ...

    def Reallocate(self, theNewSize: int, theToCopy: bool = True) -> None:
        """
        Reallocate the array to a new size.
        @param[in] theNewSize new number of elements
        @param[in] theToCopy  if true, existing elements are copied/moved to the new buffer
        """

    def Size(self) -> int: ...

    def ToArray1(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns a span as Array1 with shared memory.
        Modifying the local array or the array view may invalidate the shared buffer.
        @return array view of the local array data
        """
