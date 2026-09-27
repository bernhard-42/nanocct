"""R-VIEW: zero-copy numpy views over OCCT's contiguous arrays (State.md 8.10).

The rule is that array data which can get large crosses to Python as a view, never as a per-element loop.
Which classes get views is data (`overrides.toml [views]`); how each one builds its view is a
`ocp3x_def_views<T>` specialisation in `src/cpp/common/ocp3x_views.h`, because every case has runtime
branches a config file cannot carry.
"""
import gc

import numpy as np
import pytest

from OCP3x import (BRep, BRepMesh, BRepPrimAPI, Image, NCollection, Poly, Quantity, TopAbs,
                     TopExp, TopLoc, TopoDS, gp)


@pytest.fixture(scope="module")
def triangulation():
    shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(10.0).Shape()
    BRepMesh.BRepMesh_IncrementalMesh(shape, 0.05, False, 0.1, True)
    ex = TopExp.TopExp_Explorer(shape, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE)
    tri = BRep.BRep_Tool.Triangulation_s(TopoDS.Face(ex.Current()), TopLoc.TopLoc_Location())
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
    tri = BRep.BRep_Tool.Triangulation_s(TopoDS.Face(ex.Current()), TopLoc.TopLoc_Location())
    nodes = tri.NodesArray()
    expected = np.array(nodes)                      # a real copy, for comparison
    del tri, ex, shape
    gc.collect()
    assert np.array_equal(nodes, expected)
    assert nodes.base is not None                   # the owner is reachable from the view


def test_every_class_listed_in_overrides_has_a_specialisation():
    """A name in [views] without a ocp3x_def_views<T> specialisation is a link error; this turns it into a
    generation-time one, which is the failure the developer can act on.

    The override file is read directly rather than through `generator.parse`, which imports libclang: the
    whole suite is also run against an installed wheel on three interpreters (the R-VIEW acceptance), and
    there the generator's own dependencies are not present.
    """
    import tomllib
    from pathlib import Path

    root = Path(__file__).parents[1]
    classes = tomllib.loads((root / "generator" / "overrides.toml").read_text())["views"]["classes"]
    header = (root / "src" / "cpp" / "common" / "ocp3x_views.h").read_text()
    assert len(classes) > 0
    for name in classes:
        assert f"ocp3x_def_views<{name}>" in header, name


# ---------------------------------------------------------------------------------------------------------
# The generic containers (8.10a): NCollection_Array1/Array2 and their H- variants, for every element type
# that is a packed run of numpy scalars. The table lives in src/cpp/common/ocp3x_elem_view.h and asserts
# its own layout assumptions at compile time.

def test_a_scalar_array_views_as_a_1d_array():
    a = NCollection.NCollection_Array1__double(1, 4)
    for i in range(1, 5):
        a.SetValue(i, i / 2)
    v = a.ValuesArray()
    assert v.shape == (4,) and v.dtype == np.float64
    assert not v.flags["OWNDATA"]
    assert v.tolist() == [a.Value(i) for i in range(a.Lower(), a.Upper() + 1)]


def test_a_multi_component_element_gets_a_trailing_dimension():
    """gp_Pnt is three packed doubles, so an array of them is (N, 3) -- not (N,) of anything."""
    a = NCollection.NCollection_Array1__gp_Pnt(1, 3)
    for i in range(1, 4):
        a.SetValue(i, gp.gp_Pnt(i, i * 2, i * 3))
    v = a.ValuesArray()
    assert v.shape == (3, 3) and v.dtype == np.float64
    assert v[1].tolist() == [2.0, 4.0, 6.0]
    v[0, 0] = 99.0
    assert a.Value(1).X() == 99.0                       # a view, not a copy


def test_index_zero_of_the_view_is_Lower_whatever_Lower_is():
    """The view has no notion of OCCT's index base; that is the one thing a reader has to know."""
    a = NCollection.NCollection_Array1__int(5, 7)
    for i in range(5, 8):
        a.SetValue(i, i * 10)
    assert a.ValuesArray().tolist() == [50, 60, 70]


def test_a_direction_array_is_read_only():
    """A gp_Dir is normalised by construction and every OCCT setter keeps it so. A raw write could leave a
    direction of length 0.3 in the array, which is not a gp_Dir -- so that one view is read-only."""
    a = NCollection.NCollection_Array1__gp_Dir(1, 2)
    a.SetValue(1, gp.gp_Dir(1, 0, 0))
    a.SetValue(2, gp.gp_Dir(0, 1, 0))
    v = a.ValuesArray()
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
    v = a.ValuesArray()
    assert v.shape == (2, 3)
    assert v.tolist() == [[11.0, 12.0, 13.0], [21.0, 22.0, 23.0]]
    a2 = NCollection.NCollection_Array2__gp_Pnt(1, 2, 1, 3)
    assert a2.ValuesArray().shape == (2, 3, 3)          # the element's components come last


def test_the_handle_variants_inherit_the_accessor():
    """HArray1 derives from Array1 and HArray2 from Array2, so neither needs its own accessor."""
    h = NCollection.NCollection_HArray1__double(1, 3, 2.5)
    assert h.ValuesArray().tolist() == [2.5, 2.5, 2.5]
    h2 = NCollection.NCollection_HArray2__int(1, 2, 1, 2, 7)
    assert h2.ValuesArray().shape == (2, 2) and h2.ValuesArray().dtype == np.int32


def test_an_element_that_cannot_be_viewed_has_no_accessor():
    """A handle, a string or a TopoDS_Shape has nothing packed to view, and the binder must not pretend."""
    assert not hasattr(NCollection.NCollection_Array1__TopoDS_Shape, "ValuesArray")
    assert hasattr(NCollection.NCollection_Array1__double, "ValuesArray")


def test_an_empty_array_views_as_an_empty_array_not_None():
    a = NCollection.NCollection_Array1__double()
    assert a.Size() == 0 and a.ValuesArray().shape == (0,)


# ---------------------------------------------------------------------------------------------------------
# Image_PixMap (8.10a): the case that justifies the "how" being C++ -- padded rows and a row order that may
# run either way in memory.

def _pixmap(fmt, w, h, row_bytes=0):
    p = Image.Image_PixMap()
    assert p.InitZero(fmt, w, h, row_bytes)
    return p


def test_a_pixmap_views_as_height_width_channels():
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 5, 3)
    v = p.DataArray()
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
    v = p.DataArray()
    assert v.shape == (2, 4, channels) and v.dtype == dtype


def test_padded_rows_are_a_stride_not_a_shear():
    """SizeRowBytes() is not always SizeX * SizePixelBytes -- a FreeImage-loaded 5-pixel-wide RGB image has
    16, not 15. A shape-only view would silently shear the image, so the row stride comes from
    SizeRowBytes()."""
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 5, 3, 16)
    assert p.SizeRowBytes() == 16 > 5 * p.SizePixelBytes()
    v = p.DataArray()
    assert v.shape == (3, 5, 3)
    assert abs(v.strides[0]) == 16                      # the pad is skipped, not folded into the pixels
    v[1, 0] = [7, 8, 9]
    assert v[0, 0].tolist() == [0, 0, 0] and v[2, 0].tolist() == [0, 0, 0]   # neighbours untouched


def test_row_order_is_top_down_even_when_the_storage_is_bottom_up():
    """OCCT hides the storage direction behind Row(i): myTopRowPtr is the *top* row and TopToDown is +1 or
    (size_t)-1. The view does the same, with a negative row stride, so view[y, x] is PixelColor(x, y)
    whatever IsTopDown() says -- a view that disagreed with the class's own accessors would be a trap."""
    p = _pixmap(Image.Image_Format.Image_Format_RGB, 4, 3)
    assert p.IsTopDown() is False                       # OCCT's default for InitZero
    assert p.DataArray().strides[0] < 0

    p.DataArray()[0, 1] = [10, 20, 30]                  # top row, second pixel
    # Quantity_TOC_RGB, not sRGB: PixelColor stores the byte as-is unless asked to linearise, so reading it
    # back as sRGB re-encodes it and 10 comes out as 56.
    rgb = p.PixelColor(1, 0).GetRGB().Values(Quantity.Quantity_TypeOfColor.Quantity_TOC_RGB)
    assert [round(c * 255) for c in rgb] == [10, 20, 30]

    p.SetTopDown(True)                                  # same buffer, the other direction
    assert p.IsTopDown() is True and p.DataArray().strides[0] > 0


def test_an_empty_pixmap_has_no_view():
    assert Image.Image_PixMap().DataArray() is None


# ---------------------------------------------------------------------------------------------------------
# NCollection_Buffer, and the classes the container views reach without a specialisation of their own.

def test_a_buffer_views_as_bytes_and_None_only_when_unallocated():
    """Before this the class was unusable: Data()/ChangeData() are raw pointers, so nothing was bound but
    Size() and IsEmpty() -- which also made FSD_Base64.Decode_s, whose result *is* one of these, unusable."""
    b = NCollection.NCollection_Buffer(NCollection.NCollection_BaseAllocator.CommonBaseAllocator_s())
    assert b.Allocate(8) is True
    v = b.DataArray()
    assert v.shape == (8,) and v.dtype == np.uint8 and not v.flags["OWNDATA"]
    v[:] = range(8)
    assert b.DataArray().tolist() == list(range(8))

    # A buffer of size 0 is still *allocated* -- the allocator hands back a non-null pointer for 0 bytes --
    # so it is a zero-length array. Only Free() makes it None.
    assert NCollection.NCollection_Buffer(
        NCollection.NCollection_BaseAllocator.CommonBaseAllocator_s()).DataArray().shape == (0,)
    b.Free()
    assert b.IsEmpty() is True and b.DataArray() is None


def test_base64_goes_both_ways_now():
    """R-VIEW made Decode's result readable; R-BYTES made Encode callable. Before the two, base64 went
    nowhere: Decode returned an NCollection_Buffer with no data access, and Encode was unbindable.
    """
    import base64

    from OCP3x import FSD

    encoded = FSD.FSD_Base64.Encode_s(b"Hello, OCP3x!").ToCString()
    assert encoded == base64.b64encode(b"Hello, OCP3x!").decode()
    assert bytes(FSD.FSD_Base64.Decode_s(encoded, len(encoded)).DataArray()) == b"Hello, OCP3x!"
    assert FSD.FSD_Base64.Encode_s(b"").ToCString() == ""

    payload = bytes(range(256)) * 100                    # 25 600 bytes, well past one base64 block
    enc = FSD.FSD_Base64.Encode_s(payload).ToCString()
    assert bytes(FSD.FSD_Base64.Decode_s(enc, len(enc)).DataArray()) == payload


def test_Graphic3d_Buffer_inherits_the_accessor():
    """Its elements are interleaved vertex attributes, so the buffer itself has no single element type:
    reshaping to (NbElements, Stride) and slicing by AttributeOffset() is the caller's business."""
    from OCP3x import Graphic3d

    assert hasattr(Graphic3d.Graphic3d_Buffer, "DataArray")


def test_a_polygon_is_reached_through_its_array_with_no_specialisation_of_its_own():
    """Poly_Polygon3D needs no entry in [views]: ChangeNodes() is bound reference_internal and returns a
    bound NCollection_Array1<gp_Pnt>, so the container accessor composes into a real zero-copy path and the
    chain of owners keeps the polygon alive."""
    a = NCollection.NCollection_Array1__gp_Pnt(1, 3)
    for i in range(1, 4):
        a.SetValue(i, gp.gp_Pnt(i, 0, 0))
    poly = Poly.Poly_Polygon3D(a)
    v = poly.ChangeNodes().ValuesArray()
    assert v.shape == (3, 3) and not v.flags["OWNDATA"]
    v[0, 1] = 5.0
    assert poly.Nodes().Value(1).Y() == 5.0
