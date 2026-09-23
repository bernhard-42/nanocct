"""Generated bindings for TKDEOBJ (DataExchange: RWObj, DEOBJ): Wavefront OBJ import and export, built on TKRWMesh
like glTF. OBJ is an ASCII geometry file with a sidecar .mtl for the materials, and its reader is nevertheless fed
bytes -- the path overload opens the file with std::ios_base::binary and hands that stream on."""
import importlib
import io
from pathlib import Path

import pytest

from nanoocp import Message
from nanoocp.BRepMesh import BRepMesh_IncrementalMesh
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.DEOBJ import DEOBJ_ConfigurationNode, DEOBJ_Provider
from nanoocp.Message import Message_ProgressRange
from nanoocp.NCollection import NCollection_DataMap, NCollection_IndexedDataMap, NCollection_Sequence
from nanoocp.Quantity import Quantity_Color, Quantity_NOC_RED
from nanoocp.RWObj import (RWObj, RWObj_CafReader, RWObj_CafWriter, RWObj_Material, RWObj_MtlReader, RWObj_Reader,
                           RWObj_SubMesh, RWObj_SubMeshReason, RWObj_TriangulationReader)
from nanoocp.TCollection import TCollection_AsciiString, TCollection_ExtendedString
from nanoocp.TDF import TDF_Label
from nanoocp.TopAbs import TopAbs_COMPOUND, TopAbs_FACE
from nanoocp.TopExp import TopExp_Explorer
from nanoocp.XCAFApp import XCAFApp_Application
from nanoocp.XCAFDoc import XCAFDoc_ColorGen, XCAFDoc_DocumentTool

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDEOBJ" / "report.txt"


@pytest.fixture
def quiet_messenger():
    printers = list(Message.Message.DefaultMessenger().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


def _empty_document():
    app = XCAFApp_Application.GetApplication()
    return app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))


@pytest.fixture
def document():
    doc = _empty_document()
    shapes = XCAFDoc_DocumentTool.ShapeTool(doc.Main())
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    BRepMesh_IncrementalMesh(box, 0.1)                            # OBJ exports triangulations
    label = shapes.AddShape(box, False)
    XCAFDoc_DocumentTool.ColorTool(doc.Main()).SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorGen)
    return doc


def _write(document, path):
    writer = RWObj_CafWriter(TCollection_AsciiString(str(path)))
    metadata = NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString]()
    assert writer.Perform(document, metadata, Message_ProgressRange())
    return path


@pytest.mark.parametrize("pkg", ["RWObj", "DEOBJ"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_the_caf_writer_writes_an_obj(tmp_path, document, quiet_messenger):
    lines = _write(document, tmp_path / "box.obj").read_text().splitlines()
    assert lines[0].startswith("# Exported by Open CASCADE Technology")
    assert sum(line.startswith("v ") for line in lines) == 24     # a box meshed per face: 4 corners x 6
    assert sum(line.startswith("f ") for line in lines) == 12     # two triangles per face


def test_the_colour_becomes_an_mtl_sidecar(tmp_path, document, quiet_messenger):
    """OBJ keeps its materials in a second file, referenced by mtllib/usemtl."""
    obj = _write(document, tmp_path / "box.obj").read_text()
    assert "mtllib box.mtl" in obj and "usemtl mat_1" in obj

    mtl = (tmp_path / "box.mtl").read_text()
    assert "newmtl mat_1" in mtl
    assert "Kd 1.000000 0.000000 0.000000" in mtl                 # the diffuse colour is the red of the document

    # ... and RWObj_MtlReader reads it back. The folder is prepended verbatim, so it needs its separator
    # (RWObj_MtlReader.cxx: theFolder + theFile).
    materials = NCollection_DataMap[TCollection_AsciiString, RWObj_Material]()
    assert RWObj_MtlReader(materials).Read(TCollection_AsciiString(str(tmp_path) + "/"), TCollection_AsciiString("box.mtl"))
    assert [key.ToCString() for key in materials] == ["mat_1"]
    assert materials.Find(TCollection_AsciiString("mat_1")).DiffuseColor.Red() == 1.0


def test_a_document_round_trips(tmp_path, document, quiet_messenger):
    path = _write(document, tmp_path / "box.obj")
    reloaded = _empty_document()
    reader = RWObj_CafReader()                                    # its public constructor was unreachable until 2026-09-23
    reader.SetDocument(reloaded)
    assert reader.Perform(TCollection_AsciiString(str(path)), Message_ProgressRange())

    free = NCollection_Sequence[TDF_Label]()
    XCAFDoc_DocumentTool.ShapeTool(reloaded.Main()).GetFreeShapes(free)
    assert free.Length() == 1
    shape = reader.SingleShape()
    assert shape.ShapeType() == TopAbs_COMPOUND                   # a mesh, not the original solid
    assert sum(1 for _ in TopExp_Explorer(shape, TopAbs_FACE)) == 1   # one OBJ group, one triangulated face


def test_the_reader_streams_are_bytes(tmp_path, document, quiet_messenger):
    """RWObj_Reader::Read(path) and Probe(path) open the file with std::ios_base::in | std::ios_base::binary and hand
    that stream to the istream& overload (RWObj_Reader.hxx:53-56,74-77); read() then takes the file length from
    tellg() (RWObj_Reader.cxx:114-116), which only a binary stream reports in bytes. So both are
    overrides.toml [stream] binary_members, although OBJ itself is an ASCII format -- the same question RWStl and
    RWMesh needed (2b)."""
    assert "theStream: typing.BinaryIO" in RWObj_Reader.Read.__doc__
    assert "theStream: typing.BinaryIO" in RWObj_Reader.Probe.__doc__
    assert "theStream: typing.BinaryIO" in RWObj_CafReader.Perform.__doc__     # inherited from RWMesh_CafReader

    data = _write(document, tmp_path / "box.obj").read_bytes()
    reader = RWObj_CafReader()
    reader.SetDocument(_empty_document())
    assert reader.Perform(io.BytesIO(data), Message_ProgressRange(), TCollection_AsciiString("box.obj"))
    assert sum(1 for _ in TopExp_Explorer(reader.SingleShape(), TopAbs_FACE)) == 1


def test_the_triangulation_reader_reads_and_probes_a_stream(tmp_path, document, quiet_messenger):
    path = _write(document, tmp_path / "box.obj")
    data = path.read_bytes()

    reader = RWObj_TriangulationReader()
    assert reader.Read(io.BytesIO(data), TCollection_AsciiString(str(path)), Message_ProgressRange())
    assert reader.FileComments().ToCString().startswith("Exported by Open CASCADE Technology")

    probe = RWObj_TriangulationReader()                           # parses the file without collecting the mesh
    assert probe.Probe(io.BytesIO(data), TCollection_AsciiString(str(path)), Message_ProgressRange())
    assert (probe.NbProbeNodes(), probe.NbProbeElems()) == (24, 12)
    # the path is what locates the sidecar: the folder comes from theFile, and OCCT records the reference only once
    # the .mtl was read (RWObj_Reader.cxx:710-713)
    assert [name.ToCString() for name in probe.ExternalFiles()] == [str(tmp_path / "box.mtl")]


def test_the_package_function_reads_a_triangulation(tmp_path, document, quiet_messenger):
    path = _write(document, tmp_path / "box.obj")
    triangulation = RWObj.ReadFile(str(path), Message_ProgressRange())
    assert (triangulation.NbNodes(), triangulation.NbTriangles()) == (24, 12)


def test_the_sub_mesh_carries_the_material_and_its_reason():
    assert RWObj_SubMesh().Group.ToCString() == ""
    assert RWObj_SubMeshReason.RWObj_SubMeshReason_NewMaterial in list(RWObj_SubMeshReason)


def test_the_de_provider(tmp_path, document, quiet_messenger):
    node = DEOBJ_ConfigurationNode()
    assert node.GetFormat().ToCString() == "OBJ" and node.GetVendor().ToCString() == "OCC"
    assert [extension.ToCString() for extension in node.GetExtensions()] == ["obj"]

    path = _write(document, tmp_path / "box.obj")
    reloaded = _empty_document()
    assert DEOBJ_Provider(node).Read(TCollection_AsciiString(str(path)), reloaded, Message_ProgressRange())
    free = NCollection_Sequence[TDF_Label]()
    XCAFDoc_DocumentTool.ShapeTool(reloaded.Main()).GetFreeShapes(free)
    assert free.Length() == 1


def test_report_is_four_lines():
    """RWObj_IShapeReceiver is the reader's internal callback interface (a Python subclass would need trampolines,
    roadmap 8.5); RWObj_Tools::ReadVec3 advances a `const char*&` cursor through the line being parsed; and
    RWObj_Reader is abstract, for which clang emits no complete-object constructor -- the nm check sees the
    declaration without a symbol."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert len(lines) == 4
    assert sum(line.startswith("raw-pointer") and "reference to pointer" in line for line in lines) == 2
    assert any("RWObj_CafReader: non-public base RWObj_IShapeReceiver dropped; its members are not bound" in line
               for line in lines)
    assert any(line.startswith("undefined") and "RWObj_Reader::RWObj_Reader()" in line for line in lines)
