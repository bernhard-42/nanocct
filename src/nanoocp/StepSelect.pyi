"""OCCT package StepSelect (toolkit TKDESTEP)"""

from typing import TextIO, overload

import nanoocp.IFSelect
import nanoocp.Interface
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.TCollection


class StepSelect_Activator(nanoocp.IFSelect.IFSelect_Activator):
    """
    Performs Actions specific to StepSelect, i.e. creation of
    Step Selections and Counters, plus dumping specific to Step
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepSelect_Activator) -> None: ...

    def Do(self, number: int, pilot: nanoocp.IFSelect.IFSelect_SessionPilot | None) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Executes a Command Line for StepSelect"""

    def Help(self, number: int) -> str:
        """Sends a short help message for StepSelect commands"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepSelect_FileModifier(nanoocp.IFSelect.IFSelect_GeneralModifier):
    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite, writer: nanoocp.StepData.StepData_StepWriter) -> None:
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

class StepSelect_FloatFormat(StepSelect_FileModifier):
    """
    This class gives control out format for floatting values :
    ZeroSuppress or no, Main Format, Format in Range (for values
    around 1.), as StepWriter allows to manage it.
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
    def __init__(self, theOther: StepSelect_FloatFormat) -> None: ...

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

    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite, writer: nanoocp.StepData.StepData_StepWriter) -> None:
        """
        Sets the Floatting Formats of StepWriter to the recorded
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

class StepSelect_ModelModifier(nanoocp.IFSelect.IFSelect_Modifier):
    def Perform(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        The inherited Perform does the required cast (and refuses to
        go further if cast has failed) then calls the instantiated
        Performing
        """

    def PerformProtocol(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.StepData.StepData_StepModel | None, proto: nanoocp.StepData.StepData_Protocol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific Perform with Protocol. It is defined to let the
        Protocol unused and to call Performing without Protocol
        (most current case). It can be redefined if specific action
        requires Protocol.
        """

    def Performing(self, ctx: nanoocp.IFSelect.IFSelect_ContextModif, target: nanoocp.StepData.StepData_StepModel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
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

class StepSelect_StepType(nanoocp.IFSelect.IFSelect_Signature):
    """
    StepType is a Signature specific to Step definitions : it
    considers the type as defined in STEP Schemas, the same which
    is used in files.
    For a Complex Type, if its definition is known, StepType
    produces the list of basic types, separated by commas, the
    whole between brackets : "(TYPE1,TYPE2..)".
    If its precise definition is not known (simply it is known as
    Complex, it can be recognised, but the list is produced at
    Write time only), StepType produces : "(..COMPLEX TYPE..)\"
    """

    def __init__(self) -> None:
        """
        Creates a Signature for Step Type. Protocol is undefined here,
        hence no Signature may yet be produced. The StepType signature
        requires a Protocol before working
        """

    def SetProtocol(self, proto: nanoocp.Interface.Interface_Protocol | None) -> None:
        """
        Sets the StepType signature to work with a Protocol : this
        initialises the library
        """

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Step Type defined from the Protocol (see above).
        If <ent> is not recognised, produces "..NOT FROM SCHEMA <name>..\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepSelect_WorkLibrary(nanoocp.IFSelect.IFSelect_WorkLibrary):
    """
    Performs Read and Write a STEP File with a STEP Model
    Following the protocols, Copy may be implemented or not
    """

    @overload
    def __init__(self, copymode: bool = True) -> None:
        """
        Creates a STEP WorkLibrary
        <copymode> precises whether Copy is implemented or not
        """

    @overload
    def __init__(self, theOther: StepSelect_WorkLibrary) -> None: ...

    def SetDumpLabel(self, mode: int) -> None:
        """
        Selects a mode to dump entities
        0 (D) : prints numbers, then displays table number/label
        1 : prints labels, then displays table label/number
        2 : prints labels onky
        """

    def ReadFile(self, name: str, protocol: nanoocp.Interface.Interface_Protocol | None) -> tuple[int, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Reads a STEP File and returns a STEP Model (into <mod>),
        or lets <mod> "Null" in case of Error
        Returns 0 if OK, 1 if Read Error, -1 if File not opened
        """

    def ReadStream(self, theName: str, theIStream: TextIO, protocol: nanoocp.Interface.Interface_Protocol | None) -> tuple[int, nanoocp.Interface.Interface_InterfaceModel]:
        """
        Reads a STEP File from stream and returns a STEP Model (into <mod>),
        or lets <mod> "Null" in case of Error
        Returns 0 if OK, 1 if Read Error, -1 if File not opened
        """

    def WriteFile(self, ctx: nanoocp.IFSelect.IFSelect_ContextWrite) -> bool:
        """
        Writes a File from a STEP Model
        Returns False (and writes no file) if <ctx> does not bring a
        STEP Model
        """

    def CopyModel(self, original: nanoocp.Interface.Interface_InterfaceModel | None, newmodel: nanoocp.Interface.Interface_InterfaceModel | None, list: nanoocp.Interface.Interface_EntityIterator, TC: nanoocp.Interface.Interface_CopyTool) -> bool:
        """
        Performs the copy of entities from an original model to a new
        one. Works according <copymode> :
        if True, standard copy is run
        else nothing is done and returned value is False
        """

    def DumpEntity(self, model: nanoocp.Interface.Interface_InterfaceModel | None, protocol: nanoocp.Interface.Interface_Protocol | None, entity: nanoocp.Standard.Standard_Transient | None, level: int) -> str:
        """
        Dumps an entity under STEP form, i.e. as a part of a Step file
        Works with a StepDumper.
        Level 0 just displays type; level 1 displays the entity itself
        and level 2 displays the entity plus its shared ones (one
        sub-level : immediately shared entities)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
