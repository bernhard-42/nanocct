"""Generated bindings for TKBin (ApplicationFramework: BinDrivers, BinMDataXtd, BinMNaming): the full BinOcaf format --
documents with shapes (TNaming) and TDataXtd attributes saved to bytes and reloaded. The three packages are binary-stream
packages (overrides.toml [stream] binary_packages)."""
import importlib
import io
from pathlib import Path

import pytest

from OCP3x import BinDrivers, BinMDF, BinMNaming, PCDM, TDataStd, TDataXtd, TDocStd, TNaming, gp
from OCP3x.BRepGProp import BRepGProp
from OCP3x.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCP3x.GProp import GProp_GProps
from OCP3x.TCollection import TCollection_ExtendedString
from OCP3x.TopAbs import TopAbs_SOLID

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKBin" / "report.txt"


@pytest.mark.parametrize("pkg", ["BinDrivers", "BinMDataXtd", "BinMNaming"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


@pytest.fixture
def app():
    app = TDocStd.TDocStd_Application()
    BinDrivers.BinDrivers.DefineFormat_s(app)                 # BinOcaf, without resource files
    return app


def _document(app):
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinOcaf"))
    label = doc.Main().FindChild(1, True)
    TNaming.TNaming_Builder(label).Generated(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    TDataStd.TDataStd_Name.Set_s(label, TCollection_ExtendedString("box"))
    TDataXtd.TDataXtd_Point.Set_s(doc.Main().FindChild(2, True), gp.gp_Pnt(1.0, 2.0, 3.0))
    return doc


def test_document_with_a_shape_round_trips_through_bytes(app):
    doc = _document(app)
    status, data = app.SaveAs(doc)
    assert status == PCDM.PCDM_SS_OK and data.startswith(b"BINFILE") and len(data) > 3000
    status, again = app.Open(io.BytesIO(data))
    assert status == PCDM.PCDM_RS_OK
    label = again.Main().FindChild(1)
    found, named = label.FindAttribute(TNaming.TNaming_NamedShape.GetID_s())
    assert found and named.Get().ShapeType() == TopAbs_SOLID
    props = GProp_GProps()
    BRepGProp.VolumeProperties_s(named.Get(), props)
    assert props.Mass() == pytest.approx(6.0)
    assert label.FindAttribute(TDataStd.TDataStd_Name.GetID_s())[1].Get().ToExtString() == "box"
    point = gp.gp_Pnt()
    assert TDataXtd.TDataXtd_Geometry.Point_s(again.Main().FindChild(2), point) and (point.X(), point.Y(), point.Z()) == (1.0, 2.0, 3.0)


def test_file_form_and_binlocaf_reader_compatibility(app, tmp_path):
    doc = _document(app)
    path = tmp_path / "doc.cbf"
    assert app.SaveAs(doc, TCollection_ExtendedString(str(path))) == PCDM.PCDM_SS_OK
    assert path.read_bytes() == app.SaveAs(doc)[1]
    other = TDocStd.TDocStd_Application()
    BinDrivers.BinDrivers.DefineFormat_s(other)
    status, again = other.Open(TCollection_ExtendedString(str(path)))
    assert status == PCDM.PCDM_RS_OK and again.Main().FindChild(1).IsAttribute(TNaming.TNaming_NamedShape.GetID_s())


def test_storage_driver_options_and_named_shape_driver():
    driver = BinDrivers.BinDrivers_DocumentStorageDriver()
    assert driver.IsWithTriangles() is False and driver.IsWithNormals() is False
    driver.SetWithTriangles(None, True)                     # handle<Message_Messenger>& first
    assert driver.IsWithTriangles() is True
    table = BinDrivers.BinDrivers.AttributeDrivers_s(None)
    assert type(table) is BinMDF.BinMDF_ADriverTable
    type_id, named_driver = table.GetDriver(TNaming.TNaming_NamedShape().DynamicType())   # GetDriver(type, handle&) -> (id, driver)
    assert type_id == 0 and type(named_driver) is BinMNaming.BinMNaming_NamedShapeDriver
    assert named_driver.IsWithTriangles() is False


def test_report_is_empty():
    assert [line for line in REPORT.read_text().splitlines() if not line.startswith("#")] == []
