"""Generated bindings for TKDESTL (DataExchange: StlAPI, RWStl, DESTL): STL import and export. build123d writes STL
through StlAPI_Writer; RWStl reads and writes the Poly_Triangulation directly, in both the ASCII and the binary
flavour of the format -- the one package so far whose streams are partly text and partly bytes."""
import importlib
import io
from pathlib import Path

import pytest

from conftest import report

from nanocct import Message
from nanocct.BRepMesh import BRepMesh_IncrementalMesh
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.DESTL import DESTL_ConfigurationNode, DESTL_Provider
from nanocct.Poly import Poly_Triangulation
from nanocct.RWStl import RWStl, RWStl_Reader
from nanocct.StlAPI import StlAPI_Reader, StlAPI_Writer
from nanocct.TopAbs import TopAbs_FACE
from nanocct.TopExp import TopExp_Explorer
from nanocct.TopoDS import TopoDS_Shape

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDESTL" / "report.txt"


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
def meshed_box():
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    BRepMesh_IncrementalMesh(box, 0.1)                           # STL needs a triangulation
    return box


@pytest.mark.parametrize("pkg", ["StlAPI", "RWStl", "DESTL"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


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
    mesh = RWStl.ReadFile_s(str(path))
    assert isinstance(mesh, Poly_Triangulation)
    assert (mesh.NbTriangles(), mesh.NbNodes()) == (12, 8)


def test_the_binary_flavour_is_bytes_and_the_ascii_one_is_str(tmp_path, meshed_box, quiet_messenger):
    """RWStl writes and reads both flavours of STL, so the package is mixed: WriteBinary/ReadBinaryStream/ReadStream
    and RWStl_Reader.ReadBinary/IsAscii are in overrides.toml [stream] binary_members, WriteAscii/ReadAsciiStream stay
    text (R-STREAM-OUT, R-STREAM-IN). ReadStream sniffs the format, so bytes is the superset there."""
    writer = StlAPI_Writer()
    writer.SetASCIIMode(False)
    path = tmp_path / "box.stl"
    writer.Write(meshed_box, str(path))
    mesh = RWStl.ReadFile_s(str(path))

    ok, data = RWStl.WriteBinary_s(mesh)
    assert ok and isinstance(data, bytes)
    assert data == path.read_bytes()                              # byte-identical to the file form
    ok, text = RWStl.WriteAscii_s(mesh)
    assert ok and isinstance(text, str) and text.startswith("solid ")

    assert RWStl.ReadBinaryStream_s(io.BytesIO(data)).NbTriangles() == 12
    assert RWStl.ReadAsciiStream_s(io.StringIO(text)).NbTriangles() == 12
    assert RWStl.ReadStream_s(io.BytesIO(data)).NbTriangles() == 12              # the sniffing overload: binary ...
    assert RWStl.ReadStream_s(io.BytesIO(text.encode())).NbTriangles() == 12     # ... and ASCII, both as bytes
    with pytest.raises(TypeError):
        RWStl.ReadBinaryStream_s(io.StringIO(text))                 # a text file-like falls through
    assert "theStream: typing.BinaryIO" in RWStl_Reader.ReadBinary.__doc__


def test_the_de_provider_and_the_abstract_reader():
    assert DESTL_ConfigurationNode().GetFormat().ToCString() == "STL"
    provider = DESTL_Provider()
    assert provider.GetFormat().ToCString() == "STL" and provider.GetVendor().ToCString() == "OCC"
    # RWStl_Reader is abstract (AddNode/AddTriangle are pure virtual), so clang emits no complete-object constructor
    with pytest.raises(TypeError, match="no constructor defined"):
        RWStl_Reader()


def test_report_is_the_ascii_reader_and_the_ctor():
    _, portable, undefined, _ = report("TKDESTL")
    assert len(portable) == 1
    assert portable[0].startswith("std\tRWStl\tRWStl_Reader::ReadAscii") and "std::fpos" in portable[0]
    assert all("RWStl_Reader::RWStl_Reader()" in line for line in undefined)
