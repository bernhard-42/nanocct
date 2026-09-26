"""Generated bindings for TKOffset: BRepOffsetAPI (thick solids, offset shapes, ThruSections lofts, pipes, 2D wire offsets, draft
angles). BRepOffsetAPI_ThruSections holds a NCollection_Handle<BRepFill_Generator> (pointer-like, pointee incomplete in the header):
R-INCOMPLETE now exempts it like handle/unique_ptr."""
import importlib
import math
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import BRepBuilderAPI, BRepCheck, BRepGProp, BRepOffset, BRepOffsetAPI, BRepPrimAPI, Draft, GProp, GeomAbs, NCollection, TopAbs, TopExp, TopoDS, gp

PACKAGES = ["BRepOffsetAPI", "Draft", "BRepOffset", "BiTgte"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKOffset" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def _square(z: float, half: float) -> TopoDS.TopoDS_Wire:
    c = 5.0
    return BRepBuilderAPI.BRepBuilderAPI_MakePolygon(gp.gp_Pnt(c - half, c - half, z), gp.gp_Pnt(c + half, c - half, z),
                                                     gp.gp_Pnt(c + half, c + half, z), gp.gp_Pnt(c - half, c + half, z), True).Wire()


def test_thick_solid_offset_and_draft():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(10, 10, 10).Shape()
    faces = NCollection.NCollection_List[TopoDS.TopoDS_Shape]()
    faces.Append([f for f in TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE)][5])            # the top face
    thick = BRepOffsetAPI.BRepOffsetAPI_MakeThickSolid()
    thick.MakeThickSolidByJoin(box, faces, -1.0, 1e-3, BRepOffset.BRepOffset_Skin, False, False, GeomAbs.GeomAbs_Arc)
    assert thick.IsDone() and _volume(thick.Shape()) == pytest.approx(1000 - 8 * 8 * 9) and BRepCheck.BRepCheck_Analyzer(thick.Shape()).IsValid()
    offset = BRepOffsetAPI.BRepOffsetAPI_MakeOffsetShape()
    offset.PerformByJoin(box, 1.0, 1e-3)
    assert 12 ** 3 > _volume(offset.Shape()) > 1000                          # rounded edges (GeomAbs_Arc join)
    draft = BRepOffsetAPI.BRepOffsetAPI_DraftAngle(box)
    face = TopoDS.Face(next(iter(TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE))))
    draft.Add(face, gp.gp_Dir(0, 0, 1), math.radians(5), gp.gp_Pln(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1)))
    assert draft.AddDone() and draft.Status() == Draft.Draft_NoError


def test_loft_pipe_and_wire_offset():
    loft = BRepOffsetAPI.BRepOffsetAPI_ThruSections(True, True)              # solid, ruled
    loft.AddWire(_square(0, 5))
    loft.AddWire(_square(5, 3))
    loft.Build()
    assert loft.IsDone() and _volume(loft.Shape()) == pytest.approx(5 * (100 + 36 + 60) / 3)     # frustum of a pyramid
    spine = BRepBuilderAPI.BRepBuilderAPI_MakeWire(BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Pnt(5, 5, 0), gp.gp_Pnt(5, 5, 5)).Edge()).Wire()
    pipe = BRepOffsetAPI.BRepOffsetAPI_MakePipe(spine, BRepBuilderAPI.BRepBuilderAPI_MakeFace(_square(0, 5), True).Face())
    assert _volume(pipe.Shape()) == pytest.approx(500.0)
    offset = BRepOffsetAPI.BRepOffsetAPI_MakeOffset(_square(0, 5))
    offset.Perform(1.0)
    assert sum(1 for _ in TopExp.TopExp_Explorer(offset.Shape(), TopAbs.TopAbs_EDGE)) == 8   # 4 lines + 4 arcs
    rows = read_report(REPORT)
    # every row is an R-UNDEFINED skip; how many depends on what the platform's libTKOffset exports (macOS 2, Windows 3)
    assert all(cat != "misc" for cat, _, _ in rows) and all(cat == "undefined" for cat, _, _ in rows)
    assert len(rows) >= 2


def test_optional_pointer_parameters_are_dropped():
    # R-OPTIONAL-PTR: BRepFill_AdvancedEvolved::IsDone(unsigned int* theErrorCode = 0) had no binding at all before
    from nanoocp import BRepFill
    assert BRepFill.BRepFill_AdvancedEvolved().IsDone() is False
    assert "IsDone(self) -> bool" in BRepFill.BRepFill_AdvancedEvolved.IsDone.__doc__
