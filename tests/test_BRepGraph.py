"""BRepGraph (OCCT 8's graph-based BRep): typed ids are aliases of class templates nested in a class
(BRepGraph_NodeId::Typed<Kind::Edge>), iterators of templates nested in namespaces; all instantiated by rule 7c."""
import gc

import pytest

from nanocct import BRep, BRepGraph, BRepGraphInc, BRepPrimAPI, Geom, NCollection, TopAbs, TopoDS, gp


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
    guard = g.Editor().Edges().Mut(eid)                            # BRepGraph_MutGuard<BRepGraphInc::EdgeDef>: instantiated from the signature (7c)
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
    # R-USING: BRepGraph_FacesOfEdge inherits the constructors of its 7c base (`using EdgeParentsOf<...>::EdgeParentsOf;`)
    faces = BRepGraph.BRepGraph_FacesOfEdge(g, eid)
    assert faces.More() is False and list(faces) == []
    sigs = [l for l in BRepGraph.BRepGraph_FacesOfEdge.__init__.__doc__.splitlines() if l.startswith("__init__")]
    assert len(sigs) == 3 and "theStartIndex: int" in sigs[1]


def _face_id(i: int) -> BRepGraph.BRepGraph_NodeId:
    return BRepGraph.BRepGraph_NodeId(BRepGraph.BRepGraph_NodeId.Kind.Face, i)


def test_graph_iterators_and_flat_maps_are_python_iterables():
    """the Current() of BRepGraph_Iterator<...Def> and the Value() of NCollection_FlatMap<K, H>::Iterator are
    a dependent `const T&` inside the 7c walk, which R-ITER did not accept, and the flat maps' nested Iterator was not bound
    at all -- neither could be used in a `for` loop. The flat maps iterate over their keys too, as the other maps (7a)."""
    g = BRepGraph.BRepGraph()
    g.Clear()
    assert g.Shapes().Add(BRepPrimAPI.BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()).IsOk()
    edges, faces = list(BRepGraph.BRepGraph_EdgeIterator(g)), list(BRepGraph.BRepGraph_FaceIterator(g))
    assert (len(edges), len(faces)) == (12, 6) and type(edges[0]).__name__ == "EdgeDef"
    flat = NCollection.NCollection_FlatMap[BRepGraph.BRepGraph_NodeId]
    ids = flat()
    for i in (3, 1, 7):
        ids.Add(_face_id(i))
    assert sorted(n.Index for n in flat.Iterator(ids)) == [1, 3, 7]
    assert sorted(n.Index for n in ids) == [1, 3, 7]


def test_flat_map_contained_returns_copies():
    """R-REFWRAP, R-CONST-TWIN: Contained() hands out copies -- the key, and the (key, value) pair of the data map, whose
    non-const overload has the value mutable; Python cannot choose between the two, so the binder takes the const one, as
    for the other maps (7a). The value itself comes from ChangeFind or ChangeSeek, a view that keeps the map alive."""
    flat = NCollection.NCollection_FlatMap[BRepGraph.BRepGraph_NodeId]()
    key = _face_id(3)
    flat.Add(key)
    assert flat.Contained(key) == key and flat.Contained(_face_id(99)) is None
    data_map = NCollection.NCollection_FlatDataMap[BRepGraph.BRepGraph_NodeId, BRepGraphInc.BRepGraphInc_Storage.CachedShape]()
    data_map.Bind(key, BRepGraphInc.BRepGraphInc_Storage.CachedShape())
    stored_key, copy = data_map.Contained(key)
    assert stored_key == key and copy.StoredSubtreeGen == 0
    copy.StoredSubtreeGen = 7                                          # a copy: the map keeps its value
    assert data_map.Find(key).StoredSubtreeGen == 0
    value = data_map.ChangeFind(key)
    value.StoredSubtreeGen = 7                                         # the view: the edit reaches the map
    assert data_map.Find(key).StoredSubtreeGen == 7
    data_map = None
    gc.collect()
    assert value.StoredSubtreeGen == 7                                 # and the view keeps the map alive


def test_flat_maps_refuse_moves_while_a_value_is_viewed():
    """R-VIEW-GUARD: the flat maps keep their entries in one slot array. Every insertion can grow it (a new array, the old
    one freed -- also for a key already there) and moves entries already in it by Robin Hood probing; a removal shifts the
    entries after it. So while a value view lives, every insertion and removal raises BufferError, and an iterator goes
    stale on them. As generated classes, a ChangeFind view read freed memory after the map grew, and an iterator read the
    slots Clear(True) had freed (2026-11-24)."""
    item = BRepGraph.BRepGraph_ItemId
    data_map = NCollection.NCollection_FlatDataMap[item, item]()
    data_map.Bind(item(_face_id(0)), item(_face_id(100)))
    view = data_map.ChangeFind(item(_face_id(0)))
    for call in (lambda: data_map.Bind(item(_face_id(1)), item(_face_id(101))),
                 lambda: data_map.Bind(item(_face_id(0)), item(_face_id(102))),     # a bound key: still a possible rehash
                 lambda: data_map.TryBind(item(_face_id(1)), item(_face_id(101))),
                 lambda: data_map.Bound(item(_face_id(1)), item(_face_id(101))),
                 lambda: data_map.TryBound(item(_face_id(1)), item(_face_id(101))),
                 lambda: data_map.__setitem__(item(_face_id(1)), item(_face_id(101))),
                 lambda: data_map.UnBind(item(_face_id(0))),
                 lambda: data_map.Reserve(100),
                 lambda: data_map.Clear(True)):
        with pytest.raises(BufferError):
            call()
    assert view.NodeId().Index == 100
    view = None
    for i in range(1, 2000):                                           # grows the slot array from 8 slots
        data_map.Bind(item(_face_id(i)), item(_face_id(1000 + i)))
    assert data_map.Find(item(_face_id(0))).NodeId().Index == 100 and len(data_map) == 2000
    it = data_map.Iterator(data_map)
    data_map.Clear(True)
    with pytest.raises(RuntimeError):
        it.More()
    keys = NCollection.NCollection_FlatMap[BRepGraph.BRepGraph_NodeId]()
    keys.Add(_face_id(5))
    key_view = keys.ChangeSeek(_face_id(5))
    with pytest.raises(BufferError):
        keys.Add(_face_id(6))
    with pytest.raises(BufferError):
        keys.Remove(_face_id(5))
    key_view = None
    assert keys.Add(_face_id(6)) is True and keys.Remove(_face_id(5)) is True and len(keys) == 1


def test_flat_data_map_python_additions():
    """7a: len(), in, iteration over the keys, items(), m[k] (KeyError for a key that is not bound, as for a dict), m[k] = v
    and del m[k], as on NCollection_DataMap."""
    item = BRepGraph.BRepGraph_ItemId
    m = NCollection.NCollection_FlatDataMap[item, item]()
    m[item(_face_id(1))] = item(_face_id(11))
    m[item(_face_id(2))] = item(_face_id(12))
    assert len(m) == 2 and m.Extent() == 2 and item(_face_id(1)) in m and item(_face_id(3)) not in m
    assert sorted(k.NodeId().Index for k in m) == [1, 2]
    assert sorted((k.NodeId().Index, v.NodeId().Index) for k, v in m.items()) == [(1, 11), (2, 12)]
    assert m[item(_face_id(2))].NodeId().Index == 12 and m.Seek(item(_face_id(3))) is None
    with pytest.raises(KeyError):
        m[item(_face_id(3))]
    del m[item(_face_id(1))]
    with pytest.raises(KeyError):
        del m[item(_face_id(1))]
    assert len(m) == 1


def test_6c_instantiation_names_spell_every_template_argument():
    """Design 7c: a 7c instantiation's name spells every template argument (`NCollection_AliasedArray<>`, every argument
    defaulted, is `Poly.NCollection_AliasedArray__`), where the 7a binder kinds drop a default hasher. The OCCT 8 flat maps
    are binder kinds since 2026-11-24, so they live in nanocct.NCollection, without NCollection_DefaultHasher in their
    names; in 8.0.1.x they were 7c instantiations in BRepGraph and BRepGraphInc. Pinned here, so a change of a default
    argument in OCCT, which would rename them, fails a test instead of passing silently."""
    import nanocct.Poly as Poly
    for name, generic in (("NCollection_FlatMap__BRepGraph_UID", NCollection.NCollection_FlatMap[BRepGraph.BRepGraph_UID]),
                          ("NCollection_FlatMap__BRepGraph_NodeId", NCollection.NCollection_FlatMap[BRepGraph.BRepGraph_NodeId]),
                          ("NCollection_FlatMap__BRepGraph_ItemUID", NCollection.NCollection_FlatMap[BRepGraph.BRepGraph_ItemUID]),
                          ("NCollection_FlatDataMap__BRepGraph_ItemId__BRepGraph_ItemId",
                           NCollection.NCollection_FlatDataMap[BRepGraph.BRepGraph_ItemId, BRepGraph.BRepGraph_ItemId]),
                          ("NCollection_FlatDataMap__BRepGraph_NodeId__BRepGraphInc_Storage_CachedShape",
                           NCollection.NCollection_FlatDataMap[BRepGraph.BRepGraph_NodeId, BRepGraphInc.BRepGraphInc_Storage.CachedShape])):
        assert getattr(NCollection, name) is generic, name
    assert [n for n in dir(BRepGraph) + dir(BRepGraphInc) if n.startswith("NCollection_Flat")] == []
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
