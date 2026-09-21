"""OCCT package IntSurf (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class IntSurf_Situation(enum.IntEnum):
    IntSurf_Inside = 0

    IntSurf_Outside = 1

    IntSurf_Unknown = 2

IntSurf_Inside: IntSurf_Situation = IntSurf_Situation.IntSurf_Inside

IntSurf_Outside: IntSurf_Situation = IntSurf_Situation.IntSurf_Outside

IntSurf_Unknown: IntSurf_Situation = IntSurf_Situation.IntSurf_Unknown

class IntSurf_TypeTrans(enum.IntEnum):
    IntSurf_In = 0

    IntSurf_Out = 1

    IntSurf_Touch = 2

    IntSurf_Undecided = 3

IntSurf_In: IntSurf_TypeTrans = IntSurf_TypeTrans.IntSurf_In

IntSurf_Out: IntSurf_TypeTrans = IntSurf_TypeTrans.IntSurf_Out

IntSurf_Touch: IntSurf_TypeTrans = IntSurf_TypeTrans.IntSurf_Touch

IntSurf_Undecided: IntSurf_TypeTrans = IntSurf_TypeTrans.IntSurf_Undecided

class IntSurf:
    """
    This package provides resources for
    all the packages concerning the intersection
    between surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf) -> None: ...

    @staticmethod
    def MakeTransition(TgFirst: nanoocp.gp.gp_Vec, TgSecond: nanoocp.gp.gp_Vec, Normal: nanoocp.gp.gp_Dir, TFirst: IntSurf_Transition, TSecond: IntSurf_Transition) -> None:
        """
        Computes the transition of the intersection point
        between the two lines.
        TgFirst is the tangent vector of the first line.
        TgSecond is the tangent vector of the second line.
        Normal is the direction used to orientate the cross
        product TgFirst^TgSecond.
        TFirst is the transition of the point on the first line.
        TSecond is the transition of the point on the second line.
        """

    @staticmethod
    def SetPeriod(theFirstSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theSecondSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> list[float]:
        """
        Fills theArrOfPeriod array by the period values of theFirstSurf and theSecondSurf.
        [0] = U-period of theFirstSurf,
        [1] = V-period of theFirstSurf,
        [2] = U-period of theSecondSurf,
        [3] = V-period of theSecondSurf.

        If surface is not periodic in correspond direction then
        its period is considered to be equal to 0.
        """

class IntSurf_Couple:
    """creation d 'un couple de 2 entiers"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Index1: int, Index2: int) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_Couple) -> None: ...

    def First(self) -> int:
        """returns the first element"""

    def Second(self) -> int:
        """returns the Second element"""

class IntSurf_InteriorPoint:
    """
    Definition of a point solution of the
    intersection between an implicit an a
    parametrised surface. These points are
    passing points on the intersection lines,
    or starting points for the closed lines
    on the parametrised surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, U: float, V: float, Direc: nanoocp.gp.gp_Vec, Direc2d: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_InteriorPoint) -> None: ...

    def SetValue(self, P: nanoocp.gp.gp_Pnt, U: float, V: float, Direc: nanoocp.gp.gp_Vec, Direc2d: nanoocp.gp.gp_Vec2d) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the 3d coordinates of the interior point."""

    def Parameters(self) -> tuple[float, float]:
        """
        Returns the parameters of the interior point on the
        parametric surface.
        """

    def UParameter(self) -> float:
        """
        Returns the first parameter of the interior point on the
        parametric surface.
        """

    def VParameter(self) -> float:
        """
        Returns the second parameter of the interior point on the
        parametric surface.
        """

    def Direction(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the tangent at the intersection in 3d space
        associated to the interior point.
        """

    def Direction2d(self) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the tangent at the intersection in the parametric
        space of the parametric surface.
        """

class IntSurf_InteriorPointTool:
    """
    This class provides a tool on the "interior point"
    that can be used to instantiates the Walking
    algorithms (see package IntWalk).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_InteriorPointTool) -> None: ...

    @staticmethod
    def Value3d(PStart: IntSurf_InteriorPoint) -> nanoocp.gp.gp_Pnt:
        """Returns the 3d coordinates of the starting point."""

    @staticmethod
    def Value2d(PStart: IntSurf_InteriorPoint) -> tuple[float, float]:
        """
        Returns the <U,V> parameters which are associated
        with <P>
        it's the parameters which start the marching algorithm
        """

    @staticmethod
    def Direction3d(PStart: IntSurf_InteriorPoint) -> nanoocp.gp.gp_Vec:
        """
        returns the tangent at the intersection in 3d space
        associated to <P>
        """

    @staticmethod
    def Direction2d(PStart: IntSurf_InteriorPoint) -> nanoocp.gp.gp_Dir2d:
        """
        returns the tangent at the intersection in the
        parametric space of the parametrized surface.This tangent
        is associated to the value2d
        """

class IntSurf_PntOn2S:
    """
    This class defines the geometric information
    for an intersection point between 2 surfaces :
    The coordinates ( Pnt from gp ), and two
    parametric coordinates.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: IntSurf_PntOn2S) -> None: ...

    @overload
    def SetValue(self, Pt: nanoocp.gp.gp_Pnt) -> None:
        """Sets the value of the point in 3d space."""

    @overload
    def SetValue(self, Pt: nanoocp.gp.gp_Pnt, OnFirst: bool, U: float, V: float) -> None:
        """
        Sets the values of the point in 3d space, and
        in the parametric space of one of the surface.
        """

    @overload
    def SetValue(self, Pt: nanoocp.gp.gp_Pnt, U1: float, V1: float, U2: float, V2: float) -> None:
        """
        Sets the values of the point in 3d space, and
        in the parametric space of each surface.
        """

    @overload
    def SetValue(self, OnFirst: bool, U: float, V: float) -> None: ...

    @overload
    def SetValue(self, U1: float, V1: float, U2: float, V2: float) -> None:
        """
        Set the values of the point in the parametric
        space of one of the surface.
        """

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point in 3d space."""

    def ValueOnSurface(self, OnFirst: bool) -> nanoocp.gp.gp_Pnt2d:
        """Returns the point in 2d space of one of the surfaces."""

    def ParametersOnS1(self) -> tuple[float, float]:
        """Returns the parameters of the point on the first surface."""

    def ParametersOnS2(self) -> tuple[float, float]:
        """Returns the parameters of the point on the second surface."""

    def ParametersOnSurface(self, OnFirst: bool) -> tuple[float, float]:
        """
        Returns the parameters of the point in the
        parametric space of one of the surface.
        """

    def Parameters(self) -> tuple[float, float, float, float]:
        """Returns the parameters of the point on both surfaces."""

    def IsSame(self, theOtherPoint: IntSurf_PntOn2S, theTol3D: float = 0.0, theTol2D: float = -1.0) -> bool:
        """
        Returns TRUE if 2D- and 3D-coordinates of theOterPoint are equal to
        corresponding coordinates of me (with given tolerance).
        If theTol2D < 0.0 we will compare 3D-points only.
        """

class IntSurf_LineOn2S(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None = None) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_LineOn2S) -> None: ...

    def Add(self, P: IntSurf_PntOn2S) -> None:
        """Adds a point in the line."""

    def NbPoints(self) -> int:
        """Returns the number of points in the line."""

    @overload
    def Value(self, Index: int) -> IntSurf_PntOn2S:
        """Returns the point of range Index in the line."""

    @overload
    def Value(self, Index: int, P: IntSurf_PntOn2S) -> None:
        """Replaces the point of range Index in the line."""

    def Reverse(self) -> None:
        """Reverses the order of points of the line."""

    def Split(self, Index: int) -> IntSurf_LineOn2S:
        """
        Keeps in <me> the points 1 to Index-1, and returns
        the items Index to the end.
        """

    def SetPoint(self, Index: int, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Sets the 3D point of the Index-th PntOn2S"""

    def SetUV(self, Index: int, OnFirst: bool, U: float, V: float) -> None:
        """
        Sets the parametric coordinates on one of the surfaces
        of the point of range Index in the line.
        """

    def Clear(self) -> None: ...

    def InsertBefore(self, I: int, P: IntSurf_PntOn2S) -> None: ...

    def RemovePoint(self, I: int) -> None: ...

    def IsOutSurf1Box(self, theP: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Returns TRUE if theP is out of the box built from
        the points on 1st surface
        """

    def IsOutSurf2Box(self, theP: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Returns TRUE if theP is out of the box built from
        the points on 2nd surface
        """

    def IsOutBox(self, theP: nanoocp.gp.gp_Pnt) -> bool:
        """Returns TRUE if theP is out of the box built from 3D-points."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntSurf_PathPoint:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, U: float, V: float) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_PathPoint) -> None: ...

    def SetValue(self, P: nanoocp.gp.gp_Pnt, U: float, V: float) -> None: ...

    def AddUV(self, U: float, V: float) -> None: ...

    def SetDirections(self, V: nanoocp.gp.gp_Vec, D: nanoocp.gp.gp_Dir2d) -> None: ...

    def SetTangency(self, Tang: bool) -> None: ...

    def SetPassing(self, Pass: bool) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt: ...

    def Value2d(self) -> tuple[float, float]: ...

    def IsPassingPnt(self) -> bool: ...

    def IsTangent(self) -> bool: ...

    def Direction3d(self) -> nanoocp.gp.gp_Vec: ...

    def Direction2d(self) -> nanoocp.gp.gp_Dir2d: ...

    def Multiplicity(self) -> int: ...

    def Parameters(self, Index: int) -> tuple[float, float]: ...

class IntSurf_PathPointTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_PathPointTool) -> None: ...

    @staticmethod
    def Value3d(PStart: IntSurf_PathPoint) -> nanoocp.gp.gp_Pnt:
        """Returns the 3d coordinates of the starting point."""

    @staticmethod
    def Value2d(PStart: IntSurf_PathPoint) -> tuple[float, float]:
        """
        Returns the <U, V> parameters which are associated
        with <P>
        it's the parameters which start the marching algorithm
        """

    @staticmethod
    def IsPassingPnt(PStart: IntSurf_PathPoint) -> bool:
        """
        Returns True if the point is a point on a non-oriented
        arc, which means that the intersection line does not
        stop at such a point but just go through such a point.
        IsPassingPnt is True when IsOnArc is True
        """

    @staticmethod
    def IsTangent(PStart: IntSurf_PathPoint) -> bool:
        """
        Returns True if the surfaces are tangent at this point.
        IsTangent can be True when IsOnArc is True
        if IsPassingPnt is True and IsTangent is True,this point
        is a stopped point.
        """

    @staticmethod
    def Direction3d(PStart: IntSurf_PathPoint) -> nanoocp.gp.gp_Vec:
        """
        returns the tangent at the intersection in 3d space
        associated to <P>
        an exception is raised if IsTangent is true.
        """

    @staticmethod
    def Direction2d(PStart: IntSurf_PathPoint) -> nanoocp.gp.gp_Dir2d:
        """
        returns the tangent at the intersection in the
        parametric space of the parametrized surface.This tangent
        is associated to the value2d
        la tangente a un sens signifiant (indique le sens de chemin
        ement)
        an exception is raised if IsTangent is true.
        """

    @staticmethod
    def Multiplicity(PStart: IntSurf_PathPoint) -> int:
        """
        Returns the multiplicity of the point i-e
        the number of auxillar parameters associated to the
        point which the principal parameters are given by Value2d
        """

    @staticmethod
    def Parameters(PStart: IntSurf_PathPoint, Mult: int) -> tuple[float, float]:
        """
        Parametric coordinates associated to the multiplicity.
        An exception is raised if Mult<=0 or Mult>multiplicity.
        """

class IntSurf_Quadric:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def __init__(self, T: nanoocp.gp.gp_Torus) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_Quadric) -> None: ...

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def SetValue(self, C: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def SetValue(self, S: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def SetValue(self, C: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def SetValue(self, T: nanoocp.gp.gp_Torus) -> None: ...

    def Distance(self, P: nanoocp.gp.gp_Pnt) -> float: ...

    def Gradient(self, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Vec: ...

    def ValAndGrad(self, P: nanoocp.gp.gp_Pnt, Grad: nanoocp.gp.gp_Vec) -> float: ...

    def TypeQuadric(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType: ...

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def Value(self, U: float, V: float) -> nanoocp.gp.gp_Pnt: ...

    def D1(self, U: float, V: float, P: nanoocp.gp.gp_Pnt, D1U: nanoocp.gp.gp_Vec, D1V: nanoocp.gp.gp_Vec) -> None: ...

    def DN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    def Normale(self, U: float, V: float) -> nanoocp.gp.gp_Vec: ...

    @overload
    def Normale(self, P: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Vec: ...

    def Parameters(self, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]: ...

class IntSurf_QuadricTool:
    """
    This class provides a tool on a quadric that can be
    used to instantiates the Walking algorithms (see
    package IntWalk) with a Quadric from IntSurf
    as implicit surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntSurf_QuadricTool) -> None: ...

    @staticmethod
    def Value(Quad: IntSurf_Quadric, X: float, Y: float, Z: float) -> float:
        """Returns the value of the function."""

    @staticmethod
    def Gradient(Quad: IntSurf_Quadric, X: float, Y: float, Z: float, V: nanoocp.gp.gp_Vec) -> None:
        """Returns the gradient of the function."""

    @staticmethod
    def ValueAndGradient(Quad: IntSurf_Quadric, X: float, Y: float, Z: float, Grad: nanoocp.gp.gp_Vec) -> float:
        """Returns the value and the gradient."""

    @staticmethod
    def Tolerance(Quad: IntSurf_Quadric) -> float:
        """returns the tolerance of the zero of the implicit function"""

class IntSurf_Transition:
    """
    Definition of the transition at the intersection
    between an intersection line and a restriction curve
    on a surface.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Creates an UNDECIDED transition."""

    @overload
    def __init__(self, Tangent: bool, Type: IntSurf_TypeTrans) -> None:
        """Create a IN or OUT transition"""

    @overload
    def __init__(self, Tangent: bool, Situ: IntSurf_Situation, Oppos: bool) -> None:
        """Create a TOUCH transition."""

    @overload
    def __init__(self, theOther: IntSurf_Transition) -> None: ...

    @overload
    def SetValue(self, Tangent: bool, Type: IntSurf_TypeTrans) -> None:
        """Set the values of an IN or OUT transition."""

    @overload
    def SetValue(self, Tangent: bool, Situ: IntSurf_Situation, Oppos: bool) -> None:
        """Set the values of a TOUCH transition."""

    @overload
    def SetValue(self) -> None:
        """Set the values of an UNDECIDED transition."""

    def TransitionType(self) -> IntSurf_TypeTrans:
        """
        Returns the type of Transition (in/out/touch/undecided)
        for the arc given by value. This the transition of
        the intersection line compared to the Arc of restriction,
        i-e when the function returns INSIDE for example, it
        means that the intersection line goes inside the
        part of plane limited by the arc of restriction.
        """

    def IsTangent(self) -> bool:
        """
        Returns TRUE if the point is tangent to the arc
        given by Value.
        An exception is raised if TransitionType returns UNDECIDED.
        """

    def Situation(self) -> IntSurf_Situation:
        """
        Returns a significant value if TransitionType returns
        TOUCH. In this case, the function returns :
        INSIDE when the intersection line remains inside the Arc,
        OUTSIDE when it remains outside the Arc,
        UNKNOWN when the calsulus cannot give results.
        If TransitionType returns IN, or OUT, or UNDECIDED, a
        exception is raised.
        """

    def IsOpposite(self) -> bool:
        """
        returns a significant value if TransitionType returns
        TOUCH.
        In this case, the function returns true when
        the 2 curves locally define two different parts of the
        space.
        If TransitionType returns IN or OUT or UNDECIDED, an
        exception is raised.
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IntSurf
IntSurf_ListOfPntOn2S = nanoocp.NCollection.NCollection_List[nanoocp.IntSurf.IntSurf_PntOn2S]
IntSurf_SequenceOfInteriorPoint = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_InteriorPoint]
IntSurf_SequenceOfPathPoint = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_PathPoint]
