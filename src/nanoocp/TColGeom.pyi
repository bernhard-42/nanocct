"""TColGeom: OCCT pre-8.0 typedef names."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Geom
TColGeom_Array1OfBSplineCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve]
TColGeom_Array1OfBezierCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BezierCurve]
TColGeom_Array1OfCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Curve]
TColGeom_Array1OfSurface = nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_Surface]
TColGeom_Array2OfBezierSurface = nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_BezierSurface]
TColGeom_Array2OfSurface = nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_Surface]
TColGeom_HArray1OfBSplineCurve = nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve]
TColGeom_HArray1OfCurve = nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_Curve]
TColGeom_HArray2OfSurface = nanoocp.NCollection.NCollection_HArray2[nanoocp.Geom.Geom_Surface]
TColGeom_HSequenceOfBoundedCurve = nanoocp.NCollection.NCollection_HSequence[nanoocp.Geom.Geom_BoundedCurve]
TColGeom_SequenceOfBoundedCurve = nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_BoundedCurve]
TColGeom_SequenceOfCurve = nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]
