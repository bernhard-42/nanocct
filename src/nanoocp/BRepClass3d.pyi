"""OCCT package BRepClass3d (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.BRepAdaptor
import nanoocp.Bnd
import nanoocp.IntCurveSurface
import nanoocp.IntCurvesFace
import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class BRepClass3d:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepClass3d) -> None: ...

    @staticmethod
    def OuterShell(S: nanoocp.TopoDS.TopoDS_Solid) -> nanoocp.TopoDS.TopoDS_Shell:
        """
        Returns the outer most shell of <S>. Returns a Null
        shell if <S> has no outer shell.
        If <S> has only one shell, then it will return, without checking orientation.
        """

class BRepClass3d_BndBoxTreeSelectorPoint:
    def __init__(self, theMapOfShape: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def Reject(self, theBox: nanoocp.Bnd.Bnd_Box) -> bool: ...

    def Accept(self, theObj: int) -> bool: ...

    def SetCurrentPoint(self, theP: nanoocp.gp.gp_Pnt) -> None: ...

class BRepClass3d_BndBoxTreeSelectorLine:
    def __init__(self, theMapOfShape: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    class EdgeParam:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepClass3d_BndBoxTreeSelectorLine.EdgeParam) -> None: ...

        @property
        def myE(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

        @myE.setter
        def myE(self, arg: nanoocp.TopoDS.TopoDS_Edge, /) -> None: ...

        @property
        def myParam(self) -> float: ...

        @myParam.setter
        def myParam(self, arg: float, /) -> None: ...

        @property
        def myLParam(self) -> float: ...

        @myLParam.setter
        def myLParam(self, arg: float, /) -> None: ...

    class VertParam:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepClass3d_BndBoxTreeSelectorLine.VertParam) -> None: ...

        @property
        def myV(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

        @myV.setter
        def myV(self, arg: nanoocp.TopoDS.TopoDS_Vertex, /) -> None: ...

        @property
        def myLParam(self) -> float: ...

        @myLParam.setter
        def myLParam(self, arg: float, /) -> None: ...

    def Reject(self, theBox: nanoocp.Bnd.Bnd_Box) -> bool: ...

    def Accept(self, theObj: int) -> bool: ...

    def SetCurrentLine(self, theL: nanoocp.gp.gp_Lin, theMaxParam: float) -> None: ...

    def GetEdgeParam(self, i: int, theOutE: nanoocp.TopoDS.TopoDS_Edge) -> tuple[float, float]: ...

    def GetVertParam(self, i: int, theOutV: nanoocp.TopoDS.TopoDS_Vertex) -> float: ...

    def GetNbEdgeParam(self) -> int: ...

    def GetNbVertParam(self) -> int: ...

    def ClearResults(self) -> None: ...

    def IsCorrect(self) -> bool:
        """Returns TRUE if correct classification is possible"""

class BRepClass3d_Intersector3d:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: BRepClass3d_Intersector3d) -> None: ...

    def Perform(self, L: nanoocp.gp.gp_Lin, Prm: float, Tol: float, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Perform the intersection between the
        segment L(0) ... L(Prm) and the Shape <Sh>.

        Only the point with the smallest parameter on the
        line is returned.

        The Tolerance <Tol> is used to determine if the
        first point of the segment is near the face. In
        that case, the parameter of the intersection point
        on the line can be a negative value (greater than -Tol).
        """

    def IsDone(self) -> bool:
        """True is returned when the intersection have been computed."""

    def HasAPoint(self) -> bool:
        """True is returned if a point has been found."""

    def UParameter(self) -> float:
        """
        Returns the U parameter of the intersection point
        on the surface.
        """

    def VParameter(self) -> float:
        """
        Returns the V parameter of the intersection point
        on the surface.
        """

    def WParameter(self) -> float:
        """
        Returns the parameter of the intersection point
        on the line.
        """

    def Pnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the geometric point of the intersection
        between the line and the surface.
        """

    def Transition(self) -> nanoocp.IntCurveSurface.IntCurveSurface_TransitionOnCurve:
        """Returns the transition of the line on the surface."""

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the state of the point on the face.
        The values can be either TopAbs_IN
        ( the point is in the face)
        or TopAbs_ON
        ( the point is on a boundary of the face).
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the significant face used to determine
        the intersection.
        """

class BRepClass3d_SClassifier:
    """Provides an algorithm to classify a point in a solid."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: BRepClass3d_SolidExplorer, P: nanoocp.gp.gp_Pnt, Tol: float) -> None:
        """
        Constructor to classify the point P with the
        tolerance Tol on the solid S.
        """

    @overload
    def __init__(self, theOther: BRepClass3d_SClassifier) -> None: ...

    def Perform(self, S: BRepClass3d_SolidExplorer, P: nanoocp.gp.gp_Pnt, Tol: float) -> None:
        """
        Classify the point P with the
        tolerance Tol on the solid S.
        """

    def PerformInfinitePoint(self, S: BRepClass3d_SolidExplorer, Tol: float) -> None:
        """
        Classify an infinite point with the
        tolerance Tol on the solid S.
        """

    def Rejected(self) -> bool:
        """
        Returns True if the classification has been
        computed by rejection.
        The State is then OUT.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the result of the classification."""

    def IsOnAFace(self) -> bool:
        """Returns True when the point is a point of a face."""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the face used to determine the
        classification. When the state is ON, this is the
        face containing the point.

        When Rejected() returns True, Face() has no signification.
        """

class BRepClass3d_SolidExplorer:
    """
    Provide an exploration of a BRep Shape for the classification.
    Provide access to the special UB tree to obtain fast search.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def InitShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Reject(self, P: nanoocp.gp.gp_Pnt) -> bool:
        """Should return True if P outside of bounding vol. of the shape"""

    @staticmethod
    def FindAPointInTheFace__float(F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        FindAPointInTheFace__float: the C++ overload FindAPointInTheFace(const TopoDS_Face &, gp_Pnt &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        compute a point P in the face F. Param is a Real in
        ]0,1[ and is used to initialise the algorithm. For
        different values , different points are returned.
        """

    @staticmethod
    def FindAPointInTheFace__float__float__float(F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float, float, float]:
        """
        FindAPointInTheFace__float__float__float: the C++ overload FindAPointInTheFace(const TopoDS_Face &, gp_Pnt &, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @overload
    @staticmethod
    def FindAPointInTheFace(F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt, theVecD1U: nanoocp.gp.gp_Vec, theVecD1V: nanoocp.gp.gp_Vec) -> tuple[bool, float, float, float]: ...

    @overload
    @staticmethod
    def FindAPointInTheFace(F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt) -> bool: ...

    @overload
    @staticmethod
    def FindAPointInTheFace(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, float, float]: ...

    @staticmethod
    def FindAPointInTheFace__float__float(F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float, float]:
        """
        FindAPointInTheFace__float__float: the C++ overload FindAPointInTheFace(const TopoDS_Face &, gp_Pnt &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @overload
    def PointInTheFace(self, F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float, float, float, int]: ...

    @overload
    def PointInTheFace(self, F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt, surf: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, u1: float, v1: float, u2: float, v2: float) -> tuple[bool, float, float, float, int]: ...

    @overload
    def PointInTheFace(self, F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt, surf: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, u1: float, v1: float, u2: float, v2: float, theVecD1U: nanoocp.gp.gp_Vec, theVecD1V: nanoocp.gp.gp_Vec) -> tuple[bool, float, float, float, int]:
        """
        <Index> gives point index to search from and returns
        point index of succeseful search
        """

    def InitShell(self) -> None:
        """Starts an exploration of the shells."""

    def MoreShell(self) -> bool:
        """Returns True if there is a current shell."""

    def NextShell(self) -> None:
        """Sets the explorer to the next shell."""

    def CurrentShell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the current shell."""

    def RejectShell(self, L: nanoocp.gp.gp_Lin) -> bool:
        """Returns True if the Shell is rejected."""

    def InitFace(self) -> None:
        """Starts an exploration of the faces of the current shell."""

    def MoreFace(self) -> bool:
        """Returns True if current face in current shell."""

    def NextFace(self) -> None:
        """Sets the explorer to the next Face of the current shell."""

    def CurrentFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the current face."""

    def RejectFace(self, L: nanoocp.gp.gp_Lin) -> bool:
        """returns True if the face is rejected."""

    def Segment(self, P: nanoocp.gp.gp_Pnt, L: nanoocp.gp.gp_Lin) -> tuple[int, float]:
        """
        Returns in <L>, <Par> a segment having at least
        one intersection with the shape boundary to
        compute intersections.
        """

    def OtherSegment(self, P: nanoocp.gp.gp_Pnt, L: nanoocp.gp.gp_Lin) -> tuple[int, float]:
        """
        Returns in <L>, <Par> a segment having at least
        one intersection with the shape boundary to
        compute intersections.

        The First Call to this method returns a line which
        point to a point of the first face of the shape.
        The Second Call provide a line to the second face
        and so on.
        """

    def GetFaceSegmentIndex(self) -> int:
        """
        Returns the index of face for which
        last segment is calculated.
        """

    def DumpSegment(self, P: nanoocp.gp.gp_Pnt, L: nanoocp.gp.gp_Lin, Par: float, S: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def GetShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Intersector(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.IntCurvesFace.IntCurvesFace_Intersector: ...

    def GetTree(self) -> "NCollection_UBTree<int, Bnd_Box>":
        """Return UB-tree instance which is used for edge / vertex checks."""

    def GetMapEV(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Return edge/vertices map for current shape."""

    def Destroy(self) -> None: ...

class BRepClass3d_SolidClassifier(BRepClass3d_SClassifier):
    """Provides an algorithm to classify a point in a solid."""

    @overload
    def __init__(self) -> None:
        """empty constructor"""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Constructor from a Shape."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, P: nanoocp.gp.gp_Pnt, Tol: float) -> None:
        """
        Constructor to classify the point P with the
        tolerance Tol on the solid S.
        """

    def Load(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Perform(self, P: nanoocp.gp.gp_Pnt, Tol: float) -> None:
        """
        Classify the point P with the
        tolerance Tol on the solid S.
        """

    def PerformInfinitePoint(self, Tol: float) -> None:
        """
        Classify an infinite point with the
        tolerance Tol on the solid S.
        Useful for compute the orientation of a solid.
        """

    def Destroy(self) -> None: ...

class BRepClass3d_SolidPassiveClassifier:
    @overload
    def __init__(self) -> None:
        """Creates an undefined classifier."""

    @overload
    def __init__(self, theOther: BRepClass3d_SolidPassiveClassifier) -> None: ...

    def Reset(self, L: nanoocp.gp.gp_Lin, P: float, Tol: float) -> None:
        """
        Starts a classification process. The point to
        classify is the origin of the line <L>. <P> is
        the original length of the segment on <L> used to
        compute intersections. <Tol> is the tolerance
        attached to the intersections.
        """

    def Compare(self, F: nanoocp.TopoDS.TopoDS_Face, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Updates the classification process with the face
        <F> from the boundary.
        """

    def Parameter(self) -> float:
        """Returns the current value of the parameter."""

    def HasIntersection(self) -> bool:
        """Returns True if an intersection is computed."""

    def Intersector(self) -> BRepClass3d_Intersector3d:
        """Returns the intersecting algorithm."""

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the current state of the point."""
