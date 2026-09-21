"""OCCT package FilletSurf (toolkit TKFillet)"""

import enum
from typing import overload

import nanoocp.ChFi3d
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.NCollection
import nanoocp.TopoDS


class FilletSurf_StatusType(enum.IntEnum):
    FilletSurf_TwoExtremityOnEdge = 0

    FilletSurf_OneExtremityOnEdge = 1

    FilletSurf_NoExtremityOnEdge = 2

FilletSurf_TwoExtremityOnEdge: FilletSurf_StatusType = ...

FilletSurf_OneExtremityOnEdge: FilletSurf_StatusType = ...

FilletSurf_NoExtremityOnEdge: FilletSurf_StatusType = ...

class FilletSurf_StatusDone(enum.IntEnum):
    FilletSurf_IsOk = 0

    FilletSurf_IsNotOk = 1

    FilletSurf_IsPartial = 2

FilletSurf_IsOk: FilletSurf_StatusDone = FilletSurf_StatusDone.FilletSurf_IsOk

FilletSurf_IsNotOk: FilletSurf_StatusDone = FilletSurf_StatusDone.FilletSurf_IsNotOk

FilletSurf_IsPartial: FilletSurf_StatusDone = FilletSurf_StatusDone.FilletSurf_IsPartial

class FilletSurf_ErrorTypeStatus(enum.IntEnum):
    FilletSurf_EmptyList = 0

    FilletSurf_EdgeNotG1 = 1

    FilletSurf_FacesNotG1 = 2

    FilletSurf_EdgeNotOnShape = 3

    FilletSurf_NotSharpEdge = 4

    FilletSurf_PbFilletCompute = 5

FilletSurf_EmptyList: FilletSurf_ErrorTypeStatus = FilletSurf_ErrorTypeStatus.FilletSurf_EmptyList

FilletSurf_EdgeNotG1: FilletSurf_ErrorTypeStatus = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotG1

FilletSurf_FacesNotG1: FilletSurf_ErrorTypeStatus = FilletSurf_ErrorTypeStatus.FilletSurf_FacesNotG1

FilletSurf_EdgeNotOnShape: FilletSurf_ErrorTypeStatus = ...

FilletSurf_NotSharpEdge: FilletSurf_ErrorTypeStatus = ...

FilletSurf_PbFilletCompute: FilletSurf_ErrorTypeStatus = ...

class FilletSurf_InternalBuilder(nanoocp.ChFi3d.ChFi3d_FilBuilder):
    """
    This class is private. It is used by the class Builder
    from FilletSurf. It computes geometric information about fillets.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, FShape: nanoocp.ChFi3d.ChFi3d_FilletShape = ChFi3d_FilletShape.ChFi3d_Polynomial, Ta: float = 0.01, Tapp3d: float = 0.0001, Tapp2d: float = 1e-05) -> None: ...

    @overload
    def __init__(self, theOther: FilletSurf_InternalBuilder) -> None: ...

    def Add(self, E: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], R: float) -> int:
        """
        Initializes the contour with a list of Edges
        0 : no problem
        1 : empty list
        2 : the edges are not G1
        3 : two connected faces on a same support are not G1
        4 : the edge is not on shape
        5 : NotSharpEdge: the edge is not sharp
        """

    def Perform(self) -> None: ...

    def Done(self) -> bool: ...

    def NbSurface(self) -> int:
        """gives the number of NUBS surfaces of the Fillet."""

    def SurfaceFillet(self, Index: int) -> nanoocp.Geom.Geom_Surface:
        """gives the NUBS surface of index Index."""

    def TolApp3d(self, Index: int) -> float:
        """
        gives the 3d tolerance reached during approximation
        of the surface of index Index
        """

    def SupportFace1(self, Index: int) -> nanoocp.TopoDS.TopoDS_Face:
        """gives the first support face relative to SurfaceFillet(Index);"""

    def SupportFace2(self, Index: int) -> nanoocp.TopoDS.TopoDS_Face:
        """gives the second support face relative to SurfaceFillet(Index);"""

    def CurveOnFace1(self, Index: int) -> nanoocp.Geom.Geom_Curve:
        """gives the 3d curve of SurfaceFillet(Index) on SupportFace1(Index)"""

    def CurveOnFace2(self, Index: int) -> nanoocp.Geom.Geom_Curve:
        """gives the 3d curve of SurfaceFillet(Index) on SupportFace2(Index)"""

    def PCurveOnFace1(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurvOnSup1(Index) on the support face"""

    def PCurve1OnFillet(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurveOnFace1(Index) on the Fillet"""

    def PCurveOnFace2(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurveOnSup2(Index) on the support face"""

    def PCurve2OnFillet(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurveOnSup2(Index) on the fillet"""

    def FirstParameter(self) -> float:
        """gives the parameter of the fillet on the first edge."""

    def LastParameter(self) -> float:
        """gives the parameter of the fillet on the last edge"""

    def StartSectionStatus(self) -> FilletSurf_StatusType: ...

    def EndSectionStatus(self) -> FilletSurf_StatusType: ...

    def Simulate(self) -> None: ...

    def NbSection(self, IndexSurf: int) -> int: ...

    def Section(self, IndexSurf: int, IndexSec: int) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the arc of the section of index IndexSec of surface
        of index IndexSurf. The basis curve of the trimmed curve is a Geom_Circle.
        @param[in] IndexSurf 1-based surface index
        @param[in] IndexSec 1-based section index
        @return the section as a trimmed circular arc
        """

    def Section__Geom_TrimmedCurve(self, IndexSurf: int, IndexSec: int) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Section__Geom_TrimmedCurve: the C++ overload Section(const int, const int, occ::handle<Geom_TrimmedCurve> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use Section() returning handle by value instead

        @deprecated Use Section() returning handle by value instead.
        """

class FilletSurf_Builder:
    """
    API giving the following geometric information about fillets
    list of corresponding NUBS surfaces
    for each surface:
    the 2 support faces
    on each face: the 3d curve and the corresponding 2d curve
    the 2d curves on the fillet
    status of start and end section of the fillet
    first and last parameter on edge of the fillet.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, E: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], R: float, Ta: float = 0.01, Tapp3d: float = 0.0001, Tapp2d: float = 1e-05) -> None:
        """
        initialize of the information necessary for the
        computation of the fillet on the
        Shape S from a list of edges E and a radius R.

        Ta is the angular tolerance
        Tapp3d is the 3d approximation tolerance
        Tapp2d is the 2d approximation tolerance
        """

    @overload
    def __init__(self, theOther: FilletSurf_Builder) -> None: ...

    def Perform(self) -> None:
        """---Purpose computation of the fillet (list of NUBS)"""

    def Simulate(self) -> None: ...

    def IsDone(self) -> FilletSurf_StatusDone:
        """
        gives the status about the computation of the fillet
        returns:
        IsOK :no problem during the computation
        IsNotOk: no result is produced
        IsPartial: the result is partial
        """

    def StatusError(self) -> FilletSurf_ErrorTypeStatus:
        """
        gives information about error status if
        IsDone=IsNotOk
        returns
        EdgeNotG1: the edges are not G1
        FacesNotG1 : two connected faces on a same support are
        not G1
        EdgeNotOnShape: the edge is not on shape
        NotSharpEdge: the edge is not sharp
        PbFilletCompute: problem during the computation of the fillet
        """

    def NbSurface(self) -> int:
        """gives the number of NUBS surfaces of the Fillet."""

    def Section(self, IndexSurf: int, IndexSec: int) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Returns the arc of the section of index IndexSec of surface
        of index IndexSurf. The basis curve of the trimmed curve is a Geom_Circle.
        @param[in] IndexSurf 1-based surface index
        @param[in] IndexSec 1-based section index
        @return the section as a trimmed circular arc
        """

    def Section__Geom_TrimmedCurve(self, IndexSurf: int, IndexSec: int) -> nanoocp.Geom.Geom_TrimmedCurve:
        """
        Section__Geom_TrimmedCurve: the C++ overload Section(const int, const int, occ::handle<Geom_TrimmedCurve> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use Section() returning handle by value instead

        @deprecated Use Section() returning handle by value instead.
        """

    def SurfaceFillet(self, Index: int) -> nanoocp.Geom.Geom_Surface:
        """gives the NUBS surface of index Index."""

    def TolApp3d(self, Index: int) -> float:
        """
        gives the 3d tolerance reached during approximation
        of surface of index Index
        """

    def SupportFace1(self, Index: int) -> nanoocp.TopoDS.TopoDS_Face:
        """gives the first support face relative to SurfaceFillet(Index);"""

    def SupportFace2(self, Index: int) -> nanoocp.TopoDS.TopoDS_Face:
        """gives the second support face relative to SurfaceFillet(Index);"""

    def CurveOnFace1(self, Index: int) -> nanoocp.Geom.Geom_Curve:
        """gives the 3d curve of SurfaceFillet(Index) on SupportFace1(Index)"""

    def CurveOnFace2(self, Index: int) -> nanoocp.Geom.Geom_Curve:
        """gives the 3d curve of SurfaceFillet(Index) on SupportFace2(Index)"""

    def PCurveOnFace1(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurvOnSup1(Index) on the support face"""

    def PCurve1OnFillet(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurveOnFace1(Index) on the Fillet"""

    def PCurveOnFace2(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurveOnSup2(Index) on the support face"""

    def PCurve2OnFillet(self, Index: int) -> nanoocp.Geom2d.Geom2d_Curve:
        """gives the PCurve associated to CurveOnSup2(Index) on the fillet"""

    def FirstParameter(self) -> float:
        """gives the parameter of the fillet on the first edge."""

    def LastParameter(self) -> float:
        """gives the parameter of the fillet on the last edge"""

    def StartSectionStatus(self) -> FilletSurf_StatusType: ...

    def EndSectionStatus(self) -> FilletSurf_StatusType: ...

    def NbSection(self, IndexSurf: int) -> int: ...
