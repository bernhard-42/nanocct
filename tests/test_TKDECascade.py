"""Generated bindings for TKDECascade (DataExchange: DEBREP, DEXCAF): the DE providers for OCCT's *own* formats, and
the last toolkit in scope. With them `DE_Wrapper` dispatches `.brep` and the OCAF documents by extension, next to
STEP, IGES and the mesh formats -- OCCT's native formats stop being the exception.

It is also the one toolkit that links libraries nanocct does not bind: TKStd, TKStdL, TKTObj, TKBinTObj and
TKXmlTObj are needed by the providers' implementations but named in no header, so they come along on the link line
and have no Python module (8.15)."""
import importlib
from pathlib import Path

import pytest

from nanocct.BRepGProp import BRepGProp
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.DE import DE_Wrapper
from nanocct.DEBREP import DEBREP_ConfigurationNode, DEBREP_Provider
from nanocct.DEXCAF import DEXCAF_ConfigurationNode, DEXCAF_Provider
from nanocct.GProp import GProp_GProps
from nanocct.Message import Message_ProgressRange
from nanocct.NCollection import NCollection_Sequence
from nanocct.Quantity import Quantity_Color, Quantity_NOC_RED
from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString
from nanocct.TDF import TDF_Label
from nanocct.TopoDS import TopoDS_Shape
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDoc import XCAFDoc_ColorSurf, XCAFDoc_DocumentTool

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDECascade" / "report.txt"


@pytest.fixture
def box():
    return BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()


def _volume(shape):
    props = GProp_GProps()
    BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def _document(box):
    app = XCAFApp_Application.GetApplication_s()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    label = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main()).AddShape(box, False)
    XCAFDoc_DocumentTool.ColorTool_s(doc.Main()).SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorSurf)
    return doc


@pytest.mark.parametrize("pkg", ["DEBREP", "DEXCAF", "DEBRepCascade", "DEXCAFCascade"])
def test_every_package_imports(pkg):
    """DEBRepCascade and DEXCAFCascade hold no classes -- they are OCCT's alias packages -- but still get a shim."""
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_the_configuration_nodes():
    brep, xcaf = DEBREP_ConfigurationNode(), DEXCAF_ConfigurationNode()
    assert (brep.GetFormat().ToCString(), brep.GetVendor().ToCString()) == ("BREP", "OCC")
    assert (xcaf.GetFormat().ToCString(), xcaf.GetVendor().ToCString()) == ("XCAF", "OCC")
    assert [e.ToCString() for e in brep.GetExtensions()] == ["brep"]
    assert [e.ToCString() for e in xcaf.GetExtensions()] == ["xbf"]
    for node in (brep, xcaf):
        assert node.IsImportSupported() and node.IsExportSupported()


def test_a_shape_round_trips_through_brep(tmp_path, box):
    path = tmp_path / "box.brep"
    provider = DEBREP_Provider(DEBREP_ConfigurationNode())
    assert provider.Write(TCollection_AsciiString(str(path)), box, Message_ProgressRange())

    reloaded = TopoDS_Shape()
    assert provider.Read(TCollection_AsciiString(str(path)), reloaded, Message_ProgressRange())
    assert _volume(reloaded) == pytest.approx(6.0)


def test_the_brep_flavour_is_binary_by_default(tmp_path, box):
    """DEBREP_ConfigurationNode's InternalParameters.WriteBinary is True (DEBREP_ConfigurationNode.hxx:91), so the
    provider writes the *binary* BRep format -- unlike BRepTools.Write_s, which writes ASCII. The struct is reachable,
    so the flavour is a flag, not a rebuild."""
    node = DEBREP_ConfigurationNode()
    assert node.InternalParameters.WriteBinary is True
    binary = tmp_path / "binary.brep"
    DEBREP_Provider(node).Write(TCollection_AsciiString(str(binary)), box, Message_ProgressRange())
    assert binary.read_bytes().startswith(b"\nOpen CASCADE Topology")

    node.InternalParameters.WriteBinary = False
    ascii_path = tmp_path / "ascii.brep"
    DEBREP_Provider(node).Write(TCollection_AsciiString(str(ascii_path)), box, Message_ProgressRange())
    assert ascii_path.read_text().splitlines()[0] == "DBRep_DrawableShape"


def test_the_wrapper_dispatches_shapes_by_extension(tmp_path, box):
    """The point of the toolkit: one DE_Wrapper call handles OCCT's own formats, the same way it handles STEP."""
    wrapper = DE_Wrapper()
    assert wrapper.Bind(DEBREP_ConfigurationNode())

    through_wrapper = tmp_path / "wrapper.brep"
    assert wrapper.Write(TCollection_AsciiString(str(through_wrapper)), box)

    direct = tmp_path / "direct.brep"
    DEBREP_Provider(DEBREP_ConfigurationNode()).Write(TCollection_AsciiString(str(direct)), box, Message_ProgressRange())
    assert through_wrapper.read_bytes() == direct.read_bytes()

    reloaded = TopoDS_Shape()
    assert wrapper.Read(TCollection_AsciiString(str(through_wrapper)), reloaded)
    assert _volume(reloaded) == pytest.approx(6.0)


def test_the_wrapper_dispatches_documents(tmp_path, box):
    wrapper = DE_Wrapper()
    assert wrapper.Bind(DEXCAF_ConfigurationNode())

    path = tmp_path / "doc.xbf"
    assert wrapper.Write(TCollection_AsciiString(str(path)), _document(box))
    assert path.read_bytes()[:7] == b"BINFILE"                    # the BinXCAF document of TKBinXCAF

    app = XCAFApp_Application.GetApplication_s()
    reloaded = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    assert wrapper.Read(TCollection_AsciiString(str(path)), reloaded)
    free = NCollection_Sequence[TDF_Label]()
    XCAFDoc_DocumentTool.ShapeTool_s(reloaded.Main()).GetFreeShapes(free)
    assert free.Length() == 1


def test_the_provider_is_reachable_through_the_wrapper(tmp_path, box):
    """FindProvider probes the file's *content*, not only its extension (DE_ValidationUtils reads the first bytes),
    so it answers False for a path that does not exist -- an extension alone is not a format."""
    wrapper = DE_Wrapper()
    wrapper.Bind(DEBREP_ConfigurationNode())
    assert wrapper.FindProvider(TCollection_AsciiString(str(tmp_path / "absent.brep")), True)[0] is False

    path = tmp_path / "box.brep"
    DEBREP_Provider(DEBREP_ConfigurationNode()).Write(TCollection_AsciiString(str(path)), box, Message_ProgressRange())
    found, provider = wrapper.FindProvider(TCollection_AsciiString(str(path)), True)
    assert found and provider.GetFormat().ToCString() == "BREP"


@pytest.mark.parametrize("package", ["StdDrivers", "StdLPersistent", "TObj", "BinTObjDrivers", "XmlTObjDrivers"])
def test_the_linked_but_unbound_toolkits_have_no_module(package):
    """8.15: TKStd, TKStdL, TKTObj, TKBinTObj and TKXmlTObj are in TKDECascade's EXTERNLIB because its .cxx files use
    them, but no type of theirs appears in a header, so they are linked and not bound. This is the link-vs-import
    distinction R-LINK rests on, seen from the other side."""
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module(f"nanocct.{package}")


def test_report_is_empty():
    assert [line for line in REPORT.read_text().splitlines() if not line.startswith("#")] == []
