// Shared by every generated nanoOCP translation unit.
#pragma once
#include <nanobind/nanobind.h>
#include <nanobind/stl/array.h>
#include <nanobind/stl/function.h>
#include <nanobind/stl/list.h>
#include <nanobind/stl/map.h>
#include <nanobind/stl/optional.h>
#include <nanobind/stl/pair.h>
#include <nanobind/stl/set.h>
#include <nanobind/stl/shared_ptr.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/string_view.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/stl/unique_ptr.h>
#include <nanobind/stl/unordered_map.h>
#include <nanobind/stl/unordered_set.h>
#include <nanobind/stl/variant.h>
#include <nanobind/stl/vector.h>
#include <tuple>
#include <type_traits>

#include <string>
#include <typeinfo>
#include <unordered_map>

#include <Standard_Failure.hxx>
#include <Standard_Handle.hxx>
#include <Standard_Transient.hxx>

namespace nb = nanobind;

// ---------------------------------------------------------------------------------------------
// OCCT exceptions. Standard_Failure descendants declared with DEFINE_STANDARD_EXCEPTION are
// header-only, so their typeinfo is duplicated per shared object and catch-by-derived-type does
// not work across the OCCT library / extension module boundary. Each toolkit module therefore
// registers one translator that catches Standard_Failure and dispatches on the mangled name of
// the dynamic type; names it does not know are rethrown to the next module's translator, and the
// TKernel translator finally falls back to nanoocp.Standard.Standard_Failure.
inline std::unordered_map<std::string, PyObject *> &nanoocp_exception_map() {
    static std::unordered_map<std::string, PyObject *> map;
    return map;
}

template <typename T> void nanoocp_register_exception(nb::handle py_type) {
    nanoocp_exception_map()[typeid(T).name()] = py_type.ptr();
}

inline nb::object nanoocp_new_exception(nb::module_ &m, const char *name, const char *doc, PyObject *base) {
    std::string qualified = nb::borrow<nb::str>(m.attr("__name__")).c_str();
    qualified += ".";
    qualified += name;
    nb::object type = nb::steal(PyErr_NewExceptionWithDoc(qualified.c_str(), doc, base, nullptr));
    m.attr(name) = type;
    return type;
}

// fallback: the Python type for Standard_Failure, or nullptr to pass unknown exceptions on
inline void nanoocp_install_exception_translator(PyObject *fallback) {
    nb::register_exception_translator(
        [](const std::exception_ptr &p, void *payload) {
            try {
                std::rethrow_exception(p);
            } catch (const Standard_Failure &e) {
                auto &map = nanoocp_exception_map();
                auto it = map.find(typeid(e).name());
                if (it != map.end()) {
                    PyErr_SetString(it->second, e.what());
                    return;
                }
                if (payload != nullptr) {
                    PyErr_SetString((PyObject *) payload, e.what());
                    return;
                }
                throw;
            }
        },
        fallback);
}

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
        if (!caster.from_python(src, flags, cleanup)) return false;
        Td *ptr = caster.operator Td *();
        value = opencascade::handle<T>(ptr);
        return true;
    }

    static handle from_cpp(const Value &value, rv_policy, cleanup_list *cleanup) noexcept {
        Td *ptr = value.get();
        if (!ptr) return none().release();
        const std::type_info *type = &typeid(Td);
        const std::type_info *type_p = &typeid(*ptr);
        bool is_new = false;
        handle result = NB_CALL(nb_type_put)(NB_CTX_C(cleanup), type, type_p, ptr,
                                             rv_policy::reference, cleanup, &is_new);
        if (is_new) {
            auto *holder = new opencascade::handle<Standard_Transient>(ptr);
            keep_alive_cb(result, holder,
                          [](void *p) noexcept { delete (opencascade::handle<Standard_Transient> *) p; });
        }
        return result;
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)
