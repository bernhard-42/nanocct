"""Generated bindings for TKDEPLY (DataExchange: RWPly, DEPLY): Stanford PLY, built on TKRWMesh like OBJ and glTF --
but write-only. OCCT 8.0.1 has no PLY reader (DEPLY_Provider overrides only Write), and its writer emits
`format ascii 1.0` (RWPly_PlyWriterContext.cxx:154-155), so the ASCII/binary stream question the mesh formats keep
asking has no second flavour to answer for here."""
import importlib
from pathlib import Path

import pytest

from nanocct import Message
from nanocct.BRepMesh import BRepMesh_IncrementalMesh
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.BVH import BVH_Vec2f, BVH_Vec3i, BVH_Vec4i
from nanocct.DEPLY import DEPLY_ConfigurationNode, DEPLY_Provider
from nanocct.Quantity import NCollection_Vec3__float as Vec3f          # Graphic3d_Vec3 is a pre-8.0 alias, not bound
from nanocct.Graphic3d import NCollection_Vec4__unsigned_char as Vec4ub
from nanocct.Message import Message_ProgressRange
from nanocct.NCollection import NCollection_IndexedDataMap
from nanocct.Quantity import Quantity_Color, Quantity_NOC_RED
from nanocct.RWPly import RWPly_CafWriter, RWPly_PlyWriterContext
from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDoc import XCAFDoc_ColorGen, XCAFDoc_DocumentTool
from nanocct.gp import gp_Pnt

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDEPLY" / "report.txt"
FileInfo = NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString]


@pytest.fixture
def quiet_messenger():
    printers = list(Message.Message.DefaultMessenger_s().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


def _document():
    app = XCAFApp_Application.GetApplication_s()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    BRepMesh_IncrementalMesh(box, 0.1)                            # PLY exports triangulations
    label = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main()).AddShape(box, False)
    XCAFDoc_DocumentTool.ColorTool_s(doc.Main()).SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorGen)
    return doc


@pytest.mark.parametrize("pkg", ["RWPly", "DEPLY"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_the_caf_writer_writes_an_ascii_ply(tmp_path, quiet_messenger):
    path = tmp_path / "box.ply"
    writer = RWPly_CafWriter(TCollection_AsciiString(str(path)))
    writer.SetNormals(True)
    writer.SetColors(True)
    assert writer.Perform(_document(), FileInfo(), Message_ProgressRange())

    lines = path.read_text().splitlines()
    assert lines[0] == "ply" and lines[1] == "format ascii 1.0"   # OCCT writes no binary PLY
    assert "element vertex 24" in lines and "element face 12" in lines
    assert writer.IsDoublePrecision() is False                    # float by default


def test_the_writer_context_writes_a_ply_by_hand(tmp_path):
    """RWPly_PlyWriterContext is the low-level writer the CafWriter drives, and the only way to put a triangulation
    that is not an XCAF document into a PLY. It was bound but unusable until 2026-09-23: Open's second parameter is a
    std::shared_ptr<std::ostream> defaulted to its own empty form, which took the whole method out (R-OPTIONAL-PTR),
    and every other member needs the stream Open creates."""
    path = tmp_path / "tri.ply"
    ctx = RWPly_PlyWriterContext()
    ctx.SetNormals(True)
    ctx.SetColors(True)
    assert ctx.Open(TCollection_AsciiString(str(path))) and ctx.IsOpened()
    assert ctx.WriteHeader(3, 1, FileInfo())

    normal, uv, red = Vec3f(0.0, 0.0, 1.0), BVH_Vec2f(0.0, 0.0), Vec4ub(255, 0, 0, 255)
    for point in (gp_Pnt(0.0, 0.0, 0.0), gp_Pnt(1.0, 0.0, 0.0), gp_Pnt(0.0, 1.0, 0.0)):
        assert ctx.WriteVertex(point, normal, uv, red)
    assert ctx.NbWrittenVertices() == 3
    assert ctx.WriteTriangle(BVH_Vec3i(1, 2, 3))
    assert ctx.Close()

    lines = path.read_text().splitlines()
    assert lines[:2] == ["ply", "format ascii 1.0"]
    assert "element vertex 3" in lines and "element face 1" in lines
    assert "property uchar red" in lines and "property float nx" in lines
    assert lines[-1] == "3 1 2 3"                                 # one triangle, three indices


def test_the_colour_parameter_is_a_bound_type(tmp_path):
    """NCollection_Vec4<uint8_t> reaches the bindings only as WriteVertex's `const&` parameter -- the case 6c did not
    instantiate until 2026-09-23, which made the method a TypeError for every argument list without any report line."""
    assert "theColor: nanocct.Graphic3d.NCollection_Vec4__unsigned_char" in RWPly_PlyWriterContext.WriteVertex.__doc__
    colour = Vec4ub(1, 2, 3, 4)           # NCollection_Vec4<unsigned char>
    assert (colour.x(), colour.y(), colour.z(), colour.w()) == (1, 2, 3, 4)


def test_the_writer_context_writes_quads(tmp_path):
    path = tmp_path / "quad.ply"
    ctx = RWPly_PlyWriterContext()
    assert ctx.Open(TCollection_AsciiString(str(path)))
    assert ctx.WriteHeader(4, 1, FileInfo())
    normal, uv, white = Vec3f(0.0, 0.0, 1.0), BVH_Vec2f(0.0, 0.0), Vec4ub(255, 255, 255, 255)
    for point in (gp_Pnt(0.0, 0.0, 0.0), gp_Pnt(1.0, 0.0, 0.0), gp_Pnt(1.0, 1.0, 0.0), gp_Pnt(0.0, 1.0, 0.0)):
        ctx.WriteVertex(point, normal, uv, white)
    assert ctx.WriteQuad(BVH_Vec4i(1, 2, 3, 4))
    assert ctx.Close()
    assert path.read_text().splitlines()[-1] == "4 1 2 3 4"


def test_the_de_provider_writes_but_cannot_read(tmp_path, quiet_messenger):
    """OCCT has no PLY reader: DEPLY_Provider overrides only Write, so Read falls through to DE_Provider's base, which
    reports "doesn't support read operation"."""
    node = DEPLY_ConfigurationNode()
    assert node.GetFormat().ToCString() == "PLY" and node.GetVendor().ToCString() == "OCC"
    assert [extension.ToCString() for extension in node.GetExtensions()] == ["ply"]

    path = tmp_path / "box.ply"
    provider = DEPLY_Provider(node)
    assert provider.Write(TCollection_AsciiString(str(path)), _document(), Message_ProgressRange())
    assert path.read_text().startswith("ply\n")

    app = XCAFApp_Application.GetApplication_s()
    empty = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    assert provider.Read(TCollection_AsciiString(str(path)), empty, Message_ProgressRange()) is False


def test_report_is_empty():
    """Two classes in RWPly and three in DEPLY, all fully bound: the fifth toolkit with an empty report (TKG2d,
    TKHelix, TKXMesh, TKBin) and the first since TKBin."""
    assert [line for line in REPORT.read_text().splitlines() if not line.startswith("#")] == []
