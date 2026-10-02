"""BRepGraph (OCCT 8's graph-based BRep): typed ids are aliases of class templates nested in a class
(BRepGraph_NodeId::Typed<Kind::Edge>), iterators of templates nested in namespaces; all instantiated by rule 6c."""
import gc

import pytest

from nanocct import BRep, BRepGraph, BRepGraphInc, BRepPrimAPI, Geom, TopAbs, TopoDS, gp


def _edge_graph() -> tuple[BRepGraph.BRepGraph, TopoDS.TopoDS_Edge]:
    b = BRep.BRep_Builder()
    v1, v2 = TopoDS.TopoDS_Vertex(), TopoDS.TopoDS_Vertex()
    b.MakeVertex(v1, gp.gp_Pnt(0.0, 0.0, 0.0), 1e-7)
    b.MakeVertex(v2, gp.gp_Pnt(1.0, 0.0, 0.0), 1e-7)
    e = TopoDS.TopoDS_Edge()
    b.MakeEdge(e, Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)), 1e-7)
    v1.Orientation(TopAbs.TopAbs_Orientation.TopAbs_FORWARD)
    v2.Orientation(TopAbs.TopAbs_Orientation.TopAbs_REVERSED)
    b.Add(e, v1)
    b.Add(e, v2)
    b.Range(e, 0.0, 1.0)
    g = BRepGraph.BRepGraph()
    g.Clear()
    result = g.Shapes().Add(e)                                     # BRepGraph::ShapesView::Result (nested class of a nested class)
    assert result.IsOk() and result.Status == BRepGraph.BRepGraph.ShapesView.AddStatus.Success
    return g, e


def test_typed_ids_and_iterators():
    g, e = _edge_graph()
    assert (g.Topo().Edges().Nb(), g.Topo().Vertices().Nb()) == (1, 2)
    ids = []
    it = BRepGraph.BRepGraph_EdgeIterator(g)                       # BRepGraph_Iterator<BRepGraphInc::EdgeDef> (defaulted bool argument)
    while it.More():
        ids.append(it.CurrentId())                                 # `TypedId`, a member typedef of the template
        it.Next()
    assert len(ids) == 1 and type(ids[0]) is BRepGraph.BRepGraph_EdgeId   # BRepGraph_NodeId::Typed<BRepGraph_NodeId::Kind::Edge>
    eid = ids[0]
    assert eid.IsValid() and eid.Index == 0
    assert not BRepGraph.BRepGraph_EdgeId.Invalid_s().IsValid()
    node = BRepGraph.BRepGraph_NodeId(eid)                         # operator BRepGraph_NodeId() -> constructor of the target
    assert node.NodeKind == BRepGraph.BRepGraph_NodeId.Kind.Edge
    assert BRepGraph.BRepGraph_EdgeId.FromNodeId_s(node) == eid
    assert hash(node) == hash(BRepGraph.BRepGraph_NodeId(eid))    # std::hash<BRepGraph_NodeId>
    assert hash(eid) == hash(ids[0]) and {eid: 1}[BRepGraph.BRepGraph_EdgeId.FromNodeId_s(node)] == 1   # partial std::hash<Typed<K>>
    assert g.Shapes().Shape(eid).IsSame(e)                         # implicit EdgeId -> NodeId conversion at the call
    guard = g.Editor().Edges().Mut(eid)                            # BRepGraph_MutGuard<BRepGraphInc::EdgeDef>: instantiated from the signature (6c)
    assert type(guard).__name__ == "BRepGraph_MutGuard__BRepGraphInc_EdgeDef" and guard.Id() == eid


def test_tool_and_ref_iterators():
    g, e = _edge_graph()
    eid = BRepGraph.BRepGraph_EdgeIterator(g).CurrentId()
    Edge, Vertex = BRepGraph.BRepGraph_Tool.Edge, BRepGraph.BRepGraph_Tool.Vertex   # nested static-only classes
    assert Edge.Range_s(g, eid) == (0.0, 1.0)                        # std::pair -> tuple
    assert type(Edge.Curve_s(g, eid)) is Geom.Geom_Line
    assert Edge.Degenerated_s(g, eid) is False
    start, end = Edge.StartVertexId_s(g, eid), Edge.EndVertexId_s(g, eid)
    assert type(start) is BRepGraph.BRepGraph_VertexRefId and start != end
    assert Vertex.Pnt_s(g, start).Coord__float__float__float() == (0.0, 0.0, 0.0) and Vertex.Pnt_s(g, end).Coord__float__float__float() == (1.0, 0.0, 0.0)
    refs = 0
    rit = BRepGraph.BRepGraph_RefsVertexOfEdge(g, eid)             # BRepGraph_RefsIterator::RefsOfParent<VertexOfEdgeTraits>
    while rit.More():
        assert type(rit.CurrentId()) is BRepGraph.BRepGraph_VertexRefId
        refs += 1
        rit.Next()
    assert refs == 2
    # R-USING: BRepGraph_FacesOfEdge inherits the constructors of its 6c base (`using EdgeParentsOf<...>::EdgeParentsOf;`)
    faces = BRepGraph.BRepGraph_FacesOfEdge(g, eid)
    assert faces.More() is False and list(faces) == []
    sigs = [l for l in BRepGraph.BRepGraph_FacesOfEdge.__init__.__doc__.splitlines() if l.startswith("__init__")]
    assert len(sigs) == 3 and "theStartIndex: int" in sigs[1]


def test_graph_iterators_and_flat_maps_are_python_iterables():
    """the Current() of BRepGraph_Iterator<...Def> and the Value() of NCollection_FlatMap<K, H>::Iterator are
    a dependent `const T&` inside the 6c walk, which R-ITER did not accept, and the flat maps' nested Iterator was not bound
    at all -- neither could be used in a `for` loop."""
    g = BRepGraph.BRepGraph()
    g.Clear()
    assert g.Shapes().Add(BRepPrimAPI.BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()).IsOk()
    edges, faces = list(BRepGraph.BRepGraph_EdgeIterator(g)), list(BRepGraph.BRepGraph_FaceIterator(g))
    assert (len(edges), len(faces)) == (12, 6) and type(edges[0]).__name__ == "EdgeDef"
    flat = BRepGraph.NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId
    ids = flat()
    for i in (3, 1, 7):
        ids.Add(BRepGraph.BRepGraph_NodeId(BRepGraph.BRepGraph_NodeId.Kind.Face, i))
    assert sorted(n.Index for n in flat.Iterator(ids)) == [1, 3, 7]


def test_flat_map_contained_returns_the_stored_entries():
    """R-REFWRAP: std::reference_wrapper results (nanobind has no caster for them; without nanocct's, Contained() would
    raise TypeError). A const reference comes back as a copy (the key), a mutable one as a reference into the map that
    keeps it alive (the data map's value)."""
    flat = BRepGraph.NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId()
    key = BRepGraph.BRepGraph_NodeId(BRepGraph.BRepGraph_NodeId.Kind.Face, 3)
    flat.Add(key)
    assert flat.Contained(key) == key and flat.Contained(BRepGraph.BRepGraph_NodeId(BRepGraph.BRepGraph_NodeId.Kind.Face, 99)) is None
    data_map = next(getattr(BRepGraphInc, n) for n in dir(BRepGraphInc) if n.startswith("NCollection_FlatDataMap"))()
    data_map.Bind(key, BRepGraphInc.BRepGraphInc_Storage.CachedShape())
    stored_key, value = data_map.Contained(key)
    assert stored_key == key and value.StoredSubtreeGen == 0
    value.StoredSubtreeGen = 7                                         # a mutable reference: the edit reaches the map
    assert data_map.Find(key).StoredSubtreeGen == 7
    del data_map
    gc.collect()
    assert value.StoredSubtreeGen == 7                                 # and the value keeps the map alive



def test_6c_instantiation_names_spell_every_template_argument():
    """Design 6c: a 6c instantiation's name spells every template argument, the default hasher included, where the 6a binder
    kinds drop it (NCollection_Map<int> is NCollection_Map__int). The OCCT 8 flat maps are not binder kinds, so their names
    carry NCollection_DefaultHasher; kept as released in 8.0.1.0 (the final review's F5, 2026-09-30). Pinned here, so a change
    of a default argument in OCCT, which would rename them, fails a test instead of passing silently."""
    import nanocct.Poly as Poly
    for name in ("NCollection_FlatMap__BRepGraph_UID__NCollection_DefaultHasher__BRepGraph_UID",
                 "NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId",
                 "NCollection_FlatMap__BRepGraph_ItemUID__NCollection_DefaultHasher__BRepGraph_ItemUID",
                 "NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId__NCollection_DefaultHasher__BRepGraph_ItemId"):
        assert hasattr(BRepGraph, name), name
    assert hasattr(BRepGraphInc, "NCollection_FlatDataMap__BRepGraph_NodeId__BRepGraphInc_Storage_CachedShape"
                                 "__NCollection_DefaultHasher__BRepGraph_NodeId")
    assert hasattr(Poly, "NCollection_AliasedArray__")


def test_an_enum_parameter_takes_no_bool_or_int():
    """nanobind's enum caster took any int that is an enumerator's value in its convert pass, True and False included:
    with a typed root (converted to BRepGraph_NodeId) (Kind, True, False) reached the (AvoidKind, EmitAvoidKind,
    TraversalMode) overload, registered first, instead of C++'s (TargetKind, CumLoc, CumOri). An enum parameter takes
    only its enumerators now, as in C++ (2026-09-30)."""
    g = BRepGraph.BRepGraph()
    g.Clear()
    g.Shapes().Add(BRepPrimAPI.BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape())
    kind = BRepGraph.BRepGraph_NodeId.Kind
    explorer = BRepGraph.BRepGraph_ChildExplorer(g, BRepGraph.BRepGraph_SolidId.Start_s(), kind.Edge, True, False)
    orientations = []
    while explorer.More():
        orientations.append(explorer.Current().Orientation)
        explorer.Next()
    assert len(orientations) == 24 and set(orientations) == {TopAbs.TopAbs_Orientation.TopAbs_FORWARD}   # CumOri=False
    root = BRepGraph.BRepGraph_NodeId(BRepGraph.BRepGraph_SolidId.Start_s())
    assert BRepGraph.BRepGraph_ChildExplorer(g, root, None, False).More()   # std::optional<Kind> AvoidKind: None stays nullopt
    v = TopoDS.TopoDS_Vertex()
    with pytest.raises(TypeError):
        v.Orientation(1)                                           # C++ has no int -> TopAbs_Orientation conversion either
    v.Orientation(TopAbs.TopAbs_Orientation.TopAbs_REVERSED)
    assert v.Orientation() == TopAbs.TopAbs_REVERSED
