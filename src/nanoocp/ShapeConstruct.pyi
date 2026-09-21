"""OCCT package ShapeConstruct (toolkit TKShHealing)"""

from typing import overload

import nanoocp.BRepBuilderAPI
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeAnalysis
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class ShapeConstruct:
    """
    This package provides new algorithms for constructing
    new geometrical objects and topological shapes. It
    complements and extends algorithms available in Open
    CASCADE topological and geometrical toolkist.
    The functionality provided by this package are the
    following:
    projecting curves on surface,
    adjusting curve to have given start and end points. P
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeConstruct) -> None: ...

    @overload
    @staticmethod
    def ConvertCurveToBSpline(C3D: nanoocp.Geom.Geom_Curve | None, First: float, Last: float, Tol3d: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> nanoocp.Geom.Geom_BSplineCurve:
        """Tool for wire triangulation"""

    @overload
    @staticmethod
    def ConvertCurveToBSpline(C2D: nanoocp.Geom2d.Geom2d_Curve | None, First: float, Last: float, Tol2d: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @staticmethod
    def ConvertSurfaceToBSpline(surf: nanoocp.Geom.Geom_Surface | None, UF: float, UL: float, VF: float, VL: float, Tol3d: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> nanoocp.Geom.Geom_BSplineSurface: ...

    @staticmethod
    def JoinPCurves(theEdges: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        join pcurves of the <theEdge> on the <theFace>
        try to use pcurves from originas edges <theEdges>
        Returns false if cannot join pcurves
        """

    @overload
    @staticmethod
    def JoinCurves(c3d1: nanoocp.Geom.Geom_Curve | None, ac3d2: nanoocp.Geom.Geom_Curve | None, Orient1: nanoocp.TopAbs.TopAbs_Orientation, Orient2: nanoocp.TopAbs.TopAbs_Orientation) -> tuple[bool, float, float, float, float, nanoocp.Geom.Geom_Curve, bool, bool]:
        """
        Method for joininig curves 3D.
        Parameters : c3d1,ac3d2 - initial curves
        Orient1, Orient2 - initial edges orientations.
        first1,last1,first2,last2 - parameters for trimming curves
        (re-calculate with account of orientation edges)
        c3dOut - result curve
        isRev1,isRev2 - out parameters indicative on possible errors.
        Return value : True - if curves were joined successfully,
        else - False.
        """

    @overload
    @staticmethod
    def JoinCurves(c2d1: nanoocp.Geom2d.Geom2d_Curve | None, ac2d2: nanoocp.Geom2d.Geom2d_Curve | None, Orient1: nanoocp.TopAbs.TopAbs_Orientation, Orient2: nanoocp.TopAbs.TopAbs_Orientation, isError: bool = False) -> tuple[bool, float, float, float, float, nanoocp.Geom2d.Geom2d_Curve, bool, bool]:
        """
        Method for joininig curves 3D.
        Parameters : c3d1,ac3d2 - initial curves
        Orient1, Orient2 - initial edges orientations.
        first1,last1,first2,last2 - parameters for trimming curves
        (re-calculate with account of orientation edges)
        c3dOut - result curve
        isRev1,isRev2 - out parameters indicative on possible errors.
        isError - input parameter indicative possible errors due to that one from edges have one
        vertex Return value : True - if curves were joined successfully, else - False.
        """

class ShapeConstruct_Curve:
    """
    Adjusts curve to have start and end points at the given
    points (currently works on lines and B-Splines only)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeConstruct_Curve) -> None: ...

    def AdjustCurve(self, C3D: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, take1: bool = True, take2: bool = True) -> bool:
        """
        Modifies a curve in order to make its bounds confused with
        given points.
        Works only on lines and B-Splines, returns True in this case,
        else returns False.
        For line considers both bounding points, for B-Splines only
        specified.

        Warning : Does not check if curve should be reversed
        """

    def AdjustCurveSegment(self, C3D: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, U1: float, U2: float) -> bool:
        """
        Modifies a curve in order to make its bounds confused with
        given points.
        Works only on lines and B-Splines.

        For lines works as previous method, B-Splines are segmented
        at the given values and then are adjusted to the points.
        """

    def AdjustCurve2d(self, C2D: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, take1: bool = True, take2: bool = True) -> bool:
        """
        Modifies a curve in order to make its bounds confused with
        given points.
        Works only on lines and B-Splines, returns True in this case,
        else returns False.

        For line considers both bounding points, for B-Splines only
        specified.

        Warning : Does not check if curve should be reversed
        """

    @overload
    def ConvertToBSpline(self, C: nanoocp.Geom.Geom_Curve | None, first: float, last: float, prec: float) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        Converts a curve of any type (only part from first to last)
        to bspline. The method of conversion depends on the type
        of original curve:
        BSpline -> C.Segment(first,last)
        Bezier and Line -> GeomConvert::CurveToBSplineCurve(C).Segment(first,last)
        Conic and Other -> Approx_Curve3d(C[first,last],prec,C1,9,1000)
        """

    @overload
    def ConvertToBSpline(self, C: nanoocp.Geom2d.Geom2d_Curve | None, first: float, last: float, prec: float) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        Converts a curve of any type (only part from first to last)
        to bspline. The method of conversion depends on the type
        of original curve:
        BSpline -> C.Segment(first,last)
        Bezier and Line -> GeomConvert::CurveToBSplineCurve(C).Segment(first,last)
        Conic and Other -> Approx_Curve2d(C[first,last],prec,C1,9,1000)
        """

    @overload
    @staticmethod
    def FixKnots() -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[float]]: ...

    @overload
    @staticmethod
    def FixKnots(knots: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Fix bspline knots to ensure that there is enough
        gap between neighbouring values
        Returns True if something fixed (by shifting knot)
        """

class ShapeConstruct_MakeTriangulation(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self, pnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], prec: float = 0.0) -> None: ...

    @overload
    def __init__(self, wire: nanoocp.TopoDS.TopoDS_Wire, prec: float = 0.0) -> None: ...

    @overload
    def __init__(self, theOther: ShapeConstruct_MakeTriangulation) -> None: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def IsDone(self) -> bool: ...

class ShapeConstruct_ProjectCurveOnSurface(nanoocp.Standard.Standard_Transient):
    """
    This tool provides a method for computing pcurve by projecting
    3d curve onto a surface.
    Projection is done by 23 or more points (this number is changed
    for B-Splines according to the following rule:
    the total number of the points is not less than number of spans *
    (degree + 1);
    it is increased recursively starting with 23 and is added with 22
    until the condition is fulfilled).
    Isoparametric cases (if curve corresponds to U=const or V=const on
    the surface) are recognized with the given precision.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeConstruct_ProjectCurveOnSurface) -> None: ...

    @overload
    def Init(self, theSurf: nanoocp.Geom.Geom_Surface | None, thePreci: float) -> None:
        """
        Initializes the object with all necessary parameters,
        i.e. surface and precision
        @param[in] theSurf the surface to project on
        @param[in] thePreci the precision for projection
        """

    @overload
    def Init(self, theSurf: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None, thePreci: float) -> None:
        """
        Initializes the object with all necessary parameters,
        i.e. surface and precision
        @param[in] theSurf the surface to project on (ShapeAnalysis_Surface)
        @param[in] thePreci the precision for projection
        """

    @overload
    def SetSurface(self, theSurf: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Loads a surface (in the form of Geom_Surface) to project on
        @param[in] theSurf the surface to project on
        """

    @overload
    def SetSurface(self, theSurf: nanoocp.ShapeAnalysis.ShapeAnalysis_Surface | None) -> None:
        """
        Loads a surface (in the form of ShapeAnalysis_Surface) to project on
        @param[in] theSurf the surface to project on
        """

    def SetPrecision(self, thePreci: float) -> None:
        """
        Sets value for current precision
        @param[in] thePreci the precision value
        """

    def AdjustOverDegenMode(self) -> int:
        """
        Returns (modifiable) the flag specifying to which side of
        parametrical space adjust part of pcurve which lies on seam.
        This is required in very rare case when 3d curve which is
        to be projected goes partly along the seam on the closed
        surface with singularity (e.g. sphere), goes through the
        degenerated point and partly lies on internal area of surface.

        If this flag is True, the seam part of such curve will be
        adjusted to the left side of parametric space (on sphere U=0),
        else to the right side (on sphere U=2*PI)
        Default value is True
        @return modifiable reference to the adjustment flag
        """

    def SetAdjustOverDegenMode(self, theValue: int) -> None:
        """
        Python addition: sets the value AdjustOverDegenMode() returns by reference in C++.
        """

    def Status(self, theStatus: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Returns the status of last Perform
        @param[in] theStatus the status to query
        @return true if the specified status is set
        """

    def Perform(self, theC3D: nanoocp.Geom.Geom_Curve | None, theFirst: float, theLast: float, theTolFirst: float = 1e-07, theTolLast: float = 1e-07) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve]:
        """
        Computes the projection of 3d curve onto a surface using the
        specialized algorithm. Returns False if projector fails,
        otherwise, if pcurve computed successfully, returns True.
        The output curve 2D is guaranteed to be same-parameter
        with input curve 3D on the interval [theFirst, theLast]. If the output curve
        lies on a direct line the infinite line is returned, in the case
        same-parameter condition is satisfied.
        @param[in] theC3D the 3D curve to project
        @param[in] theFirst the first parameter of the curve
        @param[in] theLast the last parameter of the curve
        @param[out] theC2D the resulting 2D curve
        @param[in] theTolFirst the tolerance at the first point (default: Precision::Confusion())
        @param[in] theTolLast the tolerance at the last point (default: Precision::Confusion())
        @return true if projection succeeded
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
