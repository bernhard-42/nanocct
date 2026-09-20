"""OCCT package BRepGraphInc (toolkit TKBRep)"""

import enum
from typing import overload

import nanoocp.BRepGraph
from nanoocp.BRepGraphInc import (
    BRepGraphInc_Load as BRepGraphInc_Load
)
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class BRepGraphInc_BitFlags:
    """
    @brief Contiguous bit-vector for per-entity boolean flags.

    Stores one bit per entity index in a flat array of 64-bit blocks.
    Provides O(1) Set/Clear/Test operations and cache-friendly sequential
    traversal (512 flags per 64-byte cache line via eight 64-bit blocks).

    Used by BRepGraphInc_Storage to store IsRemoved and IsOwned flags
    outside the entity structs, improving cache locality during traversal
    and reducing struct size by eliminating bool-field padding.

    Public helpers in BRepGraphInc_Storage validate indices before reaching this
    low-level container. Set, Clear, and Test remain unchecked for hot internal
    paths that already proved the index is in range.

    @code
    BRepGraphInc_BitFlags aFlags;
    aFlags.Resize(1000);
    aFlags.Set(42);
    if (aFlags.Test(42)) { ... }
    aFlags.Clear(42);
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty bit-vector."""

    @overload
    def __init__(self, theOther: BRepGraphInc_BitFlags) -> None: ...

    def Resize(self, theCount: int) -> None:
        """
        Resize the bit-vector to hold at least theCount bits.
        Newly added bits are initialized to false.
        """

    def Set(self, theIndex: int) -> None:
        """Set the bit at theIndex to true."""

    def Clear(self, theIndex: int) -> None:
        """Clear the bit at theIndex to false."""

    def Test(self, theIndex: int) -> bool:
        """Return the value of the bit at theIndex."""

    def SetAll(self) -> None:
        """Set all bits to true."""

    def ClearAll(self) -> None:
        """Clear all bits to false."""

    def HasAnyBitSet(self) -> bool:
        """Return true if any bit is set."""

    def NbBlocks(self) -> int:
        """Return the number of blocks allocated."""

    def BitCount(self) -> int:
        """Return the number of valid bits represented by this vector."""

    def IsValidIndex(self, theIndex: int) -> bool:
        """Return true if theIndex is inside the valid bit range."""

class ParityOrientation:
    """
    @brief Persisted core-topology orientation stored as forward/reversed parity only.

    The wrapper keeps storage compact through one bool while remaining implicitly
    convertible to `TopAbs_Orientation` for existing orientation-facing codepaths.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Constructs the parity wrapper from a core forward/reversed orientation.
        """

    @overload
    def __init__(self, theOther: ParityOrientation) -> None: ...

    @property
    def IsReversed(self) -> bool:
        """
        Stored parity bit: `false` for `TopAbs_FORWARD`, `true` for `TopAbs_REVERSED`.
        """

    @IsReversed.setter
    def IsReversed(self, arg: bool, /) -> None: ...

class BRepGraph_RepId:
    """
    Lightweight typed index into a per-kind use-record vector inside BRepGraph.

    The pair (Kind, Index) forms a unique use-record identifier within one graph
    instance. Default-constructed RepId has Index = UINT32_MAX (invalid).

    Use records are session-local representation slots with no public stable UID,
    graph-level lock state, independent mutation generation, or layer callbacks.
    They do have a soft-removed state so an owner can clear and later reuse its slot.
    """

    @overload
    def __init__(self) -> None:
        """Default: invalid RepId."""

    @overload
    def __init__(self, theKind: BRepGraph_RepId.Kind, theIdx: int) -> None: ...

    @overload
    def __init__(self, theOther: BRepGraph_RepId) -> None: ...

    class Kind(enum.Enum):
        """Enumeration of use-record kinds."""

        EdgeCurve3D = 0

        EdgePolygon3D = 1

        CoEdgeCurve2D = 2

        CoEdgePolygon2D = 3

        CoEdgePolygonOnTri = 4

        FaceSurface = 5

        FaceTriangulation = 6

    @staticmethod
    def IsValidKind(theKind: BRepGraph_RepId.Kind) -> bool:
        """True if the kind value is one of the supported use-record kinds."""

    @overload
    def IsValid(self) -> bool:
        """True if this id points to an allocated slot."""

    @overload
    def IsValid(self, theMaxCount: int) -> bool:
        """True if this id is within [0, theMaxCount)."""

    def __eq__(self, theOther: BRepGraph_RepId) -> bool: ...

    def __ne__(self, theOther: BRepGraph_RepId) -> bool: ...

    def __lt__(self, theOther: BRepGraph_RepId) -> bool: ...

    def IsRemoved(self, theGraph: nanoocp.BRepGraph.BRepGraph) -> bool:
        """
        Return true if this use entry has been soft-removed in the given graph.
        """

    @property
    def RepKind(self) -> BRepGraph_RepId.Kind: ...

    @RepKind.setter
    def RepKind(self, arg: BRepGraph_RepId.Kind, /) -> None: ...

    @property
    def Index(self) -> int: ...

    @Index.setter
    def Index(self, arg: int, /) -> None: ...

class std_hash__BRepGraph_RepId:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: std_hash__BRepGraph_RepId) -> None: ...

    def __call__(self, theId: BRepGraph_RepId) -> int: ...

class BaseDef:
    """Fields shared by every entity."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BaseDef) -> None: ...

    @property
    def UID(self) -> int:
        """
        Persistent per-kind UID counter value.
        0 = invalid sentinel (not yet allocated). Valid UIDs start at 1.
        Kind is implicit from the concrete struct type (VertexDef, EdgeDef, etc.).
        """

    @UID.setter
    def UID(self, arg: int, /) -> None: ...

    @property
    def OwnGen(self) -> int:
        """
        Own-data mutation counter, incremented ONLY when the entity's own
        definition fields change (tolerance, point, flags, etc.).
        NOT incremented by descendant changes.
        Used by VersionStamp for persistent identity staleness detection.
        """

    @OwnGen.setter
    def OwnGen(self, arg: int, /) -> None: ...

    @property
    def SubtreeGen(self) -> int:
        """
        Subtree mutation counter, incremented when own data OR any descendant
        data changes. Propagated upward via markParentSubtreeGen().
        Used by TransientCache and shape cache for hierarchical freshness.
        """

    @SubtreeGen.setter
    def SubtreeGen(self, arg: int, /) -> None: ...

    @property
    def LastPropWave(self) -> int:
        """
        Wave counter from the last propagation that visited this node.
        Used as a re-visit guard in markParentSubtreeGen() to prevent
        exponential blowup on diamond topologies. Compared against
        BRepGraphInc_Storage::myPropagationWave.
        """

    @LastPropWave.setter
    def LastPropWave(self, arg: int, /) -> None: ...

class VertexDef(BaseDef):
    """Vertex definition: 3D point + tolerance."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VertexDef) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt:
        """
        3D point in definition frame (raw BRep_TVertex::Pnt, without vertex-in-edge Location).
        """

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt, /) -> None: ...

    @property
    def Tolerance(self) -> float:
        """Tolerance from BRep_TVertex."""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

class EdgeDef(BaseDef):
    """
    Edge entity: parameter range, boundary vertices.
    Geometry (curve, polygon) accessed via owned use records.
    Degeneracy, closure, SameRange, and SameParameter are derived from
    current topology and geometry via BRepGraph_CacheDerivedState.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgeDef) -> None: ...

    @property
    def Curve3DRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)0>":
        """Owned 3D curve use id (invalid for degenerate edges)"""

    @Curve3DRepId.setter
    def Curve3DRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)0>", /) -> None: ...

    @property
    def Tolerance(self) -> float:
        """Tolerance from BRep_TEdge"""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

    @property
    def StartVertexRefId(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>":
        """Start vertex reference"""

    @StartVertexRefId.setter
    def StartVertexRefId(self, arg: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>", /) -> None: ...

    @property
    def EndVertexRefId(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>":
        """End vertex reference"""

    @EndVertexRefId.setter
    def EndVertexRefId(self, arg: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>", /) -> None: ...

    @property
    def Polygon3DRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)1>":
        """Owned 3D polygon use id"""

    @Polygon3DRepId.setter
    def Polygon3DRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)1>", /) -> None: ...

class CoEdgeDef(BaseDef):
    """
    CoEdge entity: use of an edge on a specific face, owns PCurve data.

    Each coedge represents one edge-face binding with its parametric curve.
    Wires reference coedges rather than edges directly.
    Seam edges produce two coedges on the same face with opposite Orientation;
    the seam relation is queryable via BRepGraph_Tool::CoEdge::SeamPair.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CoEdgeDef) -> None: ...

    @property
    def ParentWireId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>":
        """Ordered owner wire"""

    @ParentWireId.setter
    def ParentWireId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", /) -> None: ...

    @property
    def ChildEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>":
        """Connected reusable edge definition"""

    @ChildEdgeId.setter
    def ChildEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", /) -> None: ...

    @property
    def FaceId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>":
        """Face this coedge belongs to (invalid for free wires)"""

    @FaceId.setter
    def FaceId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation relative to parent edge"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

    @property
    def Curve2DRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)2>":
        """Owned 2D curve use id"""

    @Curve2DRepId.setter
    def Curve2DRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)2>", /) -> None: ...

    @property
    def Polygon2DRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)3>":
        """Owned 2D polygon use id"""

    @Polygon2DRepId.setter
    def Polygon2DRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)3>", /) -> None: ...

    @property
    def PolygonOnTriRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)4>":
        """Owned polygon-on-triangulation use id"""

    @PolygonOnTriRepId.setter
    def PolygonOnTriRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)4>", /) -> None: ...

class WireDef(BaseDef):
    """
    Wire entity: ordered coedge sequence.
    Wire closure is derived from the ordered coedge chain via BRepGraph_CacheDerivedState.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireDef) -> None: ...

class FaceDef(BaseDef):
    """Face entity: surface, triangulations, wires."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceDef) -> None: ...

    @property
    def SurfaceRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)5>":
        """Owned surface use id"""

    @SurfaceRepId.setter
    def SurfaceRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)5>", /) -> None: ...

    @property
    def TriangulationRepId(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)6>":
        """Owned triangulation use id (persistent/imported)"""

    @TriangulationRepId.setter
    def TriangulationRepId(self, arg: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)6>", /) -> None: ...

    @property
    def Tolerance(self) -> float:
        """Face tolerance"""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

class ShellDef(BaseDef):
    """
    Shell entity.
    Shell closure is derived from face-boundary edge incidence via BRepGraph_CacheDerivedState.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShellDef) -> None: ...

class SolidDef(BaseDef):
    """Solid entity."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SolidDef) -> None: ...

class CompoundDef(BaseDef):
    """Compound entity."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompoundDef) -> None: ...

class CompSolidDef(BaseDef):
    """Comp-solid entity."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompSolidDef) -> None: ...

class ProductDef(BaseDef):
    """
    Product entity: reusable shape definition (part or assembly).
    Children are managed uniformly via ProductRelations::OccurrenceRefIds:
    - A part product has one occurrence whose ChildNodeId is a topology root node.
    - An assembly product has occurrences whose ChildNodeId values are other products.
    Products carry no location or orientation - those live on references.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ProductDef) -> None: ...

class OccurrenceDef(BaseDef):
    """
    Occurrence entity: reference to a child node (topology root or product).
    Parent products are determined from ProductRelations owner arrays.
    Placement lives on OccurrenceRef::LocalLocation (definitions never carry location).
    Path-based traversal (BRepGraph_UsagePath) resolves DAG paths without stored
    parent-occurrence pointers.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OccurrenceDef) -> None: ...

    @property
    def ChildNodeId(self) -> nanoocp.BRepGraph.BRepGraph_NodeId:
        """Referenced child node (topology root or product)"""

    @ChildNodeId.setter
    def ChildNodeId(self, arg: nanoocp.BRepGraph.BRepGraph_NodeId, /) -> None: ...

class BaseRef:
    """Fields shared by every reference entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BaseRef) -> None: ...

    @property
    def UID(self) -> int:
        """
        Persistent per-kind UID counter value.
        0 = invalid sentinel (not yet allocated). Valid UIDs start at 1.
        Kind is implicit from the concrete struct type (ShellRef, FaceRef, etc.).
        """

    @UID.setter
    def UID(self, arg: int, /) -> None: ...

class ShellRef(BaseRef):
    """Shell reference storage entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShellRef) -> None: ...

    @property
    def ParentSolidId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>":
        """Parent solid identifier"""

    @ParentSolidId.setter
    def ParentSolidId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", /) -> None: ...

    @property
    def ChildShellId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>":
        """Child shell identifier"""

    @ChildShellId.setter
    def ChildShellId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation within parent"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

class FaceRef(BaseRef):
    """Face reference storage entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceRef) -> None: ...

    @property
    def ParentShellId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>":
        """Parent shell identifier"""

    @ParentShellId.setter
    def ParentShellId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", /) -> None: ...

    @property
    def ChildFaceId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>":
        """Child face identifier"""

    @ChildFaceId.setter
    def ChildFaceId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation within parent"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

class WireRef(BaseRef):
    """Wire reference storage entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireRef) -> None: ...

    @property
    def ParentFaceId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>":
        """Parent face identifier"""

    @ParentFaceId.setter
    def ParentFaceId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", /) -> None: ...

    @property
    def ChildWireId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>":
        """Child wire identifier"""

    @ChildWireId.setter
    def ChildWireId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation within parent"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

class VertexRef(BaseRef):
    """Vertex reference storage entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VertexRef) -> None: ...

    @property
    def ChildVertexId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>":
        """Child vertex identifier"""

    @ChildVertexId.setter
    def ChildVertexId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>", /) -> None: ...

    @property
    def ParentEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>":
        """Edge that owns this vertex reference"""

    @ParentEdgeId.setter
    def ParentEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation within parent"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

class SolidRef(BaseRef):
    """Solid reference storage entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SolidRef) -> None: ...

    @property
    def ParentCompSolidId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>":
        """Parent compsolid identifier"""

    @ParentCompSolidId.setter
    def ParentCompSolidId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>", /) -> None: ...

    @property
    def ChildSolidId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>":
        """Child solid identifier"""

    @ChildSolidId.setter
    def ChildSolidId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation within parent"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

class ChildRef(BaseRef):
    """Child reference storage entry."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChildRef) -> None: ...

    @property
    def ParentCompoundId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>":
        """Parent compound identifier"""

    @ParentCompoundId.setter
    def ParentCompoundId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>", /) -> None: ...

    @property
    def ChildNodeId(self) -> nanoocp.BRepGraph.BRepGraph_NodeId:
        """Child node identifier (heterogeneous)"""

    @ChildNodeId.setter
    def ChildNodeId(self, arg: nanoocp.BRepGraph.BRepGraph_NodeId, /) -> None: ...

    @property
    def Orientation(self) -> ParityOrientation:
        """Orientation within parent"""

    @Orientation.setter
    def Orientation(self, arg: ParityOrientation, /) -> None: ...

    @property
    def LocalLocation(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Location relative to parent"""

    @LocalLocation.setter
    def LocalLocation(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

class OccurrenceRef(BaseRef):
    """
    Occurrence reference storage entry.
    Like ChildRef but without Orientation - placement is a reference property.
    Structurally parallel to other ref types: definitions carry no location.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OccurrenceRef) -> None: ...

    @property
    def ParentProductId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>": ...

    @ParentProductId.setter
    def ParentProductId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>", /) -> None: ...

    @property
    def ChildOccurrenceId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>": ...

    @ChildOccurrenceId.setter
    def ChildOccurrenceId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>", /) -> None: ...

    @property
    def LocalLocation(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Placement relative to parent product"""

    @LocalLocation.setter
    def LocalLocation(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

class FaceRelations:
    """@brief Topology relations for face definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceRelations) -> None: ...

    @property
    def WireRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>>":
        """Wire references owned by this face"""

    @WireRefIds.setter
    def WireRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>>", /) -> None: ...

    @property
    def ParentFaceRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>>":
        """Upstream face references (compound hierarchy)"""

    @ParentFaceRefIds.setter
    def ParentFaceRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>>", /) -> None: ...

class WireRelations:
    """@brief Topology relations for wire definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireRelations) -> None: ...

    @property
    def CoEdgeIds(self) -> "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>>":
        """Coedge identifiers in this wire"""

    @CoEdgeIds.setter
    def CoEdgeIds(self, arg: "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>>", /) -> None: ...

    @property
    def ParentWireRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>>":
        """Upstream wire references"""

    @ParentWireRefIds.setter
    def ParentWireRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>>", /) -> None: ...

class EdgeRelations:
    """@brief Topology relations for edge definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgeRelations) -> None: ...

    @property
    def CoEdgeIds(self) -> "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>>":
        """Coedge identifiers using this edge"""

    @CoEdgeIds.setter
    def CoEdgeIds(self, arg: "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>>", /) -> None: ...

class ShellRelations:
    """@brief Topology relations for shell definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShellRelations) -> None: ...

    @property
    def FaceRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>>":
        """Face references in this shell"""

    @FaceRefIds.setter
    def FaceRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>>", /) -> None: ...

    @property
    def ParentShellRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>>":
        """Upstream shell references"""

    @ParentShellRefIds.setter
    def ParentShellRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>>", /) -> None: ...

class SolidRelations:
    """@brief Topology relations for solid definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SolidRelations) -> None: ...

    @property
    def ShellRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>>":
        """Shell references in this solid"""

    @ShellRefIds.setter
    def ShellRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>>", /) -> None: ...

    @property
    def ParentSolidRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>>":
        """Upstream solid references"""

    @ParentSolidRefIds.setter
    def ParentSolidRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>>", /) -> None: ...

class CompoundRelations:
    """@brief Topology relations for compound definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompoundRelations) -> None: ...

    @property
    def ChildRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>>":
        """Child references in this compound"""

    @ChildRefIds.setter
    def ChildRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>>", /) -> None: ...

class CompSolidRelations:
    """@brief Topology relations for compsolid definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompSolidRelations) -> None: ...

    @property
    def SolidRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>>":
        """Solid references in this compsolid"""

    @SolidRefIds.setter
    def SolidRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>>", /) -> None: ...

class VertexRelations:
    """@brief Topology relations for vertex definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VertexRelations) -> None: ...

    @property
    def EdgeIds(self) -> "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>>":
        """Edge identifiers sharing this vertex"""

    @EdgeIds.setter
    def EdgeIds(self, arg: "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>>", /) -> None: ...

class ProductRelations:
    """@brief Topology relations for product definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ProductRelations) -> None: ...

    @property
    def OccurrenceRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>>":
        """Occurrence references under this product"""

    @OccurrenceRefIds.setter
    def OccurrenceRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>>", /) -> None: ...

class OccurrenceRelations:
    """@brief Topology relations for occurrence definitions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OccurrenceRelations) -> None: ...

    @property
    def ParentOccurrenceRefIds(self) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>>":
        """Upstream occurrence references"""

    @ParentOccurrenceRefIds.setter
    def ParentOccurrenceRefIds(self, arg: "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>>", /) -> None: ...

class EdgeCurve3DRep:
    """3D curve use for edges. Owned by a single edge."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgeCurve3DRep) -> None: ...

    @property
    def ParentEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>":
        """Owning edge identifier"""

    @ParentEdgeId.setter
    def ParentEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", /) -> None: ...

    @property
    def Curve(self) -> nanoocp.Geom.Geom_Curve:
        """3D curve geometry"""

    @Curve.setter
    def Curve(self, arg: nanoocp.Geom.Geom_Curve, /) -> None: ...

    @property
    def ParamFirst(self) -> float:
        """First curve parameter"""

    @ParamFirst.setter
    def ParamFirst(self, arg: float, /) -> None: ...

    @property
    def ParamLast(self) -> float:
        """Last curve parameter"""

    @ParamLast.setter
    def ParamLast(self, arg: float, /) -> None: ...

class EdgePolygon3DRep:
    """3D polygon use for edges. Owned by a single edge."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgePolygon3DRep) -> None: ...

    @property
    def ParentEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>":
        """Owning edge identifier"""

    @ParentEdgeId.setter
    def ParentEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", /) -> None: ...

    @property
    def Polygon(self) -> nanoocp.Poly.Poly_Polygon3D:
        """3D polygon geometry"""

    @Polygon.setter
    def Polygon(self, arg: nanoocp.Poly.Poly_Polygon3D, /) -> None: ...

class CoEdgeCurve2DRep:
    """
    2D parametric curve (PCurve) use for coedges. Owned by a single coedge.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CoEdgeCurve2DRep) -> None: ...

    @property
    def ParentCoEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>":
        """Owning coedge identifier"""

    @ParentCoEdgeId.setter
    def ParentCoEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>", /) -> None: ...

    @property
    def Curve(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """2D parametric curve geometry"""

    @Curve.setter
    def Curve(self, arg: nanoocp.Geom2d.Geom2d_Curve, /) -> None: ...

    @property
    def ParamFirst(self) -> float:
        """First curve parameter"""

    @ParamFirst.setter
    def ParamFirst(self, arg: float, /) -> None: ...

    @property
    def ParamLast(self) -> float:
        """Last curve parameter"""

    @ParamLast.setter
    def ParamLast(self, arg: float, /) -> None: ...

class CoEdgePolygon2DRep:
    """2D polygon-on-surface use for coedges. Owned by a single coedge."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CoEdgePolygon2DRep) -> None: ...

    @property
    def ParentCoEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>":
        """Owning coedge identifier"""

    @ParentCoEdgeId.setter
    def ParentCoEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>", /) -> None: ...

    @property
    def Polygon(self) -> nanoocp.Poly.Poly_Polygon2D:
        """2D polygon geometry"""

    @Polygon.setter
    def Polygon(self, arg: nanoocp.Poly.Poly_Polygon2D, /) -> None: ...

class CoEdgePolygonOnTriRep:
    """Polygon-on-triangulation use for coedges. Owned by a single coedge."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CoEdgePolygonOnTriRep) -> None: ...

    @property
    def ParentCoEdgeId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>":
        """Owning coedge identifier"""

    @ParentCoEdgeId.setter
    def ParentCoEdgeId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>", /) -> None: ...

    @property
    def Polygon(self) -> nanoocp.Poly.Poly_PolygonOnTriangulation:
        """Polygon-on-triangulation geometry"""

    @Polygon.setter
    def Polygon(self, arg: nanoocp.Poly.Poly_PolygonOnTriangulation, /) -> None: ...

class FaceSurfaceRep:
    """Surface geometry use for faces. Owned by a single face."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceSurfaceRep) -> None: ...

    @property
    def ParentFaceId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>":
        """Owning face identifier"""

    @ParentFaceId.setter
    def ParentFaceId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", /) -> None: ...

    @property
    def Surface(self) -> nanoocp.Geom.Geom_Surface:
        """Surface geometry"""

    @Surface.setter
    def Surface(self, arg: nanoocp.Geom.Geom_Surface, /) -> None: ...

class FaceTriangulationRep:
    """Triangulation mesh use for faces. Owned by a single face."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceTriangulationRep) -> None: ...

    @property
    def ParentFaceId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>":
        """Owning face identifier"""

    @ParentFaceId.setter
    def ParentFaceId(self, arg: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", /) -> None: ...

    @property
    def Triangulation(self) -> nanoocp.Poly.Poly_Triangulation:
        """Triangulation mesh"""

    @Triangulation.setter
    def Triangulation(self, arg: nanoocp.Poly.Poly_Triangulation, /) -> None: ...

class BRepGraphInc_Populate:
    """
    @brief Backend topology/geometry population for BRepGraph.

    This class is part of the BRepGraphInc backend and is intended for
    backend maintenance, tests, and low-level infrastructure only.
    External code should enter through BRepGraph::ShapesView::Add(), which owns the
    public lifecycle, cache invalidation, and layer coordination.

    The builder stores forward child relations only. Reverse relations are rebuilt
    by BRepGraphInc_Storage after population.
    """

    def __init__(self, theOther: BRepGraphInc_Populate) -> None: ...

    class BuildStatus(enum.Enum):
        """Result of a build operation."""

        Success = 0

        SuccessWithWarnings = 1

        Failed = 2

    class Options:
        """Options controlling population."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraphInc_Populate.Options) -> None: ...

    @staticmethod
    def Perform(theGraph: nanoocp.BRepGraph.BRepGraph, theShape: nanoocp.TopoDS.TopoDS_Shape, theParallel: bool, theOptions: BRepGraphInc_Populate.Options = ...) -> BRepGraphInc_Populate.BuildStatus:
        """
        Build backend incidence storage from a TopoDS_Shape.
        @param[out] theGraph    graph whose storage to populate (cleared first)
        @param[in]  theShape    root shape
        @param[in]  theParallel if true, face-level extraction runs in parallel
        @param[in]  theOptions  optional post-pass controls
        @return build status indicating success, warnings, or failure
        """

    @staticmethod
    def AppendFlattened(theGraph: nanoocp.BRepGraph.BRepGraph, theShape: nanoocp.TopoDS.TopoDS_Shape, theParallel: bool, theAppendedRoots: "NCollection_LinearVector<BRepGraph_NodeId>", theOptions: BRepGraphInc_Populate.Options = ...) -> BRepGraphInc_Populate.BuildStatus:
        """
        Extend existing backend storage with additional shapes (no clear).
        Flattens hierarchy containers away; Solid/Shell/Compound/CompSolid inputs
        contribute appended face roots instead of container entities.
        Recomputes the built-in metadata layers from the populated storage.
        @param[in,out] theGraph         graph whose storage to extend
        @param[in]     theShape         shape to append
        @param[in]     theParallel      if true, face-level extraction runs in parallel
        @param[out]    theAppendedRoots collected root NodeIds for non-container shapes
        @param[in]     theOptions       optional post-pass controls
        @return build status indicating success, warnings, or failure
        """

    @staticmethod
    def Append(theGraph: nanoocp.BRepGraph.BRepGraph, theShape: nanoocp.TopoDS.TopoDS_Shape, theParallel: bool, theOptions: BRepGraphInc_Populate.Options = ...) -> BRepGraphInc_Populate.BuildStatus:
        """
        Extend existing backend storage with additional shapes (no clear).
        Preserves the full shape hierarchy: Solid/Shell/Compound/CompSolid nodes
        are created alongside Face/Edge/Vertex nodes. Shapes already present in
        the storage with the same definition identity (TShape + Location, orientation ignored)
        are deduplicated and not re-added.
        @param[in,out] theGraph    graph whose storage to extend
        @param[in]     theShape    shape to append
        @param[in]     theParallel if true, face-level extraction runs in parallel
        @param[in]     theOptions  optional post-pass controls
        @return build status indicating success, warnings, or failure
        """

class BRepGraphInc_Reconstruct:
    """
    @brief Backend reconstruction helpers over incidence-table storage.

    Converts BRepGraphInc_Storage entity data back into TopoDS shapes.
    This class is part of the BRepGraphInc backend; external callers should
    prefer BRepGraph::Shapes() so reconstruction stays behind the facade.
    Supports single-node and cached multi-face reconstruction with
    shared edge/vertex reuse via the Cache.
    """

    def __init__(self, theOther: BRepGraphInc_Reconstruct) -> None: ...

    class Cache:
        """
        Per-Kind dense vector cache for O(1) shape lookup by entity index.
        Replaces NCollection_DataMap to eliminate hash/equality overhead.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraphInc_Reconstruct.Cache) -> None: ...

        class TempScope:
            @overload
            def __init__(self, theCache: BRepGraphInc_Reconstruct.Cache) -> None: ...

            @overload
            def __init__(self, theOther: BRepGraphInc_Reconstruct.Cache.TempScope) -> None: ...

        def Seek(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> nanoocp.TopoDS.TopoDS_Shape:
            """Seek a cached shape. Returns nullptr if not yet cached."""

        def Bind(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
            """Bind a reconstructed shape to a node. Grows the vector as needed."""

        def IsBound(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> bool:
            """Check if a node is already cached."""

        @property
        def myAllocator(self) -> nanoocp.NCollection.NCollection_IncAllocator: ...

        @myAllocator.setter
        def myAllocator(self, arg: nanoocp.NCollection.NCollection_IncAllocator, /) -> None: ...

        @property
        def myTempAllocator(self) -> nanoocp.NCollection.NCollection_IncAllocator: ...

        @myTempAllocator.setter
        def myTempAllocator(self, arg: nanoocp.NCollection.NCollection_IncAllocator, /) -> None: ...

        @property
        def myTempScopeDepth(self) -> int: ...

        @myTempScopeDepth.setter
        def myTempScopeDepth(self, arg: int, /) -> None: ...

    @overload
    @staticmethod
    def Node(theGraph: nanoocp.BRepGraph.BRepGraph, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Reconstruct a TopoDS_Shape from an entity node.
        Creates a local cache internally; shared vertices/edges are not reused
        across calls.
        @param[in] theGraph  graph owning the storage and caches
        @param[in] theNode   entity node id
        @return reconstructed shape
        """

    @overload
    @staticmethod
    def Node(theGraph: nanoocp.BRepGraph.BRepGraph, theNode: nanoocp.BRepGraph.BRepGraph_NodeId, theCache: BRepGraphInc_Reconstruct.Cache) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Reconstruct a TopoDS_Shape with a shared cache for sub-shape reuse.
        Vertices and edges already in theCache are returned directly.
        @param[in]     theGraph  graph owning the storage and caches
        @param[in]     theNode   entity node id
        @param[in,out] theCache  shared cache for vertex/edge/face shapes
        @return reconstructed shape
        """

    @staticmethod
    def FaceWithCache(theGraph: nanoocp.BRepGraph.BRepGraph, theFaceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theCache: BRepGraphInc_Reconstruct.Cache) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Reconstruct a face with shared edge/vertex cache for multi-face contexts.
        @param[in]     theGraph   graph owning the storage and caches
        @param[in]     theFaceId  face entity id
        @param[in,out] theCache   shared cache for edge and vertex shapes
        @return reconstructed face shape
        """

class BRepGraphInc_Storage:
    """
    @brief Central backend storage container for the incidence-table topology model.

    Holds all entity vectors (Vertex through Occurrence), representation
    vectors (Surface, Curve3D, Curve2D, Triangulation, Polygon), relation
    tables for connectivity navigation, TShape deduplication maps, original
    shape bindings, and per-kind UID vectors. Provides typed accessors
    enforcing compile-time safety for backend code. External callers should
    normally use the BRepGraph facade rather than reaching into this storage
    directly. BRepGraphInc_Populate has friend access for efficient bulk writes
    during graph population.
    """

    def __init__(self) -> None:
        """Construct an empty storage with no entities or representations."""

    class WireCoEdgeOrderStatus(enum.Enum):
        """Result of wire coedge order canonicalization."""

        Connected = 0

        Reordered = 1

        ToleranceOrdered = 2

        Partial = 3

        InvalidInput = 4

    class CachedShape:
        """Gen-validated shape cache entry."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BRepGraphInc_Storage.CachedShape) -> None: ...

        @property
        def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
            """Reconstructed shape cached for a node id."""

        @Shape.setter
        def Shape(self, arg: nanoocp.TopoDS.TopoDS_Shape, /) -> None: ...

        @property
        def StoredSubtreeGen(self) -> int:
            """Subtree generation captured when the cached shape was built."""

        @StoredSubtreeGen.setter
        def StoredSubtreeGen(self, arg: int, /) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator:
        """Return the allocator used for backend storage."""

    def RootProductIds(self) -> "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>>":
        """Return products not referenced by any active occurrence."""

    def ChangeRootProductIds(self) -> "NCollection_LinearVector<BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>>":
        """Return products not referenced by any active occurrence."""

    def DeferredModified(self) -> "NCollection_LinearVector<BRepGraph_NodeId>":
        """Return nodes accumulated during deferred invalidation."""

    def ChangeDeferredModified(self) -> "NCollection_LinearVector<BRepGraph_NodeId>":
        """Return nodes accumulated during deferred invalidation."""

    def DeferredRefModified(self) -> "NCollection_LinearVector<BRepGraph_RefId>":
        """Return refs accumulated during deferred invalidation."""

    def ChangeDeferredRefModified(self) -> "NCollection_LinearVector<BRepGraph_RefId>":
        """Return refs accumulated during deferred invalidation."""

    def IsEmpty(self) -> bool:
        """
        Return true when the graph contains no topology definitions.
        Checks whether any node kind (Vertex, Edge, Wire, Face, Shell, Solid,
        Compound, CompSolid, Product, Occurrence) has been allocated.
        """

    def NextNodeUIDCounter(self, theKind: nanoocp.BRepGraph.BRepGraph_NodeId.Kind) -> int:
        """Return the next UID counter for a given node kind."""

    def SetNextNodeUIDCounter(self, theKind: nanoocp.BRepGraph.BRepGraph_NodeId.Kind, theCounter: int) -> None:
        """Override the next UID counter for a given node kind."""

    def NextRefUIDCounter(self, theKind: nanoocp.BRepGraph.BRepGraph_RefId.Kind) -> int:
        """Return the next UID counter for a given reference kind."""

    def SetNextRefUIDCounter(self, theKind: nanoocp.BRepGraph.BRepGraph_RefId.Kind, theCounter: int) -> None:
        """Override the next UID counter for a given reference kind."""

    def AllocateNodeUID(self, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> nanoocp.BRepGraph.BRepGraph_UID:
        """
        Allocate a node UID: write counter into the entity, bind reverse map, advance counter.
        """

    def AllocateRefUID(self, theRefId: nanoocp.BRepGraph.BRepGraph_RefId) -> nanoocp.BRepGraph.BRepGraph_RefUID:
        """
        Allocate a reference UID: write counter into the ref, bind reverse map, advance counter.
        """

    def Generation(self) -> int:
        """
        Return the current graph generation used by VersionStamp staleness checks.
        """

    def SetGeneration(self, theGeneration: int) -> None:
        """Override the current graph generation."""

    def IncrementGeneration(self) -> None:
        """Increment the graph generation after a structural mutation batch."""

    def GraphGUID(self) -> nanoocp.Standard.Standard_GUID:
        """Return the stable graph instance GUID."""

    def SetGraphGUID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Override the stable graph instance GUID."""

    def DeferredMode(self) -> bool:
        """Return whether invalidation is currently deferred."""

    def SetDeferredMode(self, theEnabled: bool) -> None:
        """Enable or disable deferred invalidation mode."""

    def PropagationWave(self) -> int:
        """
        Return the current propagation wave id used to avoid revisiting parents.
        """

    def AdvancePropagationWave(self) -> int:
        """Increment the propagation wave and return the new value."""

    def IncrementPropagationWave(self) -> None:
        """Increment the propagation wave without reading it back."""

    def RemoveSubgraphDepth(self) -> int:
        """Return the recursion depth of the active RemoveSubgraph cascade."""

    def IncrementRemoveSubgraphDepth(self) -> None:
        """Enter one nested RemoveSubgraph scope."""

    def DecrementRemoveSubgraphDepth(self) -> None:
        """Leave one nested RemoveSubgraph scope."""

    def NbVertices(self) -> int:
        """Returns the total number of vertex entities (including removed)."""

    def NbEdges(self) -> int:
        """Returns the total number of edge entities (including removed)."""

    def NbCoEdges(self) -> int:
        """Returns the total number of coedge entities (including removed)."""

    def NbWires(self) -> int:
        """Returns the total number of wire entities (including removed)."""

    def NbFaces(self) -> int:
        """Returns the total number of face entities (including removed)."""

    def NbShells(self) -> int:
        """Returns the total number of shell entities (including removed)."""

    def NbSolids(self) -> int:
        """Returns the total number of solid entities (including removed)."""

    def NbCompounds(self) -> int:
        """Returns the total number of compound entities (including removed)."""

    def NbCompSolids(self) -> int:
        """Returns the total number of compsolid entities (including removed)."""

    def NbProducts(self) -> int:
        """Returns the total number of product entities (including removed)."""

    def NbOccurrences(self) -> int:
        """Returns the total number of occurrence entities (including removed)."""

    def NbShellRefs(self) -> int:
        """
        Returns the total number of shell reference entries (including removed).
        """

    def NbFaceRefs(self) -> int:
        """
        Returns the total number of face reference entries (including removed).
        """

    def NbWireRefs(self) -> int:
        """
        Returns the total number of wire reference entries (including removed).
        """

    def NbVertexRefs(self) -> int:
        """
        Returns the total number of vertex reference entries (including removed).
        """

    def NbSolidRefs(self) -> int:
        """
        Returns the total number of solid reference entries (including removed).
        """

    def NbChildRefs(self) -> int:
        """
        Returns the total number of child reference entries (including removed).
        """

    def NbOccurrenceRefs(self) -> int:
        """
        Returns the total number of occurrence reference entries (including removed).
        """

    def NbActiveVertices(self) -> int:
        """Returns the number of active vertex entities (excluding removed)."""

    def NbActiveEdges(self) -> int:
        """Returns the number of active edge entities (excluding removed)."""

    def NbActiveCoEdges(self) -> int:
        """Returns the number of active coedge entities (excluding removed)."""

    def NbActiveWires(self) -> int:
        """Returns the number of active wire entities (excluding removed)."""

    def NbActiveFaces(self) -> int:
        """Returns the number of active face entities (excluding removed)."""

    def NbActiveShells(self) -> int:
        """Returns the number of active shell entities (excluding removed)."""

    def NbActiveSolids(self) -> int:
        """Returns the number of active solid entities (excluding removed)."""

    def NbActiveCompounds(self) -> int:
        """Returns the number of active compound entities (excluding removed)."""

    def NbActiveCompSolids(self) -> int:
        """Returns the number of active compsolid entities (excluding removed)."""

    def NbActiveProducts(self) -> int:
        """Returns the number of active product entities (excluding removed)."""

    def NbActiveOccurrences(self) -> int:
        """Returns the number of active occurrence entities (excluding removed)."""

    def NbActiveShellRefs(self) -> int:
        """
        Returns the number of active shell reference entries (excluding removed).
        """

    def NbActiveFaceRefs(self) -> int:
        """
        Returns the number of active face reference entries (excluding removed).
        """

    def NbActiveWireRefs(self) -> int:
        """
        Returns the number of active wire reference entries (excluding removed).
        """

    def NbActiveVertexRefs(self) -> int:
        """
        Returns the number of active vertex reference entries (excluding removed).
        """

    def NbActiveSolidRefs(self) -> int:
        """
        Returns the number of active solid reference entries (excluding removed).
        """

    def NbActiveChildRefs(self) -> int:
        """
        Returns the number of active child reference entries (excluding removed).
        """

    def NbActiveOccurrenceRefs(self) -> int:
        """
        Returns the number of active occurrence reference entries (excluding removed).
        """

    @overload
    def MarkRemoved(self, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> bool:
        """
        Mark an entity node as removed and decrement its active counter once.
        @param[in] theNodeId typed entity id
        @return true if the node transitioned from active to removed
        """

    @overload
    def MarkRemoved(self, theRepId: BRepGraph_RepId) -> bool:
        """
        Mark a representation-use record as removed and decrement its active counter once.
        @param[in] theRepId typed use id
        @return true if the use transitioned from active to removed
        """

    def MarkRemovedRef(self, theRefId: nanoocp.BRepGraph.BRepGraph_RefId) -> bool:
        """
        Mark a reference entry as removed and decrement its active counter once.
        @param[in] theRefId typed reference id
        @return true if the ref transitioned from active to removed
        """

    def NbEdgeCurves3D(self) -> int:
        """Returns the number of edge 3D curve use records."""

    def NbEdgePolygons3D(self) -> int:
        """Returns the number of edge 3D polygon use records."""

    def NbCoEdgeCurves2D(self) -> int:
        """Returns the number of coedge 2D curve use records."""

    def NbCoEdgePolygons2D(self) -> int:
        """Returns the number of coedge 2D polygon use records."""

    def NbCoEdgePolygonsOnTri(self) -> int:
        """Returns the number of coedge polygon-on-triangulation use records."""

    def NbFaceSurfaces(self) -> int:
        """Returns the number of face surface use records."""

    def NbFaceTriangulations(self) -> int:
        """Returns the number of face triangulation use records."""

    def NbActiveEdgeCurves3D(self) -> int:
        """Returns the number of active (parent-valid) edge 3D curve use records."""

    def NbActiveCoEdgeCurves2D(self) -> int:
        """
        Returns the number of active (parent-valid) coedge 2D curve use records.
        """

    def NbActiveFaceSurfaces(self) -> int:
        """Returns the number of active (parent-valid) face surface use records."""

    def NbActiveFaceTriangulations(self) -> int:
        """
        Returns the number of active (parent-valid) face triangulation use records.
        """

    def NbActiveEdgePolygons3D(self) -> int:
        """
        Returns the number of active (parent-valid) edge 3D polygon use records.
        """

    def NbActiveCoEdgePolygons2D(self) -> int:
        """
        Returns the number of active (parent-valid) coedge 2D polygon use records.
        """

    def NbActiveCoEdgePolygonsOnTri(self) -> int:
        """
        Returns the number of active (parent-valid) coedge polygon-on-triangulation use records.
        """

    def EdgeCurve3DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)0>") -> EdgeCurve3DRep:
        """Returns the edge 3D curve use at the given id."""

    def ChangeEdgeCurve3DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)0>") -> EdgeCurve3DRep:
        """Returns a mutable reference to the edge 3D curve use at the given id."""

    def EdgePolygon3DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)1>") -> EdgePolygon3DRep:
        """Returns the edge 3D polygon use at the given id."""

    def ChangeEdgePolygon3DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)1>") -> EdgePolygon3DRep:
        """
        Returns a mutable reference to the edge 3D polygon use at the given id.
        """

    def CoEdgeCurve2DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)2>") -> CoEdgeCurve2DRep:
        """Returns the coedge 2D curve use at the given id."""

    def ChangeCoEdgeCurve2DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)2>") -> CoEdgeCurve2DRep:
        """
        Returns a mutable reference to the coedge 2D curve use at the given id.
        """

    def CoEdgePolygon2DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)3>") -> CoEdgePolygon2DRep:
        """Returns the coedge 2D polygon use at the given id."""

    def ChangeCoEdgePolygon2DRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)3>") -> CoEdgePolygon2DRep:
        """
        Returns a mutable reference to the coedge 2D polygon use at the given id.
        """

    def CoEdgePolygonOnTriRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)4>") -> CoEdgePolygonOnTriRep:
        """Returns the coedge polygon-on-triangulation use at the given id."""

    def ChangeCoEdgePolygonOnTriRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)4>") -> CoEdgePolygonOnTriRep:
        """
        Returns a mutable reference to the coedge polygon-on-triangulation use at the given id.
        """

    def FaceSurfaceRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)5>") -> FaceSurfaceRep:
        """Returns the face surface use at the given id."""

    def ChangeFaceSurfaceRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)5>") -> FaceSurfaceRep:
        """Returns a mutable reference to the face surface use at the given id."""

    def FaceTriangulationRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)6>") -> FaceTriangulationRep:
        """Returns the face triangulation use at the given id."""

    def ChangeFaceTriangulationRep(self, theId: "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)6>") -> FaceTriangulationRep:
        """
        Returns a mutable reference to the face triangulation use at the given id.
        """

    def AppendEdgeCurve3DRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)0>":
        """Appends a new edge 3D curve use record and returns its id."""

    def AppendEdgePolygon3DRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)1>":
        """Appends a new edge 3D polygon use record and returns its id."""

    def AppendCoEdgeCurve2DRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)2>":
        """Appends a new coedge 2D curve use record and returns its id."""

    def AppendCoEdgePolygon2DRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)3>":
        """Appends a new coedge 2D polygon use record and returns its id."""

    def AppendCoEdgePolygonOnTriRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)4>":
        """
        Appends a new coedge polygon-on-triangulation use record and returns its id.
        """

    def AppendFaceSurfaceRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)5>":
        """Appends a new face surface use record and returns its id."""

    def AppendFaceTriangulationRep(self) -> "BRepGraph_RepId::Typed<(BRepGraph_RepId::Kind)6>":
        """Appends a new face triangulation use record and returns its id."""

    def SetRemoved(self, theRepId: BRepGraph_RepId, theVal: bool) -> None:
        """
        Set or clear the soft-removal flag for a representation-use record.
        @param[in] theRepId typed use id
        @param[in] theVal true to mark removed, false to mark active
        """

    def Vertex(self, theVertex: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>") -> VertexDef:
        """
        Returns the vertex entity at the given typed id.
        @param[in] theVertex typed vertex id
        """

    def Edge(self, theEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>") -> EdgeDef:
        """
        Returns the edge entity at the given typed id.
        @param[in] theEdge typed edge id
        """

    def CoEdge(self, theCoEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>") -> CoEdgeDef:
        """
        Returns the coedge entity at the given typed id.
        @param[in] theCoEdge typed coedge id
        """

    def Wire(self, theWire: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> WireDef:
        """
        Returns the wire entity at the given typed id.
        @param[in] theWire typed wire id
        """

    def Face(self, theFace: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>") -> FaceDef:
        """
        Returns the face entity at the given typed id.
        @param[in] theFace typed face id
        """

    def Shell(self, theShell: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>") -> ShellDef:
        """
        Returns the shell entity at the given typed id.
        @param[in] theShell typed shell id
        """

    def Solid(self, theSolid: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>") -> SolidDef:
        """
        Returns the solid entity at the given typed id.
        @param[in] theSolid typed solid id
        """

    def Compound(self, theCompound: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>") -> CompoundDef:
        """
        Returns the compound entity at the given typed id.
        @param[in] theCompound typed compound id
        """

    def CompSolid(self, theCompSolid: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>") -> CompSolidDef:
        """
        Returns the compsolid entity at the given typed id.
        @param[in] theCompSolid typed comp-solid id
        """

    def Product(self, theProduct: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>") -> ProductDef:
        """
        Returns the product entity at the given typed id.
        @param[in] theProduct typed product id
        """

    def Occurrence(self, theOccurrence: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>") -> OccurrenceDef:
        """
        Returns the occurrence entity at the given typed id.
        @param[in] theOccurrence typed occurrence id
        """

    def ShellRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>") -> ShellRef:
        """Returns the shell reference entry at the given typed id."""

    def FaceRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>") -> FaceRef:
        """Returns the face reference entry at the given typed id."""

    def WireRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>") -> WireRef:
        """Returns the wire reference entry at the given typed id."""

    def VertexRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>") -> VertexRef:
        """Returns the vertex reference entry at the given typed id."""

    def SolidRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>") -> SolidRef:
        """Returns the solid reference entry at the given typed id."""

    def ChildRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>") -> ChildRef:
        """Returns the child reference entry at the given typed id."""

    def OccurrenceRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>") -> OccurrenceRef:
        """Returns the occurrence reference entry at the given typed id."""

    def ChangeVertex(self, theVertex: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>") -> VertexDef:
        """
        Returns a mutable reference to the vertex entity at the given typed id.
        @param[in] theVertex typed vertex id
        """

    def ChangeEdge(self, theEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>") -> EdgeDef:
        """
        Returns a mutable reference to the edge entity at the given typed id.
        @param[in] theEdge typed edge id
        """

    def ChangeCoEdge(self, theCoEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>") -> CoEdgeDef:
        """
        Returns a mutable reference to the coedge entity at the given typed id.
        @param[in] theCoEdge typed coedge id
        """

    def ChangeWire(self, theWire: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> WireDef:
        """
        Returns a mutable reference to the wire entity at the given typed id.
        @param[in] theWire typed wire id
        """

    def ChangeFace(self, theFace: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>") -> FaceDef:
        """
        Returns a mutable reference to the face entity at the given typed id.
        @param[in] theFace typed face id
        """

    def ChangeShell(self, theShell: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>") -> ShellDef:
        """
        Returns a mutable reference to the shell entity at the given typed id.
        @param[in] theShell typed shell id
        """

    def ChangeSolid(self, theSolid: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>") -> SolidDef:
        """
        Returns a mutable reference to the solid entity at the given typed id.
        @param[in] theSolid typed solid id
        """

    def ChangeCompound(self, theCompound: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>") -> CompoundDef:
        """
        Returns a mutable reference to the compound entity at the given typed id.
        @param[in] theCompound typed compound id
        """

    def ChangeCompSolid(self, theCompSolid: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>") -> CompSolidDef:
        """
        Returns a mutable reference to the compsolid entity at the given typed id.
        @param[in] theCompSolid typed comp-solid id
        """

    def ChangeProduct(self, theProduct: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>") -> ProductDef:
        """
        Returns a mutable reference to the product entity at the given typed id.
        @param[in] theProduct typed product id
        """

    def ChangeOccurrence(self, theOccurrence: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>") -> OccurrenceDef:
        """
        Returns a mutable reference to the occurrence entity at the given typed id.
        @param[in] theOccurrence typed occurrence id
        """

    def ChangeShellRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>") -> ShellRef:
        """
        Returns a mutable reference to the shell reference entry at the given typed id.
        """

    def ChangeFaceRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>") -> FaceRef:
        """
        Returns a mutable reference to the face reference entry at the given typed id.
        """

    def ChangeWireRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>") -> WireRef:
        """
        Returns a mutable reference to the wire reference entry at the given typed id.
        """

    def ChangeVertexRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>") -> VertexRef:
        """
        Returns a mutable reference to the vertex reference entry at the given typed id.
        """

    def ChangeSolidRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>") -> SolidRef:
        """
        Returns a mutable reference to the solid reference entry at the given typed id.
        """

    def ChangeChildRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>") -> ChildRef:
        """
        Returns a mutable reference to the child reference entry at the given typed id.
        """

    def ChangeOccurrenceRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>") -> OccurrenceRef:
        """
        Returns a mutable reference to the occurrence reference entry at the given typed id.
        """

    def FaceRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>") -> FaceRelations:
        """
        Return the face relations for a given face identifier.
        @param[in] theId face identifier
        @return const reference to the face relation representation
        """

    def WireRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> WireRelations:
        """
        Return the wire relations for a given wire identifier.
        @param[in] theId wire identifier
        @return const reference to the wire relation representation
        """

    def EdgeRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>") -> EdgeRelations:
        """
        Return the edge relations for a given edge identifier.
        @param[in] theId edge identifier
        @return const reference to the edge relation representation
        """

    def ShellRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>") -> ShellRelations:
        """
        Return the shell relations for a given shell identifier.
        @param[in] theId shell identifier
        @return const reference to the shell relation representation
        """

    def SolidRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>") -> SolidRelations:
        """
        Return the solid relations for a given solid identifier.
        @param[in] theId solid identifier
        @return const reference to the solid relation representation
        """

    def CompoundRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>") -> CompoundRelations:
        """
        Return the compound relations for a given compound identifier.
        @param[in] theId compound identifier
        @return const reference to the compound relation representation
        """

    def CompSolidRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>") -> CompSolidRelations:
        """
        Return the compsolid relations for a given compsolid identifier.
        @param[in] theId compsolid identifier
        @return const reference to the compsolid relation representation
        """

    def VertexRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>") -> VertexRelations:
        """
        Return the vertex relations for a given vertex identifier.
        @param[in] theId vertex identifier
        @return const reference to the vertex relation representation
        """

    def ProductRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>") -> ProductRelations:
        """
        Return the product relations for a given product identifier.
        @param[in] theId product identifier
        @return const reference to the product relation representation
        """

    def OccurrenceRelations(self, theId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>") -> OccurrenceRelations:
        """
        Return the occurrence relations for a given occurrence identifier.
        @param[in] theId occurrence identifier
        @return const reference to the occurrence relation representation
        """

    def CompoundRefsOfNode(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>>":
        """
        Return the compound child reference identifiers that point to a given node.
        @param[in] theNode node identifier
        @return const reference to the list of child reference identifiers
        """

    def OccurrenceRefsOfNode(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> "NCollection_LinearVector<BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>>":
        """
        Return the occurrence reference identifiers that point to a given node.
        @param[in] theNode node identifier
        @return const reference to the list of occurrence reference identifiers
        """

    def AppendVertex(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>":
        """Appends a new vertex entity and returns its typed id."""

    def AppendEdge(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>":
        """Appends a new edge entity and returns its typed id."""

    def AppendCoEdge(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>":
        """Appends a new coedge entity and returns its typed id."""

    def AppendWire(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>":
        """Appends a new wire entity and returns its typed id."""

    def AppendFace(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>":
        """Appends a new face entity and returns its typed id."""

    def AppendShell(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>":
        """Appends a new shell entity and returns its typed id."""

    def AppendSolid(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>":
        """Appends a new solid entity and returns its typed id."""

    def AppendCompound(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>":
        """Appends a new compound entity and returns its typed id."""

    def AppendCompSolid(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>":
        """Appends a new compsolid entity and returns its typed id."""

    def AppendProduct(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>":
        """Appends a new product entity and returns its typed id."""

    def AppendOccurrence(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>":
        """Appends a new occurrence entity and returns its typed id."""

    def AppendShellRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>":
        """Appends a new shell reference entry and returns its typed id."""

    def AppendFaceRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>":
        """Appends a new face reference entry and returns its typed id."""

    def AppendWireRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>":
        """Appends a new wire reference entry and returns its typed id."""

    def AppendVertexRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>":
        """Appends a new vertex reference entry and returns its typed id."""

    def AppendSolidRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>":
        """Appends a new solid reference entry and returns its typed id."""

    def AppendChildRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>":
        """Appends a new child reference entry and returns its typed id."""

    def AppendOccurrenceRef(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>":
        """Appends a new occurrence reference entry and returns its typed id."""

    def CreateCoEdgeUse(self, theParentWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theChildEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", theFaceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theOrientation: ParityOrientation) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>":
        """
        Create a coedge use record binding an edge to a wire within a face context.
        @param[in] theParentWireId owning wire identifier
        @param[in] theChildEdgeId  referenced edge identifier
        @param[in] theFaceId       face context identifier
        @param[in] theOrientation  orientation of the coedge
        @return the newly created coedge identifier
        """

    def AttachEdgeToVertex(self, theEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", theVertexId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>") -> None:
        """
        Attach an edge to a vertex by creating a vertex reference.
        @param[in] theEdgeId   edge identifier
        @param[in] theVertexId vertex identifier
        """

    def AttachWireToFace(self, theParentFaceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theChildWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theOrientation: ParityOrientation = ...) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>":
        """
        Attach a wire to a face by creating a wire reference.
        @param[in] theParentFaceId parent face identifier
        @param[in] theChildWireId  child wire identifier
        @param[in] theOrientation  orientation within parent
        @return the newly created wire reference identifier
        """

    def AttachFaceToShell(self, theParentShellId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", theChildFaceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theOrientation: ParityOrientation = ...) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>":
        """
        Attach a face to a shell by creating a face reference.
        @param[in] theParentShellId parent shell identifier
        @param[in] theChildFaceId   child face identifier
        @param[in] theOrientation   orientation within parent
        @return the newly created face reference identifier
        """

    def AttachShellToSolid(self, theParentSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", theChildShellId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", theOrientation: ParityOrientation = ...) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>":
        """
        Attach a shell to a solid by creating a shell reference.
        @param[in] theParentSolidId parent solid identifier
        @param[in] theChildShellId  child shell identifier
        @param[in] theOrientation   orientation within parent
        @return the newly created shell reference identifier
        """

    def AttachSolidToCompSolid(self, theParentCompSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>", theChildSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", theOrientation: ParityOrientation = ...) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>":
        """
        Attach a solid to a compsolid by creating a solid reference.
        @param[in] theParentCompSolidId parent compsolid identifier
        @param[in] theChildSolidId      child solid identifier
        @param[in] theOrientation       orientation within parent
        @return the newly created solid reference identifier
        """

    def AttachChildToCompound(self, theParentCompoundId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>", theChildNodeId: nanoocp.BRepGraph.BRepGraph_NodeId, theLocation: nanoocp.TopLoc.TopLoc_Location = ..., theOrientation: ParityOrientation = ...) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>":
        """
        Attach a child node to a compound by creating a child reference.
        @param[in] theParentCompoundId parent compound identifier
        @param[in] theChildNodeId      child node identifier
        @param[in] theLocation         optional location transformation
        @param[in] theOrientation      orientation within parent
        @return the newly created child reference identifier
        """

    def AttachOccurrenceToProduct(self, theParentProductId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>", theChildOccurrenceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>", theLocation: nanoocp.TopLoc.TopLoc_Location = ...) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>":
        """
        Attach an occurrence to a product by creating an occurrence reference.
        @param[in] theParentProductId     parent product identifier
        @param[in] theChildOccurrenceId   child occurrence identifier
        @param[in] theLocation            optional location transformation
        @return the newly created occurrence reference identifier
        """

    def DetachCoEdgeUse(self, theParentWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theCoEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>") -> bool:
        """
        Detach a coedge use from its parent wire.
        @param[in] theParentWireId owning wire identifier
        @param[in] theCoEdgeId     coedge identifier to detach
        @return true if the coedge was found and removed
        """

    def ReplaceCoEdgeUseWithPair(self, theParentWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theOldCoEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>", theNewFirstCoEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>", theNewSecondCoEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>") -> bool:
        """
        Replace a single coedge with a pair of new coedges in a wire.
        @param[in] theParentWireId    owning wire identifier
        @param[in] theOldCoEdgeId     coedge to replace
        @param[in] theNewFirstCoEdgeId  first replacement coedge
        @param[in] theNewSecondCoEdgeId second replacement coedge
        @return true if the replacement succeeded
        """

    def DetachWireFromFace(self, theParentFaceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>") -> bool:
        """
        Detach a wire reference from its parent face.
        @param[in] theParentFaceId parent face identifier
        @param[in] theRefId        wire reference identifier to detach
        @return true if the reference was found and removed
        """

    def DetachFaceFromShell(self, theParentShellId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>") -> bool:
        """
        Detach a face reference from its parent shell.
        @param[in] theParentShellId parent shell identifier
        @param[in] theRefId         face reference identifier to detach
        @return true if the reference was found and removed
        """

    def DetachShellFromSolid(self, theParentSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>") -> bool:
        """
        Detach a shell reference from its parent solid.
        @param[in] theParentSolidId parent solid identifier
        @param[in] theRefId         shell reference identifier to detach
        @return true if the reference was found and removed
        """

    def DetachSolidFromCompSolid(self, theParentCompSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>", theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>") -> bool:
        """
        Detach a solid reference from its parent compsolid.
        @param[in] theParentCompSolidId parent compsolid identifier
        @param[in] theRefId             solid reference identifier to detach
        @return true if the reference was found and removed
        """

    def DetachChildFromCompound(self, theParentCompoundId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>", theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>") -> bool:
        """
        Detach a child reference from its parent compound.
        @param[in] theParentCompoundId parent compound identifier
        @param[in] theRefId            child reference identifier to detach
        @return true if the reference was found and removed
        """

    def DetachOccurrenceFromProduct(self, theParentProductId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>", theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>") -> bool:
        """
        Detach an occurrence reference from its parent product.
        @param[in] theParentProductId parent product identifier
        @param[in] theRefId           occurrence reference identifier to detach
        @return true if the reference was found and removed
        """

    def RebindOccurrenceChild(self, theOccurrence: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>", theOldChild: nanoocp.BRepGraph.BRepGraph_NodeId, theNewChild: nanoocp.BRepGraph.BRepGraph_NodeId) -> None:
        """
        Rebind the child node of an occurrence to a new node.
        @param[in] theOccurrence occurrence identifier
        @param[in] theOldChild   old child node identifier
        @param[in] theNewChild   new child node identifier
        """

    def RebindVertexEdge(self, theOldVertex: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>", theNewVertex: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>", theEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", theExcludingRef: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>") -> None:
        """
        Rebind vertex edge references from one vertex to another, excluding a specific ref.
        @param[in] theOldVertex   old vertex identifier
        @param[in] theNewVertex   new vertex identifier
        @param[in] theEdge        edge identifier
        @param[in] theExcludingRef reference identifier to exclude from rebinding
        """

    def RebindVertexRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>", theOldVertex: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>", theNewVertex: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>") -> None:
        """
        Rebind a vertex reference to point to a new vertex.
        @param[in] theRefId     vertex reference identifier
        @param[in] theOldVertex old vertex identifier
        @param[in] theNewVertex new vertex identifier
        """

    def RebindCoEdgeEdge(self, theCoEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>", theOldEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", theNewEdge: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>") -> None:
        """
        Rebind a coedge to reference a different edge.
        @param[in] theCoEdge  coedge identifier
        @param[in] theOldEdge old edge identifier
        @param[in] theNewEdge new edge identifier
        """

    def RebindWireRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>", theOldWire: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theNewWire: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> None:
        """
        Rebind a wire reference to point to a new wire.
        @param[in] theRefId   wire reference identifier
        @param[in] theOldWire old wire identifier
        @param[in] theNewWire new wire identifier
        """

    def RebindFaceRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>", theOldFace: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theNewFace: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>") -> None:
        """
        Rebind a face reference to point to a new face.
        @param[in] theRefId   face reference identifier
        @param[in] theOldFace old face identifier
        @param[in] theNewFace new face identifier
        """

    def RebindShellRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>", theOldShell: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", theNewShell: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>") -> None:
        """
        Rebind a shell reference to point to a new shell.
        @param[in] theRefId    shell reference identifier
        @param[in] theOldShell old shell identifier
        @param[in] theNewShell new shell identifier
        """

    def RebindSolidRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>", theOldSolid: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", theNewSolid: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>") -> None:
        """
        Rebind a solid reference to point to a new solid.
        @param[in] theRefId    solid reference identifier
        @param[in] theOldSolid old solid identifier
        @param[in] theNewSolid new solid identifier
        """

    def RebindChildRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>", theOldChild: nanoocp.BRepGraph.BRepGraph_NodeId, theNewChild: nanoocp.BRepGraph.BRepGraph_NodeId) -> None:
        """
        Rebind a child reference to point to a new child node.
        @param[in] theRefId   child reference identifier
        @param[in] theOldChild old child node identifier
        @param[in] theNewChild new child node identifier
        """

    def RebindOccurrenceRef(self, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>", theOldOccurrence: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>", theNewOccurrence: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>") -> None:
        """
        Rebind an occurrence reference to point to a new occurrence.
        @param[in] theRefId         occurrence reference identifier
        @param[in] theOldOccurrence old occurrence identifier
        @param[in] theNewOccurrence new occurrence identifier
        """

    def ReverseWireCoEdges(self, theWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> None:
        """
        Reverse the order of coedges in a wire.
        @param[in] theWireId wire identifier
        """

    def SetWireCoEdges(self, theWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theCoEdgeIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge) -> None:
        """
        Replace the coedge list of a wire with a new set.
        @param[in] theWireId    wire identifier
        @param[in] theCoEdgeIds new coedge identifiers
        """

    def SetFaceWireRefs(self, theFaceId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>", theWireRefIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire) -> None:
        """
        Replace the wire reference list of a face with a new set.
        @param[in] theFaceId    face identifier
        @param[in] theWireRefIds new wire reference identifiers
        """

    def SetShellFaceRefs(self, theShellId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>", theFaceRefIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face) -> None:
        """
        Replace the face reference list of a shell with a new set.
        @param[in] theShellId   shell identifier
        @param[in] theFaceRefIds new face reference identifiers
        """

    def SetSolidShellRefs(self, theSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>", theShellRefIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell) -> None:
        """
        Replace the shell reference list of a solid with a new set.
        @param[in] theSolidId    solid identifier
        @param[in] theShellRefIds new shell reference identifiers
        """

    def SetCompSolidSolidRefs(self, theCompSolidId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>", theSolidRefIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid) -> None:
        """
        Replace the solid reference list of a compsolid with a new set.
        @param[in] theCompSolidId compsolid identifier
        @param[in] theSolidRefIds new solid reference identifiers
        """

    def SetCompoundChildRefs(self, theCompoundId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>", theChildRefIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child) -> None:
        """
        Replace the child reference list of a compound with a new set.
        @param[in] theCompoundId compound identifier
        @param[in] theChildRefIds new child reference identifiers
        """

    def SetProductOccurrenceRefs(self, theProductId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>", theOccurrenceRefIds: nanoocp.NCollection.NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence) -> None:
        """
        Replace the occurrence reference list of a product with a new set.
        @param[in] theProductId       product identifier
        @param[in] theOccurrenceRefIds new occurrence reference identifiers
        """

    def BaseRef(self, theRefId: nanoocp.BRepGraph.BRepGraph_RefId) -> BaseRef:
        """
        Return the BaseRef portion of any ref entry by generic RefId.
        @param[in] theRefId generic reference identifier
        @return const reference to the BaseRef base of the ref entry
        """

    def ChangeBaseRef(self, theRefId: nanoocp.BRepGraph.BRepGraph_RefId) -> BaseRef:
        """
        Return the mutable BaseRef portion of any ref entry by generic RefId.
        @param[in] theRefId generic reference identifier
        @return mutable pointer to the BaseRef base of the ref entry, or nullptr if not found
        """

    def FindNodeIdByUID(self, theUID: nanoocp.BRepGraph.BRepGraph_UID) -> nanoocp.BRepGraph.BRepGraph_NodeId:
        """Resolve an active node UID through storage reverse maps."""

    def FindRefIdByUID(self, theUID: nanoocp.BRepGraph.BRepGraph_RefUID) -> nanoocp.BRepGraph.BRepGraph_RefId:
        """Resolve an active reference UID through storage reverse maps."""

    def FindDefinitionByShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.BRepGraph.BRepGraph_NodeId:
        """
        Returns the node id bound to the given shape definition key, or invalid if not bound.
        """

    def HasShapeBinding(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the given shape definition key is bound to a node."""

    def SetDefinitionShapeBinding(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> None:
        """
        Set or update the shape-to-node binding. Uses replacement semantics:
        binds if absent, updates if already bound.
        """

    def RemoveDefinitionShapeBinding(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theExpectedNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> bool:
        """
        Remove the shape-to-node binding only if it points to the expected node.
        Returns true if the binding was removed.
        """

    def FindOriginal(self, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the original shape for the given node id, or a null shape if not bound.
        """

    def HasOriginal(self, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> bool:
        """Returns true if the given node id has an original shape binding."""

    def BindOriginal(self, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Binds the given node id to its construction-time shape key."""

    def UnBindOriginal(self, theNodeId: nanoocp.BRepGraph.BRepGraph_NodeId) -> None:
        """Removes the original shape binding for the given node id."""

    def CopyShapeBindingsFrom(self, theSource: BRepGraphInc_Storage) -> None:
        """
        Copy shape-to-NodeId and Original shape bindings from another storage.
        Used by identity copy to preserve shape reconstruction bindings.
        """

    def CurrentShapes(self) -> "NCollection_FlatDataMap<BRepGraph_NodeId, BRepGraphInc_Storage::CachedShape, NCollection_DefaultHasher<BRepGraph_NodeId>>":
        """Return the generation-validated node-to-shape reconstruction cache."""

    def ChangeCurrentShapes(self) -> "NCollection_FlatDataMap<BRepGraph_NodeId, BRepGraphInc_Storage::CachedShape, NCollection_DefaultHasher<BRepGraph_NodeId>>":
        """
        Return the mutable generation-validated node-to-shape reconstruction cache.
        """

    def CurrentShapesMutex(self) -> "std::__1::shared_mutex":
        """Return the mutex protecting the reconstruction cache."""

    def ClearCurrentShapes(self) -> None:
        """Clear the generation-validated shape reconstruction cache."""

    def UnbindCurrentShape(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> None:
        """
        Remove one entry from the generation-validated shape reconstruction cache.
        """

    def ClearDeferredQueues(self) -> None:
        """Clear deferred invalidation queues and release their batch allocator."""

    def Clear(self) -> None:
        """Clear all storage."""

    def PrepareForLoad(self, theCounts: BRepGraphInc_Load.Counts) -> None:
        """
        Prepare fixed-size destination ranges for indexed load.

        This is an internal backend preparation API intended for persistence read
        paths that know final section sizes in advance. It clears previous content,
        pre-sizes defs/refs/reps and UID vectors, and initializes relation tables
        exactly once. The load path then restores serialized relation lists and
        calls RebuildDerivedRelations() once to refresh derived incoming maps.
        @param theCounts final per-section slot counts.
        """

    def SetActiveCounts(self, theCounts: BRepGraphInc_Load.Counts) -> None:
        """
        Override active-slot counters after a trusted indexed load path.

        This is intended for persistence backends that already touched every slot
        during load and therefore know exact active counts without rescanning
        storage after relation construction.
        @param theCounts trusted active per-section counts.
        """

    def Counts(self) -> BRepGraphInc_Load.Counts:
        """Build a Counts struct from current allocated slot counts."""

    def ActiveCounts(self) -> BRepGraphInc_Load.Counts:
        """Build a Counts struct from current active (non-removed) counts."""

    def RecountActiveCounts(self) -> None:
        """
        Recount active-slot counters from current `IsRemoved` flags without rebuilding indexes.
        """

    def RebuildDerivedRelations(self) -> None:
        """
        Rebuild centralized relation tables from entity and reference endpoints.
        This is intended for raw load, compact, and explicit repair paths only;
        editor mutations maintain relation containers incrementally.
        """

    def RebuildDerivedRelationsPreservingActiveCounts(self) -> None:
        """
        Rebuild relation maps after a trusted load already restored active counts.
        """

    def CopyRemovedFlagsFrom(self, theSource: BRepGraphInc_Storage) -> None:
        """
        Bulk-copy all RemovedFlags bit-planes from theSource.
        Source must have been loaded with the same entity counts (identity copy path).
        """

    def ValidateRelations(self) -> bool:
        """
        Debug: verify relation-table consistency against entity/reference endpoints.
        @return true if all relations are consistent
        """

    def ValidateWireCoEdgeOrder(self, theWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> bool:
        """
        Verify coedge ordering consistency for a specific wire.
        @param[in] theWireId wire identifier
        @return true if the coedge order is valid
        """

    def ValidateWireCoEdgeOrders(self) -> bool:
        """
        Verify coedge ordering consistency for all wires.
        @return true if all wire coedge orders are valid
        """

    def CanonicalizeWireCoEdgeOrderStatus(self, theWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> BRepGraphInc_Storage.WireCoEdgeOrderStatus:
        """
        Canonicalize the coedge ordering of a wire and report the achieved order quality.
        @param[in] theWireId wire identifier
        @return canonicalization status
        """

    def CanonicalizeWireCoEdgeOrder(self, theWireId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>") -> bool:
        """
        Canonicalize the coedge ordering of a wire to a consistent form.
        @param[in] theWireId wire identifier
        @return true if canonicalization succeeded
        """

    def RebuildUIDReverseIndexes(self) -> None:
        """
        Rebuild UID reverse indexes (UID->NodeId, RefUID->RefId)
        from the current UID vectors. Clears indexes and resets allocators before rebuilding.
        Called after Compact, Load, etc. where UID vectors have been modified externally.
        """

    def MarkUIDReverseIndexesDirty(self) -> None:
        """Mark UID reverse indexes stale after bulk UID-vector replacement."""

    def EnsureUIDReverseIndex(self) -> None:
        """Lazily rebuild the node UID reverse index if it is stale."""

    def EnsureRefUIDReverseIndex(self) -> None:
        """Lazily rebuild the reference UID reverse index if it is stale."""

    def CopyDerivedRelationsFrom(self, theSource: BRepGraphInc_Storage) -> None:
        """
        Copy all forward/reverse relation vectors directly from theSource.
        Used by identity copy to avoid the clear+rebuild cycle.
        """

    def HasCompoundParent(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> bool:
        """
        Return true if the node identified by the given generic NodeId has a parent compound.
        Dispatches by node kind to the appropriate per-kind bitset.
        @param[in] theNode generic node identifier
        """

    def HasOccurrenceParent(self, theNode: nanoocp.BRepGraph.BRepGraph_NodeId) -> bool:
        """
        Return true if the node identified by the given generic NodeId has a parent occurrence.
        Dispatches by node kind to the appropriate per-kind bitset.
        @param[in] theNode generic node identifier
        """

    def IsGuarded(self, theId: nanoocp.BRepGraph.BRepGraph_ItemId) -> bool:
        """
        Return true if the entity identified by the given generic item id has an active MutGuard.
        @param[in] theId generic item identifier (node, reference, or representation)
        """

    def SetGuarded(self, theId: nanoocp.BRepGraph.BRepGraph_ItemId) -> None:
        """
        Register an active MutGuard on the entity identified by the given generic item id.
        @param[in] theId generic item identifier (node, reference, or representation)
        """

    def ClearGuarded(self, theId: nanoocp.BRepGraph.BRepGraph_ItemId) -> None:
        """
        Deregister an active MutGuard from the entity identified by the given generic item id.
        @param[in] theId generic item identifier (node, reference, or representation)
        """

    def HasAnyGuard(self) -> bool:
        """
        Return true if any entity in any store has an active MutGuard.
        Used to assert no guards are active before Clear().
        """
