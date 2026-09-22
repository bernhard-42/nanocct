"""OCCT package GeomToStep (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.NCollection
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.gp


class GeomToStep_Root:
    """
    This class implements the common services for
    all classes of GeomToStep which report error.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_Root) -> None: ...

    def IsDone(self) -> bool: ...

class GeomToStep_MakeAxis1Placement(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Axis1Placement from Geom and Ax1 from gp, and the class
    Axis1Placement from StepGeom which describes an
    Axis1Placement from Prostep.
    """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax1, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2d, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.Geom.Geom_Axis1Placement | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.Geom2d.Geom2d_AxisPlacement | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeAxis1Placement) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Axis1Placement: ...

class GeomToStep_MakeAxis2Placement2d(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Axis2Placement from Geom and Ax2, Ax22d from gp, and the class
    Axis2Placement2d from StepGeom which describes an
    axis2_placement_2d from Prostep.
    """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax22d, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeAxis2Placement2d) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement2d: ...

class GeomToStep_MakeAxis2Placement3d(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Axis2Placement from Geom and Ax2, Ax3 from gp, and the class
    Axis2Placement3d from StepGeom which describes an
    axis2_placement_3d from Prostep.
    """

    @overload
    def __init__(self, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax3, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, A: nanoocp.Geom.Geom_Axis2Placement | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeAxis2Placement3d) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d: ...

class GeomToStep_MakeBoundedCurve(GeomToStep_Root):
    """
    This class implements the mapping between classes
    BoundedCurve from Geom, Geom2d and the class BoundedCurve from
    StepGeom which describes a BoundedCurve from prostep.
    As BoundedCurve is an abstract BoundedCurve this class
    is an access to the sub-class required.
    """

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_BoundedCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_BoundedCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeBoundedCurve) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_BoundedCurve: ...

class GeomToStep_MakeBoundedSurface(GeomToStep_Root):
    """
    This class implements the mapping between classes
    BoundedSurface from Geom and the class BoundedSurface from
    StepGeom which describes a BoundedSurface from prostep.
    As BoundedSurface is an abstract BoundedSurface this class
    is an access to the sub-class required.
    """

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_BoundedSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeBoundedSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_BoundedSurface: ...

class GeomToStep_MakeBSplineCurveWithKnots(GeomToStep_Root):
    """
    This class implements the mapping between classes
    BSplineCurve from Geom, Geom2d and the class
    BSplineCurveWithKnots from StepGeom
    which describes a bspline_curve_with_knots from
    Prostep
    """

    @overload
    def __init__(self, Bsplin: nanoocp.Geom.Geom_BSplineCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, Bsplin: nanoocp.Geom2d.Geom2d_BSplineCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeBSplineCurveWithKnots) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_BSplineCurveWithKnots: ...

class GeomToStep_MakeBSplineCurveWithKnotsAndRationalBSplineCurve(GeomToStep_Root):
    """
    This class implements the mapping between classes
    BSplineCurve from Geom, Geom2d and the class
    BSplineCurveWithKnotsAndRationalBSplineCurve from StepGeom
    which describes a rational_bspline_curve_with_knots from
    Prostep
    """

    @overload
    def __init__(self, Bsplin: nanoocp.Geom.Geom_BSplineCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, Bsplin: nanoocp.Geom2d.Geom2d_BSplineCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeBSplineCurveWithKnotsAndRationalBSplineCurve) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve: ...

class GeomToStep_MakeBSplineSurfaceWithKnots(GeomToStep_Root):
    """
    This class implements the mapping between class
    BSplineSurface from Geom and the class
    BSplineSurfaceWithKnots from
    StepGeom which describes a
    bspline_Surface_with_knots from Prostep
    """

    @overload
    def __init__(self, Bsplin: nanoocp.Geom.Geom_BSplineSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeBSplineSurfaceWithKnots) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_BSplineSurfaceWithKnots: ...

class GeomToStep_MakeBSplineSurfaceWithKnotsAndRationalBSplineSurface(GeomToStep_Root):
    """
    This class implements the mapping between class
    BSplineSurface from Geom and the class
    BSplineSurfaceWithKnotsAndRationalBSplineSurface from
    StepGeom which describes a
    rational_bspline_Surface_with_knots from Prostep
    """

    @overload
    def __init__(self, Bsplin: nanoocp.Geom.Geom_BSplineSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeBSplineSurfaceWithKnotsAndRationalBSplineSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface: ...

class GeomToStep_MakeCartesianPoint(GeomToStep_Root):
    """
    This class implements the mapping between classes
    CartesianPoint from Geom and Pnt from gp, and the class
    CartesianPoint from StepGeom which describes a point from
    Prostep.
    """

    @overload
    def __init__(self, P: nanoocp.Geom2d.Geom2d_CartesianPoint | None) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, aFactor: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, aFactor: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.Geom.Geom_CartesianPoint | None, aFactor: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeCartesianPoint) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_CartesianPoint: ...

class GeomToStep_MakeCartesianTransformationOperator(GeomToStep_Root):
    """
    This class creates a cartesian_transformation_operator from gp_Trsf.
    This entity is used in OCCT to implement a transformation with scaling.
    In case of other inputs without scaling use Axis2Placement3d.
    """

    @overload
    def __init__(self, theTrsf: nanoocp.gp.gp_Trsf, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None:
        """
        Main constructor.
        @param[in] theTrsf Transformation to create the operator from it.
        @param[in] theLocalFactors Unit scale factors
        """

    @overload
    def __init__(self, theOther: GeomToStep_MakeCartesianTransformationOperator) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d:
        """
        Returns the created entity.
        @return The created value.
        """

class GeomToStep_MakeCircle(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Circle from Geom, and Circ from gp, and the class
    Circle from StepGeom which describes a circle from
    Prostep.
    """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Circle | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Circle | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeCircle) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Circle: ...

class GeomToStep_MakeConic(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Conic from Geom and the class Conic from StepGeom
    which describes a Conic from prostep. As Conic is an abstract
    Conic this class is an access to the sub-class required.
    """

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Conic | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Conic | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeConic) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Conic: ...

class GeomToStep_MakeConicalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class
    ConicalSurface from Geom and the class
    ConicalSurface from StepGeom which describes a
    conical_surface from Prostep
    """

    @overload
    def __init__(self, CSurf: nanoocp.Geom.Geom_ConicalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeConicalSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_ConicalSurface: ...

class GeomToStep_MakeCurve(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Curve from Geom and the class Curve from StepGeom which
    describes a Curve from prostep. As Curve is an
    abstract curve this class an access to the sub-class required.
    """

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Curve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeCurve) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Curve: ...

class GeomToStep_MakeCylindricalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class
    CylindricalSurface from Geom and the class
    CylindricalSurface from StepGeom which describes a
    cylindrical_surface from Prostep
    """

    @overload
    def __init__(self, CSurf: nanoocp.Geom.Geom_CylindricalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeCylindricalSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_CylindricalSurface: ...

class GeomToStep_MakeDirection(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Direction from Geom, Geom2d and Dir, Dir2d from gp, and the
    class Direction from StepGeom which describes a direction
    from Prostep.
    """

    @overload
    def __init__(self, D: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def __init__(self, D: nanoocp.gp.gp_Dir2d) -> None: ...

    @overload
    def __init__(self, D: nanoocp.Geom.Geom_Direction | None) -> None: ...

    @overload
    def __init__(self, D: nanoocp.Geom2d.Geom2d_Direction | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeDirection) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Direction: ...

class GeomToStep_MakeElementarySurface(GeomToStep_Root):
    """
    This class implements the mapping between classes
    ElementarySurface from Geom and the class ElementarySurface
    from StepGeom which describes a ElementarySurface from
    prostep. As ElementarySurface is an abstract Surface this
    class is an access to the sub-class required.
    """

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_ElementarySurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeElementarySurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_ElementarySurface: ...

class GeomToStep_MakeEllipse(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Ellipse from Geom, and Circ from gp, and the class
    Ellipse from StepGeom which describes a Ellipse from
    Prostep.
    """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Elips, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Ellipse | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Ellipse | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeEllipse) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Ellipse: ...

class GeomToStep_MakeHyperbola(GeomToStep_Root):
    """
    This class implements the mapping between the class
    Hyperbola from Geom and the class Hyperbola from
    StepGeom which describes a Hyperbola from ProSTEP
    """

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Hyperbola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Hyperbola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeHyperbola) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Hyperbola: ...

class GeomToStep_MakeLine(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Line from Geom and Lin from gp, and the class
    Line from StepGeom which describes a line from
    Prostep.
    """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Line | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Line | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeLine) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Line: ...

class GeomToStep_MakeParabola(GeomToStep_Root):
    """
    This class implements the mapping between the class
    Parabola from Geom and the class Parabola from
    StepGeom which describes a Parabola from ProSTEP
    """

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Parabola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Parabola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeParabola) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Parabola: ...

class GeomToStep_MakePlane(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Plane from Geom and Pln from gp, and the class
    Plane from StepGeom which describes a plane from
    Prostep.
    """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, P: nanoocp.Geom.Geom_Plane | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakePlane) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Plane: ...

class GeomToStep_MakePolyline(GeomToStep_Root):
    """
    This class implements the mapping between an Array1 of points
    from gp and a Polyline from StepGeom.
    """

    @overload
    def __init__(self, P: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, P: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakePolyline) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Polyline: ...

class GeomToStep_MakeRectangularTrimmedSurface(GeomToStep_Root):
    """
    This class implements the mapping between class
    RectangularTrimmedSurface from Geom and the class
    RectangularTrimmedSurface from
    StepGeom which describes a
    rectangular_trimmed_surface from ISO-IS 10303-42
    """

    @overload
    def __init__(self, RTSurf: nanoocp.Geom.Geom_RectangularTrimmedSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeRectangularTrimmedSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface: ...

class GeomToStep_MakeSphericalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class
    SphericalSurface from Geom and the class
    SphericalSurface from StepGeom which describes a
    spherical_surface from Prostep
    """

    @overload
    def __init__(self, CSurf: nanoocp.Geom.Geom_SphericalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeSphericalSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_SphericalSurface: ...

class GeomToStep_MakeSurface(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Surface from Geom and the class Surface from StepGeom which
    describes a Surface from prostep. As Surface is an abstract
    Surface this class is an access to the sub-class required.
    """

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Surface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Surface: ...

class GeomToStep_MakeSurfaceOfLinearExtrusion(GeomToStep_Root):
    """
    This class implements the mapping between class
    SurfaceOfLinearExtrusion from Geom and the class
    SurfaceOfLinearExtrusion from StepGeom which describes a
    surface_of_linear_extrusion from Prostep
    """

    @overload
    def __init__(self, CSurf: nanoocp.Geom.Geom_SurfaceOfLinearExtrusion | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeSurfaceOfLinearExtrusion) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_SurfaceOfLinearExtrusion: ...

class GeomToStep_MakeSurfaceOfRevolution(GeomToStep_Root):
    """
    This class implements the mapping between class
    SurfaceOfRevolution from Geom and the class
    SurfaceOfRevolution from StepGeom which describes a
    surface_of_revolution from Prostep
    """

    @overload
    def __init__(self, RevSurf: nanoocp.Geom.Geom_SurfaceOfRevolution | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeSurfaceOfRevolution) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_SurfaceOfRevolution: ...

class GeomToStep_MakeSweptSurface(GeomToStep_Root):
    """
    This class implements the mapping between classes
    SweptSurface from Geom and the class SweptSurface from
    StepGeom which describes a SweptSurface from prostep.
    As SweptSurface is an abstract SweptSurface this class
    is an access to the sub-class required.
    """

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_SweptSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeSweptSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_SweptSurface: ...

class GeomToStep_MakeToroidalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class
    ToroidalSurface from Geom and the class
    ToroidalSurface from StepGeom which describes a
    toroidal_surface from Prostep
    """

    @overload
    def __init__(self, TorSurf: nanoocp.Geom.Geom_ToroidalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeToroidalSurface) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_ToroidalSurface: ...

class GeomToStep_MakeVector(GeomToStep_Root):
    """
    This class implements the mapping between classes
    Vector from Geom, Geom2d and Vec, Vec2d from gp, and the class
    Vector from StepGeom which describes a Vector from
    Prostep.
    """

    @overload
    def __init__(self, V: nanoocp.gp.gp_Vec, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, V: nanoocp.gp.gp_Vec2d, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, V: nanoocp.Geom.Geom_Vector | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, V: nanoocp.Geom2d.Geom2d_Vector | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomToStep_MakeVector) -> None: ...

    def Value(self) -> nanoocp.StepGeom.StepGeom_Vector: ...
