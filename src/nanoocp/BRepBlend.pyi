"""OCCT package BRepBlend (toolkit TKFillet)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.AppBlend
import nanoocp.Approx
import nanoocp.Blend
import nanoocp.BlendFunc
import nanoocp.ChFiDS
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.IntSurf
import nanoocp.Law
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.gp
import nanoocp.math


class BRepBlend_AppFuncRoot(nanoocp.Approx.Approx_SweepFunction):
    """Function to approximate by AppSurface"""

    def D0(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """compute the section for v = param"""

    def D1(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the first derivative in v direction of the
        section for v = param
        """

    def D2(self, Param: float, First: float, Last: float, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        compute the second derivative in v direction of the
        section for v = param
        """

    def Nb2dCurves(self) -> int:
        """get the number of 2d curves to approximate."""

    def SectionShape(self) -> tuple[int, int, int]:
        """get the format of an section"""

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """get the Knots of the section"""

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """get the Multplicities of the section"""

    def IsRational(self) -> bool:
        """Returns if the section is rational or not"""

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def SetInterval(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the fonction
        This determines the derivatives in these values if the
        function is not Cn.
        """

    def Resolution(self, Index: int, Tol: float) -> tuple[float, float]:
        """
        Returns the resolutions in the sub-space 2d <Index> --
        This information is useful to find a good tolerance in
        2d approximation
        """

    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary (in radian)
        SurfTol error inside the surface.
        """

    def SetTolerance(self, Tol3d: float, Tol2d: float) -> None:
        """
        Is useful, if (me) has to be run numerical
        algorithm to perform D0, D1 or D2
        """

    def BarycentreOfSurf(self) -> nanoocp.gp.gp_Pnt:
        """
        Get the barycentre of Surface. An very poor
        estimation is sufficient. This information is useful
        to perform well conditioned rational approximation.
        """

    def MaximalSection(self) -> float:
        """
        Returns the length of the maximum section. This
        information is useful to perform well conditioned rational
        approximation.
        """

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections. This information is useful to
        perform well conditioned rational approximation.
        """

    def Point(self, Func: nanoocp.Blend.Blend_AppFunction, Param: float, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    def Vec(self, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBlend_AppFunc(BRepBlend_AppFuncRoot):
    """
    Function to approximate by AppSurface
    for Surface/Surface contact.
    """

    def __init__(self, Line: BRepBlend_Line | None, Func: nanoocp.Blend.Blend_Function, Tol3d: float, Tol2d: float) -> None: ...

    def Point(self, Func: nanoocp.Blend.Blend_AppFunction, Param: float, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    def Vec(self, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBlend_AppFuncRst(BRepBlend_AppFuncRoot):
    """Function to approximate by AppSurface for Curve/Surface contact."""

    def __init__(self, Line: BRepBlend_Line | None, Func: nanoocp.Blend.Blend_SurfRstFunction, Tol3d: float, Tol2d: float) -> None: ...

    def Point(self, Func: nanoocp.Blend.Blend_AppFunction, Param: float, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    def Vec(self, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBlend_AppFuncRstRst(BRepBlend_AppFuncRoot):
    """
    Function to approximate by AppSurface for Edge/Face (Curve/Curve contact).
    """

    def __init__(self, Line: BRepBlend_Line | None, Func: nanoocp.Blend.Blend_RstRstFunction, Tol3d: float, Tol2d: float) -> None: ...

    def Point(self, Func: nanoocp.Blend.Blend_AppFunction, Param: float, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    def Vec(self, Sol: nanoocp.math.math_Vector, Pnt: nanoocp.Blend.Blend_Point) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBlend_AppSurf(nanoocp.AppBlend.AppBlend_Approx):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_AppSurf) -> None: ...

    def Init(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: bool = False) -> None: ...

    def SetParType(self, ParType: nanoocp.Approx.Approx_ParametrizationType) -> None:
        """Define the type of parametrization used in the approximation"""

    def SetContinuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Define the Continuity used in the approximation"""

    def SetCriteriumWeight(self, W1: float, W2: float, W3: float) -> None:
        """
        define the Weights associed to the criterium used in
        the optimization.

        if Wi <= 0
        """

    def ParType(self) -> nanoocp.Approx.Approx_ParametrizationType:
        """returns the type of parametrization used in the approximation"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """returns the Continuity used in the approximation"""

    def CriteriumWeight(self) -> tuple[float, float, float]:
        """
        returns the Weights (as percent) associed to the criterium used in
        the optimization.
        """

    @overload
    def Perform(self, Lin: BRepBlend_Line | None, SecGen: nanoocp.Blend.Blend_AppFunction, SpApprox: bool = False) -> None: ...

    @overload
    def Perform(self, Lin: BRepBlend_Line | None, SecGen: nanoocp.Blend.Blend_AppFunction, NbMaxP: int) -> None: ...

    def PerformSmoothing(self, Lin: BRepBlend_Line | None, SecGen: nanoocp.Blend.Blend_AppFunction) -> None: ...

    def IsDone(self) -> bool: ...

    def SurfShape(self) -> tuple[int, int, int, int, int, int]: ...

    def Surface(self, TPoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], TWeights: nanoocp.NCollection.NCollection_Array2[float], TUKnots: nanoocp.NCollection.NCollection_Array1[float], TVKnots: nanoocp.NCollection.NCollection_Array1[float], TUMults: nanoocp.NCollection.NCollection_Array1[int], TVMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def UDegree(self) -> int: ...

    def VDegree(self) -> int: ...

    def SurfPoles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]: ...

    def SurfWeights(self) -> nanoocp.NCollection.NCollection_Array2[float]: ...

    def SurfUKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfVKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfUMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def SurfVMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def NbCurves2d(self) -> int: ...

    def Curves2dShape(self) -> tuple[int, int, int]: ...

    def Curve2d(self, Index: int, TPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TKnots: nanoocp.NCollection.NCollection_Array1[float], TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Curves2dDegree(self) -> int: ...

    def Curve2dPoles(self, Index: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]: ...

    def Curves2dKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def Curves2dMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def TolReached(self) -> tuple[float, float]: ...

    def TolCurveOnSurf(self, Index: int) -> float: ...

class BRepBlend_AppSurface(nanoocp.AppBlend.AppBlend_Approx):
    """Used to Approximate the blending surfaces."""

    @overload
    def __init__(self, Funct: nanoocp.Approx.Approx_SweepFunction | None, First: float, Last: float, Tol3d: float, Tol2d: float, TolAngular: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C0, Degmax: int = 11, Segmax: int = 50) -> None:
        """
        Approximation of the new Surface (and
        eventually the 2d Curves on the support
        surfaces).
        Normally the 2d curve are
        approximated with a tolerance given by the
        resolution on support surfaces, but if this
        tolerance is too large Tol2d is used.
        """

    @overload
    def __init__(self, theOther: BRepBlend_AppSurface) -> None: ...

    def IsDone(self) -> bool: ...

    def SurfShape(self) -> tuple[int, int, int, int, int, int]: ...

    def Surface(self, TPoles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], TWeights: nanoocp.NCollection.NCollection_Array2[float], TUKnots: nanoocp.NCollection.NCollection_Array1[float], TVKnots: nanoocp.NCollection.NCollection_Array1[float], TUMults: nanoocp.NCollection.NCollection_Array1[int], TVMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def UDegree(self) -> int: ...

    def VDegree(self) -> int: ...

    def SurfPoles(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]: ...

    def SurfWeights(self) -> nanoocp.NCollection.NCollection_Array2[float]: ...

    def SurfUKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfVKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SurfUMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def SurfVMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def MaxErrorOnSurf(self) -> float:
        """returns the maximum error in the surface approximation."""

    def NbCurves2d(self) -> int: ...

    def Curves2dShape(self) -> tuple[int, int, int]: ...

    def Curve2d(self, Index: int, TPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], TKnots: nanoocp.NCollection.NCollection_Array1[float], TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Curves2dDegree(self) -> int: ...

    def Curve2dPoles(self, Index: int) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]: ...

    def Curves2dKnots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def Curves2dMults(self) -> nanoocp.NCollection.NCollection_Array1[int]: ...

    def TolReached(self) -> tuple[float, float]: ...

    def Max2dError(self, Index: int) -> float:
        """returns the maximum error in the <Index> 2d curve approximation."""

    def TolCurveOnSurf(self, Index: int) -> float: ...

    def Dump(self) -> object:
        """display information on approximation."""

class BRepBlend_BlendTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_BlendTool) -> None: ...

    @staticmethod
    def Project(P: nanoocp.gp.gp_Pnt2d, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> tuple[bool, float, float]:
        """
        Projects the point P on the arc C.
        If the methods returns true, the projection is
        successful, and Paramproj is the parameter on the arc
        of the projected point, Dist is the distance between
        P and the curve..
        If the method returns false, Param proj and Dist
        are not significant.
        """

    @staticmethod
    def Inters(P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> tuple[bool, float, float]: ...

    @staticmethod
    def Parameter(V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """Returns the parameter of the vertex V on the edge A."""

    @staticmethod
    def Tolerance(V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """
        Returns the parametric tolerance on the arc A
        used to consider that the vertex and another point meet,
        i-e if std::abs(Parameter(Vertex)-Parameter(OtherPnt))<=
        Tolerance, the points are "merged".
        """

    @staticmethod
    def SingularOnUMin(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> bool: ...

    @staticmethod
    def SingularOnUMax(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> bool: ...

    @staticmethod
    def SingularOnVMin(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> bool: ...

    @staticmethod
    def SingularOnVMax(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> bool: ...

    @staticmethod
    def NbSamplesU(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, u1: float, u2: float) -> int: ...

    @staticmethod
    def NbSamplesV(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, v1: float, v2: float) -> int: ...

    @staticmethod
    def Bounds(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> tuple[float, float]:
        """
        Returns the parametric limits on the arc C.
        These limits must be finite : they are either
        the real limits of the arc, for a finite arc,
        or a bounding box for an infinite arc.
        """

    @staticmethod
    def CurveOnSurf(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

class BRepBlend_PointOnRst:
    """
    Definition of an intersection point between a line
    and a restriction on a surface.
    Such a point is contains geometrical information (see
    the Value method) and logical information.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Param: float, TLine: nanoocp.IntSurf.IntSurf_Transition, TArc: nanoocp.IntSurf.IntSurf_Transition) -> None:
        """
        Creates the PointOnRst on the arc A, at parameter Param,
        with the transition TLine on the walking line, and
        TArc on the arc A.
        """

    @overload
    def __init__(self, theOther: BRepBlend_PointOnRst) -> None: ...

    def SetArc(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Param: float, TLine: nanoocp.IntSurf.IntSurf_Transition, TArc: nanoocp.IntSurf.IntSurf_Transition) -> None:
        """
        Sets the values of a point which is on the arc
        A, at parameter Param.
        """

    def Arc(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the arc of restriction containing the
        vertex.
        """

    def TransitionOnLine(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """
        Returns the transition of the point on the
        line on surface.
        """

    def TransitionOnArc(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """
        Returns the transition of the point on the arc
        returned by Arc().
        """

    def ParameterOnArc(self) -> float:
        """
        Returns the parameter of the point on the
        arc returned by the method Arc().
        """

class BRepBlend_CSWalking:
    @overload
    def __init__(self, Curv: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_CSWalking) -> None: ...

    def Perform(self, F: nanoocp.Blend.Blend_CSFunction, Pdep: float, Pmax: float, MaxStep: float, Tol3d: float, TolGuide: float, Soldep: nanoocp.math.math_Vector, Fleche: float, Appro: bool = False) -> None: ...

    def Complete(self, F: nanoocp.Blend.Blend_CSFunction, Pmin: float) -> bool: ...

class BRepBlend_CurvPointRadInv(nanoocp.Blend.Blend_CurvPointFuncInv):
    """
    Function of reframing between a point and a curve.
    valid in cases of constant and progressive radius.
    This function is used to find a solution on a done
    point of the curve 1 when using RstRstConsRad or
    CSConstRad...
    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates w, U where w is the parameter on the
    guide line, U are the parametric coordinates of a
    point on the partner curve 2.
    """

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve | None, C2: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_CurvPointRadInv) -> None: ...

    @overload
    def Set(self, Choix: int) -> None: ...

    @overload
    def Set(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Set the Point on which a solution has to be found."""

    def NbEquations(self) -> int:
        """returns 2."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 3 variables;
        Tol is the tolerance used in 3d space.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 3 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        """

class BRepBlend_Extremity:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, W: float, Param: float, Tol: float) -> None:
        """Creates an extremity on a curve"""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, U: float, V: float, Param: float, Tol: float) -> None:
        """Creates an extremity on a surface"""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, U: float, V: float, Param: float, Tol: float, Vtx: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> None:
        """
        Creates an extremity on a surface. This extremity matches
        the vertex <Vtx>.
        """

    @overload
    def __init__(self, theOther: BRepBlend_Extremity) -> None: ...

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, U: float, V: float, Param: float, Tol: float) -> None:
        """Set the values for an extremity on a surface."""

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, U: float, V: float, Param: float, Tol: float, Vtx: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> None:
        """
        Set the values for an extremity on a surface.This
        extremity matches the vertex <Vtx>.
        """

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, W: float, Param: float, Tol: float) -> None:
        """Set the values for an extremity on curve."""

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """This method returns the value of the point in 3d space."""

    def SetTangent(self, Tangent: nanoocp.gp.gp_Vec) -> None:
        """
        Set the tangent vector for an extremity on a
        surface.
        """

    def HasTangent(self) -> bool:
        """Returns TRUE if the Tangent is stored."""

    def Tangent(self) -> nanoocp.gp.gp_Vec:
        """
        This method returns the value of tangent in 3d
        space.
        """

    def Tolerance(self) -> float:
        """
        This method returns the fuzziness on the point
        in 3d space.
        """

    def SetVertex(self, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> None:
        """Set the values for an extremity on a curve."""

    def AddArc(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Param: float, TLine: nanoocp.IntSurf.IntSurf_Transition, TArc: nanoocp.IntSurf.IntSurf_Transition) -> None:
        """
        Sets the values of a point which is on the arc
        A, at parameter Param.
        """

    def Parameters(self) -> tuple[float, float]:
        """
        This method returns the parameters of the point
        on the concerned surface.
        """

    def IsVertex(self) -> bool:
        """
        Returns true when the point coincide with
        an existing vertex.
        """

    def Vertex(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex:
        """Returns the vertex when IsVertex returns true."""

    def NbPointOnRst(self) -> int:
        """
        Returns the number of arc containing the extremity.
        If the method returns 0, the point is inside the
        surface.
        Otherwise, the extremity lies on at least 1 arc,
        and all the information (arc, parameter, transitions)
        are given by the point on restriction (PointOnRst)
        returned by the next method.
        """

    def PointOnRst(self, Index: int) -> BRepBlend_PointOnRst: ...

    def Parameter(self) -> float: ...

    def ParameterOnGuide(self) -> float: ...

class BRepBlend_HCurve2dTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_HCurve2dTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    @staticmethod
    def Continuity(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(myclass) >= <S>
        """

    @staticmethod
    def Intervals(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    @staticmethod
    def IsClosed(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool: ...

    @staticmethod
    def IsPeriodic(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool: ...

    @staticmethod
    def Period(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    @staticmethod
    def Value(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D0(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D1(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    @staticmethod
    def D2(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    @staticmethod
    def D3(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    @staticmethod
    def DN(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    @staticmethod
    def Resolution(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Lin2d: ...

    @staticmethod
    def Circle(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Circ2d: ...

    @staticmethod
    def Ellipse(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Elips2d: ...

    @staticmethod
    def Hyperbola(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Hypr2d: ...

    @staticmethod
    def Parabola(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Parab2d: ...

    @staticmethod
    def Bezier(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    @staticmethod
    def BSpline(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @staticmethod
    def NbSamples(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U0: float, U1: float) -> int: ...

class BRepBlend_HCurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_HCurveTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> float: ...

    @staticmethod
    def Continuity(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(myclass) >= <S>
        """

    @staticmethod
    def Intervals(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    @staticmethod
    def IsClosed(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool: ...

    @staticmethod
    def IsPeriodic(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool: ...

    @staticmethod
    def Period(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> float: ...

    @staticmethod
    def Value(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D0(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D1(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    @staticmethod
    def D2(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    @staticmethod
    def D3(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    @staticmethod
    def DN(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    @staticmethod
    def Resolution(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Lin: ...

    @staticmethod
    def Circle(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Circ: ...

    @staticmethod
    def Ellipse(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Elips: ...

    @staticmethod
    def Hyperbola(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Hypr: ...

    @staticmethod
    def Parabola(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Parab: ...

    @staticmethod
    def Bezier(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.Geom.Geom_BezierCurve: ...

    @staticmethod
    def BSpline(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @staticmethod
    def NbSamples(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U0: float, U1: float) -> int: ...

class BRepBlend_Line(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_Line) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the line."""

    def Append(self, P: nanoocp.Blend.Blend_Point) -> None:
        """Adds a point in the line."""

    def Prepend(self, P: nanoocp.Blend.Blend_Point) -> None:
        """Adds a point in the line at the first place."""

    def InsertBefore(self, Index: int, P: nanoocp.Blend.Blend_Point) -> None:
        """Adds a point in the line at the first place."""

    def Remove(self, FromIndex: int, ToIndex: int) -> None:
        """
        Removes from <me> all the items of
        positions between <FromIndex> and <ToIndex>.
        Raises an exception if the indices are out of bounds.
        """

    @overload
    def Set(self, TranS1: nanoocp.IntSurf.IntSurf_TypeTrans, TranS2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Sets the value of the transition of the line on S1 and
        the line on S2.
        """

    @overload
    def Set(self, Trans: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """Sets the value of the transition of the line on a surface"""

    def SetStartPoints(self, StartPt1: BRepBlend_Extremity, StartPt2: BRepBlend_Extremity) -> None:
        """Sets the values of the start points for the line."""

    def SetEndPoints(self, EndPt1: BRepBlend_Extremity, EndPt2: BRepBlend_Extremity) -> None:
        """Sets tne values of the end points for the line."""

    def NbPoints(self) -> int:
        """Returns the number of points in the line."""

    def Point(self, Index: int) -> nanoocp.Blend.Blend_Point:
        """Returns the point of range Index."""

    def TransitionOnS1(self) -> nanoocp.IntSurf.IntSurf_TypeTrans:
        """
        Returns the type of the transition of the line defined
        on the first surface. The transition is "constant"
        along the line.
        The transition is IN if the line is oriented in such
        a way that the system of vectors (N,DRac,T) is
        right-handed, where
        N is the normal to the first surface at a point P,
        DRac is a vector tangent to the blending patch,
        oriented towards the valid part of this patch,
        T is the tangent to the line on S1 at P.
        The transitioon is OUT when the system of vectors is
        left-handed.
        """

    def TransitionOnS2(self) -> nanoocp.IntSurf.IntSurf_TypeTrans:
        """
        Returns the type of the transition of the line defined
        on the second surface. The transition is "constant"
        along the line.
        """

    def StartPointOnFirst(self) -> BRepBlend_Extremity:
        """Returns the start point on S1."""

    def StartPointOnSecond(self) -> BRepBlend_Extremity:
        """Returns the start point on S2"""

    def EndPointOnFirst(self) -> BRepBlend_Extremity:
        """Returns the end point on S1."""

    def EndPointOnSecond(self) -> BRepBlend_Extremity:
        """Returns the point on S2."""

    def TransitionOnS(self) -> nanoocp.IntSurf.IntSurf_TypeTrans:
        """
        Returns the type of the transition of the line defined
        on the surface.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepBlend_RstRstConstRad(nanoocp.Blend.Blend_RstRstFunction):
    """
    Copy of CSConstRad with a pcurve on surface
    as support.
    """

    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_RstRstConstRad) -> None: ...

    def NbVariables(self) -> int:
        """Returns 2."""

    def NbEquations(self) -> int:
        """Returns 2."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Set(self, SurfRef1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, RstRef1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, SurfRef2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, RstRef2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def Set(self, Radius: float, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: nanoocp.BlendFunc.BlendFunc_SectionShape) -> None:
        """
        Sets the type of section generation for the
        approximations.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def PointOnRst1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnRst2(self) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2dOnRst1(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def Pnt2dOnRst2(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns U,V coordinates of the point on the curve on
        surface.
        """

    def ParameterOnRst1(self) -> float:
        """Returns parameter of the point on the curve."""

    def ParameterOnRst2(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnRst1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnRst1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnRst2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnRst2(self) -> nanoocp.gp.gp_Vec2d: ...

    def Decroch(self, Sol: nanoocp.math.math_Vector, NRst1: nanoocp.gp.gp_Vec, TgRst1: nanoocp.gp.gp_Vec, NRst2: nanoocp.gp.gp_Vec, TgRst2: nanoocp.gp.gp_Vec) -> nanoocp.Blend.Blend_DecrochStatus:
        """
        Allows implementing a specific termination criterion
        for the function.
        """

    def CenterCircleRst1Rst2(self, PtRst1: nanoocp.gp.gp_Pnt, PtRst2: nanoocp.gp.gp_Pnt, np: nanoocp.gp.gp_Vec, Center: nanoocp.gp.gp_Pnt, VdMed: nanoocp.gp.gp_Vec) -> bool:
        """
        Give the center of circle define by PtRst1, PtRst2 and
        radius ray.
        """

    @overload
    def Section(self, Param: float, U: float, V: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    def IsRational(self) -> bool:
        """Returns if the section is rational"""

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections.
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.
        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BRepBlend_RstRstEvolRad(nanoocp.Blend.Blend_RstRstFunction):
    """
    Function to approximate by AppSurface for
    Edge/Edge and evolutif radius
    """

    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Evol: nanoocp.Law.Law_Function | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_RstRstEvolRad) -> None: ...

    def NbVariables(self) -> int:
        """Returns 2."""

    def NbEquations(self) -> int:
        """Returns 2."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Set(self, SurfRef1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, RstRef1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, SurfRef2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, RstRef2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def Set(self, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: nanoocp.BlendFunc.BlendFunc_SectionShape) -> None:
        """
        Sets the type of section generation for the
        approximations.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def PointOnRst1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnRst2(self) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2dOnRst1(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def Pnt2dOnRst2(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns U,V coordinates of the point on the curve on
        surface.
        """

    def ParameterOnRst1(self) -> float:
        """Returns parameter of the point on the curve."""

    def ParameterOnRst2(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnRst1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnRst1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnRst2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnRst2(self) -> nanoocp.gp.gp_Vec2d: ...

    def Decroch(self, Sol: nanoocp.math.math_Vector, NRst1: nanoocp.gp.gp_Vec, TgRst1: nanoocp.gp.gp_Vec, NRst2: nanoocp.gp.gp_Vec, TgRst2: nanoocp.gp.gp_Vec) -> nanoocp.Blend.Blend_DecrochStatus:
        """
        Enables implementation of a criterion of decrochage
        specific to the function.
        """

    def CenterCircleRst1Rst2(self, PtRst1: nanoocp.gp.gp_Pnt, PtRst2: nanoocp.gp.gp_Pnt, np: nanoocp.gp.gp_Vec, Center: nanoocp.gp.gp_Pnt, VdMed: nanoocp.gp.gp_Vec) -> bool:
        """
        Gives the center of circle defined by PtRst1, PtRst2 and
        radius ray.
        """

    @overload
    def Section(self, Param: float, U: float, V: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    def IsRational(self) -> bool:
        """Returns if the section is rational"""

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections.
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.
        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BRepBlend_RstRstLineBuilder:
    """
    This class processes the data resulting from
    Blend_CSWalking but it takes in consideration the Surface
    supporting the curve to detect the breakpoint.

    As a result, the criteria of distribution of
    points on the line become more flexible because it
    should calculate values approached
    by an approximation of continued functions based on the
    Blend_RstRstFunction.

    Thus this pseudo path necessitates 3 criteria of
    regrouping:

    1) exit of the domain of the curve

    2) exit of the domain of the surface

    3) stall as there is a solution of problem
    surf/surf within the domain of the surface
    of support of the restriction.

    Construction of a BRepBlend_Line between two pcurves
    from an approached starting solution. The output
    entries of this builder are of the same nature
    as of a traditional walking, but the requirements
    to the Line are not the same. If the determination of validity range is always
    guaranteed, the criteria of correct repartition of sections
    before smoothing are not respected. The resulting Line
    is f(t) oriented.
    """

    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst1: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst2: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_RstRstLineBuilder) -> None: ...

    def Perform(self, Func: nanoocp.Blend.Blend_RstRstFunction, Finv1: nanoocp.Blend.Blend_SurfCurvFuncInv, FinvP1: nanoocp.Blend.Blend_CurvPointFuncInv, Finv2: nanoocp.Blend.Blend_SurfCurvFuncInv, FinvP2: nanoocp.Blend.Blend_CurvPointFuncInv, Pdep: float, Pmax: float, MaxStep: float, Tol3d: float, TolGuide: float, Soldep: nanoocp.math.math_Vector, Fleche: float, Appro: bool = False) -> None: ...

    def PerformFirstSection(self, Func: nanoocp.Blend.Blend_RstRstFunction, Finv1: nanoocp.Blend.Blend_SurfCurvFuncInv, FinvP1: nanoocp.Blend.Blend_CurvPointFuncInv, Finv2: nanoocp.Blend.Blend_SurfCurvFuncInv, FinvP2: nanoocp.Blend.Blend_CurvPointFuncInv, Pdep: float, Pmax: float, Soldep: nanoocp.math.math_Vector, Tol3d: float, TolGuide: float, RecRst1: bool, RecP1: bool, RecRst2: bool, RecP2: bool, ParSol: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def Complete(self, Func: nanoocp.Blend.Blend_RstRstFunction, Finv1: nanoocp.Blend.Blend_SurfCurvFuncInv, FinvP1: nanoocp.Blend.Blend_CurvPointFuncInv, Finv2: nanoocp.Blend.Blend_SurfCurvFuncInv, FinvP2: nanoocp.Blend.Blend_CurvPointFuncInv, Pmin: float) -> bool: ...

    def IsDone(self) -> bool: ...

    def Line(self) -> BRepBlend_Line: ...

    def Decroch1Start(self) -> bool: ...

    def Decroch1End(self) -> bool: ...

    def Decroch2Start(self) -> bool: ...

    def Decroch2End(self) -> bool: ...

class BRepBlend_SurfCurvConstRadInv(nanoocp.Blend.Blend_SurfCurvFuncInv):
    """
    Function of reframing between a restriction surface of the
    surface and a curve.
    Class used to compute a solution of the
    surfRstConstRad problem on a done restriction of the
    surface.
    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates wguide, wcurv, wrst where wguide is the
    parameter on the guide line, wcurv is the parameter on
    the curve, wrst is the parameter on the restriction on
    the surface.
    """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Cg: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfCurvConstRadInv) -> None: ...

    @overload
    def Set(self, R: float, Choix: int) -> None: ...

    @overload
    def Set(self, Rst: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """Set the restriction on which a solution has to be found."""

    def NbEquations(self) -> int:
        """returns 3."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 3 variables;
        Tol is the tolerance used in 3d space.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 3 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        """

class BRepBlend_SurfCurvEvolRadInv(nanoocp.Blend.Blend_SurfCurvFuncInv):
    """
    Function of reframing between a surface restriction
    of the surface and a curve.
    Class used to compute a solution of the
    surfRstConstRad problem on a done restriction of the
    surface.
    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates wguide, wcurv, wrst where wguide is the
    parameter on the guide line, wcurv is the parameter on
    the curve, wrst is the parameter on the restriction on
    the surface.
    """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Cg: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Evol: nanoocp.Law.Law_Function | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfCurvEvolRadInv) -> None: ...

    @overload
    def Set(self, Choix: int) -> None: ...

    @overload
    def Set(self, Rst: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """Set the restriction on which a solution has to be found."""

    def NbEquations(self) -> int:
        """returns 3."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 3 variables;
        Tol is the tolerance used in 3d space.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 3 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        """

class BRepBlend_SurfPointConstRadInv(nanoocp.Blend.Blend_SurfPointFuncInv):
    """
    Function of reframing between a point and a surface.
    This function is used to find a solution on a done
    point of the curve when using SurfRstConsRad or
    CSConstRad...
    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates w, U, V where w is the parameter on the
    guide line, U,V are the parametric coordinates of a
    point on the partner surface.
    """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfPointConstRadInv) -> None: ...

    @overload
    def Set(self, R: float, Choix: int) -> None: ...

    @overload
    def Set(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Set the Point on which a solution has to be found."""

    def NbEquations(self) -> int:
        """returns 3."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 3 variables;
        Tol is the tolerance used in 3d space.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 3 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        """

class BRepBlend_SurfPointEvolRadInv(nanoocp.Blend.Blend_SurfPointFuncInv):
    """
    Function of reframing between a point and a surface.
    This function is used to find a solution on a done
    point of the curve when using SurfRstConsRad or
    CSConstRad...
    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates w, U, V where w is the parameter on the
    guide line, U,V are the parametric coordinates of a
    point on the partner surface.
    """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Evol: nanoocp.Law.Law_Function | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfPointEvolRadInv) -> None: ...

    @overload
    def Set(self, Choix: int) -> None: ...

    @overload
    def Set(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Set the Point on which a solution has to be found."""

    def NbEquations(self) -> int:
        """returns 3."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 3 variables;
        Tol is the tolerance used in 3d space.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 3 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        """

class BRepBlend_SurfRstConstRad(nanoocp.Blend.Blend_SurfRstFunction):
    """
    Copy of CSConstRad with pcurve on surface
    as support.
    """

    @overload
    def __init__(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, SurfRst: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfRstConstRad) -> None: ...

    def NbVariables(self) -> int:
        """Returns 3."""

    def NbEquations(self) -> int:
        """Returns 3."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Set(self, SurfRef: nanoocp.Adaptor3d.Adaptor3d_Surface | None, RstRef: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def Set(self, Radius: float, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: nanoocp.BlendFunc.BlendFunc_SectionShape) -> None:
        """
        Sets the type of section generation for the
        approximations.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def PointOnS(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnRst(self) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2dOnS(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def Pnt2dOnRst(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns U,V coordinates of the point on the curve on
        surface.
        """

    def ParameterOnRst(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnRst(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnRst(self) -> nanoocp.gp.gp_Vec2d: ...

    def Decroch(self, Sol: nanoocp.math.math_Vector, NS: nanoocp.gp.gp_Vec, TgS: nanoocp.gp.gp_Vec) -> bool:
        """
        Enables implementation of a criterion of decrochage
        specific to the function.
        Warning: Can be called without previous call of IsSolution
        but the values calculated can be senseless.
        """

    @overload
    def Section(self, Param: float, U: float, V: float, W: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def IsRational(self) -> bool:
        """Returns if the section is rational"""

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections.
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.
        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BRepBlend_SurfRstEvolRad(nanoocp.Blend.Blend_SurfRstFunction):
    """
    Function to approximate by AppSurface for
    Edge/Face and evolutif radius
    """

    @overload
    def __init__(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, SurfRst: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Evol: nanoocp.Law.Law_Function | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfRstEvolRad) -> None: ...

    def NbVariables(self) -> int:
        """Returns 3."""

    def NbEquations(self) -> int:
        """Returns 3."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Set(self, SurfRef: nanoocp.Adaptor3d.Adaptor3d_Surface | None, RstRef: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def Set(self, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: nanoocp.BlendFunc.BlendFunc_SectionShape) -> None:
        """
        Sets the type of section generation for the
        approximations.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def PointOnS(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnRst(self) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2dOnS(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def Pnt2dOnRst(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns U,V coordinates of the point on the curve on
        surface.
        """

    def ParameterOnRst(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnRst(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnRst(self) -> nanoocp.gp.gp_Vec2d: ...

    def Decroch(self, Sol: nanoocp.math.math_Vector, NS: nanoocp.gp.gp_Vec, TgS: nanoocp.gp.gp_Vec) -> bool:
        """
        Permet d'implementer un critere de decrochage
        specifique a la fonction.
        """

    @overload
    def Section(self, Param: float, U: float, V: float, W: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def IsRational(self) -> bool:
        """Returns if the section is rational"""

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

    def GetMinimalWeight(self, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the minimal value of weight for each poles
        of all sections.
        """

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.
        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BRepBlend_SurfRstLineBuilder:
    """
    This class processes data resulting from
    Blend_CSWalking taking in consideration the Surface
    supporting the curve to detect the breakpoint.

    The criteria of distribution of points on the line are detailed
    because it is to be used in the calculatuon of values approached
    by an approximation of functions continued basing on
    Blend_SurfRstFunction.

    Thus this pseudo path necessitates 3 criteria of regrouping:

    1) exit of the domain of the curve

    2) exit of the domain of the surface

    3) stall as there is a solution to the problem
    surf/surf within the domain of the surface
    of support of the restriction.

    Construction of a BRepBlend_Line between a surface and
    a pcurve on surface from an approached
    starting solution. The output entries of this builder
    are of the same nature as of the traditional walking
    but the requirements on the Line are not the same
    If the determination of validity range is always
    guaranteed, the criteria of correct repartition of sections
    before smoothing are not respected. The resulting Line
    is f(t) oriented.
    """

    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Rst: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_SurfRstLineBuilder) -> None: ...

    def Perform(self, Func: nanoocp.Blend.Blend_SurfRstFunction, Finv: nanoocp.Blend.Blend_FuncInv, FinvP: nanoocp.Blend.Blend_SurfPointFuncInv, FinvC: nanoocp.Blend.Blend_SurfCurvFuncInv, Pdep: float, Pmax: float, MaxStep: float, Tol3d: float, Tol2d: float, TolGuide: float, Soldep: nanoocp.math.math_Vector, Fleche: float, Appro: bool = False) -> None: ...

    def PerformFirstSection(self, Func: nanoocp.Blend.Blend_SurfRstFunction, Finv: nanoocp.Blend.Blend_FuncInv, FinvP: nanoocp.Blend.Blend_SurfPointFuncInv, FinvC: nanoocp.Blend.Blend_SurfCurvFuncInv, Pdep: float, Pmax: float, Soldep: nanoocp.math.math_Vector, Tol3d: float, Tol2d: float, TolGuide: float, RecRst: bool, RecP: bool, RecS: bool, ParSol: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def Complete(self, Func: nanoocp.Blend.Blend_SurfRstFunction, Finv: nanoocp.Blend.Blend_FuncInv, FinvP: nanoocp.Blend.Blend_SurfPointFuncInv, FinvC: nanoocp.Blend.Blend_SurfCurvFuncInv, Pmin: float) -> bool: ...

    def ArcToRecadre(self, Sol: nanoocp.math.math_Vector, PrevIndex: int, pt2d: nanoocp.gp.gp_Pnt2d, lastpt2d: nanoocp.gp.gp_Pnt2d) -> tuple[int, float]: ...

    def IsDone(self) -> bool: ...

    def Line(self) -> BRepBlend_Line: ...

    def DecrochStart(self) -> bool: ...

    def DecrochEnd(self) -> bool: ...

class BRepBlend_Walking:
    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, HGuide: nanoocp.ChFiDS.ChFiDS_ElSpine | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepBlend_Walking) -> None: ...

    def SetDomainsToRecadre(self, RecDomain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, RecDomain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> None:
        """To define different domains for control and clipping."""

    def AddSingularPoint(self, P: nanoocp.Blend.Blend_Point) -> None:
        """To define singular points computed before walking."""

    def Perform(self, F: nanoocp.Blend.Blend_Function, FInv: nanoocp.Blend.Blend_FuncInv, Pdep: float, Pmax: float, MaxStep: float, Tol3d: float, TolGuide: float, Soldep: nanoocp.math.math_Vector, Fleche: float, Appro: bool = False) -> None: ...

    @overload
    def PerformFirstSection(self, F: nanoocp.Blend.Blend_Function, Pdep: float, ParDep: nanoocp.math.math_Vector, Tol3d: float, TolGuide: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    @overload
    def PerformFirstSection(self, F: nanoocp.Blend.Blend_Function, FInv: nanoocp.Blend.Blend_FuncInv, Pdep: float, Pmax: float, ParDep: nanoocp.math.math_Vector, Tol3d: float, TolGuide: float, RecOnS1: bool, RecOnS2: bool, ParSol: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    @overload
    def Continu(self, F: nanoocp.Blend.Blend_Function, FInv: nanoocp.Blend.Blend_FuncInv, P: float) -> bool: ...

    @overload
    def Continu(self, F: nanoocp.Blend.Blend_Function, FInv: nanoocp.Blend.Blend_FuncInv, P: float, OnS1: bool) -> bool: ...

    def Complete(self, F: nanoocp.Blend.Blend_Function, FInv: nanoocp.Blend.Blend_FuncInv, Pmin: float) -> bool: ...

    def ClassificationOnS1(self, C: bool) -> None: ...

    def ClassificationOnS2(self, C: bool) -> None: ...

    def Check2d(self, C: bool) -> None: ...

    def Check(self, C: bool) -> None: ...

    def TwistOnS1(self) -> bool: ...

    def TwistOnS2(self) -> bool: ...

    def IsDone(self) -> bool: ...

    def Line(self) -> BRepBlend_Line: ...

# C++ typedef aliases
BRepBlend_Chamfer = nanoocp.BlendFunc.BlendFunc_Chamfer
BRepBlend_ChamfInv = nanoocp.BlendFunc.BlendFunc_ChamfInv
BRepBlend_ConstThroat = nanoocp.BlendFunc.BlendFunc_ConstThroat
BRepBlend_ConstThroatInv = nanoocp.BlendFunc.BlendFunc_ConstThroatInv
BRepBlend_ConstThroatWithPenetration = nanoocp.BlendFunc.BlendFunc_ConstThroatWithPenetration
BRepBlend_ConstThroatWithPenetrationInv = nanoocp.BlendFunc.BlendFunc_ConstThroatWithPenetrationInv
BRepBlend_ChAsym = nanoocp.BlendFunc.BlendFunc_ChAsym
BRepBlend_ChAsymInv = nanoocp.BlendFunc.BlendFunc_ChAsymInv
BRepBlend_ConstRad = nanoocp.BlendFunc.BlendFunc_ConstRad
BRepBlend_ConstRadInv = nanoocp.BlendFunc.BlendFunc_ConstRadInv
BRepBlend_CSCircular = nanoocp.BlendFunc.BlendFunc_CSCircular
BRepBlend_CSConstRad = nanoocp.BlendFunc.BlendFunc_CSConstRad
BRepBlend_EvolRad = nanoocp.BlendFunc.BlendFunc_EvolRad
BRepBlend_EvolRadInv = nanoocp.BlendFunc.BlendFunc_EvolRadInv
BRepBlend_Ruled = nanoocp.BlendFunc.BlendFunc_Ruled
BRepBlend_RuledInv = nanoocp.BlendFunc.BlendFunc_RuledInv
