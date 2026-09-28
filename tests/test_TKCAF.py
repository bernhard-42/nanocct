"""Generated bindings for TKCAF (ApplicationFramework: TDataXtd, TNaming, AppStd): topological naming -- the attribute
XCAF stores shapes in (TNaming_NamedShape) with its builder, tool, iterator and selector -- the geometry/shape/triangulation
attributes of TDataXtd, and undo of a named shape."""
import importlib
from pathlib import Path

import pytest

from nanocct import AppStd, TDataXtd, TDF, TDocStd, TNaming, TopoDS, gp
from nanocct.BRep import BRep_Tool
from nanocct.BRepBuilderAPI import BRepBuilderAPI_Transform
from nanocct.BRepMesh import BRepMesh_IncrementalMesh
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.TCollection import TCollection_ExtendedString
from nanocct.TopAbs import TopAbs_FACE, TopAbs_SOLID
from nanocct.TopExp import TopExp_Explorer
from nanocct.TopLoc import TopLoc_Location

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKCAF" / "report.txt"


@pytest.mark.parametrize("pkg", ["TDataXtd", "TNaming", "AppStd"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


@pytest.fixture
def doc():
    app = TDocStd.TDocStd_Application()
    return app.NewDocument__TDocStd_Document(TCollection_ExtendedString("BinOcaf"))


@pytest.fixture
def box():
    return BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()


def test_named_shape_generated_and_found(doc, box):
    label = doc.Main().FindChild(1, True)
    builder = TNaming.TNaming_Builder(label)
    builder.Generated(box)
    named = builder.NamedShape()
    assert named.Evolution() == TNaming.TNaming_PRIMITIVE and named.IsEmpty() is False
    assert named.Get().ShapeType() == TopAbs_SOLID and named.Get().IsSame(box)
    assert TNaming.TNaming_Tool.GetShape_s(named).IsSame(box) and TNaming.TNaming_Tool.CurrentShape_s(named).IsSame(box)
    found, attr = label.FindAttribute(TNaming.TNaming_NamedShape.GetID_s())
    assert found is True and type(attr) is TNaming.TNaming_NamedShape
    assert TNaming.TNaming_Tool.HasLabel_s(doc.Main(), box) is True
    where, transdef = TNaming.TNaming_Tool.Label_s(doc.Main(), box)         # int& TransDef out-param (R-OUT)
    assert where == label and transdef == 0


def test_modify_evolution_and_iterator(doc, box):
    trsf = gp.gp_Trsf()
    trsf.SetTranslation(gp.gp_Vec(1.0, 0.0, 0.0))
    moved = BRepBuilderAPI_Transform(box, trsf, True).Shape()
    label = doc.Main().FindChild(2, True)
    TNaming.TNaming_Builder(label).Modify(box, moved)
    it = TNaming.TNaming_Iterator(label)                                   # More/Next/OldShape/NewShape: no Value(), no __iter__
    assert it.More() and it.OldShape().IsSame(box) and it.NewShape().IsSame(moved) and it.Evolution() == TNaming.TNaming_MODIFY
    it.Next()
    assert it.More() is False


def test_selector_selects_a_named_face(doc, box):
    """A face is only identifiable when it is named: with the box alone named (PRIMITIVE) Select() resolves to a compound
    of all six faces (OCCT semantics, checked); with every face on a sub-label it is the face itself."""
    label = doc.Main().FindChild(1, True)
    TNaming.TNaming_Builder(label).Generated(box)
    faces = []
    explorer = TopExp_Explorer(box, TopAbs_FACE)
    while explorer.More():
        faces.append(TopoDS.Face(explorer.Current()))
        TNaming.TNaming_Builder(label.FindChild(len(faces), True)).Generated(faces[-1])
        explorer.Next()
    selector = TNaming.TNaming_Selector(doc.Main().FindChild(4, True))
    assert selector.Select(faces[3], box) is True
    assert selector.NamedShape().Evolution() == TNaming.TNaming_SELECTED
    assert TNaming.TNaming_Tool.GetShape_s(selector.NamedShape()).IsSame(faces[3])
    identified, named = TNaming.TNaming_Selector.IsIdentified_s(doc.Main().FindChild(4), faces[3])   # handle& out-param
    assert identified is True and type(named) is TNaming.TNaming_NamedShape


def test_named_shape_undo(doc, box):
    doc.SetUndoLimit(5)
    label = doc.Main().FindChild(3, True)
    doc.NewCommand()
    TNaming.TNaming_Builder(label).Generated(box)
    doc.CommitCommand()
    assert label.IsAttribute(TNaming.TNaming_NamedShape.GetID_s()) is True
    doc.Undo()
    assert label.IsAttribute(TNaming.TNaming_NamedShape.GetID_s()) is False


def test_tdataxtd_point_shape_triangulation(doc, box):
    label = doc.Main().FindChild(1, True)
    assert type(TDataXtd.TDataXtd_Point.Set_s(label, gp.gp_Pnt(1.0, 2.0, 3.0))) is TDataXtd.TDataXtd_Point
    point = gp.gp_Pnt()
    assert TDataXtd.TDataXtd_Geometry.Point_s(label, point) is True         # gp_Pnt& filled in place (R-REF-CLASS)
    assert (point.X(), point.Y(), point.Z()) == (1.0, 2.0, 3.0)
    other = doc.Main().FindChild(2, True)
    TDataXtd.TDataXtd_Shape.Set_s(other, box)
    assert TDataXtd.TDataXtd_Shape.Get_s(other).IsSame(box)
    BRepMesh_IncrementalMesh(box, 0.1)
    face = TopoDS.Face(TopExp_Explorer(box, TopAbs_FACE).Current())
    triangulation = BRep_Tool.Triangulation_s(face, TopLoc_Location())
    attr = TDataXtd.TDataXtd_Triangulation.Set_s(label, triangulation)      # static Set collides with the instance Set (R-STATIC-S)
    assert (attr.NbNodes(), attr.NbTriangles()) == (4, 2)


def test_appstd_application_is_a_tdocstd_application():
    app = AppStd.AppStd_Application()
    assert isinstance(app, TDocStd.TDocStd_Application)
    assert type(app.NewDocument__TDocStd_Document(TCollection_ExtendedString("MDTV-Standard"))) is TDocStd.TDocStd_Document


def test_report_has_only_the_expected_omissions():
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert {line.split("\t")[0] for line in lines} <= {"iterator", "raw-pointer", "template"}
    assert any("TNaming_RefShape *" in line for line in lines)              # the internal shape->RefShape map (2d)
