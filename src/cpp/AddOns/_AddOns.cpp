// nanocct._AddOns -- hand-written additions that are *not* a 1:1 binding of an OCCT class (Binding-Rules.md R-ADDON).
//
// Everything else in nanocct mirrors OCCT. This does not, so it lives in its own package rather than being
// grafted onto an OCCT class: a user reading `AddOns.Tessellator.NormalsFromSurface(...)` can see at a glance
// that it is ours, and the 1:1 rule stays true of everything under the OCCT package names.
//
// The layout is one submodule per concern, so later additions group beside this one rather than piling up in
// a flat namespace:
//
//     nanocct.AddOns
//         Tessellator                       (Tessellator.cpp)
//             NormalsFromSurface
//             EdgeSegments
//         ShapeClean                        (ShapeClean.cpp -- a workaround for an OCCT bug, removed once OCCT is fixed)
//             ShapeUpgrade_UnifySameDomain
//
// This file only builds the module tree; each concern lives in its own source file.
#include <nanobind/nanobind.h>

namespace nb = nanobind;

void nanocct_def_Tessellator(nb::module_ &m);    // Tessellator.cpp
void nanocct_def_ShapeClean(nb::module_ &m);     // ShapeClean.cpp

NB_MODULE(_AddOns, m) {
    m.doc() = "nanocct additions that are not a 1:1 binding of OCCT";
    nb::object sys_modules = nb::module_::import_("sys").attr("modules");
    nb::module_::import_("nanocct._TKBRep");        // TopoDS_Face must be registered first
    nb::module_::import_("nanocct._TKTopAlgo");     // and BRepGProp_Face

    nb::module_ m_AddOns = m.def_submodule("AddOns", "nanocct additions (not OCCT)");
    m_AddOns.attr("__name__") = "nanocct.AddOns";
    sys_modules["nanocct._AddOns.AddOns"] = m_AddOns;

    // one submodule per concern; `import nanocct.AddOns.Tessellator` works because it is registered here
    nb::module_ m_Tess = m_AddOns.def_submodule("Tessellator", "Bulk helpers for tessellation");
    m_Tess.attr("__name__") = "nanocct.AddOns.Tessellator";
    sys_modules["nanocct.AddOns.Tessellator"] = m_Tess;
    sys_modules["nanocct._AddOns.AddOns.Tessellator"] = m_Tess;

    nanocct_def_Tessellator(m_Tess);

    // a workaround for an OCCT bug, not an addition: it carries OCCT's class name so that dropping it is an import
    // change (Binding-Rules.md R-ADDON, OCCT issue #1541)
    nb::module_ m_Clean = m_AddOns.def_submodule("ShapeClean", "Workarounds for OCCT shape-cleaning bugs");
    m_Clean.attr("__name__") = "nanocct.AddOns.ShapeClean";
    sys_modules["nanocct.AddOns.ShapeClean"] = m_Clean;
    sys_modules["nanocct._AddOns.AddOns.ShapeClean"] = m_Clean;
    nanocct_def_ShapeClean(m_Clean);
}
