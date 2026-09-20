"""OCCT package CPnts (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.gp
import nanoocp.math


class CPnts_MyGaussFunction(nanoocp.math.math_Function):
    """for implementation, compute values for Gauss"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CPnts_MyGaussFunction) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]: ...

class CPnts_MyRootFunction(nanoocp.math.math_FunctionWithDerivative):
    """
    Implements a function for the Newton algorithm to find the
    solution of Integral(F) = L
    (compute Length and Derivative of the curve for Newton)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CPnts_MyRootFunction) -> None: ...

    @overload
    def Init(self, X0: float, L: float) -> None:
        """We want to solve Integral(X0,X,F(X,D)) = L"""

    @overload
    def Init(self, X0: float, L: float, Tol: float) -> None:
        """
        We want to solve Integral(X0,X,F(X,D)) = L
        with given tolerance
        """

    def Value(self, X: float) -> tuple[bool, float]:
        """This is Integral(X0,X,F(X,D)) - L"""

    def Derivative(self, X: float) -> tuple[bool, float]:
        """This is F(X,D)"""

    def Values(self, X: float) -> tuple[bool, float, float]: ...

class CPnts_AbscissaPoint:
    """
    the algorithm computes a point on a curve at a given
    distance from another point on the curve

    We can instantiates with
    Curve from Adaptor3d, Pnt from gp, Vec from gp

    or
    Curve2d from Adaptor2d, Pnt2d from gp, Vec2d from gp
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Abscissa: float, U0: float, Resolution: float) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Abscissa: float, U0: float, Resolution: float) -> None:
        """
        the algorithm computes a point on a curve <Curve> at the
        distance <Abscissa> from the point of parameter <U0>.
        <Resolution> is the error allowed in the computation.
        The computed point can be outside of the curve 's bounds.
        """

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None:
        """
        the algorithm computes a point on a curve <Curve> at the
        distance <Abscissa> from the point of parameter <U0>.
        <Ui> is the starting value used in the iterative process
        which find the solution, it must be closed to the final
        solution
        <Resolution> is the error allowed in the computation.
        The computed point can be outside of the curve 's bounds.
        """

    @overload
    def __init__(self, theOther: CPnts_AbscissaPoint) -> None: ...

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> float: ...

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float:
        """Computes the length of the Curve <C>."""

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor3d.Adaptor3d_Curve, Tol: float) -> float: ...

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Tol: float) -> float:
        """Computes the length of the Curve <C> with the given tolerance."""

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float) -> float: ...

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float) -> float:
        """Computes the length of the Curve <C> between <U1> and <U2>."""

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, Tol: float) -> float:
        """
        Computes the length of the Curve <C> between <U1> and <U2> with the given tolerance.
        """

    @overload
    @staticmethod
    def Length(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float, Tol: float) -> float:
        """
        Computes the length of the Curve <C> between <U1> and <U2> with the given tolerance.
        creation of a indefinite AbscissaPoint.
        """

    @overload
    def Init(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None: ...

    @overload
    def Init(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Tol: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Tol: float) -> None:
        """Initializes the resolution function with <C>."""

    @overload
    def Init(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, Tol: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float, Tol: float) -> None:
        """
        Initializes the resolution function with <C>
        between U1 and U2.
        """

    @overload
    def Perform(self, Abscissa: float, U0: float, Resolution: float) -> None:
        """
        Computes the point at the distance <Abscissa> of
        the curve.
        U0 is the parameter of the point from which the distance
        is measured.
        """

    @overload
    def Perform(self, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None:
        """
        Computes the point at the distance <Abscissa> of
        the curve.
        U0 is the parameter of the point from which the distance
        is measured and Ui is the starting value for the iterative
        process (should be close to the final solution).
        """

    def AdvPerform(self, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None:
        """
        Computes the point at the distance <Abscissa> of
        the curve; performs more appropriate tolerance management;
        to use this method in right way it is necessary to call
        empty constructor. then call method Init with
        Tolerance = Resolution, then call AdvPermorm.
        U0 is the parameter of the point from which the distance
        is measured and Ui is the starting value for the iterative
        process (should be close to the final solution).
        """

    def IsDone(self) -> bool:
        """True if the computation was successful, False otherwise."""

    def Parameter(self) -> float:
        """Returns the parameter of the solution."""

    def SetParameter(self, P: float) -> None:
        """Enforce the solution, used by GCPnts."""

class CPnts_UniformDeflection:
    """
    This class defines an algorithm to create a set of points
    (with a given chordal deviation) at the
    positions of constant deflection of a given parametrized curve or a trimmed
    circle.
    The continuity of the curve must be at least C2.

    the usage of the is the following.

    class myUniformDFeflection instantiates
    UniformDeflection(Curve, Tool);

    Curve C; // Curve inherits from Curve or Curve2d from Adaptor2d
    myUniformDeflection Iter1;
    DefPntOfmyUniformDeflection P;

    for(Iter1.Initialize(C, Deflection, EPSILON, True);
    Iter1.More();
    Iter1.Next()) {
    P = Iter1.Value();
    ... make something with P
    }
    if(!Iter1.IsAllDone()) {
    ... something wrong happened
    }
    """

    @overload
    def __init__(self) -> None:
        """creation of a indefinite UniformDeflection"""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Deflection: float, Resolution: float, WithControl: bool) -> None:
        """
        Computes a uniform deflection distribution of points
        on the curve <C>.
        <Deflection> defines the constant deflection value.
        The algorithm computes the number of points and the points.
        The curve <C> must be at least C2 else the computation can fail.
        If just some parts of the curve is C2 it is better to give the
        parameters bounds and to use the below constructor .
        if <WithControl> is True, the algorithm controls the estimate
        deflection
        when the curve is singular at the point P(u),the algorithm
        computes the next point as
        P(u + std::max(CurrentStep,std::abs(LastParameter-FirstParameter)))
        if the singularity is at the first point ,the next point
        calculated is the P(LastParameter)
        """

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Deflection: float, Resolution: float, WithControl: bool) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None:
        """
        Computes an uniform deflection distribution of points on a part of
        the curve <C>. Deflection defines the step between the points.
        <U1> and <U2> define the distribution span.
        <U1> and <U2> must be in the parametric range of the curve.
        """

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None:
        """As above with 2d curve"""

    @overload
    def __init__(self, theOther: CPnts_UniformDeflection) -> None: ...

    @overload
    def Initialize(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Deflection: float, Resolution: float, WithControl: bool) -> None: ...

    @overload
    def Initialize(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Deflection: float, Resolution: float, WithControl: bool) -> None:
        """
        Initialize the algorithms with <C>, <Deflection>, <UStep>,
        <Resolution> and <WithControl>
        """

    @overload
    def Initialize(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None: ...

    @overload
    def Initialize(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None:
        """
        Initialize the algorithms with <C>, <Deflection>, <UStep>,
        <U1>, <U2> and <WithControl>
        """

    def IsAllDone(self) -> bool:
        """
        To know if all the calculus were done successfully
        (ie all the points have been computed). The calculus can fail if
        the Curve is not C1 in the considered domain.
        Returns True if the calculus was successful.
        """

    def Next(self) -> None:
        """go to the next Point."""

    def More(self) -> bool:
        """returns True if it exists a next Point."""

    def Value(self) -> float:
        """return the computed parameter"""

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """return the computed parameter"""
