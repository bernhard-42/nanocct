"""OCCT package CSLib (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class CSLib_DerivativeStatus(enum.IntEnum):
    """
    Status of surface derivatives computation for normal calculation.

    Describes the result of attempting to compute a surface normal
    from the first derivatives D1U and D1V at a point on a surface.
    """

    CSLib_Done = 0

    CSLib_D1uIsNull = 1

    CSLib_D1vIsNull = 2

    CSLib_D1IsNull = 3

    CSLib_D1uD1vRatioIsNull = 4

    CSLib_D1vD1uRatioIsNull = 5

    CSLib_D1uIsParallelD1v = 6

CSLib_Done: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_Done

CSLib_D1uIsNull: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_D1uIsNull

CSLib_D1vIsNull: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_D1vIsNull

CSLib_D1IsNull: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_D1IsNull

CSLib_D1uD1vRatioIsNull: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_D1uD1vRatioIsNull

CSLib_D1vD1uRatioIsNull: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_D1vD1uRatioIsNull

CSLib_D1uIsParallelD1v: CSLib_DerivativeStatus = CSLib_DerivativeStatus.CSLib_D1uIsParallelD1v

class CSLib_NormalStatus(enum.IntEnum):
    """
    Status of surface normal computation.

    Describes the result of attempting to compute the normal N to a surface,
    including cases involving derivatives of the normal (DN/du, DN/dv).
    """

    CSLib_Singular = 0

    CSLib_Defined = 1

    CSLib_InfinityOfSolutions = 2

    CSLib_D1NuIsNull = 3

    CSLib_D1NvIsNull = 4

    CSLib_D1NIsNull = 5

    CSLib_D1NuNvRatioIsNull = 6

    CSLib_D1NvNuRatioIsNull = 7

    CSLib_D1NuIsParallelD1Nv = 8

CSLib_Singular: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_Singular

CSLib_Defined: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_Defined

CSLib_InfinityOfSolutions: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_InfinityOfSolutions

CSLib_D1NuIsNull: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_D1NuIsNull

CSLib_D1NvIsNull: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_D1NvIsNull

CSLib_D1NIsNull: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_D1NIsNull

CSLib_D1NuNvRatioIsNull: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_D1NuNvRatioIsNull

CSLib_D1NvNuRatioIsNull: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_D1NvNuRatioIsNull

CSLib_D1NuIsParallelD1Nv: CSLib_NormalStatus = CSLib_NormalStatus.CSLib_D1NuIsParallelD1Nv

class CSLib:
    """
    Provides functions for basic geometric computation on curves and surfaces.

    This package implements functions for computing surface normals
    and their derivatives at parametric points. The tolerance criteria
    used are Resolution from gp and RealEpsilon from double.

    Key functionality:
    - Normal computation from surface first derivatives (D1U, D1V)
    - Approximate normal in singular cases using second derivatives
    - Derivatives of the non-normalized and normalized normal vectors
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CSLib) -> None: ...

    @overload
    @staticmethod
    def Normal(theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theSinTol: float, theNormal: nanoocp.gp.gp_Dir) -> CSLib_DerivativeStatus:
        """
        Computes the normal direction of a surface as the cross product D1U ^ D1V.

        The normal is undefined if:
        - D1U has null length, or
        - D1V has null length, or
        - D1U and D1V are parallel.

        To check parallelism, the sine of the angle between D1U and D1V
        is computed and compared with theSinTol.

        @param[in]  theD1U    First derivative in U direction
        @param[in]  theD1V    First derivative in V direction
        @param[in]  theSinTol Sine tolerance for parallelism check
        @param[out] theStatus Result status indicating success or failure reason
        @param[out] theNormal Computed normal direction (valid only if theStatus == CSLib_Done)
        """

    @overload
    @staticmethod
    def Normal(theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theMagTol: float, theNormal: nanoocp.gp.gp_Dir) -> CSLib_NormalStatus:
        """
        Computes the normal direction using magnitude tolerance.

        A simpler version that checks if the cross product magnitude
        and derivative magnitudes exceed the given tolerance.

        @param[in]  theD1U    First derivative in U direction
        @param[in]  theD1V    First derivative in V direction
        @param[in]  theMagTol Magnitude tolerance for singularity detection
        @param[out] theStatus Result status (CSLib_Defined or CSLib_Singular)
        @param[out] theNormal Computed normal direction (valid only if theStatus == CSLib_Defined)
        """

    @overload
    @staticmethod
    def Normal(theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec, theSinTol: float, theNormal: nanoocp.gp.gp_Dir) -> tuple[bool, CSLib_NormalStatus]:
        """
        Computes an approximate normal direction at a singular point using second derivatives.

        When the standard method cannot compute the normal (D1U ^ D1V is null or too small),
        this method uses a limited Taylor expansion:
        N(u0+du, v0+dv) = N0 + dN/du * du + dN/dv * dv + O(du^2, dv^2)

        The normal is approximated from dN/du and dN/dv where N = D1U ^ D1V.

        @param[in]  theD1U    First derivative in U direction
        @param[in]  theD1V    First derivative in V direction
        @param[in]  theD2U    Second derivative in U direction (d^2S/du^2)
        @param[in]  theD2V    Second derivative in V direction (d^2S/dv^2)
        @param[in]  theD2UV   Mixed second derivative (d^2S/dudv)
        @param[in]  theSinTol Sine tolerance for parallelism check
        @param[out] theDone   True if normal was successfully computed
        @param[out] theStatus Result status with detailed information
        @param[out] theNormal Computed normal direction (valid only if theDone is true)
        """

    @overload
    @staticmethod
    def Normal(theMaxOrder: int, theDerNUV: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec], theMagTol: float, theU: float, theV: float, theUmin: float, theUmax: float, theVmin: float, theVmax: float, theNormal: nanoocp.gp.gp_Dir) -> tuple[CSLib_NormalStatus, int, int]:
        """
        Computes the normal at a singular point using higher-order derivatives.

        Finds the first order k0 where the derivatives of N = D1U ^ D1V become non-null
        and collinear, ensuring a unique normal direction.

        @param[in]  theMaxOrder Maximum derivative order to examine
        @param[in]  theDerNUV   Array of derivatives of N (indices correspond to derivative orders)
        @param[in]  theMagTol   Magnitude tolerance
        @param[in]  theU, theV  Current parameter values
        @param[in]  theUmin, theUmax, theVmin, theVmax  Parameter bounds
        @param[out] theStatus   Result status
        @param[out] theNormal   Computed normal direction
        @param[out] theOrderU, theOrderV  Orders of the first non-null derivative used
        """

    @overload
    @staticmethod
    def DNNUV(theNu: int, theNv: int, theDerSurf: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order (theNu, theNv) of the non-normalized normal vector.

        The non-normalized normal is N = dS/du ^ dS/dv.
        This function computes d^(Nu+Nv)N / (du^Nu * dv^Nv).

        @param[in] theNu      Derivative order in U direction
        @param[in] theNv      Derivative order in V direction
        @param[in] theDerSurf Surface derivatives array where theDerSurf(i,j) = d^(i+j)S/(du^i * dv^j)
        for i = 0..theNu+1, j = 0..theNv+1
        @return The derivative vector d^(Nu+Nv)N / (du^Nu * dv^Nv)
        """

    @overload
    @staticmethod
    def DNNUV(theNu: int, theNv: int, theDerSurf1: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec], theDerSurf2: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec]) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of the non-normalized vector N = dS1/du ^ dS2/dv.

        This variant is used for osculating surfaces where the normal
        is computed from derivatives of two different surfaces.

        @param[in] theNu       Derivative order in U direction
        @param[in] theNv       Derivative order in V direction
        @param[in] theDerSurf1 Derivatives of the first surface S1
        @param[in] theDerSurf2 Derivatives of the second surface S2
        @return The derivative vector
        """

    @staticmethod
    def DNNormal(theNu: int, theNv: int, theDerNUV: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Vec], theIduref: int = 0, theIdvref: int = 0) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order (theNu, theNv) of the normalized normal vector.

        @param[in] theNu     Derivative order in U direction
        @param[in] theNv     Derivative order in V direction
        @param[in] theDerNUV Array of derivatives of the non-normalized normal.
        Contains derivatives d^(i+j)(D1U^D1V)/(du^i * dv^j)
        for i = theIduref..theNu+theIduref, j = theIdvref..theNv+theIdvref
        @param[in] theIduref Reference index offset in U (default 0 for regular cases)
        @param[in] theIdvref Reference index offset in V (default 0 for regular cases)
        @return The derivative of the normalized normal vector
        """

class CSLib_Class2d:
    """
    Low-level algorithm for 2D point-in-polygon classification.

    This class determines whether a 2D point lies inside, outside, or on the boundary
    of a closed polygon. It uses a ray-casting algorithm where a horizontal ray
    from the test point is extended to infinity, and the number of polygon edge
    crossings determines the classification.

    The polygon is internally normalized to [0,1] x [0,1] domain for numerical stability.

    @note This class was moved from package BRepTopAdaptor.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor. Creates an empty classifier."""

    @overload
    def __init__(self, thePnts2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theTolU: float, theTolV: float, theUMin: float, theVMin: float, theUMax: float, theVMax: float) -> None:
        """
        Constructs a 2D classifier from an array of polygon vertices.

        The polygon is automatically closed (no need to repeat the first point at the end).
        Points are normalized internally to the UV bounds for numerical stability.

        @param[in] thePnts2d Array of polygon vertices (minimum 3 points required)
        @param[in] theTolU   Tolerance in U direction for boundary detection
        @param[in] theTolV   Tolerance in V direction for boundary detection
        @param[in] theUMin   Minimum U bound of the polygon domain
        @param[in] theVMin   Minimum V bound of the polygon domain
        @param[in] theUMax   Maximum U bound of the polygon domain
        @param[in] theVMax   Maximum V bound of the polygon domain
        """

    @overload
    def __init__(self, thePnts2d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt2d], theTolU: float, theTolV: float, theUMin: float, theVMin: float, theUMax: float, theVMax: float) -> None:
        """
        Constructs a 2D classifier from a sequence of polygon vertices.

        Same as the array constructor but accepts a sequence for convenience.

        @param[in] thePnts2d Sequence of polygon vertices (minimum 3 points required)
        @param[in] theTolU   Tolerance in U direction for boundary detection
        @param[in] theTolV   Tolerance in V direction for boundary detection
        @param[in] theUMin   Minimum U bound of the polygon domain
        @param[in] theVMin   Minimum V bound of the polygon domain
        @param[in] theUMax   Maximum U bound of the polygon domain
        @param[in] theVMax   Maximum V bound of the polygon domain
        """

    @overload
    def __init__(self, thePnts2d: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.gp.gp_Pnt2d], theTolU: float, theTolV: float, theUMin: float, theVMin: float, theUMax: float, theVMax: float) -> None:
        """
        Constructs a 2D classifier from a vector of polygon vertices.

        Same as the array constructor but accepts a vector for convenience.

        @param[in] thePnts2d Vector of polygon vertices (minimum 3 points required)
        @param[in] theTolU   Tolerance in U direction for boundary detection
        @param[in] theTolV   Tolerance in V direction for boundary detection
        @param[in] theUMin   Minimum U bound of the polygon domain
        @param[in] theVMin   Minimum V bound of the polygon domain
        @param[in] theUMax   Maximum U bound of the polygon domain
        @param[in] theVMax   Maximum V bound of the polygon domain
        """

    class Result(enum.IntEnum):
        """Classification result for point-in-polygon tests."""

        Result_Inside = 1

        Result_Outside = -1

        Result_Uncertain = 0

    Result_Inside: CSLib_Class2d.Result = Result.Result_Inside

    Result_Outside: CSLib_Class2d.Result = Result.Result_Outside

    Result_Uncertain: CSLib_Class2d.Result = Result.Result_Uncertain

    def SiDans(self, thePoint: nanoocp.gp.gp_Pnt2d) -> CSLib_Class2d.Result:
        """
        Classifies a point relative to the polygon.

        @param[in] thePoint The 2D point to classify
        @return Classification result
        """

    def SiDans_OnMode(self, thePoint: nanoocp.gp.gp_Pnt2d, theTol: float) -> CSLib_Class2d.Result:
        """
        Classifies a point with explicit ON tolerance.

        Similar to SiDans() but uses the specified tolerance for boundary detection
        instead of the tolerances specified at construction.

        @param[in] thePoint The 2D point to classify
        @param[in] theTol   Tolerance for boundary detection
        @return Classification result
        """

class CSLib_NormalPolyDef(nanoocp.math.math_FunctionWithDerivative):
    """
    Polynomial definition for surface normal computation at singular points.

    This class defines a polynomial function F(X) and its derivative for use
    with numerical root-finding algorithms. The function represents a trigonometric
    polynomial in terms of cos(X) and sin(X) with binomial coefficients.

    The polynomial has the form:
    F(X) = Sum_{i=0}^{k0} C(k0,i) * cos^i(X) * sin^(k0-i)(X) * li(i)

    where C(k0,i) is the binomial coefficient and li(i) are user-provided coefficients.

    This is used internally by CSLib::Normal() to find the normal direction
    at singular surface points by solving for zeros of this polynomial.
    """

    @overload
    def __init__(self, theK0: int, theLi: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Constructs a polynomial definition for normal computation.

        @param[in] theK0 Polynomial degree (must be >= 0)
        @param[in] theLi Array of coefficients with indices 0 to theK0
        """

    @overload
    def __init__(self, theOther: CSLib_NormalPolyDef) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Computes the value of the function for the given variable.

        Evaluates F(X) = Sum_{i=0}^{k0} C(k0,i) * cos^i(X) * sin^(k0-i)(X) * li(i)

        @param[in]  theX Input variable (angle in radians)
        @param[out] theF Computed function value
        @return true if calculation was successful, false otherwise
        """

    def Derivative(self, theX: float) -> tuple[bool, float]:
        """
        Computes the derivative of the function for the given variable.

        Evaluates dF/dX using the chain rule on the trigonometric polynomial.

        @param[in]  theX Input variable (angle in radians)
        @param[out] theD Computed derivative value
        @return true if calculation was successful, false otherwise
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Computes both the value and derivative of the function.

        More efficient than calling Value() and Derivative() separately
        as common subexpressions are computed only once.

        @param[in]  theX Input variable (angle in radians)
        @param[out] theF Computed function value
        @param[out] theD Computed derivative value
        @return true if calculation was successful, false otherwise
        """
