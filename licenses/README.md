# Third-party licences

nanoOCP's own code is Apache-2.0 (`../LICENSE`). Everything in this directory is the verbatim licence text of something the **binary distribution bundles or compiles in** — not of a build-time-only tool. `../NOTICE` says what each one covers and where its source is; this file records how the list is kept honest.

| File | Component | How it reaches the wheel |
|---|---|---|
| `OCCT-LGPL-2.1.txt`, `OCCT-LGPL-exception.txt` | Open CASCADE Technology 8.0.1 | the `libTK*` shared libraries are bundled, and the generated bindings incorporate material from OCCT headers |
| `FreeType-FTL.txt` | FreeType 2.14.3, **unmodified** | statically linked into `libTKService`, so it is not a separate file in the wheel; `deps/occt-unexported-symbols.txt` keeps its symbols from being re-exported, which does not change the licence obligation |
| `FreeImage-FIPL.txt` | FreeImage 3.19.15, **unmodified** | bundled as its own shared library (`libFreeImage.dylib`/`.so`/`.dll`); it gives OCCT its image codecs |
| `zlib.txt`, `libpng.txt`, `libjpeg-IJG.txt`, `libtiff.txt`, `OpenJPEG-BSD-2-Clause.txt`, `Imath-Half-BSD-3-Clause.txt` | the codecs FreeImage vendors | compiled into `libFreeImage`; built with WebP, the OpenEXR codec, LibRaw and JPEG-XR switched off, and FreeImage vendors no JBIG-KIT |
| `RapidJSON.txt` | RapidJSON 1.1.0 | header-only, compiled into OCCT's glTF reader |
| `nanobind-BSD-3-Clause.txt` | nanobind 3.1.0 | its runtime is compiled into every extension module |
| `robin_map-MIT.txt` | tsl::robin_map | vendored inside nanobind, compiled in with it |

## The rule

**A licence belongs here when its code ends up in the wheel.** Build-time-only tools do not: `scikit-build-core`, `cmake`, `ninja`, `libclang` and the generator's own dependencies shape the build but ship nothing, so they are not listed. Neither do runtime dependencies we merely *import*: `numpy` is declared in `pyproject.toml` but installed by the user's resolver under its own licence, and none of its code is in our wheel.

When a dependency is added or removed, this table and `../NOTICE` change with it, in the same commit. `pyproject.toml`'s `license-files` globs `licenses/*.txt`, so a new file is picked up automatically — which means a *missing* file is the failure mode to watch for, not a stale one.

## Two things to know

**`Imath-Half-BSD-3-Clause.txt` is a pointer, not a licence text.** FreeImage's tree carries only an SPDX identifier for it and ships no OpenEXR `LICENSE` file, so the full BSD-3-Clause text has to be pasted in from the OpenEXR project before this wheel is published. Every other file here is the verbatim text as its project ships it.

**No dependency is modified.** FreeType was patched until 2026-09-25 (`deps/hide-freetype-symbols.sh`, since removed) to stop `FT_*` leaking out of `libTKService`; that is now done at link time instead, so nothing here is a modified copy and no "modified" notice is owed. The FIPL in particular would make modification expensive: its §3.2 obliges us to publish source for any change we make to FreeImage. Keep it that way.
