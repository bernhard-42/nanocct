"""OCCT package GccAna (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.GccEnt
import nanoocp.GccInt
import nanoocp.Standard
import nanoocp.gp


class GccAna_Circ2d2TanOn:
    """
    Describes functions for building a 2D circle
    -   tangential to 2 curves, or
    -   tangential to a curve and passing through a point, or
    -   passing through 2 points,
    and with its center on a curve. For these analytic
    algorithms, curves are circles or lines.
    A Circ2d2TanOn object provides a framework for:
    -   defining the construction of 2D circles(s),
    -   implementing the construction algorithm, and
    -   consulting the result(s).
    """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, OnLine: nanoocp.gp.gp_Lin2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d circles and
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, OnLine: nanoocp.gp.gp_Lin2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a 2d line
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, OnLine: nanoocp.gp.gp_Lin2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d lines
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Point2: nanoocp.gp.gp_Pnt2d, OnLine: nanoocp.gp.gp_Lin2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a point
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Point2: nanoocp.gp.gp_Pnt2d, OnLine: nanoocp.gp.gp_Lin2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a point
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, OnLine: nanoocp.gp.gp_Lin2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two points
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, OnCirc: nanoocp.gp.gp_Circ2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d circles and
        having the center ON a 2d circle.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, OnCirc: nanoocp.gp.gp_Circ2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a circle and a line
        having the center ON a 2d circle.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Point2: nanoocp.gp.gp_Pnt2d, OnCirc: nanoocp.gp.gp_Circ2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a circle and a point
        having the center ON a 2d circle.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, OnCirc: nanoocp.gp.gp_Circ2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d lines
        having the center ON a 2d circle.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Point2: nanoocp.gp.gp_Pnt2d, OnCirc: nanoocp.gp.gp_Circ2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a line and a point
        having the center ON a 2d circle.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, OnCirc: nanoocp.gp.gp_Circ2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to create
        2d circles TANgent to two points having the center ON
        a 2d circle.
        """

    @overload
    def __init__(self, theOther: GccAna_Circ2d2TanOn) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction algorithm does not fail
        (even if it finds no solution).
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of circles, representing solutions
        computed by this algorithm.
        Exceptions
        StdFail_NotDone if the construction fails.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the context
        of the algorithm-object.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        Returns the qualifiers Qualif1 and Qualif2 of the
        tangency arguments for the solution of index Index
        computed by this algorithm.
        The returned qualifiers are:
        -   those specified at the start of construction when the
        solutions are defined as enclosed, enclosing or
        outside with respect to the arguments, or
        -   those computed during construction (i.e. enclosed,
        enclosing or outside) when the solutions are defined
        as unqualified with respect to the arguments, or
        -   GccEnt_noqualifier if the tangency argument is a point.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns the information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution
        ParArg is the intrinsic parameter of the point PntSol on
        the first argument. Raises OutOfRange if Index is greater than the number
        of solutions and NotDone if IsDone returns false.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns the information about the tangency point between the
        result number Index and the second argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution.
        ParArg is the intrinsic parameter of the point PntSol on
        the second argument. Raises OutOfRange if Index is greater than the number
        of solutions and NotDone if IsDone returns false.
        """

    def CenterOn3(self, Index: int, PntArg: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Returns the information about the center (on the curv) of
        the result number Index and the third argument.
        ParArg is the intrinsic parameter of the point PntArg on
        the third argument.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        True if the solution and the first argument are the same
        (2 circles).
        If R1 is the radius of the first argument and Rsol the radius
        of the solution and dist the distance between the two centers,
        we consider the two circles are identical if R1+dist-Rsol is
        less than Tolerance.
        False in the other cases.
        Raises OutOfRange if Index is greater than the number
        of solutions and NotDone if IsDone returns false.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        True if the solution and the second argument are the same
        (2 circles).
        If R2 is the radius of the second argument and Rsol the radius
        of the solution and dist the distance between the two centers,
        we consider the two circles are identical if R2+dist-Rsol is
        less than Tolerance.
        False in the other cases.
        Raises OutOfRange if Index is greater than the number
        of solutions and NotDone if IsDone returns false.
        """

class GccAna_Circ2d2TanRad:
    """
    This class implements the algorithms used to
    create 2d circles tangent to 2
    points/lines/circles and with a given radius.
    For each construction methods arguments are:
    - Two Qualified elements for tangency constraints.
    (for example EnclosedCirc if we want the
    solution inside the argument EnclosedCirc).
    - Two Reals. One (Radius) for the radius and the
    other (Tolerance) for the tolerance.
    Tolerance is only used for the limit cases.
    For example :
    We want to create a circle inside a circle C1 and
    inside a circle C2 with a radius Radius and a
    tolerance Tolerance.
    If we do not use Tolerance it is impossible to
    find a solution in the following case : C2 is
    inside C1 and there is no intersection point
    between the two circles.
    With Tolerance it gives a solution if the lowest
    distance between C1 and C2 is lower than or equal
    Tolerance.
    """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d circle with a
        radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a 2d line
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Point2: nanoocp.gp.gp_Pnt2d, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a point
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Point2: nanoocp.gp.gp_Pnt2d, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a point
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d lines
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles passing through two points with a
        radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, theOther: GccAna_Circ2d2TanRad) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the algorithm succeeded.
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of circles, representing solutions computed by this algorithm.
        Exceptions
        StdFail_NotDone if the construction fails. of solutions.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the context
        of the algorithm-object. Raises OutOfRange exception if Index is greater
        than the number of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        Returns the information about the qualifiers of
        the tangency arguments concerning the solution number Index.
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computedin case of unqualified).
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution.
        ParArg is the intrinsic parameter of the point PntSol on the first
        argument. Raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not succeed
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the second argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution.
        ParArg is the intrinsic parameter of the point PntArg on
        the second argument. Raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not succeed.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument. Raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the second argument. Raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not succeed.
        """

class GccAna_Circ2d3Tan:
    """
    This class implements the algorithms used to
    create 2d circles tangent to 3 points/lines/circles.
    The arguments of all construction methods are :
    - The three qualified elements for the
    tangency constraints (QualifiedCirc, QualifiedLine,
    Points).
    - A real Tolerance.
    Tolerance is only used in the limit cases.
    For example :
    We want to create a circle tangent to an UnqualifiedCirc
    C1 and an UnqualifiedCirc C2 and an UnqualifiedCirc C3
    with a tolerance Tolerance.
    If we do not use Tolerance it is impossible to find
    a solution in the following case : C2 is inside C1
    and there is no intersection point between the two
    circles, and C3 is completely outside C1.
    With Tolerance we will find a solution if the
    lowest distance between C1 and C2 is lower than or
    equal Tolerance.
    """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified3: nanoocp.GccEnt.GccEnt_QualifiedCirc, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 3 circles.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified3: nanoocp.GccEnt.GccEnt_QualifiedLin, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 2 circles and 1 line.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified3: nanoocp.GccEnt.GccEnt_QualifiedLin, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 1 circle and 2 lines.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified3: nanoocp.GccEnt.GccEnt_QualifiedLin, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 3 lines.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, Point3: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 2 circles and 1 Point.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Point3: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and a line and
        1 Point.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Point3: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 2 lines and 1 Point.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Point2: nanoocp.gp.gp_Pnt2d, Point3: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and passing
        through 2 Points.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Point2: nanoocp.gp.gp_Pnt2d, Point3: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a line and passing
        through 2 Points.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, Point3: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles passing through 3 Points.
        ConstructionError is raised if there is a problem during
        the computation.
        """

    @overload
    def __init__(self, theOther: GccAna_Circ2d3Tan) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has
        reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of
        solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the
        context of the algorithm-object.
        Raises OutOfRange if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        Returns the information about the qualifiers of the
        tangency
        arguments concerning the solution number Index.
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computedin case of unqualified).
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntArg
        on the argument curv. Raises OutOfRange if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point Pntsol
        on the argument curv. Raises OutOfRange if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def Tangency3(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point Pntsol
        on the argument curv. Raises OutOfRange if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument. Raises OutOfRange if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the second argument. Raises OutOfRange Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def IsTheSame3(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the third argument. Raises OutOfRange if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

class GccAna_Circ2dBisec:
    """
    This class describes functions for building bisecting curves between two 2D circles.
    A bisecting curve between two circles is a curve such
    that each of its points is at the same distance from the
    two circles. It can be an ellipse, hyperbola, circle or line,
    depending on the relative position of the two circles.
    The algorithm computes all the elementary curves which
    are solutions. There is no solution if the two circles are coincident.
    A Circ2dBisec object provides a framework for:
    -   defining the construction of the bisecting curves,
    -   implementing the construction algorithm, and consulting the result.
    """

    @overload
    def __init__(self, Circ1: nanoocp.gp.gp_Circ2d, Circ2: nanoocp.gp.gp_Circ2d) -> None:
        """Constructs bisecting curves between the two circles Circ1 and Circ2."""

    @overload
    def __init__(self, theOther: GccAna_Circ2dBisec) -> None: ...

    def IsDone(self) -> bool:
        """This method returns True if the construction algorithm succeeded."""

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.GccInt.GccInt_Bisec:
        """
        Returns the solution number Index
        Raises OutOfRange exception if Index is greater than
        the number of solutions.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

class GccAna_Circ2dTanCen:
    """
    This class implements the algorithms used to
    create 2d circles tangent to an entity and
    centered on a point.
    The arguments of all construction methods are :
    - The qualified element for the tangency constrains
    (QualifiedCirc, Line, Point).
    - The center point Pcenter.
    - A real Tolerance.
    Tolerance is only used in the limits cases.
    For example :
    We want to create a circle tangent to an EnclosedCirc C1
    with a tolerance Tolerance.
    If we did not used Tolerance it is impossible to
    find a solution in the following case : Pcenter is
    outside C1.
    With Tolerance we will give a solution if the distance
    between C1 and Pcenter is lower than or equal Tolerance.
    """

    @overload
    def __init__(self, Linetan: nanoocp.gp.gp_Lin2d, Pcenter: nanoocp.gp.gp_Pnt2d) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a line and
        centered on a point.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Pcenter: nanoocp.gp.gp_Pnt2d) -> None:
        """
        This method implements the algorithms used to
        create 2d circles passing through a point and
        centered on a point.
        Tolerance is a tolerance criterion used by the algorithm
        to find a solution when, mathematically, the problem
        posed does not have a solution, but where there is
        numeric uncertainty attached to the arguments.
        In these algorithms Tolerance is only used in very
        specific cases where the center of the solution is very
        close to the circle to which it is tangential, and where the
        solution is therefore a very small circle.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosing for a line).
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Pcenter: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and
        centered on a point.
        """

    @overload
    def __init__(self, theOther: GccAna_Circ2dTanCen) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached
        its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of circles, representing solutions
        computed by this algorithm and raises NotDone
        exception if the algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the circle, representing the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the
        context of the algorithm-object.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions or less than zer
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns the qualifier Qualif1 of the tangency argument
        for the solution of index Index computed by this algorithm.
        The returned qualifier is:
        -   that specified at the start of construction when the
        solutions are defined as enclosed, enclosing or
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computedin case of unqualified).
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntArg
        on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions or less than zero.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions or less than zero.
        """

class GccAna_Circ2dTanOnRad:
    """
    This class implements the algorithms used to
    create a 2d circle tangent to a 2d entity,
    centered on a curv and with a given radius.
    The arguments of all construction methods are :
    - The qualified element for the tangency constrains
    (QualifiedCirc, QualifiedLin, Points).
    - The Center element (circle, line).
    - A real Tolerance.
    Tolerance is only used in the limits cases.
    For example :
    We want to create a circle tangent to an OutsideCirc C1
    centered on a line OnLine with a radius Radius and with
    a tolerance Tolerance.
    If we did not use Tolerance it is impossible to
    find a solution in the following case : OnLine is
    outside C1. There is no intersection point between C1
    and OnLine. The distance between the line and the
    circle is greater than Radius.
    With Tolerance we will give a solution if the
    distance between C1 and OnLine is lower than or
    equal Tolerance.
    """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, OnLine: nanoocp.gp.gp_Lin2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a circle and centered on a 2d Line
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        For example Tolerance is used in the case of EnclosedCirc when
        Radius-R1+dist is greater Tolerance (dist is the distance
        between the line and the location of the circ, R1 is the
        radius of the circ) because there is no solution.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, OnLine: nanoocp.gp.gp_Lin2d, Radius: float, Tolerance: float) -> None: ...

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, OnLine: nanoocp.gp.gp_Lin2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles passing through a 2d Point and centered on a
        2d Line with a given radius.
        Tolerance is used to find solution in every limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, OnCirc: nanoocp.gp.gp_Circ2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a circle and centered on a 2d Circle
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, OnCirc: nanoocp.gp.gp_Circ2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a 2d Line and centered on a 2d Line
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, OnCirc: nanoocp.gp.gp_Circ2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles passing through a 2d Point and centered on a
        2d Line with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, theOther: GccAna_Circ2dTanOnRad) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction algorithm does not fail
        (even if it finds no solution).
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has
        reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of circles, representing solutions.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the
        context of the algorithm-object.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns the qualifier Qualif1 of the tangency argument
        for the solution of index Index computed by this algorithm.
        The returned qualifier is:
        -   that specified at the start of construction when the
        solutions are defined as enclosed, enclosing or
        outside with respect to the argument, or
        -   that computed during construction (i.e. enclosed,
        enclosing or outside) when the solutions are defined
        as unqualified with respect to the argument, or
        -   GccEnt_noqualifier if the tangency argument is a point.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point on the
        solution curv.
        ParArg is the intrinsic parameter of the point on the
        argument curv.
        PntSol is the tangency point on the solution curv.
        PntArg is the tangency point on the argument curv.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def CenterOn3(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Returns information about the center (on the curv)
        of the result.
        ParArg is the intrinsic parameter of the point on
        the argument curv.
        PntSol is the center point of the solution curv.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument and False in the other cases.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

class GccAna_CircLin2dBisec:
    """
    Describes functions for building bisecting curves between a 2D line and a 2D circle.
    A bisecting curve between a circle and a line is a curve
    such that each of its points is at the same distance from
    the circle and the line. It can be a parabola or a line,
    depending of the relative position of the line and the
    circle. The algorithm computes all the elementary curves which are solutions.
    A CircLin2dBisec object provides a framework for:
    -   defining the construction of the bisecting curves,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Circle: nanoocp.gp.gp_Circ2d, Line: nanoocp.gp.gp_Lin2d) -> None:
        """
        Constructs bisecting curves between the circle Circle and the line Line.
        """

    @overload
    def __init__(self, theOther: GccAna_CircLin2dBisec) -> None: ...

    def IsDone(self) -> bool:
        """Returns true (this construction algorithm never fails)."""

    def NbSolutions(self) -> int:
        """
        Returns the number of curves, representing solutions computed by this algorithm.
        """

    def ThisSolution(self, Index: int) -> nanoocp.GccInt.GccInt_Bisec:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        """

class GccAna_CircPnt2dBisec:
    """
    Describes functions for building a bisecting curve
    between a 2D circle and a point.
    A bisecting curve between a circle and a point is such a
    curve that each of its points is at the same distance from
    the circle and the point. It can be an ellipse, hyperbola,
    circle or line, depending on the relative position of the
    point and the circle. The algorithm computes all the
    elementary curves which are solutions.
    A CircPnt2dBisec object provides a framework for:
    -   defining the construction of the bisecting curves,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Circle1: nanoocp.gp.gp_Circ2d, Point2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs bisecting curves between the circle Circle1 and the point Point2.
        """

    @overload
    def __init__(self, Circle1: nanoocp.gp.gp_Circ2d, Point2: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        Constructs bisecting curves between the circle Circle1 and the point Point2.
        Tolerance is used.
        """

    @overload
    def __init__(self, theOther: GccAna_CircPnt2dBisec) -> None: ...

    def IsDone(self) -> bool:
        """Returns true (this construction algorithm never fails)."""

    def NbSolutions(self) -> int:
        """
        Returns the number of curves, representing solutions computed by this algorithm.
        """

    def ThisSolution(self, Index: int) -> nanoocp.GccInt.GccInt_Bisec:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        """

class GccAna_Lin2d2Tan:
    """
    This class implements the algorithms used to
    create 2d lines tangent to 2 other elements which
    can be circles or points.
    Describes functions for building a 2D line:
    -   tangential to 2 circles, or
    -   tangential to a circle and passing through a point, or
    -   passing through 2 points.
    A Lin2d2Tan object provides a framework for:
    -   defining the construction of 2D line(s),
    -   implementing the construction algorithm, and
    consulting the result(s).
    Some constructors may check the type of the qualified argument
    and raise BadQualifier Error in case of incorrect couple (qualifier,
    curv).
    For example: "EnclosedCirc".
    """

    @overload
    def __init__(self, ThePoint1: nanoocp.gp.gp_Pnt2d, ThePoint2: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to
        create 2d lines passing through 2 points.
        Tolerance is used because we can't create a line
        when the distance between the two points is too small.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, ThePoint: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to
        create 2d lines tangent to one circle and passing
        through a point.
        Exception BadQualifier is raised in the case of
        EnclosedCirc
        Tolerance is used because there is no solution
        when the point is inside the solution according to
        the tolerance.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to
        create 2d lines tangent to 2 circles.
        Exception BadQualifier is raised in the case of
        EnclosedCirc
        """

    @overload
    def __init__(self, theOther: GccAna_Lin2d2Tan) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns true when there is a solution
        and false in the other cases.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the
        context of the algorithm-object. Raises OutOfRange is raised if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        Returns the qualifiers Qualif1 and Qualif2 of the
        tangency arguments for the solution of index Index
        computed by this algorithm.
        The returned qualifiers are:
        -   those specified at the start of construction when the
        solutions are defined as enclosing or outside with
        respect to the arguments, or
        -   those computed during construction (i.e. enclosing or
        outside) when the solutions are defined as unqualified
        with respect to the arguments, or
        -   GccEnt_noqualifier if the tangency argument is a point.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on
        the argument curv. Raises OutOfRange is raised if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the second argument.
        ParSol is the intrinsic parameter of the point ParSol on
        the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on
        the argument curv. Raises OutOfRange is raised if Index is greater than
        the number of solutions.
        It raises NotDone if the algorithm failed.
        """

class GccAna_Lin2dBisec:
    """
    Describes functions for building bisecting lines between two 2D lines.
    A bisecting line between two lines is such that each of its
    points is at the same distance from the two lines.
    If the two lines are secant, there are two orthogonal
    bisecting lines which share the angles made by the two
    straight lines in two equal parts. If D1 and D2 are the
    unit vectors of the two straight lines, those of the two
    bisecting lines are collinear with the following vectors:
    -   D1 + D2 for the "internal" bisecting line,
    -   D1 - D2 for the "external" bisecting line.
    If the two lines are parallel, the (unique) bisecting line is
    the straight line equidistant from the two straight lines. If
    the two straight lines are coincident, the algorithm
    returns the first straight line as the solution.
    A Lin2dTanObl object provides a framework for:
    -   defining the construction of the bisecting lines,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Lin1: nanoocp.gp.gp_Lin2d, Lin2: nanoocp.gp.gp_Lin2d) -> None:
        """Constructs bisecting lines between the two lines Lin1 and Lin2."""

    @overload
    def __init__(self, theOther: GccAna_Lin2dBisec) -> None: ...

    def IsDone(self) -> bool:
        """Returns True when the algorithm succeeded."""

    def NbSolutions(self) -> int:
        """
        Returns the number of solutions and raise NotDone if
        the constructor wasn't called before.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the solution number Index .
        The first solution is the inside one and the second is the
        outside one.
        For the first solution the direction is D1+D2 (D1 is
        the direction of the first argument and D2 the
        direction of the second argument).
        For the second solution the direction is D1-D2.
        Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def Intersection1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the intersection point between
        the result number Index and the first argument.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def Intersection2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the intersection point between
        the result number Index and the second argument.
        Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

class GccAna_Lin2dTanObl:
    """
    This class implements the algorithms used to
    create 2d line tangent to a circle or a point and
    making an angle with a line.
    The angle is in radians.
    The origin of the solution is the tangency point
    with the first argument.
    Its direction is making an angle Angle with the
    second argument.
    """

    @overload
    def __init__(self, ThePoint: nanoocp.gp.gp_Pnt2d, TheLine: nanoocp.gp.gp_Lin2d, TheAngle: float) -> None:
        """
        This class implements the algorithms used to
        create 2d line passing through a point and
        making an angle with a line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, TheLine: nanoocp.gp.gp_Lin2d, TheAngle: float) -> None:
        """
        This class implements the algorithms used to
        create 2d line tangent to a circle and
        making an angle with a line.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosed for a circle).
        """

    @overload
    def __init__(self, theOther: GccAna_Lin2dTanObl) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns True if the algorithm succeeded.
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached
        its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of lines, representing solutions computed by this algorithm.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the solution number Index.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the
        context of the algorithm-object.
        raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the number of solutions.
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns the qualifier Qualif1 of the tangency argument
        for the solution of index Index computed by this algorithm.
        The returned qualifier is:
        -   that specified at the start of construction when the
        solutions are defined as enclosing or outside with
        respect to the argument, or
        -   that computed during construction (i.e. enclosing or
        outside) when the solutions are defined as unqualified
        with respect to the argument, or
        -   GccEnt_noqualifier if the tangency argument is a point.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point ParSol on
        the solution curv.
        ParArg is the intrinsic parameter of the point ParArg on
        the argument curv. Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the number of solutions.
        """

    def Intersection2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the intersection between the
        result number Index and the third argument.
        Raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the number of solutions.
        """

class GccAna_Lin2dTanPar:
    """
    This class implements the algorithms used to create 2d
    line tangent to a circle or a point and parallel to
    another line.
    The solution has the same orientation as the
    second argument.
    Describes functions for building a 2D line parallel to a line and:
    -   tangential to a circle, or
    -   passing through a point.
    A Lin2dTanPar object provides a framework for:
    -   defining the construction of 2D line(s),
    -   implementing the construction algorithm, and consulting the result(s).
    """

    @overload
    def __init__(self, ThePoint: nanoocp.gp.gp_Pnt2d, Lin1: nanoocp.gp.gp_Lin2d) -> None:
        """
        This method implements the algorithms used to create a 2d
        line passing through a point and parallel to
        another line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Lin1: nanoocp.gp.gp_Lin2d) -> None:
        """
        This method implements the algorithms used to create a 2d
        line tangent to a circle and parallel to another line.
        It raises BadQualifier in case of EnclosedCirc.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosed for a circle).
        """

    @overload
    def __init__(self, theOther: GccAna_Lin2dTanPar) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the algorithm succeeded."""

    def NbSolutions(self) -> int:
        """
        Returns the number of solutions.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the
        context of the algorithm-object.
        raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns the information about the qualifiers of the
        tangency arguments concerning the solution number Index.
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computed in case of unqualified).
        Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def Tangency1(self, Index: int, Pnt: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point on the
        solution curv.
        ParArg is the intrinsic parameter of the point on the
        argument curv.
        ParArg is equal 0 when the solution is passing through
        a point. Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

class GccAna_Lin2dTanPer:
    """
    This class implements the algorithms used to
    create 2d lines tangent to a circle or a point and
    perpendicular to a line or a circle.
    Describes functions for building a 2D line perpendicular
    to a line and:
    -   tangential to a circle, or
    -   passing through a point.
    A Lin2dTanPer object provides a framework for:
    -   defining the construction of 2D line(s),
    -   implementing the construction algorithm, and
    -   consulting the result(s).
    """

    @overload
    def __init__(self, ThePnt: nanoocp.gp.gp_Pnt2d, TheLin: nanoocp.gp.gp_Lin2d) -> None:
        """
        This method implements the algorithms used to
        create 2d lines passing through a point and
        perpendicular to a line.
        """

    @overload
    def __init__(self, ThePnt: nanoocp.gp.gp_Pnt2d, TheCircle: nanoocp.gp.gp_Circ2d) -> None:
        """
        This method implements the algorithms used to
        create 2d lines passing through a point and
        perpendicular to a circle.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, TheLin: nanoocp.gp.gp_Lin2d) -> None:
        """
        This method implements the algorithms used to
        create 2d lines tangent to a circle and
        perpendicular to a line.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, TheCircle: nanoocp.gp.gp_Circ2d) -> None:
        """
        This method implements the algorithms used to
        create 2d lines tangent to a circle and
        perpendicular to a circle.
        """

    @overload
    def __init__(self, theOther: GccAna_Lin2dTanPer) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the algorithm succeeded."""

    def NbSolutions(self) -> int:
        """
        Returns the number of solutions.
        Raises NotDone if the construction algorithm didn't succeed.
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns the qualifier Qualif1 of the tangency argument
        for the solution of index Index computed by this algorithm.
        The returned qualifier is:
        -   that specified at the start of construction when the
        solutions are defined as enclosing or outside with
        respect to the argument, or
        -   that computed during construction (i.e. enclosing or
        outside) when the solutions are defined as unqualified
        with respect to the argument, or
        -   GccEnt_noqualifier if the tangency argument is a point.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the
        context of the algorithm-object.
        Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def Tangency1(self, Index: int, Pnt: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point on the
        solution curv.
        ParArg is the intrinsic parameter of the point on the
        argument curv.
        If the first argument is a point ParArg is equal zero.
        raises NotDone if the construction algorithm didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def Intersection2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the intersection between the
        solution number Index and the second argument.
        It returns the first intersection in a case of
        Lin2dTanPer which is perpendicular to a circle .
        ParSol is the intrinsic parameter of the point on the
        solution curv.
        ParArg is the intrinsic parameter of the point on the
        argument curv. Raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

class GccAna_LinPnt2dBisec:
    """
    Describes functions for building bisecting curves between a 2D line and a point.
    A bisecting curve between a line and a point is such a
    curve that each of its points is at the same distance from
    the circle and the point. It can be a parabola or a line,
    depending on the relative position of the line and the
    circle. There is always one unique solution.
    A LinPnt2dBisec object provides a framework for:
    - defining the construction of the bisecting curve,
    - implementing the construction algorithm, and
    - consulting the result.
    """

    @overload
    def __init__(self, Line1: nanoocp.gp.gp_Lin2d, Point2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a bisecting curve between the line Line1 and the point Point2.
        """

    @overload
    def __init__(self, theOther: GccAna_LinPnt2dBisec) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the algorithm succeeded."""

    def ThisSolution(self) -> nanoocp.GccInt.GccInt_Bisec:
        """
        Returns the number of solutions.
        It raises NotDone if the construction algorithm didn't succeed.
        """

class GccAna_NoSolution(nanoocp.Standard.Standard_Failure):
    pass

class GccAna_Pnt2dBisec:
    """
    This class implements the algorithms used to
    create the bisecting line between two 2d points
    Describes functions for building a bisecting line between two 2D points.
    The bisecting line between two points is the bisector of
    the segment which joins the two points, if these are not coincident.
    The algorithm does not find a solution if the two points are coincident.
    A Pnt2dBisec object provides a framework for:
    -   defining the construction of the bisecting line,
    -   implementing the construction algorithm, and consulting the result.
    """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d) -> None:
        """Constructs a bisecting line between the points Point1 and Point2."""

    @overload
    def __init__(self, theOther: GccAna_Pnt2dBisec) -> None: ...

    def IsDone(self) -> bool:
        """Returns true (this construction algorithm never fails)."""

    def HasSolution(self) -> bool:
        """
        Returns true if this algorithm has a solution, i.e. if the
        two points are not coincident.
        """

    def ThisSolution(self) -> nanoocp.gp.gp_Lin2d:
        """Returns a line, representing the solution computed by this algorithm."""
