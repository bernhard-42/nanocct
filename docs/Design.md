# nanocct design

Open Cascade bindings created with nanobind for the stable ABI of Python 3

The name joins nanobind, which generates the bindings, with OCCT, whose API they expose one to one: nano + occt, sharing the "o". nanobind's `STABLE_ABI` build gives one `cp312-abi3` wheel per platform that runs on every CPython from 3.12 on, without a rebuild. The distribution on PyPI and the import name are both `nanocct`.

What nanocct *is*: the scope, the conventions a user must know, the toolchain, the runtime model, the generator and the rule book. It is meant to be true for as long as the design holds, not to be updated as work proceeds.

Section numbers are stable, because the generator code and the tests cite them ("6.3", "2d", the `R-…` rule identifiers). The three documents in `docs/` share them: 2d is [Excluded.md](Excluded.md), 6.1–6.6, 6a–6c and every `R-…` identifier are [Binding-Rules.md](Binding-Rules.md), all other numbers are this document.

How to read this one:

- Sections 1–2 say what is built and the conventions a *user* must know (2a names, 2b parameters, 2c Python additions, 2d what is not bound and the workaround, in [Excluded.md](Excluded.md)) — README material.
- Sections 3–5 describe the toolchain, the runtime model and the generator.
- Section 6, the rule book, is [Binding-Rules.md](Binding-Rules.md): every deviation from 1:1, one row per rule with an identifier (`R-…`) that the generator code cites.
- Section 7 covers build and packaging; 8a is the coverage audit of FoundationClasses and ModelingData and 8b the OCP porting table.

## 1. Goals

- Python bindings for Open CASCADE Technology (OCCT) 8.0.1, generated from the OCCT headers.
- **1:1 with the OCCT API**: same class, method, parameter and enum names, same package structure, OCCT's own `//!` comments as docstrings, so the OCCT reference documentation serves as the nanocct documentation. Deviations exist only where Python cannot express a C++ idiom; each one is a documented rule (section 6).
- **nanobind** as the binding library, in **stable-ABI mode** (`abi3`), so one wheel per platform covers all supported CPython versions.
- The generator must be **simple and efficient**: one Python program, libclang for parsing, plain string emission. The generated C++ is **not** checked in — it is ephemeral build input that every platform produces for itself in a few minutes (5.3).
- Platforms for the generator and the wheels: macOS (Apple Silicon), Linux (x86_64 and aarch64), Windows.

## 2. Scope

### In scope

- All six OCCT modules: `FoundationClasses`, `ModelingData`, `ModelingAlgorithms`, `Visualization`, `ApplicationFramework` and `DataExchange` (STEP, IGES, STL, VRML, OBJ, glTF, PLY; XCAF and its Bin/Xml drivers) — **45 toolkits, all generated**. An audit of `TOOLKITS.cmake` against the manifest leaves exactly the nine toolkits below.
- Out: `Draw`; `TKIVtk` (its classes derive from VTK's own C++ classes, so using it from Python needs VTK's Python wrappers, which are built for each Python version separately — that would give up the one stable-ABI wheel per platform); `TKOpenGles`/`TKD3DHost` (platform variants of the OpenGL driver, not additional API); `TKExpress` (OCCT's symbolic expression parser, used by nothing in scope); `TKStdL`/`TKStd`/`TKTObj`/`TKBinTObj`/`TKXmlTObj` (linked only by `TKDECascade`) — **nine toolkits**, counted against `TOOLKITS.cmake`.

### Visualization: whole toolkits

`TKService`, `TKV3d`, `TKOpenGl` and `TKMeshVS` are bound as whole toolkits. Platform headers are handled by `[skip] headers` (`WNT_Dword.hxx` includes `<windows.h>`; `WNT_Window`/`WNT_WClass` guard themselves with `_WIN32`, `WNT_HIDSpaceMouse` is portable and bound). The `[include]` allowlists of 5.2 stay available but are empty.

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

## 2a. Naming conventions

Every Python name is the OCCT name. Three generated additions exist because Python cannot express the C++ idiom; they follow one lexical rule:

> **OCCT names contain single underscores (`gp_Pnt`, `Geom_Curve`), so the parts of a generated name are separated by double underscores `__`.**

These conventions are the ones a user must know (they go into the README); everything else in section 6 is a rule about *what* is bound, not about names.

### 1. Every static method gets `_s` (R-STATIC-S)

- `BRep_Tool.Pnt_s(vertex)`, `gp_QuaternionNLerp.Interpolate_s(...)`, `XCAFDoc_DocumentTool.ShapeTool_s(label)` — the same rule and the same names as OCP.
- Only static member functions of a class: functions of a C++ namespace are module functions and keep their names (`TopoDS.Edge(shape)`, OCCT 8's `namespace TopoDS`).

### 2. Container instantiations: `<template>__<arg1>__<arg2>…` (6a)

- The concrete class: `Handle_X` for `handle<X>`, nested instantiations spelled recursively — `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`.
- The primary spelling is the generic accessor `NCollection_DataMap[TopoDS_Shape, Geom_Surface](...)`, where a Python type stands for the C++ argument: `float` → `double`, `int`, `bool`, `str` → `std::string`, an OCCT class for itself *and* for `handle<class>`. The five C++ scalars without a Python type of their own are spelled by marker types from `nanocct.NCollection`: `float32` → `float` (32-bit), `uchar` → `unsigned char`, `uint` → `unsigned int`, `ulong` → `unsigned long`, `ulonglong` → `unsigned long long` — so `NCollection_HArray1[float32]` is `NCollection_HArray1__float`, and `[float]` stays C++ `double`.

### 3. Out-parameters become results; colliding overloads get `<method>__<type1>__<type2>…` (R-OUT, R-COLLISION)

- A non-const reference to a primitive, enum or `handle<T>` is dropped from the parameters and returned, after the C++ return value if there is one — `curve, first, last = BRep_Tool.Curve_s(edge)`.
- Class-typed references (`gp_Pnt&`) stay parameters and are filled in place.
- When two overloads have the same inputs and differ only in those out-parameters, **each overload with out-parameters is named `<method>__<type1>__<type2>…`** with the Python types of its returned out-parameters in order:
    - `u, v, w = ics.Parameters__float__float__float(i)` next to `u1, v1, u2, v2 = ics.Parameters__float__float__float__float(i)`;
    - `curve = GeomTools.Read_s__Geom_Curve(stream)`;
    - `x, y, z = pnt.Coord__float__float__float()` next to `pnt.Coord()`, which returns the `gp_XYZ` as in C++ (`const gp_XYZ& Coord()`, `gp_Pnt.hxx:108`); `bnd.Get()` returns `Bnd_Box.Limits` and `bnd.Get__float__float__float__float__float__float()` the six numbers.
- An overload without out-parameters always keeps the plain name, even where a sibling class spells the same name differently (`gp_Dir.Coord()` has no `gp_XYZ` twin and returns the three floats). There is no exception: the name follows from the header alone.
- Types are spelled as in convention 2: `float`, `int`, `bool`, `str` — also for a text stream, `bytes` for a binary one — an enum or class by its Python name, a container by its concrete name.
- The suffix appears only where a collision exists, and after a static's `_s` (`GeomTools.Read_s__Geom_Curve(stream)`).

### Two further name adjustments, mechanical and rare

- A C++ identifier that is a Python keyword gets a trailing underscore (`GProp_PEquation.Type.None_`, R-KEYWORD).
- A mutable reference to a primitive (`double& Value(i, j)`) is bound as the getter plus a `Set<Name>` / `__setitem__` addition (R-REF-PRIMITIVE, 2c).

## 2b. Parameter conventions

Overloads that Python cannot tell apart and that carry no new name (section 6 has the rules and the counts), plus the parameter types that need a word:

- **Const twins: only the non-const overload is bound** (R-CONST-TWIN).
    - `const gp_XYZ& Origin() const` / `gp_XYZ& Origin()`, `TopoDS.Vertex(const TopoDS_Shape&)` / `(TopoDS_Shape&)`.
    - Python objects are never const, so the non-const overload is the one C++ would select.
    - Class results of the bound twin are views into their owner (`arr[i].SetX(…)` edits the container); primitives are values with a `Set<Name>` addition.
- **Scalar width: `double` over `float`, `int` over `size_t`/`unsigned`/`long`** (R-WIDTH).
    - `Abs(double)`/`Abs(float)`, `Value(int)`/`Value(size_t)` are both bound; a Python `float`/`int` goes to the wider one.
- **Strings:** `const char*`, `char` and `TCollection_AsciiString`/`ExtendedString` parameters all take a `str` (a `char` a one-character one) and behave alike; UTF-16 (`char16_t`) round-trips as `str`. A `const char*` with a null default (`LDOM_XmlWriter(const char* theEncoding = nullptr)`, `STEPCAFControl_Writer::Write(…, const char* theIsMulti = nullptr)`) is `str | None = None` (R-CSTR-NULL). **Trap, OCCT's own default:** `TCollection_ExtendedString("pärt")` selects `ExtendedString(const char*, theIsMultiByte = false)` and copies the UTF-8 *bytes* as characters (`"pÃ¤rt"`); pass `True` (`TCollection_ExtendedString("pärt", True)`) for non-ASCII text — as in C++ and OCP.
- **Handles:** every `handle<T>` parameter accepts `None` (the null handle); a returned null handle is `None`.
- **`std::ostream&` / `std::istream&`:**
    - an output stream parameter becomes a returned `str` (`bytes` for **document streams whatever the format** — `BinTools`, the `Bin*`/`Xml*` OCAF driver packages and the format-agnostic `PCDM`/`CDF`/`TDocStd_Application` entry points; a serialised XML document is bytes with an encoding declaration, `data.decode()`/`xml.etree` take it — and for the binary flavour of a format that has both: `RWStl.WriteBinary_s(mesh) -> (ok, bytes)` next to `WriteAscii(mesh) -> (ok, str)`);
    - an input stream parameter takes a text (`io.StringIO`, an open file) or binary (`io.BytesIO`) file-like object — never a `str`, so the file-path overloads stay reachable. A reader that *sniffs* which flavour it got takes bytes, the superset: `RWStl.ReadStream_s(io.BytesIO(...))` accepts binary and ASCII STL alike, while `ReadAsciiStream` stays `typing.TextIO`. Same for the mesh readers — `RWGltf_CafReader.Perform(io.BytesIO(...))` reads a binary `.glb` and a JSON `.gltf` alike, because `RWMesh_CafReader` opens its own files with `std::ios_base::binary` (`RWMesh_CafReader.hxx:187,225`).
- **Optional pointers are dropped** (R-OPTIONAL-PTR): a pointer parameter with a null default (`bool* theIsStored = nullptr` in `BRep_Tool::CurveOnSurface`, `unsigned* theErrorCode = 0` in `BRepFill_AdvancedEvolved::IsDone`, `Standard_OStream* = nullptr` in `BRepBuilderAPI_FastSewing::GetStatuses`) is not in the Python signature; the callee always gets the null pointer.
- The same holds for a **`std::shared_ptr<T>` parameter defaulted to its own empty form** (`RWPly_PlyWriterContext::Open(name, const std::shared_ptr<std::ostream>& = std::shared_ptr<std::ostream>())`): the type has no caster, but its default needs none — the parameter is dropped and the callee gets `nullptr`, which is that same empty `shared_ptr`. `Open(path)` therefore works; without the rule the whole method would be skipped, and `RWPly_PlyWriterContext` — every other member of which needs the stream `Open` creates — would be bound and unusable.
- **Fixed-size arrays are sequences** (R-FIXED-ARRAY): `const int (&theNodes)[3]` takes any sequence of 3 ints; a non-const `gp_Pnt theP[8]` is an out-parameter returned as a list of 8 (`ok, corners = obb.GetVertex()`); a `double myPeriod[3]` member is a list property.
- **Pointer results** (R-RESULT, R-PTR-REF): a returned `T*` (also `T*&`) is the object itself, referencing the owner and keeping it alive (`fuse.Builder()`, `builder.PDS()`); a returned `Transient*` is a handle.

## 2c. Python additions

Members that have no OCCT counterpart. Each one's docstring says "Python addition"; none replaces an OCCT member, and all of them derive mechanically from the C++ (sections 4.2, 6, 6a hold the rules):

- **Containers** (`NCollection_*`, 6a):
    - `__len__` (= `Length`/`Extent`)
    - `__iter__` (values for arrays, lists and sequences; keys for maps, in index order for the indexed kinds)
    - `__contains__` (always on the maps, by key; on `List`/`Sequence` only where the element type has `operator==`)
    - `__getitem__`/`__setitem__` with the **OCCT index** (`Array1` from `Lower()`, `Sequence` 1-based, `DynamicArray`/`LinearVector` 0-based, `DataMap` by key, the indexed maps by index, `Array2` with a `(row, col)` tuple)
    - `__delitem__` on `DataMap`, `items()` on the maps

    `__call__` and, on the arrays, `__getitem__` are OCCT's own `operator()`/`operator[]` (only the `__setitem__` is the addition there).
    The generic accessor `NCollection_Array1[gp_Pnt]` is the primary spelling (2a).

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

- **Exceptions** (4.2): `Standard_Failure` and its descendants are Python exception classes with the C++ hierarchy, all deriving from `RuntimeError`; they can be raised from Python.

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

## 2d. What is not bound, and the workaround

In [Excluded.md](Excluded.md).

## 3. Toolchain and third-party dependencies

### 3.1 OCCT

- Built locally from the `V8_0_1` tag: sources extracted with `git archive` from a checkout into `deps/occt-src` (the exact tag, not a working tree).
- Script `deps/build-occt-macos.sh`; install prefix `deps/occt-8.0.1`.
- **No conda/micromamba anywhere.**

Configuration:

| Option | Value | Why |
|---|---|---|
| compiler | Apple clang (`/usr/bin/clang++`), system libc++ | Wheels must not depend on a conda/Homebrew C++ runtime. An OCCT built inside micromamba links `@rpath/libc++.1.dylib` without an `LC_RPATH`, which makes extension modules fail to load. |
| `BUILD_CPP_STANDARD` | C++17 | OCCT default. |
| `CMAKE_BUILD_TYPE`, `BUILD_OPT_PROFILE` | Release, Production (`-O3 -flto`) | Same as the OCP build scripts. |
| `BUILD_RELEASE_DISABLE_EXCEPTIONS` | **OFF** | OCCT must throw `Standard_Failure` in release builds so Python sees exceptions. |
| `CMAKE_OSX_DEPLOYMENT_TARGET` | 11.1 | Wheel platform tag `macosx_11_0_arm64`, same as OCP. |
| `BUILD_MODULE_Draw`, `USE_VTK`, `USE_TBB`, `USE_TK`, `USE_GLES2`, `USE_FFMPEG` | OFF | Not needed in scope. Without FFmpeg the `Media` package is stubs (verified). |
| `USE_XLIB` | **ON on Linux**, OFF on macOS and Windows | OCCT's own default per platform (`CMakeLists.txt:389`). With it off, Linux goes through EGL, `Xw_Window` is a stub and the viewer never initialises — *"EGL display is unavailable"* even with a GPU. macOS and Windows have no X11. The one flag on which the three builds deliberately differ. |
| `USE_OPENGL` | **ON** | `libTKOpenGl` (1.5 MB) is in the install and links `OpenGL.framework` plus AppKit/IOKit/CoreGraphics — all macOS system frameworks, never bundled (7). Only `OpenGl_GlFunctions.hxx` is guarded by `HAVE_OPENGL`, and it belongs to that toolkit. |
| `USE_FREETYPE` | ON, static build from `deps/build-freetype-macos.sh` | Required by the `Font` package (`Font_FTFont.cxx` is entirely `#ifdef HAVE_FREETYPE`). |
| `USE_RAPIDJSON` | ON (header-only, vendored in `deps/rapidjson`) | glTF reader/writer (`TKDEGLTF`). **Vendored at the pinned tag `v1.1.0` into `deps/rapidjson`**, because a system RapidJSON is not available on every build machine and all platforms need the same version. Header-only, so nothing extra ships in the wheel — but the **include path is needed twice**: an installed OCCT header includes it (`RWGltf_GltfJsonParser.hxx` → `rapidjson/document.h` under `HAVE_RAPIDJSON`), so both the generator's libclang parse (`parse.clang_args`) and the C++ build (`NANOCCT_RAPIDJSON_DIR` in `CMakeLists.txt`) pass it. OCCT's exported targets define `HAVE_RAPIDJSON` but do not carry the path. |
| `USE_FREEIMAGE` | **ON**, shared build from `deps/build-freeimage-{macos,manylinux,windows}.sh` | Without it `Image_AlienPixMap` reads nothing and `Save` writes PPM whatever the extension. **Shared, not static**: only a shared FreeImage registers its codec plugins, and OCCT never calls `FreeImage_Initialise`. Only `FreeImage_*` is exported (254 symbols), so its bundled libpng/zlib/libjpeg cannot collide with another copy in the process: `-fvisibility=hidden` does that on macOS and Windows; on Linux the libstdc++ symbols need a link-time export list as well (`deps/freeimage-version-script.map`). WebP, OpenEXR, LibRaw and JPEG-XR are off. |
| `USE_DRACO`, `USE_D3D` | OFF | glTF has no Draco decompression (`libTKDEGLTF` links no external library); D3D builds `TKD3DHost`, the optional Direct3D wrapper of the visualization module (`adm/cmake/vardescr.cmake:188`), which is only offered on Windows (`CMakeLists.txt:396-400`) and not needed in scope. |

### 3.2 Third-party policy

- The compiled third-party libraries for the whole scope are two: **FreeType** (static) and **FreeImage** (shared).
- FreeType 2.14.3 (sha256 verified against the Homebrew formula) builds in 2 s with its own CMake and `FT_DISABLE_ZLIB/BZIP2/PNG/HARFBUZZ/BROTLI=TRUE` into a static archive that links against nothing but libSystem (verified with a link test loading Helvetica).
- **FreeImage 3.19.15** (danoli3's fork, the pinned tag in `deps/fetch-freeimage-src.sh`) is the third-party image codec. Unlike FreeType it is **shared**, and it has to be: FreeImage registers its format plugins in `FreeImage_Initialise()`, which only a shared build calls by itself (`DllMain` / `__attribute__((constructor))`, both inside `#ifndef FREEIMAGE_LIB`), and OCCT never calls it — so a static FreeImage links and runs but has **no plugins at all**: measured, `Save()` fails for every extension and `Load()` says "unsupported file format", while `AdjustGamma()` still works. delocate/auditwheel bundle the one library (2.4 MB on macOS). It is built with `-fvisibility=hidden`, which leaves **only its own `FreeImage_*` API exported** (254 symbols) and hides every vendored codec — 0 `png_*`, `jpeg_*`, `TIFF*`, `opj_*`, `crc32`, `deflate`, `inflate` — so Pillow's libpng or zlib in the same process cannot be bound to FreeImage's copy, or the reverse. `BUILD_WEBP/OPENEXR/LIBRAWLITE/JXR=OFF`: the four codecs FreeImage can drop without patching. WebP is off *because* its `WEBP_EXTERN` forces default visibility, the one macro the flag cannot beat. For comparison OCP ships FreeImage plus 13 codec dylibs, all exporting everything.
- FreeType is linked into `libTKService` (`otool -L libTKService.dylib` names no FreeType library, so there is nothing to bundle). `libTKService` also links AppKit, IOKit, CoreFoundation, CoreGraphics and Foundation (`CSF_Appkit` and `CSF_IOKit` are unconditional entries in `TKService/EXTERNLIB.cmake`) — macOS system frameworks, not bundled.
- **FreeType's symbols do not leave the library it is linked into** (`deps/occt-unexported-symbols.txt` / `deps/occt-version-script.map`). Being static is not enough: without them `libTKService` re-exports **151** `FT_*` symbols on macOS and **157** in the manylinux build, and ELF has one flat namespace. This is the problem [CadQuery/ocp-build-system#54](https://github.com/CadQuery/ocp-build-system/issues/54) raises.
    - **On Linux the collision is not hypothetical, and OCCT creates it by itself.** `libTKService` has no `DT_NEEDED` for FreeType — `readelf -d` confirms the static archive is the only copy inside it — but it *does* need `libfontconfig.so.1`, and fontconfig's own `DT_NEEDED` names `libfreetype.so.6`. So every nanocct process on Linux already has **two FreeType implementations loaded**: ours inside `libTKService` and the system one pulled in through fontconfig, with the flat namespace free to bind either. Another library bundling a third (matplotlib, Pillow, Qt) only widens it.
    - FreeType already builds with `C_VISIBILITY_PRESET hidden` (its own `CMakeLists.txt`), and it makes no difference: each of its **226** `FT_EXPORT` declarations carries an explicit `__attribute__((visibility("default")))` that overrides the preset.
    - The macro **cannot be redefined from the command line.** The gcc/clang branch of `include/freetype/config/public-macros.h` defines `FT_PUBLIC_FUNCTION_ATTRIBUTE` *unconditionally*, so a `-D` loses to the header — clang reports `macro redefined` and keeps the header's. The `#ifndef` further down is only the fallback for compilers that branch does not recognise.
    - **MSVC needs nothing** (verified: 0 `FT_*` among `TKService.dll`'s 1 228 exports) — its branch marks `dllexport` only under `DLL_EXPORT`, which a static build never defines
    - **So it is done at link time, and FreeType is used unmodified**. `CMAKE_SHARED_LINKER_FLAGS` passes `-Wl,-unexported_symbols_list,deps/occt-unexported-symbols.txt` on macOS and `-Wl,--version-script=deps/occt-version-script.map` on Linux, both listing `FT_*`, `FTC_*` and `TT_*` — measured as the complete set the unpatched static `libfreetype.a` exports (203 + 15 + 2). The result: `libTKService` exports **1 846** symbols, **0** of them `FT_*`, and the FreeType code is still inside it (110 `FT_*` at local `t` binding, and its version string). Two reasons against patching FreeType's header instead: a modified dependency has to be re-checked at every bump, and it would have to be declared in `NOTICE` as a modified copy. Windows needs no flag, for the reason in the previous bullet.
    - **Measured, and FreeType still works on both:** the export list loses exactly the `FT_*` symbols (macOS `libTKService.dylib` 1 996 → 1 845, Linux `libTKService.so` 2 116 → 1 959), and the font manager enumerates and initialises fonts with real metrics on both (2 381 fonts and Helvetica on macOS, the DejaVu family in the container). OCCT uses FreeType only inside `Font_FTFont.cxx` and nanocct binds none of it, so nothing outside the library ever needed those symbols — which the link itself proves.
    - Cost: a FreeType header change makes ninja relink every dependent toolkit, and the manylinux build is `-flto`, so that takes ~18 minutes on a 32-core 2015 box against 26 s on the laptop, whose OCCT tree is not built with LTO.
    - **RapidJSON needs nothing**, measured: **0** symbols of its own on macOS and **1** on Linux (`rapidjson::internal::GetDigitsLut()::cDigitsLut`, a read-only digit table that is identical in every version). Header-only, and everything else inlined into OCCT's own functions — the symbols that mention `rapidjson` in their mangled names are OCCT's, not RapidJSON's.
    - Our own extension modules export exactly one symbol each, `PyInit__<TK>`.
- vcpkg would replace the two library builds with a bootstrap and a triplet per platform, and builds FreeType with the optional dependencies enabled by default. Revisit if the list grows (Draco, TBB); OCCT 8.0.1 has native `BUILD_USE_VCPKG` support.
- Linux additionally needs **fontconfig** (used unconditionally under `HAVE_FREETYPE` in `Font_FontMgr.cxx:86,708`): system package in the manylinux image, bundled by auditwheel.
- Windows enumerates fonts via the registry (*unverified*).

### 3.3 Python side

- Python ≥ 3.12, `uv` project.
- nanobind ≥ 3.1.0 (the `handle<T>` caster uses `nb::keep_alive_cb`, public since 3.1.0). **Documented API only**: what nanobind's documentation describes (call policies, `keep_alive_obj`/`keep_alive_cb`, `inst_ptr`, `type<T>()`, the custom type-caster contract), because an internal can change in any release; the exceptions are listed with their reason in `tests/test_nanobind_api.py` (today `NB_CALL(nb_type_put)` in the two handle casters -- no documented function returns the bound Python type for a runtime `std::type_info` -- and the MSVC `NB_INLINE` redefinition).
- scikit-build-core; pip `libclang` (fallback parser, see 5.2); pytest.

## 4. Runtime model

### 4.1 Stable ABI

- `nanobind_add_module(... STABLE_ABI NB_DOMAIN nanocct ...)` in linked mode: `Py_LIMITED_API=0x030C0000`, module file `*.abi3.so`, floor Python 3.12.
- nanobind's split mode (backend module, floor 3.10) is not used: it adds a runtime dependency on `nanobind-backend` for two extra Python versions.
- **Gotcha (verified):** nanobind silently drops `STABLE_ABI` unless `find_package(Python ... Development.SABIModule)` is requested (the module is then built as `cpython-314-darwin.so`).

### 4.2 Three kinds of C++ types

#### Value types (`gp_*`, `TopoDS_Shape`, `Bnd_Box`, …)

- Plain `nb::class_<T>` with `nb::init<...>`.
- References returned by OCCT are copied (nanobind's default policy for lvalue references).

#### `Standard_Transient` descendants

- `nb::class_<T, Base>` plus a type caster for `opencascade::handle<T>` (alias `occ::handle<T>`, `Standard_Handle.hxx:419`) in `src/cpp/common/nanocct_common.h`, modeled on nanobind's `shared_ptr` caster.
- The Python instance never owns the C++ object; a heap-allocated `handle<Standard_Transient>` is attached with `nb::keep_alive_cb`, so OCCT's intrusive reference count governs lifetime on both sides.
- Constructors are `nb::new_` lambdas returning `handle<T>` so that Python-created objects go through the same path.
- A class whose bound constructors or methods keep arguments (R-CTOR-KEEP, R-METHOD-KEEP) is constructed as `nanocct::Kept<T>`, a binding-side subclass that holds those arguments on the C++ object: they live as long as it does, also when an OCCT container or document holds it after Python dropped it. Python sees `T` (R-KEPT).
- Verified: refcount 1 after construction, 2 after C++ stores the handle, object survives Python GC, comes back as its most-derived type, `load() is back` (nanobind instance map), `None` ↔ null handle.
- A `handle<T>` *parameter* must be declared `nb::arg("x").none()` or nanobind rejects `None` before the caster runs (verified). The generator emits `.none()` for every parameter whose type is `handle<T>` (by value or reference; `Param.is_handle`), so `BRep_TFace().Surface(None)` and `BRep_Builder().UpdateEdge(E, None, L, tol)` pass a null handle (tests); the stubs then spell such parameters `T | None`.

#### `Standard_Failure` descendants

- Python exception classes created with `PyErr_NewExceptionWithDoc` (stable ABI), mirroring the C++ hierarchy (`Standard_OutOfRange → Standard_RangeError → Standard_DomainError → Standard_Failure → RuntimeError`).
- `Standard_Failure` itself derives from `std::exception` in OCCT 8 and provides `what()`.
- Translation C++ → Python does **not** use `nb::exception<T>` (catch by derived type): the `DEFINE_STANDARD_EXCEPTION` classes are header-only, so their `typeinfo` is duplicated per shared object and a `catch (Derived&)` in the extension module does not match an object thrown inside `libTKMath` (verified: `Standard_ConstructionError` arrived as `Standard_Failure`). On macOS arm64 the cause is the modules' hidden visibility (see *RTTI across libraries* below); with `-fvisibility-ms-compat` the `catch` matches there (measured), but the name dispatch stays: it does not depend on a platform's RTTI rules.
- Instead every toolkit module registers one translator that catches `Standard_Failure&` and dispatches on `typeid(e).name()` through a per-module map; unknown names are rethrown to the next module's translator (nanobind tries the newest first) and the TKernel translator falls back to `Standard_Failure`.
- Exceptions can also be raised from Python and caught by their bases.

#### Returned pointers and references

nanobind's default for a returned raw pointer is *take ownership*, which would `delete` an OCCT object that is still reference-counted (`Standard_Transient::This()` returns `Standard_Transient*`). Rules:

- a pointer or reference to a `Standard_Transient` descendant is wrapped into a `handle<T>` in a lambda (`t.This() is t` holds);
- a pointer to any other class gets `rv_policy::reference_internal` for a method, `rv_policy::reference` for a static method or a free function (R-RESULT);
- a *mutable* reference to a class (`ChangeXxx()` accessors) gets `rv_policy::reference_internal` so in-place edits reach the owner;
- const references and values are copied (nanobind default) -- a `const T&` of a class that cannot be copied comes back by reference, tied to its owner (R-RESULT);
- a value (or a copied `const T&`) of a class that holds pointers keeps alive what produced it, and so does an argument the call writes into (R-RESULT-KEEP); an OCAF label, attribute or data keeps its `TDF_Data` and that data's `TDocStd_Document` instead (R-OWNER).
- an element reference, an iterator or a numpy view of an NCollection container blocks every call that would invalidate it: the call raises `BufferError`, as a `bytearray` does while a buffer is exported (R-VIEW-GUARD).

#### Multiple inheritance

- nanobind supports one base and reuses the derived pointer as the base pointer without adjustment: a bound base must be at **offset 0** of the derived object.
- Measured: `NCollection_HArray1<T>` (`: Array1<T>, Standard_Transient`) bound with base `Standard_Transient` returned `myLowerBound` from `GetRefCount()` (5 for an array starting at 5), and `NCollection_Shared<T>` (`: Standard_Transient, T`) bound with base `T` crashed on the first `T` method.
- Rule for a class `S` with several bases:
    - nanobind's base is the offset-0 one (`mi_traits<S>::base` in `nanocct_common.h`, declared for the NCollection H-types and `Shared` via forward declarations so every TU agrees);
    - members of the other base are bound with lambdas taking `base&` and `static_cast`ing to `S&` (an adjusting downcast);
    - an **MI registry** (`nanocct_register_mi<S>`) gives the `handle<T>` caster two conversions: Python `S` → `handle<Standard_Transient>` (`to_transient` on the stored pointer, then `dynamic_cast<T*>`, so a wrong target type fails cleanly) and `handle<Standard_Transient>` holding an `S` → the stored pointer (`dynamic_cast<void*>` to the complete object, then to the base).
- Verified: `HArray1(5, 9).GetRefCount() == 1`; a `Sequence<handle<Standard_Transient>>` round-trips an `HArray1` and a `Shared<Map<int>>` by identity with exact reference counts; `isinstance(h, NCollection_Array1[T])` is `True`, `isinstance(h, Standard_Transient)` is `False` (documented).
- **RTTI across libraries** (macOS arm64): every library holds its own copy of the RTTI of a template instance (`typeinfo for NCollection_HArray1<int>` is a non-external symbol in `libTKMath`, `libTKXSBase`, `libTKDESTEP`, ...). libc++ on arm64 compares two copies by name only when *both* carry the non-unique bit, and clang sets it only for default visibility — OCCT's copies have it, those of a module compiled with nanobind's `-fvisibility=hidden` do not, so they are compared by address, and an H-array created by nanocct fails OCCT's own `occ::down_cast` in another library (`IGESBasic_HArray1OfHArray1OfInteger.Value()` returns `None`, and `StepToTopoDS_TranslateFace` dereferences the null handle: segfault). So `CMakeLists.txt` adds `-fvisibility-ms-compat` on Apple (= `-fvisibility=hidden -ftype-visibility=default`, after nanobind's flag, the last one wins): types keep default visibility, functions and variables stay hidden, and the modules export no additional symbol. Linux keeps its flags: libstdc++ compares RTTI names with `strcmp` (`__GXX_MERGED_TYPEINFO_NAMES` is 0 by default in its `<typeinfo>`). Windows keeps its flags too: the regression test (`test_h_collections_survive_occt_down_cast`) passes there without the flag (MSVC 14.44, measured). macOS x86_64 gets the same flag, but libc++ compares addresses there (mode 1 in `<typeinfo>`), so the flag's effect there is only measured by that test in CI.
- Generated OCCT classes with several bases get their first base only; the others are reported (rule in section 6, `IMeshData_Edge`).
- **Transient-ness through a template base**: whether a class derives from `Standard_Transient` is decided from the AST base chain; a base that is a template instantiation (`SelectMgr_RectangularFrustum : SelectMgr_Frustum<4>`, `BRepExtrema_TriangleSet : BVH_PrimitiveSet3d` = `BVH_PrimitiveSet<double, 3>`, `Graphic3d_BvhCStructureSet`) is followed into the template's definition through `clang_getSpecializedCursorTemplate` — libclang's cursor for the instantiation has no children, so it alone answers "no bases". The answer is cached by USR, not by spelling: the instantiation and its template share the spelling, and the instantiation's `False` would give the template's derived classes placement-new constructors on a handle-based base (`BRepExtrema_TriangleSet()` would raise `TypeError`).

#### Construction

- nanobind constructs value types with placement new, which needs either no class-level `operator new` or a public `operator new(size_t, void*)` (`DEFINE_STANDARD_ALLOC` provides one; `DEFINE_NCOLLECTION_ALLOC` does not).
- Classes failing this and abstract classes get no constructors; the report says so.
- A **non-public base** is always dropped (its members are not inherited publicly, so they are not bound), but it costs the class its constructors only when that base *provides* `operator new` — the allocation function is then inherited inaccessibly and `new Derived(...)` is ill-formed in C++ too (`Message_LazyProgressScope : protected Message_ProgressScope`, `BRepAlgoAPI_Algo : protected BOPAlgo_Options`, both `DEFINE_STANDARD_ALLOC`; verified with a compile test). A base without one leaves the class constructible: `RWObj_CafReader` — the OBJ reader into an XDE document — keeps its public default constructor, and the ten `OpenGl_*` GL function tables keep theirs.
- nanobind also instantiates `wrap_copy`/`wrap_move` (placement new) for every *non-trivially* copy/move-constructible class, so a class whose class-level `operator new` hides the placement form (`DEFINE_NCOLLECTION_ALLOC`/`DEFINE_INC_ALLOC`) **cannot be bound at all** unless it is trivially copyable (`Poly_CoherentTriPtr`: pointer fields only) or not copyable (`NCollection_ListNode`: deleted copy): the five `BRepMeshData_*` implementation classes are skipped and reported (verified with a compile test).
- A class with only non-public constructors gets no implicit default constructor either (`Standard_Type`).
- Among `nb::new_` overloads the zero-argument one must be registered first (nanobind requirement) — constructors are sorted by required-parameter count.

## 5. Package layout and generator

### 5.1 Modules and names

- **One extension module per OCCT toolkit**: `nanocct._TKMath`, `nanocct._TKernel`, …
    - mirrors OCCT's link graph; parallel compilation; all share `NB_DOMAIN nanocct` so types cross module boundaries;
    - each toolkit module first imports the toolkit modules OCCT links it against (from `EXTERNLIB.cmake`) plus the R-LINK extras that precede it in the canonical order, so base classes and default-argument types are registered before use; an extra that comes *later* is linked but not imported — that is what keeps the import graph a DAG while `_TKXSBase` imports `_TKDE` and `_TKDE` only links `libTKXSBase`.
    - **R-IMPORT-BASE:** it also imports the toolkit that binds `T` when it binds `NCollection_Shared<T>`, because the wrapper *derives* from `T` (6a) and nanobind needs the base registered first. OCCT's link graph does not imply that edge — `TKMesh` wraps a `NCollection_DataMap<TopoDS_Shape, int, TopTools_ShapeMapHasher>` that `TKBool` binds, and neither toolkit links the other. Unlike the R-LINK extras this edge ignores the EXTERNLIB order, since that order is precisely what puts the base toolkit too late; a cycle among these edges aborts the generator. The same edge goes to the toolkit binding any instantiation the toolkit's signatures use (R-IMPORT-BASE, 6).
- **One Python module per OCCT package**: `nanocct.gp.gp_Pnt`, `nanocct.Geom.Geom_CartesianPoint`.
    - `import nanocct` loads **nothing**, and `nanocct.gp` is resolved on first attribute access by a PEP 562 module `__getattr__` over the generated package list, so both `from nanocct.gp import gp_Pnt` and `import nanocct` + `nanocct.gp.gp_Pnt` work and neither costs more than the toolkit it needs. The one package that is eager is `nanocct.NCollection`, because other toolkits bind into it (6a). `nanocct/__init__.pyi` declares the submodules with `import nanocct.X as X`, the re-export form the typing spec requires, or a checker would reject `nanocct.gp`.
    - Implementation: the toolkit module creates a submodule per package, sets its `__name__` to `nanocct.<pkg>` (so `gp_Pnt.__module__ == "nanocct.gp"`), registers it in `sys.modules["nanocct._<TK>.<pkg>"]`, and a generated shim `src/nanocct/<pkg>.py` does `from nanocct._<TK>.<pkg> import *`.
- **C++ namespaces** (OCCT 8 uses them in the math packages and in ModelingData: `MathUtils`, `Geom2dGridEval`, `TopoDS`, `Geom2dEval_RepCurveDesc`, `BRepGraphInc`):
    - a namespace named like its package **is** the package module (`MathUtils::DepressCubic` → `nanocct.MathUtils.DepressCubic`, `Geom2dGridEval::CurveD1` → `nanocct.Geom2dGridEval.CurveD1`, `TopoDS::Vertex` → `nanocct.TopoDS.Vertex`);
    - every other namespace becomes a **submodule** (`Geom2dEval_RepCurveDesc::Base` → `nanocct.Geom2dEval.Geom2dEval_RepCurveDesc.Base`, nested namespaces nest);
    - implementation: `def_submodule` in the declare phase, registered in `sys.modules["nanocct._<TK>.<pkg>.<ns>"]`; the shim of such a package is a Python package `src/nanocct/<pkg>/__init__.py` with one module per namespace (`<pkg>/<ns>.py`), so `from nanocct.Geom2dEval.Geom2dEval_RepCurveDesc import Base` works and the stubs follow the same layout (`<pkg>/__init__.pyi`, `<pkg>/<ns>.pyi`);
    - nanobind also registers a submodule under `<parent __name__>.<ns>` = `nanocct.<pkg>.<ns>`; that key is popped again, otherwise `import nanocct.<pkg>.<ns>` would find the extension object without importing the package shim (observed as `cannot import name 'Geom2dEval' from 'nanocct'`);
    - namespaces in `overrides.toml [skip] namespaces` (`std`, `detail`, `Detail`, `Internal`) are not bound; anonymous namespaces are reported.
- **Nested classes** (`Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`, `Geom2dAdaptor_Curve::BezierData`, also when defined out of class: `class BRepGraph::ShapesView { … }`):
    - bound into their outer class (`nanocct.Geom2d.Geom2d_Curve.ResD1`, `__qualname__ == "Geom2d_Curve.ResD1"`), after it, and skipped when the outer class is;
    - the manifest keys are the C++ names (`Geom2d_Curve::ResD1`), and `parse.py_path(name, package, paths)` gives the Python attribute path used by the `NCollection_Xxx[T]` accessor tables, the stubs and cross-package lookups;
    - the name alone cannot tell a *class* named like its package from the package-named namespace (`BRepGraph::ShapesView` must stay `BRepGraph.ShapesView`), nor an alias name of an instantiation: `manifest.json` `paths` records those, computed from the AST.
- **Two registration phases per toolkit**: **declare** all classes and enums of all packages, then **define** members.
    - Reason: nanobind converts default-argument values to Python objects at `.def` time, so every type used in a default must already exist.
    - Packages are declared in base-class dependency order (`FSD_BinaryFile : Storage_BaseDriver` needs `Storage` before `FSD`; computed from the IR, cycles would be reported), classes within a package likewise.
- **Cross-package lookups at registration time** (exception bases) go through the extension submodule `nanocct._<TK>.<pkg>`, never through the `nanocct.<pkg>` shim: importing the shim while the toolkit module is still initialising freezes a half-filled namespace (observed: `nanocct.Standard` with 42 of 120 names).

### 5.2 Generator architecture

`generator/` is a Python package, run as `python -m generator --toolkit TKMath [--package gp]`.

#### Files

- `occt.py`: reads OCCT's own `TOOLKITS.cmake`, `PACKAGES.cmake`, `FILES.cmake`, `EXTERNLIB.cmake` for the module → toolkit → package → header tree and toolkit dependencies. No hand-maintained lists.
- `parse.py`: **libclang AST** (`clang.cindex`), one translation unit per package (an umbrella header including all package headers). Builds the IR in `model.py`. File-scope declarations in a package's `X.lxx` (the inline part `X.hxx` includes at its end) count as declarations of `X.hxx`: `std::hash<TDF_Label>`, `std::hash<TCollection_AsciiString>`, `std::hash<TopLoc_Location>`, `ShallowDump(TopLoc_Location)`, `IsEqual(AsciiString, AsciiString)`, the definition of `math_Matrix`'s friend `operator*(double, math_Matrix)` (deduplicated against the in-class friend), `NCollection_UtfStringTool`, the `TDF_Attribute*Msk` constants all live there, and would otherwise be missing (equal strings would hash by identity). Out-of-line member template definitions and explicit specialisations of member class templates (`BRepGraphInc_Storage::TypedStorePlanes<T>`, private) found at file scope are left to the class walk; `opencascade::MurmurHash` (`Standard_HashUtils.lxx`) is a skipped namespace.
    - Function bodies are parsed, because the `nm` check for declared-but-undefined methods needs to see out-of-class inline definitions (`get_definition()`).
    - It uses the **system libclang that pairs with the `clang` on `PATH`** (located from `clang -print-resource-dir`) and falls back to the pip `libclang` wheel. Reason: the pip wheel is stuck at clang 18 and cannot parse the libc++ of the current Apple SDK (`__builtin_clzg`); the pip wheel also ships no builtin headers, so `-resource-dir` must be passed explicitly. On Linux and Windows the pip wheel's clang 18 is the one used; it spells some types differently from Xcode's, one reason the generated API differs per platform (5.3).
- `binders.py`: the data-only `BINDERS` table of the NCollection binder kinds (6a) — separate from `ncollection.py` (docstring extraction, coverage check, deprecated aliases; needs libclang) so that `parse.py`, `stubs.py` and `__main__.py` import it at top level without a cycle.
- `emit.py`: IR → C++ with plain f-strings, no template engine. The `#include` list is the package headers (prelude first) plus the header of every identifier the emitted code mentions **and of every class behind a typedef in a signature** (`IMeshData::IFaceHandle` = `handle<IMeshData_Face>`, whose header nothing else pulls in), checked by `parse.include_prelude` (R-PRELUDE). `Emitter.emit()` is one method per phase (`_functions`, `_declare_class`, `_define_class`, `_conversions`, `_aliases`, `_includes`); `resolve_overload_collisions()` is a pure function on the IR (unit-tested).
- `parallel.py`: the worker side of the parallel mode below — a pool that parses and emits whole packages in separate processes. Its own module because macOS *spawns* workers: a spawned child re-imports the module holding the callable, and a function defined in `generator/__main__.py` is unreachable that way.
- `report.py`: categories for the report lines and the `report.txt` writer/reader (5.3).
- `model.py`: the IR; `ResultKind`, `StreamKind`, `ConversionKind` are `StrEnum`s. The 6c substitution state is one `Substitution` object in `parse.py` (`_SUBST`), set up and cleared by `_instantiate_template`.
- `symbols.py`: the exported-symbol list of a toolkit library for R-UNDEFINED (6) — `nm` on macOS and Linux, `dumpbin /EXPORTS` on Windows.
- `src/cpp/manifest.json`: classes bound by earlier runs, so a class whose base lives in a not-yet-generated package is skipped with a report line instead of aborting at import (`nb_type_new: base type not known`).
    - A class skipped that way — or because its own base was skipped just before (`IntPatch_PolyhedronBVH : BVH_PrimitiveSet<double, 3>`, whose base `BVH_Object<double, 3>` is unbound) — is removed from the manifest again, so neither a later package nor a later toolkit derives from a class that does not exist.
    - Its nested classes and **nested enums** go with it (`BRepExtrema_ProximityDistTool::ProxPnt_Status`, `IntPatch_BVHTraversal::TrianglePair`): they leave the manifest and the `NCollection_Xxx[T]` accessor table, a typedef of them is reported instead of aliased (R-ALIAS), and an NCollection instantiation over them is skipped and reported (`NCollection_DynamicArray<…ProxPnt_Status>`). Left in the manifest, the alias would abort the import of `TKTopAlgo` (`no attribute 'BRepExtrema_ProximityDistTool'`) and the accessor entry would break `NCollection_DynamicArray[T]` for every `T` (`Template._resolve` resolves all entries at once). Members whose signature still names such a type stay bound and uncallable (8a, usability).

#### Parallel generation (`NANOCCT_JOBS`)

The generator parses and emits every package in a process pool, **one worker per core by default**; `NANOCCT_JOBS=<n>` sets the count and **`NANOCCT_JOBS=1` is the sequential path**, which is what a byte-for-byte comparison is run against (the pools are then never entered). The worker count is capped at the number of packages, so a `--package` run does not pay for idle processes.

Measured on macOS (M5, 18 cores — 6 performance + 12 efficiency, 48 GB), 45 toolkits, 355 packages, **byte-identical output including `manifest.json` at every job count**:

| jobs | parse | emit | total |
|---|---|---|---|
| 1 | 104.5 s | 54.2 s | **161.8 s** |
| 4 | 59.9 s | 15.6 s | 77.7 s |
| 10 | 30.1 s | 8.5 s | 40.9 s |
| 14 | 25.3 s | 7.4 s | 34.9 s |
| **18** (default) | 20.7 s | 6.8 s | **29.9 s — 5.4×** |

More workers keep paying off past the six performance cores, so the default is the core count rather than a guess at the useful number. That the result is identical at 4, 10, 14 and 18 jobs is what says it does not depend on how the packages were distributed.

`parallel.jobs_from_env()` is the one place that decides the count, for these pools and for the stub subprocesses of 6b (**96.4 s → 13.7 s**). A clean regeneration plus stubs takes **43.6 s** (sequentially **258 s**).

A package normally inherits three things from the packages parsed or emitted before it. Each one is an explicit input; left implicit, each is hidden order-dependence, in the sequential generator too:

- **The parser's cross-package state** — `parse._DETECTED_NONCOPYABLE` and the `_derives_from` memo, whose value may have been computed in a translation unit where more was visible. `parse.collect_state()`/`carry_state()` make it an input/output the driver merges at a barrier, a cached `True` never overwritten by a `False`. Without it exactly one binding of ~65 000 differs (`BRepClass3d_SolidExplorer::Intersector`).
- **`known_elsewhere`** — which 6c instantiations an earlier package already bound. `_known_elsewhere_sets()` derives it from the previous round's IRs, replaying what the sequential loop does to `known`: the classes of every earlier toolkit (folded in at each toolkit boundary, a regenerated package's old entries deleted first) plus the classes of the earlier packages of its own toolkit. **Only instantiation spellings are kept**, in both paths: `parse_package` consults the set for nothing else — measured, **339 queries in a 45-toolkit run and every one a name containing `<`** — and those are also the only names R-UNDEFINED cannot remove under us, since it drops classes by plain name only.
- **Instantiation ownership** — who emits a 6a/6c instantiation, which the sequential loop decides *by* emitting (first package to need it claims it). `Emitter.assign_templates()` runs exactly the decisions and nothing else, and the driver runs it over every package in emit order against one shared registry before the pool starts; each package then knows whether it owns a key or aliases it (`Emitter.preassigned`). It is the same code the sequential path runs (`_claim_template()`, shared with the declare phase), not a second implementation. The claim loop must stay *outside* `plan()`: R-DEFAULT-UNBOUND reads the registry during the define phase, so claiming a package's keys up front would let a member see a class `emit()` has not declared yet.

The parse iterates to a fixpoint. **Round 1 runs with the manifest alone** — an empty set in a clean run — so every package instantiates everything it uses (550 instantiation classes against 391 in the steady state) and the owner of an instantiation is the first package in canonical order that has it, which is exactly the sequential rule. **Round 2 parses again with that derived answer and is the result.** The test is on the *inputs*: when the sets derived from a round's output are the sets that round was given, another round would repeat it. Two rounds suffice in practice; four without a fixpoint fails the run rather than writing a result nothing justifies.

Two checks, one free and one on demand:

- **Every parallel run** re-computes `known_elsewhere` the sequential way as the loop walks the packages and compares it with what the pool was given, naming the package and the differing entries and exiting 1 on a mismatch — the derivation simulated from IRs against the accumulation itself.
- **`tests/test_generator.py::test_a_parallel_run_reproduces_a_serial_one_byte_for_byte`**, six toolkits, **skipped unless `NANOCCT_AB=1`**: it has to run the generator serially to have something to compare against, which costs 43 s against the parallel run's 15 s — the whole speedup, spent to re-prove it. Run it after a change to the parse or the emit phase.

#### `overrides.toml` — the only hand-maintained input

Each entry is a documented deviation with a one-line reason. Sections:

- `inout`: the four `gp_*::Transforms` methods whose `double&` parameters are in/out and the two `Geom_Transformation`/`Geom2d_Transformation::Transforms` that forward to them, `Bnd_Sphere::IsOut` (`theMaxDist` compared, then lowered), `ElCLib::AdjustPeriodic` (`U1`/`U2` moved into the period from their incoming values), `BVH_BuildQueue::Fetch` (`wasBusy` from the last call), `Hermit::Solutionbis` (some branches set only one of `Knotmin`/`Knotmax`), `*::InitFromJson` for every class, `Font_FontMgr::FindFont` (`Font_FontAspect&`: the aspect looked for, replaced when an alias maps to another style — `Font_FontMgr.cxx:1060`), and the methods that read and replace a `handle<T>&` — `GeomLib::ExtendCurveToPoint` and five more, `*::ReadCompleteInfo`. OCCT's `@param[in][out]` markers are too sparse to derive the list (`gp_Trsf::Transforms` has none; a survey of the bound headers: every marked non-const primitive/enum reference in the bound headers is either in the list, a protected member or an unbound function template).
- `skip.classes`: internal helpers such as `Standard_Static_Assert<true>`.
- `skip.noncopyable`: `math_GlobOptMin`, bound through a wrapper with deleted copy/move.
- `skip.headers`: platform-specific internals OCCT only includes under `#ifdef`, e.g. `OSD_WNT.hxx`.
- `skip.methods`: members of a 6c instantiation whose template *body* does not compile for the argument — `IntPolyh_Array<IntPolyh_Edge>::Dump` calls `Edge::Dump()` which takes an `int`. Declared-but-undefined members need no entry since the `nm` check compares mangled names per overload (R-UNDEFINED).
- `skip.namespaces`: `std` (only `std::hash` specialisations); `detail`/`Detail`/`Internal` (header-only implementation helpers).
- `instantiate.extra`: container instantiations to bind although no signature uses them (6a).
- `include.packages` / `include.headers`: allowlists for a partial toolkit/package (currently empty); names are validated against `PACKAGES.cmake`/`FILES.cmake`, the other headers are reported.
- `stream.binary_packages`: packages whose streams carry a binary format (R-STREAM-OUT/IN).

#### Principles

- Regular expressions are used only for CMake list files, for recognising `std::basic_ostream`-like canonical types, and for tokenising type spellings into identifiers to collect `#include`s — never to parse C++.
- Type spellings are emitted **as written in the header** (e.g. `Standard_Size`, `size_t`) so the generated C++ is portable; the *canonical* type is used only for analysis (out-param detection, unsupported types).
    - Exceptions: types nested in a class are spelled fully qualified (`gp_Dir::D`), because inside the class the header says just `D`; likewise non-template classes and enums declared in an OCCT namespace (`Geom2dEval_RepCurveDesc::Base`, written `Base` inside the namespace).

### 5.3 Output

- Per toolkit: `src/cpp/<TK>/<pkg>.cpp` (one per package, `nanocct_declare_<pkg>` + `nanocct_define_<pkg>`), `src/cpp/<TK>/_<TK>.cpp` (module init), `src/cpp/<TK>/report.txt`, `src/nanocct/<pkg>.py`, `src/cpp/toolkits.cmake` (the toolkit list in link order plus a `NANOCCT_<TK>_EXTRA_LIBS` line per toolkit that needs one, R-LINK; the lists are kept in `manifest.json` so a partial run does not drop another toolkit's).
- **Generated files are not tracked.** Only three files under `src/` are hand-written and in git: `src/cpp/common/nanocct_common.h`, `src/cpp/common/nanocct_ncollection.h` and `src/nanocct/py.typed`. Everything else — 400 `<pkg>.cpp`, 45 `report.txt`, `manifest.json`, `toolkits.cmake`, `common/ncollection_docs.h` and 742 `.py`/`.pyi` shims, 1 190 files — is regenerated.
    - **Why:** OCCT's headers are platform-dependent, so one generation platform cannot serve the others. `WNT_Window.hxx:34` sits inside `#if defined(_WIN32) && !defined(OCCT_UWP)` (lines 22-175), so a macOS generation produces **no `WNT_Window` at all** and a Windows user would have no native window class. The converse is *not* symmetric: `Cocoa_Window` (`:60`) is **not** guarded — the `#if defined(__APPLE__)` at `:19` closes at `:21` around an include — so it is declared everywhere and only *defined* on macOS. On Windows it therefore binds as five classes with **zero methods** (R-UNDEFINED finds none of them in `TKService.lib`), which is the other half of the same argument: each platform must generate for itself. The standard library diverges too. The code is ephemeral and builds in a few minutes; `report.txt` is a debug and verification tool for a build, and the `.so` files are its result.
    - **The cost**: `report.txt` has no git history, so a regeneration that loses a member is not visible as a `git diff` — it is a per-build artefact to read on the spot. The toolkit tests that assert on it work only after a generation: the contract is **fetch deps → generate → build → test**, which is what CI does on each platform anyway.
    - Users installing a wheel never need libclang; building from source does.
- **The report**: every run prints everything not bound and why and, for a full toolkit run, writes it to `report.txt`.
    - One line per omission: `category<TAB>package<TAB>what: why`; categories assigned from the message text by the table in `generator/report.py` (a message no pattern knows lands in `misc`, currently empty; tests assert that).
    - The file is the coverage instrument: a regeneration that loses a member shows up as a change in `report.txt` (compared against the previous build's copy, not against git), and `tests/test_TKBRep.py::test_unbindable_classes_are_reported_not_bound` reads it.

## 6. Binding rules (1:1 and the documented deviations)

In [Binding-Rules.md](Binding-Rules.md): sections 6.1–6.6 and 6a–6c, and every `R-…` rule identifier.

## 7. Build and packaging

- **`CMakeLists.txt`** at the root: `find_package(OpenCASCADE)` from `NANOCCT_OCCT_DIR` (default `deps/occt-8.0.1`), one `nanobind_add_module` per toolkit from `src/cpp/toolkits.cmake`, each linked against its OCCT toolkit plus `${NANOCCT_<TK>_EXTRA_LIBS}` (R-LINK), `INSTALL_RPATH` pointing at the OCCT lib dir for development builds.
- **`pyproject.toml`**: scikit-build-core, `wheel.py-api = "cp312"`, `build-dir = "build/{wheel_tag}"` (incremental rebuilds), `wheel.packages = ["src/nanocct"]`.
- **One runtime dependency: `numpy>=2,<3`**, for the zero-copy views (R-VIEW). The upper cap is deliberate — the 1 → 2 transition broke things and the same is expected of 2 → 3, which is the high-risk case that earns one — and it matches build123d's own pin. numpy is *not* bundled, so it needs no entry in `licenses/`. The failure mode without it is call-time, not import-time: a module still imports and only the view accessor raises `TypeError: could not export nanobind::ndarray: ModuleNotFoundError`, so declaring it is a choice rather than a constraint. Reasoning also in `pyproject.toml` beside the pin.

- **Licensing.** nanocct's own code is **Apache-2.0** (`LICENSE`), declared as a PEP 639 SPDX expression (`license = "Apache-2.0"`, metadata 2.4). The wheel is an aggregate, so every licence whose code ends up in it travels with it via `license-files`: OCCT (**LGPL-2.1 with the Open CASCADE exception**), and inside it FreeType 2.14.3 (**FTL**, statically linked into `libTKService`), RapidJSON (**MIT**, header-only, in the glTF reader) and nanobind 3.1.0 with its vendored `tsl::robin_map` (**BSD-3** / **MIT**, compiled into every module). The texts are in `licenses/`, the attributions in `NOTICE`, and `licenses/README.md` records the rule: **a licence belongs there when its code ends up in the wheel** — build-time-only tools (scikit-build-core, cmake, libclang) ship nothing and are not listed. The list also carries **FreeImage** (FIPL 1.0, the permissive one of the three it offers) and the six codecs it vendors — zlib, libpng, libjpeg, libtiff, OpenJPEG and Imath's `Half`.
    - Apache-2.0 is available *because* of the OCCT exception, which lets object code incorporating material from OCCT headers — which every generated binding does — be distributed "under terms of your choice", conditional on a prominent notice that the code "makes use of or is based on facilities provided by the Open CASCADE Technology software". `NOTICE` carries that sentence verbatim, and `tests/test_licensing.py` asserts it: the wording is a licence condition, not prose. The bundled `libTK*` stay LGPL and are dynamic, so a recipient can replace them; `NOTICE` points at the pinned OCCT tag for the corresponding source.
    - **No dependency is modified**, which is a licence position and not only a maintenance one: the FIPL's §3.2 would oblige us to publish source for any change to FreeImage, and a modified FreeType would have to be declared as such; FreeType's symbols are hidden at link time for exactly this reason (3.2).
    - The ten tests in `tests/test_licensing.py` exist so a newly bundled dependency cannot arrive without its licence: a distribution without a declared licence is all-rights-reserved by default, which bundling LGPL and FTL code does not allow.
    - On macOS `CMAKE_OSX_DEPLOYMENT_TARGET = "11.1"`, the same as OCCT's, so the `.abi3.so` carries `minos 11.1` (verified with `otool -l`; without it the SDK's 26.0 is inherited). `make compile` passes it (the wheel is packed from those modules), and pyproject.toml's scikit-build override does the same for a build from source; without it delocate refuses the wheel ("has a minimum target of 26.0").
    - The generated targets compile with `-Wno-deprecated-declarations` / `/wd4996` because deprecated members are bound on purpose (6, R-DEPRECATED).
    - Development loop: regenerate → `uv sync --reinstall-package nanocct` → `pytest`.
- **Wheels**: every step runs once -- `make generate compile stubs wheel delocate test`. `make wheel` packs the raw wheel from the staged tree that `compile` and `stubs` produced (`generator/wheel.py`, stdlib only: the `.py`/`.pyi` files, `py.typed`, the extension modules, the metadata and licence files from pyproject.toml, a RECORD), `make delocate` repairs it with each platform's tool, and `make test` installs the repaired wheel into a fresh venv (`.venv-test`) and runs the suite against it, so what is tested is what ships. `uv build` is not used for it: its backend, scikit-build-core, cannot pack without compiling, so every binding would be compiled twice -- the longest step on the slower CI runners (Windows: over 30 minutes). The packed wheel has the files and metadata of scikit-build-core's (compared file by file; only `Requires-Dist` keeps pyproject.toml's spelling); scikit-build-core stays the build backend for a build from source. CI runs the same Makefile targets on five platforms (`.github/workflows/build-wheels.yml`), and `release.yml` attaches the cached wheels of a tagged commit to a GitHub release. A wheel straight from the build backend is **not portable** — its extension modules reach the OCCT libraries through an rpath into `deps/`, so it works only on the machine that built it. The repair copies those libraries in and rewrites the references to point inside the wheel. Measured, not planned:
    - **macOS** `delocate-wheel`: 20 MB → **44 MB**, 50 `libTK*` dylibs under `nanocct/.dylibs/`, no reference left into the source tree. The extensions link nothing but `libTK*`, libc++ and libSystem, and OCCT itself pulls only system frameworks (AppKit, CoreFoundation, CoreGraphics, Foundation, IOKit, OpenGL) — **no FreeType** (static inside `libTKService` since 3.2) and no RapidJSON (header-only).
    - **Linux** `auditwheel repair --plat manylinux_2_28_x86_64`: 25 MB → **50 MB**, 56 libraries, **`libfontconfig` bundled** because it is not on the policy's whitelist, while `libGL.so.1`, `libX11.so.6`, `libexpat.so.1` and `libstdc++.so.6` are on it and stay the host's (checked against auditwheel 6.8.2's own `manylinux_2_28` list of 24 entries, not from memory). Verified on a real host rather than in the build image: Ubuntu 22.04, glibc 2.35, with `LD_LIBRARY_PATH` and `PYTHONPATH` unset.
    - **Windows** `delvewheel repair --add-path <occt>/win64/vc14/bin`: 26 MB → **48 MB**, 52 DLLs in a sibling `nanocct.libs/`. The path must be given, because a PE binary carries no rpath for the tool to follow. Two consequences worth knowing. delvewheel **mangles the bundled names** (`TKBin-0e980c01ba84195e41fe9ccc44b205dc.dll`), which is what lets nanocct and cadquery-ocp hold their own OCCT in one process instead of the first loaded DLL winning. And it **prepends a patch to `nanocct/__init__.py`** that calls `os.add_dll_directory(libs_dir)`, guarded by `isdir` and deleted after use -- the same mechanism the development loop needs through `sitecustomize.py` and `NANOCCT_OCCT_BIN`, because Python has ignored `PATH` for extension-module DLLs since 3.8. The patch is additive: the PEP 562 `__getattr__` and `_PACKAGES` of 5.1 survive it, and `import nanocct` still loads no toolkit (verified on the installed wheel). `msvcp140.dll` is bundled, which is delvewheel's default and means a machine without the VC++ redistributable still works; `opengl32.dll` is not.
    - **OpenGL is never bundled**: `OpenGL.framework` is a system framework on macOS (deprecated since 10.14, present, GL 4.1 core), `libGL.so.1` and `libX11.so.6` are whitelisted on manylinux (Linux needs a working Mesa/vendor GL at runtime, as OCP does), `opengl32.dll` is a system DLL on Windows.
    - What the repair depends on: **every OCCT dylib names its siblings `@rpath/libTKX.8.0.dylib` but carries no `LC_RPATH` of its own**: invisible at runtime, because the extension module supplies the rpath for the whole load chain, but fatal to any tool that walks the graph statically — delocate stops at `libTKBO` with "Could not find all dependencies" and has no flag for extra search paths. `deps/build-occt-macos.sh` therefore adds `@loader_path` to each installed library. And a build from source with **`uv build --no-build-isolation` needs an explicit `--python`**, or it picks its own interpreter for the build environment and fails with "No module named 'scikit_build_core'" although the venv has it (measured on Windows, where `VIRTUAL_ENV` is unset).
    - The wheel is `cp312-abi3`, so a 3.10 interpreter rejects it as "not a supported wheel on this platform" — that message means the interpreter, not the platform tag. macOS wheels stay tagged `macosx_11_0_arm64`: 11.x tags normalise to `11_0`, and `MACOSX_DEPLOYMENT_TARGET=11.1` is set for delocate's own verification, not to change the tag.
- **`Makefile`** — one entry point for building it yourself on all three platforms: `make env` creates the venv, `make deps` fetches and builds RapidJSON, FreeType, FreeImage and OCCT in that order, `make generate compile stubs wheel delocate test` is the build, each step once, and `make wheels` runs it end to end plus the shim, ending in nanocct's wheel and the shim's in `dist/`. **Verified from a bare checkout on each platform** — a tree holding only the tracked files, no sources, no venv, no dependencies — which is the only thing that exercises this contract. `make wheel` packs the wheel into `dist/unrepaired/`, `make delocate` repairs it into `dist/` (`clean_dist` to start over).
    - **Linux goes through the container alone** (`deps/run-manylinux.sh`), so there is one Linux environment and it is the one CI uses; `xorg-x11-server-Xvfb` is in the image for that reason, since the viewer tests need a display and the suite would otherwise have to run on the host. A display is not enough on its own: `mesa-libGL-devel` satisfies the *link*, but without `mesa-dri-drivers` and `libglvnd-glx` the X server has no GLX extension and OCCT stops with *"OpenGl_GraphicDriver, GLX extension is unavailable"*. With them Xvfb reports `direct rendering: Yes` on llvmpipe.
    - **Windows needs Git Bash.** `uname`, `cygpath` and the generated `vcvars64` `.bat` are POSIX-shell idioms; run from `cmd.exe` or PowerShell the Makefile stops with a message saying so.
    - **`compile` builds with cmake/ninja rather than `uv sync`**, so it reports progress (`[445/446] Linking CXX shared module …`) instead of a spinner, and so the three platforms have one shape: build into a directory, stage it (`deps/stage.sh`), and let `stubs` and `test` import the staged tree through `PYTHONPATH`. Installing into the venv belongs to the wheel path, not the loop.
    - **Exactly one copy of the extension modules may be in a process.** nanobind registers its types per `NB_DOMAIN`, so a wheel-installed `nanocct` beside the staged one aborts the import with *"Critical nanobind error"* before any traceback. `compile` therefore uninstalls the venv copy after staging. Isolating with `python -S` is *not* the fix: it drops site-packages, and with it libclang and pytest.
    - `clean_gen` removes only generated files: `src/cpp/common/nanocct_common.h`, `nanocct_ncollection.h`, `src/nanocct/_templates.py` and `py.typed` are hand-written and tracked (5.3).
    - **The upstream sources are fetched, not assumed.** `deps/fetch-occt-src.sh` (`V8_0_1`) and `deps/fetch-freetype-src.sh` (`VER-2-14-3`) clone into `deps/occt-src` and `deps/freetype-src` when they are missing; `make sources` runs both, and `make freetype`/`make occt` call the one they need, as does `deps/build-occt-manylinux.sh`, so the tags are pinned in a single place. A tag rather than a checksummed tarball the way `deps/fetch-rapidjson.sh` does it, because OCCT publishes no release tarball for `V8_0_1` — a moved tag would go unnoticed, which the script says.
    - **The development interpreter is pinned**: `PY_VERSION := 3.14` drives `uv venv -p` and `ML_SYSPY` (`/opt/python/cp314-cp314/bin/python` in the container). It is **not** the wheel's floor — `requires-python = ">=3.12"` and `wheel.py-api = "cp312"` say what a *user* can install, and a 3.14 build still emits a `cp312-abi3` wheel. Without the pin the machines drift apart (3.14.7, 3.12.13 and 3.12.12 were measured), and the suite runs on a different Python depending on where it runs. Nothing exercises the 3.12 floor in development any more; that is the CI matrix's job.
    - **`make env` uses `uv sync --no-install-project` on every platform, including inside the container** (`uv` is in the manylinux image), against the one `dev` group in `pyproject.toml`. A hand-written `pip install` list drifts (one missing `libclang` makes `make generate` die with *"No module named 'clang'"*). `uv venv` also *replaces* an existing environment, which `python -m venv` does not, so an interpreter pin takes effect.
    - **Each platform's OCCT install has its own shape**, and both halves matter to anything that goes looking: the prefix is `deps/occt-8.0.1` on macOS and Windows but `deps/occt-8.0.1-manylinux` in the container, and the headers are `<install>/inc` on Windows and `<install>/include/opencascade` elsewhere. `OcctTree.include_dir` is the single place that resolves the second, and both the generator and the tests go through it — spelling either out by hand makes the generator tests skip on Linux *and* on Windows, reporting that no local OCCT build is present.
    - **Windows needs the OCCT DLL directory named explicitly.** Python has ignored `PATH` for extension modules since 3.8, so `deps/stage.sh` writes a `sitecustomize.py` calling `os.add_dll_directory` next to the staged package — the development twin of what `delvewheel` prepends to `nanocct/__init__.py` in the wheel. Without it `make stubs` and `make test` fail with *"DLL load failed while importing _TKBO"*.
- **Tests**:
    - `tests/test_<TK>.py` per toolkit against the built bindings, each generator rule exercised at least once;
    - `tests/test_generator.py` tests the generator itself — the IR of a synthetic header with one member per §6 rule (`parse_package` on a private include directory, no compiler), the overload-collision resolver, the report categories, the header allowlist, a scan of the checked-in stubs for overloads with identical Python signatures (6.4), and a regeneration of `TKG2d` into a temporary directory that must reproduce `src/cpp/TKG2d` byte for byte (the canonical-state check, ~5 s);
    - `tests/test_typing.py` runs mypy and ty on `tests/typing/check_*.py` (6b);
    - **the memory guards**: `tests/test_lifetime.py` drops one side of an ownership relation and uses the other, each scenario in a fresh interpreter with the allocator scribbling freed memory, for every lifetime rule of §6; `tests/test_memory_audit.py` holds the audit's targeted scenarios (a method or base member storing an argument, a copy sharing what a destructor frees, a view into a container, a pointer field, release and retention); `tests/test_lifetime_counts.py` is a ratchet on how many bindings each lifetime rule touched and on its report categories, pinned per platform -- an OCCT update or a generator change shows there, not only in the generated code; `tests/test_nanobind_api.py` lists every use of nanobind's internals in the hand-written C++ (`NB_CALL(nb_type_put)` in the two handle casters, the MSVC `NB_INLINE` redefinition) against an allowlist with the reason, with nanobind's backend functions read from the installed `nb_backend_slots.h` -- a new use fails, as does any in the generated code; `make test` runs pytest through `tools/pytest_leakcheck.py`, which fails on nanobind's `leaked` report at interpreter exit (a reference cycle no garbage collector sees, R-KEPT); `make asan` (macOS, opt-in) builds OCCT and the bindings with AddressSanitizer into `build/asan` (`tools/asan/`) and runs the lifetime tests and the audit's scenarios under it (`ASAN_TESTS=tests` for the whole suite), where a read of freed memory aborts with ASan's report instead of passing by coincidence;
    - the 38 tests in `test_generator.py` that parse real headers need a local OCCT build and **skip** without one, so they resolve the install the way the generator does rather than by hand — a skip is silent.


## 8a. Coverage of FoundationClasses and ModelingData (2026-09-20)

Numbers from a fresh generator run of the six toolkits (`python -m generator --toolkit X --out <scratch>`, tree untouched).

### Bound

- 1 484 classes, 14 756 methods, 256 free functions — TKernel 230/2 137/123, TKMath 271/3 789/105, TKG2d 59/892/0, TKG3d 128/2 137/0, TKGeomBase 326/2 426/9, TKBRep 470/3 375/19 (classes/methods/functions).
- Every package of both modules is generated; the OCCT 8 idioms that used to block whole APIs (namespaces, nested classes, nested and dependent templates, conversion operators, streams, mutable primitive references) are handled by rules, not by hand (6, 6c).

### Not bound: 1 360 report lines, all in explainable categories

- Since 2026-09-21 the lines are persisted per toolkit in `src/cpp/<TK>/report.txt` with a category column (`generator/report.py`), so `git diff` shows coverage changes and the totals below can be reproduced with `cut -f1 src/cpp/TK*/report.txt | sort | uniq -c`.
- 1 307 lines on 2026-09-21: +6 overload collisions from the handle out-parameter rule, +3 from binding deprecated members whose non-deprecated twin has the same Python signature, −62 deprecated members now bound, see 6.

| Lines | Category | Verdict |
|---|---|---|
| 551 | function/class templates and template members: functor-based algorithms (`MathOpt::BFGS<F>`, `MathRoot::Newton<F>`, `MathInteg::*`, `MathSys::Newton<F>`), `NCollection_MapAlgo`/`PackedMapAlgo` set algebra, `IsValidIn<CountProviderT>` | the one *chosen* gap: needs Python callables (trampolines, not planned); the classic `math_*` classes cover the same ground |
| 126 | STL-style iterators (`begin()`/`end()`, `DynamicIterator` overloads) | Python iterates with `__iter__` (containers, and R-ITER on `More`-`Next`-`Value` classes) |
| 125 | raw pointers to primitives: 67 `AdvApp2Var` Fortran-style internals, buffers (`NCollection_Buffer`, `FSD_Base64`), `char16_t*` non-const | inherent; byte buffers revisited with DataExchange |
| 122 | `operator++`, `operator<<`, `operator>>` | no Python equivalent; the stream-like writers (`BinTools_OStream`, `Message_Msg::Arg`) have named entry points where it matters |
| ~~62~~ / 50 / 48 / 44 | ~~deprecated members~~ (bound since 2026-09-21, R-DEPRECATED) / `std`, `detail`, `Internal` namespaces / `void*` allocator APIs / raw element pointers (`Data()`) | by rule |
| 48 | stream leftovers: stream-holding constructors and members (`BinTools_IStream`, `Message_PrinterOStream`), `ostream&` returns without a stream parameter, free `operator<<` | inherent (an object may keep the reference) |
| 30 | overload collisions after out-param removal | since the R-COLLISION suffix rule nothing is lost: every such overload is bound as `Name__<out types>` (6); the lines list the names |
| 28 / 26 / 11 / 9 | `_s` renames / conversion operators to enums or `string_view` / declared-but-undefined (`nm`) / `overrides.toml` | naming convention / no spelling / not callable in C++ either / documented |
| ~80 | misc: 16 free operators without a class operand, 15 `char*&`, 8 rvalue references, C arrays, variadics, `initializer_list`, anonymous namespaces | inherent |

### Usability check

- Bound members whose signature names a type nanobind does not know (grep of quoted annotations in the stubs): 52, down from 275 before the gap audit — STL iterator overloads, `char32_t`/`wchar_t` hashers, `NCollection_FlatDataMap`/`FlatMap` internals of BRepGraph, members of two skipped classes. (`BVH_Box/Set/Tree<double, 3>` were on this list until R-TEMPLATE-BASE, 2026-09-21.)
- Everything else that is bound is callable.

### Carried forward

1. ~~`handle<T>&` out-parameters~~ — rule added 2026-09-21 (section 6).
2. Coverage is verified on macOS only; Linux/Windows generator runs are open (8).
3. Functor templates stay out; Python callables are not a goal (parked as not planned 2026-09-25).

## 8b. Porting from OCP (cadquery-ocp) to nanocct

For build123d and CadQuery-style code. OCP is pybind11-based and binds OCCT 7.x/8.x with its own conventions; nanocct is 1:1 with OCCT 8.0.1 and documents every deviation in section 6. What changes (evidence: an inventory of build123d's OCP use, 285 OCP names in 84 packages):

| OCP | nanocct | Note |
|---|---|---|
| `from OCP.gp import gp_Pnt` | `from nanocct.gp import gp_Pnt` | package modules are the same; unlike OCP, `import nanocct` loads no toolkit at all and `nanocct.gp` resolves on first attribute access (5.1), so reaching `gp_Pnt` costs two toolkits instead of 45 -- `import nanocct.all` is the opt-in for everything |
| `BRep_Tool.Surface_s(face)` — every static method carries `_s` | the same: every static carries `_s` (R-STATIC-S) | 185 call sites in build123d stay as they are; only functions of a C++ namespace are plain (`TopoDS.Edge`), in OCP too |
| `BRep_Tool.Curve_s(edge, float(), float())` — `double&` kept as dummy inputs, only the handle returned | `curve, first, last = BRep_Tool.Curve_s(edge)` | non-void functions with out-parameters return a tuple, result first (R-OUT) |
| `param_min, _ = BRep_Tool.Range_s(edge)` | `param_min, _ = BRep_Tool.Range_s(edge)` | unchanged |
| `BRepGProp_Face(face).Normal(u, v, pnt, vec)`, `TopExp.Vertices_s(edge, v1, v2)` | the same | class references are mutated in place (R-REF-CLASS) |
| `wires = TopTools_HSequenceOfShape(); ShapeAnalysis_FreeBounds.ConnectEdgesToWires_s(edges, tol, False, wires)` | `wires = ShapeAnalysis_FreeBounds.ConnectEdgesToWires_s(edges, tol, False)` | a `handle<T>&` parameter is returned (R-OUT-HANDLE); the OCP form used the deprecated overload; nanocct binds deprecated members too (with the note), but the handle& parameter becomes the result there as well |
| `OCP.collections.Array1_gp_Pnt`, `List_TopoDS_Shape`, `IndexedMap_TopoDS_Shape_TopTools_ShapeMapHasher` (OCP 8) / `TColgp_Array1OfPnt`, `TopTools_ListOfShape` (OCP 7) | `NCollection_Array1[gp_Pnt]`, `NCollection_List[TopoDS_Shape]`, `NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]` | 6a. **The 7.x typedef names do not resolve**: this is an OCCT 8 binding, so `TColgp_Array1OfPnt` becomes `NCollection_Array1[gp_Pnt]`. A custom hasher is the template's last argument, as in C++: `NCollection_IndexedDataMap[TopoDS_Shape, NCollection_List[TopoDS_Shape], TopTools_ShapeMapHasher]` (measured; leaving it out names a different, unbound instantiation) |
| a container changed while an element reference, an iterator or a numpy view of it is still referenced (`it = List.Iterator(l)` ... `l.Clear()`) | `BufferError` | release the view first (`del it`), or take a numpy view after the OCCT call that fills the array (R-VIEW-GUARD); changing the container under the view read freed memory |
| `from OCP.TopoDS import TopoDS; TopoDS.Vertex_s(shape)` | `import nanocct.TopoDS as TopoDS; TopoDS.Vertex(shape)` | `TopoDS` is a C++ namespace in OCCT 8 = the package module (5.1); a wrong type raises `Standard_TypeMismatch` |
| `TopAbs_FACE`, `GeomAbs_C0`, `Font_FA_Bold`, `Graphic3d_HTA_LEFT` at module level | same (R-ENUM exports unscoped enumerators); `TopAbs_ShapeEnum.TopAbs_FACE` works too | |
| `if handle is None`, `shape.IsNull()` | unchanged | null handle ↔ `None` (R-HANDLE); `None` is accepted wherever a handle is expected |
| `if shape:` / `if not label:` (`__bool__` = `not IsNull()`) | unchanged | R-NULL-BOOL: a null shape or label is falsy; an empty compound is true (it is not null) |
| `except (Standard_Failure, Standard_ConstructionError, StdFail_NotDone)` | `except Standard_Failure` catches all of them | a real hierarchy (4.2); the derived classes still exist |
| `BinTools.Write_s(shape, io.BytesIO())` / `Read_s(shape, io.BytesIO(data))` (pickling) | `data = BinTools.Write_s(shape)` (`bytes`); `BinTools.Read_s(shape, io.BytesIO(data))` | `std::ostream&` → returned `bytes` for the binary packages, `std::istream&` ← `io.BytesIO` (R-STREAM-OUT/IN); byte-identical to the file form (verified) |
| `BRepTools.Write_s(shape, path)`, `Read_s(shape, path, builder)` | the same | the path overloads are untouched |
| `ics.Parameters(i, float(), float(), float())` — dummies for the `double&` of one of two overloads with the same inputs | `u, v, w = ics.Parameters__float__float__float(i)`; `x, y, z = pnt.Coord__float__float__float()` — unlike OCP, where `pnt.Coord()` gives the tuple and the `gp_XYZ` overload is unreachable; in nanocct `pnt.Coord()` is the `gp_XYZ`, as in C++ | R-COLLISION: overloads that differ only in their out-parameters carry a suffix naming those out-parameters' types |
| `while ex.More(): … ex.Next()` | `for s in ex:` works too, at the same speed | R-ITER: `More`/`Next`/`Value` classes are iterable and exhausted afterwards |
| `Geom_BSplineCurve.Poles(array)` (deprecated out-into-array form) | still available, docstring starts with `Deprecated in OCCT: use Poles() returning const reference instead` | R-DEPRECATED |
| `kernel.py`'s workaround for slow `List_TopoDS_Shape` iteration | not needed: `list(NCollection_List[TopoDS_Shape])` measured at 0.2 µs | |
| `TDF_Label`, XCAF, STEP | generated: `nanocct.TDF`, `nanocct.XCAFDoc`, `nanocct.STEPControl` | `STEPControl_Reader.ReadFile(path)`/`TransferRoots()`/`OneShape()` and `STEPControl_Writer.Transfer(shape, STEPControl_AsIs)`/`Write(path)` as in OCP; `WriteStream()` returns `(status, str)` and `ReadStream(name, io.StringIO(text))` takes a text file-like object instead of OCP's stream objects (R-STREAM-OUT/IN) |
| IGES | generated: `nanocct.IGESControl` | `IGESControl_Writer("MM", 1).AddShape/ComputeModel/Write(path)` and `IGESControl_Reader.ReadFile/TransferRoots/OneShape` as in OCP; `Write()` without a path returns `(ok, str)`, but IGES cannot read a stream (2d) |
| `StlAPI_Writer` | generated: `nanocct.StlAPI` | `StlAPI_Writer().Write(shape, path)` as in OCP (4 call sites in CadQuery); `RWStl.WriteBinary_s(mesh)` returns `(ok, bytes)` and `WriteAscii(mesh)` `(ok, str)` |
| VRML | generated: `nanocct.VrmlAPI` | `VrmlAPI.Write_s(shape, file, version)` as in OCP's `VrmlAPI.Write_s`; `Write(shape, version)` without a path returns `(ok, str)`. glTF ✓ (`TKDEGLTF`), OBJ ✓ (`TKDEOBJ`) and PLY ✓ (`TKDEPLY`, export only) are in; `TKBinXCAF`/`TKXmlXCAF` are what is left |

Pickling: nanocct objects are not picklable by themselves (like OCP's); build123d's `copyreg` approach keeps working with the `BinTools` change above. For a transition without changing any code, the OCP compatibility shim (`cadquery-ocp-novtk` 8.0.1.0.0, `make shim`) makes `import OCP.*` work on nanocct and applies every convention in this table automatically; it is explicitly non-1:1 and patches nanocct only when `OCP` is imported.

