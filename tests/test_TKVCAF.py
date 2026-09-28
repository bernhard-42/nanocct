"""Generated bindings for TKVCAF (ApplicationFramework: TPrsStd): AIS presentations of OCAF attributes -- the driver table
that turns a label into an AIS object, the viewer attribute, the presentation attribute with its own colour/mode. Nothing is
displayed: without a graphic driver (TKOpenGl, roadmap 8.6a) AIS_InteractiveContext::Display segfaults inside
Graphic3d_Structure's constructor (checked), in C++ as in Python."""
import importlib
from pathlib import Path

from nanocct import AIS, Quantity, TDataXtd, TDocStd, TNaming, TPrsStd, V3d, gp
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.TCollection import TCollection_ExtendedString

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKVCAF" / "report.txt"


def test_package_imports():
    assert importlib.import_module("nanocct.TPrsStd").__name__ == "nanocct.TPrsStd"


def _document():
    app = TDocStd.TDocStd_Application()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinOcaf"))
    label = doc.Main().FindChild(1, True)
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    TNaming.TNaming_Builder(label).Generated(box)
    return doc, label, box


def test_driver_table_builds_ais_objects_from_labels():
    """TPrsStd_Driver::Update(label, handle<AIS_InteractiveObject>&) -> (ok, ais) (R-OUT-HANDLE), downcast to the AIS class
    the driver creates."""
    doc, label, box = _document()
    table = TPrsStd.TPrsStd_DriverTable.Get_s()
    found, driver = table.FindDriver(TNaming.TNaming_NamedShape.GetID_s())
    assert found is True and type(driver) is TPrsStd.TPrsStd_NamedShapeDriver
    ok, ais = driver.Update(label)
    assert ok is True and type(ais) is AIS.AIS_Shape and ais.Shape().IsSame(box)
    point_label = doc.Main().FindChild(2, True)
    TDataXtd.TDataXtd_Point.Set_s(point_label, gp.gp_Pnt(1.0, 2.0, 3.0))
    ok, ais = table.FindDriver(TDataXtd.TDataXtd_Point.GetID_s())[1].Update(point_label)
    assert ok is True and type(ais) is AIS.AIS_Point


def test_viewer_attribute_and_typed_find_overloads():
    """TPrsStd_AISViewer::Find(label, handle<X>&) exists for three X: every overload carries its result type as the suffix
    (R-COLLISION), none keeps the plain name."""
    doc, label, _ = _document()
    context = AIS.AIS_InteractiveContext(V3d.V3d_Viewer(None))
    viewer = TPrsStd.TPrsStd_AISViewer.New_s(doc.Main(), context)
    assert viewer.GetInteractiveContext() is context
    assert TPrsStd.TPrsStd_AISViewer.Has_s(label) is True
    found, found_context = TPrsStd.TPrsStd_AISViewer.Find_s__AIS_InteractiveContext(label)
    assert found is True and found_context is context
    assert type(TPrsStd.TPrsStd_AISViewer.Find_s__TPrsStd_AISViewer(label)[1]) is TPrsStd.TPrsStd_AISViewer
    assert type(TPrsStd.TPrsStd_AISViewer.Find_s__V3d_Viewer(label)[1]) is V3d.V3d_Viewer
    assert not hasattr(TPrsStd.TPrsStd_AISViewer, "Find")


def test_presentation_attribute_without_display():
    doc, label, _ = _document()
    TPrsStd.TPrsStd_AISViewer.New_s(doc.Main(), AIS.AIS_InteractiveContext(V3d.V3d_Viewer(None)))
    pres = TPrsStd.TPrsStd_AISPresentation.Set_s(label, TNaming.TNaming_NamedShape.GetID_s())
    assert pres.GetDriverGUID() == TNaming.TNaming_NamedShape.GetID_s()
    assert pres.IsDisplayed() is False and pres.HasOwnColor() is False
    pres.SetColor(Quantity.Quantity_NOC_RED)
    assert pres.HasOwnColor() is True and pres.Color() == Quantity.Quantity_NOC_RED and pres.Transparency() == 0.0
    found, again = label.FindAttribute(TPrsStd.TPrsStd_AISPresentation.GetID_s())
    assert found is True and type(again) is TPrsStd.TPrsStd_AISPresentation
    TPrsStd.TPrsStd_AISPresentation.Unset_s(label)
    assert label.IsAttribute(TPrsStd.TPrsStd_AISPresentation.GetID_s()) is False


def test_report_has_only_the_expected_omissions():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert {line.split("\t")[0] for line in lines} == {"overload-collision"}
    # the deprecated out-param twins of TPrsStd_ConstraintTools::Compute*(constraint) carry the typed suffix; the modern
    # by-value overload keeps the name
    assert "ComputeDistance_s" in dir(TPrsStd.TPrsStd_ConstraintTools) and "ComputeDistance_s__AIS_InteractiveObject" in dir(TPrsStd.TPrsStd_ConstraintTools)
