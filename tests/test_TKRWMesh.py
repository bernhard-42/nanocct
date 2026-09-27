"""Generated bindings for TKRWMesh (DataExchange: the RWMesh package): the mesh reader/writer base the glTF, OBJ and
PLY toolkits build on -- the shape iterators that hand out a face's triangulation, the Z-up/Y-up coordinate converter
every mesh format needs, node attributes and the material map."""
import importlib
from pathlib import Path

import pytest

from conftest import report

from OCP3x import Message
from OCP3x.BRepMesh import BRepMesh_IncrementalMesh
from OCP3x.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCP3x.RWMesh import (RWMesh, RWMesh_CafReader, RWMesh_CoordinateSystem,
                            RWMesh_CoordinateSystemConverter, RWMesh_CoordinateSystem_negZfwd_posYup,
                            RWMesh_CoordinateSystem_posYfwd_posZup, RWMesh_EdgeIterator, RWMesh_FaceIterator,
                            RWMesh_NameFormat, RWMesh_NameFormat_Product, RWMesh_NodeAttributes,
                            RWMesh_TriangulationReader, RWMesh_VertexIterator)
from OCP3x.TCollection import TCollection_ExtendedString
from OCP3x.TDataStd import TDataStd_Name
from OCP3x.TopAbs import TopAbs_FACE
from OCP3x.XCAFApp import XCAFApp_Application
from OCP3x.XCAFDoc import XCAFDoc_DocumentTool
from OCP3x.gp import gp_XYZ

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKRWMesh" / "report.txt"


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
    BRepMesh_IncrementalMesh(box, 0.1)
    return box


def test_package_imports():
    assert importlib.import_module("OCP3x.RWMesh").__name__ == "OCP3x.RWMesh"


def test_the_face_iterator_hands_out_the_triangulation(meshed_box):
    """RWMesh_FaceIterator is what every mesh writer walks: one triangulation per face, with the nodes already
    transformed into the shape's coordinate system."""
    faces, triangles = 0, 0
    iterator = RWMesh_FaceIterator(meshed_box)
    while iterator.More():
        faces += 1
        triangles += iterator.Triangulation().NbTriangles()
        iterator.Next()
    assert (faces, triangles) == (6, 12)

    first = RWMesh_FaceIterator(meshed_box)
    assert first.More() and not first.IsEmptyMesh()
    assert first.Face().ShapeType() == TopAbs_FACE
    assert first.Triangulation().NbNodes() == 4 and first.NbTriangles() == 2
    assert first.HasNormals() and first.HasTexCoords()
    assert first.node(1).X() == pytest.approx(0.0)
    assert first.NodeLower() == 1 and first.NodeUpper() == 4
    assert first.HasFaceColor() is False


def test_the_free_edge_and_vertex_iterators_are_empty_for_a_solid(meshed_box):
    """RWMesh_EdgeIterator and RWMesh_VertexIterator visit *free* edges and vertices -- ones that belong to no face.
    A box has none, so both stop immediately; that is the shape of the API, not a binding gap."""
    for iterator in (RWMesh_EdgeIterator(meshed_box), RWMesh_VertexIterator(meshed_box)):
        steps = 0
        while iterator.More():
            steps += 1
            iterator.Next()
        assert steps == 0


def test_the_coordinate_converter_is_the_z_up_to_y_up_step():
    """OCCT is Z-up, glTF is Y-up: the converter is what the mesh writers put between them."""
    assert [m.name for m in RWMesh_CoordinateSystem] == ["RWMesh_CoordinateSystem_Undefined",
                                                         "RWMesh_CoordinateSystem_posYfwd_posZup",
                                                         "RWMesh_CoordinateSystem_negZfwd_posYup"]
    converter = RWMesh_CoordinateSystemConverter()
    assert converter.IsEmpty()
    converter.SetInputCoordinateSystem(RWMesh_CoordinateSystem_posYfwd_posZup)    # OCCT
    converter.SetOutputCoordinateSystem(RWMesh_CoordinateSystem_negZfwd_posYup)   # glTF
    assert converter.HasInputCoordinateSystem() and converter.HasOutputCoordinateSystem()
    assert not converter.IsEmpty()
    position = gp_XYZ(1.0, 2.0, 3.0)
    converter.TransformPosition(position)                                          # filled in place (R-REF-CLASS)
    assert (position.X(), position.Y(), position.Z()) == pytest.approx((1.0, 3.0, -2.0))
    converter.SetInputLengthUnit(1.0)
    converter.SetOutputLengthUnit(0.001)
    assert converter.InputLengthUnit() == 1.0 and converter.OutputLengthUnit() == 0.001


def test_node_attributes_and_the_name_format():
    attributes = RWMesh_NodeAttributes()
    attributes.Name = "the box"                                   # a str converts to TCollection_AsciiString
    assert attributes.Name.ToCString() == "the box"
    assert attributes.RawName.ToCString() == ""

    app = XCAFApp_Application.GetApplication_s()
    doc = app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinXCAF"))
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    label = shapes.AddShape(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape(), False)
    TDataStd_Name.Set_s(label, TCollection_ExtendedString("product"))
    assert RWMesh.FormatName_s(RWMesh_NameFormat_Product, label, label).ToCString() == "product"
    assert len(list(RWMesh_NameFormat)) == 7


def test_report_is_only_abstract_constructors():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    _, portable, undefined, _ = report("TKRWMesh")
    assert len(portable) == 0
    assert all(line.startswith("undefined\tRWMesh") for line in undefined)
    # all three are abstract classes: clang emits no complete-object constructor for them
    for cls in (RWMesh_CafReader, RWMesh_TriangulationReader):
        with pytest.raises(TypeError, match="no constructor defined"):
            cls()
