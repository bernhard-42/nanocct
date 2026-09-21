"""OCCT package TopOpeBRepDS (toolkit TKBool)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopOpeBRepTool
import nanoocp.TopoDS
import nanoocp.gp


class TopOpeBRepDS_Kind(enum.IntEnum):
    """different types of objects in DataStructure"""

    TopOpeBRepDS_POINT = 0

    TopOpeBRepDS_CURVE = 1

    TopOpeBRepDS_SURFACE = 2

    TopOpeBRepDS_VERTEX = 3

    TopOpeBRepDS_EDGE = 4

    TopOpeBRepDS_WIRE = 5

    TopOpeBRepDS_FACE = 6

    TopOpeBRepDS_SHELL = 7

    TopOpeBRepDS_SOLID = 8

    TopOpeBRepDS_COMPSOLID = 9

    TopOpeBRepDS_COMPOUND = 10

    TopOpeBRepDS_UNKNOWN = 11

TopOpeBRepDS_POINT: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_POINT

TopOpeBRepDS_CURVE: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_CURVE

TopOpeBRepDS_SURFACE: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_SURFACE

TopOpeBRepDS_VERTEX: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_VERTEX

TopOpeBRepDS_EDGE: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_EDGE

TopOpeBRepDS_WIRE: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_WIRE

TopOpeBRepDS_FACE: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_FACE

TopOpeBRepDS_SHELL: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_SHELL

TopOpeBRepDS_SOLID: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_SOLID

TopOpeBRepDS_COMPSOLID: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_COMPSOLID

TopOpeBRepDS_COMPOUND: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_COMPOUND

TopOpeBRepDS_UNKNOWN: TopOpeBRepDS_Kind = TopOpeBRepDS_Kind.TopOpeBRepDS_UNKNOWN

class TopOpeBRepDS_Config(enum.IntEnum):
    TopOpeBRepDS_UNSHGEOMETRY = 0

    TopOpeBRepDS_SAMEORIENTED = 1

    TopOpeBRepDS_DIFFORIENTED = 2

TopOpeBRepDS_UNSHGEOMETRY: TopOpeBRepDS_Config = TopOpeBRepDS_Config.TopOpeBRepDS_UNSHGEOMETRY

TopOpeBRepDS_SAMEORIENTED: TopOpeBRepDS_Config = TopOpeBRepDS_Config.TopOpeBRepDS_SAMEORIENTED

TopOpeBRepDS_DIFFORIENTED: TopOpeBRepDS_Config = TopOpeBRepDS_Config.TopOpeBRepDS_DIFFORIENTED

class TopOpeBRepDS_CheckStatus(enum.IntEnum):
    TopOpeBRepDS_OK = 0

    TopOpeBRepDS_NOK = 1

TopOpeBRepDS_OK: TopOpeBRepDS_CheckStatus = TopOpeBRepDS_CheckStatus.TopOpeBRepDS_OK

TopOpeBRepDS_NOK: TopOpeBRepDS_CheckStatus = TopOpeBRepDS_CheckStatus.TopOpeBRepDS_NOK

class TopOpeBRepDS:
    """
    This package provides services used by the TopOpeBRepBuild
    package performing topological operations on the BRep
    data structure.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS) -> None: ...

    @overload
    @staticmethod
    def SPrint(S: nanoocp.TopAbs.TopAbs_State) -> nanoocp.TCollection.TCollection_AsciiString:
        """IN OU ON UN"""

    @overload
    @staticmethod
    def SPrint(K: TopOpeBRepDS_Kind) -> nanoocp.TCollection.TCollection_AsciiString:
        """<K>"""

    @overload
    @staticmethod
    def SPrint(K: TopOpeBRepDS_Kind, I: int, B: nanoocp.TCollection.TCollection_AsciiString = ..., A: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString:
        """S1(<K>,<I>)S2"""

    @overload
    @staticmethod
    def SPrint(T: nanoocp.TopAbs.TopAbs_ShapeEnum) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    @staticmethod
    def SPrint(T: nanoocp.TopAbs.TopAbs_ShapeEnum, I: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """(<T>,<I>)"""

    @overload
    @staticmethod
    def SPrint(O: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    @staticmethod
    def SPrint(C: TopOpeBRepDS_Config) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    @staticmethod
    def Print(S: nanoocp.TopAbs.TopAbs_State) -> object: ...

    @overload
    @staticmethod
    def Print(K: TopOpeBRepDS_Kind) -> object: ...

    @overload
    @staticmethod
    def Print(K: TopOpeBRepDS_Kind, I: int, B: nanoocp.TCollection.TCollection_AsciiString = ..., A: nanoocp.TCollection.TCollection_AsciiString = ...) -> object: ...

    @overload
    @staticmethod
    def Print(T: nanoocp.TopAbs.TopAbs_ShapeEnum, I: int) -> object: ...

    @overload
    @staticmethod
    def Print(C: TopOpeBRepDS_Config) -> object: ...

    @staticmethod
    def IsGeometry(K: TopOpeBRepDS_Kind) -> bool: ...

    @staticmethod
    def IsTopology(K: TopOpeBRepDS_Kind) -> bool: ...

    @staticmethod
    def KindToShape(K: TopOpeBRepDS_Kind) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    @staticmethod
    def ShapeToKind(S: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepDS_Kind: ...

class TopOpeBRepDS_Transition:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def __init__(self, StateBefore: nanoocp.TopAbs.TopAbs_State, StateAfter: nanoocp.TopAbs.TopAbs_State, ShapeBefore: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE, ShapeAfter: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Transition) -> None: ...

    @overload
    def Set(self, StateBefore: nanoocp.TopAbs.TopAbs_State, StateAfter: nanoocp.TopAbs.TopAbs_State, ShapeBefore: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE, ShapeAfter: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...

    @overload
    def Set(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        set the transition corresponding to orientation <O>

        O       Before  After

        FORWARD       OUT    IN
        REVERSED      IN     OUT
        INTERNAL      IN     IN
        EXTERNAL      OUT    OUT
        """

    def StateBefore(self, S: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def StateAfter(self, S: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @overload
    def ShapeBefore(self, SE: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None: ...

    @overload
    def ShapeBefore(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    @overload
    def ShapeAfter(self, SE: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None: ...

    @overload
    def ShapeAfter(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    @overload
    def Before(self, S: nanoocp.TopAbs.TopAbs_State, ShapeBefore: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...

    @overload
    def Before(self) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def After(self, S: nanoocp.TopAbs.TopAbs_State, ShapeAfter: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...

    @overload
    def After(self) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def Index(self, I: int) -> None: ...

    @overload
    def Index(self) -> int: ...

    @overload
    def IndexBefore(self, I: int) -> None: ...

    @overload
    def IndexBefore(self) -> int: ...

    @overload
    def IndexAfter(self, I: int) -> None: ...

    @overload
    def IndexAfter(self) -> int: ...

    def ONBefore(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    def ONAfter(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    def Orientation(self, S: nanoocp.TopAbs.TopAbs_State, T: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        returns the orientation corresponding to state <S>

        Before and After not equal TopAbs_ON :
        --------------------------------------
        Before  After   Computed orientation

        S      not S   REVERSED (we leave state S)
        not S  S       FORWARD  (we enter state S)
        S      S       INTERNAL (we stay in state S)
        not S  not S   EXTERNAL (we stay outside state S)
        """

    def Complement(self) -> TopOpeBRepDS_Transition: ...

    def IsUnknown(self) -> bool:
        """returns True if both states are UNKNOWN"""

class TopOpeBRepDS_Interference(nanoocp.Standard.Standard_Transient):
    """
    An interference is the description of the
    attachment of a new geometry on a geometry. For
    example an intersection point on an Edge or on a
    Curve.

    The Interference contains the following data:

    - Transition: How the interference separates the
    existing geometry in INSIDE and OUTSIDE.

    - SupportType: Type of the object supporting the
    interference. (FACE, EDGE, VERTEX, SURFACE, CURVE).

    - Support: Index in the data structure of the
    object supporting the interference.

    - GeometryType: Type ofthe geometry of the
    interference (SURFACE, CURVE, POINT).

    - Geometry: Index in the data structure of the
    geometry.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, I: TopOpeBRepDS_Interference | None) -> None: ...

    @overload
    def __init__(self, Transition: TopOpeBRepDS_Transition, SupportType: TopOpeBRepDS_Kind, Support: int, GeometryType: TopOpeBRepDS_Kind, Geometry: int) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Interference) -> None: ...

    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...

    @overload
    def Transition(self, T: TopOpeBRepDS_Transition) -> None: ...

    def ChangeTransition(self) -> TopOpeBRepDS_Transition: ...

    def GKGSKS(self) -> tuple[TopOpeBRepDS_Kind, int, TopOpeBRepDS_Kind, int]:
        """return GeometryType + Geometry + SupportType + Support"""

    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...

    @overload
    def SupportType(self, ST: TopOpeBRepDS_Kind) -> None: ...

    @overload
    def Support(self) -> int: ...

    @overload
    def Support(self, S: int) -> None: ...

    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: ...

    @overload
    def GeometryType(self, GT: TopOpeBRepDS_Kind) -> None: ...

    @overload
    def Geometry(self) -> int: ...

    @overload
    def Geometry(self, G: int) -> None: ...

    def SetGeometry(self, GI: int) -> None: ...

    def HasSameSupport(self, Other: TopOpeBRepDS_Interference | None) -> bool: ...

    def HasSameGeometry(self, Other: TopOpeBRepDS_Interference | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_Association(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Association) -> None: ...

    @overload
    def Associate(self, I: TopOpeBRepDS_Interference | None, K: TopOpeBRepDS_Interference | None) -> None: ...

    @overload
    def Associate(self, I: TopOpeBRepDS_Interference | None, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def HasAssociation(self, I: TopOpeBRepDS_Interference | None) -> bool: ...

    def Associated(self, I: TopOpeBRepDS_Interference | None) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def AreAssociated(self, I: TopOpeBRepDS_Interference | None, K: TopOpeBRepDS_Interference | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_BuildTool:
    """
    Provides a Tool to build topologies. Used to
    instantiate the Builder algorithm.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, OutCurveType: nanoocp.TopOpeBRepTool.TopOpeBRepTool_OutCurveType) -> None: ...

    @overload
    def __init__(self, GT: nanoocp.TopOpeBRepTool.TopOpeBRepTool_GeomTool) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_BuildTool) -> None: ...

    def GetGeomTool(self) -> nanoocp.TopOpeBRepTool.TopOpeBRepTool_GeomTool: ...

    def ChangeGeomTool(self) -> nanoocp.TopOpeBRepTool.TopOpeBRepTool_GeomTool: ...

    def MakeVertex(self, V: nanoocp.TopoDS.TopoDS_Shape, P: TopOpeBRepDS_Point) -> None: ...

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Shape, C: TopOpeBRepDS_Curve) -> None: ...

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Shape, C: TopOpeBRepDS_Curve, DS: TopOpeBRepDS_DataStructure) -> None: ...

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom.Geom_Curve | None, Tol: float) -> None: ...

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeWire(self, W: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeFace(self, F: nanoocp.TopoDS.TopoDS_Shape, S: TopOpeBRepDS_Surface) -> None: ...

    def MakeShell(self, Sh: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeSolid(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def CopyEdge(self, Ein: nanoocp.TopoDS.TopoDS_Shape, Eou: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Make an edge <Eou> with the curve of the edge <Ein>"""

    def GetOrientedEdgeVertices(self, E: nanoocp.TopoDS.TopoDS_Edge, Vmin: nanoocp.TopoDS.TopoDS_Vertex, Vmax: nanoocp.TopoDS.TopoDS_Vertex) -> tuple[float, float]: ...

    def UpdateEdgeCurveTol(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge, C3Dnew: nanoocp.Geom.Geom_Curve | None, tol3d: float, tol2d1: float, tol2d2: float) -> tuple[float, float, float]: ...

    def ApproxCurves(self, C: TopOpeBRepDS_Curve, E: nanoocp.TopoDS.TopoDS_Edge, HDS: TopOpeBRepDS_HDataStructure | None) -> int: ...

    def ComputePCurves(self, C: TopOpeBRepDS_Curve, E: nanoocp.TopoDS.TopoDS_Edge, newC: TopOpeBRepDS_Curve, CompPC1: bool, CompPC2: bool, CompC3D: bool) -> None: ...

    def PutPCurves(self, newC: TopOpeBRepDS_Curve, E: nanoocp.TopoDS.TopoDS_Edge, CompPC1: bool, CompPC2: bool) -> None: ...

    def RecomputeCurves(self, C: TopOpeBRepDS_Curve, oldE: nanoocp.TopoDS.TopoDS_Edge, E: nanoocp.TopoDS.TopoDS_Edge, HDS: TopOpeBRepDS_HDataStructure | None) -> int: ...

    def CopyFace(self, Fin: nanoocp.TopoDS.TopoDS_Shape, Fou: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Make a face <Fou> with the surface of the face <Fin>"""

    @overload
    def AddEdgeVertex(self, Ein: nanoocp.TopoDS.TopoDS_Shape, Eou: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def AddEdgeVertex(self, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddWireEdge(self, W: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddFaceWire(self, F: nanoocp.TopoDS.TopoDS_Shape, W: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddShellFace(self, Sh: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddSolidShell(self, S: nanoocp.TopoDS.TopoDS_Shape, Sh: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Parameter(self, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape, P: float) -> None:
        """
        Sets the parameter <P> for the vertex <V> on the
        edge <E>.
        """

    @overload
    def Parameter(self, C: TopOpeBRepDS_Curve, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Compute the parameter of the vertex <V>, supported
        by the edge <E>, on the curve <C>.
        """

    def Range(self, E: nanoocp.TopoDS.TopoDS_Shape, first: float, last: float) -> None:
        """Sets the range of edge <E>."""

    def UpdateEdge(self, Ein: nanoocp.TopoDS.TopoDS_Shape, Eou: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets the range of edge <Eou> from <Ein>
        only when <Ein> has a closed geometry.
        """

    def Curve3D(self, E: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom.Geom_Curve | None, Tol: float) -> None:
        """Sets the curve <C> for the edge <E>"""

    @overload
    def PCurve(self, F: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """
        Sets the pcurve <C> for the edge <E> on the face
        <F>. If OverWrite is True the old pcurve if there
        is one is overwritten, else the two pcurves are
        set.
        """

    @overload
    def PCurve(self, F: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, CDS: TopOpeBRepDS_Curve, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def Orientation(self, S: nanoocp.TopoDS.TopoDS_Shape, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Orientation(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def Closed(self, S: nanoocp.TopoDS.TopoDS_Shape, B: bool) -> None: ...

    def Approximation(self) -> bool: ...

    @overload
    def UpdateSurface(self, F: nanoocp.TopoDS.TopoDS_Shape, SU: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def UpdateSurface(self, E: nanoocp.TopoDS.TopoDS_Shape, oldF: nanoocp.TopoDS.TopoDS_Shape, newF: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def OverWrite(self) -> bool: ...

    @overload
    def OverWrite(self, O: bool) -> None: ...

    @overload
    def Translate(self) -> bool: ...

    @overload
    def Translate(self, T: bool) -> None: ...

class TopOpeBRepDS_Check(nanoocp.Standard.Standard_Transient):
    """a tool verifying integrity and structure of DS"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Check) -> None: ...

    def ChkIntg(self) -> bool:
        """Check integrition of DS"""

    def ChkIntgInterf(self, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> bool:
        """
        Check integrition of interferences
        (les supports et les geometries de LI)
        """

    def CheckDS(self, i: int, K: TopOpeBRepDS_Kind) -> bool:
        """
        Verifie que le ieme element de la DS existe, et
        pour un K de type topologique, verifie qu'il est du
        bon type (VERTEX, EDGE, WIRE, FACE, SHELL ou SOLID)
        """

    def ChkIntgSamDom(self) -> bool:
        """Check integrition des champs SameDomain de la DS"""

    def CheckShapes(self, LS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Verifie que les Shapes existent bien dans la DS
        Utile pour les Shapes SameDomain
        si la liste est vide, renvoie vrai
        """

    def OneVertexOnPnt(self) -> bool:
        """
        Verifie que les Vertex non SameDomain sont bien
        nonSameDomain, que les vertex sameDomain sont bien
        SameDomain, que les Points sont non confondus
        ni entre eux, ni avec des Vertex.
        """

    def HDS(self) -> TopOpeBRepDS_HDataStructure: ...

    def ChangeHDS(self) -> TopOpeBRepDS_HDataStructure: ...

    def PrintIntg(self) -> object: ...

    def Print(self, stat: TopOpeBRepDS_CheckStatus) -> object:
        """Prints the name of CheckStatus <stat> as a String"""

    @overload
    def PrintShape(self, SE: nanoocp.TopAbs.TopAbs_ShapeEnum) -> object: ...

    @overload
    def PrintShape(self, index: int) -> object:
        """Prints the name of CheckStatus <stat> as a String"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_ShapeShapeInterference(TopOpeBRepDS_Interference):
    """Interference"""

    @overload
    def __init__(self, T: TopOpeBRepDS_Transition, ST: TopOpeBRepDS_Kind, S: int, GT: TopOpeBRepDS_Kind, G: int, GBound: bool, C: TopOpeBRepDS_Config) -> None:
        """
        a shape interferes on shape <G> with shape <S>.
        examples :
        create a ShapeShapeInterference describing :
        vertex V of edge E1 found on edge E2 :
        ST,S,GT,G = TopOpeBRepDS_EDGE,E2,TopOpeBRepDS_VERTEX,V

        create a ShapeShapeInterference describing
        vertex V of edge E found on face F :
        ST,S,GT,G = TopOpeBRepDS_FACE,F,TopOpeBRepDS_VERTEX,V

        <GBound> indicates if shape <G> is a bound of shape <S>.

        <SCC> :
        UNSH_GEOMETRY :
        <S> and <Ancestor> have any types,
        <S> and <Ancestor> don't share the same geometry
        SAME_ORIENTED :
        <S> and <Ancestor> have identical types,
        <S> and <Ancestor> orientations are IDENTICAL.
        DIFF_ORIENTED :
        <S> and <Ancestor> have identical types,
        <S> and <Ancestor> orientations are DIFFERENT.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepDS_ShapeShapeInterference) -> None: ...

    def Config(self) -> TopOpeBRepDS_Config: ...

    def GBound(self) -> bool: ...

    def SetGBound(self, b: bool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_CurvePointInterference(TopOpeBRepDS_Interference):
    """An interference with a parameter."""

    @overload
    def __init__(self, T: TopOpeBRepDS_Transition, ST: TopOpeBRepDS_Kind, S: int, GT: TopOpeBRepDS_Kind, G: int, P: float) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_CurvePointInterference) -> None: ...

    @overload
    def Parameter(self) -> float: ...

    @overload
    def Parameter(self, P: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_EdgeVertexInterference(TopOpeBRepDS_ShapeShapeInterference):
    """An interference with a parameter (ShapeShapeInterference)."""

    @overload
    def __init__(self, T: TopOpeBRepDS_Transition, S: int, G: int, GIsBound: bool, C: TopOpeBRepDS_Config, P: float) -> None:
        """
        Create an interference of VERTEX <G> on crossed EDGE <S>.

        <T> is the transition along the edge, crossing the crossed edge.
        <S> is the crossed edge.
        <GIsBound> indicates if <G> is a bound of the edge.
        <C> indicates the geometric configuration between
        the edge and the crossed edge.
        <P> is the parameter of <G> on the edge.

        interference is stored in the list of interfs of the edge.
        """

    @overload
    def __init__(self, T: TopOpeBRepDS_Transition, ST: TopOpeBRepDS_Kind, S: int, G: int, GIsBound: bool, C: TopOpeBRepDS_Config, P: float) -> None:
        """
        Create an interference of VERTEX <G> on a crossed EDGE E.

        if support type <ST> == EDGE : <S> is edge E
        FACE : <S> is the face with bound E.
        <T> is the transition along the edge, crossing the crossed edge.
        E is the crossed edge.
        <GIsBound> indicates if <G> is a bound of the edge.
        <P> is the parameter of <G> on the edge.

        interference is stored in the list of interfs of the edge.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepDS_EdgeVertexInterference) -> None: ...

    @overload
    def Parameter(self) -> float: ...

    @overload
    def Parameter(self, P: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_FaceEdgeInterference(TopOpeBRepDS_ShapeShapeInterference):
    """ShapeShapeInterference"""

    @overload
    def __init__(self, T: TopOpeBRepDS_Transition, S: int, G: int, GIsBound: bool, C: TopOpeBRepDS_Config) -> None:
        """Create an interference of EDGE <G> on FACE <S>."""

    @overload
    def __init__(self, theOther: TopOpeBRepDS_FaceEdgeInterference) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_InterferenceIterator:
    """
    Iterate on interferences of a list, matching
    conditions on interferences.
    Nota:
    inheritance of ListIteratorOfListOfInterference from
    TopOpeBRepDS has not been done because of the
    impossibility of naming the classical More, Next
    methods which are declared as static in
    TCollection_ListIteratorOfList ... . ListIteratorOfList
    has benn placed as a field of InterferenceIterator.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """Creates an iterator on the Interference of list <L>."""

    @overload
    def __init__(self, theOther: TopOpeBRepDS_InterferenceIterator) -> None: ...

    def __iter__(self) -> TopOpeBRepDS_InterferenceIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> TopOpeBRepDS_Interference:
        """Python addition: see __iter__."""

    def Init(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """
        re-initialize interference iteration process on
        the list of interference <L>.
        Conditions are not modified.
        """

    def GeometryKind(self, GK: TopOpeBRepDS_Kind) -> None:
        """
        define a condition on interference iteration process.
        Interference must match the Geometry Kind <ST>
        """

    def Geometry(self, G: int) -> None:
        """
        define a condition on interference iteration process.
        Interference must match the Geometry <G>
        """

    def SupportKind(self, ST: TopOpeBRepDS_Kind) -> None:
        """
        define a condition on interference iteration process.
        Interference must match the Support Kind <ST>
        """

    def Support(self, S: int) -> None:
        """
        define a condition on interference iteration process.
        Interference must match the Support <S>
        """

    def Match(self) -> None:
        """
        reach for an interference matching the conditions
        (if defined).
        """

    def MatchInterference(self, I: TopOpeBRepDS_Interference | None) -> bool:
        """
        Returns True if the Interference <I> matches the
        conditions (if defined).
        If no conditions defined, returns True.
        """

    def More(self) -> bool:
        """
        Returns True if there is a current Interference in
        the iteration.
        """

    def Next(self) -> None:
        """Move to the next Interference."""

    def Value(self) -> TopOpeBRepDS_Interference:
        """
        Returns the current Interference, matching the
        conditions (if defined).
        """

    def ChangeIterator(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference].Iterator: ...

class TopOpeBRepDS_Surface:
    """A Geom surface and a tolerance."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Other: TopOpeBRepDS_Surface) -> None: ...

    @overload
    def __init__(self, P: nanoocp.Geom.Geom_Surface | None, T: float) -> None: ...

    def Assign(self, Other: TopOpeBRepDS_Surface) -> None: ...

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def Tolerance(self) -> float: ...

    @overload
    def Tolerance(self, theTol: float) -> None:
        """Update the tolerance"""

    def Keep(self) -> bool: ...

    def ChangeKeep(self, theToKeep: bool) -> None: ...

class TopOpeBRepDS_GeometryData:
    """mother-class of SurfaceData, CurveData, PointData"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Other: TopOpeBRepDS_GeometryData) -> None: ...

    def Assign(self, Other: TopOpeBRepDS_GeometryData) -> None: ...

    def Interferences(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangeInterferences(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def AddInterference(self, I: TopOpeBRepDS_Interference | None) -> None: ...

class TopOpeBRepDS_SurfaceData(TopOpeBRepDS_GeometryData):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: TopOpeBRepDS_Surface) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_SurfaceData) -> None: ...

class TopOpeBRepDS_Curve:
    """A Geom curve and a tolerance."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.Geom.Geom_Curve | None, T: float, IsWalk: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Curve) -> None: ...

    def DefineCurve(self, P: nanoocp.Geom.Geom_Curve | None, T: float, IsWalk: bool) -> None: ...

    @overload
    def Tolerance(self, tol: float) -> None:
        """Update the tolerance"""

    @overload
    def Tolerance(self) -> float: ...

    def SetSCI(self, I1: TopOpeBRepDS_Interference | None, I2: TopOpeBRepDS_Interference | None) -> None:
        """define the interferences face/curve."""

    def GetSCI1(self) -> TopOpeBRepDS_Interference:
        """
        Returns the first surface-curve interference.
        @return handle to the first interference
        """

    def GetSCI2(self) -> TopOpeBRepDS_Interference:
        """
        Returns the second surface-curve interference.
        @return handle to the second interference
        """

    def GetSCI(self) -> tuple[TopOpeBRepDS_Interference, TopOpeBRepDS_Interference]:
        """
        Deprecated in OCCT: Use GetSCI1() and GetSCI2() instead

        @deprecated Use GetSCI1() and GetSCI2() instead.
        """

    def SetShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GetShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Shape1(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ChangeShape1(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape2(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ChangeShape2(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Curve(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve(self, C3D: nanoocp.Geom.Geom_Curve | None, Tol: float) -> None: ...

    def SetRange(self, First: float, Last: float) -> None: ...

    def Range(self) -> tuple[bool, float, float]: ...

    def ChangeCurve(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve1(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def Curve1(self, PC1: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def Curve2(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def Curve2(self, PC2: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    def IsWalk(self) -> bool: ...

    def ChangeIsWalk(self, B: bool) -> None: ...

    def Keep(self) -> bool: ...

    def ChangeKeep(self, B: bool) -> None: ...

    def Mother(self) -> int: ...

    def ChangeMother(self, I: int) -> None: ...

    def DSIndex(self) -> int: ...

    def ChangeDSIndex(self, I: int) -> None: ...

class TopOpeBRepDS_CurveData(TopOpeBRepDS_GeometryData):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: TopOpeBRepDS_Curve) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_CurveData) -> None: ...

class TopOpeBRepDS_Point:
    """A Geom point and a tolerance."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, T: float) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Point) -> None: ...

    def IsEqual(self, other: TopOpeBRepDS_Point) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def ChangePoint(self) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def Tolerance(self) -> float: ...

    @overload
    def Tolerance(self, Tol: float) -> None: ...

    def Keep(self) -> bool: ...

    def ChangeKeep(self, B: bool) -> None: ...

class TopOpeBRepDS_PointData(TopOpeBRepDS_GeometryData):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: TopOpeBRepDS_Point) -> None: ...

    @overload
    def __init__(self, P: TopOpeBRepDS_Point, I1: int, I2: int) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_PointData) -> None: ...

    def SetShapes(self, I1: int, I2: int) -> None: ...

    def GetShapes(self) -> tuple[int, int]: ...

class TopOpeBRepDS_ShapeData:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_ShapeData) -> None: ...

    def Interferences(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangeInterferences(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def Keep(self) -> bool: ...

    def ChangeKeep(self, B: bool) -> None: ...

class TopOpeBRepDS_ShapeWithState:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_ShapeWithState) -> None: ...

    def Part(self, aState: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddPart(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aState: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def AddParts(self, aListOfShape: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], aState: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def SetState(self, aState: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def State(self) -> nanoocp.TopAbs.TopAbs_State: ...

    def SetIsSplitted(self, anIsSplitted: bool) -> None: ...

    def IsSplitted(self) -> bool: ...

class TopOpeBRepDS_DataStructure:
    """
    The DataStructure stores :

    New geometries : points, curves, and surfaces.
    Topological shapes : vertices, edges, faces.
    The new geometries and the topological shapes have interferences.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_DataStructure) -> None: ...

    def Init(self) -> None:
        """reset the data structure"""

    def AddSurface(self, S: TopOpeBRepDS_Surface) -> int:
        """Insert a new surface. Returns the index."""

    def RemoveSurface(self, I: int) -> None: ...

    @overload
    def KeepSurface(self, I: int) -> bool: ...

    @overload
    def KeepSurface(self, S: TopOpeBRepDS_Surface) -> bool: ...

    @overload
    def ChangeKeepSurface(self, I: int, FindKeep: bool) -> None: ...

    @overload
    def ChangeKeepSurface(self, S: TopOpeBRepDS_Surface, FindKeep: bool) -> None: ...

    def AddCurve(self, S: TopOpeBRepDS_Curve) -> int:
        """Insert a new curve. Returns the index."""

    def RemoveCurve(self, I: int) -> None: ...

    @overload
    def KeepCurve(self, I: int) -> bool: ...

    @overload
    def KeepCurve(self, C: TopOpeBRepDS_Curve) -> bool: ...

    @overload
    def ChangeKeepCurve(self, I: int, FindKeep: bool) -> None: ...

    @overload
    def ChangeKeepCurve(self, C: TopOpeBRepDS_Curve, FindKeep: bool) -> None: ...

    def AddPoint(self, PDS: TopOpeBRepDS_Point) -> int:
        """Insert a new point. Returns the index."""

    def AddPointSS(self, PDS: TopOpeBRepDS_Point, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """Insert a new point. Returns the index."""

    def RemovePoint(self, I: int) -> None: ...

    @overload
    def KeepPoint(self, I: int) -> bool: ...

    @overload
    def KeepPoint(self, P: TopOpeBRepDS_Point) -> bool: ...

    @overload
    def ChangeKeepPoint(self, I: int, FindKeep: bool) -> None: ...

    @overload
    def ChangeKeepPoint(self, P: TopOpeBRepDS_Point, FindKeep: bool) -> None: ...

    @overload
    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """Insert a shape S. Returns the index."""

    @overload
    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape, I: int) -> int:
        """Insert a shape S which ancestor is I = 1 or 2. Returns the index."""

    @overload
    def KeepShape(self, I: int, FindKeep: bool = True) -> bool: ...

    @overload
    def KeepShape(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> bool: ...

    @overload
    def ChangeKeepShape(self, I: int, FindKeep: bool) -> None: ...

    @overload
    def ChangeKeepShape(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool) -> None: ...

    def InitSectionEdges(self) -> None: ...

    def AddSectionEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> int: ...

    def SurfaceInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangeSurfaceInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def CurveInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangeCurveInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def PointInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangePointInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    @overload
    def ShapeInterferences(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    @overload
    def ShapeInterferences(self, I: int, FindKeep: bool = True) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    @overload
    def ChangeShapeInterferences(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    @overload
    def ChangeShapeInterferences(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    @overload
    def ShapeSameDomain(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def ShapeSameDomain(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def ChangeShapeSameDomain(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def ChangeShapeSameDomain(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ChangeShapes(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeData, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def AddShapeSameDomain(self, S: nanoocp.TopoDS.TopoDS_Shape, SSD: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def RemoveShapeSameDomain(self, S: nanoocp.TopoDS.TopoDS_Shape, SSD: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def SameDomainRef(self, I: int) -> int: ...

    @overload
    def SameDomainRef(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def SameDomainRef(self, I: int, Ref: int) -> None: ...

    @overload
    def SameDomainRef(self, S: nanoocp.TopoDS.TopoDS_Shape, Ref: int) -> None: ...

    @overload
    def SameDomainOri(self, I: int) -> TopOpeBRepDS_Config: ...

    @overload
    def SameDomainOri(self, S: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Config: ...

    @overload
    def SameDomainOri(self, I: int, Ori: TopOpeBRepDS_Config) -> None: ...

    @overload
    def SameDomainOri(self, S: nanoocp.TopoDS.TopoDS_Shape, Ori: TopOpeBRepDS_Config) -> None: ...

    @overload
    def SameDomainInd(self, I: int) -> int: ...

    @overload
    def SameDomainInd(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def SameDomainInd(self, I: int, Ind: int) -> None: ...

    @overload
    def SameDomainInd(self, S: nanoocp.TopoDS.TopoDS_Shape, Ind: int) -> None: ...

    @overload
    def AncestorRank(self, I: int) -> int: ...

    @overload
    def AncestorRank(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def AncestorRank(self, I: int, Ianc: int) -> None: ...

    @overload
    def AncestorRank(self, S: nanoocp.TopoDS.TopoDS_Shape, Ianc: int) -> None: ...

    def AddShapeInterference(self, S: nanoocp.TopoDS.TopoDS_Shape, I: TopOpeBRepDS_Interference | None) -> None: ...

    def RemoveShapeInterference(self, S: nanoocp.TopoDS.TopoDS_Shape, I: TopOpeBRepDS_Interference | None) -> None: ...

    @overload
    def FillShapesSameDomain(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, refFirst: bool = True) -> None: ...

    @overload
    def FillShapesSameDomain(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, c1: TopOpeBRepDS_Config, c2: TopOpeBRepDS_Config, refFirst: bool = True) -> None: ...

    def UnfillShapesSameDomain(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def NbSurfaces(self) -> int: ...

    def NbCurves(self) -> int: ...

    def ChangeNbCurves(self, N: int) -> None: ...

    def NbPoints(self) -> int: ...

    def NbShapes(self) -> int: ...

    def NbSectionEdges(self) -> int: ...

    def Surface(self, I: int) -> TopOpeBRepDS_Surface:
        """Returns the surface of index <I>."""

    def ChangeSurface(self, I: int) -> TopOpeBRepDS_Surface:
        """Returns the surface of index <I>."""

    def Curve(self, I: int) -> TopOpeBRepDS_Curve:
        """Returns the Curve of index <I>."""

    def ChangeCurve(self, I: int) -> TopOpeBRepDS_Curve:
        """Returns the Curve of index <I>."""

    def Point(self, I: int) -> TopOpeBRepDS_Point:
        """Returns the point of index <I>."""

    def ChangePoint(self, I: int) -> TopOpeBRepDS_Point:
        """Returns the point of index <I>."""

    @overload
    def Shape(self, I: int, FindKeep: bool = True) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns the shape of index I stored in
        the map myShapes, accessing a list of interference.
        """

    @overload
    def Shape(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> int:
        """
        returns the index of shape <S> stored in
        the map myShapes, accessing a list of interference.
        returns 0 if <S> is not in the map.
        """

    @overload
    def SectionEdge(self, I: int, FindKeep: bool = True) -> nanoocp.TopoDS.TopoDS_Edge: ...

    @overload
    def SectionEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, FindKeep: bool = True) -> int: ...

    def IsSectionEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, FindKeep: bool = True) -> bool: ...

    def HasGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns True if <S> has new geometries, i.e :
        True si :
        HasShape(S) True
        S a une liste d'interferences non vide.
        S = SOLID, FACE, EDGE : true/false
        S = SHELL, WIRE, VERTEX : false.
        """

    def HasShape(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> bool:
        """Returns True if <S> est dans myShapes"""

    def SetNewSurface(self, F: nanoocp.TopoDS.TopoDS_Shape, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    def HasNewSurface(self, F: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def Isfafa(self, isfafa: bool) -> None: ...

    @overload
    def Isfafa(self) -> bool: ...

    def ChangeMapOfShapeWithStateObj(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def ChangeMapOfShapeWithStateTool(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def ChangeMapOfShapeWithState(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> tuple[nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher], bool]: ...

    def GetShapeWithState(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeWithState: ...

    def ChangeMapOfRejectedShapesObj(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def ChangeMapOfRejectedShapesTool(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

class TopOpeBRepDS_HDataStructure(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_HDataStructure) -> None: ...

    @overload
    def AddAncestors(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def AddAncestors(self, S: nanoocp.TopoDS.TopoDS_Shape, T1: nanoocp.TopAbs.TopAbs_ShapeEnum, T2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        Update the data structure with shapes of type T1
        containing a subshape of type T2 which is stored
        in the DS.
        Used by the previous one.
        """

    def ChkIntg(self) -> None:
        """Check the integrity of the DS"""

    def DS(self) -> TopOpeBRepDS_DataStructure: ...

    def ChangeDS(self) -> TopOpeBRepDS_DataStructure: ...

    def NbSurfaces(self) -> int: ...

    def NbCurves(self) -> int: ...

    def NbPoints(self) -> int: ...

    def Surface(self, I: int) -> TopOpeBRepDS_Surface:
        """Returns the surface of index <I>."""

    def SurfaceCurves(self, I: int) -> TopOpeBRepDS_CurveIterator:
        """
        Returns an iterator on the curves on the surface
        <I>.
        """

    def Curve(self, I: int) -> TopOpeBRepDS_Curve:
        """Returns the Curve of index <I>."""

    def ChangeCurve(self, I: int) -> TopOpeBRepDS_Curve:
        """Returns the Curve of index <I>."""

    def CurvePoints(self, I: int) -> TopOpeBRepDS_PointIterator:
        """
        Returns an iterator on the points on the curve
        <I>.
        """

    def Point(self, I: int) -> TopOpeBRepDS_Point:
        """Returns the point of index <I>."""

    def NbShapes(self) -> int: ...

    @overload
    def Shape(self, I: int, FindKeep: bool = True) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the shape of index <I> in the DS"""

    @overload
    def Shape(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> int:
        """
        Returns the index of shape <S> in the DS
        returns 0 if <S> is not in the DS
        """

    def HasGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns True if <S> has new geometries."""

    def HasShape(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> bool:
        """
        Returns True if <S> has new geometries (SOLID,FACE,EDGE)
        or if <S> (SHELL,WIRE) has sub-shape (FACE,EDGE)
        with new geometries
        """

    def HasSameDomain(self, S: nanoocp.TopoDS.TopoDS_Shape, FindKeep: bool = True) -> bool:
        """
        Returns True if <S> share a geometrical domain with
        some other shapes.
        """

    def SameDomain(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape].Iterator:
        """
        Returns an iterator on the SameDomain shapes attached
        to the shape <S>.
        """

    def SameDomainOrientation(self, S: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Config:
        """
        Returns orientation of shape <S> compared with its
        reference shape
        """

    def SameDomainReference(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Returns orientation of shape <S> compared with its
        reference shape
        """

    @overload
    def SolidSurfaces(self, S: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_SurfaceIterator:
        """
        Returns an iterator on the surfaces attached to the
        solid <S>.
        """

    @overload
    def SolidSurfaces(self, I: int) -> TopOpeBRepDS_SurfaceIterator:
        """
        Returns an iterator on the surfaces attached to the
        solid <I>.
        """

    @overload
    def FaceCurves(self, F: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_CurveIterator:
        """
        Returns an iterator on the curves attached to the
        face <F>.
        """

    @overload
    def FaceCurves(self, I: int) -> TopOpeBRepDS_CurveIterator:
        """
        Returns an iterator on the curves attached to the
        face <I>.
        """

    def EdgePoints(self, E: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_PointIterator:
        """
        Returns an iterator on the points attached to the
        edge <E>.
        """

    def MakeCurve(self, C1: TopOpeBRepDS_Curve, C2: TopOpeBRepDS_Curve) -> int: ...

    def RemoveCurve(self, iC: int) -> None: ...

    def NbGeometry(self, K: TopOpeBRepDS_Kind) -> int: ...

    @overload
    def NbTopology(self, K: TopOpeBRepDS_Kind) -> int: ...

    @overload
    def NbTopology(self) -> int: ...

    def EdgesSameParameter(self) -> bool:
        """
        returns True if all the edges stored as shapes in the DS
        are SameParameter, otherwise False.
        """

    @overload
    def SortOnParameter(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    @overload
    def SortOnParameter(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def MinMaxOnParameter(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> tuple[float, float]: ...

    def ScanInterfList(self, IT: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference].Iterator, PDS: TopOpeBRepDS_Point) -> bool:
        """
        Search, among a list of interferences accessed by the iterator
        <IT>, a geometry <G> whose 3D point is identical to the 3D point
        of the TheDSPoint <PDS>.
        returns True if such an interference has been found, False else.
        if True, iterator It points (by the Value() method) on the first
        interference accessing an identical 3D point.
        """

    def GetGeometry(self, IT: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference].Iterator, PDS: TopOpeBRepDS_Point) -> tuple[bool, int, TopOpeBRepDS_Kind]:
        """
        Get the geometry of a DS point <PDS>.
        Search for it with ScanInterfList (previous method).
        if found, set <G,K> to the geometry,kind of the interference found.
        returns the value of ScanInterfList().
        """

    @overload
    def StoreInterference(self, I: TopOpeBRepDS_Interference | None, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Add interference <I> to list <LI>."""

    @overload
    def StoreInterference(self, I: TopOpeBRepDS_Interference | None, S: nanoocp.TopoDS.TopoDS_Shape, str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Add interference <I> to list of interference of shape <S>."""

    @overload
    def StoreInterference(self, I: TopOpeBRepDS_Interference | None, IS: int, str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Add interference <I> to list of interference of shape <IS>."""

    @overload
    def StoreInterferences(self, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], S: nanoocp.TopoDS.TopoDS_Shape, str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @overload
    def StoreInterferences(self, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], IS: int, str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @overload
    def ClearStoreInterferences(self, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], S: nanoocp.TopoDS.TopoDS_Shape, str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @overload
    def ClearStoreInterferences(self, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], IS: int, str: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_CurveExplorer:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, DS: TopOpeBRepDS_DataStructure, FindOnlyKeep: bool = True) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_CurveExplorer) -> None: ...

    def Init(self, DS: TopOpeBRepDS_DataStructure, FindOnlyKeep: bool = True) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    @overload
    def Curve(self) -> TopOpeBRepDS_Curve: ...

    @overload
    def Curve(self, I: int) -> TopOpeBRepDS_Curve: ...

    def IsCurve(self, I: int) -> bool: ...

    def IsCurveKeep(self, I: int) -> bool: ...

    def NbCurve(self) -> int: ...

    def Index(self) -> int: ...

class TopOpeBRepDS_CurveIterator(TopOpeBRepDS_InterferenceIterator):
    @overload
    def __init__(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """
        Creates an iterator on the curves on surface
        described by the interferences in <L>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepDS_CurveIterator) -> None: ...

    def MatchInterference(self, I: TopOpeBRepDS_Interference | None) -> bool:
        """
        Returns True if the Interference <I> has a
        GeometryType() TopOpeBRepDS_CURVE
        returns False else.
        """

    def Current(self) -> int:
        """Index of the curve in the data structure."""

    def Orientation(self, S: nanoocp.TopAbs.TopAbs_State) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def PCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

class TopOpeBRepDS_Dumper:
    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Dumper) -> None: ...

    @overload
    def SDumpRefOri(self, K: TopOpeBRepDS_Kind, I: int) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SDumpRefOri(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SPrintShape(self, I: int) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SPrintShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SPrintShapeRefOri(self, S: nanoocp.TopoDS.TopoDS_Shape, B: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SPrintShapeRefOri(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], B: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

class TopOpeBRepDS_Edge3dInterferenceTool:
    """
    a tool computing edge / face complex transition,
    Interferences of edge reference are given by
    I = (T on face, G = point or vertex, S = edge)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Edge3dInterferenceTool) -> None: ...

    def InitPointVertex(self, IsVertex: int, VonOO: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Init(self, Eref: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape, I: TopOpeBRepDS_Interference | None) -> None: ...

    def Add(self, Eref: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape, I: TopOpeBRepDS_Interference | None) -> None: ...

    def Transition(self, I: TopOpeBRepDS_Interference | None) -> None: ...

class TopOpeBRepDS_EdgeInterferenceTool:
    """a tool computing complex transition on Edge."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_EdgeInterferenceTool) -> None: ...

    def Init(self, E: nanoocp.TopoDS.TopoDS_Shape, I: TopOpeBRepDS_Interference | None) -> None: ...

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape, I: TopOpeBRepDS_Interference | None) -> None: ...

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Shape, P: TopOpeBRepDS_Point, I: TopOpeBRepDS_Interference | None) -> None: ...

    def Transition(self, I: TopOpeBRepDS_Interference | None) -> None: ...

class TopOpeBRepDS_EIR:
    """EdgeInterferenceReducer"""

    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_EIR) -> None: ...

    @overload
    def ProcessEdgeInterferences(self) -> None: ...

    @overload
    def ProcessEdgeInterferences(self, I: int) -> None: ...

class TopOpeBRepDS_Explorer:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None, T: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE, findkeep: bool = True) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Explorer) -> None: ...

    def __iter__(self) -> TopOpeBRepDS_Explorer:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Python addition: see __iter__."""

    def Init(self, HDS: TopOpeBRepDS_HDataStructure | None, T: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE, findkeep: bool = True) -> None: ...

    def Type(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Index(self) -> int: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

class TopOpeBRepDS_ListOfShapeOn1State:
    """represent a list of shape"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_ListOfShapeOn1State) -> None: ...

    def ListOnState(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ChangeListOnState(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def IsSplit(self) -> bool: ...

    def Split(self, B: bool = True) -> None: ...

    def Clear(self) -> None: ...

class TopOpeBRepDS_FaceInterferenceTool:
    """a tool computing complex transition on Face."""

    def __init__(self, theOther: TopOpeBRepDS_FaceInterferenceTool) -> None: ...

    def Init(self, FI: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, Eisnew: bool, I: TopOpeBRepDS_Interference | None) -> None:
        """
        Eisnew = true if E is a new edge built on edge I->Geometry()
        false if E is shape <=> I->Geometry()
        """

    @overload
    def Add(self, FI: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, Eisnew: bool, I: TopOpeBRepDS_Interference | None) -> None:
        """
        Eisnew = true if E is a new edge built on edge I->Geometry()
        false if E is shape <=> I->Geometry()
        """

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Shape, C: TopOpeBRepDS_Curve, I: TopOpeBRepDS_Interference | None) -> None: ...

    def SetEdgePntPar(self, P: nanoocp.gp.gp_Pnt, par: float) -> None: ...

    def GetEdgePntPar(self, P: nanoocp.gp.gp_Pnt) -> float: ...

    def IsEdgePntParDef(self) -> bool: ...

    def Transition(self, I: TopOpeBRepDS_Interference | None) -> None: ...

class TopOpeBRepDS_Filter:
    def __init__(self, theOther: TopOpeBRepDS_Filter) -> None: ...

    def ProcessInterferences(self) -> None: ...

    @overload
    def ProcessFaceInterferences(self, MEsp: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @overload
    def ProcessFaceInterferences(self, I: int, MEsp: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @overload
    def ProcessEdgeInterferences(self) -> None: ...

    @overload
    def ProcessEdgeInterferences(self, I: int) -> None: ...

    @overload
    def ProcessCurveInterferences(self) -> None: ...

    @overload
    def ProcessCurveInterferences(self, I: int) -> None: ...

class TopOpeBRepDS_FIR:
    """FaceInterferenceReducer"""

    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_FIR) -> None: ...

    @overload
    def ProcessFaceInterferences(self, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @overload
    def ProcessFaceInterferences(self, I: int, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

class TopOpeBRepDS_GapFiller:
    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_GapFiller) -> None: ...

    def Perform(self) -> None: ...

    def FindAssociatedPoints(self, I: TopOpeBRepDS_Interference | None, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """
        Recherche parmi l'ensemble des points d'Interference
        la Liste <LI> des points qui correspondent au point d'indice <Index>
        """

    def CheckConnexity(self, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> bool:
        """
        Enchaine les sections via les points d'Interferences deja
        associe; Renvoit dans <L> les points extremites des Lignes.
        Methodes pour construire la liste des Points qui
        peuvent correspondre a une Point donne.
        """

    def AddPointsOnShape(self, S: nanoocp.TopoDS.TopoDS_Shape, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def AddPointsOnConnexShape(self, F: nanoocp.TopoDS.TopoDS_Shape, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """
        Methodes pour reduire la liste des Points qui
        peuvent correspondre a une Point donne.
        """

    def FilterByFace(self, F: nanoocp.TopoDS.TopoDS_Face, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def FilterByEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def FilterByIncidentDistance(self, F: nanoocp.TopoDS.TopoDS_Face, I: TopOpeBRepDS_Interference | None, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def IsOnFace(self, I: TopOpeBRepDS_Interference | None, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Return TRUE si I a ete obtenu par une intersection
        avec <F>.
        """

    def IsOnEdge(self, I: TopOpeBRepDS_Interference | None, E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Return TRUE si I ou une de ses representaions a
        pour support <E>.
        Methodes de reconstructions des geometries des point
        et des courbes de section
        """

    def BuildNewGeometries(self) -> None: ...

    def ReBuildGeom(self, I1: TopOpeBRepDS_Interference | None, Done: nanoocp.NCollection.NCollection_Map[int]) -> None: ...

class TopOpeBRepDS_GapTool(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_GapTool) -> None: ...

    def Init(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    def Interferences(self, IndexPoint: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def SameInterferences(self, I: TopOpeBRepDS_Interference | None) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangeSameInterferences(self, I: TopOpeBRepDS_Interference | None) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def Curve(self, I: TopOpeBRepDS_Interference | None, C: TopOpeBRepDS_Curve) -> bool: ...

    def EdgeSupport(self, I: TopOpeBRepDS_Interference | None, E: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def FacesSupport(self, I: TopOpeBRepDS_Interference | None, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Return les faces qui ont genere la section origine
        de I
        """

    def ParameterOnEdge(self, I: TopOpeBRepDS_Interference | None, E: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, float]: ...

    def SetPoint(self, I: TopOpeBRepDS_Interference | None, IndexPoint: int) -> None: ...

    def SetParameterOnEdge(self, I: TopOpeBRepDS_Interference | None, E: nanoocp.TopoDS.TopoDS_Shape, U: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_InterferenceTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_InterferenceTool) -> None: ...

    @staticmethod
    def MakeEdgeInterference(T: TopOpeBRepDS_Transition, SK: TopOpeBRepDS_Kind, SI: int, GK: TopOpeBRepDS_Kind, GI: int, P: float) -> TopOpeBRepDS_Interference: ...

    @staticmethod
    def MakeCurveInterference(T: TopOpeBRepDS_Transition, SK: TopOpeBRepDS_Kind, SI: int, GK: TopOpeBRepDS_Kind, GI: int, P: float) -> TopOpeBRepDS_Interference: ...

    @staticmethod
    def DuplicateCurvePointInterference(I: TopOpeBRepDS_Interference | None) -> TopOpeBRepDS_Interference:
        """duplicate I in a new interference with Complement() transition."""

    @staticmethod
    def MakeFaceCurveInterference(Transition: TopOpeBRepDS_Transition, FaceI: int, CurveI: int, PC: nanoocp.Geom2d.Geom2d_Curve | None) -> TopOpeBRepDS_Interference: ...

    @staticmethod
    def MakeSolidSurfaceInterference(Transition: TopOpeBRepDS_Transition, SolidI: int, SurfaceI: int) -> TopOpeBRepDS_Interference: ...

    @staticmethod
    def MakeEdgeVertexInterference(Transition: TopOpeBRepDS_Transition, EdgeI: int, VertexI: int, VertexIsBound: bool, Config: TopOpeBRepDS_Config, param: float) -> TopOpeBRepDS_Interference: ...

    @staticmethod
    def MakeFaceEdgeInterference(Transition: TopOpeBRepDS_Transition, FaceI: int, EdgeI: int, EdgeIsBound: bool, Config: TopOpeBRepDS_Config) -> TopOpeBRepDS_Interference: ...

    @overload
    @staticmethod
    def Parameter(CPI: TopOpeBRepDS_Interference | None) -> float: ...

    @overload
    @staticmethod
    def Parameter(CPI: TopOpeBRepDS_Interference | None, Par: float) -> None: ...

class TopOpeBRepDS_Marker(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Marker) -> None: ...

    def Reset(self) -> None: ...

    def Set(self, i: int, b: bool) -> None: ...

    def GetI(self, i: int) -> bool: ...

    def Allocate(self, n: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_PointExplorer:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, DS: TopOpeBRepDS_DataStructure, FindOnlyKeep: bool = True) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_PointExplorer) -> None: ...

    def Init(self, DS: TopOpeBRepDS_DataStructure, FindOnlyKeep: bool = True) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    @overload
    def Point(self) -> TopOpeBRepDS_Point: ...

    @overload
    def Point(self, I: int) -> TopOpeBRepDS_Point: ...

    def IsPoint(self, I: int) -> bool: ...

    def IsPointKeep(self, I: int) -> bool: ...

    def NbPoint(self) -> int: ...

    def Index(self) -> int: ...

class TopOpeBRepDS_PointIterator(TopOpeBRepDS_InterferenceIterator):
    @overload
    def __init__(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """
        Creates an iterator on the points on curves
        described by the interferences in <L>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepDS_PointIterator) -> None: ...

    def MatchInterference(self, I: TopOpeBRepDS_Interference | None) -> bool:
        """
        Returns True if the Interference <I> has a
        GeometryType() TopOpeBRepDS_POINT or TopOpeBRepDS_VERTEX
        returns False else.
        """

    def Current(self) -> int:
        """Index of the point in the data structure."""

    def Orientation(self, S: nanoocp.TopAbs.TopAbs_State) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def Parameter(self) -> float: ...

    def IsVertex(self) -> bool: ...

    def IsPoint(self) -> bool: ...

    def DiffOriented(self) -> bool: ...

    def SameOriented(self) -> bool: ...

    def Support(self) -> int: ...

class TopOpeBRepDS_Reducer:
    """
    reduce interferences of a data structure (HDS)
    used in topological operations.
    """

    @overload
    def __init__(self, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_Reducer) -> None: ...

    def ProcessFaceInterferences(self, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def ProcessEdgeInterferences(self) -> None: ...

class TopOpeBRepDS_SolidSurfaceInterference(TopOpeBRepDS_Interference):
    """Interference"""

    @overload
    def __init__(self, Transition: TopOpeBRepDS_Transition, SupportType: TopOpeBRepDS_Kind, Support: int, GeometryType: TopOpeBRepDS_Kind, Geometry: int) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_SolidSurfaceInterference) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_SurfaceCurveInterference(TopOpeBRepDS_Interference):
    """an interference with a 2d curve"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, I: TopOpeBRepDS_Interference | None) -> None: ...

    @overload
    def __init__(self, Transition: TopOpeBRepDS_Transition, SupportType: TopOpeBRepDS_Kind, Support: int, GeometryType: TopOpeBRepDS_Kind, Geometry: int, PC: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_SurfaceCurveInterference) -> None: ...

    @overload
    def PCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve(self, PC: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepDS_SurfaceExplorer:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, DS: TopOpeBRepDS_DataStructure, FindOnlyKeep: bool = True) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_SurfaceExplorer) -> None: ...

    def Init(self, DS: TopOpeBRepDS_DataStructure, FindOnlyKeep: bool = True) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    @overload
    def Surface(self) -> TopOpeBRepDS_Surface: ...

    @overload
    def Surface(self, I: int) -> TopOpeBRepDS_Surface: ...

    def IsSurface(self, I: int) -> bool: ...

    def IsSurfaceKeep(self, I: int) -> bool: ...

    def NbSurface(self) -> int: ...

    def Index(self) -> int: ...

class TopOpeBRepDS_SurfaceIterator(TopOpeBRepDS_InterferenceIterator):
    @overload
    def __init__(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None:
        """
        Creates an iterator on the Surfaces on solid
        described by the interferences in <L>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepDS_SurfaceIterator) -> None: ...

    def Current(self) -> int:
        """Index of the surface in the data structure."""

    def Orientation(self, S: nanoocp.TopAbs.TopAbs_State) -> nanoocp.TopAbs.TopAbs_Orientation: ...

class TopOpeBRepDS_TKI:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_TKI) -> None: ...

    def Clear(self) -> None: ...

    def FillOnGeometry(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def FillOnSupport(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

    def IsBound(self, K: TopOpeBRepDS_Kind, G: int) -> bool: ...

    def Interferences(self, K: TopOpeBRepDS_Kind, G: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def ChangeInterferences(self, K: TopOpeBRepDS_Kind, G: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]: ...

    def HasInterferences(self, K: TopOpeBRepDS_Kind, G: int) -> bool: ...

    @overload
    def Add(self, K: TopOpeBRepDS_Kind, G: int) -> None: ...

    @overload
    def Add(self, K: TopOpeBRepDS_Kind, G: int, HI: TopOpeBRepDS_Interference | None) -> None: ...

    def DumpTKIIterator(self, s1: nanoocp.TCollection.TCollection_AsciiString = ..., s2: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Value(self) -> tuple[nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], TopOpeBRepDS_Kind, int]: ...

    def ChangeValue(self) -> tuple[nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], TopOpeBRepDS_Kind, int]: ...

class TopOpeBRepDS_TOOL:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepDS_TOOL) -> None: ...

    @staticmethod
    def EShareG(HDS: TopOpeBRepDS_HDataStructure | None, E: nanoocp.TopoDS.TopoDS_Edge, lEsd: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @staticmethod
    def ShareG(HDS: TopOpeBRepDS_HDataStructure | None, is1: int, is2: int) -> bool: ...

    @staticmethod
    def GetEsd(HDS: TopOpeBRepDS_HDataStructure | None, S: nanoocp.TopoDS.TopoDS_Shape, ie: int) -> tuple[bool, int]: ...

    @staticmethod
    def ShareSplitON(HDS: TopOpeBRepDS_HDataStructure | None, MspON: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher], i1: int, i2: int, spON: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def GetConfig(HDS: TopOpeBRepDS_HDataStructure | None, MEspON: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher], ie: int, iesd: int) -> tuple[bool, int]: ...

def FDSCNX_EdgeConnexityShapeIndex(E: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None, SI: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

def FDSCNX_EdgeConnexitySameShape(E: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

def FDSCNX_Prepare(S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FDSCNX_HasConnexFace(S: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None) -> bool: ...

def FDSCNX_FaceEdgeConnexFaces(F: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

@overload
def FDSCNX_Dump(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

@overload
def FDSCNX_Dump(HDS: TopOpeBRepDS_HDataStructure | None, I: int) -> None: ...

def FDSCNX_DumpIndex(HDS: TopOpeBRepDS_HDataStructure | None, I: int) -> None: ...

def FUN_ds_redu2d1d(BDS: TopOpeBRepDS_DataStructure, ISE: int, I2d: TopOpeBRepDS_Interference | None, l1d: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], newT2d: TopOpeBRepDS_Transition) -> bool: ...

def FUN_ds_GetTr(BDS: TopOpeBRepDS_DataStructure, ISE: int, G: int, LIG: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, int, int, nanoocp.TopAbs.TopAbs_State, int, int]: ...

def FDS_SetT(T: TopOpeBRepDS_Transition, T0: TopOpeBRepDS_Transition) -> None: ...

def FDS_hasUNK(T: TopOpeBRepDS_Transition) -> bool: ...

@overload
def FDS_copy(LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], LII: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

@overload
def FDS_copy(LI: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LII: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

@overload
def FDS_assign(LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], LII: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

@overload
def FDS_assign(LI: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LII: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

def FUN_ds_samRk(BDS: TopOpeBRepDS_DataStructure, Rk: int, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LIsrk: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

@overload
def FDS_data(I: TopOpeBRepDS_Interference | None) -> tuple[TopOpeBRepDS_Kind, int, TopOpeBRepDS_Kind, int]: ...

@overload
def FDS_data(it: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference].Iterator) -> tuple[bool, TopOpeBRepDS_Interference, TopOpeBRepDS_Kind, int, TopOpeBRepDS_Kind, int]: ...

def FDS_Tdata(I: TopOpeBRepDS_Interference | None) -> tuple[nanoocp.TopAbs.TopAbs_ShapeEnum, int, nanoocp.TopAbs.TopAbs_ShapeEnum, int]: ...

def FDS_Idata(I: TopOpeBRepDS_Interference | None) -> tuple[nanoocp.TopAbs.TopAbs_ShapeEnum, int, nanoocp.TopAbs.TopAbs_ShapeEnum, int, TopOpeBRepDS_Kind, int, TopOpeBRepDS_Kind, int]: ...

def FUN_ds_getVsdm(BDS: TopOpeBRepDS_DataStructure, iV: int) -> tuple[bool, int]: ...

def FUN_ds_sdm(BDS: TopOpeBRepDS_DataStructure, s1: nanoocp.TopoDS.TopoDS_Shape, s2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

@overload
def FDS_aresamdom(BDS: TopOpeBRepDS_DataStructure, ES: nanoocp.TopoDS.TopoDS_Shape, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

@overload
def FDS_aresamdom(BDS: TopOpeBRepDS_DataStructure, SI: int, isb1: int, isb2: int) -> bool: ...

def FDS_EdgeIsConnexToSameDomainFaces(E: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None) -> bool: ...

def FDS_SIisGIofIofSBAofTofI(BDS: TopOpeBRepDS_DataStructure, SI: int, I: TopOpeBRepDS_Interference | None) -> bool: ...

def FDS_Parameter(I: TopOpeBRepDS_Interference | None) -> float: ...

def FDS_Parameter__float(I: TopOpeBRepDS_Interference | None) -> tuple[bool, float]:
    """
    FDS_Parameter__float: the C++ overload FDS_Parameter(const occ::handle<TopOpeBRepDS_Interference> &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def FDS_HasSameDomain3d(BDS: TopOpeBRepDS_DataStructure, E: nanoocp.TopoDS.TopoDS_Shape, PLSD: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape] = None) -> bool: ...

def FDS_Config3d(E1: nanoocp.TopoDS.TopoDS_Shape, E2: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, TopOpeBRepDS_Config]: ...

def FDS_HasSameDomain2d(BDS: TopOpeBRepDS_DataStructure, E: nanoocp.TopoDS.TopoDS_Shape, PLSD: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape] = None) -> bool: ...

def FDS_getupperlower(HDS: TopOpeBRepDS_HDataStructure | None, edgeIndex: int, paredge: float) -> tuple[float, float]: ...

@overload
def FUN_ds_getoov(v: nanoocp.TopoDS.TopoDS_Shape, BDS: TopOpeBRepDS_DataStructure, oov: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

@overload
def FUN_ds_getoov(v: nanoocp.TopoDS.TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure | None, oov: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_selectTRAINTinterference(li: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], liINTERNAL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> bool: ...

def FUN_ds_completeforSE1(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE2(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE3(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE4(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE5(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE6(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforE7(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE8(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_PURGEforE9(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_completeforSE9(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_complete1dForSESDM(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_redusamsha(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_shareG(HDS: TopOpeBRepDS_HDataStructure | None, iF1: int, iF2: int, iE2: int, Esp: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, bool]: ...

def FUN_ds_mkTonFsdm(HDS: TopOpeBRepDS_HDataStructure | None, iF1: int, iF2: int, iE2: int, iEG: int, paronEG: float, Esp: nanoocp.TopoDS.TopoDS_Edge, pardef: bool, T: TopOpeBRepDS_Transition) -> bool: ...

def FUN_ds_oriEinF(BDS: TopOpeBRepDS_DataStructure, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Shape) -> tuple[int, nanoocp.TopAbs.TopAbs_Orientation]: ...

def FUN_ds_FillSDMFaces(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_addSEsdm1d(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_hasI2d(EIX: int, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], LI2d: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_ds_PointToVertex(HDS: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FUN_ds_ONesd(BDS: TopOpeBRepDS_DataStructure, IE: int, EspON: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, int]: ...

def FDS_stateEwithF2d(BDS: TopOpeBRepDS_DataStructure, E: nanoocp.TopoDS.TopoDS_Edge, pE: float, KDS: TopOpeBRepDS_Kind, GDS: int, F1: nanoocp.TopoDS.TopoDS_Face, TrmemeS: TopOpeBRepDS_Transition) -> bool: ...

def FDS_parbefaft(BDS: TopOpeBRepDS_DataStructure, E: nanoocp.TopoDS.TopoDS_Edge, pE: float, pbef: float, paft: float, isonboundper: bool) -> tuple[bool, float, float]: ...

def FDS_LOIinfsup(BDS: TopOpeBRepDS_DataStructure, E: nanoocp.TopoDS.TopoDS_Edge, pE: float, KDS: TopOpeBRepDS_Kind, GDS: int, LOI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> tuple[bool, float, float, bool]: ...

def FUN_ds_FEIGb1TO0(MEspON: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> TopOpeBRepDS_HDataStructure: ...

def MakeCPVInterference(T: TopOpeBRepDS_Transition, S: int, G: int, P: float, GK: TopOpeBRepDS_Kind) -> TopOpeBRepDS_Interference: ...

@overload
def MakeEPVInterference(T: TopOpeBRepDS_Transition, S: int, G: int, P: float, GK: TopOpeBRepDS_Kind, B: bool) -> TopOpeBRepDS_Interference: ...

@overload
def MakeEPVInterference(T: TopOpeBRepDS_Transition, S: int, G: int, P: float, GK: TopOpeBRepDS_Kind, SK: TopOpeBRepDS_Kind, B: bool) -> TopOpeBRepDS_Interference: ...

def FUN_hasStateShape(T: TopOpeBRepDS_Transition, state: nanoocp.TopAbs.TopAbs_State, shape: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

def FUN_selectTRASHAinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], sha: nanoocp.TopAbs.TopAbs_ShapeEnum, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectITRASHAinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], Index: int, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectTRAUNKinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectTRAORIinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], O: nanoocp.TopAbs.TopAbs_Orientation, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectGKinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], GK: TopOpeBRepDS_Kind, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectSKinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], SK: TopOpeBRepDS_Kind, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectGIinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], GI: int, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectSIinterference(L1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], SI: int, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_interfhassupport(DS: TopOpeBRepDS_DataStructure, I: TopOpeBRepDS_Interference | None, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_transitionEQUAL(arg0: TopOpeBRepDS_Transition, arg1: TopOpeBRepDS_Transition) -> bool: ...

def FUN_transitionSTATEEQUAL(arg0: TopOpeBRepDS_Transition, arg1: TopOpeBRepDS_Transition) -> bool: ...

def FUN_transitionSHAPEEQUAL(arg0: TopOpeBRepDS_Transition, arg1: TopOpeBRepDS_Transition) -> bool: ...

def FUN_transitionINDEXEQUAL(arg0: TopOpeBRepDS_Transition, arg1: TopOpeBRepDS_Transition) -> bool: ...

def FUN_reducedoublons(LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], BDS: TopOpeBRepDS_DataStructure, SIX: int) -> None: ...

def FUN_unkeepUNKNOWN(LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], BDS: TopOpeBRepDS_DataStructure, SIX: int) -> None: ...

def FUN_select2dI(SIX: int, BDS: TopOpeBRepDS_DataStructure, TRASHAk: nanoocp.TopAbs.TopAbs_ShapeEnum, lI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l2dI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_selectpure2dI(lF: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], lFE: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l2dFE: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_select1dI(SIX: int, BDS: TopOpeBRepDS_DataStructure, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l1dI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> int: ...

def FUN_select3dinterference(SIX: int, BDS: TopOpeBRepDS_DataStructure, lF: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l3dF: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], lFE: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], lFEresi: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l3dFE: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l3dFEresi: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], l2dFE: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

def FDS_repvg(BDS: TopOpeBRepDS_DataStructure, EIX: int, GT: TopOpeBRepDS_Kind, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], reducedLI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

def FDS_repvg2(BDS: TopOpeBRepDS_DataStructure, EIX: int, GT: TopOpeBRepDS_Kind, LI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference], reducedLI: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]) -> None: ...

def FDSSDM_prepare(arg0: TopOpeBRepDS_HDataStructure | None) -> None: ...

def FDSSDM_makes1s2(S: nanoocp.TopoDS.TopoDS_Shape, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

def FDSSDM_s1s2(S: nanoocp.TopoDS.TopoDS_Shape, LS1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LS2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

def FDSSDM_sordor(S: nanoocp.TopoDS.TopoDS_Shape, LSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LDO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

def FDSSDM_contains(S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

@overload
def FDSSDM_copylist(Lin: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], I1: int, I2: int, Lou: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

@overload
def FDSSDM_copylist(Lin: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Lou: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopOpeBRepDS
import nanoocp.TopTools
TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference = nanoocp.NCollection.NCollection_Array1[int]
TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopOpeBRepDS_DataMapOfShapeState = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopAbs.TopAbs_State, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopOpeBRepDS_HArray1OfDataMapOfIntegerListOfInterference = nanoocp.NCollection.NCollection_HArray1[int]
TopOpeBRepDS_IndexedDataMapOfShapeWithState = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopOpeBRepDS_ListOfInterference = nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference]
TopOpeBRepDS_MapOfShapeData = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeData, nanoocp.TopTools.TopTools_ShapeMapHasher]
