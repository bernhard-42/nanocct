"""Generated bindings for TKXMesh: the XBRepMesh_Factory plug-in (one class, nothing unbound). Constructing a second factory is
undefined behaviour in OCCT itself (its constructor registers `this` through a temporary handle, finds the name taken, and the
temporary deletes the half-built object -- verified in plain C++, refcount garbage, Python segfaults): use the registry."""
from pathlib import Path

from nanocct import BRep, BRepMesh, BRepPrimAPI, TopAbs, TopExp, TopLoc, TopoDS, XBRepMesh

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKXMesh" / "report.txt"


def test_xbrepmesh_factory_from_the_registry():
    factory = BRepMesh.BRepMesh_DiscretAlgoFactory.FindFactory_s("XBRepMesh")
    assert type(factory) is XBRepMesh.XBRepMesh_Factory and factory.Name().ToCString() == "XBRepMesh"
    assert len(BRepMesh.BRepMesh_DiscretAlgoFactory.Factories_s()) == 2                      # IncrementalMesh + XBRepMesh
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
    algo = factory.CreateAlgorithm(box, 0.1, 0.5)
    assert type(algo) is BRepMesh.BRepMesh_IncrementalMesh                                  # most-derived type through the handle
    algo.Perform()
    faces = [TopoDS.Face(f) for f in TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE)]
    assert sum(BRep.BRep_Tool.Triangulation_s(f, TopLoc.TopLoc_Location()).NbTriangles() for f in faces) == 12
    assert [l for l in REPORT.read_text().splitlines() if not l.startswith("#")] == []
