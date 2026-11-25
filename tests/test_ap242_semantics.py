"""AP242 interoperability: nested occurrence placement and semantic PMI links.

Synthetic analytic geometry makes the expectations independent of the writer.
These are runtime-wheel tests; they do not require generated binding reports.
"""
import math

import pytest

from nanocct import Message
from nanocct.BRepAdaptor import BRepAdaptor_Surface
from nanocct.BRepGProp import BRepGProp
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from nanocct.GeomAbs import GeomAbs_Cylinder
from nanocct.GProp import GProp_GProps
from nanocct.IFSelect import IFSelect_RetDone
from nanocct.Interface import Interface_Static
from nanocct.NCollection import NCollection_Sequence
from nanocct.STEPCAFControl import STEPCAFControl_Controller, STEPCAFControl_Reader, STEPCAFControl_Writer
from nanocct.STEPControl import STEPControl_AsIs
from nanocct.TCollection import TCollection_ExtendedString
from nanocct.TDataStd import TDataStd_Name
from nanocct.TDF import TDF_Label
from nanocct.TopAbs import TopAbs_FACE, TopAbs_SOLID
from nanocct.TopExp import TopExp_Explorer
from nanocct.TopLoc import TopLoc_Location
from nanocct.TopoDS import Face
from nanocct.XCAFApp import XCAFApp_Application
from nanocct.XCAFDimTolObjects import (
    XCAFDimTolObjects_DimensionObject,
    XCAFDimTolObjects_DimensionType,
    XCAFDimTolObjects_GeomToleranceObject,
    XCAFDimTolObjects_GeomToleranceType,
)
from nanocct.XCAFDoc import XCAFDoc_Dimension, XCAFDoc_DimTolTool, XCAFDoc_DocumentTool, XCAFDoc_GeomTolerance
from nanocct.gp import gp_Ax1, gp_Dir, gp_Pnt, gp_Trsf, gp_Vec


@pytest.fixture
def quiet_messenger():
    printers = list(Message.Message.DefaultMessenger_s().Printers())
    levels = [printer.GetTraceLevel() for printer in printers]
    for printer in printers:
        printer.SetTraceLevel(Message.Message_Fail)
    yield
    for printer, level in zip(printers, levels):
        printer.SetTraceLevel(level)


@pytest.fixture
def documents(quiet_messenger):
    app = XCAFApp_Application.GetApplication_s()
    created = []

    def new_document():
        doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
        XCAFDoc_DocumentTool.SetLengthUnit_s(doc, .001)
        created.append(doc)
        return doc

    yield new_document
    for doc in reversed(created):
        app.Close(doc)


def _roundtrip(doc, path, documents):
    STEPCAFControl_Controller.Init_s()
    previous_schema = Interface_Static.CVal_s("write.step.schema")
    try:
        assert Interface_Static.SetCVal_s("write.step.schema", "AP242DIS")
        writer = STEPCAFControl_Writer()
        writer.SetDimTolMode(True)
        assert writer.Transfer(doc, STEPControl_AsIs)
        assert writer.Write(str(path)) == IFSelect_RetDone
        assert "AP242" in path.read_text()
        loaded = documents()
        reader = STEPCAFControl_Reader()
        reader.SetGDTMode(True)
        assert reader.ReadFile(str(path)) == IFSelect_RetDone
        assert reader.Transfer(loaded)
        assert XCAFDoc_DocumentTool.GetLengthUnit_s(loaded) == (True, .001)
        return loaded
    finally:
        assert Interface_Static.SetCVal_s("write.step.schema", previous_schema)


def _translation(x, y, z):
    transform = gp_Trsf()
    transform.SetTranslation(gp_Vec(x, y, z))
    return TopLoc_Location(transform)


def test_ap242_nested_repeated_assembly_preserves_rotated_occurrences(tmp_path, documents):
    doc = documents()
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    part = shapes.AddShape(BRepPrimAPI_MakeBox(2., 4., 6.).Shape(), False)
    subassembly = shapes.NewShape()
    inner = gp_Trsf()
    inner.SetRotation(gp_Ax1(gp_Pnt(0., 0., 0.), gp_Dir(1., 0., 0.)), math.pi / 2)
    inner.SetTranslationPart(gp_Vec(10., 0., 0.))
    shapes.AddComponent(subassembly, part, TopLoc_Location(inner))
    shapes.AddComponent(subassembly, part, _translation(20., 0., 0.))
    root = shapes.NewShape()
    TDataStd_Name.Set_s(root, TCollection_ExtendedString("Repeated rotated assembly"))
    rotation = gp_Trsf()
    rotation.SetRotation(gp_Ax1(gp_Pnt(0., 0., 0.), gp_Dir(0., 0., 1.)), math.pi / 2)
    rotation.SetTranslationPart(gp_Vec(100., 0., 0.))
    shapes.AddComponent(root, subassembly, TopLoc_Location(rotation))
    shapes.AddComponent(root, subassembly, _translation(0., 100., 0.))
    shapes.UpdateAssemblies()

    loaded = _roundtrip(doc, tmp_path / "nested.step", documents)
    tool = XCAFDoc_DocumentTool.ShapeTool_s(loaded.Main())
    roots = NCollection_Sequence[TDF_Label]()
    tool.GetFreeShapes(roots)
    assert roots.Length() == 1
    root_label = roots.Value(1)
    found, name = root_label.FindAttribute(TDataStd_Name.GetID_s())
    assert found and name.Get().ToExtString() == "Repeated rotated assembly"
    components = NCollection_Sequence[TDF_Label]()
    assert tool.GetComponents_s(root_label, components) and components.Length() == 2
    referred = [TDF_Label(), TDF_Label()]
    for component, label in zip(components, referred):
        assert tool.GetReferredShape_s(component, label) and tool.IsAssembly_s(label)
    assert referred[0].IsEqual(referred[1])  # one definition, two occurrences

    children = NCollection_Sequence[TDF_Label]()
    assert tool.GetComponents_s(referred[0], children) and children.Length() == 2
    parts = [TDF_Label(), TDF_Label()]
    for child, label in zip(children, parts):
        assert tool.GetReferredShape_s(child, label) and tool.IsSimpleShape_s(label)
    assert parts[0].IsEqual(parts[1])  # the leaves also share one definition

    # Numeric matrices are independent of OCCT's transform-composition implementation.
    for labels, expected in (
        (components, [((0., -1., 0., 100.), (1., 0., 0., 0.), (0., 0., 1., 0.)),
                      ((1., 0., 0., 0.), (0., 1., 0., 100.), (0., 0., 1., 0.))]),
        (children, [((1., 0., 0., 10.), (0., 0., -1., 0.), (0., 1., 0., 0.)),
                    ((1., 0., 0., 20.), (0., 1., 0., 0.), (0., 0., 1., 0.))]),
    ):
        actual = []
        for label in labels:
            transform = tool.GetLocation_s(label).Transformation()
            actual.append(tuple(transform.Value(row, col) for row in range(1, 4) for col in range(1, 5)))
        for matrix, reference in zip(sorted(actual), sorted(tuple(v for row in m for v in row) for m in expected)):
            assert matrix == pytest.approx(reference, abs=1e-7)

    centres = []
    volumes = []
    inertias = []
    for solid in TopExp_Explorer(tool.GetShape_s(root_label), TopAbs_SOLID):
        props = GProp_GProps()
        BRepGProp.VolumeProperties_s(solid, props)
        centre = props.CentreOfMass()
        centres.append((centre.X(), centre.Y(), centre.Z()))
        volumes.append(props.Mass())
        inertia = props.MatrixOfInertia()
        inertias.append(tuple(inertia.Value(i, i) for i in range(1, 4)))
    assert len(centres) == 4
    assert volumes == pytest.approx([48.] * 4)
    for (actual, inertia), (expected, diagonal) in zip(sorted(zip(centres, inertias)), [
        ((11., 97., 2.), (208., 80., 160.)),
        ((21., 102., 3.), (208., 160., 80.)),
        ((98., 21., 3.), (160., 208., 80.)),
        ((103., 11., 2.), (80., 208., 160.)),
    ]):
        assert actual == pytest.approx(expected, abs=1e-7)
        assert inertia == pytest.approx(diagonal, abs=1e-7)


def test_ap242_semantic_dimension_and_tolerance_keep_subshape_links(tmp_path, documents):
    doc = documents()
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    cylinder = BRepPrimAPI_MakeCylinder(2., 6.).Shape()
    part = shapes.AddShape(cylinder, False)
    TDataStd_Name.Set_s(part, TCollection_ExtendedString("PMI target"))
    # Same lateral area (24*pi), different radius, height and position: area alone cannot identify the target.
    shapes.AddShape(BRepPrimAPI_MakeCylinder(1., 12.).Shape().Moved(_translation(20., 0., 0.)), False)
    face = next(Face(item) for item in TopExp_Explorer(cylinder, TopAbs_FACE)
                if BRepAdaptor_Surface(Face(item)).GetType() == GeomAbs_Cylinder)
    face_label = shapes.AddSubShape(part, face)
    tolerances = XCAFDoc_DocumentTool.DimTolTool_s(doc.Main())
    dimension_label = tolerances.AddDimension()
    dimension = XCAFDimTolObjects_DimensionObject()
    dimension.SetType(XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter)
    dimension.SetValue(4.)
    assert dimension.SetUpperTolValue(.1)
    assert dimension.SetLowerTolValue(.02)
    XCAFDoc_Dimension.Set_s(dimension_label).SetObject(dimension)
    tolerances.SetDimension(face_label, dimension_label)
    tolerance_label = tolerances.AddGeomTolerance()
    tolerance = XCAFDimTolObjects_GeomToleranceObject()
    tolerance.SetType(XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity)
    tolerance.SetValue(.05)
    XCAFDoc_GeomTolerance.Set_s(tolerance_label).SetObject(tolerance)
    tolerances.SetGeomTolerance(face_label, tolerance_label)

    loaded = _roundtrip(doc, tmp_path / "semantic-pmi.step", documents)
    tool = XCAFDoc_DocumentTool.DimTolTool_s(loaded.Main())
    dimensions, geometric = NCollection_Sequence[TDF_Label](), NCollection_Sequence[TDF_Label]()
    tool.GetDimensionLabels(dimensions)
    tool.GetGeomToleranceLabels(geometric)
    assert dimensions.Length() == geometric.Length() == 1
    found, attribute = dimensions.Value(1).FindAttribute(XCAFDoc_Dimension.GetID_s())
    assert found
    dim = attribute.GetObject()
    assert dim.GetType() == XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter
    assert dim.GetValue() == pytest.approx(4.)
    assert dim.GetUpperTolValue() == pytest.approx(.1)
    assert dim.GetLowerTolValue() == pytest.approx(.02)
    found, attribute = geometric.Value(1).FindAttribute(XCAFDoc_GeomTolerance.GetID_s())
    assert found
    geom = attribute.GetObject()
    assert geom.GetType() == XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity
    assert geom.GetValue() == pytest.approx(.05)
    shape_tool = XCAFDoc_DocumentTool.ShapeTool_s(loaded.Main())
    roots = NCollection_Sequence[TDF_Label]()
    shape_tool.GetFreeShapes(roots)
    assert roots.Length() == 2
    target = None
    for root in roots:
        found, name = root.FindAttribute(TDataStd_Name.GetID_s())
        if found and name.Get().ToExtString() == "PMI target":
            assert target is None
            target = root
    assert target is not None
    expected_face = next(Face(item) for item in TopExp_Explorer(shape_tool.GetShape_s(target), TopAbs_FACE)
                         if BRepAdaptor_Surface(Face(item)).GetType() == GeomAbs_Cylinder)
    references = []
    for label in (dimensions.Value(1), geometric.Value(1)):
        first, second = NCollection_Sequence[TDF_Label](), NCollection_Sequence[TDF_Label]()
        assert XCAFDoc_DimTolTool.GetRefShapeLabel_s(label, first, second)
        assert first.Length() == 1 and second.Length() == 0
        references.append(first.Value(1))
        assert shape_tool.IsSubShape_s(first.Value(1))
        linked = shape_tool.GetShape_s(first.Value(1))
        assert linked.ShapeType() == TopAbs_FACE
        assert shape_tool.IsSubShape(target, linked) and linked.IsSame(expected_face)
        surface = BRepAdaptor_Surface(Face(linked))
        assert surface.GetType() == GeomAbs_Cylinder
        assert surface.Cylinder().Radius() == pytest.approx(2.)
        props = GProp_GProps()
        BRepGProp.SurfaceProperties_s(linked, props)
        assert props.Mass() == pytest.approx(24 * math.pi)
        centre = props.CentreOfMass()
        assert (centre.X(), centre.Y(), centre.Z()) == pytest.approx((0., 0., 3.), abs=1e-7)
    assert references[0].IsEqual(references[1])
