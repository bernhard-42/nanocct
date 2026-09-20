"""OCCT package GeomAdaptor (toolkit TKG3d)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BSplCLib
import nanoocp.BSplSLib
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.GeomEval.GeomEval_RepCurveDesc
import nanoocp.GeomEval.GeomEval_RepSurfaceDesc
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.GeomEval


class GeomAdaptor:
    """
    this package contains the geometric definition of
    curve and surface necessary to use algorithms.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomAdaptor) -> None: ...

    @staticmethod
    def MakeCurve(C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.Geom.Geom_Curve:
        """
        Inherited from GHCurve. Provides a curve
        handled by reference.
        Build a Geom_Curve using the information from the
        Curve from Adaptor3d
        """

    @staticmethod
    def MakeSurface(theS: nanoocp.Adaptor3d.Adaptor3d_Surface, theTrimFlag: bool = True) -> nanoocp.Geom.Geom_Surface:
        """
        Build a Geom_Surface using the information from the Surface from Adaptor3d
        @param theS - Surface adaptor to convert.
        @param theTrimFlag - True if perform trim surface values by adaptor and false otherwise.
        """

class GeomAdaptor_Curve(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """
    This class provides an interface between the services provided by any
    curve from the package Geom and those required of the curve by algorithms which use it.
    Creation of the loaded curve the curve is C1 by piece.

    Polynomial coefficients of BSpline curves used for their evaluation are
    cached for better performance. Therefore these evaluations are not
    thread-safe and parallel evaluations need to be prevented.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theCurve: nanoocp.Geom.Geom_Curve) -> None: ...

    @overload
    def __init__(self, theCurve: nanoocp.Geom.Geom_Curve, theUFirst: float, theULast: float) -> None:
        """
        Standard_ConstructionError is raised if theUFirst > theULast + Precision::PConfusion()
        """

    @overload
    def __init__(self, theOther: GeomAdaptor_Curve) -> None: ...

    class OffsetData:
        """Internal structure for offset curve evaluation data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Curve.OffsetData) -> None: ...

        @property
        def BasisAdaptor(self) -> GeomAdaptor_Curve:
            """Adaptor for basis curve"""

        @BasisAdaptor.setter
        def BasisAdaptor(self, arg: GeomAdaptor_Curve, /) -> None: ...

        @property
        def Offset(self) -> float:
            """Offset distance"""

        @Offset.setter
        def Offset(self, arg: float, /) -> None: ...

        @property
        def Direction(self) -> nanoocp.gp.gp_Dir:
            """Offset direction"""

        @Direction.setter
        def Direction(self, arg: nanoocp.gp.gp_Dir, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepCurveDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepCurveDesc.Base, /) -> None: ...

    class BezierData:
        """Internal structure for Bezier curve cache data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Curve.BezierData) -> None: ...

        @property
        def Curve(self) -> nanoocp.Geom.Geom_BezierCurve:
            """Bezier curve to prevent downcasts"""

        @Curve.setter
        def Curve(self, arg: nanoocp.Geom.Geom_BezierCurve, /) -> None: ...

        @property
        def Cache(self) -> nanoocp.BSplCLib.BSplCLib_Cache:
            """Cached data for evaluation"""

        @Cache.setter
        def Cache(self, arg: nanoocp.BSplCLib.BSplCLib_Cache, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepCurveDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepCurveDesc.Base, /) -> None: ...

    class BSplineData:
        """Internal structure for BSpline curve cache data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Curve.BSplineData) -> None: ...

        @property
        def Curve(self) -> nanoocp.Geom.Geom_BSplineCurve:
            """BSpline curve to prevent downcasts"""

        @Curve.setter
        def Curve(self, arg: nanoocp.Geom.Geom_BSplineCurve, /) -> None: ...

        @property
        def Cache(self) -> nanoocp.BSplCLib.BSplCLib_Cache:
            """Cached data for evaluation"""

        @Cache.setter
        def Cache(self, arg: nanoocp.BSplCLib.BSplCLib_Cache, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepCurveDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepCurveDesc.Base, /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    def Reset(self) -> None:
        """Reset currently loaded curve (undone Load())."""

    @overload
    def Load(self, theCurve: nanoocp.Geom.Geom_Curve) -> None: ...

    @overload
    def Load(self, theCurve: nanoocp.Geom.Geom_Curve, theUFirst: float, theULast: float) -> None:
        """
        Standard_ConstructionError is raised if theUFirst > theULast + Precision::PConfusion()
        """

    def Curve(self) -> nanoocp.Geom.Geom_Curve:
        """
        Provides a curve inherited from Hcurve from Adaptor.
        This is inherited to provide easy to use constructors.
        """

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

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

    def Resolution(self, R3d: float) -> float:
        """returns the parametric resolution"""

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int:
        """
        this should NEVER make a copy
        of the underlying curve to read
        the relevant information
        """

    def IsRational(self) -> bool:
        """
        this should NEVER make a copy
        of the underlying curve to read
        the relevant information
        """

    def NbPoles(self) -> int:
        """
        this should NEVER make a copy
        of the underlying curve to read
        the relevant information
        """

    def NbKnots(self) -> int:
        """
        this should NEVER make a copy
        of the underlying curve to read
        the relevant information
        """

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve:
        """
        this will NOT make a copy of the
        Bezier Curve : If you want to modify
        the Curve please make a copy yourself
        Also it will NOT trim the surface to
        myFirst/Last.
        """

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        this will NOT make a copy of the
        BSpline Curve : If you want to modify
        the Curve please make a copy yourself
        Also it will NOT trim the surface to
        myFirst/Last.
        """

    def OffsetCurve(self) -> nanoocp.Geom.Geom_OffsetCurve: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Point evaluation. Raises an exception on failure."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """D1 evaluation. Raises an exception on failure."""

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """D2 evaluation. Raises an exception on failure."""

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """D3 evaluation. Raises an exception on failure."""

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """DN evaluation. Raises an exception on failure."""

class GeomAdaptor_Surface(nanoocp.Adaptor3d.Adaptor3d_Surface):
    """
    An interface between the services provided by any
    surface from the package Geom and those required
    of the surface by algorithms which use it.
    Creation of the loaded surface the surface is C1 by piece

    Polynomial coefficients of BSpline surfaces used for their evaluation are
    cached for better performance. Therefore these evaluations are not
    thread-safe and parallel evaluations need to be prevented.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theSurf: nanoocp.Geom.Geom_Surface) -> None: ...

    @overload
    def __init__(self, theSurf: nanoocp.Geom.Geom_Surface, theUFirst: float, theULast: float, theVFirst: float, theVLast: float, theTolU: float = 0.0, theTolV: float = 0.0) -> None:
        """Standard_ConstructionError is raised if UFirst>ULast or VFirst>VLast"""

    @overload
    def __init__(self, theOther: GeomAdaptor_Surface) -> None: ...

    class ExtrusionData:
        """Internal structure for extrusion surface evaluation data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Surface.ExtrusionData) -> None: ...

        @property
        def BasisCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
            """Adaptor for basis curve"""

        @BasisCurve.setter
        def BasisCurve(self, arg: nanoocp.Adaptor3d.Adaptor3d_Curve, /) -> None: ...

        @property
        def Direction(self) -> nanoocp.gp.gp_XYZ:
            """Extrusion direction XYZ (normalized)"""

        @Direction.setter
        def Direction(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base, /) -> None: ...

    class RevolutionData:
        """Internal structure for revolution surface evaluation data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Surface.RevolutionData) -> None: ...

        @property
        def BasisCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
            """Adaptor for basis curve"""

        @BasisCurve.setter
        def BasisCurve(self, arg: nanoocp.Adaptor3d.Adaptor3d_Curve, /) -> None: ...

        @property
        def Axis(self) -> nanoocp.gp.gp_Ax1:
            """Revolution axis"""

        @Axis.setter
        def Axis(self, arg: nanoocp.gp.gp_Ax1, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base, /) -> None: ...

    class OffsetData:
        """Internal structure for offset surface evaluation data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Surface.OffsetData) -> None: ...

        @property
        def BasisAdaptor(self) -> GeomAdaptor_Surface:
            """Adaptor for basis surface"""

        @BasisAdaptor.setter
        def BasisAdaptor(self, arg: GeomAdaptor_Surface, /) -> None: ...

        @property
        def EquivalentAdaptor(self) -> GeomAdaptor_Surface:
            """Adaptor for equivalent surface (if exists)"""

        @EquivalentAdaptor.setter
        def EquivalentAdaptor(self, arg: GeomAdaptor_Surface, /) -> None: ...

        @property
        def OffsetSurface(self) -> nanoocp.Geom.Geom_OffsetSurface:
            """Original offset surface for osculating queries"""

        @OffsetSurface.setter
        def OffsetSurface(self, arg: nanoocp.Geom.Geom_OffsetSurface, /) -> None: ...

        @property
        def Offset(self) -> float:
            """Offset distance"""

        @Offset.setter
        def Offset(self, arg: float, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base, /) -> None: ...

    class BezierData:
        """Internal structure for Bezier surface cache data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Surface.BezierData) -> None: ...

        @property
        def Surface(self) -> nanoocp.Geom.Geom_BezierSurface:
            """Bezier surface to prevent downcasts"""

        @Surface.setter
        def Surface(self, arg: nanoocp.Geom.Geom_BezierSurface, /) -> None: ...

        @property
        def Cache(self) -> nanoocp.BSplSLib.BSplSLib_Cache:
            """Cached data for evaluation"""

        @Cache.setter
        def Cache(self, arg: nanoocp.BSplSLib.BSplSLib_Cache, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base, /) -> None: ...

    class BSplineData:
        """Internal structure for BSpline surface cache data."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: GeomAdaptor_Surface.BSplineData) -> None: ...

        @property
        def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
            """BSpline surface to prevent downcasts"""

        @Surface.setter
        def Surface(self, arg: nanoocp.Geom.Geom_BSplineSurface, /) -> None: ...

        @property
        def Cache(self) -> nanoocp.BSplSLib.BSplSLib_Cache:
            """Cached data for evaluation"""

        @Cache.setter
        def Cache(self, arg: nanoocp.BSplSLib.BSplSLib_Cache, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.GeomEval.GeomEval_RepSurfaceDesc.Base, /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, theSurf: nanoocp.Geom.Geom_Surface) -> None: ...

    @overload
    def Load(self, theSurf: nanoocp.Geom.Geom_Surface, theUFirst: float, theULast: float, theVFirst: float, theVLast: float, theTolU: float = 0.0, theTolV: float = 0.0) -> None:
        """
        Standard_ConstructionError is raised if theUFirst>theULast or theVFirst>theVLast
        """

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    def FirstUParameter(self) -> float: ...

    def LastUParameter(self) -> float: ...

    def FirstVParameter(self) -> float: ...

    def LastVParameter(self) -> float: ...

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds of the surface.
        @param[out] theU1 minimum U parameter
        @param[out] theU2 maximum U parameter
        @param[out] theV1 minimum V parameter
        @param[out] theV2 maximum V parameter
        """

    def ToleranceU(self) -> float:
        """Returns tolerance in U direction."""

    def ToleranceV(self) -> float:
        """Returns tolerance in V direction."""

    def UContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbUIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of U intervals for continuity
        <S>. May be one if UContinuity(me) >= <S>
        """

    def NbVIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of V intervals for continuity
        <S>. May be one if VContinuity(me) >= <S>
        """

    def UIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the U direction.
        """

    def VIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the V direction.
        """

    def UTrim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """
        Returns a surface trimmed in the U direction
        equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def VTrim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """
        Returns a surface trimmed in the V direction between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsUPeriodic(self) -> bool: ...

    def UPeriod(self) -> float: ...

    def IsVPeriodic(self) -> bool: ...

    def VPeriod(self) -> float: ...

    def EvalD0(self, theU: float, theV: float) -> nanoocp.gp.gp_Pnt:
        """Point evaluation. Raises an exception on failure."""

    def EvalD1(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """D1 evaluation. Raises an exception on failure."""

    def EvalD2(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """D2 evaluation. Raises an exception on failure."""

    def EvalD3(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """D3 evaluation. Raises an exception on failure."""

    def EvalDN(self, theU: float, theV: float, theNu: int, theNv: int) -> nanoocp.gp.gp_Vec:
        """DN evaluation. Raises an exception on failure."""

    def UResolution(self, R3d: float) -> float:
        """
        Returns the parametric U resolution corresponding
        to the real space resolution <R3d>.
        """

    def VResolution(self, R3d: float) -> float:
        """
        Returns the parametric V resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """
        Returns the type of the surface: Plane, Cylinder,
        Cone, Sphere, Torus, BezierSurface,
        BSplineSurface, SurfaceOfRevolution,
        SurfaceOfExtrusion, OtherSurface
        """

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone: ...

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def UDegree(self) -> int: ...

    def NbUPoles(self) -> int: ...

    def VDegree(self) -> int: ...

    def NbVPoles(self) -> int: ...

    def NbUKnots(self) -> int: ...

    def NbVKnots(self) -> int: ...

    def IsURational(self) -> bool: ...

    def IsVRational(self) -> bool: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierSurface:
        """
        This will NOT make a copy of the
        Bezier Surface : If you want to modify
        the Surface please make a copy yourself
        Also it will NOT trim the surface to
        myU/VFirst/Last.
        """

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        This will NOT make a copy of the
        BSpline Surface : If you want to modify
        the Surface please make a copy yourself
        Also it will NOT trim the surface to
        myU/VFirst/Last.
        """

    def AxeOfRevolution(self) -> nanoocp.gp.gp_Ax1: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def BasisCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def BasisSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def OffsetValue(self) -> float: ...

class GeomAdaptor_SurfaceOfLinearExtrusion(GeomAdaptor_Surface):
    """
    Generalised cylinder. This surface is obtained by sweeping a curve in a given
    direction. The parametrization range for the parameter U is defined
    with referenced the curve.
    The parametrization range for the parameter V is ]-infinite,+infinite[
    The position of the curve gives the origin for the parameter V.
    The continuity of the surface is CN in the V direction.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """The Curve is loaded."""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, V: nanoocp.gp.gp_Dir) -> None:
        """Thew Curve and the Direction are loaded."""

    @overload
    def __init__(self, theOther: GeomAdaptor_SurfaceOfLinearExtrusion) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """Changes the Curve"""

    @overload
    def Load(self, V: nanoocp.gp.gp_Dir) -> None:
        """Changes the Direction"""

    def FirstUParameter(self) -> float: ...

    def LastUParameter(self) -> float: ...

    def FirstVParameter(self) -> float: ...

    def LastVParameter(self) -> float: ...

    def UContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Return CN."""

    def NbUIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of U intervals for continuity
        <S>. May be one if UContinuity(me) >= <S>
        """

    def NbVIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of V intervals for continuity
        <S>. May be one if VContinuity(me) >= <S>
        """

    def UIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the U direction.
        """

    def VIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the V direction.
        """

    def UTrim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """
        Returns a surface trimmed in the U direction
        equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def VTrim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """
        Returns a surface trimmed in the V direction between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsUPeriodic(self) -> bool: ...

    def UPeriod(self) -> float: ...

    def IsVPeriodic(self) -> bool: ...

    def VPeriod(self) -> float: ...

    def UResolution(self, R3d: float) -> float:
        """
        Returns the parametric U resolution corresponding
        to the real space resolution <R3d>.
        """

    def VResolution(self, R3d: float) -> float:
        """
        Returns the parametric V resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """
        Returns the type of the surface: Plane, Cylinder,
        Cone, Sphere, Torus, BezierSurface,
        BSplineSurface, SurfaceOfRevolution,
        SurfaceOfExtrusion, OtherSurface
        """

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone: ...

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def UDegree(self) -> int: ...

    def NbUPoles(self) -> int: ...

    def IsURational(self) -> bool: ...

    def IsVRational(self) -> bool: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierSurface: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineSurface: ...

    def AxeOfRevolution(self) -> nanoocp.gp.gp_Ax1: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def BasisCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

class GeomAdaptor_SurfaceOfRevolution(GeomAdaptor_Surface):
    """
    This class defines a complete surface of revolution.
    The surface is obtained by rotating a curve a complete revolution
    about an axis. The curve and the axis must be in the same plane.
    If the curve and the axis are not in the same plane it is always
    possible to be in the previous case after a cylindrical projection
    of the curve in a referenced plane.
    For a complete surface of revolution the parametric range is
    0 <= U <= 2*PI
    The parametric range for V is defined with the revolved curve.
    The origin of the U parametrization is given by the position
    of the revolved curve (reference). The direction of the revolution
    axis defines the positive sense of rotation (trigonometric sense)
    corresponding to the increasing of the parametric value U.
    The derivatives are always defined for the u direction.
    For the v direction the definition of the derivatives depends on
    the degree of continuity of the referenced curve.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """The Curve is loaded."""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, V: nanoocp.gp.gp_Ax1) -> None:
        """The Curve and the Direction are loaded."""

    @overload
    def __init__(self, theOther: GeomAdaptor_SurfaceOfRevolution) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """Changes the Curve"""

    @overload
    def Load(self, V: nanoocp.gp.gp_Ax1) -> None:
        """Changes the Direction"""

    def AxeOfRevolution(self) -> nanoocp.gp.gp_Ax1: ...

    def FirstUParameter(self) -> float: ...

    def LastUParameter(self) -> float: ...

    def FirstVParameter(self) -> float: ...

    def LastVParameter(self) -> float: ...

    def UContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Return CN."""

    def NbUIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of U intervals for continuity
        <S>. May be one if UContinuity(me) >= <S>
        """

    def NbVIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of V intervals for continuity
        <S>. May be one if VContinuity(me) >= <S>
        """

    def UIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the U direction.
        """

    def VIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the V direction.
        """

    def UTrim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """
        Returns a surface trimmed in the U direction
        equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def VTrim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """
        Returns a surface trimmed in the V direction between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsUPeriodic(self) -> bool: ...

    def UPeriod(self) -> float: ...

    def IsVPeriodic(self) -> bool: ...

    def VPeriod(self) -> float: ...

    def UResolution(self, R3d: float) -> float:
        """
        Returns the parametric U resolution corresponding
        to the real space resolution <R3d>.
        """

    def VResolution(self, R3d: float) -> float:
        """
        Returns the parametric V resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """
        Returns the type of the surface: Plane, Cylinder,
        Cone, Sphere, Torus, BezierSurface,
        BSplineSurface, SurfaceOfRevolution,
        SurfaceOfExtrusion, OtherSurface
        """

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone:
        """
        Apex of the Cone = Cone.Position().Location()
        ==> ReferenceRadius = 0.
        """

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def VDegree(self) -> int: ...

    def NbVPoles(self) -> int: ...

    def NbVKnots(self) -> int: ...

    def IsURational(self) -> bool: ...

    def IsVRational(self) -> bool: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierSurface: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineSurface: ...

    def Axis(self) -> nanoocp.gp.gp_Ax3: ...

    def BasisCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

class GeomAdaptor_TransformedCurve(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """
    An adaptor for curves with an applied transformation.

    This class wraps a GeomAdaptor_Curve (or an Adaptor3d_CurveOnSurface) and
    applies a gp_Trsf transformation to all point and derivative evaluations.
    It serves as a base class for BRepAdaptor_Curve and allows batch evaluation
    with transformations in GeomGridEval_Curve.

    The evaluation methods (Value, D0, D1, D2, D3, DN) are marked final
    to enable optimizations in grid evaluation.
    """

    @overload
    def __init__(self) -> None:
        """Creates an undefined curve with identity transformation."""

    @overload
    def __init__(self, theCurve: nanoocp.Geom.Geom_Curve, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Creates a curve adaptor with transformation.
        @param theCurve underlying geometry
        @param theTrsf transformation to apply
        """

    @overload
    def __init__(self, theCurve: nanoocp.Geom.Geom_Curve, theFirst: float, theLast: float, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Creates a curve adaptor with transformation and parameter bounds.
        @param theCurve underlying geometry
        @param theFirst minimum parameter
        @param theLast maximum parameter
        @param theTrsf transformation to apply
        """

    @overload
    def __init__(self, theOther: GeomAdaptor_TransformedCurve) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor."""

    @overload
    def Load(self, theCurve: nanoocp.Geom.Geom_Curve) -> None:
        """
        Loads the curve geometry.
        @param theCurve underlying geometry
        """

    @overload
    def Load(self, theCurve: nanoocp.Geom.Geom_Curve, theFirst: float, theLast: float) -> None:
        """
        Loads the curve geometry with parameter bounds.
        @param theCurve underlying geometry
        @param theFirst minimum parameter
        @param theLast maximum parameter
        """

    def LoadCurveOnSurface(self, theConSurf: nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface) -> None:
        """
        Sets the curve on surface adaptor.
        @param theConSurf curve on surface adaptor
        """

    def SetTrsf(self, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Sets the transformation.
        @param theTrsf transformation to apply
        """

    def Trsf(self) -> nanoocp.gp.gp_Trsf:
        """Returns the transformation."""

    def Is3DCurve(self) -> bool:
        """Returns true if the geometry is a 3D curve (not curve on surface)."""

    def IsCurveOnSurface(self) -> bool:
        """Returns true if the geometry is a curve on surface."""

    def Curve(self) -> GeomAdaptor_Curve:
        """Returns the underlying GeomAdaptor_Curve."""

    def ChangeCurve(self) -> GeomAdaptor_Curve:
        """Returns the underlying GeomAdaptor_Curve for modification."""

    def CurveOnSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface:
        """Returns the CurveOnSurface adaptor."""

    def GeomCurve(self) -> nanoocp.Geom.Geom_Curve:
        """Returns the underlying Geom_Curve."""

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, theS: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    def Intervals(self, theT: nanoocp.NCollection.NCollection_Array1[float], theS: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Trim(self, theFirst: float, theLast: float, theTol: float) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Point evaluation. Applies transformation after evaluation."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """D1 evaluation. Applies transformation after evaluation."""

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """D2 evaluation. Applies transformation after evaluation."""

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """D3 evaluation. Applies transformation after evaluation."""

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """DN evaluation. Applies transformation after evaluation."""

    def Resolution(self, theR3d: float) -> float: ...

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def OffsetCurve(self) -> nanoocp.Geom.Geom_OffsetCurve: ...

class GeomAdaptor_TransformedSurface(nanoocp.Adaptor3d.Adaptor3d_Surface):
    """
    An adaptor for surfaces with an applied transformation.

    This class wraps a GeomAdaptor_Surface and applies a gp_Trsf transformation
    to all point and derivative evaluations. It serves as a base class for
    BRepAdaptor_Surface and allows batch evaluation with transformations in
    GeomGridEval_Surface.

    The evaluation methods (Value, D0, D1, D2, D3, DN) are marked final
    to enable optimizations in grid evaluation.
    """

    @overload
    def __init__(self) -> None:
        """Creates an undefined surface with identity transformation."""

    @overload
    def __init__(self, theSurface: nanoocp.Geom.Geom_Surface, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Creates a surface adaptor with transformation.
        @param theSurface underlying geometry
        @param theTrsf transformation to apply
        """

    @overload
    def __init__(self, theSurface: nanoocp.Geom.Geom_Surface, theUFirst: float, theULast: float, theVFirst: float, theVLast: float, theTrsf: nanoocp.gp.gp_Trsf, theTolU: float = 0.0, theTolV: float = 0.0) -> None:
        """
        Creates a surface adaptor with transformation and parameter bounds.
        @param theSurface underlying geometry
        @param theUFirst minimum U parameter
        @param theULast maximum U parameter
        @param theVFirst minimum V parameter
        @param theVLast maximum V parameter
        @param theTrsf transformation to apply
        @param theTolU tolerance in U direction
        @param theTolV tolerance in V direction
        """

    @overload
    def __init__(self, theOther: GeomAdaptor_TransformedSurface) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Shallow copy of adaptor."""

    @overload
    def Load(self, theSurface: nanoocp.Geom.Geom_Surface, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Loads the surface geometry.
        @param theSurface underlying geometry
        @param theTrsf transformation to apply
        """

    @overload
    def Load(self, theSurface: nanoocp.Geom.Geom_Surface, theUFirst: float, theULast: float, theVFirst: float, theVLast: float, theTrsf: nanoocp.gp.gp_Trsf, theTolU: float = 0.0, theTolV: float = 0.0) -> None:
        """
        Loads the surface geometry with parameter bounds.
        @param theSurface underlying geometry
        @param theUFirst minimum U parameter
        @param theULast maximum U parameter
        @param theVFirst minimum V parameter
        @param theVLast maximum V parameter
        @param theTrsf transformation to apply
        @param theTolU tolerance in U direction
        @param theTolV tolerance in V direction
        """

    def SetTrsf(self, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Sets the transformation.
        @param theTrsf transformation to apply
        """

    def HasTrsf(self) -> bool:
        """Returns true if non-identity transformation is applied."""

    def Trsf(self) -> nanoocp.gp.gp_Trsf:
        """Returns the transformation."""

    def AdaptorSurfaceOriginal(self) -> GeomAdaptor_Surface:
        """
        Returns the underlying original GeomAdaptor_Surface without transformation applied.
        """

    def AdaptorSurfaceTransformed(self) -> GeomAdaptor_Surface:
        """
        Returns an adaptor for the transformed surface state.
        Uses the original adaptor for identity transformation to preserve existing trimming.
        """

    def GeomSurfaceOriginal(self) -> nanoocp.Geom.Geom_Surface:
        """
        Returns the underlying original Geom_Surface without transformation applied.
        """

    def GeomSurfaceTransformed(self) -> nanoocp.Geom.Geom_Surface:
        """Returns the transformed Geom_Surface cached for current state."""

    def FirstUParameter(self) -> float: ...

    def LastUParameter(self) -> float: ...

    def FirstVParameter(self) -> float: ...

    def LastVParameter(self) -> float: ...

    def UContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbUIntervals(self, theS: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    def NbVIntervals(self, theS: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    def UIntervals(self, theT: nanoocp.NCollection.NCollection_Array1[float], theS: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def VIntervals(self, theT: nanoocp.NCollection.NCollection_Array1[float], theS: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def UTrim(self, theFirst: float, theLast: float, theTol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def VTrim(self, theFirst: float, theLast: float, theTol: float) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsUPeriodic(self) -> bool: ...

    def UPeriod(self) -> float: ...

    def IsVPeriodic(self) -> bool: ...

    def VPeriod(self) -> float: ...

    def ToleranceU(self) -> float:
        """Returns tolerance in U direction."""

    def ToleranceV(self) -> float:
        """Returns tolerance in V direction."""

    def EvalD0(self, theU: float, theV: float) -> nanoocp.gp.gp_Pnt:
        """Point evaluation. Applies transformation after evaluation."""

    def EvalD1(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """D1 evaluation. Applies transformation after evaluation."""

    def EvalD2(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """D2 evaluation. Applies transformation after evaluation."""

    def EvalD3(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """D3 evaluation. Applies transformation after evaluation."""

    def EvalDN(self, theU: float, theV: float, theNu: int, theNv: int) -> nanoocp.gp.gp_Vec:
        """DN evaluation. Applies transformation after evaluation."""

    def UResolution(self, theR3d: float) -> float: ...

    def VResolution(self, theR3d: float) -> float: ...

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType: ...

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone: ...

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def UDegree(self) -> int: ...

    def NbUPoles(self) -> int: ...

    def VDegree(self) -> int: ...

    def NbVPoles(self) -> int: ...

    def NbUKnots(self) -> int: ...

    def NbVKnots(self) -> int: ...

    def IsURational(self) -> bool: ...

    def IsVRational(self) -> bool: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierSurface: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineSurface: ...

    def AxeOfRevolution(self) -> nanoocp.gp.gp_Ax1: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def BasisCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def BasisSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def OffsetValue(self) -> float: ...
