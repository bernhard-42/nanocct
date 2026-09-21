"""OCCT package Law (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard


class Law:
    """Multiple services concerning 1d functions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Law) -> None: ...

    @overload
    @staticmethod
    def MixBnd(Lin: Law_Linear | None) -> Law_BSpFunc:
        """
        This algorithm searches the knot values corresponding to the
        splitting of a given B-spline law into several arcs with
        the same continuity. The continuity order is given at the
        construction time.
        Builds a 1d bspline that is near from Lin with null
        derivatives at the extremities.
        """

    @overload
    @staticmethod
    def MixBnd(Degree: int, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Lin: Law_Linear | None) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Builds the poles of the 1d bspline that is near from
        Lin with null derivatives at the extremities.
        """

    @staticmethod
    def MixTgt(Degree: int, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NulOnTheRight: bool, Index: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Builds the poles of the 1d bspline that is null on the
        right side of Knots(Index) (on the left if
        NulOnTheRight is false) and that is like a
        t*(1-t)(1-t) curve on the left side of Knots(Index)
        (on the right if NulOnTheRight is false). The result
        curve is C1 with a derivative equal to 1. at first
        parameter (-1 at last parameter if NulOnTheRight is
        false).
        Warning: Mults(Index) must greater or equal to degree-1.
        """

    @staticmethod
    def Reparametrize(Curve: nanoocp.Adaptor3d.Adaptor3d_Curve, First: float, Last: float, HasDF: bool, HasDL: bool, DFirst: float, DLast: float, Rev: bool, NbPoints: int) -> Law_BSpline:
        """
        Computes a 1d curve to reparametrize a curve. Its an
        interpolation of NbPoints points calculated at quasi
        constant abscissa.
        """

    @staticmethod
    def Scale(First: float, Last: float, HasF: bool, HasL: bool, VFirst: float, VLast: float) -> Law_BSpline:
        """
        Computes a 1d curve to scale a field of tangency.
        Value is 1. for t = (First+Last)/2 .
        If HasFirst value for t = First is VFirst (null derivative).
        If HasLast value for t = Last is VLast (null derivative).

        1.                   _
        _/ \\_
        __/     \\__
        /
        VFirst    ____/
        VLast                        \\____
        First                    Last
        """

    @staticmethod
    def ScaleCub(First: float, Last: float, HasF: bool, HasL: bool, VFirst: float, VLast: float) -> Law_BSpline: ...

class Law_Function(nanoocp.Standard.Standard_Transient):
    """Root class for evolution laws."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        The array must provide enough room to accommodate for the parameters,
        i.e. T.Length() > NbIntervals()
        """

    def Value(self, X: float) -> float:
        """Returns the value of the function at the point of parameter X."""

    def D1(self, X: float) -> tuple[float, float]:
        """
        Returns the value F and the first derivative D of the
        function at the point of parameter X.
        """

    def D2(self, X: float) -> tuple[float, float, float]:
        """
        Returns the value, first and second derivatives
        at parameter X.
        """

    def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function:
        """
        Returns a law equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        It is usfule to determines the derivatives
        in these values <First> and <Last> if
        the Law is not Cn.
        """

    def Bounds(self) -> tuple[float, float]:
        """Returns the parametric bounds of the function."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_BSpFunc(Law_Function):
    """
    Law Function based on a BSpline curve 1d. Package
    methods and classes are implemented in package Law
    to construct the basis curve with several
    constraints.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: Law_BSpline | None, First: float, Last: float) -> None: ...

    @overload
    def __init__(self, theOther: Law_BSpFunc) -> None: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        The array must provide enough room to accommodate for the parameters, i.e. T.Length() >
        NbIntervals()
        """

    def Value(self, X: float) -> float: ...

    def D1(self, X: float) -> tuple[float, float]: ...

    def D2(self, X: float) -> tuple[float, float, float]: ...

    def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function:
        """
        Returns a law equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        It is usfule to determines the derivatives
        in these values <First> and <Last> if
        the Law is not Cn.
        """

    def Bounds(self) -> tuple[float, float]: ...

    def Curve(self) -> Law_BSpline: ...

    def SetCurve(self, C: Law_BSpline | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_BSpline(nanoocp.Standard.Standard_Transient):
    """
    Definition of the 1D B_spline curve.

    Uniform  or non-uniform
    Rational or non-rational
    Periodic or non-periodic

    A b-spline curve is defined by:

    The Degree (up to 25)

    The Poles (and the weights if it is rational)

    The Knots and Multiplicities

    The knot vector is an increasing sequence of
    reals without repetition. The multiplicities are
    the repetition of the knots.

    If the knots are regularly spaced (the difference
    of two consecutive knots is a constant), the
    knots repartition is:

    - Uniform if all multiplicities are 1.

    - Quasi-uniform if all multiplicities are 1
    but the first and the last which are Degree+1.

    - PiecewiseBezier if all multiplicities are
    Degree but the first and the last which are
    Degree+1.

    The curve may be periodic.

    On a periodic curve if there are k knots and p
    poles. the period is knot(k) - knot(1)

    the poles and knots are infinite vectors with:

    knot(i+k) = knot(i) + period

    pole(i+p) = pole(i)

    References :
    . A survey of curve and surface methods in CADG Wolfgang BOHM
    CAGD 1 (1984)
    . On de Boor-like algorithms and blossoming Wolfgang BOEHM
    cagd 5 (1988)
    . Blossoming and knot insertion algorithms for B-spline curves
    Ronald N. GOLDMAN
    . Modelisation des surfaces en CAO, Henri GIAUME Peugeot SA
    . Curves and Surfaces for Computer Aided Geometric Design,
    a practical guide Gerald Farin
    """

    @overload
    def __init__(self, Poles: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Multiplicities: nanoocp.NCollection.NCollection_Array1[int], Degree: int, Periodic: bool = False) -> None:
        """
        Creates a non-rational B_spline curve on the
        basis <Knots, Multiplicities> of degree <Degree>.
        """

    @overload
    def __init__(self, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Multiplicities: nanoocp.NCollection.NCollection_Array1[int], Degree: int, Periodic: bool = False) -> None:
        """
        Creates a rational B_spline curve on the basis
        <Knots, Multiplicities> of degree <Degree>.
        """

    @overload
    def __init__(self, theOther: Law_BSpline) -> None: ...

    def IncreaseDegree(self, Degree: int) -> None:
        """
        Increase the degree to <Degree>. Nothing is done
        if <Degree> is lower or equal to the current
        degree.
        """

    @overload
    def IncreaseMultiplicity(self, Index: int, M: int) -> None:
        """
        Increases the multiplicity of the knot <Index> to
        <M>.

        If <M> is lower or equal to the current multiplicity
        nothing is done. If <M> is higher than the degree
        the degree is used.
        If <Index> is not in [FirstUKnotIndex, LastUKnotIndex]
        """

    @overload
    def IncreaseMultiplicity(self, I1: int, I2: int, M: int) -> None:
        """
        Increases the multiplicities of the knots in
        [I1,I2] to <M>.

        For each knot if <M> is lower or equal to the
        current multiplicity nothing is done. If <M> is
        higher than the degree the degree is used.
        If <I1,I2> are not in [FirstUKnotIndex, LastUKnotIndex]
        """

    def IncrementMultiplicity(self, I1: int, I2: int, M: int) -> None:
        """
        Increment the multiplicities of the knots in
        [I1,I2] by <M>.

        If <M> is not positive nothing is done.

        For each knot the resulting multiplicity is
        limited to the Degree.
        If <I1,I2> are not in [FirstUKnotIndex, LastUKnotIndex]
        """

    def InsertKnot(self, U: float, M: int = 1, ParametricTolerance: float = 0.0, Add: bool = True) -> None:
        """
        Inserts a knot value in the sequence of knots.
        If <U> is an existing knot the multiplicity is
        increased by <M>.

        If U is not on the parameter range nothing is
        done.

        If the multiplicity is negative or null nothing is
        done. The new multiplicity is limited to the
        degree.

        The tolerance criterion for knots equality is
        the max of Epsilon(U) and ParametricTolerance.
        """

    def InsertKnots(self, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], ParametricTolerance: float = 0.0, Add: bool = False) -> None:
        """
        Inserts a set of knots values in the sequence of
        knots.

        For each U = Knots(i), M = Mults(i)

        If <U> is an existing knot the multiplicity is
        increased by <M> if <Add> is True, increased to
        <M> if <Add> is False.

        If U is not on the parameter range nothing is
        done.

        If the multiplicity is negative or null nothing is
        done. The new multiplicity is limited to the
        degree.

        The tolerance criterion for knots equality is
        the max of Epsilon(U) and ParametricTolerance.
        """

    def RemoveKnot(self, Index: int, M: int, Tolerance: float) -> bool:
        """
        Decrement the knots multiplicity to <M>. If M is
        0 the knot is removed. The Poles sequence is
        modified.

        As there are two ways to compute the new poles the
        average is computed if the distance is lower than
        the <Tolerance>, else False is returned.

        A low tolerance is used to prevent the modification
        of the curve.

        A high tolerance is used to "smooth" the curve.

        Raised if Index is not in the range
        [FirstUKnotIndex, LastUKnotIndex]
        pole insertion and pole removing
        this operation is limited to the Uniform or QuasiUniform
        BSplineCurve. The knot values are modified. If the BSpline is
        NonUniform or Piecewise Bezier an exception Construction error
        is raised.
        """

    def Reverse(self) -> None:
        """
        Changes the direction of parametrization of <me>. The Knot
        sequence is modified, the FirstParameter and the
        LastParameter are not modified. The StartPoint of the
        initial curve becomes the EndPoint of the reversed curve
        and the EndPoint of the initial curve becomes the StartPoint
        of the reversed curve.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Returns the parameter on the reversed curve for
        the point of parameter U on <me>.

        returns UFirst + ULast - U
        """

    def Segment(self, U1: float, U2: float) -> None:
        """
        Segments the curve between U1 and U2.
        The control points are modified, the first and the last point
        are not the same.
        Warnings :
        Even if <me> is not closed it can become closed after the
        segmentation for example if U1 or U2 are out of the bounds
        of the curve <me> or if the curve makes loop.
        After the segmentation the length of a curve can be null.
        raises if U2 < U1.
        """

    @overload
    def SetKnot(self, Index: int, K: float) -> None:
        """
        Changes the knot of range Index.
        The multiplicity of the knot is not modified.
        Raised if K >= Knots(Index+1) or K <= Knots(Index-1).
        Raised if Index < 1 || Index > NbKnots
        """

    @overload
    def SetKnot(self, Index: int, K: float, M: int) -> None:
        """
        Changes the knot of range Index with its multiplicity.
        You can increase the multiplicity of a knot but it is
        not allowed to decrease the multiplicity of an existing knot.

        Raised if K >= Knots(Index+1) or K <= Knots(Index-1).
        Raised if M is greater than Degree or lower than the previous
        multiplicity of knot of range Index.
        Raised if Index < 1 || Index > NbKnots
        """

    def SetKnots(self, K: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Changes all the knots of the curve
        The multiplicity of the knots are not modified.

        Raised if there is an index such that K (Index+1) <= K (Index).

        Raised if K.Lower() < 1 or K.Upper() > NbKnots
        """

    def PeriodicNormalization(self) -> float:
        """
        returns the parameter normalized within
        the period if the curve is periodic : otherwise
        does not do anything
        """

    def SetPeriodic(self) -> None:
        """
        Makes a closed B-spline into a periodic curve. The curve is
        periodic if the knot sequence is periodic and if the curve is
        closed (The tolerance criterion is Resolution from gp).
        The period T is equal to Knot(LastUKnotIndex) -
        Knot(FirstUKnotIndex). A periodic B-spline can be uniform
        or not.
        Raised if the curve is not closed.
        """

    def SetOrigin(self, Index: int) -> None:
        """
        Set the origin of a periodic curve at Knot(index)
        KnotVector and poles are modified.
        Raised if the curve is not periodic
        Raised if index not in the range
        [FirstUKnotIndex , LastUKnotIndex]
        """

    def SetNotPeriodic(self) -> None:
        """
        Makes a non periodic curve. If the curve was non periodic
        the curve is not modified.
        """

    @overload
    def SetPole(self, Index: int, P: float) -> None:
        """
        Substitutes the Pole of range Index with P.

        Raised if Index < 1 || Index > NbPoles
        """

    @overload
    def SetPole(self, Index: int, P: float, Weight: float) -> None:
        """
        Substitutes the pole and the weight of range Index.
        If the curve <me> is not rational it can become rational
        If the curve was rational it can become non rational

        Raised if Index < 1 || Index > NbPoles
        Raised if Weight <= 0.0
        """

    def SetWeight(self, Index: int, Weight: float) -> None:
        """
        Changes the weight for the pole of range Index.
        If the curve was non rational it can become rational.
        If the curve was rational it can become non rational.

        Raised if Index < 1 || Index > NbPoles
        Raised if Weight <= 0.0
        """

    def IsCN(self, N: int) -> bool:
        """
        Returns the continuity of the curve, the curve is at least C0.
        Raised if N < 0.
        """

    def IsClosed(self) -> bool:
        """
        Returns true if the distance between the first point and the
        last point of the curve is lower or equal to Resolution
        from package gp.
        Warnings :
        The first and the last point can be different from the first
        pole and the last pole of the curve.
        """

    def IsPeriodic(self) -> bool:
        """Returns True if the curve is periodic."""

    def IsRational(self) -> bool:
        """
        Returns True if the weights are not identical.
        The tolerance criterion is Epsilon of the class Real.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the global continuity of the curve :
        C0 : only geometric continuity,
        C1 : continuity of the first derivative all along the Curve,
        C2 : continuity of the second derivative all along the Curve,
        C3 : continuity of the third derivative all along the Curve,
        CN : the order of continuity is infinite.
        For a B-spline curve of degree d if a knot Ui has a
        multiplicity p the B-spline curve is only Cd-p continuous
        at Ui. So the global continuity of the curve can't be greater
        than Cd-p where p is the maximum multiplicity of the interior
        Knots. In the interior of a knot span the curve is infinitely
        continuously differentiable.
        """

    def Degree(self) -> int:
        """Computation of value and derivatives"""

    def Value(self, U: float) -> float: ...

    def D0(self, U: float) -> float: ...

    def D1(self, U: float) -> tuple[float, float]: ...

    def D2(self, U: float) -> tuple[float, float, float]: ...

    def D3(self, U: float) -> tuple[float, float, float, float]: ...

    def DN(self, U: float, N: int) -> float:
        """
        The following functions computes the point of parameter U and
        the derivatives at this point on the B-spline curve arc
        defined between the knot FromK1 and the knot ToK2. U can be
        out of bounds [Knot (FromK1), Knot (ToK2)] but for the
        computation we only use the definition of the curve between
        these two knots. This method is useful to compute local
        derivative, if the order of continuity of the whole curve is
        not greater enough. Inside the parametric domain Knot
        (FromK1), Knot (ToK2) the evaluations are the same as if we
        consider the whole definition of the curve. Of course the
        evaluations are different outside this parametric domain.
        """

    def LocalValue(self, U: float, FromK1: int, ToK2: int) -> float: ...

    def LocalD0(self, U: float, FromK1: int, ToK2: int) -> float: ...

    def LocalD1(self, U: float, FromK1: int, ToK2: int) -> tuple[float, float]: ...

    def LocalD2(self, U: float, FromK1: int, ToK2: int) -> tuple[float, float, float]: ...

    def LocalD3(self, U: float, FromK1: int, ToK2: int) -> tuple[float, float, float, float]: ...

    def LocalDN(self, U: float, FromK1: int, ToK2: int, N: int) -> float: ...

    def EndPoint(self) -> float:
        """
        Returns the last point of the curve.
        Warnings :
        The last point of the curve is different from the last
        pole of the curve if the multiplicity of the last knot
        is lower than Degree.
        """

    def FirstUKnotIndex(self) -> int:
        """
        For a B-spline curve the first parameter (which gives the start
        point of the curve) is a knot value but if the multiplicity of
        the first knot index is lower than Degree + 1 it is not the
        first knot of the curve. This method computes the index of the
        knot corresponding to the first parameter.
        """

    def FirstParameter(self) -> float:
        """
        Computes the parametric value of the start point of the curve.
        It is a knot value.
        """

    def Knot(self, Index: int) -> float:
        """
        Returns the knot of range Index. When there is a knot
        with a multiplicity greater than 1 the knot is not repeated.
        The method Multiplicity can be used to get the multiplicity
        of the Knot.
        Raised if Index < 1 or Index > NbKnots
        """

    def Knots(self, K: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        returns the knot values of the B-spline curve;

        Raised if the length of K is not equal to the number of knots.
        """

    def KnotSequence(self, K: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the knots sequence.
        In this sequence the knots with a multiplicity greater than 1
        are repeated.
        Example :
        K = {k1, k1, k1, k2, k3, k3, k4, k4, k4}

        Raised if the length of K is not equal to NbPoles + Degree + 1
        """

    def KnotDistribution(self) -> nanoocp.GeomAbs.GeomAbs_BSplKnotDistribution:
        """
        Returns NonUniform or Uniform or QuasiUniform or PiecewiseBezier.
        If all the knots differ by a positive constant from the
        preceding knot the BSpline Curve can be :
        - Uniform if all the knots are of multiplicity 1,
        - QuasiUniform if all the knots are of multiplicity 1 except for
        the first and last knot which are of multiplicity Degree + 1,
        - PiecewiseBezier if the first and last knots have multiplicity
        Degree + 1 and if interior knots have multiplicity Degree
        A piecewise Bezier with only two knots is a BezierCurve.
        else the curve is non uniform.
        The tolerance criterion is Epsilon from class Real.
        """

    def LastUKnotIndex(self) -> int:
        """
        For a BSpline curve the last parameter (which gives the
        end point of the curve) is a knot value but if the
        multiplicity of the last knot index is lower than
        Degree + 1 it is not the last knot of the curve. This
        method computes the index of the knot corresponding to
        the last parameter.
        """

    def LastParameter(self) -> float:
        """
        Computes the parametric value of the end point of the curve.
        It is a knot value.
        """

    def LocateU(self, U: float, ParametricTolerance: float, WithKnotRepetition: bool = False) -> tuple[int, int]:
        """
        Locates the parametric value U in the sequence of knots.
        If "WithKnotRepetition" is True we consider the knot's
        representation with repetition of multiple knot value,
        otherwise we consider the knot's representation with
        no repetition of multiple knot values.
        Knots (I1) <= U <= Knots (I2)
        . if I1 = I2 U is a knot value (the tolerance criterion
        ParametricTolerance is used).
        . if I1 < 1 => U < Knots (1) - std::abs(ParametricTolerance)
        . if I2 > NbKnots => U > Knots (NbKnots) + std::abs(ParametricTolerance)
        """

    def Multiplicity(self, Index: int) -> int:
        """
        Returns the multiplicity of the knots of range Index.
        Raised if Index < 1 or Index > NbKnots
        """

    def Multiplicities(self, M: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Returns the multiplicity of the knots of the curve.

        Raised if the length of M is not equal to NbKnots.
        """

    def NbKnots(self) -> int:
        """
        Returns the number of knots. This method returns the number of
        knot without repetition of multiple knots.
        """

    def NbPoles(self) -> int:
        """Returns the number of poles"""

    def Pole(self, Index: int) -> float:
        """
        Returns the pole of range Index.
        Raised if Index < 1 or Index > NbPoles.
        """

    def Poles(self, P: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the poles of the B-spline curve;

        Raised if the length of P is not equal to the number of poles.
        """

    def StartPoint(self) -> float:
        """
        Returns the start point of the curve.
        Warnings :
        This point is different from the first pole of the curve if the
        multiplicity of the first knot is lower than Degree.
        """

    def Weight(self, Index: int) -> float:
        """
        Returns the weight of the pole of range Index .
        Raised if Index < 1 or Index > NbPoles.
        """

    def Weights(self, W: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the weights of the B-spline curve;

        Raised if the length of W is not equal to NbPoles.
        """

    @staticmethod
    def MaxDegree() -> int:
        """
        Returns the value of the maximum degree of the normalized
        B-spline basis functions in this package.
        """

    def MovePointAndTangent(self, U: float, NewValue: float, Derivative: float, Tolerance: float, StartingCondition: int, EndingCondition: int) -> int:
        """
        Changes the value of the Law at parameter U to NewValue.
        and makes its derivative at U be derivative.
        StartingCondition = -1 means first can move
        EndingCondition   = -1 means last point can move
        StartingCondition = 0 means the first point cannot move
        EndingCondition   = 0 means the last point cannot move
        StartingCondition = 1 means the first point and tangent cannot move
        EndingCondition   = 1 means the last point and tangent cannot move
        and so forth
        ErrorStatus != 0 means that there are not enough degree of freedom
        with the constrain to deform the curve accordingly
        """

    def Resolution(self, Tolerance3D: float) -> float:
        """
        given Tolerance3D returns UTolerance
        such that if f(t) is the curve we have
        | t1 - t0| < Utolerance ===>
        |f(t1) - f(t0)| < Tolerance3D
        """

    def Copy(self) -> Law_BSpline: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_BSplineKnotSplitting:
    """
    For a B-spline curve the discontinuities are localised at the
    knot values and between two knots values the B-spline is
    infinitely continuously differentiable.
    At a knot of range index the continuity is equal to:
    Degree - Mult (Index) where Degree is the degree of the
    basis B-spline functions and Mult the multiplicity of the knot
    of range Index.
    If for your computation you need to have B-spline curves with a
    minima of continuity it can be interesting to know between which
    knot values, a B-spline curve arc, has a continuity of given order.
    This algorithm computes the indexes of the knots where you should
    split the curve, to obtain arcs with a constant continuity given
    at the construction time. The splitting values are in the range
    [FirstUKnotValue, LastUKnotValue] (See class B-spline curve from
    package Geom).
    If you just want to compute the local derivatives on the curve you
    don't need to create the B-spline curve arcs, you can use the
    functions LocalD1, LocalD2, LocalD3, LocalDN of the class
    BSplineCurve.
    """

    @overload
    def __init__(self, BasisLaw: Law_BSpline | None, ContinuityRange: int) -> None:
        """
        Locates the knot values which correspond to the segmentation of
        the curve into arcs with a continuity equal to ContinuityRange.

        Raised if ContinuityRange is not greater or equal zero.
        """

    @overload
    def __init__(self, theOther: Law_BSplineKnotSplitting) -> None: ...

    def NbSplits(self) -> int:
        """Returns the number of knots corresponding to the splitting."""

    def Splitting(self, SplitValues: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Returns the indexes of the BSpline curve knots corresponding to
        the splitting.

        Raised if the length of SplitValues is not equal to NbSPlit.
        """

    def SplitValue(self, Index: int) -> int:
        """
        Returns the index of the knot corresponding to the splitting
        of range Index.

        Raised if Index < 1 or Index > NbSplits
        """

class Law_Composite(Law_Function):
    """
    Loi composite constituee d une liste de lois de
    ranges consecutifs.
    Cette implementation un peu lourde permet de reunir
    en une seule loi des portions de loi construites de
    facon independantes (par exemple en interactif) et
    de lancer le walking d un coup a l echelle d une
    ElSpine.
    CET OBJET REPOND DONC A UN PROBLEME D IMPLEMENTATION
    SPECIFIQUE AUX CONGES!!!
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty Law"""

    @overload
    def __init__(self, First: float, Last: float, Tol: float) -> None:
        """Construct an empty, trimmed Law"""

    @overload
    def __init__(self, theOther: Law_Composite) -> None: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        The array must provide enough room to accommodate for the parameters,
        i.e. T.Length() > NbIntervals()
        """

    def Value(self, X: float) -> float:
        """Returns the value at parameter X."""

    def D1(self, X: float) -> tuple[float, float]:
        """Returns the value and the first derivative at parameter X."""

    def D2(self, X: float) -> tuple[float, float, float]:
        """
        Returns the value, first and second derivatives
        at parameter X.
        """

    def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function:
        """
        Returns a law equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        It is usfule to determines the derivatives
        in these values <First> and <Last> if
        the Law is not Cn.
        """

    def Bounds(self) -> tuple[float, float]:
        """Returns the parametric bounds of the function."""

    def ChangeElementaryLaw(self, W: float) -> Law_Function:
        """
        Returns the elementary function of the composite used
        to compute at parameter W.
        """

    def ChangeLaws(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Law.Law_Function]: ...

    def IsPeriodic(self) -> bool: ...

    def SetPeriodic(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_Constant(Law_Function):
    """Loi constante"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Law_Constant) -> None: ...

    def Set(self, Radius: float, PFirst: float, PLast: float) -> None:
        """Set the radius and the range of the constant Law."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """Returns 1"""

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Value(self, X: float) -> float:
        """Returns the value at parameter X."""

    def D1(self, X: float) -> tuple[float, float]:
        """Returns the value and the first derivative at parameter X."""

    def D2(self, X: float) -> tuple[float, float, float]:
        """
        Returns the value, first and second derivatives
        at parameter X.
        """

    def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function: ...

    def Bounds(self) -> tuple[float, float]:
        """Returns the parametric bounds of the function."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_Interpol(Law_BSpFunc):
    """
    Provides an evolution law that interpolates a set
    of parameter and value pairs (wi, radi)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty interpolative evolution law.
        The function Set is used to define the law.
        """

    @overload
    def __init__(self, theOther: Law_Interpol) -> None: ...

    @overload
    def Set(self, ParAndRad: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Periodic: bool = False) -> None:
        """
        Defines this evolution law by interpolating the set of 2D
        points ParAndRad. The Y coordinate of a point of
        ParAndRad is the value of the function at the parameter
        point given by its X coordinate.
        If Periodic is true, this function is assumed to be periodic.
        Warning
        -   The X coordinates of points in the table ParAndRad
        must be given in ascendant order.
        -   If Periodic is true, the first and last Y coordinates of
        points in the table ParAndRad are assumed to be
        equal. In addition, with the second syntax, Dd and Df
        are also assumed to be equal. If this is not the case,
        Set uses the first value(s) as last value(s).
        """

    @overload
    def Set(self, ParAndRad: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Dd: float, Df: float, Periodic: bool = False) -> None:
        """
        Defines this evolution law by interpolating the set of 2D
        points ParAndRad. The Y coordinate of a point of
        ParAndRad is the value of the function at the parameter
        point given by its X coordinate.
        If Periodic is true, this function is assumed to be periodic.
        In the second syntax, Dd and Df define the values of
        the first derivative of the function at its first and last points.
        Warning
        -   The X coordinates of points in the table ParAndRad
        must be given in ascendant order.
        -   If Periodic is true, the first and last Y coordinates of
        points in the table ParAndRad are assumed to be
        equal. In addition, with the second syntax, Dd and Df
        are also assumed to be equal. If this is not the case,
        Set uses the first value(s) as last value(s).
        """

    @overload
    def SetInRelative(self, ParAndRad: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Ud: float, Uf: float, Periodic: bool = False) -> None: ...

    @overload
    def SetInRelative(self, ParAndRad: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Ud: float, Uf: float, Dd: float, Df: float, Periodic: bool = False) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_Interpolate:
    """
    This class is used to interpolate a BsplineCurve
    passing through an array of points, with a C2
    Continuity if tangency is not requested at the point.
    If tangency is requested at the point the continuity
    will be C1. If Perodicity is requested the curve will
    be closed and the junction will be the first point
    given. The curve will than be only C1
    """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_HArray1[float] | None, PeriodicFlag: bool, Tolerance: float) -> None: ...

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_HArray1[float] | None, Parameters: nanoocp.NCollection.NCollection_HArray1[float] | None, PeriodicFlag: bool, Tolerance: float) -> None:
        """
        Tolerance is to check if the points are not too close
        to one an other. It is also used to check if the
        tangent vector is not too small. There should be at
        least 2 points. If PeriodicFlag is True then the curve
        will be periodic be periodic
        """

    @overload
    def __init__(self, theOther: Law_Interpolate) -> None: ...

    @overload
    def Load(self, InitialTangent: float, FinalTangent: float) -> None:
        """loads initial and final tangents if any."""

    @overload
    def Load(self, Tangents: nanoocp.NCollection.NCollection_Array1[float], TangentFlags: nanoocp.NCollection.NCollection_HArray1[bool] | None) -> None:
        """
        loads the tangents. We should have as many tangents as
        they are points in the array if TangentFlags.Value(i)
        is true use the tangent Tangents.Value(i)
        otherwise the tangent is not constrained.
        """

    def Perform(self) -> None:
        """Makes the interpolation"""

    def Curve(self) -> Law_BSpline: ...

    def IsDone(self) -> bool: ...

class Law_Linear(Law_Function):
    """Describes an linear evolution law."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty linear evolution law."""

    @overload
    def __init__(self, theOther: Law_Linear) -> None: ...

    def Set(self, Pdeb: float, Valdeb: float, Pfin: float, Valfin: float) -> None:
        """
        Defines this linear evolution law by assigning both:
        -   the bounds Pdeb and Pfin of the parameter, and
        -   the values Valdeb and Valfin of the function at these
        two parametric bounds.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """Returns 1"""

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Value(self, X: float) -> float:
        """Returns the value of this function at the point of parameter X."""

    def D1(self, X: float) -> tuple[float, float]:
        """
        Returns the value F and the first derivative D of this
        function at the point of parameter X.
        """

    def D2(self, X: float) -> tuple[float, float, float]:
        """
        Returns the value, first and second derivatives
        at parameter X.
        """

    def Trim(self, PFirst: float, PLast: float, Tol: float) -> Law_Function:
        """
        Returns a law equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        It is usfule to determines the derivatives
        in these values <First> and <Last> if
        the Law is not Cn.
        """

    def Bounds(self) -> tuple[float, float]:
        """Returns the parametric bounds of the function."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Law_S(Law_BSpFunc):
    """Describes an "S" evolution law."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty "S" evolution law."""

    @overload
    def __init__(self, theOther: Law_S) -> None: ...

    @overload
    def Set(self, Pdeb: float, Valdeb: float, Pfin: float, Valfin: float) -> None:
        """
        Defines this S evolution law by assigning both:
        -   the bounds Pdeb and Pfin of the parameter, and
        -   the values Valdeb and Valfin of the function at these
        two parametric bounds.
        The function is assumed to have the first derivatives
        equal to 0 at the two parameter points Pdeb and Pfin.
        """

    @overload
    def Set(self, Pdeb: float, Valdeb: float, Ddeb: float, Pfin: float, Valfin: float, Dfin: float) -> None:
        """
        Defines this S evolution law by assigning
        -   the bounds Pdeb and Pfin of the parameter,
        -   the values Valdeb and Valfin of the function at these
        two parametric bounds, and
        -   the values Ddeb and Dfin of the first derivative of the
        function at these two parametric bounds.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Law
import nanoocp.gp
Law_Laws = nanoocp.NCollection.NCollection_List[nanoocp.Law.Law_Function]
