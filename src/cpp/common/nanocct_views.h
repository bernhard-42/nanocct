// Zero-copy numpy views over OCCT's contiguous arrays (State.md 8.10, R-VIEW).
//
// The rule: array data that can get large crosses to Python as a view, never as a per-element loop. The
// generator decides *which* classes get views -- overrides.toml [views] classes -- and emits
// `nanocct_def_views<T>(cls);`; this header decides *how*, one specialisation per class.
//
// Why the "how" is C++ and not more TOML: every case has runtime branches that a config file cannot express.
// Poly_Triangulation's dtype depends on IsDoublePrecision(); its UV nodes and normals may be absent;
// Image_PixMap's rows are padded, so the view needs a stride from SizeRowBytes() rather than width*channels
// (measured: a FreeImage-loaded 5-pixel-wide RGB image has SizeRowBytes 16, not 15 -- a shape-only view would
// silently shear it). Keeping it in C++ makes it type-checked and greppable.
//
// Lifetime: every accessor uses nb::rv_policy::reference_internal, which ties the view to the owning object
// through the array's `base`. Verified on the stable ABI: dropping every Python reference to the owner leaves
// the view valid, and the owner is destroyed exactly when the last view goes.
#pragma once

#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

#include <stdexcept>

namespace nb = nanobind;

//! Declared, never defined: a class listed in overrides.toml [views] without a specialisation below is a link
//! error rather than a silently missing accessor. generator/tests assert the two lists agree, so it normally
//! fails at generation instead.
template <class T> void nanocct_def_views(nb::class_<T> cls);

// ---- Poly_Triangulation ------------------------------------------------------------------------------------
// Nodes are one contiguous allocation (Poly_ArrayOfNodes : NCollection_AliasedArray, a single
// Standard::AllocateAligned buffer) whose element is gp_Pnt (stride 24, float64) or NCollection_Vec3<float>
// (stride 12, float32) depending on IsDoublePrecision(); triangles are NCollection_Array1<Poly_Triangle> with
// sizeof(Poly_Triangle) == 12, three int32 and no vtable.
#include <Poly_Triangulation.hxx>

template <> inline void nanocct_def_views<Poly_Triangulation>(nb::class_<Poly_Triangulation> cls) {
    cls.def("NodesArray", [](Poly_Triangulation &self) {
            const size_t n = (size_t) self.NbNodes();
            size_t shape[2] = { n, 3 };
            return nb::ndarray<nb::numpy>(
                n == 0 ? nullptr : (void *) self.InternalNodes().changeValue(0), 2, shape, nb::handle(), nullptr,
                self.IsDoublePrecision() ? nb::dtype<double>() : nb::dtype<float>());
        }, nb::rv_policy::reference_internal,
        "Python addition: zero-copy (NbNodes, 3) view of the nodes.\n\n"
        "The dtype follows the object, not the binding: float64 when IsDoublePrecision() is true (OCCT's "
        "default) and float32 otherwise. Writes go straight into the triangulation.")
       .def("TrianglesArray", [](Poly_Triangulation &self) {
            const size_t n = (size_t) self.NbTriangles();
            return nb::ndarray<nb::numpy, int32_t, nb::ndim<2>>(
                n == 0 ? nullptr : (void *) &self.InternalTriangles().ChangeFirst(), { n, 3 }, nb::handle());
        }, nb::rv_policy::reference_internal,
        "Python addition: zero-copy (NbTriangles, 3) int32 view of the triangle node indices.\n\n"
        "The indices are OCCT's, i.e. 1-based into NodesArray().")
       .def("UVNodesArray", [](Poly_Triangulation &self) -> nb::object {
            if (!self.HasUVNodes())
                return nb::none();
            const size_t n = (size_t) self.NbNodes();
            size_t shape[2] = { n, 2 };
            return nb::cast(nb::ndarray<nb::numpy>(
                n == 0 ? nullptr : (void *) self.InternalUVNodes().changeValue(0), 2, shape, nb::handle(), nullptr,
                self.InternalUVNodes().IsDoublePrecision() ? nb::dtype<double>() : nb::dtype<float>()),
                nb::rv_policy::reference_internal, nb::find(&self));
        }, nb::rv_policy::reference_internal,
        nb::sig("def UVNodesArray(self) -> NDArray | None"),
        "Python addition: zero-copy (NbNodes, 2) view of the UV nodes, or None when HasUVNodes() is false.")
       .def("NormalsArray", [](Poly_Triangulation &self) -> nb::object {
            // Unlike the nodes and UV nodes, the normals are NOT an aliased array: InternalNormals() is an
            // NCollection_Array1<NCollection_Vec3<float>>, so they are always float32 and there is no
            // precision branch to make.
            if (!self.HasNormals())
                return nb::none();
            const size_t n = (size_t) self.NbNodes();
            return nb::cast(nb::ndarray<nb::numpy, float, nb::ndim<2>>(
                n == 0 ? nullptr : (void *) &self.InternalNormals().ChangeFirst(), { n, 3 }, nb::handle()),
                nb::rv_policy::reference_internal, nb::find(&self));
        }, nb::rv_policy::reference_internal,
        nb::sig("def NormalsArray(self) -> Annotated[NDArray[numpy.float32], dict(shape=(None, None))] | None"),
        "Python addition: zero-copy (NbNodes, 3) float32 view of the normals, or None when HasNormals() is "
        "false. Always float32: OCCT stores normals as NCollection_Vec3<float> whatever the node precision.");
}

// ---- Poly_PolygonOnTriangulation ----------------------------------------------------------------------------
// An edge's polyline as indices into the face triangulation's nodes: NCollection_Array1<int>, contiguous,
// reachable through public ChangeNodeArray(). The indices are OCCT's, i.e. 1-based.
#include <Poly_PolygonOnTriangulation.hxx>

template <> inline void nanocct_def_views<Poly_PolygonOnTriangulation>(
    nb::class_<Poly_PolygonOnTriangulation> cls) {
    cls.def("NodesArray", [](Poly_PolygonOnTriangulation &self) {
            const size_t n = (size_t) self.NbNodes();
            return nb::ndarray<nb::numpy, int32_t, nb::ndim<1>>(
                n == 0 ? nullptr : (void *) &self.ChangeNodeArray().ChangeFirst(), { n }, nb::handle());
        }, nb::rv_policy::reference_internal,
        "Python addition: zero-copy (NbNodes,) int32 view of the node indices.\n\n"
        "The indices are OCCT's, i.e. 1-based into the face triangulation's NodesArray().");
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
    cls.def("DataArray", [](Image_PixMap &self) -> nb::object {
            if (self.IsEmpty())
                return nb::none();

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
            if (channels == 0)
                return nb::none();                              // Image_Format_UNKNOWN

            // Both checks turn a layout assumption into an error the caller can read, rather than an array
            // that is quietly wrong. Neither has fired; they exist because a format table can go stale.
            const size_t itemsize = dt.bits / 8;
            if (self.SizePixelBytes() != itemsize * channels)
                throw std::runtime_error("DataArray: SizePixelBytes() disagrees with the pixel format");
            if (self.SizeRowBytes() % itemsize != 0)
                throw std::runtime_error("DataArray: SizeRowBytes() is not a whole number of components");

            const size_t shape[3] = { self.SizeY(), self.SizeX(), channels };
            const int64_t strides[3] = {
                (int64_t) (self.SizeRowBytes() / itemsize) * (int64_t) (ptrdiff_t) self.TopDownInc(),
                (int64_t) channels, 1 };
            return nb::cast(nb::ndarray<nb::numpy>(self.ChangeRow(0), 3, shape, nb::handle(), strides, dt),
                            nb::rv_policy::reference_internal, nb::find(&self));
        }, nb::rv_policy::reference_internal,
        nb::sig("def DataArray(self) -> NDArray | None"),
        "Python addition: zero-copy (SizeY, SizeX, channels) view of the pixels, or None when the pixmap is "
        "empty or its Image_Format is UNKNOWN.\n\n"
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
    cls.def("DataArray", [](NCollection_Buffer &self) -> nb::object {
            if (self.IsEmpty())
                return nb::none();
            return nb::cast(nb::ndarray<nb::numpy, uint8_t, nb::ndim<1>>(
                                self.ChangeData(), { self.Size() }, nb::handle()),
                            nb::rv_policy::reference_internal, nb::find(&self));
        }, nb::rv_policy::reference_internal,
        nb::sig("def DataArray(self) -> NDArray | None"),
        "Python addition: zero-copy (Size(),) uint8 view of the buffer, or None when no buffer is allocated "
        "(IsEmpty()). Measured: a buffer constructed with size 0 *is* allocated -- the allocator returns a "
        "non-null pointer for 0 bytes -- so that case is a zero-length array, and only Free() gives None.\n\n"
        "Writes go straight into the buffer. Reinterpreting the bytes as something else is numpy's job "
        "(`view(numpy.float32)`, `reshape(NbElements, Stride)` for a Graphic3d_Buffer).");
}
