"""OCCT package Convert (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.gp


class Convert_ParameterisationType(enum.IntEnum):
    """
    Identifies a type of parameterization of a circle or ellipse represented as a BSpline curve.
    For a circle with a center C and a radius R (for example a Geom2d_Circle or a Geom_Circle),
    the natural parameterization is angular. It uses the angle Theta made by the vector CM with
    the 'X Axis' of the circle's local coordinate system as parameter for the current point M. The
    coordinates of the point M are as follows:
    X   =   R *cos ( Theta )
    y   =   R * sin ( Theta )
    Similarly, for an ellipse with a center C, a major radius R and a minor radius r, the circle
    Circ with center C and radius R (and located in the same plane as the ellipse) lends its natural
    angular parameterization to the ellipse. This is achieved by an affine transformation in the
    plane of the ellipse, in the ratio r / R, about the 'X Axis' of its local coordinate system. The
    coordinates of the current point M are as follows:
    X   =   R * cos ( Theta )
    y   =   r * sin ( Theta )
    The process of converting a circle or an ellipse into a rational or non-rational BSpline curve
    transforms the Theta angular parameter into a parameter t. This ensures the rational or
    polynomial parameterization of the resulting BSpline curve. Several types of parametric
    transformations are available.
    TgtThetaOver2
    The most usual method is Convert_TgtThetaOver2 where the parameter t on the BSpline
    curve is obtained by means of transformation of the following type:
    t = tan ( Theta / 2 )
    The result of this definition is:
    cos ( Theta ) = ( 1. - t**2 ) / ( 1. + t**2 )
    sin ( Theta ) = 2. * t / ( 1. + t**2 )
    which ensures the rational parameterization of the circle or the ellipse. However, this is not
    the most suitable parameterization method where the arc of the circle or ellipse has a large
    opening angle. In such cases, the curve will be represented by a BSpline with intermediate
    knots. Each span, i.e. each portion of curve between two different knot values, will use
    parameterization of this type. The number of spans is calculated using the following rule: ( 1.2
    * Delta / Pi ) + 1 where Delta is equal to the opening angle (in radians) of the arc of the
    circle (Delta is equal to 2.* Pi in the case of a complete circle). The resulting BSpline curve
    is "exact", i.e. computing any point of parameter t on the BSpline curve gives an exact point on
    the circle or the ellipse. TgtThetaOver2_N Where N is equal to 1, 2, 3 or 4, this ensures the
    same type of parameterization as Convert_TgtThetaOver2 but sets the number of spans in the
    resulting BSpline curve to N rather than allowing the algorithm to make this calculation.
    However, the opening angle Delta (parametric angle, given in radians) of the arc of the circle
    (or of the ellipse) must comply with the following:
    -   Delta <= 0.9999 * Pi for the Convert_TgtThetaOver2_1 method, or
    -   Delta <= 1.9999 * Pi for the Convert_TgtThetaOver2_2 method.
    QuasiAngular
    The Convert_QuasiAngular method of parameterization uses a different type of rational
    parameterization. This method ensures that the parameter t along the resulting BSpline curve is
    very close to the natural parameterization angle Theta of the circle or ellipse (i.e. which uses
    the functions sin ( Theta ) and cos ( Theta ).
    The resulting BSpline curve is "exact", i.e. computing any point of parameter t on the BSpline
    curve gives an exact point on the circle or the ellipse.
    RationalC1
    The Convert_RationalC1 method of parameterization uses a further type of rational
    parameterization. This method ensures that the equation relating to the resulting BSpline curve
    has a "C1" continuous denominator, which is not the case with the above methods. RationalC1
    enhances the degree of continuity at the junction point of the different spans of the curve.
    The resulting BSpline curve is "exact", i.e. computing any point of parameter t on the BSpline
    curve gives an exact point on the circle or the ellipse.
    Polynomial
    The Convert_Polynomial method is used to produce polynomial (i.e. non-rational)
    parameterization of the resulting BSpline curve with 8 poles (i.e. a polynomial degree equal to
    7). However, the result is an approximation of the circle or ellipse (i.e. computing the point
    of parameter t on the BSpline curve does not give an exact point on the circle or the ellipse).
    """

    Convert_TgtThetaOver2 = 0

    Convert_TgtThetaOver2_1 = 1

    Convert_TgtThetaOver2_2 = 2

    Convert_TgtThetaOver2_3 = 3

    Convert_TgtThetaOver2_4 = 4

    Convert_QuasiAngular = 5

    Convert_RationalC1 = 6

    Convert_Polynomial = 7

class Convert_ConicToBSplineCurve:
    """
    Root class for algorithms which convert a conic curve into
    a BSpline curve (CircleToBSplineCurve, EllipseToBSplineCurve,
    HyperbolaToBSplineCurve, ParabolaToBSplineCurve).
    These algorithms all work on 2D curves from the gp
    package and compute all the data needed to construct a
    BSpline curve equivalent to the conic curve. This data consists of:
    -   the degree of the curve,
    -   the periodic characteristics of the curve,
    -   a poles table with associated weights,
    -   a knots table with associated multiplicities.
    The abstract class ConicToBSplineCurve provides a
    framework for storing and consulting this computed data.
    """

    def Degree(self) -> int:
        """
        Returns the degree of the BSpline curve whose data is
        computed in this framework.
        """

    def NbPoles(self) -> int:
        """
        Returns the number of poles of the BSpline curve whose
        data is computed in this framework.
        """

    def NbKnots(self) -> int:
        """
        Returns the number of knots of the BSpline curve whose
        data is computed in this framework.
        """

    def IsPeriodic(self) -> bool:
        """
        Returns true if the BSpline curve whose data is computed in
        this framework is periodic.
        """

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns the poles of the BSpline curve."""

    def Weights(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the weights of the BSpline curve."""

    def Knots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the knots of the BSpline curve."""

    def Multiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns the multiplicities of the BSpline curve."""

class Convert_CircleToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a circle into a rational B-spline curve.
    The circle is a Circ2d from package gp and its parametrization is :
    P (U) = Loc + R * (std::cos(U) * Xdir + std::sin(U) * YDir) where Loc is the
    center of the circle Xdir and Ydir are the normalized directions
    of the local cartesian coordinate system of the circle.
    The parametrization range for the circle is U [0, 2Pi].

    Warnings :
    The parametrization range for the B-spline curve is not [0, 2Pi].

    KeyWords :
    Convert, Circle, BSplineCurve, 2D .
    """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, Parameterisation: Convert_ParameterisationType = ...) -> None:
        """
        The equivalent B-spline curve has the same orientation
        as the circle C.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, U1: float, U2: float, Parameterisation: Convert_ParameterisationType = ...) -> None:
        """
        The circle C is limited between the parametric values U1, U2
        in radians. U1 and U2 [0.0, 2*Pi] .
        The equivalent B-spline curve is oriented from U1 to U2 and has
        the same orientation as the circle C.

        Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        """

class Convert_CompPolynomialToPoles:
    """
    Convert a serie of Polynomial N-Dimensional Curves
    that are have continuity CM to an N-Dimensional Bspline Curve
    that has continuity CM.
    (to convert an function (curve) polynomial by span in a BSpline)
    This class uses the following arguments :
    NumCurves :  the number of Polynomial Curves
    Continuity:  the requested continuity for the n-dimensional Spline
    Dimension :  the dimension of the Spline
    MaxDegree :  maximum allowed degree for each composite
    polynomial segment.
    NumCoeffPerCurve : the number of coefficient per segments = degree - 1
    Coefficients  :  the coefficients organized in the following way
    [1..<myNumPolynomials>][1..myMaxDegree +1][1..myDimension]
    that is : index [n,d,i] is at slot
    (n-1) * (myMaxDegree + 1) * myDimension + (d-1) * myDimension + i
    PolynomialIntervals :  nth polynomial represents a polynomial between
    myPolynomialIntervals->Value(n,0) and
    myPolynomialIntervals->Value(n,1)
    TrueIntervals : the nth polynomial has to be mapped linearly to be
    defined on the following interval :
    myTrueIntervals->Value(n) and myTrueIntervals->Value(n+1)
    so that it adequately represents the function with the
    required continuity
    """

    @overload
    def __init__(self, Dimension: int, MaxDegree: int, Degree: int, Coefficients: nanoocp.NCollection.NCollection_Array1[float], PolynomialIntervals: nanoocp.NCollection.NCollection_Array1[float], TrueIntervals: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """To Convert only one span."""

    @overload
    def __init__(self, NumCurves: int, Continuity: int, Dimension: int, MaxDegree: int, NumCoeffPerCurve: nanoocp.NCollection.NCollection_HArray1[int], Coefficients: nanoocp.NCollection.NCollection_HArray1[float], PolynomialIntervals: nanoocp.NCollection.NCollection_HArray2[float], TrueIntervals: nanoocp.NCollection.NCollection_HArray1[float]) -> None:
        """
        Warning!
        Continuity can be at MOST the maximum degree of
        the polynomial functions
        TrueIntervals :
        this is the true parameterisation for the composite curve
        that is : the curve has myContinuity if the nth curve
        is parameterized between myTrueIntervals(n) and myTrueIntervals(n+1)

        Coefficients have to be the implicit "c form":
        Coefficients[Numcurves][MaxDegree+1][Dimension]

        Warning!
        The NumberOfCoefficient of an polynome is his degree + 1
        Example: To convert the linear function f(x) = 2*x + 1 on the
        domaine [2,5] to BSpline with the bound [-1,1]. Arguments are :
        NumCurves  = 1;
        Continuity = 1;
        Dimension  = 1;
        MaxDegree  = 1;
        NumCoeffPerCurve [1] = {2};
        Coefficients[2] = {1, 2};
        PolynomialIntervals[1,2] = {{2,5}}
        TrueIntervals[2] = {-1, 1}
        """

    @overload
    def __init__(self, NumCurves: int, Dimension: int, MaxDegree: int, Continuity: nanoocp.NCollection.NCollection_Array1[int], NumCoeffPerCurve: nanoocp.NCollection.NCollection_Array1[int], Coefficients: nanoocp.NCollection.NCollection_Array1[float], PolynomialIntervals: nanoocp.NCollection.NCollection_Array2[float], TrueIntervals: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        To Convert several span with different order of Continuity.
        Warning: The Length of Continuity have to be NumCurves-1
        """

    def NbPoles(self) -> int:
        """Returns the number of poles of the n-dimensional BSpline."""

    def Poles(self) -> nanoocp.NCollection.NCollection_Array2[float]:
        """
        Returns the poles of the n-dimensional BSpline
        in the following format:
        [1..NumPoles][1..Dimension]
        """

    def Degree(self) -> int:
        """Returns the degree of the n-dimensional BSpline."""

    def NbKnots(self) -> int:
        """Returns the number of knots of the n-dimensional BSpline."""

    def Knots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the knots of the n-dimensional BSpline."""

    def Multiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns the multiplicities of the knots in the BSpline."""

    def IsDone(self) -> bool:
        """Returns true if the conversion was successful."""

class Convert_ElementarySurfaceToBSplineSurface:
    """
    Root class for algorithms which convert an elementary
    surface (cylinder, cone, sphere or torus) into a BSpline surface.
    These algorithms all work on elementary surfaces from
    the gp package and compute all the data needed to
    construct a BSpline surface equivalent to the cylinder,
    cone, sphere or torus.
    """

    def UDegree(self) -> int:
        """Returns the degree in the U parametric direction."""

    def VDegree(self) -> int:
        """Returns the degree in the V parametric direction."""

    def NbUPoles(self) -> int:
        """Returns the number of poles in the U parametric direction."""

    def NbVPoles(self) -> int:
        """Returns the number of poles in the V parametric direction."""

    def NbUKnots(self) -> int:
        """Returns the number of knots in the U parametric direction."""

    def NbVKnots(self) -> int:
        """Returns the number of knots in the V parametric direction."""

    def IsUPeriodic(self) -> bool:
        """Returns true if the surface is periodic in the U parametric direction."""

    def IsVPeriodic(self) -> bool:
        """Returns true if the surface is periodic in the V parametric direction."""

    def Poles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """Returns the poles of the BSpline surface."""

    def Weights(self) -> nanoocp.NCollection.NCollection_Array2[float]:
        """Returns the weights of the BSpline surface."""

    def UKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the U-knots of the BSpline surface."""

    def VKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the V-knots of the BSpline surface."""

    def UMultiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns the U-multiplicities of the BSpline surface."""

    def VMultiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns the V-multiplicities of the BSpline surface."""

class Convert_ConeToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded Cone into a rational
    B-spline surface.
    The cone a Cone from package gp. Its parametrization is:
    P (U, V) = Loc + V * Zdir +
    (R + V*Tan(Ang)) * (std::cos(U)*Xdir + std::sin(U)*Ydir)
    where Loc is the location point of the cone, Xdir, Ydir and Zdir
    are the normalized directions of the local cartesian coordinate
    system of the cone (Zdir is the direction of the Cone's axis),
    Ang is the cone semi-angle. The U parametrization range is
    [0, 2PI].
    KeyWords :
    Convert, Cone, BSplineSurface.
    """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, V1: float, V2: float) -> None:
        """
        The equivalent B-spline surface as the same orientation as the
        Cone in the U and V parametric directions.

        Raised if V1 = V2.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, U1: float, U2: float, V1: float, V2: float) -> None:
        """
        The equivalent B-spline surface as the same orientation as the
        Cone in the U and V parametric directions.

        Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        Raised if V1 = V2.
        """

class Convert_CylinderToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded cylinder into a rational
    B-spline surface. The cylinder is a Cylinder from package gp.
    The parametrization of the cylinder is:
    P (U, V) = Loc + V * Zdir + Radius * (Xdir*std::cos(U) + Ydir*Sin(U))
    where Loc is the location point of the cylinder, Xdir, Ydir and
    Zdir are the normalized directions of the local cartesian
    coordinate system of the cylinder (Zdir is the direction of the
    cylinder's axis). The U parametrization range is U [0, 2PI].
    KeyWords :
    Convert, Cylinder, BSplineSurface.
    """

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, V1: float, V2: float) -> None:
        """
        The equivalent B-splineSurface as the same orientation as the
        cylinder in the U and V parametric directions.

        Raised if V1 = V2.
        """

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, U1: float, U2: float, V1: float, V2: float) -> None:
        """
        The equivalent B-splineSurface as the same orientation as the
        cylinder in the U and V parametric directions.

        Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        Raised if V1 = V2.
        """

class Convert_EllipseToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a ellipse into a rational B-spline curve.
    The ellipse is represented an Elips2d from package gp with
    the parametrization :
    P (U) =
    Loc + (MajorRadius * std::cos(U) * Xdir + MinorRadius * std::sin(U) * Ydir)
    where Loc is the center of the ellipse, Xdir and Ydir are the
    normalized directions of the local cartesian coordinate system of
    the ellipse. The parametrization range is U [0, 2PI].
    KeyWords :
    Convert, Ellipse, BSplineCurve, 2D .
    """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, Parameterisation: Convert_ParameterisationType = ...) -> None:
        """
        The equivalent B-spline curve has the same orientation
        as the ellipse E.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, U1: float, U2: float, Parameterisation: Convert_ParameterisationType = ...) -> None:
        """
        The ellipse E is limited between the parametric values U1, U2.
        The equivalent B-spline curve is oriented from U1 to U2 and has
        the same orientation as E.

        Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        """

class Convert_GridPolynomialToPoles:
    """
    Convert a grid of Polynomial Surfaces
    that are have continuity CM to an
    Bspline Surface that has continuity
    CM
    """

    @overload
    def __init__(self, theMaxUDegree: int, theMaxVDegree: int, theNumCoeff: nanoocp.NCollection.NCollection_Array1[int], theCoefficients: nanoocp.NCollection.NCollection_Array1[float], thePolynomialUIntervals: nanoocp.NCollection.NCollection_Array1[float], thePolynomialVIntervals: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        To only one polynomial Surface.
        The Length of <PolynomialUIntervals> and <PolynomialVIntervals>
        have to be 2.
        This values defined the parametric domain of the Polynomial Equation.

        Coefficients:
        The <Coefficients> have to be formatted than an "C array"
        [MaxUDegree+1] [MaxVDegree+1] [3]
        """

    @overload
    def __init__(self, theMaxUDegree: int, theMaxVDegree: int, theNumCoeff: nanoocp.NCollection.NCollection_HArray1[int], theCoefficients: nanoocp.NCollection.NCollection_HArray1[float], thePolynomialUIntervals: nanoocp.NCollection.NCollection_HArray1[float], thePolynomialVIntervals: nanoocp.NCollection.NCollection_HArray1[float]) -> None:
        """
        Handle-based overload (delegates to the array-based constructor).
        Provided for backward compatibility; new code should prefer the
        @c NCollection_Array1 form which avoids unnecessary heap allocation.
        """

    @overload
    def __init__(self, theNbUSurfaces: int, theNbVSurfaces: int, theUContinuity: int, theVContinuity: int, theMaxUDegree: int, theMaxVDegree: int, theNumCoeffPerSurface: nanoocp.NCollection.NCollection_Array2[int], theCoefficients: nanoocp.NCollection.NCollection_Array1[float], thePolynomialUIntervals: nanoocp.NCollection.NCollection_Array1[float], thePolynomialVIntervals: nanoocp.NCollection.NCollection_Array1[float], theTrueUIntervals: nanoocp.NCollection.NCollection_Array1[float], theTrueVIntervals: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        To one grid of polynomial Surface.
        Warning!
        Continuity in each parametric direction can be at MOST the
        maximum degree of the polynomial functions.

        <TrueUIntervals>, <TrueVIntervals> :
        this is the true parameterisation for the composite surface

        Coefficients:
        The Coefficients have to be formatted than an "C array"
        [NbVSurfaces] [NBUSurfaces] [MaxUDegree+1] [MaxVDegree+1] [3]
        raises DomainError if <NumCoeffPerSurface> is not a
        [1, NbVSurfaces*NbUSurfaces, 1,2] array.
        if <Coefficients> is not a
        """

    @overload
    def __init__(self, theNbUSurfaces: int, theNbVSurfaces: int, theUContinuity: int, theVContinuity: int, theMaxUDegree: int, theMaxVDegree: int, theNumCoeffPerSurface: nanoocp.NCollection.NCollection_HArray2[int], theCoefficients: nanoocp.NCollection.NCollection_HArray1[float], thePolynomialUIntervals: nanoocp.NCollection.NCollection_HArray1[float], thePolynomialVIntervals: nanoocp.NCollection.NCollection_HArray1[float], theTrueUIntervals: nanoocp.NCollection.NCollection_HArray1[float], theTrueVIntervals: nanoocp.NCollection.NCollection_HArray1[float]) -> None:
        """Handle-based overload (delegates to the array-based constructor)."""

    def NbUPoles(self) -> int:
        """Returns the number of poles in the U parametric direction."""

    def NbVPoles(self) -> int:
        """Returns the number of poles in the V parametric direction."""

    def Poles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """Returns the poles of the BSpline Surface."""

    def UDegree(self) -> int:
        """Returns the degree in the U parametric direction."""

    def VDegree(self) -> int:
        """Returns the degree in the V parametric direction."""

    def NbUKnots(self) -> int:
        """Returns the number of knots in the U parametric direction."""

    def NbVKnots(self) -> int:
        """Returns the number of knots in the V parametric direction."""

    def UKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the knots in the U direction."""

    def VKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the knots in the V direction."""

    def UMultiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns the multiplicities of the knots in the U direction."""

    def VMultiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns the multiplicities of the knots in the V direction."""

    def IsDone(self) -> bool:
        """Returns true if the conversion was successful."""

class Convert_HyperbolaToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a hyperbola into a rational B-spline curve.
    The hyperbola is an Hypr2d from package gp with the
    parametrization :
    P (U) =
    Loc + (MajorRadius * std::cosh(U) * Xdir + MinorRadius * std::sinh(U) * Ydir)
    where Loc is the location point of the hyperbola, Xdir and Ydir are
    the normalized directions of the local cartesian coordinate system
    of the hyperbola.
    KeyWords :
    Convert, Hyperbola, BSplineCurve, 2D .
    """

    def __init__(self, H: nanoocp.gp.gp_Hypr2d, U1: float, U2: float) -> None:
        """
        The hyperbola H is limited between the parametric values U1, U2
        and the equivalent B-spline curve has the same orientation as the
        hyperbola.
        """

class Convert_ParabolaToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a parabola into a non rational B-spline
    curve.
    The parabola is a Parab2d from package gp with the parametrization
    P (U) = Loc + F * (U*U * Xdir + 2 * U * Ydir) where Loc is the
    apex of the parabola, Xdir is the normalized direction of the
    symmetry axis of the parabola, Ydir is the normalized direction of
    the directrix and F is the focal length.
    KeyWords :
    Convert, Parabola, BSplineCurve, 2D .
    """

    def __init__(self, Prb: nanoocp.gp.gp_Parab2d, U1: float, U2: float) -> None:
        """
        The parabola Prb is limited between the parametric values U1, U2
        and the equivalent B-spline curve as the same orientation as the
        parabola Prb.
        """

class Convert_SphereToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded Sphere into a rational
    B-spline surface. The sphere is a Sphere from package gp.
    The parametrization of the sphere is:
    P (U, V) = Loc + Radius * std::sin(V) * Zdir +
    Radius * std::cos(V) * (std::cos(U)*Xdir + std::sin(U)*Ydir)
    where Loc is the center of the sphere Xdir, Ydir and Zdir are the
    normalized directions of the local cartesian coordinate system of
    the sphere. The parametrization range is U [0, 2PI] and
    V [-PI/2, PI/2].
    KeyWords :
    Convert, Sphere, BSplineSurface.
    """

    @overload
    def __init__(self, Sph: nanoocp.gp.gp_Sphere) -> None:
        """
        The equivalent B-spline surface as the same orientation
        as the sphere in the U and V parametric directions.
        """

    @overload
    def __init__(self, Sph: nanoocp.gp.gp_Sphere, Param1: float, Param2: float, UTrim: bool = True) -> None:
        """
        The equivalent B-spline surface as the same orientation
        as the sphere in the U and V parametric directions.

        Raised if UTrim = True and Param1 = Param2 or
        Param1 = Param2 + 2.0 * Pi
        Raised if UTrim = False and Param1 = Param2
        """

    @overload
    def __init__(self, Sph: nanoocp.gp.gp_Sphere, U1: float, U2: float, V1: float, V2: float) -> None:
        """
        The equivalent B-spline surface as the same orientation as the
        sphere in the U and V parametric directions.

        Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        Raised if V1 = V2.
        """

class Convert_TorusToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded Torus into a rational
    B-spline surface. The torus is a Torus from package gp.
    The parametrization of the torus is :
    P (U, V) =
    Loc + MinorRadius * std::sin(V) * Zdir +
    (MajorRadius+MinorRadius*std::cos(V)) * (std::cos(U)*Xdir + std::sin(U)*Ydir)
    where Loc is the center of the torus, Xdir, Ydir and Zdir are the
    normalized directions of the local cartesian coordinate system of
    the Torus. The parametrization range is U [0, 2PI], V [0, 2PI].
    KeyWords :
    Convert, Torus, BSplineSurface.
    """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Torus) -> None:
        """
        The equivalent B-spline surface as the same orientation as the
        torus in the U and V parametric directions.
        """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Torus, Param1: float, Param2: float, UTrim: bool = True) -> None:
        """
        The equivalent B-spline surface as the same orientation as the
        torus in the U and V parametric directions.

        Raised if Param1 = Param2 or Param1 = Param2 + 2.0 * Pi
        """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Torus, U1: float, U2: float, V1: float, V2: float) -> None:
        """
        The equivalent B-spline surface as the same orientation as the
        torus in the U and V parametric directions.

        Raised if U1 = U2 or U1 = U2 + 2.0 * Pi
        Raised if V1 = V2 or V1 = V2 + 2.0 * Pi
        """

def BuildPolynomialCosAndSin(theUFirst: float, theULast: float, theNumPoles: int, theCosNumerator: nanoocp.NCollection.NCollection_Array1[float], theSinNumerator: nanoocp.NCollection.NCollection_Array1[float], theDenominator: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...
