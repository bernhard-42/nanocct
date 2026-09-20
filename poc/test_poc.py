import sys, gc
sys.path.insert(0, "poc/build")
import nanoocp_poc as m

print("module file:", m.__file__)
p = m.gp_Pnt(1, 2, 3)
assert p.Distance(m.gp_Pnt()) - 3.7416573867739413 < 1e-12

# --- Transient lifetime ---
cp = m.Geom_CartesianPoint(1.0, 2.0, 3.0)
print("type after new_:", type(cp).__name__, "refcount:", cp.GetRefCount())
assert cp.GetRefCount() == 1                      # only the Python holder
m.store(cp)                                       # C++ takes a handle<Geom_Point>
assert cp.GetRefCount() == 2
del cp; gc.collect()                              # Python side gone, C++ still holds it
back = m.load()
print("returned as:", type(back).__name__, "refcount:", back.GetRefCount(), "X=", back.Pnt().X())
assert type(back).__name__ == "Geom_CartesianPoint"   # polymorphic downcast
assert back.GetRefCount() == 2                    # C++ store + new Python holder
back.SetX(42.0)
assert m.load().Pnt().X() == 42.0                 # same object
assert m.load() is back                           # nanobind instance map: identical Python object
m.clear()
assert back.GetRefCount() == 1
assert m.load() is None and m.make_none() is None # null handle -> None
m.store(None)                                     # None -> null handle
assert m.load() is None

# --- cross-toolkit ---
box = m.BRepPrimAPI_MakeBox(1, 2, 3).Shape()
assert not box.IsNull() and abs(m.volume(box) - 6.0) < 1e-9
print("box volume:", m.volume(box))
print("ALL OK")

# --- DataExchange (STEP) + resources from the local install ---
import os, tempfile
with tempfile.TemporaryDirectory() as d:
    path = os.path.join(d, "box.step")
    back = m.step_roundtrip(box, path)
    assert os.path.getsize(path) > 0
    assert not back.IsNull() and abs(m.volume(back) - 6.0) < 1e-9
    print("STEP roundtrip volume:", m.volume(back), "file bytes:", os.path.getsize(path))

# --- OCCT exception reaches Python (default nanobind translation) ---
try:
    m.raise_occ()
    raise SystemExit("no exception raised")
except Exception as e:
    print("exception type:", type(e).__name__, "| msg:", e)
print("ALL OK (local OCCT 8.0.1)")

# --- Fonts: FreeType (static) + Font_FontMgr system font enumeration + text -> BRep ---
n_fonts = m.system_fonts()
print("system fonts found:", n_fonts)
assert n_fonts > 0
txt = m.text_shape("Helvetica", "Ab", 10.0)
FACE, EDGE = 4, 6                                  # TopAbs_FACE, TopAbs_EDGE
print("text 'Ab': faces =", m.count(txt, FACE), "edges =", m.count(txt, EDGE))
assert not txt.IsNull() and m.count(txt, FACE) >= 2   # 'A' and 'b' -> at least one face each
print("ALL OK (fonts)")
