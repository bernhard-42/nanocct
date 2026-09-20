"""OCCT package BRepLProp (toolkit TKBRep)"""

from typing import overload

import nanoocp.BRepAdaptor
import nanoocp.GeomAbs
import nanoocp.gp


class BRepLProp:
    """
    These global functions compute the degree of
    continuity of a curve built by concatenation of two
    edges at their junction point.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepLProp) -> None: ...

    @overload
    @staticmethod
    def Continuity(C1: nanoocp.BRepAdaptor.BRepAdaptor_Curve, C2: nanoocp.BRepAdaptor.BRepAdaptor_Curve, u1: float, u2: float, tl: float, ta: float) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Computes the regularity at the junction between C1 and
        C2. The point u1 on C1 and the point u2 on C2 must be
        confused. tl and ta are the linear and angular
        tolerance used two compare the derivative.
        """

    @overload
    @staticmethod
    def Continuity(C1: nanoocp.BRepAdaptor.BRepAdaptor_Curve, C2: nanoocp.BRepAdaptor.BRepAdaptor_Curve, u1: float, u2: float) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        The same as preceding but using the standard tolerances from package Precision.
        """

class BRepLProp_CLProps:
    """
    Implementation class for computing local properties of a curve:
    point, derivatives up to order 3, tangent, curvature, normal,
    and centre of curvature.
    Parameterized by geometric types (Pnt/Vec/Dir) and curve type.
    @tparam Pnt the point type (gp_Pnt for 3D, gp_Pnt2d for 2D)
    @tparam Vec the vector type (gp_Vec for 3D, gp_Vec2d for 2D)
    @tparam Dir the direction type (gp_Dir for 3D, gp_Dir2d for 2D)
    @tparam CurveType the curve storage type
    @tparam Access the access policy for evaluating curve derivatives
    """

    @overload
    def __init__(self, N: int, Resolution: float) -> None:
        """
        Same as previous constructor but here the parameter is
        set to the value <U> and the curve is set
        with SetCurve.
        the curve can have a empty constructor
        All the computations done will be related to <C> and <U>
        when the functions "set" will be done.
        """

    @overload
    def __init__(self, C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, N: int, Resolution: float) -> None:
        """
        Initializes the local properties of the curve <C>
        The current point and the derivatives are
        computed at the same time, which allows an
        optimization of the computation time.
        <N> indicates the maximum number of derivations to
        be done (0, 1, 2 or 3). For example, to compute
        only the tangent, N should be equal to 1.
        <Resolution> is the linear tolerance (it is used to test
        if a vector is null).
        """

    @overload
    def __init__(self, C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, N: int, Resolution: float) -> None:
        """
        Same as previous constructor but here the parameter is
        set to the value <U>.
        All the computations done will be related to <C> and <U>.
        """

    @overload
    def __init__(self, theOther: BRepLProp_CLProps) -> None: ...

    def SetParameter(self, U: float) -> None:
        """
        Initializes the local properties of the curve
        for the parameter value <U>.
        """

    def SetCurve(self, C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> None:
        """
        Initializes the local properties of the curve
        for the new curve.
        """

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the Point."""

    def D1(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the first derivative.
        The derivative is computed if it has not been yet.
        """

    def D2(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the second derivative.
        The derivative is computed if it has not been yet.
        """

    def D3(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the third derivative.
        The derivative is computed if it has not been yet.
        """

    def IsTangentDefined(self) -> bool:
        """
        Returns True if the tangent is defined.
        For example, the tangent is not defined if the
        three first derivatives are all null.
        """

    def Tangent(self, D: nanoocp.gp.gp_Dir) -> None:
        """output the tangent direction <D>."""

    def Curvature(self) -> float:
        """Returns the curvature."""

    def Normal(self, N: nanoocp.gp.gp_Dir) -> None:
        """Returns the normal direction <N>."""

    def CentreOfCurvature(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Returns the centre of curvature <P>."""

class BRepLProp_SLProps:
    """
    Template class for computing local properties of a 3D surface:
    point, first and second derivatives, tangent directions, normal,
    and curvature analysis (max, min, mean, Gaussian).
    @tparam SurfaceType the surface storage type (e.g. occ::handle<Geom_Surface>,
    BRepAdaptor_Surface, occ::handle<Adaptor3d_Surface>, HLRBRep_SurfacePtr)
    @tparam Access the access policy for evaluating surface derivatives
    """

    @overload
    def __init__(self, N: int, Resolution: float) -> None:
        """
        idem as previous constructor but without setting the value
        of parameters <U> and <V> and the surface.
        the surface can have an empty constructor.
        """

    @overload
    def __init__(self, S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, N: int, Resolution: float) -> None:
        """
        idem as previous constructor but without setting the value
        of parameters <U> and <V>.
        """

    @overload
    def __init__(self, S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, U: float, V: float, N: int, Resolution: float) -> None:
        """
        Initializes the local properties of the surface <S>
        for the parameter values (<U>, <V>).
        The current point and the derivatives are
        computed at the same time, which allows an
        optimization of the computation time.
        <N> indicates the maximum number of derivations to
        be done (0, 1, or 2). For example, to compute
        only the tangent, N should be equal to 1.
        <Resolution> is the linear tolerance (it is used to test
        if a vector is null).
        """

    @overload
    def __init__(self, theOther: BRepLProp_SLProps) -> None: ...

    def SetSurface(self, S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> None:
        """
        Initializes the local properties of the surface S
        for the new surface.
        """

    def SetParameters(self, U: float, V: float) -> None:
        """
        Initializes the local properties of the surface S
        for the new parameter values (<U>, <V>).
        """

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point."""

    def D1U(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the first U derivative.
        The derivative is computed if it has not been yet.
        """

    def D1V(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the first V derivative.
        The derivative is computed if it has not been yet.
        """

    def D2U(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the second U derivatives
        The derivative is computed if it has not been yet.
        """

    def D2V(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the second V derivative.
        The derivative is computed if it has not been yet.
        """

    def DUV(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the second UV cross-derivative.
        The derivative is computed if it has not been yet.
        """

    def IsTangentUDefined(self) -> bool:
        """
        returns True if the U tangent is defined.
        For example, the tangent is not defined if the
        two first U derivatives are null.
        """

    def TangentU(self, D: nanoocp.gp.gp_Dir) -> None:
        """Returns the tangent direction <D> on the iso-V."""

    def IsTangentVDefined(self) -> bool:
        """
        returns if the V tangent is defined.
        For example, the tangent is not defined if the
        two first V derivatives are null.
        """

    def TangentV(self, D: nanoocp.gp.gp_Dir) -> None:
        """Returns the tangent direction <D> on the iso-V."""

    def IsNormalDefined(self) -> bool:
        """Tells if the normal is defined."""

    def Normal(self) -> nanoocp.gp.gp_Dir:
        """Returns the normal direction."""

    def IsCurvatureDefined(self) -> bool:
        """returns True if the curvature is defined."""

    def IsUmbilic(self) -> bool:
        """
        returns True if the point is umbilic (i.e. if the
        curvature is constant).
        """

    def MaxCurvature(self) -> float:
        """Returns the maximum curvature"""

    def MinCurvature(self) -> float:
        """Returns the minimum curvature"""

    def CurvatureDirections(self, MaxD: nanoocp.gp.gp_Dir, MinD: nanoocp.gp.gp_Dir) -> None:
        """
        Returns the direction of the maximum and minimum curvature
        <MaxD> and <MinD>
        """

    def MeanCurvature(self) -> float:
        """Returns the mean curvature."""

    def GaussianCurvature(self) -> float:
        """Returns the Gaussian curvature"""

class BRepLProp_SurfaceTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepLProp_SurfaceTool) -> None: ...

    @staticmethod
    def Value(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, U: float, V: float, P: nanoocp.gp.gp_Pnt) -> None:
        """
        Computes the point <P> of parameter <U> and <V> on the
        Surface <S>.
        """

    @staticmethod
    def D1(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, U: float, V: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point <P> and first derivative <D1*> of
        parameter <U> and <V> on the Surface <S>.
        """

    @staticmethod
    def D2(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, U: float, V: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec, D2U: nanoocp.gp.gp_Vec, D2V: nanoocp.gp.gp_Vec, DUV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point <P>, the first derivative <D1*> and second
        derivative <D2*> of parameter <U> and <V> on the Surface <S>.
        """

    @staticmethod
    def DN(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, U: float, V: float, IU: int, IV: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def Continuity(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> int:
        """
        returns the order of continuity of the Surface <S>.
        returns 1 : first derivative only is computable
        returns 2 : first and second derivative only are computable.
        """

    @staticmethod
    def Bounds(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> tuple[float, float, float, float]:
        """returns the bounds of the Surface."""
