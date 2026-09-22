"""OCCT package APIHeaderSection (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.HeaderSection
import nanoocp.IFSelect
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.TCollection


class APIHeaderSection_EditHeader(nanoocp.IFSelect.IFSelect_Editor):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: APIHeaderSection_EditHeader) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Recognize(self, form: nanoocp.IFSelect.IFSelect_EditForm | None) -> bool: ...

    def StringValue(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Apply(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    def Load(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class APIHeaderSection_MakeHeader:
    """
    This class allows to consult and prepare/edit data stored in
    a Step Model Header
    """

    @overload
    def __init__(self, shapetype: int = 0) -> None:
        """Prepares a new MakeHeader from scratch"""

    @overload
    def __init__(self, model: nanoocp.StepData.StepData_StepModel | None) -> None:
        """
        Prepares a MakeHeader from the content of a StepModel
        See IsDone to know if the Header is well defined
        """

    @overload
    def __init__(self, theOther: APIHeaderSection_MakeHeader) -> None: ...

    def Init(self, nameval: str) -> None:
        """
        Cancels the former definition and gives a FileName
        To be used when a Model has no well defined Header
        """

    def IsDone(self) -> bool:
        """
        Returns True if all data have been defined (see also
        HasFn, HasFs, HasFd)
        """

    def Apply(self, model: nanoocp.StepData.StepData_StepModel | None) -> None:
        """
        Creates an empty header for a new
        STEP model and allows the header fields to be completed.
        """

    def NewModel(self, protocol: nanoocp.Interface.Interface_Protocol | None) -> nanoocp.StepData.StepData_StepModel:
        """
        Builds a Header, creates a new StepModel, then applies the
        Header to the StepModel
        The Schema Name is taken from the Protocol (if it inherits
        from StepData, else it is left in blanks)
        """

    def HasFn(self) -> bool:
        """
        Checks whether there is a
        file_name entity. Returns True if there is one.
        """

    def FnValue(self) -> nanoocp.HeaderSection.HeaderSection_FileName:
        """
        Returns the file_name entity.
        Returns an empty entity if the file_name entity is not initialized.
        """

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name attribute for the file_name entity."""

    def SetTimeStamp(self, aTimeStamp: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def TimeStamp(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of the time_stamp attribute for the file_name entity.
        """

    def SetAuthor(self, aAuthor: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def SetAuthorValue(self, num: int, aAuthor: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Author(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def AuthorValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the value of the name attribute for the file_name entity."""

    def NbAuthor(self) -> int:
        """
        Returns the number of values for the author attribute in the file_name entity.
        """

    def SetOrganization(self, aOrganization: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def SetOrganizationValue(self, num: int, aOrganization: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Organization(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def OrganizationValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of attribute
        organization for the file_name entity.
        """

    def NbOrganization(self) -> int:
        """
        Returns the number of values for
        the organization attribute in the file_name entity.
        """

    def SetPreprocessorVersion(self, aPreprocessorVersion: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def PreprocessorVersion(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the preprocessor_version for the file_name entity."""

    def SetOriginatingSystem(self, aOriginatingSystem: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def OriginatingSystem(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetAuthorisation(self, aAuthorisation: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Authorisation(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of the authorization attribute for the file_name entity.
        """

    def HasFs(self) -> bool:
        """
        Checks whether there is a file_schema entity. Returns True if there is one.
        """

    def FsValue(self) -> nanoocp.HeaderSection.HeaderSection_FileSchema:
        """
        Returns the file_schema entity. Returns an empty entity if the file_schema entity is not
        initialized.
        """

    def SetSchemaIdentifiers(self, aSchemaIdentifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def SetSchemaIdentifiersValue(self, num: int, aSchemaIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SchemaIdentifiers(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def SchemaIdentifiersValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of the schema_identifier attribute for the file_schema entity.
        """

    def NbSchemaIdentifiers(self) -> int:
        """
        Returns the number of values for the schema_identifier attribute in the file_schema entity.
        """

    def AddSchemaIdentifier(self, aSchemaIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Add a subname of schema (if not yet in the list)"""

    def HasFd(self) -> bool:
        """
        Checks whether there is a file_description entity. Returns True if there is one.
        """

    def FdValue(self) -> nanoocp.HeaderSection.HeaderSection_FileDescription:
        """
        Returns the file_description
        entity. Returns an empty entity if the file_description entity is not initialized.
        """

    def SetDescription(self, aDescription: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def SetDescriptionValue(self, num: int, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def DescriptionValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of the
        description attribute for the file_description entity.
        """

    def NbDescription(self) -> int:
        """
        Returns the number of values for
        the file_description entity in the STEP file header.
        """

    def SetImplementationLevel(self, aImplementationLevel: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ImplementationLevel(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value of the
        implementation_level attribute for the file_description entity.
        """
