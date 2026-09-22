"""OCCT package TFunction (toolkit TKLCAF)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TDF


class TFunction_ExecutionStatus(enum.IntEnum):
    TFunction_ES_WrongDefinition = 0

    TFunction_ES_NotExecuted = 1

    TFunction_ES_Executing = 2

    TFunction_ES_Succeeded = 3

    TFunction_ES_Failed = 4

TFunction_ES_WrongDefinition: TFunction_ExecutionStatus = ...

TFunction_ES_NotExecuted: TFunction_ExecutionStatus = ...

TFunction_ES_Executing: TFunction_ExecutionStatus = TFunction_ExecutionStatus.TFunction_ES_Executing

TFunction_ES_Succeeded: TFunction_ExecutionStatus = TFunction_ExecutionStatus.TFunction_ES_Succeeded

TFunction_ES_Failed: TFunction_ExecutionStatus = TFunction_ExecutionStatus.TFunction_ES_Failed

class TFunction_Driver(nanoocp.Standard.Standard_Transient):
    """
    This driver class provide services around function
    execution. One instance of this class is built for
    the whole session. The driver is bound to the
    DriverGUID in the DriverTable class.
    It allows you to create classes which inherit from
    this abstract class.
    These subclasses identify the various algorithms
    which can be applied to the data contained in the
    attributes of sub-labels of a model.
    A single instance of this class and each of its
    subclasses is built for the whole session.
    """

    def Init(self, L: nanoocp.TDF.TDF_Label) -> None:
        """Initializes the label L for this function prior to its execution."""

    def Label(self) -> nanoocp.TDF.TDF_Label:
        """Returns the label of the driver for this function."""

    def Validate(self, log: TFunction_Logbook | None) -> None:
        """
        Validates labels of a function in <log>.
        This function is the one initialized in this function driver.
        Warning
        In regeneration mode, the solver must call this
        method even if the function is not executed.
        execution of function
        =====================
        """

    def MustExecute(self, log: TFunction_Logbook | None) -> bool:
        """
        Analyzes the labels in the logbook log.
        Returns true if attributes have been modified.
        If the function label itself has been modified, the function must be executed.
        """

    def Execute(self) -> tuple[int, TFunction_Logbook]:
        """
        Executes the function in this function driver and
        puts the impacted labels in the logbook log.
        arguments & results of functions
        ================================
        """

    def Arguments(self, args: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """
        The method fills-in the list by labels,
        where the arguments of the function are located.
        """

    def Results(self, res: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """
        The method fills-in the list by labels,
        where the results of the function are located.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TFunction_DriverTable(nanoocp.Standard.Standard_Transient):
    """
    A container for instances of drivers.
    You create a new instance of TFunction_Driver
    and use the method AddDriver to load it into the driver table.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: TFunction_DriverTable) -> None: ...

    @staticmethod
    def Get() -> TFunction_DriverTable:
        """Returns the driver table. If a driver does not exist, creates it."""

    def AddDriver(self, guid: nanoocp.Standard.Standard_GUID, driver: TFunction_Driver | None, thread: int = 0) -> bool:
        """
        Returns true if the driver has been added successfully to the driver table.
        """

    def HasDriver(self, guid: nanoocp.Standard.Standard_GUID, thread: int = 0) -> bool:
        """Returns true if the driver exists in the driver table."""

    def FindDriver(self, guid: nanoocp.Standard.Standard_GUID, thread: int = 0) -> tuple[bool, TFunction_Driver]:
        """Returns true if the driver was found."""

    def Dump(self) -> str: ...

    def RemoveDriver(self, guid: nanoocp.Standard.Standard_GUID, thread: int = 0) -> bool:
        """
        Removes a driver with the given GUID.
        Returns true if the driver has been removed successfully.
        """

    def Clear(self) -> None:
        """
        Removes all drivers. Returns true if the driver has been removed successfully.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TFunction_Function(nanoocp.TDF.TDF_Attribute):
    """
    Provides the following two services
    -   a link to an evaluation driver
    -   the means of providing a link between a
    function and an evaluation driver.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TFunction_Function) -> None: ...

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> TFunction_Function:
        """
        Static methods:
        ==============
        Finds or Creates a function attribute on the label <L>.
        Returns the function attribute.
        """

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label, DriverID: nanoocp.Standard.Standard_GUID) -> TFunction_Function:
        """
        Finds or Creates a function attribute on the label <L>.
        Sets a driver ID to the function.
        Returns the function attribute.
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Returns the GUID for functions.
        Returns a function found on the label.
        Instance methods:
        ================
        """

    def GetDriverGUID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID for this function's driver."""

    def SetDriverGUID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """
        Sets the driver for this function as that
        identified by the GUID guid.
        """

    def Failed(self) -> bool:
        """Returns true if the execution failed"""

    def SetFailure(self, mode: int = 0) -> None:
        """Sets the failed index."""

    def GetFailure(self) -> int:
        """
        Returns an index of failure if the execution of this function failed.
        If this integer value is 0, no failure has occurred.
        Implementation of Attribute methods:
        ===================================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TFunction_GraphNode(nanoocp.TDF.TDF_Attribute):
    """Provides links between functions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TFunction_GraphNode) -> None: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> TFunction_GraphNode:
        """
        Static methods
        ==============
        Finds or Creates a graph node attribute at the label <L>.
        Returns the attribute.
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Returns the GUID for GraphNode attribute.
        Instant methods
        ===============
        Constructor (empty).
        """

    @overload
    def AddPrevious(self, funcID: int) -> bool: ...

    @overload
    def AddPrevious(self, func: nanoocp.TDF.TDF_Label) -> bool:
        """Defines a reference to the function as a previous one."""

    @overload
    def RemovePrevious(self, funcID: int) -> bool: ...

    @overload
    def RemovePrevious(self, func: nanoocp.TDF.TDF_Label) -> bool:
        """Removes a reference to the function as a previous one."""

    def GetPrevious(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """Returns a map of previous functions."""

    def RemoveAllPrevious(self) -> None:
        """Clears a map of previous functions."""

    @overload
    def AddNext(self, funcID: int) -> bool: ...

    @overload
    def AddNext(self, func: nanoocp.TDF.TDF_Label) -> bool:
        """Defines a reference to the function as a next one."""

    @overload
    def RemoveNext(self, funcID: int) -> bool: ...

    @overload
    def RemoveNext(self, func: nanoocp.TDF.TDF_Label) -> bool:
        """Removes a reference to the function as a next one."""

    def GetNext(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """Returns a map of next functions."""

    def RemoveAllNext(self) -> None:
        """Clears a map of next functions."""

    def GetStatus(self) -> TFunction_ExecutionStatus:
        """Returns the execution status of the function."""

    def SetStatus(self, status: TFunction_ExecutionStatus) -> None:
        """
        Defines an execution status for a function.
        Implementation of Attribute methods
        ===================================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TFunction_IFunction:
    """Interface class for usage of Function Mechanism"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.TDF.TDF_Label) -> None:
        """
        A constructor.
        Initializes the interface by the label of function.
        """

    @overload
    def __init__(self, theOther: TFunction_IFunction) -> None: ...

    @staticmethod
    def NewFunction(L: nanoocp.TDF.TDF_Label, ID: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Sets a new function attached to a label <L> with <ID>.
        It creates a new TFunction_Function attribute initialized by the <ID>,
        a new TFunction_GraphNode with an empty list of dependencies and
        the status equal to TFunction_ES_WrongDefinition.
        It registers the function in the scope of functions for this document.
        """

    @staticmethod
    def DeleteFunction(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Deletes a function attached to a label <L>.
        It deletes a TFunction_Function attribute and a TFunction_GraphNode.
        It deletes the functions from the scope of function of this document.
        """

    @staticmethod
    def UpdateDependencies_s(Access: nanoocp.TDF.TDF_Label) -> bool:
        """
        Updates dependencies for all functions of the scope.
        It returns false in case of an error.
        An empty constructor.
        """

    def Init(self, L: nanoocp.TDF.TDF_Label) -> None:
        """Initializes the interface by the label of function."""

    def Label(self) -> nanoocp.TDF.TDF_Label:
        """Returns a label of the function."""

    def UpdateDependencies(self) -> bool:
        """Updates the dependencies of this function only."""

    def Arguments(self, args: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """
        The method fills-in the list by labels,
        where the arguments of the function are located.
        """

    def Results(self, res: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """
        The method fills-in the list by labels,
        where the results of the function are located.
        """

    def GetPrevious(self, prev: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """Returns a list of previous functions."""

    def GetNext(self, prev: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """Returns a list of next functions."""

    def GetStatus(self) -> TFunction_ExecutionStatus:
        """Returns the execution status of the function."""

    def SetStatus(self, status: TFunction_ExecutionStatus) -> None:
        """Defines an execution status for a function."""

    def GetAllFunctions(self) -> nanoocp.NCollection.NCollection_DoubleMap[int, nanoocp.TDF.TDF_Label]:
        """Returns the scope of all functions."""

    def GetLogbook(self) -> TFunction_Logbook:
        """Returns the Logbook - keeper of modifications."""

    def GetDriver(self, thread: int = 0) -> TFunction_Driver:
        """Returns a driver of the function."""

    def GetGraphNode(self) -> TFunction_GraphNode:
        """Returns a graph node of the function."""

class TFunction_Iterator:
    """Iterator of the graph of functions"""

    @overload
    def __init__(self) -> None:
        """An empty constructor."""

    @overload
    def __init__(self, Access: nanoocp.TDF.TDF_Label) -> None:
        """
        A constructor.
        Initializes the iterator.
        """

    @overload
    def __init__(self, theOther: TFunction_Iterator) -> None: ...

    def __iter__(self) -> TFunction_Iterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]:
        """Python addition: see __iter__."""

    def Init(self, Access: nanoocp.TDF.TDF_Label) -> None:
        """Initializes the Iterator."""

    def SetUsageOfExecutionStatus(self, usage: bool) -> None:
        """
        Defines the mode of iteration - usage or not of the execution status.
        If the iterator takes into account the execution status,
        the method ::Current() returns only "not executed" functions
        while their status is not changed.
        If the iterator ignores the execution status,
        the method ::Current() returns the functions
        following their dependencies and ignoring the execution status.
        """

    def GetUsageOfExecutionStatus(self) -> bool:
        """Returns usage of execution status by the iterator."""

    def GetMaxNbThreads(self) -> int:
        """
        Analyses the graph of dependencies and returns
        maximum number of threads may be used to calculate the model.
        """

    def Current(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]:
        """
        Returns the current list of functions.
        If the iterator uses the execution status,
        the returned list contains only the functions
        with "not executed" status.
        """

    def More(self) -> bool:
        """Returns false if the graph of functions is fully iterated."""

    def Next(self) -> None:
        """Switches the iterator to the next list of current functions."""

    def GetStatus(self, func: nanoocp.TDF.TDF_Label) -> TFunction_ExecutionStatus:
        """
        A help-function aimed to help the user to check the status of retrurned function.
        It calls TFunction_GraphNode::GetStatus() inside.
        """

    def SetStatus(self, func: nanoocp.TDF.TDF_Label, status: TFunction_ExecutionStatus) -> None:
        """
        A help-function aimed to help the user to change the execution status of a function.
        It calls TFunction_GraphNode::SetStatus() inside.
        """

    def Dump(self) -> str: ...

class TFunction_Logbook(nanoocp.TDF.TDF_Attribute):
    """
    This class contains information which is written and
    read during the solving process. Information is divided
    in three groups.

    * Touched Labels  (modified by the end user),
    * Impacted Labels (modified during execution of the function),
    * Valid Labels    (within the valid label scope).
    """

    @overload
    def __init__(self) -> None:
        """Constructor (empty)."""

    @overload
    def __init__(self, theOther: TFunction_Logbook) -> None: ...

    @staticmethod
    def Set(Access: nanoocp.TDF.TDF_Label) -> TFunction_Logbook:
        """
        Finds or Creates a TFunction_Logbook attribute at the root label accessed by <Access>.
        Returns the attribute.
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID for logbook attribute."""

    def Clear(self) -> None:
        """Clears this logbook to its default, empty state."""

    def IsEmpty(self) -> bool: ...

    def SetTouched(self, L: nanoocp.TDF.TDF_Label) -> None:
        """
        Sets the label L as a touched label in this logbook.
        In other words, L is understood to have been modified by the end user.
        """

    def SetImpacted(self, L: nanoocp.TDF.TDF_Label, WithChildren: bool = False) -> None:
        """
        Sets the label L as an impacted label in this logbook.
        This method is called by execution of the function driver.
        """

    @overload
    def SetValid(self, L: nanoocp.TDF.TDF_Label, WithChildren: bool = False) -> None:
        """Sets the label L as a valid label in this logbook."""

    @overload
    def SetValid(self, Ls: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None: ...

    def IsModified(self, L: nanoocp.TDF.TDF_Label, WithChildren: bool = False) -> bool:
        """
        Returns True if the label L is touched or impacted. This method
        is called by <TFunction_FunctionDriver::MustExecute>.
        If <WithChildren> is set to true, the method checks
        all the sublabels of <L> too.
        """

    def GetTouched(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """
        Returns the map of touched labels in this logbook.
        A touched label is the one modified by the end user.
        """

    def GetImpacted(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """Returns the map of impacted labels contained in this logbook."""

    @overload
    def GetValid(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """Returns the map of valid labels in this logbook."""

    @overload
    def GetValid(self, Ls: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None: ...

    def Done(self, status: bool) -> None:
        """Sets status of execution."""

    def IsDone(self) -> bool:
        """Returns status of execution."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None:
        """Undos (and redos) the attribute."""

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """Pastes the attribute to another label."""

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Returns a new empty instance of the attribute."""

    def Dump(self) -> str:
        """Prints th data of the attributes (touched, impacted and valid labels)."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TFunction_Scope(nanoocp.TDF.TDF_Attribute):
    """Keeps a scope of functions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TFunction_Scope) -> None: ...

    @staticmethod
    def Set(Access: nanoocp.TDF.TDF_Label) -> TFunction_Scope:
        """
        Static methods
        ==============
        Finds or Creates a TFunction_Scope attribute at the root label accessed by <Access>.
        Returns the attribute.
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Returns the GUID for Scope attribute.
        Instant methods
        ===============
        Constructor (empty).
        """

    def AddFunction(self, L: nanoocp.TDF.TDF_Label) -> bool:
        """Adds a function to the scope of functions."""

    @overload
    def RemoveFunction(self, L: nanoocp.TDF.TDF_Label) -> bool: ...

    @overload
    def RemoveFunction(self, ID: int) -> bool:
        """Removes a function from the scope of functions."""

    def RemoveAllFunctions(self) -> None:
        """Removes all functions from the scope of functions."""

    @overload
    def HasFunction(self, ID: int) -> bool:
        """Returns true if the function exists with such an ID."""

    @overload
    def HasFunction(self, L: nanoocp.TDF.TDF_Label) -> bool:
        """Returns true if the label contains a function of this scope."""

    @overload
    def GetFunction(self, L: nanoocp.TDF.TDF_Label) -> int:
        """Returns an ID of the function."""

    @overload
    def GetFunction(self, ID: int) -> nanoocp.TDF.TDF_Label:
        """Returns the label of the function with this ID."""

    def GetLogbook(self) -> TFunction_Logbook:
        """
        Returns the Logbook used in TFunction_Driver methods.
        Implementation of Attribute methods
        ===================================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Dump(self) -> str: ...

    def GetFunctions(self) -> nanoocp.NCollection.NCollection_DoubleMap[int, nanoocp.TDF.TDF_Label]:
        """Returns the scope of functions."""

    def ChangeFunctions(self) -> nanoocp.NCollection.NCollection_DoubleMap[int, nanoocp.TDF.TDF_Label]:
        """
        Returns the scope of functions for modification.
        Warning: Don't use this method if You are not sure what You do!
        """

    def SetFreeID(self, ID: int) -> None: ...

    def GetFreeID(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
TFunction_Array1OfDataMapOfGUIDDriver = nanoocp.NCollection.NCollection_Array1[int]
TFunction_HArray1OfDataMapOfGUIDDriver = nanoocp.NCollection.NCollection_HArray1[int]
