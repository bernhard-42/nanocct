cmake_minimum_required(VERSION 3.20)
project(nanoocp LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python 3.12 COMPONENTS Interpreter Development.Module Development.SABIModule REQUIRED)
execute_process(COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
                OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

# OCCT: the local build in deps/ by default (see deps/build-occt.sh)
set(NANOOCP_OCCT_DIR "${CMAKE_SOURCE_DIR}/deps/occt-8.0.1" CACHE PATH "OCCT installation prefix")
find_package(OpenCASCADE REQUIRED PATHS "${NANOOCP_OCCT_DIR}/lib/cmake/opencascade" NO_DEFAULT_PATH)
message(STATUS "nanoocp: OCCT ${OpenCASCADE_VERSION} from ${NANOOCP_OCCT_DIR}")

include("${CMAKE_SOURCE_DIR}/src/cpp/toolkits.cmake")   # generated: NANOOCP_TOOLKITS
foreach(tk IN LISTS NANOOCP_TOOLKITS)
  file(GLOB tk_sources CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/src/cpp/${tk}/*.cpp")
  nanobind_add_module(_${tk} STABLE_ABI NB_DOMAIN nanoocp ${tk_sources})
  target_include_directories(_${tk} PRIVATE "${CMAKE_SOURCE_DIR}/src/cpp/common")
  target_link_libraries(_${tk} PRIVATE ${tk})
  # dev builds: find the OCCT libraries where they are; wheels get relinked by delocate/auditwheel
  set_target_properties(_${tk} PROPERTIES INSTALL_RPATH "${NANOOCP_OCCT_DIR}/lib")
  install(TARGETS _${tk} LIBRARY DESTINATION nanoocp)
endforeach()
