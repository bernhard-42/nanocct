"""OCCT package BlendFunc (toolkit TKFillet)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.Blend
import nanoocp.Convert
import nanoocp.GeomAbs
import nanoocp.Law
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class BlendFunc_SectionShape(enum.IntEnum):
    BlendFunc_Rational = 0

    BlendFunc_QuasiAngular = 1

    BlendFunc_Polynomial = 2

    BlendFunc_Linear = 3

BlendFunc_Rational: BlendFunc_SectionShape = BlendFunc_SectionShape.BlendFunc_Rational

BlendFunc_QuasiAngular: BlendFunc_SectionShape = BlendFunc_SectionShape.BlendFunc_QuasiAngular

BlendFunc_Polynomial: BlendFunc_SectionShape = BlendFunc_SectionShape.BlendFunc_Polynomial

BlendFunc_Linear: BlendFunc_SectionShape = BlendFunc_SectionShape.BlendFunc_Linear

class BlendFunc:
    """
    This package provides a set of generic functions, that can
    instantiated to compute blendings between two surfaces
    (Constant radius, Evolutive radius, Ruled surface).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc) -> None: ...

    @staticmethod
    def GetShape(SectShape: BlendFunc_SectionShape, MaxAng: float) -> tuple[int, int, int, nanoocp.Convert.Convert_ParameterisationType]: ...

    @staticmethod
    def GetMinimalWeights(SectShape: BlendFunc_SectionShape, TConv: nanoocp.Convert.Convert_ParameterisationType, AngleMin: float, AngleMax: float, Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def NextShape(S: nanoocp.GeomAbs.GeomAbs_Shape) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Used to obtain the next level of continuity."""

    @staticmethod
    def ComputeNormal(Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, p2d: nanoocp.gp.gp_Pnt2d, Normal: nanoocp.gp.gp_Vec) -> bool: ...

    @staticmethod
    def ComputeDNormal(Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, p2d: nanoocp.gp.gp_Pnt2d, Normal: nanoocp.gp.gp_Vec, DNu: nanoocp.gp.gp_Vec, DNv: nanoocp.gp.gp_Vec) -> bool: ...

class BlendFunc_GenChamfer(nanoocp.Blend.Blend_Function):
    """Deferred class for a function used to compute a general chamfer"""

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

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
    def Set(self, Dist1: float, Dist2: float, Choix: int) -> None:
        """Sets the distances and the "quadrant"."""

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

    def GetMinimalDistance(self) -> float:
        """
        Returns the minimal Distance between two
        extremities of calculated sections.
        """

    def IsRational(self) -> bool:
        """Returns False"""

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
    def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: nanoocp.gp.gp_Lin) -> tuple[float, float]:
        """Obsolete method"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BlendFunc_GenChamfInv(nanoocp.Blend.Blend_FuncInv):
    """
    Deferred class for a function used to compute a general chamfer on a surface's boundary
    """

    @overload
    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Dist1: float, Dist2: float, Choix: int) -> None: ...

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

class BlendFunc_Corde:
    """
    This function calculates point (pts) on the curve of
    intersection between the normal to a curve (guide)
    in a chosen parameter and a surface (surf), so
    that pts was at a given distance from the guide.
    X(1),X(2) are the parameters U,V of pts on surf.
    """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_Corde) -> None: ...

    def SetParam(self, Param: float) -> None: ...

    def SetDist(self, Dist: float) -> None: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Function for the
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

    def PointOnS(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnGuide(self) -> nanoocp.gp.gp_Pnt:
        """returns the point of parameter <Param> on CGuide"""

    def NPlan(self) -> nanoocp.gp.gp_Vec:
        """returns the normal to CGuide at Ptgui."""

    def IsTangencyPoint(self) -> bool:
        """
        Returns True when it is not possible to compute
        the tangent vectors at PointOnS.
        """

    def TangentOnS(self) -> nanoocp.gp.gp_Vec:
        """Returns the tangent vector at PointOnS, in 3d space."""

    def Tangent2dOnS(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent vector at PointOnS, in the
        parametric space of the first surface.
        """

    def DerFguide(self, Sol: nanoocp.math.math_Vector, DerF: nanoocp.gp.gp_Vec2d) -> None:
        """
        Derived of the function compared to the parameter
        of the guideline
        """

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool:
        """
        Returns False if Sol is not solution else returns
        True and updates the fields tgs and tg2d
        """

class BlendFunc_Chamfer(BlendFunc_GenChamfer):
    """
    Class for a function used to compute a "ordinary" chamfer:
    when distances from spine to surfaces are constant
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, CG: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_Chamfer) -> None: ...

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

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, Dist1: float, Dist2: float, Choix: int) -> None:
        """Sets the distances and the "quadrant"."""

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

    def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: nanoocp.gp.gp_Vec, TgLast: nanoocp.gp.gp_Vec, NormFirst: nanoocp.gp.gp_Vec, NormLast: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surfaces) at
        these points.
        """

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

class BlendFunc_ChamfInv(BlendFunc_GenChamfInv):
    """
    Class for a function used to compute a chamfer with two constant distances
    on a surface's boundary
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ChamfInv) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

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

    @overload
    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """
        Sets the CurveOnSurface on which a solution has
        to be found. If <OnFirst> is set to true,
        the curve will be on the first surface, otherwise the
        curve is on the second one.
        """

    @overload
    def Set(self, Dist1: float, Dist2: float, Choix: int) -> None: ...

class BlendFunc_ChAsym(nanoocp.Blend.Blend_Function):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ChAsym) -> None: ...

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None: ...

    @overload
    def Set(self, Dist1: float, Angle: float, Choix: int) -> None:
        """Sets the distances and the angle."""

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

    def ComputeValues(self, X: nanoocp.math.math_Vector, DegF: int, DegL: int) -> bool:
        """
        computes the values <F> of the derivatives for the
        variable <X> between DegF and DegL.
        Returns True if the computation was done successfully,
        False otherwise.
        """

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

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

    def TwistOnS1(self) -> bool: ...

    def TwistOnS2(self) -> bool: ...

    def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: nanoocp.gp.gp_Vec, TgLast: nanoocp.gp.gp_Vec, NormFirst: nanoocp.gp.gp_Vec, NormLast: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surfaces) at
        these points.
        """

    @overload
    def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: nanoocp.gp.gp_Lin) -> tuple[float, float]:
        """Utile pour une visu rapide et approximative de la surface."""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

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

class BlendFunc_ChAsymInv(nanoocp.Blend.Blend_FuncInv):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ChAsymInv) -> None: ...

    @overload
    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Dist1: float, Angle: float, Choix: int) -> None: ...

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    def ComputeValues(self, X: nanoocp.math.math_Vector, DegF: int, DegL: int) -> bool:
        """
        computes the values <F> of the derivatives for the
        variable <X> between DegF and DegL.
        Returns True if the computation was done successfully,
        False otherwise.
        """

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

class BlendFunc_Tensor:
    """used to store the "gradient of gradient\""""

    @overload
    def __init__(self, NbRow: int, NbCol: int, NbMat: int) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_Tensor) -> None: ...

    def Init(self, InitialValue: float) -> None:
        """Initialize all the elements of a Tensor to InitialValue."""

    def Value(self, Row: int, Col: int, Mat: int) -> float:
        """
        accesses (in read or write mode) the value of index <Row>,
        <Col> and <Mat> of a Tensor.
        An exception is raised if <Row>, <Col> or <Mat> are not
        in the correct range.
        """

    def ChangeValue(self, Row: int, Col: int, Mat: int) -> float:
        """
        accesses (in read or write mode) the value of index <Row>,
        <Col> and <Mat> of a Tensor.
        An exception is raised if <Row>, <Col> or <Mat> are not
        in the correct range.
        """

    def SetValue(self, Row: int, Col: int, Mat: int, theValue: float) -> None:
        """
        Python addition: sets the value ChangeValue(Row, Col, Mat) returns by reference in C++.
        """

    def __call__(self, Row: int, Col: int, Mat: int) -> float: ...

    def __getitem__(self, arg: tuple[int, int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(Row, Col, Mat) returns by reference in C++.
        """

    def Multiply(self, Right: nanoocp.math.math_Vector, Product: nanoocp.math.math_Matrix) -> None: ...

class BlendFunc_ConstRad(nanoocp.Blend.Blend_Function):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ConstRad) -> None: ...

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
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None: ...

    @overload
    def Set(self, Radius: float, Choix: int) -> None:
        """Inits the value of radius, and the "quadrant"."""

    @overload
    def Set(self, TypeSection: BlendFunc_SectionShape) -> None:
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

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

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
    def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]:
        """Useful for a quick and approximate visualization of the surface area."""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

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

    def AxeRot(self, Prm: float) -> nanoocp.gp.gp_Ax1: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BlendFunc_ConstRadInv(nanoocp.Blend.Blend_FuncInv):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ConstRadInv) -> None: ...

    @overload
    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, R: float, Choix: int) -> None: ...

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

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

class BlendFunc_CSCircular(nanoocp.Blend.Blend_CSFunction):
    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None, L: nanoocp.Law.Law_Function | None) -> None:
        """
        Creates a function for a circular blending between
        a curve <C> and a surface <S>. The direction of
        the planes are given by <CGuide>. The position of
        the plane is determined on the curve <C>. <L>
        defines the change of parameter between <C> and
        <CGuide>. So, the planes are defined as described
        below:
        t is the current parameter on the guide line.
        Pguide = C(L(t)); Nguide = CGuide'(t)/||CGuide'(t)||
        """

    @overload
    def __init__(self, theOther: BlendFunc_CSCircular) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int:
        """returns the number of equations of the function (3)."""

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
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None: ...

    @overload
    def Set(self, Radius: float, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: BlendFunc_SectionShape) -> None:
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

    def PointOnS(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnC(self) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2d(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def ParameterOnC(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2d(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnC(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent(self, U: float, V: float, TgS: nanoocp.gp.gp_Vec, NormS: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surface) at
        these points.
        """

    @overload
    def Section(self, Param: float, U: float, V: float, W: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def GetSection(self, Param: float, U: float, V: float, W: float, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool: ...

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

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BlendFunc_CSConstRad(nanoocp.Blend.Blend_CSFunction):
    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, CGuide: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_CSConstRad) -> None: ...

    def NbEquations(self) -> int:
        """returns the number of equations of the function (3)."""

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
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None: ...

    @overload
    def Set(self, Radius: float, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: BlendFunc_SectionShape) -> None:
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

    def PointOnS(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnC(self) -> nanoocp.gp.gp_Pnt: ...

    def Pnt2d(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns U,V coordinates of the point on the surface."""

    def ParameterOnC(self) -> float:
        """Returns parameter of the point on the curve."""

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2d(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnC(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent(self, U: float, V: float, TgS: nanoocp.gp.gp_Vec, NormS: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surface) at
        these points.
        """

    @overload
    def Section(self, Param: float, U: float, V: float, W: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Used for the first and last section
        The method returns true if the derivatives
        are computed, otherwise it returns false.
        """

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def GetSection(self, Param: float, U: float, V: float, W: float, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool: ...

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

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BlendFunc_EvolRad(nanoocp.Blend.Blend_Function):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Law: nanoocp.Law.Law_Function | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_EvolRad) -> None: ...

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
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None: ...

    @overload
    def Set(self, Choix: int) -> None: ...

    @overload
    def Set(self, TypeSection: BlendFunc_SectionShape) -> None:
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

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

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
    def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: nanoocp.gp.gp_Circ) -> tuple[float, float]:
        """Method for graphic traces"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

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

class BlendFunc_EvolRadInv(nanoocp.Blend.Blend_FuncInv):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Law: nanoocp.Law.Law_Function | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_EvolRadInv) -> None: ...

    @overload
    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, Choix: int) -> None: ...

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

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

class BlendFunc_Ruled(nanoocp.Blend.Blend_Function):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_Ruled) -> None: ...

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
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, First: float, Last: float) -> None: ...

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

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

    def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: nanoocp.gp.gp_Vec, TgLast: nanoocp.gp.gp_Vec, NormFirst: nanoocp.gp.gp_Vec, NormLast: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surfaces) at
        these points.
        """

    def GetSection(self, Param: float, U1: float, V1: float, U2: float, V2: float, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabV: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool: ...

    def IsRational(self) -> bool:
        """Returns False"""

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
        raises OutOfRange from Standard
        """

    def GetShape(self) -> tuple[int, int, int, int]: ...

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Mults(self, TMults: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], D2Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], D2Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float], D2Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool: ...

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DPoles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DPoles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], Weigths: nanoocp.NCollection.NCollection_Array1[float], DWeigths: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """Used for the first and last section"""

    @overload
    def Section(self, P: nanoocp.Blend.Blend_Point, Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Poles2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weigths: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def AxeRot(self, Prm: float) -> nanoocp.gp.gp_Ax1: ...

    def Resolution(self, IC2d: int, Tol: float) -> tuple[float, float]: ...

class BlendFunc_RuledInv(nanoocp.Blend.Blend_FuncInv):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_RuledInv) -> None: ...

    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def GetTolerance(self, Tolerance: nanoocp.math.math_Vector, Tol: float) -> None: ...

    def GetBounds(self, InfBound: nanoocp.math.math_Vector, SupBound: nanoocp.math.math_Vector) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

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

class BlendFunc_ConstThroat(BlendFunc_GenChamfer):
    """
    Class for a function used to compute a symmetric chamfer
    with constant throat that is the height of isosceles triangle in section
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ConstThroat) -> None: ...

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

    @overload
    def Set(self, Param: float) -> None: ...

    @overload
    def Set(self, aThroat: float, arg1: float, Choix: int) -> None:
        """Sets the throat and the "quadrant"."""

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def PointOnS1(self) -> nanoocp.gp.gp_Pnt: ...

    def PointOnS2(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangencyPoint(self) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

    def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: nanoocp.gp.gp_Vec, TgLast: nanoocp.gp.gp_Vec, NormFirst: nanoocp.gp.gp_Vec, NormLast: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the tangent vector at the section,
        at the beginning and the end of the section, and
        returns the normal (of the surfaces) at
        these points.
        """

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

class BlendFunc_ConstThroatInv(BlendFunc_GenChamfInv):
    """
    Class for a function used to compute a ConstThroat chamfer on a surface's boundary
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ConstThroatInv) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

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

    @overload
    def Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """
        Sets the CurveOnSurface on which a solution has
        to be found. If <OnFirst> is set to true,
        the curve will be on the first surface, otherwise the
        curve is on the second one.
        """

    @overload
    def Set(self, theThroat: float, arg1: float, Choix: int) -> None: ...

class BlendFunc_ConstThroatWithPenetration(BlendFunc_ConstThroat):
    """
    Class for a function used to compute a chamfer with constant throat:
    the section of chamfer is right-angled triangle,
    the first of two surfaces (where is the top of the chamfer)
    is virtually moved inside the solid by offset operation,
    the apex of the section is on the intersection curve between moved surface and second surface,
    right angle is at the top of the chamfer,
    the length of the leg from apex to top is constant - it is throat
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ConstThroatWithPenetration) -> None: ...

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

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

    def TangentOnS1(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS1(self) -> nanoocp.gp.gp_Vec2d: ...

    def TangentOnS2(self) -> nanoocp.gp.gp_Vec: ...

    def Tangent2dOnS2(self) -> nanoocp.gp.gp_Vec2d: ...

    def GetSectionSize(self) -> float:
        """Returns the length of the maximum section"""

class BlendFunc_ConstThroatWithPenetrationInv(BlendFunc_ConstThroatInv):
    """
    Class for a function used to compute a ConstThroatWithPenetration chamfer
    on a surface's boundary
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BlendFunc_ConstThroatWithPenetrationInv) -> None: ...

    def IsSolution(self, Sol: nanoocp.math.math_Vector, Tol: float) -> bool: ...

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
