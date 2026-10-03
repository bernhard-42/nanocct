// Hand-written binders for the OCCT NCollection container templates (Binding-Rules.md, section 7a).
// One binder per template kind; the generator instantiates it for every typedef (TColgp_Array1OfPnt =
// NCollection_Array1<gp_Pnt>, ...) and for every instantiation that appears in a bound signature.
// Method names, signatures and docstrings are 1:1 with the template header; the docstrings live in
// the generated ncollection_docs.h. Python protocol methods (__len__, __iter__, __setitem__) are
// additions, never replacements.
#pragma once
#include "nanocct_common.h"
#include "nanocct_elem_view.h"
#include "ncollection_docs.h"

#include <nanobind/make_iterator.h>

#include <NCollection_Array1.hxx>
#include <NCollection_Array2.hxx>
#include <NCollection_DataMap.hxx>
#include <NCollection_DoubleMap.hxx>
#include <NCollection_DynamicArray.hxx>
#include <NCollection_LinearVector.hxx>
#include <NCollection_HArray2.hxx>
#include <NCollection_Shared.hxx>
#include <NCollection_DefaultHasher.hxx>
#include <NCollection_HArray1.hxx>
#include <NCollection_HSequence.hxx>
#include <NCollection_IndexedDataMap.hxx>
#include <NCollection_IndexedMap.hxx>
#include <NCollection_List.hxx>
#include <NCollection_Map.hxx>
#include <NCollection_Sequence.hxx>

#define NANOCCT_DOC(tmpl, member) nanocct_doc::tmpl::member

namespace nanocct {

// T has operator== (needed by NCollection_List::Contains / Remove(item); gp_Pnt has none, TopoDS_Shape has)
template <typename T, typename = void> struct has_equal : std::false_type {};
template <typename T>
struct has_equal<T, std::void_t<decltype(std::declval<const T &>() == std::declval<const T &>())>> : std::true_type {};

// R-VIEW-GUARD (nanocct_guards.h, Binding-Rules.md): what a member hands out that points into the container. A view of self
// (an element reference, LinearVector::ToArray1's aliasing array), an iterator over self (__iter__), an iterator
// constructed or initialised on its argument, an element reference handed out by such an iterator.
using elem_view_of_self = nb::call_policy<view_of<view_kind::element>>;
using iterator_of_self = nb::call_policy<view_of<view_kind::iterator>>;
using iterator_of_arg = nb::call_policy<view_of<view_kind::iterator, 1, 2>>;
using elem_view_of_iterator = nb::call_policy<view_through_iterator>;
// the Python object of an iterator argument, for a call that goes through it (List::Remove(it) moves it on and keeps it
// valid): that iterator does not count against the call
template <typename It> nb::object iterator_object(const It &it) { return nb::find(it); }

// def() a member returning an element reference: a view (reference_internal, counted as a view of the container: Policy)
// for class element types, a value for scalars and handles (nanobind policies are compile-time tags, hence if constexpr)
template <typename T, typename Policy = elem_view_of_self, typename C, typename F, typename... Args>
void def_elem(C &&c, const char *name, F &&f, Args &&...args) {
    if constexpr (std::is_class_v<T>)
        c.def(name, std::forward<F>(f), nb::rv_policy::reference_internal, Policy(), std::forward<Args>(args)...);
    else
        c.def(name, std::forward<F>(f), std::forward<Args>(args)...);
}

// numpy's __array__ for a container's contiguous storage (R-VIEW): `copy=True` an independent copy, otherwise a view whose
// owner keeps the container alive and counts as one of its views (R-VIEW-GUARD)
template <typename T, size_t NDim, typename Cls>
auto container_array(void *first, const size_t (&shape)[NDim], Cls &self, std::optional<bool> copy) {
    if (copy.has_value() && copy.value() == true)
        return elem_view<T>(first, shape).cast(nb::rv_policy::copy);
    return elem_view<T>(first, shape, export_view(&self, nb::find(&self))).cast(nb::rv_policy::reference);
}

// R-OWNER (Binding-Rules.md): elements whose OCAF owners are known (a TDF_Label, a handle of a TDF_Attribute -- nanocct::owners).
// A container keeps the owners of every element Python puts into it (own, own_all), an element copied out keeps its own
// (owned), and an argument a lookup writes into keeps those of what it received (own_out) -- whoever filled the container.
// For every other element type these compile to nothing.
template <typename C> PyObject *self_object(const C &self) {
    static_assert(!nanocct_is_handle<C>::value, "nb::find of a handle builds a new object");
    nb::object py = nb::find(self);
    if (!py.is_valid())
        throw std::runtime_error("nanocct R-OWNER: the container has no Python object");
    return py.ptr();                     // borrowed: Python holds the object for the duration of the call
}
template <typename C, typename T> void own(const C &self, const T &value) {
    if constexpr (owners<T>::active)
        owners<T>::keep(self_object(self), value);
}
template <typename C, typename O> void own_all(const C &self, const O &other) {
    if constexpr (owners<O>::active)
        owners<O>::keep(self_object(self), other);
}
// not for a handle: nanobind passes a handle argument as a C++ copy, so the call cannot write into the Python object -- and
// nb::find would build a new wrapper for it, whose PyObject* dies with the temporary
template <typename T> void own_out(const T &value) {
    if constexpr (owners<T>::active && !nanocct_is_handle<T>::value)
        owners<T>::keep(self_object(value), value);
}
template <typename T> decltype(auto) owned(const T &value) {
    if constexpr (owners<T>::active) {
        nb::object element = nb::cast(value, nb::rv_policy::copy);
        owners<T>::keep(element.ptr(), value);
        return nb::typed<nb::object, T>(std::move(element));
    } else {
        return (value);                  // const T &: nanobind copies it, as before
    }
}
template <typename T> decltype(auto) owned_ptr(const T *value) {
    if constexpr (owners<T>::active) {
        if (value == nullptr)
            return nb::typed<nb::object, std::optional<T>>(nb::none());
        nb::object element = nb::cast(*value, nb::rv_policy::copy);
        owners<T>::keep(element.ptr(), *value);
        return nb::typed<nb::object, std::optional<T>>(std::move(element));
    } else {
        return value;                    // rv_policy::copy at the def
    }
}
// a copy of a container keeps its source when the elements have owners; otherwise no annotation (an empty call guard)
template <typename T, size_t Nurse, size_t Patient>
using keep_if_owned = std::conditional_t<owners<T>::active, nb::keep_alive<Nurse, Patient>, nb::call_guard<>>;
// a binder that does not apply the rule must not be instantiated for such elements
template <typename T> constexpr bool owners_not_supported = !owners<T>::active;

// Array1 members shared by NCollection_Array1<T> and NCollection_HArray1<T>. Cls is the bound class,
// A the NCollection_Array1<T> it is (or derives from).
template <typename T, typename Cls, typename... Extra> void def_array1_members(nb::class_<Cls, Extra...> &c) {
    using A = NCollection_Array1<T>;
    namespace D = nanocct_doc::NCollection_Array1;
    c.def("Init", [](Cls &self, const T &v) { own(self, v); self.Init(v); }, nb::arg("theValue"), D::Init)
     .def("Size", [](const Cls &self) { return self.Size(); }, D::Size)
     .def("Length", [](const Cls &self) { return self.Length(); }, D::Length)
     .def("IsEmpty", [](const Cls &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Lower", [](const Cls &self) { return self.Lower(); }, D::Lower)
     .def("Upper", [](const Cls &self) { return self.Upper(); }, D::Upper)
     .def("IsDeletable", [](const Cls &self) { return self.IsDeletable(); }, D::IsDeletable)
     // R-VIEW-GUARD: a different size reallocates (NCollection_Array1.hxx, assign: same size copies in place)
     .def("Assign", [](Cls &self, const A &other) -> Cls & {
              if (other.Size() != self.Size()) refuse_if_viewed(&self, "Assign");
              own_all(self, other); self.Assign(other); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("CopyValues", [](Cls &self, const A &other) -> Cls & { own_all(self, other); self.CopyValues(other); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::CopyValues)
     .def("First", [](const Cls &self) -> decltype(auto) { return owned(self.First()); }, D::First)
     .def("Last", [](const Cls &self) -> decltype(auto) { return owned(self.Last()); }, D::Last)
     .def("Value", [](const Cls &self, const int i) -> decltype(auto) { return owned(self.Value(i)); }, nb::arg("theIndex"), D::Value)
     .def("At", [](const Cls &self, const size_t i) -> decltype(auto) { return owned(self.At(i)); }, nb::arg("theIndex"), D::At)
     .def("SetValue", [](Cls &self, const int i, const T &v) { own(self, v); self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::SetValue)
     .def("UpdateLowerBound", [](Cls &self, const int l) { self.UpdateLowerBound(l); }, nb::arg("theLower"), D::UpdateLowerBound)
     .def("UpdateUpperBound", [](Cls &self, const int u) { self.UpdateUpperBound(u); }, nb::arg("theUpper"), D::UpdateUpperBound)
     // R-VIEW-GUARD: "No re-allocation will be done if length of array does not change" (NCollection_Array1.hxx, Resize)
     .def("Resize", [](Cls &self, const int l, const int u, const bool copy) {
              if (u >= l && (size_t) ((long long) u - l + 1) != self.Size()) refuse_if_viewed(&self, "Resize");
              self.Resize(l, u, copy); }, nb::arg("theLower"), nb::arg("theUpper"), nb::arg("theToCopyData"), D::Resize)
     .def("Resize", [](Cls &self, const size_t n, const bool copy) {
              if (n != self.Size()) refuse_if_viewed(&self, "Resize");
              self.Resize(n, copy); }, nb::arg("theSize"), nb::arg("theToCopyData"), D::Resize)
     // operator() and operator[] are OCCT's own aliases of Value (OCCT index, not 0-based)
     .def("__call__", [](const Cls &self, const int i) -> decltype(auto) { return owned(self.Value(i)); }, nb::arg("theIndex"), D::op_call)
     .def("__getitem__", [](const Cls &self, const int i) -> decltype(auto) { return owned(self.Value(i)); }, nb::arg("theIndex"), D::op_index)
     // Python additions
     .def("__setitem__", [](Cls &self, const int i, const T &v) { own(self, v); self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), "Python addition: alias to SetValue (OCCT index).")
     .def("__len__", [](const Cls &self) { return self.Length(); }, "Python addition: alias to Length.")
     .def("__iter__", [](const Cls &self) { return nb::make_iterator(nb::type<Cls>(), "iterator", self.begin(), self.end()); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the values from Lower() to Upper().");
    // R-VIEW: a packed POD element type also gets numpy's array protocol, a zero-copy
    // view of the whole array, so the per-element __getitem__ loop above never has to be the way large data
    // reaches Python. Not every instantiation qualifies -- a handle, a string, a TopoDS_Shape has nothing to view.
    if constexpr (nanocct::view_elem<T>::supported)
        c.def("__array__", [](Cls &self, nb::handle, std::optional<bool> copy) {
            const size_t n = (size_t) self.Size();
            const size_t shape[1] = { n };
            return container_array<T>(n == 0 ? nullptr : (void *) &self.ChangeFirst(), shape, self, copy);
        }, nb::arg("dtype") = nb::none(), nb::arg("copy") = nb::none(),
        "Python addition: numpy's array protocol -- `numpy.asarray(a)` is a zero-copy view of the whole array "
        "(R-VIEW), `numpy.array(a)` a copy.\n\n"
        "Shape (Size(),) for a scalar element type and (Size(), k) for a k-component one -- (N, 3) for "
        "gp_Pnt, (N, 2) for gp_Pnt2d, (N, 3) int32 for Poly_Triangle. Index 0 of the view is Lower(), "
        "whatever Lower() is; the view has no notion of OCCT's index base. An empty array gives a "
        "zero-length view.\n\n"
        "Writes go straight into the array, except for gp_Dir and gp_Dir2d, whose view is read-only "
        "because a raw write could store a direction that is not of unit length -- use SetValue() there.\n\n"
        "The view keeps this object alive, but an array built over a caller's buffer (IsDeletable() is "
        "false) points into memory this object does not own and cannot keep alive either. While the view lives, "
        "a call that would reallocate the array (a Resize or Assign to another size) raises BufferError, as "
        "bytearray does.");
    if constexpr (std::is_class_v<T>) {
        // mutable references only make sense for class element types (a double& cannot be exposed)
        c.def("ChangeFirst", [](Cls &self) -> T & { return self.ChangeFirst(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeFirst)
         .def("ChangeLast", [](Cls &self) -> T & { return self.ChangeLast(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeLast)
         .def("ChangeValue", [](Cls &self, const int i) -> T & { return self.ChangeValue(i); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theIndex"), D::ChangeValue)
         .def("ChangeAt", [](Cls &self, const size_t i) -> T & { return self.ChangeAt(i); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theIndex"), D::ChangeAt);
    }
}

// Standard_Transient members of a multiple-inheritance type S bound with base B (offset 0): the lambdas
// take B& and static_cast to S& (adjusting downcast), see mi_traits in nanocct_registry.h
template <typename S, typename B, typename... Extra> void def_transient_members(nb::class_<S, B, Extra...> &c) {
    c.def("GetRefCount", [](const B &b) { return static_cast<const S &>(b).GetRefCount(); }, "Get the reference counter of this object (Standard_Transient).")
     .def("DynamicType", [](const B &b) { return static_cast<const S &>(b).DynamicType(); }, "Returns a type descriptor about this object (Standard_Transient).")
     .def("IsInstance", [](const B &b, const char *n) { return static_cast<const S &>(b).IsInstance(n); }, nb::arg("theTypeName"), "Standard_Transient::IsInstance")
     .def("IsKind", [](const B &b, const char *n) { return static_cast<const S &>(b).IsKind(n); }, nb::arg("theTypeName"), "Standard_Transient::IsKind")
     // R-STATIC-S: statics carry _s here too, as in the generated bindings
     .def_static("get_type_name_s", []() { return S::get_type_name(); })
     .def_static("get_type_descriptor_s", []() { return S::get_type_descriptor(); });
    nanocct_register_mi<S>(c);
}

template <typename T> void bind_NCollection_Array1(nb::module_ &m, const char *name) {
    using A = NCollection_Array1<T>;
    namespace D = nanocct_doc::NCollection_Array1;
    nb::class_<A> c(m, name, D::class_doc);
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const int, const int>(), nb::arg("theLower"), nb::arg("theUpper"), D::ctor)
     .def(nb::init<const size_t>(), nb::arg("theSize"), D::ctor)
     .def(nb::init<const A &>(), nb::arg("theOther"), keep_if_owned<T, 1, 2>(), D::ctor);
    def_array1_members<T, A>(c);
}

template <typename T> void bind_NCollection_HArray1(nb::module_ &m, const char *name) {
    using A = NCollection_Array1<T>;
    using H = NCollection_HArray1<T>;
    namespace D = nanocct_doc::NCollection_HArray1;
    // base = Array1<T> (offset 0): the whole Array1 API is inherited with an exact pointer; the
    // Standard_Transient part (non-zero offset) goes through def_transient_members / the MI registry
    nb::class_<H, A> c(m, name, D::class_doc);
    c.def(nb::new_([]() { return opencascade::handle<H>(new H()); }), D::ctor)
     .def(nb::new_([](const int l, const int u) { return opencascade::handle<H>(new H(l, u)); }), nb::arg("theLower"), nb::arg("theUpper"), D::ctor)
     .def(nb::new_([](const int l, const int u, const T &v) { return opencascade::handle<H>(new H(l, u, v)); }), nb::arg("theLower"), nb::arg("theUpper"), nb::arg("theValue"), keep_if_owned<T, 0, 4>(), D::ctor)
     .def(nb::new_([](const A &a) { return opencascade::handle<H>(new H(a)); }), nb::arg("theOther"), keep_if_owned<T, 0, 2>(), D::ctor)
     .def("Array1", [](const A &b) { return owned(A(static_cast<const H &>(b).Array1())); }, D::Array1)      // sliced copy (Array1 is polymorphic)
     .def("ChangeArray1", [](A &b) -> A & { return static_cast<H &>(b).ChangeArray1(); }, nb::rv_policy::reference_internal, D::ChangeArray1);
    def_transient_members<H, A>(c);
}

// ---------------------------------------------------------------------------------------------------
// NCollection_List<T>
template <typename T> void bind_NCollection_List(nb::module_ &m, const char *name) {
    using L = NCollection_List<T>;
    using It = typename L::Iterator;
    namespace D = nanocct_doc::NCollection_List;
    nb::class_<L> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const L &>(), nb::arg("theList"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
        .def("Initialize", [](It &self, const L &l) { self.Initialize(l); }, nb::arg("theList"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::Initialize)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value);
    def_elem<T, elem_view_of_iterator>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), "ChangeValue", [](It &self) -> T & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    // R-VIEW-GUARD: removing or clearing frees nodes; Append/Prepend/Insert*(theOther) move theOther's nodes into this list
    // (NCollection_BaseList.cxx, PAppend(list&) ...), Exchange both ways; inserting an item never moves a node
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theAllocator").none(), D::ctor)
     .def(nb::init<const L &>(), nb::arg("theOther"), keep_if_owned<T, 1, 2>(), D::ctor)
     .def("Extent", [](const L &self) { return self.Extent(); }, D::Extent)
     .def("Length", [](const L &self) { return self.Length(); }, D::Length)
     .def("Size", [](const L &self) { return self.Size(); }, D::Size)
     .def("IsEmpty", [](const L &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Allocator", [](const L &self) { return self.Allocator(); }, D::Allocator)
     .def("Assign", [](L &self, const L &o) -> L & { refuse_if_viewed(&self, "Assign"); own_all(self, o); return self.Assign(o); }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("Clear", [](L &self, const opencascade::handle<NCollection_BaseAllocator> &a) { refuse_if_viewed(&self, "Clear"); self.Clear(a); },
          nb::arg("theAllocator").none() = static_cast<opencascade::handle<NCollection_BaseAllocator>>(nullptr), D::Clear)
     .def("First", [](const L &self) -> decltype(auto) { return owned(self.First()); }, D::First)
     .def("Last", [](const L &self) -> decltype(auto) { return owned(self.Last()); }, D::Last)
     .def("Append", [](L &self, const T &v, It &it) { own(self, v); self.Append(v, it); }, nb::arg("theItem"), nb::arg("theIter"), D::Append)
     .def("Append", [](L &self, L &other) { refuse_if_viewed(&other, "Append"); own_all(self, other); self.Append(other); }, nb::arg("theOther"), D::Append)
     .def("Prepend", [](L &self, L &other) { refuse_if_viewed(&other, "Prepend"); own_all(self, other); self.Prepend(other); }, nb::arg("theOther"), D::Prepend)
     .def("RemoveFirst", [](L &self) { refuse_if_viewed(&self, "RemoveFirst"); self.RemoveFirst(); }, D::RemoveFirst)
     .def("Remove", [](L &self, It &it) { refuse_if_viewed(&self, "Remove", iterator_object(it).ptr()); self.Remove(it); }, nb::arg("theIter"), D::Remove)
     .def("InsertBefore", [](L &self, L &other, It &it) { refuse_if_viewed(&other, "InsertBefore"); own_all(self, other); self.InsertBefore(other, it); }, nb::arg("theOther"), nb::arg("theIter"), D::InsertBefore)
     .def("InsertAfter", [](L &self, L &other, It &it) { refuse_if_viewed(&other, "InsertAfter"); own_all(self, other); self.InsertAfter(other, it); }, nb::arg("theOther"), nb::arg("theIter"), D::InsertAfter)
     .def("Reverse", [](L &self) { self.Reverse(); }, D::Reverse)
     .def("Exchange", [](L &self, L &other) {
              refuse_if_viewed(&self, "Exchange"); refuse_if_viewed(&other, "Exchange");
              own_all(self, other); own_all(other, self); self.Exchange(other); }, nb::arg("theOther"), D::Exchange)
     // Python additions
     .def("__len__", [](const L &self) { return self.Extent(); }, "Python addition: alias to Extent.")
     .def("__iter__", [](const L &self) { return nb::make_iterator(nb::type<L>(), "value_iterator", self.begin(), self.end()); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the values.");
    // members returning the (inserted) element reference: view for class types, value otherwise
    def_elem<T>(c, "Append", [](L &self, const T &v) -> T & { own(self, v); return self.Append(v); }, nb::arg("theItem"), D::Append);
    def_elem<T>(c, "Prepend", [](L &self, const T &v) -> T & { own(self, v); return self.Prepend(v); }, nb::arg("theItem"), D::Prepend);
    def_elem<T>(c, "InsertBefore", [](L &self, const T &v, It &it) -> T & { own(self, v); return self.InsertBefore(v, it); }, nb::arg("theItem"), nb::arg("theIter"), D::InsertBefore);
    def_elem<T>(c, "InsertAfter", [](L &self, const T &v, It &it) -> T & { own(self, v); return self.InsertAfter(v, it); }, nb::arg("theItem"), nb::arg("theIter"), D::InsertAfter);
    if constexpr (has_equal<T>::value) {
        c.def("Contains", [](const L &self, const T &v) { return self.Contains(v); }, nb::arg("theObject"), D::Contains)
         .def("Remove", [](L &self, const T &v) { refuse_if_viewed(&self, "Remove"); return self.Remove(v); }, nb::arg("theObject"), D::Remove)
         .def("__contains__", [](const L &self, const T &v) { return self.Contains(v); }, nb::arg("theObject"), "Python addition: alias to Contains.");
    }
}

// ---------------------------------------------------------------------------------------------------
// NCollection_Sequence<T> (shared with NCollection_HSequence<T>)
template <typename T, typename Cls, typename... Extra> void def_sequence_members(nb::class_<Cls, Extra...> &c) {
    using S = NCollection_Sequence<T>;
    using It = typename S::Iterator;
    namespace D = nanocct_doc::NCollection_Sequence;
    // size_t overloads duplicate the int ones (Python cannot tell them apart): int only; At/ChangeAt are size_t-only
    c.def("Length", [](const Cls &self) { return self.Length(); }, D::Length)
     .def("Size", [](const Cls &self) { return self.Size(); }, D::Size)
     .def("IsEmpty", [](const Cls &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Lower", [](const Cls &self) { return self.Lower(); }, D::Lower)
     .def("Upper", [](const Cls &self) { return self.Upper(); }, D::Upper)
     .def("Allocator", [](const Cls &self) { return self.Allocator(); }, D::Allocator)
     .def("Reverse", [](Cls &self) { self.Reverse(); }, D::Reverse)
     .def("Exchange", [](Cls &self, const int i, const int j) { self.Exchange(i, j); }, nb::arg("I"), nb::arg("J"), D::Exchange)
     // R-VIEW-GUARD: removing, clearing and assigning free nodes; Append/Prepend/Insert*(theSeq) move theSeq's nodes into
     // this sequence, Split moves this tail into theSeq and clears theSeq first (NCollection_BaseSequence.cxx); inserting an
     // item, Exchange(I, J) and Reverse only relink
     .def("Clear", [](Cls &self, const opencascade::handle<NCollection_BaseAllocator> &a) { refuse_if_viewed(&self, "Clear"); self.Clear(a); },
          nb::arg("theAllocator").none() = static_cast<opencascade::handle<NCollection_BaseAllocator>>(nullptr), D::Clear)
     .def("Assign", [](Cls &self, const S &o) -> Cls & { refuse_if_viewed(&self, "Assign"); own_all(self, o); self.Assign(o); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("Remove", [](Cls &self, It &it) { refuse_if_viewed(&self, "Remove", iterator_object(it).ptr()); self.Remove(it); }, nb::arg("thePosition"), D::Remove)
     .def("Remove", [](Cls &self, const int i) { refuse_if_viewed(&self, "Remove"); self.Remove(i); }, nb::arg("theIndex"), D::Remove)
     .def("Remove", [](Cls &self, const int from, const int to) { refuse_if_viewed(&self, "Remove"); self.Remove(from, to); }, nb::arg("theFromIndex"), nb::arg("theToIndex"), D::Remove)
     .def("Append", [](Cls &self, const T &v) { own(self, v); self.Append(v); }, nb::arg("theItem"), D::Append)
     .def("Append", [](Cls &self, S &other) { refuse_if_viewed(&other, "Append"); own_all(self, other); self.Append(other); }, nb::arg("theSeq"), D::Append)
     .def("Prepend", [](Cls &self, const T &v) { own(self, v); self.Prepend(v); }, nb::arg("theItem"), D::Prepend)
     .def("Prepend", [](Cls &self, S &other) { refuse_if_viewed(&other, "Prepend"); own_all(self, other); self.Prepend(other); }, nb::arg("theSeq"), D::Prepend)
     .def("InsertBefore", [](Cls &self, const int i, const T &v) { own(self, v); self.InsertBefore(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::InsertBefore)
     .def("InsertBefore", [](Cls &self, const int i, S &other) { refuse_if_viewed(&other, "InsertBefore"); own_all(self, other); self.InsertBefore(i, other); }, nb::arg("theIndex"), nb::arg("theSeq"), D::InsertBefore)
     .def("InsertAfter", [](Cls &self, It &it, const T &v) { own(self, v); self.InsertAfter(it, v); }, nb::arg("thePosition"), nb::arg("theItem"), D::InsertAfter)
     .def("InsertAfter", [](Cls &self, const int i, S &other) { refuse_if_viewed(&other, "InsertAfter"); own_all(self, other); self.InsertAfter(i, other); }, nb::arg("theIndex"), nb::arg("theSeq"), D::InsertAfter)
     .def("InsertAfter", [](Cls &self, const int i, const T &v) { own(self, v); self.InsertAfter(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::InsertAfter)
     .def("Split", [](Cls &self, const int i, S &sub) {
              refuse_if_viewed(&self, "Split"); refuse_if_viewed(&sub, "Split");
              own_all(sub, self); self.Split(i, sub); }, nb::arg("theIndex"), nb::arg("theSeq"), D::Split)
     .def("First", [](const Cls &self) -> decltype(auto) { return owned(self.First()); }, D::First)
     .def("Last", [](const Cls &self) -> decltype(auto) { return owned(self.Last()); }, D::Last)
     .def("Value", [](const Cls &self, const int i) -> decltype(auto) { return owned(self.Value(i)); }, nb::arg("theIndex"), D::Value)
     .def("At", [](const Cls &self, const size_t i) -> decltype(auto) { return owned(self.At(i)); }, nb::arg("theIndex"), D::At)
     .def("SetValue", [](Cls &self, const int i, const T &v) { own(self, v); self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), D::SetValue)
     .def("__call__", [](const Cls &self, const int i) -> decltype(auto) { return owned(self.Value(i)); }, nb::arg("theIndex"), D::op_call)
     // Python additions
     .def("__getitem__", [](const Cls &self, const int i) -> decltype(auto) { return owned(self.Value(i)); }, nb::arg("theIndex"), "Python addition: alias to Value (OCCT index, 1-based).")
     .def("__setitem__", [](Cls &self, const int i, const T &v) { own(self, v); self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), "Python addition: alias to SetValue (OCCT index).")
     .def("__len__", [](const Cls &self) { return self.Length(); }, "Python addition: alias to Length.")
     .def("__iter__", [](const Cls &self) { return nb::make_iterator(nb::type<Cls>(), "value_iterator", self.cbegin(), self.cend()); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the values.");
    if constexpr (std::is_class_v<T>) {
        c.def("ChangeFirst", [](Cls &self) -> T & { return self.ChangeFirst(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeFirst)
         .def("ChangeLast", [](Cls &self) -> T & { return self.ChangeLast(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeLast)
         .def("ChangeValue", [](Cls &self, const int i) -> T & { return self.ChangeValue(i); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theIndex"), D::ChangeValue)
         .def("ChangeAt", [](Cls &self, const size_t i) -> T & { return self.ChangeAt(i); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theIndex"), D::ChangeAt);
    }
}

template <typename T> void bind_NCollection_Sequence(nb::module_ &m, const char *name) {
    using S = NCollection_Sequence<T>;
    using It = typename S::Iterator;
    namespace D = nanocct_doc::NCollection_Sequence;
    nb::class_<S> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const S &, const bool>(), nb::arg("theSeq"), nb::arg("isStart") = true, nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value);
    def_elem<T, elem_view_of_iterator>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), "ChangeValue", [](It &self) -> T & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theAllocator").none(), D::ctor)
     .def(nb::init<const S &>(), nb::arg("theOther"), keep_if_owned<T, 1, 2>(), D::ctor);
    def_sequence_members<T, S>(c);
}

template <typename T> void bind_NCollection_HSequence(nb::module_ &m, const char *name) {
    using S = NCollection_Sequence<T>;
    using H = NCollection_HSequence<T>;
    namespace D = nanocct_doc::NCollection_HSequence;
    nb::class_<H, S> c(m, name, D::class_doc);       // base = Sequence<T> (offset 0), see HArray1
    c.def(nb::new_([]() { return opencascade::handle<H>(new H()); }), D::ctor)
     .def(nb::new_([](const S &s) { return opencascade::handle<H>(new H(s)); }), nb::arg("theOther"), keep_if_owned<T, 0, 2>(), D::ctor)
     .def("Sequence", [](const S &b) { return owned(S(static_cast<const H &>(b).Sequence())); }, D::Sequence)
     .def("ChangeSequence", [](S &b) -> S & { return static_cast<H &>(b).ChangeSequence(); }, nb::rv_policy::reference_internal, D::ChangeSequence);
    def_transient_members<H, S>(c);
}

// ---------------------------------------------------------------------------------------------------
// hashed containers: members of NCollection_BaseMap plus constructors shared by all four kinds
inline const opencascade::handle<NCollection_BaseAllocator> null_allocator = nullptr;

struct BaseMapDocs {
    const char *ctor, *NbBuckets, *Extent, *Length, *Size, *IsEmpty, *Allocator, *Exchange, *Assign, *ReSize, *Clear;
};
#define NANOCCT_BASEMAP_DOCS(D) \
    nanocct::BaseMapDocs{D::ctor, D::NbBuckets, D::Extent, D::Length, D::Size, D::IsEmpty, D::Allocator, D::Exchange, D::Assign, D::ReSize, D::Clear}

// R-VIEW-GUARD: Clear, Assign and Exchange free or move every node (NCollection_BaseMap.cxx, Destroy;
// NCollection_BaseMap.hxx, exchangeMapsData). ReSize relinks the nodes into a new bucket array and frees the old one: an
// element reference stays valid, an iterator of Map, DataMap or DoubleMap does not (it caches the bucket array,
// NCollection_BaseMap.hxx, Iterator::PNext). Indexed: the iterators of IndexedMap and IndexedDataMap hold the map and an
// index (NCollection_IndexedMap.hxx, Iterator), so growing the table does not touch them.
template <bool Indexed, typename M, typename... Extra> void def_basemap_members(nb::class_<M, Extra...> &c, const BaseMapDocs &D) {
    c.def(nb::init<>(), D.ctor)
     .def(nb::init<const int, const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theNbBuckets"),
          nb::arg("theAllocator").none() = null_allocator, D.ctor)
     .def(nb::init<const M &>(), nb::arg("theOther"), keep_if_owned<M, 1, 2>(), D.ctor)
     .def("NbBuckets", [](const M &self) { return self.NbBuckets(); }, D.NbBuckets)
     .def("Extent", [](const M &self) { return self.Extent(); }, D.Extent)
     .def("Length", [](const M &self) { return self.Length(); }, D.Length)
     .def("Size", [](const M &self) { return self.Size(); }, D.Size)
     .def("IsEmpty", [](const M &self) { return self.IsEmpty(); }, D.IsEmpty)
     .def("Allocator", [](const M &self) { return self.Allocator(); }, D.Allocator)
     .def("Exchange", [](M &self, M &other) {
              refuse_if_viewed(&self, "Exchange"); refuse_if_viewed(&other, "Exchange");
              own_all(self, other); own_all(other, self); self.Exchange(other); }, nb::arg("theOther"), D.Exchange)
     .def("Assign", [](M &self, const M &other) -> M & { refuse_if_viewed(&self, "Assign"); own_all(self, other); return self.Assign(other); }, nb::rv_policy::reference, nb::arg("theOther"), D.Assign)
     .def("ReSize", [](M &self, const int n) { if constexpr (!Indexed) refuse_if_iterated(&self, "ReSize"); self.ReSize(n); }, nb::arg("N"), D.ReSize)
     .def("Clear", [](M &self, const bool release) { refuse_if_viewed(&self, "Clear"); self.Clear(release); }, nb::arg("doReleaseMemory") = true, D.Clear)
     .def("Clear", [](M &self, const opencascade::handle<NCollection_BaseAllocator> &a) { refuse_if_viewed(&self, "Clear"); self.Clear(a); }, nb::arg("theAllocator").none(), D.Clear)
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
    namespace D = nanocct_doc::NCollection_Map;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
        .def("Initialize", [](It &self, const M &map) { self.Initialize(map); }, nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::Initialize)
        .def("Reset", [](It &self) { self.Reset(); }, D::Iterator::Reset)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value)
        .def("Key", [](const It &self) -> decltype(auto) { return owned(self.Key()); }, D::Iterator::Key);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    def_basemap_members<false>(c, NANOCCT_BASEMAP_DOCS(D));
    // R-VIEW-GUARD: Add can grow the table (iterators); removal frees nodes. The set operations per NCollection_MapAlgo.hxx:
    // Union clears this map unless it is an operand, Unite only adds, the others remove or exchange into a local.
    c.def("Add", [](M &self, const K &k) { refuse_if_iterated(&self, "Add"); own(self, k); return self.Add(k); }, nb::arg("theKey"), D::Add)
     .def("Added", [](M &self, const K &k) -> decltype(auto) { refuse_if_iterated(&self, "Added"); own(self, k); return owned(self.Added(k)); }, nb::arg("theKey"), D::Added)
     .def("Contains", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), D::Contains)
     .def("Contains", [](const M &self, const M &other) { return self.Contains(other); }, nb::arg("theOther"), D::Contains_deprecated)
     .def("Remove", [](M &self, const K &k) { refuse_if_viewed(&self, "Remove"); return self.Remove(k); }, nb::arg("theKey"), D::Remove)
     .def("IsEqual", [](const M &self, const M &other) { return self.IsEqual(other); }, nb::arg("theOther"), D::IsEqual)
     .def("Union", [](M &self, const M &a, const M &b) {
              if (&self != &a && &self != &b) refuse_if_viewed(&self, "Union"); else refuse_if_iterated(&self, "Union");
              own_all(self, a); own_all(self, b); self.Union(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Union)
     .def("Unite", [](M &self, const M &other) { refuse_if_iterated(&self, "Unite"); own_all(self, other); return self.Unite(other); }, nb::arg("theOther"), D::Unite)
     .def("HasIntersection", [](const M &self, const M &other) { return self.HasIntersection(other); }, nb::arg("theMap"), D::HasIntersection)
     .def("Intersection", [](M &self, const M &a, const M &b) { refuse_if_viewed(&self, "Intersection"); own_all(self, a); own_all(self, b); self.Intersection(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Intersection)
     .def("Intersect", [](M &self, const M &other) { refuse_if_viewed(&self, "Intersect"); return self.Intersect(other); }, nb::arg("theOther"), D::Intersect)
     .def("Subtraction", [](M &self, const M &a, const M &b) { refuse_if_viewed(&self, "Subtraction"); own_all(self, a); self.Subtraction(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Subtraction)
     .def("Subtract", [](M &self, const M &other) { refuse_if_viewed(&self, "Subtract"); return self.Subtract(other); }, nb::arg("theOther"), D::Subtract)
     .def("Difference", [](M &self, const M &a, const M &b) { refuse_if_viewed(&self, "Difference"); own_all(self, a); own_all(self, b); self.Difference(a, b); }, nb::arg("theLeft"), nb::arg("theRight"), D::Difference)
     .def("Differ", [](M &self, const M &other) { refuse_if_viewed(&self, "Differ"); own_all(self, other); return self.Differ(other); }, nb::arg("theOther"), D::Differ)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), "Python addition: alias to Contains.")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Key(); }); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the keys.");
}

// ---- NCollection_DataMap<K, V, Hasher>
template <typename K, typename V, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_DataMap(nb::module_ &m, const char *name) {
    using M = NCollection_DataMap<K, V, H>;
    using It = typename M::Iterator;
    namespace D = nanocct_doc::NCollection_DataMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It> it(c, "Iterator", D::Iterator::class_doc);
    it.def(nb::init<>(), D::Iterator::ctor)
      .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
      .def("Initialize", [](It &self, const M &map) { self.Initialize(map); }, nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::Initialize)
      .def("Reset", [](It &self) { self.Reset(); }, D::Iterator::Reset)
      .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
      .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
      .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value)
      .def("Key", [](const It &self) -> decltype(auto) { return owned(self.Key()); }, D::Iterator::Key);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    def_elem<V, elem_view_of_iterator>(it, "ChangeValue", [](It &self) -> V & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    def_basemap_members<false>(c, NANOCCT_BASEMAP_DOCS(D));
    // R-VIEW-GUARD: binding can grow the table (iterators; a bound key's value is assigned in place), UnBind frees a node
    c.def("Bind", [](M &self, const K &k, const V &v) { refuse_if_iterated(&self, "Bind"); own(self, k); own(self, v); return self.Bind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bind)
     .def("TryBind", [](M &self, const K &k, const V &v) { refuse_if_iterated(&self, "TryBind"); own(self, k); own(self, v); return self.TryBind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBind)
     .def("IsBound", [](const M &self, const K &k) { return self.IsBound(k); }, nb::arg("theKey"), D::IsBound)
     .def("UnBind", [](M &self, const K &k) { refuse_if_viewed(&self, "UnBind"); return self.UnBind(k); }, nb::arg("theKey"), D::UnBind)
     .def("Find", [](const M &self, const K &k) -> decltype(auto) { return owned(self.Find(k)); }, nb::arg("theKey"), D::Find)
     .def("__call__", [](const M &self, const K &k) -> decltype(auto) { return owned(self.Find(k)); }, nb::arg("theKey"), D::op_call)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.IsBound(k); }, nb::arg("theKey"), "Python addition: alias to IsBound.")
     .def("__getitem__", [](const M &self, const K &k) -> decltype(auto) { return owned(self.Find(k)); }, nb::arg("theKey"), "Python addition: alias to Find.")
     .def("__setitem__", [](M &self, const K &k, const V &v) { refuse_if_iterated(&self, "__setitem__"); own(self, k); own(self, v); self.Bind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), "Python addition: alias to Bind.")
     .def("__delitem__", [](M &self, const K &k) { refuse_if_viewed(&self, "__delitem__"); if (!self.UnBind(k)) throw nb::key_error(); }, nb::arg("theKey"), "Python addition: UnBind, KeyError if the key is not bound.")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Key(); }); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the keys.")
     .def("items", [](const M &self) {
              nb::list out;
              for (It it(self); it.More(); it.Next()) out.append(nb::make_tuple(owned(it.Key()), owned(it.Value())));
              return out; }, "Python addition: list of (key, value) tuples.");
    // element references: view for class V, value for scalars/handles
    def_elem<V>(c, "Bound", [](M &self, const K &k, const V &v) -> V & { refuse_if_iterated(&self, "Bound"); own(self, k); own(self, v); return *self.Bound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bound);
    def_elem<V>(c, "TryBound", [](M &self, const K &k, const V &v) -> V & { refuse_if_iterated(&self, "TryBound"); own(self, k); own(self, v); return self.TryBound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBound);
    def_elem<V>(c, "ChangeFind", [](M &self, const K &k) -> V & { return self.ChangeFind(k); }, nb::arg("theKey"), D::ChangeFind);
    // Seek: nullptr when absent -> None. The const Seek is a copy, as Find() is (a const pointer is no view: nanobind has no
    // const, so reference_internal handed out a writable alias -- on DoubleMap's Seek1/Seek2 a *key*, whose change left it
    // unfindable by either spelling; final review 2026-09-30); ChangeSeek is the view
    if constexpr (std::is_class_v<V>) {
        c.def("Seek", [](const M &self, const K &k) -> decltype(auto) { return owned_ptr(self.Seek(k)); }, nb::rv_policy::copy, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> V * { return self.ChangeSeek(k); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theKey"), D::ChangeSeek)
         .def("Find", [](const M &self, const K &k, V &v) { const bool found = self.Find(k, v); own_out(v); return found; }, nb::arg("theKey"), nb::arg("theValue"), D::Find);
    } else {
        c.def("Seek", [](const M &self, const K &k) -> std::optional<V> { const V *p = self.Seek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> std::optional<V> { V *p = self.ChangeSeek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::ChangeSeek);
    }
}

// ---- NCollection_IndexedMap<K, Hasher>
template <typename K, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_IndexedMap(nb::module_ &m, const char *name) {
    using M = NCollection_IndexedMap<K, H>;
    using It = typename M::Iterator;
    namespace D = nanocct_doc::NCollection_IndexedMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value)
        .def("Index", [](const It &self) { return self.Index(); }, D::Iterator::Index)
        .def("IsEqual", [](const It &self, const It &o) { return self.IsEqual(o); }, nb::arg("theOther"), D::Iterator::IsEqual);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    def_basemap_members<true>(c, NANOCCT_BASEMAP_DOCS(D));
    // R-VIEW-GUARD: adding, Substitute and Swap keep every node (NCollection_IndexedMap.hxx); removal frees one
    c.def("Add", [](M &self, const K &k) { own(self, k); return self.Add(k); }, nb::arg("theKey"), D::Add)
     .def("Added", [](M &self, const K &k) -> decltype(auto) { own(self, k); return owned(self.Added(k)); }, nb::arg("theKey"), D::Added)
     .def("Contains", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), D::Contains)
     .def("Substitute", [](M &self, const int i, const K &k) { own(self, k); self.Substitute(i, k); }, nb::arg("theIndex"), nb::arg("theKey"), D::Substitute)
     .def("Swap", [](M &self, const int i, const int j) { self.Swap(i, j); }, nb::arg("theIndex1"), nb::arg("theIndex2"), D::Swap)
     .def("RemoveLast", [](M &self) { refuse_if_viewed(&self, "RemoveLast"); self.RemoveLast(); }, D::RemoveLast)
     .def("RemoveFromIndex", [](M &self, const int i) { refuse_if_viewed(&self, "RemoveFromIndex"); self.RemoveFromIndex(i); }, nb::arg("theIndex"), D::RemoveFromIndex)
     .def("RemoveKey", [](M &self, const K &k) { refuse_if_viewed(&self, "RemoveKey"); return self.RemoveKey(k); }, nb::arg("theKey"), D::RemoveKey)
     .def("FindKey", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindKey(i)); }, nb::arg("theIndex"), D::FindKey)
     .def("__call__", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindKey(i)); }, nb::arg("theIndex"), D::op_call)
     .def("FindIndex", [](const M &self, const K &k) { return self.FindIndex(k); }, nb::arg("theKey"), D::FindIndex)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), "Python addition: alias to Contains.")
     .def("__getitem__", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindKey(i)); }, nb::arg("theIndex"), "Python addition: alias to FindKey (1-based index).")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Value(); }); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the keys in index order.");
}

// ---- NCollection_IndexedDataMap<K, V, Hasher>
template <typename K, typename V, typename H = NCollection_DefaultHasher<K>> void bind_NCollection_IndexedDataMap(nb::module_ &m, const char *name) {
    using M = NCollection_IndexedDataMap<K, V, H>;
    using It = typename M::Iterator;
    namespace D = nanocct_doc::NCollection_IndexedDataMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It> it(c, "Iterator", D::Iterator::class_doc);
    it.def(nb::init<>(), D::Iterator::ctor)
      .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
      .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
      .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
      .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value)
      .def("Key", [](const It &self) -> decltype(auto) { return owned(self.Key()); }, D::Iterator::Key)
      .def("Index", [](const It &self) { return self.Index(); }, D::Iterator::Index)
      .def("IsEqual", [](const It &self, const It &o) { return self.IsEqual(o); }, nb::arg("theOther"), D::Iterator::IsEqual);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    def_elem<V, elem_view_of_iterator>(it, "ChangeValue", [](It &self) -> V & { return self.ChangeValue(); }, D::Iterator::ChangeValue);
    def_basemap_members<true>(c, NANOCCT_BASEMAP_DOCS(D));
    // R-VIEW-GUARD: as IndexedMap -- adding, binding (in place for a bound key), Substitute and Swap keep every node
    c.def("Add", [](M &self, const K &k, const V &v) { own(self, k); own(self, v); return self.Add(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Add)
     .def("TryBind", [](M &self, const K &k, const V &v) { own(self, k); own(self, v); return self.TryBind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBind)
     .def("Bind", [](M &self, const K &k, const V &v) { own(self, k); own(self, v); return self.Bind(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bind)
     .def("Contains", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), D::Contains)
     .def("Substitute", [](M &self, const int i, const K &k, const V &v) { own(self, k); own(self, v); self.Substitute(i, k, v); }, nb::arg("theIndex"), nb::arg("theKey"), nb::arg("theItem"), D::Substitute)
     .def("Swap", [](M &self, const int i, const int j) { self.Swap(i, j); }, nb::arg("theIndex1"), nb::arg("theIndex2"), D::Swap)
     .def("RemoveLast", [](M &self) { refuse_if_viewed(&self, "RemoveLast"); self.RemoveLast(); }, D::RemoveLast)
     .def("RemoveFromIndex", [](M &self, const int i) { refuse_if_viewed(&self, "RemoveFromIndex"); self.RemoveFromIndex(i); }, nb::arg("theIndex"), D::RemoveFromIndex)
     .def("RemoveKey", [](M &self, const K &k) { refuse_if_viewed(&self, "RemoveKey"); self.RemoveKey(k); }, nb::arg("theKey"), D::RemoveKey)
     .def("FindKey", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindKey(i)); }, nb::arg("theIndex"), D::FindKey)
     .def("FindFromIndex", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindFromIndex(i)); }, nb::arg("theIndex"), D::FindFromIndex)
     .def("__call__", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindFromIndex(i)); }, nb::arg("theIndex"), D::op_call)
     .def("FindIndex", [](const M &self, const K &k) { return self.FindIndex(k); }, nb::arg("theKey"), D::FindIndex)
     .def("FindFromKey", [](const M &self, const K &k) -> decltype(auto) { return owned(self.FindFromKey(k)); }, nb::arg("theKey"), D::FindFromKey)
     // Python additions
     .def("__contains__", [](const M &self, const K &k) { return self.Contains(k); }, nb::arg("theKey"), "Python addition: alias to Contains.")
     .def("__getitem__", [](const M &self, const int i) -> decltype(auto) { return owned(self.FindFromIndex(i)); }, nb::arg("theIndex"), "Python addition: alias to FindFromIndex (1-based index).")
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) -> const K & { return it.Key(); }); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the keys in index order.")
     .def("items", [](const M &self) {
              nb::list out;
              for (It it(self); it.More(); it.Next()) out.append(nb::make_tuple(owned(it.Key()), owned(it.Value())));
              return out; }, "Python addition: list of (key, value) tuples in index order.");
    def_elem<V>(c, "TryBound", [](M &self, const K &k, const V &v) -> V & { own(self, k); own(self, v); return self.TryBound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::TryBound);
    def_elem<V>(c, "Bound", [](M &self, const K &k, const V &v) -> V & { own(self, k); own(self, v); return *self.Bound(k, v); }, nb::arg("theKey"), nb::arg("theItem"), D::Bound);
    def_elem<V>(c, "ChangeFromIndex", [](M &self, const int i) -> V & { return self.ChangeFromIndex(i); }, nb::arg("theIndex"), D::ChangeFromIndex);
    def_elem<V>(c, "ChangeFromKey", [](M &self, const K &k) -> V & { return self.ChangeFromKey(k); }, nb::arg("theKey"), D::ChangeFromKey);
    if constexpr (std::is_class_v<V>) {
        c.def("Seek", [](const M &self, const K &k) -> decltype(auto) { return owned_ptr(self.Seek(k)); }, nb::rv_policy::copy, nb::arg("theKey"), D::Seek)   // a copy, as above
         .def("ChangeSeek", [](M &self, const K &k) -> V * { return self.ChangeSeek(k); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theKey"), D::ChangeSeek)
         .def("FindFromKey", [](const M &self, const K &k, V &v) { const bool found = self.FindFromKey(k, v); own_out(v); return found; }, nb::arg("theKey"), nb::arg("theValue"), D::FindFromKey);
    } else {
        c.def("Seek", [](const M &self, const K &k) -> std::optional<V> { const V *p = self.Seek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::Seek)
         .def("ChangeSeek", [](M &self, const K &k) -> std::optional<V> { V *p = self.ChangeSeek(k); return p ? std::optional<V>(*p) : std::nullopt; }, nb::arg("theKey"), D::ChangeSeek);
    }
}

// ---------------------------------------------------------------------------------------------------
// NCollection_Array2<T> (derives from NCollection_Array1<T>, whose binding it inherits) / HArray2
// R-VIEW-GUARD: whether Resize/ResizeWithTrim to rows x cols reallocates (NCollection_Array2.hxx: without data through
// Array1::Resize -- the same number of elements stays; with data resizeImpl keeps the buffer only for the same shape).
// Invalid bounds (no rows or columns) are left to OCCT's own check.
template <typename A2> void refuse_if_reshaped(A2 &self, long long rows, long long cols, bool copy, const char *what) {
    if (rows <= 0 || cols <= 0)
        return;
    const bool same = copy ? rows == self.NbRows() && cols == self.NbColumns() : (size_t) (rows * cols) == self.Size();
    if (!same)
        refuse_if_viewed(&self, what);
}

template <typename T, typename Cls, typename... Extra> void def_array2_members(nb::class_<Cls, Extra...> &c) {
    static_assert(owners_not_supported<T>, "R-OWNER: the Array2 binder does not keep the owners of its elements");
    using A2 = NCollection_Array2<T>;
    namespace D = nanocct_doc::NCollection_Array2;
    // R-STATIC-S: statics carry _s here too, as in the generated bindings
    c.def_static("BeginPosition_s", [](int r1, int r2, int c1, int c2) { return A2::BeginPosition(r1, r2, c1, c2); },
                 nb::arg("theRowLower"), nb::arg("theRowUpper"), nb::arg("theColLower"), nb::arg("theColUpper"), D::BeginPosition)
     .def_static("LastPosition_s", [](int r1, int r2, int c1, int c2) { return A2::LastPosition(r1, r2, c1, c2); },
                 nb::arg("theRowLower"), nb::arg("theRowUpper"), nb::arg("theColLower"), nb::arg("theColUpper"), D::LastPosition)
     .def("Size", [](const Cls &self) { return self.Size(); }, D::Size)
     .def("Length", [](const Cls &self) { return self.Length(); }, D::Length)
     .def("NbRows", [](const Cls &self) { return self.NbRows(); }, D::NbRows)
     .def("NbColumns", [](const Cls &self) { return self.NbColumns(); }, D::NbColumns)
     .def("RowLength", [](const Cls &self) { return self.RowLength(); }, D::RowLength)
     .def("ColLength", [](const Cls &self) { return self.ColLength(); }, D::ColLength)
     .def("LowerRow", [](const Cls &self) { return self.LowerRow(); }, D::LowerRow)
     .def("UpperRow", [](const Cls &self) { return self.UpperRow(); }, D::UpperRow)
     .def("LowerCol", [](const Cls &self) { return self.LowerCol(); }, D::LowerCol)
     .def("UpperCol", [](const Cls &self) { return self.UpperCol(); }, D::UpperCol)
     .def("UpdateLowerRow", [](Cls &self, const int v) { self.UpdateLowerRow(v); }, nb::arg("theLowerRow"), D::UpdateLowerRow)
     .def("UpdateLowerCol", [](Cls &self, const int v) { self.UpdateLowerCol(v); }, nb::arg("theLowerCol"), D::UpdateLowerCol)
     .def("UpdateUpperRow", [](Cls &self, const int v) { self.UpdateUpperRow(v); }, nb::arg("theUpperRow"), D::UpdateUpperRow)
     .def("UpdateUpperCol", [](Cls &self, const int v) { self.UpdateUpperCol(v); }, nb::arg("theUpperCol"), D::UpdateUpperCol)
     // R-VIEW-GUARD: Assign as Array1's (the same number of elements copies in place); Resize/ResizeWithTrim without data
     // keep the buffer for the same number of elements, with data only for the same rows and columns (NCollection_Array2.hxx,
     // resizeImpl moves *this into a temporary otherwise)
     .def("Assign", [](Cls &self, const A2 &o) -> Cls & { if (o.Size() != self.Size()) refuse_if_viewed(&self, "Assign"); self.Assign(o); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::Assign)
     .def("CopyValues", [](Cls &self, const A2 &o) -> Cls & { self.CopyValues(o); return self; }, nb::rv_policy::reference, nb::arg("theOther"), D::CopyValues)
     .def("Value", [](const Cls &self, const int r, const int c) -> const T & { return self.Value(r, c); }, nb::arg("theRow"), nb::arg("theCol"), D::Value)
     .def("__call__", [](const Cls &self, const int r, const int c) -> const T & { return self.Value(r, c); }, nb::arg("theRow"), nb::arg("theCol"), D::op_call)
     .def("SetValue", [](Cls &self, const int r, const int c, const T &v) { self.SetValue(r, c, v); }, nb::arg("theRow"), nb::arg("theCol"), nb::arg("theItem"), D::SetValue)
     .def("At", [](const Cls &self, const size_t r, const size_t c) -> const T & { return self.At(r, c); }, nb::arg("theRow"), nb::arg("theCol"), D::At)
     .def("Resize", [](Cls &self, int r1, int r2, int c1, int c2, bool copy) {
              refuse_if_reshaped(self, (long long) r2 - r1 + 1, (long long) c2 - c1 + 1, copy, "Resize"); self.Resize(r1, r2, c1, c2, copy); },
          nb::arg("theRowLower"), nb::arg("theRowUpper"), nb::arg("theColLower"), nb::arg("theColUpper"), nb::arg("theToCopyData"), D::Resize)
     .def("Resize", [](Cls &self, size_t rows, size_t cols, bool copy) {
              refuse_if_reshaped(self, (long long) rows, (long long) cols, copy, "Resize"); self.Resize(rows, cols, copy); }, nb::arg("theNbRows"), nb::arg("theNbCols"), nb::arg("theToCopyData"), D::Resize)
     .def("ResizeWithTrim", [](Cls &self, int r1, int r2, int c1, int c2, bool copy) {
              refuse_if_reshaped(self, (long long) r2 - r1 + 1, (long long) c2 - c1 + 1, copy, "ResizeWithTrim"); self.ResizeWithTrim(r1, r2, c1, c2, copy); },
          nb::arg("theRowLower"), nb::arg("theRowUpper"), nb::arg("theColLower"), nb::arg("theColUpper"), nb::arg("theToCopyData"), D::ResizeWithTrim)
     .def("ResizeWithTrim", [](Cls &self, size_t rows, size_t cols, bool copy) {
              refuse_if_reshaped(self, (long long) rows, (long long) cols, copy, "ResizeWithTrim"); self.ResizeWithTrim(rows, cols, copy); }, nb::arg("theNbRows"), nb::arg("theNbCols"), nb::arg("theToCopyData"), D::ResizeWithTrim)
     // Python additions: a[(row, col)]
     .def("__getitem__", [](const Cls &self, std::pair<int, int> rc) -> const T & { return self.Value(rc.first, rc.second); }, nb::arg("theRowCol"), "Python addition: a[(row, col)] -> Value(row, col).")
     .def("__setitem__", [](Cls &self, std::pair<int, int> rc, const T &v) { self.SetValue(rc.first, rc.second, v); }, nb::arg("theRowCol"), nb::arg("theItem"), "Python addition: a[(row, col)] = item -> SetValue.");
    // R-VIEW: the 2-D shape, which shadows the flat one inherited from the Array1 binding. Measured, not
    // assumed: NCollection_Array2 allocates one contiguous buffer and addresses it row-major --
    // `(theRow - myLowerRow) * mySizeCol + (theCol - myLowerCol)` (NCollection_Array2.hxx:306).
    if constexpr (nanocct::view_elem<T>::supported)
        c.def("__array__", [](Cls &self, nb::handle, std::optional<bool> copy) {
            const size_t shape[2] = { (size_t) self.NbRows(), (size_t) self.NbColumns() };
            return container_array<T>(
                self.Size() == 0 ? nullptr : (void *) &self.ChangeValue(self.LowerRow(), self.LowerCol()), shape, self, copy);
        }, nb::arg("dtype") = nb::none(), nb::arg("copy") = nb::none(),
        "Python addition: numpy's array protocol -- `numpy.asarray(a)` is a zero-copy view of the whole array "
        "(R-VIEW), `numpy.array(a)` a copy.\n\n"
        "Shape (NbRows(), NbColumns()) for a scalar element type and (NbRows(), NbColumns(), k) for a "
        "k-component one. Row-major, matching OCCT's own addressing; index (0, 0) is "
        "(LowerRow(), LowerCol()). Writes go straight into the array. While the view lives, a call that would "
        "reallocate the array raises BufferError, as bytearray does.");
    if constexpr (std::is_class_v<T>) {
        c.def("ChangeValue", [](Cls &self, const int r, const int cc) -> T & { return self.ChangeValue(r, cc); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theRow"), nb::arg("theCol"), D::ChangeValue)
         .def("ChangeAt", [](Cls &self, const size_t r, const size_t cc) -> T & { return self.ChangeAt(r, cc); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theRow"), nb::arg("theCol"), D::ChangeAt);
    }
}

template <typename T> void bind_NCollection_Array2(nb::module_ &m, const char *name) {
    using A2 = NCollection_Array2<T>;
    namespace D = nanocct_doc::NCollection_Array2;
    nb::class_<A2, NCollection_Array1<T>> c(m, name, D::class_doc);
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const int, const int, const int, const int>(), nb::arg("theRowLower"), nb::arg("theRowUpper"), nb::arg("theColLower"), nb::arg("theColUpper"), D::ctor)
     .def(nb::init<const size_t, const size_t>(), nb::arg("theNbRows"), nb::arg("theNbCols"), D::ctor)
     .def(nb::init<const A2 &>(), nb::arg("theOther"), D::ctor);
    def_array2_members<T, A2>(c);
}

template <typename T> void bind_NCollection_HArray2(nb::module_ &m, const char *name) {
    using A2 = NCollection_Array2<T>;
    using H = NCollection_HArray2<T>;
    namespace D = nanocct_doc::NCollection_HArray2;
    nb::class_<H, A2> c(m, name, D::class_doc);      // base = Array2<T> (offset 0), see HArray1
    c.def(nb::new_([](int r1, int r2, int c1, int c2) { return opencascade::handle<H>(new H(r1, r2, c1, c2)); }),
          nb::arg("theRowLow"), nb::arg("theRowUpp"), nb::arg("theColLow"), nb::arg("theColUpp"), D::ctor)
     .def(nb::new_([](int r1, int r2, int c1, int c2, const T &v) { return opencascade::handle<H>(new H(r1, r2, c1, c2, v)); }),
          nb::arg("theRowLow"), nb::arg("theRowUpp"), nb::arg("theColLow"), nb::arg("theColUpp"), nb::arg("theValue"), D::ctor)
     .def(nb::new_([](const A2 &a) { return opencascade::handle<H>(new H(a)); }), nb::arg("theOther"), D::ctor)
     .def("Array2", [](const A2 &b) { return A2(static_cast<const H &>(b).Array2()); }, D::Array2)
     .def("ChangeArray2", [](A2 &b) -> A2 & { return static_cast<H &>(b).ChangeArray2(); }, nb::rv_policy::reference_internal, D::ChangeArray2);
    def_transient_members<H, A2>(c);
}

// ---------------------------------------------------------------------------------------------------
// NCollection_DynamicArray<T> (0-based)
template <typename T> void bind_NCollection_DynamicArray(nb::module_ &m, const char *name) {
    static_assert(owners_not_supported<T>, "R-OWNER: the DynamicArray binder does not keep the owners of its elements");
    using V = NCollection_DynamicArray<T>;
    namespace D = nanocct_doc::NCollection_DynamicArray;
    nb::class_<V> c(m, name, D::class_doc);
    c.def(nb::init<const int>(), nb::arg("theIncrement") = 256, D::ctor)
     .def(nb::init<const int, const opencascade::handle<NCollection_BaseAllocator> &>(), nb::arg("theIncrement"), nb::arg("theAlloc").none(), D::ctor)
     .def(nb::init<const V &>(), nb::arg("theOther"), D::ctor)
     .def("Size", [](const V &self) { return self.Size(); }, D::Size)
     .def("Length", [](const V &self) { return self.Length(); }, D::Length)
     .def("Lower", [](const V &self) { return self.Lower(); }, D::Lower)
     .def("Upper", [](const V &self) { return self.Upper(); }, D::Upper)
     .def("IsEmpty", [](const V &self) { return self.IsEmpty(); }, D::IsEmpty)
     // R-VIEW-GUARD: blocks never move (NCollection_DynamicArray.hxx) -- appending and inserting keep every element in place;
     // Assign and Clear destroy or free them, EraseLast destroys the last one
     .def("Assign", [](V &self, const V &o, const bool own) -> V & { refuse_if_viewed(&self, "Assign"); return self.Assign(o, own); }, nb::rv_policy::reference, nb::arg("theOther"), nb::arg("theOwnAllocator") = true, D::Assign)
     .def("EraseLast", [](V &self) { refuse_if_viewed(&self, "EraseLast"); self.EraseLast(); }, D::EraseLast)
     .def("Value", [](const V &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::Value)
     .def("__call__", [](const V &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_call)
     .def("__getitem__", [](const V &self, const int i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_index)
     .def("First", [](const V &self) -> const T & { return self.First(); }, D::First)
     .def("Last", [](const V &self) -> const T & { return self.Last(); }, D::Last)
     .def("Clear", [](V &self, const bool release) { refuse_if_viewed(&self, "Clear"); self.Clear(release); }, nb::arg("theReleaseMemory") = false, D::Clear)
     .def("SetIncrement", [](V &self, const int inc) { self.SetIncrement(inc); }, nb::arg("theIncrement"), D::SetIncrement)
     // Python additions
     .def("__setitem__", [](V &self, const int i, const T &v) { self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), "Python addition: alias to SetValue (0-based).")
     .def("__len__", [](const V &self) { return self.Length(); }, "Python addition: alias to Length.")
     .def("__iter__", [](const V &self) { return nb::make_iterator(nb::type<V>(), "value_iterator", self.cbegin(), self.cend()); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the values.");
    def_elem<T>(c, "Append", [](V &self, const T &v) -> T & { return self.Append(v); }, nb::arg("theValue"), D::Append);
    def_elem<T>(c, "InsertAfter", [](V &self, const int i, const T &v) -> T & { return self.InsertAfter(i, v); }, nb::arg("theIndex"), nb::arg("theValue"), D::InsertAfter);
    def_elem<T>(c, "InsertBefore", [](V &self, const int i, const T &v) -> T & { return self.InsertBefore(i, v); }, nb::arg("theIndex"), nb::arg("theValue"), D::InsertBefore);
    def_elem<T>(c, "Appended", [](V &self) -> T & { return self.Appended(); }, D::Appended);
    def_elem<T>(c, "SetValue", [](V &self, const int i, const T &v) -> T & { return self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theValue"), D::SetValue);
    if constexpr (std::is_class_v<T>) {
        c.def("ChangeFirst", [](V &self) -> T & { return self.ChangeFirst(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeFirst)
         .def("ChangeLast", [](V &self) -> T & { return self.ChangeLast(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeLast)
         .def("ChangeValue", [](V &self, const int i) -> T & { return self.ChangeValue(i); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theIndex"), D::ChangeValue);
    }
}

// ---------------------------------------------------------------------------------------------------
// NCollection_LinearVector<T> (OCCT 8: contiguous 0-based vector, size_t indices; BRepGraph's container of choice).
// Data()/begin()/end() (raw element pointers) are not bound.
// R-VIEW-GUARD: Append/Insert* grow when Size() == Capacity(), SetValue past the end resizes to theIndex + 1
// (NCollection_LinearVector.hxx)
template <typename V> void refuse_if_full(V &self, const char *what) {
    if (self.Size() == self.Capacity())
        refuse_if_viewed(&self, what);
}
template <typename V> void refuse_if_grown(V &self, size_t index, const char *what) {
    if (index >= self.Capacity())
        refuse_if_viewed(&self, what);
}
template <typename T> void bind_NCollection_LinearVector(nb::module_ &m, const char *name) {
    static_assert(owners_not_supported<T>, "R-OWNER: the LinearVector binder does not keep the owners of its elements");
    using V = NCollection_LinearVector<T>;
    namespace D = nanocct_doc::NCollection_LinearVector;
    nb::class_<V> c(m, name, D::class_doc);
    c.def(nb::init<>(), D::ctor)
     .def(nb::init<const size_t>(), nb::arg("theCapacity"), D::ctor)
     .def(nb::init<const size_t, const T &>(), nb::arg("theSize"), nb::arg("theValue"), D::ctor)
     .def(nb::init<const V &>(), nb::arg("theOther"), D::ctor)
     .def("HasData", [](const V &self) { return self.HasData(); }, D::HasData)
     .def("Empty", [](const V &self) { return self.Empty(); }, D::Empty)
     .def_static("MaxSize_s", []() { return V::MaxSize(); }, D::MaxSize)   // R-STATIC-S, as in the generated bindings
     .def("Size", [](const V &self) { return self.Size(); }, D::Size)
     .def("IsEmpty", [](const V &self) { return self.IsEmpty(); }, D::IsEmpty)
     .def("Capacity", [](const V &self) { return self.Capacity(); }, D::Capacity)
     // R-VIEW-GUARD: contiguous (NCollection_LinearVector.hxx): growing past Capacity() reallocates (grow), shrinking and
     // erasing destroy elements; appending or inserting below the capacity keeps the buffer (an insert shifts values)
     .def("Reserve", [](V &self, const size_t n) { if (n > self.Capacity()) refuse_if_viewed(&self, "Reserve"); self.Reserve(n); }, nb::arg("theCapacity"), D::Reserve)
     .def("Resize", [](V &self, const size_t n) { if (n > self.Capacity() || n < self.Size()) refuse_if_viewed(&self, "Resize"); self.Resize(n); }, nb::arg("theSize"), D::Resize)
     .def("Resize", [](V &self, const size_t n, const T &v) { if (n > self.Capacity() || n < self.Size()) refuse_if_viewed(&self, "Resize"); self.Resize(n, v); }, nb::arg("theSize"), nb::arg("theValue"), D::Resize)
     .def("Value", [](const V &self, const size_t i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::Value)
     .def("__call__", [](const V &self, const size_t i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_call)
     .def("__getitem__", [](const V &self, const size_t i) -> const T & { return self.Value(i); }, nb::arg("theIndex"), D::op_index)
     .def("First", [](const V &self) -> const T & { return self.First(); }, D::First)
     .def("Last", [](const V &self) -> const T & { return self.Last(); }, D::Last)
     .def("InsertBefore", [](V &self, const size_t i, const T &v) { refuse_if_full(self, "InsertBefore"); self.InsertBefore(i, v); }, nb::arg("theIndex"), nb::arg("theValue"), D::InsertBefore)
     .def("InsertAfter", [](V &self, const size_t i, const T &v) { refuse_if_full(self, "InsertAfter"); self.InsertAfter(i, v); }, nb::arg("theIndex"), nb::arg("theValue"), D::InsertAfter)
     .def("EraseLast", [](V &self) { refuse_if_viewed(&self, "EraseLast"); self.EraseLast(); }, D::EraseLast)
     .def("Erase", [](V &self, const size_t i) { refuse_if_viewed(&self, "Erase"); self.Erase(i); }, nb::arg("theIndex"), D::Erase)
     .def("Erase", [](V &self, const size_t from, const size_t to) { refuse_if_viewed(&self, "Erase"); self.Erase(from, to); }, nb::arg("theFrom"), nb::arg("theTo"), D::Erase)
     .def("Clear", [](V &self, const bool release) { refuse_if_viewed(&self, "Clear"); self.Clear(release); }, nb::arg("theReleaseMemory") = false, D::Clear)
     // the Array1 borrows the vector's buffer (NCollection_LinearVector.hxx: Array1(myData, mySize)), so it keeps the
     // vector alive; without that it read freed memory once the vector was collected (2026-09-30). It is a view of the
     // vector's storage too (R-VIEW-GUARD): the vector refuses to reallocate while the array lives
     .def("ToArray1", [](const V &self) { return self.ToArray1(); }, nb::keep_alive<0, 1>(), elem_view_of_self(), D::ToArray1)
     // Python additions
     .def("__setitem__", [](V &self, const size_t i, const T &v) { refuse_if_grown(self, i, "__setitem__"); self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theItem"), "Python addition: alias to SetValue (0-based).")
     .def("__len__", [](const V &self) { return self.Size(); }, "Python addition: alias to Size.")
     .def("__iter__", [](const V &self) { return nb::make_iterator(nb::type<V>(), "value_iterator", self.cbegin(), self.cend()); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over the values.");
    def_elem<T>(c, "Append", [](V &self, const T &v) -> T & { refuse_if_full(self, "Append"); return self.Append(v); }, nb::arg("theValue"), D::Append);
    def_elem<T>(c, "Appended", [](V &self) -> T & { refuse_if_full(self, "Appended"); return self.Appended(); }, D::Appended);
    def_elem<T>(c, "SetValue", [](V &self, const size_t i, const T &v) -> T & { refuse_if_grown(self, i, "SetValue"); return self.SetValue(i, v); }, nb::arg("theIndex"), nb::arg("theValue"), D::SetValue);
    if constexpr (std::is_class_v<T>) {
        c.def("ChangeFirst", [](V &self) -> T & { return self.ChangeFirst(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeFirst)
         .def("ChangeLast", [](V &self) -> T & { return self.ChangeLast(); }, nb::rv_policy::reference_internal, elem_view_of_self(), D::ChangeLast)
         .def("ChangeValue", [](V &self, const size_t i) -> T & { return self.ChangeValue(i); }, nb::rv_policy::reference_internal, elem_view_of_self(), nb::arg("theIndex"), D::ChangeValue);
    }
}

// ---------------------------------------------------------------------------------------------------
// NCollection_DoubleMap<K1, K2, Hasher1, Hasher2>
template <typename K1, typename K2, typename H1 = NCollection_DefaultHasher<K1>, typename H2 = NCollection_DefaultHasher<K2>>
void bind_NCollection_DoubleMap(nb::module_ &m, const char *name) {
    using M = NCollection_DoubleMap<K1, K2, H1, H2>;
    using It = typename M::Iterator;
    namespace D = nanocct_doc::NCollection_DoubleMap;
    nb::class_<M> c(m, name, D::class_doc);
    nb::class_<It>(c, "Iterator", D::Iterator::class_doc)
        .def(nb::init<>(), D::Iterator::ctor)
        .def(nb::init<const M &>(), nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::ctor)
        .def("Initialize", [](It &self, const M &map) { self.Initialize(map); }, nb::arg("theMap"), nb::keep_alive<1, 2>(), iterator_of_arg(), D::Iterator::Initialize)
        .def("Reset", [](It &self) { self.Reset(); }, D::Iterator::Reset)
        .def("More", [](const It &self) { return self.More(); }, D::Iterator::More)
        .def("Next", [](It &self) { self.Next(); }, D::Iterator::Next)
        .def("Key1", [](const It &self) -> decltype(auto) { return owned(self.Key1()); }, D::Iterator::Key1)
        .def("Key2", [](const It &self) -> decltype(auto) { return owned(self.Key2()); }, D::Iterator::Key2)
        .def("Value", [](const It &self) -> decltype(auto) { return owned(self.Value()); }, D::Iterator::Value);
    nanocct_def_iter<It>(nb::borrow<nb::class_<It>>(c.attr("Iterator")), [](It &self) { return self.Value(); });   // R-ITER: its own Python iterator, like every More/Next/Value class
    def_basemap_members<false>(c, NANOCCT_BASEMAP_DOCS(D));
    // R-VIEW-GUARD: binding can grow both tables (iterators), UnBind1/UnBind2 free a node
    c.def("Bind", [](M &self, const K1 &a, const K2 &b) { refuse_if_iterated(&self, "Bind"); own(self, a); own(self, b); self.Bind(a, b); }, nb::arg("theKey1"), nb::arg("theKey2"), D::Bind)
     .def("TryBind", [](M &self, const K1 &a, const K2 &b) { refuse_if_iterated(&self, "TryBind"); own(self, a); own(self, b); return self.TryBind(a, b); }, nb::arg("theKey1"), nb::arg("theKey2"), D::TryBind)
     .def("AreBound", [](const M &self, const K1 &a, const K2 &b) { return self.AreBound(a, b); }, nb::arg("theKey1"), nb::arg("theKey2"), D::AreBound)
     .def("IsBound1", [](const M &self, const K1 &a) { return self.IsBound1(a); }, nb::arg("theKey1"), D::IsBound1)
     .def("IsBound2", [](const M &self, const K2 &b) { return self.IsBound2(b); }, nb::arg("theKey2"), D::IsBound2)
     .def("UnBind1", [](M &self, const K1 &a) { refuse_if_viewed(&self, "UnBind1"); return self.UnBind1(a); }, nb::arg("theKey1"), D::UnBind1)
     .def("UnBind2", [](M &self, const K2 &b) { refuse_if_viewed(&self, "UnBind2"); return self.UnBind2(b); }, nb::arg("theKey2"), D::UnBind2)
     .def("Find1", [](const M &self, const K1 &a) -> decltype(auto) { return owned(self.Find1(a)); }, nb::arg("theKey1"), D::Find1)
     .def("Find2", [](const M &self, const K2 &b) -> decltype(auto) { return owned(self.Find2(b)); }, nb::arg("theKey2"), D::Find2)
     // Python additions
     .def("__iter__", [](const M &self) { return key_iterator<M, It>(nb::type<M>(), self, [](const It &it) { return nb::make_tuple(owned(it.Key1()), owned(it.Key2())); }); },
          nb::keep_alive<0, 1>(), iterator_of_self(), "Python addition: iterates over (key1, key2) pairs.")
     .def("items", [](const M &self) {
              nb::list out;
              for (It it(self); it.More(); it.Next()) out.append(nb::make_tuple(owned(it.Key1()), owned(it.Key2())));
              return out; }, "Python addition: list of (key1, key2) tuples.");
    if constexpr (std::is_class_v<K2>) {
        c.def("Seek1", [](const M &self, const K1 &a) -> decltype(auto) { return owned_ptr(self.Seek1(a)); }, nb::rv_policy::copy, nb::arg("theKey1"), D::Seek1)   // a key: a copy, never a view
         .def("Find1", [](const M &self, const K1 &a, K2 &b) { const bool found = self.Find1(a, b); own_out(b); return found; }, nb::arg("theKey1"), nb::arg("theKey2"), D::Find1);
    } else {
        c.def("Seek1", [](const M &self, const K1 &a) -> std::optional<K2> { const K2 *p = self.Seek1(a); return p ? std::optional<K2>(*p) : std::nullopt; }, nb::arg("theKey1"), D::Seek1);
    }
    if constexpr (std::is_class_v<K1>) {
        c.def("Seek2", [](const M &self, const K2 &b) -> decltype(auto) { return owned_ptr(self.Seek2(b)); }, nb::rv_policy::copy, nb::arg("theKey2"), D::Seek2)   // a key: a copy, never a view
         .def("Find2", [](const M &self, const K2 &b, K1 &a) { const bool found = self.Find2(b, a); own_out(a); return found; }, nb::arg("theKey2"), nb::arg("theKey1"), D::Find2);
    } else {
        c.def("Seek2", [](const M &self, const K2 &b) -> std::optional<K1> { const K1 *p = self.Seek2(b); return p ? std::optional<K1>(*p) : std::nullopt; }, nb::arg("theKey2"), D::Seek2);
    }
}

// ---------------------------------------------------------------------------------------------------
// NCollection_Shared<T> (: Standard_Transient, T): T made a Standard_Transient. nanobind base = T, which
// is NOT at offset 0 -> the stored pointer is the T subobject (mi_traits); T's API is inherited,
// the Transient part is bound through adjusting downcasts. CopyT = false (R-COPY, decided by the generator): T's copy
// would share what T's destructor frees (NCollection_EBTree's nodes), so there is no constructor from a T.
template <typename T, bool CopyT = true> void bind_NCollection_Shared(nb::module_ &m, const char *name) {
    static_assert(owners_not_supported<T>, "R-OWNER: the Shared binder does not keep the owners of what it wraps");
    using S = NCollection_Shared<T>;
    namespace D = nanocct_doc::NCollection_Shared;
    nb::class_<S, T> c(m, name, D::class_doc);
    if constexpr (std::is_default_constructible_v<T>)
        c.def(nb::new_([]() { return opencascade::handle<S>(new S()); }), D::ctor);
    if constexpr (CopyT && std::is_copy_constructible_v<T>)  // NCollection_Shared<Standard_Mutex>: a mutex cannot be copied
        c.def(nb::new_([](const T &t) { return opencascade::handle<S>(new S(t)); }), nb::arg("theOther"), D::ctor);
    def_transient_members<S, T>(c);
}

} // namespace nanocct
