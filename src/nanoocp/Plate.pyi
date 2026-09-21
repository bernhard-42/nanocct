"""OCCT package Plate (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.gp


class Plate_D1:
    """
    define an order 1 derivatives of a 3d valued
    function of a 2d variable
    """

    @overload
    def __init__(self, ref: Plate_D1) -> None: ...

    @overload
    def __init__(self, du: nanoocp.gp.gp_XYZ, dv: nanoocp.gp.gp_XYZ) -> None: ...

    def DU(self) -> nanoocp.gp.gp_XYZ: ...

    def DV(self) -> nanoocp.gp.gp_XYZ: ...

class Plate_D2:
    """
    define an order 2 derivatives of a 3d valued
    function of a 2d variable
    """

    @overload
    def __init__(self, ref: Plate_D2) -> None: ...

    @overload
    def __init__(self, duu: nanoocp.gp.gp_XYZ, duv: nanoocp.gp.gp_XYZ, dvv: nanoocp.gp.gp_XYZ) -> None: ...

class Plate_D3:
    """
    define an order 3 derivatives of a 3d valued
    function of a 2d variable
    """

    @overload
    def __init__(self, ref: Plate_D3) -> None: ...

    @overload
    def __init__(self, duuu: nanoocp.gp.gp_XYZ, duuv: nanoocp.gp.gp_XYZ, duvv: nanoocp.gp.gp_XYZ, dvvv: nanoocp.gp.gp_XYZ) -> None: ...

class Plate_PinpointConstraint:
    """define a constraint on the Plate"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, ImposedValue: nanoocp.gp.gp_XYZ, iu: int = 0, iv: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: Plate_PinpointConstraint) -> None: ...

    def Pnt2d(self) -> nanoocp.gp.gp_XY: ...

    def Idu(self) -> int: ...

    def Idv(self) -> int: ...

    def Value(self) -> nanoocp.gp.gp_XYZ: ...

class Plate_LinearScalarConstraint:
    """
    define on or several constraints as linear combination of
    the X,Y and Z components of a set of PinPointConstraint
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, thePPC1: Plate_PinpointConstraint, theCoeff: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def __init__(self, thePPC: nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint], theCoeff: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_XYZ]) -> None: ...

    @overload
    def __init__(self, thePPC: nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint], theCoeff: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_XYZ]) -> None: ...

    @overload
    def __init__(self, ColLen: int, RowLen: int) -> None: ...

    @overload
    def __init__(self, theOther: Plate_LinearScalarConstraint) -> None: ...

    def GetPPC(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint]: ...

    def Coeff(self) -> nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_XYZ]: ...

    def SetPPC(self, Index: int, Value: Plate_PinpointConstraint) -> None:
        """
        Sets the PinPointConstraint of index Index to
        Value raise if Index is greater than the length of
        PPC or the Row length of coeff or lower than 1
        """

    def SetCoeff(self, Row: int, Col: int, Value: nanoocp.gp.gp_XYZ) -> None:
        """
        Sets the coeff of index (Row,Col) to Value
        raise if Row (respectively Col) is greater than the
        Row (respectively Column) length of coeff
        """

class Plate_FreeGtoCConstraint:
    """
    define a G1, G2 or G3 constraint on the Plate using weaker
    constraint than GtoCConstraint
    """

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, IncrementalLoad: float = 1.0, orientation: int = 0) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, D2S: Plate_D2, D2T: Plate_D2, IncrementalLoad: float = 1.0, orientation: int = 0) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, D2S: Plate_D2, D2T: Plate_D2, D3S: Plate_D3, D3T: Plate_D3, IncrementalLoad: float = 1.0, orientation: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: Plate_FreeGtoCConstraint) -> None: ...

    def nb_PPC(self) -> int: ...

    def GetPPC(self, Index: int) -> Plate_PinpointConstraint: ...

    def nb_LSC(self) -> int: ...

    def LSC(self, Index: int) -> Plate_LinearScalarConstraint: ...

class Plate_LinearXYZConstraint:
    """
    define on or several constraints as linear combination of
    PinPointConstraint unlike the LinearScalarConstraint, usage
    of this kind of constraint preserve the X,Y and Z uncoupling.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, thePPC: nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint], theCoeff: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, thePPC: nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint], theCoeff: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    @overload
    def __init__(self, ColLen: int, RowLen: int) -> None: ...

    @overload
    def __init__(self, theOther: Plate_LinearXYZConstraint) -> None: ...

    def GetPPC(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint]: ...

    def Coeff(self) -> nanoocp.NCollection.NCollection_Array2[float]: ...

    def SetPPC(self, Index: int, Value: Plate_PinpointConstraint) -> None:
        """
        Sets the PinPointConstraint of index Index to
        Value raise if Index is greater than the length of
        PPC or the Row length of coeff or lower than 1
        """

    def SetCoeff(self, Row: int, Col: int, Value: float) -> None:
        """
        Sets the coeff of index (Row,Col) to Value
        raise if Row (respectively Col) is greater than the
        Row (respectively Column) length of coeff
        """

class Plate_GlobalTranslationConstraint:
    """force a set of UV points to translate without deformation"""

    @overload
    def __init__(self, SOfXY: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XY]) -> None: ...

    @overload
    def __init__(self, theOther: Plate_GlobalTranslationConstraint) -> None: ...

    def LXYZC(self) -> Plate_LinearXYZConstraint: ...

class Plate_GtoCConstraint:
    """define a G1, G2 or G3 constraint on the Plate"""

    @overload
    def __init__(self, ref: Plate_GtoCConstraint) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, nP: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, D2S: Plate_D2, D2T: Plate_D2) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, D2S: Plate_D2, D2T: Plate_D2, nP: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, D2S: Plate_D2, D2T: Plate_D2, D3S: Plate_D3, D3T: Plate_D3) -> None: ...

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, D1S: Plate_D1, D1T: Plate_D1, D2S: Plate_D2, D2T: Plate_D2, D3S: Plate_D3, D3T: Plate_D3, nP: nanoocp.gp.gp_XYZ) -> None: ...

    def nb_PPC(self) -> int: ...

    def GetPPC(self, Index: int) -> Plate_PinpointConstraint: ...

    def D1SurfInit(self) -> Plate_D1: ...

class Plate_LineConstraint:
    """constraint a point to belong to a straight line"""

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, lin: nanoocp.gp.gp_Lin, iu: int = 0, iv: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: Plate_LineConstraint) -> None: ...

    def LSC(self) -> Plate_LinearScalarConstraint: ...

class Plate_PlaneConstraint:
    """constraint a point to belong to a Plane"""

    @overload
    def __init__(self, point2d: nanoocp.gp.gp_XY, pln: nanoocp.gp.gp_Pln, iu: int = 0, iv: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: Plate_PlaneConstraint) -> None: ...

    def LSC(self) -> Plate_LinearScalarConstraint: ...

class Plate_Plate:
    """
    This class implement a variational spline algorithm able
    to define a two variable function satisfying some constraints
    and minimizing an energy like criterion.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Ref: Plate_Plate) -> None: ...

    def Copy(self, Ref: Plate_Plate) -> Plate_Plate: ...

    @overload
    def Load(self, PConst: Plate_PinpointConstraint) -> None: ...

    @overload
    def Load(self, LXYZConst: Plate_LinearXYZConstraint) -> None: ...

    @overload
    def Load(self, LScalarConst: Plate_LinearScalarConstraint) -> None: ...

    @overload
    def Load(self, GTConst: Plate_GlobalTranslationConstraint) -> None: ...

    @overload
    def Load(self, LConst: Plate_LineConstraint) -> None: ...

    @overload
    def Load(self, PConst: Plate_PlaneConstraint) -> None: ...

    @overload
    def Load(self, SCConst: Plate_SampledCurveConstraint) -> None: ...

    @overload
    def Load(self, GtoCConst: Plate_GtoCConstraint) -> None: ...

    @overload
    def Load(self, FGtoCConst: Plate_FreeGtoCConstraint) -> None: ...

    def SolveTI(self, ord: int = 4, anisotropie: float = 1.0, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def destroy(self) -> None: ...

    def Init(self) -> None:
        """
        reset the Plate in the initial state
        ( same as after Create())
        """

    def Evaluate(self, point2d: nanoocp.gp.gp_XY) -> nanoocp.gp.gp_XYZ: ...

    def EvaluateDerivative(self, point2d: nanoocp.gp.gp_XY, iu: int, iv: int) -> nanoocp.gp.gp_XYZ: ...

    def CoefPol(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_XYZ]:
        """
        Returns the coefficients of the polynomial part of the Plate function.
        @return 2D array of polynomial coefficients as XYZ values
        """

    def CoefPol__NCollection_HArray2__gp_XYZ(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_XYZ]:
        """
        CoefPol__NCollection_HArray2__gp_XYZ: the C++ overload CoefPol(occ::handle<NCollection_HArray2<gp_XYZ>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use CoefPol() returning handle by value instead

        @deprecated Use CoefPol() returning handle by value instead.
        """

    def SetPolynomialPartOnly(self, PPOnly: bool = True) -> None: ...

    def Continuity(self) -> int: ...

    def UVBox(self) -> tuple[float, float, float, float]: ...

    def UVConstraints(self, Seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XY]) -> None: ...

class Plate_SampledCurveConstraint:
    """define m PinPointConstraint driven by m unknown"""

    @overload
    def __init__(self, SOPPC: nanoocp.NCollection.NCollection_Sequence[nanoocp.Plate.Plate_PinpointConstraint], n: int) -> None: ...

    @overload
    def __init__(self, theOther: Plate_SampledCurveConstraint) -> None: ...

    def LXYZC(self) -> Plate_LinearXYZConstraint: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Plate
Plate_Array1OfPinpointConstraint = nanoocp.NCollection.NCollection_Array1[nanoocp.Plate.Plate_PinpointConstraint]
Plate_SequenceOfPinpointConstraint = nanoocp.NCollection.NCollection_Sequence[nanoocp.Plate.Plate_PinpointConstraint]
