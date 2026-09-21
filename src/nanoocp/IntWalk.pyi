"""OCCT package IntWalk (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.IntImp
import nanoocp.IntSurf
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math
import nanoocp.IntWalk


class IntWalk_StatusDeflection(enum.IntEnum):
    IntWalk_PasTropGrand = 0

    IntWalk_StepTooSmall = 1

    IntWalk_PointConfondu = 2

    IntWalk_ArretSurPointPrecedent = 3

    IntWalk_ArretSurPoint = 4

    IntWalk_OK = 5

IntWalk_PasTropGrand: IntWalk_StatusDeflection = IntWalk_StatusDeflection.IntWalk_PasTropGrand

IntWalk_StepTooSmall: IntWalk_StatusDeflection = IntWalk_StatusDeflection.IntWalk_StepTooSmall

IntWalk_PointConfondu: IntWalk_StatusDeflection = IntWalk_StatusDeflection.IntWalk_PointConfondu

IntWalk_ArretSurPointPrecedent: IntWalk_StatusDeflection = ...

IntWalk_ArretSurPoint: IntWalk_StatusDeflection = IntWalk_StatusDeflection.IntWalk_ArretSurPoint

IntWalk_OK: IntWalk_StatusDeflection = IntWalk_StatusDeflection.IntWalk_OK

class IntWalk_TheFunctionOfTheInt2S(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def __init__(self, theOther: IntWalk_TheFunctionOfTheInt2S) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def ComputeParameters(self, ChoixIso: nanoocp.IntImp.IntImp_ConstIsoparametric, Param: nanoocp.NCollection.NCollection_Array1[float], UVap: nanoocp.math.math_Vector, BornInf: nanoocp.math.math_Vector, BornSup: nanoocp.math.math_Vector, Tolerance: nanoocp.math.math_Vector) -> None: ...

    def Root(self) -> float:
        """returns somme des fi*fi"""

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangent(self, UVap: nanoocp.math.math_Vector, Param: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[bool, nanoocp.IntImp.IntImp_ConstIsoparametric]: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def DirectionOnS1(self) -> nanoocp.gp.gp_Dir2d: ...

    def DirectionOnS2(self) -> nanoocp.gp.gp_Dir2d: ...

    def AuxillarSurface1(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def AuxillarSurface2(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

class IntWalk_TheInt2S:
    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TolTangency: float) -> None:
        """
        initialize the parameters to compute the solution point
        it 's possible to write to optimize:
        IntImp_Int2S inter(S1,S2,Func,TolTangency);
        math_FunctionSetRoot rsnld(inter.Function());
        while ...{
        Param(1)=...
        Param(2)=...
        param(3)=...
        inter.Perform(Param,rsnld);
        }
        """

    @overload
    def __init__(self, Param: nanoocp.NCollection.NCollection_Array1[float], S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TolTangency: float) -> None:
        """compute the solution point with the close point"""

    @overload
    def __init__(self, theOther: IntWalk_TheInt2S) -> None: ...

    @overload
    def Perform(self, Param: nanoocp.NCollection.NCollection_Array1[float], Rsnld: nanoocp.math.math_FunctionSetRoot) -> nanoocp.IntImp.IntImp_ConstIsoparametric:
        """
        returns the best constant isoparametric to find
        the next intersection's point +stores the solution
        point (the solution point is found with the close point
        to intersect the isoparametric with the other patch;
        the choice of the isoparametic is calculated)
        """

    @overload
    def Perform(self, Param: nanoocp.NCollection.NCollection_Array1[float], Rsnld: nanoocp.math.math_FunctionSetRoot, ChoixIso: nanoocp.IntImp.IntImp_ConstIsoparametric) -> nanoocp.IntImp.IntImp_ConstIsoparametric:
        """
        returns the best constant isoparametric to find
        the next intersection's point +stores the solution
        point (the solution point is found with the close point
        to intersect the isoparametric with the other patch;
        the choice of the isoparametic is given by ChoixIso)
        """

    def IsDone(self) -> bool:
        """Returns TRUE if the creation completed without failure."""

    def IsEmpty(self) -> bool:
        """Returns TRUE when there is no solution to the problem."""

    def Point(self) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """Returns the intersection point."""

    def IsTangent(self) -> bool:
        """
        Returns True if the surfaces are tangent at the
        intersection point.
        """

    def Direction(self) -> nanoocp.gp.gp_Dir:
        """Returns the tangent at the intersection line."""

    def DirectionOnS1(self) -> nanoocp.gp.gp_Dir2d:
        """
        Returns the tangent at the intersection line in the
        parametric space of the first surface.
        """

    def DirectionOnS2(self) -> nanoocp.gp.gp_Dir2d:
        """
        Returns the tangent at the intersection line in the
        parametric space of the second surface.
        """

    def Function(self) -> IntWalk_TheFunctionOfTheInt2S:
        """
        return the math function which
        is used to compute the intersection
        """

    def ChangePoint(self) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """
        return the intersection point which is
        enable for changing.
        """

class IntWalk_PWalking:
    """
    This class implements an algorithm to determine the
    intersection between 2 parametrized surfaces, marching from
    a starting point. The intersection line
    starts and ends on the natural surface's boundaries.
    """

    @overload
    def __init__(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None:
        """
        Constructor used to set the data to compute intersection
        lines between Caro1 and Caro2.
        Deflection is the maximum deflection admitted between two
        consecutive points on the resulting polyline.
        TolTangency is the tolerance to find a tangent point.
        Func is the criterion which has to be evaluated at each
        solution point (each point of the line).
        It is necessary to call the Perform method to compute
        the intersection lines.
        The line found starts at a point on or in 2 natural domains
        of surfaces. It can be closed in the
        standard case if it is open it stops and begins at the
        border of one of the domains. If an open line
        stops at the middle of a domain, one stops at the tangent point.
        Epsilon is SquareTolerance of points confusion.
        """

    @overload
    def __init__(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float, U1: float, V1: float, U2: float, V2: float) -> None:
        """
        Returns the intersection line containing the exact
        point Poin. This line is a polygonal line.
        Deflection is the maximum deflection admitted between two
        consecutive points on the resulting polyline.
        TolTangency is the tolerance to find a tangent point.
        Func is the criterion which has to be evaluated at each
        solution point (each point of the line).
        The line found starts at a point on or in 2 natural domains
        of surfaces. It can be closed in the
        standard case if it is open it stops and begins at the
        border of one of the domains. If an open line
        stops at the middle of a domain, one stops at the tangent point.
        Epsilon is SquareTolerance of points confusion.
        """

    @overload
    def __init__(self, theOther: IntWalk_PWalking) -> None: ...

    @overload
    def Perform(self, ParDep: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """calculate the line of intersection"""

    @overload
    def Perform(self, ParDep: nanoocp.NCollection.NCollection_Array1[float], u1min: float, v1min: float, u2min: float, v2min: float, u1max: float, v1max: float, u2max: float, v2max: float) -> None:
        """
        calculate the line of intersection. The regulation
        of steps is done using min and max values on u and
        v. (if this data is not presented as in the
        previous method, the initial steps are calculated
        starting from min and max uv of faces).
        """

    def PerformFirstPoint(self, ParDep: nanoocp.NCollection.NCollection_Array1[float], FirstPoint: nanoocp.IntSurf.IntSurf_PntOn2S) -> bool:
        """calculate the first point of a line of intersection"""

    def IsDone(self) -> bool:
        """Returns true if the calculus was successful."""

    def NbPoints(self) -> int:
        """
        Returns the number of points of the resulting polyline.
        An exception is raised if IsDone returns False.
        """

    def Value(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """
        Returns the point of range Index on the polyline.
        An exception is raised if IsDone returns False.
        An exception is raised if Index<=0 or Index>NbPoints.
        """

    def Line(self) -> nanoocp.IntSurf.IntSurf_LineOn2S: ...

    def TangentAtFirst(self) -> bool:
        """
        Returns True if the surface are tangent at the first point
        of the line.
        An exception is raised if IsDone returns False.
        """

    def TangentAtLast(self) -> bool:
        """
        Returns true if the surface are tangent at the last point
        of the line.
        An exception is raised if IsDone returns False.
        """

    def IsClosed(self) -> bool:
        """
        Returns True if the line is closed.
        An exception is raised if IsDone returns False.
        """

    def TangentAtLine(self) -> tuple[nanoocp.gp.gp_Dir, int]: ...

    def TestDeflection(self, ChoixIso: nanoocp.IntImp.IntImp_ConstIsoparametric, theStatus: IntWalk_StatusDeflection) -> IntWalk_StatusDeflection: ...

    def TestArret(self, DejaReparti: bool, Param: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[bool, nanoocp.IntImp.IntImp_ConstIsoparametric]: ...

    def RepartirOuDiviser(self) -> tuple[bool, nanoocp.IntImp.IntImp_ConstIsoparametric, bool]: ...

    def AddAPoint(self, thePOn2S: nanoocp.IntSurf.IntSurf_PntOn2S) -> None:
        """Inserts thePOn2S in the end of line"""

    def RemoveAPoint(self, theIndex: int) -> None:
        """
        Removes point with index theIndex from line.
        If theIndex is greater than the number of points in line
        then the last point will be removed.
        theIndex must be started with 1.
        """

    def PutToBoundary(self, theASurf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theASurf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> bool: ...

    def SeekAdditionalPoints(self, theASurf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theASurf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theMinNbPoints: int) -> bool: ...

    def MaxStep(self, theIndex: int) -> float: ...

class IntWalk_WalkingData:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntWalk_WalkingData) -> None: ...

    @property
    def ustart(self) -> float: ...

    @ustart.setter
    def ustart(self, arg: float, /) -> None: ...

    @property
    def vstart(self) -> float: ...

    @vstart.setter
    def vstart(self, arg: float, /) -> None: ...

    @property
    def etat(self) -> int: ...

    @etat.setter
    def etat(self, arg: int, /) -> None: ...

# C++ typedef aliases
IntWalk_VectorOfInteger = nanoocp.NCollection.NCollection_LinearVector[int]
IntWalk_VectorOfWalkingData = nanoocp.NCollection.NCollection_LinearVector[nanoocp.IntWalk.IntWalk_WalkingData]
