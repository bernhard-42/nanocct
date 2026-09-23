"""Generated bindings for TKXmlXCAF (DataExchange: XmlXCAFDrivers, XmlMXCAFDoc): the XML OCAF format for XCAF
documents, and the mirror of TKBinXCAF -- the same 14 attribute drivers under the same names, the same two driver
GUIDs bar one hex digit, the same product structure surviving the trip. The difference is the bytes: an XML document
`xml.etree` parses, instead of BINFILE."""
import importlib
import io
import xml.etree.ElementTree as ElementTree
from pathlib import Path

import pytest

from nanoocp import Message
from nanoocp.BRepGProp import BRepGProp
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.GProp import GProp_GProps
from nanoocp.NCollection import NCollection_Sequence
from nanoocp.PCDM import PCDM_ReadWriter, PCDM_RS_OK, PCDM_SS_OK
from nanoocp.Quantity import Quantity_Color, Quantity_NOC_RED
from nanoocp.Standard import Standard_Failure, Standard_GUID
from nanoocp.TCollection import TCollection_ExtendedString
from nanoocp.TDataStd import TDataStd_Name
from nanoocp.TDF import TDF_Label
from nanoocp.TopAbs import TopAbs_COMPOUND, TopAbs_SOLID
from nanoocp.TopLoc import TopLoc_Location
from nanoocp.XCAFApp import XCAFApp_Application
from nanoocp.XCAFDoc import XCAFDoc_ColorSurf, XCAFDoc_DocumentTool
from nanoocp.XmlMXCAFDoc import (XmlMXCAFDoc_AssemblyItemRefDriver, XmlMXCAFDoc_CentroidDriver, XmlMXCAFDoc_ColorDriver,
                                 XmlMXCAFDoc_DatumDriver, XmlMXCAFDoc_GraphNodeDriver, XmlMXCAFDoc_LocationDriver)
from nanoocp.XmlXCAFDrivers import (XmlXCAFDrivers, XmlXCAFDrivers_DocumentRetrievalDriver,
                                    XmlXCAFDrivers_DocumentStorageDriver)
from nanoocp.gp import gp_Trsf, gp_Vec

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKXmlXCAF" / "report.txt"
OCAF = "{http://www.opencascade.org/OCAF/XML}"
STORAGE_GUID = "f78ff496-a779-11d5-aab4-0050044b1af1"      # XmlXCAFDrivers.cxx:25-26 -- BinXCAF's, with an f for the a
RETRIEVAL_GUID = "f78ff497-a779-11d5-aab4-0050044b1af1"


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
def application():
    app = XCAFApp_Application.GetApplication()
    XmlXCAFDrivers.DefineFormat(app)                              # build123d spells it XmlXCAFDrivers.DefineFormat_s
    return app


def _assembly_document(app):
    """The same document TKBinXCAF's test saves: a named, coloured box referenced once from an assembly."""
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("XmlXCAF"))
    shapes = XCAFDoc_DocumentTool.ShapeTool(doc.Main())
    part = shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)
    TDataStd_Name.Set_s(part, TCollection_ExtendedString("the box"))
    XCAFDoc_DocumentTool.ColorTool(doc.Main()).SetColor(part, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorSurf)

    assembly = shapes.NewShape()
    TDataStd_Name.Set_s(assembly, TCollection_ExtendedString("assembly"))
    moved = gp_Trsf()
    moved.SetTranslation(gp_Vec(10.0, 0.0, 0.0))
    shapes.AddComponent(assembly, part, TopLoc_Location(moved))
    return doc


@pytest.mark.parametrize("pkg", ["XmlXCAFDrivers", "XmlMXCAFDoc"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_a_product_structure_round_trips_through_xml_bytes(application):
    status, data = application.SaveAs(_assembly_document(application))
    assert status == PCDM_SS_OK
    assert data.startswith(b'<?xml version="1.0" ')                # bytes whatever the format (2b), XML included

    read_status, reloaded = application.Open(io.BytesIO(data))
    assert read_status == PCDM_RS_OK
    shapes = XCAFDoc_DocumentTool.ShapeTool(reloaded.Main())
    colors = XCAFDoc_DocumentTool.ColorTool(reloaded.Main())

    labels = NCollection_Sequence[TDF_Label]()
    shapes.GetShapes(labels)
    assert labels.Length() == 2

    part, assembly = labels.Value(1), labels.Value(2)
    solid = shapes.GetShape(part)
    assert solid.ShapeType() == TopAbs_SOLID
    props = GProp_GProps()
    BRepGProp.VolumeProperties(solid, props)
    assert props.Mass() == pytest.approx(6.0)

    colour = Quantity_Color()
    assert colors.GetColor(solid, XCAFDoc_ColorSurf, colour) and colour.Name() == Quantity_NOC_RED
    assert shapes.IsAssembly(assembly) and shapes.GetShape(assembly).ShapeType() == TopAbs_COMPOUND


def test_the_bytes_are_an_ocaf_xml_document(application):
    _, data = application.SaveAs(_assembly_document(application))
    root = ElementTree.fromstring(data)
    assert root.tag == f"{OCAF}document"
    assert [child.tag for child in root][:4] == [f"{OCAF}info", f"{OCAF}comments", f"{OCAF}label", f"{OCAF}shapes"]


def test_the_file_form_is_the_same_bytes_and_needs_the_xml_extension(tmp_path, application, quiet_messenger):
    """The extension rule of TKBinXCAF holds here too: the XCAF formats want it on the path, unlike BinLOcaf/BinOcaf,
    which append their own."""
    doc = _assembly_document(application)
    path = tmp_path / "product.xml"
    assert application.SaveAs(doc, TCollection_ExtendedString(str(path))) == PCDM_SS_OK
    assert path.read_bytes() == application.SaveAs(doc)[1]

    with pytest.raises(ValueError, match="is not a valid PCDM_StoreStatus"):
        application.SaveAs(doc, TCollection_ExtendedString(str(tmp_path / "no-extension")))


def test_the_format_is_detected_from_the_bytes(application):
    _, data = application.SaveAs(_assembly_document(application))
    fmt, _storage = PCDM_ReadWriter.FileFormat(io.BytesIO(data))
    assert fmt.ToExtString() == "XmlXCAF"


def test_the_drivers_and_the_factory():
    """XmlXCAFDrivers has DefineFormat and Factory only -- no AttributeDrivers static, which BinXCAFDrivers does have.
    The table is reached through the storage/retrieval driver instead."""
    assert sorted(n for n in dir(XmlXCAFDrivers) if not n.startswith("_")) == ["DefineFormat", "Factory"]
    # the XML storage driver writes a copyright line into the document, so its constructor takes one
    assert XmlXCAFDrivers_DocumentStorageDriver(TCollection_ExtendedString("nanoOCP")) is not None
    assert XmlXCAFDrivers_DocumentRetrievalDriver() is not None

    storage = XmlXCAFDrivers.Factory(Standard_GUID(STORAGE_GUID))
    retrieval = XmlXCAFDrivers.Factory(Standard_GUID(RETRIEVAL_GUID))
    assert storage.DynamicType().Name() == "XmlXCAFDrivers_DocumentStorageDriver"
    assert retrieval.DynamicType().Name() == "XmlXCAFDrivers_DocumentRetrievalDriver"
    with pytest.raises(Standard_Failure, match="unknown GUID"):
        XmlXCAFDrivers.Factory(Standard_GUID("ad696002-5b34-11d1-b5ba-00a0c9064368"))


@pytest.mark.parametrize("driver, attribute", [
    (XmlMXCAFDoc_AssemblyItemRefDriver, "XCAFDoc_AssemblyItemRef"),
    (XmlMXCAFDoc_CentroidDriver, "XCAFDoc_Centroid"),
    (XmlMXCAFDoc_ColorDriver, "XCAFDoc_Color"),
    (XmlMXCAFDoc_DatumDriver, "XCAFDoc_Datum"),
    (XmlMXCAFDoc_GraphNodeDriver, "XCAFDoc_GraphNode"),
    (XmlMXCAFDoc_LocationDriver, "XCAFDoc_Location"),
])
def test_each_attribute_driver_names_the_attribute_it_persists(driver, attribute):
    assert driver(Message.Message.DefaultMessenger()).SourceType().Name() == attribute


def test_the_driver_set_matches_the_binary_one():
    """The two OCAF formats persist the same XCAF attributes, so the driver sets are identical name for name -- which
    is why a document written by either reads back the same product structure."""
    import nanoocp.BinMXCAFDoc as binary
    import nanoocp.XmlMXCAFDoc as xml
    assert (sorted(n[len("XmlMXCAFDoc_"):] for n in dir(xml) if n.startswith("XmlMXCAFDoc_"))
            == sorted(n[len("BinMXCAFDoc_"):] for n in dir(binary) if n.startswith("BinMXCAFDoc_")))


def test_report_is_one_line():
    """TopTools_LocationSetPtr is `TopTools_LocationSet*` (TopTools_LocationSetPtr.hxx), so the parameter is a
    reference to a pointer -- the shared location set the driver threads through a read, internal to it."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert len(lines) == 1
    assert lines[0].startswith("raw-pointer") and "XmlMXCAFDoc_LocationDriver::SetSharedLocations" in lines[0]
