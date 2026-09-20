// Hand-written binders for the OCCT NCollection container templates (Design.md, section 6a).
// One binder per template kind; the generator instantiates it for every typedef (TColgp_Array1OfPnt =
// NCollection_Array1<gp_Pnt>, ...) and for every instantiation that appears in a bound signature.
// Method names, signatures and docstrings are 1:1 with the template header; the docstrings live in
// the generated ncollection_docs.h. Python protocol methods (__len__, __iter__, __setitem__) are
// additions, never replacements.
#pragma once
#include "nanoocp_common.h"
#include "ncollection_docs.h"

#include <nanobind/make_iterator.h>

#include <NCollection_Array1.hxx>
#include <NCollection_HArray1.hxx>

#define NANOOCP_DOC(tmpl, member) nanoocp_doc::tmpl::member

namespace nanoocp {

// Array1 members shared by NCollection_Array1<T> and NCollection_HArray1<T>. Cls is the bound class,
// A the NCollection_Array1<T> it is (or derives from).
template <typename T, typename Cls, typename... Extra> void def_array1_members(nb::class_<Cls, Extra...> &c) {
    using A = NCollection_Array1<T>;
    namespace D = nanoocp_doc::NCollection_Array1;
    c.def("Init", [](Cls &self, const T &v) { self.Init(v); }, nb::arg("theValue"), D::Init)
     .def("Size", [](const Cls &self) { return self.Size(); }, D::Size)
     .def("Length", [](const Cls &self) { return self.Length(); }, D::Length)
     .def("IsEmpty", [](const Cls &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Lower", [](const Cls &self) { return self.Lower(); }, D::Lower)
     .def("Upper", [](const Cls &self) { return self.Upper(); }, D::Upper)
     .def("IsDeletable", [](const Cls &self) { return self.IsDeletable(); }, D::IsDeletable)
     .def("Assign", [](Cls &self, const A &other) -> Cls & { self.Assign(other); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("CopyValues", [](Cls &self, const A &other) -> Cls & { self.CopyValues(other); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::CopyValues)
     .def("First", [](const Cls &self) -> const T & { return self.First(); }, D::First)
     .def("Last", [](const Cls &self) -> const T & { return self.Last(); }, D::Last)
     .def("Value", [](const Cls &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::Value)
     .def("At", [](const Cls &self, const size_t i) -> const T & { return self.At(i); }, nb::arg("theIndex"), D::At)
     .def("SetValue", [](Cls &self, const int i, const T &v) { self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::SetValue)
     .def("UpdateLowerBound", [](Cls &self, const int l) { self.UpdateLowerBound(l); }, nb::arg("theLower"), D::UpdateLowerBound)
     .def("UpdateUpperBound", [](Cls &self, const int u) { self.UpdateUpperBound(u); }, nb::arg("theUpper"), D::UpdateUpperBound)
     .def("Resize", [](Cls &self, const int l, const int u, const bool copy) { self.Resize(l, u, copy); }, nb::arg("theLower"), nb::arg("theUpper"), nb::arg("theToCopyData"), D::Resize)
     .def("Resize", [](Cls &self, const size_t n, const bool copy) { self.Resize(n, copy); }, nb::arg("theSize"), nb::arg("theToCopyData"), D::Resize)
     // operator() and operator[] are OCCT's own aliases of Value (OCCT index, not 0-based)
     .def("__call__", [](const Cls &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_call)
     .def("__getitem__", [](const Cls &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_index)
     // Python additions
     .def("__setitem__", [](Cls &self, const int i, const T &v) { self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), "Python addition: alias to SetValue (OCCT index).")
     .def("__len__", [](const Cls &self) { return self.Length(); }, "Python addition: alias to Length.")
     .def("__iter__", [](const Cls &self) { return nb::make_iterator(nb::type<Cls>(), "iterator", self.begin(), self.end()); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the values from Lower() to Upper().");
    if constexpr (std::is_class_v<T>) {
        // mutable references only make sense for class element types (a double& cannot be exposed)
        c.def("ChangeFirst", [](Cls &self) -> T & { return self.ChangeFirst(); }, nb::rv_policy::reference_internal, D::ChangeFirst)
         .def("ChangeLast", [](Cls &self) -> T & { return self.ChangeLast(); }, nb::rv_policy::reference_internal, D::ChangeLast)
         .def("ChangeValue", [](Cls &self, const int i) -> T & { return self.ChangeValue(i); }, nb::rv_policy::reference_internal, nb::arg("theIndex"), D::ChangeValue)
         .def("ChangeAt", [](Cls &self, const size_t i) -> T & { return self.ChangeAt(i); }, nb::rv_policy::reference_internal, nb::arg("theIndex"), D::ChangeAt);
    }
}

template <typename T> void bind_NCollection_Array1(nb::module_ &m, const char *name) {
    using A = NCollection_Array1<T>;
    namespace D = nanoocp_doc::NCollection_Array1;
    nb::class_<A> c(m, name, D::class_doc);
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const int, const int>(), nb::arg("theLower"), nb::arg("theUpper"), D::ctor)
     .def(nb::init<const size_t>(), nb::arg("theSize"), D::ctor)
     .def(nb::init<const A &>(), nb::arg("theOther"), D::ctor)
     // Python addition: C++ converts HArray1 -> Array1 through inheritance; nanobind needs the overload
     .def(nb::init<const NCollection_HArray1<T> &>(), nb::arg("theHArray"), "Python addition: copy from an HArray1 (C++ derived-to-base conversion).");
    def_array1_members<T, A>(c);
}

template <typename T> void bind_NCollection_HArray1(nb::module_ &m, const char *name) {
    using A = NCollection_Array1<T>;
    using H = NCollection_HArray1<T>;
    namespace D = nanoocp_doc::NCollection_HArray1;
    // nanobind supports one base: Standard_Transient (handle semantics, IsKind, ...). The Array1 API is
    // bound on the class itself and an implicit conversion to NCollection_Array1<T> (a copy) lets an
    // HArray1 be passed where C++ takes const NCollection_Array1<T>&.
    nb::class_<H, Standard_Transient> c(m, name, D::class_doc);
    c.def(nb::new_([]() { return opencascade::handle<H>(new H()); }), D::ctor)
     .def(nb::new_([](const int l, const int u) { return opencascade::handle<H>(new H(l, u)); }), nb::arg("theLower"), nb::arg("theUpper"), D::ctor)
     .def(nb::new_([](const int l, const int u, const T &v) { return opencascade::handle<H>(new H(l, u, v)); }), nb::arg("theLower"), nb::arg("theUpper"), nb::arg("theValue"), D::ctor)
     .def(nb::new_([](const A &a) { return opencascade::handle<H>(new H(a)); }), nb::arg("theOther"), D::ctor)
     // Array1 is polymorphic (virtual dtor), so returning const A& would make nanobind copy the dynamic type
     // (an HArray1); slice explicitly so that the result is a plain NCollection_Array1<T>
     .def("Array1", [](const H &self) { return A(self.Array1()); }, D::Array1)
     .def("ChangeArray1", [](H &self) -> A & { return self.ChangeArray1(); }, nb::rv_policy::reference_internal, D::ChangeArray1);
    def_array1_members<T, H>(c);
    nb::implicitly_convertible<H, A>();
}

} // namespace nanoocp
