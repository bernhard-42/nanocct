"""OCCT package BRepGraph (toolkit TKBRep)"""

import enum
from typing import TypeAlias, overload

import nanoocp.Adaptor3d
from nanoocp.BRepGraph import (
    BRepGraph_DefsIterator as BRepGraph_DefsIterator,
    BRepGraph_RefsIterator as BRepGraph_RefsIterator,
    BRepGraph_ReverseIterator as BRepGraph_ReverseIterator
)
import nanoocp.BRepGraph.BRepGraph_DefsIterator
import nanoocp.BRepGraph.BRepGraph_RefsIterator
import nanoocp.BRepGraphInc
import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Geom2dAdaptor
import nanoocp.GeomAdaptor
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class BRepGraph_NodeId:
    """
    Lightweight typed index into a per-kind node vector inside BRepGraph.

    The pair (NodeKind, Index) forms a unique node identifier within one graph
    instance.  Default-constructed NodeId has Index = UINT32_MAX (invalid).

    NodeId is a value type: cheap to copy, compare, hash.  It carries no
    pointer back to the owning graph; the caller is responsible for using
    it with the correct BRepGraph instance.
    """

    @overload
    def __init__(self) -> None:
        """
        Default: invalid NodeId (Index = UINT32_MAX).
        NodeKind is set to Kind::Solid but is meaningless when !IsValid().
        """

    @overload
    def __init__(self, theKind: BRepGraph_NodeId.Kind, theIdx: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_NodeId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_SolidId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_ShellId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_FaceId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_WireId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_VertexId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_CompoundId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_CompSolidId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_CoEdgeId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_ProductId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_OccurrenceId) -> None: ...

    class Kind(enum.Enum):
        """
        Enumeration of node kinds within a BRepGraph.

        Topology kinds 0-5 cover core hierarchy; Compound(6)/CompSolid(7)
        are container kinds.  Note: ordering does NOT match TopAbs_ShapeEnum.
        Geometry kinds start at 10, leaving room for future topology extensions.
        """

        Solid = 0

        Shell = 1

        Face = 2

        Wire = 3

        Edge = 4

        Vertex = 5

        Compound = 6

        CompSolid = 7

        CoEdge = 8

        Product = 10

        Occurrence = 11

    @staticmethod
    def IsValidKind(theKind: BRepGraph_NodeId.Kind) -> bool:
        """True if the kind value is one of the supported node kinds."""

    @staticmethod
    def IsTopologyKind(theKind: BRepGraph_NodeId.Kind) -> bool:
        """True if the kind is a core topology kind (Solid..CoEdge)."""

    @staticmethod
    def IsAssemblyKind(theKind: BRepGraph_NodeId.Kind) -> bool:
        """True if the kind is an assembly kind (Product or Occurrence)."""

    @staticmethod
    def Start(theKind: BRepGraph_NodeId.Kind) -> BRepGraph_NodeId:
        """First valid id in a dense sequence for the specified kind."""

    @staticmethod
    def Invalid(theKind: BRepGraph_NodeId.Kind = BRepGraph_NodeId.Kind.Solid) -> BRepGraph_NodeId:
        """Invalid sentinel id for the specified kind."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_SolidId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_ShellId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_FaceId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_WireId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_EdgeId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_VertexId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_CompoundId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_CompSolidId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_CoEdgeId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_ProductId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_OccurrenceId, /) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_SolidId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_ShellId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_FaceId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_WireId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_EdgeId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_VertexId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_CompoundId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_CompSolidId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_CoEdgeId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_ProductId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_OccurrenceId, /) -> bool: ...

    def __lt__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_NodeId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_NodeId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def NodeKind(self) -> BRepGraph_NodeId.Kind: ...

    @NodeKind.setter
    def NodeKind(self, arg: BRepGraph_NodeId.Kind, /) -> None: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_SolidId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_SolidId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_SolidId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_SolidId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_SolidId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_SolidId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_SolidId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_SolidId) -> bool: ...

    def __le__(self, theOther: BRepGraph_SolidId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_SolidId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_SolidId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_SolidId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_SolidId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_ShellId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_ShellId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_ShellId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_ShellId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_ShellId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_ShellId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_ShellId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_ShellId) -> bool: ...

    def __le__(self, theOther: BRepGraph_ShellId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_ShellId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_ShellId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_ShellId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_ShellId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_FaceId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_FaceId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_FaceId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_FaceId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_FaceId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_FaceId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_FaceId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_FaceId) -> bool: ...

    def __le__(self, theOther: BRepGraph_FaceId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_FaceId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_FaceId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_FaceId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_FaceId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_WireId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_WireId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_WireId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_WireId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_WireId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_WireId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_WireId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_WireId) -> bool: ...

    def __le__(self, theOther: BRepGraph_WireId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_WireId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_WireId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_WireId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_WireId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_EdgeId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_EdgeId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_EdgeId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_EdgeId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_EdgeId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_EdgeId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_EdgeId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_EdgeId) -> bool: ...

    def __le__(self, theOther: BRepGraph_EdgeId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_EdgeId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_EdgeId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_EdgeId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_EdgeId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_VertexId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_VertexId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_VertexId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_VertexId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_VertexId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_VertexId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_VertexId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_VertexId) -> bool: ...

    def __le__(self, theOther: BRepGraph_VertexId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_VertexId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_VertexId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_VertexId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_VertexId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_CompoundId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_CompoundId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_CompoundId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_CompoundId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_CompoundId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_CompoundId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_CompoundId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_CompoundId) -> bool: ...

    def __le__(self, theOther: BRepGraph_CompoundId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_CompoundId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_CompoundId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_CompoundId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_CompoundId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_CompSolidId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_CompSolidId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_CompSolidId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_CompSolidId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_CompSolidId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_CompSolidId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_CompSolidId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_CompSolidId) -> bool: ...

    def __le__(self, theOther: BRepGraph_CompSolidId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_CompSolidId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_CompSolidId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_CompSolidId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_CompSolidId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_CoEdgeId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_CoEdgeId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_CoEdgeId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_CoEdgeId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_CoEdgeId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_CoEdgeId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_CoEdgeId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_CoEdgeId) -> bool: ...

    def __le__(self, theOther: BRepGraph_CoEdgeId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_CoEdgeId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_CoEdgeId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_CoEdgeId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_CoEdgeId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_ProductId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_ProductId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_ProductId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_ProductId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_ProductId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_ProductId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_ProductId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_ProductId) -> bool: ...

    def __le__(self, theOther: BRepGraph_ProductId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_ProductId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_ProductId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_ProductId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_ProductId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_OccurrenceId:
    """
    @brief Compile-time typed wrapper around BRepGraph_NodeId.

    Provides compile-time kind safety: a Typed<Kind::Face>
    cannot be accidentally used where a Typed<Kind::Edge> is expected.
    Implicitly converts to BRepGraph_NodeId for API continuity.

    @tparam TheKind the BRepGraph_NodeId::Kind this typed id represents
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid (Index = UINT32_MAX)."""

    @overload
    def __init__(self, theIdx: int) -> None:
        """Construct from index."""

    @overload
    def __init__(self, theId: BRepGraph_NodeId) -> None:
        """Construct from an untyped node id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_OccurrenceId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_OccurrenceId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_OccurrenceId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated node slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromNodeId(theId: BRepGraph_NodeId) -> BRepGraph_OccurrenceId:
        """
        Explicit conversion from untyped NodeId.
        Asserts that the Kind matches in debug builds.
        @param[in] theId untyped NodeId to convert
        """

    @overload
    def __eq__(self, theOther: BRepGraph_OccurrenceId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_NodeId) -> bool:
        """Comparison with untyped NodeId (checks both Kind and Index)."""

    @overload
    def __ne__(self, theOther: BRepGraph_OccurrenceId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_NodeId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_OccurrenceId) -> bool: ...

    def __le__(self, theOther: BRepGraph_OccurrenceId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_OccurrenceId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_OccurrenceId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_OccurrenceId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_OccurrenceId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has been soft-removed in the given graph."""

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """Return true if this node has an active owner in the given graph."""

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_RefId:
    """
    Lightweight typed index into a per-kind reference vector inside BRepGraph.

    The pair (Kind, Index) forms a unique reference identifier within one graph
    instance. Default-constructed RefId has Index = UINT32_MAX (invalid).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theKind: BRepGraph_RefId.Kind, theIdx: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_ShellRefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_FaceRefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_WireRefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_VertexRefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_SolidRefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_ChildRefId) -> None: ...

    @overload
    def __init__(self, theFrom: BRepGraph_OccurrenceRefId) -> None: ...

    class Kind(enum.Enum):
        """Enumeration of supported topology reference kinds."""

        Shell = 0

        Face = 1

        Wire = 2

        Vertex = 3

        Solid = 4

        Child = 5

        Occurrence = 6

    @staticmethod
    def IsValidKind(theKind: BRepGraph_RefId.Kind) -> bool:
        """True if the kind value is one of the supported reference kinds."""

    @staticmethod
    def IsTopologyRefKind(theKind: BRepGraph_RefId.Kind) -> bool: ...

    @staticmethod
    def Start(theKind: BRepGraph_RefId.Kind) -> BRepGraph_RefId:
        """First valid id in a dense sequence for the specified kind."""

    @staticmethod
    def Invalid(theKind: BRepGraph_RefId.Kind = BRepGraph_RefId.Kind.Shell) -> BRepGraph_RefId:
        """Invalid sentinel id for the specified kind."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_ShellRefId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_FaceRefId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_WireRefId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_VertexRefId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_SolidRefId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_ChildRefId, /) -> bool: ...

    @overload
    def __eq__(self, arg: BRepGraph_OccurrenceRefId, /) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_ShellRefId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_FaceRefId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_WireRefId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_VertexRefId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_SolidRefId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_ChildRefId, /) -> bool: ...

    @overload
    def __ne__(self, arg: BRepGraph_OccurrenceRefId, /) -> bool: ...

    def __lt__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_RefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_RefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def RefKind(self) -> BRepGraph_RefId.Kind: ...

    @RefKind.setter
    def RefKind(self, arg: BRepGraph_RefId.Kind, /) -> None: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_ShellRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_ShellRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_ShellRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_ShellRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_ShellRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_ShellRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_ShellRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_ShellRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_ShellRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_ShellRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_ShellRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_ShellRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_ShellRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_FaceRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_FaceRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_FaceRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_FaceRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_FaceRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_FaceRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_FaceRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_FaceRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_FaceRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_FaceRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_FaceRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_FaceRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_FaceRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_WireRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_WireRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_WireRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_WireRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_WireRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_WireRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_WireRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_WireRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_WireRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_WireRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_WireRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_WireRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_WireRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_VertexRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_VertexRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_VertexRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_VertexRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_VertexRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_VertexRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_VertexRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_VertexRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_VertexRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_VertexRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_VertexRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_VertexRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_VertexRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_SolidRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_SolidRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_SolidRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_SolidRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_SolidRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_SolidRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_SolidRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_SolidRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_SolidRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_SolidRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_SolidRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_SolidRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_SolidRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_ChildRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_ChildRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_ChildRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_ChildRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_ChildRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_ChildRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_ChildRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_ChildRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_ChildRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_ChildRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_ChildRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_ChildRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_ChildRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_OccurrenceRefId:
    """
    @brief Compile-time typed wrapper around BRepGraph_RefId.

    Provides compile-time kind safety similarly to BRepGraph_NodeId::Typed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIdx: int) -> None: ...

    @overload
    def __init__(self, theRefId: BRepGraph_RefId) -> None:
        """Construct from an untyped reference id of the same kind."""

    @overload
    def __init__(self, theOther: BRepGraph_OccurrenceRefId) -> None: ...

    @staticmethod
    def Start() -> BRepGraph_OccurrenceRefId:
        """First valid id in a dense per-kind sequence."""

    @staticmethod
    def Invalid() -> BRepGraph_OccurrenceRefId:
        """Invalid sentinel id."""

    @overload
    def IsValid(self) -> bool: ...

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """
        True if this id points to an allocated slot within [0, theMaxCount).
        UINT32_MAX (invalid sentinel) always fails this check for any realistic count.
        """

    @staticmethod
    def FromRefId(theRefId: BRepGraph_RefId) -> BRepGraph_OccurrenceRefId: ...

    @overload
    def __eq__(self, theOther: BRepGraph_OccurrenceRefId) -> bool: ...

    @overload
    def __eq__(self, theOther: BRepGraph_RefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_OccurrenceRefId) -> bool: ...

    @overload
    def __ne__(self, theOther: BRepGraph_RefId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_OccurrenceRefId) -> bool: ...

    def __le__(self, theOther: BRepGraph_OccurrenceRefId) -> bool: ...

    def __gt__(self, theOther: BRepGraph_OccurrenceRefId) -> bool: ...

    def __ge__(self, theOther: BRepGraph_OccurrenceRefId) -> bool: ...

    def __add__(self, theOffset: int) -> BRepGraph_OccurrenceRefId:
        """Advance by offset."""

    def __sub__(self, theOffset: int) -> BRepGraph_OccurrenceRefId:
        """Retreat by offset."""

    def IsRemoved(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has been soft-removed in the given graph.
        """

    def IsOwned(self, theGraph: BRepGraph) -> bool:
        """
        Return true if this reference entry has an active owner in the given graph.
        """

    def __hash__(self) -> int: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class BRepGraph_RefUID:
    """
    Unique reference-entry identifier within a BRepGraph.

    Identity = (RefKind, Counter). Counter 0 is an invalid sentinel.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theKind: BRepGraph_RefId.Kind, theCounter: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefUID) -> None: ...

    @staticmethod
    def Invalid() -> BRepGraph_RefUID: ...

    def IsValid(self) -> bool:
        """True if this UID has a valid kind and a non-zero counter."""

    def HashValue(self) -> int: ...

    def __eq__(self, arg: BRepGraph_RefUID, /) -> bool: ...

    def __ne__(self, arg: BRepGraph_RefUID, /) -> bool: ...

    def __lt__(self, arg: BRepGraph_RefUID, /) -> bool: ...

    def __hash__(self) -> int: ...

    @property
    def Kind(self) -> BRepGraph_RefId.Kind: ...

    @Kind.setter
    def Kind(self, arg: BRepGraph_RefId.Kind, /) -> None: ...

    @property
    def Counter(self) -> int: ...

    @Counter.setter
    def Counter(self, arg: int, /) -> None: ...

class BRepGraph_UID:
    """
    Unique definition-node identifier within a BRepGraph.

    Identity = (Kind, Counter). Two nodes of different kinds may share a
    counter value but their UIDs are distinct.  Within one kind, counter
    values never repeat (monotonic, never resets).

    Trivially copyable, cheap to pass by value.
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid UID (counter = 0 is the invalid sentinel)."""

    @overload
    def __init__(self, theKind: BRepGraph_NodeId.Kind, theCounter: int) -> None:
        """
        Construct a valid UID.  Called internally by BRepGraphInc_Storage::AllocateNodeUID().
        @pre theCounter > 0 (counter = 0 is reserved as the invalid sentinel)
        """

    @overload
    def __init__(self, theOther: BRepGraph_UID) -> None: ...

    @staticmethod
    def Invalid() -> BRepGraph_UID:
        """Factory: returns an explicitly invalid UID."""

    def IsValid(self) -> bool:
        """True if this UID has a valid kind and a non-zero counter."""

    def IsTopology(self) -> bool: ...

    def IsAssembly(self) -> bool: ...

    def HashValue(self) -> int:
        """Hash value compatible with operator==."""

    def __eq__(self, arg: BRepGraph_UID, /) -> bool: ...

    def __ne__(self, arg: BRepGraph_UID, /) -> bool: ...

    def __lt__(self, arg: BRepGraph_UID, /) -> bool: ...

    def __hash__(self) -> int: ...

    @property
    def Kind(self) -> BRepGraph_NodeId.Kind: ...

    @Kind.setter
    def Kind(self, arg: BRepGraph_NodeId.Kind, /) -> None: ...

    @property
    def Counter(self) -> int: ...

    @Counter.setter
    def Counter(self, arg: int, /) -> None: ...

class BRepGraph_ItemId:
    """
    Generic BRepGraph item identifier covering definitions and references.
    Use-records are NOT included - they are session-local, not graph identity.
    """

    @overload
    def __init__(self) -> None:
        """Construct an invalid item id."""

    @overload
    def __init__(self, theNode: BRepGraph_NodeId) -> None:
        """Construct a node item id."""

    @overload
    def __init__(self, theRef: BRepGraph_RefId) -> None:
        """Construct a reference item id."""

    @overload
    def __init__(self, theOther: BRepGraph_ItemId) -> None: ...

    class Domain(enum.Enum):
        """Addressed graph item domain."""

        Node = 1

        Reference = 2

    def IsValid(self) -> bool:
        """Return true if this item addresses a graph object."""

    def ItemDomain(self) -> BRepGraph_ItemId.Domain:
        """Return the addressed domain."""

    def IsNode(self) -> bool:
        """Return true if this item addresses a definition node."""

    def IsReference(self) -> bool:
        """Return true if this item addresses a reference entry."""

    def NodeId(self) -> BRepGraph_NodeId:
        """Convert to node id. Returns invalid id for non-node items."""

    def RefId(self) -> BRepGraph_RefId:
        """Convert to reference id. Returns invalid id for non-reference items."""

    def NodeKind(self) -> BRepGraph_NodeId.Kind:
        """Return node kind. Valid only when IsNode() is true."""

    def RefKind(self) -> BRepGraph_RefId.Kind:
        """Return reference kind. Valid only when IsReference() is true."""

    def RawKind(self) -> int:
        """Return item kind encoded in its own domain enum space."""

    def Kind(self) -> int:
        """Return item kind encoded in its own domain enum space."""

    def Index(self) -> int:
        """Return item per-kind index."""

    def __eq__(self, arg: BRepGraph_ItemId, /) -> bool: ...

    def __ne__(self, arg: BRepGraph_ItemId, /) -> bool: ...

    def __hash__(self) -> int: ...

class BRepGraph:
    """
    @brief Topology-geometry graph over TopoDS / BRep.

    Stores B-Rep topology as flat entity vectors (incidence-table model) with
    integer cross-references, enabling cache-friendly traversal, relation-table
    parent navigation, and parallel face-level geometry extraction.

    Key design concepts:
    - **NodeId** (Kind + Index): lightweight typed address into per-kind vectors.
    - **UID** (Kind + Counter): persistent identity surviving compaction/reorder.
    - **RepId** (Kind + Index): separate geometry/mesh addressing (Surface,
    Curve3D, Curve2D, Triangulation, Polygon) decoupled from topology nodes.
    - **CoEdge**: half-edge entity owning PCurve data for each edge-face binding;
    seam edges use paired CoEdges with opposite Orientation (Parasolid convention).
    - **Lifecycle**: Shapes().Add() populates from TopoDS_Shape;
    Editor() is the single mutation entry point for both structural creation/removal
    (Add*, Remove*, Append*) and field-level RAII-scoped mutation (Mut*()) with
    automatic cache invalidation and upward SubtreeGen propagation.

    Per-occurrence data (orientation, location) lives on incidence refs.
    Definition types are aliases to BRepGraphInc entity structs.

    ## Grouped View API
    Related methods are grouped behind lightweight view objects.
    Include the corresponding header (e.g. BRepGraph_TopoView.hxx) to use.

    ## Thread safety
    Const query methods are safe for concurrent reads.
    Concurrent reads during active mutation still require external synchronization.
    Deferred invalidation (BRepGraph_DeferredScope) batches SubtreeGen propagation;
    concurrent Editor().Mut*() calls during deferred mode still require external
    serialization.
    Shapes().Add() is internally parallel when requested.

    ## UID persistence
    UIDs use monotonic counters (not vector indices), persisting across Compact()
    and node removal. Only BRepGraph::Clear() resets counters (new generation).
    See BRepGraph_UID.hxx for the serialization contract.

    ## Extension model
    Extend via BRepGraph_Layer (persistent metadata / observers) or
    BRepGraph_CacheRegistry (typed algorithm-computed transient cache services).
    Direct storage extension is not supported.

    ## ID systems
    Four ID types with different stability guarantees:
    - **NodeId** (Kind + per-kind Index): fast graph-local address. NOT stable across Compact().
    Use for in-graph traversal and short-lived algorithm temporaries.
    - **UID** (Kind + monotonic Counter): persistent identity surviving Compact() and node removal.
    Use for cross-session storage, history tracking, and external references.
    - **RefId** (Kind + per-kind Index): same stability as NodeId, but addresses reference entries
    (Shell->Solid binding, Face->Shell binding, CoEdge->Wire binding) rather than defs.
    - **RepId** (Kind + per-kind Index): addresses owner-scoped geometry/mesh representation slots
    (Surface, Curve3D, Curve2D, Triangulation, Polygon).

    ## Iterator guide
    Choose the iterator that matches your traversal need:
    - **BRepGraph_Iterator\\<NodeType\\>**: flat sequential scan of ALL definitions of one kind
    (e.g. every FaceDef, skipping removed). Use for bulk per-kind algorithms.
    - **BRepGraph_DefsIterator / BRepGraph_RefsIterator**: single-level typed children of one
    parent (e.g. active shells of one solid, coedges of one wire). Zero allocation.
    Use when you have a specific parent and need its direct children.
    - **BRepGraph_ChildExplorer**: depth-first downward walk from a root with accumulated
    location/orientation per step. Use when visiting descendants across multiple levels or
    when the global transform matters. Supports Recursive and DirectChildren modes.
    - **BRepGraph_ParentExplorer**: upward walk via relation tables from a starting node.
    Use when tracing which shells/solids/compounds contain a given face or edge.
    - **BRepGraph_RelatedIterator**: single-level semantic neighbors (adjacent faces, boundary
    edges, incident vertices). No structural descent; no location accumulation.
    """

    def __init__(self) -> None:
        """Default constructor. Creates an empty graph with default allocator."""

    class EditorView:
        """
        @brief Non-const view for programmatic graph construction and structural editing.

        The single mutation entry point for a BRepGraph instance. Provides:
        - Structural creation via entity-scoped nested Ops classes (VertexOps, EdgeOps,
        CoEdgeOps, WireOps, FaceOps, ShellOps, SolidOps, CompoundOps, CompSolidOps,
        ProductOps, GenOps) to create topology definition nodes (vertices, edges, wires,
        faces, shells, solids, compounds) and assembly nodes (products, occurrences)
        without an existing TopoDS_Shape.
        - Field-level RAII-scoped mutation via Mut*() guards (Edges().Mut, Faces().Mut,
        Products().Mut, Occurrences().Mut, Edges().Mut, Faces().Mut,
        etc.) with automatic cache invalidation and upward SubtreeGen propagation on
        guard destruction.
        - Incremental shape appending, soft-deletion of nodes, and deferred invalidation
        mode for batched structural edit loops under external serialization.
        Obtained via BRepGraph::Editor().

        Each Ops class is accessed via a non-const reference accessor:
        theGraph.Editor().Vertices().Add(...)
        theGraph.Editor().Edges().Add(...)
        theGraph.Editor().CoEdges().Add(edge, face, curve2d, first, last, ori)
        theGraph.Editor().Products().Add(shapeRoot, placement)
        theGraph.Editor().Gen().RemoveNode(...)

        Contract notes:
        - Add* methods return BRepGraph_NodeId() on invalid inputs and do not
        partially modify the graph; call IsValid() on the returned id to check
        success
        - invalid inputs include wrong kind, out-of-range ids, or removed referenced
        nodes unless a method documents stricter accepted-input rules
        - linking methods such as Shells().Add() and Solids().Add()
        return an invalid typed RefId on failure and otherwise keep ownership explicit
        in the reference layer
        - use Mut*() guards for scoped field mutation on existing active
        definitions, references, and representations
        """

        def __init__(self, theOther: BRepGraph.EditorView) -> None: ...

        class VertexOps:
            """@brief Vertex creation operations."""

            def __init__(self, theOther: BRepGraph.EditorView.VertexOps) -> None: ...

            def Add(self, thePoint: nanoocp.gp.gp_Pnt, theTolerance: float) -> BRepGraph_VertexId:
                """
                Add a vertex definition to the graph.
                @param[in] thePoint     3D coordinates
                @param[in] theTolerance vertex tolerance
                @return typed vertex definition identifier
                """

            def Mut(self, theVertex: BRepGraph_VertexId) -> BRepGraph_MutGuard__BRepGraphInc_VertexDef:
                """Return scoped mutable vertex definition guard."""

            def MutRef(self, theVertexRef: BRepGraph_VertexRefId) -> BRepGraph_MutGuard__BRepGraphInc_VertexRef:
                """Return scoped mutable vertex reference guard."""

            @overload
            def SetPoint(self, theVertex: BRepGraph_VertexId, thePoint: nanoocp.gp.gp_Pnt) -> None:
                """
                Set the 3D point of a vertex definition and fire immediate notification.
                @param[in] theVertex typed vertex definition identifier
                @param[in] thePoint  new 3D coordinates
                """

            @overload
            def SetPoint(self, theMut: BRepGraph_MutGuard__BRepGraphInc_VertexDef, thePoint: nanoocp.gp.gp_Pnt) -> None:
                """
                Set the 3D point of a vertex definition inside a batched mutation scope.
                Marks the guard dirty so the destructor fires a single notification.
                @param[in] theMut   active mutable vertex guard
                @param[in] thePoint new 3D coordinates
                """

            @overload
            def SetTolerance(self, theVertex: BRepGraph_VertexId, theTolerance: float) -> None:
                """Set the tolerance of a vertex definition."""

            @overload
            def SetTolerance(self, theMut: BRepGraph_MutGuard__BRepGraphInc_VertexDef, theTolerance: float) -> None:
                """Set the tolerance inside a batched mutation scope."""

            @overload
            def SetRefOrientation(self, theVertexRef: BRepGraph_VertexRefId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation of a vertex reference."""

            @overload
            def SetRefOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_VertexRef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation inside a batched mutation scope."""

            @overload
            def SetRefChildVertexId(self, theVertexRef: BRepGraph_VertexRefId, theVertex: BRepGraph_VertexId) -> None:
                """
                Rewire a vertex reference to a different vertex def (rebinds VertexToEdges if parent is
                Edge).
                """

            @overload
            def SetRefChildVertexId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_VertexRef, theVertex: BRepGraph_VertexId) -> None: ...

        class EdgeOps:
            """@brief Edge creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.EdgeOps) -> None: ...

            def Add(self, theStartVtx: BRepGraph_VertexId, theEndVtx: BRepGraph_VertexId, theCurve: nanoocp.Geom.Geom_Curve | None, theFirst: float, theLast: float, theTolerance: float) -> BRepGraph_EdgeId:
                """
                Add an edge definition to the graph.
                @param[in] theStartVtx  typed start vertex definition identifier
                @param[in] theEndVtx    typed end vertex definition identifier
                @param[in] theCurve     3D curve (may be null for degenerate edges)
                @param[in] theFirst     first curve parameter
                @param[in] theLast      last curve parameter
                @param[in] theTolerance edge tolerance
                @return typed edge definition identifier, or invalid if either referenced
                vertex id is out of range or removed
                """

            def Split(self, theEdgeEntity: BRepGraph_EdgeId, theSplitVertex: BRepGraph_VertexId, theSplitParam: float, theSubA: BRepGraph_EdgeId, theSubB: BRepGraph_EdgeId) -> None:
                """
                Split a single edge definition at a vertex and 3D-curve parameter.
                Creates two new EdgeDef slots, splits all PCurve nodes at the corresponding
                2D parameter, and updates every wire that contained the original edge.
                @param[in]  theEdgeEntity  edge to split (must not be degenerate)
                @param[in]  theSplitVertex vertex definition at the split point (already in graph)
                @param[in]  theSplitParam  parameter on the 3D curve at the split point
                @param[out] theSubA        sub-edge: StartVertex -> SplitVertex
                @param[out] theSubB        sub-edge: SplitVertex -> EndVertex
                """

            def RemoveVertex(self, theChildEdgeId: BRepGraph_EdgeId, theVertexRefId: BRepGraph_VertexRefId) -> bool:
                """
                Detach one exact edge-owned vertex ref from an edge definition.
                Supports only the persisted boundary slots (StartVertexRefId /
                EndVertexRefId). Supplemental direct-vertex usages are stored in
                BRepGraph_LayerTopoSupplement and are not removed through this API.
                @param[in] theChildEdgeId   edge definition identifier
                @param[in] theVertexRefId exact edge-owned vertex reference identifier
                @return true if the active edge-owned usage was removed
                """

            def ReplaceVertex(self, theChildEdgeId: BRepGraph_EdgeId, theOldVertexRefId: BRepGraph_VertexRefId, theNewChildVertexId: BRepGraph_VertexId) -> BRepGraph_VertexRefId:
                """
                Remap one edge-owned vertex reference to point at a different vertex
                definition, preserving the existing orientation and local location.
                Intended for boundary-vertex substitution without a full edge rebuild
                (e.g. stitching shared endpoints after a ShapeFix pass).
                @param[in] theChildEdgeId       edge owning the vertex reference
                @param[in] theOldVertexRefId  exact boundary vertex reference to remap
                @param[in] theNewChildVertexId  replacement vertex definition
                @return typed id of the newly created vertex reference, or invalid if
                any input was inactive or the old ref did not belong to this edge
                """

            def Mut(self, theEdge: BRepGraph_EdgeId) -> BRepGraph_MutGuard__BRepGraphInc_EdgeDef:
                """Return scoped mutable edge definition guard."""

            def Reverse(self, theEdge: BRepGraph_EdgeId) -> None:
                """
                Reverse the edge: swap StartVertexRefId and EndVertexRefId. Used by
                healing/sewing when a caller wants the edge's boundary order flipped.
                Does not alter the parametric range (callers needing reparametrization
                should follow up with SetParamRange).
                @param[in] theEdge edge definition identifier
                """

            @overload
            def SetTolerance(self, theEdge: BRepGraph_EdgeId, theTolerance: float) -> None:
                """
                Set the tolerance of an edge definition and fire immediate notification.
                @param[in] theEdge      typed edge definition identifier
                @param[in] theTolerance new tolerance value
                """

            @overload
            def SetTolerance(self, theMut: BRepGraph_MutGuard__BRepGraphInc_EdgeDef, theTolerance: float) -> None:
                """
                Set the tolerance of an edge definition inside a batched mutation scope.
                @param[in] theMut       active mutable edge guard
                @param[in] theTolerance new tolerance value
                """

            @overload
            def SetParamRange(self, theEdge: BRepGraph_EdgeId, theFirst: float, theLast: float) -> None:
                """Set the parametric range of an edge definition."""

            @overload
            def SetParamRange(self, theMut: BRepGraph_MutGuard__BRepGraphInc_EdgeDef, theFirst: float, theLast: float) -> None: ...

            def SetCurve(self, theEdge: BRepGraph_EdgeId, theCurve: nanoocp.Geom.Geom_Curve | None, theFirst: float, theLast: float) -> None:
                """
                Set the 3D curve on an edge. Creates an owned EdgeCurve3DRep record
                and an associated Curve3DRep for edge geometry access.
                @param[in] theEdge  edge definition identifier
                @param[in] theCurve 3D curve geometry (must not be null)
                @param[in] theFirst first curve parameter
                @param[in] theLast  last curve parameter
                """

            def ClearCurve(self, theEdge: BRepGraph_EdgeId) -> None:
                """
                Clear the 3D curve on an edge. Removes the owned use record binding.
                @param[in] theEdge edge definition identifier
                """

            def SetPersistentPolygon3D(self, theEdge: BRepGraph_EdgeId, thePolygon: nanoocp.Poly.Poly_Polygon3D | None) -> None:
                """
                Set the persistent 3D polygon on an edge. Creates an owned EdgePolygon3DRep record.
                @param[in] theEdge    edge definition identifier
                @param[in] thePolygon 3D polygon (must not be null)
                """

            def ClearPersistentPolygon3D(self, theEdge: BRepGraph_EdgeId) -> None:
                """
                Clear the persistent 3D polygon on an edge.
                @param[in] theEdge edge definition identifier
                """

            @overload
            def SetStartVertexRefId(self, theEdge: BRepGraph_EdgeId, theVertexRef: BRepGraph_VertexRefId) -> None:
                """Set the start vertex-ref id and rebind the vertex-to-edge relation."""

            @overload
            def SetStartVertexRefId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_EdgeDef, theVertexRef: BRepGraph_VertexRefId) -> None: ...

            @overload
            def SetEndVertexRefId(self, theEdge: BRepGraph_EdgeId, theVertexRef: BRepGraph_VertexRefId) -> None:
                """Set the end vertex-ref id and rebind the vertex-to-edge relation."""

            @overload
            def SetEndVertexRefId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_EdgeDef, theVertexRef: BRepGraph_VertexRefId) -> None: ...

        class CoEdgeOps:
            """@brief CoEdge and PCurve operations."""

            def __init__(self, theOther: BRepGraph.EditorView.CoEdgeOps) -> None: ...

            @overload
            def SetPCurve(self, theCoEdge: BRepGraph_CoEdgeId, theCurve2d: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
                """
                Assign or clear the PCurve bound to an existing coedge.
                Creates a new Curve2DRep for non-null curves and stores its id on the coedge.
                Pass a null handle to clear the stored PCurve binding.
                @param[in] theCoEdge  typed coedge identifier to update
                @param[in] theCurve2d new 2D curve geometry, or null to clear
                """

            @overload
            def SetPCurve(self, theCoEdge: BRepGraph_CoEdgeId, theCurve2d: nanoocp.Geom2d.Geom2d_Curve | None, theFirst: float, theLast: float) -> None:
                """
                Set the PCurve on a coedge. Creates an owned CoEdgeCurve2DRep record.
                @param[in] theCoEdge  coedge definition identifier
                @param[in] theCurve2d 2D curve geometry (must not be null)
                @param[in] theFirst   first curve parameter
                @param[in] theLast    last curve parameter
                """

            @overload
            def Add(self, theEdge: BRepGraph_EdgeId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> BRepGraph_CoEdgeId:
                """
                Create a new CoEdge entity linking an edge with an orientation.
                The CoEdge is free-floating (no parent wire); bind it to a wire
                via WireOps::Add().
                @param[in] theEdge       typed edge definition identifier
                @param[in] theOrientation orientation of the edge in the wire
                @return typed coedge identifier, or invalid if the edge is invalid
                """

            @overload
            def Add(self, theEdgeEntity: BRepGraph_EdgeId, theFaceEntity: BRepGraph_FaceId, theCurve2d: nanoocp.Geom2d.Geom2d_Curve | None, theFirst: float, theLast: float, theEdgeOrientation: nanoocp.BRepGraphInc.ParityOrientation = ...) -> BRepGraph_CoEdgeId:
                """
                Create a new CoEdge entity with a PCurve for a given edge-face pair.
                Creates a new CoEdge entity with Curve2DRep and updates relation tables.
                This always appends a new CoEdge entry for the edge-face pair; callers
                should avoid duplicate creation unless multiple bindings are intentional
                for the modeled topology.
                For editing an already identified CoEdge inside a larger
                mutation sequence, use CoEdges().SetPCurve().
                @param[in] theEdgeEntity      typed edge definition identifier
                @param[in] theFaceEntity      typed face definition identifier
                @param[in] theCurve2d         2D curve geometry
                @param[in] theFirst           first curve parameter
                @param[in] theLast            last curve parameter
                @param[in] theEdgeOrientation edge orientation on the face
                @return typed coedge identifier, or invalid if inputs are not active
                """

            def Mut(self, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef:
                """Return scoped mutable coedge definition guard."""

            @overload
            def SetParamRange(self, theCoEdge: BRepGraph_CoEdgeId, theFirst: float, theLast: float) -> None:
                """
                Set the parametric range of a coedge definition and fire immediate notification.
                @param[in] theCoEdge  typed coedge definition identifier
                @param[in] theFirst   new first parameter value
                @param[in] theLast    new last parameter value
                """

            @overload
            def SetParamRange(self, theMut: BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef, theFirst: float, theLast: float) -> None:
                """
                Set the parametric range of a coedge definition inside a batched mutation scope.
                @param[in] theMut   active mutable coedge guard
                @param[in] theFirst new first parameter value
                @param[in] theLast  new last parameter value
                """

            @overload
            def SetOrientation(self, theCoEdge: BRepGraph_CoEdgeId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation of a coedge definition."""

            @overload
            def SetOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None: ...

            def ClearPCurve(self, theCoEdge: BRepGraph_CoEdgeId) -> None:
                """
                Clear the PCurve on a coedge.
                @param[in] theCoEdge coedge definition identifier
                """

            def SetPersistentPolygon2D(self, theCoEdge: BRepGraph_CoEdgeId, thePolygon: nanoocp.Poly.Poly_Polygon2D | None) -> None:
                """
                Set the persistent 2D polygon on a coedge.
                @param[in] theCoEdge  coedge definition identifier
                @param[in] thePolygon 2D polygon (must not be null)
                """

            def SetPersistentPolygonOnTri(self, theCoEdge: BRepGraph_CoEdgeId, thePolygon: nanoocp.Poly.Poly_PolygonOnTriangulation | None) -> None:
                """
                Set the persistent polygon-on-triangulation on a coedge.
                The triangulation is resolved via CoEdgeDef.FaceId -> FaceDef.TriangulationRepId.
                @param[in] theCoEdge       coedge definition identifier
                @param[in] thePolygon      polygon-on-triangulation (must not be null)
                """

            @overload
            def ResetPCurveBinding(self, theCoEdge: BRepGraph_CoEdgeId) -> None:
                """
                Drop face-bound parametric representation (PCurve, param range, continuity, UVs)
                while keeping structural links - used when the owning face is removed.
                """

            @overload
            def ResetPCurveBinding(self, theMut: BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef) -> None: ...

            @overload
            def SetChildEdgeId(self, theCoEdge: BRepGraph_CoEdgeId, theEdge: BRepGraph_EdgeId) -> None:
                """
                Rewire a coedge to a different child edge and rebind edge parent/use relations.
                """

            @overload
            def SetChildEdgeId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef, theEdge: BRepGraph_EdgeId) -> None: ...

            @overload
            def SetFaceId(self, theCoEdge: BRepGraph_CoEdgeId, theFace: BRepGraph_FaceId) -> None:
                """
                Rewire a coedge to a different owning face and rebind edge-to-face relations.
                """

            @overload
            def SetFaceId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef, theFace: BRepGraph_FaceId) -> None: ...

        class WireOps:
            """@brief Wire creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.WireOps) -> None: ...

            class CoEdgeOrderStatus(enum.Enum):
                """Status returned by wire coedge-order prechecks."""

                Ready = 0

                Reordered = 1

                AlreadyCurrent = 2

                AlreadyContained = 3

                Empty = 4

                InvalidWire = 5

                SizeMismatch = 6

                DuplicateCoEdge = 7

                InvalidCoEdge = 8

                CoEdgeAlreadyBound = 9

                CoEdgeNotOwnedByWire = 10

                NotPermutation = 11

                Disconnected = 12

            class ReplaceEdgeStatus(enum.Enum):
                """Status returned by wire edge-replacement prechecks."""

                Ready = 0

                AlreadyCurrent = 1

                InvalidWire = 2

                InvalidOldEdge = 3

                InvalidNewEdge = 4

                Disconnected = 5

            @overload
            def CheckCoEdgeOrder(self, theCoEdgeIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_CoEdgeId]) -> BRepGraph.EditorView.WireOps.CoEdgeOrderStatus:
                """
                Precheck free-floating CoEdges for WireOps::Add().
                @param[in] theCoEdgeIds candidate coedge identifiers
                @return status describing whether the input can form a wire
                """

            @overload
            def CheckCoEdgeOrder(self, theWire: BRepGraph_WireId, theCoEdgeIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_CoEdgeId]) -> BRepGraph.EditorView.WireOps.CoEdgeOrderStatus:
                """
                Precheck owned CoEdges for WireOps::SetCoEdgeOrder().
                @param[in] theWire      wire definition identifier
                @param[in] theCoEdgeIds candidate coedge identifiers
                @return status describing whether the input can replace the stored order
                """

            def CheckAppendCoEdge(self, theWire: BRepGraph_WireId, theCoEdgeId: BRepGraph_CoEdgeId) -> BRepGraph.EditorView.WireOps.CoEdgeOrderStatus:
                """
                Precheck appending a free CoEdge to an existing wire.
                @param[in] theWire     wire definition identifier
                @param[in] theCoEdgeId free coedge candidate
                @return status describing whether the append can preserve connected order
                """

            def CheckReplaceEdge(self, theWire: BRepGraph_WireId, theOldEdge: BRepGraph_EdgeId, theNewEdge: BRepGraph_EdgeId, theReversed: bool) -> BRepGraph.EditorView.WireOps.ReplaceEdgeStatus:
                """
                Precheck replacing one edge by another in an existing wire.
                @param[in] theWire    wire definition identifier
                @param[in] theOldEdge edge currently used by one or more wire coedges
                @param[in] theNewEdge replacement edge
                @param[in] theReversed if true, replacement coedge orientation is reversed
                @return status describing whether replacement preserves connected order
                """

            def Add(self, theCoEdgeIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_CoEdgeId]) -> BRepGraph_WireId:
                """
                Add a wire definition from pre-created CoEdges.
                Each CoEdge must be free-floating (no parent wire yet).
                The method binds all CoEdges to the new wire and updates relation tables.
                @param[in] theCoEdgeIds ordered coedge identifiers
                @return typed wire definition identifier, or invalid if any referenced
                coedge is invalid or already bound to a wire
                """

            def ReplaceEdge(self, theChildWireId: BRepGraph_WireId, theOldEdgeEntity: BRepGraph_EdgeId, theNewEdgeEntity: BRepGraph_EdgeId, theReversed: bool) -> None:
                """
                Replace one edge with another in a wire definition.
                Updates the CoEdge's EdgeIdx to point to the new edge, adjusts orientation
                if theReversed, and incrementally updates relation tables.
                @param[in] theChildWireId     wire definition identifier
                @param[in] theOldEdgeEntity edge to replace
                @param[in] theNewEdgeEntity replacement edge
                @param[in] theReversed      if true, reverse the orientation of the replacement
                """

            def RemoveCoEdge(self, theChildWireId: BRepGraph_WireId, theCoEdgeId: BRepGraph_CoEdgeId) -> bool:
                """
                Detach one exact coedge entry from a wire definition.
                Use BRepGraph_CoEdgesOfWire::CurrentId() when removing from a wire
                iterator. The method removes the exact ordered coedge entry, updates
                relation tables, and prunes the CoEdge node when it has no other active
                usages.
                @param[in] theChildWireId wire definition identifier
                @param[in] theCoEdgeId  exact wire-owned coedge identifier
                @return true if the active wire-owned usage was removed
                """

            def Reverse(self, theWire: BRepGraph_WireId) -> None:
                """
                Reverse the wire: flip the order of the wire's CoEdgeIds and flip each
                owned CoEdge's orientation. Used by healing/sewing to invert a loop.
                @param[in] theWire wire definition identifier
                """

            def SetCoEdgeOrder(self, theWire: BRepGraph_WireId, theCoEdgeIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_CoEdgeId]) -> bool:
                """
                Replace the ordered CoEdge relation vector with a permutation of its
                current content.
                @param[in] theWire       wire definition identifier
                @param[in] theCoEdgeIds  new ordered CoEdge identifiers
                @return true if the order was accepted and applied
                """

            def Mut(self, theWire: BRepGraph_WireId) -> BRepGraph_MutGuard__BRepGraphInc_WireDef:
                """Return scoped mutable wire definition guard."""

            def MutRef(self, theWireRef: BRepGraph_WireRefId) -> BRepGraph_MutGuard__BRepGraphInc_WireRef:
                """Return scoped mutable wire reference guard."""

            @overload
            def SetRefOrientation(self, theWireRef: BRepGraph_WireRefId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation of a wire reference."""

            @overload
            def SetRefOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_WireRef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None: ...

            @overload
            def SetRefChildWireId(self, theWireRef: BRepGraph_WireRefId, theWire: BRepGraph_WireId) -> None:
                """
                Rewire a wire reference to a different wire def (rebinds WireToFaces if parent is Face).
                """

            @overload
            def SetRefChildWireId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_WireRef, theWire: BRepGraph_WireId) -> None: ...

        class FaceOps:
            """@brief Face creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.FaceOps) -> None: ...

            def Add(self, theSurface: nanoocp.Geom.Geom_Surface | None, theOuterWire: BRepGraph_WireId, theInnerWires: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_WireId], theTolerance: float) -> BRepGraph_FaceId:
                """
                Add a face definition to the graph.
                @param[in] theSurface    surface geometry
                @param[in] theOuterWire  typed outer wire definition identifier
                @param[in] theInnerWires typed inner wire definition identifiers
                @param[in] theTolerance  face tolerance
                @return typed face definition identifier, or invalid if any referenced
                wire id is out of range or removed
                """

            def Append(self, theFaceEntity: BRepGraph_FaceId, theWireEntity: BRepGraph_WireId, theOri: nanoocp.BRepGraphInc.ParityOrientation = ...) -> BRepGraph_WireRefId:
                """
                Append a wire usage to an existing face definition.
                @param[in] theFaceEntity typed face definition identifier
                @param[in] theWireEntity typed wire definition identifier
                @param[in] theOri        orientation of the wire usage on the face
                @return typed wire reference identifier, or invalid if inputs are not
                active
                """

            def RemoveWire(self, theFaceId: BRepGraph_FaceId, theWireRefId: BRepGraph_WireRefId) -> bool:
                """
                Detach one exact wire ref from a face definition.
                Use BRepGraph_RefsWireOfFace::CurrentId() when removing from a face
                iterator. The method removes the exact WireRef entry, erases it from
                the face's ordered ref sequence, updates relation tables, and prunes the
                Wire subtree when it has no other active usages.
                @param[in] theFaceId face definition identifier
                @param[in] theWireRefId exact face-owned wire reference identifier
                @return true if the active face-owned usage was removed
                """

            def Mut(self, theFace: BRepGraph_FaceId) -> BRepGraph_MutGuard__BRepGraphInc_FaceDef:
                """Return scoped mutable face definition guard."""

            def MutRef(self, theFaceRef: BRepGraph_FaceRefId) -> BRepGraph_MutGuard__BRepGraphInc_FaceRef:
                """Return scoped mutable face reference guard."""

            @overload
            def SetTolerance(self, theFace: BRepGraph_FaceId, theTolerance: float) -> None:
                """
                Set the tolerance of a face definition and fire immediate notification.
                @param[in] theFace      typed face definition identifier
                @param[in] theTolerance new tolerance value
                """

            @overload
            def SetTolerance(self, theMut: BRepGraph_MutGuard__BRepGraphInc_FaceDef, theTolerance: float) -> None:
                """
                Set the tolerance of a face definition inside a batched mutation scope.
                @param[in] theMut       active mutable face guard
                @param[in] theTolerance new tolerance value
                """

            def SetSurface(self, theFace: BRepGraph_FaceId, theSurface: nanoocp.Geom.Geom_Surface | None) -> None:
                """
                Set the surface on a face. Creates an owned FaceSurfaceRep record
                and an associated SurfaceRep for face geometry access.
                @param[in] theFace    face definition identifier
                @param[in] theSurface surface geometry (must not be null)
                """

            def ClearSurface(self, theFace: BRepGraph_FaceId) -> None:
                """
                Clear the surface on a face. Removes the owned use record binding.
                @param[in] theFace face definition identifier
                """

            def SetPersistentTriangulation(self, theFace: BRepGraph_FaceId, theTriangulation: nanoocp.Poly.Poly_Triangulation | None) -> None:
                """
                Set the persistent triangulation on a face. Creates an owned FaceTriangulationRep record.
                Also creates a TriangulationRep for backward compatibility.
                @param[in] theFace         face definition identifier
                @param[in] theTriangulation triangulation mesh (must not be null)
                """

            def ClearPersistentTriangulation(self, theFace: BRepGraph_FaceId) -> None:
                """
                Clear the persistent triangulation on a face.
                @param[in] theFace face definition identifier
                """

            @overload
            def SetRefOrientation(self, theFaceRef: BRepGraph_FaceRefId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """
                Set the orientation of a face reference and fire immediate notification.
                @param[in] theFaceRef     typed face reference identifier
                @param[in] theOrientation new orientation value
                """

            @overload
            def SetRefOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_FaceRef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """
                Set the orientation of a face reference inside a batched mutation scope.
                @param[in] theMut         active mutable face reference guard
                @param[in] theOrientation new orientation value
                """

            @overload
            def SetRefFaceId(self, theFaceRef: BRepGraph_FaceRefId, theFace: BRepGraph_FaceId) -> None:
                """
                Rewire a face reference to a different face def (rebinds FaceToShells if parent is Shell).
                """

            @overload
            def SetRefFaceId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_FaceRef, theFace: BRepGraph_FaceId) -> None: ...

        class ShellOps:
            """@brief Shell creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.ShellOps) -> None: ...

            def Add(self) -> BRepGraph_ShellId:
                """
                Add an empty shell definition to the graph.
                @return typed shell definition identifier
                """

            @overload
            def Append(self, theShellEntity: BRepGraph_ShellId, theFaceEntity: BRepGraph_FaceId, theOri: nanoocp.BRepGraphInc.ParityOrientation = ...) -> BRepGraph_FaceRefId:
                """
                Append a face to a shell.
                Appends FaceRef and stores its FaceRefId in shell FaceRefIds.
                @param[in] theShellEntity typed shell definition identifier
                @param[in] theFaceEntity  typed face definition identifier
                @param[in] theOri         orientation of the face in the shell
                @return typed face reference identifier, or invalid if inputs are not active
                """

            @overload
            def Append(self, theShellEntity: BRepGraph_ShellId, theFaceIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_FaceId], theOrientations: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraphInc.ParityOrientation] = ...) -> nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_FaceRefId]:
                """
                Batch-append multiple faces to a shell.
                Two-pass: validates all inputs first, then links all.
                @param[in] theShellEntity typed shell definition identifier
                @param[in] theFaceIds     face definition identifiers to append
                @param[in] theOrientations optional parity orientations (empty = all FORWARD)
                @return array of created face reference ids, empty on validation failure
                """

            def RemoveFace(self, theChildShellId: BRepGraph_ShellId, theFaceRefId: BRepGraph_FaceRefId) -> bool:
                """
                Detach one exact face ref from a shell definition.
                Use BRepGraph_RefsFaceOfShell::CurrentId() when removing from a shell
                iterator. The method removes the exact FaceRef entry, erases it from the
                shell's ordered ref sequence, updates relation tables, and prunes the
                Face subtree when it has no other active usages.
                @param[in] theChildShellId shell definition identifier
                @param[in] theFaceRefId  exact shell-owned face reference identifier
                @return true if the active shell-owned usage was removed
                """

            def RemoveFaces(self, theShellId: BRepGraph_ShellId, theFaceRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_FaceRefId]) -> bool:
                """
                Batch-remove multiple face refs from a shell definition.
                All-or-nothing: validates all inputs first, then removes all.
                @param[in] theShellId   shell definition identifier
                @param[in] theFaceRefs  face reference identifiers to remove
                @return true if all refs were successfully removed
                """

            def Mut(self, theShell: BRepGraph_ShellId) -> BRepGraph_MutGuard__BRepGraphInc_ShellDef:
                """Return scoped mutable shell definition guard."""

            def MutRef(self, theShellRef: BRepGraph_ShellRefId) -> BRepGraph_MutGuard__BRepGraphInc_ShellRef:
                """Return scoped mutable shell reference guard."""

            @overload
            def SetRefOrientation(self, theShellRef: BRepGraph_ShellRefId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation of a shell reference."""

            @overload
            def SetRefOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_ShellRef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation inside a batched mutation scope."""

            @overload
            def SetRefChildShellId(self, theShellRef: BRepGraph_ShellRefId, theShell: BRepGraph_ShellId) -> None:
                """
                Rewire a shell reference to a different shell def (rebinds ShellToSolid if parent is Solid).
                """

            @overload
            def SetRefChildShellId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_ShellRef, theShell: BRepGraph_ShellId) -> None: ...

        class SolidOps:
            """@brief Solid creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.SolidOps) -> None: ...

            def Add(self) -> BRepGraph_SolidId:
                """
                Add an empty solid definition to the graph.
                @return typed solid definition identifier
                """

            @overload
            def Append(self, theSolidEntity: BRepGraph_SolidId, theShellEntity: BRepGraph_ShellId, theOri: nanoocp.BRepGraphInc.ParityOrientation = ...) -> BRepGraph_ShellRefId:
                """
                Append a shell to a solid.
                Appends ShellRef and stores its ShellRefId in solid ShellRefIds.
                @param[in] theSolidEntity typed solid definition identifier
                @param[in] theShellEntity typed shell definition identifier
                @param[in] theOri         orientation of the shell in the solid
                @return typed shell reference identifier, or invalid if inputs are not active
                """

            @overload
            def Append(self, theSolidEntity: BRepGraph_SolidId, theShellIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ShellId], theOrientations: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraphInc.ParityOrientation] = ...) -> nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ShellRefId]:
                """
                Batch-append multiple shells to a solid.
                Two-pass: validates all inputs first, then links all.
                @param[in] theSolidEntity typed solid definition identifier
                @param[in] theShellIds    shell definition identifiers to append
                @param[in] theOrientations optional parity orientations (empty = all FORWARD)
                @return array of created shell reference ids, empty on validation failure
                """

            def RemoveShell(self, theChildSolidId: BRepGraph_SolidId, theShellRefId: BRepGraph_ShellRefId) -> bool:
                """
                Detach one exact shell ref from a solid definition.
                Use BRepGraph_RefsShellOfSolid::CurrentId() when removing from a solid
                iterator. The method removes the exact ShellRef entry, erases it from the
                solid's ordered ref sequence, updates relation tables, and prunes the
                Shell subtree when it has no other active usages.
                @param[in] theChildSolidId solid definition identifier
                @param[in] theShellRefId exact solid-owned shell reference identifier
                @return true if the active solid-owned usage was removed
                """

            def RemoveShells(self, theSolidId: BRepGraph_SolidId, theShellRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ShellRefId]) -> bool:
                """
                Batch-remove multiple shell refs from a solid definition.
                All-or-nothing: validates all inputs first, then removes all.
                @param[in] theSolidId    solid definition identifier
                @param[in] theShellRefs  shell reference identifiers to remove
                @return true if all refs were successfully removed
                """

            def Mut(self, theSolid: BRepGraph_SolidId) -> BRepGraph_MutGuard__BRepGraphInc_SolidDef:
                """Return scoped mutable solid definition guard."""

            def MutRef(self, theSolidRef: BRepGraph_SolidRefId) -> BRepGraph_MutGuard__BRepGraphInc_SolidRef:
                """Return scoped mutable solid reference guard."""

            @overload
            def SetRefOrientation(self, theSolidRef: BRepGraph_SolidRefId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation of a solid reference."""

            @overload
            def SetRefOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_SolidRef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation inside a batched mutation scope."""

            @overload
            def SetRefChildSolidId(self, theSolidRef: BRepGraph_SolidRefId, theSolid: BRepGraph_SolidId) -> None:
                """
                Rewire a solid reference to a different solid def (rebinds SolidToCompSolid if parent is
                CompSolid).
                """

            @overload
            def SetRefChildSolidId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_SolidRef, theSolid: BRepGraph_SolidId) -> None: ...

        class CompoundOps:
            """@brief Compound creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.CompoundOps) -> None: ...

            def Add(self, theChildEntities: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId]) -> BRepGraph_CompoundId:
                """
                Add a compound entity with ordered child usages.
                @param[in] theChildEntities child node identifiers
                @return typed compound definition identifier
                """

            @overload
            def Append(self, theCompoundEntity: BRepGraph_CompoundId, theChildEntity: BRepGraph_NodeId, theOri: nanoocp.BRepGraphInc.ParityOrientation = ...) -> BRepGraph_ChildRefId:
                """
                Append a single child to an existing compound definition.
                @param[in] theCompoundEntity typed compound definition identifier
                @param[in] theChildEntity    typed child topology definition identifier
                @param[in] theOri            orientation of the child in the compound
                @return typed child reference identifier, or invalid if inputs are not active
                """

            @overload
            def Append(self, theCompoundEntity: BRepGraph_CompoundId, theChildIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theOrientations: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraphInc.ParityOrientation] = ...) -> nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ChildRefId]:
                """
                Batch-append multiple children to an existing compound definition.
                Two-pass: validates all inputs first, then links all.
                @param[in] theCompoundEntity typed compound definition identifier
                @param[in] theChildIds       child node identifiers to append
                @param[in] theOrientations   optional parity orientations (empty = all FORWARD)
                @return array of created child reference ids, empty on validation failure
                """

            def RemoveChild(self, theCompoundDefId: BRepGraph_CompoundId, theChildRefId: BRepGraph_ChildRefId) -> bool:
                """
                Detach one exact child ref from a compound definition.
                Use BRepGraph_RefsChildOfParent::CurrentId() when removing from a compound
                iterator. The method removes the exact ChildRef entry, erases it from the
                compound's ordered ref sequence, updates relation tables, and prunes the
                child subtree when it has no other active usages.
                @param[in] theCompoundDefId compound definition identifier
                @param[in] theChildRefId    exact compound-owned child reference identifier
                @return true if the active compound-owned usage was removed
                """

            def RemoveChildren(self, theCompoundId: BRepGraph_CompoundId, theChildRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ChildRefId]) -> bool:
                """
                Batch-remove multiple child refs from a compound definition.
                All-or-nothing: validates all inputs first, then removes all.
                @param[in] theCompoundId  compound definition identifier
                @param[in] theChildRefs   child reference identifiers to remove
                @return true if all refs were successfully removed
                """

            def Mut(self, theCompound: BRepGraph_CompoundId) -> BRepGraph_MutGuard__BRepGraphInc_CompoundDef:
                """Return scoped mutable compound definition guard."""

            def ReplaceChild(self, theChildRef: BRepGraph_ChildRefId, theNewChild: BRepGraph_NodeId) -> None:
                """
                Replace the child node of an existing child reference in a compound.
                Delegates to Gen().SetChildRefChildNodeId().
                @param[in] theChildRef typed child reference identifier
                @param[in] theNewChild new child node identifier
                """

        class CompSolidOps:
            """@brief CompSolid creation and editing operations."""

            def __init__(self, theOther: BRepGraph.EditorView.CompSolidOps) -> None: ...

            def Add(self, theSolidEntities: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_SolidId]) -> BRepGraph_CompSolidId:
                """
                Add a compsolid entity with ordered solid usages.
                @param[in] theSolidEntities typed child solid identifiers
                @return typed compsolid definition identifier
                """

            @overload
            def Append(self, theCompSolidEntity: BRepGraph_CompSolidId, theSolidEntity: BRepGraph_SolidId, theOri: nanoocp.BRepGraphInc.ParityOrientation = ...) -> BRepGraph_SolidRefId:
                """
                Append a single solid to an existing compsolid definition.
                @param[in] theCompSolidEntity typed compsolid definition identifier
                @param[in] theSolidEntity     typed solid definition identifier
                @param[in] theOri             orientation of the solid in the compsolid
                @return typed solid reference identifier, or invalid if inputs are not active
                """

            @overload
            def Append(self, theCompSolidEntity: BRepGraph_CompSolidId, theSolidIds: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_SolidId], theOrientations: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraphInc.ParityOrientation] = ...) -> nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_SolidRefId]:
                """
                Batch-append multiple solids to an existing compsolid definition.
                Two-pass: validates all inputs first, then links all.
                @param[in] theCompSolidEntity typed compsolid definition identifier
                @param[in] theSolidIds        solid definition identifiers to append
                @param[in] theOrientations    optional parity orientations (empty = all FORWARD)
                @return array of created solid reference ids, empty on validation failure
                """

            def RemoveSolid(self, theCompChildSolidId: BRepGraph_CompSolidId, theSolidRefId: BRepGraph_SolidRefId) -> bool:
                """
                Detach one exact solid ref from a compsolid definition.
                Use BRepGraph_RefsSolidOfCompSolid::CurrentId() when removing from a
                compsolid iterator. The method removes the exact SolidRef entry, erases it
                from the compsolid's ordered ref sequence, updates relation tables, and
                prunes the Solid subtree when it has no other active usages.
                @param[in] theCompChildSolidId compsolid definition identifier
                @param[in] theSolidRefId     exact compsolid-owned solid reference identifier
                @return true if the active compsolid-owned usage was removed
                """

            def RemoveSolids(self, theCompSolidId: BRepGraph_CompSolidId, theSolidRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_SolidRefId]) -> bool:
                """
                Batch-remove multiple solid refs from a compsolid definition.
                All-or-nothing: validates all inputs first, then removes all.
                @param[in] theCompSolidId compsolid definition identifier
                @param[in] theSolidRefs   solid reference identifiers to remove
                @return true if all refs were successfully removed
                """

            def Mut(self, theCompSolid: BRepGraph_CompSolidId) -> BRepGraph_MutGuard__BRepGraphInc_CompSolidDef:
                """Return scoped mutable comp-solid definition guard."""

            def ReplaceSolid(self, theSolidRef: BRepGraph_SolidRefId, theNewSolid: BRepGraph_SolidId) -> None:
                """
                Replace the solid of an existing solid reference in a compsolid.
                Delegates to Solids().SetRefChildSolidId().
                @param[in] theSolidRef typed solid reference identifier
                @param[in] theNewSolid new solid definition identifier
                """

        class ProductOps:
            """
            @brief Product and assembly low-level reconstruction primitives.
            Wire two existing entities together; for shape ingestion use BRepGraph::ShapesView::Add().
            """

            def __init__(self, theOther: BRepGraph.EditorView.ProductOps) -> None: ...

            @overload
            def Add(self, theShapeRoot: BRepGraph_NodeId, thePlacement: nanoocp.TopLoc.TopLoc_Location = ...) -> BRepGraph_ProductId:
                """
                Create a Product wrapping an existing topology root via an Occurrence.
                The product is NOT added to document roots; call AppendDocumentRoot() explicitly
                when this Product is a document root.
                @param[in] theShapeRoot root topology NodeId for the part
                @param[in] thePlacement local placement stored on the root OccurrenceRef
                @return typed product definition identifier, or invalid if the root is
                not an active topology definition node
                """

            @overload
            def Add(self) -> BRepGraph_ProductId:
                """
                Create an empty Product with no direct shape root; can later own child occurrences.
                The product is NOT added to document roots; call AppendDocumentRoot() explicitly
                when this Product is a document root.
                @return typed product definition identifier
                """

            def AppendDocumentRoot(self, theProductId: BRepGraph_ProductId) -> None:
                """Add an active Product to document roots if it is not already listed."""

            @overload
            def Append(self, theParentProduct: BRepGraph_ProductId, theReferencedProduct: BRepGraph_ProductId, thePlacement: nanoocp.TopLoc.TopLoc_Location, theParentOccurrence: BRepGraph_OccurrenceId = ..., theOutOccurrenceRefId: BRepGraph_OccurrenceRefId = None) -> BRepGraph_OccurrenceId:
                """
                Append two existing Products via a fresh Occurrence.
                @param[in] theParentProduct       typed parent product identifier
                @param[in] theReferencedProduct   typed child product identifier being instantiated
                @param[in] thePlacement           local placement relative to parent
                @param[in] theParentOccurrence    optional placing occurrence (nested assembly chains)
                @param[out] theOutOccurrenceRefId optional out: typed ref id of the inserted OccurrenceRef
                @return typed occurrence definition identifier, or invalid if the chain is not active
                """

            @overload
            def Append(self, theParentProduct: BRepGraph_ProductId, theChildProducts: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ProductId], thePlacements: nanoocp.NCollection.NCollection_Array1[nanoocp.TopLoc.TopLoc_Location]) -> nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]:
                """
                Batch-append multiple child products to a parent product via fresh Occurrences.
                Two-pass: validates all inputs first, then links all.
                @param[in] theParentProduct  typed parent product identifier
                @param[in] theChildProducts  child product identifiers to instantiate
                @param[in] thePlacements     local placements per child (must match child count)
                @return array of created occurrence reference ids, empty on validation failure
                """

            def RemoveOccurrence(self, theProductDefId: BRepGraph_ProductId, theOccurrenceRefId: BRepGraph_OccurrenceRefId) -> bool:
                """
                Detach one exact occurrence ref from a product definition.
                Use BRepGraph_RefsOccurrenceOfProduct::CurrentId() when removing from a
                product iterator. The method removes the exact OccurrenceRef entry, erases
                it from the product's ordered ref sequence, updates relation tables, and
                prunes the occurrence subtree when it has no other active usages.
                @param[in] theProductDefId    product definition identifier
                @param[in] theOccurrenceRefId exact product-owned occurrence reference identifier
                @return true if the active product-owned usage was removed
                """

            def RemoveOccurrences(self, theProductId: BRepGraph_ProductId, theOccurrenceRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]) -> bool:
                """
                Batch-remove multiple occurrence refs from a product definition.
                All-or-nothing: validates all inputs first, then removes all.
                @param[in] theProductId     product definition identifier
                @param[in] theOccurrenceRefs occurrence reference identifiers to remove
                @return true if all refs were successfully removed
                """

            def RemoveShapeRoot(self, theProductDefId: BRepGraph_ProductId) -> bool:
                """
                Detach the scalar shape-root ownership from a product definition.
                If no other active product owns the same topology root afterward, the root
                subgraph is pruned as orphaned. The product loses its direct shape root;
                it is no longer a part, and it only remains an assembly if it still owns
                active child occurrences.
                @param[in] theProductDefId product definition identifier
                @return true if an active shape root was detached
                """

            def Mut(self, theProduct: BRepGraph_ProductId) -> BRepGraph_MutGuard__BRepGraphInc_ProductDef:
                """Return scoped mutable product definition guard."""

        class OccurrenceOps:
            """@brief Occurrence mutation operations."""

            def __init__(self, theOther: BRepGraph.EditorView.OccurrenceOps) -> None: ...

            def Mut(self, theOccurrence: BRepGraph_OccurrenceId) -> BRepGraph_MutGuard__BRepGraphInc_OccurrenceDef:
                """Return scoped mutable occurrence definition guard."""

            def MutRef(self, theOccurrenceRef: BRepGraph_OccurrenceRefId) -> BRepGraph_MutGuard__BRepGraphInc_OccurrenceRef:
                """Return scoped mutable occurrence reference guard."""

            @overload
            def SetRefLocalLocation(self, theOccurrenceRef: BRepGraph_OccurrenceRefId, theLoc: nanoocp.TopLoc.TopLoc_Location) -> None:
                """
                Set the local location of an occurrence reference and fire immediate notification.
                @param[in] theOccurrenceRef typed occurrence reference identifier
                @param[in] theLoc           new local location
                """

            @overload
            def SetRefLocalLocation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_OccurrenceRef, theLoc: nanoocp.TopLoc.TopLoc_Location) -> None:
                """
                Set the local location of an occurrence reference inside a batched mutation scope.
                @param[in] theMut active mutable occurrence reference guard
                @param[in] theLoc new local location
                """

            @overload
            def SetChildNodeId(self, theOccurrence: BRepGraph_OccurrenceId, theChildNodeId: BRepGraph_NodeId) -> None:
                """
                Set the child node referenced by an occurrence definition.
                Invalid or removed occurrence ids are ignored. The child must be an
                active topology node or an active Product; invalid, removed, and
                Occurrence child ids are ignored.
                """

            @overload
            def SetChildNodeId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_OccurrenceDef, theChildNodeId: BRepGraph_NodeId) -> None:
                """
                Set the child node id inside a batched mutation scope. Invalid, removed,
                and Occurrence child ids are ignored.
                """

            @overload
            def SetRefChildOccurrenceId(self, theOccurrenceRef: BRepGraph_OccurrenceRefId, theOccurrence: BRepGraph_OccurrenceId) -> None:
                """
                Rewire an occurrence reference to a different occurrence def (rebinds ProductToOccurrences).
                """

            @overload
            def SetRefChildOccurrenceId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_OccurrenceRef, theOccurrence: BRepGraph_OccurrenceId) -> None: ...

        class GenOps:
            """@brief Generic node, reference, and representation removal operations."""

            def __init__(self, theOther: BRepGraph.EditorView.GenOps) -> None: ...

            def RemoveNode(self, theNode: BRepGraph_NodeId) -> None:
                """
                Mark a node as removed (soft deletion).
                @param[in] theNode node to remove
                """

            def ReplaceNode(self, theNode: BRepGraph_NodeId, theReplacement: BRepGraph_NodeId) -> None:
                """
                Replace a node by another active node and mark the old node as removed.
                For Edge nodes: all CoEdges referencing the removed edge are reparented to
                the replacement edge (ChildEdgeId updated, relation entries rebound). This prevents
                orphaned CoEdges that would disappear from CoEdgesOfEdge() queries.
                If the replacement is active, layers receive OnNodeReplaced(theNode,
                theReplacement) for structural data migration. If the replacement is invalid
                or inactive, the operation falls back to OnNodeRemoved(theNode), matching pure
                deletion. Semantic history records are not inferred here; algorithms should
                record operation-specific history.
                @param[in] theNode        node to remove
                @param[in] theReplacement node that replaces theNode
                """

            def RemoveSubgraph(self, theNode: BRepGraph_NodeId) -> None:
                """
                Mark a node and all its descendants as removed (cascading soft deletion).
                @param[in] theNode root node to remove
                """

            @overload
            def RemoveRef(self, theRef: BRepGraph_RefId) -> bool:
                """
                Mark a reference entry as removed (soft deletion).
                This is the builder-level API for detaching a child usage from its parent
                without removing the referenced definition itself.
                Invalid or already-removed ids are ignored.
                @param[in] theRef reference entry to remove
                @return true if the reference transitioned from active to removed
                """

            @overload
            def RemoveRef(self, theParent: BRepGraph_NodeId, theRef: BRepGraph_RefId, theToPruneOrphanedChild: bool) -> bool:
                """
                Mark an exact parent-owned reference entry as removed (soft deletion).
                This overload validates that the reference really belongs to the supplied
                parent and can optionally prune the child subtree when the removed usage
                was the last active parent usage of that child definition.
                Use this overload for UI/path-driven detach operations where the parent
                context is part of the user's selection.
                @param[in] theParent              expected owning parent of the reference usage
                @param[in] theRef                 reference entry to remove
                @param[in] theToPruneOrphanedChild if true, remove the referenced child
                subtree when no active parent usages remain after detachment
                @return true if the reference transitioned from active to removed
                """

            def MutChildRef(self, theChildRef: BRepGraph_ChildRefId) -> BRepGraph_MutGuard__BRepGraphInc_ChildRef:
                """
                Return scoped mutable child reference guard. ChildRef is generic (the
                child node can be of any kind), so its Mut accessor lives on the
                cross-kind Gen() rather than on a per-kind Ops.
                """

            @overload
            def SetChildRefLocalLocation(self, theChildRef: BRepGraph_ChildRefId, theLoc: nanoocp.TopLoc.TopLoc_Location) -> None:
                """
                Set the local location of a child reference and fire immediate notification.
                @param[in] theChildRef typed child reference identifier
                @param[in] theLoc      new local location
                """

            @overload
            def SetChildRefLocalLocation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_ChildRef, theLoc: nanoocp.TopLoc.TopLoc_Location) -> None:
                """
                Set the local location of a child reference inside a batched mutation scope.
                @param[in] theMut active mutable child reference guard
                @param[in] theLoc new local location
                """

            @overload
            def SetChildRefOrientation(self, theChildRef: BRepGraph_ChildRefId, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation of a child reference."""

            @overload
            def SetChildRefOrientation(self, theMut: BRepGraph_MutGuard__BRepGraphInc_ChildRef, theOrientation: nanoocp.BRepGraphInc.ParityOrientation) -> None:
                """Set the orientation inside a batched mutation scope."""

            @overload
            def SetChildRefChildNodeId(self, theChildRef: BRepGraph_ChildRefId, theChild: BRepGraph_NodeId) -> None:
                """
                Rewire a child reference to a different child def (rebinds CompoundsOf<Kind>).
                """

            @overload
            def SetChildRefChildNodeId(self, theMut: BRepGraph_MutGuard__BRepGraphInc_ChildRef, theChild: BRepGraph_NodeId) -> None: ...

            def CleanupRemovedReferences(self) -> None:
                """
                Clean up forward references to removed nodes in relation tables and
                references. After one or more RemoveNode calls, other entities may
                still hold stale child references pointing to removed nodes. This method
                marks those stale references as removed, detaches them from parent
                arrays, and updates relation entries for consistency.
                @post ValidateRelations() passes.
                """

        class BoundaryIssue:
            """
            A single boundary invariant issue detected by ValidateMutationBoundary().
            """

            @overload
            def __init__(self) -> None: ...

            @overload
            def __init__(self, theOther: BRepGraph.EditorView.BoundaryIssue) -> None: ...

            @property
            def NodeId(self) -> BRepGraph_NodeId: ...

            @NodeId.setter
            def NodeId(self, arg: BRepGraph_NodeId, /) -> None: ...

            @property
            def Description(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

            @Description.setter
            def Description(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        def Vertices(self) -> BRepGraph.EditorView.VertexOps:
            """Return vertex creation operations."""

        def Edges(self) -> BRepGraph.EditorView.EdgeOps:
            """Return edge creation and editing operations."""

        def CoEdges(self) -> BRepGraph.EditorView.CoEdgeOps:
            """Return coedge and PCurve operations."""

        def Wires(self) -> BRepGraph.EditorView.WireOps:
            """Return wire creation and editing operations."""

        def Faces(self) -> BRepGraph.EditorView.FaceOps:
            """Return face creation and editing operations."""

        def Shells(self) -> BRepGraph.EditorView.ShellOps:
            """Return shell creation and editing operations."""

        def Solids(self) -> BRepGraph.EditorView.SolidOps:
            """Return solid creation and editing operations."""

        def Compounds(self) -> BRepGraph.EditorView.CompoundOps:
            """Return compound creation and editing operations."""

        def CompSolids(self) -> BRepGraph.EditorView.CompSolidOps:
            """Return compsolid creation and editing operations."""

        def Products(self) -> BRepGraph.EditorView.ProductOps:
            """Return product and assembly creation and editing operations."""

        def Occurrences(self) -> BRepGraph.EditorView.OccurrenceOps:
            """Return occurrence mutation operations."""

        def Gen(self) -> BRepGraph.EditorView.GenOps:
            """Return generic node, reference, and representation removal operations."""

        def Supplement(self) -> BRepGraph_SupplementEditor:
            """Return runtime supplement attachment operations."""

        def BeginDeferredInvalidation(self) -> None:
            """
            Begin deferred invalidation mode.
            While active, markModified() only increments OwnGen + SubtreeGen and
            appends to the deferred list - without acquiring the shape-cache mutex
            or propagating upward.
            Call EndDeferredInvalidation() to batch-flush all accumulated changes.
            Intended for batch mutation loops (SameParameter, Sewing) where many
            entities are modified sequentially and upward propagation should be
            deferred until all mutations are complete.
            Prefer BRepGraph_DeferredScope RAII guard.
            @warning Deferred mode batches invalidation only; it does NOT serialize
            the mutation body. Callers must guarantee exclusive Editor() structural
            edit access for the whole deferred scope; concurrent Editor().Mut*()
            usage still requires external synchronization around the surrounding batch.
            """

        def EndDeferredInvalidation(self) -> None:
            """
            End deferred invalidation mode and batch-flush:
            propagates SubtreeGen upward for all modified entities from the deferred
            list. Shape cache entries are validated lazily via SubtreeGen comparison.
            """

        def IsDeferredMode(self) -> bool:
            """
            Check if deferred invalidation mode is currently active.
            @note This is a state flag only. It does not imply mutation ownership
            or synchronization guarantees.
            """

        def CommitMutation(self) -> None:
            """
            Finalize a batch of mutations.
            Validates relation consistency and asserts active entity counts
            match actual entity state.
            Call this after manual batch mutation loops, or rely on
            BRepGraph_DeferredScope to call it automatically at scope exit.
            """

        def ValidateMutationBoundary(self, theIssues: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph.EditorView.BoundaryIssue] = None) -> bool:
            """
            Validate lightweight mutation-boundary invariants.
            @param[out] theIssues optional destination for detailed issues
            @return true if no issues were found
            """

    class RefsView:
        """
        @brief Read-only view for RefId/RefUID-based reference storage.

        This view exposes reference-entry storage:
        - typed reference entry access (Shell, Face, ...)
        - reference counts
        - RefUID lookup and reverse lookup through BRepGraph::UIDs()
        - freshness checks via BRepGraph_VersionStamp through BRepGraph::UIDs()

        Identity semantics:
        - RefId (kind + index) is graph-local and may change after Compact().
        Use it for in-graph traversal and short-lived mutation logic.
        - RefUID (kind + counter) is stable across index remapping and intended
        for longer-lived identity tracking. Graph generation is carried by
        BRepGraph_VersionStamp when freshness checks are needed.

        ## RefsView vs TopoView naming
        RefsView accessors take reference IDs (BRepGraph_ShellRefId, BRepGraph_FaceRefId)
        and return reference-entry structs carrying per-use orientation and location.
        TopoView accessors take definition IDs (BRepGraph_ShellId, BRepGraph_FaceId)
        and return definition structs.

        ## Iterating over references
        Reference entries are primarily traversed in parent-owned context through
        the typed grouped IdsOf accessors. When flat iteration is needed, iterate
        using the matching typed RefId over the appropriate grouped Nb() or NbActive() count:
        @code
        const BRepGraph::RefsView& aRefs = aGraph.Refs();
        const BRepGraph_FaceRefId anEndFaceRefId = aRefs.Faces().EndId();
        for (BRepGraph_FaceRefId aFaceRefId = aRefs.Faces().StartId();
        aFaceRefId < anEndFaceRefId;
        ++aFaceRefId)
        {
        const BRepGraphInc::FaceRef& aFR = aRefs.Faces().Entry(aFaceRefId);
        if (aFR.IsRemoved)
        continue;
        // use aFR.FaceId, aFR.Orientation, aFR.Location ...
        }
        @endcode

        To iterate refs belonging to a specific parent, use the grouped IdsOf
        accessors:
        @code
        for (const BRepGraph_WireRefId& aWireRefId : aRefs.Wires().IdsOf(aFaceId))
        {
        const BRepGraphInc::WireRef& aWR = aRefs.Wires().Entry(aWireRefId);
        // ...
        }
        @endcode
        """

        def __init__(self, theOther: BRepGraph.RefsView) -> None: ...

        class ShellOps:
            """@brief Shell reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.ShellOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_ShellRefId: ...

            def EndId(self) -> BRepGraph_ShellRefId: ...

            def Entry(self, theRefId: BRepGraph_ShellRefId) -> nanoocp.BRepGraphInc.ShellRef: ...

            def IdsOf(self, theSolid: BRepGraph_SolidId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ShellRefId]: ...

        class FaceOps:
            """@brief Face reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.FaceOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_FaceRefId: ...

            def EndId(self) -> BRepGraph_FaceRefId: ...

            def Entry(self, theRefId: BRepGraph_FaceRefId) -> nanoocp.BRepGraphInc.FaceRef: ...

            def IdsOf(self, theShell: BRepGraph_ShellId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_FaceRefId]: ...

        class WireOps:
            """@brief Wire reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.WireOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_WireRefId: ...

            def EndId(self) -> BRepGraph_WireRefId: ...

            def Entry(self, theRefId: BRepGraph_WireRefId) -> nanoocp.BRepGraphInc.WireRef: ...

            def IdsOf(self, theFace: BRepGraph_FaceId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_WireRefId]: ...

        class VertexOps:
            """@brief Vertex reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.VertexOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_VertexRefId: ...

            def EndId(self) -> BRepGraph_VertexRefId: ...

            def Entry(self, theRefId: BRepGraph_VertexRefId) -> nanoocp.BRepGraphInc.VertexRef: ...

        class SolidOps:
            """@brief Solid reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.SolidOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_SolidRefId: ...

            def EndId(self) -> BRepGraph_SolidRefId: ...

            def Entry(self, theRefId: BRepGraph_SolidRefId) -> nanoocp.BRepGraphInc.SolidRef: ...

            def IdsOf(self, theCompSolid: BRepGraph_CompSolidId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_SolidRefId]: ...

        class ChildOps:
            """@brief Generic child reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.ChildOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_ChildRefId: ...

            def EndId(self) -> BRepGraph_ChildRefId: ...

            def Entry(self, theRefId: BRepGraph_ChildRefId) -> nanoocp.BRepGraphInc.ChildRef: ...

            def IdsOf(self, theCompound: BRepGraph_CompoundId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ChildRefId]: ...

            def IdsReferencing(self, theChild: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ChildRefId]: ...

        class OccurrenceOps:
            """@brief Occurrence reference queries."""

            def __init__(self, theOther: BRepGraph.RefsView.OccurrenceOps) -> None: ...

            def Nb(self) -> int: ...

            def NbActive(self) -> int: ...

            def StartId(self) -> BRepGraph_OccurrenceRefId: ...

            def EndId(self) -> BRepGraph_OccurrenceRefId: ...

            def Entry(self, theRefId: BRepGraph_OccurrenceRefId) -> nanoocp.BRepGraphInc.OccurrenceRef: ...

            def IdsOf(self, theProduct: BRepGraph_ProductId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]: ...

            def IdsReferencing(self, theChild: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]: ...

        class GenOps:
            """@brief Generic reference id queries."""

            def __init__(self, theOther: BRepGraph.RefsView.GenOps) -> None: ...

            def Nb(self, theKind: BRepGraph_RefId.Kind) -> int:
                """
                Return the number of references of the specified kind (including soft-removed).
                """

            def IsValid(self, theRef: BRepGraph_RefId) -> bool:
                """
                Return true if the reference id kind and index are within storage bounds.
                """

            def IsActive(self, theRef: BRepGraph_RefId) -> bool:
                """Return true if the reference id is valid and not soft-removed."""

            def IsRemoved(self, theRef: BRepGraph_RefId) -> bool:
                """Return true if the specified typed RefId is invalid or marked removed."""

            def RefAtStep(self, theParent: BRepGraph_NodeId, theStep: int) -> BRepGraph_RefId:
                """
                Return the direct parent-owned RefId stored at the specified child step.
                This is a structural lookup over the parent's raw ref arrays and does not
                skip removed refs or refs targeting removed child defs.
                """

            def ChildNode(self, theRef: BRepGraph_RefId) -> BRepGraph_NodeId:
                """Resolve the child definition node referenced by any typed RefId."""

            def LocalLocation(self, theRef: BRepGraph_RefId) -> nanoocp.TopLoc.TopLoc_Location:
                """
                Return the local location carried by the specified typed RefId.
                OccurrenceRef and invalid refs return identity.
                """

            def Orientation(self, theRef: BRepGraph_RefId) -> nanoocp.TopAbs.TopAbs_Orientation:
                """
                Return the orientation carried by the specified typed RefId.
                OccurrenceRef and invalid refs return TopAbs_FORWARD.
                """

        def Shells(self) -> BRepGraph.RefsView.ShellOps:
            """Grouped shell reference queries."""

        def Faces(self) -> BRepGraph.RefsView.FaceOps:
            """Grouped face reference queries."""

        def Wires(self) -> BRepGraph.RefsView.WireOps:
            """Grouped wire reference queries."""

        def Vertices(self) -> BRepGraph.RefsView.VertexOps:
            """Grouped vertex reference queries."""

        def Solids(self) -> BRepGraph.RefsView.SolidOps:
            """Grouped solid reference queries."""

        def Children(self) -> BRepGraph.RefsView.ChildOps:
            """Grouped child reference queries."""

        def Occurrences(self) -> BRepGraph.RefsView.OccurrenceOps:
            """Grouped occurrence reference queries."""

        def Gen(self) -> BRepGraph.RefsView.GenOps:
            """Grouped generic reference id queries."""

    class TopoView:
        """
        @brief Unified read-only view over topology definitions, adjacency, and representations.

        Provides topology definition lookup, representation lookup, read-only
        adjacency queries, and assembly classification over the incidence-table
        model stored in BRepGraph.
        Obtained via BRepGraph::Topo().

        ## Soft-deletion convention
        Per-kind count methods (Faces().Nb(), Edges().Nb(), etc.) return totals
        including soft-removed nodes. Prefer per-kind NbActive() variants for
        traversal and validation code that should ignore removed entities.
        Definition accessors (Face, Edge, etc.) do not filter removed nodes - callers should check
        IsRemoved() if needed.

        ## TopoView vs RefsView naming
        TopoView accessors take definition IDs (BRepGraph_FaceId, BRepGraph_ShellId, etc.)
        and return definition structs (FaceDef, ShellDef). RefsView accessors take
        reference IDs (BRepGraph_FaceRefId, BRepGraph_ShellRefId) and return
        reference-entry structs carrying per-use orientation and location.

        Relations() is the single entry point for ordered topology relation containers.
        Adjacency helpers return references only into existing relation storage.
        Ref-owned parent links are exposed as reference-id containers; callers resolve
        parent definitions through RefsView entries or typed iterators.
        """

        def __init__(self, theOther: BRepGraph.TopoView) -> None: ...

        class FaceOps:
            """@brief Face-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.FaceOps) -> None: ...

            def Nb(self) -> int:
                """Return the total number of face definitions (including soft-removed)."""

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) face definitions."""

            def StartId(self) -> BRepGraph_FaceId:
                """Return the first valid face identifier for iteration."""

            def EndId(self) -> BRepGraph_FaceId:
                """Return the past-the-end face identifier (one past the last valid id)."""

            def Definition(self, theFace: BRepGraph_FaceId) -> nanoocp.BRepGraphInc.FaceDef:
                """
                Return the definition struct for the given face.
                @param[in] theFace typed face identifier
                """

            def Relations(self, theFace: BRepGraph_FaceId) -> nanoocp.BRepGraphInc.FaceRelations:
                """
                Return the relation struct (adjacency lists) for the given face.
                @param[in] theFace typed face identifier
                """

            def Surface(self, theFace: BRepGraph_FaceId) -> nanoocp.Geom.Geom_Surface:
                """
                Return the surface handle for the given face.
                May be null if the face has no surface representation.
                @param[in] theFace typed face identifier
                """

            def ActiveTriangulation(self, theFace: BRepGraph_FaceId) -> nanoocp.Poly.Poly_Triangulation:
                """
                Return the active triangulation for the given face.
                Returns null if the face has no triangulation or it has been invalidated.
                @param[in] theFace typed face identifier
                """

        class EdgeOps:
            """@brief Edge-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.EdgeOps) -> None: ...

            def Nb(self) -> int:
                """Return the total number of edge definitions (including soft-removed)."""

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) edge definitions."""

            def StartId(self) -> BRepGraph_EdgeId:
                """Return the first valid edge identifier for iteration."""

            def EndId(self) -> BRepGraph_EdgeId:
                """Return the past-the-end edge identifier (one past the last valid id)."""

            def Definition(self, theEdge: BRepGraph_EdgeId) -> nanoocp.BRepGraphInc.EdgeDef:
                """
                Return the definition struct for the given edge.
                @param[in] theEdge typed edge identifier
                """

            def Relations(self, theEdge: BRepGraph_EdgeId) -> nanoocp.BRepGraphInc.EdgeRelations:
                """
                Return the relation struct (adjacency lists) for the given edge.
                @param[in] theEdge typed edge identifier
                """

            def NbFaces(self, theEdge: BRepGraph_EdgeId) -> int:
                """
                Return the number of active faces adjacent to the given edge through active coedges.
                @param[in] theEdge typed edge definition identifier
                @return active adjacent face count
                """

            @overload
            def WiresOf(self, theEdge: BRepGraph_EdgeId) -> BRepGraph_WiresOfEdge:
                """
                Return an iterator over active wires that reference the given edge through active coedges.
                @param[in] theEdge typed edge definition identifier
                @return iterator positioned at the first active wire, or at end if none exists
                """

            @overload
            def WiresOf(self, theEdge: BRepGraph_EdgeId, theStartIndex: int) -> BRepGraph_WiresOfEdge:
                """
                Return an iterator over active wires from a stored edge-coedge relation index.
                @param[in] theEdge       typed edge definition identifier
                @param[in] theStartIndex zero-based index in EdgeRelations::CoEdgeIds to resume from
                @return iterator positioned at the first active wire at or after theStartIndex
                """

            @overload
            def FacesOf(self, theEdge: BRepGraph_EdgeId) -> BRepGraph_FacesOfEdge:
                """
                Return an iterator over active faces adjacent to the given edge through active coedges.
                @param[in] theEdge typed edge definition identifier
                @return iterator positioned at the first active face, or at end if none exists
                """

            @overload
            def FacesOf(self, theEdge: BRepGraph_EdgeId, theStartIndex: int) -> BRepGraph_FacesOfEdge:
                """
                Return an iterator over active faces from a stored edge-coedge relation index.
                @param[in] theEdge       typed edge definition identifier
                @param[in] theStartIndex zero-based index in EdgeRelations::CoEdgeIds to resume from
                @return iterator positioned at the first active face at or after theStartIndex
                """

            def CoEdges(self, theEdge: BRepGraph_EdgeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_CoEdgeId]:
                """
                Return the coedges that reference the given edge.
                @param[in] theEdge typed edge identifier
                """

            def Curve3D(self, theEdge: BRepGraph_EdgeId) -> nanoocp.Geom.Geom_Curve:
                """
                Return the 3D curve handle for the given edge.
                May be null if the edge has no 3D curve representation.
                @param[in] theEdge typed edge identifier
                """

        class VertexOps:
            """@brief Vertex-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.VertexOps) -> None: ...

            def Nb(self) -> int:
                """
                Return the total number of vertex definitions (including soft-removed).
                """

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) vertex definitions."""

            def StartId(self) -> BRepGraph_VertexId:
                """Return the first valid vertex identifier for iteration."""

            def EndId(self) -> BRepGraph_VertexId:
                """
                Return the past-the-end vertex identifier (one past the last valid id).
                """

            def Definition(self, theVertex: BRepGraph_VertexId) -> nanoocp.BRepGraphInc.VertexDef:
                """
                Return the definition struct for the given vertex.
                @param[in] theVertex typed vertex identifier
                """

            def Relations(self, theVertex: BRepGraph_VertexId) -> nanoocp.BRepGraphInc.VertexRelations:
                """
                Return the relation struct (adjacency lists) for the given vertex.
                @param[in] theVertex typed vertex identifier
                """

            def Edges(self, theVertex: BRepGraph_VertexId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_EdgeId]:
                """
                Return the edges incident to the given vertex.
                @param[in] theVertex typed vertex identifier
                """

        class WireOps:
            """@brief Wire-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.WireOps) -> None: ...

            def Nb(self) -> int:
                """Return the total number of wire definitions (including soft-removed)."""

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) wire definitions."""

            def StartId(self) -> BRepGraph_WireId:
                """Return the first valid wire identifier for iteration."""

            def EndId(self) -> BRepGraph_WireId:
                """Return the past-the-end wire identifier (one past the last valid id)."""

            def Definition(self, theWire: BRepGraph_WireId) -> nanoocp.BRepGraphInc.WireDef:
                """
                Return the definition struct for the given wire.
                @param[in] theWire typed wire identifier
                """

            def Relations(self, theWire: BRepGraph_WireId) -> nanoocp.BRepGraphInc.WireRelations:
                """
                Return the relation struct (adjacency lists) for the given wire.
                @param[in] theWire typed wire identifier
                """

        class ShellOps:
            """@brief Shell-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.ShellOps) -> None: ...

            def Nb(self) -> int:
                """Return the total number of shell definitions (including soft-removed)."""

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) shell definitions."""

            def StartId(self) -> BRepGraph_ShellId:
                """Return the first valid shell identifier for iteration."""

            def EndId(self) -> BRepGraph_ShellId:
                """Return the past-the-end shell identifier (one past the last valid id)."""

            def Definition(self, theShell: BRepGraph_ShellId) -> nanoocp.BRepGraphInc.ShellDef:
                """
                Return the definition struct for the given shell.
                @param[in] theShell typed shell identifier
                """

            def Relations(self, theShell: BRepGraph_ShellId) -> nanoocp.BRepGraphInc.ShellRelations:
                """
                Return the relation struct (adjacency lists) for the given shell.
                @param[in] theShell typed shell identifier
                """

        class SolidOps:
            """@brief Solid-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.SolidOps) -> None: ...

            def Nb(self) -> int:
                """Return the total number of solid definitions (including soft-removed)."""

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) solid definitions."""

            def StartId(self) -> BRepGraph_SolidId:
                """Return the first valid solid identifier for iteration."""

            def EndId(self) -> BRepGraph_SolidId:
                """Return the past-the-end solid identifier (one past the last valid id)."""

            def Definition(self, theSolid: BRepGraph_SolidId) -> nanoocp.BRepGraphInc.SolidDef:
                """
                Return the definition struct for the given solid.
                @param[in] theSolid typed solid identifier
                """

            def Relations(self, theSolid: BRepGraph_SolidId) -> nanoocp.BRepGraphInc.SolidRelations:
                """
                Return the relation struct (adjacency lists) for the given solid.
                @param[in] theSolid typed solid identifier
                """

        class CoEdgeOps:
            """@brief Coedge-oriented topology and representation queries."""

            def __init__(self, theOther: BRepGraph.TopoView.CoEdgeOps) -> None: ...

            def Nb(self) -> int:
                """
                Return the total number of coedge definitions (including soft-removed).
                """

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) coedge definitions."""

            def StartId(self) -> BRepGraph_CoEdgeId:
                """Return the first valid coedge identifier for iteration."""

            def EndId(self) -> BRepGraph_CoEdgeId:
                """
                Return the past-the-end coedge identifier (one past the last valid id).
                """

            def Definition(self, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.BRepGraphInc.CoEdgeDef:
                """
                Return the definition struct for the given coedge.
                @param[in] theCoEdge typed coedge identifier
                """

            def Edge(self, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_EdgeId:
                """
                Return the parent edge of the given coedge.
                @param[in] theCoEdge typed coedge identifier
                """

            def Face(self, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_FaceId:
                """
                Return the face that owns the given coedge.
                @param[in] theCoEdge typed coedge identifier
                """

            def Wire(self, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_WireId:
                """
                Return the wire that owns the given coedge.
                @param[in] theCoEdge typed coedge identifier
                """

            def Curve2D(self, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Geom2d.Geom2d_Curve:
                """
                Return the 2D PCurve handle for the given coedge.
                May be null if the coedge has no PCurve representation.
                @param[in] theCoEdge typed coedge identifier
                """

        class CompoundOps:
            """@brief Compound-oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.CompoundOps) -> None: ...

            def Nb(self) -> int:
                """
                Return the total number of compound definitions (including soft-removed).
                """

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) compound definitions."""

            def StartId(self) -> BRepGraph_CompoundId:
                """Return the first valid compound identifier for iteration."""

            def EndId(self) -> BRepGraph_CompoundId:
                """
                Return the past-the-end compound identifier (one past the last valid id).
                """

            def Definition(self, theCompound: BRepGraph_CompoundId) -> nanoocp.BRepGraphInc.CompoundDef:
                """
                Return the definition struct for the given compound.
                @param[in] theCompound typed compound identifier
                """

            def Relations(self, theCompound: BRepGraph_CompoundId) -> nanoocp.BRepGraphInc.CompoundRelations:
                """
                Return the relation struct (child references) for the given compound.
                @param[in] theCompound typed compound identifier
                """

        class CompSolidOps:
            """@brief Comp-solid oriented topology queries."""

            def __init__(self, theOther: BRepGraph.TopoView.CompSolidOps) -> None: ...

            def Nb(self) -> int:
                """
                Return the total number of comp-solid definitions (including soft-removed).
                """

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) comp-solid definitions."""

            def StartId(self) -> BRepGraph_CompSolidId:
                """Return the first valid comp-solid identifier for iteration."""

            def EndId(self) -> BRepGraph_CompSolidId:
                """
                Return the past-the-end comp-solid identifier (one past the last valid id).
                """

            def Definition(self, theCompSolid: BRepGraph_CompSolidId) -> nanoocp.BRepGraphInc.CompSolidDef:
                """
                Return the definition struct for the given comp-solid.
                @param[in] theCompSolid typed comp-solid identifier
                """

            def Relations(self, theCompSolid: BRepGraph_CompSolidId) -> nanoocp.BRepGraphInc.CompSolidRelations:
                """
                Return the relation struct (child solids) for the given comp-solid.
                @param[in] theCompSolid typed comp-solid identifier
                """

        class ProductOps:
            """@brief Product-oriented raw assembly queries."""

            def __init__(self, theOther: BRepGraph.TopoView.ProductOps) -> None: ...

            def Nb(self) -> int:
                """
                Return the total number of product definitions (including soft-removed).
                """

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) product definitions."""

            def StartId(self) -> BRepGraph_ProductId:
                """Return the first valid product identifier for iteration."""

            def EndId(self) -> BRepGraph_ProductId:
                """
                Return the past-the-end product identifier (one past the last valid id).
                """

            def Definition(self, theProduct: BRepGraph_ProductId) -> nanoocp.BRepGraphInc.ProductDef:
                """
                Return the definition struct for the given product.
                @param[in] theProduct typed product definition identifier
                """

            def Relations(self, theProduct: BRepGraph_ProductId) -> nanoocp.BRepGraphInc.ProductRelations:
                """
                Return the relation struct (occurrences, shape root) for the given product.
                @param[in] theProduct typed product definition identifier
                """

            def ShapeRoot(self, theProduct: BRepGraph_ProductId) -> BRepGraph_NodeId:
                """
                Return the topology root NodeId for the given product.
                For assemblies (no topology root) returns an invalid NodeId.
                @param[in] theProduct typed product definition identifier
                """

            def IsAssembly(self, theProduct: BRepGraph_ProductId) -> bool:
                """
                True if the product is an assembly (has active child occurrences and no topology root).
                @param[in] theProduct typed product definition identifier
                """

            def IsPart(self, theProduct: BRepGraph_ProductId) -> bool:
                """
                True if the product is a part (has a valid topology root).
                @param[in] theProduct typed product definition identifier
                """

            def ShapeRootNode(self, theProduct: BRepGraph_ProductId) -> BRepGraph_NodeId:
                """
                Return the topology root NodeId for a part product.
                For assemblies (no topology root) returns an invalid NodeId.
                @param[in] theProduct typed product definition identifier
                """

            def NbComponents(self, theProduct: BRepGraph_ProductId) -> int:
                """
                Number of active child occurrences of a product.
                @param[in] theProduct typed product definition identifier
                """

            def Component(self, theProduct: BRepGraph_ProductId, theComponentIdx: int) -> BRepGraph_OccurrenceId:
                """
                Return the i-th active child occurrence identifier of a product.
                @param[in] theProduct typed product definition identifier
                @param[in] theComponentIdx zero-based active occurrence index within the product
                """

        class OccurrenceOps:
            """@brief Occurrence-oriented raw assembly queries."""

            def __init__(self, theOther: BRepGraph.TopoView.OccurrenceOps) -> None: ...

            def Nb(self) -> int:
                """
                Return the total number of occurrence definitions (including soft-removed).
                """

            def NbActive(self) -> int:
                """Return the number of active (non-soft-removed) occurrence definitions."""

            def StartId(self) -> BRepGraph_OccurrenceId:
                """Return the first valid occurrence identifier for iteration."""

            def EndId(self) -> BRepGraph_OccurrenceId:
                """
                Return the past-the-end occurrence identifier (one past the last valid id).
                """

            def Definition(self, theOccurrence: BRepGraph_OccurrenceId) -> nanoocp.BRepGraphInc.OccurrenceDef:
                """
                Return the definition struct for the given occurrence.
                @param[in] theOccurrence typed occurrence identifier
                """

            def Relations(self, theOccurrence: BRepGraph_OccurrenceId) -> nanoocp.BRepGraphInc.OccurrenceRelations:
                """
                Return the relation struct (parent, placement) for the given occurrence.
                @param[in] theOccurrence typed occurrence identifier
                """

            def Product(self, theOccurrence: BRepGraph_OccurrenceId) -> BRepGraph_ProductId:
                """
                Return the product that this occurrence instantiates.
                @param[in] theOccurrence typed occurrence identifier
                """

            def ParentProduct(self, theOccurrence: BRepGraph_OccurrenceId) -> BRepGraph_ProductId:
                """
                Return the parent product that owns this occurrence.
                @param[in] theOccurrence typed occurrence identifier
                """

            def OccurrenceLocation(self, theOccurrence: BRepGraph_OccurrenceId) -> nanoocp.TopLoc.TopLoc_Location:
                """
                Return the local placement of an occurrence (OccurrenceRef::LocalLocation).
                This is the placement relative to the parent product, not the global placement.
                For global placement, use ChildExplorer with cumulative location tracking.
                @param[in] theOccurrence typed occurrence identifier
                @return OccurrenceRef::LocalLocation, or identity if not found
                """

        class GenOps:
            """@brief Generic topology and assembly count / meta queries."""

            def __init__(self, theOther: BRepGraph.TopoView.GenOps) -> None: ...

            def TopoEntity(self, theId: BRepGraph_NodeId) -> nanoocp.BRepGraphInc.BaseDef:
                """
                Return the base definition pointer for any topology node (polymorphic).
                Returns null if the node id is invalid, out of range, or soft-removed.
                @param[in] theId node identifier (any kind)
                """

            def CompoundRefIds(self, theChild: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ChildRefId]:
                """
                Return the compound (child) reference identifiers that point to the given node.
                @param[in] theChild node identifier
                """

            def OccurrenceRefIds(self, theChild: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]:
                """
                Return the occurrence reference identifiers that point to the given node.
                @param[in] theChild node identifier
                """

            def HasCompoundParents(self, theNode: BRepGraph_NodeId) -> bool:
                """
                True if the node has at least one compound parent.
                @param[in] theNode node identifier
                """

            def HasOccurrenceParents(self, theNode: BRepGraph_NodeId) -> bool:
                """
                True if the node has at least one occurrence parent.
                @param[in] theNode node identifier
                """

            def NbNodes(self) -> int:
                """
                Return the total number of nodes across all topology kinds (including soft-removed).
                """

            def Nb(self, theKind: BRepGraph_NodeId.Kind) -> int:
                """
                Return the number of node definitions of the specified kind (including soft-removed).
                """

            def IsValid(self, theNode: BRepGraph_NodeId) -> bool:
                """Return true if the node id kind and index are within storage bounds."""

            def IsActive(self, theNode: BRepGraph_NodeId) -> bool:
                """Return true if the node id is valid and not soft-removed."""

            def IsRemoved(self, theNode: BRepGraph_NodeId) -> bool:
                """
                Return true if the given node is invalid or has been soft-removed.
                @param[in] theNode node identifier
                """

        class GeometryOps:
            """@brief Analytic geometry representation queries."""

            def __init__(self, theOther: BRepGraph.TopoView.GeometryOps) -> None: ...

            def NbFaceSurfaces(self) -> int:
                """
                Return the total number of face surface representations (including soft-removed).
                """

            def NbEdgeCurves3D(self) -> int:
                """
                Return the total number of edge 3D curve representations (including soft-removed).
                """

            def NbCoEdgeCurves2D(self) -> int:
                """
                Return the total number of coedge 2D PCurve representations (including soft-removed).
                """

            def NbActiveFaceSurfaces(self) -> int:
                """
                Return the number of active (non-soft-removed) face surface representations.
                """

            def NbActiveEdgeCurves3D(self) -> int:
                """
                Return the number of active (non-soft-removed) edge 3D curve representations.
                """

            def NbActiveCoEdgeCurves2D(self) -> int:
                """
                Return the number of active (non-soft-removed) coedge 2D PCurve representations.
                """

        def Faces(self) -> BRepGraph.TopoView.FaceOps:
            """Grouped face-oriented queries."""

        def Edges(self) -> BRepGraph.TopoView.EdgeOps:
            """Grouped edge-oriented queries."""

        def Vertices(self) -> BRepGraph.TopoView.VertexOps:
            """Grouped vertex-oriented queries."""

        def Wires(self) -> BRepGraph.TopoView.WireOps:
            """Grouped wire-oriented queries."""

        def Shells(self) -> BRepGraph.TopoView.ShellOps:
            """Grouped shell-oriented queries."""

        def Solids(self) -> BRepGraph.TopoView.SolidOps:
            """Grouped solid-oriented queries."""

        def CoEdges(self) -> BRepGraph.TopoView.CoEdgeOps:
            """Grouped coedge-oriented queries."""

        def Compounds(self) -> BRepGraph.TopoView.CompoundOps:
            """Grouped compound-oriented queries."""

        def CompSolids(self) -> BRepGraph.TopoView.CompSolidOps:
            """Grouped comp-solid oriented queries."""

        def Products(self) -> BRepGraph.TopoView.ProductOps:
            """Grouped product-oriented queries."""

        def Occurrences(self) -> BRepGraph.TopoView.OccurrenceOps:
            """Grouped occurrence-oriented queries."""

        def Gen(self) -> BRepGraph.TopoView.GenOps:
            """Grouped generic topology and assembly counts / meta queries."""

        def Geometry(self) -> BRepGraph.TopoView.GeometryOps:
            """Grouped analytic geometry representation queries."""

    class MeshView:
        """
        @brief Read/write view over mesh data.

        Splits mesh access into three explicit sub-views:
        - `Cache()`     - reads from the BRepGraphMesh cache only (algorithm-derived,
        freshness-checked against the entity's OwnGen).
        - `Persistent()` - reads from definition-resident mesh (FaceDef.TriangulationRepId,
        EdgeDef.Polygon3DRepId, CoEdgeDef.Polygon2DRepId,
        CoEdgeDef.PolygonOnTriRepId).
        - `Editor()`    - cache mutations (append/clear). Persistent rep creation lives on
        `BRepGraph::Editor().Edges()`, `BRepGraph::Editor().CoEdges()`,
        `BRepGraph::Editor().Faces()` since reps back the topology defs.
        - `Poly()`      - mesh element count queries (shared by all paths).

        There is no fallback path that mixes cache and persistent - callers pick the
        source explicitly.

        Obtained via `BRepGraph::Mesh()` (const) or `BRepGraph::Mesh()` (non-const for Editor).
        """

        def __init__(self, theOther: BRepGraph.MeshView) -> None: ...

        class CacheView:
            """
            Cache reads. Each accessor returns data only if a fresh cache entry exists
            for the given entity (matched against its current OwnGen).
            """

            def __init__(self, theOther: BRepGraph.MeshView.CacheView) -> None: ...

            class FaceOps:
                def __init__(self, theOther: BRepGraph.MeshView.CacheView.FaceOps) -> None: ...

                def Has(self, theFace: BRepGraph_FaceId) -> bool:
                    """
                    True if a fresh cached triangulation is present.
                    @param[in] theFace typed face definition identifier
                    @return true if Entry() would return non-null
                    """

                def Triangulation(self, theFace: BRepGraph_FaceId) -> nanoocp.Poly.Poly_Triangulation:
                    """
                    Cached triangulation handle.
                    @param[in] theFace typed face definition identifier
                    @return triangulation handle, or null handle if absent
                    """

                def Entry(self, theFace: BRepGraph_FaceId) -> "BRepGraph_CacheMesh::FaceMeshEntry":
                    """
                    Raw cached face mesh entry, or nullptr if absent or stale.
                    @param[in] theFace typed face definition identifier
                    @return cache entry pointer, or nullptr
                    """

            class EdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.CacheView.EdgeOps) -> None: ...

                def Has(self, theEdge: BRepGraph_EdgeId) -> bool:
                    """
                    True if a fresh cached Polygon3D is bound to the edge.
                    @param[in] theEdge typed edge definition identifier
                    @return true if a fresh Polygon3D is present in cache
                    """

                def Polygon3D(self, theEdge: BRepGraph_EdgeId) -> nanoocp.Poly.Poly_Polygon3D:
                    """
                    Cached Polygon3D handle.
                    @param[in] theEdge typed edge definition identifier
                    @return polygon-3D handle, or null handle if absent
                    """

                def Entry(self, theEdge: BRepGraph_EdgeId) -> "BRepGraph_CacheMesh::EdgeMeshEntry":
                    """
                    Raw cached edge mesh entry, or nullptr if absent or stale.
                    @param[in] theEdge typed edge definition identifier
                    @return cache entry pointer, or nullptr
                    """

            class CoEdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.CacheView.CoEdgeOps) -> None: ...

                def Has(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
                    """
                    True if a fresh cached entry exists (any of polygon-2D / polygon-on-tri).
                    @param[in] theCoEdge typed coedge definition identifier
                    @return true if a fresh cache entry exists
                    """

                def FindPolygon2D(self, theCoEdge: BRepGraph_CoEdgeId) -> "BRepGraph_CacheMesh::CoEdgeMeshEntry":
                    """
                    Return coedge entry if Polygon2D is fresh, nullptr otherwise.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return cache entry pointer, or nullptr
                    """

                def FindPolygonOnTri(self, theCoEdge: BRepGraph_CoEdgeId) -> "BRepGraph_CacheMesh::CoEdgeMeshEntry":
                    """
                    Return coedge entry if PolygonsOnTri is fresh, nullptr otherwise.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return cache entry pointer, or nullptr
                    """

                def FindRaw(self, theCoEdge: BRepGraph_CoEdgeId) -> "BRepGraph_CacheMesh::CoEdgeMeshEntry":
                    """
                    Raw coedge entry access (no freshness filtering). Returns nullptr if
                    the entry has no representation. For internal/testing use.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return cache entry pointer, or nullptr if absent
                    """

            def Faces(self) -> BRepGraph.MeshView.CacheView.FaceOps:
                """Grouped face cache queries."""

            def Edges(self) -> BRepGraph.MeshView.CacheView.EdgeOps:
                """Grouped edge cache queries."""

            def CoEdges(self) -> BRepGraph.MeshView.CacheView.CoEdgeOps:
                """Grouped coedge cache queries."""

        class PersistentView:
            """
            Persistent reads. Resolves data through the rep id stored on the entity's
            definition (FaceDef / EdgeDef / CoEdgeDef). Independent of the cache.
            """

            def __init__(self, theOther: BRepGraph.MeshView.PersistentView) -> None: ...

            class FaceOps:
                def __init__(self, theOther: BRepGraph.MeshView.PersistentView.FaceOps) -> None: ...

                def Has(self, theFace: BRepGraph_FaceId) -> bool:
                    """
                    True if FaceDef.TriangulationRepId is valid and the rep is not removed.
                    @param[in] theFace typed face definition identifier
                    @return true if a persistent triangulation is bound
                    """

                def Triangulation(self, theFace: BRepGraph_FaceId) -> nanoocp.Poly.Poly_Triangulation:
                    """
                    Persistent triangulation handle.
                    @param[in] theFace typed face definition identifier
                    @return triangulation handle, or null handle if absent
                    """

            class EdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.PersistentView.EdgeOps) -> None: ...

                def Has(self, theEdge: BRepGraph_EdgeId) -> bool:
                    """
                    True if EdgeDef.Polygon3DRepId is bound (dominant kind on edges).
                    @param[in] theEdge typed edge definition identifier
                    @return true if a persistent Polygon3D is bound
                    """

                def Polygon3D(self, theEdge: BRepGraph_EdgeId) -> nanoocp.Poly.Poly_Polygon3D:
                    """
                    Persistent Polygon3D handle.
                    @param[in] theEdge typed edge definition identifier
                    @return polygon-3D handle, or null handle if absent
                    """

                def HasPolygonOnTriangulation(self, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId) -> bool:
                    """
                    True if the (edge, face) coedge has a polygon-on-triangulation.
                    @param[in] theEdge typed edge definition identifier
                    @param[in] theFace typed face definition identifier
                    @return true if persistent polygon-on-triangulation is bound
                    """

                def PolygonOnTriangulation(self, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId) -> nanoocp.Poly.Poly_PolygonOnTriangulation:
                    """
                    Polygon-on-triangulation for the (edge, face) coedge.
                    @param[in] theEdge typed edge definition identifier
                    @param[in] theFace typed face definition identifier
                    @return polygon-on-triangulation handle, or null handle if absent
                    """

            class CoEdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.PersistentView.CoEdgeOps) -> None: ...

                def Has(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
                    """
                    True if CoEdgeDef.Polygon2DRepId is bound (dominant kind on coedges).
                    @param[in] theCoEdge typed coedge definition identifier
                    @return true if a persistent polygon-on-surface is bound
                    """

                def PolygonOnSurface(self, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Poly.Poly_Polygon2D:
                    """
                    Persistent polygon-on-surface (2D polygon) bound to the coedge.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return polygon-2D handle, or null handle if absent
                    """

                def HasPolygonOnTriangulation(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
                    """
                    True if CoEdgeDef.PolygonOnTriRepId is bound.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return true if persistent polygon-on-triangulation is bound
                    """

                def PolygonOnTriangulation(self, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Poly.Poly_PolygonOnTriangulation:
                    """
                    Persistent polygon-on-triangulation bound to the coedge.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return polygon-on-triangulation handle, or null handle if absent
                    """

            def Faces(self) -> BRepGraph.MeshView.PersistentView.FaceOps:
                """Grouped face persistent queries."""

            def Edges(self) -> BRepGraph.MeshView.PersistentView.EdgeOps:
                """Grouped edge persistent queries."""

            def CoEdges(self) -> BRepGraph.MeshView.PersistentView.CoEdgeOps:
                """Grouped coedge persistent queries."""

        class EffectiveView:
            """
            Resolves mesh data by checking the cache first and the persistent (def-resident)
            source second. Callers that do not care which source supplies the data go
            through this view; callers that do care use Cache() or Persistent() directly.
            """

            def __init__(self, theOther: BRepGraph.MeshView.EffectiveView) -> None: ...

            class FaceOps:
                def __init__(self, theOther: BRepGraph.MeshView.EffectiveView.FaceOps) -> None: ...

                def Has(self, theFace: BRepGraph_FaceId) -> bool:
                    """
                    True if the face has a triangulation in either cache or persistent storage.
                    @param[in] theFace typed face definition identifier
                    @return true if any triangulation is reachable
                    """

                def Triangulation(self, theFace: BRepGraph_FaceId) -> nanoocp.Poly.Poly_Triangulation:
                    """
                    Cached triangulation handle (cache first, persistent fallback).
                    @param[in] theFace typed face definition identifier
                    @return triangulation handle, or null handle if absent
                    """

            class EdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.EffectiveView.EdgeOps) -> None: ...

                def Has(self, theEdge: BRepGraph_EdgeId) -> bool:
                    """
                    True if the edge has a Polygon3D in either cache or persistent storage.
                    @param[in] theEdge typed edge definition identifier
                    @return true if any Polygon3D is reachable
                    """

                def Polygon3D(self, theEdge: BRepGraph_EdgeId) -> nanoocp.Poly.Poly_Polygon3D:
                    """
                    Polygon3D handle (cache first, persistent fallback).
                    @param[in] theEdge typed edge definition identifier
                    @return polygon-3D handle, or null handle if absent
                    """

            class CoEdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.EffectiveView.CoEdgeOps) -> None: ...

                def Has(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
                    """
                    True if the coedge has any polygon-2D / polygon-on-tri in either source.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return true if any coedge mesh data is reachable
                    """

                def HasPolygonOnSurface(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
                    """
                    True if a polygon-on-surface (2D) is reachable in either source.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return true if a polygon-2D is bound on either side
                    """

                def PolygonOnSurface(self, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Poly.Poly_Polygon2D:
                    """
                    Polygon-on-surface (2D) handle (cache first, persistent fallback).
                    @param[in] theCoEdge typed coedge definition identifier
                    @return polygon-2D handle, or null handle if absent
                    """

                def HasPolygonOnTriangulation(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
                    """
                    True if a polygon-on-triangulation is reachable in either source.
                    @param[in] theCoEdge typed coedge definition identifier
                    @return true if a polygon-on-tri is bound on either side
                    """

                def PolygonOnTriangulation(self, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Poly.Poly_PolygonOnTriangulation:
                    """
                    Polygon-on-triangulation handle (cache first, persistent fallback).
                    @param[in] theCoEdge typed coedge definition identifier
                    @return polygon-on-tri handle, or null handle if absent
                    """

            def Faces(self) -> BRepGraph.MeshView.EffectiveView.FaceOps:
                """Grouped face effective queries."""

            def Edges(self) -> BRepGraph.MeshView.EffectiveView.EdgeOps:
                """Grouped edge effective queries."""

            def CoEdges(self) -> BRepGraph.MeshView.EffectiveView.CoEdgeOps:
                """Grouped coedge effective queries."""

        class EditorView:
            """
            Cache mutation surface. Mutates the BRepGraphMesh cache only - does not
            touch persistent definition data. Persistent rep creation/edit lives on
            `BRepGraph::Editor().Edges()`, `BRepGraph::Editor().CoEdges()`,
            `BRepGraph::Editor().Faces()`.
            """

            def __init__(self, theOther: BRepGraph.MeshView.EditorView) -> None: ...

            class FaceOps:
                def __init__(self, theOther: BRepGraph.MeshView.EditorView.FaceOps) -> None: ...

                def SetCachedTriangulation(self, theFace: BRepGraph_FaceId, theTriangulation: nanoocp.Poly.Poly_Triangulation | None) -> None:
                    """
                    Set the cached triangulation for a face.
                    @param[in] theFace         typed face definition identifier
                    @param[in] theTriangulation triangulation to store (null clears)
                    """

                def Clear(self, theFace: BRepGraph_FaceId) -> None:
                    """
                    Clear the face's cached mesh entry (no effect if absent).
                    @param[in] theFace typed face definition identifier
                    """

            class EdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.EditorView.EdgeOps) -> None: ...

                def SetCachedPolygon3D(self, theEdge: BRepGraph_EdgeId, thePolygon3D: nanoocp.Poly.Poly_Polygon3D | None) -> None:
                    """
                    Bind a Polygon3D to the edge's cached entry.
                    @param[in] theEdge     typed edge definition identifier
                    @param[in] thePolygon3D polygon-3D handle (null clears the cached binding)
                    """

                def Clear(self, theEdge: BRepGraph_EdgeId) -> None:
                    """
                    Clear the edge's cached mesh entry.
                    @param[in] theEdge typed edge definition identifier
                    """

            class CoEdgeOps:
                def __init__(self, theOther: BRepGraph.MeshView.EditorView.CoEdgeOps) -> None: ...

                def AppendCachedPolygonOnTri(self, theCoEdge: BRepGraph_CoEdgeId, thePolygonOnTri: nanoocp.Poly.Poly_PolygonOnTriangulation | None) -> None:
                    """
                    Append a polygon-on-triangulation to the coedge's cached list.
                    @param[in] theCoEdge    typed coedge definition identifier
                    @param[in] thePolygonOnTri polygon-on-tri to append
                    """

                def SetCachedPolygon2D(self, theCoEdge: BRepGraph_CoEdgeId, thePolygon2D: nanoocp.Poly.Poly_Polygon2D | None) -> None:
                    """
                    Bind a polygon-2D to the coedge's cached entry.
                    @param[in] theCoEdge   typed coedge definition identifier
                    @param[in] thePolygon2D polygon-2D handle (null clears the cached binding)
                    """

                def Clear(self, theCoEdge: BRepGraph_CoEdgeId) -> None:
                    """
                    Clear the coedge's cached mesh entry.
                    @param[in] theCoEdge typed coedge definition identifier
                    """

            def Faces(self) -> BRepGraph.MeshView.EditorView.FaceOps:
                """Grouped face cache mutations."""

            def Edges(self) -> BRepGraph.MeshView.EditorView.EdgeOps:
                """Grouped edge cache mutations."""

            def CoEdges(self) -> BRepGraph.MeshView.EditorView.CoEdgeOps:
                """Grouped coedge cache mutations."""

            def PromoteToPersistent(self) -> None:
                """
                Promote all currently fresh default-slot cache mesh entries to persistent mesh reps.
                """

        class PolyOps:
            """@brief Polygonal and triangulation count queries."""

            def __init__(self, theOther: BRepGraph.MeshView.PolyOps) -> None: ...

            def NbFaceTriangulations(self) -> int:
                """Total number of face triangulation slots (including removed)."""

            def NbEdgePolygons3D(self) -> int:
                """Total number of edge polygon-3D slots (including removed)."""

            def NbCoEdgePolygons2D(self) -> int:
                """Total number of coedge polygon-2D slots (including removed)."""

            def NbCoEdgePolygonsOnTri(self) -> int:
                """
                Total number of coedge polygon-on-triangulation slots (including removed).
                """

            def NbActiveTriangulations(self) -> int:
                """Number of non-removed face triangulation entries."""

            def NbActivePolygons3D(self) -> int:
                """Number of non-removed edge polygon-3D entries."""

            def NbActivePolygons2D(self) -> int:
                """Number of non-removed coedge polygon-2D entries."""

            def NbActivePolygonsOnTri(self) -> int:
                """Number of non-removed coedge polygon-on-triangulation entries."""

        def Cache(self) -> BRepGraph.MeshView.CacheView:
            """Cache-only reads."""

        def Persistent(self) -> BRepGraph.MeshView.PersistentView:
            """Persistent (definition-resident) reads."""

        def Effective(self) -> BRepGraph.MeshView.EffectiveView:
            """
            Effective reads - cache first, persistent fallback. Use when source is irrelevant.
            """

        def Editor(self) -> BRepGraph.MeshView.EditorView:
            """Cache mutations."""

        def Poly(self) -> BRepGraph.MeshView.PolyOps:
            """Polygon/triangulation count queries."""

    class ShapesView:
        """
        @brief View for TopoDS_Shape ingestion, reconstruction and lookup.

        Reconstructs TopoDS shapes from graph nodes on demand, with caching
        for repeated access. Topology nodes are delegated to the incidence-table
        reconstruction backend, while Product / Occurrence nodes are assembled at
        the facade level using product-local roots and occurrence placement chains.
        Provides lookup from construction-time shapes back to their graph NodeIds
        using OCCT shape identity (TShape + Location, orientation ignored).
        Shape() is the stable cached public
        route for repeated access; Reconstruct() forces a fresh rebuild with the
        same node-kind semantics and bypasses the persistent reconstructed-shape cache.
        Add() and Compact() clear the persistent reconstructed-shape cache.
        Obtained via BRepGraph::Shapes().
        """

        def __init__(self, theOther: BRepGraph.ShapesView) -> None: ...

        class AddStatus(enum.Enum):
            """Status of a single Add() call."""

            Success = 0

            SuccessWithWarnings = 1

            Failed = 2

        class Options:
            """Shape-ingestion options."""

            @overload
            def __init__(self) -> None: ...

            @overload
            def __init__(self, theOther: BRepGraph.ShapesView.Options) -> None: ...

            @property
            def Populate(self) -> nanoocp.BRepGraphInc.BRepGraphInc_Populate.Options: ...

            @Populate.setter
            def Populate(self, arg: nanoocp.BRepGraphInc.BRepGraphInc_Populate.Options, /) -> None: ...

            @property
            def CreateAutoProduct(self) -> bool:
                """wrap topology root in a Product (unparented Add only)"""

            @CreateAutoProduct.setter
            def CreateAutoProduct(self, arg: bool, /) -> None: ...

            @property
            def Flatten(self) -> bool:
                """drop hierarchy containers, append faces as roots"""

            @Flatten.setter
            def Flatten(self, arg: bool, /) -> None: ...

            @property
            def Parallel(self) -> bool:
                """run face-level construction in parallel"""

            @Parallel.setter
            def Parallel(self, arg: bool, /) -> None: ...

            @property
            def TrackAddedNodes(self) -> bool:
                """
                Capture every input subshape's NodeId in Result::AddedNodes.  Off by
                default so the hot path pays nothing.  Used by algorithm wrappers
                (Booleans, fillets, ...) that need to translate TopoDS_Shape objects
                returned by an OCCT algorithm into graph NodeIds for history harvest.
                """

            @TrackAddedNodes.setter
            def TrackAddedNodes(self, arg: bool, /) -> None: ...

        class Result:
            """Outcome of a single Add() call."""

            @overload
            def __init__(self) -> None: ...

            @overload
            def __init__(self, theOther: BRepGraph.ShapesView.Result) -> None: ...

            def IsOk(self) -> bool:
                """True if the build succeeded (with or without warnings)."""

            @property
            def TopologyRoot(self) -> BRepGraph_NodeId: ...

            @TopologyRoot.setter
            def TopologyRoot(self, arg: BRepGraph_NodeId, /) -> None: ...

            @property
            def Product(self) -> BRepGraph_ProductId: ...

            @Product.setter
            def Product(self, arg: BRepGraph_ProductId, /) -> None: ...

            @property
            def Occurrence(self) -> BRepGraph_OccurrenceId: ...

            @Occurrence.setter
            def Occurrence(self, arg: BRepGraph_OccurrenceId, /) -> None: ...

            @property
            def InsertedRef(self) -> BRepGraph_RefId: ...

            @InsertedRef.setter
            def InsertedRef(self, arg: BRepGraph_RefId, /) -> None: ...

            @property
            def Status(self) -> BRepGraph.ShapesView.AddStatus: ...

            @Status.setter
            def Status(self, arg: BRepGraph.ShapesView.AddStatus, /) -> None: ...

            @property
            def AddedNodes(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher]:
                """
                Populated only when Options::TrackAddedNodes is true.  Maps every
                subshape of the input @c theShape (including the root) to the
                BRepGraph_NodeId it resolves to after the Add.  Multiple input
                shapes that share identity collapse to one entry, as in OCCT's
                map types.
                """

            @AddedNodes.setter
            def AddedNodes(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], /) -> None: ...

        @overload
        def Add(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> BRepGraph.ShapesView.Result:
            """
            Ingest a TopoDS_Shape as a new root subgraph, wrapping the topology root in a Product.
            @param[in] theShape shape to ingest
            @return Result with TopologyRoot, Product and Occurrence set on success.
            """

        @overload
        def Add(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theOptions: BRepGraph.ShapesView.Options) -> BRepGraph.ShapesView.Result:
            """
            Ingest a TopoDS_Shape as a new root subgraph with explicit options.
            @param[in] theShape   shape to ingest
            @param[in] theOptions shape-ingestion options
            @return Result with TopologyRoot set on success; Product/Occurrence set
            when theOptions.CreateAutoProduct is true.
            """

        @overload
        def Add(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theParent: BRepGraph_NodeId) -> BRepGraph.ShapesView.Result:
            """
            Ingest a TopoDS_Shape under an existing parent.

            Parent kind dispatch:
            - Product:   creates a child part-product, links via Occurrence with shape.Location().
            - Compound:  appends topology root as a child reference.
            - Shell:     appends a Face as a FaceRef; other shapes via AddChild.
            - Solid:     appends a Shell as a ShellRef; other shapes via AddChild.
            - CompSolid: appends a Solid as a SolidRef.
            Other parent kinds (Wire, Edge, Vertex, Occurrence) are not supported and yield
            an invalid Result (Result::Ok == false) without modification to the graph.
            @param[in] theShape  shape to ingest
            @param[in] theParent parent node receiving the topology
            @return Result with TopologyRoot set, plus (Product, Occurrence, InsertedRef) for Product
            parents or InsertedRef for topology container parents.
            """

        @overload
        def Add(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theParent: BRepGraph_NodeId, theOptions: BRepGraph.ShapesView.Options) -> BRepGraph.ShapesView.Result:
            """
            Ingest a shape under an existing parent with explicit options.
            Options::CreateAutoProduct is ignored.
            """

        def CollectHistoryInputs(self, theRoots: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theOutInputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
            """
            Collect a TopoDS_Shape -> NodeId map for graph roots and all subshapes
            resolvable through FindNode().  This is intended for algorithms that
            reconstruct selected graph roots to TopoDS, run OCCT, and then need to
            translate BRepTools_History back to graph NodeIds.
            """

        @overload
        def AddWithHistory(self, theResultShape: nanoocp.TopoDS.TopoDS_Shape, theInputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], theHistory: nanoocp.BRepTools.BRepTools_History | None, theOpLabel: nanoocp.TCollection.TCollection_AsciiString) -> BRepGraph.ShapesView.Result:
            """
            Add an OCCT algorithm result and absorb BRepTools_History into the
            registered BRepGraph_LayerHistory layer using explicit input shape mapping.
            """

        @overload
        def AddWithHistory(self, theResultShape: nanoocp.TopoDS.TopoDS_Shape, theInputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], theHistory: nanoocp.BRepTools.BRepTools_History | None, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOptions: BRepGraph.ShapesView.Options) -> BRepGraph.ShapesView.Result:
            """
            Add an OCCT algorithm result and absorb BRepTools_History with explicit options.
            """

        @overload
        def AddWithHistory(self, theResultShape: nanoocp.TopoDS.TopoDS_Shape, theInputRoots: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theHistory: nanoocp.BRepTools.BRepTools_History | None, theOpLabel: nanoocp.TCollection.TCollection_AsciiString) -> BRepGraph.ShapesView.Result:
            """
            Convenience overload that collects the history input map from selected roots.
            """

        @overload
        def AddWithHistory(self, theResultShape: nanoocp.TopoDS.TopoDS_Shape, theInputRoots: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theHistory: nanoocp.BRepTools.BRepTools_History | None, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOptions: BRepGraph.ShapesView.Options) -> BRepGraph.ShapesView.Result:
            """
            Convenience overload that collects the history input map from selected roots
            and uses explicit options.
            """

        def Shape(self, theNode: BRepGraph_NodeId) -> nanoocp.TopoDS.TopoDS_Shape:
            """
            Return or reconstruct a TopoDS_Shape for a node.
            Prefer this route for repeated public queries.
            Returns a cached shape when available and valid; otherwise reconstructs.
            Topology definition nodes (Vertex..CompSolid) reconstruct their topology
            directly, without assembly wrappers.
            Product nodes are reconstructed in product-local coordinates.
            Occurrence nodes are reconstructed with cumulative occurrence placement.
            @param[in] theNode node identifier
            @return corresponding TopoDS_Shape, or null shape for invalid/removed nodes
            """

        def HasOriginal(self, theNode: BRepGraph_NodeId) -> bool:
            """
            Check if the node has an original shape from graph construction.
            Editor-created and mutation-derived nodes have no original.
            @param[in] theNode node identifier
            @return true if an original shape exists
            """

        def Original(self, theNode: BRepGraph_NodeId) -> nanoocp.TopoDS.TopoDS_Shape:
            """
            Return the original TopoDS_Shape stored during graph construction.
            @param[in] theNode node identifier
            @return original shape for an active node, or null shape when absent/invalid/removed
            """

        def Reconstruct(self, theRoot: BRepGraph_NodeId) -> nanoocp.TopoDS.TopoDS_Shape:
            """
            Reconstruct a TopoDS_Shape from a graph node without using the persistent cache.
            Use this when the caller explicitly needs a fresh rebuild instead of the
            shared cached shape returned by Shape(). This method does not populate the
            persistent reconstructed-shape cache.
            Topology definition nodes reconstruct topology directly.
            Product nodes are reconstructed in product-local coordinates.
            Occurrence nodes are reconstructed with cumulative occurrence placement.
            @param[in] theRoot definition node identifier
            @return reconstructed shape, or null shape for invalid/removed nodes
            """

        @overload
        def ClearCached(self, theNode: BRepGraph_NodeId) -> None:
            """
            Remove the cached reconstructed shape for one node.
            Does not change graph generation counters and does not rebuild the shape.
            Invalid or removed nodes are ignored.
            """

        @overload
        def ClearCached(self, theRef: BRepGraph_RefId) -> None:
            """
            Remove the cached reconstructed shape for the node referenced by one reference.
            Does not change graph generation counters and does not rebuild the shape.
            Invalid or removed references are ignored.
            """

        def FindNode(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> BRepGraph_NodeId:
            """
            Look up the definition NodeId for a shape from graph construction input.
            Uses OCCT IsSame() semantics (TShape + Location, orientation ignored).
            Synthetic Product / Occurrence reconstructions are not given dedicated
            TShape bindings, so lookup is only guaranteed for construction-time topology.
            Programmatically created Editor().Add*() nodes can still be located by
            UID or by direct iteration over Topo() definitions.
            @param[in] theShape shape to look up
            @return active node identifier, or invalid NodeId if the shape is absent or removed
            """

        def HasNode(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
            """
            Check if a shape is known to the graph (was part of construction input).
            Uses OCCT IsSame() semantics (TShape + Location, orientation ignored).
            Synthetic Product / Occurrence reconstructions are not given dedicated
            TShape bindings, so this is only guaranteed for construction-time topology.
            Programmatically created Editor().Add*() nodes can still be located by
            UID or by direct iteration over Topo() definitions.
            @param[in] theShape shape to check
            @return true if the shape has a corresponding active definition node
            """

        def RemoveShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
            """
            Remove the active graph node corresponding to a construction-time shape.
            This is the convenience equivalent of FindNode(theShape) followed by
            Editor().Gen().RemoveNode(node).
            @param[in] theShape shape to remove
            @return true when an active node was found and removed
            """

    class UIDsView:
        """
        @brief Read-only view for persistent node and reference identifiers.

        UIDs are (Kind, Counter) pairs that persist across graph mutations
        (Compact, node removal). Counters are monotonic and independent of vector
        indices. Clear() starts a new graph generation and refreshes the graph
        GUID, enabling stale-reference detection when a graph is rebuilt.
        Provides bidirectional NodeId/UID and RefId/RefUID resolution.

        Version stamps are exposed here for graph-owned cache and layer freshness
        checks. They reuse node/reference UID identity and do not introduce a
        persistent representation identity.
        """

        def __init__(self, theOther: BRepGraph.UIDsView) -> None: ...

        @overload
        def Of(self, theNode: BRepGraph_NodeId) -> BRepGraph_UID:
            """
            Return the UID assigned to a node.
            @param[in] theNode node identifier
            @return UID for the active node, or invalid UID if theNode is out of bounds or removed
            """

        @overload
        def Of(self, theRefId: BRepGraph_RefId) -> BRepGraph_RefUID:
            """
            Return the RefUID assigned to a reference.
            @param[in] theRefId reference identifier
            @return RefUID for the active reference, or invalid RefUID if theRefId is out of bounds or
            removed
            """

        @overload
        def Of(self, theItem: BRepGraph_ItemId) -> BRepGraph_ItemUID:
            """
            Return the persistent UID assigned to a generic graph item.
            @param[in] theItem definition-node or reference-entry item id
            @return durable item UID, or invalid UID if the item is out of bounds or removed
            """

        def NodeIdFrom(self, theUID: BRepGraph_UID) -> BRepGraph_NodeId:
            """
            Resolve a UID back to a NodeId using the internal reverse index.
            @param[in] theUID unique identifier to resolve
            @return corresponding active NodeId, or invalid NodeId if not found/removed
            """

        def RefIdFrom(self, theUID: BRepGraph_RefUID) -> BRepGraph_RefId:
            """
            Resolve a RefUID back to a RefId using the internal reverse index.
            @param[in] theUID unique reference identifier to resolve
            @return corresponding active RefId, or invalid RefId if not found/removed
            """

        def ItemIdFrom(self, theUID: BRepGraph_ItemUID) -> BRepGraph_ItemId:
            """
            Resolve a generic item UID back to a transient item id.
            @param[in] theUID durable node/reference item identity
            @return active item id, or invalid item id if the UID cannot be resolved
            """

        @overload
        def Has(self, theUID: BRepGraph_UID) -> bool:
            """
            Check if a UID is valid and exists in this graph generation.
            @param[in] theUID unique identifier to check
            @return true if the UID resolves to an active node in this graph generation
            """

        @overload
        def Has(self, theUID: BRepGraph_RefUID) -> bool:
            """
            Check if a RefUID is valid and exists in this graph generation.
            @param[in] theUID unique reference identifier to check
            @return true if the RefUID resolves to an active reference in this graph generation
            """

        @overload
        def Has(self, theUID: BRepGraph_ItemUID) -> bool:
            """Check if a generic item UID exists in this graph generation."""

        def Generation(self) -> int:
            """
            Return the current generation counter (incremented on each BRepGraph::Clear()).
            @return graph generation number
            """

        def GraphGUID(self) -> nanoocp.Standard.Standard_GUID:
            """
            Return the graph-level identity GUID.
            Generated randomly at BRepGraph::Clear() time; changes on each rebuild.
            @return reference to the graph identity GUID
            """

        @overload
        def StampOf(self, theNode: BRepGraph_NodeId) -> BRepGraph_VersionStamp:
            """
            Produce a version stamp for the given node.
            Combines the node's UID with its current OwnGen and graph Generation.
            @param[in] theNode node identifier
            @return version stamp, or invalid stamp if theNode is invalid, removed, or out of bounds
            """

        @overload
        def StampOf(self, theRefId: BRepGraph_RefId) -> BRepGraph_VersionStamp:
            """
            Produce a version stamp for the given reference.
            Combines the reference's RefUID with its current OwnGen and graph Generation.
            @param[in] theRefId reference identifier
            @return version stamp, or invalid stamp if theRefId is invalid, removed, or out of bounds
            """

        @overload
        def StampOf(self, theRepId: nanoocp.BRepGraphInc.BRepGraph_RepId) -> BRepGraph_VersionStamp:
            """
            Produce a version stamp for an owner-scoped use record.
            Use records have no durable UID or mutation generation; the stamp uses the owning
            definition-node UID, OwnGen, and graph Generation.
            @param[in] theRepId use-record identifier
            @return version stamp, or invalid stamp if theRepId is invalid, removed, or out of bounds
            """

        @overload
        def StampOf(self, theItem: BRepGraph_ItemId) -> BRepGraph_VersionStamp:
            """
            Produce a version stamp for the given definition-node or reference-entry item.
            """

        def IsStale(self, theStamp: BRepGraph_VersionStamp) -> bool:
            """
            Check if a previously-taken stamp is stale.
            A stamp is stale when the stamped item has been mutated,
            removed, or the graph was rebuilt since the stamp was taken.
            @param[in] theStamp version stamp to check
            @return true if the stamp no longer matches the current graph state
            """

    def Clear(self) -> None:
        """
        Reset the graph to an empty state. Increments generation and regenerates the graph GUID.
        """

    def IsEmpty(self) -> bool:
        """Return true when the graph contains no topology definitions."""

    def ValidateRelations(self) -> bool:
        """
        Verify relation consistency against entity / reference-entry tables.
        Intended for debug builds and regression tests of incremental mutation paths.
        @return true when every stored relation matches its endpoints.
        """

    def RootProductIds(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ProductId]:
        """
        Return root product identifiers (products not referenced by any active occurrence).
        Maintained incrementally by Editor/EditorView mutations.
        Returns empty vector if the graph has not been built.
        """

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator:
        """Return the current allocator."""

    def IsValid(self) -> bool:
        """Return true when this wrapper references graph data."""

    def IsNull(self) -> bool:
        """Return true when this wrapper does not reference graph data."""

    def Topo(self) -> BRepGraph.TopoView:
        """
        Access topology definitions, representation access, adjacency queries,
        raw Product/Occurrence definition storage, and assembly classification.
        """

    def UIDs(self) -> BRepGraph.UIDsView:
        """Access unique identifiers."""

    def Refs(self) -> BRepGraph.RefsView:
        """Access reference entries and their UIDs."""

    def Shapes(self) -> BRepGraph.ShapesView:
        """Access cached and fresh shape reconstruction."""

    def Editor(self) -> BRepGraph.EditorView:
        """Access programmatic graph construction and mutation."""

    def Mesh(self) -> BRepGraph.MeshView:
        """
        Non-const access to mesh view (required to call Editor() sub-view for cache mutations).
        @return mutable mesh view
        """

    def LayerRegistry(self) -> BRepGraph_LayerRegistry:
        """
        Access registered graph layers.
        @return layer registry for managing attribute layers
        """

    def CacheRegistry(self) -> BRepGraph_CacheRegistry:
        """
        Access registered graph cache services.
        @return cache registry for managing typed transient cache services
        """

class BRepGraph_Cache(nanoocp.Standard.Standard_Transient):
    """
    @brief Lightweight owner-bound base for transient graph cache services.

    A cache service stores typed, recomputable, graph-local data such as
    bounding boxes, UV bounds, or display-resolution results. The registry owns
    only service identity and lifetime binding; concrete caches own their own
    typed storage and validate freshness lazily via graph generation counters.
    """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Cache service identity, unique within a graph registry."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Cache service display name."""

    def Clear(self) -> None:
        """Clear all transient data owned by this cache."""

    def CopyFreshTo(self, theCopy: BRepGraph_CopyRemap) -> None:
        """
        Copy fresh, remappable cache data into the target graph described by the remap.
        Default implementation copies nothing.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_CacheDerivedState(BRepGraph_Cache):
    """
    @brief Cache for derived edge, wire, and shell properties.

    Each query is independent and caches only its own result.
    Callers request specific values (IsDegenerated, SameParameter, etc.)
    and the cache computes + stores only what is needed.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the unique cache service GUID."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the unique cache service GUID."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the cache service display name."""

    def Clear(self) -> None:
        """Clears all cached entries."""

    def CopyFreshTo(self, theCopy: BRepGraph_CopyRemap) -> None:
        """Copy fresh, remappable derived-state entries into the target graph."""

    def IsDegenerated(self, theEdge: BRepGraph_EdgeId) -> bool:
        """
        @brief Test if an edge is degenerate (no 3D curve and vertex collapse).
        Computes and caches only Status - does NOT compute SameParameter/SameRange.
        @param[in] theEdge edge definition identifier
        @return true if the edge is degenerate
        """

    def SameParameter(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
        """
        @brief Test if a single coedge has SameParameter.
        @param[in] theCoEdge coedge definition identifier
        @return true if the coedge has SameParameter
        """

    def SameRange(self, theCoEdge: BRepGraph_CoEdgeId) -> bool:
        """
        @brief Test if a single coedge has SameRange.
        @param[in] theCoEdge coedge definition identifier
        @return true if the coedge has SameRange
        """

    def IsClosed(self, theEdge: BRepGraph_EdgeId) -> bool:
        """
        @brief Test if an edge is closed (start vertex == end vertex).
        Computes and caches only IsClosed.
        @param[in] theEdge edge definition identifier
        @return true if the edge is closed
        """

    def GetWireIsClosed(self, theWire: BRepGraph_WireId) -> tuple[bool, bool]:
        """
        @brief Return wire closure, computing and storing a fresh entry.
        @param[in]  theWire   wire definition identifier
        @param[out] theClosed filled with the fresh derived value
        @return true if computation succeeded
        """

    def SetWireIsClosed(self, theWire: BRepGraph_WireId, theClosed: bool) -> None:
        """
        @brief Store a pre-computed wire closure value.
        @param[in] theWire   wire definition identifier
        @param[in] theClosed pre-computed closure value
        """

    def IsShellClosed(self, theShell: BRepGraph_ShellId) -> bool:
        """
        @brief Test if a shell is closed.
        @param[in] theShell shell definition identifier
        @return true if the shell is closed
        """

    @staticmethod
    def ComputeEdgeProperties(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> tuple[bool, bool, bool]:
        """
        Compute edge-own derived state (Status, IsClosed).
        SameRange/SameParameter are per-CoEdge - use the per-CoEdge cache directly.
        @param[in]  theGraph source graph
        @param[in]  theEdge  edge definition identifier
        @param[out] theIsDegenerated true if edge is degenerate
        @param[out] theIsClosed      true if edge is closed
        @return true if computation succeeded
        """

    @staticmethod
    def ComputeShellIsClosed(theGraph: BRepGraph, theShell: BRepGraph_ShellId) -> bool:
        """
        Compute shell closure directly from a BRepGraph without caching.
        @param[in] theGraph source graph
        @param[in] theShell shell definition identifier
        @return true if the shell is closed
        """

    @staticmethod
    def ComputeWireIsClosed(theGraph: BRepGraph, theWire: BRepGraph_WireId) -> bool:
        """
        Compute wire closure directly from a BRepGraph without caching.
        @param[in] theGraph source graph
        @param[in] theWire  wire definition identifier
        @return true if the wire is closed
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_ItemUID:
    """
    Durable BRepGraph item identity covering definition nodes and reference entries.

    BRepGraph_ItemId is a transient structural address. BRepGraph_ItemUID is the persistent
    identity assigned at item creation and kept stable across compaction and vector reordering.
    Representation/use records are not addressed here because they do not have persisted identity.
    """

    @overload
    def __init__(self) -> None:
        """Construct an invalid UID."""

    @overload
    def __init__(self, theOther: BRepGraph_ItemUID) -> None: ...

    class Domain(enum.Enum):
        """Addressed persistent identity domain."""

        Node = 1

        Reference = 2

    @staticmethod
    def Node(theKind: BRepGraph_NodeId.Kind, theCounter: int) -> BRepGraph_ItemUID:
        """Construct a node UID."""

    @staticmethod
    def Reference(theKind: BRepGraph_RefId.Kind, theCounter: int) -> BRepGraph_ItemUID:
        """Construct a reference UID."""

    @staticmethod
    def Invalid() -> BRepGraph_ItemUID:
        """Return an invalid sentinel UID."""

    def IsValid(self) -> bool:
        """
        Return true if this UID has a non-sentinel counter and a valid domain/kind pair.
        """

    def ItemDomain(self) -> BRepGraph_ItemUID.Domain:
        """Return the addressed identity domain."""

    def IsNode(self) -> bool: ...

    def IsReference(self) -> bool: ...

    def NodeKind(self) -> BRepGraph_NodeId.Kind:
        """Return node kind. Valid only for node UIDs."""

    def RefKind(self) -> BRepGraph_RefId.Kind:
        """Return reference kind. Valid only for reference UIDs."""

    def RawKind(self) -> int:
        """Return item kind encoded in its own domain enum space."""

    def Counter(self) -> int:
        """Return the graph-wide monotonic UID counter."""

    def HashValue(self) -> int:
        """Compute a hash value compatible with operator==."""

    def __eq__(self, arg: BRepGraph_ItemUID, /) -> bool: ...

    def __ne__(self, arg: BRepGraph_ItemUID, /) -> bool: ...

    def __lt__(self, arg: BRepGraph_ItemUID, /) -> bool: ...

    def __hash__(self) -> int: ...

class BRepGraph_CopyRemap:
    """
    Immutable context passed to layer copy callbacks.

    The structural copy algorithm owns remap construction. Layers receive this
    context and decide how to copy their own representation without exposing layer
    details back to BRepGraph_Copy.
    """

    @overload
    def __init__(self, theSourceGraph: BRepGraph, theTargetGraph: BRepGraph, theItemRemap: NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId, theMode: BRepGraph_CopyRemap.Mode) -> None: ...

    @overload
    def __init__(self, theSourceGraph: BRepGraph, theTargetGraph: BRepGraph, theMappingKind: BRepGraph_CopyRemap.MappingKind, theMode: BRepGraph_CopyRemap.Mode) -> None:
        """
        Identity-mapping constructor for full identity copy into an empty target.
        Source item ids are returned directly as target item ids after validation.
        """

    @overload
    def __init__(self, theOther: BRepGraph_CopyRemap) -> None: ...

    class Mode(enum.Enum):
        """Distinguishes copy vs. compact migration semantics."""

        Copy = 0

        Compact = 1

    class MappingKind(enum.Enum):
        """Distinguishes explicit item map vs. identity mapping."""

        Explicit = 0

        Identity = 1

    def CopyMode(self) -> BRepGraph_CopyRemap.Mode:
        """Migration mode of this context."""

    def IsCompact(self) -> bool:
        """True if this is a compaction migration (not a full copy)."""

    def SourceGraph(self) -> BRepGraph:
        """Source graph the copied layer is attached to."""

    def TargetGraph(self) -> BRepGraph:
        """Target graph whose structural contents have already been copied."""

    def TargetGraphConst(self) -> BRepGraph:
        """Target graph as const."""

    def Items(self) -> NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId:
        """
        Source item id -> target item id map for copied definitions, refs, and reps.
        """

    def TargetItem(self, theSourceItem: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """
        Return the target item for a source item, or an invalid item if not copied.
        """

    def TargetItemOrInvalid(self, theSourceItem: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """Return the target item for a source item, or an invalid item id."""

    def HasTargetItem(self, theSourceItem: BRepGraph_ItemId) -> bool:
        """Return true if the source item has a valid copied target item."""

    def SourceUID(self, theSourceItem: BRepGraph_ItemId) -> BRepGraph_ItemUID:
        """Return source UID for a source item."""

    def TargetUID(self, theTargetItem: BRepGraph_ItemId) -> BRepGraph_ItemUID:
        """Return target UID for a target item."""

    def TargetUIDFromSource(self, theSourceItem: BRepGraph_ItemId) -> BRepGraph_ItemUID:
        """Return target UID for a source item by source->target remap."""

class BRepGraph_CacheRegistry:
    """
    @brief GUID-keyed runtime registry of graph cache services.

    Stores registered cache services in a stable slot array for O(1) slot access
    and a GUID-to-slot map for lookup by stable public identity. Cache services
    own their typed transient data; this registry only manages identity and
    owner binding.
    """

    def __init__(self) -> None: ...

    def RegisterCache(self, theCache: BRepGraph_Cache | None) -> int:
        """
        Register a cache service. Replaces an existing cache with the same GUID.
        @param[in] theCache cache service
        @return graph-local slot index
        """

    def Register(self, theCache: BRepGraph_Cache | None) -> int:
        """
        Register a cache service. Short form used by graph-local cache operations.
        @param[in] theCache cache service
        @return graph-local slot index
        """

    def UnregisterCache(self, theGUID: nanoocp.Standard.Standard_GUID) -> None:
        """
        Remove a cache service by GUID.
        @param[in] theGUID cache identity
        """

    def FindCache(self, theGUID: nanoocp.Standard.Standard_GUID) -> BRepGraph_Cache:
        """
        Find a cache service by GUID.
        @param[in] theGUID cache identity
        @return cache service, or null handle if not found
        """

    @overload
    def FindSlot(self, theGUID: nanoocp.Standard.Standard_GUID) -> tuple[bool, int]:
        """
        Return current graph-local slot for a GUID.
        @param[in] theGUID cache family identity
        @param[out] theSlot graph-local slot index
        @return true if the cache service is registered
        """

    @overload
    def FindSlot(self, theCache: BRepGraph_Cache | None) -> tuple[bool, int]:
        """
        Return current graph-local slot for a cache service.
        @param[in] theCache cache service
        @param[out] theSlot graph-local slot index
        @return true if the cache service is registered
        """

    def Cache(self, theSlot: int) -> BRepGraph_Cache:
        """
        Return cache service by graph-local slot, or null handle if the slot is out of range.
        @param[in] theSlot graph-local cache slot
        """

    def NbCaches(self) -> int:
        """Number of registered cache services."""

    def CacheIter(self) -> BRepGraph_CacheIterator:
        """Iterate registered cache services."""

    def ClearAll(self) -> None:
        """Clear data in all registered cache services."""

    @overload
    def CopyFreshCachesTo(self, theTargetGraph: BRepGraph, theItemRemap: NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId, theMode: BRepGraph_CopyRemap.Mode) -> None:
        """
        Ask registered cache services to copy fresh, remappable data into the target graph.
        """

    @overload
    def CopyFreshCachesTo(self, theTargetGraph: BRepGraph, theMappingKind: BRepGraph_CopyRemap.MappingKind, theMode: BRepGraph_CopyRemap.Mode) -> None:
        """
        Ask registered cache services to copy fresh data using identity mapping.
        """

    def Clear(self) -> None:
        """Unregister all cache services."""

class BRepGraph_CacheIterator:
    """
    @brief Iterator over registered cache families in a BRepGraph_CacheRegistry.

    Supports OCCT More()/Next()/Value() pattern and STL range-for via begin()/end().
    """

    @overload
    def __init__(self, theRegistry: BRepGraph_CacheRegistry) -> None:
        """Construct an iterator over all cache families in the registry."""

    @overload
    def __init__(self, theOther: BRepGraph_CacheIterator) -> None: ...

    def __iter__(self) -> BRepGraph_CacheIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_Cache:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """True if the iterator has a current element."""

    def Next(self) -> None:
        """Advance to the next cache family."""

    def Value(self) -> BRepGraph_Cache:
        """Return the current cache family descriptor."""

    def Slot(self) -> int:
        """Return the current slot index in the registry."""

    def NbCaches(self) -> int:
        """Number of cache families in the registry."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Sentinel marking end of iteration."""

class BRepGraph_Layer(nanoocp.Standard.Standard_Transient):
    """
    @brief Abstract base class for named attribute layers.

    A layer groups per-node and per-reference metadata under a unique name with
    lifecycle callbacks. Layers are registered on BRepGraph and automatically
    notified when nodes or references are removed, remapped (compact), or modified.

    Derived layers store domain-specific data (names, colors, materials, etc.)
    in internal maps keyed by BRepGraph_NodeId or BRepGraph_RefId. The lifecycle
    callbacks ensure data consistency across all graph mutations.

    ## Node Modification Events
    Layers subscribe to node modification events by overriding SubscribedKinds()
    to return a non-zero bitmask of Kind values. When a subscribed node kind is
    modified, OnNodeModified() (immediate mode) or OnNodesModified() (deferred
    batch mode) is called. Layers with SubscribedKinds() == 0 (default) incur
    zero dispatch overhead.

    ## Reference Modification Events
    Layers subscribe to reference modification events by overriding
    SubscribedRefKinds() to return a non-zero bitmask of BRepGraph_RefId::Kind
    values. When a subscribed ref kind is mutated, OnRefModified() (immediate
    mode) or OnRefsModified() (deferred batch mode) is called. Removal is always
    dispatched via OnRefRemoved() regardless of subscription.

    ## Thread safety
    Callback dispatch is single-threaded (called from mutation paths).
    Layers that only provide read access can skip internal locking.

    @warning All lifecycle callbacks are declared noexcept. Derived
    implementations that throw will cause std::terminate. This is enforced
    by C++ language semantics for noexcept virtual overrides.
    """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Layer type identity (unique within a graph)."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Layer identity (unique within a graph)."""

    def OnNodeRemoved(self, theNode: BRepGraph_NodeId) -> None:
        """
        Called when a node is soft-removed without a replacement.
        @param[in] theNode the removed node
        Layers should discard or archive data associated with it.
        @warning Layer callbacks must not throw. They are called from noexcept
        notification paths (MutGuard destructors, deferred invalidation flush).
        """

    def OnItemRemoved(self, theItem: BRepGraph_ItemId) -> None:
        """
        Dispatch a generic item removal to the matching typed removal callback.
        This is a non-virtual convenience entry point; typed callbacks remain the
        extension points for derived layers.
        @param[in] theItem the removed definition or reference
        """

    def OnNodeReplaced(self, theOldNode: BRepGraph_NodeId, theNewNode: BRepGraph_NodeId) -> None:
        """
        Called when a node is soft-removed and replaced by another node.
        @param[in] theOldNode the removed node
        @param[in] theNewNode the node that replaces theOldNode
        Layers that store node-keyed data should migrate from
        theOldNode to theNewNode when the replacement kind is
        compatible. This is a structural lifecycle event, not an
        algorithmic history record.
        @warning Layer callbacks must not throw. They are called from noexcept
        notification paths (MutGuard destructors, deferred invalidation flush).
        """

    def CopyTo(self, theCopy: BRepGraph_CopyRemap) -> None:
        """
        Copy this source layer data into another graph.
        The source graph is the graph this layer is attached to (Graph()).
        @param[in] theCopy source graph, target graph, and source item id -> target item id remap
        @note Missing source items were not copied; persistent layers should skip dependent records.
        @note For BRepGraph_CopyRemap::Mode::Compact, the layer is being migrated in-place after
        structural compaction. UID/ItemUID records and ref/rep entries should be remapped through
        the item map. Stale entries (absent from the remap) should be dropped.
        @warning This callback may allocate and is intentionally not noexcept.
        """

    def InvalidateAll(self) -> None:
        """Mark all cached values dirty (bulk invalidation)."""

    def Clear(self) -> None:
        """Clear all stored data."""

    def SubscribedKinds(self) -> int:
        """
        Return a bitmask of BRepGraph_NodeId::Kind values this layer subscribes to.
        Only modification events matching subscribed kinds are dispatched.
        Default: 0 (no subscription - no modification events received).
        Override to receive OnNodeModified/OnNodesModified callbacks.
        The returned value must be constant for the lifetime of the layer.
        """

    def OnNodeModified(self, theNode: BRepGraph_NodeId) -> None:
        """
        Called in immediate (non-deferred) mode after a single node is modified.
        Only dispatched if the node's kind matches SubscribedKinds().
        Default: no-op.
        @param[in] theNode the modified node
        """

    def OnItemModified(self, theItem: BRepGraph_ItemId) -> None:
        """
        Dispatch a generic item modification to the matching typed modification callback.
        This is a non-virtual convenience entry point; typed callbacks remain the
        extension points for derived layers.
        @param[in] theItem the modified definition or reference
        """

    def OnNodesModified(self, theModifiedNodes: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId]) -> None:
        """
        Called after EndDeferredInvalidation() with all nodes modified during
        the deferred scope. Only dispatched if at least one modified node's kind
        matches SubscribedKinds(). The array may contain nodes of kinds not
        subscribed to - layers should filter internally if needed.
        Default: no-op.
        @param[in] theModifiedNodes all modified, non-removed nodes
        """

    @staticmethod
    def KindBit(theKind: BRepGraph_NodeId.Kind) -> int:
        """Convenience: return bitmask bit for a given Kind."""

    def SubscribedRefKinds(self) -> int:
        """
        Return a bitmask of BRepGraph_RefId::Kind values this layer subscribes to.
        Only modification events matching subscribed ref kinds are dispatched.
        Default: 0 (no subscription). Must be constant for the layer's lifetime.
        """

    def OnRefRemoved(self, theRef: BRepGraph_RefId) -> None:
        """
        Called when a reference is soft-deleted via RemoveRef().
        No replacement concept - refs are simply removed (unlike nodes which can have
        a replacement during sewing or deduplication). Dispatched to all layers
        regardless of SubscribedRefKinds().
        Default: no-op.
        @param[in] theRef the removed reference
        """

    def OnRefModified(self, theRef: BRepGraph_RefId) -> None:
        """
        Called in immediate (non-deferred) mode after a single ref is mutated.
        Only dispatched if the ref's kind matches SubscribedRefKinds().
        Default: no-op.
        @param[in] theRef the modified reference
        """

    def OnRefsModified(self, theModifiedRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_RefId]) -> None:
        """
        Called after EndDeferredInvalidation() with all refs modified during
        the deferred scope. Only dispatched if at least one modified ref's kind
        matches SubscribedRefKinds(). The array may contain refs of kinds not
        subscribed to - layers should filter internally if needed.
        Default: no-op.
        @param[in] theModifiedRefs all modified, non-removed refs
        """

    @staticmethod
    def RefKindBit(theKind: BRepGraph_RefId.Kind) -> int:
        """Convenience: return bitmask bit for a given RefId::Kind."""

    def Revision(self) -> int:
        """
        Monotonic revision counter incremented by touch() on every observable
        state change. Consumers compare stored revisions to detect staleness in O(1).
        Derived layers MUST call touch() from their mutators.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_LayerTopoSupplement(BRepGraph_Layer):
    """
    @brief Runtime-only storage for supplemental TopoDS topology fragments.

    This layer stores non-core topology extracted from a source shape and
    attached to supported core graph owners. These attachments are not
    serialized and are intended only to preserve live
    `TopoDS -> Graph -> TopoDS` behavior.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_LayerTopoSupplement) -> None: ...

    class AttachmentKind(enum.Enum):
        """@brief Semantic role of one supplemental attachment."""

        VertexSupplementShape = 0

        EdgeInternalVertex = 1

        FaceDirectVertex = 2

        SolidAuxShape = 3

        ShellAuxShape = 4

        CompSolidAuxShape = 5

        CompoundAuxShape = 6

        GenericSupplementShape = 7

    class Entry:
        """@brief Stored runtime attachment record."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_LayerTopoSupplement.Entry) -> None: ...

        @property
        def BaseOwner(self) -> BRepGraph_NodeId: ...

        @BaseOwner.setter
        def BaseOwner(self, arg: BRepGraph_NodeId, /) -> None: ...

        @property
        def LocalUid(self) -> int: ...

        @LocalUid.setter
        def LocalUid(self, arg: int, /) -> None: ...

        @property
        def Kind(self) -> BRepGraph_LayerTopoSupplement.AttachmentKind: ...

        @Kind.setter
        def Kind(self, arg: BRepGraph_LayerTopoSupplement.AttachmentKind, /) -> None: ...

        @property
        def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

        @Shape.setter
        def Shape(self, arg: nanoocp.TopoDS.TopoDS_Shape, /) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """@brief Return the fixed layer type GUID."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """@brief Return the runtime type GUID for this layer instance."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        @brief Return a short stable layer name for diagnostics and registry lookup.
        """

    def FindByUid(self, theUid: int) -> BRepGraph_LayerTopoSupplement.Entry:
        """
        @brief Find one attachment entry by its layer-local uid.
        @param[in] theUid layer-local attachment uid
        @return pointer to the entry, or `nullptr` when not found
        """

    def AttachedTo(self, theOwner: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector__unsigned_long_long:
        """
        @brief Return all attachment uids currently owned by one core node.
        @param[in] theOwner core topology owner node
        @return owner-local insertion-ordered list of attachment uids
        """

    def AddAttachment(self, theOwner: BRepGraph_NodeId, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind, theShape: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        @brief Add one supplemental shape attachment to a supported core owner node.
        Supported owner kinds are vertex, edge, face, shell, solid, compsolid, and compound.
        @param[in] theOwner active core topology owner
        @param[in] theKind semantic attachment kind
        @param[in] theShape attached supplemental shape
        @return non-zero layer-local uid on success, `0` on rejection
        """

    def AddAttachmentWithUid(self, theOwner: BRepGraph_NodeId, theUid: int, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        @brief Add one supplemental shape attachment with an explicitly preserved uid.
        Supported owner kinds are vertex, edge, face, shell, solid, compsolid, and compound.
        @param[in] theOwner active core topology owner
        @param[in] theUid layer-local attachment uid to preserve
        @param[in] theKind semantic attachment kind
        @param[in] theShape attached supplemental shape
        @return `true` on success, `false` when the uid or input is rejected
        """

    def RemoveAttachment(self, theUid: int) -> bool:
        """
        @brief Remove one supplemental attachment by uid.
        @param[in] theUid layer-local attachment uid
        @return `true` when the attachment existed and was removed
        """

    def Validate(self) -> None:
        """
        @brief Validate internal owner/uid bookkeeping invariants.
        @throws Standard_ProgramError on inconsistent internal state
        """

    def OnNodeRemoved(self, theNode: BRepGraph_NodeId) -> None:
        """
        @brief Drop all attachments owned by a removed node.
        @param[in] theNode removed core node
        """

    def OnNodeReplaced(self, theOldNode: BRepGraph_NodeId, theNewNode: BRepGraph_NodeId) -> None:
        """
        @brief Migrate attachments from one owner node to another compatible node.
        @param[in] theOldNode previous owner node
        @param[in] theNewNode replacement owner node
        """

    def CopyTo(self, theCopy: BRepGraph_CopyRemap) -> None:
        """@brief Copy remapped attachments to the target graph."""

    def InvalidateAll(self) -> None:
        """@brief Invalidate all cached state in the layer."""

    def Clear(self) -> None:
        """@brief Remove every stored supplemental attachment."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_SupplementEditor:
    """@brief Lightweight mutation facade for runtime supplement attachments."""

    @overload
    def __init__(self, theGraph: BRepGraph) -> None:
        """
        @brief Create an editor facade bound to one graph instance.
        @param[in] theGraph graph receiving supplement attachments
        """

    @overload
    def __init__(self, theOther: BRepGraph_SupplementEditor) -> None: ...

    def Attach(self, theOwner: BRepGraph_NodeId, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind, theShape: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        @brief Attach one supplemental shape to an arbitrary supported core owner.
        @param[in] theOwner active owner node
        @param[in] theKind semantic attachment kind
        @param[in] theShape supplemental shape to attach
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToVertex(self, theVertex: BRepGraph_VertexId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.VertexSupplementShape) -> int:
        """
        @brief Attach a supplemental shape to a vertex owner.
        @param[in] theVertex active vertex owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToEdge(self, theEdge: BRepGraph_EdgeId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.EdgeInternalVertex) -> int:
        """
        @brief Attach a supplemental shape to an edge owner.
        @param[in] theEdge active edge owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToFace(self, theFace: BRepGraph_FaceId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.FaceDirectVertex) -> int:
        """
        @brief Attach a supplemental shape to a face owner.
        @param[in] theFace active face owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToSolid(self, theSolid: BRepGraph_SolidId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.SolidAuxShape) -> int:
        """
        @brief Attach a supplemental shape to a solid owner.
        @param[in] theSolid active solid owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToCompSolid(self, theCompSolid: BRepGraph_CompSolidId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.CompSolidAuxShape) -> int:
        """
        @brief Attach a supplemental shape to a compsolid owner.
        @param[in] theCompSolid active compsolid owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToShell(self, theShell: BRepGraph_ShellId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.ShellAuxShape) -> int:
        """
        @brief Attach a supplemental shape to a shell owner.
        @param[in] theShell active shell owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def AttachToCompound(self, theCompound: BRepGraph_CompoundId, theShape: nanoocp.TopoDS.TopoDS_Shape, theKind: BRepGraph_LayerTopoSupplement.AttachmentKind = BRepGraph_LayerTopoSupplement.AttachmentKind.CompoundAuxShape) -> int:
        """
        @brief Attach a supplemental shape to a compound owner.
        @param[in] theCompound active compound owner
        @param[in] theShape supplemental shape to attach
        @param[in] theKind semantic attachment kind
        @return non-zero attachment uid on success, `0` on rejection
        """

    def RemoveAttachment(self, theUid: int) -> bool:
        """
        @brief Remove one attachment by uid.
        @param[in] theUid layer-local attachment uid
        @return `true` when the attachment existed and was removed
        """

class BRepGraph_VersionStamp:
    """
    @brief Snapshot of a graph item identity and its freshness generation.

    Combines a persistent node or reference UID with OwnGen (own-data mutation counter)
    and graph Generation (BRepGraph::Clear() cycle). It is intended for custom cache and
    layer freshness checks, not as a separate topology identity model.

    Usage pattern:
    @code
    BRepGraph_VersionStamp aStamp = aGraph.UIDs().StampOf(aFaceId);
    // ... later, after mutations ...
    if (aGraph.UIDs().IsStale(aStamp))
    recomputeDerivedData();
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor. Creates an invalid stamp (invalid UID, zero counters).
        """

    @overload
    def __init__(self, theUID: BRepGraph_UID, theMutationGen: int, theGeneration: int) -> None:
        """
        Construct a node-domain stamp from components.
        @param[in] theUID         persistent definition-node identity
        @param[in] theMutationGen OwnGen counter (own-data mutation counter)
        @param[in] theGeneration  graph BRepGraph::Clear() generation
        """

    @overload
    def __init__(self, theRefUID: BRepGraph_RefUID, theMutationGen: int, theGeneration: int) -> None:
        """
        Construct a reference-domain stamp from components.
        @param[in] theRefUID      persistent reference identity
        @param[in] theMutationGen OwnGen counter (own-data mutation counter)
        @param[in] theGeneration  graph BRepGraph::Clear() generation
        """

    @overload
    def __init__(self, theOther: BRepGraph_VersionStamp) -> None: ...

    class Domain(enum.Enum):
        """Identity domain encoded in this stamp."""

        Node = 1

        Reference = 2

    def IsValid(self) -> bool:
        """Check if the stamp has a valid identity in its domain."""

    def IsNodeStamp(self) -> bool:
        """True when this is a definition-node-domain stamp."""

    def IsRefStamp(self) -> bool:
        """True when this is a reference-domain stamp."""

    def ItemUID(self) -> BRepGraph_ItemUID:
        """Return the active generic item identity."""

    def __eq__(self, theOther: BRepGraph_VersionStamp) -> bool:
        """
        Full equality: same domain, UID, OwnGen, and Generation.
        Two invalid stamps are equal.
        """

    def __ne__(self, theOther: BRepGraph_VersionStamp) -> bool: ...

    def IsSameItem(self, theOther: BRepGraph_VersionStamp) -> bool:
        """
        Check if two stamps refer to the same graph item regardless of version.
        Compares active UID only, ignoring OwnGen and Generation.
        @param[in] theOther stamp to compare with
        @return true if both stamps have the same domain and UID
        """

    def ToGUID(self, theGraphGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_GUID:
        """
        Derive a deterministic Standard_GUID from this stamp.
        The graph GUID is incorporated into the hash, making per-node GUIDs
        globally unique across different graph instances.
        One-way: cannot reconstruct stamp fields from the resulting GUID.
        @param[in] theGraphGUID the owning graph's identity GUID
        @return deterministic Standard_GUID derived from stamp + graph GUID
        """

    def HashValue(self) -> int:
        """
        Compute hash value consistent with operator==.
        @return hash combining active UID, domain, OwnGen, and Generation
        """

    def __hash__(self) -> int: ...

    @property
    def myNodeUID(self) -> BRepGraph_UID:
        """Definition-node identity for node-domain stamps."""

    @myNodeUID.setter
    def myNodeUID(self, arg: BRepGraph_UID, /) -> None: ...

    @property
    def myRefUID(self) -> BRepGraph_RefUID:
        """Reference-entry identity for reference-domain stamps."""

    @myRefUID.setter
    def myRefUID(self, arg: BRepGraph_RefUID, /) -> None: ...

    @property
    def myMutationGen(self) -> int:
        """OwnGen counter at snapshot time."""

    @myMutationGen.setter
    def myMutationGen(self, arg: int, /) -> None: ...

    @property
    def myGeneration(self) -> int:
        """Graph BRepGraph::Clear() generation at snapshot time."""

    @myGeneration.setter
    def myGeneration(self, arg: int, /) -> None: ...

    @property
    def myDomain(self) -> BRepGraph_VersionStamp.Domain:
        """Active identity domain."""

    @myDomain.setter
    def myDomain(self, arg: BRepGraph_VersionStamp.Domain, /) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell__BRepGraphInc_ShellRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraphInc_ShellDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell__BRepGraphInc_ShellRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraphInc_ShellDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face__BRepGraphInc_FaceRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraphInc_FaceDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face__BRepGraphInc_FaceRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraphInc_FaceDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire__BRepGraphInc_WireRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraphInc_WireDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire__BRepGraphInc_WireRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraphInc_WireDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Edge__BRepGraphInc_EdgeDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Edge__BRepGraphInc_EdgeDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid__BRepGraphInc_SolidRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraphInc_SolidDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid__BRepGraphInc_SolidRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraphInc_SolidDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child__BRepGraphInc_ChildRef__BRepGraph_NodeId__BRepGraphInc_BaseDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child__BRepGraphInc_ChildRef__BRepGraph_NodeId__BRepGraphInc_BaseDef) -> None: ...

class BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence__BRepGraphInc_OccurrenceRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Occurrence__BRepGraphInc_OccurrenceDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence__BRepGraphInc_OccurrenceRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Occurrence__BRepGraphInc_OccurrenceDef) -> None: ...

class BRepGraph_DefsShellOfSolid:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_SolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsShellOfSolid) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_ShellId: ...

    def Current(self) -> nanoocp.BRepGraphInc.ShellDef: ...

    def CurrentRefId(self) -> BRepGraph_ShellRefId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsFaceOfShell:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_ShellId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsFaceOfShell) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_FaceId: ...

    def Current(self) -> nanoocp.BRepGraphInc.FaceDef: ...

    def CurrentRefId(self) -> BRepGraph_FaceRefId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsEdgeOfWire:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_WireId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsEdgeOfWire) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_EdgeId: ...

    def Current(self) -> nanoocp.BRepGraphInc.EdgeDef: ...

    def CurrentRefId(self) -> BRepGraph_CoEdgeId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsWireOfFace:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_FaceId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsWireOfFace) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_WireId: ...

    def Current(self) -> nanoocp.BRepGraphInc.WireDef: ...

    def CurrentRefId(self) -> BRepGraph_WireRefId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsCoEdgeOfWire:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_WireId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsCoEdgeOfWire) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_CoEdgeId: ...

    def Current(self) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

    def CurrentRefId(self) -> BRepGraph_CoEdgeId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsSolidOfCompSolid:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_CompSolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsSolidOfCompSolid) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_SolidId: ...

    def Current(self) -> nanoocp.BRepGraphInc.SolidDef: ...

    def CurrentRefId(self) -> BRepGraph_SolidRefId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsChildOfCompound:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_CompoundId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsChildOfCompound) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_NodeId: ...

    def Current(self) -> nanoocp.BRepGraphInc.BaseDef: ...

    def CurrentRefId(self) -> BRepGraph_ChildRefId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_DefsOccurrenceOfProduct:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_ProductId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_DefsOccurrenceOfProduct) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_OccurrenceId: ...

    def Current(self) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

    def CurrentRefId(self) -> BRepGraph_OccurrenceRefId:
        """
        Returns the reference/coedge entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_UsagePath:
    """
    Explicit identity of a concrete usage from traversal root to selected node.

    A usage path is an ordered sequence of steps that records the exact
    traversal from a root node down to a specific graph entity. Each step
    captures the node reached, the reference through which it was reached,
    and the sibling order (step index) at that level.

    Paths are used to disambiguate multiple occurrences of the same
    definition reachable through different references or sibling positions.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty usage path."""

    @overload
    def __init__(self, theCapacity: int) -> None:
        """
        Creates a usage path with pre-allocated capacity.
        @param[in] theCapacity number of steps to pre-allocate
        """

    @overload
    def __init__(self, theOther: BRepGraph_UsagePath) -> None: ...

    class Step:
        """
        One concrete traversal step in a usage path.

        Ref is valid for reference-owned links and invalid for structural links
        such as CoEdge -> Edge or Occurrence -> Product/topology-root. Step keeps
        sibling order explicit, so coincident or structurally-linked usages remain
        distinguishable without relying on location or hashes.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_UsagePath.Step) -> None: ...

        def __eq__(self, theOther: BRepGraph_UsagePath.Step) -> bool: ...

        @property
        def Node(self) -> BRepGraph_NodeId: ...

        @Node.setter
        def Node(self, arg: BRepGraph_NodeId, /) -> None: ...

        @property
        def Ref(self) -> BRepGraph_RefId: ...

        @Ref.setter
        def Ref(self, arg: BRepGraph_RefId, /) -> None: ...

        @property
        def StepIndex(self) -> int: ...

        @StepIndex.setter
        def StepIndex(self, arg: int, /) -> None: ...

    def Size(self) -> int:
        """Returns the number of steps in the path."""

    def IsEmpty(self) -> bool:
        """Returns true if the path has no steps."""

    def Value(self, theIdx: int) -> BRepGraph_UsagePath.Step:
        """
        Returns the step at the given index.
        @param[in] theIdx zero-based index
        """

    def First(self) -> BRepGraph_UsagePath.Step:
        """Returns the first step in the path."""

    def Last(self) -> BRepGraph_UsagePath.Step:
        """Returns the last step in the path."""

    def Append(self, theStep: BRepGraph_UsagePath.Step) -> None:
        """
        Appends a step to the end of the path.
        @param[in] theStep step to append
        """

    def InsertBefore(self, theIdx: int, theStep: BRepGraph_UsagePath.Step) -> None:
        """
        Inserts a step before the given index.
        @param[in] theIdx zero-based index to insert before
        @param[in] theStep step to insert
        """

    def Clear(self) -> None:
        """Removes all steps from the path."""

    def IsEqual(self, theOther: BRepGraph_UsagePath) -> bool:
        """
        Returns true if this path is equal to the other path.
        @param[in] theOther path to compare with
        """

    def __eq__(self, theOther: BRepGraph_UsagePath) -> bool:
        """
        Returns true if this path is equal to the other path.
        @param[in] theOther path to compare with
        """

    def HashCode(self) -> int:
        """
        Returns a hash code for this path.
        Uses first step, last step, and size for O(1) computation.
        """

    def __hash__(self) -> int: ...

class BRepGraph_ChildExplorer:
    """
    @brief Stack-based lazy downward hierarchy walker for BRepGraph with inline
    location/orientation accumulation.
    @see BRepGraph class comment "Iterator guide" for choosing between iterator types.

    Walks the graph hierarchy from a root node down to entities of a target kind,
    yielding one occurrence at a time via a depth-first stack. Location and
    orientation are composed incrementally during the walk, making
    Current().Location and Current().Orientation O(1) per call.

    The traversal follows the actual graph structure transparently - every node
    kind is visited as a distinct entity (no hidden collapses):
    Compound -> children,  CompSolid -> Solids,  Solid -> Shells,
    Shell -> Faces,  Face -> Wires (+direct Vertices),  Wire -> CoEdges,
    CoEdge -> Edge,  Edge -> Vertices,
    Product -> Occurrences, Occurrence -> Product/topology-root.

    Unlike flat definition traversal by typed ids, BRepGraph_ChildExplorer visits
    each occurrence. If Edge[5] is reachable through Face[0] and Face[1],
    it is visited twice with different accumulated transforms.

    ## Traversal modes
    - **Recursive**: depth-first walk through the full subgraph.
    Without target kind, all descendant nodes are emitted.
    With target kind, only matching nodes are emitted but intermediate
    levels are traversed to reach them.
    - **DirectChildren**: yields only the immediate children of the root.
    No descent into grandchildren.  With target kind, only children
    matching the kind are returned.
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId) -> None:
        """
        Explore all descendants of the root node using recursive traversal.
        @param[in] theGraph graph to walk
        @param[in] theRoot  root node where the walk begins
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theConfig: BRepGraph_ChildExplorer.Config) -> None:
        """
        Preferred long-term constructor: all tuning knobs in `Config`.
        @param[in] theGraph graph to walk
        @param[in] theRoot  root node where the walk begins
        @param[in] theConfig traversal configuration (mode, target kind, avoid kind, etc.)
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theMode: BRepGraph_ChildExplorer.TraversalMode) -> None:
        """
        Explore descendants of the root node using the given traversal mode.
        @param[in] theGraph graph to walk
        @param[in] theRoot  root node where the walk begins
        @param[in] theMode  traversal strategy (recursive or direct children)
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind) -> None:
        """
        Explore only descendants of the given target kind.
        @param[in] theGraph     graph to walk
        @param[in] theRoot      root node where the walk begins
        @param[in] theTargetKind kind of nodes to emit
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theProduct: BRepGraph_ProductId, theTargetKind: BRepGraph_NodeId.Kind) -> None:
        """
        Explore only descendants of the given target kind starting from a product.
        @param[in] theGraph     graph to walk
        @param[in] theProduct   product whose occurrences and topology are explored
        @param[in] theTargetKind kind of nodes to emit
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theAvoidKind: BRepGraph_NodeId.Kind | None, theEmitAvoidKind: bool, theMode: BRepGraph_ChildExplorer.TraversalMode = BRepGraph_ChildExplorer.TraversalMode.Recursive) -> None:
        """
        Explore descendants while pruning branches at the avoid kind.
        @param[in] theGraph        graph to walk
        @param[in] theRoot         root node where the walk begins
        @param[in] theAvoidKind    node kind to avoid descending into
        @param[in] theEmitAvoidKind if true, emit matching avoid-kind nodes once before skipping
        @param[in] theMode         traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind, theMode: BRepGraph_ChildExplorer.TraversalMode) -> None:
        """
        Explore only descendants of the given target kind using the given traversal mode.
        @param[in] theGraph     graph to walk
        @param[in] theRoot      root node where the walk begins
        @param[in] theTargetKind kind of nodes to emit
        @param[in] theMode      traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theProduct: BRepGraph_ProductId, theTargetKind: BRepGraph_NodeId.Kind, theMode: BRepGraph_ChildExplorer.TraversalMode) -> None:
        """
        Explore only descendants of the given target kind starting from a product,
        using the given traversal mode.
        @param[in] theGraph     graph to walk
        @param[in] theProduct   product whose occurrences and topology are explored
        @param[in] theTargetKind kind of nodes to emit
        @param[in] theMode      traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind, theAvoidKind: BRepGraph_NodeId.Kind | None, theEmitAvoidKind: bool, theMode: BRepGraph_ChildExplorer.TraversalMode = BRepGraph_ChildExplorer.TraversalMode.Recursive) -> None:
        """
        Explore descendants of the given target kind while pruning branches at the avoid kind.
        @param[in] theGraph        graph to walk
        @param[in] theRoot         root node where the walk begins
        @param[in] theTargetKind   kind of nodes to emit
        @param[in] theAvoidKind    node kind to avoid descending into
        @param[in] theEmitAvoidKind if true, emit matching avoid-kind nodes once before skipping
        @param[in] theMode         traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind, theCumLoc: bool, theCumOri: bool, theMode: BRepGraph_ChildExplorer.TraversalMode = BRepGraph_ChildExplorer.TraversalMode.Recursive) -> None:
        """
        Explore only descendants of the given target kind with explicit location/orientation control.
        @param[in] theGraph     graph to walk
        @param[in] theRoot      root node where the walk begins
        @param[in] theTargetKind kind of nodes to emit
        @param[in] theCumLoc    if true, accumulate location down the walk
        @param[in] theCumOri    if true, accumulate orientation down the walk
        @param[in] theMode      traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theProduct: BRepGraph_ProductId, theTargetKind: BRepGraph_NodeId.Kind, theCumLoc: bool, theCumOri: bool, theMode: BRepGraph_ChildExplorer.TraversalMode = BRepGraph_ChildExplorer.TraversalMode.Recursive) -> None:
        """
        Explore only descendants of the given target kind starting from a product,
        with explicit location/orientation control.
        @param[in] theGraph     graph to walk
        @param[in] theProduct   product whose occurrences and topology are explored
        @param[in] theTargetKind kind of nodes to emit
        @param[in] theCumLoc    if true, accumulate location down the walk
        @param[in] theCumOri    if true, accumulate orientation down the walk
        @param[in] theMode      traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theRoot: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind, theStartLoc: nanoocp.TopLoc.TopLoc_Location, theStartOri: nanoocp.TopAbs.TopAbs_Orientation, theMode: BRepGraph_ChildExplorer.TraversalMode = BRepGraph_ChildExplorer.TraversalMode.DirectChildren) -> None:
        """
        Explore only descendants of the given target kind with an explicit initial transform.
        @param[in] theGraph     graph to walk
        @param[in] theRoot      root node where the walk begins
        @param[in] theTargetKind kind of nodes to emit
        @param[in] theStartLoc  initial accumulated location
        @param[in] theStartOri  initial accumulated orientation
        @param[in] theMode      traversal strategy
        """

    class LinkKind(enum.Enum):
        """Relationship kind between Current() and CurrentParent()."""

        Reference = 1

        Structural = 2

    class TraversalMode(enum.Enum):
        """Downward traversal strategy."""

        Recursive = 0

        DirectChildren = 1

    class Config:
        """
        Consolidated configuration for the explorer.

        The `Config`-based constructor is the preferred idiom: new options can be
        added as fields without additional constructor overloads.

        @code
        BRepGraph_ChildExplorer::Config aConfig;
        aConfig.Mode        = BRepGraph_ChildExplorer::TraversalMode::DirectChildren;
        aConfig.TargetKind  = BRepGraph_NodeId::Kind::Face;
        aConfig.StartLoc    = aParentLocation;
        aConfig.StartOri    = TopAbs_REVERSED;
        for (auto [id, loc, ori] : BRepGraph_ChildExplorer(aGraph, aRoot, aConfig)) { ... }
        @endcode
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_ChildExplorer.Config) -> None: ...

        @property
        def Mode(self) -> BRepGraph_ChildExplorer.TraversalMode: ...

        @Mode.setter
        def Mode(self, arg: BRepGraph_ChildExplorer.TraversalMode, /) -> None: ...

        @property
        def TargetKind(self) -> BRepGraph_NodeId.Kind | None:
            """Emit only this kind (no value = emit all)."""

        @TargetKind.setter
        def TargetKind(self, arg: BRepGraph_NodeId.Kind | None, /) -> None: ...

        @property
        def AvoidKind(self) -> BRepGraph_NodeId.Kind | None:
            """Do not descend into this kind."""

        @AvoidKind.setter
        def AvoidKind(self, arg: BRepGraph_NodeId.Kind | None, /) -> None: ...

        @property
        def EmitAvoidKind(self) -> bool: ...

        @EmitAvoidKind.setter
        def EmitAvoidKind(self, arg: bool, /) -> None: ...

        @property
        def AccumulateLocation(self) -> bool:
            """Compose Location down the walk."""

        @AccumulateLocation.setter
        def AccumulateLocation(self, arg: bool, /) -> None: ...

        @property
        def AccumulateOrientation(self) -> bool:
            """Compose Orientation down the walk."""

        @AccumulateOrientation.setter
        def AccumulateOrientation(self, arg: bool, /) -> None: ...

        @property
        def StartLoc(self) -> nanoocp.TopLoc.TopLoc_Location:
            """Initial accumulated location."""

        @StartLoc.setter
        def StartLoc(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

        @property
        def StartOri(self) -> nanoocp.TopAbs.TopAbs_Orientation:
            """Initial accumulated orientation."""

        @StartOri.setter
        def StartOri(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

    def __iter__(self) -> BRepGraph_ChildExplorer:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraphInc_Instance__BRepGraph_NodeId:
        """Python addition: see __iter__."""

    def GetConfig(self) -> BRepGraph_ChildExplorer.Config:
        """
        Returns the traversal configuration this explorer was constructed with.
        Read-only - configuration is fixed for the lifetime of the explorer.
        """

    def More(self) -> bool:
        """True if another matching descendant is available."""

    def Next(self) -> None:
        """Advance to the next matching descendant."""

    def Current(self) -> BRepGraphInc_Instance__BRepGraph_NodeId:
        """
        Current matching descendant node with accumulated location and orientation.
        """

    def CurrentParent(self) -> BRepGraph_NodeId:
        """
        Returns the immediate parent of Current() in the explored path.
        Returns invalid NodeId when Current() is the root/self match.
        """

    def CurrentLinkKind(self) -> BRepGraph_ChildExplorer.LinkKind:
        """Returns how Current() is linked from CurrentParent()."""

    def CurrentRef(self) -> BRepGraph_RefId:
        """
        Returns the exact parent-owned RefId for Current(), when the current step
        is represented by a reference entry. Returns invalid RefId for structural
        links without a dedicated ref entry such as CoEdge->Edge,
        Occurrence->Product/topology-root.
        """

    def CurrentUsagePath(self) -> BRepGraph_UsagePath:
        """
        Returns the explicit concrete traversal path from the explorer root to Current().
        """

    def LocationOf(self, theKind: BRepGraph_NodeId.Kind) -> nanoocp.TopLoc.TopLoc_Location:
        """
        Returns the accumulated location at the most recent ancestor of the given kind.
        @param[in] theKind node kind to search for in the ancestor chain
        @return accumulated location at the matching ancestor
        """

    def NodeOf(self, theKind: BRepGraph_NodeId.Kind) -> BRepGraph_NodeId:
        """
        Returns the node id of the most recent ancestor of the given kind.
        @param[in] theKind node kind to search for in the ancestor chain
        @return node id of the matching ancestor
        """

    def LocationAt(self, theLevel: int) -> nanoocp.TopLoc.TopLoc_Location:
        """
        Returns the accumulated location at the given stack level.
        @param[in] theLevel zero-based stack depth (0 = root)
        @return accumulated location at the specified level
        """

    def NodeAt(self, theLevel: int) -> BRepGraph_NodeId:
        """
        Returns the node id at the given stack level.
        @param[in] theLevel zero-based stack depth (0 = root)
        @return node id at the specified level
        """

    def Depth(self) -> int:
        """
        Number of valid ancestor frames currently on the stack (excluding the
        sentinel below the root). O(1); avoids the O(depth^2) NodeAt(i) walk used
        to compute container priority in selection-mode building.
        """

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_SolidDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_SolidDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_SolidId) -> nanoocp.BRepGraphInc.SolidDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_ShellDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_ShellDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_ShellId) -> nanoocp.BRepGraphInc.ShellDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_FaceDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_FaceDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_FaceId) -> nanoocp.BRepGraphInc.FaceDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_WireDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_WireDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_WireId) -> nanoocp.BRepGraphInc.WireDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_EdgeDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_EdgeDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_EdgeId) -> nanoocp.BRepGraphInc.EdgeDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_VertexDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_VertexDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_VertexId) -> nanoocp.BRepGraphInc.VertexDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_ProductDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_ProductDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_ProductId) -> nanoocp.BRepGraphInc.ProductDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_OccurrenceDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_OccurrenceDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_OccurrenceId) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_CoEdgeDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_CoEdgeDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_CoEdgeId) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_CompoundDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_CompoundDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_CompoundId) -> nanoocp.BRepGraphInc.CompoundDef: ...

class BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_CompSolidDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_IteratorDetail_NodeTraits__BRepGraphInc_CompSolidDef) -> None: ...

    @staticmethod
    def Count(theGraph: BRepGraph) -> int: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_CompSolidId) -> nanoocp.BRepGraphInc.CompSolidDef: ...

class BRepGraph_SolidIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_SolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_SolidIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.SolidDef: ...

    def CurrentId(self) -> BRepGraph_SolidId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_ShellIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ShellId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ShellIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ShellDef: ...

    def CurrentId(self) -> BRepGraph_ShellId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FaceIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_FaceId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FaceIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.FaceDef: ...

    def CurrentId(self) -> BRepGraph_FaceId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_WireIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_WireId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_WireIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.WireDef: ...

    def CurrentId(self) -> BRepGraph_WireId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_EdgeIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_EdgeIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.EdgeDef: ...

    def CurrentId(self) -> BRepGraph_EdgeId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_VertexIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_VertexId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_VertexIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.VertexDef: ...

    def CurrentId(self) -> BRepGraph_VertexId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_CoEdgeIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_CoEdgeId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_CoEdgeIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

    def CurrentId(self) -> BRepGraph_CoEdgeId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_CompoundIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_CompoundId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_CompoundIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.CompoundDef: ...

    def CurrentId(self) -> BRepGraph_CompoundId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_CompSolidIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_CompSolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_CompSolidIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.CompSolidDef: ...

    def CurrentId(self) -> BRepGraph_CompSolidId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_ProductIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ProductId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ProductIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ProductDef: ...

    def CurrentId(self) -> BRepGraph_ProductId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_OccurrenceIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_OccurrenceId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_OccurrenceIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

    def CurrentId(self) -> BRepGraph_OccurrenceId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullSolidIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_SolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullSolidIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.SolidDef: ...

    def CurrentId(self) -> BRepGraph_SolidId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullShellIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ShellId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullShellIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ShellDef: ...

    def CurrentId(self) -> BRepGraph_ShellId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullFaceIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_FaceId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullFaceIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.FaceDef: ...

    def CurrentId(self) -> BRepGraph_FaceId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullWireIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_WireId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullWireIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.WireDef: ...

    def CurrentId(self) -> BRepGraph_WireId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullEdgeIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullEdgeIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.EdgeDef: ...

    def CurrentId(self) -> BRepGraph_EdgeId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullVertexIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_VertexId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullVertexIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.VertexDef: ...

    def CurrentId(self) -> BRepGraph_VertexId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullCoEdgeIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_CoEdgeId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullCoEdgeIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

    def CurrentId(self) -> BRepGraph_CoEdgeId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullCompoundIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_CompoundId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullCompoundIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.CompoundDef: ...

    def CurrentId(self) -> BRepGraph_CompoundId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullCompSolidIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_CompSolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullCompSolidIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.CompSolidDef: ...

    def CurrentId(self) -> BRepGraph_CompSolidId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullProductIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ProductId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullProductIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ProductDef: ...

    def CurrentId(self) -> BRepGraph_ProductId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_FullOccurrenceIterator:
    """
    @brief Type-safe, allocation-free iterator over BRepGraph definition nodes.

    @tparam NodeType        Definition struct type (e.g. BRepGraphInc::FaceDef).
    @tparam TheFullTraverse When true, removed nodes are NOT skipped (for special cases).
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_OccurrenceId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullOccurrenceIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

    def CurrentId(self) -> BRepGraph_OccurrenceId:
        """Current definition index as a typed NodeId."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RootProductIterator:
    """
    @brief Allocation-free iterator over root product identifiers.

    Iterates directly over BRepGraph::RootProductIds() - products not
    referenced by any active occurrence.
    """

    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RootProductIterator) -> None: ...

    def __iter__(self) -> BRepGraph_RootProductIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_ProductId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> BRepGraph_ProductId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_ParentExplorer:
    """
    @brief Upward occurrence-aware parent traversal for BRepGraph.
    @see BRepGraph class comment "Iterator guide" for choosing between iterator types.

    Enumerates all ancestor nodes reachable from a starting node.
    Traversal is path-aware: when the same definition is reached through multiple
    occurrence paths, each path contributes its own parent sequence with its own
    accumulated location and orientation.

    The traversal follows the actual graph structure transparently - every node
    kind is visited as a distinct entity (no hidden collapses):
    Vertex -> Edge,  Edge -> CoEdge,  CoEdge -> Wire,  Wire -> Face,
    Face -> Shell,  Shell -> Solid,  Solid -> CompSolid/Compound,
    topology root -> Occurrence, Product child -> Occurrence,
    Occurrence -> parent Product.

    ## Traversal modes
    - **Recursive**: walks the full ancestor chain to the graph roots.
    Without target kind, all ancestors are emitted.
    With target kind, only matching ancestors are emitted but intermediate
    levels are traversed to reach them.
    - **DirectParents**: yields only the immediate parents of the starting node.
    No ascent into grandparents.  With target kind, only parents
    matching the kind are returned.
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId) -> None:
        """
        Explore all parents of the starting node.
        @param[in] theGraph graph to walk
        @param[in] theNode  starting node whose ancestors are explored
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId, theConfig: BRepGraph_ParentExplorer.Config) -> None:
        """
        Preferred long-term constructor: all tuning knobs in `Config`.
        @param[in] theGraph  graph to walk
        @param[in] theNode   starting node whose ancestors are explored
        @param[in] theConfig traversal configuration
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId, theMode: BRepGraph_ParentExplorer.TraversalMode) -> None:
        """
        Explore parents of the starting node using the given traversal mode.
        @param[in] theGraph graph to walk
        @param[in] theNode  starting node whose ancestors are explored
        @param[in] theMode  traversal strategy (recursive or direct parents)
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind) -> None:
        """
        Explore only parents of the given kind.
        @param[in] theGraph     graph to walk
        @param[in] theNode      starting node whose ancestors are explored
        @param[in] theTargetKind kind of nodes to emit
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId, theAvoidKind: BRepGraph_NodeId.Kind | None, theEmitAvoidKind: bool, theMode: BRepGraph_ParentExplorer.TraversalMode = BRepGraph_ParentExplorer.TraversalMode.Recursive) -> None:
        """
        Explore all parents while pruning branches at the avoid kind.
        @param[in] theGraph        graph to walk
        @param[in] theNode         starting node whose ancestors are explored
        @param[in] theAvoidKind    node kind to avoid ascending through
        @param[in] theEmitAvoidKind if true, emit matching avoid-kind ancestors once
        @param[in] theMode         traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind, theMode: BRepGraph_ParentExplorer.TraversalMode) -> None:
        """
        Explore only parents of the given kind using the given traversal mode.
        @param[in] theGraph     graph to walk
        @param[in] theNode      starting node whose ancestors are explored
        @param[in] theTargetKind kind of nodes to emit
        @param[in] theMode      traversal strategy
        """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId, theTargetKind: BRepGraph_NodeId.Kind, theAvoidKind: BRepGraph_NodeId.Kind | None, theEmitAvoidKind: bool, theMode: BRepGraph_ParentExplorer.TraversalMode = BRepGraph_ParentExplorer.TraversalMode.Recursive) -> None:
        """
        Explore parents of the given kind while pruning branches at the avoid kind.
        @param[in] theGraph        graph to walk
        @param[in] theNode         starting node whose ancestors are explored
        @param[in] theTargetKind   kind of nodes to emit
        @param[in] theAvoidKind    node kind to avoid ascending through
        @param[in] theEmitAvoidKind if true, emit matching avoid-kind ancestors once
        @param[in] theMode         traversal strategy
        """

    class LinkKind(enum.Enum):
        """Relationship kind between Current() and CurrentChild()."""

        Reference = 1

        Structural = 2

    class TraversalMode(enum.Enum):
        """Upward traversal strategy."""

        Recursive = 0

        DirectParents = 1

    class Config:
        """
        Consolidated configuration for the explorer.

        The `Config`-based constructor is the preferred idiom: new options can be
        added as fields without additional constructor overloads.

        @code
        BRepGraph_ParentExplorer::Config aConfig;
        aConfig.Mode       = BRepGraph_ParentExplorer::TraversalMode::DirectParents;
        aConfig.TargetKind = BRepGraph_NodeId::Kind::Shell;
        for (auto [id, loc, ori] : BRepGraph_ParentExplorer(aGraph, aNode, aConfig)) { ... }
        @endcode
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_ParentExplorer.Config) -> None: ...

        @property
        def Mode(self) -> BRepGraph_ParentExplorer.TraversalMode: ...

        @Mode.setter
        def Mode(self, arg: BRepGraph_ParentExplorer.TraversalMode, /) -> None: ...

        @property
        def TargetKind(self) -> BRepGraph_NodeId.Kind | None:
            """Emit only this kind (no value = emit all)."""

        @TargetKind.setter
        def TargetKind(self, arg: BRepGraph_NodeId.Kind | None, /) -> None: ...

        @property
        def AvoidKind(self) -> BRepGraph_NodeId.Kind | None:
            """Do not ascend through this kind."""

        @AvoidKind.setter
        def AvoidKind(self, arg: BRepGraph_NodeId.Kind | None, /) -> None: ...

        @property
        def EmitAvoidKind(self) -> bool:
            """Emit matching avoid-kind ancestors once."""

        @EmitAvoidKind.setter
        def EmitAvoidKind(self, arg: bool, /) -> None: ...

    def __iter__(self) -> BRepGraph_ParentExplorer:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraphInc_Instance__BRepGraph_NodeId:
        """Python addition: see __iter__."""

    def GetConfig(self) -> BRepGraph_ParentExplorer.Config:
        """
        Returns the traversal configuration this explorer was constructed with.
        Read-only - configuration is fixed for the lifetime of the explorer.
        """

    def More(self) -> bool:
        """True if another matching parent is available."""

    def Next(self) -> None:
        """Advance to the next matching parent."""

    def Current(self) -> BRepGraphInc_Instance__BRepGraph_NodeId:
        """
        Current matching ancestor node with accumulated location and orientation.
        """

    def CurrentChild(self) -> BRepGraph_NodeId:
        """
        Returns the immediate child of Current() on the currently emitted branch.
        Returns invalid NodeId when no current ancestor is available.
        """

    def CurrentLinkKind(self) -> BRepGraph_ParentExplorer.LinkKind:
        """Returns how Current() is linked to CurrentChild()."""

    def CurrentRef(self) -> BRepGraph_RefId:
        """
        Returns the exact parent-owned RefId linking Current() to CurrentChild(),
        when that branch step is represented by a reference entry.

        Some upward steps are structural and therefore have no parent-owned ref
        entry even though the parent itself is still emitted by the explorer.
        In those cases this method returns an invalid RefId, for example for
        CoEdge->Edge and Occurrence->Product/topology-root.
        """

    def LeafLocation(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Accumulated location at the starting node of the current branch."""

    def LeafOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Accumulated orientation at the starting node of the current branch."""

    def IsCurrentBranchRoot(self) -> bool:
        """True if Current() is the explicit root node of the current branch."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_LayerRegistry:
    """
    @brief Dense GUID-keyed runtime registry of graph layers.

    Stores registered layers in a compact vector for O(1) slot access and a
    GUID-to-slot map for O(1) lookup by stable public identity.
    """

    def __init__(self) -> None: ...

    def RegisterLayer(self, theLayer: BRepGraph_Layer | None) -> int:
        """
        Register a layer. Replaces an existing layer with the same GUID.
        @return slot index in the internal dense vector.
        """

    def UnregisterLayer(self, theGUID: nanoocp.Standard.Standard_GUID) -> None:
        """Remove a layer by GUID."""

    def FindLayer(self, theGUID: nanoocp.Standard.Standard_GUID) -> BRepGraph_Layer:
        """Find a layer by GUID. Returns null handle if not found."""

    def FindSlot(self, theGUID: nanoocp.Standard.Standard_GUID) -> tuple[bool, int]:
        """Return current slot for a GUID."""

    def Layer(self, theSlot: int) -> BRepGraph_Layer:
        """
        Return layer by slot index, or null handle if the slot is out of range.
        """

    def NbLayers(self) -> int:
        """Number of registered layers."""

    def HasModificationSubscribers(self) -> bool:
        """True if any registered layer subscribes to node modification events."""

    def SubscribedKindsMask(self) -> int:
        """Bitwise OR of all registered layer node subscription masks."""

    def DispatchOnNodeRemoved(self, theNode: BRepGraph_NodeId) -> None:
        """Dispatch OnNodeRemoved to all registered layers."""

    def DispatchOnItemRemoved(self, theItem: BRepGraph_ItemId) -> None:
        """Dispatch generic item removal to all registered layers."""

    def DispatchOnNodeReplaced(self, theOldNode: BRepGraph_NodeId, theNewNode: BRepGraph_NodeId) -> None:
        """Dispatch OnNodeReplaced to all registered layers."""

    def DispatchNodeModified(self, theNode: BRepGraph_NodeId) -> None:
        """Dispatch OnNodeModified to subscribed layers."""

    def DispatchItemModified(self, theItem: BRepGraph_ItemId) -> None:
        """
        Dispatch generic item modification through the matching typed subscription path.
        """

    def DispatchNodesModified(self, theModifiedNodes: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theModifiedKindsMask: int) -> None:
        """Dispatch OnNodesModified to subscribed layers."""

    @overload
    def CopyLayersTo(self, theTargetGraph: BRepGraph, theItemRemap: NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId, theMode: BRepGraph_CopyRemap.Mode) -> None:
        """
        Ask every registered source layer to copy itself into the target graph.
        For Mode::Compact, layers are unregistered first and CopyTo creates fresh instances.
        @param[in] theTargetGraph target graph to receive layer data
        @param[in] theItemRemap   source -> target item id mapping
        @param[in] theMode        Copy or Compact semantics
        """

    @overload
    def CopyLayersTo(self, theTargetGraph: BRepGraph, theMappingKind: BRepGraph_CopyRemap.MappingKind, theMode: BRepGraph_CopyRemap.Mode) -> None:
        """
        Ask every registered source layer to copy itself using identity mapping.
        Source item ids are the same as target item ids (full identity copy).
        @param[in] theTargetGraph target graph to receive layer data
        @param[in] theMappingKind identity or explicit mapping
        @param[in] theMode        Copy or Compact semantics
        """

    def HasRefModificationSubscribers(self) -> bool:
        """
        True if any registered layer subscribes to reference modification events.
        """

    def SubscribedRefKindsMask(self) -> int:
        """Bitwise OR of all registered layer reference subscription masks."""

    def DispatchOnRefRemoved(self, theRef: BRepGraph_RefId) -> None:
        """
        Dispatch OnRefRemoved to all registered layers (unconditional - not filtered).
        """

    def DispatchRefModified(self, theRef: BRepGraph_RefId) -> None:
        """Dispatch OnRefModified to subscribed layers (immediate mode)."""

    def DispatchRefsModified(self, theModifiedRefs: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_RefId], theModifiedRefKindsMask: int) -> None:
        """Dispatch OnRefsModified to subscribed layers (deferred/batch mode)."""

    def ClearAll(self) -> None:
        """Clear all registered layer data without unregistering services."""

    def InvalidateAll(self) -> None:
        """Invalidate all registered layer data."""

class BRepGraph_Data:
    """
    @brief Internal storage for BRepGraph (PIMPL).

    All topology definition data and UIDs live in myIncStorage.
    Access via myIncStorage.Edges, myIncStorage.Faces, etc.
    """

    def __init__(self) -> None: ...

    @property
    def myIncStorage(self) -> nanoocp.BRepGraphInc.BRepGraphInc_Storage:
        """
        Incidence-table storage - sole source of truth for all topology data,
        original shapes, TShape->NodeId mapping, UIDs, and UID reverse indexes.
        """

    @property
    def myLayerRegistry(self) -> BRepGraph_LayerRegistry:
        """Registered graph layers."""

    @property
    def myCacheRegistry(self) -> BRepGraph_CacheRegistry:
        """Registered transient cache services."""

    @property
    def myTopoView(self) -> BRepGraph.TopoView:
        """Stable top-level views. Nested views store graph-data context only."""

    @myTopoView.setter
    def myTopoView(self, arg: BRepGraph.TopoView, /) -> None: ...

    @property
    def myUIDsView(self) -> BRepGraph.UIDsView: ...

    @myUIDsView.setter
    def myUIDsView(self, arg: BRepGraph.UIDsView, /) -> None: ...

    @property
    def myRefsView(self) -> BRepGraph.RefsView: ...

    @myRefsView.setter
    def myRefsView(self, arg: BRepGraph.RefsView, /) -> None: ...

    @property
    def myShapesView(self) -> BRepGraph.ShapesView: ...

    @myShapesView.setter
    def myShapesView(self, arg: BRepGraph.ShapesView, /) -> None: ...

    @property
    def myEditorView(self) -> BRepGraph.EditorView: ...

    @myEditorView.setter
    def myEditorView(self, arg: BRepGraph.EditorView, /) -> None: ...

    @property
    def myMeshView(self) -> BRepGraph.MeshView: ...

    @myMeshView.setter
    def myMeshView(self, arg: BRepGraph.MeshView, /) -> None: ...

class BRepGraph_LayerHistory(BRepGraph_Layer):
    """
    History layer for BRepGraph.

    BRepGraph_LayerHistory maintains an append-only log of modification events
    and per-kind lookup maps for efficient queries.  Four event kinds are
    tracked (see #BRepGraph_LayerHistory::Kind):
    - **Modified**: input -> { modified images } (default).
    - **Generated**: input -> { generated images } (new entities born
    from the input but not sharing its identity).
    - **Deleted**: input has been consumed and has no image in the
    result.
    - **Replaced**: input was structurally detached and replaced by another
    node; this maps as Modified and also marks the input as deleted.

    Recording can be toggled on/off at runtime.  Graph-owned history is registered
    as a layer and accessed through #Ensure / #Find; algorithms wrapping OCCT's
    `BRepTools_History` can import results through #Absorb.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: BRepGraph_LayerHistory) -> None: ...

    class Kind(enum.Enum):
        """Classification of a history event."""

        Modified = 0

        Generated = 1

        Deleted = 2

        Replaced = 3

    class Event:
        """One atomic modification event recorded in the graph's history log."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_LayerHistory.Event) -> None: ...

        @property
        def OperationName(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

        @OperationName.setter
        def OperationName(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def SequenceNumber(self) -> int: ...

        @SequenceNumber.setter
        def SequenceNumber(self, arg: int, /) -> None: ...

        @property
        def RecordKind(self) -> BRepGraph_LayerHistory.Kind: ...

        @RecordKind.setter
        def RecordKind(self, arg: BRepGraph_LayerHistory.Kind, /) -> None: ...

        @property
        def Mapping(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_NodeId]]:
            """
            Key: original node id before the operation.
            Value: sequence of replacement node ids after the operation.
            """

        @Mapping.setter
        def Mapping(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_NodeId]], /) -> None: ...

        @property
        def UidMapping(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.BRepGraph.BRepGraph_UID, nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]]:
            """UID-keyed mapping for cross-graph history records."""

        @UidMapping.setter
        def UidMapping(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.BRepGraph.BRepGraph_UID, nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]], /) -> None: ...

        @property
        def ItemUidMapping(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.BRepGraph.BRepGraph_ItemUID, nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ItemUID]]:
            """ItemUID-keyed mapping for durable all-domain history records."""

        @ItemUidMapping.setter
        def ItemUidMapping(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.BRepGraph.BRepGraph_ItemUID, nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ItemUID]], /) -> None: ...

        @property
        def ExtraInfo(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """Optional diagnostic representation."""

        @ExtraInfo.setter
        def ExtraInfo(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Stable layer GUID."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Layer type identity."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Layer display name."""

    @overload
    def Record(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOriginal: BRepGraph_NodeId, theReplacements: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theKind: BRepGraph_LayerHistory.Kind = BRepGraph_LayerHistory.Kind.Modified) -> None:
        """
        Record a modification: theOriginal was replaced by theReplacements.

        @note When @p theReplacements is empty the record is auto-downgraded to
        Kind::Deleted and @p theOriginal is added to the deleted set,
        regardless of @p theKind.  Use #RecordDeleted directly for the
        deletion case to avoid relying on this implicit conversion.
        @param[in] theOpLabel      human-readable operation name
        @param[in] theOriginal     node id before the operation
        @param[in] theReplacements node ids after the operation
        @param[in] theKind         classification of this record (default Modified)
        """

    @overload
    def Record(self, theRecordIdx: int) -> BRepGraph_LayerHistory.Event:
        """
        Access a record by index (0-based).
        @param[in] theRecordIdx zero-based index into the records vector
        @return the history record at the given index
        """

    def RecordBatch(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOriginals: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theReplacements: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theExtraInfo: nanoocp.TCollection.TCollection_AsciiString = ..., theKind: BRepGraph_LayerHistory.Kind = BRepGraph_LayerHistory.Kind.Modified) -> None:
        """
        Record a batch of 1-to-1 modifications in a single history event.
        Each original is paired with the replacement at the same logical position.
        More efficient than calling Record() in a loop: creates one HistoryRecord
        and updates the per-kind maps with minimal overhead.
        @param[in] theOpLabel      human-readable operation name
        @param[in] theOriginals    node ids before the operation
        @param[in] theReplacements node ids after the operation (same length)
        @param[in] theExtraInfo    optional diagnostic info stored on the record
        @param[in] theKind         classification of this record (default Modified)
        """

    def RecordDeleted(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theDeleted: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId]) -> None:
        """
        Record that a collection of inputs has been consumed by the operation
        and has no image in the result.  Each input is appended to the
        deleted set and emits a single audit record with empty replacements.
        @param[in] theOpLabel human-readable operation name
        @param[in] theDeleted node ids that have been removed
        """

    def RecordReplaced(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOriginal: BRepGraph_NodeId, theReplacement: BRepGraph_NodeId) -> None:
        """
        Record replacements: each original is logically removed/detached and
        continued by the corresponding replacement.  Replaced records participate
        in modified-image queries and also mark originals as deleted.
        """

    def RecordReplacedBatch(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOriginals: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theReplacements: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_NodeId], theExtraInfo: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Record a batch of 1-to-1 replacements in a single history event."""

    def RecordUid(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOriginal: BRepGraph_UID, theReplacements: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_UID], theKind: BRepGraph_LayerHistory.Kind = BRepGraph_LayerHistory.Kind.Modified) -> None:
        """
        Record a UID-keyed modification/generation event.

        This is the durable-history path for operations whose source and result
        identities may live in different BRepGraph instances.  Existing NodeId
        records remain available for in-graph algorithms; UID records are queried
        directly by cross-graph consumers.
        """

    def RecordDeletedUid(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theDeleted: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_UID]) -> None:
        """Record UID-keyed deletions."""

    def RecordItemUid(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theOriginal: BRepGraph_ItemUID, theReplacements: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ItemUID], theKind: BRepGraph_LayerHistory.Kind = BRepGraph_LayerHistory.Kind.Modified) -> None:
        """Record an all-domain ItemUID-keyed modification/generation event."""

    def RecordDeletedItemUid(self, theOpLabel: nanoocp.TCollection.TCollection_AsciiString, theDeleted: nanoocp.NCollection.NCollection_Array1[nanoocp.BRepGraph.BRepGraph_ItemUID]) -> None:
        """Record ItemUID-keyed deletions."""

    @overload
    def Absorb(self, theInputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], theOutputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], theSource: nanoocp.BRepTools.BRepTools_History | None, theOpLabel: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Import a BRepTools_History into this graph-native history log.

        Iterates @p theInputs, queries @p theSource for Modified / Generated /
        IsRemoved, translates each TopoDS_Shape image to a NodeId via
        @p theOutputs, and emits the corresponding records.

        Semantics:
        - For every input shape whose Modified() list is non-empty:
        emit a Modified record.
        - For every input shape whose Generated() list is non-empty:
        emit a Generated record.
        - For every input shape with IsRemoved() == true: accumulate into
        a single Deleted record (IsRemoved takes precedence over
        Modified/Generated to handle a known OCCT bug where a shape can
        appear in both the removed set and the generated map).

        Output TopoDS_Shapes that do not appear in @p theOutputs are silently
        dropped (expected for subshapes merged into a parent compound whose
        identity is preserved at a higher level).

        @param[in] theInputs  TopoDS_Shape -> NodeId for every input subshape
        that should be tracked
        @param[in] theOutputs TopoDS_Shape -> NodeId for every subshape added
        to the graph by this operation (typically from
        BRepGraph::ShapesView::Add with TrackAddedNodes)
        @param[in] theSource  BRepTools_History from the OCCT algorithm.
        Null is accepted (no-op).
        @param[in] theOpLabel record label written into every emitted record
        """

    @overload
    def Absorb(self, theInputGraph: BRepGraph, theOutputGraph: BRepGraph, theInputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], theOutputs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepGraph.BRepGraph_NodeId, nanoocp.TopTools.TopTools_ShapeMapHasher], theSource: nanoocp.BRepTools.BRepTools_History | None, theOpLabel: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Import a BRepTools_History using persistent UIDs from source/result graphs.

        This overload is the canonical bridge for cross-graph algorithms: input
        shapes are resolved in @p theInputGraph, output shapes are resolved in
        @p theOutputGraph, and the resulting history is stored by UID.
        """

    def FindOriginal(self, theModified: BRepGraph_NodeId) -> BRepGraph_NodeId:
        """
        Walk backwards from a modified node to its original.
        Follows the reverse map recursively until a root is reached.
        @param[in] theModified node id to trace back
        @return the root original node id, or theModified itself if not found
        """

    def FindDerived(self, theOriginal: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_NodeId]:
        """
        Walk forwards from an original node to all derived nodes, including
        both Modified and Generated descendants.  Follows the forward maps
        recursively, collecting every transitively-reachable descendant
        (intermediate nodes and leaves alike, but not @p theOriginal itself).
        @param[in] theOriginal node id to trace forward
        @return all transitively derived node ids in breadth-first order
        """

    @overload
    def FindModified(self, theOriginal: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_NodeId]:
        """
        Direct lookup of the Modified images of @p theOriginal, non-recursive.
        @param[in] theOriginal node id to query
        @return pointer to the stored vector, or nullptr if @p theOriginal has
        no Modified record (note: nullptr does not imply IsDeleted).
        """

    @overload
    def FindModified(self, theUID: BRepGraph_UID) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]:
        """UID-keyed Modified images stored directly in this history."""

    @overload
    def FindModified(self, theUID: BRepGraph_ItemUID) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ItemUID]:
        """ItemUID-keyed Modified images stored directly in this history."""

    @overload
    def FindModified(self, theGraph: BRepGraph, theUID: BRepGraph_UID) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]:
        """
        UID-keyed convenience: Modified images of the input identified by
        @p theUID, resolved against @p theGraph.  Returns an empty vector if
        the UID cannot be resolved or has no Modified record.
        @param[in] theGraph graph used to translate UID <-> NodeId
        @param[in] theUID   UID of the input entity
        @return UIDs of the modified images (in record-insertion order)
        """

    @overload
    def FindGenerated(self, theOriginal: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_NodeId]:
        """
        Direct lookup of the Generated images of @p theOriginal, non-recursive.
        @param[in] theOriginal node id to query
        @return pointer to the stored vector, or nullptr if @p theOriginal has
        no Generated record.
        """

    @overload
    def FindGenerated(self, theUID: BRepGraph_UID) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]:
        """UID-keyed Generated images stored directly in this history."""

    @overload
    def FindGenerated(self, theUID: BRepGraph_ItemUID) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ItemUID]:
        """ItemUID-keyed Generated images stored directly in this history."""

    @overload
    def FindGenerated(self, theGraph: BRepGraph, theUID: BRepGraph_UID) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]:
        """
        UID-keyed convenience: Generated images.  See #FindModified for the
        resolution contract.
        @param[in] theGraph graph used to translate UID <-> NodeId
        @param[in] theUID   UID of the input entity
        @return UIDs of the generated images (in record-insertion order)
        """

    @overload
    def IsDeleted(self, theOriginal: BRepGraph_NodeId) -> bool:
        """
        Test whether @p theOriginal was deleted by some recorded operation.
        @param[in] theOriginal node id to query
        @return true if @p theOriginal is in the deleted set
        """

    @overload
    def IsDeleted(self, theUID: BRepGraph_UID) -> bool:
        """UID-keyed deletion test stored directly in this history."""

    @overload
    def IsDeleted(self, theUID: BRepGraph_ItemUID) -> bool:
        """ItemUID-keyed deletion test stored directly in this history."""

    @overload
    def IsDeleted(self, theGraph: BRepGraph, theUID: BRepGraph_UID) -> bool:
        """
        UID-keyed convenience: deletion test.
        @param[in] theGraph graph used to resolve the UID
        @param[in] theUID   UID of the input entity
        @return true if the resolved NodeId is in the deleted set
        """

    def DeletedNodes(self) -> NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId:
        """
        Borrowed access to the full deleted set.
        @return reference to the deleted-node set
        """

    def FindOriginals(self, theDerived: BRepGraph_NodeId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_NodeId]:
        """
        Direct lookup of all immediate node origins of @p theDerived.
        A derived entity can have more than one parent in reconstructive algorithms.
        """

    @overload
    def DeletedUids(self) -> NCollection_FlatMap__BRepGraph_UID__NCollection_DefaultHasher__BRepGraph_UID:
        """UID-keyed deleted set stored directly in this history."""

    @overload
    def DeletedUids(self, theGraph: BRepGraph) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_UID]:
        """
        UID-keyed convenience: dump the full deleted set as UIDs.
        @param[in] theGraph graph used to translate NodeId -> UID
        @return UIDs of all deleted entities (insertion order is not stable)
        """

    @overload
    def HasKnownInput(self, theUID: BRepGraph_UID) -> bool: ...

    @overload
    def HasKnownInput(self, theUID: BRepGraph_ItemUID) -> bool:
        """Test whether @p theUID was registered as an operation input."""

    def DeletedItemUids(self) -> NCollection_FlatMap__BRepGraph_ItemUID__NCollection_DefaultHasher__BRepGraph_ItemUID:
        """ItemUID-keyed deleted set stored directly in this history."""

    def NbRecords(self) -> int:
        """
        Number of recorded history events.
        @return record count
        """

    def SetEnabled(self, theVal: bool) -> None:
        """
        Enable or disable history recording.
        @param[in] theVal true to enable, false to disable
        """

    def IsEnabled(self) -> bool:
        """
        Query whether history recording is enabled.
        @return true if recording is active
        """

    def Clear(self) -> None:
        """Clear all records and lookup maps."""

    def OnNodeRemoved(self, theNode: BRepGraph_NodeId) -> None:
        """Layer removal callback. Records pure graph deletions when enabled."""

    def CopyTo(self, theCopy: BRepGraph_CopyRemap) -> None:
        """Copy history records whose source items have copied target items."""

    def InvalidateAll(self) -> None:
        """Clear derived caches by dropping collected history."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_LayerParametric(BRepGraph_Layer):
    """
    @brief Base layer for graph-owned parametric generators.

    The class defines the common instance identity, generation flags, mesh
    quality controls, and graph access helpers shared by higher-level parametric
    layers.
    Concrete layers such as BRepGraphPrim box, plane, or loft generators build
    their own parameter schema and manifest storage on top of this base.
    """

    class GenerationFlag(enum.Enum):
        """Controls which graph artifacts should be created or refreshed."""

        Topology = 1

        Geometry = 2

        Mesh = 4

    class MeshQuality(enum.Enum):
        """High-level mesh quality hint shared by parametric generators."""

        VeryCoarse = 0

        Coarse = 1

        Medium = 2

        Fine = 3

        VeryFine = 4

    class AddResult:
        """Result of adding a new parametric instance to a graph."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_LayerParametric.AddResult) -> None: ...

        @property
        def Instance(self) -> int:
            """Created instance identifier."""

        @Instance.setter
        def Instance(self, arg: int, /) -> None: ...

        @property
        def Root(self) -> BRepGraph_NodeId:
            """Root topology node of the created subtree."""

        @Root.setter
        def Root(self, arg: BRepGraph_NodeId, /) -> None: ...

    @staticmethod
    def GenerationMask(theFlag: BRepGraph_LayerParametric.GenerationFlag) -> int:
        """
        Convert one generation flag into its bit-mask value.
        @param[in] theFlag generation flag to convert
        @return bit-mask value for the requested generation flag
        """

    @staticmethod
    def HasGenerationFlag(theFlags: int, theFlag: BRepGraph_LayerParametric.GenerationFlag) -> bool:
        """
        Return true when the flag mask contains the requested generation flag.
        @param[in] theFlags generation mask built from GenerationFlag bits
        @param[in] theFlag generation flag to test
        @return true when the flag is present in the mask
        """

    @staticmethod
    def MeshQualityValue(theQuality: BRepGraph_LayerParametric.MeshQuality, theVeryCoarse: int, theCoarse: int, theMedium: int, theFine: int, theVeryFine: int) -> int:
        """
        Select one integer value from a mesh-quality ladder.
        @param[in] theQuality requested shared mesh quality
        @param[in] theVeryCoarse value for MeshQuality::VeryCoarse
        @param[in] theCoarse value for MeshQuality::Coarse
        @param[in] theMedium value for MeshQuality::Medium
        @param[in] theFine value for MeshQuality::Fine
        @param[in] theVeryFine value for MeshQuality::VeryFine
        @return selected value for the requested quality
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_LayerDeferred(BRepGraph_Layer):
    """
    Base layer for postponed graph item loading.

    The layer stores provider-neutral deferred representation records and owns the lock
    state through BRepGraph_LayerLock. Format-specific loaders, such as ODE or
    STEP, should derive from this class or use the same representation contract rather
    than storing deferred ownership in topology definitions.
    """

    @overload
    def __init__(self) -> None:
        """Constructor for generic deferred layers."""

    @overload
    def __init__(self, theOther: BRepGraph_LayerDeferred) -> None: ...

    class RepresentationKind(enum.Enum):
        """Representation category."""

        Unknown = 0

        Geometry = 1

        Mesh = 2

        Topology = 3

        Assembly = 4

        Parametric = 5

    class Representation:
        """One postponed representation attached to a graph item."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_LayerDeferred.Representation) -> None: ...

        @property
        def Kind(self) -> BRepGraph_LayerDeferred.RepresentationKind: ...

        @Kind.setter
        def Kind(self, arg: BRepGraph_LayerDeferred.RepresentationKind, /) -> None: ...

        @property
        def Role(self) -> int: ...

        @Role.setter
        def Role(self, arg: int, /) -> None: ...

        @property
        def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

        @Name.setter
        def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def SourceIndex(self) -> int: ...

        @SourceIndex.setter
        def SourceIndex(self, arg: int, /) -> None: ...

    class Entry:
        """Deferred ownership entry for one graph item."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_LayerDeferred.Entry) -> None: ...

        class RepresentationStorage:
            """
            Small fixed representation list. Deferred graph items have a bounded number of
            persisted representations, so avoid one heap allocation per item.
            """

            @overload
            def __init__(self) -> None: ...

            @overload
            def __init__(self, theOther: BRepGraph_LayerDeferred.Entry.RepresentationStorage) -> None: ...

            def Size(self) -> int: ...

            def IsEmpty(self) -> bool: ...

            def ContainsKind(self, theKind: BRepGraph_LayerDeferred.RepresentationKind) -> bool: ...

            def Value(self, theIndex: int) -> BRepGraph_LayerDeferred.Representation: ...

            def ChangeValue(self, theIndex: int) -> BRepGraph_LayerDeferred.Representation: ...

            def First(self) -> BRepGraph_LayerDeferred.Representation: ...

            def Append(self, theRepresentation: BRepGraph_LayerDeferred.Representation) -> None: ...

            def Clear(self) -> None: ...

        @property
        def Provider(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

        @Provider.setter
        def Provider(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def SourceKey(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

        @SourceKey.setter
        def SourceKey(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def Representations(self) -> BRepGraph_LayerDeferred.Entry.RepresentationStorage: ...

        @Representations.setter
        def Representations(self, arg: BRepGraph_LayerDeferred.Entry.RepresentationStorage, /) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Return fixed layer type GUID."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Return this layer type GUID."""

    @overload
    def FindDeferred(self, theItem: BRepGraph_ItemId) -> BRepGraph_LayerDeferred.Entry:
        """Return deferred entry for an item, or null if none exists."""

    @overload
    def FindDeferred(self, theNode: BRepGraph_NodeId) -> BRepGraph_LayerDeferred.Entry:
        """Return deferred entry for a node, or null if none exists."""

    @overload
    def FindDeferred(self, theRef: BRepGraph_RefId) -> BRepGraph_LayerDeferred.Entry:
        """Return deferred entry for a reference, or null if none exists."""

    @overload
    def HasDeferred(self, theItem: BRepGraph_ItemId) -> bool:
        """Return true if an item has deferred representations."""

    @overload
    def HasDeferred(self, theNode: BRepGraph_NodeId) -> bool:
        """Return true if a node has deferred representations."""

    @overload
    def HasDeferred(self, theRef: BRepGraph_RefId) -> bool:
        """Return true if a reference has deferred representations."""

    @overload
    def RegisterDeferred(self, theItem: BRepGraph_ItemId, theProvider: nanoocp.TCollection.TCollection_AsciiString, theSourceKey: nanoocp.TCollection.TCollection_AsciiString, theRepresentationKind: BRepGraph_LayerDeferred.RepresentationKind, theRepresentationName: nanoocp.TCollection.TCollection_AsciiString, theSourceIndex: int) -> None:
        """Register one postponed representation and lock the item."""

    @overload
    def RegisterDeferred(self, theNode: BRepGraph_NodeId, theProvider: nanoocp.TCollection.TCollection_AsciiString, theSourceKey: nanoocp.TCollection.TCollection_AsciiString, theRepresentationKind: BRepGraph_LayerDeferred.RepresentationKind, theRepresentationName: nanoocp.TCollection.TCollection_AsciiString, theSourceIndex: int) -> None:
        """Register one postponed node representation and lock the node."""

    @overload
    def RegisterDeferred(self, theRef: BRepGraph_RefId, theProvider: nanoocp.TCollection.TCollection_AsciiString, theSourceKey: nanoocp.TCollection.TCollection_AsciiString, theRepresentationKind: BRepGraph_LayerDeferred.RepresentationKind, theRepresentationName: nanoocp.TCollection.TCollection_AsciiString, theSourceIndex: int) -> None:
        """
        Register one postponed reference representation and lock the reference.
        """

    def RegisterDeferredRepresentations(self, theItem: BRepGraph_ItemId, theProvider: nanoocp.TCollection.TCollection_AsciiString, theSourceKey: nanoocp.TCollection.TCollection_AsciiString, theRepresentations: BRepGraph_LayerDeferred.Representation, theNbRepresentations: int) -> None:
        """
        Register postponed representations for one item and lock the item once.
        """

    def RegisterDeferredRepresentationsDirect(self, theItem: BRepGraph_ItemId, theProvider: nanoocp.TCollection.TCollection_AsciiString, theSourceKey: nanoocp.TCollection.TCollection_AsciiString, theRepresentations: BRepGraph_LayerDeferred.Representation, theNbRepresentations: int) -> None:
        """
        Register postponed representations for a new item and lock it once.

        This is a trusted bulk-load fast path: the caller must ensure the item is valid,
        has no existing deferred entry, and `theRepresentations` contains no duplicates.
        """

    @overload
    def UnregisterDeferred(self, theItem: BRepGraph_ItemId) -> None:
        """Remove all deferred representations for an item and unlock it."""

    @overload
    def UnregisterDeferred(self, theNode: BRepGraph_NodeId) -> None:
        """Remove all deferred representations for a node and unlock it."""

    @overload
    def UnregisterDeferred(self, theRef: BRepGraph_RefId) -> None:
        """Remove all deferred representations for a reference and unlock it."""

    def HasDeferredItems(self) -> bool:
        """Return true if at least one item has deferred representations."""

    def FindFirstDeferred(self, theKind: BRepGraph_LayerDeferred.RepresentationKind, theItem: BRepGraph_ItemId = None) -> BRepGraph_LayerDeferred.Entry:
        """
        Return first deferred entry with at least one representation of the requested kind, or null.
        """

    def ReserveDeferredItems(self, theNbItems: int) -> None:
        """Reserve deferred and lock layer buckets for bulk registration."""

    def BeginBulkRegistration(self) -> None:
        """
        Begin bulk deferred registration. Revision updates are postponed until EndBulkRegistration().
        """

    def EndBulkRegistration(self) -> None:
        """
        Finish bulk deferred registration and publish one revision update if anything changed.
        """

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def OnNodeRemoved(self, theNode: BRepGraph_NodeId) -> None: ...

    def OnNodeReplaced(self, theOldNode: BRepGraph_NodeId, theNewNode: BRepGraph_NodeId) -> None: ...

    def CopyTo(self, theCopy: BRepGraph_CopyRemap) -> None: ...

    def OnRefRemoved(self, theRef: BRepGraph_RefId) -> None: ...

    def InvalidateAll(self) -> None: ...

    def Clear(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_LayerIterator:
    """
    @brief Iterator over registered layers in a BRepGraph_LayerRegistry.

    Provides zero-allocation iteration with OCCT More()/Next()/Value() pattern
    and STL range-for via begin()/end().

    @code
    // Range-for:
    for (const occ::handle<BRepGraph_Layer>& aLayer :
    BRepGraph_LayerIterator(aGraph.LayerRegistry()))
    doSomething(aLayer);

    // Traditional:
    for (BRepGraph_LayerIterator anIt(aGraph.LayerRegistry()); anIt.More(); anIt.Next())
    doSomething(anIt.Value());
    @endcode
    """

    @overload
    def __init__(self, theRegistry: BRepGraph_LayerRegistry) -> None:
        """Construct an iterator over all layers in the registry."""

    @overload
    def __init__(self, theOther: BRepGraph_LayerIterator) -> None: ...

    def __iter__(self) -> BRepGraph_LayerIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_Layer:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """True if the iterator has a current element."""

    def Next(self) -> None:
        """Advance to the next layer."""

    def Value(self) -> BRepGraph_Layer:
        """Return the current layer handle."""

    def Slot(self) -> int:
        """Return the current slot index in the registry."""

    def NbLayers(self) -> int:
        """Number of layers in the registry."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Sentinel marking end of iteration."""

class BRepGraph_LayerLock(BRepGraph_Layer):
    """
    Owner metadata layer for owned BRepGraph items.

    Uses a root-based ownership model: only the highest owned item per group
    is stored in the map. All descendants receive the fast IsOwned bit-flag
    via automatic downward propagation. Owner lookup traverses upward to
    find the root entry.

    Overlapping roots are forbidden: SetOwner rejects if the item is already
    covered by an ancestor root with a different GUID.

    HasOwner() checks the IsOwned bit-flag (O(1)).
    FindOwnerId() traverses upward to find the root entry (O(depth)).
    """

    @overload
    def __init__(self) -> None:
        """Create lock-owner storage."""

    @overload
    def __init__(self, theOther: BRepGraph_LayerLock) -> None: ...

    class ScopedOwnerEdit:
        """
        Scoped permission for an owner layer to edit one item it owns.

        The scope traverses upward to find the root owner for GUID verification,
        then temporarily clears the fast owned bit on the specific item so existing
        editor mutation APIs can be reused by the owning layer.
        """

        def __init__(self, theLayer: BRepGraph_LayerLock, theItem: BRepGraph_ItemId, theOwnerId: nanoocp.Standard.Standard_GUID) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Return fixed layer type GUID."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Return this layer type GUID."""

    @overload
    def FindOwnerId(self, theItem: BRepGraph_ItemId, theOwnerId: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Return owner ID for an item.
        Traverses upward for nodes/refs to find the root owner entry.
        @return true when the item has a resolved owner and @p theOwnerId was filled.
        """

    @overload
    def FindOwnerId(self, theNode: BRepGraph_NodeId, theOwnerId: nanoocp.Standard.Standard_GUID) -> bool:
        """Return owner ID for a node."""

    @overload
    def FindOwnerId(self, theRef: BRepGraph_RefId, theOwnerId: nanoocp.Standard.Standard_GUID) -> bool:
        """Return owner ID for a reference."""

    @overload
    def HasOwner(self, theItem: BRepGraph_ItemId) -> bool:
        """
        Return true if an item's IsOwned bit-flag is set.
        This is an O(1) check. Use FindOwnerId() to resolve the actual owner GUID.
        """

    @overload
    def HasOwner(self, theNode: BRepGraph_NodeId) -> bool:
        """Return true if a node's IsOwned bit-flag is set."""

    @overload
    def HasOwner(self, theRef: BRepGraph_RefId) -> bool:
        """Return true if a reference's IsOwned bit-flag is set."""

    @overload
    def SetOwner(self, theItem: BRepGraph_ItemId, theOwnerId: nanoocp.Standard.Standard_GUID) -> None:
        """
        Register an owner ID and set the graph item's ownership flag.
        For nodes, propagates the IsOwned bit-flag to all descendants.
        Rejects if the item is already covered by an ancestor root with a different GUID.
        """

    @overload
    def SetOwner(self, theItem: BRepGraph_ItemId, theOwnerId: nanoocp.Standard.Standard_GUID, theToUpdateRevision: bool) -> bool:
        """
        Register an owner ID and set the graph item's ownership flag.
        Returns true when owner storage changed. Revision update can be deferred by bulk callers.
        """

    @overload
    def SetOwner(self, theNode: BRepGraph_NodeId, theOwnerId: nanoocp.Standard.Standard_GUID) -> None:
        """Register an owner ID and set the node ownership flag."""

    @overload
    def SetOwner(self, theRef: BRepGraph_RefId, theOwnerId: nanoocp.Standard.Standard_GUID) -> None:
        """Register an owner ID and set the reference ownership flag."""

    @overload
    def UnsetOwner(self, theItem: BRepGraph_ItemId) -> None:
        """
        Remove an owner and clear the graph item's ownership flag.
        For node roots, clears the IsOwned bit-flag on all descendants.
        """

    @overload
    def UnsetOwner(self, theItem: BRepGraph_ItemId, theOwnerId: nanoocp.Standard.Standard_GUID) -> None:
        """
        Remove an owner and clear the graph item's ownership flag if owner ID matches.
        """

    @overload
    def UnsetOwner(self, theNode: BRepGraph_NodeId) -> None:
        """Remove an owner and clear the node ownership flag."""

    @overload
    def UnsetOwner(self, theRef: BRepGraph_RefId) -> None:
        """Remove an owner and clear the reference ownership flag."""

    def HasOwners(self) -> bool:
        """Return true if at least one root entry exists."""

    def ReserveOwners(self, theNbOwners: int) -> None:
        """Reserve owner map buckets for bulk registration."""

    def TouchOwners(self) -> None:
        """Mark owner metadata changed after a bulk update."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def OnNodeRemoved(self, theNode: BRepGraph_NodeId) -> None: ...

    def OnNodeReplaced(self, theOldNode: BRepGraph_NodeId, theNewNode: BRepGraph_NodeId) -> None: ...

    def CopyTo(self, theCopy: BRepGraph_CopyRemap) -> None: ...

    def OnRefRemoved(self, theRef: BRepGraph_RefId) -> None: ...

    def InvalidateAll(self) -> None: ...

    def Clear(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepGraph_DeferredScope:
    """
    @brief RAII guard for batch mutation scopes with deferred invalidation.

    Activates deferred invalidation on construction and flushes it on destruction,
    followed by CommitMutation validation. Guarantees exception-safe cleanup:
    when this guard owns deferred mode, it is always closed and boundary checks
    are executed at scope exit. EndDeferredInvalidation() batch-propagates
    SubtreeGen upward, then CommitMutation() validates relation consistency and
    active-entity counts.

    Re-entrant: if deferred mode is already active (e.g., nested guard),
    the inner guard is a no-op. Only the outermost guard flushes and commits,
    so nested scopes do not create separate transaction or validation boundaries.

    @warning This guard batches invalidation and propagation; it is NOT a
    transaction and does not serialize mutation bodies. Concurrent `Mut*()`
    usage still requires external synchronization for the whole guarded scope
    (for example, a mutex protecting exclusive Builder() access until the guard
    is destroyed).

    Usage:
    @code
    {
    BRepGraph_DeferredScope aScope(theGraph);
    for (int i = 0; i < N; ++i)
    {
    // mutations
    }
    } // EndDeferredInvalidation + CommitMutation called here
    @endcode
    """

    def __init__(self, theGraph: BRepGraph) -> None:
        """Begin deferred invalidation if not already active."""

class BRepGraph_ParallelPolicy:
    """
    Lightweight workload-aware policy for deciding whether an internal phase
    should actually launch parallel work when parallel mode is allowed.

    The goal is to avoid forcing every short-lived loop onto the thread pool.
    Decisions are based on available worker capacity and on the amount of work
    already visible to the phase, instead of on buried per-loop split sizes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ParallelPolicy) -> None: ...

    class Workload:
        """Simple workload estimate for an execution phase."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_ParallelPolicy.Workload) -> None: ...

        @property
        def PrimaryItems(self) -> int:
            """Main loop range."""

        @PrimaryItems.setter
        def PrimaryItems(self, arg: int, /) -> None: ...

        @property
        def AuxiliaryItems(self) -> int:
            """Additional independent items participating in the phase."""

        @AuxiliaryItems.setter
        def AuxiliaryItems(self, arg: int, /) -> None: ...

        @property
        def InteractionCount(self) -> int:
            """Pairwise or adjacency work discovered for the phase."""

        @InteractionCount.setter
        def InteractionCount(self, arg: int, /) -> None: ...

    @staticmethod
    def WorkerCount() -> int:
        """Return the effective logical worker count reported by OSD_Parallel."""

    @staticmethod
    def IsParallelAllowed(theAllowParallel: bool) -> bool:
        """Check whether parallel execution is allowed and meaningful at all."""

    @overload
    @staticmethod
    def ShouldRun(theAllowParallel: bool, theWorkers: int, theWorkload: BRepGraph_ParallelPolicy.Workload) -> bool:
        """
        Decide whether the estimated workload is large enough to amortize
        thread-pool launch and synchronization overhead.
        @param[in] theAllowParallel  whether parallel mode is allowed by the caller
        @param[in] theWorkers        effective logical worker count
        @param[in] theWorkload       estimated workload for the phase
        @return true if parallel execution should be used
        """

    @overload
    @staticmethod
    def ShouldRun(theAllowParallel: bool, theWorkload: BRepGraph_ParallelPolicy.Workload) -> bool:
        """
        Overload that queries the active worker count lazily.
        @param[in] theAllowParallel  whether parallel mode is allowed by the caller
        @param[in] theWorkload       estimated workload for the phase
        @return true if parallel execution should be used
        """

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell__BRepGraphInc_ShellRef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell__BRepGraphInc_ShellRef) -> None: ...

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face__BRepGraphInc_FaceRef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face__BRepGraphInc_FaceRef) -> None: ...

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire__BRepGraphInc_WireRef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire__BRepGraphInc_WireRef) -> None: ...

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef) -> None: ...

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid__BRepGraphInc_SolidRef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid__BRepGraphInc_SolidRef) -> None: ...

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child__BRepGraphInc_ChildRef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child__BRepGraphInc_ChildRef) -> None: ...

class BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence__BRepGraphInc_OccurrenceRef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence__BRepGraphInc_OccurrenceRef) -> None: ...

class BRepGraph_RefsShellOfSolid:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_SolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsShellOfSolid) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_ShellRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RefsFaceOfShell:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_ShellId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsFaceOfShell) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_FaceRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RefsWireOfFace:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_FaceId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsWireOfFace) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_WireRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_CoEdgesOfWire:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_WireId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_CoEdgesOfWire) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_CoEdgeId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RefsSolidOfCompSolid:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_CompSolidId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsSolidOfCompSolid) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_SolidRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RefsChildOfCompound:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_CompoundId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsChildOfCompound) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_ChildRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RefsOccurrenceOfProduct:
    @overload
    def __init__(self, theGraph: BRepGraph, theParent: BRepGraph_ProductId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsOccurrenceOfProduct) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_OccurrenceRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_ShellRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ShellRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ShellRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ShellRef: ...

    def CurrentId(self) -> BRepGraph_ShellRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FaceRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_FaceRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FaceRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.FaceRef: ...

    def CurrentId(self) -> BRepGraph_FaceRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_WireRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_WireRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_WireRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.WireRef: ...

    def CurrentId(self) -> BRepGraph_WireRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_VertexRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_VertexRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_VertexRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.VertexRef: ...

    def CurrentId(self) -> BRepGraph_VertexRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_SolidRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_SolidRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_SolidRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.SolidRef: ...

    def CurrentId(self) -> BRepGraph_SolidRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_ChildRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ChildRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ChildRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ChildRef: ...

    def CurrentId(self) -> BRepGraph_ChildRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_OccurrenceRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_OccurrenceRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_OccurrenceRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.OccurrenceRef: ...

    def CurrentId(self) -> BRepGraph_OccurrenceRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullShellRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ShellRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullShellRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ShellRef: ...

    def CurrentId(self) -> BRepGraph_ShellRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullFaceRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_FaceRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullFaceRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.FaceRef: ...

    def CurrentId(self) -> BRepGraph_FaceRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullWireRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_WireRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullWireRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.WireRef: ...

    def CurrentId(self) -> BRepGraph_WireRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullVertexRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_VertexRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullVertexRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.VertexRef: ...

    def CurrentId(self) -> BRepGraph_VertexRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullSolidRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_SolidRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullSolidRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.SolidRef: ...

    def CurrentId(self) -> BRepGraph_SolidRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullChildRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_ChildRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullChildRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.ChildRef: ...

    def CurrentId(self) -> BRepGraph_ChildRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FullOccurrenceRefIterator:
    @overload
    def __init__(self, theGraph: BRepGraph) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theStartId: BRepGraph_OccurrenceRefId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FullOccurrenceRefIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.BRepGraphInc.OccurrenceRef: ...

    def CurrentId(self) -> BRepGraph_OccurrenceRefId: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_SolidId) -> nanoocp.BRepGraphInc.SolidDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_ShellId) -> nanoocp.BRepGraphInc.ShellDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_FaceId) -> nanoocp.BRepGraphInc.FaceDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_WireId) -> nanoocp.BRepGraphInc.WireDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Edge:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Edge) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_EdgeId) -> nanoocp.BRepGraphInc.EdgeDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Vertex:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Vertex) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_VertexId) -> nanoocp.BRepGraphInc.VertexDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_CoEdgeId) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_CompoundId) -> nanoocp.BRepGraphInc.CompoundDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_CompSolidId) -> nanoocp.BRepGraphInc.CompSolidDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_ProductId) -> nanoocp.BRepGraphInc.ProductDef: ...

class BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Occurrence:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_DefTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Occurrence) -> None: ...

    @staticmethod
    def Get(theGraph: BRepGraph, theId: BRepGraph_OccurrenceId) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

class BRepGraph_EdgesOfVertex:
    """
    Typed iterator over a relation vector of parent IDs.
    Skips removed parent definitions automatically in sequential iteration.
    Also provides indexed access (Length/Value) for callers that need
    random access into the underlying vector (e.g. BRepGraph_ParentExplorer).
    @tparam TypedIdT Typed ID such as BRepGraph_FaceId, BRepGraph_EdgeId, etc.
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theParents: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_EdgeId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theParents: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_EdgeId], theStartIndex: int) -> None:
        """
        Construct starting at a given vector index (for resumable iteration).
        Skips to the first non-removed entry at or after theStartIndex.
        """

    @overload
    def __init__(self, theOther: BRepGraph_EdgesOfVertex) -> None: ...

    def __iter__(self) -> BRepGraph_EdgesOfVertex:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_EdgeId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_EdgeId: ...

    def Current(self) -> BRepGraph_EdgeId:
        """
        Alias for CurrentId(), enables range-for via NCollection_ForwardRange Current() priority.
        """

    def Definition(self) -> nanoocp.BRepGraphInc.EdgeDef:
        """Current parent definition (typed lookup via DefTraits)."""

    def Index(self) -> int: ...

    def Size(self) -> int: ...

    def Value(self, theIndex: int) -> BRepGraph_EdgeId:
        """
        Returns the parent ID at the given bucket index (does NOT check removal status).
        """

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_CompoundsOfVertex:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ChildRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ChildRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_CompoundsOfVertex) -> None: ...

    def __iter__(self) -> BRepGraph_CompoundsOfVertex:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_CompoundId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_CompoundId: ...

    def CurrentParentId(self) -> BRepGraph_CompoundId: ...

    def CurrentRefId(self) -> BRepGraph_ChildRefId: ...

    def Current(self) -> BRepGraph_CompoundId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.CompoundDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_WireFromEdgeCoEdgeTraits:
    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theStartIndex: int) -> None:
        """
        Construct starting at a given coedge relation index (for resumable iteration).
        """

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_WireFromEdgeCoEdgeTraits) -> None: ...

    def __iter__(self) -> BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_WireFromEdgeCoEdgeTraits:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_WireId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_WireId: ...

    def Current(self) -> BRepGraph_WireId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.WireDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_WiresOfEdge(BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_WireFromEdgeCoEdgeTraits):
    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theStartIndex: int) -> None:
        """
        Construct starting at a given coedge relation index (for resumable iteration).
        """

    @overload
    def __init__(self, theOther: BRepGraph_WiresOfEdge) -> None: ...

class BRepGraph_CoEdgesOfEdge:
    """
    Typed iterator over a relation vector of parent IDs.
    Skips removed parent definitions automatically in sequential iteration.
    Also provides indexed access (Length/Value) for callers that need
    random access into the underlying vector (e.g. BRepGraph_ParentExplorer).
    @tparam TypedIdT Typed ID such as BRepGraph_FaceId, BRepGraph_EdgeId, etc.
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theParents: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_CoEdgeId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theParents: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_CoEdgeId], theStartIndex: int) -> None:
        """
        Construct starting at a given vector index (for resumable iteration).
        Skips to the first non-removed entry at or after theStartIndex.
        """

    @overload
    def __init__(self, theOther: BRepGraph_CoEdgesOfEdge) -> None: ...

    def __iter__(self) -> BRepGraph_CoEdgesOfEdge:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_CoEdgeId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_CoEdgeId: ...

    def Current(self) -> BRepGraph_CoEdgeId:
        """
        Alias for CurrentId(), enables range-for via NCollection_ForwardRange Current() priority.
        """

    def Definition(self) -> nanoocp.BRepGraphInc.CoEdgeDef:
        """Current parent definition (typed lookup via DefTraits)."""

    def Index(self) -> int: ...

    def Size(self) -> int: ...

    def Value(self, theIndex: int) -> BRepGraph_CoEdgeId:
        """
        Returns the parent ID at the given bucket index (does NOT check removal status).
        """

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_FaceFromEdgeCoEdgeTraits:
    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theStartIndex: int) -> None:
        """
        Construct starting at a given coedge relation index (for resumable iteration).
        """

    @overload
    def __init__(self, theOther: BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_FaceFromEdgeCoEdgeTraits) -> None: ...

    def __iter__(self) -> BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_FaceFromEdgeCoEdgeTraits:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_FaceId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_FaceId: ...

    def Current(self) -> BRepGraph_FaceId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.FaceDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_FacesOfEdge(BRepGraph_ReverseIterator_EdgeParentsOf__BRepGraph_ReverseIterator_FaceFromEdgeCoEdgeTraits):
    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theStartIndex: int) -> None:
        """
        Construct starting at a given coedge relation index (for resumable iteration).
        """

    @overload
    def __init__(self, theOther: BRepGraph_FacesOfEdge) -> None: ...

class BRepGraph_FacesOfWire:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_WireRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_WireRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_FacesOfWire) -> None: ...

    def __iter__(self) -> BRepGraph_FacesOfWire:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_FaceId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_FaceId: ...

    def CurrentParentId(self) -> BRepGraph_FaceId: ...

    def CurrentRefId(self) -> BRepGraph_WireRefId: ...

    def Current(self) -> BRepGraph_FaceId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.FaceDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_ShellsOfFace:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_FaceRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_FaceRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ShellsOfFace) -> None: ...

    def __iter__(self) -> BRepGraph_ShellsOfFace:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_ShellId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_ShellId: ...

    def CurrentParentId(self) -> BRepGraph_ShellId: ...

    def CurrentRefId(self) -> BRepGraph_FaceRefId: ...

    def Current(self) -> BRepGraph_ShellId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.ShellDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_SolidsOfShell:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ShellRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ShellRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_SolidsOfShell) -> None: ...

    def __iter__(self) -> BRepGraph_SolidsOfShell:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_SolidId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_SolidId: ...

    def CurrentParentId(self) -> BRepGraph_SolidId: ...

    def CurrentRefId(self) -> BRepGraph_ShellRefId: ...

    def Current(self) -> BRepGraph_SolidId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.SolidDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_CompSolidsOfSolid:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_SolidRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_SolidRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_CompSolidsOfSolid) -> None: ...

    def __iter__(self) -> BRepGraph_CompSolidsOfSolid:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_CompSolidId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_CompSolidId: ...

    def CurrentParentId(self) -> BRepGraph_CompSolidId: ...

    def CurrentRefId(self) -> BRepGraph_SolidRefId: ...

    def Current(self) -> BRepGraph_CompSolidId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.CompSolidDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_OccurrencesOfProduct:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_OccurrencesOfProduct) -> None: ...

    def __iter__(self) -> BRepGraph_OccurrencesOfProduct:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_OccurrenceId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_OccurrenceId: ...

    def CurrentParentId(self) -> BRepGraph_OccurrenceId: ...

    def CurrentRefId(self) -> BRepGraph_OccurrenceRefId: ...

    def Current(self) -> BRepGraph_OccurrenceId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_ProductsOfOccurrence:
    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]) -> None: ...

    @overload
    def __init__(self, theGraph: BRepGraph, theRefs: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId], theStartIndex: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_ProductsOfOccurrence) -> None: ...

    def __iter__(self) -> BRepGraph_ProductsOfOccurrence:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_ProductId:
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> BRepGraph_ProductId: ...

    def CurrentParentId(self) -> BRepGraph_ProductId: ...

    def CurrentRefId(self) -> BRepGraph_OccurrenceRefId: ...

    def Current(self) -> BRepGraph_ProductId: ...

    def Definition(self) -> nanoocp.BRepGraphInc.ProductDef: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel: ...

class BRepGraph_RefsWiresOfCoEdge:
    """
    Typed iterator over parent ID relation lists that also resolves the specific
    RefId linking each parent to the child by lookup in the parent definition.
    Used only where the reverse relation stores parent IDs but no ref IDs.
    @tparam TraitsT Traits with: ParentId, ChildId, RefId types,
    FindRef(graph, parentId, childId) -> RefId (invalid if not found)
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theParents: "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>>", theChild: BRepGraph_CoEdgeId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsWiresOfCoEdge) -> None: ...

    def __iter__(self) -> BRepGraph_RefsWiresOfCoEdge:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> "BRepGraph_ReverseIterator::ParentRef<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>, BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>>":
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> "BRepGraph_ReverseIterator::ParentRef<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>, BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>>": ...

    def CurrentParentId(self) -> BRepGraph_WireId: ...

    def CurrentRefId(self) -> BRepGraph_CoEdgeId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_RefsEdgesOfVertex:
    """
    Typed iterator over parent ID relation lists that also resolves the specific
    RefId linking each parent to the child by lookup in the parent definition.
    Used only where the reverse relation stores parent IDs but no ref IDs.
    @tparam TraitsT Traits with: ParentId, ChildId, RefId types,
    FindRef(graph, parentId, childId) -> RefId (invalid if not found)
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theParents: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_EdgeId], theChild: BRepGraph_VertexId) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RefsEdgesOfVertex) -> None: ...

    def __iter__(self) -> BRepGraph_RefsEdgesOfVertex:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> "BRepGraph_ReverseIterator::ParentRef<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>, BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>>":
        """Python addition: see __iter__."""

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> "BRepGraph_ReverseIterator::ParentRef<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>, BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>>": ...

    def CurrentParentId(self) -> BRepGraph_EdgeId: ...

    def CurrentRefId(self) -> BRepGraph_VertexRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_Tool:
    """
    Centralized geometry access for BRepGraph - analogue of BRep_Tool.

    Geometry in BRepGraph is stored in the definition frame (representation
    Location baked via applyRepresentationLocation). Instance Locations live
    on topology Instance/Ref structs (VertexInstance, CoEdgeInstance, WireInstance,
    FaceInstance, ShellInstance, SolidInstance, OccurrenceInstance). This class applies
    ref Locations automatically when accessing 3D geometry.
    Instance structs are lightweight read-only projections produced during
    traversal, while Ref structs are stored reference entries from RefsView;
    this API accepts whichever form naturally carries the required context for
    the queried property.

    Methods are grouped by topology kind via nested classes:
    BRepGraph_Tool::Vertex, Edge, CoEdge, Face, Wire, Shell.
    """

    def __init__(self, theOther: BRepGraph_Tool) -> None: ...

    class Vertex:
        """
        @brief Vertex geometry accessors.

        Provides 3D point retrieval (with or without Location applied) and
        tolerance access.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Tool.Vertex) -> None: ...

        @staticmethod
        def Usage(theGraph: BRepGraph, theVertexRef: BRepGraph_VertexRefId) -> BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Vertex:
            """
            Resolves a vertex reference id to a lightweight usage value.
            @param[in] theGraph     source graph
            @param[in] theVertexRef typed vertex reference identifier
            @return vertex usage, or invalid usage if the reference is invalid or removed
            """

        @overload
        @staticmethod
        def Pnt(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Vertex) -> nanoocp.gp.gp_Pnt:
            """
            Returns the vertex 3D point with VertexUsage Location applied.
            @param[in] theGraph  source graph
            @param[in] theRef    vertex incidence reference carrying Location
            @return transformed 3D point
            """

        @overload
        @staticmethod
        def Pnt(theGraph: BRepGraph, theVertex: BRepGraph_VertexId) -> nanoocp.gp.gp_Pnt:
            """
            Returns the vertex 3D point in definition frame (no Location applied).
            @param[in] theGraph  source graph
            @param[in] theVertex typed vertex definition identifier
            @return 3D point in definition frame
            """

        @overload
        @staticmethod
        def Pnt(theGraph: BRepGraph, theVertexRef: BRepGraph_VertexRefId) -> nanoocp.gp.gp_Pnt:
            """
            Returns the vertex 3D point with vertex reference location applied.
            @param[in] theGraph     source graph
            @param[in] theVertexRef typed vertex reference identifier
            @return transformed 3D point
            """

        @overload
        @staticmethod
        def Tolerance(theGraph: BRepGraph, theVertex: BRepGraph_VertexId) -> float:
            """
            Returns the vertex tolerance.
            @param[in] theGraph  source graph
            @param[in] theVertex typed vertex definition identifier
            @return tolerance value
            """

        @overload
        @staticmethod
        def Tolerance(theGraph: BRepGraph, theVertexRef: BRepGraph_VertexRefId) -> float:
            """
            Returns the vertex tolerance by vertex reference identifier.
            @param[in] theGraph     source graph
            @param[in] theVertexRef typed vertex reference identifier
            @return tolerance value
            """

        @staticmethod
        def NbEdges(theGraph: BRepGraph, theVertex: BRepGraph_VertexId) -> int:
            """
            Returns the number of edges that reference this vertex.
            @param[in] theGraph  source graph
            @param[in] theVertex typed vertex definition identifier
            @return edge count
            """

    class Edge:
        """
        @brief Edge geometry, curve, and continuity accessors.

        Provides tolerance, degeneracy, and parameter flags; raw and
        location-adjusted 3D curve access; and PCurve lookup for edge-face
        contexts including seam edge support.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Tool.Edge) -> None: ...

        @staticmethod
        def Tolerance(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> float:
            """
            Returns the edge tolerance.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return tolerance value
            """

        @staticmethod
        def Degenerated(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> bool:
            """
            Returns true if the edge is degenerate, derived from current geometry.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return true if degenerate
            """

        @staticmethod
        def IsClosed(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> bool:
            """
            Returns true if the edge forms a topological loop, derived from vertex topology.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return true if closed
            """

        @staticmethod
        def Range(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> tuple[float, float]:
            """
            Returns the 3D curve parameter range as (first, last).
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return pair of (first, last) parameters
            """

        @staticmethod
        def StartVertexId(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> BRepGraph_VertexRefId:
            """
            Returns the start vertex reference id directly.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return start vertex reference id
            """

        @staticmethod
        def EndVertexId(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> BRepGraph_VertexRefId:
            """
            Returns the end vertex reference id directly.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return end vertex reference id
            """

        @staticmethod
        def HasCurve(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> bool:
            """
            Returns true if the edge has a 3D curve representation.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return true if edge has a 3D curve
            """

        @overload
        @staticmethod
        def Curve(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> nanoocp.Geom.Geom_Curve:
            """
            Returns the raw 3D curve handle (definition frame, no copy).
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return curve handle, or null handle if no curve
            """

        @overload
        @staticmethod
        def Curve(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge) -> nanoocp.Geom.Geom_Curve:
            """
            Returns the transformed 3D curve handle via CoEdgeUsage (applies Location, may copy).
            @param[in] theGraph source graph
            @param[in] theRef   coedge incidence reference carrying Location
            @return transformed curve handle
            """

        @overload
        @staticmethod
        def CurveAdaptor(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedCurve:
            """
            Returns the 3D curve adaptor in definition frame (identity Trsf).
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return curve adaptor, or empty adaptor if no curve
            """

        @overload
        @staticmethod
        def CurveAdaptor(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedCurve:
            """
            Returns the 3D curve adaptor via CoEdgeUsage (applies edge-in-wire Location in Trsf).
            Falls back to CurveOnSurface when no 3D curve exists.
            @param[in] theGraph source graph
            @param[in] theRef   coedge incidence reference carrying Location
            @return curve adaptor with Location applied
            """

        @staticmethod
        def FindByVertices(theGraph: BRepGraph, theStartVertex: BRepGraph_VertexId, theEndVertex: BRepGraph_VertexId, theToIgnoreOrientation: bool = False) -> BRepGraph_EdgeId:
            """
            Find an active edge by its boundary vertices.
            @param[in] theGraph source graph
            @param[in] theStartVertex start vertex to match
            @param[in] theEndVertex end vertex to match
            @param[in] theToIgnoreOrientation when true, also matches the reverse vertex order
            @return edge id, or invalid if no active edge matches
            """

        @overload
        @staticmethod
        def FindPCurveCoEdgeId(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId) -> BRepGraph_CoEdgeId:
            """
            Find an active coedge carrying PCurve data for the given edge-face use.
            @param[in] theGraph source graph
            @param[in] theEdge  edge definition to match
            @param[in] theFace  face definition to match
            @return matching coedge id, or invalid if the edge/face pair has no active PCurve coedge
            """

        @overload
        @staticmethod
        def FindPCurveCoEdgeId(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId, theOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> BRepGraph_CoEdgeId:
            """
            Find an active PCurve coedge for the given edge-face use and preferred orientation.
            @param[in] theGraph      source graph
            @param[in] theEdge       edge definition to match
            @param[in] theFace       face definition to match
            @param[in] theOrientation preferred coedge orientation
            @return exact orientation match when present; otherwise the first active PCurve
            coedge on the edge-face pair; invalid if there is no active PCurve coedge
            """

        @overload
        @staticmethod
        def FindCoEdgeId(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId) -> BRepGraph_CoEdgeId:
            """
            Find an active coedge for the given edge-face use.
            @param[in] theGraph source graph
            @param[in] theEdge  edge definition to match
            @param[in] theFace  face definition to match
            @return matching coedge id, or invalid if the edge/face pair has no active coedge
            """

        @overload
        @staticmethod
        def FindCoEdgeId(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId, theOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> BRepGraph_CoEdgeId:
            """
            Find an active coedge for the given edge-face use and preferred orientation.
            @param[in] theGraph      source graph
            @param[in] theEdge       edge definition to match
            @param[in] theFace       face definition to match
            @param[in] theOrientation preferred coedge orientation
            @return exact orientation match when present; otherwise the first active coedge on the
            edge-face pair; invalid if there is no active coedge for the edge-face pair
            """

        @staticmethod
        def NbFaces(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> int:
            """
            Returns the number of faces that reference this edge via coedges.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return face count
            """

        @staticmethod
        def IsManifold(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> bool:
            """
            Returns true if the edge is shared by exactly two faces (manifold).
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return true if manifold
            """

        @staticmethod
        def IsBoundary(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId) -> bool:
            """
            Returns true if the edge belongs to exactly one face (boundary / free edge).
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @return true if boundary
            """

        @staticmethod
        def IsSeamOnFace(theGraph: BRepGraph, theEdge: BRepGraph_EdgeId, theFace: BRepGraph_FaceId) -> bool:
            """
            Returns true if the edge is a seam on the given face.
            @param[in] theGraph source graph
            @param[in] theEdge  typed edge definition identifier
            @param[in] theFace  typed face definition identifier
            @return true if the edge is a seam on this face
            """

        @staticmethod
        def CurveOnSurface(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge, theFace: BRepGraph_FaceId) -> nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface:
            """
            Returns a CurveOnSurface adaptor built from a CoEdgeUsage and face.
            @param[in] theGraph source graph
            @param[in] theRef   coedge incidence reference
            @param[in] theFace  typed face definition identifier
            @return adaptor handle, or null if PCurve or surface is missing
            """

    class CoEdge:
        """
        @brief CoEdge (half-edge) parametric curve accessors.

        Provides PCurve retrieval, adaptor construction, UV endpoint
        access, and parameter range queries for coedge definitions.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Tool.CoEdge) -> None: ...

        @staticmethod
        def Orientation(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.TopAbs.TopAbs_Orientation:
            """
            Returns the coedge orientation relative to its parent edge.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return orientation enum
            """

        @staticmethod
        def IsReversed(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> bool:
            """
            Returns true if the coedge is REVERSED relative to its parent edge.
            Convenience shortcut for `Orientation(...) == TopAbs_REVERSED`.
            """

        @staticmethod
        def EdgeOf(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_EdgeId:
            """
            Returns the parent edge definition id this coedge uses.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return parent edge id (invalid for removed coedges)
            """

        @staticmethod
        def FaceOf(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_FaceId:
            """
            Returns the owning face definition id for this coedge.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return owning face id (invalid for free-wire coedges)
            """

        @staticmethod
        def SeamPair(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> BRepGraph_CoEdgeId:
            """
            Returns the seam-pair coedge for closed/seam edges.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return paired coedge id, or invalid if this coedge is not a seam half
            """

        @staticmethod
        def IsSeam(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> bool:
            """Returns true if this coedge is one half of a seam pair."""

        @staticmethod
        def HasPCurve(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> bool:
            """
            Returns true if the coedge has a PCurve representation.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return true if PCurve exists
            """

        @staticmethod
        def SameParameter(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> bool:
            """
            Returns true if the coedge's PCurve parameter matches the 3D curve.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return true if same parameter
            """

        @staticmethod
        def SameRange(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> bool:
            """
            Returns true if the coedge's PCurve range equals the 3D curve range.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return true if same range
            """

        @staticmethod
        def PCurve(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Geom2d.Geom2d_Curve:
            """
            Returns the raw PCurve handle by coedge identifier (no Location - UV space).
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return curve handle, or null handle if no PCurve
            """

        @overload
        @staticmethod
        def PCurveAdaptor(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
            """
            Returns a PCurve adaptor by coedge identifier.
            If the coedge has a stored PCurve (Curve2DRepIdx >= 0), returns it directly.
            Otherwise, for planar face surfaces, computes the PCurve on-the-fly by projecting
            the edge's 3D curve onto the plane (CurveOnPlane), mirroring the behavior of
            BRep_Tool::CurveOnSurface for planar faces without stored PCurves.
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return 2D curve adaptor, or empty adaptor if no PCurve and surface is not planar
            """

        @overload
        @staticmethod
        def PCurveAdaptor(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
            """
            Returns a PCurve adaptor from a CoEdgeUsage.
            @param[in] theGraph source graph
            @param[in] theRef   coedge incidence reference
            @return 2D curve adaptor
            """

        @staticmethod
        def UVPoints(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> tuple[nanoocp.gp.gp_Pnt2d, nanoocp.gp.gp_Pnt2d]:
            """
            Returns the UV endpoints from a CoEdge as (UV1, UV2).
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return pair of 2D points at parameter first and last
            """

        @staticmethod
        def Range(theGraph: BRepGraph, theCoEdge: BRepGraph_CoEdgeId) -> tuple[float, float]:
            """
            Returns the PCurve parameter range as (first, last).
            @param[in] theGraph  source graph
            @param[in] theCoEdge typed coedge definition identifier
            @return pair of (first, last) parameters
            """

    class Face:
        """
        @brief Face surface and property accessors.

        Provides tolerance, natural restriction flag, surface handle
        and adaptor access (with optional UV bounds), and outer wire lookup.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Tool.Face) -> None: ...

        @staticmethod
        def Usage(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face:
            """
            Resolves a face reference id to a lightweight usage value.
            @param[in] theGraph   source graph
            @param[in] theFaceRef typed face reference identifier
            @return face usage, or invalid usage if the reference is invalid or removed
            """

        @overload
        @staticmethod
        def Tolerance(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> float:
            """
            Returns the face tolerance.
            @param[in] theGraph source graph
            @param[in] theFace  typed face definition identifier
            @return tolerance value
            """

        @overload
        @staticmethod
        def Tolerance(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> float:
            """Returns the face tolerance by face reference identifier."""

        @overload
        @staticmethod
        def HasSurface(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> bool:
            """
            Returns true if the face has a surface representation.
            @param[in] theGraph source graph
            @param[in] theFace  typed face definition identifier
            @return true if surface exists
            """

        @overload
        @staticmethod
        def HasSurface(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> bool:
            """Returns true if the face reference resolves to a face with a surface."""

        @overload
        @staticmethod
        def OuterWire(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> BRepGraph_WireId:
            """
            Returns the outer wire definition id directly.
            @param[in] theGraph source graph
            @param[in] theFace  typed face definition identifier
            @return outer wire id, or invalid if the face has no wire
            """

        @overload
        @staticmethod
        def OuterWire(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> BRepGraph_WireId:
            """Returns the outer wire definition id by face reference identifier."""

        @overload
        @staticmethod
        def Surface(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> nanoocp.Geom.Geom_Surface:
            """
            Returns the raw surface handle (definition frame, no copy).
            @param[in] theGraph source graph
            @param[in] theFace  typed face definition identifier
            @return surface handle, or null handle if no surface
            """

        @overload
        @staticmethod
        def Surface(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> nanoocp.Geom.Geom_Surface:
            """Returns the raw surface handle by face reference identifier."""

        @overload
        @staticmethod
        def SurfaceAdaptor(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface:
            """
            Returns a surface adaptor in definition frame.
            @param[in] theGraph source graph
            @param[in] theFace  typed face definition identifier
            @return surface adaptor, or empty adaptor if no surface
            """

        @overload
        @staticmethod
        def SurfaceAdaptor(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface:
            """Returns a surface adaptor with FaceUsage Location applied."""

        @overload
        @staticmethod
        def SurfaceAdaptor(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface:
            """
            Returns a surface adaptor by face reference identifier with reference Location applied.
            """

        @overload
        @staticmethod
        def SurfaceAdaptor(theGraph: BRepGraph, theFace: BRepGraph_FaceId, theUFirst: float, theULast: float, theVFirst: float, theVLast: float) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface:
            """
            Returns a surface adaptor with explicit UV bounds.
            @param[in] theGraph  source graph
            @param[in] theFace   typed face definition identifier
            @param[in] theUFirst first U parameter
            @param[in] theULast  last U parameter
            @param[in] theVFirst first V parameter
            @param[in] theVLast  last V parameter
            @return surface adaptor with bounds, or empty adaptor if no surface
            """

        @overload
        @staticmethod
        def SurfaceAdaptor(theGraph: BRepGraph, theRef: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face, theUFirst: float, theULast: float, theVFirst: float, theVLast: float) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface:
            """
            Returns a surface adaptor with explicit UV bounds and FaceUsage Location applied.
            """

        @overload
        @staticmethod
        def SurfaceAdaptor(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId, theUFirst: float, theULast: float, theVFirst: float, theVLast: float) -> nanoocp.GeomAdaptor.GeomAdaptor_TransformedSurface:
            """
            Returns a surface adaptor with explicit UV bounds by face reference identifier.
            """

        @overload
        @staticmethod
        def NbWires(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> int:
            """
            Returns the number of wire references on the face (outer + holes).
            @param[in] theGraph source graph
            @param[in] theFace  typed face definition identifier
            @return wire count (includes removed refs)
            """

        @overload
        @staticmethod
        def NbWires(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> int:
            """Returns the number of wire references by face reference identifier."""

        @overload
        @staticmethod
        def Bounds(theGraph: BRepGraph, theFace: BRepGraph_FaceId) -> tuple[float, float, float, float]:
            """
            Returns the UV parameter bounds of the face surface.
            Fills out-parameters with the surface bounds; all values are set to 0.0 if
            the face has no surface.
            @param[in]  theGraph  source graph
            @param[in]  theFace   typed face definition identifier
            @param[out] theUMin   minimum U parameter
            @param[out] theUMax   maximum U parameter
            @param[out] theVMin   minimum V parameter
            @param[out] theVMax   maximum V parameter
            """

        @overload
        @staticmethod
        def Bounds(theGraph: BRepGraph, theFaceRef: BRepGraph_FaceRefId) -> tuple[float, float, float, float]:
            """Returns the UV parameter bounds by face reference identifier."""

    class Wire:
        """
        @brief Wire property accessors.

        Provides wire closure, size, and ownership queries.
        For ordered coedge traversal, use BRepGraph_CoEdgesOfWire or
        TopoView::Wires().Relations(theWire).CoEdgeIds.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Tool.Wire) -> None: ...

        @staticmethod
        def Usage(theGraph: BRepGraph, theWireRef: BRepGraph_WireRefId) -> BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire:
            """
            Resolves a wire reference id to a lightweight usage value.
            @param[in] theGraph   source graph
            @param[in] theWireRef typed wire reference identifier
            @return wire usage, or invalid usage if the reference is invalid or removed
            """

        @overload
        @staticmethod
        def IsClosed(theGraph: BRepGraph, theWire: BRepGraph_WireId) -> bool:
            """
            Returns true if the wire is topologically closed, derived from ordered coedge chain.
            @param[in] theGraph source graph
            @param[in] theWire  typed wire definition identifier
            @return true if closed
            """

        @overload
        @staticmethod
        def IsClosed(theGraph: BRepGraph, theWireRef: BRepGraph_WireRefId) -> bool:
            """Returns true if the referenced wire is topologically closed."""

        @overload
        @staticmethod
        def NbCoEdges(theGraph: BRepGraph, theWire: BRepGraph_WireId) -> int:
            """
            Number of CoEdge usages in the wire (raw count: seam halves count twice,
            matching TopoDS_Iterator(wire) semantics).
            @param[in] theGraph source graph
            @param[in] theWire  typed wire definition identifier
            @return number of coedge entries
            """

        @overload
        @staticmethod
        def NbCoEdges(theGraph: BRepGraph, theWireRef: BRepGraph_WireRefId) -> int:
            """Number of CoEdge usages in the referenced wire."""

        @overload
        @staticmethod
        def NbDistinctEdges(theGraph: BRepGraph, theWire: BRepGraph_WireId) -> int:
            """
            Number of distinct underlying edges in the wire (seam halves count once).
            @param[in] theGraph source graph
            @param[in] theWire  typed wire definition identifier
            @return number of distinct ChildEdgeIds reachable from the wire's CoEdgeIds
            """

        @overload
        @staticmethod
        def NbDistinctEdges(theGraph: BRepGraph, theWireRef: BRepGraph_WireRefId) -> int:
            """Number of distinct underlying edges in the referenced wire."""

        @overload
        @staticmethod
        def FaceOf(theGraph: BRepGraph, theWire: BRepGraph_WireId) -> BRepGraph_FaceId:
            """
            Returns the first owning face for this wire via relation tables.
            Returns an invalid id if the wire has no owning face (free wire).
            @param[in] theGraph source graph
            @param[in] theWire  typed wire definition identifier
            @return owning face id, or invalid
            """

        @overload
        @staticmethod
        def FaceOf(theGraph: BRepGraph, theWireRef: BRepGraph_WireRefId) -> BRepGraph_FaceId:
            """Returns the first owning face for the referenced wire."""

        @overload
        @staticmethod
        def IsOuter(theGraph: BRepGraph, theWire: BRepGraph_WireId) -> bool:
            """
            Returns true if this wire is the first active wire of its owning face.
            Scans WireRefs that reference this wire.
            Returns false for free wires (no owning face).
            @param[in] theGraph source graph
            @param[in] theWire  typed wire definition identifier
            @return true if outer wire
            """

        @overload
        @staticmethod
        def IsOuter(theGraph: BRepGraph, theWireRef: BRepGraph_WireRefId) -> bool:
            """
            Returns true if the referenced wire is the outer wire of its owning face.
            """

    class Shell:
        """
        @brief Shell property accessors.

        Provides shell closure and face count queries.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Tool.Shell) -> None: ...

        @staticmethod
        def Usage(theGraph: BRepGraph, theShellRef: BRepGraph_ShellRefId) -> BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell:
            """
            Resolves a shell reference id to a lightweight usage value.
            @param[in] theGraph    source graph
            @param[in] theShellRef typed shell reference identifier
            @return shell usage, or invalid usage if the reference is invalid or removed
            """

        @overload
        @staticmethod
        def IsClosed(theGraph: BRepGraph, theShell: BRepGraph_ShellId) -> bool:
            """
            Returns true if the shell is topologically closed, derived from face-boundary edge
            incidence.
            @param[in] theGraph source graph
            @param[in] theShell typed shell definition identifier
            @return true if closed
            """

        @overload
        @staticmethod
        def IsClosed(theGraph: BRepGraph, theShellRef: BRepGraph_ShellRefId) -> bool:
            """Returns true if the referenced shell is topologically closed."""

        @overload
        @staticmethod
        def NbFaces(theGraph: BRepGraph, theShell: BRepGraph_ShellId) -> int:
            """
            Returns the number of face references in the shell.
            @param[in] theGraph source graph
            @param[in] theShell typed shell definition identifier
            @return number of face entries (including removed)
            """

        @overload
        @staticmethod
        def NbFaces(theGraph: BRepGraph, theShellRef: BRepGraph_ShellRefId) -> int:
            """Returns the number of face references in the referenced shell."""

class BRepGraph_RelatedIterator:
    """
    @brief Single-level iterator over semantically related topology nodes.
    @see BRepGraph class comment "Iterator guide" for choosing between iterator types.

    The iterator yields immediate related nodes for one source node together
    with the relation kind explaining why each node is returned. Results are not
    deduplicated; callers that need uniqueness should filter on top.
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theNode: BRepGraph_NodeId) -> None:
        """
        Construct an iterator over all semantically related nodes of the given source node.
        @param[in] theGraph graph containing the node
        @param[in] theNode  source node whose relations are iterated
        """

    @overload
    def __init__(self, theOther: BRepGraph_RelatedIterator) -> None: ...

    class RelationKind(enum.Enum):
        """
        Topological relation kinds yielded by the iterator.
        Only geometry-level relations are supported (Face, Edge, Vertex, Wire, CoEdge).
        Assembly/container nodes (Solid, Shell, Compound, Product, Occurrence) have
        no topological relations - use BRepGraph_ChildExplorer / BRepGraph_ParentExplorer instead.
        """

        BoundaryEdge = 0

        AdjacentFace = 1

        OuterWire = 2

        ReferencedByFace = 3

        IncidentVertex = 4

        WireCoEdge = 5

        OwningFace = 6

        IncidentEdge = 7

        ParentEdge = 8

        SeamPair = 9

    class Stage(enum.Enum):
        """Internal traversal stage tracking which sub-iteration is active."""

        First = 0

        Second = 1

        Third = 2

        Finished = 3

    def __iter__(self) -> BRepGraph_RelatedIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_NodeId:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """True if another related node is available."""

    def Next(self) -> None:
        """Advance to the next related node."""

    def Current(self) -> BRepGraph_NodeId:
        """Return the current related node id."""

    def CurrentRelation(self) -> BRepGraph_RelatedIterator.RelationKind:
        """Return the relation kind explaining why the current node is related."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class BRepGraph_SupplementIterator:
    """
    @brief Iterator over supplemental TopoDS attachments owned by one core node.

    The iterator resolves `BRepGraph_LayerTopoSupplement` through the graph layer
    registry and yields only explicit supplement attachments. Core traversal
    remains core-only and does not surface these entries.
    """

    @overload
    def __init__(self, theGraph: BRepGraph, theOwner: BRepGraph_NodeId) -> None:
        """
        @brief Construct an iterator over supplement attachments of one owner.
        @param[in] theGraph graph providing the supplement layer
        @param[in] theOwner core owner node whose attachments should be iterated
        """

    @overload
    def __init__(self, theOther: BRepGraph_SupplementIterator) -> None: ...

    def __iter__(self) -> BRepGraph_SupplementIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> BRepGraph_LayerTopoSupplement.Entry:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """
        @brief Return true when the iterator currently points to an attachment.
        """

    def Next(self) -> None:
        """@brief Advance to the next attachment."""

    def Uid(self) -> int:
        """@brief Return the current layer-local attachment uid."""

    def Value(self) -> BRepGraph_LayerTopoSupplement.Entry:
        """@brief Return the current attachment entry."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """@brief Sentinel marking end of iteration."""

class BRepGraph_Deduplicate:
    """
    @brief Deep geometry deduplication algorithm over an existing BRepGraph.

    This algorithm canonicalizes deep-equal geometry references (surfaces and
    3D curves) using GeomHash hashers. It updates face/edge definition links to
    canonical geometry nodes and can record lineage in graph history.

    First implementation intentionally does not merge edge/face definitions yet.
    """

    def __init__(self, theOther: BRepGraph_Deduplicate) -> None: ...

    class Options:
        """Configuration for graph deduplication run."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Deduplicate.Options) -> None: ...

        @property
        def AnalyzeOnly(self) -> bool: ...

        @AnalyzeOnly.setter
        def AnalyzeOnly(self, arg: bool, /) -> None: ...

        @property
        def HistoryMode(self) -> bool: ...

        @HistoryMode.setter
        def HistoryMode(self, arg: bool, /) -> None: ...

        @property
        def MergeEntitiesWhenSafe(self) -> bool: ...

        @MergeEntitiesWhenSafe.setter
        def MergeEntitiesWhenSafe(self, arg: bool, /) -> None: ...

        @property
        def CompTolerance(self) -> float: ...

        @CompTolerance.setter
        def CompTolerance(self, arg: float, /) -> None: ...

        @property
        def HashTolerance(self) -> float: ...

        @HashTolerance.setter
        def HashTolerance(self, arg: float, /) -> None: ...

    class Result:
        """Result counters for diagnostics and tests."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Deduplicate.Result) -> None: ...

        @property
        def NbCanonicalSurfaces(self) -> int: ...

        @NbCanonicalSurfaces.setter
        def NbCanonicalSurfaces(self, arg: int, /) -> None: ...

        @property
        def NbCanonicalCurves(self) -> int: ...

        @NbCanonicalCurves.setter
        def NbCanonicalCurves(self, arg: int, /) -> None: ...

        @property
        def NbSurfaceRewrites(self) -> int: ...

        @NbSurfaceRewrites.setter
        def NbSurfaceRewrites(self, arg: int, /) -> None: ...

        @property
        def NbCurveRewrites(self) -> int: ...

        @NbCurveRewrites.setter
        def NbCurveRewrites(self, arg: int, /) -> None: ...

        @property
        def NbNullifiedSurfaces(self) -> int: ...

        @NbNullifiedSurfaces.setter
        def NbNullifiedSurfaces(self, arg: int, /) -> None: ...

        @property
        def NbNullifiedCurves(self) -> int: ...

        @NbNullifiedCurves.setter
        def NbNullifiedCurves(self, arg: int, /) -> None: ...

        @property
        def NbHistoryRecords(self) -> int: ...

        @NbHistoryRecords.setter
        def NbHistoryRecords(self, arg: int, /) -> None: ...

        @property
        def IsEntityMergeApplied(self) -> bool: ...

        @IsEntityMergeApplied.setter
        def IsEntityMergeApplied(self, arg: bool, /) -> None: ...

        @property
        def NbMergedVertices(self) -> int:
            """
            Topology definition merge counters (active when MergeEntitiesWhenSafe = true).
            """

        @NbMergedVertices.setter
        def NbMergedVertices(self, arg: int, /) -> None: ...

        @property
        def NbMergedEdges(self) -> int: ...

        @NbMergedEdges.setter
        def NbMergedEdges(self, arg: int, /) -> None: ...

        @property
        def NbMergedWires(self) -> int: ...

        @NbMergedWires.setter
        def NbMergedWires(self, arg: int, /) -> None: ...

        @property
        def NbMergedFaces(self) -> int: ...

        @NbMergedFaces.setter
        def NbMergedFaces(self, arg: int, /) -> None: ...

        @property
        def NbReorderedWires(self) -> int: ...

        @NbReorderedWires.setter
        def NbReorderedWires(self, arg: int, /) -> None: ...

        @property
        def NbToleranceOrderedWires(self) -> int: ...

        @NbToleranceOrderedWires.setter
        def NbToleranceOrderedWires(self, arg: int, /) -> None: ...

        @property
        def NbPartialOrderedWires(self) -> int: ...

        @NbPartialOrderedWires.setter
        def NbPartialOrderedWires(self, arg: int, /) -> None: ...

        @property
        def AffectedFaces(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_FaceId]:
            """Faces whose SurfNodeId changed."""

        @AffectedFaces.setter
        def AffectedFaces(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_FaceId], /) -> None: ...

        @property
        def AffectedEdges(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_EdgeId]:
            """Edges whose CurveNodeId changed."""

        @AffectedEdges.setter
        def AffectedEdges(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_EdgeId], /) -> None: ...

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph) -> BRepGraph_Deduplicate.Result:
        """
        Run deduplication on a built graph.
        @param[in,out] theGraph graph to update
        @return dedup statistics
        """

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph, theOptions: BRepGraph_Deduplicate.Options) -> BRepGraph_Deduplicate.Result:
        """
        Run deduplication on a built graph.
        @param[in,out] theGraph graph to update
        @param[in] theOptions dedup configuration
        @return dedup statistics
        """

class BRepGraph_Compact:
    """
    @brief Graph compaction algorithm that reclaims removed node slots.

    After deduplication or other operations that mark nodes as removed,
    this algorithm rebuilds the graph with dense index arrays, eliminating
    all removed nodes and reassigning indices to be contiguous.

    Strategy: rebuild-and-swap. A fresh BRepGraph is constructed from
    non-removed nodes with remapped indices, then move-assigned into
    the input graph.
    """

    def __init__(self, theOther: BRepGraph_Compact) -> None: ...

    class Options:
        """Configuration for compaction."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Compact.Options) -> None: ...

        class CachePolicy(enum.Enum):
            Drop = 0

            CopyFresh = 1

        @property
        def HistoryMode(self) -> bool:
            """Record index remapping in history."""

        @HistoryMode.setter
        def HistoryMode(self, arg: bool, /) -> None: ...

        @property
        def CacheMode(self) -> BRepGraph_Compact.Options.CachePolicy:
            """Runtime cache migration policy."""

        @CacheMode.setter
        def CacheMode(self, arg: BRepGraph_Compact.Options.CachePolicy, /) -> None: ...

    class Result:
        """Result counters for diagnostics."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Compact.Result) -> None: ...

        @property
        def NbRemovedVertices(self) -> int: ...

        @NbRemovedVertices.setter
        def NbRemovedVertices(self, arg: int, /) -> None: ...

        @property
        def NbRemovedEdges(self) -> int: ...

        @NbRemovedEdges.setter
        def NbRemovedEdges(self, arg: int, /) -> None: ...

        @property
        def NbRemovedWires(self) -> int: ...

        @NbRemovedWires.setter
        def NbRemovedWires(self, arg: int, /) -> None: ...

        @property
        def NbRemovedFaces(self) -> int: ...

        @NbRemovedFaces.setter
        def NbRemovedFaces(self, arg: int, /) -> None: ...

        @property
        def NbRemovedShells(self) -> int: ...

        @NbRemovedShells.setter
        def NbRemovedShells(self, arg: int, /) -> None: ...

        @property
        def NbRemovedSolids(self) -> int: ...

        @NbRemovedSolids.setter
        def NbRemovedSolids(self, arg: int, /) -> None: ...

        @property
        def NbRemovedCompounds(self) -> int: ...

        @NbRemovedCompounds.setter
        def NbRemovedCompounds(self, arg: int, /) -> None: ...

        @property
        def NbRemovedCompSolids(self) -> int: ...

        @NbRemovedCompSolids.setter
        def NbRemovedCompSolids(self, arg: int, /) -> None: ...

        @property
        def NbRemovedSurfaces(self) -> int: ...

        @NbRemovedSurfaces.setter
        def NbRemovedSurfaces(self, arg: int, /) -> None: ...

        @property
        def NbRemovedCurves(self) -> int: ...

        @NbRemovedCurves.setter
        def NbRemovedCurves(self, arg: int, /) -> None: ...

        @property
        def NbNodesBefore(self) -> int: ...

        @NbNodesBefore.setter
        def NbNodesBefore(self, arg: int, /) -> None: ...

        @property
        def NbNodesAfter(self) -> int: ...

        @NbNodesAfter.setter
        def NbNodesAfter(self, arg: int, /) -> None: ...

        @property
        def NbUnmappedActiveDefs(self) -> int: ...

        @NbUnmappedActiveDefs.setter
        def NbUnmappedActiveDefs(self, arg: int, /) -> None: ...

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph) -> BRepGraph_Compact.Result:
        """
        Run compaction with default options.
        @param[in,out] theGraph graph to compact
        @return compaction statistics
        """

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph, theOptions: BRepGraph_Compact.Options) -> BRepGraph_Compact.Result:
        """
        Run compaction with specified options.
        @param[in,out] theGraph graph to compact
        @param[in] theOptions compaction configuration
        @return compaction statistics
        """

class BRepGraph_Copy:
    """
    @brief Graph-to-graph deep copy.

    Produces a new BRepGraph from an existing one in a single bottom-up pass,
    avoiding the 5-7 traversals of BRepTools_Modifier used by BRepBuilderAPI_Copy.

    Two copy modes:
    - External: source and target are different graphs. Target receives the copied data.
    - Self-copy: source and target are the same graph. The specified sub-graph is
    duplicated with new entity IDs; shared dependencies (geometry, vertices referenced
    from outside the sub-graph) are preserved.

    Geometry and mesh policies are controlled by the GeomPolicy and MeshPolicy enums.

    @note Check the return value for success: Perform returns bool,
    CopyNode returns the mapped root NodeId (invalid on failure).

    ## Typical usage
    @code
    BRepGraph aGraph;
    aGraph.Shapes().Add(myShape);
    BRepGraph aCopy;
    BRepGraph_Copy::Perform(aGraph, aCopy);
    TopoDS_Shape aShape = aCopy.Shapes().Shape();
    @endcode
    """

    def __init__(self, theOther: BRepGraph_Copy) -> None: ...

    class GeomPolicy(enum.Enum):
        """
        Policy for handling geometry handles (Geom_Curve, Geom_Surface, Geom2d_Curve).
        """

        Copy = 0

        Share = 1

        Drop = 2

    class MeshPolicy(enum.Enum):
        """
        Policy for handling mesh data (Poly_Triangulation, Poly_Polygon3D,
        Poly_PolygonOnTriangulation).
        """

        Copy = 0

        Share = 1

        Drop = 2

    class CachePolicy(enum.Enum):
        """Policy for handling transient runtime cache services."""

        Drop = 0

        CopyFresh = 1

    @staticmethod
    def Perform(theSourceGraph: BRepGraph, theTargetGraph: BRepGraph, theGeomPolicy: BRepGraph_Copy.GeomPolicy = BRepGraph_Copy.GeomPolicy.Copy, theMeshPolicy: BRepGraph_Copy.MeshPolicy = BRepGraph_Copy.MeshPolicy.Copy, theCachePolicy: BRepGraph_Copy.CachePolicy = BRepGraph_Copy.CachePolicy.Drop) -> bool:
        """
        Copy the entire source graph into the target graph.

        Self-copy (theSourceGraph == theTargetGraph):
        Identity no-op, returns true immediately.

        External copy to empty target (theTargetGraph.IsEmpty()):
        Uses identity-mapped fast path (old index == new index).

        External copy to non-empty target:
        Uses explicit mapping; IDs in theTargetGraph will differ from theSourceGraph.
        Entities from theSourceGraph are appended to theTargetGraph.

        @param[in] theSourceGraph a pre-built BRepGraph (must not be empty)
        @param[in,out] theTargetGraph destination graph (may already contain data)
        @param[in] theGeomPolicy geometry handle policy (default: Copy)
        @param[in] theMeshPolicy mesh data policy (default: Copy)
        @return true on success, false on failure (empty source)
        """

    @staticmethod
    def CopyNode(theSourceGraph: BRepGraph, theTargetGraph: BRepGraph, theNodeId: BRepGraph_NodeId, theGeomPolicy: BRepGraph_Copy.GeomPolicy = BRepGraph_Copy.GeomPolicy.Copy, theMeshPolicy: BRepGraph_Copy.MeshPolicy = BRepGraph_Copy.MeshPolicy.Copy, theCachePolicy: BRepGraph_Copy.CachePolicy = BRepGraph_Copy.CachePolicy.Drop) -> BRepGraph_NodeId:
        """
        Copy a single node sub-graph of any kind (Face, Shell, Solid, Wire, Edge, Vertex, etc.).
        The target graph receives the specified node and all entities it references.

        External copy (theSourceGraph != theTargetGraph):
        New entities are appended to theTargetGraph. Entities already present
        in theTargetGraph are reused (not duplicated).

        Self-copy (theSourceGraph == theTargetGraph):
        The specified sub-graph is duplicated with new entity IDs within the same graph.
        Shared dependencies (vertices, edges referenced from outside the sub-graph)
        are preserved as-is.

        @param[in] theSourceGraph a pre-built BRepGraph
        @param[in,out] theTargetGraph destination graph (may already contain data)
        @param[in] theNodeId node identifier (any kind)
        @param[in] theGeomPolicy geometry handle policy (default: Copy)
        @param[in] theMeshPolicy mesh data policy (default: Copy)
        @return the mapped root NodeId in theTargetGraph, or invalid NodeId on failure
        """

class BRepGraph_Transform:
    """
    @brief Graph-to-graph transformation.

    Applies a geometric transformation to vertex points and geometry node
    locations by copying into a target graph, then transforming in-place.

    Two geometry modes (matching BRepBuilderAPI_Transform semantics):
    - GeomPolicy::Copy (geometry-level): deep-copy geometry, create new
    transformed handles via Geom_Geometry::Transformed(), reset locations
    to identity.
    - GeomPolicy::Share (root-level): light-copy with shared geometry, apply
    transform via location modification only.

    Mesh handling (MeshPolicy parameter):
    - MeshPolicy::Drop (default for Transform): triangulations and polygons are
    discarded after a geometry-level transform and must be recomputed.
    - MeshPolicy::Copy: all mesh data (Poly_Triangulation on FaceDefs and the
    MeshLayer cache, Poly_Polygon3D on edges, Poly_PolygonOnTriangulation on
    coedges) is copied and transformed in sync with the geometry.
    In location-only mode the mesh data is copied as-is (nodes stay in the
    graph coordinate system, which is unaffected by a pure location compose).

    @note Check the return value for success: Perform returns bool,
    TransformNode returns the mapped root NodeId (invalid on failure).

    ## Typical usage
    @code
    BRepGraph aGraph;
    aGraph.Shapes().Add(myShape);
    gp_Trsf aTrsf;
    aTrsf.SetTranslation(gp_Vec(10.0, 0.0, 0.0));
    BRepGraph aTransformed;
    BRepGraph_Transform::Perform(aGraph, aTransformed, aTrsf);
    TopoDS_Shape aShape = aTransformed.Shapes().Shape();
    @endcode
    """

    def __init__(self, theOther: BRepGraph_Transform) -> None: ...

    @staticmethod
    def Perform(theSourceGraph: BRepGraph, theTargetGraph: BRepGraph, theTrsf: nanoocp.gp.gp_Trsf, theGeomPolicy: BRepGraph_Copy.GeomPolicy = BRepGraph_Copy.GeomPolicy.Copy, theMeshPolicy: BRepGraph_Copy.MeshPolicy = BRepGraph_Copy.MeshPolicy.Drop) -> bool:
        """
        Transform the entire graph into a target graph.

        Self-transform (theSourceGraph == theTargetGraph):
        Applies transform in-place on theTargetGraph.

        External transform to empty target (theTargetGraph.IsEmpty()):
        Copies source into target, then transforms.

        External transform to non-empty target:
        Appends source entities into target with explicit mapping, then transforms.

        @param[in] theSourceGraph a pre-built BRepGraph (must not be empty)
        @param[in,out] theTargetGraph destination graph (may already contain data)
        @param[in] theTrsf       the transformation to apply
        @param[in] theGeomPolicy geometry handle policy (default: Copy)
        @param[in] theMeshPolicy mesh data policy (default: Drop)
        @return true on success, false on failure (empty source, or Drop +
        geometry-modification-required)
        """

    @staticmethod
    def TransformNode(theSourceGraph: BRepGraph, theTargetGraph: BRepGraph, theNodeId: BRepGraph_NodeId, theTrsf: nanoocp.gp.gp_Trsf, theGeomPolicy: BRepGraph_Copy.GeomPolicy = BRepGraph_Copy.GeomPolicy.Copy, theMeshPolicy: BRepGraph_Copy.MeshPolicy = BRepGraph_Copy.MeshPolicy.Drop) -> BRepGraph_NodeId:
        """
        Transform a single node sub-graph of any kind.
        Topology nodes are copied and transformed by baking the transform into their definitions.

        Self-transform (theSourceGraph == theTargetGraph):
        Duplicates the sub-graph with new entity IDs, then transforms the copy.

        External transform:
        Copies the sub-graph into theTargetGraph, then transforms.

        @param[in] theSourceGraph a pre-built BRepGraph
        @param[in,out] theTargetGraph destination graph (may already contain data)
        @param[in] theNodeId     node identifier (any kind)
        @param[in] theTrsf       the transformation to apply
        @param[in] theGeomPolicy geometry handle policy (default: Copy; Drop is invalid for topology)
        @param[in] theMeshPolicy mesh data policy (default: Drop)
        @return the mapped root NodeId in theTargetGraph, or invalid NodeId on failure
        """

    @overload
    @staticmethod
    def MoveRef(theGraph: BRepGraph, theRefId: BRepGraph_ChildRefId, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Apply an in-place location-only transform to a child reference.
        Composes theTrsf into ChildRef placement without copying any geometry.
        Cached mesh data on entities downstream of the moved ref is stored in the
        entity's local frame and is unaffected; callers that bake a world transform
        into a cache key own the invalidation responsibility.
        @note Only pure rotation/translation transforms (scale == 1) are supported.
        The method returns false if |scaleFactor| != 1.
        @param[in] theGraph  the graph containing the reference
        @param[in] theRefId  child reference to move
        @param[in] theTrsf   the transformation to compose into the location
        @return true on success; false if the ref is invalid/removed or theTrsf has non-unit scale
        """

    @overload
    @staticmethod
    def MoveRef(theGraph: BRepGraph, theRefId: BRepGraph_OccurrenceRefId, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Apply an in-place location-only transform to an occurrence reference.
        Composes theTrsf into OccurrenceRef placement without copying any geometry.
        @note Only pure rotation/translation transforms (scale == 1) are supported.
        @return true on success; false if the ref is invalid/removed or theTrsf has non-unit scale
        """

class BRepGraph_Validate:
    """
    @brief Structural invariant checker for BRepGraph.

    Read-only algorithm that verifies the graph's internal consistency:
    cross-reference bounds, relation symmetry, incidence ref consistency,
    geometry reference validity, removed-node isolation, and wire connectivity.

    Distinct from BRepGraphCheck (geometric shape validity). This class
    checks the graph data structure itself.

    ### Validation Mode Check Matrix

    | Check                          | Lightweight | Audit |
    |--------------------------------|:-----------:|:-----:|
    | Active entity count boundary   |     YES     |  YES  |
    | Document root product sanity   |     YES     |  YES  |
    | Cross-reference bounds         |      -      |  YES  |
    | Reverse-index consistency      |      -      |  YES  |
    | Face-count cache consistency   |      -      |  YES  |
    | Incidence ref consistency      |      -      |  YES  |
    | Geometry representation refs   |      -      |  YES  |
    | Removed-node isolation         |     YES     |  YES  |
    | Wire edge connectivity         |      -      |  YES  |
    | Entity ID positional integrity |      -      |  YES  |
    | UID round-trip integrity       |      -      |  YES  |
    | Assembly DAG cycle detection   |      -      |  YES  |

    ### Mode Guidance

    | Mode | What it checks | Cost | Recommended use |
    |------|----------------|------|-----------------|
    | `Lightweight` | Active entity count boundary plus removed-node isolation | Low | Hot-path
    release builds when the graph structure is already trusted | | `Audit` | Full structural audit
    from cross-reference bounds through assembly DAG cycle detection | Higher | Default validation
    mode for production pipelines, test gates, and API-boundary verification |

    For production pipelines, prefer `Mode::Audit`; `Mode::Lightweight` is intended
    for hot-path release builds where the graph structure is already trusted.
    """

    def __init__(self, theOther: BRepGraph_Validate) -> None: ...

    class Severity(enum.Enum):
        """Severity level for reported issues."""

        Warning = 0

        Error = 1

    class Mode(enum.Enum):
        """Validation mode controlling check depth/performance trade-off."""

        Lightweight = 0

        Audit = 1

    class Issue:
        """A single structural issue found in the graph."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Validate.Issue) -> None: ...

        @property
        def Sev(self) -> BRepGraph_Validate.Severity: ...

        @Sev.setter
        def Sev(self, arg: BRepGraph_Validate.Severity, /) -> None: ...

        @property
        def NodeId(self) -> BRepGraph_NodeId: ...

        @NodeId.setter
        def NodeId(self, arg: BRepGraph_NodeId, /) -> None: ...

        @property
        def Description(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

        @Description.setter
        def Description(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    class Result:
        """Aggregated validation result."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Validate.Result) -> None: ...

        def IsValid(self) -> bool:
            """True if no Error-level issues were found."""

        def NbIssues(self, theSev: BRepGraph_Validate.Severity) -> int:
            """Count issues of a given severity."""

        @property
        def Issues(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_Validate.Issue]: ...

        @Issues.setter
        def Issues(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_Validate.Issue], /) -> None: ...

    class Options:
        """Validation options."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraph_Validate.Options) -> None: ...

        @staticmethod
        def Lightweight() -> BRepGraph_Validate.Options:
            """Build options for lightweight validation."""

        @staticmethod
        def Audit() -> BRepGraph_Validate.Options:
            """Build options for full-audit validation."""

        @property
        def ValidationMode(self) -> BRepGraph_Validate.Mode:
            """Default mode for regular validation calls."""

        @ValidationMode.setter
        def ValidationMode(self, arg: BRepGraph_Validate.Mode, /) -> None: ...

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph) -> BRepGraph_Validate.Result:
        """
        Run default lightweight structural checks on a built graph.
        Uses Mode::Lightweight; for full structural audit use Perform(theGraph, Mode::Audit).
        @param[in] theGraph graph to validate (const, read-only)
        @return validation result with all detected issues
        """

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph, theMode: BRepGraph_Validate.Mode) -> BRepGraph_Validate.Result:
        """
        Run structural checks on a built graph with explicit mode.
        @param[in] theGraph graph to validate (const, read-only)
        @param[in] theMode validation mode
        @return validation result with all detected issues
        """

    @overload
    @staticmethod
    def Perform(theGraph: BRepGraph, theOptions: BRepGraph_Validate.Options) -> BRepGraph_Validate.Result:
        """
        Run structural checks on a built graph with explicit options.
        @param[in] theGraph graph to validate (const, read-only)
        @param[in] theOptions validation profile/options
        @return validation result with all detected issues
        """

class NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId:
    """
    @brief High-performance hash map using open addressing with Robin Hood hashing.

    NCollection_FlatDataMap is an alternative to NCollection_DataMap that provides
    better cache locality and reduced memory allocation overhead by storing all
    key-value pairs inline in a contiguous array.

    Key features:
    - Open addressing with linear probing (better cache locality)
    - Robin Hood hashing (reduces probe sequence variance)
    - Power-of-2 sizing for fast modulo operations
    - No per-element allocations

    Typical faster usage patterns:
    - POD or small key/value types
    - Performance-critical code paths
    - Lookup-heavy workloads
    - Full traversal / iteration-heavy workloads
    - Stable-size maps with Reserve() called once before bulk Bind()

    Container-specific implementation notes:
    - UnBind() keeps probe clusters consistent using backward-shift compaction.

    Relative to NCollection_DataMap:
    - Bind()/UnBind() can be faster in many workloads thanks to contiguous storage and
    no per-element node allocation.
    - Iteration is often faster due to contiguous slot scanning and reduced pointer chasing.

    Limitations:
    - Keys and values must be movable
    - Higher memory usage at low load factors
    - Iteration order is not insertion order
    - Probe distance grows with collisions (bounded by table capacity)

    @note This class is NOT thread-safe. External synchronization is required
    for concurrent access from multiple threads.

    @tparam TheKeyType   Type of keys
    @tparam TheItemType  Type of values
    @tparam Hasher       Hash and equality functor (default: NCollection_DefaultHasher)
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theNbBuckets: int) -> None:
        """
        Constructor with initial capacity hint
        @param theNbBuckets initial capacity (will be rounded up to power of 2)
        """

    @overload
    def __init__(self, theHasher: NCollection_DefaultHasher__BRepGraph_ItemId, theNbBuckets: int = 0) -> None:
        """
        Constructor with custom hasher (copy).
        @param theHasher custom hasher instance
        @param theNbBuckets initial capacity hint
        """

    @overload
    def __init__(self, theOther: NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId) -> None:
        """Copy constructor"""

    def Size(self) -> int:
        """Returns number of elements."""

    def Extent(self) -> int:
        """
        Returns number of elements (legacy int-returning API, convention shared with BaseMap).
        """

    def IsEmpty(self) -> bool:
        """Returns true if map is empty"""

    def Capacity(self) -> int:
        """Returns current capacity"""

    def IsBound(self, theKey: BRepGraph_ItemId) -> bool:
        """Check if key exists"""

    def Contained(self, theKey: BRepGraph_ItemId) -> tuple["std::__1::reference_wrapper<BRepGraph_ItemId const>", "std::__1::reference_wrapper<BRepGraph_ItemId>"] | None:
        """
        Contained returns optional pair of const key reference and mutable value reference.
        Returns std::nullopt if the key is not found.
        """

    def Find(self, theKey: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """Find value by key, throws if not found"""

    def ChangeFind(self, theKey: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """Find value by key (mutable), throws if not found"""

    def __call__(self, theKey: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """Operator() for mutable access"""

    def Bind(self, theKey: BRepGraph_ItemId, theItem: BRepGraph_ItemId) -> bool:
        """
        Bind key to value
        @return true if key was newly added, false if existing key was updated
        """

    def TryBind(self, theKey: BRepGraph_ItemId, theItem: BRepGraph_ItemId) -> bool:
        """
        TryBind binds key to value only if key is not yet bound.
        @param theKey key to add
        @param theItem item to bind if key is not yet bound
        @return true if key was newly added, false if key already existed
        """

    def Bound(self, theKey: BRepGraph_ItemId, theItem: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """
        Bound binds key to value and returns reference to the value.
        @param theKey key to add/update
        @param theItem new item; overrides value previously bound to the key
        @return reference to the value in the map
        """

    def TryBound(self, theKey: BRepGraph_ItemId, theItem: BRepGraph_ItemId) -> BRepGraph_ItemId:
        """
        TryBound binds key to value only if key is not yet bound.
        @param theKey key to add
        @param theItem item to bind if key is not yet bound
        @return reference to existing or newly bound value
        """

    def UnBind(self, theKey: BRepGraph_ItemId) -> bool:
        """
        Remove key from map
        @return true if key was found and removed
        """

    def Clear(self, doReleaseMemory: bool = False) -> None:
        """
        Clear all elements
        @param doReleaseMemory if true, free the internal buffer
        """

    def Exchange(self, theOther: NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId) -> None:
        """Exchange content with another map"""

    def GetHasher(self) -> NCollection_DefaultHasher__BRepGraph_ItemId:
        """Returns const reference to the hasher."""

    def reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def Reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def begin(self) -> "NCollection_FlatDataMap<BRepGraph_ItemId, BRepGraph_ItemId, NCollection_DefaultHasher<BRepGraph_ItemId>>::Iterator":
        """Returns iterator to first element"""

    def end(self) -> "NCollection_FlatDataMap<BRepGraph_ItemId, BRepGraph_ItemId, NCollection_DefaultHasher<BRepGraph_ItemId>>::Iterator":
        """Returns iterator past the end"""

    def cbegin(self) -> "NCollection_FlatDataMap<BRepGraph_ItemId, BRepGraph_ItemId, NCollection_DefaultHasher<BRepGraph_ItemId>>::Iterator":
        """Returns iterator to first element"""

    def cend(self) -> "NCollection_FlatDataMap<BRepGraph_ItemId, BRepGraph_ItemId, NCollection_DefaultHasher<BRepGraph_ItemId>>::Iterator":
        """Returns iterator past the end"""

    def Items(self) -> "NCollection_ItemsView::View<NCollection_FlatDataMap<BRepGraph_ItemId, BRepGraph_ItemId, NCollection_DefaultHasher<BRepGraph_ItemId>>, NCollection_ItemsView::KeyValueRef<BRepGraph_ItemId, BRepGraph_ItemId, false>, NCollection_FlatDataMap<BRepGraph_ItemId, BRepGraph_ItemId, NCollection_DefaultHasher<BRepGraph_ItemId>>::ItemsExtractor, false>":
        """
        Returns a view for key-value pair iteration.
        Usage: for (auto [aKey, aValue] : aMap.Items())
        """

class NCollection_DefaultHasher__BRepGraph_ItemId:
    """
    Purpose:     The  DefaultHasher  is a  Hasher  that is used by
    default in NCollection maps.
    To compute the  hash code of the key  is used the
    global function HashCode.
    To compare two keys is used  the  global function
    IsEqual.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_DefaultHasher__BRepGraph_ItemId) -> None: ...

    @overload
    def __call__(self, theKey: BRepGraph_ItemId) -> int: ...

    @overload
    def __call__(self, theK1: BRepGraph_ItemId, theK2: BRepGraph_ItemId) -> bool: ...

class NCollection_ForwardRangeIterator__BRepGraph_CacheIterator:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_CacheIterator) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_CacheIterator) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class BRepGraph_MutGuard__BRepGraphInc_VertexDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.VertexDef, theId: BRepGraph_VertexId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_VertexId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.VertexDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_VertexRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.VertexRef, theId: BRepGraph_VertexRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_VertexRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.VertexRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_EdgeDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.EdgeDef, theId: BRepGraph_EdgeId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_EdgeId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.EdgeDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_CoEdgeDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.CoEdgeDef, theId: BRepGraph_CoEdgeId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_CoEdgeId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.CoEdgeDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_WireDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.WireDef, theId: BRepGraph_WireId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_WireId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.WireDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_WireRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.WireRef, theId: BRepGraph_WireRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_WireRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.WireRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_FaceDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.FaceDef, theId: BRepGraph_FaceId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_FaceId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.FaceDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_FaceRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.FaceRef, theId: BRepGraph_FaceRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_FaceRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.FaceRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_ShellDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.ShellDef, theId: BRepGraph_ShellId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_ShellId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.ShellDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_ShellRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.ShellRef, theId: BRepGraph_ShellRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_ShellRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.ShellRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_SolidDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.SolidDef, theId: BRepGraph_SolidId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_SolidId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.SolidDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_SolidRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.SolidRef, theId: BRepGraph_SolidRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_SolidRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.SolidRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_CompoundDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.CompoundDef, theId: BRepGraph_CompoundId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_CompoundId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.CompoundDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_CompSolidDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.CompSolidDef, theId: BRepGraph_CompSolidId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_CompSolidId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.CompSolidDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_ProductDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.ProductDef, theId: BRepGraph_ProductId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_ProductId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.ProductDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_OccurrenceDef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.OccurrenceDef, theId: BRepGraph_OccurrenceId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_OccurrenceId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.OccurrenceDef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_OccurrenceRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.OccurrenceRef, theId: BRepGraph_OccurrenceRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_OccurrenceRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.OccurrenceRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class BRepGraph_MutGuard__BRepGraphInc_ChildRef:
    """
    @brief RAII scope token batching mutation notifications for a single entity.

    Obtained via BRepGraph::Editor().<Ops>().Mut() / MutRef() / MutSurface() etc.
    Reads via `operator->()` / `operator*()`; writes via Editor's typed setters
    (or `Internal()` for in-tree structural remaps). Any call to `Internal()`
    flags the guard dirty and the destructor fires `markModified` /
    `markRefModified` once on scope exit.

    The guard registers itself as active on the guarded item at construction
    and deregisters on destruction. This prevents double-mutation: attempting
    to acquire a second guard on the same item while the first is still alive
    will throw. Move-only; after a move, the source guard becomes inert and
    does not deregister.

    Compile-time dispatch selects the ID type and notification method:
    - For types derived from BRepGraphInc::BaseDef: BRepGraph_NodeId + markModified()
    - For types derived from BRepGraphInc::BaseRef: BRepGraph_RefId + markRefModified()

    @code
    {
    BRepGraph_MutGuard<BRepGraphInc::EdgeDef> anEdge =
    theGraph.Editor().Edges().Mut(BRepGraph_EdgeId(42));
    theGraph.Editor().Edges().SetTolerance(anEdge, 0.5);
    } // markModified called once here, guard deregistered
    @endcode
    """

    def __init__(self, theGraph: BRepGraph, theStorage: nanoocp.BRepGraphInc.BRepGraphInc_Storage, theEntity: nanoocp.BRepGraphInc.ChildRef, theId: BRepGraph_ChildRefId) -> None:
        """
        Construct a guard over a mutable entity.
        Registers the item via the storage bit-plane. The Mut() factory pre-validates
        that no guard is active, so this assertion should never fire in normal use.
        @param[in] theGraph   owning graph (used for notification)
        @param[in] theStorage storage instance (for bit-plane guard tracking)
        @param[in] theEntity  pointer to the mutable entity
        @param[in] theId      identity for notification and guard registration
        """

    def Id(self) -> BRepGraph_ChildRefId:
        """Identity for notification."""

    def Graph(self) -> BRepGraph:
        """Owning graph handle."""

    def MarkDirty(self) -> None:
        """
        Flag the guarded entity as modified without writing through `Internal()`.
        Use when an external mutation (e.g. in-place geometry transform on a shared
        Geom handle) is not visible to the guard.
        """

    def IsDirty(self) -> bool:
        """True if `Internal()` or `MarkDirty()` flagged the entity modified."""

    def Internal(self) -> nanoocp.BRepGraphInc.ChildRef:
        """
        INTERNAL USE ONLY. Mutable accessor; auto-flags dirty. External code MUST go
        through Editor's typed setters. Use `operator->()` / `operator*()` for reads.
        """

    def __bool__(self) -> bool:
        """
        True when the guard still owns an entity; false after a move or when
        constructed in an inert state.
        """

class NCollection_ForwardRangeIterator__BRepGraph_DefsIterator_DefsVertexOfEdge:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_DefsIterator.DefsVertexOfEdge) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_DefsIterator_DefsVertexOfEdge) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class BRepGraphInc_Instance__BRepGraph_NodeId:
    """
    @brief Unified instance container template.

    Bundles a typed definition id with location and orientation.

    @tparam TypedIdT typed definition id (e.g. BRepGraph_FaceId, BRepGraph_NodeId).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraphInc_Instance__BRepGraph_NodeId) -> None: ...

    def IsValid(self) -> bool:
        """Returns true if the instance references an existing definition id."""

    @property
    def DefId(self) -> BRepGraph_NodeId: ...

    @DefId.setter
    def DefId(self, arg: BRepGraph_NodeId, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @Orientation.setter
    def Orientation(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

class NCollection_ForwardRangeIterator__BRepGraph_ChildExplorer:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_ChildExplorer) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_ChildExplorer) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class NCollection_ForwardRangeIterator__BRepGraph_RootProductIterator:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_RootProductIterator) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_RootProductIterator) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class NCollection_ForwardRangeIterator__BRepGraph_ParentExplorer:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_ParentExplorer) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_ParentExplorer) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId:
    """
    @brief High-performance hash set using open addressing with Robin Hood hashing.

    NCollection_FlatMap is an alternative to NCollection_Map that provides
    better cache locality and reduced memory allocation overhead by storing all
    keys inline in a contiguous array.

    Key features:
    - Open addressing with linear probing (better cache locality)
    - Robin Hood hashing (reduces probe sequence variance)
    - Power-of-2 sizing for fast modulo operations
    - No per-element allocations

    Typical faster usage patterns:
    - POD or small key types
    - Performance-critical code paths
    - Lookup-heavy workloads (Contains()/Seek())
    - Full traversal / iteration-heavy workloads
    - Stable-size maps with Reserve() called once before bulk insert

    Container-specific implementation notes:
    - Remove() keeps probe clusters consistent using backward-shift compaction.

    Relative to NCollection_Map:
    - Add()/Remove() can be faster in many workloads thanks to contiguous storage and
    no per-element node allocation.
    - Iteration is often faster due to contiguous slot scanning and reduced pointer chasing.

    Limitations:
    - Keys must be movable
    - Higher memory usage at low load factors
    - Iteration order is not insertion order
    - Probe distance grows with collisions (bounded by table capacity)

    @note This class is NOT thread-safe. External synchronization is required
    for concurrent access from multiple threads.

    @tparam TheKeyType Type of keys
    @tparam Hasher     Hash and equality functor (default: NCollection_DefaultHasher)
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theNbBuckets: int) -> None:
        """Constructor with initial capacity hint"""

    @overload
    def __init__(self, theHasher: NCollection_DefaultHasher__BRepGraph_NodeId, theNbBuckets: int = 0) -> None:
        """
        Constructor with custom hasher (copy).
        @param theHasher custom hasher instance
        @param theNbBuckets initial capacity hint
        """

    @overload
    def __init__(self, theOther: NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId) -> None:
        """Copy constructor"""

    def Size(self) -> int:
        """Returns number of elements."""

    def IsEmpty(self) -> bool:
        """Returns true if map is empty"""

    def Capacity(self) -> int:
        """Returns current capacity"""

    def Contains(self, theKey: BRepGraph_NodeId) -> bool:
        """Check if key exists"""

    def Contained(self, theKey: BRepGraph_NodeId) -> "std::__1::reference_wrapper<BRepGraph_NodeId const>" | None:
        """
        Contained returns optional const reference to the key in the map.
        Returns std::nullopt if the key is not found.
        """

    def Add(self, theKey: BRepGraph_NodeId) -> bool:
        """
        Add key to set
        @return true if key was newly added, false if already present
        """

    def Added(self, theKey: BRepGraph_NodeId) -> BRepGraph_NodeId:
        """
        Added: add a new key if not yet in the map, and return
        reference to either newly added or previously existing key.
        @param theKey key to add
        @return const reference to the key in the map
        """

    def Remove(self, theKey: BRepGraph_NodeId) -> bool:
        """
        Remove key from set
        @return true if key was found and removed
        """

    def Clear(self, doReleaseMemory: bool = False) -> None:
        """Clear all elements"""

    def Exchange(self, theOther: NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId) -> None:
        """Exchange content with another map"""

    def GetHasher(self) -> NCollection_DefaultHasher__BRepGraph_NodeId:
        """Returns const reference to the hasher."""

    def reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def Reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def begin(self) -> "NCollection_FlatMap<BRepGraph_NodeId, NCollection_DefaultHasher<BRepGraph_NodeId>>::Iterator": ...

    def end(self) -> "NCollection_FlatMap<BRepGraph_NodeId, NCollection_DefaultHasher<BRepGraph_NodeId>>::Iterator": ...

    def cbegin(self) -> "NCollection_FlatMap<BRepGraph_NodeId, NCollection_DefaultHasher<BRepGraph_NodeId>>::Iterator": ...

    def cend(self) -> "NCollection_FlatMap<BRepGraph_NodeId, NCollection_DefaultHasher<BRepGraph_NodeId>>::Iterator": ...

class NCollection_DefaultHasher__BRepGraph_NodeId:
    """
    Purpose:     The  DefaultHasher  is a  Hasher  that is used by
    default in NCollection maps.
    To compute the  hash code of the key  is used the
    global function HashCode.
    To compare two keys is used  the  global function
    IsEqual.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_DefaultHasher__BRepGraph_NodeId) -> None: ...

    @overload
    def __call__(self, theKey: BRepGraph_NodeId) -> int: ...

    @overload
    def __call__(self, theK1: BRepGraph_NodeId, theK2: BRepGraph_NodeId) -> bool: ...

class NCollection_FlatMap__BRepGraph_UID__NCollection_DefaultHasher__BRepGraph_UID:
    """
    @brief High-performance hash set using open addressing with Robin Hood hashing.

    NCollection_FlatMap is an alternative to NCollection_Map that provides
    better cache locality and reduced memory allocation overhead by storing all
    keys inline in a contiguous array.

    Key features:
    - Open addressing with linear probing (better cache locality)
    - Robin Hood hashing (reduces probe sequence variance)
    - Power-of-2 sizing for fast modulo operations
    - No per-element allocations

    Typical faster usage patterns:
    - POD or small key types
    - Performance-critical code paths
    - Lookup-heavy workloads (Contains()/Seek())
    - Full traversal / iteration-heavy workloads
    - Stable-size maps with Reserve() called once before bulk insert

    Container-specific implementation notes:
    - Remove() keeps probe clusters consistent using backward-shift compaction.

    Relative to NCollection_Map:
    - Add()/Remove() can be faster in many workloads thanks to contiguous storage and
    no per-element node allocation.
    - Iteration is often faster due to contiguous slot scanning and reduced pointer chasing.

    Limitations:
    - Keys must be movable
    - Higher memory usage at low load factors
    - Iteration order is not insertion order
    - Probe distance grows with collisions (bounded by table capacity)

    @note This class is NOT thread-safe. External synchronization is required
    for concurrent access from multiple threads.

    @tparam TheKeyType Type of keys
    @tparam Hasher     Hash and equality functor (default: NCollection_DefaultHasher)
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theNbBuckets: int) -> None:
        """Constructor with initial capacity hint"""

    @overload
    def __init__(self, theHasher: NCollection_DefaultHasher__BRepGraph_UID, theNbBuckets: int = 0) -> None:
        """
        Constructor with custom hasher (copy).
        @param theHasher custom hasher instance
        @param theNbBuckets initial capacity hint
        """

    @overload
    def __init__(self, theOther: NCollection_FlatMap__BRepGraph_UID__NCollection_DefaultHasher__BRepGraph_UID) -> None:
        """Copy constructor"""

    def Size(self) -> int:
        """Returns number of elements."""

    def IsEmpty(self) -> bool:
        """Returns true if map is empty"""

    def Capacity(self) -> int:
        """Returns current capacity"""

    def Contains(self, theKey: BRepGraph_UID) -> bool:
        """Check if key exists"""

    def Contained(self, theKey: BRepGraph_UID) -> "std::__1::reference_wrapper<BRepGraph_UID const>" | None:
        """
        Contained returns optional const reference to the key in the map.
        Returns std::nullopt if the key is not found.
        """

    def Add(self, theKey: BRepGraph_UID) -> bool:
        """
        Add key to set
        @return true if key was newly added, false if already present
        """

    def Added(self, theKey: BRepGraph_UID) -> BRepGraph_UID:
        """
        Added: add a new key if not yet in the map, and return
        reference to either newly added or previously existing key.
        @param theKey key to add
        @return const reference to the key in the map
        """

    def Remove(self, theKey: BRepGraph_UID) -> bool:
        """
        Remove key from set
        @return true if key was found and removed
        """

    def Clear(self, doReleaseMemory: bool = False) -> None:
        """Clear all elements"""

    def Exchange(self, theOther: NCollection_FlatMap__BRepGraph_UID__NCollection_DefaultHasher__BRepGraph_UID) -> None:
        """Exchange content with another map"""

    def GetHasher(self) -> NCollection_DefaultHasher__BRepGraph_UID:
        """Returns const reference to the hasher."""

    def reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def Reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def begin(self) -> "NCollection_FlatMap<BRepGraph_UID, NCollection_DefaultHasher<BRepGraph_UID>>::Iterator": ...

    def end(self) -> "NCollection_FlatMap<BRepGraph_UID, NCollection_DefaultHasher<BRepGraph_UID>>::Iterator": ...

    def cbegin(self) -> "NCollection_FlatMap<BRepGraph_UID, NCollection_DefaultHasher<BRepGraph_UID>>::Iterator": ...

    def cend(self) -> "NCollection_FlatMap<BRepGraph_UID, NCollection_DefaultHasher<BRepGraph_UID>>::Iterator": ...

class NCollection_DefaultHasher__BRepGraph_UID:
    """
    Purpose:     The  DefaultHasher  is a  Hasher  that is used by
    default in NCollection maps.
    To compute the  hash code of the key  is used the
    global function HashCode.
    To compare two keys is used  the  global function
    IsEqual.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_DefaultHasher__BRepGraph_UID) -> None: ...

    @overload
    def __call__(self, theKey: BRepGraph_UID) -> int: ...

    @overload
    def __call__(self, theK1: BRepGraph_UID, theK2: BRepGraph_UID) -> bool: ...

class NCollection_FlatMap__BRepGraph_ItemUID__NCollection_DefaultHasher__BRepGraph_ItemUID:
    """
    @brief High-performance hash set using open addressing with Robin Hood hashing.

    NCollection_FlatMap is an alternative to NCollection_Map that provides
    better cache locality and reduced memory allocation overhead by storing all
    keys inline in a contiguous array.

    Key features:
    - Open addressing with linear probing (better cache locality)
    - Robin Hood hashing (reduces probe sequence variance)
    - Power-of-2 sizing for fast modulo operations
    - No per-element allocations

    Typical faster usage patterns:
    - POD or small key types
    - Performance-critical code paths
    - Lookup-heavy workloads (Contains()/Seek())
    - Full traversal / iteration-heavy workloads
    - Stable-size maps with Reserve() called once before bulk insert

    Container-specific implementation notes:
    - Remove() keeps probe clusters consistent using backward-shift compaction.

    Relative to NCollection_Map:
    - Add()/Remove() can be faster in many workloads thanks to contiguous storage and
    no per-element node allocation.
    - Iteration is often faster due to contiguous slot scanning and reduced pointer chasing.

    Limitations:
    - Keys must be movable
    - Higher memory usage at low load factors
    - Iteration order is not insertion order
    - Probe distance grows with collisions (bounded by table capacity)

    @note This class is NOT thread-safe. External synchronization is required
    for concurrent access from multiple threads.

    @tparam TheKeyType Type of keys
    @tparam Hasher     Hash and equality functor (default: NCollection_DefaultHasher)
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theNbBuckets: int) -> None:
        """Constructor with initial capacity hint"""

    @overload
    def __init__(self, theHasher: NCollection_DefaultHasher__BRepGraph_ItemUID, theNbBuckets: int = 0) -> None:
        """
        Constructor with custom hasher (copy).
        @param theHasher custom hasher instance
        @param theNbBuckets initial capacity hint
        """

    @overload
    def __init__(self, theOther: NCollection_FlatMap__BRepGraph_ItemUID__NCollection_DefaultHasher__BRepGraph_ItemUID) -> None:
        """Copy constructor"""

    def Size(self) -> int:
        """Returns number of elements."""

    def IsEmpty(self) -> bool:
        """Returns true if map is empty"""

    def Capacity(self) -> int:
        """Returns current capacity"""

    def Contains(self, theKey: BRepGraph_ItemUID) -> bool:
        """Check if key exists"""

    def Contained(self, theKey: BRepGraph_ItemUID) -> "std::__1::reference_wrapper<BRepGraph_ItemUID const>" | None:
        """
        Contained returns optional const reference to the key in the map.
        Returns std::nullopt if the key is not found.
        """

    def Add(self, theKey: BRepGraph_ItemUID) -> bool:
        """
        Add key to set
        @return true if key was newly added, false if already present
        """

    def Added(self, theKey: BRepGraph_ItemUID) -> BRepGraph_ItemUID:
        """
        Added: add a new key if not yet in the map, and return
        reference to either newly added or previously existing key.
        @param theKey key to add
        @return const reference to the key in the map
        """

    def Remove(self, theKey: BRepGraph_ItemUID) -> bool:
        """
        Remove key from set
        @return true if key was found and removed
        """

    def Clear(self, doReleaseMemory: bool = False) -> None:
        """Clear all elements"""

    def Exchange(self, theOther: NCollection_FlatMap__BRepGraph_ItemUID__NCollection_DefaultHasher__BRepGraph_ItemUID) -> None:
        """Exchange content with another map"""

    def GetHasher(self) -> NCollection_DefaultHasher__BRepGraph_ItemUID:
        """Returns const reference to the hasher."""

    def reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def Reserve(self, theN: int) -> None:
        """Reserve capacity for at least theN elements"""

    def begin(self) -> "NCollection_FlatMap<BRepGraph_ItemUID, NCollection_DefaultHasher<BRepGraph_ItemUID>>::Iterator": ...

    def end(self) -> "NCollection_FlatMap<BRepGraph_ItemUID, NCollection_DefaultHasher<BRepGraph_ItemUID>>::Iterator": ...

    def cbegin(self) -> "NCollection_FlatMap<BRepGraph_ItemUID, NCollection_DefaultHasher<BRepGraph_ItemUID>>::Iterator": ...

    def cend(self) -> "NCollection_FlatMap<BRepGraph_ItemUID, NCollection_DefaultHasher<BRepGraph_ItemUID>>::Iterator": ...

class NCollection_DefaultHasher__BRepGraph_ItemUID:
    """
    Purpose:     The  DefaultHasher  is a  Hasher  that is used by
    default in NCollection maps.
    To compute the  hash code of the key  is used the
    global function HashCode.
    To compare two keys is used  the  global function
    IsEqual.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_DefaultHasher__BRepGraph_ItemUID) -> None: ...

    @overload
    def __call__(self, theKey: BRepGraph_ItemUID) -> int: ...

    @overload
    def __call__(self, theK1: BRepGraph_ItemUID, theK2: BRepGraph_ItemUID) -> bool: ...

class NCollection_ForwardRangeIterator__BRepGraph_LayerIterator:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_LayerIterator) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_LayerIterator) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class NCollection_ForwardRangeIterator__BRepGraph_RefsIterator_RefsVertexOfEdge:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_RefsIterator.RefsVertexOfEdge) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_RefsIterator_RefsVertexOfEdge) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Vertex:
    """
    @brief Unified instance container template.

    Bundles a typed definition id with location and orientation.

    @tparam TypedIdT typed definition id (e.g. BRepGraph_FaceId, BRepGraph_NodeId).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Vertex) -> None: ...

    def IsValid(self) -> bool:
        """Returns true if the instance references an existing definition id."""

    @property
    def DefId(self) -> BRepGraph_VertexId: ...

    @DefId.setter
    def DefId(self, arg: BRepGraph_VertexId, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @Orientation.setter
    def Orientation(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

class BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge:
    """
    @brief Unified instance container template.

    Bundles a typed definition id with location and orientation.

    @tparam TypedIdT typed definition id (e.g. BRepGraph_FaceId, BRepGraph_NodeId).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge) -> None: ...

    def IsValid(self) -> bool:
        """Returns true if the instance references an existing definition id."""

    @property
    def DefId(self) -> BRepGraph_CoEdgeId: ...

    @DefId.setter
    def DefId(self, arg: BRepGraph_CoEdgeId, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @Orientation.setter
    def Orientation(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

class BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face:
    """
    @brief Unified instance container template.

    Bundles a typed definition id with location and orientation.

    @tparam TypedIdT typed definition id (e.g. BRepGraph_FaceId, BRepGraph_NodeId).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face) -> None: ...

    def IsValid(self) -> bool:
        """Returns true if the instance references an existing definition id."""

    @property
    def DefId(self) -> BRepGraph_FaceId: ...

    @DefId.setter
    def DefId(self, arg: BRepGraph_FaceId, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @Orientation.setter
    def Orientation(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

class BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire:
    """
    @brief Unified instance container template.

    Bundles a typed definition id with location and orientation.

    @tparam TypedIdT typed definition id (e.g. BRepGraph_FaceId, BRepGraph_NodeId).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire) -> None: ...

    def IsValid(self) -> bool:
        """Returns true if the instance references an existing definition id."""

    @property
    def DefId(self) -> BRepGraph_WireId: ...

    @DefId.setter
    def DefId(self, arg: BRepGraph_WireId, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @Orientation.setter
    def Orientation(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

class BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell:
    """
    @brief Unified instance container template.

    Bundles a typed definition id with location and orientation.

    @tparam TypedIdT typed definition id (e.g. BRepGraph_FaceId, BRepGraph_NodeId).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraphInc_Instance__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell) -> None: ...

    def IsValid(self) -> bool:
        """Returns true if the instance references an existing definition id."""

    @property
    def DefId(self) -> BRepGraph_ShellId: ...

    @DefId.setter
    def DefId(self, arg: BRepGraph_ShellId, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @Orientation.setter
    def Orientation(self, arg: nanoocp.TopAbs.TopAbs_Orientation, /) -> None: ...

class NCollection_ForwardRangeIterator__BRepGraph_RelatedIterator:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_RelatedIterator) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_RelatedIterator) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

class NCollection_ForwardRangeIterator__BRepGraph_SupplementIterator:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: BRepGraph_SupplementIterator) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__BRepGraph_SupplementIterator) -> None: ...

    def __eq__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

    def __ne__(self, arg: nanoocp.NCollection.NCollection_ForwardRangeSentinel, /) -> bool: ...

BRepGraph_CompoundsOfEdge: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfCoEdge: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfWire: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfFace: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfShell: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfSolid: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfCompSolid: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfCompound: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_CompoundsOfChild: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_OccurrencesOfChild: TypeAlias = BRepGraph_OccurrencesOfProduct

BRepGraph_RefsFacesOfWire: TypeAlias = BRepGraph_FacesOfWire

BRepGraph_RefsShellsOfFace: TypeAlias = BRepGraph_ShellsOfFace

BRepGraph_RefsSolidsOfShell: TypeAlias = BRepGraph_SolidsOfShell

BRepGraph_RefsCompSolidsOfSolid: TypeAlias = BRepGraph_CompSolidsOfSolid

BRepGraph_RefsCompoundsOfChild: TypeAlias = BRepGraph_CompoundsOfVertex

BRepGraph_RefsProductsOfOccurrence: TypeAlias = BRepGraph_ProductsOfOccurrence

# C++ typedef aliases
BRepGraph_DefsVertexOfEdge = nanoocp.BRepGraph.BRepGraph_DefsIterator.DefsVertexOfEdge
BRepGraph_RefsVertexOfEdge = nanoocp.BRepGraph.BRepGraph_RefsIterator.RefsVertexOfEdge
