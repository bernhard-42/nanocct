"""C++ namespace BRepGraphInc_Load (OCCT package BRepGraphInc)"""

from typing import overload


class Counts:
    """
    Final section counts needed to prepare `BRepGraphInc_Storage` for indexed load.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Counts) -> None: ...

    @property
    def NbVertices(self) -> int:
        """Number of `VertexDef` slots."""

    @NbVertices.setter
    def NbVertices(self, arg: int, /) -> None: ...

    @property
    def NbEdges(self) -> int:
        """Number of `EdgeDef` slots."""

    @NbEdges.setter
    def NbEdges(self, arg: int, /) -> None: ...

    @property
    def NbCoEdges(self) -> int:
        """Number of `CoEdgeDef` slots."""

    @NbCoEdges.setter
    def NbCoEdges(self, arg: int, /) -> None: ...

    @property
    def NbWires(self) -> int:
        """Number of `WireDef` slots."""

    @NbWires.setter
    def NbWires(self, arg: int, /) -> None: ...

    @property
    def NbFaces(self) -> int:
        """Number of `FaceDef` slots."""

    @NbFaces.setter
    def NbFaces(self, arg: int, /) -> None: ...

    @property
    def NbShells(self) -> int:
        """Number of `ShellDef` slots."""

    @NbShells.setter
    def NbShells(self, arg: int, /) -> None: ...

    @property
    def NbSolids(self) -> int:
        """Number of `SolidDef` slots."""

    @NbSolids.setter
    def NbSolids(self, arg: int, /) -> None: ...

    @property
    def NbCompounds(self) -> int:
        """Number of `CompoundDef` slots."""

    @NbCompounds.setter
    def NbCompounds(self, arg: int, /) -> None: ...

    @property
    def NbCompSolids(self) -> int:
        """Number of `CompSolidDef` slots."""

    @NbCompSolids.setter
    def NbCompSolids(self, arg: int, /) -> None: ...

    @property
    def NbProducts(self) -> int:
        """Number of `ProductDef` slots."""

    @NbProducts.setter
    def NbProducts(self, arg: int, /) -> None: ...

    @property
    def NbOccurrences(self) -> int:
        """Number of `OccurrenceDef` slots."""

    @NbOccurrences.setter
    def NbOccurrences(self, arg: int, /) -> None: ...

    @property
    def NbShellRefs(self) -> int:
        """Number of `ShellRef` slots."""

    @NbShellRefs.setter
    def NbShellRefs(self, arg: int, /) -> None: ...

    @property
    def NbFaceRefs(self) -> int:
        """Number of `FaceRef` slots."""

    @NbFaceRefs.setter
    def NbFaceRefs(self, arg: int, /) -> None: ...

    @property
    def NbWireRefs(self) -> int:
        """Number of `WireRef` slots."""

    @NbWireRefs.setter
    def NbWireRefs(self, arg: int, /) -> None: ...

    @property
    def NbVertexRefs(self) -> int:
        """Number of `VertexRef` slots."""

    @NbVertexRefs.setter
    def NbVertexRefs(self, arg: int, /) -> None: ...

    @property
    def NbSolidRefs(self) -> int:
        """Number of `SolidRef` slots."""

    @NbSolidRefs.setter
    def NbSolidRefs(self, arg: int, /) -> None: ...

    @property
    def NbChildRefs(self) -> int:
        """Number of `ChildRef` slots."""

    @NbChildRefs.setter
    def NbChildRefs(self, arg: int, /) -> None: ...

    @property
    def NbOccurrenceRefs(self) -> int:
        """Number of `OccurrenceRef` slots."""

    @NbOccurrenceRefs.setter
    def NbOccurrenceRefs(self, arg: int, /) -> None: ...

    @property
    def NbFaceSurfaceReps(self) -> int:
        """Number of `FaceSurfaceRep` slots."""

    @NbFaceSurfaceReps.setter
    def NbFaceSurfaceReps(self, arg: int, /) -> None: ...

    @property
    def NbEdgeCurve3DReps(self) -> int:
        """Number of `EdgeCurve3DRep` slots."""

    @NbEdgeCurve3DReps.setter
    def NbEdgeCurve3DReps(self, arg: int, /) -> None: ...

    @property
    def NbCoEdgeCurve2DReps(self) -> int:
        """Number of `CoEdgeCurve2DRep` slots."""

    @NbCoEdgeCurve2DReps.setter
    def NbCoEdgeCurve2DReps(self, arg: int, /) -> None: ...

    @property
    def NbFaceTriangulationReps(self) -> int:
        """Number of `FaceTriangulationRep` slots."""

    @NbFaceTriangulationReps.setter
    def NbFaceTriangulationReps(self, arg: int, /) -> None: ...

    @property
    def NbEdgePolygon3DReps(self) -> int:
        """Number of `EdgePolygon3DRep` slots."""

    @NbEdgePolygon3DReps.setter
    def NbEdgePolygon3DReps(self, arg: int, /) -> None: ...

    @property
    def NbCoEdgePolygon2DReps(self) -> int:
        """Number of `CoEdgePolygon2DRep` slots."""

    @NbCoEdgePolygon2DReps.setter
    def NbCoEdgePolygon2DReps(self, arg: int, /) -> None: ...

    @property
    def NbCoEdgePolygonOnTriReps(self) -> int:
        """Number of `CoEdgePolygonOnTriRep` slots."""

    @NbCoEdgePolygonOnTriReps.setter
    def NbCoEdgePolygonOnTriReps(self, arg: int, /) -> None: ...

    @property
    def NbRootProducts(self) -> int:
        """Number of root product ids outside storage tables."""

    @NbRootProducts.setter
    def NbRootProducts(self, arg: int, /) -> None: ...
