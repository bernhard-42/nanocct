"""OCCT package StepToGeom (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.NCollection
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepKinematics
import nanoocp.StepRepr
import nanoocp.gp


class StepToGeom:
    """
    This class provides static methods to convert STEP geometric entities to OCCT.
    The methods returning handles will return null handle in case of error.
    The methods returning boolean will return True if succeeded and False if error.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToGeom) -> None: ...

    @staticmethod
    def MakeAxis1Placement(SA: nanoocp.StepGeom.StepGeom_Axis1Placement | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Axis1Placement: ...

    @overload
    @staticmethod
    def MakeAxis2Placement(SA: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Axis2Placement: ...

    @overload
    @staticmethod
    def MakeAxis2Placement(SP: nanoocp.StepGeom.StepGeom_SuParameters | None) -> nanoocp.Geom.Geom_Axis2Placement: ...

    @staticmethod
    def MakeAxisPlacement(SA: nanoocp.StepGeom.StepGeom_Axis2Placement2d | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_AxisPlacement: ...

    @staticmethod
    def MakeBoundedCurve(SC: nanoocp.StepGeom.StepGeom_BoundedCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_BoundedCurve: ...

    @staticmethod
    def MakeBoundedCurve2d(SC: nanoocp.StepGeom.StepGeom_BoundedCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_BoundedCurve: ...

    @staticmethod
    def MakeBoundedSurface(SS: nanoocp.StepGeom.StepGeom_BoundedSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_BoundedSurface: ...

    @staticmethod
    def MakeBSplineCurve(SC: nanoocp.StepGeom.StepGeom_BSplineCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @staticmethod
    def MakeBSplineCurve2d(SC: nanoocp.StepGeom.StepGeom_BSplineCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @staticmethod
    def MakeBSplineSurface(SS: nanoocp.StepGeom.StepGeom_BSplineSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_BSplineSurface: ...

    @staticmethod
    def MakeCartesianPoint(SP: nanoocp.StepGeom.StepGeom_CartesianPoint | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_CartesianPoint: ...

    @staticmethod
    def MakeCartesianPoint2d(SP: nanoocp.StepGeom.StepGeom_CartesianPoint | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_CartesianPoint: ...

    @staticmethod
    def MakeCircle(SC: nanoocp.StepGeom.StepGeom_Circle | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Circle: ...

    @staticmethod
    def MakeCircle2d(SC: nanoocp.StepGeom.StepGeom_Circle | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Circle: ...

    @staticmethod
    def MakeConic(SC: nanoocp.StepGeom.StepGeom_Conic | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Conic: ...

    @staticmethod
    def MakeConic2d(SC: nanoocp.StepGeom.StepGeom_Conic | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Conic: ...

    @staticmethod
    def MakeConicalSurface(SS: nanoocp.StepGeom.StepGeom_ConicalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_ConicalSurface: ...

    @staticmethod
    def MakeCurve(SC: nanoocp.StepGeom.StepGeom_Curve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Curve: ...

    @staticmethod
    def MakeCurve2d(SC: nanoocp.StepGeom.StepGeom_Curve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @staticmethod
    def MakeCylindricalSurface(SS: nanoocp.StepGeom.StepGeom_CylindricalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_CylindricalSurface: ...

    @staticmethod
    def MakeDirection(SD: nanoocp.StepGeom.StepGeom_Direction | None) -> nanoocp.Geom.Geom_Direction: ...

    @staticmethod
    def MakeDirection2d(SD: nanoocp.StepGeom.StepGeom_Direction | None) -> nanoocp.Geom2d.Geom2d_Direction: ...

    @staticmethod
    def MakeElementarySurface(SS: nanoocp.StepGeom.StepGeom_ElementarySurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_ElementarySurface: ...

    @staticmethod
    def MakeEllipse(SC: nanoocp.StepGeom.StepGeom_Ellipse | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Ellipse: ...

    @staticmethod
    def MakeEllipse2d(SC: nanoocp.StepGeom.StepGeom_Ellipse | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Ellipse: ...

    @staticmethod
    def MakeHyperbola(SC: nanoocp.StepGeom.StepGeom_Hyperbola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Hyperbola: ...

    @staticmethod
    def MakeHyperbola2d(SC: nanoocp.StepGeom.StepGeom_Hyperbola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Hyperbola: ...

    @staticmethod
    def MakeLine(SC: nanoocp.StepGeom.StepGeom_Line | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Line: ...

    @staticmethod
    def MakeLine2d(SC: nanoocp.StepGeom.StepGeom_Line | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Line: ...

    @staticmethod
    def MakeParabola(SC: nanoocp.StepGeom.StepGeom_Parabola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Parabola: ...

    @staticmethod
    def MakeParabola2d(SC: nanoocp.StepGeom.StepGeom_Parabola | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Parabola: ...

    @staticmethod
    def MakePlane(SP: nanoocp.StepGeom.StepGeom_Plane | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Plane: ...

    @staticmethod
    def MakePolyline(SPL: nanoocp.StepGeom.StepGeom_Polyline | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @staticmethod
    def MakePolyline2d(SPL: nanoocp.StepGeom.StepGeom_Polyline | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @staticmethod
    def MakeRectangularTrimmedSurface(SS: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_RectangularTrimmedSurface: ...

    @staticmethod
    def MakeSphericalSurface(SS: nanoocp.StepGeom.StepGeom_SphericalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_SphericalSurface: ...

    @staticmethod
    def MakeSurface(SS: nanoocp.StepGeom.StepGeom_Surface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_Surface: ...

    @staticmethod
    def MakeSurfaceOfLinearExtrusion(SS: nanoocp.StepGeom.StepGeom_SurfaceOfLinearExtrusion | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_SurfaceOfLinearExtrusion: ...

    @staticmethod
    def MakeSurfaceOfRevolution(SS: nanoocp.StepGeom.StepGeom_SurfaceOfRevolution | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_SurfaceOfRevolution: ...

    @staticmethod
    def MakeSweptSurface(SS: nanoocp.StepGeom.StepGeom_SweptSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_SweptSurface: ...

    @staticmethod
    def MakeToroidalSurface(SS: nanoocp.StepGeom.StepGeom_ToroidalSurface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_ToroidalSurface: ...

    @staticmethod
    def MakeTransformation2d(SCTO: nanoocp.StepGeom.StepGeom_CartesianTransformationOperator2d | None, CT: nanoocp.gp.gp_Trsf2d, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool: ...

    @staticmethod
    def MakeTransformation3d(SCTO: nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d | None, CT: nanoocp.gp.gp_Trsf, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool: ...

    @staticmethod
    def MakeTrimmedCurve(SC: nanoocp.StepGeom.StepGeom_TrimmedCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_TrimmedCurve: ...

    @staticmethod
    def MakeTrimmedCurve2d(SC: nanoocp.StepGeom.StepGeom_TrimmedCurve | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @staticmethod
    def MakeVectorWithMagnitude(SV: nanoocp.StepGeom.StepGeom_Vector | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom.Geom_VectorWithMagnitude: ...

    @staticmethod
    def MakeVectorWithMagnitude2d(SV: nanoocp.StepGeom.StepGeom_Vector | None) -> nanoocp.Geom2d.Geom2d_VectorWithMagnitude: ...

    @staticmethod
    def MakeYprRotation(SR: nanoocp.StepKinematics.StepKinematics_SpatialRotation, theCntxt: nanoocp.StepRepr.StepRepr_GlobalUnitAssignedContext | None) -> nanoocp.NCollection.NCollection_HArray1[float]: ...
