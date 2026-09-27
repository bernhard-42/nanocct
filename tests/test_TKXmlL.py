"""Generated bindings for TKXmlL (ApplicationFramework: XmlLDrivers, XmlMDF, XmlMDataStd, XmlMDocStd, XmlMFunction,
XmlObjMgt): the XML OCAF format. Its document streams are bytes like the binary ones (overrides.toml [stream]
binary_packages): the drivers override PCDM_Writer/Reader virtuals that already take bytes/BinaryIO, and a serialised XML
document is a byte sequence with an encoding declaration."""
import importlib
import io
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from OCP3x import PCDM, TDataStd, TDocStd, XmlLDrivers, XmlMDF, XmlObjMgt
from OCP3x.TCollection import TCollection_ExtendedString

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKXmlL" / "report.txt"


@pytest.mark.parametrize("pkg", ["XmlLDrivers", "XmlMDF", "XmlMDataStd", "XmlMDocStd", "XmlMFunction", "XmlObjMgt"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


@pytest.fixture
def app():
    app = TDocStd.TDocStd_Application()
    XmlLDrivers.XmlLDrivers.DefineFormat_s(app)                 # XmlLOcaf
    return app


def _document(app):
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("XmlLOcaf"))
    label = doc.Main().FindChild(1, True)
    TDataStd.TDataStd_Name.Set_s(label, TCollection_ExtendedString("pärt", True))   # True: the str is UTF-8 (OCCT's default copies bytes)
    TDataStd.TDataStd_Integer.Set_s(label, 42)
    TDataStd.TDataStd_Real.Set_s(label, 2.5)
    return doc


def test_xml_document_round_trips_through_bytes(app):
    doc = _document(app)
    status, data = app.SaveAs(doc)
    assert status == PCDM.PCDM_SS_OK and isinstance(data, bytes)
    assert data.startswith(b'<?xml version="1.0" encoding="UTF-8"?>')
    root = ET.fromstring(data)                                # a serialised XML document is bytes; etree accepts it as such
    assert root.tag == "{http://www.opencascade.org/OCAF/XML}document" and root.attrib["format"] == "XmlLOcaf"
    status, again = app.Open(io.BytesIO(data))
    assert status == PCDM.PCDM_RS_OK
    label = again.Main().FindChild(1)
    assert label.FindAttribute(TDataStd.TDataStd_Name.GetID_s())[1].Get().ToExtString() == "pärt"
    assert label.FindAttribute(TDataStd.TDataStd_Integer.GetID_s())[1].Get() == 42
    assert label.FindAttribute(TDataStd.TDataStd_Real.GetID_s())[1].Get() == 2.5


def test_xml_file_form_and_format_detection(app, tmp_path):
    doc = _document(app)
    path = tmp_path / "doc.xmll"                              # the XmlLOcaf extension (XmlLDrivers.cxx:95); another one is appended
    assert app.SaveAs(doc, TCollection_ExtendedString(str(path))) == PCDM.PCDM_SS_OK
    assert path.read_bytes() == app.SaveAs(doc)[1]
    assert PCDM.PCDM_ReadWriter.FileFormat_s(io.BytesIO(path.read_bytes()))[0].ToExtString() == "XmlLOcaf"
    other = TDocStd.TDocStd_Application()
    XmlLDrivers.XmlLDrivers.DefineFormat_s(other)
    status, again = other.Open(TCollection_ExtendedString(str(path)))
    assert status == PCDM.PCDM_RS_OK and again.Main().FindChild(1).FindAttribute(TDataStd.TDataStd_Integer.GetID_s())[1].Get() == 42


def test_storage_driver_writes_bytes_directly(app):
    doc = _document(app)
    driver = XmlLDrivers.XmlLDrivers_DocumentStorageDriver(TCollection_ExtendedString("OCP3x test"))
    data = driver.Write(doc)                                  # Write(doc, ostream&, range) -> bytes, like the app-level SaveAs
    assert isinstance(data, bytes) and driver.GetStoreStatus() == PCDM.PCDM_SS_OK
    assert b"OCP3x test" in data                            # the copyright goes into the info section
    assert type(XmlLDrivers.XmlLDrivers.AttributeDrivers_s(None)) is XmlMDF.XmlMDF_ADriverTable


def test_relocation_tables_derive_from_the_containers():
    assert XmlObjMgt.XmlObjMgt_RRelocationTable().IsEmpty()                  # NCollection_DataMap[int, Standard_Transient]
    assert XmlObjMgt.XmlObjMgt_SRelocationTable().IsEmpty()                  # NCollection_IndexedMap[Standard_Transient]


def test_report_has_only_the_expected_omissions():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert {line.split("\t")[0] for line in lines} == {"overload-collision", "raw-pointer"}
    assert all("XmlObjMgt" in line for line in lines)        # GetInteger/GetReal(const char*&): the drivers' string scanners
