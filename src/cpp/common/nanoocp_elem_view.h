// Which array element types can be viewed as numpy scalars, and how (R-VIEW, State.md 8.10a).
//
// Separate from nanoocp_views.h because this half is about the *element*, not the container: the same table
// serves NCollection_Array1/Array2/HArray1/HArray2 (nanoocp_ncollection.h) and anything else holding a
// packed array of these types. nanoocp_views.h is per-class and pulls in that class's OCCT header; this one
// only needs the small value types.
//
// The table is asserted, not assumed. Every entry static_asserts that the type really is N packed scalars
// with no padding and no vtable, so a layout change in OCCT is a compile error rather than a wrong array.
// Measured on OCCT 8.0.1 / clang 22 (arm64): gp_Pnt, gp_XYZ, gp_Vec and gp_Dir are 24 bytes, gp_Pnt2d,
// gp_XY, gp_Vec2d and gp_Dir2d 16, Poly_Triangle 12, all standard-layout, trivially copyable and
// non-polymorphic, with the first coordinate at offset 0.
#pragma once

#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

#include <cstdint>
#include <type_traits>

#include <Poly_Triangle.hxx>
#include <gp_Dir.hxx>
#include <gp_Dir2d.hxx>
#include <gp_Pnt.hxx>
#include <gp_Pnt2d.hxx>
#include <gp_Vec.hxx>
#include <gp_Vec2d.hxx>
#include <gp_XY.hxx>
#include <gp_XYZ.hxx>

namespace nb = nanobind;

namespace nanoocp {

//! Not viewable unless specialised below: a class element, a handle, a string, anything with a vtable.
template <class T> struct view_elem { static constexpr bool supported = false; };

//! @param T the array element type
//! @param S the numpy scalar it decomposes into
//! @param N how many of them (1 = a plain scalar array, no trailing dimension)
//! @param W false when a raw write could leave the value invalid, which makes the view read-only
#define NANOOCP_VIEW_ELEM(T, S, N, W)                                                              \
    template <> struct view_elem<T> {                                                              \
        using scalar = S;                                                                          \
        static constexpr size_t components = N;                                                    \
        static constexpr bool writable = W;                                                        \
        static constexpr bool supported = true;                                                    \
        static_assert(sizeof(T) == sizeof(S) * (N), #T " is not " #N " packed " #S);               \
        static_assert(std::is_standard_layout_v<T>, #T " is not standard layout");                 \
        static_assert(std::is_trivially_copyable_v<T>, #T " is not trivially copyable");           \
        static_assert(!std::is_polymorphic_v<T>, #T " has a vtable");                              \
    };

NANOOCP_VIEW_ELEM(double, double, 1, true)
NANOOCP_VIEW_ELEM(float, float, 1, true)
NANOOCP_VIEW_ELEM(int32_t, int32_t, 1, true)
NANOOCP_VIEW_ELEM(bool, bool, 1, true)
NANOOCP_VIEW_ELEM(uint8_t, uint8_t, 1, true)

NANOOCP_VIEW_ELEM(gp_Pnt, double, 3, true)
NANOOCP_VIEW_ELEM(gp_XYZ, double, 3, true)
NANOOCP_VIEW_ELEM(gp_Vec, double, 3, true)
NANOOCP_VIEW_ELEM(gp_Pnt2d, double, 2, true)
NANOOCP_VIEW_ELEM(gp_XY, double, 2, true)
NANOOCP_VIEW_ELEM(gp_Vec2d, double, 2, true)

// A gp_Dir is normalised by construction and every OCCT setter keeps it so; a raw write through a view
// could leave a direction of length 0.3 in the array, which is not a gp_Dir. Read-only, therefore --
// SetValue() is the way to change one.
NANOOCP_VIEW_ELEM(gp_Dir, double, 3, false)
NANOOCP_VIEW_ELEM(gp_Dir2d, double, 2, false)

// Three 1-based node indices, the same layout Poly_Triangulation's TrianglesArray() views.
NANOOCP_VIEW_ELEM(Poly_Triangle, int32_t, 3, true)

#undef NANOOCP_VIEW_ELEM

//! A view over `theShape` elements starting at `theFirst`, with the element's components as a trailing
//! dimension when it has more than one -- (N,) for double, (N, 3) for gp_Pnt, (rows, cols, 3) for an
//! Array2 of gp_Pnt. Writability follows the element's entry in the table above.
//!
//! The array is created with no owner: the caller's `nb::rv_policy::reference_internal` on the `.def()` is
//! what ties it to the object, as in nanoocp_views.h. nanobind copies the shape, so the local is fine.
//!
//! @param theFirst  address of element 0, or nullptr when the array is empty
//! @param theShape  the leading dimensions -- one for Array1, two for Array2
template <class T, size_t NDim>
auto elem_view(void *theFirst, const size_t (&theShape)[NDim]) {
    using E = view_elem<T>;
    using S = typename E::scalar;

    size_t shape[NDim + 1];
    for (size_t i = 0; i < NDim; ++i)
        shape[i] = theShape[i];
    shape[NDim] = E::components;
    const size_t ndim = E::components == 1 ? NDim : NDim + 1;

    if constexpr (E::writable)
        return nb::ndarray<nb::numpy, S>(theFirst, ndim, shape, nb::handle());
    else
        return nb::ndarray<nb::numpy, const S>(theFirst, ndim, shape, nb::handle());
}

} // namespace nanoocp
