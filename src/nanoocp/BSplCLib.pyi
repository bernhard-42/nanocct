"""OCCT package BSplCLib (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class BSplCLib_KnotDistribution(enum.IntEnum):
    """
    This enumeration describes the repartition of the
    knots sequence. If all the knots differ by the
    same positive constant from the preceding knot the
    "KnotDistribution" is <Uniform> else it is
    <NonUniform>
    """

    BSplCLib_NonUniform = 0

    BSplCLib_Uniform = 1

BSplCLib_NonUniform: BSplCLib_KnotDistribution = BSplCLib_KnotDistribution.BSplCLib_NonUniform

BSplCLib_Uniform: BSplCLib_KnotDistribution = BSplCLib_KnotDistribution.BSplCLib_Uniform

class BSplCLib_MultDistribution(enum.IntEnum):
    """
    This enumeration describes the form of the
    sequence of multiplicities. MultDistribution is:

    Constant if all the multiplicities have the same
    value.

    QuasiConstant if all the internal knots have the
    same multiplicity and if the first and last knot
    have a different multiplicity.

    NonConstant in other cases.
    """

    BSplCLib_NonConstant = 0

    BSplCLib_Constant = 1

    BSplCLib_QuasiConstant = 2

BSplCLib_NonConstant: BSplCLib_MultDistribution = BSplCLib_MultDistribution.BSplCLib_NonConstant

BSplCLib_Constant: BSplCLib_MultDistribution = BSplCLib_MultDistribution.BSplCLib_Constant

BSplCLib_QuasiConstant: BSplCLib_MultDistribution = BSplCLib_MultDistribution.BSplCLib_QuasiConstant

class BSplCLib_EvaluatorFunction:
    pass

class BSplCLib:
    """
    BSplCLib B-spline curve Library.

    The BSplCLib package is a basic library for BSplines. It
    provides three categories of functions.

    * Management methods to process knots and multiplicities.

    * Multi-Dimensions spline methods. BSpline methods where
    poles have an arbitrary number of dimensions. They divides
    in two groups:

    - Global methods modifying the whole set of poles. The
    poles are described by an array of Reals and a
    Dimension. Example: Inserting knots.

    - Local methods computing points and derivatives. The
    poles are described by a pointer on a local array of
    Reals and a Dimension. The local array is modified.

    * 2D and 3D spline curves methods.

    Methods for 2d and 3d BSplines curves rational or not
    rational.

    Those methods have the following structure:

    - They extract the pole information in a working array.

    - They process the working array with the multi-
    dimension methods. (for example a 3d rational curve
    is processed as a 4 dimension curve).

    - They get back the result in the original dimension.

    Note that the bspline surface methods found in the
    package BSplSLib uses the same structure and rely on
    BSplCLib.

    In the following list of methods the 2d and 3d curve
    methods will be described with the corresponding
    multi-dimension method.

    The 3d or 2d B-spline curve is defined with:

    . its control points : NCollection_Array1<gp_Pnt>(2d)        Poles
    . its weights        : NCollection_Array1<double>          Weights
    . its knots          : NCollection_Array1<double>          Knots
    . its multiplicities : NCollection_Array1<int>       Mults
    . its degree         : int              Degree
    . its periodicity    : bool              Periodic

    Warnings :
    The bounds of Poles and Weights should be the same.
    The bounds of Knots and Mults should be the same.

    Note: weight and multiplicity arrays can be passed by pointer for
    some functions so that NULL pointer is valid.
    That means no weights/no multiplicities passed.

    No weights (BSplCLib::NoWeights()) means the curve is non rational.
    No mults (BSplCLib::NoMults()) means the knots are "flat" knots.

    KeyWords :
    B-spline curve, Functions, Library

    References :
    . A survey of curves and surfaces methods in CADG Wolfgang
    BOHM CAGD 1 (1984)
    . On de Boor-like algorithms and blossoming Wolfgang BOEHM
    cagd 5 (1988)
    . Blossoming and knot insertion algorithms for B-spline curves
    Ronald N. GOLDMAN
    . Modelisation des surfaces en CAO, Henri GIAUME Peugeot SA
    . Curves and Surfaces for Computer Aided Geometric Design,
    a practical guide Gerald Farin
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BSplCLib) -> None: ...

    @staticmethod
    def Hunt(theArray: nanoocp.NCollection.NCollection_Array1[float], theX: float) -> int:
        """
        This routine searches the position of the real value theX
        in the monotonically increasing set of real values theArray using bisection algorithm.

        If the given value is out of range or array values, algorithm returns either
        theArray.Lower()-1 or theArray.Upper()+1 depending on theX position in the ordered set.

        This routine is used to locate a knot value in a set of knots.
        """

    @staticmethod
    def FirstUKnotIndex(Degree: int, Mults: nanoocp.NCollection.NCollection_Array1[int]) -> int:
        """
        Computes the index of the knots value which gives
        the start point of the curve.
        """

    @staticmethod
    def LastUKnotIndex(Degree: int, Mults: nanoocp.NCollection.NCollection_Array1[int]) -> int:
        """
        Computes the index of the knots value which gives
        the end point of the curve.
        """

    @staticmethod
    def FlatIndex(Degree: int, Index: int, Mults: nanoocp.NCollection.NCollection_Array1[int], Periodic: bool) -> int:
        """
        Computes the index of the flats knots sequence
        corresponding to <Index> in the knots sequence
        which multiplicities are <Mults>.
        """

    @overload
    @staticmethod
    def LocateParameter(Degree: int, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], U: float, IsPeriodic: bool, FromK1: int, ToK2: int) -> tuple[int, float]:
        """
        Locates the parametric value U in the knots
        sequence between the knot K1 and the knot K2.
        The value return in Index verifies.

        Knots(Index) <= U < Knots(Index + 1)
        if U <= Knots (K1) then Index = K1
        if U >= Knots (K2) then Index = K2 - 1

        If Periodic is True U may be modified to fit in
        the range Knots(K1), Knots(K2). In any case the
        correct value is returned in NewU.

        Warnings: Index is used as input data to initialize the
        searching function.
        Warning: Knots have to be "with repetitions\"
        """

    @overload
    @staticmethod
    def LocateParameter(Degree: int, Knots: nanoocp.NCollection.NCollection_Array1[float], U: float, IsPeriodic: bool, FromK1: int, ToK2: int) -> tuple[int, float]:
        """
        Locates the parametric value U in the knots
        sequence between the knot K1 and the knot K2.
        The value return in Index verifies.

        Knots(Index) <= U < Knots(Index + 1)
        if U <= Knots (K1) then Index = K1
        if U >= Knots (K2) then Index = K2 - 1

        If Periodic is True U may be modified to fit in
        the range Knots(K1), Knots(K2). In any case the
        correct value is returned in NewU.

        Warnings: Index is used as input data to initialize the
        searching function.
        Warning: Knots have to be "flat\"
        """

    @overload
    @staticmethod
    def LocateParameter(Degree: int, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], U: float, Periodic: bool) -> tuple[int, float]: ...

    @staticmethod
    def MaxKnotMult(Mults: nanoocp.NCollection.NCollection_Array1[int], K1: int, K2: int) -> int:
        """
        Finds the greatest multiplicity in a set of knots
        between K1 and K2. Mults is the multiplicity
        associated with each knot value.
        """

    @staticmethod
    def MinKnotMult(Mults: nanoocp.NCollection.NCollection_Array1[int], K1: int, K2: int) -> int:
        """
        Finds the lowest multiplicity in a set of knots
        between K1 and K2. Mults is the multiplicity
        associated with each knot value.
        """

    @staticmethod
    def NbPoles(Degree: int, Periodic: bool, Mults: nanoocp.NCollection.NCollection_Array1[int]) -> int:
        """
        Returns the number of poles of the curve. Returns 0 if
        one of the multiplicities is incorrect.

        * Non positive.

        * Greater than Degree, or Degree+1 at the first and
        last knot of a non periodic curve.

        * The last periodicity on a periodic curve is not
        equal to the first.
        """

    @staticmethod
    def KnotSequenceLength(Mults: nanoocp.NCollection.NCollection_Array1[int], Degree: int, Periodic: bool) -> int:
        """
        Returns the length of the sequence of knots with
        repetition.

        Periodic :

        Sum(Mults(i), i = Mults.Lower(); i <= Mults.Upper());

        Non Periodic :

        Sum(Mults(i); i = Mults.Lower(); i < Mults.Upper())
        + 2 * Degree
        """

    @overload
    @staticmethod
    def KnotSequence(Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], KnotSeq: nanoocp.NCollection.NCollection_Array1[float], Periodic: bool = False) -> None: ...

    @overload
    @staticmethod
    def KnotSequence(Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Degree: int, Periodic: bool, KnotSeq: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Computes the sequence of knots KnotSeq with
        repetition of the knots of multiplicity greater
        than 1.

        Length of KnotSeq must be KnotSequenceLength(Mults,Degree,Periodic)
        """

    @staticmethod
    def KnotsLength(KnotSeq: nanoocp.NCollection.NCollection_Array1[float], Periodic: bool = False) -> int:
        """
        Returns thelength of the sequence of knots (and
        Mults) without repetition.
        """

    @staticmethod
    def Knots(KnotSeq: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Periodic: bool = False) -> None:
        """
        Computes the sequence of knots Knots without
        repetition of the knots of multiplicity greater
        than 1.

        Length of <Knots> and <Mults> must be
        KnotsLength(KnotSequence,Periodic)
        """

    @staticmethod
    def KnotForm(Knots: nanoocp.NCollection.NCollection_Array1[float], FromK1: int, ToK2: int) -> BSplCLib_KnotDistribution:
        """
        Analyses if the knots distribution is "Uniform"
        or "NonUniform" between the knot FromK1 and the
        knot ToK2. There is no repetition of knot in the
        knots'sequence <Knots>.
        """

    @staticmethod
    def MultForm(Mults: nanoocp.NCollection.NCollection_Array1[int], FromK1: int, ToK2: int) -> BSplCLib_MultDistribution:
        """
        Analyses the distribution of multiplicities between
        the knot FromK1 and the Knot ToK2.
        """

    @staticmethod
    def KnotAnalysis(Degree: int, Periodic: bool, CKnots: nanoocp.NCollection.NCollection_Array1[float], CMults: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[nanoocp.GeomAbs.GeomAbs_BSplKnotDistribution, int]:
        """
        Analyzes the array of knots.
        Returns the form and the maximum knot multiplicity.
        """

    @staticmethod
    def Reparametrize(U1: float, U2: float, Knots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Reparametrizes a B-spline curve to [U1, U2].
        The knot values are recomputed such that Knots (Lower) = U1
        and Knots (Upper) = U2 but the knot form is not modified.
        Warnings:
        In the array Knots the values must be in ascending order.
        U1 must not be equal to U2 to avoid division by zero.
        """

    @overload
    @staticmethod
    def Reverse(Knots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Reverses the array knots to become the knots
        sequence of the reversed curve.
        """

    @overload
    @staticmethod
    def Reverse(Mults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """Reverses the array of multiplicities."""

    @overload
    @staticmethod
    def Reverse(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Last: int) -> None:
        """
        Reverses the array of poles. Last is the index of
        the new first pole. On a non periodic curve last
        is Poles.Upper(). On a periodic curve last is

        (number of flat knots - degree - 1)

        or

        (sum of multiplicities(but for the last) + degree - 1)
        """

    @overload
    @staticmethod
    def Reverse(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Last: int) -> None: ...

    @overload
    @staticmethod
    def Reverse(Weights: nanoocp.NCollection.NCollection_Array1[float], Last: int) -> None:
        """Reverses the array of poles."""

    @staticmethod
    def IsRational(Weights: nanoocp.NCollection.NCollection_Array1[float], I1: int, I2: int, Epsilon: float = 0.0) -> bool:
        """
        Returns False if all the weights of the array <Weights>
        between I1 an I2 are identic. Epsilon is used for
        comparing weights. If Epsilon is 0. the Epsilon of the
        first weight is used.
        """

    @staticmethod
    def MaxDegree() -> int:
        """returns the degree maxima for a BSplineCurve."""

    @overload
    @staticmethod
    def Eval(U: float, Degree: int, Dimension: int) -> tuple[float, float]:
        """
        Perform the Boor algorithm to evaluate a point at
        parameter <U>, with <Degree> and <Dimension>.

        Poles is an array of Reals of size

        <Dimension> * <Degree>+1

        Containing the poles. At the end <Poles> contains
        the current point.
        """

    @overload
    @staticmethod
    def Eval(U: float, PeriodicFlag: bool, HomogeneousFlag: bool, Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt) -> tuple[int, float]: ...

    @overload
    @staticmethod
    def Eval(U: float, PeriodicFlag: bool, HomogeneousFlag: bool, Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d) -> tuple[int, float]:
        """
        Perform the evaluation of the Bspline Basis
        and then multiplies by the weights
        this just evaluates the current point
        """

    @staticmethod
    def BoorScheme(U: float, Degree: int, Dimension: int, Depth: int, Length: int) -> tuple[float, float]:
        """
        Performs the Boor Algorithm at parameter <U> with
        the given <Degree> and the array of <Knots> on the
        poles <Poles> of dimension <Dimension>. The schema
        is computed until level <Depth> on a basis of
        <Length+1> poles.

        * Knots is an array of reals of length:

        <Length> + <Degree>

        * Poles is an array of reals of length:

        (2 * <Length> + 1) * <Dimension>

        The poles values must be set in the array at the
        positions.

        0..Dimension,

        2 * Dimension ..
        3 * Dimension

        4 * Dimension ..
        5 * Dimension

        ...

        The results are found in the array poles depending
        on the Depth. (See the method GetPole).
        """

    @staticmethod
    def AntiBoorScheme(U: float, Degree: int, Dimension: int, Depth: int, Length: int, Tolerance: float) -> tuple[bool, float, float]:
        """
        Compute the content of Pole before the BoorScheme.
        This method is used to remove poles.

        U is the poles to remove, Knots should contains the
        knots of the curve after knot removal.

        The first and last poles do not change, the other
        poles are computed by averaging two possible values.
        The distance between the two possible poles is
        computed, if it is higher than <Tolerance> False is
        returned.
        """

    @staticmethod
    def Derivative(Degree: int, Dimension: int, Length: int, Order: int) -> tuple[float, float]:
        """
        Computes the poles of the BSpline giving the
        derivatives of order <Order>.

        The formula for the first order is

        Pole(i) = Degree * (Pole(i+1) - Pole(i)) /
        (Knots(i+Degree+1) - Knots(i+1))

        This formula is repeated (Degree is decremented at
        each step).
        """

    @staticmethod
    def Bohm(U: float, Degree: int, N: int, Dimension: int) -> tuple[float, float]:
        """
        Performs the Bohm Algorithm at parameter <U>. This
        algorithm computes the value and all the derivatives
        up to order N (N <= Degree).

        <Poles> is the original array of poles.

        The result in <Poles> is the value and the
        derivatives. Poles[0] is the value, Poles[Degree]
        is the last derivative.
        """

    @staticmethod
    def NoWeights() -> nanoocp.NCollection.NCollection_Array1[float]:
        """Used as argument for a non rational curve."""

    @staticmethod
    def NoMults() -> nanoocp.NCollection.NCollection_Array1[int]:
        """Used as argument for a flatknots evaluation."""

    @staticmethod
    def MaxUnitWeightsSize() -> int:
        """
        Returns the maximum number of elements supported by the pre-allocated
        unit weights array (2049). For sizes larger than this, UnitWeights()
        will allocate a new array.
        """

    @staticmethod
    def UnitWeights(theNbElems: int) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns an NCollection_Array1<double> filled with 1.0 values.
        If theNbElems <= MaxUnitWeightsSize(), references a pre-allocated global array
        (zero allocation). Otherwise, allocates a new array and fills with 1.0.
        @warning The returned array may reference global static memory -- do NOT modify elements.
        @param[in] theNbElems the number of elements in the returned array
        @return array of unit weights with bounds [1, theNbElems]
        """

    @staticmethod
    def BuildKnots(Degree: int, Index: int, Periodic: bool, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> float:
        """
        Stores in LK the useful knots for the BoorSchem
        on the span Knots(Index) - Knots(Index+1)
        """

    @staticmethod
    def PoleIndex(Degree: int, Index: int, Periodic: bool, Mults: nanoocp.NCollection.NCollection_Array1[int]) -> int:
        """
        Return the index of the first Pole to use on the
        span Mults(Index) - Mults(Index+1). This index
        must be added to Poles.Lower().
        """

    @overload
    @staticmethod
    def BuildEval(Degree: int, Index: int, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> float: ...

    @overload
    @staticmethod
    def BuildEval(Degree: int, Index: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> float: ...

    @overload
    @staticmethod
    def BuildEval(Degree: int, Index: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """
        Copy in <LP> the poles and weights for the Eval
        scheme. starting from Poles(Poles.Lower()+Index)
        """

    @staticmethod
    def BuildBoor(Index: int, Length: int, Dimension: int, Poles: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """
        Copy in <LP> poles for <Dimension> Boor scheme.
        Starting from <Index> * <Dimension>, copy
        <Length+1> poles.
        """

    @staticmethod
    def BoorIndex(Index: int, Length: int, Depth: int) -> int:
        """
        Returns the index in the Boor result array of the
        poles <Index>. If the Boor algorithm was perform
        with <Length> and <Depth>.
        """

    @staticmethod
    def GetPole(Index: int, Length: int, Depth: int, Dimension: int, Pole: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[float, int]:
        """
        Copy the pole at position <Index> in the Boor
        scheme of dimension <Dimension> to <Position> in
        the array <Pole>. <Position> is updated.
        """

    @staticmethod
    def PrepareInsertKnots(Degree: int, Periodic: bool, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], AddKnots: nanoocp.NCollection.NCollection_Array1[float], AddMults: nanoocp.NCollection.NCollection_Array1[int], Epsilon: float, Add: bool = True) -> tuple[bool, int, int]:
        """
        Returns in <NbPoles, NbKnots> the new number of poles
        and knots if the sequence of knots <AddKnots,
        AddMults> is inserted in the sequence <Knots, Mults>.

        Epsilon is used to compare knots for equality.

        If Add is True the multiplicities on equal knots are
        added.

        If Add is False the max value of the multiplicities is
        kept.

        Return False if:
        The knew knots are knot increasing.
        The new knots are not in the range.
        """

    @overload
    @staticmethod
    def InsertKnots(Degree: int, Periodic: bool, Dimension: int, Poles: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], AddKnots: nanoocp.NCollection.NCollection_Array1[float], AddMults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], Epsilon: float, Add: bool = True) -> None: ...

    @overload
    @staticmethod
    def InsertKnots(Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], AddKnots: nanoocp.NCollection.NCollection_Array1[float], AddMults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], Epsilon: float, Add: bool = True) -> None: ...

    @overload
    @staticmethod
    def InsertKnots(Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], AddKnots: nanoocp.NCollection.NCollection_Array1[float], AddMults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], Epsilon: float, Add: bool = True) -> None:
        """
        Insert a sequence of knots <AddKnots> with
        multiplicities <AddMults>. <AddKnots> must be a non
        decreasing sequence and verifies:

        Knots(Knots.Lower()) <= AddKnots(AddKnots.Lower())
        Knots(Knots.Upper()) >= AddKnots(AddKnots.Upper())

        The NewPoles and NewWeights arrays must have a length:
        Poles.Length() + Sum(AddMults())

        When a knot to insert is identic to an existing knot the
        multiplicities are added.

        Epsilon is used to test knots for equality.

        When AddMult is negative or null the knot is not inserted.
        No multiplicity will becomes higher than the degree.

        The new Knots and Multiplicities are copied in <NewKnots>
        and <NewMults>.

        All the New arrays should be correctly dimensioned.

        When all the new knots are existing knots, i.e. only the
        multiplicities will change it is safe to use the same
        arrays as input and output.
        """

    @overload
    @staticmethod
    def InsertKnot(UIndex: int, U: float, UMult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def InsertKnot(UIndex: int, U: float, UMult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Insert a new knot U of multiplicity UMult in the knot
        sequence.

        The location of the new Knot should be given as an input
        data. UIndex locates the new knot U in the knot sequence
        and Knots (UIndex) < U < Knots (UIndex + 1).

        The new control points corresponding to this insertion are
        returned. Knots and Mults are not updated.
        """

    @overload
    @staticmethod
    def RaiseMultiplicity(KnotIndex: int, Mult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def RaiseMultiplicity(KnotIndex: int, Mult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Raise the multiplicity of knot to <UMult>.

        The new control points are returned. Knots and Mults are
        not updated.
        """

    @overload
    @staticmethod
    def RemoveKnot(Index: int, Mult: int, Degree: int, Periodic: bool, Dimension: int, Poles: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], Tolerance: float) -> bool: ...

    @overload
    @staticmethod
    def RemoveKnot(Index: int, Mult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], Tolerance: float) -> bool: ...

    @overload
    @staticmethod
    def RemoveKnot(Index: int, Mult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], Tolerance: float) -> bool:
        """
        Decrement the multiplicity of <Knots(Index)>
        to <Mult>. If <Mult> is null the knot is
        removed.

        As there are two ways to compute the new poles
        the midlle will be used as long as the
        distance is lower than Tolerance.

        If a distance is bigger than tolerance the
        methods returns False and the new arrays are
        not modified.

        A low tolerance can be used to test if the
        knot can be removed without modifying the
        curve.

        A high tolerance can be used to "smooth" the
        curve.
        """

    @staticmethod
    def IncreaseDegreeCountKnots(Degree: int, NewDegree: int, Periodic: bool, Mults: nanoocp.NCollection.NCollection_Array1[int]) -> int:
        """
        Returns the number of knots of a curve with
        multiplicities <Mults> after elevating the degree from
        <Degree> to <NewDegree>. See the IncreaseDegree method
        for more comments.
        """

    @overload
    @staticmethod
    def IncreaseDegree(Degree: int, NewDegree: int, Periodic: bool, Dimension: int, Poles: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    @staticmethod
    def IncreaseDegree(Degree: int, NewDegree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    @staticmethod
    def IncreaseDegree(Degree: int, NewDegree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    @staticmethod
    def IncreaseDegree(NewDegree: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def IncreaseDegree(theNewDegree: int, thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theWeights: nanoocp.NCollection.NCollection_Array1[float], theNewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theNewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Increase the degree of a bspline (or bezier) curve
        of dimension theDimension form theDegree to theNewDegree.

        The number of poles in the new curve is:
        @code
        Poles.Length() + (NewDegree - Degree) * Number of spans
        @endcode
        Where the number of spans is:
        @code
        LastUKnotIndex(Mults) - FirstUKnotIndex(Mults) + 1
        @endcode
        for a non-periodic curve, and
        @code
        Knots.Length() - 1
        @endcode
        for a periodic curve.

        The multiplicities of all knots are increased by the degree elevation.

        The new knots are usually the same knots with the
        exception of a non-periodic curve with the first
        and last multiplicity not equal to Degree+1 where
        knots are removed form the start and the bottom
        until the sum of the multiplicities is equal to
        NewDegree+1 at the knots corresponding to the
        first and last parameters of the curve.

        Example: Suppose a curve of degree 3 starting
        with following knots and multiplicities:
        @code
        knot : 0.  1.  2.
        mult : 1   2   1
        @endcode

        The FirstUKnot is 2.0 because the sum of multiplicities is
        @code
        Degree+1 : 1 + 2 + 1 = 4 = 3 + 1
        @endcode
        i.e. the first parameter of the curve is 2.0 and
        will still be 2.0 after degree elevation.
        Let raise this curve to degree 4.
        The multiplicities are increased by 2.

        They become 2 3 2.
        But we need a sum of multiplicities of 5 at knot 2.
        So the first knot is removed and the new knots are:
        @code
        knot : 1.  2.
        mult : 3   2
        @endcode
        The multiplicity of the first knot may also be reduced if the sum is still too big.

        In the most common situations (periodic curve or curve with first
        and last multiplicities equals to Degree+1) the knots are knot changes.

        The method IncreaseDegreeCountKnots can be used to compute the new number of knots.
        """

    @staticmethod
    def PrepareUnperiodize(Degree: int, Mults: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[int, int]:
        """
        Set in <NbKnots> and <NbPolesToAdd> the number of Knots and
        Poles of the NotPeriodic Curve identical at the
        periodic curve with a degree <Degree>, a
        knots-distribution with Multiplicities <Mults>.
        """

    @overload
    @staticmethod
    def Unperiodize(Degree: int, Dimension: int, Mults: nanoocp.NCollection.NCollection_Array1[int], Knots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Unperiodize(Degree: int, Mults: nanoocp.NCollection.NCollection_Array1[int], Knots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Unperiodize(Degree: int, Mults: nanoocp.NCollection.NCollection_Array1[int], Knots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def PrepareTrimming(Degree: int, Periodic: bool, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], U1: float, U2: float) -> tuple[int, int]:
        """
        Set in <NbKnots> and <NbPoles> the number of Knots and
        Poles of the curve resulting from the trimming of the
        BSplinecurve defined with <degree>, <knots>, <mults>
        """

    @overload
    @staticmethod
    def Trimming(Degree: int, Periodic: bool, Dimension: int, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[float], U1: float, U2: float, NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Trimming(Degree: int, Periodic: bool, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], U1: float, U2: float, NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Trimming(Degree: int, Periodic: bool, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], U1: float, U2: float, NewKnots: nanoocp.NCollection.NCollection_Array1[float], NewMults: nanoocp.NCollection.NCollection_Array1[int], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], NewWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> float: ...

    @overload
    @staticmethod
    def D0(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, UIndex: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[float, float]: ...

    @overload
    @staticmethod
    def D1(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, UIndex: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[float, float, float]: ...

    @overload
    @staticmethod
    def D2(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, UIndex: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[float, float, float, float]: ...

    @overload
    @staticmethod
    def D3(U: float, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, UIndex: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def DN(U: float, N: int, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[float], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> float: ...

    @overload
    @staticmethod
    def DN(U: float, N: int, Index: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], VN: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def DN(U: float, N: int, UIndex: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], V: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def EvalBsplineBasis(DerivativeOrder: int, Order: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameter: float, BsplineBasis: nanoocp.math.math_Matrix, isPeriodic: bool = False) -> tuple[int, int]:
        """
        This evaluates the Bspline Basis at a
        given parameter Parameter up to the
        requested DerivativeOrder and store the
        result in the array BsplineBasis in the
        following fashion
        BSplineBasis(1,1)   =
        value of first non vanishing
        Bspline function which has Index FirstNonZeroBsplineIndex
        BsplineBasis(1,2)   =
        value of second non vanishing
        Bspline function which has Index
        FirstNonZeroBsplineIndex + 1
        BsplineBasis(1,n)   =
        value of second non vanishing non vanishing
        Bspline function which has Index
        FirstNonZeroBsplineIndex + n (n <= Order)
        BSplineBasis(2,1)   =
        value of derivative of first non vanishing
        Bspline function which has Index FirstNonZeroBsplineIndex
        BSplineBasis(N,1)   =
        value of Nth derivative of first non vanishing
        Bspline function which has Index FirstNonZeroBsplineIndex
        if N <= DerivativeOrder + 1
        """

    @staticmethod
    def BuildBSpMatrix(Parameters: nanoocp.NCollection.NCollection_Array1[float], OrderArray: nanoocp.NCollection.NCollection_Array1[int], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Degree: int, Matrix: nanoocp.math.math_Matrix) -> tuple[int, int, int]:
        """
        This Builds a fully blown Matrix of
        (ni)
        Bi    (tj)

        with i and j within 1..Order + NumPoles
        The integer ni is the ith slot of the
        array OrderArray, tj is the jth slot of
        the array Parameters
        """

    @staticmethod
    def FactorBandedMatrix(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int) -> tuple[int, int]:
        """
        this factors the Banded Matrix in
        the LU form with a Banded storage of
        components of the L matrix
        WARNING : do not use if the Matrix is
        totally positive (It is the case for
        Bspline matrices build as above with
        parameters being the Schoenberg points
        """

    @overload
    @staticmethod
    def SolveBandedSystem(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int, ArrayDimension: int) -> tuple[int, float]:
        """
        This solves the system Matrix.X = B
        with when Matrix is factored in LU form
        The Array is an seen as an
        Array[1..N][1..ArrayDimension] with N =
        the rank of the matrix Matrix. The
        result is stored in Array when each
        coordinate is solved that is B is the
        array whose values are
        B[i] = Array[i][p] for each p in 1..ArrayDimension
        """

    @overload
    @staticmethod
    def SolveBandedSystem(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int, Array: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> int: ...

    @overload
    @staticmethod
    def SolveBandedSystem(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int, Array: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> int:
        """
        This solves the system Matrix.X = B
        with when Matrix is factored in LU form
        The Array has the length of
        the rank of the matrix Matrix. The
        result is stored in Array when each
        coordinate is solved that is B is the
        array whose values are
        B[i] = Array[i][p] for each p in 1..ArrayDimension
        """

    @overload
    @staticmethod
    def SolveBandedSystem(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int, HomogenousFlag: bool, ArrayDimension: int) -> tuple[int, float, float]: ...

    @overload
    @staticmethod
    def SolveBandedSystem(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int, HomogenousFlag: bool, Array: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> int:
        """
        This solves the system Matrix.X = B
        with when Matrix is factored in LU form
        The Array is an seen as an
        Array[1..N][1..ArrayDimension] with N =
        the rank of the matrix Matrix. The
        result is stored in Array when each
        coordinate is solved that is B is the
        array whose values are B[i] = Array[i][p]
        for each p in 1..ArrayDimension.
        If HomogeneousFlag == 0
        the Poles are multiplied by the
        Weights upon Entry and once
        interpolation is carried over the
        result of the poles are divided by the
        result of the interpolation of the
        weights. Otherwise if HomogenousFlag == 1
        the Poles and Weights are treated homogeneously
        that is that those are interpolated as they
        are and result is returned without division
        by the interpolated weights.
        """

    @overload
    @staticmethod
    def SolveBandedSystem(Matrix: nanoocp.math.math_Matrix, UpperBandWidth: int, LowerBandWidth: int, HomogeneousFlag: bool, Array: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> int:
        """
        This solves the system Matrix.X = B
        with when Matrix is factored in LU form
        The Array is an seen as an
        Array[1..N][1..ArrayDimension] with N =
        the rank of the matrix Matrix. The
        result is stored in Array when each
        coordinate is solved that is B is the
        array whose values are B[i] = Array[i][p]
        for each p in 1..ArrayDimension
        If HomogeneousFlag == 0
        the Poles are multiplied by the
        Weights upon Entry and once
        interpolation is carried over the
        result of the poles are divided by the
        result of the interpolation of the
        weights. Otherwise if HomogenousFlag == 1
        the Poles and Weights are treated homogeneously
        that is that those are interpolated as they
        are and result is returned without division
        by the interpolated weights.
        """

    @staticmethod
    def MergeBSplineKnots(Tolerance: float, StartValue: float, EndValue: float, Degree1: int, Knots1: nanoocp.NCollection.NCollection_Array1[float], Mults1: nanoocp.NCollection.NCollection_Array1[int], Degree2: int, Knots2: nanoocp.NCollection.NCollection_Array1[float], Mults2: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[int, nanoocp.NCollection.NCollection_HArray1[float], nanoocp.NCollection.NCollection_HArray1[int]]:
        """
        Merges two knot vector by setting the starting and
        ending values to StartValue and EndValue
        """

    @overload
    @staticmethod
    def FunctionReparameterise(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], PolesDimension: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int) -> tuple[float, float, int]: ...

    @overload
    @staticmethod
    def FunctionReparameterise(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int, NewPoles: nanoocp.NCollection.NCollection_Array1[float]) -> int:
        """
        This function will compose a given Vectorial BSpline F(t)
        defined by its BSplineDegree and BSplineFlatKnotsl,
        its Poles array which are coded as an array of Real
        of the form [1..NumPoles][1..PolesDimension] with a
        function a(t) which is assumed to satisfy the
        following:

        1. F(a(t)) is a polynomial BSpline
        that can be expressed exactly as a BSpline of degree
        NewDegree on the knots FlatKnots

        2. a(t) defines a differentiable
        isomorphism between the range of FlatKnots to the range
        of BSplineFlatKnots which is the
        same as the range of F(t)

        Warning: it is
        the caller's responsibility to insure that conditions
        1. and 2. above are satisfied: no check whatsoever
        is made in this method

        theStatus will return 0 if OK else it will return the pivot index
        of the matrix that was inverted to compute the multiplied
        BSpline: the method used is interpolation at Schoenenberg
        points of F(a(t))
        """

    @overload
    @staticmethod
    def FunctionReparameterise(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int, NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> int: ...

    @overload
    @staticmethod
    def FunctionReparameterise(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int, NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> int:
        """
        this will compose a given Vectorial BSpline F(t)
        defined by its BSplineDegree and BSplineFlatKnotsl,
        its Poles array which are coded as an array of Real
        of the form [1..NumPoles][1..PolesDimension] with a
        function a(t) which is assumed to satisfy the
        following: 1. F(a(t)) is a polynomial BSpline
        that can be expressed exactly as a BSpline of degree
        NewDegree on the knots FlatKnots
        2. a(t) defines a differentiable
        isomorphism between the range of FlatKnots to the range
        of BSplineFlatKnots which is the
        same as the range of F(t)
        Warning: it is
        the caller's responsibility to insure that conditions
        1. and 2. above are satisfied: no check whatsoever
        is made in this method
        theStatus will return 0 if OK else it will return the pivot index
        of the matrix that was inverted to compute the multiplied
        BSpline: the method used is interpolation at Schoenenberg
        points of F(a(t))
        """

    @overload
    @staticmethod
    def FunctionMultiply(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], PolesDimension: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int) -> tuple[float, float, int]: ...

    @overload
    @staticmethod
    def FunctionMultiply(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int, NewPoles: nanoocp.NCollection.NCollection_Array1[float]) -> int: ...

    @overload
    @staticmethod
    def FunctionMultiply(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int, NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> int: ...

    @overload
    @staticmethod
    def FunctionMultiply(Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewDegree: int, NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> int:
        """
        this will multiply a given Vectorial BSpline F(t)
        defined by its BSplineDegree and BSplineFlatKnotsl,
        its Poles array which are coded as an array of Real
        of the form [1..NumPoles][1..PolesDimension] by a
        function a(t) which is assumed to satisfy the
        following: 1. a(t) * F(t) is a polynomial BSpline
        that can be expressed exactly as a BSpline of degree
        NewDegree on the knots FlatKnots 2. the range of a(t)
        is the same as the range of F(t)
        Warning: it is
        the caller's responsibility to insure that conditions
        1. and 2. above are satisfied: no check whatsoever
        is made in this method
        theStatus will return 0 if OK else it will return the pivot index
        of the matrix that was inverted to compute the multiplied
        BSpline: the method used is interpolation at Schoenenberg
        points of a(t)*F(t)
        """

    @staticmethod
    def Eval__int__float__float(U: float, PeriodicFlag: bool, DerivativeRequest: int, Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], ArrayDimension: int) -> tuple[int, float, float]:
        """
        Eval__int__float__float: the C++ overload Eval(const double, const bool, const int, int &, const int, const NCollection_Array1<double> &, const int, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Perform the De Boor algorithm to evaluate a point at
        parameter <U>, with <Degree> and <Dimension>.

        Poles is an array of Reals of size

        <Dimension> * <Degree>+1

        Containing the poles. At the end <Poles> contains
        the current point. Poles Contain all the poles of
        the BsplineCurve, Knots also Contains all the knots
        of the BsplineCurve. ExtrapMode has two slots [0] =
        Degree used to extrapolate before the first knot [1]
        = Degre used to extrapolate after the last knot has
        to be between 1 and Degree
        """

    @staticmethod
    def Eval__int__float__float__float__float(U: float, PeriodicFlag: bool, DerivativeRequest: int, Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], ArrayDimension: int) -> tuple[int, float, float, float, float]:
        """
        Eval__int__float__float__float__float: the C++ overload Eval(const double, const bool, const int, int &, const int, const NCollection_Array1<double> &, const int, double &, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Perform the De Boor algorithm to evaluate a point at
        parameter <U>, with <Degree> and <Dimension>.
        Evaluates by multiplying the Poles by the Weights and
        gives the homogeneous result in PolesResult that is
        the results of the evaluation of the numerator once it
        has been multiplied by the weights and in
        WeightsResult one has the result of the evaluation of
        the denominator

        Warning: <PolesResult> and <WeightsResult> must be
        dimensioned properly.
        """

    @staticmethod
    def TangExtendToConstraint(FlatKnots: nanoocp.NCollection.NCollection_Array1[float], C1Coefficient: float, NumPoles: int, Dimension: int, Degree: int, ConstraintPoint: nanoocp.NCollection.NCollection_Array1[float], Continuity: int, After: bool) -> tuple[float, int, int, float, float]:
        """
        Extend a BSpline nD using the tangency map
        <C1Coefficient> is the coefficient of reparametrisation
        <Continuity> must be equal to 1, 2 or 3.
        <Degree> must be greater or equal than <Continuity> + 1.

        Warning: <KnotsResult> and <PolesResult> must be dimensioned
        properly.
        """

    @overload
    @staticmethod
    def CacheD0(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @overload
    @staticmethod
    def CacheD0(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Perform the evaluation of the Bspline Basis
        and then multiplies by the weights
        this just evaluates the current point
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        ththe CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effectsis just evaluates the current point
        """

    @overload
    @staticmethod
    def CoefsD0(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def CoefsD0(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Calls CacheD0 for Bezier Curves Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for Beziercurves ONLY!!!
        """

    @overload
    @staticmethod
    def CacheD1(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt, Vec: nanoocp.gp.gp_Vec) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @overload
    @staticmethod
    def CacheD1(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d, Vec: nanoocp.gp.gp_Vec2d) -> None:
        """
        Perform the evaluation of the Bspline Basis
        and then multiplies by the weights
        this just evaluates the current point
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        ththe CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effectsis just evaluates the current point
        """

    @overload
    @staticmethod
    def CoefsD1(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt, Vec: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def CoefsD1(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d, Vec: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calls CacheD1 for Bezier Curves Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for Beziercurves ONLY!!!
        """

    @overload
    @staticmethod
    def CacheD2(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt, Vec1: nanoocp.gp.gp_Vec, Vec2: nanoocp.gp.gp_Vec) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @overload
    @staticmethod
    def CacheD2(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d, Vec1: nanoocp.gp.gp_Vec2d, Vec2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Perform the evaluation of the Bspline Basis
        and then multiplies by the weights
        this just evaluates the current point
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        ththe CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effectsis just evaluates the current point
        """

    @overload
    @staticmethod
    def CoefsD2(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt, Vec1: nanoocp.gp.gp_Vec, Vec2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def CoefsD2(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d, Vec1: nanoocp.gp.gp_Vec2d, Vec2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calls CacheD1 for Bezier Curves Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for Beziercurves ONLY!!!
        """

    @overload
    @staticmethod
    def CacheD3(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt, Vec1: nanoocp.gp.gp_Vec, Vec2: nanoocp.gp.gp_Vec, Vec3: nanoocp.gp.gp_Vec) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @overload
    @staticmethod
    def CacheD3(U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d, Vec1: nanoocp.gp.gp_Vec2d, Vec2: nanoocp.gp.gp_Vec2d, Vec3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Perform the evaluation of the Bspline Basis
        and then multiplies by the weights
        this just evaluates the current point
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        ththe CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effectsis just evaluates the current point
        """

    @overload
    @staticmethod
    def CoefsD3(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt, Vec1: nanoocp.gp.gp_Vec, Vec2: nanoocp.gp.gp_Vec, Vec3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def CoefsD3(U: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Point: nanoocp.gp.gp_Pnt2d, Vec1: nanoocp.gp.gp_Vec2d, Vec2: nanoocp.gp.gp_Vec2d, Vec3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calls CacheD1 for Bezier Curves Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for Beziercurves ONLY!!!
        """

    @overload
    @staticmethod
    def BuildCache(U: float, InverseOfSpanDomain: float, PeriodicFlag: bool, Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], CachePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], CacheWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def BuildCache(U: float, InverseOfSpanDomain: float, PeriodicFlag: bool, Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], CachePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], CacheWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Perform the evaluation of the Taylor expansion
        of the Bspline normalized between 0 and 1.
        If rational computes the homogeneous Taylor expansion
        for the numerator and stores it in CachePoles
        """

    @overload
    @staticmethod
    def BuildCache(theParameter: float, theSpanDomain: float, thePeriodicFlag: bool, theDegree: int, theSpanIndex: int, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float], thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array1[float], theCacheArray: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    @overload
    @staticmethod
    def BuildCache(theParameter: float, theSpanDomain: float, thePeriodicFlag: bool, theDegree: int, theSpanIndex: int, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float], thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theWeights: nanoocp.NCollection.NCollection_Array1[float], theCacheArray: nanoocp.NCollection.NCollection_Array2[float]) -> None:
        """
        Perform the evaluation of the Taylor expansion
        of the Bspline normalized between 0 and 1.
        Structure of result optimized for BSplCLib_Cache.
        """

    @overload
    @staticmethod
    def PolesCoefficients(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], CachePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None: ...

    @overload
    @staticmethod
    def PolesCoefficients(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], CachePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], CacheWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def PolesCoefficients(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], CachePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    @staticmethod
    def PolesCoefficients(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], CachePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], CacheWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Encapsulation of BuildCache to perform the
        evaluation of the Taylor expansion for beziercurves
        at parameter 0.
        Warning: To be used for Beziercurves ONLY!!!
        """

    @staticmethod
    def FlatBezierKnots(Degree: int) -> float:
        """
        Returns pointer to statically allocated array representing
        flat knots for bezier curve of the specified degree.
        Raises OutOfRange if Degree > MaxDegree()
        """

    @staticmethod
    def BuildSchoenbergPoints(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        builds the Schoenberg points from the flat knot
        used to interpolate a BSpline since the
        BSpline matrix is invertible.
        """

    @overload
    @staticmethod
    def Interpolate(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float], ContactOrderArray: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> int:
        """
        Performs the interpolation of the data given in
        the Poles array according to the requests in
        ContactOrderArray that is: if
        ContactOrderArray(i) has value d it means that
        Poles(i) contains the dth derivative of the
        function to be interpolated. The length L of the
        following arrays must be the same:
        Parameters, ContactOrderArray, Poles,
        The length of FlatKnots is Degree + L + 1
        Warning:
        the method used to do that interpolation is
        gauss elimination WITHOUT pivoting. Thus if the
        diagonal is not dominant there is no guarantee
        that the algorithm will work. Nevertheless for
        Cubic interpolation or interpolation at Scheonberg
        points the method will work
        The InversionProblem will report 0 if there was no
        problem else it will give the index of the faulty
        pivot
        """

    @overload
    @staticmethod
    def Interpolate(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float], ContactOrderArray: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> int: ...

    @overload
    @staticmethod
    def Interpolate(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float], ContactOrderArray: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> int:
        """
        Performs the interpolation of the data given in
        the Poles array according to the requests in
        ContactOrderArray that is: if
        ContactOrderArray(i) has value d it means that
        Poles(i) contains the dth derivative of the
        function to be interpolated. The length L of the
        following arrays must be the same:
        Parameters, ContactOrderArray, Poles,
        The length of FlatKnots is Degree + L + 1
        Warning:
        the method used to do that interpolation is
        gauss elimination WITHOUT pivoting. Thus if the
        diagonal is not dominant there is no guarantee
        that the algorithm will work. Nevertheless for
        Cubic interpolation at knots or interpolation at
        Scheonberg points the method will work.
        The InversionProblem will report 0 if there was no
        problem else it will give the index of the faulty
        pivot
        """

    @overload
    @staticmethod
    def Interpolate(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float], ContactOrderArray: nanoocp.NCollection.NCollection_Array1[int], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> int:
        """
        Performs the interpolation of the data given in
        the Poles array according to the requests in
        ContactOrderArray that is: if
        ContactOrderArray(i) has value d it means that
        Poles(i) contains the dth derivative of the
        function to be interpolated. The length L of the
        following arrays must be the same:
        Parameters, ContactOrderArray, Poles,
        The length of FlatKnots is Degree + L + 1
        Warning:
        the method used to do that interpolation is
        gauss elimination WITHOUT pivoting. Thus if the
        diagonal is not dominant there is no guarantee
        that the algorithm will work. Nevertheless for
        Cubic interpolation at knots or interpolation at
        Scheonberg points the method will work.
        The InversionProblem will report 0 if there was
        no problem else it will give the i
        """

    @staticmethod
    def Interpolate__float__int(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float], ContactOrderArray: nanoocp.NCollection.NCollection_Array1[int], ArrayDimension: int) -> tuple[float, int]:
        """
        Interpolate__float__int: the C++ overload Interpolate(const int, const NCollection_Array1<double> &, const NCollection_Array1<double> &, const NCollection_Array1<int> &, const int, double &, int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Performs the interpolation of the data given in
        the Poles array according to the requests in
        ContactOrderArray that is: if
        ContactOrderArray(i) has value d it means that
        Poles(i) contains the dth derivative of the
        function to be interpolated. The length L of the
        following arrays must be the same:
        Parameters, ContactOrderArray
        The length of FlatKnots is Degree + L + 1
        The PolesArray is an seen as an
        Array[1..N][1..ArrayDimension] with N = tge length
        of the parameters array
        Warning:
        the method used to do that interpolation is
        gauss elimination WITHOUT pivoting. Thus if the
        diagonal is not dominant there is no guarantee
        that the algorithm will work. Nevertheless for
        Cubic interpolation or interpolation at Scheonberg
        points the method will work
        The InversionProblem will report 0 if there was no
        problem else it will give the index of the faulty
        pivot
        """

    @staticmethod
    def Interpolate__float__float__int(Degree: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Parameters: nanoocp.NCollection.NCollection_Array1[float], ContactOrderArray: nanoocp.NCollection.NCollection_Array1[int], ArrayDimension: int) -> tuple[float, float, int]:
        """
        Interpolate__float__float__int: the C++ overload Interpolate(const int, const NCollection_Array1<double> &, const NCollection_Array1<double> &, const NCollection_Array1<int> &, const int, double &, double &, int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @overload
    @staticmethod
    def MovePoint(U: float, Displ: nanoocp.gp.gp_Vec2d, Index1: int, Index2: int, Degree: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> tuple[int, int]: ...

    @overload
    @staticmethod
    def MovePoint(U: float, Displ: nanoocp.gp.gp_Vec, Index1: int, Index2: int, Degree: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> tuple[int, int]:
        """
        Find the new poles which allows an old point (with a
        given <u> as parameter) to reach a new position
        Index1 and Index2 indicate the range of poles we can move
        (1, NbPoles-1) or (2, NbPoles) -> no constraint for one side
        don't enter (1,NbPoles) -> error: rigid move
        (2, NbPoles-1) -> the ends are enforced
        (3, NbPoles-2) -> the ends and the tangency are enforced
        if Problem in BSplineBasis calculation, no change for the curve
        and FirstIndex, LastIndex = 0
        """

    @overload
    @staticmethod
    def MovePointAndTangent(U: float, ArrayDimension: int, Tolerance: float, Degree: int, StartingCondition: int, EndingCondition: int, Weights: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[float, float, float, float, int]: ...

    @overload
    @staticmethod
    def MovePointAndTangent(U: float, Delta: nanoocp.gp.gp_Vec, DeltaDerivative: nanoocp.gp.gp_Vec, Tolerance: float, Degree: int, StartingCondition: int, EndingCondition: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> int: ...

    @overload
    @staticmethod
    def MovePointAndTangent(U: float, Delta: nanoocp.gp.gp_Vec2d, DeltaDerivative: nanoocp.gp.gp_Vec2d, Tolerance: float, Degree: int, StartingCondition: int, EndingCondition: int, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], NewPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> int:
        """
        This is the dimension free version of the utility
        U is the parameter must be within the first FlatKnots and the
        last FlatKnots Delta is the amount the curve has to be moved
        DeltaDerivative is the amount the derivative has to be moved.
        Delta and DeltaDerivative must be array of dimension
        ArrayDimension Degree is the degree of the BSpline and the
        FlatKnots are the knots of the BSpline Starting Condition if =
        -1 means the starting point of the curve can move
        = 0 means the
        starting point of the curve cannot move but tangent starting
        point of the curve cannot move
        = 1 means the starting point and tangents cannot move
        = 2 means the starting point tangent and curvature cannot move
        = ...
        Same holds for EndingCondition
        Poles are the poles of the curve
        Weights are the weights of the curve if not NULL
        NewPoles are the poles of the deformed curve
        ErrorStatus will be 0 if no error happened
        1 if there are not enough knots/poles
        the imposed conditions
        The way to solve this problem is to add knots to the BSpline
        If StartCondition = 1 and EndCondition = 1 then you need at least
        4 + 2 = 6 poles so for example to have a C1 cubic you will need
        have at least 2 internal knots.
        """

    @overload
    @staticmethod
    def Resolution(ArrayDimension: int, NumPoles: int, Weights: nanoocp.NCollection.NCollection_Array1[float], FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Degree: int, Tolerance3D: float) -> tuple[float, float]: ...

    @overload
    @staticmethod
    def Resolution(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], NumPoles: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Degree: int, Tolerance3D: float) -> float: ...

    @overload
    @staticmethod
    def Resolution(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], NumPoles: int, FlatKnots: nanoocp.NCollection.NCollection_Array1[float], Degree: int, Tolerance3D: float) -> float:
        """
        given a tolerance in 3D space returns a
        tolerance in U parameter space such that
        all u1 and u0 in the domain of the curve f(u)
        | u1 - u0 | < UTolerance and
        we have |f (u1) - f (u0)| < Tolerance3D
        """

    @staticmethod
    def Intervals(theKnots: nanoocp.NCollection.NCollection_Array1[float], theMults: nanoocp.NCollection.NCollection_Array1[int], theDegree: int, isPeriodic: bool, theContinuity: int, theFirst: float, theLast: float, theTolerance: float, theIntervals: nanoocp.NCollection.NCollection_Array1[float]) -> int:
        """
        Splits the given range to BSpline intervals of given continuity
        @param[in] theKnots the knots of BSpline
        @param[in] theMults the knots' multiplicities
        @param[in] theDegree the degree of BSpline
        @param[in] isPeriodic the periodicity of BSpline
        @param[in] theContinuity the target interval's continuity
        @param[in] theFirst the begin of the target range
        @param[in] theLast the end of the target range
        @param[in] theTolerance the tolerance
        @param[in,out] theIntervals the array to store intervals if isn't nullptr
        @return the number of intervals
        """

class BSplCLib_CacheParams:
    """
    Simple structure containing parameters describing parameterization
    of a B-spline curve or a surface in one direction (U or V),
    and data of the current span for its caching
    """

    def __init__(self, theDegree: int, thePeriodic: bool, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Constructor, prepares data structures for caching.
        \\param theDegree     degree of the B-spline (or Bezier)
        \\param thePeriodic   identify whether the B-spline is periodic
        \\param theFlatKnots  knots of Bezier / B-spline parameterization
        """

    def PeriodicNormalization(self, theParameter: float) -> float:
        """
        Normalizes the parameter for periodic B-splines
        \\param theParameter the value to be normalized into the knots array
        """

    def IsCacheValid(self, theParameter: float) -> bool:
        """
        Verifies validity of the cache using flat parameter of the point
        \\param theParameter parameter of the point placed in the span
        """

    def LocateParameter(self, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """
        Computes span for the specified parameter
        \\param theParameter parameter of the point placed in the span
        \\param theFlatKnots  knots of Bezier / B-spline parameterization
        """

    @property
    def Degree(self) -> int:
        """< degree of Bezier/B-spline"""

    @property
    def IsPeriodic(self) -> bool:
        """< true of the B-spline is periodic"""

    @property
    def FirstParameter(self) -> float:
        """< first valid parameter"""

    @property
    def LastParameter(self) -> float:
        """< last valid parameter"""

    @property
    def SpanIndexMin(self) -> int:
        """< minimal index of span"""

    @property
    def SpanIndexMax(self) -> int:
        """< maximal index of span"""

    @property
    def SpanStart(self) -> float:
        """< parameter for the frst point of the span"""

    @SpanStart.setter
    def SpanStart(self, arg: float, /) -> None: ...

    @property
    def SpanLength(self) -> float:
        """< length of the span"""

    @SpanLength.setter
    def SpanLength(self, arg: float, /) -> None: ...

    @property
    def SpanIndex(self) -> int:
        """< index of the span"""

    @SpanIndex.setter
    def SpanIndex(self, arg: int, /) -> None: ...

class BSplCLib_Cache(nanoocp.Standard.Standard_Transient):
    """
    \\brief A cache class for Bezier and B-spline curves.

    Defines all data, that can be cached on a span of a curve.
    The data should be recalculated in going from span to span.
    """

    @overload
    def __init__(self, theDegree: int, thePeriodic: bool, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float], thePoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theWeights: nanoocp.NCollection.NCollection_Array1[float] = None) -> None:
        """
        Constructor, prepares data structures for caching values on a 2d curve.
        \\param theDegree     degree of the curve
        \\param thePeriodic   identify whether the curve is periodic
        \\param theFlatKnots  knots of Bezier/B-spline curve (with repetitions)
        \\param thePoles2d    array of poles of 2D curve
        \\param theWeights    array of weights of corresponding poles
        """

    @overload
    def __init__(self, theDegree: int, thePeriodic: bool, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float], thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array1[float] = None) -> None:
        """
        Constructor, prepares data structures for caching values on a 3d curve.
        \\param theDegree     degree of the curve
        \\param thePeriodic   identify whether the curve is periodic
        \\param theFlatKnots  knots of Bezier/B-spline curve (with repetitions)
        \\param thePoles      array of poles of 3D curve
        \\param theWeights    array of weights of corresponding poles
        """

    def IsCacheValid(self, theParameter: float) -> bool:
        """
        Verifies validity of the cache using flat parameter of the point
        \\param theParameter parameter of the point placed in the span
        """

    @overload
    def BuildCache(self, theParameter: float, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float], thePoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Recomputes the cache data for 2D curves. Does not verify validity of the cache
        \\param theParameter  the value on the knot's axis to identify the span
        \\param theFlatKnots  knots of Bezier/B-spline curve (with repetitions)
        \\param thePoles2d    array of poles of 2D curve
        \\param theWeights    array of weights of corresponding poles
        """

    @overload
    def BuildCache(self, theParameter: float, theFlatKnots: nanoocp.NCollection.NCollection_Array1[float], thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theWeights: nanoocp.NCollection.NCollection_Array1[float] = None) -> None:
        """
        Recomputes the cache data for 3D curves. Does not verify validity of the cache
        \\param theParameter  the value on the knot's axis to identify the span
        \\param theFlatKnots  knots of Bezier/B-spline curve (with repetitions)
        \\param thePoles      array of poles of 3D curve
        \\param theWeights    array of weights of corresponding poles
        """

    @overload
    def D0(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Calculates the point on the curve in the specified parameter
        \\param[in]  theParameter parameter of calculation of the value
        \\param[out] thePoint     the result of calculation (the point on the curve)
        """

    @overload
    def D0(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def D1(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt2d, theTangent: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calculates the point on the curve and its first derivative in the specified parameter
        \\param[in]  theParameter parameter of calculation of the value
        \\param[out] thePoint     the result of calculation (the point on the curve)
        \\param[out] theTangent   tangent vector (first derivatives) for the curve in the calculated
        point
        """

    @overload
    def D1(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt, theTangent: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def D2(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt2d, theTangent: nanoocp.gp.gp_Vec2d, theCurvature: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calculates the point on the curve and two derivatives in the specified parameter
        \\param[in]  theParameter parameter of calculation of the value
        \\param[out] thePoint     the result of calculation (the point on the curve)
        \\param[out] theTangent   tangent vector (1st derivatives) for the curve in the calculated
        point \\param[out] theCurvature curvature vector (2nd derivatives) for the curve in the
        calculated point
        """

    @overload
    def D2(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt, theTangent: nanoocp.gp.gp_Vec, theCurvature: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def D3(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt2d, theTangent: nanoocp.gp.gp_Vec2d, theCurvature: nanoocp.gp.gp_Vec2d, theTorsion: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calculates the point on the curve and three derivatives in the specified parameter
        \\param[in]  theParameter parameter of calculation of the value
        \\param[out] thePoint     the result of calculation (the point on the curve)
        \\param[out] theTangent   tangent vector (1st derivatives) for the curve in the calculated
        point \\param[out] theCurvature curvature vector (2nd derivatives) for the curve in the
        calculated point \\param[out] theTorsion   second curvature vector (3rd derivatives) for the
        curve in the calculated point
        """

    @overload
    def D3(self, theParameter: float, thePoint: nanoocp.gp.gp_Pnt, theTangent: nanoocp.gp.gp_Vec, theCurvature: nanoocp.gp.gp_Vec, theTorsion: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def D0Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Calculates the 3D point using pre-computed local parameter in [0, 1] range.
        This bypasses periodic normalization and local parameter calculation.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the result of calculation (the point on the curve)
        """

    @overload
    def D0Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Calculates the 2D point using pre-computed local parameter in [0, 1] range.
        This bypasses periodic normalization and local parameter calculation.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the result of calculation (the point on the curve)
        """

    @overload
    def D1Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt, theTangent: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the 3D point and first derivative using pre-computed local parameter.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the point on the curve
        @param[out] theTangent    first derivative (tangent vector)
        """

    @overload
    def D1Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt2d, theTangent: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calculates the 2D point and first derivative using pre-computed local parameter.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the point on the curve
        @param[out] theTangent    first derivative (tangent vector)
        """

    @overload
    def D2Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt, theTangent: nanoocp.gp.gp_Vec, theCurvature: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the 3D point, first and second derivatives using pre-computed local parameter.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the point on the curve
        @param[out] theTangent    first derivative (tangent vector)
        @param[out] theCurvature  second derivative (curvature vector)
        """

    @overload
    def D2Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt2d, theTangent: nanoocp.gp.gp_Vec2d, theCurvature: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calculates the 2D point, first and second derivatives using pre-computed local parameter.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the point on the curve
        @param[out] theTangent    first derivative (tangent vector)
        @param[out] theCurvature  second derivative (curvature vector)
        """

    @overload
    def D3Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt, theTangent: nanoocp.gp.gp_Vec, theCurvature: nanoocp.gp.gp_Vec, theTorsion: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the 3D point, first, second and third derivatives using pre-computed local
        parameter.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the point on the curve
        @param[out] theTangent    first derivative (tangent vector)
        @param[out] theCurvature  second derivative (curvature vector)
        @param[out] theTorsion    third derivative (torsion vector)
        """

    @overload
    def D3Local(self, theLocalParam: float, thePoint: nanoocp.gp.gp_Pnt2d, theTangent: nanoocp.gp.gp_Vec2d, theCurvature: nanoocp.gp.gp_Vec2d, theTorsion: nanoocp.gp.gp_Vec2d) -> None:
        """
        Calculates the 2D point, first, second and third derivatives using pre-computed local
        parameter.
        @param[in]  theLocalParam pre-computed local parameter: (Param - SpanStart) / SpanLength
        @param[out] thePoint      the point on the curve
        @param[out] theTangent    first derivative (tangent vector)
        @param[out] theCurvature  second derivative (curvature vector)
        @param[out] theTorsion    third derivative (torsion vector)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
