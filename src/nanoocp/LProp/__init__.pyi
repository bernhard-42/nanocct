"""OCCT package LProp (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
from nanoocp.LProp import LProp_CurveUtils as LProp_CurveUtils
import nanoocp.Standard
import nanoocp.gp


class LProp_CIType(enum.IntEnum):
    """
    Identifies the type of a particular point on a curve:
    - LProp_Inflection: a point of inflection
    - LProp_MinCur: a minimum of curvature
    - LProp_MaxCur: a maximum of curvature.
    """

    LProp_Inflection = 0

    LProp_MinCur = 1

    LProp_MaxCur = 2

LProp_Inflection: LProp_CIType = LProp_CIType.LProp_Inflection

LProp_MinCur: LProp_CIType = LProp_CIType.LProp_MinCur

LProp_MaxCur: LProp_CIType = LProp_CIType.LProp_MaxCur

class LProp_Status(enum.IntEnum):
    LProp_Undecided = 0

    LProp_Undefined = 1

    LProp_Defined = 2

    LProp_Computed = 3

LProp_Undecided: LProp_Status = LProp_Status.LProp_Undecided

LProp_Undefined: LProp_Status = LProp_Status.LProp_Undefined

LProp_Defined: LProp_Status = LProp_Status.LProp_Defined

LProp_Computed: LProp_Status = LProp_Status.LProp_Computed

class LProp_BadContinuity(nanoocp.Standard.Standard_Failure):
    pass

class LProp_NotDefined(nanoocp.Standard.Standard_Failure):
    pass

class LProp_CLProps3d:
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
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, N: int, Resolution: float) -> None:
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
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, N: int, Resolution: float) -> None:
        """
        Same as previous constructor but here the parameter is
        set to the value <U>.
        All the computations done will be related to <C> and <U>.
        """

    @overload
    def __init__(self, theOther: LProp_CLProps3d) -> None: ...

    def SetParameter(self, U: float) -> None:
        """
        Initializes the local properties of the curve
        for the parameter value <U>.
        """

    def SetCurve(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None:
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

class LProp_CurAndInf:
    """
    Stores the parameters of a curve 2d or 3d corresponding
    to the curvature's extremas and the Inflection's Points.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LProp_CurAndInf) -> None: ...

    def AddInflection(self, Param: float) -> None: ...

    def AddExtCur(self, Param: float, IsMin: bool) -> None: ...

    def Clear(self) -> None: ...

    def IsEmpty(self) -> bool: ...

    def NbPoints(self) -> int:
        """
        Returns the number of points.
        The Points are stored to increasing parameter.
        """

    def Parameter(self, N: int) -> float:
        """
        Returns the parameter of the Nth point.
        raises if N not in the range [1,NbPoints()]
        """

    def Type(self, N: int) -> LProp_CIType:
        """
        Returns
        - MinCur if the Nth parameter corresponds to
        a minimum of the radius of curvature.
        - MaxCur if the Nth parameter corresponds to
        a maximum of the radius of curvature.
        - Inflection if the parameter corresponds to
        a point of inflection.
        raises if N not in the range [1,NbPoints()]
        """

class LProp_SLProps3d:
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
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, N: int, Resolution: float) -> None:
        """
        idem as previous constructor but without setting the value
        of parameters <U> and <V>.
        """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, U: float, V: float, N: int, Resolution: float) -> None:
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
    def __init__(self, theOther: LProp_SLProps3d) -> None: ...

    def SetSurface(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
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
