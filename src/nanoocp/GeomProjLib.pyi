"""OCCT package GeomProjLib (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.gp


class GeomProjLib:
    """Projection of a curve on a surface."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomProjLib) -> None: ...

    @overload
    @staticmethod
    def Curve2d(C: nanoocp.Geom.Geom_Curve | None, First: float, Last: float, S: nanoocp.Geom.Geom_Surface | None, UFirst: float, ULast: float, VFirst: float, VLast: float) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        gives the 2d-curve of a 3d-curve lying on a
        surface (uses GeomProjLib_ProjectedCurve)
        The 3dCurve is taken between the parametrization
        range [First, Last]
        <Tolerance> is used as input if the projection needs
        an approximation. In this case, the reached
        tolerance is set in <Tolerance> as output.
        WARNING: if the projection has failed, this
        method returns a null Handle.
        """

    @overload
    @staticmethod
    def Curve2d(C: nanoocp.Geom.Geom_Curve | None, First: float, Last: float, S: nanoocp.Geom.Geom_Surface | None) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        gives the 2d-curve of a 3d-curve lying on a
        surface (uses GeomProjLib_ProjectedCurve)
        The 3dCurve is taken between the parametrization
        range [First, Last]
        If the projection needs an approximation,
        Precision::PApproximation() is used.
        WARNING: if the projection has failed, this
        method returns a null Handle.
        """

    @overload
    @staticmethod
    def Curve2d(C: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        gives the 2d-curve of a 3d-curve lying on a
        surface (uses GeomProjLib_ProjectedCurve)
        If the projection needs an approximation,
        Precision::PApproximation() is used.
        WARNING: if the projection has failed, this
        method returns a null Handle.
        """

    @overload
    @staticmethod
    def Curve2d(C: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None, UDeb: float, UFin: float, VDeb: float, VFin: float) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        gives the 2d-curve of a 3d-curve lying on a
        surface (uses GeomProjLib_ProjectedCurve)
        If the projection needs an approximation,
        Precision::PApproximation() is used.
        WARNING: if the projection has failed, this
        method returns a null Handle.
        can expand a little the bounds of surface
        """

    @overload
    @staticmethod
    def Curve2d__float(C: nanoocp.Geom.Geom_Curve | None, First: float, Last: float, S: nanoocp.Geom.Geom_Surface | None) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Curve2d__float: the C++ overload Curve2d(const occ::handle<Geom_Curve> &, const double, const double, const occ::handle<Geom_Surface> &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        gives the 2d-curve of a 3d-curve lying on a
        surface (uses GeomProjLib_ProjectedCurve)
        The 3dCurve is taken between the parametrization
        range [First, Last]
        <Tolerance> is used as input if the projection needs
        an approximation. In this case, the reached
        tolerance is set in <Tolerance> as output.
        WARNING: if the projection has failed, this
        method returns a null Handle.
        """

    @overload
    @staticmethod
    def Curve2d__float(C: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None, UDeb: float, UFin: float, VDeb: float, VFin: float) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Curve2d__float: the C++ overload Curve2d(const occ::handle<Geom_Curve> &, const occ::handle<Geom_Surface> &, const double, const double, const double, const double, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        gives the 2d-curve of a 3d-curve lying on a
        surface (uses GeomProjLib_ProjectedCurve)
        If the projection needs an approximation,
        Precision::PApproximation() is used.
        WARNING: if the projection has failed, this
        method returns a null Handle.
        can expand a little the bounds of surface
        """

    @staticmethod
    def Project(C: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> nanoocp.Geom.Geom_Curve:
        """
        Constructs the 3d-curve from the normal
        projection of the Curve <C> on the surface <S>.
        WARNING: if the projection has failed, returns a
        null Handle.
        """

    @staticmethod
    def ProjectOnPlane(Curve: nanoocp.Geom.Geom_Curve | None, Plane: nanoocp.Geom.Geom_Plane | None, Dir: nanoocp.gp.gp_Dir, KeepParametrization: bool) -> nanoocp.Geom.Geom_Curve:
        """
        Constructs the 3d-curves from the projection
        of the curve <Curve> on the plane <Plane> along
        the direction <Dir>.
        If <KeepParametrization> is true, the parametrization
        of the Projected Curve <PC> will be the same as the
        parametrization of the initial curve <C>.
        It means: proj(C(u)) = PC(u) for each u.
        Otherwise, the parametrization may change.
        """
