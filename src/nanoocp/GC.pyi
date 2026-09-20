"""OCCT package GC (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.gce
import nanoocp.gp


class GC_Root:
    """
    Provides common status services for GC builders
    reporting construction errors.
    """

    def __init__(self) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if the construction is successful."""

    def IsError(self) -> bool:
        """Returns true if the construction has failed."""

    def Status(self) -> nanoocp.gce.gce_ErrorType:
        """
        Returns the status of the construction:
        -   gce_Done, if the construction is successful, or
        -   another value of the gce_ErrorType enumeration
        indicating why the construction failed.
        """

class GC_MakeArcOfCircle(GC_Root):
    """
    Implements construction algorithms for an
    arc of circle in 3D space. The result is a Geom_TrimmedCurve curve.
    A MakeArcOfCircle object provides a framework for:
    -   defining the construction of the arc of circle,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the
    Value function returns the constructed arc of circle.
    """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates an arc of circle passing through three points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theP3 third point
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theV: nanoocp.gp.gp_Vec, theP2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates an arc of circle from two points and a tangent at the first point.
        @param[in] theP1 start point
        @param[in] theV tangent vector at start point
        @param[in] theP2 end point
        @note The tangent direction is given by the input vector.
        The orientation of the arc is:
        -   the sense determined by the order of the three input points;
        -   the sense defined by the input vector; or
        -   for the other constructors:
        -   the sense of the source circle if the orientation flag is true, or
        -   the opposite sense if `theSense` is false.
        @note Angles are expressed in radians.
        @note Construction fails with `gce_ConfusedPoints` if `theP1` and `theP2`
        are coincident.
        @note Construction fails with `gce_IntersectionError` if the supporting
        lines used to define circle center do not intersect.
        """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ, theAlpha1: float, theAlpha2: float, theSense: bool) -> None:
        """
        Creates an arc of circle from angular bounds.
        @param[in] theCirc source circle
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ, theP: nanoocp.gp.gp_Pnt, theAlpha: float, theSense: bool) -> None:
        """
        Creates an arc of circle from a point and an angular bound.
        @param[in] theCirc source circle
        @param[in] theP point on circle
        @param[in] theAlpha target angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theSense: bool) -> None:
        """
        Creates an arc of circle from two points on the circle.
        @param[in] theCirc source circle
        @param[in] theP1 first point on circle
        @param[in] theP2 second point on circle
        @param[in] theSense orientation of resulting arc
        """

    def Value(self) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the constructed arc of circle.
        Exceptions StdFail_NotDone if no arc of circle is constructed.
        @return resulting arc
        """

class GC_MakeArcOfCircle2d(GC_Root):
    """
    This class implements construction algorithms for arcs of circles in the plane.
    The result is a `Geom2d_TrimmedCurve`.
    A `GC_MakeArcOfCircle2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting arc via `Value()`.
    @note Angular parameters are expressed in radians.
    """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ2d, theAlpha1: float, theAlpha2: float, theSense: bool = True) -> None:
        """
        Constructs an arc from angular bounds on a circle.
        @param[in] theCircle source circle
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ2d, thePoint: nanoocp.gp.gp_Pnt2d, theAlpha: float, theSense: bool = True) -> None:
        """
        Constructs an arc from a point and angular bound on a circle.
        @param[in] theCircle source circle
        @param[in] thePoint point on source circle
        @param[in] theAlpha angle value (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ2d, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theSense: bool = True) -> None:
        """
        Constructs an arc between two points on a circle.
        @param[in] theCircle source circle
        @param[in] theP1 first point on source circle
        @param[in] theP2 second point on source circle
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theP3: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs an arc passing through three points.
        @param[in] theP1 first point
        @param[in] theP2 intermediate point
        @param[in] theP3 last point
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt2d, theV: nanoocp.gp.gp_Vec2d, theP2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs an arc from two points and tangent vector at start point.
        @param[in] theP1 start point
        @param[in] theV tangent vector at start point
        @param[in] theP2 end point
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """
        Returns the constructed arc of circle.
        Exceptions StdFail_NotDone if no arc of circle is constructed.
        @return resulting trimmed curve
        """

class GC_MakeArcOfEllipse(GC_Root):
    """
    Implements construction algorithms for ellipse arcs in 3D space.
    The result is a `Geom_TrimmedCurve`.
    A MakeArcOfEllipse object provides a framework for:
    -   defining the construction of the arc of ellipse,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the
    Value function returns the constructed arc of ellipse.
    """

    @overload
    def __init__(self, theElips: nanoocp.gp.gp_Elips, theAlpha1: float, theAlpha2: float, theSense: bool) -> None:
        """
        Constructs an arc from angular bounds on an ellipse.
        @param[in] theElips source ellipse
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theElips: nanoocp.gp.gp_Elips, theP: nanoocp.gp.gp_Pnt, theAlpha: float, theSense: bool) -> None:
        """
        Constructs an arc from a point and angle on an ellipse.
        @param[in] theElips source ellipse
        @param[in] theP point on ellipse
        @param[in] theAlpha target angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theElips: nanoocp.gp.gp_Elips, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theSense: bool) -> None:
        """
        Constructs an arc between two points on an ellipse.
        @param[in] theElips source ellipse
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theSense orientation of resulting arc
        @note The orientation of the arc of ellipse is:
        -   the orientation of ellipse if `theSense` is true, or
        -   the opposite orientation if `theSense` is false.
        @note Alpha1, Alpha2 and Alpha are angle values, given in radians.
        @note IsDone always returns true.
        """

    def Value(self) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the constructed arc of ellipse.
        @return resulting arc
        """

class GC_MakeArcOfEllipse2d(GC_Root):
    """
    This class implements construction algorithms for arcs of ellipses in the plane.
    The result is a `Geom2d_TrimmedCurve`.
    A `GC_MakeArcOfEllipse2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting arc via `Value()`.
    @note Angular parameters are expressed in radians.
    """

    @overload
    def __init__(self, theEllipse: nanoocp.gp.gp_Elips2d, theAlpha1: float, theAlpha2: float, theSense: bool = True) -> None:
        """
        Constructs an arc from angular bounds on an ellipse.
        @param[in] theEllipse source ellipse
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theEllipse: nanoocp.gp.gp_Elips2d, thePoint: nanoocp.gp.gp_Pnt2d, theAlpha: float, theSense: bool = True) -> None:
        """
        Constructs an arc from a point and angular bound on an ellipse.
        @param[in] theEllipse source ellipse
        @param[in] thePoint point on source ellipse
        @param[in] theAlpha angle value (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theEllipse: nanoocp.gp.gp_Elips2d, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theSense: bool = True) -> None:
        """
        Constructs an arc between two points on an ellipse.
        @param[in] theEllipse source ellipse
        @param[in] theP1 first point on source ellipse
        @param[in] theP2 second point on source ellipse
        @param[in] theSense orientation of resulting arc
        @note Orientation is trigonometric when `theSense` is true,
        otherwise opposite.
        @note IsDone always returns true.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """
        Returns the constructed arc of ellipse.
        @return resulting trimmed curve
        """

class GC_MakeArcOfHyperbola(GC_Root):
    """
    Implements construction algorithms for hyperbola arcs in 3D space.
    The result is a `Geom_TrimmedCurve`.
    A MakeArcOfHyperbola object provides a framework for:
    -   defining the construction of the arc of hyperbola,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the
    Value function returns the constructed arc of hyperbola.
    """

    @overload
    def __init__(self, theHypr: nanoocp.gp.gp_Hypr, theAlpha1: float, theAlpha2: float, theSense: bool) -> None:
        """
        Constructs an arc from angular bounds on a hyperbola.
        @param[in] theHypr source hyperbola
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theHypr: nanoocp.gp.gp_Hypr, theP: nanoocp.gp.gp_Pnt, theAlpha: float, theSense: bool) -> None:
        """
        Constructs an arc from a point and angle on a hyperbola.
        @param[in] theHypr source hyperbola
        @param[in] theP point on hyperbola
        @param[in] theAlpha target angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theHypr: nanoocp.gp.gp_Hypr, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theSense: bool) -> None:
        """
        Constructs an arc between two points on a hyperbola.
        @param[in] theHypr source hyperbola
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theSense orientation of resulting arc
        @note The orientation of the arc of hyperbola is:
        -   the orientation of hyperbola if `theSense` is true, or
        -   the opposite orientation if `theSense` is false.
        """

    def Value(self) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the constructed arc of hyperbola.
        @return resulting arc
        """

class GC_MakeArcOfHyperbola2d(GC_Root):
    """
    This class implements construction algorithms for arcs of hyperbolas in the plane.
    The result is a `Geom2d_TrimmedCurve`.
    A `GC_MakeArcOfHyperbola2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting arc via `Value()`.
    @note Angular parameters are expressed in radians.
    """

    @overload
    def __init__(self, theHyperbola: nanoocp.gp.gp_Hypr2d, theAlpha1: float, theAlpha2: float, theSense: bool = True) -> None:
        """
        Constructs an arc from angular bounds on a hyperbola.
        @param[in] theHyperbola source hyperbola
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theHyperbola: nanoocp.gp.gp_Hypr2d, thePoint: nanoocp.gp.gp_Pnt2d, theAlpha: float, theSense: bool = True) -> None:
        """
        Constructs an arc from a point and angular bound on a hyperbola.
        @param[in] theHyperbola source hyperbola
        @param[in] thePoint point on source hyperbola
        @param[in] theAlpha angle value (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theHyperbola: nanoocp.gp.gp_Hypr2d, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theSense: bool = True) -> None:
        """
        Constructs an arc between two points on a hyperbola.
        @param[in] theHyperbola source hyperbola
        @param[in] theP1 first point on source hyperbola
        @param[in] theP2 second point on source hyperbola
        @param[in] theSense orientation of resulting arc
        @note Orientation is trigonometric when `theSense` is true,
        otherwise opposite.
        @note IsDone always returns true.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """
        Returns the constructed arc of hyperbola.
        @return resulting trimmed curve
        """

class GC_MakeArcOfParabola(GC_Root):
    """
    Implements construction algorithms for parabola arcs in 3D space.
    The result is a `Geom_TrimmedCurve`.
    A MakeArcOfParabola object provides a framework for:
    -   defining the construction of the arc of parabola,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the
    Value function returns the constructed arc of parabola.
    """

    @overload
    def __init__(self, theParab: nanoocp.gp.gp_Parab, theAlpha1: float, theAlpha2: float, theSense: bool) -> None:
        """
        Constructs an arc from angular bounds on a parabola.
        @param[in] theParab source parabola
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theParab: nanoocp.gp.gp_Parab, theP: nanoocp.gp.gp_Pnt, theAlpha: float, theSense: bool) -> None:
        """
        Constructs an arc from a point and angle on a parabola.
        @param[in] theParab source parabola
        @param[in] theP point on parabola
        @param[in] theAlpha target angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theParab: nanoocp.gp.gp_Parab, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theSense: bool) -> None:
        """
        Constructs an arc between two points on a parabola.
        @param[in] theParab source parabola
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theSense orientation of resulting arc
        """

    def Value(self) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the constructed arc of parabola.
        @return resulting arc
        """

class GC_MakeArcOfParabola2d(GC_Root):
    """
    This class implements construction algorithms for arcs of parabolas in the plane.
    The result is a `Geom2d_TrimmedCurve`.
    A `GC_MakeArcOfParabola2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting arc via `Value()`.
    @note Angular parameters are expressed in radians.
    """

    @overload
    def __init__(self, theParabola: nanoocp.gp.gp_Parab2d, theAlpha1: float, theAlpha2: float, theSense: bool = True) -> None:
        """
        Constructs an arc from angular bounds on a parabola.
        @param[in] theParabola source parabola
        @param[in] theAlpha1 first angle (radians)
        @param[in] theAlpha2 second angle (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theParabola: nanoocp.gp.gp_Parab2d, thePoint: nanoocp.gp.gp_Pnt2d, theAlpha: float, theSense: bool = True) -> None:
        """
        Constructs an arc from a point and angular bound on a parabola.
        @param[in] theParabola source parabola
        @param[in] thePoint point on source parabola
        @param[in] theAlpha angle value (radians)
        @param[in] theSense orientation of resulting arc
        """

    @overload
    def __init__(self, theParabola: nanoocp.gp.gp_Parab2d, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theSense: bool = True) -> None:
        """
        Constructs an arc between two points on a parabola.
        @param[in] theParabola source parabola
        @param[in] theP1 first point on source parabola
        @param[in] theP2 second point on source parabola
        @param[in] theSense orientation of resulting arc
        @note Orientation is trigonometric when `theSense` is true,
        otherwise opposite.
        @note IsDone always returns true.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """
        Returns the constructed arc of parabola.
        @return resulting trimmed curve
        """

class GC_MakeCircle(GC_Root):
    """
    Implements construction algorithms for circles in 3D space.

    * Create a circle parallel to another and passing
    through a point.
    * Create a Circle parallel to another at the distance
    Dist.
    * Create a Circle passing through 3 points.
    * Create a Circle with its center and the normal of its
    plane and its radius.
    * Create a Circle with its axis and radius.
    The circle parameter is the angle in radians.
    The parametrization range is [0,2*PI].
    The circle is a closed and periodic curve.
    The center of the circle is the Location point of its axis
    placement. The XDirection of the axis placement defines the
    origin of the parametrization.
    """

    @overload
    def __init__(self, theC: nanoocp.gp.gp_Circ) -> None:
        """
        Creates a circle from a `gp_Circ`.
        @param[in] theC source circle
        """

    @overload
    def __init__(self, theA2: nanoocp.gp.gp_Ax2, theRadius: float) -> None:
        """
        Creates a circle from axis placement and radius.
        @param[in] theA2 local coordinate system of the circle
        @param[in] theRadius circle radius
        @note Radius equal to `0.0` is allowed.
        @note The status is `gce_NegativeRadius` if `theRadius < 0.0`.
        """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ, theDist: float) -> None:
        """
        Creates a circle concentric to the input circle with an offset radius.
        @param[in] theCirc reference circle
        @param[in] theDist radius offset
        """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a circle concentric to the input circle and passing through the input point.
        @param[in] theCirc source circle
        @param[in] thePoint point on resulting circle
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax1, theRadius: float) -> None:
        """
        Creates a circle from axis and radius.
        @param[in] theAxis circle axis
        @param[in] theRadius circle radius
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a circle passing through three points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theP3 third point
        """

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_Pnt, theNorm: nanoocp.gp.gp_Dir, theRadius: float) -> None:
        """
        Creates a circle from center point, normal and radius.
        @param[in] theCenter circle center
        @param[in] theNorm normal direction of circle plane
        @param[in] theRadius circle radius
        """

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_Pnt, thePtAxis: nanoocp.gp.gp_Pnt, theRadius: float) -> None:
        """
        Creates a circle from center point, axis point and radius.
        @param[in] theCenter circle center
        @param[in] thePtAxis point defining normal direction
        @param[in] theRadius circle radius
        @note The direction is defined by vector (`theCenter`,`thePtAxis`).
        """

    def Value(self) -> nanoocp.Geom.Geom_Circle:
        """
        Returns the constructed circle.
        Exceptions
        StdFail_NotDone if no circle is constructed.
        @return resulting circle
        """

class GC_MakeCircle2d(GC_Root):
    """
    This class implements construction algorithms for circles in the plane.
    The result is a `Geom2d_Circle`.
    A `GC_MakeCircle2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting circle via `Value()`.
    @note A circle is parameterized in the range [0, 2*PI], and the X axis
    of its local coordinate system defines the parameter origin.
    """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ2d) -> None:
        """
        Creates a circle from a non-persistent one from package gp.
        @param[in] theCircle source circle
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax2d, theRadius: float, theSense: bool = True) -> None:
        """
        Creates a circle from an axis placement and radius.
        @param[in] theAxis axis placement
        @param[in] theRadius radius value
        @param[in] theSense orientation flag
        @note Construction fails with `gce_NegativeRadius` if `theRadius` is negative.
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax22d, theRadius: float) -> None:
        """
        Creates a circle from a local coordinate system and radius.
        @param[in] theAxis local coordinate system
        @param[in] theRadius radius value
        @note Construction fails with `gce_NegativeRadius` if `theRadius` is negative.
        """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ2d, theDist: float) -> None:
        """
        Creates a circle parallel to another one at signed distance.
        @param[in] theCircle source circle
        @param[in] theDist signed distance
        @note If `theDist` is positive, the resulting circle encloses `theCircle`.
        @note If `theDist` is negative, the resulting circle is enclosed by `theCircle`.
        @note Error status is provided by the underlying `gce_MakeCirc2d`.
        """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ2d, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a circle parallel to another one and passing through a point.
        @param[in] theCircle source circle
        @param[in] thePoint point on resulting circle
        @note Error status is provided by the underlying `gce_MakeCirc2d`.
        """

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_Pnt2d, theRadius: float, theSense: bool = True) -> None:
        """
        Creates a circle from center point and radius.
        @param[in] theCenter center point
        @param[in] theRadius radius value
        @param[in] theSense orientation flag
        @note Error status is provided by the underlying `gce_MakeCirc2d`.
        """

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_Pnt2d, thePoint: nanoocp.gp.gp_Pnt2d, theSense: bool = True) -> None:
        """
        Creates a circle from center point and one point on the circle.
        @param[in] theCenter center point
        @param[in] thePoint point on resulting circle
        @param[in] theSense orientation flag
        @note Error status is provided by the underlying `gce_MakeCirc2d`.
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d, theP3: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a circle passing through three points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theP3 third point
        @note Error status is provided by the underlying `gce_MakeCirc2d`.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Circle:
        """
        Returns the constructed circle.
        Exceptions StdFail_NotDone if no circle is constructed.
        @return resulting circle
        """

class GC_MakeConicalSurface(GC_Root):
    """
    Implements construction algorithms for conical surfaces.
    Supported constructions include:
    - a conical surface from axis placement and angle/radius;
    - conversion from `gp_Cone`;
    - a conical surface through four points;
    - a conical surface from two points and two radii.
    The local coordinate system of the ConicalSurface is defined
    with an axis placement (see class ElementarySurface).

    The "ZAxis" is the symmetry axis of the ConicalSurface,
    it gives the direction of increasing parametric value V.
    The apex of the surface is on the negative side of this axis.

    The parametrization range is:
    U [0, 2*PI], V ]-infinite, + infinite[

    The "XAxis" and the "YAxis" define the placement plane of the
    surface (Z = 0, and parametric value V = 0) perpendicular to
    the symmetry axis. The "XAxis" defines the origin of the
    parameter U = 0. The trigonometric sense gives the positive
    orientation for the parameter U.

    When you create a ConicalSurface the U and V directions of
    parametrization are such that at each point of the surface the
    normal is oriented towards the "outside region".
    """

    @overload
    def __init__(self, theC: nanoocp.gp.gp_Cone) -> None:
        """
        Creates a conical surface from a `gp_Cone`.
        @param[in] theC source cone
        """

    @overload
    def __init__(self, theA2: nanoocp.gp.gp_Ax2, theAng: float, theRadius: float) -> None:
        """
        Creates a conical surface from local frame, semi-angle and radius.
        @param[in] theA2 local coordinate system
        @param[in] theAng semi-angle
        @param[in] theRadius reference radius in placement plane
        @note `theA2` defines the local coordinate system of the conical surface.
        @note `theAng` is the conical surface semi-angle ]0, PI/2[.
        @note `theRadius` is the radius of the circle Viso in the placement plane
        of the conical surface defined with "XAxis" and "YAxis".
        @note The "ZDirection" of `theA2` defines the direction of the surface axis
        of symmetry.
        @note If the location point of `theA2` is the apex of the surface,
        `theRadius` is zero.
        @note The created surface is parametrized such that the normal vector
        (`N = D1U ^ D1V`) is oriented towards the "outside region".
        @note Status is `gce_NegativeRadius` if `theRadius < 0.0`, or
        `gce_BadAngle` if `theAng` is outside valid range.
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt, theP4: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a conical surface from four points.
        @param[in] theP1 first point defining axis
        @param[in] theP2 second point defining axis
        @param[in] theP3 point defining first section radius
        @param[in] theP4 point defining second section radius
        @note Axis is defined by points `theP1` and `theP2`, and base radius is
        the distance between point `theP3` and that axis.
        @note The distance between point `theP4` and that axis is the radius of
        the section passing through P4.
        @note Construction fails if points `theP1`, `theP2`, `theP3` and `theP4` are
        collinear, or if vector (`theP3`,`theP4`) is perpendicular/collinear
        to vector (`theP1`,`theP2`).
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theR1: float, theR2: float) -> None:
        """
        Creates a conical surface with two points and two radii.
        @param[in] theP1 first axis point
        @param[in] theP2 second axis point
        @param[in] theR1 radius at P1
        @param[in] theR2 radius at P2
        @note The axis of the solution is the line passing through `theP1` and `theP2`.
        @note `theR1` and `theR2` are radii of sections passing through
        `theP1` and `theP2`.
        """

    def Value(self) -> nanoocp.Geom.Geom_ConicalSurface:
        """
        Returns the constructed cone.
        Exceptions
        StdFail_NotDone if no cone is constructed.
        @return resulting conical surface
        """

class GC_MakeCylindricalSurface(GC_Root):
    """
    Implements construction algorithms for cylindrical surfaces.
    Supported constructions include:
    - a cylindrical surface from axis placement and radius;
    - conversion from `gp_Cylinder`;
    - an offset/parallel cylindrical surface;
    - a cylindrical surface through three points;
    - a cylindrical surface from axis and radius;
    - a cylindrical surface from circular base.
    The local coordinate system of the CylindricalSurface is defined
    with an axis placement (see class ElementarySurface).

    The "ZAxis" is the symmetry axis of the CylindricalSurface,
    it gives the direction of increasing parametric value V.

    The parametrization range is :
    U [0, 2*PI], V ]- infinite, + infinite[

    The "XAxis" and the "YAxis" define the placement plane of the
    surface (Z = 0, and parametric value V = 0) perpendicular to
    the symmetry axis. The "XAxis" defines the origin of the
    parameter U = 0. The trigonometric sense gives the positive
    orientation for the parameter U.
    """

    @overload
    def __init__(self, theC: nanoocp.gp.gp_Cylinder) -> None:
        """
        Creates a cylindrical surface from a `gp_Cylinder`.
        @param[in] theC source cylinder
        """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ) -> None:
        """
        Creates a cylindrical surface from its circular base.
        @param[in] theCirc base circle
        """

    @overload
    def __init__(self, theA2: nanoocp.gp.gp_Ax2, theRadius: float) -> None:
        """
        Creates a cylindrical surface from axis placement and radius.
        @param[in] theA2 local coordinate system
        @param[in] theRadius cylinder radius
        @note `theA2` defines the local coordinate system of the cylindrical surface.
        @note The "ZDirection" of `theA2` defines the direction of the surface axis
        of symmetry.
        @note The created surface is parametrized such that the normal vector
        (`N = D1U ^ D1V`) is oriented towards the "outside region".
        @note It is valid to create a cylindrical surface with `theRadius = 0.0`.
        @note Status is `gce_NegativeRadius` if `theRadius < 0.0`.
        """

    @overload
    def __init__(self, theCyl: nanoocp.gp.gp_Cylinder, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cylindrical surface parallel to the input cylinder and passing through the input
        point.
        @param[in] theCyl source cylinder
        @param[in] thePoint point on resulting surface
        """

    @overload
    def __init__(self, theCyl: nanoocp.gp.gp_Cylinder, theDist: float) -> None:
        """
        Creates a cylindrical surface parallel to the input cylinder at signed distance.
        @param[in] theCyl source cylinder
        @param[in] theDist signed offset distance
        @note The result radius is the absolute value of
        (source radius + signed distance).
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax1, theRadius: float) -> None:
        """
        Creates a cylindrical surface from axis and radius.
        @param[in] theAxis cylinder axis
        @param[in] theRadius cylinder radius
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cylindrical surface passing through three points.
        @param[in] theP1 first axis point
        @param[in] theP2 second axis point
        @param[in] theP3 point defining radius
        @note The axis is defined by points `theP1` and `theP2`, and radius is the
        distance between point `theP3` and that axis.
        """

    def Value(self) -> nanoocp.Geom.Geom_CylindricalSurface:
        """
        Returns the constructed cylinder.
        Exceptions StdFail_NotDone if no cylinder is constructed.
        @return resulting cylindrical surface
        """

class GC_MakeEllipse(GC_Root):
    """
    Implements construction algorithms for ellipses in 3D space.
    The result is a `Geom_Ellipse`.
    A MakeEllipse object provides a framework for:
    -   defining the construction of the ellipse,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the Value
    function returns the constructed ellipse.
    """

    @overload
    def __init__(self, theE: nanoocp.gp.gp_Elips) -> None:
        """
        Creates an ellipse from a `gp_Elips`.
        @param[in] theE source ellipse
        """

    @overload
    def __init__(self, theA2: nanoocp.gp.gp_Ax2, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        Constructs an ellipse with major and minor radii MajorRadius and
        MinorRadius, and located in the plane defined by
        the "X Axis" and "Y Axis" of the coordinate system A2, where:
        -   its center is the origin of A2, and
        -   its major axis is the "X Axis" of A2;
        @note Construction with `theMajorRadius == theMinorRadius` is allowed.
        @note Construction fails with `gce_NegativeRadius` if `theMinorRadius < 0.0`.
        @note Construction fails with `gce_InvertAxis` if
        `theMajorRadius < theMinorRadius`.
        @param[in] theA2 ellipse local coordinate system
        @param[in] theMajorRadius major radius
        @param[in] theMinorRadius minor radius
        """

    @overload
    def __init__(self, theS1: nanoocp.gp.gp_Pnt, theS2: nanoocp.gp.gp_Pnt, theCenter: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs an ellipse centered on the point Center, where
        -   the plane of the ellipse is defined by Center, S1 and S2,
        -   its major axis is defined by Center and S1,
        -   its major radius is the distance between Center and S1, and
        -   its minor radius is the distance between S2 and the major axis.
        @param[in] theS1 point defining the major axis
        @param[in] theS2 point defining the minor radius
        @param[in] theCenter ellipse center
        """

    def Value(self) -> nanoocp.Geom.Geom_Ellipse:
        """
        Returns the constructed ellipse.
        Exceptions StdFail_NotDone if no ellipse is constructed.
        @return resulting ellipse
        """

class GC_MakeEllipse2d(GC_Root):
    """
    This class implements construction algorithms for ellipses in the plane.
    The result is a `Geom2d_Ellipse`.
    A `GC_MakeEllipse2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting ellipse via `Value()`.
    @note Ellipse parameterization range is [0, 2*PI].
    @note The X axis of the local coordinate system is the major axis,
    and the Y axis is the minor axis.
    """

    @overload
    def __init__(self, theEllipse: nanoocp.gp.gp_Elips2d) -> None:
        """
        Creates an ellipse from a non-persistent one from package gp.
        @param[in] theEllipse source ellipse
        """

    @overload
    def __init__(self, theMajorAxis: nanoocp.gp.gp_Ax2d, theMajorRadius: float, theMinorRadius: float, theSense: bool = True) -> None:
        """
        Creates an ellipse from major axis placement and radii.
        @param[in] theMajorAxis major axis placement
        @param[in] theMajorRadius major radius value
        @param[in] theMinorRadius minor radius value
        @param[in] theSense orientation flag
        @note Error status is provided by the underlying `gce_MakeElips2d`
        (for example `gce_InvertRadius` or `gce_NegativeRadius`).
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax22d, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        Creates an ellipse from a local coordinate system and radii.
        @param[in] theAxis local coordinate system
        @param[in] theMajorRadius major radius value
        @param[in] theMinorRadius minor radius value
        @note Error status is provided by the underlying `gce_MakeElips2d`
        (for example `gce_InvertRadius` or `gce_NegativeRadius`).
        """

    @overload
    def __init__(self, theS1: nanoocp.gp.gp_Pnt2d, theS2: nanoocp.gp.gp_Pnt2d, theCenter: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates an ellipse from two apex points and center point.
        @param[in] theS1 first apex point
        @param[in] theS2 second point defining minor radius
        @param[in] theCenter center point
        @note Error status is provided by the underlying `gce_MakeElips2d`.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Ellipse:
        """
        Returns the constructed ellipse.
        Exceptions StdFail_NotDone if no ellipse is constructed.
        @return resulting ellipse
        """

class GC_MakeHyperbola(GC_Root):
    """
    Implements construction algorithms for hyperbolas in 3D space.
    The result is a `Geom_Hyperbola`.
    A MakeHyperbola object provides a framework for:
    -   defining the construction of the hyperbola,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the Value
    function returns the constructed hyperbola.
    To define the main branch of a hyperbola.
    The parameterization range is ]-infinite,+infinite[
    It is possible to get the other branch and the two conjugate
    branches of the main branch.

    ^YAxis
    |
    FirstConjugateBranch
    |
    Other            |                Main
    --------------------- C ------------------------------>XAxis
    Branch           |                Branch
    |
    SecondConjugateBranch
    |

    The major radius is the distance between the Location point
    of the hyperbola C and the apex of the Main Branch (or the
    Other branch). The major axis is the XAxis.
    The minor radius is the distance between the Location point
    of the hyperbola C and the apex of the First (or Second)
    Conjugate branch. The minor axis is the YAxis.
    The major radius can be lower than the minor radius.
    """

    @overload
    def __init__(self, theH: nanoocp.gp.gp_Hypr) -> None:
        """
        Creates a hyperbola from a `gp_Hypr`.
        @param[in] theH source hyperbola
        """

    @overload
    def __init__(self, theA2: nanoocp.gp.gp_Ax2, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        Constructs a hyperbola centered on the origin of the coordinate system
        A2, with major and minor radii MajorRadius and MinorRadius, where:
        the plane of the hyperbola is defined by the "X Axis" and "Y Axis" of A2,
        -   its major axis is the "X Axis" of A2.
        @param[in] theA2 hyperbola local coordinate system
        @param[in] theMajorRadius major radius
        @param[in] theMinorRadius minor radius
        """

    @overload
    def __init__(self, theS1: nanoocp.gp.gp_Pnt, theS2: nanoocp.gp.gp_Pnt, theCenter: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a hyperbola centered on the point Center, where
        -   the plane of the hyperbola is defined by Center, S1 and S2,
        -   its major axis is defined by Center and S1,
        -   its major radius is the distance between Center and S1, and
        -   its minor radius is the distance between S2 and the major axis;
        @param[in] theS1 point defining the major axis
        @param[in] theS2 point defining the minor radius
        @param[in] theCenter hyperbola center
        """

    def Value(self) -> nanoocp.Geom.Geom_Hyperbola:
        """
        Returns the constructed hyperbola.
        Exceptions StdFail_NotDone if no hyperbola is constructed.
        @return resulting hyperbola
        """

class GC_MakeHyperbola2d(GC_Root):
    """
    This class implements construction algorithms for hyperbolas in the plane.
    The result is a `Geom2d_Hyperbola` (main branch).
    A `GC_MakeHyperbola2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting hyperbola via `Value()`.
    @note Hyperbola parameterization range is ]-infinite, +infinite[.
    @note In the local coordinate system, the X axis is the major axis
    and the Y axis is the minor axis.
    """

    @overload
    def __init__(self, theHyperbola: nanoocp.gp.gp_Hypr2d) -> None:
        """
        Creates a hyperbola from a non-persistent one from package gp.
        @param[in] theHyperbola source hyperbola
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax22d, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        Creates a hyperbola from local coordinate system and radii.
        @param[in] theAxis local coordinate system
        @param[in] theMajorRadius major radius value
        @param[in] theMinorRadius minor radius value
        @note Error status is provided by the underlying `gce_MakeHypr2d`
        (for example `gce_NegativeRadius`).
        """

    @overload
    def __init__(self, theS1: nanoocp.gp.gp_Pnt2d, theS2: nanoocp.gp.gp_Pnt2d, theCenter: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a hyperbola from two apex points and center point.
        @param[in] theS1 first apex point
        @param[in] theS2 second point defining conjugate radius
        @param[in] theCenter center point
        @note Error status is provided by the underlying `gce_MakeHypr2d`
        (for example `gce_ConfusedPoints` or `gce_ColinearPoints`).
        """

    @overload
    def __init__(self, theMajorAxis: nanoocp.gp.gp_Ax2d, theMajorRadius: float, theMinorRadius: float, theSense: bool) -> None:
        """
        Creates a hyperbola from major axis placement and radii.
        @param[in] theMajorAxis major axis placement
        @param[in] theMajorRadius major radius value
        @param[in] theMinorRadius minor radius value
        @param[in] theSense orientation flag
        @note Error status is provided by the underlying `gce_MakeHypr2d`
        (for example `gce_NegativeRadius`).
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Hyperbola:
        """
        Returns the constructed hyperbola.
        Exceptions: StdFail_NotDone if no hyperbola is constructed.
        @return resulting hyperbola
        """

class GC_MakeLine(GC_Root):
    """
    This class implements the following algorithms used
    to create a Line from Geom.
    * Create a Line parallel to another and passing
    through a point.
    * Create a Line passing through 2 points.
    A MakeLine object provides a framework for:
    -   defining the construction of the line,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the Value
    function returns the constructed line.
    """

    @overload
    def __init__(self, theA1: nanoocp.gp.gp_Ax1) -> None:
        """
        Creates a line located in 3D space with the axis placement A1.
        @param[in] theA1 line axis placement
        @note The location of `theA1` is the origin of the line.
        """

    @overload
    def __init__(self, theL: nanoocp.gp.gp_Lin) -> None:
        """
        Creates a line from a non-persistent line from package gp.
        @param[in] theL source line
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theV: nanoocp.gp.gp_Dir) -> None:
        """
        Creates a line from point and direction.
        @param[in] theP line origin
        @param[in] theV line direction
        """

    @overload
    def __init__(self, theLin: nanoocp.gp.gp_Lin, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a line parallel to the input line and passing through the input point.
        @param[in] theLin source line
        @param[in] thePoint point on resulting line
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a line passing through two points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @note Construction fails with `gce_ConfusedPoints` if the two points are coincident.
        """

    def Value(self) -> nanoocp.Geom.Geom_Line:
        """
        Returns the constructed line.
        Exceptions StdFail_NotDone if no line is constructed.
        @return resulting line
        """

class GC_MakeLine2d(GC_Root):
    """
    This class implements construction algorithms for lines in the plane.
    The result is a `Geom2d_Line`.
    A `GC_MakeLine2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting line via `Value()`.
    Supported constructions include:
    - line from axis placement;
    - line from existing `gp_Lin2d`;
    - line from point and direction;
    - line parallel to input line through a point;
    - line parallel to input line at signed distance;
    - line through two points.
    """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax2d) -> None:
        """
        Creates a line from an axis placement.
        @param[in] theAxis axis placement
        @note The location of `theAxis` is the line origin.
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d) -> None:
        """
        Creates a line from a non-persistent line from package gp.
        @param[in] theLine source line
        """

    @overload
    def __init__(self, thePoint: nanoocp.gp.gp_Pnt2d, theDir: nanoocp.gp.gp_Dir2d) -> None:
        """
        Constructs a line from origin and direction.
        @param[in] thePoint point on line
        @param[in] theDir direction
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a line parallel to input line and passing through a point.
        @param[in] theLine source line
        @param[in] thePoint point on resulting line
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d, theDist: float) -> None:
        """
        Constructs a line parallel to input line at signed distance.
        @param[in] theLine source line
        @param[in] theDist signed distance
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a line passing through two points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @note Status is `gce_ConfusedPoints` if points are coincident.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Line:
        """
        Returns the constructed line.
        Exceptions StdFail_NotDone if no line is constructed.
        @return resulting line
        """

class GC_MakeMirror:
    """
    This class implements elementary construction algorithms for a
    symmetrical transformation in 3D space about a point,
    axis or plane. The result is a Geom_Transformation transformation.
    A MakeMirror object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a central symmetry about a point.
        @param[in] thePoint center point
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax1) -> None:
        """
        Constructs an axial symmetry about an axis.
        @param[in] theAxis mirror axis
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin) -> None:
        """
        Constructs an axial symmetry about a line.
        @param[in] theLine mirror line
        """

    @overload
    def __init__(self, thePlane: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def __init__(self, thePlane: nanoocp.gp.gp_Ax2) -> None:
        """
        Constructs a planar symmetry about a plane.
        @param[in] thePlane mirror plane
        """

    @overload
    def __init__(self, thePoint: nanoocp.gp.gp_Pnt, theDirec: nanoocp.gp.gp_Dir) -> None:
        """
        Constructs an axial symmetry about an axis defined by point and direction.
        @param[in] thePoint point on the axis
        @param[in] theDirec axis direction
        """

    def Value(self) -> nanoocp.Geom.Geom_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeMirror2d:
    """
    This class implements elementary construction algorithms for
    symmetric transformations in 2D space about a point, axis, or line.
    The result is a `Geom2d_Transformation`.
    A `GC_MakeMirror2d` object provides a framework for:
    - defining the transformation parameters;
    - running the construction algorithm;
    - querying the resulting transformation via `Value()`.
    """

    @overload
    def __init__(self, thePoint: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a central symmetry about a point.
        @param[in] thePoint center point
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax2d) -> None:
        """
        Constructs an axial symmetry about an axis.
        @param[in] theAxis symmetry axis
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d) -> None:
        """
        Constructs an axial symmetry about a line.
        @param[in] theLine symmetry line
        """

    @overload
    def __init__(self, thePoint: nanoocp.gp.gp_Pnt2d, theDirec: nanoocp.gp.gp_Dir2d) -> None:
        """
        Constructs an axial symmetry about a line defined by point and direction.
        @param[in] thePoint point on symmetry axis
        @param[in] theDirec symmetry direction
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakePlane(GC_Root):
    """
    Implements construction algorithms for planes in 3D space.
    Supported constructions include:
    - a plane parallel to another plane and passing through a point;
    - a plane passing through three points;
    - a plane defined by a point and normal direction.
    A MakePlane object provides a framework for:
    -   defining the construction of the plane,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the Value
    function returns the constructed plane.
    """

    @overload
    def __init__(self, thePl: nanoocp.gp.gp_Pln) -> None:
        """
        Creates a plane from a non-persistent plane from package gp.
        @param[in] thePl source plane
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax1) -> None:
        """
        Creates a plane through axis location and normal to axis direction.
        @param[in] theAxis axis defining location and normal
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theV: nanoocp.gp.gp_Dir) -> None:
        """
        Creates a plane from point and normal direction.
        @param[in] theP location point of the plane
        @param[in] theV normal direction
        """

    @overload
    def __init__(self, thePln: nanoocp.gp.gp_Pln, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a plane parallel to the input plane and passing through the input point.
        @param[in] thePln source plane
        @param[in] thePoint point on resulting plane
        """

    @overload
    def __init__(self, thePln: nanoocp.gp.gp_Pln, theDist: float) -> None:
        """
        Creates a plane parallel to the input plane at signed distance.
        @param[in] thePln source plane
        @param[in] theDist signed distance
        @note Positive distance follows the normal of the input plane.
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a plane passing through three points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @param[in] theP3 third point
        @note Construction fails when points are confused/collinear.
        """

    @overload
    def __init__(self, theA: float, theB: float, theC: float, theD: float) -> None:
        """
        Creates a plane from its cartesian equation:
        `A * x + B * y + C * z + D = 0.0`.
        @param[in] theA equation coefficient A
        @param[in] theB equation coefficient B
        @param[in] theC equation coefficient C
        @param[in] theD equation coefficient D
        @note Status is `gce_BadEquation` if `sqrt(theA*theA + theB*theB + theC*theC)`
        is below gp resolution.
        """

    def Value(self) -> nanoocp.Geom.Geom_Plane:
        """
        Returns the constructed plane.
        Exceptions StdFail_NotDone if no plane is constructed.
        @return resulting plane
        """

class GC_MakeRotation:
    """
    This class implements elementary construction algorithms for a
    rotation in 3D space. The result is a
    Geom_Transformation transformation.
    A MakeRotation object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin, theAngle: float) -> None:
        """
        Constructs a rotation around the axis defined by a line.
        @param[in] theLine rotation axis
        @param[in] theAngle rotation angle in radians
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax1, theAngle: float) -> None:
        """
        Constructs a rotation around an axis.
        @param[in] theAxis rotation axis
        @param[in] theAngle rotation angle in radians
        """

    @overload
    def __init__(self, thePoint: nanoocp.gp.gp_Pnt, theDirec: nanoocp.gp.gp_Dir, theAngle: float) -> None:
        """
        Constructs a rotation around an axis defined by point and direction.
        @param[in] thePoint point on the axis
        @param[in] theDirec axis direction
        @param[in] theAngle rotation angle in radians
        """

    def Value(self) -> nanoocp.Geom.Geom_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeRotation2d:
    """
    This class implements elementary construction algorithms for
    rotations in 2D space.
    The result is a `Geom2d_Transformation`.
    A `GC_MakeRotation2d` object provides a framework for:
    - defining the transformation parameters;
    - running the construction algorithm;
    - querying the resulting transformation via `Value()`.
    """

    def __init__(self, thePoint: nanoocp.gp.gp_Pnt2d, theAngle: float) -> None:
        """
        Constructs a rotation through angle Angle about the center Point.
        @param[in] thePoint rotation center
        @param[in] theAngle rotation angle in radians
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeScale:
    """
    Implements construction of a scaling transformation in 3D space.
    The result is a `Geom_Transformation` centered at `Point`
    with scale factor `Scale`.
    A MakeScale object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    def __init__(self, thePoint: nanoocp.gp.gp_Pnt, theScale: float) -> None:
        """
        Constructs a scaling transformation.
        @param[in] thePoint center point of scaling
        @param[in] theScale scale factor
        """

    def Value(self) -> nanoocp.Geom.Geom_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeScale2d:
    """
    This class implements elementary construction algorithms for
    scaling transformations in 2D space.
    The result is a `Geom2d_Transformation`.
    A `GC_MakeScale2d` object provides a framework for:
    - defining the transformation parameters;
    - running the construction algorithm;
    - querying the resulting transformation via `Value()`.
    """

    def __init__(self, thePoint: nanoocp.gp.gp_Pnt2d, theScale: float) -> None:
        """
        Constructs a scaling transformation.
        @param[in] thePoint center point
        @param[in] theScale scale factor
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeSegment(GC_Root):
    """
    Implements construction algorithms for line segments in 3D space.
    The result is a `Geom_TrimmedCurve`.
    A `GC_MakeSegment` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and resulting segment via `Value()`.
    """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a segment of a line from two points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @note Construction fails if the two points are coincident.
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin, theU1: float, theU2: float) -> None:
        """
        Creates a segment of the input line between two parameters.
        @param[in] theLine source line
        @param[in] theU1 first parameter
        @param[in] theU2 second parameter
        @note Construction fails when both parameters are equal.
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin, thePoint: nanoocp.gp.gp_Pnt, theUlast: float) -> None:
        """
        Creates a segment of the input line between a point and a parameter.
        @param[in] theLine source line
        @param[in] thePoint start point on line
        @param[in] theUlast end parameter
        @note Construction fails if trimming parameters are equal.
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a segment of the input line between two points.
        @param[in] theLine source line
        @param[in] theP1 first point
        @param[in] theP2 second point
        @note Construction fails if trimming parameters are equal.
        """

    def Value(self) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the constructed line segment.
        @return resulting line segment
        """

class GC_MakeSegment2d(GC_Root):
    """
    This class implements construction algorithms for line segments in the plane.
    The result is a `Geom2d_TrimmedCurve`.
    A `GC_MakeSegment2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting segment via `Value()`.
    """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a segment between two points.
        @param[in] theP1 first point
        @param[in] theP2 second point
        @note Construction fails with `gce_ConfusedPoints` if points are coincident.
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt2d, theV: nanoocp.gp.gp_Dir2d, theP2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a segment on a line defined by point and direction.
        The segment starts at `theP1` and ends at the orthogonal projection
        of `theP2` onto that line.
        @param[in] theP1 first point
        @param[in] theV direction vector
        @param[in] theP2 second point
        @note Construction fails with `gce_ConfusedPoints` if the projected
        endpoint is coincident with `theP1` within resolution.
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d, theU1: float, theU2: float) -> None:
        """
        Creates a segment on a line between two parameter values.
        @param[in] theLine source line
        @param[in] theU1 first parameter
        @param[in] theU2 second parameter
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d, thePoint: nanoocp.gp.gp_Pnt2d, theUlast: float) -> None:
        """
        Creates a segment on a line between point parameter and target parameter.
        @param[in] theLine source line
        @param[in] thePoint first point on segment support line
        @param[in] theUlast last parameter
        """

    @overload
    def __init__(self, theLine: nanoocp.gp.gp_Lin2d, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a segment on a line between projections of two points.
        @param[in] theLine source line
        @param[in] theP1 first point
        @param[in] theP2 second point
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """
        Returns the constructed line segment.
        Exceptions StdFail_NotDone if no line segment is constructed.
        @return resulting trimmed curve
        """

class GC_MakeTranslation:
    """
    This class implements elementary construction algorithms for a
    translation in 3D space. The result is a
    Geom_Transformation transformation.
    A MakeTranslation object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, theVect: nanoocp.gp.gp_Vec) -> None:
        """
        Constructs a translation from a vector.
        @param[in] theVect translation vector
        """

    @overload
    def __init__(self, thePoint1: nanoocp.gp.gp_Pnt, thePoint2: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a translation from two points.
        @param[in] thePoint1 start point
        @param[in] thePoint2 end point
        """

    def Value(self) -> nanoocp.Geom.Geom_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeTranslation2d:
    """
    This class implements elementary construction algorithms for
    translations in 2D space.
    The result is a `Geom2d_Transformation`.
    A `GC_MakeTranslation2d` object provides a framework for:
    - defining the transformation parameters;
    - running the construction algorithm;
    - querying the resulting transformation via `Value()`.
    """

    @overload
    def __init__(self, theVect: nanoocp.gp.gp_Vec2d) -> None:
        """
        Constructs a translation along a vector.
        @param[in] theVect translation vector
        """

    @overload
    def __init__(self, thePoint1: nanoocp.gp.gp_Pnt2d, thePoint2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a translation along the vector from one point to another.
        @param[in] thePoint1 first point
        @param[in] thePoint2 second point
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Transformation:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

class GC_MakeTrimmedCone(GC_Root):
    """
    Implements construction algorithms for trimmed cones.
    The result is a `Geom_RectangularTrimmedSurface`.
    A MakeTrimmedCone provides a framework for:
    -   defining the construction of the trimmed cone,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the Value
    function returns the constructed trimmed cone.
    """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt, theP4: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a rectangular trimmed conical surface from four points.
        @param[in] theP1 first axis point
        @param[in] theP2 second axis point
        @param[in] theP3 point defining first trimming section
        @param[in] theP4 point defining second trimming section
        @note The surface is trimmed by points P3 and P4.
        @note The axis is defined by points P1 and P2; the base radius is
        the distance from point P3 to that axis.
        @note The distance from point P4 to that axis is the radius of
        the section passing through P4.
        @note Construction fails if points P1, P2, P3 and P4 are
        collinear, or if vector P3P4 is perpendicular/collinear
        to vector P1P2.
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theR1: float, theR2: float) -> None:
        """
        Creates a rectangular trimmed conical surface from two points and two radii.
        @param[in] theP1 first axis point
        @param[in] theP2 second axis point
        @param[in] theR1 radius at P1
        @param[in] theR2 radius at P2
        @note The two radii correspond to sections passing through the two axis points.
        @note On failure, status is propagated from
        `GC_MakeConicalSurface(theP1, theP2, theR1, theR2)`.
        """

    def Value(self) -> nanoocp.Geom.Geom_RectangularTrimmedSurface:
        """
        Returns the constructed trimmed cone.
        StdFail_NotDone if no trimmed cone is constructed.
        @return resulting trimmed conical surface
        """

class GC_MakeTrimmedCylinder(GC_Root):
    """
    Implements construction algorithms for trimmed cylinders.
    The result is a `Geom_RectangularTrimmedSurface`.
    A MakeTrimmedCylinder provides a framework for:
    -   defining the construction of the trimmed cylinder,
    -   implementing the construction algorithm, and
    -   consulting the results. In particular, the Value
    function returns the constructed trimmed cylinder.
    """

    @overload
    def __init__(self, theCirc: nanoocp.gp.gp_Circ, theHeight: float) -> None:
        """
        Creates a trimmed cylindrical surface from a base circle and height.
        @param[in] theCirc base circle
        @param[in] theHeight trimming height
        @note The axis is the normal to the plane defined by `theCirc`.
        @note `theHeight` can be positive or negative.
        @note If `theHeight` is positive, the V parametric direction of
        result has the same orientation as the normal to `theCirc`.
        @note If `theHeight` is negative, it has the opposite orientation.
        """

    @overload
    def __init__(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt, theP3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a trimmed cylindrical surface from three points.
        @param[in] theP1 first axis point
        @param[in] theP2 second axis point
        @param[in] theP3 point defining radius
        @note The axis is the line passing through `theP1` and `theP2`.
        @note The radius is the distance from `theP3` to that axis.
        @note The height is the distance between `theP1` and `theP2`.
        """

    @overload
    def __init__(self, theA1: nanoocp.gp.gp_Ax1, theRadius: float, theHeight: float) -> None:
        """
        Creates a trimmed cylindrical surface from axis, radius and height.
        @param[in] theA1 cylinder axis
        @param[in] theRadius cylinder radius
        @param[in] theHeight trimming height
        @note Status is `gce_NegativeRadius` if `theRadius` is less than zero.
        @note `theHeight` can be positive or negative.
        @note If `theHeight` is positive, the V parametric direction of
        result has the same orientation as `theA1`.
        @note If `theHeight` is negative, it has the opposite orientation.
        """

    def Value(self) -> nanoocp.Geom.Geom_RectangularTrimmedSurface:
        """
        Returns the constructed trimmed cylinder.
        Exceptions
        StdFail_NotDone if no trimmed cylinder is constructed.
        @return resulting trimmed cylindrical surface
        """

class GC_MakeParabola2d(GC_Root):
    """
    This class implements construction algorithms for parabolas in the plane.
    The result is a `Geom2d_Parabola`.
    A `GC_MakeParabola2d` object provides a framework for:
    - defining the construction parameters;
    - running the construction algorithm;
    - querying the construction status and the resulting parabola via `Value()`.
    @note Parabola parameterization range is ]-infinite, +infinite[.
    @note In the local coordinate system, the parabola equation is
    Y**2 = (2*P) * X, where P is the parameter and F = P/2 is focal length.
    """

    @overload
    def __init__(self, theParabola: nanoocp.gp.gp_Parab2d) -> None:
        """
        Creates a parabola from a non-persistent one from package gp.
        @param[in] theParabola source parabola
        """

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax22d, theFocal: float) -> None:
        """
        Creates a parabola from a local coordinate system and focal length.
        @param[in] theAxis local coordinate system
        @param[in] theFocal focal length
        @note Construction fails with `gce_NullFocusLength` if `theFocal` is negative.
        """

    @overload
    def __init__(self, theDirectrix: nanoocp.gp.gp_Ax2d, theFocus: nanoocp.gp.gp_Pnt2d, theSense: bool = True) -> None:
        """
        Creates a parabola from directrix and focus point.
        @param[in] theDirectrix directrix axis
        @param[in] theFocus focus point
        @param[in] theSense orientation flag
        """

    @overload
    def __init__(self, theFocus: nanoocp.gp.gp_Pnt2d, theVertex: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a parabola from focus and vertex points.
        @param[in] theFocus focus point
        @param[in] theVertex vertex point
        @note Error status is provided by the underlying `gce_MakeParab2d`
        (for example `gce_NullAxis`).
        """

    @overload
    def __init__(self, theMirrorAxis: nanoocp.gp.gp_Ax2d, theFocal: float, theSense: bool) -> None:
        """
        Creates a parabola from symmetry axis and focal length.
        @param[in] theMirrorAxis symmetry axis placement
        @param[in] theFocal focal length
        @param[in] theSense orientation flag
        @note Construction fails with `gce_NullFocusLength` if `theFocal` is negative.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_Parabola:
        """
        Returns the constructed parabola.
        Exceptions StdFail_NotDone if no parabola is constructed.
        @return resulting parabola
        """
