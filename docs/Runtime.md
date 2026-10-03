# 5. Runtime model

Part of the nanocct design documents in `docs/`, indexed in [Design.md](Design.md); their section numbers and the `R-…` rule identifiers are shared across them.


## 5.1 Stable ABI

- `nanobind_add_module(... STABLE_ABI NB_DOMAIN nanocct ...)` in linked mode: `Py_LIMITED_API=0x030C0000`, module file `*.abi3.so`, floor Python 3.12.
- nanobind's split mode (backend module, floor 3.10) is not used: it adds a runtime dependency on `nanobind-backend` for two extra Python versions.
- **Gotcha (verified):** nanobind silently drops `STABLE_ABI` unless `find_package(Python ... Development.SABIModule)` is requested (the module is then built as `cpython-314-darwin.so`).

## 5.2 Three kinds of C++ types

### Value types (`gp_*`, `TopoDS_Shape`, `Bnd_Box`, …)

- Plain `nb::class_<T>` with `nb::init<...>`.
- References returned by OCCT are copied (nanobind's default policy for lvalue references).

### `Standard_Transient` descendants

- `nb::class_<T, Base>` plus a type caster for `opencascade::handle<T>` (alias `occ::handle<T>`, `Standard_Handle.hxx:419`) in `src/cpp/common/nanocct_casters.h`, modeled on nanobind's `shared_ptr` caster.
- The Python instance never owns the C++ object; a heap-allocated `handle<Standard_Transient>` is attached with `nb::keep_alive_cb`, so OCCT's intrusive reference count governs lifetime on both sides.
- Constructors are `nb::new_` lambdas returning `handle<T>` so that Python-created objects go through the same path.
- A class whose bound constructors or methods keep arguments (R-CTOR-KEEP, R-METHOD-KEEP) is constructed as `nanocct::Kept<T>`, a binding-side subclass that holds those arguments on the C++ object: they live as long as it does, also when an OCCT container or document holds it after Python dropped it. Python sees `T` (R-KEPT).
- Verified: refcount 1 after construction, 2 after C++ stores the handle, object survives Python GC, comes back as its most-derived type, `load() is back` (nanobind instance map), `None` ↔ null handle.
- A `handle<T>` *parameter* must be declared `nb::arg("x").none()` or nanobind rejects `None` before the caster runs (verified). The generator emits `.none()` for every parameter whose type is `handle<T>` (by value or reference; `Param.is_handle`), so `BRep_TFace().Surface(None)` and `BRep_Builder().UpdateEdge(E, None, L, tol)` pass a null handle (tests); the stubs then spell such parameters `T | None`.

### `Standard_Failure` descendants

- Python exception classes created with `PyErr_NewExceptionWithDoc` (stable ABI), mirroring the C++ hierarchy (`Standard_OutOfRange → Standard_RangeError → Standard_DomainError → Standard_Failure → RuntimeError`).
- `Standard_Failure` itself derives from `std::exception` in OCCT 8 and provides `what()`.
- Translation C++ → Python does **not** use `nb::exception<T>` (catch by derived type): the `DEFINE_STANDARD_EXCEPTION` classes are header-only, so their `typeinfo` is duplicated per shared object and a `catch (Derived&)` in the extension module does not match an object thrown inside `libTKMath` (verified: `Standard_ConstructionError` arrived as `Standard_Failure`). On macOS arm64 the cause is the modules' hidden visibility (see *RTTI across libraries* below); with `-fvisibility-ms-compat` the `catch` matches there (measured), but the name dispatch stays: it does not depend on a platform's RTTI rules.
- Instead every toolkit module registers one translator that catches `Standard_Failure&` and dispatches on `typeid(e).name()` through a per-module map; unknown names are rethrown to the next module's translator (nanobind tries the newest first) and the TKernel translator falls back to `Standard_Failure`.
- Exceptions can also be raised from Python and caught by their bases.

### Returned pointers and references

nanobind's default for a returned raw pointer is *take ownership*, which would `delete` an OCCT object that is still reference-counted (`Standard_Transient::This()` returns `Standard_Transient*`). Rules:

- a pointer or reference to a `Standard_Transient` descendant is wrapped into a `handle<T>` in a lambda (`t.This() is t` holds);
- a pointer to any other class gets `rv_policy::reference_internal` for a method, `rv_policy::reference` for a static method or a free function (R-RESULT);
- a *mutable* reference to a class (`ChangeXxx()` accessors) gets `rv_policy::reference_internal` so in-place edits reach the owner;
- const references and values are copied (nanobind default) -- a `const T&` of a class that cannot be copied comes back by reference, tied to its owner (R-RESULT);
- a value (or a copied `const T&`) of a class that holds pointers keeps alive what produced it, and so does an argument the call writes into (R-RESULT-KEEP); an OCAF label, attribute or data keeps its `TDF_Data` and that data's `TDocStd_Document` instead (R-OWNER).
- an element reference, an iterator or a numpy view of an NCollection container blocks every call that would invalidate it: the call raises `BufferError`, as a `bytearray` does while a buffer is exported (R-VIEW-GUARD).

### Multiple inheritance

- nanobind supports one base and reuses the derived pointer as the base pointer without adjustment: a bound base must be at **offset 0** of the derived object.
- Measured: `NCollection_HArray1<T>` (`: Array1<T>, Standard_Transient`) bound with base `Standard_Transient` returned `myLowerBound` from `GetRefCount()` (5 for an array starting at 5), and `NCollection_Shared<T>` (`: Standard_Transient, T`) bound with base `T` crashed on the first `T` method.
- Rule for a class `S` with several bases:
    - nanobind's base is the offset-0 one (`mi_traits<S>::base` in `nanocct_registry.h`, declared for the NCollection H-types and `Shared` via forward declarations so every TU agrees);
    - members of the other base are bound with lambdas taking `base&` and `static_cast`ing to `S&` (an adjusting downcast);
    - an **MI registry** (`nanocct_register_mi<S>`) gives the `handle<T>` caster two conversions: Python `S` → `handle<Standard_Transient>` (`to_transient` on the stored pointer, then `dynamic_cast<T*>`, so a wrong target type fails cleanly) and `handle<Standard_Transient>` holding an `S` → the stored pointer (`dynamic_cast<void*>` to the complete object, then to the base).
- Verified: `HArray1(5, 9).GetRefCount() == 1`; a `Sequence<handle<Standard_Transient>>` round-trips an `HArray1` and a `Shared<Map<int>>` by identity with exact reference counts; `isinstance(h, NCollection_Array1[T])` is `True`, `isinstance(h, Standard_Transient)` is `False` (documented).
- **RTTI across libraries** (macOS arm64): every library holds its own copy of the RTTI of a template instance (`typeinfo for NCollection_HArray1<int>` is a non-external symbol in `libTKMath`, `libTKXSBase`, `libTKDESTEP`, ...). libc++ on arm64 compares two copies by name only when *both* carry the non-unique bit, and clang sets it only for default visibility — OCCT's copies have it, those of a module compiled with nanobind's `-fvisibility=hidden` do not, so they are compared by address, and an H-array created by nanocct fails OCCT's own `occ::down_cast` in another library (`IGESBasic_HArray1OfHArray1OfInteger.Value()` returns `None`, and `StepToTopoDS_TranslateFace` dereferences the null handle: segfault). So `CMakeLists.txt` adds `-fvisibility-ms-compat` on Apple (= `-fvisibility=hidden -ftype-visibility=default`, after nanobind's flag, the last one wins): types keep default visibility, functions and variables stay hidden, and the modules export no additional symbol. Linux keeps its flags: libstdc++ compares RTTI names with `strcmp` (`__GXX_MERGED_TYPEINFO_NAMES` is 0 by default in its `<typeinfo>`). Windows keeps its flags too: the regression test (`test_h_collections_survive_occt_down_cast`) passes there without the flag (MSVC 14.44, measured). macOS x86_64 gets the same flag, but libc++ compares addresses there (mode 1 in `<typeinfo>`), so the flag's effect there is only measured by that test in CI.
- Generated OCCT classes with several bases get their first base only; the others are reported (rule in section 6, `IMeshData_Edge`).
- **Transient-ness through a template base**: whether a class derives from `Standard_Transient` is decided from the AST base chain; a base that is a template instantiation (`SelectMgr_RectangularFrustum : SelectMgr_Frustum<4>`, `BRepExtrema_TriangleSet : BVH_PrimitiveSet3d` = `BVH_PrimitiveSet<double, 3>`, `Graphic3d_BvhCStructureSet`) is followed into the template's definition through `clang_getSpecializedCursorTemplate` — libclang's cursor for the instantiation has no children, so it alone answers "no bases". The answer is cached by USR, not by spelling: the instantiation and its template share the spelling, and the instantiation's `False` would give the template's derived classes placement-new constructors on a handle-based base (`BRepExtrema_TriangleSet()` would raise `TypeError`).

### Construction

- nanobind constructs value types with placement new, which needs either no class-level `operator new` or a public `operator new(size_t, void*)` (`DEFINE_STANDARD_ALLOC` provides one; `DEFINE_NCOLLECTION_ALLOC` does not).
- Classes failing this and abstract classes get no constructors; the report says so.
- A **non-public base** is always dropped (its members are not inherited publicly, so they are not bound), but it costs the class its constructors only when that base *provides* `operator new` — the allocation function is then inherited inaccessibly and `new Derived(...)` is ill-formed in C++ too (`Message_LazyProgressScope : protected Message_ProgressScope`, `BRepAlgoAPI_Algo : protected BOPAlgo_Options`, both `DEFINE_STANDARD_ALLOC`; verified with a compile test). A base without one leaves the class constructible: `RWObj_CafReader` — the OBJ reader into an XDE document — keeps its public default constructor, and the ten `OpenGl_*` GL function tables keep theirs.
- nanobind also instantiates `wrap_copy`/`wrap_move` (placement new) for every *non-trivially* copy/move-constructible class, so a class whose class-level `operator new` hides the placement form (`DEFINE_NCOLLECTION_ALLOC`/`DEFINE_INC_ALLOC`) **cannot be bound at all** unless it is trivially copyable (`Poly_CoherentTriPtr`: pointer fields only) or not copyable (`NCollection_ListNode`: deleted copy): the five `BRepMeshData_*` implementation classes are skipped and reported (verified with a compile test).
- A class with only non-public constructors gets no implicit default constructor either (`Standard_Type`).
- Among `nb::new_` overloads the zero-argument one must be registered first (nanobind requirement) — constructors are sorted by required-parameter count.
