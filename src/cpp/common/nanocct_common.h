// Shared by every generated nanocct translation unit.
#pragma once
// MSVC only: nanobind defines NB_INLINE as __forceinline, and MSVC's optimizer is superlinear in the size of a
// function that expands it that often. A binding registration function is exactly that. Measured on gauss
// (i7-8700, MSVC 14.44, 2026-09-23) for src/cpp/TKMath/math.cpp -- 531 .def calls in one function -- at the build's
// own /O2 /Ob2 /Os:
//     __forceinline (stock)   ~1677 s (in the parallel build; /O1 alone ran >8 min and was killed)
//     inline                      16 s, and the object is SMALLER (6958 KB vs 9045 KB at /Od)
// Upstream reports the same and names __forceinline as the trigger: 2 h 28 m -> 3 m 04 s
// (https://github.com/wjakob/nanobind/discussions/791). nb_defs.h is #pragma once guarded, so pulling it in first and
// redefining the macro here needs no patched or vendored nanobind. clang and gcc keep always_inline: neither has the
// problem, and nanobind wants the hint for the binding layer's hot paths.
#if defined(_MSC_VER)
#  include <nanobind/nb_defs.h>
#  undef NB_INLINE
#  define NB_INLINE inline
#endif
#include <nanobind/nanobind.h>
#include <nanobind/make_iterator.h>
// R-STL: nanobind's casters for std types (generator/parse.py _STD_TEMPLATES_OK lists them, plus std::bitset: R-BITSET)
#include <nanobind/stl/array.h>
#include <nanobind/stl/function.h>
#include <nanobind/stl/list.h>
#include <nanobind/stl/map.h>
#include <nanobind/stl/optional.h>
#include <nanobind/stl/pair.h>
#include <nanobind/stl/set.h>
#include <nanobind/stl/shared_ptr.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/string_view.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/stl/unique_ptr.h>
#include <nanobind/stl/unordered_map.h>
#include <nanobind/stl/unordered_set.h>
#include <nanobind/stl/variant.h>
#include <nanobind/stl/vector.h>
#include <algorithm>
#include <array>
#include <functional>
#include <bitset>
#include <tuple>
#include <type_traits>

#include <atomic>
#include <cstdint>
#include <stdexcept>
#include <mutex>
#include <sstream>
#include <string>
#include <typeinfo>
#include <unordered_map>
#include <utility>
#include <vector>
#include <memory>

#include <Standard_Failure.hxx>
#include <Standard_Handle.hxx>
#include <Standard_Transient.hxx>
#include <NCollection_Handle.hxx>

namespace nb = nanobind;

// The parts, in this order (each relies on the ones before it; review M8, 2026-10-03):
#include "nanocct_registry.h"
#include "nanocct_lifetime.h"
#include "nanocct_class_helpers.h"
#include "nanocct_call_policies.h"
#include "nanocct_guards.h"
#include "nanocct_casters.h"
