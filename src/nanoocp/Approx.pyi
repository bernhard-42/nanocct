"""OCCT package Approx (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.AppCont
import nanoocp.AppParCurves
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class Approx_ParametrizationType(enum.IntEnum):
    Approx_ChordLength = 0

    Approx_Centripetal = 1

    Approx_IsoParametric = 2

Approx_ChordLength: Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength

Approx_Centripetal: Approx_ParametrizationType = Approx_ParametrizationType.Approx_Centripetal

Approx_IsoParametric: Approx_ParametrizationType = Approx_ParametrizationType.Approx_IsoParametric

class Approx_Status(enum.IntEnum):
    """It is an auxiliary flag being used in inner computations"""

    Approx_PointsAdded = 0

    Approx_NoPointsAdded = 1

    Approx_NoApproximation = 2

Approx_PointsAdded: Approx_Status = Approx_Status.Approx_PointsAdded

Approx_NoPointsAdded: Approx_Status = Approx_Status.Approx_NoPointsAdded

Approx_NoApproximation: Approx_Status = Approx_Status.Approx_NoApproximation

class Approx_Curve2d:
    """Makes an approximation for HCurve2d from Adaptor3d"""

    @overload
    def __init__(self, C2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, First: float, Last: float, TolU: float, TolV: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None: ...

    @overload
    def __init__(self, theOther: Approx_Curve2d) -> None: ...

    def IsDone(self) -> bool: ...

    def HasResult(self) -> bool: ...

    def Curve(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def MaxError2dU(self) -> float: ...

    def MaxError2dV(self) -> float: ...

class Approx_Curve3d:
    @overload
    def __init__(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tol3d: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> None:
        """
        Approximation of a curve with respect of the
        required tolerance Tol3D.
        """

    @overload
    def __init__(self, theOther: Approx_Curve3d) -> None: ...

    def Curve(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def IsDone(self) -> bool:
        """
        returns true if the approximation has
        been done within required tolerance
        """

    def HasResult(self) -> bool:
        """
        returns true if the approximation did come out
        with a result that is not NECESSARILY within the required
        tolerance
        """

    def MaxError(self) -> float:
        """
        returns the Maximum Error (>0 when an approximation
        has been done, 0 if no approximation)
        """

    def Dump(self) -> object:
        """Print on the stream 'o' information about the object"""

class Approx_CurveOnSurface:
    """Approximation of curve on surface"""

    @overload
    def __init__(self, theC2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theFirst: float, theLast: float, theTol: float) -> None:
        """
        This constructor does not call perform method.
        @param theC2D   2D Curve to be approximated in 3D.
        @param theSurf  Surface where 2D curve is located.
        @param theFirst First parameter of resulting curve.
        @param theFirst Last parameter of resulting curve.
        @param theTol   Computation tolerance.
        """

    @overload
    def __init__(self, theOther: Approx_CurveOnSurface) -> None: ...

    def IsDone(self) -> bool: ...

    def HasResult(self) -> bool: ...

    def Curve3d(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def MaxError3d(self) -> float: ...

    def Curve2d(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def MaxError2dU(self) -> float: ...

    def MaxError2dV(self) -> float:
        """
        returns the maximum errors relatively to the U component or the V component of the
        2d Curve
        """

    def Perform(self, theMaxSegments: int, theMaxDegree: int, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape, theOnly3d: bool = False, theOnly2d: bool = False) -> None:
        """
        Constructs the 3d curve. Input parameters are ignored when the input curve is
        U-isoline or V-isoline.
        @param theMaxSegments Maximal number of segments in the resulting spline.
        @param theMaxDegree   Maximal degree of the result.
        @param theContinuity  Resulting continuity.
        @param theOnly3d      Determines building only 3D curve.
        @param theOnly2d      Determines building only 2D curve.
        """

class Approx_CurvilinearParameter:
    """
    Approximation of a Curve to make its parameter be its curvilinear abscissa.
    If the curve is a curve on a surface S, C2D is the corresponding Pcurve,
    we consider the curve is given by its representation
    @code
    S(C2D(u))
    @endcode
    If the curve is a curve on 2 surfaces S1 and S2 and C2D1 C2D2 are the two corresponding Pcurve,
    we consider the curve is given by its representation
    @code
    1/2(S1(C2D1(u) + S2(C2D2(u)))
    @endcode
    """

    @overload
    def __init__(self, C3D: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tol: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None:
        """case of a free 3D curve"""

    @overload
    def __init__(self, C2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None:
        """case of a curve on one surface"""

    @overload
    def __init__(self, C2D1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C2D2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None:
        """case of a curve on two surfaces"""

    @overload
    def __init__(self, theOther: Approx_CurvilinearParameter) -> None: ...

    def IsDone(self) -> bool: ...

    def HasResult(self) -> bool: ...

    def Curve3d(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """returns the Bspline curve corresponding to the reparametrized 3D curve"""

    def MaxError3d(self) -> float:
        """returns the maximum error on the reparametrized 3D curve"""

    def Curve2d1(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        returns the BsplineCurve representing the reparametrized 2D curve on the
        first surface (case of a curve on one or two surfaces)
        """

    def MaxError2d1(self) -> float:
        """returns the maximum error on the first reparametrized 2D curve"""

    def Curve2d2(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        returns the BsplineCurve representing the reparametrized 2D curve on the
        second surface (case of a curve on two surfaces)
        """

    def MaxError2d2(self) -> float:
        """returns the maximum error on the second reparametrized 2D curve"""

    def Dump(self) -> object:
        """print the maximum errors(s)"""

class Approx_CurvlinFunc(nanoocp.Standard.Standard_Transient):
    """
    defines an abstract curve with
    curvilinear parametrization
    """

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tol: float) -> None: ...

    @overload
    def __init__(self, C2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol: float) -> None: ...

    @overload
    def __init__(self, C2D1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, C2D2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol: float) -> None: ...

    @overload
    def __init__(self, theOther: Approx_CurvlinFunc) -> None: ...

    def SetTol(self, Tol: float) -> None:
        """---Purpose Update the tolerance to used"""

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> None:
        """if First < 0 or Last > 1"""

    @overload
    def Length(self) -> None:
        """Computes length of the curve."""

    @overload
    def Length(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, FirstU: float, LasrU: float) -> float:
        """Computes length of the curve segment."""

    def GetLength(self) -> float: ...

    def GetUParameter(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: float, NumberOfCurve: int) -> float:
        """
        returns original parameter corresponding S. if
        Case == 1 computation is performed on myC2D1 and mySurf1,
        otherwise it is done on myC2D2 and mySurf2.
        """

    def GetSParameter(self, U: float) -> float:
        """returns original parameter corresponding S."""

    def EvalCase1(self, S: float, Order: int, Result: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """if myCase != 1"""

    def EvalCase2(self, S: float, Order: int, Result: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """if myCase != 2"""

    def EvalCase3(self, S: float, Order: int, Result: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """if myCase != 3"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Approx_FitAndDivide:
    @overload
    def __init__(self, degreemin: int = 3, degreemax: int = 8, Tolerance3d: float = 1e-05, Tolerance2d: float = 1e-05, cutting: bool = False, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint = ..., LastC: nanoocp.AppParCurves.AppParCurves_Constraint = ...) -> None:
        """Initializes the fields of the algorithm."""

    @overload
    def __init__(self, Line: nanoocp.AppCont.AppCont_Function, degreemin: int = 3, degreemax: int = 8, Tolerance3d: float = 1e-05, Tolerance2d: float = 1e-05, cutting: bool = False, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint = ..., LastC: nanoocp.AppParCurves.AppParCurves_Constraint = ...) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        """

    @overload
    def __init__(self, theOther: Approx_FitAndDivide) -> None: ...

    def Perform(self, Line: nanoocp.AppCont.AppCont_Function) -> None:
        """runs the algorithm after having initialized the fields."""

    def SetDegrees(self, degreemin: int, degreemax: int) -> None:
        """changes the degrees of the approximation."""

    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None:
        """Changes the tolerances of the approximation."""

    def SetConstraints(self, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint, LastC: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """Changes the constraints of the approximation."""

    def SetMaxSegments(self, theMaxSegments: int) -> None:
        """Changes the max number of segments, which is allowed for cutting."""

    def SetInvOrder(self, theInvOrder: bool) -> None:
        """
        Set inverse order of degree selection:
        if theInvOrdr = true, current degree is chosen by inverse order -
        from maxdegree to mindegree.
        By default inverse order is used.
        """

    def SetHangChecking(self, theHangChecking: bool) -> None:
        """
        Set value of hang checking flag
        if this flag = true, possible hang of algorithm is checked
        and algorithm is forced to stop.
        By default hang checking is used.
        """

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
        """returns the approximation MultiCurve of range <Index>."""

    def Parameters(self, Index: int) -> tuple[float, float]: ...

class Approx_FitAndDivide2d:
    @overload
    def __init__(self, degreemin: int = 3, degreemax: int = 8, Tolerance3d: float = 1e-05, Tolerance2d: float = 1e-05, cutting: bool = False, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint = ..., LastC: nanoocp.AppParCurves.AppParCurves_Constraint = ...) -> None:
        """Initializes the fields of the algorithm."""

    @overload
    def __init__(self, Line: nanoocp.AppCont.AppCont_Function, degreemin: int = 3, degreemax: int = 8, Tolerance3d: float = 1e-05, Tolerance2d: float = 1e-05, cutting: bool = False, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint = ..., LastC: nanoocp.AppParCurves.AppParCurves_Constraint = ...) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        """

    @overload
    def __init__(self, theOther: Approx_FitAndDivide2d) -> None: ...

    def Perform(self, Line: nanoocp.AppCont.AppCont_Function) -> None:
        """runs the algorithm after having initialized the fields."""

    def SetDegrees(self, degreemin: int, degreemax: int) -> None:
        """changes the degrees of the approximation."""

    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None:
        """Changes the tolerances of the approximation."""

    def SetConstraints(self, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint, LastC: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """Changes the constraints of the approximation."""

    def SetMaxSegments(self, theMaxSegments: int) -> None:
        """Changes the max number of segments, which is allowed for cutting."""

    def SetInvOrder(self, theInvOrder: bool) -> None:
        """
        Set inverse order of degree selection:
        if theInvOrdr = true, current degree is chosen by inverse order -
        from maxdegree to mindegree.
        By default inverse order is used.
        """

    def SetHangChecking(self, theHangChecking: bool) -> None:
        """
        Set value of hang checking flag
        if this flag = true, possible hang of algorithm is checked
        and algorithm is forced to stop.
        By default hang checking is used.
        """

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
        """returns the approximation MultiCurve of range <Index>."""

    def Parameters(self, Index: int) -> tuple[float, float]: ...

class Approx_MCurvesToBSpCurve:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Approx_MCurvesToBSpCurve) -> None: ...

    def Reset(self) -> None: ...

    def Append(self, MC: nanoocp.AppParCurves.AppParCurves_MultiCurve) -> None: ...

    @overload
    def Perform(self) -> None: ...

    @overload
    def Perform(self, TheSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.AppParCurves.AppParCurves_MultiCurve]) -> None: ...

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """return the composite MultiCurves as a MultiBSpCurve."""

    def ChangeValue(self) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve:
        """return the composite MultiCurves as a MultiBSpCurve."""

class Approx_SameParameter:
    """
    Approximation of a PCurve on a surface to make its
    parameter be the same that the parameter of a given 3d
    reference curve.
    """

    @overload
    def __init__(self, C3D: nanoocp.Geom.Geom_Curve | None, C2D: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, Tol: float) -> None: ...

    @overload
    def __init__(self, C3D: nanoocp.Adaptor3d.Adaptor3d_Curve | None, C2D: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol: float) -> None: ...

    @overload
    def __init__(self, C3D: nanoocp.Adaptor3d.Adaptor3d_Curve | None, C2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol: float) -> None:
        """Warning: the C3D and C2D must have the same parametric domain."""

    def IsDone(self) -> bool:
        """
        @Returns .false. if calculations failed,
        .true. if calculations succeed
        """

    def TolReached(self) -> float:
        """
        @Returns tolerance (maximal distance) between 3d curve
        and curve on surface, generated by 2d curve and surface.
        """

    def IsSameParameter(self) -> bool:
        """
        Tells whether the original data had already the same
        parameter up to the tolerance : in that case nothing
        is done.
        """

    def Curve2d(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Returns the 2D curve that has the same parameter as
        the 3D curve once evaluated on the surface up to the
        specified tolerance.
        """

    def Curve3d(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """
        Returns the 3D curve that has the same parameter as
        the 3D curve once evaluated on the surface up to the
        specified tolerance.
        """

    def CurveOnSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface:
        """
        Returns the 3D curve on surface that has the same parameter as
        the 3D curve up to the specified tolerance.
        """

class Approx_SweepApproximation:
    """
    Approximation of an Surface S(u,v)
    (and eventually associate 2d Curves) defined
    by section's law.

    This surface is defined by a function F(u, v)
    where Ft(u) = F(u, t) is a bspline curve.
    To use this algorithm, you have to implement Ft(u)
    as a derivative class of Approx_SweepFunction.
    This algorithm can be used by blending, sweeping...
    """

    @overload
    def __init__(self, Func: Approx_SweepFunction | None) -> None: ...

    @overload
    def __init__(self, theOther: Approx_SweepApproximation) -> None: ...

    def Perform(self, First: float, Last: float, Tol3d: float, BoundTol: float, Tol2d: float, TolAngular: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C0, Degmax: int = 11, Segmax: int = 50) -> None:
        """
        Perform the Approximation
        [First, Last] : Approx_SweepApproximation.cdl
        Tol3d : Tolerance to surface approximation
        Tol2d : Tolerance used to perform curve approximation
        Normally the 2d curve are approximated with a
        tolerance given by the resolution on support surfaces,
        but if this tolerance is too large Tol2d is used.
        TolAngular : Tolerance (in radian) to control the angle
        between tangents on the section law and
        tangent of iso-v on approximated surface
        Continuity : The continuity in v waiting on the surface
        Degmax     : The maximum degree in v required on the surface
        Segmax     : The maximum number of span in v required on
        the surface
        Warning : The continuity ci can be obtained only if Ft is Ci
        """

    def Eval(self, Parameter: float, DerivativeRequest: int, First: float, Last: float) -> tuple[int, float]:
        """The EvaluatorFunction from AdvApprox;"""

    def IsDone(self) -> bool:
        """returns if we have an result"""

    def SurfShape(self) -> tuple[int, int, int, int, int, int]: ...

    def Surface(self, TPoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], TWeights: nanoocp.NCollection.NCollection_Array2[float], TUKnots: nanoocp.NCollection.NCollection_Array1[float], TVKnots: nanoocp.NCollection.NCollection_Array1[float], TUMults: nanoocp.NCollection.NCollection_Array1[int], TVMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def UDegree(self) -> int: ...

    def VDegree(self) -> int: ...

    def SurfPoles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]: ...

    def SurfWeights(self) -> nanoocp.NCollection.NCollection_Array2[float]: ...

    def SurfUKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfVKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfUMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def SurfVMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def MaxErrorOnSurf(self) -> float:
        """returns the maximum error in the surface approximation."""

    def AverageErrorOnSurf(self) -> float:
        """returns the average error in the surface approximation."""

    def NbCurves2d(self) -> int: ...

    def Curves2dShape(self) -> tuple[int, int, int]: ...

    def Curve2d(self, Index: int, TPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TKnots: nanoocp.NCollection.NCollection_Array1[float], TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Curves2dDegree(self) -> int: ...

    def Curve2dPoles(self, Index: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]: ...

    def Curves2dKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def Curves2dMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def Max2dError(self, Index: int) -> float:
        """
        returns the maximum error of the <Index>
        2d curve approximation.
        """

    def Average2dError(self, Index: int) -> float:
        """
        returns the average error of the <Index>
        2d curve approximation.
        """

    def TolCurveOnSurf(self, Index: int) -> float:
        """
        returns the maximum 3d error of the <Index>
        2d curve approximation on the Surface.
        """

    def Dump(self) -> object:
        """display information on approximation."""

class Approx_SweepFunction(nanoocp.Standard.Standard_Transient):
    """
    defined the function used by SweepApproximation to
    perform sweeping application.
    """

    def D0(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        Warning : It used only for C1 or C2 approximation
        """

    def D2(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        Warning : It used only for C2 approximation
        """

    def Nb2dCurves(self) -> int:
        """get the number of 2d curves to approximate."""

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the sections are rational or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>.
        May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the function
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def Resolution(self, Index: int, Tol: float) -> tuple[float, float]:
        """
        Returns the resolutions in the sub-space 2d <Index>
        This information is useful to find a good tolerance in
        2d approximation.
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerance to reach in approximation
        to satisfy.
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary (in radian)
        SurfTol error inside the surface.
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if (me) have to run numerical algorithm to perform D0, D1 or D2
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface.
        An very poor estimation is sufficient.
        This information is useful to perform well conditioned rational approximation.
        Warning: Used only if <me> IsRational
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the greater section.
        This information is useful to G1's control.
        Warning: With an little value, approximation can be slower.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles in all sections.
        This information is useful to control error in rational approximation.
        Warning: Used only if <me> IsRational
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
