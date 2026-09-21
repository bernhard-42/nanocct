"""OCCT package Blend (toolkit TKFillet)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class Blend_DecrochStatus(enum.IntEnum):
    Blend_NoDecroch = 0

    Blend_DecrochRst1 = 1

    Blend_DecrochRst2 = 2

    Blend_DecrochBoth = 3

Blend_NoDecroch: Blend_DecrochStatus = Blend_DecrochStatus.Blend_NoDecroch

Blend_DecrochRst1: Blend_DecrochStatus = Blend_DecrochStatus.Blend_DecrochRst1

Blend_DecrochRst2: Blend_DecrochStatus = Blend_DecrochStatus.Blend_DecrochRst2

Blend_DecrochBoth: Blend_DecrochStatus = Blend_DecrochStatus.Blend_DecrochBoth

class Blend_Status(enum.IntEnum):
    Blend_StepTooLarge = 0

    Blend_StepTooSmall = 1

    Blend_Backward = 2

    Blend_SamePoints = 3

    Blend_OnRst1 = 4

    Blend_OnRst2 = 5

    Blend_OnRst12 = 6

    Blend_OK = 7

Blend_StepTooLarge: Blend_Status = Blend_Status.Blend_StepTooLarge

Blend_StepTooSmall: Blend_Status = Blend_Status.Blend_StepTooSmall

Blend_Backward: Blend_Status = Blend_Status.Blend_Backward

Blend_SamePoints: Blend_Status = Blend_Status.Blend_SamePoints

Blend_OnRst1: Blend_Status = Blend_Status.Blend_OnRst1

Blend_OnRst2: Blend_Status = Blend_Status.Blend_OnRst2

Blend_OnRst12: Blend_Status = Blend_Status.Blend_OnRst12

Blend_OK: Blend_Status = Blend_Status.Blend_OK

class Blend_AppFunction(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Deferred class for a function used to compute a blending
    surface between two surfaces, using a guide line.
    The vector <X> used in Value, Values and Derivatives methods
    has to be the vector of the parametric coordinates U1,V1,
    U2,V2, of the extremities of a section on the first and
    second surface.
    """

    def NbVariables(self) -> int:
        """returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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
    def Set(self, Param: float) -> None:
        """
        Sets the value of the parameter along the guide line.
        This determines the plane in which the solution has
        to be found.
        """

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 4 variables;
        Tol is the tolerance used in 3d space.
        """

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 4 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 4 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        The computation is made at the current value of
        the parameter on the guide line.
        """

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def Pnt1(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the first support."""

    def Pnt2(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the first support."""

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
        raises
        OutOfRange from Standard
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

    def Parameter(self, P: Blend_Point) -> float:
        """
        Returns the parameter of the point P. Used to
        impose the parameters in the approximation.
        """

class Blend_CSFunction(Blend_AppFunction):
    """
    Deferred class for a function used to compute a blending
    surface between a surface and a curve, using a guide line.
    The vector <X> used in Value, Values and Derivatives methods
    may be the vector of the parametric coordinates U,V,
    W of the extremities of a section on the surface and
    the curve.
    """

    def NbVariables(self) -> int:
        """Returns 3 (default value). Can be redefined."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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
    def Set(self, Param: float) -> None:
        """
        Sets the value of the parameter along the guide line.
        This determines the plane in which the solution has
        to be found.
        """

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 3 variables;
        Tol is the tolerance used in 3d space.
        """

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
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
        The computation is made at the current value of
        the parameter on the guide line.
        """

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def Pnt1(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the first support."""

    def Pnt2(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the second support."""

    def PointOnS(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the surface."""

    def PointOnC(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the curve."""

    def Pnt2d(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def ParameterOnC(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool:
        """
        Returns True when it is not possible to compute
        the tangent vectors at PointOnS and/or PointOnC.
        """

    def TangentOnS(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnS, in 3d space."""

    def Tangent2d(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnS, in the
        parametric space of the first surface.
        """

    def TangentOnC(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnC, in 3d space."""

    def Tangent(self, U: float, V: float, TgS: nanoocp.gp.gp_Vec, NormS: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surfaces) at
        these points.
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

class Blend_CurvPointFuncInv(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Deferred class for a function used to compute a
    blending surface between a surface and a curve, using
    a guide line. This function is used to find a
    solution on a done point of the curve.
    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates w, U, V where w is the parameter on the
    guide line, U,V are the parametric coordinates of a
    point on the partner surface.
    """

    def NbVariables(self) -> int:
        """Returns 3."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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

    def Set(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Set the Point on which a solution has to be found."""

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

class Blend_FuncInv(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Deferred class for a function used to compute a blending
    surface between two surfaces, using a guide line.
    This function is used to find a solution on a restriction
    of one of the surface.
    The vector <X> used in Value, Values and Derivatives methods
    has to be the vector of the parametric coordinates t,w,U,V
    where t is the parameter on the curve on surface,
    w is the parameter on the guide line,
    U,V are the parametric coordinates of a point on the
    partner surface.
    """

    def NbVariables(self) -> int:
        """Returns 4."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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

    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """
        Sets the CurveOnSurface on which a solution has
        to be found. If <OnFirst> is set to true,
        the curve will be on the first surface, otherwise the
        curve is on the second one.
        """

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each of the 4 variables;
        Tol is the tolerance used in 3d space.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each of the 4 variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 4 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        """

class Blend_Function(Blend_AppFunction):
    """
    Deferred class for a function used to compute a blending
    surface between two surfaces, using a guide line.
    The vector <X> used in Value, Values and Derivatives methods
    has to be the vector of the parametric coordinates U1,V1,
    U2,V2, of the extremities of a section on the first and
    second surface.
    """

    def NbVariables(self) -> int:
        """Returns 4."""

    def Pnt1(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the first support."""

    def Pnt2(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the second support."""

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point on the first surface, at parameter
        Sol(1),Sol(2) (Sol is the vector used in the call of
        IsSolution.
        """

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point on the second surface, at parameter
        Sol(3),Sol(4) (Sol is the vector used in the call of
        IsSolution.
        """

    def IsTangencyPoint(self) -> bool:
        """
        Returns True when it is not possible to compute
        the tangent vectors at PointOnS1 and/or PointOnS2.
        """

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnS1, in 3d space."""

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnS1, in the
        parametric space of the first surface.
        """

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnS2, in 3d space."""

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnS2, in the
        parametric space of the second surface.
        """

    def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: nanoocp.gp.gp_Vec, TgLast: nanoocp.gp.gp_Vec, NormFirst: nanoocp.gp.gp_Vec, NormLast: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surfaces) at
        these points.
        """

    def TwistOnS1(self) -> bool: ...

    def TwistOnS2(self) -> bool: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false
        """

class Blend_Point:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Pts: nanoocp.gp.gp_Pnt, Ptc: nanoocp.gp.gp_Pnt, Param: float, U: float, V: float, W: float) -> None:
        """Creates a point on a surface and a curve, without tangents."""

    @overload
    def __init__(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float) -> None:
        """Creates a point on 2 surfaces, without tangents."""

    @overload
    def __init__(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float) -> None:
        """
        Creates a point on a surface and a curve on surface,
        without tangents.
        """

    @overload
    def __init__(self, Pts: nanoocp.gp.gp_Pnt, Ptc: nanoocp.gp.gp_Pnt, Param: float, U: float, V: float, W: float, Tgs: nanoocp.gp.gp_Vec, Tgc: nanoocp.gp.gp_Vec, Tg2d: nanoocp.gp.gp_Vec2d) -> None:
        """Creates a point on a surface and a curve, with tangents."""

    @overload
    def __init__(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float) -> None: ...

    @overload
    def __init__(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, Tg1: nanoocp.gp.gp_Vec, Tg2: nanoocp.gp.gp_Vec, Tg12d: nanoocp.gp.gp_Vec2d, Tg22d: nanoocp.gp.gp_Vec2d) -> None:
        """Creates a point on 2 surfaces, with tangents."""

    @overload
    def __init__(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float, Tg1: nanoocp.gp.gp_Vec, Tg2: nanoocp.gp.gp_Vec, Tg12d: nanoocp.gp.gp_Vec2d, Tg22d: nanoocp.gp.gp_Vec2d) -> None:
        """
        Creates a point on a surface and a curve on surface,
        with tangents.
        """

    @overload
    def __init__(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float, Tg1: nanoocp.gp.gp_Vec, Tg2: nanoocp.gp.gp_Vec, Tg12d: nanoocp.gp.gp_Vec2d, Tg22d: nanoocp.gp.gp_Vec2d) -> None:
        """Creates a point on two curves on surfaces, with tangents."""

    @overload
    def __init__(self, theOther: Blend_Point) -> None: ...

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, Tg1: nanoocp.gp.gp_Vec, Tg2: nanoocp.gp.gp_Vec, Tg12d: nanoocp.gp.gp_Vec2d, Tg22d: nanoocp.gp.gp_Vec2d) -> None:
        """Set the values for a point on 2 surfaces, with tangents."""

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float) -> None:
        """Set the values for a point on 2 surfaces, without tangents."""

    @overload
    def SetValue(self, Pts: nanoocp.gp.gp_Pnt, Ptc: nanoocp.gp.gp_Pnt, Param: float, U: float, V: float, W: float, Tgs: nanoocp.gp.gp_Vec, Tgc: nanoocp.gp.gp_Vec, Tg2d: nanoocp.gp.gp_Vec2d) -> None:
        """
        Set the values for a point on a surface and a curve,
        with tangents.
        """

    @overload
    def SetValue(self, Pts: nanoocp.gp.gp_Pnt, Ptc: nanoocp.gp.gp_Pnt, Param: float, U: float, V: float, W: float) -> None:
        """
        Set the values for a point on a surface and a curve,
        without tangents.
        """

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float, Tg1: nanoocp.gp.gp_Vec, Tg2: nanoocp.gp.gp_Vec, Tg12d: nanoocp.gp.gp_Vec2d, Tg22d: nanoocp.gp.gp_Vec2d) -> None:
        """
        Creates a point on a surface and a curve on surface,
        with tangents.
        """

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float) -> None:
        """
        Creates a point on a surface and a curve on surface,
        without tangents.
        """

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float, Tg1: nanoocp.gp.gp_Vec, Tg2: nanoocp.gp.gp_Vec, Tg12d: nanoocp.gp.gp_Vec2d, Tg22d: nanoocp.gp.gp_Vec2d) -> None:
        """Creates a point on two curves on surfaces, with tangents."""

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float) -> None:
        """Creates a point on two curves on surfaces, without tangents."""

    @overload
    def SetValue(self, Pt1: nanoocp.gp.gp_Pnt, Pt2: nanoocp.gp.gp_Pnt, Param: float, PC1: float, PC2: float) -> None:
        """Creates a point on two curves."""

    def SetParameter(self, Param: float) -> None:
        """Changes parameter on existing point"""

    def Parameter(self) -> float: ...

    def IsTangencyPoint(self) -> bool:
        """
        Returns true if it was not possible to compute
        the tangent vectors at PointOnS1 and/or PointOnS2.
        """

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def ParametersOnS1(self) -> tuple[float, float]: ...

    def ParametersOnS2(self) -> tuple[float, float]: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

    def PointOnS(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnC(self) -> nanoocp.gp.gp_Pnt: ...

    def ParametersOnS(self) -> tuple[float, float]: ...

    def ParameterOnC(self) -> float: ...

    def TangentOnS(self) -> nanoocp.gp.gp_Vec: ...

    def TangentOnC(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2d(self) -> nanoocp.gp.gp_Vec2d: ...

    def PointOnC1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnC2(self) -> nanoocp.gp.gp_Pnt: ...

    def ParameterOnC1(self) -> float: ...

    def ParameterOnC2(self) -> float: ...

    def TangentOnC1(self) -> nanoocp.gp.gp_Vec: ...

    def TangentOnC2(self) -> nanoocp.gp.gp_Vec: ...

class Blend_RstRstFunction(Blend_AppFunction):
    """
    Deferred class for a function used to compute a blending
    surface between a surface and a pcurve on an other Surface,
    using a guide line.
    The vector <X> used in Value, Values and Derivatives methods
    may be the vector of the parametric coordinates U,V,
    W of the extremities of a section on the surface and
    the curve.
    """

    def NbVariables(self) -> int:
        """Returns 2 (default value). Can be redefined."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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
    def Set(self, Param: float) -> None:
        """
        Sets the value of the parameter along the guide line.
        This determines the plane in which the solution has
        to be found.
        """

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each variable;
        Tol is the tolerance used in 3d space.
        """

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each variables.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        The computation is made at the current value of
        the parameter on the guide line.
        """

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def Pnt1(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the first support."""

    def Pnt2(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the second support."""

    def PointOnRst1(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the surface."""

    def PointOnRst2(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the curve."""

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

    def IsTangencyPoint(self) -> bool:
        """
        Returns True when it is not possible to compute
        the tangent vectors at PointOnS and/or PointOnRst.
        """

    def TangentOnRst1(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnS, in 3d space."""

    def Tangent2dOnRst1(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnS, in the
        parametric space of the first surface.
        """

    def TangentOnRst2(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnC, in 3d space."""

    def Tangent2dOnRst2(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnRst, in the
        parametric space of the second surface.
        """

    def Decroch(self, Sol: nanoocp.math.math_Vector, NRst1: nanoocp.gp.gp_Vec, TgRst1: nanoocp.gp.gp_Vec, NRst2: nanoocp.gp.gp_Vec, TgRst2: nanoocp.gp.gp_Vec) -> Blend_DecrochStatus:
        """
        Enables to implement a criterion of decrochage
        specific to the function.
        Warning: Can be called without previous call of IsSolution
        but the values calculated can be senseless.
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

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

class Blend_SurfCurvFuncInv(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Deferred class for a function used to compute a
    blending surface between a surface and a curve, using
    a guide line. This function is used to find a
    solution on a done restriction of the surface.

    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates wguide, wcurv, wrst where wguide is the
    parameter on the guide line, wcurv is the parameter on
    the curve, wrst is the parameter on the restriction on
    the surface.
    """

    def NbVariables(self) -> int:
        """Returns 3."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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

    def Set(self, Rst: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """Set the Point on which a solution has to be found."""

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

class Blend_SurfPointFuncInv(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Deferred class for a function used to compute a
    blending surface between a surface and a curve, using
    a guide line. This function is used to find a
    solution on a done point of the curve.

    The vector <X> used in Value, Values and Derivatives
    methods has to be the vector of the parametric
    coordinates w, U, V where w is the parameter on the
    guide line, U,V are the parametric coordinates of a
    point on the partner surface.
    """

    def NbVariables(self) -> int:
        """Returns 3."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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

    def Set(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Set the Point on which a solution has to be found."""

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

class Blend_SurfRstFunction(Blend_AppFunction):
    """
    Deferred class for a function used to compute a blending
    surface between a surface and a pcurve on an other Surface,
    using a guide line.
    The vector <X> used in Value, Values and Derivatives methods
    may be the vector of the parametric coordinates U,V,
    W of the extremities of a section on the surface and
    the curve.
    """

    def NbVariables(self) -> int:
        """Returns 3 (default value). Can be redefined."""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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
    def Set(self, Param: float) -> None:
        """
        Sets the value of the parameter along the guide line.
        This determines the plane in which the solution has
        to be found.
        """

    @overload
    def Set(self, First: float, Last: float) -> None:
        """
        Sets the bounds of the parametric interval on
        the guide line.
        This determines the derivatives in these values if the
        function is not Cn.
        """

    @overload
    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None:
        """
        Returns in the vector Tolerance the parametric tolerance
        for each variable.
        Tol is the tolerance used in 3d space.
        """

    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: nanoocp.math.math_Vector, Tol1D: nanoocp.math.math_Vector) -> None:
        """
        Returns the tolerance to reach in approximation
        to respect
        BoundTol error at the Boundary
        AngleTol tangent error at the Boundary
        SurfTol error inside the surface.
        """

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None:
        """
        Returns in the vector InfBound the lowest values allowed
        for each variable.
        Returns in the vector SupBound the greatest values allowed
        for each of the 3 variables.
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns true if Sol is a zero of the function.
        Tol is the tolerance used in 3d space.
        The computation is made at the current value of
        the parameter on the guide line.
        """

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def Pnt1(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the first support."""

    def Pnt2(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the second support."""

    def PointOnS(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the surface."""

    def PointOnRst(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point on the curve."""

    def Pnt2dOnS(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def Pnt2dOnRst(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns U,V coordinates of the point on the curve on
        surface.
        """

    def ParameterOnRst(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool:
        """
        Returns True when it is not possible to compute
        the tangent vectors at PointOnS and/or PointOnRst.
        """

    def TangentOnS(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnS, in 3d space."""

    def Tangent2dOnS(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnS, in the
        parametric space of the first surface.
        """

    def TangentOnRst(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnC, in 3d space."""

    def Tangent2dOnRst(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnRst, in the
        parametric space of the second surface.
        """

    def Decroch(self, Sol: nanoocp.math.math_Vector, NS: nanoocp.gp.gp_Vec, TgS: nanoocp.gp.gp_Vec) -> bool:
        """
        Enables implementation of a criterion of decrochage
        specific to the function.
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

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...
