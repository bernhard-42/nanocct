"""OCCT package IntPatch (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.Bnd
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.IntAna
import nanoocp.IntSurf
import nanoocp.Intf
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math
from nanoocp.math import math_Vector as math_Vector


class IntPatch_IType(enum.IntEnum):
    IntPatch_Lin = 0

    IntPatch_Circle = 1

    IntPatch_Ellipse = 2

    IntPatch_Parabola = 3

    IntPatch_Hyperbola = 4

    IntPatch_Analytic = 5

    IntPatch_Walking = 6

    IntPatch_Restriction = 7

IntPatch_Lin: IntPatch_IType = IntPatch_IType.IntPatch_Lin

IntPatch_Circle: IntPatch_IType = IntPatch_IType.IntPatch_Circle

IntPatch_Ellipse: IntPatch_IType = IntPatch_IType.IntPatch_Ellipse

IntPatch_Parabola: IntPatch_IType = IntPatch_IType.IntPatch_Parabola

IntPatch_Hyperbola: IntPatch_IType = IntPatch_IType.IntPatch_Hyperbola

IntPatch_Analytic: IntPatch_IType = IntPatch_IType.IntPatch_Analytic

IntPatch_Walking: IntPatch_IType = IntPatch_IType.IntPatch_Walking

IntPatch_Restriction: IntPatch_IType = IntPatch_IType.IntPatch_Restriction

class IntPatch_SpecPntType(enum.IntEnum):
    """
    This enum describes the different kinds of
    special (singular) points of Surface-Surface
    intersection algorithm. Such as pole of sphere,
    apex of cone, point on U- or V-seam etc.
    """

    IntPatch_SPntNone = 0

    IntPatch_SPntSeamU = 1

    IntPatch_SPntSeamV = 2

    IntPatch_SPntSeamUV = 3

    IntPatch_SPntPoleSeamU = 4

    IntPatch_SPntPole = 5

IntPatch_SPntNone: IntPatch_SpecPntType = IntPatch_SpecPntType.IntPatch_SPntNone

IntPatch_SPntSeamU: IntPatch_SpecPntType = IntPatch_SpecPntType.IntPatch_SPntSeamU

IntPatch_SPntSeamV: IntPatch_SpecPntType = IntPatch_SpecPntType.IntPatch_SPntSeamV

IntPatch_SPntSeamUV: IntPatch_SpecPntType = IntPatch_SpecPntType.IntPatch_SPntSeamUV

IntPatch_SPntPoleSeamU: IntPatch_SpecPntType = IntPatch_SpecPntType.IntPatch_SPntPoleSeamU

IntPatch_SPntPole: IntPatch_SpecPntType = IntPatch_SpecPntType.IntPatch_SPntPole

class IntPatch_Line(nanoocp.Standard.Standard_Transient):
    """
    Definition of an intersection line between two
    surfaces.
    A line may be either geometric : line, circle, ellipse,
    parabola, hyperbola, as defined in the class GLine,
    or analytic, as defined in the class ALine, or defined
    by a set of points (coming from a walking algorithm) as
    defined in the class WLine.
    """

    def __init__(self, theOther: IntPatch_Line) -> None: ...

    def SetValue(self, Uiso1: bool, Viso1: bool, Uiso2: bool, Viso2: bool) -> None:
        """
        To set the values returned by IsUIsoS1,....
        The default values are False.
        """

    def ArcType(self) -> IntPatch_IType:
        """
        Returns the type of geometry 3d (Line, Circle, Parabola,
        Hyperbola, Ellipse, Analytic, Walking, Restriction)
        """

    def IsTangent(self) -> bool:
        """
        Returns TRUE if the intersection is a line of tangency
        between the 2 patches.
        """

    def TransitionOnS1(self) -> nanoocp.IntSurf.IntSurf_TypeTrans:
        """
        Returns the type of the transition of the line
        for the first surface. The transition is "constant"
        along the line.
        The transition is IN if the line is oriented in such
        a way that the system of vector (N1,N2,T) is right-handed,
        where N1 is the normal to the first surface at a point P,
        N2 is the normal to the second surface at a point P,
        T is the tangent to the intersection line at P.
        If the system of vector is left-handed, the transition
        is OUT.
        When N1 and N2 are colinear all along the intersection
        line, the transition will be
        - TOUCH, if it is possible to use the 2nd derivatives
        to determine the position of one surafce compared
        to the other (see Situation)
        - UNDECIDED otherwise.

        If one of the transition is TOUCH or UNDECIDED, the other
        one has got the same value.
        """

    def TransitionOnS2(self) -> nanoocp.IntSurf.IntSurf_TypeTrans:
        """
        Returns the type of the transition of the line
        for the second surface. The transition is "constant"
        along the line.
        """

    def SituationS1(self) -> nanoocp.IntSurf.IntSurf_Situation:
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of
        the first patch compared to the second one, when
        TransitionOnS1 or TransitionOnS2 returns TOUCH.
        Otherwise, an exception is raised.
        """

    def SituationS2(self) -> nanoocp.IntSurf.IntSurf_Situation:
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of
        the second patch compared to the first one, when
        TransitionOnS1 or TransitionOnS2 returns TOUCH.
        Otherwise, an exception is raised.
        """

    def IsUIsoOnS1(self) -> bool:
        """
        Returns TRUE if the intersection is a U isoparametric curve
        on the first patch.
        """

    def IsVIsoOnS1(self) -> bool:
        """
        Returns TRUE if the intersection is a V isoparametric curve
        on the first patch.
        """

    def IsUIsoOnS2(self) -> bool:
        """
        Returns TRUE if the intersection is a U isoparametric curve
        on the second patch.
        """

    def IsVIsoOnS2(self) -> bool:
        """
        Returns TRUE if the intersection is a V isoparametric curve
        on the second patch.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_Point:
    """
    Definition of an intersection point between two surfaces.
    Such a point is contains geometrical information (see
    the Value method) and logical information.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: IntPatch_Point) -> None: ...

    @overload
    def SetValue(self, Pt: nanoocp.gp.gp_Pnt, Tol: float, Tangent: bool) -> None:
        """
        Sets the values of a point which is on no domain,
        when both surfaces are implicit ones.
        If Tangent is True, the point is a point of tangency
        between the surfaces.
        """

    @overload
    def SetValue(self, Pt: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def SetValue(self, thePOn2S: nanoocp.IntSurf.IntSurf_PntOn2S) -> None:
        """Sets the value of <pt> member"""

    def SetTolerance(self, Tol: float) -> None: ...

    def SetParameters(self, U1: float, V1: float, U2: float, V2: float) -> None:
        """
        Sets the values of the parameters of the point
        on each surface.
        """

    def SetParameter(self, Para: float) -> None:
        """Set the value of the parameter on the intersection line."""

    def SetVertex(self, OnFirst: bool, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> None:
        """
        Sets the values of a point which is a vertex on
        the initial facet of restriction of one
        of the surface.
        If OnFirst is True, the point is on the domain of the
        first patch, otherwise the point is on the domain of the
        second surface.
        """

    def SetArc(self, OnFirst: bool, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Param: float, TLine: nanoocp.IntSurf.IntSurf_Transition, TArc: nanoocp.IntSurf.IntSurf_Transition) -> None:
        """
        Sets the values of a point which is on one of the domain,
        when both surfaces are implicit ones.
        If OnFirst is True, the point is on the domain of the
        first patch, otherwise the point is on the domain of the
        second surface.
        """

    def SetMultiple(self, IsMult: bool) -> None:
        """
        Sets (or unsets) the point as a point on several
        intersection line.
        """

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the intersection point (geometric information)."""

    def ParameterOnLine(self) -> float:
        """
        This method returns the parameter of the point
        on the intersection line.
        If the points does not belong to an intersection line,
        the value returned does not have any sens.
        """

    def Tolerance(self) -> float:
        """This method returns the fuzziness on the point."""

    def IsTangencyPoint(self) -> bool:
        """
        Returns True if the Point is a tangency point between
        the surfaces.
        If the Point is on one of the domain (IsOnDomS1 returns
        True or IsOnDomS2 returns True), an exception is raised.
        """

    def ParametersOnS1(self) -> tuple[float, float]:
        """Returns the parameters on the first surface of the point."""

    def ParametersOnS2(self) -> tuple[float, float]:
        """Returns the parameters on the second surface of the point."""

    def IsMultiple(self) -> bool:
        """
        Returns True if the point belongs to several intersection
        lines.
        """

    def IsOnDomS1(self) -> bool:
        """
        Returns TRUE if the point is on a boundary of the domain
        of the first patch.
        """

    def IsVertexOnS1(self) -> bool:
        """
        Returns TRUE if the point is a vertex on the initial
        restriction facet of the first surface.
        """

    def VertexOnS1(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex:
        """
        Returns the information about the point when it is
        on the domain of the first patch, i-e when the function
        IsVertexOnS1 returns True.
        Otherwise, an exception is raised.
        """

    def ArcOnS1(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the arc of restriction containing the
        vertex.
        The exception DomainError is raised if
        IsOnDomS1 returns False.
        """

    def TransitionLineArc1(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """
        Returns the transition of the point on the
        intersection line with the arc on S1.
        The exception DomainError is raised if IsOnDomS1
        returns False.
        """

    def TransitionOnS1(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """
        Returns the transition between the intersection line
        returned by the method Line and the arc on S1 returned
        by ArcOnS1().
        The exception DomainError is raised if
        IsOnDomS1 returns False.
        """

    def ParameterOnArc1(self) -> float:
        """
        Returns the parameter of the point on the
        arc returned by the method ArcOnS2.
        The exception DomainError is raised if
        IsOnDomS1 returns False.
        """

    def IsOnDomS2(self) -> bool:
        """
        Returns TRUE if the point is on a boundary of the domain
        of the second patch.
        """

    def IsVertexOnS2(self) -> bool:
        """
        Returns TRUE if the point is a vertex on the initial
        restriction facet of the first surface.
        """

    def VertexOnS2(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex:
        """
        Returns the information about the point when it is
        on the domain of the second patch, i-e when the function
        IsVertexOnS2 returns True.
        Otherwise, an exception is raised.
        """

    def ArcOnS2(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the arc of restriction containing the
        vertex.
        The exception DomainError is raised if
        IsOnDomS2 returns False.
        """

    def TransitionLineArc2(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """
        Returns the transition of the point on the
        intersection line with the arc on S2.
        The exception DomainError is raised if IsOnDomS2
        returns False.
        """

    def TransitionOnS2(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """
        Returns the transition between the intersection line
        returned by the method Line and the arc on S2 returned
        by ArcOnS2.
        The exception DomainError is raised if
        IsOnDomS2 returns False.
        """

    def ParameterOnArc2(self) -> float:
        """
        Returns the parameter of the point on the
        arc returned by the method ArcOnS2.
        The exception DomainError is raised if
        IsOnDomS2 returns False.
        """

    def PntOn2S(self) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """
        Returns the PntOn2S
        (geometric Point and the parameters)
        """

    def Parameters(self) -> tuple[float, float, float, float]:
        """
        Returns the parameters on the first and on the
        second surface of the point.
        """

    def ReverseTransition(self) -> None: ...

    def Dump(self) -> None: ...

class IntPatch_ALine(IntPatch_Line):
    """
    Implementation of an intersection line described by a
    parametrized curve.
    """

    @overload
    def __init__(self, C: nanoocp.IntAna.IntAna_Curve, Tang: bool) -> None:
        """
        Creates an analytic intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, C: nanoocp.IntAna.IntAna_Curve, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates an analytic intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, C: nanoocp.IntAna.IntAna_Curve, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates an analytic intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, theOther: IntPatch_ALine) -> None: ...

    def AddVertex(self, Pnt: IntPatch_Point) -> None:
        """To add a vertex in the list."""

    def Replace(self, Index: int, Pnt: IntPatch_Point) -> None:
        """
        Replaces the element of range Index in the list
        of points.
        """

    def SetFirstPoint(self, IndFirst: int) -> None: ...

    def SetLastPoint(self, IndLast: int) -> None: ...

    def FirstParameter(self) -> tuple[float, bool]:
        """
        Returns the first parameter on the intersection line.
        If IsIncluded returns True, Value and D1 methods can
        be call with a parameter equal to FirstParameter.
        Otherwise, the parameter must be greater than
        FirstParameter.
        """

    def LastParameter(self) -> tuple[float, bool]:
        """
        Returns the last parameter on the intersection line.
        If IsIncluded returns True, Value and D1 methods can
        be call with a parameter equal to LastParameter.
        Otherwise, the parameter must be less than LastParameter.
        """

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point of parameter U on the analytic
        intersection line.
        """

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, Du: nanoocp.gp.gp_Vec) -> bool:
        """
        Returns true when the derivative at parameter U
        is defined on the analytic intersection line.
        In that case, Du is the derivative.
        Returns false when it is not possible to
        evaluate the derivative.
        In both cases, P is the point at parameter U on the
        intersection.
        """

    def FindParameter(self, P: nanoocp.gp.gp_Pnt, theParams: nanoocp.NCollection.NCollection_List[float]) -> None:
        """
        Tries to find the parameters of the point P on the curve.
        If the method returns False, the "projection" is
        impossible.
        If the method returns True at least one parameter has been found.
        theParams is always sorted in ascending order.
        """

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the line has a known First point.
        This point is given by the method FirstPoint().
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the line has a known Last point.
        This point is given by the method LastPoint().
        """

    def FirstPoint(self) -> IntPatch_Point:
        """
        Returns the IntPoint corresponding to the FirstPoint.
        An exception is raised when HasFirstPoint returns False.
        """

    def LastPoint(self) -> IntPatch_Point:
        """
        Returns the IntPoint corresponding to the LastPoint.
        An exception is raised when HasLastPoint returns False.
        """

    def NbVertex(self) -> int: ...

    def Vertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ChangeVertex(self, theIndex: int) -> IntPatch_Point:
        """Allows modifying the vertex with index theIndex on the line."""

    def ComputeVertexParameters(self, Tol: float) -> None:
        """
        Set the parameters of all the vertex on the line.
        if a vertex is already in the line,
        its parameter is modified
        else a new point in the line is inserted.
        """

    def Curve(self) -> nanoocp.IntAna.IntAna_Curve: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_ALineToWLine:
    @overload
    def __init__(self, theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theNbPoints: int = 200) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: IntPatch_ALineToWLine) -> None: ...

    def SetTolOpenDomain(self, aT: float) -> None: ...

    def TolOpenDomain(self) -> float: ...

    def SetTolTransition(self, aT: float) -> None: ...

    def TolTransition(self) -> float: ...

    def SetTol3D(self, aT: float) -> None: ...

    def Tol3D(self) -> float: ...

    @overload
    def MakeWLine(self, aline: IntPatch_ALine | None, theLines: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line]) -> None:
        """
        Converts aline to the set of Walking-lines and adds
        them in theLines.
        """

    @overload
    def MakeWLine(self, aline: IntPatch_ALine | None, paraminf: float, paramsup: float, theLines: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line]) -> None:
        """
        Converts aline (limited by paraminf and paramsup) to the set of
        Walking-lines and adds them in theLines.
        """

class IntPatch_ArcFunction(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_ArcFunction) -> None: ...

    def SetQuadric(self, Q: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    @overload
    def Set(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    @overload
    def Set(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]: ...

    def Derivative(self, X: float) -> tuple[bool, float]: ...

    def Values(self, X: float) -> tuple[bool, float, float]: ...

    def NbSamples(self) -> int: ...

    def GetStateNumber(self) -> int: ...

    def Valpoint(self, Index: int) -> nanoocp.gp.gp_Pnt: ...

    def Quadric(self) -> nanoocp.IntSurf.IntSurf_Quadric: ...

    def Arc(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def Surface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def LastComputedPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point, which has been computed
        while the last calling Value() method
        """

class IntPatch_CSFunction(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    this function is associated to the intersection between
    a curve on surface and a surface.
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
        """
        S1 is the surface on which the intersection is searched.
        C is a curve on the surface S2.
        """

    @overload
    def __init__(self, theOther: IntPatch_CSFunction) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def Root(self) -> float: ...

    def AuxillarSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def AuxillarCurve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

class IntPatch_CurvIntSurf:
    @overload
    def __init__(self, F: IntPatch_CSFunction, TolTangency: float) -> None:
        """initialize the parameters to compute the solution"""

    @overload
    def __init__(self, U: float, V: float, W: float, F: IntPatch_CSFunction, TolTangency: float, MarginCoef: float = 0.0) -> None:
        """
        compute the solution point with the close point
        MarginCoef is the coefficient for extension of UV bounds.
        Ex., UFirst -= MarginCoef*(ULast-UFirst)
        """

    @overload
    def __init__(self, theOther: IntPatch_CurvIntSurf) -> None: ...

    def Perform(self, U: float, V: float, W: float, Rsnld: nanoocp.math.math_FunctionSetRoot, u0: float, v0: float, u1: float, v1: float, w0: float, w1: float) -> None:
        """
        compute the solution
        it's possible to write to optimize:
        IntImp_IntCS inter(S1,C1,Toltangency)
        math_FunctionSetRoot rsnld(Inter.function())
        while ...{
        u=...
        v=...
        w=...
        inter.Perform(u,v,w,rsnld)
        }
        or
        IntImp_IntCS inter(Toltangency)
        inter.SetSurface(S);
        math_FunctionSetRoot rsnld(Inter.function())
        while ...{
        C=...
        inter.SetCurve(C);
        u=...
        v=...
        w=...
        inter.Perform(u,v,w,rsnld)
        }
        """

    def IsDone(self) -> bool:
        """Returns TRUE if the creation completed without failure."""

    def IsEmpty(self) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the intersection point
        The exception NotDone is raised if IsDone is false.
        The exception DomainError is raised if IsEmpty is true.
        """

    def ParameterOnCurve(self) -> float: ...

    def ParameterOnSurface(self) -> tuple[float, float]: ...

    def Function(self) -> IntPatch_CSFunction:
        """
        return the math function which
        is used to compute the intersection
        """

class IntPatch_GLine(IntPatch_Line):
    """
    Implementation of an intersection line represented
    by a conic.
    """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, Tang: bool) -> None:
        """
        Creates a Line as intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, Tang: bool) -> None:
        """
        Creates a circle as intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips, Tang: bool) -> None:
        """
        Creates an ellipse as intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab, Tang: bool) -> None:
        """
        Creates a parabola as intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr, Tang: bool) -> None:
        """
        Creates an hyperbola as intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates a Line as intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates a Line as intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates a circle as intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates a circle as intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates an ellipse as intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates an ellispe as intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates a parabola as intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates a parabola as intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates an hyperbola as intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates an hyperbola as intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, theOther: IntPatch_GLine) -> None: ...

    def AddVertex(self, Pnt: IntPatch_Point) -> None:
        """To add a vertex in the list."""

    def Replace(self, Index: int, Pnt: IntPatch_Point) -> None:
        """
        To replace the element of range Index in the list
        of points.
        """

    def SetFirstPoint(self, IndFirst: int) -> None: ...

    def SetLastPoint(self, IndLast: int) -> None: ...

    def Line(self) -> nanoocp.gp.gp_Lin:
        """
        Returns the Lin from gp corresponding to the intersection
        when ArcType returns IntPatch_Line.
        """

    def Circle(self) -> nanoocp.gp.gp_Circ:
        """
        Returns the Circ from gp corresponding to the intersection
        when ArcType returns IntPatch_Circle.
        """

    def Ellipse(self) -> nanoocp.gp.gp_Elips:
        """
        Returns the Elips from gp corresponding to the intersection
        when ArcType returns IntPatch_Ellipse.
        """

    def Parabola(self) -> nanoocp.gp.gp_Parab:
        """
        Returns the Parab from gp corresponding to the intersection
        when ArcType returns IntPatch_Parabola.
        """

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr:
        """
        Returns the Hypr from gp corresponding to the intersection
        when ArcType returns IntPatch_Hyperbola.
        """

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the line has a known First point.
        This point is given by the method FirstPoint().
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the line has a known Last point.
        This point is given by the method LastPoint().
        """

    def FirstPoint(self) -> IntPatch_Point:
        """
        Returns the IntPoint corresponding to the FirstPoint.
        An exception is raised when HasFirstPoint returns False.
        """

    def LastPoint(self) -> IntPatch_Point:
        """
        Returns the IntPoint corresponding to the LastPoint.
        An exception is raised when HasLastPoint returns False.
        """

    def NbVertex(self) -> int: ...

    def Vertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ComputeVertexParameters(self, Tol: float) -> None:
        """
        Set the parameters of all the vertex on the line.
        if a vertex is already in the line,
        its parameter is modified
        else a new point in the line is inserted.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_HCurve2dTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_HCurve2dTool) -> None: ...

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

class IntPatch_HInterTool:
    """
    Tool for the intersection between 2 surfaces.
    Regroupe pour l instant les methodes hors Adaptor3d...
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_HInterTool) -> None: ...

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

    def NbSamplePoints(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> int: ...

    def SamplePoint(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Index: int) -> tuple[float, float]: ...

    @staticmethod
    def HasBeenSeen(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool:
        """
        Returns True if all the intersection point and edges
        are known on the Arc.
        The intersection point are given as vertices.
        The intersection edges are given as intervals between
        two vertices.
        """

    @staticmethod
    def NbSamplesOnArc(A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> int:
        """
        returns the number of points which is used to make
        a sample on the arc. this number is a function of
        the Surface and the CurveOnSurface complexity.
        """

    @staticmethod
    def Bounds(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> tuple[float, float]:
        """
        Returns the parametric limits on the arc C.
        These limits must be finite : they are either
        the real limits of the arc, for a finite arc,
        or a bounding box for an infinite arc.
        """

    @staticmethod
    def Project(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, P: nanoocp.gp.gp_Pnt2d, Ptproj: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float]:
        """
        Projects the point P on the arc C.
        If the methods returns true, the projection is
        successful, and Paramproj is the parameter on the arc
        of the projected point, Ptproj is the projected Point.
        If the method returns false, Param proj and Ptproj
        are not significant.
        """

    @staticmethod
    def Tolerance(V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """
        Returns the parametric tolerance used to consider
        that the vertex and another point meet, i-e
        if std::abs(parameter(Vertex) - parameter(OtherPnt))<=
        Tolerance, the points are "merged".
        """

    @staticmethod
    def Parameter(V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """Returns the parameter of the vertex V on the arc A."""

    @staticmethod
    def NbPoints(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> int:
        """Returns the number of intersection points on the arc A."""

    @staticmethod
    def Value(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int, Pt: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        Returns the value (Pt), the tolerance (Tol), and
        the parameter (U) on the arc A , of the intersection
        point of range Index.
        """

    @staticmethod
    def IsVertex(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> bool:
        """
        Returns True if the intersection point of range Index
        corresponds with a vertex on the arc A.
        """

    @staticmethod
    def Vertex(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> nanoocp.Adaptor3d.Adaptor3d_HVertex:
        """
        When IsVertex returns True, this method returns the
        vertex on the arc A.
        """

    @staticmethod
    def NbSegments(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> int:
        """
        returns the number of part of A solution of the
        of intersection problem.
        """

    @staticmethod
    def HasFirstPoint(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> tuple[bool, int]:
        """
        Returns True when the segment of range Index is not
        open at the left side. In that case, IndFirst is the
        range in the list intersection points (see NbPoints)
        of the one which defines the left bound of the segment.
        Otherwise, the method has to return False, and IndFirst
        has no meaning.
        """

    @staticmethod
    def HasLastPoint(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> tuple[bool, int]:
        """
        Returns True when the segment of range Index is not
        open at the right side. In that case, IndLast is the
        range in the list intersection points (see NbPoints)
        of the one which defines the right bound of the segment.
        Otherwise, the method has to return False, and IndLast
        has no meaning.
        """

    @staticmethod
    def IsAllSolution(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool:
        """
        Returns True when the whole restriction is solution
        of the intersection problem.
        """

class IntPatch_ThePathPointOfTheSOnBounds:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Tol: float, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Tol: float, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_ThePathPointOfTheSOnBounds) -> None: ...

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, Tol: float, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, Tol: float, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt: ...

    def Tolerance(self) -> float: ...

    def IsNew(self) -> bool: ...

    def Vertex(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex: ...

    def Arc(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def Parameter(self) -> float: ...

class IntPatch_TheSegmentOfTheSOnBounds:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: IntPatch_TheSegmentOfTheSOnBounds) -> None: ...

    def SetValue(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """Defines the concerned arc."""

    def SetLimitPoint(self, V: IntPatch_ThePathPointOfTheSOnBounds, First: bool) -> None:
        """
        Defines the first point or the last point,
        depending on the value of the boolean First.
        """

    def Curve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the geometric curve on the surface 's domain
        which is solution.
        """

    def HasFirstPoint(self) -> bool:
        """
        Returns True if there is a vertex (ThePathPoint) defining
        the lowest valid parameter on the arc.
        """

    def FirstPoint(self) -> IntPatch_ThePathPointOfTheSOnBounds:
        """Returns the first point."""

    def HasLastPoint(self) -> bool:
        """
        Returns True if there is a vertex (ThePathPoint) defining
        the greatest valid parameter on the arc.
        """

    def LastPoint(self) -> IntPatch_ThePathPointOfTheSOnBounds:
        """Returns the last point."""

class IntPatch_TheSOnBounds:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: IntPatch_TheSOnBounds) -> None: ...

    def Perform(self, F: IntPatch_ArcFunction, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolBoundary: float, TolTangency: float, RecheckOnRegularity: bool = False) -> None:
        """
        Algorithm to find the points and parts of curves of Domain
        (domain of of restriction of a surface) which verify
        F = 0.
        TolBoundary defines if a curve is on Q.
        TolTangency defines if a point is on Q.
        """

    def IsDone(self) -> bool:
        """Returns True if the calculus was successful."""

    def AllArcSolution(self) -> bool:
        """
        Returns true if all arc of the Arcs are solution (inside
        the surface).
        An exception is raised if IsDone returns False.
        """

    def NbPoints(self) -> int:
        """
        Returns the number of resulting points.
        An exception is raised if IsDone returns False (NotDone).
        """

    def Point(self, Index: int) -> IntPatch_ThePathPointOfTheSOnBounds:
        """
        Returns the resulting point of range Index.
        The exception NotDone is raised if IsDone() returns
        False.
        The exception OutOfRange is raised if
        Index <= 0 or Index > NbPoints.
        """

    def NbSegments(self) -> int:
        """
        Returns the number of the resulting segments.
        An exception is raised if IsDone returns False (NotDone).
        """

    def Segment(self, Index: int) -> IntPatch_TheSegmentOfTheSOnBounds:
        """
        Returns the resulting segment of range Index.
        The exception NotDone is raised if IsDone() returns
        False.
        The exception OutOfRange is raised if
        Index <= 0 or Index > NbPoints.
        """

class IntPatch_ImpImpIntersection:
    """
    Implementation of the intersection between two
    quadric patches : Plane, Cone, Cylinder or Sphere.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float, theIsReqToKeepRLine: bool = False) -> None:
        """
        Flag theIsReqToKeepRLine has been entered only for
        compatibility with TopOpeBRep package. It shall be deleted
        after deleting TopOpeBRep.
        When intersection result returns IntPatch_RLine and another
        IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE)
        will always keep both lines even if they are coincided.
        """

    @overload
    def __init__(self, theOther: IntPatch_ImpImpIntersection) -> None: ...

    class IntStatus(enum.IntEnum):
        IntStatus_OK = 0

        IntStatus_InfiniteSectionCurve = 1

        IntStatus_Fail = 2

    IntStatus_OK: IntPatch_ImpImpIntersection.IntStatus = IntStatus.IntStatus_OK

    IntStatus_InfiniteSectionCurve: IntPatch_ImpImpIntersection.IntStatus = IntStatus.IntStatus_InfiniteSectionCurve

    IntStatus_Fail: IntPatch_ImpImpIntersection.IntStatus = IntStatus.IntStatus_Fail

    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float, theIsReqToKeepRLine: bool = False) -> None:
        """
        Flag theIsReqToKeepRLine has been entered only for
        compatibility with TopOpeBRep package. It shall be deleted
        after deleting TopOpeBRep.
        When intersection result returns IntPatch_RLine and another
        IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE)
        will always keep both lines even if they are coincided.
        """

    def IsDone(self) -> bool:
        """Returns True if the calculus was successful."""

    def GetStatus(self) -> IntPatch_ImpImpIntersection.IntStatus:
        """Returns status"""

    def IsEmpty(self) -> bool:
        """Returns true if the is no intersection."""

    def TangentFaces(self) -> bool:
        """
        Returns True if the two patches are considered as
        entirely tangent, i.e every restriction arc of one
        patch is inside the geometric base of the other patch.
        """

    def OppositeFaces(self) -> bool:
        """
        Returns True when the TangentFaces returns True and the
        normal vectors evaluated at a point on the first and the
        second surface are opposite.
        The exception DomainError is raised if TangentFaces
        returns False.
        """

    def NbPnts(self) -> int:
        """Returns the number of "single" points."""

    def Point(self, Index: int) -> IntPatch_Point:
        """
        Returns the point of range Index.
        An exception is raised if Index<=0 or Index>NbPnt.
        """

    def NbLines(self) -> int:
        """Returns the number of intersection lines."""

    def Line(self, Index: int) -> IntPatch_Line:
        """
        Returns the line of range Index.
        An exception is raised if Index<=0 or Index>NbLine.
        """

class IntPatch_TheSearchInside:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: IntPatch_TheSurfFunction, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, T: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Epsilon: float) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_TheSearchInside) -> None: ...

    @overload
    def Perform(self, F: IntPatch_TheSurfFunction, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, T: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Epsilon: float) -> None: ...

    @overload
    def Perform(self, F: IntPatch_TheSurfFunction, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, UStart: float, VStart: float) -> None: ...

    def IsDone(self) -> bool: ...

    def NbPoints(self) -> int:
        """
        Returns the number of points.
        The exception NotDone if raised if IsDone
        returns False.
        """

    def Value(self, Index: int) -> nanoocp.IntSurf.IntSurf_InteriorPoint:
        """
        Returns the point of range Index.
        The exception NotDone if raised if IsDone
        returns False.
        The exception OutOfRange if raised if
        Index <= 0 or Index > NbPoints.
        """

class IntPatch_ImpPrmIntersection:
    """
    Implementation of the intersection between a natural
    quadric patch : Plane, Cone, Cylinder or Sphere and
    a bi-parametrised surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float, Fleche: float, Pas: float) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_ImpPrmIntersection) -> None: ...

    def SetStartPoint(self, U: float, V: float) -> None:
        """to search for solution from the given point"""

    def Perform(self, Surf1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Surf2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float, Fleche: float, Pas: float) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if the calculus was successful."""

    def IsEmpty(self) -> bool:
        """Returns true if the is no intersection."""

    def NbPnts(self) -> int:
        """Returns the number of "single" points."""

    def Point(self, Index: int) -> IntPatch_Point:
        """
        Returns the point of range Index.
        An exception is raised if Index<=0 or Index>NbPnt.
        """

    def NbLines(self) -> int:
        """Returns the number of intersection lines."""

    def Line(self, Index: int) -> IntPatch_Line:
        """
        Returns the line of range Index.
        An exception is raised if Index<=0 or Index>NbLine.
        """

class IntPatch_InterferencePolyhedron(nanoocp.Intf.Intf_Interference):
    """
    Computes the interference between two polyhedra or the
    self interference of a polyhedron. Points of intersection,
    polylines of intersection and zones of tangence.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty interference of Polyhedron."""

    @overload
    def __init__(self, Obje: IntPatch_Polyhedron) -> None:
        """
        Constructs and computes the self interference of a
        Polyhedron.
        """

    @overload
    def __init__(self, Obje1: IntPatch_Polyhedron, Obje2: IntPatch_Polyhedron) -> None:
        """
        Constructs and computes an interference between the two
        Polyhedra.
        """

    @overload
    def __init__(self, theOther: IntPatch_InterferencePolyhedron) -> None: ...

    @overload
    def Perform(self, Obje1: IntPatch_Polyhedron, Obje2: IntPatch_Polyhedron) -> None:
        """Computes the interference between the two Polyhedra."""

    @overload
    def Perform(self, Obje: IntPatch_Polyhedron) -> None:
        """Computes the self interference of a Polyhedron."""

class IntPatch_Intersection:
    """
    This class provides a generic algorithm to intersect
    2 surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_Intersection) -> None: ...

    def SetTolerances(self, TolArc: float, TolTang: float, UVMaxStep: float, Fleche: float) -> None:
        """
        Set the tolerances used by the algorithms:
        --- Implicit   - Parametric
        --- Parametric - Parametric
        --- Implicit   - Implicit

        TolArc is used to compute the intersections
        between the restrictions of a surface and a
        walking line.

        TolTang is used to compute the points on a walking
        line, and in geometric algorithms.

        Fleche is a parameter used in the walking
        algorithms to provide small curvatures on a line.

        UVMaxStep is a parameter used in the walking
        algorithms to compute the distance between to
        points in their respective parametric spaces.
        """

    @overload
    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float, isGeomInt: bool = True, theIsReqToKeepRLine: bool = False, theIsReqToPostWLProc: bool = True) -> None:
        """
        Flag theIsReqToKeepRLine has been entered only for
        compatibility with TopOpeBRep package. It shall be deleted
        after deleting TopOpeBRep.
        When intersection result returns IntPatch_RLine and another
        IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE)
        will always keep both lines even if they are coincided.
        Flag theIsReqToPostWLProc has been entered only for
        compatibility with TopOpeBRep package. It shall be deleted
        after deleting TopOpeBRep.
        If theIsReqToPostWLProc == FALSE, then we will work with Walking-line
        obtained after intersection algorithm directly (without any post-processing).
        """

    @overload
    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float, LOfPnts: nanoocp.NCollection.NCollection_List[nanoocp.IntSurf.IntSurf_PntOn2S], isGeomInt: bool = True, theIsReqToKeepRLine: bool = False, theIsReqToPostWLProc: bool = True) -> None:
        """
        If isGeomInt == false, then method
        Param-Param intersection will be used.
        Flag theIsReqToKeepRLine has been entered only for
        compatibility with TopOpeBRep package. It shall be deleted
        after deleting TopOpeBRep.
        When intersection result returns IntPatch_RLine and another
        IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE)
        will always keep both lines even if they are coincided.
        Flag theIsReqToPostWLProc has been entered only for
        compatibility with TopOpeBRep package. It shall be deleted
        after deleting TopOpeBRep.
        If theIsReqToPostWLProc == FALSE, then we will work with Walking-line
        obtained after intersection algorithm directly (without any post-processing).
        """

    @overload
    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, U1: float, V1: float, U2: float, V2: float, TolArc: float, TolTang: float) -> None:
        """Perform with start point"""

    @overload
    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolArc: float, TolTang: float) -> None:
        """Uses for finding self-intersected surfaces."""

    def IsDone(self) -> bool:
        """Returns True if the calculus was successful."""

    def IsEmpty(self) -> bool:
        """Returns true if the is no intersection."""

    def TangentFaces(self) -> bool:
        """
        Returns True if the two patches are considered as
        entirely tangent, i-e every restriction arc of one
        patch is inside the geometric base of the other patch.
        """

    def OppositeFaces(self) -> bool:
        """
        Returns True when the TangentFaces returns True and the
        normal vectors evaluated at a point on the first and the
        second surface are opposite.
        The exception DomainError is raised if TangentFaces
        returns False.
        """

    def NbPnts(self) -> int:
        """Returns the number of "single" points."""

    def Point(self, Index: int) -> IntPatch_Point:
        """
        Returns the point of range Index.
        An exception is raised if Index<=0 or Index>NbPnt.
        """

    def NbLines(self) -> int:
        """Returns the number of intersection lines."""

    def Line(self, Index: int) -> IntPatch_Line:
        """
        Returns the line of range Index.
        An exception is raised if Index<=0 or Index>NbLine.
        """

    def SequenceOfLine(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line]: ...

    def Dump(self, Mode: int, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> None:
        """
        Dump of each result line.
        Mode for more accurate dumps.
        """

    @staticmethod
    def CheckSingularPoints(theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theD1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> tuple[bool, float]:
        """
        Checks if surface theS1 has degenerated boundary (dS/du or dS/dv = 0) and
        calculates minimal distance between corresponding singular points and surface theS2
        If singular point exists the method returns "true" and stores minimal distance in theDist.
        """

    @staticmethod
    def DefineUVMaxStep(theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theD1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theD2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> float:
        """
        Calculates recommended value for myUVMaxStep depending on surfaces and their domains
        """

    @staticmethod
    def PrepareSurfaces(theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theD1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theD2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Tol: float, theSeqHS1: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Adaptor3d.Adaptor3d_Surface], theSeqHS2: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Adaptor3d.Adaptor3d_Surface]) -> None:
        """Prepares surfaces for intersection"""

class IntPatch_LineConstructor:
    """
    The intersections algorithms compute the intersection
    on two surfaces and return the intersections lines as
    IntPatch_Line.
    """

    @overload
    def __init__(self, mode: int) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_LineConstructor) -> None: ...

    def Perform(self, SL: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line], L: IntPatch_Line | None, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, D2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Tol: float) -> None: ...

    def NbLines(self) -> int: ...

    def Line(self, index: int) -> IntPatch_Line: ...

class IntPatch_PointLine(IntPatch_Line):
    """
    Definition of an intersection line between two
    surfaces.
    A line defined by a set of points
    (e.g. coming from a walking algorithm) as
    defined in the class WLine or RLine (Restriction line).
    """

    def AddVertex(self, Pnt: IntPatch_Point, theIsPrepend: bool = False) -> None:
        """
        Adds a vertex in the list. If theIsPrepend == TRUE the new
        vertex will be added before the first element of vertices sequence.
        Otherwise, to the end of the sequence
        """

    def NbPnts(self) -> int:
        """Returns the number of intersection points."""

    def NbVertex(self) -> int:
        """Returns number of vertices (IntPatch_Point) of the line"""

    def Point(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """Returns the intersection point of range Index."""

    def Vertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ChangeVertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ClearVertexes(self) -> None:
        """Removes vertices from the line"""

    def RemoveVertex(self, theIndex: int) -> None:
        """Removes single vertex from the line"""

    def Curve(self) -> nanoocp.IntSurf.IntSurf_LineOn2S:
        """Returns set of intersection points"""

    def IsOutSurf1Box(self, P1: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Returns TRUE if P1 is out of the box built from
        the points on 1st surface
        """

    def IsOutSurf2Box(self, P2: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Returns TRUE if P2 is out of the box built from
        the points on 2nd surface
        """

    def IsOutBox(self, P: nanoocp.gp.gp_Pnt) -> bool:
        """Returns TRUE if P is out of the box built from 3D-points."""

    @staticmethod
    def CurvatureRadiusOfIntersLine(theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theUVPoint: nanoocp.IntSurf.IntSurf_PntOn2S) -> float:
        """
        Returns the radius of curvature of
        the intersection line in given point.
        Returns negative value if computation is not possible.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_Polygo(nanoocp.Intf.Intf_Polygon2d):
    def Error(self) -> float: ...

    def NbPoints(self) -> int: ...

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt2d: ...

    def DeflectionOverEstimation(self) -> float:
        """Returns the tolerance of the polygon."""

    def NbSegments(self) -> int:
        """Returns the number of Segments in the polyline."""

    def Segment(self, theIndex: int, theBegin: nanoocp.gp.gp_Pnt2d, theEnd: nanoocp.gp.gp_Pnt2d) -> None:
        """Returns the points of the segment <Index> in the Polygon."""

    def Dump(self) -> None: ...

class IntPatch_PolyArc(IntPatch_Polygo):
    @overload
    def __init__(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, NbSample: int, Pfirst: float, Plast: float, BoxOtherPolygon: nanoocp.Bnd.Bnd_Box2d) -> None:
        """
        Creates the polygon of the arc A on the surface S.
        The arc is limited by the parameters Pfirst and Plast.
        None of these parameters can be infinite.
        """

    @overload
    def __init__(self, theOther: IntPatch_PolyArc) -> None: ...

    def Closed(self) -> bool: ...

    def NbPoints(self) -> int: ...

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt2d: ...

    def Parameter(self, Index: int) -> float: ...

    def SetOffset(self, OffsetX: float, OffsetY: float) -> None: ...

class IntPatch_PolyLine(IntPatch_Polygo):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, InitDefle: float) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_PolyLine) -> None: ...

    def SetWLine(self, OnFirst: bool, Line: IntPatch_WLine | None) -> None: ...

    def SetRLine(self, OnFirst: bool, Line: IntPatch_RLine | None) -> None: ...

    def ResetError(self) -> None: ...

    def NbPoints(self) -> int: ...

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt2d: ...

class IntPatch_Polyhedron:
    """
    This class provides a linear approximation of the PSurface.
    preview a constructor on a zone of a surface
    """

    @overload
    def __init__(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def __init__(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, nbdU: int, nbdV: int) -> None:
        """
        MaTriangle constructor with an double array of pnt for the
        representation of a double array of triangles.
        """

    @overload
    def __init__(self, theOther: IntPatch_Polyhedron) -> None: ...

    def Destroy(self) -> None: ...

    @overload
    def DeflectionOverEstimation(self, flec: float) -> None: ...

    @overload
    def DeflectionOverEstimation(self) -> float: ...

    def Size(self) -> tuple[int, int]:
        """Get the size of the MaTriangle."""

    def NbTriangles(self) -> int:
        """
        Give the number of triangles in this double array of
        triangles (nbdu*nbdv*2).
        """

    def Triangle(self, Index: int) -> tuple[int, int, int]:
        """
        Give the 3 points of the triangle of address Index in
        the double array of triangles.
        """

    def TriConnex(self, Triang: int, Pivot: int, Pedge: int) -> tuple[int, int, int]:
        """
        Give the address Tricon of the triangle connexe to the
        triangle of address Triang by the edge Pivot Pedge and
        the third point of this connexe triangle. When we are
        on a free edge TriCon==0 but the function return the
        value of the triangle in the other side of Pivot on
        the free edge. Used to turn around a vertex.
        """

    def NbPoints(self) -> int:
        """
        Give the number of point in the double array of
        triangles ((nbdu+1)*(nbdv+1)).
        """

    @overload
    def Point(self, thePnt: nanoocp.gp.gp_Pnt, lig: int, col: int, U: float, V: float) -> None:
        """
        Set the value of a field of the double array of
        points.
        """

    @overload
    def Point(self, Index: int) -> tuple[nanoocp.gp.gp_Pnt, float, float]: ...

    @overload
    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def Point(self, Index: int, P: nanoocp.gp.gp_Pnt) -> None:
        """Give the point of index i in the MaTriangle."""

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the MaTriangle."""

    def FillBounding(self) -> None:
        """
        Compute the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    def ComponentsBounding(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]:
        """
        Give the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    def PlaneEquation(self, Triang: int, NormalVector: nanoocp.gp.gp_XYZ) -> float:
        """Give the plane equation of the triangle of address Triang."""

    def Contain(self, Triang: int, ThePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Give the plane equation of the triangle of address Triang."""

    def Parameters(self, Index: int) -> tuple[float, float]: ...

    def Dump(self) -> None: ...

class IntPatch_PolyhedronTool:
    """
    Describe the signature of a polyhedral surface with
    only triangular facets and the necessary information
    to compute the interferences.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_PolyhedronTool) -> None: ...

    @staticmethod
    def Bounding(thePolyh: IntPatch_Polyhedron) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the Polyhedron."""

    @staticmethod
    def ComponentsBounding(thePolyh: IntPatch_Polyhedron) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]:
        """
        Give the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    @staticmethod
    def DeflectionOverEstimation(thePolyh: IntPatch_Polyhedron) -> float:
        """Give the tolerance of the polygon."""

    @staticmethod
    def NbTriangles(thePolyh: IntPatch_Polyhedron) -> int:
        """Give the number of triangles in this polyhedral surface."""

    @staticmethod
    def Triangle(thePolyh: IntPatch_Polyhedron, Index: int) -> tuple[int, int, int]:
        """
        Give the indices of the 3 points of the triangle of
        address Index in the Polyhedron.
        """

    @staticmethod
    def Point(thePolyh: IntPatch_Polyhedron, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of index i in the polyhedral surface."""

    @staticmethod
    def TriConnex(thePolyh: IntPatch_Polyhedron, Triang: int, Pivot: int, Pedge: int) -> tuple[int, int, int]:
        """
        Gives the address Tricon of the triangle connexe to
        the triangle of address Triang by the edge Pivot Pedge
        and the third point of this connexe triangle. When we
        are on a free edge TriCon==0 but the function return
        the value of the triangle in the other side of Pivot
        on the free edge. Used to turn around a vertex.
        """

class IntPatch_PrmPrmIntersection:
    """
    Implementation of the Intersection between two bi-parametrised surfaces.

    To avoid multiple constructions of the approximated
    polyhedron of the surfaces, the algorithm can be
    called with the two surfaces and their associated polyhedron.
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, theOther: IntPatch_PrmPrmIntersection) -> None: ...

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron1: IntPatch_Polyhedron, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron2: IntPatch_Polyhedron, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None:
        """
        Performs the intersection between <Caro1> and
        <Caro2>. Associated Polyhedrons <Polyhedron1>
        and <Polyhedron2> are given.
        """

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron1: IntPatch_Polyhedron, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float, ClearFlag: bool = True) -> None: ...

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float, ListOfPnts: nanoocp.NCollection.NCollection_List[nanoocp.IntSurf.IntSurf_PntOn2S]) -> None: ...

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, U1: float, V1: float, U2: float, V2: float, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None:
        """
        Performs the intersection between <Caro1> and
        <Caro2>. The method computes the polyhedron on
        each surface.
        """

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron2: IntPatch_Polyhedron, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None:
        """
        Performs the intersection between <Caro1> and
        <Caro2>.

        The polyhedron which approximates <Caro2>,
        <Polyhedron2> is given. The other one is
        computed.
        """

    @overload
    def Perform(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron1: IntPatch_Polyhedron, Domain1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None:
        """
        Performs the intersection between <Caro1> and
        <Caro2>.

        The polyhedron which approximates <Caro1>,
        <Polyhedron1> is given. The other one is
        computed.
        """

    def IsDone(self) -> bool:
        """Returns true if the calculus was successful."""

    def IsEmpty(self) -> bool:
        """Returns true if the is no intersection."""

    def NbLines(self) -> int:
        """Returns the number of intersection lines."""

    def Line(self, Index: int) -> IntPatch_Line:
        """
        Returns the line of range Index.
        An exception is raised if Index<=0 or Index>NbLine.
        """

    def NewLine(self, Caro1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Caro2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, IndexLine: int, LowPoint: int, HighPoint: int, NbPoints: int) -> IntPatch_Line:
        """
        Computes about <NbPoints> Intersection Points on
        the Line <IndexLine> between the Points of Index
        <LowPoint> and <HighPoint>.

        All the points of the line of index <IndexLine>
        with an index between <LowPoint> and <HighPoint>
        are in the returned line. New Points are inserted
        between existing points if those points are not
        too closed.

        An exception is raised if Index<=0 or Index>NbLine.
        or if IsDone returns False
        """

    def GrilleInteger(self, ix: int, iy: int, iz: int) -> int: ...

    def IntegerGrille(self, t: int) -> tuple[int, int, int]: ...

    def DansGrille(self, t: int) -> int: ...

    def NbPointsGrille(self) -> int: ...

    def RemplitLin(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, Map: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...

    def RemplitTri(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, x3: int, y3: int, z3: int, Map: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...

    def Remplit(self, a: int, b: int, c: int, Map: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...

    def CodeReject(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float) -> int: ...

    def PointDepart(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, SU1: int, SV1: int, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, SU2: int, SV2: int) -> nanoocp.IntSurf.IntSurf_LineOn2S: ...

class IntPatch_PrmPrmIntersection_T3Bits:
    @overload
    def __init__(self, size: int) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...

    def Add(self, t: int) -> None: ...

    def Val(self, t: int) -> int: ...

    def Raz(self, t: int) -> None: ...

    def ResetAnd(self) -> None: ...

    def And(self, Oth: IntPatch_PrmPrmIntersection_T3Bits) -> tuple[int, int]: ...

class IntPatch_RLine(IntPatch_PointLine):
    """
    Implementation of an intersection line described by a
    restriction line on one of the surfaces.
    """

    @overload
    def __init__(self, Tang: bool) -> None:
        """
        Creates a restriction as an intersection line
        when the transitions are Undecided.
        """

    @overload
    def __init__(self, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates a restriction as an intersection line
        when the transitions are In or Out.
        """

    @overload
    def __init__(self, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates a restriction as an intersection line
        when the transitions are Touch.
        """

    @overload
    def __init__(self, theOther: IntPatch_RLine) -> None: ...

    def AddVertex(self, Pnt: IntPatch_Point, theIsPrepend: bool = False) -> None:
        """
        Adds a vertex in the list. If theIsPrepend == TRUE the new
        vertex will be added before the first element of vertices sequence.
        Otherwise, to the end of the sequence
        """

    def Replace(self, Index: int, Pnt: IntPatch_Point) -> None:
        """
        Replaces the element of range Index in the list
        of points.
        """

    def SetFirstPoint(self, IndFirst: int) -> None: ...

    def SetLastPoint(self, IndLast: int) -> None: ...

    def Add(self, L: nanoocp.IntSurf.IntSurf_LineOn2S | None) -> None: ...

    def IsArcOnS1(self) -> bool:
        """
        Returns True if the intersection is on the domain of the
        first patch.
        Returns False if the intersection is on the domain of
        the second patch.
        """

    def IsArcOnS2(self) -> bool:
        """
        Returns True if the intersection is on the domain of the
        first patch.
        Returns False if the intersection is on the domain of
        the second patch.
        """

    def SetArcOnS1(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def SetArcOnS2(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def ArcOnS1(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Returns the concerned arc."""

    def ArcOnS2(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Returns the concerned arc."""

    def ParamOnS1(self) -> tuple[float, float]: ...

    def ParamOnS2(self) -> tuple[float, float]: ...

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the line has a known First point.
        This point is given by the method FirstPoint().
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the line has a known Last point.
        This point is given by the method LastPoint().
        """

    def FirstPoint(self) -> IntPatch_Point:
        """
        Returns the IntPoint corresponding to the FirstPoint.
        An exception is raised when HasFirstPoint returns False.
        """

    def LastPoint(self) -> IntPatch_Point:
        """
        Returns the IntPoint corresponding to the LastPoint.
        An exception is raised when HasLastPoint returns False.
        """

    def NbVertex(self) -> int:
        """Returns number of vertices (IntPatch_Point) of the line"""

    def Vertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ChangeVertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def RemoveVertex(self, theIndex: int) -> None:
        """Removes single vertex from the line"""

    def HasPolygon(self) -> bool: ...

    def NbPnts(self) -> int:
        """Returns the number of intersection points."""

    def Point(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """Returns the intersection point of range Index."""

    def SetPoint(self, Index: int, Pnt: IntPatch_Point) -> None:
        """Set the Point of index <Index> in the LineOn2S"""

    def ComputeVertexParameters(self, Tol: float) -> None:
        """
        Set the parameters of all the vertex on the line.
        if a vertex is already in the line,
        its parameter is modified
        else a new point in the line is inserted.
        """

    def Curve(self) -> nanoocp.IntSurf.IntSurf_LineOn2S:
        """Returns set of intersection points"""

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

    def ClearVertexes(self) -> None:
        """Removes vertices from the line (i.e. cleans svtx member)"""

    def SetCurve(self, theNewCurve: nanoocp.IntSurf.IntSurf_LineOn2S | None) -> None: ...

    def Dump(self, theMode: int) -> None:
        """
        if (theMode == 0) then prints the information about WLine
        if (theMode == 1) then prints the list of 3d-points
        if (theMode == 2) then prints the list of 2d-points on the 1st surface
        Otherwise, prints list of 2d-points on the 2nd surface
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_RstInt:
    """
    trouver les points d intersection entre la ligne de
    cheminement et les arcs de restriction
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_RstInt) -> None: ...

    @staticmethod
    def PutVertexOnLine(L: IntPatch_Line | None, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, OtherSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, OnFirst: bool, Tol: float) -> None: ...

class IntPatch_SpecialPoints:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_SpecialPoints) -> None: ...

    @staticmethod
    def AddCrossUVIsoPoint(theQSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, thePSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theRefPt: nanoocp.IntSurf.IntSurf_PntOn2S, theTol3d: float, theAddedPoint: nanoocp.IntSurf.IntSurf_PntOn2S, theIsReversed: bool = False) -> bool:
        """
        Adds the point defined as intersection
        of two isolines (U = 0 and V = 0) on theQSurf in theLine.
        theRefPt is used to correct adjusting parameters.
        If theIsReversed is TRUE then theQSurf correspond to the
        second (otherwise, the first) surface while forming
        intersection point IntSurf_PntOn2S.
        """

    @staticmethod
    def AddPointOnUorVIso(theQSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, thePSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theRefPt: nanoocp.IntSurf.IntSurf_PntOn2S, theIsU: bool, theIsoParameter: float, theToler: nanoocp.math.math_Vector, theInitPoint: nanoocp.math.math_Vector, theInfBound: nanoocp.math.math_Vector, theSupBound: nanoocp.math.math_Vector, theAddedPoint: nanoocp.IntSurf.IntSurf_PntOn2S, theIsReversed: bool = False) -> bool:
        """
        Adds the point lain strictly in the isoline U = 0 or V = 0 of theQSurf,
        in theLine.
        theRefPt is used to correct adjusting parameters.
        If theIsReversed is TRUE then theQSurf corresponds to the
        second (otherwise, the first) surface while forming
        intersection point IntSurf_PntOn2S.
        All math_Vector-objects must be filled as follows:
        [1] - U-parameter of thePSurf;
        [2] - V-parameter of thePSurf;
        [3] - U- (if V-isoline is considered) or V-parameter
        (if U-isoline is considered) of theQSurf.
        """

    @staticmethod
    def AddSingularPole(theQSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, thePSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, thePtIso: nanoocp.IntSurf.IntSurf_PntOn2S, theVertex: IntPatch_Point, theAddedPoint: nanoocp.IntSurf.IntSurf_PntOn2S, theIsReversed: bool = False, theIsReqRefCheck: bool = False) -> bool:
        """
        Computes the pole of sphere to add it in the intersection line.
        Stores the result in theAddedPoint variable (does not add in the line).
        At that, cone and sphere (with singularity) must be set in theQSurf parameter.
        By default (if theIsReversed == FALSE), theQSurf is the first surface of the
        Walking line. If it is not, theIsReversed parameter must be set to TRUE.
        theIsReqRefCheck is TRUE if and only if 3D-point of theRefPt must be pole or apex
        for check (e.g. if it is vertex).
        thePtIso is the reference point for obtaining isoline where must be placed the Apex/Pole.

        ATTENTION!!!
        theVertex must be initialized before calling the method .
        """

    @staticmethod
    def ContinueAfterSpecialPoint(theQSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, thePSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theRefPt: nanoocp.IntSurf.IntSurf_PntOn2S, theSPType: IntPatch_SpecPntType, theTol2D: float, theNewPoint: nanoocp.IntSurf.IntSurf_PntOn2S, theIsReversed: bool = False) -> bool:
        """
        Special point has already been added in the line. Now, we need in correct
        prolongation of the line or in start new line. This function returns new point.

        ATTENTION!!!
        theNewPoint is not only Output parameter. It is Input/Output one. I.e.
        theNewPoint is reference point together with theRefPt.
        """

class IntPatch_TheIWLineOfTheIWalking(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None = None) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_TheIWLineOfTheIWalking) -> None: ...

    def Reverse(self) -> None:
        """reverse the points in the line. Hasfirst, HasLast are kept."""

    def Cut(self, Index: int) -> None:
        """Cut the line at the point of rank Index."""

    def AddPoint(self, P: nanoocp.IntSurf.IntSurf_PntOn2S) -> None:
        """Add a point in the line."""

    @overload
    def AddStatusFirst(self, Closed: bool, HasFirst: bool) -> None: ...

    @overload
    def AddStatusFirst(self, Closed: bool, HasLast: bool, Index: int, P: nanoocp.IntSurf.IntSurf_PathPoint) -> None: ...

    def AddStatusFirstLast(self, Closed: bool, HasFirst: bool, HasLast: bool) -> None: ...

    @overload
    def AddStatusLast(self, HasLast: bool) -> None: ...

    @overload
    def AddStatusLast(self, HasLast: bool, Index: int, P: nanoocp.IntSurf.IntSurf_PathPoint) -> None: ...

    def AddIndexPassing(self, Index: int) -> None:
        """
        associate the index of the point on the line with the index of the point
        passing through the starting iterator
        """

    def SetTangentVector(self, V: nanoocp.gp.gp_Vec, Index: int) -> None: ...

    def SetTangencyAtBegining(self, IsTangent: bool) -> None: ...

    def SetTangencyAtEnd(self, IsTangent: bool) -> None: ...

    def NbPoints(self) -> int:
        """
        Returns the number of points of the line (including first
        point and end point : see HasLastPoint and HasFirstPoint).
        """

    def Value(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """
        Returns the point of range Index.
        If index <= 0 or Index > NbPoints, an exception is raised.
        """

    def Line(self) -> nanoocp.IntSurf.IntSurf_LineOn2S:
        """Returns the LineOn2S contained in the walking line."""

    def IsClosed(self) -> bool:
        """Returns True if the line is closed."""

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the first point of the line is a
        marching point. when HasFirstPoint==False the line
        begins on the natural bound of the surface. The line
        can be too long
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the end point of the line is a
        marching point (Point from IntWS).
        when HasFirstPoint==False the line ends
        on the natural bound of the surface. The line can be
        too long.
        """

    def FirstPoint(self) -> nanoocp.IntSurf.IntSurf_PathPoint:
        """
        Returns the first point of the line when it is a
        marching point.
        An exception is raised if HasFirstPoint returns False.
        """

    def FirstPointIndex(self) -> int:
        """
        Returns the Index of first point of the line when it is a
        marching point. This index is the index in the
        PointStartIterator.
        An exception is raised if HasFirstPoint returns False.
        """

    def LastPoint(self) -> nanoocp.IntSurf.IntSurf_PathPoint:
        """
        Returns the last point of the line when it is a
        marching point.
        An exception is raised if HasLastPoint returns False.
        """

    def LastPointIndex(self) -> int:
        """
        Returns the index of last point of the line when it is a
        marching point. This index is the index in the
        PointStartIterator.
        An exception is raised if HasLastPoint returns False.
        """

    def NbPassingPoint(self) -> int:
        """
        returns the number of points belonging to Pnts1 which are
        passing point.
        """

    def PassingPoint(self, Index: int) -> tuple[int, int]:
        """
        returns the index of the point belonging to the line which
        is associated to the passing point belonging to Pnts1
        an exception is raised if Index > NbPassingPoint()
        """

    def TangentVector(self) -> tuple[nanoocp.gp.gp_Vec, int]: ...

    def IsTangentAtBegining(self) -> bool: ...

    def IsTangentAtEnd(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_TheIWalking:
    @overload
    def __init__(self, Epsilon: float, Deflection: float, Step: float, theToFillHoles: bool = False) -> None:
        """
        Deflection is the maximum deflection admitted between two
        consecutive points on a resulting polyline.
        Step is the maximum increment admitted between two
        consecutive points (in 2d space).
        Epsilon is the tolerance beyond which 2 points
        are confused.
        theToFillHoles is the flag defining whether possible holes
        between resulting curves are filled or not
        in case of IntPatch walking theToFillHoles is False
        """

    @overload
    def __init__(self, theOther: IntPatch_TheIWalking) -> None: ...

    def SetTolerance(self, Epsilon: float, Deflection: float, Step: float) -> None:
        """
        Deflection is the maximum deflection admitted between two
        consecutive points on a resulting polyline.
        Step is the maximum increment admitted between two
        consecutive points (in 2d space).
        Epsilon is the tolerance beyond which 2 points
        are confused
        """

    @overload
    def Perform(self, Pnts1: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_PathPoint], Pnts2: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_InteriorPoint], Func: IntPatch_TheSurfFunction, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Reversed: bool = False) -> None:
        """
        Searches a set of polylines starting on a point of Pnts1
        or Pnts2.
        Each point on a resulting polyline verifies F(u,v)=0
        """

    @overload
    def Perform(self, Pnts1: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_PathPoint], Func: IntPatch_TheSurfFunction, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Reversed: bool = False) -> None:
        """
        Searches a set of polylines starting on a point of Pnts1.
        Each point on a resulting polyline verifies F(u,v)=0
        """

    def IsDone(self) -> bool:
        """Returns true if the calculus was successful."""

    def NbLines(self) -> int:
        """
        Returns the number of resulting polylines.
        An exception is raised if IsDone returns False.
        """

    def Value(self, Index: int) -> IntPatch_TheIWLineOfTheIWalking:
        """
        Returns the polyline of range Index.
        An exception is raised if IsDone is False.
        An exception is raised if Index<=0 or Index>NbLines.
        """

    def NbSinglePnts(self) -> int:
        """
        Returns the number of points belonging to Pnts on which no
        line starts or ends.
        An exception is raised if IsDone returns False.
        """

    def SinglePnt(self, Index: int) -> nanoocp.IntSurf.IntSurf_PathPoint:
        """
        Returns the point of range Index .
        An exception is raised if IsDone returns False.
        An exception is raised if Index<=0 or
        Index > NbSinglePnts.
        """

class IntPatch_TheSurfFunction(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, IS: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    @overload
    def __init__(self, PS: nanoocp.Adaptor3d.Adaptor3d_Surface | None, IS: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_TheSurfFunction) -> None: ...

    @overload
    def Set(self, PS: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def Set(self, Tolerance: float) -> None: ...

    def SetImplicitSurface(self, IS: nanoocp.IntSurf.IntSurf_Quadric) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Root(self) -> float: ...

    def Tolerance(self) -> float:
        """
        Returns the value Tol so that if std::abs(Func.Root())<Tol
        the function is considered null.
        """

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def IsTangent(self) -> bool: ...

    def Direction3d(self) -> nanoocp.gp.gp_Vec: ...

    def Direction2d(self) -> nanoocp.gp.gp_Dir2d: ...

    def PSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def ISurface(self) -> nanoocp.IntSurf.IntSurf_Quadric: ...

class IntPatch_WLine(IntPatch_PointLine):
    """
    Definition of set of points as a result of the intersection
    between 2 parametrised patches.
    """

    @overload
    def __init__(self, Line: nanoocp.IntSurf.IntSurf_LineOn2S | None, Tang: bool) -> None:
        """
        Creates a WLine as an intersection when the
        transitions are Undecided.
        """

    @overload
    def __init__(self, Line: nanoocp.IntSurf.IntSurf_LineOn2S | None, Tang: bool, Trans1: nanoocp.IntSurf.IntSurf_TypeTrans, Trans2: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """
        Creates a WLine as an intersection when the
        transitions are In or Out.
        """

    @overload
    def __init__(self, Line: nanoocp.IntSurf.IntSurf_LineOn2S | None, Tang: bool, Situ1: nanoocp.IntSurf.IntSurf_Situation, Situ2: nanoocp.IntSurf.IntSurf_Situation) -> None:
        """
        Creates a WLine as an intersection when the
        transitions are Touch.
        """

    @overload
    def __init__(self, theOther: IntPatch_WLine) -> None: ...

    class IntPatch_WLType(enum.IntEnum):
        """Enumeration of ways of WLine creation."""

        IntPatch_WLUnknown = 0

        IntPatch_WLImpImp = 1

        IntPatch_WLImpPrm = 2

        IntPatch_WLPrmPrm = 3

    IntPatch_WLUnknown: IntPatch_WLine.IntPatch_WLType = IntPatch_WLType.IntPatch_WLUnknown

    IntPatch_WLImpImp: IntPatch_WLine.IntPatch_WLType = IntPatch_WLType.IntPatch_WLImpImp

    IntPatch_WLImpPrm: IntPatch_WLine.IntPatch_WLType = IntPatch_WLType.IntPatch_WLImpPrm

    IntPatch_WLPrmPrm: IntPatch_WLine.IntPatch_WLType = IntPatch_WLType.IntPatch_WLPrmPrm

    def AddVertex(self, Pnt: IntPatch_Point, theIsPrepend: bool = False) -> None:
        """
        Adds a vertex in the list. If theIsPrepend == TRUE the new
        vertex will be added before the first element of vertices sequence.
        Otherwise, to the end of the sequence
        """

    def SetPoint(self, Index: int, Pnt: IntPatch_Point) -> None:
        """Set the Point of index <Index> in the LineOn2S"""

    def Replace(self, Index: int, Pnt: IntPatch_Point) -> None:
        """
        Replaces the element of range Index in the list
        of points.
        The exception OutOfRange is raised when
        Index <= 0 or Index > NbVertex.
        """

    def SetFirstPoint(self, IndFirst: int) -> None: ...

    def SetLastPoint(self, IndLast: int) -> None: ...

    def NbPnts(self) -> int:
        """Returns the number of intersection points."""

    def Point(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """Returns the intersection point of range Index."""

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the line has a known First point.
        This point is given by the method FirstPoint().
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the line has a known Last point.
        This point is given by the method LastPoint().
        """

    @overload
    def FirstPoint(self) -> tuple[IntPatch_Point, int]:
        """
        Returns the Point corresponding to the FirstPoint.
        Indfirst is the index of the first in the list
        of vertices.
        """

    @overload
    def FirstPoint(self) -> IntPatch_Point:
        """Returns the Point corresponding to the FirstPoint."""

    @overload
    def LastPoint(self) -> tuple[IntPatch_Point, int]:
        """
        Returns the Point corresponding to the LastPoint.
        Indlast is the index of the last in the list
        of vertices.
        """

    @overload
    def LastPoint(self) -> IntPatch_Point:
        """Returns the Point corresponding to the LastPoint."""

    def NbVertex(self) -> int:
        """Returns number of vertices (IntPatch_Point) of the line"""

    def Vertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ChangeVertex(self, Index: int) -> IntPatch_Point:
        """Returns the vertex of range Index on the line."""

    def ComputeVertexParameters(self, Tol: float) -> None:
        """
        Set the parameters of all the vertex on the line.
        if a vertex is already in the line,
        its parameter is modified
        else a new point in the line is inserted.
        """

    def Curve(self) -> nanoocp.IntSurf.IntSurf_LineOn2S:
        """Returns set of intersection points"""

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

    def SetPeriod(self, pu1: float, pv1: float, pu2: float, pv2: float) -> None: ...

    def U1Period(self) -> float: ...

    def V1Period(self) -> float: ...

    def U2Period(self) -> float: ...

    def V2Period(self) -> float: ...

    def SetArcOnS1(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def HasArcOnS1(self) -> bool: ...

    def GetArcOnS1(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def SetArcOnS2(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def HasArcOnS2(self) -> bool: ...

    def GetArcOnS2(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def ClearVertexes(self) -> None:
        """Removes vertices from the line (i.e. cleans svtx member)"""

    def RemoveVertex(self, theIndex: int) -> None:
        """Removes single vertex from the line"""

    def InsertVertexBefore(self, theIndex: int, thePnt: IntPatch_Point) -> None: ...

    def Dump(self, theMode: int) -> None:
        """
        if (theMode == 0) then prints the information about WLine
        if (theMode == 1) then prints the list of 3d-points
        if (theMode == 2) then prints the list of 2d-points on the 1st surface
        Otherwise, prints list of 2d-points on the 2nd surface
        """

    def EnablePurging(self, theIsEnabled: bool) -> None:
        """Allows or forbids purging of existing WLine"""

    def IsPurgingAllowed(self) -> bool:
        """Returns TRUE if purging is allowed or forbidden for existing WLine"""

    def GetCreatingWay(self) -> IntPatch_WLine.IntPatch_WLType:
        """Returns the way of <*this> creation."""

    def SetCreatingWayInfo(self, theAlgo: IntPatch_WLine.IntPatch_WLType) -> None:
        """Sets the info about the way of <*this> creation."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IntPatch_WLineTool:
    """
    IntPatch_WLineTool provides set of static methods related to walking lines.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPatch_WLineTool) -> None: ...

    @staticmethod
    def ComputePurgedWLine(theWLine: IntPatch_WLine | None, theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theDom1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, theDom2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> IntPatch_WLine:
        """
        I
        Removes equal points (leave one of equal points) from theWLine
        and recompute vertex parameters.

        II
        Removes point out of borders in case of non periodic surfaces.

        III
        Removes exceed points using tube criteria:
        delete 7D point if it lies near to expected lines in 2d and 3d.
        Each task (2d, 2d, 3d) have its own tolerance and checked separately.

        Returns new WLine or null WLine if the number
        of the points is less than 2.
        """

    @staticmethod
    def JoinWLines(theSlin: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line], theSPnt: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Point], theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theTol3D: float) -> None:
        """
        Joins all WLines from theSlin to one if it is possible and records
        the result into theSlin again. Lines will be kept to be split if:
        a) they are separated (has no common points);
        b) resulted line (after joining) go through seam-edges or surface boundaries.

        In addition, if points in theSPnt lies at least in one of the line in theSlin,
        this point will be deleted.
        """

# C++ typedef aliases
IntPatch_SearchPnt = nanoocp.Intf.Intf_InterferencePolygon2d

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IntPatch
IntPatch_SequenceOfLine = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Line]
IntPatch_SequenceOfPoint = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntPatch.IntPatch_Point]
