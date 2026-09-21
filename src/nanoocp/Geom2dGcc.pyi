"""OCCT package Geom2dGcc (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.GccAna
import nanoocp.GccEnt
import nanoocp.Geom2d
import nanoocp.Geom2dAdaptor
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class Geom2dGcc_Type3(enum.IntEnum):
    Geom2dGcc_CuCu = 0

    Geom2dGcc_CiCu = 1

Geom2dGcc_CuCu: Geom2dGcc_Type3 = Geom2dGcc_Type3.Geom2dGcc_CuCu

Geom2dGcc_CiCu: Geom2dGcc_Type3 = Geom2dGcc_Type3.Geom2dGcc_CiCu

class Geom2dGcc_Type1(enum.IntEnum):
    Geom2dGcc_CuCuCu = 0

    Geom2dGcc_CiCuCu = 1

    Geom2dGcc_CiCiCu = 2

    Geom2dGcc_CiLiCu = 3

    Geom2dGcc_LiLiCu = 4

    Geom2dGcc_LiCuCu = 5

Geom2dGcc_CuCuCu: Geom2dGcc_Type1 = Geom2dGcc_Type1.Geom2dGcc_CuCuCu

Geom2dGcc_CiCuCu: Geom2dGcc_Type1 = Geom2dGcc_Type1.Geom2dGcc_CiCuCu

Geom2dGcc_CiCiCu: Geom2dGcc_Type1 = Geom2dGcc_Type1.Geom2dGcc_CiCiCu

Geom2dGcc_CiLiCu: Geom2dGcc_Type1 = Geom2dGcc_Type1.Geom2dGcc_CiLiCu

Geom2dGcc_LiLiCu: Geom2dGcc_Type1 = Geom2dGcc_Type1.Geom2dGcc_LiLiCu

Geom2dGcc_LiCuCu: Geom2dGcc_Type1 = Geom2dGcc_Type1.Geom2dGcc_LiCuCu

class Geom2dGcc_Type2(enum.IntEnum):
    Geom2dGcc_CuCuOnCu = 0

    Geom2dGcc_CiCuOnCu = 1

    Geom2dGcc_LiCuOnCu = 2

    Geom2dGcc_CuPtOnCu = 3

    Geom2dGcc_CuCuOnLi = 4

    Geom2dGcc_CiCuOnLi = 5

    Geom2dGcc_LiCuOnLi = 6

    Geom2dGcc_CuPtOnLi = 7

    Geom2dGcc_CuCuOnCi = 8

    Geom2dGcc_CiCuOnCi = 9

    Geom2dGcc_LiCuOnCi = 10

    Geom2dGcc_CuPtOnCi = 11

Geom2dGcc_CuCuOnCu: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CuCuOnCu

Geom2dGcc_CiCuOnCu: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CiCuOnCu

Geom2dGcc_LiCuOnCu: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_LiCuOnCu

Geom2dGcc_CuPtOnCu: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CuPtOnCu

Geom2dGcc_CuCuOnLi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CuCuOnLi

Geom2dGcc_CiCuOnLi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CiCuOnLi

Geom2dGcc_LiCuOnLi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_LiCuOnLi

Geom2dGcc_CuPtOnLi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CuPtOnLi

Geom2dGcc_CuCuOnCi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CuCuOnCi

Geom2dGcc_CiCuOnCi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CiCuOnCi

Geom2dGcc_LiCuOnCi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_LiCuOnCi

Geom2dGcc_CuPtOnCi: Geom2dGcc_Type2 = Geom2dGcc_Type2.Geom2dGcc_CuPtOnCi

class Geom2dGcc:
    """
    The Geom2dGcc package describes qualified 2D
    curves used in the construction of constrained geometric
    objects by an algorithm provided by the Geom2dGcc package.
    A qualified 2D curve is a curve with a qualifier which
    specifies whether the solution of a construction
    algorithm using the qualified curve (as an argument):
    -   encloses the curve, or
    -   is enclosed by the curve, or
    -   is built so that both the curve and this solution are external to one another, or
    -   is undefined (all solutions apply).
    These package methods provide simpler functions to construct a qualified curve.
    Note: the interior of a curve is defined as the left-hand
    side of the curve in relation to its orientation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc) -> None: ...

    @staticmethod
    def Unqualified(Obj: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve:
        """
        Constructs such a qualified curve that the relative
        position of the solution computed by a construction
        algorithm using the qualified curve to the circle or line is
        not qualified, i.e. all solutions apply.
        Warning
        Obj is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by a computation algorithm.
        The adapted curve is created in the following way:
        occ::handle<Geom2d_Curve> mycurve = ...
        ;
        Geom2dAdaptor_Curve Obj ( mycurve )
        ;
        The qualified curve is then constructed with this object:
        Geom2dGcc_QualifiedCurve
        myQCurve = Geom2dGcc::Unqualified(Obj);
        """

    @staticmethod
    def Enclosing(Obj: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve:
        """
        Constructs such a qualified curve that the solution
        computed by a construction algorithm using the qualified
        curve encloses the curve.
        Warning
        Obj is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by a computation algorithm.
        The adapted curve is created in the following way:
        occ::handle<Geom2d_Curve> mycurve = ...
        ;
        Geom2dAdaptor_Curve Obj ( mycurve )
        ;
        The qualified curve is then constructed with this object:
        Geom2dGcc_QualifiedCurve
        myQCurve = Geom2dGcc::Enclosing(Obj);
        """

    @staticmethod
    def Enclosed(Obj: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve:
        """
        Constructs such a qualified curve that the solution
        computed by a construction algorithm using the qualified
        curve is enclosed by the curve.
        Warning
        Obj is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by a computation algorithm.
        The adapted curve is created in the following way:
        occ::handle<Geom2d_Curve> mycurve = ...
        ;
        Geom2dAdaptor_Curve Obj ( mycurve )
        ;
        The qualified curve is then constructed with this object:
        Geom2dGcc_QualifiedCurve
        myQCurve = Geom2dGcc::Enclosed(Obj);
        """

    @staticmethod
    def Outside(Obj: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve:
        """
        Constructs such a qualified curve that the solution
        computed by a construction algorithm using the qualified
        curve and the curve are external to one another.
        Warning
        Obj is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by a computation algorithm.
        The adapted curve is created in the following way:
        occ::handle<Geom2d_Curve> mycurve = ...
        ;
        Geom2dAdaptor_Curve Obj ( mycurve )
        ;
        The qualified curve is then constructed with this object:
        Geom2dGcc_QualifiedCurve
        myQCurve = Geom2dGcc::Outside(Obj);
        """

class Geom2dGcc_Circ2d2TanOn:
    """
    This class implements the algorithms used to
    create 2d circles TANgent to 2 entities and
    having the center ON a curve.
    The order of the tangency argument is always
    QualifiedCirc, QualifiedLin, QualifiedCurv, Pnt2d.
    the arguments are :
    - The two tangency arguments.
    - The center line.
    - The parameter for each tangency argument which
    is a curve.
    - The tolerance.
    """

    @overload
    def __init__(self, Point1: nanoocp.Geom2d.Geom2d_Point | None, Point2: nanoocp.Geom2d.Geom2d_Point | None, OnCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two points and
        having the center ON a 2d curve.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Point: nanoocp.Geom2d.Geom2d_Point | None, OnCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float, Param1: float, ParamOn: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to one curve and one point and
        having the center ON a 2d curve.
        Param1 is the initial guess on the first curve QualifiedCurv.
        ParamOn is the initial guess on the center curve OnCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Qualified2: Geom2dGcc_QualifiedCurve, OnCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float, Param1: float, Param2: float, ParamOn: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two curves and
        having the center ON a 2d curve.
        Param1 is the initial guess on the first curve QualifiedCurv.
        Param1 is the initial guess on the second curve QualifiedCurv.
        ParamOn is the initial guess on the center curve OnCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d2TanOn) -> None: ...

    @overload
    def Results(self, Circ: nanoocp.GccAna.GccAna_Circ2d2TanOn) -> None: ...

    @overload
    def Results(self, Circ: Geom2dGcc_Circ2d2TanOnGeo) -> None: ...

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
        This method returns the number of solutions.
        NotDone is raised if the algorithm failed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the context
        of the algorithm-object.
        Exceptions
        Standard_OutOfRange if Index is less than or equal
        to zero or greater than the number of solutions
        computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        It returns the information about the qualifiers of
        the tangency
        arguments concerning the solution number Index.
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computedin case of unqualified).
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the second argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """

    def CenterOn3(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Returns the center PntSol of the solution of index Index
        computed by this algorithm.
        ParArg is the parameter of the point PntSol on the third argument.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns true if the solution of index Index and,
        respectively, the first or second argument of this
        algorithm are the same (i.e. there are 2 identical circles).
        If Rarg is the radius of the first or second argument,
        Rsol is the radius of the solution and dist is the
        distance between the two centers, we consider the two
        circles to be identical if |Rarg - Rsol| and dist
        are less than or equal to the tolerance criterion given at
        the time of construction of this algorithm.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        Returns true if the solution of index Index and,
        respectively, the first or second argument of this
        algorithm are the same (i.e. there are 2 identical circles).
        If Rarg is the radius of the first or second argument,
        Rsol is the radius of the solution and dist is the
        distance between the two centers, we consider the two
        circles to be identical if |Rarg - Rsol| and dist
        are less than or equal to the tolerance criterion given at
        the time of construction of this algorithm.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

class Geom2dGcc_Circ2d2TanOnGeo:
    """
    This class implements the algorithms used to
    create 2d circles TANgent to 2 entities and
    having the center ON a curve.
    The order of the tangency argument is always
    QualifiedCirc, QualifiedLin, QualifiedCurv, Pnt2d.
    the arguments are :
    - The two tangency arguments (lines, circles or points).
    - The center line (a curve).
    - The parameter for each tangency argument which
    is a curve.
    - The tolerance.
    """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d circles and
        having the center ON a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a 2d line
        having the center ON a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Point2: nanoocp.gp.gp_Pnt2d, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a point
        having the center ON a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two 2d lines
        having the center ON a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.gp.gp_Pnt2d, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a point
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two points
        having the center ON a 2d line.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d2TanOnGeo) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the
        context of the algorithm-object.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        It returns the information about the qualifiers of
        the tangency
        arguments concerning the solution number Index.
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computedin case of unqualified).
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
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the second argument.
        ParSol is the intrinsic parameter of the point on the
        solution curv.
        ParArg is the intrinsic parameter of the point on the
        argument curv.
        PntSol is the tangency point on the solution curv.
        PntArg is the tangency point on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
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
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument and False in the other cases.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the second argument and False in the other cases.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

class Geom2dGcc_Circ2d2TanOnIter:
    """
    This class implements the algorithms used to
    create 2d circles TANgent to 2 entities and
    having the center ON a curv.
    The order of the tangency argument is always
    QualifiedCirc, QualifiedLin, QualifiedCurv, Pnt2d.
    the arguments are :
    - The two tangency arguments.
    - The center line.
    - The parameter for each tangency argument which
    is a curve.
    - The tolerance.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Point2: nanoocp.gp.gp_Pnt2d, OnLine: nanoocp.gp.gp_Lin2d, Param1: float, Param2: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d point and a curve and
        having the center ON a 2d line.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Point2: nanoocp.gp.gp_Pnt2d, OnCirc: nanoocp.gp.gp_Circ2d, Param1: float, Param2: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d point and a curve and
        having the center ON a 2d circle.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Point2: nanoocp.gp.gp_Pnt2d, OnCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Param1: float, ParamOn: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d Point and a curve and
        having the center ON a 2d curve.
        Param1 is the initial guess on the curve QualifiedCurv.
        ParamOn is the initial guess on the center curve OnCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, OnLine: nanoocp.gp.gp_Lin2d, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a curve and
        having the center ON a 2d line.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: Geom2dGcc_QCurve, OnLine: nanoocp.gp.gp_Lin2d, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a curve and
        having the center ON a 2d line.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, OnLine: nanoocp.gp.gp_Lin2d, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two curves and
        having the center ON a 2d line.
        Param1 is the initial guess on the first QualifiedCurv.
        Param2 is the initial guess on the first QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, OnCirc: nanoocp.gp.gp_Circ2d, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a curve and
        having the center ON a 2d circle.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: Geom2dGcc_QCurve, OnCirc: nanoocp.gp.gp_Circ2d, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a curve and
        having the center ON a 2d circle.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, OnCirc: nanoocp.gp.gp_Circ2d, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two curves and
        having the center ON a 2d circle.
        Param1 is the initial guess on the first QualifiedCurv.
        Param2 is the initial guess on the first QualifiedCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Param1: float, Param2: float, ParamOn: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a curve and
        having the center ON a 2d curve.
        Param2 is the initial guess on the curve QualifiedCurv.
        ParamOn is the initial guess on the center curve OnCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: Geom2dGcc_QCurve, OnCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Param1: float, Param2: float, ParamOn: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a curve and
        having the center ON a 2d curve.
        Param2 is the initial guess on the curve QualifiedCurv.
        ParamOn is the initial guess on the center curve OnCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, OnCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Param1: float, Param2: float, ParamOn: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two curves and
        having the center ON a 2d curve.
        Param1 is the initial guess on the first curve QualifiedCurv.
        Param1 is the initial guess on the second curve QualifiedCurv.
        ParamOn is the initial guess on the center curve OnCurv.
        Tolerance is used for the limit cases.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d2TanOnIter) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        """

    def ThisSolution(self) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def WhichQualifier(self) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]: ...

    def Tangency1(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between
        the result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol
        on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def Tangency2(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between
        the result and the second argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol
        on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def CenterOn3(self, PntSol: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Returns information about the center (on the curv) of the
        result and the third argument.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def IsTheSame1(self) -> bool:
        """
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def IsTheSame2(self) -> bool:
        """
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

class Geom2dGcc_Circ2d2TanRad:
    """
    This class implements the algorithms used to
    create 2d circles tangent to one curve and a
    point/line/circle/curv and with a given radius.
    For each construction methods arguments are:
    - Two Qualified elements for tangency constrains.
    (for example EnclosedCirc if we want the
    solution inside the argument EnclosedCirc).
    - Two Reals. One (Radius) for the radius and the
    other (Tolerance) for the tolerance.
    Tolerance is only used for the limit cases.
    For example :
    We want to create a circle inside a circle C1 and
    inside a curve Cu2 with a radius Radius and a
    tolerance Tolerance.
    If we did not used Tolerance it is impossible to
    find a solution in the following case : Cu2 is
    inside C1 and there is no intersection point
    between the two elements.
    with Tolerance we will give a solution if the
    lowest distance between C1 and Cu2 is lower than or
    equal Tolerance.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Qualified2: Geom2dGcc_QualifiedCurve, Radius: float, Tolerance: float) -> None: ...

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Point: nanoocp.Geom2d.Geom2d_Point | None, Radius: float, Tolerance: float) -> None: ...

    @overload
    def __init__(self, Point1: nanoocp.Geom2d.Geom2d_Point | None, Point2: nanoocp.Geom2d.Geom2d_Point | None, Radius: float, Tolerance: float) -> None:
        """
        These constructors create one or more 2D circles of radius Radius either
        -   tangential to the 2 curves Qualified1 and Qualified2, or
        -   tangential to the curve Qualified1 and passing through the point Point, or
        -   passing through two points Point1 and Point2.
        Tolerance is a tolerance criterion used by the algorithm
        to find a solution when, mathematically, the problem
        posed does not have a solution, but where there is
        numeric uncertainty attached to the arguments.
        For example, take two circles C1 and C2, such that C2
        is inside C1, and almost tangential to C1. There is, in
        fact, no point of intersection between C1 and C2. You
        now want to find a circle of radius R (smaller than the
        radius of C2), which is tangential to C1 and C2, and
        inside these two circles: a pure mathematical resolution
        will not find a solution. This is where the tolerance
        criterion is used: the algorithm considers that C1 and
        C2 are tangential if the shortest distance between these
        two circles is less than or equal to Tolerance. Thus, a
        solution is found by the algorithm.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosing for a line).
        Standard_NegativeValue if Radius is negative.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d2TanRad) -> None: ...

    @overload
    def Results(self, Circ: nanoocp.GccAna.GccAna_Circ2d2TanRad) -> None: ...

    @overload
    def Results(self, Circ: Geom2dGcc_Circ2d2TanRadGeo) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the algorithm succeeded.
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        NotDone is raised if the algorithm failed.
        Exceptions
        StdFail_NotDone if the construction fails.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the context of the algorithm-object.
        Warning
        This indexing simply provides a means of consulting the
        solutions. The index values are not associated with
        these solutions outside the context of the algorithm object.
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
        -   GccEnt_noqualifier if the tangency argument is a point, or
        -   GccEnt_unqualified in certain limit cases where it
        is impossible to qualify the solution as enclosed, enclosing or outside.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        OutOfRange is raised if Index is greater than the number of solutions.
        notDone is raised if the construction algorithm did not succeed.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the second argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        OutOfRange is raised if Index is greater than the number of solutions.
        notDone is raised if the construction algorithm did not succeed.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns true if the solution of index Index and,
        respectively, the first or second argument of this
        algorithm are the same (i.e. there are 2 identical circles).
        If Rarg is the radius of the first or second argument,
        Rsol is the radius of the solution and dist is the
        distance between the two centers, we consider the two
        circles to be identical if |Rarg - Rsol| and dist
        are less than or equal to the tolerance criterion given at
        the time of construction of this algorithm.
        OutOfRange is raised if Index is greater than the number of solutions.
        notDone is raised if the construction algorithm did not succeed.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        Returns true if the solution of index Index and,
        respectively, the first or second argument of this
        algorithm are the same (i.e. there are 2 identical circles).
        If Rarg is the radius of the first or second argument,
        Rsol is the radius of the solution and dist is the
        distance between the two centers, we consider the two
        circles to be identical if |Rarg - Rsol| and dist
        are less than or equal to the tolerance criterion given at
        the time of construction of this algorithm.
        OutOfRange is raised if Index is greater than the number of solutions.
        notDone is raised if the construction algorithm did not succeed.
        """

class Geom2dGcc_Circ2d2TanRadGeo:
    """
    This class implements the algorithms used to
    create 2d circles tangent to one curve and a
    point/line/circle/curv and with a given radius.
    For each construction methods arguments are:
    - Two Qualified elements for tangency constrains.
    (for example EnclosedCirc if we want the
    solution inside the argument EnclosedCirc).
    - Two Reals. One (Radius) for the radius and the
    other (Tolerance) for the tolerance.
    Tolerance is only used for the limit cases.
    For example :
    We want to create a circle inside a circle C1 and
    inside a curve Cu2 with a radius Radius and a
    tolerance Tolerance.
    If we did not used Tolerance it is impossible to
    find a solution in the following case : Cu2 is
    inside C1 and there is no intersection point
    between the two elements.
    With Tolerance we will get a solution if the
    lowest distance between C1 and Cu2 is lower than or
    equal Tolerance.
    """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d circle and a curve
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: Geom2dGcc_QCurve, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a 2d line and a curve
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to two curves with
        a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Point2: nanoocp.gp.gp_Pnt2d, Radius: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles TANgent to a curve and a point
        with a radius of Radius.
        It raises NegativeValue if Radius is lower than zero.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d2TanRadGeo) -> None: ...

    def IsDone(self) -> bool:
        """This method returns True if the algorithm succeeded."""

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        It raises NotDone if the algorithm failed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to those outside the context
        of the algorithm-object.
        It raises OutOfRange exception if Index is greater
        than the number of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        It returns the information about the qualifiers of
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
        argument.
        It raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the second argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution.
        ParArg is the intrinsic parameter of the point PntArg on
        the second argument.
        It raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument.
        It raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

    def IsTheSame2(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the second argument.
        It raises OutOfRange if Index is greater than the number
        of solutions.
        It raises NotDone if the construction algorithm did not
        succeed.
        """

class Geom2dGcc_Circ2d3Tan:
    """
    This class implements the algorithms used to
    create 2d circles tangent to 3 points/lines/circles/
    curves with one curve or more.
    The arguments of all construction methods are :
    - The three qualifiied elements for the
    tangency constrains (QualifiedCirc, QualifiedLine,
    Qualifiedcurv, Points).
    - A parameter for each QualifiedCurv.
    Describes functions for building a 2D circle:
    -   tangential to 3 curves, or
    -   tangential to 2 curves and passing through a point, or
    -   tangential to a curve and passing through 2 points, or
    -   passing through 3 points.
    A Circ2d3Tan object provides a framework for:
    -   defining the construction of 2D circles(s),
    -   implementing the construction algorithm, and
    -   consulting the result(s).
    """

    @overload
    def __init__(self, Point1: nanoocp.Geom2d.Geom2d_Point | None, Point2: nanoocp.Geom2d.Geom2d_Point | None, Point3: nanoocp.Geom2d.Geom2d_Point | None, Tolerance: float) -> None:
        """
        Constructs one or more 2D circles passing through three points Point1, Point2 and Point3.
        Tolerance is a tolerance criterion used by the algorithm
        to find a solution when, mathematically, the problem
        posed does not have a solution, but where there is
        numeric uncertainty attached to the arguments.
        For example, take:
        -   two circles C1 and C2, such that C2 is inside C1,
        and almost tangential to C1; there is in fact no point
        of intersection between C1 and C2; and
        -   a circle C3 outside C1.
        You now want to find a circle which is tangential to C1,
        C2 and C3: a pure mathematical resolution will not find
        a solution. This is where the tolerance criterion is used:
        the algorithm considers that C1 and C2 are tangential if
        the shortest distance between these two circles is less
        than or equal to Tolerance. Thus, the algorithm finds a solution.
        Warning
        An iterative algorithm is used if Qualified1, Qualified2 or
        Qualified3 is more complex than a line or a circle. In
        such cases, the algorithm constructs only one solution.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosing for a line).
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Point1: nanoocp.Geom2d.Geom2d_Point | None, Point2: nanoocp.Geom2d.Geom2d_Point | None, Tolerance: float, Param1: float) -> None:
        """
        Constructs one or more 2D circles tangential to the curve Qualified1 and passing
        through two points Point1 and Point2, where Param1
        is used as the initial value of the parameter on
        Qualified1 of the tangency point between this
        argument and the solution sought, if the algorithm
        chooses an iterative method to find the solution (i.e. if
        Qualified1 is more complex than a line or a circle)
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Qualified2: Geom2dGcc_QualifiedCurve, Point: nanoocp.Geom2d.Geom2d_Point | None, Tolerance: float, Param1: float, Param2: float) -> None:
        """
        Constructs one or more 2D circles
        tangential to two curves Qualified1 and Qualified2
        and passing through the point Point, where Param1
        and Param2 are used, respectively, as the initial
        values of the parameters on Qualified1 and
        Qualified2 of the tangency point between this
        argument and the solution sought, if the algorithm
        chooses an iterative method to find the solution (i.e. if
        either Qualified1 or Qualified2 is more complex than
        a line or a circle).
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Qualified2: Geom2dGcc_QualifiedCurve, Qualified3: Geom2dGcc_QualifiedCurve, Tolerance: float, Param1: float, Param2: float, Param3: float) -> None:
        """
        Constructs one or more 2D circles
        tangential to three curves Qualified1, Qualified2 and
        Qualified3, where Param1, Param2 and Param3 are
        used, respectively, as the initial values of the
        parameters on Qualified1, Qualified2 and Qualified3
        of the tangency point between these arguments and
        the solution sought, if the algorithm chooses an
        iterative method to find the solution (i.e. if either
        Qualified1, Qualified2 or Qualified3 is more complex
        than a line or a circle).
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d3Tan) -> None: ...

    def Results(self, Circ: nanoocp.GccAna.GccAna_Circ2d3Tan, Rank1: int, Rank2: int, Rank3: int) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution).
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        NotDone is raised if the algorithm failed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the context
        of the algorithm-object.
        """

    def WhichQualifier(self, Index: int) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]:
        """
        It returns the information about the qualifiers of the tangency
        arguments concerning the solution number Index.
        It returns the real qualifiers (the qualifiers given to the
        constructor method in case of enclosed, enclosing and outside
        and the qualifiers computedin case of unqualified).
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the second argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """

    def Tangency3(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the third argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """Returns True if the solution is equal to the first argument."""

    def IsTheSame2(self, Index: int) -> bool:
        """Returns True if the solution is equal to the second argument."""

    def IsTheSame3(self, Index: int) -> bool:
        """
        Returns True if the solution is equal to the third argument.
        If Rarg is the radius of the first, second or third
        argument, Rsol is the radius of the solution and dist
        is the distance between the two centers, we consider
        the two circles to be identical if |Rarg - Rsol| and
        dist are less than or equal to the tolerance criterion
        given at the time of construction of this algorithm.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

class Geom2dGcc_Circ2d3TanIter:
    """
    This class implements the algorithms used to
    create 2d circles tangent to 3 points/lines/circles/
    curves with one curve or more.
    The arguments of all construction methods are :
    - The three qualifiied elements for the
    tangency constrains (QualifiedCirc, QualifiedLine,
    Qualifiedcurv, Points).
    - A parameter for each QualifiedCurv.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, Param1: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a curve and 2 points.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, Point3: nanoocp.gp.gp_Pnt2d, Param1: float, Param2: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and a point and
        a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: Geom2dGcc_QCurve, Point3: nanoocp.gp.gp_Pnt2d, Param1: float, Param2: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a line and a curve
        and a point.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, Point2: nanoocp.gp.gp_Pnt2d, Param1: float, Param2: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 2 curves and a point.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified3: Geom2dGcc_QCurve, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 2 circles and a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, Qualified3: Geom2dGcc_QCurve, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and 2 curves.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified3: Geom2dGcc_QCurve, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and a line and
        a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified3: Geom2dGcc_QCurve, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 2 lines and a curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, Qualified2: Geom2dGcc_QCurve, Qualified3: Geom2dGcc_QCurve, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a line and 2 curves.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, Qualified3: Geom2dGcc_QCurve, Param1: float, Param2: float, Param3: float, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to 3 curves.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2d3TanIter) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        """

    def ThisSolution(self) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def WhichQualifier(self) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]: ...

    def Tangency1(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between
        the result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol
        on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def Tangency2(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between
        the result and the second argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol
        on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def Tangency3(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between
        the result and the third argument.
        ParSol is the intrinsic parameter of the point PntSol
        on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol
        on the argument curv.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def IsTheSame1(self) -> bool:
        """
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def IsTheSame2(self) -> bool:
        """
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def IsTheSame3(self) -> bool:
        """
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

class Geom2dGcc_Circ2dTanCen:
    """
    This class implements the algorithms used to
    create 2d circles tangent to a curve and
    centered on a point.
    The arguments of all construction methods are :
    - The qualified element for the tangency constrains
    (QualifiedCurv).
    -The center point Pcenter.
    - A real Tolerance.
    Tolerance is only used in the limits cases.
    For example :
    We want to create a circle tangent to an EnclosedCurv C1
    with a tolerance Tolerance.
    If we did not used Tolerance it is impossible to
    find a solution in the following case : Pcenter is
    outside C1.
    With Tolerance we will give a solution if the distance
    between C1 and Pcenter is lower than or equal Tolerance/2.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Pcenter: nanoocp.Geom2d.Geom2d_Point | None, Tolerance: float) -> None:
        """
        Constructs one or more 2D circles tangential to the
        curve Qualified1 and centered on the point Pcenter.
        Tolerance is a tolerance criterion used by the algorithm
        to find a solution when, mathematically, the problem
        posed does not have a solution, but where there is
        numeric uncertainty attached to the arguments.
        Tolerance is only used in these algorithms in very
        specific cases where the center of the solution is very
        close to the circle to which it is tangential, and where the
        solution is thus a very small circle.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosing for a line).
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2dTanCen) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction algorithm does not fail
        (even if it finds no solution).
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached
        its numeric limits.
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
        Returns a circle, representing the solution of index
        Index computed by this algorithm.
        Warning
        This indexing simply provides a means of consulting the
        solutions. The index values are not associated with
        these solutions outside the context of the algorithm object.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails
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
        as unqualified with respect to the argument.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency1(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns true if the solution of index Index and the first
        argument of this algorithm are the same (i.e. there are 2
        identical circles).
        If Rarg is the radius of the first argument, Rsol is the
        radius of the solution and dist is the distance between
        the two centers, we consider the two circles to be
        identical if |Rarg - Rsol| and dist are less than
        or equal to the tolerance criterion given at the time of
        construction of this algorithm.
        NotDone is raised if the construction algorithm didn't succeed.
        OutOfRange is raised if Index is greater than the
        number of solutions.
        """

class Geom2dGcc_Circ2dTanCenGeo:
    """
    This class implements the algorithms used to
    create 2d circles tangent to a curve and
    centered on a point.
    The arguments of all construction methods are :
    - The qualified element for the tangency constrains
    (QualifiedCurv).
    -The center point Pcenter.
    - A real Tolerance.
    Tolerance is only used in the limits cases.
    For example :
    We want to create a circle tangent to an EnclosedCurv C1
    with a tolerance Tolerance.
    If we did not use Tolerance it is impossible to
    find a solution in the following case : Pcenter is
    outside C1.
    With Tolerance we will give a solution if the distance
    between C1 and Pcenter is lower than or equal Tolerance/2.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Pcenter: nanoocp.gp.gp_Pnt2d, Tolerance: float) -> None:
        """
        This method implements the algorithms used to
        create 2d circles tangent to a circle and
        centered on a point.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2dTanCenGeo) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of solutions and raises NotDone
        exception if the algorithm didn't succeed.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the
        context of the algorithm-object.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions or less than zero.
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position: ...

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

class Geom2dGcc_Circ2dTanOnRad:
    """
    This class implements the algorithms used to
    create a 2d circle tangent to a 2d entity,
    centered on a 2d entity and with a given radius.
    More than one argument must be a curve.
    The arguments of all construction methods are :
    - The qualified element for the tangency constrains
    (QualifiedCirc, QualifiedLin, QualifiedCurvPoints).
    - The Center element (circle, line, curve).
    - A real Tolerance.
    Tolerance is only used in the limits cases.
    For example :
    We want to create a circle tangent to an OutsideCurv Cu1
    centered on a line OnLine with a radius Radius and with
    a tolerance Tolerance.
    If we did not used Tolerance it is impossible to
    find a solution in the following case : OnLine is
    outside Cu1. There is no intersection point between Cu1
    and OnLine. The distance between the line and the
    circle is greater than Radius.
    With Tolerance we will give a solution if the
    distance between Cu1 and OnLine is lower than or
    equal Tolerance.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Radius: float, Tolerance: float) -> None:
        """
        Constructs one or more 2D circles of radius Radius,
        centered on the 2D curve OnCurv and:
        -   tangential to the curve Qualified1
        """

    @overload
    def __init__(self, Point1: nanoocp.Geom2d.Geom2d_Point | None, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Radius: float, Tolerance: float) -> None:
        """
        Constructs one or more 2D circles of radius Radius,
        centered on the 2D curve OnCurv and:
        passing through the point Point1.
        OnCurv is an adapted curve, i.e. an object which is an
        interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by the construction algorithm.
        Similarly, the qualified curve Qualified1 is created from
        an adapted curve.
        Adapted curves are created in the following way:
        occ::handle<Geom2d_Curve> myCurveOn = ... ;
        Geom2dAdaptor_Curve OnCurv ( myCurveOn ) ;
        The algorithm is then constructed with this object:
        occ::handle<Geom2d_Curve> myCurve1 = ...
        ;
        Geom2dAdaptor_Curve Adapted1 ( myCurve1 ) ;
        Geom2dGcc_QualifiedCurve
        Qualified1 = Geom2dGcc::Outside(Adapted1);
        double Radius = ... , Tolerance = ... ;
        Geom2dGcc_Circ2dTanOnRad
        myAlgo ( Qualified1 , OnCurv , Radius , Tolerance ) ;
        if ( myAlgo.IsDone() )
        { int Nbr = myAlgo.NbSolutions() ;
        gp_Circ2d Circ ;
        for ( int i = 1 ;
        i <= nbr ; i++ )
        { Circ = myAlgo.ThisSolution (i) ;
        ...
        }
        }
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2dTanOnRad) -> None: ...

    @overload
    def Results(self, Circ: nanoocp.GccAna.GccAna_Circ2dTanOnRad) -> None: ...

    @overload
    def Results(self, Circ: Geom2dGcc_Circ2dTanOnRadGeo) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction algorithm does not fail
        (even if it finds no solution).
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm which has reached
        its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of circles, representing solutions
        computed by this algorithm.
        Exceptions: StdFail_NotDone if the construction fails.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the context
        of the algorithm-object.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns the qualifier Qualif1 of the tangency argument
        for the solution of index Index computed by this algorithm.
        The returned qualifier is:
        -   that specified at the start of construction when the
        solutions are defined as enclosed, enclosing or
        outside with respect to the arguments, or
        -   that computed during construction (i.e. enclosed,
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
        Returns information about the tangency point between the
        result number Index and the first argument.
        ParSol is the intrinsic parameter of the point on the solution curv.
        ParArg is the intrinsic parameter of the point on the argument curv.
        PntSol is the tangency point on the solution curv.
        PntArg is the tangency point on the argument curv.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def CenterOn3(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Returns the center PntSol on the second argument (i.e.
        line or circle) of the solution of index Index computed by
        this algorithm.
        ParArg is the intrinsic parameter of the point on the argument curv.
        PntSol is the center point of the solution curv.
        PntArg is the projection of PntSol on the argument curv.
        Exceptions:
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns true if the solution of index Index and the first
        argument of this algorithm are the same (i.e. there are 2
        identical circles).
        If Rarg is the radius of the first argument, Rsol is the
        radius of the solution and dist is the distance between
        the two centers, we consider the two circles to be
        identical if |Rarg - Rsol| and dist are less than
        or equal to the tolerance criterion given at the time of
        construction of this algorithm.
        OutOfRange is raised if Index is greater than the number of solutions.
        notDone is raised if the construction algorithm did not succeed.
        """

class Geom2dGcc_Circ2dTanOnRadGeo:
    """
    This class implements the algorithms used to
    create a 2d circle tangent to a 2d entity,
    centered on a 2d entity and with a given radius.
    More than one argument must be a curve.
    The arguments of all construction methods are :
    - The qualified element for the tangency constrains
    (QualifiedCirc, QualifiedLin, QualifiedCurvPoints).
    - The Center element (circle, line, curve).
    - A real Tolerance.
    Tolerance is only used in the limits cases.
    For example :
    We want to create a circle tangent to an OutsideCurv Cu1
    centered on a line OnLine with a radius Radius and with
    a tolerance Tolerance.
    If we did not use Tolerance it is impossible to
    find a solution in the following case : OnLine is
    outside Cu1. There is no intersection point between Cu1
    and OnLine. The distance between the line and the
    circle is greater than Radius.
    With Tolerance we will give a solution if the
    distance between Cu1 and OnLine is lower than or
    equal Tolerance.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, OnLine: nanoocp.gp.gp_Lin2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a curve and centered on a 2d Line
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, OnCirc: nanoocp.gp.gp_Circ2d, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a curve and centered on a 2d Circle
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a circle and centered on a 2d curve
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedLin, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a 2d Line and centered on a 2d curve
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles tangent to a 2d curve and centered on a 2d curve
        with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, OnCurv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Radius: float, Tolerance: float) -> None:
        """
        This methods implements the algorithms used to create
        2d Circles passing through a 2d point and centered on a
        2d curve with a given radius.
        Tolerance is used to find solution in every limit cases.
        raises NegativeValue in case of NegativeRadius.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Circ2dTanOnRadGeo) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns True if the construction
        algorithm succeeded.
        """

    def NbSolutions(self) -> int:
        """
        This method returns the number of solutions.
        It raises NotDone if the construction algorithm
        didn't succeed.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the solution number Index and raises OutOfRange
        exception if Index is greater than the number of solutions.
        Be careful: the Index is only a way to get all the
        solutions, but is not associated to these outside the
        context of the algorithm-object.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def WhichQualifier(self, Index: int) -> nanoocp.GccEnt.GccEnt_Position: ...

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
        It raises NotDone if the construction algorithm
        didn't succeed.
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
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

    def IsTheSame1(self, Index: int) -> bool:
        """
        Returns True if the solution number Index is equal to
        the first argument and False in the other cases.
        It raises NotDone if the construction algorithm
        didn't succeed.
        It raises OutOfRange if Index is greater than the
        number of solutions.
        """

class Geom2dGcc_CurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_CurveTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> float: ...

    @staticmethod
    def EpsX(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Tol: float) -> float: ...

    @staticmethod
    def NbSamples(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> int: ...

    @staticmethod
    def Value(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, X: float) -> nanoocp.gp.gp_Pnt2d: ...

    @staticmethod
    def D1(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def D2(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d, N: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def D3(C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d, N: nanoocp.gp.gp_Vec2d, dN: nanoocp.gp.gp_Vec2d) -> None: ...

class Geom2dGcc_FunctionTanCirCu(nanoocp.math.math_FunctionWithDerivative):
    """
    This abstract class describes a Function of 1 Variable
    used to find a line tangent to a curve and a circle.
    """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ2d, Curv: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_FunctionTanCirCu) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """
        Computes the value of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        Computes the derivative of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        Computes the value and the derivative of the function F
        for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

class Geom2dGcc_FunctionTanCuCu(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    This abstract class describes a Function of 1 Variable
    used to find a line tangent to two curves.
    """

    @overload
    def __init__(self, Curv1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Curv2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, Circ1: nanoocp.gp.gp_Circ2d, Curv2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_FunctionTanCuCu) -> None: ...

    def InitDerivative(self, X: nanoocp.math.math_Vector, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, Tan1: nanoocp.gp.gp_Vec2d, Tan2: nanoocp.gp.gp_Vec2d, D21: nanoocp.gp.gp_Vec2d, D22: nanoocp.gp.gp_Vec2d) -> None: ...

    def NbVariables(self) -> int:
        """returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        Computes the value of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, Deriv: nanoocp.math.math_Matrix) -> bool:
        """
        Computes the derivative of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, Deriv: nanoocp.math.math_Matrix) -> bool:
        """
        Computes the value and the derivative of the function F
        for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

class Geom2dGcc_FunctionTanCuCuCu(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    This abstract class describes a set on N Functions of
    M independent variables.
    """

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C3: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C3: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Circ2d, C3: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, L2: nanoocp.gp.gp_Lin2d, C3: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, L2: nanoocp.gp.gp_Lin2d, C3: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C3: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_FunctionTanCuCuCu) -> None: ...

    def InitDerivative(self, X: nanoocp.math.math_Vector, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, Point3: nanoocp.gp.gp_Pnt2d, Tan1: nanoocp.gp.gp_Vec2d, Tan2: nanoocp.gp.gp_Vec2d, Tan3: nanoocp.gp.gp_Vec2d, D21: nanoocp.gp.gp_Vec2d, D22: nanoocp.gp.gp_Vec2d, D23: nanoocp.gp.gp_Vec2d) -> None: ...

    def NbVariables(self) -> int:
        """Returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """Returns the number of equations of the function."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """Computes the values of the Functions for the variable <X>."""

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """Returns the values of the derivatives for the variable <X>."""

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        Returns the values of the functions and the derivatives
        for the variable <X>.
        """

class Geom2dGcc_FunctionTanCuCuOnCu(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    This abstract class describes a set on N Functions of
    M independent variables.
    """

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnCi: nanoocp.gp.gp_Circ2d, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnCi: nanoocp.gp.gp_Circ2d, Rad: float) -> None: ...

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnCi: nanoocp.gp.gp_Circ2d, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, P2: nanoocp.gp.gp_Pnt2d, OnCi: nanoocp.gp.gp_Circ2d, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnLi: nanoocp.gp.gp_Lin2d, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnLi: nanoocp.gp.gp_Lin2d, Rad: float) -> None: ...

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnLi: nanoocp.gp.gp_Lin2d, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, P2: nanoocp.gp.gp_Pnt2d, OnLi: nanoocp.gp.gp_Lin2d, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnCu: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnCu: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Rad: float) -> None: ...

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, OnCu: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Rad: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, P1: nanoocp.gp.gp_Pnt2d, OnCu: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Rad: float) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_FunctionTanCuCuOnCu) -> None: ...

    def InitDerivative(self, X: nanoocp.math.math_Vector, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d, Point3: nanoocp.gp.gp_Pnt2d, Tan1: nanoocp.gp.gp_Vec2d, Tan2: nanoocp.gp.gp_Vec2d, Tan3: nanoocp.gp.gp_Vec2d, D21: nanoocp.gp.gp_Vec2d, D22: nanoocp.gp.gp_Vec2d, D23: nanoocp.gp.gp_Vec2d) -> None: ...

    def NbVariables(self) -> int:
        """Returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """Returns the number of equations of the function."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """Computes the values of the Functions for the variable <X>."""

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """Returns the values of the derivatives for the variable <X>."""

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        Returns the values of the functions and the derivatives
        for the variable <X>.
        """

class Geom2dGcc_FunctionTanCuPnt(nanoocp.math.math_FunctionWithDerivative):
    """
    This abstract class describes a Function of 1 Variable
    used to find a line tangent to a curve and passing
    through a point.
    """

    @overload
    def __init__(self, C: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Point: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_FunctionTanCuPnt) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """
        Computes the value of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        Computes the derivative of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        Computes the value and the derivative of the function F
        for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

class Geom2dGcc_FunctionTanObl(nanoocp.math.math_FunctionWithDerivative):
    """This class describe a function of a single variable."""

    @overload
    def __init__(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Dir: nanoocp.gp.gp_Dir2d) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_FunctionTanObl) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """
        Computes the value of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        Computes the derivative of the function F for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        Computes the value and the derivative of the function F
        for the variable X.
        It returns True if the computation is successfully done,
        False otherwise.
        """

class Geom2dGcc_IsParallel(nanoocp.Standard.Standard_DomainError):
    pass

class Geom2dGcc_Lin2d2Tan:
    """
    This class implements the algorithms used to
    create 2d lines tangent to 2 other elements which
    can be circles, curves or points.
    More than one argument must be a curve.
    Describes functions for building a 2D line:
    -   tangential to 2 curves, or
    -   tangential to a curve and passing through a point.
    A Lin2d2Tan object provides a framework for:
    -   defining the construction of 2D line(s),
    -   implementing the construction algorithm, and
    -   consulting the result(s).

    Note: Some constructors may check the type of the qualified argument
    and raise BadQualifier Error in case of incorrect couple (qualifier, curv).
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Qualified2: Geom2dGcc_QualifiedCurve, Tolang: float) -> None:
        """
        This class implements the algorithms used to create 2d
        line tangent to two curves.
        Tolang is used to determine the tolerance for the tangency points.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, ThePoint: nanoocp.gp.gp_Pnt2d, Tolang: float) -> None:
        """
        This class implements the algorithms used to create 2d
        lines passing through a point and tangent to a curve.
        Tolang is used to determine the tolerance for the tangency points.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, ThePoint: nanoocp.gp.gp_Pnt2d, Tolang: float, Param1: float) -> None:
        """
        This class implements the algorithms used to create 2d
        lines passing through a point and tangent to a curve.
        Tolang is used to determine the tolerance for the tangency points.
        Param2 is used for the initial guess on the curve.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, Qualified2: Geom2dGcc_QualifiedCurve, Tolang: float, Param1: float, Param2: float) -> None:
        """
        This class implements the algorithms used to create 2d
        line tangent to two curves.
        Tolang is used to determine the tolerance for the tangency points.
        Param1 is used for the initial guess on the first curve.
        Param2 is used for the initial guess on the second curve.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Lin2d2Tan) -> None: ...

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
        Returns the number of lines, representing solutions computed by this algorithm.
        Exceptions StdFail_NotDone if the construction fails.R
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns a line, representing the solution of index Index computed by this algorithm.
        Warning
        This indexing simply provides a means of consulting the
        solutions. The index values are not associated with
        these solutions outside the context of the algorithm object.
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
        result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

    def Tangency2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
        """

class Geom2dGcc_Lin2d2TanIter:
    """
    This class implements the algorithms used to
    create 2d lines tangent to 2 other elements which
    can be circles, curves or points.
    More than one argument must be a curve.

    Note: Some constructors may check the type of the qualified argument
    and raise BadQualifier Error in case of incorrect couple (qualifier,
    curv).
    For example: "EnclosedCirc".
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, ThePoint: nanoocp.gp.gp_Pnt2d, Param1: float, Tolang: float) -> None:
        """
        This class implements the algorithms used to create 2d
        lines passing through a point and tangent to a curve.
        Tolang is used to determine the tolerance for the
        tangency points.
        Param2 is used for the initial guess on the curve.
        """

    @overload
    def __init__(self, Qualified1: nanoocp.GccEnt.GccEnt_QualifiedCirc, Qualified2: Geom2dGcc_QCurve, Param2: float, Tolang: float) -> None:
        """
        This class implements the algorithms used to create 2d
        line tangent to a circle and to a curve.
        Tolang is used to determine the tolerance for the
        tangency points.
        Param2 is used for the initial guess on the curve.
        Exception BadQualifier is raised in the case of
        EnclosedCirc
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, Qualified2: Geom2dGcc_QCurve, Param1: float, Param2: float, Tolang: float) -> None:
        """
        This class implements the algorithms used to create 2d
        line tangent to two curves.
        Tolang is used to determine the tolerance for the
        tangency points.
        Param1 is used for the initial guess on the first curve.
        Param2 is used for the initial guess on the second curve.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Lin2d2TanIter) -> None: ...

    def IsDone(self) -> bool:
        """
        This methode returns true when there is a solution
        and false in the other cases.
        """

    def ThisSolution(self) -> nanoocp.gp.gp_Lin2d:
        """Returns the solution."""

    def WhichQualifier(self) -> tuple[nanoocp.GccEnt.GccEnt_Position, nanoocp.GccEnt.GccEnt_Position]: ...

    def Tangency1(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns information about the tangency point between the
        result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on
        the argument curv.
        """

    def Tangency2(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]: ...

class Geom2dGcc_Lin2dTanObl:
    """
    This class implements the algorithms used to
    create 2d line tangent to a curve QualifiedCurv and
    doing an angle Angle with a line TheLin.
    The angle must be in Radian.
    Describes functions for building a 2D line making a given
    angle with a line and tangential to a curve.
    A Lin2dTanObl object provides a framework for:
    -   defining the construction of 2D line(s),
    -   implementing the construction algorithm, and
    -   consulting the result(s).
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, TheLin: nanoocp.gp.gp_Lin2d, TolAng: float, Angle: float) -> None:
        """
        This class implements the algorithm used to
        create 2d line tangent to a curve and doing an
        angle Angle with the line TheLin.
        Angle must be in Radian.
        Tolang is the angular tolerance.
        """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QualifiedCurve, TheLin: nanoocp.gp.gp_Lin2d, TolAng: float, Param1: float, Angle: float) -> None:
        """
        This class implements the algorithm used to
        create 2d line tangent to a curve and doing an
        angle Angle with the line TheLin.
        Angle must be in Radian.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolang is the angular tolerance.
        Warning
        An iterative algorithm is used if Qualified1 is more
        complex than a line or a circle. In such cases, the
        algorithm constructs only one solution.
        Exceptions
        GccEnt_BadQualifier if a qualifier is inconsistent with
        the argument it qualifies (for example, enclosed for a circle).
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Lin2dTanObl) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction algorithm does not fail
        (even if it finds no solution).
        Note: IsDone protects against a failure arising from a
        more internal intersection algorithm, which has reached its numeric limits.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of lines, representing solutions computed by this algorithm.
        Exceptions
        StdFail_NotDone if the construction fails.
        """

    def ThisSolution(self, Index: int) -> nanoocp.gp.gp_Lin2d:
        """
        Returns a line, representing the solution of index Index
        computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        StdFail_NotDone if the construction fails.
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
        result and the first argument.
        ParSol is the intrinsic parameter of the point PntSol on
        the solution curv.
        ParArg is the intrinsic parameter of the point PntSol on
        the argument curv.
        """

    def Intersection2(self, Index: int, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns the point of intersection PntSol between the
        solution of index Index and the second argument (the line) of this algorithm.
        ParSol is the parameter of the point PntSol on the
        solution. ParArg is the parameter of the point PntSol on the second argument (the line).
        Exceptions
        StdFail_NotDone if the construction fails.
        Geom2dGcc_IsParallel if the solution and the second
        argument (the line) are parallel.
        Standard_OutOfRange if Index is less than zero or
        greater than the number of solutions computed by this algorithm.
        """

class Geom2dGcc_Lin2dTanOblIter:
    """
    This class implements the algorithms used to
    create 2d line tangent to a curve QualifiedCurv and
    doing an angle Angle with a line TheLin.
    The angle must be in Radian.
    """

    @overload
    def __init__(self, Qualified1: Geom2dGcc_QCurve, TheLin: nanoocp.gp.gp_Lin2d, Param1: float, TolAng: float, Angle: float = 0.0) -> None:
        """
        This class implements the algorithm used to
        create 2d line tangent to a curve and doing an
        angle Angle with the line TheLin.
        Angle must be in Radian.
        Param2 is the initial guess on the curve QualifiedCurv.
        Tolang is the angular tolerance.
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_Lin2dTanOblIter) -> None: ...

    def IsDone(self) -> bool:
        """
        This method returns true when there is a solution
        and false in the other cases.
        """

    def ThisSolution(self) -> nanoocp.gp.gp_Lin2d: ...

    def WhichQualifier(self) -> nanoocp.GccEnt.GccEnt_Position: ...

    def Tangency1(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]: ...

    def Intersection2(self, PntSol: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]: ...

    def IsParallel2(self) -> bool: ...

class Geom2dGcc_QCurve:
    """Creates a qualified 2d line."""

    @overload
    def __init__(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Qualifier: nanoocp.GccEnt.GccEnt_Position) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dGcc_QCurve) -> None: ...

    def Qualified(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve: ...

    def Qualifier(self) -> nanoocp.GccEnt.GccEnt_Position: ...

    def IsUnqualified(self) -> bool:
        """
        Returns true if the solution is unqualified and false in the
        other cases.
        """

    def IsEnclosing(self) -> bool:
        """
        Returns true if the solution is Enclosing the Curv and false in
        the other cases.
        """

    def IsEnclosed(self) -> bool:
        """
        Returns true if the solution is Enclosed in the Curv and false in
        the other cases.
        """

    def IsOutside(self) -> bool:
        """
        Returns true if the solution is Outside the Curv and false in
        the other cases.
        """

class Geom2dGcc_QualifiedCurve:
    """
    Describes functions for building a qualified 2D curve.
    A qualified 2D curve is a curve with a qualifier which
    specifies whether the solution of a construction
    algorithm using the qualified curve (as an argument):
    -   encloses the curve, or
    -   is enclosed by the curve, or
    -   is built so that both the curve and it are external to one another, or
    -   is undefined (all solutions apply).
    """

    @overload
    def __init__(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Qualifier: nanoocp.GccEnt.GccEnt_Position) -> None:
        """
        Constructs a qualified curve by assigning the qualifier
        Qualifier to the curve Curve. Qualifier may be:
        -   GccEnt_enclosing if the solution of a construction
        algorithm using the qualified curve encloses the curve, or
        -   GccEnt_enclosed if the solution is enclosed by the curve, or
        -   GccEnt_outside if both the solution and the curve
        are external to one another, or
        -   GccEnt_unqualified if all solutions apply.
        Note: The interior of a curve is defined as the left-hand
        side of the curve in relation to its orientation.
        Warning
        Curve is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by a computation algorithm.
        The adapted curve is created in the following way:
        occ::handle<Geom2d_Curve> mycurve = ... ;
        Geom2dAdaptor_Curve Curve ( mycurve ) ;
        The qualified curve is then constructed with this object:
        GccEnt_Position myQualif = GccEnt_outside ;
        Geom2dGcc_QualifiedCurve myQCurve ( Curve, myQualif );
        is private;
        """

    @overload
    def __init__(self, theOther: Geom2dGcc_QualifiedCurve) -> None: ...

    def Qualified(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """
        Returns a 2D curve to which the qualifier is assigned.
        Warning
        The returned curve is an adapted curve, i.e. an object
        which is an interface between:
        -   the services provided by a 2D curve from the package Geom2d,
        -   and those required on the curve by a computation algorithm.
        The Geom2d curve on which the adapted curve is
        based can be obtained in the following way:
        myQualifiedCurve = ... ;
        Geom2dAdaptor_Curve myAdaptedCurve = myQualifiedCurve.Qualified();
        occ::handle<Geom2d_Curve> = myAdaptedCurve.Curve();
        """

    def Qualifier(self) -> nanoocp.GccEnt.GccEnt_Position:
        """
        Returns
        - the qualifier of this qualified curve if it is enclosing,
        enclosed or outside, or
        -   GccEnt_noqualifier if it is unqualified.
        """

    def IsUnqualified(self) -> bool:
        """
        Returns true if the solution is unqualified and false in the other cases.
        """

    def IsEnclosing(self) -> bool:
        """
        It returns true if the solution is Enclosing the Curv and false in
        the other cases.
        """

    def IsEnclosed(self) -> bool:
        """
        It returns true if the solution is Enclosed in the Curv and false in
        the other cases.
        """

    def IsOutside(self) -> bool:
        """
        It returns true if the solution is Outside the Curv and false in
        the other cases.
        """
