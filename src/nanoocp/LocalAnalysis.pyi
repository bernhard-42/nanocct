"""OCCT package LocalAnalysis (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomLProp


class LocalAnalysis_StatusErrorType(enum.IntEnum):
    LocalAnalysis_NullFirstDerivative = 0

    LocalAnalysis_NullSecondDerivative = 1

    LocalAnalysis_TangentNotDefined = 2

    LocalAnalysis_NormalNotDefined = 3

    LocalAnalysis_CurvatureNotDefined = 4

LocalAnalysis_NullFirstDerivative: LocalAnalysis_StatusErrorType = ...

LocalAnalysis_NullSecondDerivative: LocalAnalysis_StatusErrorType = ...

LocalAnalysis_TangentNotDefined: LocalAnalysis_StatusErrorType = ...

LocalAnalysis_NormalNotDefined: LocalAnalysis_StatusErrorType = ...

LocalAnalysis_CurvatureNotDefined: LocalAnalysis_StatusErrorType = ...

class LocalAnalysis:
    """
    This package gives tools to check the local continuity
    between two points situated on two curves or two surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LocalAnalysis) -> None: ...

    @overload
    @staticmethod
    def Dump(surfconti: LocalAnalysis_SurfaceContinuity) -> str:
        """
        This class computes and gives tools to check the local
        continuity between two points situated on 2 curves.

        This function gives information about a variable CurveContinuity
        """

    @overload
    @staticmethod
    def Dump(curvconti: LocalAnalysis_CurveContinuity) -> str:
        """This function gives information about a variable SurfaceContinuity"""

class LocalAnalysis_CurveContinuity:
    """
    This class gives tools to check local continuity C0
    C1 C2 G1 G2 between two points situated on two curves
    """

    @overload
    def __init__(self, Curv1: nanoocp.Geom.Geom_Curve | None, u1: float, Curv2: nanoocp.Geom.Geom_Curve | None, u2: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, EpsNul: float = 0.001, EpsC0: float = 0.001, EpsC1: float = 0.001, EpsC2: float = 0.001, EpsG1: float = 0.001, EpsG2: float = 0.001, Percent: float = 0.01, Maxlen: float = 10000.0) -> None:
        """
        -u1 is the parameter of the point on Curv1
        -u2 is the parameter of the point on Curv2
        -Order is the required continuity:
        GeomAbs_C0 GeomAbs_C1 GeomAbs_C2
        GeomAbs_G1 GeomAbs_G2

        -EpsNul is used to detect a vector with null
        magnitude (in mm)

        -EpsC0 is used for C0 continuity to confuse two
        points (in mm)

        -EpsC1 is an angular tolerance in radians used
        for C1 continuity to compare the angle between
        the first derivatives

        -EpsC2 is an angular tolerance in radians used
        for C2 continuity to compare the angle between
        the second derivatives

        -EpsG1 is an angular tolerance in radians used
        for G1 continuity to compare the angle between
        the tangents

        -EpsG2 is an angular tolerance in radians used
        for G2 continuity to compare the angle between
        the normals

        - percent: percentage of curvature variation (unitless)
        used for G2 continuity

        - Maxlen is the maximum length of Curv1 or Curv2 in
        meters used to detect nul curvature (in mm)

        the constructor computes the quantities which are
        necessary to check the continuity in the following cases:

        case C0
        -------
        - the distance between P1 and P2 with P1=Curv1 (u1) and
        P2=Curv2(u2)

        case C1
        -------

        - the angle between the first derivatives
        dCurv1(u1)           dCurv2(u2)
        --------     and     ---------
        du                   du

        - the ratio between the magnitudes of the first
        derivatives

        the angle value is between 0 and PI/2

        case C2
        -------
        - the angle between the second derivatives
        2                   2
        d  Curv1(u1)       d Curv2(u2)
        ----------        ----------
        2                   2
        du                  du

        the angle value is between 0 and PI/2

        - the ratio between the magnitudes of the second
        derivatives

        case G1
        -------
        the angle between the tangents at each point

        the angle value is between 0 and PI/2

        case G2
        -------
        -the angle between the normals at each point

        the angle value is between 0 and PI/2

        - the relative variation of curvature:
        |curvat1-curvat2|
        ------------------
        1/2
        (curvat1*curvat2)

        where curvat1 is the curvature at the first point
        and curvat2 the curvature at the second point
        """

    @overload
    def __init__(self, theOther: LocalAnalysis_CurveContinuity) -> None: ...

    def IsDone(self) -> bool: ...

    def StatusError(self) -> LocalAnalysis_StatusErrorType: ...

    def ContinuityStatus(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def C0Value(self) -> float: ...

    def C1Angle(self) -> float: ...

    def C1Ratio(self) -> float: ...

    def C2Angle(self) -> float: ...

    def C2Ratio(self) -> float: ...

    def G1Angle(self) -> float: ...

    def G2Angle(self) -> float: ...

    def G2CurvatureVariation(self) -> float: ...

    def IsC0(self) -> bool: ...

    def IsC1(self) -> bool: ...

    def IsC2(self) -> bool: ...

    def IsG1(self) -> bool: ...

    def IsG2(self) -> bool: ...

class LocalAnalysis_SurfaceContinuity:
    """
    This class gives tools to check local continuity C0
    C1 C2 G1 G2 between two points situated on two surfaces
    """

    @overload
    def __init__(self, EpsNul: float = 0.001, EpsC0: float = 0.001, EpsC1: float = 0.001, EpsC2: float = 0.001, EpsG1: float = 0.001, Percent: float = 0.01, Maxlen: float = 10000.0) -> None:
        """
        This constructor is used when we want to compute many analysis.
        After we use the method ComputeAnalysis
        """

    @overload
    def __init__(self, curv1: nanoocp.Geom2d.Geom2d_Curve | None, curv2: nanoocp.Geom2d.Geom2d_Curve | None, U: float, Surf1: nanoocp.Geom.Geom_Surface | None, Surf2: nanoocp.Geom.Geom_Surface | None, Order: nanoocp.GeomAbs.GeomAbs_Shape, EpsNul: float = 0.001, EpsC0: float = 0.001, EpsC1: float = 0.001, EpsC2: float = 0.001, EpsG1: float = 0.001, Percent: float = 0.01, Maxlen: float = 10000.0) -> None: ...

    @overload
    def __init__(self, Surf1: nanoocp.Geom.Geom_Surface | None, u1: float, v1: float, Surf2: nanoocp.Geom.Geom_Surface | None, u2: float, v2: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, EpsNul: float = 0.001, EpsC0: float = 0.001, EpsC1: float = 0.001, EpsC2: float = 0.001, EpsG1: float = 0.001, Percent: float = 0.01, Maxlen: float = 10000.0) -> None:
        """
        -u1,v1 are the parameters of the point on Surf1
        -u2,v2 are the parameters of the point on Surf2
        -Order is the required continuity:
        GeomAbs_C0 GeomAbs_C1 GeomAbs_C2
        GeomAbs_G1 GeomAbs_G2

        -EpsNul is used to detect a a vector with nul
        magnitude

        -EpsC0 is used for C0 continuity to confuse two
        points (in mm)

        -EpsC1 is an angular tolerance in radians used
        for C1 continuity to compare the angle between
        the first derivatives

        -EpsC2 is an angular tolerance in radians used
        for C2 continuity to compare the angle between
        the second derivatives

        -EpsG1 is an angular tolerance in radians used
        for G1 continuity to compare the angle between
        the normals

        -Percent: percentage of curvature variation (unitless)
        used for G2 continuity

        - Maxlen is the maximum length of Surf1 or Surf2 in
        meters used to detect null curvature (in mm)

        the constructor computes the quantities which are
        necessary to check the continuity in the following cases:

        case C0
        --------
        - the distance between P1 and P2 with P1=Surf (u1,v1) and
        P2=Surfv2(u2,v2)

        case C1
        -------

        - the angle between the first derivatives in u :

        dSurf1(u1,v1)               dSurf2(u2,v2)
        -----------      and        ---------
        du                           du

        the angle value is between 0 and PI/2

        - the angle between the first derivatives in v :

        dSurf1(u1,v1)               dSurf2(u2,v2)
        --------         and         ---------
        dv                           dv

        - the ratio between the magnitudes of the first derivatives in u
        - the ratio between the magnitudes of the first derivatives in v

        the angle value is between 0 and pi/2

        case C2
        -------
        - the angle between the second derivatives in u
        2                  2
        d Surf1(u1,v1)    d  Surf2(u2,v2)
        ----------        ----------
        2                  2
        d u               d  u

        - the ratio between the magnitudes of the second derivatives in u
        - the ratio between the magnitudes of the second derivatives in v

        the angle value is between 0 and PI/2

        case G1
        -------
        -the angle between the normals at each point
        the angle value is between 0 and PI/2

        case G2
        -------
        - the maximum normal curvature gap between the two
        points
        """

    @overload
    def __init__(self, theOther: LocalAnalysis_SurfaceContinuity) -> None: ...

    def ComputeAnalysis(self, Surf1: nanoocp.GeomLProp.GeomLProp_SLProps, Surf2: nanoocp.GeomLProp.GeomLProp_SLProps, Order: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def IsDone(self) -> bool: ...

    def ContinuityStatus(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def StatusError(self) -> LocalAnalysis_StatusErrorType: ...

    def C0Value(self) -> float: ...

    def C1UAngle(self) -> float: ...

    def C1URatio(self) -> float: ...

    def C1VAngle(self) -> float: ...

    def C1VRatio(self) -> float: ...

    def C2UAngle(self) -> float: ...

    def C2URatio(self) -> float: ...

    def C2VAngle(self) -> float: ...

    def C2VRatio(self) -> float: ...

    def G1Angle(self) -> float: ...

    def G2CurvatureGap(self) -> float: ...

    def IsC0(self) -> bool: ...

    def IsC1(self) -> bool: ...

    def IsC2(self) -> bool: ...

    def IsG1(self) -> bool: ...

    def IsG2(self) -> bool: ...
