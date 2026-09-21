"""OCCT package IntCurvesFace (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Bnd
import nanoocp.GeomAbs
import nanoocp.IntCurveSurface
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class IntCurvesFace_Intersector(nanoocp.Standard.Standard_Transient):
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, aTol: float, aRestr: bool = True, UseBToler: bool = True) -> None:
        """
        Load a Face.

        The Tolerance <Tol> is used to determine if the
        first point of the segment is near the face. In
        that case, the parameter of the intersection point
        on the line can be a negative value (greater than -Tol).
        If aRestr = true UV bounding box of face is used to restrict
        it's underlined surface,
        otherwise surface is not restricted.
        If UseBToler = false then the 2d-point of intersection is classified with null-tolerance
        (relative to face);
        otherwise it's using maximum between input tolerance(aTol) and tolerances of face bounds
        (edges).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin, PInf: float, PSup: float) -> None:
        """
        Perform the intersection between the
        segment L and the loaded face.

        PInf is the smallest parameter on the line
        PSup is the highest parameter on the line

        For an infinite line PInf and PSup can be
        +/- RealLast.
        """

    @overload
    def Perform(self, HCu: nanoocp.Adaptor3d.Adaptor3d_Curve | None, PInf: float, PSup: float) -> None:
        """
        same method for a HCurve from Adaptor3d.
        PInf an PSup can also be - and + INF.
        """

    def SurfaceType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """Return the surface type"""

    def IsDone(self) -> bool:
        """True is returned when the intersection have been computed."""

    def NbPnt(self) -> int: ...

    def UParameter(self, I: int) -> float:
        """
        Returns the U parameter of the ith intersection point
        on the surface.
        """

    def VParameter(self, I: int) -> float:
        """
        Returns the V parameter of the ith intersection point
        on the surface.
        """

    def WParameter(self, I: int) -> float:
        """
        Returns the parameter of the ith intersection point
        on the line.
        """

    def Pnt(self, I: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the geometric point of the ith intersection
        between the line and the surface.
        """

    def Transition(self, I: int) -> nanoocp.IntCurveSurface.IntCurveSurface_TransitionOnCurve:
        """Returns the ith transition of the line on the surface."""

    def State(self, I: int) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the ith state of the point on the face.
        The values can be either TopAbs_IN
        ( the point is in the face)
        or TopAbs_ON
        ( the point is on a boundary of the face).
        """

    def IsParallel(self) -> bool:
        """
        Returns true if curve is parallel or belongs face surface
        This case is recognized only for some pairs
        of analytical curves and surfaces (plane - line, ...)
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the significant face used to determine
        the intersection.
        """

    def ClassifyUVPoint(self, Puv: nanoocp.gp.gp_Pnt2d) -> nanoocp.TopAbs.TopAbs_State: ...

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box: ...

    def SetUseBoundToler(self, UseBToler: bool) -> None:
        """Sets the boundary tolerance flag"""

    def GetUseBoundToler(self) -> bool:
        """Returns the boundary tolerance flag"""

class IntCurvesFace_ShapeIntersector:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntCurvesFace_ShapeIntersector) -> None: ...

    def Load(self, Sh: nanoocp.TopoDS.TopoDS_Shape, Tol: float) -> None: ...

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin, PInf: float, PSup: float) -> None:
        """
        Perform the intersection between the
        segment L and the loaded shape.

        PInf is the smallest parameter on the line
        PSup is the highest parameter on the line

        For an infinite line PInf and PSup can be
        +/- RealLast.
        """

    @overload
    def Perform(self, HCu: nanoocp.Adaptor3d.Adaptor3d_Curve | None, PInf: float, PSup: float) -> None:
        """
        same method for a HCurve from Adaptor3d.
        PInf an PSup can also be -INF and +INF.
        """

    def PerformNearest(self, L: nanoocp.gp.gp_Lin, PInf: float, PSup: float) -> None:
        """
        Perform the intersection between the
        segment L and the loaded shape.

        PInf is the smallest parameter on the line
        PSup is the highest parameter on the line

        For an infinite line PInf and PSup can be
        +/- RealLast.
        """

    def IsDone(self) -> bool:
        """True when the intersection has been computed."""

    def NbPnt(self) -> int:
        """Returns the number of the intersection points"""

    def UParameter(self, I: int) -> float:
        """
        Returns the U parameter of the ith intersection point
        on the surface.
        """

    def VParameter(self, I: int) -> float:
        """
        Returns the V parameter of the ith intersection point
        on the surface.
        """

    def WParameter(self, I: int) -> float:
        """
        Returns the parameter of the ith intersection point
        on the line.
        """

    def Pnt(self, I: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the geometric point of the ith intersection
        between the line and the surface.
        """

    def Transition(self, I: int) -> nanoocp.IntCurveSurface.IntCurveSurface_TransitionOnCurve:
        """Returns the ith transition of the line on the surface."""

    def State(self, I: int) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the ith state of the point on the face.
        The values can be either TopAbs_IN
        ( the point is in the face)
        or TopAbs_ON
        ( the point is on a boundary of the face).
        """

    def Face(self, I: int) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the significant face used to determine
        the intersection.
        """

    def SortResult(self) -> None:
        """
        Internal method. Sort the result on the Curve
        parameter.
        """
