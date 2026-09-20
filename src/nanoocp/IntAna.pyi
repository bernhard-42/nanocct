"""OCCT package IntAna (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.gp


class IntAna_ResultType(enum.IntEnum):
    IntAna_Point = 0

    IntAna_Line = 1

    IntAna_Circle = 2

    IntAna_PointAndCircle = 3

    IntAna_Ellipse = 4

    IntAna_Parabola = 5

    IntAna_Hyperbola = 6

    IntAna_Empty = 7

    IntAna_Same = 8

    IntAna_NoGeometricSolution = 9

class IntAna_Curve:
    """
    Definition of a parametric Curve which is the result
    of the intersection between two quadrics.
    """

    def __init__(self) -> None:
        """Empty Constructor"""

    def SetCylinderQuadValues(self, Cylinder: nanoocp.gp.gp_Cylinder, Qxx: float, Qyy: float, Qzz: float, Qxy: float, Qxz: float, Qyz: float, Qx: float, Qy: float, Qz: float, Q1: float, Tol: float, DomInf: float, DomSup: float, TwoZForATheta: bool, ZIsPositive: bool) -> None:
        """
        Sets the parameters used to compute Points and Derivative
        on the curve.
        """

    def SetConeQuadValues(self, Cone: nanoocp.gp.gp_Cone, Qxx: float, Qyy: float, Qzz: float, Qxy: float, Qxz: float, Qyz: float, Qx: float, Qy: float, Qz: float, Q1: float, Tol: float, DomInf: float, DomSup: float, TwoZForATheta: bool, ZIsPositive: bool) -> None:
        """
        Sets the parameters used to compute Points and
        Derivative on the curve.
        """

    def IsOpen(self) -> bool:
        """
        Returns TRUE if the curve is not infinite at the
        last parameter or at the first parameter of the domain.
        """

    def Domain(self) -> tuple[float, float]:
        """Returns the parametric domain of the curve."""

    def IsConstant(self) -> bool:
        """Returns TRUE if the function is constant."""

    def IsFirstOpen(self) -> bool:
        """Returns TRUE if the domain is open at the beginning."""

    def IsLastOpen(self) -> bool:
        """Returns TRUE if the domain is open at the end."""

    def Value(self, Theta: float) -> nanoocp.gp.gp_Pnt:
        """Returns the point at parameter Theta on the curve."""

    def D1u(self, Theta: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> bool:
        """
        Returns the point and the first derivative at parameter
        Theta on the curve.
        """

    def FindParameter(self, P: nanoocp.gp.gp_Pnt, theParams: nanoocp.NCollection.NCollection_List[float]) -> None:
        """
        Tries to find the parameter of the point P on the curve.
        If the method returns False, the "projection" is
        impossible.
        If the method returns True at least one parameter has been found.
        theParams is always sorted in ascending order.
        """

    def SetIsFirstOpen(self, Flag: bool) -> None:
        """
        If flag is True, the Curve is not defined at the
        first parameter of its domain.
        """

    def SetIsLastOpen(self, Flag: bool) -> None:
        """
        If flag is True, the Curve is not defined at the
        first parameter of its domain.
        """

    def SetDomain(self, theFirst: float, theLast: float) -> None:
        """Trims this curve"""

class IntAna_Int3Pln:
    """
    Intersection between 3 planes. The algorithm searches
    for an intersection point. If two of the planes are
    parallel or identical, IsEmpty returns TRUE.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pln, P2: nanoocp.gp.gp_Pln, P3: nanoocp.gp.gp_Pln) -> None:
        """
        Determination of the intersection point between
        3 planes.
        """

    def Perform(self, P1: nanoocp.gp.gp_Pln, P2: nanoocp.gp.gp_Pln, P3: nanoocp.gp.gp_Pln) -> None:
        """
        Determination of the intersection point between
        3 planes.
        """

    def IsDone(self) -> bool:
        """Returns True if the computation was successful."""

    def IsEmpty(self) -> bool:
        """
        Returns TRUE if there is no intersection POINT.
        If 2 planes are identical or parallel, IsEmpty
        will return TRUE.
        """

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the intersection point."""

class IntAna_IntConicQuad:
    """
    This class provides the analytic intersection between
    a conic defined as an element of gp (Lin,Circ,Elips,
    Parab,Hypr) and a quadric as defined in the class
    Quadric from IntAna.
    The intersection between a conic and a plane is treated
    as a special case.

    The result of the intersection are points (Pnt from
    gp), associated with the parameter on the conic.

    A call to an Intersection L:Lin from gp and
    SPH: Sphere from gp can be written either:
    IntAna_IntConicQuad Inter(L,IntAna_Quadric(SPH))
    or:
    IntAna_IntConicQuad Inter(L,SPH) (it is necessary
    to include IntAna_Quadric.hxx in this case)
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, Q: IntAna_Quadric) -> None:
        """Creates the intersection between a line and a quadric."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, Q: IntAna_Quadric) -> None:
        """Creates the intersection between a circle and a quadric."""

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips, Q: IntAna_Quadric) -> None:
        """Creates the intersection between an ellipse and a quadric."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab, Q: IntAna_Quadric) -> None:
        """Creates the intersection between a parabola and a quadric."""

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr, Q: IntAna_Quadric) -> None:
        """
        Creates the intersection between an hyperbola and
        a quadric.
        """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, P: nanoocp.gp.gp_Pln, Tolang: float, Tol: float = 0.0, Len: float = 0.0) -> None:
        """
        Intersection between a line and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        Tol is used to check the distance between line and plane
        on the distance <Len> from the origin of the line.
        """

    @overload
    def __init__(self, Pb: nanoocp.gp.gp_Parab, P: nanoocp.gp.gp_Pln, Tolang: float) -> None:
        """
        Intersection between a parabola and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        """

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr, P: nanoocp.gp.gp_Pln, Tolang: float) -> None:
        """
        Intersection between an hyperbola and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, P: nanoocp.gp.gp_Pln, Tolang: float, Tol: float) -> None:
        """
        Intersection between a circle and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        Tol is used to determine if a distance is null.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips, P: nanoocp.gp.gp_Pln, Tolang: float, Tol: float) -> None:
        """
        Intersection between an ellipse and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        Tol is used to determine if a distance is null.
        """

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin, Q: IntAna_Quadric) -> None:
        """Intersects a line and a quadric."""

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, Q: IntAna_Quadric) -> None:
        """Intersects a circle and a quadric."""

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips, Q: IntAna_Quadric) -> None:
        """Intersects an ellipse and a quadric."""

    @overload
    def Perform(self, P: nanoocp.gp.gp_Parab, Q: IntAna_Quadric) -> None:
        """Intersects a parabola and a quadric."""

    @overload
    def Perform(self, H: nanoocp.gp.gp_Hypr, Q: IntAna_Quadric) -> None:
        """Intersects an hyperbola and a quadric."""

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin, P: nanoocp.gp.gp_Pln, Tolang: float, Tol: float = 0.0, Len: float = 0.0) -> None:
        """
        Intersects a line and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        Tol is used to check the distance between line and plane
        on the distance <Len> from the origin of the line.
        """

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, P: nanoocp.gp.gp_Pln, Tolang: float, Tol: float) -> None:
        """
        Intersects a circle and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        Tol is used to determine if a distance is null.
        """

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips, P: nanoocp.gp.gp_Pln, Tolang: float, Tol: float) -> None:
        """
        Intersects an ellipse and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        Tol is used to determine if a distance is null.
        """

    @overload
    def Perform(self, Pb: nanoocp.gp.gp_Parab, P: nanoocp.gp.gp_Pln, Tolang: float) -> None:
        """
        Intersects a parabola and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        """

    @overload
    def Perform(self, H: nanoocp.gp.gp_Hypr, P: nanoocp.gp.gp_Pln, Tolang: float) -> None:
        """
        Intersects an hyperbola and a plane.
        Tolang is used to determine if the angle between two
        vectors is null.
        """

    def IsDone(self) -> bool:
        """Returns TRUE if the creation completed."""

    def IsInQuadric(self) -> bool:
        """Returns TRUE if the conic is in the quadric."""

    def IsParallel(self) -> bool:
        """
        Returns TRUE if the line is in a quadric which
        is parallel to the quadric.
        """

    def NbPoints(self) -> int:
        """Returns the number of intersection point."""

    def Point(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the point of range N."""

    def ParamOnConic(self, N: int) -> float:
        """
        Returns the parameter on the line of the intersection
        point of range N.
        """

class IntAna_IntLinTorus:
    """Intersection between a line and a torus."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, T: nanoocp.gp.gp_Torus) -> None:
        """Creates the intersection between a line and a torus."""

    def Perform(self, L: nanoocp.gp.gp_Lin, T: nanoocp.gp.gp_Torus) -> None:
        """Intersects a line and a torus."""

    def IsDone(self) -> bool:
        """Returns True if the computation was successful."""

    def NbPoints(self) -> int:
        """Returns the number of intersection points."""

    def Value(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """Returns the intersection point of range Index."""

    def ParamOnLine(self, Index: int) -> float:
        """
        Returns the parameter on the line of the intersection
        point of range Index.
        """

    def ParamOnTorus(self, Index: int) -> tuple[float, float]:
        """
        Returns the parameters on the torus of the intersection
        point of range Index.
        """

class IntAna_IntQuadQuad:
    """
    This class provides the analytic intersection between a
    cylinder or a cone from gp and another quadric, as defined
    in the class Quadric from IntAna.
    This algorithm is used when the geometric intersection
    (class QuadQuadGeo from IntAna) returns no geometric
    solution.
    The result of the intersection may be
    - Curves as defined in the class Curve from IntAna
    - Points (Pnt from gp)
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder, Q: IntAna_Quadric, Tol: float) -> None:
        """
        Creates the intersection between a cylinder and a quadric.
        Tol est a definir plus precisemment.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, Q: IntAna_Quadric, Tol: float) -> None:
        """
        Creates the intersection between a cone and a quadric.
        Tol est a definir plus precisemment.
        """

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cylinder, Q: IntAna_Quadric, Tol: float) -> None:
        """
        Intersects a cylinder and a quadric .
        Tol est a definir plus precisemment.
        """

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cone, Q: IntAna_Quadric, Tol: float) -> None:
        """
        Intersects a cone and a quadric.
        Tol est a definir plus precisemment.
        """

    def IsDone(self) -> bool:
        """Returns True if the computation was successful."""

    def IdenticalElements(self) -> bool:
        """
        Returns TRUE if the cylinder, the cone or the sphere
        is identical to the quadric.
        """

    def NbCurve(self) -> int:
        """Returns the number of curves solution."""

    def Curve(self, N: int) -> IntAna_Curve:
        """Returns the curve of range N."""

    def NbPnt(self) -> int:
        """Returns the number of contact point."""

    def Point(self, N: int) -> nanoocp.gp.gp_Pnt:
        """Returns the point of range N."""

    def Parameters(self, N: int) -> tuple[float, float]:
        """
        Returns the parameters on the "explicit quadric"
        (i.e. the cylinder or the cone, the first argument given to the constructor)
        of the point of range N.
        """

    def HasNextCurve(self, I: int) -> bool:
        """
        Returns True if the Curve I shares its last bound
        with another curve.
        """

    def NextCurve(self, I: int) -> tuple[int, bool]:
        """
        If HasNextCurve(I) returns True, this function
        returns the Index J of the curve which has a
        common bound with the curve I. If theOpposite ==
        True, then the last parameter of the curve I, and
        the last parameter of the curve J give the same
        point. Else the last parameter of the curve I and
        the first parameter of the curve J are the same
        point.
        """

    def HasPreviousCurve(self, I: int) -> bool:
        """
        Returns True if the Curve I shares its first bound
        with another curve.
        """

    def PreviousCurve(self, I: int) -> tuple[int, bool]:
        """
        if HasPreviousCurve(I) returns True, this function
        returns the Index J of the curve which has a common
        bound with the curve I. If theOpposite == True
        then the first parameter of the curve I, and the
        first parameter of the curve J give the same
        point. Else the first parameter of the curve I and
        the last parameter of the curve J are the same
        point.
        """

class IntAna_QuadQuadGeo:
    """
    Geometric intersections between two natural quadrics
    (Sphere , Cylinder , Cone , Pln from gp).
    The possible intersections are :
    - 1 point
    - 1 or 2 line(s)
    - 1 Point and 1 Line
    - 1 circle
    - 1 ellipse
    - 1 parabola
    - 1 or 2 hyperbola(s).
    - Empty : there is no intersection between the two quadrics.
    - Same  : the quadrics are identical
    - NoGeometricSolution : there may be an intersection, but it
    is necessary to use an analytic algorithm to determine
    it. See class IntQuadQuad from IntAna.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, S: nanoocp.gp.gp_Sphere) -> None:
        """Creates the intersection between a plane and a sphere."""

    @overload
    def __init__(self, Cyl1: nanoocp.gp.gp_Cylinder, Cyl2: nanoocp.gp.gp_Cylinder, Tol: float) -> None:
        """Creates the intersection between two cylinders."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, Sph: nanoocp.gp.gp_Sphere, Tol: float) -> None:
        """Creates the intersection between a Cylinder and a Sphere."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, Con: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """Creates the intersection between a Cylinder and a Cone"""

    @overload
    def __init__(self, Sph1: nanoocp.gp.gp_Sphere, Sph2: nanoocp.gp.gp_Sphere, Tol: float) -> None:
        """Creates the intersection between two Spheres."""

    @overload
    def __init__(self, Sph: nanoocp.gp.gp_Sphere, Con: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """Creates the intersection between a Sphere and a Cone."""

    @overload
    def __init__(self, Con1: nanoocp.gp.gp_Cone, Con2: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """Creates the intersection between two cones."""

    @overload
    def __init__(self, Pln: nanoocp.gp.gp_Pln, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Creates the intersection between plane and torus."""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Creates the intersection between cylinder and torus."""

    @overload
    def __init__(self, Con: nanoocp.gp.gp_Cone, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Creates the intersection between cone and torus."""

    @overload
    def __init__(self, Sph: nanoocp.gp.gp_Sphere, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Creates the intersection between sphere and torus."""

    @overload
    def __init__(self, Tor1: nanoocp.gp.gp_Torus, Tor2: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Creates the intersection between two toruses."""

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pln, P2: nanoocp.gp.gp_Pln, TolAng: float, Tol: float) -> None:
        """
        Creates the intersection between two planes.
        TolAng is the angular tolerance used to determine
        if the planes are parallel.
        Tol is the tolerance used to determine if the planes
        are identical (only when they are parallel).
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, C: nanoocp.gp.gp_Cylinder, Tolang: float, Tol: float, H: float = 0.0) -> None:
        """
        Creates the intersection between a plane and a cylinder.
        TolAng is the angular tolerance used to determine
        if the axis of the cylinder is parallel to the plane.
        Tol is the tolerance used to determine if the result
        is a circle or an ellipse. If the maximum distance between
        the ellipse solution and the circle centered at the ellipse
        center is less than Tol, the result will be the circle.
        H is the height of the cylinder <Cyl>. It is used to check
        whether the plane and cylinder are parallel.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, C: nanoocp.gp.gp_Cone, Tolang: float, Tol: float) -> None:
        """
        Creates the intersection between a plane and a cone.
        TolAng is the angular tolerance used to determine
        if the axis of the cone is parallel or perpendicular
        to the plane, and if the generating line of the cone
        is parallel to the plane.
        Tol is the tolerance used to determine if the apex
        of the cone is in the plane.
        """

    @overload
    def Perform(self, P1: nanoocp.gp.gp_Pln, P2: nanoocp.gp.gp_Pln, TolAng: float, Tol: float) -> None:
        """
        Intersects two planes.
        TolAng is the angular tolerance used to determine
        if the planes are parallel.
        Tol is the tolerance used to determine if the planes
        are identical (only when they are parallel).
        """

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pln, C: nanoocp.gp.gp_Cylinder, Tolang: float, Tol: float, H: float = 0.0) -> None:
        """
        Intersects a plane and a cylinder.
        TolAng is the angular tolerance used to determine
        if the axis of the cylinder is parallel to the plane.
        Tol is the tolerance used to determine if the result
        is a circle or an ellipse. If the maximum distance between
        the ellipse solution and the circle centered at the ellipse
        center is less than Tol, the result will be the circle.
        H is the height of the cylinder <Cyl>. It is used to check
        whether the plane and cylinder are parallel.
        """

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pln, S: nanoocp.gp.gp_Sphere) -> None:
        """Intersects a plane and a sphere."""

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pln, C: nanoocp.gp.gp_Cone, Tolang: float, Tol: float) -> None:
        """
        Intersects a plane and a cone.
        TolAng is the angular tolerance used to determine
        if the axis of the cone is parallel or perpendicular
        to the plane, and if the generating line of the cone
        is parallel to the plane.
        Tol is the tolerance used to determine if the apex
        of the cone is in the plane.
        """

    @overload
    def Perform(self, Cyl1: nanoocp.gp.gp_Cylinder, Cyl2: nanoocp.gp.gp_Cylinder, Tol: float) -> None:
        """Intersects two cylinders"""

    @overload
    def Perform(self, Cyl: nanoocp.gp.gp_Cylinder, Sph: nanoocp.gp.gp_Sphere, Tol: float) -> None:
        """Intersects a cylinder and a sphere."""

    @overload
    def Perform(self, Cyl: nanoocp.gp.gp_Cylinder, Con: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """Intersects a cylinder and a cone."""

    @overload
    def Perform(self, Sph1: nanoocp.gp.gp_Sphere, Sph2: nanoocp.gp.gp_Sphere, Tol: float) -> None:
        """Intersects a two spheres."""

    @overload
    def Perform(self, Sph: nanoocp.gp.gp_Sphere, Con: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """Intersects a sphere and a cone."""

    @overload
    def Perform(self, Con1: nanoocp.gp.gp_Cone, Con2: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """Intersects two cones."""

    @overload
    def Perform(self, Pln: nanoocp.gp.gp_Pln, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Intersects plane and torus."""

    @overload
    def Perform(self, Cyl: nanoocp.gp.gp_Cylinder, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Intersects cylinder and torus."""

    @overload
    def Perform(self, Con: nanoocp.gp.gp_Cone, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Intersects cone and torus."""

    @overload
    def Perform(self, Sph: nanoocp.gp.gp_Sphere, Tor: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Intersects sphere and torus."""

    @overload
    def Perform(self, Tor1: nanoocp.gp.gp_Torus, Tor2: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """Intersects two toruses."""

    def IsDone(self) -> bool:
        """Returns true if the computation was successful."""

    def TypeInter(self) -> IntAna_ResultType:
        """Returns the type of intersection."""

    def NbSolutions(self) -> int:
        """
        Returns the number of intersections.
        The possible intersections are :
        - 1 point
        - 1 or 2 line(s)
        - 1 Point and 1 Line
        - 1 circle
        - 1 ellipse
        - 1 parabola
        - 1 or 2 hyperbola(s).
        """

    def Point(self, Num: int) -> nanoocp.gp.gp_Pnt:
        """Returns the point solution of range Num."""

    def Line(self, Num: int) -> nanoocp.gp.gp_Lin:
        """Returns the line solution of range Num."""

    def Circle(self, Num: int) -> nanoocp.gp.gp_Circ:
        """Returns the circle solution of range Num."""

    def Ellipse(self, Num: int) -> nanoocp.gp.gp_Elips:
        """Returns the ellipse solution of range Num."""

    def Parabola(self, Num: int) -> nanoocp.gp.gp_Parab:
        """Returns the parabola solution of range Num."""

    def Hyperbola(self, Num: int) -> nanoocp.gp.gp_Hypr:
        """Returns the hyperbola solution of range Num."""

    def HasCommonGen(self) -> bool: ...

    def PChar(self) -> nanoocp.gp.gp_Pnt: ...

class IntAna_Quadric:
    """
    This class provides a description of Quadrics by their
    Coefficients in natural coordinate system.
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln) -> None:
        """Creates a Quadric from a Pln"""

    @overload
    def __init__(self, Sph: nanoocp.gp.gp_Sphere) -> None:
        """Creates a Quadric from a Sphere"""

    @overload
    def __init__(self, Cyl: nanoocp.gp.gp_Cylinder) -> None:
        """Creates a Quadric from a Cylinder"""

    @overload
    def __init__(self, Cone: nanoocp.gp.gp_Cone) -> None:
        """Creates a Quadric from a Cone"""

    @overload
    def SetQuadric(self, P: nanoocp.gp.gp_Pln) -> None:
        """Initializes the quadric with a Pln"""

    @overload
    def SetQuadric(self, Sph: nanoocp.gp.gp_Sphere) -> None:
        """Initialize the quadric with a Sphere"""

    @overload
    def SetQuadric(self, Con: nanoocp.gp.gp_Cone) -> None:
        """Initializes the quadric with a Cone"""

    @overload
    def SetQuadric(self, Cyl: nanoocp.gp.gp_Cylinder) -> None:
        """Initializes the quadric with a Cylinder"""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Returns the coefficients of the polynomial equation
        which define the quadric:
        xCXX x**2 + xCYY y**2 + xCZZ z**2
        + 2 ( xCXY x y  + xCXZ x z  + xCYZ y z  )
        + 2 ( xCX x + xCY y + xCZ z )
        + xCCte
        """

    def NewCoefficients(self, Axis: nanoocp.gp.gp_Ax3) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Returns the coefficients of the polynomial equation
        ( written in the natural coordinates system )
        in the local coordinates system defined by Axis
        """

    def SpecialPoints(self) -> nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt]:
        """Returns the list of special points (with singularities)"""
