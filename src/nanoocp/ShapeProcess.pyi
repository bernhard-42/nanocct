"""OCCT package ShapeProcess (toolkit TKShHealing)"""

import enum
from typing import overload

import nanoocp.BRepTools
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Resource
import nanoocp.ShapeBuild
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.TopTools


class ShapeProcess:
    """
    Shape Processing module
    allows to define and apply general Shape Processing as a
    customizable sequence of Shape Healing operators. The
    customization is implemented via user-editable resource
    file which defines sequence of operators to be executed
    and their parameters.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeProcess) -> None: ...

    class Operation(enum.IntEnum):
        """
        Describes all available operations.
        C++11 enum class is not used to allow implicit conversion to underlying type.
        """

        First = 0

        DirectFaces = 0

        SameParameter = 1

        SetTolerance = 2

        SplitAngle = 3

        BSplineRestriction = 4

        ElementaryToRevolution = 5

        SweptToElementary = 6

        SurfaceToBSpline = 7

        ToBezier = 8

        SplitContinuity = 9

        SplitClosedFaces = 10

        FixWireGaps = 11

        FixFaceSize = 12

        DropSmallSolids = 13

        DropSmallEdges = 14

        FixShape = 15

        SplitClosedEdges = 16

        SplitCommonVertex = 17

        Last = 17

    First: ShapeProcess.Operation = Operation.First

    SameParameter: ShapeProcess.Operation = Operation.SameParameter

    SetTolerance: ShapeProcess.Operation = Operation.SetTolerance

    SplitAngle: ShapeProcess.Operation = Operation.SplitAngle

    BSplineRestriction: ShapeProcess.Operation = Operation.BSplineRestriction

    ElementaryToRevolution: ShapeProcess.Operation = Operation.ElementaryToRevolution

    SweptToElementary: ShapeProcess.Operation = Operation.SweptToElementary

    SurfaceToBSpline: ShapeProcess.Operation = Operation.SurfaceToBSpline

    ToBezier: ShapeProcess.Operation = Operation.ToBezier

    SplitContinuity: ShapeProcess.Operation = Operation.SplitContinuity

    SplitClosedFaces: ShapeProcess.Operation = Operation.SplitClosedFaces

    FixWireGaps: ShapeProcess.Operation = Operation.FixWireGaps

    FixFaceSize: ShapeProcess.Operation = Operation.FixFaceSize

    DropSmallSolids: ShapeProcess.Operation = Operation.DropSmallSolids

    DropSmallEdges: ShapeProcess.Operation = Operation.DropSmallEdges

    FixShape: ShapeProcess.Operation = Operation.FixShape

    SplitClosedEdges: ShapeProcess.Operation = Operation.SplitClosedEdges

    SplitCommonVertex: ShapeProcess.Operation = Operation.SplitCommonVertex

    DirectFaces: ShapeProcess.Operation = Operation.DirectFaces

    Last: ShapeProcess.Operation = Operation.Last

    @staticmethod
    def RegisterOperator(name: str, op: ShapeProcess_Operator | None) -> bool:
        """Registers operator to make it visible for Performer"""

    @staticmethod
    def FindOperator(name: str) -> tuple[bool, ShapeProcess_Operator]:
        """Finds operator by its name"""

    @staticmethod
    def Perform(context: ShapeProcess_Context | None, seq: str, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Performs a specified sequence of operators on Context
        Resource file and other data should be already loaded
        to Context (including description of sequence seq)
        """

    @staticmethod
    def ToOperationFlag(theName: str) -> tuple[ShapeProcess.Operation, bool]:
        """
        Converts operation name to operation flag.
        @param theName Operation name.
        @return Operation flag and true if the operation name is valid, false otherwise.
        """

class ShapeProcess_Context(nanoocp.Standard.Standard_Transient):
    """
    Provides convenient interface to resource file
    Allows to load resource file and get values of
    attributes starting from some scope, for example
    if scope is defined as "ToV4" and requested parameter
    is "exec.op", value of "ToV4.exec.op" parameter from
    the resource file will be returned
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, file: str, scope: str = '') -> None:
        """
        Creates a new tool and initialises by name of
        resource file and (if specified) starting scope
        Calls method Init()
        """

    @overload
    def __init__(self, theOther: ShapeProcess_Context) -> None: ...

    def Init(self, file: str, scope: str = '') -> bool:
        """
        Initialises a tool by loading resource file and
        (if specified) sets starting scope
        Returns False if resource file not found
        """

    def LoadResourceManager(self, file: str) -> nanoocp.Resource.Resource_Manager:
        """
        Loading Resource_Manager object if this object not
        equal internal static Resource_Manager object or
        internal static Resource_Manager object is null
        """

    def ResourceManager(self) -> nanoocp.Resource.Resource_Manager:
        """Returns internal Resource_Manager object"""

    def SetScope(self, scope: str) -> None:
        """Set a new (sub)scope"""

    def UnSetScope(self) -> None:
        """Go out of current scope"""

    def IsParamSet(self, param: str) -> bool:
        """Returns True if parameter is defined in the resource file"""

    def GetReal(self, param: str) -> tuple[bool, float]: ...

    def GetInteger(self, param: str) -> tuple[bool, int]: ...

    def GetBoolean(self, param: str) -> tuple[bool, bool]: ...

    def GetString(self, param: str, val: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Get value of parameter as being of specific type
        Returns False if parameter is not defined or has a wrong type
        """

    def RealVal(self, param: str, def: float) -> float: ...

    def IntegerVal(self, param: str, def: int) -> int: ...

    def BooleanVal(self, param: str, def: bool) -> bool: ...

    def StringVal(self, param: str, def: str) -> str:
        """
        Get value of parameter as being of specific type
        If parameter is not defined or does not have expected
        type, returns default value as specified
        """

    def SetMessenger(self, messenger: nanoocp.Message.Message_Messenger | None) -> None:
        """Sets Messenger used for outputting messages."""

    def Messenger(self) -> nanoocp.Message.Message_Messenger:
        """Returns Messenger used for outputting messages."""

    def SetTraceLevel(self, tracelev: int) -> None:
        """
        Sets trace level used for outputting messages
        - 0: no trace at all
        - 1: errors
        - 2: errors and warnings
        - 3: all messages
        Default is 1 : Errors traced
        """

    def TraceLevel(self) -> int:
        """Returns trace level used for outputting messages."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeProcess_Operator(nanoocp.Standard.Standard_Transient):
    """
    Abstract Operator class providing a tool to
    perform an operation on Context
    """

    def Perform(self, context: ShapeProcess_Context | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Performs operation and eventually records
        changes in the context
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeProcess_OperLibrary:
    """
    Provides a set of following operators

    DirectFaces
    FixShape
    SameParameter
    SetTolerance
    SplitAngle
    BSplineRestriction
    ElementaryToRevolution
    SurfaceToBSpline
    ToBezier
    SplitContinuity
    SplitClosedFaces
    FixWireGaps
    FixFaceSize
    DropSmallEdges
    FixShape
    SplitClosedEdges
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeProcess_OperLibrary) -> None: ...

    @staticmethod
    def Init() -> None:
        """Registers all the operators"""

    @staticmethod
    def ApplyModifier(S: nanoocp.TopoDS.TopoDS_Shape, context: ShapeProcess_ShapeContext | None, M: nanoocp.BRepTools.BRepTools_Modification | None, map: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], msg: nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator | None = None, theMutableInput: bool = False) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Applies BRepTools_Modification to a shape,
        taking into account sharing of components of compounds.
        if theMutableInput vat is set to true then input shape S
        can be modified during the modification process.
        """

class ShapeProcess_ShapeContext(ShapeProcess_Context):
    """
    Extends Context to handle shapes
    Contains map of shape-shape, and messages
    attached to shapes
    """

    @overload
    def __init__(self, file: str, seq: str = '') -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, file: str, seq: str = '') -> None:
        """
        Initializes a tool by resource file and shape
        to be processed
        """

    @overload
    def __init__(self, theOther: ShapeProcess_ShapeContext) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes tool by a new shape and clears all results"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns shape being processed"""

    def Result(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns current result"""

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """
        Returns map of replacements shape -> shape
        This map is not recursive
        """

    def Messages(self) -> nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator:
        """
        Returns messages recorded during shape processing
        It can be nullified before processing in order to
        avoid recording messages
        """

    def SetDetalisation(self, level: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None: ...

    def GetDetalisation(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        Set and get value for detalisation level
        Only shapes of types from TopoDS_COMPOUND and until
        specified detalisation level will be recorded in maps
        To cancel mapping, use TopAbs_SHAPE
        To force full mapping, use TopAbs_VERTEX
        The default level is TopAbs_FACE
        """

    def SetResult(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets a new result shape
        NOTE: this method should be used very carefully
        to keep consistency of modifications
        It is recommended to use RecordModification() methods
        with explicit definition of mapping from current
        result to a new one
        """

    @overload
    def RecordModification(self, repl: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], msg: nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator | None = None) -> None: ...

    @overload
    def RecordModification(self, repl: nanoocp.ShapeBuild.ShapeBuild_ReShape | None, msg: nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator | None) -> None: ...

    @overload
    def RecordModification(self, repl: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> None: ...

    @overload
    def RecordModification(self, sh: nanoocp.TopoDS.TopoDS_Shape, repl: nanoocp.BRepTools.BRepTools_Modifier, msg: nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator | None = None) -> None:
        """
        Records modifications and resets result accordingly
        NOTE: modification of resulting shape should be explicitly
        defined in the maps along with modifications of subshapes

        In the last function, sh is the shape on which Modifier
        was run. It can be different from the whole shape,
        but in that case result as a whole should be reset later
        either by call to SetResult(), or by another call to
        RecordModification() which contains mapping of current
        result to a new one explicitly
        """

    def AddMessage(self, S: nanoocp.TopoDS.TopoDS_Shape, msg: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity = Message_Gravity.Message_Warning) -> None:
        """
        Record a message for shape S
        Shape S should be one of subshapes of original shape
        (or whole one), but not one of intermediate shapes
        Records only if Message() is not Null
        """

    def GetContinuity(self, param: str) -> tuple[bool, nanoocp.GeomAbs.GeomAbs_Shape]:
        """
        Get value of parameter as being of the type GeomAbs_Shape
        Returns False if parameter is not defined or has a wrong type
        """

    def ContinuityVal(self, param: str, def: nanoocp.GeomAbs.GeomAbs_Shape) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Get value of parameter as being of the type GeomAbs_Shape
        If parameter is not defined or does not have expected
        type, returns default value as specified
        """

    def PrintStatistics(self) -> None:
        """Prints statistics on Shape Processing onto the current Messenger."""

    def SetNonManifold(self, theNonManifold: bool) -> None:
        """Set NonManifold flag"""

    def IsNonManifold(self) -> bool:
        """Get NonManifold flag"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeProcess_UOperator(ShapeProcess_Operator):
    """
    Defines operator as container for static function
    OperFunc. This allows user to create new operators
    without creation of new classes
    """

    def __init__(self, theOther: ShapeProcess_UOperator) -> None: ...

    def Perform(self, context: ShapeProcess_Context | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """Performs operation and records changes in the context"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
