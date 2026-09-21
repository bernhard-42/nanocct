"""OCCT package GeomFill (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.AppBlend
import nanoocp.Approx
import nanoocp.Convert
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Law
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class GeomFill_ApproxStyle(enum.IntEnum):
    GeomFill_Section = 0

    GeomFill_Location = 1

GeomFill_Section: GeomFill_ApproxStyle = GeomFill_ApproxStyle.GeomFill_Section

GeomFill_Location: GeomFill_ApproxStyle = GeomFill_ApproxStyle.GeomFill_Location

class GeomFill_FillingStyle(enum.IntEnum):
    """
    Defines the three filling styles used in this package
    -   GeomFill_Stretch - the style with the flattest patches
    -   GeomFill_Coons - a rounded style of patch with
    less depth than those of Curved
    -   GeomFill_Curved - the style with the most rounded patches.
    """

    GeomFill_StretchStyle = 0

    GeomFill_CoonsStyle = 1

    GeomFill_CurvedStyle = 2

GeomFill_StretchStyle: GeomFill_FillingStyle = GeomFill_FillingStyle.GeomFill_StretchStyle

GeomFill_CoonsStyle: GeomFill_FillingStyle = GeomFill_FillingStyle.GeomFill_CoonsStyle

GeomFill_CurvedStyle: GeomFill_FillingStyle = GeomFill_FillingStyle.GeomFill_CurvedStyle

class GeomFill_PipeError(enum.IntEnum):
    GeomFill_PipeOk = 0

    GeomFill_PipeNotOk = 1

    GeomFill_PlaneNotIntersectGuide = 2

    GeomFill_ImpossibleContact = 3

GeomFill_PipeOk: GeomFill_PipeError = GeomFill_PipeError.GeomFill_PipeOk

GeomFill_PipeNotOk: GeomFill_PipeError = GeomFill_PipeError.GeomFill_PipeNotOk

GeomFill_PlaneNotIntersectGuide: GeomFill_PipeError = ...

GeomFill_ImpossibleContact: GeomFill_PipeError = GeomFill_PipeError.GeomFill_ImpossibleContact

class GeomFill_Trihedron(enum.IntEnum):
    GeomFill_IsCorrectedFrenet = 0

    GeomFill_IsFixed = 1

    GeomFill_IsFrenet = 2

    GeomFill_IsConstantNormal = 3

    GeomFill_IsDarboux = 4

    GeomFill_IsGuideAC = 5

    GeomFill_IsGuidePlan = 6

    GeomFill_IsGuideACWithContact = 7

    GeomFill_IsGuidePlanWithContact = 8

    GeomFill_IsDiscreteTrihedron = 9

GeomFill_IsCorrectedFrenet: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsCorrectedFrenet

GeomFill_IsFixed: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsFixed

GeomFill_IsFrenet: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsFrenet

GeomFill_IsConstantNormal: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsConstantNormal

GeomFill_IsDarboux: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsDarboux

GeomFill_IsGuideAC: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsGuideAC

GeomFill_IsGuidePlan: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsGuidePlan

GeomFill_IsGuideACWithContact: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsGuideACWithContact

GeomFill_IsGuidePlanWithContact: GeomFill_Trihedron = ...

GeomFill_IsDiscreteTrihedron: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsDiscreteTrihedron

class GeomFill:
    """Tools and Data to filling Surface and Sweep Surfaces"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill) -> None: ...

    @staticmethod
    def Surface(Curve1: nanoocp.Geom.Geom_Curve | None, Curve2: nanoocp.Geom.Geom_Curve | None) -> nanoocp.Geom.Geom_Surface:
        """Builds a ruled surface between the two curves, Curve1 and Curve2."""

    @overload
    @staticmethod
    def GetCircle(TConv: nanoocp.Convert.Convert_ParameterisationType, ns1: nanoocp.gp.gp_Vec, ns2: nanoocp.gp.gp_Vec, nplan: nanoocp.gp.gp_Vec, pt1: nanoocp.gp.gp_Pnt, pt2: nanoocp.gp.gp_Pnt, Rayon: float, Center: nanoocp.gp.gp_Pnt, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def GetCircle(TConv: nanoocp.Convert.Convert_ParameterisationType, ns1: nanoocp.gp.gp_Vec, ns2: nanoocp.gp.gp_Vec, dn1w: nanoocp.gp.gp_Vec, dn2w: nanoocp.gp.gp_Vec, nplan: nanoocp.gp.gp_Vec, dnplan: nanoocp.gp.gp_Vec, pts1: nanoocp.gp.gp_Pnt, pts2: nanoocp.gp.gp_Pnt, tang1: nanoocp.gp.gp_Vec, tang2: nanoocp.gp.gp_Vec, Rayon: float, DRayon: float, Center: nanoocp.gp.gp_Pnt, DCenter: nanoocp.gp.gp_Vec, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    @staticmethod
    def GetCircle(TConv: nanoocp.Convert.Convert_ParameterisationType, ns1: nanoocp.gp.gp_Vec, ns2: nanoocp.gp.gp_Vec, dn1w: nanoocp.gp.gp_Vec, dn2w: nanoocp.gp.gp_Vec, d2n1w: nanoocp.gp.gp_Vec, d2n2w: nanoocp.gp.gp_Vec, nplan: nanoocp.gp.gp_Vec, dnplan: nanoocp.gp.gp_Vec, d2nplan: nanoocp.gp.gp_Vec, pts1: nanoocp.gp.gp_Pnt, pts2: nanoocp.gp.gp_Pnt, tang1: nanoocp.gp.gp_Vec, tang2: nanoocp.gp.gp_Vec, Dtang1: nanoocp.gp.gp_Vec, Dtang2: nanoocp.gp.gp_Vec, Rayon: float, DRayon: float, D2Rayon: float, Center: nanoocp.gp.gp_Pnt, DCenter: nanoocp.gp.gp_Vec, D2Center: nanoocp.gp.gp_Vec, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @staticmethod
    def GetShape(MaxAng: float) -> tuple[int, int, int, nanoocp.Convert.Convert_ParameterisationType]: ...

    @staticmethod
    def Knots(TypeConv: nanoocp.Convert.Convert_ParameterisationType, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def Mults(TypeConv: nanoocp.Convert.Convert_ParameterisationType, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @staticmethod
    def GetMinimalWeights(TConv: nanoocp.Convert.Convert_ParameterisationType, AngleMin: float, AngleMax: float, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def GetTolerance(TConv: nanoocp.Convert.Convert_ParameterisationType, AngleMin: float, Radius: float, AngularTol: float, SpatialTol: float) -> float:
        """
        Used by the generical classes to determine
        Tolerance for approximation
        """

class GeomFill_AppSurf(nanoocp.AppBlend.AppBlend_Approx):
    """
    Approximate a BSplineSurface passing by all the
    curves described in the SectionGenerator
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_AppSurf) -> None: ...

    def Init(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: bool = False) -> None: ...

    def SetParType(self, ParType: nanoocp.Approx.Approx_ParametrizationType) -> None:
        """Define the type of parametrization used in the approximation"""

    def SetContinuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Define the Continuity used in the approximation"""

    def SetCriteriumWeight(self, W1: float, W2: float, W3: float) -> None:
        """
        define the Weights associed to the criterium used in
        the optimization.

        if Wi <= 0
        """

    def ParType(self) -> nanoocp.Approx.Approx_ParametrizationType:
        """returns the type of parametrization used in the approximation"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """returns the Continuity used in the approximation"""

    def CriteriumWeight(self) -> tuple[float, float, float]:
        """
        returns the Weights (as percent) associed to the criterium used in
        the optimization.
        """

    @overload
    def Perform(self, Lin: GeomFill_Line | None, SecGen: GeomFill_SectionGenerator, SpApprox: bool = False) -> None: ...

    @overload
    def Perform(self, Lin: GeomFill_Line | None, SecGen: GeomFill_SectionGenerator, NbMaxP: int) -> None: ...

    def PerformSmoothing(self, Lin: GeomFill_Line | None, SecGen: GeomFill_SectionGenerator) -> None: ...

    def IsDone(self) -> bool: ...

    def SurfShape(self) -> tuple[int, int, int, int, int, int]: ...

    def Surface(self, TPoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], TWeights: nanoocp.NCollection.NCollection_Array2[float], TUKnots: nanoocp.NCollection.NCollection_Array1[float], TVKnots: nanoocp.NCollection.NCollection_Array1[float], TUMults: nanoocp.NCollection.NCollection_Array1[int], TVMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def UDegree(self) -> int: ...

    def VDegree(self) -> int: ...

    def SurfPoles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]: ...

    def SurfWeights(self) -> nanoocp.NCollection.NCollection_Array2[float]: ...

    def SurfUKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfVKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfUMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def SurfVMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def NbCurves2d(self) -> int: ...

    def Curves2dShape(self) -> tuple[int, int, int]: ...

    def Curve2d(self, Index: int, TPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TKnots: nanoocp.NCollection.NCollection_Array1[float], TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Curves2dDegree(self) -> int: ...

    def Curve2dPoles(self, Index: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]: ...

    def Curves2dKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def Curves2dMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def TolReached(self) -> tuple[float, float]: ...

    def TolCurveOnSurf(self, Index: int) -> float: ...

class GeomFill_AppSweep(nanoocp.AppBlend.AppBlend_Approx):
    """
    Approximate a sweep surface passing by all the
    curves described in the SweepSectionGenerator.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_AppSweep) -> None: ...

    def Init(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: bool = False) -> None: ...

    def SetParType(self, ParType: nanoocp.Approx.Approx_ParametrizationType) -> None:
        """Define the type of parametrization used in the approximation"""

    def SetContinuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Define the Continuity used in the approximation"""

    def SetCriteriumWeight(self, W1: float, W2: float, W3: float) -> None:
        """
        define the Weights associed to the criterium used in
        the optimization.

        if Wi <= 0
        """

    def ParType(self) -> nanoocp.Approx.Approx_ParametrizationType:
        """returns the type of parametrization used in the approximation"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """returns the Continuity used in the approximation"""

    def CriteriumWeight(self) -> tuple[float, float, float]:
        """
        returns the Weights (as percent) associed to the criterium used in
        the optimization.
        """

    @overload
    def Perform(self, Lin: GeomFill_Line | None, SecGen: GeomFill_SweepSectionGenerator, SpApprox: bool = False) -> None: ...

    @overload
    def Perform(self, Lin: GeomFill_Line | None, SecGen: GeomFill_SweepSectionGenerator, NbMaxP: int) -> None: ...

    def PerformSmoothing(self, Lin: GeomFill_Line | None, SecGen: GeomFill_SweepSectionGenerator) -> None: ...

    def IsDone(self) -> bool: ...

    def SurfShape(self) -> tuple[int, int, int, int, int, int]: ...

    def Surface(self, TPoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], TWeights: nanoocp.NCollection.NCollection_Array2[float], TUKnots: nanoocp.NCollection.NCollection_Array1[float], TVKnots: nanoocp.NCollection.NCollection_Array1[float], TUMults: nanoocp.NCollection.NCollection_Array1[int], TVMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def UDegree(self) -> int: ...

    def VDegree(self) -> int: ...

    def SurfPoles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]: ...

    def SurfWeights(self) -> nanoocp.NCollection.NCollection_Array2[float]: ...

    def SurfUKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfVKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfUMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def SurfVMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def NbCurves2d(self) -> int: ...

    def Curves2dShape(self) -> tuple[int, int, int]: ...

    def Curve2d(self, Index: int, TPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TKnots: nanoocp.NCollection.NCollection_Array1[float], TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Curves2dDegree(self) -> int: ...

    def Curve2dPoles(self, Index: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]: ...

    def Curves2dKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def Curves2dMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def TolReached(self) -> tuple[float, float]: ...

    def TolCurveOnSurf(self, Index: int) -> float: ...

class GeomFill_BezierCurves:
    """
    This class provides an algorithm for constructing a Bezier surface filled from
    contiguous Bezier curves which form its boundaries.
    The algorithm accepts two, three or four Bezier curves
    as the boundaries of the target surface.
    A range of filling styles - more or less rounded, more or less flat - is available.
    A BezierCurves object provides a framework for:
    -   defining the boundaries, and the filling style of the surface
    -   implementing the construction algorithm
    -   consulting the result.
    Warning
    Some problems may show up with rational curves.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty framework for building a Bezier
        surface from contiguous Bezier curves.
        You use the Init function to define the boundaries of the surface.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_BezierCurve | None, C2: nanoocp.Geom.Geom_BezierCurve | None, Type: GeomFill_FillingStyle) -> None:
        """
        Constructs a framework for building a Bezier surface
        from the two contiguous Bezier curves, C1 and C2
        Raises Standard_ConstructionError if the curves are not contiguous.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_BezierCurve | None, C2: nanoocp.Geom.Geom_BezierCurve | None, C3: nanoocp.Geom.Geom_BezierCurve | None, Type: GeomFill_FillingStyle) -> None:
        """
        Constructs a framework for building a Bezier surface
        from the three contiguous Bezier curves, C1, C2 and C3
        Raises Standard_ConstructionError if the curves are not contiguous.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_BezierCurve | None, C2: nanoocp.Geom.Geom_BezierCurve | None, C3: nanoocp.Geom.Geom_BezierCurve | None, C4: nanoocp.Geom.Geom_BezierCurve | None, Type: GeomFill_FillingStyle) -> None:
        """
        Constructs a framework for building a Bezier surface
        from the four contiguous Bezier curves, C1, C2, C3 and C4
        Raises Standard_ConstructionError if the curves are not contiguous.
        """

    @overload
    def __init__(self, theOther: GeomFill_BezierCurves) -> None: ...

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_BezierCurve | None, C2: nanoocp.Geom.Geom_BezierCurve | None, C3: nanoocp.Geom.Geom_BezierCurve | None, C4: nanoocp.Geom.Geom_BezierCurve | None, Type: GeomFill_FillingStyle) -> None: ...

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_BezierCurve | None, C2: nanoocp.Geom.Geom_BezierCurve | None, C3: nanoocp.Geom.Geom_BezierCurve | None, Type: GeomFill_FillingStyle) -> None:
        """if the curves cannot be joined"""

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_BezierCurve | None, C2: nanoocp.Geom.Geom_BezierCurve | None, Type: GeomFill_FillingStyle) -> None:
        """
        Initializes or reinitializes this algorithm with two, three,
        or four curves - C1, C2, C3, and C4 - and Type, one
        of the following filling styles:
        -   GeomFill_Stretch - the style with the flattest patch
        -   GeomFill_Coons - a rounded style of patch with
        less depth than that of Curved
        -   GeomFill_Curved - the style with the most rounded patch.
        Exceptions
        Standard_ConstructionError if the curves are not contiguous.
        """

    def Surface(self) -> nanoocp.Geom.Geom_BezierSurface:
        """
        Returns the Bezier surface resulting from the
        computation performed by this algorithm.
        """

class GeomFill_Boundary(nanoocp.Standard.Standard_Transient):
    """
    Root class to define a boundary which will form part of a
    contour around a gap requiring filling.
    Any new type of constrained boundary must inherit this class.
    The GeomFill package provides two classes to define constrained boundaries:
    -   GeomFill_SimpleBound to define an unattached boundary
    -   GeomFill_BoundWithSurf to define a boundary attached to a surface.
    These objects are used to define the boundaries for a
    GeomFill_ConstrainedFilling framework.
    """

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt: ...

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None: ...

    def HasNormals(self) -> bool: ...

    def Norm(self, U: float) -> nanoocp.gp.gp_Vec: ...

    def D1Norm(self, U: float, N: nanoocp.gp.gp_Vec, DN: nanoocp.gp.gp_Vec) -> None: ...

    def Reparametrize(self, First: float, Last: float, HasDF: bool, HasDL: bool, DF: float, DL: float, Rev: bool) -> None: ...

    def Points(self, PFirst: nanoocp.gp.gp_Pnt, PLast: nanoocp.gp.gp_Pnt) -> None: ...

    def Bounds(self) -> tuple[float, float]: ...

    def IsDegenerated(self) -> bool: ...

    @overload
    def Tol3d(self) -> float: ...

    @overload
    def Tol3d(self, Tol: float) -> None: ...

    @overload
    def Tolang(self) -> float: ...

    @overload
    def Tolang(self, Tol: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_BoundWithSurf(GeomFill_Boundary):
    """
    Defines a 3d curve as a boundary for a
    GeomFill_ConstrainedFilling algorithm.
    This curve is attached to an existing surface.
    Defines a constrained boundary for filling
    the computations are done with a CurveOnSurf and a
    normals field defined by the normalized normal to
    the surface along the PCurve.
    Contains fields to allow a reparametrization of curve
    and normals field.
    """

    @overload
    def __init__(self, CurveOnSurf: nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface, Tol3d: float, Tolang: float) -> None:
        """
        Constructs a boundary object defined by the 3d curve CurveOnSurf.
        The surface to be filled along this boundary will be in the
        tolerance range defined by Tol3d.
        What's more, at each point of CurveOnSurf, the angle
        between the normal to the surface to be filled along this
        boundary, and the normal to the surface on which
        CurveOnSurf lies, must not be greater than TolAng.
        This object is to be used as a boundary for a
        GeomFill_ConstrainedFilling framework.
        Warning
        CurveOnSurf is an adapted curve, that is, an object
        which is an interface between:
        -   the services provided by a curve lying on a surface from the package Geom
        -   and those required of the curve by the computation algorithm which uses it.
        The adapted curve is created in the following way:
        occ::handle<Geom_Surface> mySurface = ... ;
        occ::handle<Geom2d_Curve> myParamCurve = ... ;
        // where myParamCurve is a 2D curve in the parametric space of the surface mySurface
        occ::handle<GeomAdaptor_Surface>
        Surface = new
        GeomAdaptor_Surface(mySurface);
        occ::handle<Geom2dAdaptor_Curve>
        ParamCurve = new
        Geom2dAdaptor_Curve(myParamCurve);
        CurveOnSurf = Adaptor3d_CurveOnSurface(ParamCurve,Surface);
        The boundary is then constructed with the CurveOnSurf object:
        double Tol = ... ;
        double TolAng = ... ;
        myBoundary = GeomFill_BoundWithSurf (
        CurveOnSurf, Tol, TolAng );
        """

    @overload
    def __init__(self, theOther: GeomFill_BoundWithSurf) -> None: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt: ...

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None: ...

    def HasNormals(self) -> bool: ...

    def Norm(self, U: float) -> nanoocp.gp.gp_Vec: ...

    def D1Norm(self, U: float, N: nanoocp.gp.gp_Vec, DN: nanoocp.gp.gp_Vec) -> None: ...

    def Reparametrize(self, First: float, Last: float, HasDF: bool, HasDL: bool, DF: float, DL: float, Rev: bool) -> None: ...

    def Bounds(self) -> tuple[float, float]: ...

    def IsDegenerated(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_BSplineCurves:
    """
    An algorithm for constructing a BSpline surface filled
    from contiguous BSpline curves which form its boundaries.
    The algorithm accepts two, three or four BSpline
    curves as the boundaries of the target surface.
    A range of filling styles - more or less rounded, more
    or less flat - is available.
    A BSplineCurves object provides a framework for:
    -   defining the boundaries, and the filling style of the surface
    -   implementing the construction algorithm
    -   consulting the result.
    Warning
    Some problems may show up with rational curves.
    """

    @overload
    def __init__(self) -> None:
        """Constructs a default BSpline surface framework."""

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_BSplineCurve | None, C2: nanoocp.Geom.Geom_BSplineCurve | None, Type: GeomFill_FillingStyle) -> None:
        """
        Constructs a framework for building a BSpline surface from either
        -   the four contiguous BSpline curves, C1, C2, C3 and C4, or
        -   the three contiguous BSpline curves, C1, C2 and C3, or
        -   the two contiguous BSpline curves, C1 and C2.
        The type of filling style Type to be used is one of:
        -   GeomFill_Stretch - the style with the flattest patch
        -   GeomFill_Coons - a rounded style of patch with
        less depth than that of Curved
        -   GeomFill_Curved - the style with the most rounded
        patch.Constructs a framework for building a BSpline
        surface common to the two BSpline curves, C1 and C2.
        Exceptions
        Standard_ConstructionError if the curves are not contiguous.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_BSplineCurve | None, C2: nanoocp.Geom.Geom_BSplineCurve | None, C3: nanoocp.Geom.Geom_BSplineCurve | None, Type: GeomFill_FillingStyle) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_BSplineCurve | None, C2: nanoocp.Geom.Geom_BSplineCurve | None, C3: nanoocp.Geom.Geom_BSplineCurve | None, C4: nanoocp.Geom.Geom_BSplineCurve | None, Type: GeomFill_FillingStyle) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_BSplineCurves) -> None: ...

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_BSplineCurve | None, C2: nanoocp.Geom.Geom_BSplineCurve | None, C3: nanoocp.Geom.Geom_BSplineCurve | None, C4: nanoocp.Geom.Geom_BSplineCurve | None, Type: GeomFill_FillingStyle) -> None: ...

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_BSplineCurve | None, C2: nanoocp.Geom.Geom_BSplineCurve | None, C3: nanoocp.Geom.Geom_BSplineCurve | None, Type: GeomFill_FillingStyle) -> None:
        """if the curves cannot be joined"""

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_BSplineCurve | None, C2: nanoocp.Geom.Geom_BSplineCurve | None, Type: GeomFill_FillingStyle) -> None:
        """
        Initializes or reinitializes this algorithm with two, three,
        or four curves - C1, C2, C3, and C4 - and Type, one
        of the following filling styles:
        -   GeomFill_Stretch - the style with the flattest patch
        -   GeomFill_Coons - a rounded style of patch with
        less depth than that of Curved
        -   GeomFill_Curved - the style with the most rounded patch.
        Exceptions
        Standard_ConstructionError if the curves are not contiguous.
        """

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Returns the BSpline surface Surface resulting from
        the computation performed by this algorithm.
        """

class GeomFill_CircularBlendFunc(nanoocp.Approx.Approx_SweepFunction):
    """
    Circular Blend Function to approximate by
    SweepApproximation from Approx
    """

    @overload
    def __init__(self, Path: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve1: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve2: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Radius: float, Polynomial: bool = False) -> None:
        """
        Create a Blend with a constant radius with 2
        guide-line. <FShape> sets the type of fillet
        surface. The default value is Convert_TgtThetaOver2
        (classical nurbs representation of circles).
        ChFi3d_QuasiAngular corresponds to a nurbs
        representation of circles which parameterisation
        matches the circle one. ChFi3d_Polynomial
        corresponds to a polynomial representation of
        circles.
        """

    @overload
    def __init__(self, theOther: GeomFill_CircularBlendFunc) -> None: ...

    def D0(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        """

    def D2(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        """

    def Nb2dCurves(self) -> int:
        """get the number of 2d curves to approximate."""

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the section is rational or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the fonction
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary (in radian)
        SurfTol error inside the surface.
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if (me) has to be run numerical
        algorithm to perform D0, D1 or D2
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface. A very poor
        estimation is sufficient. This information is useful
        to perform well conditioned rational approximation.
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the maximum section. This
        information is useful to perform well conditioned rational
        approximation.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections. This information is useful to
        perform well conditioned rational approximation.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_TrihedronLaw(nanoocp.Standard.Standard_Transient):
    """To define Trihedron along one Curve"""

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of trihedron law
        @return true
        """

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def ErrorStatus(self) -> GeomFill_PipeError:
        """
        Give a status to the Law
        Returns PipeOk (default implementation)
        """

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """compute Triedrhon on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Triedrhon and derivative Trihedron on curve
        at parameter <Param>
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant"""

    def IsOnlyBy3dCurve(self) -> bool:
        """
        Say if the law is defined, only by the 3d Geometry of
        the set Curve
        Return False by Default.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_ConstantBiNormal(GeomFill_TrihedronLaw):
    """Defined a Trihedron Law where the BiNormal, is fixed"""

    @overload
    def __init__(self, BiNormal: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_ConstantBiNormal) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of trihedron law
        @return true in case if execution end correctly
        """

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """Computes Triedrhon on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        Computes Triedrhon and derivative Trihedron on curve
        at parameter <Param>
        Warning: It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning: It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Gets average value of Tangent(t) and Normal(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Says if the law is Constant."""

    def IsOnlyBy3dCurve(self) -> bool:
        """Return True."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_CornerState:
    """
    Class (should be a structure) storing the
    information about continuity, normals
    parallelism, coons conditions and bounds tangents
    angle on the corner of contour to be filled.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_CornerState) -> None: ...

    @overload
    def Gap(self) -> float: ...

    @overload
    def Gap(self, G: float) -> None: ...

    @overload
    def TgtAng(self) -> float: ...

    @overload
    def TgtAng(self, Ang: float) -> None: ...

    def HasConstraint(self) -> bool: ...

    def Constraint(self) -> None: ...

    @overload
    def NorAng(self) -> float: ...

    @overload
    def NorAng(self, Ang: float) -> None: ...

    def IsToKill(self) -> tuple[bool, float]: ...

    def DoKill(self, Scal: float) -> None: ...

class GeomFill_ConstrainedFilling:
    """
    An algorithm for constructing a BSpline surface filled
    from a series of boundaries which serve as path
    constraints and optionally, as tangency constraints.
    The algorithm accepts three or four curves as the
    boundaries of the target surface.
    The only FillingStyle used is Coons.
    A ConstrainedFilling object provides a framework for:
    -   defining the boundaries of the surface
    -   implementing the construction algorithm
    -   consulting the result.
    Warning
    This surface filling algorithm is specifically designed to
    be used in connection with fillets. Satisfactory results
    cannot be guaranteed for other uses.
    """

    @overload
    def __init__(self, MaxDeg: int, MaxSeg: int) -> None:
        """
        Constructs an empty framework for filling a surface from boundaries.
        The boundaries of the surface will be defined, and the
        surface will be built by using the function Init.
        The surface will respect the following constraints:
        -   its degree will not be greater than MaxDeg
        -   the maximum number of segments MaxSeg which
        BSpline surfaces can have.
        """

    @overload
    def __init__(self, theOther: GeomFill_ConstrainedFilling) -> None: ...

    @overload
    def Init(self, B1: GeomFill_Boundary | None, B2: GeomFill_Boundary | None, B3: GeomFill_Boundary | None, NoCheck: bool = False) -> None: ...

    @overload
    def Init(self, B1: GeomFill_Boundary | None, B2: GeomFill_Boundary | None, B3: GeomFill_Boundary | None, B4: GeomFill_Boundary | None, NoCheck: bool = False) -> None:
        """
        Constructs a BSpline surface filled from the series of
        boundaries B1, B2, B3 and, if need be, B4, which serve:
        -   as path constraints
        -   and optionally, as tangency constraints if they are
        GeomFill_BoundWithSurf curves.
        The boundaries may be given in any order: they are
        classified and if necessary, reversed and reparameterized.
        The surface will also respect the following constraints:
        -   its degree will not be greater than the maximum
        degree defined at the time of construction of this framework, and
        -   the maximum number of segments MaxSeg which BSpline surfaces can have
        """

    def SetDomain(self, l: float, B: GeomFill_BoundWithSurf | None) -> None:
        """
        Allows to modify domain on which the blending function
        associated to the constrained boundary B will propag
        the influence of the field of tangency. Can be
        useful to reduce influence of boundaries on which
        the Coons compatibility conditions are not respected.
        l is a relative value of the parametric range of B.
        Default value for l is 1 (used in Init).
        Warning: Must be called after Init with a constrained boundary
        used in the call to Init.
        """

    def ReBuild(self) -> None:
        """
        Computes the new poles of the surface using the new
        blending functions set by several calls to SetDomain.
        """

    def Boundary(self, I: int) -> GeomFill_Boundary:
        """Returns the bound of index i after sort."""

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Returns the BSpline surface after computation of the fill by this framework.
        """

    def Eval(self, W: float, Ord: int) -> tuple[int, float]:
        """Internal use for Advmath approximation call."""

    def CheckCoonsAlgPatch(self, I: int) -> None:
        """
        Computes the fields of tangents on 30 points along the
        bound I, these are not the constraint tangents but
        gives an idea of the coonsAlgPatch regularity.
        """

    def CheckTgteField(self, I: int) -> None:
        """
        Computes the fields of tangents and normals on 30
        points along the bound I, draw them, and computes the
        max dot product that must be near than 0.
        """

    def CheckApprox(self, I: int) -> None:
        """
        Computes values and normals along the bound I and
        compare them to the approx result curves (bound and
        tgte field) , draw the normals and tangents.
        """

    def CheckResult(self, I: int) -> None:
        """
        Computes values and normals along the bound I on both
        constraint surface and result surface, draw the
        normals, and computes the max distance between values
        and the max angle between normals.
        """

class GeomFill_Filling:
    """Root class for Filling;"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Filling) -> None: ...

    def NbUPoles(self) -> int: ...

    def NbVPoles(self) -> int: ...

    def Poles(self, Poles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]) -> None: ...

    def isRational(self) -> bool: ...

    def Weights(self, Weights: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

class GeomFill_Coons(GeomFill_Filling):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float], W3: nanoocp.NCollection.NCollection_Array1[float], W4: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Coons) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float], W3: nanoocp.NCollection.NCollection_Array1[float], W4: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

class GeomFill_CoonsAlgPatch(nanoocp.Standard.Standard_Transient):
    """
    Provides evaluation methods on an algorithmic
    patch (based on 4 Curves) defined by its boundaries and blending
    functions.
    """

    @overload
    def __init__(self, B1: GeomFill_Boundary | None, B2: GeomFill_Boundary | None, B3: GeomFill_Boundary | None, B4: GeomFill_Boundary | None) -> None:
        """
        Constructs the algorithmic patch. By Default the
        constructed blending functions are linear.
        Warning: No control is done on the bounds.
        B1/B3 and B2/B4 must be same range and well oriented.
        """

    @overload
    def __init__(self, theOther: GeomFill_CoonsAlgPatch) -> None: ...

    @overload
    def Func(self) -> tuple[nanoocp.Law.Law_Function, nanoocp.Law.Law_Function]:
        """Give the blending functions."""

    @overload
    def Func(self, I: int) -> nanoocp.Law.Law_Function: ...

    def SetFunc(self, f1: nanoocp.Law.Law_Function | None, f2: nanoocp.Law.Law_Function | None) -> None:
        """Set the blending functions."""

    def Value(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the value on the algorithmic patch at
        parameters U and V.
        """

    def D1U(self, U: float, V: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the d/dU partial derivative on the
        algorithmic patch at parameters U and V.
        """

    def D1V(self, U: float, V: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the d/dV partial derivative on the
        algorithmic patch at parameters U and V.
        """

    def DUV(self, U: float, V: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the d2/dUdV partial derivative on the
        algorithmic patch made with linear blending functions
        at parameter U and V.
        """

    def Corner(self, I: int) -> nanoocp.gp.gp_Pnt: ...

    def Bound(self, I: int) -> GeomFill_Boundary: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_CorrectedFrenet(GeomFill_TrihedronLaw):
    """
    Defined an Corrected Frenet Trihedron Law It is
    like Frenet with an Torsion's minimization
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, ForEvaluation: bool) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_CorrectedFrenet) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of frenet law
        @return true in case if execution end correctly
        """

    def SetInterval(self, First: float, Last: float) -> None: ...

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """compute Triedrhon on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Triedrhon and derivative Trihedron on curve
        at parameter <Param>
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def EvaluateBestMode(self) -> GeomFill_Trihedron:
        """
        Tries to define the best trihedron mode
        for the curve. It can be:
        - Frenet
        - CorrectedFrenet
        - DiscreteTrihedron
        Warning: the CorrectedFrenet must be constructed
        with option ForEvaluation = True,
        the curve must be set by method SetCurve.
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of Tangent(t) and Normal(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant."""

    def IsOnlyBy3dCurve(self) -> bool:
        """Return True."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_LocationLaw(nanoocp.Standard.Standard_Transient):
    """
    To define location law in Sweeping location is
    defined by an Matrix M and an Vector V, and
    transform an point P in MP+V.
    """

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """initialize curve of location law"""

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def SetTrsf(self, Transfo: nanoocp.gp.gp_Mat) -> None:
        """
        Set a transformation Matrix like the law M(t) become
        Mat * M(t)
        """

    def Copy(self) -> GeomFill_LocationLaw: ...

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec) -> bool:
        """compute Location"""

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> bool:
        """compute Location and 2d points"""

    def D1(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first derivatives.
        Warning: It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, D2M: nanoocp.gp.gp_Mat, D2V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first and second derivatives.
        Warning: It used only for C2 approximation
        """

    def Nb2dCurves(self) -> int:
        """
        get the number of 2d curves (Restrictions + Traces)
        to approximate.
        """

    def HasFirstRestriction(self) -> bool:
        """
        Say if the first restriction is defined in this class.
        If it is true the first element of poles array in
        D0,D1,D2... Correspond to this restriction.
        Returns false (default implementation)
        """

    def HasLastRestriction(self) -> bool:
        """
        Say if the last restriction is defined in this class.
        If it is true the last element of poles array in
        D0,D1,D2... Correspond to this restriction.
        Returns false (default implementation)
        """

    def TraceNumber(self) -> int:
        """
        Give the number of trace (Curves 2d which are not restriction)
        Returns 0 (default implementation)
        """

    def ErrorStatus(self) -> GeomFill_PipeError:
        """
        Give a status to the Law
        Returns PipeOk (default implementation)
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def Resolution(self, Index: int, Tol: float) -> tuple[float, float]:
        """
        Returns the resolutions in the sub-space 2d <Index>
        This information is useful to find a good tolerance in
        2d approximation.
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if (me) have to run numerical
        algorithm to perform D0, D1 or D2
        The default implementation make nothing.
        """

    def GetMaximalNorm(self) -> float:
        """
        Get the maximum Norm of the matrix-location part. It
        is usful to find a good Tolerance to approx M(t).
        """

    def GetAverageLaw(self, AM: nanoocp.gp.gp_Mat, AV: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsTranslation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is an translation of Location
        The default implementation is " returns False ".
        """

    def IsRotation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is a rotation of Location
        The default implementation is " returns False ".
        """

    def Rotation(self, Center: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_CurveAndTrihedron(GeomFill_LocationLaw):
    """
    Define location law with an TrihedronLaw and an
    curve
    Definition Location is:
    transformed section coordinates in (Curve(v)),
    (Normal(v), BiNormal(v), Tangente(v))) systems are
    the same like section shape coordinates in
    (O,(OX, OY, OZ)) system.
    """

    @overload
    def __init__(self, Trihedron: GeomFill_TrihedronLaw | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_CurveAndTrihedron) -> None: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of trihedron law
        @return true in case if execution end correctly
        """

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def SetTrsf(self, Transfo: nanoocp.gp.gp_Mat) -> None:
        """
        Set a transformation Matrix like the law M(t) become
        Mat * M(t)
        """

    def Copy(self) -> GeomFill_LocationLaw: ...

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec) -> bool: ...

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> bool:
        """compute Location and 2d points"""

    def D1(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first derivatives.
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, D2M: nanoocp.gp.gp_Mat, D2V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def GetMaximalNorm(self) -> float:
        """
        Get the maximum Norm of the matrix-location part. It
        is usful to find a good Tolerance to approx M(t).
        """

    def GetAverageLaw(self, AM: nanoocp.gp.gp_Mat, AV: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsTranslation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is an translation of Location
        The default implementation is " returns False ".
        """

    def IsRotation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is a rotation of Location
        The default implementation is " returns False ".
        """

    def Rotation(self, Center: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_Curved(GeomFill_Filling):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float], W3: nanoocp.NCollection.NCollection_Array1[float], W4: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Curved) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float], W3: nanoocp.NCollection.NCollection_Array1[float], W4: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

class GeomFill_Darboux(GeomFill_TrihedronLaw):
    """Defines Darboux case of Frenet Trihedron Law"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Darboux) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """compute Triedrhon on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Triedrhon and derivative Trihedron on curve
        at parameter <Param>
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of Tangent(t) and Normal(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant."""

    def IsOnlyBy3dCurve(self) -> bool:
        """Return False."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_DegeneratedBound(GeomFill_Boundary):
    """
    Description of a degenerated boundary (a point).
    Class defining a degenerated boundary for a
    constrained filling with a point and no other
    constraint. Only used to simulate an ordinary bound,
    may not be useful and desapear soon.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt, First: float, Last: float, Tol3d: float, Tolang: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_DegeneratedBound) -> None: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt: ...

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None: ...

    def Reparametrize(self, First: float, Last: float, HasDF: bool, HasDL: bool, DF: float, DL: float, Rev: bool) -> None: ...

    def Bounds(self) -> tuple[float, float]: ...

    def IsDegenerated(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_DiscreteTrihedron(GeomFill_TrihedronLaw):
    """
    Defined Discrete Trihedron Law.
    The requirement for path curve is only G1.
    The result is C0-continuous surface
    that can be later approximated to C1.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_DiscreteTrihedron) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def Init(self) -> None: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of trihedron law
        @return true in case if execution end correctly
        """

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """compute Trihedron on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron and derivative Trihedron on curve
        at parameter <Param>
        Warning : It used only for C1 or C2 approximation
        For the moment it returns null values for DTangent, DNormal
        and DBiNormal.
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning : It used only for C2 approximation
        For the moment it returns null values for DTangent, DNormal
        DBiNormal, D2Tangent, D2Normal, D2BiNormal.
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of Tangent(t) and Normal(t) it is usful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant."""

    def IsOnlyBy3dCurve(self) -> bool:
        """Return True."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_DraftTrihedron(GeomFill_TrihedronLaw):
    @overload
    def __init__(self, BiNormal: nanoocp.gp.gp_Vec, Angle: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_DraftTrihedron) -> None: ...

    def SetAngle(self, Angle: float) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Triedrhon and derivative Trihedron on curve at
        parameter <Param>
        Warning: It used only for C1 or C2 approximation
        """

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning: It used only for C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of Tangent(t) and Normal(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant."""

    def IsOnlyBy3dCurve(self) -> bool:
        """Return True."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_SectionLaw(nanoocp.Standard.Standard_Transient):
    """To define section law in sweeping"""

    def D0(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        Warning : It used only for C2 approximation
        """

    def BSplineSurface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        give if possible an bspline Surface, like iso-v are the
        section. If it is not possible this method have to
        get an Null Surface. It is the default implementation.
        """

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the sections are rational or not"""

    def IsUPeriodic(self) -> bool:
        """Returns if the sections are periodic or not"""

    def IsVPeriodic(self) -> bool:
        """Returns if law is periodic or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerances associated at each poles to
        reach in approximation, to satisfy: BoundTol error
        at the Boundary AngleTol tangent error at the
        Boundary (in radian) SurfTol error inside the
        surface.
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if <me> has to run numerical
        algorithm to perform D0, D1 or D2
        The default implementation make nothing.
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface.
        A very poor estimation is sufficient.
        This information is useful to perform well
        conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the greater section. This
        information is useful to G1's control.
        Warning: With an little value, approximation can be slower.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        in all sections.
        This information is useful to control error
        in rational approximation.
        Warning: Used only if <me> IsRational
        """

    def IsConstant(self) -> tuple[bool, float]:
        """Say if all sections are equals"""

    def ConstantSection(self) -> nanoocp.Geom.Geom_Curve:
        """
        Return a copy of the constant Section, if <me>
        IsConstant
        """

    def IsConicalLaw(self) -> tuple[bool, float]:
        """
        Returns True if all section are circle, with same
        plane,same center and linear radius evolution
        Return False by Default.
        """

    def CirclSection(self, Param: float) -> nanoocp.Geom.Geom_Curve:
        """
        Return the circle section at parameter <Param>, if
        <me> a IsConicalLaw
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_EvolvedSection(GeomFill_SectionLaw):
    """Define an Constant Section Law"""

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve | None, L: nanoocp.Law.Law_Function | None) -> None:
        """Make an SectionLaw with a Curve and a real Law."""

    @overload
    def __init__(self, theOther: GeomFill_EvolvedSection) -> None: ...

    def D0(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        Warning : It used only for C2 approximation
        """

    def BSplineSurface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        give if possible an bspline Surface, like iso-v are the
        section. If it is not possible this methode have to
        get an Null Surface. Is it the default implementation.
        """

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the sections are rational or not"""

    def IsUPeriodic(self) -> bool:
        """Returns if the sections are periodic or not"""

    def IsVPeriodic(self) -> bool:
        """Returns if the law isperiodic or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerances associated at each poles to
        reach in approximation, to satisfy: BoundTol error
        at the Boundary AngleTol tangent error at the
        Boundary (in radian) SurfTol error inside the
        surface.
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface.
        An very poor estimation is sufficient.
        This information is useful to perform well
        conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the greater section. This
        information is useful to G1's control.
        Warning: With an little value, approximation can be slower.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        in all sections.
        This information is useful to control error
        in rational approximation.
        Warning: Used only if <me> IsRational
        """

    def IsConstant(self) -> tuple[bool, float]:
        """return True If the Law isConstant"""

    def ConstantSection(self) -> nanoocp.Geom.Geom_Curve:
        """Return the constant Section if <me> IsConstant."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_Fixed(GeomFill_TrihedronLaw):
    """Defined an constant TrihedronLaw"""

    @overload
    def __init__(self, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Fixed) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """compute Triedrhon on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Triedrhon and derivative Trihedron on curve
        at parameter <Param>
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of Tangent(t) and Normal(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Return True."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_Frenet(GeomFill_TrihedronLaw):
    """Defined Frenet Trihedron Law"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Frenet) -> None: ...

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def Init(self) -> None: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of frenet law
        @return true
        """

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """compute Triedrhon on curve at parameter <Param>"""

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Triedrhon and derivative Trihedron on curve
        at parameter <Param>
        Warning: It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool:
        """
        compute Trihedron on curve
        first and second derivatives.
        Warning: It used only for C2 approximation
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of Tangent(t) and Normal(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant."""

    def IsOnlyBy3dCurve(self) -> bool:
        """Return True."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_FunctionDraft(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_FunctionDraft) -> None: ...

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

    def DerivT(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Param: float, W: float, dN: nanoocp.gp.gp_Vec, teta: float, F: nanoocp.math.math_Vector) -> bool:
        """
        returns the values <F> of the T derivatives for
        the parameter Param.
        """

    def Deriv2T(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Param: float, W: float, d2N: nanoocp.gp.gp_Vec, teta: float, F: nanoocp.math.math_Vector) -> bool:
        """
        returns the values <F> of the T2 derivatives for
        the parameter Param.
        """

    def DerivTX(self, dN: nanoocp.gp.gp_Vec, teta: float, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the TX derivatives for
        the parameter Param.
        """

    def Deriv2X(self, X: nanoocp.math.math_Vector, T: GeomFill_Tensor) -> bool:
        """
        returns the values <T> of the X2 derivatives for
        the parameter Param.
        """

class GeomFill_FunctionGuide(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self, S: GeomFill_SectionLaw | None, Guide: nanoocp.Adaptor3d.Adaptor3d_Curve | None, ParamOnLaw: float = 0.0) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_FunctionGuide) -> None: ...

    def SetParam(self, Param: float, Centre: nanoocp.gp.gp_Pnt, Dir: nanoocp.gp.gp_XYZ, XDir: nanoocp.gp.gp_XYZ) -> None: ...

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

    def DerivT(self, X: nanoocp.math.math_Vector, DCentre: nanoocp.gp.gp_XYZ, DDir: nanoocp.gp.gp_XYZ, DFDT: nanoocp.math.math_Vector) -> bool:
        """
        returns the values <F> of the T derivatives for
        the parameter Param .
        """

class GeomFill_Profiler:
    """
    Evaluation of the common BSplineProfile of a group
    of curves from Geom. All the curves will have the
    same degree, the same knot-vector, so the same
    number of poles.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Profiler) -> None: ...

    def AddCurve(self, Curve: nanoocp.Geom.Geom_Curve | None) -> None: ...

    def Perform(self, PTol: float) -> None:
        """
        Converts all curves to BSplineCurves.
        Set them to the common profile.
        <PTol> is used to compare 2 knots.
        """

    def Degree(self) -> int:
        """Raises if not yet perform"""

    def IsPeriodic(self) -> bool: ...

    def NbPoles(self) -> int:
        """Raises if not yet perform"""

    def Poles(self, Index: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        returns in <Poles> the poles of the BSplineCurve
        from index <Index> adjusting to the current profile.
        Raises if not yet perform
        Raises if <Index> not in the range [1,NbCurves]
        if the length of <Poles> is not equal to
        NbPoles().
        """

    def Weights(self, Index: int, Weights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        returns in <Weights> the weights of the BSplineCurve
        from index <Index> adjusting to the current profile.
        Raises if not yet perform
        Raises if <Index> not in the range [1,NbCurves] or
        if the length of <Weights> is not equal to
        NbPoles().
        """

    def NbKnots(self) -> int:
        """Raises if not yet perform"""

    def KnotsAndMults(self, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Raises if not yet perform
        Raises if the lengths of <Knots> and <Mults> are
        not equal to NbKnots().
        """

    def Curve(self, Index: int) -> nanoocp.Geom.Geom_Curve: ...

class GeomFill_Generator(GeomFill_Profiler):
    """
    Create a surface using generating lines. Inherits
    profiler. The surface will be a BSplineSurface
    passing by all the curves described in the
    generator. The VDegree of the resulting surface is
    1.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Generator) -> None: ...

    def Perform(self, PTol: float) -> None:
        """
        Converts all curves to BSplineCurves.
        Set them to the common profile.
        Compute the surface (degv = 1).
        <PTol> is used to compare 2 knots.
        """

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

class GeomFill_Gordon:
    """
    High-level Gordon surface construction from arbitrary curve networks.

    A Gordon surface (transfinite interpolation) constructs a smooth B-spline
    surface from a network of intersecting profile (V) and guide (U) curves.

    This generalizes the existing GeomFill_Coons (4-boundary patch) to N x M
    curve networks.

    This class accepts arbitrary Geom_Curve inputs, handles conversion to BSpline,
    expands periodic B-splines into explicit non-periodic form, finds intersections,
    sorts the network, reparametrizes curves for compatibility, then evaluates a
    transfinite interpolation surface over the compatible network.

    Usage:
    @code
    GeomFill_Gordon aGordon;
    aGordon.Init(theProfiles, theGuides, theTolerance);
    aGordon.Perform();
    if (aGordon.IsDone())
    {
    const occ::handle<Geom_BSplineSurface>& aSurf = aGordon.Surface();
    }
    @endcode

    Limitations:
    - Every profile must intersect every guide. Multiple contacts are accepted
    only when they contain a single monotone branch over the ordered network.
    - Rational networks are combined by exact common-denominator multiplication.
    Construction can fail if the resulting product degree exceeds OCCT's
    B-spline degree limit.
    - ApproximationMode::AllowApproximateFallback may build a sampled surface
    when exact construction fails, or rebuild rational curves approximately
    when exact reparametrization is required. Such a surface is marked by
    IsApproximate() and does not guarantee exact interpolation of the input curves.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty Gordon surface algorithm."""

    @overload
    def __init__(self, theOther: GeomFill_Gordon) -> None: ...

    class ResultStatus(enum.Enum):
        """Result state of the last Perform() call."""

        NotStarted = 0

        Done = 1

        InvalidInput = 2

        ConversionFailed = 3

        IntersectionFailed = 4

        OrderingFailed = 5

        ReparametrizationFailed = 6

        CompatibilityFailed = 7

        CurveCompatibilityFailed = 8

        RationalReparametrizationFailed = 9

        SkinningFailed = 10

        ReferenceSurfaceFailed = 11

        KnotAlignmentFailed = 12

        RationalDegreeOverflow = 13

        RationalConstructionFailed = 14

        PeriodicityFailed = 15

        ApproximationFailed = 16

        ConstructionFailed = 17

    class ApproximationMode(enum.Enum):
        """Controls behavior when exact pole-based construction fails."""

        ExactOnly = 0

        AllowApproximateFallback = 1

    class BuildStage(enum.Enum):
        """Construction stage reached by the last Perform() call."""

        NotStarted = 0

        InputConversion = 1

        ContactDiscovery = 2

        NetworkOrdering = 3

        Reparametrization = 4

        ExactConstruction = 5

        Validation = 6

        Approximation = 7

    class BuildReport:
        """Diagnostics for the last Perform() call."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomFill_Gordon.BuildReport) -> None: ...

        @property
        def Status(self) -> GeomFill_Gordon.ResultStatus: ...

        @Status.setter
        def Status(self, arg: GeomFill_Gordon.ResultStatus, /) -> None: ...

        @property
        def FailedStage(self) -> GeomFill_Gordon.BuildStage: ...

        @FailedStage.setter
        def FailedStage(self, arg: GeomFill_Gordon.BuildStage, /) -> None: ...

        @property
        def IsApproximate(self) -> bool: ...

        @IsApproximate.setter
        def IsApproximate(self, arg: bool, /) -> None: ...

        @property
        def MaxContactGap(self) -> float: ...

        @MaxContactGap.setter
        def MaxContactGap(self, arg: float, /) -> None: ...

        @property
        def MaxReparametrizationDeviation(self) -> float: ...

        @MaxReparametrizationDeviation.setter
        def MaxReparametrizationDeviation(self, arg: float, /) -> None: ...

        @property
        def MaxProfileDeviation(self) -> float: ...

        @MaxProfileDeviation.setter
        def MaxProfileDeviation(self, arg: float, /) -> None: ...

        @property
        def MaxGuideDeviation(self) -> float: ...

        @MaxGuideDeviation.setter
        def MaxGuideDeviation(self, arg: float, /) -> None: ...

        @property
        def MaxApproximationDeviation(self) -> float: ...

        @MaxApproximationDeviation.setter
        def MaxApproximationDeviation(self, arg: float, /) -> None: ...

    def Init(self, theProfiles: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve], theGuides: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve], theTolerance: float) -> None:
        """
        Initializes the algorithm with profile and guide curves.
        @param[in] theProfiles  array of profile curves (V-direction sections, must be >= 2)
        @param[in] theGuides    array of guide curves (U-direction sections, must be >= 2)
        @param[in] theTolerance geometric tolerance for intersection detection
        """

    def Perform(self) -> None:
        """Performs the Gordon surface construction."""

    def SetParallelMode(self, theToUseParallel: bool) -> None:
        """
        Enables/disables parallel processing in internal stages.
        By default, single-thread mode is used.
        """

    def SetApproximationMode(self, theMode: GeomFill_Gordon.ApproximationMode) -> None:
        """
        Sets optional fallback behavior for failures in exact B-spline construction.
        Approximate fallback results should be checked by IsApproximate().
        """

    def GetApproximationMode(self) -> GeomFill_Gordon.ApproximationMode:
        """Returns current fallback behavior."""

    def IsParallelMode(self) -> bool:
        """Returns true if internal parallel processing is enabled."""

    def IsDone(self) -> bool:
        """Returns true if the surface was successfully constructed."""

    def IsApproximate(self) -> bool:
        """
        Returns true if the resulting surface was produced by approximate fallback.
        Approximate results do not have the exact Gordon interpolation guarantee.
        """

    def Status(self) -> GeomFill_Gordon.ResultStatus:
        """Returns the result state of the last Perform() call."""

    def Report(self) -> GeomFill_Gordon.BuildReport:
        """Returns diagnostics for the last Perform() call."""

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """Returns the resulting Gordon B-spline surface."""

class GeomFill_NetworkSurface:
    """
    Low-level Gordon surface construction from a compatible B-spline curve network.

    This class builds the final surface for an already prepared Gordon network:
    input curves must be explicit non-periodic B-spline curves, consistently
    ordered, and consistently reparametrized. Curve families are made compatible
    by the builder before skinning when they are polynomial.

    Profile skin, guide skin, and an intersection-grid reference surface are
    built in B-spline form and aligned to a common knot basis. The final surface
    is obtained by moving the profile-skin poles by the guide-skin deviation
    measured from this reference surface. No point-grid surface approximation is
    performed here.

    This class does not find curve intersections, sort the network, convert
    arbitrary curves, or reparametrize the input. These operations are handled
    by GeomFill_Gordon before calling this builder.

    Limitations:
    - Periodic input curves are not accepted; callers should expand a required
    period before initialization.
    - Rational construction uses exact common-denominator multiplication and
    can fail if the resulting product degree exceeds OCCT's B-spline degree
    limit.
    - At least two profiles and two guides are required
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty network surface algorithm."""

    @overload
    def __init__(self, theOther: GeomFill_NetworkSurface) -> None: ...

    class ResultStatus(enum.Enum):
        """Result state of the last Perform() call."""

        NotStarted = 0

        Done = 1

        InvalidInput = 2

        CurveCompatibilityFailed = 3

        SkinningFailed = 4

        ReferenceSurfaceFailed = 5

        KnotAlignmentFailed = 6

        RationalDegreeOverflow = 7

        RationalConstructionFailed = 8

        ConstructionFailed = 9

        PeriodicityFailed = 10

    def Init(self, theProfiles: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve], theGuides: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve], theProfileParameters: nanoocp.NCollection.NCollection_Array1[float], theGuideParameters: nanoocp.NCollection.NCollection_Array1[float], theIntersectionPoints: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theIntersectionWeights: nanoocp.NCollection.NCollection_Array2[float], theTolerance: float, theIsUClosed: bool, theIsVClosed: bool) -> None:
        """
        Initializes the algorithm with a compatible profile/guide B-spline network.
        @param[in] theProfiles          profile curves evaluated in U direction
        @param[in] theGuides            guide curves evaluated in V direction
        @param[in] theProfileParameters V parameters locating profiles on guide skin
        @param[in] theGuideParameters   U parameters locating guides on profile skin
        @param[in] theIntersectionPoints validated profile/guide contact grid
        @param[in] theIntersectionWeights rational weights for the contact grid
        @param[in] theTolerance         geometric tolerance for closed-seam checks
        @param[in] theIsUClosed         indicates that first/last guide curves close the U seam
        @param[in] theIsVClosed         indicates that first/last profile curves close the V seam
        """

    def Perform(self) -> None:
        """Performs the pole-based network surface construction."""

    def IsDone(self) -> bool:
        """Returns true if the surface was successfully constructed."""

    def Status(self) -> GeomFill_NetworkSurface.ResultStatus:
        """Returns the result state of the last Perform() call."""

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Returns the constructed B-spline surface.
        @throws StdFail_NotDone if Perform() has not completed successfully.
        """

class GeomFill_TrihedronWithGuide(GeomFill_TrihedronLaw):
    """To define Trihedron along one Curve with a guide"""

    def Guide(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def Origine(self, Param1: float, Param2: float) -> None: ...

    def CurrentPointOnGuide(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the current point on guide
        found by D0, D1 or D2.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_GuideTrihedronAC(GeomFill_TrihedronWithGuide):
    """
    Trihedron in the case of a sweeping along a guide curve.
    defined by curviline absciss
    """

    @overload
    def __init__(self, guide: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_GuideTrihedronAC) -> None: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of trihedron law
        @return true
        """

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def Guide(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant"""

    def IsOnlyBy3dCurve(self) -> bool:
        """
        Say if the law is defined, only by the 3d Geometry of
        the set Curve
        Return False by Default.
        """

    def Origine(self, OrACR1: float, OrACR2: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_GuideTrihedronPlan(GeomFill_TrihedronWithGuide):
    """
    Trihedron in the case of sweeping along a guide curve defined
    by the orthogonal plan on the trajectory
    """

    @overload
    def __init__(self, theGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_GuideTrihedronPlan) -> None: ...

    def SetCurve(self, thePath: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        initialize curve of trihedron law
        @return true in case if execution end correctly
        """

    def Copy(self) -> GeomFill_TrihedronLaw: ...

    def ErrorStatus(self) -> GeomFill_PipeError:
        """
        Give a status to the Law
        Returns PipeOk (default implementation)
        """

    def Guide(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def D0(self, Param: float, Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def D1(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def D2(self, Param: float, Tangent: nanoocp.gp.gp_Vec, DTangent: nanoocp.gp.gp_Vec, D2Tangent: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Vec, DNormal: nanoocp.gp.gp_Vec, D2Normal: nanoocp.gp.gp_Vec, BiNormal: nanoocp.gp.gp_Vec, DBiNormal: nanoocp.gp.gp_Vec, D2BiNormal: nanoocp.gp.gp_Vec) -> bool: ...

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetAverageLaw(self, ATangent: nanoocp.gp.gp_Vec, ANormal: nanoocp.gp.gp_Vec, ABiNormal: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsConstant(self) -> bool:
        """Say if the law is Constant"""

    def IsOnlyBy3dCurve(self) -> bool:
        """
        Say if the law is defined, only by the 3d Geometry of
        the set Curve
        Return False by Default.
        """

    def Origine(self, OrACR1: float, OrACR2: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_Line(nanoocp.Standard.Standard_Transient):
    """class for instantiation of AppBlend"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, NbPoints: int) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Line) -> None: ...

    def NbPoints(self) -> int: ...

    def Point(self, Index: int) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_LocationDraft(GeomFill_LocationLaw):
    @overload
    def __init__(self, Direction: nanoocp.gp.gp_Dir, Angle: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_LocationDraft) -> None: ...

    def SetStopSurf(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    def SetAngle(self, Angle: float) -> None: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        calculation of poles on locking surfaces (the intersection between the generatrixand the
        surface at the cross - section points myNbPts)
        @return true in case if execution end correctly
        """

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def SetTrsf(self, Transfo: nanoocp.gp.gp_Mat) -> None: ...

    def Copy(self) -> GeomFill_LocationLaw: ...

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec) -> bool:
        """compute Location"""

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> bool:
        """compute Location and 2d points"""

    def D1(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first derivatives.
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, D2M: nanoocp.gp.gp_Mat, D2V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def HasFirstRestriction(self) -> bool:
        """
        Say if the first restriction is defined in this class.
        If it is true the first element of poles array in
        D0,D1,D2... Correspond to this restriction.
        Returns false (default implementation)
        """

    def HasLastRestriction(self) -> bool:
        """
        Say if the last restriction is defined in this class.
        If it is true the last element of poles array in
        D0,D1,D2... Correspond to this restriction.
        Returns false (default implementation)
        """

    def TraceNumber(self) -> int:
        """
        Give the number of trace (Curves 2d which are not restriction)
        Returns 1 (default implementation)
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returnsthe number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def Resolution(self, Index: int, Tol: float) -> tuple[float, float]:
        """
        Returns the resolutions in the sub-space 2d <Index>
        This information is useful to find a good tolerance in
        2d approximation.
        Warning: Used only if Nb2dCurve > 0
        """

    def GetMaximalNorm(self) -> float:
        """
        Get the maximum Norm of the matrix-location part. It
        is usful to find a good Tolerance to approx M(t).
        """

    def GetAverageLaw(self, AM: nanoocp.gp.gp_Mat, AV: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsTranslation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is an translation of Location
        The default implementation is " returns False ".
        """

    def IsRotation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is a rotation of Location
        The default implementation is " returns False ".
        """

    def Rotation(self, Center: nanoocp.gp.gp_Pnt) -> None: ...

    def IsIntersec(self) -> bool:
        """Say if the generatrice interset the surface"""

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_LocationGuide(GeomFill_LocationLaw):
    @overload
    def __init__(self, Triedre: GeomFill_TrihedronWithGuide | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_LocationGuide) -> None: ...

    def Set(self, Section: GeomFill_SectionLaw | None, rotat: bool, SFirst: float, SLast: float, PrecAngle: float) -> float: ...

    def EraseRotation(self) -> None: ...

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool:
        """
        calculating poles on a surface (courbe guide / the surface of rotation in points myNbPts)
        @return true
        """

    def GetCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def SetTrsf(self, Transfo: nanoocp.gp.gp_Mat) -> None: ...

    def Copy(self) -> GeomFill_LocationLaw: ...

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec) -> bool:
        """compute Location"""

    @overload
    def D0(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> bool:
        """compute Location and 2d points"""

    def D1(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first derivatives.
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, M: nanoocp.gp.gp_Mat, V: nanoocp.gp.gp_Vec, DM: nanoocp.gp.gp_Mat, DV: nanoocp.gp.gp_Vec, D2M: nanoocp.gp.gp_Mat, D2V: nanoocp.gp.gp_Vec, Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        compute location 2d points and associated
        first and second derivatives.
        Warning : It used only for C2 approximation
        """

    def HasFirstRestriction(self) -> bool:
        """
        Say if the first restriction is defined in this class.
        If it is true the first element of poles array in
        D0,D1,D2... Correspond to this restriction.
        Returns false (default implementation)
        """

    def HasLastRestriction(self) -> bool:
        """
        Say if the last restriction is defined in this class.
        If it is true the last element of poles array in
        D0,D1,D2... Correspond to this restriction.
        Returns false (default implementation)
        """

    def TraceNumber(self) -> int:
        """
        Give the number of trace (Curves 2d which are not restriction)
        Returns 1 (default implementation)
        """

    def ErrorStatus(self) -> GeomFill_PipeError:
        """
        Give a status to the Law
        Returns PipeOk (default implementation)
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if (me) have to run numerical
        algorithm to perform D0, D1 or D2
        The default implementation make nothing.
        """

    def Resolution(self, Index: int, Tol: float) -> tuple[float, float]:
        """
        Returns the resolutions in the sub-space 2d <Index>
        This information is useful to find a good tolerance in
        2d approximation.
        Warning: Used only if Nb2dCurve > 0
        """

    def GetMaximalNorm(self) -> float:
        """
        Get the maximum Norm of the matrix-location part. It
        is usful to find a good Tolerance to approx M(t).
        """

    def GetAverageLaw(self, AM: nanoocp.gp.gp_Mat, AV: nanoocp.gp.gp_Vec) -> None:
        """
        Get average value of M(t) and V(t) it is useful to
        make fast approximation of rational surfaces.
        """

    def IsTranslation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is an translation of Location
        The default implementation is " returns False ".
        """

    def IsRotation(self) -> tuple[bool, float]:
        """
        Say if the Location Law, is a rotation of Location
        The default implementation is " returns False ".
        """

    def Rotation(self, Center: nanoocp.gp.gp_Pnt) -> None: ...

    def Section(self) -> nanoocp.Geom.Geom_Curve: ...

    def Guide(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def SetOrigine(self, Param1: float, Param2: float) -> None: ...

    def ComputeAutomaticLaw(self) -> tuple[GeomFill_PipeError, nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d]]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_LocFunction:
    @overload
    def __init__(self, Law: GeomFill_LocationLaw | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_LocFunction) -> None: ...

    def D0(self, Param: float, First: float, Last: float) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, First: float, Last: float) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        """

    def D2(self, Param: float, First: float, Last: float) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        """

    def DN(self, Param: float, First: float, Last: float, Order: int) -> tuple[float, int]: ...

class GeomFill_NSections(GeomFill_SectionLaw):
    """Define a Section Law by N Sections"""

    @overload
    def __init__(self, NC: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None:
        """Make a SectionLaw with N Curves."""

    @overload
    def __init__(self, NC: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve], NP: nanoocp.NCollection.NCollection_Sequence[float]) -> None:
        """Make a SectionLaw with N Curves and N associated parameters."""

    @overload
    def __init__(self, NC: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve], NP: nanoocp.NCollection.NCollection_Sequence[float], UF: float, UL: float) -> None:
        """
        Make a SectionLaw with N Curves and N associated parameters.
        UF and UL are the parametric bounds of the NSections
        """

    @overload
    def __init__(self, NC: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve], NP: nanoocp.NCollection.NCollection_Sequence[float], UF: float, UL: float, VF: float, VL: float) -> None:
        """
        Make a SectionLaw with N Curves and N associated parameters.
        UF and UL are the parametric bounds of the NSections
        VF and VL are the parametric bounds of the path
        """

    @overload
    def __init__(self, NC: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve], Trsfs: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Trsf], NP: nanoocp.NCollection.NCollection_Sequence[float], UF: float, UL: float, VF: float, VL: float, Surf: nanoocp.Geom.Geom_BSplineSurface | None) -> None:
        """
        Make a SectionLaw with N Curves and N associated parameters.
        UF and UL are the parametric bounds of the NSections
        VF and VL are the parametric bounds of the path
        UF and UL are the parametric bounds of the NSections
        Surf is a reference surface used by BRepFill_NSections
        """

    @overload
    def __init__(self, theOther: GeomFill_NSections) -> None: ...

    def D0(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        Warning : It used only for C2 approximation
        """

    def SetSurface(self, RefSurf: nanoocp.Geom.Geom_BSplineSurface | None) -> None:
        """Sets the reference surface"""

    def ComputeSurface(self) -> None:
        """Computes the surface"""

    def BSplineSurface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        give if possible an bspline Surface, like iso-v are the
        section. If it is not possible this methode have to
        get an Null Surface. Is it the default implementation.
        """

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the sections are rational or not"""

    def IsUPeriodic(self) -> bool:
        """Returns if the sections are periodic or not"""

    def IsVPeriodic(self) -> bool:
        """Returns if the law isperiodic or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerances associated at each poles to
        reach in approximation, to satisfy: BoundTol error
        at the Boundary AngleTol tangent error at the
        Boundary (in radian) SurfTol error inside the
        surface.
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface.
        An very poor estimation is sufficient.
        This information is useful to perform well
        conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the greater section. This
        information is useful to G1's control.
        Warning: With an little value, approximation can be slower.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        in all sections.
        This information is useful to control error
        in rational approximation.
        Warning: Used only if <me> IsRational
        """

    def IsConstant(self) -> tuple[bool, float]:
        """return True If the Law isConstant"""

    def ConstantSection(self) -> nanoocp.Geom.Geom_Curve:
        """Return the constant Section if <me> IsConstant."""

    def IsConicalLaw(self) -> tuple[bool, float]:
        """
        Returns True if all section are circle, with same
        plane,same center and linear radius evolution
        Return False by Default.
        """

    def CirclSection(self, Param: float) -> nanoocp.Geom.Geom_Curve:
        """
        Return the circle section at parameter <Param>, if
        <me> a IsConicalLaw
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_Pipe:
    """
    Describes functions to construct pipes. A pipe is built by
    sweeping a curve (the section) along another curve (the path).
    The Pipe class provides the following types of construction:
    -   pipes with a circular section of constant radius,
    -   pipes with a constant section,
    -   pipes with a section evolving between two given curves.
    All standard specific cases are detected in order to build,
    where required, a plane, cylinder, cone, sphere, torus,
    surface of linear extrusion or surface of revolution.
    Generally speaking, the result is a BSpline surface (NURBS).
    A Pipe object provides a framework for:
    -   defining the pipe to be built,
    -   implementing the construction algorithm, and
    -   consulting the resulting surface.
    There are several methods to instantiate a Pipe:
    1) give a path and a radius: the section is
    a circle. This location is the first point
    of the path, and this direction is the first
    derivate (calculate at the first point ) of
    the path.

    2) give a path and a section.
    Differtent options are available
    2.a) Use the classical Frenet trihedron
    - or the CorrectedFrenet trihedron
    (To avoid twisted surface)
    - or a constant trihedron to have all the sections
    in a same plane
    2.b) Define a ConstantBinormal Direction to keep the
    same angle between the Direction and the sections
    along the sweep surface.
    2.c) Define the path by a surface and a 2dcurve,
    the surface is used to define the trihedron's normal.
    It is useful to keep a constant angle between
    input surface and the pipe.
    3) give a path and two sections. The section
    evaluate from First to Last Section.

    3) give a path and N sections. The section
    evaluate from First to Last Section.

    In general case the result is a NURBS. But we
    can generate plane, cylindrical, spherical,
    conical, toroidal surface in some particular case.

    The natural parametrization of the result is:

    U-Direction along the section.
    V-Direction along the path.

    But, in some particular case, the surface must
    be construct otherwise.
    The method "EchangeUV" return false in such cases.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm for building pipes. Use
        the function Init to initialize it.
        """

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, Radius: float) -> None: ...

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, Option: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsCorrectedFrenet) -> None:
        """
        Create a pipe with a constant section
        (<FirstSection>) and a path (<Path>)
        Option can be - GeomFill_IsCorrectedFrenet
        - GeomFill_IsFrenet
        - GeomFill_IsConstant
        """

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, NSections: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None:
        """
        Create a pipe with N sections
        The section evaluate from First to Last Section
        """

    @overload
    def __init__(self, Path: nanoocp.Geom2d.Geom2d_Curve | None, Support: nanoocp.Geom.Geom_Surface | None, FirstSect: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Create a pipe with a constant section
        (<FirstSection>) and a path defined by <Path> and <Support>
        """

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, Dir: nanoocp.gp.gp_Dir) -> None:
        """
        Create a pipe with a constant section
        (<FirstSection>) and a path <Path> and a fixed
        binormal direction <Dir>
        """

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, LastSect: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Create a pipe with an evolving section
        The section evaluate from First to Last Section
        """

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, Curve1: nanoocp.Geom.Geom_Curve | None, Curve2: nanoocp.Geom.Geom_Curve | None, Radius: float) -> None: ...

    @overload
    def __init__(self, Path: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve1: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve2: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Radius: float) -> None:
        """
        Create a pipe with a constant radius with 2
        guide-line.
        """

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, Guide: nanoocp.Adaptor3d.Adaptor3d_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, ByACR: bool, rotat: bool) -> None:
        """
        Create a pipe with a constant section and with 1
        guide-line.
        Use the function Perform to build the surface.
        All standard specific cases are detected in order to
        construct, according to the respective geometric
        nature of Path and the sections, a planar, cylindrical,
        conical, spherical or toroidal surface, a surface of
        linear extrusion or a surface of revolution.
        In the general case, the result is a BSpline surface
        (NURBS) built by approximation of a series of sections where:
        -   the number of sections N is chosen automatically
        by the algorithm according to the respective
        geometries of Path and the sections. N is greater than or equal to 2;
        -   N points Pi (with i in the range [ 1,N ]) are
        defined at regular intervals along the curve Path
        from its first point to its end point. At each point Pi,
        a coordinate system Ti is computed with Pi as
        origin, and with the tangential and normal vectors
        to Path defining two of its coordinate axes.
        In the case of a pipe with a constant circular section,
        the first section is a circle of radius Radius centered
        on the origin of Path and whose "Z Axis" is aligned
        along the vector tangential to the origin of Path. In the
        case of a pipe with a constant section, the first section
        is the curve FirstSect. In these two cases, the ith
        section (for values of i greater than 1) is obtained by
        applying to a copy of this first section the geometric
        transformation which transforms coordinate system
        T1 into coordinate system Ti.
        In the case of an evolving section, N-2 intermediate
        curves Si are first computed (if N is greater than 2,
        and with i in the range [ 2,N-1 ]) whose geometry
        evolves regularly from the curve S1=FirstSect to the
        curve SN=LastSect. The first section is FirstSect,
        and the ith section (for values of i greater than 1) is
        obtained by applying to the curve Si the geometric
        transformation which transforms coordinate system
        T1 into coordinate system Ti.
        """

    @overload
    def __init__(self, theOther: GeomFill_Pipe) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, Radius: float) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, Option: GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsCorrectedFrenet) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom2d.Geom2d_Curve | None, Support: nanoocp.Geom.Geom_Surface | None, FirstSect: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, Dir: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, LastSect: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, NSections: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve1: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve2: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Radius: float) -> None:
        """
        Create a pipe with a constant radius with 2
        guide-line.
        """

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, Guide: nanoocp.Adaptor3d.Adaptor3d_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, ByACR: bool, rotat: bool) -> None:
        """
        Initializes this pipe algorithm to build the following surface:
        -   a pipe with a constant circular section of radius
        Radius along the path Path, or
        -   a pipe with constant section FirstSect along the path Path, or
        -   a pipe where the section evolves from FirstSect to
        LastSect along the path Path.
        Use the function Perform to build the surface.
        Note: a description of the resulting surface is given under Constructors.
        """

    @overload
    def Perform(self, WithParameters: bool = False, myPolynomial: bool = False) -> None:
        """
        Builds the pipe defined at the time of initialization of this
        algorithm. A description of the resulting surface is given under Constructors.
        If WithParameters (defaulted to false) is set to true, the
        approximation algorithm (used only in the general case
        of construction of a BSpline surface) builds the surface
        with a u parameter corresponding to the one of the path.
        Exceptions
        Standard_ConstructionError if a surface cannot be constructed from the data.
        Warning: It is the old Perform method, the next methode is recommended.
        """

    @overload
    def Perform(self, Tol: float, Polynomial: bool, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1, MaxDegree: int = 11, NbMaxSegment: int = 30) -> None:
        """
        Detects the particular cases, and computes the surface.
        if none particular case is detected we make an approximation
        with respect of the Tolerance <Tol>, the continuty <Conti>, the
        maximum degree <MaxDegree>, the maximum number of span <NbMaxSegment>
        and the spine parametrization.
        If we can't create a surface with the data
        """

    def Surface(self) -> nanoocp.Geom.Geom_Surface:
        """
        Returns the surface built by this algorithm.
        Warning:
        Do not use this function before the surface is built (in this
        case the function will return a null handle).
        """

    def ExchangeUV(self) -> bool:
        """
        The u parametric direction of the surface constructed by
        this algorithm usually corresponds to the evolution
        along the path and the v parametric direction
        corresponds to the evolution along the section(s).
        However, this rule is not respected when constructing
        certain specific Geom surfaces (typically cylindrical
        surfaces, surfaces of revolution, etc.) for which the
        parameterization is inversed.
        The ExchangeUV function checks for this, and returns
        true in all these specific cases.
        Warning:
        Do not use this function before the surface is built.
        """

    @overload
    def GenerateParticularCase(self, B: bool) -> None:
        """
        Sets a flag to try to create as many planes,
        cylinder,... as possible. Default value is
        <false>.
        """

    @overload
    def GenerateParticularCase(self) -> bool:
        """Returns the flag."""

    def ErrorOnSurf(self) -> float:
        """
        Returns the approximation's error. if the Surface
        is plane, cylinder ... this error can be 0.
        """

    def IsDone(self) -> bool:
        """Returns whether approximation was done."""

    def GetStatus(self) -> GeomFill_PipeError:
        """Returns execution status"""

class GeomFill_PlanFunc(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_PlanFunc) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """
        computes the value <F>of the function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        computes the derivative <D> of the function
        for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        computes the value <F> and the derivative <D> of the
        function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def D2(self, X: float) -> tuple[float, float, float]: ...

    def DEDT(self, X: float, DP: nanoocp.gp.gp_Vec, DV: nanoocp.gp.gp_Vec) -> float: ...

    def D2E(self, X: float, DP: nanoocp.gp.gp_Vec, D2P: nanoocp.gp.gp_Vec, DV: nanoocp.gp.gp_Vec, D2V: nanoocp.gp.gp_Vec) -> tuple[float, float, float]: ...

class GeomFill_PolynomialConvertor:
    """To convert circular section in polynome"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_PolynomialConvertor) -> None: ...

    def Initialized(self) -> bool:
        """say if <me> is Initialized"""

    def Init(self) -> None: ...

    @overload
    def Section(self, FirstPnt: nanoocp.gp.gp_Pnt, Center: nanoocp.gp.gp_Pnt, Dir: nanoocp.gp.gp_Vec, Angle: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def Section(self, FirstPnt: nanoocp.gp.gp_Pnt, DFirstPnt: nanoocp.gp.gp_Vec, Center: nanoocp.gp.gp_Pnt, DCenter: nanoocp.gp.gp_Vec, Dir: nanoocp.gp.gp_Vec, DDir: nanoocp.gp.gp_Vec, Angle: float, DAngle: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> None: ...

    @overload
    def Section(self, FirstPnt: nanoocp.gp.gp_Pnt, DFirstPnt: nanoocp.gp.gp_Vec, D2FirstPnt: nanoocp.gp.gp_Vec, Center: nanoocp.gp.gp_Pnt, DCenter: nanoocp.gp.gp_Vec, D2Center: nanoocp.gp.gp_Vec, Dir: nanoocp.gp.gp_Vec, DDir: nanoocp.gp.gp_Vec, D2Dir: nanoocp.gp.gp_Vec, Angle: float, DAngle: float, D2Angle: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> None: ...

class GeomFill_QuasiAngularConvertor:
    """
    To convert circular section in QuasiAngular Bezier
    form
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_QuasiAngularConvertor) -> None: ...

    def Initialized(self) -> bool:
        """say if <me> is Initialized"""

    def Init(self) -> None: ...

    @overload
    def Section(self, FirstPnt: nanoocp.gp.gp_Pnt, Center: nanoocp.gp.gp_Pnt, Dir: nanoocp.gp.gp_Vec, Angle: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, FirstPnt: nanoocp.gp.gp_Pnt, DFirstPnt: nanoocp.gp.gp_Vec, Center: nanoocp.gp.gp_Pnt, DCenter: nanoocp.gp.gp_Vec, Dir: nanoocp.gp.gp_Vec, DDir: nanoocp.gp.gp_Vec, Angle: float, DAngle: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weights: nanoocp.NCollection.NCollection_Array1[float], DWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, FirstPnt: nanoocp.gp.gp_Pnt, DFirstPnt: nanoocp.gp.gp_Vec, D2FirstPnt: nanoocp.gp.gp_Vec, Center: nanoocp.gp.gp_Pnt, DCenter: nanoocp.gp.gp_Vec, D2Center: nanoocp.gp.gp_Vec, Dir: nanoocp.gp.gp_Vec, DDir: nanoocp.gp.gp_Vec, D2Dir: nanoocp.gp.gp_Vec, Angle: float, DAngle: float, D2Angle: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weights: nanoocp.NCollection.NCollection_Array1[float], DWeights: nanoocp.NCollection.NCollection_Array1[float], D2Weights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

class GeomFill_SectionGenerator(GeomFill_Profiler):
    """
    gives the functions needed for instantiation from
    AppSurf in AppBlend. Allow to evaluate a surface
    passing by all the curves if the Profiler.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_SectionGenerator) -> None: ...

    def SetParam(self, Params: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    def Section(self, P: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Parameter(self, P: int) -> float:
        """
        Returns the parameter of Section<P>, to impose it for the
        approximation.
        """

class GeomFill_SectionPlacement:
    """To place section in sweep Function"""

    @overload
    def __init__(self, L: GeomFill_LocationLaw | None, Section: nanoocp.Geom.Geom_Geometry | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_SectionPlacement) -> None: ...

    def SetLocation(self, L: GeomFill_LocationLaw | None) -> None:
        """To change the section Law"""

    @overload
    def Perform(self, Tol: float) -> None: ...

    @overload
    def Perform(self, Path: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tol: float) -> None: ...

    @overload
    def Perform(self, ParamOnPath: float, Tol: float) -> None: ...

    def IsDone(self) -> bool: ...

    def ParameterOnPath(self) -> float: ...

    def ParameterOnSection(self) -> float: ...

    def Distance(self) -> float: ...

    def Angle(self) -> float: ...

    def Transformation(self, WithTranslation: bool, WithCorrection: bool = False) -> nanoocp.gp.gp_Trsf: ...

    def Section(self, WithTranslation: bool) -> nanoocp.Geom.Geom_Curve:
        """
        Compute the Section, in the coordinate system given by
        the Location Law.
        If <WithTranslation> contact between
        <Section> and <Path> is forced.
        """

    def ModifiedSection(self, WithTranslation: bool) -> nanoocp.Geom.Geom_Curve:
        """
        Compute the Section, in the coordinate system given by
        the Location Law.
        To have the Normal to section equal to the Location
        Law Normal. If <WithTranslation> contact between
        <Section> and <Path> is forced.
        """

class GeomFill_SimpleBound(GeomFill_Boundary):
    """
    Defines a 3d curve as a boundary for a
    GeomFill_ConstrainedFilling algorithm.
    This curve is unattached to an existing surface.D
    Contains fields to allow a reparametrization of curve.
    """

    @overload
    def __init__(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tol3d: float, Tolang: float) -> None:
        """
        Constructs the boundary object defined by the 3d curve.
        The surface to be built along this boundary will be in the
        tolerance range defined by Tol3d.
        This object is to be used as a boundary for a
        GeomFill_ConstrainedFilling framework.
        Dummy is initialized but has no function in this class.
        Warning
        Curve is an adapted curve, that is, an object which is an interface between:
        -   the services provided by a 3D curve from the package Geom
        -   and those required of the curve by the computation
        algorithm which uses it.
        The adapted curve is created in one of the following ways:
        -   First sequence:
        occ::handle<Geom_Curve> myCurve = ... ;
        occ::handle<GeomAdaptor_Curve>
        Curve = new
        GeomAdaptor_Curve(myCurve);
        -   Second sequence:
        // Step 1
        occ::handle<Geom_Curve> myCurve = ... ;
        GeomAdaptor_Curve Crv (myCurve);
        // Step 2
        occ::handle<GeomAdaptor_Curve>
        Curve = new
        GeomAdaptor_Curve(Crv);
        You use the second part of this sequence if you already
        have the adapted curve Crv.
        The boundary is then constructed with the Curve object:
        double Tol = ... ;
        double dummy = 0. ;
        myBoundary = GeomFill_SimpleBound
        (Curve,Tol,dummy);
        """

    @overload
    def __init__(self, theOther: GeomFill_SimpleBound) -> None: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt: ...

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None: ...

    def Reparametrize(self, First: float, Last: float, HasDF: bool, HasDL: bool, DF: float, DL: float, Rev: bool) -> None: ...

    def Bounds(self) -> tuple[float, float]: ...

    def IsDegenerated(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_SnglrFunc(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """to represent function C'(t)^C''(t)"""

    @overload
    def __init__(self, HC: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_SnglrFunc) -> None: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    def SetRatio(self, Ratio: float) -> None: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

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

class GeomFill_Stretch(GeomFill_Filling):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float], W3: nanoocp.NCollection.NCollection_Array1[float], W4: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Stretch) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def Init(self, P1: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P2: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P3: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], P4: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], W1: nanoocp.NCollection.NCollection_Array1[float], W2: nanoocp.NCollection.NCollection_Array1[float], W3: nanoocp.NCollection.NCollection_Array1[float], W4: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

class GeomFill_Sweep:
    """Geometrical Sweep Algorithm"""

    @overload
    def __init__(self, Location: GeomFill_LocationLaw | None, WithKpart: bool = True) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Sweep) -> None: ...

    def SetDomain(self, First: float, Last: float, SectionFirst: float, SectionLast: float) -> None:
        """
        Set parametric information
        [<First>, <Last>] Sets the parametric bound of the
        sweeping surface to build.
        <SectionFirst>, <SectionLast> gives corresponding
        bounds parameter on the section law of <First> and <Last>

        V-Iso on Sweeping Surface S(u,v) is defined by
        Location(v) and Section(w) where
        w = SectionFirst + (v - First) / (Last-First)
        * (SectionLast - SectionFirst)

        By default w = v, and First and Last are given by
        First and Last parameter stored in LocationLaw.
        """

    def SetTolerance(self, Tol3d: float, BoundTol: float = 1.0, Tol2d: float = 1e-05, TolAngular: float = 1.0) -> None:
        """
        Set Approximation Tolerance
        Tol3d : Tolerance to surface approximation
        Tol2d : Tolerance used to perform curve approximation
        Normally the 2d curve are approximated with a
        tolerance given by the resolution method define in
        <LocationLaw> but if this tolerance is too large Tol2d
        is used.
        TolAngular : Tolerance (in radian) to control the angle
        between tangents on the section law and
        tangent of iso-v on approximated surface
        """

    def SetForceApproxC1(self, ForceApproxC1: bool) -> None:
        """
        Set the flag that indicates attempt to approximate
        a C1-continuous surface if a swept surface proved
        to be C0.
        """

    def ExchangeUV(self) -> bool:
        """
        returns true if sections are U-Iso
        This can be produce in some cases when <WithKpart> is True.
        """

    def UReversed(self) -> bool:
        """
        returns true if Parametrisation sens in U is inverse of
        parametrisation sens of section (or of path if ExchangeUV)
        """

    def VReversed(self) -> bool:
        """
        returns true if Parametrisation sens in V is inverse of
        parametrisation sens of path (or of section if ExchangeUV)
        """

    def Build(self, Section: GeomFill_SectionLaw | None, Methode: GeomFill_ApproxStyle = GeomFill_ApproxStyle.GeomFill_Location, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Degmax: int = 10, Segmax: int = 30) -> None:
        """
        Build the Sweeep Surface
        ApproxStyle defines Approximation Strategy
        - GeomFill_Section : The composed Function : Location X Section
        is directly approximated.
        - GeomFill_Location : The location law is approximated, and the
        SweepSurface is build algebric composition
        of approximated location law and section law
        This option is Ok, if Section.Surface() methode
        is effective.
        Continuity : The continuity in v waiting on the surface
        Degmax     : The maximum degree in v required on the surface
        Segmax     : The maximum number of span in v required on
        the surface

        raise If Domain are infinite or Profile not set.
        """

    def IsDone(self) -> bool:
        """Tells if the Surface is Built."""

    def ErrorOnSurface(self) -> float:
        """Gets the Approximation error."""

    def ErrorOnRestriction(self, IsFirst: bool) -> tuple[float, float]:
        """Gets the Approximation error."""

    def ErrorOnTrace(self, IndexOfTrace: int) -> tuple[float, float]:
        """Gets the Approximation error."""

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    def Restriction(self, IsFirst: bool) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def NumberOfTrace(self) -> int: ...

    def Trace(self, IndexOfTrace: int) -> nanoocp.Geom2d.Geom2d_Curve: ...

class GeomFill_SweepFunction(nanoocp.Approx.Approx_SweepFunction):
    """
    Function to approximate by SweepApproximation from
    Approx. To build general sweep Surface.
    """

    @overload
    def __init__(self, Section: GeomFill_SectionLaw | None, Location: GeomFill_LocationLaw | None, FirstParameter: float, FirstParameterOnS: float, RatioParameterOnS: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_SweepFunction) -> None: ...

    def D0(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        """

    def D2(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        """

    def Nb2dCurves(self) -> int:
        """get the number of 2d curves to approximate."""

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of a section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the section is rational or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def Resolution(self, Index: int, Tol: float) -> tuple[float, float]:
        """
        Returns the resolutions in the sub-space 2d <Index>
        This information is useful to find a good tolerance in
        2d approximation.
        Warning: Used only if Nb2dCurve > 0
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary (in radian)
        SurfTol error inside the surface.
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if <me> has to be run numerical
        algorithme to perform D0, D1 or D2
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface. An very poor
        estimation is sufficient. This information is useful
        to perform well conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the maximum section. This
        information is useful to perform well conditioned rational
        approximation.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections. This information is useful to
        perform well conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_SweepSectionGenerator:
    """
    class for instantiation of AppBlend.
    evaluate the sections of a sweep surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, Radius: float) -> None:
        """Create a sweept surface with a constant radius."""

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None) -> None:
        """Create a sweept surface with a constant section"""

    @overload
    def __init__(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, LastSect: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Create a sweept surface with an evolving section
        The section evaluate from First to Last Section
        """

    @overload
    def __init__(self, Path: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve1: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve2: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Radius: float) -> None:
        """
        Create a pipe with a constant radius with 2
        guide-line.
        """

    @overload
    def __init__(self, theOther: GeomFill_SweepSectionGenerator) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, Radius: float) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Geom.Geom_Curve | None, FirstSect: nanoocp.Geom.Geom_Curve | None, LastSect: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def Init(self, Path: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve1: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Curve2: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Radius: float) -> None: ...

    def Perform(self, Polynomial: bool = False) -> None: ...

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def NbSections(self) -> int: ...

    @overload
    def Section(self, P: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Transformation(self, Index: int) -> nanoocp.gp.gp_Trsf:
        """raised if <Index> not in the range [1,NbSections()]"""

    def Parameter(self, P: int) -> float:
        """
        Returns the parameter of <P>, to impose it for the
        approximation.
        """

class GeomFill_Tensor:
    """used to store the "gradient of gradient\""""

    @overload
    def __init__(self, NbRow: int, NbCol: int, NbMat: int) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_Tensor) -> None: ...

    def Init(self, InitialValue: float) -> None:
        """Initialize all the elements of a Tensor to InitialValue."""

    def Value(self, Row: int, Col: int, Mat: int) -> float:
        """
        accesses (in read or write mode) the value of index <Row>,
        <Col> and <Mat> of a Tensor.
        An exception is raised if <Row>, <Col> or <Mat> are not
        in the correct range.
        """

    @overload
    def __call__(self, Row: int, Col: int, Mat: int) -> float: ...

    @overload
    def __call__(self, Row: int, Col: int, Mat: int) -> float: ...

    def ChangeValue(self, Row: int, Col: int, Mat: int) -> float:
        """
        accesses (in read or write mode) the value of index <Row>,
        <Col> and <Mat> of a Tensor.
        An exception is raised if <Row>, <Col> or <Mat> are not
        in the correct range.
        """

    def SetValue(self, Row: int, Col: int, Mat: int, theValue: float) -> None:
        """
        Python addition: sets the value ChangeValue(Row, Col, Mat) returns by reference in C++.
        """

    def __getitem__(self, arg: tuple[int, int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(Row, Col, Mat) returns by reference in C++.
        """

    def Multiply(self, Right: nanoocp.math.math_Vector, Product: nanoocp.math.math_Matrix) -> None: ...

class GeomFill_TgtField(nanoocp.Standard.Standard_Transient):
    """
    Root class defining the methods we need to make an
    algorithmic tangents field.
    """

    def IsScalable(self) -> bool: ...

    def Scale(self, Func: nanoocp.Law.Law_BSpline | None) -> None: ...

    def Value(self, W: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the value of the field of tangency at
        parameter W.
        """

    @overload
    def D1(self, W: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of the field of tangency at
        parameter W.
        """

    @overload
    def D1(self, W: float, V: nanoocp.gp.gp_Vec, DV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the value and the derivative of the field of
        tangency at parameter W.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_TgtOnCoons(GeomFill_TgtField):
    """
    Defines an algorithmic tangents field on a
    boundary of a CoonsAlgPatch.
    """

    @overload
    def __init__(self, K: GeomFill_CoonsAlgPatch | None, I: int) -> None: ...

    @overload
    def __init__(self, theOther: GeomFill_TgtOnCoons) -> None: ...

    def Value(self, W: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the value of the field of tangency at
        parameter W.
        """

    @overload
    def D1(self, W: float) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of the field of tangency at
        parameter W.
        """

    @overload
    def D1(self, W: float, T: nanoocp.gp.gp_Vec, DT: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the value and the derivative of the field of
        tangency at parameter W.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomFill_UniformSection(GeomFill_SectionLaw):
    """Define an Constant Section Law"""

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve | None, FirstParameter: float = 0.0, LastParameter: float = 1.0) -> None:
        """
        Make an constant Law with C.
        [First, Last] define law definition domain
        """

    @overload
    def __init__(self, theOther: GeomFill_UniformSection) -> None: ...

    def D0(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        Warning : It used only for C2 approximation
        """

    def BSplineSurface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        give if possible an bspline Surface, like iso-v are the
        section. If it is not possible this method have to
        get an Null Surface. Is it the default implementation.
        """

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the sections are rational or not"""

    def IsUPeriodic(self) -> bool:
        """Returns if the sections are periodic or not"""

    def IsVPeriodic(self) -> bool:
        """Returns if the law isperiodic or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def GetInterval(self) -> tuple[float, float]:
        """
        Gets the bounds of the parametric interval on
        the function
        """

    def GetDomain(self) -> tuple[float, float]:
        """
        Gets the bounds of the function parametric domain.
        Warning: This domain it is not modified by the
        SetValue method
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerances associated at each poles to
        reach in approximation, to satisfy: BoundTol error
        at the Boundary AngleTol tangent error at the
        Boundary (in radian) SurfTol error inside the
        surface.
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface.
        An very poor estimation is sufficient.
        This information is useful to perform well
        conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the greater section. This
        information is useful to G1's control.
        Warning: With an little value, approximation can be slower.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        in all sections.
        This information is useful to control error
        in rational approximation.
        Warning: Used only if <me> IsRational
        """

    def IsConstant(self) -> tuple[bool, float]:
        """return True"""

    def ConstantSection(self) -> nanoocp.Geom.Geom_Curve:
        """Return the constant Section if <me> IsConstant."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
GeomFill_SequenceOfTrsf = nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Trsf]
