"""OCCT package IGESSelect (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IFGraph
import nanoocp.IFSelect
import nanoocp.IGESData
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class IGESSelect:
    """
    This package defines the library of the most used tools for
    IGES Files : Selections & Modifiers specific to the IGES norm,
    and the most needed converters
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSelect) -> None: ...

    @staticmethod
    def Run() -> None:
        """
        Simply gives a prompt for a conversational action on standard
        input/output. Returns the status of a
        """

    @staticmethod
    def WhatIges(ent: nanoocp.IGESData.IGESData_IGESEntity | None, G: nanoocp.Interface.Interface_Graph) -> tuple[int, nanoocp.IGESData.IGESData_IGESEntity, int]:
        """
        Gives a quick analysis of an IGES Entity in the context of a
        model (i.e. a File) described by a Graph.
        Returned values are :
        <sup> : the most meaningful super entity, if any (else Null)
        <index> : meaningful index relating to super entity, if any
        <returned> : a status which helps exploitation of <sup>, by
        giving a case
        (normally, types of <ent> and <sup> should suffice to
        known the case)
        """

class IGESSelect_Activator(nanoocp.IFSelect.IFSelect_Activator):
    """
    Performs Actions specific to IGESSelect, i.e. creation of
    IGES Selections and Dispatches, plus dumping specific to IGES
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSelect_Activator) -> None: ...

    def Do(self, number: int, pilot: nanoocp.IFSelect.IFSelect_SessionPilot | None) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Executes a Command Line for IGESSelect"""

    def Help(self, number: int) -> str:
        """Sends a short help message for IGESSelect commands"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_FileModifier(nanoocp.IFSelect.IFSelect_GeneralModifier):
    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite, writer: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """
        Perform the action specific to each class of File Modifier
        <ctx> is the ContextWrite, which brings : the model, the
        protocol, the file name, plus the object AppliedModifiers
        (not used here) and the CheckList
        Remark that the model has to be casted for specific access

        <writer> is the Writer and is specific to each norm, on which
        to act
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_AddFileComment(IGESSelect_FileModifier):
    """
    This class allows to add comment lines on writing an IGES File
    These lines are added to Start Section, instead of the only
    one blank line written by default.
    """

    @overload
    def __init__(self) -> None:
        """Creates a new empty AddFileComment. Use AddLine to complete it"""

    @overload
    def __init__(self, theOther: IGESSelect_AddFileComment) -> None: ...

    def Clear(self) -> None:
        """Clears the list of file comment lines already stored"""

    def AddLine(self, line: str) -> None:
        """
        Adds a line for file comment
        Remark: Lines are limited to 72 useful chars. A line of more than
        72 chars will be split into several ones of 72 max each.
        """

    def AddLines(self, lines: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        Adds a list of lines for file comment
        Each of them must comply with demand of AddLine
        """

    def NbLines(self) -> int:
        """Returns the count of stored lines"""

    def Line(self, num: int) -> str:
        """Returns a stored line given its rank"""

    def Lines(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns the complete list of lines in once"""

    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite, writer: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Sends the comment lines to the file (Start Section)"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns specific Label, which is
        "Add <nn> Comment Lines (Start Section)\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_ModelModifier(nanoocp.IFSelect.IFSelect_Modifier):
    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        The inherited Perform does the required cast (and refuses to
        go further if cast has failed) then calls the instantiated
        Performing
        """

    def PerformProtocol(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, proto: nanoocp.IGESData.IGESData_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific Perform with Protocol. It is defined to let the
        Protocol unused and to call Performing without Protocol
        (most current case). It can be redefined if specific action
        requires Protocol.
        """

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific Perform, without Protocol. If Performing with
        Protocol is redefined, Performing without Protocol must
        though be defined to do nothing (not called, but demanded
        by the linker)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_AddGroup(IGESSelect_ModelModifier):
    """
    Adds a Group to contain the entities designated by the
    Selection. If no Selection is given, nothing is done
    """

    @overload
    def __init__(self) -> None:
        """Creates an AddGroup"""

    @overload
    def __init__(self, theOther: IGESSelect_AddGroup) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Specific action : Adds a new group"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Add Group\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_AutoCorrect(IGESSelect_ModelModifier):
    """
    Does the absolutely effective corrections on IGES Entity.
    That is to say : regarding the norm in details, some values
    have mandatory values, or set of values with constraints.
    When such values/constraints are univoque, they can be forced.
    Also nullifies items of Directory Part, Associativities, and
    Properties, which are not (or not longer) in <target> Model.

    Works by calling a BasicEditor from IGESData
    Works with the specific IGES Services : DirChecker which
    allows to correct data in "Directory Part" of Entities (such
    as required values for status, or references to be null), and
    the specific IGES service OwnCorrect, which is specialised for
    each type of entity.

    Remark : this does not comprise the computation of use flag or
    subordinate status according references, which is made by
    the ModelModifier class ComputeStatus.

    The Input Selection, when present, designates the entities to
    be corrected. If it is not present, all the entities of the
    model are corrected.
    """

    @overload
    def __init__(self) -> None:
        """Creates an AutoCorrect."""

    @overload
    def __init__(self, theOther: IGESSelect_AutoCorrect) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : corrects entities when it is absolutely
        obvious, i.e. non equivoque (by DirChecker and specific
        service OwnCorrect) : works with a protocol.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Auto-correction of IGES Entities\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_ChangeLevelList(IGESSelect_ModelModifier):
    """
    Changes Level List (in directory part) to a new single value
    Only entities attached to a LevelListEntity are considered
    If OldNumber is defined, only entities whose LevelList
    contains its Value are processed. Else all LevelLists are.

    Remark : this concerns the Directory Part only. The Level List
    Entities themselves (their content) are not affected.

    If NewNumber is defined (positive or zero), it gives the new
    value for Level Number. Else, the first value of the LevelList
    is set as new LevelNumber
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a ChangeLevelList, not yet defined
        (see SetOldNumber and SetNewNumber)
        """

    @overload
    def __init__(self, theOther: IGESSelect_ChangeLevelList) -> None: ...

    def HasOldNumber(self) -> bool:
        """
        Returns True if OldNumber is defined : then, only entities
        which have a LevelList which contains the value are processed.
        Else, all entities attached to a LevelList are.
        """

    def OldNumber(self) -> nanoocp.IFSelect.IFSelect_IntParam:
        """
        Returns the parameter for OldNumber. If not defined (Null
        Handle), it will be interpreted as "all level lists\"
        """

    def SetOldNumber(self, param: nanoocp.IFSelect.IFSelect_IntParam | None) -> None:
        """Sets a parameter for OldNumber"""

    def HasNewNumber(self) -> bool:
        """
        Returns True if NewNumber is defined : then, it gives the new
        value for Level Number. Else, the first value of the LevelList
        is used as new Level Number.
        """

    def NewNumber(self) -> nanoocp.IFSelect.IFSelect_IntParam:
        """
        Returns the parameter for NewNumber. If not defined (Null
        Handle), it will be interpreted as "new value 0\"
        """

    def SetNewNumber(self, param: nanoocp.IFSelect.IFSelect_IntParam | None) -> None:
        """Sets a parameter for NewNumber"""

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : considers selected target entities :
        If OldNumber is not defined, all entities attached to a
        Level List
        If OldNumber is defined (value not negative), entities with a
        Level List which contains this value
        Attaches all these entities to value given by NewNumber, or
        the first value of the Level List
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which begins by
        "Changes Level Lists containing <old>", or
        "Changes all Level Lists in D.E.", and ends by
        " to Number <new>"  or  " to Number = first value in List\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_ChangeLevelNumber(IGESSelect_ModelModifier):
    """
    Changes Level Number (as null or single) to a new single value
    Entities attached to a LevelListEntity are ignored
    Entities considered can be, either all Entities but those
    attached to a LevelListEntity, or Entities attached to a
    specific Level Number (0 for not defined).

    Remark : this concerns the Directory Part only. The Level List
    Entities themselves (their content) are not affected.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a ChangeLevelNumber, not yet defined
        (see SetOldNumber and SetNewNumber)
        """

    @overload
    def __init__(self, theOther: IGESSelect_ChangeLevelNumber) -> None: ...

    def HasOldNumber(self) -> bool:
        """
        Returns True if OldNumber is defined : then, only entities
        attached to the value of OldNumber will be considered. Else,
        all entities but those attached to a Level List will be.
        """

    def OldNumber(self) -> nanoocp.IFSelect.IFSelect_IntParam:
        """
        Returns the parameter for OldNumber. If not defined (Null
        Handle), it will be interpreted as "all level numbers\"
        """

    def SetOldNumber(self, param: nanoocp.IFSelect.IFSelect_IntParam | None) -> None:
        """Sets a parameter for OldNumber"""

    def NewNumber(self) -> nanoocp.IFSelect.IFSelect_IntParam:
        """
        Returns the parameter for NewNumber. If not defined (Null
        Handle), it will be interpreted as "new value 0\"
        """

    def SetNewNumber(self, param: nanoocp.IFSelect.IFSelect_IntParam | None) -> None:
        """Sets a parameter for NewNumber"""

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : considers selected target entities :
        If OldNumber is not defined, all entities but those attached
        to a Level List
        If OldNumber is defined (value not negative), entities with a
        defined Level Number (can be zero)
        Attaches all these entities to value given by NewNumber, or
        zero if not defined
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Changes Level Number <old> to <new>" , or
        "Changes all Levels Numbers positive and zero to <new>\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_ComputeStatus(IGESSelect_ModelModifier):
    """
    Computes Status of IGES Entities for a whole IGESModel.
    This concerns SubordinateStatus and UseFlag, which must have
    some definite values according the way they are referenced.
    (see definitions of Logical use, Physical use, etc...)

    Works by calling a BasicEditor from IGESData. Works on the
    whole produced (target) model, because computation is global.
    """

    @overload
    def __init__(self) -> None:
        """Creates an ComputeStatus, which uses the system Date"""

    @overload
    def __init__(self, theOther: IGESSelect_ComputeStatus) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : it first evaluates the required values for
        Subordinate Status and Use Flag (in Directory Part of each
        IGES Entity). Then it corrects them, for the whole target.
        Works with a Protocol. Implementation uses BasicEditor
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Compute Subordinate Status and Use Flag\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_CounterOfLevelNumber(nanoocp.IFSelect.IFSelect_SignCounter):
    """
    This class gives information about Level Number. It counts
    entities according level number, considering also the
    multiple level (see the class LevelList) for which an entity
    is attached to each of the listed levels.

    Data are available, as level number, or as their alphanumeric
    counterparts ("LEVEL nnnnnnn", " NO LEVEL", " LEVEL LIST")
    """

    @overload
    def __init__(self, withmap: bool = True, withlist: bool = False) -> None:
        """
        Creates a CounterOfLevelNumber, clear, ready to work
        <withmap> and <withlist> are transmitted to SignCounter
        """

    @overload
    def __init__(self, theOther: IGESSelect_CounterOfLevelNumber) -> None: ...

    def Clear(self) -> None:
        """Resets already memorized information : also numeric data"""

    def AddSign(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Adds an entity by considering its lrvrl number(s)
        A level is added both in numeric and alphanumeric form,
        i.e. LevelList gives "LEVEL LIST", others (no level or
        positive level) displays level number on 7 digits (C : %7d)
        Remark : an entity attached to a Level List is added for
        " LEVEL LIST", and for each of its constituent levels
        """

    def AddLevel(self, ent: nanoocp.Standard.Standard_Transient | None, level: int) -> None:
        """
        The internal action to record a new level number, positive,
        null (no level) or negative (level list)
        """

    def HighestLevel(self) -> int:
        """Returns the highest value found for a level number"""

    def NbTimesLevel(self, level: int) -> int:
        """
        Returns the number of times a level is used,
        0 if it has not been recorded at all
        <level> = 0 counts entities attached to no level
        <level> < 0 counts entities attached to a LevelList
        """

    def Levels(self) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """Returns the ordered list of used positive Level numbers"""

    def Sign(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Determines and returns the value of the signature for an
        entity as an HAsciiString. Redefined, gives the same result
        as AddSign, see this method ("LEVEL LIST" or "nnnnnnn")
        """

    def PrintCount(self) -> str:
        """
        Prints the counts of items (not the list) then the Highest
        Level Number recorded
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_DispPerDrawing(nanoocp.IFSelect.IFSelect_Dispatch):
    """
    This type of dispatch defines sets of entities attached to
    distinct drawings. This information is taken from attached
    views which appear in the Directory Part. Also Drawing Frames
    are considered when Drawings are part of input list.

    Remaining data concern entities not attached to a drawing.
    """

    @overload
    def __init__(self) -> None:
        """Creates a DispPerDrawing"""

    @overload
    def __init__(self, theOther: IGESSelect_DispPerDrawing) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "One File per Drawing\""""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Computes the list of produced Packets. Packets are computed
        by a ViewSorter (SortDrawings with also frames).
        """

    def CanHaveRemainder(self) -> bool:
        """Returns True, because of entities attached to no view."""

    def Remainder(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns Remainder which is a set of Entities.
        It is supposed to be called once Packets has been called.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_DispPerSingleView(nanoocp.IFSelect.IFSelect_Dispatch):
    """
    This type of dispatch defines sets of entities attached to
    distinct single views. This information appears in the
    Directory Part. Drawings are taken into account too,
    because of their frames (proper lists of annotations)

    Remaining data concern entities not attached to a single view.
    """

    @overload
    def __init__(self) -> None:
        """Creates a DispPerSingleView"""

    @overload
    def __init__(self, theOther: IGESSelect_DispPerSingleView) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns as Label, "One File per single View or Drawing Frame\""""

    def Packets(self, G: nanoocp.Interface.Interface_Graph, packs: nanoocp.IFGraph.IFGraph_SubPartsIterator) -> None:
        """
        Computes the list of produced Packets. Packets are computed
        by a ViewSorter (SortSingleViews with also frames).
        """

    def CanHaveRemainder(self) -> bool:
        """Returns True, because of entities attached to no view."""

    def Remainder(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns Remainder which is a set of Entities.
        It is supposed to be called once Packets has been called.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_Dumper(nanoocp.IFSelect.IFSelect_SessionDumper):
    """
    Dumper from IGESSelect takes into account, for SessionFile, the
    classes defined in the package IGESSelect : Selections,
    Dispatches, Modifiers
    """

    @overload
    def __init__(self) -> None:
        """Creates a Dumper and puts it into the Library of Dumper"""

    @overload
    def __init__(self, theOther: IGESSelect_Dumper) -> None: ...

    def WriteOwn(self, file: nanoocp.IFSelect.IFSelect_SessionFile, item: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Write the Own Parameters of Types defined in package IGESSelect
        Returns True if <item> has been processed, False else
        """

    def ReadOwn(self, file: nanoocp.IFSelect.IFSelect_SessionFile, type: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Recognizes and Read Own Parameters for Types of package
        IGESSelect. Returns True if done and <item> created, False else
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_EditDirPart(nanoocp.IFSelect.IFSelect_Editor):
    """
    This class is aimed to display and edit the Directory Part of
    an IGESEntity
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSelect_EditDirPart) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Recognize(self, form: nanoocp.IFSelect.IFSelect_EditForm | None) -> bool: ...

    def StringValue(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Load(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    def Update(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int, newval: nanoocp.TCollection.TCollection_HAsciiString | None, enforce: bool) -> bool: ...

    def Apply(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_EditHeader(nanoocp.IFSelect.IFSelect_Editor):
    """
    This class is aimed to display and edit the Header of an
    IGES Model : Start Section and Global Section
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSelect_EditHeader) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Recognize(self, form: nanoocp.IFSelect.IFSelect_EditForm | None) -> bool: ...

    def StringValue(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Load(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    def Update(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int, newval: nanoocp.TCollection.TCollection_HAsciiString | None, enforce: bool) -> bool: ...

    def Apply(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_FloatFormat(IGESSelect_FileModifier):
    """
    This class gives control out format for floatting values :
    ZeroSuppress or no, Main Format, Format in Range (for values
    around 1.), as IGESWriter allows to manage it.
    Formats are given under C-printf form
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a new FloatFormat, with standard options :
        ZeroSuppress, Main Format = %E,
        Format between 0.001 and 1000. = %f
        """

    @overload
    def __init__(self, theOther: IGESSelect_FloatFormat) -> None: ...

    def SetDefault(self, digits: int = 0) -> None:
        """
        Sets FloatFormat to default value (see Create) but if <digits>
        is given positive, it commands Formats (main and range) to
        ensure <digits> significant digits to be displayed
        """

    def SetZeroSuppress(self, mode: bool) -> None:
        """Sets ZeroSuppress mode to a new value"""

    def SetFormat(self, format: str = '%E') -> None:
        """
        Sets Main Format to a new value
        Remark : SetFormat, SetZeroSuppress and SetFormatForRange are
        independent
        """

    def SetFormatForRange(self, format: str = '%f', Rmin: float = 0.1, Rmax: float = 1000.0) -> None:
        """
        Sets Format for Range to a new value with its range of
        application.
        To cancel it, give format as "" (empty string)
        Remark that if the condition (0. < Rmin < Rmax) is not
        verified, this secondary format will be ignored.
        Moreover, this secondary format is intended to be used in a
        range around 1.
        """

    def Format(self, mainform: nanoocp.TCollection.TCollection_AsciiString, forminrange: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, bool, float, float]:
        """
        Returns all recorded parameters :
        zerosup  : ZeroSuppress status
        mainform : Main Format (which applies out of the range, or
        for every real if no range is set)
        hasrange : True if a FormatInRange is set, False else
        (following parameters do not apply if it is False)
        forminrange : Secondary Format (it applies inside the range)
        rangemin, rangemax : the range in which the secondary format
        applies
        """

    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite, writer: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """
        Sets the Floatting Formats of IGESWriter to the recorded
        parameters
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns specific Label : for instance,
        "Float Format [ZeroSuppress] %E [, in range R1-R2 %f]\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_IGESName(nanoocp.IFSelect.IFSelect_Signature):
    """
    IGESName is a Signature specific to IGESNorm :
    it considers the Name of an IGESEntity as being its ShortLabel
    (some sending systems use name, not to identify entities, but
    ratjer to classify them)
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a Signature for IGES Name (reduced to ShortLabel,
        without SubscriptLabel or Long Name)
        """

    @overload
    def __init__(self, theOther: IGESSelect_IGESName) -> None: ...

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the ShortLabel as being the Name of an IGESEntity
        If <ent> has no name, it returns empty string "\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_IGESTypeForm(nanoocp.IFSelect.IFSelect_Signature):
    """
    IGESTypeForm is a Signature specific to the IGES Norm :
    it gives the signature under two possible forms :
    - as "mmm nnn", with "mmm" as IGES Type Number, and "nnn"
    as IGES From Number (even if = 0) [Default]
    - as "mmm" alone, which gives only the IGES Type Number
    """

    @overload
    def __init__(self, withform: bool = True) -> None:
        """
        Creates a Signature for IGES Type & Form Numbers
        If <withform> is False, for IGES Type Number only
        """

    @overload
    def __init__(self, theOther: IGESSelect_IGESTypeForm) -> None: ...

    def SetForm(self, withform: bool) -> None:
        """Changes the mode for giving the Form Number"""

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the signature for IGES, "mmm nnn" or "mmm" according
        creation choice (Type & Form or Type only)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_RebuildDrawings(IGESSelect_ModelModifier):
    """
    Rebuilds Drawings which were bypassed to produce new models.
    If a set of entities, all put into a same IGESModel, were
    attached to a same Drawing in the starting Model, this Modifier
    rebuilds the original Drawing, but only with the transferred
    entities. This includes that all its views are kept too, but
    empty; and annotations are not kept. Drawing Name is renewed.

    If the Input Selection is present, tries to rebuild Drawings
    only for the selected entities. Else, tries to rebuild
    Drawings for all the transferred entities.
    """

    @overload
    def __init__(self) -> None:
        """Creates an RebuildDrawings, which uses the system Date"""

    @overload
    def __init__(self, theOther: IGESSelect_RebuildDrawings) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Specific action : Rebuilds the original Drawings"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Rebuild Drawings\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_RebuildGroups(IGESSelect_ModelModifier):
    """
    Rebuilds Groups which were bypassed to produce new models.
    If a set of entities, all put into a same IGESModel, were
    part of a same Group in the starting Model, this Modifier
    rebuilds the original group, but only with the transferred
    entities. The distinctions (Ordered or not, "WithoutBackP"
    or not) are renewed, also the name of the group.

    If the Input Selection is present, tries to rebuild groups
    only for the selected entities. Else, tries to rebuild
    groups for all the transferred entities.
    """

    @overload
    def __init__(self) -> None:
        """Creates an RebuildGroups, which uses the system Date"""

    @overload
    def __init__(self, theOther: IGESSelect_RebuildGroups) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Specific action : Rebuilds the original groups"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Rebuild Groups\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_RemoveCurves(IGESSelect_ModelModifier):
    """
    Removes Curves UV or 3D (not both !) from Faces, those
    designated by the Selection. No Selection means all the file
    """

    @overload
    def __init__(self, UV: bool) -> None:
        """
        Creates a RemoveCurves from Faces (141/142/143/144)
        UV True  : Removes UV Curves (pcurves)
        UV False : Removes 3D Curves
        """

    @overload
    def __init__(self, theOther: IGESSelect_RemoveCurves) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Specific action : Removes the Curves"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Remove Curves UV on Face" or "Remove Curves 3D on Face\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectBasicGeom(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    This selection returns the basic geometric elements
    contained in an IGES Entity
    Intended to run a "quick" transfer. I.E. :
    - for a Group, considers its Elements
    - for a Trimmed or Bounded Surface or a Face (BREP),
    considers the 3D curves of each of its loops
    - for a Plane (108), considers its Bounding Curve
    - for a Curve itself, takes it

    Also, FREE surfaces are taken, because curve 3d is known for
    them. (the ideal should be to have their natural bounds)

    If <curvesonly> is set, ONLY curves-3d are returned
    """

    @overload
    def __init__(self, mode: int) -> None:
        """
        Creates a SelectBasicGeom, which always works recursively
        mode = -1 : Returns Surfaces (without trimming)
        mode = +1 : Returns Curves 3D (free or bound of surface)
        mode = +2 : Returns Basic Curves 3D : as 1 but CompositeCurves
        are returned in detail
        mode = 0  : both
        """

    @overload
    def __init__(self, theOther: IGESSelect_SelectBasicGeom) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity, to take its contained Curves 3d
        Works recursively
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium : "Curves 3d" or
        "Basic Geometry\"
        """

    @staticmethod
    def SubCurves(ent: nanoocp.IGESData.IGESData_IGESEntity | None, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        This method can be called from everywhere to get the curves
        as sub-elements of a given curve :
        CompositeCurve : explored lists its subs + returns True
        Any Curve : explored is not filled but returned is True
        Other : returned is False
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectBypassGroup(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    Selects a list built as follows :
    Groups are entities type 402, forms 1,7,14,15 (Group,
    Ordered or not, "WithoutBackPointer" or not)

    Entities which are not GROUP are taken as such
    For Groups, their list of Elements is explore
    Hence, level 0 (D) recursively explores a Group if some of
    its Elements are Groups. level 1 explores just at first level
    """

    @overload
    def __init__(self, level: int = 0) -> None:
        """
        Creates a SelectBypassGroup, by default all level
        (level = 1 explores at first level)
        """

    @overload
    def __init__(self, theOther: IGESSelect_SelectBypassGroup) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity : for a Group, gives its elements
        Else, takes the entity itself
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Content of Group\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectBypassSubfigure(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    Selects a list built as follows :
    Subfigures correspond to
    * Definition (basic : type 308, or Network : type 320)
    * Instance (Singular : type 408, or Network : 420, or
    patterns : 412,414)

    Entities which are not Subfigure are taken as such
    For Subfigures Instances, their definition is taken, then
    explored itself
    For Subfigures Definitions, the list of "Associated Entities"
    is explored
    Hence, level 0 (D) recursively explores a Subfigure if some of
    its Elements are Subfigures. level 1 explores just at first
    level (i.e. for an instance, returns its definition)
    """

    @overload
    def __init__(self, level: int = 0) -> None:
        """
        Creates a SelectBypassSubfigure, by default all level
        (level = 1 explores at first level)
        """

    @overload
    def __init__(self, theOther: IGESSelect_SelectBypassSubfigure) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity : for a Subfigure, gives its elements
        Else, takes the entity itself
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Content of Subfigure\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectDrawingFrom(nanoocp.IFSelect.IFSelect_SelectDeduct):
    """
    This selection gets the Drawings attached to its input IGES
    entities. They are read through the Single Views, referenced
    in Directory Parts of the entities
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectDrawingFrom"""

    @overload
    def __init__(self, theOther: IGESSelect_SelectDrawingFrom) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Selects the Drawings attached (through Single Views in
        Directory Part) to input entities
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the label, with its "Drawings attached\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectFaces(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    This selection returns the faces contained in an IGES Entity
    or itself if it is a Face
    Face means :
    - Face (510) of a ManifoldSolidBrep
    - TrimmedSurface (144)
    - BoundedSurface (143)
    - Plane with a Bounding Curve (108, form not 0)
    - Also, any Surface which is not in a TrimmedSurface, a
    BoundedSurface, or a Face (FREE Surface)
    -> i.e. a Face for which Natural Bounds will be considered
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSelect_SelectFaces) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity, to take its faces
        Works recursively
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Faces\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectFromDrawing(nanoocp.IFSelect.IFSelect_SelectDeduct):
    """
    This selection gets in all the model, the entities which are
    attached to the drawing(s) given as input. This includes :
    - Drawing Frame (Annotations directky referenced by Drawings)
    - Entities attached to the single Views referenced by Drawings
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectFromDrawing"""

    @overload
    def __init__(self, theOther: IGESSelect_SelectFromDrawing) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Selects the Entities which are attached to the Drawing(s)
        present in the Input
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the label, with is "Entities attached to Drawing\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectFromSingleView(nanoocp.IFSelect.IFSelect_SelectDeduct):
    """
    This selection gets in all the model, the entities which are
    attached to the views given as input. Only Single Views are
    considered. This information is kept from Directory Part
    (View Item).
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectFromSingleView"""

    @overload
    def __init__(self, theOther: IGESSelect_SelectFromSingleView) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Selects the Entities which are attached to the Single View(s)
        present in the Input
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the label, with is "Entities attached to single View\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectLevelNumber(nanoocp.IFSelect.IFSelect_SelectExtract):
    """
    This selection looks at Level Number of IGES Entities :
    it considers items attached, either to a single level with a
    given value, or to a level list which contains this value

    Level = 0  means entities not attached to any level

    Remark : the class CounterOfLevelNumber gives information
    about present levels in a file.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a SelectLevelNumber, with no Level criterium : see
        SetLevelNumber. Empty, this selection filters nothing.
        """

    @overload
    def __init__(self, theOther: IGESSelect_SelectLevelNumber) -> None: ...

    def SetLevelNumber(self, levnum: nanoocp.IFSelect.IFSelect_IntParam | None) -> None:
        """Sets a Parameter as Level criterium"""

    def LevelNumber(self) -> nanoocp.IFSelect.IFSelect_IntParam:
        """
        Returns the Level criterium. NullHandle if not yet set
        (interpreted as Level = 0 : no level number attached)
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True if <ent> is an IGES Entity with Level Number
        admits the criterium (= value if single level, or one of the
        attached level numbers = value if level list)
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the Selection criterium :
        "IGES Entity, Level Number admits <nn>" (if nn > 0) or
        "IGES Entity attached to no Level" (if nn = 0)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectName(nanoocp.IFSelect.IFSelect_SelectExtract):
    """
    Selects Entities which have a given name.
    Consider Property Name if present, else Short Label, but
    not the Subscript Number
    First version : keeps exact name
    Later : regular expression
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty SelectName : every entity is considered
        good (no filter active)
        """

    @overload
    def __init__(self, theOther: IGESSelect_SelectName) -> None: ...

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns True if Name of Entity complies with Name Filter"""

    def SetName(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Sets a Name as a criterium : IGES Entities which have this name
        are kept (without regular expression, there should be at most
        one). <name> can be regarded as a Text Parameter
        """

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the Name used as Filter"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the Selection criterium : "IGES Entity, Name : <name>\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectPCurves(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    This Selection returns the pcurves which lie on a face
    In two modes : global (i.e. a CompositeCurve is not explored)
    or basic (all the basic curves are listed)
    """

    @overload
    def __init__(self, basic: bool) -> None:
        """
        Creates a SelectPCurves
        basic True  : lists all the components of pcurves
        basic False : lists the uppest level definitions
        (i.e. stops at CompositeCurve)
        """

    @overload
    def __init__(self, theOther: IGESSelect_SelectPCurves) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity, to take its contained PCurves
        An independent curve is IGNORED : only faces are explored
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium : "Basic PCurves" or
        "Global PCurves\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectSingleViewFrom(nanoocp.IFSelect.IFSelect_SelectDeduct):
    """
    This selection gets the Single Views attached to its input
    IGES entities. Single Views themselves or Drawings as passed
    as such (Drawings, for their Annotations)
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectSingleViewFrom"""

    @overload
    def __init__(self, theOther: IGESSelect_SelectSingleViewFrom) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Selects the Single Views attached (in Directory Part) to
        input entities
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the label, with is "Single Views attached\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectSubordinate(nanoocp.IFSelect.IFSelect_SelectExtract):
    """
    This selections uses Subordinate Status as sort criterium
    It is an integer number which can be :
    0 Independent
    1 Physically Dependent
    2 Logically Dependent
    3 Both (recorded)
    + to sort :
    4 : 1 or 3  ->  at least Physically
    5 : 2 or 3  ->  at least Logically
    6 : 1 or 2 or 3 -> any kind of dependence
    (corresponds to 0 reversed)
    """

    @overload
    def __init__(self, status: int) -> None:
        """Creates a SelectSubordinate with a status to be sorted"""

    @overload
    def __init__(self, theOther: IGESSelect_SelectSubordinate) -> None: ...

    def Status(self) -> int:
        """Returns the status used for sorting"""

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True if <ent> is an IGES Entity with Subordinate
        Status matching the criterium
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the Selection criterium : "IGES Entity, Independent"
        etc...
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SelectVisibleStatus(nanoocp.IFSelect.IFSelect_SelectExtract):
    """
    This selection looks at Blank Status of IGES Entities
    Direct  selection keeps Visible Entities (Blank = 0),
    Reverse selection keeps Blanked Entities (Blank = 1)
    """

    @overload
    def __init__(self) -> None:
        """Creates a SelectVisibleStatus"""

    @overload
    def __init__(self, theOther: IGESSelect_SelectVisibleStatus) -> None: ...

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns True if <ent> is an IGES Entity with Blank Status = 0"""

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the Selection criterium : "IGES Entity, Status Visible\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SetGlobalParameter(IGESSelect_ModelModifier):
    """
    Sets a Global (Header) Parameter to a new value, directly given
    Controls the form of the parameter (Integer, Real, String
    with such or such form), but not the consistence of the new
    value regarding the rest of the file.

    The new value is given under the form of a HAsciiString, even
    for Integer or Real values. For String values, Hollerith forms
    are accepted but not mandatory
    Warning : a Null (not set) value is not accepted. For an empty string,
    give a Text Parameter which is empty
    """

    @overload
    def __init__(self, numpar: int) -> None:
        """
        Creates an SetGlobalParameter, to be applied on Global
        Parameter <numpar>
        """

    @overload
    def __init__(self, theOther: IGESSelect_SetGlobalParameter) -> None: ...

    def GlobalNumber(self) -> int:
        """
        Returns the global parameter number to which this modifiers
        applies
        """

    def SetValue(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets a Text Parameter for the new value"""

    def Value(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the value to set to the global parameter (Text Param)"""

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : only <target> is used : the form of the new
        value is checked regarding the parameter number (given at
        creation time).
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Sets Global Parameter <numpar> to <new value>\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SetLabel(IGESSelect_ModelModifier):
    """
    Sets/Clears Short Label of Entities, those designated by the
    Selection. No Selection means all the file

    May enforce, else it sets only if no label is yet set
    Mode : 0 to clear (always enforced)
    1 to set label to DE number (changes it if already set)
    """

    @overload
    def __init__(self, mode: int, enforce: bool) -> None:
        """
        Creates a SetLabel for IGESEntity
        Mode : see Purpose of the class
        """

    @overload
    def __init__(self, theOther: IGESSelect_SetLabel) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Specific action : Sets or Clears the Label"""

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Clear Short Label" or "Set Label to DE"
        With possible additional information " (enforced)\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SetVersion5(IGESSelect_ModelModifier):
    """
    Sets IGES Version (coded in global parameter 23) to be at least
    IGES 5.1 . If it is older, it is set to IGES 5.1, and
    LastChangeDate (new Global n0 25) is added (current time)
    Else, it does nothing (i.e. changes neither IGES Version nor
    LastChangeDate)
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an SetVersion5, which uses the system Date for Last
        Change Date
        """

    @overload
    def __init__(self, theOther: IGESSelect_SetVersion5) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : only <target> is used : IGES Version (coded)
        is upgraded to 5.1 if it is older, and it this case the new
        global parameter 25 (LastChangeDate) is set to current time
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Update IGES Version to 5.1\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SignColor(nanoocp.IFSelect.IFSelect_Signature):
    """
    Gives Color attached to an entity
    Several forms are possible, according to <mode>
    1 : number : "Dnn" for entity, "Snn" for standard, "(none)" for 0
    2 : name : Of standard color, or of the color entity, or "(none)"
    (if the color entity has no name, its label is taken)
    3 : RGB values, form R:nn,G:nn,B:nn
    4 : RED value   : an integer
    5 : GREEN value : an integer
    6 : BLUE value  : an integer
    Other computable values can be added if needed :
    CMY values, Percentages for Hue, Lightness, Saturation
    """

    @overload
    def __init__(self, mode: int) -> None:
        """
        Creates a SignColor
        mode : see above for the meaning
        modes 4,5,6 give a numeric integer value
        Name is initialised according to the mode
        """

    @overload
    def __init__(self, theOther: IGESSelect_SignColor) -> None: ...

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """Returns the value (see above)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SignLevelNumber(nanoocp.IFSelect.IFSelect_Signature):
    """
    Gives D.E. Level Number under two possible forms :
    * for counter : "LEVEL nnnnnnn", " NO LEVEL", " LEVEL LIST"
    * for selection : "/nnn/", "/0/", "/1/2/nnn/"

    For matching, giving /nn/ gets any entity attached to level nn
    whatever simple or in a level list
    """

    @overload
    def __init__(self, countmode: bool) -> None:
        """
        Creates a SignLevelNumber
        <countmode> True : values are naturally displayed
        <countmode> False: values are separated by slashes
        in order to allow selection by signature by Draw or C++
        """

    @overload
    def __init__(self, theOther: IGESSelect_SignLevelNumber) -> None: ...

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """Returns the value (see above)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SignStatus(nanoocp.IFSelect.IFSelect_Signature):
    """
    Gives D.E. Status under the form i,j,k,l (4 figures)
    i for BlankStatus
    j for SubordinateStatus
    k for UseFlag
    l for Hierarchy

    For matching, allowed shortcuts
    B(Blanked) or V(Visible) are allowed instead of i
    I(Independant=0), P(Physically Dep.=1), L(Logically Dep.=2) or
    D(Dependant=3) are allowed instead of j
    These letters must be given in their good position
    For non-exact matching :
    a letter (see above), no comma : only this status is checked
    nothing or a star between commas : this status is OK
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSelect_SignStatus) -> None: ...

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """Returns the value (see above)"""

    def Matches(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None, text: nanoocp.TCollection.TCollection_AsciiString, exact: bool) -> bool:
        """Performs the match rule (see above)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_SplineToBSpline(nanoocp.IFSelect.IFSelect_Transformer):
    """
    This type of Transformer allows to convert Spline Curves (IGES
    type 112) and Surfaces (IGES Type 126) to BSpline Curves (IGES
    type 114) and Surfac (IGES Type 128). All other entities are
    rebuilt as identical but on the basis of this conversion.

    It also gives an option to, either convert as such (i.e. each
    starting part of the spline becomes a segment of the bspline,
    with continuity C0 between segments), or try to increase
    continuity as far as possible to C1 or to C2.

    It does nothing if the starting model contains no Spline
    Curve (IGES Type 112) or Surface (IGES Type 126). Else,
    converting and rebuilding implies copying of entities.
    """

    @overload
    def __init__(self, tryC2: bool) -> None:
        """
        Creates a Transformer SplineToBSpline. If <tryC2> is True,
        it will in addition try to upgrade continuity up to C2.
        """

    @overload
    def __init__(self, theOther: IGESSelect_SplineToBSpline) -> None: ...

    def OptionTryC2(self) -> bool:
        """Returns the option TryC2 given at creation time"""

    def Perform(self, G: nanoocp.Interface.Interface_Graph, protocol: nanoocp.Interface.Interface_Protocol | None, checks: nanoocp.Interface.Interface_CheckIterator) -> tuple[bool, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Performs the transformation, if there is at least one Spline
        Curve (112) or Surface (126). Does nothing if there is none.
        """

    def Updated(self, entfrom: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns the transformed entities.
        If original data contained no Spline Curve or Surface,
        the result is identity : <entto> = <entfrom>
        Else, the copied counterpart is returned : for a Spline Curve
        or Surface, it is a converted BSpline Curve or Surface. Else,
        it is the result of general service Copy (rebuilt as necessary
        by BSPlines replacing Splines).
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which defines the way a Transformer works :
        "Conversion Spline to BSpline" and as opted,
        " trying to upgrade continuity\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_UpdateCreationDate(IGESSelect_ModelModifier):
    """
    Allows to Change the Creation Date indication in the Header
    (Global Section) of IGES File. It is taken from the operating
    system (time of application of the Modifier).
    The Selection of the Modifier is not used : it simply acts as
    a criterium to select IGES Files to touch up
    """

    @overload
    def __init__(self) -> None:
        """Creates an UpdateCreationDate, which uses the system Date"""

    @overload
    def __init__(self, theOther: IGESSelect_UpdateCreationDate) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : only <target> is used : the system Date
        is set to Global Section Item n0 18.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Update IGES Header Creation Date\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_UpdateFileName(IGESSelect_ModelModifier):
    """
    Sets the File Name in Header to be the actual name of the file
    If new file name is unknown, the former one is kept
    Remark : this works well only when it is Applied and send time
    If it is run immediately, new file name is unknown and nothing
    is done
    The Selection of the Modifier is not used : it simply acts as
    a criterium to select IGES Files to touch up
    """

    @overload
    def __init__(self) -> None:
        """Creates an UpdateFileName, which uses the system Date"""

    @overload
    def __init__(self, theOther: IGESSelect_UpdateFileName) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : only <target> is used : the system Date
        is set to Global Section Item n0 18.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Updates IGES File Name to new current one\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_UpdateLastChange(IGESSelect_ModelModifier):
    """
    Allows to Change the Last Change Date indication in the Header
    (Global Section) of IGES File. It is taken from the operating
    system (time of application of the Modifier).
    The Selection of the Modifier is not used : it simply acts as
    a criterium to select IGES Files to touch up.
    Remark : IGES Models noted as version before IGES 5.1 are in
    addition changed to 5.1
    """

    @overload
    def __init__(self) -> None:
        """Creates an UpdateLastChange, which uses the system Date"""

    @overload
    def __init__(self, theOther: IGESSelect_UpdateLastChange) -> None: ...

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.IGESData.IGESData_IGESModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific action : only <target> is used : the system Date
        is set to Global Section Item n0 25. Also sets IGES Version
        (Item n0 23) to IGES5 if it was older.
        """

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text which is
        "Update IGES Header Last Change Date\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_ViewSorter(nanoocp.Standard.Standard_Transient):
    """
    Sorts IGES Entities on the views and drawings.
    In a first step, it splits a set of entities according the
    different views they are attached to.
    Then, packets according single views (+ drawing frames), or
    according drawings (which refer to the views) can be determined

    It is a TShared, hence it can be a workomg field of a non-
    mutable object (a Dispatch for instance)
    """

    @overload
    def __init__(self) -> None:
        """Creates a ViewSorter, empty. SetModel remains to be called"""

    @overload
    def __init__(self, theOther: IGESSelect_ViewSorter) -> None: ...

    def SetModel(self, model: nanoocp.IGESData.IGESData_IGESModel | None) -> None:
        """Sets the Model (for PacketList)"""

    def Clear(self) -> None:
        """Clears recorded data"""

    def Add(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Adds an item according its type : AddEntity,AddList,AddModel"""

    def AddEntity(self, igesent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Adds an IGES entity. Records the view it is attached to.
        Records directly <ent> if it is a ViewKindEntity or a Drawing
        Returns True if added, False if already in the map
        """

    def AddList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Adds a list of entities by adding each of the items"""

    def AddModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Adds all the entities contained in a Model"""

    def NbEntities(self) -> int:
        """Returns the count of already recorded"""

    def SortSingleViews(self, alsoframes: bool) -> None:
        """
        Prepares the result to keep only sets attached to Single Views
        If <alsoframes> is given True, it keeps also the Drawings as
        specific sets, in order to get their frames.
        Entities attached to no single view are put in Remaining List.

        Result can then be read by the methods NbSets,SetItem,SetList,
        RemainingList(final = True)
        """

    def SortDrawings(self, G: nanoocp.Interface.Interface_Graph) -> None:
        """
        Prepares the result to the sets attached to Drawings :
        All the single views referenced by a Drawing become bound to
        the set for this Drawing

        Entities or Views which correspond to no Drawing are put into
        the Remaining List.

        Result can then be read by the methods NbSets,SetItem,SetList,
        RemainingList(final = True)
        """

    def NbSets(self, final: bool) -> int:
        """
        Returns the count of sets recorded, one per distinct item.
        The Remaining List is not counted.
        If <final> is False, the sets are attached to distinct views
        determined by the method Add.
        If <final> is True, they are the sets determined by the last
        call to, either SortSingleViews, or SortDrawings.

        Warning : Drawings directly recorded are also counted as sets, because
        of their Frame (which is made of Annotations)
        """

    def SetItem(self, num: int, final: bool) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Returns the Item which is attached to a set of entities
        For <final> and definition of sets, see method NbSets.
        This item can be a kind of View or a Drawing
        """

    def Sets(self, final: bool) -> nanoocp.IFSelect.IFSelect_PacketList:
        """
        Returns the complete content of the determined Sets, which
        include Duplicated and Remaining (duplication 0) lists
        For <final> and definition of sets, see method NbSets.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSelect_WorkLibrary(nanoocp.IFSelect.IFSelect_WorkLibrary):
    """Performs Read and Write an IGES File with an IGES Model"""

    @overload
    def __init__(self, modefnes: bool = False) -> None:
        """
        Creates a IGES WorkLibrary
        If <modefnes> is given as True, it will work for FNES
        """

    @overload
    def __init__(self, theOther: IGESSelect_WorkLibrary) -> None: ...

    def ReadFile(self, name: str, protocol: nanoocp.Interface.Interface_Protocol | None) -> tuple[int, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Reads a IGES File and returns a IGES Model (into <mod>),
        or lets <mod> "Null" in case of Error
        Returns 0 if OK, 1 if Read Error, -1 if File not opened
        """

    def WriteFile(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite) -> bool:
        """
        Writes a File from a IGES Model (brought by <ctx>)
        Returns False (and writes no file) if <ctx> is not for IGES
        """

    @staticmethod
    def DefineProtocol() -> nanoocp.IGESData.IGESData_Protocol:
        """
        Defines a protocol to be adequate for IGES
        (encompasses ALL the IGES norm including IGESSolid, IGESAppli)
        """

    def DumpEntity(self, model: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, entity: nanoocp.Standard.Standard_Transient | None, level: int) -> str:
        """
        Dumps an IGES Entity with an IGES Dumper. <level> is the one
        used by IGESDumper.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
