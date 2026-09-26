"""Generated bindings for TKBool: BRepFill (lofts, pipes), BRepAlgo, BRepProj and the old TopOpeBRep boolean kernel with its
package-level free functions. New with this toolkit: R-UNDEFINED covers free functions (two TopOpeBRepDS FUN_* declared without
a definition broke the link), and NCollection_TListIterator<T> in a signature resolves to the List binder's Iterator."""
import importlib
import math
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import BRepAlgo, BRepBuilderAPI, BRepFill, BRepGProp, BRepPrimAPI, BRepProj, GProp, GeomAbs, NCollection, TopAbs, TopExp, TopOpeBRepDS, TopOpeBRepTool, TopoDS, gp

PACKAGES = ["TopOpeBRep", "TopOpeBRepDS", "TopOpeBRepBuild", "TopOpeBRepTool", "BRepAlgo", "BRepFill", "BRepProj"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKBool" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _area(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.SurfaceProperties_s(shape, props)
    return props.Mass()


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def _square(z: float) -> TopoDS.TopoDS_Wire:
    return BRepBuilderAPI.BRepBuilderAPI_MakePolygon(gp.gp_Pnt(0, 0, z), gp.gp_Pnt(1, 0, z), gp.gp_Pnt(1, 1, z), gp.gp_Pnt(0, 1, z), True).Wire()


def test_fill_loft_and_pipes():
    shell = BRepFill.BRepFill.Shell_s(_square(0), _square(2))              # ruled loft between two wires
    assert _area(shell) == pytest.approx(8.0) and sum(1 for _ in TopExp.TopExp_Explorer(shell, TopAbs.TopAbs_FACE)) == 4
    e1 = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(1, 0, 0)).Edge()
    e2 = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Pnt(0, 0, 1), gp.gp_Pnt(1, 0, 1)).Edge()
    assert _area(BRepFill.BRepFill.Face_s(e1, e2)) == pytest.approx(1.0)
    spine = BRepBuilderAPI.BRepBuilderAPI_MakeWire(BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(0, 0, 5)).Edge()).Wire()
    circle = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Circ(gp.gp_Ax2(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1)), 1.0)).Edge()
    profile = BRepBuilderAPI.BRepBuilderAPI_MakeWire(circle).Wire()
    pipe = BRepFill.BRepFill_Pipe(spine, profile)
    assert _area(pipe.Shape()) == pytest.approx(2 * math.pi * 5, rel=1e-6)
    shell = BRepFill.BRepFill_PipeShell(spine)                            # Transient, handle-managed
    shell.Add(profile)
    shell.Build()
    assert shell.MakeSolid() and _volume(shell.Shape()) == pytest.approx(math.pi * 5, rel=1e-6)
    assert BRepAlgo.BRepAlgo.IsValid_s(pipe.Shape())
    joined = BRepAlgo.BRepAlgo.ConcatenateWire_s(_square(0), GeomAbs.GeomAbs_C1, 1e-3)
    assert sum(1 for _ in TopExp.TopExp_Explorer(joined, TopAbs.TopAbs_EDGE)) == 4


def test_projection_is_an_iterator():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape()
    proj = BRepProj.BRepProj_Projection(_square(0), box, gp.gp_Dir(0, 0, 1))
    assert proj.IsDone()
    wires = list(proj)                                                     # R-ITER (More/Next/Current)
    assert len(wires) == 3 and all(w.ShapeType() == TopAbs.TopAbs_WIRE for w in wires)


def test_topopebrep_free_functions_and_iterator_typedef():
    # the old kernel's helpers are package-level free functions (FUN_*, FDS_*, FC2D_*)
    assert len([n for n in dir(TopOpeBRepTool) if n.startswith("FUN_")]) == 70
    assert TopOpeBRepDS.TopOpeBRepDS_DataStructure().NbShapes() == 0
    assert TopOpeBRepDS.TopOpeBRepDS_FACE is TopOpeBRepDS.TopOpeBRepDS_Kind.TopOpeBRepDS_FACE
    # NCollection_TListIterator<TopoDS_Shape> in a signature is NCollection_List<TopoDS_Shape>::Iterator (bound by the List binder)
    hds = TopOpeBRepDS.TopOpeBRepDS_HDataStructure()
    it = hds.SameDomain(BRepPrimAPI.BRepPrimAPI_MakeBox(1, 1, 1).Shape())
    assert type(it) is NCollection.NCollection_List__TopoDS_Shape.Iterator and it.More() is False
    assert "-> nanoocp.NCollection.NCollection_List__TopoDS_Shape.Iterator" in TopOpeBRepDS.TopOpeBRepDS_HDataStructure.SameDomain.__doc__
    assert not hasattr(TopOpeBRepDS, "NCollection_TListIterator__TopoDS_Shape")
    # R-COLLISION on free functions with out-parameters
    assert hasattr(TopOpeBRepTool, "FUN_tool_closedS__bool__float__bool__float") and hasattr(TopOpeBRepTool, "FUN_tool_closedS__bool__float__float")


def test_undefined_free_functions_are_skipped():
    # R-UNDEFINED now covers free functions: FUN_scanloi and FDSSDM_s1s2makesordor are declared in TopOpeBRepDS headers without a
    # definition in libTKBool (the extension failed to link before)
    assert not hasattr(TopOpeBRepDS, "FUN_scanloi") and not hasattr(TopOpeBRepDS, "FDSSDM_s1s2makesordor")
    rows = read_report(REPORT)
    assert all(cat != "misc" for cat, _, _ in rows)
    undefined = [msg for cat, _, msg in rows if cat == "undefined"]
    assert any(m.startswith("FUN_scanloi(") and m.endswith("declared in the header, no definition in libTKBool") for m in undefined)
    assert any(m.startswith("FDSSDM_s1s2makesordor(") for m in undefined)
