"""nanoocp.AddOns -- the additions that are not a 1:1 binding of OCCT (State.md 8.10b).

Everything else in nanoOCP mirrors an OCCT class. These do not, so they live in their own package: a reader
of `AddOns.Tessellator.NormalsFromSurface(...)` can see at a glance that it is ours.

Both helpers exist because a zero-copy view cannot express them. A view moves data that is already there;
these *compute*, one OCCT call per node or per edge, and that loop has to stay out of Python.
"""
import numpy as np
import pytest

from nanoocp import (AddOns, BRep, BRepMesh, BRepPrimAPI, BRepTools, NCollection, TopAbs, TopExp,
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
    assert AddOns.Tessellator.__name__ == "nanoocp.AddOns.Tessellator"
    import nanoocp.AddOns.Tessellator as T           # importable as a module path, not only as an attribute
    assert T is AddOns.Tessellator


def test_normals_from_surface_matches_the_per_node_loop(meshed):
    face = _first_face(meshed)
    tri = BRep.BRep_Tool.Triangulation_s(face, TopLoc.TopLoc_Location())
    u_min, u_max, v_min, v_max = BRepTools.BRepTools.UVBounds_s(face)
    uv = np.ascontiguousarray(np.clip(np.asarray(tri.UVNodesArray()), [u_min, v_min], [u_max, v_max]))

    bulk = AddOns.Tessellator.NormalsFromSurface(face, uv)
    assert bulk.shape == (tri.NbNodes(), 3) and bulk.dtype == np.float64

    from nanoocp import BRepGProp
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
    uv = np.ascontiguousarray(np.clip(np.asarray(tri.UVNodesArray()), [u_min, v_min], [u_max, v_max]))
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
    from nanoocp import BRepAdaptor

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
