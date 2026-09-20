"""OCCT package Geom2dEval (toolkit TKG2d)"""

from typing import overload

import nanoocp.Geom2d
from nanoocp.Geom2dEval import (
    Geom2dEval_RepCurveDesc as Geom2dEval_RepCurveDesc
)
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class Geom2dEval_AHTBezierCurve(nanoocp.Geom2d.Geom2d_BoundedCurve):
    """
    2D Algebraic-Hyperbolic-Trigonometric Bezier curve.
    Uses a mixed basis: {1, t, ..., t^k, sinh(alpha*t), cosh(alpha*t), sin(beta*t), cos(beta*t)}.
    The number of basis functions = algDegree + 1 + 2*(alpha>0) + 2*(beta>0) must equal NbPoles.
    Parameter range: [0, 1].
    """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theAlgDegree: int, theAlpha: float, theBeta: float) -> None:
        """
        Non-rational constructor.
        @param[in] thePoles control points
        @param[in] theAlgDegree algebraic polynomial degree (>= 0)
        @param[in] theAlpha hyperbolic frequency (>= 0, 0 = no hyperbolic terms)
        @param[in] theBeta trigonometric frequency (>= 0, 0 = no trig terms)
        """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theWeights: nanoocp.NCollection.NCollection_Array1[float], theAlgDegree: int, theAlpha: float, theBeta: float) -> None:
        """
        Rational constructor.
        @param[in] thePoles control points
        @param[in] theWeights weights for each pole (must be > 0)
        @param[in] theAlgDegree algebraic polynomial degree (>= 0)
        @param[in] theAlpha hyperbolic frequency (>= 0, 0 = no hyperbolic terms)
        @param[in] theBeta trigonometric frequency (>= 0, 0 = no trig terms)
        """

    @overload
    def __init__(self, theOther: Geom2dEval_AHTBezierCurve) -> None: ...

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns the array of poles."""

    def Weights(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the array of weights."""

    def AlgDegree(self) -> int:
        """Returns the algebraic polynomial degree."""

    def Alpha(self) -> float:
        """Returns the hyperbolic frequency parameter."""

    def Beta(self) -> float:
        """Returns the trigonometric frequency parameter."""

    def NbPoles(self) -> int:
        """Returns the number of poles."""

    def IsRational(self) -> bool:
        """Returns true if the curve is rational (has explicit weights)."""

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the start point of the curve (at parameter 0)."""

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the end point of the curve (at parameter 1)."""

    def Reverse(self) -> None:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def FirstParameter(self) -> float:
        """Returns the value of the first parameter: 0.0."""

    def LastParameter(self) -> float:
        """Returns the value of the last parameter: 1.0."""

    def IsClosed(self) -> bool:
        """Returns true if the curve is closed."""

    def IsPeriodic(self) -> bool:
        """Returns false. The AHT-Bezier curve is not periodic."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN."""

    def IsCN(self, N: int) -> bool:
        """
        Returns true for any N. The AHT-Bezier curve is infinitely differentiable.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the N-th derivative at parameter U.
        @param[in] U the parameter value
        @param[in] N the derivative order (must be >= 1)
        @return the N-th derivative vector
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Creates a new object which is a copy of this curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2dEval_ArchimedeanSpiralCurve(nanoocp.Geom2d.Geom2d_Curve):
    """
    Describes a 2D Archimedean spiral curve.
    The polar equation is r = a + b*t, where a is the initial radius
    and b is the growth rate per radian.

    The parametric equation is:
    @code
    C(t) = O + (a + b*t)*cos(t)*XDir + (a + b*t)*sin(t)*YDir
    @endcode
    where:
    - O, XDir are from the local coordinate system,
    - YDir is the perpendicular to XDir,
    - a is the initial radius (>= 0),
    - b is the growth rate per radian (> 0).

    The parameter range is [0, +inf). The curve is neither periodic nor closed.
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2d, theInitialRadius: float, theGrowthRate: float) -> None:
        """
        Creates an Archimedean spiral.
        @param[in] thePosition the local coordinate system
        @param[in] theInitialRadius the initial radius (must be >= 0)
        @param[in] theGrowthRate the growth rate per radian (must be > 0)
        @throw Standard_ConstructionError if theInitialRadius < 0 or theGrowthRate <= 0
        """

    @overload
    def __init__(self, theOther: Geom2dEval_ArchimedeanSpiralCurve) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Ax2d:
        """Returns the local coordinate system."""

    def InitialRadius(self) -> float:
        """Returns the initial radius."""

    def GrowthRate(self) -> float:
        """Returns the growth rate per radian."""

    def Reverse(self) -> None:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def FirstParameter(self) -> float:
        """Returns 0."""

    def LastParameter(self) -> float:
        """Returns Precision::Infinite()."""

    def IsClosed(self) -> bool:
        """Returns false."""

    def IsPeriodic(self) -> bool:
        """Returns false."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN."""

    def IsCN(self, N: int) -> bool:
        """Returns true for any N >= 0."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the N-th derivative at parameter U.
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Creates a new object which is a copy of this curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2dEval_CircleInvoluteCurve(nanoocp.Geom2d.Geom2d_Curve):
    """
    Describes a 2D involute of a circle.
    Critical for gear tooth profiles.

    The parametric equation is:
    @code
    C(t) = O + R*(cos(t) + t*sin(t))*XDir + R*(sin(t) - t*cos(t))*YDir
    @endcode
    where:
    - O, XDir are from the local coordinate system,
    - YDir is the perpendicular to XDir,
    - R is the base circle radius (> 0).

    The parameter range is [0, +inf).
    At t=0, the curve starts on the base circle. D1(0) = (0,0) (cusp).
    |D1(t)| = R*t (speed linear in parameter).
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2d, theRadius: float) -> None:
        """
        Creates an involute of a circle.
        @param[in] thePosition the local coordinate system
        @param[in] theRadius the base circle radius (must be > 0)
        @throw Standard_ConstructionError if theRadius <= 0
        """

    @overload
    def __init__(self, theOther: Geom2dEval_CircleInvoluteCurve) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Ax2d:
        """Returns the local coordinate system."""

    def Radius(self) -> float:
        """Returns the base circle radius."""

    def Reverse(self) -> None:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def FirstParameter(self) -> float:
        """Returns 0."""

    def LastParameter(self) -> float:
        """Returns Precision::Infinite()."""

    def IsClosed(self) -> bool:
        """Returns false."""

    def IsPeriodic(self) -> bool:
        """Returns false."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN."""

    def IsCN(self, N: int) -> bool:
        """Returns true for any N >= 0."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the N-th derivative at parameter U.
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Creates a new object which is a copy of this curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2dEval_LogarithmicSpiralCurve(nanoocp.Geom2d.Geom2d_Curve):
    """
    Describes a 2D logarithmic (equiangular) spiral curve.
    The polar equation is r = a*exp(b*t).

    The parametric equation is:
    @code
    C(t) = O + a*exp(b*t)*cos(t)*XDir + a*exp(b*t)*sin(t)*YDir
    @endcode
    where:
    - O, XDir are from the local coordinate system,
    - YDir is the perpendicular to XDir,
    - a is the scale factor (> 0),
    - b is the growth exponent (> 0).

    The parameter range is (-inf, +inf).
    The angle between tangent and radial direction is constant = atan(1/b).
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2d, theScale: float, theGrowthExponent: float) -> None:
        """
        Creates a logarithmic spiral.
        @param[in] thePosition the local coordinate system
        @param[in] theScale the scale factor (must be > 0)
        @param[in] theGrowthExponent the growth exponent (must be > 0)
        @throw Standard_ConstructionError if theScale <= 0 or theGrowthExponent <= 0
        """

    @overload
    def __init__(self, theOther: Geom2dEval_LogarithmicSpiralCurve) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Ax2d:
        """Returns the local coordinate system."""

    def Scale(self) -> float:
        """Returns the scale factor."""

    def GrowthExponent(self) -> float:
        """Returns the growth exponent."""

    def Reverse(self) -> None:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def FirstParameter(self) -> float:
        """Returns -Precision::Infinite()."""

    def LastParameter(self) -> float:
        """Returns Precision::Infinite()."""

    def IsClosed(self) -> bool:
        """Returns false."""

    def IsPeriodic(self) -> bool:
        """Returns false."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN."""

    def IsCN(self, N: int) -> bool:
        """Returns true for any N >= 0."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the N-th derivative at parameter U.
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Creates a new object which is a copy of this curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2dEval_SineWaveCurve(nanoocp.Geom2d.Geom2d_Curve):
    """
    Describes a 2D sine wave curve.

    The parametric equation is:
    @code
    C(t) = O + t*XDir + A*sin(omega*t + phi)*YDir
    @endcode
    where:
    - O, XDir, YDir are from the local coordinate system (gp_Ax2d gives XDir,
    YDir is the perpendicular),
    - A is the amplitude (> 0),
    - omega is the angular frequency (> 0),
    - phi is the phase shift.

    The parameter range is (-inf, +inf). The curve is not periodic.
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2d, theAmplitude: float, theOmega: float, thePhase: float = 0.0) -> None:
        """
        Creates a 2D sine wave curve.
        @param[in] thePosition the local coordinate system
        @param[in] theAmplitude the wave amplitude (must be > 0)
        @param[in] theOmega the angular frequency (must be > 0)
        @param[in] thePhase the phase shift (default 0)
        @throw Standard_ConstructionError if theAmplitude <= 0 or theOmega <= 0
        """

    @overload
    def __init__(self, theOther: Geom2dEval_SineWaveCurve) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Ax2d:
        """Returns the local coordinate system."""

    def Amplitude(self) -> float:
        """Returns the amplitude."""

    def Omega(self) -> float:
        """Returns the angular frequency."""

    def Phase(self) -> float:
        """Returns the phase shift."""

    def Reverse(self) -> None:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def FirstParameter(self) -> float:
        """Returns -Precision::Infinite()."""

    def LastParameter(self) -> float:
        """Returns Precision::Infinite()."""

    def IsClosed(self) -> bool:
        """Returns false."""

    def IsPeriodic(self) -> bool:
        """Returns false."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN."""

    def IsCN(self, N: int) -> bool:
        """Returns true for any N >= 0."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the N-th derivative at parameter U.
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Creates a new object which is a copy of this curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2dEval_TBezierCurve(nanoocp.Geom2d.Geom2d_BoundedCurve):
    """
    2D Trigonometric Bezier curve.
    Uses a trigonometric Bernstein-like basis over the space
    {1, sin(alpha*t), cos(alpha*t), ..., sin(n*alpha*t), cos(n*alpha*t)}.

    The parameter domain is [0, Pi/alpha].
    The number of control points is 2*n + 1 for order n.

    The alpha parameter controls the frequency of the trigonometric basis.
    A T-Bezier curve of order n with poles P_0, P_1, ..., P_{2n} is:
    @code
    C(t) = P_0 * T_0(t) + P_1 * T_1(t) + ... + P_{2n} * T_{2n}(t)
    @endcode
    where:
    - T_0(t) = 1
    - T_{2k-1}(t) = sin(k * alpha * t), for k = 1..n
    - T_{2k}(t) = cos(k * alpha * t), for k = 1..n

    For rational curves, each pole is weighted:
    @code
    C(t) = sum(w_i * P_i * T_i(t)) / sum(w_i * T_i(t))
    @endcode
    """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theAlpha: float) -> None:
        """
        Constructs a non-rational T-Bezier curve from poles and alpha.
        @param[in] thePoles control points (1-based, size must be odd >= 3)
        @param[in] theAlpha frequency parameter (must be > 0)
        @throw Standard_ConstructionError if NbPoles is not odd or < 3 or theAlpha <= 0
        """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theWeights: nanoocp.NCollection.NCollection_Array1[float], theAlpha: float) -> None:
        """
        Constructs a rational T-Bezier curve.
        @param[in] thePoles control points (1-based, size must be odd >= 3)
        @param[in] theWeights weights (same size as poles, all > 0)
        @param[in] theAlpha frequency parameter (must be > 0)
        @throw Standard_ConstructionError if validation fails
        """

    @overload
    def __init__(self, theOther: Geom2dEval_TBezierCurve) -> None: ...

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns the poles array."""

    def Weights(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the weights array (empty if non-rational)."""

    def Alpha(self) -> float:
        """Returns the frequency parameter alpha."""

    def NbPoles(self) -> int:
        """Returns the number of poles."""

    def Order(self) -> int:
        """Returns the trigonometric order n (NbPoles = 2*n + 1)."""

    def IsRational(self) -> bool:
        """Returns true if the curve is rational."""

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the start point C(0)."""

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the end point C(Pi/alpha)."""

    def Reverse(self) -> None:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval curve.
        @throw Standard_NotImplemented
        """

    def FirstParameter(self) -> float:
        """Returns the first parameter value: 0.0."""

    def LastParameter(self) -> float:
        """Returns the last parameter value: Pi/alpha."""

    def IsClosed(self) -> bool:
        """Returns true if StartPoint and EndPoint coincide."""

    def IsPeriodic(self) -> bool:
        """Returns false. T-Bezier curves are not periodic."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN. T-Bezier curves are infinitely differentiable."""

    def IsCN(self, N: int) -> bool:
        """Returns true for all N. T-Bezier curves are infinitely differentiable."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point C(U)."""

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """Computes the point and first derivative at U."""

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """Computes the point and first two derivatives at U."""

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """Computes the point and first three derivatives at U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the N-th derivative at U.
        @param[in] U parameter value
        @param[in] N derivative order (must be >= 1)
        @return the N-th derivative vector
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Creates a new object which is a copy of this T-Bezier curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
