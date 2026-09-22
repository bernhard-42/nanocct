"""OCCT package Transfer (toolkit TKXSBase)"""

import enum
from typing import overload

import nanoocp.DE
import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard


class Transfer_StatusResult(enum.IntEnum):
    """result status of transferring an entity (see Transcriptor)"""

    Transfer_StatusVoid = 0

    Transfer_StatusDefined = 1

    Transfer_StatusUsed = 2

Transfer_StatusVoid: Transfer_StatusResult = Transfer_StatusResult.Transfer_StatusVoid

Transfer_StatusDefined: Transfer_StatusResult = Transfer_StatusResult.Transfer_StatusDefined

Transfer_StatusUsed: Transfer_StatusResult = Transfer_StatusResult.Transfer_StatusUsed

class Transfer_StatusExec(enum.IntEnum):
    """execution status of an individual transfer (see Transcriptor)"""

    Transfer_StatusInitial = 0

    Transfer_StatusRun = 1

    Transfer_StatusDone = 2

    Transfer_StatusError = 3

    Transfer_StatusLoop = 4

Transfer_StatusInitial: Transfer_StatusExec = Transfer_StatusExec.Transfer_StatusInitial

Transfer_StatusRun: Transfer_StatusExec = Transfer_StatusExec.Transfer_StatusRun

Transfer_StatusDone: Transfer_StatusExec = Transfer_StatusExec.Transfer_StatusDone

Transfer_StatusError: Transfer_StatusExec = Transfer_StatusExec.Transfer_StatusError

Transfer_StatusLoop: Transfer_StatusExec = Transfer_StatusExec.Transfer_StatusLoop

class Transfer_UndefMode(enum.IntEnum):
    """used on processing Undefined Entities (see TransferOutput)"""

    Transfer_UndefIgnore = 0

    Transfer_UndefFailure = 1

    Transfer_UndefContent = 2

    Transfer_UndefUser = 3

Transfer_UndefIgnore: Transfer_UndefMode = Transfer_UndefMode.Transfer_UndefIgnore

Transfer_UndefFailure: Transfer_UndefMode = Transfer_UndefMode.Transfer_UndefFailure

Transfer_UndefContent: Transfer_UndefMode = Transfer_UndefMode.Transfer_UndefContent

Transfer_UndefUser: Transfer_UndefMode = Transfer_UndefMode.Transfer_UndefUser

class Transfer_TransferDispatch(nanoocp.Interface.Interface_CopyTool):
    """
    A TransferDispatch is aimed to dispatch Entities between two
    Interface Models, by default by copying them, as CopyTool, but
    with more capabilities of adapting : Copy is redefined to
    firstly pass the hand to a TransferProcess. If this gives no
    result, standard Copy is called.

    This allow, for instance, to modify the copied Entity (such as
    changing a Name for a VDA Entity), or to do a deeper work
    (such as Substituting a kind of Entity to another one).

    For these reasons, TransferDispatch is basically a CopyTool,
    but uses a more sophiscated control, which is TransferProcess,
    and its method Copy is redefined
    """

    @overload
    def __init__(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Same as above, but works with the Active Protocol"""

    @overload
    def __init__(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None, lib: nanoocp.Interface.Interface_GeneralLib) -> None:
        """
        Creates a TransferDispatch from a Model. Works with a General
        Service Library, given as an Argument
        A TransferDispatch is created as a CopyTool in which the
        Control is set to TransientProcess
        """

    @overload
    def __init__(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None) -> None:
        """Same as above, but Library is defined through a Protocol"""

    @overload
    def __init__(self, theOther: Transfer_TransferDispatch) -> None: ...

    def TransientProcess(self) -> Transfer_TransientProcess:
        """Returns the content of Control Object, as a TransientProcess"""

    def Copy(self, entfrom: nanoocp.Standard.Standard_Transient | None, mapped: bool, errstat: bool) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Copies an Entity by calling the method Transferring from the
        TransferProcess. If this called produces a Null Binder, then
        the standard, inherited Copy is called
        """

class Transfer_Binder(nanoocp.Standard.Standard_Transient):
    """
    A Binder is an auxiliary object to Map the Result of the
    Transfer of a given Object : it records the Result of the
    Unitary Transfer (Resulting Object), status of progress and
    error (if any) of the Process

    The class Binder itself makes no definition for the Result :
    it is defined by sub-classes : it can be either Simple (and
    has to be typed : see generic class SimpleBinder) or Multiple
    (see class MultipleBinder).

    In principle, for a Transfer in progress, Result cannot be
    accessed : this would cause an exception raising.
    This is controlled by the value if StatusResult : if it is
    "Used", the Result cannot be changed. This status is normally
    controlled by TransferProcess but can be directly (see method
    SetAlreadyUsed)

    Checks can be completed by a record of cases, as string which
    can be used as codes, but not to be printed

    In addition to the Result, a Binder can bring a list of
    Attributes, which are additional data, each of them has a name
    """

    def Merge(self, other: Transfer_Binder | None) -> None:
        """
        Merges basic data (Check, ExecStatus) from another Binder but
        keeps its result. Used when a binder is replaced by another
        one, this allows to keep messages
        """

    def IsMultiple(self) -> bool:
        """
        Returns True if a Binder has several results, either by itself
        or because it has next results
        Can be defined by sub-classes.
        """

    def ResultType(self) -> nanoocp.Standard.Standard_Type:
        """Returns the Type which characterizes the Result (if known)"""

    def ResultTypeName(self) -> str:
        """
        Returns the Name of the Type which characterizes the Result
        Can be returned even if ResultType itself is unknown
        """

    def AddResult(self, next: Transfer_Binder | None) -> None:
        """
        Adds a next result (at the end of the list)
        Remark : this information is not processed by Merge
        """

    def NextResult(self) -> Transfer_Binder:
        """Returns the next result, Null if none"""

    def HasResult(self) -> bool:
        """
        Returns True if a Result is available (StatusResult = Defined)
        A Unique Result will be gotten by Result (which must be
        defined in each sub-class according to result type)
        For a Multiple Result, see class MultipleBinder
        For other case, specific access has to be forecast
        """

    def SetAlreadyUsed(self) -> None:
        """
        Declares that result is now used by another one, it means that
        it cannot be modified (by Rebind)
        """

    def Status(self) -> Transfer_StatusResult:
        """
        Returns status, which can be Initial (not yet done), Made (a
        result is recorded, not yet shared), Used (it is shared and
        cannot be modified)
        """

    def StatusExec(self) -> Transfer_StatusExec:
        """Returns execution status"""

    def SetStatusExec(self, stat: Transfer_StatusExec) -> None:
        """
        Modifies execution status; called by TransferProcess only
        (for StatusError, rather use SetError, below)
        """

    def AddFail(self, mess: str, orig: str = '') -> None:
        """
        Used to declare an individual transfer as being erroneous
        (Status is set to Void, StatusExec is set to Error, <errmess>
        is added to Check's list of Fails)
        It is possible to record several messages of error

        It has same effect for TransferProcess as raising an exception
        during the operation of Transfer, except the Transfer tries to
        continue (as if ErrorHandle had been set)
        """

    def AddWarning(self, mess: str, orig: str = '') -> None:
        """
        Used to attach a Warning Message to an individual Transfer
        It has no effect on the Status
        """

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """
        Returns Check which stores Fail messages
        Note that no Entity is associated in this Check
        """

    def CCheck(self) -> nanoocp.Interface.Interface_Check:
        """
        Returns Check which stores Fail messages, in order to modify
        it (adding messages, or replacing it)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ActorOfProcessForTransient(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_ActorOfProcessForTransient) -> None: ...

    def Recognize(self, start: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Prerequisite for Transfer : the method Transfer is
        called on a starting object only if Recognize has
        returned True on it
        This allows to define a list of Actors, each one
        processing a definite kind of data
        TransferProcess calls Recognize on each one before
        calling Transfer. But even if Recognize has returned
        True, Transfer can reject by returning a Null Binder
        (afterwards rejection), the next actor is then invoked

        The provided default returns True, can be redefined
        """

    def Transferring(self, start: nanoocp.Standard.Standard_Transient | None, TP: Transfer_ProcessForTransient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder:
        """
        Specific action of Transfer. The Result is stored in
        the returned Binder, or a Null Handle for "No result"
        (Default defined as doing nothing; should be deferred)
        "mutable" allows the Actor to record intermediate
        information, in addition to those of TransferProcess
        """

    def TransientResult(self, res: nanoocp.Standard.Standard_Transient | None) -> Transfer_SimpleBinderOfTransient:
        """
        Prepares and Returns a Binder for a Transient Result
        Returns a Null Handle if <res> is itself Null
        """

    def NullResult(self) -> Transfer_Binder:
        """Returns a Binder for No Result, i.e. a Null Handle"""

    def SetLast(self, mode: bool = True) -> None:
        """
        If <mode> is True, commands an Actor to be set at the
        end of the list of Actors (see SetNext)
        If it is False (creation default), each add Actor is
        set at the beginning of the list
        This allows to define default Actors (which are Last)
        """

    def IsLast(self) -> bool:
        """Returns the Last status (see SetLast)."""

    def SetNext(self, next: Transfer_ActorOfProcessForTransient | None) -> None:
        """
        Defines a Next Actor : it can then be asked to work if
        <me> produces no result for a given type of Object.
        If Next is already set and is not "Last", calls
        SetNext on it. If Next defined and "Last", the new
        actor is added before it in the list
        """

    def Next(self) -> Transfer_ActorOfProcessForTransient:
        """Returns the Actor defined as Next, or a Null Handle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ActorOfTransientProcess(Transfer_ActorOfProcessForTransient):
    """The original class was renamed. Compatibility only"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_ActorOfTransientProcess) -> None: ...

    def Transferring(self, start: nanoocp.Standard.Standard_Transient | None, TP: Transfer_ProcessForTransient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder: ...

    def Transfer(self, start: nanoocp.Standard.Standard_Transient | None, TP: Transfer_TransientProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder: ...

    def TransferTransient(self, start: nanoocp.Standard.Standard_Transient | None, TP: Transfer_TransientProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Standard.Standard_Transient: ...

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString] = ...) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are copied to the internal map.
        Parameters from @p theAdditionalParameters are copied to the internal map
        if they are not present in @p theParameters.
        @param theParameters the parameters for shape processing.
        @param theAdditionalParameters the additional parameters for shape processing.
        """

    def GetShapeFixParameters(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns parameters for shape processing that was set by SetParameters() method.
        @return the parameters for shape processing. Empty map if no parameters were set.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ActorDispatch(Transfer_ActorOfTransientProcess):
    """
    This class allows to work with a TransferDispatch, i.e. to
    transfer entities from a data set to another one defined by
    the same interface norm, with the following features :
    - ActorDispatch itself acts as a default actor, i.e. it copies
    entities with the general service Copy, as CopyTool does
    - it allows to add other actors for specific ways of transfer,
    which may include data modifications, conversions ...
    - and other features from TransferDispatch (such as mapping
    other than one-one)
    """

    @overload
    def __init__(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Same as above, but works with the Active Protocol"""

    @overload
    def __init__(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None, lib: nanoocp.Interface.Interface_GeneralLib) -> None:
        """
        Creates an ActorDispatch from a Model. Works with a General
        Service Library, given as an Argument
        This causes TransferDispatch and its TransientProcess to be
        created, with default actor <me>
        """

    @overload
    def __init__(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None) -> None:
        """Same as above, but Library is defined through a Protocol"""

    @overload
    def __init__(self, theOther: Transfer_ActorDispatch) -> None: ...

    def AddActor(self, actor: Transfer_ActorOfTransientProcess | None) -> None:
        """
        Utility which adds an actor to the default <me> (it calls
        SetActor from the TransientProcess)
        """

    def TransferDispatch(self) -> Transfer_TransferDispatch:
        """
        Returns the TransferDispatch, which does the work, records
        the intermediate data, etc...
        See TransferDispatch & CopyTool, to see the available methods
        """

    def Transfer(self, start: nanoocp.Standard.Standard_Transient | None, TP: Transfer_TransientProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder:
        """
        Specific action : it calls the method Transfer from CopyTool
        i.e. the general service Copy, then returns the Binder
        produced by the TransientProcess
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_Finder(nanoocp.Standard.Standard_Transient):
    """
    a Finder allows to map any kind of object as a Key for a Map.
    This works by defining, for a Hash Code, that of the real Key,
    not of the Finder which acts only as an intermediate.
    When a Map asks for the HashCode of a Finder, this one returns
    the code it has determined at creation time
    """

    def GetHashCode(self) -> int:
        """
        Returns the HashCode which has been stored by SetHashCode
        (remark that HashCode could be deferred then be defined by
        sub-classes, the result is the same)
        """

    def Equates(self, other: Transfer_Finder | None) -> bool:
        """
        Specific testof equality : to be defined by each sub-class,
        must be False if Finders have not the same true Type, else
        their contents must be compared
        """

    def ValueType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type of the Value. By default, returns the
        DynamicType of <me>, but can be redefined
        """

    def ValueTypeName(self) -> str:
        """
        Returns the name of the Type of the Value. Default is name
        of ValueType, unless it is for a non-handled object
        """

    def SetAttribute(self, name: str, val: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds an attribute with a given name (replaces the former one
        with the same name if already exists)
        """

    def RemoveAttribute(self, name: str) -> bool:
        """
        Removes an attribute
        Returns True when done, False if this attribute did not exist
        """

    def GetAttribute(self, name: str, type: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns an attribute from its name, filtered by a type
        If no attribute has this name, or if it is not kind of this
        type, <val> is Null and returned value is False
        Else, it is True
        """

    def Attribute(self, name: str) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an attribute from its name. Null Handle if not recorded
        (whatever Transient, Integer, Real ...)
        """

    def AttributeType(self, name: str) -> nanoocp.Interface.Interface_ParamType:
        """
        Returns the type of an attribute :
        ParamInt , ParamReal , ParamText (String) , ParamIdent (any)
        or ParamVoid (not recorded)
        """

    def SetIntegerAttribute(self, name: str, val: int) -> None:
        """Adds an integer value for an attribute"""

    def GetIntegerAttribute(self, name: str) -> tuple[bool, int]:
        """
        Returns an attribute from its name, as integer
        If no attribute has this name, or not an integer,
        <val> is 0 and returned value is False
        Else, it is True
        """

    def IntegerAttribute(self, name: str) -> int:
        """Returns an integer attribute from its name. 0 if not recorded"""

    def SetRealAttribute(self, name: str, val: float) -> None:
        """Adds a real value for an attribute"""

    def GetRealAttribute(self, name: str) -> tuple[bool, float]:
        """
        Returns an attribute from its name, as real
        If no attribute has this name, or not a real
        <val> is 0.0 and returned value is False
        Else, it is True
        """

    def RealAttribute(self, name: str) -> float:
        """Returns a real attribute from its name. 0.0 if not recorded"""

    def SetStringAttribute(self, name: str, val: str) -> None:
        """Adds a String value for an attribute"""

    def StringAttribute(self, name: str) -> str:
        """Returns a String attribute from its name. "" if not recorded"""

    def AttrList(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]:
        """Returns the exhaustive list of attributes"""

    def SameAttributes(self, other: Transfer_Finder | None) -> None:
        """
        Gets the list of attributes from <other>, as such, i.e.
        not copied : attributes are shared, any attribute edited,
        added, or removed in <other> is also in <me> and vice versa
        The former list of attributes of <me> is dropped
        """

    def GetAttributes(self, other: Transfer_Finder | None, fromname: str = '', copied: bool = True) -> None:
        """
        Gets the list of attributes from <other>, by copying it
        By default, considers all the attributes from <other>
        If <fromname> is given, considers only the attributes with
        name beginning by <fromname>

        For each attribute, if <copied> is True (D), its value is also
        copied if it is a basic type (Integer,Real,String), else it
        remains shared between <other> and <me>

        These new attributes are added to the existing ones in <me>,
        in case of same name, they replace the existing ones
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_FindHasher:
    """
    FindHasher defines HashCode for Finder, which is : ask a
    Finder its HashCode! Because this is the Finder itself which
    brings the HashCode for its Key

    This class complies to the template given in TCollection by
    MapHasher itself
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_FindHasher) -> None: ...

    @overload
    def __call__(self, theFinder: Transfer_Finder | None) -> int: ...

    @overload
    def __call__(self, theK1: Transfer_Finder | None, theK2: Transfer_Finder | None) -> bool:
        """
        Returns True if two keys are the same.
        The test does not work on the Finders themselves but by
        calling their methods Equates
        """

class Transfer_ActorOfProcessForFinder(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_ActorOfProcessForFinder) -> None: ...

    def Recognize(self, start: Transfer_Finder | None) -> bool:
        """
        Prerequisite for Transfer : the method Transfer is
        called on a starting object only if Recognize has
        returned True on it
        This allows to define a list of Actors, each one
        processing a definite kind of data
        TransferProcess calls Recognize on each one before
        calling Transfer. But even if Recognize has returned
        True, Transfer can reject by returning a Null Binder
        (afterwards rejection), the next actor is then invoked

        The provided default returns True, can be redefined
        """

    def Transferring(self, start: Transfer_Finder | None, TP: Transfer_ProcessForFinder | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder:
        """
        Specific action of Transfer. The Result is stored in
        the returned Binder, or a Null Handle for "No result"
        (Default defined as doing nothing; should be deferred)
        "mutable" allows the Actor to record intermediate
        information, in addition to those of TransferProcess
        """

    def TransientResult(self, res: nanoocp.Standard.Standard_Transient | None) -> Transfer_SimpleBinderOfTransient:
        """
        Prepares and Returns a Binder for a Transient Result
        Returns a Null Handle if <res> is itself Null
        """

    def NullResult(self) -> Transfer_Binder:
        """Returns a Binder for No Result, i.e. a Null Handle"""

    def SetLast(self, mode: bool = True) -> None:
        """
        If <mode> is True, commands an Actor to be set at the
        end of the list of Actors (see SetNext)
        If it is False (creation default), each add Actor is
        set at the beginning of the list
        This allows to define default Actors (which are Last)
        """

    def IsLast(self) -> bool:
        """Returns the Last status (see SetLast)."""

    def SetNext(self, next: Transfer_ActorOfProcessForFinder | None) -> None:
        """
        Defines a Next Actor : it can then be asked to work if
        <me> produces no result for a given type of Object.
        If Next is already set and is not "Last", calls
        SetNext on it. If Next defined and "Last", the new
        actor is added before it in the list
        """

    def Next(self) -> Transfer_ActorOfProcessForFinder:
        """Returns the Actor defined as Next, or a Null Handle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ActorOfFinderProcess(Transfer_ActorOfProcessForFinder):
    """
    The original class was renamed. Compatibility only

    ModeTrans : a simple way of transmitting a transfer mode from
    a user. To be interpreted for each norm
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_ActorOfFinderProcess) -> None: ...

    def ModeTrans(self) -> int:
        """Returns the Transfer Mode, modifiable"""

    def SetModeTrans(self, theValue: int) -> None:
        """
        Python addition: sets the value ModeTrans() returns by reference in C++.
        """

    def Transferring(self, start: Transfer_Finder | None, TP: Transfer_ProcessForFinder | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder: ...

    def Transfer(self, start: Transfer_Finder | None, TP: Transfer_FinderProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder: ...

    def TransferTransient(self, start: nanoocp.Standard.Standard_Transient | None, TP: Transfer_FinderProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Standard.Standard_Transient: ...

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString] = ...) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are copied to the internal map.
        Parameters from @p theAdditionalParameters are copied to the internal map
        if they are not present in @p theParameters.
        @param theParameters the parameters for shape processing.
        @param theAdditionalParameters the additional parameters for shape processing.
        """

    def GetShapeFixParameters(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns parameters for shape processing that was set by SetParameters() method.
        @return the parameters for shape processing. Empty map if no parameters were set.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_SimpleBinderOfTransient(Transfer_Binder):
    """
    An adapted instantiation of SimpleBinder for Transient Result,
    i.e. ResultType can be computed from the Result itself,
    instead of being static
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty SimpleBinderOfTransient
        Returns True if a starting object is bound with SEVERAL
        results : Here, returns always False
        See Binder itself
        """

    @overload
    def __init__(self, theOther: Transfer_SimpleBinderOfTransient) -> None: ...

    def ResultType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Effective (Dynamic) Type of the Result
        (Standard_Transient if no Result is defined)
        """

    def ResultTypeName(self) -> str:
        """
        Returns the Effective Name of (Dynamic) Type of the Result
        (void) if no result is defined
        """

    def SetResult(self, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """Defines the Result"""

    def Result(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the defined Result, if there is one"""

    @staticmethod
    def GetTypedResult(bnd: Transfer_Binder | None, atype: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns a transient result according to its type (IsKind)
        i.e. the result itself if IsKind(atype), else searches in
        NextResult, until first found, then returns True
        If not found, returns False (res is NOT touched)

        This syntactic form avoids to do DownCast : if a result is
        found with the good type, it is loaded in <res> and can be
        immediately used, well initialised
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_BinderOfTransientInteger(Transfer_SimpleBinderOfTransient):
    """
    This type of Binder allows to attach as result, besides a
    Transient Object, an Integer Value, which can be an Index
    in the Object if it defines a List, for instance

    This Binder is otherwise a kind of SimpleBinderOfTransient,
    i.e. its basic result (for iterators, etc) is the Transient
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty BinderOfTransientInteger; Default value for
        the integer part is zero
        """

    @overload
    def __init__(self, theOther: Transfer_BinderOfTransientInteger) -> None: ...

    def SetInteger(self, value: int) -> None:
        """Sets a value for the integer part"""

    def Integer(self) -> int:
        """Returns the value set for the integer part"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_DataInfo:
    """
    Gives information on an object
    Used as template to instantiate Mapper and SimpleBinder
    This class is for Transient
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_DataInfo) -> None: ...

    @staticmethod
    def Type(ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type attached to an object
        Here, the Dynamic Type of a Transient. Null Type if unknown
        """

    @staticmethod
    def TypeName(ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Returns Type Name (string)
        Allows to name type of non-handled objects
        """

class Transfer_DispatchControl(nanoocp.Interface.Interface_CopyControl):
    """
    This is an auxiliary class for TransferDispatch, which allows
    to record simple copies, as CopyControl from Interface, but
    based on a TransientProcess. Hence, it allows in addition
    more actions (such as recording results of adaptations)
    """

    @overload
    def __init__(self, model: nanoocp.Interface.Interface_InterfaceModel | None, TP: Transfer_TransientProcess | None) -> None:
        """Creates the DispatchControl, ready for use"""

    @overload
    def __init__(self, theOther: Transfer_DispatchControl) -> None: ...

    def TransientProcess(self) -> Transfer_TransientProcess:
        """
        Returns the content of the DispatchControl : it can be used
        for a direct call, if the basic methods do not suffice
        """

    def StartingModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model from which the transfer is to be done"""

    def Clear(self) -> None:
        """Clears the List of Copied Results"""

    def Bind(self, ent: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """Binds a (Transient) Result to a (Transient) Starting Entity"""

    def Search(self, ent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Searches for the Result bound to a Starting Entity
        If Found, returns True and fills <res>
        Else, returns False and nullifies <res>
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ProcessForFinder(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, nb: int = 10000) -> None:
        """
        Sets TransferProcess at initial state. Gives an Initial size
        (indicative) for the Map when known (default is 10000).
        Sets default trace file as a printer and default trace level
        (see Message_TraceFile).
        """

    @overload
    def __init__(self, printer: nanoocp.Message.Message_Messenger | None, nb: int = 10000) -> None:
        """
        Sets TransferProcess at initial state. Gives an Initial size
        (indicative) for the Map when known (default is 10000).
        Sets a specified printer.
        """

    @overload
    def __init__(self, theOther: Transfer_ProcessForFinder) -> None: ...

    def Clear(self) -> None:
        """
        Resets a TransferProcess as ready for a completely new work.
        Clears general data (roots) and the Map
        """

    def Clean(self) -> None:
        """
        Rebuilds the Map and the roots to really remove Unbound items
        Because Unbind keeps the entity in place, even if not bound
        Hence, working by checking new items is meaningless if a
        formerly unbound item is rebound
        """

    def Resize(self, nb: int) -> None:
        """
        Resizes the Map as required (if a new reliable value has been
        determined). Acts only if <nb> is greater than actual NbMapped
        """

    def SetActor(self, actor: Transfer_ActorOfProcessForFinder | None) -> None:
        """
        Defines an Actor, which is used for automatic Transfer
        If already defined, the new Actor is cumulated
        (see SetNext from Actor)
        """

    def Actor(self) -> Transfer_ActorOfProcessForFinder:
        """
        Returns the defined Actor. Returns a Null Handle if
        not set.
        """

    def Find(self, start: Transfer_Finder | None) -> Transfer_Binder:
        """
        Returns the Binder which is linked with a starting Object
        It can either bring a Result (Transfer done) or none (for a
        pre-binding).
        If no Binder is linked with <start>, returns a Null Handle
        Considers a category number, by default 0
        """

    def IsBound(self, start: Transfer_Finder | None) -> bool:
        """
        Returns True if a Result (whatever its form) is Bound with
        a starting Object. I.e., if a Binder with a Result set,
        is linked with it
        Considers a category number, by default 0
        """

    def IsAlreadyUsed(self, start: Transfer_Finder | None) -> bool:
        """
        Returns True if the result of the transfer of an object is
        already used in other ones. If it is, Rebind cannot change it.
        Considers a category number, by default 0
        """

    def Bind(self, start: Transfer_Finder | None, binder: Transfer_Binder | None) -> None:
        """
        Creates a Link a starting Object with a Binder. This Binder
        can either bring a Result (effective Binding) or none (it can
        be set later : pre-binding).
        Considers a category number, by default 0
        """

    def Rebind(self, start: Transfer_Finder | None, binder: Transfer_Binder | None) -> None:
        """
        Changes the Binder linked with a starting Object for its
        unitary transfer. This it can be useful when the exact form
        of the result is known once the transfer is widely engaged.
        This can be done only on first transfer.
        Considers a category number, by default 0
        """

    def Unbind(self, start: Transfer_Finder | None) -> bool:
        """
        Removes the Binder linked with a starting object
        If this Binder brings a non-empty Check, it is replaced by
        a VoidBinder. Also removes from the list of Roots as required.
        Returns True if done, False if <start> was not bound
        Considers a category number, by default 0
        """

    def FindElseBind(self, start: Transfer_Finder | None) -> Transfer_Binder:
        """
        Returns a Binder for a starting entity, as follows :
        Tries to Find the already bound one
        If none found, creates a VoidBinder and Binds it
        """

    def SetMessenger(self, messenger: nanoocp.Message.Message_Messenger | None) -> None:
        """Sets Messenger used for outputting messages."""

    def Messenger(self) -> nanoocp.Message.Message_Messenger:
        """
        Returns Messenger used for outputting messages.
        The returned object is guaranteed to be non-null;
        default is Message::Messenger().
        """

    def SetTraceLevel(self, tracelev: int) -> None:
        """
        Sets trace level used for outputting messages:
        <trace> = 0 : no trace at all
        <trace> = 1 : handled exceptions and calls to AddError
        <trace> = 2 : also calls to AddWarning
        <trace> = 3 : also traces new Roots
        (uses method ErrorTrace).
        Default is 1 : Errors traced
        """

    def TraceLevel(self) -> int:
        """Returns trace level used for outputting messages."""

    def SendFail(self, start: Transfer_Finder | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """New name for AddFail (Msg)"""

    def SendWarning(self, start: Transfer_Finder | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """New name for AddWarning (Msg)"""

    def SendMsg(self, start: Transfer_Finder | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Adds an information message
        Trace is filled if trace level is at least 3
        """

    @overload
    def AddFail(self, start: Transfer_Finder | None, mess: str, orig: str = '') -> None:
        """
        Adds an Error message to a starting entity (to the check of
        its Binder of category 0, as a Fail)
        """

    @overload
    def AddFail(self, start: Transfer_Finder | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Adds an Error Message to a starting entity from the definition
        of a Msg (Original+Value)
        """

    def AddError(self, start: Transfer_Finder | None, mess: str, orig: str = '') -> None:
        """(other name of AddFail, maintained for compatibility)"""

    @overload
    def AddWarning(self, start: Transfer_Finder | None, mess: str, orig: str = '') -> None:
        """
        Adds a Warning message to a starting entity (to the check of
        its Binder of category 0)
        """

    @overload
    def AddWarning(self, start: Transfer_Finder | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Adds a Warning Message to a starting entity from the definition
        of a Msg (Original+Value)
        """

    def Mend(self, start: Transfer_Finder | None, pref: str = '') -> None: ...

    def Check(self, start: Transfer_Finder | None) -> nanoocp.Interface.Interface_Check:
        """
        Returns the Check attached to a starting entity. If <start>
        is unknown, returns an empty Check
        Adds a case name to a starting entity
        Adds a case value to a starting entity
        Returns the complete case list for an entity. Null Handle if empty
        In the list of mapped items (between 1 and NbMapped),
        searches for the first item which follows <num0>(not included)
        and which has an attribute named <name>
        Attributes are brought by Binders
        Hence, allows such an iteration

        for (num = TP->NextItemWithAttribute(name,0);
        num > 0;
        num = TP->NextItemWithAttribute(name,num) {
        .. process mapped item <num>
        }
        Returns the type of an Attribute attached to binders
        If this name gives no Attribute, returns ParamVoid
        If this name gives several different types, returns ParamMisc
        Else, returns the effective type (ParamInteger, ParamReal,
        ParamIdent, or ParamText)
        Returns the list of recorded Attribute Names, as a Dictionary
        of Integer : each value gives the count of items which bring
        this attribute name
        By default, considers all the attribute names
        If <rootname> is given, considers only the attribute names
        which begin by <rootname>
        """

    def BindTransient(self, start: Transfer_Finder | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Binds a starting object with a Transient Result.
        Uses a SimpleBinderOfTransient to work. If there is already
        one but with no Result set, sets its Result.
        Considers a category number, by default 0
        """

    def FindTransient(self, start: Transfer_Finder | None) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Result of the Transfer of an object <start> as a
        Transient Result.
        Returns a Null Handle if there is no Transient Result
        Considers a category number, by default 0
        Warning : Supposes that Binding is done with a SimpleBinderOfTransient
        """

    def BindMultiple(self, start: Transfer_Finder | None) -> None:
        """
        Prepares an object <start> to be bound with several results.
        If no Binder is yet attached to <obj>, a MultipleBinder
        is created, empty. If a Binder is already set, it must
        accept Multiple Binding.
        Considers a category number, by default 0
        """

    def AddMultiple(self, start: Transfer_Finder | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds an item to a list of results bound to a starting object.
        Considers a category number, by default 0, for all results
        """

    def FindTypedTransient(self, start: Transfer_Finder | None, atype: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Searches for a transient result attached to a starting object,
        according to its type, by criterium IsKind(atype)

        In case of multiple result, explores the list and gives in
        <val> the first transient result IsKind(atype)
        Returns True and fills <val> if found
        Else, returns False (<val> is not touched, not even nullified)

        This syntactic form avoids to do DownCast : if a result is
        found with the good type, it is loaded in <val> and can be
        immediately used, well initialised
        """

    def GetTypedTransient(self, binder: Transfer_Binder | None, atype: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Searches for a transient result recorded in a Binder, whatever
        this Binder is recorded or not in <me>

        This is strictly equivalent to the class method GetTypedResult
        from class SimpleBinderOfTransient, but is just lighter to call

        Apart from this, works as FindTypedTransient
        """

    def NbMapped(self) -> int:
        """
        Returns the maximum possible value for Map Index
        (no result can be bound with a value greater than it)
        """

    def Mapped(self, num: int) -> Transfer_Finder:
        """Returns the Starting Object bound to an Index,"""

    def MapIndex(self, start: Transfer_Finder | None) -> int:
        """Returns the Index value bound to a Starting Object, 0 if none"""

    def MapItem(self, num: int) -> Transfer_Binder:
        """
        Returns the Binder bound to an Index
        Considers a category number, by default 0
        """

    def SetRoot(self, start: Transfer_Finder | None) -> None:
        """
        Declares <obj> (and its Result) as Root. This status will be
        later exploited by RootResult, see below (Result can be
        produced at any time)
        """

    def SetRootManagement(self, stat: bool) -> None:
        """
        Enable (if <stat> True) or Disables (if <stat> False) Root
        Management. If it is set, Transfers are considered as stacked
        (a first Transfer commands other Transfers, and so on) and
        the Transfers commanded by an external caller are "Root".
        Remark : SetRoot can be called whatever this status, on every
        object.
        Default is set to True.
        """

    def NbRoots(self) -> int:
        """Returns the count of recorded Roots"""

    def Root(self, num: int) -> Transfer_Finder:
        """Returns a Root Entity given its number in the list (1-NbRoots)"""

    def RootItem(self, num: int) -> Transfer_Binder:
        """
        Returns the Binder bound with a Root Entity given its number
        Considers a category number, by default 0
        """

    def RootIndex(self, start: Transfer_Finder | None) -> int:
        """
        Returns the index in the list of roots for a starting item,
        or 0 if it is not recorded as a root
        """

    def NestingLevel(self) -> int:
        """
        Returns Nesting Level of Transfers (managed by methods
        TranscriptWith & Co). Starts to zero. If no automatic Transfer
        is used, it remains to zero. Zero means Root Level.
        """

    def ResetNestingLevel(self) -> None:
        """
        Resets Nesting Level of Transfers to Zero (Root Level),
        whatever its current value.
        """

    def Recognize(self, start: Transfer_Finder | None) -> bool:
        """
        Tells if <start> has been recognized as good candidate for
        Transfer. i.e. queries the Actor and its Nexts
        """

    def Transferring(self, start: Transfer_Finder | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder:
        """
        Performs the Transfer of a Starting Object, by calling
        the method TransferProduct (see below).
        Mapping and Roots are managed : nothing is done if a Result is
        already Bound, an exception is raised in case of error.
        """

    def Transfer(self, start: Transfer_Finder | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Same as Transferring but does not return the Binder.
        Simply returns True in case of success (for user call)
        """

    def SetErrorHandle(self, err: bool) -> None:
        """
        Allows controls if exceptions will be handled
        Transfer Operations
        <err> False : they are not handled with try {} catch {}
        <err> True  : they are
        Default is False: no handling performed
        """

    def ErrorHandle(self) -> bool:
        """Returns error handling flag"""

    def StartTrace(self, binder: Transfer_Binder | None, start: Transfer_Finder | None, level: int, mode: int) -> None:
        """
        Method called when trace is asked
        Calls PrintTrace to display information relevant for starting
        objects (which can be redefined)
        <level> is Nesting Level of Transfer (0 = root)
        <mode> controls the way the trace is done :
        0 neutral, 1 for Error, 2 for Warning message, 3 for new Root
        """

    def PrintTrace(self, start: Transfer_Finder | None) -> str:
        """
        Prints a short information on a starting object. By default
        prints its Dynamic Type. Can be redefined
        """

    def IsLooping(self, alevel: int) -> bool:
        """
        Returns True if we are surely in a DeadLoop. Evaluation is not
        exact, it is a "majorant" which must be computed fast.
        This "majorant" is : <alevel> greater than NbMapped.
        """

    def RootResult(self, withstart: bool = False) -> Transfer_IteratorOfProcessForFinder:
        """
        Returns, as an iterator, the log of root transfer, i.e. the
        created objects and Binders bound to starting roots
        If withstart is given True, Starting Objects are also returned
        """

    def CompleteResult(self, withstart: bool = False) -> Transfer_IteratorOfProcessForFinder:
        """
        Returns, as an Iterator, the entire log of transfer (list of
        created objects and Binders which can bring errors)
        If withstart is given True, Starting Objects are also returned
        """

    def AbnormalResult(self) -> Transfer_IteratorOfProcessForFinder:
        """
        Returns Binders which are neither "Done" nor "Initial",
        that is Error,Loop or Run (abnormal states at end of Transfer)
        Starting Objects are given in correspondence in the iterator
        """

    def CheckList(self, erronly: bool) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns a CheckList as a list of Check : each one is for a
        starting entity which have either check (warning or fail)
        messages are attached, or are in abnormal state : that case
        gives a specific message
        If <erronly> is True, checks with Warnings only are ignored
        """

    def ResultOne(self, start: Transfer_Finder | None, level: int, withstart: bool = False) -> Transfer_IteratorOfProcessForFinder:
        """
        Returns, as an Iterator, the log of transfer for one object
        <level> = 0 : this object only
        and if <start> is a scope owner (else, <level> is ignored) :
        <level> = 1 : object plus its immediate scoped ones
        <level> = 2 : object plus all its scoped ones
        """

    def CheckListOne(self, start: Transfer_Finder | None, level: int, erronly: bool) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns a CheckList for one starting object
        <level> interpreted as by ResultOne
        If <erronly> is True, checks with Warnings only are ignored
        """

    def IsCheckListEmpty(self, start: Transfer_Finder | None, level: int, erronly: bool) -> bool:
        """
        Returns True if no check message is attached to a starting
        object. <level> interpreted as by ResultOne
        If <erronly> is True, checks with Warnings only are ignored
        """

    def RemoveResult(self, start: Transfer_Finder | None, level: int, compute: bool = True) -> None:
        """
        Removes Results attached to (== Unbinds) a given object and,
        according <level> :
        <level> = 0 : only it
        <level> = 1 : it plus its immediately owned sub-results(scope)
        <level> = 2 : it plus all its owned sub-results(scope)
        """

    def CheckNum(self, start: Transfer_Finder | None) -> int:
        """
        Computes a number to be associated to a starting object in
        a check or a check-list
        By default, returns 0; can be redefined
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_FinderProcess(Transfer_ProcessForFinder):
    """
    Adds specific features to the generic definition :
    PrintTrace is adapted
    """

    @overload
    def __init__(self, nb: int = 10000) -> None:
        """Sets FinderProcess at initial state, with an initial size"""

    @overload
    def __init__(self, theOther: Transfer_FinderProcess) -> None: ...

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Sets an InterfaceModel, which can be used during transfer
        for instance if a context must be managed, it is in the Model
        """

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model which can be used for context"""

    def NextMappedWithAttribute(self, name: str, num0: int) -> int:
        """
        In the list of mapped items (between 1 and NbMapped),
        searches for the first mapped item which follows <num0>
        (not included) and which has an attribute named <name>
        The considered Attributes are those brought by Finders,i.e.
        by Input data.
        While NextItemWithAttribute works on Result data (Binders)

        Hence, allows such an iteration

        for (num = FP->NextMappedWithAttribute(name,0);
        num > 0;
        num = FP->NextMappedWithAttribute(name,num) {
        .. process mapped item <num>
        }
        """

    def TransientMapper(self, obj: nanoocp.Standard.Standard_Transient | None) -> Transfer_TransientMapper:
        """
        Returns a TransientMapper for a given Transient Object
        Either <obj> is already mapped, then its Mapper is returned
        Or it is not, then a new one is created then returned, BUT
        it is not mapped here (use Bind or FindElseBind to do this)
        """

    def PrintTrace(self, start: Transfer_Finder | None) -> str:
        """Specific printing to trace a Finder (by its method ValueType)"""

    def PrintStats(self, mode: int) -> str:
        """Prints statistics on a given output, according mode"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_TransferIterator:
    """
    Defines an Iterator on the result of a Transfer
    Available for Normal Results or not (Erroneous Transfer)
    It gives several kinds of Information, and allows to consider
    various criteria (criteria are cumulative)
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty Iterator"""

    @overload
    def __init__(self, theOther: Transfer_TransferIterator) -> None: ...

    def __iter__(self) -> Transfer_TransferIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> Transfer_Binder:
        """Python addition: see __iter__."""

    def AddItem(self, atr: Transfer_Binder | None) -> None:
        """Adds a Binder to the iteration list (construction)"""

    def SelectBinder(self, atype: nanoocp.Standard.Standard_Type | None, keep: bool) -> None:
        """
        Selects Items on the Type of Binder : keep only
        Binders which are of a given Type (if keep is True) or
        reject only them (if keep is False)
        """

    def SelectResult(self, atype: nanoocp.Standard.Standard_Type | None, keep: bool) -> None:
        """
        Selects Items on the Type of Result. Considers only Unique
        Results. Considers Dynamic Type for Transient Result,
        Static Type (the one given to define the Binder) else.

        Results which are of a given Type (if keep is True) or reject
        only them (if keep is False)
        """

    def SelectUnique(self, keep: bool) -> None:
        """
        Select Items according Unicity : keep only Unique Results (if
        keep is True) or keep only Multiple Results (if keep is False)
        """

    def SelectItem(self, num: int, keep: bool) -> None:
        """
        Selects/Unselect (according to <keep> an item designated by
        its rank <num> in the list
        Used by sub-classes which have specific criteria
        """

    def Number(self) -> int:
        """Returns count of Binders to be iterated"""

    def Start(self) -> None:
        """Clears Iteration in progress, to allow it to be restarted"""

    def More(self) -> bool:
        """Returns True if there are other Items to iterate"""

    def Next(self) -> None:
        """Sets Iteration to the next Item"""

    def Value(self) -> Transfer_Binder:
        """Returns the current Binder"""

    def HasResult(self) -> bool:
        """
        Returns True if current Item brings a Result, Transient
        (Handle) or not or Multiple. That is to say, if it corresponds
        to a normally achieved Transfer, Transient Result is read by
        specific TransientResult below.
        Other kind of Result must be read specifically from its Binder
        """

    def HasUniqueResult(self) -> bool:
        """Returns True if Current Item has a Unique Result"""

    def ResultType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type of the Result of the current Item, if Unique.
        If No Unique Result (Error Transfer or Multiple Result),
        returns a Null Handle
        The Type is : the Dynamic Type for a Transient Result,
        the Type defined by the Binder Class else
        """

    def HasTransientResult(self) -> bool:
        """
        Returns True if the current Item has a Transient Unique
        Result (if yes, use TransientResult to get it)
        """

    def TransientResult(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Transient Result of the current Item if there is
        (else, returns a null Handle)
        Supposes that Binding is done by a SimpleBinderOfTransient
        """

    def Status(self) -> Transfer_StatusExec:
        """
        Returns Execution Status of current Binder
        Normal transfer corresponds to StatusDone
        """

    def HasFails(self) -> bool:
        """
        Returns True if Fail Messages are recorded with the current
        Binder. They can then be read through Check (see below)
        """

    def HasWarnings(self) -> bool:
        """
        Returns True if Warning Messages are recorded with the current
        Binder. They can then be read through Check (see below)
        """

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """
        Returns Check associated to current Binder
        (in case of error, it brings Fail messages)
        (in case of warnings, it brings Warning messages)
        """

class Transfer_IteratorOfProcessForFinder(Transfer_TransferIterator):
    @overload
    def __init__(self, withstarts: bool) -> None:
        """
        Creates an empty Iterator
        if withstarts is True, each Binder to be iterated will
        be associated to its corresponding Starting Object
        """

    @overload
    def __init__(self, theOther: Transfer_IteratorOfProcessForFinder) -> None: ...

    @overload
    def Add(self, binder: Transfer_Binder | None) -> None:
        """
        Adds a Binder to the iteration list (construction)
        with no corresponding Starting Object
        (note that Result is brought by Binder)
        """

    @overload
    def Add(self, binder: Transfer_Binder | None, start: Transfer_Finder | None) -> None:
        """
        Adds a Binder to the iteration list, associated with
        its corresponding Starting Object "start"
        Starting Object is ignored if not required at
        Creation time
        """

    def Filter(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Transfer.Transfer_Finder] | None, keep: bool = True) -> None:
        """
        After having added all items, keeps or rejects items
        which are attached to starting data given by <only>
        <keep> = True (D) : keeps. <keep> = False : rejects
        Does nothing if <withstarts> was False
        """

    def HasStarting(self) -> bool:
        """
        Returns True if Starting Object is available
        (defined at Creation Time)
        """

    def Starting(self) -> Transfer_Finder:
        """Returns corresponding Starting Object"""

class Transfer_IteratorOfProcessForTransient(Transfer_TransferIterator):
    @overload
    def __init__(self, withstarts: bool) -> None:
        """
        Creates an empty Iterator
        if withstarts is True, each Binder to be iterated will
        be associated to its corresponding Starting Object
        """

    @overload
    def __init__(self, theOther: Transfer_IteratorOfProcessForTransient) -> None: ...

    @overload
    def Add(self, binder: Transfer_Binder | None) -> None:
        """
        Adds a Binder to the iteration list (construction)
        with no corresponding Starting Object
        (note that Result is brought by Binder)
        """

    @overload
    def Add(self, binder: Transfer_Binder | None, start: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds a Binder to the iteration list, associated with
        its corresponding Starting Object "start"
        Starting Object is ignored if not required at
        Creation time
        """

    def Filter(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, keep: bool = True) -> None:
        """
        After having added all items, keeps or rejects items
        which are attached to starting data given by <only>
        <keep> = True (D) : keeps. <keep> = False : rejects
        Does nothing if <withstarts> was False
        """

    def HasStarting(self) -> bool:
        """
        Returns True if Starting Object is available
        (defined at Creation Time)
        """

    def Starting(self) -> nanoocp.Standard.Standard_Transient:
        """Returns corresponding Starting Object"""

class Transfer_MapContainer(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_MapContainer) -> None: ...

    def SetMapObjects(self, theMapObjects: nanoocp.NCollection.NCollection_DataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]) -> None:
        """Set map already translated geometry objects."""

    def GetMapObjects(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]:
        """Get map already translated geometry objects."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_MultipleBinder(Transfer_Binder):
    """
    Allows direct binding between a starting Object and the Result
    of its transfer, when it can be made of several Transient
    Objects. Compared to a Transcriptor, it has no Transfer Action

    Result is a list of Transient Results. Unique Result is not
    available : SetResult is redefined to start the list on the
    first call, and refuse the other times.

    rr

    Remark : MultipleBinder itself is intended to be created and
    filled by TransferProcess itself (method Bind). In particular,
    conflicts between Unique (Standard) result and Multiple result
    are avoided through management made by TransferProcess.

    Also, a Transcriptor (with an effective Transfer Method) which
    can produce a Multiple Result, may be defined as a sub-class
    of MultipleBinder by redefining method Transfer.
    """

    @overload
    def __init__(self) -> None:
        """normal standard constructor, creates an empty MultipleBinder"""

    @overload
    def __init__(self, theOther: Transfer_MultipleBinder) -> None: ...

    def IsMultiple(self) -> bool:
        """
        Returns True if a starting object is bound with SEVERAL
        results : Here, returns always True
        """

    def ResultType(self) -> nanoocp.Standard.Standard_Type:
        """Returns the Type permitted for Results, i.e. here Transient"""

    def ResultTypeName(self) -> str:
        """
        Returns the Name of the Type which characterizes the Result
        Here, returns "(list)\"
        """

    def AddResult(self, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds a new Item to the Multiple Result"""

    def NbResults(self) -> int:
        """Returns the actual count of recorded (Transient) results"""

    def ResultValue(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns the value of the recorded result n0 <num>"""

    def MultipleResult(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the Multiple Result, if it is defined (at least one
        Item). Else, returns a Null Handle
        """

    def SetMultipleResult(self, mulres: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None:
        """
        Defines a Binding with a Multiple Result, given as a Sequence
        Error if a Unique Result has yet been defined
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ProcessForTransient(nanoocp.Standard.Standard_Transient):
    """
    Manages Transfer of Transient Objects. Produces also
    ActorOfTransientProcess       (deferred class),
    IteratorOfTransientProcess    (for Results),
    TransferMapOfTransientProcess (internally used)
    Normally uses as TransientProcess, which adds some specifics
    """

    @overload
    def __init__(self, nb: int = 10000) -> None:
        """
        Sets TransferProcess at initial state. Gives an Initial size
        (indicative) for the Map when known (default is 10000).
        Sets default trace file as a printer and default trace level
        (see Message_TraceFile).
        """

    @overload
    def __init__(self, printer: nanoocp.Message.Message_Messenger | None, nb: int = 10000) -> None:
        """
        Sets TransferProcess at initial state. Gives an Initial size
        (indicative) for the Map when known (default is 10000).
        Sets a specified printer.
        """

    @overload
    def __init__(self, theOther: Transfer_ProcessForTransient) -> None: ...

    def Clear(self) -> None:
        """
        Resets a TransferProcess as ready for a completely new work.
        Clears general data (roots) and the Map
        """

    def Clean(self) -> None:
        """
        Rebuilds the Map and the roots to really remove Unbound items
        Because Unbind keeps the entity in place, even if not bound
        Hence, working by checking new items is meaningless if a
        formerly unbound item is rebound
        """

    def Resize(self, nb: int) -> None:
        """
        Resizes the Map as required (if a new reliable value has been
        determined). Acts only if <nb> is greater than actual NbMapped
        """

    def SetActor(self, actor: Transfer_ActorOfProcessForTransient | None) -> None:
        """
        Defines an Actor, which is used for automatic Transfer
        If already defined, the new Actor is cumulated
        (see SetNext from Actor)
        """

    def Actor(self) -> Transfer_ActorOfProcessForTransient:
        """
        Returns the defined Actor. Returns a Null Handle if
        not set.
        """

    def Find(self, start: nanoocp.Standard.Standard_Transient | None) -> Transfer_Binder:
        """
        Returns the Binder which is linked with a starting Object
        It can either bring a Result (Transfer done) or none (for a
        pre-binding).
        If no Binder is linked with <start>, returns a Null Handle
        Considers a category number, by default 0
        """

    def IsBound(self, start: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if a Result (whatever its form) is Bound with
        a starting Object. I.e., if a Binder with a Result set,
        is linked with it
        Considers a category number, by default 0
        """

    def IsAlreadyUsed(self, start: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if the result of the transfer of an object is
        already used in other ones. If it is, Rebind cannot change it.
        Considers a category number, by default 0
        """

    def Bind(self, start: nanoocp.Standard.Standard_Transient | None, binder: Transfer_Binder | None) -> None:
        """
        Creates a Link a starting Object with a Binder. This Binder
        can either bring a Result (effective Binding) or none (it can
        be set later : pre-binding).
        Considers a category number, by default 0
        """

    def Rebind(self, start: nanoocp.Standard.Standard_Transient | None, binder: Transfer_Binder | None) -> None:
        """
        Changes the Binder linked with a starting Object for its
        unitary transfer. This it can be useful when the exact form
        of the result is known once the transfer is widely engaged.
        This can be done only on first transfer.
        Considers a category number, by default 0
        """

    def Unbind(self, start: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Removes the Binder linked with a starting object
        If this Binder brings a non-empty Check, it is replaced by
        a VoidBinder. Also removes from the list of Roots as required.
        Returns True if done, False if <start> was not bound
        Considers a category number, by default 0
        """

    def FindElseBind(self, start: nanoocp.Standard.Standard_Transient | None) -> Transfer_Binder:
        """
        Returns a Binder for a starting entity, as follows :
        Tries to Find the already bound one
        If none found, creates a VoidBinder and Binds it
        """

    def SetMessenger(self, messenger: nanoocp.Message.Message_Messenger | None) -> None:
        """Sets Messenger used for outputting messages."""

    def Messenger(self) -> nanoocp.Message.Message_Messenger:
        """
        Returns Messenger used for outputting messages.
        The returned object is guaranteed to be non-null;
        default is Message::Messenger().
        """

    def SetTraceLevel(self, tracelev: int) -> None:
        """
        Sets trace level used for outputting messages:
        <trace> = 0 : no trace at all
        <trace> = 1 : handled exceptions and calls to AddError
        <trace> = 2 : also calls to AddWarning
        <trace> = 3 : also traces new Roots
        (uses method ErrorTrace).
        Default is 1 : Errors traced
        """

    def TraceLevel(self) -> int:
        """Returns trace level used for outputting messages."""

    def SendFail(self, start: nanoocp.Standard.Standard_Transient | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """New name for AddFail (Msg)"""

    def SendWarning(self, start: nanoocp.Standard.Standard_Transient | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """New name for AddWarning (Msg)"""

    def SendMsg(self, start: nanoocp.Standard.Standard_Transient | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Adds an information message
        Trace is filled if trace level is at least 3
        """

    @overload
    def AddFail(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """
        Adds an Error message to a starting entity (to the check of
        its Binder of category 0, as a Fail)
        """

    @overload
    def AddFail(self, start: nanoocp.Standard.Standard_Transient | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Adds an Error Message to a starting entity from the definition
        of a Msg (Original+Value)
        """

    def AddError(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """(other name of AddFail, maintained for compatibility)"""

    @overload
    def AddWarning(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """
        Adds a Warning message to a starting entity (to the check of
        its Binder of category 0)
        """

    @overload
    def AddWarning(self, start: nanoocp.Standard.Standard_Transient | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Adds a Warning Message to a starting entity from the definition
        of a Msg (Original+Value)
        """

    def Mend(self, start: nanoocp.Standard.Standard_Transient | None, pref: str = '') -> None: ...

    def Check(self, start: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check:
        """
        Returns the Check attached to a starting entity. If <start>
        is unknown, returns an empty Check
        Adds a case name to a starting entity
        Adds a case value to a starting entity
        Returns the complete case list for an entity. Null Handle if empty
        In the list of mapped items (between 1 and NbMapped),
        searches for the first item which follows <num0>(not included)
        and which has an attribute named <name>
        Attributes are brought by Binders
        Hence, allows such an iteration

        for (num = TP->NextItemWithAttribute(name,0);
        num > 0;
        num = TP->NextItemWithAttribute(name,num) {
        .. process mapped item <num>
        }
        Returns the type of an Attribute attached to binders
        If this name gives no Attribute, returns ParamVoid
        If this name gives several different types, returns ParamMisc
        Else, returns the effective type (ParamInteger, ParamReal,
        ParamIdent, or ParamText)
        Returns the list of recorded Attribute Names, as a Dictionary
        of Integer : each value gives the count of items which bring
        this attribute name
        By default, considers all the attribute names
        If <rootname> is given, considers only the attribute names
        which begin by <rootname>
        """

    def BindTransient(self, start: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Binds a starting object with a Transient Result.
        Uses a SimpleBinderOfTransient to work. If there is already
        one but with no Result set, sets its Result.
        Considers a category number, by default 0
        """

    def FindTransient(self, start: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Result of the Transfer of an object <start> as a
        Transient Result.
        Returns a Null Handle if there is no Transient Result
        Considers a category number, by default 0
        Warning : Supposes that Binding is done with a SimpleBinderOfTransient
        """

    def BindMultiple(self, start: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Prepares an object <start> to be bound with several results.
        If no Binder is yet attached to <obj>, a MultipleBinder
        is created, empty. If a Binder is already set, it must
        accept Multiple Binding.
        Considers a category number, by default 0
        """

    def AddMultiple(self, start: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds an item to a list of results bound to a starting object.
        Considers a category number, by default 0, for all results
        """

    def FindTypedTransient(self, start: nanoocp.Standard.Standard_Transient | None, atype: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Searches for a transient result attached to a starting object,
        according to its type, by criterium IsKind(atype)

        In case of multiple result, explores the list and gives in
        <val> the first transient result IsKind(atype)
        Returns True and fills <val> if found
        Else, returns False (<val> is not touched, not even nullified)

        This syntactic form avoids to do DownCast : if a result is
        found with the good type, it is loaded in <val> and can be
        immediately used, well initialised
        """

    def GetTypedTransient(self, binder: Transfer_Binder | None, atype: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Searches for a transient result recorded in a Binder, whatever
        this Binder is recorded or not in <me>

        This is strictly equivalent to the class method GetTypedResult
        from class SimpleBinderOfTransient, but is just lighter to call

        Apart from this, works as FindTypedTransient
        """

    def NbMapped(self) -> int:
        """
        Returns the maximum possible value for Map Index
        (no result can be bound with a value greater than it)
        """

    def Mapped(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns the Starting Object bound to an Index,"""

    def MapIndex(self, start: nanoocp.Standard.Standard_Transient | None) -> int:
        """Returns the Index value bound to a Starting Object, 0 if none"""

    def MapItem(self, num: int) -> Transfer_Binder:
        """
        Returns the Binder bound to an Index
        Considers a category number, by default 0
        """

    def SetRoot(self, start: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Declares <obj> (and its Result) as Root. This status will be
        later exploited by RootResult, see below (Result can be
        produced at any time)
        """

    def SetRootManagement(self, stat: bool) -> None:
        """
        Enable (if <stat> True) or Disables (if <stat> False) Root
        Management. If it is set, Transfers are considered as stacked
        (a first Transfer commands other Transfers, and so on) and
        the Transfers commanded by an external caller are "Root".
        Remark : SetRoot can be called whatever this status, on every
        object.
        Default is set to True.
        """

    def NbRoots(self) -> int:
        """Returns the count of recorded Roots"""

    def Root(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns a Root Entity given its number in the list (1-NbRoots)"""

    def RootItem(self, num: int) -> Transfer_Binder:
        """
        Returns the Binder bound with a Root Entity given its number
        Considers a category number, by default 0
        """

    def RootIndex(self, start: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the index in the list of roots for a starting item,
        or 0 if it is not recorded as a root
        """

    def NestingLevel(self) -> int:
        """
        Returns Nesting Level of Transfers (managed by methods
        TranscriptWith & Co). Starts to zero. If no automatic Transfer
        is used, it remains to zero. Zero means Root Level.
        """

    def ResetNestingLevel(self) -> None:
        """
        Resets Nesting Level of Transfers to Zero (Root Level),
        whatever its current value.
        """

    def Recognize(self, start: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Tells if <start> has been recognized as good candidate for
        Transfer. i.e. queries the Actor and its Nexts
        """

    def Transferring(self, start: nanoocp.Standard.Standard_Transient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> Transfer_Binder:
        """
        Performs the Transfer of a Starting Object, by calling
        the method TransferProduct (see below).
        Mapping and Roots are managed : nothing is done if a Result is
        already Bound, an exception is raised in case of error.
        """

    def Transfer(self, start: nanoocp.Standard.Standard_Transient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Same as Transferring but does not return the Binder.
        Simply returns True in case of success (for user call)
        """

    def SetErrorHandle(self, err: bool) -> None:
        """
        Allows controls if exceptions will be handled
        Transfer Operations
        <err> False : they are not handled with try {} catch {}
        <err> True  : they are
        Default is False: no handling performed
        """

    def ErrorHandle(self) -> bool:
        """Returns error handling flag"""

    def StartTrace(self, binder: Transfer_Binder | None, start: nanoocp.Standard.Standard_Transient | None, level: int, mode: int) -> None:
        """
        Method called when trace is asked
        Calls PrintTrace to display information relevant for starting
        objects (which can be redefined)
        <level> is Nesting Level of Transfer (0 = root)
        <mode> controls the way the trace is done :
        0 neutral, 1 for Error, 2 for Warning message, 3 for new Root
        """

    def PrintTrace(self, start: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints a short information on a starting object. By default
        prints its Dynamic Type. Can be redefined
        """

    def IsLooping(self, alevel: int) -> bool:
        """
        Returns True if we are surely in a DeadLoop. Evaluation is not
        exact, it is a "majorant" which must be computed fast.
        This "majorant" is : <alevel> greater than NbMapped.
        """

    def RootResult(self, withstart: bool = False) -> Transfer_IteratorOfProcessForTransient:
        """
        Returns, as an iterator, the log of root transfer, i.e. the
        created objects and Binders bound to starting roots
        If withstart is given True, Starting Objects are also returned
        """

    def CompleteResult(self, withstart: bool = False) -> Transfer_IteratorOfProcessForTransient:
        """
        Returns, as an Iterator, the entire log of transfer (list of
        created objects and Binders which can bring errors)
        If withstart is given True, Starting Objects are also returned
        """

    def AbnormalResult(self) -> Transfer_IteratorOfProcessForTransient:
        """
        Returns Binders which are neither "Done" nor "Initial",
        that is Error,Loop or Run (abnormal states at end of Transfer)
        Starting Objects are given in correspondence in the iterator
        """

    def CheckList(self, erronly: bool) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns a CheckList as a list of Check : each one is for a
        starting entity which have either check (warning or fail)
        messages are attached, or are in abnormal state : that case
        gives a specific message
        If <erronly> is True, checks with Warnings only are ignored
        """

    def ResultOne(self, start: nanoocp.Standard.Standard_Transient | None, level: int, withstart: bool = False) -> Transfer_IteratorOfProcessForTransient:
        """
        Returns, as an Iterator, the log of transfer for one object
        <level> = 0 : this object only
        and if <start> is a scope owner (else, <level> is ignored) :
        <level> = 1 : object plus its immediate scoped ones
        <level> = 2 : object plus all its scoped ones
        """

    def CheckListOne(self, start: nanoocp.Standard.Standard_Transient | None, level: int, erronly: bool) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns a CheckList for one starting object
        <level> interpreted as by ResultOne
        If <erronly> is True, checks with Warnings only are ignored
        """

    def IsCheckListEmpty(self, start: nanoocp.Standard.Standard_Transient | None, level: int, erronly: bool) -> bool:
        """
        Returns True if no check message is attached to a starting
        object. <level> interpreted as by ResultOne
        If <erronly> is True, checks with Warnings only are ignored
        """

    def RemoveResult(self, start: nanoocp.Standard.Standard_Transient | None, level: int, compute: bool = True) -> None:
        """
        Removes Results attached to (== Unbinds) a given object and,
        according <level> :
        <level> = 0 : only it
        <level> = 1 : it plus its immediately owned sub-results(scope)
        <level> = 2 : it plus all its owned sub-results(scope)
        """

    def CheckNum(self, start: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Computes a number to be associated to a starting object in
        a check or a check-list
        By default, returns 0; can be redefined
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ResultFromModel(nanoocp.Standard.Standard_Transient):
    """
    ResultFromModel is used to store a final result stored in a
    TransientProcess, respectfully to its structuration in scopes
    by using a set of ResultFromTransient
    Hence, it can be regarded as a passive equivalent of the
    stored data in the TransientProcess, while an Iterator gives
    a flat view of it.

    A ResultFromModel is intended to be attached to the transfer
    of one entity (typically root entity but it is not mandatory)

    It is then possible to :
    - Create and fill a ResultFromModel from a TransientProcess,
    by designating a starting entity
    - Fill back the TransientProcess from a ResultFromModel, as it
    were filled by the operation which filled it the first time
    """

    @overload
    def __init__(self) -> None:
        """Creates a ResultFromModel, empty"""

    @overload
    def __init__(self, theOther: Transfer_ResultFromModel) -> None: ...

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Sets starting Model"""

    def SetFileName(self, filename: str) -> None:
        """Sets starting File Name"""

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns starting Model (null if not set)"""

    def FileName(self) -> str:
        """Returns starting File Name (empty if not set)"""

    def Fill(self, TP: Transfer_TransientProcess | None, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Fills from a TransientProcess, with the result attached to
        a starting entity. Considers its Model if it is set.
        This action produces a structured set of ResultFromTransient,
        considering scopes, starting by that of <ent>.
        If <ent> has no recorded result, it remains empty
        Returns True if a result is recorded, False else
        """

    def Strip(self, mode: int) -> None:
        """
        Clears some data attached to binders used by TransientProcess,
        which become useless once the transfer has been done,
        by calling Strip on its ResultFromTransient

        mode = 0  : minimum, clears data remaining from TransferProcess
        mode = 10 : just keeps file name, label, check status ...,
        and MainResult but only the result (Binder)
        mode = 11 : also clears MainResult (status and names remain)
        """

    def FillBack(self, TP: Transfer_TransientProcess | None) -> None:
        """
        Fills back a TransientProcess from the structured set of
        binders. Also sets the Model.
        """

    def HasResult(self) -> bool:
        """Returns True if a Result is recorded"""

    def MainResult(self) -> Transfer_ResultFromTransient:
        """Returns the main recorded ResultFromTransient, or a null"""

    def SetMainResult(self, amain: Transfer_ResultFromTransient | None) -> None:
        """Sets a new value for the main recorded ResultFromTransient"""

    def MainLabel(self) -> str:
        """
        Returns the label in starting model attached to main entity
        (updated by Fill or SetMainResult, if Model is known)
        """

    def MainNumber(self) -> int:
        """Returns the label in starting model attached to main entity"""

    def ResultFromKey(self, start: nanoocp.Standard.Standard_Transient | None) -> Transfer_ResultFromTransient:
        """
        Searches for a key (starting entity) and returns its result
        Returns a null handle if not found
        """

    def Results(self, level: int) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Internal method which returns the list of ResultFromTransient,
        according level (2:complete; 1:sub-level 1; 0:main only)
        """

    def TransferredList(self, level: int = 2) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of recorded starting entities, ending by the
        root. Entities with check but no transfer result are ignored
        <level> = 2 (D), considers the complete list
        <level> = 1      considers the main result plus immediate subs
        <level> = 0      just the main result
        """

    def CheckedList(self, check: nanoocp.Interface.Interface_CheckStatus, result: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of starting entities to which a check status
        is attached.
        <check> = -2  all entities whatever the check (see result)
        <check> = -1  entities with no fail (warning allowed)
        <check> =  0  entities with no check at all
        <check> =  1  entities with warning but no fail
        <check> =  2  entities with fail
        <result> : if True, only entities with an attached result
        Remark : result True and check=0 will give an empty list
        """

    def CheckList(self, erronly: bool, level: int = 2) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the check-list of this set of results
        <erronly> true : only fails are considered
        <level> = 0 : considers only main binder
        <level> = 1 : considers main binder plus immediate subs
        <level> = 2 (D) : considers all checks
        """

    def CheckStatus(self) -> nanoocp.Interface.Interface_CheckStatus:
        """
        Returns the check status with corresponds to the content
        of this ResultFromModel; considers all levels of transfer
        (worst status). Returns CheckAny if not yet computed
        Reads it from recorded status if already computed, else
        recomputes one
        """

    def ComputeCheckStatus(self, enforce: bool) -> nanoocp.Interface.Interface_CheckStatus:
        """
        Computes and records check status (see CheckStatus)
        Does not computes it if already done and <enforce> False
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_ResultFromTransient(nanoocp.Standard.Standard_Transient):
    """
    This class, in conjunction with ResultFromModel, allows to
    record the result of a transfer initially stored in a
    TransientProcess.

    A ResultFromTransient records a couple (Transient,Binder for
    the result and checks) plus a list of "sub-results", which
    have been recorded in the TrabsientProcess, under scope
    attached to the starting transient.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ResultFromTransient, empty"""

    @overload
    def __init__(self, theOther: Transfer_ResultFromTransient) -> None: ...

    def SetStart(self, start: nanoocp.Standard.Standard_Transient | None) -> None:
        """Sets starting entity"""

    def SetBinder(self, binder: Transfer_Binder | None) -> None:
        """Sets Binder (for result plus individual check)"""

    def Start(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the starting entity"""

    def Binder(self) -> Transfer_Binder:
        """Returns the binder"""

    def HasResult(self) -> bool:
        """Returns True if a result is recorded"""

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """Returns the check (or an empty one if no binder)"""

    def CheckStatus(self) -> nanoocp.Interface.Interface_CheckStatus:
        """Returns the check status"""

    def ClearSubs(self) -> None:
        """Clears the list of (immediate) sub-results"""

    def AddSubResult(self, sub: Transfer_ResultFromTransient | None) -> None:
        """Adds a sub-result"""

    def NbSubResults(self) -> int:
        """Returns the count of recorded sub-results"""

    def SubResult(self, num: int) -> Transfer_ResultFromTransient:
        """Returns a sub-result, given its rank"""

    def ResultFromKey(self, key: nanoocp.Standard.Standard_Transient | None) -> Transfer_ResultFromTransient:
        """
        Returns the ResultFromTransient attached to a given starting
        entity (the key). Returns a null handle if not found
        """

    def FillMap(self, map: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
        """
        This method is used by ResultFromModel to collate the list of
        ResultFromTransient, avoiding duplications with a map
        Remark : <me> is already in the map and has not to be bound
        """

    def Fill(self, TP: Transfer_TransientProcess | None) -> None:
        """
        Fills from a TransientProcess, with the starting entity which
        must have been set before. It works with scopes, calls Fill
        on each of its sub-results
        """

    def Strip(self) -> None:
        """
        Clears some data attached to binders used by TransientProcess,
        which become useless once the transfer has been done :
        the list of sub-scoped binders, which is now recorded as
        sub-results
        """

    def FillBack(self, TP: Transfer_TransientProcess | None) -> None:
        """
        Fills back a TransientProcess with definition of a
        ResultFromTransient, respectfully to its structuration in
        scopes
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_TransferFailure(nanoocp.Interface.Interface_InterfaceError):
    pass

class Transfer_TransferDeadLoop(Transfer_TransferFailure):
    pass

class Transfer_TransferInput:
    """
    A TransferInput is a Tool which fills an InterfaceModel with
    the result of the Transfer of CasCade Objects, once determined
    The Result comes from a TransferProcess, either from
    Transient (the Complete Result is considered, it must contain
    only Transient Objects)
    """

    @overload
    def __init__(self) -> None:
        """Creates a TransferInput ready to use"""

    @overload
    def __init__(self, theOther: Transfer_TransferInput) -> None: ...

    def Entities(self, list: Transfer_TransferIterator) -> nanoocp.Interface.Interface_EntityIterator:
        """Takes the transient items stored in a TransferIterator"""

    @overload
    def FillModel(self, proc: Transfer_TransientProcess | None, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None: ...

    @overload
    def FillModel(self, proc: Transfer_TransientProcess | None, amodel: nanoocp.Interface.Interface_InterfaceModel | None, proto: nanoocp.Interface.Interface_Protocol | None, roots: bool = True) -> None: ...

    @overload
    def FillModel(self, proc: Transfer_FinderProcess | None, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Fills an InterfaceModel with the Complete Result of a Transfer
        stored in a TransientProcess (Starting Objects are Transient)
        The complete result is exactly added to the model
        """

    @overload
    def FillModel(self, proc: Transfer_FinderProcess | None, amodel: nanoocp.Interface.Interface_InterfaceModel | None, proto: nanoocp.Interface.Interface_Protocol | None, roots: bool = True) -> None:
        """
        Fills an InterfaceModel with results of the Transfer recorded
        in a TransientProcess (Starting Objects are Transient) :
        Root Result if <roots> is True (Default), Complete Result else
        The entities added to the model are determined from the result
        by by adding the referenced entities
        """

class Transfer_TransferOutput:
    """
    A TransferOutput is a Tool which manages the transfer of
    entities created by an Interface, stored in an InterfaceModel,
    into a set of Objects suitable for an Application
    Objects to be transferred are given, by method Transfer
    (which calls Transfer from TransientProcess)
    A default action is available to get all roots of the Model
    Result is given as a TransferIterator (see TransferProcess)
    Also, it is possible to pilot directly the TransientProcess
    """

    @overload
    def __init__(self, actor: Transfer_ActorOfTransientProcess | None, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Creates a TransferOutput ready to use, with a TransientProcess"""

    @overload
    def __init__(self, proc: Transfer_TransientProcess | None, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Creates a TransferOutput from an already existing
        TransientProcess, and a Model
        Returns (by Reference, hence can be changed) the Mode for
        Scope Management. False (D) means Scope is ignored.
        True means that each individual Transfer (direct or through
        TransferRoots) is regarded as one Scope
        """

    @overload
    def __init__(self, theOther: Transfer_TransferOutput) -> None: ...

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Starting Model"""

    def TransientProcess(self) -> Transfer_TransientProcess:
        """Returns the TransientProcess used to work"""

    def Transfer(self, obj: nanoocp.Standard.Standard_Transient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Transfer checks that all taken Entities come from the same
        Model, then calls Transfer from TransientProcess
        """

    @overload
    def TransferRoots(self, protocol: nanoocp.Interface.Interface_Protocol | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Runs transfer on the roots of the Interface Model
        The Roots are computed with a ShareFlags created from a
        Protocol given as Argument
        """

    @overload
    def TransferRoots(self, G: nanoocp.Interface.Interface_Graph, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Runs transfer on the roots defined by a Graph of dependences
        (which detains also a Model and its Entities)
        Roots are computed with a ShareFlags created from the Graph
        """

    @overload
    def TransferRoots(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Runs transfer on the roots of the Interface Model
        Remark : the Roots are computed with a ShareFlags created
        from the Active Protocol
        """

    def ListForStatus(self, normal: bool, roots: bool = True) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of Starting Entities with these criteria :
        - <normal> False, gives the entities bound with ABNORMAL STATUS
        (e.g. : Fail recorded, Exception raised during Transfer)
        - <normal> True, gives Entities with or without a Result, but
        with no Fail, no Exception (Warnings are not counted)
        - <roots> False, considers all entities recorded (either for
        Result, or for at least one Fail or Warning message)
        - <roots> True (Default), considers only roots of Transfer
        (the Entities recorded at highest level)
        This method is based on AbnormalResult from TransferProcess
        """

    def ModelForStatus(self, protocol: nanoocp.Interface.Interface_Protocol | None, normal: bool, roots: bool = True) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Fills a Model with the list determined by ListForStatus
        This model starts from scratch (made by NewEmptyModel from the
        current Model), then is filled by AddWithRefs

        Useful to get separately from a transfer, the entities which
        have caused problem, in order to furtherly analyse them (with
        normal = False), or the "good" entities, to obtain a data set
        "which works well" (with normal = True)
        """

class Transfer_TransientListBinder(Transfer_Binder):
    """
    This binder binds several (a list of) Transients with a starting
    entity, when this entity itself corresponds to a simple list
    of Transients. Each part is not seen as a sub-result of an
    independent component, but as an item of a built-in list
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None: ...

    @overload
    def __init__(self, theOther: Transfer_TransientListBinder) -> None: ...

    def IsMultiple(self) -> bool: ...

    def ResultType(self) -> nanoocp.Standard.Standard_Type: ...

    def ResultTypeName(self) -> str: ...

    def AddResult(self, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds an item to the result list"""

    def Result(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]: ...

    def SetResult(self, num: int, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """Changes an already defined sub-result"""

    def NbTransients(self) -> int: ...

    def Transient(self, num: int) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_TransientMapper(Transfer_Finder):
    @overload
    def __init__(self, akey: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Creates a Mapper with a Value. This Value can then not be
        changed. It is used by the Hasher to compute the HashCode,
        which will then be stored for an immediate reading.
        """

    @overload
    def __init__(self, theOther: Transfer_TransientMapper) -> None: ...

    def Value(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the contained value"""

    def Equates(self, other: Transfer_Finder | None) -> bool:
        """
        Specific testof equality : defined as False if <other> has
        not the same true Type, else contents are compared (by
        C++ operator ==)
        """

    def ValueType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type of the Value. By default, returns the
        DynamicType of <me>, but can be redefined
        """

    def ValueTypeName(self) -> str:
        """
        Returns the name of the Type of the Value. Default is name
        of ValueType, unless it is for a non-handled object
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_TransientProcess(Transfer_ProcessForTransient):
    """
    Adds specific features to the generic definition :
    TransientProcess is intended to work from an InterfaceModel
    to a set of application objects.

    Hence, some information about starting entities can be gotten
    from the model : for Trace, CheckList, Integrity Status
    """

    @overload
    def __init__(self, nb: int = 10000) -> None:
        """Sets TransientProcess at initial state, with an initial size"""

    @overload
    def __init__(self, theOther: Transfer_TransientProcess) -> None: ...

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Sets an InterfaceModel, used by StartTrace, CheckList, queries
        on Integrity, to give information significant for each norm.
        """

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model used for StartTrace"""

    def SetGraph(self, HG: nanoocp.Interface.Interface_HGraph | None) -> None:
        """Sets a Graph : supersedes SetModel if already done"""

    def HasGraph(self) -> bool: ...

    def HGraph(self) -> nanoocp.Interface.Interface_HGraph: ...

    def Graph(self) -> nanoocp.Interface.Interface_Graph: ...

    def SetContext(self, name: str, ctx: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Sets a Context : according to receiving appli, to be
        interpreted by the Actor
        """

    def GetContext(self, name: str, type: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns the Context attached to a name, if set and if it is
        Kind of the type, else a Null Handle
        Returns True if OK, False if no Context
        """

    def Context(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]:
        """
        Returns (modifiable) the whole definition of Context
        Rather for internal use (ex.: preparing and setting in once)
        """

    def PrintTrace(self, start: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Specific printing to trace an entity : prints label and type
        (if model is set)
        """

    def CheckNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Specific number of a starting object for check-list : Number
        in model
        """

    def TypedSharings(self, start: nanoocp.Standard.Standard_Transient | None, type: nanoocp.Standard.Standard_Type | None) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of sharings entities, AT ANY LEVEL, which are
        kind of a given type. Calls TypedSharings from Graph
        Returns an empty list if the Graph has not been acknowledged
        """

    def IsDataLoaded(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Tells if an entity is well loaded from file (even if its data
        fail on checking, they are present). Mostly often, answers
        True. Else, there was a syntactic error in the file.
        A non-loaded entity MAY NOT BE transferred, unless its Report
        (in the model) is interpreted
        """

    def IsDataFail(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Tells if an entity fails on data checking (load time,
        syntactic, or semantic check). Normally, should answer False.
        It is not prudent to try transferring an entity which fails on
        data checking
        """

    def PrintStats(self, mode: int) -> str:
        """Prints statistics on a given output, according mode"""

    def RootsForTransfer(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Transfer_VoidBinder(Transfer_Binder):
    """
    a VoidBinder is used to bind a starting item with a status,
    error or warning messages, but no result
    It is interpreted by TransferProcess, which admits a
    VoidBinder to be over-written, and copies its check to the
    new Binder
    """

    @overload
    def __init__(self) -> None:
        """
        a VoidBinder is not Multiple (Remark : it is not Simple too)
        But it can bring next results ...
        """

    @overload
    def __init__(self, theOther: Transfer_VoidBinder) -> None: ...

    def ResultType(self) -> nanoocp.Standard.Standard_Type:
        """
        while a VoidBinder admits no Result, its ResultType returns
        the type of <me>
        """

    def ResultTypeName(self) -> str:
        """Returns "(void)\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TCollection
import nanoocp.Transfer
Transfer_HSequenceOfFinder = nanoocp.NCollection.NCollection_HSequence[nanoocp.Transfer.Transfer_Finder]
Transfer_SequenceOfFinder = nanoocp.NCollection.NCollection_Sequence[nanoocp.Transfer.Transfer_Finder]
