"""OCCT package ShapeCustom (toolkit TKShHealing)"""

from typing import overload

import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeBuild
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class ShapeCustom:
    """
    This package is intended to
    convert geometrical objects and topological. The
    modifications of one geometrical object to another
    (one) geometrical object are provided. The supported
    modifications are the following:
    conversion of BSpline and Bezier surfaces to analytical form,
    conversion of indirect elementary surfaces (with left-handed
    coordinate systems) into direct ones,
    conversion of elementary surfaces to surfaces of revolution,
    conversion of surface of linear extrusion, revolution, offset
    surface to bspline,
    modification of parameterization, degree, number of segments of bspline
    surfaces, scale the shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom) -> None: ...

    @staticmethod
    def ApplyModifier(S: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.BRepTools.BRepTools_Modification | None, context: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], MD: nanoocp.BRepTools.BRepTools_Modifier, theProgress: nanoocp.Message.Message_ProgressRange = ..., aReShape: nanoocp.ShapeBuild.ShapeBuild_ReShape | None = None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Applies modifier to shape and checks sharing in the case assemblies."""

    @staticmethod
    def DirectFaces(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns a new shape without indirect surfaces."""

    @staticmethod
    def ScaleShape(S: nanoocp.TopoDS.TopoDS_Shape, scale: float) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns a new shape which is scaled original"""

    @staticmethod
    def BSplineRestriction(S: nanoocp.TopoDS.TopoDS_Shape, Tol3d: float, Tol2d: float, MaxDegree: int, MaxNbSegment: int, Continuity3d: nanoocp.GeomAbs.GeomAbs_Shape, Continuity2d: nanoocp.GeomAbs.GeomAbs_Shape, Degree: bool, Rational: bool, aParameters: ShapeCustom_RestrictionParameters | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a new shape with all surfaces, curves and pcurves
        which type is BSpline/Bezier or based on them converted
        having Degree less than <MaxDegree> or number of spans less
        than <NbMaxSegment> in dependence on parameter priority <Degree>.
        <GmaxDegree> and <GMaxSegments> are maximum possible degree
        and number of spans correspondingly.
        These values will be used in those cases when approximation with
        specified parameters is impossible and one of GmaxDegree or
        GMaxSegments is selected in dependence on priority.
        Note that even if approximation is impossible with <GMaxDegree>
        then number of spans can exceed specified <GMaxSegment>
        <Rational> specifies if to convert Rational BSpline/Bezier into
        polynomial B-Spline.
        If flags ConvOffSurf,ConvOffCurve3d,ConvOffCurve2d are true there are means
        that Offset surfaces , Offset curves 3d and Offset curves 2d are converted to BSPline
        correspondingly.
        """

    @staticmethod
    def ConvertToRevolution(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a new shape with all elementary periodic surfaces converted
        to Geom_SurfaceOfRevolution
        """

    @staticmethod
    def SweptToElementary(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a new shape with all surfaces of revolution and linear extrusion
        convert to elementary periodic surfaces
        """

    @staticmethod
    def ConvertToBSpline(S: nanoocp.TopoDS.TopoDS_Shape, extrMode: bool, revolMode: bool, offsetMode: bool, planeMode: bool = False) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a new shape with all surfaces of linear extrusion, revolution,
        offset, and planar surfaces converted according to flags to
        Geom_BSplineSurface (with same parameterisation).
        """

class ShapeCustom_Modification(nanoocp.BRepTools.BRepTools_Modification):
    """
    A base class of Modification's from ShapeCustom.
    Implements message sending mechanism.
    """

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def MsgRegistrator(self) -> nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator:
        """Returns message registrator"""

    def SendMsg(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity = Message_Gravity.Message_Info) -> None:
        """
        Sends a message to be attached to the shape.
        Calls corresponding message of message registrator.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_BSplineRestriction(ShapeCustom_Modification):
    """
    this tool intended for approximation surfaces, curves and pcurves with
    specified degree , max number of segments, tolerance 2d, tolerance 3d. Specified
    continuity can be reduced if approximation with specified continuity was not done.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, anApproxSurfaceFlag: bool, anApproxCurve3dFlag: bool, anApproxCurve2dFlag: bool, aTol3d: float, aTol2d: float, aContinuity3d: nanoocp.GeomAbs.GeomAbs_Shape, aContinuity2d: nanoocp.GeomAbs.GeomAbs_Shape, aMaxDegree: int, aNbMaxSeg: int, Degree: bool, Rational: bool) -> None: ...

    @overload
    def __init__(self, anApproxSurfaceFlag: bool, anApproxCurve3dFlag: bool, anApproxCurve2dFlag: bool, aTol3d: float, aTol2d: float, aContinuity3d: nanoocp.GeomAbs.GeomAbs_Shape, aContinuity2d: nanoocp.GeomAbs.GeomAbs_Shape, aMaxDegree: int, aNbMaxSeg: int, Degree: bool, Rational: bool, aModes: ShapeCustom_RestrictionParameters | None) -> None:
        """Initializes with specified parameters of approximation."""

    @overload
    def __init__(self, theOther: ShapeCustom_BSplineRestriction) -> None: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location,
        <Tol> the new tolerance. <RevWires> has to be set to
        true when the modification reverses the
        normal of the surface. (the wires have to be
        reversed). <RevFace> has to be set to
        true if the orientation of the modified
        face changes in the shells which contain it.

        Otherwise, returns false, and <S>, <L>,
        <Tol>, <RevWires>, <RevFace> are not significant.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if curve from the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location, <Tol>
        the new tolerance.
        Otherwise, returns true if Surface is modified or
        one of pcurves of edge is modified. In this case C is copy of
        geometric support of the edge.
        In other cases returns false, and <C>, <L>, <Tol> are not
        significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has been modified.
        In this case,if curve on the surface is modified, <C>
        is the new geometric support of the edge, <L> the
        new location, <Tol> the new tolerance. If curve on the surface
        is not modified C is copy curve on surface from the edge <E>.

        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.

        <NewE> is the new edge created from <E>. <NewF>
        is the new face created from <F>. They may be useful.
        """

    def ConvertSurface(self, aSurface: nanoocp.Geom.Geom_Surface | None, UF: float, UL: float, VF: float, VL: float, IsOf: bool = True) -> tuple[bool, nanoocp.Geom.Geom_Surface]:
        """
        Returns true if the surface has been modified.
        if flag IsOf equals true Offset surfaces are approximated to Offset
        if false to BSpline
        """

    def ConvertCurve(self, aCurve: nanoocp.Geom.Geom_Curve | None, IsConvert: bool, First: float, Last: float, IsOf: bool = True) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the curve has been modified.
        if flag IsOf equals true Offset curves are approximated to Offset
        if false to BSpline
        """

    def ConvertCurve2d(self, aCurve: nanoocp.Geom2d.Geom2d_Curve | None, IsConvert: bool, First: float, Last: float, IsOf: bool = True) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the pcurve has been modified.
        if flag IsOf equals true Offset pcurves are approximated to Offset
        if false to BSpline
        """

    def SetTol3d(self, Tol3d: float) -> None:
        """Sets tolerance of approximation for curve3d and surface"""

    def SetTol2d(self, Tol2d: float) -> None:
        """Sets tolerance of approximation for curve2d"""

    def ModifyApproxSurfaceFlag(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether the
        surface is approximated.
        """

    def SetModifyApproxSurfaceFlag(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyApproxSurfaceFlag() returns by reference in C++.
        """

    def ModifyApproxCurve3dFlag(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether the
        curve3d is approximated.
        """

    def SetModifyApproxCurve3dFlag(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyApproxCurve3dFlag() returns by reference in C++.
        """

    def ModifyApproxCurve2dFlag(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether the curve2d is approximated.
        """

    def SetModifyApproxCurve2dFlag(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyApproxCurve2dFlag() returns by reference in C++.
        """

    def SetContinuity3d(self, Continuity3d: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets continuity3d for approximation curve3d and surface."""

    def SetContinuity2d(self, Continuity2d: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets continuity3d for approximation curve2d."""

    def SetMaxDegree(self, MaxDegree: int) -> None:
        """Sets max degree for approximation."""

    def SetMaxNbSegments(self, MaxNbSegments: int) -> None:
        """Sets max number of segments for approximation."""

    def SetPriority(self, Degree: bool) -> None:
        """
        Sets priority for approximation curves and surface.
        If Degree is True approximation is made with degree less
        then specified MaxDegree at the expense of number of spanes.
        If Degree is False approximation is made with number of
        spans less then specified MaxNbSegment at the expense of
        specified MaxDegree.
        """

    def SetConvRational(self, Rational: bool) -> None:
        """
        Sets flag for define if rational BSpline or Bezier is
        converted to polynomial. If Rational is True approximation
        for rational BSpline and Bezier is made to polynomial even
        if degree is less then MaxDegree and number of spans is less
        then specified MaxNbSegment.
        """

    def GetRestrictionParameters(self) -> ShapeCustom_RestrictionParameters:
        """
        Returns the container of modes which defines
        what geometry should be converted to BSplines.
        """

    def SetRestrictionParameters(self, aModes: ShapeCustom_RestrictionParameters | None) -> None:
        """
        Sets the container of modes which defines
        what geometry should be converted to BSplines.
        """

    def Curve3dError(self) -> float:
        """Returns error for approximation curve3d."""

    def Curve2dError(self) -> float:
        """Returns error for approximation curve2d."""

    def SurfaceError(self) -> float:
        """Returns error for approximation surface."""

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]: ...

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]: ...

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def MaxErrors(self) -> tuple[float, float, float]:
        """Returns error for approximation surface, curve3d and curve2d."""

    def NbOfSpan(self) -> int:
        """Returns number for approximation surface, curve3d and curve2d."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_ConvertToBSpline(ShapeCustom_Modification):
    """
    implement a modification for BRepTools
    Modifier algorithm. Converts Surface of
    Linear Exctrusion, Revolution and Offset
    surfaces into BSpline Surface according to
    flags.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_ConvertToBSpline) -> None: ...

    def SetExtrusionMode(self, extrMode: bool) -> None:
        """
        Sets mode for conversion of Surfaces of Linear
        extrusion.
        """

    def SetRevolutionMode(self, revolMode: bool) -> None:
        """Sets mode for conversion of Surfaces of Revolution."""

    def SetOffsetMode(self, offsetMode: bool) -> None:
        """Sets mode for conversion of Offset surfaces."""

    def SetPlaneMode(self, planeMode: bool) -> None:
        """Sets mode for conversion of Plane surfaces."""

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location,
        <Tol> the new tolerance. Otherwise, returns
        false, and <S>, <L>, <Tol> are not
        significant.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location,
        <Tol> the new tolerance. Otherwise, returns
        false, and <C>, <L>, <Tol> are not
        significant.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex <V> has been
        modified. In this case, <P> is the new geometric
        support of the vertex, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has a new
        curve on surface on the face <F>.In this case, <C>
        is the new geometric support of the edge, <L> the
        new location, <Tol> the new tolerance.

        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.

        <NewE> is the new edge created from <E>. <NewF>
        is the new face created from <F>. They may be useful.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex <V> has a new
        parameter on the edge <E>. In this case, <P> is
        the parameter, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of <NewE> between <NewF1>
        and <NewF2>.

        <NewE> is the new edge created from <E>. <NewF1>
        (resp. <NewF2>) is the new face created from <F1>
        (resp. <F2>).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_ConvertToRevolution(ShapeCustom_Modification):
    """
    implements a modification for the BRepTools
    Modifier algorithm. Converts all elementary
    surfaces into surfaces of revolution.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_ConvertToRevolution) -> None: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <S>, <L>, <Tol> are not
        significant.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <C>, <L>, <Tol> are not
        significant.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex <V> has been
        modified. In this case, <P> is the new geometric
        support of the vertex, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has a new
        curve on surface on the face <F>.In this case, <C>
        is the new geometric support of the edge, <L> the
        new location, <Tol> the new tolerance.

        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.

        <NewE> is the new edge created from <E>. <NewF>
        is the new face created from <F>. They may be useful.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex <V> has a new
        parameter on the edge <E>. In this case, <P> is
        the parameter, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of <NewE> between <NewF1>
        and <NewF2>.

        <NewE> is the new edge created from <E>. <NewF1>
        (resp. <NewF2>) is the new face created from <F1>
        (resp. <F2>).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_Curve:
    """Converts BSpline curve to periodic"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_Curve) -> None: ...

    def Init(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    def ConvertToPeriodic(self, substitute: bool, preci: float = -1.0) -> nanoocp.Geom.Geom_Curve:
        """
        Tries to convert the Curve to the Periodic form
        Returns the resulting curve
        Works only if the Curve is BSpline and is closed with
        Precision::Confusion()
        Else, or in case of failure, returns a Null Handle
        """

class ShapeCustom_Curve2d:
    """
    Converts curve2d to analytical form with given
    precision or simplify curve2d.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_Curve2d) -> None: ...

    @staticmethod
    def IsLinear(thePoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theTolerance: float) -> tuple[bool, float]:
        """
        Check if poleses is in the plane with given precision
        Returns false if no.
        """

    @staticmethod
    def ConvertToLine2d(theCurve: nanoocp.Geom2d.Geom2d_Curve | None, theFirstIn: float, theLastIn: float, theTolerance: float) -> tuple[nanoocp.Geom2d.Geom2d_Line, float, float, float]:
        """
        Try to convert BSpline2d or Bezier2d to line 2d
        only if it is linear. Recalculate first and last parameters.
        Returns line2d or null curve2d.
        """

    @staticmethod
    def SimplifyBSpline2d(theTolerance: float) -> tuple[bool, nanoocp.Geom2d.Geom2d_BSplineCurve]:
        """
        Try to remove knots from bspline where local derivatives are the same.
        Remove knots with given precision.
        Returns false if Bsplien was not modified
        """

class ShapeCustom_DirectModification(ShapeCustom_Modification):
    """
    implements a modification for the BRepTools
    Modifier algorithm. Will redress indirect
    surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_DirectModification) -> None: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <S>, <L>, <Tol> are not
        significant.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <C>, <L>, <Tol> are not
        significant.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex <V> has been
        modified. In this case, <P> is the new geometric
        support of the vertex, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has a new
        curve on surface on the face <F>.In this case, <C>
        is the new geometric support of the edge, <L> the
        new location, <Tol> the new tolerance.

        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.

        <NewE> is the new edge created from <E>. <NewF>
        is the new face created from <F>. They may be useful.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex <V> has a new
        parameter on the edge <E>. In this case, <P> is
        the parameter, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of <NewE> between <NewF1>
        and <NewF2>.

        <NewE> is the new edge created from <E>. <NewF1>
        (resp. <NewF2>) is the new face created from <F1>
        (resp. <F2>).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_RestrictionParameters(nanoocp.Standard.Standard_Transient):
    """
    This class is axuluary tool which contains parameters for
    BSplineRestriction class.
    """

    @overload
    def __init__(self) -> None:
        """Sets default parameters."""

    @overload
    def __init__(self, theOther: ShapeCustom_RestrictionParameters) -> None: ...

    def GMaxDegree(self) -> int:
        """Returns (modifiable) maximal degree of approximation."""

    def SetGMaxDegree(self, theValue: int) -> None:
        """
        Python addition: sets the value GMaxDegree() returns by reference in C++.
        """

    def GMaxSeg(self) -> int:
        """
        Returns (modifiable) maximal number of spans of
        approximation.
        """

    def SetGMaxSeg(self, theValue: int) -> None:
        """Python addition: sets the value GMaxSeg() returns by reference in C++."""

    def ConvertPlane(self) -> bool:
        """Sets flag for define if Plane converted to BSpline surface."""

    def SetConvertPlane(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertPlane() returns by reference in C++.
        """

    def ConvertBezierSurf(self) -> bool:
        """
        Sets flag for define if Bezier surface converted to BSpline
        surface.
        """

    def SetConvertBezierSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertBezierSurf() returns by reference in C++.
        """

    def ConvertRevolutionSurf(self) -> bool:
        """
        Sets flag for define if surface of Revolution converted to
        BSpline surface.
        """

    def SetConvertRevolutionSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertRevolutionSurf() returns by reference in C++.
        """

    def ConvertExtrusionSurf(self) -> bool:
        """
        Sets flag for define if surface of LinearExtrusion converted
        to BSpline surface.
        """

    def SetConvertExtrusionSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertExtrusionSurf() returns by reference in C++.
        """

    def ConvertOffsetSurf(self) -> bool:
        """
        Sets flag for define if Offset surface converted to BSpline
        surface.
        """

    def SetConvertOffsetSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertOffsetSurf() returns by reference in C++.
        """

    def ConvertCylindricalSurf(self) -> bool:
        """
        Sets flag for define if cylindrical surface converted to BSpline
        surface.
        """

    def SetConvertCylindricalSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertCylindricalSurf() returns by reference in C++.
        """

    def ConvertConicalSurf(self) -> bool:
        """
        Sets flag for define if conical surface converted to BSpline
        surface.
        """

    def SetConvertConicalSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertConicalSurf() returns by reference in C++.
        """

    def ConvertToroidalSurf(self) -> bool:
        """
        Sets flag for define if toroidal surface converted to BSpline
        surface.
        """

    def SetConvertToroidalSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertToroidalSurf() returns by reference in C++.
        """

    def ConvertSphericalSurf(self) -> bool:
        """
        Sets flag for define if spherical surface converted to BSpline
        surface.
        """

    def SetConvertSphericalSurf(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertSphericalSurf() returns by reference in C++.
        """

    def SegmentSurfaceMode(self) -> bool:
        """
        Sets Segment mode for surface. If Segment is True surface is
        approximated in the bondaries of face lying on this surface.
        """

    def SetSegmentSurfaceMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value SegmentSurfaceMode() returns by reference in C++.
        """

    def ConvertCurve3d(self) -> bool:
        """Sets flag for define if 3d curve converted to BSpline curve."""

    def SetConvertCurve3d(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertCurve3d() returns by reference in C++.
        """

    def ConvertOffsetCurv3d(self) -> bool:
        """
        Sets flag for define if Offset curve3d converted to BSpline
        surface.
        """

    def SetConvertOffsetCurv3d(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertOffsetCurv3d() returns by reference in C++.
        """

    def ConvertCurve2d(self) -> bool:
        """
        Returns (modifiable) flag for define if 2d curve converted
        to BSpline curve.
        """

    def SetConvertCurve2d(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertCurve2d() returns by reference in C++.
        """

    def ConvertOffsetCurv2d(self) -> bool:
        """
        Returns (modifiable) flag for define if Offset curve2d
        converted to BSpline surface.
        """

    def SetConvertOffsetCurv2d(self, theValue: bool) -> None:
        """
        Python addition: sets the value ConvertOffsetCurv2d() returns by reference in C++.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_Surface:
    """
    Converts a surface to the analytical form with given
    precision. Conversion is done only the surface is bspline
    of bezier and this can be approximated by some analytical
    surface with that precision.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_Surface) -> None: ...

    def Init(self, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    def Gap(self) -> float:
        """
        Returns maximal deviation of converted surface from the original
        one computed by last call to ConvertToAnalytical
        """

    def ConvertToAnalytical(self, tol: float, substitute: bool) -> nanoocp.Geom.Geom_Surface:
        """
        Tries to convert the Surface to an Analytic form
        Returns the result
        Works only if the Surface is BSpline or Bezier.
        Else, or in case of failure, returns a Null Handle

        If <substitute> is True, the new surface replaces the actual
        one in <me>

        It works by analysing the case which can apply, creating the
        corresponding analytic surface, then checking coincidence
        Warning: Parameter laws are not kept, hence PCurves should be redone
        """

    def ConvertToPeriodic(self, substitute: bool, preci: float = -1.0) -> nanoocp.Geom.Geom_Surface:
        """
        Tries to convert the Surface to the Periodic form
        Returns the resulting surface
        Works only if the Surface is BSpline and is closed with
        Precision::Confusion()
        Else, or in case of failure, returns a Null Handle
        """

class ShapeCustom_SweptToElementary(ShapeCustom_Modification):
    """
    implements a modification for the BRepTools
    Modifier algorithm. Converts all elementary
    surfaces into surfaces of revolution.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeCustom_SweptToElementary) -> None: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <S>, <L>, <Tol> are not
        significant.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <C>, <L>, <Tol> are not
        significant.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex <V> has been
        modified. In this case, <P> is the new geometric
        support of the vertex, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has a new
        curve on surface on the face <F>.In this case, <C>
        is the new geometric support of the edge, <L> the
        new location, <Tol> the new tolerance.

        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.

        <NewE> is the new edge created from <E>. <NewF>
        is the new face created from <F>. They may be useful.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex <V> has a new
        parameter on the edge <E>. In this case, <P> is
        the parameter, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of <NewE> between <NewF1>
        and <NewF2>.

        <NewE> is the new edge created from <E>. <NewF1>
        (resp. <NewF2>) is the new face created from <F1>
        (resp. <F2>).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeCustom_TrsfModification(nanoocp.BRepTools.BRepTools_TrsfModification):
    """
    Complements BRepTools_TrsfModification to provide reversible
    scaling regarding tolerances.
    Uses actual tolerances (attached to the shapes) not ones
    returned by BRep_Tool::Tolerance to work with tolerances
    lower than Precision::Confusion.
    """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeCustom_TrsfModification) -> None: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Calls inherited method.
        Sets <Tol> as actual tolerance of <F> multiplied with scale
        factor.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Calls inherited method.
        Sets <Tol> as actual tolerance of <E> multiplied with scale
        factor.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Calls inherited method.
        Sets <Tol> as actual tolerance of <V> multiplied with scale
        factor.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Calls inherited method.
        Sets <Tol> as actual tolerance of <E> multiplied with scale
        factor.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Calls inherited method.
        Sets <Tol> as actual tolerance of <V> multiplied with scale
        factor.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
