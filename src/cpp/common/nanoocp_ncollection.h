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
#include <NCollection_HSequence.hxx>
#include <NCollection_List.hxx>
#include <NCollection_Sequence.hxx>

#define NANOOCP_DOC(tmpl, member) nanoocp_doc::tmpl::member

namespace nanoocp {

// T has operator== (needed by NCollection_List::Contains / Remove(item); gp_Pnt has none, TopoDS_Shape has)
template <typename T, typename = void> struct has_equal : std::false_type {};
template <typename T>
struct has_equal<T, std::void_t<decltype(std::declval<const T &>() == std::declval<const T &>())>> : std::true_type {};

// def() a member returning an element reference: a view (reference_internal) for class element types,
// a value for scalars and handles (nanobind policies are compile-time tags, hence if constexpr)
template <typename T, typename C, typename F, typename... Args>
void def_elem(C &&c, const char *name, F &&f, Args &&...args) {
    if constexpr (std::is_class_v<T>)
        c.def(name, std::forward<F>(f), nb::rv_policy::reference_internal, std::forward<Args>(args)...);
    else
        c.def(name, std::forward<F>(f), std::forward<Args>(args)...);
}

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

// ---------------------------------------------------------------------------------------------------
// NCollection_List<T>
template <typename T> void bind_NCollection_List(nb::module_ &m, const char *name) {
    using L = NCollection_List<T>;
    using It = typename L::Iterator;
    namespace D = nanoocp_doc::NCollection_List;
    nb::class_<L> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const L &>(), nb::arg("theList"), nb::keep_alive<1, 2>(), D::Iterator::ctor)
        .def("Initialize", [](It &self, const L &l) { self.Initialize(l); }, nb::arg("theList"), nb::keep_alive<1, 2>(), D::Iterator::Initialize)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> const T & { return self.Value(); }, D::Iterator::Value);
    def_elem<T>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), "ChangeValue", [](It &self) -> T & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theAllocator").none(), D::ctor)
     .def(nb::init<const L &>(), nb::arg("theOther"), D::ctor)
     .def("Extent", [](const L &self) { return self.Extent(); }, D::Extent)
     .def("Length", [](const L &self) { return self.Length(); }, D::Length)
     .def("Size", [](const L &self) { return self.Size(); }, D::Size)
     .def("IsEmpty", [](const L &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Allocator", [](const L &self) { return self.Allocator(); }, D::Allocator)
     .def("Assign", [](L &self, const L &o) -> L & { return self.Assign(o); }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("Clear", [](L &self, const opencascade::handle<NCollection_BaseAllocator> &a) { self.Clear(a); },
          nb::arg("theAllocator").none() = static_cast<opencascade::handle<NCollection_BaseAllocator>>(nullptr), D::Clear)
     .def("First", [](const L &self) -> const T & { return self.First(); }, D::First)
     .def("Last", [](const L &self) -> const T & { return self.Last(); }, D::Last)
     .def("Append", [](L &self, const T &v, It &it) { self.Append(v, it); }, nb::arg("theItem"), nb::arg("theIter"), D::Append)
     .def("Append", [](L &self, L &other) { self.Append(other); }, nb::arg("theOther"), D::Append)
     .def("Prepend", [](L &self, L &other) { self.Prepend(other); }, nb::arg("theOther"), D::Prepend)
     .def("RemoveFirst", [](L &self) { self.RemoveFirst(); }, D::RemoveFirst)
     .def("Remove", [](L &self, It &it) { self.Remove(it); }, nb::arg("theIter"), D::Remove)
     .def("InsertBefore", [](L &self, L &other, It &it) { self.InsertBefore(other, it); }, nb::arg("theOther"), nb::arg("theIter"), D::InsertBefore)
     .def("InsertAfter", [](L &self, L &other, It &it) { self.InsertAfter(other, it); }, nb::arg("theOther"), nb::arg("theIter"), D::InsertAfter)
     .def("Reverse", [](L &self) { self.Reverse(); }, D::Reverse)
     .def("Exchange", [](L &self, L &other) { self.Exchange(other); }, nb::arg("theOther"), D::Exchange)
     // Python additions
     .def("__len__", [](const L &self) { return self.Extent(); }, "Python addition: alias to Extent.")
     .def("__iter__", [](const L &self) { return nb::make_iterator(nb::type<L>(), "value_iterator", self.begin(), self.end()); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the values.");
    // members returning the (inserted) element reference: view for class types, value otherwise
    def_elem<T>(c, "Append", [](L &self, const T &v) -> T & { return self.Append(v); }, nb::arg("theItem"), D::Append);
    def_elem<T>(c, "Prepend", [](L &self, const T &v) -> T & { return self.Prepend(v); }, nb::arg("theItem"), D::Prepend);
    def_elem<T>(c, "InsertBefore", [](L &self, const T &v, It &it) -> T & { return self.InsertBefore(v, it); }, nb::arg("theItem"), nb::arg("theIter"), D::InsertBefore);
    def_elem<T>(c, "InsertAfter", [](L &self, const T &v, It &it) -> T & { return self.InsertAfter(v, it); }, nb::arg("theItem"), nb::arg("theIter"), D::InsertAfter);
    if constexpr (has_equal<T>::value) {
        c.def("Contains", [](const L &self, const T &v) { return self.Contains(v); }, nb::arg("theObject"), D::Contains)
         .def("Remove", [](L &self, const T &v) { return self.Remove(v); }, nb::arg("theObject"), D::Remove)
         .def("__contains__", [](const L &self, const T &v) { return self.Contains(v); }, nb::arg("theObject"), "Python addition: alias to Contains.");
    }
}

// ---------------------------------------------------------------------------------------------------
// NCollection_Sequence<T> (shared with NCollection_HSequence<T>)
template <typename T, typename Cls, typename... Extra> void def_sequence_members(nb::class_<Cls, Extra...> &c) {
    using S = NCollection_Sequence<T>;
    using It = typename S::Iterator;
    namespace D = nanoocp_doc::NCollection_Sequence;
    // size_t overloads duplicate the int ones (Python cannot tell them apart): int only; At/ChangeAt are size_t-only
    c.def("Length", [](const Cls &self) { return self.Length(); }, D::Length)
     .def("Size", [](const Cls &self) { return self.Size(); }, D::Size)
     .def("IsEmpty", [](const Cls &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Lower", [](const Cls &self) { return self.Lower(); }, D::Lower)
     .def("Upper", [](const Cls &self) { return self.Upper(); }, D::Upper)
     .def("Allocator", [](const Cls &self) { return self.Allocator(); }, D::Allocator)
     .def("Reverse", [](Cls &self) { self.Reverse(); }, D::Reverse)
     .def("Exchange", [](Cls &self, const int i, const int j) { self.Exchange(i, j); }, nb::arg("I"), nb::arg("J"), D::Exchange)
     .def("Clear", [](Cls &self, const opencascade::handle<NCollection_BaseAllocator> &a) { self.Clear(a); },
          nb::arg("theAllocator").none() = static_cast<opencascade::handle<NCollection_BaseAllocator>>(nullptr), D::Clear)
     .def("Assign", [](Cls &self, const S &o) -> Cls & { self.Assign(o); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("Remove", [](Cls &self, It &it) { self.Remove(it); }, nb::arg("thePosition"), D::Remove)
     .def("Remove", [](Cls &self, const int i) { self.Remove(i); }, nb::arg("theIndex"), D::Remove)
     .def("Remove", [](Cls &self, const int from, const int to) { self.Remove(from, to); }, nb::arg("theFromIndex"), nb::arg("theToIndex"), D::Remove)
     .def("Append", [](Cls &self, const T &v) { self.Append(v); }, nb::arg("theItem"), D::Append)
     .def("Append", [](Cls &self, S &other) { self.Append(other); }, nb::arg("theSeq"), D::Append)
     .def("Prepend", [](Cls &self, const T &v) { self.Prepend(v); }, nb::arg("theItem"), D::Prepend)
     .def("Prepend", [](Cls &self, S &other) { self.Prepend(other); }, nb::arg("theSeq"), D::Prepend)
     .def("InsertBefore", [](Cls &self, const int i, const T &v) { self.InsertBefore(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::InsertBefore)
     .def("InsertBefore", [](Cls &self, const int i, S &other) { self.InsertBefore(i, other); }, nb::arg("theIndex"), nb::arg("theSeq"), D::InsertBefore)
     .def("InsertAfter", [](Cls &self, It &it, const T &v) { self.InsertAfter(it, v); }, nb::arg("thePosition"), nb::arg("theItem"), D::InsertAfter)
     .def("InsertAfter", [](Cls &self, const int i, S &other) { self.InsertAfter(i, other); }, nb::arg("theIndex"), nb::arg("theSeq"), D::InsertAfter)
     .def("InsertAfter", [](Cls &self, const int i, const T &v) { self.InsertAfter(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::InsertAfter)
     .def("Split", [](Cls &self, const int i, S &sub) { self.Split(i, sub); }, nb::arg("theIndex"), nb::arg("theSeq"), D::Split)
     .def("First", [](const Cls &self) -> const T & { return self.First(); }, D::First)
     .def("Last", [](const Cls &self) -> const T & { return self.Last(); }, D::Last)
     .def("Value", [](const Cls &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::Value)
     .def("At", [](const Cls &self, const size_t i) -> const T & { return self.At(i); }, nb::arg("theIndex"), D::At)
     .def("SetValue", [](Cls &self, const int i, const T &v) { self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::SetValue)
     .def("__call__", [](const Cls &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_call)
     // Python additions
     .def("__getitem__", [](const Cls &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), "Python addition: alias to Value (OCCT index, 1-based).")
     .def("__setitem__", [](Cls &self, const int i, const T &v) { self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), "Python addition: alias to SetValue (OCCT index).")
     .def("__len__", [](const Cls &self) { return self.Length(); }, "Python addition: alias to Length.")
     .def("__iter__", [](const Cls &self) { return nb::make_iterator(nb::type<Cls>(), "value_iterator", self.cbegin(), self.cend()); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the values.");
    if constexpr (std::is_class_v<T>) {
        c.def("ChangeFirst", [](Cls &self) -> T & { return self.ChangeFirst(); }, nb::rv_policy::reference_internal, D::ChangeFirst)
         .def("ChangeLast", [](Cls &self) -> T & { return self.ChangeLast(); }, nb::rv_policy::reference_internal, D::ChangeLast)
         .def("ChangeValue", [](Cls &self, const int i) -> T & { return self.ChangeValue(i); }, nb::rv_policy::reference_internal, nb::arg("theIndex"), D::ChangeValue)
         .def("ChangeAt", [](Cls &self, const size_t i) -> T & { return self.ChangeAt(i); }, nb::rv_policy::reference_internal, nb::arg("theIndex"), D::ChangeAt);
    }
}

template <typename T> void bind_NCollection_Sequence(nb::module_ &m, const char *name) {
    using S = NCollection_Sequence<T>;
    using It = typename S::Iterator;
    namespace D = nanoocp_doc::NCollection_Sequence;
    nb::class_<S> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const S &, const bool>(), nb::arg("theSeq"), nb::arg("isStart") = true, nb::keep_alive<1, 2>(), D::Iterator::ctor)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> const T & { return self.Value(); }, D::Iterator::Value);
    def_elem<T>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), "ChangeValue", [](It &self) -> T & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theAllocator").none(), D::ctor)
     .def(nb::init<const S &>(), nb::arg("theOther"), D::ctor)
     .def(nb::init<const NCollection_HSequence<T> &>(), nb::arg("theHSequence"), "Python addition: copy from an HSequence (C++ derived-to-base conversion).");
    def_sequence_members<T, S>(c);
}

template <typename T> void bind_NCollection_HSequence(nb::module_ &m, const char *name) {
    using S = NCollection_Sequence<T>;
    using H = NCollection_HSequence<T>;
    namespace D = nanoocp_doc::NCollection_HSequence;
    nb::class_<H, Standard_Transient> c(m, name, D::class_doc);
    c.def(nb::new_([]() { return opencascade::handle<H>(new H()); }), D::ctor)
     .def(nb::new_([](const S &s) { return opencascade::handle<H>(new H(s)); }), nb::arg("theOther"), D::ctor)
     .def("Sequence", [](const H &self) { return S(self.Sequence()); }, D::Sequence)      // sliced copy, see HArray1
     .def("ChangeSequence", [](H &self) -> S & { return self.ChangeSequence(); }, nb::rv_policy::reference_internal, D::ChangeSequence);
    def_sequence_members<T, H>(c);
    nb::implicitly_convertible<H, S>();
}

} // namespace nanoocp
