"""OCCT package HLRTopoBRep (toolkit TKHLR)"""

from typing import overload

import nanoocp.Contap
import nanoocp.Geom2d
import nanoocp.HLRAlgo
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.BRepTopAdaptor
import nanoocp.TopTools


class HLRTopoBRep_FaceData:
    """
    Contains the 3 ListOfShape of a Face
    (Internal OutLines, OutLines on restriction and IsoLines).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRTopoBRep_FaceData) -> None: ...

    def FaceIntL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def FaceOutL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def FaceIsoL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddIntL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddOutL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddIsoL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class HLRTopoBRep_VData:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: float, V: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: HLRTopoBRep_VData) -> None: ...

    def Parameter(self) -> float: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class HLRTopoBRep_Data:
    """
    Stores the results of the OutLine and IsoLine
    processes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRTopoBRep_Data) -> None: ...

    def Clear(self) -> None:
        """Clear of all the maps."""

    def Clean(self) -> None:
        """
        Clear of all the data not needed during and after
        the hiding process.
        """

    def EdgeHasSplE(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns True if the Edge is split."""

    def FaceHasIntL(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns True if the Face has internal outline."""

    def FaceHasOutL(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns True if the Face has outlines on restriction."""

    def FaceHasIsoL(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns True if the Face has isolines."""

    def IsSplEEdgeEdge(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def IsIntLFaceEdge(self, F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def IsOutLFaceEdge(self, F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def IsIsoLFaceEdge(self, F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def NewSOldS(self, New: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def EdgeSplE(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of the edges."""

    def FaceIntL(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of the internal OutLines."""

    def FaceOutL(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of the OutLines on restriction."""

    def FaceIsoL(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of the IsoLines."""

    def IsOutV(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> bool:
        """
        Returns True if V is an outline vertex on a
        restriction.
        """

    def IsIntV(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> bool:
        """Returns True if V is an internal outline vertex."""

    def AddOldS(self, NewS: nanoocp.TopoDS.TopoDS_Shape, OldS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddSplE(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddIntL(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddOutL(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddIsoL(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddOutV(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def AddIntV(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def InitEdge(self) -> None: ...

    def MoreEdge(self) -> bool: ...

    def NextEdge(self) -> None: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def InitVertex(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Start an iteration on the vertices of E."""

    def MoreVertex(self) -> bool: ...

    def NextVertex(self) -> None: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Parameter(self) -> float: ...

    def InsertBefore(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: float) -> None:
        """Insert before the current position."""

    def Append(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: float) -> None: ...

class HLRTopoBRep_DSFiller:
    """Provides methods to fill a HLRTopoBRep_Data."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRTopoBRep_DSFiller) -> None: ...

    @staticmethod
    def Insert(S: nanoocp.TopoDS.TopoDS_Shape, FO: nanoocp.Contap.Contap_Contour, DS: HLRTopoBRep_Data, MST: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepTopAdaptor.BRepTopAdaptor_Tool, nanoocp.TopTools.TopTools_ShapeMapHasher], nbIso: int) -> None:
        """
        Stores in <DS> the outlines of <S> using the current
        outliner and stores the isolines in <DS> using a Hatcher.
        """

class HLRTopoBRep_FaceIsoLiner:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: HLRTopoBRep_FaceIsoLiner) -> None: ...

    @staticmethod
    def Perform(FI: int, F: nanoocp.TopoDS.TopoDS_Face, DS: HLRTopoBRep_Data, nbIsos: int) -> None: ...

    @staticmethod
    def MakeVertex(E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.gp.gp_Pnt, Par: float, Tol: float, DS: HLRTopoBRep_Data) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    @staticmethod
    def MakeIsoLine(F: nanoocp.TopoDS.TopoDS_Face, Iso: nanoocp.Geom2d.Geom2d_Line | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, U1: float, U2: float, Tol: float, DS: HLRTopoBRep_Data) -> None: ...

class HLRTopoBRep_OutLiner(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, OriSh: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, OriS: nanoocp.TopoDS.TopoDS_Shape, OutS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: HLRTopoBRep_OutLiner) -> None: ...

    @overload
    def OriginalShape(self, OriS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def OriginalShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def OutLinedShape(self, OutS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def OutLinedShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def DataStructure(self) -> HLRTopoBRep_Data: ...

    def Fill(self, P: nanoocp.HLRAlgo.HLRAlgo_Projector, MST: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepTopAdaptor.BRepTopAdaptor_Tool, nanoocp.TopTools.TopTools_ShapeMapHasher], nbIso: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
