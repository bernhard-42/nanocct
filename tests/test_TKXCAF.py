"""Generated bindings for TKXCAF (DataExchange: XCAFApp, XCAFDoc, XCAFPrs, XCAFView, XCAFDimTolObjects,
XCAFNoteObjects): the extended CAF document -- assemblies of shapes with colours, layers, materials, dimensions and
notes. This is what build123d and CadQuery drive after a STEP import; the STEP reader itself arrives with TKDESTEP."""
import importlib
from pathlib import Path

import pytest

from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.NCollection import NCollection_Sequence
from nanocct.Quantity import Quantity_Color, Quantity_NameOfColor, Quantity_NOC_RED
from nanocct.TCollection import TCollection_ExtendedString
from nanocct.TDataStd import TDataStd_Name
from nanocct.TDF import TDF_Label
from nanocct.TopAbs import TopAbs_SOLID
from nanocct.TopLoc import TopLoc_Location
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDoc import (XCAFDoc, XCAFDoc_AssemblyIterator, XCAFDoc_ColorGen, XCAFDoc_ColorTool,
                             XCAFDoc_ColorType, XCAFDoc_DocumentTool, XCAFDoc_Note, XCAFDoc_NoteBalloon,
                             XCAFDoc_NoteComment, XCAFDoc_ShapeTool)
from nanocct.XCAFPrs import XCAFPrs_DocumentExplorer, XCAFPrs_DocumentExplorerFlags_None
from nanocct.gp import gp_Trsf, gp_Vec

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKXCAF" / "report.txt"


@pytest.mark.parametrize("pkg", ["XCAFApp", "XCAFDoc", "XCAFPrs", "XCAFView", "XCAFDimTolObjects", "XCAFNoteObjects"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


@pytest.fixture
def doc():
    app = XCAFApp_Application.GetApplication_s()                       # OCP: GetApplication_s
    return app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))


def test_the_document_tools_build123d_uses(doc):
    """build123d calls XCAFDoc_DocumentTool.ShapeTool_s/ColorTool_s/LayerTool_s/MaterialTool_s/SetLengthUnit_s;
    every static carries _s in nanocct as in OCP (R-STATIC-S, 2026-09-26), so the plain names do not exist."""
    assert type(XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())).__name__ == "XCAFDoc_ShapeTool"
    assert type(XCAFDoc_DocumentTool.ColorTool_s(doc.Main())).__name__ == "XCAFDoc_ColorTool"
    assert type(XCAFDoc_DocumentTool.LayerTool_s(doc.Main())).__name__ == "XCAFDoc_LayerTool"
    assert type(XCAFDoc_DocumentTool.MaterialTool_s(doc.Main())).__name__ == "XCAFDoc_MaterialTool"
    for name in ("ShapeTool", "ColorTool", "LayerTool", "MaterialTool", "SetLengthUnit"):
        assert not hasattr(XCAFDoc_DocumentTool, name)
    XCAFDoc_DocumentTool.SetLengthUnit_s(doc, 0.001)
    assert XCAFDoc_DocumentTool.GetLengthUnit_s(doc) == (True, 0.001)   # double& -> returned (R-OUT)


def test_a_shape_with_a_name_and_a_colour(doc):
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    colors = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    label = shapes.AddShape(box, False)
    TDataStd_Name.Set_s(label, TCollection_ExtendedString("the box"))
    assert shapes.IsShape_s(label) and shapes.IsSimpleShape_s(label)
    assert shapes.GetShape_s(label).ShapeType() == TopAbs_SOLID
    labels = NCollection_Sequence[TDF_Label]()
    shapes.GetShapes(labels)                                          # class reference filled in place (R-REF-CLASS)
    assert labels.Length() == 1 and labels.Value(1).Tag() == label.Tag()
    colors.SetColor(label, Quantity_Color(Quantity_NOC_RED), XCAFDoc_ColorGen)
    color = Quantity_Color()
    assert colors.GetColor(box, XCAFDoc_ColorGen, color)              # the instance overload takes the shape
    assert color.Name() == Quantity_NameOfColor.Quantity_NOC_RED
    color_label = TDF_Label()
    assert colors.GetColor(box, XCAFDoc_ColorGen, color_label)        # ... or the colour label
    assert XCAFDoc_ColorTool.GetColor_s(color_label, color)           # the static twin keeps _s (an instance GetColor exists)
    assert color.Name() == Quantity_NameOfColor.Quantity_NOC_RED
    assert list(XCAFDoc_ColorType)[:2] == [XCAFDoc_ColorType.XCAFDoc_ColorGen, XCAFDoc_ColorType.XCAFDoc_ColorSurf]
    assert XCAFDoc.ColorRefGUID_s(XCAFDoc_ColorGen).IsNotSame(XCAFDoc.MaterialRefGUID_s())


def test_an_assembly_with_a_component(doc):
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    box = shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)
    assembly = shapes.NewShape()
    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(10.0, 0.0, 0.0))
    component = shapes.AddComponent(assembly, box, TopLoc_Location(trsf))
    assert shapes.IsAssembly_s(assembly) and shapes.IsComponent_s(component)
    assert XCAFDoc_ShapeTool.IsReference_s(component)                   # OCP: IsReference_s; no instance twin here
    referred = TDF_Label()
    assert XCAFDoc_ShapeTool.GetReferredShape_s(component, referred)    # OCP: GetReferredShape_s
    assert referred.Tag() == box.Tag()
    free = NCollection_Sequence[TDF_Label]()
    shapes.GetFreeShapes(free)
    assert free.Length() == 1 and free.Value(1).Tag() == assembly.Tag()


def test_the_document_iterators(doc):
    """R-ITER: the assembly iterator and the presentation explorer are their own Python iterators."""
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    box = shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape(), False)
    assembly = shapes.NewShape()
    shapes.AddComponent(assembly, box, TopLoc_Location())
    assert sum(1 for _ in XCAFDoc_AssemblyIterator(doc)) == 2
    assert sum(1 for _ in XCAFPrs_DocumentExplorer(doc, XCAFPrs_DocumentExplorerFlags_None)) == 2


def test_a_static_is_renamed_when_a_base_has_the_instance_method():
    """XCAFDoc_NoteBalloon declares only a static Set; the instance Set comes from XCAFDoc_Note two levels up.
    Binding both under one name aborts the module import ("mismatched static/instance method flags"), so R-STATIC-S
    is decided over the whole inheritance chain since 2026-09-22."""
    assert XCAFDoc_NoteBalloon.__mro__[1] is XCAFDoc_NoteComment and XCAFDoc_NoteComment.__mro__[1] is XCAFDoc_Note
    assert hasattr(XCAFDoc_NoteBalloon, "Set_s") and hasattr(XCAFDoc_NoteBalloon, "Set")
    assert XCAFDoc_NoteBalloon.Set_s.__doc__.startswith("Set_s(theLabel")      # a static: no self
    assert XCAFDoc_NoteBalloon.Set.__doc__.startswith("Set(self")               # the inherited instance method
    assert hasattr(XCAFDoc_NoteComment, "Set_s")                      # static and instance in the same class
    assert not hasattr(XCAFDoc_Note, "Set_s") and hasattr(XCAFDoc_Note, "Set")


def test_report_categories():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    counts: dict[str, int] = {}
    for line in lines:
        counts[line.split("\t")[0]] = counts.get(line.split("\t")[0], 0) + 1
    assert counts == {"iterator": 4, "overload-collision": 3, "template": 2, "header": 1, "undefined": 1, "null-bool": 1,   # XCAFDoc_AssemblyItemId (R-NULL-BOOL)
                      "copy": 1}         # XCAFPrs_AISObject, an AIS object (R-COPY, 2026-10-02)
    # the two template lines are XCAFDoc_AssemblyTool::Traverse (a visitor template); the iterators are the way in (2d)
    assert sum("XCAFDoc_AssemblyTool::Traverse" in line for line in lines) == 2
