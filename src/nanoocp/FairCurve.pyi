"""OCCT package FairCurve (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Geom2d
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class FairCurve_AnalysisCode(enum.IntEnum):
    """
    To deal with different results in the computation of curvatures.
    -   FairCurve_OK describes the case where computation is successfully
    completed
    -   FairCurve_NotConverged describes
    the case where the algorithm does not
    converge. In this case, you can not be
    certain of the result quality and should
    resume computation if you want to make use of the curve.
    -   FairCurve_InfiniteSliding describes the case where sliding is infinite, and,
    consequently, computation stops. The solution is to use an imposed sliding value.
    -   FairCurve_NullHeight describes the case where no matter is left at one of the
    ends of the curve, and as a result, computation stops. The solution is to
    change (increase or reduce) the slope value by increasing or decreasing it.
    """

    FairCurve_OK = 0

    FairCurve_NotConverged = 1

    FairCurve_InfiniteSliding = 2

    FairCurve_NullHeight = 3

FairCurve_OK: FairCurve_AnalysisCode = FairCurve_AnalysisCode.FairCurve_OK

FairCurve_NotConverged: FairCurve_AnalysisCode = FairCurve_AnalysisCode.FairCurve_NotConverged

FairCurve_InfiniteSliding: FairCurve_AnalysisCode = FairCurve_AnalysisCode.FairCurve_InfiniteSliding

FairCurve_NullHeight: FairCurve_AnalysisCode = FairCurve_AnalysisCode.FairCurve_NullHeight

class FairCurve_Batten:
    """
    Constructs curves with a constant or linearly increasing
    section to be used in the design of wooden or plastic
    battens. These curves are two-dimensional, and
    simulate physical splines or battens.
    """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, Height: float, Slope: float = 0.0) -> None:
        """
        Constructor with the two points and the geometrical
        characteristics of the batten (elastic beam)
        Height is the height of the deformation, and Slope is the
        slope value, initialized at 0. The user can then supply the
        desired slope value by the method, SetSlope.
        Other parameters are initialized as follow :
        - FreeSliding = False
        - ConstraintOrder1 = 1
        - ConstraintOrder2 = 1
        - Angle1 = 0
        - Angle2 = 0
        - SlidingFactor = 1
        Exceptions
        NegativeValue if Height is less than or equal to 0.
        NullValue if the distance between P1 and P2 is less
        than or equal to the tolerance value for distance in
        Precision::Confusion: P1.IsEqual(P2,
        Precision::Confusion()). The function
        gp_Pnt2d::IsEqual tests to see if this is the case.
        """

    @overload
    def __init__(self, theOther: FairCurve_Batten) -> None: ...

    def SetFreeSliding(self, FreeSliding: bool) -> None:
        """
        Freesliding is initialized with the default setting false.
        When Freesliding is set to true and, as a result, sliding
        is free, the sliding factor is automatically computed to
        satisfy the equilibrium of the batten.
        """

    def SetConstraintOrder1(self, ConstraintOrder: int) -> None:
        """
        Allows you to change the order of the constraint on the
        first point. ConstraintOrder has the default setting of 1.
        The following settings are available:
        -   0-the curve must pass through a point
        -   1-the curve must pass through a point and have a given tangent
        -   2-the curve must pass through a point, have a given tangent and a given curvature.
        The third setting is only valid for
        FairCurve_MinimalVariation curves.
        These constraints, though geometric, represent the
        mechanical constraints due, for example, to the
        resistance of the material the actual physical batten is made of.
        """

    def SetConstraintOrder2(self, ConstraintOrder: int) -> None:
        """
        Allows you to change the order of the constraint on the
        second point. ConstraintOrder is initialized with the default setting of 1.
        The following settings are available:
        -   0-the curve must pass through a point
        -   1-the curve must pass through a point and have a given tangent
        -   2-the curve must pass through a point, have a given
        tangent and a given curvature.
        The third setting is only valid for
        FairCurve_MinimalVariation curves.
        These constraints, though geometric, represent the
        mechanical constraints due, for example, to the
        resistance of the material the actual physical batten is made of.
        """

    def SetP1(self, P1: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Allows you to change the location of the point, P1, and in
        doing so, modify the curve.
        Warning
        This method changes the angle as well as the point.
        Exceptions
        NullValue if the distance between P1 and P2 is less
        than or equal to the tolerance value for distance in
        Precision::Confusion: P1.IsEqual(P2,
        Precision::Confusion()). The function
        gp_Pnt2d::IsEqual tests to see if this is the case.
        """

    def SetP2(self, P2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Allows you to change the location of the point, P1, and in
        doing so, modify the curve.
        Warning
        This method changes the angle as well as the point.
        Exceptions
        NullValue if the distance between P1 and P2 is less
        than or equal to the tolerance value for distance in
        Precision::Confusion: P1.IsEqual(P2,
        Precision::Confusion()). The function
        gp_Pnt2d::IsEqual tests to see if this is the case.
        """

    def SetAngle1(self, Angle1: float) -> None:
        """
        Allows you to change the angle Angle1 at the first point,
        P1. The default setting is 0.
        """

    def SetAngle2(self, Angle2: float) -> None:
        """
        Allows you to change the angle Angle2 at the second
        point, P2. The default setting is 0.
        """

    def SetHeight(self, Height: float) -> None:
        """
        Allows you to change the height of the deformation.
        Raises NegativeValue; -- if Height <= 0
        if Height <= 0
        """

    def SetSlope(self, Slope: float) -> None:
        """Allows you to set the slope value, Slope."""

    def SetSlidingFactor(self, SlidingFactor: float) -> None:
        """
        Allows you to change the ratio SlidingFactor. This
        compares the length of the batten and the reference
        length, which is, in turn, a function of the constraints.
        This modification has one of the following two effects:
        -   if you increase the value, it inflates the batten
        -   if you decrease the value, it flattens the batten.
        When sliding is free, the sliding factor is automatically
        computed to satisfy the equilibrium of the batten. When
        sliding is imposed, a value is required for the sliding factor.
        SlidingFactor is initialized with the default setting of 1.
        """

    def Compute(self, NbIterations: int = 50, Tolerance: float = 0.001) -> tuple[bool, FairCurve_AnalysisCode]:
        """
        Performs the algorithm, using the arguments Code,
        NbIterations and Tolerance and computes the curve
        with respect to the constraints.
        Code will have one of the following values:
        -   OK
        -   NotConverged
        -   InfiniteSliding
        -   NullHeight
        The parameters Tolerance and NbIterations control
        how precise the computation is, and how long it will take.
        """

    def SlidingOfReference(self) -> float:
        """
        Computes the real number value for length Sliding of
        Reference for new constraints. If you want to give a
        specific length to a batten curve, use the following
        syntax: b.SetSlidingFactor(L /
        b.SlidingOfReference()) where b is the
        name of the batten curve object.
        """

    def GetFreeSliding(self) -> bool:
        """
        Returns the initial free sliding value, false by default.
        Free sliding is generally more aesthetically pleasing
        than constrained sliding. However, the computation can
        fail with values such as angles greater than PI/2. This is
        because the resulting batten length is theoretically infinite.
        """

    def GetConstraintOrder1(self) -> int:
        """Returns the established first constraint order."""

    def GetConstraintOrder2(self) -> int:
        """Returns the established second constraint order."""

    def GetP1(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the established location of the point P1."""

    def GetP2(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the established location of the point P2."""

    def GetAngle1(self) -> float:
        """Returns the established first angle."""

    def GetAngle2(self) -> float:
        """Returns the established second angle."""

    def GetHeight(self) -> float:
        """Returns the thickness of the lathe."""

    def GetSlope(self) -> float:
        """Returns the established slope value."""

    def GetSlidingFactor(self) -> float:
        """Returns the initial sliding factor."""

    def Curve(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """Returns the computed curve a 2d BSpline."""

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.

        Private methodes --------------------------------------
        """

class FairCurve_BattenLaw(nanoocp.math.math_Function):
    """This class compute the Heigth of an batten"""

    @overload
    def __init__(self, Heigth: float, Slope: float, Sliding: float) -> None:
        """
        Constructor of linear batten with
        Heigth  : the Heigth at the middle point
        Slope   : the geometric slope of the batten
        Sliding : Active Length of the batten without extension
        """

    @overload
    def __init__(self, theOther: FairCurve_BattenLaw) -> None: ...

    def SetSliding(self, Sliding: float) -> None:
        """Change the value of sliding"""

    def SetHeigth(self, Heigth: float) -> None:
        """Change the value of Heigth at the middle point."""

    def SetSlope(self, Slope: float) -> None:
        """Change the value of the geometric slope."""

    def Value(self, T: float) -> tuple[bool, float]:
        """
        computes the value of the heigth for the parameter T
        on the neutral fibber
        """

class FairCurve_DistributionOfEnergy(nanoocp.math.math_FunctionSet):
    """Abstract class to use the Energy of an FairCurve"""

    def NbVariables(self) -> int:
        """returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    def SetDerivativeOrder(self, DerivativeOrder: int) -> None: ...

class FairCurve_DistributionOfJerk(FairCurve_DistributionOfEnergy):
    """Compute the "Jerk" distribution."""

    @overload
    def __init__(self, BSplOrder: int, FlatKnots: nanoocp.NCollection.NCollection_HArray1[float] | None, Poles: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, DerivativeOrder: int, Law: FairCurve_BattenLaw, NbValAux: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: FairCurve_DistributionOfJerk) -> None: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

class FairCurve_DistributionOfSagging(FairCurve_DistributionOfEnergy):
    """Compute the Sagging Distribution"""

    @overload
    def __init__(self, BSplOrder: int, FlatKnots: nanoocp.NCollection.NCollection_HArray1[float] | None, Poles: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, DerivativeOrder: int, Law: FairCurve_BattenLaw, NbValAux: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: FairCurve_DistributionOfSagging) -> None: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

class FairCurve_DistributionOfTension(FairCurve_DistributionOfEnergy):
    """Compute the Tension Distribution"""

    @overload
    def __init__(self, BSplOrder: int, FlatKnots: nanoocp.NCollection.NCollection_HArray1[float] | None, Poles: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, DerivativeOrder: int, LengthSliding: float, Law: FairCurve_BattenLaw, NbValAux: int = 0, Uniform: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: FairCurve_DistributionOfTension) -> None: ...

    def SetLengthSliding(self, LengthSliding: float) -> None:
        """change the length sliding"""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

class FairCurve_Energy(nanoocp.math.math_MultipleVarFunctionWithHessian):
    """necessary methodes to compute the energy of an FairCurve."""

    def NbVariables(self) -> int:
        """returns the number of variables of the energy."""

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        computes the values of the Energys E for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """
        computes the gradient <G> of the energys for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        computes the Energy <E> and the gradient <G> of the
        energy for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector, H: nanoocp.math.math_Matrix) -> tuple[bool, float]:
        """
        computes the Energy <E>, the gradient <G> and the
        Hessian <H> of the energy for the variable <X>.
        Returns True if the computation was done
        successfully, False otherwise.
        """

    def Variable(self, X: nanoocp.math.math_Vector) -> bool:
        """compute the variables <X> which correspond with the field <MyPoles>"""

    def Poles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d]:
        """return the poles"""

class FairCurve_EnergyOfBatten(FairCurve_Energy):
    """Energy Criterium to minimize in Batten."""

    @overload
    def __init__(self, BSplOrder: int, FlatKnots: nanoocp.NCollection.NCollection_HArray1[float] | None, Poles: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, ContrOrder1: int, ContrOrder2: int, Law: FairCurve_BattenLaw, LengthSliding: float, FreeSliding: bool = True, Angle1: float = 0.0, Angle2: float = 0.0) -> None:
        """Angles correspond to the Ox axis"""

    @overload
    def __init__(self, theOther: FairCurve_EnergyOfBatten) -> None: ...

    def LengthSliding(self) -> float:
        """return the lengthSliding = P1P2 + Sliding"""

    def Status(self) -> FairCurve_AnalysisCode:
        """return the status"""

    def Variable(self, X: nanoocp.math.math_Vector) -> bool:
        """compute the variables <X> which correspond with the field <MyPoles>"""

class FairCurve_EnergyOfMVC(FairCurve_Energy):
    """Energy Criterium to minimize in MinimalVariationCurve."""

    @overload
    def __init__(self, BSplOrder: int, FlatKnots: nanoocp.NCollection.NCollection_HArray1[float] | None, Poles: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, ContrOrder1: int, ContrOrder2: int, Law: FairCurve_BattenLaw, PhysicalRatio: float, LengthSliding: float, FreeSliding: bool = True, Angle1: float = 0.0, Angle2: float = 0.0, Curvature1: float = 0.0, Curvature2: float = 0.0) -> None:
        """Angles correspond to the Ox axis"""

    @overload
    def __init__(self, theOther: FairCurve_EnergyOfMVC) -> None: ...

    def LengthSliding(self) -> float:
        """return the lengthSliding = P1P2 + Sliding"""

    def Status(self) -> FairCurve_AnalysisCode:
        """return the status"""

    def Variable(self, X: nanoocp.math.math_Vector) -> bool:
        """compute the variables <X> which correspond with the field <MyPoles>"""

class FairCurve_MinimalVariation(FairCurve_Batten):
    """
    Computes a 2D curve using an algorithm which
    minimizes tension, sagging, and jerk energy. As in
    FairCurve_Batten, two reference points are used.
    Unlike that class, FairCurve_MinimalVariation
    requires curvature settings at the first and second
    reference points. These are defined by the rays of
    curvature desired at each point.
    """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, Heigth: float, Slope: float = 0.0, PhysicalRatio: float = 0.0) -> None:
        """
        Constructs the two contact points P1 and P2 and the geometrical
        characteristics of the batten (elastic beam)
        These include the real number values for height of
        deformation Height, slope value Slope, and kind of
        energy PhysicalRatio. The kinds of energy include:
        -   Jerk (0)
        -   Sagging (1).
        Note that the default setting for Physical Ration is in FairCurve_Batten
        Other parameters are initialized as follow :
        - FreeSliding = False
        - ConstraintOrder1 = 1
        - ConstraintOrder2 = 1
        - Angle1 = 0
        - Angle2 = 0
        - Curvature1 = 0
        - Curvature2 = 0
        - SlidingFactor = 1
        Warning
        If PhysicalRatio equals 1, you cannot impose constraints on curvature.
        Exceptions
        NegativeValue if Height is less than or equal to 0.
        NullValue if the distance between P1 and P2 is less
        than or equal to the tolerance value for distance in
        Precision::Confusion: P1.IsEqual(P2,
        Precision::Confusion()). The function
        gp_Pnt2d::IsEqual tests to see if this is the case.
        Definition of the geometricals constraints
        """

    @overload
    def __init__(self, theOther: FairCurve_MinimalVariation) -> None: ...

    def SetCurvature1(self, Curvature: float) -> None:
        """Allows you to set a new constraint on curvature at the first point."""

    def SetCurvature2(self, Curvature: float) -> None:
        """Allows you to set a new constraint on curvature at the second point."""

    def SetPhysicalRatio(self, Ratio: float) -> None:
        """
        Allows you to set the physical ratio Ratio.
        The kinds of energy which you can specify include:
        0 is only "Jerk" Energy
        1 is only "Sagging" Energy like batten
        Warning: if Ratio is 1 it is impossible to impose curvature constraints.
        Raises DomainError if Ratio < 0 or Ratio > 1
        """

    def Compute(self, NbIterations: int = 50, Tolerance: float = 0.001) -> tuple[bool, FairCurve_AnalysisCode]:
        """
        Computes the curve with respect to the constraints,
        NbIterations and Tolerance. The tolerance setting
        allows you to control the precision of computation, and
        the maximum number of iterations allows you to set a limit on computation time.
        """

    def GetCurvature1(self) -> float:
        """Returns the first established curvature."""

    def GetCurvature2(self) -> float:
        """Returns the second established curvature."""

    def GetPhysicalRatio(self) -> float:
        """Returns the physical ratio, or kind of energy."""

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class FairCurve_Newton(nanoocp.math.math_NewtonMinimum):
    """Algorithm of Optimization used to make "FairCurve\""""

    @overload
    def __init__(self, theFunction: nanoocp.math.math_MultipleVarFunctionWithHessian, theSpatialTolerance: float = 1e-07, theCriteriumTolerance: float = 1e-07, theNbIterations: int = 40, theConvexity: float = 1e-06, theWithSingularity: bool = True) -> None:
        """
        The tolerance required on the solution is given by Tolerance.
        Iteration are stopped if (!WithSingularity) and H(F(Xi)) is not definite
        positive (if the smaller eigenvalue of H < Convexity)
        or IsConverged() returns True for 2 successives Iterations.
        Warning: This constructor do not computation
        """

    @overload
    def __init__(self, theOther: FairCurve_Newton) -> None: ...

    def IsConverged(self) -> bool:
        """
        This method is called at the end of each
        iteration to check the convergence:
        || Xi+1 - Xi || < SpatialTolerance/100 Or
        || Xi+1 - Xi || < SpatialTolerance and
        |F(Xi+1) - F(Xi)| < CriteriumTolerance * |F(xi)|
        It can be redefined in a sub-class to implement a specific test.
        """
