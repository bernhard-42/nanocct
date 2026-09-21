"""OCCT package HelixGeom (toolkit TKHelix)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class HelixGeom_BuilderApproxCurve:
    """
    Base class for helix curve approximation algorithms.

    This abstract class provides common functionality for approximating
    parametric helix curves using B-spline curves. It manages:
    - Approximation tolerance and parameters
    - Continuity requirements (C0, C1, C2)
    - Maximum degree and number of segments
    - Error and warning status reporting
    - Result curve storage

    Derived classes must implement the Perform() method to execute
    the specific approximation algorithm.

    @sa HelixGeom_BuilderHelixGen, HelixGeom_BuilderHelix, HelixGeom_BuilderHelixCoil
    """

    def SetApproxParameters(self, aCont: nanoocp.GeomAbs.GeomAbs_Shape, aMaxDegree: int, aMaxSeg: int) -> None:
        """Sets approximation parameters"""

    def ApproxParameters(self) -> tuple[nanoocp.GeomAbs.GeomAbs_Shape, int, int]:
        """Gets approximation parameters"""

    def SetTolerance(self, aTolerance: float) -> None:
        """Sets approximation tolerance"""

    def Tolerance(self) -> float:
        """Gets approximation tolerance"""

    def ToleranceReached(self) -> float:
        """Gets actual tolerance reached by approximation algorithm"""

    def Curves(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]:
        """Gets sequence of BSpline curves representing helix coils"""

    def ErrorStatus(self) -> int:
        """Returns error status of algorithm"""

    def WarningStatus(self) -> int:
        """Returns warning status of algorithm"""

    def Perform(self) -> None:
        """
        Performs calculations.
        Must be redefined.
        """

class HelixGeom_BuilderHelixGen(HelixGeom_BuilderApproxCurve):
    """
    Base class for helix curve building algorithms with parameter management.

    This class extends HelixGeom_BuilderApproxCurve by adding helix-specific
    geometric parameters:
    - Parameter range (T1, T2) - angular range in radians
    - Pitch - vertical distance per full turn (2*PI radians)
    - Start radius (RStart) - radius at parameter T1
    - Taper angle - angle for radius variation (0 = cylindrical)
    - Orientation - clockwise or counter-clockwise

    Concrete implementations include:
    - HelixGeom_BuilderHelix: Single helix approximation
    - HelixGeom_BuilderHelixCoil: Multi-coil helix approximation

    @sa HelixGeom_BuilderApproxCurve, HelixGeom_HelixCurve
    """

    def SetCurveParameters(self, aT1: float, aT2: float, aPitch: float, aRStart: float, aTaperAngle: float, bIsClockwise: bool) -> None:
        """Sets parameters for building helix curves"""

    def CurveParameters(self) -> tuple[float, float, float, float, float, bool]:
        """Gets parameters for building helix curves"""

class HelixGeom_BuilderHelix(HelixGeom_BuilderHelixGen):
    """
    Upper level class for geometrical algorithm of building
    helix curves using arbitrary axis
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: HelixGeom_BuilderHelix) -> None: ...

    def SetPosition(self, aAx2: nanoocp.gp.gp_Ax2) -> None:
        """Sets coordinate axes for helix"""

    def Position(self) -> nanoocp.gp.gp_Ax2:
        """Gets coordinate axes for helix"""

    def Perform(self) -> None:
        """Performs calculations"""

class HelixGeom_BuilderHelixCoil(HelixGeom_BuilderHelixGen):
    """
    Implementation of algorithm for building helix coil with
    axis OZ
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: HelixGeom_BuilderHelixCoil) -> None: ...

    def Perform(self) -> None:
        """Performs calculations"""

class HelixGeom_HelixCurve(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """
    Adaptor class for calculation of helix curves with analytical expressions.

    This class provides parametric representation of helix curves including:
    - Cylindrical helixes (constant radius)
    - Tapered helixes (variable radius with taper angle)
    - Both clockwise and counter-clockwise orientations

    The helix is defined by parametric equations in cylindrical coordinates:
    - x(t) = r(t) * cos(t)
    - y(t) = r(t) * sin(t) [* direction factor]
    - z(t) = pitch * t / (2*PI)
    where r(t) = rStart + taper_factor * t

    @sa HelixGeom_BuilderHelix, HelixGeom_BuilderHelixCoil
    """

    @overload
    def __init__(self) -> None:
        """implementation of analytical expressions"""

    @overload
    def __init__(self, theOther: HelixGeom_HelixCurve) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Load(self) -> None:
        """Sets default values for parameters"""

    @overload
    def Load(self, aT1: float, aT2: float, aPitch: float, aRStart: float, aTaperAngle: float, aIsCW: bool) -> None:
        """Sets helix parameters"""

    def FirstParameter(self) -> float:
        """Gets first parameter"""

    def LastParameter(self) -> float:
        """Gets last parameter"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Gets continuity"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """Gets number of intervals"""

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Gets parametric intervals"""

    def Resolution(self, R3d: float) -> float:
        """Gets parametric resolution"""

    def IsClosed(self) -> bool:
        """Returns False"""

    def IsPeriodic(self) -> bool:
        """Returns False"""

    def Period(self) -> float:
        """Returns 2*PI"""

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter theU on the curve."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """Computes the point and first derivative at parameter theU."""

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """Computes the point and first two derivatives at parameter theU."""

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """Returns the derivative of order theN at parameter theU."""

class HelixGeom_Tools:
    """
    Static utility class providing approximation algorithms for helix curves.

    This class contains static methods for:
    - Converting analytical helix curves to B-spline approximations
    - Generic curve approximation with specified tolerances and continuity
    - High-quality approximation suitable for CAD/CAM applications

    The approximation algorithms use advanced techniques to ensure:
    - Accurate representation within specified tolerances
    - Smooth continuity (C0, C1, C2) as required
    - Efficient B-spline parameterization
    - Robust handling of edge cases
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HelixGeom_Tools) -> None: ...

    @staticmethod
    def ApprHelix(aT1: float, aT2: float, aPitch: float, aRStart: float, aTaperAngle: float, aIsCW: bool, aTol: float) -> tuple[int, nanoocp.Geom.Geom_BSplineCurve, float]:
        """
        Approximates a parametric helix curve using B-spline representation.
        @param aT1 [in] Start parameter (angular position in radians)
        @param aT2 [in] End parameter (angular position in radians)
        @param aPitch [in] Helix pitch (vertical distance per 2*PI radians)
        @param aRStart [in] Starting radius at parameter aT1
        @param aTaperAngle [in] Taper angle in radians (0 = cylindrical helix)
        @param aIsCW [in] True for clockwise, false for counter-clockwise
        @param aTol [in] Approximation tolerance
        @param theBSpl [out] Resulting B-spline curve
        @param theMaxError [out] Maximum approximation error achieved
        @return 0 on success, error code otherwise
        """

    @staticmethod
    def ApprCurve3D(theHC: nanoocp.Adaptor3d.Adaptor3d_Curve | None, theTol: float, theCont: nanoocp.GeomAbs.GeomAbs_Shape, theMaxSeg: int, theMaxDeg: int) -> tuple[int, nanoocp.Geom.Geom_BSplineCurve, float]:
        """
        Approximates a generic 3D curve using B-spline representation.
        @param theHC [in] Handle to the curve adaptor to approximate
        @param theTol [in] Approximation tolerance
        @param theCont [in] Required continuity (C0, C1, C2)
        @param theMaxSeg [in] Maximum number of curve segments
        @param theMaxDeg [in] Maximum degree of B-spline curve
        @param theBSpl [out] Resulting B-spline curve
        @param theMaxError [out] Maximum approximation error achieved
        @return 0 on success, error code otherwise
        """
