# Third-party licences

nanocct's own code is Apache-2.0 (`../LICENSE`). Everything in this directory is the verbatim licence text of something the **binary distribution bundles or compiles in** — not of a build-time-only tool — except `Microsoft-VC-Runtime.txt`: Microsoft's terms for the Visual C++ runtime are not open source, so that file records the runtime's provenance, identifies the applicable Microsoft terms and links them. `../NOTICE` says what each one covers and where its source is; this file records how the list is kept honest. `components.toml` holds the same information in machine-readable form, and the build and the tests read it.

**Source and modifications.** The bundled third-party libraries are built from their upstream source with the build options described below, and nanocct applies no source patches of its own; the Linux system libraries are the AlmaLinux 8 packages as the distribution builds them, including the patches of its source packages. The generated type stubs reproduce and adapt documentation from the OCCT headers, and each stub file as a whole is distributed under `LGPL-2.1-only WITH OCCT-exception-1.0`; the comment at the top of each stub identifies that material, the OCCT and nanocct versions it was made from, the copyright holders and the licence.

## Licence expressions

The expression below is the union of the licences applicable across nanocct's binary wheels. It is an inventory for this documentation, not the licence expression of every individual wheel:

```
Apache-2.0 AND LGPL-2.1-only WITH OCCT-exception-1.0 AND FTL AND FreeImage AND Zlib AND libpng-2.0
AND libpng-1.6.35 AND LicenseRef-IJG-libjpeg-10 AND libtiff AND BSD-2-Clause AND BSD-3-Clause AND MIT
AND HPND-sell-variant AND LicenseRef-libpng-1.6.34 AND bzip2-1.0.6 AND LicenseRef-libuuid
AND LicenseRef-Microsoft-VC-Runtime
```

Each wheel's `License-Expression` metadata describes the components actually included in that wheel: `../generator/wheel.py` writes it from `components.toml` for the wheel's platform, as the Core Metadata specification asks of a field that "only applies to the Distribution Archive containing the metadata with this field". The macOS wheels carry the first twelve terms (up to `MIT`), the Linux wheels add the four terms of the Linux system libraries (`HPND-sell-variant` to `LicenseRef-libuuid`), the Windows wheel adds `LicenseRef-Microsoft-VC-Runtime`. `../tests/test_licensing.py` checks every repaired wheel's expression and libraries against the table. nanocct publishes no sdist.

The licences apply together, each to the component or material identified in the table; they do not all apply to every file.

**How the identifiers were assigned.** Each licence file below was compared word by word with the SPDX licence text, and where they differ, with SPDX's matching template (license-list-XML), so that only the variations the template permits — copyright lines, the licensor's name, marked alternatives — are accepted. A file that differs beyond that gets a custom `LicenseRef-` reference, defined by the file the table names:

- `HPND-sell-variant` (fontconfig): the differences are the copyright lines, the licensor's name and "appear" for "appears", all of which the template permits.
- `libpng-2.0` and `libpng-1.6.35` (FreeImage's libpng): its licence file carries both texts, the current licence and the one for libpng 0.5 to 1.6.35; they differ from SPDX's texts only in copyright years.
- `LicenseRef-libpng-1.6.34` (the system libpng 1.6.34): its text names other versions and dates than SPDX's `libpng-1.6.35`, whose template has no alternatives for them, and it adds trademark and export notes.
- `LicenseRef-IJG-libjpeg-10` (libjpeg 10, vendored by FreeImage): the legal section of its README differs in substance from both `IJG` and `IJG-short`.
- `LicenseRef-libuuid`: its first condition ("the entire permission notice in its entirety, including the disclaimer of warranties") is not the wording `BSD-3-Clause`'s template allows.
- `LicenseRef-Microsoft-VC-Runtime` is a custom license reference, not an identifier from the SPDX License List. It identifies the applicable proprietary Microsoft runtime terms.

FreeType and FreeImage offer alternative licences; the FTL and the FreeImage Public License are the ones chosen (`../NOTICE`).

## Components

| File | SPDX | Component | Wheels | How it reaches the wheel |
| --- | --- | --- | --- | --- |
| `../LICENSE` | `Apache-2.0` | nanocct | all | nanocct-authored bindings, generator code and generated binding code, and the AddOns; excluding the type stubs (next row) and third-party material |
| `OCCT-LGPL-2.1.txt`, `OCCT-LGPL-exception.txt` | `LGPL-2.1-only WITH OCCT-exception-1.0` | Open CASCADE Technology 8.0.1 | all | the `libTK*` shared libraries are bundled, the generated bindings incorporate material from OCCT headers, and the `.pyi` type stubs reproduce and adapt OCCT's header documentation: source text, which the exception does not cover, so each stub file as a whole is under this licence, nanocct's contributions to it included, and says so at its top |
| `FreeType-FTL.txt` | `FTL` | FreeType 2.14.3 | all | statically linked into `libTKService`, so it is not a separate file in the wheel; `deps/occt-unexported-symbols.txt` keeps its symbols from being re-exported, which does not change the licence obligation |
| `FreeImage-FIPL.txt` | `FreeImage` | FreeImage&nbsp;3.19.15 | all | bundled as its own shared library (`libFreeImage.dylib`/`.so`/`.dll`); it gives OCCT its image codecs |
| `zlib.txt`, `libpng.txt`, `libjpeg-IJG.txt`, `libtiff.txt`, `OpenJPEG-BSD-2-Clause.txt` | `Zlib`, `libpng-2.0` and `libpng-1.6.35`, `LicenseRef-IJG-libjpeg-10`, `libtiff`, `BSD-2-Clause` | the codecs FreeImage vendors | all | compiled into `libFreeImage`; built with WebP, the OpenEXR codec, LibRaw and JPEG-XR switched off, and FreeImage vendors no JBIG-KIT |
| `Imath-Half-BSD-3-Clause.txt` | `BSD-3-Clause` | the OpenEXR-derived half-float implementation (Imath) | all | FreeImage compiles `Source/OpenEXR/Half/half.cpp` ("Copyright Contributors to the OpenEXR Project", `SPDX-License-Identifier: BSD-3-Clause`) into `libFreeImage` for its 16-bit float pixel type. The OpenEXR image codec is disabled, and no separate OpenEXR library is bundled |
| `fontconfig.txt`, `FreeType-FTL.txt`, `libpng-1.6.34.txt`, `bzip2.txt`, `libuuid.txt` | `HPND-sell-variant`, `FTL`, `LicenseRef-libpng-1.6.34`, `bzip2-1.0.6`, `LicenseRef-libuuid` | fontconfig 2.13.1, FreeType 2.9.1, libpng 1.6.34, bzip2 1.0.6, libuuid (util-linux) | Linux | `auditwheel repair` bundles them from the manylinux_2_28 build image (AlmaLinux 8): OCCT's `libTKService` needs fontconfig, which needs FreeType and libuuid, which need libpng and libbz2. Source: the AlmaLinux 8.10 source RPMs |
| `Microsoft-VC-Runtime.txt` | `LicenseRef-Microsoft-VC-Runtime` | `msvcp140.dll`, the Microsoft Visual C++ runtime, unmodified | Windows | `delvewheel repair` takes it from the building Visual Studio's `VC\Redist` folder (`../deps/vc-redist-crt.sh`), and `../tools/check_vc_runtime.py` checks it is byte-identical. The file records provenance, identifies the applicable Microsoft terms, and links to them; it does not replace or grant rights beyond those terms |
| `RapidJSON.txt` | `MIT` | RapidJSON 1.1.0 | all | header-only, compiled into OCCT's glTF reader. Its bundled msinttypes headers (BSD) are used only by MSVC before Visual Studio 2013 (`rapidjson.h:162`), so not here, and the JSON-licensed `bin/jsonchecker` is not shipped |
| `nanobind-BSD-3-Clause.txt` | `BSD-3-Clause` | nanobind 3.1.0 | all | its runtime is compiled into every extension module |
| `robin_map-MIT.txt` | `MIT` | tsl::robin_map | all | vendored inside nanobind, compiled in with it |
