// nanocct.AddOns.ShapeClean -- a workaround for an OCCT bug, not an addition. It is removed again once OCCT is fixed.
//
// The bug (OCCT issue #1541, open, unfixed on master 3d097a0328). ShapeUpgrade_UnifySameDomain::UnionPCurves hands
// the pcurves of a circle's arcs, in chain order, to Geom2dConvert::ConcatC1, which joins them with
// Geom2dConvert_CompCurveToBSplineCurve::Add at its default After = false (Geom2dConvert.cxx:1444; the 3D twin in
// GeomConvert.cxx:1298 passes true). When the pieces close a loop in 2D, both ends of the last piece match and the
// tie-break for After = false *prepends* it: the pcurve is the right loop but starts at the wrong junction, offset
// from the 3D circle by the first arc's angle. Same-parameter checking inflates the edge tolerance to match (0.6 on
// a unit box), and ShapeFix_Wire::FixDegenerated then swaps the edge in the spherical face for a degenerated one.
// build123d runs UnifySameDomain after every boolean, so a sphere cut from a box whose centre lies outside the box
// breaks in 53 of 300 random orientations (2026-09-27): the seam splits the full cut circle into two arcs.
//
// The workaround handles exactly that case -- a full circle made of >= 2 arcs with a non-line pcurve on a non-planar
// face -- and leaves everything else to OCCT:
//   1. unify the faces alone. Only then is it known which circles the edge pass would close: before, the arcs'
//      junctions still touch the edges that divide the faces being merged (measured: 0 vertices found on the raw
//      cut, 2 after this pass). OCCT's own Build() runs faces then edges too (ShapeUpgrade_UnifySameDomain.cxx:4517).
//   2. find those circles and keep enough of their junction vertices that no closed pcurve loop is concatenated,
//   3. unify the edges with those vertices kept,
//   4. merge each protected circle into one closed edge, concatenating its pcurves with After = true,
//   5. compose the three histories.
//
// Removal: the class carries OCCT's name and the members build123d uses, with OCCT's signatures, so reverting is
// changing the import back to nanocct.ShapeUpgrade. tests/test_AddOns.py holds the canary that fails once OCCT
// produces a valid shape on the reproducer -- that is the signal to delete this file (Binding-Rules.md R-ADDON).
#include "nanocct_common.h"

#include <BRepAdaptor_Curve.hxx>
#include <BRepAdaptor_Curve2d.hxx>
#include <BRepAdaptor_Surface.hxx>
#include <BRepCheck_Analyzer.hxx>
#include <BRepLib.hxx>
#include <BRepTools_History.hxx>
#include <BRepTools_ReShape.hxx>
#include <BRep_Builder.hxx>
#include <BRep_Tool.hxx>
#include <BSplCLib.hxx>
#include <Geom2dAdaptor_Curve.hxx>
#include <Geom2dConvert.hxx>
#include <Geom2dConvert_CompCurveToBSplineCurve.hxx>
#include <Geom2d_BSplineCurve.hxx>
#include <Geom2d_TrimmedCurve.hxx>
#include <Geom_Circle.hxx>
#include <Geom_Surface.hxx>
#include <GeomAbs_CurveType.hxx>
#include <GeomAbs_SurfaceType.hxx>
#include <NCollection_IndexedDataMap.hxx>
#include <NCollection_IndexedMap.hxx>
#include <NCollection_List.hxx>
#include <NCollection_Map.hxx>
#include <ShapeUpgrade_UnifySameDomain.hxx>
#include <TopAbs_ShapeEnum.hxx>
#include <TopExp.hxx>
#include <TopTools_ShapeMapHasher.hxx>
#include <TopoDS.hxx>
#include <TopoDS_Edge.hxx>
#include <TopoDS_Face.hxx>
#include <TopoDS_Shape.hxx>
#include <TopoDS_Vertex.hxx>
#include <gp_Ax2.hxx>
#include <gp_Circ.hxx>
#include <gp_Dir.hxx>
#include <gp_Vec.hxx>
#include <gp_Vec2d.hxx>

#include <cmath>
#include <optional>
#include <vector>

namespace nb = nanobind;

namespace nanocct_addons {

using ShapeMap        = NCollection_Map<TopoDS_Shape, TopTools_ShapeMapHasher>;
using IndexedShapeMap = NCollection_IndexedMap<TopoDS_Shape, TopTools_ShapeMapHasher>;
using AncestorMap     = NCollection_IndexedDataMap<TopoDS_Shape, NCollection_List<TopoDS_Shape>, TopTools_ShapeMapHasher>;

// Arcs belong to the same circle when centre, axis and radius agree within this. It is coarser than the
// Precision::Confusion() UnifySameDomain itself merges circles by, so every chain it would close is found.
constexpr double THE_CIRCLE_TOL = 1.0e-5;
constexpr double THE_TWO_PI     = 6.283185307179586476925286766559;   // not M_PI: MSVC needs _USE_MATH_DEFINES

//! A full circle present as >= 2 arcs. `free` are the junction vertices with exactly two edges -- the ones
//! UnifySameDomain chains through; `blocked` counts the others. It closes the circle into ONE edge iff blocked <= 1.
struct CircleCycle
{
    std::vector<TopoDS_Edge>   edges;
    std::vector<TopoDS_Vertex> free;
    int                        blocked = 0;
};

//! Every full circle in theShape that is present as >= 2 arcs.
//!
//! Arcs are grouped by comparing against each group's first arc, not by rounding to a grid as the Python
//! original did: a grid splits a circle whose centre or radius straddles a cell boundary into two groups, and
//! neither group then sums to a full turn.
std::vector<CircleCycle> CircleCycles(const TopoDS_Shape &theShape, const AncestorMap &theEdgeFaces)
{
    AncestorMap aVertexEdges;
    TopExp::MapShapesAndUniqueAncestors(theShape, TopAbs_VERTEX, TopAbs_EDGE, aVertexEdges);

    struct Group
    {
        gp_Circ                  circ;
        std::vector<TopoDS_Edge> edges;
    };
    std::vector<Group> aGroups;
    for (int i = 1; i <= theEdgeFaces.Extent(); ++i)
    {
        const TopoDS_Edge &anEdge = TopoDS::Edge(theEdgeFaces.FindKey(i));
        if (BRep_Tool::Degenerated(anEdge))
            continue;
        BRepAdaptor_Curve aCurve(anEdge);
        if (aCurve.GetType() != GeomAbs_Circle)
            continue;
        const gp_Circ aCirc = aCurve.Circle();
        Group        *aGroup = nullptr;
        for (Group &g : aGroups)
        {
            if (g.circ.Location().Distance(aCirc.Location()) <= THE_CIRCLE_TOL
                && std::abs(g.circ.Radius() - aCirc.Radius()) <= THE_CIRCLE_TOL
                && g.circ.Axis().Direction().IsParallel(aCirc.Axis().Direction(), THE_CIRCLE_TOL))
            {
                aGroup = &g;
                break;
            }
        }
        if (aGroup == nullptr)
        {
            aGroups.push_back({ aCirc, {} });
            aGroup = &aGroups.back();
        }
        aGroup->edges.push_back(anEdge);
    }

    std::vector<CircleCycle> aCycles;
    for (const Group &g : aGroups)
    {
        if (g.edges.size() < 2)
            continue;
        double aSweep = 0.0;
        for (const TopoDS_Edge &e : g.edges)
        {
            BRepAdaptor_Curve aCurve(e);
            aSweep += std::abs(aCurve.LastParameter() - aCurve.FirstParameter());
        }
        if (std::abs(aSweep - THE_TWO_PI) > 1.0e-6)
            continue;
        IndexedShapeMap aVertices;
        for (const TopoDS_Edge &e : g.edges)
        {
            aVertices.Add(TopExp::FirstVertex(e));
            aVertices.Add(TopExp::LastVertex(e));
        }
        CircleCycle aCycle;
        aCycle.edges = g.edges;
        for (int i = 1; i <= aVertices.Extent(); ++i)
        {
            if (aVertexEdges.FindFromKey(aVertices.FindKey(i)).Size() == 2)
                aCycle.free.push_back(TopoDS::Vertex(aVertices.FindKey(i)));
        }
        aCycle.blocked = aVertices.Extent() - static_cast<int>(aCycle.free.size());
        aCycles.push_back(std::move(aCycle));
    }
    return aCycles;
}

//! True when merging these arcs would concatenate non-line pcurves on a non-planar face, i.e. take the
//! Geom2dConvert::ConcatC1 path. UnionPCurves skips planes the same way.
bool IsHazard(const std::vector<TopoDS_Edge> &theEdges, const AncestorMap &theEdgeFaces)
{
    for (const TopoDS_Edge &anEdge : theEdges)
    {
        for (const TopoDS_Shape &aShape : theEdgeFaces.FindFromKey(anEdge))
        {
            const TopoDS_Face &aFace = TopoDS::Face(aShape);
            if (BRepAdaptor_Surface(aFace, false).GetType() == GeomAbs_Plane)
                continue;
            double aFirst = 0.0, aLast = 0.0;
            const occ::handle<Geom2d_Curve> aPCurve = BRep_Tool::CurveOnSurface(anEdge, aFace, aFirst, aLast);
            if (aPCurve.IsNull())
                continue;
            if (Geom2dAdaptor_Curve(aPCurve).GetType() != GeomAbs_Line)
                return true;
        }
    }
    return false;
}

//! The arcs ordered head to tail starting at theStart: (edge, traversed along its parameter). Empty when the arcs
//! are not one simple cycle.
std::vector<std::pair<TopoDS_Edge, bool>> Chain(const std::vector<TopoDS_Edge> &theEdges, const TopoDS_Vertex &theStart)
{
    AncestorMap aVertexEdges;       // only the cycle's own arcs
    for (const TopoDS_Edge &e : theEdges)
    {
        for (const TopoDS_Vertex &v : { TopExp::FirstVertex(e), TopExp::LastVertex(e) })
        {
            if (!aVertexEdges.Contains(v))
                aVertexEdges.Add(v, NCollection_List<TopoDS_Shape>());
            aVertexEdges.ChangeFromKey(v).Append(e);
        }
    }
    for (int i = 1; i <= aVertexEdges.Extent(); ++i)
    {
        if (aVertexEdges(i).Size() != 2)
            return {};
    }
    if (!aVertexEdges.Contains(theStart))
        return {};

    std::vector<std::pair<TopoDS_Edge, bool>> aChain;
    ShapeMap      aUsed;
    TopoDS_Vertex aVertex = theStart;
    do
    {
        TopoDS_Edge aNext;
        int         aCount = 0;
        for (const TopoDS_Shape &e : aVertexEdges.FindFromKey(aVertex))
        {
            if (!aUsed.Contains(e))
            {
                aNext = TopoDS::Edge(e);
                ++aCount;
            }
        }
        // leaving the start both ways is a choice, not an ambiguity: take the first arc
        if (aCount == 0 || (aCount != 1 && !aChain.empty()))
            return {};
        const bool isForward = TopExp::FirstVertex(aNext).IsSame(aVertex);
        aChain.emplace_back(aNext, isForward);
        aUsed.Add(aNext);
        aVertex = isForward ? TopExp::LastVertex(aNext) : TopExp::FirstVertex(aNext);
    } while (!aVertex.IsSame(theStart));
    if (aChain.size() != theEdges.size())
        return {};
    return aChain;
}

struct MergedCircle
{
    TopoDS_Edge                               edge;
    TopoDS_Vertex                             closure;
    std::vector<std::pair<TopoDS_Edge, bool>> chain;
};

//! One closed circle edge replacing the arcs, its pcurves concatenated with After = true -- what
//! Geom2dConvert::ConcatC1 would produce without the defect. Empty when the arcs cannot be merged safely; the
//! circle then stays split, which is valid.
std::optional<MergedCircle> MergeCircle(const CircleCycle &theCycle, const AncestorMap &theEdgeFaces)
{
    IndexedShapeMap aFaces;
    for (const TopoDS_Edge &e : theCycle.edges)
    {
        for (const TopoDS_Shape &f : theEdgeFaces.FindFromKey(e))
        {
            aFaces.Add(f);
            if (BRep_Tool::IsClosed(e, TopoDS::Face(f)))
                return std::nullopt;                                  // a seam edge
        }
    }
    for (const TopoDS_Edge &e : theCycle.edges)                        // every arc borders the same faces
    {
        if (theEdgeFaces.FindFromKey(e).Size() != aFaces.Extent())
            return std::nullopt;
    }

    // the closure vertex is the one other edges end at (a blocked one), if any
    TopoDS_Vertex aStart = TopExp::FirstVertex(theCycle.edges.front());
    for (const TopoDS_Edge &e : theCycle.edges)
    {
        for (const TopoDS_Vertex &v : { TopExp::FirstVertex(e), TopExp::LastVertex(e) })
        {
            bool isFree = false;
            for (const TopoDS_Vertex &f : theCycle.free)
                isFree = isFree || v.IsSame(f);
            if (!isFree)
                aStart = v;
        }
    }
    MergedCircle aResult;
    aResult.closure = aStart;
    aResult.chain   = Chain(theCycle.edges, aStart);
    if (aResult.chain.empty())
        return std::nullopt;

    double aTol = 0.0;                              // the merged edge cannot be more precise than its arcs
    for (const TopoDS_Edge &e : theCycle.edges)
        aTol = std::max(aTol, BRep_Tool::Tolerance(e));

    // 3D circle: parameter 0 at the closure vertex, increasing along the chain
    const auto &[aFirstEdge, isFirstForward] = aResult.chain.front();
    const gp_Circ aCirc   = BRepAdaptor_Curve(aFirstEdge).Circle();
    gp_Dir        aNormal = aCirc.Axis().Direction();
    if (!isFirstForward)
        aNormal.Reverse();
    const gp_Dir aXDir(gp_Vec(aCirc.Location(), BRep_Tool::Pnt(aStart)));
    occ::handle<Geom_Circle> aCircle = new Geom_Circle(gp_Circ(gp_Ax2(aCirc.Location(), aNormal, aXDir), aCirc.Radius()));

    BRep_Builder aBuilder;
    TopoDS_Edge  anEdge;
    aBuilder.MakeEdge(anEdge, aCircle, aTol);      // range [0, 2pi]
    aBuilder.Add(anEdge, aStart.Oriented(TopAbs_FORWARD));
    aBuilder.Add(anEdge, aStart.Oriented(TopAbs_REVERSED));

    for (int i = 1; i <= aFaces.Extent(); ++i)
    {
        const TopoDS_Face &aFace = TopoDS::Face(aFaces.FindKey(i));
        if (BRepAdaptor_Surface(aFace, false).GetType() == GeomAbs_Plane)
            continue;
        const occ::handle<Geom_Surface> aSurf = BRep_Tool::Surface(aFace);
        std::vector<gp_Vec2d>           aPeriods;
        if (aSurf->IsUPeriodic())
            aPeriods.insert(aPeriods.end(), { gp_Vec2d(aSurf->UPeriod(), 0.0), gp_Vec2d(-aSurf->UPeriod(), 0.0) });
        if (aSurf->IsVPeriodic())
            aPeriods.insert(aPeriods.end(), { gp_Vec2d(0.0, aSurf->VPeriod()), gp_Vec2d(0.0, -aSurf->VPeriod()) });
        const auto joins = [](const gp_Pnt2d &a, const gp_Pnt2d &b) { return a.Distance(b) < 1.0e-6; };

        std::optional<Geom2dConvert_CompCurveToBSplineCurve> aComp;
        gp_Pnt2d                                             anEnd;
        for (const auto &[e, isForward] : aResult.chain)
        {
            BRepAdaptor_Curve2d              anAdaptor(e, aFace);
            occ::handle<Geom2d_TrimmedCurve> aPiece =
                new Geom2d_TrimmedCurve(anAdaptor.Curve(), anAdaptor.FirstParameter(), anAdaptor.LastParameter());
            if (!isForward)
                aPiece->Reverse();
            occ::handle<Geom2d_BSplineCurve> aBSpline = Geom2dConvert::CurveToBSplineCurve(aPiece);
            if (!aComp.has_value())
            {
                aComp.emplace(aBSpline);
                anEnd = aBSpline->EndPoint();
                continue;
            }
            // the piece continues where the previous one ended; on a periodic surface it may sit one period away
            // (its arc was parametrised across the seam)
            if (!joins(anEnd, aBSpline->StartPoint()))
            {
                bool isShifted = false;
                for (const gp_Vec2d &aShift : aPeriods)
                {
                    if (joins(anEnd, aBSpline->StartPoint().Translated(aShift)))
                    {
                        aBSpline->Translate(aShift);
                        isShifted = true;
                        break;
                    }
                }
                if (!isShifted)
                    return std::nullopt;
            }
            if (!aComp->Add(aBSpline, aTol, true))     // After = true: append, never prepend -- the whole fix
                return std::nullopt;
            anEnd = aBSpline->EndPoint();
        }
        occ::handle<Geom2d_BSplineCurve> aPCurve = aComp->BSplineCurve();
        // same-parameter with the 3D circle: the pieces carry their arcs' parameter lengths, so a linear remap
        // of the knots onto [0, 2pi] lines them up (BRepLib::SameParameter below checks it)
        NCollection_Array1<double> aKnots(aPCurve->Knots());
        BSplCLib::Reparametrize(0.0, THE_TWO_PI, aKnots);
        aPCurve->SetKnots(aKnots);
        // the loop must close in 2D, exactly or up to one period of the surface
        const gp_Vec2d aGap(aPCurve->EndPoint(), aPCurve->StartPoint());
        bool isClosed = aGap.Magnitude() <= 1.0e-6;
        for (const gp_Vec2d &aPeriod : aPeriods)
            isClosed = isClosed || aGap.Added(aPeriod).Magnitude() < 1.0e-6;
        if (!isClosed)
            return std::nullopt;
        aBuilder.UpdateEdge(anEdge, aPCurve, aFace, aTol);
    }
    // MakeEdge flags the edge SameParameter, which makes BRepLib::SameParameter a no-op; clear the flags so it
    // really measures the pcurves against the 3D circle
    aBuilder.SameRange(anEdge, false);
    aBuilder.SameParameter(anEdge, false);
    BRepLib::SameParameter(anEdge, aTol);
    if (BRep_Tool::Tolerance(anEdge) > std::max(1.0e-5, 10.0 * aTol))
        return std::nullopt;                        // the pcurve does not follow the 3D circle closely enough
    aResult.edge = anEdge;
    return aResult;
}

//! ShapeUpgrade_UnifySameDomain with the closed-circle pcurve defect worked around. Same name and, for the
//! members it has, the same signatures as OCCT's class, so that switching back is changing the import.
class ShapeUpgrade_UnifySameDomain
{
public:
    ShapeUpgrade_UnifySameDomain(const TopoDS_Shape &aShape, bool UnifyEdges, bool UnifyFaces, bool ConcatBSplines)
        : myInitShape(aShape), myUnifyEdges(UnifyEdges), myUnifyFaces(UnifyFaces), myConcatBSplines(ConcatBSplines),
          myHistory(new BRepTools_History())
    {
    }

    void AllowInternalEdges(bool theValue) { myAllowInternal = theValue; }

    void Build()
    {
        myHistory = new BRepTools_History();
        TopoDS_Shape aShape = myInitShape;
        if (myUnifyFaces)
            aShape = Run(aShape, false, true, ShapeMap());
        if (myUnifyEdges)
        {
            ShapeMap aKept;
            AncestorMap anEdgeFaces;
            TopExp::MapShapesAndAncestors(aShape, TopAbs_EDGE, TopAbs_FACE, anEdgeFaces);
            for (const CircleCycle &aCycle : CircleCycles(aShape, anEdgeFaces))
            {
                // >= 2 blocked vertices already split the circle into open chains, nothing closes
                if (aCycle.blocked >= 2 || static_cast<int>(aCycle.free.size()) < 2 - aCycle.blocked
                    || !IsHazard(aCycle.edges, anEdgeFaces))
                    continue;
                for (int i = 0; i < 2 - aCycle.blocked; ++i)
                    aKept.Add(aCycle.free[i]);
            }
            aShape = Run(aShape, true, false, aKept);
            if (!aKept.IsEmpty())
                aShape = MergeCircles(aShape, aKept);
        }
        myShape = aShape;
    }

    const TopoDS_Shape &Shape() const { return myShape; }

    occ::handle<BRepTools_History> &History() { return myHistory; }

private:
    TopoDS_Shape Run(const TopoDS_Shape &theShape, bool theEdges, bool theFaces, const ShapeMap &theKeep)
    {
        ::ShapeUpgrade_UnifySameDomain aUnifier(theShape, theEdges, theFaces, myConcatBSplines);
        aUnifier.AllowInternalEdges(myAllowInternal);
        if (!theKeep.IsEmpty())
            aUnifier.KeepShapes(theKeep);
        aUnifier.Build();
        myHistory->Merge(aUnifier.History());
        return aUnifier.Shape();
    }

    //! Merge the circles that were protected from UnifySameDomain -- only those: a circle the edge pass left split
    //! for a reason of its own stays split.
    TopoDS_Shape MergeCircles(const TopoDS_Shape &theShape, const ShapeMap &theKept)
    {
        AncestorMap anEdgeFaces;
        TopExp::MapShapesAndAncestors(theShape, TopAbs_EDGE, TopAbs_FACE, anEdgeFaces);
        occ::handle<BRepTools_ReShape> aReShape = new BRepTools_ReShape();
        BRepTools_History              aHistory;
        int                            aNbMerged = 0;
        for (const CircleCycle &aCycle : CircleCycles(theShape, anEdgeFaces))
        {
            bool isProtected = false;
            for (const TopoDS_Vertex &v : aCycle.free)
                isProtected = isProtected || theKept.Contains(v);
            if (!isProtected || aCycle.blocked >= 2)
                continue;
            std::optional<MergedCircle> aMerged;
            try
            {
                aMerged = MergeCircle(aCycle, anEdgeFaces);
            }
            catch (const Standard_Failure &)
            {
                // an OCCT failure while building the replacement leaves this circle split, which is valid
            }
            if (!aMerged.has_value())
                continue;
            for (const auto &[e, isForward] : aMerged->chain)
                aHistory.AddModified(e, aMerged->edge);
            const auto &[aFirst, isFirstForward] = aMerged->chain.front();
            aReShape->Replace(aFirst.Oriented(TopAbs_FORWARD),
                              isFirstForward ? TopoDS_Shape(aMerged->edge) : aMerged->edge.Reversed());
            for (size_t i = 1; i < aMerged->chain.size(); ++i)
                aReShape->Remove(aMerged->chain[i].first.Oriented(TopAbs_FORWARD));
            for (const TopoDS_Vertex &v : aCycle.free)
            {
                if (!v.IsSame(aMerged->closure))
                    aHistory.Remove(v);
            }
            ++aNbMerged;
        }
        if (aNbMerged == 0)
            return theShape;
        const TopoDS_Shape aNewShape = aReShape->Apply(theShape);
        if (!BRepCheck_Analyzer(aNewShape).IsValid())
            return theShape;                        // keep the arcs: split but valid
        // the faces and solids containing a merged edge were rebuilt by the ReShape
        for (const TopAbs_ShapeEnum aKind : { TopAbs_FACE, TopAbs_SOLID })
        {
            IndexedShapeMap aSubShapes;
            TopExp::MapShapes(theShape, aKind, aSubShapes);
            for (int i = 1; i <= aSubShapes.Extent(); ++i)
            {
                const TopoDS_Shape &anOld = aSubShapes.FindKey(i);
                const TopoDS_Shape  aNew  = aReShape->Apply(anOld);
                if (!aNew.IsNull() && !aNew.IsSame(anOld))
                    aHistory.AddModified(anOld, aNew);
            }
        }
        myHistory->Merge(aHistory);
        return aNewShape;
    }

    TopoDS_Shape                   myInitShape;
    TopoDS_Shape                   myShape;
    bool                           myUnifyEdges;
    bool                           myUnifyFaces;
    bool                           myConcatBSplines;
    bool                           myAllowInternal = false;
    occ::handle<BRepTools_History> myHistory;
};

} // namespace nanocct_addons

void nanocct_def_ShapeClean(nb::module_ &m)
{
    using Cls = nanocct_addons::ShapeUpgrade_UnifySameDomain;
    // Signatures, defaults and docstrings as nanocct.ShapeUpgrade.ShapeUpgrade_UnifySameDomain binds them.
    nb::class_<Cls>(m, "ShapeUpgrade_UnifySameDomain",
                    "ShapeUpgrade_UnifySameDomain with OCCT issue #1541 worked around: a full circle made of two or "
                    "more arcs on a non-planar face is merged with correctly concatenated pcurves instead of an "
                    "invalid, tolerance-inflated edge. Everything else is OCCT's own ShapeUpgrade_UnifySameDomain, "
                    "run as a face pass followed by an edge pass. Remove once OCCT is fixed.")
        .def(nb::init<const TopoDS_Shape &, bool, bool, bool>(), nb::arg("aShape"), nb::arg("UnifyEdges") = true,
             nb::arg("UnifyFaces") = true, nb::arg("ConcatBSplines") = false,
             "Constructor defining input shape and necessary flags.\nIt does not perform unification.")
        .def("AllowInternalEdges", &Cls::AllowInternalEdges, nb::arg("theValue"),
             "Sets the flag defining whether it is allowed to create\ninternal edges inside merged faces in the case "
             "of non-manifold\ntopology. Without this flag merging through multi connected edge\nis forbidden. "
             "Default value is false.")
        .def("Build", &Cls::Build, "Performs unification and builds the resulting shape.")
        .def("Shape", &Cls::Shape, "Gives the resulting shape")
        .def("History", &Cls::History, nb::rv_policy::reference_internal, "Returns the history of the processed shapes.");
}
