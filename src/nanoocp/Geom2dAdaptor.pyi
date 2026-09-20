"""OCCT package Geom2dAdaptor (toolkit TKG2d)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.BSplCLib
import nanoocp.Geom2d
import nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.Geom2dEval


class Geom2dAdaptor:
    """
    this package contains the geometric definition of
    2d curves compatible with the Adaptor package
    templates.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def MakeCurve(HC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Inherited from GHCurve. Provides a curve
        handled by reference.
        Creates a 2d curve from a HCurve2d. This
        cannot process the OtherCurves.
        """

class Geom2dAdaptor_Curve(nanoocp.Adaptor2d.Adaptor2d_Curve2d):
    """
    An interface between the services provided by any
    curve from the package Geom2d and those required
    of the curve by algorithms which use it.

    Polynomial coefficients of BSpline curves used for their evaluation are
    cached for better performance. Therefore these evaluations are not
    thread-safe and parallel evaluations need to be prevented.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Curve, UFirst: float, ULast: float) -> None:
        """Standard_ConstructionError is raised if Ufirst>Ulast"""

    class OffsetData:
        """Internal structure for 2D offset curve evaluation data."""

        def __init__(self) -> None: ...

        @property
        def BasisAdaptor(self) -> Geom2dAdaptor_Curve:
            """Adaptor for basis curve"""

        @BasisAdaptor.setter
        def BasisAdaptor(self, arg: Geom2dAdaptor_Curve, /) -> None: ...

        @property
        def Offset(self) -> float:
            """Offset distance"""

        @Offset.setter
        def Offset(self, arg: float, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base, /) -> None: ...

    class BezierData:
        """Internal structure for Bezier curve evaluation data."""

        def __init__(self) -> None: ...

        @property
        def Curve(self) -> nanoocp.Geom2d.Geom2d_BezierCurve:
            """Bezier curve to prevent downcasts"""

        @Curve.setter
        def Curve(self, arg: nanoocp.Geom2d.Geom2d_BezierCurve, /) -> None: ...

        @property
        def Cache(self) -> nanoocp.BSplCLib.BSplCLib_Cache:
            """Cached data for evaluation"""

        @Cache.setter
        def Cache(self, arg: nanoocp.BSplCLib.BSplCLib_Cache, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base, /) -> None: ...

    class BSplineData:
        """Internal structure for BSpline curve evaluation data."""

        def __init__(self) -> None: ...

        @property
        def Curve(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
            """BSpline curve to prevent downcasts"""

        @Curve.setter
        def Curve(self, arg: nanoocp.Geom2d.Geom2d_BSplineCurve, /) -> None: ...

        @property
        def Cache(self) -> nanoocp.BSplCLib.BSplCLib_Cache:
            """Cached data for evaluation"""

        @Cache.setter
        def Cache(self, arg: nanoocp.BSplCLib.BSplCLib_Cache, /) -> None: ...

        @property
        def EvalRep(self) -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base:
            """Eval representation descriptor"""

        @EvalRep.setter
        def EvalRep(self, arg: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base, /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Shallow copy of adaptor"""

    def Reset(self) -> None:
        """Reset currently loaded curve (undone Load())."""

    @overload
    def Load(self, theCurve: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    @overload
    def Load(self, theCurve: nanoocp.Geom2d.Geom2d_Curve, theUFirst: float, theULast: float) -> None:
        """
        Standard_ConstructionError is raised if theUFirst > theULast + Precision::PConfusion()
        """

    def IsInitialized(self) -> bool:
        """Returns true if the adaptor has been loaded with a curve."""

    def Curve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

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
        """Computes the point of parameter U on the curve"""

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U."""

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

    def Resolution(self, Ruv: float) -> float:
        """returns the parametric resolution"""

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def NbSamples(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt2d:
        """Point evaluation. Raises an exception on failure."""

    def EvalD1(self, theU: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """D1 evaluation. Raises an exception on failure."""

    def EvalD2(self, theU: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """D2 evaluation. Raises an exception on failure."""

    def EvalD3(self, theU: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """D3 evaluation. Raises an exception on failure."""

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec2d:
        """DN evaluation. Raises an exception on failure."""
