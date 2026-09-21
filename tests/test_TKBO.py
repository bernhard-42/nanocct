"""Generated bindings for TKBO: the boolean operations (BRepAlgoAPI_Fuse/Cut/Common/Section/Splitter, BOPAlgo, BOPDS, IntTools),
and the rule this toolkit introduced -- members re-exported with `using Base::name;` from a protected base (R-USING), which is
how every boolean gets SetFuzzyValue/SetRunParallel/HasErrors (build123d calls them)."""
import importlib
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import BOPAlgo, BOPDS, BOPTools, BRepAlgoAPI, BRepCheck, BRepGProp, BRepPrimAPI, GProp, IntTools, Message, NCollection, TopAbs, TopExp, TopoDS, gp

PACKAGES = ["IntTools", "BOPAlgo", "BRepAlgoAPI", "BOPDS", "BOPTools"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKBO" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties(shape, props)
    return props.Mass()


def _boxes() -> tuple[TopoDS.TopoDS_Shape, TopoDS.TopoDS_Shape]:
    """Two 2 x 2 x 2 cubes overlapping in a unit cube."""
    return (BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape(),
            BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(1, 1, 1), gp.gp_Pnt(3, 3, 3)).Shape())


def test_booleans():
    a, b = _boxes()
    fuse = BRepAlgoAPI.BRepAlgoAPI_Fuse(a, b)
    assert fuse.IsDone() and _volume(fuse.Shape()) == pytest.approx(15.0) and BRepCheck.BRepCheck_Analyzer(fuse.Shape()).IsValid()
    assert _volume(BRepAlgoAPI.BRepAlgoAPI_Cut(a, b).Shape()) == pytest.approx(7.0)
    assert _volume(BRepAlgoAPI.BRepAlgoAPI_Common(a, b).Shape()) == pytest.approx(1.0)
    assert TopoDS.TopoDS_Shape(fuse).IsSame(fuse.Shape())                                  # R-CONV through MakeShape
    face = next(iter(TopExp.TopExp_Explorer(a, TopAbs.TopAbs_FACE)))
    assert isinstance(fuse.Modified(face), NCollection.NCollection_List[TopoDS.TopoDS_Shape])
    section = BRepAlgoAPI.BRepAlgoAPI_Section(a, gp.gp_Pln(gp.gp_Pnt(1, 0, 0), gp.gp_Dir(1, 0, 0)))
    section.Build()
    assert sum(1 for _ in TopExp.TopExp_Explorer(section.Shape(), TopAbs.TopAbs_EDGE)) == 4


def test_using_declarations_of_the_protected_options_base():
    # R-USING: BRepAlgoAPI_Algo : protected BOPAlgo_Options re-exports 14 members with `using BOPAlgo_Options::X;`;
    # they are bound on BRepAlgoAPI_Algo through lambdas (the base itself is not a Python base of the class)
    a, b = _boxes()
    fuse = BRepAlgoAPI.BRepAlgoAPI_Fuse(a, b)
    assert BOPAlgo.BOPAlgo_Options not in type(fuse).__mro__ and BRepAlgoAPI.BRepAlgoAPI_Algo in type(fuse).__mro__
    assert fuse.HasErrors() is False and fuse.HasWarnings() is False
    assert fuse.FuzzyValue() == pytest.approx(1e-7) and fuse.RunParallel() is False
    fuse.SetFuzzyValue(1e-5)                                                                # build123d's calls
    fuse.SetRunParallel(True)
    assert fuse.FuzzyValue() == pytest.approx(1e-5) and fuse.RunParallel() is True
    assert isinstance(fuse.GetReport(), Message.Message_Report)
    assert fuse.DumpErrors() == ""                                                          # R-STREAM-OUT through the using
    assert fuse.HasError(BOPAlgo.BOPAlgo_AlertBOPNotSet.get_type_descriptor()) is False
    for name in ("Clear", "ClearWarnings", "DumpErrors", "DumpWarnings", "FuzzyValue", "GetReport", "HasError", "HasErrors",
                 "HasWarning", "HasWarnings", "RunParallel", "SetFuzzyValue", "SetRunParallel", "SetUseOBB"):
        assert hasattr(BRepAlgoAPI.BRepAlgoAPI_Algo, name), name
    lines = REPORT.read_text().splitlines()
    assert any(l.endswith("BRepAlgoAPI_Algo: non-public base BOPAlgo_Options dropped; class not constructible") for l in lines)


def test_general_fuse_splitter_and_bop():
    a, b = _boxes()
    args = NCollection.NCollection_List[TopoDS.TopoDS_Shape]()
    args.Append(a)
    args.Append(b)
    gf = BRepAlgoAPI.BRepAlgoAPI_BuilderAlgo()
    gf.SetArguments(args)
    gf.Build()
    assert gf.IsDone() and sum(1 for _ in TopExp.TopExp_Explorer(gf.Shape(), TopAbs.TopAbs_SOLID)) == 3
    splitter = BRepAlgoAPI.BRepAlgoAPI_Splitter()
    splitter.SetArguments(args)
    tools = NCollection.NCollection_List[TopoDS.TopoDS_Shape]()
    tools.Append(BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(0, 0, 1), gp.gp_Pnt(3, 3, 1.5)).Shape())
    splitter.SetTools(tools)
    splitter.Build()
    assert sum(1 for _ in TopExp.TopExp_Explorer(splitter.Shape(), TopAbs.TopAbs_SOLID)) == 7
    bop = BOPAlgo.BOPAlgo_BOP()
    bop.AddArgument(a)
    bop.AddTool(b)
    bop.SetOperation(BOPAlgo.BOPAlgo_FUSE)                      # R-ENUM: exported enumerator
    bop.Perform()
    assert _volume(bop.Shape()) == pytest.approx(15.0)
    assert [e.name for e in BOPAlgo.BOPAlgo_Operation] == ["BOPAlgo_COMMON", "BOPAlgo_FUSE", "BOPAlgo_CUT", "BOPAlgo_CUT21", "BOPAlgo_SECTION", "BOPAlgo_UNKNOWN"]


def test_general_fuse_internals_are_reachable():
    # R-PTR-REF: Builder()/DSFiller() return BOPAlgo_Builder*& / BOPAlgo_PaveFiller*&; R-PTR-INCOMPLETE: PDS() returns BOPDS_DS*
    # (forward-declared in BOPAlgo_Builder.hxx, header included by the generator)
    a, b = _boxes()
    fuse = BRepAlgoAPI.BRepAlgoAPI_Fuse(a, b)
    builder, filler = fuse.Builder(), fuse.DSFiller()
    assert type(builder) is BOPAlgo.BOPAlgo_BOP and type(filler) is BOPAlgo.BOPAlgo_PaveFiller
    ds = builder.PDS()
    assert type(ds) is BOPDS.BOPDS_DS and ds.NbSourceShapes() == 68 and ds.NbShapes() > ds.NbSourceShapes()
    assert len(builder.Images()) > 0 and filler.PDS().NbShapes() == ds.NbShapes()


def test_data_structures_hashes_and_report():
    assert BOPDS.BOPDS_DS().NbShapes() == 0
    assert type(IntTools.IntTools_Context()).__name__ == "IntTools_Context"
    # R-HASH: OCCT specialises std::hash for BOPTools_Set and BOPDS_Pave
    assert "__hash__" in BOPTools.BOPTools_Set.__dict__ and "__hash__" in BOPDS.BOPDS_Pave.__dict__
    rows = read_report(REPORT)
    assert all(cat != "misc" for cat, _, _ in rows)
    msgs = [msg for _, _, msg in rows]
    # the BVH-based box trees are bound through the template chain (R-TEMPLATE-BASE); the 2D pair selector is an OCCT bug
    # (its RejectNode builds a 3D box from 2D vectors) and skipped by overrides.toml
    assert hasattr(BOPTools, "BOPTools_BoxTree") and hasattr(BOPTools, "BOPTools_BoxPairSelector") and not hasattr(BOPTools, "BOPTools_Box2dPairSelector")
    tree = BOPTools.BOPTools_BoxTree()
    assert tree.Size() == 0 and any("BOPTools_PairSelector<2>: skipped (overrides.toml [skip] classes)" in m for m in msgs)
    # R-COLLISION on out-int overloads
    assert hasattr(BOPDS.BOPDS_PaveBlock, "HasEdge") and hasattr(BOPDS.BOPDS_PaveBlock, "HasEdge__int")
    # an rvalue-reference parameter is skipped (BOPAlgo_PaveFiller::SetArguments(List&&)); the const& overload remains
    assert any(m.startswith("BOPAlgo_PaveFiller::SetArguments(): param 'theLS': rvalue reference") for m in msgs)
    assert BOPAlgo.BOPAlgo_PaveFiller.SetArguments.__doc__.count("SetArguments(self") >= 1
