cmake_minimum_required(VERSION 3.20)
project(nanocct LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python 3.12 COMPONENTS Interpreter Development.Module Development.SABIModule REQUIRED)
execute_process(COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
                OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

# OCCT: the local build in deps/ by default (see deps/build-occt-macos.sh)
set(NANOCCT_OCCT_DIR "${CMAKE_SOURCE_DIR}/deps/occt" CACHE PATH "OCCT installation prefix")
set(NANOCCT_RAPIDJSON_DIR "${CMAKE_SOURCE_DIR}/deps/rapidjson/include" CACHE PATH "RapidJSON headers (vendored)")
# OCCT's install layout differs by platform: lib/cmake/opencascade on Unix, cmake/ on Windows (2026-09-23)
find_package(OpenCASCADE REQUIRED NO_DEFAULT_PATH PATHS
             "${NANOCCT_OCCT_DIR}/lib/cmake/opencascade"
             "${NANOCCT_OCCT_DIR}/cmake")
message(STATUS "nanocct: OCCT ${OpenCASCADE_VERSION} from ${NANOCCT_OCCT_DIR}")
# The sources were generated from one OCCT (the manifest records its version); compiling them against another must
# fail here. NANOCCT_OCCT_DIR is a cache variable, so a build directory configured before the OCCT version changed
# keeps the old prefix whatever the default above says.
file(READ "${CMAKE_SOURCE_DIR}/src/cpp/manifest.json" NANOCCT_MANIFEST)
string(JSON NANOCCT_GENERATED_OCCT GET "${NANOCCT_MANIFEST}" occt_version)
if(NOT OpenCASCADE_VERSION VERSION_EQUAL NANOCCT_GENERATED_OCCT)
  message(FATAL_ERROR "nanocct: the sources were generated from OCCT ${NANOCCT_GENERATED_OCCT}, but ${NANOCCT_OCCT_DIR} "
                      "is OCCT ${OpenCASCADE_VERSION} -- regenerate (make generate), or reconfigure with "
                      "-DNANOCCT_OCCT_DIR=<the matching install> (a build directory keeps the prefix it was configured with)")
endif()

# macOS: types keep default visibility, functions and variables stay hidden (-fvisibility-ms-compat = -fvisibility=hidden
# -ftype-visibility=default; it must come after nanobind's -fvisibility=hidden, the last of the two wins). Every library
# has its own copy of the RTTI of a template instance (NCollection_HArray1<int>), and libc++ on arm64 compares two copies
# by name only when both are marked non-unique -- clang marks only those of default visibility, as OCCT's are. Under
# nanobind's -fvisibility=hidden an H-array created by nanocct failed OCCT's own occ::down_cast, and OCCT dereferenced the
# null handle (2026-09-30). It exports no symbol: clang keeps such RTTI hidden (measured).
if(APPLE)
  set(NANOCCT_VISIBILITY -fvisibility-ms-compat)
endif()

include("${CMAKE_SOURCE_DIR}/src/cpp/toolkits.cmake")   # generated: NANOCCT_TOOLKITS
foreach(tk IN LISTS NANOCCT_TOOLKITS)
  file(GLOB tk_sources CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/src/cpp/${tk}/*.cpp")
  nanobind_add_module(_${tk} STABLE_ABI NB_DOMAIN nanocct ${tk_sources})
  target_compile_options(_${tk} PRIVATE ${NANOCCT_VISIBILITY})
  target_include_directories(_${tk} PRIVATE "${CMAKE_SOURCE_DIR}/src/cpp/common")
  # OCCT's exported targets define HAVE_RAPIDJSON but do not carry the include path, and an installed header
  # includes it (RWGltf_GltfJsonParser.hxx -> rapidjson/document.h). Same vendored copy the OCCT build used
  # (deps/fetch-rapidjson.sh); header-only, so nothing extra is linked or shipped.
  if(EXISTS "${NANOCCT_RAPIDJSON_DIR}")
    target_include_directories(_${tk} PRIVATE "${NANOCCT_RAPIDJSON_DIR}")
  endif()
  # Private OCCT headers that installed headers include and the install lacks, copied from the OCCT sources by the
  # generator (generated toolkits.cmake; GeomBndLib_InfiniteHelpers.pxx in OCCT 8.0.2, Binding-Rules.md R-PRIVATE-HEADER).
  # The directory holds only those, so it shadows no installed header.
  if(DEFINED NANOCCT_OCCT_PRIVATE_INCLUDE)
    target_include_directories(_${tk} PRIVATE "${NANOCCT_OCCT_PRIVATE_INCLUDE}")
  endif()
  # deprecated OCCT members are bound on purpose (their deprecation message becomes the docstring, Binding-Rules.md)
  if(MSVC)
    target_compile_options(_${tk} PRIVATE /wd4996)
  else()
    target_compile_options(_${tk} PRIVATE -Wno-deprecated-declarations)
  endif()
  # ${tk} brings OCCT's own EXTERNLIB closure; NANOCCT_<tk>_EXTRA_LIBS adds the toolkits whose types the
  # generated code names but OCCT does not link (typeinfo for the handle caster, Binding-Rules.md R-LINK).
  target_link_libraries(_${tk} PRIVATE ${tk} ${NANOCCT_${tk}_EXTRA_LIBS})
  # dev builds: find the OCCT libraries where they are; wheels get relinked by delocate/auditwheel
  set_target_properties(_${tk} PROPERTIES INSTALL_RPATH "${NANOCCT_OCCT_DIR}/lib")
  install(TARGETS _${tk} LIBRARY DESTINATION nanocct)
endforeach()

# nanocct._AddOns: hand-written, not generated and not a binding of an OCCT toolkit, so it is built outside the
# loop above and tracked in git (src/cpp/AddOns, kept by .gitignore and untouched by `make clean_gen`). It holds
# the helpers that zero-copy views cannot express because they are computations rather than data,
# and, rarely, a workaround for an OCCT bug that is not fixed upstream (Binding-Rules.md R-ADDON).
nanobind_add_module(_AddOns STABLE_ABI NB_DOMAIN nanocct "${CMAKE_SOURCE_DIR}/src/cpp/AddOns/_AddOns.cpp"
                    "${CMAKE_SOURCE_DIR}/src/cpp/AddOns/Tessellator.cpp"
                    "${CMAKE_SOURCE_DIR}/src/cpp/AddOns/ShapeClean.cpp")
target_compile_options(_AddOns PRIVATE ${NANOCCT_VISIBILITY})
target_include_directories(_AddOns PRIVATE "${CMAKE_SOURCE_DIR}/src/cpp/common")
if(MSVC)
  target_compile_options(_AddOns PRIVATE /wd4996)
else()
  target_compile_options(_AddOns PRIVATE -Wno-deprecated-declarations)
endif()
# BRepGProp_Face lives in TKTopAlgo; ShapeClean needs ShapeUpgrade (TKShHealing) and Geom2dConvert (TKGeomBase)
target_link_libraries(_AddOns PRIVATE TKShHealing TKTopAlgo TKGeomBase TKBRep TKG2d TKG3d TKMath TKernel)
set_target_properties(_AddOns PROPERTIES INSTALL_RPATH "${NANOCCT_OCCT_DIR}/lib")
install(TARGETS _AddOns LIBRARY DESTINATION nanocct)
