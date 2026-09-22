"""OCCT package StepFile (toolkit TKDESTEP)"""

import nanoocp.Interface


class StepFile_ReadData:
    def __init__(self) -> None:
        """Constructs an uninitialized tool"""

    def CreateNewText(self, theNewText: str, theLenText: int) -> None:
        """
        Prepares the text value for analysis.
        It is the main tool for transferring data from flex to bison
        If characters page is full, allocates a new page.
        """

    def RecordNewEntity(self) -> None:
        """Adds the current record to the list"""

    def RecordIdent(self) -> None:
        """Creates a new record and sets Ident from myResText"""

    def RecordType(self) -> None:
        """Starts reading of the type (entity)"""

    def RecordListStart(self) -> None:
        """Prepares and saves a record or sub-record"""

    def CreateNewArg(self) -> None:
        """
        Prepares new arguments.
        Type and value already known.
        If arguments page is full, allocates a new page
        """

    def CreateErrorArg(self) -> None:
        """
        Prepares error arguments, controls count of error arguments.
        If bison handles a sequence of error types,
        creates only one argument and updates text value
        """

    def AddNewScope(self) -> None:
        """Creates a new scope, containing the current record"""

    def FinalOfScope(self) -> None:
        """Ends the scope"""

    def ClearRecorder(self, theMode: int) -> None:
        """
        Releases memory.
        @param theMode
        * 1 - clear pages of records and arguments
        * 2 - clear pages of characters
        * 3 - clear all data
        """

    def RecordTypeText(self) -> None:
        """Initializes the record type with myResText"""

    def NextRecord(self) -> None:
        """Skips to next record"""

    def PrintCurrentRecord(self) -> None:
        """Prints data of current record according to the modeprint"""

    def PrepareNewArg(self) -> None:
        """
        Controls the correct argument count for the record.
        Resets error argyment mode
        """

    def FinalOfHead(self) -> None:
        """Prepares the end of the head section"""

    def SetTypeArg(self, theArgType: nanoocp.Interface.Interface_ParamType) -> None:
        """Sets type of the current argument"""

    def SetModePrint(self, theMode: int) -> None:
        """
        Initializes the print mode
        0 - don't print descriptions
        1 - print only descriptions of record
        2 - print descriptions of records and its arguments
        """

    def GetModePrint(self) -> int:
        """Returns mode print"""

    def GetNbRecord(self) -> int:
        """Returns number of records"""

    def AddError(self, theErrorMessage: str) -> None:
        """Adds an error message"""

    def ErrorHandle(self, theCheck: nanoocp.Interface.Interface_Check | None) -> bool:
        """Transfers error messages to checker"""

    def GetLastError(self) -> str:
        """Returns the message of the last error"""

def StepFile_Interrupt(theErrorMessage: str, theIsFail: bool = True) -> None:
    """
    Prints the error message
    @param theErrorMessage - error message for output
    @param theFail - if true output as a fail info, else output as a trace info ( log )
    """
