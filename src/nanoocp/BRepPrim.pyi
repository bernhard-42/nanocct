"""OCCT package BRepPrim (toolkit TKPrim)"""

import enum
from typing import overload

import nanoocp.BRep
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.TopoDS
import nanoocp.gp


class BRepPrim_Direction(enum.IntEnum):
    BRepPrim_XMin = 0

    BRepPrim_XMax = 1

    BRepPrim_YMin = 2

    BRepPrim_YMax = 3

    BRepPrim_ZMin = 4

    BRepPrim_ZMax = 5

BRepPrim_XMin: BRepPrim_Direction = BRepPrim_Direction.BRepPrim_XMin

BRepPrim_XMax: BRepPrim_Direction = BRepPrim_Direction.BRepPrim_XMax

BRepPrim_YMin: BRepPrim_Direction = BRepPrim_Direction.BRepPrim_YMin

BRepPrim_YMax: BRepPrim_Direction = BRepPrim_Direction.BRepPrim_YMax

BRepPrim_ZMin: BRepPrim_Direction = BRepPrim_Direction.BRepPrim_ZMin

BRepPrim_ZMax: BRepPrim_Direction = BRepPrim_Direction.BRepPrim_ZMax

class BRepPrim_Builder:
    """implements the abstract Builder with the BRep Builder"""

    @overload
    def __init__(self) -> None:
        """
        Creates an empty, useless Builder. Necesseray for
        compilation.
        """

    @overload
    def __init__(self, B: nanoocp.BRep.BRep_Builder) -> None:
        """Creates from a Builder."""

    @overload
    def __init__(self, theOther: BRepPrim_Builder) -> None: ...

    def Builder(self) -> nanoocp.BRep.BRep_Builder: ...

    def MakeShell(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Make a empty Shell."""

    def MakeFace(self, F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pln) -> None:
        """
        Returns in <F> a Face built with the plane
        equation <P>. Used by all primitives.
        """

    def MakeWire(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Returns in <W> an empty Wire."""

    def MakeDegeneratedEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Returns in <E> a degenerated edge."""

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.gp.gp_Lin) -> None:
        """
        Returns in <E> an Edge built with the line
        equation <L>.
        """

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.gp.gp_Circ) -> None:
        """
        Returns in <E> an Edge built with the circle
        equation <C>.
        """

    @overload
    def SetPCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.gp.gp_Lin2d) -> None:
        """
        Sets the line <L> to be the curve representing the
        edge <E> in the parametric space of the surface of
        <F>.
        """

    @overload
    def SetPCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, L1: nanoocp.gp.gp_Lin2d, L2: nanoocp.gp.gp_Lin2d) -> None:
        """
        Sets the lines <L1,L2> to be the curves
        representing the edge <E> in the parametric space
        of the closed surface of <F>.
        """

    @overload
    def SetPCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, C: nanoocp.gp.gp_Circ2d) -> None:
        """
        Sets the circle <C> to be the curve representing
        the edge <E> in the parametric space of the
        surface of <F>.
        """

    def MakeVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> None:
        """Returns in <V> a Vertex built with the point <P>."""

    def ReverseFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Reverses the Face <F>."""

    @overload
    def AddEdgeVertex(self, E: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex, P: float, direct: bool) -> None:
        """
        Adds the Vertex <V> in the Edge <E>. <P> is the
        parameter of the vertex on the edge. If direct
        is False the Vertex is reversed.
        """

    @overload
    def AddEdgeVertex(self, E: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex, P1: float, P2: float) -> None:
        """
        Adds the Vertex <V> in the Edge <E>. <P1,P2>
        are the parameters of the vertex on the closed
        edge.
        """

    def SetParameters(self, E: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex, P1: float, P2: float) -> None:
        """
        <P1,P2> are the parameters of the vertex on the
        edge. The edge is a closed curve.
        """

    def AddWireEdge(self, W: nanoocp.TopoDS.TopoDS_Wire, E: nanoocp.TopoDS.TopoDS_Edge, direct: bool) -> None:
        """
        Adds the Edge <E> in the Wire <W>, if direct is
        False the Edge is reversed.
        """

    def AddFaceWire(self, F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Adds the Wire <W> in the Face <F>."""

    def AddShellFace(self, Sh: nanoocp.TopoDS.TopoDS_Shell, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Adds the Face <F> in the Shell <Sh>."""

    def CompleteEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        This is called once an edge is completed. It gives
        the opportunity to perform any post treatment.
        """

    def CompleteWire(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        This is called once a wire is completed. It gives
        the opportunity to perform any post treatment.
        """

    def CompleteFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        This is called once a face is completed. It gives
        the opportunity to perform any post treatment.
        """

    def CompleteShell(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """
        This is called once a shell is completed. It gives
        the opportunity to perform any post treatment.
        """

class BRepPrim_OneAxis:
    """
    Algorithm to build primitives with one axis of
    revolution.

    The revolution body is described by:

    A coordinate system (Ax2 from gp). The Z axis is
    the rotational axis.

    An Angle around the Axis, When the Angle is 2*PI
    the primitive is not limited by planar faces. The
    U parameter range from 0 to Angle.

    A parameter range VMin, VMax on the meridian.

    A meridian: The meridian is a curve described by
    a set of deferred methods.

    The topology consists of A shell, Faces, Wires,
    Edges and Vertices. Methods are provided to build
    all the elements. Building an element implies the
    automatic building of all its sub-elements.

    So building the shell builds everything.

    There are at most 5 faces:

    - The LateralFace.
    - The TopFace and the BottomFace.
    - The StartFace and the EndFace.
    """

    def SetMeridianOffset(self, MeridianOffset: float = 0.0) -> None:
        """
        The MeridianOffset is added to the parameters on
        the meridian curve and to the V values of the
        pcurves. This is used for the sphere for example,
        to give a range on the meridian edge which is not
        VMin, VMax.
        """

    @overload
    def Axes(self) -> nanoocp.gp.gp_Ax2:
        """Returns the Ax2 from <me>."""

    @overload
    def Axes(self, A: nanoocp.gp.gp_Ax2) -> None: ...

    @overload
    def Angle(self) -> float: ...

    @overload
    def Angle(self, A: float) -> None: ...

    @overload
    def VMin(self) -> float: ...

    @overload
    def VMin(self, V: float) -> None: ...

    @overload
    def VMax(self) -> float: ...

    @overload
    def VMax(self, V: float) -> None: ...

    def MakeEmptyLateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns a face with no edges. The surface is the
        lateral surface with normals pointing outward. The
        U parameter is the angle with the origin on the X
        axis. The V parameter is the parameter of the
        meridian.
        """

    def MakeEmptyMeridianEdge(self, Ang: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns an edge with a 3D curve made from the
        meridian in the XZ plane rotated by <Ang> around
        the Z-axis. Ang may be 0 or myAngle.
        """

    def SetMeridianPCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Sets the parametric curve of the edge <E> in the
        face <F> to be the 2d representation of the
        meridian.
        """

    def MeridianValue(self, V: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the meridian point at parameter <V> in the
        plane XZ.
        """

    def MeridianOnAxis(self, V: float) -> bool:
        """
        Returns True if the point of parameter <V> on the
        meridian is on the Axis. Default implementation is
        std::abs(MeridianValue(V).X()) < Precision::Confusion()
        """

    def MeridianClosed(self) -> bool:
        """
        Returns True if the meridian is closed.
        Default implementation is:
        MeridianValue(VMin).IsEqual(MeridianValue(VMax),
        Precision::Confusion())
        """

    def VMaxInfinite(self) -> bool:
        """
        Returns True if VMax is infinite.
        Default Precision::IsPositiveInfinite(VMax);
        """

    def VMinInfinite(self) -> bool:
        """
        Returns True if VMin is infinite.
        Default Precision::IsNegativeInfinite(VMax);
        """

    def HasTop(self) -> bool:
        """
        Returns True if there is a top face.

        That is neither: VMaxInfinite()
        MeridianClosed()
        MeridianOnAxis(VMax)
        """

    def HasBottom(self) -> bool:
        """
        Returns True if there is a bottom face.

        That is neither: VMinInfinite()
        MeridianClosed()
        MeridianOnAxis(VMin)
        """

    def HasSides(self) -> bool:
        """
        Returns True if there are Start and End faces.

        That is: 2*PI - Angle > Precision::Angular()
        """

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """
        Returns the Shell containing all the Faces of the
        primitive.
        """

    def LateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the lateral Face. It is oriented toward
        the outside of the primitive.
        """

    def TopFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the top planar Face. It is Oriented
        toward the +Z axis (outside).
        """

    def BottomFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the Bottom planar Face. It is Oriented
        toward the -Z axis (outside).
        """

    def StartFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the Face starting the slice, it is
        oriented toward the exterior of the primitive.
        """

    def EndFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the Face ending the slice, it is oriented
        toward the exterior of the primitive.
        """

    def LateralWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the wire in the lateral face."""

    def LateralStartWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the wire in the lateral face with the
        start edge.
        """

    def LateralEndWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the wire with in lateral face with the end
        edge.
        """

    def TopWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the wire in the top face."""

    def BottomWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the wire in the bottom face."""

    def StartWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the wire in the start face."""

    def AxisStartWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the wire in the start face with the
        AxisEdge.
        """

    def EndWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the Wire in the end face."""

    def AxisEndWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the Wire in the end face with the
        AxisEdge.
        """

    def AxisEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the Edge built along the Axis and oriented
        on +Z of the Axis.
        """

    def StartEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the Edge at angle 0."""

    def EndEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the Edge at angle Angle. If !HasSides()
        the StartEdge and the EndEdge are the same edge.
        """

    def StartTopEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the linear Edge between start Face and top
        Face.
        """

    def StartBottomEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the linear Edge between start Face and
        bottom Face.
        """

    def EndTopEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the linear Edge between end Face and top
        Face.
        """

    def EndBottomEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the linear Edge between end Face and
        bottom Face.
        """

    def TopEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge at VMax. If MeridianClosed() the
        TopEdge and the BottomEdge are the same edge.
        """

    def BottomEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge at VMin. If MeridianClosed() the
        TopEdge and the BottomEdge are the same edge.
        """

    def AxisTopVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the Vertex at the Top altitude on the axis."""

    def AxisBottomVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the Vertex at the Bottom altitude on the
        axis.
        """

    def TopStartVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the vertex (0,VMax)"""

    def TopEndVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the vertex (angle,VMax)"""

    def BottomStartVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the vertex (0,VMin)"""

    def BottomEndVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the vertex (angle,VMax)"""

class BRepPrim_Revolution(BRepPrim_OneAxis):
    """
    Implement the OneAxis algorithm for a revolution
    surface.
    """

    @overload
    def __init__(self, A: nanoocp.gp.gp_Ax2, VMin: float, VMax: float, M: nanoocp.Geom.Geom_Curve | None, PM: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """
        Create a revolution body <M> is the meridian nd
        must be in the XZ plane of <A>. <PM> is the
        meridian in the XZ plane.
        """

    @overload
    def __init__(self, theOther: BRepPrim_Revolution) -> None: ...

    def MakeEmptyLateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        The surface normal should be directed towards the
        outside.
        """

    def MakeEmptyMeridianEdge(self, Ang: float) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns an edge with a 3D curve made from the
        meridian in the XZ plane rotated by <Ang> around
        the Z-axis. Ang may be 0 or myAngle.
        """

    def MeridianValue(self, V: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the meridian point at parameter <V> in the
        plane XZ.
        """

    def SetMeridianPCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Sets the parametric urve of the edge <E> in the
        face <F> to be the 2d representation of the
        meridian.
        """

class BRepPrim_Cone(BRepPrim_Revolution):
    """Implement the cone primitive."""

    @overload
    def __init__(self, Angle: float) -> None:
        """infinite cone at origin on Z negative"""

    @overload
    def __init__(self, Angle: float, Apex: nanoocp.gp.gp_Pnt) -> None:
        """infinite cone at Apex on Z negative"""

    @overload
    def __init__(self, Angle: float, Axes: nanoocp.gp.gp_Ax2) -> None:
        """infinite cone with Axes"""

    @overload
    def __init__(self, Angle: float, Position: nanoocp.gp.gp_Ax2, Height: float, Radius: float = 0.0) -> None:
        """
        the STEP definition
        Angle = semi-angle of the cone
        Position : the coordinate system
        Height : height of the cone.
        Radius : radius of truncated face at z = 0

        The apex is on z < 0

        Errors : Height < Resolution
        Angle < Resolution / Height
        Angle > PI/2 - Resolution / Height
        """

    @overload
    def __init__(self, R1: float, R2: float, H: float) -> None:
        """
        create a Cone at origin on Z axis, of height H,
        radius R1 at Z = 0, R2 at Z = H, X is the origin
        of angles. If R1 or R2 is 0 there is an apex.
        Otherwise, it is a truncated cone.

        Error  : R1 and R2 < Resolution
        R1 or R2 negative
        std::abs(R1-R2) < Resolution
        H < Resolution
        H negative
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, R1: float, R2: float, H: float) -> None:
        """same as above but at a given point"""

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float, H: float) -> None:
        """same as above with given axes system."""

    @overload
    def __init__(self, theOther: BRepPrim_Cone) -> None: ...

    def MakeEmptyLateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        The surface normal should be directed towards the
        outside.
        """

class BRepPrim_Cylinder(BRepPrim_Revolution):
    """Cylinder primitive."""

    @overload
    def __init__(self, Radius: float) -> None:
        """infinite Cylinder at origin on Z negative"""

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, Radius: float) -> None:
        """infinite Cylinder at Center on Z negative"""

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, Radius: float) -> None:
        """infinite Cylinder at Axes on Z negative"""

    @overload
    def __init__(self, R: float, H: float) -> None:
        """
        create a Cylinder at origin on Z axis, of
        height H and radius R
        Error : Radius < Resolution
        H < Resolution
        H negative
        """

    @overload
    def __init__(self, Position: nanoocp.gp.gp_Ax2, Radius: float, Height: float) -> None:
        """
        the STEP definition
        Position : center of a Face and Axis
        Radius : radius of cylinder
        Height : distance between faces
        on positive side

        Errors : Height < Resolution
        Radius < Resolution
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, R: float, H: float) -> None:
        """same as above but at a given point"""

    @overload
    def __init__(self, theOther: BRepPrim_Cylinder) -> None: ...

    def MakeEmptyLateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        The surface normal should be directed towards the
        outside.
        """

class BRepPrim_FaceBuilder:
    """
    The FaceBuilder is an algorithm to build a BRep
    Face from a Geom Surface.

    The face covers the whole surface or the area
    delimited by UMin, UMax, VMin, VMax
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, B: nanoocp.BRep.BRep_Builder, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def __init__(self, B: nanoocp.BRep.BRep_Builder, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepPrim_FaceBuilder) -> None: ...

    @overload
    def Init(self, B: nanoocp.BRep.BRep_Builder, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def Init(self, B: nanoocp.BRep.BRep_Builder, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Edge(self, I: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge of index <I>
        1 - Edge VMin
        2 - Edge UMax
        3 - Edge VMax
        4 - Edge UMin
        """

    def Vertex(self, I: int) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the vertex of index <I>
        1 - Vertex UMin,VMin
        2 - Vertex UMax,VMin
        3 - Vertex UMax,VMax
        4 - Vertex UMin,VMax
        """

class BRepPrim_GWedge:
    """
    A wedge is defined by:

    Axes: an Axis2 (coordinate system)

    YMin, YMax the coordinates of the ymin and ymax
    rectangular faces parallel to the ZX plane (of the
    coordinate systems)

    ZMin, ZMax, XMin, XMax the rectangular
    left (YMin) face parallel to the Z and X axes.

    Z2Min, Z2Max, X2Min, X2Max the rectangular
    right (YMax) face parallel to the Z and X axes.

    For a box Z2Min = ZMin, Z2Max = ZMax,
    X2Min = XMin, X2Max = XMax

    The wedge can be open in the corresponding direction
    of its Boolean myInfinite
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, B: BRepPrim_Builder, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float) -> None:
        """
        Creates a GWedge algorithm. <Axes> is the axis
        system for the primitive.

        XMin, YMin, ZMin are set to 0
        XMax, YMax, ZMax are set to dx, dy, dz
        Z2Min = ZMin
        Z2Max = ZMax
        X2Min = XMin
        X2Max = XMax
        The result is a box
        dx,dy,dz should be positive
        """

    @overload
    def __init__(self, B: BRepPrim_Builder, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float, ltx: float) -> None:
        """
        Creates a GWedge primitive. <Axes> is the axis
        system for the primitive.

        XMin, YMin, ZMin are set to 0
        XMax, YMax, ZMax are set to dx, dy, dz
        Z2Min = ZMin
        Z2Max = ZMax
        X2Min = ltx
        X2Max = ltx
        The result is a STEP right angular wedge
        dx,dy,dz should be positive
        ltx should not be negative
        """

    @overload
    def __init__(self, B: BRepPrim_Builder, Axes: nanoocp.gp.gp_Ax2, xmin: float, ymin: float, zmin: float, z2min: float, x2min: float, xmax: float, ymax: float, zmax: float, z2max: float, x2max: float) -> None:
        """
        Create a GWedge primitive. <Axes> is the axis
        system for the primitive.

        all the fields are set to the corresponding value
        XYZMax - XYZMin should be positive
        ZX2Max - ZX2Min should not be negative
        """

    @overload
    def __init__(self, theOther: BRepPrim_GWedge) -> None: ...

    def Axes(self) -> nanoocp.gp.gp_Ax2:
        """Returns the coordinates system from <me>."""

    def GetXMin(self) -> float:
        """Returns Xmin value from <me>."""

    def GetYMin(self) -> float:
        """Returns YMin value from <me>."""

    def GetZMin(self) -> float:
        """Returns ZMin value from <me>."""

    def GetZ2Min(self) -> float:
        """Returns Z2Min value from <me>."""

    def GetX2Min(self) -> float:
        """Returns X2Min value from <me>."""

    def GetXMax(self) -> float:
        """Returns XMax value from <me>."""

    def GetYMax(self) -> float:
        """Returns YMax value from <me>."""

    def GetZMax(self) -> float:
        """Returns ZMax value from <me>."""

    def GetZ2Max(self) -> float:
        """Returns Z2Max value from <me>."""

    def GetX2Max(self) -> float:
        """Returns X2Max value from <me>."""

    def Open(self, d1: BRepPrim_Direction) -> None:
        """
        Opens <me> in <d1> direction. A face and its edges
        or vertices are said nonexistent.
        """

    def Close(self, d1: BRepPrim_Direction) -> None:
        """
        Closes <me> in <d1> direction. A face and its
        edges or vertices are said existent.
        """

    def IsInfinite(self, d1: BRepPrim_Direction) -> bool:
        """Returns True if <me> is open in <d1> direction."""

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the Shell containing the Faces of <me>."""

    def HasFace(self, d1: BRepPrim_Direction) -> bool:
        """Returns True if <me> has a Face in <d1> direction."""

    def Face(self, d1: BRepPrim_Direction) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the Face of <me> located in <d1> direction."""

    def Plane(self, d1: BRepPrim_Direction) -> nanoocp.gp.gp_Pln:
        """
        Returns the plane of the Face of <me> located in
        <d1> direction.
        """

    def HasWire(self, d1: BRepPrim_Direction) -> bool:
        """Returns True if <me> has a Wire in <d1> direction."""

    def Wire(self, d1: BRepPrim_Direction) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the Wire of <me> located in <d1> direction."""

    def HasEdge(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction) -> bool:
        """Returns True if <me> has an Edge in <d1><d2> direction."""

    def Edge(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the Edge of <me> located in <d1><d2> direction."""

    def Line(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction) -> nanoocp.gp.gp_Lin:
        """
        Returns the line of the Edge of <me> located in
        <d1><d2> direction.
        """

    def HasVertex(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction, d3: BRepPrim_Direction) -> bool:
        """
        Returns True if <me> has a Vertex in <d1><d2><d3>
        direction.
        """

    def Vertex(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction, d3: BRepPrim_Direction) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the Vertex of <me> located in <d1><d2><d3>
        direction.
        """

    def Point(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction, d3: BRepPrim_Direction) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point of the Vertex of <me> located in
        <d1><d2><d3> direction.
        """

    def IsDegeneratedShape(self) -> bool:
        """
        Checks a shape on degeneracy
        @return TRUE if a shape is degenerated
        """

class BRepPrim_Sphere(BRepPrim_Revolution):
    """Implements the sphere primitive"""

    @overload
    def __init__(self, Radius: float) -> None:
        """
        Creates a Sphere at origin with Radius. The axes
        of the sphere are the reference axes. An error is
        raised if the radius is < Resolution.
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, Radius: float) -> None:
        """
        Creates a Sphere with Center and Radius.
        Axes are the reference axes.
        This is the STEP constructor.
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, Radius: float) -> None:
        """Creates a sphere with given axes system."""

    @overload
    def __init__(self, theOther: BRepPrim_Sphere) -> None: ...

    def MakeEmptyLateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        The surface normal should be directed towards the
        outside.
        """

class BRepPrim_Torus(BRepPrim_Revolution):
    """Implements the torus primitive"""

    @overload
    def __init__(self, Major: float, Minor: float) -> None:
        """Torus centered at origin"""

    @overload
    def __init__(self, Position: nanoocp.gp.gp_Ax2, Major: float, Minor: float) -> None:
        """
        the STEP definition
        Position : center and axes
        Major, Minor : Radii

        Errors : Major < Resolution
        Minor < Resolution
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, Major: float, Minor: float) -> None:
        """Torus at Center"""

    @overload
    def __init__(self, theOther: BRepPrim_Torus) -> None: ...

    def MakeEmptyLateralFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        The surface normal should be directed towards the
        outside.
        """

class BRepPrim_Wedge(BRepPrim_GWedge):
    """Provides constructors without Builders."""

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float) -> None:
        """
        Creates a Wedge algorithm. <Axes> is the axis
        system for the primitive.

        XMin, YMin, ZMin are set to 0
        XMax, YMax, ZMax are set to dx, dy, dz
        Z2Min = ZMin
        Z2Max = ZMax
        X2Min = XMin
        X2Max = XMax
        The result is a box
        dx,dy,dz should be positive
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float, ltx: float) -> None:
        """
        Creates a Wedge primitive. <Axes> is the axis
        system for the primitive.

        XMin, YMin, ZMin are set to 0
        XMax, YMax, ZMax are set to dx, dy, dz
        Z2Min = ZMin
        Z2Max = ZMax
        X2Min = ltx
        X2Max = ltx
        The result is a STEP right angular wedge
        dx,dy,dz should be positive
        ltx should not be negative
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, xmin: float, ymin: float, zmin: float, z2min: float, x2min: float, xmax: float, ymax: float, zmax: float, z2max: float, x2max: float) -> None:
        """
        Create a Wedge primitive. <Axes> is the axis
        system for the primitive.

        all the fields are set to the corresponding value
        XYZMax - XYZMin should be positive
        ZX2Max - ZX2Min should not be negative
        """

    @overload
    def __init__(self, theOther: BRepPrim_Wedge) -> None: ...
