"""OCCT package Intf (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Bnd
import nanoocp.gp


class Intf_PIType(enum.IntEnum):
    """
    Describes the different intersection point types for this
    application.
    """

    Intf_EXTERNAL = 0

    Intf_FACE = 1

    Intf_EDGE = 2

    Intf_VERTEX = 3

Intf_EXTERNAL: Intf_PIType = Intf_PIType.Intf_EXTERNAL

Intf_FACE: Intf_PIType = Intf_PIType.Intf_FACE

Intf_EDGE: Intf_PIType = Intf_PIType.Intf_EDGE

Intf_VERTEX: Intf_PIType = Intf_PIType.Intf_VERTEX

class Intf:
    """
    Interference computation between polygons, lines and
    polyhedra with only triangular facets. These objects
    are polygonal representations of complex curves and
    triangulated representations of complex surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Intf) -> None: ...

    @staticmethod
    def PlaneEquation(P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, NormalVector: nanoocp.gp.gp_XYZ) -> float:
        """
        Computes the interference between two polygons in 2d.
        Result : points of intersections and zones of tangence.
        Computes the interference between a polygon or a straight
        line and a polyhedron. Points of intersection and zones
        of tangence.
        Give the plane equation of the triangle <P1> <P2> <P3>.
        """

    @staticmethod
    def Contain(P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, ThePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Compute if the triangle <P1> <P2> <P3> contain <ThePnt>."""

class Intf_SectionPoint:
    """
    Describes an intersection point between polygons and
    polyedra.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Where: nanoocp.gp.gp_Pnt2d, DimeO: Intf_PIType, AddrO1: int, ParamO: float, DimeT: Intf_PIType, AddrT1: int, ParamT: float, Incid: float) -> None:
        """
        Builds a SectionPoint 2d with the respective dimensions
        (vertex or edge) of the concerned arguments and their
        addresses in the Topological structure.
        """

    @overload
    def __init__(self, Where: nanoocp.gp.gp_Pnt, DimeO: Intf_PIType, AddrO1: int, AddrO2: int, ParamO: float, DimeT: Intf_PIType, AddrT1: int, AddrT2: int, ParamT: float, Incid: float) -> None:
        """
        Builds a SectionPoint with the respective dimensions
        (vertex edge or face) of the concerned arguments and their
        addresses in the Topological structure.
        """

    @overload
    def __init__(self, theOther: Intf_SectionPoint) -> None: ...

    def Pnt(self) -> nanoocp.gp.gp_Pnt:
        """Returns the location of the SectionPoint."""

    def ParamOnFirst(self) -> float:
        """
        Returns the cumulated Parameter of the SectionPoint on the
        first element.
        """

    def ParamOnSecond(self) -> float:
        """
        Returns the cumulated Parameter of the section point on the
        second element.
        """

    def TypeOnFirst(self) -> Intf_PIType:
        """Returns the type of the section point on the first element."""

    def TypeOnSecond(self) -> Intf_PIType:
        """
        Returns the type of the section point on the second
        element.
        """

    def InfoFirst__Intf_PIType_int_int_float(self) -> tuple[Intf_PIType, int, int, float]:
        """
        InfoFirst__Intf_PIType_int_int_float: the C++ overload InfoFirst(Intf_PIType &, int &, int &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    def InfoFirst__Intf_PIType_int_float(self) -> tuple[Intf_PIType, int, float]:
        """
        InfoFirst__Intf_PIType_int_float: the C++ overload InfoFirst(Intf_PIType &, int &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Gives the data about the first argument of the Interference.
        """

    def InfoSecond__Intf_PIType_int_int_float(self) -> tuple[Intf_PIType, int, int, float]:
        """
        InfoSecond__Intf_PIType_int_int_float: the C++ overload InfoSecond(Intf_PIType &, int &, int &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    def InfoSecond__Intf_PIType_int_float(self) -> tuple[Intf_PIType, int, float]:
        """
        InfoSecond__Intf_PIType_int_float: the C++ overload InfoSecond(Intf_PIType &, int &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Gives the data about the second argument of the Interference.
        """

    def Incidence(self) -> float:
        """
        Gives the incidence at this section point. The incidence
        between the two triangles is given by the cosine. The best
        incidence is 0. (PI/2). The worst is 1. (null angle).
        """

    def IsEqual(self, Other: Intf_SectionPoint) -> bool:
        """
        Returns True if the two SectionPoint have the same logical
        information.
        """

    def __eq__(self, Other: Intf_SectionPoint) -> bool: ...

    def IsOnSameEdge(self, Other: Intf_SectionPoint) -> bool:
        """
        Returns True if the two SectionPoints are on the same edge
        of the first or the second element.
        """

    def Merge(self, Other: Intf_SectionPoint) -> None:
        """Merges two SectionPoints."""

    def Dump(self, Indent: int) -> None: ...

class Intf_SectionLine:
    """
    Describe a polyline of intersection between two
    polyhedra as a sequence of points of intersection.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty SectionLine."""

    @overload
    def __init__(self, Other: Intf_SectionLine) -> None:
        """Copies a SectionLine."""

    def NumberOfPoints(self) -> int:
        """Returns number of points in this SectionLine."""

    def GetPoint(self, Index: int) -> Intf_SectionPoint:
        """
        Gives the point of intersection of address <Index> in the
        SectionLine.
        """

    def IsClosed(self) -> bool:
        """Returns True if the SectionLine is closed."""

    def Contains(self, ThePI: Intf_SectionPoint) -> bool:
        """Returns True if ThePI is in the SectionLine <me>."""

    def IsEnd(self, ThePI: Intf_SectionPoint) -> int:
        """
        Checks if <ThePI> is an end of the SectionLine. Returns 1
        for the beginning, 2 for the end, otherwise 0.
        """

    def IsEqual(self, Other: Intf_SectionLine) -> bool:
        """Compares two SectionLines."""

    def __eq__(self, Other: Intf_SectionLine) -> bool: ...

    @overload
    def Append(self, Pi: Intf_SectionPoint) -> None:
        """Adds a point at the end of the SectionLine."""

    @overload
    def Append(self, LS: Intf_SectionLine) -> None:
        """
        Concatenates the SectionLine <LS> at the end of the
        SectionLine <me>.
        """

    @overload
    def Prepend(self, Pi: Intf_SectionPoint) -> None:
        """Adds a point to the beginning of the SectionLine <me>."""

    @overload
    def Prepend(self, LS: Intf_SectionLine) -> None:
        """
        Concatenates a SectionLine <LS> at the beginning of the
        SectionLine <me>.
        """

    def Reverse(self) -> None:
        """Reverses the order of the elements of the SectionLine."""

    def Close(self) -> None:
        """Closes the SectionLine."""

    def Dump(self, Indent: int) -> None: ...

class Intf_TangentZone:
    """
    Describes a zone of tangence between polygons or
    polyhedra as a sequence of points of intersection.
    """

    @overload
    def __init__(self) -> None:
        """Builds an empty tangent zone."""

    @overload
    def __init__(self, theOther: Intf_TangentZone) -> None: ...

    def NumberOfPoints(self) -> int:
        """Returns number of SectionPoint in this TangentZone."""

    def GetPoint(self, Index: int) -> Intf_SectionPoint:
        """
        Gives the SectionPoint of address <Index> in the
        TangentZone.
        """

    def IsEqual(self, Other: Intf_TangentZone) -> bool:
        """Compares two TangentZones."""

    def __eq__(self, Other: Intf_TangentZone) -> bool: ...

    def Contains(self, ThePI: Intf_SectionPoint) -> bool:
        """Checks if <ThePI> is in TangentZone."""

    def ParamOnFirst(self) -> tuple[float, float]:
        """
        Gives the parameter range of the TangentZone on the first
        argument of the Interference. (Usable only for polygon)
        """

    def ParamOnSecond(self) -> tuple[float, float]:
        """
        Gives the parameter range of the TangentZone on the second
        argument of the Interference. (Usable only for polygon)
        """

    def InfoFirst(self) -> tuple[int, float, int, float]:
        """
        Gives information about the first argument of the
        Interference. (Usable only for polygon)
        """

    def InfoSecond(self) -> tuple[int, float, int, float]:
        """
        Gives information about the second argument of the
        Interference. (Usable only for polygon)
        """

    def RangeContains(self, ThePI: Intf_SectionPoint) -> bool:
        """
        Returns True if <ThePI> is in the parameter range of the
        TangentZone.
        """

    def HasCommonRange(self, Other: Intf_TangentZone) -> bool:
        """
        Returns True if the TangentZone <Other> has a common part
        with <me>.
        """

    @overload
    def Append(self, Pi: Intf_SectionPoint) -> None:
        """Adds a SectionPoint to the TangentZone."""

    @overload
    def Append(self, Tzi: Intf_TangentZone) -> None:
        """Adds the TangentZone <Tzi> to <me>."""

    def Insert(self, Pi: Intf_SectionPoint) -> bool:
        """Inserts a SectionPoint in the TangentZone."""

    def PolygonInsert(self, Pi: Intf_SectionPoint) -> None:
        """Inserts a point in the polygonal TangentZone."""

    def InsertBefore(self, Index: int, Pi: Intf_SectionPoint) -> None:
        """Inserts a SectionPoint before <Index> in the TangentZone."""

    def InsertAfter(self, Index: int, Pi: Intf_SectionPoint) -> None:
        """Inserts a SectionPoint after <Index> in the TangentZone."""

    def Dump(self, Indent: int) -> None: ...

class Intf_Interference:
    """
    Describes the Interference computation result
    between polygon2d or polygon3d or polyhedron
    (as three sequences of points of intersection,
    polylines of intersection and zones de tangence).
    """

    def NbSectionPoints(self) -> int:
        """
        Gives the number of points of intersection in the
        interference.
        """

    def PntValue(self, Index: int) -> Intf_SectionPoint:
        """
        Gives the point of intersection of address Index in
        the interference.
        """

    def NbSectionLines(self) -> int:
        """
        Gives the number of polylines of intersection in the
        interference.
        """

    def LineValue(self, Index: int) -> Intf_SectionLine:
        """
        Gives the polyline of intersection at address <Index> in
        the interference.
        """

    def NbTangentZones(self) -> int:
        """Gives the number of zones of tangence in the interference."""

    def ZoneValue(self, Index: int) -> Intf_TangentZone:
        """
        Gives the zone of tangence at address Index in the
        interference.
        """

    def GetTolerance(self) -> float:
        """Gives the tolerance used for the calculation."""

    def Contains(self, ThePnt: Intf_SectionPoint) -> bool:
        """
        Tests if the polylines of intersection or the zones of
        tangence contain the point of intersection <ThePnt>.
        """

    @overload
    def Insert(self, TheZone: Intf_TangentZone) -> bool:
        """
        Inserts a new zone of tangence in the current list of
        tangent zones of the interference and returns True
        when done.
        """

    @overload
    def Insert(self, pdeb: Intf_SectionPoint, pfin: Intf_SectionPoint) -> None:
        """
        Insert a new segment of intersection in the current list of
        polylines of intersection of the interference.
        """

    def Dump(self) -> None: ...

class Intf_InterferencePolygon2d(Intf_Interference):
    """
    Computes the interference between two polygons or
    the self intersection of a polygon in two
    dimensions.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty interference of Polygon."""

    @overload
    def __init__(self, Obje: Intf_Polygon2d) -> None:
        """Constructs and computes the auto interference of a Polygon."""

    @overload
    def __init__(self, Obje1: Intf_Polygon2d, Obje2: Intf_Polygon2d) -> None:
        """Constructs and computes an interference between two Polygons."""

    @overload
    def __init__(self, theOther: Intf_InterferencePolygon2d) -> None: ...

    @overload
    def Perform(self, Obje1: Intf_Polygon2d, Obje2: Intf_Polygon2d) -> None:
        """Computes an interference between two Polygons."""

    @overload
    def Perform(self, Obje: Intf_Polygon2d) -> None:
        """Computes the self interference of a Polygon."""

    def Pnt2dValue(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Gives the geometrical 2d point of the intersection
        point at address <Index> in the interference.
        """

class Intf_Polygon2d:
    """
    Describes the necessary polygon information to compute
    the interferences.
    """

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box2d:
        """Returns the bounding box of the polygon."""

    def Closed(self) -> bool:
        """Returns True if the polyline is closed."""

    def DeflectionOverEstimation(self) -> float:
        """Returns the tolerance of the polygon."""

    def NbSegments(self) -> int:
        """Returns the number of Segments in the polyline."""

    def Segment(self, theIndex: int, theBegin: nanoocp.gp.gp_Pnt2d, theEnd: nanoocp.gp.gp_Pnt2d) -> None:
        """Returns the points of the segment <Index> in the Polygon."""

class Intf_Tool:
    """
    Provides services to create box for infinites
    lines in a given contexte.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Intf_Tool) -> None: ...

    def Lin2dBox(self, theLin2d: nanoocp.gp.gp_Lin2d, bounding: nanoocp.Bnd.Bnd_Box2d, boxLin: nanoocp.Bnd.Bnd_Box2d) -> None: ...

    def Hypr2dBox(self, theHypr2d: nanoocp.gp.gp_Hypr2d, bounding: nanoocp.Bnd.Bnd_Box2d, boxHypr: nanoocp.Bnd.Bnd_Box2d) -> None: ...

    def Parab2dBox(self, theParab2d: nanoocp.gp.gp_Parab2d, bounding: nanoocp.Bnd.Bnd_Box2d, boxHypr: nanoocp.Bnd.Bnd_Box2d) -> None: ...

    def LinBox(self, theLin: nanoocp.gp.gp_Lin, bounding: nanoocp.Bnd.Bnd_Box, boxLin: nanoocp.Bnd.Bnd_Box) -> None: ...

    def HyprBox(self, theHypr: nanoocp.gp.gp_Hypr, bounding: nanoocp.Bnd.Bnd_Box, boxHypr: nanoocp.Bnd.Bnd_Box) -> None: ...

    def ParabBox(self, theParab: nanoocp.gp.gp_Parab, bounding: nanoocp.Bnd.Bnd_Box, boxHypr: nanoocp.Bnd.Bnd_Box) -> None: ...

    def NbSegments(self) -> int: ...

    def BeginParam(self, SegmentNum: int) -> float: ...

    def EndParam(self, SegmentNum: int) -> float: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
Intf_Array1OfLin = nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin]
