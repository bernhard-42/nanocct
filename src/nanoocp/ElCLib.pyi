"""OCCT package ElCLib (toolkit TKMath)"""

from typing import overload

import nanoocp.gp


class ElCLib:
    """
    Provides functions for basic geometric computations on
    elementary curves such as conics and lines in 2D and 3D space.
    This includes:
    -   calculation of a point or derived vector on a 2D or
    3D curve where:
    -   the curve is provided by the gp package, or
    defined in reference form (as in the gp package),
    and
    -   the point is defined by a parameter,
    -   evaluation of the parameter corresponding to a point
    on a 2D or 3D curve from gp,
    -   various elementary computations which allow you to
    position parameterized values within the period of a curve.
    Notes:
    -   ElCLib stands for Elementary Curves Library.
    -   If the curves provided by the gp package are not
    explicitly parameterized, they still have an implicit
    parameterization, analogous to that which they infer
    for the equivalent Geom or Geom2d curves.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ElCLib) -> None: ...

    @staticmethod
    def InPeriod(U: float, UFirst: float, ULast: float) -> float:
        """
        Return a value in the range <UFirst, ULast> by
        adding or removing the period <ULast - UFirst> to
        <U>.
        ATTENTION!!!
        It is expected but not checked that (ULast > UFirst)
        """

    @staticmethod
    def AdjustPeriodic(UFirst: float, ULast: float, Precision: float) -> tuple[float, float]:
        """
        Adjust U1 and U2 in the parametric range UFirst
        Ulast of a periodic curve, where ULast -
        UFirst is its period. To do this, this function:
        -   sets U1 in the range [ UFirst, ULast ] by
        adding/removing the period to/from the value U1, then
        -   sets U2 in the range [ U1, U1 + period ] by
        adding/removing the period to/from the value U2.
        Precision is used to test the equalities.
        """

    @overload
    @staticmethod
    def Value(U: float, L: nanoocp.gp.gp_Lin) -> nanoocp.gp.gp_Pnt:
        """
        For elementary curves (lines, circles and conics) from
        the gp package, computes the point of parameter U.
        The result is either:
        -   a gp_Pnt point for a curve in 3D space, or
        -   a gp_Pnt2d point for a curve in 2D space.
        """

    @overload
    @staticmethod
    def Value(U: float, C: nanoocp.gp.gp_Circ) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, E: nanoocp.gp.gp_Elips) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, H: nanoocp.gp.gp_Hypr) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, Prb: nanoocp.gp.gp_Parab) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def Value(U: float, L: nanoocp.gp.gp_Lin2d) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Value(U: float, C: nanoocp.gp.gp_Circ2d) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Value(U: float, E: nanoocp.gp.gp_Elips2d) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Value(U: float, H: nanoocp.gp.gp_Hypr2d) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def Value(U: float, Prb: nanoocp.gp.gp_Parab2d) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def D1(U: float, L: nanoocp.gp.gp_Lin, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None:
        """
        For elementary curves (lines, circles and conics) from the
        gp package, computes:
        -   the point P of parameter U, and
        -   the first derivative vector V1 at this point.
        The results P and V1 are either:
        -   a gp_Pnt point and a gp_Vec vector, for a curve in 3D space, or
        -   a gp_Pnt2d point and a gp_Vec2d vector, for a curve in 2D space.
        """

    @overload
    @staticmethod
    def D1(U: float, C: nanoocp.gp.gp_Circ, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, E: nanoocp.gp.gp_Elips, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, H: nanoocp.gp.gp_Hypr, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, Prb: nanoocp.gp.gp_Parab, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, L: nanoocp.gp.gp_Lin2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, C: nanoocp.gp.gp_Circ2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, E: nanoocp.gp.gp_Elips2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, H: nanoocp.gp.gp_Hypr2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D1(U: float, Prb: nanoocp.gp.gp_Parab2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, C: nanoocp.gp.gp_Circ, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        For elementary curves (circles and conics) from the gp
        package, computes:
        - the point P of parameter U, and
        - the first and second derivative vectors V1 and V2 at this point.
        The results, P, V1 and V2, are either:
        -   a gp_Pnt point and two gp_Vec vectors, for a curve in 3D space, or
        -   a gp_Pnt2d point and two gp_Vec2d vectors, for a curve in 2D space.
        """

    @overload
    @staticmethod
    def D2(U: float, E: nanoocp.gp.gp_Elips, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, H: nanoocp.gp.gp_Hypr, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, Prb: nanoocp.gp.gp_Parab, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, C: nanoocp.gp.gp_Circ2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, E: nanoocp.gp.gp_Elips2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, H: nanoocp.gp.gp_Hypr2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D2(U: float, Prb: nanoocp.gp.gp_Parab2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, C: nanoocp.gp.gp_Circ, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None:
        """
        For elementary curves (circles, ellipses and hyperbolae)
        from the gp package, computes:
        -   the point P of parameter U, and
        -   the first, second and third derivative vectors V1, V2
        and V3 at this point.
        The results, P, V1, V2 and V3, are either:
        -   a gp_Pnt point and three gp_Vec vectors, for a curve in 3D space, or
        -   a gp_Pnt2d point and three gp_Vec2d vectors, for a curve in 2D space.
        """

    @overload
    @staticmethod
    def D3(U: float, E: nanoocp.gp.gp_Elips, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, H: nanoocp.gp.gp_Hypr, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, C: nanoocp.gp.gp_Circ2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, E: nanoocp.gp.gp_Elips2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def D3(U: float, H: nanoocp.gp.gp_Hypr2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        In the following functions N is the order of derivation
        and should be greater than 0
        """

    @overload
    @staticmethod
    def DN(U: float, L: nanoocp.gp.gp_Lin, N: int) -> nanoocp.gp.gp_Vec:
        """
        For elementary curves (lines, circles and conics) from
        the gp package, computes the vector corresponding to
        the Nth derivative at the point of parameter U. The result is either:
        -   a gp_Vec vector for a curve in 3D space, or
        -   a gp_Vec2d vector for a curve in 2D space.
        In the following functions N is the order of derivation
        and should be greater than 0
        """

    @overload
    @staticmethod
    def DN(U: float, C: nanoocp.gp.gp_Circ, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, E: nanoocp.gp.gp_Elips, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, H: nanoocp.gp.gp_Hypr, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, Prb: nanoocp.gp.gp_Parab, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def DN(U: float, L: nanoocp.gp.gp_Lin2d, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def DN(U: float, C: nanoocp.gp.gp_Circ2d, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def DN(U: float, E: nanoocp.gp.gp_Elips2d, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def DN(U: float, H: nanoocp.gp.gp_Hypr2d, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def DN(U: float, Prb: nanoocp.gp.gp_Parab2d, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def LineValue(U: float, Pos: nanoocp.gp.gp_Ax1) -> nanoocp.gp.gp_Pnt:
        """
        Curve evaluation
        The following basis functions compute the derivatives on
        elementary curves defined by their geometric characteristics.
        These functions can be called without constructing a conic
        from package gp. They are called by the previous functions.
        Example :
        A circle is defined by its position and its radius.
        """

    @overload
    @staticmethod
    def LineValue(U: float, Pos: nanoocp.gp.gp_Ax2d) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def CircleValue(U: float, Pos: nanoocp.gp.gp_Ax2, Radius: float) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def CircleValue(U: float, Pos: nanoocp.gp.gp_Ax22d, Radius: float) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def EllipseValue(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def EllipseValue(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def HyperbolaValue(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def HyperbolaValue(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def ParabolaValue(U: float, Pos: nanoocp.gp.gp_Ax2, Focal: float) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def ParabolaValue(U: float, Pos: nanoocp.gp.gp_Ax22d, Focal: float) -> nanoocp.gp.gp_Pnt2d: ...

    @overload
    @staticmethod
    def LineD1(U: float, Pos: nanoocp.gp.gp_Ax1, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def LineD1(U: float, Pos: nanoocp.gp.gp_Ax2d, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def CircleD1(U: float, Pos: nanoocp.gp.gp_Ax2, Radius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def CircleD1(U: float, Pos: nanoocp.gp.gp_Ax22d, Radius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def EllipseD1(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def EllipseD1(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def HyperbolaD1(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def HyperbolaD1(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def ParabolaD1(U: float, Pos: nanoocp.gp.gp_Ax2, Focal: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def ParabolaD1(U: float, Pos: nanoocp.gp.gp_Ax22d, Focal: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def CircleD2(U: float, Pos: nanoocp.gp.gp_Ax2, Radius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def CircleD2(U: float, Pos: nanoocp.gp.gp_Ax22d, Radius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def EllipseD2(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def EllipseD2(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def HyperbolaD2(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def HyperbolaD2(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def ParabolaD2(U: float, Pos: nanoocp.gp.gp_Ax2, Focal: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def ParabolaD2(U: float, Pos: nanoocp.gp.gp_Ax22d, Focal: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def CircleD3(U: float, Pos: nanoocp.gp.gp_Ax2, Radius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def CircleD3(U: float, Pos: nanoocp.gp.gp_Ax22d, Radius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def EllipseD3(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def EllipseD3(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    @staticmethod
    def HyperbolaD3(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    @staticmethod
    def HyperbolaD3(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        In the following functions N is the order of derivation
        and should be greater than 0
        """

    @overload
    @staticmethod
    def LineDN(U: float, Pos: nanoocp.gp.gp_Ax1, N: int) -> nanoocp.gp.gp_Vec:
        """
        In the following functions N is the order of derivation
        and should be greater than 0
        """

    @overload
    @staticmethod
    def LineDN(U: float, Pos: nanoocp.gp.gp_Ax2d, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def CircleDN(U: float, Pos: nanoocp.gp.gp_Ax2, Radius: float, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def CircleDN(U: float, Pos: nanoocp.gp.gp_Ax22d, Radius: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def EllipseDN(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def EllipseDN(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def HyperbolaDN(U: float, Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def HyperbolaDN(U: float, Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @overload
    @staticmethod
    def ParabolaDN(U: float, Pos: nanoocp.gp.gp_Ax2, Focal: float, N: int) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def ParabolaDN(U: float, Pos: nanoocp.gp.gp_Ax22d, Focal: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The following functions compute the parametric value corresponding
        to a given point on a elementary curve. The point should be on the
        curve.
        """

    @overload
    @staticmethod
    def Parameter(L: nanoocp.gp.gp_Lin, P: nanoocp.gp.gp_Pnt) -> float:
        """
        Computes the parameter value of the point P on the given curve.
        Note: In its local coordinate system, the parametric
        equation of the curve is given by the following:
        -   for the line L: P(U) = Po + U*Vo
        where Po is the origin and Vo the unit vector of its positioning axis.
        -   for the circle C: X(U) = Radius*std::cos(U), Y(U) = Radius*Sin(U)
        -   for the ellipse E: X(U) = MajorRadius*std::cos(U). Y(U) = MinorRadius*Sin(U)
        -   for the hyperbola H: X(U) = MajorRadius*Ch(U), Y(U) = MinorRadius*Sh(U)
        -   for the parabola Prb:
        X(U) = U**2 / (2*p)
        Y(U) = U
        where p is the distance between the focus and the directrix.
        Warning
        The point P must be on the curve. These functions are
        not protected, however, and if point P is not on the
        curve, an exception may be raised.
        """

    @overload
    @staticmethod
    def Parameter(L: nanoocp.gp.gp_Lin2d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        parametrization
        P (U) = L.Location() + U * L.Direction()
        """

    @overload
    @staticmethod
    def Parameter(C: nanoocp.gp.gp_Circ, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def Parameter(C: nanoocp.gp.gp_Circ2d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        parametrization
        In the local coordinate system of the circle
        X (U) = Radius * Cos (U)
        Y (U) = Radius * Sin (U)
        """

    @overload
    @staticmethod
    def Parameter(E: nanoocp.gp.gp_Elips, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def Parameter(E: nanoocp.gp.gp_Elips2d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        parametrization
        In the local coordinate system of the Ellipse
        X (U) = MajorRadius * Cos (U)
        Y (U) = MinorRadius * Sin (U)
        """

    @overload
    @staticmethod
    def Parameter(H: nanoocp.gp.gp_Hypr, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def Parameter(H: nanoocp.gp.gp_Hypr2d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        parametrization
        In the local coordinate system of the Hyperbola
        X (U) = MajorRadius * Ch (U)
        Y (U) = MinorRadius * Sh (U)
        """

    @overload
    @staticmethod
    def Parameter(Prb: nanoocp.gp.gp_Parab, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def Parameter(Prb: nanoocp.gp.gp_Parab2d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        parametrization
        In the local coordinate system of the parabola
        Y**2 = (2*P) * X where P is the distance between the focus
        and the directrix.
        """

    @overload
    @staticmethod
    def LineParameter(Pos: nanoocp.gp.gp_Ax1, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def LineParameter(Pos: nanoocp.gp.gp_Ax2d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        parametrization
        P (U) = L.Location() + U * L.Direction()
        """

    @overload
    @staticmethod
    def CircleParameter(Pos: nanoocp.gp.gp_Ax2, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def CircleParameter(Pos: nanoocp.gp.gp_Ax22d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Pos is the Axis of the Circle
        parametrization
        In the local coordinate system of the circle
        X (U) = Radius * Cos (U)
        Y (U) = Radius * Sin (U)
        """

    @overload
    @staticmethod
    def EllipseParameter(Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def EllipseParameter(Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Pos is the Axis of the Ellipse
        parametrization
        In the local coordinate system of the Ellipse
        X (U) = MajorRadius * Cos (U)
        Y (U) = MinorRadius * Sin (U)
        """

    @overload
    @staticmethod
    def HyperbolaParameter(Pos: nanoocp.gp.gp_Ax2, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def HyperbolaParameter(Pos: nanoocp.gp.gp_Ax22d, MajorRadius: float, MinorRadius: float, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Pos is the Axis of the Hyperbola
        parametrization
        In the local coordinate system of the Hyperbola
        X (U) = MajorRadius * Ch (U)
        Y (U) = MinorRadius * Sh (U)
        """

    @overload
    @staticmethod
    def ParabolaParameter(Pos: nanoocp.gp.gp_Ax2, P: nanoocp.gp.gp_Pnt) -> float: ...

    @overload
    @staticmethod
    def ParabolaParameter(Pos: nanoocp.gp.gp_Ax22d, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Pos is the mirror axis of the parabola
        parametrization
        In the local coordinate system of the parabola
        Y**2 = (2*P) * X where P is the distance between the focus
        and the directrix.
        The following functions build a 3d curve from a
        2d curve at a given position defined with an Ax2.
        """

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, P: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Pnt: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, V: nanoocp.gp.gp_Vec2d) -> nanoocp.gp.gp_Vec: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, V: nanoocp.gp.gp_Dir2d) -> nanoocp.gp.gp_Dir: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, A: nanoocp.gp.gp_Ax2d) -> nanoocp.gp.gp_Ax1: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, A: nanoocp.gp.gp_Ax22d) -> nanoocp.gp.gp_Ax2: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, L: nanoocp.gp.gp_Lin2d) -> nanoocp.gp.gp_Lin: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, C: nanoocp.gp.gp_Circ2d) -> nanoocp.gp.gp_Circ: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, E: nanoocp.gp.gp_Elips2d) -> nanoocp.gp.gp_Elips: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, H: nanoocp.gp.gp_Hypr2d) -> nanoocp.gp.gp_Hypr: ...

    @overload
    @staticmethod
    def To3d(Pos: nanoocp.gp.gp_Ax2, Prb: nanoocp.gp.gp_Parab2d) -> nanoocp.gp.gp_Parab:
        """
        These functions build a 3D geometric entity from a 2D geometric entity.
        The "X Axis" and the "Y Axis" of the global coordinate
        system (i.e. 2D space) are lined up respectively with the
        "X Axis" and "Y Axis" of the 3D coordinate system, Pos.
        """
