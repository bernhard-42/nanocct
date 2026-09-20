"""C++ namespace LProp_SurfaceUtils (OCCT package GeomLProp)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Geom
import nanoocp.LProp
import nanoocp.gp


class DirectAccess:
    """
    Direct access policy: calls D0/D1/D2 methods on the surface object.
    Works with occ::handle<T> and by-value surface types.
    """

    def __init__(self) -> None: ...

@overload
def GetSurfBounds(theSurf: nanoocp.Geom.Geom_Surface) -> tuple[float, float, float, float]:
    """
    Get bounds from Geom_Surface (uses Bounds method with U1, U2, V1, V2 order).
    """

@overload
def GetSurfBounds(theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface) -> tuple[float, float, float, float]:
    """
    Get bounds from Adaptor3d_Surface (uses individual parameter methods).
    Also works for BRepAdaptor_Surface which inherits from Adaptor3d_Surface.
    """

def FindSurfTangentOrder(theD1: nanoocp.gp.gp_Vec, theD2: nanoocp.gp.gp_Vec, theCN: int, theTolSq: float) -> tuple[bool, int, nanoocp.LProp.LProp_Status]:
    """
    Check if the surface tangent is defined for a given derivative direction.
    Searches for the first non-null derivative in either U or V direction.
    @param[in]  theD1        first derivative (D1U for U direction, D1V for V direction)
    @param[in]  theD2        second derivative (D2U for U direction, D2V for V direction)
    @param[in]  theCN        continuity order
    @param[in]  theTolSq     squared linear tolerance
    @param[out] theOrder     order of first significant derivative
    @param[out] theStatus    resulting tangent status
    @return true if tangent is defined
    """

def ComputeSurfNormal(theD1u: nanoocp.gp.gp_Vec, theD1v: nanoocp.gp.gp_Vec, theLinTol: float, theNormal: nanoocp.gp.gp_Dir) -> bool:
    """
    Check if surface normal is defined, and compute it via CSLib::Normal.
    @param[in]  theD1u     first U derivative
    @param[in]  theD1v     first V derivative
    @param[in]  theLinTol  linear tolerance
    @param[out] theNormal  computed normal direction (if defined)
    @return true if normal is defined
    """

def ComputeSurfCurvatures(theD1u: nanoocp.gp.gp_Vec, theD1v: nanoocp.gp.gp_Vec, theD2u: nanoocp.gp.gp_Vec, theD2v: nanoocp.gp.gp_Vec, theDuv: nanoocp.gp.gp_Vec, theNormal: nanoocp.gp.gp_Dir, theDirMin: nanoocp.gp.gp_Dir, theDirMax: nanoocp.gp.gp_Dir) -> tuple[bool, float, float, float, float]:
    """
    Compute principal curvatures and directions via fundamental forms.
    Solves the eigenvalue problem for the shape operator using
    first and second fundamental form coefficients.
    @param[in]  theD1u      first U derivative
    @param[in]  theD1v      first V derivative
    @param[in]  theD2u      second U derivative
    @param[in]  theD2v      second V derivative
    @param[in]  theDuv      mixed UV derivative
    @param[in]  theNormal   surface normal direction
    @param[out] theMinCurv  minimum principal curvature
    @param[out] theMaxCurv  maximum principal curvature
    @param[out] theDirMin   direction of minimum curvature
    @param[out] theDirMax   direction of maximum curvature
    @param[out] theMeanCurv mean curvature
    @param[out] theGausCurv Gaussian curvature
    @return true if curvatures are successfully computed
    """

def IsNormalDefined(theD1u: nanoocp.gp.gp_Vec, theD1v: nanoocp.gp.gp_Vec, theLinTol: float, theNormal: nanoocp.gp.gp_Dir) -> tuple[bool, nanoocp.LProp.LProp_Status]:
    """IsNormalDefined: checks normal status, then computes via CSLib."""
