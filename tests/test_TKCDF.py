"""Generated bindings for TKCDF (ApplicationFramework: CDM, PCDM, CDF, UTL, LDOM): the document-framework bases that
TDocStd/XCAF build on, OCAF format detection from bytes (PCDM/CDF are binary-stream packages, R-STREAM-IN/OUT), the reader
filter, and OCCT's own XML DOM (LDOM) parsed from and written to Python strings. The first `const char* = nullptr`
parameter (LDOM_XmlWriter) exercises R-CSTR-NULL."""
import importlib
import io
from pathlib import Path

import pytest

from nanoocp import CDF, CDM, LDOM, PCDM, UTL
from nanoocp.TCollection import TCollection_AsciiString, TCollection_ExtendedString

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKCDF" / "report.txt"

XML = '<?xml version="1.0"?>\n<root a="1"><child b="two">text</child><child/><!-- c --></root>\n'


@pytest.mark.parametrize("pkg", ["CDM", "PCDM", "CDF", "UTL", "LDOM"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_ldom_parse_from_a_text_file_like_and_navigate():
    """LDOMParser::parse(istream&) takes a text file-like (R-STREAM-IN) and returns True on *error* (LDOMParser.hxx:53-64)."""
    parser = LDOM.LDOMParser()
    assert parser.parse(io.StringIO(XML)) is False
    assert parser.GetError(TCollection_AsciiString()).IsEmpty()
    root = parser.getDocument().getDocumentElement()
    assert root.getTagName().GetString() == "root"
    assert root.getNodeType() == LDOM.LDOM_Node.NodeType.ELEMENT_NODE
    # a str converts to LDOMString implicitly (R-IMPLICIT); a numeric attribute value is an LDOM_Integer, whose
    # GetString() is "" by OCCT's design (LDOMBasicString.hxx:58) -- GetInteger() gives it back
    a = root.getAttribute("a")
    assert a.Type() == LDOM.LDOMBasicString.StringType.LDOM_Integer and a.GetString() == "" and a.GetInteger() == (True, 1)
    child = root.GetChildByTagName(LDOM.LDOMString("child"))
    assert child.getAttribute("b").GetString() == "two"
    assert child.getFirstChild().getNodeValue().GetString() == "text"
    assert root.getElementsByTagName("child").getLength() == 2
    first = root.getFirstChild()
    assert first == root.getFirstChild() and first != root.getLastChild() and not first.isNull()
    assert LDOM.LDOM_Node().isNull()
    attrs = root.GetAttributesList()
    assert attrs.getLength() == 1 and attrs.item(0).getNodeName().GetString() == "a"


def test_ldom_parse_error_is_reported():
    parser = LDOM.LDOMParser()
    assert parser.parse(io.StringIO("<root><unclosed></root>")) is True
    assert parser.GetError(TCollection_AsciiString()).Length() > 0


def test_ldom_writer_optional_encoding_and_str_result():
    """LDOM_XmlWriter(const char* theEncoding = nullptr): the default is reachable (R-CSTR-NULL) and equals None; the
    ostream& of Write() comes back as str (R-STREAM-OUT)."""
    doc = LDOM.LDOM_Document.createDocument("root")
    item = doc.createElement("item")
    item.setAttribute("id", "7")
    item.appendChild(doc.createTextNode("hello"))
    doc.getDocumentElement().appendChild(item)
    for writer in (LDOM.LDOM_XmlWriter(), LDOM.LDOM_XmlWriter(None), LDOM.LDOM_XmlWriter("UTF-8")):
        text = writer.Write(doc)
        assert isinstance(text, str)
        assert text == '<?xml version="1.0" encoding="UTF-8"?>\n<root><item id="7">hello</item></root>'
    with pytest.raises(TypeError):
        LDOM.LDOM_XmlWriter(b"UTF-8")
    indented = LDOM.LDOM_XmlWriter()
    indented.SetIndentation(2)
    assert "\n  <item" in indented.Write(doc)
    # a round trip through the parser
    parser = LDOM.LDOMParser()
    assert parser.parse(io.StringIO(LDOM.LDOM_XmlWriter().Write(doc))) is False
    assert parser.getDocument().getDocumentElement().GetChildByTagName("item").getAttribute("id").GetInteger() == (True, 7)


def test_pcdm_format_detection_from_bytes():
    """PCDM/CDF are binary-stream packages: their istream& parameters take a binary file-like (R-STREAM-IN), because the
    same entry points read binary and XML OCAF documents. The XML header is detected by PCDM::FileDriverType (PCDM.cxx:82)
    and the format by the `document` element's attribute (PCDM_ReadWriter.cxx:211-233)."""
    xml = b'<?xml version="1.0" encoding="UTF-8"?>\n<document format="XmlOcaf" xmlns="http://www.opencascade.org/OCAF/XML"><info/></document>\n'
    fmt, data = PCDM.PCDM_ReadWriter.FileFormat(io.BytesIO(xml))       # handle<Storage_Data>& out: null (None) on the XML path
    assert fmt.ToExtString() == "XmlOcaf" and data is None
    assert PCDM.PCDM.FileDriverType(io.BytesIO(xml)) == (PCDM.PCDM_TOFD_XmlFile, None)
    assert PCDM.PCDM.FileDriverType(io.BytesIO(b"garbage")) == (PCDM.PCDM_TOFD_Unknown, None)
    with pytest.raises(TypeError):                                         # a text file-like falls through (typing.BinaryIO)
        PCDM.PCDM.FileDriverType(io.StringIO(xml.decode()))
    assert "theIStream: typing.BinaryIO" in CDF.CDF_Application.Read.__doc__
    assert "-> bytes" in PCDM.PCDM_StorageDriver.Write.__doc__


def test_pcdm_reader_filter():
    flt = PCDM.PCDM_ReaderFilter(PCDM.PCDM_ReaderFilter.AppendMode_Forbid)
    assert flt.Mode() == PCDM.PCDM_ReaderFilter.AppendMode.AppendMode_Forbid and flt.IsAppendMode() is False
    flt.AddSkipped(TCollection_AsciiString("TDataStd_Name"))
    flt.AddRead(TCollection_AsciiString("TDataStd_Integer"))
    assert flt.IsPassedAttr(TCollection_AsciiString("TDataStd_Name")) is False
    assert flt.IsPassedAttr(TCollection_AsciiString("TDataStd_Integer")) is True


def test_cdf_directory_utl_and_metadata_print():
    directory = CDF.CDF_Directory()
    assert directory.IsEmpty() and directory.Length() == 0
    assert UTL.UTL.Extension(TCollection_ExtendedString("doc.xbf")).ToExtString() == "xbf"
    assert "Print(self) -> str" in CDM.CDM_MetaData.Print.__doc__                  # Print(Standard_OStream&) -> str


def test_report_has_only_the_expected_omissions():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    categories = {line.split("\t")[0] for line in lines}
    assert categories <= {"iterator", "operator", "raw-pointer", "unbound-type", "undefined"}
    assert any("LDOM_OSStream: base class Standard_OStream" in line for line in lines)   # the std::ostream subclass (Design.md 2d)
