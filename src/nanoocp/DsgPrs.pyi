"""OCCT package DsgPrs (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.Graphic3d
import nanoocp.Prs3d
import nanoocp.TCollection
import nanoocp.TopoDS
import nanoocp.gp


class DsgPrs_ArrowSide(enum.IntEnum):
    """
    Designates how many arrows will be displayed and
    where they will be displayed in presenting a length.
    """

    DsgPrs_AS_NONE = 0

    DsgPrs_AS_FIRSTAR = 1

    DsgPrs_AS_LASTAR = 2

    DsgPrs_AS_BOTHAR = 3

    DsgPrs_AS_FIRSTPT = 4

    DsgPrs_AS_LASTPT = 5

    DsgPrs_AS_BOTHPT = 6

    DsgPrs_AS_FIRSTAR_LASTPT = 7

    DsgPrs_AS_FIRSTPT_LASTAR = 8

DsgPrs_AS_NONE: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_NONE

DsgPrs_AS_FIRSTAR: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR

DsgPrs_AS_LASTAR: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_LASTAR

DsgPrs_AS_BOTHAR: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_BOTHAR

DsgPrs_AS_FIRSTPT: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT

DsgPrs_AS_LASTPT: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_LASTPT

DsgPrs_AS_BOTHPT: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_BOTHPT

DsgPrs_AS_FIRSTAR_LASTPT: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR_LASTPT

DsgPrs_AS_FIRSTPT_LASTAR: DsgPrs_ArrowSide = DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT_LASTAR

class DsgPrs:
    """Describes Standard Presentations for DsgIHM objects"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs) -> None: ...

    @staticmethod
    def ComputeSymbol(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, anAspect: nanoocp.Prs3d.Prs3d_DimensionAspect | None, pt1: nanoocp.gp.gp_Pnt, pt2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, ArrowSide: DsgPrs_ArrowSide, drawFromCenter: bool = True) -> None:
        """
        draws symbols ((one or two) arrows,(one or two)points
        at thebeginning and at the end of the dimension
        """

    @staticmethod
    def ComputePlanarFacesLengthPresentation(FirstArrowLength: float, SecondArrowLength: float, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, DirAttach: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt, PlaneOfFaces: nanoocp.gp.gp_Pln, EndOfArrow1: nanoocp.gp.gp_Pnt, EndOfArrow2: nanoocp.gp.gp_Pnt, DirOfArrow1: nanoocp.gp.gp_Dir) -> None: ...

    @staticmethod
    def ComputeCurvilinearFacesLengthPresentation(FirstArrowLength: float, SecondArrowLength: float, SecondSurf: nanoocp.Geom.Geom_Surface | None, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, DirAttach: nanoocp.gp.gp_Dir, EndOfArrow2: nanoocp.gp.gp_Pnt, DirOfArrow1: nanoocp.gp.gp_Dir) -> tuple[nanoocp.Geom.Geom_Curve, nanoocp.Geom.Geom_Curve, float, float, float, float]: ...

    @staticmethod
    def ComputeFacesAnglePresentation(ArrowLength: float, Value: float, CenterPoint: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, axisdir: nanoocp.gp.gp_Dir, isPlane: bool, AxisOfSurf: nanoocp.gp.gp_Ax1, OffsetPoint: nanoocp.gp.gp_Pnt, AngleCirc: nanoocp.gp.gp_Circ, EndOfArrow1: nanoocp.gp.gp_Pnt, EndOfArrow2: nanoocp.gp.gp_Pnt, DirOfArrow1: nanoocp.gp.gp_Dir, DirOfArrow2: nanoocp.gp.gp_Dir, ProjAttachPoint2: nanoocp.gp.gp_Pnt, AttachCirc: nanoocp.gp.gp_Circ) -> tuple[float, float, float, float]: ...

    @staticmethod
    def ComputeRadiusLine(aCenter: nanoocp.gp.gp_Pnt, anEndOfArrow: nanoocp.gp.gp_Pnt, aPosition: nanoocp.gp.gp_Pnt, drawFromCenter: bool, aRadLineOrign: nanoocp.gp.gp_Pnt, aRadLineEnd: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def ComputeFilletRadiusPresentation(ArrowLength: float, Value: float, Position: nanoocp.gp.gp_Pnt, NormalDir: nanoocp.gp.gp_Dir, FirstPoint: nanoocp.gp.gp_Pnt, SecondPoint: nanoocp.gp.gp_Pnt, Center: nanoocp.gp.gp_Pnt, BasePnt: nanoocp.gp.gp_Pnt, drawRevers: bool, FilletCirc: nanoocp.gp.gp_Circ, EndOfArrow: nanoocp.gp.gp_Pnt, DirOfArrow: nanoocp.gp.gp_Dir, DrawPosition: nanoocp.gp.gp_Pnt) -> tuple[bool, float, float]:
        """
        computes Geometry for fillet radius presentation;
        special case flag SpecCase equal true if
        radius of fillet circle = 0 or if angle between
        Vec1(Center, FirstPoint) and Vec2(Center,SecondPoint) equal 0 or PI
        """

    @staticmethod
    def DistanceFromApex(elips: nanoocp.gp.gp_Elips, Apex: nanoocp.gp.gp_Pnt, par: float) -> float:
        """computes length of ellipse arc in parametric units"""

class DsgPrs_AnglePresentation:
    """A framework for displaying angles."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_AnglePresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aCircle: nanoocp.gp.gp_Circ, aPosition: nanoocp.gp.gp_Pnt, Apex: nanoocp.gp.gp_Pnt, VminCircle: nanoocp.gp.gp_Circ, VmaxCircle: nanoocp.gp.gp_Circ, aArrowSize: float) -> None:
        """
        Draws the presentation of the full angle of a cone.
        VminCircle - a circle at V parameter = Vmin
        VmaxCircle - a circle at V parameter = Vmax
        aCircle - a circle at V parameter from projection of aPosition to axis of the cone
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, CenterPoint: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Draws the representation of the angle
        defined by dir1 and dir2, centered on
        CenterPoint, using the offset point OffsetPoint.
        Lines are drawn to points AttachmentPoint1 and AttachmentPoint2
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, thevalstring: nanoocp.TCollection.TCollection_ExtendedString, CenterPoint: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Same as above, but <thevalstring> contains conversion
        in Session units....
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, thevalstring: nanoocp.TCollection.TCollection_ExtendedString, CenterPoint: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Same as above, may add one or
        two Arrows according to <ArrowSide> value
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, thevalstring: nanoocp.TCollection.TCollection_ExtendedString, CenterPoint: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, axisdir: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Same as above, but axisdir contains the axis direction
        useful for Revol that can be opened with 180 degrees
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, thevalstring: nanoocp.TCollection.TCollection_ExtendedString, CenterPoint: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, dir1: nanoocp.gp.gp_Dir, dir2: nanoocp.gp.gp_Dir, axisdir: nanoocp.gp.gp_Dir, isPlane: bool, AxisOfSurf: nanoocp.gp.gp_Ax1, OffsetPoint: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Same as above,may add one or
        two Arrows according to <ArrowSide> value
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, theCenter: nanoocp.gp.gp_Pnt, AttachmentPoint1: nanoocp.gp.gp_Pnt, theAxe: nanoocp.gp.gp_Ax1, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        simple representation of a poor lonesome angle dimension
        Draw a line from <theCenter> to <AttachmentPoint1>, then operates
        a rotation around the perpmay add one or
        two Arrows according to <ArrowSide> value. The
        attributes (color,arrowsize,...) are driven by the Drawer.
        """

class DsgPrs_Chamf2dPresentation:
    """Framework for display of 2D chamfers."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_Chamf2dPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aPntAttach: nanoocp.gp.gp_Pnt, aPntEnd: nanoocp.gp.gp_Pnt, aText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Defines the display of elements showing 2D chamfers on shapes.
        These include the text aText, the point of attachment,
        aPntAttach and the end point aPntEnd.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aPntAttach: nanoocp.gp.gp_Pnt, aPntEnd: nanoocp.gp.gp_Pnt, aText: nanoocp.TCollection.TCollection_ExtendedString, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Defines the display of texts, symbols and icons used
        to present 2D chamfers.
        These include the text aText, the point of attachment,
        aPntAttach and the end point aPntEnd.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer. The arrow
        at the point of attachment has a display defined by a
        value of the enumeration DsgPrs_Arrowside.
        """

class DsgPrs_ConcentricPresentation:
    """A framework to define display of relations of concentricity."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_ConcentricPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aCenter: nanoocp.gp.gp_Pnt, aRadius: float, aNorm: nanoocp.gp.gp_Dir, aPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Defines the display of elements showing relations of
        concentricity between shapes.
        These include the center aCenter, the radius
        aRadius, the direction aNorm and the point aPoint.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer.
        """

class DsgPrs_DatumPrs(nanoocp.Prs3d.Prs3d_Root):
    """A framework for displaying an XYZ trihedron."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_DatumPrs) -> None: ...

    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theDatum: nanoocp.gp.gp_Ax2, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Draw XYZ axes at specified location with attributes defined by the attribute manager
        theDrawer:
        - Prs3d_DatumAspect defines arrow, line and length trihedron axis parameters,
        - Prs3d_TextAspect defines displayed text.
        The thihedron origin and axis directions are defined by theDatum coordinate system.
        DsgPrs_XYZAxisPresentation framework is used to create graphical primitives for each axis.
        Axes are marked with "X", "Y", "Z" text.
        @param[out] thePresentation  the modified presentation
        @param[in] theDatum  the source of trihedron position
        @param[in] theDrawer  the provider of display attributes
        """

class DsgPrs_DiameterPresentation:
    """A framework for displaying diameters in shapes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_DiameterPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint: nanoocp.gp.gp_Pnt, aCircle: nanoocp.gp.gp_Circ, ArrowSide: DsgPrs_ArrowSide, IsDiamSymbol: bool) -> None:
        """
        Draws the diameter of the circle aCircle displayed in
        the presentation aPresentation and with attributes
        defined by the attribute manager aDrawer. The point
        AttachmentPoint defines the point of contact
        between the circle and the diameter presentation.
        The value of the enumeration ArrowSide controls
        whether arrows will be displayed at either or both
        ends of the length. The text aText labels the diameter.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint: nanoocp.gp.gp_Pnt, aCircle: nanoocp.gp.gp_Circ, uFirst: float, uLast: float, ArrowSide: DsgPrs_ArrowSide, IsDiamSymbol: bool) -> None:
        """
        Draws the diameter of the arc anArc displayed in the
        presentation aPresentation and with attributes
        defined by the attribute manager aDrawer. The point
        AttachmentPoint defines the point of contact
        between the arc and the diameter presentation. The
        value of the enumeration ArrowSide controls whether
        arrows will be displayed at either or both ends of the
        length. The parameters uFirst and uLast define the
        first and last points of the arc. The text aText labels the diameter.
        """

class DsgPrs_EllipseRadiusPresentation:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_EllipseRadiusPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint: nanoocp.gp.gp_Pnt, anEndOfArrow: nanoocp.gp.gp_Pnt, aCenter: nanoocp.gp.gp_Pnt, IsMaxRadius: bool, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        draws a Radius (Major or Minor)
        representation for whole ellipse case
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, aText: nanoocp.TCollection.TCollection_ExtendedString, anEllipse: nanoocp.gp.gp_Elips, AttachmentPoint: nanoocp.gp.gp_Pnt, anEndOfArrow: nanoocp.gp.gp_Pnt, aCenter: nanoocp.gp.gp_Pnt, uFirst: float, IsInDomain: bool, IsMaxRadius: bool, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        draws a Radius (Major or Minor) representation
        for arc of an ellipse case
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theval: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aCurve: nanoocp.Geom.Geom_OffsetCurve | None, AttachmentPoint: nanoocp.gp.gp_Pnt, anEndOfArrow: nanoocp.gp.gp_Pnt, aCenter: nanoocp.gp.gp_Pnt, uFirst: float, IsInDomain: bool, IsMaxRadius: bool, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        draws a Radius (Major or Minor) representation
        for arc of an offset curve from ellipse
        """

class DsgPrs_EqualDistancePresentation:
    """
    A framework to display equal distances between shapes and a given plane.
    The distance is the length of a projection from the shape to the plane.
    These distances are used to compare two shapes by this vector alone.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_EqualDistancePresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, Point1: nanoocp.gp.gp_Pnt, Point2: nanoocp.gp.gp_Pnt, Point3: nanoocp.gp.gp_Pnt, Point4: nanoocp.gp.gp_Pnt, Plane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Adds the points Point1, Point2, Point3 Point4, and the
        plane Plane to the presentation object aPresentation.
        The display attributes of these elements is defined by the attribute manager aDrawer.
        The distance is the length of a projection from the shape to the plane.
        These distances are used to compare two shapes by this vector alone.
        """

    @staticmethod
    def AddInterval(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aPoint1: nanoocp.gp.gp_Pnt, aPoint2: nanoocp.gp.gp_Pnt, aDir: nanoocp.gp.gp_Dir, aPosition: nanoocp.gp.gp_Pnt, anArrowSide: DsgPrs_ArrowSide, anExtremePnt1: nanoocp.gp.gp_Pnt, anExtremePnt2: nanoocp.gp.gp_Pnt) -> None:
        """
        is used for presentation of interval between
        two lines or two points or between a line and a point.
        """

    @staticmethod
    def AddIntervalBetweenTwoArcs(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aCircle1: nanoocp.gp.gp_Circ, aCircle2: nanoocp.gp.gp_Circ, aPoint1: nanoocp.gp.gp_Pnt, aPoint2: nanoocp.gp.gp_Pnt, aPoint3: nanoocp.gp.gp_Pnt, aPoint4: nanoocp.gp.gp_Pnt, anArrowSide: DsgPrs_ArrowSide) -> None:
        """
        is used for presentation of interval between two arcs.
        One of arcs can have a zero radius.
        """

class DsgPrs_EqualRadiusPresentation:
    """A framework to define display of equality in radii."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_EqualRadiusPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, FirstCenter: nanoocp.gp.gp_Pnt, SecondCenter: nanoocp.gp.gp_Pnt, FirstPoint: nanoocp.gp.gp_Pnt, SecondPoint: nanoocp.gp.gp_Pnt, Plane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Adds the points FirstCenter, SecondCenter,
        FirstPoint, SecondPoint, and the plane Plane to the
        presentation object aPresentation.
        The display attributes of these elements is defined by
        the attribute manager aDrawer.
        FirstCenter and SecondCenter are the centers of the
        first and second shapes respectively, and FirstPoint
        and SecondPoint are the attachment points of the radii to arcs.
        """

class DsgPrs_FilletRadiusPresentation:
    """A framework for displaying radii of fillets."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_FilletRadiusPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, thevalue: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aPosition: nanoocp.gp.gp_Pnt, aNormalDir: nanoocp.gp.gp_Dir, aBasePnt: nanoocp.gp.gp_Pnt, aFirstPoint: nanoocp.gp.gp_Pnt, aSecondPoint: nanoocp.gp.gp_Pnt, aCenter: nanoocp.gp.gp_Pnt, ArrowPrs: DsgPrs_ArrowSide, drawRevers: bool, DrawPosition: nanoocp.gp.gp_Pnt, EndOfArrow: nanoocp.gp.gp_Pnt) -> tuple[nanoocp.Geom.Geom_TrimmedCurve, bool]:
        """
        Adds a display of the radius of a fillet to the
        presentation aPresentation. The display ttributes
        defined by the attribute manager aDrawer. the value
        specifies the length of the radius.
        """

class DsgPrs_FixPresentation:
    """class which draws the presentation of Fixed objects"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_FixPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aPntAttach: nanoocp.gp.gp_Pnt, aPntEnd: nanoocp.gp.gp_Pnt, aNormPln: nanoocp.gp.gp_Dir, aSymbSize: float) -> None:
        """
        draws the presentation of fixed objects by
        drawing the 'fix' symbol at position <aPntEnd>.
        A binding segment is drawn between <aPntAttach>
        ( which belongs to the fixed object) and <aPntEnd>.
        aSymbSize is the size of the 'fix'symbol
        """

class DsgPrs_IdenticPresentation:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_IdenticPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, aPntAttach: nanoocp.gp.gp_Pnt, aPntOffset: nanoocp.gp.gp_Pnt) -> None:
        """
        draws a line between <aPntAttach> and
        <aPntOffset>.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, aFAttach: nanoocp.gp.gp_Pnt, aSAttach: nanoocp.gp.gp_Pnt, aPntOffset: nanoocp.gp.gp_Pnt) -> None:
        """
        draws the 'identic' presentation by
        drawing a line between <aFAttach> and
        <aSAttach> , and a linkimg segment
        between <aPntOffset> and its projection
        on the precedent line.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, aAx2: nanoocp.gp.gp_Ax2, aCenter: nanoocp.gp.gp_Pnt, aFAttach: nanoocp.gp.gp_Pnt, aSAttach: nanoocp.gp.gp_Pnt, aPntOffset: nanoocp.gp.gp_Pnt) -> None:
        """
        draws the 'identic' presentation in the case of
        circles : draws an arc of circle between
        <aFAttach> and <aSAttach> of center <aCenter>
        and of radius dist(aCenter, aFAttach), and
        draws a segment between <aPntOffset> and
        its projection on the arc.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, aAx2: nanoocp.gp.gp_Ax2, aCenter: nanoocp.gp.gp_Pnt, aFAttach: nanoocp.gp.gp_Pnt, aSAttach: nanoocp.gp.gp_Pnt, aPntOffset: nanoocp.gp.gp_Pnt, aPntOnCirc: nanoocp.gp.gp_Pnt) -> None:
        """
        draws the 'identic' presentation in the case of
        circles : draws an arc of circle between
        <aFAttach> and <aSAttach> of center <aCenter>
        and of radius dist(aCenter, aFAttach), and
        draws a segment between <aPntOffset> and <aPntOnCirc>
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, anEllipse: nanoocp.gp.gp_Elips, aFAttach: nanoocp.gp.gp_Pnt, aSAttach: nanoocp.gp.gp_Pnt, aPntOffset: nanoocp.gp.gp_Pnt, aPntOnElli: nanoocp.gp.gp_Pnt) -> None:
        """
        draws the 'identic' presentation in the case of
        ellipses: draws an arc of the anEllipse
        between <aFAttach> and <aSAttach> and
        draws a segment between <aPntOffset> and <aPntOnElli>
        """

class DsgPrs_LengthPresentation:
    """
    Framework for displaying lengths.
    The length displayed is indicated by line segments
    and text alone or by a combination of line segment,
    text and arrows at either or both of its ends.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_LengthPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Draws a line segment representing a length in the
        display aPresentation.
        This segment joins the points AttachmentPoint1 and
        AttachmentPoint2, along the direction aDirection.
        The text aText will be displayed at the offset point OffsetPoint.
        The line and text attributes are specified by the
        attribute manager aDrawer.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Draws a line segment representing a length in the
        display aPresentation.
        This segment joins the points AttachmentPoint1 and
        AttachmentPoint2, along the direction aDirection.
        The text aText will be displayed at the offset point
        OffsetPoint. The value of the enumeration ArrowSide
        controls whether arrows will be displayed at either or
        both ends of the length.
        The line, text and arrow attributes are specified by the
        attribute manager aDrawer.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, PlaneOfFaces: nanoocp.gp.gp_Pln, aDirection: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Draws a line segment representing a length in the
        display aPresentation.
        This segment joins the points AttachmentPoint1 and
        AttachmentPoint2, along the direction aDirection.
        The text aText will be displayed at the offset point
        OffsetPoint. The value of the enumeration ArrowSide
        controls whether arrows will be displayed at either or
        both ends of the length.
        The plane PlaneOfFaces is used if length is null.
        The line, text and arrow attributes are specified by the
        attribute manager aDrawer.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, SecondSurf: nanoocp.Geom.Geom_Surface | None, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Draws a line segment representing a length in the
        display aPresentation.
        This segment joins the points AttachmentPoint1 and
        AttachmentPoint2, along the direction
        aDirection. AttachmentPoint2 lies on the curvilinear
        faces SecondSurf. The text aText will be displayed at
        the offset point OffsetPoint. The value of the
        enumeration ArrowSide controls whether arrows will
        be displayed at either or both ends of the length.
        The line, text and arrow attributes are specified by the
        attribute manager aDrawer.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Draws a line segment representing a length in the
        display aPresentation.
        This segment joins the points AttachmentPoint1 and
        AttachmentPoint2, along the direction aDirection.
        The value of the enumeration ArrowSide controls
        whether arrows will be displayed at either or both ends of the length.
        The line and arrow attributes are specified by the attribute manager aDrawer.
        """

class DsgPrs_MidPointPresentation:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_MidPointPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theAxe: nanoocp.gp.gp_Ax2, MidPoint: nanoocp.gp.gp_Pnt, Position: nanoocp.gp.gp_Pnt, AttachPoint: nanoocp.gp.gp_Pnt, first: bool) -> None:
        """
        draws the representation of a MidPoint between
        two vertices.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theAxe: nanoocp.gp.gp_Ax2, MidPoint: nanoocp.gp.gp_Pnt, Position: nanoocp.gp.gp_Pnt, AttachPoint: nanoocp.gp.gp_Pnt, Point1: nanoocp.gp.gp_Pnt, Point2: nanoocp.gp.gp_Pnt, first: bool) -> None:
        """
        draws the representation of a MidPoint between
        two lines or linear segments.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aCircle: nanoocp.gp.gp_Circ, MidPoint: nanoocp.gp.gp_Pnt, Position: nanoocp.gp.gp_Pnt, AttachPoint: nanoocp.gp.gp_Pnt, Point1: nanoocp.gp.gp_Pnt, Point2: nanoocp.gp.gp_Pnt, first: bool) -> None:
        """
        draws the representation of a MidPoint between
        two entire circles or two circular arcs.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, anElips: nanoocp.gp.gp_Elips, MidPoint: nanoocp.gp.gp_Pnt, Position: nanoocp.gp.gp_Pnt, AttachPoint: nanoocp.gp.gp_Pnt, Point1: nanoocp.gp.gp_Pnt, Point2: nanoocp.gp.gp_Pnt, first: bool) -> None:
        """
        draws the representation of a MidPoint between
        two entire ellipses or two elliptic arcs.
        """

class DsgPrs_OffsetPresentation:
    """A framework to define display of offsets."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_OffsetPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, aDirection2: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Defines the display of elements showing offset shapes.
        These include the two points of attachment
        AttachmentPoint1 and AttachmentPoint1, the two
        directions aDirection and aDirection2, and the offset point OffsetPoint.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer.
        """

    @staticmethod
    def AddAxes(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, aDirection2: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        draws the representation of axes alignment Constraint
        between the point AttachmentPoint1 and the
        point AttachmentPoint2, along direction
        aDirection, using the offset point OffsetPoint.
        """

class DsgPrs_ParalPresentation:
    """
    A framework to define display of relations of parallelism between shapes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_ParalPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Defines the display of elements showing relations of
        parallelism between shapes.
        These include the two points of attachment
        AttachmentPoint1 and AttachmentPoint1, the
        direction aDirection, and the offset point OffsetPoint.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, OffsetPoint: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide) -> None:
        """
        Defines the display of elements showing relations of
        parallelism between shapes.
        These include the two points of attachment
        AttachmentPoint1 and AttachmentPoint1, the
        direction aDirection, the offset point OffsetPoint and
        the text aText.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer.
        """

class DsgPrs_PerpenPresentation:
    """
    A framework to define display of perpendicular
    constraints between shapes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_PerpenPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, pAx1: nanoocp.gp.gp_Pnt, pAx2: nanoocp.gp.gp_Pnt, pnt1: nanoocp.gp.gp_Pnt, pnt2: nanoocp.gp.gp_Pnt, OffsetPoint: nanoocp.gp.gp_Pnt, intOut1: bool, intOut2: bool) -> None:
        """
        Defines the display of elements showing
        perpendicular constraints between shapes.
        These include the two axis points pAx1 and pAx2,
        the two points pnt1 and pnt2, the offset point
        OffsetPoint and the two Booleans intOut1} and intOut2{.
        These arguments are added to the presentation
        object aPresentation. Their display attributes are
        defined by the attribute manager aDrawer.
        """

class DsgPrs_RadiusPresentation:
    """A framework to define display of radii."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_RadiusPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint: nanoocp.gp.gp_Pnt, aCircle: nanoocp.gp.gp_Circ, firstparam: float, lastparam: float, drawFromCenter: bool = True, reverseArrow: bool = False) -> None:
        """
        Adds the point AttachmentPoint, the circle aCircle,
        the text aText, and the parameters firstparam and
        lastparam to the presentation object aPresentation.
        The display attributes of these elements is defined by
        the attribute manager aDrawer.
        If the Boolean drawFromCenter is false, the
        arrowhead will point towards the center of aCircle.
        If the Boolean reverseArrow is true, the arrowhead
        will point away from the attachment point.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, AttachmentPoint: nanoocp.gp.gp_Pnt, Center: nanoocp.gp.gp_Pnt, EndOfArrow: nanoocp.gp.gp_Pnt, ArrowSide: DsgPrs_ArrowSide, drawFromCenter: bool = True, reverseArrow: bool = False) -> None:
        """
        Adds the circle aCircle, the text aText, the points
        AttachmentPoint, Center and EndOfArrow to the
        presentation object aPresentation.
        The display attributes of these elements is defined by
        the attribute manager aDrawer.
        The value of the enumeration Arrowside determines
        the type of arrow displayed: whether there will be
        arrowheads at both ends or only one, for example.
        If the Boolean drawFromCenter is false, the
        arrowhead will point towards the center of aCircle.
        If the Boolean reverseArrow is true, the arrowhead
        will point away from the attachment point.
        """

class DsgPrs_ShadedPlanePresentation:
    """A framework to define display of shaded planes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_ShadedPlanePresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aPt1: nanoocp.gp.gp_Pnt, aPt2: nanoocp.gp.gp_Pnt, aPt3: nanoocp.gp.gp_Pnt) -> None:
        """
        Adds the points aPt1, aPt2 and aPt3 to the
        presentation object, aPresentation.
        The display attributes of the shaded plane are
        defined by the attribute manager aDrawer.
        """

class DsgPrs_ShapeDirPresentation:
    """
    A framework to define display of the normal to the
    surface of a shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_ShapeDirPresentation) -> None: ...

    @staticmethod
    def Add(prs: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, shape: nanoocp.TopoDS.TopoDS_Shape, mode: int) -> None:
        """
        Adds the shape shape and the mode mode to the
        presentation object prs.
        The display attributes of the normal are defined by the
        attribute manager aDrawer.
        mode determines whether the first or the last point of
        the normal is given to the presentation object. If the
        first point: 0; if the last point, 1.
        """

class DsgPrs_SymbPresentation:
    """A framework to define display of symbols."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_SymbPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aText: nanoocp.TCollection.TCollection_ExtendedString, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Adds the text aText and the point OffsetPoint to the
        presentation object aPresentation.
        The display attributes of the shaded plane are
        defined by the attribute manager aDrawer.
        """

class DsgPrs_SymmetricPresentation:
    """A framework to define display of symmetry between shapes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_SymmetricPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aDirection1: nanoocp.gp.gp_Dir, aAxis: nanoocp.gp.gp_Lin, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Adds the points OffsetPoint, AttachmentPoint1,
        AttachmentPoint2, the direction aDirection1 and the
        axis anAxis to the presentation object aPresentation.
        The display attributes of the symmetry are defined by
        the attribute manager aDrawer.
        This syntax is used for display of symmetries between two segments.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aCircle1: nanoocp.gp.gp_Circ, aAxis: nanoocp.gp.gp_Lin, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Adds the points OffsetPoint, AttachmentPoint1,
        AttachmentPoint2, the direction aDirection1 the circle
        aCircle1 and the axis anAxis to the presentation
        object aPresentation.
        The display attributes of the symmetry are defined by
        the attribute manager aDrawer.
        This syntax is used for display of symmetries between two arcs.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, AttachmentPoint1: nanoocp.gp.gp_Pnt, AttachmentPoint2: nanoocp.gp.gp_Pnt, aAxis: nanoocp.gp.gp_Lin, OffsetPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Adds the points OffsetPoint, AttachmentPoint1,
        AttachmentPoint2 and the axis anAxis to the
        presentation object aPresentation.
        The display attributes of the symmetry are defined by
        the attribute manager aDrawer.
        This syntax is used for display of symmetries between two vertices.
        """

class DsgPrs_TangentPresentation:
    """A framework to define display of tangents."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_TangentPresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, OffsetPoint: nanoocp.gp.gp_Pnt, aDirection: nanoocp.gp.gp_Dir, aLength: float) -> None:
        """
        Adds the point OffsetPoint, the direction aDirection
        and the length aLength to the presentation object aPresentation.
        The display attributes of the tangent are defined by
        the attribute manager aDrawer.
        """

class DsgPrs_XYZAxisPresentation:
    """A framework for displaying the axes of an XYZ trihedron."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_XYZAxisPresentation) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, anLineAspect: nanoocp.Prs3d.Prs3d_LineAspect | None, aDir: nanoocp.gp.gp_Dir, aVal: float, aText: str, aPfirst: nanoocp.gp.gp_Pnt, aPlast: nanoocp.gp.gp_Pnt) -> None:
        """
        Draws each axis of a trihedron displayed in the
        presentation aPresentation and with lines shown by
        the values of aLineAspect. Each axis is defined by:
        -   the first and last points aPfirst and aPlast
        -   the direction aDir and
        -   the value aVal which provides a value for length.
        The value for length is provided so that the trihedron
        can vary in length relative to the scale of shape display.
        Each axis will be identified as X, Y, or Z by the text aText.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aLineAspect: nanoocp.Prs3d.Prs3d_LineAspect | None, anArrowAspect: nanoocp.Prs3d.Prs3d_ArrowAspect | None, aTextAspect: nanoocp.Prs3d.Prs3d_TextAspect | None, aDir: nanoocp.gp.gp_Dir, aVal: float, aText: str, aPfirst: nanoocp.gp.gp_Pnt, aPlast: nanoocp.gp.gp_Pnt) -> None:
        """draws the presentation X ,Y ,Z axis"""

class DsgPrs_XYZPlanePresentation:
    """A framework for displaying the planes of an XYZ trihedron."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DsgPrs_XYZPlanePresentation) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aPt1: nanoocp.gp.gp_Pnt, aPt2: nanoocp.gp.gp_Pnt, aPt3: nanoocp.gp.gp_Pnt) -> None:
        """
        Draws each plane of a trihedron displayed in the
        presentation aPresentation and with attributes
        defined by the attribute manager aDrawer. Each
        triangular plane is defined by the points aPt1 aPt2 and aPt3.
        """
