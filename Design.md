# nanoOCP design

**nano**bind-based **O**pen **C**ascade for **P**ython

Living document. Every design decision goes here with its rationale and the evidence it rests on; when a decision changes, the entry is updated and the change is logged in the [decision log](#decision-log) at the end. Facts marked *unverified* have not been tested yet.

How to read it:

- Sections 1–2 say what is built and the conventions a *user* must know (2a names, 2b parameters, 2c Python additions, 2d what is not bound and the workaround) — README material.
- Sections 3–5 describe the toolchain, the runtime model and the generator.
- Section 6 is the rule book: every deviation from 1:1, one row per rule with an identifier (`R-…`) that the generator code cites.
- Sections 7–8 cover build, packaging, coverage, the roadmap and the OCP porting table.
- Section 9 is the working state for context resets; the decision log closes the document.

## 1. Goals

- Python bindings for Open CASCADE Technology (OCCT) 8.0.1, generated from the OCCT headers.
- **1:1 with the OCCT API**: same class, method, parameter and enum names, same package structure, OCCT's own `//!` comments as docstrings, so the OCCT reference documentation serves as the nanoOCP documentation. Deviations exist only where Python cannot express a C++ idiom; each one is a documented rule (section 6).
- **nanobind** as the binding library, in **stable-ABI mode** (`abi3`), so one wheel per platform covers all supported CPython versions.
- The generator must be **simple and efficient**: one Python program, libclang for parsing, plain string emission, generated C++ checked into the repository.
- Platforms for the generator and the wheels: macOS (Apple Silicon), Linux (x86_64 and aarch64), Windows.

## 2. Scope

### Phases

- Phase 1: `FoundationClasses`, `ModelingData`, `ModelingAlgorithms`.
- Phase 2 (order decided 2026-09-22): `Visualization` first — `TKService` ✓ and `TKV3d` as **whole toolkits**, because the link graph of the later modules needs them (`TKVCAF`, `TKXCAF`, the mesh writers `TKRWMesh`/`TKDEGLTF`/`TKDEOBJ`/`TKDEPLY`/`TKDEVRML` link `TKV3d` and `TKService`, `EXTERNLIB.cmake`) — then the `ApplicationFramework` subset `DataExchange` links (`TKCDF`, `TKLCAF`, `TKCAF`, `TKVCAF`, `TKBinL`, `TKBin`, `TKXmlL`, `TKXml`), then `DataExchange` (STEP, IGES, STL, VRML, OBJ, glTF, PLY; XCAF and its Bin/Xml drivers).
- After Phase 2: `TKMeshVS` (built) and `TKOpenGl` (needs an OCCT rebuild with `USE_OPENGL=ON`; Linux additionally `USE_XLIB=ON` or EGL, 3.1); nothing in AppFW/DataExchange links either.
- Out: `Draw`; `TKIVtk` (VTK, the user's only exclusion); `TKOpenGles`/`TKD3DHost` (platform variants of the OpenGL driver, not additional API); `TKStdL`/`TKStd`/`TKTObj`/`TKBinTObj`/`TKXmlTObj` (linked only by `TKDECascade`, the `.xbf`/`.cbf` DE plugin) unless that plugin is wanted.

### Visualization: whole toolkits (decision 2026-09-22, replacing the font slice)

`TKService` and `TKV3d` are bound completely — with `USE_OPENGL=OFF` the viewer classes exist without a driver, which is exactly what cadquery-ocp 7.9.3 ships (`OCP/AIS`, `Aspect`, `Graphic3d`, `V3d`, `OpenGl`, … without `IVtk`). Platform headers are handled by `[skip] headers` (`WNT_Dword.hxx` includes `<windows.h>`; `WNT_Window`/`WNT_WClass` guard themselves with `_WIN32`, `WNT_HIDSpaceMouse` is portable and bound). The `[include]` allowlists of 5.2 stay available but are empty. The font slice below is what the scope *was* until 2026-09-22 and remains the part build123d needs:

- toolkit `TKService`: the whole `Font` package (13 headers, `Font_FontMgr`, `Font_SystemFont`, `Font_FontAspect`, `Font_FTFont`, `Font_TextFormatter`, …) and two enum headers of `Graphic3d` (`Graphic3d_HorizontalTextAlignment.hxx`, `Graphic3d_VerticalTextAlignment.hxx`: `Font_FTFont` and `StdPrs_BRepTextBuilder::Perform` take them);
- toolkit `TKV3d`: `StdPrs_BRepFont.hxx` and `StdPrs_BRepTextBuilder.hxx` of `StdPrs` — `Font_BRepFont` and `Font_BRepTextBuilder` are typedefs of these (`Font_BRepFont.hxx:21`);
- not in the slice: `Image_PixMap` (only `Font_FTFont::GlyphImage()` returns it; that member will be reported as unbound), `Aspect`, `Quantity` beyond what TKernel already binds.

This is exactly what build123d imports (`composite.py`: `Font_SystemFont`, `Graphic3d_HTA_*`/`VTA_*`, `StdPrs_BRepFont`, `StdPrs_BRepTextBuilder`, `NCollection_String`); CadQuery additionally uses `Prs3d_IsoAspect` and `Aspect_TOL_SOLID` (`shapes.py:1719`). What the DataExchange headers name from Visualization is small — `Graphic3d_AlphaMode`, `Graphic3d_TypeOfBackfacingModel`, `Graphic3d_TypeOfData`, `Graphic3d_MaterialAspect`, `Graphic3d_Aspects`, `Graphic3d_BndBox3d`, `Graphic3d_Texture2D`, `Image_Texture`, `Image_PixMap` in `XCAFDoc`/`XCAFPrs`/`RWGltf`; `AIS_ColoredShape` in `XCAFPrs_AISObject`; `TPrsStd_Driver` in `XCAFPrs_Driver` — but the link graph requires the toolkits anyway.

### Sizes

`.hxx` headers listed in the packages' `FILES.cmake`, as `generator/occt.py` reads them, `V8_0_1`, 2026-09-21. Files outside `FILES.cmake` are not compiled by OCCT and not bound.

| Module | Headers | Toolkits |
|---|---|---|
| FoundationClasses | 575 | 2 |
| ModelingData | 672 | 4 |
| ModelingAlgorithms | 1 494 | 14 |
| ApplicationFramework | 443 | 13 |
| DataExchange | 2 060 | 14 |
| Visualization | 787 (font slice: 17) | 7 |

## 2a. Naming conventions

Every Python name is the OCCT name. Three generated additions exist because Python cannot express the C++ idiom; they follow one lexical rule:

> **OCCT names contain single underscores (`gp_Pnt`, `Geom_Curve`), so the parts of a generated name are separated by double underscores `__`.**

These conventions are the ones a user must know (they go into the README); everything else in section 6 is a rule about *what* is bound, not about names.

### 1. Static methods that collide with an instance method get `_s` (R-STATIC-S)

- `gp_QuaternionNLerp.Interpolate_s(...)`.
- Every other static method keeps its name (`BRep_Tool.Pnt(vertex)`), unlike OCP, which suffixes all of them.

### 2. Container instantiations: `<template>__<arg1>__<arg2>…` (6a)

- The concrete class: `Handle_X` for `handle<X>`, nested instantiations spelled recursively — `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`.
- The primary spelling is the generic accessor `NCollection_DataMap[TopoDS_Shape, Geom_Surface](...)`, where a Python type stands for the C++ argument: `float` → `double`, `int`, `bool`, `str` → `std::string`, an OCCT class for itself *and* for `handle<class>`.

### 3. Out-parameters become results; colliding overloads get `<method>__<type1>__<type2>…` (R-OUT, R-COLLISION)

- A non-const reference to a primitive, enum or `handle<T>` is dropped from the parameters and returned, after the C++ return value if there is one — `curve, first, last = BRep_Tool.Curve(edge)`.
- Class-typed references (`gp_Pnt&`) stay parameters and are filled in place.
- When two overloads have the same inputs and differ only in those out-parameters, **each overload with out-parameters is named `<method>__<type1>__<type2>…`** with the Python types of its returned out-parameters in order:
    - `u, v, w = ics.Parameters__float__float__float(i)` next to `u1, v1, u2, v2 = ics.Parameters__float__float__float__float(i)`;
    - `x, y, z = pnt.Coord__float__float__float()` while `pnt.Coord()` returns the `gp_XYZ` as in C++;
    - `curve = GeomTools.Read__Geom_Curve(stream)`.
- Types are spelled as in convention 2: `float`, `int`, `bool`, `str` — also for a text stream, `bytes` for a binary one — an enum or class by its Python name, a container by its concrete name.
- The suffix appears only where a collision exists, and after `_s` when both apply.

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
- **Strings:** `const char*`, `char` and `TCollection_AsciiString`/`ExtendedString` parameters all take a `str` (a `char` a one-character one) and behave alike; UTF-16 (`char16_t`) round-trips as `str`.
- **Handles:** every `handle<T>` parameter accepts `None` (the null handle); a returned null handle is `None`.
- **`std::ostream&` / `std::istream&`:**
    - an output stream parameter becomes a returned `str` (`bytes` in the binary packages, `BinTools`);
    - an input stream parameter takes a text (`io.StringIO`, an open file) or binary (`io.BytesIO`) file-like object — never a `str`, so the file-path overloads stay reachable.
- **Optional pointers are dropped** (R-OPTIONAL-PTR): a pointer parameter with a null default (`bool* theIsStored = nullptr` in `BRep_Tool::CurveOnSurface`, `unsigned* theErrorCode = 0` in `BRepFill_AdvancedEvolved::IsDone`, `Standard_OStream* = nullptr` in `BRepBuilderAPI_FastSewing::GetStatuses`) is not in the Python signature; the callee always gets the null pointer.
- **Fixed-size arrays are sequences** (R-FIXED-ARRAY): `const int (&theNodes)[3]` takes any sequence of 3 ints; a non-const `gp_Pnt theP[8]` is an out-parameter returned as a list of 8 (`ok, corners = obb.GetVertex()`); a `double myPeriod[3]` member is a list property.
- **Pointer results** (R-RESULT, R-PTR-REF): a returned `T*` (also `T*&`) is the object itself, referencing the owner (`fuse.Builder()`, `builder.PDS()`); a returned `Transient*` is a handle.

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

- **Operators** (R-OPERATOR, R-IOP, R-FREE-OP):
    - C++ operators become the Python dunders (`__add__`, `__eq__`, `__call__`, `__getitem__`, `__neg__`, …)
    - OCCT's `void operator+=` becomes `__iadd__` returning `self`
    - a free `operator*(double, gp_Vec)` becomes `__rmul__`

- **Conversions** (R-CONV, R-CONV-SCALAR, R-IMPLICIT-CONV):
    - `operator bool/int/double()` → `__bool__`/`__int__`/`__float__`
    - `operator T()` → a constructor `T(aFrom)` on the target plus an implicit conversion unless `explicit` (`TopoDS_Shape(aMakeShape)`)
    - non-`explicit` converting constructors convert implicitly as in C++ (`OSD_Path("/x")`)
    - an implicit copy constructor is bound where C++ has one (`TopoDS_Shape(aVertex)` upcasts, R-IMPLICIT-COPY)

- **`__hash__`** only where OCCT specialises `std::hash<T>` (`TopoDS_Shape`, `gp_Pnt`, `TopLoc_Location`, …), so value-equal shapes are one dict key; every other class keeps identity hashing (R-HASH).

- **Enums** (R-ENUM): unscoped enumerators are attributes of the enclosing module/class as in C++ (`TopAbs.TopAbs_FACE`), `int(e)` works; `enum class` stays nested.

- **Exceptions** (4.2): `Standard_Failure` and its descendants are Python exception classes with the C++ hierarchy, all deriving from `RuntimeError`; they can be raised from Python.

- **Iteration over OCCT iterators** (R-ITER):
    - every class with `More() -> bool`, `Next()` and a parameterless `Value()` or `Current()` gets `__iter__`/`__next__`, yielding `Value()`/`Current()` while `More()` — `for e in TopExp_Explorer(shape, TopAbs_EDGE):`
    - the object is its own iterator, so it is exhausted afterwards like a file
    - the C++ range-for support (`begin()`/`end()`, `operator++`, `NCollection_ForwardRangeIterator`) stays out (R-ITERATOR)

- **Docstrings**: OCCT's `//!` comments; a deprecated member's first line is `Deprecated in OCCT: <message>` (R-DEPRECATED), a suffixed overload's first line names its C++ signature (R-COLLISION).

## 2d. What is not bound, and the workaround

Members that nanoOCP cannot bind and that a user might look for, with the OCCT-level alternative. The complete list of omissions is `src/cpp/<TK>/report.txt` per toolkit (categories in 8a); everything internal to an algorithm is left out of this table on purpose. **Maintained per toolkit: every new toolkit's report is checked for user-facing omissions and this table extended (§9 development loop).**

| Not bound | Why | Use instead |
|---|---|---|
| `gp_XYZ::GetData()/ChangeData()`, `NCollection_Vec2/3/4::GetData()`, `operator T*` | raw pointer into the object | `Coord()`, `X()/Y()/Z()`, `x()/y()/z()`, `SetCoord()` |
| `BinTools::GetReal/GetInteger/…(istream&, …)`, `BinTools_IStream`/`BinTools_OStream`, `BinTools_CurveSet::ReadCurve(istream&)` | stream-holding objects and `istream&` results | `BinTools.Write(shape) -> bytes`, `BinTools.Read(shape, io.BytesIO(data))` (8b); `BinTools_ShapeSet` for the shape-set level |
| `BRepMesh_IncrementalMesh::Discret(shape, deflection, angle, BRepMesh_DiscretRoot*&)` | reference to a pointer parameter | `BRepMesh_DiscretAlgoFactory.DefaultFactory().CreateAlgorithm(shape, deflection, angle)` or the `BRepMesh_IncrementalMesh` constructor |
| `TCollection_AsciiString(const wchar_t*)`, `ExtendedString::ToUTF8CString(char*&)`, `AsciiString::Cat(const wchar_t*)` | wide-char pointers | the `str` constructors and `ToCString()`/`ToExtString()` (UTF-16 round-trips as `str`) |
| `TCollection_*::Move(&&)`, `TCollection_H*String(&&)` | rvalue references | copy (`TCollection_AsciiString(other)`) |
| `Standard_Failure::Raise(fmt, ...)` | variadic | `raise Standard_Failure("message")` |
| `Standard::Allocate/Free`, atomics, hash functions | raw memory | not needed from Python |
| `Adaptor3d_TopolTool::Edge()`, `BRepPrimAPI_MakeOneAxis::OneAxis()` | `void*` (`Standard_Address`) results | `BRepTopAdaptor_TopolTool::Edge()` is the same pointer; `MakeOneAxis` results come from `Shape()`/`Face()`/`Shell()`/`Solid()` |
| `BRepBuilderAPI_FastSewing::GetStatuses(ostream*)` | the stream is optional | `GetStatuses()` returns the status flags; the text dump is not available |
| `IMeshData_Edge/Face/Wire` members of the second base `IMeshData_StatusOwner` (`GetStatus`, `SetStatus`) | nanobind single inheritance (R-MI) | mesh-algorithm internals; `BRepMesh_IncrementalMesh.GetStatusFlags()` is the user-level status |
| `XBRepMesh_Factory()` (constructing a second one) | undefined behaviour in OCCT itself (9) | `BRepMesh_DiscretAlgoFactory.FindFactory("XBRepMesh")` |
| `BVH_Set` members of `BVH_PrimitiveSet<double, 3>` not overridden by the derived class (`Center(i)`, `Swap(i, j)`; `Size()`/`Box()` are overridden and bound) | second base (R-MI) | not needed by `BRepExtrema_ShapeProximity`; the BVH tree is built inside OCCT |
| `BVH_Box3d.Transform(mat4)` / `Transformed(mat4)` | live in a partial specialisation of the dropped CRTP base `BVH_BaseBox` (R-TEMPLATE-BASE) | `Bnd_Box.Transformed(gp_Trsf)` for axis-aligned boxes; `BVH_Box3d.Add(point)` after transforming the corners |
| `BOPTools_Box2dPairSelector` | OCCT bug: the 2D instantiation does not compile (`overrides.toml`) | the 3D `BOPTools_BoxPairSelector`; 2D pairs through `Bnd_Box2d` |
| `ShapeProcess::Perform(context, std::bitset)`, `ShapeProcess_UOperator(function pointer)` | `std::bitset`, C function pointer | `ShapeProcessAPI_ApplySequence`, `ShapeProcess.Perform(context, sequence)` |
| `MathUtils::Polynomial/Rational(std::initializer_list)` | initializer lists | the `NCollection_Array1[float]` constructors |
| functor-template algorithms (`MathOpt::BFGS<F>`, `MathRoot::Newton<F>`, …) | need a C++ functor type (8.5) | the classic `math_BFGS`, `math_FunctionRoot`, … |
| `Image_PixMap::Data()/ChangeData()/Row()/RawValue*()`, `Image_PixMapData::Value*()`, `Image_PixMap::InitWrapper()`, `Graphic3d_Buffer::Data()/AttributeData()/value()`, `Graphic3d_BoundBuffer::Bounds`, `Graphic3d_HatchStyle::Pattern()` | raw pointers into pixel/vertex buffers (8a: byte buffers, revisited with DataExchange) | `Image_PixMap.PixelColor(x, y)`/`SetPixelColor` per pixel, `InitZero`/`InitCopy`; `Graphic3d_ArrayOfPrimitives.AddVertex`/`Vertice(i)`/`Attribute*`; the `Graphic3d_HatchStyle(NCollection_HArray1[int])` constructor |
| `Image_AlienPixMap.Load(path)` (returns `False`), `Save(path)` writes **PPM** whatever the extension; `Image_AlienPixMap::Load/Save(uint8_t*, …)` | the local OCCT is built without FreeImage (`USE_FREEIMAGE=OFF`, 3.1): no PNG/JPEG codecs; the buffer overloads are raw pointers | `Save` for PPM; decide on FreeImage before `TKOpenGl`/`V3d_View::Dump` (8) |
| `Media_*` (`Media_CodecContext::Init(const AVStream&)`, `Media_FormatContext::Stream()`, `Media_Frame::Frame()`, `Media_Packet`, `Graphic3d_MediaTextureSet`'s second base `Media_IFrameQueue`) | FFmpeg types without headers (`USE_FFMPEG=OFF`, R-PTR-INCOMPLETE); OCCT compiles the package as stubs | video textures are not available in this build |
| `Xw_Window::ProcessMessage(listener, XEvent&)`, `Xw_Window::NativeFBConfig()`, `Aspect_DisplayConnection::Init/GetDisplayAspect/GetDefaultVisualInfo/…`, `Wasm_Window::Process*Event(listener, Emscripten*Event*)` | X11/Emscripten types without headers, raw pointers | Linux/WebAssembly window plumbing; revisit with `TKOpenGl` and the Linux build (`USE_XLIB`) |
| `Cocoa_Window(NSView*)`, `Cocoa_Window::HView()/SetHView()`, `Aspect_Window::NativeFBConfig()`, `Aspect_NeutralWindow::SetNativeHandles(Aspect_Drawable, …)`, `Graphic3d_CView::SetWindow(…, Aspect_RenderingContext)` | native window handles (`void*`) | embedding a viewer needs `TKOpenGl` first (roadmap); a Python window integration is a subsystem of its own |
| `Graphic3d_TransformUtils::Project/UnProject/Ortho/Rotate/Scale/Translate/Convert/…<T>`, `Graphic3d_TransformPers::Apply/Compute<T>`, `Graphic3d_Flipper::Apply/Compute<T>`, `NCollection_Mat3/Mat4::ConvertFrom<Other>` | function templates on the scalar type (R-TEMPLATE-SKIP) | `gp_Trsf`/`gp_GTrsf` for geometry; `NCollection_Mat4[float]`'s own methods (`Multiply`, `Inverted`, `Transposed`, `SetColumn`…) for view matrices |
| `Graphic3d_Structure::Owner()/SetOwner(Standard_Address)`, `Graphic3d_GraduatedTrihedron::SetCubicAxesCallback`, `Graphic3d_MediaTextureSet::SetCallback`, `Font_FTLibrary::Instance()` (`FT_Library`), `Font_FTFont::renderGlyphOutline` | `void*` owner, C function pointers, FreeType handle | driver internals; `Font_FTFont` renders through `RenderGlyph`/`GlyphImage` (the latter returns `Image_PixMap`) |
| `NCollection_Map<Graphic3d_Structure*>`, `NCollection_IndexedMap<Graphic3d_CView*>`, `NCollection_IndexedMap<const Graphic3d_CStructure*>` | container instantiations over raw pointers (6a) | `Graphic3d_StructureManager` methods (`DisplayedStructures`, `DefinedViews`) return them; the structure/view sets are driver internals |
| `operator\|(Graphic3d_TransModeFlags, Graphic3d_TransModeFlags)` | free operator on an integer typedef | Python `int \| int` |

## 3. Toolchain and third-party dependencies

### 3.1 OCCT

- Built locally from the `V8_0_1` tag: sources extracted with `git archive` from a checkout into `deps/occt-src` (the exact tag, not a working tree).
- Script `deps/build-occt.sh`; install prefix `deps/occt-8.0.1`.
- **No conda/micromamba anywhere.** The user's OCP build scripts in `~/Development/CAD/ocp-build-system/local-build/` are a reference for the CMake options only.

Configuration:

| Option | Value | Why |
|---|---|---|
| compiler | Apple clang (`/usr/bin/clang++`), system libc++ | Wheels must not depend on a conda/Homebrew C++ runtime. The previous `/opt/local/occt-8_0_1-novtk` install was built inside micromamba and links `@rpath/libc++.1.dylib` without an `LC_RPATH`, which makes extension modules fail to load. |
| `BUILD_CPP_STANDARD` | C++17 | OCCT default. |
| `CMAKE_BUILD_TYPE`, `BUILD_OPT_PROFILE` | Release, Production (`-O3 -flto`) | Same as the OCP build scripts. |
| `BUILD_RELEASE_DISABLE_EXCEPTIONS` | **OFF** | OCCT must throw `Standard_Failure` in release builds so Python sees exceptions. |
| `CMAKE_OSX_DEPLOYMENT_TARGET` | 11.1 | Wheel platform tag `macosx_11_0_arm64`, same as OCP. |
| `BUILD_MODULE_Draw`, `USE_VTK`, `USE_TBB`, `USE_TK`, `USE_XLIB`, `USE_OPENGL`, `USE_GLES2`, `USE_FFMPEG` | OFF | Not needed in scope. |
| `USE_FREETYPE` | ON, static build from `deps/build-freetype.sh` | Required by the font slice (`Font_FTFont.cxx` is entirely `#ifdef HAVE_FREETYPE`). |
| `USE_RAPIDJSON` | ON (header-only, currently from Homebrew) | glTF reader/writer (`TKDEGLTF`). To be vendored. |
| `USE_FREEIMAGE`, `USE_FFMPEG`, `USE_DRACO`, `USE_XLIB`, `USE_GLES2`, `USE_D3D` | OFF | Consequences (verified 2026-09-22): `Image_AlienPixMap` has no codecs — `Save` writes PPM regardless of the extension, `Load` fails; the `Media` package is stubs; glTF has no Draco decompression (`libTKDEGLTF` links no external library); on Linux no X11 window. FreeImage is the one to decide before `TKOpenGl`/`V3d_View::Dump` (8). |

### 3.2 Third-party policy: no vcpkg (for now)

- The compiled third-party surface for the whole scope is one library, **FreeType**.
- FreeType 2.14.3 (sha256 verified against the Homebrew formula) builds in 2 s with its own CMake and `FT_DISABLE_ZLIB/BZIP2/PNG/HARFBUZZ/BROTLI=TRUE` into a static archive that links against nothing but libSystem (verified with a link test loading Helvetica).
- It is linked into `libTKService` (149 exported `FT_*` symbols; `otool -L libTKService.dylib` shows only libSystem/libobjc/libc++).
- vcpkg would replace that one step with a bootstrap and a triplet per platform, and builds FreeType with the optional dependencies enabled by default. Revisit if the list grows (Draco, TBB, FreeImage); OCCT 8.0.1 has native `BUILD_USE_VCPKG` support.
- Linux additionally needs **fontconfig** (used unconditionally under `HAVE_FREETYPE` in `Font_FontMgr.cxx:86,708`): system package in the manylinux image, bundled by auditwheel. Accepted by the user.
- Windows enumerates fonts via the registry (*unverified*).

### 3.3 Python side

- Python ≥ 3.12, `uv` project.
- nanobind ≥ 3.1.0 (the `handle<T>` caster uses `nb::keep_alive_cb`, public since 3.1.0).
- scikit-build-core; pip `libclang` (fallback parser, see 5.2); pytest.

## 4. Runtime model

### 4.1 Stable ABI

- `nanobind_add_module(... STABLE_ABI NB_DOMAIN nanoocp ...)` in linked mode: `Py_LIMITED_API=0x030C0000`, module file `*.abi3.so`, floor Python 3.12.
- nanobind's split mode (backend module, floor 3.10) was rejected: it adds a runtime dependency on `nanobind-backend` for two extra Python versions.
- **Gotcha (verified):** nanobind silently drops `STABLE_ABI` unless `find_package(Python ... Development.SABIModule)` is requested; the first PoC produced `cpython-314-darwin.so` because of this.

### 4.2 Three kinds of C++ types

#### Value types (`gp_*`, `TopoDS_Shape`, `Bnd_Box`, …)

- Plain `nb::class_<T>` with `nb::init<...>`.
- References returned by OCCT are copied (nanobind's default policy for lvalue references).

#### `Standard_Transient` descendants

- `nb::class_<T, Base>` plus a type caster for `opencascade::handle<T>` (alias `occ::handle<T>`, `Standard_Handle.hxx:419`) in `src/cpp/common/nanoocp_common.h`, modeled on nanobind's `shared_ptr` caster.
- The Python instance never owns the C++ object; a heap-allocated `handle<Standard_Transient>` is attached with `nb::keep_alive_cb`, so OCCT's intrusive reference count governs lifetime on both sides.
- Constructors are `nb::new_` lambdas returning `handle<T>` so that Python-created objects go through the same path.
- Verified in `poc/test_poc.py`: refcount 1 after construction, 2 after C++ stores the handle, object survives Python GC, comes back as its most-derived type, `load() is back` (nanobind instance map), `None` ↔ null handle.
- A `handle<T>` *parameter* must be declared `nb::arg("x").none()` or nanobind rejects `None` before the caster runs (verified). The generator emits `.none()` for every parameter whose type is `handle<T>` (by value or reference; `Param.is_handle`), so `BRep_TFace().Surface(None)` and `BRep_Builder().UpdateEdge(E, None, L, tol)` pass a null handle (tests, 2026-09-21); the stubs then spell such parameters `T | None`. The review of 2026-09-20 found this rule documented but not emitted — 0 of 96 generated files had `.none()`.

#### `Standard_Failure` descendants

- Python exception classes created with `PyErr_NewExceptionWithDoc` (stable ABI), mirroring the C++ hierarchy (`Standard_OutOfRange → Standard_RangeError → Standard_DomainError → Standard_Failure → RuntimeError`).
- `Standard_Failure` itself derives from `std::exception` in OCCT 8 and provides `what()`.
- Translation C++ → Python does **not** use `nb::exception<T>` (catch by derived type): the `DEFINE_STANDARD_EXCEPTION` classes are header-only, so their `typeinfo` is duplicated per shared object and a `catch (Derived&)` in the extension module does not match an object thrown inside `libTKMath` (verified: `Standard_ConstructionError` arrived as `Standard_Failure`).
- Instead every toolkit module registers one translator that catches `Standard_Failure&` and dispatches on `typeid(e).name()` through a per-module map; unknown names are rethrown to the next module's translator (nanobind tries the newest first) and the TKernel translator falls back to `Standard_Failure`.
- Exceptions can also be raised from Python and caught by their bases.

#### Returned pointers and references

nanobind's default for a returned raw pointer is *take ownership*, which would `delete` an OCCT object that is still reference-counted (`Standard_Transient::This()` returns `Standard_Transient*`). Rules:

- a pointer or reference to a `Standard_Transient` descendant is wrapped into a `handle<T>` in a lambda (`t.This() is t` holds);
- a pointer to any other class gets `rv_policy::reference`;
- a *mutable* reference to a class (`ChangeXxx()` accessors) gets `rv_policy::reference_internal` so in-place edits reach the owner;
- const references and values are copied (nanobind default).

#### Multiple inheritance (verified 2026-09-20)

- nanobind supports one base and reuses the derived pointer as the base pointer without adjustment: a bound base must be at **offset 0** of the derived object.
- Measured: `NCollection_HArray1<T>` (`: Array1<T>, Standard_Transient`) bound with base `Standard_Transient` returned `myLowerBound` from `GetRefCount()` (5 for an array starting at 5), and `NCollection_Shared<T>` (`: Standard_Transient, T`) bound with base `T` crashed on the first `T` method.
- Rule for a class `S` with several bases:
    - nanobind's base is the offset-0 one (`mi_traits<S>::base` in `nanoocp_common.h`, declared for the NCollection H-types and `Shared` via forward declarations so every TU agrees);
    - members of the other base are bound with lambdas taking `base&` and `static_cast`ing to `S&` (an adjusting downcast);
    - an **MI registry** (`nanoocp_register_mi<S>`) gives the `handle<T>` caster two conversions: Python `S` → `handle<Standard_Transient>` (`to_transient` on the stored pointer, then `dynamic_cast<T*>`, so a wrong target type fails cleanly) and `handle<Standard_Transient>` holding an `S` → the stored pointer (`dynamic_cast<void*>` to the complete object, then to the base).
- Verified: `HArray1(5, 9).GetRefCount() == 1`; a `Sequence<handle<Standard_Transient>>` round-trips an `HArray1` and a `Shared<Map<int>>` by identity with exact reference counts; `isinstance(h, NCollection_Array1[T])` is `True`, `isinstance(h, Standard_Transient)` is `False` (documented).
- Generated OCCT classes with several bases get their first base only; the others are reported (rule in section 6, `IMeshData_Edge`).

#### Construction

- nanobind constructs value types with placement new, which needs either no class-level `operator new` or a public `operator new(size_t, void*)` (`DEFINE_STANDARD_ALLOC` provides one; `DEFINE_NCOLLECTION_ALLOC` does not).
- Classes failing this, classes with a non-public base (`Message_LazyProgressScope : protected Message_ProgressScope`, whose inherited `operator new` is inaccessible even to C++) and abstract classes get no constructors; the report says so.
- nanobind also instantiates `wrap_copy`/`wrap_move` (placement new) for every *non-trivially* copy/move-constructible class, so a class whose class-level `operator new` hides the placement form (`DEFINE_NCOLLECTION_ALLOC`/`DEFINE_INC_ALLOC`) **cannot be bound at all** unless it is trivially copyable (`Poly_CoherentTriPtr`: pointer fields only) or not copyable (`NCollection_ListNode`: deleted copy): the five `BRepMeshData_*` implementation classes are skipped and reported (verified with a compile test 2026-09-21).
- A class with only non-public constructors gets no implicit default constructor either (`Standard_Type`).
- Among `nb::new_` overloads the zero-argument one must be registered first (nanobind requirement) — constructors are sorted by required-parameter count.

## 5. Package layout and generator

### 5.1 Modules and names

- **One extension module per OCCT toolkit**: `nanoocp._TKMath`, `nanoocp._TKernel`, …
    - mirrors OCCT's link graph; parallel compilation; all share `NB_DOMAIN nanoocp` so types cross module boundaries;
    - each toolkit module first imports the toolkit modules it links against (from `EXTERNLIB.cmake`), so base classes and parameter types are registered before use.
- **One Python module per OCCT package**: `nanoocp.gp.gp_Pnt`, `nanoocp.Geom.Geom_CartesianPoint`.
    - Implementation: the toolkit module creates a submodule per package, sets its `__name__` to `nanoocp.<pkg>` (so `gp_Pnt.__module__ == "nanoocp.gp"`), registers it in `sys.modules["nanoocp._<TK>.<pkg>"]`, and a generated shim `src/nanoocp/<pkg>.py` does `from nanoocp._<TK>.<pkg> import *`.
- **C++ namespaces** (OCCT 8 uses them in the math packages and in ModelingData: `MathUtils`, `Geom2dGridEval`, `TopoDS`, `Geom2dEval_RepCurveDesc`, `BRepGraphInc`):
    - a namespace named like its package **is** the package module (`MathUtils::DepressCubic` → `nanoocp.MathUtils.DepressCubic`, `Geom2dGridEval::CurveD1` → `nanoocp.Geom2dGridEval.CurveD1`, `TopoDS::Vertex` → `nanoocp.TopoDS.Vertex`);
    - every other namespace becomes a **submodule** (`Geom2dEval_RepCurveDesc::Base` → `nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base`, nested namespaces nest);
    - implementation: `def_submodule` in the declare phase, registered in `sys.modules["nanoocp._<TK>.<pkg>.<ns>"]`; the shim of such a package is a Python package `src/nanoocp/<pkg>/__init__.py` with one module per namespace (`<pkg>/<ns>.py`), so `from nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc import Base` works and the stubs follow the same layout (`<pkg>/__init__.pyi`, `<pkg>/<ns>.pyi`);
    - nanobind also registers a submodule under `<parent __name__>.<ns>` = `nanoocp.<pkg>.<ns>`; that key is popped again, otherwise `import nanoocp.<pkg>.<ns>` would find the extension object without importing the package shim (observed as `cannot import name 'Geom2dEval' from 'nanoocp'`);
    - namespaces in `overrides.toml [skip] namespaces` (`std`, `detail`, `Detail`, `Internal`) are not bound; anonymous namespaces are reported.
- **Nested classes** (`Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`, `Geom2dAdaptor_Curve::BezierData`, also when defined out of class: `class BRepGraph::ShapesView { … }`):
    - bound into their outer class (`nanoocp.Geom2d.Geom2d_Curve.ResD1`, `__qualname__ == "Geom2d_Curve.ResD1"`), after it, and skipped when the outer class is;
    - the manifest keys are the C++ names (`Geom2d_Curve::ResD1`), and `parse.py_path(name, package, paths)` gives the Python attribute path used by the `NCollection_Xxx[T]` accessor tables, the stubs and cross-package lookups;
    - the name alone cannot tell a *class* named like its package from the package-named namespace (`BRepGraph::ShapesView` must stay `BRepGraph.ShapesView`), nor an alias name of an instantiation: `manifest.json` `paths` records those, computed from the AST.
- **Two registration phases per toolkit**: **declare** all classes and enums of all packages, then **define** members.
    - Reason: nanobind converts default-argument values to Python objects at `.def` time, so every type used in a default must already exist.
    - Packages are declared in base-class dependency order (`FSD_BinaryFile : Storage_BaseDriver` needs `Storage` before `FSD`; computed from the IR, cycles would be reported), classes within a package likewise.
- **Cross-package lookups at registration time** (exception bases) go through the extension submodule `nanoocp._<TK>.<pkg>`, never through the `nanoocp.<pkg>` shim: importing the shim while the toolkit module is still initialising freezes a half-filled namespace (observed: `nanoocp.Standard` with 42 of 120 names).

### 5.2 Generator architecture

`generator/` is a Python package, run as `python -m generator --toolkit TKMath [--package gp]`.

#### Files

- `occt.py`: reads OCCT's own `TOOLKITS.cmake`, `PACKAGES.cmake`, `FILES.cmake`, `EXTERNLIB.cmake` for the module → toolkit → package → header tree and toolkit dependencies. No hand-maintained lists.
- `parse.py`: **libclang AST** (`clang.cindex`), one translation unit per package (an umbrella header including all package headers). Builds the IR in `model.py`.
    - Function bodies are parsed, because the `nm` check for declared-but-undefined methods needs to see out-of-class inline definitions (`get_definition()`).
    - It uses the **system libclang that pairs with the `clang` on `PATH`** (located from `clang -print-resource-dir`) and falls back to the pip `libclang` wheel. Reason: the pip wheel is stuck at clang 18 and cannot parse the libc++ of the current Apple SDK (`__builtin_clzg`); the pip wheel also ships no builtin headers, so `-resource-dir` must be passed explicitly. Cross-platform behaviour of this selection is *unverified* (macOS only so far).
- `binders.py`: the data-only `BINDERS` table of the NCollection binder kinds (6a) — separate from `ncollection.py` (docstring extraction, coverage check, deprecated aliases; needs libclang) so that `parse.py`, `stubs.py` and `__main__.py` import it at top level without a cycle.
- `emit.py`: IR → C++ with plain f-strings, no template engine. The `#include` list is the package headers (prelude first) plus the header of every identifier the emitted code mentions **and of every class behind a typedef in a signature** (`IMeshData::IFaceHandle` = `handle<IMeshData_Face>`, whose header nothing else pulls in), checked by `parse.include_prelude` (R-PRELUDE). `Emitter.emit()` is one method per phase (`_functions`, `_declare_class`, `_define_class`, `_conversions`, `_aliases`, `_includes`); `resolve_overload_collisions()` is a pure function on the IR (unit-tested).
- `report.py`: categories for the report lines and the `report.txt` writer/reader (5.3).
- `model.py`: the IR; `ResultKind`, `StreamKind`, `ConversionKind` are `StrEnum`s. The 6c substitution state is one `Substitution` object in `parse.py` (`_SUBST`), set up and cleared by `_instantiate_template`.
- `symbols.py`: the `nm` symbol list of a toolkit library for R-UNDEFINED (6).
- `src/cpp/manifest.json`: classes bound by earlier runs, so a class whose base lives in a not-yet-generated package is skipped with a report line instead of aborting at import (`nb_type_new: base type not known`).
    - A class skipped that way — or because its own base was skipped just before (`IntPatch_PolyhedronBVH : BVH_PrimitiveSet<double, 3>`, whose base `BVH_Object<double, 3>` is unbound) — is removed from the manifest again, so neither a later package nor a later toolkit derives from a class that does not exist (until 2026-09-21 such classes leaked into the manifest: `BVH_Box<double, 3>`, `OSD_StreamBuffer<…>`, `Standard_ArrayStreamBuffer`; harmless only because nothing derived from them).
    - Its nested classes and **nested enums** go with it (`BRepExtrema_ProximityDistTool::ProxPnt_Status`, `IntPatch_BVHTraversal::TrianglePair`): they leave the manifest and the `NCollection_Xxx[T]` accessor table, a typedef of them is reported instead of aliased (R-ALIAS), and an NCollection instantiation over them is skipped and reported (`NCollection_DynamicArray<…ProxPnt_Status>`). Until 2026-09-21 the nested enum stayed in the manifest: the alias aborted the import of `TKTopAlgo` (`no attribute 'BRepExtrema_ProximityDistTool'`) and the accessor entry would have broken `NCollection_DynamicArray[T]` for every `T` (`Template._resolve` resolves all entries at once). Members whose signature still names such a type stay bound and uncallable (8a, usability).

#### `overrides.toml` — the only hand-maintained input

Each entry is a documented deviation with a one-line reason. Sections:

- `inout`: the four `Transforms` methods whose `double&` parameters are in/out, `*::InitFromJson` for every class, `Font_FontMgr::FindFont` (`Font_FontAspect&`: the aspect looked for, replaced when an alias maps to another style — `Font_FontMgr.cxx:1060`), and the methods that read and replace a `handle<T>&` — `GeomLib::ExtendCurveToPoint` and five more, `*::ReadCompleteInfo`. OCCT's `@param[in][out]` markers are too sparse to derive the list (`gp_Trsf::Transforms` has none; 2026-09-22 survey: every marked non-const primitive/enum reference in the bound headers is either in the list, a protected member or an unbound function template).
- `skip.classes`: internal helpers such as `Standard_Static_Assert<true>`.
- `skip.noncopyable`: `math_GlobOptMin`, bound through a wrapper with deleted copy/move.
- `skip.headers`: platform-specific internals OCCT only includes under `#ifdef`, e.g. `OSD_WNT.hxx`.
- `skip.methods`: members of a 6c instantiation whose template *body* does not compile for the argument — `IntPolyh_Array<IntPolyh_Edge>::Dump` calls `Edge::Dump()` which takes an `int`. Declared-but-undefined members need no entry since the `nm` check compares mangled names per overload (R-UNDEFINED).
- `skip.namespaces`: `std` (only `std::hash` specialisations); `detail`/`Detail`/`Internal` (header-only implementation helpers).
- `instantiate.extra`: container instantiations to bind although no signature uses them (6a).
- `include.packages` / `include.headers`: allowlists for a partial toolkit/package — the font slice; names are validated against `PACKAGES.cmake`/`FILES.cmake`, the other headers are reported.
- `stream.binary_packages`: packages whose streams carry a binary format (R-STREAM-OUT/IN).

#### Principles

- Regular expressions are used only for CMake list files, for recognising `std::basic_ostream`-like canonical types, and for tokenising type spellings into identifiers to collect `#include`s — never to parse C++.
- Type spellings are emitted **as written in the header** (e.g. `Standard_Size`, `size_t`) so the generated C++ is portable; the *canonical* type is used only for analysis (out-param detection, unsupported types).
    - Exceptions: types nested in a class are spelled fully qualified (`gp_Dir::D`), because inside the class the header says just `D`; likewise non-template classes and enums declared in an OCCT namespace (`Geom2dEval_RepCurveDesc::Base`, written `Base` inside the namespace).

### 5.3 Output

- Per toolkit: `src/cpp/<TK>/<pkg>.cpp` (one per package, `nanoocp_declare_<pkg>` + `nanoocp_define_<pkg>`), `src/cpp/<TK>/_<TK>.cpp` (module init), `src/cpp/<TK>/report.txt`, `src/nanoocp/<pkg>.py`, `src/cpp/toolkits.cmake`.
- Generated files are checked in; users never need libclang.
- **The report**: every run prints everything not bound and why and, for a full toolkit run, writes it to `report.txt`.
    - One line per omission: `category<TAB>package<TAB>what: why`; categories assigned from the message text by the table in `generator/report.py` (a message no pattern knows lands in `misc`, currently empty; tests assert that).
    - The file is the coverage instrument: a regeneration that loses a member shows up as a `git diff` of `report.txt`, and `tests/test_TKBRep.py::test_unbindable_classes_are_reported_not_bound` reads it.

## 6. Binding rules (1:1 and the documented deviations)

Rows carry an identifier (`R-OUT`, `R-STREAM-OUT`, …) that the code cites in a comment at the rule's sites: `grep -rn R-COLLISION generator/` finds the implementation of a row, and a comment in the generator points back here. The rows are grouped by theme; 2a–2c summarise the user-facing ones.

#### 6.1 The 1:1 baseline

| C++ idiom | Python | Rule |
|---|---|---|
| method, constructor, static method, public field, enum | same name | 1:1; overloads are chained `.def`s, resolved by nanobind |
| `//!` comments | docstrings | class and member docs come from `raw_comment` |

#### 6.2 Names

What a member, class or enumerator is called in Python (the user-facing summary is 2a).

| C++ idiom | Python | Rule |
|---|---|---|
| **R-STATIC-S** static and instance method with the same name | static gets suffix `_s` (`gp_QuaternionNLerp.Interpolate_s`) | Python cannot overload across static/instance. OCP suffixes *every* static method (`BRep_Tool.Pnt_s`); nanoOCP only the colliding ones (`BRep_Tool.Pnt`), 28 in FoundationClasses/ModelingData (report category `static-rename`) |
| **R-KEYWORD** C++ identifier that is a Python keyword (`GProp_PEquation::Type::None`) | trailing underscore (`None_`) | PEP 8 / pybind11 convention; applies to enumerators, methods, fields, functions |
| **R-TEMPLATE-NAME** explicit template specialisation without an OCCT typedef (`NCollection_Lerp<gp_Trsf>`) | `NCollection_Lerp__gp_Trsf` | the 6a naming: `<` and `,` → `__`, `>` dropped |
| **R-ALIAS** `typedef`/`using` of a bound class, at package level or in a namespace (`using CurveD1 = Geom_Curve::ResD1` in `namespace GeomGridEval`; the deprecated `using GCE2d_MakeSegment = GC_MakeSegment2d`) | attribute alias (`nanoocp.GeomGridEval.CurveD1 is nanoocp.Geom.Geom_Curve.ResD1`); the stub says `CurveD1 = nanoocp.Geom.Geom_Curve.ResD1` (stubgen writes `from nanoocp.Geom import ResD1 as CurveD1`, which is wrong for nested classes and, per the typing spec, not a re-export — ty enforces that; fixed in `generator/stubs.py`) | scalar typedefs (`Standard_Real`) and aliases of unbound types are not exposed (reported when in a namespace, and at package level when the target is a skipped class or a member of one: `ProxPnt_Status = BRepExtrema_ProximityDistTool::ProxPnt_Status`, `BVH_PrimitiveSet3d`, `OSD_IStreamBuffer`, 5.2); deprecated class aliases are kept (they are how 7.x code and docs resolve) |
| **R-NAMESPACE** `constexpr` constants, functions, classes, enums in a namespace (`MathUtils::THE_NEWTON_MAX_ITER`, `MathLin::LeastSquares`, `Geom2dGridEval::CurveD1`, `Geom2dEval_RepCurveDesc::Base`) | attributes of the package module when the namespace is named like the package, else of the submodule `nanoocp.<pkg>.<ns>` (5.1) | OCCT 8 uses namespaces as packages-within-packages |
| **R-NESTED** public nested class/struct (`Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`) | attribute of the outer class, fields/methods 1:1 | OCCT 8 result structs (`EvalD1() -> ResD1`), also inside `std::optional`/`NCollection_Array1<…>`; non-public nested classes stay out |
| **R-ENUM** unscoped enum | `nb::enum_` with `is_arithmetic` (`int(e)` works); the enumerators are also **exported into the enclosing scope** (`.export_values()`: `nanoocp.TopAbs.TopAbs_FACE is TopAbs_ShapeEnum.TopAbs_FACE`, `TopoDS_TShape.Bits_Reserved` for a class-nested enum); an **alias enumerator** (`Font_FA_Bold = Font_FontAspect_Bold`, OCCT's "old aliases"; `Resource_ANSI`, `BinTools_FormatVersion_CURRENT`) is exported by name after it | matches C++: an unscoped enumerator lives in the enclosing namespace/class; OCP and 7.x code spell them that way (build123d imports 28 such names, `Font_FA_Bold` among them). nanobind's `export_values()` iterates the Python enum class, which hides aliases (`nb_enum.cpp:428`), so the emitter exports those itself (2026-09-22). A scoped `enum class` stays nested (`gp_Dir.D.NZ`; `gp_Dir.Z` is the method) |
| **R-ENUM** nested `enum class` | attribute of the class (`gp_Dir.D.Z`) | |
| **R-ANON-ENUM** anonymous enum (`enum { BVH_Constants_MaxTreeDepth = 32 };`) | integer attributes on the module/class | C++ integer constants |

#### 6.3 Parameters and results

How arguments go in and results come out (the user-facing summary is 2b).

| C++ idiom | Python | Rule |
|---|---|---|
| **R-OUT** non-const reference to a primitive (`double&`, `int&`, enum) as parameter | dropped from the signature, **returned** (bare value if it is the only result, else a tuple; a non-void return comes first) | pure-out is the common case (`gp_Pnt::Coord`) |
| **R-OUT** free function with `double&`/`int&` out-parameters (`MathUtils::DepressCubic`) | out-params returned as a tuple, like methods | |
| **R-INOUT** same, but the method reads the value too (`gp_Trsf::Transforms`) | parameter kept **and** returned | listed in `overrides.toml [inout]`; not derivable from syntax |
| **R-REF-CLASS** non-const reference to a class (`gp_XYZ&`) | passed and **mutated in place** | nanobind by-reference semantics |
| **R-OPTIONAL-PTR** pointer parameter with a null default (`bool* theIsStored = nullptr` in `BRep_Tool::CurveOnSurface`, `unsigned* theErrorCode = 0` in `BRepFill_AdvancedEvolved::IsDone`, `Standard_OStream* = nullptr` in `BRepBuilderAPI_FastSewing::GetStatuses`, `Standard_Address = NULL` in `TopOpeBRepBuild_WireEdgeSet`) | dropped from the signature; the lambda passes `nullptr` (constructors through a placement-new lambda / `nb::new_`) | the optional output/context is not expressible; 16 members were skipped entirely before 2026-09-21 (`AdvancedEvolved` had no `IsDone`) |
| **R-FIXED-ARRAY** C array of a primitive or bound class with a known size, as parameter or member (`gp_Pnt theP[8]` in `Bnd_OBB::GetVertex`, `const int (&theEdges)[3]` in `BRepMesh_Triangle`, `double myPeriod[3]` in `BOPAlgo_MakePeriodic::PeriodicityParams`) | non-const → out-parameter returned as a list of N (suffix type `list`); const → any sequence of N (`std::array` caster, copied into a C array for the call); member → list property (`def_prop_rw`, read-only when const) | arrays of unknown size (`double theCoeff[]`), of pointers or of std types stay out (R-ARRAY) |
| **R-OUT-HANDLE** non-const reference to a `handle<T>` (`BRep_Tool::CurveOnSurface(E, handle<Geom2d_Curve>& C, handle<Geom_Surface>& S, L, double& First, double& Last)`, `GeomTools::Read(handle<Geom_Surface>&, istream&)`) | an **out-parameter** like `double&`: dropped from the signature, returned (`C, S, First, Last = CurveOnSurface(E, L)`) | the caster hands the callee a *temporary* handle, so a handle assigned by the callee was lost silently before 2026-09-21 (35 sites in FoundationClasses/ModelingData, 50 more in ModelingAlgorithms). Methods that read the handle first are in/out via `overrides.toml [inout]` (`GeomLib::ExtendCurveToPoint(Curve, …)` keeps `Curve` and returns the extended curve; 7 entries, each checked against the `.cxx`). Overloads that differ only in the out-handle type are told apart by the R-COLLISION suffix (`GeomTools.Read__Geom_Curve`, `Read__Geom2d_Curve`, `Read__Geom_Surface`) |
| **R-HANDLE** `handle<T>` return; `handle<T>` parameter | most-derived registered type; null → `None`; a parameter accepts `None` (`nb::arg(...).none()`, 4.2) | caster |
| **R-NULL** OCCT undefined behaviour on null input (`BRep_Tool::Surface(aNullFace)` dereferences the null `TShape`, `BRep_Tool.cxx:125`; likewise `Curve`, `Pnt`, `Triangulation`) | **faithful**: the process crashes as it does in C++; no guards are inserted | decision 2026-09-21: guards would be a hand-maintained list that hides the OCCT contract; callers check `IsNull()` as in C++ (build123d does). Revisit if it bites in practice |
| **R-RESULT** `T*` / `T&` return, T Transient | wrapped in `handle<T>` (same Python object as before) | never let nanobind own a Transient |
| **R-RESULT** `T*` return, other class | `rv_policy::reference` | |
| **R-PTR-REF** `T*&` return (`BOPAlgo_Builder*& BRepAlgoAPI_BuilderAlgo::Builder()`, `DSFiller()`) | the pointer, copied out by a lambda: `reference` for a class, a handle for a Transient | nanobind cannot return a reference to a pointer |
| **R-PTR-INCOMPLETE** `T*` or `T&` where `T` is only forward-declared in the package's translation unit (`BOPDS_DS* BOPAlgo_Builder::PDS()`) | bound when `T.hxx` exists in the OCCT install: the emitter includes it (the class behind every parameter/result type is an include candidate, 5.2) | `Standard_CLocaleSentry::GetCLocale()` (`locale_t`, no header), `const AVStream&`/`const AVRational&` (FFmpeg, `Media_*`) and `XEvent&` (X11, `Xw_Window::ProcessMessage`) stay out — references included since 2026-09-22 (they compiled to `typeid` of an incomplete type before) |
| **R-RESULT** `T&` (mutable) return, other class | `rv_policy::reference_internal` for methods; **copied** for free functions (`TopoDS::Vertex(TopoDS_Shape&)`) | in-place edits via `ChangeXxx()`; a free function has no `self` to tie the reference to, and the mutable `TopoDS::Xxx` overloads are unreachable anyway (the `const&` overload is registered first) |
| **R-REF-PRIMITIVE** non-const method returning a mutable reference to a primitive (`double& math_Matrix::Value(i, j)`, `double& gp_XYZ::ChangeCoord(i)`, `bool& BRepTools_ReShape::ModeConsiderLocation()`) | getter under the C++ name (returns the value) plus a **Python addition** setter: `Set<Name>` with a `Change` prefix dropped (`SetValue(i, j, v)`, `SetModeConsiderLocation(b)`) unless OCCT already has a method of that name (`gp_XYZ::SetCoord`), and for `operator()`/`operator[]` `__setitem__` (+ `__getitem__`) with a tuple index for several arguments (`a[(2, 1)] = 7.0`) | Python cannot hold a reference to a `double`; the setter docstrings say "Python addition" |
| **R-DEFAULT** default argument | cast to `std::decay_t<ParamType>` (a `char` default written as `0` becomes a 1-char `str`); unqualified static members/enumerators of the class are qualified (`NCollection_IncAllocator::THE_DEFAULT_BLOCK_SIZE`) | the expression is emitted outside the class scope |
| **R-DEFAULT-QUAL** default argument naming a nested type unqualified (`= Options()` inside `BRepGraphInc_Populate`) | qualified from the AST type reference | same mechanism as the namespace case |
| **R-DEFAULT-QUAL** default argument naming an enumerator or static member of an *enclosing* or *base* class unqualified (`= IterationFilter_None` inside `Font_TextFormatter::Iterator` and `Graphic3d_LightSet::Iterator`) | qualified through the class chain of the referenced declaration (`Font_TextFormatter::IterationFilter_None`) | the nested class sees the outer class's names, the emitted expression does not (2026-09-22; until then only the class's own members and namespaces were qualified) |
| **R-DEFAULT-QUAL** default argument naming something from a namespace unqualified (`= LeastSquaresMethod::QR` inside `namespace MathLin`, `= THE_2PI` via `using namespace MathUtils`) | qualified from the AST reference (`MathLin::LeastSquaresMethod::QR`, `MathUtils::THE_2PI`) | the expression is emitted outside the namespace |
| **R-DEFAULT-UNBOUND** default argument of a type no binding knows (`BRepGraph_OccurrenceId`, a nested class template instantiation) | member skipped, reported | nanobind converts defaults to Python at `.def` time → `std::bad_cast` aborts the module import; `nullptr` defaults are fine (→ `None`) |
| **R-CHAR** `char` parameter | 1-character `str` | nanobind convention |
| **R-CHAR16** `char16_t` / `const char16_t*` (`Standard_ExtString`, the UTF-16 API of `TCollection_ExtendedString`); `char32_t` (`Standard_Utf32Char`: the code-point API of `Font_FTFont::AdvanceX/HasSymbol/RenderGlyph`, `Font_TextFormatter::Iterator::Symbol`) | `str` (1 character / UTF-16 string), casters in `nanoocp_common.h` (stable-ABI `PyUnicode_AsUTF16String` / `PyUnicode_DecodeUTF16`, `PyUnicode_ReadChar` / `PyUnicode_DecodeUTF32`); a `char32_t` is a 1-character `str` in both directions (`font.HasSymbol("€")`; an `int` is rejected) | `ToExtString()` round-trips; `wchar_t` (only in hasher specialisations) is not cast. `PyUnicode_FromKindAndData` is not in the limited API |
| **R-CSTRING** `const char*` (`Standard_CString`) | `str`, UTF-8 | **limitation:** `TCollection_AsciiString` holds 8-bit (Latin-1-like) text; `ToCString()` on such content raises `UnicodeDecodeError` in Python (OCCT treats U+0080..U+00FF as representable). Use the `?`-replacement overload or the `ExtendedString` UTF-8 paths. |
| **R-STL** `std::vector/map/set/pair/optional/shared_ptr/function/string_view` of supported types | native Python objects via nanobind's STL casters; a **non-const reference** to one (`BRepMesh_ConeRangeSplitter::GetSplitSteps(…, std::pair<int, int>&)`) is an out-parameter like `double&` (R-OUT; suffix type `tuple`/`list`/`dict`/`str`) because the caster hands the callee a temporary | `std::shared_ptr<std::istream>`, `std::vector<NestedStruct>` are skipped (reported) |
| **R-STREAM-OUT** `std::ostream&` parameter (`DumpJson`, `Dump`, `Print`, `BRepTools::Write(shape, stream)`) | dropped from the signature, the written text is **returned as `str`** (a tuple after a non-void result, like out-params); a returned `Standard_OStream&` (chaining, `TopAbs::Print`) is dropped | the out-param rule applied to streams; `str` decoded with `surrogateescape` so a stray non-UTF-8 byte is lossless. **Binary formats are `bytes`**: the packages listed in `overrides.toml [stream] binary_packages` (`BinTools`; `BinLDrivers` & co. in Phase 2) return `bytes` from their `ostream&` parameters (`BinTools.Write(shape)` is byte-identical to the file form, tested) — decision 2026-09-21, replacing the surrogate-escaped `str`. Not a file-like target: OCCT's stream APIs are of modest size, and the file-path overloads exist for bulk I/O |
| **R-STREAM-IN** `std::istream&` / `Standard_SStream&` parameter (`BRepTools::Read(shape, stream, builder)`, `InitFromJson(sstream, pos)`, `GeomTools::Read`) | a **text file-like object** (`typing.TextIO`: `io.StringIO`, an open file; anything with `read()`), read completely into a `std::stringstream` for the call | deliberately *not* a `str`: `Read(shape, "x.brep", builder)` must keep hitting the file-path overload; a non-file-like argument falls through to the next overload (`nanoocp::TextInput` caster). `InitFromJson`'s `int& theStreamPos` is in/out (`overrides.toml [inout] "*::InitFromJson"`, start at 1). In a binary package the parameter is a **binary file-like object** (`typing.BinaryIO`: `io.BytesIO`, a file opened `"rb"`; `nanoocp::BinaryInput` caster, `read()` must return `bytes`, so a text file-like falls through). Constructors keep streams unsupported (an object may hold the reference) |

#### 6.4 Overloads that Python cannot tell apart

See 2a (3) and 2b.

| C++ idiom | Python | Rule |
|---|---|---|
| **R-COLLISION** overloads that coincide once out-params are dropped (`gp_Pnt::Coord()` → `gp_XYZ` and `Coord(double&, double&, double&)`; `GeomAPI_IntCS::Parameters(Index, U&, V&, W&)` for a point and `Parameters(Index, U1&, V1&, U2&, V2&)` for a segment; `GeomTools::Read(handle<Geom_Curve>&, istream&)` / `Geom2d_Curve` / `Geom_Surface`) — overloads that differ only in the *width* of their parameters, out-parameters included (`Graphic3d_Vertex::Coord(double&, double&, double&)` / `Coord(float&, float&, float&)`), are R-WIDTH twins, not a collision: both keep the plain name, the wider one first (2026-09-22) | every overload that has out-parameters is bound as **`Name__<type1>_<type2>_…`** — the Python types of its removed out-parameters in C++ order (`float`, `int`, `bool`, `str`; `str`/`bytes` for a stream; an enum or class by its Python name, a container instantiation by its 6a name): `Coord__float__float__float()`, `Parameters__float__float__float(i)` and `Parameters__float__float__float__float(i)`, `Read__Geom_Curve(stream)`, `Normal__CSLib_NormalStatus(…)`, `Knots__NCollection_HArray1__double()`; an overload **without** out-parameters keeps the plain name and means what it means in C++ (`Coord()` → `gp_XYZ`, `Bnd_Box.Get()` → `Limits`, `BRep_Tool.Parameter(V, E)` → `float`); after `_s` when both apply (`Name_s__float`). The docstring's first line names the C++ overload. Applies to methods and namespace functions | Python cannot dispatch on results, so the overloads must get distinct names; the suffix is unique within a group because C++ overloads cannot share a parameter list, it is stable across OCCT versions (unlike a number) and derivable from the reference docs — the same principle as `_s` (R-STATIC-S), applied only where a collision exists. 54 suffixed overloads in 40 groups over the seven toolkits (2026-09-21; the 11 `operator>>` groups are not bound anyway). Decision 2026-09-21, replacing the winner rule of 2026-09-20 (scalar result / most out-params / deprecated loses), which made 10 of 51 overloads unreachable that carry different information (`GeomAPI_IntCS::Parameters`, `GeomTools::Read`, `CSLib::Normal`, `Units::ToSI` with its dimension handle) |
| **R-CONST-TWIN** overloads that differ only in constness — of the method (`const gp_XYZ& Origin() const` / `gp_XYZ& Origin()`, `math_Vector::Value(i)`, `NCollection_Vec3::x()`, `BRepGraph::Editor()`) or of a parameter (`TopoDS::Vertex(const TopoDS_Shape&)` / `(TopoDS_Shape&)`, `NCollection_Mat4::Map(const T*)` / `(T*)`) | only the **least const** twin is bound; the others are reported | Python objects are never const, so C++ itself would select the non-const overload on any Python-held object; before 2026-09-21 header order decided, i.e. whether `arr[i].SetX()` edited the container (`reference_internal`) or a copy. 91 twins skipped in the seven toolkits |
| **R-WIDTH** overloads that differ only in the width of scalar parameters (`Abs(double)` / `Abs(float)`, `Min`, `Max`, `Quantity_Color::Convert_sRGB_To_LinearRGB`, `NCollection_PackedMap(size_t)` / `(int)`, `Poly_ArrayOfNodes::Value(int)` / `(size_t)`) | both bound, the **wider** one registered first: `double` before `float`, `int` before `size_t`/`unsigned`/`long`/… (`order_by_width()` in `emit.py`, also for constructors and namespace functions); every pair reported | nanobind takes the first overload a Python `float`/`int` fits; a narrow twin first would truncate to `float` or reject negative indices. Header order happened to be right in every current case (`Standard.Abs(-1e300) == 1e300` verified) but is not a rule. 16 pairs |
| **R-CTOR-AMBIGUOUS** constructor overloads whose call with some number of arguments is ambiguous in C++ (`IntPolyh_Array(const int aIncrement = 256)` next to `IntPolyh_Array(const int aN, const int aIncrement = 256)`: `IntPolyh_Array<T>(5)` does not compile) | a constructor is bound with the largest number of leading parameters whose call is unambiguous (`nb::init<>()` for the first one above, the second in full); a constructor with no such arity is skipped; no `implicitly_convertible` when the one-argument call is ambiguous | nanobind's `nb::init<Args…>` always calls the constructor with every bound parameter (Python fills the defaults), so the ambiguity is a compile error; `resolve_ctor_arities()` in `emit.py` (pure, unit-tested); reported as `overload-collision` |

#### 6.5 Operators, conversions, hashing, iteration

The Python additions of 2c.

| C++ idiom | Python | Rule |
|---|---|---|
| **R-OPERATOR** `operator+ - * / % ^ & \| == != < <= > >= () []`, unary `- + !` | `__add__` … `__call__`, `__neg__` … | member operators; `nb::is_operator()` |
| **R-IOP** `void operator+=` etc. | `__iadd__` … returning `self` (same object) | OCCT in-place operators return `void` |
| **R-FREE-OP** free `operator*(double, gp_Vec)`; a **hidden friend** operator declared in the class body (`friend NCollection_Vec3 operator+(const NCollection_Vec3&, const NCollection_Vec3&)` in `NCollection_Vec2/3/4`, `friend math_Matrix operator*(double, const math_Matrix&)`, `friend bool operator==(const BRepGraph_ItemId&, const BRepGraph_ItemId&)`, `NCollection_UtfString::operator+`) | `__rmul__` on `gp_Vec` (reflected when the class is the 2nd operand, normal when it is the 1st); the friend is handed to the same pass from the class walk (`Class.friend_ops`) and bound through a lambda that finds it by ADL (`v + v` on `Graphic3d_Vec3`, `2.0 * m` on `math_Matrix`) | a hidden friend is found by ADL only and was never walked before 2026-09-22 — silently, since nothing reports a `FRIEND_DECL`; the lambda has no library symbol to check (R-UNDEFINED does not apply) |
| **R-CONV-SCALAR** conversion operator `operator bool/int/double() const` | `__bool__`/`__int__`/`__float__` | |
| **R-CONV** conversion operator `operator T() const` / `operator const handle<T>&() const` with a bound class `T` (`gce_MakeLin` → `gp_Lin`, `GC_MakeSegment` → `handle<Geom_TrimmedCurve>`, `BRepGraph_EdgeId` → `BRepGraph_NodeId`, later `BRepBuilderAPI_MakeShape` → `TopoDS_Shape`) | `T(aFrom)` constructor overload on `T` plus, unless `explicit`, `nb::implicitly_convertible` (a From passes where a T is expected); a handle conversion returns the same object | emitted in a phase of its own after every definition of the toolkit (a class's zero-argument `__new__` must come first); a target in a *later* toolkit would be skipped and reported (none at present: `NCollection_Vec3<float>` is instantiated on demand by `Quantity` in a clean run, so `Quantity_Color` → `BVH_Vec3f` works); enum targets have no Python spelling |
| **R-IMPLICIT-CONV** non-`explicit` converting constructor `T(const A&)` | `nb::implicitly_convertible<A, T>` — `OSD_Path("/x")` works because `TCollection_AsciiString(const char*)` is implicit | C++ implicit conversion semantics, 1:1 |
| **R-IMPLICIT-COPY** implicit copy constructor (none declared: `TopoDS_Shape`, `gp_Pnt`, …) | `__init__(theOther)` bound when `std::is_copy_constructible_v<T>` (helper `nanoocp_implicit_copy_ctor`, after the declared constructors) | `TopoDS_Shape(aVertex)` is the C++ way to upcast a shape; sub-classes convert implicitly as in C++ |
| **R-IMPLICIT-DEFAULT** class declaring no constructor | implicit default constructor bound only if `std::is_default_constructible_v<T>` (compile-time helper `nanoocp_implicit_default_ctor`) | a reference member deletes the implicit constructor without the header saying so (`MathRoot::MultipleGetValueFn`) |
| **R-HASH** `std::hash<T>` specialised by OCCT (`TopoDS_Shape` and its sub-classes, `gp_Pnt`, `TopLoc_Location`, `Quantity_Color`, …) | `__hash__` calling `std::hash<T>` | nanobind keeps identity hashing even with `__eq__`; a value-equal shape must hash equal to be a dict key. Classes with `operator==` but no `std::hash` keep identity hashing |
| **R-ITER** class with `More() -> bool`, `Next()` and a parameterless `Value()` or `Current()` returning a value (`TopExp_Explorer`, `TopoDS_Iterator`, `BRepTools_WireExplorer`, `Adaptor3d_TopolTool`, the `BRepGraph` iterators; 32 in the seven toolkits; since 2026-09-22 also the seven hand-written binder `Iterator` classes of 6a — `NCollection_List__int.Iterator`, the map iterators yielding `Value()`: the key for `Map`, the value for `DataMap` — and through them `Graphic3d_SequenceOfHClipPlane.Iterator`) | `__iter__` returning `self` and `__next__` = `Value()` (or `Current()`) then `Next()`, `StopIteration` when `!More()` — the object is its own iterator, like a file (a second `for` over an exhausted one yields nothing); `nanoocp_def_iter` in `nanoocp_common.h`, `Emitter._iter_getter` | Python addition (2c), decision 2026-09-21; the element is copied out before `Next()`, so `Value()` results that are Transient pointers/references are excluded (`Storage_BucketIterator`) |
| **R-ITERATOR** STL-style iterators (`NCollection_ForwardRangeIterator`, `NCollection_IndexedIterator`, `NCollection_StlIterator`, `NCollection_UtfIterator`, `NCollection_DynamicArray::DynamicIterator`; `begin()`/`end()`) | skipped | Python iterates with `__iter__` (containers, and R-ITER below) |

#### 6.6 Classes and members that need special handling, and what is skipped

| C++ idiom | Python | Rule |
|---|---|---|
| **R-FIELD** public data member | `def_rw` when the member type is copy-assignable, `def_ro` otherwise (helper `nanoocp_def_field`, compile time); a **bit-field** (`unsigned stick : 1` in `Graphic3d_CStructure`, the only public ones in the install) is a `def_prop_rw` through lambdas, since no pointer-to-member exists (`Field.is_bitfield`, 2026-09-22) | a member of a type with a deleted assignment (`BRepGraphInc_Storage`) breaks `def_rw` |
| **R-MI** class with several bases (`IMeshData_Edge : IMeshData_TessellatedShape, IMeshData_StatusOwner`) | first base only, others reported | nanobind single inheritance (4.2) |
| **R-USING** `using Base::name;` in a public section (`BRepAlgoAPI_Algo : protected BOPAlgo_Options` re-exports `SetFuzzyValue`, `SetRunParallel`, `HasErrors`, `GetReport`, … — 14 members every boolean has and build123d calls; `Blend_FuncInv::Set`, `BRepFeat_Builder::Perform` un-hide base overloads) | the base's overloads of `name` (resolved with `clang_getOverloadedDecl`) are bound **on the derived class through lambdas** calling `self.name(...)` on the derived object; out-parameters, streams and results follow the usual rules (class results are copied, a `T*` keeps `reference`); `using Base::Base;` binds the base's constructors on the derived class (`BRepGraph_FacesOfEdge(theGraph, theEdge)`; default/copy/move are not inherited in C++, the derived class gets its own implicit ones) | a member pointer of the base would need the inaccessible upcast, and nanobind never merges overloads across classes, so without the rule a derived overload set hides the base's. The member's symbol belongs to the base's library (the base's own binding runs the nm check). Decision 2026-09-21 |
| **R-NONCOPYABLE** class whose implicit copy/move constructor does not compile although the traits say copyable: a member `NCollection_CellFilter<…>` or `NCollection_Map<…CellFilter<…>::Cell>` (`math_GlobOptMin`, `BRepExtrema_ProximityValueTool`, `BRepMesh_CircleTool`, `BRepMesh_VertexTool`, the `CellFilter` instantiations themselves), a container of a type whose copy constructor is deleted (`NCollection_Sequence<CSLib_Class2d>` in `BRepTopAdaptor_FClass2d`), or such a class held by value (`BRepExtrema_ShapeProximity`, `BRepMesh_Delaun`) | **detected by the parser** (field types; `overrides.toml [skip] noncopyable` remains for cases it cannot see, currently empty) and bound through a generated wrapper struct — except a **Transient** class (`BRepMesh_VertexTool`), which is skipped: the wrapper would be the registered type while OCCT hands out the OCCT class, and nanobind's copy wrapper would not compile — with deleted copy and move constructors and inherited constructors, under the original name; member pointers still name the OCCT class, lambdas take the wrapper; reported (category `noncopyable`) | nanobind instantiates its copy/move wrappers from `std::is_copy/move_constructible` (no hook for move); the wrapper is what Python sees (`type(opt).__name__ == "math_GlobOptMin"`), no OCCT API returns a reference to one of them |
| **R-INCOMPLETE** class with a data member of a type declared but never defined in the headers (`BRepGraph_CacheMesh::Slot`, defined in the `.cxx`; through `NCollection_LinearVector<Slot>`) | class skipped, reported | `nb::class_` needs the destructor; `unique_ptr`/`shared_ptr`/`handle`/`NCollection_Handle` members are exempt (pointee may stay incomplete, `Geom_OffsetSurface`, `BRepOffsetAPI_ThruSections`) |
| **R-UNDEFINED** method, constructor or free function declared, never defined by OCCT (`math_NewtonMinimum::IsConvex`, `OSD_Path::LocateExecFile`, the overload `GeomInt_WLApprox::Perform()` next to three defined `Perform` overloads, three `Geom2dGcc_FunctionTanCuCuCu` constructors, `TopOpeBRepDS`'s `FUN_scanloi`/`FDSSDM_s1s2makesordor`) | skipped automatically, per overload | `generator/symbols.py`: `nm` on the toolkit library vs. libclang's `Cursor.mangled_name` of every method/constructor without an inline definition (bodies are parsed so `get_definition()` sees out-of-class inline definitions; pure virtuals excluded). Mangled names make the check exact and overload-aware; the platform mangling matches `nm` on macOS (leading underscore included, verified), Linux *unverified*, Windows has no `nm` (the linker reports leftovers). Replaced the name-only check plus three hand-listed overloads in `overrides.toml` on 2026-09-21 (six link errors in TKGeomAlgo) |
| **R-UNDEFINED-COPY** copy constructor declared in the header but never defined in the library (`GCPnts_DistFunction`, the pre-C++11 idiom to forbid copies) | class skipped, reported | nanobind's copy wrapper is instantiated for every `std::is_copy_constructible` type → link error; detected by `nm` (`Class::Class(Class const&)` absent; `= default` counts as defined) |
| **R-DEPRECATED** deprecated member (`Standard_DEPRECATED("use Poles() returning const reference instead")`, 62 in FoundationClasses/ModelingData) | **bound**, OCCT's message becomes the first line of the docstring (`Deprecated in OCCT: use Poles() …`); no runtime warning | the OCCT docs are the nanoOCP docs, and 7.x-era code keeps working (build123d calls two deprecated members); the message is read through `clang_getCursorPlatformAvailability` (cindex exposes only the availability kind); the extension is compiled with `-Wno-deprecated-declarations`. Decision 2026-09-21 (was: skipped) |
| **R-PRELUDE** header that is not self-contained (`GeomGridEval_Line.hxx` calls `Geom_Line::Lin()` with `gp_Lin` only forward-declared; `IntWalk_PWalking.hxx` names `handle<IntSurf_LineOn2S>` and `ChFiKPart_ComputeData_ChPlnCon.hxx` `ChFiDS_ChamfMode` without any declaration) | the parser reads `incomplete type 'X'`, `use of undeclared identifier 'X'` or `unknown type name 'X'` from the diagnostics, includes `X.hxx` before the package headers and parses again; the generated `.cpp` includes it first too. The same loop runs on the **emitted include list** of every package (`parse.include_prelude`, one TU with bodies skipped): the identifier-based extra includes may pull in a header that is not self-contained (`HLRTopoBRep.cpp` includes `Contap_Contour.hxx`, whose `Contap_Line.hxx` names `handle<Adaptor2d_Curve2d>` undeclared) | reported. A survey of all 1 494 ModelingAlgorithms headers (2026-09-21) found only these two cases in umbrella order; the include-list check found the Contap case |
| **R-SKIP-HEADER** public header including a private `.pxx` that is not installed (`GeomBndLib_Line.hxx`, `_Line2d`, and `GeomBndLib_Curve.hxx`/`_Curve2d.hxx` which include them; OCCT 8.0.1 packaging bug) | skipped via `overrides.toml [skip] headers` | `BndLib_Add3dCurve` and the per-type `GeomBndLib_Circle` … classes remain |
| **R-TEMPLATE-SKIP** function/class templates in a namespace (`MathSys::Newton<FuncSetType>`), type aliases in a namespace | not bound, reported | need a concrete functor type; the classic `math_*` classes are the Python-facing API |
| **R-ARRAY** array parameter or member that R-FIXED-ARRAY cannot express: unknown size (`const double theCoeff[]`, `BRepGProp_Gauss`), pointers (`const Poly_CoherentTriangle *pTri[2]`), std types (`std::array<std::complex>`) | skipped | 7 lines |
| deleted members, move constructors | skipped | reported |
| **R-UNSUPPORTED** raw pointers to primitives (also when they appear as `T*` in a 6c instantiation — `NCollection_Mat4<float>::Map(float*)`, `math_VectorBase<double>(const double* theTab, …)` were bound until 2026-09-21 and would have taken a pointer to a temporary), references to pointers (`char*&`), pointers to incomplete types (`_xlocale*`), C-array fields, reference-typed fields, template members, nested class templates, non-public bases, `std::ostream&` *returns* and stream members (`BinTools_IStream`, `Message_PrinterOStream`) | skipped | reported |

### 6a. NCollection containers (hand-written binders)

#### Facts

- OCCT 8.0.1 spells containers directly in its API (`Geom_BSplineCurve(const NCollection_Array1<gp_Pnt>& Poles, …)`; 2050 distinct `NCollection_*<…>` spellings in the installed headers).
- The pre-8.0 typedef names (`TColgp_Array1OfPnt`, `TopTools_ListOfShape`, 972 headers) live in `src/Deprecated/NCollectionAliases`, outside every toolkit, each marked deprecated with "use `NCollection_Array1<gp_Pnt>` directly". The reference documentation for the container API is therefore the template class page.
- `NCollection_HArray1<T>` derives from both `NCollection_Array1<T>` and `Standard_Transient`; `NCollection_Array1` has a virtual destructor (polymorphic).

#### Decision (2026-09-20, option b)

- One hand-written C++ binder per template kind in `src/cpp/common/nanoocp_ncollection.h` (`nanoocp::bind_NCollection_Array1<T>(module, name)`, `bind_NCollection_HArray1<T>`), instantiated by the generator.
- The alternative — instantiating template members generically via libclang with argument substitution — was rejected: dependent types, `enable_if` overloads and members that do not compile for every element type would each need a special rule, for the same user-visible result.
- All 15 container kinds of the scope are bound.

#### Which instantiations, and their names

- **Which:** every `NCollection_X<…>` (also inside `handle<…>`, also nested) that appears in a bound signature, collected while parsing; nested arguments and `requires` (`Array1<T>` before `HArray1<T>`) are bound first. Over-approximation (unused instantiations) only costs compile time. A template that *is* a binder kind's nested class (`NCollection_TListIterator<T>` = `NCollection_List<T>::Iterator`, `BINDERS[...]["nested_from"]`) registers the owner instantiation instead of a 6c class of its own (`TopOpeBRepDS_HDataStructure::SameDomain` returns `NCollection_List__TopoDS_Shape.Iterator`; binding it twice aborted the import).
- **Primary spelling `NCollection_Array1[T]`** (revised 2026-09-20, replaces "home = element package"): `nanoocp.NCollection.NCollection_Array1[gp.gp_Pnt](1, 4)` mirrors the docs' `NCollection_Array1<gp_Pnt>`.
    - `NCollection_Array1` is a generated `Template` object (`nanoocp/_templates.py`, table in the `NCollection` shim from `manifest.json`) mapping Python element types to the bound classes: `float → double`, `int → int`, `bool → bool`, `str → std::string`, an OCCT class for itself **and** for `handle<class>`, a bound instantiation for a nested container.
    - Other C++ scalars (`float`, `size_t`, `char`…) are reachable only by the concrete name.
    - Unbound element types raise `TypeError` listing what is bound; calling the template itself raises `TypeError` with a hint.
- **Concrete classes:** one per C++ instantiation, named `template__arg1__arg2` (double underscore separates arguments — OCCT names never contain `__`; `handle<X>` → `Handle_X`; nested left to right; defaulted template arguments such as hashers are omitted): `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`. They are what `type()`, `repr` and stubs show.
    - All of them live in **`nanoocp.NCollection`** (the doc page's package), bound by the first toolkit that needs them (`manifest.json` records `by`, the binding package, so regeneration is idempotent — verified by running the generator twice).
    - Because a later toolkit adds to `NCollection`, `import nanoocp` imports **all toolkit modules eagerly** in dependency order and shims have a module `__getattr__` fallback.
- **Deprecated typedef names:** parsed from `NCollectionAliases` (one libclang TU, ~1 s) and exposed as lazy aliases: `nanoocp.TColStd.TColStd_Array1OfReal is nanoocp.Standard.NCollection_Array1_double`; prefixes that are not packages in 8.0 (`TColgp`, `SelectMgr` until TKV3d) become alias-only modules. So both 7.x-era docs/OCP code and 8.0 docs resolve. Typedefs of **6c instantiations** (`Graphic3d_Vec3 = NCollection_Vec3<float>`, `Graphic3d_Mat4`, `gp_Vec3f`, `SelectMgr_Vec3`) resolve through the manifest's canonical spelling too (2026-09-22; they were silently dropped before — 235 resolved, 603 not bound: `Vec4<unsigned char>` & co. have no bound instantiation).
- **`[instantiate]` override:** instantiations to bind although no bound OCCT signature uses them (`NCollection_Map<int>`, `NCollection_DataMap<int, double>`, …), registered by the `NCollection` package. Used to exercise binders that the current scope does not reach yet, and available for user conveniences.

#### Methods, docstrings, Python additions

- **1:1 methods** with OCCT names and signatures.
- **Docstrings extracted from the template header** by the generator into `ncollection_docs.h` (first overload wins).
- A **coverage check** reports template members that are neither bound nor listed as knowingly skipped (`Move`, `operator=`, `EmplaceValue`, iterators, allocation operators).
- **Python additions** (never replacements, marked "Python addition" in their docstrings): `__len__` (= `Length`), `__iter__` (values `Lower()..Upper()`), `__setitem__` (= `SetValue`). `__call__` and `__getitem__` are OCCT's own `operator()`/`operator[]` = `Value` with the **OCCT index**, not 0-based.
- `Change*` accessors are bound only for class element types (`double&` cannot be exposed).

#### The H-types: HArray1 / HArray2 / HSequence / Shared (revised, see 4.2 "Multiple inheritance")

- Bound with the offset-0 base (`Array1<T>`, `Array2<T>`, `Sequence<T>`, `T`), so the container API is inherited with an exact pointer and `isinstance(h, NCollection_Array1[T])` holds.
- `GetRefCount`, `DynamicType`, `IsKind`, `IsInstance`, `get_type_*` are bound through adjusting casts; handles convert both ways through the MI registry.
- The first version (base `Standard_Transient`, Array API re-bound, implicit conversion) was wrong and is gone.
- `h.Array1()` returns a sliced copy of static type `Array1` (returning `const A&` would make nanobind copy the dynamic type); `h.ChangeArray1() is h`.
- Stubs: the H-types derive from the generic container class; `NCollection_Shared[T]` is typed as an accessor with one overload per bound instantiation returning the concrete class (which derives from `T`'s class), because `Generic[_T]` cannot derive from `_T`.
- **Lesson recorded:** nanobind copy-constructs the *dynamic* type for polymorphic by-value/const-reference returns whenever that type is registered. For Transient classes this yields an owned private copy, which is harmless but can surprise; relevant wherever OCCT returns a polymorphic value class by const reference.

#### List / Sequence / HSequence (2026-09-20)

- Nested `Iterator` classes bound as `NCollection_List__int.Iterator` (1:1 with `NCollection_List<T>::Iterator`; `TopTools_ListIteratorOfListOfShape`-style aliases resolve to them), with `nb::keep_alive` on the container; they are their own Python iterators (R-ITER, `__iter__`/`__next__` yielding `Value()`, all seven binder kinds with an `Iterator`, 2026-09-22).
- **A class deriving from a binder's nested Iterator** (`Graphic3d_SequenceOfHClipPlane::Iterator : NCollection_Sequence<handle<Graphic3d_ClipPlane>>::Iterator` — the only one in OCCT 8.0.1, and the only way to iterate a view's clip planes, `myItems` being protected) is declared in the **templates phase**, after the instantiation that registers its base (`Class.after_templates`; the parser spells the base with the manifest key and registers the owner instantiation). The declare phase of every package runs before any templates phase, so the base would not exist yet otherwise (2026-09-22).
- `size_t` overloads that duplicate `int` ones are not bound (Python cannot distinguish them); `At`/`ChangeAt` (size_t only) are.
- `Contains`/`Remove(item)`/`__contains__` are bound only when `T` has `operator==` (compile-time trait; `gp_Pnt` has none, `TopoDS_Shape` has).
- Members returning the inserted element (`Append` → `T&`) return a view for class types and a value for scalars.
- Members inherited from the non-template bases (`NCollection_BaseList::Extent`, …) are covered by the docs/coverage extractor via `bases`.
- Python additions: `__len__`, `__iter__`, `__contains__`, and for Sequence `__getitem__`/`__setitem__` (1-based like `Value`).
- Generic stubs for the three kinds; verified with mypy and ty. Divergence: ty rejects `NCollection_List[int].Iterator` (nested class through a specialised generic), mypy accepts it — typed code uses the concrete `NCollection_List__int.Iterator`.
- **Ordering lesson:** instantiations are registered in the toolkit's *declaration* order, so packages are also *emitted* in that order; otherwise an `HSequence<T>` bound by an early-running package could precede the `Sequence<T>` its implicit conversion needs (observed as `implicitly_convertible: destination type unknown`).

#### Map / DataMap / IndexedMap / IndexedDataMap (2026-09-20)

- The hasher template argument is dropped from key and name only when it equals its default `NCollection_DefaultHasher<Key>` (`defaults` per kind in `BINDERS`, applied by `instance_args`); a custom hasher stays part of both, so it cannot be merged with the default instantiation (a different C++ type).
- Shared base members (`NCollection_BaseMap`: `NbBuckets`, `Extent`, …) in one helper.
- `Seek`/`ChangeSeek` return `None` for absent keys (a view for class items, a value for scalars); `Find(key, item&)`/`FindFromKey(key, item&)` only for class items (in-place).
- Skipped: `Contained` (`std::optional<std::reference_wrapper<…>>`), `Emplace*`, `Items()`/`IndexedItems()` views, `GetHasher`.
- Python additions: `__len__`, `__contains__`, `__iter__` over keys (index order for the indexed kinds), `__getitem__`/`__setitem__`/`__delitem__` on DataMap (`Find`/`Bind`/`UnBind`, `KeyError` when unbound), `__getitem__(index)` on the indexed kinds, `items()` → list of `(key, value)`.
- The indexed maps' iterators do not derive from `NCollection_BaseMap::Iterator` (no `Initialize`/`Reset`), the others do.
- Enums count as element types (`NCollection_IndexedMap[Message_MetricType]`).

#### Array2 / HArray2 / DynamicArray / DoubleMap / Shared (2026-09-20)

- `Array2<T>` derives from `Array1<T>` in 8.0 and inherits its binding (`__len__`/`__iter__` are flat, row-major; `Value(i)` is hidden by `Value(row, col)` as in C++; `a[(row, col)]` is the Python addition).
- `DynamicArray` is 0-based (`Lower() == 0`).
- `DoubleMap` has two default hashers (both stripped when default); iteration yields `(key1, key2)` pairs.
- `Shared<T>` requires `T` to be bound (class or instantiation), otherwise the instantiation is skipped with a report (`Standard_HMutex = Shared<Standard_Mutex>` is skipped because `Standard_Mutex` is not bound).

#### LinearVector (2026-09-20)

- `NCollection_LinearVector<T>`, OCCT 8's contiguous 0-based vector with `size_t` indices and BRepGraph's container of choice (`NCollection_LinearVector<BRepGraph_NodeId>` …).
- `Data()`/`begin()`/`end()` (raw element pointers) are not bound.
- A typedef of a binder instantiation (`BVH_Array3d = NCollection_LinearVector<NCollection_Vec3<double>>`) is an attribute alias of the concrete class, not a 6c class of its own.
- Container-typed **fields** (`MathRoot::MultipleResult::Roots`) and template arguments of instantiated templates (`NCollection_Iterator<NCollection_DynamicArray<Poly_CoherentTriangle>>`) register their instantiations like parameters do.
- Not bound: `NCollection_FlatDataMap`/`FlatMap` (BRepGraph internals, 6 signatures).

### 6b. Type stubs

- `python -m generator.stubs` (after the build; it imports the extension) runs nanobind's `StubGen` (API, recursive: the CLI refuses `-r` for modules without `__file__`) per package module into `src/nanoocp/<pkg>.pyi` — or `<pkg>/__init__.pyi` plus `<pkg>/<ns>.pyi` for a package with namespaces (5.1). Cross-references come out as `nanoocp.Standard.X` because of the `__module__` rule.
- It adds:
    - the deprecated typedef aliases as assignments;
    - in `NCollection/__init__.pyi` a hand-written **`Generic[_T]` class per container kind** (`generator/stubs/<kind>.pyi`, kept in step with the binder) and every instantiation as `class NCollection_Array1__double(NCollection_Array1[float]): ...`;
    - in every other stub, the concrete instantiation names in OCCT signatures rewritten to the generic spelling (`nanoocp.NCollection.NCollection_Array1__double` → `nanoocp.NCollection.NCollection_Array1[float]`, nested arguments included, missing `import nanoocp.<pkg>` lines added), because the checker types `NCollection_Array1[float](…)` as the generic and would otherwise reject passing it to any OCCT method (`Geom2d_BezierCurve(poles)`); the concrete class derives from the generic one, so results stay assignable.
- Verified with **mypy** and **ty** (`tests/test_typing.py` runs both on every `tests/typing/check_*.py`): `a[2]` is `float`, `h.Value(1)` is `Standard_Persistent`, `def f(arr: NCollection_Array1[float])` accepts every double array, nested classes and namespace modules resolve (`check_namespaces.py`), and the deliberate errors (wrong element type, wrong overload, `HArray1[X]` passed as `Array1[float]`, `Base` assigned to `Full`) are reported by both checkers.
- Known imprecision: a *returned* null handle is typed as the class, not `X | None` (same as nanobind's own handle stubs); handle *parameters* are `X | None` since `.none()` is emitted.
- The generic nested `Iterator` classes use their own type variables (`_IT`, `_IK`, `_IV`): a nested class cannot reuse the outer class's `_T` (mypy then treats it as non-generic and `Value()` was `Never`), and every concrete instantiation gets a concrete `class Iterator(NCollection_List.Iterator[int]): ...`, so `NCollection_List__int.Iterator(l).Value()` is `int` and `for x in it` types `x` (2026-09-22, `tests/typing/check_iterators.py`). The generic-spelling rewrite leaves a concrete name alone when a nested-class access follows (`class Iterator(nanoocp.NCollection.NCollection_Sequence__Handle_Graphic3d_ClipPlane.Iterator)`), the ty divergence above.

### 6c. Aliases of OCCT class templates (instantiated from the header)

#### What they are

- OCCT 8 turned several classic classes into class templates with aliases: `using math_Vector = math_VectorBase<double>;`, `math_IntegerVector`, `Bnd_B2d/B3d/B2f/B3f`, `BVH_Vec3d = BVH::VectorType<double, 3>::Type` (→ `NCollection_Vec3<double>`), `BVH_Builder3d`, `TColStd_PackedMapOfInteger = NCollection_PackedMap<int>`, `NCollection_String`, later `Extrema_ExtPC = Extrema_GGExtPC<Adaptor3d_Curve, …>`, `GeomLProp_CLProps`.
- These are not containers, so 6a does not apply; they are the one place where the generic option (a) is used (decision 2026-09-20).

#### Rule

- A package-level `typedef`/`using` whose canonical type is an instantiation of an OCCT class template (not an NCollection binder kind, not `handle`, not `std::`) — or an **un-aliased instantiation used as a base class** (`BRepGraph_WiresOfEdge : EdgeParentsOf<…>`, `Poly_ArrayOfNodes : NCollection_AliasedArray<>`, bound under the mangled name) — is bound as a normal class **under the alias name** (`nanoocp.math.math_Vector`, C++ type `math_VectorBase<double>`).
- The template's definition is walked with the ordinary class walker while a substitution map rewrites every type spelling and default argument:
    - template parameters → arguments (position-wise, using the parameter names of *every* declaration of the template, because a forward declaration may name them differently and libclang spells some dependent types with those names);
    - the injected class name → the full instantiation (`math_VectorBase` → `math_VectorBase<double>`).
- Arguments come from the canonical type when the alias goes through a metafunction (`BVH::VectorType<…>::Type`); non-type arguments (`BVH_Builder<double, 3>`) are taken as written.
- Members whose types stay dependent (libclang's `type-parameter-0-0`, e.g. `T* begin()`) are skipped and reported.
- A default `T(0)` whose argument is a multi-word builtin (`NCollection_Vec3<unsigned long>` in `Image_PixMapData`) is spelled as a C-style cast, `(unsigned long)(0)` — `unsigned long(0)` is not C++ (2026-09-22). `NCollection_Vec3<unsigned long>::cwiseAbs` is in `overrides.toml [skip] methods` (`std::abs(unsigned long)` is ambiguous).
- An instantiation with a **raw pointer as template argument** (`HLRBRep_SLProps = GeomLProp_SLPropsBase<void*, …>`, `HLRBRep_CLProps` over `const HLRBRep_Curve*`, the `Extrema_G*<void*, HLRBRep_CurveTool, …>` locators) is not bound and reported: every member takes or returns the pointer (R-UNSUPPORTED), and `const T&` with `T` a pointer is `T* const&`, not what the substitution spells.
- A member whose *body* does not compile for the argument (`IntPolyh_Array<IntPolyh_Edge>::Dump()` calls `(*this)[i].Dump()`, but `IntPolyh_Edge::Dump` takes an `int` and `IntPolyh_PointNormal` has none) cannot be seen from the signature: it is listed in `overrides.toml [skip] methods` with the instantiation name (three entries, found as compile errors).
- Instantiations have no library symbols, so the `nm` check does not apply to them.
- The same instantiation aliased in several packages is bound once (manifest key = canonical spelling) and aliased elsewhere; the same alias repeated in several headers of one package is bound once.
- Docstrings come from the template. Stubs: stubgen emits a full concrete class for the alias (no generic class, unlike 6a).
- Verified: `math_Vector` constructors (incl. from `gp_XYZ`), operators, `math_Matrix.Row()` returning `math_Vector`, `BVH_Vec3d`, `Bnd_B3d`, `TColStd_PackedMapOfInteger`.

#### On-demand instantiation (2026-09-20)

- Besides aliases and base classes, every instantiation of an OCCT class template that appears in a bound signature, field or typedef (`BRepGraph_MutGuard<BRepGraphInc::EdgeDef>` returned by `EditorView::EdgeOps::Mut`) is instantiated under its mangled name unless an earlier package or run bound it (manifest); its own template arguments are registered too.
- **Template bases of instantiations (R-TEMPLATE-BASE, 2026-09-21):** a base that is itself a template instantiation is only spellable after substitution (`BVH_PrimitiveSet<double, 3> : BVH_Object<double, 3>`, `BVH_Distance<…> : BVH_Traverse<…> : BVH_BaseTraverse<double>`); such spellings are collected during the walk and resolved by a **probe re-parse** — the package umbrella plus one `using nanoocp_probe_i = <spelling>;` per base gives each a libclang `Type` to instantiate from (up to four rounds for deeper chains). A base written through a typedef (`BRepExtrema_TriangleSet : BVH_PrimitiveSet3d`) or with defaulted arguments (`BVH_PairTraverse<double, 3>`) is named as the instantiation is (canonical arguments). What still cannot be instantiated — the empty CRTP base `BVH_BaseBox<T, N, BVH_Box>` with its template template parameter and a partial specialisation holding the members, `NCollection_UBTree<int, Bnd_Box>::Selector` (a nested class of an instantiation) — is **dropped from the derived class's bases** (reported; the base's members are not inherited: `BVH_Box.Transform/Transformed`, the `Selector` interface of the internal `*BndBoxTreeSelector*` classes) instead of skipping the class; a Transient class whose only path to `Standard_Transient` was such a base is skipped. Whether an instantiation is abstract only the compiler can tell (`BVH_PrimitiveSet<double, 3>` through `BVH_Set`'s pure virtuals): its constructors are registered inside `nanoocp_if_concrete<T>` (a generic lambda, instantiated only when `!std::is_abstract_v<T>`). Two template bodies OCCT cannot compile for the argument are in `overrides.toml`: `BVH_PairTraverse<…, void, double>::Select()` and the whole `BOPTools_PairSelector<2>` (an OCCT bug). This binds the BVH chain end to end: `BRepExtrema_ShapeProximity` with `ProxPntStatus*`, `ElementSet1/2` (`BRepExtrema_TriangleSet`), `OverlapSubShapes1/2`, `BRepExtrema_ProximityDistTool/OverlapTool`, `BOPTools_BoxTree`, `IntPatch_PolyhedronBVH`.
- A private member typedef used in a public signature (`BRepGraph_MutGuard::TypeId`) is spelled by its underlying type.

#### Nested templates and dependent names (2026-09-20, for BRepGraph)

- The template may be nested in a class or namespace (`BRepGraph_NodeId::Typed<Kind::Face>` = `BRepGraph_FaceId`, `BRepGraph_RefsIterator::RefIterator<…>`): the definition is found by descending every reopening of the enclosing scopes, and the injected class name maps to the full instantiation when written bare, to the qualified template name when written with arguments (`Typed<TheKind>`).
- Names the template writes unqualified are qualified during the walk: its own member types (`using TypedId = …; TypedId CurrentId()` → `BRepGraph_Iterator<…>::TypedId`, valid C++ once the instantiation is concrete) and types/templates of the enclosing scopes (`DefTraits<IdType>` → `BRepGraph_ReverseIterator::DefTraits<…>`). A qualified spelling of another template with the same leaf name (`BRepGraph_RefId::Typed`) is left alone.
- Defaulted template arguments come from the parameter's default (`bool IsFull = false`); one libclang cannot spell at all (`NCollection_AliasedArray<>`) stays out of the name but is substituted.
- libclang exposes no members on an instantiated specialisation cursor (verified: zero children), so walking the definition is the only route.
- Dependent results: `T&` written as such becomes a mutable reference (`reference_internal`, class element types only); a pointer, or a typedef hiding one (`LinearVector<T>::iterator`), is skipped — nanobind would take ownership of an element — except `const char*` (`NCollection_String::ToCString`).
- Partial `std::hash<Tmpl<K>>` specialisations give `__hash__` to every instantiation; `template <> struct std::hash<X>` written at file scope (semantic parent `std::__1`) is recognised like the `namespace std {}` form.

## 7. Build and packaging

- **`CMakeLists.txt`** at the root: `find_package(OpenCASCADE)` from `NANOOCP_OCCT_DIR` (default `deps/occt-8.0.1`), one `nanobind_add_module` per toolkit from `src/cpp/toolkits.cmake`, `INSTALL_RPATH` pointing at the OCCT lib dir for development builds.
- **`pyproject.toml`**: scikit-build-core, `wheel.py-api = "cp312"`, `build-dir = "build/{wheel_tag}"` (incremental rebuilds), `wheel.packages = ["src/nanoocp"]`.
    - On macOS `CMAKE_OSX_DEPLOYMENT_TARGET = "11.1"` (scikit-build override), the same as OCCT's, so the `.abi3.so` carries `minos 11.1` (verified with `otool -l`; without it the SDK's 26.0 was inherited).
    - The generated targets compile with `-Wno-deprecated-declarations` / `/wd4996` because deprecated members are bound on purpose (6, R-DEPRECATED).
    - Development loop: regenerate → `uv sync --reinstall-package nanoocp` → `pytest` (commands in 9).
- **Wheels**: bundling OCCT dylibs (delocate/auditwheel/delvewheel) is not done yet.
- **Tests**:
    - `tests/test_<TK>.py` per toolkit against the built bindings, each generator rule exercised at least once;
    - `tests/test_generator.py` tests the generator itself — the IR of a synthetic header with one member per §6 rule (`parse_package` on a private include directory, no compiler), the overload-collision resolver, the report categories, the header allowlist, a scan of the checked-in stubs for overloads with identical Python signatures (6.4), and a regeneration of `TKG2d` into a temporary directory that must reproduce `src/cpp/TKG2d` byte for byte (the canonical-state check, ~5 s);
    - `tests/test_typing.py` runs mypy and ty on `tests/typing/check_*.py` (6b).

## 8. Open questions and next steps

### Open

1. `ModelingAlgorithms`, then Phase 2 and the font slice (the ordered plan is in section 9, "Next steps").
2. Generator on Linux and Windows (libclang selection, MSVC/libstdc++ header discovery, platform-dependent `#ifdef`s in OCCT headers such as `OSD_*`).
3. Vendor RapidJSON; decide whether to vendor the ~23 clang builtin headers so the pip `libclang` fallback works without a host clang.
4. Wheel bundling and CI matrix (the deployment target is set, 7).
9. **FreeImage** (found with TKService, 2026-09-22, kept open by the user): without it `Image_AlienPixMap` has exactly one writer and no reader — `Save(path)` is always binary PPM (`P6`, RGB8, alpha dropped, per-pixel; `Image_AlienPixMap.cxx:1313-1328`), `Save(ostream)` and every `Load` return `false` (`:996-1010`, `:1523`); a Windows build without FreeImage uses WIC (`HAVE_WINCODEC`, `:16-18`, not tested). OCCT itself needs a codec only where C++ decodes images: texture import in the glTF/OBJ readers and `V3d_View::Dump` writing PNG directly (with `TKOpenGl`). Everything else can stay Python-side (roadmap 10). Decide when DataExchange shows whether texture import matters; a second compiled dependency would revisit vcpkg (3.2).
10. **Pixel-buffer view as a Python addition (2c)** — expose `Image_PixMap`'s data (`Data()`/`ChangeData()`/`Row()` are raw pointers, 2d) as a buffer-protocol/`nb::ndarray` view of shape `(height, width, channels)` with `keep_alive`, writable for `ChangeData()`, so `numpy.asarray(px)` / `PIL.Image.fromarray(...)` and the reverse (a Pillow-loaded PNG pushed into a pixmap) work without a per-pixel loop. Today the per-pixel route works: `PixelColor()`/`SetPixelColor()` measured at ~0.3 µs/pixel (512×512 RGBA in 0.08 s; 1080p ≈ 0.6 s), or `Save("x.ppm")` + Pillow. Same mechanism for the other byte buffers (`NCollection_Buffer`, `FSD_Base64`, glTF/STL buffers — 8a "revisited with DataExchange"). First check: whether `nb::ndarray` works under the stable ABI (*unverified*). Pixmap row order (`IsTopDown()`) must be documented with it.

### Roadmap

5. **Python-side subclassing of abstract OCCT interfaces (nanobind trampolines)** — `math_Function`/`math_MultipleVarFunction` (the classic `math_BFGS`, `math_NewtonMinimum`, `math_FunctionRoot` are bound but need a Python-defined function), `Adaptor3d_Curve`/`Adaptor3d_Surface`, `Message_Printer`. This is the answer to the 249 functor-template lines of the report (`MathOpt::BFGS<F>` & co. need a C++ functor type and stay out, decision 2026-09-21): one rule "an abstract class with public virtuals gets a trampoline" makes the classic algorithms usable from Python. A subsystem of its own (trampolines, GIL, lifetime of Python-held objects referenced from C++); not needed by build123d; after Phase 1.
6. **An OCP compatibility shim.** A generated package that mimics cadquery-ocp's API on top of nanoOCP: `_s` aliases for every static method, `OCP.collections`-style container names, the `TopoDS` class-like object, flat exceptions — generated from the manifest, explicitly non-1:1, in its own distribution. Stretch goal: name the package `OCP` so that build123d's (and CadQuery's) own test suites run against nanoOCP **without any change** — the strongest possible integration test for nanoOCP, and a migration path for those projects. Not before Phase 1 and DataExchange are generated (the shim is only as complete as the bindings under it). The rename table in 8b is the specification's starting point.

### Decided

7. ~~The four container instantiations build123d constructs directly~~ — all arrived without an `[instantiate]` entry: `HArray1<bool>` with TKGeomAlgo (`Law`), `DataMap<TopoDS_Shape, TopoDS_Shape, TopTools_ShapeMapHasher>` with TKTopAlgo (`BRepLib`), `HSequence<TopoDS_Shape>` (`ShapeExtend`) and `Sequence<TopoDS_Shape>` (`ShapeFix`) with TKShHealing (2026-09-21).
8. ~~R-COLLISION losers that matter~~ — decided 2026-09-21: every colliding overload with out-parameters is bound under a typed suffix (6, R-COLLISION); nothing is unreachable any more.

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
| 551 | function/class templates and template members: functor-based algorithms (`MathOpt::BFGS<F>`, `MathRoot::Newton<F>`, `MathInteg::*`, `MathSys::Newton<F>`), `NCollection_MapAlgo`/`PackedMapAlgo` set algebra, `IsValidIn<CountProviderT>` | the one *chosen* gap: needs Python callables (trampolines, roadmap 8.5); the classic `math_*` classes cover the same ground |
| 126 | STL-style iterators (`begin()`/`end()`, `DynamicIterator` overloads) | Python iterates with `__iter__` (containers, and R-ITER on `More`-`Next`-`Value` classes) |
| 125 | raw pointers to primitives: 67 `AdvApp2Var` Fortran-style internals, buffers (`NCollection_Buffer`, `FSD_Base64`), `char16_t*` non-const | inherent; byte buffers revisited with DataExchange (Phase 2) |
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
3. Functor templates stay out unless Python callables become a goal (roadmap 8.5).

## 8b. Porting from OCP (cadquery-ocp) to nanoOCP

For build123d and CadQuery-style code. OCP is pybind11-based and binds OCCT 7.x/8.x with its own conventions; nanoOCP is 1:1 with OCCT 8.0.1 and documents every deviation in section 6. What changes (evidence: the build123d inventory in `reviews/review-2026-09-20.md`, 285 OCP names at 84 packages):

| OCP | nanoOCP | Note |
|---|---|---|
| `from OCP.gp import gp_Pnt` | `from nanoocp.gp import gp_Pnt` | package modules are the same; `import nanoocp` imports every toolkit eagerly |
| `BRep_Tool.Surface_s(face)` — every static method carries `_s` | `BRep_Tool.Surface(face)`; `_s` only where an instance method of the same name exists (`TDataStd_Name.Set_s`, `gp_QuaternionNLerp.Interpolate_s`) | 185 call sites in build123d; a blind strip is wrong for the genuine collisions (report category `static-rename` lists them) |
| `BRep_Tool.Curve_s(edge, float(), float())` — `double&` kept as dummy inputs, only the handle returned | `curve, first, last = BRep_Tool.Curve(edge)` | non-void functions with out-parameters return a tuple, result first (R-OUT) |
| `param_min, _ = BRep_Tool.Range_s(edge)` | `param_min, _ = BRep_Tool.Range(edge)` | unchanged |
| `BRepGProp_Face(face).Normal(u, v, pnt, vec)`, `TopExp.Vertices_s(edge, v1, v2)` | same without `_s` | class references are mutated in place (R-REF-CLASS) |
| `wires = TopTools_HSequenceOfShape(); ShapeAnalysis_FreeBounds.ConnectEdgesToWires_s(edges, tol, False, wires)` | `wires = ShapeAnalysis_FreeBounds.ConnectEdgesToWires(edges, tol, False)` | a `handle<T>&` parameter is returned (R-OUT-HANDLE); the OCP form used the deprecated overload; nanoOCP binds deprecated members too (with the note), but the handle& parameter becomes the result there as well |
| `OCP.collections.Array1_gp_Pnt`, `List_TopoDS_Shape`, `IndexedMap_TopoDS_Shape_TopTools_ShapeMapHasher` (OCP 8) / `TColgp_Array1OfPnt`, `TopTools_ListOfShape` (OCP 7) | `NCollection_Array1[gp_Pnt]`, `NCollection_List[TopoDS_Shape]`, concrete `NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher`; the 7.x typedef names resolve too (`nanoocp.TopTools.TopTools_ListOfShape`) | 6a; a custom hasher is reachable only by the concrete name or the 7.x alias |
| `from OCP.TopoDS import TopoDS; TopoDS.Vertex_s(shape)` | `import nanoocp.TopoDS as TopoDS; TopoDS.Vertex(shape)` | `TopoDS` is a C++ namespace in OCCT 8 = the package module (5.1); a wrong type raises `Standard_TypeMismatch` |
| `TopAbs_FACE`, `GeomAbs_C0`, `Font_FA_Bold`, `Graphic3d_HTA_LEFT` at module level | same (R-ENUM exports unscoped enumerators); `TopAbs_ShapeEnum.TopAbs_FACE` works too | |
| `if handle is None`, `shape.IsNull()` | unchanged | null handle ↔ `None` (R-HANDLE); `None` is accepted wherever a handle is expected |
| `except (Standard_Failure, Standard_ConstructionError, StdFail_NotDone)` | `except Standard_Failure` catches all of them | a real hierarchy (4.2); the derived classes still exist |
| `BinTools.Write_s(shape, io.BytesIO())` / `Read_s(shape, io.BytesIO(data))` (pickling) | `data = BinTools.Write(shape)` (`bytes`); `BinTools.Read(shape, io.BytesIO(data))` | `std::ostream&` → returned `bytes` for the binary packages, `std::istream&` ← `io.BytesIO` (R-STREAM-OUT/IN); byte-identical to the file form (verified) |
| `BRepTools.Write_s(shape, path)`, `Read_s(shape, path, builder)` | same without `_s` | the path overloads are untouched |
| `ics.Parameters(i, float(), float(), float())` — dummies for the `double&` of one of two overloads with the same inputs | `u, v, w = ics.Parameters__float__float__float(i)`; `pnt.Coord()` stays `gp_XYZ`, the three floats are `pnt.Coord__float__float__float()` | R-COLLISION: overloads that differ only in their out-parameters carry a suffix naming those out-parameters' types |
| `while ex.More(): … ex.Next()` | `for s in ex:` works too | R-ITER: `More`/`Next`/`Value` classes are their own iterator |
| `Geom_BSplineCurve.Poles(array)` (deprecated out-into-array form) | still available, docstring starts with `Deprecated in OCCT: use Poles() returning const reference instead` | R-DEPRECATED |
| `kernel.py`'s workaround for slow `List_TopoDS_Shape` iteration | not needed: `list(NCollection_List[TopoDS_Shape])` measured at 0.2 µs | |
| `TDF_Label`, STEP/IGES/STL, XCAF | Phase 2 | not generated yet |

Pickling: nanoOCP objects are not picklable by themselves (like OCP's); build123d's `copyreg` approach keeps working with the `BinTools` change above. A `nanoocp.compat.ocp` module that adds the `_s` aliases and the `OCP.collections` names for a transition is possible (generated from the manifest) but would be a separate, explicitly non-1:1 module (8).

## 9. Working state and how to continue (kept current for context resets)

### State on 2026-09-22

Branch `main`, no remote; Phase 1 complete and gap-reviewed (2d); Phase 2 started with `TKService` (the first Visualization toolkit, whole); the roadmap is in 8.

- **Phase 2 order (decided 2026-09-22, §2):** `TKService` ✓ → `TKV3d` → `TKCDF` → `TKLCAF` → `TKCAF` → `TKVCAF` → `TKBinL` → `TKBin` → `TKXmlL` → `TKXml` → `TKDE` → `TKXSBase` → `TKXCAF` → `TKDESTEP` (1 089 headers, the largest toolkit in scope) → `TKDEIGES` → `TKDESTL` → `TKRWMesh` → `TKDEGLTF`, `TKDEOBJ`, `TKDEPLY` → `TKDEVRML` → `TKBinXCAF`, `TKXmlXCAF`; afterwards `TKMeshVS` and `TKOpenGl` (OCCT rebuild). Header counts per toolkit: `TKV3d` 289 (`AIS` 65, `Prs3d` 38, `SelectMgr` 35, `PrsDim` 32, `StdPrs` 28, `DsgPrs` 26, `Select3D` 23, `V3d` 22, `StdSelect` 11, `PrsMgr` 6, `SelectBasics` 3), `TKCDF` 61, `TKLCAF` 102, `TKCAF` 45, `TKVCAF` 11, `TKBinL` 49, `TKBin` 14, `TKXmlL` 48, `TKXml` 14, `TKXSBase` 226, `TKXCAF` 71, `TKDEIGES` 461, `TKDEVRML` 102, the rest ≤ 25.
- **TKService** (10 packages, 207 classes, 103 enums, 2 810 methods; 291 report lines, 2d rows added): the font manager (`Font_FontMgr.FindFont` returning the in/out aspect, 2 381 system fonts on this machine), `Font_FTFont` with FreeType metrics and the `char32_t` code-point API, `Font_TextFormatter` + its `Iterator`, `Graphic3d_MaterialAspect`, the `NCollection_Vec*`/`Mat*` instantiations with their hidden-friend operators, `Image_PixMap` pixel access, `Graphic3d_SequenceOfHClipPlane.Iterator`, `Graphic3d_ArrayOfPrimitives`. Generator rules added: hidden friends (R-FREE-OP), alias enumerators (R-ENUM), bit-fields (R-FIELD), references to headerless types (R-PTR-INCOMPLETE), enclosing-class defaults (R-DEFAULT-QUAL), `char32_t` (R-CHAR16), width twins with out-params (R-COLLISION), binder iterators as iterators (R-ITER), classes deriving from a binder Iterator (6a), deprecated typedefs of 6c instantiations (6a), multi-word casts (6c), concrete `Iterator` stubs (6b). Five of these were Phase-1 gaps that nothing reported (friend operators, alias enumerators, the `Graphic3d_Vec3`-style typedefs, `Value()` typed `Never`, binder iterators not iterable).

- **Generated, built, stubbed:** FoundationClasses and ModelingData complete — `TKernel` (18 packages), `TKMath` (21), `TKG2d` (6), `TKG3d` (8), `TKGeomBase` (27), `TKBRep` (10, incl. `BRepGraph`/`BRepGraphInc` with their typed ids and iterators) — and the first two ModelingAlgorithms toolkits `TKGeomAlgo` (33 packages, 355 classes, 3 492 methods; 72 report lines) and `TKTopAlgo` (16 packages, 166 classes, 1 653 methods; 47 report lines: the `BRepBuilderAPI` makers with `TopoDS_Shape(aMaker)`, `BRepGProp`, `BRepCheck`, `BRepExtrema` minus the BVH-based proximity tools, `BRepBndLib`, the classifiers, `BRepLib`, the 2D medial axis), and `TKPrim` (5 packages, 35 classes, 301 methods; 8 report lines: `BRepPrimAPI_MakeBox/Cylinder/Sphere/Cone/Torus/Wedge/Prism/Revol`, `BRepPrim_*` builders, `TopoDS_Solid(aMakeBox)`/`TopoDS_Shell(…)`/`TopoDS_Face(aMakeOneAxis)` conversions; volumes verified analytically) — the `BRepPrimAPI_MakeBox` milestone — and `TKShHealing` (11 packages, 111 classes, 1 415 methods; 12 report lines: `ShapeAnalysis_FreeBounds.ConnectEdgesToWires` returning the `HSequence`, `ShapeFix_Shape`, `ShapeUpgrade_UnifySameDomain`, `ShapeCustom.ScaleShape`; `HSequence`/`Sequence<TopoDS_Shape>` arrive here, closing 8.7), and `TKBO` (5 packages, 141 classes, 1 156 methods; 49 report lines: `BRepAlgoAPI_Fuse/Cut/Common/Section/Splitter/BuilderAlgo`, `BOPAlgo_BOP`, `BOPDS`, `IntTools`; the BVH box trees of `BOPTools` stay out), and `TKBool` (7 packages, 170 classes, 2 067 methods, 219 free functions; 47 report lines: `BRepFill` lofts/pipes, `BRepAlgo`, `BRepProj`, the `TopOpeBRep*` kernel with its `FUN_*` helpers), and `TKHLR` (8 packages, 107 classes, 1 215 methods; 136 report lines, 91 of them `HLRBRep`'s raw-pointer curve/surface accessors: `HLRBRep_Algo` + `HLRBRep_HLRToShape` hidden-line removal works, `HLRBRep_PolyAlgo` needs a mesh from TKMesh), and `TKHelix` (2 packages, 7 classes, 47 methods; nothing unbound: `HelixBRep_BuilderHelix`, `HelixGeom_HelixCurve`), and `TKMesh` (4 packages, 84 classes, 549 methods; 97 report lines: `BRepMesh_IncrementalMesh` + `IMeshTools_Parameters`, the `IMeshData` interfaces with first base only, the `BRepMeshData_*` implementation classes skipped), and `TKFillet` (9 packages, 87 classes, 1 632 methods, 99 free functions; 14 report lines: `BRepFilletAPI_MakeFillet/MakeChamfer` verified on a cube, `ChFi2d`, the `Blend*` functions), and `TKOffset` (4 packages, 31 classes, 391 methods; 2 report lines: `BRepOffsetAPI_MakeThickSolid/MakeOffsetShape/ThruSections/MakePipe/MakeOffset/DraftAngle` verified on volumes), and `TKFeat` (2 packages, 35 classes, 301 methods; 5 report lines: `BRepFeat_MakePrism` as pocket and boss), and `TKXMesh` (1 class, nothing unbound) — **ModelingAlgorithms complete** (14 toolkits; `TKExpress` out of scope).
- **Tests:** 390 pass (`tests/`, incl. generator unit tests, a byte-for-byte regeneration test of `TKG2d`, the re-homing guard and the stub scan), mypy and ty included.
- **Coverage:** every omission is tabulated in 8a and persisted in `src/cpp/<TK>/report.txt`.
- **Rules in place:** 15 NCollection binder kinds (6a), class-template aliases and on-demand instantiations incl. nested/dependent templates (6c), C++ namespaces as (sub)modules, nested classes, typedef aliases, conversion operators, `__hash__` from `std::hash`, implicit copy constructors, overload collisions resolved by typed `__` suffixes (R-COLLISION), const twins skipped (R-CONST-TWIN), wider scalar overloads first (R-WIDTH), `__iter__` on `More/Next/Value` classes (R-ITER), `using Base::name` re-exports (R-USING), mutable primitive references with `Set<Name>`/`__setitem__`, streams (`ostream&` → `str`, `istream&` ← `typing.TextIO`), `handle<T>&` out-parameters, `None` for every handle parameter, unscoped enumerators exported, deprecated members bound with OCCT's message, `char16_t` casters, non-copyable classes via a wrapper (4 classes), nested enums of a skipped class skipped with it (5.2). Every §6 rule has an identifier (`R-…`) cited at its code sites.
- **The checked-in sources are the clean-regeneration state** (`rm src/cpp/manifest.json`, toolkits in order), which is reproducible byte for byte.

### Seen with TKService (2026-09-22)

- The incremental first run re-homed 20 instantiations (`NCollection_Vec3<float>` from `Quantity` to `Graphic3d`, …) and a later `--package Quantity` run then broke the TKMath import (`no attribute 'NCollection_Vec3__float'`): after a `--allow-rehoming` run, never regenerate an *earlier* package incrementally — go straight to the clean regeneration.
- The clean regeneration must be run **twice** when the generator changed: the second run's diff (only the files the last generator change touches) is the idempotence proof; the per-toolkit script is in the memory notes (`finish_tk.sh`; `diff | head` under `pipefail` aborts the script — write the diff to a file).
- nanobind facts verified: `export_values()` skips alias enumerators (Python `Enum` iteration); a bit-field has no pointer-to-member (compile error in `def_rw`); `typeid` of a forward-declared type without a definition fails in the caster (`AVStream&`); `PyUnicode_FromKindAndData` is outside the limited API (`PyUnicode_DecodeUTF32` is in).
- OCCT facts: `Font_FontMgr::FindFont` prints its fallback warning unconditionally (`Message::SendWarning`, `Font_FontMgr.cxx:1114`; the test raises the printers' trace level); `Font_FTFont::AdvanceX(next)` is 0 before a glyph was loaded — use `AdvanceX(char, next)`; `Image_AlienPixMap::Save` writes PPM without FreeImage (3.1).

### ModelingAlgorithms: toolkit order and expectations

- Dependency order from `EXTERNLIB.cmake` (it differs from `TOOLKITS.cmake`): TKGeomAlgo ✓ → TKTopAlgo ✓ → TKPrim ✓ → TKShHealing ✓ → TKBO ✓ → TKBool ✓ → {TKHLR ✓, TKHelix ✓, TKMesh ✓, TKFillet ✓} → TKOffset ✓, TKFeat ✓, TKXMesh ✓ — all done 2026-09-21.
- `TKExpress` links only TKernel and holds `Expr`/`ExprIntrp`, OCCT's symbolic expression parser — not used by STEP (`TKDESTEP` does not link it), nor by build123d/CadQuery: out of scope.
- A parse survey of the whole module (scratch script, 18 s with bodies skipped) found only two non-self-contained headers (R-PRELUDE).
- Arrived as predicted: `BOPDS_*`/`BOPTools_Set` `std::hash` (TKBO), the multi-base `IMeshData_*` classes with their first base (TKMesh), the `ChFiDS_ChamfMode.hxx` prelude for `ChFiKPart` (TKFillet).
- Seen with TKTopAlgo: the BVH-based classes (`BRepExtrema_OverlapTool`, `_ProximityDistTool`, `_TriangleSet`) stayed out until R-TEMPLATE-BASE (6c, 2026-09-21) instantiated their template bases; the `*BndBoxTreeSelector*` classes bind without their `NCollection_UBTree::Selector` base (internal to the classifiers); a class that holds a non-copyable member by value needs its own `[skip] noncopyable` entry (R-NONCOPYABLE); `BRepTopAdaptor_FClass2d.Perform` classifies the centre of a 10 × 5 face as `ON` — OCP 7.9.3 gives the same, OCCT semantics; a header that forward-declares `math_VectorBase` and re-aliases `math_Vector` (`BRepGProp_Gauss.hxx`, `IntPatch_SpecialPoints.hxx`, `Extrema_FuncPSDist.hxx`) adds two harmless `template` lines to its package's report (`math_Vector` is bound by TKMath).
- Seen with TKXMesh: `XBRepMesh_Factory()` from Python segfaults — OCCT's constructor registers `this` through a temporary handle, finds the name registered at library load and the temporary deletes the half-built object (plain C++ shows a garbage refcount and a null name); `BRepMesh_DiscretAlgoFactory.FindFactory("XBRepMesh")` is the way in.
- Seen with TKPrim: nothing new for the generator; OCCT semantics to know when testing — `BRepPrimAPI_MakeBox::Solid()` builds a fresh solid on every call and `Shell()` replaces the result of `Shape()` (`BRepPrimAPI_MakeBox.cxx:148,165`); `Shape()` returns the declared `TopoDS_Shape`, the typed accessors and conversions (`TopoDS_Solid(aMakeBox)`) give the sub-class. The `OneAxis()` accessors return `Standard_Address` (`void*`, not bound).

### Development loop

The venv is `.venv`, managed by `uv`; `deps/occt-8.0.1` and `deps/freetype` are built, `deps/occt-build` is the ninja tree for incremental OCCT rebuilds.

```bash
uv run python -m generator --toolkit TKernel          # regenerate one toolkit (all packages); --package X for one package
rm src/cpp/manifest.json && uv run python -m generator --toolkit TKernel --toolkit TKMath --toolkit TKG2d --toolkit TKG3d --toolkit TKGeomBase --toolkit TKBRep --toolkit TKGeomAlgo --toolkit TKTopAlgo --toolkit TKPrim --toolkit TKShHealing --toolkit TKBO --toolkit TKBool --toolkit TKHLR --toolkit TKHelix --toolkit TKMesh --toolkit TKFillet --toolkit TKOffset --toolkit TKFeat --toolkit TKXMesh   # clean regeneration, 90 s (idempotent byte for byte, verified 2026-09-21)
uv sync --reinstall-package nanoocp                    # build + install (scikit-build-core, build dir build/{wheel_tag}), ~30 s wall
uv run python -m generator.stubs                       # .pyi stubs (after the build; imports the extension)
uv run pytest tests -q
```

Per new toolkit: generate (`--allow-rehoming` is legitimate for a *new* toolkit when the earlier ones are in their clean state — nothing before it can own the new instantiations), build, smoke test, `tests/test_<TK>.py`, watch `report.txt` — **sort its lines with the 2d criteria (internal only / no Python equivalent / workaround → add the row to 2d / undefined) and treat anything left as a gap to close** — then a clean regeneration before the commit.

### Canonical regeneration and the re-homing guard

- Generation order matters the first time after deleting `src/cpp/manifest.json`: dependencies first (`TKernel`, then `TKMath`, …), because the manifest carries bound classes/instantiations across runs.
- Regenerating everything: `rm src/cpp/manifest.json` then all toolkits in dependency order. **Do that before every commit**: an on-demand instantiation (6c, and the NCollection instantiations of 6a) is bound by the first package that needs it, so an incremental run can leave it in a different package than a clean run does (`NCollection_Vec3<float>`: `Quantity` in a clean run, `BVH` after an incremental one); the clean order is canonical and reproducible byte for byte (`tests/test_generator.py` checks `TKG2d`).
- Since 2026-09-21 an incremental run **refuses** to bind an instantiation for the first time when a toolkit that is not being regenerated precedes the binding toolkit and could own it (`rehoming: … not regenerated`, exit 1, nothing written; `--allow-rehoming` overrides; only toolkits at or after the latest toolkit of the instantiation's argument types count).
- A fully canonical incremental run would need to re-parse the owner packages, i.e. the full 22 s parse of all 90 packages — the ritual plus the guard was chosen instead (decision log).
- A faster compile-only check without installing: `cmake --build build/dev` (configured with `-DPython_EXECUTABLE=$PWD/.venv/bin/python -DCMAKE_INSTALL_PREFIX=$PWD/build/stage`).

### Debugging a nanobind "Critical nanobind error" at import

Release builds hide the message.

- Build the Debug tree `build/debug`: `cmake -S . -B build/debug -G Ninja -DCMAKE_BUILD_TYPE=Debug -DPython_EXECUTABLE=$PWD/.venv/bin/python -DCMAKE_INSTALL_PREFIX=$PWD/build/stage-debug`, `cmake --build build/debug`, `cmake --install build/debug`, copy `src/nanoocp/*.py` into `build/stage-debug/nanoocp/`.
- Then `PYTHONPATH=build/stage-debug .venv/bin/python -S -c "import nanoocp._TKMath"` — `-S` is required because the editable-install `.pth` hook would otherwise load the Release module.
- For a C++ exception at init: `lldb --batch -o "break set -E c++" -o run -o "bt 12" -- .venv/bin/python -S -c "import nanoocp._TKernel"`.

### Recurring pitfalls

- safe-chain hides packages younger than 48 h from `uv`; the user overrides it themselves (nanobind is in the exclusions now).
- A `str.replace(old, new)` with an empty `old` inserts `new` between every character — it happened once to `parse.py` and was recovered exactly; use asserts on anchors.
- Partial regeneration of a single package is safe (toolkit module stays complete, manifest entries of the package are refreshed).
- Every new package tends to reveal one or two OCCT-specific idioms: the report printed by the generator (`- …: reason`, persisted as `src/cpp/<TK>/report.txt`; watch its `git diff` after a regeneration and the `misc` category) is the place to look, and the compiler/linker tells the rest.
- The review of 2026-09-20 (`reviews/`, git-ignored) lists the remaining *Should*/*Could* items (8).

### Coverage of FoundationClasses/ModelingData

See 8a (1 484 classes, 14 756 methods; every omission categorised).

### Next steps, in order

1. ~~ModelingAlgorithms~~ — complete (Phase 1 generated). Python subclassing of `Adaptor3d_Curve` remains on the roadmap (8.5), not in Phase 1.
2. Conversion operators whose target lives in a later toolkit (`Quantity_Color` → `NCollection_Vec3<float>`) could be emitted from the target's package via the manifest if wanted.
3. Phase 2 in the order above: `TKV3d` next (whole toolkit; `StdPrs_BRepFont`/`StdPrs_BRepTextBuilder` are build123d's text path — the smoke test), then the ApplicationFramework subset (`BinLDrivers`, `BinMDF`, … into `overrides.toml [stream] binary_packages`), then DataExchange.
4. Linux/Windows runs of the generator and the wheel pipeline (bundle OCCT dylibs; the static FreeType is inside `libTKService`); the FreeImage decision (8.9) and the `TKOpenGl` rebuild.

## Decision log

Chronological; the test count of each entry is the tie-breaker within a day. Details live in the sections the entries point to.

### 2026-09-20

- **2026-09-20** — nanobind stable ABI (linked mode, 3.12+) chosen over split mode; PoC verified against OCCT (`poc/`).
- **2026-09-20** — `handle<T>` caster with intrusive refcount + `keep_alive_cb`, constructors via `nb::new_` (verified lifetime semantics).
- **2026-09-20** — One extension per toolkit, Python namespace per package (`nanoocp.gp.gp_Pnt`), out-params → tuples (user decisions).
- **2026-09-20** — Local OCCT build from `V8_0_1` with Apple clang, no conda; exceptions enabled; OpenGL/X11/Tk/TBB/VTK/Draw off.
- **2026-09-20** — Fonts are in scope (user needs text-to-BRep) → FreeType required; built statically from source; fontconfig on Linux accepted.
- **2026-09-20** — vcpkg declined for now (single compiled dependency); revisit if the list grows.
- **2026-09-20** — Generator: libclang AST, system libclang preferred over the pip wheel; type spellings as written; two-phase declare/define; manifest for cross-run base checks; `_s` suffix for mixed static/instance names; `overrides.toml` for in/out parameters. First package `gp` generated and tested (13 tests).
- **2026-09-20** — TKernel generated (18 packages, 44 tests). New rules: Transient pointer/reference returns wrapped in handles, `reference`/`reference_internal` policies, constructibility from `operator new` accessibility, exception translation by dynamic type name across DSOs (replaces `nb::exception`), implicit conversions from non-explicit constructors, defaults cast to the parameter type and qualified, package declaration order by base dependencies, `skip.headers`/`skip.methods` overrides, STL casters.
- **2026-09-20** — NCollection containers: option (b) hand-written binders; `Array1`/`HArray1` done (53 tests). Instantiations from signature scanning, home = element package, eager toolkit import, deprecated typedef aliases, docstrings extracted from the template header, coverage check.
- **2026-09-20** — `NCollection_Xxx[T]` accessor as primary spelling; concrete names with `__` separators; all instantiations homed in `nanoocp.NCollection`; type stubs (stubgen + generic container classes) verified with mypy and ty. mypy and ty added as dev dependencies (user request).
- **2026-09-20** — NCollection `List`, `Sequence`, `HSequence` binders with nested iterators (62 tests); packages emitted in declaration order.
- **2026-09-20** — NCollection hashed kinds (`Map`, `DataMap`, `IndexedMap`, `IndexedDataMap`) with default-hasher stripping, `[instantiate]` override, enums as element types (68 tests).
- **2026-09-20** — Multiple-inheritance rule discovered and fixed (offset-0 base + MI registry in the handle caster); `Array2`, `HArray2`, `DynamicArray`, `DoubleMap`, `Shared` bound — all 14 NCollection kinds done (72 tests).
- **2026-09-20** — Rest of `TKMath` generated (21 packages, 98 tests): namespaces descended (constants bound, templates reported), anonymous enums as constants, `nm`-based check for declared-but-undefined methods (full-body parsing), first-base-only rule for multi-base classes, array parameters skipped, template arguments respelled recursively (nested types), non-type template arguments kept as written, `math_GlobOptMin` skipped. Open: aliases of OCCT class templates (`math_Vector`, `Extrema_ExtPC`, …).
- **2026-09-20** — Aliases of OCCT class templates instantiated from the header (6c): `math_Vector`, `Bnd_B*`, `BVH_Vec*`, `TColStd_PackedMapOfInteger`, … (99 tests). Partial regeneration (`--package`) keeps the toolkit module complete (package order stored in the manifest).
- **2026-09-20** — `TKG2d` generated (6 packages, 118 tests). C++ namespaces bound: package-named namespace = package module, others = submodules backed by Python sub-packages (`nanoocp/<pkg>/<ns>.py`, stubs alongside); `std`/`detail`/`Detail`/`Internal` skipped via `overrides.toml`. Public nested classes bound into their outer class. Namespace functions bound (with out-param tuples) and their defaults qualified from AST references. `nm` regex fixed for `operator()` (`Geom2dHash_CurveHasher`, `std::hash` were wrongly reported undefined). Implicit default constructors guarded by `std::is_default_constructible_v`; reference-typed fields skipped. Stubs: concrete container names rewritten to the generic spelling in OCCT signatures; `stubgen` driven through its API. Regenerating `TKernel`/`TKMath` with these rules added the `MathUtils`/`MathLin`/`MathOpt`/`MathRoot`/`MathSys`/`MathPoly`/`MathInteg` namespace functions and `NCollection_Primes`.
- **2026-09-20** — `TKG3d` generated (8 packages, 132 tests): typedefs of bound classes become attribute aliases (`GeomGridEval::CurveD1`), non-self-contained headers are parsed with the missing header included first (`gp_Lin.hxx` for `GeomGridEval_Line.hxx`), overloads that collide after out-param removal are reported (first declared wins — existing behaviour made visible), stubgen's `from X import Nested` bindings for nested-class aliases fixed.
- **2026-09-20** — `TKGeomBase` generated (27 packages, 164 tests): four `GeomBndLib` headers skipped (uninstalled `.pxx`), classes with a declared-but-undefined copy constructor skipped automatically (`nm` signature check), Python keywords as identifiers suffixed (`None_`), stub aliases of imported classes written as assignments (ty does not treat `from X import A as B` as a re-export). The 6c aliases `Extrema_ExtPC`, `Extrema_ExtCC`, `GeomLProp_CLProps` work as predicted; deprecated `GCE2d_*` class aliases resolve to the `GC_*2d` makers.
- **2026-09-20** — `TKBRep` generated (10 packages, 179 tests; ModelingData complete): implicit copy constructors bound (`TopoDS_Shape(aVertex)`), `__hash__` from OCCT's `std::hash<T>` specialisations, fields through a compile-time `def_rw`/`def_ro` helper, classes with members of incomplete type skipped, members whose default argument has an unbound type skipped (import would abort with `std::bad_cast`), nested types in defaults qualified. Package instantiations are registered before members are emitted. BRepGraph's namespace-nested class templates stay unbound (reported).
- **2026-09-20** — BRepGraph made usable (182 tests): 6c extended to class templates nested in classes/namespaces, member and enclosing-scope names qualified during the walk, defaulted template arguments, un-aliased template base classes instantiated on demand, dependent `T&`/`T*` results handled, partial `std::hash` specialisations and file-scope `std::hash` recognised, conversion operators bound (`__bool__`/`__int__`/`__float__`, `T(aFrom)` + implicit conversion for class/handle targets, emitted in a fourth phase), classes named like their package keep their path (`manifest.json` `paths`).
- **2026-09-20** — Gap audit of FoundationClasses + ModelingData (184 tests): `char16_t` casters (ExtendedString round trip), `NCollection_LinearVector` binder (15th kind), on-demand 6c for instantiations in signatures, container-typed fields registered, STL-style iterators skipped, `NCollection_Shared` constructors guarded for non-copyable/non-default-constructible `T`. Unregistered types in bound signatures: 275 → 51.
- **2026-09-20** — Overload collisions decided by the result type instead of header order (`BRep_Tool::Parameter(V, E)` → `double`, `gp_Pnt::Coord()` stays a tuple); `math_GlobOptMin` bound through a non-copyable wrapper (185 tests).
- **2026-09-20** — Mutable primitive references (`double& Value(i, j)`) bound as getter + `Set<Name>`/`__setitem__` Python additions (`math_Matrix`, `math_Vector`, `gp_Mat`, `Poly_Triangle`, `BRepTools_ReShape` flags; 186 tests).
- **2026-09-20** — Stream parameters bound: `std::ostream&` → returned `str` (`DumpJson`, `Dump`, `Print`, `BRepTools::Write`; surrogateescape for binary), `std::istream&`/`Standard_SStream&` ← `typing.TextIO` file-like object (never a `str`, to keep the file-path overloads reachable); `InitFromJson`'s stream position is in/out (190 tests). Decision: no `io.BytesIO`/file targets for output — OCCT streams are text and the path overloads cover bulk I/O.

### 2026-09-21

- **2026-09-21** — Review follow-up, *Must* items (195 tests): `nb::arg(...).none()` emitted for every `handle<T>` parameter (was documented, not implemented); unscoped enumerators exported into the enclosing scope (`export_values()`); `handle<T>&` parameters are out-parameters like `double&`, with 7 in/out cases in `overrides.toml` verified against the `.cxx`; the generator report persisted per toolkit as `report.txt` with categories; `--out` into a fresh directory fixed (missing `common/`, toolkit dependencies now from the manifest); the default-expression tidy-up that had slipped into a comment restored (`Message_ProgressRange()` again); Design.md consistency rows 1–6 and 19 of the review fixed, decision log sorted chronologically; `[tool.pytest.ini_options] pythonpath` so tests can import the generator.
- **2026-09-21** — Review follow-up, *Should* items (209 tests): deprecated members bound with OCCT's message as the docstring's first line (R-DEPRECATED, message via `clang_getCursorPlatformAvailability`; a deprecated overload loses a collision); `CMAKE_OSX_DEPLOYMENT_TARGET=11.1` for the extension (`minos 11.1` verified); generator: `binders.py` (data only, all imports top-level, no `parse`↔`ncollection` cycle), `StrEnum`s for the IR kinds, `Emitter.emit()` split into phases with `resolve_overload_collisions()` as a pure function, the 6c substitution state as one `Substitution` object, `[include] packages`/`headers` allowlists for the font slice, `configure_libclang()` idempotent; `tests/test_generator.py` (synthetic-header IR tests per rule, collision resolver, report categories, allowlist, TKG2d regeneration diff); Design.md: 6a/6b/6c in order, rule identifiers `R-…` in §6 cited in the code, font slice defined header by header (§2), "Porting from OCP" (8b), `overrides.toml` reasons per entry, stale code comments fixed, dead `TemplateInstance.element` removed.
- **2026-09-21** — Review follow-up, mechanical *Could* items (209 tests): `stubs.py` reads the manifest once; dead code removed (`ncollection.py` `umbrella`, an empty `elif` in `_unsupported`); free functions returning a mutable class reference now copy the result (R-RESULT) instead of a `reference` without owner; header counts in section 2 recomputed from `FILES.cmake` via `occt.py` with the method stated. Deferred to a decision: deterministic instantiation ownership (needs a full parse per run, measured 22 s of the 28 s), `bytes` for `BinTools`, `nanoocp.compat.ocp`, null-shape guards.
- **2026-09-21** — Decisions on the last review items (210 tests): (1) incremental generator runs keep their speed but fail loudly when they would re-home an instantiation (`--allow-rehoming` to override) instead of a full parse per run; (2) binary formats are `bytes` — `overrides.toml [stream] binary_packages = ["BinTools"]`, `BinTools.Write(shape)` → `bytes`, `Read(shape, io.BytesIO(data))`, `nanoocp::BinaryInput` caster; (3) an OCP compatibility shim (stretch goal: a package named `OCP` so build123d's tests run unchanged) goes on the roadmap (8), not into Phase 1; (4) null-shape behaviour stays faithful to OCCT (R-NULL), no guards.
- **2026-09-21** — `TKGeomAlgo` generated (33 packages, 253 tests; ModelingAlgorithms started): R-CTOR-AMBIGUOUS, R-UNDEFINED by mangled name per overload, R-PRELUDE for undeclared identifiers, skipped-base chain forgotten by the manifest, `[skip] methods` for template bodies that do not compile (6).
- **2026-09-21** — R-COLLISION replaced: colliding overloads with out-parameters bound as `Name__<type>__<type>` instead of picking a winner (2a, 6); numbered suffixes and a hand-picked default rejected; `TKExpress` (`Expr`/`ExprIntrp`) out of scope; skipped 6c instantiations stay in the manifest as `skipped`.
- **2026-09-21** — Silent collisions audited (144 groups in the stubs): R-CONST-TWIN and R-WIDTH (2b, 6); `str`-kind twins unchanged; stub scan as a regression test; dependent `T*` parameters of 6c instantiations now R-UNSUPPORTED (254 tests).
- **2026-09-21** — R-ITER: `More/Next/Value` classes are their own Python iterator (2c, 6; 32 classes, 255 tests). Functor templates stay out, trampolines for abstract interfaces on the roadmap (8.5); raw pointers and stream operators stay out (8a).
- **2026-09-21** — `TKTopAlgo` generated (16 packages, 278 tests): three more classes through the non-copyable wrapper (R-NONCOPYABLE, incl. one holding such a member by value); nested enums and classes of a skipped class leave the manifest with it — no alias, accessor entry or NCollection instantiation names them (5.2; the alias had aborted the import); aliases of skipped types reported (R-ALIAS); `DataMap<TopoDS_Shape, TopoDS_Shape, TopTools_ShapeMapHasher>` arrived (8.7).
- **2026-09-21** — `TKPrim` generated (5 packages, 287 tests): the `BRepPrimAPI_MakeBox` milestone, every primitive and sweep verified against analytic volumes; no new generator rule (9).
- **2026-09-21** — `TKShHealing` generated (11 packages, 301 tests): no new generator rule; the last two build123d container instantiations arrived (8.7 closed).
- **2026-09-21** — `TKBO` generated (5 packages, 311 tests): R-USING — members re-exported with `using Base::name;` are bound on the derived class through lambdas (6; `BRepAlgoAPI_Algo`'s 14 `BOPAlgo_Options` members such as `SetFuzzyValue`/`HasErrors` were silently missing before); inherited constructors (`BRepGraph_FacesOfEdge`) bound the same way.
- **2026-09-21** — `TKBool` generated (7 packages, 322 tests): R-UNDEFINED extended to free functions (two `TopOpeBRepDS` helpers broke the link); `NCollection_TListIterator<T>` in signatures resolves to the List binder's `Iterator` instead of a second registration (6a).
- **2026-09-21** — `TKHLR` generated (8 packages, 332 tests): R-PRELUDE applied to the emitted include list of every package (6); 6c instantiations with a raw-pointer template argument stay out (6c).
- **2026-09-21** — `TKHelix` generated (2 packages, 335 tests): nothing new.
- **2026-09-21** — `TKMesh` generated (4 packages, 343 tests): R-NONCOPYABLE detected by the parser (the four hand-listed overrides retired), classes whose class-level `operator new` hides the placement form skipped when non-trivially copyable (4.2), array references skipped (R-ARRAY), non-const `std::` references returned (R-STL/R-OUT), headers of classes behind typedefs included (5.2).
- **2026-09-21** — `TKFillet` generated (9 packages, 354 tests): nothing new; the ChFiKPart prelude and the `Blend_FuncInv::Set` un-hiding (R-USING) arrived as predicted.
- **2026-09-21** — `TKOffset` generated (4 packages, 360 tests): `NCollection_Handle<T>` members are pointer-like for R-INCOMPLETE (`ThruSections` was skipped).
- **2026-09-21** — `TKFeat` generated (2 packages, 363 tests): nothing new.
- **2026-09-21** — R-TEMPLATE-BASE (6c): template bases of instantiations resolved through a probe re-parse, uninstantiable ones dropped, constructors guarded by `nanoocp_if_concrete`; the BVH chain binds — `BRepExtrema_ShapeProximity` complete (`ProxPntStatus`, `ElementSet`, `OverlapSubShapes`; OCP 7.9.3 cannot return the latter), `ProximityDistTool`, `OverlapTool`, `BOPTools_BoxTree`. Gap 1 of the review closed; all four closed.
- **2026-09-21** — Gap review of Phase 1 with the user's criteria (internal only / no Python equivalent / workaround documented / undefined): 2d added (workarounds, maintained per toolkit); four rules close the rest — R-OPTIONAL-PTR, R-FIXED-ARRAY, R-PTR-REF, R-PTR-INCOMPLETE (2b, 6); `Bnd_OBB.GetVertex()`, `BRepAlgoAPI_BuilderAlgo.Builder()/DSFiller()`, `BOPAlgo_Builder.PDS()`, all four `BRep_Tool.CurveOnSurface` overloads, `BRepFill_AdvancedEvolved.IsDone()` reachable. The BVH chain is the remaining slice.
- **2026-09-21** — `TKXMesh` generated (1 class, 364 tests): ModelingAlgorithms complete. Constructing a second `XBRepMesh_Factory` is undefined behaviour in OCCT itself (the constructor's temporary handle deletes the object; verified in C++): faithful, use the registry (R-NULL).

### 2026-09-22

- **2026-09-22** — Scope: Visualization in except VTK (`TKIVtk`); `TKService` and `TKV3d` as whole toolkits instead of the font slice, Phase 2 order `TKService` → `TKV3d` → AppFW subset → DataExchange, `TKMeshVS`/`TKOpenGl` afterwards (2, 9). User decision after the link-graph evidence (`EXTERNLIB.cmake`).
- **2026-09-22** — `TKService` generated (10 packages, 390 tests): R-FREE-OP for hidden friends, R-ENUM alias enumerators exported, R-FIELD bit-fields, R-PTR-INCOMPLETE for references, R-DEFAULT-QUAL through enclosing/base classes, R-CHAR16 for `char32_t`, R-COLLISION folds R-WIDTH twins, R-ITER on the binder iterators, classes deriving from a binder Iterator declared after the templates phase, deprecated typedefs of 6c instantiations resolved, multi-word casts in 6c defaults, concrete `Iterator` stubs with their own type variables (6, 6a, 6b, 6c); `Font_FontMgr::FindFont` in/out; `WNT_Dword.hxx` skipped; 2d rows for FFmpeg/X11/native-handle/pixel-buffer APIs; FreeImage as open question 8.9.
