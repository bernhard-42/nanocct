"""OCCT package Geom2dToIGES (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.Geom2d
import nanoocp.IGESData
import nanoocp.IGESGeom


class Geom2dToIGES_Geom2dEntity:
    """provides methods to transfer Geom2d entity from CASCADE to IGES."""

    @overload
    def __init__(self) -> None:
        """Creates a tool Geom2dEntity"""

    @overload
    def __init__(self, GE: Geom2dToIGES_Geom2dEntity) -> None:
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
        in millimeters.
        """

class Geom2dToIGES_Geom2dCurve(Geom2dToIGES_Geom2dEntity):
    """
    This class implements the transfer of the Curve Entity from Geom2d
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
    def __init__(self, G2dE: Geom2dToIGES_Geom2dEntity) -> None:
        """
        Creates a tool Geom2dCurve ready to run and sets its
        fields as G2dE's.
        """

    @overload
    def __init__(self, theOther: Geom2dToIGES_Geom2dCurve) -> None: ...

    def Transfer2dCurve(self, start: nanoocp.Geom2d.Geom2d_Curve | None, Udeb: float, Ufin: float) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an Entity from Geom2d to IGES. If this
        Entity could not be converted, this member returns a NullEntity.
        """

class Geom2dToIGES_Geom2dPoint(Geom2dToIGES_Geom2dEntity):
    """
    This class implements the transfer of the Point Entity from Geom2d
    to IGES. These are:
    . 2dPoint
    * 2dCartesianPoint
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, G2dE: Geom2dToIGES_Geom2dEntity) -> None:
        """
        Creates a tool Geom2dPoint ready to run and sets its
        fields as G2dE's.
        """

    @overload
    def __init__(self, theOther: Geom2dToIGES_Geom2dPoint) -> None: ...

    @overload
    def Transfer2dPoint(self, start: nanoocp.Geom2d.Geom2d_Point | None) -> nanoocp.IGESGeom.IGESGeom_Point:
        """
        Transfer a Point from Geom to IGES. If this
        Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def Transfer2dPoint(self, start: nanoocp.Geom2d.Geom2d_CartesianPoint | None) -> nanoocp.IGESGeom.IGESGeom_Point:
        """
        Transfer a CartesianPoint from Geom to IGES. If this
        Entity could not be converted, this member returns a NullEntity.
        """

class Geom2dToIGES_Geom2dVector(Geom2dToIGES_Geom2dEntity):
    """
    This class implements the transfer of the Vector from Geom2d
    to IGES. These can be:
    . Vector
    * Direction
    * VectorWithMagnitude
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, G2dE: Geom2dToIGES_Geom2dEntity) -> None:
        """
        Creates a tool Geom2dVector ready to run and sets its
        fields as G2dE's.
        """

    @overload
    def __init__(self, theOther: Geom2dToIGES_Geom2dVector) -> None: ...

    @overload
    def Transfer2dVector(self, start: nanoocp.Geom2d.Geom2d_Vector | None) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        Transfer a GeometryEntity which answer True to the
        member : BRepToIGES::IsGeomVector(Geometry). If this
        Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def Transfer2dVector(self, start: nanoocp.Geom2d.Geom2d_VectorWithMagnitude | None) -> nanoocp.IGESGeom.IGESGeom_Direction: ...

    @overload
    def Transfer2dVector(self, start: nanoocp.Geom2d.Geom2d_Direction | None) -> nanoocp.IGESGeom.IGESGeom_Direction: ...
