// Part of nanocct_common.h -- the argument and result helpers of the generated lambdas: stream text (R-STREAM-OUT/IN), R-CSTR-NULL, and the keep_slot / keep_view / const-reference result policies.
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

// Binding-Rules.md R-STREAM-OUT: the text an OCCT method wrote to a std::ostream& parameter, as a str. OCCT streams are
// text (Dump, DumpJson, Print, BRepTools::Write); decoded with surrogateescape so that a stray non-UTF-8 byte is lossless.
inline nb::str nanocct_stream_text(const std::ostringstream &stream) {
    const std::string text = stream.str();
    return nb::steal<nb::str>(PyUnicode_DecodeUTF8(text.data(), static_cast<Py_ssize_t>(text.size()), "surrogateescape"));
}

// The same for the binary formats (the BinTools package, overrides.toml [stream] binary_packages): bytes.
inline nb::bytes nanocct_stream_bytes(const std::ostringstream &stream) {
    const std::string data = stream.str();
    return nb::bytes(data.data(), data.size());
}

// Binding-Rules.md R-STREAM-IN: a std::istream& / std::stringstream parameter (BRepTools::Read, InitFromJson): the text
// of a Python file-like object (anything with read(): io.StringIO, an open text file). A str is deliberately not accepted
// -- it would collide with the file-path overloads -- so a non-file-like argument falls through to the next overload.
// Typed typing.TextIO.
namespace nanocct {
struct TextInput {
    std::string text;
};
// The binary counterpart (BinTools::Read): a binary file-like object (io.BytesIO, a file opened "rb"), whose read()
// returns bytes. Typed typing.BinaryIO. A text file-like object falls through (read() returns str).
struct BinaryInput {
    std::string data;
};
// R-CSTR-NULL: a const char* parameter with a null default (LDOM_XmlWriter(const char* theEncoding = nullptr),
// STEPCAFControl_Writer::Transfer(..., const char* const theIsMulti = nullptr)). nanobind's const char* caster rejects
// None, which would make the default unreachable; this one takes a str or None (-> nullptr). The UTF-8 buffer belongs to
// the str object, which is alive for the duration of the call (as for nanobind's own caster). Typed `str | None` (with
// .none()).
struct OptionalCString {
    const char *ptr = nullptr;
};
// R-RESULT: nb::keep_alive<0, 1> for a `T&` Transient member result, except when the result is self. A method returning
// *this (LDOM_MemManager::Self(), FSD_File::PutInteger()) hands back the same Python object, and nanobind's keep_alive_py
// has no nurse == patient check (nb_type.cpp, nanobind 3.1.0): the object would hold a reference to itself that the
// garbage collector cannot see, and would never be freed ("nanobind: leaked instances").
struct KeepOwnerUnlessSelf {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, PyObject *&ret) {
        if (ret != nullptr && ret != args[0])
            nb::keep_alive_obj(ret, args[0]);   // the result (nurse) keeps self (patient) alive
    }
};
// R-METHOD-KEEP (the table: nanocct::slots above). Patient: the argument's position as in nb::keep_alive (1 is self);
// Slot: the declaration and parameter, numbered per file. An object passed to itself is not kept by itself (a reference
// the garbage collector cannot see). R-KEPT: Self, the class the method is bound on, and Cpp, the argument passed the
// cycle check -- then a Kept<T> object keeps it in a slot of its C++ object instead of the table.
template <typename Tag, size_t Patient, size_t Slot, typename Self = void, bool Cpp = false> struct keep_slot {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle) {
        PyObject *owner = args[0];
        PyObject *argument = args[Patient - 1];          // the converted object when an implicit conversion took place
        if (argument == owner)
            return;
        kept_base *k = nullptr;
        if constexpr (Cpp)
            k = kept_of<Self>(owner);
        store_slot(owner, k, slot_key{&slot_tag<Tag>::id, Slot}, argument);
    }
};
// R-RESULT-KEEP / R-OWNER (Binding-Rules.md): a result, or an argument the call writes into, of a class that holds pointers
// keeps alive what it may point into. R: its C++ type; Owned: the generator found that R's OCAF owners are known -- checked
// against nanocct::owners, so the two cannot disagree silently; Nurse: 0 = the result, k = argument k (1 is self); Elem:
// the result's position in a returned tuple (out-parameters), -1 if none; Patients: the arguments it may point into.
// keep_alive_obj on a fresh result keeps one call's arguments; an argument written into keeps them for good, nanobind
// skipping duplicates. The nurse also keeps what the patients' slots hold now (keep_slots_of: it may point there too).
// A nurse that is also a patient (a method returning *this) keeps nothing of itself. A `const T&` of
// a class that cannot be copied comes back by reference (cref_policy) and may be an object Python already has -- one of the
// patients, even (VrmlData_Node::Scene() of the scene the node keeps): it keeps no producers, which could make a cycle.
template <typename R, bool Owned, size_t Nurse, int Elem, size_t... Patients> struct keep_view {
    using T = owner_target_t<R>;
    static_assert(owners<T>::active == Owned, "R-OWNER: the generator and nanocct::owners disagree about this type");
    static constexpr bool keeps_producers = Nurse != 0 || !std::is_lvalue_reference_v<R>
                                            || std::is_copy_constructible_v<std::remove_cv_t<std::remove_reference_t<R>>>;
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        PyObject *nurse = Nurse == 0 ? ret.ptr() : args[Nurse - 1];
        if constexpr (Elem >= 0)
            nurse = PyTuple_GetItem(nurse, Elem);       // borrowed
        if (nurse == nullptr || nurse == Py_None)
            return;
        if constexpr (keeps_producers)
            (keep_view_of(nurse, args[Patients - 1]), ...);
        if constexpr (Owned)
            owners<T>::keep(nurse, nb::cast<const T &>(nb::handle(nurse)));
    }
};
// R-RESULT: a `const T&` result is copied (nanobind's default) -- unless T cannot be copied (a deleted copy constructor
// in either form, `T(const T&)` or `T(T&)`, or a member that cannot be copied: Extrema_ExtCC, Extrema_ExtPS), where
// nanobind's copy aborts the process ("Critical nanobind error"). Such a result is handed out by reference instead:
// tied to its owner for a method (reference_internal), plain for a static method or free function (no owner).
// Decided by the compiler, so a class's copyability never has to be guessed from its header. nanobind 3.1 takes the
// policy as a compile-time tag type (nb_attr.h: a runtime rv_policy value is rejected), hence a type: cref_policy<R, O>{}.
template <typename R, bool HasOwner>
using cref_policy = nb::rv_policy::policy_tag<
    std::is_copy_constructible_v<std::remove_cv_t<std::remove_reference_t<R>>> ? nb::rv_policy::copy_v
    : HasOwner ? nb::rv_policy::reference_internal_v : nb::rv_policy::reference_v>;
