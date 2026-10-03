// Part of nanocct_common.h -- the type casters: std::bitset (R-BITSET), char16_t/char32_t (R-CHAR16), opencascade::handle<T> (R-HANDLE), NCollection_Handle<T> (R-NCHANDLE), std::reference_wrapper (R-REFWRAP).
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

// Binding-Rules.md R-BITSET: an std::bitset<N> is a set of flags indexed by an enumerator
// (ShapeProcess::OperationsFlags = std::bitset<ShapeProcess::Operation::Last + 1>), so Python sees the set of the
// indices whose bit is set: proc.ProcessShape(shape, {ShapeProcess.FixShape, ShapeProcess.SameParameter}).
// nanobind's arithmetic enums are Python IntEnums, so the enumerators go in as ints and the plain ints that come
// back compare and hash equal to them ({0, 1} == {ShapeProcess.DirectFaces, ShapeProcess.SameParameter}).
// Any iterable of indices is accepted (set, frozenset, list, tuple); str, bytes and dict are rejected so that a
// name-taking overload stays reachable (ShapeProcess::Perform(context, const char* seq, range)).
template <size_t N> struct type_caster<std::bitset<N>> {
    NB_TYPE_CASTER(std::bitset<N>, const_name("set[int]"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (src.ptr() == nullptr || str_check(src.ptr()) || bytes_check(src.ptr()) || dict_check(src.ptr()))
            return false;
        PyObject *iterator = PyObject_GetIter(src.ptr());
        if (iterator == nullptr) {
            PyErr_Clear();
            return false;
        }
        value.reset();
        bool ok = true;
        PyObject *item = nullptr;
        while (ok && (item = PyIter_Next(iterator)) != nullptr) {
            if (!int_check(item)) {
                ok = false;
            } else {
                Py_ssize_t index = PyLong_AsSsize_t(item);
                if (index < 0 || (size_t) index >= N)
                    ok = false;
                else
                    value.set((size_t) index);
            }
            Py_DECREF(item);
        }
        Py_DECREF(iterator);
        if (PyErr_Occurred() != nullptr) {
            PyErr_Clear();
            ok = false;
        }
        return ok;
    }

    static handle from_cpp(const std::bitset<N> &v, rv_policy, cleanup_list *) noexcept {
        PyObject *out = PySet_New(nullptr);
        if (out == nullptr) {
            PyErr_Clear();
            return handle();
        }
        for (size_t i = 0; i < N; ++i) {
            if (!v.test(i))
                continue;
            PyObject *index = PyLong_FromSize_t(i);
            if (index == nullptr || PySet_Add(out, index) != 0) {
                Py_XDECREF(index);
                Py_DECREF(out);
                PyErr_Clear();
                return handle();
            }
            Py_DECREF(index);
        }
        return out;
    }
};

template <> struct type_caster<nanocct::TextInput> {
    NB_TYPE_CASTER(nanocct::TextInput, const_name("typing.TextIO"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!hasattr(src, "read"))
            return false;
        try {
            object text = src.attr("read")();
            if (!str_check(text.ptr()))
                return false;
            bytes data = borrow<bytes>(text.attr("encode")("utf-8", "surrogateescape"));   // the inverse of nanocct_stream_text
            value.text.assign(data.c_str(), data.size());
        } catch (...) {
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanocct::TextInput &, rv_policy, cleanup_list *) noexcept { return none_ref(); }
};

template <> struct type_caster<nanocct::OptionalCString> {
    NB_TYPE_CASTER(nanocct::OptionalCString, const_name("str"))   // nb::arg(...).none() appends "| None"

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (src.is_none()) {
            value.ptr = nullptr;
            return true;
        }
        if (!str_check(src.ptr()))
            return false;
        Py_ssize_t size = 0;
        value.ptr = PyUnicode_AsUTF8AndSize(src.ptr(), &size);
        if (value.ptr == nullptr) {
            PyErr_Clear();
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanocct::OptionalCString &v, rv_policy, cleanup_list *) noexcept {
        if (v.ptr == nullptr)
            return none_ref();
        return PyUnicode_FromString(v.ptr);
    }
};

template <> struct type_caster<nanocct::BinaryInput> {
    NB_TYPE_CASTER(nanocct::BinaryInput, const_name("typing.BinaryIO"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!hasattr(src, "read"))
            return false;
        try {
            object data = src.attr("read")();
            if (!PyBytes_Check(data.ptr()))
                return false;
            bytes b = borrow<bytes>(data);
            value.data.assign(b.c_str(), b.size());
        } catch (...) {
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanocct::BinaryInput &, rv_policy, cleanup_list *) noexcept { return none_ref(); }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Binding-Rules.md R-CHAR16: type caster for char16_t and const char16_t* (Standard_ExtString: OCCT's UTF-16 strings,
// TCollection_ExtendedString), modeled on nanobind's char caster: a Python str converts to a NUL-terminated UTF-16
// buffer owned by the caster for the duration of the call, a const char16_t* result decodes to str, a single char16_t
// is a 1-character str.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <> struct type_caster<char16_t> {
    using Value = const char16_t *;
    Value value = nullptr;
    std::u16string storage;
    static constexpr auto Name = const_name("str");
    template <typename T_>
    using Cast = std::conditional_t<is_pointer_v<T_>, const char16_t *, char16_t>;

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!str_check(src.ptr()))
            return false;
        PyObject *bytes = PyUnicode_AsUTF16String(src.ptr());     // BOM + native byte order
        if (bytes == nullptr) {
            PyErr_Clear();
            return false;
        }
        char *buf = nullptr;
        Py_ssize_t n = 0;
        if (PyBytes_AsStringAndSize(bytes, &buf, &n) != 0) {
            PyErr_Clear();
            Py_DECREF(bytes);
            return false;
        }
        const char16_t *units = reinterpret_cast<const char16_t *>(buf);
        size_t count = static_cast<size_t>(n) / sizeof(char16_t);
        if (count > 0 && units[0] == u'\uFEFF') {
            ++units;
            --count;
        }
        storage.assign(units, count);
        Py_DECREF(bytes);
        value = storage.c_str();
        return true;
    }

    static handle from_cpp(const char16_t *v, rv_policy, cleanup_list *) noexcept {
        if (v == nullptr)
            return none_ref();
        int byteorder = 0;                                          // native
        return PyUnicode_DecodeUTF16(reinterpret_cast<const char *>(v),
                                     static_cast<Py_ssize_t>(std::char_traits<char16_t>::length(v) * sizeof(char16_t)),
                                     nullptr, &byteorder);
    }

    static handle from_cpp(char16_t v, rv_policy, cleanup_list *) noexcept {
        int byteorder = 0;
        return PyUnicode_DecodeUTF16(reinterpret_cast<const char *>(&v), sizeof(char16_t), nullptr, &byteorder);
    }

    template <typename T_>
    NB_INLINE bool can_cast() const noexcept {
        return std::is_pointer_v<T_> || storage.size() == 1;
    }

    explicit operator const char16_t *() { return value; }

    explicit operator char16_t() {
        if (storage.size() == 1)
            return storage[0];
        throw next_overload();
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Type caster for char32_t (Standard_Utf32Char: the code-point API of Font_FTFont, Font_TextFormatter, NCollection_UtfString):
// a 1-character Python str, like char and char16_t (Binding-Rules.md R-CHAR16).
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <> struct type_caster<char32_t> {
    NB_TYPE_CASTER(char32_t, const_name("str"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!str_check(src.ptr()) || PyUnicode_GetLength(src.ptr()) != 1)
            return false;
        Py_UCS4 c = PyUnicode_ReadChar(src.ptr(), 0);
        if (c == (Py_UCS4) -1 && PyErr_Occurred()) {
            PyErr_Clear();
            return false;
        }
        value = static_cast<char32_t>(c);
        return true;
    }

    static handle from_cpp(char32_t v, rv_policy, cleanup_list *) noexcept {
        int byteorder = 0;                                          // native; PyUnicode_FromKindAndData is not in the stable ABI
        return PyUnicode_DecodeUTF32(reinterpret_cast<const char *>(&v), sizeof(char32_t), nullptr, &byteorder);
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Binding-Rules.md R-HANDLE: opencascade::handle<T> is transparent -- the most-derived registered type, a null handle is
// None, None is a null handle.
// Type caster for opencascade::handle<T> (also occ::handle<T>), modeled on nanobind's shared_ptr
// caster. The Python instance never owns the C++ object directly; a heap-allocated handle is attached
// via keep_alive, so OCCT's intrusive reference count governs the lifetime on both sides.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <typename T> struct type_caster<opencascade::handle<T>> {
    static constexpr bool IsClass = true;
    using Caster = make_caster<T>;
    using Td = std::decay_t<T>;
    NB_TYPE_CASTER(opencascade::handle<T>, Caster::Name)

    bool from_python(handle src, uint32_t flags, cleanup_list *cleanup) noexcept {
        if (src.is_none()) { value = opencascade::handle<T>(); return true; }
        flags &= ~cast_flags::convert;
        Caster caster;
        if (caster.from_python(src, flags, cleanup)) {
            Td *ptr = caster.operator Td *();
            if constexpr (has_mi_traits<Td>::value)      // stored pointer is the offset-0 base subobject
                ptr = static_cast<Td *>(reinterpret_cast<typename mi_traits<Td>::base *>(static_cast<void *>(ptr)));
            // A reference count of 0 means no handle owns the object: nanobind does (a by-value copy, a member reached
            // through a field). A handle made from it would delete that memory when it goes, whatever C++ does with it
            // (8.18). Every Transient nanocct creates is handle-held (constructors, R-RESULT), so this is a gap in the
            // bindings; refusing the argument turns a crash into a TypeError.
            if (ptr != nullptr && ptr->GetRefCount() == 0)
                return false;
            value = opencascade::handle<T>(ptr);
            return true;
        }
        // a multiple-inheritance type whose Transient base is not the bound base (HArray1 -> Standard_Transient)
        for (const mi_entry &e : nanocct_mi_list()) {
            if (PyType_IsSubtype(Py_TYPE(src.ptr()), (PyTypeObject *) e.py_type)) {
                Standard_Transient *t = e.to_transient(inst_ptr<void>(src));
                Td *ptr = dynamic_cast<Td *>(t);
                if (ptr == nullptr || ptr->GetRefCount() == 0) return false;   // count 0: see above
                value = opencascade::handle<T>(ptr);
                return true;
            }
        }
        return false;
    }

    // Documented nanobind API only (Toolchain.md 4.3): the object's existing Python object when it has one (nb::find, a
    // cast with rv_policy::none), else a new one that does not own it -- nb::inst_reference for a type in the MI registry
    // (a multiple-inheritance H-collection, a nanocct::Kept<T>, whose own typeid nanobind does not know), nb::cast with
    // rv_policy::reference otherwise (nanobind's automatic downcasting: the most-derived bound type). Only a new one gets
    // the heap handle that keeps the object alive; another thread creating it in between (free-threading) costs one more
    // holder, freed with the Python object.
    static handle from_cpp(const Value &value, rv_policy, cleanup_list *) noexcept {
        Td *ptr = value.get();
        if (!ptr) return none().release();
        object result;
        try {
            // the registry entry of the dynamic type (a registered MI type, or a nanocct::Kept<T>: R-KEPT), else of a static MI
            // type: nanobind stores such an object by its base subobject, not by the address of Td
            const mi_entry *entry = nullptr;
            void *stored = ptr;
            auto &mi = nanocct_mi_by_name();
            auto it = mi.find(typeid(*ptr).name());
            if constexpr (has_mi_traits<Td>::value)
                if (it == mi.end())
                    it = mi.find(typeid(Td).name());
            if (it != mi.end()) {
                entry = &it->second;
                stored = entry->from_transient(ptr);
            } else if constexpr (has_mi_traits<Td>::value) {
                return handle();                        // an MI type is registered when it is bound (nanocct_register_mi)
            }
            object existing = entry != nullptr ? steal(entry->find(stored)) : nb::find(*ptr);
            if (existing.is_valid())
                return existing.release();
            result = entry != nullptr ? inst_reference(handle(entry->py_type), stored) : nb::cast(ptr, rv_policy::reference);
        } catch (...) {
            return handle();                            // no bound type for the object: nanobind reports the failed conversion
        }
        auto *holder = new opencascade::handle<Standard_Transient>(ptr);
        keep_alive_cb(result, holder,
                      [](void *p) noexcept { delete (opencascade::handle<Standard_Transient> *) p; });
        return result.release();
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Type caster for NCollection_Handle<T> (R-NCHANDLE): OCCT's reference-counted owner of a *non*-Transient
// object, transparent like opencascade::handle. A result is the object itself, shared with its owner as in C++, kept
// alive by a heap copy of the handle attached with keep_alive (the handle's hidden Ptr is a Standard_Transient, so OCCT's
// reference count governs the lifetime). A null handle is None -- IsNull() is asked first, because
// NCollection_Handle::get() dereferences the null Ptr (NCollection_Handle.hxx). A parameter takes the object or None, and
// the object is COPIED into a new handle: the handle deletes what it holds, and the Python object owns its C++ object.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <typename T> struct type_caster<NCollection_Handle<T>> {
    static constexpr bool IsClass = true;
    using Caster = make_caster<T>;
    NB_TYPE_CASTER(NCollection_Handle<T>, Caster::Name)

    bool from_python(handle src, uint32_t flags, cleanup_list *cleanup) noexcept {
        if (src.is_none()) { value = NCollection_Handle<T>(); return true; }
        flags &= ~cast_flags::convert;
        Caster caster;
        if (!caster.from_python(src, flags, cleanup))
            return false;
        T *ptr = caster.operator T *();
        if (ptr == nullptr)
            return false;
        try {
            value = NCollection_Handle<T>(new T(*ptr));
        } catch (...) {
            return false;
        }
        return true;
    }

    // documented nanobind API only, as for opencascade::handle above: the existing Python object (nb::find), else a new one
    // that does not own the object (rv_policy::reference) with the holder attached
    static handle from_cpp(const Value &value, rv_policy, cleanup_list *) noexcept {
        if (value.IsNull()) return none().release();
        T *ptr = const_cast<T *>(value.get());
        object result;
        try {
            object existing = nb::find(*ptr);
            if (existing.is_valid())
                return existing.release();
            result = nb::cast(ptr, rv_policy::reference);
        } catch (...) {
            return handle();
        }
        auto *holder = new NCollection_Handle<T>(value);
        keep_alive_cb(result, holder, [](void *p) noexcept { delete (NCollection_Handle<T> *) p; });
        return result.release();
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Binding-Rules.md R-REFWRAP: type caster for std::reference_wrapper<T> results: NCollection_FlatMap::Contained()
// returns std::optional<std::reference_wrapper<const K>>, NCollection_FlatDataMap::Contained() an optional pair of them.
// nanobind has no caster for it, so without this one those members would raise TypeError. A const T is returned as a
// copy (a read-only key or value); a mutable T as a reference into its owner that keeps the owner alive
// (reference_internal), so edits reach the map as in C++. Results only: no OCCT parameter takes a reference_wrapper.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <typename T> struct type_caster<std::reference_wrapper<T>> {
    using Td = std::remove_cv_t<T>;
    using Caster = make_caster<Td>;
    static constexpr auto Name = Caster::Name;

    static handle from_cpp(std::reference_wrapper<T> value, rv_policy policy, cleanup_list *cleanup) noexcept {
        if constexpr (std::is_const_v<T>)
            policy = rv_policy::copy;
        else if (policy == rv_policy::automatic || policy == rv_policy::automatic_reference)
            policy = rv_policy::reference_internal;
        return Caster::from_cpp(value.get(), policy, cleanup);
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)
