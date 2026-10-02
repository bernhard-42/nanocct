// Zero-copy numpy views over OCCT's contiguous arrays (R-VIEW).
//
// The rule: array data that can get large crosses to Python as a view, never as a per-element loop. The
// generator decides *which* classes get views -- overrides.toml [views] classes -- and emits
// `nanocct_def_views<T>(cls);`; this header decides *how*, one specialisation per class.
//
// The view is numpy's array protocol, `__array__`: `numpy.asarray(obj)` is the view,
// `numpy.array(obj)` a copy. No class gets a method OCCT does not have. A class whose data sits in several
// arrays (Poly_Triangulation: nodes, triangles, UV nodes, normals) gets nothing itself -- OCCT's own
// accessors hand out the arrays (InternalNodes() ...), and those carry `__array__`. An empty array is a
// zero-length view, never None: `__array__` has to return an array, and "is there anything" is OCCT's
// question (HasUVNodes(), HasNormals(), IsEmpty()).
//
// Why the "how" is C++ and not more TOML: every case has runtime branches that a config file cannot express.
// Poly_ArrayOfNodes' dtype depends on IsDoublePrecision();
// Image_PixMap's rows are padded, so the view needs a stride from SizeRowBytes() rather than width*channels
// (measured: a FreeImage-loaded 5-pixel-wide RGB image has SizeRowBytes 16, not 15 -- a shape-only view would
// silently shear it). Keeping it in C++ makes it type-checked and greppable.
//
// Lifetime: every view is cast with nb::rv_policy::reference_internal (nanocct::array_protocol), which ties
// it to the owning object through the array's `base`. Verified on the stable ABI: dropping every Python
// reference to the owner leaves the view valid, and the owner is destroyed exactly when the last view goes.
#pragma once

#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

#include "nanocct_elem_view.h"

#include <optional>
#include <stdexcept>

namespace nb = nanobind;

//! Declared, never defined: a class listed in overrides.toml [views] without a specialisation below is a link
//! error rather than a silently missing accessor. tests/test_views.py asserts the two lists agree, so it normally
//! fails in the test suite instead.
template <class T> void nanocct_def_views(nb::class_<T> cls);

// ---- Poly_ArrayOfNodes, Poly_ArrayOfUVNodes ---------------------------------------------------------------
// What Poly_Triangulation::InternalNodes() / InternalUVNodes() return, by reference to the triangulation's own
// storage. One contiguous allocation (NCollection_AliasedArray, a single Standard::AllocateAligned buffer,
// 0-based: Lower() is always 0) whose element is gp_Pnt / gp_Pnt2d (float64) or NCollection_Vec3/Vec2<float>
// (float32), decided by IsDoublePrecision() when the array was allocated -- so the dtype follows the object,
// not the binding, and cannot be a static type. A triangulation without UV nodes holds an unallocated array
// of size 0, which is a (0, 2) view.
#include <Poly_ArrayOfNodes.hxx>
#include <Poly_ArrayOfUVNodes.hxx>

namespace nanocct {

//! __array__ for an aliased node array of K coordinates per node
template <class A, size_t K> void def_aliased_nodes_view(nb::class_<A> cls, const char *theDoc) {
    cls.def("__array__", [](A &self, nb::handle, std::optional<bool> copy) {
            const size_t n = (size_t) self.Size();
            const size_t shape[2] = { n, K };
            return array_protocol(
                nb::ndarray<nb::numpy>(n == 0 ? nullptr : (void *) self.changeValue(0), 2, shape, nb::handle(),
                                       nullptr, self.IsDoublePrecision() ? nb::dtype<double>() : nb::dtype<float>()),
                nb::find(&self), copy);
        }, nb::arg("dtype") = nb::none(), nb::arg("copy") = nb::none(), theDoc);
}

} // namespace nanocct

template <> inline void nanocct_def_views<Poly_ArrayOfNodes>(nb::class_<Poly_ArrayOfNodes> cls) {
    nanocct::def_aliased_nodes_view<Poly_ArrayOfNodes, 3>(cls,
        "Python addition: numpy's array protocol -- `numpy.asarray(nodes)` is a zero-copy (Size(), 3) view of "
        "the nodes (R-VIEW), `numpy.array(nodes)` a copy.\n\n"
        "The dtype follows the object, not the binding: float64 when IsDoublePrecision() is true (OCCT's "
        "default) and float32 otherwise. Writes go straight into the array -- for "
        "Poly_Triangulation.InternalNodes(), into the triangulation.");
}

template <> inline void nanocct_def_views<Poly_ArrayOfUVNodes>(nb::class_<Poly_ArrayOfUVNodes> cls) {
    nanocct::def_aliased_nodes_view<Poly_ArrayOfUVNodes, 2>(cls,
        "Python addition: numpy's array protocol -- `numpy.asarray(uv)` is a zero-copy (Size(), 2) view of the "
        "UV nodes (R-VIEW), `numpy.array(uv)` a copy.\n\n"
        "The dtype follows the object: float64 when IsDoublePrecision() is true, float32 otherwise. A "
        "triangulation without UV nodes (HasUVNodes() false) has an empty array, i.e. a (0, 2) view. Writes go "
        "straight into the array.");
}

// ---- Image_PixMap --------------------------------------------------------------------------------------
// Two things make this the case that justifies the "how" being C++ rather than more TOML.
//
// Rows are padded. SizeRowBytes() is not always SizeX() * SizePixelBytes() -- measured, a FreeImage-loaded
// 5-pixel-wide RGB image has SizeRowBytes 16, not 15 -- so a shape-only view silently shears the image and
// the row stride has to come from SizeRowBytes().
//
// Rows may also run bottom-up. OCCT hides that behind Row(i): myTopRowPtr points at the *top* row and
// TopToDown is +1 or (size_t)-1, so Row(i) walks downwards either way (Image_PixMapData.hxx:95, :186).
// The view does the same -- it starts at Row(0) and takes a signed row stride -- so view[y, x] is
// PixelColor(x, y) whatever IsTopDown() says, instead of disagreeing with the class's own accessors.
#include <Image_PixMap.hxx>

template <> inline void nanocct_def_views<Image_PixMap>(nb::class_<Image_PixMap> cls) {
    cls.def("__array__", [](Image_PixMap &self, nb::handle, std::optional<bool> copy) {
            nb::dlpack::dtype dt{};
            size_t channels = 0;
            const auto set = [&dt, &channels](nb::dlpack::dtype_code theCode, uint8_t theBits, size_t theN) {
                dt = nb::dlpack::dtype{ (uint8_t) theCode, theBits, 1 };
                channels = theN;
            };
            using C = nb::dlpack::dtype_code;
            switch (self.Format()) {
                case Image_Format_Gray:        set(C::UInt, 8, 1); break;
                case Image_Format_Alpha:       set(C::UInt, 8, 1); break;
                case Image_Format_RGB:         set(C::UInt, 8, 3); break;
                case Image_Format_BGR:         set(C::UInt, 8, 3); break;
                case Image_Format_RGB32:       set(C::UInt, 8, 4); break;
                case Image_Format_BGR32:       set(C::UInt, 8, 4); break;
                case Image_Format_RGBA:        set(C::UInt, 8, 4); break;
                case Image_Format_BGRA:        set(C::UInt, 8, 4); break;
                case Image_Format_Gray16:      set(C::UInt, 16, 1); break;
                case Image_Format_GrayF:       set(C::Float, 32, 1); break;
                case Image_Format_AlphaF:      set(C::Float, 32, 1); break;
                case Image_Format_RGF:         set(C::Float, 32, 2); break;
                case Image_Format_RGBF:        set(C::Float, 32, 3); break;
                case Image_Format_BGRF:        set(C::Float, 32, 3); break;
                case Image_Format_RGBAF:       set(C::Float, 32, 4); break;
                case Image_Format_BGRAF:       set(C::Float, 32, 4); break;
                case Image_Format_GrayF_half:  set(C::Float, 16, 1); break;
                case Image_Format_RGF_half:    set(C::Float, 16, 2); break;
                case Image_Format_RGBAF_half:  set(C::Float, 16, 4); break;
                case Image_Format_UNKNOWN:     break;
            }
            // Image_Format_UNKNOWN: InitTrash() accepts it and allocates real bytes (measured: 4x4 gives 16),
            // but there is no dtype to give them. An error, rather than raw bytes that invent a meaning.
            if (channels == 0)
                throw nb::value_error("Image_PixMap.__array__: the pixel format is Image_Format_UNKNOWN");

            // An empty pixmap still has a format (Gray by default), hence a dtype: a (0, 0, channels) view.
            if (self.IsEmpty()) {
                const size_t shape[3] = { 0, 0, channels };
                return nanocct::array_protocol(nb::ndarray<nb::numpy>(nullptr, 3, shape, nb::handle(), nullptr, dt),
                                               nb::find(&self), copy);
            }

            // Both checks turn a layout assumption into an error the caller can read, rather than an array
            // that is quietly wrong. Neither has fired; they exist because a format table can go stale.
            const size_t itemsize = dt.bits / 8;
            if (self.SizePixelBytes() != itemsize * channels)
                throw std::runtime_error("Image_PixMap.__array__: SizePixelBytes() disagrees with the pixel format");
            if (self.SizeRowBytes() % itemsize != 0)
                throw std::runtime_error("Image_PixMap.__array__: SizeRowBytes() is not a whole number of components");

            const size_t shape[3] = { self.SizeY(), self.SizeX(), channels };
            const int64_t strides[3] = {
                (int64_t) (self.SizeRowBytes() / itemsize) * (int64_t) (ptrdiff_t) self.TopDownInc(),
                (int64_t) channels, 1 };
            return nanocct::array_protocol(nb::ndarray<nb::numpy>(self.ChangeRow(0), 3, shape, nb::handle(), strides, dt),
                                           nb::find(&self), copy);
        }, nb::arg("dtype") = nb::none(), nb::arg("copy") = nb::none(),
        "Python addition: numpy's array protocol -- `numpy.asarray(pixmap)` is a zero-copy (SizeY, SizeX, "
        "channels) view of the pixels (R-VIEW), `numpy.array(pixmap)` a copy. An empty pixmap gives a "
        "(0, 0, channels) view; Image_Format_UNKNOWN has no dtype and raises ValueError.\n\n"
        "The dtype and the channel count follow Format(): uint8 for the 8-bit formats, uint16 for Gray16, "
        "float32 for the F formats and float16 for the half ones. Channel *order* follows it too and is not "
        "normalised -- BGR stays BGR.\n\n"
        "Row order is top-down, matching Row() and PixelColor(), even when IsTopDown() is false: the view "
        "then has a negative row stride, which is a view and costs nothing. Rows are padded, so it is "
        "strided rather than contiguous whenever SizeRowBytes() exceeds SizeX() * SizePixelBytes().\n\n"
        "Writes go straight into the pixmap.");
}

// ---- NCollection_Buffer --------------------------------------------------------------------------------
// A plain byte buffer, and until it had a view the class was unusable from Python: Data()/ChangeData() are
// raw pointers, so nothing was bound but Size() and IsEmpty(). FSD_Base64::Decode *returns* one of these,
// which made that method unusable too. Graphic3d_Buffer derives from it and inherits the accessor; its
// elements are interleaved vertex attributes, so reshaping the bytes to (NbElements, Stride) and slicing by
// AttributeOffset() is the caller's business -- the buffer itself does not know a single element type.
#include <NCollection_Buffer.hxx>

template <> inline void nanocct_def_views<NCollection_Buffer>(nb::class_<NCollection_Buffer> cls) {
    cls.def("__array__", [](NCollection_Buffer &self, nb::handle, std::optional<bool> copy) {
            // Free() leaves IsEmpty() true and Size() 0 (measured): an unallocated buffer is simply empty.
            const size_t n = self.IsEmpty() ? 0 : self.Size();
            return nanocct::array_protocol(
                nb::ndarray<nb::numpy, uint8_t, nb::ndim<1>>(n == 0 ? nullptr : self.ChangeData(), { n }, nb::handle()),
                nb::find(&self), copy);
        }, nb::arg("dtype") = nb::none(), nb::arg("copy") = nb::none(),
        "Python addition: numpy's array protocol -- `numpy.asarray(buffer)` is a zero-copy (Size(),) uint8 view "
        "of the buffer (R-VIEW), `numpy.array(buffer)` a copy. An unallocated buffer (IsEmpty(), e.g. after "
        "Free()) gives a zero-length view.\n\n"
        "Writes go straight into the buffer. Reinterpreting the bytes as something else is numpy's job "
        "(`view(numpy.float32)`, `reshape(NbElements, Stride)` for a Graphic3d_Buffer).");
}
