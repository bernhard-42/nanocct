"""OCCT package ProjLib (toolkit TKGeomBase)"""

from typing import TypeAlias, overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.AppParCurves
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomAdaptor
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class ProjLib:
    """
    The ProjLib package first provides projection of curves on a plane along a given Direction.
    The result will be a 3D curve.

    The ProjLib package provides projection of curves on surfaces to compute the curve in the
    parametric space. It is assumed that the curve is on the surface.

    It provides:

    * Package methods to handle the easiest cases:
    - Line, Circle, Ellipse, Parabola, Hyperbola on plane.
    - Line, Circle on cylinder.
    - Line, Circle on cone.

    * Classes to handle the general cases:
    - Plane.
    - Cylinder.
    - Cone.
    - Sphere.
    - Torus.

    * A generic class to handle a Adaptor3d_Curve on a Adaptor3d_Surface.
    """

    def __init__(self) -> None: ...

    @overload
    @staticmethod
    def Project(Pl: nanoocp.gp.gp_Pln, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Project(Pl: nanoocp.gp.gp_Pln, L: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Lin2d: ...

    @overload
    @staticmethod
    def Project(Pl: nanoocp.gp.gp_Pln, C: nanoocp.gp.gp_Circ) -> nanoocp.gp.gp_Circ2d: ...

    @overload
    @staticmethod
    def Project(Pl: nanoocp.gp.gp_Pln, E: nanoocp.gp.gp_Elips) -> nanoocp.gp.gp_Elips2d: ...

    @overload
    @staticmethod
    def Project(Pl: nanoocp.gp.gp_Pln, P: nanoocp.gp.gp_Parab) -> nanoocp.gp.gp_Parab2d: ...

    @overload
    @staticmethod
    def Project(Pl: nanoocp.gp.gp_Pln, H: nanoocp.gp.gp_Hypr) -> nanoocp.gp.gp_Hypr2d: ...

    @overload
    @staticmethod
    def Project(Cy: nanoocp.gp.gp_Cylinder, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Project(Cy: nanoocp.gp.gp_Cylinder, L: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Lin2d: ...

    @overload
    @staticmethod
    def Project(Cy: nanoocp.gp.gp_Cylinder, Ci: nanoocp.gp.gp_Circ) -> nanoocp.gp.gp_Lin2d: ...

    @overload
    @staticmethod
    def Project(Co: nanoocp.gp.gp_Cone, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Project(Co: nanoocp.gp.gp_Cone, L: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Lin2d: ...

    @overload
    @staticmethod
    def Project(Co: nanoocp.gp.gp_Cone, Ci: nanoocp.gp.gp_Circ) -> nanoocp.gp.gp_Lin2d: ...

    @overload
    @staticmethod
    def Project(Sp: nanoocp.gp.gp_Sphere, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Project(Sp: nanoocp.gp.gp_Sphere, Ci: nanoocp.gp.gp_Circ) -> nanoocp.gp.gp_Lin2d: ...

    @overload
    @staticmethod
    def Project(To: nanoocp.gp.gp_Torus, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Project(To: nanoocp.gp.gp_Torus, Ci: nanoocp.gp.gp_Circ) -> nanoocp.gp.gp_Lin2d: ...

    @staticmethod
    def MakePCurveOfType(PC: ProjLib_ProjectedCurve, aC: nanoocp.Geom2d.Geom2d_Curve) -> None:
        """Make empty P-Curve <aC> of relevant to <PC> type"""

    @staticmethod
    def IsAnaSurf(theAS: nanoocp.Adaptor3d.Adaptor3d_Surface) -> bool:
        """
        Returns "true" if surface is analytical, that is it can be
        Plane, Cylinder, Cone, Sphere, Torus.
        For all other types of surface method returns "false".
        """

class ProjLib_Projector:
    """Root class for projection algorithms, stores the result."""

    def __init__(self) -> None:
        """Sets the type to OtherCurve"""

    def IsDone(self) -> bool: ...

    def Done(self) -> None:
        """Set isDone = true;"""

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def SetBSpline(self, C: nanoocp.Geom2d.Geom2d_BSplineCurve) -> None: ...

    def SetBezier(self, C: nanoocp.Geom2d.Geom2d_BezierCurve) -> None: ...

    def SetType(self, Type: nanoocp.GeomAbs.GeomAbs_CurveType) -> None: ...

    def IsPeriodic(self) -> bool: ...

    def SetPeriodic(self) -> None: ...

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @overload
    def Project(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def Project(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def Project(self, E: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def Project(self, H: nanoocp.gp.gp_Hypr) -> None: ...

    def UFrame(self, CFirst: float, CLast: float, UFirst: float, Period: float) -> None:
        """
        Translates the 2d curve
        to set the part of the curve [CFirst, CLast]
        in the range [ UFirst, UFirst + Period [
        """

    def VFrame(self, CFirst: float, CLast: float, VFirst: float, Period: float) -> None:
        """
        Translates the 2d curve
        to set the part of the curve [CFirst, CLast]
        in the range [ VFirst, VFirst + Period [
        """

class ProjLib_CompProjectedCurve(nanoocp.Adaptor2d.Adaptor2d_Curve2d):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Tol3d: float, S: nanoocp.Adaptor3d.Adaptor3d_Surface, C: nanoocp.Adaptor3d.Adaptor3d_Curve, MaxDist: float = -1.0) -> None:
        """
        this constructor tries to optimize the search using the
        assumption that maximum distance between surface and curve less or
        equal then MaxDist.
        if MaxDist < 0 then algorithm try to find all solutions
        Tolerances of parameters are calculated automatically.
        """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, C: nanoocp.Adaptor3d.Adaptor3d_Curve, TolU: float, TolV: float) -> None:
        """try to find all solutions"""

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, C: nanoocp.Adaptor3d.Adaptor3d_Curve, TolU: float, TolV: float, MaxDist: float) -> None:
        """
        this constructor tries to optimize the search using the
        assumption that maximum distance between surface and curve less or
        equal then MaxDist.
        if MaxDist < 0 then algorithm works as above.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Shallow copy of adaptor"""

    def Init(self) -> None:
        """
        computes a set of projected point and determine the
        continuous parts of the projected curves. The points
        corresponding to a projection on the bounds of the surface are
        included in this set of points.
        """

    def Perform(self) -> None:
        """
        Performs projecting for given curve.
        If projecting uses approximation,
        approximation parameters can be set before by corresponding methods
        SetTol3d(...), SeContinuity(...), SetMaxDegree(...), SetMaxSeg(...)
        """

    def SetTol3d(self, theTol3d: float) -> None:
        """Set the parameter, which defines 3d tolerance of approximation."""

    def SetContinuity(self, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Set the parameter, which defines curve continuity.
        Default value is GeomAbs_C2;
        """

    def SetMaxDegree(self, theMaxDegree: int) -> None:
        """
        Set max possible degree of result BSpline curve2d, which is got by approximation.
        If MaxDegree < 0, algorithm uses values that are chosen depending of types curve 3d
        and surface.
        """

    def SetMaxSeg(self, theMaxSeg: int) -> None:
        """
        Set the parameter, which defines maximal value of parametric intervals the projected
        curve can be cut for approximation. If MaxSeg < 0, algorithm uses default
        value = 16.
        """

    def SetProj2d(self, theProj2d: bool) -> None:
        """Set the parameter, which defines necessity of 2d results."""

    def SetProj3d(self, theProj3d: bool) -> None:
        """Set the parameter, which defines necessity of 3d results."""

    @overload
    def Load(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """Changes the surface."""

    @overload
    def Load(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """Changes the curve."""

    def GetSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def GetTolerance(self) -> tuple[float, float]: ...

    def NbCurves(self) -> int:
        """returns the number of continuous part of the projected curve"""

    def Bounds(self, Index: int) -> tuple[float, float]:
        """returns the bounds of the continuous part corresponding to Index"""

    def IsSinglePnt(self, Index: int, P: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        returns True if part of projection with number Index is a single point and writes
        its coordinates in P
        """

    def IsUIso(self, Index: int) -> tuple[bool, float]:
        """
        returns True if part of projection with number Index is an u-isoparametric curve of
        input surface
        """

    def IsVIso(self, Index: int) -> tuple[bool, float]:
        """
        returns True if part of projection with number Index is an v-isoparametric curve of
        input surface
        """

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if N < 1.
        Raised if N > 2.
        """

    def FirstParameter(self) -> float:
        """
        Returns the first parameter of the curve C
        which has a projection on S.
        """

    def LastParameter(self) -> float:
        """
        Returns the last parameter of the curve C
        which has a projection on S.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns the Continuity used in the approximation."""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals which define
        an S continuous part of the projected curve
        """

    def Trim(self, FirstParam: float, LastParam: float, Tol: float) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 2d points confusion.
        If <First> >= <Last>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the parameters corresponding to
        S discontinuities.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def MaxDistance(self, Index: int) -> float:
        """
        returns the maximum distance between
        curve to project and surface
        """

    def GetSequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]: ...

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    def ResultIsPoint(self, theIndex: int) -> bool:
        """
        Returns true if result of projecting of the curve interval
        with number Index is point.
        """

    def GetResult2dUApproxError(self, theIndex: int) -> float:
        """
        Returns the error of approximation of U parameter 2d-curve as a result
        projecting of the curve interval with number Index.
        """

    def GetResult2dVApproxError(self, theIndex: int) -> float:
        """
        Returns the error of approximation of V parameter 2d-curve as a result
        projecting of the curve interval with number Index.
        """

    def GetResult3dApproxError(self, theIndex: int) -> float:
        """
        Returns the error of approximation of 3d-curve as a result
        projecting of the curve interval with number Index.
        """

    def GetResult2dC(self, theIndex: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Returns the resulting 2d-curve of projecting
        of the curve interval with number Index.
        """

    def GetResult3dC(self, theIndex: int) -> nanoocp.Geom.Geom_Curve:
        """
        Returns the resulting 3d-curve of projecting
        of the curve interval with number Index.
        """

    def GetResult2dP(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the resulting 2d-point of projecting
        of the curve interval with number Index.
        """

    def GetResult3dP(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the resulting 3d-point of projecting
        of the curve interval with number Index.
        """

    def GetProj2d(self) -> bool:
        """Returns the parameter, which defines necessity of only 2d results."""

    def GetProj3d(self) -> bool:
        """Returns the parameter, which defines necessity of only 3d results."""

class ProjLib_ComputeApprox:
    """
    Approximate the projection of a 3d curve on an
    analytic surface and stores the result in Approx.
    The result is a 2d curve.
    For approximation some parameters are used, including
    required tolerance of approximation.
    Tolerance is maximal possible value of 3d deviation of 3d projection of projected curve from
    "exact" 3d projection. Since algorithm searches 2d curve on surface, required 2d tolerance is
    computed from 3d tolerance with help of U,V resolutions of surface. 3d and 2d tolerances have
    sense only for curves on surface, it defines precision of projecting and approximation and have
    nothing to do with distance between the projected curve and the surface.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor, it only sets some initial values for class fields."""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Tol: float) -> None:
        """
        <Tol> is the tolerance with which the approximation is performed.
        Other parameters for approximation have default values.
        """

    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Performs projecting.
        In case of approximation current values of parameters are used:
        default values or set by corresponding methods Set...
        """

    def SetTolerance(self, theTolerance: float) -> None:
        """
        Set tolerance of approximation.
        Default value is Precision::Confusion().
        """

    def SetDegree(self, theDegMin: int, theDegMax: int) -> None:
        """
        Set min and max possible degree of result BSpline curve2d, which is got by approximation.
        If theDegMin/Max < 0, algorithm uses values that are chosen depending of types curve 3d
        and surface.
        """

    def SetMaxSegments(self, theMaxSegments: int) -> None:
        """
        Set the parameter, which defines maximal value of parametric intervals the projected
        curve can be cut for approximation. If theMaxSegments < 0, algorithm uses default
        value = 1000.
        """

    def SetBndPnt(self, theBndPnt: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """
        Set the parameter, which defines type of boundary condition between segments during
        approximation. It can be AppParCurves_PassPoint or AppParCurves_TangencyPoint. Default value
        is AppParCurves_TangencyPoint;
        """

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    def Tolerance(self) -> float:
        """returns the reached Tolerance."""

class ProjLib_ComputeApproxOnPolarSurface:
    """
    Approximate the projection of a 3d curve on an
    polar surface and stores the result in Approx.
    The result is a 2d curve. The evaluation of the
    current point of the 2d curve is done with the
    evaluation of the extrema P3d - Surface.
    For approximation some parameters are used, including
    required tolerance of approximation.
    Tolerance is maximal possible value of 3d deviation of 3d projection of projected curve from
    "exact" 3d projection. Since algorithm searches 2d curve on surface, required 2d tolerance is
    computed from 3d tolerance with help of U,V resolutions of surface. 3d and 2d tolerances have
    sense only for curves on surface, it defines precision of projecting and approximation and have
    nothing to do with distance between the projected curve and the surface.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor, it only sets some initial values for class fields."""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Tol: float = 0.0001) -> None:
        """Constructor, which performs projecting."""

    @overload
    def __init__(self, InitCurve2d: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Tol: float) -> None:
        """
        Constructor, which performs projecting, using initial curve 2d InitCurve2d, which is any rough
        approximation of result curve. Parameter Tol is 3d tolerance of approximation.
        """

    @overload
    def __init__(self, InitCurve2d: nanoocp.Adaptor2d.Adaptor2d_Curve2d, InitCurve2dBis: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Tol: float) -> None:
        """
        Constructor, which performs projecting, using two initial curves 2d: InitCurve2d and
        InitCurve2dBis that are any rough approximations of result curves. This constructor is used to
        get two pcurves for seem edge. Parameter Tol is 3d tolerance of approximation.
        """

    def SetDegree(self, theDegMin: int, theDegMax: int) -> None:
        """
        Set min and max possible degree of result BSpline curve2d, which is got by approximation.
        If theDegMin/Max < 0, algorithm uses values min = 2, max = 8.
        """

    def SetMaxSegments(self, theMaxSegments: int) -> None:
        """
        Set the parameter, which defines maximal value of parametric intervals the projected
        curve can be cut for approximation. If theMaxSegments < 0, algorithm uses default
        value = 1000.
        """

    def SetBndPnt(self, theBndPnt: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """
        Set the parameter, which defines type of boundary condition between segments during
        approximation. It can be AppParCurves_PassPoint or AppParCurves_TangencyPoint. Default value
        is AppParCurves_TangencyPoint.
        """

    def SetMaxDist(self, theMaxDist: float) -> None:
        """
        Set the parameter, which defines maximal possible distance between projected curve and
        surface. It is used only for projecting on not analytical surfaces. If theMaxDist < 0,
        algorithm uses default value 100.*Tolerance. If real distance between curve and surface more
        then theMaxDist, algorithm stops working.
        """

    def SetTolerance(self, theTolerance: float) -> None:
        """
        Set the tolerance used to project
        the curve on the surface.
        Default value is Precision::Approximation().
        """

    @overload
    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Method, which performs projecting, using default values of parameters or
        they must be set by corresponding methods before using.
        """

    @overload
    def Perform(self, InitCurve2d: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        Method, which performs projecting, using default values of parameters or
        they must be set by corresponding methods before using.
        Parameter InitCurve2d is any rough estimation of 2d result curve.
        """

    def BuildInitialCurve2d(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Builds initial 2d curve as BSpline with degree = 1 using Extrema algorithm.
        Method is used in method Perform(...).
        """

    def ProjectUsingInitialCurve2d(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, InitCurve2d: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        Method, which performs projecting.
        Method is used in method Perform(...).
        """

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """Returns result curve 2d."""

    def Curve2d(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns second 2d curve."""

    def IsDone(self) -> bool: ...

    def Tolerance(self) -> float:
        """returns the reached Tolerance."""

class ProjLib_Cone(ProjLib_Projector):
    """Projects elementary curves on a cone."""

    @overload
    def __init__(self) -> None:
        """Undefined projection."""

    @overload
    def __init__(self, Co: nanoocp.gp.gp_Cone) -> None:
        """Projection on the cone <Co>."""

    @overload
    def __init__(self, Co: nanoocp.gp.gp_Cone, L: nanoocp.gp.gp_Lin) -> None:
        """Projection of the line <L> on the cone <Co>."""

    @overload
    def __init__(self, Co: nanoocp.gp.gp_Cone, C: nanoocp.gp.gp_Circ) -> None:
        """Projection of the circle <C> on the cone <Co>."""

    def Init(self, Co: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def Project(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def Project(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def Project(self, E: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def Project(self, H: nanoocp.gp.gp_Hypr) -> None: ...

class ProjLib_Cylinder(ProjLib_Projector):
    """Projects elementary curves on a cylinder."""

    @overload
    def __init__(self) -> None:
        """Undefined projection."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder) -> None:
        """Projection on the cylinder <Cyl>."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, L: nanoocp.gp.gp_Lin) -> None:
        """Projection of the line <L> on the cylinder <Cyl>."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, C: nanoocp.gp.gp_Circ) -> None:
        """Projection of the circle <C> on the cylinder <Cyl>."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, E: nanoocp.gp.gp_Elips) -> None:
        """Projection of the ellipse <E> on the cylinder <Cyl>."""

    def Init(self, Cyl: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def Project(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def Project(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def Project(self, E: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def Project(self, H: nanoocp.gp.gp_Hypr) -> None: ...

class ProjLib_ProjectedCurve(nanoocp.Adaptor2d.Adaptor2d_Curve2d):
    """
    Compute the 2d-curve. Try to solve the particular
    case if possible. Otherwise, an approximation is
    done. For approximation some parameters are used, including
    required tolerance of approximation.
    Tolerance is maximal possible value of 3d deviation of 3d projection of projected curve from
    "exact" 3d projection. Since algorithm searches 2d curve on surface, required 2d tolerance is
    computed from 3d tolerance with help of U,V resolutions of surface. 3d and 2d tolerances have
    sense only for curves on surface, it defines precision of projecting and approximation and have
    nothing to do with distance between the projected curve and the surface.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor, it only sets some initial values for class fields."""

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """Constructor with initialisation field mySurface"""

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Constructor, which performs projecting.
        If projecting uses approximation, default parameters are used, in particular, 3d tolerance of
        approximation is Precision::Confusion()
        """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Tol: float) -> None:
        """
        Constructor, which performs projecting.
        If projecting uses approximation, 3d tolerance is Tol, default parameters are used,
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, Tolerance: float) -> None:
        """
        Changes the tolerance used to project
        the curve on the surface
        """

    @overload
    def Load(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """Changes the Surface."""

    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Performs projecting for given curve.
        If projecting uses approximation,
        approximation parameters can be set before by corresponding methods
        SetDegree(...), SetMaxSegmets(...), SetBndPnt(...), SetMaxDist(...)
        """

    def SetDegree(self, theDegMin: int, theDegMax: int) -> None:
        """
        Set min and max possible degree of result BSpline curve2d, which is got by approximation.
        If theDegMin/Max < 0, algorithm uses values that are chosen depending of types curve 3d
        and surface.
        """

    def SetMaxSegments(self, theMaxSegments: int) -> None:
        """
        Set the parameter, which defines maximal value of parametric intervals the projected
        curve can be cut for approximation. If theMaxSegments < 0, algorithm uses default
        value = 1000.
        """

    def SetBndPnt(self, theBndPnt: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """
        Set the parameter, which defines type of boundary condition between segments during
        approximation. It can be AppParCurves_PassPoint or AppParCurves_TangencyPoint. Default value
        is AppParCurves_TangencyPoint;
        """

    def SetMaxDist(self, theMaxDist: float) -> None:
        """
        Set the parameter, which degines maximal possible distance between projected curve and
        surface. It uses only for projecting on not analytical surfaces. If theMaxDist < 0, algorithm
        uses default value 100.*Tolerance. If real distance between curve and surface more then
        theMaxDist, algorithm stops working.
        """

    def GetSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def GetTolerance(self) -> float:
        """
        returns the tolerance reached if an approximation
        is Done.
        """

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    def D3(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    def Resolution(self, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve:
        """
        Warning! This will NOT make a copy of the Bezier Curve
        If you want to modify the Curve please make a copy
        yourself. Also it will NOT trim the surface to myFirst/Last.
        """

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        Warning! This will NOT make a copy of the BSpline Curve
        If you want to modify the Curve please make a copy
        yourself. Also it will NOT trim the surface to myFirst/Last.
        """

class ProjLib_Plane(ProjLib_Projector):
    """Projects elementary curves on a plane."""

    @overload
    def __init__(self) -> None:
        """Undefined projection."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Pln) -> None:
        """Projection on the plane <Pl>."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Pln, L: nanoocp.gp.gp_Lin) -> None:
        """Projection of the line <L> on the plane <Pl>."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Pln, C: nanoocp.gp.gp_Circ) -> None:
        """Projection of the circle <C> on the plane <Pl>."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Pln, E: nanoocp.gp.gp_Elips) -> None:
        """Projection of the ellipse <E> on the plane <Pl>."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Pln, P: nanoocp.gp.gp_Parab) -> None:
        """Projection of the parabola <P> on the plane <Pl>."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Pln, H: nanoocp.gp.gp_Hypr) -> None:
        """Projection of the hyperbola <H> on the plane <Pl>."""

    def Init(self, Pl: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def Project(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def Project(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def Project(self, E: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def Project(self, H: nanoocp.gp.gp_Hypr) -> None: ...

class ProjLib_PrjFunc(nanoocp.math.math_FunctionSetWithDerivatives):
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, FixVal: float, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Fix: int) -> None: ...

    def NbVariables(self) -> int:
        """returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Solution(self) -> nanoocp.gp.gp_Pnt2d:
        """returns point on surface"""

class ProjLib_PrjResolve:
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Fix: int) -> None: ...

    def Perform(self, t: float, U: float, V: float, Tol: nanoocp.gp.gp_Pnt2d, Inf: nanoocp.gp.gp_Pnt2d, Sup: nanoocp.gp.gp_Pnt2d, FTol: float = -1.0, StrictInside: bool = False) -> None:
        """
        Calculates the ort from C(t) to S with a close point.
        The close point is defined by the parameter values U0 and V0.
        The function F(u,v)=distance(S(u,v),C(t)) has an extremum when gradient(F)=0.
        The algorithm searches a zero near the close point.
        """

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def Solution(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the point of the extremum distance."""

class ProjLib_ProjectOnPlane(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """
    Class used to project a 3d curve on a plane. The
    result will be a 3d curve.

    You can ask the projected curve to have the same
    parametrization as the original curve.

    The projection can be done along every direction not
    parallel to the plane.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Ax3) -> None:
        """
        The projection will be normal to the Plane defined
        by the Ax3 <Pl>.
        """

    @overload
    def __init__(self, Pl: nanoocp.gp.gp_Ax3, D: nanoocp.gp.gp_Dir) -> None:
        """
        The projection will be along the direction <D> on
        the plane defined by the Ax3 <Pl>.
        raises if the direction <D> is parallel to the
        plane <Pl>.
        """

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    def Load(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Tolerance: float, KeepParametrization: bool = True) -> None:
        """
        Sets the Curve and perform the projection.
        if <KeepParametrization> is true, the parametrization
        of the Projected Curve <PC> will be the same as
        the parametrization of the initial curve <C>.
        It means: proj(C(u)) = PC(u) for each u.
        Otherwise, the parametrization may change.
        """

    def GetPlane(self) -> nanoocp.gp.gp_Ax3: ...

    def GetDirection(self) -> nanoocp.gp.gp_Dir: ...

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def GetResult(self) -> nanoocp.GeomAdaptor.GeomAdaptor_Curve: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter theU on the curve."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """
        Computes the point of parameter theU on the curve with its first derivative.
        Raised if the continuity of the current interval is not C1.
        """

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """
        Returns the point and the first and second derivatives at parameter theU.
        Raised if the continuity of the current interval is not C2.
        """

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """
        Returns the point and the first, second and third derivatives at parameter theU.
        Raised if the continuity of the current interval is not C3.
        """

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """
        Returns the derivative of order theN at parameter theU.
        Raised if the continuity of the current interval is not CN.
        Raised if theN < 1.
        """

    def Resolution(self, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve:
        """
        Warning ! this will NOT make a copy of the
        Bezier Curve : If you want to modify
        the Curve please make a copy yourself
        Also it will NOT trim the surface to
        myFirst/Last.
        """

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        Warning ! this will NOT make a copy of the
        BSpline Curve : If you want to modify
        the Curve please make a copy yourself
        Also it will NOT trim the surface to
        myFirst/Last.
        """

class ProjLib_ProjectOnSurface:
    """
    Project a curve on a surface. The result
    (a 3D Curve) will be an approximation
    """

    @overload
    def __init__(self) -> None:
        """Create an empty projector."""

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """Create a projector normally to the surface <S>."""

    @overload
    def Load(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Set the Surface to <S>.
        To compute the projection, you have to Load the Curve.
        """

    @overload
    def Load(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Tolerance: float) -> None:
        """Compute the projection of the curve <C> on the Surface."""

    def IsDone(self) -> bool: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

class ProjLib_Sphere(ProjLib_Projector):
    """Projects elementary curves on a sphere."""

    @overload
    def __init__(self) -> None:
        """Undefined projection."""

    @overload
    def __init__(self, Sp: nanoocp.gp.gp_Sphere) -> None:
        """Projection on the sphere <Sp>."""

    @overload
    def __init__(self, Sp: nanoocp.gp.gp_Sphere, C: nanoocp.gp.gp_Circ) -> None:
        """Projection of the circle <C> on the sphere <Sp>."""

    def Init(self, Sp: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def Project(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def Project(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def Project(self, E: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def Project(self, H: nanoocp.gp.gp_Hypr) -> None: ...

    def SetInBounds(self, U: float) -> None:
        """
        Set the point of parameter U on C in the natural
        restrictions of the sphere.
        """

class ProjLib_Torus(ProjLib_Projector):
    """Projects elementary curves on a torus."""

    @overload
    def __init__(self) -> None:
        """Undefined projection."""

    @overload
    def __init__(self, To: nanoocp.gp.gp_Torus) -> None:
        """Projection on the torus <To>."""

    @overload
    def __init__(self, To: nanoocp.gp.gp_Torus, C: nanoocp.gp.gp_Circ) -> None:
        """Projection of the circle <C> on the torus <To>."""

    def Init(self, To: nanoocp.gp.gp_Torus) -> None: ...

    @overload
    def Project(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def Project(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def Project(self, E: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def Project(self, H: nanoocp.gp.gp_Hypr) -> None: ...

ProjLib_HCompProjectedCurve: TypeAlias = ProjLib_CompProjectedCurve

ProjLib_HProjectedCurve: TypeAlias = ProjLib_ProjectedCurve

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
ProjLib_HSequenceOfHSequenceOfPnt = nanoocp.NCollection.NCollection_HSequence[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]
ProjLib_SequenceOfHSequenceOfPnt = nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]
