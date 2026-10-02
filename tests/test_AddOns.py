"""nanocct.AddOns -- the additions that are not a 1:1 binding of OCCT.

Everything else in nanocct mirrors an OCCT class. These do not, so they live in their own package: a reader
of `AddOns.Tessellator.NormalsFromSurface(...)` can see at a glance that it is ours.

Both helpers exist because a zero-copy view cannot express them. A view moves data that is already there;
these *compute*, one OCCT call per node or per edge, and that loop has to stay out of Python.
"""
import numpy as np
import pytest

from nanocct import (AddOns, BRep, BRepMesh, BRepPrimAPI, BRepTools, NCollection, TopAbs, TopExp,
                     TopLoc, TopoDS, gp)


@pytest.fixture(scope="module")
def meshed():
    shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(10.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(shape, 0.1, False, 0.2, True)
    return shape


def _first_face(shape):
    m = NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher()
    TopExp.TopExp.MapShapes_s(shape, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE, m)
    return TopoDS.Face(m.FindKey(1))


def test_the_package_is_not_pretending_to_be_occt():
    assert AddOns.Tessellator.__name__ == "nanocct.AddOns.Tessellator"
    import nanocct.AddOns.Tessellator as T           # importable as a module path, not only as an attribute
    assert T is AddOns.Tessellator


def test_normals_from_surface_matches_the_per_node_loop(meshed):
    face = _first_face(meshed)
    tri = BRep.BRep_Tool.Triangulation_s(face, TopLoc.TopLoc_Location())
    u_min, u_max, v_min, v_max = BRepTools.BRepTools.UVBounds_s(face)
    uv = np.ascontiguousarray(np.clip(np.asarray(tri.InternalUVNodes()), [u_min, v_min], [u_max, v_max]))

    bulk = AddOns.Tessellator.NormalsFromSurface(face, uv)
    assert bulk.shape == (tri.NbNodes(), 3) and bulk.dtype == np.float64

    from nanocct import BRepGProp
    prop = BRepGProp.BRepGProp_Face(face)
    p, n = gp.gp_Pnt(), gp.gp_Vec()
    for i in (0, len(uv) // 2, len(uv) - 1):
        prop.Normal(float(uv[i, 0]), float(uv[i, 1]), p, n)
        if n.SquareMagnitude() > 0:
            n.Normalize()
        assert np.allclose(bulk[i], [n.X(), n.Y(), n.Z()]), i
    assert np.allclose(np.linalg.norm(bulk, axis=1), 1.0)          # normalised


def test_normals_reverse_flag_negates(meshed):
    face = _first_face(meshed)
    tri = BRep.BRep_Tool.Triangulation_s(face, TopLoc.TopLoc_Location())
    u_min, u_max, v_min, v_max = BRepTools.BRepTools.UVBounds_s(face)
    uv = np.ascontiguousarray(np.clip(np.asarray(tri.InternalUVNodes()), [u_min, v_min], [u_max, v_max]))
    assert np.allclose(AddOns.Tessellator.NormalsFromSurface(face, uv, True),
                       -AddOns.Tessellator.NormalsFromSurface(face, uv, False))


def test_normals_rejects_a_wrong_shape(meshed):
    with pytest.raises(ValueError, match=r"\(N, 2\)"):
        AddOns.Tessellator.NormalsFromSurface(_first_face(meshed), np.zeros((4, 3)))


def test_edge_segments_are_consecutive_point_pairs(meshed):
    seg, per_edge, edge_types = AddOns.Tessellator.EdgeSegments(meshed)
    assert seg.ndim == 2 and seg.shape[1] == 3 and seg.dtype == np.float64
    assert per_edge.dtype == np.int32 and edge_types.dtype == np.int32
    # two endpoints per segment, and the counts account for every point
    assert len(seg) == 2 * int(per_edge.sum())
    # consecutive pairs share a point: segment i's end is segment i+1's start, within one edge.
    # Not every edge has two segments -- find one that does rather than assume the first.
    start = 0
    for count in per_edge:
        if count >= 2:
            assert np.allclose(seg[2 * start + 1], seg[2 * start + 2])
            break
        start += int(count)
    else:
        pytest.skip("no edge with more than one segment")


def test_edge_types_align_with_the_counts_and_match_BRepAdaptor(meshed):
    """One type per kept edge, and it is BRepAdaptor_Curve's -- the value ocp-tessellate records.

    The type has to come out of the helper because the helper is what decides which edges are kept: it
    skips an edge with no ancestor face, no triangulation or no polygon on it, and a Python loop over the
    edge map cannot tell which those were without redoing those lookups.
    """
    from nanocct import BRepAdaptor

    _seg, per_edge, edge_types = AddOns.Tessellator.EdgeSegments(meshed)
    assert len(edge_types) == len(per_edge) > 0

    # a sphere's edges all survive, so the two orders can be compared directly
    m = NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher()
    TopExp.TopExp.MapShapes_s(meshed, TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE, m)
    assert m.Extent() == len(edge_types)
    expected = [BRepAdaptor.BRepAdaptor_Curve(TopoDS.Edge(m.FindKey(i))).GetType().value
                for i in range(1, m.Extent() + 1)]
    assert list(edge_types) == expected


def test_edge_segments_needs_a_mesh():
    """An unmeshed shape has no triangulation, so every edge is skipped rather than raising."""
    seg, per_edge, edge_types = AddOns.Tessellator.EdgeSegments(
        BRepPrimAPI.BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape())
    assert len(per_edge) == 0 and len(seg) == 0 and len(edge_types) == 0


# ---- AddOns.ShapeClean: a workaround for OCCT issue #1541, removed once OCCT is fixed (Binding-Rules.md R-ADDON) ------------
#
# The reproducer is build123d's `Box(1, 1, 1) - Pos(...) * Sphere(0.5)`: the sphere's centre lies outside the box, so
# the cut circle on the face x = -0.5 is a full circle, and the sphere's seam splits it into two arcs. Unifying the two
# spherical faces makes those arcs a closed chain, whose pcurves ShapeUpgrade_UnifySameDomain concatenates starting at
# the wrong junction.

from nanocct import (BRepAdaptor, BRepAlgoAPI, BRepCheck, BRepGProp, GeomAbs, GProp, ShapeUpgrade,  # noqa: E402
                     TopTools)

_EDGE, _FACE, _VERTEX = (TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE,
                         TopAbs.TopAbs_ShapeEnum.TopAbs_VERTEX)
_OCCT = ShapeUpgrade.ShapeUpgrade_UnifySameDomain
_ADDON = AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain


def _box_minus_sphere(x, y, z, r=0.5):
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(-0.5, -0.5, -0.5), 1.0, 1.0, 1.0).Shape()
    return BRepAlgoAPI.BRepAlgoAPI_Cut(box, BRepPrimAPI.BRepPrimAPI_MakeSphere(gp.gp_Pnt(x, y, z), r).Shape()).Shape()


@pytest.fixture(scope="module")
def closed_circle_cut():
    return _box_minus_sphere(-0.8941468682889828, -0.05608050987114277, 0.16128077950256148)


def _subshapes(shape, kind):
    m = NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher()
    TopExp.TopExp.MapShapes_s(shape, kind, m)
    return [m.FindKey(i) for i in range(1, m.Extent() + 1)]


def _unify(cls, shape):
    """What build123d's Shape.clean and every boolean do."""
    unifier = cls(shape, True, True, True)
    unifier.AllowInternalEdges(False)
    unifier.Build()
    return unifier


def _max_edge_tolerance(shape):
    return max(BRep.BRep_Tool.Tolerance_s(TopoDS.Edge(e)) for e in _subshapes(shape, _EDGE))


def _volume(shape):
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def test_occt_still_breaks_the_closed_circle(closed_circle_cut):
    """The canary. When this fails, OCCT has fixed #1541: switch build123d back to
    nanocct.ShapeUpgrade.ShapeUpgrade_UnifySameDomain and delete AddOns.ShapeClean (Binding-Rules.md R-ADDON)."""
    result = _unify(_OCCT, closed_circle_cut).Shape()
    broken = not BRepCheck.BRepCheck_Analyzer(result).IsValid() or _max_edge_tolerance(result) > 1e-3
    assert broken, ("OCCT issue #1541 looks fixed: ShapeUpgrade_UnifySameDomain now cleans the closed-circle "
                    "reproducer correctly. Remove nanocct.AddOns.ShapeClean and its use in nanocctbuild's build123d patch.")


def test_shape_clean_carries_the_occt_name_and_signatures():
    """Reverting is an import change only if every member build123d calls is spelled as OCCT's binding spells it."""
    assert _ADDON.__name__ == _OCCT.__name__ == "ShapeUpgrade_UnifySameDomain"
    assert _ADDON.__module__ == "nanocct.AddOns.ShapeClean" and _ADDON is not _OCCT
    import nanocct.AddOns.ShapeClean as S
    assert S is AddOns.ShapeClean
    for member in ("__init__", "AllowInternalEdges", "Build", "Shape", "History"):
        ours = getattr(_ADDON, member).__nb_signature__
        theirs = getattr(_OCCT, member).__nb_signature__
        assert len(ours) == 1 and ours[0] in theirs, member   # signature, docstring and defaults


def test_shape_clean_merges_the_closed_circle_validly(closed_circle_cut):
    result = _unify(_ADDON, closed_circle_cut).Shape()
    assert BRepCheck.BRepCheck_Analyzer(result).IsValid()
    assert _max_edge_tolerance(result) <= 1e-6
    assert not any(BRep.BRep_Tool.Degenerated_s(TopoDS.Edge(e)) for e in _subshapes(result, _EDGE))
    assert abs(_volume(result) - _volume(closed_circle_cut)) < 1e-6
    # the two spherical faces became one, bounded by ONE closed circle -- not by the two arcs it was cut into
    spheres = [TopoDS.Face(f) for f in _subshapes(result, _FACE)
               if BRepAdaptor.BRepAdaptor_Surface(TopoDS.Face(f)).GetType() == GeomAbs.GeomAbs_SurfaceType.GeomAbs_Sphere]
    assert len(spheres) == 1
    (circle,) = _subshapes(spheres[0], _EDGE)
    curve = BRepAdaptor.BRepAdaptor_Curve(TopoDS.Edge(circle))
    assert curve.GetType() == GeomAbs.GeomAbs_CurveType.GeomAbs_Circle and curve.IsClosed()
    assert (len(_subshapes(result, _FACE)), len(_subshapes(result, _EDGE)), len(_subshapes(result, _VERTEX))) == (7, 13, 9)


def test_shape_clean_history_runs_from_the_input_to_the_result(closed_circle_cut):
    """Three histories are composed (face pass, edge pass, circle merge); build123d reads the composition."""
    unifier = _unify(_ADDON, closed_circle_cut)
    result, history = unifier.Shape(), unifier.History()
    in_result = NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher()
    for kind in (_FACE, _EDGE, _VERTEX):
        TopExp.TopExp.MapShapes_s(result, kind, in_result)

    def is_sphere(f):
        return BRepAdaptor.BRepAdaptor_Surface(TopoDS.Face(f)).GetType() == GeomAbs.GeomAbs_SurfaceType.GeomAbs_Sphere

    ef = NCollection.NCollection_IndexedDataMap[TopoDS.TopoDS_Shape, NCollection.NCollection_List[TopoDS.TopoDS_Shape],
                                                TopTools.TopTools_ShapeMapHasher]()
    TopExp.TopExp.MapShapesAndAncestors_s(closed_circle_cut, _EDGE, _FACE, ef)
    arcs = [ef.FindKey(i) for i in range(1, ef.Extent() + 1)
            if sum(is_sphere(f) for f in ef.FindFromIndex(i)) == 1 and ef.FindFromIndex(i).Size() == 2]
    assert len(arcs) == 2                       # the cut circle, split by the seam
    images = [list(history.Modified(a)) for a in arcs]
    assert all(len(i) == 1 for i in images) and images[0][0].IsSame(images[1][0])
    assert in_result.Contains(images[0][0])     # both arcs map to the one circle that is in the result
    # every input face either survives, is removed, or maps to something in the result
    for f in _subshapes(closed_circle_cut, _FACE):
        assert in_result.Contains(f) or history.IsRemoved(f) or all(in_result.Contains(m) for m in history.Modified(f))


@pytest.mark.parametrize("centre", [(0.0, 0.0, 0.3), (-0.5, 0.5, 0.5), (0.2, -0.1, 0.9)],
                         ids=["inside", "corner", "cap-above"])
def test_shape_clean_leaves_everything_else_to_occt(centre):
    """Without a closed circle to protect, the result is OCCT's: same topology, same validity."""
    raw = _box_minus_sphere(*centre)
    ours, theirs = _unify(_ADDON, raw).Shape(), _unify(_OCCT, raw).Shape()
    for kind in (_FACE, _EDGE, _VERTEX):
        assert len(_subshapes(ours, kind)) == len(_subshapes(theirs, kind))
    assert BRepCheck.BRepCheck_Analyzer(ours).IsValid() == BRepCheck.BRepCheck_Analyzer(theirs).IsValid() is True


def test_shape_clean_over_random_orientations():
    """The failure depends on where the sphere's seam falls. Rotate the sphere at random with its centre outside the
    box: OCCT breaks some of these cuts, the AddOn none."""
    import random
    from nanocct import BRepBuilderAPI

    rng = random.Random(7)
    occt_broken = 0
    for _ in range(40):
        r = rng.uniform(0.2, 0.45)
        axis = gp.gp_Dir(rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-1, 1) + 1e-3)
        trsf = gp.gp_Trsf()
        trsf.SetRotation(gp.gp_Ax1(gp.gp_Pnt(0, 0, 0), axis), rng.uniform(0, 6.283))
        move = gp.gp_Trsf()
        move.SetTranslation(gp.gp_Vec(rng.uniform(-0.45 + r, 0.45 - r), rng.uniform(-0.45 + r, 0.45 - r),
                                      0.5 + rng.uniform(0.05, 0.9) * r))
        sphere = BRepBuilderAPI.BRepBuilderAPI_Transform(BRepPrimAPI.BRepPrimAPI_MakeSphere(r).Shape(), trsf).Shape()
        sphere = BRepBuilderAPI.BRepBuilderAPI_Transform(sphere, move).Shape()
        box = BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(-0.5, -0.5, -0.5), 1.0, 1.0, 1.0).Shape()
        raw = BRepAlgoAPI.BRepAlgoAPI_Cut(box, sphere).Shape()
        ours, theirs = _unify(_ADDON, raw).Shape(), _unify(_OCCT, raw).Shape()
        assert BRepCheck.BRepCheck_Analyzer(ours).IsValid() and _max_edge_tolerance(ours) <= 1e-6
        occt_broken += not BRepCheck.BRepCheck_Analyzer(theirs).IsValid() or _max_edge_tolerance(theirs) > 1e-3
    assert occt_broken > 0                      # the sweep did exercise the bug


def test_every_submodule_has_its_stub_in_the_package():
    """nanocct.AddOns was one module file, so nanobind's stubgen wrote the submodules' stubs as
    nanocct/ShapeClean.pyi and nanocct/Tessellator.pyi -- stubs of modules that do not exist -- and every AddOns name
    was Any to a type checker. The package now carries them next to its own __init__.pyi."""
    import types
    from pathlib import Path
    subs = sorted(n for n, v in vars(AddOns).items() if isinstance(v, types.ModuleType) and v.__name__ == f"nanocct.AddOns.{n}")
    assert len(subs) > 0
    here = Path(AddOns.__file__).parent
    assert here.name == "AddOns" and (here / "__init__.pyi").is_file()
    assert [n for n in subs if not (here / f"{n}.pyi").is_file()] == []
    assert [n for n in subs if (here.parent / f"{n}.pyi").exists()] == []
