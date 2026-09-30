// nanocct.AddOns.Tessellator -- bulk helpers for tessellation (Design.md R-ADDON).
//
// Why it exists. Zero-copy views (R-VIEW) bring the *data* side of tessellation to the speed
// of a C++ extension -- measured against ocp-addons' NativeTessellator, vertices/triangles/UVs and their
// assembly come out at 1.06x of it. What a view cannot do is the part that is a *computation*: a surface
// normal per node, which OCCT offers only as BRepGProp_Face::Normal(u, v, ...), one call at a time. In the
// pure-numpy spike that single loop was 77% of the remaining time (3.22 ms of 4.20 ms over four shapes).
//
// OCCT's own Poly_Triangulation normals are not a substitute: BRepLib::EnsureNormalConsistency fills them in
// 0.1 ms for a whole shape, but on a fused solid 2 of 1773 nodes came out flipped by 180 degrees -- the
// dark-speck artefact that ocp-tessellate's UV clamping exists to avoid.
#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

#include <BRepAdaptor_Curve.hxx>
#include <BRepGProp_Face.hxx>
#include <BRep_Tool.hxx>
#include <GeomAbs_CurveType.hxx>
#include <NCollection_IndexedDataMap.hxx>
#include <NCollection_IndexedMap.hxx>
#include <NCollection_List.hxx>
#include <Poly_PolygonOnTriangulation.hxx>
#include <Poly_Triangulation.hxx>
#include <TopAbs_ShapeEnum.hxx>
#include <TopExp.hxx>
#include <TopLoc_Location.hxx>
#include <TopTools_ShapeMapHasher.hxx>
#include <TopoDS.hxx>
#include <TopoDS_Edge.hxx>
#include <TopoDS_Face.hxx>
#include <TopoDS_Shape.hxx>
#include <gp_Pnt.hxx>
#include <gp_Vec.hxx>

#include <vector>

namespace nb = nanobind;

namespace {

//! One surface normal per (u, v), evaluated in C++ so the per-node OCCT call never crosses into Python.
//!
//! @param theFace     the face whose surface is evaluated
//! @param theUV       (N, 2) float64 array of parameters, C-contiguous. **Clamp it to the face domain
//!                    first** (BRepTools::UVBounds): a tessellation can place a node's UV one ULP outside
//!                    the bounds at a parametric singularity -- a sphere pole, say -- and the normal
//!                    evaluated just across the singularity comes back inward-flipped. numpy.clip does that
//!                    in one call, so it stays the caller's business rather than being hidden here.
//! @param theReverse  negate every normal (the caller passes true for a TopAbs_INTERNAL face)
//! @return            (N, 3) float64 array, normalised; a zero-length normal is left as zero
nb::ndarray<nb::numpy, double, nb::ndim<2>> NormalsFromSurface(
    const TopoDS_Face &theFace,
    nb::ndarray<const double, nb::ndim<2>, nb::c_contig> theUV,
    bool theReverse)
{
    if (theUV.shape(1) != 2)
        throw nb::value_error("NormalsFromSurface: theUV must have shape (N, 2)");

    const size_t aNbNodes = theUV.shape(0);
    const double *aUV = theUV.data();

    // owned by the returned array: nanobind frees it when the last reference goes
    double *anOut = new double[aNbNodes * 3];
    nb::capsule anOwner(anOut, [](void *p) noexcept { delete[] static_cast<double *>(p); });

    BRepGProp_Face aProp(theFace);
    gp_Pnt aPnt;
    gp_Vec aNorm;
    for (size_t i = 0; i < aNbNodes; ++i)
    {
        aProp.Normal(aUV[2 * i], aUV[2 * i + 1], aPnt, aNorm);
        if (aNorm.SquareMagnitude() > 0.0)
            aNorm.Normalize();
        if (theReverse)
            aNorm.Reverse();
        anOut[3 * i]     = aNorm.X();
        anOut[3 * i + 1] = aNorm.Y();
        anOut[3 * i + 2] = aNorm.Z();
    }
    return nb::ndarray<nb::numpy, double, nb::ndim<2>>(anOut, { aNbNodes, 3 }, anOwner);
}

//! Every edge's polyline, for a whole shape, as consecutive point pairs -- the loop that would otherwise run
//! once per edge from Python.
//!
//! Mirrors ocp_tessellate.Tessellator.compute_edges exactly: iterate the *edge* map in index order, take each
//! edge's first ancestor face, and skip an edge with no face, no triangulation or no polygon on it -- so the
//! per-edge counts stay aligned with whatever the caller records alongside them.
//!
//! Why this is C++ and the face path need not be: an edge carries ~26 points against a face's ~128, so the
//! per-item Python overhead never amortises. Vectorising *inside* one edge saved almost nothing -- 33 370
//! edges took 221 ms from Python against pure Python's 274 ms, while the same shape's faces went 4.9 s -> 0.49 s.
//!
//! The curve type comes along because the caller cannot compute it afterwards: which edges were skipped is
//! decided here, so a Python loop over the edge map could not be aligned with the counts without redoing the
//! triangulation and polygon lookups this function exists to avoid. It is BRepAdaptor_Curve::GetType, the
//! same value ocp-tessellate records as edge_types, and it costs ~25 ms over the 33 388 edges of a real
//! assembly against ~350 ms for the whole extraction.
//!
//! @return (segments, segments_per_edge, edge_types): (2 * S, 3) float64 of segment endpoints, flattened as
//!         the tessellator expects, and two (E,) int32 arrays -- segments per edge, and GeomAbs_CurveType
//!         per edge -- for the edges that were not skipped, in edge-map order.
nb::object EdgeSegments(const TopoDS_Shape &theShape)
{
    using ShapeMap  = NCollection_IndexedMap<TopoDS_Shape, TopTools_ShapeMapHasher>;
    using ShapeList = NCollection_List<TopoDS_Shape>;
    using AncMap    = NCollection_IndexedDataMap<TopoDS_Shape, ShapeList, TopTools_ShapeMapHasher>;

    ShapeMap anEdges;
    TopExp::MapShapes(theShape, TopAbs_EDGE, anEdges);
    AncMap anAncestors;
    TopExp::MapShapesAndAncestors(theShape, TopAbs_EDGE, TopAbs_FACE, anAncestors);

    std::vector<double> aPts;
    std::vector<int32_t> aPerEdge;
    std::vector<int32_t> aTypes;
    for (int i = 1; i <= anEdges.Extent(); ++i)
    {
        const TopoDS_Edge &anEdge = TopoDS::Edge(anEdges.FindKey(i));
        if (!anAncestors.Contains(anEdge))
            continue;
        const ShapeList &aFaces = anAncestors.FindFromKey(anEdge);
        if (aFaces.IsEmpty())
            continue;

        TopLoc_Location aLoc;
        const occ::handle<Poly_Triangulation> aTri =
            BRep_Tool::Triangulation(TopoDS::Face(aFaces.First()), aLoc);
        if (aTri.IsNull())
            continue;
        const occ::handle<Poly_PolygonOnTriangulation> aPoly =
            BRep_Tool::PolygonOnTriangulation(anEdge, aTri, aLoc);
        if (aPoly.IsNull())
            continue;

        // A polygon of fewer than two nodes yields no segment but is still an edge that was kept:
        // ocp-tessellate records its type and a count of zero, and the three arrays have to stay aligned.
        // A degenerated edge reaches this point -- it has no 3D curve, but it has a pcurve, so
        // BRepAdaptor_Curve falls back to Adaptor3d_CurveOnSurface rather than throwing.
        aTypes.push_back(static_cast<int32_t>(BRepAdaptor_Curve(anEdge).GetType()));

        const gp_Trsf &aTrsf = aLoc.Transformation();
        const int aNb = aPoly->NbNodes();
        if (aNb >= 2)
        {
            gp_Pnt aPrev = aTri->Node(aPoly->Node(1)).Transformed(aTrsf);
            for (int j = 2; j <= aNb; ++j)
            {
                const gp_Pnt aCur = aTri->Node(aPoly->Node(j)).Transformed(aTrsf);
                aPts.insert(aPts.end(), { aPrev.X(), aPrev.Y(), aPrev.Z(), aCur.X(), aCur.Y(), aCur.Z() });
                aPrev = aCur;
            }
        }
        aPerEdge.push_back(aNb >= 1 ? aNb - 1 : 0);
    }

    const size_t aNbPts = aPts.size() / 3;
    double *anOutPts = new double[aPts.size()];
    std::copy(aPts.begin(), aPts.end(), anOutPts);
    nb::capsule aPtsOwner(anOutPts, [](void *p) noexcept { delete[] static_cast<double *>(p); });

    int32_t *anOutCnt = new int32_t[aPerEdge.size()];
    std::copy(aPerEdge.begin(), aPerEdge.end(), anOutCnt);
    nb::capsule aCntOwner(anOutCnt, [](void *p) noexcept { delete[] static_cast<int32_t *>(p); });

    int32_t *anOutTyp = new int32_t[aTypes.size()];
    std::copy(aTypes.begin(), aTypes.end(), anOutTyp);
    nb::capsule aTypOwner(anOutTyp, [](void *p) noexcept { delete[] static_cast<int32_t *>(p); });

    return nb::make_tuple(
        nb::ndarray<nb::numpy, double, nb::ndim<2>>(anOutPts, { aNbPts, 3 }, aPtsOwner),
        nb::ndarray<nb::numpy, int32_t, nb::ndim<1>>(anOutCnt, { aPerEdge.size() }, aCntOwner),
        nb::ndarray<nb::numpy, int32_t, nb::ndim<1>>(anOutTyp, { aTypes.size() }, aTypOwner));
}

} // namespace

void nanocct_def_Tessellator(nb::module_ &m)
{
    m.def("NormalsFromSurface", &NormalsFromSurface,
          nb::arg("theFace"), nb::arg("theUV"), nb::arg("theReverse") = false,
          "One surface normal per (u, v) row, evaluated in C++.\n\n"
          "theUV is an (N, 2) float64 C-contiguous array and must already be clamped to the face's UV "
          "bounds (BRepTools.UVBounds): a node parked one ULP outside them at a parametric singularity "
          "evaluates to an inward-flipped normal. Returns (N, 3) float64, normalised.");

    m.def("EdgeSegments", &EdgeSegments, nb::arg("theShape"),
          "Every edge's polyline for a whole shape, as consecutive point pairs.\n\n"
          "Returns (segments, segments_per_edge, edge_types): an (2*S, 3) float64 array of endpoints "
          "and two (E,) int32 arrays, the segment count and the GeomAbs_CurveType of each edge that "
          "was kept. Edges with no ancestor face, no triangulation or no polygon on it are skipped, so "
          "all three align. The type is returned here because which edges were skipped is decided "
          "here. Mesh the shape first.");
}
