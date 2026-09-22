"""OCCT package Interface (toolkit TKXSBase)"""

import enum
from typing import TextIO, overload

import nanoocp.Message
import nanoocp.MoniTool
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class Interface_CheckStatus(enum.IntEnum):
    """
    Classifies checks
    OK     : check is empty
    Warning: Warning, no Fail
    Fail   : Fail
    Others to query:
    Any    : any status
    Message: Warning/Fail
    NoFail : Warning/OK
    """

    Interface_CheckOK = 0

    Interface_CheckWarning = 1

    Interface_CheckFail = 2

    Interface_CheckAny = 3

    Interface_CheckMessage = 4

    Interface_CheckNoFail = 5

Interface_CheckOK: Interface_CheckStatus = Interface_CheckStatus.Interface_CheckOK

Interface_CheckWarning: Interface_CheckStatus = Interface_CheckStatus.Interface_CheckWarning

Interface_CheckFail: Interface_CheckStatus = Interface_CheckStatus.Interface_CheckFail

Interface_CheckAny: Interface_CheckStatus = Interface_CheckStatus.Interface_CheckAny

Interface_CheckMessage: Interface_CheckStatus = Interface_CheckStatus.Interface_CheckMessage

Interface_CheckNoFail: Interface_CheckStatus = Interface_CheckStatus.Interface_CheckNoFail

class Interface_DataState(enum.IntEnum):
    """validity state of anentity's content (see InterfaceModel)"""

    Interface_StateOK = 0

    Interface_LoadWarning = 1

    Interface_LoadFail = 2

    Interface_DataWarning = 3

    Interface_DataFail = 4

    Interface_StateUnloaded = 5

    Interface_StateUnknown = 6

Interface_StateOK: Interface_DataState = Interface_DataState.Interface_StateOK

Interface_LoadWarning: Interface_DataState = Interface_DataState.Interface_LoadWarning

Interface_LoadFail: Interface_DataState = Interface_DataState.Interface_LoadFail

Interface_DataWarning: Interface_DataState = Interface_DataState.Interface_DataWarning

Interface_DataFail: Interface_DataState = Interface_DataState.Interface_DataFail

Interface_StateUnloaded: Interface_DataState = Interface_DataState.Interface_StateUnloaded

Interface_StateUnknown: Interface_DataState = Interface_DataState.Interface_StateUnknown

class Interface_ParamType(enum.IntEnum):
    Interface_ParamMisc = 0

    Interface_ParamInteger = 1

    Interface_ParamReal = 2

    Interface_ParamIdent = 3

    Interface_ParamVoid = 4

    Interface_ParamText = 5

    Interface_ParamEnum = 6

    Interface_ParamLogical = 7

    Interface_ParamSub = 8

    Interface_ParamHexa = 9

    Interface_ParamBinary = 10

Interface_ParamMisc: Interface_ParamType = Interface_ParamType.Interface_ParamMisc

Interface_ParamInteger: Interface_ParamType = Interface_ParamType.Interface_ParamInteger

Interface_ParamReal: Interface_ParamType = Interface_ParamType.Interface_ParamReal

Interface_ParamIdent: Interface_ParamType = Interface_ParamType.Interface_ParamIdent

Interface_ParamVoid: Interface_ParamType = Interface_ParamType.Interface_ParamVoid

Interface_ParamText: Interface_ParamType = Interface_ParamType.Interface_ParamText

Interface_ParamEnum: Interface_ParamType = Interface_ParamType.Interface_ParamEnum

Interface_ParamLogical: Interface_ParamType = Interface_ParamType.Interface_ParamLogical

Interface_ParamSub: Interface_ParamType = Interface_ParamType.Interface_ParamSub

Interface_ParamHexa: Interface_ParamType = Interface_ParamType.Interface_ParamHexa

Interface_ParamBinary: Interface_ParamType = Interface_ParamType.Interface_ParamBinary

class Interface_BitMap:
    """
    A bit map simply allows to associate a boolean flag to each
    item of a list, such as a list of entities, etc... numbered
    between 1 and a positive count nbitems

    The BitMap class allows to associate several binary flags,
    each of one is identified by a number from 0 to a count
    which can remain at zero or be positive : nbflags

    Flags lists over than numflag=0 are added after creation
    Each of one can be named, hence the user can identify it
    either by its flag number or by a name which gives a flag n0
    (flag n0 0 has no name)
    """

    @overload
    def __init__(self) -> None:
        """Creates a empty BitMap"""

    @overload
    def __init__(self, nbitems: int, resflags: int = 0) -> None:
        """
        Creates a BitMap for <nbitems> items
        One flag is defined, n0 0
        <resflags> prepares allocation for <resflags> more flags
        Flags values start at false
        """

    @overload
    def __init__(self, other: Interface_BitMap, copied: bool = False) -> None:
        """
        Creates a BitMap from another one
        if <copied> is True, copies data
        else, data are not copied, only the header object is
        """

    @overload
    def Initialize(self, nbitems: int, resflags: int = 0) -> None:
        """
        Initialize empty bit by <nbitems> items
        One flag is defined, n0 0
        <resflags> prepares allocation for <resflags> more flags
        Flags values start at false
        """

    @overload
    def Initialize(self, other: Interface_BitMap, copied: bool = False) -> None:
        """Initialize a BitMap from another one"""

    def Reservate(self, moreflags: int) -> None:
        """Reservates for a count of more flags"""

    def SetLength(self, nbitems: int) -> None:
        """
        Sets for a new count of items, which can be either less or
        greater than the former one
        For new items, their flags start at false
        """

    def AddFlag(self, name: str = '') -> int:
        """
        Adds a flag, a name can be attached to it
        Returns its flag number
        Makes required reservation
        """

    def AddSomeFlags(self, more: int) -> int:
        """
        Adds several flags (<more>) with no name
        Returns the number of last added flag
        """

    def RemoveFlag(self, num: int) -> bool:
        """
        Removes a flag given its number.
        Returns True if done, false if num is out of range
        """

    def SetFlagName(self, num: int, name: str) -> bool:
        """
        Sets a name for a flag, given its number
        name can be empty (to erase the name of a flag)
        Returns True if done, false if : num is out of range, or
        name non-empty already set to another flag
        """

    def NbFlags(self) -> int:
        """Returns the count of flags (flag 0 not included)"""

    def Length(self) -> int:
        """Returns the count of items (i.e. the length of the bitmap)"""

    def FlagName(self, num: int) -> str:
        """Returns the name recorded for a flag, or an empty string"""

    def FlagNumber(self, name: str) -> int:
        """Returns the number or a flag given its name, or zero"""

    def Value(self, item: int, flag: int = 0) -> bool:
        """
        Returns the value (true/false) of a flag, from :
        - the number of the item
        - the flag number, by default 0
        """

    def SetValue(self, item: int, val: bool, flag: int = 0) -> None:
        """Sets a new value for a flag"""

    def SetTrue(self, item: int, flag: int = 0) -> None:
        """Sets a flag to True"""

    def SetFalse(self, item: int, flag: int = 0) -> None:
        """Sets a flag to False"""

    def CTrue(self, item: int, flag: int = 0) -> bool:
        """
        Returns the former value for a flag and sets it to True
        (before : value returned; after : True)
        """

    def CFalse(self, item: int, flag: int = 0) -> bool:
        """
        Returns the former value for a flag and sets it to False
        (before : value returned; after : False)
        """

    def Init(self, val: bool, flag: int = 0) -> None:
        """
        Initialises all the values of Flag Number <flag> to a given
        value <val>
        """

    def Clear(self) -> None:
        """Clear all field of bit map"""

class Interface_GeneralLib:
    @overload
    def __init__(self) -> None:
        """
        Creates an empty Library : it will later by filled by method
        AddProtocol
        """

    @overload
    def __init__(self, aprotocol: Interface_Protocol | None) -> None:
        """
        Creates a Library which complies with a Protocol, that is :
        Same class (criterium IsInstance)
        This creation gets the Modules from the global set, those
        which are bound to the given Protocol and its Resources
        """

    @overload
    def __init__(self, theOther: Interface_GeneralLib) -> None: ...

    @staticmethod
    def SetGlobal(amodule: Interface_GeneralModule | None, aprotocol: Interface_Protocol | None) -> None:
        """
        Adds a couple (Module-Protocol) into the global definition set
        for this class of Library.
        """

    def AddProtocol(self, aprotocol: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds a couple (Module-Protocol) to the Library, given the
        class of a Protocol. Takes Resources into account.
        (if <aprotocol> is not of type TheProtocol, it is not added)
        """

    def Clear(self) -> None:
        """
        Clears the list of Modules of a library (can be used to
        redefine the order of Modules before action : Clear then
        refill the Library by calls to AddProtocol)
        """

    def SetComplete(self) -> None:
        """
        Sets a library to be defined with the complete Global list
        (all the couples Protocol/Modules recorded in it)
        """

    def Select(self, obj: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, Interface_GeneralModule, int]:
        """
        Selects a Module from the Library, given an Object.
        Returns True if Select has succeeded, False else.
        Also Returns (as arguments) the selected Module and the Case
        Number determined by the associated Protocol.
        If Select has failed, <module> is Null Handle and CN is zero.
        (Select can work on any criterium, such as Object DynamicType)
        """

    def Start(self) -> None:
        """Starts Iteration on the Modules (sets it on the first one)"""

    def More(self) -> bool:
        """Returns True if there are more Modules to iterate on"""

    def Next(self) -> None:
        """
        Iterates by getting the next Module in the list
        If there is none, the exception will be raised by Value
        """

    def Module(self) -> Interface_GeneralModule:
        """Returns the current Module in the Iteration"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the current Protocol in the Iteration"""

class Interface_GTool(nanoocp.Standard.Standard_Transient):
    """
    GTool - General Tool for a Model
    Provides the functions performed by Protocol/GeneralModule for
    entities of a Model, and recorded in a GeneralLib
    Optimized : once an entity has been queried, the GeneralLib is
    not longer queried
    Shareable between several users : as a Handle
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty, not set, GTool"""

    @overload
    def __init__(self, proto: Interface_Protocol | None, nbent: int = 0) -> None:
        """
        Creates a GTool from a Protocol
        Optional starting count of entities
        """

    @overload
    def __init__(self, theOther: Interface_GTool) -> None: ...

    def SetSignType(self, sign: Interface_SignType | None) -> None:
        """Sets a new SignType"""

    def SignType(self) -> Interface_SignType:
        """Returns the SignType. Can be null"""

    def SignValue(self, ent: nanoocp.Standard.Standard_Transient | None, model: Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient Object in a Model
        It calls SignType to do that
        If SignType is not defined, return ClassName of <ent>
        """

    def SignName(self) -> str:
        """Returns the Name of the SignType, or "Class Name\""""

    def SetProtocol(self, proto: Interface_Protocol | None, enforce: bool = False) -> None:
        """
        Sets a new Protocol
        if <enforce> is False and the new Protocol equates the old one
        then nothing is done
        """

    def Protocol(self) -> Interface_Protocol:
        """Returns the Protocol. Warning: it can be Null"""

    def Lib(self) -> Interface_GeneralLib:
        """Returns the GeneralLib itself"""

    def Reservate(self, nb: int, enforce: bool = False) -> None:
        """
        Reservates maps for a count of entities
        <enforce> False : minimum count
        <enforce> True  : clears former reservations
        Does not clear the maps
        """

    def ClearEntities(self) -> None:
        """
        Clears the maps which record, for each already recorded entity
        its Module and Case Number
        """

    def Select(self, ent: nanoocp.Standard.Standard_Transient | None, enforce: bool = False) -> tuple[bool, Interface_GeneralModule, int]:
        """
        Selects for an entity, its Module and Case Number
        It is optimised : once done for each entity, the result is
        mapped and the GeneralLib is not longer queried
        <enforce> True overpasses this optimisation
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_Category:
    """
    This class manages categories
    A category is defined by a name and a number, and can be
    seen as a way of rough classification, i.e. less precise than
    a cdl type.
    Hence, it is possible to dispatch every entity in about
    a dozen of categories, twenty is a reasonable maximum.

    Basically, the system provides the following categories :
    Shape (Geometry, BRep, CSG, Features, etc...)
    Drawing (Drawing, Views, Annotations, Pictures, Sketches ...)
    Structure (Component & Part, Groups & Patterns ...)
    Description (Meta-Data : Relations, Properties, Product ...)
    Auxiliary (those which do not enter in the above list)
    and some dedicated categories
    FEA, Kinematics, Piping, etc...
    plus Professional for other dedicated non-classed categories

    In addition, this class provides a way to compute then quickly
    query category numbers for an entire model.
    Values are just recorded as a list of numbers, control must
    then be done in a wider context (which must provide a Graph)
    """

    @overload
    def __init__(self) -> None:
        """Creates a Category, with no protocol yet"""

    @overload
    def __init__(self, theProtocol: Interface_Protocol | None) -> None:
        """Creates a Category with a given protocol"""

    @overload
    def __init__(self, theGTool: Interface_GTool | None) -> None:
        """Creates a Category with a given GTool"""

    @overload
    def __init__(self, theOther: Interface_Category) -> None: ...

    def SetProtocol(self, theProtocol: Interface_Protocol | None) -> None:
        """Sets/Changes Protocol"""

    def CatNum(self, theEnt: nanoocp.Standard.Standard_Transient | None, theShares: Interface_ShareTool) -> int:
        """
        Determines the Category Number for an entity in its context,
        by using general service CategoryNumber
        """

    def ClearNums(self) -> None:
        """Clears the recorded list of category numbers for a Model"""

    def Compute(self, theModel: Interface_InterfaceModel | None, theShares: Interface_ShareTool) -> None:
        """
        Computes the Category Number for each entity and records it,
        in an array (ent.number -> category number)
        Hence, it can be queried by the method Num.
        The Model itself is not recorded, this method is intended to
        be used in a wider context (which detains also a Graph, etc)
        """

    def Num(self, theNumEnt: int) -> int:
        """
        Returns the category number recorded for an entity number
        Returns 0 if out of range
        """

    @staticmethod
    def AddCategory(theName: str) -> int:
        """
        Records a new Category defined by its names, produces a number
        New if not yet recorded
        """

    @staticmethod
    def NbCategories() -> int:
        """Returns the count of recorded categories"""

    @staticmethod
    def Name(theNum: int) -> str:
        """Returns the name of a category, according to its number"""

    @staticmethod
    def Number(theName: str) -> int:
        """Returns the number of a category, according to its name"""

    @staticmethod
    def Init() -> None:
        """
        Default initialisation
        (protected against several calls : passes only once)
        """

class Interface_Check(nanoocp.Standard.Standard_Transient):
    """
    Defines a Check, as a list of Fail or Warning Messages under
    a literal form, which can be empty. A Check can also bring an
    Entity, which is the Entity to which the messages apply
    (this Entity may be any Transient Object).

    Messages can be stored in two forms : the definitive form
    (the only one by default), and another form, the original
    form, which can be different if it contains values to be
    inserted (integers, reals, strings)
    The original form can be more suitable for some operations
    such as counting messages
    """

    @overload
    def __init__(self) -> None:
        """
        Allows definition of a Sequence. Used also for Global Check
        of an InterfaceModel (which stores global messages for file)
        """

    @overload
    def __init__(self, anentity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Defines a Check on an Entity"""

    @overload
    def __init__(self, theOther: Interface_Check) -> None: ...

    def SendFail(self, amsg: nanoocp.Message.Message_Msg) -> None:
        """New name for AddFail (Msg)"""

    @overload
    def AddFail(self, amess: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Records a new Fail message"""

    @overload
    def AddFail(self, amess: nanoocp.TCollection.TCollection_HAsciiString | None, orig: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Records a new Fail message under two forms : final,original"""

    @overload
    def AddFail(self, amess: str, orig: str = '') -> None:
        """
        Records a new Fail message given as "error text" directly
        If <orig> is given, a distinct original form is recorded
        else (D), the original form equates <amess>
        """

    @overload
    def AddFail(self, amsg: nanoocp.Message.Message_Msg) -> None:
        """Records a new Fail from the definition of a Msg (Original+Value)"""

    def HasFailed(self) -> bool:
        """Returns True if Check brings at least one Fail Message"""

    def NbFails(self) -> int:
        """Returns count of recorded Fails"""

    def Fail(self, num: int, final: bool = True) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Fail Message as a String
        Final form by default, Original form if <final> is False
        """

    def CFail(self, num: int, final: bool = True) -> str:
        """
        Same as above, but returns a CString (to be printed ...)
        Final form by default, Original form if <final> is False
        """

    def Fails(self, final: bool = True) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of Fails, for a frontal-engine logic
        Final forms by default, Original forms if <final> is False
        Can be empty
        """

    def SendWarning(self, amsg: nanoocp.Message.Message_Msg) -> None:
        """New name for AddWarning"""

    @overload
    def AddWarning(self, amess: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Records a new Warning message"""

    @overload
    def AddWarning(self, amess: nanoocp.TCollection.TCollection_HAsciiString | None, orig: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Records a new Warning message under two forms : final,original"""

    @overload
    def AddWarning(self, amess: str, orig: str = '') -> None:
        """
        Records a Warning message given as "warning message" directly
        If <orig> is given, a distinct original form is recorded
        else (D), the original form equates <amess>
        """

    @overload
    def AddWarning(self, amsg: nanoocp.Message.Message_Msg) -> None:
        """Records a new Warning from the definition of a Msg (Original+Value)"""

    def HasWarnings(self) -> bool:
        """Returns True if Check brings at least one Warning Message"""

    def NbWarnings(self) -> int:
        """Returns count of recorded Warning messages"""

    def Warning(self, num: int, final: bool = True) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Warning message as a String
        Final form by default, Original form if <final> is False
        """

    def CWarning(self, num: int, final: bool = True) -> str:
        """
        Same as above, but returns a CString (to be printed ...)
        Final form by default, Original form if <final> is False
        """

    def Warnings(self, final: bool = True) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of Warnings, for a frontal-engine logic
        Final forms by default, Original forms if <final> is False
        Can be empty
        """

    def SendMsg(self, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Records an information message
        This does not change the status of the Check
        """

    def NbInfoMsgs(self) -> int:
        """Returns the count of recorded information messages"""

    def InfoMsg(self, num: int, final: bool = True) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns information message as a String"""

    def CInfoMsg(self, num: int, final: bool = True) -> str:
        """
        Same as above, but returns a CString (to be printed ...)
        Final form by default, Original form if <final> is False
        """

    def InfoMsgs(self, final: bool = True) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of Info Msg, for a frontal-engine logic
        Final forms by default, Original forms if <final> is False
        Can be empty
        """

    def Status(self) -> Interface_CheckStatus:
        """Returns the Check Status : OK, Warning or Fail"""

    @overload
    def Complies(self, status: Interface_CheckStatus) -> bool:
        """
        Tells if Check Status complies with a given one
        (i.e. also status for query)
        """

    @overload
    def Complies(self, mess: nanoocp.TCollection.TCollection_HAsciiString | None, incl: int, status: Interface_CheckStatus) -> bool:
        """
        Tells if a message is brought by a Check, as follows :
        <incl> = 0 : <mess> exactly matches one of the messages
        <incl> < 0 : <mess> is contained by one of the messages
        <incl> > 0 : <mess> contains one of the messages
        For <status> : for CheckWarning and CheckFail, considers only
        resp. Warning or Check messages. for CheckAny, considers all
        other values are ignored (answer will be false)
        """

    def HasEntity(self) -> bool:
        """
        Returns True if a Check is devoted to an entity; else, it is
        global (for InterfaceModel's storing of global error messages)
        """

    def Entity(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the entity on which the Check has been defined"""

    def Clear(self) -> None:
        """
        Clears a check, in order to receive information from transfer
        (Messages and Entity)
        """

    def ClearFails(self) -> None:
        """Clears the Fail Messages (for instance to keep only Warnings)"""

    def ClearWarnings(self) -> None:
        """Clears the Warning Messages (for instance to keep only Fails)"""

    def ClearInfoMsgs(self) -> None:
        """Clears the Info Messages"""

    def Remove(self, mess: nanoocp.TCollection.TCollection_HAsciiString | None, incl: int, status: Interface_CheckStatus) -> bool:
        """
        Removes the messages which comply with <mess>, as follows :
        <incl> = 0 : <mess> exactly matches one of the messages
        <incl> < 0 : <mess> is contained by one of the messages
        <incl> > 0 : <mess> contains one of the messages
        For <status> : for CheckWarning and CheckFail, considers only
        resp. Warning or Check messages. for CheckAny, considers all
        other values are ignored (nothing is done)
        Returns True if at least one message has been removed, False else
        """

    def Mend(self, pref: str, num: int = 0) -> bool:
        """
        Mends messages, according <pref> and <num>
        According to <num>, works on the whole list of Fails if = 0(D)
        or only one Fail message, given its rank
        If <pref> is empty, converts Fail(s) to Warning(s)
        Else, does the conversion but prefixes the new Warning(s) but
        <pref> followed by a semi-column
        Some reserved values of <pref> are :
        "FM" : standard prefix "Mended" (can be translated)
        "CF" : clears Fail(s)
        "CW" : clears Warning(s) : here, <num> refers to Warning list
        "CA" : clears all messages : here, <num> is ignored
        """

    def SetEntity(self, anentity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Receives an entity result of a Transfer"""

    def GetEntity(self, anentity: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        same as SetEntity (old form kept for compatibility)
        Warning : Does nothing if Entity field is not yet clear
        """

    def GetMessages(self, other: Interface_Check | None) -> None:
        """
        Copies messages stored in another Check, cumulating
        Does not regard other's Entity. Used to cumulate messages
        """

    def GetAsWarning(self, other: Interface_Check | None, failsonly: bool) -> None:
        """
        Copies messages converted into Warning messages
        If failsonly is true, only Fails are taken, and converted
        else, Warnings are taken too. Does not regard Entity
        Used to keep Fail messages as Warning, after a recovery
        """

    def Print(self, level: int, final: int = 1) -> str:
        """
        Prints the messages of the check to an Messenger
        <level> = 1 : only fails
        <level> = 2 : fails and warnings
        <level> = 3 : all (fails, warnings, info msg)
        <final> : if positive (D) prints final values of messages
        if negative, prints originals
        if null, prints both forms
        """

    def Trace(self, level: int = -1, final: int = 1) -> None:
        """
        Prints the messages of the check to the default trace file
        By default, according to the default standard level
        Else, according level (see method Print)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_InterfaceError(nanoocp.Standard.Standard_Failure):
    pass

class Interface_CheckFailure(Interface_InterfaceError):
    pass

class Interface_CheckIterator:
    """Result of a Check operation (especially from InterfaceModel)"""

    @overload
    def __init__(self) -> None:
        """Creates an empty CheckIterator"""

    @overload
    def __init__(self, name: str) -> None:
        """
        Creates a CheckIterator with a name (displayed by Print as a
        title)
        """

    @overload
    def __init__(self, theOther: Interface_CheckIterator) -> None: ...

    def __iter__(self) -> Interface_CheckIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> Interface_Check:
        """Python addition: see __iter__."""

    def SetName(self, name: str) -> None:
        """Sets / Changes the name"""

    def Name(self) -> str:
        """Returns the recorded name (can be empty)"""

    def SetModel(self, model: Interface_InterfaceModel | None) -> None:
        """
        Defines a Model, used to locate entities (not required, if it
        is absent, entities are simply less documented)
        """

    def Model(self) -> Interface_InterfaceModel:
        """Returns the stored model (can be a null handle)"""

    def Clear(self) -> None:
        """Clears the list of checks"""

    def Merge(self, other: Interface_CheckIterator) -> None:
        """
        Merges another CheckIterator into <me>, i.e. adds each of its
        Checks. Content of <other> remains unchanged.
        Takes also the Model but not the Name
        """

    def Add(self, ach: Interface_Check | None, num: int = 0) -> None:
        """
        Adds a Check to the list to be iterated
        This Check is Accompanied by Entity Number in the Model
        (0 for Global Check or Entity unknown in the Model), if 0 and
        Model is recorded in <me>, it is computed
        """

    @overload
    def Check(self, num: int) -> Interface_Check:
        """
        Returns the Check which was attached to an Entity given its
        Number in the Model. <num>=0 is for the Global Check.
        If no Check was recorded for this Number, returns an empty
        Check.
        Remark : Works apart from the iteration methods (no interference)
        """

    @overload
    def Check(self, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_Check:
        """
        Returns the Check attached to an Entity
        If no Check was recorded for this Entity, returns an empty
        Check.
        Remark : Works apart from the iteration methods (no interference)
        """

    @overload
    def CCheck(self, num: int) -> Interface_Check:
        """
        Returns the Check bound to an Entity Number (0 : Global)
        in order to be consulted or completed on the spot
        I.e. returns the Check if is already exists, or adds it then
        returns the new empty Check
        """

    @overload
    def CCheck(self, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_Check:
        """
        Returns the Check bound to an Entity, in order to be consulted
        or completed on the spot
        I.e. returns the Check if is already exists, or adds it then
        returns the new empty Check
        """

    def IsEmpty(self, failsonly: bool) -> bool:
        """
        Returns True if : no Fail has been recorded if <failsonly> is
        True, no Check at all if <failsonly> is False
        """

    def Status(self) -> Interface_CheckStatus:
        """Returns worst status among : OK, Warning, Fail"""

    def Complies(self, status: Interface_CheckStatus) -> bool:
        """
        Tells if this check list complies with a given status :
        OK (i.e. empty), Warning (at least one Warning, but no Fail),
        Fail (at least one), Message (not OK), NoFail, Any
        """

    @overload
    def Extract(self, status: Interface_CheckStatus) -> Interface_CheckIterator:
        """
        Returns a CheckIterator which contains the checks which comply
        with a given status
        Each check is added completely (no split Warning/Fail)
        """

    @overload
    def Extract(self, mess: str, incl: int, status: Interface_CheckStatus) -> Interface_CheckIterator:
        """
        Returns a CheckIterator which contains the check which comply
        with a message, plus some conditions as follows :
        <incl> = 0 : <mess> exactly matches one of the messages
        <incl> < 0 : <mess> is contained by one of the messages
        <incl> > 0 : <mess> contains one of the messages
        For <status> : for CheckWarning and CheckFail, considers only
        resp. Warning or Check messages. for CheckAny, considers all
        other values are ignored (answer will be false)
        Each Check which complies is entirely taken
        """

    def Remove(self, mess: str, incl: int, status: Interface_CheckStatus) -> bool:
        """
        Removes the messages of all Checks, under these conditions :
        <incl> = 0 : <mess> exactly matches one of the messages
        <incl> < 0 : <mess> is contained by one of the messages
        <incl> > 0 : <mess> contains one of the messages
        For <status> : for CheckWarning and CheckFail, considers only
        resp. Warning or Check messages. for CheckAny, considers all
        other values are ignored (nothing is done)
        Returns True if at least one message has been removed, False else
        """

    def Checkeds(self, failsonly: bool, global_: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities concerned by a Check
        Only fails if <failsonly> is True, else all non-empty checks
        If <global> is true, adds the model for a global check
        Else, global check is ignored
        """

    def Start(self) -> None:
        """
        Starts Iteration. Thus, it is possible to restart it
        Remark : an iteration may be done with a const Iterator
        While its content is modified (through a pointer), this allows
        to give it as a const argument to a function
        """

    def More(self) -> bool:
        """Returns True if there are more Checks to get"""

    def Next(self) -> None:
        """Sets Iteration to next Item"""

    def Value(self) -> Interface_Check:
        """
        Returns Check currently Iterated
        It brings all other information (status, messages, ...)
        The Number of the Entity in the Model is given by Number below
        """

    def Number(self) -> int:
        """
        Returns Number of Entity for the Check currently iterated
        or 0 for GlobalCheck
        """

    @overload
    def Print(self, failsonly: bool, final: int = 0) -> str:
        """
        Prints the list of Checks with their attached Numbers
        If <failsonly> is True, prints only Fail messages
        If <failsonly> is False, prints all messages
        If <final> = 0 (D), prints also original messages if different
        If <final> < 0, prints only original messages
        If <final> > 0, prints only final messages
        It uses the recorded Model if it is defined
        Remark : Works apart from the iteration methods (no interference)
        """

    @overload
    def Print(self, model: Interface_InterfaceModel | None, failsonly: bool, final: int = 0) -> str:
        """
        Works as Print without a model, but for entities which have
        no attached number (Number not positive), tries to compute
        this Number from <model> and displays "original" or "computed\"
        """

    def Destroy(self) -> None:
        """Clears data of iteration"""

class Interface_ShareTool:
    """
    Builds the Graph of Dependencies, from the General Service
    "Shared" -> builds for each Entity of a Model, the Shared and
    Sharing Lists, and gives access to them.
    Allows to complete with Implied References (which are not
    regarded as Shared Entities, but are nevertheless Referenced),
    this can be useful for Reference Checking
    """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None) -> None:
        """Same as above, but works with the GTool of the Model"""

    @overload
    def __init__(self, agraph: Interface_Graph) -> None:
        """
        Creates a ShareTool from an already defined Graph
        Remark that the data of the Graph are copied
        """

    @overload
    def __init__(self, ahgraph: Interface_HGraph | None) -> None:
        """
        Completes the Graph by Adding Implied References. Hence, they
        are considered as Sharing References in all the other queries
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, lib: Interface_GeneralLib) -> None:
        """
        Creates a ShareTool from a Model and builds all required data,
        by calling the General Service Library and Modules
        (GeneralLib given as an argument)
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, gtool: Interface_GTool | None) -> None:
        """Same a above, but GeneralLib is detained by a GTool"""

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, protocol: Interface_Protocol | None) -> None:
        """
        Same a above, but GeneralLib is defined through a Protocol
        Protocol is used to build the working library
        """

    @overload
    def __init__(self, theOther: Interface_ShareTool) -> None: ...

    def Model(self) -> Interface_InterfaceModel:
        """Returns the Model used for Creation (directly or for Graph)"""

    def Graph(self) -> Interface_Graph:
        """
        Returns the data used by the ShareTool to work
        Can then be used directly (read only)
        """

    def RootEntities(self) -> Interface_EntityIterator:
        """
        Returns the Entities which are not Shared (their Sharing List
        is empty) in the Model
        """

    def IsShared(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Returns True if <ent> is Shared by other Entities in the Model"""

    def Shareds(self, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_EntityIterator:
        """Returns the List of Entities Shared by a given Entity <ent>"""

    def Sharings(self, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_EntityIterator:
        """Returns the List of Entities Sharing a given Entity <ent>"""

    def NbTypedSharings(self, ent: nanoocp.Standard.Standard_Transient | None, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns the count of Sharing Entities of an Entity, which
        are Kind of a given Type
        """

    def TypedSharing(self, ent: nanoocp.Standard.Standard_Transient | None, atype: nanoocp.Standard.Standard_Type | None) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Sharing Entity of an Entity, which is Kind of a
        given Type. Allows to access a Sharing Entity of a given type
        when there is one and only one (current case)
        """

    def All(self, ent: nanoocp.Standard.Standard_Transient | None, rootlast: bool = True) -> Interface_EntityIterator:
        """
        Returns the complete list of entities shared by <ent> at any
        level, including <ent> itself
        If <ent> is the Model, considers the concatenation of
        AllShared for each root
        If <rootlast> is True (D), the list starts with lower level
        entities and ends by the root. Else, the root is first and
        the lower level entities are at end
        """

    def Print(self, iter: Interface_EntityIterator) -> str:
        """
        Utility method which Prints the content of an iterator
        (by their Numbers)
        """

class Interface_CheckTool:
    """
    Performs Checks on Entities, using General Service Library and
    Modules to work. Works on one Entity or on a complete Model
    """

    @overload
    def __init__(self, model: Interface_InterfaceModel | None) -> None:
        """
        Creates a CheckTool, by calling the General Service Library
        and Modules, selected through a Protocol, to work on a Model
        Protocol and so on are taken from the Model (its GTool)
        """

    @overload
    def __init__(self, graph: Interface_Graph) -> None:
        """
        Creates a CheckTool from a Graph. The Graph contains a Model
        which designates a Protocol: they are used to create ShareTool
        """

    @overload
    def __init__(self, hgraph: Interface_HGraph | None) -> None: ...

    @overload
    def __init__(self, model: Interface_InterfaceModel | None, protocol: Interface_Protocol | None) -> None:
        """
        Creates a CheckTool, by calling the General Service Library
        and Modules, selected through a Protocol, to work on a Model
        Moreover, Protocol recognizes Unknown Entities
        """

    @overload
    def __init__(self, theOther: Interface_CheckTool) -> None: ...

    def FillCheck(self, ent: nanoocp.Standard.Standard_Transient | None, sh: Interface_ShareTool) -> Interface_Check:
        """
        Fills as required a Check with the Error and Warning messages
        produced by Checking a given Entity.
        For an Erroneous or Corrected Entity : Check build at Analyse
        time; else, Check computed for Entity (Verify integrity), can
        use a Graph as required to control context
        """

    @overload
    def Print(self, ach: Interface_Check | None) -> str:
        """Utility method which Prints the content of a Check"""

    @overload
    def Print(self, list: Interface_CheckIterator) -> str:
        """
        Simply Lists all the Checks and the Content (messages) and the
        Entity, if there is, of each Check
        (if all Checks are OK, nothing is Printed)
        """

    def Check(self, num: int) -> Interface_Check:
        """
        Returns the Check associated to an Entity identified by
        its Number in a Model.
        """

    def CheckSuccess(self, reset: bool = False) -> None:
        """
        Checks if any Error has been detected (CheckList not empty)
        Returns normally if none, raises exception if some exists.
        It reuses the last computations from other checking methods,
        unless the argument <reset> is given True
        """

    def CompleteCheckList(self) -> Interface_CheckIterator:
        """
        Returns list of all "remarkable" information, which include :
        - GlobalCheck, if not empty
        - Error Checks, for all Errors (Verify + Analyse)
        - also Corrected Entities
        - and Unknown Entities : for those, each Unknown Entity is
        associated to an empty Check (it is neither an Error nor a
        Correction, but a remarkable information)
        """

    def CheckList(self) -> Interface_CheckIterator:
        """
        Returns list of all Errors detected
        Note that presence of Unknown Entities is not an error
        Cumulates : GlobalCheck if error +
        AnalyseCheckList + VerifyCheckList
        """

    def AnalyseCheckList(self) -> Interface_CheckIterator:
        """
        Returns list of errors detected at Analyse time (syntactic)
        (note that GlobalCheck is not in this list)
        """

    def VerifyCheckList(self) -> Interface_CheckIterator:
        """
        Returns list of integrity constraints errors (semantic)
        (note that GlobalCheck is not in this list)
        """

    def WarningCheckList(self) -> Interface_CheckIterator:
        """Returns list of Corrections (includes GlobalCheck if corrected)"""

    def UnknownEntities(self) -> Interface_EntityIterator:
        """
        Returns list of Unknown Entities
        Note that Error and Erroneous Entities are not considered
        as Unknown
        """

class Interface_CopyControl(nanoocp.Standard.Standard_Transient):
    """
    This deferred class describes the services required by
    CopyTool to work. They are very simple and correspond
    basically to the management of an indexed map.
    But they can be provided by various classes which can
    control a Transfer. Each Starting Entity have at most
    one Result (Mapping one-one)
    """

    def Clear(self) -> None:
        """
        Clears List of Copy Results. Gets Ready to begin another Copy
        Process.
        """

    def Bind(self, ent: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """Bind a Result to a Starting Entity identified by its Number"""

    def Search(self, ent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Searches for the Result bound to a Startingf Entity identified
        by its Number.
        If Found, returns True and fills <res>
        Else, returns False and nullifies <res>
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_CopyMap(Interface_CopyControl):
    """
    Manages a Map for the need of single Transfers, such as Copies
    In such transfer, Starting Entities are read from a unique
    Starting Model, and each transferred Entity is bound to one
    and only one Result, which cannot be changed later.
    """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None) -> None:
        """Creates a CopyMap adapted to work from a Model"""

    @overload
    def __init__(self, theOther: Interface_CopyMap) -> None: ...

    def Clear(self) -> None:
        """Clears Transfer List. Gets Ready to begin another Transfer"""

    def Model(self) -> Interface_InterfaceModel:
        """Returns the InterfaceModel used at Creation time"""

    def Bind(self, ent: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Binds a Starting Entity identified by its Number <num> in the
        Starting Model, to a Result of Transfer <res>
        """

    def Search(self, ent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Search for the result of a Starting Object (i.e. an Entity,
        identified by its Number <num> in the Starting Model)
        Returns True  if a  Result is Bound (and fills <res>)
        Returns False if no result is Bound (and nullifies <res>)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_CopyTool:
    """
    Performs Deep Copies of sets of Entities
    Allows to perform Copy of Interface Entities from a Model to
    another one. Works by calling general services GetFromAnother
    and GetImplied.
    Uses a CopyMap to bind a unique Result to each Copied Entity

    It is possible to command Copies of Entities (and those they
    reference) by call to the General Service Library, or to
    enforce results for transfer of some Entities (calling Bind)

    A Same CopyTool can be used for several successive Copies from
    the same Model : either by restarting from scratch (e.g. to
    copy different parts of a starting Model to several Targets),
    or incremental : in that case, it is possible to know what is
    the content of the last increment (defined by last call to
    ClearLastFlags and queried by call to LastCopiedAfter)

    Works in two times : first, create the list of copied Entities
    second, pushes them to a target Model (manages also Model's
    Header) or returns the Result as an Iterator, as desired

    The core action (Copy) works by using ShallowCopy (method
    attached to each class) and Copy from GeneralLib (itself using
    dedicated tools). It can be redefined for specific actions.
    """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None) -> None:
        """Same as above, but works with the Active Protocol"""

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, lib: Interface_GeneralLib) -> None:
        """
        Creates a CopyTool adapted to work from a Model. Works
        with a General Service Library, given as an argument
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, protocol: Interface_Protocol | None) -> None:
        """Same as above, but Library is defined through a Protocol"""

    @overload
    def __init__(self, theOther: Interface_CopyTool) -> None: ...

    def Model(self) -> Interface_InterfaceModel:
        """Returns the Model on which the CopyTool works"""

    def SetControl(self, othermap: Interface_CopyControl | None) -> None:
        """
        Changes the Map of Result for another one. This allows to work
        with a more sophisticated Mapping Control than the Standard
        one which is CopyMap (e.g. TransferProcess from Transfer)
        """

    def Control(self) -> Interface_CopyControl:
        """Returns the object used for Control"""

    def Clear(self) -> None:
        """Clears Transfer List. Gets Ready to begin another Transfer"""

    def Copy(self, entfrom: nanoocp.Standard.Standard_Transient | None, mapped: bool, errstat: bool) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Creates the CounterPart of an Entity (by ShallowCopy), Binds
        it, then Copies the content of the former Entity to the other
        one (same Type), by call to the General Service Library
        It may command the Copy of Referenced Entities
        Then, its returns True.

        If <mapped> is True, the Map is used to store the Result
        Else, the Result is simply produced : it can be used to Copy
        internal sub-parts of Entities, which are not intended to be
        shared (Strings, Arrays, etc...)
        If <errstat> is True, this means that the Entity is recorded
        in the Model as Erroneous : in this case, the General Service
        for Deep Copy is not called (this could be dangerous) : hence
        the Counter-Part is produced but empty, it can be referenced.

        This method does nothing and returns False if the Protocol
        does not recognize <ent>.
        It basically makes a Deep Copy without changing the Types.
        It can be redefined for special uses.
        """

    def Transferred(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Transient:
        """
        Transfers one Entity, if not yet bound to a result
        Remark : For an Entity which is reported in the Starting Model,
        the ReportEntity will also be copied with its Content if it
        has one (at least ShallowCopy; Complete Copy if the Protocol
        recognizes the Content : see method Copy)
        """

    def Bind(self, ent: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Defines a Result for the Transfer of a Starting object.
        Used by method Transferred (which performs a normal Copy),
        but can also be called to enforce a result : in the latter
        case, the enforced result must be compatible with the other
        Transfers which are performed
        """

    def Search(self, ent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Search for the result of a Starting Object (i.e. an Entity)
        Returns True if a Result is Bound (and fills "result")
        Returns False if no result is Bound
        """

    def ClearLastFlags(self) -> None:
        """
        Clears LastFlags only. This allows to know what Entities are
        copied after its call (see method LastCopiedAfter). It can be
        used when copies are done by increments, which must be
        distinguished. ClearLastFlags is also called by Clear.
        """

    def LastCopiedAfter(self, numfrom: int) -> tuple[int, nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]:
        """
        Returns an copied Entity and its Result which were operated
        after last call to ClearLastFlags. It returns the first
        "Last Copied Entity" which Number follows <numfrom>, Zero if
        none. It is used in a loop as follow :
        Integer num = 0;
        while ( (num = CopyTool.LastCopiedAfter(num,ent,res)) ) {
        .. Process Starting <ent> and its Result <res>
        }
        """

    def TransferEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Transfers one Entity and records result into the Transfer List
        Calls method Transferred
        """

    def RenewImpliedRefs(self) -> None:
        """
        Renews the Implied References. These References do not involve
        Copying of referenced Entities. For such a Reference, if the
        Entity which defines it AND the referenced Entity are both
        copied, then this Reference is renewed. Else it is deleted in
        the copied Entities.
        Remark : this concerns only some specific references, such as
        "back pointers".
        """

    def FillModel(self, bmodel: Interface_InterfaceModel | None) -> None:
        """
        Fills a Model with the result of the transfer (TransferList)
        Commands copy of Header too, and calls RenewImpliedRefs
        """

    def CompleteResult(self, withreports: bool = False) -> Interface_EntityIterator:
        """
        Returns the complete list of copied Entities
        If <withreports> is given True, the entities which were
        reported in the Starting Model are replaced in the list
        by the copied ReportEntities
        """

    def RootResult(self, withreports: bool = False) -> Interface_EntityIterator:
        """
        Returns the list of Root copied Entities (those which were
        asked for copy by the user of CopyTool, not by copying
        another Entity)
        """

class Interface_EntityCluster(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary class for EntityList. An EntityList designates an
    EntityCluster, which brings itself an fixed maximum count of
    Entities. If it is full, it gives access to another cluster
    ("Next"). This class is intended to give a good compromise
    between access time (faster than a Sequence, good for little
    count) and memory use (better than a Sequence in any case,
    overall for little count, better than an Array for a very
    little count. It is designed for a light management.
    Remark that a new Item may not be Null, because this is the
    criterium used for "End of List\"
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty, non-chained, EntityCluster"""

    @overload
    def __init__(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Creates a non-chained EntityCluster, filled with one Entity"""

    @overload
    def __init__(self, ec: Interface_EntityCluster | None) -> None:
        """
        Creates an empty EntityCluster, chained with another one
        (that is, put BEFORE this other one in the list)
        """

    @overload
    def __init__(self, ant: nanoocp.Standard.Standard_Transient | None, ec: Interface_EntityCluster | None) -> None:
        """
        Creates an EntityCluster, filled with a first Entity, and
        chained to another EntityCluster (BEFORE it, as above)
        """

    @overload
    def __init__(self, theOther: Interface_EntityCluster) -> None: ...

    def Append(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Appends an Entity to the Cluster. If it is not full, adds the
        entity directly inside itself. Else, transmits to its Next
        and Creates it if it does not yet exist
        """

    @overload
    def Remove(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Removes an Entity from the Cluster. If it is not found, calls
        its Next one to do so.
        Returns True if it becomes itself empty, False else
        (thus, a Cluster which becomes empty is deleted from the list)
        """

    @overload
    def Remove(self, num: int) -> bool:
        """
        Removes an Entity from the Cluster, given its rank. If <num>
        is greater than NbLocal, calls its Next with (num - NbLocal),
        Returns True if it becomes itself empty, False else
        """

    def NbEntities(self) -> int:
        """Returns total count of Entities (including Next)"""

    def Value(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Entity identified by its rank in the list
        (including Next)
        """

    def SetValue(self, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Changes an Entity given its rank."""

    def FillIterator(self, iter: Interface_EntityIterator) -> None:
        """Fills an Iterator with designated Entities (includes Next)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_EntityIterator:
    """
    Defines an Iterator on Entities.
    Allows considering of various criteria
    """

    @overload
    def __init__(self) -> None:
        """Defines an empty iterator (see AddList & AddItem)"""

    @overload
    def __init__(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Defines an iterator on a list, directly i.e. without copying it"""

    @overload
    def __init__(self, theOther: Interface_EntityIterator) -> None: ...

    def __iter__(self) -> Interface_EntityIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.Standard.Standard_Transient:
        """Python addition: see __iter__."""

    def AddList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Gets a list of entities and adds its to the iteration list"""

    def AddItem(self, anentity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds to the iteration list a defined entity"""

    def GetOneItem(self, anentity: nanoocp.Standard.Standard_Transient | None) -> None:
        """same as AddItem (kept for compatibility)"""

    def SelectType(self, atype: nanoocp.Standard.Standard_Type | None, keep: bool) -> None:
        """
        Selects entities with are Kind of a given type, keep only
        them (is keep is True) or reject only them (if keep is False)
        """

    def NbEntities(self) -> int:
        """
        Returns count of entities which will be iterated on
        Calls Start if not yet done
        """

    def NbTyped(self, type: nanoocp.Standard.Standard_Type | None) -> int:
        """Returns count of entities of a given type (kind of)"""

    def Typed(self, type: nanoocp.Standard.Standard_Type | None) -> Interface_EntityIterator:
        """Returns the list of entities of a given type (kind of)"""

    def Start(self) -> None:
        """Allows re-iteration (useless for the first iteration)"""

    def More(self) -> bool:
        """
        Says if there are other entities (vertices) to iterate
        the first time, calls Start
        """

    def Next(self) -> None:
        """Sets iteration to the next entity (vertex) to give"""

    def Value(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the current Entity iterated, to be used by Interface
        tools
        """

    def Content(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the content of the Iterator, accessed through a Handle
        to be used by a frontal-engine logic
        Returns an empty Sequence if the Iterator is empty
        Calls Start if not yet done
        """

    def Destroy(self) -> None:
        """Clears data of iteration"""

class Interface_EntityList:
    """
    This class defines a list of Entities (Transient Objects),
    it can be used as a field of other Transient classes, with
    these features :
    - oriented to define a little list, that is, slower than an
    Array or a Map of Entities for a big count (about 100 and
    over), but faster than a Sequence
    - allows to work as a Sequence, limited to Clear, Append,
    Remove, Access to an Item identified by its rank in the list
    - space saving, compared to a Sequence, especially for little
    amounts; better than an Array for a very little amount (less
    than 10) but less good for a greater amount

    Works in conjunction with EntityCluster
    An EntityList gives access to a list of Entity Clusters, which
    are chained (in one sense : Single List)
    Remark : a new Item may not be Null, because this is the
    criterium used for "End of List\"
    """

    @overload
    def __init__(self) -> None:
        """Creates a List as being empty"""

    @overload
    def __init__(self, theOther: Interface_EntityList) -> None: ...

    def Clear(self) -> None:
        """Clears the List"""

    def Append(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Appends an Entity, that is to the END of the list
        (keeps order, but works slowerly than Add, see below)
        """

    def Add(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds an Entity to the list, that is, with NO REGARD about the
        order (faster than Append if count becomes greater than 10)
        """

    @overload
    def Remove(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Removes an Entity from the list, if it is there"""

    @overload
    def Remove(self, num: int) -> None:
        """Removes an Entity from the list, given its rank"""

    def IsEmpty(self) -> bool:
        """Returns True if the list is empty"""

    def NbEntities(self) -> int:
        """Returns count of recorded Entities"""

    def Value(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an Item given its number. Beware about the way the
        list was filled (see above, Add and Append)
        """

    def SetValue(self, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Returns an Item given its number. Beware about the way the
        list was filled (see above, Add and Append)
        """

    def FillIterator(self, iter: Interface_EntityIterator) -> None:
        """
        fills an Iterator with the content of the list
        (normal way to consult a list which has been filled with Add)
        """

    def NbTypedEntities(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """Returns count of Entities of a given Type (0 : none)"""

    def TypedEntity(self, atype: nanoocp.Standard.Standard_Type | None, num: int = 0) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Entity which is of a given type.
        If num = 0 (D), there must be ONE AND ONLY ONE
        If num > 0, returns the num-th entity of this type
        """

class Interface_FileParameter:
    """
    Auxiliary class to store a literal parameter in a file
    intermediate directory or in an UndefinedContent : a reference
    type Parameter detains an Integer which is used to address a
    record in the directory.
    FileParameter is intended to be stored in a ParamSet : hence
    memory management is performed by ParamSet, which calls Clear
    to work, while the Destructor (see Destroy) does nothing.
    Also a FileParameter can be read for consultation only, not to
    be read from a Structure to be included into another one.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Interface_FileParameter) -> None: ...

    @overload
    def Init(self, val: nanoocp.TCollection.TCollection_AsciiString, typ: Interface_ParamType) -> None:
        """Fills fields (with Entity Number set to zero)"""

    @overload
    def Init(self, val: str, typ: Interface_ParamType) -> None:
        """Same as above, but builds the Value from a CString"""

    def CValue(self) -> str:
        """
        Same as above, but as a CString (for immediate exploitation)
        was C++ : return const
        """

    def ParamType(self) -> Interface_ParamType:
        """Returns the type of the parameter"""

    def SetEntityNumber(self, num: int) -> None:
        """Allows to set a reference to an Entity in a numbered list"""

    def EntityNumber(self) -> int:
        """Returns value set by SetEntityNumber"""

    def Clear(self) -> None:
        """Clears stored data : frees memory taken for the String Value"""

    def Destroy(self) -> None:
        """Destructor. Does nothing because Memory is managed by ParamSet"""

class Interface_FileReaderData(nanoocp.Standard.Standard_Transient):
    """
    This class defines services which permit to access Data issued
    from a File, in a form which does not depend of physical
    format : thus, each Record has an attached ParamList (to be
    managed) and resulting Entity.

    Each Interface defines its own FileReaderData : on one hand by
    defining deferred methods given here, on the other hand by
    describing literal data and their accesses, with the help of
    basic classes such as String, Array1OfString, etc...

    FileReaderData is used by a FileReaderTool, which is also
    specific of each Norm, to read an InterfaceModel of the Norm
    FileReaderData inherits TShared to be accessed by Handle :
    this allows FileReaderTool to define more easily the specific
    methods, and improves memory management.
    """

    def NbRecords(self) -> int:
        """
        Returns the count of registered records
        That is, value given for Initialization (can be redefined)
        """

    def NbEntities(self) -> int:
        """
        Returns the count of entities. Depending of each norm, records
        can be Entities or SubParts (SubList in STEP, SubGroup in SET
        ...). NbEntities counts only Entities, not Subs
        Used for memory reservation in InterfaceModel
        Default implementation uses FindNextRecord
        Can be redefined into a more performant way
        """

    def FindNextRecord(self, num: int) -> int:
        """
        Determines the record number defining an Entity following a
        given record number. Specific to each sub-class of
        FileReaderData. Returning zero means no record found
        """

    def InitParams(self, num: int) -> None:
        """attaches an empty ParamList to a Record"""

    @overload
    def AddParam(self, num: int, aval: str, atype: Interface_ParamType, nument: int = 0) -> None:
        """
        Adds a parameter to record no "num" and fills its fields
        (EntityNumber is optional)
        Warning : <aval> is assumed to be memory-managed elsewhere : it is NOT
        copied. This gives a best speed : strings remain stored in
        pages of characters
        """

    @overload
    def AddParam(self, num: int, aval: nanoocp.TCollection.TCollection_AsciiString, atype: Interface_ParamType, nument: int = 0) -> None:
        """
        Same as above, but gets a AsciiString from TCollection
        Remark that the content of the AsciiString is locally copied
        (because its content is most often lost after using)
        """

    @overload
    def AddParam(self, num: int, FP: Interface_FileParameter) -> None:
        """
        Same as above, but gets a complete FileParameter
        Warning : Content of <FP> is NOT copied : its original address and space
        in memory are assumed to be managed elsewhere (see ParamSet)
        """

    def SetParam(self, num: int, nump: int, FP: Interface_FileParameter) -> None:
        """
        Sets a new value for a parameter of a record, given by :
        num : record number; nump : parameter number in the record
        """

    def NbParams(self, num: int) -> int:
        """
        Returns count of parameters attached to record "num"
        If <num> = 0, returns the total recorded count of parameters
        """

    def Params(self, num: int) -> Interface_ParamList:
        """
        Returns the complete ParamList of a record (read only)
        num = 0 to return the whole param list for the file
        """

    def Param(self, num: int, nump: int) -> Interface_FileParameter:
        """
        Returns parameter "nump" of record "num", as a complete
        FileParameter
        """

    def ChangeParam(self, num: int, nump: int) -> Interface_FileParameter:
        """Same as above, but in order to be modified on place"""

    def ParamType(self, num: int, nump: int) -> Interface_ParamType:
        """
        Returns type of parameter "nump" of record "num"
        Returns literal value of parameter "nump" of record "num"
        was C++ : return const &
        """

    def ParamCValue(self, num: int, nump: int) -> str:
        """
        Same as above, but as a CString
        was C++ : return const
        """

    def IsParamDefined(self, num: int, nump: int) -> bool:
        """
        Returns True if parameter "nump" of record "num" is defined
        (it is not if its type is ParamVoid)
        """

    def ParamNumber(self, num: int, nump: int) -> int:
        """
        Returns record number of an entity referenced by a parameter
        of type Ident; 0 if no EntityNumber has been determined
        Note that it is used to reference Entities but also Sublists
        (sublists are not objects, but internal descriptions)
        """

    def ParamEntity(self, num: int, nump: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the StepEntity referenced by a parameter
        Error if none
        """

    def ParamFirstRank(self, num: int) -> int:
        """
        Returns the absolute rank of the beginning of a record
        (its list is from ParamFirstRank+1 to ParamFirstRank+NbParams)
        """

    def BoundEntity(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns the entity bound to a record, set by SetEntities"""

    def BindEntity(self, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Binds an entity to a record"""

    def SetErrorLoad(self, val: bool) -> None:
        """
        Sets the status "Error Load" on, to overside check fails
        <val> True  : declares unloaded
        <val> False : declares loaded
        If not called before loading (see FileReaderTool), check fails
        give the status
        IsErrorLoad says if SetErrorLoad has been called by user
        ResetErrorLoad resets it (called by FileReaderTool)
        This allows to specify that the currently loaded entity
        remains unloaded (because of syntactic fail)
        """

    def IsErrorLoad(self) -> bool:
        """
        Returns True if the status "Error Load" has been set (to True
        or False)
        """

    def ResetErrorLoad(self) -> bool:
        """
        Returns the former value of status "Error Load" then resets it
        Used to read the status then ensure it is reset
        """

    def Destroy(self) -> None:
        """Destructor (waiting for memory management)"""

    @staticmethod
    def Fastof(str: str) -> float:
        """Same spec.s as standard <atof> but 5 times faster"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_FileReaderTool:
    """
    Defines services which are required to load an InterfaceModel
    from a File. Typically, it may firstly transform a system
    file into a FileReaderData object, then work on it, not longer
    considering file contents, to load an Interface Model.
    It may also work on a FileReaderData already loaded.

    FileReaderTool provides, on one hand, some general services
    which are common to all read operations but can be redefined,
    plus general actions to be performed specifically for each
    Norm, as deferred methods to define.

    In particular, FileReaderTool defines the Interface's Unknown
    and Error entities
    """

    def SetData(self, reader: Interface_FileReaderData | None, protocol: Interface_Protocol | None) -> None:
        """Sets Data to a FileReaderData. Works with a Protocol"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the Protocol given at creation time"""

    def Data(self) -> Interface_FileReaderData:
        """Returns the FileReaderData which is used to work"""

    def SetModel(self, amodel: Interface_InterfaceModel | None) -> None:
        """Stores a Model. Used when the Model has been loaded"""

    def Model(self) -> Interface_InterfaceModel:
        """Returns the stored Model"""

    def SetMessenger(self, messenger: nanoocp.Message.Message_Messenger | None) -> None:
        """Sets Messenger used for outputting messages"""

    def Messenger(self) -> nanoocp.Message.Message_Messenger:
        """
        Returns Messenger used for outputting messages.
        The returned object is guaranteed to be non-null;
        default is Message::Messenger().
        """

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

    def SetErrorHandle(self, err: bool) -> None:
        """
        Allows controlling whether exception raisings are handled
        If err is False, they are not (hence, dbx can take control)
        If err is True, they are, and they are traced
        (by putting on messenger Entity's Number and file record num)
        Default given at Model's creation time is True
        """

    def ErrorHandle(self) -> bool:
        """Returns ErrorHandle flag"""

    def SetEntities(self) -> None:
        """
        Fills records with empty entities; once done, each entity can
        ask the FileReaderTool for any entity referenced through an
        identifier. Calls Recognize which is specific to each specific
        type of FileReaderTool
        """

    def Recognize(self, num: int) -> tuple[bool, Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        Recognizes a record, given its number. Specific to each
        Interface; called by SetEntities. It can call the basic method
        RecognizeByLib.
        Returns False if recognition has failed, True else.
        <ach> has not to be filled if simply Recognition has failed :
        it must record true error messages : RecognizeByLib can
        generate error messages if NewRead is called

        Note that it works thru a Recognizer (method Evaluate) which
        has to be memorized before starting
        """

    def RecognizeByLib(self, num: int, glib: Interface_GeneralLib, rlib: Interface_ReaderLib) -> tuple[bool, Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        Recognizes a record with the help of Libraries. Can be used
        to implement the method Recognize.
        <rlib> is used to find Protocol and CaseNumber to apply
        <glib> performs the creation (by service NewVoid, or NewRead
        if NewVoid gave no result)
        <ach> is a check, which is transmitted to NewRead if it is
        called, gives a result but which is false
        <ent> is the result
        Returns False if recognition has failed, True else
        """

    def UnknownEntity(self) -> nanoocp.Standard.Standard_Transient:
        """
        Provides an unknown entity, specific to the Interface
        called by SetEntities when Recognize has failed (Unknown alone)
        or by LoadModel when an Entity has caused a Fail on reading
        (to keep at least its literal description)
        Uses Protocol to do it
        """

    def NewModel(self) -> Interface_InterfaceModel:
        """Creates an empty Model of the norm. Uses Protocol to do it"""

    def LoadModel(self, amodel: Interface_InterfaceModel | None) -> None:
        """
        Reads and fills Entities from the FileReaderData set by
        SetData to an InterfaceModel.
        It enchains required operations, the specific ones correspond
        to deferred methods (below) to be defined for each Norm.
        It manages also error recovery and trace.
        Remark : it calls SetModel.
        It Can raise any error which can occur during a load
        operation, unless Error Handling is set.
        This method can also be redefined if judged necessary.
        """

    def LoadedEntity(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        Reads, Fills and Returns one Entity read from a Record of the
        FileReaderData. This Method manages also case of Fail or
        Warning, by producing a ReportEntyty plus , for a Fail, a
        literal Content (as an UnknownEntity). Performs also Trace
        """

    def BeginRead(self, amodel: Interface_InterfaceModel | None) -> None:
        """
        Fills model's header; each Interface defines for its Model its
        own file header; this method fills it from FileReaderTool.+
        It is called by AnalyseFile from InterfaceModel
        """

    def AnalyseRecord(self, num: int, anent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, Interface_Check]:
        """
        Fills an Entity, given record no; specific to each Interface,
        called by AnalyseFile from InterfaceModel (which manages its
        calling arguments)
        To work, each Interface can define a method in its proper
        Transient class, like this (given as an example) :
        AnalyseRecord (me : mutable; FR : in out FileReaderTool;
        num : Integer; acheck : in out Check)
        returns Boolean;
        and call it from AnalyseRecord

        Returned Value : True if the entity could be loaded, False
        else (in case of syntactic fail)
        """

    def EndRead(self, amodel: Interface_InterfaceModel | None) -> None:
        """
        Ends file reading after reading all the entities
        default is doing nothing; redefinable as necessary
        """

    def Clear(self) -> None:
        """Clear fields"""

class Interface_FloatWriter:
    """
    This class converts a floating number (Real) to a string
    It can be used if the standard C-C++ output functions
    (Sprintf or std::cout<<) are not convenient. That is to say :
    - to suppress trailing '0' and 'E+00' (if desired)
    - to control exponent output and floating point output

    Formats are given in the form used by printf-Sprintf
    """

    @overload
    def __init__(self, chars: int = 0) -> None:
        """
        Creates a FloatWriter ready to work, with default options
        - zero suppress option is set
        - main format is set to "%E"
        - secondary format is set to "%f" for values between 0.1 and
        1000. in absolute values
        If <chars> is given (and positive), it will produce options
        to produce this count of characters : "%<chars>f","%<chars>%E\"
        """

    @overload
    def __init__(self, theOther: Interface_FloatWriter) -> None: ...

    def SetFormat(self, form: str, reset: bool = True) -> None:
        """
        Sets a specific Format for Sending Reals (main format)
        (Default from Creation is "%E")
        If <reset> is given True (default), this call clears effects
        of former calls to SetFormatForRange and SetZeroSuppress
        """

    def SetFormatForRange(self, form: str, R1: float, R2: float) -> None:
        """
        Sets a secondary Format for Real, to be applied between R1 and
        R2 (in absolute values). A Call to SetRealForm cancels this
        secondary form if <reset> is True.
        (Default from Creation is "%f" between 0.1 and 1000.)
        Warning : if the condition (0. <= R1 < R2) is not fulfilled, this
        secondary form is canceled.
        """

    def SetZeroSuppress(self, mode: bool) -> None:
        """
        Sets Sending Real Parameters to suppress trailing Zeros and
        Null Exponent ("E+00"), if <mode> is given True, Resets this
        mode if <mode> is False (in addition to Real Forms)
        A call to SetRealFrom resets this mode to False ig <reset> is
        given True (Default from Creation is True)
        """

    def SetDefaults(self, chars: int = 0) -> None:
        """Sets again options to the defaults given by Create"""

    def Options(self) -> tuple[bool, bool, float, float]:
        """
        Returns active options : <zerosup> is the option ZeroSuppress,
        <range> is True if a range is set, False else
        R1,R2 give the range (if it is set)
        """

    def MainFormat(self) -> str:
        """
        Returns the main format
        was C++ : return const
        """

    def FormatForRange(self) -> str:
        """
        Returns the format for range, if set
        Meaningful only if <range> from Options is True
        was C++ : return const
        """

    def Write(self, val: float, text: str) -> int:
        """
        Writes a Real value <val> to a string <text> by using the
        options. Returns the useful Length of produced string.
        It calls the class method Convert.
        Warning : <text> is assumed to be wide enough (20-30 is correct)
        And, even if declared in, its content will be modified
        """

    @staticmethod
    def Convert(val: float, text: str, zerosup: bool, Range1: float, Range2: float, mainform: str, rangeform: str) -> int:
        """
        This class method converts a Real Value to a string, given
        options given as arguments. It can be called independently.
        Warning : even if declared in, content of <text> will be modified
        """

class Interface_GeneralModule(nanoocp.Standard.Standard_Transient):
    """
    This class defines general services, which must be provided
    for each type of Entity (i.e. of Transient Object processed
    by an Interface) : Shared List, Check, Copy, Delete, Category

    To optimise processing (e.g. firstly bind an Entity to a Module
    then calls Module), each recognized Entity Type corresponds
    to a Case Number, determined by the Protocol each class of
    GeneralModule belongs to.
    """

    def FillShared(self, model: Interface_InterfaceModel | None, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: Interface_EntityIterator) -> None:
        """
        Specific filling of the list of Entities shared by an Entity
        <ent>, according a Case Number <CN> (formerly computed by
        CaseNum), considered in the context of a Model <model>
        Default calls FillSharedCase (i.e., ignores the model)
        Can be redefined to use the model for working
        """

    def FillSharedCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: Interface_EntityIterator) -> None:
        """
        Specific filling of the list of Entities shared by an Entity
        <ent>, according a Case Number <CN> (formerly computed by
        CaseNum). Can use the internal utility method Share, below
        """

    def Share(self, iter: Interface_EntityIterator, shared: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds an Entity to a Shared List (uses GetOneItem on <iter>)"""

    def ListImplied(self, model: Interface_InterfaceModel | None, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: Interface_EntityIterator) -> None:
        """
        List the Implied References of <ent> considered in the context
        of a Model <model> : i.e. the Entities which are Referenced
        while not considered as Shared (not copied if <ent> is,
        references not renewed by CopyCase but by ImpliedCase, only
        if referenced Entities have been Copied too)
        FillShared + ListImplied give the complete list of References
        Default calls ListImpliedCase (i.e. ignores the model)
        Can be redefined to use the model for working
        """

    def ListImpliedCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: Interface_EntityIterator) -> None:
        """
        List the Implied References of <ent> (see above)
        are Referenced while not considered as Shared (not copied if
        <ent> is, references not renewed by CopyCase but by
        ImpliedCase, only if referenced Entities have been Copied too)
        FillSharedCase + ListImpliedCase give the complete list of
        Referenced Entities
        The provided default method does nothing (Implied References
        are specific of a little amount of Entity Classes).
        """

    def CheckCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: Interface_ShareTool) -> Interface_Check:
        """
        Specific Checking of an Entity <ent>
        Can check context queried through a ShareTool, as required
        """

    def CanCopy(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Specific answer to the question "is Copy properly implemented"
        Remark that it should be in phase with the implementation of
        NewVoid+CopyCase/NewCopyCase
        Default returns always False, can be redefined
        """

    def Dispatch(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, TC: Interface_CopyTool) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Dispatches an entity
        Returns True if it works by copy, False if it just duplicates
        the starting Handle

        Dispatching means producing a new entity, image of the
        starting one, in order to be put into a new Model, this Model
        being itself the result of a dispatch from an original Model

        According to the cases, dispatch can either
        * just return <entto> as equating <entfrom>
        -> the new model designates the starting entity : it is
        lighter, but the dispatched entity being shared might not be
        modified for dispatch
        * copy <entfrom> to <entto>
        by calling NewVoid+CopyCase (two steps) or NewCopiedCase (1)
        -> the dispatched entity is a COPY, hence it can be modified

        The provided default just duplicates the handle without
        copying, then returns False. Can be redefined
        """

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Creates a new void entity <entto> according to a Case Number
        This entity remains to be filled, by reading from a file or
        by copying from another entity of same type (see CopyCase)
        """

    def CopyCase(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: Interface_CopyTool) -> None:
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type)
        by using a CopyTool which provides its working Map.
        Use method Transferred from CopyTool to work
        """

    def NewCopiedCase(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, TC: Interface_CopyTool) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Specific operator (create+copy) defaulted to do nothing.
        It can be redefined : When it is not possible to work in two
        steps (NewVoid then CopyCase). This can occur when there is
        no default constructor : hence the result <entto> must be
        created with an effective definition.
        Remark : if NewCopiedCase is defined, CopyCase has nothing to do
        Returns True if it has produced something, false else
        """

    def RenewImpliedCase(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: Interface_CopyTool) -> None:
        """
        Specific Copying of Implied References
        A Default is provided which does nothing (must current case !)
        Already copied references (by CopyFrom) must remain unchanged
        Use method Search from CopyTool to work
        """

    def WhenDeleteCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, dispatched: bool) -> None:
        """
        Prepares an entity to be deleted. What does it mean :
        Basically, any class of entity may define its own destructor
        By default, it does nothing but calling destructors on fields
        With the Memory Manager, it is useless to call destructor,
        it is done automatically when the Handle is nullified(cleared)
        BUT this is ineffective in looping structures (whatever these
        are "Implied" references or not).

        THUS : if no loop may appear in definitions, a class which
        inherits from TShared is correctly managed by automatic way
        BUT if there can be loops (or simply back pointers), they must
        be broken, for instance by clearing fields of one of the nodes
        The default does nothing, to be redefined if a loop can occur
        (Implied generally requires WhenDelete, but other cases can
        occur)

        Warning : <dispatched> tells if the entity to be deleted has been
        produced by Dispatch or not. Hence WhenDelete must be in
        coherence with Dispatch
        Dispatch can either copy or not.
        If it copies the entity, this one should be deleted
        If it doesn't (i.e. duplicates the handle) nothing to do

        If <dispatch> is False, normal deletion is to be performed
        """

    def CategoryNumber(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: Interface_ShareTool) -> int:
        """
        Returns a category number which characterizes an entity
        Category Numbers are managed by the class Category
        <shares> can be used to evaluate this number in the context
        Default returns 0 which means "unspecified\"
        """

    def Name(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: Interface_ShareTool) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Determines if an entity brings a Name (or widerly, if a Name
        can be attached to it, through the ShareTool
        By default, returns a Null Handle (no name can be produced)
        Can be redefined

        Warning : While this string may be edited on the spot, if it is a read
        field, the returned value must be copied before.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_GlobalNodeOfGeneralLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty GlobalNode, with no Next"""

    @overload
    def __init__(self, theOther: Interface_GlobalNodeOfGeneralLib) -> None: ...

    def Add(self, amodule: Interface_GeneralModule | None, aprotocol: Interface_Protocol | None) -> None:
        """
        Adds a Module bound with a Protocol to the list : does
        nothing if already in the list, THAT IS, Same Type (exact
        match) and Same State (that is, IsEqual is not required)
        Once added, stores its attached Protocol in correspondence
        """

    def Module(self) -> Interface_GeneralModule:
        """Returns the Module stored in a given GlobalNode"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the attached Protocol stored in a given GlobalNode"""

    def Next(self) -> Interface_GlobalNodeOfGeneralLib:
        """
        Returns the Next GlobalNode. If none is defined, returned
        value is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_GlobalNodeOfReaderLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty GlobalNode, with no Next"""

    @overload
    def __init__(self, theOther: Interface_GlobalNodeOfReaderLib) -> None: ...

    def Add(self, amodule: Interface_ReaderModule | None, aprotocol: Interface_Protocol | None) -> None:
        """
        Adds a Module bound with a Protocol to the list : does
        nothing if already in the list, THAT IS, Same Type (exact
        match) and Same State (that is, IsEqual is not required)
        Once added, stores its attached Protocol in correspondence
        """

    def Module(self) -> Interface_ReaderModule:
        """Returns the Module stored in a given GlobalNode"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the attached Protocol stored in a given GlobalNode"""

    def Next(self) -> Interface_GlobalNodeOfReaderLib:
        """
        Returns the Next GlobalNode. If none is defined, returned
        value is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_InterfaceModel(nanoocp.Standard.Standard_Transient):
    """
    Defines an (Indexed) Set of data corresponding to a complete
    Transfer by a File Interface, i.e. File Header and Transient
    Entities (Objects) contained in a File. Contained Entities are
    identified in the Model by unique and consecutive Numbers.

    In addition, a Model can attach to each entity, a specific
    Label according to the norm (e.g. Name for VDA, #ident for
    Step ...), intended to be output on a string or a stream
    (remark : labels are not obliged to be unique)

    InterfaceModel itself is not Transient, it is intended to
    work on a set of Transient Data. The services offered are
    basic Listing and Identification operations on Transient
    Entities, storage of Error Reports, Copying.

    Moreovere, it is possible to define and use templates. These
    are empty Models, from which copies can be obtained in order
    to be filled with effective data. This allows to record
    standard definitions for headers, avoiding to recreate them
    for each sendings, and assuring customisation of produced
    files for a given site.
    A template is attached to a name. It is possible to define a
    template from another one (get it, edit it then record it
    under another name).

    See also Graph, ShareTool, CheckTool for more
    """

    def Destroy(self) -> None:
        """Clears the list of entities (service WhenDelete)"""

    def SetProtocol(self, proto: Interface_Protocol | None) -> None:
        """
        Sets a Protocol for this Model
        It is also set by a call to AddWithRefs with Protocol
        It is used for : DumpHeader (as required), ClearEntities ...
        """

    def Protocol(self) -> Interface_Protocol:
        """
        Returns the Protocol which has been set by SetProtocol, or
        AddWithRefs with Protocol
        """

    def SetGTool(self, gtool: Interface_GTool | None) -> None:
        """Sets a GTool for this model, which already defines a Protocol"""

    def GTool(self) -> Interface_GTool:
        """Returns the GTool, set by SetProtocol or by SetGTool"""

    def DispatchStatus(self) -> bool:
        """
        Returns the Dispatch Status, either for get or set
        A Model which is produced from Dispatch may share entities
        with the original (according to the Protocol), hence these
        non-copied entities should not be deleted
        """

    def SetDispatchStatus(self, theValue: bool) -> None:
        """
        Python addition: sets the value DispatchStatus() returns by reference in C++.
        """

    def Clear(self) -> None:
        """
        Erases contained data; used when a Model is copied to others :
        the new copied ones begin from clear
        Clear calls specific method ClearHeader (see below)
        """

    def ClearEntities(self) -> None:
        """
        Clears the entities; uses the general service WhenDelete, in
        addition to the standard Memory Manager; can be redefined
        """

    def ClearLabels(self) -> None:
        """
        Erases information about labels, if any : specific to each
        norm
        """

    def ClearHeader(self) -> None:
        """Clears Model's header : specific to each norm"""

    def NbEntities(self) -> int:
        """Returns count of contained Entities"""

    def Contains(self, anentity: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if a Model contains an Entity (for a ReportEntity,
        looks for the ReportEntity itself AND its Concerned Entity)
        """

    def Number(self, anentity: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the Number of an Entity in the Model if it contains it.
        Else returns 0. For a ReportEntity, looks at Concerned Entity.
        Returns the Directory entry Number of an Entity in
        the Model if it contains it. Else returns 0.
        For a ReportEntity, looks at Concerned Entity.
        """

    def Value(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an Entity identified by its number in the Model
        Each sub-class of InterfaceModel can define its own method
        Entity to return its specific class of Entity (e.g. for VDA,
        VDAModel returns a VDAEntity), working by calling Value
        Remark : For a Reported Entity, (Erroneous, Corrected, Unknown), this
        method returns this Reported Entity.
        See ReportEntity for other questions.
        """

    def NbTypes(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the count of DISTINCT types under which an entity may
        be processed. Defined by the Protocol, which gives default as
        1 (dynamic Type).
        """

    def Type(self, ent: nanoocp.Standard.Standard_Transient | None, num: int = 1) -> nanoocp.Standard.Standard_Type:
        """
        Returns a type, given its rank : defined by the Protocol
        (by default, the first one)
        """

    def TypeName(self, ent: nanoocp.Standard.Standard_Transient | None, complete: bool = True) -> str:
        """
        Returns the type name of an entity, from the list of types
        (one or more ...)
        <complete> True (D) gives the complete type, else packages are
        removed
        WARNING : buffered, to be immediately copied or printed
        """

    @staticmethod
    def ClassName(typnam: str) -> str:
        """
        From a CDL Type Name, returns the Class part (package dropped)
        WARNING : buffered, to be immediately copied or printed
        """

    def EntityState(self, num: int) -> Interface_DataState:
        """Returns the State of an entity, given its number"""

    def IsReportEntity(self, num: int, semantic: bool = False) -> bool:
        """
        Returns True if <num> identifies a ReportEntity in the Model
        Hence, ReportEntity can be called.

        By default, queries main report, if <semantic> is True, it
        queries report for semantic check

        Remember that a Report Entity can be defined for an Unknown
        Entity, or a Corrected or Erroneous (at read time) Entity.
        The ReportEntity is defined before call to method AddEntity.
        """

    def ReportEntity(self, num: int, semantic: bool = False) -> Interface_ReportEntity:
        """
        Returns a ReportEntity identified by its number in the Model,
        or a Null Handle If <num> does not identify a ReportEntity.

        By default, queries main report, if <semantic> is True, it
        queries report for semantic check
        """

    def IsErrorEntity(self, num: int) -> bool:
        """
        Returns True if <num> identifies an Error Entity : in this
        case, a ReportEntity brings Fail Messages and possibly an
        "undefined" Content, see IsRedefinedEntity
        """

    def IsRedefinedContent(self, num: int) -> bool:
        """
        Returns True if <num> identifies an Entity which content is
        redefined through a ReportEntity (i.e. with literal data only)
        This happens when an entity is syntactically erroneous in the
        way that its basic content remains empty.
        For more details (such as content itself), see ReportEntity
        """

    def ClearReportEntity(self, num: int) -> bool:
        """
        Removes the ReportEntity attached to Entity <num>. Returns
        True if done, False if no ReportEntity was attached to <num>.
        Warning : the caller must assume that this clearing is meaningful
        """

    def SetReportEntity(self, num: int, rep: Interface_ReportEntity | None) -> bool:
        """
        Sets or Replaces a ReportEntity for the Entity <num>. Returns
        True if Report is replaced, False if it has been replaced
        Warning : the caller must assume that this setting is meaningful
        """

    def AddReportEntity(self, rep: Interface_ReportEntity | None, semantic: bool = False) -> bool:
        """
        Adds a ReportEntity as such. Returns False if the concerned
        entity is not recorded in the Model
        Else, adds it into, either the main report list or the
        list for semantic checks, then returns True
        """

    def IsUnknownEntity(self, num: int) -> bool:
        """
        Returns True if <num> identifies an Unknown Entity : in this
        case, a ReportEntity with no Check Messages designates it.
        """

    def FillSemanticChecks(self, checks: Interface_CheckIterator, clear: bool = True) -> None:
        """
        Fills the list of semantic checks.
        This list is computed (by CheckTool). Hence, it can be stored
        in the model for later queries
        <clear> True (D) : new list replaces
        <clear> False    : new list is cumulated
        """

    def HasSemanticChecks(self) -> bool:
        """Returns True if semantic checks have been filled"""

    def Check(self, num: int, syntactic: bool) -> Interface_Check:
        """
        Returns the check attached to an entity, designated by its
        Number. 0 for global check
        <semantic> True  : recorded semantic check
        <semantic> False : recorded syntactic check (see ReportEntity)
        If no check is recorded for <num>, returns an empty Check
        """

    def Reservate(self, nbent: int) -> None:
        """
        Does a reservation for the List of Entities (for optimized
        storage management). If it is not called, storage management
        can be less efficient. <nbent> is the expected count of
        Entities to store
        """

    def AddEntity(self, anentity: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Internal method for adding an Entity. Used by file reading
        (defined by each Interface) and Transfer tools. It adds the
        entity required to be added, not its refs : see AddWithRefs.
        If <anentity> is a ReportEntity, it is added to the list of
        Reports, its Concerned Entity (Erroneous or Corrected, else
        Unknown) is added to the list of Entities.
        That is, the ReportEntity must be created before Adding
        """

    @overload
    def AddWithRefs(self, anent: nanoocp.Standard.Standard_Transient | None, proto: Interface_Protocol | None, level: int = 0, listall: bool = False) -> None:
        """
        Adds to the Model, an Entity with all its References, as they
        are defined by General Services FillShared and ListImplied.
        Process is recursive (any sub-levels) if <level> = 0 (Default)
        Else, adds sub-entities until the required sub-level.
        Especially, if <level> = 1, adds immediate subs and that's all

        If <listall> is False (Default), an entity (<anentity> itself
        or one of its subs at any level) which is already recorded in
        the Model is not analysed, only the newly added ones are.
        If <listall> is True, all items are analysed (this allows to
        ensure the consistency of an adding made by steps)
        """

    @overload
    def AddWithRefs(self, anent: nanoocp.Standard.Standard_Transient | None, level: int = 0, listall: bool = False) -> None:
        """Same as above, but works with the Protocol of the Model"""

    @overload
    def AddWithRefs(self, anent: nanoocp.Standard.Standard_Transient | None, lib: Interface_GeneralLib, level: int = 0, listall: bool = False) -> None:
        """Same as above, but works with an already created GeneralLib"""

    def ReplaceEntity(self, nument: int, anent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Replace Entity with Number=nument on other entity - "anent\""""

    def ReverseOrders(self, after: int = 0) -> None:
        """
        Reverses the Numbers of the Entities, between <after> and the
        total count of Entities. Thus, the entities :
        1,2 ... after, after+1 ... nb-1, nb  become numbered as :
        1,2 ... after, nb, nb-1 ... after+1
        By default (after = 0) the whole list of Entities is reversed
        """

    def ChangeOrder(self, oldnum: int, newnum: int, count: int = 1) -> None:
        """
        Changes the Numbers of some Entities : <oldnum> is moved to
        <newnum>, same for <count> entities. Thus :
        1,2 ... newnum-1 newnum ... oldnum .. oldnum+count oldnum+count+1 .. gives
        1,2 ... newnum-1 oldnum .. oldnum+count newnum ... oldnum+count+1
        (can be seen as a circular permutation)
        """

    def GetFromTransfer(self, aniter: Interface_EntityIterator) -> None:
        """
        Gets contents from an EntityIterator, prepared by a
        Transfer tool (e.g TransferCopy). Starts from clear
        """

    def GetFromAnother(self, other: Interface_InterfaceModel | None) -> None:
        """
        Gets header (data specific of a defined Interface) from
        another InterfaceModel; called from TransferCopy
        """

    def NewEmptyModel(self) -> Interface_InterfaceModel:
        """
        Returns a New Empty Model, same type as <me> (whatever its
        Type); called to Copy parts a Model into other ones, then
        followed by a call to GetFromAnother (Header) then filling
        with specified Entities, themselves copied
        """

    def SetCategoryNumber(self, num: int, val: int) -> bool:
        """
        Records a category number for an entity number
        Returns True when done, False if <num> is out of range
        """

    def CategoryNumber(self, num: int) -> int:
        """
        Returns the recorded category number for a given entity number
        0 if none was defined for this entity
        """

    def FillIterator(self, iter: Interface_EntityIterator) -> None:
        """Allows an EntityIterator to get a list of Entities"""

    def Entities(self) -> Interface_EntityIterator:
        """
        Returns the list of all Entities, as an Iterator on Entities
        (the Entities themselves, not the Reports)
        """

    def Reports(self, semantic: bool = False) -> Interface_EntityIterator:
        """
        Returns the list of all ReportEntities, i.e. data about
        Entities read with Error or Warning information
        (each item has to be casted to Report Entity then it can be
        queried for Concerned Entity, Content, Check ...)
        By default, returns the main reports, is <semantic> is True it
        returns the list for semantic checks
        """

    def Redefineds(self) -> Interface_EntityIterator:
        """
        Returns the list of ReportEntities which redefine data
        (generally, if concerned entity is "Error", a literal content
        is added to it : this is a "redefined entity\"
        """

    def GlobalCheck(self, syntactic: bool = True) -> Interface_Check:
        """
        Returns the GlobalCheck, which memorizes messages global to
        the file (not specific to an Entity), especially Header
        """

    def SetGlobalCheck(self, ach: Interface_Check | None) -> None:
        """
        Allows to modify GlobalCheck, after getting then completing it
        Remark : it is SYNTACTIC check. Semantics, see FillChecks
        """

    def VerifyCheck(self) -> Interface_Check:
        """
        Minimum Semantic Global Check on data in model (header)
        Can only check basic Data. See also GlobalCheck from Protocol
        for a check which takes the Graph into account
        Default does nothing, can be redefined
        """

    def DumpHeader(self, level: int = 0) -> str:
        """
        Dumps Header in a short, easy to read, form, onto a Stream
        <level> allows to print more or less parts of the header,
        if necessary. 0 for basic print
        """

    def Print(self, ent: nanoocp.Standard.Standard_Transient | None, mode: int = 0) -> str:
        """
        Prints identification of a given entity in <me>, in order to
        be printed in a list or phrase
        <mode> < 0 : prints only its number
        <mode> = 1 : just calls PrintLabel
        <mode> = 0 (D) : prints its number plus '/' plus PrintLabel
        If <ent> == <me>, simply prints "Global"
        If <ent> is unknown, prints "??/its type\"
        """

    def PrintLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints label specific to each norm, for a given entity.
        Must only print label itself, in order to be included in a
        phrase. Can call the result of StringLabel, but not obliged.
        """

    def PrintToLog(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints label specific to each norm in log format, for
        a given entity.
        By default, just calls PrintLabel, can be redefined
        """

    def StringLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a string with the label attached to a given entity.
        Warning : While this string may be edited on the spot, if it is a read
        field, the returned value must be copied before.
        """

    def NextNumberForLabel(self, label: str, lastnum: int = 0, exact: bool = True) -> int:
        """
        Searches a label which matches with one entity.
        Begins from <lastnum>+1 (default:1) and scans the entities
        until <NbEntities>. For the first which matches <label>,
        this method returns its Number. Returns 0 if nothing found
        Can be called recursively (labels are not specified as unique)
        <exact> : if True (default), exact match is required
        else, checks the END of entity label

        This method is virtual, hence it can be redefined for a more
        efficient search (if exact is true).
        """

    @staticmethod
    def HasTemplate(name: str) -> bool:
        """Returns true if a template is attached to a given name"""

    @staticmethod
    def Template(name: str) -> Interface_InterfaceModel:
        """Returns the template model attached to a name, or a Null Handle"""

    @staticmethod
    def SetTemplate(name: str, model: Interface_InterfaceModel | None) -> bool:
        """
        Records a new template model with a name. If the name was
        already recorded, the corresponding template is replaced by
        the new one. Then, WARNING : test HasTemplate to avoid
        surprises
        """

    @staticmethod
    def ListTemplates() -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns the complete list of names attached to template models"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_Graph:
    """
    Gives basic data structure for operating and storing
    graph results (usage is normally internal)
    Entities are Mapped according their Number in the Model

    Each Entity from the Model can be known as "Present" or
    not; if it is, it is Mapped with a Status : an Integer
    which can be used according to needs of each algorithm
    In addition, the Graph brings a BitMap which can be used
    by any caller

    Also, it is bound with two lists : a list of Shared
    Entities (in fact, their Numbers in the Model) which is
    filled by a ShareTool, and a list of Sharing Entities,
    computed by deduction from the Shared Lists

    Moreover, it is possible to redefine the list of Entities
    Shared by an Entity (instead of standard answer by general
    service Shareds) : this new list can be empty; it can
    be changed or reset (i.e. to come back to standard answer)
    """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, theModeStats: bool = True) -> None:
        """Same a above but works with the Protocol recorded in the Model"""

    @overload
    def __init__(self, agraph: Interface_Graph, copied: bool = False) -> None:
        """
        Creates a Graph from another one, getting all its data
        Remark that status are copied from <agraph>, but the other
        lists (sharing/shared) are copied only if <copied> = True
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, lib: Interface_GeneralLib, theModeStats: bool = True) -> None:
        """
        Creates an empty graph, ready to receive Entities from amodel
        Note that this way of Creation allows <me> to verify that
        Entities to work with are contained in <amodel>
        Basic Shared and Sharing lists are obtained from a General
        Services Library, given directly as an argument
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, protocol: Interface_Protocol | None, theModeStats: bool = True) -> None: ...

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, gtool: Interface_GTool | None, theModeStats: bool = True) -> None:
        """Same as above, but the Library is defined through a Protocol"""

    def Reset(self) -> None:
        """
        Erases data, making graph ready to rebegin from void
        (also resets Shared lists redefinitions)
        """

    def ResetStatus(self) -> None:
        """
        Erases Status (Values and Flags of Presence), making graph
        ready to rebegin from void. Does not concerns Shared lists
        """

    def Size(self) -> int:
        """Returns size (max nb of entities, i.e. Model's nb of entities)"""

    def NbStatuses(self) -> int:
        """Returns size of array of statuses"""

    def EntityNumber(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the Number of the entity in the Map, computed at
        creation time (Entities loaded from the Model)
        Returns 0 if <ent> not contained by Model used to create <me>
        (that is, <ent> is unknown from <me>)
        """

    @overload
    def IsPresent(self, num: int) -> bool:
        """
        Returns True if an Entity is noted as present in the graph
        (See methods Get... which determine this status)
        Returns False if <num> is out of range too
        """

    @overload
    def IsPresent(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Same as above but directly on an Entity <ent> : if it is not
        contained in the Model, returns False. Else calls
        IsPresent(num) with <num> given by EntityNumber
        """

    def Entity(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns mapped Entity given its no (if it is present)"""

    def Status(self, num: int) -> int:
        """Returns Status associated to a numero (only to read it)"""

    def SetStatus(self, num: int, stat: int) -> None:
        """Modifies Status associated to a numero"""

    def RemoveItem(self, num: int) -> None:
        """Clears Entity and sets Status to 0, for a numero"""

    def ChangeStatus(self, oldstat: int, newstat: int) -> None:
        """Changes all status which value is oldstat to new value newstat"""

    def RemoveStatus(self, stat: int) -> None:
        """Removes all items of which status has a given value stat"""

    def BitMap(self) -> Interface_BitMap:
        """Returns the Bit Map in order to read or edit flag values"""

    def CBitMap(self) -> Interface_BitMap:
        """Returns the Bit Map in order to edit it (add new flags)"""

    def Model(self) -> Interface_InterfaceModel:
        """Returns the Model with which this Graph was created"""

    def GetFromModel(self) -> None:
        """Loads Graph with all Entities contained in the Model"""

    @overload
    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None, shared: bool, newstat: int = 0) -> None:
        """
        Gets an Entity, plus its shared ones (at every level) if
        "shared" is True. New items are set to status "newstat"
        Items already present in graph remain unchanged
        Of course, redefinitions of Shared lists are taken into
        account if there are some
        """

    @overload
    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None, shared: bool, newstat: int, overlapstat: int, cumul: bool) -> None:
        """
        Gets an Entity, plus its shared ones (at every level) if
        "shared" is True. New items are set to status "newstat".
        Items already present in graph are processed as follows :
        - if they already have status "newstat", they remain unchanged
        - if they have another status, this one is modified :
        if cumul is True,  to former status + overlapstat (cumul)
        if cumul is False, to overlapstat (enforce)
        """

    @overload
    def GetFromIter(self, iter: Interface_EntityIterator, newstat: int) -> None:
        """
        Gets Entities given by an EntityIterator. Entities which were
        not yet present in the graph are mapped with status "newstat"
        Entities already present remain unchanged
        """

    @overload
    def GetFromIter(self, iter: Interface_EntityIterator, newstat: int, overlapstat: int, cumul: bool) -> None:
        """
        Gets Entities given by an EntityIterator and distinguishes
        those already present in the Graph :
        - new entities added to the Graph with status "newstst"
        - entities already present with status = "newstat" remain
        unchanged
        - entities already present with status different form
        "newstat" have their status modified :
        if cumul is True,  to former status + overlapstat (cumul)
        if cumul is False, to overlapstat (enforce)
        (Note : works as GetEntity, shared = False, for each entity)
        """

    @overload
    def GetFromGraph(self, agraph: Interface_Graph) -> None:
        """Gets all present items from another graph"""

    @overload
    def GetFromGraph(self, agraph: Interface_Graph, stat: int) -> None:
        """Gets items from another graph which have a specific Status"""

    def HasShareErrors(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if <ent> or the list of entities shared by <ent>
        (not redefined) contains items unknown from this Graph
        Remark : apart from the status HasShareError, these items
        are ignored
        """

    def GetShareds(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """Returns the sequence of Entities Shared by an Entity"""

    def Shareds(self, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_EntityIterator:
        """
        Returns the list of Entities Shared by an Entity, as recorded
        by the Graph. That is, by default Basic Shared List, else it
        can be redefined by methods SetShare, SetNoShare ... see below
        """

    def Sharings(self, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_EntityIterator:
        """
        Returns the list of Entities which Share an Entity, computed
        from the Basic or Redefined Shared Lists
        """

    def GetSharings(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """Returns the sequence of Entities Sharings by an Entity"""

    def TypedSharings(self, ent: nanoocp.Standard.Standard_Transient | None, type: nanoocp.Standard.Standard_Type | None) -> Interface_EntityIterator:
        """
        Returns the list of sharings entities, AT ANY LEVEL, which are
        kind of a given type. A sharing entity kind of this type
        ends the exploration of its branch
        """

    def RootEntities(self) -> Interface_EntityIterator:
        """
        Returns the Entities which are not Shared (their Sharing List
        is empty) in the Model
        """

    def Name(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Determines the name attached to an entity, by using the
        general service Name in GeneralModule
        Returns a null handle if no name could be computed or if
        the entity is not in the model
        """

    def SharingTable(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_List[int]]:
        """
        Returns the Table of Sharing lists. Used to Create
        another Graph from <me>
        """

    def ModeStat(self) -> bool:
        """Returns mode responsible for computation of statuses;"""

class Interface_GraphContent(Interface_EntityIterator):
    """
    Defines general form for classes of graph algorithms on
    Interfaces, this form is that of EntityIterator
    Each sub-class fills it according to its own algorithm
    This also allows to combine any graph result to others,
    all being given under one unique form
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty GraphContent, ready to be filled"""

    @overload
    def __init__(self, agraph: Interface_Graph) -> None:
        """Creates with all entities designated by a Graph"""

    @overload
    def __init__(self, agraph: Interface_Graph, stat: int) -> None:
        """Creates with entities having specific Status value in a Graph"""

    @overload
    def __init__(self, agraph: Interface_Graph, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Creates an Iterator with Shared entities of an entity
        (equivalente to EntityIterator but with a Graph)
        """

    @overload
    def __init__(self, theOther: Interface_GraphContent) -> None: ...

    @overload
    def GetFromGraph(self, agraph: Interface_Graph) -> None:
        """
        Gets all Entities designated by a Graph (once created), adds
        them to those already recorded
        """

    @overload
    def GetFromGraph(self, agraph: Interface_Graph, stat: int) -> None:
        """
        Gets entities from a graph which have a specific Status value
        (one created), adds them to those already recorded
        """

    def Result(self) -> Interface_EntityIterator:
        """
        Returns Result under the exact form of an EntityIterator :
        Can be used when EntityIterator itself is required (as a
        returned value for instance), without way for a sub-class
        """

    def Begin(self) -> None:
        """
        Does the Evaluation before starting the iteration itself
        (in out)
        """

    def Evaluate(self) -> None:
        """
        Evaluates list of Entities to be iterated. Called by Start
        Default is set to doing nothing : intended to be redefined
        by each sub-class
        """

class Interface_HGraph(nanoocp.Standard.Standard_Transient):
    """
    This class allows to store a redefinable Graph, via a Handle
    (useful for an Object which can work on several successive
    Models, with the same general conditions)
    """

    @overload
    def __init__(self, agraph: Interface_Graph) -> None:
        """
        Creates an HGraph directly from a Graph.
        Remark that the starting Graph is duplicated
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, theModeStats: bool = True) -> None:
        """Same a above, but works with the GTool in the model"""

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, lib: Interface_GeneralLib, theModeStats: bool = True) -> None:
        """Creates an HGraph with a Graph created from <amodel> and <lib>"""

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, protocol: Interface_Protocol | None, theModeStats: bool = True) -> None: ...

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, gtool: Interface_GTool | None, theModeStats: bool = True) -> None:
        """
        Creates an HGraph with a graph itself created from <amodel>
        and <protocol>
        """

    @overload
    def __init__(self, theOther: Interface_HGraph) -> None: ...

    def Graph(self) -> Interface_Graph:
        """
        Returns the Graph contained in <me>, for Read Only Operations
        Remark that it is returns as "const &"
        Getting it in a new variable instead of a reference would be
        a pity, because all the graph's content would be duplicated
        """

    def CGraph(self) -> Interface_Graph:
        """
        Same as above, but for Read-Write Operations
        Then, The Graph will be modified in the HGraph itself
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_InterfaceMismatch(Interface_InterfaceError):
    pass

class Interface_IntList:
    """
    This class detains the data which describe a Graph. A Graph
    has two lists, one for shared refs, one for sharing refs
    (the reverses). Each list comprises, for each Entity of the
    Model of the Graph, a list of Entities (shared or sharing).
    In fact, entities are identified by their numbers in the Model
    or Graph : this gives better performances.

    A simple way to implement this is to instantiate a HArray1
    with a HSequenceOfInteger : each Entity Number designates a
    value, which is a Sequence (if it is null, it is considered as
    empty : this is a little optimisation).

    This class gives a more efficient way to implement this.
    It has two lists (two arrays of integers), one to describe
    list (empty, one value given immediately, or negated index in
    the second list), one to store refs (pointed from the first
    list). This is much more efficient than a list of sequences,
    in terms of speed (especially for read) and of memory

    An IntList can also be set to access data for a given entity
    number, it then acts as a single sequence

    Remark that if an IntList is created from another one, it can
    be read, but if it is created without copying, it may not be
    edited
    """

    @overload
    def __init__(self) -> None:
        """Creates empty IntList."""

    @overload
    def __init__(self, nbe: int) -> None:
        """Creates an IntList for <nbe> entities"""

    @overload
    def __init__(self, other: Interface_IntList, copied: bool) -> None:
        """
        Creates an IntList from another one.
        if <copied> is True, copies data
        else, data are not copied, only the header object is
        """

    @overload
    def __init__(self, theOther: Interface_IntList) -> None: ...

    def Initialize(self, nbe: int) -> None:
        """Initialize IntList by number of entities."""

    def NbReferences(self) -> int:
        """
        Returns count of stored references.
        @return number of references
        """

    def Entities(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Returns entity headers used to describe the lists.
        @return handle to the array of entity headers
        """

    def References(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Returns the packed references storage.
        @return handle to the array of packed references
        """

    def Internals(self) -> tuple[int, nanoocp.NCollection.NCollection_HArray1[int], nanoocp.NCollection.NCollection_HArray1[int]]:
        """
        Deprecated in OCCT: Use NbReferences(), Entities(), and References() instead

        Returns internal values, used for copying
        @deprecated Use NbReferences(), Entities(), and References() instead.
        """

    def NbEntities(self) -> int:
        """Returns count of entities to be acknowledged"""

    def SetNbEntities(self, nbe: int) -> None:
        """Changes the count of entities (ignored if decreased)"""

    def SetNumber(self, number: int) -> None:
        """Sets an entity number as current (for read and fill)"""

    def Number(self) -> int:
        """Returns the current entity number"""

    def List(self, number: int, copied: bool = False) -> Interface_IntList:
        """
        Returns an IntList, identical to <me> but set to a specified
        entity Number
        By default, not copied (in order to be read)
        Specified <copied> to produce another list and edit it
        """

    def SetRedefined(self, mode: bool) -> None:
        """
        Sets current entity list to be redefined or not
        This is used in a Graph for redefinition list : it can be
        disable (no redefinition, i.e. list is cleared), or enabled
        (starts as empty). The original list has not to be "redefined\"
        """

    def Reservate(self, count: int) -> None:
        """
        Makes a reservation for <count> references to be later
        attached to the current entity. If required, it increases
        the size of array used to store refs. Remark that if count is
        less than two, it does nothing (because immediate storing)
        """

    def Add(self, ref: int) -> None:
        """
        Adds a reference (as an integer value, an entity number) to
        the current entity number. Zero is ignored
        """

    def Length(self) -> int:
        """Returns the count of refs attached to current entity number"""

    def IsRedefined(self, num: int = 0) -> bool:
        """
        Returns True if the list for a number
        (default is taken as current) is "redefined" (useful for empty list)
        """

    def Value(self, num: int) -> int:
        """
        Returns a reference number in the list for current number,
        according to its rank
        """

    def Remove(self, num: int) -> bool:
        """
        Removes an item in the list for current number, given its rank
        Returns True if done, False else
        """

    def Clear(self) -> None:
        """Clears all data, hence each entity number has an empty list"""

    def AdjustSize(self, margin: int = 0) -> None:
        """
        Resizes lists to exact sizes. For list of refs, a positive
        margin can be added.
        """

class Interface_IntVal(nanoocp.Standard.Standard_Transient):
    """An Integer through a Handle (i.e. managed as TShared)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Interface_IntVal) -> None: ...

    def Value(self) -> int: ...

    def CValue(self) -> int: ...

    def SetCValue(self, theValue: int) -> None:
        """Python addition: sets the value CValue() returns by reference in C++."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_LineBuffer:
    """
    Simple Management of a Line Buffer, to be used by Interface
    File Writers.
    While a String is suitable to do that, this class ensures an
    optimised Memory Management, because this is a hard point of
    File Writing.
    """

    @overload
    def __init__(self, size: int = 10) -> None:
        """
        Creates a LineBuffer with an absolute maximum size
        (Default value is only to satisfy compiler requirement)
        """

    @overload
    def __init__(self, theOther: Interface_LineBuffer) -> None: ...

    def SetMax(self, max: int) -> None:
        """
        Changes Maximum allowed size of Buffer.
        If <max> is Zero, Maximum size is set to the initial size.
        """

    def SetInitial(self, initial: int) -> None:
        """
        Sets an Initial reservation for Blank characters
        (this reservation is counted in the size of the current Line)
        """

    def SetKeep(self) -> None:
        """
        Sets a Keep Status at current Length. It means that at next
        Move, the new line will begin by characters between Keep + 1
        and current Length
        """

    def CanGet(self, more: int) -> bool:
        """
        Returns True if there is room enough to add <more> characters
        Else, it is required to Dump the Buffer before refilling it
        <more> is recorded to manage SetKeep status
        """

    def Content(self) -> str:
        """Returns the Content of the LineBuffer"""

    def Length(self) -> int:
        """Returns the Length of the LineBuffer"""

    def Clear(self) -> None:
        """Clears completely the LineBuffer"""

    def FreezeInitial(self) -> None:
        """
        Inhibits effect of SetInitial until the next Move (i.e. Keep)
        Then Prepare will not insert initial blanks, but further ones
        will. This allows to cancel initial blanks on an internal Split
        A call to SetInitial has no effect on this until Move
        """

    @overload
    def Move(self, str: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Fills a AsciiString <str> with the Content of the Line Buffer,
        then Clears the LineBuffer
        """

    @overload
    def Move(self, str: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Same as above, but <str> is known through a Handle"""

    def Moved(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Same as above, but generates the HAsciiString"""

    @overload
    def Add(self, text: str) -> None:
        """
        Adds a text as a CString. Its Length is evaluated from the
        text (by C function strlen)
        """

    @overload
    def Add(self, text: str, lntext: int) -> None:
        """Adds a text as a CString. Its length is given as <lntext>"""

    @overload
    def Add(self, text: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Adds a text as a AsciiString from TCollection"""

    @overload
    def Add(self, text: str) -> None:
        """Adds a text made of only ONE Character"""

class Interface_MSG:
    """
    This class gives a set of functions to manage and use a list
    of translated messages (messagery)

    Keys are strings, their corresponding (i.e. translated) items
    are strings, managed by a dictionary (a global one).

    If the dictionary is not set, or if a key is not recorded,
    the key is returned as item, and it is possible to :
    - trace or not this fail, record or not it for further trace

    It is also possible to suspend the translation (keys are then
    always returned as items)

    This class also provides a file format for loading :
    It is made of couples of lines, the first one begins by '@'
    the following is the key, the second one is the message
    Lines which are empty or which begin by '@@' are skipped
    """

    @overload
    def __init__(self, key: str) -> None:
        """
        A MSG is created to write a "functional code" in conjunction
        with operator () attached to Value
        Then, to have a translated message, write in C++ :

        Interface_MSG("...mykey...") which returns a CString
        See also some help which follow
        """

    @overload
    def __init__(self, key: str, i1: int) -> None:
        """
        Translates a message which contains one integer variable
        It is just a help which avoid the following :
        char mess[100]; Sprintf(mess,Interface_MSG("code"),ival);
        then AddFail(mess);
        replaced by AddFail (Interface_MSG("code",ival));

        The basic message is intended to be in C-Sprintf format,
        with one %d form in it
        """

    @overload
    def __init__(self, key: str, r1: float, intervals: int = -1) -> None:
        """
        Translates a message which contains one real variable
        <intervals> if set, commands the variable to be rounded to an
        interval (see below, method Intervals)
        As for one integer, it is just a writing help

        The basic message is intended to be in C-Sprintf format
        with one %f form (or equivalent : %e etc) in it
        """

    @overload
    def __init__(self, key: str, str: str) -> None:
        """
        Translates a message which contains one string variable
        As for one integer, it is just a writing help

        The basic message is intended to be in C-Sprintf format
        with one %s form in it
        """

    @overload
    def __init__(self, key: str, i1: int, i2: int) -> None:
        """
        Translates a message which contains two integer variables
        As for one integer, it is just a writing help

        The basic message is intended to be in C-Sprintf format
        with two %d forms in it
        """

    @overload
    def __init__(self, key: str, ival: int, str: str) -> None:
        """
        Translates a message which contains one integer and one
        string variables
        As for one integer, it is just a writing help
        Used for instance to say "Param n0.<ival> i.e. <str> is not.."

        The basic message is intended to be in C-Sprintf format
        with one %d then one %s forms in it
        """

    @overload
    def __init__(self, theOther: Interface_MSG) -> None: ...

    def Destroy(self) -> None:
        """Optimised destructor (applies for additional forms of Create)"""

    def Value(self) -> str:
        """
        Returns the translated message, in a functional form with
        operator ()
        was C++ : return const
        """

    @overload
    @staticmethod
    def Read(S: TextIO) -> int:
        """
        Reads a list of messages from a stream, returns read count
        0 means empty file, -1 means error
        """

    @overload
    @staticmethod
    def Read(file: str) -> int:
        """Reads a list of messages from a file defined by its name"""

    @staticmethod
    def Write(rootkey: str = '') -> tuple[int, str]:
        """
        Writes the list of messages recorded to be translated, to a
        stream. Writes all the list (Default) or only keys which begin
        by <rootkey>. Returns the count of written messages
        """

    @staticmethod
    def IsKey(mess: str) -> bool:
        """
        Returns True if a given message is surely a key
        (according to the form adopted for keys)
        (before activating messages, answer is false)
        """

    @staticmethod
    def Translated(key: str) -> str:
        """
        Returns the item recorded for a key.
        Returns the key itself if :
        - it is not recorded (then, the trace system is activated)
        - MSG has been required to be hung on
        """

    @staticmethod
    def Record(key: str, item: str) -> None:
        """
        Fills the dictionary with a couple (key-item)
        If a key is already recorded, it is possible to :
        - keep the last definition, and activate the trace system
        """

    @staticmethod
    def SetTrace(toprint: bool, torecord: bool) -> None:
        """
        Sets the trace system to work when activated, as follow :
        - if <toprint>  is True, print immediately on standard output
        - if <torecord> is True, record it for further print
        """

    @staticmethod
    def SetMode(running: bool, raising: bool) -> None:
        """
        Sets the main modes for MSG :
        - if <running> is True, translation works normally
        - if <running> is False, translated item equate keys
        - if <raising> is True, errors (from Record or Translate)
        cause MSG to raise an exception
        - if <raising> is False, MSG runs without exception, then
        see also Trace Modes above
        """

    @staticmethod
    def PrintTrace() -> str:
        """
        Prints the recorded errors (without title; can be empty, this
        is the normally expected case)
        """

    @staticmethod
    def Intervalled(val: float, order: int = 3, upper: bool = False) -> float:
        """
        Returns an "intervalled" value from a starting real <val> :
        i.e. a value which is rounded on an interval limit
        Interval limits are defined to be in a coarsely "geometric"
        progression (two successive intervals are inside a limit ratio)

        <order> gives the count of desired intervals in a range <1-10>
        <upper> False, returns the first lower interval (D)
        <upper> True,  returns the first upper interval
        Values of Intervals according <order> :
        0,1 : 1 10 100 ...
        2   : 1 3 10 30 100 ...
        3(D): 1 2 5 10 20 50 100 ...
        4   : 1 2 3 6 10 20 30 60 100 ...
        6   : 1 1.5 2 3 5 7 10 15 20 ...
        10  : 1 1.2 1.5 2 2.5 3 4 5 6 8 10 12 15 20 25 ...
        """

    @staticmethod
    def TDate(text: str, yy: int, mm: int, dd: int, hh: int, mn: int, ss: int, format: str = '') -> None:
        """
        Codes a date as a text, from its numeric value (-> seconds) :
        YYYY-MM-DD:HH-MN-SS fixed format, completed by leading zeros
        Another format can be provided, as follows :
        C:%d ...   C like format, preceded by C:
        S:...      format to call system (not yet implemented)
        """

    @staticmethod
    def NDate(text: str) -> tuple[bool, int, int, int, int, int, int]:
        """
        Decodes a date to numeric integer values
        Returns True if OK, False if text does not fit with required
        format. Incomplete forms are allowed (for instance, for only
        YYYY-MM-DD, hour is zero)
        """

    @staticmethod
    def CDate(text1: str, text2: str) -> int:
        """
        Returns a value about comparison of two dates
        0 : equal. <0 text1 anterior. >0 text1 posterior
        """

    @overload
    @staticmethod
    def Blanks(val: int, max: int) -> str:
        """
        Returns a blank string, of length between 0 and <max>, to fill
        the printing of a numeric value <val>, i.e.
        If val < 10 , max-1 blanks
        If val between 10 and 99, max-2 blanks ... etc...
        """

    @overload
    @staticmethod
    def Blanks(val: str, max: int) -> str:
        """
        Returns a blank string, to complete a given string <val> up to
        <max> characters:
        If strlen(val) is 0, max blanks
        If strlen(val) is 5, max-5 blanks etc...
        """

    @overload
    @staticmethod
    def Blanks(count: int) -> str:
        """Returns a blank string of <count> blanks (mini 0, maxi 76)"""

    @staticmethod
    def Print(val: str, max: int, just: int = -1) -> str:
        """
        Prints a String on an Output Stream, as follows:
        Accompanied with blanks, to give up to <max> chars at all,
        justified accordingly:
        -1 (D) : left 0 : center 1 : right
        Maximum 76 characters
        """

class Interface_NodeOfGeneralLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty Node, with no Next"""

    @overload
    def __init__(self, theOther: Interface_NodeOfGeneralLib) -> None: ...

    def AddNode(self, anode: Interface_GlobalNodeOfGeneralLib | None) -> None:
        """
        Adds a couple (Module,Protocol), that is, stores it into
        itself if not yet done, else creates a Next Node to do it
        """

    def Module(self) -> Interface_GeneralModule:
        """Returns the Module designated by a precise Node"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the Protocol designated by a precise Node"""

    def Next(self) -> Interface_NodeOfGeneralLib:
        """
        Returns the Next Node. If none was defined, returned value
        is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_NodeOfReaderLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty Node, with no Next"""

    @overload
    def __init__(self, theOther: Interface_NodeOfReaderLib) -> None: ...

    def AddNode(self, anode: Interface_GlobalNodeOfReaderLib | None) -> None:
        """
        Adds a couple (Module,Protocol), that is, stores it into
        itself if not yet done, else creates a Next Node to do it
        """

    def Module(self) -> Interface_ReaderModule:
        """Returns the Module designated by a precise Node"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the Protocol designated by a precise Node"""

    def Next(self) -> Interface_NodeOfReaderLib:
        """
        Returns the Next Node. If none was defined, returned value
        is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_ParamList(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, theIncrement: int = 256) -> None:
        """Creates an vector with size of memory block equal to theIncrement"""

    @overload
    def __init__(self, theOther: Interface_ParamList) -> None: ...

    def Length(self) -> int:
        """Returns the number of elements of <me>."""

    def Lower(self) -> int:
        """
        Returns the lower bound.
        Warning
        """

    def Upper(self) -> int:
        """
        Returns the upper bound.
        Warning
        """

    def SetValue(self, Index: int, Value: Interface_FileParameter) -> None:
        """Assigns the value <Value> to the <Index>-th item of this array."""

    def Value(self, Index: int) -> Interface_FileParameter:
        """
        Return the value of the <Index>th element of the
        array.
        """

    def ChangeValue(self, Index: int) -> Interface_FileParameter:
        """
        return the value of the <Index>th element of the
        array.
        """

    def __call__(self, Index: int) -> Interface_FileParameter: ...

    def Clear(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_ParamSet(nanoocp.Standard.Standard_Transient):
    """
    Defines an ordered set of FileParameters, in a way to be
    efficient as in memory requirement or in speed
    """

    @overload
    def __init__(self, nres: int, nst: int = 1) -> None:
        """
        Creates an empty ParamSet, beginning at number "nst" and of
        initial reservation "nres" : the "nres" first parameters
        which follow "ndeb" (included) will be put in an Array
        (a ParamList). The remainders are set in Next(s) ParamSet(s)
        """

    @overload
    def __init__(self, theOther: Interface_ParamSet) -> None: ...

    @overload
    def Append(self, val: str, lnval: int, typ: Interface_ParamType, nument: int) -> int:
        """
        Adds a parameter defined as its Value (CString and length) and
        Type. Optional EntityNumber (for FileReaderData) can be given
        Allows a better memory management than Appending a
        complete FileParameter
        If <lnval> < 0, <val> is assumed to be managed elsewhere : its
        address is stored as such. Else, <val> is copied in a locally
        (quickly) managed Page of Characters
        Returns new count of recorded Parameters
        """

    @overload
    def Append(self, FP: Interface_FileParameter) -> int:
        """
        Adds a parameter at the end of the ParamSet (transparent
        about reservation and "Next")
        Returns new count of recorded Parameters
        """

    def NbParams(self) -> int:
        """Returns the total count of parameters (including nexts)"""

    def Param(self, num: int) -> Interface_FileParameter:
        """Returns a parameter identified by its number"""

    def ChangeParam(self, num: int) -> Interface_FileParameter:
        """Same as above, but in order to be modified on place"""

    def SetParam(self, num: int, FP: Interface_FileParameter) -> None:
        """Changes a parameter identified by its number"""

    def Params(self, num: int, nb: int) -> Interface_ParamList:
        """
        Builds and returns the sub-list corresponding to parameters,
        from "num" included, with count "nb"
        If <num> and <nb> are zero, returns the whole list
        """

    def Destroy(self) -> None:
        """Destructor (waiting for transparent memory management)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_Protocol(nanoocp.Standard.Standard_Transient):
    """
    General description of Interface Protocols. A Protocol defines
    a set of Entity types. This class provides also the notion of
    Active Protocol, as a working context, defined once then
    exploited by various Tools and Libraries.

    It also gives control of type definitions. By default, types
    are provided by CDL, but specific implementations, or topics
    like multi-typing, may involve another way
    """

    @staticmethod
    def Active() -> Interface_Protocol:
        """
        Returns the Active Protocol, if defined (else, returns a
        Null Handle, which means "no defined active protocol")
        """

    @staticmethod
    def SetActive(aprotocol: Interface_Protocol | None) -> None:
        """
        Sets a given Protocol to be the Active one (for the users of
        Active, see just above). Applies to every sub-type of Protocol
        """

    @staticmethod
    def ClearActive() -> None:
        """Erases the Active Protocol (hence it becomes undefined)"""

    def NbResources(self) -> int:
        """Returns count of Protocol used as Resources (level one)"""

    def Resource(self, num: int) -> Interface_Protocol:
        """Returns a Resource, given its rank (between 1 and NbResources)"""

    def CaseNumber(self, obj: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns a unique positive CaseNumber for each Recognized
        Object. By default, recognition is based on Type(1)
        By default, calls the following one which is deferred.
        """

    def IsDynamicType(self, obj: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if type of <obj> is that defined from CDL
        This is the default but it may change according implementation
        """

    def NbTypes(self, obj: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the count of DISTINCT types under which an entity may
        be processed. Each one is candidate to be recognized by
        TypeNumber, <obj> is then processed according it
        By default, returns 1 (the DynamicType)
        """

    def Type(self, obj: nanoocp.Standard.Standard_Transient | None, nt: int = 1) -> nanoocp.Standard.Standard_Type:
        """
        Returns a type under which <obj> can be recognized and
        processed, according its rank in its definition list (see
        NbTypes).
        By default, returns DynamicType
        """

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a unique positive CaseNumber for each Recognized Type,
        Returns Zero for "<type> not recognized\"
        """

    def GlobalCheck(self, G: Interface_Graph) -> tuple[bool, Interface_Check]:
        """
        Evaluates a Global Check for a model (with its Graph)
        Returns True when done, False if data in model do not apply

        Very specific of each norm, i.e. of each protocol : the
        uppest level Protocol assumes it, it can call GlobalCheck of
        its resources only if it is necessary

        Default does nothing, can be redefined
        """

    def NewModel(self) -> Interface_InterfaceModel:
        """Creates an empty Model of the considered Norm"""

    def IsSuitableModel(self, model: Interface_InterfaceModel | None) -> bool:
        """Returns True if <model> is a Model of the considered Norm"""

    def UnknownEntity(self) -> nanoocp.Standard.Standard_Transient:
        """Creates a new Unknown Entity for the considered Norm"""

    def IsUnknownEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e.
        same Type as them created by method UnknownEntity
        (for an Entity out of the Norm, answer can be unpredictable)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_ReaderLib:
    @overload
    def __init__(self) -> None:
        """
        Creates an empty Library : it will later by filled by method
        AddProtocol
        """

    @overload
    def __init__(self, aprotocol: Interface_Protocol | None) -> None:
        """
        Creates a Library which complies with a Protocol, that is :
        Same class (criterium IsInstance)
        This creation gets the Modules from the global set, those
        which are bound to the given Protocol and its Resources
        """

    @overload
    def __init__(self, theOther: Interface_ReaderLib) -> None: ...

    @staticmethod
    def SetGlobal(amodule: Interface_ReaderModule | None, aprotocol: Interface_Protocol | None) -> None:
        """
        Adds a couple (Module-Protocol) into the global definition set
        for this class of Library.
        """

    def AddProtocol(self, aprotocol: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds a couple (Module-Protocol) to the Library, given the
        class of a Protocol. Takes Resources into account.
        (if <aprotocol> is not of type TheProtocol, it is not added)
        """

    def Clear(self) -> None:
        """
        Clears the list of Modules of a library (can be used to
        redefine the order of Modules before action : Clear then
        refill the Library by calls to AddProtocol)
        """

    def SetComplete(self) -> None:
        """
        Sets a library to be defined with the complete Global list
        (all the couples Protocol/Modules recorded in it)
        """

    def Select(self, obj: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, Interface_ReaderModule, int]:
        """
        Selects a Module from the Library, given an Object.
        Returns True if Select has succeeded, False else.
        Also Returns (as arguments) the selected Module and the Case
        Number determined by the associated Protocol.
        If Select has failed, <module> is Null Handle and CN is zero.
        (Select can work on any criterium, such as Object DynamicType)
        """

    def Start(self) -> None:
        """Starts Iteration on the Modules (sets it on the first one)"""

    def More(self) -> bool:
        """Returns True if there are more Modules to iterate on"""

    def Next(self) -> None:
        """
        Iterates by getting the next Module in the list
        If there is none, the exception will be raised by Value
        """

    def Module(self) -> Interface_ReaderModule:
        """Returns the current Module in the Iteration"""

    def Protocol(self) -> Interface_Protocol:
        """Returns the current Protocol in the Iteration"""

class Interface_ReaderModule(nanoocp.Standard.Standard_Transient):
    """
    Defines unitary operations required to read an Entity from a
    File (see FileReaderData, FileReaderTool), under control of
    a FileReaderTool. The initial creation is performed by a
    GeneralModule (set in GeneralLib). Then, which remains is
    Loading data from the FileReaderData to the Entity

    To work, a GeneralModule has formerly recognized the Type read
    from FileReaderData as a positive Case Number, then the
    ReaderModule reads it according to this Case Number
    """

    def CaseNum(self, data: Interface_FileReaderData | None, num: int) -> int:
        """
        Translates the type of record <num> in <data> to a positive
        Case Number. If Recognition fails, must return 0
        """

    def Read(self, casenum: int, data: Interface_FileReaderData | None, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> Interface_Check:
        """
        Performs the effective loading from <data>, record <num>,
        to the Entity <ent> formerly created
        In case of Error or Warning, fills <ach> with messages
        Remark that the Case Number comes from translating a record
        """

    def NewRead(self, casenum: int, data: Interface_FileReaderData | None, num: int) -> tuple[bool, Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        Specific operator (create+read) defaulted to do nothing.
        It can be redefined when it is not possible to work in two
        steps (NewVoid then Read). This occurs when no default
        constructor is defined : hence the result <ent> must be
        created with an effective definition from the reader.
        Remark : if NewRead is defined, Copy has nothing to do.

        Returns True if it has produced something, false else.
        If nothing was produced, <ach> should be filled : it will be
        treated as "Unrecognized case" by reader tool.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_ReportEntity(nanoocp.Standard.Standard_Transient):
    """
    A ReportEntity is produced to acknowledge and memorize the
    binding between a Check and an Entity. The Check can bring
    Fails (+ Warnings if any), or only Warnings. If it is empty,
    the Report Entity is for an Unknown Entity.

    The ReportEntity brings : the Concerned Entity, the
    Check, and if the Entity is empty (Fails due to Read
    Errors, hence the Entity could not be loaded), a Content.
    The Content is itself an Transient Object, but remains in a
    literal form : it is an "Unknown Entity". If the Concerned
    Entity is itself Unknown, Concerned and Content are equal.

    According to the Check, if it brings Fail messages,
    the ReportEntity is an "Error Entity", the Concerned Entity is
    an "Erroneous Entity". Else it is a "Correction Entity", the
    Concerned Entity is a "Corrected Entity". With no Check
    message and if Concerned and Content are equal, it reports
    for an "Unknown Entity".

    Each norm must produce its own type of Unknown Entity, but can
    use the class UndefinedContent to brings parameters : it is
    enough for most of information and avoids to redefine them,
    only the specific part remains to be defined for each norm.
    """

    @overload
    def __init__(self, unknown: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Creates a ReportEntity for an Unknown Entity : Check is empty,
        and Concerned equates Content (i.e. the Unknown Entity)
        """

    @overload
    def __init__(self, acheck: Interface_Check | None, concerned: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Creates a ReportEntity with its features :
        - <acheck> is the Check to be memorised
        - <concerned> is the Entity to which the Check is bound
        Later, a Content can be set : it is required for an Error
        """

    @overload
    def __init__(self, theOther: Interface_ReportEntity) -> None: ...

    def SetContent(self, content: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Sets a Content : it brings non interpreted data which belong
        to the Concerned Entity. It can be empty then loaded later.
        Remark that for an Unknown Entity, Content is set by Create.
        """

    def Check(self) -> Interface_Check:
        """Returns the stored Check"""

    def CCheck(self) -> Interface_Check:
        """Returns the stored Check in order to change it"""

    def Concerned(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the stored Concerned Entity. It equates the Content
        in the case of an Unknown Entity
        """

    def HasContent(self) -> bool:
        """Returns True if a Content is stored (it can equate Concerned)"""

    def HasNewContent(self) -> bool:
        """
        Returns True if a Content is stored AND differs from Concerned
        (i.e. redefines content) : used when Concerned could not be
        loaded
        """

    def Content(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the stored Content, or a Null Handle
        Remark that it must be an "Unknown Entity" suitable for
        the norm of the containing Model
        """

    def IsError(self) -> bool:
        """
        Returns True for an Error Entity, i.e. if the Check
        brings at least one Fail message
        """

    def IsUnknown(self) -> bool:
        """
        Returns True for an Unknown Entity, i,e. if the Check
        is empty and Concerned equates Content
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_ShareFlags:
    """
    This class only says for each Entity of a Model, if it is
    Shared or not by one or more other(s) of this Model
    It uses the General Service "Shared".
    """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None) -> None:
        """Same as above, but works with the GTool of the Model"""

    @overload
    def __init__(self, agraph: Interface_Graph) -> None:
        """
        Creates a ShareFlags by querying information from a Graph
        (remark that Graph also has a method IsShared)
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, lib: Interface_GeneralLib) -> None:
        """
        Creates a ShareFlags from a Model and builds required data
        (flags) by calling the General Service Library given as
        argument <lib>
        """

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, gtool: Interface_GTool | None) -> None:
        """Same as above, but GeneralLib is detained by a GTool"""

    @overload
    def __init__(self, amodel: Interface_InterfaceModel | None, protocol: Interface_Protocol | None) -> None:
        """Same as above, but GeneralLib is defined through a Protocol"""

    @overload
    def __init__(self, theOther: Interface_ShareFlags) -> None: ...

    def Model(self) -> Interface_InterfaceModel:
        """Returns the Model used for the evaluation"""

    def IsShared(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if <ent> is Shared by one or more other
        Entity(ies) of the Model
        """

    def RootEntities(self) -> Interface_EntityIterator:
        """Returns the Entities which are not Shared (see their flags)"""

    def NbRoots(self) -> int:
        """Returns the count of root entities"""

    def Root(self, num: int = 1) -> nanoocp.Standard.Standard_Transient:
        """
        Returns a root entity according its rank in the list of roots
        By default, it returns the first one
        """

class Interface_SignLabel(nanoocp.MoniTool.MoniTool_SignText):
    """Signature to give the Label from the Model"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Interface_SignLabel) -> None: ...

    def Name(self) -> str:
        """Returns "Entity Label\""""

    def Text(self, ent: nanoocp.Standard.Standard_Transient | None, context: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Considers context as an InterfaceModel and returns the Label
        computed by it
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_SignType(nanoocp.MoniTool.MoniTool_SignText):
    """
    Provides the basic service to get a type name, according
    to a norm
    It can be used for other classes (general signatures ...)
    """

    def Text(self, ent: nanoocp.Standard.Standard_Transient | None, context: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns an identification of the Signature (a word), given at
        initialization time
        Specialised to consider context as an InterfaceModel
        """

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient object. It is specific
        of each sub-class of Signature. For a Null Handle, it should
        provide ""
        It can work with the model which contains the entity
        """

    @staticmethod
    def ClassName(typnam: str) -> str:
        """
        From a CDL Type Name, returns the Class part (package dropped)
        WARNING : buffered, to be immediately copied or printed
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_STAT:
    """
    This class manages statistics to be queried asynchronously.
    Way of use :
    An operator describes a STAT form then fills it according to
    its progression. This produces a state of advancement of the
    process. This state can then be queried asynchronously :
    typically it is summarised as a percentage. There are also
    an identification of the current state, and information on
    processed volume.

    A STAT form can be described once for all (as static).
    It describes the stream of the process (see later), in terms
    of phases, cycles, steps, with estimated weights. But it
    brings no current data.

    One STAT at a time is active for filling and querying. It is
    used to control phasing, weighting ... Specific data for
    execution are given when running on active STAT : counts of
    items ... Data for query are then recorded and can be accessed
    at any time, asynchronously.

    A STAT is organised as follows :
    - it can be split into PHASES (by default, there is none, and
    all process takes place in one "default" phase)
    - each phase is identified by a name and is attached a weight
    -> the sum of the weights is used to compute relative weights
    - for each phase, or for the unique default phase if none :
    -- the process works on a list of ITEMS
    -- by default, all the items are processed in once
    -- but this list can be split into CYCLES, each one takes
    a sub-list : the weight of each cycle is related to its
    count of items
    -- a cycle can be split into STEPS, by default there are none
    then one "default step" is considered
    -- each step is attached a weight
    -> the sum of the weights of steps is used to compute relative
    weights of the steps in each cycle
    -> all the cycles of a phase have the same organisation

    Hence, when defining the STAT form, the phases have to be
    described. If no weight is precisely known, give 1. for all...
    No phase description will give only one "default" phase
    For each phase, a typical cycle can be described by its steps.
    Here too, for no weight precisely known, give 1. for all...

    For executing, activate a STAT to begin count. Give counts of
    items and cycles for the first phase (for the unique default
    one if no phasing is described)
    Else, give count of items and cycles for each new phase.
    Class methods allow also to set next cycle (given count of
    items), next step in cycle (if more then one), next item in
    step.
    """

    @overload
    def __init__(self, title: str = '') -> None:
        """
        Creates a STAT form. At start, one default phase is defined,
        with one default step. Then, it suffises to start with a
        count of items (and cycles if several) then record items,
        to have a queryable report.
        """

    @overload
    def __init__(self, other: Interface_STAT) -> None:
        """used when starting"""

    def Internals(self) -> tuple[nanoocp.TCollection.TCollection_HAsciiString, float, nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString], nanoocp.NCollection.NCollection_HSequence[float], nanoocp.NCollection.NCollection_HSequence[int], nanoocp.NCollection.NCollection_HSequence[int], nanoocp.NCollection.NCollection_HSequence[float]]:
        """
        Returns fields in once, without copying them, used for copy
        when starting
        """

    def AddPhase(self, weight: float, name: str = '') -> None:
        """
        Adds a new phase to the description.
        The first one after Create replaces the default unique one
        """

    def AddStep(self, weight: float = 1.0) -> None:
        """
        Adds a new step for the last added phase, the default unique
        one if no AddPhase has already been added
        Warning : AddStep before the first AddPhase are cancelled
        """

    def Step(self, num: int) -> float:
        """
        Returns weight of a Step, related to the cumul given for the
        phase.
        <num> is given by <n0step> + i, i between 1 and <nbsteps>
        (default gives n0step < 0 then weight is one)
        """

    def Start(self, items: int, cycles: int = 1) -> None:
        """
        Starts a STAT on its first phase (or its default one)
        <items> gives the total count of items, <cycles> the count of
        cycles
        If <cycles> is more than one, the first Cycle must then be
        started by NextCycle (NextStep/NextItem are ignored).
        If it is one, NextItem/NextStep can then be called
        """

    @staticmethod
    def StartCount(items: int, title: str = '') -> None:
        """
        Starts a default STAT, with no phase, no step, ready to just
        count items.
        <items> gives the total count of items
        Hence, NextItem is available to directly count
        """

    @staticmethod
    def NextPhase(items: int, cycles: int = 1) -> None:
        """
        Commands to resume the preceding phase and start a new one
        <items> and <cycles> as for Start, but for this new phase
        Ignored if count of phases is already passed
        If <cycles> is more than one, the first Cycle must then be
        started by NextCycle (NextStep/NextItem are ignored).
        If it is one, NextItem/NextStep can then be called
        """

    @staticmethod
    def SetPhase(items: int, cycles: int = 1) -> None:
        """
        Changes the parameters of the phase to start
        To be used before first counting (i.e. just after NextPhase)
        Can be used by an operator which has to reajust counts on run
        """

    @staticmethod
    def NextCycle(items: int) -> None:
        """
        Commands to resume the preceding cycle and start a new one,
        with a count of items
        Ignored if count of cycles is already passed
        Then, first step is started (or default one)
        NextItem can be called for the first step, or NextStep to pass
        to the next one
        """

    @staticmethod
    def NextStep() -> None:
        """
        Commands to resume the preceding step of the cycle
        Ignored if count of steps is already passed
        NextItem can be called for this step, NextStep passes to next
        """

    @staticmethod
    def NextItem(nbitems: int = 1) -> None:
        """
        Commands to add an item in the current step of the current
        cycle of the current phase
        By default, one item per call, can be overpassed
        Ignored if count of items of this cycle is already passed
        """

    @staticmethod
    def End() -> None:
        """
        Commands to declare the process ended (hence, advancement is
        forced to 100 %)
        """

    @staticmethod
    def Where(phase: bool = True) -> str:
        """
        Returns an identification of the STAT :
        <phase> True (D) : the name of the current phase
        <phase> False : the title of the current STAT
        """

    @staticmethod
    def Percent(phase: bool = False) -> int:
        """
        Returns the advancement as a percentage :
        <phase> True : inside the current phase
        <phase> False (D) : relative to the whole process
        """

class Interface_TypedValue(nanoocp.MoniTool.MoniTool_TypedValue):
    """
    Now strictly equivalent to TypedValue from MoniTool,
    except for ParamType which remains for compatibility reasons

    This class allows to dynamically manage .. typed values, i.e.
    values which have an alphanumeric expression, but with
    controls. Such as "must be an Integer" or "Enumerative Text"
    etc

    Hence, a TypedValue brings a specification (type + constraints
    if any) and a value. Its basic form is a string, it can be
    specified as integer or real or enumerative string, then
    queried as such.
    Its string content, which is a occ::handle<HAsciiString> can be
    shared by other data structures, hence gives a direct on line
    access to its value.
    """

    @overload
    def __init__(self, name: str, type: Interface_ParamType = Interface_ParamType.Interface_ParamText, init: str = '') -> None:
        """
        Creates a TypedValue, with a name

        type gives the type of the parameter, default is free text
        Also available : Integer, Real, Enum, Entity (i.e. Object)
        More precise specifications, titles, can be given to the
        TypedValue once created

        init gives an initial value. If it is not given, the
        TypedValue begins as "not set", its value is empty
        """

    @overload
    def __init__(self, theOther: Interface_TypedValue) -> None: ...

    def Type(self) -> Interface_ParamType:
        """
        Returns the type
        I.E. calls ValueType then makes correspondence between
        ParamType from Interface (which remains for compatibility
        reasons) and ValueType from MoniTool
        """

    @staticmethod
    def ParamTypeToValueType(typ: Interface_ParamType) -> nanoocp.MoniTool.MoniTool_ValueType:
        """Correspondence ParamType from Interface to ValueType from MoniTool"""

    @staticmethod
    def ValueTypeToParamType(typ: nanoocp.MoniTool.MoniTool_ValueType) -> Interface_ParamType:
        """Correspondence ParamType from Interface to ValueType from MoniTool"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_Static(Interface_TypedValue):
    """
    This class gives a way to manage meaningful static variables,
    used as "global" parameters in various procedures.

    A Static brings a specification (its type, constraints if any)
    and a value. Its basic form is a string, it can be specified
    as integer or real or enumerative string, and queried as such.
    Its string content, which is a occ::handle<HAsciiString> can be
    shared by other data structures, hence gives a direct on line
    access to its value.

    All this description is inherited from TypedValue

    A Static can be given an initial value, it can be filled from,
    either a set of Resources (an applicative feature which
    accesses and manages parameter files), or environment or
    internal definition : these define families of Static.
    In addition, it supports a status for reinitialisation : an
    initialisation procedure can ask if the value of the Static
    has changed from its last call, in this case does something
    then marks the Status "uptodate", else it does nothing.

    Statics are named and recorded then accessed in an alphabetic
    dictionary
    """

    @overload
    def __init__(self, family: str, name: str, type: Interface_ParamType = Interface_ParamType.Interface_ParamText, init: str = '') -> None:
        """
        Creates and records a Static, with a family and a name
        family can report to a name of resource or to a system or
        internal definition. The name must be unique.

        type gives the type of the parameter, default is free text
        Also available : Integer, Real, Enum, Entity (i.e. Object)
        More precise specifications, titles, can be given to the
        Static once created

        init gives an initial value. If it is not given, the Static
        begin as "not set", its value is empty
        """

    @overload
    def __init__(self, family: str, name: str, other: Interface_Static | None) -> None:
        """
        Creates a new Static with same definition as another one
        (value is copied, except for Entity : it remains null)
        """

    @overload
    def __init__(self, theOther: Interface_Static) -> None: ...

    def PrintStatic(self) -> str:
        """
        Writes the properties of a
        parameter in the diagnostic file. These include:
        - Name
        - Family,
        - Wildcard (if it has one)
        - Current status (empty string if it was updated or
        if it is the original one)
        - Value
        """

    def Family(self) -> str:
        """
        Returns the family. It can be : a resource name for applis,
        an internal name between : $e (environment variables),
        $l (other, purely local)
        """

    def SetWild(self, wildcard: Interface_Static | None) -> None:
        """
        Sets a "wild-card" static : its value will be considered
        if <me> is not properly set. (reset by set a null one)
        """

    def Wild(self) -> Interface_Static:
        """Returns the wildcard static, which can be (is most often) null"""

    def SetUptodate(self) -> None:
        """
        Records a Static has "uptodate", i.e. its value has been taken
        into account by a reinitialisation procedure
        This flag is reset at each successful SetValue
        """

    def UpdatedStatus(self) -> bool:
        """Returns the status "uptodate\""""

    @overload
    @staticmethod
    def Init(family: str, name: str, type: Interface_ParamType, init: str = '') -> bool:
        """
        Declares a new Static (by calling its constructor)
        If this name is already taken, does nothing and returns False
        Else, creates it and returns True
        For additional definitions, get the Static then edit it
        """

    @overload
    @staticmethod
    def Init(family: str, name: str, type: str, init: str = '') -> bool:
        """
        As Init with ParamType, but type is given as a character
        This allows a simpler call
        Types : 'i' Integer, 'r' Real, 't' Text, 'e' Enum, 'o' Object
        '=' for same definition as, <init> gives the initial Static
        Returns False if <type> does not match this list
        """

    @staticmethod
    def Static(name: str) -> Interface_Static:
        """Returns a Static from its name. Null Handle if not present"""

    @staticmethod
    def IsPresent(name: str) -> bool:
        """Returns True if a Static named <name> is present, False else"""

    @staticmethod
    def CDef(name: str, part: str) -> str:
        """
        Returns a part of the definition of a Static, as a CString
        The part is designated by its name, as a CString
        If the required value is not a string, it is converted to a
        CString then returned
        If <name> is not present, or <part> not defined for <name>,
        this function returns an empty string

        Allowed parts for CDef :
        family : the family
        type  : the type ("integer","real","text","enum")
        label : the label
        satis : satisfy function name if any
        rmin : minimum real value
        rmax : maximum real value
        imin : minimum integer value
        imax : maximum integer value
        enum nn (nn : value of an integer) : enum value for nn
        unit : unit definition for a real
        """

    @staticmethod
    def IDef(name: str, part: str) -> int:
        """
        Returns a part of the definition of a Static, as an Integer
        The part is designated by its name, as a CString
        If the required value is not a string, returns zero
        For a Boolean, 0 for false, 1 for true
        If <name> is not present, or <part> not defined for <name>,
        this function returns zero

        Allowed parts for IDef :
        imin, imax : minimum or maximum integer value
        estart : starting number for enum
        ecount : count of enum values (starting from estart)
        ematch : exact match status
        eval val : case determined from a string
        """

    @staticmethod
    def IsSet(name: str, proper: bool = True) -> bool:
        """
        Returns True if <name> is present AND set
        <proper> True (D) : considers this item only
        <proper> False    : if not set and attached to a wild-card,
        considers this wild-card
        """

    @staticmethod
    def CVal(name: str) -> str:
        """
        Returns the value of the
        parameter identified by the string name.
        If the specified parameter does not exist, an empty
        string is returned.
        Example
        Interface_Static::CVal("write.step.schema");
        which could return:
        "AP214\"
        """

    @staticmethod
    def IVal(name: str) -> int:
        """
        Returns the integer value of
        the translation parameter identified by the string name.
        Returns the value 0 if the parameter does not exist.
        Example
        Interface_Static::IVal("write.step.schema");
        which could return: 3
        """

    @staticmethod
    def RVal(name: str) -> float:
        """
        Returns the value of a static
        translation parameter identified by the string name.
        Returns the value 0.0 if the parameter does not exist.
        """

    @staticmethod
    def SetCVal(name: str, val: str) -> bool:
        """
        Modifies the value of the
        parameter identified by name. The modification is specified
        by the string val. false is returned if the parameter does not exist.
        Example
        Interface_Static::SetCVal
        ("write.step.schema","AP203")
        This syntax specifies a switch from the default STEP 214 mode to STEP 203 mode.
        """

    @staticmethod
    def SetIVal(name: str, val: int) -> bool:
        """
        Modifies the value of the
        parameter identified by name. The modification is specified
        by the integer value val. false is returned if the
        parameter does not exist.
        Example
        Interface_Static::SetIVal
        ("write.step.schema", 3)
        This syntax specifies a switch from the default STEP 214 mode to STEP 203 mode.S
        """

    @staticmethod
    def SetRVal(name: str, val: float) -> bool:
        """
        Modifies the value of a
        translation parameter. false is returned if the
        parameter does not exist. The modification is specified
        by the real number value val.
        """

    @staticmethod
    def Update(name: str) -> bool:
        """
        Sets a Static to be "uptodate"
        Returns False if <name> is not present
        This status can be used by a reinitialisation procedure to
        rerun if a value has been changed
        """

    @staticmethod
    def IsUpdated(name: str) -> bool:
        """
        Returns the status "uptodate" from a Static
        Returns False if <name> is not present
        """

    @staticmethod
    def Items(mode: int = 0, criter: str = '') -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns a list of names of statics :
        <mode> = 0 (D) : criter is for family
        <mode> = 1 : criter is regexp on names, takes final items
        (ignore wild cards)
        <mode> = 2 : idem but take only wilded, not final items
        <mode> = 3 : idem, take all items matching criter
        idem + 100 : takes only non-updated items
        idem + 200 : takes only updated items
        criter empty (D) : returns all names
        else returns names which match the given criter
        Remark : families beginning by '$' are not listed by criter ""
        they are listed only by criter "$"

        This allows for instance to set new values after having loaded
        or reloaded a resource, then to update them as required
        """

    @staticmethod
    def Standards() -> None:
        """
        Initializes all standard static parameters, which can be used
        by every function. statics specific of a norm or a function
        must be defined around it
        """

    @staticmethod
    def FillMap(theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Fills given string-to-string map with all static data"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Interface_UndefinedContent(nanoocp.Standard.Standard_Transient):
    """
    Defines resources for an "Undefined Entity" : such an Entity
    is used to describe an Entity which complies with the Norm,
    but of an Unknown Type : hence it is kept under a literal
    form (avoiding to loose data). UndefinedContent offers a way
    to store a list of Parameters, as literals or references to
    other Entities

    Each Interface must provide one "UndefinedEntity", which must
    have same basic description as all its types of entities :
    the best way would be double inheritance : on the Entity Root
    of the Norm and on an general "UndefinedEntity"

    While it is not possible to do so, the UndefinedEntity of each
    Interface can define its own UndefinedEntity by INCLUDING
    (in a field) this UndefinedContent

    Hence, for that UndefinedEntity, define a Constructor which
    creates this UndefinedContent, plus access methods to it
    (or to its data, calling methods defined here).

    Finally, the Protocols of each norm have to Create and
    Recognize Unknown Entities of this norm
    """

    @overload
    def __init__(self) -> None:
        """Defines an empty UndefinedContent"""

    @overload
    def __init__(self, theOther: Interface_UndefinedContent) -> None: ...

    def NbParams(self) -> int:
        """Gives count of recorded parameters"""

    def NbLiterals(self) -> int:
        """Gives count of Literal Parameters"""

    def ParamData(self, num: int) -> tuple[bool, Interface_ParamType, nanoocp.Standard.Standard_Transient, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns data of a Parameter : its type, and the entity if it
        designates en entity ("ent") or its literal value else ("str")
        Returned value (Boolean) : True if it is an Entity, False else
        """

    def ParamType(self, num: int) -> Interface_ParamType:
        """
        Returns the ParamType of a Param, given its rank
        Error if num is not between 1 and NbParams
        """

    def IsParamEntity(self, num: int) -> bool:
        """
        Returns True if a Parameter is recorded as an entity
        Error if num is not between 1 and NbParams
        """

    def ParamEntity(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns Entity corresponding to a Param, given its rank"""

    def ParamValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns literal value of a Parameter, given its rank"""

    def Reservate(self, nb: int, nblit: int) -> None:
        """
        Manages reservation for parameters (internal use)
        (nb : total count of parameters, nblit : count of literals)
        """

    def AddLiteral(self, ptype: Interface_ParamType, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Adds a literal Parameter to the list"""

    def AddEntity(self, ptype: Interface_ParamType, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds a Parameter which references an Entity"""

    def RemoveParam(self, num: int) -> None:
        """Removes a Parameter given its rank"""

    def SetLiteral(self, num: int, ptype: Interface_ParamType, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Sets a new value for the Parameter <num>, to a literal value
        (if it referenced formerly an Entity, this Entity is removed)
        """

    @overload
    def SetEntity(self, num: int, ptype: Interface_ParamType, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Sets a new value for the Parameter <num>, to reference an
        Entity. To simply change the Entity, see the variant below
        """

    @overload
    def SetEntity(self, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Changes the Entity referenced by the Parameter <num>
        (with same ParamType)
        """

    def EntityList(self) -> Interface_EntityList:
        """
        Returns globally the list of param entities. Note that it can
        be used as shared entity list for the UndefinedEntity
        """

    def GetFromAnother(self, other: Interface_UndefinedContent | None, TC: Interface_CopyTool) -> None:
        """
        Copies contents of undefined entities; deigned to be called by
        GetFromAnother method from Undefined entity of each Interface
        (the basic operation is the same regardless the norm)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
