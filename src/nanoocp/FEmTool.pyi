"""OCCT package FEmTool (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.PLib
import nanoocp.Standard
import nanoocp.math


class FEmTool_Assembly:
    """Assemble and solve system from (one dimensional) Finite Elements"""

    @overload
    def __init__(self, Dependence: nanoocp.NCollection.NCollection_Array2[int], Table: nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]] | None) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_Assembly) -> None: ...

    def NullifyMatrix(self) -> None:
        """Nullify all Matrix's Coefficient"""

    def AddMatrix(self, Element: int, Dimension1: int, Dimension2: int, Mat: nanoocp.math.math_Matrix) -> None:
        """
        Add an elementary Matrix in the assembly Matrix
        if Dependence(Dimension1,Dimension2) is False
        """

    def NullifyVector(self) -> None:
        """Nullify all Coordinate of assembly Vector (second member)"""

    def AddVector(self, Element: int, Dimension: int, Vec: nanoocp.math.math_Vector) -> None:
        """Add an elementary Vector in the assembly Vector (second member)"""

    def ResetConstraint(self) -> None:
        """Delete all Constraints."""

    def NullifyConstraint(self) -> None:
        """Nullify all Constraints."""

    def AddConstraint(self, IndexofConstraint: int, Element: int, Dimension: int, LinearForm: nanoocp.math.math_Vector, Value: float) -> None: ...

    def Solve(self) -> bool:
        """
        Solve the assembly system
        Returns false if the computation failed.
        """

    def Solution(self, Solution: nanoocp.math.math_Vector) -> None: ...

    def NbGlobVar(self) -> int: ...

    def AssemblyTable(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]]:
        """
        Returns the assembly table mapping element-local indices to global indices.
        @return const reference to the assembly table
        """

class FEmTool_Curve(nanoocp.Standard.Standard_Transient):
    """Curve defined by Polynomial Elements."""

    @overload
    def __init__(self, Dimension: int, NbElements: int, TheBase: nanoocp.PLib.PLib_HermitJacobi, Tolerance: float) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_Curve) -> None: ...

    def Knots(self) -> nanoocp.NCollection.NCollection_Array1[float]: ...

    def SetElement(self, IndexOfElement: int, Coeffs: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    def D0(self, U: float, Pnt: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def D1(self, U: float, Vec: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def D2(self, U: float, Vec: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def Length(self, FirstU: float, LastU: float) -> float: ...

    def GetElement(self, IndexOfElement: int, Coeffs: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    def GetPolynom(self, Coeffs: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """returns coefficients of all elements in canonical base."""

    def NbElements(self) -> int: ...

    def Dimension(self) -> int: ...

    def Base(self) -> nanoocp.PLib.PLib_HermitJacobi: ...

    def Degree(self, IndexOfElement: int) -> int: ...

    def SetDegree(self, IndexOfElement: int, Degree: int) -> None: ...

    def ReduceDegree(self, IndexOfElement: int, Tol: float) -> tuple[int, float]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class FEmTool_ElementaryCriterion(nanoocp.Standard.Standard_Transient):
    """defined J Criteria to used in minimisation"""

    @overload
    def Set(self, Coeff: nanoocp.NCollection.NCollection_HArray2[float] | None) -> None:
        """Set the coefficient of the Element (the Curve)"""

    @overload
    def Set(self, FirstKnot: float, LastKnot: float) -> None:
        """Set the definition interval of the Element"""

    def DependenceTable(self) -> nanoocp.NCollection.NCollection_HArray2[int]:
        """To know if two dimension are independent."""

    def Value(self) -> float:
        """To Compute J(E) where E is the current Element"""

    def Hessian(self, Dim1: int, Dim2: int, H: nanoocp.math.math_Matrix) -> None:
        """
        To Compute J(E) the coefficients of Hessian matrix of
        J(E) which are crossed derivatives in dimensions <Dim1>
        and <Dim2>.
        If DependenceTable(Dimension1,Dimension2) is False
        """

    def Gradient(self, Dim: int, G: nanoocp.math.math_Vector) -> None:
        """
        To Compute the coefficients in the dimension <dim>
        of the J(E)'s Gradient where E is the current Element
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class FEmTool_ElementsOfRefMatrix(nanoocp.math.math_FunctionSet):
    """
    this class describes the functions needed for calculating
    matrix elements of RefMatrix for linear criteriums
    (Tension, Flexion and Jerk) by Gauss integration.
    Each function from set gives value Pi(u)'*Pj(u)' or
    Pi(u)''*Pj(u)'' or Pi(u)'''*Pj(u)''' for each i and j,
    where Pi(u) is i-th basis function of expansion and
    (') means derivative.
    """

    @overload
    def __init__(self, TheBase: nanoocp.PLib.PLib_HermitJacobi, DerOrder: int) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_ElementsOfRefMatrix) -> None: ...

    def NbVariables(self) -> int:
        """
        returns the number of variables of the function.
        It is supposed that NbVariables = 1.
        """

    def NbEquations(self) -> int:
        """returns the number of equations of the function."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        F contains results only for i<=j in following order:
        P0*P0, P0*P1, P0*P2... P1*P1, P1*P2,... (upper triangle of
        matrix {PiPj})
        """

class FEmTool_LinearFlexion(FEmTool_ElementaryCriterion):
    """Criterium of LinearFlexion To Hermit-Jacobi elements"""

    @overload
    def __init__(self, WorkDegree: int, ConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_LinearFlexion) -> None: ...

    def DependenceTable(self) -> nanoocp.NCollection.NCollection_HArray2[int]: ...

    def Value(self) -> float: ...

    def Hessian(self, Dimension1: int, Dimension2: int, H: nanoocp.math.math_Matrix) -> None: ...

    def Gradient(self, Dimension: int, G: nanoocp.math.math_Vector) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class FEmTool_LinearJerk(FEmTool_ElementaryCriterion):
    """Criterion of LinearJerk To Hermit-Jacobi elements"""

    @overload
    def __init__(self, WorkDegree: int, ConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_LinearJerk) -> None: ...

    def DependenceTable(self) -> nanoocp.NCollection.NCollection_HArray2[int]: ...

    def Value(self) -> float: ...

    def Hessian(self, Dimension1: int, Dimension2: int, H: nanoocp.math.math_Matrix) -> None: ...

    def Gradient(self, Dimension: int, G: nanoocp.math.math_Vector) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class FEmTool_LinearTension(FEmTool_ElementaryCriterion):
    """Criterium of LinearTension To Hermit-Jacobi elements"""

    @overload
    def __init__(self, WorkDegree: int, ConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_LinearTension) -> None: ...

    def DependenceTable(self) -> nanoocp.NCollection.NCollection_HArray2[int]: ...

    def Value(self) -> float: ...

    def Hessian(self, Dimension1: int, Dimension2: int, H: nanoocp.math.math_Matrix) -> None: ...

    def Gradient(self, Dimension: int, G: nanoocp.math.math_Vector) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class FEmTool_SparseMatrix(nanoocp.Standard.Standard_Transient):
    """Sparse Matrix definition"""

    def Init(self, Value: float) -> None: ...

    def ChangeValue(self, I: int, J: int) -> float: ...

    def SetValue(self, I: int, J: int, theValue: float) -> None:
        """
        Python addition: sets the value ChangeValue(I, J) returns by reference in C++.
        """

    def Decompose(self) -> bool:
        """To make a Factorization of <me>"""

    @overload
    def Solve(self, B: nanoocp.math.math_Vector, X: nanoocp.math.math_Vector) -> None:
        """Direct Solve of AX = B"""

    @overload
    def Solve(self, B: nanoocp.math.math_Vector, Init: nanoocp.math.math_Vector, X: nanoocp.math.math_Vector, Residual: nanoocp.math.math_Vector, Tolerance: float = 1e-08, NbIterations: int = 50) -> None:
        """Iterative solve of AX = B"""

    def Prepare(self) -> bool:
        """Make Preparation to iterative solve"""

    def Multiplied(self, X: nanoocp.math.math_Vector, MX: nanoocp.math.math_Vector) -> None:
        """
        returns the product of a SparseMatrix by a vector.
        An exception is raised if the dimensions are different
        """

    def RowNumber(self) -> int:
        """returns the row range of a matrix."""

    def ColNumber(self) -> int:
        """returns the column range of the matrix."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class FEmTool_ProfileMatrix(FEmTool_SparseMatrix):
    """
    Symmetric Sparse ProfileMatrix useful for 1D Finite
    Element methods
    """

    @overload
    def __init__(self, FirstIndexes: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    @overload
    def __init__(self, theOther: FEmTool_ProfileMatrix) -> None: ...

    def Init(self, Value: float) -> None: ...

    def ChangeValue(self, I: int, J: int) -> float: ...

    def SetValue(self, I: int, J: int, theValue: float) -> None:
        """
        Python addition: sets the value ChangeValue(I, J) returns by reference in C++.
        """

    def Decompose(self) -> bool:
        """To make a Factorization of <me>"""

    @overload
    def Solve(self, B: nanoocp.math.math_Vector, X: nanoocp.math.math_Vector) -> None:
        """Direct Solve of AX = B"""

    @overload
    def Solve(self, B: nanoocp.math.math_Vector, Init: nanoocp.math.math_Vector, X: nanoocp.math.math_Vector, Residual: nanoocp.math.math_Vector, Tolerance: float = 1e-08, NbIterations: int = 50) -> None:
        """Iterative solve of AX = B"""

    def Prepare(self) -> bool:
        """Make Preparation to iterative solve"""

    def Multiplied(self, X: nanoocp.math.math_Vector, MX: nanoocp.math.math_Vector) -> None:
        """
        returns the product of a SparseMatrix by a vector.
        An exception is raised if the dimensions are different
        """

    def RowNumber(self) -> int:
        """returns the row range of a matrix."""

    def ColNumber(self) -> int:
        """returns the column range of the matrix."""

    def IsInProfile(self, i: int, j: int) -> bool: ...

    def OutM(self) -> None: ...

    def OutS(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
FEmTool_AssemblyTable = nanoocp.NCollection.NCollection_Array2[nanoocp.NCollection.NCollection_HArray1[int]]
FEmTool_HAssemblyTable = nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[int]]
