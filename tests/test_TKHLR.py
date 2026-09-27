"""Generated bindings for TKHLR: hidden-line removal (HLRBRep_Algo + HLRBRep_HLRToShape), Contap, Intrv. New with this toolkit:
R-PRELUDE applied to the emitted include list (an extra header may not be self-contained), and 6c instantiations with a raw
pointer as template argument stay out (HLRBRep's Extrema/LProp instantiations over void*)."""
import importlib
from pathlib import Path

import pytest

from generator.report import read_report
from OCP3x import BRepPrimAPI, HLRAlgo, HLRBRep, HLRTopoBRep, Intrv, TopAbs, TopExp, gp

PACKAGES = ["HLRTopoBRep", "HLRBRep", "HLRAlgo", "HLRAppli", "Intrv", "TopBas", "TopCnx", "Contap"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKHLR" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


def test_hidden_line_removal_of_a_box():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
    algo = HLRBRep.HLRBRep_Algo()                                   # Transient
    algo.Add(box)
    algo.Projector(HLRAlgo.HLRAlgo_Projector(gp.gp_Ax2(gp.gp_Pnt(5, -5, 5), gp.gp_Dir(-1, 1, -1))))
    algo.Update()
    algo.Hide()
    to_shape = HLRBRep.HLRBRep_HLRToShape(algo)
    visible = sum(1 for _ in TopExp.TopExp_Explorer(to_shape.VCompound(), TopAbs.TopAbs_EDGE))
    hidden = sum(1 for _ in TopExp.TopExp_Explorer(to_shape.HCompound(), TopAbs.TopAbs_EDGE))
    assert (visible, hidden) == (9, 3)
    assert Intrv.Intrv_Interval(0.0, 1.0).Start() == 0.0


def test_pointer_template_arguments_and_include_prelude():
    rows = read_report(REPORT)
    assert all(cat != "misc" for cat, _, _ in rows)
    msgs = [msg for _, _, msg in rows]
    # HLRBRep_CLProps = GeomLProp_CLPropsBase<..., const HLRBRep_Curve*, ...>, HLRBRep_SLProps over void*: not bound, reported
    assert not hasattr(HLRBRep, "HLRBRep_CLProps") and not hasattr(HLRBRep, "HLRBRep_SLProps")
    assert any(m.startswith("HLRBRep_SLProps = GeomLProp_SLPropsBase<HLRBRep_SurfacePtr, ") and m.endswith("template argument void * is a raw pointer -> not bound") for m in msgs)
    # HLRTopoBRep.cpp includes Contap_Contour.hxx, whose Contap_Line.hxx names handle<Adaptor2d_Curve2d> without declaring it
    assert ("header", "HLRTopoBRep", "HLRTopoBRep: extra headers not self-contained, Adaptor2d_Curve2d.hxx included first") in rows
    cpp = (REPORT.parent / "HLRTopoBRep.cpp").read_text()
    assert cpp.index("#include <Adaptor2d_Curve2d.hxx>") < cpp.index("#include <Contap_Contour.hxx>")
