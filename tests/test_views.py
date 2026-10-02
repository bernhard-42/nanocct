"""R-VIEW: zero-copy numpy views over OCCT's contiguous arrays.

The rule is that array data which can get large crosses to Python as a view, never as a per-element loop.
The view is numpy's array protocol: `np.asarray(obj)` is a view, `np.array(obj)` a copy, and no class gets a
method OCCT does not have. Which classes need a view of their own is data (`overrides.toml [views]`); how
each one builds it is a `nanocct_def_views<T>` specialisation in `src/cpp/common/nanocct_views.h`, because
every case has runtime branches a config file cannot carry. The NCollection arrays get theirs from the
element table in `src/cpp/common/nanocct_elem_view.h`.
"""
import gc

import numpy as np
import pytest

from nanocct import (BRep, BRepMesh, BRepPrimAPI, Image, NCollection, Poly, Quantity, TopAbs,
                     TopExp, TopLoc, TopoDS, gp)


@pytest.fixture(scope="module")
def triangulation():
    shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(10.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(shape, 0.05, False, 0.1, True)
    ex = TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE)
    tri = BRep.BRep_Tool.Triangulation_s(TopoDS.Face(ex.Current()), TopLoc.TopLoc_Location())
    assert tri is not None and tri.NbNodes() > 100
    return tri


# ---------------------------------------------------------------------------------------------------------
# Poly_Triangulation: no method of its own. OCCT's Internal*() accessors return the triangulation's storage
# by reference, and those arrays carry __array__.

def test_nodes_and_triangles_are_views_that_agree_with_the_per_value_api(triangulation):
    t = triangulation
    nodes, tris = np.asarray(t.InternalNodes()), np.asarray(t.InternalTriangles())
    assert nodes.shape == (t.NbNodes(), 3) and tris.shape == (t.NbTriangles(), 3)
    assert tris.dtype == np.int32
    assert not nodes.flags["OWNDATA"] and not tris.flags["OWNDATA"]      # views, not copies
    p = t.Node(1)
    assert np.allclose(nodes[0], [p.X(), p.Y(), p.Z()])
    assert tuple(tris[0]) == t.Triangle(1).Get()                         # OCCT's 1-based indices, unchanged


def test_the_node_dtype_follows_the_object_not_the_binding(triangulation):
    """Poly_ArrayOfNodes stores gp_Pnt (stride 24) or NCollection_Vec3<float> (stride 12); one __array__ serves
    both, because nb::ndarray takes its dtype at run time. OCCT's default is double."""
    assert triangulation.IsDoublePrecision() is True
    assert np.asarray(triangulation.InternalNodes()).dtype == np.float64

    t = Poly.Poly_Triangulation()
    t.SetDoublePrecision(False)                          # only before allocation (OCCT raises afterwards)
    t.ResizeNodes(3, False)
    t.SetNode(2, gp.gp_Pnt(1, 2, 3))
    nodes = np.asarray(t.InternalNodes())
    assert nodes.dtype == np.float32 and nodes.shape == (3, 3)
    assert nodes[1].tolist() == [1.0, 2.0, 3.0]


def test_writes_go_through_the_view(triangulation):
    t = triangulation
    nodes = np.asarray(t.InternalNodes())
    before = t.Node(1).X()
    nodes[0, 0] = 42.0
    try:
        assert t.Node(1).X() == 42.0
    finally:
        nodes[0, 0] = before


def test_absent_arrays_are_empty_arrays_and_Has_says_whether_they_are_there(triangulation):
    """A triangulation without UV nodes or normals holds an empty array (measured: UV size 0 and not
    allocated, normals Lower/Upper 1/0). `__array__` has to return an array, so that is a zero-length view;
    "is it there" is OCCT's question, HasUVNodes()/HasNormals()."""
    t = triangulation
    assert t.HasUVNodes() and np.asarray(t.InternalUVNodes()).shape == (t.NbNodes(), 2)
    assert t.HasNormals() is False
    normals = np.asarray(t.InternalNormals())
    assert normals.shape == (0, 3) and normals.dtype == np.float32

    bare = Poly.Poly_Triangulation(3, 1, False, False)
    assert bare.HasUVNodes() is False and np.asarray(bare.InternalUVNodes()).shape == (0, 2)


def test_normals_are_always_float32():
    """Unlike the nodes and UV nodes, InternalNormals() is an NCollection_Array1<NCollection_Vec3<float>>,
    whatever the node precision -- the view comes from the container's element table, not a specialisation."""
    t = Poly.Poly_Triangulation(3, 1, True, True)
    assert t.IsDoublePrecision() is True and t.HasNormals() is True
    n = np.asarray(t.InternalNormals())
    assert n.shape == (3, 3) and n.dtype == np.float32 and not n.flags["OWNDATA"]
    n[1] = [0.0, 0.0, 1.0]
    assert t.Normal(2).Z() == 1.0


def test_a_const_accessor_hands_out_a_copy_not_the_storage(triangulation):
    """Triangles() returns `const NCollection_Array1<Poly_Triangle>&`, and the binding copies a const
    reference result -- so a view of it is a view of that copy, and writes never reach OCCT. The zero-copy
    route is InternalTriangles(). Pinned because it is easy to get wrong in the documentation."""
    t = triangulation
    copy = np.asarray(t.Triangles())
    before = t.Triangle(1).Get()
    copy[0] = [1, 1, 1]
    assert t.Triangle(1).Get() == before


def test_the_view_keeps_the_triangulation_alive():
    """rv_policy::reference_internal ties the view to the owner. Without it this is a use-after-free, and the
    poisoned read would usually still *look* right -- so the test drops every other reference and checks the
    values, which is the best a pure-Python test can do."""
    shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(5.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(shape, 0.5, False, 0.1, True)
    ex = TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE)
    tri = BRep.BRep_Tool.Triangulation_s(TopoDS.Face(ex.Current()), TopLoc.TopLoc_Location())
    nodes = np.asarray(tri.InternalNodes())
    expected = np.array(nodes)                      # a real copy, for comparison
    del tri, ex, shape
    gc.collect()
    assert np.array_equal(nodes, expected)
    assert nodes.base is not None                   # the owner is reachable from the view


def test_every_class_listed_in_overrides_has_a_specialisation():
    """A name in [views] without a nanocct_def_views<T> specialisation is a link error; this turns it into a
    test failure, which is the failure the developer can act on.

    The override file is read directly rather than through `generator.parse`, which imports libclang: the
    whole suite is also run against an installed wheel on three interpreters (the R-VIEW acceptance), and
    there the generator's own dependencies are not present.
    """
    import tomllib
    from pathlib import Path

    root = Path(__file__).parents[1]
    classes = tomllib.loads((root / "generator" / "overrides.toml").read_text())["views"]["classes"]
    header = (root / "src" / "cpp" / "common" / "nanocct_views.h").read_text()
    assert len(classes) > 0
    for name in classes:
        assert f"nanocct_def_views<{name}>" in header, name


# ---------------------------------------------------------------------------------------------------------
# numpy's protocol itself: __array__(dtype=None, copy=None). Measured on numpy 2.5.3: numpy casts a dtype
# itself, but trusts copy=True -- so the copy is __array__'s job.

def test_asarray_is_a_view_and_array_is_a_copy():
    a = NCollection.NCollection_Array1__double(1, 3)
    a.Init(1.5)
    view, copy = np.asarray(a), np.array(a)
    assert np.shares_memory(view, np.asarray(a)) and not np.shares_memory(copy, view)
    copy[0] = 7.0
    assert a.Value(1) == 1.5                        # the copy is independent
    view[0] = 7.0
    assert a.Value(1) == 7.0                        # the view is not


def test_copy_False_is_the_view_and_a_dtype_is_numpys_conversion():
    a = NCollection.NCollection_Array1__double(1, 3)
    a.Init(0.1)
    assert np.shares_memory(np.asarray(a, copy=False), np.asarray(a))
    f = np.asarray(a, dtype=np.float32)
    assert f.dtype == np.float32 and not np.shares_memory(f, np.asarray(a))
    with pytest.raises(ValueError):                 # a conversion cannot be a view; numpy says so itself
        np.asarray(a, dtype=np.float32, copy=False)


def test_a_copy_of_a_read_only_view_is_writable():
    a = NCollection.NCollection_Array1__gp_Dir(1, 1)
    c = np.array(a)
    assert c.flags["WRITEABLE"] and not np.asarray(a).flags["WRITEABLE"]


# ---------------------------------------------------------------------------------------------------------
# The generic containers (8.10a): NCollection_Array1/Array2 and their H- variants, for every element type
# that is a packed run of numpy scalars. The table lives in src/cpp/common/nanocct_elem_view.h and asserts
# its own layout assumptions at compile time.

def test_a_scalar_array_views_as_a_1d_array():
    a = NCollection.NCollection_Array1__double(1, 4)
    for i in range(1, 5):
        a.SetValue(i, i / 2)
    v = np.asarray(a)
    assert v.shape == (4,) and v.dtype == np.float64
    assert not v.flags["OWNDATA"]
    assert v.tolist() == [a.Value(i) for i in range(a.Lower(), a.Upper() + 1)]


def test_a_multi_component_element_gets_a_trailing_dimension():
    """gp_Pnt is three packed doubles, so an array of them is (N, 3) -- not (N,) of anything."""
    a = NCollection.NCollection_Array1__gp_Pnt(1, 3)
    for i in range(1, 4):
        a.SetValue(i, gp.gp_Pnt(i, i * 2, i * 3))
    v = np.asarray(a)
    assert v.shape == (3, 3) and v.dtype == np.float64
    assert v[1].tolist() == [2.0, 4.0, 6.0]
    v[0, 0] = 99.0
    assert a.Value(1).X() == 99.0                       # a view, not a copy


@pytest.mark.parametrize("k", [2, 3, 4])
@pytest.mark.parametrize("scalar, dtype", [("float", np.float32), ("double", np.float64), ("int", np.int32)])
def test_the_NCollection_vectors_view_like_any_packed_element(k, scalar, dtype):
    """NCollection_Vec2/3/4 are a plain `Element_t v[N]` (NCollection_Vec3.hxx:420); all nine bound arrays of
    them are in the element table."""
    a = getattr(NCollection, f"NCollection_Array1__NCollection_Vec{k}__{scalar}")(1, 2)
    v = np.asarray(a)
    assert v.shape == (2, k) and v.dtype == dtype and not v.flags["OWNDATA"]


def test_index_zero_of_the_view_is_Lower_whatever_Lower_is():
    """The view has no notion of OCCT's index base; that is the one thing a reader has to know."""
    a = NCollection.NCollection_Array1__int(5, 7)
    for i in range(5, 8):
        a.SetValue(i, i * 10)
    assert np.asarray(a).tolist() == [50, 60, 70]


def test_a_direction_array_is_read_only():
    """A gp_Dir is normalised by construction and every OCCT setter keeps it so. A raw write could leave a
    direction of length 0.3 in the array, which is not a gp_Dir -- so that one view is read-only."""
    a = NCollection.NCollection_Array1__gp_Dir(1, 2)
    a.SetValue(1, gp.gp_Dir(1, 0, 0))
    a.SetValue(2, gp.gp_Dir(0, 1, 0))
    v = np.asarray(a)
    assert v.shape == (2, 3) and not v.flags["WRITEABLE"]
    assert v.tolist() == [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
    with pytest.raises(ValueError):
        v[0, 0] = 0.3


def test_a_2d_array_views_row_major_and_matches_Value():
    """NCollection_Array2 allocates one contiguous buffer addressed row-major
    ((row - LowerRow) * NbColumns + (col - LowerCol), NCollection_Array2.hxx:306), so the view is direct."""
    a = NCollection.NCollection_Array2__double(1, 2, 1, 3)
    for r in range(1, 3):
        for c in range(1, 4):
            a.SetValue(r, c, r * 10 + c)
    v = np.asarray(a)
    assert v.shape == (2, 3)
    assert v.tolist() == [[11.0, 12.0, 13.0], [21.0, 22.0, 23.0]]
    a2 = NCollection.NCollection_Array2__gp_Pnt(1, 2, 1, 3)
    assert np.asarray(a2).shape == (2, 3, 3)            # the element's components come last


def test_the_handle_variants_inherit_the_view():
    """HArray1 derives from Array1 and HArray2 from Array2, so neither needs its own __array__."""
    h = NCollection.NCollection_HArray1__double(1, 3, 2.5)
    assert np.asarray(h).tolist() == [2.5, 2.5, 2.5]
    h2 = NCollection.NCollection_HArray2__int(1, 2, 1, 2, 7)
    assert np.asarray(h2).shape == (2, 2) and np.asarray(h2).dtype == np.int32


def test_an_element_that_cannot_be_viewed_has_no_array_protocol():
    """A handle, a string or a TopoDS_Shape has nothing packed to view, and the binder must not pretend.
    numpy then falls back to what it does for any iterable -- measured: an object array of copies."""
    assert not hasattr(NCollection.NCollection_Array1__TopoDS_Shape, "__array__")
    assert hasattr(NCollection.NCollection_Array1__double, "__array__")
    a = NCollection.NCollection_Array1__TopoDS_Shape(1, 2)
    assert np.asarray(a).dtype == object


def test_an_empty_array_views_as_an_empty_array_not_None():
    a = NCollection.NCollection_Array1__double()
    assert a.Size() == 0 and np.asarray(a).shape == (0,)
    assert np.array(a).shape == (0,)                    # the copy of nothing is nothing, not an error


def test_no_view_accessor_methods_are_left():
    """8.21: the six R-VIEW accessors of 8.10a read like OCCT methods and were replaced by __array__."""
    for cls, name in [(NCollection.NCollection_Array1__double, "ValuesArray"),
                      (NCollection.NCollection_Array2__double, "ValuesArray"),
                      (Poly.Poly_Triangulation, "NodesArray"), (Poly.Poly_Triangulation, "TrianglesArray"),
                      (Poly.Poly_Triangulation, "UVNodesArray"), (Poly.Poly_Triangulation, "NormalsArray"),
                      (Poly.Poly_PolygonOnTriangulation, "NodesArray"),
                      (Image.Image_PixMap, "DataArray"), (NCollection.NCollection_Buffer, "DataArray")]:
        assert not hasattr(cls, name), f"{cls.__name__}.{name}"


# ---------------------------------------------------------------------------------------------------------
# Image_PixMap (8.10a): the case that justifies the "how" being C++ -- padded rows and a row order that may
# run either way in memory.

def _pixmap(fmt, w, h, row_bytes=0):
    p = Image.Image_PixMap()
    assert p.InitZero(fmt, w, h, row_bytes)
    return p


def test_a_pixmap_views_as_height_width_channels():
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 5, 3)
    v = np.asarray(p)
    assert v.shape == (3, 5, 3) and v.dtype == np.uint8 and not v.flags["OWNDATA"]


@pytest.mark.parametrize("fmt, channels, dtype", [
    ("Image_Format_Gray", 1, np.uint8),
    ("Image_Format_RGB", 3, np.uint8),
    ("Image_Format_RGBA", 4, np.uint8),
    ("Image_Format_Gray16", 1, np.uint16),
    ("Image_Format_RGBF", 3, np.float32),
    ("Image_Format_RGBAF_half", 4, np.float16),
])
def test_the_dtype_and_channel_count_follow_the_format(fmt, channels, dtype):
    p = _pixmap(getattr(Image.Image_Format, fmt), 4, 2)
    v = np.asarray(p)
    assert v.shape == (2, 4, channels) and v.dtype == dtype


def test_padded_rows_are_a_stride_not_a_shear():
    """SizeRowBytes() is not always SizeX * SizePixelBytes -- a FreeImage-loaded 5-pixel-wide RGB image has
    16, not 15. A shape-only view would silently shear the image, so the row stride comes from
    SizeRowBytes()."""
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 5, 3, 16)
    assert p.SizeRowBytes() == 16 > 5 * p.SizePixelBytes()
    v = np.asarray(p)
    assert v.shape == (3, 5, 3)
    assert abs(v.strides[0]) == 16                      # the pad is skipped, not folded into the pixels
    v[1, 0] = [7, 8, 9]
    assert v[0, 0].tolist() == [0, 0, 0] and v[2, 0].tolist() == [0, 0, 0]   # neighbours untouched


def test_a_copy_of_a_padded_bottom_up_pixmap_is_the_same_image():
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 5, 3, 16)
    v = np.asarray(p)
    v[:] = np.arange(45, dtype=np.uint8).reshape(3, 5, 3)
    c = np.array(p)
    assert c.flags["OWNDATA"] and np.array_equal(c, v)


def test_row_order_is_top_down_even_when_the_storage_is_bottom_up():
    """OCCT hides the storage direction behind Row(i): myTopRowPtr is the *top* row and TopToDown is +1 or
    (size_t)-1. The view does the same, with a negative row stride, so view[y, x] is PixelColor(x, y)
    whatever IsTopDown() says -- a view that disagreed with the class's own accessors would be a trap."""
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 4, 3)
    assert p.IsTopDown() is False                       # OCCT's default for InitZero
    assert np.asarray(p).strides[0] < 0

    np.asarray(p)[0, 1] = [10, 20, 30]                  # top row, second pixel
    # Quantity_TOC_RGB, not sRGB: PixelColor stores the byte as-is unless asked to linearise, so reading it
    # back as sRGB re-encodes it and 10 comes out as 56.
    rgb = p.PixelColor(1, 0).GetRGB().Values(Quantity.Quantity_TypeOfColor.Quantity_TOC_RGB)
    assert [round(c * 255) for c in rgb] == [10, 20, 30]

    p.SetTopDown(True)                                  # same buffer, the other direction
    assert p.IsTopDown() is True and np.asarray(p).strides[0] > 0


def test_an_empty_pixmap_is_a_zero_size_view_of_its_format():
    """An empty pixmap still has a format -- Gray by default (measured) -- and so a dtype."""
    p = Image.Image_PixMap()
    assert p.IsEmpty() is True and p.Format() == Image.Image_Format.Image_Format_Gray
    v = np.asarray(p)
    assert v.shape == (0, 0, 1) and v.dtype == np.uint8


def test_an_UNKNOWN_pixmap_has_no_dtype_and_raises():
    """InitTrash accepts Image_Format_UNKNOWN and allocates real bytes (measured: 4x4 gives 16), but there is
    no dtype to give them; raw bytes would invent a meaning OCCT does not have."""
    p = Image.Image_PixMap()
    assert p.InitTrash(Image.Image_Format.Image_Format_UNKNOWN, 4, 4) is True and p.IsEmpty() is False
    with pytest.raises(ValueError, match="Image_Format_UNKNOWN"):
        np.asarray(p)


# ---------------------------------------------------------------------------------------------------------
# NCollection_Buffer, and the classes the container views reach without a specialisation of their own.

def test_a_buffer_views_as_bytes_and_as_empty_when_unallocated():
    """Before the view the class was unusable: Data()/ChangeData() are raw pointers, so nothing was bound but
    Size() and IsEmpty() -- which also made FSD_Base64.Decode_s, whose result *is* one of these, unusable."""
    b = NCollection.NCollection_Buffer(NCollection.NCollection_BaseAllocator.CommonBaseAllocator_s())
    assert b.Allocate(8) is True
    v = np.asarray(b)
    assert v.shape == (8,) and v.dtype == np.uint8 and not v.flags["OWNDATA"]
    v[:] = range(8)
    assert np.asarray(b).tolist() == list(range(8))

    # A buffer of size 0 is still *allocated* (the allocator hands back a non-null pointer for 0 bytes); after
    # Free() it is not. Both are zero-length views.
    assert NCollection.NCollection_Buffer(
        NCollection.NCollection_BaseAllocator.CommonBaseAllocator_s()).IsEmpty() is False
    b.Free()
    assert b.IsEmpty() is True and np.asarray(b).shape == (0,)


def test_base64_goes_both_ways_now():
    """R-VIEW made Decode's result readable; R-BYTES made Encode callable. Before the two, base64 went
    nowhere: Decode returned an NCollection_Buffer with no data access, and Encode was unbindable.
    """
    import base64

    from nanocct import FSD

    encoded = FSD.FSD_Base64.Encode_s(b"Hello, nanocct!").ToCString()
    assert encoded == base64.b64encode(b"Hello, nanocct!").decode()
    assert bytes(np.asarray(FSD.FSD_Base64.Decode_s(encoded, len(encoded)))) == b"Hello, nanocct!"
    assert FSD.FSD_Base64.Encode_s(b"").ToCString() == ""

    payload = bytes(range(256)) * 100                    # 25 600 bytes, well past one base64 block
    enc = FSD.FSD_Base64.Encode_s(payload).ToCString()
    assert bytes(np.asarray(FSD.FSD_Base64.Decode_s(enc, len(enc)))) == payload


def test_Graphic3d_Buffer_inherits_the_view():
    """Its elements are interleaved vertex attributes, so the buffer itself has no single element type:
    reshaping to (NbElements, Stride) and slicing by AttributeOffset() is the caller's business."""
    from nanocct import Graphic3d

    assert hasattr(Graphic3d.Graphic3d_Buffer, "__array__")


def test_a_polygon_is_reached_through_its_array_with_no_specialisation_of_its_own():
    """Poly_Polygon3D needs no entry in [views]: ChangeNodes() is bound reference_internal and returns a
    bound NCollection_Array1<gp_Pnt>, so the container view composes into a real zero-copy path and the
    chain of owners keeps the polygon alive."""
    a = NCollection.NCollection_Array1__gp_Pnt(1, 3)
    for i in range(1, 4):
        a.SetValue(i, gp.gp_Pnt(i, 0, 0))
    poly = Poly.Poly_Polygon3D(a)
    v = np.asarray(poly.ChangeNodes())
    assert v.shape == (3, 3) and not v.flags["OWNDATA"]
    v[0, 1] = 5.0
    assert poly.Nodes().Value(1).Y() == 5.0


def test_a_polygon_on_triangulation_is_reached_through_ChangeNodeArray():
    """Its node indices are an NCollection_Array1<int>; ChangeNodeArray() is the reference, Nodes() a copy."""
    idx = NCollection.NCollection_Array1__int(1, 3)
    for i in range(1, 4):
        idx.SetValue(i, i)
    p = Poly.Poly_PolygonOnTriangulation(idx)
    v = np.asarray(p.ChangeNodeArray())
    assert v.dtype == np.int32 and v.tolist() == [1, 2, 3] and not v.flags["OWNDATA"]
    v[0] = 9
    assert p.Node(1) == 9
