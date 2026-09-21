"""OCCT package HLRAlgo (toolkit TKHLR)"""

import enum
from typing import overload

import nanoocp.Bnd
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.gp


class HLRAlgo_PolyMask(enum.IntEnum):
    HLRAlgo_PolyMask_EMskOutLin1 = 1

    HLRAlgo_PolyMask_EMskOutLin2 = 2

    HLRAlgo_PolyMask_EMskOutLin3 = 4

    HLRAlgo_PolyMask_EMskGrALin1 = 8

    HLRAlgo_PolyMask_EMskGrALin2 = 16

    HLRAlgo_PolyMask_EMskGrALin3 = 32

    HLRAlgo_PolyMask_FMskBack = 64

    HLRAlgo_PolyMask_FMskSide = 128

    HLRAlgo_PolyMask_FMskHiding = 256

    HLRAlgo_PolyMask_FMskFlat = 512

    HLRAlgo_PolyMask_FMskOnOutL = 1024

    HLRAlgo_PolyMask_FMskOrBack = 2048

    HLRAlgo_PolyMask_FMskFrBack = 4096

HLRAlgo_PolyMask_EMskOutLin1: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin1

HLRAlgo_PolyMask_EMskOutLin2: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin2

HLRAlgo_PolyMask_EMskOutLin3: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin3

HLRAlgo_PolyMask_EMskGrALin1: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin1

HLRAlgo_PolyMask_EMskGrALin2: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin2

HLRAlgo_PolyMask_EMskGrALin3: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin3

HLRAlgo_PolyMask_FMskBack: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskBack

HLRAlgo_PolyMask_FMskSide: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskSide

HLRAlgo_PolyMask_FMskHiding: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskHiding

HLRAlgo_PolyMask_FMskFlat: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFlat

HLRAlgo_PolyMask_FMskOnOutL: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOnOutL

HLRAlgo_PolyMask_FMskOrBack: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOrBack

HLRAlgo_PolyMask_FMskFrBack: HLRAlgo_PolyMask = HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFrBack

class HLRAlgo_EdgesBlock(nanoocp.Standard.Standard_Transient):
    """
    An EdgesBlock is a set of Edges. It is used by the
    DataStructure to structure the Edges.

    An EdgesBlock contains:

    * An Array of index of Edges.

    * An Array of flagsf
    (Orientation
    OutLine
    Internal
    Double
    IsoLine)
    """

    @overload
    def __init__(self, NbEdges: int) -> None:
        """Create a Block of Edges for a wire."""

    @overload
    def __init__(self, theOther: HLRAlgo_EdgesBlock) -> None: ...

    class MinMaxIndices:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

        def Minimize(self, theMinMaxIndices: HLRAlgo_EdgesBlock.MinMaxIndices) -> HLRAlgo_EdgesBlock.MinMaxIndices: ...

        def Maximize(self, theMinMaxIndices: HLRAlgo_EdgesBlock.MinMaxIndices) -> HLRAlgo_EdgesBlock.MinMaxIndices: ...

    def NbEdges(self) -> int: ...

    @overload
    def Edge(self, I: int, EI: int) -> None: ...

    @overload
    def Edge(self, I: int) -> int: ...

    @overload
    def Orientation(self, I: int, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Orientation(self, I: int) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def OutLine(self, I: int) -> bool: ...

    @overload
    def OutLine(self, I: int, B: bool) -> None: ...

    @overload
    def Internal(self, I: int) -> bool: ...

    @overload
    def Internal(self, I: int, B: bool) -> None: ...

    @overload
    def Double(self, I: int) -> bool: ...

    @overload
    def Double(self, I: int, B: bool) -> None: ...

    @overload
    def IsoLine(self, I: int) -> bool: ...

    @overload
    def IsoLine(self, I: int, B: bool) -> None: ...

    def UpdateMinMax(self, TotMinMax: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    def MinMax(self) -> HLRAlgo_EdgesBlock.MinMaxIndices: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo_WiresBlock(nanoocp.Standard.Standard_Transient):
    """
    A WiresBlock is a set of Blocks. It is used by the
    DataStructure to structure the Edges.

    A WiresBlock contains:

    * An Array of Blocks.
    """

    @overload
    def __init__(self, NbWires: int) -> None:
        """Create a Block of Blocks."""

    @overload
    def __init__(self, theOther: HLRAlgo_WiresBlock) -> None: ...

    def NbWires(self) -> int: ...

    def Set(self, I: int, W: HLRAlgo_EdgesBlock | None) -> None: ...

    def Wire(self, I: int) -> HLRAlgo_EdgesBlock: ...

    def UpdateMinMax(self, theMinMaxes: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    def MinMax(self) -> HLRAlgo_EdgesBlock.MinMaxIndices: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo:
    """
    In order to have the precision required in
    industrial design, drawings need to offer the
    possibility of removing lines, which are hidden
    in a given projection. To do this, the Hidden
    Line Removal component provides two
    algorithms: HLRBRep_Algo and HLRBRep_PolyAlgo.
    These algorithms remove or indicate lines
    hidden by surfaces. For a given projection, they
    calculate a set of lines characteristic of the
    object being represented. They are also used
    in conjunction with extraction utilities, which
    reconstruct a new, simplified shape from a
    selection of calculation results. This new shape
    is made up of edges, which represent the lines
    of the visualized shape in a plane. This plane is the projection plane.
    HLRBRep_Algo takes into account the shape
    itself. HLRBRep_PolyAlgo works with a
    polyhedral simplification of the shape. When
    you use HLRBRep_Algo, you obtain an exact
    result, whereas, when you use
    HLRBRep_PolyAlgo, you reduce computation
    time but obtain polygonal segments.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo) -> None: ...

    @staticmethod
    def EncodeMinMax(Min: HLRAlgo_EdgesBlock.MinMaxIndices, Max: HLRAlgo_EdgesBlock.MinMaxIndices, MinMax: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    @staticmethod
    def SizeBox(Min: HLRAlgo_EdgesBlock.MinMaxIndices, Max: HLRAlgo_EdgesBlock.MinMaxIndices) -> float: ...

    @staticmethod
    def DecodeMinMax(MinMax: HLRAlgo_EdgesBlock.MinMaxIndices, Min: HLRAlgo_EdgesBlock.MinMaxIndices, Max: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    @staticmethod
    def CopyMinMax(IMin: HLRAlgo_EdgesBlock.MinMaxIndices, IMax: HLRAlgo_EdgesBlock.MinMaxIndices, OMin: HLRAlgo_EdgesBlock.MinMaxIndices, OMax: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

    @staticmethod
    def AddMinMax(IMin: HLRAlgo_EdgesBlock.MinMaxIndices, IMax: HLRAlgo_EdgesBlock.MinMaxIndices, OMin: HLRAlgo_EdgesBlock.MinMaxIndices, OMax: HLRAlgo_EdgesBlock.MinMaxIndices) -> None: ...

class HLRAlgo_BiPoint:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, flag: int) -> None: ...

    @overload
    def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...

    @overload
    def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, flag: int) -> None: ...

    @overload
    def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...

    @overload
    def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, i2: int, i2p1: int, i2p2: int, flag: int) -> None: ...

    @overload
    def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, i2: int, i2p1: int, i2p2: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_BiPoint) -> None: ...

    class IndicesT:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_BiPoint.IndicesT) -> None: ...

        @property
        def ShapeIndex(self) -> int: ...

        @ShapeIndex.setter
        def ShapeIndex(self, arg: int, /) -> None: ...

        @property
        def FaceConex1(self) -> int: ...

        @FaceConex1.setter
        def FaceConex1(self, arg: int, /) -> None: ...

        @property
        def Face1Pt1(self) -> int: ...

        @Face1Pt1.setter
        def Face1Pt1(self, arg: int, /) -> None: ...

        @property
        def Face1Pt2(self) -> int: ...

        @Face1Pt2.setter
        def Face1Pt2(self, arg: int, /) -> None: ...

        @property
        def FaceConex2(self) -> int: ...

        @FaceConex2.setter
        def FaceConex2(self, arg: int, /) -> None: ...

        @property
        def Face2Pt1(self) -> int: ...

        @Face2Pt1.setter
        def Face2Pt1(self, arg: int, /) -> None: ...

        @property
        def Face2Pt2(self) -> int: ...

        @Face2Pt2.setter
        def Face2Pt2(self, arg: int, /) -> None: ...

        @property
        def MinSeg(self) -> int: ...

        @MinSeg.setter
        def MinSeg(self, arg: int, /) -> None: ...

        @property
        def MaxSeg(self) -> int: ...

        @MaxSeg.setter
        def MaxSeg(self, arg: int, /) -> None: ...

        @property
        def SegFlags(self) -> int: ...

        @SegFlags.setter
        def SegFlags(self, arg: int, /) -> None: ...

    class PointsT:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_BiPoint.PointsT) -> None: ...

        def PntP12D(self) -> nanoocp.gp.gp_XY: ...

        def PntP22D(self) -> nanoocp.gp.gp_XY: ...

        @property
        def Pnt1(self) -> nanoocp.gp.gp_XYZ: ...

        @Pnt1.setter
        def Pnt1(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def Pnt2(self) -> nanoocp.gp.gp_XYZ: ...

        @Pnt2.setter
        def Pnt2(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def PntP1(self) -> nanoocp.gp.gp_XYZ: ...

        @PntP1.setter
        def PntP1(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def PntP2(self) -> nanoocp.gp.gp_XYZ: ...

        @PntP2.setter
        def PntP2(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

    @overload
    def Rg1Line(self) -> bool: ...

    @overload
    def Rg1Line(self, B: bool) -> None: ...

    @overload
    def RgNLine(self) -> bool: ...

    @overload
    def RgNLine(self, B: bool) -> None: ...

    @overload
    def OutLine(self) -> bool: ...

    @overload
    def OutLine(self, B: bool) -> None: ...

    @overload
    def IntLine(self) -> bool: ...

    @overload
    def IntLine(self, B: bool) -> None: ...

    @overload
    def Hidden(self) -> bool: ...

    @overload
    def Hidden(self, B: bool) -> None: ...

    def Indices(self) -> HLRAlgo_BiPoint.IndicesT: ...

    def Points(self) -> HLRAlgo_BiPoint.PointsT: ...

class HLRAlgo_Coincidence:
    """
    The Coincidence class is used in an Interference to
    store information on the "hiding" edge.

    2D Data: The tangent and the curvature of the
    projection of the edge at the intersection point.
    This is necesserary when the intersection is at
    the extremity of the edge.

    3D Data: The state of the edge near the
    intersection with the face (before and after).
    This is necessary when the intersection is "ON"
    the face.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_Coincidence) -> None: ...

    def Set2D(self, FE: int, Param: float) -> None: ...

    def SetState3D(self, stbef: nanoocp.TopAbs.TopAbs_State, staft: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def Value2D(self) -> tuple[int, float]: ...

    def State3D(self) -> tuple[nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

class HLRAlgo_EdgeIterator:
    @overload
    def __init__(self) -> None:
        """Iterator on the visible or hidden parts of an edge."""

    @overload
    def __init__(self, theOther: HLRAlgo_EdgeIterator) -> None: ...

    def InitHidden(self, status: HLRAlgo_EdgeStatus) -> None: ...

    def MoreHidden(self) -> bool: ...

    def NextHidden(self) -> None: ...

    def Hidden(self) -> tuple[float, float, float, float]:
        """
        Returns the bounds and the tolerances
        of the current Hidden Interval
        """

    def InitVisible(self, status: HLRAlgo_EdgeStatus) -> None: ...

    def MoreVisible(self) -> bool: ...

    def NextVisible(self) -> None: ...

    def Visible(self) -> tuple[float, float, float, float]:
        """
        Returns the bounds and the tolerances
        of the current Visible Interval
        """

class HLRAlgo_EdgeStatus:
    """
    This class describes the Hidden Line status of an
    Edge. It contains:

    The Bounds of the Edge and their tolerances

    Two flags indicating if the edge is full visible
    or full hidden
    TheSequenceof visible Intervals on the Edge.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Start: float, TolStart: float, End: float, TolEnd: float) -> None:
        """
        Creates a new EdgeStatus. Default visible. The
        Edge is bounded by the interval <Start>, <End>
        with the tolerances <TolStart>, <TolEnd>.
        """

    @overload
    def __init__(self, theOther: HLRAlgo_EdgeStatus) -> None: ...

    def Initialize(self, Start: float, TolStart: float, End: float, TolEnd: float) -> None:
        """
        Initialize an EdgeStatus. Default visible. The
        Edge is bounded by the interval <Start>, <End>
        with the tolerances <TolStart>, <TolEnd>.
        """

    def Bounds(self) -> tuple[float, float, float, float]: ...

    def NbVisiblePart(self) -> int: ...

    def VisiblePart(self, Index: int) -> tuple[float, float, float, float]: ...

    def Hide(self, Start: float, TolStart: float, End: float, TolEnd: float, OnFace: bool, OnBoundary: bool) -> None:
        """
        Hides the interval <Start>, <End> with the
        tolerances <TolStart>, <TolEnd>. This interval is
        subtracted from the visible parts. If the hidden
        part is on (or under) the face the flag <OnFace>
        is True (or False). If the hidden part is on
        (or inside) the boundary of the face the flag
        <OnBoundary> is True (or False).
        """

    def HideAll(self) -> None:
        """Hide the whole Edge."""

    def ShowAll(self) -> None:
        """Show the whole Edge."""

    @overload
    def AllHidden(self) -> bool: ...

    @overload
    def AllHidden(self, B: bool) -> None: ...

    @overload
    def AllVisible(self) -> bool: ...

    @overload
    def AllVisible(self, B: bool) -> None: ...

class HLRAlgo_Intersection:
    """
    Describes an intersection on an edge to hide.
    Contains a parameter and a state (ON = on the
    face, OUT = above the face, IN = under the Face)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Ori: nanoocp.TopAbs.TopAbs_Orientation, Lev: int, SegInd: int, Ind: int, P: float, Tol: float, S: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_Intersection) -> None: ...

    @overload
    def Orientation(self, Ori: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def Level(self, Lev: int) -> None: ...

    @overload
    def Level(self) -> int: ...

    @overload
    def SegIndex(self, SegInd: int) -> None: ...

    @overload
    def SegIndex(self) -> int: ...

    @overload
    def Index(self, Ind: int) -> None: ...

    @overload
    def Index(self) -> int: ...

    @overload
    def Parameter(self, P: float) -> None: ...

    @overload
    def Parameter(self) -> float: ...

    @overload
    def Tolerance(self, T: float) -> None: ...

    @overload
    def Tolerance(self) -> float: ...

    @overload
    def State(self, S: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def State(self) -> nanoocp.TopAbs.TopAbs_State: ...

class HLRAlgo_Interference:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Inters: HLRAlgo_Intersection, Bound: HLRAlgo_Coincidence, Orient: nanoocp.TopAbs.TopAbs_Orientation, Trans: nanoocp.TopAbs.TopAbs_Orientation, BTrans: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_Interference) -> None: ...

    @overload
    def Intersection(self, I: HLRAlgo_Intersection) -> None: ...

    @overload
    def Intersection(self) -> HLRAlgo_Intersection: ...

    @overload
    def Boundary(self, B: HLRAlgo_Coincidence) -> None: ...

    @overload
    def Boundary(self) -> HLRAlgo_Coincidence: ...

    @overload
    def Orientation(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def Transition(self, Tr: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Transition(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def BoundaryTransition(self, BTr: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def BoundaryTransition(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def ChangeIntersection(self) -> HLRAlgo_Intersection: ...

    def ChangeBoundary(self) -> HLRAlgo_Coincidence: ...

class HLRAlgo_PolyHidingData:
    """Data structure of a set of Hiding Triangles."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyHidingData) -> None: ...

    class TriangleIndices:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_PolyHidingData.TriangleIndices) -> None: ...

        @property
        def Index(self) -> int: ...

        @Index.setter
        def Index(self, arg: int, /) -> None: ...

        @property
        def Min(self) -> int: ...

        @Min.setter
        def Min(self, arg: int, /) -> None: ...

        @property
        def Max(self) -> int: ...

        @Max.setter
        def Max(self, arg: int, /) -> None: ...

    class PlaneT:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_PolyHidingData.PlaneT) -> None: ...

        @property
        def Normal(self) -> nanoocp.gp.gp_XYZ: ...

        @Normal.setter
        def Normal(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def D(self) -> float: ...

        @D.setter
        def D(self, arg: float, /) -> None: ...

    def Set(self, Index: int, Minim: int, Maxim: int, A: float, B: float, C: float, D: float) -> None: ...

    def Indices(self) -> HLRAlgo_PolyHidingData.TriangleIndices: ...

    def Plane(self) -> HLRAlgo_PolyHidingData.PlaneT: ...

class HLRAlgo_TriangleData:
    """Data structure of a triangle."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_TriangleData) -> None: ...

    @property
    def Node1(self) -> int: ...

    @Node1.setter
    def Node1(self, arg: int, /) -> None: ...

    @property
    def Node2(self) -> int: ...

    @Node2.setter
    def Node2(self, arg: int, /) -> None: ...

    @property
    def Node3(self) -> int: ...

    @Node3.setter
    def Node3(self, arg: int, /) -> None: ...

    @property
    def Flags(self) -> int: ...

    @Flags.setter
    def Flags(self, arg: int, /) -> None: ...

class HLRAlgo_PolyData(nanoocp.Standard.Standard_Transient):
    """Data structure of a set of Triangles."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyData) -> None: ...

    class FaceIndices:
        @overload
        def __init__(self) -> None:
            """The default constructor."""

        @overload
        def __init__(self, theOther: HLRAlgo_PolyData.FaceIndices) -> None: ...

        @property
        def Index(self) -> int: ...

        @Index.setter
        def Index(self, arg: int, /) -> None: ...

        @property
        def Min(self) -> int: ...

        @Min.setter
        def Min(self, arg: int, /) -> None: ...

        @property
        def Max(self) -> int: ...

        @Max.setter
        def Max(self, arg: int, /) -> None: ...

    class Triangle:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_PolyData.Triangle) -> None: ...

        @property
        def V1(self) -> nanoocp.gp.gp_XY: ...

        @V1.setter
        def V1(self, arg: nanoocp.gp.gp_XY, /) -> None: ...

        @property
        def V2(self) -> nanoocp.gp.gp_XY: ...

        @V2.setter
        def V2(self, arg: nanoocp.gp.gp_XY, /) -> None: ...

        @property
        def V3(self) -> nanoocp.gp.gp_XY: ...

        @V3.setter
        def V3(self, arg: nanoocp.gp.gp_XY, /) -> None: ...

        @property
        def Param(self) -> float: ...

        @Param.setter
        def Param(self, arg: float, /) -> None: ...

        @property
        def TolParam(self) -> float: ...

        @TolParam.setter
        def TolParam(self, arg: float, /) -> None: ...

        @property
        def TolAng(self) -> float: ...

        @TolAng.setter
        def TolAng(self, arg: float, /) -> None: ...

        @property
        def Tolerance(self) -> float: ...

        @Tolerance.setter
        def Tolerance(self, arg: float, /) -> None: ...

    def HNodes(self, HNodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    def HTData(self, HTData: nanoocp.NCollection.NCollection_HArray1[nanoocp.HLRAlgo.HLRAlgo_TriangleData] | None) -> None: ...

    def HPHDat(self, HPHDat: nanoocp.NCollection.NCollection_HArray1[nanoocp.HLRAlgo.HLRAlgo_PolyHidingData] | None) -> None: ...

    @overload
    def FaceIndex(self, I: int) -> None: ...

    @overload
    def FaceIndex(self) -> int: ...

    def Nodes(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_XYZ]: ...

    def TData(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_TriangleData]: ...

    def PHDat(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyHidingData]: ...

    def UpdateGlobalMinMax(self, theBox: nanoocp.Bnd.Bnd_Box) -> None: ...

    def Hiding(self) -> bool: ...

    def HideByPolyData(self, thePoints: HLRAlgo_BiPoint.PointsT, theTriangle: HLRAlgo_PolyData.Triangle, theIndices: HLRAlgo_BiPoint.IndicesT, HidingShell: bool, status: HLRAlgo_EdgeStatus) -> None:
        """process hiding between <Pt1> and <Pt2>."""

    def Indices(self) -> HLRAlgo_PolyData.FaceIndices: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo_PolyAlgo(nanoocp.Standard.Standard_Transient):
    """to remove Hidden lines on Triangulations."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyAlgo) -> None: ...

    def Init(self, theNbShells: int) -> None: ...

    def PolyShell(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyShellData]: ...

    def ChangePolyShell(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyShellData]: ...

    def Clear(self) -> None: ...

    def Update(self) -> None:
        """Prepare all the data to process the algo."""

    def InitHide(self) -> None: ...

    def MoreHide(self) -> bool: ...

    def NextHide(self) -> None: ...

    def Hide(self, status: HLRAlgo_EdgeStatus) -> tuple[HLRAlgo_BiPoint.PointsT, int, bool, bool, bool, bool]:
        """process hiding between <Pt1> and <Pt2>."""

    def InitShow(self) -> None: ...

    def MoreShow(self) -> bool: ...

    def NextShow(self) -> None: ...

    def Show(self) -> tuple[HLRAlgo_BiPoint.PointsT, int, bool, bool, bool, bool]:
        """process hiding between <Pt1> and <Pt2>."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo_PolyInternalSegment:
    """to Update OutLines."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyInternalSegment) -> None: ...

    @property
    def LstSg1(self) -> int: ...

    @LstSg1.setter
    def LstSg1(self, arg: int, /) -> None: ...

    @property
    def LstSg2(self) -> int: ...

    @LstSg2.setter
    def LstSg2(self, arg: int, /) -> None: ...

    @property
    def NxtSg1(self) -> int: ...

    @NxtSg1.setter
    def NxtSg1(self, arg: int, /) -> None: ...

    @property
    def NxtSg2(self) -> int: ...

    @NxtSg2.setter
    def NxtSg2(self, arg: int, /) -> None: ...

    @property
    def Conex1(self) -> int: ...

    @Conex1.setter
    def Conex1(self, arg: int, /) -> None: ...

    @property
    def Conex2(self) -> int: ...

    @Conex2.setter
    def Conex2(self, arg: int, /) -> None: ...

class HLRAlgo_PolyInternalNode(nanoocp.Standard.Standard_Transient):
    """to Update OutLines."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyInternalNode) -> None: ...

    class NodeIndices:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_PolyInternalNode.NodeIndices) -> None: ...

        @property
        def NdSg(self) -> int: ...

        @NdSg.setter
        def NdSg(self, arg: int, /) -> None: ...

        @property
        def Flag(self) -> int: ...

        @Flag.setter
        def Flag(self, arg: int, /) -> None: ...

        @property
        def Edg1(self) -> int: ...

        @Edg1.setter
        def Edg1(self, arg: int, /) -> None: ...

        @property
        def Edg2(self) -> int: ...

        @Edg2.setter
        def Edg2(self, arg: int, /) -> None: ...

    class NodeData:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_PolyInternalNode.NodeData) -> None: ...

        @property
        def Point(self) -> nanoocp.gp.gp_XYZ: ...

        @Point.setter
        def Point(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def Normal(self) -> nanoocp.gp.gp_XYZ: ...

        @Normal.setter
        def Normal(self, arg: nanoocp.gp.gp_XYZ, /) -> None: ...

        @property
        def UV(self) -> nanoocp.gp.gp_XY: ...

        @UV.setter
        def UV(self, arg: nanoocp.gp.gp_XY, /) -> None: ...

        @property
        def PCu1(self) -> float: ...

        @PCu1.setter
        def PCu1(self, arg: float, /) -> None: ...

        @property
        def PCu2(self) -> float: ...

        @PCu2.setter
        def PCu2(self, arg: float, /) -> None: ...

        @property
        def Scal(self) -> float: ...

        @Scal.setter
        def Scal(self, arg: float, /) -> None: ...

    def Indices(self) -> HLRAlgo_PolyInternalNode.NodeIndices: ...

    def Data(self) -> HLRAlgo_PolyInternalNode.NodeData: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo_PolyInternalData(nanoocp.Standard.Standard_Transient):
    """to Update OutLines."""

    @overload
    def __init__(self, nbNod: int, nbTri: int) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyInternalData) -> None: ...

    def UpdateLinks(self, theTData: nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_TriangleData], thePISeg: nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyInternalSegment], thePINod: nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyInternalNode]) -> None: ...

    def Dump(self) -> None: ...

    def DecTData(self) -> None: ...

    def DecPISeg(self) -> None: ...

    def DecPINod(self) -> None: ...

    def NbTData(self) -> int: ...

    def NbPISeg(self) -> int: ...

    def NbPINod(self) -> int: ...

    @overload
    def Planar(self) -> bool: ...

    @overload
    def Planar(self, B: bool) -> None: ...

    @overload
    def IntOutL(self) -> bool: ...

    @overload
    def IntOutL(self, B: bool) -> None: ...

    def TData(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_TriangleData]: ...

    def PISeg(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyInternalSegment]: ...

    def PINod(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyInternalNode]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo_PolyShellData(nanoocp.Standard.Standard_Transient):
    """All the PolyData of a Shell"""

    @overload
    def __init__(self, nbFace: int) -> None: ...

    @overload
    def __init__(self, theOther: HLRAlgo_PolyShellData) -> None: ...

    class ShellIndices:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: HLRAlgo_PolyShellData.ShellIndices) -> None: ...

        @property
        def Min(self) -> int: ...

        @Min.setter
        def Min(self, arg: int, /) -> None: ...

        @property
        def Max(self) -> int: ...

        @Max.setter
        def Max(self, arg: int, /) -> None: ...

    def UpdateGlobalMinMax(self, theBox: nanoocp.Bnd.Bnd_Box) -> None: ...

    def UpdateHiding(self, nbHiding: int) -> None: ...

    def Hiding(self) -> bool: ...

    def PolyData(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyData]: ...

    def HidingPolyData(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyData]: ...

    def Edges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.HLRAlgo.HLRAlgo_BiPoint]: ...

    def Indices(self) -> HLRAlgo_PolyShellData.ShellIndices: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class HLRAlgo_Projector:
    """
    Implements a projector object.
    To transform and project Points and Planes.
    This object is designed to be used in the
    removal of hidden lines and is returned by the
    Prs3d_Projector::Projector function.
    You define the projection of the selected shape
    by calling one of the following functions:
    -   HLRBRep_Algo::Projector, or
    -   HLRBRep_PolyAlgo::Projector
    The choice depends on the algorithm, which you are using.
    The parameters of the view are defined at the
    time of construction of a Prs3d_Projector object.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, CS: nanoocp.gp.gp_Ax2) -> None:
        """
        Creates an axonometric projector. <CS> is the
        viewing coordinate system.
        """

    @overload
    def __init__(self, CS: nanoocp.gp.gp_Ax2, Focus: float) -> None:
        """
        Creates a perspective projector. <CS> is the
        viewing coordinate system.
        """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf, Persp: bool, Focus: float) -> None:
        """build a Projector with automatic minmax directions."""

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf, Persp: bool, Focus: float, v1: nanoocp.gp.gp_Vec2d, v2: nanoocp.gp.gp_Vec2d, v3: nanoocp.gp.gp_Vec2d) -> None:
        """build a Projector with given minmax directions."""

    @overload
    def __init__(self, theOther: HLRAlgo_Projector) -> None: ...

    def Set(self, T: nanoocp.gp.gp_Trsf, Persp: bool, Focus: float) -> None: ...

    def Directions(self, D1: nanoocp.gp.gp_Vec2d, D2: nanoocp.gp.gp_Vec2d, D3: nanoocp.gp.gp_Vec2d) -> None: ...

    def Scaled(self, On: bool = False) -> None:
        """to compute with the given scale and translation."""

    def Perspective(self) -> bool:
        """Returns True if there is a perspective transformation."""

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """Returns the active transformation."""

    def InvertedTransformation(self) -> nanoocp.gp.gp_Trsf:
        """Returns the active inverted transformation."""

    def FullTransformation(self) -> nanoocp.gp.gp_Trsf:
        """Returns the original transformation."""

    def Focus(self) -> float:
        """Returns the focal length."""

    @overload
    def Transform(self, D: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def Transform(self, Pnt: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Pnt, Pout: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Pnt) -> tuple[float, float, float]: ...

    @overload
    def Project(self, P: nanoocp.gp.gp_Pnt, D1: nanoocp.gp.gp_Vec, Pout: nanoocp.gp.gp_Pnt2d, D1out: nanoocp.gp.gp_Vec2d) -> None:
        """Transform and apply perspective if needed."""

    def Shoot(self, X: float, Y: float) -> nanoocp.gp.gp_Lin:
        """
        return a line going through the eye towards the
        2d point <X,Y>.
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.HLRAlgo
HLRAlgo_Array1OfPHDat = nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyHidingData]
HLRAlgo_Array1OfPINod = nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyInternalNode]
HLRAlgo_Array1OfPISeg = nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_PolyInternalSegment]
HLRAlgo_Array1OfTData = nanoocp.NCollection.NCollection_Array1[nanoocp.HLRAlgo.HLRAlgo_TriangleData]
HLRAlgo_HArray1OfPHDat = nanoocp.NCollection.NCollection_HArray1[nanoocp.HLRAlgo.HLRAlgo_PolyHidingData]
HLRAlgo_HArray1OfTData = nanoocp.NCollection.NCollection_HArray1[nanoocp.HLRAlgo.HLRAlgo_TriangleData]
HLRAlgo_InterferenceList = nanoocp.NCollection.NCollection_List[nanoocp.HLRAlgo.HLRAlgo_Interference]
HLRAlgo_ListOfBPoint = nanoocp.NCollection.NCollection_List[nanoocp.HLRAlgo.HLRAlgo_BiPoint]
