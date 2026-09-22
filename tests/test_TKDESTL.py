"""Generated bindings for TKDESTL (DataExchange: StlAPI, RWStl, DESTL): STL import and export. build123d writes STL
through StlAPI_Writer; RWStl reads and writes the Poly_Triangulation directly, in both the ASCII and the binary
flavour of the format -- the one package so far whose streams are partly text and partly bytes."""
import importlib
import io
from pathlib import Path

import pytest

from nanoocp import Message
from nanoocp.BRepMesh import BRepMesh_IncrementalMesh
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.DESTL import DESTL_ConfigurationNode, DESTL_Provider
from nanoocp.Poly import Poly_Triangulation
from nanoocp.RWStl import RWStl, RWStl_Reader
from nanoocp.StlAPI import StlAPI_Reader, StlAPI_Writer
from nanoocp.TopAbs import TopAbs_FACE
from nanoocp.TopExp import TopExp_Explorer
from nanoocp.TopoDS import TopoDS_Shape

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDESTL" / "report.txt"


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
    BRepMesh_IncrementalMesh(box, 0.1)                           # STL needs a triangulation
    return box


@pytest.mark.parametrize("pkg", ["StlAPI", "RWStl", "DESTL"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_stl_api_writer_is_build123d_s_call(tmp_path, meshed_box, quiet_messenger):
    writer = StlAPI_Writer()
    assert writer.ASCIIMode() is True                             # OCCT's default
    ascii_path = tmp_path / "box_ascii.stl"
    assert writer.Write(meshed_box, str(ascii_path))
    assert ascii_path.read_text().startswith("solid ")
    writer.SetASCIIMode(False)
    binary_path = tmp_path / "box_binary.stl"
    assert writer.Write(meshed_box, str(binary_path))
    assert binary_path.read_bytes()[:3] == b"STL" and binary_path.stat().st_size == 684

    shape = TopoDS_Shape()
    assert StlAPI_Reader().Read(shape, str(ascii_path))
    assert sum(1 for _ in TopExp_Explorer(shape, TopAbs_FACE)) == 12


def test_rwstl_reads_and_writes_a_triangulation(tmp_path, meshed_box, quiet_messenger):
    writer = StlAPI_Writer()
    writer.SetASCIIMode(False)
    path = tmp_path / "box.stl"
    writer.Write(meshed_box, str(path))
    mesh = RWStl.ReadFile(str(path))
    assert isinstance(mesh, Poly_Triangulation)
    assert (mesh.NbTriangles(), mesh.NbNodes()) == (12, 8)


def test_the_binary_flavour_is_bytes_and_the_ascii_one_is_str(tmp_path, meshed_box, quiet_messenger):
    """RWStl writes and reads both flavours of STL, so the package is mixed: WriteBinary/ReadBinaryStream/ReadStream
    and RWStl_Reader.ReadBinary/IsAscii are in overrides.toml [stream] binary_members, WriteAscii/ReadAsciiStream stay
    text (R-STREAM-OUT/IN). ReadStream sniffs the format, so bytes is the superset there."""
    writer = StlAPI_Writer()
    writer.SetASCIIMode(False)
    path = tmp_path / "box.stl"
    writer.Write(meshed_box, str(path))
    mesh = RWStl.ReadFile(str(path))

    ok, data = RWStl.WriteBinary(mesh)
    assert ok and isinstance(data, bytes)
    assert data == path.read_bytes()                              # byte-identical to the file form
    ok, text = RWStl.WriteAscii(mesh)
    assert ok and isinstance(text, str) and text.startswith("solid ")

    assert RWStl.ReadBinaryStream(io.BytesIO(data)).NbTriangles() == 12
    assert RWStl.ReadAsciiStream(io.StringIO(text)).NbTriangles() == 12
    assert RWStl.ReadStream(io.BytesIO(data)).NbTriangles() == 12              # the sniffing overload: binary ...
    assert RWStl.ReadStream(io.BytesIO(text.encode())).NbTriangles() == 12     # ... and ASCII, both as bytes
    with pytest.raises(TypeError):
        RWStl.ReadBinaryStream(io.StringIO(text))                 # a text file-like falls through
    assert "theStream: typing.BinaryIO" in RWStl_Reader.ReadBinary.__doc__


def test_the_de_provider_and_the_abstract_reader():
    assert DESTL_ConfigurationNode().GetFormat().ToCString() == "STL"
    provider = DESTL_Provider()
    assert provider.GetFormat().ToCString() == "STL" and provider.GetVendor().ToCString() == "OCC"
    # RWStl_Reader is abstract (AddNode/AddTriangle are pure virtual), so clang emits no complete-object constructor
    with pytest.raises(TypeError, match="no constructor defined"):
        RWStl_Reader()


def test_report_is_two_lines():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert len(lines) == 2
    assert lines[0].startswith("std\tRWStl\tRWStl_Reader::ReadAscii") and "std::fpos" in lines[0]
    assert lines[1].startswith("undefined\tRWStl\tRWStl_Reader::RWStl_Reader()")
