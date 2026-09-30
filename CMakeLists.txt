cmake_minimum_required(VERSION 3.20)
project(nanocct LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python 3.12 COMPONENTS Interpreter Development.Module Development.SABIModule REQUIRED)
execute_process(COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
                OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

# OCCT: the local build in deps/ by default (see deps/build-occt-macos.sh)
set(NANOCCT_OCCT_DIR "${CMAKE_SOURCE_DIR}/deps/occt-8.0.1" CACHE PATH "OCCT installation prefix")
set(NANOCCT_RAPIDJSON_DIR "${CMAKE_SOURCE_DIR}/deps/rapidjson/include" CACHE PATH "RapidJSON headers (vendored)")
# OCCT's install layout differs by platform: lib/cmake/opencascade on Unix, cmake/ on Windows (2026-09-23)
find_package(OpenCASCADE REQUIRED NO_DEFAULT_PATH PATHS
             "${NANOCCT_OCCT_DIR}/lib/cmake/opencascade"
             "${NANOCCT_OCCT_DIR}/cmake")
message(STATUS "nanocct: OCCT ${OpenCASCADE_VERSION} from ${NANOCCT_OCCT_DIR}")

include("${CMAKE_SOURCE_DIR}/src/cpp/toolkits.cmake")   # generated: NANOCCT_TOOLKITS
foreach(tk IN LISTS NANOCCT_TOOLKITS)
  file(GLOB tk_sources CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/src/cpp/${tk}/*.cpp")
  nanobind_add_module(_${tk} STABLE_ABI NB_DOMAIN nanocct ${tk_sources})
  target_include_directories(_${tk} PRIVATE "${CMAKE_SOURCE_DIR}/src/cpp/common")
  # OCCT's exported targets define HAVE_RAPIDJSON but do not carry the include path, and an installed header
  # includes it (RWGltf_GltfJsonParser.hxx -> rapidjson/document.h). Same vendored copy the OCCT build used
  # (deps/fetch-rapidjson.sh); header-only, so nothing extra is linked or shipped.
  if(EXISTS "${NANOCCT_RAPIDJSON_DIR}")
    target_include_directories(_${tk} PRIVATE "${NANOCCT_RAPIDJSON_DIR}")
  endif()
  # deprecated OCCT members are bound on purpose (their deprecation message becomes the docstring, Design.md 6)
  if(MSVC)
    target_compile_options(_${tk} PRIVATE /wd4996)
  else()
    target_compile_options(_${tk} PRIVATE -Wno-deprecated-declarations)
  endif()
  # ${tk} brings OCCT's own EXTERNLIB closure; NANOCCT_<tk>_EXTRA_LIBS adds the toolkits whose types the
  # generated code names but OCCT does not link (typeinfo for the handle caster, Design.md 6 R-LINK).
  target_link_libraries(_${tk} PRIVATE ${tk} ${NANOCCT_${tk}_EXTRA_LIBS})
  # dev builds: find the OCCT libraries where they are; wheels get relinked by delocate/auditwheel
  set_target_properties(_${tk} PROPERTIES INSTALL_RPATH "${NANOCCT_OCCT_DIR}/lib")
  install(TARGETS _${tk} LIBRARY DESTINATION nanocct)
endforeach()

# nanocct._AddOns: hand-written, not generated and not a binding of an OCCT toolkit, so it is built outside the
# loop above and tracked in git (src/cpp/AddOns, kept by .gitignore and untouched by `make clean_gen`). It holds
# the helpers that zero-copy views cannot express because they are computations rather than data,
# and, rarely, a workaround for an OCCT bug that is not fixed upstream (Design.md R-ADDON).
nanobind_add_module(_AddOns STABLE_ABI NB_DOMAIN nanocct "${CMAKE_SOURCE_DIR}/src/cpp/AddOns/_AddOns.cpp"
                    "${CMAKE_SOURCE_DIR}/src/cpp/AddOns/Tessellator.cpp"
                    "${CMAKE_SOURCE_DIR}/src/cpp/AddOns/ShapeClean.cpp")
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
