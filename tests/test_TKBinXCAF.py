"""Generated bindings for TKBinXCAF (DataExchange: BinXCAFDrivers, BinMXCAFDoc): the binary OCAF format for XCAF
documents. TKBin already round-trips a plain document through bytes; this toolkit adds the attribute drivers for the
XCAF attributes -- colours, assemblies, materials, dimensions and tolerances, notes -- so a whole product structure
survives the trip."""
import importlib
import io
from pathlib import Path

import pytest

from nanocct import Message
from nanocct.BinMXCAFDoc import (BinMXCAFDoc_AssemblyItemRefDriver, BinMXCAFDoc_CentroidDriver, BinMXCAFDoc_ColorDriver,
                                 BinMXCAFDoc_DatumDriver, BinMXCAFDoc_GraphNodeDriver, BinMXCAFDoc_LocationDriver)
from nanocct.BinXCAFDrivers import (BinXCAFDrivers, BinXCAFDrivers_DocumentRetrievalDriver,
                                    BinXCAFDrivers_DocumentStorageDriver)
from nanocct.BRepGProp import BRepGProp
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.GProp import GProp_GProps
from nanocct.NCollection import NCollection_Sequence
from nanocct.PCDM import PCDM_ReadWriter, PCDM_RS_OK, PCDM_SS_OK
from nanocct.Quantity import Quantity_Color, Quantity_NOC_RED
from nanocct.Standard import Standard_Failure, Standard_GUID, Standard_OutOfRange
from nanocct.TCollection import TCollection_ExtendedString
from nanocct.TDataStd import TDataStd_Name
from nanocct.TDF import TDF_Label
from nanocct.TopAbs import TopAbs_COMPOUND, TopAbs_SOLID
from nanocct.TopLoc import TopLoc_Location
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDoc import XCAFDoc_ColorSurf, XCAFDoc_DocumentTool
from nanocct.gp import gp_Trsf, gp_Vec

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKBinXCAF" / "report.txt"
STORAGE_GUID = "a78ff496-a779-11d5-aab4-0050044b1af1"      # BinXCAFDrivers.cxx:27-28
RETRIEVAL_GUID = "a78ff497-a779-11d5-aab4-0050044b1af1"


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
def application():
    app = XCAFApp_Application.GetApplication_s()
    BinXCAFDrivers.DefineFormat_s(app)                              # build123d spells it BinXCAFDrivers.DefineFormat_s
    return app


def _assembly_document(app):
    """A box with a name and a colour, referenced once from an assembly 10 mm along X."""
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    part = shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)
    TDataStd_Name.Set_s(part, TCollection_ExtendedString("the box"))
    XCAFDoc_DocumentTool.ColorTool_s(doc.Main()).SetColor(part, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorSurf)

    assembly = shapes.NewShape()
    TDataStd_Name.Set_s(assembly, TCollection_ExtendedString("assembly"))
    moved = gp_Trsf()
    moved.SetTranslation(gp_Vec(10.0, 0.0, 0.0))
    shapes.AddComponent(assembly, part, TopLoc_Location(moved))
    return doc


@pytest.mark.parametrize("pkg", ["BinXCAFDrivers", "BinMXCAFDoc"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_a_product_structure_round_trips_through_bytes(application):
    """The milestone of this toolkit: SaveAs(doc) -> (status, bytes) and Open(io.BytesIO(data)) keep the geometry,
    the colour and the assembly structure, not just the labels."""
    status, data = application.SaveAs(_assembly_document(application))
    assert status == PCDM_SS_OK
    assert data[:7] == b"BINFILE"

    read_status, reloaded = application.Open(io.BytesIO(data))
    assert read_status == PCDM_RS_OK
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(reloaded.Main())
    colors = XCAFDoc_DocumentTool.ColorTool_s(reloaded.Main())

    labels = NCollection_Sequence[TDF_Label]()
    shapes.GetShapes(labels)
    assert labels.Length() == 2                                   # the part and the assembly

    part, assembly = labels.Value(1), labels.Value(2)
    solid = shapes.GetShape_s(part)
    assert solid.ShapeType() == TopAbs_SOLID
    props = GProp_GProps()
    BRepGProp.VolumeProperties_s(solid, props)
    assert props.Mass() == pytest.approx(6.0)                     # 1 x 2 x 3

    colour = Quantity_Color()
    assert colors.GetColor(solid, XCAFDoc_ColorSurf, colour) and colour.Name() == Quantity_NOC_RED
    assert shapes.IsAssembly_s(assembly) and shapes.GetShape_s(assembly).ShapeType() == TopAbs_COMPOUND


def test_the_file_form_is_the_same_bytes_and_needs_the_xbf_extension(tmp_path, application, quiet_messenger):
    """OCCT semantics worth knowing: unlike BinLOcaf/BinOcaf, which append their .cbfl/.cbf, BinXCAF requires the
    extension on the path -- without it SaveAs reports "folder  does not exist" and writes nothing.

    What it does NOT do is return a usable status: it leaves the status variable uninitialised, so the value that
    reaches Python is whatever was on the stack. This test used to assert the ValueError that PCDM_StoreStatus
    raises for an out-of-range value, which passed on macOS, on host Linux and on Windows and failed in the
    manylinux container, where the first call happened to land on PCDM_SS_UserBreak -- a valid enumerator.
    Measured 2026-09-24: eight identical calls gave PCDM_SS_UserBreak then 2821076856 seven times in the
    container, 2430944776 then 4294967295 on the host. The file not being written is the only defined outcome,
    so that is what is asserted; the status is deliberately not inspected."""
    doc = _assembly_document(application)
    path = tmp_path / "product.xbf"
    assert application.SaveAs(doc, TCollection_ExtendedString(str(path))) == PCDM_SS_OK
    assert path.read_bytes() == application.SaveAs(doc)[1]

    no_extension = tmp_path / "no-extension"
    try:
        application.SaveAs(doc, TCollection_ExtendedString(str(no_extension)))
    except ValueError:
        pass                                    # the uninitialised status was out of the enum's range this time
    except Standard_OutOfRange:
        # Windows only, and only when a *directory* on the path has a dot (C:\...\.agent-scratch\tmp\...):
        # TDocStd_PathParser::Parse takes the extension from the last '.' of the whole path, and its _WIN32 branch
        # then splits out of range (TDocStd_PathParser.cxx:29-52). The Unix branch copes; measured 2026-09-25.
        pass
    assert not no_extension.exists(), "BinXCAF wrote a file for a path without the .xbf extension"


def test_the_format_is_detected_from_the_bytes(application):
    """PCDM_ReadWriter.FileFormat_s sniffs the format out of the document stream, as it does for BinOcaf and XmlOcaf."""
    _, data = application.SaveAs(_assembly_document(application))
    fmt, _storage = PCDM_ReadWriter.FileFormat_s(io.BytesIO(data))
    assert fmt.ToExtString() == "BinXCAF"


def test_the_drivers_and_the_factory(quiet_messenger):
    assert BinXCAFDrivers_DocumentStorageDriver() is not None
    assert BinXCAFDrivers_DocumentRetrievalDriver() is not None
    messenger = Message.Message.DefaultMessenger_s()
    assert BinXCAFDrivers.AttributeDrivers_s(messenger) is not None

    storage = BinXCAFDrivers.Factory_s(Standard_GUID(STORAGE_GUID))
    retrieval = BinXCAFDrivers.Factory_s(Standard_GUID(RETRIEVAL_GUID))
    assert storage.DynamicType().Name() == "BinXCAFDrivers_DocumentStorageDriver"
    assert retrieval.DynamicType().Name() == "BinXCAFDrivers_DocumentRetrievalDriver"
    with pytest.raises(Standard_Failure, match="unknown GUID"):
        BinXCAFDrivers.Factory_s(Standard_GUID("ad696002-5b34-11d1-b5ba-00a0c9064368"))


@pytest.mark.parametrize("driver, attribute", [
    (BinMXCAFDoc_AssemblyItemRefDriver, "XCAFDoc_AssemblyItemRef"),
    (BinMXCAFDoc_CentroidDriver, "XCAFDoc_Centroid"),
    (BinMXCAFDoc_ColorDriver, "XCAFDoc_Color"),
    (BinMXCAFDoc_DatumDriver, "XCAFDoc_Datum"),
    (BinMXCAFDoc_GraphNodeDriver, "XCAFDoc_GraphNode"),
    (BinMXCAFDoc_LocationDriver, "XCAFDoc_Location"),
])
def test_each_attribute_driver_names_the_attribute_it_persists(driver, attribute):
    """The 15 BinMXCAFDoc drivers are what makes the round trip above carry XCAF's attributes; each one declares the
    attribute type it reads and writes."""
    assert driver(Message.Message.DefaultMessenger_s()).SourceType().Name() == attribute


def test_report_is_only_the_drivers_without_a_copy():
    """Two packages, 18 classes, nothing unbound -- the drivers only override AttributeDrivers, and Write/Read come
    from BinDrivers, which TKBin already binds. Two have no copy constructor: their BinObjMgt_Persistent frees its data
    blocks (R-COPY)."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert [line.split("\t")[2].split(":")[0] for line in lines] == ["BinXCAFDrivers_DocumentRetrievalDriver", "BinXCAFDrivers_DocumentStorageDriver"]
    assert all(line.startswith("copy\t") for line in lines)
