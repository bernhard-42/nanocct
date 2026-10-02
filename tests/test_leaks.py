"""Memory-growth tests: the ownership rules must not leak C++ objects (Binding-Rules.md R-RESULT).

test_lifetime.py checks that a result or its owner survives when the other side is dropped, and nanobind's report at exit
catches Python objects that are never freed. Neither sees a C++ object that is never freed: a handle whose count never
returns to 0, a permanent reference that outlives its owner. Here every row of R-RESULT / R-PTR-REF / R-PTR-INCOMPLETE
runs its full life cycle many times -- build a fresh owner, take the result, drop both -- and the process's memory must
stay flat.

Why growth and not a leak checker: Apple's `leaks` (tried 2026-09-28) finds a deliberately leaked OCCT object only 0-2
times in 5, because stale copies of its address keep it "reachable"; LeakSanitizer needs a sanitizer build. Growth is
blunt but exact where it matters: measured on macOS, every case below stays at 0 bytes per call, one leaked
Geom_CartesianPoint per call shows as 48 bytes per call -- and test_the_measurement_sees_a_leak keeps proving that.

Each case runs in a fresh interpreter, like test_lifetime.py: one warm-up fifth of the calls (caches, allocator pools),
then four blocks, and the growth between the end of the first block and the end of the last. It fails when that growth
exceeds both BYTES_PER_CALL per measured call and FLOOR, *and* memory grew in each of the three intervals (_leaks) --
a leak grows steadily, an allocator step once: every C++ object is at least 16 bytes, and the floor absorbs a
one-off allocator step -- up to 144 KB measured on macOS, 264 KB on Linux (glibc growing its heap once: the fuse case at
1 000 calls grew by 264 KB in 3 of 5 runs and then stayed flat, at 4 000 calls by 0 KB in 5 of 5). The cheap cases run
40 000 calls, so the floor still means about 17 bytes per call; in the few expensive ones any real leak -- a whole fuse,
a mesh model -- is far larger than the floor. Memory is the resident set on Linux (/proc/self/statm) and macOS (ps), and the
private bytes on Windows (GetProcessMemoryInfo), which the working set could hide by trimming.
"""
from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
BYTES_PER_CALL = 16
FLOOR = 512 * 1024

MEASURE = """
import gc, os, sys
if sys.platform == "linux":
    PAGE = os.sysconf("SC_PAGE_SIZE")
    def memory():
        with open("/proc/self/statm") as f:
            return int(f.read().split()[1]) * PAGE
elif sys.platform == "darwin":
    import subprocess
    def memory():
        out = subprocess.run(["ps", "-o", "rss=", "-p", str(os.getpid())], capture_output=True, text=True, check=True)
        return int(out.stdout) * 1024
else:
    import ctypes
    from ctypes import wintypes
    class _Counters(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t), ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t),
                    ("PrivateUsage", ctypes.c_size_t)]
    _kernel32 = ctypes.WinDLL("kernel32")
    _kernel32.GetCurrentProcess.restype = wintypes.HANDLE
    _psapi = ctypes.WinDLL("psapi")
    _psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(_Counters), wintypes.DWORD]
    _psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
    def memory():
        counters = _Counters()
        counters.cb = ctypes.sizeof(counters)
        if _psapi.GetProcessMemoryInfo(_kernel32.GetCurrentProcess(), ctypes.byref(counters), counters.cb) == 0:
            raise ctypes.WinError()
        return counters.PrivateUsage

def measure(step, calls):
    for _ in range(calls // 5):
        step()
    points = []
    for _ in range(4):
        for _ in range(calls // 4):
            step()
        gc.collect()
        points.append(memory())
    print(3 * (calls // 4), *(p - points[0] for p in points))
"""

BOX = """
from nanocct import BRepPrimAPI, TopAbs, TopExp, TopoDS
box = BRepPrimAPI.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
face = TopoDS.Face(TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE).Current())
"""


def _growth(setup: str, step: str, calls: int) -> tuple[int, list[int]]:
    """Run `step` (the body of a function) `calls` times after `setup` in a fresh interpreter: the measured calls, and the
    memory after each of the four blocks in bytes, relative to the first."""
    body = "def step():\n" + textwrap.indent(textwrap.dedent(step), "    ")
    code = MEASURE + textwrap.dedent(setup) + body + f"\nmeasure(step, {calls})\n"
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=ROOT, timeout=600)
    assert r.returncode == 0, f"rc={r.returncode}\nstdout:\n{r.stdout}\nstderr:\n{r.stderr[-4000:]}"
    measured, *points = (int(v) for v in r.stdout.split())
    return measured, points


def _leaks(measured: int, points: list[int]) -> tuple[bool, str]:
    """A leak grows in every block; a one-off allocator step in one. So: the total growth exceeds the limit, and each of
    the three measured intervals grew by at least a sixth of it (half the share of a leak exactly at the limit). The
    flat cases hit single steps of 544 KB (macOS, fuse, 1 run in 15) and 264 KB (Linux) that stayed flat afterwards."""
    limit = max(BYTES_PER_CALL * measured, FLOOR)
    steps = [b - a for a, b in zip(points, points[1:])]
    leak = points[-1] > limit and all(d >= limit / 6 for d in steps)
    detail = (f"memory grew by {points[-1]} bytes over {measured} calls ({points[-1] / measured:.1f} bytes per call, "
              f"limit {limit}); KB after each block: {' '.join(str(p // 1024) for p in points)}")
    return leak, detail


def _flat(setup: str, step: str, calls: int) -> None:
    leak, detail = _leaks(*_growth(setup, step, calls))
    assert not leak, detail


# ---- the measurement itself ----------------------------------------------------------------------------------------------

def test_the_measurement_sees_a_leak():
    """The control: one Geom_CartesianPoint leaked per call (its count never returns to 0) must fail the limit."""
    leak, detail = _leaks(*_growth("from nanocct import Geom\n", """
        p = Geom.Geom_CartesianPoint(1.0, 2.0, 3.0)
        p.IncrementRefCounter()
    """, 40000))
    assert leak, f"a leak of one object per call went unseen: {detail}"


# ---- R-RESULT: T* to a Transient -> a handle -----------------------------------------------------------------------------

def test_transient_pointer_result():
    """PrsMgr_PresentableObject::Parent() (test_lifetime.test_transient_pointer_result_*)."""
    _flat("from nanocct import AIS\n" + BOX, """
        parent, child = AIS.AIS_Shape(box), AIS.AIS_Shape(box)
        parent.AddChild(child)
        result = child.Parent()
    """, 40000)


# ---- R-PTR-REF: T*& to a Transient -> the pointer, as a handle -----------------------------------------------------------

def test_transient_pointer_reference_result():
    """IMeshData_Wire::GetEdge(), IMeshData_PCurve::GetFace(): released before their model, as OCCT requires
    (test_lifetime.test_imeshdata_objects_outliving_their_model)."""
    _flat("from nanocct import BRepMesh, IMeshTools\n" + BOX, """
        model = BRepMesh.BRepMesh_ModelBuilder().Perform(box, IMeshTools.IMeshTools_Parameters())
        wire = model.GetFace(0).GetWire(0)
        edge = wire.GetEdge(0)
        face = edge.GetPCurve(0).GetFace()
        del edge, face, wire
    """, 4000)


# ---- R-RESULT: T& to a Transient, reference count > 0 (handle-owned) -----------------------------------------------------

def test_transient_reference_result_handle_owned():
    """LDOM_Node::getOwnerDocument(), and LDOM_MemManager::Self() -- the `*this` result that once kept itself alive."""
    _flat("from nanocct import LDOM\n", """
        doc = LDOM.LDOM_Document.createDocument_s("root")
        manager = doc.getDocumentElement().getOwnerDocument()
        manager.Self()
    """, 40000)


# ---- R-RESULT: T& to a Transient, reference count 0 (one permanent reference + keep_alive<0, 1>) -------------------------

def test_transient_reference_result_member():
    """BRepAdaptor_Curve::Curve(): a member held by value gets one permanent reference -- which must die with its owner."""
    _flat("""
        from nanocct import BRepAdaptor, BRepBuilderAPI, GC, gp
        edge = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(GC.GC_MakeCircle(gp.gp_Ax2(), 1.0).Value()).Edge()
    """, """
        owner = BRepAdaptor.BRepAdaptor_Curve(edge)
        result = owner.Curve()
        result.Curve()
    """, 40000)


def test_transient_reference_result_allocator_storage():
    """IntTools_Context::SurfaceAdaptor(): placement-new'd into the context's own allocator."""
    _flat("from nanocct import IntTools\n" + BOX, """
        owner = IntTools.IntTools_Context()
        result = owner.SurfaceAdaptor(face)
    """, 40000)


def test_transient_reference_result_raw_heap_object():
    """BRepClass3d_SolidExplorer::Intersector(): allocated with `new`, deleted by the explorer itself."""
    _flat("from nanocct import BRepClass3d\n" + BOX, """
        owner = BRepClass3d.BRepClass3d_SolidExplorer(box)
        result = owner.Intersector(face)
    """, 40000)


# ---- R-RESULT: T* to another class -> rv_policy::reference; R-PTR-REF; R-PTR-INCOMPLETE ----------------------------------

def test_class_pointer_result():
    """Geom_BSplineCurve::Weights(): a pointer into the curve."""
    _flat("""
        from nanocct import Geom, NCollection, gp
        poles = NCollection.NCollection_Array1[gp.gp_Pnt](1, 3)
        for i, p in enumerate([gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(1, 1, 0), gp.gp_Pnt(2, 0, 0)], 1):
            poles.SetValue(i, p)
        weights = NCollection.NCollection_Array1[float](1, 3)
        for i, w in enumerate([1.0, 2.0, 1.0], 1):
            weights.SetValue(i, w)
        knots = NCollection.NCollection_Array1[float](1, 2)
        knots.SetValue(1, 0.0)
        knots.SetValue(2, 1.0)
        mults = NCollection.NCollection_Array1[int](1, 2)
        mults.SetValue(1, 3)
        mults.SetValue(2, 3)
    """, """
        owner = Geom.Geom_BSplineCurve(poles, weights, knots, mults, 2)
        result = owner.Weights()
        result.Length()
    """, 40000)


def test_class_pointer_reference_and_incomplete_class_results():
    """BRepAlgoAPI_BuilderAlgo::Builder() (`BOPAlgo_Builder* const&`) and BOPAlgo_Builder::PDS() (a forward-declared
    BOPDS_DS*), released before the fuse that owns both."""
    _flat("from nanocct import BRepAlgoAPI, gp\n" + BOX
          + "other = BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(0.5, 0.5, 0.5), 1, 1, 1).Shape()\n", """
        owner = BRepAlgoAPI.BRepAlgoAPI_Fuse(box, other)
        builder = owner.Builder()
        ds = builder.PDS()
        ds.NbShapes()
        del ds, builder
    """, 2000)


# ---- R-RESULT: mutable T& -> reference_internal (methods), a copy (free functions) ---------------------------------------

def test_mutable_reference_method():
    """gp_Pnt::ChangeCoord() into a value class nanobind owns, Poly_Polygon3D::ChangeNodes() into a Transient."""
    _flat("from nanocct import NCollection, Poly, gp\n", """
        p = gp.gp_Pnt(1, 2, 3)
        xyz = p.ChangeCoord()
        xyz.SetX(10.0)
        nodes = NCollection.NCollection_Array1[gp.gp_Pnt](1, 2)
        poly = Poly.Poly_Polygon3D(nodes)
        array = poly.ChangeNodes()
    """, 40000)


def test_mutable_reference_free_function_is_a_copy():
    """TopOpeBRepTool's FSC_GetPSC() and TopoDS::Vertex(): no `self` to tie the reference to, so each call copies."""
    _flat("from nanocct import TopOpeBRepTool\n" + BOX, """
        TopOpeBRepTool.FSC_GetPSC(box)
        TopoDS.Vertex(TopExp.TopExp_Explorer(box, TopAbs.TopAbs_VERTEX).Current())
    """, 40000)


def test_a_transient_returned_by_value_into_a_handle():
    """Geom2dGcc_QualifiedCurve::Qualified() returns Geom2dAdaptor_Curve by value, moved into a handle; an
    Adaptor2d_OffsetCurve then holds it."""
    _flat("""
        from nanocct import Adaptor2d, GccEnt, Geom2d, Geom2dAdaptor, Geom2dGcc, gp
        line = Geom2d.Geom2d_Line(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(1, 0))
    """, """
        qualified = Geom2dGcc.Geom2dGcc_QualifiedCurve(Geom2dAdaptor.Geom2dAdaptor_Curve(line), GccEnt.GccEnt_unqualified)
        curve = qualified.Qualified()
        offset = Adaptor2d.Adaptor2d_OffsetCurve(curve)
        del offset
    """, 40000)
