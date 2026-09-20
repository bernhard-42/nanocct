"""OCCT package IntAna2d (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.gp


class IntAna2d_IntPoint:
    """Geometrical intersection between two 2d elements."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, X: float, Y: float, U1: float) -> None:
        """
        Create an intersection point between a parametric 2d line,
        and a line given by an implicit equation (ImplicitCurve).
        X,Y are the coordinate of the point. U1 is the parameter
        on the parametric element.
        Empty constructor. It's necessary to use one of
        the SetValue method after this one.
        """

    @overload
    def __init__(self, X: float, Y: float, U1: float, U2: float) -> None:
        """
        Create an intersection point between 2 parametric 2d lines.
        X,Y are the coordinate of the point. U1 is the parameter
        on the first element, U2 the parameter on the second one.
        """

    @overload
    def SetValue(self, X: float, Y: float, U1: float, U2: float) -> None:
        """Set the values for a "non-implicit" point."""

    @overload
    def SetValue(self, X: float, Y: float, U1: float) -> None:
        """Set the values for an "implicit" point."""

    def Value(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the geometric point."""

    def SecondIsImplicit(self) -> bool:
        """Returns True if the second curve is implicit."""

    def ParamOnFirst(self) -> float:
        """Returns the parameter on the first element."""

    def ParamOnSecond(self) -> float:
        """
        Returns the parameter on the second element.
        If the second element is an implicit curve, an exception
        is raised.
        """

class IntAna2d_AnaIntersection:
    """
    Implementation of the analytical intersection between:
    - two Lin2d,
    - two Circ2d,
    - a Lin2d and a Circ2d,
    - an element of gp (Lin2d, Circ2d, Elips2d, Parab2d, Hypr2d)
    and another conic.
    No tolerance is given for all the intersections: the tolerance
    will be the "precision machine".
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. IsDone returns False."""

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, L2: nanoocp.gp.gp_Lin2d) -> None:
        """Intersection between two lines."""

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Circ2d) -> None:
        """Intersection between two circles."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, C: nanoocp.gp.gp_Circ2d) -> None:
        """Intersection between a line and a circle."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, C: IntAna2d_Conic) -> None:
        """Intersection between a line and a conic."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, Co: IntAna2d_Conic) -> None:
        """Intersection between a circle and another conic."""

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, C: IntAna2d_Conic) -> None:
        """Intersection between an ellipse and another conic."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab2d, C: IntAna2d_Conic) -> None:
        """Intersection between a parabola and another conic."""

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr2d, C: IntAna2d_Conic) -> None:
        """Intersection between an hyperbola and another conic."""

    @overload
    def Perform(self, L1: nanoocp.gp.gp_Lin2d, L2: nanoocp.gp.gp_Lin2d) -> None:
        """Intersection between two lines."""

    @overload
    def Perform(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Circ2d) -> None:
        """Intersection between two circles."""

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, C: nanoocp.gp.gp_Circ2d) -> None:
        """Intersection between a line and a circle."""

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, C: IntAna2d_Conic) -> None:
        """Intersection between a line and a conic."""

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ2d, Co: IntAna2d_Conic) -> None:
        """Intersection between a circle and another conic."""

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips2d, C: IntAna2d_Conic) -> None:
        """Intersection between an ellipse and another conic."""

    @overload
    def Perform(self, P: nanoocp.gp.gp_Parab2d, C: IntAna2d_Conic) -> None:
        """Intersection between a parabola and another conic."""

    @overload
    def Perform(self, H: nanoocp.gp.gp_Hypr2d, C: IntAna2d_Conic) -> None:
        """Intersection between an hyperbola and another conic."""

    def IsDone(self) -> bool:
        """Returns TRUE if the computation was successful."""

    def IsEmpty(self) -> bool:
        """
        Returns TRUE when there is no intersection, i-e
        - no intersection point
        - the elements are not identical.
        The element may be parallel in this case.
        """

    def IdenticalElements(self) -> bool:
        """
        For the intersection between an element of gp and a conic
        known by an implicit equation, the result will be TRUE
        if the element of gp verifies the implicit equation.
        For the intersection between two Lin2d or two Circ2d, the
        result will be TRUE if the elements are identical.
        The function returns FALSE in all the other cases.
        """

    def ParallelElements(self) -> bool:
        """
        For the intersection between two Lin2d or two Circ2d,
        the function returns TRUE if the elements are parallel.
        The function returns FALSE in all the other cases.
        """

    def NbPoints(self) -> int:
        """returns the number of IntPoint between the 2 curves."""

    def Point(self, N: int) -> IntAna2d_IntPoint:
        """
        returns the intersection point of range N;
        If (N<=0) or (N>NbPoints), an exception is raised.
        """

class IntAna2d_Conic:
    """
    Definition of a conic by its implicit quadaratic equation:
    A.X**2 + B.Y**2 + 2.C.X*Y + 2.D.X + 2.E.Y + F = 0.
    """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin2d) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Parab2d) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Hypr2d) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Elips2d) -> None: ...

    def Value(self, X: float, Y: float) -> float:
        """value of the function F at the point X,Y."""

    def Grad(self, X: float, Y: float) -> nanoocp.gp.gp_XY:
        """returns the value of the gradient of F at the point X,Y."""

    def ValAndGrad(self, X: float, Y: float, Grd: nanoocp.gp.gp_XY) -> float:
        """
        Returns the value of the function and its gradient at
        the point X,Y.
        """

    def Coefficients(self) -> tuple[float, float, float, float, float, float]:
        """
        returns the coefficients of the polynomial equation
        which defines the conic:
        A.X**2 + B.Y**2 + 2.C.X*Y + 2.D.X + 2.E.Y + F = 0.
        """

    def NewCoefficients(self, Axis: nanoocp.gp.gp_Ax2d) -> tuple[float, float, float, float, float, float]:
        """
        Returns the coefficients of the polynomial equation
        ( written in the natural coordinates system )
        A x x + B y y + 2 C x y + 2 D x + 2 E y + F
        in the local coordinates system defined by Axis
        """

class MyDirectPolynomialRoots:
    @overload
    def __init__(self, A2: float, A1: float, A0: float) -> None: ...

    @overload
    def __init__(self, A4: float, A3: float, A2: float, A1: float, A0: float) -> None: ...

    def NbSolutions(self) -> int: ...

    def Value(self, i: int) -> float: ...

    def IsDone(self) -> float: ...

    def InfiniteRoots(self) -> bool: ...

def Points_Confondus(xa: float, ya: float, xb: float, yb: float) -> bool: ...

def Traitement_Points_Confondus(pts: IntAna2d_IntPoint) -> int: ...

def Coord_Ancien_Repere(Axe_Nouveau_Repere: nanoocp.gp.gp_Ax2d) -> tuple[float, float]: ...
