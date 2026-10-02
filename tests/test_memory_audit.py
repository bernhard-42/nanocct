"""The targeted scenarios of the 2026-10-01 memory audit (Design.md 6: R-CTOR-KEEP, R-METHOD-KEEP, R-KEPT, R-RESULT,
R-RESULT-KEEP, R-OWNER, R-COPY, R-FIELD, R-VIEW-GUARD), each asserting the safe outcome.

Every scenario drops one side of a relation a static scan of the headers found -- an argument an object keeps the address
of, a copy sharing what a destructor frees, a view into a container, a pointer field -- and then uses the other side, in a
fresh interpreter with the allocator scribbling freed memory (tests/test_lifetime.py's runner). On the release build most
of them crashed or printed garbage before the rules; on the AddressSanitizer build (`make asan`) each one is checked for
the access itself. The d_* scenarios check the other direction: what is kept is released with its owner, and repeated
calls do not accumulate keep-alives. Categories: 1 a method stores its argument's address, 2 a base class's member does,
4 a copy of a class whose destructor frees what the copy shares, 5 a value holding a pointer into what produced it,
6 a view into a container that reallocates or frees, 7 a pointer data member, d destruction and retention.
"""
from __future__ import annotations

import pytest

from test_lifetime import _ok, _run


def run(body: str):
    return _run(body, "import sys\n")


def ok(r) -> list[str]:
    """The scenario's printed words (tests/test_lifetime.py's checks: no crash, no leak report, no ASan report)."""
    return " ".join(_ok(r)).split()


# ---- category 1: a method stores the argument's address -------------------------------------------------------------

def test_c1_extrema_extps_initialize_keeps_the_surface():
    """Extrema_ExtPS::Initialize stores myS = &theS (Extrema_ExtPS.cxx:210): R-METHOD-KEEP."""
    out = ok(run("""
        from nanocct import Extrema, Geom, GeomAdaptor, gp
        ext = Extrema.Extrema_ExtPS()
        s = GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln()))
        ext.Initialize(s, -10.0, 10.0, -10.0, 10.0, 1e-7, 1e-7)
        del s
        collect()
        ext.Perform(gp.gp_Pnt(1, 2, 3))
        print(ext.IsDone(), ext.NbExt())
    """))
    assert out == ["True", "1"]


def test_c1_bopds_subiterator_keeps_the_list():
    """BOPDS_SubIterator::SetSubSet1 stores mySubSet1 = &theLI."""
    out = ok(run("""
        from nanocct.BOPDS import BOPDS_SubIterator
        from nanocct.NCollection import NCollection_List
        it = BOPDS_SubIterator()
        lst = NCollection_List[int]()
        for i in range(5):
            lst.Append(i)
        it.SetSubSet1(lst)
        del lst
        collect()
        print(it.SubSet1().Size())
    """))
    assert out == ["5"]


def test_c1_vrml_coordinate_reads_one_object_as_an_array():
    """VrmlData_Coordinate(scene, name, nPoints, const gp_XYZ* arrPoints) keeps the pointer (base VrmlData_ArrayVec3d);
    from Python the "array" is one gp_XYZ, here a temporary. One point: more would read past it (the next scenario)."""
    out = ok(run("""
        from nanocct.VrmlData import VrmlData_Scene, VrmlData_Coordinate
        from nanocct.gp import gp_XYZ
        scene = VrmlData_Scene()
        c = VrmlData_Coordinate(scene, "c", 1, gp_XYZ(1, 2, 3))
        collect()
        print(c.Length(), c.Coordinate(0).X(), c.Coordinate(0).Z())
    """))
    assert out == ["1", "1.0", "3.0"]


@pytest.mark.xfail(strict=False, reason="open: a `const gp_XYZ*` array taken by its first element gets one gp_XYZ from "
                                        "Python, and nPoints > 1 reads past it (not a lifetime rule; AddressSanitizer: "
                                        "heap-buffer-overflow)")
def test_vrml_coordinate_array_taken_by_its_first_element():
    out = ok(run("""
        from nanocct.VrmlData import VrmlData_Scene, VrmlData_Coordinate
        from nanocct.gp import gp_XYZ
        scene = VrmlData_Scene()
        c = VrmlData_Coordinate(scene, "c", 3, gp_XYZ(1, 2, 3))
        print(c.Length(), c.Coordinate(0).X(), c.Coordinate(2).X())
    """))
    assert out[0] == "3"


# ---- category 2: kept by a base class's member -----------------------------------------------------------------------

def test_c2_vrml_node_keeps_the_scene():
    """VrmlData_Box(scene, ...) -> VrmlData_Geometry(theScene) -> VrmlData_Node::myScene = &theScene."""
    out = ok(run("""
        from nanocct.VrmlData import VrmlData_Scene, VrmlData_Box
        scene = VrmlData_Scene()
        box = VrmlData_Box(scene, "b", 1.0, 2.0, 3.0)
        del scene
        collect()
        print(box.Scene().Status())
    """))
    assert len(out) == 1


def test_c2_boolean_keeps_the_pave_filler():
    """BRepAlgoAPI_Cut(S1, S2, PF) -> BRepAlgoAPI_BuilderAlgo(thePF): myDSFiller = &thePF, held in a typedef'd pointer
    (BOPAlgo_PPaveFiller) of a base class; the history reads the filler's data structure."""
    out = ok(run("""
        from nanocct import BOPAlgo, BRepAlgoAPI, BRepPrimAPI, TopAbs, TopExp, TopoDS, gp
        from nanocct.NCollection import NCollection_List
        box = BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape()
        cyl = BRepPrimAPI.BRepPrimAPI_MakeCylinder(gp.gp_Ax2(gp.gp_Pnt(1, 1, -1), gp.gp_Dir(0, 0, 1)), 0.5, 4).Shape()
        args = NCollection_List[TopoDS.TopoDS_Shape]()
        args.Append(box)
        args.Append(cyl)
        pf = BOPAlgo.BOPAlgo_PaveFiller()
        pf.SetArguments(args)
        pf.Perform()
        cut = BRepAlgoAPI.BRepAlgoAPI_Cut(box, cyl, pf)
        del pf, args
        collect()
        top = None
        ex = TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE)
        n = 0
        while ex.More():
            n += cut.Modified(ex.Current()).Size()
            ex.Next()
        print(cut.IsDone(), n > 0, cut.HasModified(), cut.SectionEdges().Size() > 0)
    """))
    assert out == ["True", "True", "True", "True"]


def test_c2_section_keeps_the_pave_filler():
    """BRepAlgoAPI_Section::HasAncestorFaceOn1 reads myDSFiller (BRepAlgoAPI_Section.cxx:228)."""
    out = ok(run("""
        from nanocct import BOPAlgo, BRepAlgoAPI, BRepPrimAPI, TopAbs, TopExp, TopoDS, gp
        from nanocct.NCollection import NCollection_List
        box = BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape()
        cyl = BRepPrimAPI.BRepPrimAPI_MakeCylinder(gp.gp_Ax2(gp.gp_Pnt(1, 1, -1), gp.gp_Dir(0, 0, 1)), 0.5, 4).Shape()
        args = NCollection_List[TopoDS.TopoDS_Shape]()
        args.Append(box)
        args.Append(cyl)
        pf = BOPAlgo.BOPAlgo_PaveFiller()
        pf.SetArguments(args)
        pf.Perform()
        sec = BRepAlgoAPI.BRepAlgoAPI_Section(box, cyl, pf)
        del pf, args
        collect()
        e = TopoDS.Edge(TopExp.TopExp_Explorer(sec.Shape(), TopAbs.TopAbs_EDGE).Current())
        face = TopoDS.TopoDS_Shape()
        found = sec.HasAncestorFaceOn1(e, face)
        print(sec.IsDone(), found)
    """))
    assert out == ["True", "True"]


# ---- category 4: the bindings expose a copy of a class whose destructor frees a raw pointer -------------------------

def test_c4_copy_of_t3bits_frees_twice():
    """IntPatch_PrmPrmIntersection_T3Bits: ~T3Bits deletes p, copy constructor implicit and bound (theOther)."""
    out = ok(run("""
        from nanocct.IntPatch import IntPatch_PrmPrmIntersection_T3Bits as T
        a = T(64)
        a.Add(3)
        try:
            b = T(a)
        except TypeError:
            print("TypeError")             # R-COPY: an owner has no copy constructor
        del a
        collect()
        print("end")
    """))
    assert out == ["TypeError", "end"]


# ---- category 5: a value type holding a raw pointer, returned by value ----------------------------------------------

def test_c5_label_outlives_its_data():
    out = ok(run("""
        from nanocct.TDF import TDF_Data
        label = TDF_Data().Root()
        collect()
        print(label.Tag(), label.Depth())
    """))
    assert out == ["0", "0"]


def test_c5_main_label_outlives_its_document():
    out = ok(run("""
        from nanocct.TDocStd import TDocStd_Document
        from nanocct.TCollection import TCollection_ExtendedString
        doc = TDocStd_Document(TCollection_ExtendedString("XmlOcaf"))
        main = doc.Main()
        del doc
        collect()
        print(main.Tag(), main.Depth())
    """))
    assert out == ["1", "1"]


def test_c5_child_iterator_outlives_its_data():
    out = ok(run("""
        from nanocct.TDF import TDF_Data, TDF_ChildIterator
        data = TDF_Data()
        root = data.Root()
        root.FindChild(1, True)
        root.FindChild(2, True)
        it = TDF_ChildIterator(root, False)
        del data, root
        collect()
        n = 0
        while it.More():
            n += 1
            it.Next()
        print(n)
    """))
    assert out == ["2"]


# ---- category 6: element references (reference_internal) into a container that reallocates or drops the element ------

def test_c6_change_value_after_resize():
    out = ok(run("""
        from nanocct.NCollection import NCollection_Array1
        from nanocct.gp import gp_Pnt
        a = NCollection_Array1[gp_Pnt](1, 2)
        a.SetValue(1, gp_Pnt(7, 8, 9))
        p = a.ChangeValue(1)
        try:
            a.Resize(1, 100000, True)
        except BufferError:
            print("BufferError")
        collect()
        print(p.X())
    """))
    assert out == ["BufferError", "7.0"]          # R-VIEW-GUARD: the array refuses while the view lives


def test_c6_numpy_view_after_resize():
    out = ok(run("""
        import numpy as np
        from nanocct.NCollection import NCollection_Array1
        a = NCollection_Array1[float](1, 4)
        for i in range(1, 5):
            a.SetValue(i, float(i))
        v = np.asarray(a)
        try:
            a.Resize(1, 100000, True)
        except BufferError:
            print("BufferError")
        collect()
        print(np.array(v)[0])
    """))
    assert out == ["BufferError", "1.0"]


def test_c6_sequence_change_value_after_remove():
    out = ok(run("""
        from nanocct.NCollection import NCollection_Sequence
        from nanocct.gp import gp_Pnt
        s = NCollection_Sequence[gp_Pnt]()
        s.Append(gp_Pnt(1, 2, 3))
        s.Append(gp_Pnt(4, 5, 6))
        p = s.ChangeValue(1)
        try:
            s.Remove(1)
        except BufferError:
            print("BufferError")
        collect()
        print(p.X())
    """))
    assert out == ["BufferError", "1.0"]


def test_c6_list_append_result_after_clear():
    """NCollection_List.Append returns T& (reference_internal) into the new node."""
    out = ok(run("""
        from nanocct.NCollection import NCollection_List
        from nanocct.gp import gp_Pnt
        l = NCollection_List[gp_Pnt]()
        p = l.Append(gp_Pnt(1, 2, 3))
        try:
            l.Clear()
        except BufferError:
            print("BufferError")
        collect()
        print(p.X())
    """))
    assert out == ["BufferError", "1.0"]


# ---- d: explicit destruction / retention, the argument direction -----------------------------------------------------

def test_d_ctor_keep_releases_the_argument_with_its_owner():
    """R-CTOR-KEEP: GeomBndLib_Surface(const Adaptor3d_Surface&) keeps the argument (+1) and releases it (0)."""
    out = ok(run("""
        from nanocct import Geom, GeomAdaptor, GeomBndLib, gp
        s = GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln()))
        base = sys.getrefcount(s)
        b = GeomBndLib.GeomBndLib_Surface(s)
        kept = sys.getrefcount(s)
        del b
        collect()
        print(kept - base, sys.getrefcount(s) - base)
    """))
    assert out == ["1", "0"]


def test_d_ctor_keep_on_a_transient_owner_releases_the_argument():
    """R-CTOR-KEEP on a Transient (R-KEPT: in a slot of the C++ object): IntPatch_PolyhedronBVH(const IntPatch_Polyhedron&)."""
    out = ok(run("""
        from nanocct import Geom, GeomAdaptor, IntPatch, gp
        poly = IntPatch.IntPatch_Polyhedron(GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln())), 4, 4)
        base = sys.getrefcount(poly)
        bvh = IntPatch.IntPatch_PolyhedronBVH(poly)
        kept = sys.getrefcount(poly)
        del bvh
        collect()
        print(kept - base, sys.getrefcount(poly) - base)
    """))
    assert out == ["1", "0"]


def test_d_repeated_constructions_do_not_accumulate():
    out = ok(run("""
        from nanocct import Geom, GeomAdaptor, GeomBndLib, gp
        s = GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln()))
        base = sys.getrefcount(s)
        for i in range(5000):
            b = GeomBndLib.GeomBndLib_Surface(s)
        del b
        collect()
        print(sys.getrefcount(s) - base)
    """))
    assert out == ["0"]


def test_d_reference_internal_results_do_not_accumulate():
    out = ok(run("""
        from nanocct.NCollection import NCollection_Array1
        from nanocct.gp import gp_Pnt
        a = NCollection_Array1[gp_Pnt](1, 3)
        base = sys.getrefcount(a)
        for i in range(10000):
            p = a.ChangeValue(1)
        kept = sys.getrefcount(a)
        del p
        collect()
        print(kept - base, sys.getrefcount(a) - base)
    """))
    assert out == ["1", "0"]


def test_d_occt_handle_count_returns_after_use():
    """No C++ reference left behind by the bindings: a curve used by an edge is back to its own count afterwards."""
    out = ok(run("""
        from nanocct import BRepBuilderAPI, Geom, gp
        c = Geom.Geom_Circle(gp.gp_Ax2(), 1.0)
        rc0 = c.GetRefCount()
        e = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(c).Edge()
        rc1 = c.GetRefCount()
        del e
        collect()
        print(rc1 > rc0, c.GetRefCount() - rc0)
    """))
    assert out == ["True", "0"]


# ---- category 4, more: copyable classes whose destructor frees what the copy shares (one call below the destructor) ---

BOX_AND_CYL = """
from nanocct import BOPAlgo, BRepPrimAPI, TopoDS, gp
from nanocct.NCollection import NCollection_List
box = BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape()
cyl = BRepPrimAPI.BRepPrimAPI_MakeCylinder(gp.gp_Ax2(gp.gp_Pnt(1, 1, -1), gp.gp_Dir(0, 0, 1)), 0.5, 4).Shape()
args = NCollection_List[TopoDS.TopoDS_Shape]()
args.Append(box)
args.Append(cyl)
"""


def test_c4_copy_of_a_pave_filler():
    """BOPAlgo_PaveFiller::~ -> Clear() deletes what it owns; the bound implicit copy shares those pointers."""
    out = ok(run(BOX_AND_CYL + """
pf = BOPAlgo.BOPAlgo_PaveFiller()
pf.SetArguments(args)
pf.Perform()
try:
    pf2 = BOPAlgo.BOPAlgo_PaveFiller(pf)
except TypeError:
    print("TypeError")
del pf
collect()
print("end")
"""))
    assert out == ["TypeError", "end"]


def test_c4_copy_of_a_builder():
    """BOPAlgo_Builder::~ deletes myPaveFiller when it created it (Perform without a filler)."""
    out = ok(run(BOX_AND_CYL + """
b = BOPAlgo.BOPAlgo_Builder()
b.SetArguments(args)
b.Perform()
try:
    b2 = BOPAlgo.BOPAlgo_Builder(b)
except TypeError:
    print("TypeError")
print(b.Shape().IsNull())
del b
collect()
print("end")
"""))
    assert out == ["TypeError", "False", "end"]


def test_c4_copy_of_a_polyhedron():
    """IntPatch_Polyhedron::~ -> Destroy() deletes its arrays (C_MyPnts, C_MyU, C_MyV)."""
    out = ok(run("""
        from nanocct import Geom, GeomAdaptor, IntPatch, gp
        p = IntPatch.IntPatch_Polyhedron(GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln())), 4, 4)
        try:
            q = IntPatch.IntPatch_Polyhedron(p)
        except TypeError:
            print("TypeError")
        del p
        collect()
        print("end")
    """))
    assert out == ["TypeError", "end"]


def test_c4_copy_of_a_cs_intersector():
    """LocOpe_CSIntersector::~ -> Destroy() deletes myPoints."""
    out = ok(run("""
        from nanocct import BRepPrimAPI, LocOpe, gp
        from nanocct.NCollection import NCollection_Sequence
        box = BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape()
        a = LocOpe.LocOpe_CSIntersector(box)
        lines = NCollection_Sequence[gp.gp_Lin]()
        lines.Append(gp.gp_Lin(gp.gp_Pnt(1, 1, -1), gp.gp_Dir(0, 0, 1)))
        a.Perform(lines)
        try:
            b = LocOpe.LocOpe_CSIntersector(a)
        except TypeError:
            print("TypeError")
        print(a.NbPoints(1))
        del a
        collect()
        print("end")
    """))
    assert out == ["TypeError", "2", "end"]


def test_d_ctor_keep_follows_the_cpp_object_of_a_transient():
    """R-KEPT: an OCCT sequence keeps the BVH after Python dropped it; the polyhedron it points to lives as long as the
    C++ object, not as long as its Python object."""
    out = ok(run("""
        from nanocct import Geom, GeomAdaptor, IntPatch, NCollection, Standard, gp
        seq = NCollection.NCollection_HSequence[Standard.Standard_Transient]()
        poly = IntPatch.IntPatch_Polyhedron(GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln())), 4, 4)
        bvh = IntPatch.IntPatch_PolyhedronBVH(poly)
        n0 = bvh.Center(0, 0)
        seq.Append(bvh)
        del bvh, poly
        collect()
        again = seq.Value(1)
        print(n0, again.Center(0, 0))
    """))
    assert out[0] == out[1]


def test_d_copy_of_a_kept_owner_keeps_the_arguments():
    """R-COPY: the copy (`Extrema_ExtCC2d(other)`) points at the original's arguments; it keeps the original and what its
    slots hold."""
    out = ok(run("""
        from nanocct import Extrema, Geom2d, Geom2dAdaptor, gp
        def line(y):
            return Geom2dAdaptor.Geom2dAdaptor_Curve(Geom2d.Geom2d_Line(gp.gp_Pnt2d(0, y), gp.gp_Dir2d(1, 0)), -10.0, 10.0)
        c1 = line(0.0)
        ext = Extrema.Extrema_ExtCC2d(c1, line(1.0))      # keeps both arguments (R-CTOR-KEEP)
        cp = Extrema.Extrema_ExtCC2d(ext)                  # shares the stored C2, not the keep-alive
        del ext
        collect()
        cp.Perform(c1, -10.0, 10.0)                        # reads the stored C2
        print(cp.IsDone(), cp.IsParallel())
    """))
    assert out == ["True", "True"]


# ---- category 7: a public pointer data member (R-FIELD: read-only, the getter copies) ----------------------------------

def test_c7_pointer_field_keeps_the_address_of_a_temporary():
    """BRepMesh_FaceChecker::Segment::Point1 is `gp_Pnt2d*`: a setter would store the address of the Python object
    assigned."""
    out = ok(run("""
        from nanocct.BRepMesh import BRepMesh_FaceChecker
        from nanocct.gp import gp_Pnt2d
        seg = BRepMesh_FaceChecker.Segment()
        try:
            seg.Point1 = gp_Pnt2d(3.0, 4.0)
        except AttributeError:
            print("AttributeError")         # R-FIELD: a pointer member is read-only
        collect()
        print(seg.Point1)
    """))
    assert out == ["AttributeError", "None"]


def test_c7_char_pointer_field_points_into_a_python_string():
    """V3d_ImageDumpOptions::LightName is `const char*`: a setter would store a pointer into the str's own buffer."""
    out = ok(run("""
        from nanocct.V3d import V3d_ImageDumpOptions
        o = V3d_ImageDumpOptions()
        try:
            o.LightName = "light-" + str(12345) * 50      # a fresh string, not interned
        except AttributeError:
            print("AttributeError")
        collect()
        print(repr(o.LightName))
    """))
    assert out == ["AttributeError", "''"]


def test_c1_extrema_extpc_initialize_with_a_temporary_adaptor():
    """The natural Python form: `ext.Initialize(BRepAdaptor_Curve(edge), u0, u1)` -- the adaptor is a temporary.
    Extrema_ExtPC's Initialize is generic code (Extrema_GExtPC): the rule sees it after template substitution."""
    out = ok(run("""
        from nanocct import BRepAdaptor, BRepBuilderAPI, Extrema, gp
        edge = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(10, 0, 0)).Edge()
        ext = Extrema.Extrema_ExtPC()
        ext.Initialize(BRepAdaptor.BRepAdaptor_Curve(edge), 0.0, 10.0)
        collect()
        ext.Perform(gp.gp_Pnt(3, 1, 0))
        print(ext.IsDone(), ext.NbExt())
    """))
    assert out == ["True", "1"]
