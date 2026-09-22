"""OCCT package RWHeaderSection (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.HeaderSection
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.TCollection


class RWHeaderSection:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWHeaderSection) -> None: ...

    @staticmethod
    def Init() -> None:
        """enforced the initialisation of the libraries"""

class RWHeaderSection_GeneralModule(nanoocp.StepData.StepData_GeneralModule):
    """
    Defines General Services for HeaderSection Entities
    (Share,Check,Copy; Trace already inherited)
    Depends (for case numbers) of Protocol from HeaderSection
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule"""

    @overload
    def __init__(self, theOther: RWHeaderSection_GeneralModule) -> None: ...

    def FillSharedCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Specific filling of the list of Entities shared by an Entity
        <ent>, according to a Case Number <CN> (provided by HeaderSection
        Protocol).
        """

    def CheckCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Specific Checking of an Entity <ent>"""

    def CopyCase(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type)
        by using a CopyTool which provides its working Map.
        Use method Transferred from CopyTool to work
        """

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class RWHeaderSection_ReadWriteModule(nanoocp.StepData.StepData_ReadWriteModule):
    """General module to read and write HeaderSection entities"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWHeaderSection_ReadWriteModule) -> None: ...

    @overload
    def CaseStep(self, atype: nanoocp.TCollection.TCollection_AsciiString) -> int:
        """
        associates a positive Case Number to each type of HeaderSection entity,
        given as a String defined in the EXPRESS form
        """

    @overload
    def CaseStep(self, types: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> int:
        """
        associates a positive Case Number to each type of HeaderSection Complex entity,
        given as a String defined in the EXPRESS form
        """

    def IsComplex(self, CN: int) -> bool:
        """returns True if the Case Number corresponds to a Complex Type"""

    def StepType(self, CN: int) -> str:
        """
        returns a StepType (defined in EXPRESS form which belongs to a
        Type of Entity, identified by its CaseNumber determined by Protocol
        """

    def ReadStep(self, CN: int, data: nanoocp.StepData.StepData_StepReaderData | None, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check: ...

    def WriteStep(self, CN: int, SW: nanoocp.StepData.StepData_StepWriter, ent: nanoocp.Standard.Standard_Transient | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class RWHeaderSection_RWFileDescription:
    """Read & Write Module for FileDescription"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWHeaderSection_RWFileDescription) -> None: ...

    def ReadStep(self, data: nanoocp.StepData.StepData_StepReaderData | None, num: int, ent: nanoocp.HeaderSection.HeaderSection_FileDescription | None) -> nanoocp.Interface.Interface_Check: ...

    def WriteStep(self, SW: nanoocp.StepData.StepData_StepWriter, ent: nanoocp.HeaderSection.HeaderSection_FileDescription | None) -> None: ...

class RWHeaderSection_RWFileName:
    """Read & Write Module for FileName"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWHeaderSection_RWFileName) -> None: ...

    def ReadStep(self, data: nanoocp.StepData.StepData_StepReaderData | None, num: int, ent: nanoocp.HeaderSection.HeaderSection_FileName | None) -> nanoocp.Interface.Interface_Check: ...

    def WriteStep(self, SW: nanoocp.StepData.StepData_StepWriter, ent: nanoocp.HeaderSection.HeaderSection_FileName | None) -> None: ...

class RWHeaderSection_RWFileSchema:
    """Read & Write Module for FileSchema"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWHeaderSection_RWFileSchema) -> None: ...

    def ReadStep(self, data: nanoocp.StepData.StepData_StepReaderData | None, num: int, ent: nanoocp.HeaderSection.HeaderSection_FileSchema | None) -> nanoocp.Interface.Interface_Check: ...

    def WriteStep(self, SW: nanoocp.StepData.StepData_StepWriter, ent: nanoocp.HeaderSection.HeaderSection_FileSchema | None) -> None: ...
