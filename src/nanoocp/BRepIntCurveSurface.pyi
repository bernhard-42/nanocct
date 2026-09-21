"""OCCT package BRepIntCurveSurface (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.GeomAdaptor
import nanoocp.IntCurveSurface
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class BRepIntCurveSurface_Inter:
    """
    Computes the intersection between a face and a
    curve. To intersect one curve with shape method
    Init(Shape, curve, tTol) should be used. To
    intersect a few curves with specified shape it is
    necessary to load shape one time using method
    Load(shape, tol) and find intersection points for
    each curve using method Init(curve). For
    iteration by intersection points method More() and
    Next() should be used.

    Example:
    Inter.Load(shape, tol);
    for( i =1; i <= nbCurves;i++)
    {
    Inter.Init(curve);
    for( ;Inter.More(); Inter.Next())
    {
    .......
    }
    }
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor;"""

    @overload
    def __init__(self, theOther: BRepIntCurveSurface_Inter) -> None: ...

    @overload
    def Init(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theCurve: nanoocp.GeomAdaptor.GeomAdaptor_Curve, theTol: float) -> None: ...

    @overload
    def Init(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLine: nanoocp.gp.gp_Lin, theTol: float) -> None:
        """
        Load the Shape, the curve and initialize the
        tolerance used for the classification.
        """

    @overload
    def Init(self, theCurve: nanoocp.GeomAdaptor.GeomAdaptor_Curve) -> None:
        """Method to find intersections of specified curve with loaded shape."""

    def Load(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theTol: float) -> None:
        """
        Load the Shape, and initialize the
        tolerance used for the classification.
        """

    def More(self) -> bool:
        """returns True if there is a current face."""

    def Next(self) -> None:
        """Sets the next intersection point to check."""

    def Point(self) -> nanoocp.IntCurveSurface.IntCurveSurface_IntersectionPoint:
        """returns the current Intersection point."""

    def Pnt(self) -> nanoocp.gp.gp_Pnt:
        """returns the current geometric Point"""

    def U(self) -> float:
        """
        returns the U parameter of the current point
        on the current face.
        """

    def V(self) -> float:
        """
        returns the V parameter of the current point
        on the current face.
        """

    def W(self) -> float:
        """
        returns the parameter of the current point
        on the curve.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """returns the current state (IN or ON)"""

    def Transition(self) -> nanoocp.IntCurveSurface.IntCurveSurface_TransitionOnCurve:
        """
        returns the transition of the line on the surface (IN or OUT or UNKNOWN)
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """returns the current face."""
