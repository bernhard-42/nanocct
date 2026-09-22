"""OCCT package IFSelect (toolkit TKXSBase)"""

import enum
from typing import TextIO, overload

import nanoocp.IFGraph
import nanoocp.Interface
import nanoocp.MoniTool
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class IFSelect_ReturnStatus(enum.IntEnum):
    """
    Qualifies an execution status :
    RetVoid  : normal execution which created nothing, or
    no data to process
    RetDone  : normal execution with a result
    RetError : error in command or input data, no execution
    RetFail  : execution was run and has failed
    RetStop  : indicates end or stop (such as Raise)
    """

    IFSelect_RetVoid = 0

    IFSelect_RetDone = 1

    IFSelect_RetError = 2

    IFSelect_RetFail = 3

    IFSelect_RetStop = 4

IFSelect_RetVoid: IFSelect_ReturnStatus = IFSelect_ReturnStatus.IFSelect_RetVoid

IFSelect_RetDone: IFSelect_ReturnStatus = IFSelect_ReturnStatus.IFSelect_RetDone

IFSelect_RetError: IFSelect_ReturnStatus = IFSelect_ReturnStatus.IFSelect_RetError

IFSelect_RetFail: IFSelect_ReturnStatus = IFSelect_ReturnStatus.IFSelect_RetFail

IFSelect_RetStop: IFSelect_ReturnStatus = IFSelect_ReturnStatus.IFSelect_RetStop

class IFSelect_PrintCount(enum.IntEnum):
    """
    Lets you choose the manner in which you want to analyze an
    IGES or STEP file. Your analysis can be either message-oriented or
    entity-oriented. The specific values are as follows:
    - ItemsByEntity is a sequential list of all
    messages per entity of the defined type
    - CountByItem is the number of entities of the defined
    type, with their rank number per message
    - ShortByItem is the number of entities of the defined
    type, with their types per message; displays the rank
    numbers of the first five entities of the defined type
    per message
    - ListByItem is the number of entities of the defined type
    per message and the numbers of the entities
    - EntitiesByItem is the number of entities of the
    defined type, with their types, rank numbers and
    Directory Entry numbers per message
    - GeneralInfo is general information on transfer such as:
    -      number of entities
    -      number of roots
    -      number of resulting Open CASCADE shapes
    -      number of warnings and failures
    -      CountSummary summary statistics for counters and signatures
    -      ResultCount information that contains the number of
    roots in the IGES file and the number of resulting Open CASCADE shapes.
    -       Mapping of the IGES root entities to the resulting Open
    CASCADE shape (including type and form of the IGES entity
    and type of the resulting shape).
    """

    IFSelect_ItemsByEntity = 0

    IFSelect_CountByItem = 1

    IFSelect_ShortByItem = 2

    IFSelect_ListByItem = 3

    IFSelect_EntitiesByItem = 4

    IFSelect_CountSummary = 5

    IFSelect_GeneralInfo = 6

    IFSelect_Mapping = 7

    IFSelect_ResultCount = 8

IFSelect_ItemsByEntity: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_ItemsByEntity

IFSelect_CountByItem: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_CountByItem

IFSelect_ShortByItem: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_ShortByItem

IFSelect_ListByItem: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_ListByItem

IFSelect_EntitiesByItem: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_EntitiesByItem

IFSelect_CountSummary: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_CountSummary

IFSelect_GeneralInfo: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_GeneralInfo

IFSelect_Mapping: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_Mapping

IFSelect_ResultCount: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_ResultCount

class IFSelect_EditValue(enum.IntEnum):
    """
    Controls access on Values by an Editor
    EditOptional  : normal access, in addition may be removed
    Editable      : normal access, must be present
    EditProtected : access must be validated
    EditComputed  : why write it ?  it will be recomputed
    EditRead      : no way to write it, only for read
    EditDynamic   : not a field, only to be displayed
    """

    IFSelect_Optional = 0

    IFSelect_Editable = 1

    IFSelect_EditProtected = 2

    IFSelect_EditComputed = 3

    IFSelect_EditRead = 4

    IFSelect_EditDynamic = 5

IFSelect_Optional: IFSelect_EditValue = IFSelect_EditValue.IFSelect_Optional

IFSelect_Editable: IFSelect_EditValue = IFSelect_EditValue.IFSelect_Editable

IFSelect_EditProtected: IFSelect_EditValue = IFSelect_EditValue.IFSelect_EditProtected

IFSelect_EditComputed: IFSelect_EditValue = IFSelect_EditValue.IFSelect_EditComputed

IFSelect_EditRead: IFSelect_EditValue = IFSelect_EditValue.IFSelect_EditRead

IFSelect_EditDynamic: IFSelect_EditValue = IFSelect_EditValue.IFSelect_EditDynamic

class IFSelect_PrintFail(enum.IntEnum):
    """
    Indicates whether there will
    be information on warnings as well as on failures. The
    terms of this enumeration have the following semantics:
    - IFSelect_FailOnly gives information on failures only
    - IFSelect_FailAndWarn gives information on both
    failures and warnings. used to pilot PrintCheckList
    """

    IFSelect_FailOnly = 0

    IFSelect_FailAndWarn = 1

IFSelect_FailOnly: IFSelect_PrintFail = IFSelect_PrintFail.IFSelect_FailOnly

IFSelect_FailAndWarn: IFSelect_PrintFail = IFSelect_PrintFail.IFSelect_FailAndWarn

class IFSelect_RemainMode(enum.IntEnum):
    IFSelect_RemainForget = 0

    IFSelect_RemainCompute = 1

    IFSelect_RemainDisplay = 2

    IFSelect_RemainUndo = 3

IFSelect_RemainForget: IFSelect_RemainMode = IFSelect_RemainMode.IFSelect_RemainForget

IFSelect_RemainCompute: IFSelect_RemainMode = IFSelect_RemainMode.IFSelect_RemainCompute

IFSelect_RemainDisplay: IFSelect_RemainMode = IFSelect_RemainMode.IFSelect_RemainDisplay

IFSelect_RemainUndo: IFSelect_RemainMode = IFSelect_RemainMode.IFSelect_RemainUndo

class IFSelect:
    """
    Gives tools to manage Selecting a group of Entities
    processed by an Interface, for instance to divide up an
    original Model (from a File) to several smaller ones
    They use description of an Interface Model as a graph

    Remark that this corresponds to the description of a
    "scenario" of sharing out a File. Parts of this Scenario
    are intended to be permanently stored. IFSelect provides
    the Transient, active counterparts (to run the Scenario).
    But a permanent one (either as Persistent Objects or as
    interpretable Text) must be provided elsewhere.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IFSelect) -> None: ...

    @staticmethod
    def SaveSession(WS: IFSelect_WorkSession | None, file: str) -> bool:
        """
        Saves the state of a WorkSession from IFSelect, by using a
        SessionFile from IFSelect. Returns True if Done, False in
        case of Error on Writing. <file> gives the name of the File
        to be produced (this avoids to export the class SessionFile).
        """

    @staticmethod
    def RestoreSession(WS: IFSelect_WorkSession | None, file: str) -> bool:
        """
        Restore the state of a WorkSession from IFSelect, by using a
        SessionFile from IFSelect. Returns True if Done, False in
        case of Error on Writing. <file> gives the name of the File
        to be used (this avoids to export the class SessionFile).
        """

class IFSelect_Activator(nanoocp.Standard.Standard_Transient):
    """
    Defines the general frame for working with a SessionPilot.
    Each Activator treats a set of Commands. Commands are given as
    alphanumeric strings. They can be of two main forms :
    - classic, to list, evaluate, enrich the session (by itself) :
    no specific remark, its complete execution must be described
    - creation of a new item : instead of creatinf it plus adding
    it to the session (which is a classic way), it is possible
    to create it and make it recorded by the SessionPilot :
    then, the Pilot will add it to the session; this way allows
    the Pilot to manage itself named items

    In order to make easier the use of Activator, this class
    provides a simple way to Select an Actor for a Command :
    each sub-class of SectionActor defines the command titles it
    recognizes, plus attaches a Number, unique for this sub-class,
    to each distinct command title.

    Each time an action is required, the corresponding Number
    can then be given to help the selection of the action to do.

    The result of an Execution must indicate if it is worth to be
    recorded or not : see method Do
    """

    @staticmethod
    def Adding(actor: IFSelect_Activator | None, number: int, command: str, mode: int) -> None:
        """
        Records, in a Dictionary available for all the Activators,
        the command title an Activator can process, attached with
        its number, proper for this Activator
        <mode> allows to distinguish various execution modes
        0: default mode; 1 : for xset
        """

    def Add(self, number: int, command: str) -> None:
        """
        Allows a self-definition by an Activator of the Commands it
        processes, call the class method Adding (mode 0)
        """

    def AddSet(self, number: int, command: str) -> None:
        """
        Same as Add but specifies that this command is candidate for
        xset (creation of items, xset : named items; mode 1)
        """

    @staticmethod
    def Remove(command: str) -> None:
        """Removes a Command, if it is recorded (else, does nothing)"""

    @staticmethod
    def Select(command: str) -> tuple[bool, int, IFSelect_Activator]:
        """
        Selects, for a Command given by its title, an actor with its
        command number. Returns True if found, False else
        """

    @staticmethod
    def Mode(command: str) -> int:
        """Returns mode recorded for a command. -1 if not found"""

    @staticmethod
    def Commands(mode: int = -1, command: str = '') -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns, for a root of command title, the list of possible
        commands.
        <mode> : -1 (D) for all commands if <commands> is empty
        -1 + command : about a Group , >= 0 see Adding
        By default, it returns the whole list of known commands.
        """

    def Do(self, number: int, pilot: IFSelect_SessionPilot | None) -> IFSelect_ReturnStatus:
        """
        Tries to execute a Command Line. <number> is the number of the
        command for this Activator. It Must forecast to record the
        result of the execution, for need of Undo-Redo
        Must Returns : 0 for a void command (not to be recorded),
        1 if execution OK, -1 if command incorrect, -2 if error
        on execution
        """

    def Help(self, number: int) -> str:
        """
        Sends a short help message for a given command identified by
        it number for this Activator (must take one line max)
        """

    def Group(self) -> str: ...

    def File(self) -> str: ...

    def SetForGroup(self, group: str, file: str = '') -> None:
        """
        Group and SetGroup define a "Group of commands" which
        correspond to an Activator. Default is "XSTEP"
        Also a file may be attached
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SessionPilot(IFSelect_Activator):
    """
    A SessionPilot is intended to make easier the use of a WorkSession.
    It receives commands, under alphanumeric form,
    then calls a library of Activators to interpret and run them.

    Then, WorkSession just records data required to work :
    Rules for Selection, Dispatch ... ; File Data (InterfaceModel
    and results of Evaluations and Transfer as required).
    SessionPilot records and works with alphanumeric commands and
    their results (under a very simple form). It calls a list of
    Activators to perform the actions.

    A Command can have several forms :
    - classic execution, to list, evaluate, or enrich the session
    - command which creates a new item (a Selection for instance)
    such a command should not add it to the session, but make it
    recorded by the Pilot (method RecordItem). The Pilot will
    add the item in the session, with no name
    -> such a command may be called :
    - directly, it will add an item with no name
    - by command xset, in the following form :
    xset name command ... calls the command and adds the item
    to the session under the specified name (if not yet known)

    Thus, to a specific Norm or way of working, only Activators
    change. A specific Initialisation can be done by starting
    with a specific set of commands.

    In addition, SessionPilot is a sub-type of Activator, to
    recognize some built-in commands : exit/x, help/?, control of
    command line, and commands xstep xset ... See method Do

    At least, empty lines and comment lines (beginning by '#')
    are skipped (comment lines are display if read from file)
    """

    @overload
    def __init__(self, prompt: str = '') -> None:
        """
        Creates an empty SessionPilot, with a prompt which will be
        displayed on querying commands. If not precised (""), this
        prompt is set to "Test-XSTEP>\"
        """

    @overload
    def __init__(self, theOther: IFSelect_SessionPilot) -> None: ...

    def Session(self) -> IFSelect_WorkSession:
        """Returns the WorkSession which is worked on"""

    def Library(self) -> IFSelect_WorkLibrary:
        """
        Returns the WorKlibrary (Null if not set). WorkLibrary is used
        to Read and Write Files, according to the Norm
        """

    def RecordMode(self) -> bool:
        """Returns the Record Mode for Commands. Default is False."""

    def SetSession(self, WS: IFSelect_WorkSession | None) -> None:
        """Sets a WorkSession to be worked on"""

    def SetLibrary(self, WL: IFSelect_WorkLibrary | None) -> None:
        """Sets a WorkLibrary"""

    def SetRecordMode(self, mode: bool) -> None:
        """Changes the RecordMode."""

    def SetCommandLine(self, command: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets the value of the Command Line to be interpreted
        Also prepares the interpretation (splitting by blanks)
        """

    def CommandLine(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the Command Line to be interpreted"""

    def CommandPart(self, numarg: int = 0) -> str:
        """
        Returns the part of the command line which begins at argument
        <numarg> between 0 and NbWords-1 (by default, all the line)
        Empty string if out of range
        """

    def NbWords(self) -> int:
        """
        Returns the count of words of the Command Line, separated by
        blanks : 0 if empty, one if a command without args, else it
        gives the count of args minus one.
        Warning : limited to 10 (command title + 9 args)
        """

    def Word(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a word given its rank in the Command Line. Begins at 0
        which is the Command Title, 1 is the 1st arg., etc...
        """

    def Arg(self, num: int) -> str:
        """
        Returns a word given its rank, as a CString.
        As for Word, begins at 0 (the command name), etc...
        """

    def RemoveWord(self, num: int) -> bool:
        """
        Removes a word given its rank. Returns True if Done, False if
        <num> is out of range
        """

    def NbCommands(self) -> int:
        """Returns the count of recorded Commands"""

    def Command(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a recorded Command, given its rank (from 1)"""

    def RecordItem(self, item: nanoocp.Standard.Standard_Transient | None) -> IFSelect_ReturnStatus:
        """
        Allows to associate a Transient Value with the last execution
        as a partial result
        Returns RetDone if item is not Null, RetFail if item is Null
        Remark : it is nullified for each Perform
        """

    def RecordedItem(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Transient Object which was recorded with the
        current Line Command. If none was, returns a Null Handle
        """

    def Clear(self) -> None:
        """Clears the recorded information (commands, objects)"""

    def ReadScript(self, file: str = '') -> IFSelect_ReturnStatus:
        """
        Reads commands from a Script File, named <file>. By default
        (file = ""), reads from standard input with a prompt
        Else (reading from a file), the read commands are displayed
        onto standard output. Allows nested reads. Reading is stopped
        either by command x or exit, or by reaching end of file
        Return Value follows the rules of Do : RetEnd for normal end,
        RetFail if script could not be opened
        """

    def Perform(self) -> IFSelect_ReturnStatus:
        """
        Executes the Command, itself (for built-in commands, which
        have priority) or by using the list of Activators.
        The value returned is : RetVoid if nothing done (void command)
        RetDone if execution OK, RetEnd if END OF SESSION, RetError if
        command unknown or incorrect, RetFail if error on execution
        If execution is OK and RecordMode is set, this Command Line is
        recorded to the list (see below).
        """

    def ExecuteAlias(self, aliasname: nanoocp.TCollection.TCollection_AsciiString) -> IFSelect_ReturnStatus:
        """
        Executes the Commands, except that the command name (word 0)
        is aliased. The rest of the command line is unchanged
        If <alias> is empty, Executes with no change

        Error status is returned if the alias is unknown as command
        """

    def Execute(self, command: nanoocp.TCollection.TCollection_AsciiString) -> IFSelect_ReturnStatus:
        """
        Sets the Command then tries to execute it. Return value :
        same as for Perform
        """

    def ExecuteCounter(self, counter: IFSelect_SignCounter | None, numword: int, mode: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_CountByItem) -> IFSelect_ReturnStatus:
        """
        Executes a Counter in a general way
        If <numword> is greater than count of command words, it counts
        all the model. Else it considers the word <numword> as the
        identifier of a Selection
        <mode> gives the mode of printing results, default is
        CountByItem
        """

    def Number(self, val: str) -> int:
        """
        Interprets a string value as an entity number :
        if it gives an integer, returns its value
        else, considers it as ENtityLabel (preferably case sensitive)
        in case of failure, returns 0
        """

    def Do(self, number: int, session: IFSelect_SessionPilot | None) -> IFSelect_ReturnStatus:
        """
        Processes specific commands, which are :
        x or exit for end of session
        ? or help for help messages
        xcommand to control command lines (Record Mode, List, Clear,
        File Output ...)
        xsource to execute a command file (no nesting allowed),
        in case of error, source is stopped and keyword recovers
        xstep is a simple prefix (useful in a wider environment, to
        avoid conflicts on command names)
        xset control commands which create items with names
        """

    def Help(self, number: int) -> str:
        """Help for specific commands (apart from general command help)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_Act(IFSelect_Activator):
    """
    Act gives a simple way to define and add functions to be ran
    from a SessionPilot, as follows :

    Define a function as
    static IFSelect_RetStatus myfunc
    (const char* const name,
    const occ::handle<IFSelect_SessionPilot>& pilot)
    { ... }
    When ran, it receives the exact name (string) of the called
    function, and the SessionPilot which brings other infos

    Add it by
    IFSelect_Act::AddFunc (name,help,myfunc);
    for a normal function, or
    IFSelect_Act::AddFSet (name,help,myfunc);
    for a function which is intended to create a control item
    name and help are given as CString

    Then, it is available for run
    """

    def __init__(self, theOther: IFSelect_Act) -> None: ...

    def Do(self, number: int, pilot: IFSelect_SessionPilot | None) -> IFSelect_ReturnStatus:
        """
        Execution of Command Line. remark that <number> is senseless
        because each Act brings one and only one function
        """

    def Help(self, number: int) -> str:
        """Short Help for commands : returns the help given to create"""

    @staticmethod
    def SetGroup(group: str, file: str = '') -> None:
        """
        Changes the default group name for the following Acts
        group empty means to come back to default from Activator
        Also a file name can be precised (to query by getsource)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_GeneralModifier(nanoocp.Standard.Standard_Transient):
    """
    This class gives a frame for Actions which modify the effect
    of a Dispatch, i.e. :
    By Selections and Dispatches, an original Model can be
    split into one or more "target" Models : these Models
    contain Entities copied from the original one (that is, a
    part of it). Basically, these dispatched Entities are copied
    as identical to their original counterparts. Also the copied
    Models reproduce the Header of the original one.

    Modifiers allow to change this copied content : this is the
    way to be used for any kind of alterations, adaptations ...
    They are exploited by a ModelCopier, which firstly performs
    the copy operation described by Dispatches, then invokes the
    Modifiers to work on the result.

    Each GeneralModifier can be attached to :
    - all the Models produced
    - a Dispatch (it will be applied to all the Models obtained
    from this Dispatch) designated by its Ident in a ShareOut
    - in addition, to a Selection (facultative) : this adds a
    criterium, the Modifier is invoked on a produced Model only
    if this Model contains an Entity copied from one of the
    Entities designated by this Selection.
    (for special Modifiers from IFAdapt, while they must work on
    definite Entities, this Selection is mandatory to run)

    Remark : this class has no action attached, it only provides
    a frame to work on criteria. Then, sub-classes will define
    their kind of action, which can be applied at a precise step
    of the production of a File : see Modifier, and in the
    package IFAdapt, EntityModifier and EntityCopier
    """

    def MayChangeGraph(self) -> bool:
        """
        Returns True if this modifier may change the graph of
        dependences (acknowledged at creation time)
        """

    def SetDispatch(self, disp: IFSelect_Dispatch | None) -> None:
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it
        (to apply the Modifier on every Dispatch)
        """

    def Dispatch(self) -> IFSelect_Dispatch:
        """Returns the Dispatch to be matched, Null if not set"""

    def Applies(self, disp: IFSelect_Dispatch | None) -> bool:
        """
        Returns True if a Model obtained from the Dispatch <disp>
        is to be treated (apart from the Selection criterium)
        If Dispatch(me) is Null, returns True. Else, checks <disp>
        """

    def SetSelection(self, sel: IFSelect_Selection | None) -> None:
        """
        Sets a Selection : a Model is treated if it contains one or
        more Entities designated by the Selection
        """

    def ResetSelection(self) -> None:
        """Resets the Selection : this criterium is not longer active"""

    def HasSelection(self) -> bool:
        """Returns True if a Selection is set as an additional criterium"""

    def Selection(self) -> IFSelect_Selection:
        """Returns the Selection, or a Null Handle if not set"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a short text which defines the operation performed"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_AppliedModifiers(nanoocp.Standard.Standard_Transient):
    """
    This class allows to memorize and access to the modifiers
    which are to be applied to a file. To each modifier, is bound
    a list of integers (optional) : if this list is absent,
    the modifier applies to all the file. Else, it applies to the
    entities designated by these numbers in the produced file.

    To record a modifier, and a possible list of entity numbers to be applied on:
    AddModif (amodifier);
    loop on  AddNum (anumber);

    To query it,  Count gives the count of recorded modifiers, then for each one:
    Item (numodif, amodifier, entcount);
    IsForAll ()  -> can be called, if True, applies on the whole file

    for (i = 1; i <= entcount; i ++)
    nument = ItemNum (i);  -> return an entity number
    """

    @overload
    def __init__(self, nbmax: int, nbent: int) -> None:
        """
        Creates an AppliedModifiers, ready to record up to <nbmax>
        modifiers, on a model of <nbent> entities
        """

    @overload
    def __init__(self, theOther: IFSelect_AppliedModifiers) -> None: ...

    def AddModif(self, modif: IFSelect_GeneralModifier | None) -> bool:
        """
        Records a modifier. By default, it is to apply on all a
        produced file. Further calls to AddNum will restrict this.
        Returns True if done, False if too many modifiers are already
        recorded
        """

    def AddNum(self, nument: int) -> bool:
        """
        Adds a number of entity of the output file to be applied on.
        If a sequence of AddNum is called after AddModif, this
        Modifier will be applied on the list of designated entities.
        Else, it will be applied on all the file
        Returns True if done, False if no modifier has yet been added
        """

    def Count(self) -> int:
        """Returns the count of recorded modifiers"""

    def Item(self, num: int) -> tuple[bool, IFSelect_GeneralModifier, int]:
        """
        Returns the description for applied modifier n0 <num> :
        the modifier itself, and the count of entities to be applied
        on. If no specific list of number has been defined, returns
        the total count of entities of the file
        If this count is zero, then the modifier applies to all
        the file (see below). Else, the numbers are then queried by
        calls to ItemNum between 1 and <entcount>
        Returns True if OK, False if <num> is out of range
        """

    def ItemNum(self, nument: int) -> int:
        """
        Returns a numero of entity to be applied on, given its rank
        in the list. If no list is defined (i.e. for all the file),
        returns <nument> itself, to give all the entities of the file
        Returns 0 if <nument> out of range
        """

    def ItemList(self) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """
        Returns the list of entities to be applied on (see Item)
        as a HSequence (IsForAll produces the complete list of all
        the entity numbers of the file
        """

    def IsForAll(self) -> bool:
        """
        Returns True if the applied modifier queried by last call to
        Item is to be applied to all the produced file.
        Else, <entcount> returned by Item gives the count of entity
        numbers, each one is queried by ItemNum
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SessionDumper(nanoocp.Standard.Standard_Transient):
    """
    A SessionDumper is called by SessionFile. It takes into
    account a set of classes (such as Selections, Dispatches ...).
    SessionFile writes the Type (as defined by cdl) of each Item
    and its general Parameters. It manages the names of the Items.

    A SessionDumper must be able to Write the Parameters which are
    own of each Item it takes into account, given its Class, then
    to Recognize the Type and Read its Own Parameters to create
    an Item of this Type with these own Parameters.

    Then, there must be defined one sub-type of SessionDumper per
    consistent set of classes (e.g. a package).

    By Own Parameters, understand Parameters given at Creation Time
    if there are, or specific of a given class, apart from those
    defined at superclass levels (e.g. Final Selection for a
    Dispatch, Input Selection for a SelectExtract or SelectDeduct,
    Direct Status for a SelectExtract, etc...).

    The Parameters are those stored in a WorkSession, they can be
    of Types : IntParam, HAsciiString (for TextParam), Selection,
    Dispatch.

    SessionDumpers are organized in a Library which is used by
    SessionFile. They are put at Creation Time in this Library.
    """

    @staticmethod
    def First() -> IFSelect_SessionDumper:
        """
        Returns the First item of the Library of Dumper. The Next ones
        are then obtained by Next on the returned items
        """

    def Next(self) -> IFSelect_SessionDumper:
        """
        Returns the Next SesionDumper in the Library. Returns a Null
        Handle at the End.
        """

    def WriteOwn(self, file: IFSelect_SessionFile, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Writes the Own Parameters of a given Item, if it forecast to
        manage its Type.
        Returns True if it has recognized the Type of the Item (in
        this case, it is assumed to have written the Own Parameters if
        there are some), False else : in that case, SessionFile will
        try another SessionDumper in the Library.
        WriteOwn can use these methods from SessionFile : SendVoid,
        SendItem, SendText, and if necessary, WorkSession.
        """

    def ReadOwn(self, file: IFSelect_SessionFile, type: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Recognizes a Type (given as <type>) then Creates an Item of
        this Type with the Own Parameter, as required.
        Returns True if it has recognized the Type (in this case, it
        is assumed to have created the Item, returned as <item>),
        False else : in that case, SessionFile will try another
        SessionDumper in the Library.
        ReadOwn can use these methods from SessionFile to access Own
        Parameters : NbOwnParams, IsVoid, IsText, TextValue, ItemValue
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_BasicDumper(IFSelect_SessionDumper):
    """
    BasicDumper takes into account, for SessionFile, all the
    classes defined in the package IFSelect : Selections,
    Dispatches (there is no Modifier)
    """

    @overload
    def __init__(self) -> None:
        """Creates a BasicDumper and puts it into the Library of Dumper"""

    @overload
    def __init__(self, theOther: IFSelect_BasicDumper) -> None: ...

    def WriteOwn(self, file: IFSelect_SessionFile, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Write the Own Parameters of Types defined in package IFSelect
        Returns True if <item> has been processed, False else
        """

    def ReadOwn(self, file: IFSelect_SessionFile, type: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Recognizes and Read Own Parameters for Types of package
        IFSelect. Returns True if done and <item> created, False else
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SignatureList(nanoocp.Standard.Standard_Transient):
    """
    A SignatureList is given as result from a Counter (any kind)
    It gives access to a list of signatures, with counts, and
    optionally with list of corresponding entities

    It can also be used only to give a signature, through SignOnly
    Mode. This can be useful for a specific counter (used in a
    Selection), while it remains better to use a Signature
    whenever possible
    """

    @overload
    def __init__(self, withlist: bool = False) -> None:
        """
        Creates a SignatureList. If <withlist> is True, entities will
        be not only counted per signature, but also listed.
        """

    @overload
    def __init__(self, theOther: IFSelect_SignatureList) -> None: ...

    def SetList(self, withlist: bool) -> None:
        """
        Changes the record-list status. The list is not cleared but
        its use changes
        """

    def ModeSignOnly(self) -> bool:
        """
        Returns modifiable the SignOnly Mode
        If False (D), the counter normally counts
        If True, the counting work is turned off, Add only fills the
        LastValue, which can be used as signature, when a counter
        works from data which are not available from a Signature
        """

    def SetModeSignOnly(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModeSignOnly() returns by reference in C++.
        """

    def Clear(self) -> None: ...

    def Add(self, ent: nanoocp.Standard.Standard_Transient | None, sign: str) -> None:
        """
        Adds an entity with its signature, i.e. :
        - counts an item more for <sign>
        - if record-list status is set, records the entity
        Accepts a null entity (the signature is then for the global
        model). But if the string is empty, counts a Null item.

        If SignOnly Mode is set, this work is replaced by just
        setting LastValue
        """

    def LastValue(self) -> str:
        """
        Returns the last value recorded by Add (only if SignMode set)
        Cleared by Clear or Init
        """

    def Init(self, name: str, count: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, int], list: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient], nbnuls: int) -> None:
        """Acknowledges the list in once. Name identifies the Signature"""

    def List(self, root: str = '') -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of signatures, as a sequence of strings
        (but without their respective counts). It is ordered.
        By default, for all the signatures.
        If <root> is given non empty, for the signatures which
        begin by <root>
        """

    def HasEntities(self) -> bool:
        """
        Returns True if the list of Entities is acknowledged, else
        the method Entities will always return a Null Handle
        """

    def NbNulls(self) -> int:
        """Returns the count of null entities"""

    def NbTimes(self, sign: str) -> int:
        """
        Returns the number of times a signature was counted,
        0 if it has not been recorded at all
        """

    def Entities(self, sign: str) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities attached to a signature
        It is empty if <sign> has not been recorded
        It is a Null Handle if the list of entities is not known
        """

    def SetName(self, name: str) -> None:
        """Defines a name for a SignatureList (used to print it)"""

    def Name(self) -> str:
        """
        Returns the recorded Name.
        Remark : default is "..." (no SetName called)
        """

    def PrintCount(self) -> str:
        """Prints the counts of items (not the list)"""

    def PrintList(self, model: nanoocp.Interface.Interface_InterfaceModel | None, mod: IFSelect_PrintCount = IFSelect_PrintCount.IFSelect_ListByItem) -> str:
        """
        Prints the lists of items, if they are present (else, prints
        a message "no list available")
        Uses <model> to determine for each entity to be listed, its
        number, and its specific identifier (by PrintLabel)
        <mod> gives a mode for printing :
        - CountByItem : just count (as PrintCount)
        - ShortByItem : minimum i.e. count plus 5 first entity numbers
        - ShortByItem(D) complete list of entity numbers (0: "Global")
        - EntitiesByItem : list of (entity number/PrintLabel from the model)
        other modes are ignored
        """

    def PrintSum(self) -> str:
        """
        Prints a summary
        Item which has the greatest count of entities
        For items which are numeric values : their count, maximum,
        minimum values, cumul, average
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_CheckCounter(IFSelect_SignatureList):
    """
    A CheckCounter allows to see a CheckList (i.e. CheckIterator)
    not per entity, its messages, but per message, the entities
    attached (count and list). Because many messages can be
    repeated if they are due to systematic errors
    """

    @overload
    def __init__(self, withlist: bool = False) -> None:
        """Creates a CheckCounter, empty ready to work"""

    @overload
    def __init__(self, theOther: IFSelect_CheckCounter) -> None: ...

    def SetSignature(self, sign: nanoocp.MoniTool.MoniTool_SignText | None) -> None:
        """
        Sets a specific signature
        Else, the current SignType (in the model) is used
        """

    def Signature(self) -> nanoocp.MoniTool.MoniTool_SignText:
        """Returns the Signature;"""

    def Analyse(self, list: nanoocp.Interface.Interface_CheckIterator, model: nanoocp.Interface.Interface_InterfaceModel | None, original: bool = False, failsonly: bool = False) -> None:
        """
        Analyses a CheckIterator according a Model (which detains the
        entities for which the CheckIterator has messages), i.e.
        counts messages for entities
        If <original> is True, does not consider final messages but
        those before interpretation (such as inserting variables :
        integers, reals, strings)
        If <failsonly> is True, only Fails are considered
        Remark : global messages are recorded with a Null entity
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ContextModif:
    """
    This class gathers various information used by Model Modifiers
    apart from the target model itself, and the CopyTool which
    must be passed directly.

    These information report to original data : model, entities,
    and the selection list if there is one : it allows to query
    about such or such starting entity, or result entity, or
    iterate on selection list ...
    Also data useful for file output are available (because some
    Modifiers concern models produced for file output).

    Furthermore, in return, ContextModif can record Checks, either
    one for all, or one for each Entity. It supports trace too.
    """

    @overload
    def __init__(self, graph: nanoocp.Interface.Interface_Graph, filename: str = '') -> None:
        """
        Prepares a ContextModif with these information :
        - the graph established from original model (target passed
        directly to Modifier)
        - an optional file name (for file output)
        Here, no CopyControl, hence all entities are considered equal
        as starting and result

        Such a ContextModif is considered to be applied on all
        transferred entities (no filter active)
        """

    @overload
    def __init__(self, graph: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool, filename: str = '') -> None:
        """
        Prepares a ContextModif with these information :
        - the graph established from original model (target passed
        directly to Modifier)
        - the CopyTool which detains the CopyControl, which maps
        starting (in original) and result (in target) entities
        - an optional file name (for file output)

        Such a ContextModif is considered to be applied on all
        transferred entities (no filter active)
        """

    @overload
    def __init__(self, theOther: IFSelect_ContextModif) -> None: ...

    def Select(self, list: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        This method requires ContextModif to be applied with a filter.
        If a ModelModifier is defined with a Selection criterium,
        the result of this Selection is used as a filter :
        - if none of its items has been transferred, the modification
        does not apply at all
        - else, the Modifier can query for what entities were selected
        and what are their results
        - if this method is not called before working, the Modifier
        has to work on the whole Model
        """

    def OriginalGraph(self) -> nanoocp.Interface.Interface_Graph:
        """
        Returns the original Graph (compared to OriginalModel, it
        gives more query capabilitites)
        """

    def OriginalModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the original model"""

    def SetProtocol(self, proto: nanoocp.Interface.Interface_Protocol | None) -> None:
        """Allows to transmit a Protocol as part of a ContextModif"""

    def Protocol(self) -> nanoocp.Interface.Interface_Protocol:
        """Returns the Protocol (Null if not set)"""

    def HasFileName(self) -> bool:
        """Returns True if a non empty file name has been defined"""

    def FileName(self) -> str:
        """Returns File Name (can be empty)"""

    def Control(self) -> nanoocp.Interface.Interface_CopyControl:
        """Returns the map for a direct use, if required"""

    def IsForNone(self) -> bool:
        """
        Returns True if Select has determined that a Modifier may not
        be run (filter defined and empty)
        """

    def IsForAll(self) -> bool:
        """
        Returns True if no filter is defined : a Modifier has to work
        on all entities of the resulting (target) model
        """

    def IsTransferred(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Returns True if a starting item has been transferred"""

    def IsSelected(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Returns True if a starting item has been transferred and selected"""

    def SelectedOriginal(self) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of original selected items.
        See also the iteration
        """

    def SelectedResult(self) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of resulting counterparts of selected items.
        See also the iteration
        """

    def SelectedCount(self) -> int:
        """Returns the count of selected and transferred items"""

    def Start(self) -> None:
        """
        Starts an iteration on selected items. It takes into account
        IsForAll/IsForNone, by really iterating on all selected items.
        """

    def More(self) -> bool:
        """Returns True until the iteration has finished"""

    def Next(self) -> None:
        """Advances the iteration"""

    def ValueOriginal(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the current selected item in the original model"""

    def ValueResult(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the result counterpart of current selected item
        (in the target model)
        """

    def TraceModifier(self, modif: IFSelect_GeneralModifier | None) -> None:
        """
        Traces the application of a Modifier. Works with default trace
        File and Level. Fills the trace if default trace level is at
        least 1. Traces the Modifier (its Label) and its Selection if
        there is one (its Label).
        To be called after Select (because status IsForAll is printed)
        Worths to trace a global modification. See also Trace below
        """

    def Trace(self, mess: str = '') -> None:
        """
        Traces the modification of the current entity (see above,
        ValueOriginal and ValueResult) for default trace level >= 2.
        To be called on each individual entity really modified
        <mess> is an optional additional message
        """

    def AddCheck(self, check: nanoocp.Interface.Interface_Check | None) -> None:
        """
        Adds a Check to the CheckList. If it is empty, nothing is done
        If it concerns an Entity from the Original Model (by SetEntity)
        to which another Check is attached, it is merged to it.
        Else, it is added or merged as to GlobalCheck.
        """

    def AddWarning(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """
        Adds a Warning Message for an Entity from the original Model
        If <start> is not an Entity from the original model (e.g. the
        model itself) this message is added to Global Check.
        """

    def AddFail(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """
        Adds a Fail Message for an Entity from the original Model
        If <start> is not an Entity from the original model (e.g. the
        model itself) this message is added to Global Check.
        """

    @overload
    def CCheck(self, num: int = 0) -> nanoocp.Interface.Interface_Check:
        """
        Returns a Check given an Entity number (in the original Model)
        by default a Global Check. Creates it the first time.
        It can then be acknowledged on the spot, in condition that the
        caller works by reference ("Interface_Check& check = ...")
        """

    @overload
    def CCheck(self, start: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check:
        """
        Returns a Check attached to an Entity from the original Model
        It can then be acknowledged on the spot, in condition that the
        caller works by reference ("Interface_Check& check = ...")
        """

    def CheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """Returns the complete CheckList"""

class IFSelect_ContextWrite:
    """
    This class gathers various information used by File Modifiers
    apart from the writer object, which is specific of the norm
    and of the physical format

    These information are controlled by an object AppliedModifiers
    (if it is not defined, no modification is allowed on writing)

    Furthermore, in return, ContextModif can record Checks, either
    one for all, or one for each Entity. It supports trace too.
    """

    @overload
    def __init__(self, model: nanoocp.Interface.Interface_InterfaceModel | None, proto: nanoocp.Interface.Interface_Protocol | None, applieds: IFSelect_AppliedModifiers | None, filename: str) -> None:
        """
        Prepares a ContextWrite with these information :
        - the model which is to be written
        - the protocol to be used
        - the filename
        - an object AppliedModifiers to work. It gives a list of
        FileModifiers to be ran, and for each one it can give
        a restricted list of entities (in the model), else all
        the model is considered
        """

    @overload
    def __init__(self, hgraph: nanoocp.Interface.Interface_HGraph | None, proto: nanoocp.Interface.Interface_Protocol | None, applieds: IFSelect_AppliedModifiers | None, filename: str) -> None:
        """Same as above but with an already computed Graph"""

    @overload
    def __init__(self, theOther: IFSelect_ContextWrite) -> None: ...

    def __iter__(self) -> IFSelect_ContextWrite:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.Standard.Standard_Transient:
        """Python addition: see __iter__."""

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model"""

    def Protocol(self) -> nanoocp.Interface.Interface_Protocol:
        """Returns the Protocol;"""

    def FileName(self) -> str:
        """Returns the File Name"""

    def AppliedModifiers(self) -> IFSelect_AppliedModifiers:
        """Returns the object AppliedModifiers"""

    def Graph(self) -> nanoocp.Interface.Interface_Graph:
        """
        Returns the Graph, either given when created, else created
        the first time it is queried
        """

    def NbModifiers(self) -> int:
        """Returns the count of recorded File Modifiers"""

    def SetModifier(self, numod: int) -> bool:
        """
        Sets active the File Modifier n0 <numod>
        Then, it prepares the list of entities to consider, if any
        Returns False if <numod> out of range
        """

    def FileModifier(self) -> IFSelect_GeneralModifier:
        """
        Returns the currently active File Modifier. Cast to be done
        Null if not properly set : must be test IsNull after casting
        """

    def IsForNone(self) -> bool:
        """Returns True if no modifier is currently set"""

    def IsForAll(self) -> bool:
        """
        Returns True if the current modifier is to be applied to
        the whole model. Else, a restricted list of selected entities
        is defined, it can be exploited by the File Modifier
        """

    def NbEntities(self) -> int:
        """Returns the total count of selected entities"""

    def Start(self) -> None:
        """
        Starts an iteration on selected items. It takes into account
        IsForAll/IsForNone, by really iterating on all selected items.
        """

    def More(self) -> bool:
        """Returns True until the iteration has finished"""

    def Next(self) -> None:
        """Advances the iteration"""

    def Value(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the current selected entity in the model"""

    def AddCheck(self, check: nanoocp.Interface.Interface_Check | None) -> None:
        """
        Adds a Check to the CheckList. If it is empty, nothing is done
        If it concerns an Entity from the Model (by SetEntity)
        to which another Check is attached, it is merged to it.
        Else, it is added or merged as to GlobalCheck.
        """

    def AddWarning(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """
        Adds a Warning Message for an Entity from the Model
        If <start> is not an Entity from the model (e.g. the
        model itself) this message is added to Global Check.
        """

    def AddFail(self, start: nanoocp.Standard.Standard_Transient | None, mess: str, orig: str = '') -> None:
        """
        Adds a Fail Message for an Entity from the Model
        If <start> is not an Entity from the model (e.g. the
        model itself) this message is added to Global Check.
        """

    @overload
    def CCheck(self, num: int = 0) -> nanoocp.Interface.Interface_Check:
        """
        Returns a Check given an Entity number (in the Model)
        by default a Global Check. Creates it the first time.
        It can then be acknowledged on the spot, in condition that the
        caller works by reference ("Interface_Check& check = ...")
        """

    @overload
    def CCheck(self, start: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check:
        """
        Returns a Check attached to an Entity from the Model
        It can then be acknowledged on the spot, in condition that the
        caller works by reference ("Interface_Check& check = ...")
        """

    def CheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """Returns the complete CheckList"""

class IFSelect_Dispatch(nanoocp.Standard.Standard_Transient):
    """
    This class allows to describe how a set of Entities has to be
    dispatched into resulting Packets : a Packet is a sub-set of
    the initial set of entities.

    Thus, it can generate zero, one, or more Packets according
    input set and criterium of dispatching. And it can let apart
    some entities : it is the Remainder, which can be recovered
    by a specific Selection (RemainderFromDispatch).

    Depending of sub-classes, a Dispatch can potentially generate
    a limited or not count of packet, and a remainder or none.

    The input set is read from a specified Selection, attached to
    the Dispatch : the Final Selection of the Dispatch. The input
    is the Unique Root Entities list of the Final Selection
    """

    def SetRootName(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Sets a Root Name as an HAsciiString
        To reset it, give a Null Handle (then, a ShareOut will have
        to define the Default Root Name)
        """

    def HasRootName(self) -> bool:
        """
        Returns True if a specific Root Name has been set
        (else, the Default Root Name has to be used)
        """

    def RootName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the Root Name for files produced by this dispatch
        It is empty if it has not been set or if it has been reset
        """

    def SetFinalSelection(self, sel: IFSelect_Selection | None) -> None:
        """Stores (or Changes) the Final Selection for a Dispatch"""

    def FinalSelection(self) -> IFSelect_Selection:
        """
        Returns the Final Selection of a Dispatch
        we 'd like : C++ : return const &
        """

    def Selections(self) -> IFSelect_SelectionIterator:
        """
        Returns the complete list of source Selections (starting
        from FinalSelection)
        """

    def CanHaveRemainder(self) -> bool:
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its
        criterium can let entities apart. It is a potential answer,
        remainder can be empty at run-time even if answer is True.
        (to attach a RemainderFromDispatch Selection is not allowed if
        answer is True).
        Default answer given here is False (can be redefined)
        """

    def LimitedMax(self, nbent: int) -> tuple[bool, int]:
        """
        Returns True if a Dispatch generates a count of Packets always
        less than or equal to a maximum value : it can be computed
        from the total count of Entities to be dispatched : <nbent>.
        If answer is False, no limited maximum is expected for account
        If answer is True, expected maximum is given in argument <max>
        Default answer given here is False (can be redefined)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which defines the way a Dispatch produces
        packets (which will become files) from its Input
        """

    def GetEntities(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Gets Unique Root Entities from the Final Selection, given an
        input Graph
        This the starting step for an Evaluation (Packets - Remainder)
        """

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Returns the list of produced Packets into argument <pack>.
        Each Packet corresponds to a Part, the Entities listed are the
        Roots given by the Selection. Input is given as a Graph.
        Thus, to create a file from a packet, it suffices to take the
        entities listed in a Part of Packets (that is, a Packet)
        without worrying about Shared entities
        This method can raise an Exception if data are not coherent
        """

    def Packeted(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of all Input Entities (see GetEntities) which
        are put in a Packet. That is, Entities listed in GetEntities
        but not in Remainder (see below). Input is given as a Graph.
        """

    def Remainder(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns Remainder which is a set of Entities. Can be empty.
        Default evaluation is empty (has to be redefined if
        CanHaveRemainder is redefined to return True).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_DispGlobal(IFSelect_Dispatch):
    """
    A DispGlobal gathers all the input Entities into only one
    global Packet
    """

    @overload
    def __init__(self) -> None:
        """Creates a DispGlobal"""

    @overload
    def __init__(self, theOther: IFSelect_DispGlobal) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "One File for all Input\""""

    def LimitedMax(self, nbent: int) -> tuple[bool, int]:
        """Returns True : maximum equates 1"""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Computes the list of produced Packets. It is made of only ONE
        Packet, which gets the RootResult from the Final Selection.
        Remark : the inherited exception raising is never activated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_DispPerCount(IFSelect_Dispatch):
    """
    A DispPerCount gathers all the input Entities into one or
    several Packets, each containing a defined count of Entity
    This count is a Parameter of the DispPerCount, given as an
    IntParam, thus allowing external control of its Value
    """

    @overload
    def __init__(self) -> None:
        """Creates a DispPerCount with no Count (default value 1)"""

    @overload
    def __init__(self, theOther: IFSelect_DispPerCount) -> None: ...

    def Count(self) -> IFSelect_IntParam:
        """Returns the Count Parameter used for splitting"""

    def SetCount(self, count: IFSelect_IntParam | None) -> None:
        """Sets a new Parameter for Count"""

    def CountValue(self) -> int:
        """
        Returns the effective value of the count parameter
        (if Count Parameter not Set or value not positive, returns 1)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "One File per <count> Input Entities\""""

    def LimitedMax(self, nbent: int) -> tuple[bool, int]:
        """Returns True, maximum count is given as <nbent>"""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Computes the list of produced Packets. It defines Packets in
        order to have at most <Count> Entities per Packet, Entities
        are given by RootResult from the Final Selection.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_DispPerFiles(IFSelect_Dispatch):
    """
    A DispPerFiles produces a determined count of Packets from the
    input Entities. It divides, as equally as possible, the input
    list into a count of files. This count is the parameter of the
    DispPerFiles. If the input list has less than this count, of
    course there will be one packet per input entity.
    This count is a Parameter of the DispPerFiles, given as an
    IntParam, thus allowing external control of its Value
    """

    @overload
    def __init__(self) -> None:
        """Creates a DispPerFiles with no Count (default value 1 file)"""

    @overload
    def __init__(self, theOther: IFSelect_DispPerFiles) -> None: ...

    def Count(self) -> IFSelect_IntParam:
        """Returns the Count Parameter used for splitting"""

    def SetCount(self, count: IFSelect_IntParam | None) -> None:
        """Sets a new Parameter for Count"""

    def CountValue(self) -> int:
        """
        Returns the effective value of the count parameter
        (if Count Parameter not Set or value not positive, returns 1)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "Maximum <count> Files\""""

    def LimitedMax(self, nbent: int) -> tuple[bool, int]:
        """Returns True, maximum count is given as CountValue"""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Computes the list of produced Packets. It defines Packets in
        order to have <Count> Packets, except if the input count of
        Entities is lower. Entities are given by RootResult from the
        Final Selection.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_DispPerOne(IFSelect_Dispatch):
    """
    A DispPerOne gathers all the input Entities into as many
    Packets as there Root Entities from the Final Selection,
    that is, one Packet per Entity
    """

    @overload
    def __init__(self) -> None:
        """Creates a DispPerOne"""

    @overload
    def __init__(self, theOther: IFSelect_DispPerOne) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "One File per Input Entity\""""

    def LimitedMax(self, nbent: int) -> tuple[bool, int]:
        """Returns True, maximum limit is given as <nbent>"""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Returns the list of produced Packets. It defines one Packet
        per Entity given by RootResult from the Final Selection.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_DispPerSignature(IFSelect_Dispatch):
    """
    A DispPerSignature sorts input Entities according to a
    Signature : it works with a SignCounter to do this.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a DispPerSignature with no SignCounter (by default,
        produces only one packet)
        """

    @overload
    def __init__(self, theOther: IFSelect_DispPerSignature) -> None: ...

    def SignCounter(self) -> IFSelect_SignCounter:
        """Returns the SignCounter used for splitting"""

    def SetSignCounter(self, sign: IFSelect_SignCounter | None) -> None:
        """
        Sets a SignCounter for sort
        Remark : it is set to record lists of entities, not only counts
        """

    def SignName(self) -> str:
        """
        Returns the name of the SignCounter, which characterises the
        sorting criterium for this Dispatch
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "One File per Signature <name>\""""

    def LimitedMax(self, nbent: int) -> tuple[bool, int]:
        """Returns True, maximum count is given as <nbent>"""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Computes the list of produced Packets. It defines Packets from
        the SignCounter, which sirts the input Entities per Signature
        (specific of the SignCounter).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_EditForm(nanoocp.Standard.Standard_Transient):
    """
    An EditForm is the way to apply an Editor on an Entity or on
    the Model
    It gives read-only or read-write access, with or without undo

    It can be complete (all the values of the Editor are present)
    or partial (a sub-list of these value are present)
    Anyway, all references to Number (argument <num>) refer to
    Number of Value for the Editor
    While references to Rank are for rank in the EditForm, which
    may differ if it is not Complete
    Two methods give the correspondence between this Number and
    the Rank in the EditForm : RankFromNumber and NumberFromRank
    """

    @overload
    def __init__(self, editor: IFSelect_Editor | None, readonly: bool, undoable: bool, label: str = '') -> None:
        """
        Creates a complete EditForm from an Editor
        A specific Label can be given
        """

    @overload
    def __init__(self, editor: IFSelect_Editor | None, nums: nanoocp.NCollection.NCollection_Sequence[int], readonly: bool, undoable: bool, label: str = '') -> None:
        """
        Creates an extracted EditForm from an Editor, limited to
        the values identified in <nums>
        A specific Label can be given
        """

    @overload
    def __init__(self, theOther: IFSelect_EditForm) -> None: ...

    def EditKeepStatus(self) -> bool:
        """
        Returns and may change the keep status on modif
        It starts as False
        If it is True, Apply does not clear modification status
        and the EditForm can be loaded again, modified value remain
        and may be applied again
        Remark that ApplyData does not clear the modification status,
        a call to ClearEdit does
        """

    def SetEditKeepStatus(self, theValue: bool) -> None:
        """
        Python addition: sets the value EditKeepStatus() returns by reference in C++.
        """

    def Label(self) -> str: ...

    def IsLoaded(self) -> bool:
        """Tells if the EditForm is loaded now"""

    def ClearData(self) -> None: ...

    def SetData(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None: ...

    def SetEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None: ...

    def Entity(self) -> nanoocp.Standard.Standard_Transient: ...

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel: ...

    def Editor(self) -> IFSelect_Editor: ...

    def IsComplete(self) -> bool:
        """Tells if an EditForm is complete or is an extract from Editor"""

    def NbValues(self, editable: bool) -> int:
        """
        Returns the count of values
        <editable> True : count of editable values, i.e.
        For a complete EditForm, it is given by the Editor
        Else, it is the length of the extraction map
        <editable> False : all the values from the Editor
        """

    def NumberFromRank(self, rank: int) -> int:
        """
        Returns the Value Number in the Editor from a given Rank in
        the EditForm
        For a complete EditForm, both are equal
        Else, it is given by the extraction map
        Returns 0 if <rank> exceeds the count of editable values,
        """

    def RankFromNumber(self, number: int) -> int:
        """
        Returns the Rank in the EditForm from a given Number of Value
        for the Editor
        For a complete EditForm, both are equal
        Else, it is given by the extraction map
        Returns 0 if <number> is not forecast to be edited, or is
        out of range
        """

    def NameNumber(self, name: str) -> int:
        """
        Returns the Value Number in the Editor for a given Name
        i.e. the true ValueNumber which can be used in various methods
        of EditForm
        If it is not complete, for a recorded (in the Editor) but
        non-loaded name, returns negative value (- number)
        """

    def NameRank(self, name: str) -> int:
        """
        Returns the Rank of Value in the EditForm for a given Name
        i.e. if it is not complete, for a recorded (in the Editor) but
        non-loaded name, returns 0
        """

    def LoadDefault(self) -> None:
        """
        For a read-write undoable EditForm, loads original values
        from defaults stored in the Editor
        """

    @overload
    def LoadData(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Loads modifications to data
        Default uses Editor. Can be redefined
        Remark that <ent> and/or <model> may be null, according to the
        kind of Editor. Shortcuts are available for these cases, but
        they finally call LoadData (hence, just ignore non-used args)
        """

    @overload
    def LoadData(self) -> bool:
        """
        Shortcut when both <ent> and <model> are not used
        (when the Editor works on fully static or global data)
        """

    def LoadEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Shortcut for LoadData when <model> is not used"""

    def LoadModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Shortcut for LoadData when only the model is concerned"""

    def ListEditor(self, num: int) -> IFSelect_ListEditor:
        """
        Returns a ListEditor to edit the parameter <num> of the
        EditForm, if it is a List
        The Editor created it (by ListEditor) then loads it (by
        ListValue)
        For a single parameter, returns a Null Handle ...
        """

    def LoadValue(self, num: int, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Loads an original value (single). Called by the Editor only"""

    def LoadList(self, num: int, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """Loads an original value as a list. Called by the Editor only"""

    def OriginalValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        From an edited value, returns its ... value (original one)
        Null means that this value is not defined
        <num> is for the EditForm, not the Editor
        It is for a single parameter. For a list, gives a Null Handle
        """

    def OriginalList(self, num: int) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns an original value, as a list
        <num> is for the EditForm, not the Editor
        For a single parameter, gives a Null Handle
        """

    def EditedValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the Edited (i.e. Modified) Value (string for single)
        <num> reports to the EditForm
        If IsModified is False, returns OriginalValue
        Null with IsModified True : means that this value is not
        defined or has been removed
        It is for a single parameter. For a list, gives a Null Handle
        """

    def EditedList(self, num: int) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the Edited Value as a list
        If IsModified is False, returns OriginalValue
        Null with IsModified True : means that this value is not
        defined or has been removed
        For a single parameter, gives a Null Handle
        """

    def IsModified(self, num: int) -> bool:
        """
        Tells if a Value (of the EditForm) is modified (directly or
        through touching by Update)
        """

    def IsTouched(self, num: int) -> bool:
        """
        Tells if a Value (of the EditForm) has been touched, i.e.
        not modified directly but by the modification of another one
        (by method Update from the Editor)
        """

    def Modify(self, num: int, newval: nanoocp.TCollection.TCollection_HAsciiString | None, enforce: bool = False) -> bool:
        """
        Gives a new value for the item <num> of the EditForm, if
        it is a single parameter (for a list, just returns False)
        Null means to Remove it
        <enforce> True to overpass Protected or Computed Access Mode
        Calls the method Update from the Editor, which can touch other
        parameters (see NbTouched)
        Returns True if well recorded, False if this value is not
        allowed
        Warning : Does not apply immediately : will be applied by the method
        Apply
        """

    def ModifyList(self, num: int, edited: IFSelect_ListEditor | None, enforce: bool = False) -> bool:
        """
        Changes the value of an item of the EditForm, if it is a List
        (else, just returns False)
        The ListEditor contains the edited values of the list
        If no edition was recorded, just returns False
        Calls the method Update from the Editor, which can touch other
        parameters (see NbTouched)
        Returns True if well recorded, False if this value is not
        allowed
        Warning : Does not apply immediately : will be applied by the method
        Apply
        """

    def ModifyListValue(self, num: int, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None, enforce: bool = False) -> bool:
        """
        As ModifyList but the new value is given as such
        Creates a ListEditor, Loads it, then calls ModifyList
        """

    def Touch(self, num: int, newval: nanoocp.TCollection.TCollection_HAsciiString | None) -> bool:
        """
        Gives a new value computed by the Editor, if another parameter
        commands the value of <num>
        It is generally the case for a Computed Parameter for instance
        Increments the counter of touched parameters
        Warning : it gives no protection for ReadOnly etc... while it is the
        internal way of touching parameters
        Does not work (returns False) if <num> is for a list
        """

    def TouchList(self, num: int, newlist: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None) -> bool:
        """
        Acts as Touch but for a list
        Does not work (returns False) if <num> is for a single param
        """

    def ClearEdit(self, num: int = 0) -> None:
        """
        Clears modification status : by default all, or one by its
        numbers (in the Editor)
        """

    def PrintDefs(self) -> str:
        """Prints Definitions, relative to the Editor"""

    def PrintValues(self, what: int, names: bool, alsolist: bool = False) -> str:
        """
        Prints Values, according to what and alsolist
        <names> True : prints Long Names; False : prints Short Names
        <what> < 0 : prints Original Values (+ flag Modified)
        <what> > 0 : prints Final Values (+flag Modified)
        <what> = 0 : prints Modified Values (Original + Edited)
        <alsolist> False (D) : lists are printed only as their count
        <alsolist> True : lists are printed for all their items
        """

    def Apply(self) -> bool:
        """
        Applies modifications to own data
        Calls ApplyData then Clears Status according EditKeepStatus
        """

    def Recognize(self) -> bool:
        """
        Tells if this EditForm can work with its Editor and its actual
        Data (Entity and Model)
        Default uses Editor. Can be redefined
        """

    def ApplyData(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Applies modifications to data
        Default uses Editor. Can be redefined
        """

    def Undo(self) -> bool:
        """
        For an undoable EditForm, Applies ... origibal values !
        and clears modified ones
        Can be run only once
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_Editor(nanoocp.Standard.Standard_Transient):
    """
    An Editor defines a set of values and a way to edit them, on
    an entity or on the model (e.g. on its header)

    Each Value is controlled by a TypedValue, with a number (it is
    an Integer) and a name under two forms (complete and short)
    and an edit mode
    """

    def SetValue(self, num: int, typval: nanoocp.Interface.Interface_TypedValue | None, shortname: str = '', accessmode: IFSelect_EditValue = IFSelect_EditValue.IFSelect_Editable) -> None:
        """
        Sets a Typed Value for a given ident and short name, with an
        Edit Mode
        """

    def SetList(self, num: int, max: int = 0) -> None:
        """
        Sets a parameter to be a List
        max < 0 : not for a list (set when starting)
        max = 0 : list with no length limit (default for SetList)
        max > 0 : list limited to <max> items
        """

    def NbValues(self) -> int:
        """Returns the count of Typed Values"""

    def TypedValue(self, num: int) -> nanoocp.Interface.Interface_TypedValue:
        """Returns a Typed Value from its ident"""

    def IsList(self, num: int) -> bool:
        """Tells if a parameter is a list"""

    def MaxList(self, num: int) -> int:
        """
        Returns max length allowed for a list
        = 0 means : list with no limit
        < 0 means : not a list
        """

    def Name(self, num: int, isshort: bool = False) -> str:
        """
        Returns the name of a Value (complete or short) from its ident
        Short Name can be empty
        """

    def EditMode(self, num: int) -> IFSelect_EditValue:
        """Returns the edit mode of a Value"""

    def NameNumber(self, name: str) -> int:
        """
        Returns the number (ident) of a Value, from its name, short or
        complete. If not found, returns 0
        """

    def PrintNames(self) -> str: ...

    def PrintDefs(self, labels: bool = False) -> str: ...

    def MaxNameLength(self, what: int) -> int:
        """
        Returns the MaxLength of, according to what :
        <what> = -1 : length of short names
        <what> =  0 : length of complete names
        <what> =  1 : length of values labels
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the specific label"""

    def Form(self, readonly: bool, undoable: bool = True) -> IFSelect_EditForm:
        """
        Builds and Returns an EditForm, empty (no data yet)
        Can be redefined to return a specific type of EditForm
        """

    def Recognize(self, form: IFSelect_EditForm | None) -> bool:
        """
        Tells if this Editor can work on this EditForm and its content
        (model, entity ?)
        """

    def StringValue(self, form: IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of an EditForm, for a given item
        (if not a list. for a list, a Null String may be returned)
        """

    def ListEditor(self, num: int) -> IFSelect_ListEditor:
        """
        Returns a ListEditor for a parameter which is a List
        Default returns a basic ListEditor for a List, a Null Handle
        if <num> is not for a List. Can be redefined
        """

    def ListValue(self, form: IFSelect_EditForm | None, num: int) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the value of an EditForm as a List, for a given item
        If not a list, a Null Handle should be returned
        Default returns a Null Handle, because many Editors have
        no list to edit. To be redefined as required
        """

    def Load(self, form: IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Loads original values from some data, to an EditForm
        Remark: <ent> may be Null, this means all <model> is concerned
        Also <model> may be Null, if no context applies for <ent>
        And both <ent> and <model> may be Null, for a full static
        editor
        """

    def Update(self, form: IFSelect_EditForm | None, num: int, newval: nanoocp.TCollection.TCollection_HAsciiString | None, enforce: bool) -> bool:
        """
        Updates the EditForm when a parameter is modified
        I.E.  default does nothing, can be redefined, as follows :
        Returns True when done (even if does nothing), False in case
        of refuse (for instance, if the new value is not suitable)
        <num> is the rank of the parameter for the EDITOR itself
        <enforce> True means that protected parameters can be touched

        If a parameter commands the value of other ones, when it is
        modified, it is necessary to touch them by Touch from EditForm
        """

    def UpdateList(self, form: IFSelect_EditForm | None, num: int, newlist: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None, enforce: bool) -> bool:
        """Acts as Update, but when the value is a list"""

    def Apply(self, form: IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Applies modified values of the EditForm with some data
        Remark: <ent> may be Null, this means all <model> is concerned
        Also <model> may be Null, if no context applies for <ent>
        And both <ent> and <model> may be Null, for a full static
        editor
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_Functions:
    """
    Functions gives access to all the actions which can be
    commanded with the resources provided by IFSelect : especially
    WorkSession and various types of Selections and Dispatches

    It works by adding functions by method Init
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IFSelect_Functions) -> None: ...

    @staticmethod
    def GiveEntity(WS: IFSelect_WorkSession | None, name: str = '') -> nanoocp.Standard.Standard_Transient:
        """
        Takes the name of an entity, either as argument,
        or (if <name> is empty) on keyboard, and returns the entity
        name can be a label or a number (in alphanumeric),
        it is searched by NumberFromLabel from WorkSession.
        If <name> doesn't match en entity, a Null Handle is returned
        """

    @staticmethod
    def GiveEntityNumber(WS: IFSelect_WorkSession | None, name: str = '') -> int:
        """
        Same as GetEntity, but returns the number in the model of the
        entity. Returns 0 for null handle
        """

    @staticmethod
    def GiveList(WS: IFSelect_WorkSession | None, first: str = '', second: str = '') -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Computes a List of entities from a WorkSession and two idents,
        first and second, as follows :
        if <first> is a Number or Label of an entity : this entity
        if <first> is the name of a Selection in <WS>, and <second>
        not defined, the standard result of this Selection
        if <first> is for a Selection and <second> is defined, the
        standard result of this selection from the list computed
        with <second> (an entity or a selection)
        If <second> is erroneous, it is ignored
        """

    @staticmethod
    def GiveDispatch(WS: IFSelect_WorkSession | None, name: str, mode: bool = True) -> IFSelect_Dispatch:
        """
        Evaluates and returns a Dispatch, from data of a WorkSession
        if <mode> is False, searches for exact name of Dispatch in WS
        Else (D), allows a parameter between brackets :
        ex.: dispatch_name(parameter)
        The parameter can be: an integer for DispPerCount or DispPerFiles
        or the name of a Signature for DispPerSignature
        Returns Null Handle if not found not well evaluated
        """

    @staticmethod
    def Init() -> None:
        """Defines and loads all basic functions (as ActFunc)"""

class IFSelect_SignCounter(IFSelect_SignatureList):
    """
    SignCounter gives the frame to count signatures associated
    with entities, deducted from them. Ex.: their Dynamic Type.

    It can sort a set of Entities according a signature, i.e. :
    - list of different values found for this Signature
    - for each one, count and list of entities
    Results are returned as a SignatureList, which can be queried
    on the count (list of strings, count per signature, or list of
    entities per signature)

    A SignCounter can be filled, either directly from lists, or
    from the result of a Selection : hence, its content can be
    automatically recomputed as desired

    SignCounter works by using a Signature in its method AddSign

    Methods can be redefined to, either
    - directly compute the value without a Signature
    - compute the value in the context of a Graph
    """

    @overload
    def __init__(self, withmap: bool = True, withlist: bool = False) -> None:
        """
        Creates a SignCounter, without proper Signature
        If <withmap> is True (default), added entities are counted
        only if they are not yet recorded in the map
        Map control can be set off if the input guarantees uniqueness of data
        <withlist> is transmitted to SignatureList (option to list
        entities, not only to count them).
        """

    @overload
    def __init__(self, matcher: IFSelect_Signature | None, withmap: bool = True, withlist: bool = False) -> None:
        """
        Creates a SignCounter, with a predefined Signature
        Other arguments as for Create without Signature.
        """

    @overload
    def __init__(self, theOther: IFSelect_SignCounter) -> None: ...

    def Signature(self) -> IFSelect_Signature:
        """Returns the Signature used to count entities. It can be null."""

    def SetMap(self, withmap: bool) -> None:
        """
        Changes the control status. The map is not cleared, simply
        its use changes
        """

    def AddEntity(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Adds an entity by considering its signature, which is given by
        call to method AddSign
        Returns True if added, False if already in the map (and
        map control status set)
        """

    def AddSign(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Adds an entity (already filtered by Map) with its signature.
        This signature can be computed with the containing model.
        Its value is provided by the object Signature given at start,
        if no Signature is defined, it does nothing.

        Can be redefined (in this case, see also Sign)
        """

    def AddList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Adds a list of entities by adding each of the items"""

    def AddWithGraph(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, graph: nanoocp.Interface.Interface_Graph) -> None:
        """
        Adds a list of entities in the context given by the graph
        Default just call basic AddList
        Can be redefined to get a signature computed with the graph
        """

    def AddModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Adds all the entities contained in a Model"""

    def AddFromSelection(self, sel: IFSelect_Selection | None, G: nanoocp.Interface.Interface_Graph) -> None:
        """
        Adds the result determined by a Selection from a Graph
        Remark : does not impact at all data from SetSelection & Co
        """

    def SetSelection(self, sel: IFSelect_Selection | None) -> None:
        """
        Sets a Selection as input : this causes content to be cleared
        then the Selection to be ready to compute (but not immediately)
        """

    def Selection(self) -> IFSelect_Selection:
        """Returns the selection, or a null Handle"""

    def SetSelMode(self, selmode: int) -> None:
        """
        Changes the mode of working with the selection :
        -1 just clears optimisation data and nothing else
        0 clears it
        1 inhibits it for computing (but no clearing)
        2 sets it active for computing
        Default at creation is 0, after SetSelection (not null) is 2
        """

    def SelMode(self) -> int:
        """Returns the mode of working with the selection"""

    def ComputeSelected(self, G: nanoocp.Interface.Interface_Graph, forced: bool = False) -> bool:
        """
        Computes from the selection result, if selection is active
        (mode 2). If selection is not defined (mode 0) or is inhibited
        (mode 1) does nothing.
        Returns True if computation is done (or optimised), False else
        This method is called by ComputeCounter from WorkSession

        If <forced> is True, recomputes systematically
        Else (D), if the counter was not cleared and if the former
        computed result started from the same total size of Graph and
        same count of selected entities : computation is not redone
        unless <forced> is given as True
        """

    def Sign(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Determines and returns the value of the signature for an
        entity as an HAsciiString. This method works exactly as
        AddSign, which is optimized

        Can be redefined, accorded with AddSign
        """

    def ComputedSign(self, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph) -> str:
        """
        Applies AddWithGraph on one entity, and returns the Signature
        Value which has been recorded
        To do this, Add is called with SignOnly Mode True during the
        call, the returned value is LastValue
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_GraphCounter(IFSelect_SignCounter):
    """
    A GraphCounter computes values to be sorted with the help of
    a Graph. I.E. not from a Signature

    The default GraphCounter works with an Applied Selection (a
    SelectDeduct), the value is the count of selected entities
    from each input entities)
    """

    @overload
    def __init__(self, withmap: bool = True, withlist: bool = False) -> None:
        """Creates a GraphCounter, without applied selection"""

    @overload
    def __init__(self, theOther: IFSelect_GraphCounter) -> None: ...

    def Applied(self) -> IFSelect_SelectDeduct:
        """Returns the applied selection"""

    def SetApplied(self, sel: IFSelect_SelectDeduct | None) -> None:
        """Sets a new applied selection"""

    def AddWithGraph(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, graph: nanoocp.Interface.Interface_Graph) -> None:
        """
        Adds a list of entities in the context given by the graph
        Default takes the count of entities selected by the applied
        selection, when it is given each entity of the list
        Can be redefined
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_IntParam(nanoocp.Standard.Standard_Transient):
    """
    This class simply allows to access an Integer value through a
    Handle, as a String can be (by using HString).
    Hence, this value can be accessed : read and modified, without
    passing through the specific object which detains it. Thus,
    parameters of a Selection or a Dispatch (according its type)
    can be controlled directly from the ShareOut which contains them

    Additionally, an IntParam can be bound to a Static.
    Remember that for a String, binding is immediate, because the
    string value of a Static is a HAsciiString, it then suffices
    to get its Handle.
    For an Integer, an IntParam can designate (by its name) a
    Static : each time its value is required or set, the Static
    is acknowledged
    """

    @overload
    def __init__(self) -> None:
        """Creates an IntParam. Initial value is set to zer"""

    @overload
    def __init__(self, theOther: IFSelect_IntParam) -> None: ...

    def SetStaticName(self, statname: str) -> None:
        """
        Commands this IntParam to be bound to a Static
        Hence, Value will return the value if this Static if it is set
        Else, Value works on the locally stored value
        SetValue also will set the value of the Static
        This works only for a present static of type integer or enum
        Else, it is ignored

        If <statname> is empty, disconnects the IntParam from Static
        """

    def Value(self) -> int:
        """
        Reads Integer Value of the IntParam. If a StaticName is
        defined and the Static is set, looks in priority the value
        of the static
        """

    def SetValue(self, val: int) -> None:
        """
        Sets a new Integer Value for the IntParam. If a StaticName is
        defined and the Static is set, also sets the value of the static
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ListEditor(nanoocp.Standard.Standard_Transient):
    """
    A ListEditor is an auxiliary operator for Editor/EditForm
    I.E. it works on parameter values expressed as strings

    For a parameter which is a list, it may not be edited in once
    by just setting a new value (as a string)

    Firstly, a list can be long (and tedious to be accessed flat)
    then requires a better way of accessing

    Moreover, not only its VALUES may be changed (SetValue), but
    also its LENGTH : items may be added or removed ...

    Hence, the way of editing a parameter as a list is :
    - edit it separately, with the help of a ListEditor
    - it remains possible to prepare a new list of values apart
    - then give the new list in once to the EditForm

    An EditList is produced by the Editor, with a basic definition
    This definition (brought by this class) can be redefined
    Hence the Editor may produce a specific ListEditor as needed
    """

    @overload
    def __init__(self) -> None:
        """Creates a ListEditor with absolutely no constraint"""

    @overload
    def __init__(self, def_: nanoocp.Interface.Interface_TypedValue | None, max: int = 0) -> None:
        """
        Creates a ListEditor, for which items of the list to edit are
        defined by <def>, and <max> describes max length :
        0 (D) means no limit
        value > 0 means : no more the <max> items are allowed
        """

    @overload
    def __init__(self, theOther: IFSelect_ListEditor) -> None: ...

    def LoadModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Loads a Model. It is used to check items of type Entity(Ident)"""

    def LoadValues(self, vals: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        Loads the original values for the list.
        Remark : If its length is more then MaxLength, editions remain allowed, except Add
        """

    def SetTouched(self) -> None:
        """Declares this ListEditor to have been touched (whatever action)"""

    def ClearEdit(self) -> None:
        """Clears all editions already recorded"""

    def LoadEdited(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None) -> bool:
        """
        Loads a new list to replace the older one, in once !
        By default (can be redefined) checks the length of the list
        and the value of each item according to the def
        Items are all recorded as Modified

        If no def has been given at creation time, no check is done
        Returns True when done, False if checks have failed ... a
        specialisation may also lock it by returning always False ...
        """

    def SetValue(self, num: int, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> bool:
        """
        Sets a new value for the item <num> (in edited list)
        <val> may be a Null Handle, then the value will be cleared but
        not removed
        Returns True when done. False if <num> is out of range or if
        <val> does not satisfy the definition
        """

    def AddValue(self, val: nanoocp.TCollection.TCollection_HAsciiString | None, atnum: int = 0) -> bool:
        """
        Adds a new item. By default appends (at the end of the list)
        Can insert before a given rank <num>, if positive
        Returns True when done. False if MaxLength may be overpassed
        or if <val> does not satisfy the definition
        """

    def Remove(self, num: int = 0, howmany: int = 1) -> bool:
        """
        Removes items from the list
        By default removes one item. Else, count given by <howmany>
        Remove from rank <num> included. By default, from the end
        Returns True when done, False (and does not work) if case of
        out of range of if <howmany> is greater than current length
        """

    def OriginalValues(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns the value from which the edition started"""

    def EditedValues(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns the result of the edition"""

    def NbValues(self, edited: bool = True) -> int:
        """Returns count of values, edited (D) or original"""

    def Value(self, num: int, edited: bool = True) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a value given its rank. Edited (D) or Original
        A Null String means the value is cleared but not removed
        """

    def IsChanged(self, num: int) -> bool:
        """
        Tells if a value (in edited list) has been changed, i.e.
        either modified-value, or added
        """

    def IsModified(self, num: int) -> bool:
        """
        Tells if a value (in edited list) has been modified-value
        (not added)
        """

    def IsAdded(self, num: int) -> bool:
        """Tells if a value (in edited list) has been added (new one)"""

    def IsTouched(self) -> bool:
        """
        Tells if at least one edition (SetValue-AddValue-Remove) has
        been recorded
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ModelCopier(nanoocp.Standard.Standard_Transient):
    """
    This class performs the Copy operations involved by the
    description of a ShareOut (evaluated by a ShareOutResult)
    plus, if there are, the Modifications on the results, with
    the help of Modifiers. Each Modifier can work on one or more
    resulting packets, according to its criteria : it operates on
    a Model once copied and filled with the content of the packet.

    Modifiers can be :
    - Model Modifiers, inheriting from the specific class Modifier
    able to run on the content of a Model (header or entities),
    activated by the ModelCopier itself
    - File Modifiers, inheriting directly from GeneralModifier,
    intended to be activated under the control of a WorkLibrary,
    once the Model has been produced (i.e. to act on output
    format, or other specific file features)

    The Copy operations can be :
    - immediately put to files : for each packet, a Model is
    created and filled, then the file is output, at that's all
    - memorized : for each packet, a Model is created and filled,
    it is memorized with the corresponding file name.
    it is possible to query the result of memorization (list of
    produced Models and their file names)
    -> it is also possible to send it into the files :
    once files are written, the result is cleared

    In addition, a list of really written files is managed :
    A first call to BeginSentFiles clears the list and commands,
    either to begin a new list, or to stop recording it. A call
    to SentFiles returns the list (if recording has been required)
    This list allows to globally exploit the set of produced files

    Remark : For operations which concern specific Entities, see
    also in package IFAdapt : a sub-class of ModelCopier allows
    to work with EntityModifier, in addition to Modifier itself
    which still applies to a whole copied Model.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty ModelCopier"""

    @overload
    def __init__(self, theOther: IFSelect_ModelCopier) -> None: ...

    def SetShareOut(self, sho: IFSelect_ShareOut | None) -> None:
        """Sets the ShareOut, which is used to define Modifiers to apply"""

    def ClearResult(self) -> None:
        """Clears the list of produced Models"""

    def AddFile(self, filename: nanoocp.TCollection.TCollection_AsciiString, content: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Records a new File to be sent, as a couple
        (Name as AsciiString, Content as InterfaceModel)
        Returns True if Done, False if <filename> is already attached
        to another File
        """

    def NameFile(self, num: int, filename: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Changes the Name attached to a File which was formerly defined
        by a call to AddFile
        Returns True if Done, False else : if <num> out of range or if
        the new <filename> is already attached to another File
        Remark : Giving an empty File Name is equivalent to ClearFile
        """

    def ClearFile(self, num: int) -> bool:
        """
        Clears the Name attached to a File which was formerly defined
        by a call to AddFile. This Clearing can be undone by a call to
        NameFile (with same <num>)
        Returns True if Done, False else : if <num> is out of range
        """

    def SetAppliedModifiers(self, num: int, applied: IFSelect_AppliedModifiers | None) -> bool:
        """Sets a list of File Modifiers to be applied on a file"""

    def ClearAppliedModifiers(self, num: int) -> bool:
        """Clears the list of File Modifiers to be applied on a file"""

    def Copy(self, eval: IFSelect_ShareOutResult, WL: IFSelect_WorkLibrary | None, protocol: nanoocp.Interface.Interface_Protocol | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Performs the Copy Operations, which include the Modifications
        defined by the list of Modifiers. Memorizes the result, as a
        list of InterfaceModels with the corresponding FileNames
        They can then be sent, by the method Send, or queried
        Copy calls internal method Copying.
        Returns the produced CheckList
        """

    def SendCopied(self, WL: IFSelect_WorkLibrary | None, protocol: nanoocp.Interface.Interface_Protocol | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Sends the formerly defined results (see method Copy) to files,
        then clears it
        Remark : A Null File Name cause file to be not produced
        """

    def Send(self, eval: IFSelect_ShareOutResult, WL: IFSelect_WorkLibrary | None, protocol: nanoocp.Interface.Interface_Protocol | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Performs the Copy Operations (which include the Modifications)
        and Sends the result on files, without memorizing it.
        (the memorized result is ignored : neither queried not filled)
        """

    def SendAll(self, filename: str, G: nanoocp.Interface.Interface_Graph, WL: IFSelect_WorkLibrary | None, protocol: nanoocp.Interface.Interface_Protocol | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Sends a model (defined in <G>) into one file, without managing
        remaining data, already sent files, etc. Applies the Model and
        File Modifiers.
        Returns True if well done, False else
        """

    def SendSelected(self, filename: str, G: nanoocp.Interface.Interface_Graph, WL: IFSelect_WorkLibrary | None, protocol: nanoocp.Interface.Interface_Protocol | None, iter: nanoocp.Interface.Interface_EntityIterator) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Sends a part of a model into one file. Model is gotten from
        <G>, the part is defined in <iter>.
        Remaining data are managed and can be later be worked on.
        Returns True if well done, False else
        """

    def CopiedRemaining(self, G: nanoocp.Interface.Interface_Graph, WL: IFSelect_WorkLibrary | None, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Produces a Model copied from the Remaining List as <newmod>
        <newmod> is a Null Handle if this list is empty
        <WL> performs the copy by using <TC>
        <TC> is assumed to have been defined with the starting model
        same as defined by <G>.
        Produces a model copied from the remaining list.
        @param[in] G the interface graph
        @param[in] WL the work library performing the copy
        @param[in,out] TC the copy tool
        @return the new model with remaining data, or null handle if empty
        """

    def CopiedRemaining__Interface_InterfaceModel(self, G: nanoocp.Interface.Interface_Graph, WL: IFSelect_WorkLibrary | None, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        CopiedRemaining__Interface_InterfaceModel: the C++ overload CopiedRemaining(const Interface_Graph &, const occ::handle<IFSelect_WorkLibrary> &, Interface_CopyTool &, occ::handle<Interface_InterfaceModel> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use CopiedRemaining() returning handle by value instead

        @deprecated Use CopiedRemaining() returning handle by value instead.
        """

    def SetRemaining(self, CG: nanoocp.Interface.Interface_Graph) -> bool:
        """
        Updates Graph status for remaining data, for each entity :
        - Entities just Sent to file or Copied (by CopiedRemaining)
        have their status set to 1
        - the other keep their former status (1 for Send/Copied,
        0 for Remaining)
        These status are computed by Copying/Sending/CopiedRemaining
        Then, SetRemaining updates graph status, and mustr be called
        just after one of these method has been called
        Returns True if done, False if remaining info if not in phase
        which the Graph (not same counts of items)
        """

    def NbFiles(self) -> int:
        """
        Returns the count of Files produced, i.e. the count of Models
        memorized (produced by the mmethod Copy) with their file names
        """

    def FileName(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the File Name for a file given its rank
        It is empty after a call to ClearFile on same <num>
        """

    def FileModel(self, num: int) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Returns the content of a file before sending, under the form
        of an InterfaceModel, given its rank
        """

    def AppliedModifiers(self, num: int) -> IFSelect_AppliedModifiers:
        """
        Returns the list of File Modifiers to be applied on a file
        when it will be sent, as computed by CopiedModel :
        If it is a null handle, no File Modifier has to be applied.
        """

    def BeginSentFiles(self, sho: IFSelect_ShareOut | None, record: bool) -> None:
        """
        Begins a sequence of recording the really sent files
        <sho> : the default file numbering is cleared
        If <record> is False, clears the list and stops recording
        If <record> is True, clears the list and commands recording
        Creation time corresponds to "stop recording\"
        """

    def AddSentFile(self, filename: str) -> None:
        """
        Adds the name of a just sent file, if BeginSentFiles
        has commanded recording; else does nothing
        It is called by methods SendCopied Sending
        """

    def SentFiles(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of recorded names of sent files. Can be empty
        (if no file has been sent). Returns a Null Handle if
        BeginSentFiles has stopped recording.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_Modifier(IFSelect_GeneralModifier):
    """
    This class gives a frame for Actions which can work globally
    on a File once completely defined (i.e. afterwards)

    Remark : if no Selection is set as criterium, the Modifier is
    set to work and should consider all the content of the Model
    produced.
    """

    def Perform(self, ctx: IFSelect_ContextModif, target: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        This deferred method defines the action specific to each class
        of Modifier. It is called by a ModelCopier, once the Model
        generated and filled. ModelCopier has already checked the
        criteria (Dispatch, Model Rank, Selection) before calling it.

        <ctx> detains information about original data and selection.
        The result of copying, on which modifications are to be done,
        is <target>.
        <TC> allows to run additional copies as required

        In case of Error, use methods CCheck from the ContextModif
        to acknowledge an entity Check or a Global Check with messages
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ModifEditForm(IFSelect_Modifier):
    """This modifier applies an EditForm on the entities selected"""

    @overload
    def __init__(self, editform: IFSelect_EditForm | None) -> None:
        """Creates a ModifEditForm. It may not change the graph"""

    @overload
    def __init__(self, theOther: IFSelect_ModifEditForm) -> None: ...

    def EditForm(self) -> IFSelect_EditForm:
        """Returns the EditForm"""

    def Perform(self, ctx: IFSelect_ContextModif, target: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Acts by applying an EditForm to entities, selected or all model"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Label as "Apply EditForm <+ label of EditForm>\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ModifReorder(IFSelect_Modifier):
    """
    This modifier reorders a whole model from its roots, i.e.
    according to <rootlast> status, it considers each of its
    roots, then it orders all its shared entities at any level,
    the result begins by the lower level entities ... ends by
    the roots.
    """

    @overload
    def __init__(self, rootlast: bool = True) -> None:
        """
        Creates a ModifReorder. It may change the graph (it does !)
        If <rootlast> is True (D), roots are set at the end of packets
        Else, they are set at beginning (as done by AddWithRefs)
        """

    @overload
    def __init__(self, theOther: IFSelect_ModifReorder) -> None: ...

    def Perform(self, ctx: IFSelect_ContextModif, target: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Acts by computing orders (by method All from ShareTool) then
        forcing them in the model. Remark that selection is ignored :
        ALL the model is processed in once
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Label as "Reorder, Roots (last or first)\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_PacketList(nanoocp.Standard.Standard_Transient):
    """
    This class gives a simple way to return then consult a
    list of packets, determined from the content of a Model,
    by various criteria.

    It allows to describe several lists with entities from a
    given model, possibly more than one list knowing every entity,
    and to determine the remaining list (entities in no lists) and
    the duplications (with their count).
    """

    @overload
    def __init__(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Creates a PackList, empty, ready to receive entities from a
        given Model
        """

    @overload
    def __init__(self, theOther: IFSelect_PacketList) -> None: ...

    def SetName(self, name: str) -> None:
        """
        Sets a name to a packet list : this makes easier a general
        routine to print it. Default is "Packets\"
        """

    def Name(self) -> str:
        """Returns the recorded name for a packet list"""

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model of reference"""

    def AddPacket(self) -> None:
        """
        Declares a new Packet, ready to be filled
        The entities to be added will be added to this Packet
        """

    def Add(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds an entity from the Model into the current packet for Add"""

    def AddList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Adds an list of entities into the current packet for Add"""

    def NbPackets(self) -> int:
        """Returns the count of non-empty packets"""

    def NbEntities(self, numpack: int) -> int:
        """Returns the count of entities in a Packet given its rank, or 0"""

    def Entities(self, numpack: int) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the content of a Packet given its rank
        Null Handle if <numpack> is out of range
        """

    def HighestDuplicationCount(self) -> int:
        """
        Returns the highest number of packets which know a same entity
        For no duplication, should be one
        """

    def NbDuplicated(self, count: int, andmore: bool) -> int:
        """
        Returns the count of entities duplicated :
        <count> times, if <andmore> is False, or
        <count> or more times, if <andmore> is True
        See Duplicated for more details
        """

    def Duplicated(self, count: int, andmore: bool) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns a list of entities duplicated :
        <count> times, if <andmore> is False, or
        <count> or more times, if <andmore> is True
        Hence, count=2 & andmore=True gives all duplicated entities
        count=1 gives non-duplicated entities (in only one packet)
        count=0 gives remaining entities (in no packet at all)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ParamEditor(IFSelect_Editor):
    """
    A ParamEditor gives access for edition to a list of TypedValue
    (i.e. of Static too)
    Its definition is made of the TypedValue to edit themselves,
    and can add some constants, which can then be displayed but
    not changed (for instance, system name, processor version ...)

    I.E. it gives a way of editing or at least displaying
    parameters as global
    """

    @overload
    def __init__(self, nbmax: int = 100, label: str = '') -> None:
        """
        Creates a ParamEditor, empty, with a maximum count of params
        (default is 100)
        And a label, by default it will be "Param Editor\"
        """

    @overload
    def __init__(self, theOther: IFSelect_ParamEditor) -> None: ...

    def AddValue(self, val: nanoocp.Interface.Interface_TypedValue | None, shortname: str = '') -> None:
        """
        Adds a TypedValue
        By default, its short name equates its complete name, it can be made explicit
        """

    def AddConstantText(self, val: str, shortname: str, completename: str = '') -> None:
        """
        Adds a Constant Text, it will be Read Only
        By default, its long name equates its shortname
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Recognize(self, form: IFSelect_EditForm | None) -> bool: ...

    def StringValue(self, form: IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Load(self, form: IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    def Apply(self, form: IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    @staticmethod
    def StaticEditor(list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None, label: str = '') -> IFSelect_ParamEditor:
        """
        Returns a ParamEditor to work on the Static Parameters of
        which names are listed in <list>
        Null Handle if <list> is null or empty
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_Selection(nanoocp.Standard.Standard_Transient):
    """
    A Selection allows to define a set of Interface Entities.
    Entities to be put on an output file should be identified in
    a way as independent from such or such execution as possible.
    This permits to handle comprehensive criteria, and to replay
    them when a new variant of an input file has to be processed.

    Its input can be, either an Interface Model (the very source),
    or another-other Selection(s) or any other output.
    All list computations start from an input Graph (from IFGraph)
    """

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities, computed from Input
        given as a Graph. Specific to each class of Selection
        Note that uniqueness of each entity is not required here
        This method can raise an exception as necessary
        """

    def UniqueResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities, each of them being
        unique. Default definition works from RootResult. According
        HasUniqueResult, UniqueResult returns directly RootResult,
        or build a Unique Result from it with a Graph.
        """

    def CompleteResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of entities involved by a Selection, i.e.
        UniqueResult plus the shared entities (directly or not)
        """

    def FillIterator(self, iter: IFSelect_SelectionIterator) -> None:
        """
        Puts in an Iterator the Selections from which "me" depends
        (there can be zero, or one, or a list).
        Specific to each class of Selection
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which defines the criterium applied by a
        Selection (can be used to be printed, displayed ...)
        Specific to each class
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectDeduct(IFSelect_Selection):
    """
    A SelectDeduct determines a list of Entities from an Input
    Selection, by a computation : Output list is not obliged to be
    a sub-list of Input list
    (for more specific, see SelectExtract for filtered sub-lists,
    and SelectExplore for recurcive exploration)

    A SelectDeduct may use an alternate input for one shot
    This allows to use an already existing definition, by
    overloading the input selection by an alternate list,
    already defined, for one use :
    If this alternate list is set, InputResult queries it instead
    of calling the input selection, then clears it immediately
    """

    def SetInput(self, sel: IFSelect_Selection | None) -> None:
        """Defines or Changes the Input Selection"""

    def Input(self) -> IFSelect_Selection:
        """Returns the Input Selection"""

    def HasInput(self) -> bool:
        """Returns True if the Input Selection is defined, False else"""

    def HasAlternate(self) -> bool:
        """
        Tells if an Alternate List has been set, i.e. : the Alternate
        Definition is present and set
        """

    def Alternate(self) -> IFSelect_SelectPointed:
        """
        Returns the Alternate Definition
        It is returned modifiable, hence an already defined
        SelectPointed can be used
        But if it was not yet defined, it is created the first time

        It is exploited by InputResult
        """

    def InputResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the Result determined by Input Selection, as Unique
        if Input Selection is not defined, returns an empty list.

        If Alternate is set, InputResult takes its definition instead
        of calling the Input Selection, then clears it
        """

    def FillIterator(self, iter: IFSelect_SelectionIterator) -> None:
        """
        Puts in an Iterator the Selections from which "me" depends
        This list contains one Selection : the InputSelection
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectAnyList(IFSelect_SelectDeduct):
    """
    A SelectAnyList kind Selection selects a List of an Entity, as
    well as this Entity contains some. A List contains sub-entities
    as one per Item, or several (for instance if an Entity binds
    couples of sub-entities, each item is one of these couples).
    Remark that only Entities are taken into account (neither
    Reals, nor Strings, etc...)

    To define the list on which to work, SelectAnyList has two
    deferred methods : NbItems (which gives the length of the
    list), FillResult (which fills an EntityIterator). They are
    intended to get a List in an Entity of the required Type (and
    consider that list is empty if Entity has not required Type)

    In addition, remark that some types of Entity define more than
    one list in each instance : a given sub-class of SelectAnyList
    must be attached to one list

    SelectAnyList keeps or rejects a sub-set of the list,
    that is the Items of which rank in the list is in a given
    range (for instance form 2nd to 6th, etc...)
    Range is defined by two Integer values. In order to allow
    external control of them, these values are not directly
    defined as fields, but accessed through IntParams, that is,
    referenced as Transient (Handle) objects

    Warning : the Input can be any kind of Selection, BUT its
    RootResult must have zero (empty) or one Entity maximum
    """

    def KeepInputEntity(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Keeps Input Entity, as having required type. It works by
        keeping in <iter>, only suitable Entities (SelectType can be
        used). Called by RootResult (which waits for ONE ENTITY MAX)
        """

    def NbItems(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns count of Items in the list in the Entity <ent>
        If <ent> has not required type, returned value must be Zero
        """

    def SetRange(self, rankfrom: IFSelect_IntParam | None, rankto: IFSelect_IntParam | None) -> None:
        """Sets a Range for numbers, with a lower and a upper limits"""

    def SetOne(self, rank: IFSelect_IntParam | None) -> None:
        """Sets a unique number (only one Entity will be sorted as True)"""

    def SetFrom(self, rankfrom: IFSelect_IntParam | None) -> None:
        """Sets a Lower limit but no upper limit"""

    def SetUntil(self, rankto: IFSelect_IntParam | None) -> None:
        """Sets an Upper limit but no lower limit (equivalent to lower 1)"""

    def HasLower(self) -> bool:
        """Returns True if a Lower limit is defined"""

    def Lower(self) -> IFSelect_IntParam:
        """Returns Lower limit (if there is; else, value is senseless)"""

    def LowerValue(self) -> int:
        """Returns Integer Value of Lower Limit (0 if none)"""

    def HasUpper(self) -> bool:
        """Returns True if a Lower limit is defined"""

    def Upper(self) -> IFSelect_IntParam:
        """Returns Upper limit (if there is; else, value is senseless)"""

    def UpperValue(self) -> int:
        """Returns Integer Value of Upper Limit (0 if none)"""

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities (list of entities
        complying with rank criterium)
        Error if the input list has more than one Item
        """

    def FillResult(self, n1: int, n2: int, ent: nanoocp.Standard.Standard_Transient | None, res: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Puts into <res>, the sub-entities of the list, from n1 to
        n2 included. Remark that adequation with Entity's type and
        length of list has already been made at this stage
        Called by RootResult
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium : "Components of List "
        then Specific List Label, then, following cases :
        " From .. Until .." or "From .." or "Until .." or "Rank no .."
        Specific type is given by deferred method ListLabel
        """

    def ListLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the specific label for the list, which is included as
        a part of Label
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectExtract(IFSelect_SelectDeduct):
    """
    A SelectExtract determines a list of Entities from an Input
    Selection, as a sub-list of the Input Result
    It works by applying a sort criterium on each Entity of the
    Input. This criterium can be applied Direct to Pick Items
    (default case) or Reverse to Remove Item

    Basic features (the unique Input) are inherited from SelectDeduct
    """

    def IsDirect(self) -> bool:
        """Returns True if Sort criterium is Direct, False if Reverse"""

    def SetDirect(self, direct: bool) -> None:
        """
        Sets Sort criterium sense to a new value
        (True : Direct , False : Reverse)
        """

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities. Works by calling the
        method Sort on each input Entity : the Entity is kept as
        output if Sort returns the same value as Direct status
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True for an Entity if it satisfies the Sort criterium
        It receives :
        - <rank>, the rank of the Entity in the Iteration,
        - <ent> , the Entity itself, and
        - <model>, the Starting Model
        Hence, the Entity to check is "model->Value(num)" (but an
        InterfaceModel allows other checks)
        This method is specific to each class of SelectExtract
        """

    def SortInGraph(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph) -> bool:
        """
        Works as Sort but works on the Graph
        Default directly calls Sort, but it can be redefined
        If SortInGraph is redefined, Sort should be defined even if
        not called (to avoid deferred methods in a final class)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text saying "Picked" or "Removed", plus the
        specific criterium returned by ExtractLabel (see below)
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium for extraction"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectAnyType(IFSelect_SelectExtract):
    """
    A SelectAnyType sorts the Entities of which the Type is Kind
    of a given Type : this Type for Match is specific of each
    class of SelectAnyType
    """

    def TypeForMatch(self) -> nanoocp.Standard.Standard_Type:
        """Returns the Type which has to be matched for select"""

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True for an Entity (model->Value(num)) which is kind
        of the chosen type, given by the method TypeForMatch.
        Criterium is IsKind.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectBase(IFSelect_Selection):
    """
    SelectBase works directly from an InterfaceModel : it is the
    first base for other Selections.
    """

    def FillIterator(self, iter: IFSelect_SelectionIterator) -> None:
        """
        Puts in an Iterator the Selections from which "me" depends
        This list is empty for all SelectBase type Selections
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectCombine(IFSelect_Selection):
    """
    A SelectCombine type Selection defines algebraic operations
    between results of several Selections
    It is a deferred class : sub-classes will have to define
    precise what operator is to be applied
    """

    def NbInputs(self) -> int:
        """Returns the count of Input Selections"""

    def Input(self, num: int) -> IFSelect_Selection:
        """Returns an Input Selection, given its rank in the list"""

    def InputRank(self, sel: IFSelect_Selection | None) -> int:
        """
        Returns the rank of an input Selection, 0 if not in the list.
        Most generally, its value is meaningless, except for testing
        the presence of an input Selection :
        - == 0  if <sel> is not an input for <me>
        - >  0  if <sel> is an input for <me>
        """

    def Add(self, sel: IFSelect_Selection | None, atnum: int = 0) -> None:
        """
        Adds a Selection to the filling list
        By default, adds it to the end of the list
        A Positive rank less then NbInputs gives an insertion rank
        (InsertBefore : the new <atnum>th item of the list is <sel>)
        """

    @overload
    def Remove(self, sel: IFSelect_Selection | None) -> bool:
        """
        Removes an input Selection.
        Returns True if Done, False, if <sel> is not an input for <me>
        """

    @overload
    def Remove(self, num: int) -> bool:
        """
        Removes an input Selection, given its rank in the list
        Returns True if Done, False if <num> is out of range
        """

    def FillIterator(self, iter: IFSelect_SelectionIterator) -> None:
        """
        Puts in an Iterator the Selections from which "me" depends
        That is to say, the list of Input Selections
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectControl(IFSelect_Selection):
    """
    A SelectControl kind Selection works with two input Selections
    in a dissymmetric way : the Main Input which gives an input
    list of Entities, to be processed, and the Second Input which
    gives another list, to be used to filter the main input.

    e.g. : SelectDiff retains the items of the Main Input which
    are not in the Control Input (which acts as Diff Input)
    or a specific selection which retains Entities from the Main
    Input if and only if they are concerned by an entity from
    the Control Input (such as Views in IGES, etc...)

    The way RootResult and Label are produced are at charge of
    each sub-class
    """

    def MainInput(self) -> IFSelect_Selection:
        """Returns the Main Input Selection"""

    def HasSecondInput(self) -> bool:
        """
        Returns True if a Control Input is defined
        Thus, Result can be computed differently if there is a
        Control Input or if there is none
        """

    def SecondInput(self) -> IFSelect_Selection:
        """Returns the Control Input Selection, or a Null Handle"""

    def SetMainInput(self, sel: IFSelect_Selection | None) -> None:
        """Sets a Selection to be the Main Input"""

    def SetSecondInput(self, sel: IFSelect_Selection | None) -> None:
        """Sets a Selection to be the Control Input"""

    def FillIterator(self, iter: IFSelect_SelectionIterator) -> None:
        """
        Puts in an Iterator the Selections from which "me" depends
        That is to say, the list of Input Selections
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectDiff(IFSelect_SelectControl):
    """
    A SelectDiff keeps the entities from a Selection, the Main
    Input, which are not listed by the Second Input
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty SelectDiff"""

    @overload
    def __init__(self, theOther: IFSelect_SelectDiff) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities : they are the Entities
        gotten from the Main Input but not from the Diff Input
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Difference\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectEntityNumber(IFSelect_SelectBase):
    """
    A SelectEntityNumber gets in an InterfaceModel (through a
    Graph), the Entity which has a specified Number (its rank of
    adding into the Model) : there can be zero (if none) or one.
    The Number is not directly defined as an Integer, but as a
    Parameter, which can be externally controlled
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectEntityNumber, initially with no specified Number"""

    @overload
    def __init__(self, theOther: IFSelect_SelectEntityNumber) -> None: ...

    def SetNumber(self, num: IFSelect_IntParam | None) -> None:
        """Sets Entity Number to be taken (initially, none is set : 0)"""

    def Number(self) -> IFSelect_IntParam:
        """Returns specified Number (as a Parameter)"""

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities : the Entity having the
        specified Number (this result assures naturally uniqueness)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Entity Number ...\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectErrorEntities(IFSelect_SelectExtract):
    """
    A SelectErrorEntities sorts the Entities which are qualified
    as "Error" (their Type has not been recognized) during reading
    a File. This does not concern Entities which are syntactically
    correct, but with incorrect data (for integrity constraints).
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectErrorEntities"""

    @overload
    def __init__(self, theOther: IFSelect_SelectErrorEntities) -> None: ...

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True for an Entity which is qualified as "Error", i.e.
        if <model> explicitly knows <ent> (through its Number) as
        Erroneous
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Error Entities\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectExplore(IFSelect_SelectDeduct):
    """
    A SelectExplore determines from an input list of Entities,
    a list obtained by a way of exploration. This implies the
    possibility of recursive exploration : the output list is
    itself reused as input, etc...
    Examples : Shared Entities, can be considered at one level
    (immediate shared) or more, or max level

    Then, for each input entity, if it is not rejected, it can be
    either taken itself, or explored : it then produces a list.
    According to a level, either the produced lists or taken
    entities give the result (level one), or lists are themselves
    considered and for each item, is it taken or explored.

    Remark that rejection is just a safety : normally, an input
    entity is, either taken itself, or explored
    A maximum level can be specified. Else, the process continues
    until all entities have been either taken or rejected
    """

    def Level(self) -> int:
        """Returns the required exploring level"""

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities. Works by calling the
        method Explore on each input entity : it can be rejected,
        taken for output, or to explore. If the maximum level has not
        yet been attained, or if no max level is specified, entities
        to be explored are themselves used as if they were input
        """

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Analyses and, if required, Explores an entity, as follows :
        The explored list starts as empty, it has to be filled by this
        method.
        If it returns False, <ent> is rejected for result (this is to
        be used only as safety)
        If it returns True and <explored> remains empty, <ent> is
        taken itself for result, not explored
        If it returns True and <explored> is not empty, the content
        of this list is considered :
        If maximum level is attained, it is taken for result
        Else (or no max), each of its entity will be itself explored
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text saying "(Recursive)" or "(Level nn)" plus
        specific criterium returned by ExploreLabel (see below)
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the way of exploration"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectFlag(IFSelect_SelectExtract):
    """
    A SelectFlag queries a flag noted in the bitmap of the Graph.
    The Flag is designated by its Name. Flag Names are defined
    by Work Session and, as necessary, other functional objects

    WorkSession from IFSelect defines flag "Incorrect"
    Objects which control application running define some others
    """

    @overload
    def __init__(self, flagname: str) -> None:
        """Creates a Select Flag, to query a flag designated by its name"""

    @overload
    def __init__(self, theOther: IFSelect_SelectFlag) -> None: ...

    def FlagName(self) -> str:
        """Returns the name of the flag"""

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities. It is redefined to
        work on the graph itself (not queried by sort)

        An entity is selected if its flag is True on Direct mode,
        False on Reversed mode

        If flag does not exist for the given name, returns an empty
        result, whatever the Direct/Reversed sense
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns always False because RootResult has done the work"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium, includes the flag name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectIncorrectEntities(IFSelect_SelectFlag):
    """
    A SelectIncorrectEntities sorts the Entities which have been
    noted as Incorrect in the Graph of the Session
    (flag "Incorrect")
    It can find a result only if ComputeCheck has formerly been
    called on the WorkSession. Else, its result will be empty.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a SelectIncorrectEntities
        i.e. a SelectFlag("Incorrect")
        """

    @overload
    def __init__(self, theOther: IFSelect_SelectIncorrectEntities) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectInList(IFSelect_SelectAnyList):
    """
    A SelectInList kind Selection selects a List of an Entity,
    which is composed of single Entities
    To know the list on which to work, SelectInList has two
    deferred methods : NbItems (inherited from SelectAnyList) and
    ListedEntity (which gives an item as an Entity) which must be
    defined to get a List in an Entity of the required Type (and
    consider that list is empty if Entity has not required Type)

    As for SelectAnyList, if a type of Entity defines several
    lists, a given sub-class of SelectInList is attached on one
    """

    def ListedEntity(self, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Transient:
        """Returns an Entity, given its rank in the list"""

    def FillResult(self, n1: int, n2: int, ent: nanoocp.Standard.Standard_Transient | None, result: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Puts into the result, the sub-entities of the list, from n1 to
        n2 included. Remark that adequation with Entity's type and
        length of list has already been made at this stage
        Called by RootResult; calls ListedEntity (see below)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectIntersection(IFSelect_SelectCombine):
    """
    A SelectIntersection filters the Entities issued from several
    other Selections as Intersection of results : "AND" operator
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty SelectIntersection"""

    @overload
    def __init__(self, theOther: IFSelect_SelectIntersection) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected Entities, which is the common part
        of results from all input selections. Uniqueness is guaranteed.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Intersection (AND)\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectionIterator:
    """Defines an Iterator on a list of Selections"""

    @overload
    def __init__(self) -> None:
        """Creates an empty iterator, ready to be filled"""

    @overload
    def __init__(self, sel: IFSelect_Selection | None) -> None:
        """
        Creates an iterator from a Selection : it lists the Selections
        from which <sel> depends (given by its method FillIterator)
        """

    @overload
    def __init__(self, theOther: IFSelect_SelectionIterator) -> None: ...

    def __iter__(self) -> IFSelect_SelectionIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> IFSelect_Selection:
        """Python addition: see __iter__."""

    def AddFromIter(self, iter: IFSelect_SelectionIterator) -> None:
        """
        Adds to an iterator the content of another one
        (each selection is present only once in the result)
        """

    def AddItem(self, sel: IFSelect_Selection | None) -> None:
        """Adds a Selection to an iterator (if not yet noted)"""

    def AddList(self, list: nanoocp.NCollection.NCollection_Sequence[nanoocp.IFSelect.IFSelect_Selection]) -> None:
        """
        Adds a list of Selections to an iterator (this list comes
        from the description of a Selection or a Dispatch, etc...)
        """

    def More(self) -> bool:
        """Returns True if there are more Selections to get"""

    def Next(self) -> None:
        """Sets iterator to the next item"""

    def Value(self) -> IFSelect_Selection:
        """
        Returns the current Selection being iterated
        Error if count of Selection has been passed
        """

class IFSelect_SelectModelEntities(IFSelect_SelectBase):
    """
    A SelectModelEntities gets all the Entities of an
    InterfaceModel.
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectModelRoot"""

    @overload
    def __init__(self, theOther: IFSelect_SelectModelEntities) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities : the Entities of the
        Model (note that this result assures naturally uniqueness)
        """

    def CompleteResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        The complete list of Entities (including shared ones) ...
        is exactly identical to RootResults in this case
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Model Entities\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectModelRoots(IFSelect_SelectBase):
    """
    A SelectModelRoots gets all the Root Entities of an
    InterfaceModel. Remember that a "Root Entity" is defined as
    having no Sharing Entity (if there is a Loop between Entities,
    none of them can be a "Root").
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectModelRoot"""

    @overload
    def __init__(self, theOther: IFSelect_SelectModelRoots) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities : the Roots of the Model
        (note that this result assures naturally uniqueness)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Model Roots\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectPointed(IFSelect_SelectBase):
    """
    This type of Selection is intended to describe a direct
    selection without an explicit criterium, for instance the
    result of picking viewed entities on a graphic screen

    It can also be used to provide a list as internal alternate
    input : this use implies to clear the list once queried
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectPointed"""

    @overload
    def __init__(self, theOther: IFSelect_SelectPointed) -> None: ...

    def Clear(self) -> None:
        """
        Clears the list of selected items
        Also says the list is unset
        All Add* methods and SetList say the list is set
        """

    def IsSet(self) -> bool:
        """Tells if the list has been set. Even if empty"""

    def SetEntity(self, item: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        As SetList but with only one entity
        If <ent> is Null, the list is said as being set but is empty
        """

    def SetList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None:
        """
        Sets a given list to define the list of selected items
        <list> can be empty or null : in this case, the list is said
        as being set, but it is empty

        To use it as an alternate input, one shot :
        - SetList or SetEntity to define the input list
        - RootResult to get it
        - then Clear to drop it
        """

    def Add(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Adds an item. Returns True if Done, False if <item> is already
        in the selected list
        """

    def Remove(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Removes an item. Returns True if Done, False if <item> was not
        in the selected list
        """

    def Toggle(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Toggles status of an item : adds it if not pointed or removes
        it if already pointed. Returns the new status (Pointed or not)
        """

    def AddList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> bool:
        """
        Adds all the items defined in a list. Returns True if at least
        one item has been added, False else
        """

    def RemoveList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> bool:
        """
        Removes all the items defined in a list. Returns True if at
        least one item has been removed, False else
        """

    def ToggleList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> bool:
        """
        Toggles status of all the items defined in a list : adds it if
        not pointed or removes it if already pointed.
        """

    def Rank(self, item: nanoocp.Standard.Standard_Transient | None) -> int:
        """Returns the rank of an item in the selected list, or 0."""

    def NbItems(self) -> int:
        """Returns the count of selected items"""

    def Item(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """Returns an item given its rank, or a Null Handle"""

    @overload
    def Update(self, control: nanoocp.Interface.Interface_CopyControl | None) -> None:
        """
        Rebuilds the selected list. Any selected entity which has a
        bound result is replaced by this result, else it is removed.
        """

    @overload
    def Update(self, trf: IFSelect_Transformer | None) -> None:
        """
        Rebuilds the selected list, by querying a Transformer
        (same principle as from a CopyControl)
        """

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected items. Only the selected entities
        which are present in the graph are given (this result assures
        uniqueness).
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which identifies the type of selection made.
        It is "Pointed Entities\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectRange(IFSelect_SelectExtract):
    """
    A SelectRange keeps or rejects a sub-set of the input set,
    that is the Entities of which rank in the iteration list
    is in a given range (for instance form 2nd to 6th, etc...)
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectRange. Default is Take all the input list"""

    @overload
    def __init__(self, theOther: IFSelect_SelectRange) -> None: ...

    def SetRange(self, rankfrom: IFSelect_IntParam | None, rankto: IFSelect_IntParam | None) -> None:
        """
        Sets a Range for numbers, with a lower and a upper limits
        Error if rankto is lower then rankfrom
        """

    def SetOne(self, rank: IFSelect_IntParam | None) -> None:
        """Sets a unique number (only one Entity will be sorted as True)"""

    def SetFrom(self, rankfrom: IFSelect_IntParam | None) -> None:
        """Sets a Lower limit but no upper limit"""

    def SetUntil(self, rankto: IFSelect_IntParam | None) -> None:
        """Sets an Upper limit but no lower limit (equivalent to lower 1)"""

    def HasLower(self) -> bool:
        """Returns True if a Lower limit is defined"""

    def Lower(self) -> IFSelect_IntParam:
        """Returns Lower limit (if there is; else, value is senseless)"""

    def LowerValue(self) -> int:
        """Returns Value of Lower Limit (0 if none is defined)"""

    def HasUpper(self) -> bool:
        """Returns True if a Lower limit is defined"""

    def Upper(self) -> IFSelect_IntParam:
        """Returns Upper limit (if there is; else, value is senseless)"""

    def UpperValue(self) -> int:
        """Returns Value of Upper Limit (0 if none is defined)"""

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True for an Entity of which occurrence number in the
        iteration is inside the selected Range (considers <rank>)
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium : following cases,
        " From .. Until .." or "From .." or "Until .." or "Rank no ..\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectRootComps(IFSelect_SelectExtract):
    """
    A SelectRootComps sorts the Entities which are part of Strong
    Components, local roots of a set of Entities : they can be
    Single Components (containing one Entity) or Cycles
    This class gives a more secure result than SelectRoots (which
    considers only Single Components) but is longer to work : it
    can be used when there can be or there are cycles in a Model
    For each cycle, one Entity is given arbitrarily
    Reject works as for SelectRoots : Strong Components defined in
    the input list which are not local roots are given
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectRootComps"""

    @overload
    def __init__(self, theOther: IFSelect_SelectRootComps) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of local root strong components, by one Entity per component.
        It is redefined for a purpose of efficiency : calling a Sort routine for each Entity would
        cost more resources than to work in once using a Map
        RootResult takes in account the Direct status
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns always True, because RootResult has done work"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Local Root Components\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectRoots(IFSelect_SelectExtract):
    """
    A SelectRoots sorts the Entities which are local roots of a
    set of Entities (not shared by other Entities inside this set,
    even if they are shared by other Entities outside it)
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectRoots"""

    @overload
    def __init__(self, theOther: IFSelect_SelectRoots) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of local roots.
        It is redefined for a purpose of efficiency:
        calling a Sort routine for each Entity would cost more resources
        than to work in once using a Map RootResult takes in account the Direct status.
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns always True, because RootResult has done work"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Local Root Entities\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectSent(IFSelect_SelectExtract):
    """
    This class returns entities according sending to a file
    Once a model has been loaded, further sendings are recorded
    as status in the graph (for each value, a count of sendings)

    Hence, it is possible to query entities : sent ones (at least
    once), non-sent (i.e. remaining) ones, duplicated ones, etc...

    This selection performs this query
    """

    @overload
    def __init__(self, sentcount: int = 1, atleast: bool = True) -> None:
        """
        Creates a SelectSent :
        sentcount = 0 -> remaining (non-sent) entities
        sentcount = 1, atleast = True (D) -> sent (at least once)
        sentcount = 2, atleast = True -> duplicated (sent least twice)
        etc...
        sentcount = 1, atleast = False -> sent just once (non-dupl.d)
        sentcount = 2, atleast = False -> sent just twice
        etc...
        """

    @overload
    def __init__(self, theOther: IFSelect_SelectSent) -> None: ...

    def SentCount(self) -> int:
        """Returns the queried count of sending"""

    def AtLeast(self) -> bool:
        """
        Returns the <atleast> status, True for sending at least the
        sending count, False for sending exactly the sending count
        Remark : if SentCount is 0, AtLeast is ignored
        """

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities. It is redefined to
        work on the graph itself (not queried by sort)

        An entity is selected if its count complies to the query in
        Direct Mode, rejected in Reversed Mode

        Query works on the sending count recorded as status in Graph
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns always False because RootResult has done the work"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium : query :
        SentCount = 0 -> "Remaining (non-sent) entities"
        SentCount = 1, AtLeast = True  -> "Sent entities"
        SentCount = 1, AtLeast = False -> "Sent once (no duplicated)"
        SentCount = 2, AtLeast = True  -> "Sent several times entities"
        SentCount = 2, AtLeast = False -> "Sent twice entities"
        SentCount > 2, AtLeast = True  -> "Sent at least <count> times entities"
        SentCount > 2, AtLeast = False -> "Sent <count> times entities\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectShared(IFSelect_SelectDeduct):
    """
    A SelectShared selects Entities which are directly Shared
    by the Entities of the Input list
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectShared;"""

    @overload
    def __init__(self, theOther: IFSelect_SelectShared) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities (list of entities
        shared by those of input list)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Shared (one level)\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectSharing(IFSelect_SelectDeduct):
    """
    A SelectSharing selects Entities which directly Share (Level
    One) the Entities of the Input list
    Remark : if an Entity of the Input List directly shares
    another one, it is of course present in the Result List
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectSharing;"""

    @overload
    def __init__(self, theOther: IFSelect_SelectSharing) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities (list of entities
        which share (level one) those of input list)
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Sharing (one level)\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectSignature(IFSelect_SelectExtract):
    """
    A SelectSignature sorts the Entities on a Signature Matching.
    The signature to match is given at creation time. Also, the
    required match is given at creation time : exact (IsEqual) or
    contains (the Type's Name must contain the criterium Text)

    Remark that no more interpretation is done, it is an
    alphanumeric signature : for instance, DynamicType is matched
    as such, super-types are not considered

    Also, numeric (integer) comparisons are supported : an item
    can be <val ou <=val or >val or >=val , val being an Integer

    A SelectSignature may also be created from a SignCounter,
    which then just gives its LastValue as SignatureValue
    """

    @overload
    def __init__(self, matcher: IFSelect_Signature | None, signtext: str, exact: bool = True) -> None:
        """
        Creates a SelectSignature with its Signature and its Text to
        Match.
        <exact> if True requires exact match,
        if False requires <signtext> to be contained in the Signature
        of the entity (default is "exact")
        """

    @overload
    def __init__(self, matcher: IFSelect_Signature | None, signtext: nanoocp.TCollection.TCollection_AsciiString, exact: bool = True) -> None:
        """As above with an AsciiString"""

    @overload
    def __init__(self, matcher: IFSelect_SignCounter | None, signtext: str, exact: bool = True) -> None:
        """
        Creates a SelectSignature with a Counter, more precisely a
        SelectSignature. Which is used here to just give a Signature
        Value (by SignOnly Mode)
        Matching is the default provided by the class Signature
        """

    @overload
    def __init__(self, theOther: IFSelect_SelectSignature) -> None: ...

    def Signature(self) -> IFSelect_Signature:
        """
        Returns the used Signature, then it is possible to access it,
        modify it as required. Can be null, hence see Counter
        """

    def Counter(self) -> IFSelect_SignCounter:
        """
        Returns the used SignCounter. Can be used as alternative for
        Signature
        """

    def SortInGraph(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph) -> bool:
        """
        Returns True for an Entity (model->Value(num)) of which the
        signature matches the text given as creation time
        May also work with a Counter from the Graph
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Not called, defined only to remove a deferred method here"""

    def SignatureText(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Text used to Sort Entity on its Signature or SignCounter"""

    def IsExact(self) -> bool:
        """Returns True if match must be exact"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium.
        (it refers to the text and exact flag to be matched, and is
        qualified by the Name provided by the Signature)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectSignedShared(IFSelect_SelectExplore):
    """
    In the graph, explore the Shareds of the input entities,
    until it encounters some which match a given Signature
    (for a limited level, filters the returned list)
    By default, fitted for any level
    """

    @overload
    def __init__(self, matcher: IFSelect_Signature | None, signtext: str, exact: bool = True, level: int = 0) -> None:
        """
        Creates a SelectSignedShared, defaulted for any level
        with a given Signature and text to match
        """

    @overload
    def __init__(self, theOther: IFSelect_SelectSignedShared) -> None: ...

    def Signature(self) -> IFSelect_Signature:
        """
        Returns the used Signature, then it is possible to access it,
        modify it as required
        """

    def SignatureText(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Text used to Sort Entity on its Signature"""

    def IsExact(self) -> bool:
        """Returns True if match must be exact"""

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity : its Shared entities
        <ent> to take if it matches the Signature
        At level max, filters the result. Else gives all Shareds
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium.
        (it refers to the text and exact flag to be matched, and is
        qualified by the Name provided by the Signature)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectSignedSharing(IFSelect_SelectExplore):
    """
    In the graph, explore the sharings of the input entities,
    until it encounters some which match a given Signature
    (for a limited level, filters the returned list)
    By default, fitted for any level
    """

    @overload
    def __init__(self, matcher: IFSelect_Signature | None, signtext: str, exact: bool = True, level: int = 0) -> None:
        """
        Creates a SelectSignedSharing, defaulted for any level
        with a given Signature and text to match
        """

    @overload
    def __init__(self, theOther: IFSelect_SelectSignedSharing) -> None: ...

    def Signature(self) -> IFSelect_Signature:
        """
        Returns the used Signature, then it is possible to access it,
        modify it as required
        """

    def SignatureText(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Text used to Sort Entity on its Signature"""

    def IsExact(self) -> bool:
        """Returns True if match must be exact"""

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity : its sharing entities
        <ent> to take if it matches the Signature
        At level max, filters the result. Else gives all sharings
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium.
        (it refers to the text and exact flag to be matched, and is
        qualified by the Name provided by the Signature)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectSuite(IFSelect_SelectDeduct):
    """
    A SelectSuite can describe a suite of SelectDeduct as a unique
    one : in other words, it can be seen as a "macro selection"

    It works by applying each of its items (which is a
    SelectDeduct) on the result computed by the previous one
    (by using Alternate Input)

    But each of these Selections used as items may be used
    independently, it will then give its own result

    Hence, SelectSuite gives a way of defining a new Selection
    from existing ones, without having to do copies or saves
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty SelectSuite"""

    @overload
    def __init__(self, theOther: IFSelect_SelectSuite) -> None: ...

    def AddInput(self, item: IFSelect_Selection | None) -> bool:
        """
        Adds an input selection. I.E. :
        If <item> is a SelectDeduct, adds it as Previous, not as Input
        Else, sets it as Input
        Returns True when done
        Returns False and refuses to work if Input is already defined
        """

    def AddPrevious(self, item: IFSelect_SelectDeduct | None) -> None:
        """
        Adds a new first item (prepends to the list). The Input is not
        touched
        If <item> is null, does nothing
        """

    def AddNext(self, item: IFSelect_SelectDeduct | None) -> None:
        """
        Adds a new last item (prepends to the list)
        If <item> is null, does nothing
        """

    def NbItems(self) -> int:
        """Returns the count of Items"""

    def Item(self, num: int) -> IFSelect_SelectDeduct:
        """
        Returns an item from its rank in the list
        (the Input is always apart)
        """

    def SetLabel(self, lab: str) -> None:
        """Sets a value for the Label"""

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected entities
        To do this, once InputResult has been taken (if Input or
        Alternate has been defined, else the first Item gives it) :
        this result is set as alternate input for the first item,
        which computes its result : this result is set as alternate
        input for the second item, etc...
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the Label
        Either it has been defined by SetLabel, or it will give
        "Suite of nn Selections\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectType(IFSelect_SelectAnyType):
    """
    A SelectType keeps or rejects Entities of which the Type
    is Kind of a given Cdl Type
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectType. Default is no filter"""

    @overload
    def __init__(self, atype: nanoocp.Standard.Standard_Type | None) -> None:
        """Creates a SelectType for a given Type"""

    @overload
    def __init__(self, theOther: IFSelect_SelectType) -> None: ...

    def SetType(self, atype: nanoocp.Standard.Standard_Type | None) -> None:
        """Sets a TYpe for filter"""

    def TypeForMatch(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type to be matched for select : this is the type
        given at instantiation time
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium.
        (should by gotten from Type of Entity used for instantiation)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectUnion(IFSelect_SelectCombine):
    """
    A SelectUnion cumulates the Entities issued from several other
    Selections (union of results : "OR" operator)
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty SelectUnion"""

    @overload
    def __init__(self, theOther: IFSelect_SelectUnion) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of selected Entities, which is the addition
        result from all input selections. Uniqueness is guaranteed.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Union (OR)\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SelectUnknownEntities(IFSelect_SelectExtract):
    """
    A SelectUnknownEntities sorts the Entities which are qualified
    as "Unknown" (their Type has not been recognized)
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectUnknownEntities"""

    @overload
    def __init__(self, theOther: IFSelect_SelectUnknownEntities) -> None: ...

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True for an Entity which is qualified as "Unknown",
        i.e. if <model> known <ent> (through its Number) as Unknown
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Recognized Entities\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SessionFile:
    """
    A SessionFile is intended to manage access between a
    WorkSession and an Ascii Form, to be considered as a Dump.
    It allows to write the File from the WorkSession, and later
    read the File to the WorkSession, by keeping required
    descriptions (such as dependences).

    The produced File is under an Ascii Form, then it may be
    easily consulted.
    It is possible to cumulate reading of several Files. But in
    case of Names conflict, the newer Names are forgottens.

    The Dump supports the description of XSTEP functionalities
    (Sharing an Interface File, with Selections, Dispatches,
    Modifiers ...) but does not refer to the Interface File
    which is currently loaded.

    SessionFile works with a library of SessionDumper type objects

    The File is Produced as follows :
    SessionFile produces all general Information (such as Int and
    Text Parameters, Types and Inputs of Selections, Dispatches,
    Modifiers ...) and calls the SessionDumpers to produce all
    the particular Data : creation arguments, parameters to be set
    It is Read in the same terms :
    SessionFile reads and interprets all general Information,
    and calls the SessionDumpers to recognize Types and for a
    recognized Type create the corresponding Object with its
    particular parameters as they were written.
    The best way to work is to have one SessionDumper for each
    consistent set of classes (e.g. a package).
    """

    @overload
    def __init__(self, WS: IFSelect_WorkSession | None) -> None:
        """
        Creates a SessionFile, ready to read Files in order to load
        them into a given WorkSession.
        The following Read Operations must then be called.
        It is also possible to perform a Write, which produces a
        complete File of all the content of the WorkSession.
        """

    @overload
    def __init__(self, WS: IFSelect_WorkSession | None, filename: str) -> None:
        """
        Creates a SessionFile which Writes the content of a WorkSession
        to a File (directly calls Write)
        Then, IsDone acknowledges on the result of the Operation.
        But such a SessionFile may not Read a File to a WorkSession.
        """

    @overload
    def __init__(self, theOther: IFSelect_SessionFile) -> None: ...

    def ClearLines(self) -> None:
        """Clears the lines recorded whatever for writing or for reading"""

    def NbLines(self) -> int:
        """Returns the count of recorded lines"""

    def Line(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a line given its rank in the list of recorded lines"""

    def AddLine(self, line: str) -> None:
        """Adds a line to the list of recorded lines"""

    def RemoveLastLine(self) -> None:
        """
        Removes the last line. Can be called recursively.
        Does nothing if the list is empty
        """

    def WriteFile(self, name: str) -> bool:
        """
        Writes the recorded lines to a file named <name> then clears
        the list of lines.
        Returns False (with no clearing) if the file could not be
        created
        """

    def ReadFile(self, name: str) -> bool:
        """
        Reads the recorded lines from a file named <name>, after
        having cleared the list (stops if RecognizeFile fails)
        Returns False (with no clearing) if the file could not be read
        """

    def RecognizeFile(self, headerline: str) -> bool:
        """Recognizes the header line. returns True if OK, False else"""

    def Write(self, filename: str) -> int:
        """
        Performs a Write Operation from a WorkSession to a File
        i.e. calls WriteSession then WriteEnd, and WriteFile
        Returned Value is : 0 for OK, -1 File could not be created,
        >0 Error during Write (see WriteSession)
        IsDone can be called too (will return True for OK)
        """

    def Read(self, filename: str) -> int:
        """
        Performs a Read Operation from a file to a WorkSession
        i.e. calls ReadFile, then ReadSession and ReadEnd
        Returned Value is : 0 for OK, -1 File could not be opened,
        >0 Error during Read (see WriteSession)
        IsDone can be called too (will return True for OK)
        """

    def WriteSession(self) -> int:
        """
        Prepares the Write operation from a WorkSession (IFSelect) to
        a File, i.e. fills the list of lines (the file itself remains
        to be written; or NbLines/Line may be called)
        Important Remark : this excludes the reading of the last line,
        which is performed by WriteEnd
        Returns 0 if OK, status > 0 in case of error
        """

    def WriteEnd(self) -> int:
        """
        Writes the trailing line. It is separate from WriteSession,
        in order to allow to redefine WriteSession without touching
        WriteEnd (WriteSession defines the body of the file)
        WriteEnd fills the list of lines. Returns a status of error,
        0 if OK, >0 else
        """

    def WriteLine(self, line: str, follow: str = '\x00') -> None:
        """
        Writes a line to the File. If <follow> is given, it is added
        at the following of the line. '\\n' must be added for the end.
        """

    def WriteOwn(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Writes the Parameters own to each type of Item. Uses the
        Library of SessionDumpers
        Returns True if Done, False if <item> could not be treated
        (hence it remains written with no Own Parameter)
        """

    def ReadSession(self) -> int:
        """
        Performs a Read Operation from a File to a WorkSession, i.e.
        reads the list of line (which must have already been loaded,
        by ReadFile or by calls to AddLine)
        Important Remark : this excludes the reading of the last line,
        which is performed by ReadEnd
        Returns 0 for OK, >0 status for Read Error (not a suitable
        File, or WorkSession given as Immutable at Creation Time)
        IsDone can be called too (will return True for OK)
        """

    def ReadEnd(self) -> int:
        """
        Reads the end of a file (its last line). Returns 0 if OK,
        status >0 in case of error (not a suitable end line).
        """

    def ReadLine(self) -> bool:
        """
        Reads a Line and splits it into a set of alphanumeric items,
        which can then be queried by NbParams/ParamValue ...
        """

    def SplitLine(self, line: str) -> None:
        """
        Internal routine which processes a line into words
        and prepares its exploration
        """

    def ReadOwn(self) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Tries to Read an Item, by calling the Library of Dumpers
        Sets the list of parameters of the line to be read from the
        first own one
        """

    def AddItem(self, item: nanoocp.Standard.Standard_Transient | None, active: bool = True) -> None:
        """
        Adds an Item to the WorkSession, taken as Name the first
        item of the read Line. If this Name is not a Name but a Number
        or if this Name is already recorded in the WorkSession, it
        adds the Item but with no Name. Then the Name is recorded
        in order to be used by the method ItemValue
        <active> commands to make <item> active or not in the session
        """

    def IsDone(self) -> bool:
        """
        Returns True if the last Read or Write operation has been correctly performed.
        Else returns False.
        """

    def WorkSession(self) -> IFSelect_WorkSession:
        """
        Returns the WorkSession on which a SessionFile works.
        Remark that it is returned as Immutable.
        """

    def NewItem(self, ident: int, par: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        At beginning of writing an Item, writes its basics :
        - either its name in the session if it has one
        - or its relative number of item in the file, else (preceded by a '_')
        - then, its Dynamic Type (in the sense of cdl : pk_class)
        This basic description can be followed by the parameters
        which are used in the definition of the item.
        """

    def SetOwn(self, mode: bool) -> None:
        """
        Sets Parameters to be sent as Own if <mode> is True (their
        Name or Number or Void Mark or Text Value is preceded by a
        Column sign ':') else they are sent normally
        Hence, the Own Parameter are clearly identified in the File
        """

    def SendVoid(self) -> None:
        """
        During a Write action, commands to send a Void Parameter
        i.e. a Parameter which is present but undefined
        Its form will be the dollar sign : $
        """

    def SendItem(self, par: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        During a Write action, commands to send the identification of
        a Parameter : if it is Null (undefined) it is send as Void ($)
        if it is Named in the WorkSession, its Name is sent preceded
        by ':', else a relative Ident Number is sent preceded by '#'
        (relative to the present Write, i.e. starting at one, without
        skip, and counted part from Named Items)
        """

    def SendText(self, text: str) -> None:
        """
        During a Write action, commands to send a Text without
        interpretation. It will be sent as well
        """

    def SetLastGeneral(self, lastgen: int) -> None:
        """
        Sets the rank of Last General Parameter to a new value. It is
        followed by the Fist Own Parameter of the item.
        Used by SessionFile after reading general parameters.
        """

    def NbParams(self) -> int:
        """
        During a Read operation, SessionFile processes sequentially the Items to read.
        For each one, it gives access to the list
        of its Parameters : they were defined by calls to
        SendVoid/SendParam/SendText during Writing the File.
        NbParams returns the count of Parameters for the line
        currently read.
        """

    def IsVoid(self, num: int) -> bool:
        """
        Returns True if a Parameter, given its rank in the Own List
        (see NbOwnParams), is Void. Returns also True if <num> is
        out of range (undefined parameters)
        """

    def IsText(self, num: int) -> bool:
        """
        Returns True if a Parameter, in the Own List (see NbOwnParams)
        is a Text (between "..."). Else it is an Item (Parameter,
        Selection, Dispatch ...), which can be Void.
        """

    def ParamValue(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a Parameter (alphanumeric item of a line) as it
        has been read
        """

    def TextValue(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the content of a Text Parameter (without the quotes).
        Returns an empty string if the Parameter is not a Text.
        """

    def ItemValue(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns a Parameter as an Item. Returns a Null Handle if the
        Parameter is a Text, or if it is defined as Void
        """

    def Destroy(self) -> None:
        """Specific Destructor (closes the File if not yet done)"""

class IFSelect_ShareOut(nanoocp.Standard.Standard_Transient):
    """
    This class gathers the information required to produce one or
    several file(s) from the content of an InterfaceModel (passing
    through the creation of intermediate Models).

    It can correspond to a complete Divide up of a set of Entities
    intended to be exhaustive and to limit duplications. Or to a
    simple Extraction of some Entities, in order to work on them.

    A ShareOut is composed of a list of Dispatches.
    To Each Dispatch in the ShareOut, is bound an Id. Number
    This Id. Number allows to identify a Display inside the
    ShareOut in a stable way (for instance, to attach file names)

    ShareOut can be seen as a "passive" description, activated
    through a ShareOutResult, which gives the InterfaceModel on
    which to work, as a unique source. Thus it is easy to change
    it without coherence problems

    Services about it are provided by the class ShareOutResult
    which is a service class : simulation (list of files and of
    entities per file; "forgotten" entities; duplicated entities),
    exploitation (generation of derivated Models, each of them
    generating an output file)
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty ShareOut"""

    @overload
    def __init__(self, theOther: IFSelect_ShareOut) -> None: ...

    def Clear(self, onlydisp: bool) -> None:
        """
        Removes in one operation all the Dispatches with their Idents
        Also clears all information about Names, and all Results but
        naming information which are :
        - kept if <onlydisp> is True.
        - cleared if <onlydisp> is False (complete clearing)
        If <onlydisp> is True, that's all. Else, clears also Modifiers
        """

    def ClearResult(self, alsoname: bool) -> None:
        """
        Clears all data produced (apart from Dispatches, etc...)
        if <alsoname> is True, all is cleared. Else, information
        about produced Names are kept (to maintain unicity of naming
        across clearings)
        """

    def RemoveItem(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Removes an item, which can be, either a Dispatch (removed from
        the list of Dispatches), or a GeneralModifier (removed from
        the list of Model Modifiers or from the list of File Modifiers
        according to its type).
        Returns True if done, False if has not been found or if it is
        neither a Dispatch, nor a Modifier.
        """

    def LastRun(self) -> int:
        """Returns the rank of last run item (ClearResult resets it to 0)"""

    def SetLastRun(self, last: int) -> None:
        """Records a new value for the rank of last run item"""

    def NbDispatches(self) -> int:
        """Returns the count of Dispatches"""

    def DispatchRank(self, disp: IFSelect_Dispatch | None) -> int:
        """
        Returns the Rank of a Dispatch, given its Value (Handle).
        Returns 0 if the Dispatch is unknown in the ShareOut
        """

    def Dispatch(self, num: int) -> IFSelect_Dispatch:
        """Returns a Dispatch, given its rank in the list"""

    def AddDispatch(self, disp: IFSelect_Dispatch | None) -> None:
        """Adds a Dispatch to the list"""

    def RemoveDispatch(self, rank: int) -> bool:
        """
        Removes a Dispatch, given its rank in the list
        Returns True if done, False if rank is not between
        (LastRun + 1) and (NbDispatches)
        """

    @overload
    def AddModifier(self, modifier: IFSelect_GeneralModifier | None, atnum: int) -> None:
        """
        Sets a Modifier to be applied on all Dispatches to be run
        If <modifier> is a ModelModifier, adds it to the list of
        Model Modifiers; else to the list of File Modifiers
        By default (atnum = 0) at the end of the list, else at <atnum>
        Each Modifier is used, after each copy of a packet of Entities
        into a Model : its criteria are checked and if they are OK,
        the method Perform of this Modifier is run.
        """

    @overload
    def AddModifier(self, modifier: IFSelect_GeneralModifier | None, dispnum: int, atnum: int) -> None:
        """
        Sets a Modifier to be applied on the Dispatch <dispnum>
        If <modifier> is a ModelModifier, adds it to the list of
        Model Modifiers; else to the list of File Modifiers
        This is the same list as for all Dispatches, but the
        Modifier is qualified to be applied to one Dispatch only
        Then, <atnum> refers to the entire list
        By default (atnum = 0) at the end of the list, else at <atnum>
        Remark : if the Modifier was already in the list and if
        <atnum> = 0, the Modifier is not moved, but only qualified
        for a Dispatch
        """

    def AddModif(self, modifier: IFSelect_GeneralModifier | None, formodel: bool, atnum: int = 0) -> None:
        """
        Adds a Modifier to the list of Modifiers : Model Modifiers if
        <formodel> is True, File Modifiers else (internal).
        """

    def NbModifiers(self, formodel: bool) -> int:
        """
        Returns count of Modifiers (which apply to complete Models) :
        Model Modifiers if <formodel> is True, File Modifiers else
        """

    def GeneralModifier(self, formodel: bool, num: int) -> IFSelect_GeneralModifier:
        """
        Returns a Modifier of the list, given its rank :
        Model Modifiers if <formodel> is True, File Modifiers else
        """

    def ModelModifier(self, num: int) -> IFSelect_Modifier:
        """Returns a Modifier of the list of Model Modifiers, duely casted"""

    def ModifierRank(self, modifier: IFSelect_GeneralModifier | None) -> int:
        """
        Gives the rank of a Modifier in the list, 0 if not in the list
        Model Modifiers if <modifier> is kind of ModelModifer,
        File Modifiers else
        """

    def RemoveModifier(self, formodel: bool, num: int) -> bool:
        """
        Removes a Modifier, given it rank in the list :
        Model Modifiers if <formodel> is True, File Modifiers else
        Returns True if done, False if <num> is out of range
        """

    def ChangeModifierRank(self, formodel: bool, befor: int, after: int) -> bool:
        """
        Changes the rank of a modifier in the list :
        Model Modifiers if <formodel> is True, File Modifiers else
        from <before> to <after>
        Returns True if done, False else (before or after out of range)
        """

    def SetRootName(self, num: int, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> bool:
        """
        Attaches a Root Name to a Dispatch given its rank, as an
        HAsciiString (standard form). A Null Handle resets this name.
        Returns True if OK, False if this Name is already attached,
        for a Dispatch or for Default, or <num> out of range
        """

    def HasRootName(self, num: int) -> bool:
        """
        Returns True if the Dispatch of rank <num> has an attached
        Root Name. False else, or if num is out of range
        """

    def RootName(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the Root bound to a Dispatch, given its rank
        Returns a Null Handle if not defined
        """

    def RootNumber(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> int:
        """
        Returns an integer value about a given root name :
        - positive : it's the rank of the Dispatch which has this name
        - null : this root name is unknown
        - negative (-1) : this root name is the default root name
        """

    def SetPrefix(self, pref: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Defines or Changes the general Prefix (which is prepended to
        complete file name generated). If this method is not call,
        Prefix remains empty
        """

    def SetDefaultRootName(self, defrt: nanoocp.TCollection.TCollection_HAsciiString | None) -> bool:
        """
        Defines or Changes the Default Root Name to a new value (which
        is used for dispatches which have no attached root name).
        If this method is not called, DefaultRootName remains empty
        Returns True if OK, False if this Name is already attached,
        for a Dispatch or for Default
        """

    def SetExtension(self, ext: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Defines or Changes the general Extension (which is appended to
        complete file name generated). If this method is not call,
        Extension remains empty
        """

    def Prefix(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the general Prefix. Can be empty."""

    def DefaultRootName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the Default Root Name. Can be empty."""

    def Extension(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the general Extension. Can be empty (not recommended)"""

    def FileName(self, dnum: int, pnum: int, nbpack: int = 0) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Computes the complete file name for a Packet of a Dispatch,
        given Dispatch Number (Rank), Packet Number, and Count of
        Packets generated by this Dispatch (0 if unknown)

        File Name is made of following strings, concatenated :
        General Prefix, Root Name for Dispatch, Packet Suffix, and
        General Extension. If no Root Name is specified for a
        Dispatch, DefaultRootName is considered (and pnum is not used,
        but <thenbdefs> is incremented and used
        Error if no Root is defined for this <idnum>
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_ShareOutResult:
    """
    This class gives results computed from a ShareOut : simulation
    before transfer, helps to list entities ...
    Transfer itself will later be performed, either by a
    TransferCopy to simply divide up a file, or a TransferDispatch
    which can be parametred with more details
    """

    @overload
    def __init__(self, sho: IFSelect_ShareOut | None, mod: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Creates a ShareOutResult from a ShareOut, to work on a Model
        (without any more precision; uses Active Protocol)
        """

    @overload
    def __init__(self, sho: IFSelect_ShareOut | None, G: nanoocp.Interface.Interface_Graph) -> None:
        """
        Creates a ShareOutResult from a ShareOut, to work on a Graph
        already computed, which defines the Input Model and can
        specialize some Entities
        """

    @overload
    def __init__(self, disp: IFSelect_Dispatch | None, mod: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Creates a ShareOutResult from a unique Dispatch, to work on
        a Model. As if it was a ShareOut with only one Dispatch
        (without any more precision; uses Active Protocol)
        Allows to compute the effect of a single Dispatch
        """

    @overload
    def __init__(self, disp: IFSelect_Dispatch | None, G: nanoocp.Interface.Interface_Graph) -> None:
        """
        Creates a ShareOutResult from a unique Dispatch, to work on
        a Graph. As if it was a ShareOut with only one Dispatch
        Allows to compute the effect of a single Dispatch
        """

    def ShareOut(self) -> IFSelect_ShareOut:
        """
        Returns the ShareOut used to create the ShareOutResult
        if creation from a Dispatch, returns a Null Handle
        """

    def Graph(self) -> nanoocp.Interface.Interface_Graph:
        """Returns the Graph used to create theShareOutResult"""

    def Reset(self) -> None:
        """Erases computed data, in order to command a new Evaluation"""

    def Evaluate(self) -> None:
        """
        Evaluates the result of a ShareOut : determines Entities to be
        forgotten by the ShareOut, Entities to be transferred several
        times (duplicated), prepares an iteration on the packets to be
        produced
        Called the first time anyone question is asked, or after a
        call to Reset. Works by calling the method Prepare.
        """

    def Packets(self, complete: bool = True) -> IFSelect_PacketList:
        """
        Returns the list of recorded Packets, under two modes :
        - <complete> = False, the strict definition of Packets, i.e.
        for each one, the Root Entities, to be explicitly sent
        - <complete> = True (Default), the completely evaluated list,
        i.e. which really gives the destination of each entity :
        this mode allows to evaluate duplications
        Remark that to send packets, iteration remains preferable
        (file names are managed)
        """

    def NbPackets(self) -> int:
        """
        Returns the total count of produced non empty packets
        (in out : calls Evaluate as necessary)
        """

    def Prepare(self) -> None:
        """
        Prepares the iteration on the packets
        This method is called by Evaluate, but can be called anytime
        The iteration consists in taking each Dispatch of the ShareOut
        beginning by the first one, compute its packets, then iterate
        on these packets. Once all these packets are iterated, the
        iteration passes to the next Dispatch, or stops.
        For a creation from a unique Dispatch, same but with only
        this Dispatch.
        Each packet can be listed, or really transferred (producing
        a derived Model, from which a file can be generated)

        Prepare sets the iteration to the first Dispatch, first Packet
        """

    def More(self) -> bool:
        """
        Returns True if there is more packets in the current Dispatch,
        else if there is more Dispatch in the ShareOut
        """

    def Next(self) -> None:
        """
        Passes to the next Packet in the current Dispatch, or if there
        is none, to the next Dispatch in the ShareOut
        """

    def NextDispatch(self) -> None:
        """Passes to the next Dispatch, regardless about remaining packets"""

    def Dispatch(self) -> IFSelect_Dispatch:
        """Returns the current Dispatch"""

    def DispatchRank(self) -> int:
        """
        Returns the Rank of the current Dispatch in the ShareOut
        Returns Zero if there is none (iteration finished)
        """

    def PacketsInDispatch(self) -> tuple[int, int]:
        """
        Returns Number (rank) of current Packet in current Dispatch,
        and total count of Packets in current Dispatch, as arguments
        """

    def PacketRoot(self) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of Roots of the current Packet (never empty)
        (i.e. the Entities to be themselves asked for transfer)
        Error if there is none (iteration finished)
        """

    def PacketContent(self) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the complete content of the current Packet (i.e.
        with shared entities, which will also be put in the file)
        """

    def FileName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the File Name which corresponds to current Packet
        (computed by ShareOut)
        If current Packet has no associated name (see ShareOut),
        the returned value is Null
        """

class IFSelect_Signature(nanoocp.Interface.Interface_SignType):
    """
    Signature provides the basic service used by the classes
    SelectSignature and Counter (i.e. Name, Value), which is :
    - for an entity in a model, give a characteristic string, its
    signature
    This string has not to be unique in the model, but gives a
    value for such or such important feature.
    Examples : Dynamic Type; Category; etc
    """

    def SetIntCase(self, hasmin: bool, valmin: int, hasmax: bool, valmax: int) -> None:
        """
        Sets the information data to tell "integer cases" with
        possible min and max values
        To be called when creating
        """

    def IsIntCase(self) -> tuple[bool, bool, int, bool, int]:
        """
        Tells if this Signature gives integer values
        and returns values from SetIntCase if True
        """

    def AddCase(self, acase: str) -> None:
        """
        Adds a possible case
        To be called when creating, IF the list of possible cases for
        Value is known when starting
        For instance, for CDL types, rather do not fill this,
        but for a specific enumeration (such as a status), can be used
        """

    def CaseList(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns the predefined list of possible cases, filled by AddCase
        Null Handle if no predefined list (hence, to be counted)
        Useful to filter on really possible vase, for instance, or
        for a help
        """

    def Name(self) -> str:
        """
        Returns an identification of the Signature (a word), given at
        initialization time
        Returns the Signature for a Transient object. It is specific
        of each sub-class of Signature. For a Null Handle, it should
        provide ""
        It can work with the model which contains the entity
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        The label of a Signature uses its name as follow :
        "Signature : <name>\"
        """

    def Matches(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None, text: nanoocp.TCollection.TCollection_AsciiString, exact: bool) -> bool:
        """
        Tells if the value for <ent> in <model> matches a text, with
        a criterium <exact>.
        The default definition calls MatchValue
        Can be redefined
        """

    @staticmethod
    def MatchValue(val: str, text: nanoocp.TCollection.TCollection_AsciiString, exact: bool) -> bool:
        """
        Default procedure to tell if a value <val> matches a text
        with a criterium <exact>. <exact> = True requires equality,
        else only contained (no reg-exp)
        """

    @staticmethod
    def IntValue(val: int) -> str:
        """
        This procedure converts an Integer to a CString
        It is a convenient way when the value of a signature has the
        form of a simple integer value
        The value is to be used immediately (one buffer only, no copy)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SignType(IFSelect_Signature):
    """
    This Signature returns the cdl Type of an entity, under two
    forms :
    - complete dynamic type (package and class)
    - class type, without package name
    """

    @overload
    def __init__(self, nopk: bool = False) -> None:
        """
        Returns a SignType
        <nopk> false (D) : complete dynamic type (name = Dynamic Type)
        <nopk> true : class type without pk (name = Class Type)
        """

    @overload
    def __init__(self, theOther: IFSelect_SignType) -> None: ...

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient object, as its Dynamic
        Type, with or without package name, according starting option
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SignAncestor(IFSelect_SignType):
    @overload
    def __init__(self, nopk: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: IFSelect_SignAncestor) -> None: ...

    def Matches(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None, text: nanoocp.TCollection.TCollection_AsciiString, exact: bool) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SignCategory(IFSelect_Signature):
    """
    This Signature returns the Category of an entity, as recorded
    in the model
    """

    @overload
    def __init__(self) -> None:
        """Returns a SignCategory"""

    @overload
    def __init__(self, theOther: IFSelect_SignCategory) -> None: ...

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient object, as its Category
        recorded in the model
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SignMultiple(IFSelect_Signature):
    """
    Multiple Signature : ordered list of other Signatures
    It concatenates on a same line the result of its sub-items
    separated by sets of 3 blanks
    It is possible to define tabulations between sub-items
    Moreover, match rules are specific
    """

    @overload
    def __init__(self, name: str) -> None:
        """
        Creates an empty SignMultiple with a Name
        This name should take expected tabulations into account
        """

    @overload
    def __init__(self, theOther: IFSelect_SignMultiple) -> None: ...

    def Add(self, subsign: IFSelect_Signature | None, width: int = 0, maxi: bool = False) -> None:
        """
        Adds a Signature. Width, if given, gives the tabulation
        If <maxi> is True, it is a forced tabulation (overlength is
        replaced by a final dot)
        If <maxi> is False, just 3 blanks follow an overlength
        """

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Concatenates the values of sub-signatures, with their
        tabulations
        """

    def Matches(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None, text: nanoocp.TCollection.TCollection_AsciiString, exact: bool) -> bool:
        """
        Specialized Match Rule
        If <exact> is False, simply checks if at least one sub-item
        matches
        If <exact> is True, standard match with Value
        (i.e. tabulations must be respected)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_SignValidity(IFSelect_Signature):
    """
    This Signature returns the Validity Status of an entity, as
    deducted from data in the model : it can be
    "OK" "Unknown" "Unloaded" "Syntactic Fail"(but loaded)
    "Syntactic Warning" "Semantic Fail" "Semantic Warning\"
    """

    @overload
    def __init__(self) -> None:
        """Returns a SignValidity"""

    @overload
    def __init__(self, theOther: IFSelect_SignValidity) -> None: ...

    @staticmethod
    def CVal(ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient object, as a validity
        deducted from data (reports) stored in the model.
        Class method, can be called by any one
        """

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient object, as a validity
        deducted from data (reports) stored in the model
        Calls the class method CVal
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_Transformer(nanoocp.Standard.Standard_Transient):
    """
    A Transformer defines the way an InterfaceModel is transformed
    (without sending it to a file).
    In order to work, each type of Transformer defines it method
    Perform, it can be parametred as needed.

    It receives a Model (the data set) as input. It then can :
    - edit this Model on the spot
    (i.e. alter its content: by editing entities, or adding/replacing some ...)
    - produce a copied Model, which detains the needed changes
    (typically on the same type, but some or all entities being
    rebuilt or converted; or converted from a protocol to another one)
    """

    def Perform(self, G: nanoocp.Interface.Interface_Graph, protocol: nanoocp.Interface.Interface_Protocol | None, checks: nanoocp.Interface.Interface_CheckIterator) -> tuple[bool, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Performs a Transformation (defined by each sub-class) :
        <G> gives the input data (especially the starting model) and
        can be used for queries (by Selections, etc...)
        <protocol> allows to work with General Services as necessary
        (it applies to input data)
        If the change corresponds to a conversion to a new protocol,
        see also the method ChangeProtocol
        <checks> stores produced checks messages if any
        <newmod> gives the result of the transformation :
        - if it is Null (i.e. has not been affected), the transformation
        has been made on the spot, it is assumed to cause no change
        to the graph of dependences
        - if it equates the starting Model, it has been transformed on
        the spot (possibly some entities were replaced inside it)
        - if it is new, it corresponds to a new data set which replaces
        the starting one

        <me> is mutable to allow results for ChangeProtocol to be
        memorized if needed, and to store information useful for
        the method Updated

        Returns True if Done, False if an Error occurred:
        in this case, if a new data set has been produced, the transformation is ignored,
        else data may be corrupted.
        """

    def ChangeProtocol(self) -> tuple[bool, nanoocp.Interface.Interface_Protocol]:
        """
        This methods allows to declare that the Protocol applied to
        the new Model has changed. It applies to the last call to
        Perform.

        Returns True if the Protocol has changed, False else.
        The provided default keeps the starting Protocol. This method
        should be redefined as required by the effect of Perform.
        """

    def Updated(self, entfrom: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        This method allows to know what happened to a starting
        entity after the last Perform. If <entfrom> (from starting
        model) has one and only one known item which corresponds in
        the new produced model, this method must return True and
        fill the argument <entto>. Else, it returns False.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which defines the way a Transformer works
        (to identify the transformation it performs)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_TransformStandard(IFSelect_Transformer):
    """
    This class runs transformations made by Modifiers, as
    the ModelCopier does when it produces files (the same set
    of Modifiers can then be used, as to transform the starting
    Model, as at file sending time).

    First, considering the resulting model, two options :
    - modifications are made directly on the starting model
    (OnTheSpot option), or
    - data are copied by the standard service Copy, only the
    remaining (not yet sent in a file) entities are copied
    (StandardCopy option)

    If a Selection is set, it forces the list of Entities on which
    the Modifiers are applied. Else, each Modifier is considered
    its Selection. By default, it is for the whole Model

    Then, the Modifiers are sequentially applied
    If at least one Modifier "May Change Graph", or if the option
    StandardCopy is selected, the graph will be recomputed
    (by the WorkSession, see method RunTransformer)

    Remark that a TransformStandard with option StandardCopy
    and no Modifier at all has the effect of computing the
    remaining data (those not yet sent in any output file).
    Moreover, the Protocol is not changed
    """

    @overload
    def __init__(self) -> None:
        """Creates a TransformStandard, option StandardCopy, no Modifier"""

    @overload
    def __init__(self, theOther: IFSelect_TransformStandard) -> None: ...

    def SetCopyOption(self, option: bool) -> None:
        """
        Sets the Copy option to a new value :
        True for StandardCopy. False for OnTheSpot
        """

    def CopyOption(self) -> bool:
        """Returns the Copy option"""

    def SetSelection(self, sel: IFSelect_Selection | None) -> None:
        """
        Sets a Selection (or unsets if Null)
        This Selection then defines the list of entities on which the
        Modifiers will be applied
        If it is set, it has priority on Selections of Modifiers
        Else, for each Modifier its Selection is evaluated
        By default, all the Model is taken
        """

    def Selection(self) -> IFSelect_Selection:
        """Returns the Selection, Null by default"""

    def NbModifiers(self) -> int:
        """Returns the count of recorded Modifiers"""

    def Modifier(self, num: int) -> IFSelect_Modifier:
        """Returns a Modifier given its rank in the list"""

    def ModifierRank(self, modif: IFSelect_Modifier | None) -> int:
        """Returns the rank of a Modifier in the list, 0 if unknown"""

    def AddModifier(self, modif: IFSelect_Modifier | None, atnum: int = 0) -> bool:
        """
        Adds a Modifier to the list :
        - <atnum> = 0 (default) : at the end of the list
        - <atnum> > 0 : at rank <atnum>
        Returns True if done, False if <atnum> is out of range
        """

    @overload
    def RemoveModifier(self, modif: IFSelect_Modifier | None) -> bool:
        """
        Removes a Modifier from the list
        Returns True if done, False if <modif> not in the list
        """

    @overload
    def RemoveModifier(self, num: int) -> bool:
        """
        Removes a Modifier from the list, given its rank
        Returns True if done, False if <num> is out of range
        """

    def Perform(self, G: nanoocp.Interface.Interface_Graph, protocol: nanoocp.Interface.Interface_Protocol | None, checks: nanoocp.Interface.Interface_CheckIterator) -> tuple[bool, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Performs the Standard Transformation, by calling Copy then
        ApplyModifiers (which can return an error status)
        """

    def Copy(self, G: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        This the first operation. It calls StandardCopy or OnTheSpot
        according the option
        Performs the copy operation. Calls StandardCopy or OnTheSpot
        according to the copy option.
        @param[in] G the interface graph
        @param[in,out] TC the copy tool
        @return the new model produced by the copy
        """

    def Copy__Interface_InterfaceModel(self, G: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Copy__Interface_InterfaceModel: the C++ overload Copy(const Interface_Graph &, Interface_CopyTool &, occ::handle<Interface_InterfaceModel> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use Copy() returning handle by value instead

        @deprecated Use Copy() returning handle by value instead.
        """

    def StandardCopy(self, G: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        This is the standard action of Copy : its takes into account
        only the remaining entities (noted by Graph Status positive)
        and their proper dependences of course. Produces a new model.
        Performs a standard copy of remaining entities and their dependencies.
        @param[in] G the interface graph
        @param[in,out] TC the copy tool
        @return the new model with copied entities
        """

    def StandardCopy__Interface_InterfaceModel(self, G: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        StandardCopy__Interface_InterfaceModel: the C++ overload StandardCopy(const Interface_Graph &, Interface_CopyTool &, occ::handle<Interface_InterfaceModel> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use StandardCopy() returning handle by value instead

        @deprecated Use StandardCopy() returning handle by value instead.
        """

    def OnTheSpot(self, G: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        This is the OnTheSpot action : each entity is bound with ...
        itself. The produced model is the same as the starting one.
        Performs the on-the-spot action: each entity is bound with itself.
        The produced model is the same as the starting one.
        @param[in] G the interface graph
        @param[in,out] TC the copy tool
        @return the starting model (same instance)
        """

    def OnTheSpot__Interface_InterfaceModel(self, G: nanoocp.Interface.Interface_Graph, TC: nanoocp.Interface.Interface_CopyTool) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        OnTheSpot__Interface_InterfaceModel: the C++ overload OnTheSpot(const Interface_Graph &, Interface_CopyTool &, occ::handle<Interface_InterfaceModel> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use OnTheSpot() returning handle by value instead

        @deprecated Use OnTheSpot() returning handle by value instead.
        """

    def ApplyModifiers(self, G: nanoocp.Interface.Interface_Graph, protocol: nanoocp.Interface.Interface_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool, checks: nanoocp.Interface.Interface_CheckIterator) -> tuple[bool, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Applies the modifiers sequentially.
        For each one, prepares required data (if a Selection is associated as a filter).
        For the option OnTheSpot, it determines if the graph may be
        changed and updates <newmod> if required
        If a Modifier causes an error (check "HasFailed"),
        ApplyModifier stops : the following Modifiers are ignored
        """

    def Updated(self, entfrom: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        This methods allows to know what happened to a starting
        entity after the last Perform. It reads result from the map
        which was filled by Perform.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which defines the way a Transformer works :
        "On the spot edition" or "Standard Copy" followed by
        "<nn> Modifiers\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_WorkLibrary(nanoocp.Standard.Standard_Transient):
    """
    This class defines the (empty) frame which can be used to
    enrich a XSTEP set with new capabilities
    In particular, a specific WorkLibrary must give the way for
    Reading a File into a Model, and Writing a Model to a File
    Thus, it is possible to define several Work Libraries for each
    norm, but recommended to define one general class for each one :
    this general class will define the Read and Write methods.

    Also a Dump service is provided, it can produce, according the
    norm, either a parcel of a file for an entity, or any other
    kind of information relevant for the norm,
    """

    def ReadFile(self, name: str, protocol: nanoocp.Interface.Interface_Protocol | None) -> tuple[int, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Gives the way to Read a File and transfer it to a Model
        <mod> is the resulting Model, which has to be created by this
        method. In case of error, <mod> must be returned Null
        Return value is a status with free values.
        Simply, 0 is for "Execution OK"
        The Protocol can be used to work (e.g. create the Model, read
        and recognize the Entities)
        """

    def ReadStream(self, theName: str, theIStream: TextIO, protocol: nanoocp.Interface.Interface_Protocol | None) -> tuple[int, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Interface to read a data from the specified stream.
        @param model is the resulting Model, which has to be created by this method.
        In case of error, model must be returned Null
        Return value is a status: 0 - OK, 1 - read failure, -1 - stream failure.

        Default implementation returns 1 (error).
        """

    def WriteFile(self, ctx: IFSelect_ContextWrite) -> bool:
        """
        Gives the way to Write a File from a Model.
        <ctx> contains all necessary information : the model, the
        protocol, the file name, and the list of File Modifiers to be
        applied, also with restricted list of selected entities for
        each one, if required.
        In return, it brings the produced check-list

        The WorkLibrary has to query <applied> to get then run the
        ContextWrite by looping like this (example) :
        for (numap = 1; numap <= ctx.NbModifiers(); numap ++) {
        ctx.SetModifier (numap);
        cast ctx.FileModifier()  to specific type -> variable filemod
        if (!filemod.IsNull()) filemod->Perform (ctx,writer);
        filemod then works with ctx. It can, either act on the
        model itself (for instance on its header), or iterate
        on selected entities (Start/Next/More/Value)
        it can call AddFail or AddWarning, as necessary
        }
        """

    def CopyModel(self, original: nanoocp.Interface.Interface_InterfaceModel | None, newmodel: nanoocp.Interface.Interface_InterfaceModel | None, list: nanoocp.Interface.Interface_EntityIterator, TC: nanoocp.Interface.Interface_CopyTool) -> bool:
        """
        Performs the copy of entities from an original model to a new
        one. It must also copy headers if any. Returns True when done.
        The provided default works by copying the individual entities
        designated in the list, by using the general service class
        CopyTool.
        It can be redefined for a norm which, either implements Copy
        by another way (do not forget to Bind each copied result with
        its original entity in TC) and returns True, or does not know
        how to copy and returns False
        """

    @overload
    def DumpEntity(self, model: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, entity: nanoocp.Standard.Standard_Transient | None, level: int) -> str:
        """
        Gives the way of dumping an entity under a form comprehensive
        for each norm. <model> helps to identify, number ... entities.
        <level> is to be interpreted for each norm (because of the
        formats which can be very different)
        """

    @overload
    def DumpEntity(self, model: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, entity: nanoocp.Standard.Standard_Transient | None) -> str:
        """Calls deferred DumpEntity with the recorded default level"""

    def SetDumpLevels(self, def_: int, max: int) -> None:
        """
        Records a default level and a maximum value for level
        level for DumpEntity can go between 0 and <max>
        default value will be <def>
        """

    def DumpLevels(self) -> tuple[int, int]:
        """
        Returns the recorded default and maximum dump levels
        If none was recorded, max is returned negative, def as zero
        """

    def SetDumpHelp(self, level: int, help: str) -> None:
        """Records a short line of help for a level (0 - max)"""

    def DumpHelp(self, level: int) -> str:
        """Returns the help line recorded for <level>, or an empty string"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IFSelect_WorkSession(nanoocp.Standard.Standard_Transient):
    """
    This class can be used to simply manage a process such as
    splitting a file, extracting a set of Entities ...
    It allows to manage different types of Variables : Integer or
    Text Parameters, Selections, Dispatches, in addition to a
    ShareOut. To each of these variables, a unique Integer
    Identifier is attached. A Name can be attached too as desired.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a Work Session
        It provides default, empty ShareOut and ModelCopier, which can
        be replaced (if required, should be done just after creation).
        """

    @overload
    def __init__(self, theOther: IFSelect_WorkSession) -> None: ...

    def SetErrorHandle(self, toHandle: bool) -> None:
        """Changes the Error Handler status (by default, it is not set)"""

    def ErrorHandle(self) -> bool:
        """Returns the Error Handler status"""

    def ShareOut(self) -> IFSelect_ShareOut:
        """Returns the ShareOut defined at creation time"""

    def SetShareOut(self, shareout: IFSelect_ShareOut | None) -> None:
        """
        Sets a new ShareOut. Fills Items which its content
        Warning : data from the former ShareOut are lost
        """

    def SetModeStat(self, theMode: bool) -> None:
        """
        Set value of mode responsible for presence of selections after loading
        If mode set to true that different selections will be accessible after loading
        else selections will be not accessible after loading( for economy memory in applications)
        """

    def GetModeStat(self) -> bool:
        """Return value of mode defining of filling selection during loading"""

    def SetLibrary(self, theLib: IFSelect_WorkLibrary | None) -> None:
        """Sets a WorkLibrary, which will be used to Read and Write Files"""

    def WorkLibrary(self) -> IFSelect_WorkLibrary:
        """
        Returns the WorkLibrary. Null Handle if not yet set
        should be C++ : return const &
        """

    def SetProtocol(self, protocol: nanoocp.Interface.Interface_Protocol | None) -> None:
        """
        Sets a Protocol, which will be used to determine Graphs, to
        Read and to Write Files
        """

    def Protocol(self) -> nanoocp.Interface.Interface_Protocol:
        """
        Returns the Protocol. Null Handle if not yet set
        should be C++ : return const &
        """

    def SetSignType(self, signtype: IFSelect_Signature | None) -> None:
        """
        Sets a specific Signature to be the SignType, i.e. the
        Signature which will determine TypeName from the Model
        (basic function). It is recorded in the GTool
        This Signature is also set as "xst-sign-type" (reserved name)
        """

    def SignType(self) -> IFSelect_Signature:
        """Returns the current SignType"""

    def HasModel(self) -> bool:
        """Returns True is a Model has been set"""

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None, clearpointed: bool = True) -> None:
        """
        Sets a Model as input : this will be the Model from which the
        ShareOut will work
        if <clearpointed> is True (default) all SelectPointed items
        are cleared, else they must be managed by the caller
        Remark : SetModel clears the Graph, recomputes it if a
        Protocol is set and if the Model is not empty, of course
        """

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Returns the Model of the Work Session (Null Handle if none)
        should be C++ : return const &
        """

    def SetLoadedFile(self, theFileName: str) -> None:
        """
        Stores the filename used for read for setting the model
        It is cleared by SetModel and ClearData(1)
        """

    def LoadedFile(self) -> str:
        """
        Returns the filename used to load current model
        empty if unknown
        """

    def ReadFile(self, filename: str) -> IFSelect_ReturnStatus:
        """
        Reads a file with the WorkLibrary (sets Model and LoadedFile)
        Returns a integer status which can be :
        RetDone if OK, RetVoid if no Protocol not defined,
        RetError for file not found, RetFail if fail during read
        """

    def ReadStream(self, theName: str, theIStream: TextIO) -> IFSelect_ReturnStatus:
        """
        Reads a file from stream with the WorkLibrary (sets Model and LoadedFile)
        Returns a integer status which can be :
        RetDone if OK, RetVoid if no Protocol not defined,
        RetError for file not found, RetFail if fail during read
        """

    def NbStartingEntities(self) -> int:
        """Returns the count of Entities stored in the Model, or 0"""

    def StartingEntity(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an Entity stored in the Model of the WorkSession
        (Null Handle is no Model or num out of range)
        """

    def StartingNumber(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the Number of an Entity in the Model
        (0 if no Model set or <ent> not in the Model)
        """

    def NumberFromLabel(self, val: str, afternum: int = 0) -> int:
        """
        From a given label in Model, returns the corresponding number
        Starts from first entity by Default, may start after a given
        number : this number may be given negative, its absolute value
        is then considered. Hence a loop on NumberFromLabel may be
        programmed (stop test is : returned value positive or null)

        Returns 0 if not found, < 0 if more than one found (first
        found in negative).
        If <val> just gives an integer value, returns it
        """

    def EntityLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the label for <ent>, as the Model does
        If <ent> is not in the Model or if no Model is loaded, a Null
        Handle is returned
        """

    def EntityName(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the Name of an Entity
        This Name is computed by the general service Name
        Returns a Null Handle if fails
        """

    def CategoryNumber(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the Category Number determined for an entity
        it is computed by the class Category
        An unknown entity (number 0) gives a value -1
        """

    def CategoryName(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Returns the Category Name determined for an entity
        it is computed by the class Category
        Remark : an unknown entity gives an empty string
        """

    def ValidityName(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Returns the Validity Name determined for an entity
        it is computed by the class SignValidity
        Remark : an unknown entity gives an empty string
        """

    def ClearData(self, mode: int) -> None:
        """
        Clears recorded data (not the items) according mode :
        1 : all Data : Model, Graph, CheckList, + ClearData 4
        2 : Graph and CheckList (they will then be recomputed later)
        3 : CheckList (it will be recomputed by ComputeCheck)
        4 : just content of SelectPointed and Counters
        Plus 0 : does nothing but called by SetModel
        ClearData is virtual, hence it can be redefined to clear
        other data of a specialised Work Session
        """

    def ComputeGraph(self, enforce: bool = False) -> bool:
        """
        Computes the Graph used for Selections, Displays ...
        If a HGraph is already set, with same model as given by method
        Model, does nothing. Else, computes a new Graph.
        If <enforce> is given True, computes a new Graph anyway.
        Remark that a call to ClearGraph will cause ComputeGraph to
        really compute a new Graph
        Returns True if Graph is OK, False else (i.e. if no Protocol
        is set, or if Model is absent or empty).
        """

    def HGraph(self) -> nanoocp.Interface.Interface_HGraph:
        """Returns the Computed Graph as HGraph (Null Handle if not set)"""

    def Graph(self) -> nanoocp.Interface.Interface_Graph:
        """Returns the Computed Graph, for Read only"""

    def Shareds(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities shared by <ent> (can be empty)
        Returns a null Handle if <ent> is unknown
        """

    def Sharings(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities sharing <ent> (can be empty)
        Returns a null Handle if <ent> is unknown
        """

    def IsLoaded(self) -> bool:
        """
        Returns True if a Model is defined and really loaded (not
        empty), a Protocol is set and a Graph has been computed.
        In this case, the WorkSession can start to work
        """

    def ComputeCheck(self, enforce: bool = False) -> bool:
        """
        Computes the CheckList for the Model currently loaded
        It can then be used for displays, queries ...
        Returns True if OK, False else (i.e. no Protocol set, or Model
        absent). If <enforce> is False, works only if not already done
        or if a new Model has been loaded from last call.
        Remark : computation is enforced by every call to
        SetModel or RunTransformer
        """

    def ModelCheckList(self, complete: bool = True) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the Check List for the Model currently loaded :
        <complete> = True  : complete (syntactic & semantic messages),
        computed if not yet done
        <complete> = False : only syntactic (check file form)
        """

    def CheckOne(self, ent: nanoocp.Standard.Standard_Transient | None, complete: bool = True) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns a Check for a single entity, under the form of a
        CheckIterator (this gives only one form for the user)
        if <ent> is Null or equates the current Model, it gives the
        Global Check, else the Check for the given entity
        <complete> as for ModelCheckList
        """

    def LastRunCheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the Check List produced by the last execution of
        either : EvaluateFile(for Split), SendSplit, SendAll,
        SendSelected, RunTransformer-RunModifier
        Cleared by SetModel or ClearData(1)
        The field is protected, hence a specialized WorkSession may
        fill it
        """

    def MaxIdent(self) -> int:
        """
        Returns the Maximum Value for an Item Identifier. It can be
        greater to the count of known Items, because some can have
        been removed
        """

    def Item(self, id: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an Item, given its Ident. Returns a Null Handle if
        no Item corresponds to this Ident.
        """

    def ItemIdent(self, item: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the Ident attached to an Item in the WorkSession, or
        Zero if it is unknown
        """

    @overload
    def NamedItem(self, name: str) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Item which corresponds to a Variable, given its
        Name (whatever the type of this Item).
        Returns a Null Handle if this Name is not recorded
        """

    @overload
    def NamedItem(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.Standard.Standard_Transient:
        """
        Same as above, but <name> is given through a Handle
        Especially useful with methods SelectionNames, etc...
        """

    def NameIdent(self, name: str) -> int:
        """Returns the Ident attached to a Name, 0 if name not recorded"""

    def HasName(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Returns True if an Item of the WorkSession has an attached Name"""

    def Name(self, item: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the Name attached to an Item as a Variable of this
        WorkSession. If <item> is Null or not recorded, returns an
        empty string.
        """

    def AddItem(self, item: nanoocp.Standard.Standard_Transient | None, active: bool = True) -> int:
        """
        Adds an Item and returns its attached Ident. Does nothing
        if <item> is already recorded (and returns its attached Ident)
        <active> if True commands call to SetActive (see below)
        Remark : the determined Ident is used if <item> is a Dispatch,
        to fill the ShareOut
        """

    def AddNamedItem(self, name: str, item: nanoocp.Standard.Standard_Transient | None, active: bool = True) -> int:
        """
        Adds an Item with an attached Name. If the Name is already
        known in the WorkSession, the older item losts it
        Returns Ident if Done, 0 else, i.e. if <item> is null
        If <name> is empty, works as AddItem (i.e. with no name)
        If <item> is already known but with no attached Name, this
        method tries to attached a Name to it
        <active> if True commands call to SetActive (see below)
        """

    def SetActive(self, item: nanoocp.Standard.Standard_Transient | None, mode: bool) -> bool:
        """
        Following the type of <item> :
        - Dispatch : Adds or Removes it in the ShareOut & FileNaming
        - GeneralModifier : Adds or Removes it for final sending
        (i.e. in the ModelCopier)
        Returns True if it did something, False else (state unchanged)
        """

    def RemoveNamedItem(self, name: str) -> bool:
        """
        Removes an Item from the Session, given its Name
        Returns True if Done, False else (Name not recorded)
        (Applies only on Item which are Named)
        """

    def RemoveName(self, name: str) -> bool:
        """
        Removes a Name without removing the Item
        Returns True if Done, False else (Name not recorded)
        """

    def RemoveItem(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Removes an Item given its Ident. Returns False if <id> is
        attached to no Item in the WorkSession. For a Named Item,
        also removes its Name.
        """

    def ClearItems(self) -> None:
        """
        Clears all the recorded Items : Selections, Dispatches,
        Modifiers, and Strings & IntParams, with their Idents & Names.
        Remark that if a Model has been loaded, it is not cleared.
        """

    def ItemLabel(self, id: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a Label which illustrates the content of an Item,
        given its Ident. This Label is :
        - for a Text Parameter, "Text:<text value>"
        - for an Integer Parameter, "Integer:<integer value>"
        - for a Selection, a Dispatch or a Modifier, its Label
        (see these classes)
        - for any other kind of Variable, its cdl type
        """

    def ItemIdents(self, type: nanoocp.Standard.Standard_Type | None) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """
        Fills a Sequence with the List of Idents attached to the Items
        of which Type complies with (IsKind) <type> (alphabetic order)
        Remark : <type> = TYPE(Standard_Transient) gives all the
        Idents which are suitable in the WorkSession
        """

    def ItemNames(self, type: nanoocp.Standard.Standard_Type | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Fills a Sequence with the list of the Names attached to Items
        of which Type complies with (IsKind) <type> (alphabetic order)
        Remark : <type> = TYPE(Standard_Transient) gives all the Names
        """

    def ItemNamesForLabel(self, label: str) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Fills a Sequence with the NAMES of the control items, of which
        the label matches <label> (contain it) : see NextIdentForLabel
        Search mode is fixed to "contained"
        If <label> is empty, returns all Names
        """

    def NextIdentForLabel(self, label: str, id: int, mode: int = 0) -> int:
        """
        For query by Label with possible iterations
        Searches the Ident of which Item has a Label which matches a
        given one, the search starts from an initial Ident.
        Returns the first found Ident which follows <id>, or ZERO

        The search must start with <id> = 0, it returns the next Ident
        which matches. To iterate, call again this method which this
        returned value as <id>. Once an Ident has been returned, the
        Item can be obtained by the method Item

        <mode> precises the required matching mode :
        - 0 (Default) : <label> must match exactly with the Item Label
        - 1 : <label> must match the exact beginning (the end is free)
        - 2 : <label> must be at least once wherever in the Item Label
        - other values are ignored
        """

    def NewParamFromStatic(self, statname: str, name: str = '') -> nanoocp.Standard.Standard_Transient:
        """
        Creates a parameter as being bound to a Static
        If the Static is Integer, this creates an IntParam bound to
        it by its name. Else this creates a String which is the value
        of the Static.
        Returns a null handle if <statname> is unknown as a Static
        """

    def IntParam(self, id: int) -> IFSelect_IntParam:
        """
        Returns an IntParam, given its Ident in the Session
        Null result if <id> is not suitable for an IntParam
        (undefined, or defined for another kind of variable)
        """

    def IntValue(self, it: IFSelect_IntParam | None) -> int:
        """Returns Integer Value of an IntParam"""

    def NewIntParam(self, name: str = '') -> IFSelect_IntParam:
        """
        Creates a new IntParam. A Name can be set (Optional)
        Returns the created IntParam, or a Null Handle in case of
        Failure (see AddItem/AddNamedItem)
        """

    def SetIntValue(self, it: IFSelect_IntParam | None, val: int) -> bool:
        """
        Changes the Integer Value of an IntParam
        Returns True if Done, False if <it> is not in the WorkSession
        """

    def TextParam(self, id: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a TextParam, given its Ident in the Session
        Null result if <id> is not suitable for a TextParam
        (undefined, or defined for another kind of variable)
        """

    def TextValue(self, par: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns Text Value of a TextParam (a String)
        or an empty string if <it> is not in the WorkSession
        """

    def NewTextParam(self, name: str = '') -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Creates a new (empty) TextParam. A Name can be set (Optional)
        Returns the created TextParam (as an HAsciiString), or a Null
        Handle in case of Failure (see AddItem/AddNamedItem)
        """

    def SetTextValue(self, par: nanoocp.TCollection.TCollection_HAsciiString | None, val: str) -> bool:
        """
        Changes the Text Value of a TextParam (an HAsciiString)
        Returns True if Done, False if <it> is not in the WorkSession
        """

    def Signature(self, id: int) -> IFSelect_Signature:
        """
        Returns a Signature, given its Ident in the Session
        Null result if <id> is not suitable for a Signature
        (undefined, or defined for another kind of variable)
        """

    def SignValue(self, sign: IFSelect_Signature | None, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Returns the Value computed by a Signature for an Entity
        Returns an empty string if the entity does not belong to the
        loaded model
        """

    def Selection(self, id: int) -> IFSelect_Selection:
        """
        Returns a Selection, given its Ident in the Session
        Null result if <id> is not suitable for a Selection
        (undefined, or defined for another kind of variable)
        """

    def EvalSelection(self, sel: IFSelect_Selection | None) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Evaluates the effect of a Selection applied on the input Model
        Returned Result remains empty if no input Model has been set
        """

    def Sources(self, sel: IFSelect_Selection | None) -> IFSelect_SelectionIterator:
        """
        Returns the Selections which are source of Selection, given
        its rank in the List of Selections (see SelectionIterator)
        Returned value is empty if <num> is out of range or if
        <sel> is not in the WorkSession
        """

    def SelectionResult(self, sel: IFSelect_Selection | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the result of a Selection, computed by EvalSelection
        (see above) under the form of a HSequence (hence, it can be
        used by a frontal-engine logic). It can be empty
        Returns a Null Handle if <sel> is not in the WorkSession
        """

    def SelectionResultFromList(self, sel: IFSelect_Selection | None, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the result of a Selection, by forcing its input with
        a given list <list> (unless <list> is Null).
        RULES :
        <list> applies only for a SelectDeduct kind Selection :
        its Input is considered : if it is a SelectDeduct kind
        Selection, its Input is considered, etc... until an Input
        is not a Deduct/Extract : its result is replaced by <list>
        and all the chain of deductions is applied
        """

    def SetItemSelection(self, item: nanoocp.Standard.Standard_Transient | None, sel: IFSelect_Selection | None) -> bool:
        """
        Sets a Selection as input for an item, according its type :
        if <item> is a Dispatch : as Final Selection
        if <item> is a GeneralModifier (i.e. any kind of Modifier) :
        as Selection used to filter entities to modify
        <sel> Null causes this Selection to be nullified
        Returns False if <item> is not of a suitable type, or
        <item> or <sel> is not in the WorkSession
        """

    def ResetItemSelection(self, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Resets input Selection which was set by SetItemSelection
        Same conditions as for SetItemSelection
        Returns True if done, False if <item> is not in the WorkSession
        """

    def ItemSelection(self, item: nanoocp.Standard.Standard_Transient | None) -> IFSelect_Selection:
        """
        Returns the Selection of a Dispatch or a GeneralModifier.
        Returns a Null Handle if none is defined or <item> not good type
        """

    def SignCounter(self, id: int) -> IFSelect_SignCounter:
        """
        Returns a SignCounter from its ident in the Session
        Null result if <id> is not suitable for a SignCounter
        (undefined, or defined for another kind of variable)
        """

    def ComputeCounter(self, counter: IFSelect_SignCounter | None, forced: bool = False) -> bool:
        """
        Computes the content of a SignCounter when it is defined with
        a Selection, then returns True
        Returns False if the SignCounter is not defined with a
        Selection, or if its Selection Mode is inhibited
        <forced> to work around optimisations
        """

    def ComputeCounterFromList(self, counter: IFSelect_SignCounter | None, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, clear: bool = True) -> bool:
        """
        Computes the content of a SignCounter from an input list
        If <list> is Null, uses internal definition of the Counter :
        a Selection, else the whole Model (recomputation forced)
        If <clear> is True (D), starts from scratch
        Else, cumulates computations
        """

    def AppliedDispatches(self) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """Returns the ordered list of dispatches stored by the ShareOut"""

    def ClearShareOut(self, onlydisp: bool) -> None:
        """
        Clears the list of Dispatches recorded by the ShareOut
        if <only> disp is True, tha's all. Else, clears also the lists
        of Modifiers recorded by the ShareOut
        """

    def Dispatch(self, id: int) -> IFSelect_Dispatch:
        """
        Returns a Dispatch, given its Ident in the Session
        Null result if <id> is not suitable for a Dispatch
        (undefined, or defined for another kind of variable)
        """

    def DispatchRank(self, disp: IFSelect_Dispatch | None) -> int:
        """
        Returns the rank of a Dispatch in the ShareOut, or 0 if <disp>
        is not in the ShareOut or not in the WorkSession
        """

    def ModelCopier(self) -> IFSelect_ModelCopier:
        """Gives access to the complete ModelCopier"""

    def SetModelCopier(self, copier: IFSelect_ModelCopier | None) -> None:
        """Sets a new ModelCopier. Fills Items which its content"""

    def NbFinalModifiers(self, formodel: bool) -> int:
        """
        Returns the count of Modifiers applied to final sending
        Model Modifiers if <formodel> is True, File Modifiers else
        (i.e. Modifiers which apply once the Models have been filled)
        """

    def FinalModifierIdents(self, formodel: bool) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """
        Fills a Sequence with a list of Idents, those attached to
        the Modifiers applied to final sending.
        Model Modifiers if <formodel> is True, File Modifiers else
        This list is given in the order in which they will be applied
        (which takes into account the Changes to Modifier Ranks)
        """

    def GeneralModifier(self, id: int) -> IFSelect_GeneralModifier:
        """
        Returns a Modifier, given its Ident in the Session
        Null result if <id> is not suitable for a Modifier
        (undefined, or defined for another kind of variable)
        """

    def ModelModifier(self, id: int) -> IFSelect_Modifier:
        """
        Returns a Model Modifier, given its Ident in the Session,
        i.e. typed as a Modifier (not simply a GeneralModifier)
        Null result if <id> is not suitable for a Modifier
        (undefined, or defined for another kind of variable)
        """

    def ModifierRank(self, item: IFSelect_GeneralModifier | None) -> int:
        """
        Returns the Rank of a Modifier given its Ident. Model or File
        Modifier according its type (ModelModifier or not)
        Remember that Modifiers are applied sequentially following
        their Rank : first Model Modifiers then File Modifiers
        Rank is given by rank of call to AddItem and can be
        changed by ChangeModifierRank
        """

    def ChangeModifierRank(self, formodel: bool, before: int, after: int) -> bool:
        """
        Changes the Rank of a Modifier in the Session :
        Model Modifiers if <formodel> is True, File Modifiers else
        the Modifier n0 <before> is put to n0 <after>
        Return True if Done, False if <before> or <after> out of range
        """

    def ClearFinalModifiers(self) -> None:
        """
        Removes all the Modifiers active in the ModelCopier : they
        become inactive and they are removed from the Session
        """

    def SetAppliedModifier(self, modif: IFSelect_GeneralModifier | None, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Sets a GeneralModifier to be applied to an item :
        - item = ShareOut : applies for final sending (all dispatches)
        - item is a Dispatch : applies for this dispatch only
        Returns True if done, False if <modif> or <item> not in <me>
        """

    def ResetAppliedModifier(self, modif: IFSelect_GeneralModifier | None) -> bool:
        """
        Resets a GeneralModifier to be applied
        Returns True if done, False if <modif> was not applied
        """

    def UsesAppliedModifier(self, modif: IFSelect_GeneralModifier | None) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the item on which a GeneralModifier is applied :
        the ShareOut, or a given Dispatch
        Returns a Null Handle if <modif> is not applied
        """

    def Transformer(self, id: int) -> IFSelect_Transformer:
        """
        Returns a Transformer, given its Ident in the Session
        Null result if <id> is not suitable for a Transformer
        (undefined, or defined for another kind of variable)
        """

    def RunTransformer(self, transf: IFSelect_Transformer | None) -> int:
        """
        Runs a Transformer on starting Model, which can then be edited
        or replaced by a new one. The Protocol can also be changed.
        Fills LastRunCheckList

        Returned status is 0 if nothing done (<transf> or model
        undefined), positive if OK, negative else :
        0  : Nothing done
        1  : OK, edition on the spot with no change to the graph
        of dependencies (purely local)
        2  : OK, model edited on the spot (graph recomputed, may
        have changed), protocol unchanged
        3  : OK, new model produced, same protocol
        4  : OK, model edited on the spot (graph recomputed),
        but protocol has changed
        5  : OK, new model produced, protocol has changed
        -1 : Error on the spot (slight changes), data may be corrupted
        (remark : corruption should not be profound)
        -2 : Error on edition the spot, data may be corrupted
        (checking them is recommended)
        -3 : Error with a new data set, transformation ignored
        -4 : OK as 4, but graph of dependences count not be recomputed
        (the former one is kept) : check the protocol
        """

    def RunModifier(self, modif: IFSelect_Modifier | None, copy: bool) -> int:
        """
        Runs a Modifier on Starting Model. It can modify entities, or
        add new ones. But the Model or the Protocol is unchanged.
        The Modifier is applied on each entity of the Model. See also
        RunModifierSelected
        Fills LastRunCheckList

        <copy> : if True, a new data set is produced which brings
        the modifications (Model + its Entities)
        if False, data are modified on the spot

        It works through a TransformStandard defined with <modif>
        Returned status as RunTransformer : 0 nothing done, >0 OK,
        <0 problem, but only between -3 and 3 (protocol unchanged)
        Remark : <copy> True will give <effect> = 3 or -3
        """

    def RunModifierSelected(self, modif: IFSelect_Modifier | None, sel: IFSelect_Selection | None, copy: bool) -> int:
        """
        Acts as RunModifier, but the Modifier is applied on the list
        determined by a Selection, rather than on the whole Model
        If the selection is a null handle, the whole model is taken
        """

    def NewTransformStandard(self, copy: bool, name: str = '') -> IFSelect_Transformer:
        """
        Creates and returns a TransformStandard, empty, with its
        Copy Option (True = Copy, False = On the Spot) and an
        optional name.
        To a TransformStandard, the method SetAppliedModifier applies
        """

    def SetModelContent(self, sel: IFSelect_Selection | None, keep: bool) -> bool:
        """
        Defines a new content from the former one
        If <keep> is True, it is given by entities selected by
        Selection <sel> (and all shared entities)
        Else, it is given by all the former content but entities
        selected by the Selection <sel> (and properly shared ones)
        Returns True if done. Returns False if the selected list
        (from <sel>) is empty, hence nothing is done
        """

    def FilePrefix(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the defined File Prefix. Null Handle if not defined"""

    def DefaultFileRoot(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the defined Default File Root. It is used for
        Dispatches which have no specific root attached.
        Null Handle if not defined
        """

    def FileExtension(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the defined File Extension. Null Handle if not defined"""

    def FileRoot(self, disp: IFSelect_Dispatch | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the File Root defined for a Dispatch. Null if no
        Root Name is defined for it (hence, no File will be produced)
        """

    def SetFilePrefix(self, name: str) -> None:
        """Defines a File Prefix"""

    def SetDefaultFileRoot(self, name: str) -> bool:
        """
        Defines a Default File Root Name. Clears it is <name> = ""
        Returns True if OK, False if <name> already set for a Dispatch
        """

    def SetFileExtension(self, name: str) -> None:
        """Defines a File Extension"""

    def SetFileRoot(self, disp: IFSelect_Dispatch | None, name: str) -> bool:
        """
        Defines a Root for a Dispatch
        If <name> is empty, clears Root Name
        This has as effect to inhibit the production of File by <disp>
        Returns False if <disp> is not in the WorkSession or if a
        root name is already defined for it
        """

    def GiveFileRoot(self, file: str) -> str:
        """
        Extracts File Root Name from a given complete file name
        (uses OSD_Path)
        """

    def GiveFileComplete(self, file: str) -> str:
        """
        Completes a file name as required, with Prefix and Extension
        (if defined; for a non-defined item, completes nothing)
        """

    def ClearFile(self) -> None:
        """
        Erases all stored data from the File Evaluation
        (i.e. ALL former naming information are lost)
        """

    def EvaluateFile(self) -> None:
        """
        Performs and stores a File Evaluation. The Results are a List
        of produced Models and a List of names (Strings), in parallel
        Fills LastRunCheckList
        """

    def NbFiles(self) -> int:
        """Returns the count of produced Models"""

    def FileModel(self, num: int) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns a Model, given its rank in the Evaluation List"""

    def FileName(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the name of a file corresponding to a produced Model,
        given its rank in the Evaluation List
        """

    def BeginSentFiles(self, record: bool) -> None:
        """
        Commands file sending to clear the list of already sent files,
        commands to record a new one if <record> is True
        This list is managed by the ModelCopier when SendSplit is called
        It allows a global exploitation of the set of sent files
        """

    def SentFiles(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of recorded sent files, or a Null Handle is
        recording has not been enabled
        """

    def SendSplit(self) -> bool:
        """
        Performs creation of derived files from the input Model
        Takes its data (sub-models and names), from result EvaluateFile
        if active, else by dynamic Evaluation (not stored)
        After SendSplit, result of EvaluateFile is Cleared
        Fills LastRunCheckList

        Works with the WorkLibrary which acts on specific type of Model
        and can work with File Modifiers (managed by the Model Copier)
        and a ModelCopier, which can work with Model Modifiers
        Returns False if, either WorkLibrary has failed on at least
        one sub-file, or the Work Session is badly conditioned
        (no Model defined, or FileNaming not in phase with ShareOut)
        """

    def EvalSplit(self) -> IFSelect_PacketList:
        """
        Returns an Evaluation of the whole ShareOut definition : i.e.
        how the entities of the starting model are forecast to be sent
        to various files : list of packets according the dispatches,
        effective lists of roots for each packet (which determine the
        content of the corresponding file); plus evaluation of which
        entities are : forgotten (sent into no file), duplicated (sent
        into more than one file), sent into a given file.
        See the class PacketList for more details.
        """

    def SentList(self, count: int = -1) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns the list of Entities sent in files, according to the
        count of files each one has been sent (these counts are reset
        by SetModel or SetRemaining(Forget) ) stored in Graph Status
        <count> = -1 (default) is for ENtities sent at least once
        <count> = 0 is for the Remaining List (entities not yet sent)
        <count> = 1 is for entities sent in one and only one file
        (the ideal case)
        Remaining Data are computed on each Sending/Copying output
        files (see methods EvaluateFile and SendSplit)
        Graph Status is 0 for Remaining Entity, <count> for Sent into
        <count> files
        This status is set to 0 (not yet sent) for all by SetModel
        and by SetRemaining(mode=Forget,Display)
        """

    def MaxSendingCount(self) -> int:
        """
        Returns the greater count of different files in which any of
        the starting entities could be sent.
        Before any file output, this count is 0.
        Ideal count is 1. More than 1 means that duplications occur.
        """

    def SetRemaining(self, mode: IFSelect_RemainMode) -> bool:
        """
        Processes Remaining data (after having sent files), mode :
        Forget  : forget remaining info (i.e. clear all "Sent" status)
        Compute : compute and keep remaining (does nothing if :
        remaining is empty or if no files has been sent)
        Display : display entities recorded as remaining
        Undo    : restore former state of data (after Remaining(1) )
        Returns True if OK, False else (i.e. mode = 2 and Remaining
        List is either empty or takes all the entities, or mode = 3
        and no former computation of remaining data was done)
        """

    def SendAll(self, filename: str, computegraph: bool = False) -> IFSelect_ReturnStatus:
        """
        Sends the starting Model into one file, without splitting,
        managing remaining data or anything else.
        <computegraph> true commands the Graph to be recomputed before
        sending : required when a Model is filled in several steps

        The Model and File Modifiers recorded to be applied on sending
        files are.
        Returns a status of execution :
        Done if OK,
        Void if no data available,
        Error if errors occurred (work library is not defined), errors during translation
        Fail if exception during translation is raised
        Stop if no disk space or disk, file is write protected
        Fills LastRunCheckList
        """

    def SendSelected(self, filename: str, sel: IFSelect_Selection | None, computegraph: bool = False) -> IFSelect_ReturnStatus:
        """
        Sends a part of the starting Model into one file, without
        splitting. But remaining data are managed.
        <computegraph> true commands the Graph to be recomputed before
        sending : required when a Model is filled in several steps

        The Model and File Modifiers recorded to be applied on sending
        files are.
        Returns a status : Done if OK, Fail if error during send,
        Error : WorkLibrary not defined, Void : selection list empty
        Fills LastRunCheckList
        """

    @overload
    def WriteFile(self, filename: str) -> IFSelect_ReturnStatus:
        """
        Writes the current Interface Model globally to a File, and
        returns a write status which can be :
        Done OK, Fail file could not be written, Error no norm is selected
        Remark : It is a simple, one-file writing, other operations are
        available (such as splitting ...) which calls SendAll
        """

    @overload
    def WriteFile(self, filename: str, sel: IFSelect_Selection | None) -> IFSelect_ReturnStatus:
        """
        Writes a sub-part of the current Interface Model to a File,
        as defined by a Selection <sel>, recomputes the Graph, and
        returns a write status which can be :
        Done OK, Fail file could not be written, Error no norm is selected
        Remark : It is a simple, one-file writing, other operations are
        available (such as splitting ...) which calls SendSelected
        """

    def NbSources(self, sel: IFSelect_Selection | None) -> int:
        """
        Returns the count of Input Selections known for a Selection,
        or 0 if <sel> not in the WorkSession. This count is one for a
        SelectDeduct / SelectExtract kind, two for SelectControl kind,
        variable for a SelectCombine (Union/Intersection), zero else
        """

    def Source(self, sel: IFSelect_Selection | None, num: int = 1) -> IFSelect_Selection:
        """
        Returns the <num>th Input Selection of a Selection
        (see NbSources).
        Returns a Null Handle if <sel> is not in the WorkSession or if
        <num> is out of the range <1-NbSources>
        To obtain more details, see the method Sources
        """

    def IsReversedSelectExtract(self, sel: IFSelect_Selection | None) -> bool:
        """Returns True if <sel> a Reversed SelectExtract, False else"""

    def ToggleSelectExtract(self, sel: IFSelect_Selection | None) -> bool:
        """
        Toggles the Sense (Direct <-> Reversed) of a SelectExtract
        Returns True if Done, False if <sel> is not a SelectExtract or
        is not in the WorkSession
        """

    def SetInputSelection(self, sel: IFSelect_Selection | None, input: IFSelect_Selection | None) -> bool:
        """
        Sets an Input Selection (as <input>) to a SelectExtract or
        a SelectDeduct (as <sel>).
        Returns True if Done, False if <sel> is neither a
        SelectExtract nor a SelectDeduct, or not in the WorkSession
        """

    def SetControl(self, sel: IFSelect_Selection | None, sc: IFSelect_Selection | None, formain: bool = True) -> bool:
        """
        Sets an Input Selection, Main if <formain> is True, Second else
        (as <sc>) to a SelectControl (as <sel>). Returns True if Done,
        False if <sel> is not a SelectControl, or <sc> or <sel> is not
        in the WorkSession
        """

    def CombineAdd(self, selcomb: IFSelect_Selection | None, seladd: IFSelect_Selection | None, atnum: int = 0) -> int:
        """
        Adds an input selection to a SelectCombine (Union or Inters.).
        Returns new count of inputs for this SelectCombine if Done or
        0 if <sel> is not kind of SelectCombine, or if <seladd> or
        <sel> is not in the WorkSession
        By default, adding is done at the end of the list
        Else, it is an insertion to rank <atnum> (useful for Un-ReDo)
        """

    def CombineRemove(self, selcomb: IFSelect_Selection | None, selrem: IFSelect_Selection | None) -> bool:
        """
        Removes an input selection from a SelectCombine (Union or
        Intersection). Returns True if done, False if <selcomb> is not
        kind of SelectCombine or <selrem> is not source of <selcomb>
        """

    def NewSelectPointed(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, name: str) -> IFSelect_Selection:
        """
        Creates a new Selection, of type SelectPointed, its content
        starts with <list>. A name must be given (can be empty)
        """

    def SetSelectPointed(self, sel: IFSelect_Selection | None, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, mode: int) -> bool:
        """
        Changes the content of a Selection of type SelectPointed
        According <mode> : 0 set <list> as new content (clear former)
        1  : adds <list> to actual content
        -1  : removes <list> from actual content
        Returns True if done, False if <sel> is not a SelectPointed
        """

    def GiveSelection(self, selname: str) -> IFSelect_Selection:
        """
        Returns a Selection from a Name :
        - the name of a Selection : this Selection
        - the name of a Signature + criteria between (..) : a new
        Selection from this Signature
        - an entity or a list of entities : a new SelectPointed
        Else, returns a Null Handle
        """

    @overload
    def GiveList(self, obj: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Determines a list of entities from an object :
        <obj> already HSequenceOfTransient : returned itself
        <obj> Selection : its Result of Evaluation is returned
        <obj> an entity of the Model : a HSequence which contains it
        else, an empty HSequence
        <obj> the Model it self : ALL its content (not only the roots)
        """

    @overload
    def GiveList(self, first: str, second: str = '') -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Computes a List of entities from two alphanums,
        first and second, as follows :
        if <first> is a Number or Label of an entity : this entity
        if <first> is a list of Numbers/Labels : the list of entities
        if <first> is the name of a Selection in <WS>, and <second>
        not defined, the standard result of this Selection
        else, let's consider "first second" : this whole phrase is
        split by blanks, as follows (RECURSIVE CALL) :
        - the leftest term is the final selection
        - the other terms define the result of the selection
        - and so on (the "leftest minus one" is a selection, of which
        the input is given by the remaining ...)
        """

    def GiveListFromList(self, selname: str, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Computes a List of entities from the model as follows
        <first> being a Selection or a combination of Selections,
        <ent> being an entity or a list
        of entities (as a HSequenceOfTransient) :
        the standard result of this selection applied to this list
        if <ent> is Null, the standard definition of the selection is
        used (which contains a default input selection)
        if <selname> is erroneous, a null handle is returned

        REMARK : selname is processed as <first second> of preceding
        GiveList
        """

    def GiveListCombined(self, l1: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, l2: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, mode: int) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Combines two lists and returns the result, according to mode :
        <mode> < 0 : entities in <l1> AND NOT in <l2>
        <mode> = 0 : entities in <l1> AND in <l2>
        <mode> > 0 : entities in <l1> OR  in <l2>
        """

    def QueryCheckList(self, chl: nanoocp.Interface.Interface_CheckIterator) -> None:
        """Loads data from a check iterator to query status on it"""

    def QueryCheckStatus(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Determines check status for an entity regarding last call to
        QueryCheckList :
        -1 : <ent> unknown in the model, ignored
        0 : no check at all, immediate or inherited thru Graph
        1 : immediate warning (no fail), no inherited check
        2 : immediate fail, no inherited check
        +10 : idem but some inherited warning (no fail)
        +20 : idem but some inherited fail
        """

    def QueryParent(self, entdad: nanoocp.Standard.Standard_Transient | None, entson: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Determines if <entdad> is parent of <entson> (in the graph),
        returns : -1 if no; 0 if <entdad> = <entson>
        1 if immediate parent, > 1 if parent, gives count of steps
        """

    def SetParams(self, params: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.Standard.Standard_Transient], uselist: nanoocp.NCollection.NCollection_DynamicArray[int]) -> None:
        """
        Sets a list of Parameters, i.e. TypedValue, to be handled
        through an Editor
        The two lists are parallel, if <params> is longer than <uses>,
        surnumeral parameters are for general use

        EditForms are created to handle these parameters (list, edit)
        on the basis of a ParamEditor xst-params-edit

        A use number dispatches the parameter to a given EditForm
        EditForms are defined as follows
        Name                Use   Means
        xst-params          all   All Parameters (complete list)
        xst-params-general  1     Generals
        xst-params-load     2     LoadFile (no Transfer)
        xst-params-send     3     SendFile (Write, no Transfer)
        xst-params-split    4     Split
        xst-param-read      5     Transfer on Reading
        xst-param-write     6     Transfer on Writing
        """

    def TraceStatics(self, use: int, mode: int = 0) -> None:
        """
        Traces the Statics attached to a given use number
        If <use> is given positive (normal), the trace is embedded
        with a header and a trailer
        If <use> is negative, just values are printed
        (this allows to make compositions)
        Remark : use number  5 commands use -2 to be traced
        Remark : use numbers 4 and 6 command use -3 to be traced
        """

    def DumpShare(self) -> None:
        """Dumps contents of the ShareOut (on "cout")"""

    def ListItems(self, label: str = '') -> None:
        """
        Lists the Labels of all Items of the WorkSession
        If <label> is defined, lists labels which contain it
        """

    def ListFinalModifiers(self, formodel: bool) -> None:
        """
        Lists the Modifiers of the session (for each one, displays
        its Label). Listing is done following Ranks (Modifiers are
        invoked following their ranks)
        Model Modifiers if <formodel> is True, File Modifiers else
        """

    def DumpSelection(self, sel: IFSelect_Selection | None) -> None:
        """
        Lists a Selection and its Sources (see SelectionIterator),
        given its rank in the list
        """

    def DumpModel(self, level: int) -> str:
        """
        Lists the content of the Input Model (if there is one)
        According level : 0 -> gives only count of Entities and Roots
        1 -> Lists also Roots; 2 -> Lists all Entities (by TraceType)
        3 -> Performs a call to CheckList (Fails) and lists the result
        4 -> as 3 but all CheckList (Fails + Warnings)
        5,6,7  : as 3 but resp. Count,List,Labels by Fail
        8,9,10 : as 4 but resp. Count,List,Labels by message
        """

    def TraceDumpModel(self, mode: int) -> None:
        """
        Dumps the current Model (as inherited DumpModel), on currently
        defined Default Trace File (default is standard output)
        """

    def DumpEntity(self, ent: nanoocp.Standard.Standard_Transient | None, level: int) -> str:
        """
        Dumps a starting entity according to the current norm.
        To do this, it calls DumpEntity from WorkLibrary.
        <level> is to be interpreted for each norm : see specific
        classes of WorkLibrary for it. Generally, 0 if for very basic
        (only type ...), greater values give more and more details.
        """

    def PrintEntityStatus(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints main information about an entity : its number, type,
        validity (and checks if any), category, shareds and sharings..
        mutable because it can recompute checks as necessary
        """

    def TraceDumpEntity(self, ent: nanoocp.Standard.Standard_Transient | None, level: int) -> None:
        """
        Dumps an entity from the current Model as inherited DumpEntity
        on currently defined Default Trace File
        (<level> interpreted according to the Norm, see WorkLibrary)
        """

    def PrintCheckList(self, checklist: nanoocp.Interface.Interface_CheckIterator, failsonly: bool, mode: IFSelect_PrintCount) -> str:
        """
        Prints a CheckIterator to the current Trace File, controlled
        with the current Model
        complete or fails only, according to <failsonly>
        <mode> defines the mode of printing
        0 : sequential, according entities; else with a CheckCounter
        1 : according messages, count of entities
        2 : id but with list of entities, designated by their numbers
        3 : as 2 but with labels of entities
        """

    def PrintSignatureList(self, signlist: IFSelect_SignatureList | None, mode: IFSelect_PrintCount) -> str:
        """
        Prints a SignatureList to the current Trace File, controlled
        with the current Model
        <mode> defines the mode of printing (see SignatureList)
        """

    def EvaluateSelection(self, sel: IFSelect_Selection | None) -> None:
        """
        Displays the list of Entities selected by a Selection (i.e.
        the result of EvalSelection).
        """

    def EvaluateDispatch(self, disp: IFSelect_Dispatch | None, mode: int = 0) -> None:
        """
        Displays the result of applying a Dispatch on the input Model
        (also shows Remainder if there is)
        <mode> = 0 (default), displays nothing else
        <mode> = 1 : displays also duplicated entities (because of
        this dispatch)
        <mode> = 2 : displays the entities of the starting Model
        which are not taken by this dispatch (forgotten entities)
        <mode> = 3 : displays both duplicated and forgotten entities
        Remark : EvaluateComplete displays these data evaluated for
        for all the dispatches, if there are several
        """

    def EvaluateComplete(self, mode: int = 0) -> None:
        """
        Displays the effect of applying the ShareOut on the input
        Model.
        <mode> = 0 (default) : displays only roots for each packet,
        <mode> = 1 : displays all entities for each packet, plus
        duplicated entities
        <mode> = 2 : same as <mode> = 1, plus displays forgotten
        entities (which are in no packet at all)
        """

    def ListEntities(self, iter: nanoocp.Interface.Interface_EntityIterator, mode: int) -> str:
        """
        Internal method which displays an EntityIterator
        <mode> 0 gives short display (only entity numbers)
        1 gives a more complete trace (1 line per Entity)
        (can be used each time a trace has to be output from a list)
        2 gives a form suitable for givelist : (n1,n2,n3...)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IFSelect
IFSelect_TSeqOfSelection = nanoocp.NCollection.NCollection_Sequence[nanoocp.IFSelect.IFSelect_Selection]
