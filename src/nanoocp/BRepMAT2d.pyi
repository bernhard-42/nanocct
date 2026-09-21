"""OCCT package BRepMAT2d (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.Bisector
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.MAT
import nanoocp.NCollection
import nanoocp.TopoDS
import nanoocp.gp


class BRepMAT2d_BisectingLocus:
    """
    BisectingLocus generates and contains the Bisecting_Locus
    of a set of lines from Geom2d, defined by <ExploSet>.

    If the set of lines contains closed lines:
    ------------------------------------------
    These lines cut the plane in areas.
    One map can be computed for each area.

    Bisecting locus computes a map in an area.
    The area is defined by a side (MAT_Left,MAT_Right)
    on one of the closed lines.

    If the set of lines contains only open lines:
    --------------------------------------------
    the map recovers all the plane.

    Warning: Assume the orientation of the closed lines are
    compatible.

    Assume the explo contains only lines located in the
    area where the bisecting locus will be computed.

    Assume a line don't cross itself or an other line.

    Remark:
    the curves coming from the explorer can be
    decomposed in different parts. It the case for the
    curves other than circles or lines.

    The map of bisecting locus is described by a graph.
    - The BasicsElements correspond to elements on
    the figure described by the Explorer from BRepMAT2d.
    - The Arcs correspond to the bisectors.
    - The Nodes are the extremities of the arcs.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepMAT2d_BisectingLocus) -> None: ...

    def Compute(self, anExplo: BRepMAT2d_Explorer, LineIndex: int = 1, aSide: nanoocp.MAT.MAT_Side = MAT_Side.MAT_Left, aJoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None:
        """
        Computation of the Bisector_Locus in a set of Lines
        defined in <anExplo>.
        The bisecting locus are computed on the side <aSide>
        from the line <LineIndex> in <anExplo>.
        """

    def IsDone(self) -> bool:
        """Returns True if Compute has succeeded."""

    def Graph(self) -> nanoocp.MAT.MAT_Graph:
        """Returns <theGraph> of <me>."""

    def NumberOfContours(self) -> int:
        """Returns the number of contours."""

    def NumberOfElts(self, IndLine: int) -> int:
        """
        Returns the number of BasicElts on the line
        <IndLine>.
        """

    def NumberOfSections(self, IndLine: int, Index: int) -> int:
        """
        Returns the number of sections of a curve.
        this curve is the Indexth curve in the IndLineth contour
        given by anExplo.
        """

    def BasicElt(self, IndLine: int, Index: int) -> nanoocp.MAT.MAT_BasicElt:
        """
        Returns the BasicElts located at the position
        <Index> on the contour designed by <IndLine>.
        Remark: the BasicElts on a contour are sorted.
        """

    @overload
    def GeomElt(self, aBasicElt: nanoocp.MAT.MAT_BasicElt | None) -> nanoocp.Geom2d.Geom2d_Geometry:
        """Returns the geometry linked to the <BasicElt>."""

    @overload
    def GeomElt(self, aNode: nanoocp.MAT.MAT_Node | None) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the geometry of type <gp> linked to
        the <Node>.
        """

    def GeomBis(self, anArc: nanoocp.MAT.MAT_Arc | None) -> tuple[nanoocp.Bisector.Bisector_Bisec, bool]:
        """
        Returns the geometry of type <Bissec>
        linked to the arc <ARC>.
        <Reverse> is False when the FirstNode of <anArc>
        correspond to the first point of geometry.
        """

class BRepMAT2d_Explorer:
    """
    Construct an explorer from wires, face, set of curves
    from Geom2d to compute the bisecting Locus.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aFace: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: BRepMAT2d_Explorer) -> None: ...

    def __iter__(self) -> BRepMAT2d_Explorer:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """Python addition: see __iter__."""

    def Clear(self) -> None:
        """Clear the contents of <me>."""

    def Perform(self, aFace: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def NumberOfContours(self) -> int:
        """Returns the Number of contours."""

    def NumberOfCurves(self, IndexContour: int) -> int:
        """
        Returns the Number of Curves in the Contour number
        <IndexContour>.
        """

    def Init(self, IndexContour: int) -> None:
        """
        Initialisation of an Iterator on the curves of
        the Contour number <IndexContour>.
        """

    def More(self) -> bool:
        """
        Return False if there is no more curves on the Contour
        initialised by the method Init.
        """

    def Next(self) -> None:
        """Move to the next curve of the current Contour."""

    def Value(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns the current curve on the current Contour."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Contour(self, IndexContour: int) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom2d.Geom2d_Curve]: ...

    def IsModified(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def ModifiedShape(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """If the shape is not modified, returns the shape itself."""

    def GetIsClosed(self) -> nanoocp.NCollection.NCollection_Sequence[bool]: ...

class BRepMAT2d_LinkTopoBilo:
    """
    Constructs links between the Wire or the Face of the explorer and
    the BasicElts contained in the bisecting locus.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Explo: BRepMAT2d_Explorer, BiLo: BRepMAT2d_BisectingLocus) -> None:
        """
        Constructs the links Between S and BiLo.

        raises if <S> is not a face.
        """

    @overload
    def __init__(self, theOther: BRepMAT2d_LinkTopoBilo) -> None: ...

    def __iter__(self) -> BRepMAT2d_LinkTopoBilo:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.MAT.MAT_BasicElt:
        """Python addition: see __iter__."""

    def Perform(self, Explo: BRepMAT2d_Explorer, BiLo: BRepMAT2d_BisectingLocus) -> None:
        """
        Constructs the links Between S and BiLo.

        raises if <S> is not a face or a wire.
        """

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initialise the Iterator on <S>
        <S> is an edge or a vertex of the initial
        wire or face.
        raises if <S> is not an edge or a vertex.
        """

    def More(self) -> bool:
        """Returns True if there is a current BasicElt."""

    def Next(self) -> None:
        """Proceed to the next BasicElt."""

    def Value(self) -> nanoocp.MAT.MAT_BasicElt:
        """Returns the current BasicElt."""

    def GeneratingShape(self, aBE: nanoocp.MAT.MAT_BasicElt | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the Shape linked to <aBE>."""
