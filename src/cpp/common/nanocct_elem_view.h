// Which array element types can be viewed as numpy scalars, and how (R-VIEW).
//
// Separate from nanocct_views.h because this half is about the *element*, not the container: the same table
// serves NCollection_Array1/Array2/HArray1/HArray2 (nanocct_ncollection.h) and anything else holding a
// packed array of these types. nanocct_views.h is per-class and pulls in that class's OCCT header; this one
// only needs the small value types.
//
// The table is asserted, not assumed. Every entry static_asserts that the type really is N packed scalars
// with no padding and no vtable, so a layout change in OCCT is a compile error rather than a wrong array.
// Measured on OCCT 8.0.1 / clang 22 (arm64): gp_Pnt, gp_XYZ, gp_Vec and gp_Dir are 24 bytes, gp_Pnt2d,
// gp_XY, gp_Vec2d and gp_Dir2d 16, Poly_Triangle 12, all standard-layout, trivially copyable and
// non-polymorphic, with the first coordinate at offset 0. NCollection_Vec2/3/4 are a plain `Element_t v[N]`
// (NCollection_Vec3.hxx:420).
//
// The view reaches Python through numpy's array protocol, `__array__` (array_protocol below), not through a
// method of its own: OCCT has no such method, and `np.asarray(obj)` is one spelling for every class.
#pragma once

#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

#include <nanobind/stl/optional.h>

#include <cstdint>
#include <optional>
#include <type_traits>

#include <NCollection_Vec2.hxx>
#include <NCollection_Vec3.hxx>
#include <NCollection_Vec4.hxx>
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

namespace nanocct {

//! Not viewable unless specialised below: a class element, a handle, a string, anything with a vtable.
template <class T> struct view_elem { static constexpr bool supported = false; };

//! @param T the array element type
//! @param S the numpy scalar it decomposes into
//! @param N how many of them (1 = a plain scalar array, no trailing dimension)
//! @param W false when a raw write could leave the value invalid, which makes the view read-only
#define NANOCCT_VIEW_ELEM(T, S, N, W)                                                              \
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

NANOCCT_VIEW_ELEM(double, double, 1, true)
NANOCCT_VIEW_ELEM(float, float, 1, true)
NANOCCT_VIEW_ELEM(int32_t, int32_t, 1, true)
NANOCCT_VIEW_ELEM(bool, bool, 1, true)
NANOCCT_VIEW_ELEM(uint8_t, uint8_t, 1, true)

NANOCCT_VIEW_ELEM(gp_Pnt, double, 3, true)
NANOCCT_VIEW_ELEM(gp_XYZ, double, 3, true)
NANOCCT_VIEW_ELEM(gp_Vec, double, 3, true)
NANOCCT_VIEW_ELEM(gp_Pnt2d, double, 2, true)
NANOCCT_VIEW_ELEM(gp_XY, double, 2, true)
NANOCCT_VIEW_ELEM(gp_Vec2d, double, 2, true)

// A gp_Dir is normalised by construction and every OCCT setter keeps it so; a raw write through a view
// could leave a direction of length 0.3 in the array, which is not a gp_Dir. Read-only, therefore --
// SetValue() is the way to change one.
NANOCCT_VIEW_ELEM(gp_Dir, double, 3, false)
NANOCCT_VIEW_ELEM(gp_Dir2d, double, 2, false)

// Three 1-based node indices -- Poly_Triangulation::InternalTriangles() is an array of these.
NANOCCT_VIEW_ELEM(Poly_Triangle, int32_t, 3, true)

// OCCT's small fixed-size vectors. NCollection_Vec3<float> is what Poly_Triangulation::InternalNormals()
// holds, whatever the node precision.
NANOCCT_VIEW_ELEM(NCollection_Vec2<float>, float, 2, true)
NANOCCT_VIEW_ELEM(NCollection_Vec3<float>, float, 3, true)
NANOCCT_VIEW_ELEM(NCollection_Vec4<float>, float, 4, true)
NANOCCT_VIEW_ELEM(NCollection_Vec2<double>, double, 2, true)
NANOCCT_VIEW_ELEM(NCollection_Vec3<double>, double, 3, true)
NANOCCT_VIEW_ELEM(NCollection_Vec4<double>, double, 4, true)
NANOCCT_VIEW_ELEM(NCollection_Vec2<int>, int32_t, 2, true)
NANOCCT_VIEW_ELEM(NCollection_Vec3<int>, int32_t, 3, true)
NANOCCT_VIEW_ELEM(NCollection_Vec4<int>, int32_t, 4, true)

#undef NANOCCT_VIEW_ELEM

//! A view over `theShape` elements starting at `theFirst`, with the element's components as a trailing
//! dimension when it has more than one -- (N,) for double, (N, 3) for gp_Pnt, (rows, cols, 3) for an
//! Array2 of gp_Pnt. Writability follows the element's entry in the table above.
//!
//! Without an owner the caller's `nb::rv_policy::reference_internal` is what ties the array to the object, as in
//! nanocct_views.h; an NCollection container passes its own owner (R-VIEW-GUARD: one that also counts the view).
//! nanobind copies the shape, so the local is fine.
//!
//! @param theFirst  address of element 0, or nullptr when the array is empty
//! @param theShape  the leading dimensions -- one for Array1, two for Array2
//! @param theOwner  the object the array keeps alive, or none
template <class T, size_t NDim>
auto elem_view(void *theFirst, const size_t (&theShape)[NDim], nb::handle theOwner = nb::handle()) {
    using E = view_elem<T>;
    using S = typename E::scalar;

    size_t shape[NDim + 1];
    for (size_t i = 0; i < NDim; ++i)
        shape[i] = theShape[i];
    shape[NDim] = E::components;
    const size_t ndim = E::components == 1 ? NDim : NDim + 1;

    if constexpr (E::writable)
        return nb::ndarray<nb::numpy, S>(theFirst, ndim, shape, theOwner);
    else
        return nb::ndarray<nb::numpy, const S>(theFirst, ndim, shape, theOwner);
}

//! The result of numpy's `__array__(dtype=None, copy=None)` for a view over `theOwner`'s memory.
//!
//! Measured on numpy 2.5.3, not assumed: numpy casts to a requested dtype itself (and raises itself when
//! `copy=False` makes that impossible), so `dtype` needs no handling here. But numpy *trusts* `copy=True` --
//! what `np.array(obj)` passes -- and a view returned for it stays shared with the object, so the copy has to
//! happen here. `ndarray::cast` keeps the static type, so the stub still names the exact dtype.
//!
//! @param theView  a view created with no owner (nb::handle())
//! @param theOwner the Python object whose memory it is; the view keeps it alive
//! @param theCopy  `copy` as numpy passed it: true = an independent copy, None or false = the view
template <class A> auto array_protocol(A theView, nb::handle theOwner, std::optional<bool> theCopy) {
    // rv_policy's members are distinct tag types (nb_backend.h), so no ternary between two of them
    nb::rv_policy policy = nb::rv_policy::reference_internal;
    if (theCopy.has_value() && theCopy.value() == true)
        policy = nb::rv_policy::copy;
    return theView.cast(policy, theOwner);
}

} // namespace nanocct
