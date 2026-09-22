"""OCCT package GeomToIGES (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.Geom
import nanoocp.IGESData
import nanoocp.IGESGeom


class GeomToIGES_GeomEntity:
    """provides methods to transfer Geom entity from CASCADE to IGES."""

    @overload
    def __init__(self) -> None:
        """Creates a tool GeomEntity"""

    @overload
    def __init__(self, GE: GeomToIGES_GeomEntity) -> None:
        """
        Creates a tool ready to run and sets its
        fields as GE's.
        """

    def SetModel(self, model: nanoocp.IGESData.IGESData_IGESModel | None) -> None:
        """Set the value of "TheModel\""""

    def GetModel(self) -> nanoocp.IGESData.IGESData_IGESModel:
        """Returns the value of "TheModel\""""

    def SetUnit(self, unit: float) -> None:
        """Sets the value of the UnitFlag"""

    def GetUnit(self) -> float:
        """
        Returns the value of the UnitFlag of the header of the model
        in meters.
        """

class GeomToIGES_GeomCurve(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Curve Entity from Geom
    To IGES. These can be:
    Curve
    . BoundedCurve
    * BSplineCurve
    * BezierCurve
    * TrimmedCurve
    . Conic
    * Circle
    * Ellipse
    * Hyperbloa
    * Line
    * Parabola
    . OffsetCurve
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, GE: GeomToIGES_GeomEntity) -> None:
        """
        Creates a tool GeomCurve ready to run and sets its
        fields as GE's.
        """

    @overload
    def __init__(self, theOther: GeomToIGES_GeomCurve) -> None: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Curve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a GeometryEntity which answer True to the
        member : BRepToIGES::IsGeomCurve(Geometry). If this
        Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_BoundedCurve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_BSplineCurve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_BezierCurve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_TrimmedCurve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Conic | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Circle | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Ellipse | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Hyperbola | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Line | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_Parabola | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferCurve(self, start: nanoocp.Geom.Geom_OffsetCurve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

class GeomToIGES_GeomPoint(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Point Entity from Geom
    to IGES. These are:
    . Point
    * CartesianPoint
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, GE: GeomToIGES_GeomEntity) -> None:
        """
        Creates a tool GeomPoint ready to run and sets its
        fields as GE's.
        """

    @overload
    def __init__(self, theOther: GeomToIGES_GeomPoint) -> None: ...

    @overload
    def TransferPoint(self, start: nanoocp.Geom.Geom_Point | None) -> nanoocp.IGESGeom.IGESGeom_Point:
        """
        Transfer a Point from Geom to IGES. If this
        Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def TransferPoint(self, start: nanoocp.Geom.Geom_CartesianPoint | None) -> nanoocp.IGESGeom.IGESGeom_Point:
        """
        Transfer a CartesianPoint from Geom to IGES. If this
        Entity could not be converted, this member returns a NullEntity.
        """

class GeomToIGES_GeomSurface(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Surface Entity from Geom
    To IGES. These can be:
    . BoundedSurface
    * BSplineSurface
    * BezierSurface
    * RectangularTrimmedSurface
    . ElementarySurface
    * Plane
    * CylindricalSurface
    * ConicalSurface
    * SphericalSurface
    * ToroidalSurface
    . SweptSurface
    * SurfaceOfLinearExtrusion
    * SurfaceOfRevolution
    . OffsetSurface
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, GE: GeomToIGES_GeomEntity) -> None:
        """
        Creates a tool GeomSurface ready to run and sets its
        fields as GE's.
        """

    @overload
    def __init__(self, theOther: GeomToIGES_GeomSurface) -> None: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_Surface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a GeometryEntity which answer True to the
        member : BRepToIGES::IsGeomSurface(Geometry). If this
        Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_BoundedSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_BSplineSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_BezierSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_RectangularTrimmedSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_ElementarySurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_Plane | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_CylindricalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_ConicalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_SphericalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_ToroidalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_SweptSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_SurfaceOfLinearExtrusion | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_SurfaceOfRevolution | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferSurface(self, start: nanoocp.Geom.Geom_OffsetSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    def TransferPlaneSurface(self, start: nanoocp.Geom.Geom_Plane | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    def TransferCylindricalSurface(self, start: nanoocp.Geom.Geom_CylindricalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    def TransferConicalSurface(self, start: nanoocp.Geom.Geom_ConicalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    def TransferSphericalSurface(self, start: nanoocp.Geom.Geom_SphericalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    def TransferToroidalSurface(self, start: nanoocp.Geom.Geom_ToroidalSurface | None, Udeb: float, Ufin: float, Vdeb: float, Vfin: float) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    def Length(self) -> float:
        """Returns the value of "TheLength\""""

    def GetBRepMode(self) -> bool:
        """Returns Brep mode flag."""

    def SetBRepMode(self, flag: bool) -> None:
        """Sets BRep mode flag."""

    def GetAnalyticMode(self) -> bool:
        """Returns flag for writing elementary surfaces"""

    def SetAnalyticMode(self, flag: bool) -> None:
        """Setst flag for writing elementary surfaces"""

class GeomToIGES_GeomVector(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Vector from Geom
    to IGES. These can be:
    . Vector
    * Direction
    * VectorWithMagnitude
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, GE: GeomToIGES_GeomEntity) -> None:
        """
        Creates a tool GeomVector ready to run and sets its
        fields as GE's.
        """

    @overload
    def __init__(self, theOther: GeomToIGES_GeomVector) -> None: ...

    @overload
    def TransferVector(self, start: nanoocp.Geom.Geom_Vector | None) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        Transfer a GeometryEntity which answer True to the
        member : BRepToIGES::IsGeomVector(Geometry). If this
        Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def TransferVector(self, start: nanoocp.Geom.Geom_VectorWithMagnitude | None) -> nanoocp.IGESGeom.IGESGeom_Direction: ...

    @overload
    def TransferVector(self, start: nanoocp.Geom.Geom_Direction | None) -> nanoocp.IGESGeom.IGESGeom_Direction: ...
