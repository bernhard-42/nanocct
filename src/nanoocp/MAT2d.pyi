"""OCCT package MAT2d (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.Bisector
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.MAT
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class MAT2d_BiInt:
    """BiInt is a set of two integers."""

    @overload
    def __init__(self, I1: int, I2: int) -> None: ...

    @overload
    def __init__(self, theOther: MAT2d_BiInt) -> None: ...

    @overload
    def FirstIndex(self) -> int: ...

    @overload
    def FirstIndex(self, I1: int) -> None: ...

    @overload
    def SecondIndex(self) -> int: ...

    @overload
    def SecondIndex(self, I2: int) -> None: ...

    def IsEqual(self, B: MAT2d_BiInt) -> bool: ...

    def __eq__(self, B: MAT2d_BiInt) -> bool: ...

    def __hash__(self) -> int: ...

class MAT2d_Connexion(nanoocp.Standard.Standard_Transient):
    """
    A Connexion links two lines of items in a set
    of lines. It contains two points and their paramatric
    definitions on the lines.
    The items can be points or curves.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LineA: int, LineB: int, ItemA: int, ItemB: int, Distance: float, ParameterOnA: float, ParameterOnB: float, PointA: nanoocp.gp.gp_Pnt2d, PointB: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, theOther: MAT2d_Connexion) -> None: ...

    @overload
    def IndexFirstLine(self) -> int:
        """Returns the Index on the first line."""

    @overload
    def IndexFirstLine(self, anIndex: int) -> None: ...

    @overload
    def IndexSecondLine(self) -> int:
        """Returns the Index on the Second line."""

    @overload
    def IndexSecondLine(self, anIndex: int) -> None: ...

    @overload
    def IndexItemOnFirst(self) -> int:
        """Returns the Index of the item on the first line."""

    @overload
    def IndexItemOnFirst(self, anIndex: int) -> None: ...

    @overload
    def IndexItemOnSecond(self) -> int:
        """Returns the Index of the item on the second line."""

    @overload
    def IndexItemOnSecond(self, anIndex: int) -> None: ...

    @overload
    def ParameterOnFirst(self) -> float:
        """Returns the parameter of the point on the firstline."""

    @overload
    def ParameterOnFirst(self, aParameter: float) -> None: ...

    @overload
    def ParameterOnSecond(self) -> float:
        """Returns the parameter of the point on the secondline."""

    @overload
    def ParameterOnSecond(self, aParameter: float) -> None: ...

    @overload
    def PointOnFirst(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the point on the firstline."""

    @overload
    def PointOnFirst(self, aPoint: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def PointOnSecond(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the point on the secondline."""

    @overload
    def PointOnSecond(self, aPoint: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def Distance(self) -> float:
        """Returns the distance between the two points."""

    @overload
    def Distance(self, aDistance: float) -> None: ...

    def Reverse(self) -> MAT2d_Connexion:
        """
        Returns the reverse connexion of <me>.
        the firstpoint is the secondpoint.
        the secondpoint is the firstpoint.
        """

    def IsAfter(self, aConnexion: MAT2d_Connexion | None, aSense: float) -> bool:
        """
        Returns <True> if my firstPoint is on the same line
        than the firstpoint of <aConnexion> and my firstpoint
        is after the firstpoint of <aConnexion> on the line.
        <aSense> = 1 if <aConnexion> is on the Left of its
        firstline, else <aSense> = -1.
        """

    def Dump(self, Deep: int = 0, Offset: int = 0) -> None:
        """Print <me>."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT2d_Circuit(nanoocp.Standard.Standard_Transient):
    """
    Constructs a circuit on a set of lines.
    EquiCircuit gives a Circuit passing by all the lines
    in a set and all the connexions of the minipath associated.
    """

    @overload
    def __init__(self, aJoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: MAT2d_Circuit) -> None: ...

    def Perform(self, aFigure: nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom2d.Geom2d_Geometry]], IsClosed: nanoocp.NCollection.NCollection_Sequence[bool], IndRefLine: int, Trigo: bool) -> None: ...

    def NumberOfItems(self) -> int:
        """Returns the Number of Items ."""

    def Value(self, Index: int) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Returns the item at position <Index> in <me>."""

    def LineLength(self, IndexLine: int) -> int:
        """Returns the number of items on the line <IndexLine>."""

    def RefToEqui(self, IndLine: int, IndCurve: int) -> nanoocp.NCollection.NCollection_Sequence[int]:
        """
        Returns the set of index of the items in <me>corresponding
        to the curve <IndCurve> on the line <IndLine> from the
        initial figure.
        """

    def Connexion(self, Index: int) -> MAT2d_Connexion:
        """Returns the Connexion on the item <Index> in me."""

    def ConnexionOn(self, Index: int) -> bool:
        """
        Returns <True> is there is a connexion on the item <Index>
        in <me>.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT2d_CutCurve:
    """
    Cuts a curve at the extremas of curvature
    and at the inflections. Constructs a trimmed
    Curve for each interval.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: MAT2d_CutCurve) -> None: ...

    def Perform(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """
        Cuts a curve at the extremas of curvature
        and at the inflections.
        """

    def UnModified(self) -> bool:
        """Returns True if the curve is not cut."""

    def NbCurves(self) -> int:
        """
        Returns the number of curves.
        it's always greatest than 2.

        raises if the Curve is UnModified;
        """

    def Value(self, Index: int) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """
        Returns the Indexth curve.
        raises if Index not in the range [1,NbCurves()]
        """

class MAT2d_Mat2d:
    """
    this class contains the generic algorithm of
    computation of the bisecting locus.
    """

    @overload
    def __init__(self, IsOpenResult: bool = False) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: MAT2d_Mat2d) -> None: ...

    def CreateMat(self, aTool: MAT2d_Tool2d) -> None:
        """Algorithm of computation of the bisecting locus."""

    def CreateMatOpen(self, aTool: MAT2d_Tool2d) -> None:
        """
        Algorithm of computation of the bisecting locus for
        open wire.
        """

    def IsDone(self) -> bool:
        """Returns <TRUE> if CreateMat has succeeded."""

    def Init(self) -> None:
        """
        Initialize an iterator on the set of the roots
        of the trees of bisectors.
        """

    def More(self) -> bool:
        """Return False if there is no more roots."""

    def Next(self) -> None:
        """Move to the next root."""

    def Bisector(self) -> nanoocp.MAT.MAT_Bisector:
        """Returns the current root."""

    def SemiInfinite(self) -> bool:
        """
        Returns True if there are semi_infinite bisectors.
        So there is a tree for each semi_infinte bisector.
        """

    def NumberOfBisectors(self) -> int:
        """Returns the total number of bisectors."""

class MAT2d_MiniPath:
    """
    MiniPath computes a path to link all the lines in
    a set of lines. The path is described as a set of
    connexions.

    The set of connexions can be seen as an arbitrary Tree.
    The node of the tree are the lines. The arcs of the
    tree are the connexions. The ancestror of a line is
    the connexion which ends on it. The children of a line
    are the connexions which start on it.

    The children of a line are ordered by the relation
    <IsAfter> defined on the connexions.
    (See MAT2s_Connexion.cdl).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MAT2d_MiniPath) -> None: ...

    def Perform(self, Figure: nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom2d.Geom2d_Geometry]], IndStart: int, Sense: bool) -> None:
        """
        Computes the path to link the lines in <Figure>.
        the path starts on the line of index <IndStart>
        <Sense> = True if the Circuit turns in the
        trigonometric sense.
        """

    def RunOnConnexions(self) -> None:
        """
        Run on the set of connexions to compute the path.
        the path is an exploration of the tree which contains
        the connexions and their reverses.
        if the tree of connexions is
        A
        / |
        B  E
        / |  |
        C  D  F

        the path is A->B, B->C, C->B, B->D, D->B, B->A, A->E,
        E->F, F->E, E->A.
        """

    def Path(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT2d.MAT2d_Connexion]:
        """
        Returns the sequence of connexions corresponding to
        the path.
        """

    def IsConnexionsFrom(self, Index: int) -> bool:
        """
        Returns <True> if there is one Connexion which starts
        on line designed by <Index>.
        """

    def ConnexionsFrom(self, Index: int) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT2d.MAT2d_Connexion]:
        """
        Returns the connexions which start on line
        designed by <Index>.
        """

    def IsRoot(self, Index: int) -> bool:
        """
        Returns <True> if the line designed by <Index> is
        the root.
        """

    def Father(self, Index: int) -> MAT2d_Connexion:
        """
        Returns the connexion which ends on line
        designed by <Index>.
        """

class MAT2d_Tool2d:
    """
    Set of the methods useful for the MAT's computation.
    Tool2d contains the geometry of the bisecting locus.
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor."""

    @overload
    def __init__(self, theOther: MAT2d_Tool2d) -> None: ...

    def Sense(self, aside: nanoocp.MAT.MAT_Side) -> None:
        """<aSide> defines the side of the computation of the map."""

    def SetJoinType(self, aJoinType: nanoocp.GeomAbs.GeomAbs_JoinType) -> None: ...

    def InitItems(self, aCircuit: MAT2d_Circuit | None) -> None:
        """
        InitItems cuts the line in Items.
        this Items are the geometrics representations of
        the BasicElts from MAT.
        """

    def NumberOfItems(self) -> int:
        """Returns the Number of Items ."""

    def ToleranceOfConfusion(self) -> float:
        """Returns tolerance to test the confusion of two points."""

    def FirstPoint(self, anitem: int) -> tuple[int, float]:
        """
        Creates the point at the origin of the bisector between
        anitem and the previous item.
        dist is the distance from the FirstPoint to <anitem>.
        Returns the index of this point in <theGeomPnts>.
        """

    def TangentBefore(self, anitem: int, IsOpenResult: bool) -> int:
        """
        Creates the Tangent at the end of the Item defined
        by <anitem>. Returns the index of this vector in
        <theGeomVecs>
        """

    def TangentAfter(self, anitem: int, IsOpenResult: bool) -> int:
        """
        Creates the Reversed Tangent at the origin of the Item
        defined by <anitem>. Returns the index of this vector in
        <theGeomVecs>
        """

    def Tangent(self, bisector: int) -> int:
        """
        Creates the Tangent at the end of the bisector defined
        by <bisector>. Returns the index of this vector in
        <theGeomVecs>
        """

    def CreateBisector(self, abisector: nanoocp.MAT.MAT_Bisector | None) -> None:
        """Creates the geometric bisector defined by <abisector>."""

    @overload
    def TrimBisector(self, abisector: nanoocp.MAT.MAT_Bisector | None) -> bool:
        """
        Trims the geometric bisector by the <firstparameter>
        of <abisector>.
        If the parameter is out of the bisector, Return FALSE.
        else Return True.
        """

    @overload
    def TrimBisector(self, abisector: nanoocp.MAT.MAT_Bisector | None, apoint: int) -> bool:
        """
        Trims the geometric bisector by the point of index
        <apoint> in <theGeomPnts>.
        If the point is out of the bisector, Return FALSE.
        else Return True.
        """

    def IntersectBisector(self, bisectorone: nanoocp.MAT.MAT_Bisector | None, bisectortwo: nanoocp.MAT.MAT_Bisector | None) -> tuple[float, int]:
        """
        Computes the point of intersection between the
        bisectors defined by <bisectorone> and
        <bisectortwo> .
        If this point exists, <intpnt> is its index
        in <theGeomPnts> and Return the distance of the point
        from the bisector else Return <RealLast>.
        """

    def Distance(self, abisector: nanoocp.MAT.MAT_Bisector | None, param1: float, param2: float) -> float:
        """
        Returns the distance between the two points designed
        by their parameters on <abisector>.
        """

    def Dump(self, bisector: int, erease: int) -> None:
        """
        displays information about the bisector defined by
        <bisector>.
        """

    def GeomBis(self, Index: int) -> nanoocp.Bisector.Bisector_Bisec:
        """
        Returns the <Bisec> of index <Index> in
        <theGeomBisectors>.
        """

    def GeomElt(self, Index: int) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Returns the Geometry of index <Index> in <theGeomElts>."""

    def GeomPnt(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """Returns the point of index <Index> in the <theGeomPnts>."""

    def GeomVec(self, Index: int) -> nanoocp.gp.gp_Vec2d:
        """
        Returns the vector of index <Index> in the
        <theGeomVecs>.
        """

    def Circuit(self) -> MAT2d_Circuit: ...

    def BisecFusion(self, Index1: int, Index2: int) -> None: ...

    def ChangeGeomBis(self, Index: int) -> nanoocp.Bisector.Bisector_Bisec:
        """
        Returns the <Bisec> of index <Index> in
        <theGeomBisectors>.
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.MAT2d
MAT2d_SequenceOfConnexion = nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT2d.MAT2d_Connexion]
MAT2d_SequenceOfSequenceOfGeometry = nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom2d.Geom2d_Geometry]]
