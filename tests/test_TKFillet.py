"""Generated bindings for TKFillet: BRepFilletAPI_MakeFillet/MakeChamfer, ChFi2d, the Blend* function classes. Predictions from
Design.md 9 confirmed: ChFiKPart needs ChFiDS_ChamfMode.hxx as prelude (R-PRELUDE); `using Blend_FuncInv::Set` un-hides the base
overload next to the derived class's own (R-USING)."""
import importlib
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import Blend, BlendFunc, BRepBuilderAPI, BRepCheck, BRepFilletAPI, BRepGProp, BRepPrimAPI, ChFi2d, ChFiDS, GProp, TopAbs, TopExp, TopoDS, gp

PACKAGES = ["ChFiDS", "ChFi2d", "ChFi3d", "ChFiKPart", "Blend", "BRepBlend", "BlendFunc", "BRepFilletAPI", "FilletSurf"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKFillet" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties(shape, props)
    return props.Mass()


def test_fillet_and_chamfer_of_a_cube():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(10, 10, 10).Shape()
    fillet = BRepFilletAPI.BRepFilletAPI_MakeFillet(box)
    for e in TopExp.TopExp_Explorer(box, TopAbs.TopAbs_EDGE):
        fillet.Add(1.0, TopoDS.Edge(e))
    fillet.Build()
    assert fillet.IsDone() and fillet.NbContours() == 12
    shape = fillet.Shape()
    assert sum(1 for _ in TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_FACE)) == 26 and BRepCheck.BRepCheck_Analyzer(shape).IsValid()
    assert 970 < _volume(shape) < 980                                  # 12 edge fillets + 8 corner patches
    chamfer = BRepFilletAPI.BRepFilletAPI_MakeChamfer(box)
    for e in TopExp.TopExp_Explorer(box, TopAbs.TopAbs_EDGE):
        chamfer.Add(1.0, TopoDS.Edge(e))
    chamfer.Build()
    assert chamfer.IsDone() and sum(1 for _ in TopExp.TopExp_Explorer(chamfer.Shape(), TopAbs.TopAbs_FACE)) == 26
    assert _volume(chamfer.Shape()) == pytest.approx(945.3333, rel=1e-4)
    assert [e.name for e in ChFiDS.ChFiDS_ChamfMode] == ["ChFiDS_ClassicChamfer", "ChFiDS_ConstThroatChamfer", "ChFiDS_ConstThroatWithPenetrationChamfer"]
    wire = BRepBuilderAPI.BRepBuilderAPI_MakePolygon(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(10, 0, 0), gp.gp_Pnt(10, 10, 0), gp.gp_Pnt(0, 10, 0), True).Wire()
    builder = ChFi2d.ChFi2d_Builder(BRepBuilderAPI.BRepBuilderAPI_MakeFace(wire, True).Face())
    assert builder.Status() == ChFi2d.ChFi2d_Ready


def test_using_unhides_base_overloads_and_prelude():
    # R-USING: BlendFunc_ConstRadInv declares Set(R, Choix) and `using Blend_FuncInv::Set` for Set(OnFirst, COnSurf)
    sigs = [l for l in BlendFunc.BlendFunc_ConstRadInv.Set.__doc__.splitlines() if l.startswith("Set(")]
    assert sigs == ["Set(self, OnFirst: bool, COnSurf: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None", "Set(self, R: float, Choix: int) -> None"]
    assert [l for l in Blend.Blend_FuncInv.Set.__doc__.splitlines() if l.startswith("Set(")] == sigs[:1]
    rows = read_report(REPORT)
    assert all(cat != "misc" for cat, _, _ in rows)
    assert ("header", "ChFiKPart", "ChFiKPart: headers not self-contained, parsed with <ChFiDS_ChamfMode.hxx> included first") in rows
    assert any(msg.startswith("BlendFunc::Knots(const BlendFunc_SectionShape, NCollection_Array1<double> &): declared in the header") for _, _, msg in rows)
