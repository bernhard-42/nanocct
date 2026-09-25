"""R-VIEW: zero-copy numpy views over OCCT's contiguous arrays (State.md 8.10).

The rule is that array data which can get large crosses to Python as a view, never as a per-element loop.
Which classes get views is data (`overrides.toml [views]`); how each one builds its view is a
`nanoocp_def_views<T>` specialisation in `src/cpp/common/nanoocp_views.h`, because every case has runtime
branches a config file cannot carry.
"""
import gc

import numpy as np
import pytest

from nanoocp import BRep, BRepMesh, BRepPrimAPI, Poly, TopAbs, TopExp, TopLoc, TopoDS


@pytest.fixture(scope="module")
def triangulation():
    shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(10.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(shape, 0.05, False, 0.1, True)
    ex = TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE)
    tri = BRep.BRep_Tool.Triangulation(TopoDS.Face(ex.Current()), TopLoc.TopLoc_Location())
    assert tri is not None and tri.NbNodes() > 100
    return tri


def test_nodes_and_triangles_are_views_that_agree_with_the_per_value_api(triangulation):
    t = triangulation
    nodes, tris = t.NodesArray(), t.TrianglesArray()
    assert nodes.shape == (t.NbNodes(), 3) and tris.shape == (t.NbTriangles(), 3)
    assert tris.dtype == np.int32
    assert not nodes.flags["OWNDATA"] and not tris.flags["OWNDATA"]      # views, not copies
    p = t.Node(1)
    assert np.allclose(nodes[0], [p.X(), p.Y(), p.Z()])
    assert tuple(tris[0]) == t.Triangle(1).Get()                         # OCCT's 1-based indices, unchanged


def test_the_node_dtype_follows_the_object_not_the_binding(triangulation):
    """Poly_ArrayOfNodes stores gp_Pnt (stride 24) or NCollection_Vec3<float> (stride 12); one accessor serves
    both, because nb::ndarray takes its dtype at run time. OCCT's default is double."""
    t = triangulation
    assert t.IsDoublePrecision() is True
    assert t.NodesArray().dtype == np.float64


def test_writes_go_through_the_view(triangulation):
    t = triangulation
    nodes = t.NodesArray()
    before = t.Node(1).X()
    nodes[0, 0] = 42.0
    try:
        assert t.Node(1).X() == 42.0
    finally:
        nodes[0, 0] = before


def test_absent_arrays_are_None_not_an_empty_array(triangulation):
    """UV nodes and normals are optional; a view cannot represent "not there", so the accessor returns None."""
    t = triangulation
    assert t.HasUVNodes() and t.UVNodesArray().shape == (t.NbNodes(), 2)
    assert t.HasNormals() is False and t.NormalsArray() is None


def test_the_view_keeps_the_triangulation_alive():
    """rv_policy::reference_internal ties the view to the owner. Without it this is a use-after-free, and the
    poisoned read would usually still *look* right -- so the test drops every other reference and checks the
    values, which is the best a pure-Python test can do."""
    shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(5.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(shape, 0.5, False, 0.1, True)
    ex = TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE)
    tri = BRep.BRep_Tool.Triangulation(TopoDS.Face(ex.Current()), TopLoc.TopLoc_Location())
    nodes = tri.NodesArray()
    expected = np.array(nodes)                      # a real copy, for comparison
    del tri, ex, shape
    gc.collect()
    assert np.array_equal(nodes, expected)
    assert nodes.base is not None                   # the owner is reachable from the view


def test_every_class_listed_in_overrides_has_a_specialisation():
    """A name in [views] without a nanoocp_def_views<T> specialisation is a link error; this turns it into a
    generation-time one, which is the failure the developer can act on."""
    from pathlib import Path

    from generator.parse import VIEW_CLASSES

    header = (Path(__file__).parents[1] / "src" / "cpp" / "common" / "nanoocp_views.h").read_text()
    for name in VIEW_CLASSES:
        assert f"nanoocp_def_views<{name}>" in header, name
