"""OCCT package AppDef (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.AppParCurves
import nanoocp.Approx
import nanoocp.FEmTool
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class AppDef_BSpGradient_BFGSOfMyBSplGradientOfBSplineCompute(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: AppDef_BSpGradient_BFGSOfMyBSplGradientOfBSplineCompute) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class AppDef_BSplineCompute:
    @overload
    def __init__(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None: ...

    @overload
    def __init__(self, Line: AppDef_MultiLine, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        If <Squares> is True, the computation will be done with
        no iteration at all.

        The multiplicities of the internal knots is set by
        default.
        """

    @overload
    def __init__(self, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    @overload
    def __init__(self, Line: AppDef_MultiLine, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        If <Squares> is True, the computation will be done with
        no iteration at all.
        """

    @overload
    def __init__(self, theOther: AppDef_BSplineCompute) -> None: ...

    def Interpol(self, Line: AppDef_MultiLine) -> None:
        """
        Constructs an interpolation of the MultiLine <Line>
        The result will be a C2 curve of degree 3.
        """

    def Init(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, Line: AppDef_MultiLine) -> None:
        """runs the algorithm after having initialized the fields."""

    def SetParameters(self, ThePar: nanoocp.math.math_Vector) -> None:
        """
        The approximation will begin with the
        set of parameters <ThePar>.
        """

    def SetKnots(self, Knots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        The approximation will be done with the
        set of knots <Knots>. The multiplicities will be set
        with the degree and the desired continuity.
        """

    def SetKnotsAndMultiplicities(self, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        The approximation will be done with the
        set of knots <Knots> and the multiplicities <Mults>.
        """

    def SetDegrees(self, degreemin: int, degreemax: int) -> None:
        """changes the degrees of the approximation."""

    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None:
        """Changes the tolerances of the approximation."""

    def SetContinuity(self, C: int) -> None:
        """
        sets the continuity of the spline.
        if C = 2, the spline will be C2.
        """

    def SetConstraints(self, firstC: nanoocp.AppParCurves.AppParCurves_Constraint, lastC: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """changes the first and the last constraint points."""

    def SetPeriodic(self, thePeriodic: bool) -> None:
        """
        Sets periodic flag.
        If thePeriodic = true, algorithm tries to build periodic
        multicurve using corresponding C1 boundary condition for first and last multipoints.
        Multiline must be closed.
        """

    def IsAllApproximated(self) -> bool:
        """
        returns False if at a moment of the approximation,
        the status NoApproximation has been sent by the user
        when more points were needed.
        """

    def IsToleranceReached(self) -> bool:
        """returns False if the status NoPointsAdded has been sent."""

    def Error(self) -> tuple[float, float]:
        """returns the tolerances 2d and 3d of the MultiBSpCurve."""

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """returns the result of the approximation."""

    def ChangeValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """returns the result of the approximation."""

    def Parameters(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        returns the new parameters of the approximation
        corresponding to the points of the MultiBSpCurve.
        """

class AppDef_MultiPointConstraint(nanoocp.AppParCurves.AppParCurves_MultiPoint):
    """
    Describes a MultiPointConstraint used in a
    Multiline. MultiPointConstraints are composed
    of several two or three-dimensional points.
    The purpose is to define the corresponding
    points that share a common constraint in order
    to compute the approximation of several lines in parallel.
    Notes:
    -   The order of points of a MultiPointConstraints is very important.
    Users must give 3D points first, and then 2D points.
    -   The constraints for the points included in a
    MultiPointConstraint are always identical for
    all points, including the parameter.
    -   If a MultiPointConstraint is a "tangency"
    point, the point is also a "passing" point.
    """

    @overload
    def __init__(self) -> None:
        """creates an undefined MultiPointConstraint."""

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """creates a MultiPoint only composed of 3D points."""

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """creates a MultiPoint only composed of 2D points."""

    @overload
    def __init__(self, NbPoints: int, NbPoints2d: int) -> None: ...

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        constructs a set of Points used to approximate a Multiline.
        These Points can be of 2 or 3 dimensions.
        Points will be initialized with SetPoint and SetPoint2d.
        """

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabVec: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> None:
        """
        creates a MultiPointConstraint only composed of 3d points
        with constraints of tangency.
        An exception is raised if the length of tabP is different
        from the length of tabVec.
        """

    @overload
    def __init__(self, tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], tabVec2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> None:
        """
        creates a MultiPointConstraint only composed of 2d points
        with constraints of tangency.
        An exception is raised if the length of tabP is different
        from the length of tabVec2d.
        """

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabVec: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabCur: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> None:
        """
        creates a MultiPointConstraint only composed of 3d points
        with constraints of curvature.
        An exception is raised if the length of tabP is different
        from the length of tabVec or from tabCur.
        """

    @overload
    def __init__(self, tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], tabVec2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], tabCur2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> None:
        """
        creates a MultiPointConstraint only composed of 2d points
        with constraints of curvature.
        An exception is raised if the length of tabP is different
        from the length of tabVec2d or from tabCur2d.
        """

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], tabVec: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabVec2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> None:
        """
        creates a MultiPointConstraint with a constraint of
        Tangency.
        An exception is raised if
        (length of <tabP> + length of <tabP2d> ) is different
        from (length of <tabVec> + length of <tabVec2d> )
        """

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], tabVec: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabVec2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], tabCur: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabCur2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> None:
        """
        creates a MultiPointConstraint with a constraint of
        Curvature.
        An exception is raised if
        (length of <tabP> + length of <tabP2d> ) is different
        from (length of <tabVec> + length of <tabVec2d> ) or
        from (length of <tabCur> + length of <tabCur2d> )
        """

    @overload
    def __init__(self, theOther: AppDef_MultiPointConstraint) -> None: ...

    def SetTang(self, Index: int, Tang: nanoocp.gp.gp_Vec) -> None:
        """
        sets the value of the tangency of the point of range
        Index.
        An exception is raised if Index <0 or if Index > number
        of 3d points.
        An exception is raised if Tang has an incorrect number of
        dimensions.
        """

    def Tang(self, Index: int) -> nanoocp.gp.gp_Vec:
        """
        returns the tangency value of the point of range Index.
        An exception is raised if Index < 0 or if Index > number
        of 3d points.
        """

    def SetTang2d(self, Index: int, Tang2d: nanoocp.gp.gp_Vec2d) -> None:
        """
        sets the value of the tangency of the point of range
        Index.
        An exception is raised if Index <number of 3d points or if
        Index > total number of Points
        An exception is raised if Tang has an incorrect number of
        dimensions.
        """

    def Tang2d(self, Index: int) -> nanoocp.gp.gp_Vec2d:
        """
        returns the tangency value of the point of range Index.
        An exception is raised if Index < number of 3d points or
        if Index > total number of points.
        """

    def SetCurv(self, Index: int, Curv: nanoocp.gp.gp_Vec) -> None:
        """
        Vec sets the value of the normal vector at the
        point of index Index. The norm of the normal
        vector at the point of position Index is set to the normal curvature.
        An exception is raised if Index <0 or if Index > number
        of 3d points.
        An exception is raised if Curv has an incorrect number of
        dimensions.
        """

    def Curv(self, Index: int) -> nanoocp.gp.gp_Vec:
        """
        returns the normal vector at the point of range Index.
        An exception is raised if Index < 0 or if Index > number
        of 3d points.
        """

    def SetCurv2d(self, Index: int, Curv2d: nanoocp.gp.gp_Vec2d) -> None:
        """
        Vec sets the value of the normal vector at the
        point of index Index. The norm of the normal
        vector at the point of position Index is set to the normal curvature.
        An exception is raised if Index <0 or if Index > number
        of 3d points.
        An exception is raised if Curv has an incorrect number of
        dimensions.
        """

    def Curv2d(self, Index: int) -> nanoocp.gp.gp_Vec2d:
        """
        returns the normal vector at the point of range Index.
        An exception is raised if Index < 0 or if Index > number
        of 3d points.
        """

    def IsTangencyPoint(self) -> bool:
        """returns True if the MultiPoint has a tangency value."""

    def IsCurvaturePoint(self) -> bool:
        """returns True if the MultiPoint has a curvature value."""

class AppDef_MultiLine:
    """
    This class describes the organized set of points used in the
    approximations. A MultiLine is composed of n
    MultiPointConstraints.
    The approximation of the MultiLine will be done in the order
    of the given n MultiPointConstraints.

    Example of a MultiLine composed of MultiPointConstraints:

    P1______P2_____P3______P4________........_____PNbMult

    Q1______Q2_____Q3______Q4________........_____QNbMult
    .                                               .
    .                                               .
    .                                               .
    R1______R2_____R3______R4________........_____RNbMult

    Pi, Qi, ..., Ri are points of dimension 2 or 3.

    (P1, Q1, ...R1), ...(Pn, Qn, ...Rn) n= 1,...NbMult are
    MultiPointConstraints.
    There are NbPoints points in each MultiPointConstraint.
    """

    @overload
    def __init__(self) -> None:
        """creates an undefined MultiLine."""

    @overload
    def __init__(self, NbMult: int) -> None:
        """
        given the number NbMult of MultiPointConstraints of this
        MultiLine, it initializes all the fields.SetValue must be
        called in order for the values of the multipoint
        constraint to be taken into account.
        An exception is raised if NbMult < 0.
        """

    @overload
    def __init__(self, tabMultiP: nanoocp.NCollection.NCollection_Array1[nanoocp.AppDef.AppDef_MultiPointConstraint]) -> None:
        """Constructs a MultiLine with an array of MultiPointConstraints."""

    @overload
    def __init__(self, tabP3d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        The MultiLine constructed will have one line of
        3d points without their tangencies.
        """

    @overload
    def __init__(self, tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        The MultiLine constructed will have one line of
        2d points without their tangencies.
        """

    @overload
    def __init__(self, theOther: AppDef_MultiLine) -> None: ...

    def NbMultiPoints(self) -> int:
        """
        returns the number of MultiPointConstraints of the
        MultiLine.
        """

    def NbPoints(self) -> int:
        """
        returns the number of Points from MultiPoints composing
        the MultiLine.
        """

    def SetValue(self, Index: int, MPoint: AppDef_MultiPointConstraint) -> None:
        """
        It sets the MultiPointConstraint of range Index to the
        value MPoint.
        An exception is raised if Index < 0 or Index> MPoint.
        An exception is raised if the dimensions of the
        MultiPoints are different.
        """

    def Value(self, Index: int) -> AppDef_MultiPointConstraint:
        """
        returns the MultiPointConstraint of range Index
        An exception is raised if Index<0 or Index>MPoint.
        """

class AppDef_BSpParLeastSquareOfMyBSplGradientOfBSplineCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        NbPol is the number of control points wanted
        for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the Bernstein matrix computed with the
        parameters, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        Deg is the degree wanted for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the BSpline functions matrix computed with
        <parameters>, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, theOther: AppDef_BSpParLeastSquareOfMyBSplGradientOfBSplineCompute) -> None: ...

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector) -> None:
        """
        Is used after having initialized the fields.
        The case "CurvaturePoint" is not treated in this method.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """Is used after having initialized the fields."""

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, V1c: nanoocp.math.math_Vector, V2c: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        <V1c> is the tangent vector at the first point.
        <V2c> is the tangent vector at the last point.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def BezierValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def BSplineValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def FunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the function matrix used to approximate the
        set.
        """

    def DerivativeFunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the derivative function matrix used
        to approximate the set.
        """

    def ErrorGradient(self, Grad: nanoocp.math.math_Vector) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances. Grad is the derivative vector of the
        function F.
        """

    def Distance(self) -> nanoocp.math.math_Matrix:
        """
        returns the distances between the points of the
        multiline and the approximation curves.
        """

    def Error(self) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances.
        """

    def FirstLambda(self) -> float:
        """
        returns the value (P2 - P1)/ V1 if the first point
        was a tangency point.
        """

    def LastLambda(self) -> float:
        """
        returns the value (PN - PN-1)/ VN if the last point
        was a tangency point.
        """

    def Points(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of points value."""

    def Poles(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of resulting control points value."""

    def KIndex(self) -> nanoocp.math.math_IntegerVector:
        """
        Returns the indexes of the first non null values of
        A and DA.
        The values are non null from Index(ieme point) +1
        to Index(ieme point) + degree +1.
        """

class AppDef_BSpParFunctionOfMyBSplGradientOfBSplineCompute(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NbPol: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has <NbPol> control points.
        """

    @overload
    def __init__(self, theOther: AppDef_BSpParFunctionOfMyBSplGradientOfBSplineCompute) -> None: ...

    def NbVariables(self) -> int:
        """
        returns the number of variables of the function. It
        corresponds to the number of MultiPoints.
        """

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        this method computes the new approximation of the
        MultiLine
        SSP and calculates F = sum (||Pui - Bi*Pi||2) for each
        point of the MultiLine.
        """

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """
        returns the gradient G of the sum above for the
        parameters Xi.
        """

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        returns the value F=sum(||Pui - Bi*Pi||)2.
        returns the value G = grad(F) for the parameters Xi.
        """

    def NewParameters(self) -> nanoocp.math.math_Vector:
        """returns the new parameters of the MultiLine."""

    def CurveValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns the MultiBSpCurve approximating the set after
        computing the value F or Grad(F).
        """

    def Error(self, IPoint: int, CurveIndex: int) -> float:
        """
        returns the distance between the MultiPoint of range
        IPoint and the curve CurveIndex.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiBSpCurve.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiBSpCurve.
        """

    def FunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the function matrix used to approximate the
        multiline.
        """

    def DerivativeFunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the derivative function matrix used to approximate the
        multiline.
        """

    def Index(self) -> nanoocp.math.math_IntegerVector:
        """
        Returns the indexes of the first non null values of
        A and DA.
        The values are non null from Index(ieme point) +1
        to Index(ieme point) + degree +1.
        """

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def SetFirstLambda(self, l1: float) -> None: ...

    def SetLastLambda(self, l2: float) -> None: ...

class AppDef_Compute:
    @overload
    def __init__(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None: ...

    @overload
    def __init__(self, Line: AppDef_MultiLine, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None: ...

    @overload
    def __init__(self, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    @overload
    def __init__(self, Line: AppDef_MultiLine, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        If <Squares> is True, the computation will be done with
        no iteration at all.
        """

    @overload
    def __init__(self, theOther: AppDef_Compute) -> None: ...

    def Init(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, Line: AppDef_MultiLine) -> None:
        """runs the algorithm after having initialized the fields."""

    def SetDegrees(self, degreemin: int, degreemax: int) -> None:
        """changes the degrees of the approximation."""

    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None:
        """Changes the tolerances of the approximation."""

    def SetConstraints(self, firstC: nanoocp.AppParCurves.AppParCurves_Constraint, lastC: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """changes the first and the last constraint points."""

    def IsAllApproximated(self) -> bool:
        """
        returns False if at a moment of the approximation,
        the status NoApproximation has been sent by the user
        when more points were needed.
        """

    def IsToleranceReached(self) -> bool:
        """returns False if the status NoPointsAdded has been sent."""

    def Error(self, Index: int) -> tuple[float, float]:
        """returns the tolerances 2d and 3d of the <Index> MultiCurve."""

    def NbMultiCurves(self) -> int:
        """
        Returns the number of MultiCurve doing the approximation
        of the MultiLine.
        """

    def Value(self, Index: int = 1) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """returns the result of the approximation."""

    def ChangeValue(self, Index: int = 1) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """returns the result of the approximation."""

    def SplineValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """returns the result of the approximation."""

    def Parametrization(self) -> nanoocp.Approx.Approx_ParametrizationType:
        """returns the type of parametrization"""

    def Parameters(self, Index: int = 1) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        returns the new parameters of the approximation
        corresponding to the points of the multicurve <Index>.
        """

class AppDef_Gradient_BFGSOfMyGradientbisOfBSplineCompute(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: AppDef_Gradient_BFGSOfMyGradientbisOfBSplineCompute) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class AppDef_Gradient_BFGSOfMyGradientOfCompute(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: AppDef_Gradient_BFGSOfMyGradientOfCompute) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class AppDef_Gradient_BFGSOfTheGradient(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: AppDef_Gradient_BFGSOfTheGradient) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class AppDef_SmoothCriterion(nanoocp.Standard.Standard_Transient):
    """defined criterion to smooth points in curve"""

    def SetParameters(self, Parameters: nanoocp.NCollection.NCollection_HArray1[float]) -> None: ...

    def SetCurve(self, C: nanoocp.FEmTool.FEmTool_Curve) -> None: ...

    def Curve(self) -> nanoocp.FEmTool.FEmTool_Curve:
        """
        Returns the curve associated with this criterion.
        @return handle to the FEmTool curve
        """

    def GetCurve(self, C: nanoocp.FEmTool.FEmTool_Curve) -> None: ...

    def SetEstimation(self, E1: float, E2: float, E3: float) -> None: ...

    def EstLength(self) -> float: ...

    def SetEstLength(self, theValue: float) -> None:
        """
        Python addition: sets the value EstLength() returns by reference in C++.
        """

    def GetEstimation(self) -> tuple[float, float, float]: ...

    def AssemblyTable(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]]: ...

    def DependenceTable(self) -> nanoocp.NCollection.NCollection_HArray2[int]: ...

    def QualityValues(self, J1min: float, J2min: float, J3min: float) -> tuple[int, float, float, float]: ...

    def ErrorValues(self) -> tuple[float, float, float]: ...

    def Hessian(self, Element: int, Dimension1: int, Dimension2: int, H: nanoocp.math.math_Matrix) -> None: ...

    def Gradient(self, Element: int, Dimension: int, G: nanoocp.math.math_Vector) -> None: ...

    def InputVector(self, X: nanoocp.math.math_Vector, AssTable: nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]]) -> None:
        """Convert the assembly Vector in an Curve;"""

    @overload
    def SetWeight(self, QuadraticWeight: float, QualityWeight: float, percentJ1: float, percentJ2: float, percentJ3: float) -> None: ...

    @overload
    def SetWeight(self, Weight: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def GetWeight(self) -> tuple[float, float]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AppDef_LinearCriteria(AppDef_SmoothCriterion):
    """
    defined an Linear Criteria to used in variational
    Smoothing of points.
    """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int) -> None: ...

    @overload
    def __init__(self, theOther: AppDef_LinearCriteria) -> None: ...

    def SetParameters(self, Parameters: nanoocp.NCollection.NCollection_HArray1[float]) -> None: ...

    def SetCurve(self, C: nanoocp.FEmTool.FEmTool_Curve) -> None: ...

    def GetCurve(self, C: nanoocp.FEmTool.FEmTool_Curve) -> None: ...

    def SetEstimation(self, E1: float, E2: float, E3: float) -> None: ...

    def EstLength(self) -> float: ...

    def SetEstLength(self, theValue: float) -> None:
        """
        Python addition: sets the value EstLength() returns by reference in C++.
        """

    def GetEstimation(self) -> tuple[float, float, float]: ...

    def AssemblyTable(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]]: ...

    def DependenceTable(self) -> nanoocp.NCollection.NCollection_HArray2[int]: ...

    def QualityValues(self, J1min: float, J2min: float, J3min: float) -> tuple[int, float, float, float]: ...

    def ErrorValues(self) -> tuple[float, float, float]: ...

    def Hessian(self, Element: int, Dimension1: int, Dimension2: int, H: nanoocp.math.math_Matrix) -> None: ...

    def Gradient(self, Element: int, Dimension: int, G: nanoocp.math.math_Vector) -> None: ...

    def InputVector(self, X: nanoocp.math.math_Vector, AssTable: nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]]) -> None:
        """Convert the assembly Vector in an Curve;"""

    @overload
    def SetWeight(self, QuadraticWeight: float, QualityWeight: float, percentJ1: float, percentJ2: float, percentJ3: float) -> None: ...

    @overload
    def SetWeight(self, Weight: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def GetWeight(self) -> tuple[float, float]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AppDef_MyBSplGradientOfBSplineCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 1) -> None: ...

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Deg: int, Tol3d: float, Tol2d: float, NbIterations: int, lambda1: float, lambda2: float) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating BSpline curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_MyBSplGradientOfBSplineCompute) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns all the BSpline curves approximating the
        MultiLine SSP after minimization of the parameter.
        """

    def Error(self, Index: int) -> float:
        """
        returns the difference between the old and the new
        approximation.
        An exception is raised if NotDone.
        An exception is raised if Index<1 or Index>NbParameters.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def AverageError(self) -> float:
        """
        returns the average error between the old and the
        new approximation.
        """

class AppDef_MyGradientbisOfBSplineCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 200) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating Bezier curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_MyGradientbisOfBSplineCompute) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns all the Bezier curves approximating the
        MultiLine SSP after minimization of the parameter.
        """

    def Error(self, Index: int) -> float:
        """
        returns the difference between the old and the new
        approximation.
        An exception is raised if NotDone.
        An exception is raised if Index<1 or Index>NbParameters.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def AverageError(self) -> float:
        """
        returns the average error between the old and the
        new approximation.
        """

class AppDef_MyGradientOfCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 200) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating Bezier curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_MyGradientOfCompute) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns all the Bezier curves approximating the
        MultiLine SSP after minimization of the parameter.
        """

    def Error(self, Index: int) -> float:
        """
        returns the difference between the old and the new
        approximation.
        An exception is raised if NotDone.
        An exception is raised if Index<1 or Index>NbParameters.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def AverageError(self) -> float:
        """
        returns the average error between the old and the
        new approximation.
        """

class AppDef_MyLineTool:
    """
    Example of MultiLine tool corresponding to the tools of the packages AppParCurves and Approx.
    For Approx, the tool will not add points if the algorithms want some.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AppDef_MyLineTool) -> None: ...

    @staticmethod
    def FirstPoint(ML: AppDef_MultiLine) -> int:
        """Returns the first index of multipoints of the MultiLine."""

    @staticmethod
    def LastPoint(ML: AppDef_MultiLine) -> int:
        """Returns the last index of multipoints of the MultiLine."""

    @staticmethod
    def NbP2d(ML: AppDef_MultiLine) -> int:
        """Returns the number of 2d points of a MultiLine."""

    @staticmethod
    def NbP3d(ML: AppDef_MultiLine) -> int:
        """Returns the number of 3d points of a MultiLine."""

    @overload
    @staticmethod
    def Value(ML: AppDef_MultiLine, MPointIndex: int, tabPt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        returns the 3d points of the multipoint <MPointIndex>
        when only 3d points exist.
        """

    @overload
    @staticmethod
    def Value(ML: AppDef_MultiLine, MPointIndex: int, tabPt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        returns the 2d points of the multipoint <MPointIndex>
        when only 2d points exist.
        """

    @overload
    @staticmethod
    def Value(ML: AppDef_MultiLine, MPointIndex: int, tabPt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabPt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        returns the 3d and 2d points of the multipoint
        <MPointIndex>.
        """

    @overload
    @staticmethod
    def Tangency(ML: AppDef_MultiLine, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """
        returns the 3d points of the multipoint <MPointIndex>
        when only 3d points exist.
        """

    @overload
    @staticmethod
    def Tangency(ML: AppDef_MultiLine, MPointIndex: int, tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 2d tangency points of the multipoint
        <MPointIndex> only when 2d points exist.
        """

    @overload
    @staticmethod
    def Tangency(ML: AppDef_MultiLine, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 3d and 2d points of the multipoint
        <MPointIndex>.
        """

    @overload
    @staticmethod
    def Curvature(ML: AppDef_MultiLine, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """
        returns the 3d curvatures of the multipoint <MPointIndex>
        when only 3d points exist.
        """

    @overload
    @staticmethod
    def Curvature(ML: AppDef_MultiLine, MPointIndex: int, tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 2d curvatures of the multipoint
        <MPointIndex> only when 2d points exist.
        """

    @overload
    @staticmethod
    def Curvature(ML: AppDef_MultiLine, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 3d and 2d curvatures of the multipoint
        <MPointIndex>.
        """

    @staticmethod
    def WhatStatus(ML: AppDef_MultiLine, I1: int, I2: int) -> nanoocp.Approx.Approx_Status:
        """returns NoPointsAdded"""

    @staticmethod
    def MakeMLBetween(ML: AppDef_MultiLine, I1: int, I2: int, NbPMin: int) -> AppDef_MultiLine:
        """
        Is never called in the algorithms.
        Nothing is done.
        """

    @staticmethod
    def MakeMLOneMorePoint(ML: AppDef_MultiLine, I1: int, I2: int, indbad: int, OtherLine: AppDef_MultiLine) -> bool:
        """
        Is never called in the algorithms.
        Nothing is done.
        """

class AppDef_ParLeastSquareOfMyGradientbisOfBSplineCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        NbPol is the number of control points wanted
        for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the Bernstein matrix computed with the
        parameters, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        Deg is the degree wanted for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the BSpline functions matrix computed with
        <parameters>, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, theOther: AppDef_ParLeastSquareOfMyGradientbisOfBSplineCompute) -> None: ...

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector) -> None:
        """
        Is used after having initialized the fields.
        The case "CurvaturePoint" is not treated in this method.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """Is used after having initialized the fields."""

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, V1c: nanoocp.math.math_Vector, V2c: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        <V1c> is the tangent vector at the first point.
        <V2c> is the tangent vector at the last point.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def BezierValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def BSplineValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def FunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the function matrix used to approximate the
        set.
        """

    def DerivativeFunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the derivative function matrix used
        to approximate the set.
        """

    def ErrorGradient(self, Grad: nanoocp.math.math_Vector) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances. Grad is the derivative vector of the
        function F.
        """

    def Distance(self) -> nanoocp.math.math_Matrix:
        """
        returns the distances between the points of the
        multiline and the approximation curves.
        """

    def Error(self) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances.
        """

    def FirstLambda(self) -> float:
        """
        returns the value (P2 - P1)/ V1 if the first point
        was a tangency point.
        """

    def LastLambda(self) -> float:
        """
        returns the value (PN - PN-1)/ VN if the last point
        was a tangency point.
        """

    def Points(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of points value."""

    def Poles(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of resulting control points value."""

    def KIndex(self) -> nanoocp.math.math_IntegerVector:
        """
        Returns the indexes of the first non null values of
        A and DA.
        The values are non null from Index(ieme point) +1
        to Index(ieme point) + degree +1.
        """

class AppDef_ParFunctionOfMyGradientbisOfBSplineCompute(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has the desired degree Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_ParFunctionOfMyGradientbisOfBSplineCompute) -> None: ...

    def NbVariables(self) -> int:
        """
        returns the number of variables of the function. It
        corresponds to the number of MultiPoints.
        """

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        this method computes the new approximation of the
        MultiLine
        SSP and calculates F = sum (||Pui - Bi*Pi||2) for each
        point of the MultiLine.
        """

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """
        returns the gradient G of the sum above for the
        parameters Xi.
        """

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        returns the value F=sum(||Pui - Bi*Pi||)2.
        returns the value G = grad(F) for the parameters Xi.
        """

    def NewParameters(self) -> nanoocp.math.math_Vector:
        """returns the new parameters of the MultiLine."""

    def CurveValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the MultiCurve approximating the set after
        computing the value F or Grad(F).
        """

    def Error(self, IPoint: int, CurveIndex: int) -> float:
        """
        returns the distance between the MultiPoint of range
        IPoint and the curve CurveIndex.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

class AppDef_ParLeastSquareOfMyGradientOfCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        NbPol is the number of control points wanted
        for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the Bernstein matrix computed with the
        parameters, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        Deg is the degree wanted for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the BSpline functions matrix computed with
        <parameters>, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, theOther: AppDef_ParLeastSquareOfMyGradientOfCompute) -> None: ...

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector) -> None:
        """
        Is used after having initialized the fields.
        The case "CurvaturePoint" is not treated in this method.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """Is used after having initialized the fields."""

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, V1c: nanoocp.math.math_Vector, V2c: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        <V1c> is the tangent vector at the first point.
        <V2c> is the tangent vector at the last point.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def BezierValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def BSplineValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def FunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the function matrix used to approximate the
        set.
        """

    def DerivativeFunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the derivative function matrix used
        to approximate the set.
        """

    def ErrorGradient(self, Grad: nanoocp.math.math_Vector) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances. Grad is the derivative vector of the
        function F.
        """

    def Distance(self) -> nanoocp.math.math_Matrix:
        """
        returns the distances between the points of the
        multiline and the approximation curves.
        """

    def Error(self) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances.
        """

    def FirstLambda(self) -> float:
        """
        returns the value (P2 - P1)/ V1 if the first point
        was a tangency point.
        """

    def LastLambda(self) -> float:
        """
        returns the value (PN - PN-1)/ VN if the last point
        was a tangency point.
        """

    def Points(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of points value."""

    def Poles(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of resulting control points value."""

    def KIndex(self) -> nanoocp.math.math_IntegerVector:
        """
        Returns the indexes of the first non null values of
        A and DA.
        The values are non null from Index(ieme point) +1
        to Index(ieme point) + degree +1.
        """

class AppDef_ParFunctionOfMyGradientOfCompute(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has the desired degree Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_ParFunctionOfMyGradientOfCompute) -> None: ...

    def NbVariables(self) -> int:
        """
        returns the number of variables of the function. It
        corresponds to the number of MultiPoints.
        """

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        this method computes the new approximation of the
        MultiLine
        SSP and calculates F = sum (||Pui - Bi*Pi||2) for each
        point of the MultiLine.
        """

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """
        returns the gradient G of the sum above for the
        parameters Xi.
        """

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        returns the value F=sum(||Pui - Bi*Pi||)2.
        returns the value G = grad(F) for the parameters Xi.
        """

    def NewParameters(self) -> nanoocp.math.math_Vector:
        """returns the new parameters of the MultiLine."""

    def CurveValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the MultiCurve approximating the set after
        computing the value F or Grad(F).
        """

    def Error(self, IPoint: int, CurveIndex: int) -> float:
        """
        returns the distance between the MultiPoint of range
        IPoint and the curve CurveIndex.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

class AppDef_ParLeastSquareOfTheGradient:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        NbPol is the number of control points wanted
        for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the Bernstein matrix computed with the
        parameters, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        Deg is the degree wanted for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the BSpline functions matrix computed with
        <parameters>, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, theOther: AppDef_ParLeastSquareOfTheGradient) -> None: ...

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector) -> None:
        """
        Is used after having initialized the fields.
        The case "CurvaturePoint" is not treated in this method.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """Is used after having initialized the fields."""

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, V1c: nanoocp.math.math_Vector, V2c: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        <V1c> is the tangent vector at the first point.
        <V2c> is the tangent vector at the last point.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def BezierValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def BSplineValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def FunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the function matrix used to approximate the
        set.
        """

    def DerivativeFunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the derivative function matrix used
        to approximate the set.
        """

    def ErrorGradient(self, Grad: nanoocp.math.math_Vector) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances. Grad is the derivative vector of the
        function F.
        """

    def Distance(self) -> nanoocp.math.math_Matrix:
        """
        returns the distances between the points of the
        multiline and the approximation curves.
        """

    def Error(self) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances.
        """

    def FirstLambda(self) -> float:
        """
        returns the value (P2 - P1)/ V1 if the first point
        was a tangency point.
        """

    def LastLambda(self) -> float:
        """
        returns the value (PN - PN-1)/ VN if the last point
        was a tangency point.
        """

    def Points(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of points value."""

    def Poles(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of resulting control points value."""

    def KIndex(self) -> nanoocp.math.math_IntegerVector:
        """
        Returns the indexes of the first non null values of
        A and DA.
        The values are non null from Index(ieme point) +1
        to Index(ieme point) + degree +1.
        """

class AppDef_ParFunctionOfTheGradient(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has the desired degree Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_ParFunctionOfTheGradient) -> None: ...

    def NbVariables(self) -> int:
        """
        returns the number of variables of the function. It
        corresponds to the number of MultiPoints.
        """

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        this method computes the new approximation of the
        MultiLine
        SSP and calculates F = sum (||Pui - Bi*Pi||2) for each
        point of the MultiLine.
        """

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """
        returns the gradient G of the sum above for the
        parameters Xi.
        """

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        returns the value F=sum(||Pui - Bi*Pi||)2.
        returns the value G = grad(F) for the parameters Xi.
        """

    def NewParameters(self) -> nanoocp.math.math_Vector:
        """returns the new parameters of the MultiLine."""

    def CurveValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the MultiCurve approximating the set after
        computing the value F or Grad(F).
        """

    def Error(self, IPoint: int, CurveIndex: int) -> float:
        """
        returns the distance between the MultiPoint of range
        IPoint and the curve CurveIndex.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

class AppDef_ResConstraintOfMyGradientbisOfBSplineCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, SCurv: nanoocp.AppParCurves.AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Bern: nanoocp.math.math_Matrix, DerivativeBern: nanoocp.math.math_Matrix, Tolerance: float = 1e-10) -> None:
        """
        Given a MultiLine SSP with constraints points, this
        algorithm finds the best curve solution to approximate it.
        The poles from SCurv issued for example from the least
        squares are used as a guess solution for the uzawa
        algorithm. The tolerance used in the Uzawa algorithms
        is Tolerance.
        A is the Bernstein matrix associated to the MultiLine
        and DA is the derivative bernstein matrix.(They can come
        from an approximation with ParLeastSquare.)
        The MultiCurve is modified. New MultiPoles are given.
        """

    @overload
    def __init__(self, theOther: AppDef_ResConstraintOfMyGradientbisOfBSplineCompute) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def ConstraintMatrix(self) -> nanoocp.math.math_Matrix: ...

    def Duale(self) -> nanoocp.math.math_Vector:
        """returns the duale variables of the system."""

    def ConstraintDerivative(self, SSP: AppDef_MultiLine, Parameters: nanoocp.math.math_Vector, Deg: int, DA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix:
        """Returns the derivative of the constraint matrix."""

    def InverseMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the Inverse of Cont*Transposed(Cont), where
        Cont is the constraint matrix for the algorithm.
        """

class AppDef_ResConstraintOfMyGradientOfCompute:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, SCurv: nanoocp.AppParCurves.AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Bern: nanoocp.math.math_Matrix, DerivativeBern: nanoocp.math.math_Matrix, Tolerance: float = 1e-10) -> None:
        """
        Given a MultiLine SSP with constraints points, this
        algorithm finds the best curve solution to approximate it.
        The poles from SCurv issued for example from the least
        squares are used as a guess solution for the uzawa
        algorithm. The tolerance used in the Uzawa algorithms
        is Tolerance.
        A is the Bernstein matrix associated to the MultiLine
        and DA is the derivative bernstein matrix.(They can come
        from an approximation with ParLeastSquare.)
        The MultiCurve is modified. New MultiPoles are given.
        """

    @overload
    def __init__(self, theOther: AppDef_ResConstraintOfMyGradientOfCompute) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def ConstraintMatrix(self) -> nanoocp.math.math_Matrix: ...

    def Duale(self) -> nanoocp.math.math_Vector:
        """returns the duale variables of the system."""

    def ConstraintDerivative(self, SSP: AppDef_MultiLine, Parameters: nanoocp.math.math_Vector, Deg: int, DA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix:
        """Returns the derivative of the constraint matrix."""

    def InverseMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the Inverse of Cont*Transposed(Cont), where
        Cont is the constraint matrix for the algorithm.
        """

class AppDef_ResConstraintOfTheGradient:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, SCurv: nanoocp.AppParCurves.AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Bern: nanoocp.math.math_Matrix, DerivativeBern: nanoocp.math.math_Matrix, Tolerance: float = 1e-10) -> None:
        """
        Given a MultiLine SSP with constraints points, this
        algorithm finds the best curve solution to approximate it.
        The poles from SCurv issued for example from the least
        squares are used as a guess solution for the uzawa
        algorithm. The tolerance used in the Uzawa algorithms
        is Tolerance.
        A is the Bernstein matrix associated to the MultiLine
        and DA is the derivative bernstein matrix.(They can come
        from an approximation with ParLeastSquare.)
        The MultiCurve is modified. New MultiPoles are given.
        """

    @overload
    def __init__(self, theOther: AppDef_ResConstraintOfTheGradient) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def ConstraintMatrix(self) -> nanoocp.math.math_Matrix: ...

    def Duale(self) -> nanoocp.math.math_Vector:
        """returns the duale variables of the system."""

    def ConstraintDerivative(self, SSP: AppDef_MultiLine, Parameters: nanoocp.math.math_Vector, Deg: int, DA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix:
        """Returns the derivative of the constraint matrix."""

    def InverseMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the Inverse of Cont*Transposed(Cont), where
        Cont is the constraint matrix for the algorithm.
        """

class AppDef_TheLeastSquares:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        NbPol is the number of control points wanted
        for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the Bernstein matrix computed with the
        parameters, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: AppDef_MultiLine, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
        """
        given a MultiLine, this algorithm computes the least
        square resolution using the Householder-QR method.
        If the first and/or the last point is a constraint
        point, the value of the tangency or curvature is
        computed in the resolution.
        Deg is the degree wanted for the approximating curves.
        The system to solve is the following:
        A X = B.
        Where A is the BSpline functions matrix computed with
        <parameters>, B the points coordinates and X the poles
        solutions.
        The matrix A is the same for each coordinate x, y and z
        and is also the same for each MultiLine point because
        they are approximated in parallel(so with the same
        parameter, only the vector B changes).
        """

    @overload
    def __init__(self, theOther: AppDef_TheLeastSquares) -> None: ...

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector) -> None:
        """
        Is used after having initialized the fields.
        The case "CurvaturePoint" is not treated in this method.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """Is used after having initialized the fields."""

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        """

    @overload
    def Perform(self, Parameters: nanoocp.math.math_Vector, V1t: nanoocp.math.math_Vector, V2t: nanoocp.math.math_Vector, V1c: nanoocp.math.math_Vector, V2c: nanoocp.math.math_Vector, l1: float, l2: float) -> None:
        """
        Is used after having initialized the fields.
        <V1t> is the tangent vector at the first point.
        <V2t> is the tangent vector at the last point.
        <V1c> is the tangent vector at the first point.
        <V2c> is the tangent vector at the last point.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def BezierValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def BSplineValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns the result of the approximation, i.e. all the
        Curves.
        An exception is raised if NotDone.
        """

    def FunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the function matrix used to approximate the
        set.
        """

    def DerivativeFunctionMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the derivative function matrix used
        to approximate the set.
        """

    def ErrorGradient(self, Grad: nanoocp.math.math_Vector) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances. Grad is the derivative vector of the
        function F.
        """

    def Distance(self) -> nanoocp.math.math_Matrix:
        """
        returns the distances between the points of the
        multiline and the approximation curves.
        """

    def Error(self) -> tuple[float, float, float]:
        """
        returns the maximum errors between the MultiLine
        and the approximation curves. F is the sum of the square
        distances.
        """

    def FirstLambda(self) -> float:
        """
        returns the value (P2 - P1)/ V1 if the first point
        was a tangency point.
        """

    def LastLambda(self) -> float:
        """
        returns the value (PN - PN-1)/ VN if the last point
        was a tangency point.
        """

    def Points(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of points value."""

    def Poles(self) -> nanoocp.math.math_Matrix:
        """returns the matrix of resulting control points value."""

    def KIndex(self) -> nanoocp.math.math_IntegerVector:
        """
        Returns the indexes of the first non null values of
        A and DA.
        The values are non null from Index(ieme point) +1
        to Index(ieme point) + degree +1.
        """

class AppDef_TheFunction(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has the desired degree Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_TheFunction) -> None: ...

    def NbVariables(self) -> int:
        """
        returns the number of variables of the function. It
        corresponds to the number of MultiPoints.
        """

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        this method computes the new approximation of the
        MultiLine
        SSP and calculates F = sum (||Pui - Bi*Pi||2) for each
        point of the MultiLine.
        """

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """
        returns the gradient G of the sum above for the
        parameters Xi.
        """

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        returns the value F=sum(||Pui - Bi*Pi||)2.
        returns the value G = grad(F) for the parameters Xi.
        """

    def NewParameters(self) -> nanoocp.math.math_Vector:
        """returns the new parameters of the MultiLine."""

    def CurveValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns the MultiCurve approximating the set after
        computing the value F or Grad(F).
        """

    def Error(self, IPoint: int, CurveIndex: int) -> float:
        """
        returns the distance between the MultiPoint of range
        IPoint and the curve CurveIndex.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum distance between the points
        and the MultiCurve.
        """

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

class AppDef_TheGradient:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Parameters: nanoocp.math.math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 200) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating Bezier curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: AppDef_TheGradient) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """
        returns all the Bezier curves approximating the
        MultiLine SSP after minimization of the parameter.
        """

    def Error(self, Index: int) -> float:
        """
        returns the difference between the old and the new
        approximation.
        An exception is raised if NotDone.
        An exception is raised if Index<1 or Index>NbParameters.
        """

    def MaxError3d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def MaxError2d(self) -> float:
        """
        returns the maximum difference between the old and the
        new approximation.
        """

    def AverageError(self) -> float:
        """
        returns the average error between the old and the
        new approximation.
        """

class AppDef_TheResol:
    @overload
    def __init__(self, SSP: AppDef_MultiLine, SCurv: nanoocp.AppParCurves.AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], Bern: nanoocp.math.math_Matrix, DerivativeBern: nanoocp.math.math_Matrix, Tolerance: float = 1e-10) -> None:
        """
        Given a MultiLine SSP with constraints points, this
        algorithm finds the best curve solution to approximate it.
        The poles from SCurv issued for example from the least
        squares are used as a guess solution for the uzawa
        algorithm. The tolerance used in the Uzawa algorithms
        is Tolerance.
        A is the Bernstein matrix associated to the MultiLine
        and DA is the derivative bernstein matrix.(They can come
        from an approximation with ParLeastSquare.)
        The MultiCurve is modified. New MultiPoles are given.
        """

    @overload
    def __init__(self, theOther: AppDef_TheResol) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def ConstraintMatrix(self) -> nanoocp.math.math_Matrix: ...

    def Duale(self) -> nanoocp.math.math_Vector:
        """returns the duale variables of the system."""

    def ConstraintDerivative(self, SSP: AppDef_MultiLine, Parameters: nanoocp.math.math_Vector, Deg: int, DA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix:
        """Returns the derivative of the constraint matrix."""

    def InverseMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the Inverse of Cont*Transposed(Cont), where
        Cont is the constraint matrix for the algorithm.
        """

class AppDef_Variational:
    """
    This class is used to smooth N points with constraints
    by minimization of quadratic criterium but also
    variational criterium in order to obtain " fair Curve "
    Computes the approximation of a Multiline by
    Variational optimization.
    """

    @overload
    def __init__(self, SSP: AppDef_MultiLine, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple], MaxDegree: int = 14, MaxSegment: int = 100, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, WithMinMax: bool = False, WithCutting: bool = True, Tolerance: float = 1.0, NbIterations: int = 2) -> None:
        """
        Constructor.
        Initialization of the fields.
        Warning:
        Nc0 : number of PassagePoint consraints
        Nc2 : number of TangencyPoint constraints
        Nc3 : number of CurvaturePoint constraints
        if ((MaxDegree-Continuity)*MaxSegment -Nc0 - 2*Nc1 -3*Nc2)
        is negative
        The problem is over-constrained.

        Limitation : The MultiLine from AppDef has to be composed by
        only one Line ( Dimension 2 or 3).
        """

    @overload
    def __init__(self, theOther: AppDef_Variational) -> None: ...

    def Approximate(self) -> None:
        """Makes the approximation with the current fields."""

    def IsCreated(self) -> bool:
        """
        returns True if the creation is done
        and correspond to the current fields.
        """

    def IsDone(self) -> bool:
        """
        returns True if the approximation is ok
        and correspond to the current fields.
        """

    def IsOverConstrained(self) -> bool:
        """
        returns True if the problem is overconstrained
        in this case, approximation cannot be done.
        """

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """
        returns all the BSpline curves approximating the
        MultiLine from AppDef SSP after minimization of the parameter.
        """

    def MaxError(self) -> float:
        """
        returns the maximum of the distances between
        the points of the multiline and the approximation
        curves.
        """

    def MaxErrorIndex(self) -> int:
        """returns the index of the MultiPoint of ErrorMax"""

    def QuadraticError(self) -> float:
        """
        returns the quadratic average of the distances between
        the points of the multiline and the approximation
        curves.
        """

    def Distance(self, mat: nanoocp.math.math_Matrix) -> None:
        """
        returns the distances between the points of the
        multiline and the approximation curves.
        """

    def AverageError(self) -> float:
        """
        returns the average error between
        the MultiLine from AppDef and the approximation.
        """

    def Parameters(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the parameters uses to the approximations"""

    def Knots(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the knots uses to the approximations"""

    def Criterium(self) -> tuple[float, float, float]:
        """returns the values of the quality criterium."""

    def CriteriumWeight(self) -> tuple[float, float, float]:
        """
        returns the Weights (as percent) associed to the criterium used in
        the optimization.
        """

    def MaxDegree(self) -> int:
        """returns the Maximum Degree used in the approximation"""

    def MaxSegment(self) -> int:
        """returns the Maximum of segment used in the approximation"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """returns the Continuity used in the approximation"""

    def WithMinMax(self) -> bool:
        """
        returns if the approximation search to minimize the
        maximum Error or not.
        """

    def WithCutting(self) -> bool:
        """returns if the approximation can insert new Knots or not."""

    def Tolerance(self) -> float:
        """returns the tolerance used in the approximation."""

    def NbIterations(self) -> int:
        """returns the number of iterations used in the approximation."""

    def SetConstraints(self, aConstrainst: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple]) -> bool:
        """
        Define the constraints to approximate
        If this value is incompatible with the others fields
        this method modify nothing and returns false
        """

    def SetParameters(self, param: nanoocp.NCollection.NCollection_HArray1[float]) -> None:
        """Defines the parameters used by the approximations."""

    def SetKnots(self, knots: nanoocp.NCollection.NCollection_HArray1[float]) -> bool:
        """
        Defines the knots used by the approximations
        If this value is incompatible with the others fields
        this method modify nothing and returns false
        """

    def SetMaxDegree(self, Degree: int) -> bool:
        """
        Define the Maximum Degree used in the approximation
        If this value is incompatible with the others fields
        this method modify nothing and returns false
        """

    def SetMaxSegment(self, NbSegment: int) -> bool:
        """
        Define the maximum number of segments used in the approximation
        If this value is incompatible with the others fields
        this method modify nothing and returns false
        """

    def SetContinuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> bool:
        """
        Define the Continuity used in the approximation
        If this value is incompatible with the others fields
        this method modify nothing and returns false
        """

    def SetWithMinMax(self, MinMax: bool) -> None:
        """
        Define if the approximation search to minimize the
        maximum Error or not.
        """

    def SetWithCutting(self, Cutting: bool) -> bool:
        """
        Define if the approximation can insert new Knots or not.
        If this value is incompatible with the others fields
        this method modify nothing and returns false
        """

    @overload
    def SetCriteriumWeight(self, Percent1: float, Percent2: float, Percent3: float) -> None:
        """
        define the Weights (as percent) associed to the criterium used in
        the optimization.

        if Percent <= 0
        """

    @overload
    def SetCriteriumWeight(self, Order: int, Percent: float) -> None:
        """
        define the Weight (as percent) associed to the
        criterium Order used in the optimization : Others
        weights are updated.
        if Percent < 0
        if Order < 1 or Order > 3
        """

    def SetTolerance(self, Tol: float) -> None:
        """define the tolerance used in the approximation."""

    def SetNbIterations(self, Iter: int) -> None:
        """
        define the number of iterations used in the approximation.
        if Iter < 1
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.AppDef
AppDef_Array1OfMultiPointConstraint = nanoocp.NCollection.NCollection_Array1[nanoocp.AppDef.AppDef_MultiPointConstraint]
