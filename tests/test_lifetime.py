"""Lifetime tests for the ownership rules: what happens when Python lets go (Design.md 6 R-RESULT).

The rest of the suite tests that an API works while its objects are alive. These tests drop one side and use the other,
in both directions, for every row of R-RESULT / R-PTR-REF / R-PTR-INCOMPLETE:

- forward: take the result, drop it, collect, use the owner;
- reverse: drop the owner, collect, use the result.

Each scenario runs in a fresh interpreter, because a lifetime bug does not raise: it frees memory twice or reads memory
that was freed, and the process aborts or segfaults (the R-RESULT bug of 2026-09-25 took the whole pytest process with
it). A crash is a non-zero return code here, not a dead suite. The subprocess also runs with the allocator's scribbling
switched on (`MallocScribble` on macOS, `MALLOC_PERTURB_` on glibc; each ignores the other's), so freed memory is
overwritten and a read after free is far more likely to show; after dropping one side, the prelude's `collect()` also
allocates enough to reuse what was freed. And it fails on nanobind's "leaked instances" report at exit, which is how a
reference cycle through `keep_alive` shows. On an AddressSanitizer audit build an ASan report aborts the
child, so it fails here like any crash -- provided `ASAN_OPTIONS` has `strip_env=0`, without which ASan removes
`DYLD_INSERT_LIBRARIES` from the environment and every child aborts at its first import.

The call sites are real generated ones, one per row, named in each test. Where a reverse direction is unsafe for a
reason the bindings cannot change (an OCCT bug), the test asserts the safe outcome and is marked `xfail(strict=False)`:
the finding stays visible in every run (and an AddressSanitizer build names the use-after-free) without making the suite
depend on what freed memory happens to contain.
Three bugs these tests found (a Transient returned by value, a `*this` result keeping itself alive, a `T*` result that did
not keep its owner -- `rv_policy::reference`, by design until 2026-10-02) are fixed; their tests are ordinary ones now.
"""
from __future__ import annotations

import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
ENV = {**os.environ, "MallocScribble": "1", "MALLOC_PERTURB_": "85"}
if "ASAN_OPTIONS" not in os.environ:
    # the native stack of a crash, in the failure message. Not under AddressSanitizer: faulthandler would catch the
    # signal first and re-raise it, and ASan would then report the re-raise instead of the faulting access.
    ENV["PYTHONFAULTHANDLER"] = "1"

PRELUDE = """
import gc
def collect():
    gc.collect()
    return [bytearray(96) for _ in range(20000)]    # reuse what was just freed, so a dangling read sees other data
"""

BOX = """
from nanocct import BRepPrimAPI, TopAbs, TopExp, TopoDS
box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
face = TopoDS.Face(TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE).Current())
"""


def _run(body: str, setup: str = "") -> subprocess.CompletedProcess:
    """One scenario in a fresh interpreter: `setup` builds the objects, `body` prints what the test checks."""
    return subprocess.run([sys.executable, "-c", PRELUDE + setup + textwrap.dedent(body)], capture_output=True, text=True,
                          cwd=ROOT, env=ENV, timeout=300)


def _ok(r: subprocess.CompletedProcess) -> list[str]:
    """The scenario's printed lines, after checking it neither crashed nor leaked."""
    assert r.returncode == 0, f"rc={r.returncode}\nstdout:\n{r.stdout}\nstderr:\n{r.stderr[-4000:]}"
    assert "nanobind: leaked" not in r.stderr, f"leaked at exit:\n{r.stderr[-4000:]}"
    # on the AddressSanitizer audit build with halt_on_error=0 a report does not end the process: then the report on
    # stderr is the failure (with log_path set it goes to a file instead, and only the log directory tells)
    assert "ERROR: AddressSanitizer" not in r.stderr, r.stderr[-8000:]
    return r.stdout.splitlines()


# ---- R-RESULT: T* to a Transient -> a handle ------------------------------------------------------------------------

def test_transient_pointer_result_forward():
    """PrsMgr_PresentableObject::Parent() returns `PrsMgr_PresentableObject*` (a raw back pointer): the parent's own
    Python object, holding a handle. Dropping it leaves the child and the parent intact."""
    out = _ok(_run("""
        from nanocct import AIS
        parent, child = AIS.AIS_Shape(box), AIS.AIS_Shape(box)
        parent.AddChild(child)
        result = child.Parent()
        print(result is parent)
        del result
        collect()
        print(child.Parent() is parent, parent.Children().Size(), parent.GetRefCount())
    """, BOX))
    assert out == ["True", "True 1 1"]


def test_transient_pointer_result_reverse():
    """The same, dropping the child and the parent's own variable: the result's handle keeps the parent alive, and the
    parent's child list keeps the child."""
    out = _ok(_run("""
        from nanocct import AIS
        parent, child = AIS.AIS_Shape(box), AIS.AIS_Shape(box)
        parent.AddChild(child)
        result = child.Parent()
        del child, parent
        collect()
        print(result.GetRefCount(), result.Children().Size(), result.Children().First().Parent() is result)
    """, BOX))
    assert out == ["1 1 True"]


# ---- R-PTR-REF: T*& to a Transient -> the pointer, as a handle --------------------------------------------------------

MESH_MODEL = BOX + """
from nanocct import BRepMesh, IMeshTools
model = BRepMesh.BRepMesh_ModelBuilder().Perform(box, IMeshTools.IMeshTools_Parameters())
wire = model.GetFace(0).GetWire(0)
"""


def test_transient_pointer_reference_result_forward():
    """IMeshData_Wire::GetEdge(i) returns `const IMeshData::IEdgePtr&` (`IMeshData_Edge* const&`), IMeshData_PCurve::GetFace()
    `const IMeshData::IFacePtr&`: both are handle-owned by the model."""
    out = _ok(_run("""
        edge = wire.GetEdge(0)
        face = edge.GetPCurve(0).GetFace()
        print(edge.GetRefCount(), face.GetRefCount())
        del edge, face
        collect()
        print(wire.EdgesNb(), wire.GetEdge(0).PCurvesNb(), model.GetFace(0).WiresNb())
        del wire
        collect()
    """, MESH_MODEL))
    assert out == ["2 2", "4 2 1"]


def test_transient_pointer_reference_result_reverse():
    """Dropping the wire and the pcurve the results came from (the model stays): the results are handles of their own.
    Everything taken from the model is released before it, at the end (see the next test)."""
    out = _ok(_run("""
        pcurve = wire.GetEdge(0).GetPCurve(0)
        edge, face = wire.GetEdge(0), pcurve.GetFace()
        del wire, pcurve
        collect()
        print(edge.PCurvesNb(), face.WiresNb(), face.GetWire(0).EdgesNb())
        del edge, face
        collect()
    """, MESH_MODEL))


@pytest.mark.xfail(strict=False, reason="OCCT, not a binding rule: a BRepMeshData object is placement-new'd into its model's "
                                        "NCollection_IncAllocator and holds a handle to it; the last one to die frees its own "
                                        "storage in its member destructor, and ~IMeshData_Edge then runs on freed memory "
                                        "(OCCT's own use-after-free)")
def test_imeshdata_objects_outliving_their_model():
    """Any handle into the mesh data model -- `GetFace()`/`GetWire()` (R-HANDLE) as much as `GetEdge()` (R-PTR-REF) --
    must be released before the model: BRepMeshData_Model.cxx:73 creates each edge with `new (myAllocator)`, and
    BRepMeshData_Edge.cxx:27 keeps `myAllocator` as a member, destroyed before the base class IMeshData_Edge. While the
    model lives it holds the allocator and nothing happens; here the model goes first. C++ has the same hazard for a
    handle kept past the model; in Python it is also whatever order the interpreter clears globals in at exit."""
    out = _ok(_run("""
        edge = wire.GetEdge(0)
        del model
        collect()
        print(edge.PCurvesNb())
        del wire
        collect()
        del edge
        collect()
    """, MESH_MODEL))
    assert out == ["2"]
    assert out == ["2 1 4"]


# ---- R-RESULT: T& to a Transient, reference count > 0 (handle-owned) --------------------------------------------------

LDOM_DOC = """
from nanocct import LDOM
doc = LDOM.LDOM_Document.createDocument_s("root")
element = doc.getDocumentElement()
"""


def test_transient_reference_result_handle_owned_forward():
    """LDOM_Node::getOwnerDocument() returns `const LDOM_MemManager&`, held by the node's `handle<LDOM_MemManager>`: the
    count is > 0 at return, so no permanent reference is added -- the count is the same for every fresh wrapper."""
    out = _ok(_run("""
        result = element.getOwnerDocument()
        first = result.GetRefCount()
        del result
        collect()
        again = element.getOwnerDocument()
        print(first == again.GetRefCount(), again.RootElement() is not None, element.getTagName().GetString())
    """, LDOM_DOC))
    assert out == ["True True root"]


def test_transient_reference_result_handle_owned_reverse():
    out = _ok(_run("""
        result = element.getOwnerDocument()
        del element, doc
        collect()
        print(result.GetRefCount() > 0, result.RootElement() is not None)
    """, LDOM_DOC))
    assert out == ["True True"]


# ---- R-RESULT: T& to a Transient, reference count 0 (not handle-owned: one permanent reference + keep_alive<0, 1>) -----

def test_transient_reference_result_member_forward():
    """BRepAdaptor_Curve::Curve() (GeomAdaptor_TransformedCurve::Curve) returns `const GeomAdaptor_Curve&`, a member held by
    value -- the shape of the 2026-09-25 crash. It gets exactly one permanent reference, however often it is returned."""
    out = _ok(_run("""
        import math
        from nanocct import BRepAdaptor, BRepBuilderAPI, GC, gp
        edge = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(GC.GC_MakeCircle(gp.gp_Ax2(), 1.0).Value()).Edge()
        owner = BRepAdaptor.BRepAdaptor_Curve(edge)
        for _ in range(100):
            owner.Curve().Curve().Copy()
        collect()
        result = owner.Curve()
        print(result.GetRefCount())                  # the permanent reference + this wrapper's handle
        del result
        collect()
        print(math.isclose(owner.LastParameter(), 2 * math.pi), math.isclose(owner.Curve().LastParameter(), 2 * math.pi))
    """, BOX))
    assert out == ["2", "True True"]


def test_transient_reference_result_member_reverse():
    """keep_alive<0, 1>: the member's wrapper keeps its owner alive, so the member outlives the owner's variable."""
    out = _ok(_run("""
        import math
        from nanocct import BRepAdaptor, BRepBuilderAPI, GC, gp
        edge = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(GC.GC_MakeCircle(gp.gp_Ax2(), 1.0).Value()).Edge()
        owner = BRepAdaptor.BRepAdaptor_Curve(edge)
        result = owner.Curve()
        del owner, edge
        collect()
        print(result.FirstParameter(), math.isclose(result.LastParameter(), 2 * math.pi), result.Curve().IsClosed())
    """, BOX))
    assert out == ["0.0 True True"]


def test_transient_reference_result_allocator_storage_forward():
    """IntTools_Context::SurfaceAdaptor(face) returns a `BRepAdaptor_Surface&` placement-new'd into the context's own
    allocator (IntTools_Context.cxx:333-334): count 0, and never allocated on its own, like a member."""
    out = _ok(_run("""
        from nanocct import IntTools
        owner = IntTools.IntTools_Context()
        result = owner.SurfaceAdaptor(face)
        print(result.GetRefCount())
        del result
        collect()
        again = owner.SurfaceAdaptor(face)
        print(again.GetRefCount(), again.LastUParameter(), again.LastVParameter())
    """, BOX))
    assert out == ["2", "2 3.0 0.0"]


def test_transient_reference_result_allocator_storage_reverse():
    out = _ok(_run("""
        from nanocct import IntTools
        owner = IntTools.IntTools_Context()
        result = owner.SurfaceAdaptor(face)
        del owner
        collect()
        print(result.FirstUParameter(), result.LastUParameter(), result.LastVParameter())
    """, BOX))
    assert out == ["0.0 3.0 0.0"]


def test_transient_reference_result_raw_heap_object_forward():
    """BRepClass3d_SolidExplorer::Intersector(face) returns `IntCurvesFace_Intersector&` to an object the explorer
    allocated with `new` and `delete`s itself in Destroy() (BRepClass3d_SolidExplorer.cxx:884-893): count 0."""
    out = _ok(_run("""
        from nanocct import BRepClass3d, gp
        owner = BRepClass3d.BRepClass3d_SolidExplorer(box)
        result = owner.Intersector(face)
        print(result.GetRefCount())
        del result
        collect()
        again = owner.Intersector(face)
        again.Perform(gp.gp_Lin(gp.gp_Pnt(-1.0, 1.0, 1.5), gp.gp_Dir(1, 0, 0)), -10.0, 10.0)
        print(again.IsDone(), again.NbPnt())
    """, BOX))
    assert out == ["2", "True 1"]


def test_transient_reference_result_raw_heap_object_reverse():
    out = _ok(_run("""
        from nanocct import BRepClass3d, gp
        owner = BRepClass3d.BRepClass3d_SolidExplorer(box)
        result = owner.Intersector(face)
        del owner
        collect()
        result.Perform(gp.gp_Lin(gp.gp_Pnt(-1.0, 1.0, 1.5), gp.gp_Dir(1, 0, 0)), -10.0, 10.0)
        print(result.IsDone(), result.NbPnt())
    """, BOX))
    assert out == ["True 1"]


# ---- R-RESULT: T* to another class -> rv_policy::reference (no keep_alive) --------------------------------------------

BSPLINE = """
from nanocct import Geom, NCollection, gp
poles = NCollection.NCollection_Array1[gp.gp_Pnt](1, 3)
for i, p in enumerate([gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(1, 1, 0), gp.gp_Pnt(2, 0, 0)], 1):
    poles.SetValue(i, p)
weights = NCollection.NCollection_Array1[float](1, 3)
for i, w in enumerate([1.0, 2.0, 1.0], 1):
    weights.SetValue(i, w)
knots = NCollection.NCollection_Array1[float](1, 2)
knots.SetValue(1, 0.0); knots.SetValue(2, 1.0)
mults = NCollection.NCollection_Array1[int](1, 2)
mults.SetValue(1, 3); mults.SetValue(2, 3)
owner = Geom.Geom_BSplineCurve(poles, weights, knots, mults, 2)
"""


def test_class_pointer_result_forward():
    """Geom_BSplineCurve::Weights() returns `const NCollection_Array1<double>*` into the curve (rv_policy::reference)."""
    out = _ok(_run("""
        result = owner.Weights()
        print(list(result))
        del result
        collect()
        print(owner.IsRational(), list(owner.Weights()))
    """, BSPLINE))
    assert out == ["[1.0, 2.0, 1.0]", "True [1.0, 2.0, 1.0]"]


def test_class_pointer_result_reverse():
    out = _ok(_run("""
        result = owner.Weights()
        del owner
        collect()
        print(list(result))
    """, BSPLINE))
    assert out == ["[1.0, 2.0, 1.0]"]


# ---- R-PTR-REF: T*& to another class; R-PTR-INCOMPLETE: T* to a forward-declared class --------------------------------

FUSE = BOX + """
from nanocct import BRepAlgoAPI, gp
owner = BRepAlgoAPI.BRepAlgoAPI_Fuse(box, BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(0.5, 0.5, 0.5), 1, 1, 1).Shape())
"""


def test_class_pointer_reference_result_forward():
    """BRepAlgoAPI_BuilderAlgo::Builder() returns `const BOPAlgo_PBuilder&` (`BOPAlgo_Builder* const&`), which the fuse owns
    and deletes."""
    out = _ok(_run("""
        result = owner.Builder()
        print(type(result).__name__, result.HasErrors(), result.Arguments().Size())
        del result
        collect()
        print(owner.IsDone(), owner.Shape().IsNull(), owner.Builder().Arguments().Size())
    """, FUSE))
    assert out == ["BOPAlgo_BOP False 1", "True False 1"]


def test_class_pointer_reference_result_reverse():
    out = _ok(_run("""
        result = owner.Builder()
        del owner
        collect()
        print(result.HasErrors(), result.Arguments().Size())
    """, FUSE))
    assert out == ["False 1"]


def test_incomplete_class_pointer_result_forward():
    """BOPAlgo_Builder::PDS() returns `BOPDS_PDS`, a `BOPDS_DS*` whose class BOPDS_PDS.hxx only forward-declares
    (R-PTR-INCOMPLETE): the same rv_policy::reference as any class pointer."""
    out = _ok(_run("""
        result = owner.Builder().PDS()
        n = result.NbShapes()
        del result
        collect()
        print(n > 0, owner.Builder().PDS().NbShapes() == n, owner.Shape().IsNull())
    """, FUSE))
    assert out == ["True True False"]


def test_incomplete_class_pointer_result_reverse():
    out = _ok(_run("""
        result = owner.Builder().PDS()
        n = result.NbShapes()
        del owner
        collect()
        print(result.NbShapes() == n)
    """, FUSE))
    assert out == ["True"]


# ---- R-RESULT: mutable T& to another class -> rv_policy::reference_internal (methods) ------------------------------------

def test_mutable_reference_method_forward():
    """gp_Pnt::ChangeCoord() returns `gp_XYZ&` into a value class nanobind owns; Poly_Polygon3D::ChangeNodes() returns
    `NCollection_Array1<gp_Pnt>&` into a Transient. Edits through the result reach the owner."""
    out = _ok(_run("""
        from nanocct import NCollection, Poly, gp
        p = gp.gp_Pnt(1, 2, 3)
        xyz = p.ChangeCoord()
        xyz.SetX(10.0)
        del xyz
        collect()
        print(p.X(), p.Y(), p.Z())
        nodes = NCollection.NCollection_Array1[gp.gp_Pnt](1, 2)
        nodes.SetValue(1, gp.gp_Pnt(0, 0, 0)); nodes.SetValue(2, gp.gp_Pnt(1, 0, 0))
        poly = Poly.Poly_Polygon3D(nodes)
        arr = poly.ChangeNodes()
        arr.SetValue(2, gp.gp_Pnt(5, 0, 0))
        del arr
        collect()
        print(poly.NbNodes(), poly.Nodes().Value(2).X())
    """))
    assert out == ["10.0 2.0 3.0", "2 5.0"]


def test_mutable_reference_method_reverse():
    """reference_internal is keep_alive<0, 1>: the reference keeps its owner alive."""
    out = _ok(_run("""
        from nanocct import NCollection, Poly, gp
        p = gp.gp_Pnt(1, 2, 3)
        xyz = p.ChangeCoord()
        del p
        collect()
        xyz.SetZ(7.0)
        print(xyz.X(), xyz.Y(), xyz.Z())
        nodes = NCollection.NCollection_Array1[gp.gp_Pnt](1, 2)
        nodes.SetValue(1, gp.gp_Pnt(0, 0, 0)); nodes.SetValue(2, gp.gp_Pnt(1, 0, 0))
        poly = Poly.Poly_Polygon3D(nodes)
        arr = poly.ChangeNodes()
        del poly, nodes
        collect()
        print(arr.Length(), arr.Value(2).X())
    """))
    assert out == ["1.0 2.0 7.0", "2 1.0"]


# ---- R-RESULT: mutable T& from a free function -> copied ------------------------------------------------------------

def test_mutable_reference_free_function_is_a_copy():
    """TopOpeBRepTool's FSC_GetPSC() returns `TopOpeBRepTool_ShapeClassifier&` to a process-wide static
    (TopOpeBRepTool_SC.cxx:28-35); TopoDS::Vertex(TopoDS_Shape&) a reference into its argument. With no `self` to tie a
    reference to, both are copied: every call is a new object, and a result outlives its source."""
    out = _ok(_run("""
        from nanocct import TopOpeBRepTool
        first, second = TopOpeBRepTool.FSC_GetPSC(), TopOpeBRepTool.FSC_GetPSC(box)
        print(first is second)
        del first, second
        collect()
        print(type(TopOpeBRepTool.FSC_GetPSC()).__name__)
        source = TopExp.TopExp_Explorer(box, TopAbs.TopAbs_VERTEX).Current()
        vertex = TopoDS.Vertex(source)
        print(vertex is source, vertex.IsSame(source))
        del source
        collect()
        print(vertex.ShapeType() == TopAbs.TopAbs_VERTEX, vertex.IsNull())
    """, BOX))
    assert out == ["False", "TopOpeBRepTool_ShapeClassifier", "False True", "True False"]


# ---- bugs these tests found (xfail strict: remove the marker with the fix) ---------------------------------------------

def test_a_result_that_is_self_does_not_leak():
    """LDOM_MemManager::Self() and FSD_File::PutInteger() return `*this` (chaining); the result is the same Python object.
    A plain keep_alive<0, 1> made it keep itself alive for ever -- nanobind's keep_alive_py has no nurse == patient
    check -- so R-RESULT uses nanocct::KeepOwnerUnlessSelf (found by this test, 8.18)."""
    out = _ok(_run("""
        from nanocct import LDOM
        doc = LDOM.LDOM_Document.createDocument_s("root")
        manager = doc.getDocumentElement().getOwnerDocument()
        print(manager.Self() is manager)
    """))
    assert out == ["True"]


def test_a_transient_returned_by_value_survives_a_handle():
    """Geom2dGcc_QualifiedCurve::Qualified() returns `Geom2dAdaptor_Curve` by value; Adaptor2d_OffsetCurve takes
    `const handle<Adaptor2d_Curve2d>&` and keeps it. Dropping the offset curve drops the last handle. A nanobind-owned
    copy (count 0) was deleted by that handle, so R-RESULT moves the value into a handle (found by this test, 8.18)."""
    out = _ok(_run("""
        from nanocct import Adaptor2d, GccEnt, Geom2d, Geom2dAdaptor, Geom2dGcc, gp
        line = Geom2d.Geom2d_Line(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(1, 0))
        qualified = Geom2dGcc.Geom2dGcc_QualifiedCurve(Geom2dAdaptor.Geom2dAdaptor_Curve(line), GccEnt.GccEnt_unqualified)
        curve = qualified.Qualified()
        offset = Adaptor2d.Adaptor2d_OffsetCurve(curve)
        del offset
        collect()
        print(curve.FirstParameter() < 0)
    """))
    assert out == ["True"]


# ---- R-CTOR-KEEP: a constructor argument the object keeps a pointer or reference to -----------------------------------

def test_a_kept_constructor_argument_outlives_its_variable():
    """GeomBndLib_Surface(const Adaptor3d_Surface&) keeps `myAdaptorRef = &theSurf` (GeomBndLib_Surface.cxx). A temporary
    adaptor was collected before Add() read it, and Add() crashed; the argument now lives as long as the object."""
    out = _ok(_run("""
        from nanocct import Bnd, Geom, GeomAdaptor, GeomBndLib, gp
        sphere = Geom.Geom_SphericalSurface(gp.gp_Ax3(), 2.0)
        bounds = GeomBndLib.GeomBndLib_Surface(GeomAdaptor.GeomAdaptor_Surface(sphere))
        collect()
        box = Bnd.Bnd_Box()
        bounds.Add(1e-7, box)
        print(round(box.Get().Xmax, 3) >= 2.0, round(box.Get().Xmax, 3) < 2.5)
    """))
    assert out == ["True True"]


def test_a_kept_container_and_graph_outlive_their_variables():
    """BRepGraph's reverse iterators keep `const ContainerType* myRefs` and `const BRepGraph* myGraph` (a template, bound
    through an __init__ lambda). Topo().Vertices().Edges() is a copy, a temporary in this call: the iterator read freed
    memory (a size of 53778742144, or a crash in Next()). Both arguments now live as long as the iterator."""
    out = _ok(_run("""
        from nanocct import BRepGraph, BRepPrimAPI
        g = BRepGraph.BRepGraph()
        g.Clear()
        g.Shapes().Add(BRepPrimAPI.BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape())
        it = BRepGraph.BRepGraph_EdgesOfVertex(g, g.Topo().Vertices().Edges(BRepGraph.BRepGraph_VertexId(0)))
        del g
        collect()
        n = 0
        while it.More():
            n += 1
            it.Next()
        print(n)
    """))
    assert out == ["3"]


def test_a_transient_keeps_its_constructor_argument_while_it_lives():
    """A Transient is built by nb::new_, whose extras reach __new__(cls, args...) and a no-op __init__(self, args...):
    keep_alive<0, k> ties the argument to the returned object (in __init__ the nurse is None and ignored). The argument
    gains one reference while the object lives and loses it with the object -- with the type as nurse it never would.
    CDF_FWOSDriver(NCollection_DataMap<...>& theLookUpTable) keeps a reference to the table."""
    out = _ok(_run("""
        import sys
        from nanocct import CDF, CDM, NCollection, TCollection
        table = NCollection.NCollection_DataMap[TCollection.TCollection_ExtendedString, CDM.CDM_MetaData]()
        before = sys.getrefcount(table)
        driver = CDF.CDF_FWOSDriver(table)
        during = sys.getrefcount(table)
        del driver
        collect()
        print(during - before, sys.getrefcount(table) - before)
    """))
    assert out == ["1 0"]


# ---- R-CTOR-KEEP from the whole layout: a base's member, a typedef'd pointer, a member held by value, a void* member ---

def test_a_base_class_member_keeps_the_constructor_argument():
    """BRepAlgoAPI_Cut(S1, S2, PF) hands the filler to BRepAlgoAPI_BuilderAlgo, whose `BOPAlgo_PPaveFiller myDSFiller` (a
    typedef'd pointer, in a base) keeps its address; SectionEdges() and Modified() read the filler's data structure. The
    filler was collected under the operation (segfault): R-CTOR-KEEP looked at the class's own members only, spelled as
    written. It also gains exactly one reference while the operation lives, and loses it with the operation."""
    out = _ok(_run("""
        import sys
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
        before = sys.getrefcount(pf)
        cut = BRepAlgoAPI.BRepAlgoAPI_Cut(box, cyl, pf)
        during = sys.getrefcount(pf)
        del pf, args
        collect()
        n = 0
        ex = TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE)
        while ex.More():
            n += cut.Modified(ex.Current()).Size()
            ex.Next()
        print(during - before, cut.IsDone(), n > 0, cut.SectionEdges().Size() > 0)
    """))
    assert out == ["1 True True True"]


def test_a_base_class_member_of_a_transient_keeps_the_constructor_argument():
    """Every VRML node keeps its scene in its base's `const VrmlData_Scene* myScene` (VrmlData_Node): VrmlData_Box(scene, ...)
    gains a reference to the scene while the node lives and gives it back with the node (keep_alive<0, k> through nb::new_)."""
    out = _ok(_run("""
        import sys
        from nanocct.VrmlData import VrmlData_Box, VrmlData_Scene
        scene = VrmlData_Scene()
        before = sys.getrefcount(scene)
        box = VrmlData_Box(scene, "b", 1.0, 2.0, 3.0)
        during = sys.getrefcount(scene)
        del box
        collect()
        print(during - before, sys.getrefcount(scene) - before)
    """))
    assert out == ["1 0"]


def test_a_member_held_by_value_keeps_the_constructor_argument():
    """Extrema_GenExtCS keeps the curve inside a member it holds by value (`Extrema_FuncExtCS myF`, whose `myC` points at
    it): the curve gains one reference while the extrema object lives."""
    out = _ok(_run("""
        import sys
        from nanocct import Extrema, Geom, GeomAdaptor, gp
        curve = GeomAdaptor.GeomAdaptor_Curve(Geom.Geom_Line(gp.gp_Pnt(0, 0, 3), gp.gp_Dir(1, 1, 0)), -10.0, 10.0)
        surface = GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_SphericalSurface(gp.gp_Ax3(), 2.0))
        before = sys.getrefcount(curve)
        ext = Extrema.Extrema_GenExtCS(curve, surface, 20, 20, 20, 1e-7, 1e-7)
        during = sys.getrefcount(curve)
        del ext
        collect()
        print(during - before, sys.getrefcount(curve) - before)
    """))
    assert out == ["1 0"]


def test_a_void_pointer_member_keeps_the_constructor_argument():
    """CPnts_UniformDeflection keeps its curve as `void* myCurve`: a `void *` member may hold any object, so every class
    argument by reference is kept. A temporary adaptor was collected before More()/Next() read it (segfault)."""
    out = _ok(_run("""
        from nanocct import CPnts, Geom, GeomAdaptor, gp
        ud = CPnts.CPnts_UniformDeflection(GeomAdaptor.GeomAdaptor_Curve(Geom.Geom_Circle(gp.gp_Ax2(), 5.0)), 0.05, 1e-6, True)
        collect()
        n, radius = 0, 0.0
        while ud.More():
            p = ud.Point()
            radius = max(radius, (p.X() ** 2 + p.Y() ** 2) ** 0.5)
            ud.Next()
            n += 1
        print(n > 10, round(radius, 6))
    """))
    assert out == ["True 5.0"]


# ---- R-METHOD-KEEP: a method argument the object keeps the address of lives in a slot ---------------------------------

def test_a_method_keeps_the_argument_it_stores():
    """Extrema_ExtPS::Initialize(S, ...) stores `myS = &S` (Extrema_ExtPS.cxx); Perform() reads it. With the surface
    dropped, Perform() read freed memory (segfault)."""
    out = _ok(_run("""
        from nanocct import Extrema, Geom, GeomAdaptor, gp
        ext = Extrema.Extrema_ExtPS()
        s = GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln()))
        ext.Initialize(s, -10.0, 10.0, -10.0, 10.0, 1e-7, 1e-7)
        del s
        collect()
        ext.Perform(gp.gp_Pnt(1, 2, 3))
        print(ext.IsDone(), ext.NbExt())
    """))
    assert out == ["True 1"]


def test_a_method_keeps_a_temporary_argument():
    """The natural Python form: a temporary adaptor passed to Initialize(), Perform() later."""
    out = _ok(_run("""
        from nanocct import BRepAdaptor, Extrema, gp
        edge = TopoDS.Edge(TopExp.TopExp_Explorer(box, TopAbs.TopAbs_EDGE).Current())
        ext = Extrema.Extrema_ExtPC()
        curve = BRepAdaptor.BRepAdaptor_Curve(edge)
        ext.Initialize(BRepAdaptor.BRepAdaptor_Curve(edge), curve.FirstParameter(), curve.LastParameter(), 1e-7)
        del curve
        collect()
        ext.Perform(gp.gp_Pnt(0.5, -1.0, 0.0))
        print(ext.IsDone(), ext.NbExt() > 0)
    """, BOX))
    assert out == ["True True"]


def test_each_method_parameter_has_its_own_slot_and_a_call_replaces_it():
    """BOPDS_SubIterator keeps both subsets (`mySubSet1 = &theLI`, `mySubSet2 = &theLI`): one slot each. A second
    SetSubSet1() releases the first list and leaves the second subset's list alone."""
    out = _ok(_run("""
        import sys
        from nanocct.BOPDS import BOPDS_SubIterator
        from nanocct.NCollection import NCollection_List
        def filled(n):
            lst = NCollection_List[int]()
            for i in range(n):
                lst.Append(i)
            return lst
        a, b, c = filled(5), filled(3), filled(2)
        def counts():                      # one form for every measurement: Python 3.14 counts a borrowed load differently
            return [sys.getrefcount(a), sys.getrefcount(b), sys.getrefcount(c)]
        base = counts()
        it = BOPDS_SubIterator()
        it.SetSubSet1(a)
        it.SetSubSet2(b)
        kept = [n - r for n, r in zip(counts(), base)]
        it.SetSubSet1(c)
        replaced = [n - r for n, r in zip(counts(), base)]
        del a, b
        collect()
        print(kept, replaced, it.SubSet1().Size(), it.SubSet2().Size())
    """))
    assert out == ["[1, 1, 0] [0, 1, 1] 2 3"]


def test_a_slot_keeps_one_argument_however_often_it_is_called():
    """nb::keep_alive on a method would keep every argument of a loop of calls (and walk all of them on each call): a slot
    keeps the last one, and the object releases it when it goes."""
    out = _ok(_run("""
        import sys
        from nanocct import Extrema, Geom, GeomAdaptor, gp
        surfaces = [GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln(gp.gp_Pnt(0, 0, i), gp.gp_Dir(0, 0, 1))))
                    for i in range(50)]
        def counts():                      # one form for every measurement: Python 3.14 counts a borrowed load differently
            return [sys.getrefcount(s) for s in surfaces]
        base = counts()
        ext = Extrema.Extrema_ExtPS()
        for surface in surfaces:
            ext.Initialize(surface, -10.0, 10.0, -10.0, 10.0, 1e-7, 1e-7)
        del surface
        during = [n - r for n, r in zip(counts(), base)]
        del ext
        collect()
        after = [n - r for n, r in zip(counts(), base)]
        print(sum(during[:-1]), during[-1], sum(after))
    """))
    assert out == ["0 1 0"]


# ---- R-RESULT-KEEP: a result that can point into what produced it keeps it alive --------------------------------------

def test_a_result_holding_a_pointer_keeps_its_producer():
    """BRepGraph::Topo() returns a view (`BRepGraph::TopoView`, copied out of the `const&`) that holds `BRepGraph*`: with
    the graph's variable gone, every count read the freed graph (segfault)."""
    out = _ok(_run("""
        from nanocct import BRepGraph, BRepPrimAPI
        g = BRepGraph.BRepGraph()
        g.Clear()
        g.Shapes().Add(BRepPrimAPI.BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape())
        topo = g.Topo()
        del g
        collect()
        print(topo.Vertices().Nb(), topo.Edges().Nb(), topo.Faces().Nb())
    """))
    assert out == ["8 12 6"]


def test_a_constructor_keeps_an_argument_it_copies_a_pointer_out_of():
    """TDF_ChildIterator(label) stores the label's `TDF_LabelNode*`, not the label: the iterator's layout and the label's
    share TDF_LabelNode, so the iterator keeps the label -- and the label its TDF_Data (R-OWNER). It walked freed nodes."""
    out = _ok(_run("""
        from nanocct.TDF import TDF_ChildIterator, TDF_Data
        data = TDF_Data()
        root = data.Root()
        root.FindChild(1, True)
        root.FindChild(2, True)
        it = TDF_ChildIterator(root, False)
        del data, root
        collect()
        print([label.Tag() for label in it])
    """))
    assert out == ["[1, 2]"]


def test_a_copy_keeps_the_original():
    """A copy of an object holding pointers shares them: `Extrema_ExtCC2d(other)` points at the curve the original keeps
    (R-CTOR-KEEP). The copy keeps the original, so the curve outlives the original's variable."""
    out = _ok(_run("""
        from nanocct import Extrema, Geom2d, Geom2dAdaptor, gp
        def line(y):
            return Geom2dAdaptor.Geom2dAdaptor_Curve(Geom2d.Geom2d_Line(gp.gp_Pnt2d(0, y), gp.gp_Dir2d(1, 0)), -10.0, 10.0)
        c1 = line(0.0)
        ext = Extrema.Extrema_ExtCC2d(c1, line(1.0))
        copy = Extrema.Extrema_ExtCC2d(ext)
        del ext
        collect()
        copy.Perform(c1, -10.0, 10.0)
        print(copy.IsDone(), copy.IsParallel())
    """))
    assert out == ["True True"]


def test_a_copy_keeps_what_the_original_stored_before_it_stores_another():
    """The copy shares the pointer the original stored through `Initialize` (R-METHOD-KEEP's slot); the original's next
    `Initialize` drops that argument from its slot. So the copy keeps what the original's slots hold when it is made
    (R-COPY), not only the original: it computed against freed memory (heap-use-after-free under ASan, a different curve
    on a release build)."""
    out = _ok(_run("""
        from nanocct import Extrema, Geom2d, Geom2dAdaptor, gp
        def circle(r):
            return Geom2dAdaptor.Geom2dAdaptor_Curve(Geom2d.Geom2d_Circle(gp.gp_Ax2d(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(1, 0)), r))
        def line(y):
            return Geom2dAdaptor.Geom2dAdaptor_Curve(Geom2d.Geom2d_Line(gp.gp_Pnt2d(0, y), gp.gp_Dir2d(1, 0)), -10.0, 10.0)
        two_pi = 6.283185307179586
        ext = Extrema.Extrema_ExtCC2d()
        ext.Initialize(circle(1.0), 0.0, two_pi, 1e-9, 1e-9)
        copy = Extrema.Extrema_ExtCC2d(ext)
        ext.Initialize(circle(2.0), 0.0, two_pi, 1e-9, 1e-9)
        collect()
        others = [line(9.0) for _ in range(500)]
        copy.Perform(circle(5.0), 0.0, two_pi)
        print(copy.IsDone(), copy.IsParallel())          # concentric circles
    """))
    assert out == ["True True"]


# ---- R-COPY: no copy of a class whose destructor frees what its pointers point to -------------------------------------

def test_an_owner_cannot_be_copied():
    """A copy shares the raw pointers, and the second destructor frees them again: `IntPatch_PrmPrmIntersection_T3Bits`
    deletes its bit array, `BOPAlgo_PaveFiller`/`BOPAlgo_Builder` clear what they own, `IntPatch_Polyhedron` and
    `LocOpe_CSIntersector` destroy theirs (double free / use after free, all five crashed on release builds). Such a
    class has no copy constructor in Python -- `Cls(other)` is a TypeError."""
    out = _ok(_run("""
        from nanocct import BOPAlgo, BRepPrimAPI, Geom, GeomAdaptor, IntPatch, LocOpe, gp
        objects = [IntPatch.IntPatch_PrmPrmIntersection_T3Bits(64), BOPAlgo.BOPAlgo_PaveFiller(), BOPAlgo.BOPAlgo_Builder(),
                   IntPatch.IntPatch_Polyhedron(GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_Plane(gp.gp_Pln())), 4, 4),
                   LocOpe.LocOpe_CSIntersector(BRepPrimAPI.BRepPrimAPI_MakeBox(2, 2, 2).Shape())]
        for obj in objects:
            try:
                copy = type(obj)(obj)
                del copy
                collect()
                print(type(obj).__name__, "copied")
            except TypeError:
                print(type(obj).__name__, "TypeError")
    """))
    assert out == [f"{name} TypeError" for name in ("IntPatch_PrmPrmIntersection_T3Bits", "BOPAlgo_PaveFiller", "BOPAlgo_Builder",
                                                     "IntPatch_Polyhedron", "LocOpe_CSIntersector")]


def test_an_owner_returned_by_const_reference_is_not_copied():
    """`BinObjMgt_Persistent::GetAsciiString(s)` returns `*this` as a `const&`: R-RESULT's copy shared the data blocks, and
    the copy's destructor (`Destroy()`) freed them under the original. An owner's `const&` comes back by reference."""
    out = _ok(_run("""
        from nanocct.BinObjMgt import BinObjMgt_Persistent
        from nanocct.TCollection import TCollection_AsciiString
        p = BinObjMgt_Persistent()
        p.PutAsciiString(TCollection_AsciiString("hello"))
        r = p.GetAsciiString(TCollection_AsciiString())
        print(r is p, p.Length())
        del r
        collect()
        p.PutAsciiString(TCollection_AsciiString("world"))
        print(p.Length())
    """))
    assert out == ["True 6", "14"]


# ---- R-FIELD: a raw pointer member is read-only; it reads as a copy ------------------------------------------------------

def test_a_pointer_member_cannot_be_assigned():
    """`BRepMesh_FaceChecker::Segment::Point1` is a `gp_Pnt2d*`, `V3d_ImageDumpOptions::LightName` a `const char*`: the
    setter stored the address of the Python object (or of the str's buffer) without keeping it, and the next read went
    through freed memory (heap-use-after-free under ASan). Both are read-only now; a null pointer reads as None."""
    out = _ok(_run("""
        from nanocct.BRepMesh import BRepMesh_FaceChecker
        from nanocct.V3d import V3d_ImageDumpOptions
        from nanocct.gp import gp_Pnt2d
        segment, options = BRepMesh_FaceChecker.Segment(), V3d_ImageDumpOptions()
        for obj, name, value in ((segment, "Point1", gp_Pnt2d(3.0, 4.0)), (options, "LightName", "light-" + str(12345) * 50)):
            try:
                setattr(obj, name, value)
                print(name, "assigned")
            except AttributeError:
                print(name, "read-only")
        collect()
        print(segment.Point1, repr(options.LightName))
    """))
    assert out == ["Point1 read-only", "LightName read-only", "None ''"]


# ---- R-OWNER: a TDF_Label, TDF_Attribute or TDF_Data keeps its TDF_Data and that data's TDocStd_Document ---------------

XCAF = BOX + """
from nanocct.NCollection import NCollection_Sequence
from nanocct.TCollection import TCollection_ExtendedString
from nanocct.TDF import TDF_Label
from nanocct.TDocStd import TDocStd_Document
from nanocct.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ShapeTool
def new_document():
    return TDocStd_Document(TCollection_ExtendedString("XmlXCAF"))
"""


def test_a_label_keeps_its_data():
    """`TDF_Data().Root()`: the label points at the root node of a TDF_Data nobody else holds (tests/test_streams.py does
    exactly this). It read the scribbled node (Tag() 1431655765 = 0x55555555)."""
    out = _ok(_run("""
        from nanocct.TDF import TDF_Data
        label = TDF_Data().Root()
        collect()
        print(label.Tag(), label.Depth(), label.IsRoot())
    """))
    assert out == ["0 0 True"]


def test_a_label_keeps_its_document():
    """doc.Main() after the document's variable is gone: the label keeps the data and the document, so the way back from
    the label to its document (TDocStd_Document::Get, through the TDocStd_Owner's raw pointer) stays valid too."""
    out = _ok(_run("""
        main = new_document().Main()
        collect()
        document = TDocStd_Document.Get_s(main)
        print(main.Tag(), main.Depth(), type(document).__name__, document.Main().IsEqual(main))
    """, XCAF))
    assert out == ["1 1 TDocStd_Document True"]


def test_an_attribute_keeps_its_document():
    """An XCAF tool is an attribute in the document's label tree: `ShapeTool(doc.Main())` and then dropping the document
    left the tool pointing at freed nodes."""
    out = _ok(_run("""
        tool = XCAFDoc_DocumentTool.ShapeTool_s(new_document().Main())
        collect()
        label = tool.AddShape(box, False)
        print(tool.IsTopLevel(label), XCAFDoc_ShapeTool.GetShape_s(label).IsSame(box))
    """, XCAF))
    assert out == ["True True"]


def test_a_label_from_an_attribute_keeps_the_document():
    """A label returned by a tool keeps the document, not only the tool: the tool does not own the label tree."""
    out = _ok(_run("""
        document = new_document()
        label = XCAFDoc_DocumentTool.ShapeTool_s(document.Main()).AddShape(box, False)
        del document
        collect()
        print(XCAFDoc_ShapeTool.GetShape_s(label).IsSame(box), TDocStd_Document.Get_s(label).Main().Depth())
    """, XCAF))
    assert out == ["True 1"]


def test_labels_a_call_writes_into_a_sequence_keep_their_document():
    """GetFreeShapes(seq) fills a Python sequence with labels of the document: the sequence keeps their owners."""
    out = _ok(_run("""
        from nanocct.BRepPrimAPI import BRepPrimAPI_MakeSphere
        document = new_document()
        tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
        tool.AddShape(box, False)
        tool.AddShape(BRepPrimAPI_MakeSphere(1.0).Shape(), False)
        labels = NCollection_Sequence[TDF_Label]()
        tool.GetFreeShapes(labels)
        del document, tool
        collect()
        print(labels.Length(), [XCAFDoc_ShapeTool.GetShape_s(label).ShapeType().name for label in labels])
    """, XCAF))
    assert out == ["2 ['TopAbs_SOLID', 'TopAbs_SOLID']"]


def test_a_label_a_call_writes_into_keeps_its_document():
    """FindShape(shape, label) writes into a label Python passed: that label keeps the document."""
    out = _ok(_run("""
        document = new_document()
        tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
        tool.AddShape(box, False)
        label = TDF_Label()
        found = tool.FindShape(box, label, False)
        del document, tool
        collect()
        print(found, XCAFDoc_ShapeTool.GetShape_s(label).IsSame(box))
    """, XCAF))
    assert out == ["True True"]


def test_a_container_keeps_the_owners_of_what_python_puts_in():
    """A sequence holds copies of the labels appended to it; it keeps their owners, and a label read back keeps them too."""
    out = _ok(_run("""
        labels = NCollection_Sequence[TDF_Label]()
        labels.Append(new_document().Main())
        collect()
        first = labels.Value(1)
        del labels
        collect()
        print(first.Tag(), first.Depth(), TDocStd_Document.Get_s(first).Main().IsEqual(first))
    """, XCAF))
    assert out == ["1 1 True"]


def test_a_copy_of_a_label_keeps_its_document():
    out = _ok(_run("""
        copy = TDF_Label(new_document().Main())
        collect()
        print(copy.Tag(), copy.Depth())
    """, XCAF))
    assert out == ["1 1"]


def test_labels_and_their_tool_do_not_keep_each_other_alive():
    """`label = tool.NewShape(); tool.SetShape(label, shape)`: the tool keeps the label (R-METHOD-KEEP: the label's node
    pointer may be stored), so a label keeping the tool back would be a keep-alive cycle no garbage collector sees, and the
    whole document would leak (nanobind's report at exit). A label keeps the document instead (R-OWNER)."""
    _ok(_run("""
        for _ in range(3):
            document = new_document()
            tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
            label = tool.NewShape()
            tool.SetShape(label, box)
            del document, tool, label
            collect()
    """, XCAF))


def test_a_guard_handed_back_to_its_editor_is_released():
    """`ops.SetTolerance(ops.Mut(id), t)`: the RAII guard keeps its editor (R-RESULT-KEEP), so the editor must not keep the
    guard in a slot -- the two would keep each other until exit (16 instances leaked) and the guard's markModified() in its
    destructor would never run. R-CTOR-KEEP's argument-layout test is for constructors only."""
    out = _ok(_run("""
        from nanocct import BRepGraph, BRepPrimAPI
        g = BRepGraph.BRepGraph()
        g.Clear()
        g.Shapes().Add(BRepPrimAPI.BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
        ops = g.Editor().Edges()
        guard = ops.Mut(BRepGraph.BRepGraph_EdgeId(0))
        ops.SetTolerance(guard, 0.5)
        del guard
        collect()
        print(g.Topo().Edges().Definition(BRepGraph.BRepGraph_EdgeId(0)).Tolerance)
    """))
    assert out == ["0.5"]
