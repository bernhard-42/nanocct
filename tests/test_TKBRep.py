"""Generated bindings for TKBRep: TopoDS shapes (implicit copy constructors, __hash__ from std::hash, the TopoDS
namespace functions), BRep_Builder/BRep_Tool, TopExp, TopTools aliases of hashed containers, adaptors, BRep/BinTools I/O."""
import importlib
import os
import tempfile

import pytest

from nanoocp import BRep, BRepAdaptor, BRepLProp, BRepTools, BinTools, Geom, GeomAbs, NCollection, TopAbs, TopExp, TopTools, TopoDS, gp

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
    assert not hasattr(BRepGraph, "BRepGraph_CacheMesh")            # member of a type defined only in the .cxx
    assert hasattr(BRepGraph, "BRepGraph")                          # the graph itself is bound
