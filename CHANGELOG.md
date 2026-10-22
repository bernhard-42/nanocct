# Changelog

## v8.0.1.5 (unreleased)

- Building from source on Windows with MSVC 14.51 (Visual Studio 18): the generator's parse of the OCCT headers failed in every package with `use of undeclared identifier '__builtin_verbose_trap'`, because that STL's assertion macros use a clang 19 builtin under clang and the pip libclang is 18.1.1. The parse now defines `_MSVC_STL_USE_ABORT_AS_DOOM_FUNCTION`, the STL's own switch to `abort()` for those macros; the generated bindings are unchanged

## v8.0.1.4 (2026-10-21)

- `AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` works around a third defect, in OCCT's face merging: a face merged with its mirror image (a mirrored revolved part) became two faces, one not closed, or was left with shifted curves when OCCT gave the merge up. A group OCCT broke gets its input faces back; merges OCCT gets right stay
- `AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` works around a second defect of OCCT's edge merging: after merging an edge from several pieces, OCCT can recompute its curve in the face's parameter space one period away on a periodic face, so a hole through a cylindrical face across its period line left the face invalid. The merged curve is moved back to where its pieces were (an exact translation); the merge itself is OCCT's

## v8.0.1.3 (2026-10-12)

- macOS x86_64: an OCCT exception unwinding through one of 309 OCCT functions with a large stack frame (`ChFi3d_FilBuilder::PerformTwoCorner` in a failing fillet, `ShapeFix::SameParameter`, …) could crash the process, because their compact unwind entries read the frame size from the wrong bytes. OCCT is now built without `-fomit-frame-pointer` on x86_64 (the Default profile instead of Production), and the build checks the wheel's unwind entries (`tools/check_compact_unwind.py`)
- The `TopoDS` casts (`TopoDS.Vertex`, `Edge`, `Wire`, `Face`, `Shell`, `Solid`, `CompSolid`, `Compound`) hand back their argument when it already is an object of the target class, as the C++ reference does: the result is the same object, so moving one moves the other. They returned a copy before, so a shape built from another shape's `TopoDS` object stayed behind when that object was moved. An argument of another class (a `TopoDS_Shape` object) still gets a copy. New binding rule R-CAST
- The same for every other reference result that can be one of its arguments or `self` (46 call sites): `BRepBuilderAPI_Sewing.Modified(S)` of a shape sewing did not modify, `BRepOffset_Analyse.EdgeReplacement`, `ChFi2d_Builder.BasisEdge`, `SelectBasics_PickResult.Min_s`, `NCollection_String.Assign` and others return that argument's object instead of a copy when its class is exactly the result's; any other result, an argument of a derived class included (a `TopoDS_Face` given to `Sewing.Modified`), is still a copy

## v8.0.1.2 (2026-10-10)

- Metadata completed for the PyPI release: description (the Readme, with absolute links so that it renders on PyPI), author, keywords, classifiers and project URLs

## v8.0.1.1 (2026-10-03)

**Breaking changes**

- The zero-copy array views are reached through numpy's `__array__`, `np.asarray(obj)`, instead of the six `…Array()` accessors

**Lifetimes and memory safety**

- An object keeps alive what it holds a pointer or reference to: constructor arguments (from its whole layout: base members, typedef'd pointers, members held by value, `void*` members), method arguments it keeps the address of, and what its constructors and methods keep, as long as its C++ object lives
- A `T*` method result keeps its object alive; a value holding pointers keeps what produced it; an OCAF label keeps its data and its document, and an object holding labels keeps the document it was given
- A class holding an allocator keeps itself alive for the Transients it hands out
- No copy of a class whose destructor frees what it points to; a copy keeps what its original holds; pointer members are read-only copies
- A `const T&` result of a class that cannot be copied is returned by reference (the process aborted before), and so are `const&` results of the classes whose copy drops state
- `NCollection_LinearVector.ToArray1()` keeps the vector alive
- A container's live iterators go stale instead of blocking it; a call that would invalidate a live view or numpy array raises `BufferError`
- Memory guards: a leak check in `make test`, lifetime tests per ownership rule, `make asan`

**Fixes**

- macOS: OCCT's `down_cast` recognises template objects created by nanocct (a null handle and a segfault in `StepToTopoDS` before)
- One registry shared by all extension modules: an H-collection bound by one toolkit is accepted as `handle<Standard_Transient>` by every other
- The `ExtremaPC_*` classes are bound; more in/out parameters; handle fields accept `None`; static `T&` results are returned by reference
- An enum parameter takes its enumerators only, as in C++
- A class pointer accepts `None` also without a null default; `__bool__` of a null object is `not IsNull()`
- Static const class data members are read-only static properties; Windows: declaration-only statics link
- The `PLib`/`BSplCLib` overloads that take an array by its first element are not bound (OCCT read past a single `double`); `VrmlData` arrays are sequences; `char` is ASCII-only
- `operator!` and `end()` are not bound; members with unbound types and unreachable overloads are left out
- Images from memory and binary image streams

**Type stubs**

- The stubs are checked with mypy as part of the test suite (pinned per error code), and against the runtime members
- Fixes for NCollection generics, nested classes, enum defaults, `__eq__`/`__ne__`, names with leading or trailing underscores

**Documentation**

- `Pythonic-OCCT.md`: the Python additions to the OCCT API, for developers (operators, equality, enums, exceptions, iteration, streams, AddOns, null handles)
- The design documents are split into `docs/`, one document per topic, with one entry per binding rule

**Build and CI**

- The CI also tests the wheel on Python 3.12, the oldest version it supports
- The CI keeps the dependency caches alive

**Removed**

- The OCP compatibility shim and `nanocctbuild`: [nanocct-tests](https://github.com/bernhard-42/nanocct-tests) sets up build123d and the packages it builds on with nanocct

## v8.0.1.0 (2026-09-28)

- First release: nanobind bindings for the Python 3 stable ABI of Open CASCADE Technology 8.0.1, 45 toolkits (FoundationClasses, ModelingData, ModelingAlgorithms, Visualization without VTK, ApplicationFramework, DataExchange)
- One `cp312-abi3` wheel per platform: macOS arm64 and x86_64, Linux x86_64 and aarch64 (`manylinux_2_28`), Windows x64; the wheels bundle OCCT, FreeType and FreeImage, and ship type stubs
- The OCCT 8 collection classes as Python generics, out-parameters as results, data exchange in memory, zero-copy numpy views of OCCT's arrays
- An OCP compatibility shim wheel was released alongside
