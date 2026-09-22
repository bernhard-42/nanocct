"""OCCT package StepAP214 (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.StepVisual
import nanoocp.TCollection


class StepAP214:
    """
    Complete AP214 CC1 , Revision 4
    Upgrading from Revision 2 to Revision 4 : 26 Mar 1997
    Splitting in sub-schemas : 5 Nov 1997
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP214) -> None: ...

    @staticmethod
    def Protocol() -> StepAP214_Protocol:
        """creates a Protocol"""

class StepAP214_ApprovalItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ApprovalItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_ApprovalItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ApprovalItem Kind Entity that is :
        1 -> AssemblyComponentUsageSubstitute
        2 -> DocumentFile
        3 -> MaterialDesignation
        4 -> MechanicalDesignGeometricPresentationRepresentation
        5 -> PresentationArea
        6 -> Product
        7 -> ProductDefinition
        8 -> ProductDefinitionFormation
        9 -> ProductDefinitionRelationship
        10 -> PropertyDefinition
        11 -> ShapeRepresentation
        12 -> SecurityClassification
        13 -> ConfigurationItem
        14 -> Date
        15 -> Document
        16 -> Effectivity
        17 -> Group
        18 -> GroupRelationship
        19 -> ProductDefinitionFormationRelationship
        20 -> Representation
        21 -> ShapeAspectRelationship
        0 else
        """

    def AssemblyComponentUsageSubstitute(self) -> nanoocp.StepRepr.StepRepr_AssemblyComponentUsageSubstitute:
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
        """

    def DocumentFile(self) -> nanoocp.StepBasic.StepBasic_DocumentFile:
        """returns Value as a DocumentFile (Null if another type)"""

    def MaterialDesignation(self) -> nanoocp.StepRepr.StepRepr_MaterialDesignation:
        """returns Value as a MaterialDesignation (Null if another type)"""

    def MechanicalDesignGeometricPresentationRepresentation(self) -> nanoocp.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation:
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
        """

    def PresentationArea(self) -> nanoocp.StepVisual.StepVisual_PresentationArea:
        """returns Value as a PresentationArea (Null if another type)"""

    def Product(self) -> nanoocp.StepBasic.StepBasic_Product:
        """returns Value as a Product (Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """returns Value as a ProductDefinitionFormation (Null if another type)"""

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """returns Value as aProductDefinitionRelationship (Null if another type)"""

    def PropertyDefinition(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinition:
        """returns Value as a PropertyDefinition (Null if another type)"""

    def ShapeRepresentation(self) -> nanoocp.StepShape.StepShape_ShapeRepresentation:
        """returns Value as a ShapeRepresentation (Null if another type)"""

    def SecurityClassification(self) -> nanoocp.StepBasic.StepBasic_SecurityClassification:
        """returns Value as a SecurityClassification (Null if another type)"""

    def ConfigurationItem(self) -> nanoocp.StepRepr.StepRepr_ConfigurationItem:
        """returns Value as a ConfigurationItem (Null if another type)"""

    def Date(self) -> nanoocp.StepBasic.StepBasic_Date:
        """returns Value as a Date (Null if another type)"""

    def Document(self) -> nanoocp.StepBasic.StepBasic_Document:
        """returns Value as a Document (Null if another type)"""

    def Effectivity(self) -> nanoocp.StepBasic.StepBasic_Effectivity:
        """returns Value as a Effectivity (Null if another type)"""

    def Group(self) -> nanoocp.StepBasic.StepBasic_Group:
        """returns Value as a Group (Null if another type)"""

    def GroupRelationship(self) -> nanoocp.StepBasic.StepBasic_GroupRelationship:
        """returns Value as a GroupRelationship (Null if another type)"""

    def ProductDefinitionFormationRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormationRelationship:
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def ShapeAspectRelationship(self) -> nanoocp.StepRepr.StepRepr_ShapeAspectRelationship:
        """returns Value as a ShapeAspectRelationship (Null if another type)"""

class StepAP214_AppliedApprovalAssignment(nanoocp.StepBasic.StepBasic_ApprovalAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AppliedApprovalAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedApprovalAssignment) -> None: ...

    def Init(self, aAssignedApproval: nanoocp.StepBasic.StepBasic_Approval | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ApprovalItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ApprovalItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ApprovalItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_ApprovalItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_DateAndTimeItem(StepAP214_ApprovalItem):
    @overload
    def __init__(self) -> None:
        """Returns a DateAndTimeItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_DateAndTimeItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a DateAndTimeItem Kind Entity that is :
        1 -> ApprovalPersonOrganization
        2 -> AppliedDateAndPersonAssignment
        3 -> AppliedOrganizationAssignment
        4 -> AssemblyComponentUsageSubstitute
        5 -> DocumentFile
        6 -> Effectivity
        7 -> MaterialDesignation
        8 -> MechanicalDesignGeometricPresentationRepresentation
        9 -> PresentationArea
        10 -> Product
        11 -> ProductDefinition
        12 -> ProductDefinitionFormation
        13 -> ProductDefinitionRelationship
        14 -> PropertyDefinition
        15 -> ShapeRepresentation
        16 -> SecurityClassification
        0 else
        """

    def ApprovalPersonOrganization(self) -> nanoocp.StepBasic.StepBasic_ApprovalPersonOrganization:
        """returns Value as a ApprovalPersonOrganization (Null if another type)"""

    def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment:
        """
        returns Value as a AppliedDateAndPersonAssignment (Null if another type)
        """

    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment:
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """

class StepAP214_AppliedDateAndTimeAssignment(nanoocp.StepBasic.StepBasic_DateAndTimeAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AppliedDateAndTimeAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedDateAndTimeAssignment) -> None: ...

    def Init(self, aAssignedDateAndTime: nanoocp.StepBasic.StepBasic_DateAndTime | None, aRole: nanoocp.StepBasic.StepBasic_DateTimeRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateAndTimeItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateAndTimeItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateAndTimeItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_DateAndTimeItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_DateItem(StepAP214_ApprovalItem):
    @overload
    def __init__(self) -> None:
        """Returns a DateItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_DateItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a DateItem Kind Entity that is :
        1 -> ApprovalPersonOrganization
        2 -> AppliedDateAndPersonAssignment
        3 -> AppliedOrganizationAssignment
        4 -> AssemblyComponentUsageSubstitute
        5 -> DocumentFile
        6 -> Effectivity
        7 -> MaterialDesignation
        8 -> MechanicalDesignGeometricPresentationRepresentation
        9 -> PresentationArea
        10 -> Product
        11 -> ProductDefinition
        12 -> ProductDefinitionFormation
        13 -> ProductDefinitionRelationship
        14 -> PropertyDefinition
        15 -> ShapeRepresentation
        16 -> AppliedSecurityClassificationAssignment
        17 -> Document
        0 else
        """

    def ApprovalPersonOrganization(self) -> nanoocp.StepBasic.StepBasic_ApprovalPersonOrganization:
        """returns Value as a ApprovalPersonOrganization (Null if another type)"""

    def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment:
        """
        returns Value as a AppliedDateAndPersonAssignment (Null if another type)
        """

    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment:
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """

    def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment:
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """

class StepAP214_AppliedDateAssignment(nanoocp.StepBasic.StepBasic_DateAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AppliedDateAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedDateAssignment) -> None: ...

    def Init(self, aAssignedDate: nanoocp.StepBasic.StepBasic_Date | None, aRole: nanoocp.StepBasic.StepBasic_DateRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_DateItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_DocumentReferenceItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a DocumentReferenceItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_DocumentReferenceItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """Recognizes a DocumentReferenceItem Kind Entity that is :"""

    def Approval(self) -> nanoocp.StepBasic.StepBasic_Approval:
        """returns Value as a Approval (Null if another type)"""

    def DescriptiveRepresentationItem(self) -> nanoocp.StepRepr.StepRepr_DescriptiveRepresentationItem:
        """returns Value as a (Null if another type)"""

    def MaterialDesignation(self) -> nanoocp.StepRepr.StepRepr_MaterialDesignation:
        """returns Value as a MaterialDesignation (Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """returns Value as aProductDefinitionRelationship (Null if another type)"""

    def PropertyDefinition(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinition:
        """returns Value as a PropertyDefinition (Null if another type)"""

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def ShapeAspectRelationship(self) -> nanoocp.StepRepr.StepRepr_ShapeAspectRelationship:
        """returns Value as a ShapeAspectRelationship (Null if another type)"""

    def AppliedExternalIdentificationAssignment(self) -> StepAP214_AppliedExternalIdentificationAssignment:
        """
        returns Value as a AppliedExternalIdentificationAssignment (Null if another type)
        """

    def AssemblyComponentUsage(self) -> nanoocp.StepRepr.StepRepr_AssemblyComponentUsage:
        """returns Value as a AssemblyComponentUsage (Null if another type)"""

    def CharacterizedObject(self) -> nanoocp.StepBasic.StepBasic_CharacterizedObject:
        """returns Value as a CharacterizedObject (Null if another type)"""

    def DimensionalSize(self) -> nanoocp.StepShape.StepShape_DimensionalSize:
        """returns Value as a DimensionalSize (Null if another type)"""

    def ExternallyDefinedItem(self) -> nanoocp.StepBasic.StepBasic_ExternallyDefinedItem:
        """returns Value as a ExternallyDefinedItem (Null if another type)"""

    def Group(self) -> nanoocp.StepBasic.StepBasic_Group:
        """returns Value as a Group (Null if another type)"""

    def GroupRelationship(self) -> nanoocp.StepBasic.StepBasic_GroupRelationship:
        """returns Value as a GroupRelationship (Null if another type)"""

    def MeasureRepresentationItem(self) -> nanoocp.StepRepr.StepRepr_MeasureRepresentationItem:
        """returns Value as a MeasureRepresentationItem (Null if another type)"""

    def ProductCategory(self) -> nanoocp.StepBasic.StepBasic_ProductCategory:
        """returns Value as a ProductCategory (Null if another type)"""

    def ProductDefinitionContext(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionContext:
        """returns Value as a ProductDefinitionContext (Null if another type)"""

    def RepresentationItem(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """returns Value as a RepresentationItem (Null if another type)"""

class StepAP214_AppliedDocumentReference(nanoocp.StepBasic.StepBasic_DocumentReference):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP214_AppliedDocumentReference) -> None: ...

    def Init(self, aAssignedDocument: nanoocp.StepBasic.StepBasic_Document | None, aSource: nanoocp.TCollection.TCollection_HAsciiString | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DocumentReferenceItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DocumentReferenceItem]: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DocumentReferenceItem] | None) -> None: ...

    def ItemsValue(self, num: int) -> StepAP214_DocumentReferenceItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_ExternalIdentificationItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ExternalIdentificationItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_ExternalIdentificationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ExternalIdentificationItem select type
        1 -> DocumentFile from StepBasic
        2 -> ExternallyDefinedClass from StepAP214
        3 -> ExternallyDefinedGeneralProperty from StepAP214
        4 -> ProductDefinition from StepBasic
        5 -> AppliedOrganizationAssignment from AP214
        6 -> AppliedPersonAndOrganizationAssignment from AP214
        7 -> Approval from StepBasic
        8 -> ApprovalStatus from StepBasic
        9 -> ExternalSource from StepBasic
        10 -> OrganizationalAddress from StepBasic
        11 -> SecurityClassification from StepBasic
        12 -> TrimmedCurve from StepGeom
        13 -> VersionedActionRequest from StepBasic
        14 -> DateAndTimeAssignment from StepBasic
        15 -> DateAssignment from StepBasic
        0 else
        """

    def DocumentFile(self) -> nanoocp.StepBasic.StepBasic_DocumentFile:
        """Returns Value as DocumentFile (or Null if another type)"""

    def ExternallyDefinedClass(self) -> StepAP214_ExternallyDefinedClass:
        """Returns Value as ExternallyDefinedClass (or Null if another type)"""

    def ExternallyDefinedGeneralProperty(self) -> StepAP214_ExternallyDefinedGeneralProperty:
        """
        Returns Value as ExternallyDefinedGeneralProperty (or Null if another type)
        """

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment:
        """
        Returns Value as AppliedOrganizationAssignment (or Null if another type)
        """

    def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment:
        """
        Returns Value as AppliedPersonAndOrganizationAssignment (or Null if another type)
        """

    def Approval(self) -> nanoocp.StepBasic.StepBasic_Approval:
        """Returns Value as Approval (or Null if another type)"""

    def ApprovalStatus(self) -> nanoocp.StepBasic.StepBasic_ApprovalStatus:
        """Returns Value as ApprovalStatus (or Null if another type)"""

    def ExternalSource(self) -> nanoocp.StepBasic.StepBasic_ExternalSource:
        """Returns Value as ExternalSource (or Null if another type)"""

    def OrganizationalAddress(self) -> nanoocp.StepBasic.StepBasic_OrganizationalAddress:
        """Returns Value as OrganizationalAddress (or Null if another type)"""

    def SecurityClassification(self) -> nanoocp.StepBasic.StepBasic_SecurityClassification:
        """Returns Value as SecurityClassification (or Null if another type)"""

    def TrimmedCurve(self) -> nanoocp.StepGeom.StepGeom_TrimmedCurve:
        """Returns Value as TrimmedCurve (or Null if another type)"""

    def VersionedActionRequest(self) -> nanoocp.StepBasic.StepBasic_VersionedActionRequest:
        """Returns Value as VersionedActionRequest (or Null if another type)"""

    def DateAndTimeAssignment(self) -> nanoocp.StepBasic.StepBasic_DateAndTimeAssignment:
        """Returns Value as DateAndTimeAssignment (or Null if another type)"""

    def DateAssignment(self) -> nanoocp.StepBasic.StepBasic_DateAssignment:
        """Returns Value as DateAssignment (or Null if another type)"""

class StepAP214_AppliedExternalIdentificationAssignment(nanoocp.StepBasic.StepBasic_ExternalIdentificationAssignment):
    """Representation of STEP entity AppliedExternalIdentificationAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedExternalIdentificationAssignment) -> None: ...

    def Init(self, aIdentificationAssignment_AssignedId: nanoocp.TCollection.TCollection_HAsciiString | None, aIdentificationAssignment_Role: nanoocp.StepBasic.StepBasic_IdentificationRole | None, aExternalIdentificationAssignment_Source: nanoocp.StepBasic.StepBasic_ExternalSource | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ExternalIdentificationItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ExternalIdentificationItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ExternalIdentificationItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_GroupItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a GroupItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_GroupItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a GroupItem Kind Entity that is :
        1 ->  GeometricRepresentationItem
        2 ->  GroupRelationship
        3 ->  MappedItem
        4 ->  ProductDefinition
        5 ->  ProductDefinitionFormation
        6 ->  PropertyDefinitionRepresentation
        7 ->  Representation
        8 ->  RepresentationItem
        9 ->  RepresentationRelationshipWithTransformation
        10 -> ShapeAspect
        11 -> ShapeAspectRelationship
        12 -> ShapeRepresentationRelationship
        13 -> StyledItem
        14 -> TopologicalRepresentationItem
        0 else
        """

    def GeometricRepresentationItem(self) -> nanoocp.StepGeom.StepGeom_GeometricRepresentationItem:
        """returns Value as a GeometricRepresentationItem (Null if another type)"""

    def GroupRelationship(self) -> nanoocp.StepBasic.StepBasic_GroupRelationship:
        """returns Value as a GroupRelationship (Null if another type)"""

    def MappedItem(self) -> nanoocp.StepRepr.StepRepr_MappedItem:
        """returns Value as a MappedItem (Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """returns Value as a ProductDefinitionFormation (Null if another type)"""

    def PropertyDefinitionRepresentation(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation:
        """
        returns Value as a PropertyDefinitionRepresentation (Null if another type)
        """

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def RepresentationItem(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """returns Value as a RepresentationItem (Null if another type)"""

    def RepresentationRelationshipWithTransformation(self) -> nanoocp.StepRepr.StepRepr_RepresentationRelationshipWithTransformation:
        """
        returns Value as a RepresentationRelationshipWithTransformation (Null if another type)
        """

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def ShapeAspectRelationship(self) -> nanoocp.StepRepr.StepRepr_ShapeAspectRelationship:
        """returns Value as a ShapeAspectRelationship (Null if another type)"""

    def ShapeRepresentationRelationship(self) -> nanoocp.StepRepr.StepRepr_ShapeRepresentationRelationship:
        """
        returns Value as a ShapeRepresentationRelationship (Null if another type)
        """

    def StyledItem(self) -> nanoocp.StepVisual.StepVisual_StyledItem:
        """returns Value as a StyledItem (Null if another type)"""

    def TopologicalRepresentationItem(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem:
        """
        returns Value as a TopologicalRepresentationItem (Null if another type)
        """

class StepAP214_AppliedGroupAssignment(nanoocp.StepBasic.StepBasic_GroupAssignment):
    """Representation of STEP entity AppliedGroupAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedGroupAssignment) -> None: ...

    def Init(self, aGroupAssignment_AssignedGroup: nanoocp.StepBasic.StepBasic_Group | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_GroupItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_GroupItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_GroupItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_OrganizationItem(StepAP214_ApprovalItem):
    @overload
    def __init__(self) -> None:
        """Returns a OrganizationItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_OrganizationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """Recognizes a OrganizationItem Kind Entity that is :"""

    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment:
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """

    def Approval(self) -> nanoocp.StepBasic.StepBasic_Approval:
        """returns Value as a Approval (Null if another type)"""

    def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment:
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """

class StepAP214_AppliedOrganizationAssignment(nanoocp.StepBasic.StepBasic_OrganizationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AppliedOrganizationAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedOrganizationAssignment) -> None: ...

    def Init(self, aAssignedOrganization: nanoocp.StepBasic.StepBasic_Organization | None, aRole: nanoocp.StepBasic.StepBasic_OrganizationRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_OrganizationItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_OrganizationItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_OrganizationItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_OrganizationItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_PersonAndOrganizationItem(StepAP214_ApprovalItem):
    @overload
    def __init__(self) -> None:
        """Returns a PersonAndOrganizationItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_PersonAndOrganizationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a APersonAndOrganizationItem Kind Entity that is :
        1 -> AppliedOrganizationAssignment
        2 -> AssemblyComponentUsageSubstitute
        3 -> DocumentFile
        4 -> MaterialDesignation
        5 -> MechanicalDesignGeometricPresentationRepresentation
        6 -> PresentationArea
        7 -> Product
        8 -> ProductDefinition
        9 -> ProductDefinitionFormation
        10 -> ProductDefinitionRelationship
        11 -> PropertyDefinition
        12 -> ShapeRepresentation
        13 -> SecurityClassification
        14 -> AppliedSecurityClassificationAssignment
        15 -> Approval
        0 else
        """

    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment:
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """

    def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment:
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """

    def Approval(self) -> nanoocp.StepBasic.StepBasic_Approval:
        """returns Value as a Approval (Null if another type)"""

class StepAP214_AppliedPersonAndOrganizationAssignment(nanoocp.StepBasic.StepBasic_PersonAndOrganizationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignDateAndPersonAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedPersonAndOrganizationAssignment) -> None: ...

    def Init(self, aAssignedPersonAndOrganization: nanoocp.StepBasic.StepBasic_PersonAndOrganization | None, aRole: nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PersonAndOrganizationItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PersonAndOrganizationItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PersonAndOrganizationItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_PersonAndOrganizationItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_PresentedItemSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a PresentedItemSelect SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_PresentedItemSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a PresentedItemSelect Kind Entity that is :
        1 -> ProductDefinition,
        2 -> ProductDefinitionRelationship,
        0 else
        """

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

class StepAP214_AppliedPresentedItem(nanoocp.StepVisual.StepVisual_PresentedItem):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignPresentedItem"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedPresentedItem) -> None: ...

    def Init(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PresentedItemSelect] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PresentedItemSelect] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PresentedItemSelect]: ...

    def ItemsValue(self, num: int) -> StepAP214_PresentedItemSelect: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_SecurityClassificationItem(StepAP214_ApprovalItem):
    @overload
    def __init__(self) -> None:
        """Returns a SecurityClassificationItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_SecurityClassificationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a SecurityClassificationItem Kind Entity that is :
        1 -> Action
        2 -> AssemblyComponentUsage
        3 -> AssemblyComponentUsageSubstitute
        4 -> ConfigurationDesign
        5 -> ConfigurationEffectivity
        6 -> Document
        7 -> DocumentFile
        8 -> DraughtingModel
        9 -> GeneralProperty
        10 -> MakeFromUsageOption
        11 -> MaterialDesignation
        12 -> MechanicalDesignGeometricPresentationRepresentation
        13 -> PresentationArea
        14 -> Product
        15 -> ProductConcept
        16 -> ProductDefinition
        17 -> ProductDefinitionFormation
        18 -> ProductDefinitionRelationship
        19 -> ProductDefinitionUsage
        20 -> PropertyDefinition
        21 -> ShapeRepresentation
        22 -> VersionedActionRequest
        0 else
        """

    def Action(self) -> nanoocp.StepBasic.StepBasic_Action:
        """returns Value as a Action (Null if another type)"""

    def AssemblyComponentUsage(self) -> nanoocp.StepRepr.StepRepr_AssemblyComponentUsage:
        """returns Value as a AssemblyComponentUsage (Null if another type)"""

    def ConfigurationDesign(self) -> nanoocp.StepRepr.StepRepr_ConfigurationDesign:
        """returns Value as a ConfigurationDesign (Null if another type)"""

    def ConfigurationEffectivity(self) -> nanoocp.StepRepr.StepRepr_ConfigurationEffectivity:
        """returns Value as a ConfigurationEffectivity (Null if another type)"""

    def DraughtingModel(self) -> nanoocp.StepVisual.StepVisual_DraughtingModel:
        """returns Value as a DraughtingModel (Null if another type)"""

    def GeneralProperty(self) -> nanoocp.StepBasic.StepBasic_GeneralProperty:
        """returns Value as a GeneralProperty (Null if another type)"""

    def MakeFromUsageOption(self) -> nanoocp.StepRepr.StepRepr_MakeFromUsageOption:
        """returns Value as a MakeFromUsageOption (Null if another type)"""

    def ProductConcept(self) -> nanoocp.StepRepr.StepRepr_ProductConcept:
        """returns Value as a ProductConcept (Null if another type)"""

    def ProductDefinitionUsage(self) -> nanoocp.StepRepr.StepRepr_ProductDefinitionUsage:
        """returns Value as a ProductDefinitionUsage (Null if another type)"""

    def VersionedActionRequest(self) -> nanoocp.StepBasic.StepBasic_VersionedActionRequest:
        """returns Value as a VersionedActionRequest (Null if another type)"""

class StepAP214_AppliedSecurityClassificationAssignment(nanoocp.StepBasic.StepBasic_SecurityClassificationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AppliedSecurityClassificationAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AppliedSecurityClassificationAssignment) -> None: ...

    def Init(self, aAssignedSecurityClassification: nanoocp.StepBasic.StepBasic_SecurityClassification | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_SecurityClassificationItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_SecurityClassificationItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_SecurityClassificationItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_SecurityClassificationItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignDateAndTimeItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignDateAndTimeItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignDateAndTimeItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignDateAndTimeItem Kind Entity that is :
        1 -> ApprovalPersonOrganization
        2 -> AutoDesignDateAndPersonAssignment
        0 else
        """

    def ApprovalPersonOrganization(self) -> nanoocp.StepBasic.StepBasic_ApprovalPersonOrganization:
        """returns Value as a ApprovalPersonOrganization (Null if another type)"""

    def AutoDesignDateAndPersonAssignment(self) -> StepAP214_AutoDesignDateAndPersonAssignment:
        """
        returns Value as a AutoDesignDateAndPersonAssignment (Null if another type)
        """

    def ProductDefinitionEffectivity(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionEffectivity: ...

class StepAP214_AutoDesignActualDateAndTimeAssignment(nanoocp.StepBasic.StepBasic_DateAndTimeAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignActualDateAndTimeAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignActualDateAndTimeAssignment) -> None: ...

    def Init(self, aAssignedDateAndTime: nanoocp.StepBasic.StepBasic_DateAndTime | None, aRole: nanoocp.StepBasic.StepBasic_DateTimeRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignDateAndTimeItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignDatedItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignDatedItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignDatedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignDatedItem Kind Entity that is :
        1 -> ApprovalPersonOrganization
        2 -> AutoDesignDateAndPersonAssignment
        0 else
        """

    def ApprovalPersonOrganization(self) -> nanoocp.StepBasic.StepBasic_ApprovalPersonOrganization:
        """returns Value as a ApprovalPersonOrganization (Null if another type)"""

    def AutoDesignDateAndPersonAssignment(self) -> StepAP214_AutoDesignDateAndPersonAssignment:
        """
        returns Value as a AutoDesignDateAndPersonAssignment (Null if another type)
        """

    def ProductDefinitionEffectivity(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionEffectivity:
        """returns Value as a ProductDefinitionEffectivity"""

class StepAP214_AutoDesignActualDateAssignment(nanoocp.StepBasic.StepBasic_DateAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignActualDateAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignActualDateAssignment) -> None: ...

    def Init(self, aAssignedDate: nanoocp.StepBasic.StepBasic_Date | None, aRole: nanoocp.StepBasic.StepBasic_DateRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignDatedItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignGeneralOrgItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignGeneralOrgItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignGeneralOrgItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignGeneralOrgItem Kind Entity that is :
        1     Product from StepBasic,
        2     ProductDefinition from StepBasic,
        3     ProductDefinitionFormation from StepBasic,
        4     ProductDefinitionRelationship from StepBasic,
        5     ProductDefinitionWithAssociatedDocuments from StepBasic,
        6     Representation from StepRepr
        7     ExternallyDefinedRepresentation from StepRepr,
        8     AutoDesignDocumentReference from StepAP214,
        0 else
        """

    def Product(self) -> nanoocp.StepBasic.StepBasic_Product:
        """returns Value as a Product (Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """returns Value as a ProductDefinitionFormation (Null if another type)"""

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """

    def ProductDefinitionWithAssociatedDocuments(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments:
        """
        returns Value as a ProductDefinitionWithAssociatedDocuments (Null if another type)
        """

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def ExternallyDefinedRepresentation(self) -> nanoocp.StepRepr.StepRepr_ExternallyDefinedRepresentation:
        """returns Value as a Representation (Null if another type)"""

    def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: ...

class StepAP214_AutoDesignApprovalAssignment(nanoocp.StepBasic.StepBasic_ApprovalAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignApprovalAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignApprovalAssignment) -> None: ...

    def Init(self, aAssignedApproval: nanoocp.StepBasic.StepBasic_Approval | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignGeneralOrgItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignDateAndPersonItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignDateAndPersonItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignDateAndPersonItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignDateAndPersonItem Kind Entity that is :
        1     AutoDesignOrganizationAssignment from StepAP214,
        2     Product from StepBasic,
        3     ProductDefinition from StepBasic,
        4     ProductDefinitionFormation from StepBasic,
        5     Representation from StepRepr,
        6     AutoDesignDocumentReference from StepAP214,
        7     ExternallyDefinedRepresentation from StepRepr,
        8     ProductDefinitionRelationship from StepBasic,
        9     ProductDefinitionWithAssociatedDocuments from StepBasic
        0 else
        """

    def AutoDesignOrganizationAssignment(self) -> StepAP214_AutoDesignOrganizationAssignment: ...

    def Product(self) -> nanoocp.StepBasic.StepBasic_Product: ...

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition: ...

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation: ...

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation: ...

    def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: ...

    def ExternallyDefinedRepresentation(self) -> nanoocp.StepRepr.StepRepr_ExternallyDefinedRepresentation: ...

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship: ...

    def ProductDefinitionWithAssociatedDocuments(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments: ...

class StepAP214_AutoDesignDateAndPersonAssignment(nanoocp.StepBasic.StepBasic_PersonAndOrganizationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignDateAndPersonAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignDateAndPersonAssignment) -> None: ...

    def Init(self, aAssignedPersonAndOrganization: nanoocp.StepBasic.StepBasic_PersonAndOrganization | None, aRole: nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndPersonItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndPersonItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndPersonItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignDateAndPersonItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignReferencingItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignReferencingItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignReferencingItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignReferencingItem Kind Entity that is :
        1     Approval from StepBasic,
        2     DocumentRelationship from StepBasic,
        3     ExternallyDefinedRepresentation from StepRepr,
        4     MappedItem from StepRepr,
        5     MaterialDesignation from StepRepr,
        6     PresentationArea from StepVisual,
        7     PresentationView from StepVisual,
        8     ProductCategory from StepBasic,
        9     ProductDefinition from StepBasic,
        10     ProductDefinitionRelationship from StepBasic,
        11     PropertyDefinition from StepBasic,
        12     Representation from StepRepr,
        13     RepresentationRelationship from StepRepr,
        14     ShapeAspect from StepRepr
        0 else
        """

    def Approval(self) -> nanoocp.StepBasic.StepBasic_Approval: ...

    def DocumentRelationship(self) -> nanoocp.StepBasic.StepBasic_DocumentRelationship: ...

    def ExternallyDefinedRepresentation(self) -> nanoocp.StepRepr.StepRepr_ExternallyDefinedRepresentation: ...

    def MappedItem(self) -> nanoocp.StepRepr.StepRepr_MappedItem: ...

    def MaterialDesignation(self) -> nanoocp.StepRepr.StepRepr_MaterialDesignation: ...

    def PresentationArea(self) -> nanoocp.StepVisual.StepVisual_PresentationArea: ...

    def PresentationView(self) -> nanoocp.StepVisual.StepVisual_PresentationView: ...

    def ProductCategory(self) -> nanoocp.StepBasic.StepBasic_ProductCategory: ...

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition: ...

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship: ...

    def PropertyDefinition(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinition: ...

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation: ...

    def RepresentationRelationship(self) -> nanoocp.StepRepr.StepRepr_RepresentationRelationship: ...

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect: ...

class StepAP214_AutoDesignDocumentReference(nanoocp.StepBasic.StepBasic_DocumentReference):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignDocumentReference) -> None: ...

    def Init(self, aAssignedDocument: nanoocp.StepBasic.StepBasic_Document | None, aSource: nanoocp.TCollection.TCollection_HAsciiString | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignReferencingItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignReferencingItem]: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignReferencingItem] | None) -> None: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignReferencingItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignGroupedItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignGroupedItem SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignGroupedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignGroupedItem Kind Entity that is :
        1 -> AdvancedBrepShapeRepresentation
        2 -> CsgShapeRepresentation
        3 -> FacetedBrepShapeRepresentation
        4 -> GeometricallyBoundedSurfaceShapeRepresentation
        5 -> GeometricallyBoundedWireframeShapeRepresentation
        6 -> ManifoldSurfaceShapeRepresentation
        7 -> Representation
        8 -> RepresentationItem
        9 -> ShapeAspect
        10 -> ShapeRepresentation
        11 -> TemplateInstance
        0 else
        """

    def AdvancedBrepShapeRepresentation(self) -> nanoocp.StepShape.StepShape_AdvancedBrepShapeRepresentation:
        """
        returns Value as a AdvancedBrepShapeRepresentation (Null if another type)
        """

    def CsgShapeRepresentation(self) -> nanoocp.StepShape.StepShape_CsgShapeRepresentation:
        """returns Value as a CsgShapeRepresentation (Null if another type)"""

    def FacetedBrepShapeRepresentation(self) -> nanoocp.StepShape.StepShape_FacetedBrepShapeRepresentation:
        """
        returns Value as a FacetedBrepShapeRepresentation (Null if another type)
        """

    def GeometricallyBoundedSurfaceShapeRepresentation(self) -> nanoocp.StepShape.StepShape_GeometricallyBoundedSurfaceShapeRepresentation:
        """
        returns Value as a GeometricallyBoundedSurfaceShapeRepresentation (Null if another type)
        """

    def GeometricallyBoundedWireframeShapeRepresentation(self) -> nanoocp.StepShape.StepShape_GeometricallyBoundedWireframeShapeRepresentation:
        """
        returns Value as a GeometricallyBoundedWireframeShapeRepresentation (Null if another type)
        """

    def ManifoldSurfaceShapeRepresentation(self) -> nanoocp.StepShape.StepShape_ManifoldSurfaceShapeRepresentation:
        """
        returns Value as a ManifoldSurfaceShapeRepresentation (Null if another type)
        """

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def RepresentationItem(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """returns Value as a RepresentationItem (Null if another type)"""

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def ShapeRepresentation(self) -> nanoocp.StepShape.StepShape_ShapeRepresentation:
        """returns Value as a ShapeRepresentation (Null if another type)"""

    def TemplateInstance(self) -> nanoocp.StepVisual.StepVisual_TemplateInstance:
        """returns Value as a TemplateInstance (Null if another type)"""

class StepAP214_AutoDesignGroupAssignment(nanoocp.StepBasic.StepBasic_GroupAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignGroupAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignGroupAssignment) -> None: ...

    def Init(self, aAssignedGroup: nanoocp.StepBasic.StepBasic_Group | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGroupedItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGroupedItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGroupedItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignGroupedItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignNominalDateAndTimeAssignment(nanoocp.StepBasic.StepBasic_DateAndTimeAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignNominalDateAndTimeAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignNominalDateAndTimeAssignment) -> None: ...

    def Init(self, aAssignedDateAndTime: nanoocp.StepBasic.StepBasic_DateAndTime | None, aRole: nanoocp.StepBasic.StepBasic_DateTimeRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignDateAndTimeItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignNominalDateAssignment(nanoocp.StepBasic.StepBasic_DateAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignNominalDateAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignNominalDateAssignment) -> None: ...

    def Init(self, aAssignedDate: nanoocp.StepBasic.StepBasic_Date | None, aRole: nanoocp.StepBasic.StepBasic_DateRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignDatedItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignOrganizationAssignment(nanoocp.StepBasic.StepBasic_OrganizationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignOrganizationAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignOrganizationAssignment) -> None: ...

    def Init(self, aAssignedOrganization: nanoocp.StepBasic.StepBasic_Organization | None, aRole: nanoocp.StepBasic.StepBasic_OrganizationRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignGeneralOrgItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignOrganizationItem(StepAP214_AutoDesignGeneralOrgItem):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignOrganizationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int: ...

    def Document(self) -> nanoocp.StepBasic.StepBasic_Document: ...

    def PhysicallyModeledProductDefinition(self) -> nanoocp.StepBasic.StepBasic_PhysicallyModeledProductDefinition: ...

class StepAP214_AutoDesignPersonAndOrganizationAssignment(nanoocp.StepBasic.StepBasic_PersonAndOrganizationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignPersonAndOrganizationAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignPersonAndOrganizationAssignment) -> None: ...

    def Init(self, aAssignedPersonAndOrganization: nanoocp.StepBasic.StepBasic_PersonAndOrganization | None, aRole: nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignGeneralOrgItem: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignPresentedItemSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignPresentedItemSelect SelectType"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignPresentedItemSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AutoDesignPresentedItemSelect Kind Entity that is :
        1 -> ProductDefinition,
        2 -> ProductDefinitionRelationship,
        3 -> ProductDefinitionShape
        4 -> RepresentationRelationship
        5 -> ShapeAspect
        6 -> DocumentRelationship,
        0 else
        """

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

    def ProductDefinitionShape(self) -> nanoocp.StepRepr.StepRepr_ProductDefinitionShape:
        """returns Value as a ProductDefinitionShape (Null if another type)"""

    def RepresentationRelationship(self) -> nanoocp.StepRepr.StepRepr_RepresentationRelationship:
        """returns Value as a RepresentationRelationship (Null if another type)"""

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def DocumentRelationship(self) -> nanoocp.StepBasic.StepBasic_DocumentRelationship:
        """returns Value as a DocumentRelationship (Null if another type)"""

class StepAP214_AutoDesignPresentedItem(nanoocp.StepVisual.StepVisual_PresentedItem):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignPresentedItem"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignPresentedItem) -> None: ...

    def Init(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignPresentedItemSelect] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignPresentedItemSelect] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignPresentedItemSelect]: ...

    def ItemsValue(self, num: int) -> StepAP214_AutoDesignPresentedItemSelect: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_AutoDesignSecurityClassificationAssignment(nanoocp.StepBasic.StepBasic_SecurityClassificationAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a AutoDesignSecurityClassificationAssignment"""

    @overload
    def __init__(self, theOther: StepAP214_AutoDesignSecurityClassificationAssignment) -> None: ...

    def Init(self, aAssignedSecurityClassification: nanoocp.StepBasic.StepBasic_SecurityClassification | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Approval] | None) -> None: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Approval] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Approval]: ...

    def ItemsValue(self, num: int) -> nanoocp.StepBasic.StepBasic_Approval: ...

    def NbItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_Class(nanoocp.StepBasic.StepBasic_Group):
    """Representation of STEP entity Class"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_Class) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_ExternallyDefinedClass(StepAP214_Class):
    """Representation of STEP entity ExternallyDefinedClass"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_ExternallyDefinedClass) -> None: ...

    def Init(self, aGroup_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasGroup_Description: bool, aGroup_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aExternallyDefinedItem_ItemId: nanoocp.StepBasic.StepBasic_SourceItem, aExternallyDefinedItem_Source: nanoocp.StepBasic.StepBasic_ExternalSource | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ExternallyDefinedItem(self) -> nanoocp.StepBasic.StepBasic_ExternallyDefinedItem:
        """Returns data for supertype ExternallyDefinedItem"""

    def SetExternallyDefinedItem(self, ExternallyDefinedItem: nanoocp.StepBasic.StepBasic_ExternallyDefinedItem | None) -> None:
        """Set data for supertype ExternallyDefinedItem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_ExternallyDefinedGeneralProperty(nanoocp.StepBasic.StepBasic_GeneralProperty):
    """Representation of STEP entity ExternallyDefinedGeneralProperty"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_ExternallyDefinedGeneralProperty) -> None: ...

    def Init(self, aGeneralProperty_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aGeneralProperty_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasGeneralProperty_Description: bool, aGeneralProperty_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aExternallyDefinedItem_ItemId: nanoocp.StepBasic.StepBasic_SourceItem, aExternallyDefinedItem_Source: nanoocp.StepBasic.StepBasic_ExternalSource | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ExternallyDefinedItem(self) -> nanoocp.StepBasic.StepBasic_ExternallyDefinedItem:
        """Returns data for supertype ExternallyDefinedItem"""

    def SetExternallyDefinedItem(self, ExternallyDefinedItem: nanoocp.StepBasic.StepBasic_ExternallyDefinedItem | None) -> None:
        """Set data for supertype ExternallyDefinedItem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_Protocol(nanoocp.StepData.StepData_Protocol):
    """
    Protocol for StepAP214 Entities
    It requires StepAP214 as a Resource
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepAP214_Protocol) -> None: ...

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """Returns a Case Number for each of the StepAP214 Entities"""

    def SchemaName(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> str: ...

    def NbResources(self) -> int:
        """Returns count of Protocol used as Resources (level one)"""

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given its rank (between 1 and NbResources)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP214_RepItemGroup(nanoocp.StepBasic.StepBasic_Group):
    """Representation of STEP entity RepItemGroup"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP214_RepItemGroup) -> None: ...

    def Init(self, aGroup_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasGroup_Description: bool, aGroup_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def RepresentationItem(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """Returns data for supertype RepresentationItem"""

    def SetRepresentationItem(self, RepresentationItem: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> None:
        """Set data for supertype RepresentationItem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepAP214
StepAP214_Array1OfApprovalItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_ApprovalItem]
StepAP214_Array1OfAutoDesignDateAndPersonItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndPersonItem]
StepAP214_Array1OfAutoDesignDateAndTimeItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem]
StepAP214_Array1OfAutoDesignDatedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem]
StepAP214_Array1OfAutoDesignGeneralOrgItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem]
StepAP214_Array1OfAutoDesignGroupedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignGroupedItem]
StepAP214_Array1OfAutoDesignPresentedItemSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignPresentedItemSelect]
StepAP214_Array1OfAutoDesignReferencingItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_AutoDesignReferencingItem]
StepAP214_Array1OfDateAndTimeItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_DateAndTimeItem]
StepAP214_Array1OfDateItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_DateItem]
StepAP214_Array1OfDocumentReferenceItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_DocumentReferenceItem]
StepAP214_Array1OfExternalIdentificationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_ExternalIdentificationItem]
StepAP214_Array1OfGroupItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_GroupItem]
StepAP214_Array1OfOrganizationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_OrganizationItem]
StepAP214_Array1OfPersonAndOrganizationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_PersonAndOrganizationItem]
StepAP214_Array1OfPresentedItemSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_PresentedItemSelect]
StepAP214_Array1OfSecurityClassificationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP214.StepAP214_SecurityClassificationItem]
StepAP214_HArray1OfApprovalItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ApprovalItem]
StepAP214_HArray1OfAutoDesignDateAndPersonItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndPersonItem]
StepAP214_HArray1OfAutoDesignDateAndTimeItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDateAndTimeItem]
StepAP214_HArray1OfAutoDesignDatedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignDatedItem]
StepAP214_HArray1OfAutoDesignGeneralOrgItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGeneralOrgItem]
StepAP214_HArray1OfAutoDesignGroupedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignGroupedItem]
StepAP214_HArray1OfAutoDesignPresentedItemSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignPresentedItemSelect]
StepAP214_HArray1OfAutoDesignReferencingItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_AutoDesignReferencingItem]
StepAP214_HArray1OfDateAndTimeItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateAndTimeItem]
StepAP214_HArray1OfDateItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DateItem]
StepAP214_HArray1OfDocumentReferenceItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_DocumentReferenceItem]
StepAP214_HArray1OfExternalIdentificationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_ExternalIdentificationItem]
StepAP214_HArray1OfGroupItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_GroupItem]
StepAP214_HArray1OfOrganizationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_OrganizationItem]
StepAP214_HArray1OfPersonAndOrganizationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PersonAndOrganizationItem]
StepAP214_HArray1OfPresentedItemSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_PresentedItemSelect]
StepAP214_HArray1OfSecurityClassificationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP214.StepAP214_SecurityClassificationItem]
