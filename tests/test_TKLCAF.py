"""Generated bindings for TKLCAF (ApplicationFramework: TDF, TDataStd, TFunction, TDocStd, AppStdL): the OCAF document
that build123d/CadQuery's XCAF export is built on -- application, document, labels, standard attributes, undo/redo,
iterators, dumps. No storage driver is linked yet (TKBinL/TKXmlL): saving is exercised as far as the driverless status."""
import importlib
from pathlib import Path

import pytest

from nanocct import AppStdL, PCDM, TDF, TDataStd, TDocStd, TFunction
from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKLCAF" / "report.txt"


@pytest.mark.parametrize("pkg", ["TDF", "TDataStd", "TFunction", "TDocStd", "AppStdL"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


@pytest.fixture
def doc():
    app = TDocStd.TDocStd_Application()
    return app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinOcaf"))


def test_new_document_both_overloads_downcast(doc):
    """NewDocument(format, handle<TDocStd_Document>&) and the CDM_Application one (handle<CDM_Document>&) both return the
    document (R-OUT-HANDLE); the handle caster downcasts to the dynamic type (4.2)."""
    app = TDocStd.TDocStd_Application()
    assert type(doc) is TDocStd.TDocStd_Document
    assert type(app.NewDocument(TCollection_ExtendedString("BinOcaf"))) is TDocStd.TDocStd_Document
    assert doc.StorageFormat().ToExtString() == "BinOcaf"
    assert doc.Main().Tag() == 1 and doc.Main().Depth() == 1 and doc.Main().IsRoot() is False


def test_standard_attributes_static_set_and_find(doc):
    """TDataStd_Name::Set(label, string) is static and collides with the instance Set(string): Set_s (R-STATIC-S) --
    build123d calls exactly TDataStd_Name.Set_s. FindAttribute(GUID, handle&) returns (found, attribute) downcast."""
    label = doc.Main().FindChild(1, True)
    name = TDataStd.TDataStd_Name.Set_s(label, TCollection_ExtendedString("part"))
    assert type(name) is TDataStd.TDataStd_Name and name.Get().ToExtString() == "part"
    found, attr = label.FindAttribute(TDataStd.TDataStd_Name.GetID_s())
    assert found is True and type(attr) is TDataStd.TDataStd_Name and attr.Get().ToExtString() == "part"
    assert label.FindAttribute(TDataStd.TDataStd_Real.GetID_s())[0] is False
    integer = TDataStd.TDataStd_Integer.Set_s(label, 42)
    real = TDataStd.TDataStd_Real.Set_s(label, 2.5)
    assert (integer.Get(), real.Get(), label.NbAttributes()) == (42, 2.5, 3)
    assert [type(a).__name__ for a in TDF.TDF_AttributeIterator(label)] == ["TDataStd_Name", "TDataStd_Integer", "TDataStd_Real"]
    array = TDataStd.TDataStd_RealArray.Set_s(label, 1, 3)               # no instance Set of that name: plain Set
    array.SetValue(2, 7.5)
    assert [array.Value(k) for k in range(1, 4)] == [0.0, 7.5, 0.0]


def test_label_entries_children_equality_and_hash(doc):
    main = doc.Main()
    child = main.FindChild(1, True)
    entry = TCollection_AsciiString()
    TDF.TDF_Tool.Entry_s(child, entry)                                    # TCollection_AsciiString& filled in place (R-REF-CLASS)
    assert entry.ToCString() == "0:1:1"
    found = TDF.TDF_Label()
    TDF.TDF_Tool.Label_s(doc.GetData(), TCollection_AsciiString("0:1:1"), found, False)
    assert found == child and found != main and not found.IsNull() and TDF.TDF_Label().IsNull()
    assert found and not TDF.TDF_Label()                                  # R-NULL-BOOL: __bool__ is not IsNull()
    assert hash(found) == hash(child) and {child: "c"}[found] == "c"     # std::hash<TDF_Label> lives in TDF_Label.lxx
    main.FindChild(2, True)
    main.FindChild(3, True)
    assert [c.Tag() for c in TDF.TDF_ChildIterator(main)] == [1, 2, 3]
    TDataStd.TDataStd_Integer.Set_s(child, 1)
    assert [type(a).__name__ for a in TDF.TDF_ChildIDIterator(main, TDataStd.TDataStd_Integer.GetID_s())] == ["TDataStd_Integer"]
    assert child.Father() == main and child.Root().IsRoot() and child.Data() is doc.GetData()


def test_undo_redo(doc):
    doc.SetUndoLimit(10)
    label = doc.Main().FindChild(1, True)
    integer = TDataStd.TDataStd_Integer.Set_s(label, 42)
    doc.NewCommand()
    TDataStd.TDataStd_Integer.Set_s(label, 43)
    assert doc.CommitCommand() is True and integer.Get() == 43 and doc.GetAvailableUndos() == 1
    doc.Undo()
    assert integer.Get() == 42 and doc.GetAvailableRedos() == 1
    doc.Redo()
    assert integer.Get() == 43


def test_tree_nodes_and_functions(doc):
    label = doc.Main().FindChild(1, True)
    node = TDataStd.TDataStd_TreeNode.Set_s(label)
    node.Append(TDataStd.TDataStd_TreeNode.Set_s(doc.Main().FindChild(2, True)))
    assert [t.Label().Tag() for t in TDataStd.TDataStd_ChildNodeIterator(node)] == [2]
    fn = TFunction.TFunction_Function.Set_s(label, TDataStd.TDataStd_Integer.GetID_s())
    assert fn.GetDriverGUID() == TDataStd.TDataStd_Integer.GetID_s()


def test_dumps_are_str(doc):
    label = doc.Main().FindChild(1, True)
    assert label.Dump().startswith("0:1:1\t")                            # Dump(Standard_OStream&) -> str (R-STREAM-OUT)
    assert TDF.TDF_Tool.DeepDump_s(doc.GetData()).startswith("Dump of a TDF_Data.")
    assert '"className": "TDocStd_Document"' in doc.DumpJson()


def test_save_without_a_storage_driver_and_stream_kinds(doc):
    """TDocStd_Application::SaveAs(doc, ostream&) and Open(istream&) are document streams (bytes, overrides.toml
    [stream] binary_members) inside an otherwise text package (DumpJson). Without TKBinL no driver is defined for
    BinOcaf: the status says so (and OCCT prints the resource message)."""
    app = TDocStd.TDocStd_Application()
    status, data = app.SaveAs(doc)
    assert status == PCDM.PCDM_SS_Failure and data == b""
    assert "-> tuple[nanocct.PCDM.PCDM_StoreStatus, bytes]" in TDocStd.TDocStd_Application.SaveAs.__doc__
    assert "theIStream: typing.BinaryIO" in TDocStd.TDocStd_Application.Open.__doc__
    assert "DumpJson(self, theDepth: int = -1) -> str" in TDocStd.TDocStd_Document.DumpJson.__doc__
    # SaveAs(doc, ostream&, ExtendedString& theStatusMessage, range) collides with SaveAs(doc, path, range) after the
    # stream is removed: the typed suffix names the returned stream (R-COLLISION)
    assert "SaveAs__bytes(self, theDoc" in TDocStd.TDocStd_Application.SaveAs__bytes.__doc__


def test_keyword_parameter_names_are_suffixed():
    """TDataStd_Name::Restore(const handle<TDF_Attribute>& with): `with` is a Python keyword (R-KEYWORD -> with_)."""
    assert "Restore(self, with_: " in TDataStd.TDataStd_Name.Restore.__doc__


def test_report_has_only_the_expected_omissions():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    categories = {line.split("\t")[0] for line in lines}
    assert categories <= {"copy", "iterator", "not-constructible", "null-bool", "operator", "overload-collision", "raw-pointer", "stream", "template", "unbound-type", "view-guard"}
    # R-VIEW-GUARD (2026-10-02): the data set's and relocation table's maps, the HDataMaps' ChangeMap(), ...
    assert sum(line.startswith("view-guard") for line in lines) == 15
    # R-COPY (2026-10-02): a copy of a TDF_Data would share its label tree, which its destructor frees
    assert [line.split("\t")[2].split(":")[0] for line in lines if line.startswith("copy")] == ["TDF_Data"]
    # R-UNBOUND-TYPE (2026-09-30): the TDF_LabelNode* constructor -- TDF_LabelNode is internal and not bound; TDF_Label's stays
    assert [line.split("\t")[2].split("): ")[0] + ")" for line in lines if line.startswith("unbound-type")] == [
        "TDF_AttributeIterator::TDF_AttributeIterator(const TDF_LabelNodePtr, const bool)"]
    assert any("TDF_Label::FindAttribute: template member" in line for line in lines)    # the non-template overload downcasts (2d)
