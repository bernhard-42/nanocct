"""OCCT package TopOpeBRepTool (toolkit TKBool)"""

import enum
from typing import overload

import nanoocp.BRepAdaptor
import nanoocp.Bnd
import nanoocp.Extrema
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomAdaptor
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopExp
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class TopOpeBRepTool_OutCurveType(enum.IntEnum):
    TopOpeBRepTool_BSPLINE1 = 0

    TopOpeBRepTool_APPROX = 1

    TopOpeBRepTool_INTERPOL = 2

TopOpeBRepTool_BSPLINE1: TopOpeBRepTool_OutCurveType = ...

TopOpeBRepTool_APPROX: TopOpeBRepTool_OutCurveType = TopOpeBRepTool_OutCurveType.TopOpeBRepTool_APPROX

TopOpeBRepTool_INTERPOL: TopOpeBRepTool_OutCurveType = ...

class TopOpeBRepTool:
    """
    This package provides services used by the TopOpeBRep
    package performing topological operations on the BRep
    data structure.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool) -> None: ...

    @overload
    @staticmethod
    def PurgeClosingEdges(F: nanoocp.TopoDS.TopoDS_Face, FF: nanoocp.TopoDS.TopoDS_Face, MWisOld: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int, nanoocp.TopTools.TopTools_ShapeMapHasher], MshNOK: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Fuse edges (in a wire) of a shape where we have
        useless vertex.
        In case face <FF> is built on UV-non-connexed wires
        (with the two closing edges FORWARD and REVERSED, in
        spite of one only), we find out the faulty edge, add
        the faulty shapes (edge,wire,face) to <MshNOK>.
        <FF> is a face descendant of <F>.
        <MWisOld>(wire) = 1 if wire is wire of <F>
        0 wire results from <F>'s wire split.
        returns false if purge fails
        """

    @overload
    @staticmethod
    def PurgeClosingEdges(F: nanoocp.TopoDS.TopoDS_Face, LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], MWisOld: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int, nanoocp.TopTools.TopTools_ShapeMapHasher], MshNOK: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    @staticmethod
    def CorrectONUVISO(F: nanoocp.TopoDS.TopoDS_Face, Fsp: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @staticmethod
    def MakeFaces(F: nanoocp.TopoDS.TopoDS_Face, LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], MshNOK: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape], LOFF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Builds up the correct list of faces <LOFF> from <LOF>, using
        faulty shapes from map <MshNOK>.
        <LOF> is the list of <F>'s descendant faces.
        returns false if building fails
        """

    @staticmethod
    def Regularize(aFace: nanoocp.TopoDS.TopoDS_Face, aListOfFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], ESplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Returns <False> if the face is valid (the UV
        representation of the face is a set of pcurves
        connexed by points with connexity 2).
        Else, splits <aFace> in order to return a list of valid
        faces.
        """

    @staticmethod
    def RegularizeWires(aFace: nanoocp.TopoDS.TopoDS_Face, OldWiresNewWires: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], ESplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Returns <False> if the face is valid (the UV
        representation of the face is a set of pcurves
        connexed by points with connexity 2).
        Else, splits wires of the face, these are boundaries of the
        new faces to build up; <OldWiresNewWires> describes (wire,
        splits of wire); <ESplits> describes (edge, edge's splits)
        """

    @staticmethod
    def RegularizeFace(aFace: nanoocp.TopoDS.TopoDS_Face, OldWiresnewWires: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], aListOfFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Classify wire's splits of map <OldWiresnewWires> in order to
        compute <aListOfFaces>, the splits of <aFace>.
        """

    @staticmethod
    def RegularizeShells(aSolid: nanoocp.TopoDS.TopoDS_Solid, OldSheNewShe: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], FSplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Returns <False> if the shell is valid (the solid is a set
        of faces connexed by edges with connexity 2).
        Else, splits faces of the shell; <OldFacesnewFaces> describes
        (face, splits of face).
        """

    @staticmethod
    def Print(OCT: TopOpeBRepTool_OutCurveType) -> object:
        """Prints <OCT> as string on stream <S>; returns <S>."""

class TopOpeBRepTool_AncestorsTool:
    """
    Describes the ancestors tool needed by
    the class DSFiller from TopOpeInter.

    This class has been created because it is not possible
    to instantiate the argument TheAncestorsTool (of
    DSFiller from TopOpeInter) with a package (TopExp)
    giving services as package methods.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_AncestorsTool) -> None: ...

    @staticmethod
    def MakeAncestors(S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum, M: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """same as package method TopExp::MapShapeListOfShapes()"""

class TopOpeBRepTool_HBoxTool(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_HBoxTool) -> None: ...

    def Clear(self) -> None: ...

    def AddBoxes(self, S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    def AddBox(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def ComputeBox(S: nanoocp.TopoDS.TopoDS_Shape, B: nanoocp.Bnd.Bnd_Box) -> None: ...

    @staticmethod
    def ComputeBoxOnVertices(S: nanoocp.TopoDS.TopoDS_Shape, B: nanoocp.Bnd.Bnd_Box) -> None: ...

    @staticmethod
    def DumpB(B: nanoocp.Bnd.Bnd_Box) -> None: ...

    @overload
    def Box(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Bnd.Bnd_Box: ...

    @overload
    def Box(self, I: int) -> nanoocp.Bnd.Bnd_Box: ...

    def HasBox(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def Shape(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Index(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def Extent(self) -> int: ...

    def ChangeIMS(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Bnd.Bnd_Box]: ...

    def IMS(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Bnd.Bnd_Box]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepTool_BoxSort:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, T: TopOpeBRepTool_HBoxTool | None) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_BoxSort) -> None: ...

    def SetHBoxTool(self, T: TopOpeBRepTool_HBoxTool | None) -> None: ...

    def HBoxTool(self) -> TopOpeBRepTool_HBoxTool: ...

    def Clear(self) -> None: ...

    def AddBoxes(self, S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    def MakeHAB(self, S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    def HAB(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]: ...

    @staticmethod
    def MakeHABCOB(HAB: nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box] | None, COB: nanoocp.Bnd.Bnd_Box) -> None: ...

    def HABShape(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def MakeCOB(self, S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    def AddBoxesMakeCOB(self, S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    def Compare(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List__int.Iterator: ...

    def TouchedShape(self, I: nanoocp.NCollection.NCollection_List__int.Iterator) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Box(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Bnd.Bnd_Box: ...

class TopOpeBRepTool_C2DF:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, PC: nanoocp.Geom2d.Geom2d_Curve | None, f2d: float, l2d: float, tol: float, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_C2DF) -> None: ...

    def SetPC(self, PC: nanoocp.Geom2d.Geom2d_Curve | None, f2d: float, l2d: float, tol: float) -> None: ...

    def SetFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def PC(self) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def IsPC(self, PC: nanoocp.Geom2d.Geom2d_Curve | None) -> bool: ...

    def IsFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

class TopOpeBRepTool_face:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_face) -> None: ...

    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire, Fref: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    def W(self) -> nanoocp.TopoDS.TopoDS_Wire: ...

    def IsDone(self) -> bool: ...

    def Finite(self) -> bool: ...

    def Ffinite(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def RealF(self) -> nanoocp.TopoDS.TopoDS_Face: ...

class TopOpeBRepTool_CLASSI:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_CLASSI) -> None: ...

    def Init2d(self, Fref: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def HasInit2d(self) -> bool: ...

    def Add2d(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def GetBox2d(self, S: nanoocp.TopoDS.TopoDS_Shape, Box2d: nanoocp.Bnd.Bnd_Box2d) -> bool: ...

    def ClassiBnd2d(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, tol: float, checklarge: bool) -> int: ...

    def Classip2d(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, stabnd2d12: int) -> int: ...

    def Getface(self, S: nanoocp.TopoDS.TopoDS_Shape, fa: TopOpeBRepTool_face) -> bool: ...

    def Classilist(self, lS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], mapgreasma: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool: ...

class TopOpeBRepTool_connexity:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Key: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_connexity) -> None: ...

    def SetKey(self, Key: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Key(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Item(self, OriKey: int, Item: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    def AllItems(self, Item: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @overload
    def AddItem(self, OriKey: int, Item: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def AddItem(self, OriKey: int, Item: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def RemoveItem(self, OriKey: int, Item: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @overload
    def RemoveItem(self, Item: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def ChangeItem(self, OriKey: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def IsMultiple(self) -> bool: ...

    def IsFaulty(self) -> bool: ...

    def IsInternal(self, Item: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

class TopOpeBRepTool_CORRISO:
    """
    Fref is built on x-periodic surface (x=u,v).
    S built on Fref's geometry, should be UVClosed.

    Give us E, an edge of S. 2drep(E) is not UV connexed.
    We translate 2drep(E) in xdir*xperiod if necessary.

    call : TopOpeBRepTool_CORRISO Tool(Fref);
    Tool.Init(S);
    if (!Tool.UVClosed()) {
    // initialize EdsToCheck,nfybounds,stopatfirst

    Tool.EdgeWithFaultyUV(EdsToCheck,nfybounds,FyEds,stopatfirst);
    if (Tool.SetUVClosed()) S = Tool.GetnewS();
    }
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, FRef: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_CORRISO) -> None: ...

    def Fref(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def GASref(self) -> nanoocp.GeomAdaptor.GeomAdaptor_Surface: ...

    def Refclosed(self, x: int) -> tuple[bool, float]: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def S(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Eds(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def UVClosed(self) -> bool: ...

    def Tol(self, I: int, tol3d: float) -> float: ...

    def PurgeFyClosingE(self, ClEds: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], fyClEds: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def EdgeOUTofBoundsUV(self, E: nanoocp.TopoDS.TopoDS_Edge, onU: bool, tolx: float) -> tuple[int, float]: ...

    def EdgesOUTofBoundsUV(self, EdsToCheck: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], onU: bool, tolx: float, FyEds: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int]) -> bool: ...

    @overload
    def EdgeWithFaultyUV(self, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, int]: ...

    @overload
    def EdgeWithFaultyUV(self, EdsToCheck: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nfybounds: int, fyE: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, int]: ...

    def EdgesWithFaultyUV(self, EdsToCheck: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nfybounds: int, FyEds: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int], stopatfirst: bool = False) -> bool: ...

    def TrslUV(self, onU: bool, FyEds: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int]) -> bool: ...

    def GetnewS(self, newS: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    def UVRep(self, E: nanoocp.TopoDS.TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> bool: ...

    def SetUVRep(self, E: nanoocp.TopoDS.TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> bool: ...

    def Connexity(self, V: nanoocp.TopoDS.TopoDS_Vertex, Eds: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def SetConnexity(self, V: nanoocp.TopoDS.TopoDS_Vertex, Eds: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def AddNewConnexity(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def RemoveOldConnexity(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

class TopOpeBRepTool_GeomTool:
    @overload
    def __init__(self, TypeC3D: TopOpeBRepTool_OutCurveType = ..., CompC3D: bool = True, CompPC1: bool = True, CompPC2: bool = True) -> None:
        """
        Boolean flags <CompC3D>, <CompPC1>, <CompPC2>
        indicate whether the corresponding result curves
        <C3D>, <PC1>, <PC2> of MakeCurves method must or not
        be computed from an intersection line <L>.
        When the line <L> is a walking one, <TypeC3D> is the
        kind of the 3D curve <C3D> to compute:
        - BSPLINE1 to compute a BSpline of degree 1 on the
        walking points of <L>,
        - APPROX to build an approximation curve on the
        walking points of <L>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepTool_GeomTool) -> None: ...

    @overload
    def Define(self, TypeC3D: TopOpeBRepTool_OutCurveType, CompC3D: bool, CompPC1: bool, CompPC2: bool) -> None: ...

    @overload
    def Define(self, TypeC3D: TopOpeBRepTool_OutCurveType) -> None: ...

    @overload
    def Define(self, GT: TopOpeBRepTool_GeomTool) -> None: ...

    def DefineCurves(self, CompC3D: bool) -> None: ...

    def DefinePCurves1(self, CompPC1: bool) -> None: ...

    def DefinePCurves2(self, CompPC2: bool) -> None: ...

    def GetTolerances(self) -> tuple[float, float]: ...

    def SetTolerances(self, tol3d: float, tol2d: float) -> None: ...

    def NbPntMax(self) -> int: ...

    def SetNbPntMax(self, NbPntMax: int) -> None: ...

    def TypeC3D(self) -> TopOpeBRepTool_OutCurveType: ...

    def CompC3D(self) -> bool: ...

    def CompPC1(self) -> bool: ...

    def CompPC2(self) -> bool: ...

class TopOpeBRepTool_CurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, OCT: TopOpeBRepTool_OutCurveType) -> None: ...

    @overload
    def __init__(self, GT: TopOpeBRepTool_GeomTool) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_CurveTool) -> None: ...

    def ChangeGeomTool(self) -> TopOpeBRepTool_GeomTool: ...

    def GetGeomTool(self) -> TopOpeBRepTool_GeomTool: ...

    def SetGeomTool(self, GT: TopOpeBRepTool_GeomTool) -> None: ...

    def MakeCurves(self, min: float, max: float, C3D: nanoocp.Geom.Geom_Curve | None, PC1: nanoocp.Geom2d.Geom2d_Curve | None, PC2: nanoocp.Geom2d.Geom2d_Curve | None, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, float, float]:
        """
        Approximates curves.
        Returns False in the case of failure
        """

    @staticmethod
    def MakeBSpline1fromPnt(P: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> nanoocp.Geom.Geom_Curve: ...

    @staticmethod
    def MakeBSpline1fromPnt2d(P: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @staticmethod
    def IsProjectable(S: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom.Geom_Curve | None) -> bool: ...

    @staticmethod
    def MakePCurveOnFace(S: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom.Geom_Curve | None, first: float = 0.0, last: float = 0.0) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]: ...

class TopOpeBRepTool_FuseEdges:
    """
    This class can detect vertices in a face that can
    be considered useless and then perform the fuse of
    the edges and remove the useless vertices. By
    useles vertices, we mean:
    * vertices that have exactly two connex edges
    * the edges connex to the vertex must have
    exactly the same 2 connex faces.
    * The edges connex to the vertex must have the
    same geometric support.
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, PerformNow: bool = False) -> None:
        """
        Initialise members and build construction of map
        of ancestors.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepTool_FuseEdges) -> None: ...

    def AvoidEdges(self, theMapEdg: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """set edges to avoid being fused"""

    def Edges(self, theMapLstEdg: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]]) -> None:
        """
        returns all the list of edges to be fused
        each list of the map represent a set of connex edges
        that can be fused.
        """

    def ResultEdges(self, theMapEdg: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        returns all the fused edges. each integer entry in
        the map corresponds to the integer in the
        DataMapOfIntegerListOfShape we get in method
        Edges. That is to say, to the list of edges in
        theMapLstEdg(i) corresponds the resulting edge theMapEdge(i)
        """

    def Faces(self, theMapFac: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """returns the map of modified faces."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns myShape modified with the list of internal
        edges removed from it.
        """

    def NbVertices(self) -> int:
        """returns the number of vertices candidate to be removed"""

    def Perform(self) -> None:
        """
        Using map of list of connex edges, fuse each list to
        one edge and then update myShape
        """

class TopOpeBRepTool_makeTransition:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_makeTransition) -> None: ...

    def Initialize(self, E: nanoocp.TopoDS.TopoDS_Edge, pbef: float, paft: float, parE: float, FS: nanoocp.TopoDS.TopoDS_Face, uv: nanoocp.gp.gp_Pnt2d, factor: float) -> bool: ...

    def Setfactor(self, factor: float) -> None: ...

    def Getfactor(self) -> float: ...

    def IsT2d(self) -> bool: ...

    def SetRest(self, ES: nanoocp.TopoDS.TopoDS_Edge, parES: float) -> bool: ...

    def HasRest(self) -> bool: ...

    def MkT2donE(self) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    def MkT3onE(self) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    def MkT3dproj(self) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    def MkTonE(self) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

class TopOpeBRepTool_mkTondgE:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_mkTondgE) -> None: ...

    def Initialize(self, dgE: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, uvi: nanoocp.gp.gp_Pnt2d, Fi: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    def SetclE(self, clE: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def IsT2d(self) -> bool: ...

    def SetRest(self, pari: float, Ei: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def GetAllRest(self, lEi: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @overload
    def MkTonE(self) -> tuple[bool, int, float, float]: ...

    @overload
    def MkTonE(self, Ei: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, int, float, float]: ...

class TopOpeBRepTool_PurgeInternalEdges:
    """
    remove from a shape, the internal edges that are
    not connected to any face in the shape. We can
    get the list of the edges as a
    DataMapOfShapeListOfShape with a Face of the Shape
    as the key and a list of internal edges as the
    value. The list of internal edges means edges
    that are not connected to any face in the shape.

    Example of use:
    NCollection_DataMap<TopoDS_Shape, NCollection_List<TopoDS_Shape>, TopTools_ShapeMapHasher>
    mymap; TopOpeBRepTool_PurgeInternalEdges mypurgealgo(mysolid); mypurgealgo.GetFaces(mymap);
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, PerformNow: bool = True) -> None:
        """
        Initialize members and begin exploration of shape
        depending of the value of PerformNow
        """

    @overload
    def __init__(self, theOther: TopOpeBRepTool_PurgeInternalEdges) -> None: ...

    def Faces(self, theMapFacLstEdg: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        returns the list internal edges associated with
        the faces of the myShape. If PerformNow was False
        when created, then call the private Perform method
        that do the main job.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns myShape modified with the list of internal
        edges removed from it.
        """

    def NbEdges(self) -> int:
        """returns the number of edges candidate to be removed"""

    def IsDone(self) -> bool:
        """
        returns False if the list of internal edges has
        not been extracted
        """

    def Perform(self) -> None:
        """
        Using the list of internal edges from each face,
        rebuild myShape by removing those edges.
        """

class TopOpeBRepTool_REGUS:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_REGUS) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def S(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def MapS(self) -> bool: ...

    @staticmethod
    def WireToFace(Fanc: nanoocp.TopoDS.TopoDS_Face, nWs: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nFs: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    @staticmethod
    def SplitF(Fanc: nanoocp.TopoDS.TopoDS_Face, FSplits: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def SplitFaces(self) -> bool: ...

    def REGU(self) -> bool: ...

    def SetFsplits(self, Fsplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def GetFsplits(self, Fsplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def SetOshNsh(self, OshNsh: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def GetOshNsh(self, OshNsh: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def InitBlock(self) -> bool: ...

    def NextinBlock(self) -> bool: ...

    def NearestF(self, e: nanoocp.TopoDS.TopoDS_Edge, lof: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], ffound: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

class TopOpeBRepTool_REGUW:
    @overload
    def __init__(self, FRef: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_REGUW) -> None: ...

    def Fref(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def SetEsplits(self, Esplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def GetEsplits(self, Esplits: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def SetOwNw(self, OwNw: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def GetOwNw(self, OwNw: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def SplitEds(self) -> bool: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def S(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def HasInit(self) -> bool: ...

    def MapS(self) -> bool: ...

    @overload
    def REGU(self, istep: int, Scur: nanoocp.TopoDS.TopoDS_Shape, Splits: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    @overload
    def REGU(self) -> bool: ...

    def GetSplits(self, Splits: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def InitBlock(self) -> bool: ...

    def NextinBlock(self) -> bool: ...

    def NearestE(self, loe: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], efound: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def Connexity(self, v: nanoocp.TopoDS.TopoDS_Vertex, co: TopOpeBRepTool_connexity) -> bool: ...

    def AddNewConnexity(self, v: nanoocp.TopoDS.TopoDS_Vertex, OriKey: int, e: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def RemoveOldConnexity(self, v: nanoocp.TopoDS.TopoDS_Vertex, OriKey: int, e: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def UpdateMultiple(self, v: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

class TopOpeBRepTool_SolidClassifier:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_SolidClassifier) -> None: ...

    def Clear(self) -> None: ...

    def LoadSolid(self, S: nanoocp.TopoDS.TopoDS_Solid) -> None: ...

    @overload
    def Classify(self, S: nanoocp.TopoDS.TopoDS_Solid, P: nanoocp.gp.gp_Pnt, Tol: float) -> nanoocp.TopAbs.TopAbs_State:
        """
        compute the position of point <P> regarding with the
        geometric domain of the solid <S>.
        """

    @overload
    def Classify(self, S: nanoocp.TopoDS.TopoDS_Shell, P: nanoocp.gp.gp_Pnt, Tol: float) -> nanoocp.TopAbs.TopAbs_State:
        """
        compute the position of point <P> regarding with the
        geometric domain of the shell <S>.
        """

    def LoadShell(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None: ...

    def State(self) -> nanoocp.TopAbs.TopAbs_State: ...

class TopOpeBRepTool_ShapeClassifier:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, SRef: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        SRef is the reference shape.
        StateShapeShape(S) calls will classify S with SRef.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepTool_ShapeClassifier) -> None: ...

    def ClearAll(self) -> None:
        """reset all internal data (SolidClassifier included)"""

    def ClearCurrent(self) -> None:
        """reset all internal data (except SolidClassified)"""

    def SetReference(self, SRef: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Set SRef as reference shape
        the next StateShapeReference(S,AvoidS) calls will classify S with SRef.
        """

    @overload
    def StateShapeShape(self, S: nanoocp.TopoDS.TopoDS_Shape, SRef: nanoocp.TopoDS.TopoDS_Shape, samedomain: int = 0) -> nanoocp.TopAbs.TopAbs_State:
        """
        classify shape S compared with shape SRef.
        samedomain = 0 : S1,S2 are not same domain
        samedomain = 1 : S1,S2 are same domain
        """

    @overload
    def StateShapeShape(self, S: nanoocp.TopoDS.TopoDS_Shape, AvoidS: nanoocp.TopoDS.TopoDS_Shape, SRef: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """
        classify shape S compared with shape SRef.
        AvoidS is not used in classification; AvoidS may be IsNull().
        (useful to avoid ON or UNKNOWN state in special cases)
        """

    @overload
    def StateShapeShape(self, S: nanoocp.TopoDS.TopoDS_Shape, LAvoidS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], SRef: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """
        classify shape S compared with shape SRef.
        LAvoidS is list of S subshapes to avoid in classification
        AvoidS is not used in classification; AvoidS may be IsNull().
        (useful to avoid ON or UNKNOWN state in special cases)
        """

    @overload
    def SameDomain(self) -> int: ...

    @overload
    def SameDomain(self, samedomain: int) -> None:
        """
        set mode for next StateShapeShape call
        samedomain = true --> S,Sref are same domain --> point
        on restriction (ON S) is used to classify S.
        samedomain = false --> S,Sref are not domain --> point
        not on restriction of S (IN S) is used to classify S.
        samedomain value is used only in next StateShapeShape call
        """

    @overload
    def StateShapeReference(self, S: nanoocp.TopoDS.TopoDS_Shape, AvoidS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """
        classify shape S compared with reference shape.
        AvoidS is not used in classification; AvoidS may be IsNull().
        (useful to avoid ON or UNKNOWN state in special cases)
        """

    @overload
    def StateShapeReference(self, S: nanoocp.TopoDS.TopoDS_Shape, LAvoidS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> nanoocp.TopAbs.TopAbs_State:
        """
        classify shape S compared with reference shape.
        LAvoidS is list of S subshapes to avoid in classification
        (useful to avoid ON or UNKNOWN state in special cases)
        """

    def ChangeSolidClassifier(self) -> TopOpeBRepTool_SolidClassifier: ...

    def StateP2DReference(self, P2D: nanoocp.gp.gp_Pnt2d) -> None:
        """classify point P2D with myRef"""

    def StateP3DReference(self, P3D: nanoocp.gp.gp_Pnt) -> None:
        """classify point P3D with myRef"""

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """return field myState"""

    def P2D(self) -> nanoocp.gp.gp_Pnt2d: ...

    def P3D(self) -> nanoocp.gp.gp_Pnt: ...

class TopOpeBRepTool_ShapeExplorer(nanoocp.TopExp.TopExp_Explorer):
    """
    Extends TopExp_Explorer by counting index of current item
    (for tracing and debug)
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty explorer, becomes useful after Init."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, ToFind: nanoocp.TopAbs.TopAbs_ShapeEnum, ToAvoid: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None:
        """
        Creates an Explorer on the Shape <S>.

        <ToFind> is the type of shapes to search.
        TopAbs_VERTEX, TopAbs_EDGE, ...

        <ToAvoid> is the type of shape to skip in the
        exploration. If <ToAvoid> is equal or less
        complex than <ToFind> or if <ToAVoid> is SHAPE it
        has no effect on the exploration.
        """

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, ToFind: nanoocp.TopAbs.TopAbs_ShapeEnum, ToAvoid: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    def Next(self) -> None:
        """Moves to the next Shape in the exploration."""

    def Index(self) -> int:
        """Index of current sub-shape"""

    def DumpCurrent(self) -> object:
        """Dump info on current shape to stream"""

class TopOpeBRepTool_ShapeTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_ShapeTool) -> None: ...

    @staticmethod
    def Tolerance(S: nanoocp.TopoDS.TopoDS_Shape) -> float:
        """
        Returns the tolerance of the shape <S>.
        If the shape <S> is Null, returns 0.
        """

    @staticmethod
    def Pnt(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.gp.gp_Pnt:
        """Returns 3D point of vertex <S>."""

    @overload
    @staticmethod
    def BASISCURVE(C: nanoocp.Geom.Geom_Curve | None) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    @staticmethod
    def BASISCURVE(E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    @staticmethod
    def BASISSURFACE(S: nanoocp.Geom.Geom_Surface | None) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    @staticmethod
    def BASISSURFACE(F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    @staticmethod
    def UVBOUNDS(S: nanoocp.Geom.Geom_Surface | None) -> tuple[bool, bool, float, float, float, float]: ...

    @overload
    @staticmethod
    def UVBOUNDS(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool, float, float, float, float]: ...

    @staticmethod
    def AdjustOnPeriodic(S: nanoocp.TopoDS.TopoDS_Shape) -> tuple[float, float]:
        """
        adjust u,v values in UVBounds of the domain of the
        geometric shape <S>, according to Uperiodicity and
        VPeriodicity of the domain.
        <S> is assumed to be a face.
        u and/or v is/are not modified when the domain is
        not periodic in U and/or V .
        """

    @staticmethod
    def Closed(S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """indicates whether shape S1 is a closing shape on S2 or not."""

    @staticmethod
    def PeriodizeParameter(par: float, EE: nanoocp.TopoDS.TopoDS_Shape, FF: nanoocp.TopoDS.TopoDS_Shape) -> float: ...

    @staticmethod
    def ShapesSameOriented(S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def SurfacesSameOriented(S1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, S2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> bool: ...

    @staticmethod
    def FacesSameOriented(F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def CurvesSameOriented(C1: nanoocp.BRepAdaptor.BRepAdaptor_Curve, C2: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> bool: ...

    @staticmethod
    def EdgesSameOriented(E1: nanoocp.TopoDS.TopoDS_Shape, E2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @overload
    @staticmethod
    def EdgeData(BRAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, P: float, T: nanoocp.gp.gp_Dir, N: nanoocp.gp.gp_Dir) -> tuple[float, float]:
        """
        Compute tangent T, normal N, curvature C at point of parameter
        P on curve BRAC. Returns the tolerance indicating if T,N are null.
        """

    @overload
    @staticmethod
    def EdgeData(E: nanoocp.TopoDS.TopoDS_Shape, P: float, T: nanoocp.gp.gp_Dir, N: nanoocp.gp.gp_Dir) -> tuple[float, float]:
        """Same as previous on edge E."""

    @staticmethod
    def Resolution3dU(SU: nanoocp.Geom.Geom_Surface | None, Tol2d: float) -> float: ...

    @staticmethod
    def Resolution3dV(SU: nanoocp.Geom.Geom_Surface | None, Tol2d: float) -> float: ...

    @overload
    @staticmethod
    def Resolution3d(SU: nanoocp.Geom.Geom_Surface | None, Tol2d: float) -> float: ...

    @overload
    @staticmethod
    def Resolution3d(F: nanoocp.TopoDS.TopoDS_Face, Tol2d: float) -> float: ...

class TopOpeBRepTool_TOOL:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepTool_TOOL) -> None: ...

    @staticmethod
    def OriinSor(sub: nanoocp.TopoDS.TopoDS_Shape, S: nanoocp.TopoDS.TopoDS_Shape, checkclo: bool = False) -> int: ...

    @staticmethod
    def OriinSorclosed(sub: nanoocp.TopoDS.TopoDS_Shape, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @staticmethod
    def ClosedE(E: nanoocp.TopoDS.TopoDS_Edge, vclo: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

    @staticmethod
    def ClosedS(F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    @staticmethod
    def IsClosingE(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    @staticmethod
    def IsClosingE(E: nanoocp.TopoDS.TopoDS_Edge, W: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @staticmethod
    def Vertices(E: nanoocp.TopoDS.TopoDS_Edge, Vces: nanoocp.NCollection.NCollection_Array1[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @staticmethod
    def Vertex(Iv: int, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    @staticmethod
    def ParE(Iv: int, E: nanoocp.TopoDS.TopoDS_Edge) -> float: ...

    @staticmethod
    def OnBoundary(par: float, E: nanoocp.TopoDS.TopoDS_Edge) -> int: ...

    @staticmethod
    def UVF(par: float, C2DF: TopOpeBRepTool_C2DF) -> nanoocp.gp.gp_Pnt2d: ...

    @staticmethod
    def ParISO(p2d: nanoocp.gp.gp_Pnt2d, e: nanoocp.TopoDS.TopoDS_Edge, f: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, float]: ...

    @staticmethod
    def ParE2d(p2d: nanoocp.gp.gp_Pnt2d, e: nanoocp.TopoDS.TopoDS_Edge, f: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, float, float]: ...

    @staticmethod
    def Getduv(f: nanoocp.TopoDS.TopoDS_Face, uv: nanoocp.gp.gp_Pnt2d, dir: nanoocp.gp.gp_Vec, factor: float, duv: nanoocp.gp.gp_Dir2d) -> bool: ...

    @staticmethod
    def uvApp(f: nanoocp.TopoDS.TopoDS_Face, e: nanoocp.TopoDS.TopoDS_Edge, par: float, eps: float, uvapp: nanoocp.gp.gp_Pnt2d) -> bool: ...

    @staticmethod
    def TolUV(F: nanoocp.TopoDS.TopoDS_Face, tol3d: float) -> float: ...

    @staticmethod
    def TolP(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> float: ...

    @staticmethod
    def minDUV(F: nanoocp.TopoDS.TopoDS_Face) -> float: ...

    @staticmethod
    def outUVbounds(uv: nanoocp.gp.gp_Pnt2d, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @staticmethod
    def stuvF(uv: nanoocp.gp.gp_Pnt2d, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[int, int]: ...

    @overload
    @staticmethod
    def TggeomE(par: float, BC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, Tg: nanoocp.gp.gp_Vec) -> bool: ...

    @overload
    @staticmethod
    def TggeomE(par: float, E: nanoocp.TopoDS.TopoDS_Edge, Tg: nanoocp.gp.gp_Vec) -> bool: ...

    @staticmethod
    def TgINSIDE(v: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge, Tg: nanoocp.gp.gp_Vec) -> tuple[bool, int]: ...

    @staticmethod
    def Tg2d(iv: int, E: nanoocp.TopoDS.TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> nanoocp.gp.gp_Vec2d: ...

    @staticmethod
    def Tg2dApp(iv: int, E: nanoocp.TopoDS.TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF, factor: float) -> nanoocp.gp.gp_Vec2d: ...

    @staticmethod
    def tryTg2dApp(iv: int, E: nanoocp.TopoDS.TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF, factor: float) -> nanoocp.gp.gp_Vec2d: ...

    @staticmethod
    def XX(uv: nanoocp.gp.gp_Pnt2d, f: nanoocp.TopoDS.TopoDS_Face, par: float, e: nanoocp.TopoDS.TopoDS_Edge, xx: nanoocp.gp.gp_Dir) -> bool: ...

    @staticmethod
    def Nt(uv: nanoocp.gp.gp_Pnt2d, f: nanoocp.TopoDS.TopoDS_Face, normt: nanoocp.gp.gp_Dir) -> bool: ...

    @staticmethod
    def NggeomF(uv: nanoocp.gp.gp_Pnt2d, F: nanoocp.TopoDS.TopoDS_Face, ng: nanoocp.gp.gp_Vec) -> bool: ...

    @staticmethod
    def NgApp(par: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, tola: float, ngApp: nanoocp.gp.gp_Dir) -> bool: ...

    @staticmethod
    def tryNgApp(par: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, tola: float, ng: nanoocp.gp.gp_Dir) -> bool: ...

    @staticmethod
    def tryOriEinF(par: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> int: ...

    @overload
    @staticmethod
    def IsQuad(E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    @overload
    @staticmethod
    def IsQuad(F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @staticmethod
    def CurvE(E: nanoocp.TopoDS.TopoDS_Edge, par: float, tg0: nanoocp.gp.gp_Dir) -> tuple[bool, float]: ...

    @staticmethod
    def CurvF(F: nanoocp.TopoDS.TopoDS_Face, uv: nanoocp.gp.gp_Pnt2d, tg0: nanoocp.gp.gp_Dir) -> tuple[bool, float, bool]: ...

    @overload
    @staticmethod
    def UVISO(PC: nanoocp.Geom2d.Geom2d_Curve | None, d2d: nanoocp.gp.gp_Dir2d, o2d: nanoocp.gp.gp_Pnt2d) -> tuple[bool, bool, bool]: ...

    @overload
    @staticmethod
    def UVISO(C2DF: TopOpeBRepTool_C2DF, d2d: nanoocp.gp.gp_Dir2d, o2d: nanoocp.gp.gp_Pnt2d) -> tuple[bool, bool, bool]: ...

    @overload
    @staticmethod
    def UVISO(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, d2d: nanoocp.gp.gp_Dir2d, o2d: nanoocp.gp.gp_Pnt2d) -> tuple[bool, bool, bool]: ...

    @overload
    @staticmethod
    def IsonCLO(PC: nanoocp.Geom2d.Geom2d_Curve | None, onU: bool, xfirst: float, xperiod: float, xtol: float) -> bool: ...

    @overload
    @staticmethod
    def IsonCLO(C2DF: TopOpeBRepTool_C2DF, onU: bool, xfirst: float, xperiod: float, xtol: float) -> bool: ...

    @staticmethod
    def TrslUV(t2d: nanoocp.gp.gp_Vec2d, C2DF: TopOpeBRepTool_C2DF) -> None: ...

    @staticmethod
    def TrslUVModifE(t2d: nanoocp.gp.gp_Vec2d, F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    @overload
    @staticmethod
    def Matter(d1: nanoocp.gp.gp_Vec, d2: nanoocp.gp.gp_Vec, ref: nanoocp.gp.gp_Vec) -> float: ...

    @overload
    @staticmethod
    def Matter(d1: nanoocp.gp.gp_Vec2d, d2: nanoocp.gp.gp_Vec2d) -> float: ...

    @overload
    @staticmethod
    def Matter(xx1: nanoocp.gp.gp_Dir, nt1: nanoocp.gp.gp_Dir, xx2: nanoocp.gp.gp_Dir, nt2: nanoocp.gp.gp_Dir, tola: float) -> tuple[bool, float]: ...

    @overload
    @staticmethod
    def Matter(f1: nanoocp.TopoDS.TopoDS_Face, f2: nanoocp.TopoDS.TopoDS_Face, e: nanoocp.TopoDS.TopoDS_Edge, pare: float, tola: float) -> tuple[bool, float]: ...

    @staticmethod
    def MatterKPtg(f1: nanoocp.TopoDS.TopoDS_Face, f2: nanoocp.TopoDS.TopoDS_Face, e: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]: ...

    @staticmethod
    def Getstp3dF(p: nanoocp.gp.gp_Pnt, f: nanoocp.TopoDS.TopoDS_Face, uv: nanoocp.gp.gp_Pnt2d) -> tuple[bool, nanoocp.TopAbs.TopAbs_State]: ...

    @staticmethod
    def SplitE(Eanc: nanoocp.TopoDS.TopoDS_Edge, Splits: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    @staticmethod
    def MkShell(lF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], She: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def Remove(loS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], toremove: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def WireToFace(Fref: nanoocp.TopoDS.TopoDS_Face, mapWlow: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], lFs: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    @staticmethod
    def EdgeONFace(par: float, ed: nanoocp.TopoDS.TopoDS_Edge, uv: nanoocp.gp.gp_Pnt2d, fa: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]: ...

def FC2D_Prepare(S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

def FC2D_HasC3D(E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

def FC2D_HasCurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

def FC2D_HasOldCurveOnSurface__Geom2d_Curve__float__float__float(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float, float, float]:
    """
    FC2D_HasOldCurveOnSurface__Geom2d_Curve__float__float__float: the C++ overload FC2D_HasOldCurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def FC2D_HasOldCurveOnSurface__Geom2d_Curve(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve]:
    """
    FC2D_HasOldCurveOnSurface__Geom2d_Curve: the C++ overload FC2D_HasOldCurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def FC2D_HasNewCurveOnSurface__Geom2d_Curve__float__float__float(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float, float, float]:
    """
    FC2D_HasNewCurveOnSurface__Geom2d_Curve__float__float__float: the C++ overload FC2D_HasNewCurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def FC2D_HasNewCurveOnSurface__Geom2d_Curve(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve]:
    """
    FC2D_HasNewCurveOnSurface__Geom2d_Curve: the C++ overload FC2D_HasNewCurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

@overload
def FC2D_CurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, trim3d: bool = False) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]: ...

@overload
def FC2D_CurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, EF: nanoocp.TopoDS.TopoDS_Edge, trim3d: bool = False) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]: ...

def FC2D_MakeCurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, trim3d: bool = False) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]: ...

def FC2D_EditableCurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, trim3d: bool = False) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]: ...

def FC2D_AddNewCurveOnSurface(PC: nanoocp.Geom2d.Geom2d_Curve | None, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, f: float, l: float, tol: float) -> int: ...

def FBOX_Prepare() -> None: ...

def FBOX_GetHBoxTool() -> TopOpeBRepTool_HBoxTool: ...

def FBOX_Box(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Bnd.Bnd_Box: ...

def BASISCURVE2D(C: nanoocp.Geom2d.Geom2d_Curve | None) -> nanoocp.Geom2d.Geom2d_Curve: ...

@overload
def FUN_tool_dirC(par: float, C: nanoocp.Geom.Geom_Curve | None) -> nanoocp.gp.gp_Dir: ...

@overload
def FUN_tool_dirC(par: float, BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> nanoocp.gp.gp_Dir: ...

def FUN_tool_onapex(p2d: nanoocp.gp.gp_Pnt2d, S: nanoocp.Geom.Geom_Surface | None) -> bool: ...

def FUN_tool_ngS(p2d: nanoocp.gp.gp_Pnt2d, S: nanoocp.Geom.Geom_Surface | None) -> nanoocp.gp.gp_Dir: ...

@overload
def FUN_tool_line(C3d: nanoocp.Geom.Geom_Curve | None) -> bool: ...

@overload
def FUN_tool_line(C2d: nanoocp.Geom2d.Geom2d_Curve | None) -> bool: ...

@overload
def FUN_tool_line(E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

@overload
def FUN_tool_line(BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> bool: ...

def FUN_quadCT(CT: nanoocp.GeomAbs.GeomAbs_CurveType) -> bool: ...

@overload
def FUN_tool_quad(C3d: nanoocp.Geom.Geom_Curve | None) -> bool: ...

@overload
def FUN_tool_quad(pc: nanoocp.Geom2d.Geom2d_Curve | None) -> bool: ...

@overload
def FUN_tool_quad(S: nanoocp.Geom.Geom_Surface | None) -> bool: ...

@overload
def FUN_tool_quad(E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

@overload
def FUN_tool_quad(BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> bool: ...

@overload
def FUN_tool_quad(F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

def FUN_tool_closed(S: nanoocp.Geom.Geom_Surface | None) -> tuple[bool, bool, float, bool, float]: ...

def FUN_tool_UpdateBnd2d(B2d: nanoocp.Bnd.Bnd_Box2d, newB2d: nanoocp.Bnd.Bnd_Box2d) -> None: ...

def FUN_tool_nCinsideS(tgC: nanoocp.gp.gp_Dir, ngS: nanoocp.gp.gp_Dir) -> nanoocp.gp.gp_Dir: ...

def FUN_tool_nC2dINSIDES(tgC2d: nanoocp.gp.gp_Dir2d) -> nanoocp.gp.gp_Dir2d: ...

@overload
def FUN_tool_bounds(E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[float, float]: ...

@overload
def FUN_tool_bounds(F: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, float, float, float, float]: ...

@overload
def FUN_tool_getindex(ponc: nanoocp.Extrema.Extrema_ExtPC) -> int: ...

@overload
def FUN_tool_getindex(ponc: nanoocp.Extrema.Extrema_ExtPC2d) -> int: ...

@overload
def FUN_tool_projPonC(P: nanoocp.gp.gp_Pnt, tole: float, BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, pmin: float, pmax: float) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_projPonC(P: nanoocp.gp.gp_Pnt, BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, pmin: float, pmax: float) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_projPonC(P: nanoocp.gp.gp_Pnt, BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_projPonC2D(P: nanoocp.gp.gp_Pnt, tole: float, BAC2D: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d, pmin: float, pmax: float) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_projPonC2D(P: nanoocp.gp.gp_Pnt, BAC2D: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d, pmin: float, pmax: float) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_projPonC2D(P: nanoocp.gp.gp_Pnt, BAC2D: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d) -> tuple[bool, float, float]: ...

def FUN_tool_projPonS(P: nanoocp.gp.gp_Pnt, S: nanoocp.Geom.Geom_Surface | None, UV: nanoocp.gp.gp_Pnt2d, anExtFlag: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, anExtAlgo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> tuple[bool, float]: ...

@overload
def FUN_tool_projPonE(P: nanoocp.gp.gp_Pnt, tole: float, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_projPonE(P: nanoocp.gp.gp_Pnt, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]: ...

def FUN_tool_projPonboundedF(P: nanoocp.gp.gp_Pnt, F: nanoocp.TopoDS.TopoDS_Face, UV: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float]: ...

def FUN_tool_projPonF(P: nanoocp.gp.gp_Pnt, F: nanoocp.TopoDS.TopoDS_Face, UV: nanoocp.gp.gp_Pnt2d, anExtFlag: nanoocp.Extrema.Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, anExtAlgo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> tuple[bool, float]: ...

@overload
def FSC_GetPSC() -> TopOpeBRepTool_ShapeClassifier: ...

@overload
def FSC_GetPSC(S: nanoocp.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_ShapeClassifier: ...

def FSC_StatePonFace(P: nanoocp.gp.gp_Pnt, F: nanoocp.TopoDS.TopoDS_Shape, PSC: TopOpeBRepTool_ShapeClassifier) -> nanoocp.TopAbs.TopAbs_State: ...

def FSC_StateEonFace(E: nanoocp.TopoDS.TopoDS_Shape, t: float, F: nanoocp.TopoDS.TopoDS_Shape, PSC: TopOpeBRepTool_ShapeClassifier) -> nanoocp.TopAbs.TopAbs_State: ...

def FTOL_FaceTolerances(B1: nanoocp.Bnd.Bnd_Box, B2: nanoocp.Bnd.Bnd_Box, myFace1: nanoocp.TopoDS.TopoDS_Face, myFace2: nanoocp.TopoDS.TopoDS_Face, mySurface1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, mySurface2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> tuple[float, float, float, float]: ...

@overload
def FTOL_FaceTolerances3d(myFace1: nanoocp.TopoDS.TopoDS_Face, myFace2: nanoocp.TopoDS.TopoDS_Face) -> float: ...

@overload
def FTOL_FaceTolerances3d(B1: nanoocp.Bnd.Bnd_Box, B2: nanoocp.Bnd.Bnd_Box, myFace1: nanoocp.TopoDS.TopoDS_Face, myFace2: nanoocp.TopoDS.TopoDS_Face, mySurface1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, mySurface2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> tuple[float, float, float, float]: ...

def FTOL_FaceTolerances2d(B1: nanoocp.Bnd.Bnd_Box, B2: nanoocp.Bnd.Bnd_Box, myFace1: nanoocp.TopoDS.TopoDS_Face, myFace2: nanoocp.TopoDS.TopoDS_Face, mySurface1: nanoocp.BRepAdaptor.BRepAdaptor_Surface, mySurface2: nanoocp.BRepAdaptor.BRepAdaptor_Surface) -> tuple[float, float]: ...

def FUN_tool_tolUV(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[float, float]: ...

def FUN_tool_direct(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]: ...

def FUN_tool_geombounds(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, float, float, float, float]: ...

def FUN_tool_isobounds(F: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, float, float, float, float]: ...

def FUN_tool_outbounds(Sh: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, float, float, float, float, bool]: ...

@overload
def FUN_tool_PinC(P: nanoocp.gp.gp_Pnt, BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, pmin: float, pmax: float, tol: float) -> bool: ...

@overload
def FUN_tool_PinC(P: nanoocp.gp.gp_Pnt, BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, tol: float) -> bool: ...

@overload
def FUN_tool_value(par: float, E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.gp.gp_Pnt) -> bool: ...

@overload
def FUN_tool_value(UV: nanoocp.gp.gp_Pnt2d, F: nanoocp.TopoDS.TopoDS_Face, P: nanoocp.gp.gp_Pnt) -> bool: ...

@overload
def FUN_tool_staPinE(P: nanoocp.gp.gp_Pnt, E: nanoocp.TopoDS.TopoDS_Edge, tol: float) -> nanoocp.TopAbs.TopAbs_State: ...

@overload
def FUN_tool_staPinE(P: nanoocp.gp.gp_Pnt, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopAbs.TopAbs_State: ...

def FUN_tool_orientVinE(v: nanoocp.TopoDS.TopoDS_Vertex, e: nanoocp.TopoDS.TopoDS_Edge) -> int: ...

def FUN_tool_orientEinF(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation]: ...

def FUN_tool_orientEinFFORWARD(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation]: ...

def FUN_tool_EboundF(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

@overload
def FUN_tool_nggeomF(p2d: nanoocp.gp.gp_Pnt2d, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.gp.gp_Vec: ...

@overload
def FUN_tool_nggeomF(paronE: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, nggeomF: nanoocp.gp.gp_Vec) -> bool: ...

@overload
def FUN_tool_nggeomF(paronE: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, nggeomF: nanoocp.gp.gp_Vec, tol: float) -> bool: ...

def FUN_tool_EtgF(paronE: float, E: nanoocp.TopoDS.TopoDS_Edge, p2d: nanoocp.gp.gp_Pnt2d, F: nanoocp.TopoDS.TopoDS_Face, tola: float) -> bool: ...

def FUN_tool_EtgOOE(paronE: float, E: nanoocp.TopoDS.TopoDS_Edge, paronOOE: float, OOE: nanoocp.TopoDS.TopoDS_Edge, tola: float) -> bool: ...

@overload
def FUN_tool_getgeomxx(Fi: nanoocp.TopoDS.TopoDS_Face, Ei: nanoocp.TopoDS.TopoDS_Edge, parOnEi: float, ngFi: nanoocp.gp.gp_Dir) -> nanoocp.gp.gp_Vec: ...

@overload
def FUN_tool_getgeomxx(Fi: nanoocp.TopoDS.TopoDS_Face, Ei: nanoocp.TopoDS.TopoDS_Edge, parOnEi: float) -> nanoocp.gp.gp_Vec: ...

def FUN_nearestISO(F: nanoocp.TopoDS.TopoDS_Face, xpar: float, isoU: bool) -> tuple[bool, float, float]: ...

@overload
def FUN_tool_getxx(Fi: nanoocp.TopoDS.TopoDS_Face, Ei: nanoocp.TopoDS.TopoDS_Edge, parOnEi: float, ngFi: nanoocp.gp.gp_Dir, XX: nanoocp.gp.gp_Dir) -> bool: ...

@overload
def FUN_tool_getxx(Fi: nanoocp.TopoDS.TopoDS_Face, Ei: nanoocp.TopoDS.TopoDS_Edge, parOnEi: float, XX: nanoocp.gp.gp_Dir) -> bool: ...

def FUN_tool_getdxx(F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge, parE: float, XX: nanoocp.gp.gp_Vec2d) -> bool: ...

def FUN_tool_EitangenttoFe(ngFe: nanoocp.gp.gp_Dir, Ei: nanoocp.TopoDS.TopoDS_Edge, parOnEi: float) -> bool: ...

def FUN_tool_typ(E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

def FUN_tool_plane(F: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_tool_cylinder(F: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_tool_closedS__bool__float__bool__float(F: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, bool, float, bool, float]:
    """
    FUN_tool_closedS__bool__float__bool__float: the C++ overload FUN_tool_closedS(const TopoDS_Shape &, bool &, double &, bool &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def FUN_tool_closedS(F: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_tool_closedS__bool__float__float(F: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, bool, float, float]:
    """
    FUN_tool_closedS__bool__float__float: the C++ overload FUN_tool_closedS(const TopoDS_Shape &, bool &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
    """

def FUN_tool_mkBnd2d(W: nanoocp.TopoDS.TopoDS_Shape, FF: nanoocp.TopoDS.TopoDS_Shape, B2d: nanoocp.Bnd.Bnd_Box2d) -> None: ...

def FUN_tool_IsClosingE(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

def FUN_tool_ClosingE(E: nanoocp.TopoDS.TopoDS_Edge, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

def FUN_tool_inS(subshape: nanoocp.TopoDS.TopoDS_Shape, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_tool_Eshared(v: nanoocp.TopoDS.TopoDS_Shape, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape, Eshared: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

def FUN_tool_parVonE(v: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]: ...

@overload
def FUN_tool_parE(E0: nanoocp.TopoDS.TopoDS_Edge, par0: float, E: nanoocp.TopoDS.TopoDS_Edge, tol: float) -> tuple[bool, float]: ...

@overload
def FUN_tool_parE(E0: nanoocp.TopoDS.TopoDS_Edge, par0: float, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]: ...

@overload
def FUN_tool_paronEF(E: nanoocp.TopoDS.TopoDS_Edge, par: float, F: nanoocp.TopoDS.TopoDS_Face, UV: nanoocp.gp.gp_Pnt2d, tol: float) -> bool: ...

@overload
def FUN_tool_paronEF(E: nanoocp.TopoDS.TopoDS_Edge, par: float, F: nanoocp.TopoDS.TopoDS_Face, UV: nanoocp.gp.gp_Pnt2d) -> bool: ...

@overload
def FUN_tool_parF(E: nanoocp.TopoDS.TopoDS_Edge, par: float, F: nanoocp.TopoDS.TopoDS_Face, UV: nanoocp.gp.gp_Pnt2d, tol: float) -> bool: ...

@overload
def FUN_tool_parF(E: nanoocp.TopoDS.TopoDS_Edge, par: float, F: nanoocp.TopoDS.TopoDS_Face, UV: nanoocp.gp.gp_Pnt2d) -> bool: ...

def FUN_tool_tggeomE(paronE: float, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.gp.gp_Vec: ...

def FUN_tool_findPinBAC(BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]: ...

def FUN_tool_findparinBAC(BAC: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> tuple[bool, float]: ...

def FUN_tool_findparinE(E: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, float]: ...

def FUN_tool_findPinE(E: nanoocp.TopoDS.TopoDS_Shape, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]: ...

@overload
def FUN_tool_maxtol(S: nanoocp.TopoDS.TopoDS_Shape, typ: nanoocp.TopAbs.TopAbs_ShapeEnum) -> tuple[bool, float]: ...

@overload
def FUN_tool_maxtol(S: nanoocp.TopoDS.TopoDS_Shape) -> float: ...

def FUN_tool_nbshapes(S: nanoocp.TopoDS.TopoDS_Shape, typ: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int: ...

def FUN_tool_shapes(S: nanoocp.TopoDS.TopoDS_Shape, typ: nanoocp.TopAbs.TopAbs_ShapeEnum, ltyp: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

def FUN_tool_comparebndkole(sh1: nanoocp.TopoDS.TopoDS_Shape, sh2: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

def FUN_tool_SameOri(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

def FUN_tool_haspc(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

@overload
def FUN_tool_pcurveonF(F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

@overload
def FUN_tool_pcurveonF(fF: nanoocp.TopoDS.TopoDS_Face, faultyE: nanoocp.TopoDS.TopoDS_Edge, C2d: nanoocp.Geom2d.Geom2d_Curve | None, newf: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

@overload
def FUN_tool_curvesSO(E1: nanoocp.TopoDS.TopoDS_Edge, p1: float, E2: nanoocp.TopoDS.TopoDS_Edge, p2: float) -> tuple[bool, bool]: ...

@overload
def FUN_tool_curvesSO(E1: nanoocp.TopoDS.TopoDS_Edge, p1: float, E2: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, bool]: ...

@overload
def FUN_tool_curvesSO(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, bool]: ...

def FUN_tool_findAncestor(lF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], E: nanoocp.TopoDS.TopoDS_Edge, Fanc: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

def FUN_ds_CopyEdge(Ein: nanoocp.TopoDS.TopoDS_Shape, Eou: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

def FUN_ds_Parameter(E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape, P: float) -> None: ...

def FUN_tool_MakeWire(loE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], newW: nanoocp.TopoDS.TopoDS_Wire) -> bool: ...
