"""OCCT package BRepAdaptor (toolkit TKBRep)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.Geom
import nanoocp.Geom2dAdaptor
import nanoocp.GeomAbs
import nanoocp.GeomAdaptor
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp


class BRepAdaptor_Curve(nanoocp.GeomAdaptor.GeomAdaptor_TransformedCurve):
    """
    The Curve from BRepAdaptor allows to use an Edge
    of the BRep topology like a 3D curve.

    It has the methods the class Curve from Adaptor3d.

    It is created or Initialized with an Edge. It
    takes into account local coordinate systems. If
    the Edge has a 3D curve it is use with priority.
    If the edge has no 3D curve one of the curves on
    surface is used. It is possible to enforce using a
    curve on surface by creating or initialising with
    an Edge and a Face.
    """

    @overload
    def __init__(self) -> None:
        """Creates an undefined Curve with no Edge loaded."""

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Creates a Curve to access the geometry of edge <E>."""

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Creates a Curve to access the geometry of edge
        <E>. The geometry will be computed using the
        parametric curve of <E> on the face <F>. An Error
        is raised if the edge does not have a pcurve on
        the face.
        """

    @overload
    def __init__(self, theOther: BRepAdaptor_Curve) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    def Reset(self) -> None:
        """Reset currently loaded curve (undone Load())."""

    @overload
    def Initialize(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Sets the Curve <me> to access the geometry of
        edge <E>.
        """

    @overload
    def Initialize(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Sets the Curve <me> to access the geometry of
        edge <E>. The geometry will be computed using the
        parametric curve of <E> on the face <F>. An Error
        is raised if the edge does not have a pcurve on
        the face.
        """

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the edge."""

    def Tolerance(self) -> float:
        """Returns the edge tolerance."""

    def Trim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        """

class BRepAdaptor_CompCurve(nanoocp.Adaptor3d.Adaptor3d_Curve):
    """
    The Curve from BRepAdaptor allows to use a Wire
    of the BRep topology like a 3D curve.
    Warning: With this class of curve, C0 and C1 continuities
    are not assumed. So be careful with some algorithm!
    Please note that BRepAdaptor_CompCurve cannot be
    periodic curve at all (even if it contains single
    periodic edge).

    BRepAdaptor_CompCurve can only work on valid wires where all edges are
    connected to each other to make a chain.
    """

    @overload
    def __init__(self) -> None:
        """Creates an undefined Curve with no Wire loaded."""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, KnotByCurvilinearAbcissa: bool = False) -> None: ...

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, KnotByCurvilinearAbcissa: bool, First: float, Last: float, Tol: float) -> None:
        """Creates a Curve to access the geometry of edge <W>."""

    @overload
    def __init__(self, theOther: BRepAdaptor_CompCurve) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """Shallow copy of adaptor."""

    @overload
    def Initialize(self, W: nanoocp.TopoDS.TopoDS_Wire, KnotByCurvilinearAbcissa: bool) -> None:
        """Sets the wire <W>."""

    @overload
    def Initialize(self, W: nanoocp.TopoDS.TopoDS_Wire, KnotByCurvilinearAbcissa: bool, First: float, Last: float, Tol: float) -> None:
        """Sets wire <W> and trimmed parameter."""

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the wire."""

    def Edge(self, U: float, E: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """
        returns an edge and one parameter on them
        corresponding to the parameter U.
        """

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> nanoocp.Adaptor3d.Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter theU on the curve."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """
        Computes the point of parameter theU on the curve with its first derivative.
        Raised if the continuity of the current interval is not C1.
        """

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """
        Returns the point and the first and second derivatives at parameter theU.
        Raised if the continuity of the current interval is not C2.
        """

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """
        Returns the point and the first, second and third derivatives at parameter theU.
        Raised if the continuity of the current interval is not C3.
        """

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """
        Returns the derivative of order theN at parameter theU.
        Raised if the continuity of the current interval is not CN.
        Raised if theN < 1.
        """

    def Resolution(self, R3d: float) -> float:
        """returns the parametric resolution"""

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

class BRepAdaptor_Curve2d(nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve):
    """
    The Curve2d from BRepAdaptor allows to use an Edge
    on a Face like a 2d curve (curve in the parametric
    space).

    It has the methods of the class Curve2d from
    Adpator.

    It is created or initialized with a Face and an
    Edge. The methods are inherited from Curve from
    Geom2dAdaptor.
    """

    @overload
    def __init__(self) -> None:
        """Creates an uninitialized curve2d."""

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Creates with the pcurve of <E> on <F>."""

    @overload
    def __init__(self, theOther: BRepAdaptor_Curve2d) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Shallow copy of adaptor"""

    def Initialize(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initialize with the pcurve of <E> on <F>."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the Edge."""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the Face."""

class BRepAdaptor_Surface(nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface):
    """
    The Surface from BRepAdaptor allows to use a Face
    of the BRep topology look like a 3D surface.

    It has the methods of the class Surface from
    Adaptor3d.

    It is created or initialized with a Face. It takes
    into account the local coordinates system.

    The u,v parameter range is the minmax value for
    the restriction, unless the flag restriction is
    set to false.
    """

    @overload
    def __init__(self) -> None:
        """Creates an undefined surface with no face loaded."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, R: bool = True) -> None:
        """
        Creates a surface to access the geometry of <F>.
        If <Restriction> is true the parameter range is
        the parameter range in the UV space of the
        restriction.
        """

    @overload
    def __init__(self, theOther: BRepAdaptor_Surface) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Shallow copy of adaptor."""

    def Initialize(self, F: nanoocp.TopoDS.TopoDS_Face, Restriction: bool = True) -> None:
        """Sets the surface to the geometry of <F>."""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the face."""

    def Tolerance(self) -> float:
        """Returns the face tolerance."""
