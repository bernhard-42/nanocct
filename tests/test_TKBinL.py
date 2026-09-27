"""Generated bindings for TKBinL (ApplicationFramework: BinLDrivers, BinMDF, BinMDataStd, BinMDocStd, BinMFunction,
BinObjMgt): the binary OCAF format. The whole toolkit is a binary-stream toolkit (overrides.toml [stream] binary_packages):
TDocStd_Application.SaveAs(doc) gives the file's bytes, Open(io.BytesIO(...)) reads them back."""
import importlib
import io
from pathlib import Path

import pytest

from OCP3x import BinLDrivers, BinMDF, BinObjMgt, PCDM, TDataStd, TDocStd
from OCP3x.TCollection import TCollection_ExtendedString

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKBinL" / "report.txt"


@pytest.mark.parametrize("pkg", ["BinLDrivers", "BinMDF", "BinMDataStd", "BinMDocStd", "BinMFunction", "BinObjMgt"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


@pytest.fixture
def app():
    app = TDocStd.TDocStd_Application()
    BinLDrivers.BinLDrivers.DefineFormat_s(app)           # registers BinLOcaf without resource files
    return app


def _document(app):
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinLOcaf"))
    label = doc.Main().FindChild(1, True)
    TDataStd.TDataStd_Name.Set_s(label, TCollection_ExtendedString("part"))
    TDataStd.TDataStd_Integer.Set_s(label, 42)
    TDataStd.TDataStd_Real.Set_s(label, 2.5)
    return doc


def test_save_to_bytes_and_reload(app):
    doc = _document(app)
    status, data = app.SaveAs(doc)                       # SaveAs(doc, ostream&) -> (status, bytes)
    assert status == PCDM.PCDM_SS_OK and isinstance(data, bytes) and data.startswith(b"BINFILE")
    status, again = app.Open(io.BytesIO(data))           # Open(istream&, handle<TDocStd_Document>&) -> (status, doc)
    assert status == PCDM.PCDM_RS_OK and type(again) is TDocStd.TDocStd_Document
    label = again.Main().FindChild(1, False)
    assert label.FindAttribute(TDataStd.TDataStd_Name.GetID_s())[1].Get().ToExtString() == "part"
    assert label.FindAttribute(TDataStd.TDataStd_Integer.GetID_s())[1].Get() == 42
    assert label.FindAttribute(TDataStd.TDataStd_Real.GetID_s())[1].Get() == 2.5
    with pytest.raises(TypeError):                       # a text file-like is not a binary stream
        app.Open(io.StringIO(data.decode("latin-1")))


def test_save_to_file_matches_the_bytes(app, tmp_path):
    """OCCT appends the format's extension when the path's does not match (`doc.cbf` is saved as `doc.cbf.cbfl`, checked);
    with `.cbfl` the file is written as given and holds exactly the SaveAs(doc) bytes."""
    doc = _document(app)
    path = tmp_path / "doc.cbfl"
    assert app.SaveAs(doc, TCollection_ExtendedString(str(path))) == PCDM.PCDM_SS_OK
    assert doc.IsSaved() and doc.GetPath().ToExtString() == str(path)
    assert path.read_bytes() == app.SaveAs(doc)[1]
    # the document is open in this application under that path: OCCT refuses to retrieve it a second time
    assert app.Open(TCollection_ExtendedString(str(path))) == (PCDM.PCDM_RS_AlreadyRetrieved, None)
    other = TDocStd.TDocStd_Application()
    BinLDrivers.BinLDrivers.DefineFormat_s(other)
    status, again = other.Open(TCollection_ExtendedString(str(path)))
    assert status == PCDM.PCDM_RS_OK and again.Main().FindChild(1).FindAttribute(TDataStd.TDataStd_Integer.GetID_s())[1].Get() == 42


def test_save_without_a_defined_format_fails(app):
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinOcaf"))     # TKBin's format, not defined here
    assert app.SaveAs(doc)[0] == PCDM.PCDM_SS_Failure                                # WriterFromFormat fails on the missing resource


def test_drivers_and_relocation_tables():
    drivers = BinLDrivers.BinLDrivers.AttributeDrivers_s(None)                 # handle<Message_Messenger>& -> None
    assert type(drivers) is BinMDF.BinMDF_ADriverTable
    table = BinObjMgt.BinObjMgt_RRelocationTable()                           # derives from NCollection_DataMap[int, Standard_Transient]
    assert table.IsEmpty() and table.Extent() == 0 and table.GetHeaderData() is None
    persistent = BinObjMgt.BinObjMgt_Persistent()
    persistent.SetTypeId(1)                                                  # Read() stops at a zero type id (BinObjMgt_Persistent.cxx:140)
    persistent.SetId(7)
    persistent.PutInteger(42)
    data = persistent.Write(False)                                           # Write(ostream&, direct) -> bytes
    assert isinstance(data, bytes) and len(data) > 0
    back = BinObjMgt.BinObjMgt_Persistent()
    back.Read(io.BytesIO(data))                                              # Read(istream&) -> istream& chaining dropped
    assert (back.TypeId(), back.Id(), back.GetInteger()) == (1, 7, 42)


def test_report_has_only_the_expected_omissions():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    categories = {line.split("\t")[0] for line in lines}
    assert categories <= {"operator", "overload-collision", "override", "raw-pointer", "stream", "template"}
    assert any("SetOStream" in line and "[skip] methods" in line for line in lines)   # stores the stream reference: dangling
    assert not any("RRelocationTable" in line for line in lines)                      # the binder base is bound now
