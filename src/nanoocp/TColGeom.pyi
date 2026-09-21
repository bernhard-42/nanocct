"""TColGeom: OCCT pre-8.0 typedef names."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Geom
TColGeom_Array1OfBSplineCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve]
TColGeom_Array1OfBezierCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BezierCurve]
TColGeom_Array1OfCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve]
TColGeom_Array2OfBezierSurface = nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_BezierSurface]
TColGeom_HArray1OfBSplineCurve = nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve]
TColGeom_SequenceOfCurve = nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]
