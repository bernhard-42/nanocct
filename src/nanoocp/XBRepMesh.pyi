"""OCCT package XBRepMesh (toolkit TKXMesh)"""

from typing import overload

import nanoocp.BRepMesh
import nanoocp.Standard
import nanoocp.TopoDS


class XBRepMesh_Factory(nanoocp.BRepMesh.BRepMesh_DiscretAlgoFactory):
    """
    Factory for creating XBRepMesh meshing algorithm instances.
    This factory is registered under the name "XBRepMesh" and provides
    an alternative meshing algorithm based on BRepMesh_IncrementalMesh.
    """

    @overload
    def __init__(self) -> None:
        """Constructor. Registers this factory under the name "XBRepMesh"."""

    @overload
    def __init__(self, theOther: XBRepMesh_Factory) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CreateAlgorithm(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLinDeflection: float, theAngDeflection: float) -> nanoocp.BRepMesh.BRepMesh_DiscretRoot:
        """
        Creates a new meshing algorithm instance.
        @param[in] theShape         shape to be meshed
        @param[in] theLinDeflection linear deflection for meshing
        @param[in] theAngDeflection angular deflection for meshing
        @return new meshing algorithm instance
        """
