"""Generated bindings for TKShHealing: ShapeAnalysis, ShapeFix, ShapeUpgrade, ShapeCustom, ShapeBuild, ShapeExtend — the healing
packages build123d uses (ShapeAnalysis_FreeBounds, ShapeFix_Shape, ShapeUpgrade_UnifySameDomain). The last two container
instantiations build123d constructs directly (HSequence/Sequence<TopoDS_Shape>) arrive with this toolkit."""
import importlib
import math
from pathlib import Path

import pytest

from generator.report import read_report
from nanocct import (BRepBuilderAPI, BRepCheck, BRepGProp, BRepPrimAPI, GProp, NCollection, ShapeAnalysis, ShapeBuild, ShapeCustom,
                     ShapeExtend, ShapeFix, ShapeUpgrade, TopAbs, TopExp, TopoDS, gp)

PACKAGES = ["ShapeBuild", "ShapeExtend", "ShapeConstruct", "ShapeCustom", "ShapeAnalysis", "ShapeFix", "ShapeUpgrade", "ShapeAlgo",
            "ShapeProcess", "ShapeProcessAPI", "SHMessage"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKShHealing" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def _edges() -> NCollection.NCollection_HSequence:
    p = [gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(10, 0, 0), gp.gp_Pnt(10, 5, 0), gp.gp_Pnt(0, 5, 0)]
    edges = NCollection.NCollection_HSequence[TopoDS.TopoDS_Shape]()          # build123d: TopTools_HSequenceOfShape()
    for i in range(4):
        edges.Append(BRepBuilderAPI.BRepBuilderAPI_MakeEdge(p[i], p[(i + 1) % 4]).Edge())
    return edges


def test_connect_edges_to_wires_build123d_style():
    edges = _edges()
    assert len(edges) == 4 and isinstance(edges, NCollection.NCollection_Sequence[TopoDS.TopoDS_Shape])
    wires = ShapeAnalysis.ShapeAnalysis_FreeBounds.ConnectEdgesToWires_s(edges, 1e-7, False)     # static, no _s; handle returned
    assert type(wires).__name__ == "NCollection_HSequence__TopoDS_Shape" and len(wires) == 1
    assert wires.Value(1).ShapeType() == TopAbs.TopAbs_WIRE
    # the deprecated overload with the handle<HSequence>& out-parameter carries the R-COLLISION suffix and returns it too
    dep = ShapeAnalysis.ShapeAnalysis_FreeBounds.ConnectEdgesToWires_s__NCollection_HSequence__TopoDS_Shape
    assert "the suffix lists its returned out-parameters (nanocct R-COLLISION)" in dep.__doc__
    assert "Deprecated in OCCT: Use ConnectEdgesToWires() returning handle by value" in dep.__doc__
    assert len(dep(edges, 1e-7, False)) == 1
    # NCollection_Sequence<TopoDS_Shape> (8.7) arrived with ShapeFix
    seq = NCollection.NCollection_Sequence[TopoDS.TopoDS_Shape]()
    seq.Append(wires.Value(1))
    assert len(seq) == 1 and seq[1].IsSame(wires.Value(1))
    # a 10 x 5 wire from ShapeAnalysis, analysed by ShapeAnalysis_Wire (Check* return True when a problem was found)
    wire = TopoDS.Wire(wires.Value(1))
    face = BRepBuilderAPI.BRepBuilderAPI_MakeFace(wire, True).Face()
    saw = ShapeAnalysis.ShapeAnalysis_Wire(wire, face, 1e-7)
    assert saw.CheckClosed() is False and saw.NbEdges() == 4
    assert ShapeAnalysis.ShapeAnalysis.OuterWire_s(face).IsSame(wire)               # namespace-like static class, no _s
    edge = TopoDS.Edge(next(iter(TopExp.TopExp_Explorer(wire, TopAbs.TopAbs_EDGE))))
    assert ShapeAnalysis.ShapeAnalysis_Edge().IsClosed3d(edge) is False
    assert ShapeAnalysis.ShapeAnalysis_ShapeTolerance().Tolerance(face, 0) == pytest.approx(1e-7)


def test_shape_fix_and_upgrade():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
    sfs = ShapeFix.ShapeFix_Shape(box)
    sfs.Perform()
    assert BRepCheck.BRepCheck_Analyzer(sfs.Shape()).IsValid() and sfs.Shape().ShapeType() == TopAbs.TopAbs_SOLID
    assert sfs.Status(ShapeExtend.ShapeExtend_DONE) is True                     # R-ENUM: unscoped enumerator exported
    assert isinstance(sfs.Context(), ShapeBuild.ShapeBuild_ReShape)
    cyl = BRepPrimAPI.BRepPrimAPI_MakeCylinder(1.0, 2.0).Shape()
    usd = ShapeUpgrade.ShapeUpgrade_UnifySameDomain(cyl)
    usd.Build()
    assert sum(1 for _ in TopExp.TopExp_Explorer(usd.Shape(), TopAbs.TopAbs_FACE)) == 3
    assert usd.History() is not None                                               # R-CONST-TWIN: the non-const History() is bound
    sda = ShapeUpgrade.ShapeUpgrade_ShapeDivideAngle(math.pi / 2, cyl)
    sda.Perform()
    assert sum(1 for _ in TopExp.TopExp_Explorer(sda.Result(), TopAbs.TopAbs_FACE)) == 6
    scaled = ShapeCustom.ShapeCustom.ScaleShape_s(box, 2.0)
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(scaled, props)
    assert props.Mass() == pytest.approx(48.0)


def test_report():
    rows = read_report(REPORT)
    assert all(cat != "misc" for cat, _, _ in rows)
    msgs = [msg for _, _, msg in rows]
    # the std::bitset overload of ShapeProcess::Perform is bound since the R-BITSET caster (2026-09-22); a
    # function-pointer constructor is an inherent limit
    assert not any("std::bitset" in m for m in msgs)
    assert any(m.startswith("ShapeProcess_UOperator::ShapeProcess_UOperator(): param 'func': function pointer") for m in msgs)
    # R-UNDEFINED: a constructor declared but never defined in libTKShHealing
    assert any(m.startswith("ShapeFix_WireSegment::ShapeFix_WireSegment(const TopoDS_Wire &, const TopAbs_Orientation): declared") for m in msgs)
    sigs = [l for l in ShapeFix.ShapeFix_WireSegment.__init__.__doc__.splitlines() if l.startswith("__init__(self")]
    assert len(sigs) == 3                                                            # (), (WireData, ori), copy


def test_shape_process_operations_are_a_set_of_flags():
    """R-BITSET: ShapeProcess::OperationsFlags is a std::bitset indexed by ShapeProcess::Operation, so Python passes
    the set of enumerators. The name-taking Perform overload stays reachable because the caster rejects a str."""
    from nanocct.ShapeProcess import ShapeProcess, ShapeProcess_Context
    assert ShapeProcess.ToOperationFlag_s("FixShape") == (ShapeProcess.FixShape, True)
    assert ShapeProcess.ToOperationFlag_s("no-such-operation")[1] is False
    overloads = [l for l in ShapeProcess.Perform_s.__doc__.splitlines() if l.startswith("Perform_s(")]
    assert len(overloads) == 2
    assert any("seq: str" in l for l in overloads) and any("theOperations: set[int]" in l for l in overloads)
    context = ShapeProcess_Context()
    assert ShapeProcess.Perform_s(context, set()) is False                    # nothing to do, no operator performed
    assert ShapeProcess.Perform_s(context, "no-such-sequence") is False       # the str overload is still selected
