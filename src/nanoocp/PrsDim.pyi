"""OCCT package PrsDim (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.AIS
import nanoocp.Aspect
import nanoocp.Bnd
import nanoocp.DsgPrs
import nanoocp.Geom
import nanoocp.Graphic3d
import nanoocp.NCollection
import nanoocp.Prs3d
import nanoocp.PrsMgr
import nanoocp.Quantity
import nanoocp.SelectMgr
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopoDS
import nanoocp.gp


class PrsDim_KindOfSurface(enum.IntEnum):
    PrsDim_KOS_Plane = 0

    PrsDim_KOS_Cylinder = 1

    PrsDim_KOS_Cone = 2

    PrsDim_KOS_Sphere = 3

    PrsDim_KOS_Torus = 4

    PrsDim_KOS_Revolution = 5

    PrsDim_KOS_Extrusion = 6

    PrsDim_KOS_OtherSurface = 7

PrsDim_KOS_Plane: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Plane

PrsDim_KOS_Cylinder: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Cylinder

PrsDim_KOS_Cone: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Cone

PrsDim_KOS_Sphere: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Sphere

PrsDim_KOS_Torus: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Torus

PrsDim_KOS_Revolution: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Revolution

PrsDim_KOS_Extrusion: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_Extrusion

PrsDim_KOS_OtherSurface: PrsDim_KindOfSurface = PrsDim_KindOfSurface.PrsDim_KOS_OtherSurface

class PrsDim_DimensionSelectionMode(enum.IntEnum):
    """Specifies dimension selection modes."""

    PrsDim_DimensionSelectionMode_All = 0

    PrsDim_DimensionSelectionMode_Line = 1

    PrsDim_DimensionSelectionMode_Text = 2

PrsDim_DimensionSelectionMode_All: PrsDim_DimensionSelectionMode = ...

PrsDim_DimensionSelectionMode_Line: PrsDim_DimensionSelectionMode = ...

PrsDim_DimensionSelectionMode_Text: PrsDim_DimensionSelectionMode = ...

class PrsDim_DisplaySpecialSymbol(enum.IntEnum):
    """Specifies dimension special symbol display options"""

    PrsDim_DisplaySpecialSymbol_No = 0

    PrsDim_DisplaySpecialSymbol_Before = 1

    PrsDim_DisplaySpecialSymbol_After = 2

PrsDim_DisplaySpecialSymbol_No: PrsDim_DisplaySpecialSymbol = ...

PrsDim_DisplaySpecialSymbol_Before: PrsDim_DisplaySpecialSymbol = ...

PrsDim_DisplaySpecialSymbol_After: PrsDim_DisplaySpecialSymbol = ...

class PrsDim_KindOfDimension(enum.IntEnum):
    """
    Declares the kinds of dimensions needed in the
    display of Interactive Objects.
    """

    PrsDim_KOD_NONE = 0

    PrsDim_KOD_LENGTH = 1

    PrsDim_KOD_PLANEANGLE = 2

    PrsDim_KOD_SOLIDANGLE = 3

    PrsDim_KOD_AREA = 4

    PrsDim_KOD_VOLUME = 5

    PrsDim_KOD_MASS = 6

    PrsDim_KOD_TIME = 7

    PrsDim_KOD_RADIUS = 8

    PrsDim_KOD_DIAMETER = 9

    PrsDim_KOD_CHAMF2D = 10

    PrsDim_KOD_CHAMF3D = 11

    PrsDim_KOD_OFFSET = 12

    PrsDim_KOD_ELLIPSERADIUS = 13

PrsDim_KOD_NONE: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_NONE

PrsDim_KOD_LENGTH: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_LENGTH

PrsDim_KOD_PLANEANGLE: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_PLANEANGLE

PrsDim_KOD_SOLIDANGLE: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_SOLIDANGLE

PrsDim_KOD_AREA: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_AREA

PrsDim_KOD_VOLUME: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_VOLUME

PrsDim_KOD_MASS: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_MASS

PrsDim_KOD_TIME: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_TIME

PrsDim_KOD_RADIUS: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_RADIUS

PrsDim_KOD_DIAMETER: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_DIAMETER

PrsDim_KOD_CHAMF2D: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_CHAMF2D

PrsDim_KOD_CHAMF3D: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_CHAMF3D

PrsDim_KOD_OFFSET: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_OFFSET

PrsDim_KOD_ELLIPSERADIUS: PrsDim_KindOfDimension = PrsDim_KindOfDimension.PrsDim_KOD_ELLIPSERADIUS

class PrsDim_TypeOfAngle(enum.IntEnum):
    """Declares the type of angle."""

    PrsDim_TypeOfAngle_Interior = 0

    PrsDim_TypeOfAngle_Exterior = 1

PrsDim_TypeOfAngle_Interior: PrsDim_TypeOfAngle = PrsDim_TypeOfAngle.PrsDim_TypeOfAngle_Interior

PrsDim_TypeOfAngle_Exterior: PrsDim_TypeOfAngle = PrsDim_TypeOfAngle.PrsDim_TypeOfAngle_Exterior

class PrsDim_TypeOfAngleArrowVisibility(enum.IntEnum):
    """Declares what arrows are visible on angle presentation"""

    PrsDim_TypeOfAngleArrowVisibility_Both = 0

    PrsDim_TypeOfAngleArrowVisibility_First = 1

    PrsDim_TypeOfAngleArrowVisibility_Second = 2

    PrsDim_TypeOfAngleArrowVisibility_None = 3

PrsDim_TypeOfAngleArrowVisibility_Both: PrsDim_TypeOfAngleArrowVisibility = ...

PrsDim_TypeOfAngleArrowVisibility_First: PrsDim_TypeOfAngleArrowVisibility = ...

PrsDim_TypeOfAngleArrowVisibility_Second: PrsDim_TypeOfAngleArrowVisibility = ...

PrsDim_TypeOfAngleArrowVisibility_None: PrsDim_TypeOfAngleArrowVisibility = ...

class PrsDim_TypeOfDist(enum.IntEnum):
    """To declare the type of distance."""

    PrsDim_TypeOfDist_Unknown = 0

    PrsDim_TypeOfDist_Horizontal = 1

    PrsDim_TypeOfDist_Vertical = 2

PrsDim_TypeOfDist_Unknown: PrsDim_TypeOfDist = PrsDim_TypeOfDist.PrsDim_TypeOfDist_Unknown

PrsDim_TypeOfDist_Horizontal: PrsDim_TypeOfDist = PrsDim_TypeOfDist.PrsDim_TypeOfDist_Horizontal

PrsDim_TypeOfDist_Vertical: PrsDim_TypeOfDist = PrsDim_TypeOfDist.PrsDim_TypeOfDist_Vertical

class PrsDim_KindOfRelation(enum.IntEnum):
    PrsDim_KOR_NONE = 0

    PrsDim_KOR_CONCENTRIC = 1

    PrsDim_KOR_EQUALDISTANCE = 2

    PrsDim_KOR_EQUALRADIUS = 3

    PrsDim_KOR_FIX = 4

    PrsDim_KOR_IDENTIC = 5

    PrsDim_KOR_OFFSET = 6

    PrsDim_KOR_PARALLEL = 7

    PrsDim_KOR_PERPENDICULAR = 8

    PrsDim_KOR_TANGENT = 9

    PrsDim_KOR_SYMMETRIC = 10

PrsDim_KOR_NONE: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_NONE

PrsDim_KOR_CONCENTRIC: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_CONCENTRIC

PrsDim_KOR_EQUALDISTANCE: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_EQUALDISTANCE

PrsDim_KOR_EQUALRADIUS: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_EQUALRADIUS

PrsDim_KOR_FIX: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_FIX

PrsDim_KOR_IDENTIC: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_IDENTIC

PrsDim_KOR_OFFSET: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_OFFSET

PrsDim_KOR_PARALLEL: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_PARALLEL

PrsDim_KOR_PERPENDICULAR: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_PERPENDICULAR

PrsDim_KOR_TANGENT: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_TANGENT

PrsDim_KOR_SYMMETRIC: PrsDim_KindOfRelation = PrsDim_KindOfRelation.PrsDim_KOR_SYMMETRIC

class PrsDim:
    """Auxiliary methods for computing dimensions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PrsDim) -> None: ...

    @overload
    @staticmethod
    def Nearest(aShape: nanoocp.TopoDS.TopoDS_Shape, aPoint: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Returns the nearest point in a shape. This is used by
        several classes in calculation of dimensions.
        """

    @overload
    @staticmethod
    def Nearest(theLine: nanoocp.gp.gp_Lin, thePoint: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """@return the nearest point on the line."""

    @overload
    @staticmethod
    def Nearest(theCurve: nanoocp.Geom.Geom_Curve | None, thePoint: nanoocp.gp.gp_Pnt, theFirstPoint: nanoocp.gp.gp_Pnt, theLastPoint: nanoocp.gp.gp_Pnt, theNearestPoint: nanoocp.gp.gp_Pnt) -> bool:
        """
        For the given point finds nearest point on the curve,
        @return TRUE if found point is belongs to the curve
        and FALSE otherwise.
        """

    @staticmethod
    def Farest(aShape: nanoocp.TopoDS.TopoDS_Shape, aPoint: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def ComputeGeometry__Geom_Curve(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFirstPnt: nanoocp.gp.gp_Pnt, theLastPnt: nanoocp.gp.gp_Pnt) -> tuple[bool, nanoocp.Geom.Geom_Curve]:
        """
        ComputeGeometry__Geom_Curve: the C++ overload ComputeGeometry(const TopoDS_Edge &, occ::handle<Geom_Curve> &, gp_Pnt &, gp_Pnt &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Used by 2d Relation only
        Computes the 3d geometry of <anEdge> in the current WorkingPlane
        and the extremities if any
        Return TRUE if ok.
        """

    @staticmethod
    def ComputeGeometry__Geom_Curve__bool(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFirstPnt: nanoocp.gp.gp_Pnt, theLastPnt: nanoocp.gp.gp_Pnt) -> tuple[bool, nanoocp.Geom.Geom_Curve, bool]:
        """
        ComputeGeometry__Geom_Curve__bool: the C++ overload ComputeGeometry(const TopoDS_Edge &, occ::handle<Geom_Curve> &, gp_Pnt &, gp_Pnt &, bool &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Used by dimensions only.
        Computes the 3d geometry of <anEdge>.
        Return TRUE if ok.
        """

    @overload
    @staticmethod
    def ComputeGeometry(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFirstPnt: nanoocp.gp.gp_Pnt, theLastPnt: nanoocp.gp.gp_Pnt, thePlane: nanoocp.Geom.Geom_Plane | None) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom.Geom_Curve, bool, bool]:
        """
        Used by 2d Relation only
        Computes the 3d geometry of <anEdge> in the current WorkingPlane
        and the extremities if any.
        If <aCurve> is not in the current plane, <extCurve> contains
        the not projected curve associated to <anEdge>.
        If <anEdge> is infinite, <isinfinite> = true and the 2
        parameters <FirstPnt> and <LastPnt> have no signification.
        Return TRUE if ok.
        """

    @overload
    @staticmethod
    def ComputeGeometry(theFirstEdge: nanoocp.TopoDS.TopoDS_Edge, theSecondEdge: nanoocp.TopoDS.TopoDS_Edge, theFirstPnt1: nanoocp.gp.gp_Pnt, theLastPnt1: nanoocp.gp.gp_Pnt, theFirstPnt2: nanoocp.gp.gp_Pnt, theLastPnt2: nanoocp.gp.gp_Pnt) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom.Geom_Curve, bool, bool]:
        """
        Used by dimensions only.Computes the 3d geometry
        of<anEdge1> and <anEdge2> and checks if they are infinite.
        """

    @overload
    @staticmethod
    def ComputeGeometry(aVertex: nanoocp.TopoDS.TopoDS_Vertex, point: nanoocp.gp.gp_Pnt, aPlane: nanoocp.Geom.Geom_Plane | None) -> tuple[bool, bool]: ...

    @staticmethod
    def ComputeGeometry__Geom_Curve__Geom_Curve(theFirstEdge: nanoocp.TopoDS.TopoDS_Edge, theSecondEdge: nanoocp.TopoDS.TopoDS_Edge, theFirstPnt1: nanoocp.gp.gp_Pnt, theLastPnt1: nanoocp.gp.gp_Pnt, theFirstPnt2: nanoocp.gp.gp_Pnt, theLastPnt2: nanoocp.gp.gp_Pnt, thePlane: nanoocp.Geom.Geom_Plane | None) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom.Geom_Curve]:
        """
        ComputeGeometry__Geom_Curve__Geom_Curve: the C++ overload ComputeGeometry(const TopoDS_Edge &, const TopoDS_Edge &, occ::handle<Geom_Curve> &, occ::handle<Geom_Curve> &, gp_Pnt &, gp_Pnt &, gp_Pnt &, gp_Pnt &, const occ::handle<Geom_Plane> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Used by 2d Relation only
        Computes the 3d geometry of <anEdge> in the current WorkingPlane
        and the extremities if any
        Return TRUE if ok.
        """

    @staticmethod
    def ComputeGeometry__int__Geom_Curve__Geom_Curve__Geom_Curve__bool__bool(theFirstEdge: nanoocp.TopoDS.TopoDS_Edge, theSecondEdge: nanoocp.TopoDS.TopoDS_Edge, theFirstPnt1: nanoocp.gp.gp_Pnt, theLastPnt1: nanoocp.gp.gp_Pnt, theFirstPnt2: nanoocp.gp.gp_Pnt, theLastPnt2: nanoocp.gp.gp_Pnt, thePlane: nanoocp.Geom.Geom_Plane | None) -> tuple[bool, int, nanoocp.Geom.Geom_Curve, nanoocp.Geom.Geom_Curve, nanoocp.Geom.Geom_Curve, bool, bool]:
        """
        ComputeGeometry__int__Geom_Curve__Geom_Curve__Geom_Curve__bool__bool: the C++ overload ComputeGeometry(const TopoDS_Edge &, const TopoDS_Edge &, int &, occ::handle<Geom_Curve> &, occ::handle<Geom_Curve> &, gp_Pnt &, gp_Pnt &, gp_Pnt &, gp_Pnt &, occ::handle<Geom_Curve> &, bool &, bool &, const occ::handle<Geom_Plane> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Used by 2d Relation only Computes the 3d geometry
        of<anEdge1> and <anEdge2> in the current Plane and the
        extremities if any. Return in ExtCurve the 3d curve
        (not projected in the plane) of the first edge if
        <indexExt> =1 or of the 2nd edge if <indexExt> = 2. If
        <indexExt> = 0, ExtCurve is Null. if there is an edge
        external to the plane, <isinfinite> is true if this
        edge is infinite. So, the extremities of it are not
        significant. Return TRUE if ok
        """

    @staticmethod
    def ComputeGeomCurve(first1: float, last1: float, FirstPnt1: nanoocp.gp.gp_Pnt, LastPnt1: nanoocp.gp.gp_Pnt, aPlane: nanoocp.Geom.Geom_Plane | None) -> tuple[bool, nanoocp.Geom.Geom_Curve, bool]:
        """
        Checks if aCurve belongs to aPlane; if not, projects aCurve in aPlane
        and returns aCurve;
        Return TRUE if ok
        """

    @staticmethod
    def GetPlaneFromFace(aFace: nanoocp.TopoDS.TopoDS_Face, aPlane: nanoocp.gp.gp_Pln) -> tuple[bool, nanoocp.Geom.Geom_Surface, PrsDim_KindOfSurface, float]:
        """
        Tries to get Plane from Face. Returns Surface of Face
        in aSurf. Returns true and Plane of Face in
        aPlane in following cases:
        Face is Plane, Offset of Plane,
        Extrusion of Line and Offset of Extrusion of Line
        Returns pure type of Surface which can be:
        Plane, Cylinder, Cone, Sphere, Torus,
        SurfaceOfRevolution, SurfaceOfExtrusion
        """

    @staticmethod
    def InitFaceLength(aFace: nanoocp.TopoDS.TopoDS_Face, aPlane: nanoocp.gp.gp_Pln) -> tuple[nanoocp.Geom.Geom_Surface, PrsDim_KindOfSurface, float]: ...

    @staticmethod
    def InitLengthBetweenCurvilinearFaces(theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face, theFirstAttach: nanoocp.gp.gp_Pnt, theSecondAttach: nanoocp.gp.gp_Pnt, theDirOnPlane: nanoocp.gp.gp_Dir) -> tuple[nanoocp.Geom.Geom_Surface, nanoocp.Geom.Geom_Surface]:
        """
        Finds attachment points on two curvilinear faces for length dimension.
        @param[in] thePlaneDir  the direction on the dimension plane to
        compute the plane automatically. It will not be taken into account if
        plane is defined by user.
        """

    @staticmethod
    def InitAngleBetweenPlanarFaces(theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face, theCenter: nanoocp.gp.gp_Pnt, theFirstAttach: nanoocp.gp.gp_Pnt, theSecondAttach: nanoocp.gp.gp_Pnt, theIsFirstPointSet: bool = False) -> bool:
        """
        Finds three points for the angle dimension between
        two planes.
        """

    @staticmethod
    def InitAngleBetweenCurvilinearFaces(theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face, theFirstSurfType: PrsDim_KindOfSurface, theSecondSurfType: PrsDim_KindOfSurface, theCenter: nanoocp.gp.gp_Pnt, theFirstAttach: nanoocp.gp.gp_Pnt, theSecondAttach: nanoocp.gp.gp_Pnt, theIsFirstPointSet: bool = False) -> bool:
        """
        Finds three points for the angle dimension between
        two curvilinear surfaces.
        """

    @staticmethod
    def ProjectPointOnPlane(aPoint: nanoocp.gp.gp_Pnt, aPlane: nanoocp.gp.gp_Pln) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def ProjectPointOnLine(aPoint: nanoocp.gp.gp_Pnt, aLine: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def TranslatePointToBound(aPoint: nanoocp.gp.gp_Pnt, aDir: nanoocp.gp.gp_Dir, aBndBox: nanoocp.Bnd.Bnd_Box) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def InDomain(aFirstPar: float, aLastPar: float, anAttachPar: float) -> bool:
        """
        returns True if point with anAttachPar is
        in domain of arc
        """

    @staticmethod
    def NearestApex(elips: nanoocp.gp.gp_Elips, pApex: nanoocp.gp.gp_Pnt, nApex: nanoocp.gp.gp_Pnt, fpara: float, lpara: float) -> tuple[nanoocp.gp.gp_Pnt, bool]:
        """computes nearest to ellipse arc apex"""

    @staticmethod
    def DistanceFromApex(elips: nanoocp.gp.gp_Elips, Apex: nanoocp.gp.gp_Pnt, par: float) -> float:
        """computes length of ellipse arc in parametric units"""

    @staticmethod
    def ComputeProjEdgePresentation(aPres: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, anEdge: nanoocp.TopoDS.TopoDS_Edge, ProjCurve: nanoocp.Geom.Geom_Curve | None, FirstP: nanoocp.gp.gp_Pnt, LastP: nanoocp.gp.gp_Pnt, aColor: nanoocp.Quantity.Quantity_NameOfColor = Quantity_NameOfColor.Quantity_NOC_PURPLE, aWidth: float = 2.0, aProjTOL: nanoocp.Aspect.Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_DASH, aCallTOL: nanoocp.Aspect.Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_DOT) -> None: ...

    @staticmethod
    def ComputeProjVertexPresentation(aPres: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aVertex: nanoocp.TopoDS.TopoDS_Vertex, ProjPoint: nanoocp.gp.gp_Pnt, aColor: nanoocp.Quantity.Quantity_NameOfColor = Quantity_NameOfColor.Quantity_NOC_PURPLE, aWidth: float = 2.0, aProjTOM: nanoocp.Aspect.Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_PLUS, aCallTOL: nanoocp.Aspect.Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_DOT) -> None: ...

class PrsDim_DimensionOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """
    The owner is the entity which makes it possible to link
    the sensitive primitives and the reference shapes that
    you want to detect. It stocks the various pieces of
    information which make it possible to find objects. An
    owner has a priority which you can modulate, so as to
    make one entity more selectable than another. You
    might want to make edges more selectable than
    faces, for example. In that case, you could attribute sa
    higher priority to the one compared to the other. An
    edge, could have priority 5, for example, and a face,
    priority 4. The default priority is 5.
    """

    @overload
    def __init__(self, theSelObject: nanoocp.SelectMgr.SelectMgr_SelectableObject | None, theSelMode: PrsDim_DimensionSelectionMode, thePriority: int = 0) -> None:
        """
        Initializes the dimension owner, theSO, and attributes it
        the priority, thePriority.
        """

    @overload
    def __init__(self, theOther: PrsDim_DimensionOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SelectionMode(self) -> PrsDim_DimensionSelectionMode: ...

    def HilightWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None: ...

    def IsHilighted(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int = 0) -> bool:
        """
        Returns true if an object with the selection mode
        aMode is highlighted in the presentation manager aPM.
        """

    def Unhilight(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int = 0) -> None:
        """Removes highlighting from the selected part of dimension."""

class PrsDim_Dimension(nanoocp.AIS.AIS_InteractiveObject):
    """
    PrsDim_Dimension is a base class for 2D presentations of linear (length, diameter, radius)
    and angular dimensions.

    The dimensions provide measurement of quantities, such as lengths or plane angles.
    The measurement of dimension "value" is done in model space "as is".
    These "value" are said to be represented in "model units", which can be specified by user.
    During the display the measured value converted from "model units" to "display units".
    The display and model units are stored in common Prs3d_Drawer (drawer of the context)
    to share it between all dimensions.
    The specified by user units are stored in the dimension's drawer.

    As a drawing, the dimension is composed from the following components:
    - Attachment (binding) points. The points where the dimension lines attaches to, for
    length dimensions the distances are measured between these points.
    - Main dimension line. The which extends from the attachment points in "up" direction,
    and which contains text label on it with value string.
    - Flyouts. The lines connecting the attachment points with main dimension line.
    - Extension. The lines used to extend the main dimension line in the cases when text
    or arrows do not fit into the main dimension line due to their size.
    - Arrows.

    <pre>
    Linear dimensions:

    extension
    line                                     arrow
    -->|------- main dimension line -------|<--
    |                                   |
    |flyout                       flyout|
    |                                   |
    +-----------------------------------+
    attachment                                attachment
    point                                       point

    Angular dimensions:

    extension
    line
    -->|+++++
    arrow |     +++
    |        90(deg) - main dimension line
    flyout |         +++
    |           +
    o---flyout---
    center         ^
    point          | extension
    line
    </pre>

    Being a 2D drawings, the dimensions are created on imaginary plane, called "dimension plane",
    which can be thought of as reference system of axes (X,Y,N) for constructing the presentation.

    The role of axes of the dimension plane is to guide you through the encapsulated automations
    of presentation building to help you understand how is the presentation will look and how it
    will be oriented in model space during construction.

    Orientation of dimension line in model space relatively to the base shapes is defined
    with the flyouts. Flyouts specify length of flyout lines and their orientation relatively
    to the attachment points on the working plane.
    For linear dimensions:
    Direction of flyouts is specified with direction of main dimension line
    (vector from the first attachment to the second attachment) and the normal of the dimension
    plane. Positive direction of flyouts is defined by vector multiplication: AttachVector *
    PlaneNormal.
    For angular dimensions:
    Flyouts are defined by vectors from the center point to the attachment points.
    These vectors directions are supposed to be the positive directions of flyouts.
    Negative flyouts directions means that these vectors should be reversed
    (and dimension will be built out of the angle constructed with center and two attach points).

    The dimension plane can be constructed automatically by application (where possible,
    it depends on the measured geometry).
    It can be also set by user. However, if the user-defined plane does not fit the
    geometry of the dimension (attach points do not belong to it), the dimension could not
    be built.
    If it is not possible to compute automatic plane (for example, in case of length between
    two points) the user is supposed to specify the custom plane.

    Since the dimensions feature automated construction procedures from an arbitrary shapes,
    the interfaces to check the validness are also implemented. Once the measured geometry is
    specified, the one can inquire the validness status by calling "IsValid()" method. If the result
    is TRUE, then all of public parameters should be pre-computed and ready. The presentation
    should be also computable. Otherwise, the parameters may return invalid values. In this case,
    the presentation will not be computed and displayed.

    The dimension support two local selection modes: main dimension line selection and text label
    selection. These modes can be used to develop interactive modification of dimension
    presentations. The component highlighting in these selection modes is provided by
    PrsDim_DimensionOwner class. Please note that selection is unavailable until the presentation is
    computed.

    The specific drawing attributes are controlled through Prs3d_DimensionAspect. The one can change
    color, arrows, text and arrow style and specify positioning of value label by setting
    corresponding values to the aspect.

    Such set of parameters that consists of:
    - flyout size and direction,
    - user-defined dimension plane,
    - horizontal and vertical text alignment
    can be uniquely replaced with text position in 3d space. Therefore, there are methods to convert
    this set of parameters to the text position and vice versa:

    - If the fixed text position is defined by user, called SetTextPosition (theTextPos) method
    converts this 3d point to the set of parameters including adjusting of the dimension plane (this
    plane will be automatic plane, NOT user-defined one). If the fixed text position is set, the
    flag myIsFixedTextPosition is set to TRUE. ATTENTION! myIsFixedTextPosition fixes all parameters
    of the set from recomputing inside SetMeasureGeometry() methods. Parameters in dimension aspect
    (they are horizontal text position and extension size) are adjusted on presentation computing
    step, user-defined values in dimension aspect are not changed. But plane and flyout as dimension
    position parameters are changed by SetTextPosition() method according with user-defined text
    position. If parameters from the set are changed by user with calls of setters, it leads to
    disabling of fixed text position (myIsFixedTextPosition is set to FALSE). If the fixed text
    position is set and geometry is changed by user (SetMeasureGeometry() method is called) and the
    geometry doesn't satisfy computed dimension plane, the dimension is not valid.

    - If the set of parameters was set by user (may be without the user-defined plane or with it),
    it can be converted to the text position by calling the method GetTextPosition(). In this case
    the text position is NOT fixed, and SetMeasureGeometry() without user-defined plane adjusts
    the automatic plane according input geometry (if it is possible).
    """

    class ComputeMode(enum.IntEnum):
        """
        Specifies supported presentation compute modes.
        Used to compute only parts of presentation for
        advanced highlighting.
        """

        ComputeMode_All = 0

        ComputeMode_Line = 1

        ComputeMode_Text = 2

    ComputeMode_All: PrsDim_Dimension.ComputeMode = ComputeMode.ComputeMode_All

    ComputeMode_Line: PrsDim_Dimension.ComputeMode = ComputeMode.ComputeMode_Line

    ComputeMode_Text: PrsDim_Dimension.ComputeMode = ComputeMode.ComputeMode_Text

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetValue(self) -> float:
        """
        Gets dimension measurement value. If the value to display is not
        specified by user, then the dimension object is responsible to
        compute it on its own in model space coordinates.
        @return the dimension value (in model units) which is used
        during display of the presentation.
        """

    def SetComputedValue(self) -> None:
        """Sets computed dimension value. Resets custom value mode if it was set."""

    @overload
    def SetCustomValue(self, theValue: float) -> None:
        """
        Sets user-defined dimension value.
        The user-defined dimension value is specified in model space,
        and affect by unit conversion during the display.
        @param[in] theValue  the user-defined value to display.
        """

    @overload
    def SetCustomValue(self, theValue: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Sets user-defined dimension value.
        Unit conversion during the display is not applied.
        @param[in] theValue  the user-defined value to display.
        """

    def GetCustomValue(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Gets user-defined dimension value.
        @return dimension value string.
        """

    def GetPlane(self) -> nanoocp.gp.gp_Pln:
        """
        Get the dimension plane in which the 2D dimension presentation is computed.
        By default, if plane is not defined by user, it is computed automatically
        after dimension geometry is computed.
        If computed dimension geometry (points) can't be placed on the user-defined
        plane, dimension geometry was set as invalid (validity flag is set to false)
        and dimension presentation will not be computed.
        If user-defined plane allow geometry placement on it, it will be used for
        computing of the dimension presentation.
        @return dimension plane used for presentation computing.
        """

    def GetGeometryType(self) -> int:
        """
        Geometry type defines type of shapes on which the dimension is to be built.
        @return type of geometry on which the dimension will be built.
        """

    def SetCustomPlane(self, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Sets user-defined plane where the 2D dimension presentation will be placed.
        Checks validity of this plane if geometry has been set already.
        Validity of the plane is checked according to the geometry set
        and has different criteria for different kinds of dimensions.
        """

    def UnsetCustomPlane(self) -> None:
        """
        Unsets user-defined plane. Therefore the plane for dimension will be
        computed automatically.
        """

    def IsTextPositionCustom(self) -> bool:
        """
        @return TRUE if text position is set by user with method SetTextPosition().
        """

    def SetTextPosition(self, arg0: nanoocp.gp.gp_Pnt) -> None:
        """
        Fixes the absolute text position and adjusts flyout, plane and text alignment
        according to it. Updates presentation if the text position is valid.
        ATTENTION! It does not change vertical text alignment.
        @param[in] theTextPos  the point of text position.
        """

    def GetTextPosition(self) -> nanoocp.gp.gp_Pnt:
        """
        Computes absolute text position from dimension parameters
        (flyout, plane and text alignment).
        """

    def DimensionAspect(self) -> nanoocp.Prs3d.Prs3d_DimensionAspect:
        """
        Gets the dimension aspect from AIS object drawer.
        Dimension aspect contains aspects of line, text and arrows for dimension presentation.
        """

    def SetDimensionAspect(self, theDimensionAspect: nanoocp.Prs3d.Prs3d_DimensionAspect | None) -> None:
        """
        Sets new dimension aspect for the interactive object drawer.
        The dimension aspect provides dynamic properties which are generally
        used during computation of dimension presentations.
        """

    def KindOfDimension(self) -> PrsDim_KindOfDimension:
        """@return the kind of dimension."""

    def Type(self) -> nanoocp.AIS.AIS_KindOfInteractive:
        """@return the kind of interactive."""

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        Returns true if the class of objects accepts the display mode theMode.
        The interactive context can have a default mode of representation for
        the set of Interactive Objects. This mode may not be accepted by object.
        """

    def DisplaySpecialSymbol(self) -> PrsDim_DisplaySpecialSymbol:
        """@return dimension special symbol display options."""

    def SetDisplaySpecialSymbol(self, theDisplaySpecSymbol: PrsDim_DisplaySpecialSymbol) -> None:
        """Specifies whether to display special symbol or not."""

    def SpecialSymbol(self) -> str:
        """@return special symbol."""

    def SetSpecialSymbol(self, theSpecialSymbol: str) -> None:
        """Specifies special symbol."""

    def GetDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def GetModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetDisplayUnits(self, arg0: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetModelUnits(self, arg0: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def UnsetFixedTextPosition(self) -> None:
        """
        Unsets user defined text positioning and enables text positioning
        by other parameters: text alignment, extension size, flyout and custom plane.
        """

    def SelToleranceForText2d(self) -> float:
        """
        Returns selection tolerance for text2d:
        For 2d text selection detection sensitive point with tolerance is used
        Important! Only for 2d text.
        """

    def SetSelToleranceForText2d(self, theTol: float) -> None:
        """
        Sets selection tolerance for text2d:
        For 2d text selection detection sensitive point with tolerance is used
        to change this tolerance use this method
        Important! Only for 2d text.
        """

    def GetFlyout(self) -> float:
        """@return flyout value for dimension."""

    def SetFlyout(self, theFlyout: float) -> None:
        """Sets flyout value for dimension."""

    def IsValid(self) -> bool:
        """
        Check that the input geometry for dimension is valid and the
        presentation can be successfully computed.
        @return TRUE if dimension geometry is ok.
        """

class PrsDim_AngleDimension(PrsDim_Dimension):
    """
    Angle dimension. Can be constructed:
    - on two intersected edges.
    - on three points or vertices.
    - on conical face.
    - between two intersected faces.

    In case of three points or two intersected edges the dimension plane
    (on which dimension presentation is built) can be computed uniquely
    as through three defined points can be built only one plane.
    Therefore, if user-defined plane differs from this one, the dimension can't be built.

    In cases of two planes automatic plane by default is built on point of the
    origin of parametric space of the first face (the basis surface) so, that
    the working plane and two faces intersection forms minimal angle between the faces.
    User can define the other point which the dimension plane should pass through
    using the appropriate constructor. This point can lay on the one of the faces or not.
    Also user can define his own plane but it should pass through the three points
    computed on the geometry initialization step (when the constructor or SetMeasuredGeometry()
    method is called).

    In case of the conical face the center point of the angle is the apex of the conical surface.
    The attachment points are points of the first and the last parameter of the basis circle of the
    cone.
    """

    @overload
    def __init__(self, theCone: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Constructs angle dimension for the cone face.
        @param[in] theCone  the conical face.
        """

    @overload
    def __init__(self, theFirstEdge: nanoocp.TopoDS.TopoDS_Edge, theSecondEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Constructs minimum angle dimension between two linear edges (where possible).
        These two edges should be intersected by each other. Otherwise the geometry is not valid.
        @param[in] theFirstEdge  the first edge.
        @param[in] theSecondEdge  the second edge.
        """

    @overload
    def __init__(self, theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Constructs angle dimension between two planar faces.
        @param[in] theFirstFace  the first face.
        @param[in] theSecondFace  the second face.
        """

    @overload
    def __init__(self, theFirstPoint: nanoocp.gp.gp_Pnt, theSecondPoint: nanoocp.gp.gp_Pnt, theThirdPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs the angle display object defined by three points.
        @param[in] theFirstPoint  the first point (point on first angle flyout).
        @param[in] theSecondPoint  the center point of angle dimension.
        @param[in] theThirdPoint  the second point (point on second angle flyout).
        """

    @overload
    def __init__(self, theFirstVertex: nanoocp.TopoDS.TopoDS_Vertex, theSecondVertex: nanoocp.TopoDS.TopoDS_Vertex, theThirdVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Constructs the angle display object defined by three vertices.
        @param[in] theFirstVertex  the first vertex (vertex for first angle flyout).
        @param[in] theSecondVertex  the center vertex of angle dimension.
        @param[in] theThirdPoint  the second vertex (vertex for second angle flyout).
        """

    @overload
    def __init__(self, theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Constructs angle dimension between two planar faces.
        @param[in] theFirstFace  the first face.
        @param[in] theSecondFace  the second face.
        @param[in] thePoint  the point which the dimension plane should pass through.
        This point can lay on the one of the faces or not.
        """

    @overload
    def __init__(self, theOther: PrsDim_AngleDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def FirstPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return first point forming the angle."""

    def SecondPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return second point forming the angle."""

    def CenterPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return center point forming the angle."""

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return first argument shape."""

    def SecondShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return second argument shape."""

    def ThirdShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return third argument shape."""

    @overload
    def SetMeasuredGeometry(self, theFirstEdge: nanoocp.TopoDS.TopoDS_Edge, theSecondEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Measures minimum angle dimension between two linear edges.
        These two edges should be intersected by each other. Otherwise the geometry is not valid.
        @param[in] theFirstEdge  the first edge.
        @param[in] theSecondEdge  the second edge.
        """

    @overload
    def SetMeasuredGeometry(self, theFirstPoint: nanoocp.gp.gp_Pnt, theSecondPoint: nanoocp.gp.gp_Pnt, theThridPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Measures angle defined by three points.
        @param[in] theFirstPoint  the first point (point on first angle flyout).
        @param[in] theSecondPoint  the center point of angle dimension.
        @param[in] theThirdPoint  the second point (point on second angle flyout).
        """

    @overload
    def SetMeasuredGeometry(self, theFirstVertex: nanoocp.TopoDS.TopoDS_Vertex, theSecondVertex: nanoocp.TopoDS.TopoDS_Vertex, theThirdVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Measures angle defined by three vertices.
        @param[in] theFirstVertex  the first vertex (vertex for first angle flyout).
        @param[in] theSecondVertex  the center vertex of angle dimension.
        @param[in] theThirdPoint  the second vertex (vertex for second angle flyout).
        """

    @overload
    def SetMeasuredGeometry(self, theCone: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Measures angle of conical face.
        @param[in] theCone  the shape to measure.
        """

    @overload
    def SetMeasuredGeometry(self, theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Measures angle between two planar faces.
        @param[in] theFirstFace  the first face.
        @param[in] theSecondFace  the second face..
        """

    @overload
    def SetMeasuredGeometry(self, theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Measures angle between two planar faces.
        @param[in] theFirstFace  the first face.
        @param[in] theSecondFace  the second face.
        @param[in] thePoint  the point which the dimension plane should pass through.
        This point can lay on the one of the faces or not.
        """

    def GetDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the display units string."""

    def GetModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the model units string."""

    def SetDisplayUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetModelUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetTextPosition(self, theTextPos: nanoocp.gp.gp_Pnt) -> None:
        """
        Principle of horizontal text alignment settings:
        - divide circle into two halves according to attachment points
        - if aTextPos is between attach points -> Center + positive flyout
        - if aTextPos is not between attach points but in this half -> Left or Right + positive flyout
        - if aTextPos is between reflections of attach points -> Center + negative flyout
        - if aTextPos is not between reflections of attach points -> Left or Right + negative flyout
        """

    def GetTextPosition(self) -> nanoocp.gp.gp_Pnt: ...

    def SetType(self, theType: PrsDim_TypeOfAngle) -> None:
        """
        Sets angle type.
        @param[in] theType  the type value.
        """

    def GetType(self) -> PrsDim_TypeOfAngle:
        """@return the current angle type."""

    def SetArrowsVisibility(self, theType: PrsDim_TypeOfAngleArrowVisibility) -> None:
        """
        Sets visible arrows type
        @param[in] theType  the type of visibility of arrows.
        """

    def GetArrowsVisibility(self) -> PrsDim_TypeOfAngleArrowVisibility:
        """@return the type of visibility of arrows."""

class PrsDim_Relation(nanoocp.AIS.AIS_InteractiveObject):
    """
    One of the four types of interactive object in
    AIS,comprising dimensions and constraints. Serves
    as the abstract class for the seven relation classes as
    well as the seven dimension classes.
    The statuses available for relations between shapes are as follows:
    -   0 - there is no connection to a shape;
    -   1 - there is a connection to the first shape;
    -   2 - there is a connection to the second shape.
    The connection takes the form of an edge between the two shapes.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Allows you to provide settings for the color theColor
        of the lines representing the relation between the two shapes.
        """

    def UnsetColor(self) -> None:
        """
        Allows you to remove settings for the color of the
        lines representing the relation between the two shapes.
        """

    def Type(self) -> nanoocp.AIS.AIS_KindOfInteractive: ...

    def KindOfDimension(self) -> PrsDim_KindOfDimension:
        """Indicates that the type of dimension is unknown."""

    def IsMovable(self) -> bool:
        """Returns true if the interactive object is movable."""

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def SetFirstShape(self, aFShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def SecondShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the second shape."""

    def SetSecondShape(self, aSShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Allows you to identify the second shape aSShape
        relative to the first.
        """

    def SetBndBox(self, theXmin: float, theYmin: float, theZmin: float, theXmax: float, theYmax: float, theZmax: float) -> None: ...

    def UnsetBndBox(self) -> None: ...

    def Plane(self) -> nanoocp.Geom.Geom_Plane:
        """Returns the plane."""

    def SetPlane(self, thePlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Allows you to set the plane thePlane. This is used to
        define relations and dimensions in several daughter classes.
        """

    def Value(self) -> float:
        """Returns the value of each object in the relation."""

    def SetValue(self, theVal: float) -> None:
        """
        Allows you to provide settings for the value theVal for each object in the relation.
        """

    def Position(self) -> nanoocp.gp.gp_Pnt:
        """Returns the position set using SetPosition."""

    def SetPosition(self, thePosition: nanoocp.gp.gp_Pnt) -> None:
        """
        Allows you to provide the objects in the relation with
        settings for a non-default position.
        """

    def Text(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns settings for text aspect."""

    def SetText(self, theText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Allows you to provide the settings theText for text aspect."""

    def ArrowSize(self) -> float:
        """
        Returns the value for the size of the arrow identifying
        the relation between the two shapes.
        """

    def SetArrowSize(self, theArrowSize: float) -> None:
        """
        Allows you to provide settings for the size of the
        arrow theArrowSize identifying the relation between the two shapes.
        """

    def SymbolPrs(self) -> nanoocp.DsgPrs.DsgPrs_ArrowSide:
        """
        Returns the value of the symbol presentation. This will be one of:
        -   AS_NONE - none
        -   AS_FIRSTAR - first arrow
        -   AS_LASTAR - last arrow
        -   AS_BOTHAR - both arrows
        -   AS_FIRSTPT - first point
        -   AS_LASTPT - last point
        -   AS_BOTHPT - both points
        -   AS_FIRSTAR_LASTPT - first arrow, last point
        -   AS_FIRSTPT_LASTAR - first point, last arrow
        """

    def SetSymbolPrs(self, theSymbolPrs: nanoocp.DsgPrs.DsgPrs_ArrowSide) -> None:
        """Allows you to provide settings for the symbol presentation."""

    def SetExtShape(self, theIndex: int) -> None:
        """
        Allows you to set the status of the extension shape by
        the index aIndex.
        The status will be one of the following:
        -   0 - there is no connection to a shape;
        -   1 - there is a connection to the first shape;
        -   2 - there is a connection to the second shape.
        """

    def ExtShape(self) -> int:
        """Returns the status index of the extension shape."""

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        Returns true if the display mode aMode is accepted
        for the Interactive Objects in the relation.
        ComputeProjPresentation(me;
        aPres    : Presentation from Prs3d;
        Curve1   : Curve                from Geom;
        Curve2   : Curve                from Geom;
        FirstP1  : Pnt                  from gp;
        LastP1   : Pnt                  from gp;
        FirstP2  : Pnt                  from gp;
        LastP2   : Pnt                  from gp;
        aColor   : NameOfColor          from Quantity = Quantity_NOC_PURPLE;
        aWidth   : Real                 from Standard = 2;
        aProjTOL : TypeOfLine           from Aspect   = Aspect_TOL_DASH;
        aCallTOL : TypeOfLine           from Aspect   = Aspect_TOL_DOT)
        """

    def SetAutomaticPosition(self, theStatus: bool) -> None: ...

    def AutomaticPosition(self) -> bool: ...

class PrsDim_Chamf2dDimension(PrsDim_Relation):
    """
    A framework to define display of 2D chamfers.
    A chamfer is displayed with arrows and text. The text
    gives the length of the chamfer if it is a symmetrical
    chamfer, or the angle if it is not.
    """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Constructs the display object for 2D chamfers.
        This object is defined by the face aFShape, the
        dimension aVal, the plane aPlane and the text aText.
        """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aPosition: nanoocp.gp.gp_Pnt, aSymbolPrs: nanoocp.DsgPrs.DsgPrs_ArrowSide, anArrowSize: float = 0.0) -> None:
        """
        Constructs the display object for 2D chamfers.
        This object is defined by the face aFShape, the plane
        aPlane, the dimension aVal, the position aPosition,
        the type of arrow aSymbolPrs with the size
        anArrowSize, and the text aText.
        """

    @overload
    def __init__(self, theOther: PrsDim_Chamf2dDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def KindOfDimension(self) -> PrsDim_KindOfDimension:
        """Indicates that we are concerned with a 2d length."""

    def IsMovable(self) -> bool:
        """Returns true if the 2d chamfer dimension is movable."""

class PrsDim_Chamf3dDimension(PrsDim_Relation):
    """
    A framework to define display of 3D chamfers.
    A chamfer is displayed with arrows and text. The text
    gives the length of the chamfer if it is a symmetrical
    chamfer, or the angle if it is not.
    """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Constructs a display object for 3D chamfers.
        This object is defined by the shape aFShape, the
        dimension aVal and the text aText.
        """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aPosition: nanoocp.gp.gp_Pnt, aSymbolPrs: nanoocp.DsgPrs.DsgPrs_ArrowSide, anArrowSize: float = 0.0) -> None:
        """
        Constructs a display object for 3D chamfers.
        This object is defined by the shape aFShape, the
        dimension aVal, the text aText, the point of origin of
        the chamfer aPosition, the type of arrow aSymbolPrs
        with the size anArrowSize.
        """

    @overload
    def __init__(self, theOther: PrsDim_Chamf3dDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def KindOfDimension(self) -> PrsDim_KindOfDimension:
        """Indicates that we are concerned with a 3d length."""

    def IsMovable(self) -> bool:
        """Returns true if the 3d chamfer dimension is movable."""

class PrsDim_ConcentricRelation(PrsDim_Relation):
    """
    A framework to define a constraint by a relation of
    concentricity between two or more interactive datums.
    The display of this constraint is also defined.
    A plane is used to create an axis along which the
    relation of concentricity can be extended.
    """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aSShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Constructs the display object for concentric relations
        between shapes.
        This object is defined by the two shapes, aFShape
        and aSShape and the plane aPlane.
        aPlane is provided to create an axis along which the
        relation of concentricity can be extended.
        """

    @overload
    def __init__(self, theOther: PrsDim_ConcentricRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PrsDim_DiameterDimension(PrsDim_Dimension):
    """
    Diameter dimension. Can be constructed:
    - On generic circle.
    - On generic circle with user-defined anchor point on that circle
    (dimension plane is oriented to follow the anchor point).
    - On generic circle in the specified plane.
    - On generic shape containing geometry that can be measured
    by diameter dimension: circle wire, circular face, etc.
    The anchor point is the location of the left attachment point of
    dimension on the circle.
    The anchor point computation is processed after dimension plane setting
    so that positive flyout direction stands with normal of the circle and
    the normal of the plane.
    If the plane is user-defined the anchor point was computed as intersection
    of the plane and the basis circle. Among two intersection points
    the one is selected so that positive flyout direction vector and
    the circle normal on the one side form the circle plane.
    (corner between positive flyout directio nand the circle normal is acute.)
    If the plane is computed automatically (by default it is the circle plane),
    the anchor point is the zero parameter point of the circle.

    The dimension is considered as invalid if the user-defined plane
    does not include th enachor point and th ecircle center,
    if the diameter of the circle is less than Precision::Confusion().
    In case if the dimension is built on the arbitrary shape, it can be considered
    as invalid if the shape does not contain circle geometry.
    """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ) -> None:
        """
        Construct diameter dimension for the circle.
        @param[in] theCircle  the circle to measure.
        """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Construct diameter on the passed shape, if applicable.
        @param[in] theShape  the shape to measure.
        """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Construct diameter dimension for the circle and orient it correspondingly
        to the passed plane.
        @param[in] theCircle  the circle to measure.
        @param[in] thePlane  the plane defining preferred orientation
        for dimension.
        """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Construct diameter on the passed shape, if applicable - and
        define the preferred plane to orient the dimension.
        @param[in] theShape  the shape to measure.
        @param[in] thePlane  the plane defining preferred orientation
        for dimension.
        """

    @overload
    def __init__(self, theOther: PrsDim_DiameterDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Circle(self) -> nanoocp.gp.gp_Circ:
        """@return measured geometry circle."""

    def AnchorPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return anchor point on circle for diameter dimension."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return the measured shape."""

    @overload
    def SetMeasuredGeometry(self, theCircle: nanoocp.gp.gp_Circ) -> None:
        """
        Measure diameter of the circle.
        The actual dimension plane is used for determining anchor points
        on the circle to attach the dimension lines to.
        The dimension will become invalid if the diameter of the circle
        is less than Precision::Confusion().
        @param[in] theCircle  the circle to measure.
        """

    @overload
    def SetMeasuredGeometry(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Measure diameter on the passed shape, if applicable.
        The dimension will become invalid if the passed shape is not
        measurable or if measured diameter value is less than Precision::Confusion().
        @param[in] theShape  the shape to measure.
        """

    def GetDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the display units string."""

    def GetModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the model units string."""

    def SetDisplayUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetModelUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetTextPosition(self, theTextPos: nanoocp.gp.gp_Pnt) -> None: ...

    def GetTextPosition(self) -> nanoocp.gp.gp_Pnt: ...

class PrsDim_EllipseRadiusDimension(PrsDim_Relation):
    """
    Computes geometry (basis curve and plane of dimension)
    for input shape aShape from TopoDS
    Root class for MinRadiusDimension and MaxRadiusDimension
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def KindOfDimension(self) -> PrsDim_KindOfDimension: ...

    def IsMovable(self) -> bool: ...

    def ComputeGeometry(self) -> None: ...

class PrsDim_EqualDistanceRelation(PrsDim_Relation):
    """
    A framework to display equivalent distances between
    shapes and a given plane.
    The distance is the length of a projection from the
    shape to the plane.
    These distances are used to compare shapes by this vector alone.
    """

    @overload
    def __init__(self, aShape1: nanoocp.TopoDS.TopoDS_Shape, aShape2: nanoocp.TopoDS.TopoDS_Shape, aShape3: nanoocp.TopoDS.TopoDS_Shape, aShape4: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Constructs a framework to display equivalent
        distances between the shapes aShape1, aShape2,
        aShape3, aShape4 and the plane aPlane.
        The distance is the length of a projection from the
        shape to the plane.
        """

    @overload
    def __init__(self, theOther: PrsDim_EqualDistanceRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetShape3(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets the shape aShape to be used as the shape
        aShape3 in the framework created at construction time.
        """

    def Shape3(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape aShape3 from the framework
        created at construction time.
        """

    def SetShape4(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets the shape aShape to be used as the shape
        aShape4 in the framework created at construction time.
        """

    def Shape4(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape aShape4 from the framework
        created at construction time.
        """

    @staticmethod
    def ComputeTwoEdgesLength(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, ArrowSize: float, FirstEdge: nanoocp.TopoDS.TopoDS_Edge, SecondEdge: nanoocp.TopoDS.TopoDS_Edge, Plane: nanoocp.Geom.Geom_Plane | None, AutomaticPos: bool, IsSetBndBox: bool, BndBox: nanoocp.Bnd.Bnd_Box, Position: nanoocp.gp.gp_Pnt, FirstAttach: nanoocp.gp.gp_Pnt, SecondAttach: nanoocp.gp.gp_Pnt, FirstExtreme: nanoocp.gp.gp_Pnt, SecondExtreme: nanoocp.gp.gp_Pnt) -> nanoocp.DsgPrs.DsgPrs_ArrowSide:
        """
        Computes the location of an intreval between
        between two edges. FirstAttach , SecondAttach
        are the returned extreme points of the interval.
        """

    @staticmethod
    def ComputeTwoVerticesLength(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, ArrowSize: float, FirstVertex: nanoocp.TopoDS.TopoDS_Vertex, SecondVertex: nanoocp.TopoDS.TopoDS_Vertex, Plane: nanoocp.Geom.Geom_Plane | None, AutomaticPos: bool, IsSetBndBox: bool, BndBox: nanoocp.Bnd.Bnd_Box, TypeDist: PrsDim_TypeOfDist, Position: nanoocp.gp.gp_Pnt, FirstAttach: nanoocp.gp.gp_Pnt, SecondAttach: nanoocp.gp.gp_Pnt, FirstExtreme: nanoocp.gp.gp_Pnt, SecondExtreme: nanoocp.gp.gp_Pnt) -> nanoocp.DsgPrs.DsgPrs_ArrowSide:
        """
        Computes the interval position between two vertexs. FirstAttach,
        SecondAttach are the returned extreme points of the interval.
        """

    @staticmethod
    def ComputeOneEdgeOneVertexLength(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, ArrowSize: float, FirstShape: nanoocp.TopoDS.TopoDS_Shape, SecondShape: nanoocp.TopoDS.TopoDS_Shape, Plane: nanoocp.Geom.Geom_Plane | None, AutomaticPos: bool, IsSetBndBox: bool, BndBox: nanoocp.Bnd.Bnd_Box, Position: nanoocp.gp.gp_Pnt, FirstAttach: nanoocp.gp.gp_Pnt, SecondAttach: nanoocp.gp.gp_Pnt, FirstExtreme: nanoocp.gp.gp_Pnt, SecondExtreme: nanoocp.gp.gp_Pnt) -> nanoocp.DsgPrs.DsgPrs_ArrowSide:
        """
        Compute the interval location between a vertex and an edge. Edge may be
        a line or a circle.
        """

class PrsDim_EqualRadiusRelation(PrsDim_Relation):
    @overload
    def __init__(self, aFirstEdge: nanoocp.TopoDS.TopoDS_Edge, aSecondEdge: nanoocp.TopoDS.TopoDS_Edge, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Creates equal relation of two arc's radiuses.
        If one of edges is not in the given plane,
        the presentation method projects it onto the plane.
        """

    @overload
    def __init__(self, theOther: PrsDim_EqualRadiusRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PrsDim_FixRelation(PrsDim_Relation):
    """
    Constructs and manages a constraint by a fixed
    relation between two or more interactive datums. This
    constraint is represented by a wire from a shape -
    point, vertex, or edge - in the first datum and a
    corresponding shape in the second.
    Warning: This relation is not bound with any kind of parametric
    constraint : it represents the "status" of an parametric
    object.
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """initializes the edge aShape and the plane aPlane."""

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, aWire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        initializes the vertex aShape, the
        plane aPlane and the wire aWire, which connects
        the two vertices in a fixed relation.
        """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, aPosition: nanoocp.gp.gp_Pnt, anArrowSize: float = 0.01) -> None:
        """
        initializes the edge aShape, the
        plane aPlane, the position aPosition and the arrow
        size anArrowSize.
        """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, aWire: nanoocp.TopoDS.TopoDS_Wire, aPosition: nanoocp.gp.gp_Pnt, anArrowSize: float = 0.01) -> None:
        """
        initializes the vertex aShape, the
        plane aPlane and the wire aWire, the position
        aPosition, the arrow size anArrowSize and the
        wire aWire, which connects the two vertices in a fixed relation.
        """

    @overload
    def __init__(self, theOther: PrsDim_FixRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the wire which connects vertices in a fixed relation."""

    def SetWire(self, aWire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Constructs the wire aWire. This connects vertices
        which are in a fixed relation.
        """

    def IsMovable(self) -> bool:
        """
        Returns true if the Interactive Objects in the relation
        are movable.
        """

class PrsDim_IdenticRelation(PrsDim_Relation):
    """
    Constructs a constraint by a relation of identity
    between two or more datums figuring in shape
    Interactive Objects.
    """

    @overload
    def __init__(self, FirstShape: nanoocp.TopoDS.TopoDS_Shape, SecondShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Initializes the relation of identity between the two
        entities, FirstShape and SecondShape. The plane
        aPlane is initialized in case a visual reference is
        needed to show identity.
        """

    @overload
    def __init__(self, theOther: PrsDim_IdenticRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HasUsers(self) -> bool: ...

    def Users(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_Transient]: ...

    def AddUser(self, theUser: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def ClearUsers(self) -> None: ...

    def IsMovable(self) -> bool:
        """Returns true if the interactive object is movable."""

class PrsDim_LengthDimension(PrsDim_Dimension):
    """
    Length dimension. Can be constructed:
    - Between two generic points.
    - Between two vertices.
    - Between two faces.
    - Between two parallel edges.
    - Between face and edge.

    In case of two points (vertices) or one linear edge the user-defined plane
    that includes this geometry is necessary to be set.

    In case of face-edge, edge-vertex or face-face lengths the automatic plane
    computing is allowed. For this plane the third point is found on the
    edge or on the face.

    Please note that if the inappropriate geometry is defined
    or the distance between measured points is less than
    Precision::Confusion(), the dimension is invalid and its
    presentation can not be computed.
    """

    @overload
    def __init__(self) -> None:
        """
        Construct an empty length dimension.
        @sa SetMeasuredGeometry(), SetMeasuredShapes() for initialization.
        """

    @overload
    def __init__(self, theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Construct length dimension between face and edge.
        Here dimension can be built without user-defined plane.
        @param[in] theFace  the face (first shape).
        @param[in] theEdge  the edge (second shape).
        """

    @overload
    def __init__(self, theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Construct length dimension between two faces.
        @param[in] theFirstFace  the first face (first shape).
        @param[in] theSecondFace  the second face (second shape).
        """

    @overload
    def __init__(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Construct length dimension of linear edge.
        @param[in] theEdge  the edge to measure.
        @param[in] thePlane  the plane to orient dimension.
        """

    @overload
    def __init__(self, theFirstPoint: nanoocp.gp.gp_Pnt, theSecondPoint: nanoocp.gp.gp_Pnt, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Construct length dimension between two points in
        the specified plane.
        @param[in] theFirstPoint  the first point.
        @param[in] theSecondPoint  the second point.
        @param[in] thePlane  the plane to orient dimension.
        """

    @overload
    def __init__(self, theFirstShape: nanoocp.TopoDS.TopoDS_Shape, theSecondShape: nanoocp.TopoDS.TopoDS_Shape, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Construct length dimension between two arbitrary shapes in
        the specified plane.
        @param[in] theFirstShape  the first shape.
        @param[in] theSecondShape  the second shape.
        @param[in] thePlane  the plane to orient dimension.
        """

    @overload
    def __init__(self, theOther: PrsDim_LengthDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def FirstPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return first attachment point."""

    def SecondPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return second attachment point."""

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return first attachment shape."""

    def SecondShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return second attachment shape."""

    @overload
    def SetMeasuredGeometry(self, theFirstPoint: nanoocp.gp.gp_Pnt, theSecondPoint: nanoocp.gp.gp_Pnt, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Measure distance between two points.
        The dimension will become invalid if the new distance between
        attachment points is less than Precision::Confusion().
        @param[in] theFirstPoint  the first point.
        @param[in] theSecondPoint  the second point.
        @param[in] thePlane  the user-defined plane
        """

    @overload
    def SetMeasuredGeometry(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Measure length of edge.
        The dimension will become invalid if the new length of edge
        is less than Precision::Confusion().
        @param[in] theEdge  the edge to measure.
        @param[in] thePlane  the user-defined plane
        """

    @overload
    def SetMeasuredGeometry(self, theFirstFace: nanoocp.TopoDS.TopoDS_Face, theSecondFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Measure distance between two faces.
        The dimension will become invalid if the distance can not
        be measured or it is less than Precision::Confusion().
        @param[in] theFirstFace  the first face (first shape).
        @param[in] theSecondFace  the second face (second shape).
        """

    @overload
    def SetMeasuredGeometry(self, theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Measure distance between face and edge.
        The dimension will become invalid if the distance can not
        be measured or it is less than Precision::Confusion().
        @param[in] theFace  the face (first shape).
        @param[in] theEdge  the edge (second shape).
        """

    def SetMeasuredShapes(self, theFirstShape: nanoocp.TopoDS.TopoDS_Shape, theSecondShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Measure distance between generic pair of shapes (edges, vertices, length),
        where measuring is applicable.
        @param[in] theFirstShape  the first shape.
        @param[in] theSecondShape  the second shape.
        """

    def GetDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the display units string."""

    def GetModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the model units string."""

    def SetDisplayUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetModelUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetTextPosition(self, theTextPos: nanoocp.gp.gp_Pnt) -> None: ...

    def GetTextPosition(self) -> nanoocp.gp.gp_Pnt: ...

    def SetDirection(self, theDirection: nanoocp.gp.gp_Dir, theUseDirection: bool = True) -> None:
        """
        Set custom direction for dimension. If it is not set, the direction is obtained
        from the measured geometry (e.g. line between points of dimension)
        The direction does not change flyout direction of dimension.
        @param[in] theDirection  the dimension direction.
        @param[in] theUseDirection  boolean value if custom direction should be used.
        """

class PrsDim_MaxRadiusDimension(PrsDim_EllipseRadiusDimension):
    """
    Ellipse Max radius dimension of a Shape which can be Edge
    or Face (planar or cylindrical(surface of extrusion or
    surface of offset))
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Max Ellipse radius dimension
        Shape can be edge, planar face or cylindrical face
        """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aPosition: nanoocp.gp.gp_Pnt, aSymbolPrs: nanoocp.DsgPrs.DsgPrs_ArrowSide, anArrowSize: float = 0.0) -> None:
        """
        Max Ellipse radius dimension with position
        Shape can be edge, planar face or cylindrical face
        """

    @overload
    def __init__(self, theOther: PrsDim_MaxRadiusDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PrsDim_MidPointRelation(PrsDim_Relation):
    """presentation of equal distance to point myMidPoint"""

    @overload
    def __init__(self, aSymmTool: nanoocp.TopoDS.TopoDS_Shape, FirstShape: nanoocp.TopoDS.TopoDS_Shape, SecondShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None: ...

    @overload
    def __init__(self, theOther: PrsDim_MidPointRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsMovable(self) -> bool: ...

    def SetTool(self, aMidPointTool: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GetTool(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class PrsDim_MinRadiusDimension(PrsDim_EllipseRadiusDimension):
    """
    Ellipse Min radius dimension of a Shape which
    can be Edge or Face (planar or cylindrical(surface of
    extrusion or surface of offset))
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Max Ellipse radius dimension
        Shape can be edge, planar face or cylindrical face
        """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString, aPosition: nanoocp.gp.gp_Pnt, aSymbolPrs: nanoocp.DsgPrs.DsgPrs_ArrowSide, anArrowSize: float = 0.0) -> None:
        """
        Max Ellipse radius dimension with position
        Shape can be edge, planar face or cylindrical face
        """

    @overload
    def __init__(self, theOther: PrsDim_MinRadiusDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PrsDim_OffsetDimension(PrsDim_Relation):
    """
    A framework to display dimensions of offsets.
    The relation between the offset and the basis shape
    is indicated. This relation is displayed with arrows and
    text. The text gives the dsitance between the offset
    and the basis shape.
    """

    @overload
    def __init__(self, FistShape: nanoocp.TopoDS.TopoDS_Shape, SecondShape: nanoocp.TopoDS.TopoDS_Shape, aVal: float, aText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Constructs the offset display object defined by the
        first shape aFShape, the second shape aSShape, the
        dimension aVal, and the text aText.
        """

    @overload
    def __init__(self, theOther: PrsDim_OffsetDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def KindOfDimension(self) -> PrsDim_KindOfDimension:
        """Indicates that the dimension we are concerned with is an offset."""

    def IsMovable(self) -> bool:
        """Returns true if the offset datum is movable."""

    def SetRelativePos(self, aTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Sets a transformation aTrsf for presentation and
        selection to a relative position.
        """

class PrsDim_ParallelRelation(PrsDim_Relation):
    """
    A framework to display constraints of parallelism
    between two or more Interactive Objects. These
    entities can be faces or edges.
    """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aSShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Constructs an object to display parallel constraints.
        This object is defined by the first shape aFShape and
        the second shape aSShape and the plane aPlane.
        """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aSShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, aPosition: nanoocp.gp.gp_Pnt, aSymbolPrs: nanoocp.DsgPrs.DsgPrs_ArrowSide, anArrowSize: float = 0.01) -> None:
        """
        Constructs an object to display parallel constraints.
        This object is defined by the first shape aFShape and
        the second shape aSShape the plane aPlane, the
        position aPosition, the type of arrow, aSymbolPrs and
        its size anArrowSize.
        """

    @overload
    def __init__(self, theOther: PrsDim_ParallelRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsMovable(self) -> bool:
        """Returns true if the parallelism is movable."""

class PrsDim_PerpendicularRelation(PrsDim_Relation):
    """
    A framework to display constraints of perpendicularity
    between two or more interactive datums. These
    datums can be edges or faces.
    """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aSShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Constructs an object to display constraints of
        perpendicularity on shapes.
        This object is defined by a first shape aFShape and a
        second shape aSShape.
        """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aSShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Constructs an object to display constraints of
        perpendicularity on shapes.
        This object is defined by a first shape aFShape, a
        second shape aSShape, and a plane aPlane.
        aPlane is the plane of reference to show and test the
        perpendicular relation between two shapes, at least
        one of which has a revolved surface.
        """

    @overload
    def __init__(self, theOther: PrsDim_PerpendicularRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PrsDim_RadiusDimension(PrsDim_Dimension):
    """
    Radius dimension. Can be constructed:
    - On generic circle.
    - On generic circle with user-defined anchor point on that circle.
    - On generic shape containing geometry that can be measured
    by diameter dimension: circle wire, arc, circular face, etc.
    The anchor point is the location of left attachment point of
    dimension on the circle. It can be user-specified, or computed as
    middle point on the arc. The radius dimension always lies in the
    plane of the measured circle. The dimension is considered as
    invalid if the user-specified anchor point is not lying on the circle,
    if the radius of the circle is less than Precision::Confusion().
    In case if the dimension is built on the arbitrary shape,
    it can be considered as invalid if the shape does not contain
    circle geometry.
    """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ) -> None:
        """
        Create radius dimension for the circle geometry.
        @param[in] theCircle  the circle to measure.
        """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Create radius dimension for the arbitrary shape (if possible).
        @param[in] theShape  the shape to measure.
        """

    @overload
    def __init__(self, theCircle: nanoocp.gp.gp_Circ, theAnchorPoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Create radius dimension for the circle geometry and define its
        orientation by location of the first point on that circle.
        @param[in] theCircle  the circle to measure.
        @param[in] theAnchorPoint  the point to define the position
        of the dimension attachment on the circle.
        """

    @overload
    def __init__(self, theOther: PrsDim_RadiusDimension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Circle(self) -> nanoocp.gp.gp_Circ:
        """@return measured geometry circle."""

    def AnchorPoint(self) -> nanoocp.gp.gp_Pnt:
        """@return anchor point on circle for radius dimension."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """@return the measured shape."""

    @overload
    def SetMeasuredGeometry(self, theCircle: nanoocp.gp.gp_Circ) -> None:
        """
        Measure radius of the circle.
        The dimension will become invalid if the radius of the circle
        is less than Precision::Confusion().
        @param[in] theCircle  the circle to measure.
        """

    @overload
    def SetMeasuredGeometry(self, theCircle: nanoocp.gp.gp_Circ, theAnchorPoint: nanoocp.gp.gp_Pnt, theHasAnchor: bool = True) -> None:
        """
        Measure radius of the circle and orient the dimension so
        the dimension lines attaches to anchor point on the circle.
        The dimension will become invalid if the radius of the circle
        is less than Precision::Confusion().
        @param[in] theCircle  the circle to measure.
        @param[in] theAnchorPoint  the point to attach the dimension lines, should be on the circle
        @param[in] theHasAnchor    should be set TRUE if theAnchorPoint should be used
        """

    @overload
    def SetMeasuredGeometry(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Measure radius on the passed shape, if applicable.
        The dimension will become invalid if the passed shape is not
        measurable or if measured diameter value is less than Precision::Confusion().
        @param[in] theShape  the shape to measure.
        """

    @overload
    def SetMeasuredGeometry(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theAnchorPoint: nanoocp.gp.gp_Pnt, theHasAnchor: bool = True) -> None:
        """
        Measure radius on the passed shape, if applicable.
        The dimension will become invalid if the passed shape is not
        measurable or if measured diameter value is less than Precision::Confusion().
        @param[in] theShape  the shape to measure.
        @param[in] theAnchorPoint  the point to attach the dimension lines, should be on the circle
        @param[in] theHasAnchor    should be set TRUE if theAnchorPoint should be used
        """

    def GetDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the display units string."""

    def GetModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return the model units string."""

    def SetDisplayUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetModelUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetTextPosition(self, theTextPos: nanoocp.gp.gp_Pnt) -> None: ...

    def GetTextPosition(self) -> nanoocp.gp.gp_Pnt: ...

class PrsDim_SymmetricRelation(PrsDim_Relation):
    """
    A framework to display constraints of symmetricity
    between two or more datum Interactive Objects.
    A plane serves as the axis of symmetry between the
    shapes of which the datums are parts.
    """

    @overload
    def __init__(self, aSymmTool: nanoocp.TopoDS.TopoDS_Shape, FirstShape: nanoocp.TopoDS.TopoDS_Shape, SecondShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Constructs an object to display constraints of symmetricity.
        This object is defined by a tool aSymmTool, a first
        shape FirstShape, a second shape SecondShape, and a plane aPlane.
        aPlane serves as the axis of symmetry.
        aSymmTool is the shape composed of FirstShape
        SecondShape and aPlane. It may be queried and
        edited using the functions GetTool and SetTool.
        The two shapes are typically two edges, two vertices or two points.
        """

    @overload
    def __init__(self, theOther: PrsDim_SymmetricRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsMovable(self) -> bool:
        """Returns true if the symmetric constraint display is movable."""

    def SetTool(self, aSymmetricTool: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets the tool aSymmetricTool composed of a first
        shape, a second shape, and a plane.
        This tool is initially created at construction time.
        """

    def GetTool(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the tool composed of a first shape, a second
        shape, and a plane. This tool is created at construction time.
        """

class PrsDim_TangentRelation(PrsDim_Relation):
    """
    A framework to display tangency constraints between
    two or more Interactive Objects of the datum type.
    The datums are normally faces or edges.
    """

    @overload
    def __init__(self, aFShape: nanoocp.TopoDS.TopoDS_Shape, aSShape: nanoocp.TopoDS.TopoDS_Shape, aPlane: nanoocp.Geom.Geom_Plane | None, anExternRef: int = 0) -> None:
        """
        TwoFacesTangent or TwoEdgesTangent relation
        Constructs an object to display tangency constraints.
        This object is defined by the first shape aFShape, the
        second shape aSShape, the plane aPlane and the index anExternRef.
        aPlane serves as an optional axis.
        anExternRef set to 0 indicates that there is no relation.
        """

    @overload
    def __init__(self, theOther: PrsDim_TangentRelation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ExternRef(self) -> int:
        """
        Returns the external reference for tangency.
        The values are as follows:
        -   0 - there is no connection;
        -   1 - there is a connection to the first shape;
        -   2 - there is a connection to the second shape.
        This reference is defined at construction time.
        """

    def SetExternRef(self, aRef: int) -> None:
        """
        Sets the external reference for tangency, aRef.
        The values are as follows:
        -   0 - there is no connection;
        -   1 - there is a connection to the first shape;
        -   2 - there is a connection to the second shape.
        This reference is initially defined at construction time.
        """
