# nanocct design

Open Cascade bindings created with nanobind for the stable ABI of Python 3

The name joins nanobind, which generates the bindings, with OCCT, whose API they expose one to one: nano + occt, sharing the "o". nanobind's `STABLE_ABI` build gives one `cp312-abi3` wheel per platform that runs on every CPython from 3.12 on, without a rebuild. The distribution on PyPI and the import name are both `nanocct`.

What nanocct *is*: the scope, the conventions a user must know, the toolchain, the runtime model, the generator and the rule book. It is meant to be true for as long as the design holds, not to be updated as work proceeds.

Section numbers are stable, because the generator code and the tests cite them ("7.3", the `R-…` rule identifiers). The design documents in `docs/` share them; this one holds the goals and the scope and links to the others below.

How to read them:

- 1–2, this document: what is built, what is in scope, the Python additions and what is not bound ([Excluded.md](Excluded.md)) — README material.
- 3, [Conventions.md](Conventions.md): the naming and parameter conventions a *user* must know.
- 4–6, [Toolchain.md](Toolchain.md), [Runtime.md](Runtime.md), [Generator.md](Generator.md): the toolchain, the runtime model and the generator.
- 7, [Binding-Rules.md](Binding-Rules.md): the rule book -- every deviation from 1:1, one entry per rule with an identifier (`R-…`) that the generator code cites.
- 8, [Build.md](Build.md): build and packaging; 9, [Coverage.md](Coverage.md): the coverage audit of FoundationClasses and ModelingData; 10, [Porting.md](Porting.md): porting from OCP.
## 1. Goals

- Python bindings for Open CASCADE Technology (OCCT) 8.0.1, generated from the OCCT headers.
- **1:1 with the OCCT API**: same class, method, parameter and enum names, same package structure, OCCT's own `//!` comments as docstrings, so the OCCT reference documentation serves as the nanocct documentation. Deviations exist only where Python cannot express a C++ idiom; each one is a documented rule (section 7).
- **nanobind** as the binding library, in **stable-ABI mode** (`abi3`), so one wheel per platform covers all supported CPython versions.
- The generator must be **simple and efficient**: one Python program, libclang for parsing, plain string emission. The generated C++ is **not** checked in — it is ephemeral build input that every platform produces for itself in a few minutes (6.3).
- Platforms for the generator and the wheels: macOS (Apple Silicon), Linux (x86_64 and aarch64), Windows.

## 2. Scope

### In scope

#### Included

All six OCCT modules: `FoundationClasses`, `ModelingData`, `ModelingAlgorithms`, `Visualization`, `ApplicationFramework` and `DataExchange` (STEP, IGES, STL, VRML, OBJ, glTF, PLY; XCAF and its Bin/Xml drivers) — **45 toolkits, all generated**. An audit of `TOOLKITS.cmake` against the manifest leaves exactly the nine toolkits below.

#### Excluded

- Out: `Draw`; `TKIVtk` (its classes derive from VTK's own C++ classes, so using it from Python needs VTK's Python wrappers, which are built for each Python version separately — that would give up the one stable-ABI wheel per platform); `TKOpenGles`/`TKD3DHost` (platform variants of the OpenGL driver, not additional API); `TKExpress` (OCCT's symbolic expression parser, used by nothing in scope); `TKStdL`/`TKStd`/`TKTObj`/`TKBinTObj`/`TKXmlTObj` (linked only by `TKDECascade`) — **nine toolkits**, counted against `TOOLKITS.cmake`.


#### Python additions


Members that have no OCCT counterpart. Each one's docstring says "Python addition"; none replaces an OCCT member, and all of them derive mechanically from the C++ (sections 5.2, 7, 7a hold the rules):

- **Containers** (`NCollection_*`, 7a):
    - `__len__` (= `Length`/`Extent`)
    - `__iter__` (values for arrays, lists and sequences; keys for maps, in index order for the indexed kinds)
    - `__contains__` (always on the maps, by key; on `List`/`Sequence` only where the element type has `operator==`)
    - `__getitem__`/`__setitem__` with the **OCCT index** (`Array1` from `Lower()`, `Sequence` 1-based, `DynamicArray`/`LinearVector` 0-based, `DataMap` by key, the indexed maps by index, `Array2` with a `(row, col)` tuple)
    - `__delitem__` on `DataMap`, `items()` on the maps

    `__call__` and, on the arrays, `__getitem__` are OCCT's own `operator()`/`operator[]` (only the `__setitem__` is the addition there).
    The generic accessor `NCollection_Array1[gp_Pnt]` is the primary spelling (3.1).

- **Mutable primitive references** (`double& Value(i, j)`, R-REF-PRIMITIVE):
    - the getter keeps the OCCT name
    - the setter `Set<Name>` is added (`Change` prefix dropped: `ChangeValue` → `SetValue`) unless OCCT has one
    - for `operator()`/`operator[]`: `__setitem__` (`m[(2, 1)] = 7.0`)

- **Operators** (R-OPERATOR, R-IOP, R-FREE-OP, R-STR):
    - C++ operators become the Python dunders (`__add__`, `__eq__`, `__call__`, `__getitem__`, `__neg__`, …)
    - OCCT's `void operator+=` becomes `__iadd__` returning `self`
    - a free `operator*(double, gp_Vec)` becomes `__rmul__`
    - OCCT's print operator `operator<<(Standard_OStream&, const T&)` becomes `__str__`: `str(aMatrix)` is OCCT's own rendering, the same text as `Dump()` where the class has one; `repr()` stays the default
    - `VrmlData_Scene`'s reading operator `operator<<(Standard_IStream&)` becomes `Read(TextIO)`

- **Conversions** (R-CONV, R-CONV-SCALAR, R-IMPLICIT-CONV):
    - `operator bool/int/double()` → `__bool__`/`__int__`/`__float__`
    - a class with `IsNull()` and no `operator bool` (`TopoDS_Shape`, `TDF_Label`) gets `__bool__` = `not IsNull()`: a null shape is falsy, as a null handle (`None`) and an empty container are (R-NULL-BOOL)
    - `operator T()` → a constructor `T(aFrom)` on the target plus an implicit conversion unless `explicit` (`TopoDS_Shape(aMakeShape)`)
    - non-`explicit` converting constructors convert implicitly as in C++ (`OSD_Path("/x")`)
    - an implicit copy constructor is bound where C++ has one (`TopoDS_Shape(aVertex)` upcasts, R-IMPLICIT-COPY) -- unless the copy would share pointers a destructor frees (R-COPY)

- **`__hash__`** only where OCCT specialises `std::hash<T>` (`TopoDS_Shape`, `gp_Pnt`, `TopLoc_Location`, …), so value-equal shapes are one dict key; a class with a value `__eq__` and no such specialisation is **unhashable**, as it would be in Python (R-UNHASHABLE); everything else keeps identity hashing (R-HASH).

- **Enums** (R-ENUM): unscoped enumerators are attributes of the enclosing module/class as in C++ (`TopAbs.TopAbs_FACE`), `int(e)` works; `enum class` stays nested.

- **Flag sets** (R-BITSET): a `std::bitset<N>` indexed by an enumerator is a Python `set` of those enumerators — `reader.SetShapeProcessFlags({ShapeProcess.FixShape})`; what comes back is a set of plain `int`s, which compare and hash equal to the enumerators.

- **Exceptions** (5.2): `Standard_Failure` and its descendants are Python exception classes with the C++ hierarchy, all deriving from `RuntimeError`; they can be raised from Python.

- **Iteration over OCCT iterators** (R-ITER):
    - every class with `More() -> bool`, `Next()` and a parameterless `Value()` or `Current()` gets `__iter__`, yielding `Value()`/`Current()` while `More()` — `for e in TopExp_Explorer(shape, TopAbs_EDGE):`
    - `iter(x)` is an `nb::make_iterator` that advances `x` itself, so `x` is exhausted afterwards like a file, and a `for` loop costs what a hand-written `More()`/`Next()` loop does (0.46 vs 0.49 µs for 6 faces); `x` as its own iterator, with a `__next__` that ends every loop by throwing a C++ `nb::stop_iteration`, costs ~8 µs per loop
    - the C++ range-for support (`begin()`/`end()`, `operator++`, `NCollection_ForwardRangeIterator`) stays out (R-ITERATOR)

- **Zero-copy array views (R-VIEW)**: a class holding a large contiguous array implements numpy's array protocol, `__array__(dtype=None, copy=None)`, so `np.asarray(obj)` is a numpy view of OCCT's memory, never a copy and never a per-element loop, and `np.array(obj)` a copy. No class gets a method OCCT does not have: the dunder is the only addition, and it is one spelling for every class. Writes go through the view into the object, and the view keeps the object alive. An empty array is a zero-length view, never `None` — `__array__` has to return an array, and whether there is anything is OCCT's question (`HasUVNodes()`, `HasNormals()`, `IsEmpty()`).
    - `NCollection_Array1` and `NCollection_Array2`, inherited by `HArray1`/`HArray2`, for every element type that is a packed run of numpy scalars: `(Size(),)` for `double`/`float`/`int`/`bool`/`unsigned char`, `(Size(), 3)` for `gp_Pnt`/`gp_XYZ`/`gp_Vec`/`Poly_Triangle`, `(Size(), 2)` for the 2d ones, `(Size(), k)` for `NCollection_Vec2/3/4` of `float`/`double`/`int`, and `(NbRows(), NbColumns()[, k])` for an `Array2`. An element with nothing packed to view — a handle, a string, a `TopoDS_Shape` — simply has no `__array__` (numpy then builds an object array of copies, as for any iterable).
    - `Poly_ArrayOfNodes` `(Size(), 3)` and `Poly_ArrayOfUVNodes` `(Size(), 2)`, float64 or float32 as `IsDoublePrecision()` says.
    - `Image_PixMap` `(SizeY, SizeX, channels)`; an empty pixmap is `(0, 0, channels)` of its format's dtype, and `Image_Format_UNKNOWN` raises `ValueError` — `InitTrash` accepts it and allocates real bytes, but there is no dtype to give them.
    - `NCollection_Buffer` `(Size(),)` uint8, zero-length when unallocated; `Graphic3d_Buffer` inherits it, and reshaping to `(NbElements, Stride)` and slicing by `AttributeOffset()` is the caller's, since a buffer of interleaved vertex attributes has no single element type. Without it the class has no data access at all, and `FSD_Base64.Decode_s` — whose result *is* one of these — would be unusable.
    - **Most classes need nothing of their own**: OCCT's accessors hand out the arrays. `Poly_Triangulation`'s four arrays are `np.asarray(tri.InternalNodes())`, `InternalTriangles()` (int32), `InternalUVNodes()` and `InternalNormals()` (always float32, `NCollection_Vec3<float>`); `Poly_PolygonOnTriangulation`'s indices are `np.asarray(p.ChangeNodeArray())`, `Poly_Polygon3D`'s points `np.asarray(poly.ChangeNodes())`. Each is bound `reference_internal`, so the chain of owners keeps the object alive. **Only a non-const reference is zero-copy**: an accessor returning a `const &` (`Triangles()`, `Nodes()`) is bound as a copy, so its view is a view of that copy and writes never reach OCCT (measured).
    - **One view is read-only**: `NCollection_Array1<gp_Dir>` (and `gp_Dir2d`). A `gp_Dir` is normalised by construction and every OCCT setter keeps it so; a raw write could leave a direction of length 0.3 in the array. `SetValue()` is the way to change one.
    - **Two things a reader has to know.** *Indices are OCCT's.* `InternalTriangles()` and `ChangeNodeArray()` hand back 1-based node indices unchanged, which is right for a 1:1 binding and wrong for a renderer — subtract 1 before feeding them to one. *The view has no index base*: element 0 of the view of an `NCollection_Array1` is `Lower()`, whatever `Lower()` is.
- **A byte buffer parameter takes `bytes` (R-BYTES)**: where OCCT spells an input buffer as `const uint8_t*` followed by its length, nanocct takes one `bytes` and reads the length from it — `FSD_Base64.Encode_s(b"...")`. The pair is listed in `overrides.toml [bytes]` rather than inferred, because "the next integer is the length" is a convention and not a type. An *output* buffer (a non-const `uint8_t*`, which the caller is expected to size and own) is not expressible as `bytes` and stays unbound; the class's other overload is the way in. Listed today: `FSD_Base64::Encode`, `Image_AlienPixMap::Load` (an image from memory, `Load(data, "x.png")`) and the `WNT_HIDSpaceMouse` constructor; `tests/test_generator.py` scans OCCT's headers for the pattern, so the list cannot fall behind unnoticed. In a constructor the `bytes` object is kept alive by the new object, because OCCT may keep the pointer (`WNT_HIDSpaceMouse` does).

- **`nanocct.AddOns` — the one package that is not OCCT.** Everything under an OCCT package name is a 1:1 binding; anything that is *ours* lives here instead of being grafted onto an OCCT class, so the 1:1 rule stays true everywhere else. One submodule per concern, so later additions group rather than pile up: `AddOns.Tessellator.NormalsFromSurface(face, uv, reverse)` and `AddOns.Tessellator.EdgeSegments(shape) -> (segments, segments_per_edge, edge_types)`; and, as a workaround for an OCCT bug rather than an addition, `AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` (6, R-ADDON's second row). Hand-written in `src/cpp/AddOns/`, tracked in git, built by `CMakeLists.txt` outside the toolkit loop, and untouched by `make clean_gen`; only its Python shim and its `_PACKAGES` entry are generated. It is a **package, never a toolkit** — `HANDWRITTEN_PACKAGE` in `generator/__main__.py` keeps it out of `generated_pkgs`, because that goes into the manifest and an incremental run would read it back into the toolkit graph, where `_topo` looks for a toolkit OCCT has never heard of.

- **Docstrings**: OCCT's `//!` comments; a deprecated member's first line is `Deprecated in OCCT: <message>` (R-DEPRECATED), a suffixed overload's first line names its C++ signature (R-COLLISION).

#### Excluded classes and methods

Members that nanocct cannot bind and that a user might look for, with the OCCT-level alternative: [Excluded.md](Excluded.md).

### Visualization: whole toolkits

`TKService`, `TKV3d`, `TKOpenGl` and `TKMeshVS` are bound as whole toolkits. Platform headers are handled by `[skip] headers` (`WNT_Dword.hxx` includes `<windows.h>`; `WNT_Window`/`WNT_WClass` guard themselves with `_WIN32`, `WNT_HIDSpaceMouse` is portable and bound). The `[include]` allowlists of 6.2 stay available but are empty.

What the DataExchange headers name from Visualization is small — `Graphic3d_AlphaMode`, `Graphic3d_TypeOfBackfacingModel`, `Graphic3d_TypeOfData`, `Graphic3d_MaterialAspect`, `Graphic3d_Aspects`, `Graphic3d_BndBox3d`, `Graphic3d_Texture2D`, `Image_Texture`, `Image_PixMap` in `XCAFDoc`/`XCAFPrs`/`RWGltf`; `AIS_ColoredShape` in `XCAFPrs_AISObject`; `TPrsStd_Driver` in `XCAFPrs_Driver` — but the link graph requires the toolkits anyway.

### Sizes

`.hxx` headers listed in the packages' `FILES.cmake`, as `generator/occt.py` reads them, OCCT `V8_0_1`. Files outside `FILES.cmake` are not compiled by OCCT and not bound.

| Module | Headers | Toolkits |
|---|---|---|
| FoundationClasses | 575 | 2 |
| ModelingData | 672 | 4 |
| ModelingAlgorithms | 1 494 | 14 |
| ApplicationFramework | 443 | 13 |
| DataExchange | 2 060 | 14 |
| Visualization | 787 | 7 |

## 3. Conventions

[Conventions.md](Conventions.md): 3.1 naming conventions, 3.2 parameter conventions.

## 4. Toolchain and third-party dependencies

[Toolchain.md](Toolchain.md): 4.1 OCCT, 4.2 third-party policy, 4.3 Python side.

## 5. Runtime model

[Runtime.md](Runtime.md): 5.1 stable ABI, 5.2 three kinds of C++ types.

## 6. Package layout and generator

[Generator.md](Generator.md): 6.1 modules and names, 6.2 generator architecture, 6.3 output.

## 7. Binding rules (1:1 and the documented deviations)

[Binding-Rules.md](Binding-Rules.md): 7.1–7.6 the rules by theme, 7a NCollection containers, 7b type stubs, 7c aliases of class templates.

## 8. Build and packaging

[Build.md](Build.md): how the wheels are built and what they carry.

## 9. Coverage of FoundationClasses and ModelingData (2026-09-20)

[Coverage.md](Coverage.md): the coverage audit.

## 10. Porting from OCP (cadquery-ocp) to nanocct

[Porting.md](Porting.md): the porting table.
