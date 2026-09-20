"""OCCT package ElSLib (toolkit TKMath)"""

from typing import overload

import nanoocp.gp


class ElSLib:
    """
    Provides functions for basic geometric computation on
    elementary surfaces.
    This includes:
    -   calculation of a point or derived vector on a surface
    where the surface is provided by the gp package, or
    defined in canonical form (as in the gp package), and
    the point is defined with a parameter,
    -   evaluation of the parameters corresponding to a
    point on an elementary surface from gp,
    -   calculation of isoparametric curves on an elementary
    surface defined in canonical form (as in the gp package).
    Notes:
    -   ElSLib stands for Elementary Surfaces Library.
    -   If the surfaces provided by the gp package are not
    explicitly parameterized, they still have an implicit
    parameterization, similar to that which they infer on
    the equivalent Geom surfaces.
    Note: ElSLib stands for Elementary Surfaces Library.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ElSLib) -> None: ...

    @overload
    @staticmethod
    def Value(U: float, V: float, Pl: nanoocp.gp.gp_Pln) -> nanoocp.gp.gp_Pnt:
        """
        For elementary surfaces from the gp package (planes,
        cones, cylinders, spheres and tori), computes the point
        of parameters (U, V).
        """

    @overload
    @staticmethod
    def Value(U: float, V: float, C: nanoocp.gp.gp_Cone) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, V: float, C: nanoocp.gp.gp_Cylinder) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, V: float, S: nanoocp.gp.gp_Sphere) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, V: float, T: nanoocp.gp.gp_Torus) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def DN(U: float, V: float, Pl: nanoocp.gp.gp_Pln, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        For elementary surfaces from the gp package (planes,
        cones, cylinders, spheres and tori), computes the
        derivative vector of order Nu and Nv in the u and v
        parametric directions respectively, at the point of
        parameters (U, V).
        """

    @overload
    @staticmethod
    def DN(U: float, V: float, C: nanoocp.gp.gp_Cone, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, V: float, C: nanoocp.gp.gp_Cylinder, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, V: float, S: nanoocp.gp.gp_Sphere, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, V: float, T: nanoocp.gp.gp_Torus, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def D0(U: float, V: float, Pl: nanoocp.gp.gp_Pln, P: nanoocp.gp.gp_Pnt) -> None:
        """
        For elementary surfaces from the gp package (planes,
        cones, cylinders, spheres and tori), computes the point P
        of parameters (U, V).inline
        """

    @overload
    @staticmethod
    def D0(U: float, V: float, C: nanoocp.gp.gp_Cone, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, V: float, C: nanoocp.gp.gp_Cylinder, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, V: float, S: nanoocp.gp.gp_Sphere, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def D0(U: float, V: float, T: nanoocp.gp.gp_Torus, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, V: float, Pl: nanoocp.gp.gp_Pln, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None:
        """
        For elementary surfaces from the gp package (planes,
        cones, cylinders, spheres and tori), computes:
        -   the point P of parameters (U, V), and
        -   the first derivative vectors Vu and Vv at this point in
        the u and v parametric directions respectively.
        """

    @overload
    @staticmethod
    def D1(U: float, V: float, C: nanoocp.gp.gp_Cone, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, V: float, C: nanoocp.gp.gp_Cylinder, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, V: float, S: nanoocp.gp.gp_Sphere, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, V: float, T: nanoocp.gp.gp_Torus, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, V: float, C: nanoocp.gp.gp_Cone, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None:
        """
        For elementary surfaces from the gp package (cones,
        cylinders, spheres and tori), computes:
        -   the point P of parameters (U, V), and
        -   the first derivative vectors Vu and Vv at this point in
        the u and v parametric directions respectively, and
        -   the second derivative vectors Vuu, Vvv and Vuv at this point.
        """

    @overload
    @staticmethod
    def D2(U: float, V: float, C: nanoocp.gp.gp_Cylinder, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, V: float, S: nanoocp.gp.gp_Sphere, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, V: float, T: nanoocp.gp.gp_Torus, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, V: float, C: nanoocp.gp.gp_Cone, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None:
        """
        For elementary surfaces from the gp package (cones,
        cylinders, spheres and tori), computes:
        -   the point P of parameters (U,V), and
        -   the first derivative vectors Vu and Vv at this point in
        the u and v parametric directions respectively, and
        -   the second derivative vectors Vuu, Vvv and Vuv at
        this point, and
        -   the third derivative vectors Vuuu, Vvvv, Vuuv and
        Vuvv at this point.
        """

    @overload
    @staticmethod
    def D3(U: float, V: float, C: nanoocp.gp.gp_Cylinder, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, V: float, S: nanoocp.gp.gp_Sphere, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, V: float, T: nanoocp.gp.gp_Torus, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None:
        """
        Surface evaluation
        The following functions compute the point and the
        derivatives on elementary surfaces defined with their
        geometric characteristics.
        You don't need to create the surface to use these functions.
        These functions are called by the previous ones.
        Example:
        A cylinder is defined with its position and its radius.
        """

    @staticmethod
    def PlaneValue(U: float, V: float, Pos: nanoocp.gp.gp_Ax3) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def CylinderValue(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def ConeValue(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def SphereValue(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def TorusValue(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def PlaneDN(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def CylinderDN(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def ConeDN(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def SphereDN(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def TorusDN(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def PlaneD0(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def ConeD0(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def CylinderD0(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def SphereD0(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def TorusD0(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def PlaneD1(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def ConeD1(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def CylinderD1(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def SphereD1(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def TorusD1(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def ConeD2(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def CylinderD2(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def SphereD2(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def TorusD2(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def ConeD3(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def CylinderD3(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def SphereD3(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def TorusD3(U: float, V: float, Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None:
        """
        The following functions compute the parametric values
        corresponding to a given point on a elementary surface.
        The point should be on the surface.
        """

    @overload
    @staticmethod
    def Parameters(Pl: nanoocp.gp.gp_Pln, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) =
        Pl.Location() + U * Pl.XDirection() + V * Pl.YDirection()
        """

    @overload
    @staticmethod
    def Parameters(C: nanoocp.gp.gp_Cylinder, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location + V * ZDirection +
        Radius * (std::cos(U) * XDirection + Sin (U) * YDirection)
        """

    @overload
    @staticmethod
    def Parameters(C: nanoocp.gp.gp_Cone, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location + V * ZDirection +
        (Radius + V * Tan (SemiAngle)) *
        (std::cos(U) * XDirection + std::sin(U) * YDirection)
        """

    @overload
    @staticmethod
    def Parameters(S: nanoocp.gp.gp_Sphere, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location +
        Radius * Cos (V) * (Cos (U) * XDirection + Sin (U) * YDirection) +
        Radius * Sin (V) * ZDirection
        """

    @overload
    @staticmethod
    def Parameters(T: nanoocp.gp.gp_Torus, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location +
        (MajorRadius + MinorRadius * std::cos(U)) *
        (std::cos(V) * XDirection - std::sin(V) * YDirection) +
        MinorRadius * std::sin(U) * ZDirection
        """

    @staticmethod
    def PlaneParameters(Pos: nanoocp.gp.gp_Ax3, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) =
        Pl.Location() + U * Pl.XDirection() + V * Pl.YDirection()
        """

    @staticmethod
    def CylinderParameters(Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location + V * ZDirection +
        Radius * (std::cos(U) * XDirection + Sin (U) * YDirection)
        """

    @staticmethod
    def ConeParameters(Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location + V * ZDirection +
        (Radius + V * Tan (SemiAngle)) *
        (std::cos(U) * XDirection + std::sin(U) * YDirection)
        """

    @staticmethod
    def SphereParameters(Pos: nanoocp.gp.gp_Ax3, Radius: float, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location +
        Radius * Cos (V) * (Cos (U) * XDirection + Sin (U) * YDirection) +
        Radius * Sin (V) * ZDirection
        """

    @staticmethod
    def TorusParameters(Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        parametrization
        P (U, V) = Location +
        (MajorRadius + MinorRadius * std::cos(U)) *
        (std::cos(V) * XDirection - std::sin(V) * YDirection) +
        MinorRadius * std::sin(U) * ZDirection
        """

    @staticmethod
    def PlaneUIso(Pos: nanoocp.gp.gp_Ax3, U: float) -> nanoocp.gp.gp_Lin:
        """compute the U Isoparametric gp_Lin of the plane."""

    @staticmethod
    def CylinderUIso(Pos: nanoocp.gp.gp_Ax3, Radius: float, U: float) -> nanoocp.gp.gp_Lin:
        """compute the U Isoparametric gp_Lin of the cylinder."""

    @staticmethod
    def ConeUIso(Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, U: float) -> nanoocp.gp.gp_Lin:
        """compute the U Isoparametric gp_Lin of the cone."""

    @staticmethod
    def SphereUIso(Pos: nanoocp.gp.gp_Ax3, Radius: float, U: float) -> nanoocp.gp.gp_Circ:
        """
        compute the U Isoparametric gp_Circ of the sphere,
        (the meridian is not trimmed).
        """

    @staticmethod
    def TorusUIso(Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, U: float) -> nanoocp.gp.gp_Circ:
        """compute the U Isoparametric gp_Circ of the torus."""

    @staticmethod
    def PlaneVIso(Pos: nanoocp.gp.gp_Ax3, V: float) -> nanoocp.gp.gp_Lin:
        """compute the V Isoparametric gp_Lin of the plane."""

    @staticmethod
    def CylinderVIso(Pos: nanoocp.gp.gp_Ax3, Radius: float, V: float) -> nanoocp.gp.gp_Circ:
        """compute the V Isoparametric gp_Circ of the cylinder."""

    @staticmethod
    def ConeVIso(Pos: nanoocp.gp.gp_Ax3, Radius: float, SAngle: float, V: float) -> nanoocp.gp.gp_Circ:
        """compute the V Isoparametric gp_Circ of the cone."""

    @staticmethod
    def SphereVIso(Pos: nanoocp.gp.gp_Ax3, Radius: float, V: float) -> nanoocp.gp.gp_Circ:
        """
        compute the V Isoparametric gp_Circ of the sphere,
        (the meridian is not trimmed).
        """

    @staticmethod
    def TorusVIso(Pos: nanoocp.gp.gp_Ax3, MajorRadius: float, MinorRadius: float, V: float) -> nanoocp.gp.gp_Circ:
        """compute the V Isoparametric gp_Circ of the torus."""
