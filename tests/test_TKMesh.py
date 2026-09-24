"""Generated bindings for TKMesh: BRepMesh_IncrementalMesh (the mesher build123d/CadQuery tessellate with), IMeshTools_Parameters,
the IMeshData interfaces (first base only, R-MI). New with this toolkit: non-copyable classes detected by the parser (CellFilter
members, containers of deleted-copy elements), classes whose class-level operator new hides the placement form skipped when
nanobind needs it, array references skipped, non-const std:: references returned as out-parameters."""
import importlib
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import BRep, BRepMesh, BRepMeshData, BRepPrimAPI, HLRAlgo, HLRBRep, IMeshData, IMeshTools, TopAbs, TopExp, TopLoc, TopoDS, gp

PACKAGES = ["IMeshData", "IMeshTools", "BRepMeshData", "BRepMesh"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKMesh" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _triangles(shape: TopoDS.TopoDS_Shape) -> int:
    total = 0
    for f in TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_FACE):
        tri = BRep.BRep_Tool.Triangulation(TopoDS.Face(f), TopLoc.TopLoc_Location())
        total += 0 if tri is None else tri.NbTriangles()
    return total


def test_incremental_mesh():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
    mesh = BRepMesh.BRepMesh_IncrementalMesh(box, 0.1)
    assert mesh.IsDone() and mesh.GetStatusFlags() == 0 and _triangles(box) == 12
    params = IMeshTools.IMeshTools_Parameters()                       # public fields (R-FIELD)
    params.Deflection = 0.01
    params.Angle = 0.1
    params.InParallel = False
    sphere = BRepPrimAPI.BRepPrimAPI_MakeSphere(1.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(sphere, params)
    assert _triangles(sphere) > 1000
    # HLRBRep_PolyAlgo works once the shape carries a triangulation
    algo = HLRBRep.HLRBRep_PolyAlgo()
    algo.Load(box)
    algo.Projector(HLRAlgo.HLRAlgo_Projector(gp.gp_Ax2(gp.gp_Pnt(5, -5, 5), gp.gp_Dir(-1, 1, -1))))
    algo.Update()
    to_shape = HLRBRep.HLRBRep_PolyHLRToShape()
    to_shape.Update(algo)
    assert sum(1 for _ in TopExp.TopExp_Explorer(to_shape.VCompound(), TopAbs.TopAbs_EDGE)) == 9


def test_multiple_inheritance_first_base_only():
    # R-MI, predicted in Design.md 9: IMeshData_Edge/Face/Wire : IMeshData_TessellatedShape, IMeshData_StatusOwner
    assert [c.__name__ for c in IMeshData.IMeshData_Edge.__mro__[:4]] == ["IMeshData_Edge", "IMeshData_TessellatedShape", "IMeshData_Shape", "Standard_Transient"]
    rows = read_report(REPORT)
    assert ("inheritance", "IMeshData", "IMeshData_Edge: additional base IMeshData_StatusOwner not declared (nanobind: single inheritance, offset-0 base only)") in rows
    assert all(cat != "misc" for cat, _, _ in rows)


def test_detected_noncopyable_and_hidden_placement_new():
    rows = read_report(REPORT)
    msgs = [msg for _, _, msg in rows]
    # R-NONCOPYABLE detected by the parser: CellFilter members, and a class holding such a class by value
    assert "BRepMesh_CircleTool: member myCellFilter of type NCollection_CellFilter<BRepMesh_CircleInspector> is not copyable -> bound through the non-copyable wrapper (R-NONCOPYABLE)" in msgs
    assert "BRepMesh_Delaun: member myCircles of type BRepMesh_CircleTool is not copyable -> bound through the non-copyable wrapper (R-NONCOPYABLE)" in msgs
    assert type(BRepMesh.BRepMesh_CircleTool).__name__ == "nb_type" and BRepMesh.BRepMesh_CircleTool.__name__ == "BRepMesh_CircleTool"
    # a Transient class with such a member cannot take the wrapper (the handle caster looks the OCCT class up): skipped
    assert not hasattr(BRepMesh, "BRepMesh_VertexTool")
    assert "BRepMesh_VertexTool: member myCellFilter of type NCollection_CellFilter<BRepMesh_VertexInspector> is not copyable and the class is Transient (no non-copyable wrapper possible) -> class skipped" in msgs
    # DEFINE_INC_ALLOC hides the placement operator new; the BRepMeshData_* implementation classes are non-trivially copyable
    # (bases, handles) so nanobind's copy wrapper cannot compile: skipped. BRepMeshData_Model (DEFINE_STANDARD_ALLOC) stays
    assert not hasattr(BRepMeshData, "BRepMeshData_Curve") and hasattr(BRepMeshData, "BRepMeshData_Model")
    assert any(m.startswith("BRepMeshData_Face: operator new is not public (no placement form) and the class is not trivially copyable") for m in msgs)
    # int (&)[3] parameters are fixed arrays (R-FIXED-ARRAY): a sequence of 3 in, a list of 3 out; std::pair<int, int>& is returned (R-OUT)
    tri = BRepMesh.BRepMesh_Triangle([1, 2, 3], [True, False, True], BRepMesh.BRepMesh_Free)
    assert tri.Edges() == ([1, 2, 3], [True, False, True]) and tri.myEdges == [1, 2, 3]
    tri.myOrientations = [False, False, False]
    assert tri.Edges()[1] == [False, False, False]
    # GetSplitSteps carries no Standard_EXPORT, so it is absent from libTKMesh on Windows and R-UNDEFINED skips it
    if not hasattr(BRepMesh.BRepMesh_ConeRangeSplitter, "GetSplitSteps"):
        assert any("BRepMesh_ConeRangeSplitter::GetSplitSteps" in msg and "no definition in lib" in msg for msg in msgs)
        return
    doc = BRepMesh.BRepMesh_ConeRangeSplitter.GetSplitSteps.__doc__
    assert "GetSplitSteps(self, theParameters: nanoocp.IMeshTools.IMeshTools_Parameters) -> tuple[tuple[float, float], tuple[int, int]]" in doc
