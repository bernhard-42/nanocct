"""Generated bindings for TKDEIGES (DataExchange, 20 packages): IGES import and export -- IGESControl_Reader/Writer
and the IGES entity classes (IGESGeom, IGESSolid, IGESDimen, IGESDraw, ...), the same shape as TKDESTEP one toolkit
earlier. IGES writes in memory but only reads from a file: OCCT implements ReadStream for STEP alone."""
import importlib
import io
from pathlib import Path

import pytest

from nanoocp import Message
from nanoocp.BRepGProp import BRepGProp
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.GProp import GProp_GProps
from nanoocp.IFSelect import IFSelect_RetDone, IFSelect_RetFail
from nanoocp.IGESCAFControl import IGESCAFControl_Reader, IGESCAFControl_Writer
from nanoocp.IGESControl import IGESControl_Controller, IGESControl_Reader, IGESControl_Writer
from nanoocp.IGESGeom import IGESGeom_CircularArc, IGESGeom_Point
from nanoocp.IGESSolid import IGESSolid_Block
from nanoocp.Interface import Interface_Static
from nanoocp.TCollection import TCollection_ExtendedString
from nanoocp.TopAbs import TopAbs_FACE, TopAbs_SOLID
from nanoocp.TopExp import TopExp_Explorer
from nanoocp.XCAFApp import XCAFApp_Application
from nanoocp.XCAFDoc import XCAFDoc_DocumentTool
from nanoocp.gp import gp_XYZ

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDEIGES" / "report.txt"
PACKAGES = ["IGESControl", "IGESCAFControl", "IGESData", "IGESBasic", "IGESGeom", "IGESSolid", "IGESDimen",
            "IGESDraw", "IGESGraph", "IGESDefs", "IGESAppli", "IGESSelect", "IGESToBRep", "GeomToIGES",
            "Geom2dToIGES", "BRepToIGES", "BRepToIGESBRep", "IGESConvGeom", "DEIGES"]


@pytest.fixture(scope="module", autouse=True)
def controller():
    IGESControl_Controller.Init()


@pytest.fixture
def quiet_messenger():
    printers = list(Message.Message.DefaultMessenger().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


def _volume(shape) -> float:
    properties = GProp_GProps()
    BRepGProp.VolumeProperties(shape, properties)
    return properties.Mass()


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_a_solid_round_trips_in_brep_mode(tmp_path, quiet_messenger):
    """write.iges.brep.mode = 1 keeps the solid; the IGES default (0) writes trimmed surfaces."""
    assert Interface_Static.IsPresent("write.iges.brep.mode")
    assert Interface_Static.SetIVal("write.iges.brep.mode", 1)
    writer = IGESControl_Writer("MM", 1)
    assert writer.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    writer.ComputeModel()
    path = tmp_path / "box.igs"
    assert writer.Write(str(path))
    lines = path.read_text().splitlines()
    assert all(len(line) == 80 for line in lines[:5])            # IGES is a fixed 80-column format
    assert lines[0][72] == "S"                                   # section letter in column 73

    reader = IGESControl_Reader()
    assert reader.ReadFile(str(path)) == IFSelect_RetDone
    assert reader.NbRootsForTransfer() == 1
    assert reader.TransferRoots() == 1
    shape = reader.OneShape()
    assert shape.ShapeType() == TopAbs_SOLID
    assert _volume(shape) == pytest.approx(6.0)


def test_faces_mode_writes_surfaces(tmp_path, quiet_messenger):
    assert Interface_Static.SetIVal("write.iges.brep.mode", 0)
    writer = IGESControl_Writer("MM", 0)
    writer.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    writer.ComputeModel()
    path = tmp_path / "faces.igs"
    assert writer.Write(str(path))
    reader = IGESControl_Reader()
    assert reader.ReadFile(str(path)) == IFSelect_RetDone
    reader.TransferRoots()
    assert sum(1 for _ in TopExp_Explorer(reader.OneShape(), TopAbs_FACE)) == 6
    Interface_Static.SetIVal("write.iges.brep.mode", 1)


def test_the_writer_streams_but_the_reader_does_not(tmp_path, quiet_messenger):
    """IGESControl_Writer::Write(ostream&, fnes) is the (bool, str) overload (R-STREAM-OUT) and produces exactly the
    file's bytes. Reading back in memory is not possible: IFSelect_WorkLibrary::ReadStream is a stub returning 1
    (IFSelect_WorkLibrary.cxx:118) and only StepSelect_WorkLibrary overrides it, so IGES always answers RetFail --
    OCCT behaviour, not an omission."""
    Interface_Static.SetIVal("write.iges.brep.mode", 1)
    writer = IGESControl_Writer("MM", 1)
    writer.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    writer.ComputeModel()
    path = tmp_path / "both.igs"
    writer.Write(str(path))
    ok, text = writer.Write()                                    # the ostream& overload
    assert ok and isinstance(text, str)
    assert text == path.read_text()                              # byte-identical to the file form
    assert IGESControl_Reader().ReadStream("in-memory", io.StringIO(text)) == IFSelect_RetFail
    with open(path) as handle:                                   # not the caster: a real file fails the same way
        assert IGESControl_Reader().ReadStream("from-file", handle) == IFSelect_RetFail


def test_the_reader_exposes_its_model(tmp_path, quiet_messenger):
    writer = IGESControl_Writer("MM", 1)
    writer.AddShape(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape())
    writer.ComputeModel()
    path = tmp_path / "cube.igs"
    writer.Write(str(path))
    reader = IGESControl_Reader()
    reader.ReadFile(str(path))
    session = reader.WS()
    assert type(session.NormAdaptor()).__name__ == "IGESControl_Controller"
    assert session.Model().NbEntities() > 10
    assert isinstance(reader.PrintCheckLoad__str(False, 0), str)


def test_an_xcaf_document_round_trips(tmp_path, quiet_messenger):
    app = XCAFApp_Application.GetApplication()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    shapes = XCAFDoc_DocumentTool.ShapeTool(doc.Main())
    shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)
    writer = IGESCAFControl_Writer()
    assert writer.Transfer(doc)
    path = tmp_path / "doc.igs"
    assert writer.Write(str(path))
    reloaded = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    reader = IGESCAFControl_Reader()
    assert reader.ReadFile(str(path)) == IFSelect_RetDone
    assert reader.Transfer(reloaded)
    assert _volume(XCAFDoc_DocumentTool.ShapeTool(reloaded.Main()).GetShape(
        reloaded.Main().FindChild(1).FindChild(1))) == pytest.approx(6.0)


def test_the_entity_classes():
    point = IGESGeom_Point()
    point.Init(gp_XYZ(1.0, 2.0, 3.0), None)
    assert point.Value().X() == 1.0 and point.DynamicType().Name() == "IGESGeom_Point"
    assert IGESGeom_CircularArc().DynamicType().Name() == "IGESGeom_CircularArc"
    assert IGESSolid_Block().DynamicType().Name() == "IGESSolid_Block"


def test_report_categories():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    counts: dict[str, int] = {}
    for line in lines:
        counts[line.split("\t")[0]] = counts.get(line.split("\t")[0], 0) + 1
    assert counts == {"raw-pointer": 6, "template": 3, "rvalue": 2, "undefined": 2}
    assert len(lines) == 13                                      # 455 classes, 4 127 methods bound
    # DEIGES_Provider::Read/Write keep their work session (overrides.toml [inout] "DE*_Provider::Read"), so none of
    # the four overloads collides into Read__XSControl_WorkSession
    assert not any("XSControl_WorkSession" in line for line in lines)
