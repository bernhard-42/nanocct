"""Generated bindings for TKXml (ApplicationFramework: XmlDrivers, XmlMDataXtd, XmlMNaming): the full XmlOcaf format --
documents with shapes (TNaming) and TDataXtd attributes as XML bytes. Completes the ApplicationFramework subset that
DataExchange links."""
import importlib
import io
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from nanoocp import PCDM, TDataStd, TDataXtd, TDocStd, TNaming, XmlDrivers, XmlMDF, gp
from nanoocp.BRepGProp import BRepGProp
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.GProp import GProp_GProps
from nanoocp.TCollection import TCollection_ExtendedString
from nanoocp.TopAbs import TopAbs_SOLID

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKXml" / "report.txt"


@pytest.mark.parametrize("pkg", ["XmlDrivers", "XmlMDataXtd", "XmlMNaming"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


@pytest.fixture
def app():
    app = TDocStd.TDocStd_Application()
    XmlDrivers.XmlDrivers.DefineFormat(app)                  # XmlOcaf
    return app


def _document(app):
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("XmlOcaf"))
    label = doc.Main().FindChild(1, True)
    TNaming.TNaming_Builder(label).Generated(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    TDataStd.TDataStd_Name.Set_s(label, TCollection_ExtendedString("box"))
    TDataXtd.TDataXtd_Point.Set(doc.Main().FindChild(2, True), gp.gp_Pnt(1.0, 2.0, 3.0))
    return doc


def test_document_with_a_shape_round_trips_as_xml(app):
    doc = _document(app)
    status, data = app.SaveAs(doc)
    assert status == PCDM.PCDM_SS_OK and isinstance(data, bytes)
    root = ET.fromstring(data)
    assert root.attrib["format"] == "XmlOcaf"
    assert [child.tag.split("}")[-1] for child in root] == ["info", "comments", "label", "shapes"]   # the shape section
    status, again = app.Open(io.BytesIO(data))
    assert status == PCDM.PCDM_RS_OK
    label = again.Main().FindChild(1)
    named = label.FindAttribute(TNaming.TNaming_NamedShape.GetID())[1]
    assert named.Get().ShapeType() == TopAbs_SOLID
    props = GProp_GProps()
    BRepGProp.VolumeProperties(named.Get(), props)
    assert props.Mass() == pytest.approx(6.0)
    assert label.FindAttribute(TDataStd.TDataStd_Name.GetID())[1].Get().ToExtString() == "box"
    point = gp.gp_Pnt()
    assert TDataXtd.TDataXtd_Geometry.Point(again.Main().FindChild(2), point) and point.X() == 1.0


def test_file_form(app, tmp_path):
    doc = _document(app)
    path = tmp_path / "doc.xml"                              # the XmlOcaf extension
    assert app.SaveAs(doc, TCollection_ExtendedString(str(path))) == PCDM.PCDM_SS_OK
    assert path.read_bytes() == app.SaveAs(doc)[1]
    assert PCDM.PCDM_ReadWriter.FileFormat(io.BytesIO(path.read_bytes()))[0].ToExtString() == "XmlOcaf"
    other = TDocStd.TDocStd_Application()
    XmlDrivers.XmlDrivers.DefineFormat(other)
    status, again = other.Open(TCollection_ExtendedString(str(path)))
    assert status == PCDM.PCDM_RS_OK and again.Main().FindChild(1).IsAttribute(TNaming.TNaming_NamedShape.GetID())


def test_drivers(app):
    assert type(XmlDrivers.XmlDrivers.AttributeDrivers(None)) is XmlMDF.XmlMDF_ADriverTable
    driver = XmlDrivers.XmlDrivers_DocumentStorageDriver(TCollection_ExtendedString("nanoOCP test"))
    data = driver.Write(_document(app))                      # Write(doc, ostream&, range) -> bytes
    assert driver.GetStoreStatus() == PCDM.PCDM_SS_OK and b"nanoOCP test" in data


def test_report_has_only_the_const_twin():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert len(lines) == 1 and lines[0].startswith("overload-collision\tXmlMNaming\tXmlMNaming_Shape1::Element() const")
