#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include "occ_handle.h"
#include <gp_Pnt.hxx>
#include <Standard_Transient.hxx>
#include <Geom_Geometry.hxx>
#include <Geom_Point.hxx>
#include <Geom_CartesianPoint.hxx>
#include <TopoDS_Shape.hxx>
#include <BRepPrimAPI_MakeBox.hxx>
#include <GProp_GProps.hxx>
#include <BRepGProp.hxx>
#include <STEPControl_Writer.hxx>
#include <STEPControl_Reader.hxx>
#include <Standard_Failure.hxx>
#include <StdPrs_BRepFont.hxx>
#include <StdPrs_BRepTextBuilder.hxx>
#include <Font_FontMgr.hxx>
#include <TopExp_Explorer.hxx>
#include <TopAbs_ShapeEnum.hxx>

namespace nb = nanobind;

// Simulates C++ code that stores a handle (like BRep_TFace storing a Geom_Surface)
static opencascade::handle<Geom_Point> g_store;

NB_MODULE(nanoocp_poc, m) {
    nb::class_<gp_Pnt>(m, "gp_Pnt")
        .def(nb::init<>())
        .def(nb::init<double, double, double>())
        .def("X", &gp_Pnt::X).def("Y", &gp_Pnt::Y).def("Z", &gp_Pnt::Z)
        .def("Distance", &gp_Pnt::Distance);

    nb::class_<Standard_Transient>(m, "Standard_Transient")
        .def("GetRefCount", &Standard_Transient::GetRefCount);
    nb::class_<Geom_Geometry, Standard_Transient>(m, "Geom_Geometry");
    nb::class_<Geom_Point, Geom_Geometry>(m, "Geom_Point")
        .def("Pnt", &Geom_Point::Pnt);
    nb::class_<Geom_CartesianPoint, Geom_Point>(m, "Geom_CartesianPoint")
        .def(nb::new_([](const gp_Pnt &p) { return opencascade::handle<Geom_CartesianPoint>(new Geom_CartesianPoint(p)); }))
        .def(nb::new_([](double x, double y, double z) { return opencascade::handle<Geom_CartesianPoint>(new Geom_CartesianPoint(x, y, z)); }))
        .def("SetX", &Geom_CartesianPoint::SetX);

    m.def("store", [](const opencascade::handle<Geom_Point> &h) { g_store = h; }, nb::arg("h").none());
    m.def("load", []() { return g_store; });           // returns handle<Geom_Point>; should come back as Geom_CartesianPoint
    m.def("clear", []() { g_store.Nullify(); });
    m.def("make_none", []() { return opencascade::handle<Geom_Point>(); });

    nb::class_<TopoDS_Shape>(m, "TopoDS_Shape")
        .def("IsNull", &TopoDS_Shape::IsNull)
        .def("ShapeType", [](const TopoDS_Shape &s) { return (int) s.ShapeType(); });
    nb::class_<BRepPrimAPI_MakeBox>(m, "BRepPrimAPI_MakeBox")
        .def(nb::init<double, double, double>())
        .def("Shape", &BRepPrimAPI_MakeBox::Shape);
    m.def("step_roundtrip", [](const TopoDS_Shape &s, const std::string &path) {
        STEPControl_Writer w; w.Transfer(s, STEPControl_AsIs); w.Write(path.c_str());
        STEPControl_Reader r; r.ReadFile(path.c_str()); r.TransferRoots(); return r.OneShape(); });
    // Text -> BRep via FreeType (static) + system font lookup through Font_FontMgr
    m.def("text_shape", [](const std::string &font, const std::string &text, double size) {
        occ::handle<StdPrs_BRepFont> f = StdPrs_BRepFont::FindAndCreate(font.c_str(), Font_FA_Regular, size);
        if (f.IsNull()) throw std::runtime_error("font not found: " + font);
        StdPrs_BRepTextBuilder b;
        return b.Perform(*f, NCollection_String(text.c_str()));
    });
    m.def("count", [](const TopoDS_Shape &s, int type) {
        int n = 0; for (TopExp_Explorer e(s, (TopAbs_ShapeEnum) type); e.More(); e.Next()) ++n; return n; });
    m.def("system_fonts", []() {
        occ::handle<Font_FontMgr> mgr = Font_FontMgr::GetInstance();
        return (int) mgr->GetAvailableFonts().Size(); });
    m.def("raise_occ", []() { throw Standard_Failure("boom from OCCT"); });
    m.def("volume", [](const TopoDS_Shape &s) { GProp_GProps g; BRepGProp::VolumeProperties(s, g); return g.Mass(); });
}
