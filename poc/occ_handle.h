// Type caster for opencascade::handle<T>, modeled on nanobind's shared_ptr caster.
// Python instance never owns the C++ object directly; instead a heap-allocated
// handle<T> is attached via keep_alive, so the intrusive refcount governs lifetime.
#pragma once
#include <nanobind/nanobind.h>
#include <Standard_Handle.hxx>

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
        value = opencascade::handle<T>(ptr);   // intrusive +1
        return true;
    }

    static handle from_cpp(const Value &value, rv_policy, cleanup_list *cleanup) noexcept {
        Td *ptr = value.get();
        if (!ptr) return none().release();
        const std::type_info *type = &typeid(Td);
        const std::type_info *type_p = &typeid(*ptr);   // Standard_Transient is polymorphic
        bool is_new = false;
        handle result = NB_CALL(nb_type_put)(NB_CTX_C(cleanup), type, type_p, ptr,
                                             rv_policy::reference, cleanup, &is_new);
        if (is_new) {
            // Python object now holds one intrusive reference, released on GC.
            auto *holder = new opencascade::handle<Standard_Transient>(ptr);
            keep_alive_cb(result, holder,
                       [](void *p) noexcept { delete (opencascade::handle<Standard_Transient> *) p; });
        }
        return result;
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)
