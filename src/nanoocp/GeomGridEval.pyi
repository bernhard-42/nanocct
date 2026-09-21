"""OCCT package GeomGridEval (toolkit TKG3d)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp


class GeomGridEval_Line:
    """
    @brief Efficient batch evaluator for line grid points.

    Uses direct analytical formula: P(t) = Location + t * Direction

    Usage:
    @code
    GeomGridEval_Line anEvaluator(myGeomLine);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theLine: nanoocp.Geom.Geom_Line | None) -> None:
        """
        Constructor with geometry.
        @param theLine the line geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_Line:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        For a line, D1 is constant (the direction vector).
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        For a line, D1 is constant and D2 is zero.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        For a line, D1 is constant, D2 and D3 are zero.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        For a line: D1 = Direction, DN = 0 for N > 1.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing),
        or empty array if geometry is null or no parameters
        """

class GeomGridEval_Circle:
    """
    @brief Efficient batch evaluator for circle grid points.

    Uses analytical formula: P(u) = Center + R * (cos(u) * XDir + sin(u) * YDir)

    Usage:
    @code
    GeomGridEval_Circle anEvaluator(myGeomCircle);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theCircle: nanoocp.Geom.Geom_Circle | None) -> None:
        """
        Constructor with geometry.
        @param theCircle the circle geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_Circle:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values (angles in radians)
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        D1 = R * (-sin(u) * XDir + cos(u) * YDir)
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        D2 = R * (-cos(u) * XDir - sin(u) * YDir) = -P (relative to center)
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        D3 = R * (sin(u) * XDir - cos(u) * YDir) = -D1
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        Circle has cyclic derivatives with period 4:
        D1 = R * (-sin(u) * X + cos(u) * Y)
        D2 = R * (-cos(u) * X - sin(u) * Y)
        D3 = R * (sin(u) * X - cos(u) * Y)
        D4 = R * (cos(u) * X + sin(u) * Y) = D0, then repeats
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing),
        or empty array if geometry is null or no parameters
        """

class GeomGridEval_Ellipse:
    """
    @brief Efficient batch evaluator for ellipse grid points.

    Uses analytical formula:
    P(u) = Center + MajorRadius * cos(u) * XDir + MinorRadius * sin(u) * YDir

    Usage:
    @code
    GeomGridEval_Ellipse anEvaluator(myGeomEllipse);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theEllipse: nanoocp.Geom.Geom_Ellipse | None) -> None:
        """
        Constructor with geometry.
        @param theEllipse the ellipse geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_Ellipse:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        Ellipse has cyclic derivatives with period 4:
        D1 = -MajR * sin(u) * X + MinR * cos(u) * Y
        D2 = -MajR * cos(u) * X - MinR * sin(u) * Y
        D3 = MajR * sin(u) * X - MinR * cos(u) * Y
        D4 = MajR * cos(u) * X + MinR * sin(u) * Y = D0, then repeats
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Hyperbola:
    """
    @brief Efficient batch evaluator for hyperbola grid points.

    Uses analytical formula:
    P(u) = Center + MajorRadius * cosh(u) * XDir + MinorRadius * sinh(u) * YDir

    Usage:
    @code
    GeomGridEval_Hyperbola anEvaluator(myGeomHyperbola);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theHyperbola: nanoocp.Geom.Geom_Hyperbola | None) -> None:
        """
        Constructor with geometry.
        @param theHyperbola the hyperbola geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_Hyperbola:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        Hyperbola has cyclic derivatives with period 2:
        D1 = MajR * sinh(u) * X + MinR * cosh(u) * Y
        D2 = MajR * cosh(u) * X + MinR * sinh(u) * Y = D0
        D3 = D1, D4 = D0, etc.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Parabola:
    """
    @brief Efficient batch evaluator for parabola grid points.

    Uses analytical formula:
    P(u) = Center + (u^2 / (4*Focal)) * XDir + u * YDir

    Usage:
    @code
    GeomGridEval_Parabola anEvaluator(myGeomParabola);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theParabola: nanoocp.Geom.Geom_Parabola | None) -> None:
        """
        Constructor with geometry.
        @param theParabola the parabola geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_Parabola:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        Parabola: P = Center + (u^2/4F) * X + u * Y
        D1 = (u/2F) * X + Y (depends on u)
        D2 = (1/2F) * X (constant)
        DN = 0 for N >= 3
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_BezierCurve:
    """
    @brief Efficient batch evaluator for Bezier curve grid points.

    Uses BSplCLib to evaluate Bezier curves (treated as B-Splines).

    Usage:
    @code
    GeomGridEval_BezierCurve anEvaluator(myGeomBezier);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theBezier: nanoocp.Geom.Geom_BezierCurve | None) -> None:
        """
        Constructor with geometry.
        @param theBezier the bezier curve geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_BezierCurve:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses BSplCLib::DN.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_BSplineCurve:
    """
    @brief Efficient batch evaluator for B-spline curve grid points.

    Optimizes evaluation of multiple points on a B-spline curve by:
    - Pre-computing span indices for input parameters (no runtime binary search)
    - Pre-grouping parameters by span for cache-optimal iteration
    - Rebuilding cache only once per span block (not per point)
    - Using KnotSequence() from Geom_BSplineCurve for direct flat knot access

    Usage:
    @code
    GeomGridEval_BSplineCurve anEvaluator(myBSplineCurve);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theCurve: nanoocp.Geom.Geom_BSplineCurve | None) -> None:
        """
        Constructor with geometry.
        @param theCurve the B-spline curve to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        Points are evaluated in span-grouped order to minimize cache rebuilds.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses geometry DN method.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_OtherCurve:
    """
    @brief Fallback evaluator for unknown curve types.

    Uses Adaptor3d_Curve::D0 for point-by-point evaluation.
    This is the slowest evaluator but handles any curve type.

    @note The curve adaptor reference must remain valid during the lifetime
    of this evaluator. The evaluator does not take ownership.

    Usage:
    @code
    GeomGridEval_OtherCurve anEvaluator(myCurveAdaptor);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Constructor with curve adaptor reference.
        @param theCurve reference to curve adaptor (must remain valid)
        """

    def Curve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Returns the curve adaptor reference."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses adaptor DN method.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_OffsetCurve:
    """
    @brief Batch evaluator for offset curve grid points.

    Evaluates the offset curve formula:
    P(u) = C(u) + Offset * (D1(u) ^ Direction) / |D1(u) ^ Direction|

    Uses GeomGridEval_Curve for batch evaluation of the basis curve,
    then applies offset transformation.

    Usage:
    @code
    GeomGridEval_OffsetCurve anEvaluator(myGeomOffset);
    NCollection_Array1<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theOffset: nanoocp.Geom.Geom_OffsetCurve | None) -> None:
        """
        Constructor with geometry.
        @param theOffset the offset curve geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_OffsetCurve:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate all grid points with derivatives up to third order.
        Uses GeomAdaptor_Curve::D3 for evaluation.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses geometry DN method.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Curve:
    """
    @brief Unified grid evaluator for any 3D curve.

    Uses std::variant for compile-time type safety and zero heap allocation
    for the evaluator itself. Automatically detects curve type from
    Adaptor3d_Curve and dispatches to the appropriate specialized evaluator.

    Supported curve types with optimized evaluation:
    - Line: Direct analytical formula
    - Circle: Trigonometric formula
    - Ellipse: Analytical formula
    - Hyperbola: Analytical formula
    - Parabola: Analytical formula
    - BezierCurve: Optimized batch evaluation via BSplCLib
    - BSplineCurve: Optimized batch evaluation via BSplCLib_GridEvaluator
    - Other: Fallback using Adaptor3d_Curve::D0

    Usage:
    @code
    GeomGridEval_Curve anEval(myAdaptorCurve);
    // OR
    GeomGridEval_Curve anEval(myGeomCurve);
    NCollection_Array1<gp_Pnt> aGrid = anEval.EvaluateGrid(myParams);
    @endcode
    """

    @overload
    def __init__(self, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Construct from adaptor reference (auto-detects curve type).
        For GeomAdaptor_Curve, extracts underlying Geom_Curve for optimized evaluation.
        For other adaptors, stores reference for fallback evaluation.
        @note The curve adaptor reference must remain valid during the lifetime
        of this evaluator when using fallback evaluation.
        @param[in] theCurve curve adaptor reference to evaluate
        """

    @overload
    def __init__(self, theCurve: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Construct from geometry handle (auto-detects curve type).
        @param[in] theCurve geometry to evaluate
        """

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at all parameters.
        @param theParams array of parameter values
        @return array of 3D points (1-based indexing)
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD1]:
        """
        Evaluate grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD2]:
        """
        Evaluate grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve.ResD3]:
        """
        Evaluate grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]:
        """
        Evaluate Nth derivative at all grid points.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """Returns the detected curve type."""

class GeomGridEval_Plane:
    """
    @brief Efficient batch evaluator for plane grid points.

    Uses direct analytical formula: P(u,v) = Location + u * XDir + v * YDir
    This is a header-only implementation for maximum performance.

    Usage:
    @code
    GeomGridEval_Plane anEvaluator(myGeomPlane);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, thePlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Constructor with geometry.
        @param thePlane the plane geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_Plane:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of evaluated points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Cylinder:
    """
    @brief Efficient batch evaluator for cylinder grid points.

    Uses analytical formula:
    P(u,v) = Location + R * (cos(u) * XDir + sin(u) * YDir) + v * ZDir

    Where U is angle (0 to 2*PI) and V is height.

    Usage:
    @code
    GeomGridEval_Cylinder anEvaluator(myGeomCylinder);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theCylinder: nanoocp.Geom.Geom_CylindricalSurface | None) -> None:
        """
        Constructor with geometry.
        @param theCylinder the cylindrical surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_CylindricalSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (height)
        @return 2D array of evaluated points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (height)
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (height)
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (height)
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        For a cylinder:
        - U derivatives are cyclic (period 4): D_nU = R * (cyclic trig)
        - V derivatives: D1V = ZDir, higher = 0
        - Mixed: D_{nu,nv} = 0 for nv > 1
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (height)
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Sphere:
    """
    @brief Efficient batch evaluator for sphere grid points.

    Uses analytical formula:
    P(u,v) = Center + R * (cos(v) * cos(u) * XDir + cos(v) * sin(u) * YDir + sin(v) * ZDir)

    Where U is longitude (0 to 2*PI) and V is latitude (-PI/2 to PI/2).

    Usage:
    @code
    GeomGridEval_Sphere anEvaluator(myGeomSphere);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theSphere: nanoocp.Geom.Geom_SphericalSurface | None) -> None:
        """
        Constructor with geometry.
        @param theSphere the spherical surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_SphericalSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        @param theUParams array of U parameter values (longitude)
        @param theVParams array of V parameter values (latitude)
        @return 2D array of evaluated points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values (longitude)
        @param theVParams array of V parameter values (latitude)
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values (longitude)
        @param theVParams array of V parameter values (latitude)
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param theUParams array of U parameter values (longitude)
        @param theVParams array of V parameter values (latitude)
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses geometry DN method.
        @param theUParams array of U parameter values (longitude)
        @param theVParams array of V parameter values (latitude)
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Cone:
    """
    @brief Efficient batch evaluator for cone grid points.

    Uses analytical formula:
    P(u,v) = Location + (RefRadius + v * sin(SemiAngle)) * (cos(u) * XDir + sin(u) * YDir) + v *
    cos(SemiAngle) * ZDir

    Where U is angle (0 to 2*PI) and V is linear parameter along the ruling.

    Usage:
    @code
    GeomGridEval_Cone anEvaluator(myGeomCone);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theCone: nanoocp.Geom.Geom_ConicalSurface | None) -> None:
        """
        Constructor with geometry.
        @param theCone the conical surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_ConicalSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (linear along ruling)
        @return 2D array of evaluated points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (linear along ruling)
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (linear along ruling)
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (linear along ruling)
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses geometry DN method.
        @param theUParams array of U parameter values (angle)
        @param theVParams array of V parameter values (linear along ruling)
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Torus:
    """
    @brief Efficient batch evaluator for torus grid points.

    Uses analytical formula:
    P(u,v) = Location + (MajorRadius + MinorRadius * cos(v)) * (cos(u) * XDir + sin(u) * YDir) +
    MinorRadius * sin(v) * ZDir

    Where U is major angle (0 to 2*PI) and V is minor angle (0 to 2*PI).

    Usage:
    @code
    GeomGridEval_Torus anEvaluator(myGeomTorus);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theTorus: nanoocp.Geom.Geom_ToroidalSurface | None) -> None:
        """
        Constructor with geometry.
        @param theTorus the toroidal surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_ToroidalSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        @param theUParams array of U parameter values (major angle)
        @param theVParams array of V parameter values (minor angle)
        @return 2D array of evaluated points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values (major angle)
        @param theVParams array of V parameter values (minor angle)
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values (major angle)
        @param theVParams array of V parameter values (minor angle)
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param theUParams array of U parameter values (major angle)
        @param theVParams array of V parameter values (minor angle)
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses geometry DN method.
        @param theUParams array of U parameter values (major angle)
        @param theVParams array of V parameter values (minor angle)
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_BezierSurface:
    """
    @brief Efficient batch evaluator for Bezier surface grid points.

    Uses BSplSLib_Cache for optimized polynomial evaluation.
    Bezier surfaces are treated as single-span B-spline surfaces.

    Usage:
    @code
    GeomGridEval_BezierSurface anEvaluator(myGeomBezier);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theBezier: nanoocp.Geom.Geom_BezierSurface | None) -> None:
        """
        Constructor with geometry.
        @param theBezier the bezier surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_BezierSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate all grid points with first partial derivatives.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD1 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate all grid points with first and second partial derivatives.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD2 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate all grid points with derivatives up to third order.
        Uses direct Geom_BezierSurface::D3 evaluation.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD3 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses geometry DN method.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @param[in] theNU derivative order in U direction
        @param[in] theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_OffsetSurface:
    """
    @brief Batch evaluator for offset surface grid points.

    Evaluates the offset surface formula:
    P(u,v) = S(u,v) + Offset * Normal(u,v)

    Uses GeomGridEval_Surface for batch evaluation of the basis surface,
    then applies offset transformation.

    Usage:
    @code
    GeomGridEval_OffsetSurface anEvaluator(myGeomOffset);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theOffset: nanoocp.Geom.Geom_OffsetSurface | None) -> None:
        """
        Constructor with geometry.
        @param theOffset the offset surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_OffsetSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate all grid points with first partial derivatives.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD1 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate all grid points with first and second partial derivatives.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD2 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate all grid points with derivatives up to third order.
        Uses GeomAdaptor_Surface::D3 for evaluation.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD3 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        Uses geometry DN method.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @param[in] theNU derivative order in U direction
        @param[in] theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_BSplineSurface:
    """
    @brief Efficient batch evaluator for B-spline surface points.

    Stateless evaluator - constructor takes geometry, parameters passed to methods.

    Optimizes evaluation by:
    - Pre-computing span indices for U and V parameters separately (O(aNbU + aNbV))
    - Grouping evaluation by (USpan, VSpan) for cache-optimal iteration
    - Rebuilding cache only once per span group (not per point)
    - Writing results directly to 2D output grid (no intermediate buffers)

    Usage:
    @code
    GeomGridEval_BSplineSurface anEvaluator(myBSplineSurface);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theSurface: nanoocp.Geom.Geom_BSplineSurface | None) -> None:
        """
        Constructor with geometry.
        @param theSurface the B-spline surface to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        Points are evaluated in span-grouped order to minimize cache rebuilds.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of evaluated points (1-based indexing),
        or empty array if geometry is null or parameters empty
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD1 (1-based indexing),
        or empty array if geometry is null or parameters empty
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD2 (1-based indexing),
        or empty array if geometry is null or parameters empty
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        Uses direct BSplSLib::D3 evaluation (no caching for D3).
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD3 (1-based indexing),
        or empty array if geometry is null or parameters empty
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        For orders > degree in either direction, returns zero.
        Uses direct geometry DN method.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_OtherSurface:
    """
    @brief Fallback evaluator for any surface type.

    Uses D0/D1/D2/D3/DN methods for point-by-point evaluation. Supports both
    Adaptor3d_Surface (by pointer) and occ::handle<Geom_Surface> as input.
    This is the slowest evaluator but handles any surface type.

    @note When using adaptor pointer, the adaptor must remain valid
    during the lifetime of this evaluator.

    Usage:
    @code
    GeomGridEval_OtherSurface anEvaluator(&mySurfaceAdaptor);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    @overload
    def __init__(self, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Constructor with surface adaptor pointer.
        @param theSurface pointer to surface adaptor (must remain valid)
        """

    @overload
    def __init__(self, theSurface: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Constructor with geometry handle.
        @param theSurface handle to Geom_Surface
        """

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at Cartesian product of U and V parameters.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of evaluated points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative at all grid points.
        @param theUParams array of U parameter values
        @param theVParams array of V parameter values
        @param theNU derivative order in U direction
        @param theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_SurfaceOfRevolution:
    """
    @brief Optimized batch evaluator for revolution surface grid points.

    Evaluates the revolution surface formula:
    S(u, v) = Rotation(u, Axis) * C(v)

    Where:
    - C(v) is the meridian (basis curve)
    - u is the rotation angle around the axis
    - Axis is the axis of revolution

    Optimization: Uses GeomGridEval_Curve for batch evaluation of the basis curve,
    then applies rotation transformations. Precomputes sin/cos values for each U parameter.

    Mathematical formulas for derivatives:
    - D1U = Axis Cross (P - AxisLocation), then rotated
    - D1V = C'(v), rotated
    - D2U = (Axis Dot (P - AxisLocation)) * Axis - (P - AxisLocation), then rotated
    - D2UV = Axis Cross C'(v), then rotated
    - D2V = C''(v), rotated

    Usage:
    @code
    GeomGridEval_SurfaceOfRevolution anEvaluator(myRevolutionSurface);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theRevolution: nanoocp.Geom.Geom_SurfaceOfRevolution | None) -> None:
        """
        Constructor with geometry.
        @param theRevolution the revolution surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_SurfaceOfRevolution:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param[in] theUParams array of U parameter values (rotation angle)
        @param[in] theVParams array of V parameter values (curve parameter)
        @return 2D array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate all grid points with first partial derivatives.
        @param[in] theUParams array of U parameter values (rotation angle)
        @param[in] theVParams array of V parameter values (curve parameter)
        @return 2D array of SurfD1 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate all grid points with first and second partial derivatives.
        @param[in] theUParams array of U parameter values (rotation angle)
        @param[in] theVParams array of V parameter values (curve parameter)
        @return 2D array of SurfD2 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate all grid points with derivatives up to third order.
        @param[in] theUParams array of U parameter values (rotation angle)
        @param[in] theVParams array of V parameter values (curve parameter)
        @return 2D array of SurfD3 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        @param[in] theUParams array of U parameter values (rotation angle)
        @param[in] theVParams array of V parameter values (curve parameter)
        @param[in] theNU derivative order in U direction
        @param[in] theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_SurfaceOfExtrusion:
    """
    @brief Optimized batch evaluator for linear extrusion surface grid points.

    Evaluates the extrusion surface formula:
    S(u, v) = C(u) + v * Direction

    Where:
    - C(u) is the basis curve
    - v is the extrusion parameter
    - Direction is the extrusion direction (unit vector)

    Optimization: Uses GeomGridEval_Curve for batch evaluation of the basis curve,
    then applies the linear shift v*Direction for each grid point.
    This is more efficient than point-by-point evaluation.

    Usage:
    @code
    GeomGridEval_SurfaceOfExtrusion anEvaluator(myExtrusionSurface);
    NCollection_Array2<gp_Pnt> aGrid = anEvaluator.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    def __init__(self, theExtrusion: nanoocp.Geom.Geom_SurfaceOfLinearExtrusion | None) -> None:
        """
        Constructor with geometry.
        @param theExtrusion the extrusion surface geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom.Geom_SurfaceOfLinearExtrusion:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate all grid points.
        @param[in] theUParams array of U parameter values (curve parameter)
        @param[in] theVParams array of V parameter values (extrusion distance)
        @return 2D array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate all grid points with first partial derivatives.
        @param[in] theUParams array of U parameter values (curve parameter)
        @param[in] theVParams array of V parameter values (extrusion distance)
        @return 2D array of SurfD1 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate all grid points with first and second partial derivatives.
        @param[in] theUParams array of U parameter values (curve parameter)
        @param[in] theVParams array of V parameter values (extrusion distance)
        @return 2D array of SurfD2 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate all grid points with derivatives up to third order.
        @param[in] theUParams array of U parameter values (curve parameter)
        @param[in] theVParams array of V parameter values (extrusion distance)
        @return 2D array of SurfD3 (1-based indexing),
        or empty array if geometry is null or no parameters set
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        @param[in] theUParams array of U parameter values (curve parameter)
        @param[in] theVParams array of V parameter values (extrusion distance)
        @param[in] theNU derivative order in U direction
        @param[in] theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

class GeomGridEval_Surface:
    """
    @brief Unified grid evaluator for any 3D surface.

    Uses std::variant for compile-time type safety and zero heap allocation
    for the evaluator itself. Automatically detects surface type from
    Adaptor3d_Surface and dispatches to the appropriate specialized evaluator.

    Supported surface types with optimized evaluation:
    - Plane: Direct analytical formula
    - Cylinder: Analytical formula
    - Sphere: Trigonometric formula
    - Cone: Analytical formula
    - Torus: Analytical formula
    - BezierSurface: Optimized batch evaluation via BSplSLib
    - BSplineSurface: Optimized batch evaluation with span-based caching
    - OffsetSurface: Optimized batch evaluation using basis surface derivatives
    - SurfaceOfRevolution: Batch evaluation using basis curve
    - SurfaceOfExtrusion: Batch evaluation using basis curve
    - Other: Fallback using Adaptor3d_Surface::D0

    Usage:
    @code
    GeomGridEval_Surface anEval(myAdaptorSurface);
    // OR
    GeomGridEval_Surface anEval(myGeomSurface);
    // Grid evaluation
    NCollection_Array2<gp_Pnt> aGrid = anEval.EvaluateGrid(myUParams, myVParams);
    @endcode
    """

    @overload
    def __init__(self, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Construct from adaptor reference (auto-detects surface type).
        For GeomAdaptor_Surface, extracts underlying Geom_Surface for optimized evaluation.
        For other adaptors, stores reference for fallback evaluation.
        @note The surface adaptor reference must remain valid during the lifetime
        of this evaluator when using fallback evaluation.
        @param[in] theSurface surface adaptor reference to evaluate
        """

    @overload
    def __init__(self, theSurface: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Construct from geometry handle (auto-detects surface type).
        @param[in] theSurface geometry to evaluate
        """

    def EvaluateGrid(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]:
        """
        Evaluate grid points at all specified parameters.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of 3D points (1-based indexing)
        """

    def EvaluateGridD1(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD1]:
        """
        Evaluate grid points with first partial derivatives.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD2]:
        """
        Evaluate grid points with first and second partial derivatives.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface.ResD3]:
        """
        Evaluate grid points with derivatives up to third order.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @return 2D array of SurfD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theUParams: nanoocp.NCollection.NCollection_Array1[float], theVParams: nanoocp.NCollection.NCollection_Array1[float], theNU: int, theNV: int) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]:
        """
        Evaluate partial derivative d^(NU+NV)S/(dU^NU dV^NV) at all grid points.
        @param[in] theUParams array of U parameter values
        @param[in] theVParams array of V parameter values
        @param[in] theNU derivative order in U direction
        @param[in] theNV derivative order in V direction
        @return 2D array of derivative vectors (1-based indexing)
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """Returns the detected surface type."""

    def HasTransformation(self) -> bool:
        """Returns true if a transformation is applied."""

    def GetTransformation(self) -> nanoocp.gp.gp_Trsf | None:
        """Returns the transformation (empty if not set)."""

# C++ typedef aliases
CurveD1 = nanoocp.Geom.Geom_Curve.ResD1
CurveD2 = nanoocp.Geom.Geom_Curve.ResD2
CurveD3 = nanoocp.Geom.Geom_Curve.ResD3
SurfD1 = nanoocp.Geom.Geom_Surface.ResD1
SurfD2 = nanoocp.Geom.Geom_Surface.ResD2
SurfD3 = nanoocp.Geom.Geom_Surface.ResD3
