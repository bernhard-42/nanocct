"""OCCT package ShapeExtend (toolkit TKShHealing)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class ShapeExtend_Status(enum.IntEnum):
    """
    This enumeration is used in
    ShapeHealing toolkit for representing flags in the
    return statuses of class methods.
    The status is a field of the class which is set by one or
    several methods of that class.
    It is used for reporting about errors and other situations
    encountered during execution of the method.
    There are defined 8 values for DONE and 8 for FAIL flags:
    ShapeExtend_DONE1 ...      ShapeExtend_DONE8,
    ShapeExtend_FAIL1 ...      ShapeExtend_FAIL8
    and also enumerations for representing combinations of flags:
    ShapeExtend_OK - no flags at all,
    ShapeExtend_DONE - any of flags DONEi,
    ShapeExtend_FAIL - any of flags FAILi.
    The class that uses statuses provides a method(s) which
    answers whether the flag corresponding to a given
    enumerative value is (are) set:
    bool Status(const ShapeExtend_Status test);
    Note that status can have several flags set simultaneously.
    Status(ShapeExtend_OK) gives True when no flags are set.
    Nothing done, everything OK
    Something was done, case 1
    Something was done, case 2
    Something was done, case 3
    Something was done, case 4
    Something was done, case 5
    Something was done, case 6
    Something was done, case 7
    Something was done, case 8
    Something was done (any of DONE#)
    The method failed, case 1
    The method failed, case 2
    The method failed, case 3
    The method failed, case 4
    The method failed, case 5
    The method failed, case 6
    The method failed, case 7
    The method failed, case 8
    The method failed (any of FAIL# occurred)
    """

    ShapeExtend_OK = 0

    ShapeExtend_DONE1 = 1

    ShapeExtend_DONE2 = 2

    ShapeExtend_DONE3 = 3

    ShapeExtend_DONE4 = 4

    ShapeExtend_DONE5 = 5

    ShapeExtend_DONE6 = 6

    ShapeExtend_DONE7 = 7

    ShapeExtend_DONE8 = 8

    ShapeExtend_DONE = 9

    ShapeExtend_FAIL1 = 10

    ShapeExtend_FAIL2 = 11

    ShapeExtend_FAIL3 = 12

    ShapeExtend_FAIL4 = 13

    ShapeExtend_FAIL5 = 14

    ShapeExtend_FAIL6 = 15

    ShapeExtend_FAIL7 = 16

    ShapeExtend_FAIL8 = 17

    ShapeExtend_FAIL = 18

ShapeExtend_OK: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_OK

ShapeExtend_DONE1: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE1

ShapeExtend_DONE2: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE2

ShapeExtend_DONE3: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE3

ShapeExtend_DONE4: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE4

ShapeExtend_DONE5: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE5

ShapeExtend_DONE6: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE6

ShapeExtend_DONE7: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE7

ShapeExtend_DONE8: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE8

ShapeExtend_DONE: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_DONE

ShapeExtend_FAIL1: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL1

ShapeExtend_FAIL2: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL2

ShapeExtend_FAIL3: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL3

ShapeExtend_FAIL4: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL4

ShapeExtend_FAIL5: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL5

ShapeExtend_FAIL6: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL6

ShapeExtend_FAIL7: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL7

ShapeExtend_FAIL8: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL8

ShapeExtend_FAIL: ShapeExtend_Status = ShapeExtend_Status.ShapeExtend_FAIL

class ShapeExtend_Parametrisation(enum.IntEnum):
    """
    Defines kind of global parametrisation on the composite surface
    each patch of the 1st row and column adds its range, Ui+1 = Ui + URange(i,1), etc.
    each patch gives range 1.: Ui = i-1, Vj = j-1
    uniform parametrisation with global range [0,1]
    """

    ShapeExtend_Natural = 0

    ShapeExtend_Uniform = 1

    ShapeExtend_Unitary = 2

ShapeExtend_Natural: ShapeExtend_Parametrisation = ShapeExtend_Parametrisation.ShapeExtend_Natural

ShapeExtend_Uniform: ShapeExtend_Parametrisation = ShapeExtend_Parametrisation.ShapeExtend_Uniform

ShapeExtend_Unitary: ShapeExtend_Parametrisation = ShapeExtend_Parametrisation.ShapeExtend_Unitary

class ShapeExtend:
    """
    This package provides general tools and data structures common
    for other packages in SHAPEWORKS and extending CAS.CADE
    structures.
    The following items are provided by this package:
    - enumeration Status used for coding status flags in methods
    inside the SHAPEWORKS
    - enumeration Parametrisation used for setting global parametrisation
    on the composite surface
    - class CompositeSurface representing a composite surface
    made of a grid of surface patches
    - class WireData representing a wire in the form of ordered
    list of edges
    - class MsgRegistrator for attaching messages to the objects
    - tools for exploring the shapes
    - tools for creating new shapes
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeExtend) -> None: ...

    @staticmethod
    def Init() -> None:
        """
        Inits using of ShapeExtend.
        Currently, loads messages output by ShapeHealing algorithms.
        """

    @staticmethod
    def EncodeStatus(status: ShapeExtend_Status) -> int:
        """Encodes status (enumeration) to a bit flag"""

    @staticmethod
    def DecodeStatus(flag: int, status: ShapeExtend_Status) -> bool:
        """Tells if a bit flag contains bit corresponding to enumerated status"""

class ShapeExtend_BasicMsgRegistrator(nanoocp.Standard.Standard_Transient):
    """
    Abstract class that can be used for attaching messages
    to the objects (e.g. shapes).
    It is used by ShapeHealing algorithms to attach a message
    describing encountered case (e.g. removing small edge from
    a wire).

    The methods of this class are empty and redefined, for instance,
    in the classes for Data Exchange processors for attaching
    messages to interface file entities or CAS.CADE shapes.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeExtend_BasicMsgRegistrator) -> None: ...

    @overload
    def Send(self, object: nanoocp.Standard.Standard_Transient | None, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity) -> None:
        """
        Sends a message to be attached to the object.
        Object can be of any type interpreted by redefined MsgRegistrator.
        """

    @overload
    def Send(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity) -> None:
        """Sends a message to be attached to the shape."""

    @overload
    def Send(self, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity) -> None:
        """Calls Send method with Null Transient."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeExtend_ComplexCurve(nanoocp.Geom.Geom_Curve):
    """
    Defines a curve which consists of several segments.
    Implements basic interface to it.
    """

    def NbCurves(self) -> int:
        """Returns number of curves"""

    def Curve(self, index: int) -> nanoocp.Geom.Geom_Curve:
        """Returns curve given by its index"""

    def LocateParameter(self, U: float) -> tuple[int, float]:
        """
        Returns number of the curve for the given parameter U
        and local parameter UOut for the found curve
        """

    def LocalToGlobal(self, index: int, Ulocal: float) -> float:
        """
        Returns global parameter for the whole curve according
        to the segment and local parameter on it
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """Applies transformation to each curve"""

    def ReversedParameter(self, U: float) -> float:
        """Returns 1 - U"""

    def FirstParameter(self) -> float:
        """Returns 0"""

    def LastParameter(self) -> float:
        """Returns 1"""

    def IsClosed(self) -> bool:
        """Returns True if the curve is closed"""

    def IsPeriodic(self) -> bool:
        """Returns False"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns GeomAbs_C0"""

    def IsCN(self, N: int) -> bool:
        """Returns False if N > 0"""

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt:
        """
        Returns point at parameter U.
        Finds appropriate curve and local parameter on it.
        """

    def EvalD1(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD1: ...

    def EvalD2(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD2: ...

    def EvalD3(self, U: float) -> nanoocp.Geom.Geom_Curve.ResD3: ...

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec: ...

    def GetScaleFactor(self, ind: int) -> float:
        """Returns scale factor for recomputing of deviatives."""

    def CheckConnectivity(self, Preci: float) -> bool:
        """
        Checks geometrical connectivity of the curves, including
        closure (sets fields myClosed)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeExtend_CompositeSurface(nanoocp.Geom.Geom_Surface):
    """
    Composite surface is represented by a grid of surfaces
    (patches) connected geometrically. Patches may have different
    parametrisation ranges, but they should be parametrised in
    the same manner so that parameter of each patch (u,v) can be converted
    to global parameter on the whole surface (U,V) with help of linear
    transformation:

    for any i,j-th patch
    U = Ui + ( u - uijmin ) * ( Ui+1 - Ui ) / ( uijmax - uijmin )
    V = Vj + ( v - vijmin ) * ( Vj+1 - Vj ) / ( vijmax - vijmin )

    where

    [uijmin, uijmax] * [ vijmin, vijmax] - parametric range of i,j-th patch,

    Ui (i=1,..,Nu+1), Vi (j=1,..,Nv+1) - values defining global
    parametrisation by U and V (correspond to points between patches and
    bounds, (Ui,Uj) corresponds to (uijmin,vijmin) on i,j-th patch) and to
    (u(i-1)(j-1)max,v(i-1)(j-1)max) on (i-1),(j-1)-th patch.

    Geometrical connectivity is expressed via global parameters:
    S[i,j](Ui+1,V) = S[i+1,j](Ui+1,V) for any i, j, V
    S[i,j](U,Vj+1) = S[i,j+1](U,Vj+1) for any i, j, U
    It is checked with Precision::Confusion() by default.

    NOTE 1: This class is inherited from Geom_Surface in order to
    make it more easy to store and deal with it. However, it should
    not be passed to standard methods dealing with geometry since
    this type is not known to them.
    NOTE 2: Not all the inherited methods are implemented, and some are
    implemented not in the full form.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, GridSurf: nanoocp.NCollection.NCollection_HArray2[nanoocp.Geom.Geom_Surface] | None, param: ShapeExtend_Parametrisation = ShapeExtend_Parametrisation.ShapeExtend_Natural) -> None: ...

    @overload
    def __init__(self, GridSurf: nanoocp.NCollection.NCollection_HArray2[nanoocp.Geom.Geom_Surface] | None, UJoints: nanoocp.NCollection.NCollection_Array1[float], VJoints: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Initializes by a grid of surfaces (calls Init())."""

    @overload
    def __init__(self, theOther: ShapeExtend_CompositeSurface) -> None: ...

    @overload
    def Init(self, GridSurf: nanoocp.NCollection.NCollection_HArray2[nanoocp.Geom.Geom_Surface] | None, param: ShapeExtend_Parametrisation = ShapeExtend_Parametrisation.ShapeExtend_Natural) -> bool:
        """
        Initializes by a grid of surfaces.
        All the Surfaces of the grid must have geometrical
        connectivity as stated above.
        If geometrical connectivity is not satisfied, method
        returns False.
        However, class is initialized even in that case.

        Last parameter defines how global parametrisation
        (joint values) will be computed:
        ShapeExtend_Natural: U1 = u11min, Ui+1 = Ui + (ui1max-ui1min), etc.
        ShapeExtend_Uniform: Ui = i-1, Vj = j-1
        ShapeExtend_Unitary: Ui = (i-1)/Nu, Vi = (j-1)/Nv
        """

    @overload
    def Init(self, GridSurf: nanoocp.NCollection.NCollection_HArray2[nanoocp.Geom.Geom_Surface] | None, UJoints: nanoocp.NCollection.NCollection_Array1[float], VJoints: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Initializes by a grid of surfaces with given global
        parametrisation defined by UJoints and VJoints arrays,
        each having length equal to number of patches in corresponding
        direction + 1. Global joint values should be sorted in
        increasing order.
        All the Surfaces of the grid must have geometrical
        connectivity as stated above.
        If geometrical connectivity is not satisfied, method
        returns False.
        However, class is initialized even in that case.
        """

    def NbUPatches(self) -> int:
        """Returns number of patches in U direction."""

    def NbVPatches(self) -> int:
        """Returns number of patches in V direction."""

    @overload
    def Patch(self, i: int, j: int) -> nanoocp.Geom.Geom_Surface:
        """Returns one surface patch"""

    @overload
    def Patch(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface:
        """Returns one surface patch that contains given (global) parameters"""

    @overload
    def Patch(self, pnt: nanoocp.gp.gp_Pnt2d) -> nanoocp.Geom.Geom_Surface:
        """Returns one surface patch that contains given point"""

    def Patches(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.Geom.Geom_Surface]:
        """Returns grid of surfaces"""

    def UJointValues(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the array of U values corresponding to joint
        points between patches as well as to start and end points,
        which define global parametrisation of the surface
        """

    def VJointValues(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the array of V values corresponding to joint
        points between patches as well as to start and end points,
        which define global parametrisation of the surface
        """

    def UJointValue(self, i: int) -> float:
        """
        Returns i-th joint value in U direction
        (1-st is global Umin, (NbUPatches()+1)-th is global Umax
        on the composite surface)
        """

    def VJointValue(self, j: int) -> float:
        """
        Returns j-th joint value in V direction
        (1-st is global Vmin, (NbVPatches()+1)-th is global Vmax
        on the composite surface)
        """

    def SetUJointValues(self, UJoints: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Sets the array of U values corresponding to joint
        points, which define global parametrisation of the surface.
        Number of values in array should be equal to NbUPatches()+1.
        All the values should be sorted in increasing order.
        If this is not satisfied, does nothing and returns False.
        """

    def SetVJointValues(self, VJoints: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Sets the array of V values corresponding to joint
        points, which define global parametrisation of the surface
        Number of values in array should be equal to NbVPatches()+1.
        All the values should be sorted in increasing order.
        If this is not satisfied, does nothing and returns False.
        """

    def SetUFirstValue(self, UFirst: float) -> None:
        """
        Changes starting value for global U parametrisation (all
        other joint values are shifted accordingly)
        """

    def SetVFirstValue(self, VFirst: float) -> None:
        """
        Changes starting value for global V parametrisation (all
        other joint values are shifted accordingly)
        """

    def LocateUParameter(self, U: float) -> int:
        """Returns number of col that contains given (global) parameter"""

    def LocateVParameter(self, V: float) -> int:
        """Returns number of row that contains given (global) parameter"""

    def LocateUVPoint(self, pnt: nanoocp.gp.gp_Pnt2d) -> tuple[int, int]:
        """
        Returns number of row and col of surface that contains
        given point
        """

    def ULocalToGlobal(self, i: int, j: int, u: float) -> float:
        """Converts local parameter u on patch i,j to global parameter U"""

    def VLocalToGlobal(self, i: int, j: int, v: float) -> float:
        """Converts local parameter v on patch i,j to global parameter V"""

    def LocalToGlobal(self, i: int, j: int, uv: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Pnt2d:
        """Converts local parameters uv on patch i,j to global parameters UV"""

    def UGlobalToLocal(self, i: int, j: int, U: float) -> float:
        """Converts global parameter U to local parameter u on patch i,j"""

    def VGlobalToLocal(self, i: int, j: int, V: float) -> float:
        """Converts global parameter V to local parameter v on patch i,j"""

    def GlobalToLocal(self, i: int, j: int, UV: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Pnt2d:
        """Converts global parameters UV to local parameters uv on patch i,j"""

    def GlobalToLocalTransformation(self, i: int, j: int, Trsf: nanoocp.gp.gp_Trsf2d) -> tuple[bool, float]:
        """
        Computes transformation operator and uFactor descrinbing affine
        transformation required to convert global parameters on composite
        surface to local parameters on patch (i,j):
        uv = ( uFactor, 1. ) X Trsf * UV;
        NOTE: Thus Trsf contains shift and scale by V, scale by U is stored in uFact.
        Returns True if transformation is not an identity
        """

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """Applies transformation to all the patches"""

    def Copy(self) -> nanoocp.Geom.Geom_Geometry:
        """Returns a copy of the surface"""

    def UReverse(self) -> None:
        """NOT IMPLEMENTED (does nothing)"""

    def UReversedParameter(self, U: float) -> float:
        """Returns U"""

    def VReverse(self) -> None:
        """NOT IMPLEMENTED (does nothing)"""

    def VReversedParameter(self, V: float) -> float:
        """Returns V"""

    def Bounds(self) -> tuple[float, float, float, float]:
        """Returns the parametric bounds of grid"""

    def IsUClosed(self) -> bool:
        """
        Returns True if grid is closed in U direction
        (i.e. connected with Precision::Confusion)
        """

    def IsVClosed(self) -> bool:
        """
        Returns True if grid is closed in V direction
        (i.e. connected with Precision::Confusion)
        """

    def IsUPeriodic(self) -> bool:
        """Returns False"""

    def IsVPeriodic(self) -> bool:
        """Returns False"""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """NOT IMPLEMENTED (returns Null curve)"""

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """NOT IMPLEMENTED (returns Null curve)"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """returns C0"""

    def IsCNu(self, N: int) -> bool:
        """returns True if N <=0"""

    def IsCNv(self, N: int) -> bool:
        """returns True if N <=0"""

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter U,V on the grid."""

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """
        Computes the point P and the first derivatives in the
        directions U and V at this point.
        """

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """
        Computes the point P, the first and the second derivatives in
        the directions U and V at this point.
        """

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """
        Computes the point P, the first,the second and the third
        derivatives in the directions U and V at this point.
        """

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the direction U and Nv
        in the direction V at the point P(U, V).
        """

    def Value(self, pnt: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter pnt on the grid."""

    def ComputeJointValues(self, param: ShapeExtend_Parametrisation = ShapeExtend_Parametrisation.ShapeExtend_Natural) -> None:
        """Computes Joint values according to parameter"""

    def CheckConnectivity(self, prec: float) -> bool:
        """
        Checks geometrical connectivity of the patches, including
        closedness (sets fields muUClosed and myVClosed)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeExtend_Explorer:
    """
    This class is intended to
    explore shapes and convert different representations
    (list, sequence, compound) of complex shapes. It provides tools for:
    - obtaining type of the shapes in context of TopoDS_Compound,
    - exploring shapes in context of TopoDS_Compound,
    - converting different representations of shapes (list, sequence, compound).
    """

    @overload
    def __init__(self) -> None:
        """Creates an object Explorer"""

    @overload
    def __init__(self, theOther: ShapeExtend_Explorer) -> None: ...

    def CompoundFromSeq(self, seqval: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Converts a sequence of Shapes to a Compound"""

    def SeqFromCompound(self, comp: nanoocp.TopoDS.TopoDS_Shape, expcomp: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Converts a Compound to a list of Shapes
        if <comp> is not a compound, the list contains only <comp>
        if <comp> is Null, the list is empty
        if <comp> is a Compound, its sub-shapes are put into the list
        then if <expcomp> is True, if a sub-shape is a Compound, it
        is not put to the list but its sub-shapes are (recursive)
        """

    def ListFromSeq(self, seqval: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, lisval: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], clear: bool = True) -> None:
        """
        Converts a Sequence of Shapes to a List of Shapes
        <clear> if True (D), commands the list to start from scratch
        else, the list is cumulated
        """

    def SeqFromList(self, lisval: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """Converts a List of Shapes to a Sequence of Shapes"""

    def ShapeType(self, shape: nanoocp.TopoDS.TopoDS_Shape, compound: bool) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        Returns the type of a Shape: true type if <compound> is False
        If <compound> is True and <shape> is a Compound, iterates on
        its items. If all are of the same type, returns this type.
        Else, returns COMPOUND. If it is empty, returns SHAPE
        For a Null Shape, returns SHAPE
        """

    def SortedCompound(self, shape: nanoocp.TopoDS.TopoDS_Shape, type: nanoocp.TopAbs.TopAbs_ShapeEnum, explore: bool, compound: bool) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds a COMPOUND from the given shape.
        It explores the shape level by level, according to the
        <explore> argument. If <explore> is False, only COMPOUND
        items are explored, else all items are.
        The following shapes are added to resulting compound:
        - shapes which comply to <type>
        - if <type> is WIRE, considers also free edges (and makes wires)
        - if <type> is SHELL, considers also free faces (and makes shells)
        If <compound> is True, gathers items in compounds which
        correspond to starting COMPOUND,SOLID or SHELL containers, or
        items directly contained in a Compound
        """

    def DispatchList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None) -> tuple[nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]]:
        """
        Dispatches starting list of shapes according to their type,
        to the appropriate resulting lists
        For each of these lists, if it is null, it is firstly created
        else, new items are appended to the already existing ones
        """

class ShapeExtend_MsgRegistrator(ShapeExtend_BasicMsgRegistrator):
    """
    Attaches messages to the objects (generic Transient or shape).
    The objects of this class are transmitted to the Shape Healing
    algorithms so that they could collect messages occurred during
    processing.

    Messages are added to the Maps (stored as a field) that can be
    used, for instance, by Data Exchange processors to attach those
    messages to initial file entities.
    """

    @overload
    def __init__(self) -> None:
        """Creates an object."""

    @overload
    def __init__(self, theOther: ShapeExtend_MsgRegistrator) -> None: ...

    @overload
    def Send(self, object: nanoocp.Standard.Standard_Transient | None, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity) -> None:
        """
        Sends a message to be attached to the object.
        If the object is in the map then the message is added to the
        list, otherwise the object is firstly added to the map.
        """

    @overload
    def Send(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity) -> None:
        """
        Sends a message to be attached to the shape.
        If the shape is in the map then the message is added to the
        list, otherwise the shape is firstly added to the map.
        """

    def MapTransient(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.Standard.Standard_Transient, nanoocp.NCollection.NCollection_List[nanoocp.Message.Message_Msg]]:
        """Returns a Map of objects and message list"""

    def MapShape(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.Message.Message_Msg], nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns a Map of shapes and message list"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeExtend_WireData(nanoocp.Standard.Standard_Transient):
    """
    This class provides a data structure necessary for work with the wire as with
    ordered list of edges, what is required for many algorithms. The advantage of
    this class is that it allows to work with wires which are not correct.
    The object of the class ShapeExtend_WireData can be initialized by
    TopoDS_Wire, and converted back to TopoDS_Wire.
    An edge in the wire is defined by its rank number. Operations of accessing,
    adding and removing edge at the given rank number are provided. On the whole
    wire, operations of circular permutation and reversing (both orientations of
    all edges and order of edges) are provided as well.
    This class also provides a method to check if the edge in the wire is a seam
    (if the wire lies on a face).
    This class is handled by reference. Such an approach gives the following advantages:
    1.    Sharing the object of this class strongly optimizes the processes of
    analysis and fixing performed in parallel on the wire stored in the form
    of this class. Fixing tool (e.g. ShapeFix_Wire) fixes problems one by
    one using analyzing tool (e.g. ShapeAnalysis_Wire). Sharing allows not
    to reinitialize each time the analyzing tool with modified
    ShapeExtend_WireData what consumes certain time.
    2.    No copying of contents. The object of ShapeExtend_WireData class has
    quite big size, returning it as a result of the function would cause
    additional copying of contents if this class were one handled by value.
    Moreover, this class is stored as a field in other classes which are
    they returned as results of functions, storing only a handle to
    ShapeExtend_WireData saves time and memory.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor, creates empty wire with no edges"""

    @overload
    def __init__(self, wire: nanoocp.TopoDS.TopoDS_Wire, chained: bool = True, theManifoldMode: bool = True) -> None:
        """
        Constructor initializing the data from TopoDS_Wire. Calls Init(wire,chained).
        """

    @overload
    def __init__(self, theOther: ShapeExtend_WireData) -> None: ...

    @overload
    def Init(self, other: ShapeExtend_WireData | None) -> None:
        """Copies data from another WireData"""

    @overload
    def Init(self, wire: nanoocp.TopoDS.TopoDS_Wire, chained: bool = True, theManifoldMode: bool = True) -> bool:
        """
        Loads an already existing wire
        If <chained> is True (default), edges are added in the
        sequence as they are explored by TopoDS_Iterator
        Else, if <chained> is False, wire is explored by
        BRepTools_WireExplorer and it is guaranteed that edges will
        be sequentially connected.
        Remark : In the latter case it can happen that not all edges
        will be found (because of limitations of
        BRepTools_WireExplorer for disconnected wires and wires
        with seam edges).
        """

    def Clear(self) -> None:
        """Clears data about Wire."""

    def ComputeSeams(self, enforce: bool = True) -> None:
        """
        Computes the list of seam edges
        By default (direct call), computing is enforced
        For indirect call (from IsSeam) it is redone only if not yet
        already done or if the list of edges has changed
        Remark : A Seam Edge is an Edge present twice in the list, once as
        FORWARD and once as REVERSED
        Each sense has its own PCurve, the one for FORWARD
        must be set in first
        """

    def SetLast(self, num: int) -> None:
        """Does a circular permutation in order to set <num>th edge last"""

    def SetDegeneratedLast(self) -> None:
        """
        When the wire contains at least one degenerated edge, sets it
        as last one
        Note   : It is useful to process pcurves, for instance, while the pcurve
        of a DGNR may not be computed from its 3D part (there is none)
        it is computed after the other edges have been computed and
        chained.
        """

    @overload
    def Add(self, edge: nanoocp.TopoDS.TopoDS_Edge, atnum: int = 0) -> None:
        """
        Adds an edge to a wire, being defined (not yet ended)
        This is the plain, basic, function to add an edge
        <num> = 0 (D): Appends at end
        <num> = 1: Preprends at start
        else, Insert before <num>
        Remark : Null Edge is simply ignored
        """

    @overload
    def Add(self, wire: nanoocp.TopoDS.TopoDS_Wire, atnum: int = 0) -> None:
        """
        Adds an entire wire, considered as a list of edges
        Remark : The wire is assumed to be ordered (TopoDS_Iterator
        is used)
        """

    @overload
    def Add(self, wire: ShapeExtend_WireData | None, atnum: int = 0) -> None:
        """Adds a wire in the form of WireData"""

    @overload
    def Add(self, shape: nanoocp.TopoDS.TopoDS_Shape, atnum: int = 0) -> None:
        """Adds an edge or a wire invoking corresponding method Add"""

    @overload
    def AddOriented(self, edge: nanoocp.TopoDS.TopoDS_Edge, mode: int) -> None:
        """
        Adds an edge to start or end of <me>, according to <mode>
        0: at end, as direct
        1: at end, as reversed
        2: at start, as direct
        3: at start, as reversed
        < 0: no adding
        """

    @overload
    def AddOriented(self, wire: nanoocp.TopoDS.TopoDS_Wire, mode: int) -> None:
        """
        Adds a wire to start or end of <me>, according to <mode>
        0: at end, as direct
        1: at end, as reversed
        2: at start, as direct
        3: at start, as reversed
        < 0: no adding
        """

    @overload
    def AddOriented(self, shape: nanoocp.TopoDS.TopoDS_Shape, mode: int) -> None:
        """
        Adds an edge or a wire invoking corresponding method
        AddOriented
        """

    def Remove(self, num: int = 0) -> None:
        """Removes an Edge, given its rank. By default removes the last edge."""

    def Set(self, edge: nanoocp.TopoDS.TopoDS_Edge, num: int = 0) -> None:
        """
        Replaces an edge at the given
        rank number <num> with new one. Default is last edge (<num> = 0).
        """

    @overload
    def Reverse(self) -> None:
        """
        Reverses the sense of the list and the orientation of each Edge
        This method should be called when either wire has no seam edges
        or face is not available
        """

    @overload
    def Reverse(self, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Reverses the sense of the list and the orientation of each Edge
        The face is necessary for swapping pcurves for seam edges
        (first pcurve corresponds to orientation FORWARD, and second to
        REVERSED; when edge is reversed, pcurves must be swapped)
        If face is NULL, no swapping is performed
        """

    def NbEdges(self) -> int:
        """Returns the count of currently recorded edges"""

    def NbNonManifoldEdges(self) -> int:
        """Returns the count of currently recorded non-manifold edges"""

    def NonmanifoldEdge(self, num: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns <num>th nonmanifold Edge"""

    def NonmanifoldEdges(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns sequence of non-manifold edges
        This sequence can be not empty if wire data set in manifold mode but
        initial wire has INTERNAL orientation or contains INTERNAL edges
        """

    def ManifoldMode(self) -> bool:
        """
        Returns mode defining manifold wire data or not.
        If manifold that nonmanifold edges will not be not
        consider during operations(previous behaviour)
        and they will be added only in result wire
        else non-manifold edges will consider during operations
        """

    def SetManifoldMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ManifoldMode() returns by reference in C++.
        """

    def Edge(self, num: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns <num>th Edge"""

    def Index(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> int:
        """
        Returns the index of the edge
        If the edge is a seam the orientation is also checked
        Returns 0 if the edge is not found in the list
        """

    def IsSeam(self, num: int) -> bool:
        """
        Tells if an Edge is seam (see ComputeSeams)
        An edge is considered as seam if it presents twice in
        the edge list, once as FORWARD and once as REVERSED.
        """

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Makes TopoDS_Wire using
        BRep_Builder (just creates the TopoDS_Wire object and adds
        all edges into it). This method should be called when
        the wire is correct (for example, after successful
        fixes by ShapeFix_Wire) and adjacent edges share common
        vertices. In case if adjacent edges do not share the same
        vertices the resulting TopoDS_Wire will be invalid.
        """

    def WireAPIMake(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Makes TopoDS_Wire using
        BRepAPI_MakeWire. Class BRepAPI_MakeWire merges
        geometrically coincided vertices and can disturb
        correct order of edges in the wire. If this class fails,
        null shape is returned.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopTools
ShapeExtend_DataMapOfShapeListOfMsg = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.Message.Message_Msg], nanoocp.TopTools.TopTools_ShapeMapHasher]
