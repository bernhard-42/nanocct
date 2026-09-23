"""Generated bindings for TKDEVRML (DataExchange: Vrml, VrmlData, VrmlAPI, VrmlConverter, DEVRML): VRML, the last
DataExchange format toolkit. It brings VrmlAPI.Write, one of the calls build123d and CadQuery make, and it is the
only format so far with two generations side by side -- `Vrml` is the VRML 1.0 node set that prints itself, `VrmlData`
the VRML 2.0 DOM that parses and converts."""
import importlib
import io
from pathlib import Path

import pytest

from nanoocp import Message
from nanoocp.BRepMesh import BRepMesh_IncrementalMesh
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.DEVRML import DEVRML_ConfigurationNode, DEVRML_Provider
from nanoocp.Message import Message_ProgressRange
from nanoocp.NCollection import NCollection_DataMap__Handle_TopoDS_TShape__Handle_VrmlData_Appearance as AppearanceMap
from nanoocp.Quantity import Quantity_Color, Quantity_NOC_RED
from nanoocp.TCollection import TCollection_AsciiString, TCollection_ExtendedString
from nanoocp.TopAbs import TopAbs_COMPOUND, TopAbs_FACE
from nanoocp.TopExp import TopExp_Explorer
from nanoocp.Vrml import Vrml_Cone, Vrml_Material
from nanoocp.VrmlAPI import VrmlAPI, VrmlAPI_CafReader, VrmlAPI_RepresentationOfShape, VrmlAPI_Writer
from nanoocp.VrmlConverter import VrmlConverter_Drawer
from nanoocp.VrmlData import VrmlData_Scene, VrmlData_ShapeConvert
from nanoocp.XCAFApp import XCAFApp_Application
from nanoocp.XCAFDoc import XCAFDoc_ColorGen, XCAFDoc_DocumentTool

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDEVRML" / "report.txt"


@pytest.fixture
def quiet_messenger():
    printers = list(Message.Message.DefaultMessenger().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


@pytest.fixture
def meshed_box():
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    BRepMesh_IncrementalMesh(box, 0.1)                            # VRML exports triangulations
    return box


def _document(box):
    app = XCAFApp_Application.GetApplication()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    label = XCAFDoc_DocumentTool.ShapeTool(doc.Main()).AddShape(box, False)
    XCAFDoc_DocumentTool.ColorTool(doc.Main()).SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorGen)
    return doc


@pytest.mark.parametrize("pkg", ["Vrml", "VrmlData", "VrmlAPI", "VrmlConverter", "DEVRML"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_the_package_function_is_build123d_s_call(tmp_path, meshed_box, quiet_messenger):
    """VrmlAPI.Write(shape, file, version) -- OCP spells it VrmlAPI.Write_s; here the static has no instance twin."""
    path = tmp_path / "box.wrl"
    assert VrmlAPI.Write(meshed_box, str(path), 2)
    assert path.read_text().splitlines()[0] == "#VRML V2.0 utf8"

    older = tmp_path / "box1.wrl"
    assert VrmlAPI.Write(meshed_box, str(older), 1)
    assert older.read_text().splitlines()[0] == "#VRML V1.0 ascii"


def test_the_writer_writes_to_a_file_and_to_a_string(tmp_path, meshed_box, quiet_messenger):
    """VRML is text, so the ostream& overloads are R-STREAM-OUT results: (ok, str), and the same bytes as the file."""
    writer = VrmlAPI_Writer()
    assert writer.GetRepresentation() == VrmlAPI_RepresentationOfShape.VrmlAPI_BothRepresentation
    writer.SetRepresentation(VrmlAPI_RepresentationOfShape.VrmlAPI_ShadedRepresentation)
    writer.SetDeflection(0.1)

    path = tmp_path / "box.wrl"
    assert writer.Write(meshed_box, str(path), 2)
    status, text = writer.Write(meshed_box, 2)
    assert status and text == path.read_text()


def test_a_document_is_written_with_its_colour(tmp_path, meshed_box, quiet_messenger):
    writer = VrmlAPI_Writer()
    path = tmp_path / "doc.wrl"
    assert writer.WriteDoc(_document(meshed_box), str(path), 1.0)
    status, text = writer.WriteDoc(_document(meshed_box), 1.0)
    assert status and text == path.read_text()
    assert "diffuseColor" in text                                 # the material carries the document's colour


def test_the_caf_reader_reads_a_file_and_bytes(tmp_path, meshed_box, quiet_messenger):
    """VrmlAPI_CafReader derives from RWMesh_CafReader, so it inherits the binary-stream Perform (2b): VRML is text,
    but the path overload opens the file std::ios_base::binary and hands that stream on, exactly as OBJ does."""
    assert "theStream: typing.BinaryIO" in VrmlAPI_CafReader.Perform.__doc__

    path = tmp_path / "doc.wrl"
    VrmlAPI_Writer().WriteDoc(_document(meshed_box), str(path), 1.0)

    app = XCAFApp_Application.GetApplication()
    reader = VrmlAPI_CafReader()
    reader.SetDocument(app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF")))
    assert reader.Perform(TCollection_AsciiString(str(path)), Message_ProgressRange())
    shape = reader.SingleShape()
    assert shape.ShapeType() == TopAbs_COMPOUND                   # a mesh, not the original solid
    assert sum(1 for _ in TopExp_Explorer(shape, TopAbs_FACE)) == 6

    from_memory = VrmlAPI_CafReader()
    from_memory.SetDocument(app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF")))
    assert from_memory.Perform(io.BytesIO(path.read_bytes()), Message_ProgressRange(), TCollection_AsciiString(str(path)))


def test_the_vrml_1_nodes_print_themselves():
    """The `Vrml` package is VRML 1.0: 40 node classes whose only output is Print(Standard_OStream&), which returns
    the stream for chaining -- R-STREAM-OUT drops the chained result and returns the text (2b)."""
    assert Vrml_Cone().Print() == "Cone {\n}\n"
    material = Vrml_Material().Print()
    assert material.startswith("Material {") and "ambientColor" in material and "diffuseColor" in material


def test_a_shape_becomes_a_vrml_2_scene(meshed_box):
    """VrmlData is the VRML 2.0 DOM. A scene is filled from shapes with VrmlData_ShapeConvert and converts back to a
    shape -- what it cannot do is parse or serialise VRML text, which is the operator<< pair (2d)."""
    scene = VrmlData_Scene()
    assert scene.Dump().startswith(" ===== Diagnostic Dump of a Scene (1 nodes)")

    convert = VrmlData_ShapeConvert(scene, 1.0)
    convert.AddShape(meshed_box, "box")
    convert.Convert(True, False, 0.01)
    assert "28 nodes" in scene.Dump().splitlines()[0]
    assert not scene.GetShape(AppearanceMap()).IsNull()


def test_the_scene_stream_operators_are_not_bound():
    """`VrmlData_Scene& operator<<(Standard_IStream&)` is the only VRML 2.0 parser and the friend
    `operator<<(Standard_OStream&, const VrmlData_Scene&)` the only serialiser; neither has a Python spelling (2d).
    VrmlAPI covers both directions, which is what the rest of this file exercises."""
    assert not hasattr(VrmlData_Scene, "__lshift__")
    lines = REPORT.read_text().splitlines()
    assert any("VrmlData_Scene::operator<<(Standard_IStream &): operator has no Python equivalent" in line for line in lines)
    assert any("friend operator<<(Standard_OStream &, const VrmlData_Scene &): iostream type" in line for line in lines)


def test_the_drawer_and_the_de_provider(tmp_path, meshed_box, quiet_messenger):
    assert VrmlConverter_Drawer().MaximalChordialDeviation() == 0.1

    node = DEVRML_ConfigurationNode()
    assert node.GetFormat().ToCString() == "VRML" and node.GetVendor().ToCString() == "OCC"
    assert [extension.ToCString() for extension in node.GetExtensions()] == ["vrml", "wrl"]

    path = tmp_path / "prov.wrl"
    provider = DEVRML_Provider(node)
    assert provider.Write(TCollection_AsciiString(str(path)), _document(meshed_box), Message_ProgressRange())
    assert path.read_text().startswith("#VRML")


def test_report_is_twenty_seven_lines():
    """All 27 are in VrmlData, the VRML 2.0 DOM: the index arrays it hands out as `const int*&` into its own memory,
    VrmlData_InBuffer (which *holds* the istream it parses from), the two stream operators, and
    VrmlData_IndexedFaceSet::GetNormal -- declared Standard_EXPORT at VrmlData_IndexedFaceSet.hxx:180 and defined
    nowhere in OCCT, which the nm check caught before the linker did."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert len(lines) == 27
    assert all(line.split("\t")[1] == "VrmlData" for line in lines)
    assert sum(line.startswith("raw-pointer") for line in lines) == 18
    assert any("VrmlData_IndexedFaceSet::GetNormal" in line and line.startswith("undefined") for line in lines)
