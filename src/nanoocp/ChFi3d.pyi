"""OCCT package ChFi3d (toolkit TKFillet)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BRepAdaptor
import nanoocp.BRepBlend
import nanoocp.Bnd
import nanoocp.ChFiDS
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomAdaptor
import nanoocp.GeomFill
import nanoocp.IntSurf
import nanoocp.Law
import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.TopOpeBRepBuild
import nanoocp.TopOpeBRepDS
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.math


class ChFi3d_FilletShape(enum.IntEnum):
    """
    Lists the types of fillet shapes. These include the following:
    -   ChFi3d_Rational (default value), which is the
    standard NURBS representation of circles,
    -   ChFi3d_QuasiAngular, which is a NURBS
    representation of circles where the parameters
    match those of the circle,
    -   ChFi3d_Polynomial, which corresponds to a
    polynomial approximation of circles. This type
    facilitates the implementation of the construction algorithm.
    """

    ChFi3d_Rational = 0

    ChFi3d_QuasiAngular = 1

    ChFi3d_Polynomial = 2

ChFi3d_Rational: ChFi3d_FilletShape = ChFi3d_FilletShape.ChFi3d_Rational

ChFi3d_QuasiAngular: ChFi3d_FilletShape = ChFi3d_FilletShape.ChFi3d_QuasiAngular

ChFi3d_Polynomial: ChFi3d_FilletShape = ChFi3d_FilletShape.ChFi3d_Polynomial

class ChFi3d:
    """creation of spatial fillets on a solid."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFi3d) -> None: ...

    @staticmethod
    def DefineConnectType(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, SinTol: float, CorrectPoint: bool) -> nanoocp.ChFiDS.ChFiDS_TypeOfConcavity:
        """Defines the type of concavity in the edge of connection of two faces"""

    @staticmethod
    def IsTangentFaces(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace1: nanoocp.TopoDS.TopoDS_Face, theFace2: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_G1) -> bool:
        """Returns true if theEdge between theFace1 and theFace2 is tangent"""

    @staticmethod
    def ConcaveSide(S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[int, nanoocp.TopAbs.TopAbs_Orientation, nanoocp.TopAbs.TopAbs_Orientation]:
        """
        Returns Reversed in Or1 and(or) Or2 if
        the concave edge defined by the interior of faces F1 and F2,
        in the neighbourhood of their boundary E is of the edge opposite to the
        normal of their surface support. The orientation of
        faces is not taken into consideration in the calculation. The
        function returns 0 if the calculation fails (tangence),
        if not, it returns the number of choice of the fillet
        or chamfer corresponding to the orientations calculated
        and to the tangent to the guide line read in E.
        """

    @overload
    @staticmethod
    def NextSide(OrSave1: nanoocp.TopAbs.TopAbs_Orientation, OrSave2: nanoocp.TopAbs.TopAbs_Orientation, ChoixSauv: int) -> tuple[int, nanoocp.TopAbs.TopAbs_Orientation, nanoocp.TopAbs.TopAbs_Orientation]:
        """
        Same as ConcaveSide, but the orientations are
        logically deduced from the result of the call of
        ConcaveSide on the first pair of faces of the fillet or
        chamnfer.
        """

    @overload
    @staticmethod
    def NextSide(OrSave: nanoocp.TopAbs.TopAbs_Orientation, OrFace: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Same as the other NextSide, but the calculation is done
        on an edge only.
        """

    @staticmethod
    def SameSide(Or: nanoocp.TopAbs.TopAbs_Orientation, OrSave1: nanoocp.TopAbs.TopAbs_Orientation, OrSave2: nanoocp.TopAbs.TopAbs_Orientation, OrFace1: nanoocp.TopAbs.TopAbs_Orientation, OrFace2: nanoocp.TopAbs.TopAbs_Orientation) -> bool:
        """
        Enables to determine while processing an angle, if
        two fillets or chamfers constituting a face have
        identic or opposed concave edges.
        """

class ChFi3d_Builder:
    """
    Root class for calculation of surfaces (fillets,
    chamfers) destined to smooth edges of
    a gap on a Shape and the reconstruction of the Shape.
    """

    def SetParams(self, Tang: float, Tesp: float, T2d: float, TApp3d: float, TolApp2d: float, Fleche: float) -> None: ...

    def SetContinuity(self, InternalContinuity: nanoocp.GeomAbs.GeomAbs_Shape, AngularTolerance: float) -> None: ...

    def Remove(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """extracts from the list the contour containing edge E."""

    def Contains(self, E: nanoocp.TopoDS.TopoDS_Edge) -> int:
        """
        gives the number of the contour containing E or 0
        if E does not belong to any contour.
        """

    def Contains__int(self, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[int, int]:
        """
        Contains__int: the C++ overload Contains(const TopoDS_Edge &, int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        gives the number of the contour containing E or 0
        if E does not belong to any contour.
        Sets in IndexInSpine the index of E in the contour if it's found
        """

    def NbElements(self) -> int:
        """
        gives the number of disjoint contours on which
        the fillets are calculated
        """

    def Value(self, I: int) -> nanoocp.ChFiDS.ChFiDS_Spine:
        """
        gives the n'th set of edges (contour)
        if I >NbElements()
        """

    def Length(self, IC: int) -> float:
        """returns the length of the contour of index IC."""

    def FirstVertex(self, IC: int) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        returns the First vertex V of
        the contour of index IC.
        """

    def LastVertex(self, IC: int) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        returns the Last vertex V of
        the contour of index IC.
        """

    def Abscissa(self, IC: int, V: nanoocp.TopoDS.TopoDS_Vertex) -> float:
        """
        returns the abscissa of the vertex V on
        the contour of index IC.
        """

    def RelativeAbscissa(self, IC: int, V: nanoocp.TopoDS.TopoDS_Vertex) -> float:
        """
        returns the relative abscissa([0.,1.]) of the
        vertex V on the contour of index IC.
        """

    def ClosedAndTangent(self, IC: int) -> bool:
        """
        returns true if the contour of index IC is closed
        an tangent.
        """

    def Closed(self, IC: int) -> bool:
        """returns true if the contour of index IC is closed"""

    def Compute(self) -> None:
        """
        general calculation of geometry on all edges,
        topologic reconstruction.
        """

    def IsDone(self) -> bool:
        """returns True if the computation is success"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        if (Isdone()) makes the result.
        if (!Isdone())
        """

    def Generated(self, EouV: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Advanced function for the history"""

    def NbFaultyContours(self) -> int:
        """
        Returns the number of contours on which the calculation
        has failed.
        """

    def FaultyContour(self, I: int) -> int:
        """
        Returns the number of I'th contour on which the calculation
        has failed.
        """

    def NbComputedSurfaces(self, IC: int) -> int:
        """Returns the number of surfaces calculated on the contour IC."""

    def ComputedSurface(self, IC: int, IS: int) -> nanoocp.Geom.Geom_Surface:
        """Returns the IS'th surface calculated on the contour IC."""

    def NbFaultyVertices(self) -> int:
        """
        Returns the number of vertices on which the calculation
        has failed.
        """

    def FaultyVertex(self, IV: int) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the IV'th vertex on which the calculation has failed."""

    def HasResult(self) -> bool:
        """returns True if a partial result has been calculated"""

    def BadShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        if (HasResult()) returns partial result
        if (!HasResult())
        """

    def StripeStatus(self, IC: int) -> nanoocp.ChFiDS.ChFiDS_ErrorStatus:
        """
        for the stripe IC ,indication on the cause
        of failure WalkingFailure,TwistedSurface,Error, Ok
        """

    def Reset(self) -> None:
        """
        Reset all results of compute and returns the algorithm
        in the state of the last acquisition to enable modification of contours or areas.
        """

    def Builder(self) -> nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder:
        """Returns the Builder of topologic operations."""

    def SplitKPart(self, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, SetData: nanoocp.NCollection.NCollection_Sequence[nanoocp.ChFiDS.ChFiDS_SurfData], Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Iedge: int, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> tuple[bool, bool, bool]:
        """
        Method, implemented in the inheritants, calculates
        the elements of construction of the surface (fillet or
        chamfer).
        """

    def PerformTwoCornerbyInter(self, Index: int) -> bool: ...

class ChFi3d_ChBuilder(ChFi3d_Builder):
    """construction tool for 3D chamfers on edges (on a solid)."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, Ta: float = 0.01) -> None:
        """
        initializes the Builder with the Shape <S> for the
        computation of chamfers
        """

    @overload
    def __init__(self, theOther: ChFi3d_ChBuilder) -> None: ...

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        initializes a contour with the edge <E> as first
        (the next are found by propagation ).
        The two distances (parameters of the chamfer) must
        be set after.
        if the edge <E> has more than 2 adjacent faces
        """

    @overload
    def Add(self, Dis: float, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        initializes a new contour with the edge <E> as first
        (the next are found by propagation ), and the
        distance <Dis>
        if the edge <E> has more than 2 adjacent faces
        """

    @overload
    def Add(self, Dis1: float, Dis2: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        initializes a new contour with the edge <E> as first
        (the next are found by propagation ), and the
        distance <Dis1> and <Dis2>
        if the edge <E> has more than 2 adjacent faces
        """

    def SetDist(self, Dis: float, IC: int, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        set the distance <Dis> of the fillet
        contour of index <IC> in the DS with <Dis> on <F>.
        if the face <F> is not one of common faces
        of an edge of the contour <IC>
        """

    def GetDist(self, IC: int) -> float:
        """
        gives the distances <Dis> of the fillet
        contour of index <IC> in the DS
        """

    def SetDists(self, Dis1: float, Dis2: float, IC: int, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        set the distances <Dis1> and <Dis2> of the fillet
        contour of index <IC> in the DS with <Dis1> on <F>.
        if the face <F> is not one of common faces
        of an edge of the contour <IC>
        """

    def Dists(self, IC: int) -> tuple[float, float]:
        """
        gives the distances <Dis1> and <Dis2> of the fillet
        contour of index <IC> in the DS
        """

    def AddDA(self, Dis: float, Angle: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        initializes a new contour with the edge <E> as first
        (the next are found by propagation ), and the
        distance <Dis1> and <Angle>
        if the edge <E> has more than 2 adjacent faces
        """

    def SetDistAngle(self, Dis: float, Angle: float, IC: int, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        set the distance <Dis> and <Angle> of the fillet
        contour of index <IC> in the DS with <Dis> on <F>.
        if the face <F> is not one of common faces
        of an edge of the contour <IC>
        """

    def GetDistAngle(self, IC: int) -> tuple[float, float]:
        """
        gives the distances <Dis> and <Angle> of the fillet
        contour of index <IC> in the DS
        """

    def SetMode(self, theMode: nanoocp.ChFiDS.ChFiDS_ChamfMode) -> None:
        """set the mode of shamfer"""

    def IsChamfer(self, IC: int) -> nanoocp.ChFiDS.ChFiDS_ChamfMethod:
        """renvoi la methode des chanfreins utilisee"""

    def Mode(self) -> nanoocp.ChFiDS.ChFiDS_ChamfMode:
        """returns the mode of chamfer used"""

    def ResetContour(self, IC: int) -> None:
        """Reset tous rayons du contour IC."""

    def Simulate(self, IC: int) -> None: ...

    def NbSurf(self, IC: int) -> int: ...

    def Sect(self, IC: int, IS: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.ChFiDS.ChFiDS_CircSection]: ...

    @overload
    def SimulSurf(self, Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Or2: nanoocp.TopAbs.TopAbs_Orientation, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: nanoocp.math.math_Vector) -> tuple[nanoocp.ChFiDS.ChFiDS_SurfData, bool, float, float]: ...

    @overload
    def SimulSurf(self, Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Or1: nanoocp.TopAbs.TopAbs_Orientation, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: nanoocp.math.math_Vector) -> tuple[nanoocp.ChFiDS.ChFiDS_SurfData, bool, float, float]: ...

    @overload
    def SimulSurf(self, Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Or1: nanoocp.TopAbs.TopAbs_Orientation, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Or2: nanoocp.TopAbs.TopAbs_Orientation, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP1: bool, RecRst1: bool, RecP2: bool, RecRst2: bool, Soldep: nanoocp.math.math_Vector) -> tuple[nanoocp.ChFiDS.ChFiDS_SurfData, bool, bool, float, float]: ...

    @overload
    def PerformSurf(self, Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.ChFiDS.ChFiDS_SurfData], Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecOnS1: bool, RecOnS2: bool, Soldep: nanoocp.math.math_Vector) -> tuple[bool, float, float, int, int]:
        """
        Methode, implemented in inheritants, calculates
        the elements of construction of the surface (fillet
        or chamfer).
        """

    @overload
    def PerformSurf(self, Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.ChFiDS.ChFiDS_SurfData], Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Or2: nanoocp.TopAbs.TopAbs_Orientation, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: nanoocp.math.math_Vector) -> tuple[bool, float, float]:
        """
        Method, implemented in the inheritants, calculates
        the elements of construction of the surface (fillet
        or chamfer) contact edge/face.
        """

    @overload
    def PerformSurf(self, Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.ChFiDS.ChFiDS_SurfData], Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Or1: nanoocp.TopAbs.TopAbs_Orientation, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: nanoocp.math.math_Vector) -> tuple[bool, float, float]:
        """
        Method, implemented in inheritants, calculates
        the elements of construction of the surface (fillet
        or chamfer) contact edge/face.
        """

    @overload
    def PerformSurf(self, Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.ChFiDS.ChFiDS_SurfData], Guide: nanoocp.ChFiDS.ChFiDS_ElSpine | None, Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, Choix: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I1: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref1: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref1: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Or1: nanoocp.TopAbs.TopAbs_Orientation, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, I2: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, PC2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Sref2: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, PCref2: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None, Or2: nanoocp.TopAbs.TopAbs_Orientation, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP1: bool, RecRst1: bool, RecP2: bool, RecRst2: bool, Soldep: nanoocp.math.math_Vector) -> tuple[bool, bool, float, float]:
        """
        Method, implemented in inheritants, calculates
        the elements of construction of the surface (fillet
        or chamfer) contact edge/edge.
        """

class ChFi3d_FilBuilder(ChFi3d_Builder):
    """Tool of construction of fillets 3d on edges (on a solid)."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, FShape: ChFi3d_FilletShape = ChFi3d_FilletShape.ChFi3d_Rational, Ta: float = 0.01) -> None: ...

    @overload
    def __init__(self, theOther: ChFi3d_FilBuilder) -> None: ...

    def SetFilletShape(self, FShape: ChFi3d_FilletShape) -> None:
        """Sets the type of fillet surface."""

    def GetFilletShape(self) -> ChFi3d_FilletShape:
        """Returns the type of fillet surface."""

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        initialisation of a contour with the first edge
        (the following are found by propagation).
        Attention, you need to start with SetRadius.
        """

    @overload
    def Add(self, Radius: float, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """initialisation of the constant vector the corresponding 1st edge."""

    @overload
    def SetRadius(self, C: nanoocp.Law.Law_Function | None, IC: int, IinC: int) -> None:
        """Set the radius of the contour of index IC."""

    @overload
    def SetRadius(self, Radius: float, IC: int, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Set a constant on edge E of the contour of
        index IC. Since then E is flagged as constant.
        """

    @overload
    def SetRadius(self, Radius: float, IC: int, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """Set a vector on vertex V of the contour of index IC."""

    @overload
    def SetRadius(self, UandR: nanoocp.gp.gp_XY, IC: int, IinC: int) -> None:
        """
        Set a vertex on the point of parameter U in the edge IinC
        of the contour of index IC
        """

    @overload
    def IsConstant(self, IC: int) -> bool:
        """Returns true the contour is flagged as edge constant."""

    @overload
    def IsConstant(self, IC: int, E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns true E is flagged as edge constant."""

    @overload
    def Radius(self, IC: int) -> float:
        """
        Returns the vector if the contour is flagged as edge
        constant.
        """

    @overload
    def Radius(self, IC: int, E: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """Returns the vector if E is flagged as edge constant."""

    def ResetContour(self, IC: int) -> None:
        """Reset all vectors of contour IC."""

    @overload
    def UnSet(self, IC: int, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Extracts the flag constant and the vector of edge E."""

    @overload
    def UnSet(self, IC: int, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """Extracts the vector of the vertex V."""

    def GetBounds(self, IC: int, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns in First and Last extremities of the
        part of variable vector framing E, returns
        False if E is flagged as edge constant.
        """

    def GetLaw(self, IC: int, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.Law.Law_Function:
        """
        Returns the rule of elementary evolution of the
        part to variable vector framing E, returns a
        rule zero if E is flagged as edge constant.
        """

    def SetLaw(self, IC: int, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.Law.Law_Function | None) -> None:
        """
        Sets the rule of elementary evolution of the
        part to variable vector framing E.
        """

    def Simulate(self, IC: int) -> None: ...

    def NbSurf(self, IC: int) -> int: ...

    def Sect(self, IC: int, IS: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.ChFiDS.ChFiDS_CircSection]: ...

class ChFi3d_SearchSing(nanoocp.math.math_FunctionWithDerivative):
    """
    Searches singularities on fillet.
    F(t) = (C1(t) - C2(t)).(C1'(t) - C2'(t));
    """

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_Curve | None, C2: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: ChFi3d_SearchSing) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """
        computes the value of the function <F> for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        computes the derivative <D> of the function
        for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        computes the value <F> and the derivative <D> of the
        function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

def ChFi3d_InPeriod(U: float, UFirst: float, ULast: float, Eps: float) -> float: ...

@overload
def ChFi3d_Boite(p1: nanoocp.gp.gp_Pnt2d, p2: nanoocp.gp.gp_Pnt2d) -> tuple[float, float, float, float]: ...

@overload
def ChFi3d_Boite(p1: nanoocp.gp.gp_Pnt2d, p2: nanoocp.gp.gp_Pnt2d, p3: nanoocp.gp.gp_Pnt2d, p4: nanoocp.gp.gp_Pnt2d) -> tuple[float, float, float, float, float, float]: ...

def ChFi3d_SetPointTolerance(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, box: nanoocp.Bnd.Bnd_Box, IP: int) -> None: ...

@overload
def ChFi3d_EnlargeBox(C: nanoocp.Geom.Geom_Curve | None, wd: float, wf: float, box1: nanoocp.Bnd.Bnd_Box, box2: nanoocp.Bnd.Bnd_Box) -> None: ...

@overload
def ChFi3d_EnlargeBox(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, PC: nanoocp.Geom2d.Geom2d_Curve | None, wd: float, wf: float, box1: nanoocp.Bnd.Bnd_Box, box2: nanoocp.Bnd.Bnd_Box) -> None: ...

@overload
def ChFi3d_EnlargeBox(E: nanoocp.TopoDS.TopoDS_Edge, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], w: float, box: nanoocp.Bnd.Bnd_Box) -> None: ...

@overload
def ChFi3d_EnlargeBox(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, st: nanoocp.ChFiDS.ChFiDS_Stripe | None, sd: nanoocp.ChFiDS.ChFiDS_SurfData | None, b1: nanoocp.Bnd.Bnd_Box, b2: nanoocp.Bnd.Bnd_Box, isfirst: bool) -> None: ...

def ChFi3d_evalconti(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

def ChFi3d_conexfaces(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, EFMap: nanoocp.ChFiDS.ChFiDS_Map) -> None: ...

def ChFi3d_EdgeState(E: nanoocp.TopoDS.TopoDS_Edge, EFMap: nanoocp.ChFiDS.ChFiDS_Map) -> nanoocp.ChFiDS.ChFiDS_State: ...

def ChFi3d_KParticular(Spine: nanoocp.ChFiDS.ChFiDS_Spine | None, IE: int, S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

def ChFi3d_BoundFac(S: nanoocp.BRepAdaptor.BRepAdaptor_Surface, umin: float, umax: float, vmin: float, vmax: float, checknaturalbounds: bool = True) -> None: ...

def ChFi3d_BoundSrf(S: nanoocp.GeomAdaptor.GeomAdaptor_Surface, umin: float, umax: float, vmin: float, vmax: float, checknaturalbounds: bool = True) -> None: ...

def ChFi3d_InterPlaneEdge(Plan: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Sens: bool, tolc: float) -> tuple[bool, float]: ...

def ChFi3d_ExtrSpineCarac(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, cd: nanoocp.ChFiDS.ChFiDS_Stripe | None, i: int, p: float, jf: int, sens: int, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> float: ...

def ChFi3d_CircularSpine(Pdeb: nanoocp.gp.gp_Pnt, Vdeb: nanoocp.gp.gp_Vec, Pfin: nanoocp.gp.gp_Pnt, Vfin: nanoocp.gp.gp_Vec, rad: float) -> tuple[nanoocp.Geom.Geom_Circle, float, float]: ...

def ChFi3d_Spine(pd: nanoocp.gp.gp_Pnt, vd: nanoocp.gp.gp_Vec, pf: nanoocp.gp.gp_Pnt, vf: nanoocp.gp.gp_Vec, R: float) -> nanoocp.Geom.Geom_BezierCurve: ...

@overload
def ChFi3d_mkbound(Fac: nanoocp.Adaptor3d.Adaptor3d_Surface | None, sens1: int, pfac1: nanoocp.gp.gp_Pnt2d, vfac1: nanoocp.gp.gp_Vec2d, sens2: int, pfac2: nanoocp.gp.gp_Pnt2d, vfac2: nanoocp.gp.gp_Vec2d, t3d: float, ta: float) -> tuple[nanoocp.GeomFill.GeomFill_Boundary, nanoocp.Geom2d.Geom2d_Curve]: ...

@overload
def ChFi3d_mkbound(Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, sens1: int, p1: nanoocp.gp.gp_Pnt2d, v1: nanoocp.gp.gp_Vec, sens2: int, p2: nanoocp.gp.gp_Pnt2d, v2: nanoocp.gp.gp_Vec, t3d: float, ta: float) -> tuple[nanoocp.GeomFill.GeomFill_Boundary, nanoocp.Geom2d.Geom2d_Curve]: ...

@overload
def ChFi3d_mkbound(s: nanoocp.Geom.Geom_Surface | None, p1: nanoocp.gp.gp_Pnt2d, p2: nanoocp.gp.gp_Pnt2d, t3d: float, ta: float, isfreeboundary: bool = False) -> nanoocp.GeomFill.GeomFill_Boundary: ...

@overload
def ChFi3d_mkbound(HS: nanoocp.Adaptor3d.Adaptor3d_Surface | None, p1: nanoocp.gp.gp_Pnt2d, p2: nanoocp.gp.gp_Pnt2d, t3d: float, ta: float, isfreeboundary: bool = False) -> nanoocp.GeomFill.GeomFill_Boundary: ...

@overload
def ChFi3d_mkbound(HS: nanoocp.Adaptor3d.Adaptor3d_Surface | None, curv: nanoocp.Geom2d.Geom2d_Curve | None, t3d: float, ta: float, isfreeboundary: bool = False) -> nanoocp.GeomFill.GeomFill_Boundary: ...

def ChFi3d_mkbound__Geom2d_Curve(Fac: nanoocp.Adaptor3d.Adaptor3d_Surface | None, p1: nanoocp.gp.gp_Pnt2d, p2: nanoocp.gp.gp_Pnt2d, t3d: float, ta: float, isfreeboundary: bool = False) -> tuple[nanoocp.GeomFill.GeomFill_Boundary, nanoocp.Geom2d.Geom2d_Curve]:
    """
    ChFi3d_mkbound__Geom2d_Curve: the C++ overload ChFi3d_mkbound(const occ::handle<Adaptor3d_Surface> &, occ::handle<Geom2d_Curve> &, const gp_Pnt2d &, const gp_Pnt2d &, const double, const double, const bool); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def ChFi3d_Coefficient(V3d: nanoocp.gp.gp_Vec, D1u: nanoocp.gp.gp_Vec, D1v: nanoocp.gp.gp_Vec) -> tuple[float, float]: ...

@overload
def ChFi3d_BuildPCurve(p1: nanoocp.gp.gp_Pnt2d, d1: nanoocp.gp.gp_Dir2d, p2: nanoocp.gp.gp_Pnt2d, d2: nanoocp.gp.gp_Dir2d, redresse: bool = True) -> nanoocp.Geom2d.Geom2d_Curve: ...

@overload
def ChFi3d_BuildPCurve(Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, p1: nanoocp.gp.gp_Pnt2d, v1: nanoocp.gp.gp_Vec, p2: nanoocp.gp.gp_Pnt2d, v2: nanoocp.gp.gp_Vec, redresse: bool = False) -> nanoocp.Geom2d.Geom2d_Curve: ...

@overload
def ChFi3d_BuildPCurve(Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, p1: nanoocp.gp.gp_Pnt2d, v1: nanoocp.gp.gp_Vec2d, p2: nanoocp.gp.gp_Pnt2d, v2: nanoocp.gp.gp_Vec2d, redresse: bool = False) -> nanoocp.Geom2d.Geom2d_Curve: ...

def ChFi3d_CheckSameParameter(C3d: nanoocp.Adaptor3d.Adaptor3d_Curve | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, tol3d: float) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]: ...

@overload
def ChFi3d_SameParameter(C3d: nanoocp.Adaptor3d.Adaptor3d_Curve | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, tol3d: float) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]: ...

@overload
def ChFi3d_SameParameter(C3d: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None, Pardeb: float, Parfin: float, tol3d: float) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]: ...

@overload
def ChFi3d_ComputePCurv(C3d: nanoocp.Geom.Geom_Curve | None, UV1: nanoocp.gp.gp_Pnt2d, UV2: nanoocp.gp.gp_Pnt2d, S: nanoocp.Geom.Geom_Surface | None, Pardeb: float, Parfin: float, tol3d: float, reverse: bool = False) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]: ...

@overload
def ChFi3d_ComputePCurv(C3d: nanoocp.Adaptor3d.Adaptor3d_Curve | None, UV1: nanoocp.gp.gp_Pnt2d, UV2: nanoocp.gp.gp_Pnt2d, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Pardeb: float, Parfin: float, tol3d: float, reverse: bool = False) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]: ...

@overload
def ChFi3d_ComputePCurv(UV1: nanoocp.gp.gp_Pnt2d, UV2: nanoocp.gp.gp_Pnt2d, Pardeb: float, Parfin: float, reverse: bool = False) -> nanoocp.Geom2d.Geom2d_Curve: ...

def ChFi3d_IntTraces(fd1: nanoocp.ChFiDS.ChFiDS_SurfData | None, pref1: float, jf1: int, sens1: int, fd2: nanoocp.ChFiDS.ChFiDS_SurfData | None, pref2: float, jf2: int, sens2: int, RefP2d: nanoocp.gp.gp_Pnt2d, Check2dDistance: bool = False, enlarge: bool = False) -> tuple[bool, float, float]: ...

def ChFi3d_IsInFront(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, cd1: nanoocp.ChFiDS.ChFiDS_Stripe | None, cd2: nanoocp.ChFiDS.ChFiDS_Stripe | None, i1: int, i2: int, sens1: int, sens2: int, face: nanoocp.TopoDS.TopoDS_Face, Vtx: nanoocp.TopoDS.TopoDS_Vertex, Check2dDistance: bool = False, enlarge: bool = False) -> tuple[bool, float, float, bool, int, int, bool]: ...

def ChFi3d_ProjectPCurv(HCg: nanoocp.Adaptor3d.Adaptor3d_Curve | None, HSg: nanoocp.Adaptor3d.Adaptor3d_Surface | None, tol3d: float) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]: ...

def ChFi3d_ReparamPcurv(Uf: float, Ul: float) -> nanoocp.Geom2d.Geom2d_Curve: ...

def ChFi3d_ComputeArete(P1: nanoocp.ChFiDS.ChFiDS_CommonPoint, UV1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.ChFiDS.ChFiDS_CommonPoint, UV2: nanoocp.gp.gp_Pnt2d, Surf: nanoocp.Geom.Geom_Surface | None, tol3d: float, tol2d: float, IFlag: int) -> tuple[nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, float, float, float]: ...

def ChFi3d_FilCurveInDS(Icurv: int, Isurf: int, Pcurv: nanoocp.Geom2d.Geom2d_Curve | None, Et: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_SurfaceCurveInterference: ...

def ChFi3d_TrsfTrans(T1: nanoocp.IntSurf.IntSurf_TypeTrans) -> nanoocp.TopAbs.TopAbs_Orientation: ...

def ChFi3d_FilCommonPoint(SP: nanoocp.BRepBlend.BRepBlend_Extremity, TransLine: nanoocp.IntSurf.IntSurf_TypeTrans, Start: bool, CP: nanoocp.ChFiDS.ChFiDS_CommonPoint, Tol: float) -> None: ...

def ChFi3d_SolidIndex(sp: nanoocp.ChFiDS.ChFiDS_Spine | None, DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, MapESo: nanoocp.ChFiDS.ChFiDS_Map, MapESh: nanoocp.ChFiDS.ChFiDS_Map) -> int: ...

def ChFi3d_IndexPointInDS(P1: nanoocp.ChFiDS.ChFiDS_CommonPoint, DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure) -> int: ...

def ChFi3d_FilPointInDS(Et: nanoocp.TopAbs.TopAbs_Orientation, Ic: int, Ip: int, Par: float, IsVertex: bool = False) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_CurvePointInterference: ...

def ChFi3d_FilVertexInDS(Et: nanoocp.TopAbs.TopAbs_Orientation, Ic: int, Ip: int, Par: float) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_CurvePointInterference: ...

def ChFi3d_FilDS(SolidIndex: int, CorDat: nanoocp.ChFiDS.ChFiDS_Stripe | None, DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, reglist: nanoocp.NCollection.NCollection_List[nanoocp.ChFiDS.ChFiDS_Regul], tol3d: float, tol2d: float) -> None: ...

def ChFi3d_StripeEdgeInter(theStripe1: nanoocp.ChFiDS.ChFiDS_Stripe | None, theStripe2: nanoocp.ChFiDS.ChFiDS_Stripe | None, DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, tol2d: float) -> None: ...

def ChFi3d_IndexOfSurfData(V1: nanoocp.TopoDS.TopoDS_Vertex, CD: nanoocp.ChFiDS.ChFiDS_Stripe | None) -> tuple[int, int]: ...

def ChFi3d_EdgeFromV1(V1: nanoocp.TopoDS.TopoDS_Vertex, CD: nanoocp.ChFiDS.ChFiDS_Stripe | None) -> tuple[nanoocp.TopoDS.TopoDS_Edge, int]: ...

def ChFi3d_ConvTol2dToTol3d(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, tol2d: float) -> float: ...

def ChFi3d_ComputeCurves(S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Pardeb: nanoocp.NCollection.NCollection_Array1[float], Parfin: nanoocp.NCollection.NCollection_Array1[float], tol3d: float, tol2d: float, wholeCurv: bool = True) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, float]: ...

def ChFi3d_IntCS(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, p2dS: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float]: ...

@overload
def ChFi3d_ComputesIntPC(Fi1: nanoocp.ChFiDS.ChFiDS_FaceInterference, Fi2: nanoocp.ChFiDS.ChFiDS_FaceInterference, HS1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, HS2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None) -> tuple[float, float]: ...

@overload
def ChFi3d_ComputesIntPC(Fi1: nanoocp.ChFiDS.ChFiDS_FaceInterference, Fi2: nanoocp.ChFiDS.ChFiDS_FaceInterference, HS1: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, HS2: nanoocp.GeomAdaptor.GeomAdaptor_Surface | None, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]: ...

def ChFi3d_BoundSurf(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Fd1: nanoocp.ChFiDS.ChFiDS_SurfData | None, IFaCo1: int, IFaArc1: int) -> nanoocp.GeomAdaptor.GeomAdaptor_Surface: ...

def ChFi3d_SearchFD(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, cd1: nanoocp.ChFiDS.ChFiDS_Stripe | None, cd2: nanoocp.ChFiDS.ChFiDS_Stripe | None, sens1: int, sens2: int, ind1: int, ind2: int, face: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, int, int, float, float, bool, int, int]: ...

def ChFi3d_Parameters(S: nanoocp.Geom.Geom_Surface | None, p3d: nanoocp.gp.gp_Pnt) -> tuple[float, float]: ...

def ChFi3d_TrimCurve(gc: nanoocp.Geom.Geom_Curve | None, FirstP: nanoocp.gp.gp_Pnt, LastP: nanoocp.gp.gp_Pnt) -> nanoocp.Geom.Geom_TrimmedCurve: ...

def ChFi3d_PerformElSpine(continuity: nanoocp.GeomAbs.GeomAbs_Shape, tol: float, IsOffset: bool = False) -> tuple[nanoocp.ChFiDS.ChFiDS_ElSpine, nanoocp.ChFiDS.ChFiDS_Spine]: ...

def ChFi3d_cherche_face1(map: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], F1: nanoocp.TopoDS.TopoDS_Face, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

def ChFi3d_cherche_element(V: nanoocp.TopoDS.TopoDS_Vertex, E1: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge, Vtx: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

def ChFi3d_EvalTolReached(S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, pc1: nanoocp.Geom2d.Geom2d_Curve | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, pc2: nanoocp.Geom2d.Geom2d_Curve | None, C: nanoocp.Geom.Geom_Curve | None) -> float: ...

def ChFi3d_cherche_edge(V: nanoocp.TopoDS.TopoDS_Vertex, E1: nanoocp.NCollection.NCollection_Array1[nanoocp.TopoDS.TopoDS_Shape], F1: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge, Vtx: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

def ChFi3d_nbface(mapVF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

def ChFi3d_edge_common_faces(mapEF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None: ...

def ChFi3d_AngleEdge(Vtx: nanoocp.TopoDS.TopoDS_Vertex, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> float: ...

def ChFi3d_ChercheBordsLibres(myVEMap: nanoocp.ChFiDS.ChFiDS_Map, V1: nanoocp.TopoDS.TopoDS_Vertex, edgelibre1: nanoocp.TopoDS.TopoDS_Edge, edgelibre2: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

def ChFi3d_NbNotDegeneratedEdges(Vtx: nanoocp.TopoDS.TopoDS_Vertex, VEMap: nanoocp.ChFiDS.ChFiDS_Map) -> int: ...

def ChFi3d_NumberOfEdges(Vtx: nanoocp.TopoDS.TopoDS_Vertex, VEMap: nanoocp.ChFiDS.ChFiDS_Map) -> int: ...

def ChFi3d_NumberOfSharpEdges(Vtx: nanoocp.TopoDS.TopoDS_Vertex, VEMap: nanoocp.ChFiDS.ChFiDS_Map, EFmap: nanoocp.ChFiDS.ChFiDS_Map) -> int: ...

def ChFi3d_cherche_vertex(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, vertex: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

def ChFi3d_Couture(F: nanoocp.TopoDS.TopoDS_Face, edgecouture: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

def ChFi3d_CoutureOnVertex(F: nanoocp.TopoDS.TopoDS_Face, V: nanoocp.TopoDS.TopoDS_Vertex, edgecouture: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

def ChFi3d_IsPseudoSeam(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

def ChFi3d_ApproxByC2(C: nanoocp.Geom.Geom_Curve | None) -> nanoocp.Geom.Geom_BSplineCurve: ...

def ChFi3d_IsSmooth(C: nanoocp.Geom.Geom_Curve | None) -> bool: ...
