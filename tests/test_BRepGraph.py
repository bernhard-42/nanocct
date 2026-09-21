"""BRepGraph (OCCT 8's graph-based BRep): typed ids are aliases of class templates nested in a class
(BRepGraph_NodeId::Typed<Kind::Edge>), iterators of templates nested in namespaces; all instantiated by rule 6c."""
import pytest

from nanoocp import BRep, BRepGraph, Geom, TopAbs, TopoDS, gp


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
    assert not BRepGraph.BRepGraph_EdgeId.Invalid().IsValid()
    node = BRepGraph.BRepGraph_NodeId(eid)                         # operator BRepGraph_NodeId() -> constructor of the target
    assert node.NodeKind == BRepGraph.BRepGraph_NodeId.Kind.Edge
    assert BRepGraph.BRepGraph_EdgeId.FromNodeId(node) == eid
    assert hash(node) == hash(BRepGraph.BRepGraph_NodeId(eid))    # std::hash<BRepGraph_NodeId>
    assert hash(eid) == hash(ids[0]) and {eid: 1}[BRepGraph.BRepGraph_EdgeId.FromNodeId(node)] == 1   # partial std::hash<Typed<K>>
    assert g.Shapes().Shape(eid).IsSame(e)                         # implicit EdgeId -> NodeId conversion at the call
    guard = g.Editor().Edges().Mut(eid)                            # BRepGraph_MutGuard<BRepGraphInc::EdgeDef>: instantiated from the signature (6c)
    assert type(guard).__name__ == "BRepGraph_MutGuard__BRepGraphInc_EdgeDef" and guard.Id() == eid


def test_tool_and_ref_iterators():
    g, e = _edge_graph()
    eid = BRepGraph.BRepGraph_EdgeIterator(g).CurrentId()
    Edge, Vertex = BRepGraph.BRepGraph_Tool.Edge, BRepGraph.BRepGraph_Tool.Vertex   # nested static-only classes
    assert Edge.Range(g, eid) == (0.0, 1.0)                        # std::pair -> tuple
    assert type(Edge.Curve(g, eid)) is Geom.Geom_Line
    assert Edge.Degenerated(g, eid) is False
    start, end = Edge.StartVertexId(g, eid), Edge.EndVertexId(g, eid)
    assert type(start) is BRepGraph.BRepGraph_VertexRefId and start != end
    assert Vertex.Pnt(g, start).Coord__float_float_float() == (0.0, 0.0, 0.0) and Vertex.Pnt(g, end).Coord__float_float_float() == (1.0, 0.0, 0.0)
    refs = 0
    rit = BRepGraph.BRepGraph_RefsVertexOfEdge(g, eid)             # BRepGraph_RefsIterator::RefsOfParent<VertexOfEdgeTraits>
    while rit.More():
        assert type(rit.CurrentId()) is BRepGraph.BRepGraph_VertexRefId
        refs += 1
        rit.Next()
    assert refs == 2
