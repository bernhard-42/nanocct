"""OCCT package GeomEval (toolkit TKG3d)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.GeomAbs
from nanoocp.GeomEval import (
    GeomEval_RepCurveDesc as GeomEval_RepCurveDesc,
    GeomEval_RepSurfaceDesc as GeomEval_RepSurfaceDesc
)
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class GeomEval_AHTBezierCurve(nanoocp.Geom.Geom_BoundedCurve):
    """
    3D Algebraic-Hyperbolic-Trigonometric Bezier curve.
    Uses a mixed basis: {1, t, ..., t^k, sinh(alpha*t), cosh(alpha*t), sin(beta*t), cos(beta*t)}.
    The number of basis functions = algDegree + 1 + 2*(alpha>0) + 2*(beta>0) must equal NbPoles.
    Parameter range: [0, 1].
    """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theAlgDegree: int, theAlpha: float, theBeta: float) -> None:
        """
        Non-rational constructor.
        @param[in] thePoles control points
        @param[in] theAlgDegree algebraic polynomial degree (>= 0)
        @param[in] theAlpha hyperbolic frequency (>= 0, 0 = no hyperbolic terms)
        @param[in] theBeta trigonometric frequency (>= 0, 0 = no trig terms)
        """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array1[float], theAlgDegree: int, theAlpha: float, theBeta: float) -> None:
        """
        Rational constructor.
        @param[in] thePoles control points
        @param[in] theWeights weights for each pole (must be > 0)
        @param[in] theAlgDegree algebraic polynomial degree (>= 0)
        @param[in] theAlpha hyperbolic frequency (>= 0, 0 = no hyperbolic terms)
        @param[in] theBeta trigonometric frequency (>= 0, 0 = no trig terms)
        """

    @overload
    def __init__(self, theOther: GeomEval_AHTBezierCurve) -> None: ...

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
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

    def StartPoint(self) -> nanoocp.gp.gp_Pnt:
        """Returns the start point of the curve (at parameter 0)."""

    def EndPoint(self) -> nanoocp.gp.gp_Pnt:
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

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the N-th derivative at parameter U.
        @param[in] U the parameter value
        @param[in] N the derivative order (must be >= 1)
        @return the N-th derivative vector
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this curve."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_AHTBezierSurface(nanoocp.Geom.Geom_BoundedSurface):
    """
    Tensor-product Algebraic-Hyperbolic-Trigonometric Bezier surface.
    Uses a mixed basis in each parametric direction:
    {1, t, ..., t^k, sinh(alpha*t), cosh(alpha*t), sin(beta*t), cos(beta*t)}.

    Separate AHT parameters per direction: (algDegreeU, alphaU, betaU)
    and (algDegreeV, alphaV, betaV).

    The number of basis functions in each direction must equal the number
    of poles in that direction.
    Parameter range: U in [0, 1], V in [0, 1].
    """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theAlgDegreeU: int, theAlgDegreeV: int, theAlphaU: float, theAlphaV: float, theBetaU: float, theBetaV: float) -> None:
        """
        Non-rational constructor.
        @param[in] thePoles 2D array of control points
        @param[in] theAlgDegreeU algebraic polynomial degree in U (>= 0)
        @param[in] theAlgDegreeV algebraic polynomial degree in V (>= 0)
        @param[in] theAlphaU hyperbolic frequency in U (>= 0)
        @param[in] theAlphaV hyperbolic frequency in V (>= 0)
        @param[in] theBetaU trigonometric frequency in U (>= 0)
        @param[in] theBetaV trigonometric frequency in V (>= 0)
        """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array2[float], theAlgDegreeU: int, theAlgDegreeV: int, theAlphaU: float, theAlphaV: float, theBetaU: float, theBetaV: float) -> None:
        """
        Rational constructor.
        @param[in] thePoles 2D array of control points
        @param[in] theWeights 2D array of weights (must be > 0)
        @param[in] theAlgDegreeU algebraic polynomial degree in U (>= 0)
        @param[in] theAlgDegreeV algebraic polynomial degree in V (>= 0)
        @param[in] theAlphaU hyperbolic frequency in U (>= 0)
        @param[in] theAlphaV hyperbolic frequency in V (>= 0)
        @param[in] theBetaU trigonometric frequency in U (>= 0)
        @param[in] theBetaV trigonometric frequency in V (>= 0)
        """

    @overload
    def __init__(self, theOther: GeomEval_AHTBezierSurface) -> None: ...

    def Poles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """Returns the 2D array of poles."""

    def Weights(self) -> nanoocp.NCollection.NCollection_Array2[float]:
        """Returns the 2D array of weights."""

    def AlgDegreeU(self) -> int:
        """Returns the algebraic polynomial degree in U."""

    def AlgDegreeV(self) -> int:
        """Returns the algebraic polynomial degree in V."""

    def AlphaU(self) -> float:
        """Returns the hyperbolic frequency in U."""

    def AlphaV(self) -> float:
        """Returns the hyperbolic frequency in V."""

    def BetaU(self) -> float:
        """Returns the trigonometric frequency in U."""

    def BetaV(self) -> float:
        """Returns the trigonometric frequency in V."""

    def NbPolesU(self) -> int:
        """Returns the number of poles in U direction."""

    def NbPolesV(self) -> int:
        """Returns the number of poles in V direction."""

    def IsURational(self) -> bool:
        """Returns true if the surface is rational in U direction."""

    def IsVRational(self) -> bool:
        """Returns true if the surface is rational in V direction."""

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds.
        @param[out] U1 lower U bound (0)
        @param[out] U2 upper U bound (1)
        @param[out] V1 lower V bound (0)
        @param[out] V2 upper V bound (1)
        """

    def IsUClosed(self) -> bool:
        """Returns false. The AHT-Bezier surface is not closed in U."""

    def IsVClosed(self) -> bool:
        """Returns false. The AHT-Bezier surface is not closed in V."""

    def IsUPeriodic(self) -> bool:
        """Returns false. The AHT-Bezier surface is not periodic in U."""

    def IsVPeriodic(self) -> bool:
        """Returns false. The AHT-Bezier surface is not periodic in V."""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Isoparametric curve extraction is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Isoparametric curve extraction is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN."""

    def IsCNu(self, N: int) -> bool:
        """Returns true for any N."""

    def IsCNv(self, N: int) -> bool:
        """Returns true for any N."""

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point at parameters (U, V)."""

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in U and Nv in V.
        @param[in] U the u parameter
        @param[in] V the v parameter
        @param[in] Nu derivative order in u (must be >= 0)
        @param[in] Nv derivative order in v (must be >= 0)
        @return the derivative vector
        @throw Standard_RangeError if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this surface."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_CircularHelicoidSurface(nanoocp.Geom.Geom_ElementarySurface):
    """
    Describes a circular helicoid surface.
    A ruled surface generated by a line segment rotating uniformly about an axis
    while translating along it. Named "circular" because the generating line
    sweeps circular helices at constant radius.

    The parametric equation is:
    @code
    S(u,v) = O + v*cos(u)*XDir + v*sin(u)*YDir + (P*u/(2*Pi))*ZDir
    @endcode
    where:
    - O, XDir, YDir, ZDir are from the local coordinate system (gp_Ax3),
    - P is the pitch (axial advance per 2*Pi turn, must be != 0).

    The parametric range is (-inf, +inf) for both u and v.
    The surface is neither periodic nor closed. Continuity is GeomAbs_CN.
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax3, thePitch: float) -> None:
        """
        Creates a circular helicoid surface.
        @param[in] thePosition the local coordinate system
        @param[in] thePitch the axial advance per 2*Pi turn (must be != 0)
        @throw Standard_ConstructionError if thePitch == 0
        """

    @overload
    def __init__(self, theOther: GeomEval_CircularHelicoidSurface) -> None: ...

    def Pitch(self) -> float:
        """Returns the pitch."""

    def SetPitch(self, thePitch: float) -> None:
        """
        Sets a new pitch value.
        @param[in] thePitch the new pitch (must be != 0)
        @throw Standard_ConstructionError if thePitch == 0
        """

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """Returns infinite bounds for both parameters."""

    def IsUClosed(self) -> bool:
        """Returns false."""

    def IsVClosed(self) -> bool:
        """Returns false."""

    def IsUPeriodic(self) -> bool:
        """Returns false."""

    def IsVPeriodic(self) -> bool:
        """Returns false."""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Isoparametric curve extraction is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Isoparametric curve extraction is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point S(U, V) on the surface."""

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in u and Nv in v.
        @throw Geom_UndefinedDerivative if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this surface."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_CircularHelixCurve(nanoocp.Geom.Geom_Curve):
    """
    Describes a circular helix in 3D space.
    A circular helix is an unbounded curve defined by a radius R,
    a pitch P (axial advance per full 2*Pi turn), and a coordinate system.

    The parametric equation is:
    @code
    C(t) = O + R*cos(t)*XDir + R*sin(t)*YDir + (P*t/(2*Pi))*ZDir
    @endcode
    where:
    - O, XDir, YDir, ZDir are the origin and directions of the local coordinate system,
    - R is the radius (> 0),
    - P is the pitch (can be negative for left-handed helix).

    The parameter range is (-inf, +inf). The curve is neither periodic nor closed.
    Continuity is GeomAbs_CN.
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2, theRadius: float, thePitch: float) -> None:
        """
        Creates a circular helix with the given coordinate system, radius, and pitch.
        @param[in] thePosition the local coordinate system
        @param[in] theRadius the helix radius (must be > 0)
        @param[in] thePitch the axial advance per 2*Pi turn (can be negative)
        @throw Standard_ConstructionError if theRadius <= 0
        """

    @overload
    def __init__(self, theOther: GeomEval_CircularHelixCurve) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Ax2:
        """Returns the local coordinate system."""

    def Radius(self) -> float:
        """Returns the helix radius."""

    def Pitch(self) -> float:
        """Returns the pitch (axial advance per 2*Pi turn)."""

    def Reverse(self) -> None:
        """
        Reversal of parametrization is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Reversal of parametrization is not supported for this eval geometry.
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

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the N-th derivative at parameter U.
        @param[in] U the parameter value
        @param[in] N the derivative order (must be >= 1)
        @return the N-th derivative vector
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this curve."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_EllipsoidSurface(nanoocp.Geom.Geom_ElementarySurface):
    """
    Describes a triaxial ellipsoid surface.
    An ellipsoid is defined by three semi-axes A, B, C (all > 0)
    and is positioned in space by a coordinate system (a gp_Ax3 object),
    the origin of which is the center of the ellipsoid.

    The parametric equation of the ellipsoid is:
    @code
    P(u,v) = O + A*cos(v)*cos(u)*XDir + B*cos(v)*sin(u)*YDir + C*sin(v)*ZDir
    @endcode
    where:
    - O, XDir, YDir and ZDir are respectively the origin,
    the "X Direction", the "Y Direction" and the "Z Direction"
    of its local coordinate system, and
    - A, B, C are the three semi-axes.

    The parametric range is:
    - [0, 2*Pi] for u, and
    - [-Pi/2, Pi/2] for v.

    When A == B the surface degenerates to a spheroid (ellipsoid of revolution).

    The implicit equation in local coordinates is:
    @code
    X^2/A^2 + Y^2/B^2 + Z^2/C^2 - 1 = 0
    @endcode
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax3, theA: float, theB: float, theC: float) -> None:
        """
        Creates a triaxial ellipsoid surface with the given local coordinate system
        and three semi-axes.
        @param[in] thePosition the local coordinate system
        @param[in] theA the semi-axis along XDir (must be > 0)
        @param[in] theB the semi-axis along YDir (must be > 0)
        @param[in] theC the semi-axis along ZDir (must be > 0)
        @throw Standard_ConstructionError if any semi-axis <= 0
        """

    @overload
    def __init__(self, theOther: GeomEval_EllipsoidSurface) -> None: ...

    def SemiAxisA(self) -> float:
        """Returns the semi-axis A (along XDir)."""

    def SemiAxisB(self) -> float:
        """Returns the semi-axis B (along YDir)."""

    def SemiAxisC(self) -> float:
        """Returns the semi-axis C (along ZDir)."""

    def SetSemiAxisA(self, theA: float) -> None:
        """
        Assigns the value theA to the semi-axis A.
        @param[in] theA the new semi-axis value (must be > 0)
        @throw Standard_ConstructionError if theA <= 0
        """

    def SetSemiAxisB(self, theB: float) -> None:
        """
        Assigns the value theB to the semi-axis B.
        @param[in] theB the new semi-axis value (must be > 0)
        @throw Standard_ConstructionError if theB <= 0
        """

    def SetSemiAxisC(self, theC: float) -> None:
        """
        Assigns the value theC to the semi-axis C.
        @param[in] theC the new semi-axis value (must be > 0)
        @throw Standard_ConstructionError if theC <= 0
        """

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this ellipsoid.
        @param[out] U1 lower U bound (0)
        @param[out] U2 upper U bound (2*Pi)
        @param[out] V1 lower V bound (-Pi/2)
        @param[out] V2 upper V bound (Pi/2)
        """

    def IsUClosed(self) -> bool:
        """Returns True. The ellipsoid is closed in U (period 2*Pi)."""

    def IsVClosed(self) -> bool:
        """Returns False."""

    def IsUPeriodic(self) -> bool:
        """Returns True. The ellipsoid is periodic in U (period 2*Pi)."""

    def IsVPeriodic(self) -> bool:
        """Returns False."""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the U isoparametric curve.
        For a triaxial ellipsoid, the U isoparametric curve is not
        a standard Geom_Curve type.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the V isoparametric curve.
        For a triaxial ellipsoid, the V isoparametric curve is not
        a standard Geom_Curve type (it is an ellipse only when A == B).
        @throw Standard_NotImplemented
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point P(U, V) on the surface.
        @code
        P(U, V) = O + A*cos(V)*cos(U)*XDir + B*cos(V)*sin(U)*YDir + C*sin(V)*ZDir
        @endcode
        """

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and the first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the direction u
        and Nv in the direction v.
        @param[in] U the u parameter
        @param[in] V the v parameter
        @param[in] Nu derivative order in u (must be >= 0)
        @param[in] Nv derivative order in v (must be >= 0)
        @return the derivative vector
        @throw Geom_UndefinedDerivative if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this ellipsoid."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Returns the coefficients of the implicit equation of the
        quadric in the absolute Cartesian coordinate system:
        @code
        A1*X^2 + A2*Y^2 + A3*Z^2 + 2*(B1*X*Y + B2*X*Z + B3*Y*Z) +
        2*(C1*X + C2*Y + C3*Z) + D = 0
        @endcode
        In local coordinates the equation is: X^2/A^2 + Y^2/B^2 + Z^2/C^2 - 1 = 0.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_HypParaboloidSurface(nanoocp.Geom.Geom_ElementarySurface):
    """
    Describes a hyperbolic paraboloid (saddle surface).

    A hyperbolic paraboloid is defined by two semi-axis lengths A and B,
    and is positioned in space by a coordinate system (a gp_Ax3 object),
    the origin of which is the saddle point.

    The parametric equation (rectangular parametrization) is:
    @code
    P(u,v) = O + u*XDir + v*YDir + (u^2/A^2 - v^2/B^2)*ZDir
    @endcode
    where:
    - O, XDir, YDir and ZDir are respectively the origin,
    the "X Direction", the "Y Direction" and the "Z Direction"
    of its local coordinate system, and
    - A and B are the semi-axis lengths (both > 0).

    The parametric range is:
    - (-inf, +inf) for u, and
    - (-inf, +inf) for v.

    The surface is doubly ruled, not periodic, and not closed.

    The implicit equation in local coordinates is:
    @code
    X^2/A^2 - Y^2/B^2 - Z = 0
    @endcode
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax3, theA: float, theB: float) -> None:
        """
        Creates a hyperbolic paraboloid surface with the given local coordinate system
        and semi-axis lengths.
        @param[in] thePosition the local coordinate system
        @param[in] theA the first semi-axis length (must be > 0)
        @param[in] theB the second semi-axis length (must be > 0)
        @throw Standard_ConstructionError if theA <= 0 or theB <= 0
        """

    @overload
    def __init__(self, theOther: GeomEval_HypParaboloidSurface) -> None: ...

    def SemiAxisA(self) -> float:
        """Returns the first semi-axis length A."""

    def SemiAxisB(self) -> float:
        """Returns the second semi-axis length B."""

    def SetSemiAxisA(self, theA: float) -> None:
        """
        Assigns the value theA to the first semi-axis length.
        @param[in] theA the new first semi-axis length (must be > 0)
        @throw Standard_ConstructionError if theA <= 0
        """

    def SetSemiAxisB(self, theB: float) -> None:
        """
        Assigns the value theB to the second semi-axis length.
        @param[in] theB the new second semi-axis length (must be > 0)
        @throw Standard_ConstructionError if theB <= 0
        """

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this surface.
        @param[out] U1 lower U bound (-Precision::Infinite())
        @param[out] U2 upper U bound (Precision::Infinite())
        @param[out] V1 lower V bound (-Precision::Infinite())
        @param[out] V2 upper V bound (Precision::Infinite())
        """

    def IsUClosed(self) -> bool:
        """Returns False. The hyperbolic paraboloid is not closed in U."""

    def IsVClosed(self) -> bool:
        """Returns False. The hyperbolic paraboloid is not closed in V."""

    def IsUPeriodic(self) -> bool:
        """Returns False. The hyperbolic paraboloid is not periodic in U."""

    def IsVPeriodic(self) -> bool:
        """Returns False. The hyperbolic paraboloid is not periodic in V."""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the U isoparametric curve.
        For a hyperbolic paraboloid, no standard Geom_Curve representation is available.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the V isoparametric curve.
        For a hyperbolic paraboloid, no standard Geom_Curve representation is available.
        @throw Standard_NotImplemented
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point P(U, V) on the surface.
        @code
        P(U, V) = O + U*XDir + V*YDir + (U^2/A^2 - V^2/B^2)*ZDir
        @endcode
        """

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and the first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the direction u
        and Nv in the direction v.
        @param[in] U the u parameter
        @param[in] V the v parameter
        @param[in] Nu derivative order in u (must be >= 0)
        @param[in] Nv derivative order in v (must be >= 0)
        @return the derivative vector
        @throw Geom_UndefinedDerivative if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this hyperbolic paraboloid."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Returns the coefficients of the implicit equation of the
        quadric in the absolute Cartesian coordinate system:
        @code
        A1*X^2 + A2*Y^2 + A3*Z^2 + 2*(B1*X*Y + B2*X*Z + B3*Y*Z) +
        2*(C1*X + C2*Y + C3*Z) + D = 0
        @endcode
        In local coordinates the equation is: X^2/A^2 - Y^2/B^2 - Z = 0.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_HyperboloidSurface(nanoocp.Geom.Geom_ElementarySurface):
    """
    Describes a hyperboloid of revolution surface (one-sheet or two-sheet).

    A hyperboloid is defined by two semi-axis radii R1 and R2, a sheet mode,
    and is positioned in space by a coordinate system (a gp_Ax3 object),
    the origin of which is the center of the hyperboloid.

    **One-sheet parametrization:**
    @code
    P(u,v) = O + R1*cosh(v)*cos(u)*XDir + R1*cosh(v)*sin(u)*YDir + R2*sinh(v)*ZDir
    @endcode
    Implicit equation in local coordinates:
    @code
    X^2/R1^2 + Y^2/R1^2 - Z^2/R2^2 = 1
    @endcode

    **Two-sheet parametrization** (covers one sheet only):
    @code
    P(u,v) = O + R2*sinh(v)*cos(u)*XDir + R2*sinh(v)*sin(u)*YDir + R1*cosh(v)*ZDir
    @endcode
    Implicit equation in local coordinates:
    @code
    X^2/R2^2 + Y^2/R2^2 - Z^2/R1^2 = -1
    @endcode
    The second sheet is not represented by this class.

    The parametric range is:
    - [0, 2*Pi] for u (periodic, closed), and
    - (-inf, +inf) for v (not periodic, not closed).
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax3, theR1: float, theR2: float, theMode: GeomEval_HyperboloidSurface.SheetMode = GeomEval_HyperboloidSurface.SheetMode.OneSheet) -> None:
        """
        Creates a hyperboloid surface with the given local coordinate system,
        semi-axis radii, and sheet mode.
        @param[in] thePosition local coordinate system
        @param[in] theR1 first semi-axis radius (must be > 0)
        @param[in] theR2 second semi-axis radius (must be > 0)
        @param[in] theMode one-sheet or two-sheet mode
        @throw Standard_ConstructionError if theR1 <= 0 or theR2 <= 0
        """

    @overload
    def __init__(self, theOther: GeomEval_HyperboloidSurface) -> None: ...

    class SheetMode(enum.Enum):
        """Sheet mode selector."""

        OneSheet = 0

        TwoSheets = 1

    def R1(self) -> float:
        """Returns the first semi-axis radius."""

    def R2(self) -> float:
        """Returns the second semi-axis radius."""

    def Mode(self) -> GeomEval_HyperboloidSurface.SheetMode:
        """Returns the sheet mode."""

    def SetR1(self, theR1: float) -> None:
        """
        Assigns the value theR1 to the first semi-axis radius.
        @param[in] theR1 the new first semi-axis radius (must be > 0)
        @throw Standard_ConstructionError if theR1 <= 0
        """

    def SetR2(self, theR2: float) -> None:
        """
        Assigns the value theR2 to the second semi-axis radius.
        @param[in] theR2 the new second semi-axis radius (must be > 0)
        @throw Standard_ConstructionError if theR2 <= 0
        """

    def SetMode(self, theMode: GeomEval_HyperboloidSurface.SheetMode) -> None:
        """
        Sets the sheet mode.
        @param[in] theMode one-sheet or two-sheet mode
        """

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this hyperboloid.
        @param[out] U1 lower U bound (0)
        @param[out] U2 upper U bound (2*Pi)
        @param[out] V1 lower V bound (-Precision::Infinite())
        @param[out] V2 upper V bound (Precision::Infinite())
        """

    def IsUClosed(self) -> bool:
        """Returns True. The hyperboloid is closed in U (period 2*Pi)."""

    def IsVClosed(self) -> bool:
        """Returns False."""

    def IsUPeriodic(self) -> bool:
        """Returns True. The hyperboloid is periodic in U (period 2*Pi)."""

    def IsVPeriodic(self) -> bool:
        """Returns False."""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the U isoparametric curve.
        For a hyperboloid, no standard Geom_Curve representation is available.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the V isoparametric curve.
        For a hyperboloid, no standard Geom_Curve representation is available.
        @throw Standard_NotImplemented
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point P(U, V) on the surface."""

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and the first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the direction u
        and Nv in the direction v.
        @param[in] U the u parameter
        @param[in] V the v parameter
        @param[in] Nu derivative order in u (must be >= 0)
        @param[in] Nv derivative order in v (must be >= 0)
        @return the derivative vector
        @throw Geom_UndefinedDerivative if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this hyperboloid."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Returns the coefficients of the implicit equation of the
        quadric in the absolute Cartesian coordinate system:
        @code
        A1*X^2 + A2*Y^2 + A3*Z^2 + 2*(B1*X*Y + B2*X*Z + B3*Y*Z) +
        2*(C1*X + C2*Y + C3*Z) + D = 0
        @endcode
        For one-sheet (local): X^2/R1^2 + Y^2/R1^2 - Z^2/R2^2 - 1 = 0.
        For two-sheet (local): X^2/R2^2 + Y^2/R2^2 - Z^2/R1^2 + 1 = 0.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_ParaboloidSurface(nanoocp.Geom.Geom_ElementarySurface):
    """
    Describes a circular paraboloid surface of revolution.
    A paraboloid is defined by its focal distance and is positioned
    in space by a coordinate system (a gp_Ax3 object), the origin
    of which is the vertex of the paraboloid.

    The parametric equation of the paraboloid is:
    @code
    P(u,v) = O + v*cos(u)*XDir + v*sin(u)*YDir + v^2/(4*F)*ZDir
    @endcode
    where:
    - O, XDir, YDir and ZDir are respectively the origin,
    the "X Direction", the "Y Direction" and the "Z Direction"
    of its local coordinate system, and
    - F is the focal distance.

    The parametric range is:
    - [0, 2*Pi] for u, and
    - (-inf, +inf) for v.

    The implicit equation in local coordinates is:
    @code
    X^2 + Y^2 - 4*F*Z = 0
    @endcode
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax3, theFocal: float) -> None:
        """
        Creates a paraboloid surface with the given local coordinate system
        and focal distance.
        @param[in] thePosition the local coordinate system
        @param[in] theFocal the focal distance (must be > 0)
        @throw Standard_ConstructionError if theFocal <= 0
        """

    @overload
    def __init__(self, theOther: GeomEval_ParaboloidSurface) -> None: ...

    def Focal(self) -> float:
        """Returns the focal distance of this paraboloid."""

    def SetFocal(self, theFocal: float) -> None:
        """
        Assigns the value theFocal to the focal distance of this paraboloid.
        @param[in] theFocal the new focal distance (must be > 0)
        @throw Standard_ConstructionError if theFocal <= 0
        """

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this paraboloid.
        @param[out] U1 lower U bound (0)
        @param[out] U2 upper U bound (2*Pi)
        @param[out] V1 lower V bound (-Precision::Infinite())
        @param[out] V2 upper V bound (Precision::Infinite())
        """

    def IsUClosed(self) -> bool:
        """Returns True. The paraboloid is closed in U (period 2*Pi)."""

    def IsVClosed(self) -> bool:
        """Returns False."""

    def IsUPeriodic(self) -> bool:
        """Returns True. The paraboloid is periodic in U (period 2*Pi)."""

    def IsVPeriodic(self) -> bool:
        """Returns False."""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the U isoparametric curve.
        For a paraboloid, the U isoparametric curve is a parabola,
        which is not a standard Geom_Curve type.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the V isoparametric curve.
        For a paraboloid, the V isoparametric curve is a circle of radius |v|,
        which degenerates to a point at v=0.
        @throw Standard_NotImplemented
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point P(U, V) on the surface.
        @code
        P(U, V) = O + V*cos(U)*XDir + V*sin(U)*YDir + V^2/(4*F)*ZDir
        @endcode
        """

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and the first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the direction u
        and Nv in the direction v.
        @param[in] U the u parameter
        @param[in] V the v parameter
        @param[in] Nu derivative order in u (must be >= 0)
        @param[in] Nv derivative order in v (must be >= 0)
        @return the derivative vector
        @throw Geom_UndefinedDerivative if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this paraboloid."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Returns the coefficients of the implicit equation of the
        quadric in the absolute Cartesian coordinate system:
        @code
        A1*X^2 + A2*Y^2 + A3*Z^2 + 2*(B1*X*Y + B2*X*Z + B3*Y*Z) +
        2*(C1*X + C2*Y + C3*Z) + D = 0
        @endcode
        In local coordinates the equation is: X^2 + Y^2 - 4*F*Z = 0.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_SineWaveCurve(nanoocp.Geom.Geom_Curve):
    """
    Describes a 3D sine wave curve.
    The curve lies in the plane defined by the local coordinate system,
    oscillating along YDir with propagation along XDir.

    The parametric equation is:
    @code
    C(t) = O + t*XDir + A*sin(omega*t + phi)*YDir
    @endcode
    where:
    - O, XDir, YDir are from the local coordinate system,
    - A is the amplitude (> 0),
    - omega is the angular frequency (> 0),
    - phi is the phase shift.

    The parameter range is (-inf, +inf). The curve is not periodic.
    """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2, theAmplitude: float, theOmega: float, thePhase: float = 0.0) -> None:
        """
        Creates a 3D sine wave curve.
        @param[in] thePosition the local coordinate system
        @param[in] theAmplitude the wave amplitude (must be > 0)
        @param[in] theOmega the angular frequency (must be > 0)
        @param[in] thePhase the phase shift (default 0)
        @throw Standard_ConstructionError if theAmplitude <= 0 or theOmega <= 0
        """

    @overload
    def __init__(self, theOther: GeomEval_SineWaveCurve) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Ax2:
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

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point at parameter U."""

    def EvalD1(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """Computes the point and first derivative at parameter U."""

    def EvalD2(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """Computes the point and first two derivatives at parameter U."""

    def EvalD3(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """Computes the point and first three derivatives at parameter U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the N-th derivative at parameter U.
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this curve."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_TBezierCurve(nanoocp.Geom.Geom_BoundedCurve):
    """
    3D Trigonometric Bezier curve.
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
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theAlpha: float) -> None:
        """
        Constructs a non-rational T-Bezier curve from poles and alpha.
        @param[in] thePoles control points (1-based, size must be odd >= 3)
        @param[in] theAlpha frequency parameter (must be > 0)
        @throw Standard_ConstructionError if NbPoles is not odd or < 3 or theAlpha <= 0
        """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array1[float], theAlpha: float) -> None:
        """
        Constructs a rational T-Bezier curve.
        @param[in] thePoles control points (1-based, size must be odd >= 3)
        @param[in] theWeights weights (same size as poles, all > 0)
        @param[in] theAlpha frequency parameter (must be > 0)
        @throw Standard_ConstructionError if validation fails
        """

    @overload
    def __init__(self, theOther: GeomEval_TBezierCurve) -> None: ...

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
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

    def StartPoint(self) -> nanoocp.gp.gp_Pnt:
        """Returns the start point C(0)."""

    def EndPoint(self) -> nanoocp.gp.gp_Pnt:
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

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point C(U)."""

    def EvalD1(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """Computes the point and first derivative at U."""

    def EvalD2(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """Computes the point and first two derivatives at U."""

    def EvalD3(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """Computes the point and first three derivatives at U."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the N-th derivative at U.
        @param[in] U parameter value
        @param[in] N derivative order (must be >= 1)
        @return the N-th derivative vector
        @throw Standard_RangeError if N < 1
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this T-Bezier curve."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomEval_TBezierSurface(nanoocp.Geom.Geom_BoundedSurface):
    """
    Tensor-product Trigonometric Bezier surface.
    Uses trigonometric Bernstein-like bases in both U and V directions
    over the space {1, sin(alpha*t), cos(alpha*t), ..., sin(n*alpha*t), cos(n*alpha*t)}.

    Parameter domain: U in [0, Pi/alphaU], V in [0, Pi/alphaV].
    Number of control points: (2*nU + 1) x (2*nV + 1) for orders nU, nV.

    The surface is:
    @code
    S(u,v) = sum_i sum_j P_ij * Bu_i(u) * Bv_j(v)
    @endcode
    where Bu_i and Bv_j are trigonometric basis functions in U and V respectively.

    For rational surfaces:
    @code
    S(u,v) = sum_i sum_j (w_ij * P_ij * Bu_i(u) * Bv_j(v))
    / sum_i sum_j (w_ij * Bu_i(u) * Bv_j(v))
    @endcode
    """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theAlphaU: float, theAlphaV: float) -> None:
        """
        Constructs a non-rational T-Bezier surface from poles and alpha parameters.
        @param[in] thePoles control points grid (row count and col count must be odd >= 3)
        @param[in] theAlphaU frequency parameter in U direction (must be > 0)
        @param[in] theAlphaV frequency parameter in V direction (must be > 0)
        @throw Standard_ConstructionError if validation fails
        """

    @overload
    def __init__(self, thePoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array2[float], theAlphaU: float, theAlphaV: float) -> None:
        """
        Constructs a rational T-Bezier surface.
        @param[in] thePoles control points grid
        @param[in] theWeights weights grid (same dimensions as poles, all > 0)
        @param[in] theAlphaU frequency parameter in U direction (must be > 0)
        @param[in] theAlphaV frequency parameter in V direction (must be > 0)
        @throw Standard_ConstructionError if validation fails
        """

    @overload
    def __init__(self, theOther: GeomEval_TBezierSurface) -> None: ...

    def Poles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """Returns the poles grid."""

    def Weights(self) -> nanoocp.NCollection.NCollection_Array2[float]:
        """Returns the weights grid (empty if non-rational)."""

    def AlphaU(self) -> float:
        """Returns the frequency parameter alpha in the U direction."""

    def AlphaV(self) -> float:
        """Returns the frequency parameter alpha in the V direction."""

    def NbUPoles(self) -> int:
        """Returns the number of poles in the U direction."""

    def NbVPoles(self) -> int:
        """Returns the number of poles in the V direction."""

    def OrderU(self) -> int:
        """Returns the trigonometric order in U (NbUPoles = 2*nU + 1)."""

    def OrderV(self) -> int:
        """Returns the trigonometric order in V (NbVPoles = 2*nV + 1)."""

    def IsRational(self) -> bool:
        """Returns true if the surface is rational."""

    def UReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReverse(self) -> None:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Reversal is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the parametric bounds.
        @param[out] U1 lower U bound (0)
        @param[out] U2 upper U bound (Pi/alphaU)
        @param[out] V1 lower V bound (0)
        @param[out] V2 upper V bound (Pi/alphaV)
        """

    def IsUClosed(self) -> bool:
        """Returns true if the surface is closed in U."""

    def IsVClosed(self) -> bool:
        """Returns true if the surface is closed in V."""

    def IsUPeriodic(self) -> bool:
        """Returns false. T-Bezier surfaces are not periodic in U."""

    def IsVPeriodic(self) -> bool:
        """Returns false. T-Bezier surfaces are not periodic in V."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN. T-Bezier surfaces are infinitely differentiable."""

    def IsCNu(self, N: int) -> bool:
        """
        Returns true for all N. T-Bezier surfaces are infinitely differentiable in U.
        """

    def IsCNv(self, N: int) -> bool:
        """
        Returns true for all N. T-Bezier surfaces are infinitely differentiable in V.
        """

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Isoparametric curve extraction is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Isoparametric curve extraction is not supported for this eval surface.
        @throw Standard_NotImplemented
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point S(U, V)."""

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """Computes the point and first partial derivatives at (U, V)."""

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """Computes the point and partial derivatives up to 2nd order at (U, V)."""

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """Computes the point and partial derivatives up to 3rd order at (U, V)."""

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in U and Nv in V.
        @param[in] U the u parameter
        @param[in] V the v parameter
        @param[in] Nu derivative order in U (must be >= 0)
        @param[in] Nv derivative order in V (must be >= 0)
        @return the derivative vector
        @throw Standard_RangeError if Nu + Nv < 1 or Nu < 0 or Nv < 0
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation is not supported for this eval geometry.
        @throw Standard_NotImplemented
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Creates a new object which is a copy of this T-Bezier surface."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
