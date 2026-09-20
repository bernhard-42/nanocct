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
#include <NCollection_DataMap.hxx>
#include <NCollection_DefaultHasher.hxx>
#include <NCollection_HArray1.hxx>
#include <NCollection_HSequence.hxx>
#include <NCollection_IndexedDataMap.hxx>
#include <NCollection_IndexedMap.hxx>
#include <NCollection_List.hxx>
#include <NCollection_Map.hxx>
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

// ---------------------------------------------------------------------------------------------------
// hashed containers: members of NCollection_BaseMap plus constructors shared by all four kinds
inline const opencascade::handle<NCollection_BaseAllocator> null_allocator = nullptr;

struct BaseMapDocs {
    const char *ctor, *NbBuckets, *Extent, *Length, *Size, *IsEmpty, *Allocator, *Exchange, *Assign, *ReSize, *Clear;
};
#define NANOOCP_BASEMAP_DOCS(D) \
    nanoocp::BaseMapDocs{D::ctor, D::NbBuckets, D::Extent, D::Length, D::Size, D::IsEmpty, D::Allocator, D::Exchange, D::Assign, D::ReSize, D::Clear}

template <typename M, typename... Extra> void def_basemap_members(nb::class_<M, Extra...> &c, const BaseMapDocs &D) {
    c.def(nb::init<>(), D.ctor)
     .def(nb::init<const int, const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theNbBuckets"),
          nb::arg("theAllocator").none() = null_allocator, D.ctor)
     .def(nb::init<const M &>(), nb::arg("theOther"), D.ctor)
     .def("NbBuckets", [](const M &self) { return self.NbBuckets(); }, D.NbBuckets)
     .def("Extent", [](const M &self) { return self.Extent(); }, D.Extent)
     .def("Length", [](const M &self) { return self.Length(); }, D.Length)
     .def("Size", [](const M &self) { return self.Size(); }, D.Size)
     .def("IsEmpty", [](const M &self) { return self.IsEmpty(); }, D.IsEmpty)
     .def("Allocator", [](const M &self) { return self.Allocator(); }, D.Allocator)
     .def("Exchange", [](M &self, M &other) { self.Exchange(other); }, nb::arg("theOther"), D.Exchange)
     .def("Assign", [](M &self, const M &other) -> M & { return self.Assign(other); }, nb::rv_policy::reference, nb::arg("theOther"), D.Assign)
     .def("ReSize", [](M &self, const int n) { self.ReSize(n); }, nb::arg("N"), D.ReSize)
     .def("Clear", [](M &self, const bool release) { self.Clear(release); }, nb::arg("doReleaseMemory") = true, D.Clear)
     .def("Clear", [](M &self, const opencascade::handle<NCollection_BaseAllocator> &a) { self.Clear(a); }, nb::arg("theAllocator").none(), D.Clear)
     .def("__len__", [](const M &self) { return self.Extent(); }, "Python addition: alias to Extent.");
}

// iterate over the keys (Map/IndexedMap: Value(); DataMap/IndexedDataMap: Key()) of a hashed container
template <typename M, typename It, typename Get> auto key_iterator(nb::handle scope, const M &self, Get get) {
    // nb::make_iterator needs C++ iterators; wrap OCCT's More/Next protocol in a minimal forward iterator
    struct Cursor {
        It it; Get get;
        bool operator==(const Cursor &o) const { return it.More() == o.it.More(); }
        bool operator!=(const Cursor &o) const { return !(*this == o); }
        Cursor &operator++() { it.Next(); return *this; }
        decltype(auto) operator*() const { return get(it); }
    };
    return nb::make_iterator(scope, "key_iterator", Cursor{It(self), get}, Cursor{It(), get});
}


// ---- NCollection_Map<K, Hasher>
template <typename K, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_Map(nb::module_ &m, const char *name) {
    using M = NCollection_Map<K, H>;
    using It = typename M::Iterator;
    namespace D = nanoocp_doc::NCollection_Map;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), D::Iterator::ctor)
        .def("Initialize", [](It &self, const M &map) { self.Initialize(map); }, nb::arg("theMap"), nb::keep_alive<1, 2>(), D::Iterator::Initialize)
        .def("Reset", [](It &self) { self.Reset(); }, D::Iterator::Reset)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> const K & { return self.Value(); }, D::Iterator::Value)
        .def("Key", [](const It &self) -> const K & { return self.Key(); }, D::Iterator::Key);
    def_basemap_members(c, NANOOCP_BASEMAP_DOCS(D));
    c.def("Add", [](M &self, const K &k) { return self.Add(k); }, nb::arg("theKey"), D::Add)
     .def("Added", [](M &self, const K &k) -> const K & { return self.Added(k); }, nb::arg("theKey"), D::Added)
     .def("Contains", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), D::Contains)
     .def("Contains", [](const M &self, const M &other) { return self.Contains(other); }, nb::arg("theOther"), D::Contains)
     .def("Remove", [](M &self, const K &k) { return self.Remove(k); }, nb::arg("theKey"), D::Remove)
     .def("IsEqual", [](const M &self, const M &other) { return self.IsEqual(other); }, nb::arg("theOther"), D::IsEqual)
     .def("Union", [](M &self, const M &a, const M &b) { self.Union(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Union)
     .def("Unite", [](M &self, const M &other) { return self.Unite(other); }, nb::arg("theOther"), D::Unite)
     .def("HasIntersection", [](const M &self, const M &other) { return self.HasIntersection(other); }, nb::arg("theMap"), D::HasIntersection)
     .def("Intersection", [](M &self, const M &a, const M &b) { self.Intersection(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Intersection)
     .def("Intersect", [](M &self, const M &other) { return self.Intersect(other); }, nb::arg("theOther"), D::Intersect)
     .def("Subtraction", [](M &self, const M &a, const M &b) { self.Subtraction(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Subtraction)
     .def("Subtract", [](M &self, const M &other) { return self.Subtract(other); }, nb::arg("theOther"), D::Subtract)
     .def("Difference", [](M &self, const M &a, const M &b) { self.Difference(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Difference)
     .def("Differ", [](M &self, const M &other) { return self.Differ(other); }, nb::arg("theOther"), D::Differ)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), "Python addition: alias to Contains.")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Key(); }); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the keys.");
}

// ---- NCollection_DataMap<K, V, Hasher>
template <typename K, typename V, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_DataMap(nb::module_ &m, const char *name) {
    using M = NCollection_DataMap<K, V, H>;
    using It = typename M::Iterator;
    namespace D = nanoocp_doc::NCollection_DataMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It> it(c, "Iterator", D::Iterator::class_doc);
    it.def(nb::init<>(), D::Iterator::ctor)
      .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), D::Iterator::ctor)
      .def("Initialize", [](It &self, const M &map) { self.Initialize(map); }, nb::arg("theMap"), nb::keep_alive<1, 2>(), D::Iterator::Initialize)
      .def("Reset", [](It &self) { self.Reset(); }, D::Iterator::Reset)
      .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
      .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
      .def("Value", [](const It &self) -> const V & { return self.Value(); }, D::Iterator::Value)
      .def("Key", [](const It &self) -> const K & { return self.Key(); }, D::Iterator::Key);
    def_elem<V>(it, "ChangeValue", [](It &self) -> V & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    def_basemap_members(c, NANOOCP_BASEMAP_DOCS(D));
    c.def("Bind", [](M &self, const K &k, const V &v) { return self.Bind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bind)
     .def("TryBind", [](M &self, const K &k, const V &v) { return self.TryBind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBind)
     .def("IsBound", [](const M &self, const K &k) { return self.IsBound(k); }, nb::arg("theKey"), D::IsBound)
     .def("UnBind", [](M &self, const K &k) { return self.UnBind(k); }, nb::arg("theKey"), D::UnBind)
     .def("Find", [](const M &self, const K &k) -> const V & { return self.Find(k); }, nb::arg("theKey"), D::Find)
     .def("__call__", [](const M &self, const K &k) -> const V & { return self.Find(k); }, nb::arg("theKey"), D::op_call)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.IsBound(k); }, nb::arg("theKey"), "Python addition: alias to IsBound.")
     .def("__getitem__", [](const M &self, const K &k) -> const V & { return self.Find(k); }, nb::arg("theKey"), "Python addition: alias to Find.")
     .def("__setitem__", [](M &self, const K &k, const V &v) { self.Bind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), "Python addition: alias to Bind.")
     .def("__delitem__", [](M &self, const K &k) { if (!self.UnBind(k)) throw nb::key_error(); }, nb::arg("theKey"), "Python addition: UnBind, KeyError if the key is not bound.")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Key(); }); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the keys.")
     .def("items", [](const M &self) {
              nb::list out;
              for (It it(self); it.More(); it.Next()) out.append(nb::make_tuple(it.Key(), it.Value()));
              return out; }, "Python addition: list of (key, value) tuples.");
    // element references: view for class V, value for scalars/handles
    def_elem<V>(c, "Bound", [](M &self, const K &k, const V &v) -> V & { return *self.Bound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bound);
    def_elem<V>(c, "TryBound", [](M &self, const K &k, const V &v) -> V & { return self.TryBound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBound);
    def_elem<V>(c, "ChangeFind", [](M &self, const K &k) -> V & { return self.ChangeFind(k); }, nb::arg("theKey"), D::ChangeFind);
    // Seek: nullptr when absent -> None
    if constexpr (std::is_class_v<V>) {
        c.def("Seek", [](const M &self, const K &k) -> const V * { return self.Seek(k); }, nb::rv_policy::reference_internal, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> V * { return self.ChangeSeek(k); }, nb::rv_policy::reference_internal, nb::arg("theKey"), D::ChangeSeek)
         .def("Find", [](const M &self, const K &k, V &v) { return self.Find(k, v); }, nb::arg("theKey"), nb::arg("theValue"), D::Find);
    } else {
        c.def("Seek", [](const M &self, const K &k) -> std::optional<V> { const V *p = self.Seek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> std::optional<V> { V *p = self.ChangeSeek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::ChangeSeek);
    }
}

// ---- NCollection_IndexedMap<K, Hasher>
template <typename K, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_IndexedMap(nb::module_ &m, const char *name) {
    using M = NCollection_IndexedMap<K, H>;
    using It = typename M::Iterator;
    namespace D = nanoocp_doc::NCollection_IndexedMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), D::Iterator::ctor)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> const K & { return self.Value(); }, D::Iterator::Value)
        .def("Index", [](const It &self) { return self.Index(); }, D::Iterator::Index)
        .def("IsEqual", [](const It &self, const It &o) { return self.IsEqual(o); }, nb::arg("theOther"), D::Iterator::IsEqual);
    def_basemap_members(c, NANOOCP_BASEMAP_DOCS(D));
    c.def("Add", [](M &self, const K &k) { return self.Add(k); }, nb::arg("theKey"), D::Add)
     .def("Added", [](M &self, const K &k) -> const K & { return self.Added(k); }, nb::arg("theKey"), D::Added)
     .def("Contains", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), D::Contains)
     .def("Substitute", [](M &self, const int i, const K &k) { self.Substitute(i, k); }, nb::arg("theIndex"), nb::arg("theKey"), D::Substitute)
     .def("Swap", [](M &self, const int i, const int j) { self.Swap(i, j); }, nb::arg("theIndex1"), nb::arg("theIndex2"), D::Swap)
     .def("RemoveLast", [](M &self) { self.RemoveLast(); }, D::RemoveLast)
     .def("RemoveFromIndex", [](M &self, const int i) { self.RemoveFromIndex(i); }, nb::arg("theIndex"), D::RemoveFromIndex)
     .def("RemoveKey", [](M &self, const K &k) { return self.RemoveKey(k); }, nb::arg("theKey"), D::RemoveKey)
     .def("FindKey", [](const M &self, const int i) -> const K & { return self.FindKey(i); }, nb::arg("theIndex"), D::FindKey)
     .def("__call__", [](const M &self, const int i) -> const K & { return self.FindKey(i); }, nb::arg("theIndex"), D::op_call)
     .def("FindIndex", [](const M &self, const K &k) { return self.FindIndex(k); }, nb::arg("theKey"), D::FindIndex)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), "Python addition: alias to Contains.")
     .def("__getitem__", [](const M &self, const int i) -> const K & { return self.FindKey(i); }, nb::arg("theIndex"), "Python addition: alias to FindKey (1-based index).")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Value(); }); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the keys in index order.");
}

// ---- NCollection_IndexedDataMap<K, V, Hasher>
template <typename K, typename V, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_IndexedDataMap(nb::module_ &m, const char *name) {
    using M = NCollection_IndexedDataMap<K, V, H>;
    using It = typename M::Iterator;
    namespace D = nanoocp_doc::NCollection_IndexedDataMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It> it(c, "Iterator", D::Iterator::class_doc);
    it.def(nb::init<>(), D::Iterator::ctor)
      .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), D::Iterator::ctor)
      .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
      .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
      .def("Value", [](const It &self) -> const V & { return self.Value(); }, D::Iterator::Value)
      .def("Key", [](const It &self) -> const K & { return self.Key(); }, D::Iterator::Key)
      .def("Index", [](const It &self) { return self.Index(); }, D::Iterator::Index)
      .def("IsEqual", [](const It &self, const It &o) { return self.IsEqual(o); }, nb::arg("theOther"), D::Iterator::IsEqual);
    def_elem<V>(it, "ChangeValue", [](It &self) -> V & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    def_basemap_members(c, NANOOCP_BASEMAP_DOCS(D));
    c.def("Add", [](M &self, const K &k, const V &v) { return self.Add(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Add)
     .def("TryBind", [](M &self, const K &k, const V &v) { return self.TryBind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBind)
     .def("Bind", [](M &self, const K &k, const V &v) { return self.Bind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bind)
     .def("Contains", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), D::Contains)
     .def("Substitute", [](M &self, const int i, const K &k, const V &v) { self.Substitute(i, k, v); }, nb::arg("theIndex"), nb::arg("theKey"), nb::arg("theItem"), D::Substitute)
     .def("Swap", [](M &self, const int i, const int j) { self.Swap(i, j); }, nb::arg("theIndex1"), nb::arg("theIndex2"), D::Swap)
     .def("RemoveLast", [](M &self) { self.RemoveLast(); }, D::RemoveLast)
     .def("RemoveFromIndex", [](M &self, const int i) { self.RemoveFromIndex(i); }, nb::arg("theIndex"), D::RemoveFromIndex)
     .def("RemoveKey", [](M &self, const K &k) { self.RemoveKey(k); }, nb::arg("theKey"), D::RemoveKey)
     .def("FindKey", [](const M &self, const int i) -> const K & { return self.FindKey(i); }, nb::arg("theIndex"), D::FindKey)
     .def("FindFromIndex", [](const M &self, const int i) -> const V & { return self.FindFromIndex(i); }, nb::arg("theIndex"), D::FindFromIndex)
     .def("__call__", [](const M &self, const int i) -> const V & { return self.FindFromIndex(i); }, nb::arg("theIndex"), D::op_call)
     .def("FindIndex", [](const M &self, const K &k) { return self.FindIndex(k); }, nb::arg("theKey"), D::FindIndex)
     .def("FindFromKey", [](const M &self, const K &k) -> const V & { return self.FindFromKey(k); }, nb::arg("theKey"), D::FindFromKey)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), "Python addition: alias to Contains.")
     .def("__getitem__", [](const M &self, const int i) -> const V & { return self.FindFromIndex(i); }, nb::arg("theIndex"), "Python addition: alias to FindFromIndex (1-based index).")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Key(); }); },
          nb::keep_alive<0, 1>(), "Python addition: iterates over the keys in index order.")
     .def("items", [](const M &self) {
              nb::list out;
              for (It it(self); it.More(); it.Next()) out.append(nb::make_tuple(it.Key(), it.Value()));
              return out; }, "Python addition: list of (key, value) tuples in index order.");
    def_elem<V>(c, "TryBound", [](M &self, const K &k, const V &v) -> V & { return self.TryBound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBound);
    def_elem<V>(c, "Bound", [](M &self, const K &k, const V &v) -> V & { return *self.Bound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bound);
    def_elem<V>(c, "ChangeFromIndex", [](M &self, const int i) -> V & { return self.ChangeFromIndex(i); }, nb::arg("theIndex"), D::ChangeFromIndex);
    def_elem<V>(c, "ChangeFromKey", [](M &self, const K &k) -> V & { return self.ChangeFromKey(k); }, nb::arg("theKey"), D::ChangeFromKey);
    if constexpr (std::is_class_v<V>) {
        c.def("Seek", [](const M &self, const K &k) -> const V * { return self.Seek(k); }, nb::rv_policy::reference_internal, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> V * { return self.ChangeSeek(k); }, nb::rv_policy::reference_internal, nb::arg("theKey"), D::ChangeSeek)
         .def("FindFromKey", [](const M &self, const K &k, V &v) { return self.FindFromKey(k, v); }, nb::arg("theKey"), nb::arg("theValue"), D::FindFromKey);
    } else {
        c.def("Seek", [](const M &self, const K &k) -> std::optional<V> { const V *p = self.Seek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> std::optional<V> { V *p = self.ChangeSeek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::ChangeSeek);
    }
}

} // namespace nanoocp
