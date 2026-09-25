// Zero-copy numpy views over OCCT's contiguous arrays (State.md 8.10, R-VIEW).
//
// The rule: array data that can get large crosses to Python as a view, never as a per-element loop. The
// generator decides *which* classes get views -- overrides.toml [views] classes -- and emits
// `nanoocp_def_views<T>(cls);`; this header decides *how*, one specialisation per class.
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

namespace nb = nanobind;

//! Declared, never defined: a class listed in overrides.toml [views] without a specialisation below is a link
//! error rather than a silently missing accessor. generator/tests assert the two lists agree, so it normally
//! fails at generation instead.
template <class T> void nanoocp_def_views(nb::class_<T> cls);

// ---- Poly_Triangulation ------------------------------------------------------------------------------------
// Nodes are one contiguous allocation (Poly_ArrayOfNodes : NCollection_AliasedArray, a single
// Standard::AllocateAligned buffer) whose element is gp_Pnt (stride 24, float64) or NCollection_Vec3<float>
// (stride 12, float32) depending on IsDoublePrecision(); triangles are NCollection_Array1<Poly_Triangle> with
// sizeof(Poly_Triangle) == 12, three int32 and no vtable.
#include <Poly_Triangulation.hxx>

template <> inline void nanoocp_def_views<Poly_Triangulation>(nb::class_<Poly_Triangulation> cls) {
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
        "Python addition: zero-copy (NbNodes, 3) float32 view of the normals, or None when HasNormals() is "
        "false. Always float32: OCCT stores normals as NCollection_Vec3<float> whatever the node precision.");
}
