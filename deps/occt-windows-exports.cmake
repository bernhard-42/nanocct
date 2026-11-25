# Windows only: the exports OCCT's DLLs need beyond what Standard_EXPORT marks, from deps/occt-windows-exports.txt.
#
# Standard_EXPORT is __declspec(dllexport) on Windows and empty elsewhere, so a member OCCT defines in a .cxx without it
# is exported on macOS and Linux and missing from the Windows DLL. deps/occt-windows-exports.txt lists the ones the
# bindings call (written by `make occt-exports`); this file turns its [exports] section into one module-definition file
# per toolkit and
# adds it to that toolkit's target, so the linker exports those names too. OCCT's sources and CMake files stay as they
# are: deps/build-occt-windows.sh passes this file as CMAKE_PROJECT_INCLUDE, which CMake includes after every project()
# call ("intended for injecting custom code into project builds without modifying their source", cmake
# --help-variable CMAKE_PROJECT_INCLUDE) -- once per toolkit, as each toolkit's CMakeLists.txt starts with project().
include_guard(GLOBAL)

if(NOT DEFINED NANOCCT_OCCT_WINDOWS_EXPORTS OR NOT EXISTS "${NANOCCT_OCCT_WINDOWS_EXPORTS}")
  message(FATAL_ERROR "nanocct: NANOCCT_OCCT_WINDOWS_EXPORTS must name deps/occt-windows-exports.txt "
    "(got '${NANOCCT_OCCT_WINDOWS_EXPORTS}')")
endif()

# Deferred to the end of the top-level directory: the toolkit targets exist only after OCCT's add_subdirectory loop.
function(_nanocct_occt_exports)
  file(STRINGS "${NANOCCT_OCCT_WINDOWS_EXPORTS}" _lines)
  set(_section "")
  set(_toolkits "")
  foreach(_line IN LISTS _lines)
    if(_line MATCHES "^#" OR _line STREQUAL "")
      continue()
    endif()
    if(_line MATCHES "^\\[([a-z]+)\\]$")
      set(_section "${CMAKE_MATCH_1}")
      continue()
    endif()
    if(NOT _section STREQUAL "exports")
      continue()
    endif()
    if(NOT _line MATCHES "^(TK[A-Za-z0-9_]+)[ \t]+([^ \t]+)$")
      message(FATAL_ERROR "nanocct: unreadable line in ${NANOCCT_OCCT_WINDOWS_EXPORTS}: '${_line}'")
    endif()
    set(_tk "${CMAKE_MATCH_1}")
    if(NOT _tk IN_LIST _toolkits)
      list(APPEND _toolkits "${_tk}")
      set(_text_${_tk} "EXPORTS\n")
    endif()
    string(APPEND _text_${_tk} "\t${CMAKE_MATCH_2}\n")
  endforeach()

  set(_dir "${CMAKE_BINARY_DIR}/nanocct-exports")
  foreach(_tk IN LISTS _toolkits)
    if(NOT TARGET "${_tk}")
      message(FATAL_ERROR
        "nanocct: ${NANOCCT_OCCT_WINDOWS_EXPORTS} lists exports for ${_tk}, which this OCCT build has no target for")
    endif()
    # COPYONLY: decorated names are full of '@' ("?Foo@Bar@@..." holds "@Bar@"), which file(CONFIGURE) or a plain
    # configure_file would substitute as a variable reference. configure_file because "the generated file is modified
    # and its timestamp updated on subsequent cmake runs only if its content is changed": an unchanged list relinks nothing.
    file(WRITE "${_dir}/staging/${_tk}.def" "${_text_${_tk}}")
    configure_file("${_dir}/staging/${_tk}.def" "${_dir}/${_tk}.def" COPYONLY)
    target_sources("${_tk}" PRIVATE "${_dir}/${_tk}.def")
    message(STATUS "nanocct: ${_tk} exports the names in ${_dir}/${_tk}.def")
  endforeach()
endfunction()

cmake_language(DEFER DIRECTORY "${CMAKE_SOURCE_DIR}" CALL _nanocct_occt_exports)
