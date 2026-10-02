# 9. Coverage of FoundationClasses and ModelingData (2026-09-20)

Part of the nanocct design documents in `docs/`, indexed in [Design.md](Design.md); their section numbers and the `R-…` rule identifiers are shared across them.


Numbers from a fresh generator run of the six toolkits (`python -m generator --toolkit X --out <scratch>`, tree untouched).

## Bound

- 1 484 classes, 14 756 methods, 256 free functions — TKernel 230/2 137/123, TKMath 271/3 789/105, TKG2d 59/892/0, TKG3d 128/2 137/0, TKGeomBase 326/2 426/9, TKBRep 470/3 375/19 (classes/methods/functions).
- Every package of both modules is generated; the OCCT 8 idioms that used to block whole APIs (namespaces, nested classes, nested and dependent templates, conversion operators, streams, mutable primitive references) are handled by rules, not by hand (7, 7c).

## Not bound: 1 360 report lines, all in explainable categories

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

## Usability check

- Bound members whose signature names a type nanobind does not know (grep of quoted annotations in the stubs): 52, down from 275 before the gap audit — STL iterator overloads, `char32_t`/`wchar_t` hashers, `NCollection_FlatDataMap`/`FlatMap` internals of BRepGraph, members of two skipped classes. (`BVH_Box/Set/Tree<double, 3>` were on this list until R-TEMPLATE-BASE, 2026-09-21.)
- Everything else that is bound is callable.

## Carried forward

1. ~~`handle<T>&` out-parameters~~ — rule added 2026-09-21 (section 6).
2. Coverage is verified on macOS only; Linux/Windows generator runs are open (8).
3. Functor templates stay out; Python callables are not a goal (parked as not planned 2026-09-25).
