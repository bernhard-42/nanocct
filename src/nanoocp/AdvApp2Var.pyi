"""OCCT package AdvApp2Var (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.AdvApprox
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class AdvApp2Var_CriterionType(enum.IntEnum):
    """
    influence of the criterion on cutting process
    cutting when criterion is not satisfied
    deactivation of the compute of the error max
    cutting when error max is not good or if error
    max is good and criterion is not satisfied
    """

    AdvApp2Var_Absolute = 0

    AdvApp2Var_Relative = 1

class AdvApp2Var_CriterionRepartition(enum.IntEnum):
    """
    way of cutting process//! all new cutting points at each step of cutting
    process : (a+i(b-a)/N)i at step N,
    (a+i(b-a)/(N+1))i at step N+1,...
    where (a,b) is the global interval//! add one new cutting point at each step
    of cutting process
    """

    AdvApp2Var_Regular = 0

    AdvApp2Var_Incremental = 1

class AdvApp2Var_Context:
    """
    contains all the parameters for approximation
    (tolerancy, computing option, ...)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, ifav: int, iu: int, iv: int, nlimu: int, nlimv: int, iprecis: int, nb1Dss: int, nb2Dss: int, nb3Dss: int, tol1D: nanoocp.NCollection.NCollection_HArray1[float], tol2D: nanoocp.NCollection.NCollection_HArray1[float], tol3D: nanoocp.NCollection.NCollection_HArray1[float], tof1D: nanoocp.NCollection.NCollection_HArray2[float], tof2D: nanoocp.NCollection.NCollection_HArray2[float], tof3D: nanoocp.NCollection.NCollection_HArray2[float]) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_Context) -> None: ...

    def TotalDimension(self) -> int: ...

    def TotalNumberSSP(self) -> int: ...

    def FavorIso(self) -> int: ...

    def UOrder(self) -> int: ...

    def VOrder(self) -> int: ...

    def ULimit(self) -> int: ...

    def VLimit(self) -> int: ...

    def UJacDeg(self) -> int: ...

    def VJacDeg(self) -> int: ...

    def UJacMax(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def VJacMax(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def URoots(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def VRoots(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def UGauss(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def VGauss(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def IToler(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def FToler(self) -> nanoocp.NCollection.NCollection_HArray2[float]: ...

    def CToler(self) -> nanoocp.NCollection.NCollection_HArray2[float]: ...

class AdvApp2Var_EvaluatorFunc2Var:
    pass

class AdvApp2Var_Patch(nanoocp.Standard.Standard_Transient):
    """used to store results on a domain [Ui,Ui+1]x[Vj,Vj+1]"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, U0: float, U1: float, V0: float, V1: float, iu: int, iv: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsDiscretised(self) -> bool: ...

    def Discretise(self, Conditions: AdvApp2Var_Context, Constraints: AdvApp2Var_Framework, func: AdvApp2Var_EvaluatorFunc2Var) -> None: ...

    def IsApproximated(self) -> bool: ...

    def HasResult(self) -> bool: ...

    def MakeApprox(self, Conditions: AdvApp2Var_Context, Constraints: AdvApp2Var_Framework, NumDec: int) -> None: ...

    def AddConstraints(self, Conditions: AdvApp2Var_Context, Constraints: AdvApp2Var_Framework) -> None: ...

    def AddErrors(self, Constraints: AdvApp2Var_Framework) -> None: ...

    def ChangeDomain(self, a: float, b: float, c: float, d: float) -> None: ...

    def ResetApprox(self) -> None: ...

    def OverwriteApprox(self) -> None: ...

    def U0(self) -> float: ...

    def U1(self) -> float: ...

    def V0(self) -> float: ...

    def V1(self) -> float: ...

    def UOrder(self) -> int: ...

    def VOrder(self) -> int: ...

    @overload
    def CutSense(self) -> int: ...

    @overload
    def CutSense(self, Crit: AdvApp2Var_Criterion, NumDec: int) -> int: ...

    def NbCoeffInU(self) -> int: ...

    def NbCoeffInV(self) -> int: ...

    def ChangeNbCoeff(self, NbCoeffU: int, NbCoeffV: int) -> None: ...

    def Poles(self, SSPIndex: int, Conditions: AdvApp2Var_Context) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_Pnt]: ...

    def Coefficients(self, SSPIndex: int, Conditions: AdvApp2Var_Context) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def MaxErrors(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def AverageErrors(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def IsoErrors(self) -> nanoocp.NCollection.NCollection_HArray2[float]: ...

    def CritValue(self) -> float: ...

    def SetCritValue(self, dist: float) -> None: ...

class AdvApp2Var_Network:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Net: nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Patch], TheU: nanoocp.NCollection.NCollection_Sequence[float], TheV: nanoocp.NCollection.NCollection_Sequence[float]) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_Network) -> None: ...

    def FirstNotApprox(self) -> tuple[bool, int]:
        """
        search the Index of the first Patch not approximated,
        if all Patches are approximated false is returned
        """

    def ChangePatch(self, Index: int) -> AdvApp2Var_Patch: ...

    @overload
    def __call__(self, Index: int) -> AdvApp2Var_Patch: ...

    @overload
    def __call__(self, UIndex: int, VIndex: int) -> AdvApp2Var_Patch: ...

    def UpdateInU(self, CuttingValue: float) -> None: ...

    def UpdateInV(self, CuttingValue: float) -> None: ...

    def SameDegree(self, iu: int, iv: int) -> tuple[int, int]: ...

    def NbPatch(self) -> int: ...

    def NbPatchInU(self) -> int: ...

    def NbPatchInV(self) -> int: ...

    def UParameter(self, Index: int) -> float: ...

    def VParameter(self, Index: int) -> float: ...

    def Patch(self, UIndex: int, VIndex: int) -> AdvApp2Var_Patch: ...

class AdvApp2Var_Node(nanoocp.Standard.Standard_Transient):
    """used to store constraints on a (Ui,Vj) point"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, iu: int, iv: int) -> None: ...

    @overload
    def __init__(self, UV: nanoocp.gp.gp_XY, iu: int, iv: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Coord(self) -> nanoocp.gp.gp_XY:
        """Returns the coordinates (U,V) of the node"""

    def SetCoord(self, x1: float, x2: float) -> None:
        """changes the coordinates (U,V) to (x1,x2)"""

    def UOrder(self) -> int:
        """returns the continuity order in U of the node"""

    def VOrder(self) -> int:
        """returns the continuity order in V of the node"""

    def SetPoint(self, iu: int, iv: int, Pt: nanoocp.gp.gp_Pnt) -> None:
        """affects the value F(U,V) or its derivates on the node (U,V)"""

    def Point(self, iu: int, iv: int) -> nanoocp.gp.gp_Pnt:
        """returns the value F(U,V) or its derivates on the node (U,V)"""

    def SetError(self, iu: int, iv: int, error: float) -> None:
        """affects the error between F(U,V) and its approximation"""

    def Error(self, iu: int, iv: int) -> float:
        """returns the error between F(U,V) and its approximation"""

class AdvApp2Var_Iso(nanoocp.Standard.Standard_Transient):
    """used to store constraints on a line U = Ui or V = Vj"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, type: nanoocp.GeomAbs.GeomAbs_IsoType, iu: int, iv: int) -> None: ...

    @overload
    def __init__(self, type: nanoocp.GeomAbs.GeomAbs_IsoType, cte: float, Ufirst: float, Ulast: float, Vfirst: float, Vlast: float, pos: int, iu: int, iv: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsApproximated(self) -> bool: ...

    def HasResult(self) -> bool: ...

    def MakeApprox(self, Conditions: AdvApp2Var_Context, a: float, b: float, c: float, d: float, func: AdvApp2Var_EvaluatorFunc2Var, NodeBegin: AdvApp2Var_Node, NodeEnd: AdvApp2Var_Node) -> None: ...

    @overload
    def ChangeDomain(self, a: float, b: float) -> None: ...

    @overload
    def ChangeDomain(self, a: float, b: float, c: float, d: float) -> None: ...

    def SetConstante(self, newcte: float) -> None: ...

    def SetPosition(self, newpos: int) -> None: ...

    def ResetApprox(self) -> None: ...

    def OverwriteApprox(self) -> None: ...

    def Type(self) -> nanoocp.GeomAbs.GeomAbs_IsoType: ...

    def Constante(self) -> float: ...

    def T0(self) -> float: ...

    def T1(self) -> float: ...

    def U0(self) -> float: ...

    def U1(self) -> float: ...

    def V0(self) -> float: ...

    def V1(self) -> float: ...

    def UOrder(self) -> int: ...

    def VOrder(self) -> int: ...

    def Position(self) -> int: ...

    def NbCoeff(self) -> int: ...

    def Polynom(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def SomTab(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def DifTab(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def MaxErrors(self) -> nanoocp.NCollection.NCollection_HArray2[float]: ...

    def MoyErrors(self) -> nanoocp.NCollection.NCollection_HArray2[float]: ...

class AdvApp2Var_Framework:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Frame: nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Node], UFrontier: nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Iso]], VFrontier: nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Iso]]) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_Framework) -> None: ...

    def FirstNotApprox(self) -> tuple[AdvApp2Var_Iso, int, int]:
        """
        search the Index of the first Iso not approximated,
        if all Isos are approximated NULL is returned.
        """

    def FirstNode(self, Type: nanoocp.GeomAbs.GeomAbs_IsoType, IndexIso: int, IndexStrip: int) -> int: ...

    def LastNode(self, Type: nanoocp.GeomAbs.GeomAbs_IsoType, IndexIso: int, IndexStrip: int) -> int: ...

    def ChangeIso(self, IndexIso: int, IndexStrip: int, anIso: AdvApp2Var_Iso) -> None: ...

    @overload
    def Node(self, IndexNode: int) -> AdvApp2Var_Node: ...

    @overload
    def Node(self, U: float, V: float) -> AdvApp2Var_Node: ...

    def IsoU(self, U: float, V0: float, V1: float) -> AdvApp2Var_Iso: ...

    def IsoV(self, U0: float, U1: float, V: float) -> AdvApp2Var_Iso: ...

    def UpdateInU(self, CuttingValue: float) -> None: ...

    def UpdateInV(self, CuttingValue: float) -> None: ...

    def UEquation(self, IndexIso: int, IndexStrip: int) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def VEquation(self, IndexIso: int, IndexStrip: int) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

class AdvApp2Var_ApproxAFunc2Var:
    """
    Perform the approximation of <Func> F(U,V)
    Arguments are :
    Num1DSS, Num2DSS, Num3DSS :The numbers of 1,2,3 dimensional subspaces
    OneDTol, TwoDTol, ThreeDTol: The tolerance of approximation in each
    subspaces
    OneDTolFr, TwoDTolFr, ThreeDTolFr: The tolerance of approximation on
    the boundaries in each subspaces
    [FirstInU, LastInU]: The Bounds in U of the Approximation
    [FirstInV, LastInV]: The Bounds in V of the Approximation
    FavorIso : Give preference to extract u-iso or v-iso on F(U,V)
    This can be useful to optimize the <Func> method
    ContInU, ContInV : Continuity waiting in u and v
    PrecisCode : Precision on approximation's error measurement
    1 : Fast computation and average precision
    2 : Average computation and good precision
    3 : Slow computation and very good precision
    MaxDegInU : Maximum u-degree waiting in U
    MaxDegInV : Maximum u-degree waiting in V
    Warning:
    MaxDegInU (resp. MaxDegInV) must be >= 2*iu (resp. iv) + 1,
    where iu (resp. iv) = 0 if ContInU (resp. ContInV) = GeomAbs_C0,
    = 1 if = GeomAbs_C1,
    = 2 if = GeomAbs_C2.
    MaxPatch  : Maximum number of Patch waiting
    number of Patch is number of u span * number of v span
    Func      : The external method to evaluate F(U,V)
    Crit      : To (re)defined condition of convergence
    UChoice, VChoice : To define the way in U (or V) Knot insertion
    Warning:
    for the moment, the result is a 3D Surface
    so Num1DSS and Num2DSS must be equals to 0
    and Num3DSS must be equal to 1.
    Warning:
    the Function of type EvaluatorFunc2Var from Approx
    must be a subclass of AdvApp2Var_EvaluatorFunc2Var

    the result should be formatted in the following way :
    <--Num1DSS--> <--2 * Num2DSS--> <--3 * Num3DSS-->
    R[0,0] ....   R[Num1DSS,0].....  R[Dimension-1,0] for the 1st parameter
    R[0,i] ....   R[Num1DSS,i].....  R[Dimension-1,i] for the ith parameter
    R[0,N-1] .... R[Num1DSS,N-1].... R[Dimension-1,N-1] for the Nth parameter

    the order in which each Subspace appears should be consistent
    with the tolerances given in the create function and the
    results will be given in that order as well that is :
    Surface(n) will correspond to the nth entry described by Num3DSS
    """

    @overload
    def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: nanoocp.NCollection.NCollection_HArray1[float], TwoDTol: nanoocp.NCollection.NCollection_HArray1[float], ThreeDTol: nanoocp.NCollection.NCollection_HArray1[float], OneDTolFr: nanoocp.NCollection.NCollection_HArray2[float], TwoDTolFr: nanoocp.NCollection.NCollection_HArray2[float], ThreeDTolFr: nanoocp.NCollection.NCollection_HArray2[float], FirstInU: float, LastInU: float, FirstInV: float, LastInV: float, FavorIso: nanoocp.GeomAbs.GeomAbs_IsoType, ContInU: nanoocp.GeomAbs.GeomAbs_Shape, ContInV: nanoocp.GeomAbs.GeomAbs_Shape, PrecisCode: int, MaxDegInU: int, MaxDegInV: int, MaxPatch: int, Func: AdvApp2Var_EvaluatorFunc2Var, UChoice: nanoocp.AdvApprox.AdvApprox_Cutting, VChoice: nanoocp.AdvApprox.AdvApprox_Cutting) -> None: ...

    @overload
    def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: nanoocp.NCollection.NCollection_HArray1[float], TwoDTol: nanoocp.NCollection.NCollection_HArray1[float], ThreeDTol: nanoocp.NCollection.NCollection_HArray1[float], OneDTolFr: nanoocp.NCollection.NCollection_HArray2[float], TwoDTolFr: nanoocp.NCollection.NCollection_HArray2[float], ThreeDTolFr: nanoocp.NCollection.NCollection_HArray2[float], FirstInU: float, LastInU: float, FirstInV: float, LastInV: float, FavorIso: nanoocp.GeomAbs.GeomAbs_IsoType, ContInU: nanoocp.GeomAbs.GeomAbs_Shape, ContInV: nanoocp.GeomAbs.GeomAbs_Shape, PrecisCode: int, MaxDegInU: int, MaxDegInV: int, MaxPatch: int, Func: AdvApp2Var_EvaluatorFunc2Var, Crit: AdvApp2Var_Criterion, UChoice: nanoocp.AdvApprox.AdvApprox_Cutting, VChoice: nanoocp.AdvApprox.AdvApprox_Cutting) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_ApproxAFunc2Var) -> None: ...

    def IsDone(self) -> bool:
        """
        True if the approximation succeeded within the imposed
        tolerances and the wished continuities
        """

    def HasResult(self) -> bool:
        """
        True if the approximation did come out with a result that
        is not NECESSARELY within the required tolerance or a result
        that is not recognized with the wished continuities
        """

    def Surface(self, Index: int) -> nanoocp.Geom.Geom_BSplineSurface:
        """returns the BSplineSurface of range Index"""

    def UDegree(self) -> int: ...

    def VDegree(self) -> int: ...

    def NumSubSpaces(self, Dimension: int) -> int: ...

    @overload
    def MaxError(self, Dimension: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the errors max"""

    @overload
    def MaxError(self, Dimension: int, Index: int) -> float:
        """returns the error max of the BSplineSurface of range Index"""

    @overload
    def AverageError(self, Dimension: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the average errors"""

    @overload
    def AverageError(self, Dimension: int, Index: int) -> float:
        """returns the average error of the BSplineSurface of range Index"""

    @overload
    def UFrontError(self, Dimension: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        returns the errors max on UFrontiers
        Warning:
        Dimension must be equal to 3.
        """

    @overload
    def UFrontError(self, Dimension: int, Index: int) -> float:
        """
        returns the error max of the BSplineSurface of range Index on a UFrontier
        """

    @overload
    def VFrontError(self, Dimension: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        returns the errors max on VFrontiers
        Warning:
        Dimension must be equal to 3.
        """

    @overload
    def VFrontError(self, Dimension: int, Index: int) -> float:
        """
        returns the error max of the BSplineSurface of range Index on a VFrontier
        """

    def CritError(self, Dimension: int, Index: int) -> float: ...

    def Dump(self) -> object:
        """
        Prints on the stream 'o' information on the current state
        of the object.
        """

class AdvApp2Var_ApproxF2var:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_ApproxF2var) -> None: ...

class AdvApp2Var_Criterion:
    """this class contains a given criterion to be satisfied"""

    def Value(self, P: AdvApp2Var_Patch, C: AdvApp2Var_Context) -> None: ...

    def IsSatisfied(self, P: AdvApp2Var_Patch) -> bool: ...

    def MaxValue(self) -> float: ...

    def Type(self) -> AdvApp2Var_CriterionType: ...

    def Repartition(self) -> AdvApp2Var_CriterionRepartition: ...

class AdvApp2Var_MathBase:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_MathBase) -> None: ...

class AdvApp2Var_SysBase:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AdvApp2Var_SysBase) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.AdvApp2Var
AdvApp2Var_SequenceOfNode = nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Node]
AdvApp2Var_SequenceOfPatch = nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Patch]
AdvApp2Var_SequenceOfStrip = nanoocp.NCollection.NCollection_Sequence[nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Iso]]
AdvApp2Var_Strip = nanoocp.NCollection.NCollection_Sequence[nanoocp.AdvApp2Var.AdvApp2Var_Iso]
