"""Generated bindings for TKBRep: TopoDS shapes (implicit copy constructors, __hash__ from std::hash, the TopoDS
namespace functions), BRep_Builder/BRep_Tool, TopExp, TopTools aliases of hashed containers, adaptors, BRep/BinTools I/O."""
import importlib
import os
import tempfile
from pathlib import Path

import pytest

from nanoocp import BRep, BRepAdaptor, BRepLProp, BRepTools, BinTools, Geom, Geom2d, GeomAbs, NCollection, Standard, TopAbs, TopExp, TopLoc, TopTools, TopoDS, gp

PACKAGES = ["TopoDS", "TopExp", "TopTools", "BRep", "BRepLProp", "BRepAdaptor", "BRepTools", "BinTools", "BRepGraph", "BRepGraphInc"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _compound() -> tuple[TopoDS.TopoDS_Compound, TopoDS.TopoDS_Vertex, TopoDS.TopoDS_Edge]:
    b = BRep.BRep_Builder()
    v = TopoDS.TopoDS_Vertex()
    b.MakeVertex(v, gp.gp_Pnt(1.0, 2.0, 3.0), 1e-7)
    e = TopoDS.TopoDS_Edge()
    b.MakeEdge(e, Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)), 1e-7)
    c = TopoDS.TopoDS_Compound()
    b.MakeCompound(c)
    b.Add(c, v)
    b.Add(c, e)
    return c, v, e


def test_shapes_copy_equality_and_hash():
    c, v, e = _compound()
    assert v.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_VERTEX and not v.IsNull()
    assert BRep.BRep_Tool.Pnt(v).Coord() == (1.0, 2.0, 3.0)
    assert BRep.BRep_Tool.Tolerance(v) == 1e-7
    s = TopoDS.TopoDS_Shape(v)                                     # implicit copy constructor; sub-class converts, as in C++
    assert type(s) is TopoDS.TopoDS_Shape and s.IsSame(v) and s == v
    assert hash(s) == hash(v)                                      # __hash__ from OCCT's std::hash<TopoDS_Shape>
    assert {v: "vertex"}[TopoDS.Vertex(s)] == "vertex"             # TopoDS::Vertex(const TopoDS_Shape&) -> nanoocp.TopoDS.Vertex
    assert type(TopoDS.Vertex(s)) is TopoDS.TopoDS_Vertex
    assert s.Reversed().Orientation() == TopAbs.TopAbs_Orientation.TopAbs_REVERSED
    assert s.Reversed() != s
    assert type(TopoDS.TopoDS_Compound(c)) is TopoDS.TopoDS_Compound
    assert hash(gp.gp_Pnt(1.0, 2.0, 3.0)) == hash(gp.gp_Pnt(1.0, 2.0, 3.0))   # std::hash<gp_Pnt> too


def test_explorer_iterator_and_shape_maps():
    c, v, e = _compound()
    assert c.NbChildren() == 2
    found = []
    ex = TopExp.TopExp_Explorer(c, TopAbs.TopAbs_ShapeEnum.TopAbs_VERTEX)
    while ex.More():
        found.append(ex.Current())
        ex.Next()
    assert len(found) == 1 and found[0].IsSame(v)
    kinds = []
    it = TopoDS.TopoDS_Iterator(c)
    while it.More():
        kinds.append(it.Value().ShapeType())
        it.Next()
    assert kinds == [TopAbs.TopAbs_ShapeEnum.TopAbs_VERTEX, TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE]
    # hashed containers keep a non-default hasher in their type: NCollection_IndexedMap<TopoDS_Shape, TopTools_ShapeMapHasher>
    Map = NCollection.NCollection_IndexedMap[TopoDS.TopoDS_Shape, TopTools.TopTools_ShapeMapHasher]
    assert Map is TopTools.TopTools_IndexedMapOfShape
    m = Map()
    TopExp.TopExp.MapShapes(c, m)
    assert m.Extent() == 3 and [s.ShapeType() for s in m][0] == TopAbs.TopAbs_ShapeEnum.TopAbs_COMPOUND
    lst = NCollection.NCollection_List[TopoDS.TopoDS_Shape]()
    lst.Append(v)
    assert type(lst) is TopTools.TopTools_ListOfShape and v in lst


def test_brep_tool_and_adaptors():
    c, v, e = _compound()
    curve, first, last = BRep.BRep_Tool.Curve(e)                    # handle + two double& out-params
    assert type(curve) is Geom.Geom_Line and first == -2e100 and last == 2e100
    assert BRep.BRep_Tool.Degenerated(e) is False
    # Parameter(V, E) -> double (throws) and Parameter(V, E, double&) -> bool collide after out-param removal: the
    # scalar-returning overload without out-params wins
    b = BRep.BRep_Builder()
    free_edge = TopoDS.TopoDS_Edge()                                 # e above is frozen (it belongs to the compound)
    b.MakeEdge(free_edge, Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)), 1e-7)
    on_edge = TopoDS.TopoDS_Vertex()
    b.MakeVertex(on_edge, gp.gp_Pnt(2.0, 0.0, 0.0), 1e-7)
    on_edge.Orientation(TopAbs.TopAbs_Orientation.TopAbs_FORWARD)
    b.Add(free_edge, on_edge)
    b.Range(free_edge, 0.0, 2.0)
    b.UpdateVertex(on_edge, 2.0, free_edge, 1e-7)                   # the vertex's parameter on the edge
    assert BRep.BRep_Tool.Parameter(on_edge, free_edge) == 2.0
    with pytest.raises(Standard.Standard_NoSuchObject):
        BRep.BRep_Tool.Parameter(v, free_edge)                      # v is not a vertex of that edge
    ad = BRepAdaptor.BRepAdaptor_Curve(e)
    assert ad.GetType() == GeomAbs.GeomAbs_CurveType.GeomAbs_Line
    assert ad.Line().Direction().Coord() == (1.0, 0.0, 0.0)
    props = BRepLProp.BRepLProp_CLProps(ad, 2.0, 1, 1e-9)
    assert props.Value().Coord() == (2.0, 0.0, 0.0)


def test_brep_and_binary_round_trip():
    c, v, e = _compound()
    d = tempfile.mkdtemp()
    path = os.path.join(d, "c.brep")
    assert BRepTools.BRepTools.Write(c, path) is True
    back = TopoDS.TopoDS_Shape()
    assert BRepTools.BRepTools.Read(back, path, BRep.BRep_Builder()) is True
    assert back.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_COMPOUND and back.NbChildren() == 2
    binary = os.path.join(d, "c.bin")
    assert BinTools.BinTools.Write(c, binary) is True
    back2 = TopoDS.TopoDS_Shape()
    assert BinTools.BinTools.Read(back2, binary) is True and back2.NbChildren() == 2


def test_unbindable_classes_are_reported_not_bound():
    from nanoocp import BRepGraph
    from generator.report import read_report
    assert not hasattr(BRepGraph, "BRepGraph_CacheMesh")            # member of a type defined only in the .cxx
    assert hasattr(BRepGraph, "BRepGraph")                          # the graph itself is bound
    rows = read_report(Path(__file__).parents[1] / "src" / "cpp" / "TKBRep" / "report.txt")
    matches = [(cat, pkg, msg) for cat, pkg, msg in rows if msg.startswith("BRepGraph_CacheMesh:")]
    assert matches == [("incomplete", "BRepGraph",
                        "BRepGraph_CacheMesh: member mySlots of incomplete type BRepGraph_CacheMesh::Slot -> class skipped")]
    assert all(cat != "misc" for cat, _, _ in rows)                 # every omission has a category (generator/report.py)


def test_handle_parameters_accept_none():
    # a handle<T> parameter is nb::arg(...).none(): None is the null handle (Design.md 4.2)
    tf = BRep.BRep_TFace()
    tf.Surface(None)
    assert tf.Surface() is None
    b = BRep.BRep_Builder()
    e = TopoDS.TopoDS_Edge()
    b.MakeEdge(e)
    b.UpdateEdge(e, None, TopLoc.TopLoc_Location(), 1e-6)          # handle<Geom_Curve>& C = null: an edge without 3D curve
    assert BRep.BRep_Tool.Degenerated(e) is False


def test_handle_out_parameters_are_returned():
    # handle<T>& out-parameters come back in the result tuple, like double& (Design.md 6)
    b = BRep.BRep_Builder()
    e = TopoDS.TopoDS_Edge()
    b.MakeEdge(e, Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)), 1e-7)
    b.Range(e, 0.0, 2.0)
    plane = Geom.Geom_Plane(gp.gp_Pnt(), gp.gp_Dir(0.0, 0.0, 1.0))
    b.UpdateEdge(e, Geom2d.Geom2d_Line(gp.gp_Pnt2d(), gp.gp_Dir2d(1.0, 0.0)), plane, TopLoc.TopLoc_Location(), 1e-7)
    loc = TopLoc.TopLoc_Location()
    curve2d, surface, first, last = BRep.BRep_Tool.CurveOnSurface(e, loc)   # C, S (out), L (in place), First, Last (out)
    assert isinstance(curve2d, Geom2d.Geom2d_Line) and surface is plane
    assert (first, last) == (0.0, 2.0)
    assert BRep.BRep_Tool.CurveOnSurface.__doc__.splitlines()[0].endswith(
        "-> tuple[nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom.Geom_Surface, float, float]")


def test_unscoped_enumerators_are_exported_to_the_enclosing_scope():
    # C++ puts TopAbs_FACE next to TopAbs_ShapeEnum; export_values() does the same (Design.md 6)
    assert TopAbs.TopAbs_FACE is TopAbs.TopAbs_ShapeEnum.TopAbs_FACE
    assert int(TopAbs.TopAbs_FACE) == 4
    assert TopoDS.TopoDS_TShape.Bits_Reserved is TopoDS.TopoDS_TShape.BitLayout.Bits_Reserved   # nested unscoped enum -> class attribute
    assert gp.gp_Dir.D.NZ is not None and not hasattr(gp.gp_Dir, "NZ")                        # scoped enum class stays nested
