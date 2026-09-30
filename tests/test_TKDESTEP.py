"""Generated bindings for TKDESTEP (DataExchange, 42 packages, the largest toolkit in scope): STEP import and export.
STEPControl_Reader/Writer for plain shapes -- CadQuery's path -- and STEPCAFControl_Reader/Writer for XCAF documents
with colours, plus the StepBasic/StepGeom/StepShape/... entity classes the AP214 schema is made of."""
import gc
import importlib
import re
from pathlib import Path

import pytest

from conftest import report

from nanocct import Message
from nanocct.BRepGProp import BRepGProp
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.GProp import GProp_GProps
from nanocct.IFSelect import IFSelect_RetDone
from nanocct.Interface import Interface_Static
from nanocct.NCollection import NCollection_Array1, NCollection_DynamicArray, NCollection_HArray1, NCollection_HSequence, NCollection_Sequence
from nanocct.Quantity import Quantity_Color, Quantity_NameOfColor, Quantity_NOC_RED
from nanocct.STEPCAFControl import STEPCAFControl_Controller, STEPCAFControl_Reader, STEPCAFControl_Writer
from nanocct.STEPConstruct import STEPConstruct
from nanocct.STEPControl import STEPControl_AsIs, STEPControl_Reader, STEPControl_StepModelType, STEPControl_Writer
from nanocct.StepBasic import StepBasic_Product, StepBasic_SiUnitName
from nanocct.StepGeom import StepGeom_CartesianPoint
from nanocct.StepShape import StepShape_ManifoldSolidBrep
from nanocct.StepVisual import StepVisual_TessellatedCurveSet, StepVisual_TessellatedGeometricSet, StepVisual_TessellatedItem
from nanocct.TCollection import TCollection_ExtendedString, TCollection_HAsciiString
from nanocct.TDF import TDF_Label
from nanocct.TopAbs import TopAbs_SOLID
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDoc import XCAFDoc_ColorCurv, XCAFDoc_ColorGen, XCAFDoc_ColorSurf, XCAFDoc_DocumentTool

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDESTEP" / "report.txt"
PACKAGES = ["STEPControl", "STEPCAFControl", "STEPConstruct", "STEPEdit", "STEPSelections", "StepBasic", "StepGeom",
            "StepShape", "StepRepr", "StepVisual", "StepData", "StepDimTol", "StepKinematics", "StepElement",
            "StepFEA", "StepAP203", "StepAP214", "StepAP242", "StepToGeom", "GeomToStep", "StepToTopoDS",
            "TopoDSToStep", "HeaderSection", "APIHeaderSection", "DESTEP", "StepTidy"]


@pytest.fixture(scope="module", autouse=True)
def controller():
    """STEPCAFControl_Controller::Init declares the STEP statics (write.step.schema and friends); without it
    Interface_Static.SetCVal_s on a STEP name returns False (seen with TKXSBase)."""
    STEPCAFControl_Controller.Init_s()


@pytest.fixture
def quiet_messenger():
    """The readers and writers print transfer statistics unconditionally."""
    printers = list(Message.Message.DefaultMessenger_s().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


def _volume(shape) -> float:
    properties = GProp_GProps()
    BRepGProp.VolumeProperties_s(shape, properties)
    return properties.Mass()


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_the_step_statics_cadquery_sets():
    """CadQuery's sequence (shapes.py:560-563) works once the controller declared the names."""
    assert Interface_Static.IsPresent_s("write.step.schema")
    assert Interface_Static.SetIVal_s("write.surfacecurve.mode", 1)
    assert Interface_Static.SetIVal_s("write.precision.mode", 0)
    assert Interface_Static.SetCVal_s("xstep.cascade.unit", "MM") and Interface_Static.CVal_s("xstep.cascade.unit") == "MM"
    # an enum static: the schema names are AP214IS/AP203/AP214DIS/AP242DIS, "AP214" alone is rejected
    assert Interface_Static.CVal_s("write.step.schema") == "AP214IS"
    assert not Interface_Static.SetCVal_s("write.step.schema", "AP214")
    assert Interface_Static.SetCVal_s("write.step.schema", "AP203") and Interface_Static.CVal_s("write.step.schema") == "AP203"
    assert Interface_Static.SetCVal_s("write.step.schema", "AP214IS")


def test_a_box_round_trips_through_a_step_file(tmp_path, quiet_messenger):
    """The milestone: write a solid as AP214 and read it back with the same volume."""
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    writer = STEPControl_Writer()
    assert writer.Transfer(box, STEPControl_AsIs) == IFSelect_RetDone
    path = tmp_path / "box.step"
    assert writer.Write(str(path)) == IFSelect_RetDone
    text = path.read_text()
    assert text.startswith("ISO-10303-21;") and "MANIFOLD_SOLID_BREP" in text

    reader = STEPControl_Reader()
    assert reader.ReadFile(str(path)) == IFSelect_RetDone
    assert reader.NbRootsForTransfer() == 1
    assert reader.TransferRoots() == 1
    result = reader.OneShape()
    assert result.ShapeType() == TopAbs_SOLID
    assert _volume(result) == pytest.approx(6.0)
    assert reader.NbShapes() == 1 and reader.Shape(1).ShapeType() == TopAbs_SOLID


def test_a_step_file_round_trips_in_memory(quiet_messenger):
    """No file needed: the writer's ostream& is the returned text (R-STREAM-OUT) and the reader takes a text
    file-like object (R-STREAM-IN; STEP is text, unlike the OCAF document streams)."""
    import io
    writer = STEPControl_Writer()
    assert writer.Transfer(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), STEPControl_AsIs) == IFSelect_RetDone
    status, text = writer.WriteStream()
    assert status == IFSelect_RetDone and text.startswith("ISO-10303-21;") and len(text) > 10000
    reader = STEPControl_Reader()
    assert reader.ReadStream("in-memory", io.StringIO(text)) == IFSelect_RetDone
    assert reader.NbRootsForTransfer() == 1 and reader.TransferRoots() == 1
    assert _volume(reader.OneShape()) == pytest.approx(6.0)


def test_the_reader_exposes_its_work_session_and_model(tmp_path, quiet_messenger):
    box = BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape()
    writer = STEPControl_Writer()
    writer.Transfer(box, STEPControl_AsIs)
    path = tmp_path / "cube.step"
    writer.Write(str(path))
    reader = STEPControl_Reader()
    reader.ReadFile(str(path))
    session = reader.WS()                                        # TKXSBase types, registered there
    assert type(session).__name__ == "XSControl_WorkSession"
    # STEPCAFControl_Controller::Init registered the CAF controller, which derives from STEPControl_Controller
    assert type(session.NormAdaptor()).__name__ == "STEPCAFControl_Controller"
    model = session.Model()
    assert model.NbEntities() > 100
    assert isinstance(reader.PrintCheckLoad__str(False, 0), str)  # ostream& -> returned str (R-STREAM-OUT, R-COLLISION)
    assert STEPControl_StepModelType.STEPControl_AsIs is STEPControl_AsIs


def test_an_xcaf_document_round_trips_with_its_colour(tmp_path, quiet_messenger):
    """STEPCAFControl writes the XCAF document; OCCT maps a generic colour onto the entity's surface and curve
    colours, so it comes back as XCAFDoc_ColorSurf/ColorCurv, not ColorGen."""
    app = XCAFApp_Application.GetApplication_s()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    colors = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    label = shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)
    colors.SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorGen)

    writer = STEPCAFControl_Writer()
    assert writer.Transfer(doc, STEPControl_AsIs)
    path = tmp_path / "assembly.step"
    assert writer.Write(str(path)) == IFSelect_RetDone

    reloaded = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    reader = STEPCAFControl_Reader()
    assert reader.ReadFile(str(path)) == IFSelect_RetDone
    assert reader.Transfer(reloaded)
    shapes2 = XCAFDoc_DocumentTool.ShapeTool_s(reloaded.Main())
    colors2 = XCAFDoc_DocumentTool.ColorTool_s(reloaded.Main())
    free = NCollection_Sequence[TDF_Label]()
    shapes2.GetFreeShapes(free)
    assert free.Length() == 1
    shape = shapes2.GetShape_s(free.Value(1))
    assert _volume(shape) == pytest.approx(6.0)
    labels = NCollection_Sequence[TDF_Label]()
    colors2.GetColors(labels)
    assert labels.Length() == 1
    color = Quantity_Color()
    assert not colors2.GetColor(shape, XCAFDoc_ColorGen, color)   # OCCT semantics, not an omission
    assert colors2.GetColor(shape, XCAFDoc_ColorSurf, color)
    assert color.Name() == Quantity_NameOfColor.Quantity_NOC_RED
    assert colors2.GetColor(shape, XCAFDoc_ColorCurv, color)


def test_the_entity_classes_of_the_schema():
    """The AP214 entity classes are plain Transients; 1 040 of them carry the schema."""
    point = StepGeom_CartesianPoint()
    coordinates = NCollection_HArray1[float](1, 3)
    for i, value in enumerate((1.0, 2.0, 3.0), start=1):
        coordinates.SetValue(i, value)
    point.Init(TCollection_HAsciiString("origin"), coordinates)
    assert point.Name().ToCString() == "origin" and point.NbCoordinates() == 3
    assert point.CoordinatesValue(2) == 2.0
    product = StepBasic_Product()
    assert product.DynamicType().Name() == "StepBasic_Product"
    assert StepShape_ManifoldSolidBrep().DynamicType().Name() == "StepShape_ManifoldSolidBrep"
    assert StepBasic_SiUnitName.StepBasic_sunMetre is not None
    assert hasattr(STEPConstruct, "FindEntity_s")


def test_report_categories():
    all_lines, lines, undefined, counts = report("TKDESTEP")
    # raw-pointer fell from 12 to 9 and override rose to 4 on 2026-09-23, when StepFile_ReadData was skipped: its
    # inline destructor calls the unexported ClearRecorder, so the class does not link on Windows (overrides.toml)
    # raw-pointer 9 -> 1 and unbound-type 2 -> 0 on 2026-09-30: NCollection_Handle<T> is a caster now (R-NCHANDLE), not a
    # class template the 6c walk tried and failed to bind (its get()/operator-> and its handle<Standard_Transient> base)
    assert counts == {"raw-pointer": 1, "rvalue": 3, "override": 4, "template": 2,
                      "header": 1, "stream": 1,
                      "overload-collision": 3,    # StepToTopoDS_Builder::Init, derived class first (R-OVERLOAD-ORDER)
                      "null-bool": 1}             # StepData_SelectType (R-NULL-BOOL, 2026-09-30)
    assert len(lines) == 16
    # which members R-UNDEFINED reports is the platform's business (macOS names four entities, Windows others), so
    # only the package is asserted here; the portable categories above are what this test is really about
    assert all(line.split("\t")[1].lower().startswith(("step", "rwstep", "apiheadersection")) for line in undefined)                                       # 1 040 classes, 7 688 methods bound
    # the bison/flex parser of step.tab.hxx is skipped wholesale (overrides.toml [skip] namespaces)
    assert sum(re.search(r"\bstep\b", line) is not None and "namespace" in line for line in lines) == 2
    # the rvalue lines are the && twins of bound const& overloads: SetShapeFixParameters, as in TKXSBase
    assert all("SetShapeFixParameters" in line for line in lines if line.startswith("rvalue"))


def test_ncollection_handle_is_transparent_and_init_takes_a_copy():
    """R-NCHANDLE: NCollection_Handle<X> -- OCCT's reference-counted owner of a non-Transient X -- is the X
    itself in Python, like opencascade::handle: Items()/Curves() raised TypeError (unregistered type) and Init() rejected
    both an array and None. A result is shared with the entity and outlives it; a null handle is None; a parameter is
    copied, because the handle deletes what it holds and the Python array owns its own."""
    geo = StepVisual_TessellatedGeometricSet()
    assert geo.Items() is None                                       # null: get() would dereference the null Ptr
    first, second = StepVisual_TessellatedItem(), StepVisual_TessellatedItem()
    items = NCollection_Array1[StepVisual_TessellatedItem](1, 1)
    items.SetValue(1, first)
    geo.Init(TCollection_HAsciiString("set"), items)
    got = geo.Items()
    assert type(got).__name__ == "NCollection_Array1__Handle_StepVisual_TessellatedItem" and got.Length() == 1
    assert got.Value(1) is first and geo.Items() is got              # the same wrapper for the same array
    items.SetValue(1, second)
    assert geo.Items().Value(1) is first                             # Init took a copy
    got.SetValue(1, second)
    assert geo.Items().Value(1) is second                            # the result is shared, as in C++
    del geo
    gc.collect()
    assert got.Length() == 1 and got.Value(1) is second              # kept alive by its own copy of the handle
    empty = StepVisual_TessellatedGeometricSet()
    empty.Init(TCollection_HAsciiString("empty"), None)
    assert empty.Items() is None
    curves = StepVisual_TessellatedCurveSet()
    assert curves.Curves() is None
    seq = NCollection_HSequence[int]()
    seq.Append(3)
    seq.Append(5)
    polylines = NCollection_DynamicArray[NCollection_HSequence[int]]()
    polylines.Append(seq)
    curves.Init(TCollection_HAsciiString("curves"), None, polylines)
    back = curves.Curves()
    assert back.Length() == 1 and back.Value(0) is seq and [back.Value(0).Value(i) for i in (1, 2)] == [3, 5]

