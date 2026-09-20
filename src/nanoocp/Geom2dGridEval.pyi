"""OCCT package Geom2dGridEval (toolkit TKG2d)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.Geom2dGridEval


class CurveD1:
    """Result structure for curve D1 evaluation (point and first derivative)."""

    def __init__(self) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt2d: ...

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt2d, /) -> None: ...

    @property
    def D1(self) -> nanoocp.gp.gp_Vec2d: ...

    @D1.setter
    def D1(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

class CurveD2:
    """
    Result structure for curve D2 evaluation (point and first two derivatives).
    """

    def __init__(self) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt2d: ...

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt2d, /) -> None: ...

    @property
    def D1(self) -> nanoocp.gp.gp_Vec2d: ...

    @D1.setter
    def D1(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

    @property
    def D2(self) -> nanoocp.gp.gp_Vec2d: ...

    @D2.setter
    def D2(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

class CurveD3:
    """
    Result structure for curve D3 evaluation (point and first three derivatives).
    """

    def __init__(self) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt2d: ...

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt2d, /) -> None: ...

    @property
    def D1(self) -> nanoocp.gp.gp_Vec2d: ...

    @D1.setter
    def D1(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

    @property
    def D2(self) -> nanoocp.gp.gp_Vec2d: ...

    @D2.setter
    def D2(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

    @property
    def D3(self) -> nanoocp.gp.gp_Vec2d: ...

    @D3.setter
    def D3(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

class Geom2dGridEval_BezierCurve:
    """
    @brief Efficient batch evaluator for 2D Bezier curve grid points.

    Uses BSplCLib to evaluate Bezier curves (treated as B-Splines).

    Usage:
    @code
    Geom2dGridEval_BezierCurve anEvaluator(myGeom2dBezier);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theBezier: nanoocp.Geom2d.Geom2d_BezierCurve) -> None:
        """
        Constructor with geometry.
        @param theBezier the 2D bezier curve geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_BezierCurve:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses BSplCLib::DN.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class Geom2dGridEval_BSplineCurve:
    """
    @brief Efficient batch evaluator for 2D B-spline curve grid points.

    Optimizes evaluation of multiple points on a 2D B-spline curve by:
    - Pre-computing span indices for input parameters (no runtime binary search)
    - Pre-grouping parameters by span for cache-optimal iteration
    - Rebuilding cache only once per span block (not per point)
    - Using KnotSequence() from Geom2d_BSplineCurve for direct flat knot access

    Usage:
    @code
    Geom2dGridEval_BSplineCurve anEvaluator(myBSplineCurve2d);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theCurve: nanoocp.Geom2d.Geom2d_BSplineCurve) -> None:
        """
        Constructor with geometry.
        @param theCurve the 2D B-spline curve to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        Points are evaluated in span-grouped order to minimize cache rebuilds.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses BSplCLib::DN.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class Geom2dGridEval_Circle:
    """
    @brief Efficient batch evaluator for 2D circle grid points.

    Uses analytical formula: P(u) = Center + R * (cos(u) * XDir + sin(u) * YDir)

    Usage:
    @code
    Geom2dGridEval_Circle anEvaluator(myGeom2dCircle);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theCircle: nanoocp.Geom2d.Geom2d_Circle) -> None:
        """
        Constructor with geometry.
        @param theCircle the 2D circle geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Circle:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values (angles in radians)
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        D1 = R * (-sin(u) * XDir + cos(u) * YDir)
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        D2 = R * (-cos(u) * XDir - sin(u) * YDir) = -P (relative to center)
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        D3 = R * (sin(u) * XDir - cos(u) * YDir) = -D1
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
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

class Geom2dGridEval_Ellipse:
    """
    @brief Efficient batch evaluator for 2D ellipse grid points.

    Uses analytical formula:
    P(u) = Center + MajorRadius * cos(u) * XDir + MinorRadius * sin(u) * YDir

    Usage:
    @code
    Geom2dGridEval_Ellipse anEvaluator(myGeom2dEllipse);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theEllipse: nanoocp.Geom2d.Geom2d_Ellipse) -> None:
        """
        Constructor with geometry.
        @param theEllipse the 2D ellipse geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Ellipse:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        Ellipse has cyclic derivatives with period 4:
        D1 = -MajR * sin(u) * X + MinR * cos(u) * Y
        D2 = -MajR * cos(u) * X - MinR * sin(u) * Y
        D3 = MajR * sin(u) * X - MinR * cos(u) * Y
        D4 = MajR * cos(u) * X + MinR * sin(u) * Y = D0, then repeats
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing),
        or empty array if geometry is null or no parameters
        """

class Geom2dGridEval_Hyperbola:
    """
    @brief Efficient batch evaluator for 2D hyperbola grid points.

    Uses analytical formula:
    P(u) = Center + MajorRadius * cosh(u) * XDir + MinorRadius * sinh(u) * YDir

    Usage:
    @code
    Geom2dGridEval_Hyperbola anEvaluator(myGeom2dHyperbola);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theHyperbola: nanoocp.Geom2d.Geom2d_Hyperbola) -> None:
        """
        Constructor with geometry.
        @param theHyperbola the 2D hyperbola geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Hyperbola:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
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

class Geom2dGridEval_Line:
    """
    @brief Efficient batch evaluator for 2D line grid points.

    Uses direct analytical formula: P(t) = Location + t * Direction

    Usage:
    @code
    Geom2dGridEval_Line anEvaluator(myGeom2dLine);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theLine: nanoocp.Geom2d.Geom2d_Line) -> None:
        """
        Constructor with geometry.
        @param theLine the 2D line geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Line:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        For a line, D1 is constant (the direction vector).
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        For a line, D1 is constant and D2 is zero.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        For a line, D1 is constant, D2 and D3 are zero.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        For a line: D1 = Direction, DN = 0 for N > 1.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing),
        or empty array if geometry is null or no parameters
        """

class Geom2dGridEval_OffsetCurve:
    """
    @brief Batch evaluator for 2D offset curve grid points.

    Evaluates the 2D offset curve formula:
    P(u) = C(u) + Offset * N / ||N||
    where N = (D1.Y, -D1.X) is the normal (tangent rotated 90 degrees).

    Uses Geom2dGridEval_Curve for batch evaluation of the basis curve,
    then applies offset transformation.

    Usage:
    @code
    Geom2dGridEval_OffsetCurve anEvaluator(myGeom2dOffset);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theOffset: nanoocp.Geom2d.Geom2d_OffsetCurve) -> None:
        """
        Constructor with geometry.
        @param theOffset the 2D offset curve geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_OffsetCurve:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with derivatives up to third order.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses basis curve DN method.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class Geom2dGridEval_OtherCurve:
    """
    @brief Fallback evaluator for unknown 2D curve types.

    Uses Adaptor2d_Curve2d::D0 for point-by-point evaluation.
    This is the slowest evaluator but handles any 2D curve type.

    @note The curve adaptor reference must remain valid during the lifetime
    of this evaluator. The evaluator does not take ownership.

    Usage:
    @code
    Geom2dGridEval_OtherCurve anEvaluator(myCurveAdaptor2d);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """
        Constructor with curve adaptor reference.
        @param theCurve reference to 2D curve adaptor (must remain valid)
        """

    def Curve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Returns the curve adaptor reference."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing),
        or empty array if no parameters
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        For orders 1-3, reuses EvaluateGridD1/D2/D3.
        For orders > 3, uses adaptor DN method.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

class Geom2dGridEval_Parabola:
    """
    @brief Efficient batch evaluator for 2D parabola grid points.

    Uses analytical formula:
    P(u) = Center + (u^2 / (4*Focal)) * XDir + u * YDir

    Usage:
    @code
    Geom2dGridEval_Parabola anEvaluator(myGeom2dParabola);
    NCollection_Array1<gp_Pnt2d> aGrid = anEvaluator.EvaluateGrid(myParams);
    @endcode
    """

    def __init__(self, theParabola: nanoocp.Geom2d.Geom2d_Parabola) -> None:
        """
        Constructor with geometry.
        @param theParabola the 2D parabola geometry to evaluate
        """

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Parabola:
        """Returns the geometry handle."""

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate all grid points.
        @param theParams array of parameter values
        @return array of evaluated points (1-based indexing),
        or empty array if geometry is null or no parameters
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate all grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate all grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate all grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
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

class Geom2dGridEval_Curve:
    """
    @brief Unified grid evaluator for any 2D curve.

    Uses std::variant for compile-time type safety and zero heap allocation
    for the evaluator itself. Automatically detects curve type from
    Adaptor2d_Curve2d and dispatches to the appropriate specialized evaluator.

    Supported curve types with optimized evaluation:
    - Line: Direct analytical formula
    - Circle: Trigonometric formula
    - Ellipse: Analytical formula
    - Hyperbola: Analytical formula
    - Parabola: Analytical formula
    - BezierCurve: Optimized batch evaluation via BSplCLib
    - BSplineCurve: Optimized batch evaluation via BSplCLib with span caching
    - OffsetCurve: Composite evaluation using basis curve batch evaluator
    - Other: Fallback using Adaptor2d_Curve2d::D0

    Usage:
    @code
    Geom2dGridEval_Curve anEval(myAdaptorCurve2d);
    // OR
    Geom2dGridEval_Curve anEval(myGeom2dCurve);
    NCollection_Array1<gp_Pnt2d> aGrid = anEval.EvaluateGrid(myParams);
    @endcode
    """

    @overload
    def __init__(self, theCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """
        Construct from 2D adaptor reference (auto-detects curve type).
        For Geom2dAdaptor_Curve, extracts underlying Geom2d_Curve for optimized evaluation.
        For other adaptors, stores reference for fallback evaluation.
        @note The curve adaptor reference must remain valid during the lifetime
        of this evaluator when using fallback evaluation.
        @param[in] theCurve 2D curve adaptor reference to evaluate
        """

    @overload
    def __init__(self, theCurve: nanoocp.Geom2d.Geom2d_Curve) -> None:
        """
        Construct from geometry handle (auto-detects curve type).
        @param[in] theCurve 2D geometry to evaluate
        """

    def EvaluateGrid(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """
        Evaluate grid points at all parameters.
        @param theParams array of parameter values
        @return array of 2D points (1-based indexing)
        """

    def EvaluateGridD1(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD1]:
        """
        Evaluate grid points with first derivative.
        @param theParams array of parameter values
        @return array of CurveD1 (1-based indexing)
        """

    def EvaluateGridD2(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD2]:
        """
        Evaluate grid points with first and second derivatives.
        @param theParams array of parameter values
        @return array of CurveD2 (1-based indexing)
        """

    def EvaluateGridD3(self, theParams: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Geom2dGridEval.CurveD3]:
        """
        Evaluate grid points with first, second, and third derivatives.
        @param theParams array of parameter values
        @return array of CurveD3 (1-based indexing)
        """

    def EvaluateGridDN(self, theParams: nanoocp.NCollection.NCollection_Array1[float], theN: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d]:
        """
        Evaluate Nth derivative at all grid points.
        @param theParams array of parameter values
        @param theN derivative order (N >= 1)
        @return array of derivative vectors (1-based indexing)
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """Returns the detected curve type."""
