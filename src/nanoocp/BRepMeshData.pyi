"""OCCT package BRepMeshData (toolkit TKMesh)"""

from typing import overload

import nanoocp.IMeshData
import nanoocp.Standard
import nanoocp.TopoDS


class BRepMeshData_Model(nanoocp.IMeshData.IMeshData_Model):
    """Default implementation of model entity."""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Constructor.
        Initializes empty model.
        """

    @overload
    def __init__(self, theOther: BRepMeshData_Model) -> None: ...

    def GetMaxSize(self) -> float:
        """Returns maximum size of shape's bounding box."""

    def SetMaxSize(self, theValue: float) -> None:
        """Sets maximum size of shape's bounding box."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def FacesNb(self) -> int:
        """
        @name discrete faces
        Returns number of faces in discrete model.
        """

    def AddFace(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.IMeshData.IMeshData_Face:
        """Adds new face to shape model."""

    def GetFace(self, theIndex: int) -> nanoocp.IMeshData.IMeshData_Face:
        """Gets model's face with the given index."""

    def EdgesNb(self) -> int:
        """
        @name discrete edges
        Returns number of edges in discrete model.
        """

    def AddEdge(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.IMeshData.IMeshData_Edge:
        """Adds new edge to shape model."""

    def GetEdge(self, theIndex: int) -> nanoocp.IMeshData.IMeshData_Edge:
        """Gets model's edge with the given index."""
