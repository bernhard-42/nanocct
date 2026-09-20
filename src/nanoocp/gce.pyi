"""OCCT package gce (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.gp


class gce_ErrorType(enum.IntEnum):
    """
    Defines status codes returned by `gce` construction algorithms.
    - `gce_Done`: construction completed successfully.
    - `gce_ConfusedPoints`: two points are coincident.
    - `gce_NegativeRadius`: a radius value is negative.
    - `gce_ColinearPoints`: three points are collinear.
    - `gce_IntersectionError`: intersection cannot be computed.
    - `gce_NullAxis`: axis is undefined.
    - `gce_NullAngle`: angle value is invalid (usually null).
    - `gce_NullRadius`: radius is null.
    - `gce_InvertAxis`: axis value is invalid.
    - `gce_BadAngle`: angle value is invalid.
    - `gce_InvertRadius`: radius values are inconsistent.
    - `gce_NullFocusLength`: focal distance is null.
    - `gce_NullVector`: vector is null.
    - `gce_BadEquation`: coefficients of an equation are invalid.
    """

    gce_Done = 0

    gce_ConfusedPoints = 1

    gce_NegativeRadius = 2

    gce_ColinearPoints = 3

    gce_IntersectionError = 4

    gce_NullAxis = 5

    gce_NullAngle = 6

    gce_NullRadius = 7

    gce_InvertAxis = 8

    gce_BadAngle = 9

    gce_InvertRadius = 10

    gce_NullFocusLength = 11

    gce_NullVector = 12

    gce_BadEquation = 13

class gce_Root:
    """Provides common status services for all `gce` construction classes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: gce_Root) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the construction is successful.
        @return true if status is `gce_Done`
        """

    def IsError(self) -> bool:
        """
        Returns true if the construction has failed.
        @return true if status is not `gce_Done`
        """

    def Status(self) -> gce_ErrorType:
        """
        Returns the status of the construction:
        -   gce_Done, if the construction is successful, or
        -   another value of the gce_ErrorType enumeration
        indicating why the construction failed.
        @return construction status
        """

class gce_MakeCirc(gce_Root):
    """
    This class implements construction algorithms for `gp_Circ`.
    Supported constructions include:
    - circle from axis and radius;
    - circle coaxial to another one, through point or at signed offset;
    - circle through three points;
    - circle from center and normal/plane;
    - circle from center and axis-defining point;
    - circle from axis and radius.
    """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2, Radius: float) -> None:
        """
        Creates a circle from axis placement and radius.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @param[in] A2 local coordinate system
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ, Dist: float) -> None:
        """
        Creates a circle coaxial to input circle at signed distance.
        @note If `Dist` is positive, the result encloses `Circ`.
        @note If `Dist` is negative, the result is enclosed by `Circ`.
        @param[in] Circ source circle
        @param[in] Dist signed distance
        """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a circle coaxial to input circle and passing through a point.
        @param[in] Circ source circle
        @param[in] Point reference point
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1, Radius: float) -> None:
        """
        Creates a circle from axis and radius.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @param[in] Axis axis definition
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a circle passing through three points.
        @param[in] P1 first point
        @param[in] P2 second point
        @param[in] P3 third point
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, Norm: nanoocp.gp.gp_Dir, Radius: float) -> None:
        """
        Creates a circle from center, plane normal and radius.
        @param[in] Center center point
        @param[in] Norm input value
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, Plane: nanoocp.gp.gp_Pln, Radius: float) -> None:
        """
        Creates a circle from center, reference plane and radius.
        @param[in] Center center point
        @param[in] Plane reference plane
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, Ptaxis: nanoocp.gp.gp_Pnt, Radius: float) -> None:
        """
        Creates a circle from center, axis-defining point and radius.
        @param[in] Center center point
        @param[in] Ptaxis point defining axis direction
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, theOther: gce_MakeCirc) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Circ:
        """
        Returns the constructed circle.
        Exceptions StdFail_NotDone if no circle is constructed.
        @return resulting circle
        """

    def Operator(self) -> nanoocp.gp.gp_Circ:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeCirc2d(gce_Root):
    """
    This class implements construction algorithms for `gp_Circ2d`.
    Supported constructions include:
    - circle from axis and radius;
    - circle concentric to another one, through point or at signed offset;
    - circle through three points;
    - circle from center and radius;
    - circle from center and one point.
    """

    @overload
    def __init__(self, XAxis: nanoocp.gp.gp_Ax2d, Radius: float, Sense: bool = True) -> None:
        """
        Creates a circle from axis and radius.
        @note The location of `XAxis` is the circle center.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @param[in] XAxis axis placement
        @param[in] Radius radius value
        @param[in] Sense orientation flag
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax22d, Radius: float) -> None:
        """
        Creates a circle from local coordinate system and radius.
        @note The location of `Axis` is the circle center.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @param[in] Axis axis definition
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ2d, Dist: float) -> None:
        """
        Creates a circle concentric to input circle with signed offset.
        @note Result radius is `Abs(Circ.Radius() + Dist)`.
        @param[in] Circ source circle
        @param[in] Dist signed distance
        """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ2d, Point: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a circle concentric to input circle and passing through a point.
        @param[in] Circ source circle
        @param[in] Point reference point
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt2d, Radius: float, Sense: bool = True) -> None:
        """
        Creates a circle from center and radius.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @param[in] Center center point
        @param[in] Radius radius value
        @param[in] Sense orientation flag
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt2d, Point: nanoocp.gp.gp_Pnt2d, Sense: bool = True) -> None:
        """
        Creates a circle from center and one point on circle.
        @note `Sense` controls result orientation.
        @param[in] Center center point
        @param[in] Point reference point
        @param[in] Sense orientation flag
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, P3: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a circle passing through three points.
        @note The local coordinate system of the result is derived
        from input points.
        @param[in] P1 first point
        @param[in] P2 second point
        @param[in] P3 third point
        """

    @overload
    def __init__(self, theOther: gce_MakeCirc2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the constructed circle.
        Exceptions StdFail_NotDone if no circle is constructed.
        @return resulting circle
        """

    def Operator(self) -> nanoocp.gp.gp_Circ2d:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeCone(gce_Root):
    """
    This class implements construction algorithms for `gp_Cone`.
    Supported constructions include:
    - from axis placement, semi-angle and reference radius;
    - cone coaxial to another cone, through a point or at signed offset;
    - cone from four points;
    - cone from axis and two points;
    - cone from two axis points and two section radii.
    """

    @overload
    def __init__(self, Cone: nanoocp.gp.gp_Cone, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cone coaxial to input cone and passing through a point.
        @note Construction fails with `gce_NegativeRadius` when no non-negative
        solution radius can be found.
        @param[in] Cone source cone
        @param[in] Point reference point
        """

    @overload
    def __init__(self, Cone: nanoocp.gp.gp_Cone, Dist: float) -> None:
        """
        Creates a cone coaxial to input cone at signed distance.
        @note Construction fails with `gce_NullAngle` if semi-angle cosine is
        numerically too small.
        @note Construction fails with `gce_NegativeRadius` if resulting radius is negative.
        @param[in] Cone source cone
        @param[in] Dist signed distance
        """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2, Ang: float, Radius: float) -> None:
        """
        Creates a cone from axis placement, semi-angle and reference radius.
        @note `A2` defines cone position and reference section plane.
        @note `Ang` is the cone semi-angle (radians), expected in ]0, PI/2[.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @note Construction fails with `gce_BadAngle` if
        `Ang <= gp::Resolution()` or `PI/2 - Ang <= gp::Resolution()`.
        @param[in] A2 local coordinate system
        @param[in] Ang angle value
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cone from axis and two points.
        @note Distance from `P1` to axis gives first section radius.
        @note Distance from `P2` to axis gives second section radius.
        @note Error status is propagated from the 4-point construction.
        @param[in] Axis axis definition
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Lin, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cone from line axis and two points.
        @note Distance from `P1` to axis gives first section radius.
        @note Distance from `P2` to axis gives second section radius.
        @note Error status is propagated from the 4-point construction.
        @param[in] Axis axis definition
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, P4: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cone from four points.
        @note `P1` and `P2` define the axis direction.
        @note Distance from `P3` to that axis defines base radius.
        @note Distance from `P4` to that axis defines radius of section through `P4`.
        @note Construction fails with `gce_ConfusedPoints` if `P1`/`P2` or `P3`/`P4`
        are coincident.
        @note Construction fails with `gce_NullAngle` if section distances produce
        zero cone angle.
        @note Construction fails with `gce_NullRadius` for degenerate right-angle
        or zero-angle radius configuration.
        @param[in] P1 first point
        @param[in] P2 second point
        @param[in] P3 third point
        @param[in] P4 fourth point
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, R1: float, R2: float) -> None:
        """
        Creates a cone from two axis points and two section radii.
        @note The axis is the line passing through `P1` and `P2`.
        @note `R1` is section radius at `P1`, `R2` is section radius at `P2`.
        @note Construction fails with `gce_NullAxis` if `P1` and `P2` are coincident.
        @note Construction fails with `gce_NegativeRadius` if `R1` or `R2` is negative.
        @note Construction fails with `gce_NullAngle` for degenerate zero-angle
        or right-angle configurations.
        @param[in] P1 first point
        @param[in] P2 second point
        @param[in] R1 first radius value
        @param[in] R2 second radius value
        """

    @overload
    def __init__(self, theOther: gce_MakeCone) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Cone:
        """
        Returns the constructed cone.
        Exceptions StdFail_NotDone if no cone is constructed.
        @return resulting cone
        """

    def Operator(self) -> nanoocp.gp.gp_Cone:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeCylinder(gce_Root):
    """
    This class implements construction algorithms for `gp_Cylinder`.
    Supported constructions include:
    - cylinder from axis placement and radius;
    - cylinder coaxial to another, through point or at signed offset;
    - cylinder from three points;
    - cylinder from axis and radius;
    - cylinder from circular base.
    """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ) -> None:
        """
        Creates a cylinder from circular base.
        @note The resulting cylinder axis equals the circle axis.
        @note This constructor succeeds for any valid `Circ`.
        @param[in] Circ source circle
        """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2, Radius: float) -> None:
        """
        Creates a cylinder from axis placement and radius.
        @note Construction fails with `gce_NegativeRadius` if `Radius` is negative.
        @param[in] A2 local coordinate system
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cylinder coaxial to input cylinder and passing through a point.
        @param[in] Cyl source cylinder
        @param[in] Point reference point
        """

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, Dist: float) -> None:
        """
        Creates a cylinder coaxial to input cylinder at signed distance.
        @note Construction fails with `gce_NegativeRadius` if resulting radius is negative.
        @param[in] Cyl source cylinder
        @param[in] Dist signed distance
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1, Radius: float) -> None:
        """
        Makes a Cylinder by its axis <Axis> and radius <Radius>.
        @param[in] Axis axis definition
        @param[in] Radius radius value
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a cylinder from three points.
        @note Axis is defined by points `P1` and `P2`.
        @note Radius is the distance from `P3` to that axis.
        @param[in] P1 first point
        @param[in] P2 second point
        @param[in] P3 third point
        """

    @overload
    def __init__(self, theOther: gce_MakeCylinder) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Cylinder:
        """
        Returns the constructed cylinder.
        Exceptions StdFail_NotDone if no cylinder is constructed.
        @return resulting cylinder
        """

    def Operator(self) -> nanoocp.gp.gp_Cylinder:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeDir(gce_Root):
    """
    This class implements construction algorithms for `gp_Dir`.
    Supported constructions include:
    - direction from vector or coordinate components;
    - direction from two points.
    """

    @overload
    def __init__(self, V: nanoocp.gp.gp_Vec) -> None:
        """
        Normalizes the vector V and creates a direction.
        @note Construction fails with `gce_NullVector` if
        `V.Magnitude() <= gp::Resolution()`.
        @param[in] V direction vector
        """

    @overload
    def __init__(self, Coord: nanoocp.gp.gp_XYZ) -> None:
        """
        Creates a direction from a coordinate vector.
        @note Construction fails with `gce_NullVector` if
        `Coord.Modulus() <= gp::Resolution()`.
        @param[in] Coord coordinate vector
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a direction from two points.
        @note Construction fails with `gce_ConfusedPoints` if points are coincident.
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, Xv: float, Yv: float, Zv: float) -> None:
        """
        Creates a direction with its 3 cartesian coordinates.
        @note Construction fails with `gce_NullVector` if
        `Xv*Xv + Yv*Yv + Zv*Zv <= gp::Resolution()`.
        @param[in] Xv X coordinate value
        @param[in] Yv Y coordinate value
        @param[in] Zv Z coordinate value
        """

    @overload
    def __init__(self, theOther: gce_MakeDir) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Dir:
        """
        Returns the constructed unit vector.
        Exceptions StdFail_NotDone if no unit vector is constructed.
        @return resulting direction
        """

    def Operator(self) -> nanoocp.gp.gp_Dir:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeDir2d(gce_Root):
    """
    This class implements construction algorithms for `gp_Dir2d`.
    Supported constructions include:
    - direction from vector or coordinate components;
    - direction from two points.
    """

    @overload
    def __init__(self, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Normalizes the vector V and creates a direction.
        @note Construction fails with `gce_NullVector` if
        `V.Magnitude() <= gp::Resolution()`.
        @param[in] V direction vector
        """

    @overload
    def __init__(self, Coord: nanoocp.gp.gp_XY) -> None:
        """
        Creates a direction from a coordinate vector.
        @note Construction fails with `gce_NullVector` if
        `Coord.Modulus() <= gp::Resolution()`.
        @param[in] Coord coordinate vector
        """

    @overload
    def __init__(self, Xv: float, Yv: float) -> None:
        """
        Creates a direction with its two cartesian coordinates.
        @note Construction fails with `gce_NullVector` if
        `Xv*Xv + Yv*Yv <= gp::Resolution()`.
        @param[in] Xv X coordinate value
        @param[in] Yv Y coordinate value
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a direction from two points.
        @note Construction fails with `gce_ConfusedPoints` if points are coincident.
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, theOther: gce_MakeDir2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Dir2d:
        """
        Returns the constructed unit vector.
        Exceptions StdFail_NotDone if no unit vector is constructed.
        @return resulting direction
        """

    def Operator(self) -> nanoocp.gp.gp_Dir2d:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeElips(gce_Root):
    """
    This class implements construction algorithms for `gp_Elips`.
    Supported constructions include:
    - ellipse from local coordinate system and radii;
    - ellipse from center and two points.
    """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float) -> None:
        """
        The major radius of the ellipse is on the "XAxis" and the
        minor radius is on the "YAxis" of the ellipse. The "XAxis"
        is defined with the "XDirection" of A2 and the "YAxis" is
        defined with the "YDirection" of A2.
        @note It is possible to create an ellipse with
        `MajorRadius == MinorRadius`.
        @note Construction fails with `gce_InvertRadius` if
        `MajorRadius < MinorRadius`.
        @note Construction fails with `gce_NegativeRadius` if
        `MinorRadius < 0.0`.
        @param[in] A2 local coordinate system
        @param[in] MajorRadius major radius value
        @param[in] MinorRadius minor radius value
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pnt, S2: nanoocp.gp.gp_Pnt, Center: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates an ellipse from center and two points.
        @note `S1` defines major radius direction and value.
        @note Minor radius is computed as distance from `S2` to major axis.
        @note Construction fails with `gce_NullAxis` if `S1` and `Center` coincide.
        @note Construction fails with `gce_InvertAxis` when computed minor radius
        is null/greater than major radius, or when points are collinear.
        @param[in] S1 first point
        @param[in] S2 second point
        @param[in] Center center point
        """

    @overload
    def __init__(self, theOther: gce_MakeElips) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Elips:
        """
        Returns the constructed ellipse.
        Exceptions StdFail_NotDone if no ellipse is constructed.
        @return resulting ellipse
        """

    def Operator(self) -> nanoocp.gp.gp_Elips:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeElips2d(gce_Root):
    """
    This class implements construction algorithms for `gp_Elips2d`.
    Supported constructions include:
    - ellipse from major axis (or local 2D coordinate system) and radii;
    - ellipse from center and two points.
    """

    @overload
    def __init__(self, MajorAxis: nanoocp.gp.gp_Ax2d, MajorRadius: float, MinorRadius: float, Sense: bool = True) -> None:
        """
        Creates an ellipse with the major axis, the major and the
        minor radius. The location of the MajorAxis is the center
        of the ellipse.
        The sense of parametrization is given by Sense.
        It is possible to create an ellipse with MajorRadius = MinorRadius.
        @note Construction fails with `gce_InvertRadius` if
        `MajorRadius < MinorRadius`.
        @note Construction fails with `gce_NegativeRadius` if
        `MajorRadius < 0.0`.
        @param[in] MajorAxis major axis placement
        @param[in] MajorRadius major radius value
        @param[in] MinorRadius minor radius value
        @param[in] Sense orientation flag
        """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float) -> None:
        """
        Axis defines the Xaxis and Yaxis of the ellipse which defines
        the origin and the sense of parametrization.
        Creates an ellipse with the AxisPlacement the major and the
        minor radius. The location of Axis is the center
        of the ellipse.
        It is possible to create an ellipse with MajorRadius = MinorRadius.
        @note Construction fails with `gce_InvertRadius` if
        `MajorRadius < MinorRadius`.
        @note Construction fails with `gce_NegativeRadius` if
        `MajorRadius < 0.0`.
        @param[in] A local coordinate system
        @param[in] MajorRadius major radius value
        @param[in] MinorRadius minor radius value
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pnt2d, S2: nanoocp.gp.gp_Pnt2d, Center: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates an ellipse from center and two points.
        @note `S1` defines major radius direction and value.
        @note Minor radius is computed as distance from `S2` to major axis.
        @note Construction fails with `gce_NullAxis` when computed minor radius
        is null.
        @note Construction fails with `gce_InvertAxis` when computed minor radius
        exceeds major radius.
        @param[in] S1 first point
        @param[in] S2 second point
        @param[in] Center center point
        """

    @overload
    def __init__(self, theOther: gce_MakeElips2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Elips2d:
        """
        Returns the constructed ellipse.
        Exceptions StdFail_NotDone if no ellipse is constructed.
        @return resulting ellipse
        """

    def Operator(self) -> nanoocp.gp.gp_Elips2d:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeHypr(gce_Root):
    """
    This class implements construction algorithms for `gp_Hypr`.
    Supported constructions include:
    - hyperbola from center and two points (one on major axis);
    - hyperbola from local coordinate system and radii.

    ^YAxis
    |
    FirstConjugateBranch
    |
    Other            |                Main
    --------------------- C ------------------------------>XAxis
    Branch           |                Branch
    |
    |
    SecondConjugateBranch
    |

    The local Cartesian coordinate system of the hyperbola is an
    axis placement (two axes).

    The "XDirection" and the "YDirection" of the axis placement
    define the plane of the hyperbola.

    The "Direction" of the axis placement defines the normal axis
    to the hyperbola's plane.

    The "XAxis" of the hyperbola ("Location", "XDirection") is the
    major axis and the "YAxis" of the hyperbola ("Location",
    "YDirection") is the minor axis.

    @note The major radius (on major axis) can be lower than the
    minor radius (on minor axis).
    """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float) -> None:
        """
        Creates a hyperbola from a local coordinate system and radii.
        @note In the local coordinate system of `A2`, the equation is
        `X*X / (MajorRadius*MajorRadius) - Y*Y / (MinorRadius*MinorRadius) = 1.0`.
        @note Construction with `MajorRadius == MinorRadius` is valid.
        @note Construction fails with `gce_NegativeRadius` if
        `MajorRadius < 0.0` or `MinorRadius < 0.0`.
        @param[in] A2 local coordinate system
        @param[in] MajorRadius major radius value
        @param[in] MinorRadius minor radius value
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pnt, S2: nanoocp.gp.gp_Pnt, Center: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a hyperbola from center and two points.
        @note `Center` is the hyperbola center, `Center`-`S1` defines the major axis,
        major radius is `Distance(Center, S1)`, and minor radius is distance from
        `S2` to this major axis.
        @note Construction fails with `gce_ConfusedPoints` if any two of `S1`, `S2`,
        and `Center` are coincident.
        @note Construction fails with `gce_ColinearPoints` if `S1`, `S2`, and `Center`
        are collinear.
        @param[in] S1 first point
        @param[in] S2 second point
        @param[in] Center center point
        """

    @overload
    def __init__(self, theOther: gce_MakeHypr) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Hypr:
        """
        Returns the constructed hyperbola.
        Exceptions StdFail_NotDone if no hyperbola is constructed.
        @return resulting hyperbola
        """

    def Operator(self) -> nanoocp.gp.gp_Hypr:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeHypr2d(gce_Root):
    """
    This class implements construction algorithms for `gp_Hypr2d`.
    Supported constructions include:
    - hyperbola from center and two points (one on major axis);
    - hyperbola from major axis and radii;
    - hyperbola from local coordinate system and radii.

    ^YAxis
    |
    FirstConjugateBranch
    |
    Other            |                Main
    --------------------- C ------------------------------>XAxis
    Branch           |                Branch
    |
    |
    SecondConjugateBranch
    |

    An axis placement (one axis) is associated with the hyperbola.
    This axis is the "XAxis" or major axis of the hyperbola.
    It is the symmetry axis of the main branch.
    The "YAxis" is normal to this axis and passes through its location point.
    It is the minor axis.

    The major radius is the distance between the Location point
    of the hyperbola C and the vertex of the Main Branch (or the
    Other branch). The minor radius is the distance between the
    Location point of the hyperbola C and the vertex of the First
    (or Second) Conjugate branch.
    The major radius can be lower than the minor radius.
    """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pnt2d, S2: nanoocp.gp.gp_Pnt2d, Center: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a hyperbola from center and two points.
        @note `Center` is the hyperbola center, `Center`-`S1` defines major axis,
        major radius is `Distance(Center, S1)`, and minor radius is distance
        from `S2` to this major axis.
        @note Construction fails with `gce_ConfusedPoints` if any two of `S1`, `S2`,
        and `Center` are coincident.
        @note Construction fails with `gce_ColinearPoints` if `S1`, `S2`, and `Center`
        are collinear.
        @param[in] S1 first point
        @param[in] S2 second point
        @param[in] Center center point
        """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float) -> None:
        """
        Creates a hyperbola from local coordinate system and radii.
        @note The result is centered at `A.Location()`, and its major axis follows
        the X axis direction of `A`.
        @note Construction fails with `gce_NegativeRadius` if
        `MajorRadius < 0.0` or `MinorRadius < 0.0`.
        @param[in] A local coordinate system
        @param[in] MajorRadius major radius value
        @param[in] MinorRadius minor radius value
        """

    @overload
    def __init__(self, MajorAxis: nanoocp.gp.gp_Ax2d, MajorRadius: float, MinorRadius: float, Sense: bool) -> None:
        """
        Creates a hyperbola from major axis and radii.
        @note Center is located at `MajorAxis.Location()`.
        @note If `Sense` is `false`, the opposite direction of `MajorAxis` is used.
        @note Construction fails with `gce_NegativeRadius` if
        `MajorRadius < 0.0` or `MinorRadius < 0.0`.
        @param[in] MajorAxis major axis placement
        @param[in] MajorRadius major radius value
        @param[in] MinorRadius minor radius value
        @param[in] Sense orientation flag
        """

    @overload
    def __init__(self, theOther: gce_MakeHypr2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Hypr2d:
        """
        Returns the constructed hyperbola.
        Exceptions StdFail_NotDone if no hyperbola is constructed.
        @return resulting hyperbola
        """

    def Operator(self) -> nanoocp.gp.gp_Hypr2d:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeLin(gce_Root):
    """
    This class implements construction algorithms for `gp_Lin`.
    Supported constructions include:
    - line from axis placement;
    - line from point and direction;
    - parallel line through point;
    - line through two points.
    """

    @overload
    def __init__(self, A1: nanoocp.gp.gp_Ax1) -> None:
        """
        Creates a line located along the axis A1.
        @note The location of `A1` is the line origin.
        @param[in] A1 axis placement
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Dir) -> None:
        """
        <P> is the location point (origin) of the line and
        <V> is the direction of the line.
        @param[in] P point
        @param[in] V direction vector
        """

    @overload
    def __init__(self, Lin: nanoocp.gp.gp_Lin, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a line parallel to input line and passing through a point.
        @param[in] Lin source line
        @param[in] Point reference point
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a line passing through two points.
        @note Construction fails with `gce_ConfusedPoints` if points are coincident.
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, theOther: gce_MakeLin) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Lin:
        """
        Returns the constructed line.
        Exceptions StdFail_NotDone is raised if no line is constructed.
        @return resulting line
        """

    def Operator(self) -> nanoocp.gp.gp_Lin:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeLin2d(gce_Root):
    """
    This class implements construction algorithms for `gp_Lin2d`.
    Supported constructions include:
    - line from axis placement;
    - line from point and direction;
    - line from cartesian equation;
    - parallel line through point or at signed distance;
    - line through two points.
    """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """
        Creates a line located with A.
        @note The location of `A` is the line origin.
        @param[in] A local coordinate system
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Dir2d) -> None:
        """
        <P> is the location point (origin) of the line and
        <V> is the direction of the line.
        @param[in] P point
        @param[in] V direction vector
        """

    @overload
    def __init__(self, Lin: nanoocp.gp.gp_Lin2d, Dist: float) -> None:
        """
        Creates a line parallel to input line at signed distance.
        @note If `Dist` is positive, the result is on the right side
        of `Lin` (in line local orientation), otherwise on the left.
        @param[in] Lin source line
        @param[in] Dist signed distance
        """

    @overload
    def __init__(self, Lin: nanoocp.gp.gp_Lin2d, Point: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a line parallel to input line and passing through a point.
        @param[in] Lin source line
        @param[in] Point reference point
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a line passing through two points.
        @note Construction fails with `gce_ConfusedPoints` if `P1` and `P2`
        are coincident.
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, A: float, B: float, C: float) -> None:
        """
        Creates the line from the equation A*X + B*Y + C = 0.0
        @note Construction fails with `gce_NullAxis` if
        `A*A + B*B <= gp::Resolution()`.
        @param[in] A equation coefficient A
        @param[in] B equation coefficient B
        @param[in] C equation coefficient C
        """

    @overload
    def __init__(self, theOther: gce_MakeLin2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the constructed line.
        Exceptions StdFail_NotDone if no line is constructed.
        @return resulting line
        """

    def Operator(self) -> nanoocp.gp.gp_Lin2d:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeMirror:
    """
    This class implements elementary construction algorithms for a
    symmetrical transformation in 3D space about a point,
    axis or plane. The result is a gp_Trsf transformation.
    A MakeMirror object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a central symmetry about a point.
        @param[in] Point center point
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1) -> None:
        """
        Constructs an axial symmetry about an axis.
        @param[in] Axis mirror axis
        """

    @overload
    def __init__(self, Line: nanoocp.gp.gp_Lin) -> None:
        """
        Constructs an axial symmetry about a line.
        @param[in] Line mirror line
        """

    @overload
    def __init__(self, Plane: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def __init__(self, Plane: nanoocp.gp.gp_Ax2) -> None:
        """
        Constructs a planar symmetry about a plane.
        @param[in] Plane mirror plane
        """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt, Direc: nanoocp.gp.gp_Dir) -> None:
        """
        Constructs an axial symmetry about an axis defined by point and direction.
        @param[in] Point point on the axis
        @param[in] Direc axis direction
        """

    @overload
    def __init__(self, theOther: gce_MakeMirror) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeMirror2d:
    """
    This class implements elementary construction algorithms for a
    symmetrical transformation in 2D space about a point
    or axis. The result is a gp_Trsf2d transformation.
    A MakeMirror2d object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and consulting the result.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a central symmetry about a point.
        @param[in] Point center point
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax2d) -> None:
        """
        Constructs an axial symmetry about an axis.
        @param[in] Axis mirror axis
        """

    @overload
    def __init__(self, Line: nanoocp.gp.gp_Lin2d) -> None:
        """
        Constructs an axial symmetry about a line.
        @param[in] Line mirror line
        """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt2d, Direc: nanoocp.gp.gp_Dir2d) -> None:
        """
        Constructs an axial symmetry about an axis defined by point and direction.
        @param[in] Point point on the axis
        @param[in] Direc axis direction
        """

    @overload
    def __init__(self, theOther: gce_MakeMirror2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeParab(gce_Root):
    """
    Implements construction algorithms for `gp_Parab`.
    The parabola is infinite in the parameter range ]-infinite, +infinite[.
    The vertex is the `Location` point of the local coordinate system.

    The `XDirection` and `YDirection` define the parabola plane.

    The `XAxis` (`Location`, `XDirection`) is the symmetry axis and is oriented
    from the vertex to the focus.

    The `YAxis` (`Location`, `YDirection`) is parallel to the directrix.

    The equation in the local coordinate system is:
    `Y**2 = (2*P) * X`, where `P` is the parameter
    (distance between focus and directrix).
    The focal length `F = P / 2` is the distance from vertex to focus.

    Supported constructions:
    - from local coordinate system and focal length;
    - from directrix and focus.
    """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2, Focal: float) -> None:
        """
        Creates a parabola from local coordinate system and focal length.
        @param[in] A2 local coordinate system of the parabola
        @param[in] Focal focal length
        @note `TheError` is set to `gce_NullFocusLength` if `Focal < 0.0`.
        """

    @overload
    def __init__(self, D: nanoocp.gp.gp_Ax1, F: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a parabola from directrix and focus.
        @param[in] D directrix of the parabola
        @param[in] F focus point of the parabola
        """

    @overload
    def __init__(self, theOther: gce_MakeParab) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Parab:
        """
        Returns the constructed parabola.
        @return resulting parabola
        @throw StdFail_NotDone if construction has failed
        """

    def Operator(self) -> nanoocp.gp.gp_Parab:
        """
        Alias for Value() returning a copy.
        @return resulting parabola
        """

class gce_MakeParab2d(gce_Root):
    """
    Implements construction algorithms for `gp_Parab2d`.
    The parabola is infinite and represented in a local 2D coordinate system.
    The `XAxis` is the symmetry axis directed from vertex to focus,
    and the `YAxis` is parallel to the directrix.
    The equation in local coordinates is:
    `Y**2 = (2*P) * X`, where `P` is the distance between focus and directrix.
    The focal length `F = P / 2` is the distance from vertex to focus.

    Supported constructions:
    - from symmetry axis and focal length;
    - from full axis system and focal length;
    - from directrix and focus;
    - from focus and vertex.
    """

    @overload
    def __init__(self, MirrorAxis: nanoocp.gp.gp_Ax2d, Focal: float, Sense: bool = True) -> None:
        """
        Creates a parabola from symmetry axis and focal length.
        @param[in] MirrorAxis symmetry axis of the parabola
        @param[in] Focal focal length
        @param[in] Sense orientation of parametrization
        @note `Focal = 0` is accepted.
        @note `TheError` is set to `gce_NullFocusLength` if `Focal < 0.0`.
        """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax22d, Focal: float) -> None:
        """
        Creates a parabola from full local coordinate system and focal length.
        @param[in] A local coordinate system of the parabola
        @param[in] Focal focal length
        @note `Focal = 0` is accepted.
        @note `TheError` is set to `gce_NullFocusLength` if `Focal < 0.0`.
        """

    @overload
    def __init__(self, D: nanoocp.gp.gp_Ax2d, F: nanoocp.gp.gp_Pnt2d, Sense: bool = True) -> None:
        """
        Creates a parabola from directrix and focus.
        @param[in] D directrix of the parabola
        @param[in] F focus point of the parabola
        @param[in] Sense orientation of parametrization
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pnt2d, Center: nanoocp.gp.gp_Pnt2d, Sense: bool = True) -> None:
        """
        Creates a parabola from focus and vertex.
        @param[in] S1 focus point
        @param[in] Center vertex point
        @param[in] Sense orientation of parametrization
        @note The class does not prevent zero focal distance.
        @note `TheError` is set to `gce_NullAxis` if `S1` and `Center` are coincident.
        """

    @overload
    def __init__(self, theOther: gce_MakeParab2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Parab2d:
        """
        Returns the constructed parabola.
        @return resulting parabola
        @throw StdFail_NotDone if construction has failed
        """

    def Operator(self) -> nanoocp.gp.gp_Parab2d:
        """
        Alias for Value() returning a copy.
        @return resulting parabola
        """

class gce_MakePln(gce_Root):
    """
    This class implements construction algorithms for `gp_Pln`.
    Supported constructions include:
    - plane from axis placement or point+normal;
    - plane from cartesian equation;
    - plane parallel to another plane through point or at signed distance;
    - plane through two or three points;
    - plane through axis location normal to axis direction.
    @note A plane is positioned by local coordinate system (`gp_Ax3`):
    - `Location` is the origin,
    - main direction is the plane normal,
    - `XDirection` and `YDirection` define in-plane axes.
    """

    @overload
    def __init__(self, A2: nanoocp.gp.gp_Ax2) -> None:
        """
        The coordinate system of the plane is defined with the axis
        placement A2.
        The "Direction" of A2 defines the normal to the plane.
        The "Location" of A2 defines the location (origin) of the plane.
        The "XDirection" and "YDirection" of A2 define the "XAxis" and
        the "YAxis" of the plane used to parametrize the plane.
        @param[in] A2 local coordinate system
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1) -> None:
        """
        Make a pln passing through the location of <Axis>and
        normal to the Direction of <Axis>.
        @note This constructor always succeeds for valid `Axis`.
        @param[in] Axis axis definition
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Dir) -> None:
        """
        Creates a plane with the "Location" point <P>
        and the normal direction <V>.
        @param[in] P point
        @param[in] V direction vector
        """

    @overload
    def __init__(self, Pln: nanoocp.gp.gp_Pln, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a plane parallel to input plane and passing through a point.
        @param[in] Pln source plane
        @param[in] Point reference point
        """

    @overload
    def __init__(self, Pln: nanoocp.gp.gp_Pln, Dist: float) -> None:
        """
        Creates a plane parallel to input plane at signed distance.
        @note Positive `Dist` shifts along the plane normal, negative in opposite direction.
        @param[in] Pln source plane
        @param[in] Dist signed distance
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a plane through `P1`, normal to direction (`P1`,`P2`).
        @note Construction fails with `gce_ConfusedPoints` if `P1` and `P2` coincide.
        @param[in] P1 first point
        @param[in] P2 second point
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a plane through three points.
        @note Construction fails with `gce_ColinearPoints` if points are collinear.
        @param[in] P1 first point
        @param[in] P2 second point
        @param[in] P3 third point
        """

    @overload
    def __init__(self, A: float, B: float, C: float, D: float) -> None:
        """
        Creates a plane from its cartesian equation :
        A * X + B * Y + C * Z + D = 0.0

        @note Construction fails with `gce_BadEquation` if
        `A*A + B*B + C*C <= gp::Resolution()`.
        @param[in] A equation coefficient A
        @param[in] B equation coefficient B
        @param[in] C equation coefficient C
        @param[in] D equation constant term
        """

    @overload
    def __init__(self, theOther: gce_MakePln) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pln:
        """
        Returns the constructed plane.
        Exceptions StdFail_NotDone if no plane is constructed.
        @return resulting plane
        """

    def Operator(self) -> nanoocp.gp.gp_Pln:
        """
        Alias for Value() returning a copy.
        @return resulting object
        """

class gce_MakeRotation:
    """
    This class implements elementary construction algorithms for a
    rotation in 3D space. The result is a gp_Trsf transformation.
    A MakeRotation object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Line: nanoocp.gp.gp_Lin, Angle: float) -> None:
        """
        Constructs a rotation around the axis defined by a line.
        @param[in] Line rotation axis
        @param[in] Angle rotation angle in radians
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1, Angle: float) -> None:
        """
        Constructs a rotation around an axis.
        @param[in] Axis rotation axis
        @param[in] Angle rotation angle in radians
        """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt, Direc: nanoocp.gp.gp_Dir, Angle: float) -> None:
        """
        Constructs a rotation around an axis defined by point and direction.
        @param[in] Point point on the axis
        @param[in] Direc axis direction
        @param[in] Angle rotation angle in radians
        """

    @overload
    def __init__(self, theOther: gce_MakeRotation) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeRotation2d:
    """
    Implements an elementary construction algorithm for
    a rotation in 2D space. The result is a gp_Trsf2d transformation.
    A MakeRotation2d object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt2d, Angle: float) -> None:
        """
        Constructs a rotation around a point in 2D.
        @param[in] Point rotation center
        @param[in] Angle rotation angle in radians
        """

    @overload
    def __init__(self, theOther: gce_MakeRotation2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeScale:
    """
    Implements an elementary construction algorithm for
    a scaling transformation in 3D space. The result is a gp_Trsf transformation.
    A MakeScale object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt, Scale: float) -> None:
        """
        Constructs a scaling transformation.
        @param[in] Point center of scaling
        @param[in] Scale scale factor
        """

    @overload
    def __init__(self, theOther: gce_MakeScale) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeScale2d:
    """
    This class implements an elementary construction algorithm for
    a scaling transformation in 2D space. The result is a gp_Trsf2d transformation.
    A MakeScale2d object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt2d, Scale: float) -> None:
        """
        Constructs a scaling transformation.
        @param[in] Point center of scaling
        @param[in] Scale scale factor
        """

    @overload
    def __init__(self, theOther: gce_MakeScale2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeTranslation:
    """
    This class implements elementary construction algorithms for a
    translation in 3D space. The result is a gp_Trsf transformation.
    A MakeTranslation object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Vect: nanoocp.gp.gp_Vec) -> None:
        """
        Constructs a translation from a vector.
        @param[in] Vect translation vector
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt, Point2: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs a translation from two points.
        @param[in] Point1 start point
        @param[in] Point2 end point
        """

    @overload
    def __init__(self, theOther: gce_MakeTranslation) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """

class gce_MakeTranslation2d:
    """
    This class implements elementary construction algorithms for a
    translation in 2D space. The result is a gp_Trsf2d transformation.
    A MakeTranslation2d object provides a framework for:
    -   defining the construction of the transformation,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Vect: nanoocp.gp.gp_Vec2d) -> None:
        """
        Constructs a translation from a vector.
        @param[in] Vect translation vector
        """

    @overload
    def __init__(self, Point1: nanoocp.gp.gp_Pnt2d, Point2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Constructs a translation from two points.
        @param[in] Point1 start point
        @param[in] Point2 end point
        """

    @overload
    def __init__(self, theOther: gce_MakeTranslation2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Returns the constructed transformation.
        @return resulting transformation
        """

    def Operator(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Alias for Value() returning a copy.
        @return resulting transformation
        """
