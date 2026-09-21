"""OCCT package GeomInt (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.AppParCurves
import nanoocp.Approx
import nanoocp.ApproxInt
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAdaptor
import nanoocp.IntImp
import nanoocp.IntPatch
import nanoocp.IntSurf
import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.gp
import nanoocp.math


class GeomInt:
    """
    Provides intersections on between two surfaces of Geom.
    The result are curves from Geom.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt) -> None: ...

    @staticmethod
    def AdjustPeriodic(thePar: float, theParMin: float, theParMax: float, thePeriod: float, theEps: float = 0.0) -> tuple[bool, float, float]:
        """Adjusts the parameter <thePar> to the range [theParMin, theParMax]"""

class GeomInt_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfWLApprox(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfWLApprox) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class GeomInt_TheMultiLineOfWLApprox:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, line: nanoocp.IntPatch.IntPatch_WLine | None, NbP3d: int, NbP2d: int, ApproxU1V1: bool, ApproxU2V2: bool, xo: float, yo: float, zo: float, u1o: float, v1o: float, u2o: float, v2o: float, P2DOnFirst: bool, IndMin: int = 0, IndMax: int = 0) -> None:
        """No Extra points will be added on the current line"""

    @overload
    def __init__(self, theOther: GeomInt_TheMultiLineOfWLApprox) -> None: ...

    def FirstPoint(self) -> int: ...

    def LastPoint(self) -> int: ...

    def NbP2d(self) -> int:
        """Returns the number of 2d points of a TheLine."""

    def NbP3d(self) -> int:
        """Returns the number of 3d points of a TheLine."""

    def WhatStatus(self) -> nanoocp.Approx.Approx_Status: ...

    @overload
    def Value(self, MPointIndex: int, tabPt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        Returns the 3d points of the multipoint <MPointIndex> when only 3d points exist.
        """

    @overload
    def Value(self, MPointIndex: int, tabPt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        Returns the 2d points of the multipoint <MPointIndex> when only 2d points exist.
        """

    @overload
    def Value(self, MPointIndex: int, tabPt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabPt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """returns the 3d and 2d points of the multipoint <MPointIndex>."""

    @overload
    def Tangency(self, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """
        Returns the 3d tangency points of the multipoint <MPointIndex> only
        when 3d points exist.
        """

    @overload
    def Tangency(self, MPointIndex: int, tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        Returns the 2d tangency points of the multipoint <MPointIndex> only
        when 2d points exist.
        """

    @overload
    def Tangency(self, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """Returns the 3d and 2d points of the multipoint <MPointIndex>."""

    def MakeMLBetween(self, Low: int, High: int, NbPointsToInsert: int) -> GeomInt_TheMultiLineOfWLApprox:
        """
        Tries to make a sub-line between <Low> and <High> points of this line
        by adding <NbPointsToInsert> new points
        """

    def MakeMLOneMorePoint(self, Low: int, High: int, indbad: int, OtherLine: GeomInt_TheMultiLineOfWLApprox) -> bool:
        """
        Tries to make a sub-line between <Low> and <High> points of this line
        by adding one more point between (indbad-1)-th and indbad-th points
        """

    def Dump(self) -> None:
        """Dump of the current multi-line."""

class GeomInt_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
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
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
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
    def __init__(self, theOther: GeomInt_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfWLApprox) -> None: ...

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

class GeomInt_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfWLApprox(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], NbPol: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has <NbPol> control points.
        """

    @overload
    def __init__(self, theOther: GeomInt_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfWLApprox) -> None: ...

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

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def SetFirstLambda(self, l1: float) -> None: ...

    def SetLastLambda(self, l2: float) -> None: ...

class GeomInt_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfWLApprox(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfWLApprox) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class GeomInt_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfWLApprox(nanoocp.math.math_BFGS):
    @overload
    def __init__(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient, StartingPoint: nanoocp.math.math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: int = 200) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfWLApprox) -> None: ...

    def IsSolutionReached(self, F: nanoocp.math.math_MultipleVarFunctionWithGradient) -> bool: ...

class GeomInt_LineConstructor:
    """Splits given Line."""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: GeomInt_LineConstructor) -> None: ...

    def Load(self, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, S2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None) -> None:
        """
        Initializes me by two surfaces and corresponding
        tools which represent boundaries of surfaces
        """

    def Perform(self, L: nanoocp.IntPatch.IntPatch_Line | None) -> None:
        """Splits line"""

    def IsDone(self) -> bool:
        """Returns True if splitting was successful"""

    def NbParts(self) -> int:
        """Returns number of splits"""

    def Part(self, I: int) -> tuple[float, float]:
        """
        Return first and last parameters
        for given index of split
        """

class GeomInt_IntSS:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, Tol: float, Approx: bool = True, ApproxS1: bool = False, ApproxS2: bool = False) -> None:
        """performs general intersection of two surfaces just now"""

    @overload
    def __init__(self, theOther: GeomInt_IntSS) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, Tol: float, Approx: bool = True, ApproxS1: bool = False, ApproxS2: bool = False) -> None:
        """general intersection of two surfaces"""

    @overload
    def Perform(self, HS1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, HS2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, Tol: float, Approx: bool = True, ApproxS1: bool = False, ApproxS2: bool = False) -> None:
        """intersection of adapted surfaces"""

    @overload
    def Perform(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, Tol: float, U1: float, V1: float, U2: float, V2: float, Approx: bool = True, ApproxS1: bool = False, ApproxS2: bool = False) -> None:
        """general intersection using a starting point"""

    @overload
    def Perform(self, HS1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, HS2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, Tol: float, U1: float, V1: float, U2: float, V2: float, Approx: bool = True, ApproxS1: bool = False, ApproxS2: bool = False) -> None:
        """intersection of adapted surfaces using a starting point"""

    def IsDone(self) -> bool: ...

    def TolReached3d(self) -> float: ...

    def TolReached2d(self) -> float: ...

    def NbLines(self) -> int: ...

    def Line(self, Index: int) -> nanoocp.Geom.Geom_Curve: ...

    def HasLineOnS1(self, Index: int) -> bool: ...

    def LineOnS1(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def HasLineOnS2(self, Index: int) -> bool: ...

    def LineOnS2(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def NbBoundaries(self) -> int: ...

    def Boundary(self, Index: int) -> nanoocp.Geom.Geom_Curve: ...

    def NbPoints(self) -> int: ...

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2d(self, Index: int, OnFirst: bool) -> nanoocp.gp.gp_Pnt2d: ...

    @staticmethod
    def TreatRLine(theRL: nanoocp.IntPatch.IntPatch_RLine | None, theHS1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, theHS2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None) -> tuple[nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, float]:
        """converts RLine to Geom(2d)_Curve."""

    @overload
    @staticmethod
    def BuildPCurves(theFirst: float, theLast: float, theUmin: float, theUmax: float, theVmin: float, theVmax: float, theSurface: nanoocp.Geom.Geom_Surface | None, theCurve: nanoocp.Geom.Geom_Curve | None) -> tuple[float, nanoocp.Geom2d.Geom2d_Curve]: ...

    @overload
    @staticmethod
    def BuildPCurves(f: float, l: float, S: nanoocp.Geom.Geom_Surface | None, C: nanoocp.Geom.Geom_Curve | None) -> tuple[float, nanoocp.Geom2d.Geom2d_Curve]:
        """creates 2D-curve on given surface from given 3D-curve"""

    @staticmethod
    def TrimILineOnSurfBoundaries(theC2d1: nanoocp.Geom2d.Geom2d_Curve | None, theC2d2: nanoocp.Geom2d.Geom2d_Curve | None, theBound1: nanoocp.Bnd.Bnd_Box2d, theBound2: nanoocp.Bnd.Bnd_Box2d, theArrayOfParameters: nanoocp.NCollection.NCollection_DynamicArray[float]) -> None:
        """
        puts into theArrayOfParameters the parameters of intersection
        points of given theC2d1 and theC2d2 curves with the boundaries
        of the source surface.
        """

    @staticmethod
    def MakeBSpline(WL: nanoocp.IntPatch.IntPatch_WLine | None, ideb: int, ifin: int) -> nanoocp.Geom.Geom_Curve: ...

    @staticmethod
    def MakeBSpline2d(theWLine: nanoocp.IntPatch.IntPatch_WLine | None, ideb: int, ifin: int, onFirst: bool) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

class GeomInt_LineTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_LineTool) -> None: ...

    @staticmethod
    def NbVertex(L: nanoocp.IntPatch.IntPatch_Line | None) -> int: ...

    @staticmethod
    def Vertex(L: nanoocp.IntPatch.IntPatch_Line | None, I: int) -> nanoocp.IntPatch.IntPatch_Point: ...

    @staticmethod
    def FirstParameter(L: nanoocp.IntPatch.IntPatch_Line | None) -> float: ...

    @staticmethod
    def LastParameter(L: nanoocp.IntPatch.IntPatch_Line | None) -> float: ...

    @staticmethod
    def DecompositionOfWLine(theWLine: nanoocp.IntPatch.IntPatch_WLine | None, theSurface1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, theSurface2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, aTolSum: float, theLConstructor: GeomInt_LineConstructor, theNewLines: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line]) -> bool: ...

class GeomInt_MyBSplGradientOfTheComputeLineOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 1) -> None: ...

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], Deg: int, Tol3d: float, Tol2d: float, NbIterations: int, lambda1: float, lambda2: float) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating BSpline curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: GeomInt_MyBSplGradientOfTheComputeLineOfWLApprox) -> None: ...

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

class GeomInt_MyGradientbisOfTheComputeLineOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 200) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating Bezier curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: GeomInt_MyGradientbisOfTheComputeLineOfWLApprox) -> None: ...

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

class GeomInt_MyGradientOfTheComputeLineBezierOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int = 200) -> None:
        """
        Tries to minimize the sum (square(||Qui - Bi*Pi||))
        where Pui describe the approximating Bezier curves'Poles
        and Qi the MultiLine points with a parameter ui.
        In this algorithm, the parameters ui are the unknowns.
        The tolerance required on this sum is given by Tol.
        The desired degree of the resulting curve is Deg.
        """

    @overload
    def __init__(self, theOther: GeomInt_MyGradientOfTheComputeLineBezierOfWLApprox) -> None: ...

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

class GeomInt_ParameterAndOrientation:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_ParameterAndOrientation) -> None: ...

    def SetOrientation1(self, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def SetOrientation2(self, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def Parameter(self) -> float: ...

    def Orientation1(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def Orientation2(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

class GeomInt_ParLeastSquareOfMyGradientbisOfTheComputeLineOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
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
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
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
    def __init__(self, theOther: GeomInt_ParLeastSquareOfMyGradientbisOfTheComputeLineOfWLApprox) -> None: ...

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

class GeomInt_ParFunctionOfMyGradientbisOfTheComputeLineOfWLApprox(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Deg: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has the desired degree Deg.
        """

    @overload
    def __init__(self, theOther: GeomInt_ParFunctionOfMyGradientbisOfTheComputeLineOfWLApprox) -> None: ...

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

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

class GeomInt_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None: ...

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
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
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, NbPol: int) -> None:
        """Initializes the fields of the object."""

    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], FirstPoint: int, LastPoint: int, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Parameters: nanoocp.math.math_Vector, NbPol: int) -> None:
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
    def __init__(self, theOther: GeomInt_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfWLApprox) -> None: ...

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

class GeomInt_ParFunctionOfMyGradientOfTheComputeLineBezierOfWLApprox(nanoocp.math.math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Parameters: nanoocp.math.math_Vector, Deg: int) -> None:
        """
        initializes the fields of the function. The approximating
        curve has the desired degree Deg.
        """

    @overload
    def __init__(self, theOther: GeomInt_ParFunctionOfMyGradientOfTheComputeLineBezierOfWLApprox) -> None: ...

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

    def FirstConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, FirstPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

    def LastConstraint(self, TheConstraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, LastPoint: int) -> nanoocp.AppParCurves.AppParCurves_Constraint: ...

class GeomInt_ResConstraintOfMyGradientbisOfTheComputeLineOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, SCurv: nanoocp.AppParCurves.AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Bern: nanoocp.math.math_Matrix, DerivativeBern: nanoocp.math.math_Matrix, Tolerance: float = 1e-10) -> None:
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
    def __init__(self, theOther: GeomInt_ResConstraintOfMyGradientbisOfTheComputeLineOfWLApprox) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def ConstraintMatrix(self) -> nanoocp.math.math_Matrix: ...

    def Duale(self) -> nanoocp.math.math_Vector:
        """returns the duale variables of the system."""

    def ConstraintDerivative(self, SSP: GeomInt_TheMultiLineOfWLApprox, Parameters: nanoocp.math.math_Vector, Deg: int, DA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix:
        """Returns the derivative of the constraint matrix."""

    def InverseMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the Inverse of Cont*Transposed(Cont), where
        Cont is the constraint matrix for the algorithm.
        """

class GeomInt_ResConstraintOfMyGradientOfTheComputeLineBezierOfWLApprox:
    @overload
    def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, SCurv: nanoocp.AppParCurves.AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple] | None, Bern: nanoocp.math.math_Matrix, DerivativeBern: nanoocp.math.math_Matrix, Tolerance: float = 1e-10) -> None:
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
    def __init__(self, theOther: GeomInt_ResConstraintOfMyGradientOfTheComputeLineBezierOfWLApprox) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def ConstraintMatrix(self) -> nanoocp.math.math_Matrix: ...

    def Duale(self) -> nanoocp.math.math_Vector:
        """returns the duale variables of the system."""

    def ConstraintDerivative(self, SSP: GeomInt_TheMultiLineOfWLApprox, Parameters: nanoocp.math.math_Vector, Deg: int, DA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix:
        """Returns the derivative of the constraint matrix."""

    def InverseMatrix(self) -> nanoocp.math.math_Matrix:
        """
        returns the Inverse of Cont*Transposed(Cont), where
        Cont is the constraint matrix for the algorithm.
        """

class GeomInt_TheComputeLineBezierOfWLApprox:
    @overload
    def __init__(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None: ...

    @overload
    def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None: ...

    @overload
    def __init__(self, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    @overload
    def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        If <Squares> is True, the computation will be done with
        no iteration at all.
        """

    @overload
    def __init__(self, theOther: GeomInt_TheComputeLineBezierOfWLApprox) -> None: ...

    def Init(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, Line: GeomInt_TheMultiLineOfWLApprox) -> None:
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

class GeomInt_TheComputeLineOfWLApprox:
    @overload
    def __init__(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None: ...

    @overload
    def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None:
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
    def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, Parameters: nanoocp.math.math_Vector, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, Squares: bool = False) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        If <Squares> is True, the computation will be done with
        no iteration at all.
        """

    @overload
    def __init__(self, theOther: GeomInt_TheComputeLineOfWLApprox) -> None: ...

    def Interpol(self, Line: GeomInt_TheMultiLineOfWLApprox) -> None:
        """
        Constructs an interpolation of the MultiLine <Line>
        The result will be a C2 curve of degree 3.
        """

    def Init(self, degreemin: int = 4, degreemax: int = 8, Tolerance3d: float = 0.001, Tolerance2d: float = 1e-06, NbIterations: int = 5, cutting: bool = True, parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength, Squares: bool = False) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, Line: GeomInt_TheMultiLineOfWLApprox) -> None:
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

class GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def ComputeParameters(self, ChoixIso: nanoocp.IntImp.IntImp_ConstIsoparametric, Param: nanoocp.NCollection.NCollection_Array1[float], UVap: nanoocp.math.math_Vector, BornInf: nanoocp.math.math_Vector, BornSup: nanoocp.math.math_Vector, Tolerance: nanoocp.math.math_Vector) -> None: ...

    def Root(self) -> float:
        """returns somme des fi*fi"""

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangent(self, UVap: nanoocp.math.math_Vector, Param: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[bool, nanoocp.IntImp.IntImp_ConstIsoparametric]: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def DirectionOnS1(self) -> nanoocp.gp.gp_Dir2d: ...

    def DirectionOnS2(self) -> nanoocp.gp.gp_Dir2d: ...

    def AuxillarSurface1(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def AuxillarSurface2(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

class GeomInt_TheZerImpFuncOfTheImpPrmSvSurfacesOfWLApprox(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, IS: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    @overload
    def __init__(self, PS: nanoocp.Adaptor3d.Adaptor3d_Surface | None, IS: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_TheZerImpFuncOfTheImpPrmSvSurfacesOfWLApprox) -> None: ...

    @overload
    def Set(self, PS: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def Set(self, Tolerance: float) -> None: ...

    def SetImplicitSurface(self, IS: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Root(self) -> float: ...

    def Tolerance(self) -> float:
        """
        Returns the value Tol so that if std::abs(Func.Root())<Tol
        the function is considered null.
        """

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangent(self) -> bool: ...

    def Direction3d(self) -> nanoocp.gp.gp_Vec: ...

    def Direction2d(self) -> nanoocp.gp.gp_Dir2d: ...

    def PSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def ISurface(self) -> nanoocp.IntSurf.IntSurf_Quadric: ...

class GeomInt_TheImpPrmSvSurfacesOfWLApprox(nanoocp.ApproxInt.ApproxInt_SvSurfaces):
    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Surf2: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    @overload
    def __init__(self, Surf1: nanoocp.IntSurf.IntSurf_Quadric, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_TheImpPrmSvSurfacesOfWLApprox) -> None: ...

    def Compute(self, Pt: nanoocp.gp.gp_Pnt, Tg: nanoocp.gp.gp_Vec, Tguv1: nanoocp.gp.gp_Vec2d, Tguv2: nanoocp.gp.gp_Vec2d) -> tuple[bool, float, float, float, float]:
        """returns True if Tg,Tguv1 Tguv2 can be computed."""

    def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: nanoocp.IntSurf.IntSurf_PntOn2S) -> bool: ...

    def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec) -> bool: ...

    def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec2d) -> bool: ...

    def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec2d) -> bool: ...

    def FillInitialVectorOfSolution(self, u1: float, v1: float, u2: float, v2: float, binfu: float, bsupu: float, binfv: float, bsupv: float, X: nanoocp.math.math_Vector) -> tuple[bool, float, float]: ...

class GeomInt_TheInt2SOfThePrmPrmSvSurfacesOfWLApprox:
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TolTangency: float) -> None:
        """
        initialize the parameters to compute the solution point
        it 's possible to write to optimize:
        IntImp_Int2S inter(S1,S2,Func,TolTangency);
        math_FunctionSetRoot rsnld(inter.Function());
        while ...{
        Param(1)=...
        Param(2)=...
        param(3)=...
        inter.Perform(Param,rsnld);
        }
        """

    @overload
    def __init__(self, Param: nanoocp.NCollection.NCollection_Array1[float], S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TolTangency: float) -> None:
        """compute the solution point with the close point"""

    @overload
    def __init__(self, theOther: GeomInt_TheInt2SOfThePrmPrmSvSurfacesOfWLApprox) -> None: ...

    @overload
    def Perform(self, Param: nanoocp.NCollection.NCollection_Array1[float], Rsnld: nanoocp.math.math_FunctionSetRoot) -> nanoocp.IntImp.IntImp_ConstIsoparametric:
        """
        returns the best constant isoparametric to find
        the next intersection's point +stores the solution
        point (the solution point is found with the close point
        to intersect the isoparametric with the other patch;
        the choice of the isoparametic is calculated)
        """

    @overload
    def Perform(self, Param: nanoocp.NCollection.NCollection_Array1[float], Rsnld: nanoocp.math.math_FunctionSetRoot, ChoixIso: nanoocp.IntImp.IntImp_ConstIsoparametric) -> nanoocp.IntImp.IntImp_ConstIsoparametric:
        """
        returns the best constant isoparametric to find
        the next intersection's point +stores the solution
        point (the solution point is found with the close point
        to intersect the isoparametric with the other patch;
        the choice of the isoparametic is given by ChoixIso)
        """

    def IsDone(self) -> bool:
        """Returns TRUE if the creation completed without failure."""

    def IsEmpty(self) -> bool:
        """Returns TRUE when there is no solution to the problem."""

    def Point(self) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """Returns the intersection point."""

    def IsTangent(self) -> bool:
        """
        Returns True if the surfaces are tangent at the
        intersection point.
        """

    def Direction(self) -> nanoocp.gp.gp_Dir:
        """Returns the tangent at the intersection line."""

    def DirectionOnS1(self) -> nanoocp.gp.gp_Dir2d:
        """
        Returns the tangent at the intersection line in the
        parametric space of the first surface.
        """

    def DirectionOnS2(self) -> nanoocp.gp.gp_Dir2d:
        """
        Returns the tangent at the intersection line in the
        parametric space of the second surface.
        """

    def Function(self) -> GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox:
        """
        return the math function which
        is used to compute the intersection
        """

    def ChangePoint(self) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """
        return the intersection point which is
        enable for changing.
        """

class GeomInt_TheMultiLineToolOfWLApprox:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_TheMultiLineToolOfWLApprox) -> None: ...

    @staticmethod
    def FirstPoint(ML: GeomInt_TheMultiLineOfWLApprox) -> int:
        """Returns the number of multipoints of the TheMultiLine."""

    @staticmethod
    def LastPoint(ML: GeomInt_TheMultiLineOfWLApprox) -> int:
        """Returns the number of multipoints of the TheMultiLine."""

    @staticmethod
    def NbP2d(ML: GeomInt_TheMultiLineOfWLApprox) -> int:
        """Returns the number of 2d points of a TheMultiLine."""

    @staticmethod
    def NbP3d(ML: GeomInt_TheMultiLineOfWLApprox) -> int:
        """Returns the number of 3d points of a TheMultiLine."""

    @overload
    @staticmethod
    def Value(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabPt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        returns the 3d points of the multipoint <MPointIndex>
        when only 3d points exist.
        """

    @overload
    @staticmethod
    def Value(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabPt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        returns the 2d points of the multipoint <MPointIndex>
        when only 2d points exist.
        """

    @overload
    @staticmethod
    def Value(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabPt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabPt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        returns the 3d and 2d points of the multipoint
        <MPointIndex>.
        """

    @overload
    @staticmethod
    def Tangency(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """
        returns the 3d points of the multipoint <MPointIndex>
        when only 3d points exist.
        """

    @overload
    @staticmethod
    def Tangency(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 2d tangency points of the multipoint
        <MPointIndex> only when 2d points exist.
        """

    @overload
    @staticmethod
    def Tangency(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 3d and 2d points of the multipoint
        <MPointIndex>.
        """

    @overload
    @staticmethod
    def Curvature(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """
        returns the 3d curvature of the multipoint <MPointIndex>
        when only 3d points exist.
        """

    @overload
    @staticmethod
    def Curvature(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 2d curvature points of the multipoint
        <MPointIndex> only when 2d points exist.
        """

    @overload
    @staticmethod
    def Curvature(ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], tabV2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]) -> bool:
        """
        returns the 3d and 2d curvature of the multipoint
        <MPointIndex>.
        """

    @staticmethod
    def MakeMLBetween(ML: GeomInt_TheMultiLineOfWLApprox, I1: int, I2: int, NbPMin: int) -> GeomInt_TheMultiLineOfWLApprox:
        """Is called if WhatStatus returned "PointsAdded"."""

    @staticmethod
    def MakeMLOneMorePoint(ML: GeomInt_TheMultiLineOfWLApprox, I1: int, I2: int, indbad: int, OtherLine: GeomInt_TheMultiLineOfWLApprox) -> bool:
        """Is called when the Bezier curve contains a loop"""

    @staticmethod
    def WhatStatus(ML: GeomInt_TheMultiLineOfWLApprox, I1: int, I2: int) -> nanoocp.Approx.Approx_Status: ...

    @staticmethod
    def Dump(ML: GeomInt_TheMultiLineOfWLApprox) -> None:
        """Dump of the current multi-line."""

class GeomInt_ThePrmPrmSvSurfacesOfWLApprox(nanoocp.ApproxInt.ApproxInt_SvSurfaces):
    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_ThePrmPrmSvSurfacesOfWLApprox) -> None: ...

    def Compute(self, Pt: nanoocp.gp.gp_Pnt, Tg: nanoocp.gp.gp_Vec, Tguv1: nanoocp.gp.gp_Vec2d, Tguv2: nanoocp.gp.gp_Vec2d) -> tuple[bool, float, float, float, float]:
        """returns True if Tg,Tguv1 Tguv2 can be computed."""

    def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: nanoocp.IntSurf.IntSurf_PntOn2S) -> bool: ...

    def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec) -> bool: ...

    def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec2d) -> bool: ...

    def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: nanoocp.gp.gp_Vec2d) -> bool: ...

class GeomInt_WLApprox:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomInt_WLApprox) -> None: ...

    @overload
    def Perform(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, aLine: nanoocp.IntPatch.IntPatch_WLine | None, ApproxXYZ: bool = True, ApproxU1V1: bool = True, ApproxU2V2: bool = True, indicemin: int = 0, indicemax: int = 0) -> None: ...

    @overload
    def Perform(self, aLine: nanoocp.IntPatch.IntPatch_WLine | None, ApproxXYZ: bool = True, ApproxU1V1: bool = True, ApproxU2V2: bool = True, indicemin: int = 0, indicemax: int = 0) -> None: ...

    def SetParameters(self, Tol3d: float, Tol2d: float, DegMin: int, DegMax: int, NbIterMax: int, NbPntMax: int = 30, ApproxWithTangency: bool = True, Parametrization: nanoocp.Approx.Approx_ParametrizationType = Approx_ParametrizationType.Approx_ChordLength) -> None: ...

    def TolReached3d(self) -> float: ...

    def TolReached2d(self) -> float: ...

    def IsDone(self) -> bool: ...

    def NbMultiCurves(self) -> int: ...

    def Value(self, Index: int) -> nanoocp.AppParCurves.AppParCurves_MultiBSpCurve: ...

    @staticmethod
    def Parameters(Line: GeomInt_TheMultiLineOfWLApprox, firstP: int, lastP: int, Par: nanoocp.Approx.Approx_ParametrizationType, TheParameters: nanoocp.math.math_Vector) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
GeomInt_VectorOfReal = nanoocp.NCollection.NCollection_DynamicArray[float]
