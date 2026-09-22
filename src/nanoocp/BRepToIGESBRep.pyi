"""OCCT package BRepToIGESBRep (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.BRepToIGES
import nanoocp.IGESData
import nanoocp.IGESSolid
import nanoocp.Message
import nanoocp.TopoDS


class BRepToIGESBRep_Entity(nanoocp.BRepToIGES.BRepToIGES_BREntity):
    """provides methods to transfer BRep entity from CASCADE to IGESBRep."""

    @overload
    def __init__(self) -> None:
        """Creates a tool Entity"""

    @overload
    def __init__(self, theOther: BRepToIGESBRep_Entity) -> None: ...

    def Clear(self) -> None:
        """Clears the contents of the fields"""

    def TransferVertexList(self) -> None:
        """Create the VertexList entity"""

    def IndexVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex) -> int:
        """Returns the index of <myvertex> in "myVertices\""""

    def AddVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex) -> int:
        """
        Stores <myvertex> in "myVertices"
        Returns the index of <myvertex>.
        """

    def TransferEdgeList(self) -> None:
        """Transfer an Edge entity from TopoDS to IGES"""

    def IndexEdge(self, myedge: nanoocp.TopoDS.TopoDS_Edge) -> int:
        """Returns the index of <myedge> in "myEdges\""""

    def AddEdge(self, myedge: nanoocp.TopoDS.TopoDS_Edge, mycurve3d: nanoocp.IGESData.IGESData_IGESEntity | None) -> int:
        """
        Stores <myedge> in "myEdges" and <mycurve3d> in "myCurves".
        Returns the index of <myedge>.
        """

    def TransferShape(self, start: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Returns the result of the transfert of any Shape
        If the transfer has failed, this member returns a NullEntity.
        """

    @overload
    def TransferEdge(self, myedge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.IGESData.IGESData_IGESEntity: ...

    @overload
    def TransferEdge(self, myedge: nanoocp.TopoDS.TopoDS_Edge, myface: nanoocp.TopoDS.TopoDS_Face, length: float) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an Edge entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferWire(self, mywire: nanoocp.TopoDS.TopoDS_Wire, myface: nanoocp.TopoDS.TopoDS_Face, length: float) -> nanoocp.IGESSolid.IGESSolid_Loop:
        """
        Transfer a Wire entity from TopoDS to IGES.
        Returns the curve associated to mywire in the parametric space of myface.
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferFace(self, start: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.IGESSolid.IGESSolid_Face:
        """
        Transfer a Face entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferShell(self, start: nanoocp.TopoDS.TopoDS_Shell, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESSolid.IGESSolid_Shell:
        """
        Transfer an Shell entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferSolid(self, start: nanoocp.TopoDS.TopoDS_Solid, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESSolid.IGESSolid_ManifoldSolid:
        """
        Transfer a Solid entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferCompSolid(self, start: nanoocp.TopoDS.TopoDS_CompSolid, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an CompSolid entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferCompound(self, start: nanoocp.TopoDS.TopoDS_Compound, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Compound entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """
