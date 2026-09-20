"""OCCT package Geom2d (toolkit TKG2d)"""

from typing import overload

import nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.Geom2dEval


class Geom2d_Geometry(nanoocp.Standard.Standard_Transient):
    """
    The general abstract class Geometry in 2D space describes
    the common behaviour of all the geometric entities.

    All the objects derived from this class can be move with a
    geometric transformation. Only the transformations which
    doesn't modify the nature of the geometry are available in
    this package.
    The method Transform which defines a general transformation
    is deferred. The other specifics transformations used the
    method Transform.
    All the following transformations modify the object itself.
    Warning
    Only transformations which do not modify the nature
    of the geometry can be applied to Geom2d objects:
    this is the case with translations, rotations,
    symmetries and scales; this is also the case with
    gp_Trsf2d composite transformations which are
    used to define the geometric transformations applied
    using the Transform or Transformed functions.
    Note: Geometry defines the "prototype" of the
    abstract method Transform which is defined for each
    concrete type of derived object. All other
    transformations are implemented using the Transform method.
    """

    @overload
    def Mirror(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Performs the symmetrical transformation of a Geometry
        with respect to the point P which is the center of the
        symmetry and assigns the result to this geometric object.
        """

    @overload
    def Mirror(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """
        Performs the symmetrical transformation of a Geometry
        with respect to an axis placement which is the axis of the symmetry.
        """

    def Rotate(self, P: nanoocp.gp.gp_Pnt2d, Ang: float) -> None:
        """
        Rotates a Geometry. P is the center of the rotation.
        Ang is the angular value of the rotation in radians.
        """

    def Scale(self, P: nanoocp.gp.gp_Pnt2d, S: float) -> None:
        """Scales a Geometry. S is the scaling value."""

    @overload
    def Translate(self, V: nanoocp.gp.gp_Vec2d) -> None:
        """Translates a Geometry. V is the vector of the translation."""

    @overload
    def Translate(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
        """Translates a Geometry from the point P1 to the point P2."""

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation of a geometric object. This transformation
        can be a translation, a rotation, a symmetry, a scaling
        or a complex transformation obtained by combination of
        the previous elementaries transformations.
        (see class Transformation of the package Geom2d).
        The following transformations have the same properties
        as the previous ones but they don't modified the object
        itself. A copy of the object is returned.
        """

    @overload
    def Mirrored(self, P: nanoocp.gp.gp_Pnt2d) -> Geom2d_Geometry: ...

    @overload
    def Mirrored(self, A: nanoocp.gp.gp_Ax2d) -> Geom2d_Geometry: ...

    def Rotated(self, P: nanoocp.gp.gp_Pnt2d, Ang: float) -> Geom2d_Geometry: ...

    def Scaled(self, P: nanoocp.gp.gp_Pnt2d, S: float) -> Geom2d_Geometry: ...

    def Transformed(self, T: nanoocp.gp.gp_Trsf2d) -> Geom2d_Geometry: ...

    @overload
    def Translated(self, V: nanoocp.gp.gp_Vec2d) -> Geom2d_Geometry: ...

    @overload
    def Translated(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> Geom2d_Geometry: ...

    def Copy(self) -> Geom2d_Geometry: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_AxisPlacement(Geom2d_Geometry):
    """
    Describes an axis in 2D space.
    An axis is defined by:
    - its origin, also termed the "Location point" of the axis,
    - its unit vector, termed the "Direction" of the axis.
    Note: Geom2d_AxisPlacement axes provide the
    same kind of "geometric" services as gp_Ax2d axes
    but have more complex data structures. The
    geometric objects provided by the Geom2d package
    use gp_Ax2d objects to include axes in their data
    structures, or to define an axis of symmetry or axis of rotation.
    Geom2d_AxisPlacement axes are used in a context
    where they can be shared by several objects
    contained inside a common data structure.
    """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """Constructs an axis by conversion of the gp_Ax2d axis A."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Dir2d) -> None:
        """Constructs an axis from a given origin P and unit vector V."""

    def Reverse(self) -> None: ...

    def Reversed(self) -> Geom2d_AxisPlacement:
        """
        Reverses the unit vector of this axis.
        Note:
        - Reverse assigns the result to this axis, while
        - Reversed creates a new one.
        """

    def SetAxis(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """Changes the complete definition of the axis placement."""

    def SetDirection(self, V: nanoocp.gp.gp_Dir2d) -> None:
        """Changes the "Direction" of the axis placement."""

    def SetLocation(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Changes the "Location" point (origin) of the axis placement."""

    def Angle(self, Other: Geom2d_AxisPlacement) -> float:
        """
        Computes the angle between the "Direction" of
        two axis placement in radians.
        The result is comprised between -Pi and Pi.
        """

    def Ax2d(self) -> nanoocp.gp.gp_Ax2d:
        """Converts this axis into a gp_Ax2d axis."""

    def Direction(self) -> nanoocp.gp.gp_Dir2d:
        """
        Returns the "Direction" of <me>.
        -C++: return const&
        """

    def Location(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the "Location" point (origin) of the axis placement.
        -C++: return const&
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this axis."""

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this axis."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_UndefinedDerivative(nanoocp.Standard.Standard_DomainError):
    pass

class Geom2d_UndefinedValue(nanoocp.Standard.Standard_DomainError):
    pass

class Geom2d_Curve(Geom2d_Geometry):
    """
    The abstract class Curve describes the common
    behavior of curves in 2D space. The Geom2d
    package provides numerous concrete classes of
    derived curves, including lines, circles, conics, Bezier
    or BSpline curves, etc.
    The main characteristic of these curves is that they
    are parameterized. The Geom2d_Curve class shows:
    - how to work with the parametric equation of a
    curve in order to calculate the point of parameter
    u, together with the vector tangent and the
    derivative vectors of order 2, 3,..., N at this point;
    - how to obtain general information about the curve
    (for example, level of continuity, closed
    characteristics, periodicity, bounds of the parameter field);
    - how the parameter changes when a geometric
    transformation is applied to the curve or when the
    orientation of the curve is inverted.
    All curves must have a geometric continuity: a curve is
    at least "C0". Generally, this property is checked at
    the time of construction or when the curve is edited.
    Where this is not the case, the documentation
    explicitly states so.
    Warning
    The Geom2d package does not prevent the
    construction of curves with null length or curves which
    self-intersect.
    """

    class ResD1:
        """Result of D1 evaluation: point and first derivative."""

        def __init__(self) -> None: ...

        @property
        def Point(self) -> nanoocp.gp.gp_Pnt2d: ...

        @Point.setter
        def Point(self, arg: nanoocp.gp.gp_Pnt2d, /) -> None: ...

        @property
        def D1(self) -> nanoocp.gp.gp_Vec2d: ...

        @D1.setter
        def D1(self, arg: nanoocp.gp.gp_Vec2d, /) -> None: ...

    class ResD2:
        """Result of D2 evaluation: point and first two derivatives."""

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

    class ResD3:
        """Result of D3 evaluation: point and first three derivatives."""

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

    def Reverse(self) -> None:
        """
        Changes the direction of parametrization of <me>.
        The "FirstParameter" and the "LastParameter" are not changed
        but the orientation of the curve is modified. If the curve
        is bounded the StartPoint of the initial curve becomes the
        EndPoint of the reversed curve and the EndPoint of the initial
        curve becomes the StartPoint of the reversed curve.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed curve for
        the point of parameter U on this curve.
        Note: The point of parameter U on this curve is
        identical to the point of parameter
        ReversedParameter(U) on the reversed curve.
        """

    def TransformedParameter(self, U: float, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Computes the parameter on the curve transformed by
        T for the point of parameter U on this curve.
        Note: this function generally returns U but it can be
        redefined (for example, on a line).
        """

    def ParametricTransformation(self, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns the coefficient required to compute the
        parametric transformation of this curve when
        transformation T is applied. This coefficient is the
        ratio between the parameter of a point on this curve
        and the parameter of the transformed point on the
        new curve transformed by T.
        Note: this function generally returns 1. but it can be
        redefined (for example, on a line).
        """

    def Reversed(self) -> Geom2d_Curve:
        """
        Creates a reversed duplicate Changes the orientation of this curve. The first and
        last parameters are not changed, but the parametric
        direction of the curve is reversed.
        If the curve is bounded:
        - the start point of the initial curve becomes the end
        point of the reversed curve, and
        - the end point of the initial curve becomes the start
        point of the reversed curve.
        - Reversed creates a new curve.
        """

    def FirstParameter(self) -> float:
        """
        Returns the value of the first parameter.
        Warnings :
        It can be RealFirst or RealLast from package Standard
        if the curve is infinite
        """

    def LastParameter(self) -> float:
        """
        Value of the last parameter.
        Warnings :
        It can be RealFirst or RealLast from package Standard
        if the curve is infinite
        """

    def IsClosed(self) -> bool:
        """
        Returns true if the curve is closed.
        Examples :
        Some curves such as circle are always closed, others such as line
        are never closed (by definition).
        Some Curves such as OffsetCurve can be closed or not. These curves
        are considered as closed if the distance between the first point
        and the last point of the curve is lower or equal to the Resolution
        from package gp which is a fixed criterion independent of the
        application.
        """

    def IsPeriodic(self) -> bool:
        """
        Returns true if the parameter of the curve is periodic.
        It is possible only if the curve is closed and if the
        following relation is satisfied :
        for each parametric value U the distance between the point
        P(u) and the point P (u + T) is lower or equal to Resolution
        from package gp, T is the period and must be a constant.
        There are three possibilities :
        . the curve is never periodic by definition (SegmentLine)
        . the curve is always periodic by definition (Circle)
        . the curve can be defined as periodic (BSpline). In this case
        a function SetPeriodic allows you to give the shape of the
        curve. The general rule for this case is : if a curve can be
        periodic or not the default periodicity set is non periodic
        and you have to turn (explicitly) the curve into a periodic
        curve if you want the curve to be periodic.
        """

    def Period(self) -> float:
        """
        Returns the period of this curve.
        raises if the curve is not periodic
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        It is the global continuity of the curve :
        C0 : only geometric continuity,
        C1 : continuity of the first derivative all along the Curve,
        C2 : continuity of the second derivative all along the Curve,
        C3 : continuity of the third derivative all along the Curve,
        G1 : tangency continuity all along the Curve,
        G2 : curvature continuity all along the Curve,
        CN : the order of continuity is infinite.
        """

    def IsCN(self, N: int) -> bool:
        """
        Returns true if the degree of continuity of this curve is at least N.
        Exceptions Standard_RangeError if N is less than 0.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Computes the point of parameter U.
        Raises an exception on failure.
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """
        Computes the point and first derivative at parameter U.
        Raises an exception if the curve continuity is not C1.
        """

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Computes the point and first two derivatives at parameter U.
        Raises an exception if the curve continuity is not C2.
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        Computes the point and first three derivatives at parameter U.
        Raises an exception if the curve continuity is not C3.
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the Nth derivative at parameter U.
        Raises an exception if the curve continuity is not CN, or N < 1.
        """

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Returns in P the point of parameter U."""

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None:
        """Returns the point P of parameter U and the first derivative V1."""

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """

    def D3(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second and the third derivative.
        """

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """Computes the Nth derivative vector."""

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on <me>. Implemented with D0."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_BoundedCurve(Geom2d_Curve):
    """
    The abstract class BoundedCurve describes the
    common behavior of bounded curves in 2D space. A
    bounded curve is limited by two finite values of the
    parameter, termed respectively "first parameter" and
    "last parameter". The "first parameter" gives the "start
    point" of the bounded curve, and the "last parameter"
    gives the "end point" of the bounded curve.
    The length of a bounded curve is finite.
    The Geom2d package provides three concrete
    classes of bounded curves:
    - two frequently used mathematical formulations of complex curves:
    - Geom2d_BezierCurve,
    - Geom2d_BSplineCurve, and
    - Geom2d_TrimmedCurve to trim a curve, i.e. to
    only take part of the curve limited by two values of
    the parameter of the basis curve.
    """

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the end point of the curve.
        The end point is the value of the curve for the
        "LastParameter" of the curve.
        """

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the start point of the curve.
        The start point is the value of the curve for the
        "FirstParameter" of the curve.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_BezierCurve(Geom2d_BoundedCurve):
    """
    Describes a rational or non-rational Bezier curve
    - a non-rational Bezier curve is defined by a table
    of poles (also called control points),
    - a rational Bezier curve is defined by a table of
    poles with varying weights.
    These data are manipulated by two parallel arrays:
    - the poles table, which is an array of gp_Pnt2d points, and
    - the weights table, which is an array of reals.
    The bounds of these arrays are 1 and "the number of poles" of the curve.
    The poles of the curve are "control points" used to deform the curve.
    The first pole is the start point of the curve, and the
    last pole is the end point of the curve. The segment
    which joins the first pole to the second pole is the
    tangent to the curve at its start point, and the
    segment which joins the last pole to the
    second-from-last pole is the tangent to the curve
    at its end point.
    It is more difficult to give a geometric signification
    to the weights but they are useful for providing
    exact representations of the arcs of a circle or
    ellipse. Moreover, if the weights of all the poles are
    equal, the curve is polynomial; it is therefore a
    non-rational curve. The non-rational curve is a
    special and frequently used case. The weights are
    defined and used only in case of a rational curve.
    The degree of a Bezier curve is equal to the
    number of poles, minus 1. It must be greater than or
    equal to 1. However, the degree of a
    Geom2d_BezierCurve curve is limited to a value
    (25) which is defined and controlled by the system.
    This value is returned by the function MaxDegree.
    The parameter range for a Bezier curve is [ 0, 1 ].
    If the first and last control points of the Bezier
    curve are the same point then the curve is closed.
    For example, to create a closed Bezier curve with
    four control points, you have to give a set of control
    points P1, P2, P3 and P1.
    The continuity of a Bezier curve is infinite.
    It is not possible to build a Bezier curve with
    negative weights. We consider that a weight value
    is zero if it is less than or equal to
    gp::Resolution(). We also consider that
    two weight values W1 and W2 are equal if:
    |W2 - W1| <= gp::Resolution().
    Warning
    - When considering the continuity of a closed
    Bezier curve at the junction point, remember that
    a curve of this type is never periodic. This means
    that the derivatives for the parameter u = 0
    have no reason to be the same as the
    derivatives for the parameter u = 1 even if the curve is closed.
    - The length of a Bezier curve can be null.
    """

    @overload
    def __init__(self, CurvePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        Creates a non rational Bezier curve with a set of poles :
        CurvePoles. The weights are defaulted to all being 1.
        Raises ConstructionError if the number of poles is greater than MaxDegree + 1
        or lower than 2.
        """

    @overload
    def __init__(self, theOther: Geom2d_BezierCurve) -> None:
        """Copy constructor for optimized copying without validation."""

    @overload
    def __init__(self, CurvePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], PoleWeights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Creates a rational Bezier curve with the set of poles
        CurvePoles and the set of weights PoleWeights.
        If all the weights are identical the curve is considered
        as non rational. Raises ConstructionError if the number
        of poles is greater than MaxDegree + 1 or lower than 2
        or CurvePoles and CurveWeights have not the same length
        or one weight value is lower or equal to Resolution from
        package gp.
        """

    def HasEvalRepresentation(self) -> bool:
        """Returns true if an evaluation representation is attached."""

    def EvalRepresentation(self) -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base:
        """
        Returns the current evaluation representation descriptor (may be null).
        """

    def SetEvalRepresentation(self, theDesc: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base) -> None:
        """
        Sets a new evaluation representation.
        Validates descriptor data and ensures no circular references.
        """

    def ClearEvalRepresentation(self) -> None:
        """Removes the evaluation representation."""

    def Increase(self, Degree: int) -> None:
        """
        Increases the degree of a bezier curve. Degree is the new
        degree of <me>.
        raises ConstructionError if Degree is greater than MaxDegree or lower than 2
        or lower than the initial degree of <me>.
        """

    def InsertPoleAfter(self, Index: int, P: nanoocp.gp.gp_Pnt2d, Weight: float = 1.0) -> None:
        """
        Inserts a pole with its weight in the set of poles after the
        pole of range Index. If the curve was non rational it can
        become rational if all the weights are not identical.
        Raised if Index is not in the range [0, NbPoles]

        Raised if the resulting number of poles is greater than
        MaxDegree + 1.
        """

    def InsertPoleBefore(self, Index: int, P: nanoocp.gp.gp_Pnt2d, Weight: float = 1.0) -> None:
        """
        Inserts a pole with its weight in the set of poles after
        the pole of range Index. If the curve was non rational it
        can become rational if all the weights are not identical.
        Raised if Index is not in the range [1, NbPoles+1]

        Raised if the resulting number of poles is greater than
        MaxDegree + 1.
        """

    def RemovePole(self, Index: int) -> None:
        """
        Removes the pole of range Index.
        If the curve was rational it can become non rational.
        Raised if Index is not in the range [1, NbPoles]
        """

    def Reverse(self) -> None:
        """
        Reverses the direction of parametrization of <me>
        Value (NewU) = Value (1 - OldU)
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Returns the parameter on the reversed curve for
        the point of parameter U on <me>.

        returns 1-U
        """

    def Segment(self, U1: float, U2: float) -> None:
        """
        Segments the curve between U1 and U2 which can be out
        of the bounds of the curve. The curve is oriented from U1
        to U2.
        The control points are modified, the first and the last point
        are not the same but the parametrization range is [0, 1]
        else it could not be a Bezier curve.
        Warnings:
        Even if <me> is not closed it can become closed after the
        segmentation for example if U1 or U2 are out of the bounds
        of the curve <me> or if the curve makes loop.
        After the segmentation the length of a curve can be null.
        """

    @overload
    def SetPole(self, Index: int, P: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Substitutes the pole of range index with P.
        If the curve <me> is rational the weight of range Index
        is not modified.
        raiseD if Index is not in the range [1, NbPoles]
        """

    @overload
    def SetPole(self, Index: int, P: nanoocp.gp.gp_Pnt2d, Weight: float) -> None:
        """
        Substitutes the pole and the weights of range Index.
        If the curve <me> is not rational it can become rational
        if all the weights are not identical.
        If the curve was rational it can become non rational if
        all the weights are identical.
        Raised if Index is not in the range [1, NbPoles]
        Raised if Weight <= Resolution from package gp
        """

    def SetWeight(self, Index: int, Weight: float) -> None:
        """
        Changes the weight of the pole of range Index.
        If the curve <me> is not rational it can become rational
        if all the weights are not identical.
        If the curve was rational it can become non rational if
        all the weights are identical.
        Raised if Index is not in the range [1, NbPoles]
        Raised if Weight <= Resolution from package gp
        """

    def IsClosed(self) -> bool:
        """
        Returns True if the distance between the first point
        and the last point of the curve is lower or equal to
        the Resolution from package gp.
        """

    def IsCN(self, N: int) -> bool:
        """Continuity of the curve, returns True."""

    def IsPeriodic(self) -> bool:
        """
        Returns False. A BezierCurve cannot be periodic in this
        package
        """

    def IsRational(self) -> bool:
        """
        Returns false if all the weights are identical. The tolerance
        criterion is Resolution from package gp.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN, which is the continuity of any Bezier curve."""

    def Degree(self) -> int:
        """
        Returns the polynomial degree of the curve. It is the number
        of poles less one. In this package the Degree of a Bezier
        curve cannot be greater than "MaxDegree".
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d: ...

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1: ...

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2: ...

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3: ...

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For this Bezier curve, computes
        - the point P of parameter U, or
        - the point P and one or more of the following values:
        - V1, the first derivative vector,
        - V2, the second derivative vector,
        - V3, the third derivative vector.
        Note: the parameter U can be outside the bounds of the curve.
        Raises RangeError if N < 1.
        """

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the end point or start point of this Bezier curve."""

    def FirstParameter(self) -> float:
        """
        Returns the value of the first parameter of this Bezier curve.
        This is 0.0, which gives the start point of this Bezier curve.
        """

    def LastParameter(self) -> float:
        """
        Returns the value of the last parameter of this Bezier curve.
        This is 1.0, which gives the end point of this Bezier curve.
        """

    def NbPoles(self) -> int:
        """Returns the number of poles for this Bezier curve."""

    def Pole(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the pole of range Index.
        Raised if Index is not in the range [1, NbPoles]
        """

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns all the poles of the curve."""

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns Value (U=1), it is the first control point
        of the curve.
        """

    def Weight(self, Index: int) -> float:
        """
        Returns the weight of range Index.
        Raised if Index is not in the range [1, NbPoles]
        """

    def Weights(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns all the weights of the curve."""

    def WeightsArray(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns a const reference to the weights array.
        For rational curves: the internal owning weights array.
        For non-rational curves: a non-owning view of unit weights from BSplCLib.
        The array is always sized to match NbPoles().
        @warning Do NOT modify elements through the returned reference.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this Bezier curve."""

    @staticmethod
    def MaxDegree() -> int:
        """
        Returns the value of the maximum polynomial degree of a
        BezierCurve. This value is 25.
        """

    def Resolution(self, ToleranceUV: float) -> float:
        """
        Computes for this Bezier curve the parametric
        tolerance UTolerance for a given tolerance
        Tolerance3D (relative to dimensions in the plane).
        If f(t) is the equation of this Bezier curve,
        UTolerance ensures that
        | t1 - t0| < Utolerance ===>
        |f(t1) - f(t0)| < ToleranceUV
        """

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this Bezier curve."""

    def Knots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns Bezier knots {0.0, 1.0} as a static array."""

    def Multiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Returns Bezier multiplicities for the current degree."""

    def KnotSequence(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns Bezier flat knots for the current degree."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_BSplineCurve(Geom2d_BoundedCurve):
    """
    Describes a BSpline curve.
    A BSpline curve can be:
    - uniform or non-uniform,
    - rational or non-rational,
    - periodic or non-periodic.
    A BSpline curve is defined by:
    - its degree; the degree for a
    Geom2d_BSplineCurve is limited to a value (25)
    which is defined and controlled by the system. This
    value is returned by the function MaxDegree;
    - its periodic or non-periodic nature;
    - a table of poles (also called control points), with
    their associated weights if the BSpline curve is
    rational. The poles of the curve are "control points"
    used to deform the curve. If the curve is
    non-periodic, the first pole is the start point of the
    curve, and the last pole is the end point of the
    curve. The segment, which joins the first pole to the
    second pole, is the tangent to the curve at its start
    point, and the segment, which joins the last pole to
    the second-from-last pole, is the tangent to the
    curve at its end point. If the curve is periodic, these
    geometric properties are not verified. It is more
    difficult to give a geometric signification to the
    weights but they are useful for providing exact
    representations of the arcs of a circle or ellipse.
    Moreover, if the weights of all the poles are equal,
    the curve has a polynomial equation; it is
    therefore a non-rational curve.
    - a table of knots with their multiplicities. For a
    Geom2d_BSplineCurve, the table of knots is an
    increasing sequence of reals without repetition; the
    multiplicities define the repetition of the knots. A
    BSpline curve is a piecewise polynomial or rational
    curve. The knots are the parameters of junction
    points between two pieces. The multiplicity
    Mult(i) of the knot Knot(i) of the BSpline
    curve is related to the degree of continuity of the
    curve at the knot Knot(i), which is equal to
    Degree - Mult(i) where Degree is the
    degree of the BSpline curve.
    If the knots are regularly spaced (i.e. the difference
    between two consecutive knots is a constant), three
    specific and frequently used cases of knot distribution
    can be identified:
    - "uniform" if all multiplicities are equal to 1,
    - "quasi-uniform" if all multiplicities are equal to 1,
    except the first and the last knot which have a
    multiplicity of Degree + 1, where Degree is
    the degree of the BSpline curve,
    - "Piecewise Bezier" if all multiplicities are equal to
    Degree except the first and last knot which have
    a multiplicity of Degree + 1, where Degree is
    the degree of the BSpline curve. A curve of this
    type is a concatenation of arcs of Bezier curves.
    If the BSpline curve is not periodic:
    - the bounds of the Poles and Weights tables are 1
    and NbPoles, where NbPoles is the number of
    poles of the BSpline curve,
    - the bounds of the Knots and Multiplicities tables are
    1 and NbKnots, where NbKnots is the number
    of knots of the BSpline curve.
    If the BSpline curve is periodic, and if there are k
    periodic knots and p periodic poles, the period is:
    period = Knot(k + 1) - Knot(1)
    and the poles and knots tables can be considered as
    infinite tables, such that:
    - Knot(i+k) = Knot(i) + period
    - Pole(i+p) = Pole(i)
    Note: data structures of a periodic BSpline curve are
    more complex than those of a non-periodic one.
    Warnings:
    In this class we consider that a weight value is zero if
    Weight <= Resolution from package gp.
    For two parametric values (or two knot values) U1, U2 we
    consider that U1 = U2 if Abs (U2 - U1) <= Epsilon (U1).
    For two weights values W1, W2 we consider that W1 = W2 if
    Abs (W2 - W1) <= Epsilon (W1). The method Epsilon is
    defined in the class Real from package Standard.

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
    def __init__(self, theOther: Geom2d_BSplineCurve) -> None:
        """Copy constructor for optimized copying without validation."""

    @overload
    def __init__(self, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Knots: nanoocp.NCollection.NCollection_Array1[float], Multiplicities: nanoocp.NCollection.NCollection_Array1[int], Degree: int, Periodic: bool = False) -> None:
        """
        Creates a non-rational B_spline curve on the
        basis <Knots, Multiplicities> of degree <Degree>.
        The following conditions must be verified.
        0 < Degree <= MaxDegree.

        Knots.Length() == Mults.Length() >= 2

        Knots(i) < Knots(i+1) (Knots are increasing)

        1 <= Mults(i) <= Degree

        On a non periodic curve the first and last multiplicities
        may be Degree+1 (this is even recommended if you want the
        curve to start and finish on the first and last pole).

        On a periodic curve the first and the last multicities
        must be the same.

        on non-periodic curves

        Poles.Length() == Sum(Mults(i)) - Degree - 1 >= 2

        on periodic curves

        Poles.Length() == Sum(Mults(i)) except the first or last
        """

    @overload
    def __init__(self, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], Knots: nanoocp.NCollection.NCollection_Array1[float], Multiplicities: nanoocp.NCollection.NCollection_Array1[int], Degree: int, Periodic: bool = False) -> None:
        """
        Creates a rational B_spline curve on the basis
        <Knots, Multiplicities> of degree <Degree>.
        The following conditions must be verified.
        0 < Degree <= MaxDegree.

        Knots.Length() == Mults.Length() >= 2

        Knots(i) < Knots(i+1) (Knots are increasing)

        1 <= Mults(i) <= Degree

        On a non periodic curve the first and last multiplicities
        may be Degree+1 (this is even recommended if you want the
        curve to start and finish on the first and last pole).

        On a periodic curve the first and the last multicities
        must be the same.

        on non-periodic curves

        Poles.Length() == Sum(Mults(i)) - Degree - 1 >= 2

        on periodic curves

        Poles.Length() == Sum(Mults(i)) except the first or last
        """

    def HasEvalRepresentation(self) -> bool:
        """Returns true if an evaluation representation is attached."""

    def EvalRepresentation(self) -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base:
        """
        Returns the current evaluation representation descriptor (may be null).
        """

    def SetEvalRepresentation(self, theDesc: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base) -> None:
        """
        Sets a new evaluation representation.
        Validates descriptor data and ensures no circular references.
        """

    def ClearEvalRepresentation(self) -> None:
        """Removes the evaluation representation."""

    def IncreaseDegree(self, Degree: int) -> None:
        """
        Increases the degree of this BSpline curve to
        Degree. As a result, the poles, weights and
        multiplicities tables are modified; the knots table is
        not changed. Nothing is done if Degree is less than
        or equal to the current degree.
        Exceptions
        Standard_ConstructionError if Degree is greater than
        Geom2d_BSplineCurve::MaxDegree().
        """

    @overload
    def IncreaseMultiplicity(self, Index: int, M: int) -> None:
        """
        Increases the multiplicity of the knot <Index> to
        <M>.

        If <M> is lower or equal to the current multiplicity
        nothing is done. If <M> is higher than the degree,
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
        As a result, the poles and weights tables of this curve are modified.
        Warning
        It is forbidden to modify the multiplicity of the first or
        last knot of a non-periodic curve. Be careful as
        Geom2d does not protect against this.
        Exceptions
        Standard_OutOfRange if either Index, I1 or I2 is
        outside the bounds of the knots table.
        """

    def IncrementMultiplicity(self, I1: int, I2: int, M: int) -> None:
        """
        Increases by M the multiplicity of the knots of indexes
        I1 to I2 in the knots table of this BSpline curve. For
        each knot, the resulting multiplicity is limited to the
        degree of this curve. If M is negative, nothing is done.
        As a result, the poles and weights tables of this
        BSpline curve are modified.
        Warning
        It is forbidden to modify the multiplicity of the first or
        last knot of a non-periodic curve. Be careful as
        Geom2d does not protect against this.
        Exceptions
        Standard_OutOfRange if I1 or I2 is outside the
        bounds of the knots table.
        """

    def InsertKnot(self, U: float, M: int = 1, ParametricTolerance: float = 0.0) -> None:
        """
        Inserts a knot value in the sequence of knots. If
        <U> is an existing knot the multiplicity is
        increased by <M>.

        If U is not on the parameter range nothing is
        done.

        If the multiplicity is negative or null nothing is
        done. The new multiplicity is limited to the
        degree.

        The tolerance criterion for knots equality is
        the max of Epsilon(U) and ParametricTolerance.
        Warning
        - If U is less than the first parameter or greater than
        the last parameter of this BSpline curve, nothing is done.
        - If M is negative or null, nothing is done.
        - The multiplicity of a knot is limited to the degree of
        this BSpline curve.
        """

    def InsertKnots(self, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int], ParametricTolerance: float = 0.0, Add: bool = False) -> None:
        """
        Inserts the values of the array Knots, with the
        respective multiplicities given by the array Mults, into
        the knots table of this BSpline curve.
        If a value of the array Knots is an existing knot, its multiplicity is:
        - increased by M, if Add is true, or
        - increased to M, if Add is false (default value).
        The tolerance criterion used for knot equality is the
        larger of the values ParametricTolerance (defaulted
        to 0.) and double::Epsilon(U),
        where U is the current knot value.
        Warning
        - For a value of the array Knots which is less than
        the first parameter or greater than the last
        parameter of this BSpline curve, nothing is done.
        - For a value of the array Mults which is negative or
        null, nothing is done.
        - The multiplicity of a knot is limited to the degree of
        this BSpline curve.
        """

    def RemoveKnot(self, Index: int, M: int, Tolerance: float) -> bool:
        """
        Reduces the multiplicity of the knot of index Index
        to M. If M is equal to 0, the knot is removed.
        With a modification of this type, the array of poles is also modified.
        Two different algorithms are systematically used to
        compute the new poles of the curve. If, for each
        pole, the distance between the pole calculated
        using the first algorithm and the same pole
        calculated using the second algorithm, is less than
        Tolerance, this ensures that the curve is not
        modified by more than Tolerance. Under these
        conditions, true is returned; otherwise, false is returned.
        A low tolerance is used to prevent modification of
        the curve. A high tolerance is used to "smooth" the curve.
        Exceptions
        Standard_OutOfRange if Index is outside the
        bounds of the knots table.
        """

    def InsertPoleAfter(self, Index: int, P: nanoocp.gp.gp_Pnt2d, Weight: float = 1.0) -> None:
        """
        The new pole is inserted after the pole of range Index.
        If the curve was non rational it can become rational.

        Raised if the B-spline is NonUniform or PiecewiseBezier or if
        Weight <= 0.0
        Raised if Index is not in the range [1, Number of Poles]
        """

    def InsertPoleBefore(self, Index: int, P: nanoocp.gp.gp_Pnt2d, Weight: float = 1.0) -> None:
        """
        The new pole is inserted before the pole of range Index.
        If the curve was non rational it can become rational.

        Raised if the B-spline is NonUniform or PiecewiseBezier or if
        Weight <= 0.0
        Raised if Index is not in the range [1, Number of Poles]
        """

    def RemovePole(self, Index: int) -> None:
        """
        Removes the pole of range Index
        If the curve was rational it can become non rational.

        Raised if the B-spline is NonUniform or PiecewiseBezier.
        Raised if the number of poles of the B-spline curve is lower or
        equal to 2 before removing.
        Raised if Index is not in the range [1, Number of Poles]
        """

    def Reverse(self) -> None:
        """
        Reverses the orientation of this BSpline curve. As a result
        - the knots and poles tables are modified;
        - the start point of the initial curve becomes the end
        point of the reversed curve;
        - the end point of the initial curve becomes the start
        point of the reversed curve.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed curve for
        the point of parameter U on this BSpline curve.
        The returned value is: UFirst + ULast - U,
        where UFirst and ULast are the values of the
        first and last parameters of this BSpline curve.
        """

    def Segment(self, U1: float, U2: float, theTolerance: float = 1e-09) -> None:
        """
        Modifies this BSpline curve by segmenting it
        between U1 and U2. Either of these values can be
        outside the bounds of the curve, but U2 must be greater than U1.
        All data structure tables of this BSpline curve are
        modified, but the knots located between U1 and U2
        are retained. The degree of the curve is not modified.

        Parameter theTolerance defines the possible proximity of the segment
        boundaries and B-spline knots to treat them as equal.

        Warnings:
        Even if <me> is not closed it can become closed after the
        segmentation for example if U1 or U2 are out of the bounds
        of the curve <me> or if the curve makes loop.
        After the segmentation the length of a curve can be null.
        - The segmentation of a periodic curve over an
        interval corresponding to its period generates a
        non-periodic curve with equivalent geometry.
        Exceptions
        Standard_DomainError if U2 is less than U1.
        raises if U2 < U1.
        Standard_DomainError if U2 - U1 exceeds the period for periodic curves.
        i.e. ((U2 - U1) - Period) > Precision::PConfusion().
        """

    @overload
    def SetKnot(self, Index: int, K: float) -> None:
        """
        Modifies this BSpline curve by assigning the value K
        to the knot of index Index in the knots table. This is a
        relatively local modification because K must be such that:
        Knots(Index - 1) < K < Knots(Index + 1)
        Exceptions
        Standard_ConstructionError if:
        - K is not such that:
        Knots(Index - 1) < K < Knots(Index + 1)
        - M is greater than the degree of this BSpline curve
        or lower than the previous multiplicity of knot of
        index Index in the knots table.
        Standard_OutOfRange if Index is outside the bounds of the knots table.
        """

    @overload
    def SetKnot(self, Index: int, K: float, M: int) -> None:
        """
        Modifies this BSpline curve by assigning the value K
        to the knot of index Index in the knots table. This is a
        relatively local modification because K must be such that:
        Knots(Index - 1) < K < Knots(Index + 1)
        The second syntax allows you also to increase the
        multiplicity of the knot to M (but it is not possible to
        decrease the multiplicity of the knot with this function).
        Exceptions
        Standard_ConstructionError if:
        - K is not such that:
        Knots(Index - 1) < K < Knots(Index + 1)
        - M is greater than the degree of this BSpline curve
        or lower than the previous multiplicity of knot of
        index Index in the knots table.
        Standard_OutOfRange if Index is outside the bounds of the knots table.
        """

    def SetKnots(self, K: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Modifies this BSpline curve by assigning the array
        K to its knots table. The multiplicity of the knots is not modified.
        Exceptions
        Standard_ConstructionError if the values in the
        array K are not in ascending order.
        Standard_OutOfRange if the bounds of the array
        K are not respectively 1 and the number of knots of this BSpline curve.
        """

    def PeriodicNormalization(self) -> float:
        """
        Computes the parameter normalized within the
        "first" period of this BSpline curve, if it is periodic:
        the returned value is in the range Param1 and
        Param1 + Period, where:
        - Param1 is the "first parameter", and
        - Period the period of this BSpline curve.
        Note: If this curve is not periodic, U is not modified.
        """

    def SetPeriodic(self) -> None:
        """
        Changes this BSpline curve into a periodic curve.
        To become periodic, the curve must first be closed.
        Next, the knot sequence must be periodic. For this,
        FirstUKnotIndex and LastUKnotIndex are used to
        compute I1 and I2, the indexes in the knots array
        of the knots corresponding to the first and last
        parameters of this BSpline curve.
        The period is therefore Knot(I2) - Knot(I1).
        Consequently, the knots and poles tables are modified.
        Exceptions
        Standard_ConstructionError if this BSpline curve is not closed.
        """

    def SetOrigin(self, Index: int) -> None:
        """
        Assigns the knot of index Index in the knots table as
        the origin of this periodic BSpline curve. As a
        consequence, the knots and poles tables are modified.
        Exceptions
        Standard_NoSuchObject if this curve is not periodic.
        Standard_DomainError if Index is outside the
        bounds of the knots table.
        """

    def SetNotPeriodic(self) -> None:
        """
        Changes this BSpline curve into a non-periodic
        curve. If this curve is already non-periodic, it is not modified.
        Note that the poles and knots tables are modified.
        Warning
        If this curve is periodic, as the multiplicity of the first
        and last knots is not modified, and is not equal to
        Degree + 1, where Degree is the degree of
        this BSpline curve, the start and end points of the
        curve are not its first and last poles.
        """

    @overload
    def SetPole(self, Index: int, P: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Modifies this BSpline curve by assigning P to the
        pole of index Index in the poles table.
        Exceptions
        Standard_OutOfRange if Index is outside the
        bounds of the poles table.
        Standard_ConstructionError if Weight is negative or null.
        """

    @overload
    def SetPole(self, Index: int, P: nanoocp.gp.gp_Pnt2d, Weight: float) -> None:
        """
        Modifies this BSpline curve by assigning P to the
        pole of index Index in the poles table.
        The second syntax also allows you to modify the
        weight of the modified pole, which becomes Weight.
        In this case, if this BSpline curve is non-rational, it
        can become rational and vice versa.
        Exceptions
        Standard_OutOfRange if Index is outside the
        bounds of the poles table.
        Standard_ConstructionError if Weight is negative or null.
        """

    def SetWeight(self, Index: int, Weight: float) -> None:
        """
        Assigns the weight Weight to the pole of index Index of the poles table.
        If the curve was non rational it can become rational.
        If the curve was rational it can become non rational.
        Exceptions
        Standard_OutOfRange if Index is outside the
        bounds of the poles table.
        Standard_ConstructionError if Weight is negative or null.
        """

    def MovePoint(self, U: float, P: nanoocp.gp.gp_Pnt2d, Index1: int, Index2: int) -> tuple[int, int]:
        """
        Moves the point of parameter U of this BSpline
        curve to P. Index1 and Index2 are the indexes in the
        table of poles of this BSpline curve of the first and
        last poles designated to be moved.
        FirstModifiedPole and LastModifiedPole are the
        indexes of the first and last poles, which are
        effectively modified.
        In the event of incompatibility between Index1,
        Index2 and the value U:
        - no change is made to this BSpline curve, and
        - the FirstModifiedPole and LastModifiedPole are returned null.
        Exceptions
        Standard_OutOfRange if:
        - Index1 is greater than or equal to Index2, or
        - Index1 or Index2 is less than 1 or greater than the
        number of poles of this BSpline curve.
        """

    def MovePointAndTangent(self, U: float, P: nanoocp.gp.gp_Pnt2d, Tangent: nanoocp.gp.gp_Vec2d, Tolerance: float, StartingCondition: int, EndingCondition: int) -> int:
        """
        Move a point with parameter U to P.
        and makes it tangent at U be Tangent.
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

    def IsCN(self, N: int) -> bool:
        """
        Returns true if the degree of continuity of this
        BSpline curve is at least N. A BSpline curve is at least GeomAbs_C0.
        Exceptions Standard_RangeError if N is negative.
        """

    def IsG1(self, theTf: float, theTl: float, theAngTol: float) -> bool:
        """
        Check if curve has at least G1 continuity in interval [theTf, theTl]
        Returns true if IsCN(1)
        or
        angle between "left" and "right" first derivatives at
        knots with C0 continuity is less then theAngTol
        only knots in interval [theTf, theTl] is checked
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
        """
        Returns the degree of this BSpline curve.
        In this class the degree of the basis normalized B-spline
        functions cannot be greater than "MaxDegree"
        Computation of value and derivatives
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d: ...

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """Raised if the continuity of the curve is not C1."""

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """Raised if the continuity of the curve is not C2."""

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        For this BSpline curve, computes
        - the point P of parameter U, or
        - the point P and one or more of the following values:
        - V1, the first derivative vector,
        - V2, the second derivative vector,
        - V3, the third derivative vector.
        Warning
        On a point where the continuity of the curve is not the
        one requested, these functions impact the part
        defined by the parameter with a value greater than U,
        i.e. the part of the curve to the "right" of the singularity.
        Raises UndefinedDerivative if the continuity of the curve is not C3.
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this BSpline curve,
        computes the vector corresponding to the Nth derivative.
        Warning
        On a point where the continuity of the curve is not the
        one requested, this function impacts the part defined
        by the parameter with a value greater than U, i.e. the
        part of the curve to the "right" of the singularity.
        Raises UndefinedDerivative if the continuity of the curve is not CN.
        RangeError if N < 1.
        The following functions computes the point of parameter U
        and the derivatives at this point on the B-spline curve
        arc defined between the knot FromK1 and the knot ToK2.
        U can be out of bounds [Knot (FromK1), Knot (ToK2)] but
        for the computation we only use the definition of the curve
        between these two knots. This method is useful to compute
        local derivative, if the order of continuity of the whole
        curve is not greater enough. Inside the parametric
        domain Knot (FromK1), Knot (ToK2) the evaluations are
        the same as if we consider the whole definition of the
        curve. Of course the evaluations are different outside
        this parametric domain.
        """

    def LocalValue(self, U: float, FromK1: int, ToK2: int) -> nanoocp.gp.gp_Pnt2d:
        """Raised if FromK1 = ToK2."""

    def LocalD0(self, U: float, FromK1: int, ToK2: int, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Raised if FromK1 = ToK2."""

    def LocalD1(self, U: float, FromK1: int, ToK2: int, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None:
        """
        Raised if the local continuity of the curve is not C1
        between the knot K1 and the knot K2.
        Raised if FromK1 = ToK2.
        """

    def LocalD2(self, U: float, FromK1: int, ToK2: int, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Raised if the local continuity of the curve is not C2
        between the knot K1 and the knot K2.
        Raised if FromK1 = ToK2.
        """

    def LocalD3(self, U: float, FromK1: int, ToK2: int, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Raised if the local continuity of the curve is not C3
        between the knot K1 and the knot K2.
        Raised if FromK1 = ToK2.
        """

    def LocalDN(self, U: float, FromK1: int, ToK2: int, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        Raised if the local continuity of the curve is not CN
        between the knot K1 and the knot K2.
        Raised if FromK1 = ToK2.
        Raised if N < 1.
        """

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
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

    def Knots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """returns the knot values of the B-spline curve;"""

    def KnotSequence(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns the knots sequence.
        In this sequence the knots with a multiplicity greater than 1
        are repeated.
        Example :
        K = {k1, k1, k1, k2, k3, k3, k4, k4, k4}
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
        . if I1 = I2  U is a knot value (the tolerance criterion
        ParametricTolerance is used).
        . if I1 < 1  => U < Knots (1) - std::abs(ParametricTolerance)
        . if I2 > NbKnots => U > Knots (NbKnots) + std::abs(ParametricTolerance)
        """

    def Multiplicity(self, Index: int) -> int:
        """
        Returns the multiplicity of the knots of range Index.
        Raised if Index < 1 or Index > NbKnots
        """

    def Multiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """returns the multiplicity of the knots of the curve."""

    def NbKnots(self) -> int:
        """
        Returns the number of knots. This method returns the number of
        knot without repetition of multiple knots.
        """

    def NbPoles(self) -> int:
        """Returns the number of poles"""

    def Pole(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the pole of range Index.
        Raised if Index < 1 or Index > NbPoles.
        """

    def Poles(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]:
        """Returns the poles of the B-spline curve;"""

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
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

    def Weights(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the weights of the B-spline curve;"""

    def WeightsArray(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns a const reference to the weights array.
        For rational curves: the internal owning weights array.
        For non-rational curves: a non-owning view of unit weights from BSplCLib.
        The array is always sized to match NbPoles().
        @warning Do NOT modify elements through the returned reference.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this BSpline curve."""

    @staticmethod
    def MaxDegree() -> int:
        """
        Returns the value of the maximum degree of the normalized
        B-spline basis functions in this package.
        """

    def Resolution(self, ToleranceUV: float) -> float:
        """
        Computes for this BSpline curve the parametric
        tolerance UTolerance for a given tolerance
        Tolerance3D (relative to dimensions in the plane).
        If f(t) is the equation of this BSpline curve,
        UTolerance ensures that:
        | t1 - t0| < Utolerance ===>
        |f(t1) - f(t0)| < ToleranceUV
        """

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this BSpline curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Point(Geom2d_Geometry):
    """
    The abstract class Point describes the common
    behavior of geometric points in 2D space.
    The Geom2d package also provides the concrete
    class Geom2d_CartesianPoint.
    """

    def Coord(self) -> tuple[float, float]:
        """returns the Coordinates of <me>."""

    def Pnt2d(self) -> nanoocp.gp.gp_Pnt2d:
        """returns a non persistent copy of <me>"""

    def X(self) -> float:
        """returns the X coordinate of <me>."""

    def Y(self) -> float:
        """returns the Y coordinate of <me>."""

    def Distance(self, Other: Geom2d_Point) -> float:
        """computes the distance between <me> and <Other>."""

    def SquareDistance(self, Other: Geom2d_Point) -> float:
        """computes the square distance between <me> and <Other>."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_CartesianPoint(Geom2d_Point):
    """
    Describes a point in 2D space. A
    Geom2d_CartesianPoint is defined by a gp_Pnt2d
    point, with its two Cartesian coordinates X and Y.
    """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Returns a persistent copy of P."""

    @overload
    def __init__(self, X: float, Y: float) -> None: ...

    def SetCoord(self, X: float, Y: float) -> None:
        """Set <me> to X, Y coordinates."""

    def SetPnt2d(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Set <me> to P.X(), P.Y() coordinates."""

    def SetX(self, X: float) -> None:
        """Changes the X coordinate of me."""

    def SetY(self, Y: float) -> None:
        """Changes the Y coordinate of me."""

    def Coord(self) -> tuple[float, float]:
        """Returns the coordinates of <me>."""

    def Pnt2d(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns a non persistent cartesian point with
        the same coordinates as <me>.
        -C++: return const&
        """

    def X(self) -> float:
        """Returns the X coordinate of <me>."""

    def Y(self) -> float:
        """Returns the Y coordinate of <me>."""

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None: ...

    def Copy(self) -> Geom2d_Geometry: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Conic(Geom2d_Curve):
    """
    The abstract class Conic describes the common
    behavior of conic curves in 2D space and, in
    particular, their general characteristics. The Geom2d
    package provides four specific classes of conics:
    Geom2d_Circle, Geom2d_Ellipse,
    Geom2d_Hyperbola and Geom2d_Parabola.
    A conic is positioned in the plane with a coordinate
    system (gp_Ax22d object), where the origin is the
    center of the conic (or the apex in case of a parabola).
    This coordinate system is the local coordinate
    system of the conic. It gives the conic an explicit
    orientation, determining the direction in which the
    parameter increases along the conic. The "X Axis" of
    the local coordinate system also defines the origin of
    the parameter of the conic.
    """

    def SetAxis(self, theA: nanoocp.gp.gp_Ax22d) -> None:
        """
        Modifies this conic, redefining its local coordinate system
        partially, by assigning theA as its axis
        """

    def SetXAxis(self, theAX: nanoocp.gp.gp_Ax2d) -> None:
        """
        Assigns the origin and unit vector of axis theA to the
        origin of the local coordinate system of this conic and X Direction.
        The other unit vector of the local coordinate system
        of this conic is recomputed normal to theA, without
        changing the orientation of the local coordinate
        system (right-handed or left-handed).
        """

    def SetYAxis(self, theAY: nanoocp.gp.gp_Ax2d) -> None:
        """
        Assigns the origin and unit vector of axis theA to the
        origin of the local coordinate system of this conic and Y Direction.
        The other unit vector of the local coordinate system
        of this conic is recomputed normal to theA, without
        changing the orientation of the local coordinate
        system (right-handed or left-handed).
        """

    def SetLocation(self, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Modifies this conic, redefining its local coordinate
        system partially, by assigning theP as its origin.
        """

    def XAxis(self) -> nanoocp.gp.gp_Ax2d:
        """
        Returns the "XAxis" of the conic.
        This axis defines the origin of parametrization of the conic.
        This axis and the "Yaxis" define the local coordinate system
        of the conic.
        -C++: return const&
        """

    def YAxis(self) -> nanoocp.gp.gp_Ax2d:
        """
        Returns the "YAxis" of the conic.
        The "YAxis" is perpendicular to the "Xaxis".
        """

    def Eccentricity(self) -> float:
        """
        returns the eccentricity value of the conic e.
        e = 0 for a circle
        0 < e < 1 for an ellipse (e = 0 if MajorRadius = MinorRadius)
        e > 1 for a hyperbola
        e = 1 for a parabola
        """

    def Location(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the location point of the conic.
        For the circle, the ellipse and the hyperbola it is the center of
        the conic. For the parabola it is the vertex of the parabola.
        """

    def Position(self) -> nanoocp.gp.gp_Ax22d:
        """Returns the local coordinates system of the conic."""

    def Reverse(self) -> None:
        """
        Reverses the direction of parameterization of <me>.
        The local coordinate system of the conic is modified.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Returns the parameter on the reversed curve for
        the point of parameter U on <me>.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN which is the global continuity of any conic."""

    def IsCN(self, N: int) -> bool:
        """Returns True, the order of continuity of a conic is infinite."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Circle(Geom2d_Conic):
    """
    Describes a circle in the plane (2D space).
    A circle is defined by its radius and, as with any conic
    curve, is positioned in the plane with a coordinate
    system (gp_Ax22d object) where the origin is the
    center of the circle.
    The coordinate system is the local coordinate
    system of the circle.
    The orientation (direct or indirect) of the local
    coordinate system gives an explicit orientation to the
    circle, determining the direction in which the
    parameter increases along the circle.
    The Geom2d_Circle circle is parameterized by an angle:
    P(U) = O + R*std::cos(U)*XDir + R*Sin(U)*YDir
    where:
    - P is the point of parameter U,
    - O, XDir and YDir are respectively the origin, "X
    Direction" and "Y Direction" of its local coordinate system,
    - R is the radius of the circle.
    The "X Axis" of the local coordinate system therefore
    defines the origin of the parameter of the circle. The
    parameter is the angle with this "X Direction".
    A circle is a closed and periodic curve. The period is
    2.*Pi and the parameter range is [ 0,2.*Pi [.
    See Also
    GCE2d_MakeCircle which provides functions for
    more complex circle constructions
    gp_Ax22d and gp_Circ2d for an equivalent, non-parameterized data structure.
    """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d) -> None:
        """Constructs a circle by conversion of the gp_Circ2d circle C."""

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2d, Radius: float, Sense: bool = True) -> None:
        """
        Constructs a circle of radius Radius, whose center is the origin of axis
        A; A is the "X Axis" of the local coordinate system
        of the circle; this coordinate system is direct if
        Sense is true (default value) or indirect if Sense is false.
        Note: It is possible to create a circle where Radius is equal to 0.0.
        Exceptions Standard_ConstructionError if Radius is negative.
        """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax22d, Radius: float) -> None:
        """
        Constructs a circle
        of radius Radius, where the coordinate system A
        locates the circle and defines its orientation in the plane such that:
        - the center of the circle is the origin of A,
        - the orientation (direct or indirect) of A gives the
        orientation of the circle.
        """

    def SetCirc2d(self, C: nanoocp.gp.gp_Circ2d) -> None:
        """Converts the gp_Circ2d circle C into this circle."""

    def SetRadius(self, R: float) -> None: ...

    def Circ2d(self) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the non persistent circle from gp with the same
        geometric properties as <me>.
        """

    def Radius(self) -> float:
        """Returns the radius of this circle."""

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed circle for
        the point of parameter U on this circle.
        For a circle, the returned value is: 2.*Pi - U.
        """

    def Eccentricity(self) -> float:
        """Returns 0., which is the eccentricity of any circle."""

    def FirstParameter(self) -> float:
        """Returns 0.0"""

    def LastParameter(self) -> float:
        """Returns 2*PI."""

    def IsClosed(self) -> bool:
        """returns True."""

    def IsPeriodic(self) -> bool:
        """returns True. The period of a circle is 2.*Pi."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns in P the point of parameter U.
        P = C + R * Cos (U) * XDir + R * Sin (U) * YDir
        where C is the center of the circle , XDir the XDirection and
        YDir the YDirection of the circle's local coordinate system.
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """Returns the point P of parameter U and the first derivative V1."""

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        Returns the point P of parameter u, the first second and third
        derivatives V1 V2 and V3.
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this circle, computes
        the vector corresponding to the Nth derivative.
        Exceptions: Standard_RangeError if N is less than 1.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this circle."""

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this circle."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Vector(Geom2d_Geometry):
    """
    The abstract class Vector describes the common
    behavior of vectors in 2D space.
    The Geom2d package provides two concrete
    classes of vectors: Geom2d_Direction (unit vector)
    and Geom2d_VectorWithMagnitude.
    """

    def Reverse(self) -> None:
        """Reverses the vector <me>."""

    def Reversed(self) -> Geom2d_Vector:
        """Returns a copy of <me> reversed."""

    def Angle(self, Other: Geom2d_Vector) -> float:
        """
        Computes the angular value, in radians, between this
        vector and vector Other. The result is a value
        between -Pi and Pi. The orientation is from this
        vector to vector Other.
        Raises VectorWithNullMagnitude if one of the two vectors is a vector with
        null magnitude because the angular value is indefinite.
        """

    def Coord(self) -> tuple[float, float]:
        """Returns the coordinates of <me>."""

    def Magnitude(self) -> float:
        """Returns the Magnitude of <me>."""

    def SquareMagnitude(self) -> float:
        """Returns the square magnitude of <me>."""

    def X(self) -> float:
        """Returns the X coordinate of <me>."""

    def Y(self) -> float:
        """Returns the Y coordinate of <me>."""

    def Crossed(self, Other: Geom2d_Vector) -> float:
        """Cross product of <me> with the vector <Other>."""

    def Dot(self, Other: Geom2d_Vector) -> float:
        """Returns the scalar product of 2 Vectors."""

    def Vec2d(self) -> nanoocp.gp.gp_Vec2d:
        """Returns a non persistent copy of <me>."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Direction(Geom2d_Vector):
    """
    The class Direction specifies a vector that is never null.
    It is a unit vector.
    """

    @overload
    def __init__(self, V: nanoocp.gp.gp_Dir2d) -> None:
        """Creates a persistent copy of <me>."""

    @overload
    def __init__(self, X: float, Y: float) -> None:
        """
        Creates a unit vector with it 2 cartesian coordinates.

        Raised if std::sqrt( X*X + Y*Y) <= Resolution from gp.
        """

    def SetCoord(self, X: float, Y: float) -> None:
        """
        Assigns the coordinates X and Y to this unit vector,
        then normalizes it.
        Exceptions
        Standard_ConstructionError if std::sqrt(X*X + Y*Y) is less than or equal to gp::Resolution().
        """

    def SetDir2d(self, V: nanoocp.gp.gp_Dir2d) -> None:
        """Converts the gp_Dir2d unit vector V into this unit vector."""

    def SetX(self, X: float) -> None:
        """
        Assigns a value to the X coordinate of this unit vector, then normalizes it.
        Exceptions
        Standard_ConstructionError if the value assigned
        causes the magnitude of the vector to become less
        than or equal to gp::Resolution().
        """

    def SetY(self, Y: float) -> None:
        """
        Assigns a value to the Y coordinate of this unit vector, then normalizes it.
        Exceptions
        Standard_ConstructionError if the value assigned
        causes the magnitude of the vector to become less
        than or equal to gp::Resolution().
        """

    def Dir2d(self) -> nanoocp.gp.gp_Dir2d:
        """Converts this unit vector into a gp_Dir2d unit vector."""

    def Magnitude(self) -> float:
        """returns 1.0"""

    def SquareMagnitude(self) -> float:
        """returns 1.0"""

    def Crossed(self, Other: Geom2d_Vector) -> float:
        """Computes the cross product between <me> and <Other>."""

    def __xor__(self, Other: Geom2d_Vector) -> float: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this unit vector, then normalizes it."""

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this unit vector."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Ellipse(Geom2d_Conic):
    """
    Describes an ellipse in the plane (2D space).
    An ellipse is defined by its major and minor radii and,
    as with any conic curve, is positioned in the plane
    with a coordinate system (gp_Ax22d object) where:
    - the origin is the center of the ellipse,
    - the "X Direction" defines the major axis, and
    - the "Y Direction" defines the minor axis.
    This coordinate system is the local coordinate system of the ellipse.
    The orientation (direct or indirect) of the local
    coordinate system gives an explicit orientation to the
    ellipse, determining the direction in which the
    parameter increases along the ellipse.
    The Geom2d_Ellipse ellipse is parameterized by an angle:
    P(U) = O + MajorRad*std::cos(U)*XDir + MinorRad*Sin(U)*YDir
    where:
    - P is the point of parameter U,
    - O, XDir and YDir are respectively the origin, "X
    Direction" and "Y Direction" of its local coordinate system,
    - MajorRad and MinorRad are the major and
    minor radii of the ellipse.
    The "X Axis" of the local coordinate system therefore
    defines the origin of the parameter of the ellipse.
    An ellipse is a closed and periodic curve. The period
    is 2.*Pi and the parameter range is [ 0,2.*Pi [.
    See Also
    GCE2d_MakeEllipse which provides functions for
    more complex ellipse constructions
    gp_Ax22d
    gp_Elips2d for an equivalent, non-parameterized data structure
    """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d) -> None:
        """Creates an ellipse by conversion of the gp_Elips2d ellipse E."""

    @overload
    def __init__(self, MajorAxis: nanoocp.gp.gp_Ax2d, MajorRadius: float, MinorRadius: float, Sense: bool = True) -> None:
        """
        Creates an ellipse defined by its major and minor radii,
        MajorRadius and MinorRadius, and positioned
        in the plane by its major axis MajorAxis; the
        center of the ellipse is the origin of MajorAxis
        and the unit vector of MajorAxis is the "X
        Direction" of the local coordinate system of the
        ellipse; this coordinate system is direct if Sense
        is true (default value) or indirect if Sense is false.
        Warnings :
        It is not forbidden to create an ellipse with MajorRadius =
        MinorRadius.
        Exceptions
        Standard_ConstructionError if:
        - MajorRadius is less than MinorRadius, or
        - MinorRadius is less than 0.
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float) -> None:
        """
        Creates an ellipse defined by its major and minor radii,
        MajorRadius and MinorRadius, where the
        coordinate system Axis locates the ellipse and
        defines its orientation in the plane such that:
        - the center of the ellipse is the origin of Axis,
        - the "X Direction" of Axis defines the major
        axis of the ellipse,
        - the "Y Direction" of Axis defines the minor
        axis of the ellipse,
        - the orientation of Axis (direct or indirect)
        gives the orientation of the ellipse.
        Warnings :
        It is not forbidden to create an ellipse with MajorRadius =
        MinorRadius.
        Exceptions
        Standard_ConstructionError if:
        - MajorRadius is less than MinorRadius, or
        - MinorRadius is less than 0.
        """

    def SetElips2d(self, E: nanoocp.gp.gp_Elips2d) -> None:
        """Converts the gp_Elips2d ellipse E into this ellipse."""

    def SetMajorRadius(self, MajorRadius: float) -> None:
        """
        Assigns a value to the major radius of this ellipse.
        Exceptions
        Standard_ConstructionError if:
        - the major radius of this ellipse becomes less than
        the minor radius, or
        - MinorRadius is less than 0.
        """

    def SetMinorRadius(self, MinorRadius: float) -> None:
        """
        Assigns a value to the minor radius of this ellipse.
        Exceptions
        Standard_ConstructionError if:
        - the major radius of this ellipse becomes less than
        the minor radius, or
        - MinorRadius is less than 0.
        """

    def Elips2d(self) -> nanoocp.gp.gp_Elips2d:
        """Converts this ellipse into a gp_Elips2d ellipse."""

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed ellipse for
        the point of parameter U on this ellipse.
        For an ellipse, the returned value is: 2.*Pi - U.
        """

    def Directrix1(self) -> nanoocp.gp.gp_Ax2d:
        """
        Computes the directrices of this ellipse.
        This directrix is the line normal to the XAxis of the ellipse
        in the local plane (Z = 0) at a distance d = MajorRadius / e
        from the center of the ellipse, where e is the eccentricity of
        the ellipse.
        This line is parallel to the "YAxis". The intersection point
        between directrix1 and the "XAxis" is the "Location" point
        of the directrix1. This point is on the positive side of
        the "XAxis".
        Raises ConstructionError if Eccentricity = 0.0. (The ellipse degenerates
        into a circle)
        """

    def Directrix2(self) -> nanoocp.gp.gp_Ax2d:
        """
        This line is obtained by the symmetrical transformation
        of "Directrix1" with respect to the "YAxis" of the ellipse.
        Raises ConstructionError if Eccentricity = 0.0. (The ellipse degenerates into a
        circle).
        """

    def Eccentricity(self) -> float:
        """
        Returns the eccentricity of the ellipse between 0.0 and 1.0
        If f is the distance between the center of the ellipse and
        the Focus1 then the eccentricity e = f / MajorRadius.
        Returns 0 if MajorRadius = 0
        """

    def Focal(self) -> float:
        """
        Computes the focal distance. The focal distance is the distance between the center
        and a focus of the ellipse.
        """

    def Focus1(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the first focus of the ellipse. This focus is on the
        positive side of the "XAxis" of the ellipse.
        """

    def Focus2(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the second focus of the ellipse. This focus is on
        the negative side of the "XAxis" of the ellipse.
        """

    def MajorRadius(self) -> float:
        """Returns the major radius of this ellipse."""

    def MinorRadius(self) -> float:
        """Returns the minor radius of this ellipse."""

    def Parameter(self) -> float:
        """
        Computes the parameter of this ellipse. This value is
        given by the formula p = (1 - e * e) * MajorRadius where e is the eccentricity
        of the ellipse.
        Returns 0 if MajorRadius = 0
        """

    def FirstParameter(self) -> float:
        """
        Returns the value of the first parameter of this
        ellipse. This is 0.0, which gives the start point of this ellipse.
        The start point and end point of an ellipse are coincident.
        """

    def LastParameter(self) -> float:
        """
        Returns the value of the last parameter of this
        ellipse. This is 2.*Pi, which gives the end point of this ellipse.
        The start point and end point of an ellipse are coincident.
        """

    def IsClosed(self) -> bool:
        """return True."""

    def IsPeriodic(self) -> bool:
        """return True."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns in P the point of parameter U.
        P = C + MajorRadius * Cos (U) * XDir + MinorRadius * Sin (U) * YDir
        where C is the center of the ellipse , XDir the direction of
        the "XAxis" and "YDir" the "YAxis" of the ellipse.
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1: ...

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Returns the point P of parameter U. The vectors V1 and V2
        are the first and second derivatives at this point.
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        Returns the point P of parameter U, the first second and
        third derivatives V1 V2 and V3.
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this ellipse,
        computes the vector corresponding to the Nth derivative.
        Exceptions Standard_RangeError if N is less than 1.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this ellipse."""

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this ellipse."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Hyperbola(Geom2d_Conic):
    """
    Describes a branch of a hyperbola in the plane (2D space).
    A hyperbola is defined by its major and minor radii
    and, as with any conic curve, is positioned in the
    plane with a coordinate system (gp_Ax22d object) where:
    - the origin is the center of the hyperbola,
    - the "X Direction" defines the major axis, and
    - the "Y Direction" defines the minor axis.
    This coordinate system is the local coordinate
    system of the hyperbola.
    The branch of the hyperbola described is the one
    located on the positive side of the major axis.
    The orientation (direct or indirect) of the local
    coordinate system gives an explicit orientation to the
    hyperbola, determining the direction in which the
    parameter increases along the hyperbola.
    The Geom2d_Hyperbola hyperbola is parameterized as follows:
    P(U) = O + MajRad*std::cosh(U)*XDir + MinRad*std::sinh(U)*YDir
    where:
    - P is the point of parameter U,
    - O, XDir and YDir are respectively the origin, "X
    Direction" and "Y Direction" of its local coordinate system,
    - MajRad and MinRad are the major and minor radii of the hyperbola.
    The "X Axis" of the local coordinate system therefore
    defines the origin of the parameter of the hyperbola.
    The parameter range is ] -infinite,+infinite [.
    The following diagram illustrates the respective
    positions, in the plane of the hyperbola, of the three
    branches of hyperbolas constructed using the
    functions OtherBranch, ConjugateBranch1 and
    ConjugateBranch2:
    ^YAxis
    |
    FirstConjugateBranch
    |
    Other         |          Main
    --------------------- C
    --------------------->XAxis
    Branch       |
    Branch
    |
    SecondConjugateBranch
    |
    Warning
    The value of the major radius (on the major axis) can
    be less than the value of the minor radius (on the minor axis).
    See Also
    GCE2d_MakeHyperbola which provides functions for
    more complex hyperbola constructions
    gp_Ax22d
    gp_Hypr2d for an equivalent, non-parameterized data structure
    """

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr2d) -> None:
        """Creates an Hyperbola from a non persistent one from package gp"""

    @overload
    def __init__(self, MajorAxis: nanoocp.gp.gp_Ax2d, MajorRadius: float, MinorRadius: float, Sense: bool = True) -> None:
        """
        MajorAxis is the "XAxis" of the hyperbola.
        The YAxis is in the direct sense if "Sense" is True;
        The major radius of the hyperbola is on this "XAxis" and
        the minor radius is on the "YAxis" of the hyperbola.
        Raised if MajorRadius < 0.0 or if MinorRadius < 0.0
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float) -> None:
        """
        The XDirection of "Axis" is the "XAxis" of the hyperbola and
        the YDirection of "Axis" is the "YAxis".
        The major radius of the hyperbola is on this "XAxis" and
        the minor radius is on the "YAxis" of the hyperbola.
        Raised if MajorRadius < 0.0 or if MinorRadius < 0.0
        """

    def SetHypr2d(self, H: nanoocp.gp.gp_Hypr2d) -> None:
        """Converts the gp_Hypr2d hyperbola H into this hyperbola."""

    def SetMajorRadius(self, MajorRadius: float) -> None:
        """
        Assigns a value to the major or minor radius of this hyperbola.
        Exceptions
        Standard_ConstructionError if:
        - MajorRadius is less than 0.0,
        - MinorRadius is less than 0.0.
        """

    def SetMinorRadius(self, MinorRadius: float) -> None:
        """
        Assigns a value to the major or minor radius of this hyperbola.
        Exceptions
        Standard_ConstructionError if:
        - MajorRadius is less than 0.0,
        - MinorRadius is less than 0.0.
        """

    def Hypr2d(self) -> nanoocp.gp.gp_Hypr2d:
        """Converts this hyperbola into a gp_Hypr2d one."""

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed hyperbola,
        for the point of parameter U on this hyperbola.
        For a hyperbola, the returned value is -U.
        """

    def FirstParameter(self) -> float:
        """Returns RealFirst from Standard."""

    def LastParameter(self) -> float:
        """returns RealLast from Standard."""

    def IsClosed(self) -> bool:
        """Returns False."""

    def IsPeriodic(self) -> bool:
        """return False for an hyperbola."""

    def Asymptote1(self) -> nanoocp.gp.gp_Ax2d:
        """
        In the local coordinate system of the hyperbola the
        equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0
        and the equation of the first asymptote is Y = (B/A)*X
        where A is the major radius of the hyperbola and B is the
        minor radius of the hyperbola.
        Raised if MajorRadius = 0.0
        """

    def Asymptote2(self) -> nanoocp.gp.gp_Ax2d:
        """
        In the local coordinate system of the hyperbola the
        equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0
        and the equation of the first asymptote is Y = -(B/A)*X.
        where A is the major radius of the hyperbola and B is the
        minor radius of the hyperbola.
        raised if MajorRadius = 0.0
        """

    def ConjugateBranch1(self) -> nanoocp.gp.gp_Hypr2d:
        """
        Computes the first conjugate branch relative to this hyperbola.
        Note: The diagram given under the class purpose
        indicates where these two branches of hyperbola are
        positioned in relation to this branch of hyperbola.
        """

    def ConjugateBranch2(self) -> nanoocp.gp.gp_Hypr2d:
        """
        Computes the second conjugate branch relative to this hyperbola.
        Note: The diagram given under the class purpose
        indicates where these two branches of hyperbola are
        positioned in relation to this branch of hyperbola.
        """

    def Directrix1(self) -> nanoocp.gp.gp_Ax2d:
        """
        This directrix is the line normal to the XAxis of the hyperbola
        in the local plane (Z = 0) at a distance d = MajorRadius / e
        from the center of the hyperbola, where e is the eccentricity of
        the hyperbola.
        This line is parallel to the "YAxis". The intersection point
        between directrix1 and the "XAxis" is the location point of the
        directrix1. This point is on the positive side of the "XAxis".
        """

    def Directrix2(self) -> nanoocp.gp.gp_Ax2d:
        """
        This line is obtained by the symmetrical transformation
        of "Directrix1" with respect to the "YAxis" of the hyperbola.
        """

    def Eccentricity(self) -> float:
        """
        Returns the eccentricity of the hyperbola (e > 1).
        If f is the distance between the location of the hyperbola
        and the Focus1 then the eccentricity e = f / MajorRadius.
        raised if MajorRadius = 0.0
        """

    def Focal(self) -> float:
        """
        Computes the focal distance. It is the distance between the
        two focus of the hyperbola.
        """

    def Focus1(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the first focus of the hyperbola. This focus is on the
        positive side of the "XAxis" of the hyperbola.
        """

    def Focus2(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the second focus of the hyperbola. This focus is on the
        negative side of the "XAxis" of the hyperbola.
        """

    def MajorRadius(self) -> float:
        """
        Returns the major or minor radius of this hyperbola.
        The major radius is also the distance between the
        center of the hyperbola and the apex of the main
        branch (located on the "X Axis" of the hyperbola).
        """

    def MinorRadius(self) -> float:
        """
        Returns the major or minor radius of this hyperbola.
        The minor radius is also the distance between the
        center of the hyperbola and the apex of a conjugate
        branch (located on the "Y Axis" of the hyperbola).
        """

    def OtherBranch(self) -> nanoocp.gp.gp_Hypr2d:
        """
        Computes the "other" branch of this hyperbola. This
        is a symmetrical branch with respect to the center of this hyperbola.
        Note: The diagram given under the class purpose
        indicates where the "other" branch is positioned in
        relation to this branch of the hyperbola.
        ^ YAxis
        |
        FirstConjugateBranch
        |
        Other   | Main
        ---------------------------- C
        ------------------------------------------&gtXAxis
        Branch |  Branch
        |
        |
        SecondConjugateBranch
        |
        Warning
        The major radius can be less than the minor radius.
        """

    def Parameter(self) -> float:
        """
        Computes the parameter of this hyperbola.
        The parameter is:
        p = (e*e - 1) * MajorRadius
        where e is the eccentricity of this hyperbola and
        MajorRadius its major radius.
        Exceptions
        Standard_DomainError if the major radius of this
        hyperbola is null.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns in P the point of parameter U.
        P = C + MajorRadius * std::cosh(U) * XDir +
        MinorRadius * std::sinh(U) * YDir
        where C is the center of the hyperbola , XDir the XDirection and
        YDir the YDirection of the hyperbola's local coordinate system.
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """Returns the point P of parameter U and the first derivative V1."""

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        Returns the point P of parameter U, the first second and
        third derivatives V1 V2 and V3.
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this hyperbola,
        computes the vector corresponding to the Nth derivative.
        Exceptions Standard_RangeError if N is less than 1.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this hyperbola."""

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this hyperbola."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Line(Geom2d_Curve):
    """
    Describes an infinite line in the plane (2D space).
    A line is defined and positioned in the plane with an
    axis (gp_Ax2d object) which gives it an origin and a unit vector.
    The Geom2d_Line line is parameterized as follows:
    P (U) = O + U*Dir
    where:
    - P is the point of parameter U,
    - O is the origin and Dir the unit vector of its positioning axis.
    The parameter range is ] -infinite, +infinite [.
    The orientation of the line is given by the unit vector
    of its positioning axis.
    See Also
    GCE2d_MakeLine which provides functions for more
    complex line constructions
    gp_Ax2d
    gp_Lin2d for an equivalent, non-parameterized data structure.
    """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """
        Creates a line located in 2D space with the axis placement A.
        The Location of A is the origin of the line.
        """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d) -> None:
        """Creates a line by conversion of the gp_Lin2d line L."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Dir2d) -> None:
        """
        Constructs a line passing through point P and parallel to
        vector V (P and V are, respectively, the origin
        and the unit vector of the positioning axis of the line).
        """

    def SetLin2d(self, L: nanoocp.gp.gp_Lin2d) -> None:
        """Set <me> so that <me> has the same geometric properties as L."""

    def SetDirection(self, V: nanoocp.gp.gp_Dir2d) -> None:
        """changes the direction of the line."""

    def Direction(self) -> nanoocp.gp.gp_Dir2d:
        """changes the direction of the line."""

    def SetLocation(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Changes the "Location" point (origin) of the line."""

    def Location(self) -> nanoocp.gp.gp_Pnt2d:
        """Changes the "Location" point (origin) of the line."""

    def SetPosition(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """Changes the "Location" and a the "Direction" of <me>."""

    def Position(self) -> nanoocp.gp.gp_Ax2d: ...

    def Lin2d(self) -> nanoocp.gp.gp_Lin2d:
        """
        Returns non persistent line from gp with the same geometric
        properties as <me>
        """

    def Reverse(self) -> None:
        """
        Changes the orientation of this line. As a result, the
        unit vector of the positioning axis of this line is reversed.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed line for the
        point of parameter U on this line.
        For a line, the returned value is -U.
        """

    def FirstParameter(self) -> float:
        """Returns RealFirst from Standard."""

    def LastParameter(self) -> float:
        """Returns RealLast from Standard"""

    def IsClosed(self) -> bool:
        """Returns False"""

    def IsPeriodic(self) -> bool:
        """Returns False"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_CN, which is the global continuity of any line."""

    def Distance(self, P: nanoocp.gp.gp_Pnt2d) -> float:
        """Computes the distance between <me> and the point P."""

    def IsCN(self, N: int) -> bool:
        """Returns True."""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns in P the point of parameter U.
        P (U) = O + U * Dir where O is the "Location" point of the
        line and Dir the direction of the line.
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """Returns the point P of parameter u and the first derivative V1."""

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2. V2 is a vector with null magnitude
        for a line.
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """V2 and V3 are vectors with null magnitude for a line."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this line, computes
        the vector corresponding to the Nth derivative.
        Note: if N is greater than or equal to 2, the result is a
        vector with null magnitude.
        Exceptions Standard_RangeError if N is less than 1.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this line."""

    def TransformedParameter(self, U: float, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Computes the parameter on the line transformed by
        T for the point of parameter U on this line.
        For a line, the returned value is equal to U multiplied
        by the scale factor of transformation T.
        """

    def ParametricTransformation(self, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns the coefficient required to compute the
        parametric transformation of this line when
        transformation T is applied. This coefficient is the
        ratio between the parameter of a point on this line
        and the parameter of the transformed point on the
        new line transformed by T.
        For a line, the returned value is the scale factor of the transformation T.
        """

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object, which is a copy of this line."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_OffsetCurve(Geom2d_Curve):
    """
    This class implements the basis services for the creation,
    edition, modification and evaluation of planar offset curve.
    The offset curve is obtained by offsetting by distance along
    the normal to a basis curve defined in 2D space.
    The offset curve in this package can be a self intersecting
    curve even if the basis curve does not self-intersect.
    The self intersecting portions are not deleted at the
    construction time.
    An offset curve is a curve at constant distance (Offset) from a
    basis curve and the offset curve takes its parametrization from
    the basis curve. The Offset curve is in the direction of the
    normal to the basis curve N.
    The distance offset may be positive or negative to indicate the
    preferred side of the curve :
    . distance offset >0 => the curve is in the direction of N
    . distance offset >0 => the curve is in the direction of - N
    On the Offset curve :
    Value(u) = BasisCurve.Value(U) + (Offset * (T ^ Z)) / ||T ^ Z||
    where T is the tangent vector to the basis curve and Z the
    direction of the normal vector to the plane of the curve,
    N = T ^ Z defines the offset direction and should not have
    null length.

    Warnings :
    In this package we suppose that the continuity of the offset
    curve is one degree less than the continuity of the
    basis curve and we don't check that at any point ||T^Z|| != 0.0

    So to evaluate the curve it is better to check that the offset
    curve is well defined at any point because an exception could
    be raised. The check is not done in this package at the creation
    of the offset curve because the control needs the use of an
    algorithm which cannot be implemented in this package.
    The OffsetCurve is closed if the first point and the last point
    are the same (The distance between these two points is lower or
    equal to the Resolution sea package gp) . The OffsetCurve can be
    closed even if the basis curve is not closed.
    """

    @overload
    def __init__(self, theOther: Geom2d_OffsetCurve) -> None:
        """Copy constructor for optimized copying without validation."""

    @overload
    def __init__(self, C: Geom2d_Curve, Offset: float, isNotCheckC0: bool = False) -> None:
        """
        Constructs a curve offset from the basis curve C,
        where Offset is the distance between the offset
        curve and the basis curve at any point.
        A point on the offset curve is built by measuring the
        offset value along a normal vector at a point on C.
        This normal vector is obtained by rotating the
        vector tangential to C at 90 degrees in the
        anti-trigonometric sense. The side of C on which
        the offset value is measured is indicated by this
        normal vector if Offset is positive, or in the inverse
        sense if Offset is negative.
        If isNotCheckC0 = TRUE checking if basis curve has C0-continuity
        is not made.
        Warnings :
        In this package the entities are not shared. The OffsetCurve is
        built with a copy of the curve C. So when C is modified the
        OffsetCurve is not modified
        Warning! if isNotCheckC0 = false,
        ConstructionError raised if the basis curve C is not at least C1.
        No check is done to know if ||V^Z|| != 0.0 at any point.
        """

    def HasEvalRepresentation(self) -> bool:
        """Returns true if an evaluation representation is attached."""

    def EvalRepresentation(self) -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base:
        """
        Returns the current evaluation representation descriptor (may be null).
        """

    def SetEvalRepresentation(self, theDesc: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base) -> None:
        """
        Sets a new evaluation representation.
        Validates descriptor data and ensures no circular references.
        """

    def ClearEvalRepresentation(self) -> None:
        """Removes the evaluation representation."""

    def Reverse(self) -> None:
        """
        Changes the direction of parametrization of <me>.
        As a result:
        - the basis curve is reversed,
        - the start point of the initial curve becomes the end
        point of the reversed curve,
        - the end point of the initial curve becomes the start
        point of the reversed curve, and
        - the first and last parameters are recomputed.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed curve for
        the point of parameter U on this offset curve.
        """

    def SetBasisCurve(self, C: Geom2d_Curve, isNotCheckC0: bool = False) -> None:
        """
        Changes this offset curve by assigning C as the
        basis curve from which it is built.
        If isNotCheckC0 = TRUE checking if basis curve has C0-continuity
        is not made.
        Exceptions
        if isNotCheckC0 = false,
        Standard_ConstructionError if the curve C is not at least "C1" continuous.
        """

    def SetOffsetValue(self, D: float) -> None:
        """Changes this offset curve by assigning D as the offset value."""

    def BasisCurve(self) -> Geom2d_Curve:
        """
        Returns the basis curve of this offset curve. The basis curve can be an offset curve.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Continuity of the Offset curve :
        C0 : only geometric continuity,
        C1 : continuity of the first derivative all along the Curve,
        C2 : continuity of the second derivative all along the Curve,
        C3 : continuity of the third derivative all along the Curve,
        G1 : tangency continuity all along the Curve,
        G2 : curvature continuity all along the Curve,
        CN : the order of continuity is infinite.
        Warnings :
        Returns the continuity of the basis curve - 1.
        The offset curve must have a unique normal direction defined
        at any point.
        Value and derivatives

        Warnings :
        The exception UndefinedValue or UndefinedDerivative is
        raised if it is not possible to compute a unique offset
        direction.
        If T is the first derivative with not null length and
        Z the direction normal to the plane of the curve, the
        relation ||T(U) ^ Z|| != 0 must be satisfied to evaluate
        the offset curve.
        No check is done at the creation time and we suppose
        in this package that the offset curve is well defined.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Warning! this should not be called
        if the basis curve is not at least C1. Nevertheless
        if used on portion where the curve is C1, it is OK
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """
        Warning! this should not be called
        if the continuity of the basis curve is not C2.
        Nevertheless, it's OK to use it on portion
        where the curve is C2
        """

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Warning! This should not be called
        if the continuity of the basis curve is not C3.
        Nevertheless, it's OK to use it on portion
        where the curve is C3
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        Warning! This should not be called
        if the continuity of the basis curve is not C4.
        Nevertheless, it's OK to use it on portion
        where the curve is C4
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative
        for the order of derivation N.
        Warning! this should not be called
        raises UndefunedDerivative if the continuity of the basis curve is not CN+1.
        Nevertheless, it's OK to use it on portion
        where the curve is CN+1
        raises RangeError if N < 1.
        raises NotImplemented if N > 3.
        The following functions compute the value and derivatives
        on the offset curve and returns the derivatives on the
        basis curve too.
        The computation of the value and derivatives on the basis
        curve are used to evaluate the offset curve
        Warnings :
        The exception UndefinedValue or UndefinedDerivative is
        raised if it is not possible to compute a unique offset direction.
        """

    def FirstParameter(self) -> float:
        """
        Returns the value of the first parameter of this
        offset curve. The first parameter corresponds to the
        start point of the curve.
        Note: the first and last parameters of this offset curve
        are also the ones of its basis curve.
        """

    def LastParameter(self) -> float:
        """
        Returns the value of the last parameter of this
        offset curve. The last parameter
        corresponds to the end point.
        Note: the first and last parameters of this offset curve
        are also the ones of its basis curve.
        """

    def Offset(self) -> float:
        """Returns the offset value of this offset curve."""

    def IsClosed(self) -> bool:
        """
        Returns True if the distance between the start point
        and the end point of the curve is lower or equal to
        Resolution from package gp.
        """

    def IsCN(self, N: int) -> bool:
        """
        Is the order of continuity of the curve N ?
        Warnings :
        This method answer True if the continuity of the basis curve
        is N + 1. We suppose in this class that a normal direction
        to the basis curve (used to compute the offset curve) is
        defined at any point on the basis curve.
        Raised if N < 0.
        """

    def IsPeriodic(self) -> bool:
        """
        Is the parametrization of a curve is periodic ?
        If the basis curve is a circle or an ellipse the corresponding
        OffsetCurve is periodic. If the basis curve can't be periodic
        (for example BezierCurve) the OffsetCurve can't be periodic.
        """

    def Period(self) -> float:
        """
        Returns the period of this offset curve, i.e. the period
        of the basis curve of this offset curve.
        Exceptions
        Standard_NoSuchObject if the basis curve is not periodic.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Applies the transformation T to this offset curve.
        Note: the basis curve is also modified.
        """

    def TransformedParameter(self, U: float, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns the parameter on the transformed curve for
        the transform of the point of parameter U on <me>.

        me->Transformed(T)->Value(me->TransformedParameter(U,T))

        is the same point as

        me->Value(U).Transformed(T)

        This methods calls the basis curve method.
        """

    def ParametricTransformation(self, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns a coefficient to compute the parameter on
        the transformed curve for the transform of the
        point on <me>.

        Transformed(T)->Value(U * ParametricTransformation(T))

        is the same point as

        Value(U).Transformed(T)

        This methods calls the basis curve method.
        """

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object, which is a copy of this offset curve."""

    def GetBasisCurveContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns continuity of the basis curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Parabola(Geom2d_Conic):
    """
    Describes a parabola in the plane (2D space).
    A parabola is defined by its focal length (i.e. the
    distance between its focus and its apex) and is
    positioned in the plane with a coordinate system
    (gp_Ax22d object) where:
    - the origin is the apex of the parabola, and
    - the "X Axis" defines the axis of symmetry; the
    parabola is on the positive side of this axis.
    This coordinate system is the local coordinate
    system of the parabola.
    The orientation (direct or indirect) of the local
    coordinate system gives an explicit orientation to the
    parabola, determining the direction in which the
    parameter increases along the parabola.
    The Geom_Parabola parabola is parameterized as follows:
    P(U) = O + U*U/(4.*F)*XDir + U*YDir, where:
    - P is the point of parameter U,
    - O, XDir and YDir are respectively the origin, "X
    Direction" and "Y Direction" of its local coordinate system,
    - F is the focal length of the parabola.
    The parameter of the parabola is therefore its Y
    coordinate in the local coordinate system, with the "X
    Axis" of the local coordinate system defining the
    origin of the parameter.
    The parameter range is ] -infinite,+infinite [.
    """

    @overload
    def __init__(self, Prb: nanoocp.gp.gp_Parab2d) -> None:
        """Creates a parabola from a non persistent one."""

    @overload
    def __init__(self, MirrorAxis: nanoocp.gp.gp_Ax2d, Focal: float, Sense: bool = True) -> None:
        """
        Creates a parabola with its "MirrorAxis" and it's focal
        length "Focal".
        MirrorAxis is the axis of symmetry of the curve, it is the
        "XAxis". The "YAxis" is parallel to the directrix of the
        parabola and is in the direct sense if Sense is True.
        The "Location" point of "MirrorAxis" is the vertex of the parabola
        Raised if Focal < 0.0
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax22d, Focal: float) -> None:
        """
        Creates a parabola with its Axis and it's focal
        length "Focal".
        The XDirection of Axis is the axis of symmetry of the curve,
        it is the "XAxis". The "YAxis" is parallel to the directrix of the
        parabola. The "Location" point of "Axis" is the vertex
        of the parabola.
        Raised if Focal < 0.0
        """

    @overload
    def __init__(self, D: nanoocp.gp.gp_Ax2d, F: nanoocp.gp.gp_Pnt2d) -> None:
        """
        D is the directrix of the parabola and F the focus point.
        The symmetry axis "XAxis" of the parabola is normal to the
        directrix and pass through the focus point F, but its
        "Location" point is the vertex of the parabola.
        The "YAxis" of the parabola is parallel to D and its "Location"
        point is the vertex of the parabola.
        """

    def SetFocal(self, Focal: float) -> None:
        """
        Assigns the value Focal to the focal length of this parabola.
        Exceptions Standard_ConstructionError if Focal is negative.
        """

    def SetParab2d(self, Prb: nanoocp.gp.gp_Parab2d) -> None:
        """Converts the gp_Parab2d parabola Prb into this parabola."""

    def Parab2d(self) -> nanoocp.gp.gp_Parab2d:
        """
        Returns the non persistent parabola from gp with the same
        geometric properties as <me>.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Computes the parameter on the reversed parabola
        for the point of parameter U on this parabola.
        For a parabola, the returned value is -U.
        """

    def FirstParameter(self) -> float:
        """Returns RealFirst from Standard."""

    def LastParameter(self) -> float:
        """Returns RealLast from Standard."""

    def IsClosed(self) -> bool:
        """Returns False"""

    def IsPeriodic(self) -> bool:
        """Returns False"""

    def Directrix(self) -> nanoocp.gp.gp_Ax2d:
        """
        The directrix is parallel to the "YAxis" of the parabola.
        The "Location" point of the directrix is the intersection
        point between the directrix and the symmetry axis ("XAxis") of the parabola.
        """

    def Eccentricity(self) -> float:
        """Returns the eccentricity e = 1.0"""

    def Focus(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Computes the focus of this parabola The focus is on the
        positive side of the "X Axis" of the local coordinate system of the parabola.
        """

    def Focal(self) -> float:
        """
        Computes the focal length of this parabola.
        The focal length is the distance between the apex and the focus of the parabola.
        """

    def Parameter(self) -> float:
        """
        Computes the parameter of this parabola, which is
        the distance between its focus and its directrix. This
        distance is twice the focal length.
        If P is the parameter of the parabola, the equation of
        the parabola in its local coordinate system is: Y**2 = 2.*P*X.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns in P the point of parameter U.
        If U = 0 the returned point is the origin of the XAxis and
        the YAxis of the parabola and it is the vertex of the parabola.
        P = S + F * (U * U * XDir + * U * YDir)
        where S is the vertex of the parabola, XDir the XDirection and
        YDir the YDirection of the parabola's local coordinate system.
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """Returns the point P of parameter U and the first derivative V1."""

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        """

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """
        Returns the point P of parameter U, the first second and third
        derivatives V1 V2 and V3.
        """

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this parabola,
        computes the vector corresponding to the Nth derivative.
        Exceptions Standard_RangeError if N is less than 1.
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this parabola."""

    def TransformedParameter(self, U: float, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Computes the parameter on the transformed
        parabola, for the point of parameter U on this parabola.
        For a parabola, the returned value is equal to U
        multiplied by the scale factor of transformation T.
        """

    def ParametricTransformation(self, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns a coefficient to compute the parameter on
        the transformed curve for the transform of the
        point on <me>.

        Transformed(T)->Value(U * ParametricTransformation(T))

        is the same point as

        Value(U).Transformed(T)

        This methods returns T.ScaleFactor()
        """

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object, which is a copy of this parabola."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_Transformation(nanoocp.Standard.Standard_Transient):
    """
    The class Transformation allows to create Translation,
    Rotation, Symmetry, Scaling and complex transformations
    obtained by combination of the previous elementary
    transformations.
    The Transformation class can also be used to
    construct complex transformations by combining
    these elementary transformations.
    However, these transformations can never change
    the type of an object. For example, the projection
    transformation can change a circle into an ellipse,
    and therefore change the real type of the object.
    Such a transformation is forbidden in this
    environment and cannot be a Geom2d_Transformation.
    The transformation can be represented as follows:

    V1   V2     T
    | a11  a12    a14 |   | x |      | x'|
    | a21  a22    a24 |   | y |      | y'|
    |  0    0      1  |   | 1 |      | 1 |

    where {V1, V2} defines the vectorial part of the
    transformation and T defines the translation part of
    the transformation.
    - Geom2d_Transformation transformations provide
    the same kind of "geometric" services as
    gp_Trsf2d ones but have more complex data
    structures. The geometric objects provided by the
    Geom2d package use gp_Trsf2d transformations
    in the syntaxes Transform and Transformed.
    - Geom2d_Transformation transformations are
    used in a context where they can be shared by
    several objects contained inside a common data structure.
    """

    @overload
    def __init__(self) -> None:
        """Creates an identity transformation."""

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Creates a persistent copy of T."""

    @overload
    def SetMirror(self, P: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Makes the transformation into a symmetrical transformation
        with respect to a point P.
        P is the center of the symmetry.
        """

    @overload
    def SetMirror(self, A: nanoocp.gp.gp_Ax2d) -> None:
        """
        Makes the transformation into a symmetrical transformation
        with respect to an axis A.
        A is the center of the axial symmetry.
        """

    def SetRotation(self, P: nanoocp.gp.gp_Pnt2d, Ang: float) -> None:
        """
        Assigns to this transformation the geometric
        properties of a rotation at angle Ang (in radians) about point P.
        """

    def SetScale(self, P: nanoocp.gp.gp_Pnt2d, S: float) -> None:
        """
        Makes the transformation into a scale. P is the center of
        the scale and S is the scaling value.
        """

    @overload
    def SetTransformation(self, FromSystem1: nanoocp.gp.gp_Ax2d, ToSystem2: nanoocp.gp.gp_Ax2d) -> None:
        """
        Makes a transformation allowing passage from the coordinate
        system "FromSystem1" to the coordinate system "ToSystem2".
        """

    @overload
    def SetTransformation(self, ToSystem: nanoocp.gp.gp_Ax2d) -> None:
        """
        Makes the transformation allowing passage from the basic
        coordinate system
        {P(0.,0.,0.), VX (1.,0.,0.), VY (0.,1.,0.)}
        to the local coordinate system defined with the Ax2d ToSystem.
        """

    @overload
    def SetTranslation(self, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Makes the transformation into a translation.
        V is the vector of the translation.
        """

    @overload
    def SetTranslation(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Makes the transformation into a translation from the point
        P1 to the point P2.
        """

    def SetTrsf2d(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Makes the transformation into a transformation T from
        package gp.
        """

    def IsNegative(self) -> bool:
        """
        Checks whether this transformation is an indirect
        transformation: returns true if the determinant of the
        matrix of the vectorial part of the transformation is less than 0.
        """

    def Form(self) -> nanoocp.gp.gp_TrsfForm:
        """
        Returns the nature of this transformation as a value
        of the gp_TrsfForm enumeration.
        Returns the nature of the transformation. It can be
        Identity, Rotation, Translation, PntMirror, Ax1Mirror,
        Scale, CompoundTrsf
        """

    def ScaleFactor(self) -> float:
        """Returns the scale value of the transformation."""

    def Trsf2d(self) -> nanoocp.gp.gp_Trsf2d:
        """
        Converts this transformation into a gp_Trsf2d transformation.
        Returns a non persistent copy of <me>.
        -C++: return const&
        """

    def Value(self, Row: int, Col: int) -> float:
        """
        Returns the coefficients of the global matrix of transformation.
        It is a 2 rows X 3 columns matrix.

        Raised if Row < 1 or Row > 2 or Col < 1 or Col > 2

        Computes the reverse transformation.
        """

    def Invert(self) -> None:
        """
        Computes the inverse of this transformation
        and assigns the result to this transformation.

        Raised if the transformation is singular. This means that
        the ScaleFactor is lower or equal to Resolution from
        package gp.
        """

    def Inverted(self) -> Geom2d_Transformation:
        """
        Computes the inverse of this transformation and creates a new one.
        Raises ConstructionError if the transformation is singular. This means that
        the ScaleFactor is lower or equal to Resolution from package gp.
        """

    def Multiplied(self, Other: Geom2d_Transformation) -> Geom2d_Transformation:
        """
        Computes the transformation composed with Other and <me>.
        <me> * Other.
        Returns a new transformation
        """

    def __mul__(self, Other: Geom2d_Transformation) -> Geom2d_Transformation: ...

    def Multiply(self, Other: Geom2d_Transformation) -> None:
        """
        Computes the transformation composed with Other and <me> .
        <me> = <me> * Other.

        Computes the following composition of transformations
        if N > 0  <me> * <me> * .......* <me>.
        if N = 0  Identity
        if N < 0  <me>.Invert() * .........* <me>.Invert()
        """

    def __imul__(self, Other: Geom2d_Transformation) -> Geom2d_Transformation: ...

    def Power(self, N: int) -> None:
        """Raised if N < 0 and if the transformation is not inversible"""

    def Powered(self, N: int) -> Geom2d_Transformation:
        """Raised if N < 0 and if the transformation is not inversible"""

    def PreMultiply(self, Other: Geom2d_Transformation) -> None:
        """
        Computes the matrix of the transformation composed with
        <me> and Other. <me> = Other * <me>
        """

    def Transforms(self) -> tuple[float, float]:
        """Applies the transformation <me> to the triplet {X, Y}."""

    def Copy(self) -> Geom2d_Transformation:
        """Creates a new object, which is a copy of this transformation."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_TrimmedCurve(Geom2d_BoundedCurve):
    """
    Defines a portion of a curve limited by two values of
    parameters inside the parametric domain of the curve.
    The trimmed curve is defined by:
    - the basis curve, and
    - the two parameter values which limit it.
    The trimmed curve can either have the same
    orientation as the basis curve or the opposite orientation.
    """

    def __init__(self, C: Geom2d_Curve, U1: float, U2: float, Sense: bool = True, theAdjustPeriodic: bool = True) -> None:
        """
        Creates a trimmed curve from the basis curve C limited between
        U1 and U2.

        . U1 can be greater or lower than U2.
        . The returned curve is oriented from U1 to U2.
        . If the basis curve C is periodic there is an ambiguity
        because two parts are available. In this case by default
        the trimmed curve has the same orientation as the basis
        curve (Sense = True). If Sense = False then the orientation
        of the trimmed curve is opposite to the orientation of the
        basis curve C.
        If the curve is closed but not periodic it is not possible
        to keep the part of the curve including the junction point
        (except if the junction point is at the beginning or
        at the end of the trimmed curve) because you could lose the
        fundamental characteristics of the basis curve which are
        used for example to compute the derivatives of the trimmed
        curve. So for a closed curve the rules are the same as for
        a open curve.
        Warnings :
        In this package the entities are not shared. The TrimmedCurve is
        built with a copy of the curve C. So when C is modified the
        TrimmedCurve is not modified
        Warnings :
        If <C> is periodic and <theAdjustPeriodic> is True, parametrics
        bounds of the TrimmedCurve, can be different to [<U1>;<U2>},
        if <U1> or <U2> are not in the principal period.
        Include :
        For more explanation see the scheme given with this class.
        Raises ConstructionError the C is not periodic and U1 or U2 are out of
        the bounds of C.
        Raised if U1 = U2.
        """

    def Reverse(self) -> None:
        """
        Changes the direction of parametrization of <me>. The first and
        the last parametric values are modified. The "StartPoint"
        of the initial curve becomes the "EndPoint" of the reversed
        curve and the "EndPoint" of the initial curve becomes the
        "StartPoint" of the reversed curve.
        Example  -   If the trimmed curve is defined by:
        - a basis curve whose parameter range is [ 0.,1. ], and
        - the two trim values U1 (first parameter) and U2 (last parameter),
        the reversed trimmed curve is defined by:
        - the reversed basis curve, whose parameter range is still [ 0.,1. ], and
        - the two trim values 1. - U2 (first parameter)
        and 1. - U1 (last parameter).
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Returns the parameter on the reversed curve for
        the point of parameter U on <me>.

        returns UFirst + ULast - U
        """

    def SetTrim(self, U1: float, U2: float, Sense: bool = True, theAdjustPeriodic: bool = True) -> None:
        """
        Changes this trimmed curve, by redefining the
        parameter values U1 and U2, which limit its basis curve.
        Note: If the basis curve is periodic, the trimmed curve
        has the same orientation as the basis curve if Sense
        is true (default value) or the opposite orientation if Sense is false.
        Warning
        If the basis curve is periodic and theAdjustPeriodic is True,
        the bounds of the trimmed curve may be different from U1 and U2 if the
        parametric origin of the basis curve is within the arc
        of the trimmed curve. In this case, the modified
        parameter will be equal to U1 or U2 plus or minus the period.
        If theAdjustPeriodic is False, parameters U1 and U2 will stay unchanged.
        Exceptions
        Standard_ConstructionError if:
        - the basis curve is not periodic, and either U1 or U2
        are outside the bounds of the basis curve, or
        - U1 is equal to U2.
        """

    def BasisCurve(self) -> Geom2d_Curve:
        """
        Returns the basis curve.
        Warning
        This function does not return a constant reference.
        Consequently, any modification of the returned value
        directly modifies the trimmed curve.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the global continuity of the basis curve of this trimmed curve.
        C0 : only geometric continuity,
        C1 : continuity of the first derivative all along the Curve,
        C2 : continuity of the second derivative all along the Curve,
        C3 : continuity of the third derivative all along the Curve,
        CN : the order of continuity is infinite.
        """

    def IsCN(self, N: int) -> bool:
        """
        --- Purpose
        Returns True if the order of continuity of the
        trimmed curve is N. A trimmed curve is at least "C0" continuous.
        Warnings :
        The continuity of the trimmed curve can be greater than
        the continuity of the basis curve because you consider
        only a part of the basis curve.
        Raised if N < 0.
        """

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the end point of <me>. This point is the
        evaluation of the curve for the "LastParameter".
        """

    def FirstParameter(self) -> float:
        """
        Returns the value of the first parameter of <me>.
        The first parameter is the parameter of the "StartPoint"
        of the trimmed curve.
        """

    def IsClosed(self) -> bool:
        """
        Returns TRUE if the basis curve is periodic and the trim spans
        exactly one full period, or if the distance between the StartPoint
        and the EndPoint is within computational precision.
        """

    def IsPeriodic(self) -> bool:
        """
        Returns TRUE if the basis curve is periodic and the trim
        spans exactly one full period. Returns FALSE otherwise.
        """

    def Period(self) -> float:
        """
        Returns the period of the basis curve of this trimmed curve.
        Exceptions
        Standard_NoSuchObject if the basis curve is not periodic.
        """

    def LastParameter(self) -> float:
        """
        Returns the value of the last parameter of <me>.
        The last parameter is the parameter of the "EndPoint" of the
        trimmed curve.
        """

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the start point of <me>.
        This point is the evaluation of the curve from the
        "FirstParameter".
        value and derivatives
        Warnings :
        The returned derivatives have the same orientation as the
        derivatives of the basis curve.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        If the basis curve is an OffsetCurve sometimes it is not
        possible to do the evaluation of the curve at the parameter
        U (see class OffsetCurve).
        """

    def EvalD1(self, U: float) -> Geom2d_Curve.ResD1:
        """Raised if the continuity of the curve is not C1."""

    def EvalD2(self, U: float) -> Geom2d_Curve.ResD2:
        """Raised if the continuity of the curve is not C2."""

    def EvalD3(self, U: float) -> Geom2d_Curve.ResD3:
        """Raised if the continuity of the curve is not C3."""

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        For the point of parameter U of this trimmed curve,
        computes the vector corresponding to the Nth derivative.
        Warning
        The returned derivative vector has the same
        orientation as the derivative vector of the basis curve,
        even if the trimmed curve does not have the same
        orientation as the basis curve.
        Exceptions
        Standard_RangeError if N is less than 1.
        geometric transformations
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Applies the transformation T to this trimmed curve.
        Warning The basis curve is also modified.
        """

    def TransformedParameter(self, U: float, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns the parameter on the transformed curve for
        the transform of the point of parameter U on <me>.

        me->Transformed(T)->Value(me->TransformedParameter(U,T))

        is the same point as

        me->Value(U).Transformed(T)

        This methods calls the basis curve method.
        """

    def ParametricTransformation(self, T: nanoocp.gp.gp_Trsf2d) -> float:
        """
        Returns a coefficient to compute the parameter on
        the transformed curve for the transform of the
        point on <me>.

        Transformed(T)->Value(U * ParametricTransformation(T))

        is the same point as

        Value(U).Transformed(T)

        This methods calls the basis curve method.
        """

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object, which is a copy of this trimmed curve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Geom2d_VectorWithMagnitude(Geom2d_Vector):
    """
    Defines a vector with magnitude.
    A vector with magnitude can have a zero length.
    """

    @overload
    def __init__(self, V: nanoocp.gp.gp_Vec2d) -> None:
        """Creates a persistent copy of V."""

    @overload
    def __init__(self, X: float, Y: float) -> None:
        """Creates a vector with two cartesian coordinates."""

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creates a vector from the point P1 to the point P2.
        The magnitude of the vector is the distance between P1 and P2
        """

    def SetCoord(self, X: float, Y: float) -> None:
        """Set <me> to X, Y coordinates."""

    def SetVec2d(self, V: nanoocp.gp.gp_Vec2d) -> None: ...

    def SetX(self, X: float) -> None:
        """Changes the X coordinate of <me>."""

    def SetY(self, Y: float) -> None:
        """Changes the Y coordinate of <me>"""

    def Magnitude(self) -> float:
        """Returns the magnitude of <me>."""

    def SquareMagnitude(self) -> float:
        """Returns the square magnitude of <me>."""

    def Add(self, Other: Geom2d_Vector) -> None:
        """Adds the Vector Other to <me>."""

    def __iadd__(self, Other: Geom2d_Vector) -> Geom2d_VectorWithMagnitude: ...

    def Added(self, Other: Geom2d_Vector) -> Geom2d_VectorWithMagnitude:
        """Adds the vector Other to <me>."""

    def __add__(self, Other: Geom2d_Vector) -> Geom2d_VectorWithMagnitude: ...

    def Crossed(self, Other: Geom2d_Vector) -> float:
        """
        Computes the cross product between <me> and Other
        <me> ^ Other. A new vector is returned.
        """

    def __xor__(self, Other: Geom2d_Vector) -> float: ...

    def Divide(self, Scalar: float) -> None:
        """Divides <me> by a scalar."""

    def __itruediv__(self, Scalar: float) -> Geom2d_VectorWithMagnitude: ...

    def Divided(self, Scalar: float) -> Geom2d_VectorWithMagnitude:
        """Divides <me> by a scalar. A new vector is returned."""

    def __truediv__(self, Scalar: float) -> Geom2d_VectorWithMagnitude: ...

    def Multiplied(self, Scalar: float) -> Geom2d_VectorWithMagnitude:
        """
        Computes the product of the vector <me> by a scalar.
        A new vector is returned.

        -C++: alias operator *
        Collision with same operator defined for the class Vector!
        """

    def Multiply(self, Scalar: float) -> None:
        """Computes the product of the vector <me> by a scalar."""

    def __imul__(self, Scalar: float) -> Geom2d_VectorWithMagnitude: ...

    def Normalize(self) -> None:
        """
        Normalizes <me>.

        Raised if the magnitude of the vector is lower or equal to
        Resolution from package gp.
        """

    def Normalized(self) -> Geom2d_VectorWithMagnitude:
        """
        Returns a copy of <me> Normalized.

        Raised if the magnitude of the vector is lower or equal to
        Resolution from package gp.
        """

    def Subtract(self, Other: Geom2d_Vector) -> None:
        """Subtracts the Vector Other to <me>."""

    def __isub__(self, Other: Geom2d_Vector) -> Geom2d_VectorWithMagnitude: ...

    def Subtracted(self, Other: Geom2d_Vector) -> Geom2d_VectorWithMagnitude:
        """Subtracts the vector Other to <me>. A new vector is returned."""

    def __sub__(self, Other: Geom2d_Vector) -> Geom2d_VectorWithMagnitude: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """Applies the transformation T to this vector."""

    def Copy(self) -> Geom2d_Geometry:
        """Creates a new object which is a copy of this vector."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
