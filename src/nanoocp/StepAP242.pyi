"""OCCT package StepAP242 (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepAP214
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepDimTol
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.TCollection


class StepAP242_ItemIdentifiedRepresentationUsageDefinition(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ItemIdentifiedRepresentationUsageDefinition select type"""

    @overload
    def __init__(self, theOther: StepAP242_ItemIdentifiedRepresentationUsageDefinition) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ItemIdentifiedRepresentationUsageDefinition Kind Entity that is :
        1 -> AppliedApprovalAssignment
        2 -> AppliedDateAndTimeAssignment
        3 -> AppliedDateAssignment
        4 -> AppliedDocumentReference
        5 -> AppliedExternalIdentificationAssignment
        6 -> AppliedGroupAssignment
        7 -> AppliedOrganizationAssignment
        8 -> AppliedPersonAndOrganizationAssignment
        9 -> AppliedSecurityClassificationAssignment
        10 -> DimensionalSize
        11 -> GeneralProperty
        12 -> GeometricTolerance
        13 -> ProductDefinitionRelationship
        14 -> PropertyDefinition
        15 -> PropertyDefinitionRelationship
        16 -> ShapeAspect
        17 -> ShapeAspectRelationship
        0 else
        """

    def AppliedApprovalAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedApprovalAssignment:
        """returns Value as a AppliedApprovalAssignment (Null if another type)"""

    def AppliedDateAndTimeAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedDateAndTimeAssignment:
        """returns Value as a AppliedDateAndTimeAssignment (Null if another type)"""

    def AppliedDateAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedDateAssignment:
        """returns Value as a AppliedDateAssignment (Null if another type)"""

    def AppliedDocumentReference(self) -> nanoocp.StepAP214.StepAP214_AppliedDocumentReference:
        """returns Value as a AppliedDocumentReference (Null if another type)"""

    def AppliedExternalIdentificationAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedExternalIdentificationAssignment:
        """
        returns Value as a AppliedExternalIdentificationAssignment (Null if another type)
        """

    def AppliedGroupAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedGroupAssignment:
        """returns Value as a AppliedGroupAssignment (Null if another type)"""

    def AppliedOrganizationAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedOrganizationAssignment:
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """

    def AppliedPersonAndOrganizationAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedPersonAndOrganizationAssignment:
        """
        returns Value as a AppliedPersonAndOrganizationAssignment (Null if another type)
        """

    def AppliedSecurityClassificationAssignment(self) -> nanoocp.StepAP214.StepAP214_AppliedSecurityClassificationAssignment:
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """

    def DimensionalSize(self) -> nanoocp.StepShape.StepShape_DimensionalSize:
        """returns Value as a DimensionalSize (Null if another type)"""

    def GeneralProperty(self) -> nanoocp.StepBasic.StepBasic_GeneralProperty:
        """returns Value as a GeneralProperty (Null if another type)"""

    def GeometricTolerance(self) -> nanoocp.StepDimTol.StepDimTol_GeometricTolerance:
        """returns Value as a GeometricTolerance (Null if another type)"""

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """

    def PropertyDefinition(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinition:
        """returns Value as a PropertyDefinition (Null if another type)"""

    def PropertyDefinitionRelationship(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinitionRelationship:
        """
        returns Value as a PropertyDefinitionRelationship (Null if another type)
        """

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def ShapeAspectRelationship(self) -> nanoocp.StepRepr.StepRepr_ShapeAspectRelationship:
        """returns Value as a ShapeAspectRelationship (Null if another type)"""

class StepAP242_ItemIdentifiedRepresentationUsage(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ItemIdentifiedRepresentationUsage"""

    @overload
    def __init__(self, theOther: StepAP242_ItemIdentifiedRepresentationUsage) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theDefinition: StepAP242_ItemIdentifiedRepresentationUsageDefinition, theUsedRepresentation: nanoocp.StepRepr.StepRepr_Representation | None, theIdentifiedItem: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None) -> None:
        """Init all fields own and inherited"""

    def SetName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetDescription(self, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDefinition(self, theDefinition: StepAP242_ItemIdentifiedRepresentationUsageDefinition) -> None:
        """Set field Definition"""

    def Definition(self) -> StepAP242_ItemIdentifiedRepresentationUsageDefinition:
        """Returns field Definition"""

    def SetUsedRepresentation(self, theUsedRepresentation: nanoocp.StepRepr.StepRepr_Representation | None) -> None:
        """Set field UsedRepresentation"""

    def UsedRepresentation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """Returns field UsedRepresentation"""

    def IdentifiedItem(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem]:
        """Returns field IdentifiedItem"""

    def NbIdentifiedItem(self) -> int:
        """Returns number of identified items"""

    def SetIdentifiedItem(self, theIdentifiedItem: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None) -> None:
        """Set field IdentifiedItem"""

    def IdentifiedItemValue(self, num: int) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """Returns identified item with given number"""

    def SetIdentifiedItemValue(self, num: int, theItem: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> None:
        """Set identified item with given number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP242_DraughtingModelItemAssociation(StepAP242_ItemIdentifiedRepresentationUsage):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP242_DraughtingModelItemAssociation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP242_GeometricItemSpecificUsage(StepAP242_ItemIdentifiedRepresentationUsage):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP242_GeometricItemSpecificUsage) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP242_IdAttributeSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a IdAttributeSelect select type"""

    @overload
    def __init__(self, theOther: StepAP242_IdAttributeSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a IdAttributeSelect Kind Entity that is :
        1 -> Action
        2 -> Address
        3 -> ApplicationContext
        4 -> DimensionalSize
        5 -> GeometricTolerance
        6 -> Group
        7 -> Reserved for OrganizatonalProject (not implemented in OCCT)
        8 -> ProductCategory
        9 -> PropertyDefinition
        10 -> Representation
        11 -> ShapeAspect
        12 -> ShapeAspectRelationship
        0 else
        """

    def Action(self) -> nanoocp.StepBasic.StepBasic_Action:
        """returns Value as a Action (Null if another type)"""

    def Address(self) -> nanoocp.StepBasic.StepBasic_Address:
        """returns Value as a Address (Null if another type)"""

    def ApplicationContext(self) -> nanoocp.StepBasic.StepBasic_ApplicationContext:
        """returns Value as a ApplicationContext (Null if another type)"""

    def DimensionalSize(self) -> nanoocp.StepShape.StepShape_DimensionalSize:
        """returns Value as a DimensionalSize (Null if another type)"""

    def GeometricTolerance(self) -> nanoocp.StepDimTol.StepDimTol_GeometricTolerance:
        """returns Value as a GeometricTolerance (Null if another type)"""

    def Group(self) -> nanoocp.StepBasic.StepBasic_Group:
        """returns Value as a Group (Null if another type)"""

    def ProductCategory(self) -> nanoocp.StepBasic.StepBasic_ProductCategory:
        """returns Value as a ProductCategory (Null if another type)"""

    def PropertyDefinition(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinition:
        """returns Value as a PropertyDefinition (Null if another type)"""

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def ShapeAspectRelationship(self) -> nanoocp.StepRepr.StepRepr_ShapeAspectRelationship:
        """returns Value as a ShapeAspectRelationship (Null if another type)"""

class StepAP242_IdAttribute(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a IdAttribute"""

    @overload
    def __init__(self, theOther: StepAP242_IdAttribute) -> None: ...

    def Init(self, theAttributeValue: nanoocp.TCollection.TCollection_HAsciiString | None, theIdentifiedItem: StepAP242_IdAttributeSelect) -> None:
        """Init all field own and inherited"""

    def SetAttributeValue(self, theAttributeValue: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def AttributeValue(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field AttributeValue"""

    def SetIdentifiedItem(self, theIdentifiedItem: StepAP242_IdAttributeSelect) -> None:
        """Set field IdentifiedItem"""

    def IdentifiedItem(self) -> StepAP242_IdAttributeSelect:
        """Returns IdentifiedItem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
