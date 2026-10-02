"""Generated bindings for TKDEGLTF (DataExchange: RWGltf, DEGLTF): glTF import and export. RWGltf_CafWriter is the
last of the calls build123d and CadQuery make that nanocct was missing. glTF comes in two flavours -- .gltf is JSON
with a sidecar .bin, .glb is one binary file -- and the reader takes either as bytes."""
import importlib
import io
import json
from pathlib import Path

import pytest

from nanocct import Message
from nanocct.BRepMesh import BRepMesh_IncrementalMesh
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.DEGLTF import DEGLTF_ConfigurationNode, DEGLTF_Provider
from nanocct.Message import Message_ProgressRange
from nanocct.NCollection import NCollection_IndexedDataMap, NCollection_Sequence
from nanocct.Quantity import Quantity_Color, Quantity_NOC_RED
from nanocct.RWGltf import RWGltf_CafReader, RWGltf_CafWriter, RWGltf_TriangulationReader
from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString
from nanocct.TDF import TDF_Label
from nanocct.TopAbs import TopAbs_COMPOUND, TopAbs_FACE
from nanocct.TopExp import TopExp_Explorer
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDoc import XCAFDoc_ColorGen, XCAFDoc_DocumentTool

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDEGLTF" / "report.txt"


@pytest.fixture
def quiet_messenger():
    printers = list(Message.Message.DefaultMessenger_s().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


@pytest.fixture
def document():
    app = XCAFApp_Application.GetApplication_s()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    BRepMesh_IncrementalMesh(box, 0.1)                            # glTF exports triangulations
    label = shapes.AddShape(box, False)
    XCAFDoc_DocumentTool.ColorTool_s(doc.Main()).SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorGen)
    return doc


def _empty_document():
    app = XCAFApp_Application.GetApplication_s()
    return app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))


@pytest.mark.parametrize("pkg", ["RWGltf", "DEGLTF"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_the_caf_writer_is_build123d_s_last_missing_call(tmp_path, document, quiet_messenger):
    """RWGltf_CafWriter(path, isBinary): False writes .gltf (JSON plus a sidecar .bin), True writes one .glb."""
    path = tmp_path / "box.gltf"
    writer = RWGltf_CafWriter(TCollection_AsciiString(str(path)), False)
    metadata = NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString]()
    assert writer.Perform(document, metadata, Message_ProgressRange())
    assert (tmp_path / "box.bin").exists()                        # the sidecar buffer

    content = json.loads(path.read_text())
    assert content["asset"]["version"] == "2.0"
    assert len(content["meshes"]) == 1 and len(content["materials"]) == 1
    assert {"accessors", "bufferViews", "buffers", "nodes", "scene"} <= set(content)


def test_the_binary_flavour_is_a_glb(tmp_path, document, quiet_messenger):
    path = tmp_path / "box.glb"
    writer = RWGltf_CafWriter(TCollection_AsciiString(str(path)), True)
    assert writer.Perform(document, NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString](),
                          Message_ProgressRange())
    assert path.read_bytes()[:4] == b"glTF"                       # the glb magic
    assert not (tmp_path / "box.bin").exists()                    # one self-contained file


def test_a_document_round_trips(tmp_path, document, quiet_messenger):
    path = tmp_path / "box.glb"
    RWGltf_CafWriter(TCollection_AsciiString(str(path)), True).Perform(
        document, NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString](), Message_ProgressRange())

    reloaded = _empty_document()
    reader = RWGltf_CafReader()
    reader.SetDocument(reloaded)
    assert reader.Perform(TCollection_AsciiString(str(path)), Message_ProgressRange())
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(reloaded.Main())
    free = NCollection_Sequence[TDF_Label]()
    shapes.GetFreeShapes(free)
    assert free.Length() == 1
    shape = shapes.GetShape_s(free.Value(1))
    assert shape.ShapeType() == TopAbs_COMPOUND                   # a mesh, not the original solid
    assert sum(1 for _ in TopExp_Explorer(shape, TopAbs_FACE)) == 6


def test_both_flavours_read_from_memory_as_bytes(tmp_path, document, quiet_messenger):
    """RWMesh_CafReader::Perform/ProbeHeader open their file with std::ios_base::binary and hand that stream on
    (RWMesh_CafReader.hxx:187,225), and ProbeHeader sniffs which flavour it got -- so both are bytes, not text
    (overrides.toml [stream] binary_members). TKRWMesh had bound them as typing.TextIO until 2026-09-22."""
    assert "theStream: typing.BinaryIO" in RWGltf_CafReader.Perform.__doc__
    assert "theStream: typing.BinaryIO" in RWGltf_CafReader.ProbeHeader.__doc__
    assert "typing.BinaryIO" in RWGltf_TriangulationReader.ReadStream.__doc__

    written = {}
    for name, is_binary in (("box.glb", True), ("box.gltf", False)):
        path = tmp_path / name
        RWGltf_CafWriter(TCollection_AsciiString(str(path)), is_binary).Perform(
            document, NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString](),
            Message_ProgressRange())
        written[name] = path

    for name, path in written.items():
        reloaded = _empty_document()
        reader = RWGltf_CafReader()
        reader.SetDocument(reloaded)
        assert reader.Perform(io.BytesIO(path.read_bytes()), Message_ProgressRange(),
                              TCollection_AsciiString(str(path))), name
        free = NCollection_Sequence[TDF_Label]()
        XCAFDoc_DocumentTool.ShapeTool_s(reloaded.Main()).GetFreeShapes(free)
        assert free.Length() == 1, name
    assert RWGltf_CafReader().ProbeHeader(io.BytesIO(written["box.glb"].read_bytes()),
                                          TCollection_AsciiString(str(written["box.glb"])))


def test_the_de_provider():
    assert DEGLTF_ConfigurationNode().GetFormat().ToCString() == "GLTF"
    assert DEGLTF_Provider().GetVendor().ToCString() == "OCC"


def test_report_is_nine_lines():
    """RapidJSON is third-party plumbing: RWGltf_GltfJsonParser derives from rapidjson::GenericDocument, which pulled
    the library's Writer/MemoryPoolAllocator/UTF8 into the package until the namespace was skipped."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    # 7 until 2026-09-23: rapidjson::GenericValue appears only as a reference parameter, so the skipped namespace was
    # not reported for it -- the method bound with an unregistered type instead (6c, R-UNSUPPORTED)
    # 9 since 2026-09-30: FormatParseError(rapidjson::ParseErrorCode) is not bound, no Python value of the type exists (R-UNBOUND-TYPE)
    # 14 since 2026-10-02: RWGltf_GltfMaterialMap keeps the writer it is handed (R-METHOD-KEEP), so the writer, written into,
    # does not keep the map back -- that would be a keep-alive cycle (R-RESULT-KEEP)
    assert len(lines) == 14
    assert sum(line.startswith("lifetime") and "RWGltf_GltfMaterialMap::" in line and "theWriter" in line for line in lines) == 5
    assert sum("rapidjson" in line and "namespace skipped" in line for line in lines) == 4
    assert sum("R-TEMPLATE-BASE" in line for line in lines) == 2   # the two rapidjson bases, dropped
    # the two stream lines are objects that *hold* a stream beyond the call, as for BinTools (2d)
    assert sum(line.startswith("stream") for line in lines) == 2
