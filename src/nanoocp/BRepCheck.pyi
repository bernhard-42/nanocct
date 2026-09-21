"""OCCT package BRepCheck (toolkit TKTopAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopoDS


class BRepCheck_Status(enum.IntEnum):
    BRepCheck_NoError = 0

    BRepCheck_InvalidPointOnCurve = 1

    BRepCheck_InvalidPointOnCurveOnSurface = 2

    BRepCheck_InvalidPointOnSurface = 3

    BRepCheck_No3DCurve = 4

    BRepCheck_Multiple3DCurve = 5

    BRepCheck_Invalid3DCurve = 6

    BRepCheck_NoCurveOnSurface = 7

    BRepCheck_InvalidCurveOnSurface = 8

    BRepCheck_InvalidCurveOnClosedSurface = 9

    BRepCheck_InvalidSameRangeFlag = 10

    BRepCheck_InvalidSameParameterFlag = 11

    BRepCheck_InvalidDegeneratedFlag = 12

    BRepCheck_FreeEdge = 13

    BRepCheck_InvalidMultiConnexity = 14

    BRepCheck_InvalidRange = 15

    BRepCheck_EmptyWire = 16

    BRepCheck_RedundantEdge = 17

    BRepCheck_SelfIntersectingWire = 18

    BRepCheck_NoSurface = 19

    BRepCheck_InvalidWire = 20

    BRepCheck_RedundantWire = 21

    BRepCheck_IntersectingWires = 22

    BRepCheck_InvalidImbricationOfWires = 23

    BRepCheck_EmptyShell = 24

    BRepCheck_RedundantFace = 25

    BRepCheck_InvalidImbricationOfShells = 26

    BRepCheck_UnorientableShape = 27

    BRepCheck_NotClosed = 28

    BRepCheck_NotConnected = 29

    BRepCheck_SubshapeNotInShape = 30

    BRepCheck_BadOrientation = 31

    BRepCheck_BadOrientationOfSubshape = 32

    BRepCheck_InvalidPolygonOnTriangulation = 33

    BRepCheck_InvalidToleranceValue = 34

    BRepCheck_EnclosedRegion = 35

    BRepCheck_CheckFail = 36

BRepCheck_NoError: BRepCheck_Status = BRepCheck_Status.BRepCheck_NoError

BRepCheck_InvalidPointOnCurve: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidPointOnCurve

BRepCheck_InvalidPointOnCurveOnSurface: BRepCheck_Status = ...

BRepCheck_InvalidPointOnSurface: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidPointOnSurface

BRepCheck_No3DCurve: BRepCheck_Status = BRepCheck_Status.BRepCheck_No3DCurve

BRepCheck_Multiple3DCurve: BRepCheck_Status = BRepCheck_Status.BRepCheck_Multiple3DCurve

BRepCheck_Invalid3DCurve: BRepCheck_Status = BRepCheck_Status.BRepCheck_Invalid3DCurve

BRepCheck_NoCurveOnSurface: BRepCheck_Status = BRepCheck_Status.BRepCheck_NoCurveOnSurface

BRepCheck_InvalidCurveOnSurface: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidCurveOnSurface

BRepCheck_InvalidCurveOnClosedSurface: BRepCheck_Status = ...

BRepCheck_InvalidSameRangeFlag: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidSameRangeFlag

BRepCheck_InvalidSameParameterFlag: BRepCheck_Status = ...

BRepCheck_InvalidDegeneratedFlag: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidDegeneratedFlag

BRepCheck_FreeEdge: BRepCheck_Status = BRepCheck_Status.BRepCheck_FreeEdge

BRepCheck_InvalidMultiConnexity: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidMultiConnexity

BRepCheck_InvalidRange: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidRange

BRepCheck_EmptyWire: BRepCheck_Status = BRepCheck_Status.BRepCheck_EmptyWire

BRepCheck_RedundantEdge: BRepCheck_Status = BRepCheck_Status.BRepCheck_RedundantEdge

BRepCheck_SelfIntersectingWire: BRepCheck_Status = BRepCheck_Status.BRepCheck_SelfIntersectingWire

BRepCheck_NoSurface: BRepCheck_Status = BRepCheck_Status.BRepCheck_NoSurface

BRepCheck_InvalidWire: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidWire

BRepCheck_RedundantWire: BRepCheck_Status = BRepCheck_Status.BRepCheck_RedundantWire

BRepCheck_IntersectingWires: BRepCheck_Status = BRepCheck_Status.BRepCheck_IntersectingWires

BRepCheck_InvalidImbricationOfWires: BRepCheck_Status = ...

BRepCheck_EmptyShell: BRepCheck_Status = BRepCheck_Status.BRepCheck_EmptyShell

BRepCheck_RedundantFace: BRepCheck_Status = BRepCheck_Status.BRepCheck_RedundantFace

BRepCheck_InvalidImbricationOfShells: BRepCheck_Status = ...

BRepCheck_UnorientableShape: BRepCheck_Status = BRepCheck_Status.BRepCheck_UnorientableShape

BRepCheck_NotClosed: BRepCheck_Status = BRepCheck_Status.BRepCheck_NotClosed

BRepCheck_NotConnected: BRepCheck_Status = BRepCheck_Status.BRepCheck_NotConnected

BRepCheck_SubshapeNotInShape: BRepCheck_Status = BRepCheck_Status.BRepCheck_SubshapeNotInShape

BRepCheck_BadOrientation: BRepCheck_Status = BRepCheck_Status.BRepCheck_BadOrientation

BRepCheck_BadOrientationOfSubshape: BRepCheck_Status = ...

BRepCheck_InvalidPolygonOnTriangulation: BRepCheck_Status = ...

BRepCheck_InvalidToleranceValue: BRepCheck_Status = BRepCheck_Status.BRepCheck_InvalidToleranceValue

BRepCheck_EnclosedRegion: BRepCheck_Status = BRepCheck_Status.BRepCheck_EnclosedRegion

BRepCheck_CheckFail: BRepCheck_Status = BRepCheck_Status.BRepCheck_CheckFail

class BRepCheck:
    """
    This package provides tools to check the validity
    of the BRep.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepCheck) -> None: ...

    @staticmethod
    def Add(List: nanoocp.NCollection.NCollection_List[nanoocp.BRepCheck.BRepCheck_Status], Stat: BRepCheck_Status) -> None: ...

    @staticmethod
    def Print(Stat: BRepCheck_Status) -> object: ...

    @staticmethod
    def SelfIntersection(W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    @staticmethod
    def PrecCurve(aAC3D: nanoocp.Adaptor3d.Adaptor3d_Curve) -> float:
        """Returns the resolution on the 3d curve"""

    @staticmethod
    def PrecSurface(aAHSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> float:
        """Returns the resolution on the surface"""

class BRepCheck_Result(nanoocp.Standard.Standard_Transient):
    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def InContext(self, ContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Minimum(self) -> None: ...

    def Blind(self) -> None: ...

    def SetFailStatus(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Status(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BRepCheck.BRepCheck_Status]: ...

    def IsMinimum(self) -> bool: ...

    def IsBlind(self) -> bool: ...

    def InitContextIterator(self) -> None: ...

    def MoreShapeInContext(self) -> bool: ...

    def ContextualShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def StatusOnShape(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BRepCheck.BRepCheck_Status]: ...

    @overload
    def StatusOnShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.BRepCheck.BRepCheck_Status]: ...

    def NextShapeInContext(self) -> None: ...

    def SetParallel(self, theIsParallel: bool) -> None:
        """Sets the parallel execution flag for sub-algorithms."""

    def IsParallel(self) -> bool:
        """Returns TRUE if sub-algorithms should use parallel execution."""

    def IsStatusOnShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepCheck_Analyzer:
    """
    A framework to check the overall
    validity of a shape. For a shape to be valid in Open
    CASCADE, it - or its component subshapes - must respect certain
    criteria. These criteria are checked by the function IsValid.
    Once you have determined whether a shape is valid or not, you can
    diagnose its specific anomalies and correct them using the services of
    the ShapeAnalysis, ShapeUpgrade, and ShapeFix packages.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, GeomControls: bool = True, theIsParallel: bool = False, theIsExact: bool = False) -> None:
        """
        Constructs a shape validation object defined by the shape S.
        <S> is the shape to control. <GeomControls> If
        False only topological informaions are checked.
        The geometricals controls are
        For a Vertex:
        BRepCheck_InvalidToleranceValue NYI
        For an Edge:
        BRepCheck_InvalidCurveOnClosedSurface,
        BRepCheck_InvalidCurveOnSurface,
        BRepCheck_InvalidSameParameterFlag,
        BRepCheck_InvalidToleranceValue NYI
        For a face:
        BRepCheck_UnorientableShape,
        BRepCheck_IntersectingWires,
        BRepCheck_InvalidToleranceValue NYI
        For a wire:
        BRepCheck_SelfIntersectingWire
        """

    @overload
    def __init__(self, theOther: BRepCheck_Analyzer) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, GeomControls: bool = True) -> None:
        """
        <S> is the shape to control. <GeomControls> If
        False only topological informaions are checked.
        The geometricals controls are
        For a Vertex:
        BRepCheck_InvalidTolerance NYI
        For an Edge:
        BRepCheck_InvalidCurveOnClosedSurface,
        BRepCheck_InvalidCurveOnSurface,
        BRepCheck_InvalidSameParameterFlag,
        BRepCheck_InvalidTolerance NYI
        For a face:
        BRepCheck_UnorientableShape,
        BRepCheck_IntersectingWires,
        BRepCheck_InvalidTolerance NYI
        For a wire:
        BRepCheck_SelfIntersectingWire
        """

    def SetExactMethod(self, theIsExact: bool) -> None:
        """
        Sets method to calculate distance: Calculating in finite number of points (if theIsExact
        is false, faster, but possible not correct result) or exact calculating by using
        BRepLib_CheckCurveOnSurface class (if theIsExact is true, slowly, but more correctly).
        Exact method is used only when edge is SameParameter.
        Default method is calculating in finite number of points
        """

    def IsExactMethod(self) -> bool:
        """Returns true if exact method selected"""

    def SetParallel(self, theIsParallel: bool) -> None:
        """Sets parallel flag"""

    def IsParallel(self) -> bool:
        """Returns true if parallel flag is set"""

    @overload
    def IsValid(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        <S> is a subshape of the original shape. Returns
        <STandard_True> if no default has been detected on
        <S> and any of its subshape.
        """

    @overload
    def IsValid(self) -> bool:
        """
        Returns true if no defect is
        detected on the shape S or any of its subshapes.
        Returns true if the shape S is valid.
        This function checks whether a given shape is valid by checking that:
        -      the topology is correct
        -      parameterization of edges in particular is correct.
        For the topology to be correct, the following conditions must be satisfied:
        -      edges should have at least two vertices if they are not
        degenerate edges. The vertices should be within the range of
        the bounding edges at the tolerance specified in the vertex,
        -      edges should share at least one face. The representation of
        the edges should be within the tolerance criterion assigned to them.
        -      wires defining a face should not self-intersect and should be closed,
        - there should be one wire which contains all other wires inside a face,
        -      wires should be correctly oriented with respect to each of the edges,
        -      faces should be correctly oriented, in particular with
        respect to adjacent faces if these faces define a solid,
        -      shells defining a solid should be closed. There should
        be one enclosing shell if the shape is a solid;
        To check parameterization of edge, there are 2 approaches depending on
        the edge?s contextual situation.
        -      if the edge is either single, or it is in the context
        of a wire or a compound, its parameterization is defined by
        the parameterization of its 3D curve and is considered as valid.
        -      If the edge is in the context of a face, it should
        have SameParameter and SameRange flags set to true. To
        check these flags, you should call the function
        BRep_Tool::SameParameter and BRep_Tool::SameRange for an
        edge. If at least one of these flags is set to false,
        the edge is considered as invalid without any additional check.
        If the edge is contained by a face, and it has SameParameter and
        SameRange flags set to true, IsValid checks
        whether representation of the edge on face, in context of which the
        edge is considered, has the same parameterization up to the
        tolerance value coded on the edge. For a given parameter t on the edge
        having C as a 3D curve and one PCurve P on a surface S (base
        surface of the reference face), this checks that |C(t) - S(P(t))|
        is less than or equal to tolerance, where tolerance is the tolerance
        value coded on the edge.
        """

    def Result(self, theSubS: nanoocp.TopoDS.TopoDS_Shape) -> BRepCheck_Result: ...

class BRepCheck_Edge(BRepCheck_Result):
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def InContext(self, ContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Minimum(self) -> None: ...

    def Blind(self) -> None: ...

    @overload
    def GeometricControls(self) -> bool: ...

    @overload
    def GeometricControls(self, B: bool) -> None: ...

    def Tolerance(self) -> float: ...

    def SetStatus(self, theStatus: BRepCheck_Status) -> None:
        """Sets status of Edge;"""

    def SetExactMethod(self, theIsExact: bool) -> None:
        """
        Sets method to calculate distance: Calculating in finite number of points (if theIsExact
        is false, faster, but possible not correct result) or exact calculating by using
        BRepLib_CheckCurveOnSurface class (if theIsExact is true, slowly, but more correctly).
        Exact method is used only when edge is SameParameter.
        Default method is calculating in finite number of points
        """

    def IsExactMethod(self) -> bool:
        """Returns true if exact method selected"""

    def CheckPolygonOnTriangulation(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> BRepCheck_Status:
        """
        Checks, if polygon on triangulation of heEdge
        is out of 3D-curve of this edge.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepCheck_Face(BRepCheck_Result):
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def InContext(self, ContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Minimum(self) -> None: ...

    def Blind(self) -> None: ...

    def IntersectWires(self, Update: bool = False) -> BRepCheck_Status: ...

    def ClassifyWires(self, Update: bool = False) -> BRepCheck_Status: ...

    def OrientationOfWires(self, Update: bool = False) -> BRepCheck_Status: ...

    def SetUnorientable(self) -> None: ...

    def SetStatus(self, theStatus: BRepCheck_Status) -> None:
        """Sets status of Face;"""

    def IsUnorientable(self) -> bool: ...

    @overload
    def GeometricControls(self) -> bool: ...

    @overload
    def GeometricControls(self, B: bool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepCheck_Shell(BRepCheck_Result):
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None: ...

    def InContext(self, ContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Minimum(self) -> None: ...

    def Blind(self) -> None: ...

    def Closed(self, Update: bool = False) -> BRepCheck_Status:
        """
        Checks if the oriented faces of the shell give a
        closed shell. If the wire is closed, returns
        BRepCheck_NoError. If <Update> is set to
        true, registers the status in the list.
        """

    def Orientation(self, Update: bool = False) -> BRepCheck_Status:
        """
        Checks if the oriented faces of the shell are
        correctly oriented. An internal call is made to
        the method Closed. If <Update> is set to
        true, registers the status in the list.
        """

    def SetUnorientable(self) -> None: ...

    def IsUnorientable(self) -> bool: ...

    def NbConnectedSet(self, theSets: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepCheck_Solid(BRepCheck_Result):
    """The class is to check a solid."""

    def __init__(self, theS: nanoocp.TopoDS.TopoDS_Solid) -> None:
        """
        Constructor
        <theS> is the solid to check
        """

    def InContext(self, theContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Checks the solid in context of
        the shape <theContextShape>
        """

    def Minimum(self) -> None:
        """
        Checks the solid per se.

        The scan area is:
        1.  Shells that overlaps each other
        Status:  BRepCheck_InvalidImbricationOfShells

        2.  Detached parts of the solid (vertices, edges)
        that have non-internal orientation
        Status:  BRepCheck_BadOrientationOfSubshape

        3.  For closed, non-internal shells:
        3.1 Shells containing entities of the solid that
        are outside towards the shells
        Status:  BRepCheck_SubshapeNotInShape

        3.2 Shells that encloses other Shells
        (for non-holes)
        Status:  BRepCheck_EnclosedRegion
        """

    def Blind(self) -> None:
        """see the parent class for more details"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepCheck_Vertex(BRepCheck_Result):
    def __init__(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def InContext(self, ContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Minimum(self) -> None: ...

    def Blind(self) -> None: ...

    def Tolerance(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepCheck_Wire(BRepCheck_Result):
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    def InContext(self, ContextShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        if <ContextShape> is a face, consequently checks
        SelfIntersect(), Closed(), Orientation() and
        Closed2d until faulty is found
        """

    def Minimum(self) -> None:
        """
        checks that the wire is not empty and "connex".
        Called by constructor
        """

    def Blind(self) -> None:
        """Does nothing"""

    def Closed(self, Update: bool = False) -> BRepCheck_Status:
        """
        Checks if the oriented edges of the wire give a
        closed wire. If the wire is closed, returns
        BRepCheck_NoError. Warning: if the first and
        last edge are infinite, the wire will be
        considered as a closed one. If <Update> is set to
        true, registers the status in the list.
        May return (and registers):
        **BRepCheck_NotConnected, if wire is not
        topologically closed
        **BRepCheck_RedundantEdge, if an edge is in wire
        more than 3 times or in case of 2 occurrences if
        not with FORWARD and REVERSED orientation.
        **BRepCheck_NoError
        """

    def Closed2d(self, F: nanoocp.TopoDS.TopoDS_Face, Update: bool = False) -> BRepCheck_Status:
        """
        Checks if edges of the wire give a wire closed in
        2d space.
        Returns BRepCheck_NoError, or BRepCheck_NotClosed
        If <Update> is set to true, registers the
        status in the list.
        """

    def Orientation(self, F: nanoocp.TopoDS.TopoDS_Face, Update: bool = False) -> BRepCheck_Status:
        """
        Checks if the oriented edges of the wire are
        correctly oriented. An internal call is made to
        the method Closed. If no face exists, call the
        method with a null face (TopoDS_face()). If
        <Update> is set to true, registers the
        status in the list.
        May return (and registers):
        BRepCheck_InvalidDegeneratedFlag,
        BRepCheck_BadOrientationOfSubshape,
        BRepCheck_NotClosed,
        BRepCheck_NoError
        """

    def SelfIntersect(self, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, Update: bool = False) -> BRepCheck_Status:
        """
        Checks if the wire intersect itself on the face
        <F>. <E1> and <E2> are the first intersecting
        edges found. <E2> may be a null edge when a
        self-intersecting edge is found.If <Update> is set
        to true, registers the status in the
        list.
        May return (and register):
        BRepCheck_EmptyWire,
        BRepCheck_SelfIntersectingWire,
        BRepCheck_NoCurveOnSurface,
        BRepCheck_NoError
        """

    @overload
    def GeometricControls(self) -> bool:
        """report SelfIntersect() check would be (is) done"""

    @overload
    def GeometricControls(self, B: bool) -> None:
        """set SelfIntersect() to be checked"""

    def SetStatus(self, theStatus: BRepCheck_Status) -> None:
        """Sets status of Wire;"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BRepCheck
BRepCheck_ListOfStatus = nanoocp.NCollection.NCollection_List[nanoocp.BRepCheck.BRepCheck_Status]
