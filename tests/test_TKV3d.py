"""Generated bindings for TKV3d (Visualization: AIS, Prs3d, V3d, SelectMgr, StdPrs, PrsDim, …): the text-to-BRep path build123d
uses (StdPrs_BRepFont + StdPrs_BRepTextBuilder), CadQuery's Prs3d_Drawer call, AIS objects and a viewer/context without a
graphic driver (there is no TKOpenGl yet, Design.md 2). The whole toolkit compiled without a new generator rule."""
import importlib
from pathlib import Path

import pytest

from nanoocp import AIS, Aspect, BRepBndLib, BRepGProp, BRepPrimAPI, Bnd, Font, GProp, Graphic3d, Prs3d, PrsDim, Quantity, SelectMgr, StdPrs, TopAbs, TopExp, TopoDS, V3d, gp
from nanoocp.NCollection import NCollection_String
from nanoocp.TCollection import TCollection_AsciiString

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKV3d" / "report.txt"


@pytest.mark.parametrize("pkg", ["V3d", "Select3D", "Prs3d", "StdPrs", "SelectBasics", "SelectMgr", "PrsMgr", "AIS", "StdSelect", "DsgPrs", "PrsDim"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _bbox(shape):
    box = Bnd.Bnd_Box()
    BRepBndLib.BRepBndLib.Add_s(shape, box)
    l = box.Get()
    return l.Xmin, l.Ymin, l.Xmax, l.Ymax


def test_text_to_brep_like_build123d():
    """composite.py: StdPrs_BRepFont(NCollection_String(name), aspect, size) + Font_BRepTextBuilder().Perform(font, text, ax3, hta, vta)."""
    font = StdPrs.StdPrs_BRepFont(NCollection_String("Helvetica"), Font.Font_FA_Bold, 10.0)
    assert font.FTFont().IsValid() and font.Ascender() > 0 and font.PointSize() > 0
    builder = StdPrs.StdPrs_BRepTextBuilder()
    shape = builder.Perform(font, NCollection_String("Hi"), gp.gp_Ax3(), Graphic3d.Graphic3d_HTA_LEFT, Graphic3d.Graphic3d_VTA_BOTTOM)
    comp = TopoDS.Compound(shape)
    assert sum(1 for _ in TopExp.TopExp_Explorer(comp, TopAbs.TopAbs_FACE)) == 3          # H, the i stem, the i dot
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.SurfaceProperties_s(comp, props)
    assert 20 < props.Mass() < 60
    xmin, ymin, xmax, ymax = _bbox(comp)
    assert xmin >= 0 and ymin == pytest.approx(0, abs=1e-6) and 5 < ymax < 10 and xmax > 5       # bottom-left aligned, ~10 units high
    centered = builder.Perform(font, NCollection_String("Hi"), gp.gp_Ax3(), Graphic3d.Graphic3d_HTA_CENTER, Graphic3d.Graphic3d_VTA_CENTER)
    cxmin, cymin, cxmax, cymax = _bbox(centered)
    assert cxmin < 0 < cxmax and cymin < 0 < cymax and cxmax - cxmin == pytest.approx(xmax - xmin, abs=1e-6)
    single = StdPrs.StdPrs_BRepFont.FindAndCreate_s(TCollection_AsciiString("Helvetica"), Font.Font_FA_Regular, 5.0)
    assert single is not None and single.PointSize() == pytest.approx(font.PointSize() / 2, rel=1e-6)
    single.SetCompositeCurveMode(False)                                                          # build123d's single-stroke branch


def test_drawer_iso_aspect_like_cadquery():
    drawer = Prs3d.Prs3d_Drawer()
    drawer.SetUIsoAspect(Prs3d.Prs3d_IsoAspect(Quantity.Quantity_Color(), Aspect.Aspect_TOL_SOLID, 1, 0))     # shapes.py:1719
    assert drawer.UIsoAspect().Number() == 0 and drawer.HasOwnUIsoAspect()
    drawer.SetMaximalChordialDeviation(0.01)
    assert drawer.MaximalChordialDeviation() == 0.01 and drawer.HasOwnMaximalChordialDeviation()


def test_ais_objects_dimensions_and_a_driverless_viewer():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
    shp = AIS.AIS_Shape(box)
    assert shp.Shape().IsSame(box) and shp.Type() == AIS.AIS_KindOfInteractive_Shape and not shp.HasColor()
    shp.SetColor(Quantity.Quantity_Color(Quantity.Quantity_NOC_RED))
    color = Quantity.Quantity_Color()
    shp.Color(color)                                                          # Quantity_Color& filled in place (R-REF-CLASS)
    assert shp.HasColor() and color.Name() == Quantity.Quantity_NOC_RED
    dim = PrsDim.PrsDim_LengthDimension(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(3, 0, 0), gp.gp_Pln(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1)))
    assert dim.GetValue() == 3.0 and dim.IsValid()
    viewer = V3d.V3d_Viewer(None)                                             # handle<Graphic3d_GraphicDriver> = None: no driver yet
    assert viewer.DefaultViewSize() == 1000.0 and viewer.DefaultBackgroundColor().Name() == Quantity.Quantity_NOC_GRAY30
    ctx = AIS.AIS_InteractiveContext(viewer)
    assert ctx.NbSelected() == 0 and ctx.CurrentViewer() is not None
    sel = SelectMgr.SelectMgr_Selection(1)
    assert sel.Mode() == 1 and sel.Sensitivity() == 2
    assert isinstance(SelectMgr.SelectMgr_RectangularFrustum(), SelectMgr.SelectMgr_Frustum__4)       # R-TEMPLATE-BASE


def test_report_is_small_and_known():
    lines = [l for l in REPORT.read_text().splitlines() if not l.startswith("#")]
    cats = {l.split("\t")[0] for l in lines}
    assert "misc" not in cats and len(lines) < 60
    assert any(l.startswith("raw-pointer\tV3d\tV3d_CircularGrid::V3d_CircularGrid(): param 'aViewer': reference to pointer") for l in lines)
    assert any(l.startswith("template\tPrs3d\tPrs3d_Point: template (not bound)") for l in lines)
