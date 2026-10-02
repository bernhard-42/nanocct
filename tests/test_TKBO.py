"""Generated bindings for TKBO: the boolean operations (BRepAlgoAPI_Fuse/Cut/Common/Section/Splitter, BOPAlgo, BOPDS, IntTools),
and the rule this toolkit introduced -- members re-exported with `using Base::name;` from a protected base (R-USING), which is
how every boolean gets SetFuzzyValue/SetRunParallel/HasErrors (build123d calls them)."""
import importlib
from pathlib import Path

import pytest

from generator.report import read_report
from nanocct import BOPAlgo, BOPDS, BOPTools, BVH, Bnd, BRepAlgoAPI, BRepCheck, BRepGProp, BRepPrimAPI, GProp, IntTools, Message, NCollection, TopAbs, TopExp, TopoDS, gp

PACKAGES = ["IntTools", "BOPAlgo", "BRepAlgoAPI", "BOPDS", "BOPTools"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKBO" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(shape, props)
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
    assert fuse.HasError(BOPAlgo.BOPAlgo_AlertBOPNotSet.get_type_descriptor_s()) is False
    for name in ("Clear", "ClearWarnings", "DumpErrors", "DumpWarnings", "FuzzyValue", "GetReport", "HasError", "HasErrors",
                 "HasWarning", "HasWarnings", "RunParallel", "SetFuzzyValue", "SetRunParallel", "SetUseOBB"):
        assert hasattr(BRepAlgoAPI.BRepAlgoAPI_Algo, name), name
    lines = REPORT.read_text().splitlines()
    # BOPAlgo_Options has DEFINE_STANDARD_ALLOC, so its operator new is inherited inaccessibly through the protected
    # base and BRepAlgoAPI_Algo cannot be constructed -- which costs nothing here, its own constructors are protected
    assert any(l.endswith("BRepAlgoAPI_Algo: non-public base BOPAlgo_Options provides operator new -> inaccessible, "
                          "class not constructible") for l in lines)


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
    # R-PTR-REF: Builder()/DSFiller() return BOPAlgo_Builder* const& / BOPAlgo_PaveFiller* const&; R-PTR-INCOMPLETE: PDS()
    # returns BOPDS_DS* (forward-declared in BOPAlgo_Builder.hxx, header included by the generator)
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


def test_the_box_trees_expose_their_bvh_tree():
    """BVH_PrimitiveSet<double, 2>::BVH() returns handle<BVH_Tree<double, 2>>, which 7c skipped as a
    handle -- the call raised TypeError. The tree classes were then bound empty, 2D and 3D alike: their members live in the
    partial specialisation BVH_Tree<T, N, BVH_BinaryTree> (BVH_BinaryTree.hxx) and 7c walked the empty primary template;
    since 2026-09-30 the specialisation is walked and its base BVH_TreeBase<T, N> is bound."""
    boxes2 = BOPTools.BOPTools_Box2dTree()
    for i, (x, y) in enumerate([(0.0, 0.0), (5.0, 5.0), (10.0, 0.0)]):
        boxes2.Add(i, Bnd.BVH_Box__double__2(BVH.BVH_Vec2d(x, y), BVH.BVH_Vec2d(x + 1.0, y + 1.0)))
    boxes2.Build()
    tree2 = boxes2.BVH()
    assert type(tree2).__name__ == "BVH_Tree__double__2__BVH_BinaryTree" and boxes2.Size() == 3
    assert tree2.Length() >= 1 and (tree2.MaxPoint(0).x(), tree2.MaxPoint(0).y()) == (11.0, 6.0)   # the root spans every box
    boxes3 = BOPTools.BOPTools_BoxTree()
    for i, (x, y, z) in enumerate([(0.0, 0.0, 0.0), (5.0, 5.0, 5.0), (20.0, 20.0, 20.0)]):
        boxes3.Add(i, Bnd.BVH_Box__double__3(BVH.BVH_Vec3d(x, y, z), BVH.BVH_Vec3d(x + 1.0, y + 1.0, z + 1.0)))
    boxes3.Build()
    tree3 = boxes3.BVH()
    assert [c.__name__ for c in type(tree3).__mro__[1:4]] == ["BVH_TreeBase__double__3", "BVH_TreeBaseTransient", "Standard_Transient"]
    assert (tree3.MinPoint(0).x(), tree3.MaxPoint(0).z()) == (0.0, 21.0) and tree3.Depth() >= 0
    by_hand = BVH.BVH_Tree__double__3__BVH_BinaryTree()                   # a Transient: held by a handle from the start
    assert by_hand.AddLeafNode(BVH.BVH_Vec3d(0.0, 0.0, 0.0), BVH.BVH_Vec3d(1.0, 2.0, 3.0), 0, 0) == 0
    assert (by_hand.Length(), by_hand.MaxPoint(0).z(), by_hand.GetRefCount()) == (1, 3.0, 1)