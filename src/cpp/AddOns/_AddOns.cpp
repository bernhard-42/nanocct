// OCP3x._AddOns -- hand-written additions that are *not* a 1:1 binding of an OCCT class.
//
// Everything else in OCP3x mirrors OCCT. This does not, so it lives in its own package rather than being
// grafted onto an OCCT class: a user reading `AddOns.Tessellator.NormalsFromSurface(...)` can see at a glance
// that it is ours, and the 1:1 rule stays true of everything under the OCCT package names.
//
// The layout is one submodule per concern, so later additions group beside this one rather than piling up in
// a flat namespace:
//
//     OCP3x.AddOns
//         Tessellator                       (Tessellator.cpp)
//             NormalsFromSurface
//             EdgeSegments
//         ShapeClean                        (ShapeClean.cpp -- a workaround for an OCCT bug, removed once OCCT is fixed)
//             ShapeUpgrade_UnifySameDomain
//
// This file only builds the module tree; each concern lives in its own source file.
#include <nanobind/nanobind.h>

namespace nb = nanobind;

void ocp3x_def_Tessellator(nb::module_ &m);    // Tessellator.cpp
void ocp3x_def_ShapeClean(nb::module_ &m);     // ShapeClean.cpp

NB_MODULE(_AddOns, m) {
    m.doc() = "OCP3x additions that are not a 1:1 binding of OCCT";
    nb::object sys_modules = nb::module_::import_("sys").attr("modules");
    nb::module_::import_("OCP3x._TKBRep");        // TopoDS_Face must be registered first
    nb::module_::import_("OCP3x._TKTopAlgo");     // and BRepGProp_Face

    nb::module_ m_AddOns = m.def_submodule("AddOns", "OCP3x additions (not OCCT)");
    m_AddOns.attr("__name__") = "OCP3x.AddOns";
    sys_modules["OCP3x._AddOns.AddOns"] = m_AddOns;

    // one submodule per concern; `import OCP3x.AddOns.Tessellator` works because it is registered here
    nb::module_ m_Tess = m_AddOns.def_submodule("Tessellator", "Bulk helpers for tessellation");
    m_Tess.attr("__name__") = "OCP3x.AddOns.Tessellator";
    sys_modules["OCP3x.AddOns.Tessellator"] = m_Tess;
    sys_modules["OCP3x._AddOns.AddOns.Tessellator"] = m_Tess;

    ocp3x_def_Tessellator(m_Tess);

    // a workaround for an OCCT bug, not an addition: it carries OCCT's class name so that dropping it is an import
    // change (Design.md R-ADDON, OCCT issue #1541)
    nb::module_ m_Clean = m_AddOns.def_submodule("ShapeClean", "Workarounds for OCCT shape-cleaning bugs");
    m_Clean.attr("__name__") = "OCP3x.AddOns.ShapeClean";
    sys_modules["OCP3x.AddOns.ShapeClean"] = m_Clean;
    sys_modules["OCP3x._AddOns.AddOns.ShapeClean"] = m_Clean;
    ocp3x_def_ShapeClean(m_Clean);
}
