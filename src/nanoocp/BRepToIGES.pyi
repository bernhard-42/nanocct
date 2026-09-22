"""OCCT package BRepToIGES (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.Geom
import nanoocp.IGESData
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.gp
import nanoocp.TopTools


class BRepToIGES_BREntity:
    """provides methods to transfer BRep entity from CASCADE to IGES."""

    @overload
    def __init__(self) -> None:
        """Creates a tool BREntity"""

    @overload
    def __init__(self, theOther: BRepToIGES_BREntity) -> None: ...

    def Init(self) -> None:
        """
        Initializes the field of the tool BREntity with
        default creating values.
        """

    def SetModel(self, model: nanoocp.IGESData.IGESData_IGESModel | None) -> None:
        """Set the value of "TheModel\""""

    def GetModel(self) -> nanoocp.IGESData.IGESData_IGESModel:
        """Returns the value of "TheModel\""""

    def GetUnit(self) -> float:
        """
        Returns the value of the UnitFlag of the header of the model
        in meters.
        """

    def SetTransferProcess(self, TP: nanoocp.Transfer.Transfer_FinderProcess | None) -> None:
        """Set the value of "TheMap\""""

    def GetTransferProcess(self) -> nanoocp.Transfer.Transfer_FinderProcess:
        """Returns the value of "TheMap\""""

    def TransferShape(self, start: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Returns the result of the transfert of any Shape
        If the transfer has failed, this member return a NullEntity.
        """

    @overload
    def AddFail(self, start: nanoocp.TopoDS.TopoDS_Shape, amess: str) -> None: ...

    @overload
    def AddFail(self, start: nanoocp.Standard.Standard_Transient | None, amess: str) -> None:
        """Records a new Fail message"""

    @overload
    def AddWarning(self, start: nanoocp.TopoDS.TopoDS_Shape, amess: str) -> None: ...

    @overload
    def AddWarning(self, start: nanoocp.Standard.Standard_Transient | None, amess: str) -> None:
        """Records a new Warning message"""

    @overload
    def HasShapeResult(self, start: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @overload
    def HasShapeResult(self, start: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if start was already treated and has a result in "TheMap"
        else returns False.
        """

    @overload
    def GetShapeResult(self, start: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the result of the transfer of the Shape "start" contained
        in "TheMap". (if HasShapeResult is True).
        """

    @overload
    def GetShapeResult(self, start: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the result of the transfer of the Transient "start" contained
        in "TheMap". (if HasShapeResult is True).
        """

    @overload
    def SetShapeResult(self, start: nanoocp.TopoDS.TopoDS_Shape, result: nanoocp.Standard.Standard_Transient | None) -> None:
        """set in "TheMap" the result of the transfer of the Shape "start"."""

    @overload
    def SetShapeResult(self, start: nanoocp.Standard.Standard_Transient | None, result: nanoocp.Standard.Standard_Transient | None) -> None:
        """set in "TheMap" the result of the transfer of the Transient "start"."""

    def GetConvertSurfaceMode(self) -> bool:
        """
        Returns mode for conversion of surfaces
        (value of parameter write.convertsurface.mode)
        """

    def GetPCurveMode(self) -> bool:
        """
        Returns mode for writing pcurves
        (value of parameter write.surfacecurve.mode)
        """

class BRepToIGES_BRShell(BRepToIGES_BREntity):
    """
    This class implements the transfer of Shape Entities from Geom
    To IGES. These can be:
    . Vertex
    . Edge
    . Wire
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, BR: BRepToIGES_BREntity) -> None: ...

    @overload
    def __init__(self, theOther: BRepToIGES_BRShell) -> None: ...

    @overload
    def TransferShell(self, start: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an Shape entity from TopoDS to IGES
        This entity must be a Face or a Shell.
        If this Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def TransferShell(self, start: nanoocp.TopoDS.TopoDS_Shell, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an Shell entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

    def TransferFace(self, start: nanoocp.TopoDS.TopoDS_Face, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Face entity from TopoDS to IGES
        If this Entity could not be converted, this member returns a NullEntity.
        """

class BRepToIGES_BRSolid(BRepToIGES_BREntity):
    """
    This class implements the transfer of Shape Entities from Geom
    To IGES. These can be:
    . Vertex
    . Edge
    . Wire
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, BR: BRepToIGES_BREntity) -> None: ...

    @overload
    def __init__(self, theOther: BRepToIGES_BRSolid) -> None: ...

    @overload
    def TransferSolid(self, start: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Shape entity from TopoDS to IGES
        this entity must be a Solid or a CompSolid or a Compound.
        If this Entity could not be converted, this member returns a NullEntity.
        """

    @overload
    def TransferSolid(self, start: nanoocp.TopoDS.TopoDS_Solid, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IGESData.IGESData_IGESEntity:
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

class BRepToIGES_BRWire(BRepToIGES_BREntity):
    """
    This class implements the transfer of Shape Entities
    from Geom To IGES. These can be:
    . Vertex
    . Edge
    . Wire
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, BR: BRepToIGES_BREntity) -> None: ...

    @overload
    def __init__(self, theOther: BRepToIGES_BRWire) -> None: ...

    @overload
    def TransferWire(self, start: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Shape entity from TopoDS to IGES
        this entity must be a Vertex or an Edge or a Wire.
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferWire(self, mywire: nanoocp.TopoDS.TopoDS_Wire) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Wire entity from TopoDS to IGES
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferWire(self, theWire: nanoocp.TopoDS.TopoDS_Wire, theFace: nanoocp.TopoDS.TopoDS_Face, theOriginMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theLength: float) -> tuple[nanoocp.IGESData.IGESData_IGESEntity, nanoocp.IGESData.IGESData_IGESEntity]:
        """
        Transfer a Wire entity from TopoDS to IGES.
        @param[in] theWire input wire
        @param[in] theFace input face
        @param[in] theOriginMap shapemap contains the original shapes. Should be empty if face is not
        reversed
        @param[in] theCurve2d input curve 2d
        @param[in] theLength input surface length
        @return Iges entity (the curve associated to mywire in the parametric space of myface)
        or null if could not be converted
        """

    @overload
    def TransferVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Vertex entity from TopoDS to IGES
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex, myedge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[nanoocp.IGESData.IGESData_IGESEntity, float]:
        """
        Transfer a Vertex entity on an Edge from TopoDS to IGES
        Returns the parameter of myvertex on myedge.
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex, myedge: nanoocp.TopoDS.TopoDS_Edge, myface: nanoocp.TopoDS.TopoDS_Face) -> tuple[nanoocp.IGESData.IGESData_IGESEntity, float]:
        """
        Transfer a Vertex entity of an edge on a Face
        from TopoDS to IGES
        Returns the parameter of myvertex on the pcurve
        of myedge on myface
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex, myedge: nanoocp.TopoDS.TopoDS_Edge, mysurface: nanoocp.Geom.Geom_Surface | None, myloc: nanoocp.TopLoc.TopLoc_Location) -> tuple[nanoocp.IGESData.IGESData_IGESEntity, float]:
        """
        Transfer a Vertex entity of an edge on a Surface
        from TopoDS to IGES
        Returns the parameter of myvertex on the pcurve
        of myedge on mysurface
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferVertex(self, myvertex: nanoocp.TopoDS.TopoDS_Vertex, myface: nanoocp.TopoDS.TopoDS_Face, mypoint: nanoocp.gp.gp_Pnt2d) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer a Vertex entity on a Face from TopoDS to IGES
        Returns the parameters of myvertex on myface
        If this Entity could not be converted,
        this member returns a NullEntity.
        """

    @overload
    def TransferEdge(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theOriginMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theIsBRepMode: bool) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an Edge 3d entity from TopoDS to IGES
        If edge is REVERSED and isBRepMode is False 3D edge curve is reversed
        @param[in] theEdge input edge to transfer
        @param[in] theOriginMap shapemap contains the original shapes. Should be empty if face is not
        reversed
        @param[in] theIsBRepMode indicates if write mode is BRep
        @return Iges entity or null if could not be converted
        """

    @overload
    def TransferEdge(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theOriginMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theLength: float, theIsBRepMode: bool) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Transfer an Edge 2d entity on a Face from TopoDS to IGES
        @param[in] theEdge input edge to transfer
        @param[in] theFace input face to get the surface and UV coordinates from it
        @param[in] theOriginMap shapemap contains the original shapes. Should be empty if face is not
        reversed
        @param[in] theLength input surface length
        @param[in] theIsBRepMode indicates if write mode is BRep
        @return Iges entity or null if could not be converted
        """
