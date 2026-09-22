"""OCCT package StepAP203 (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepRepr
import nanoocp.TCollection


class StepAP203_ApprovedItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ApprovedItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_ApprovedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ApprovedItem select type
        1 -> ProductDefinitionFormation from StepBasic
        2 -> ProductDefinition from StepBasic
        3 -> ConfigurationEffectivity from StepRepr
        4 -> ConfigurationItem from StepRepr
        5 -> SecurityClassification from StepBasic
        6 -> ChangeRequest from StepAP203
        7 -> Change from StepAP203
        8 -> StartRequest from StepAP203
        9 -> StartWork from StepAP203
        10 -> Certification from StepBasic
        11 -> Contract from StepBasic
        0 else
        """

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def ConfigurationEffectivity(self) -> nanoocp.StepRepr.StepRepr_ConfigurationEffectivity:
        """Returns Value as ConfigurationEffectivity (or Null if another type)"""

    def ConfigurationItem(self) -> nanoocp.StepRepr.StepRepr_ConfigurationItem:
        """Returns Value as ConfigurationItem (or Null if another type)"""

    def SecurityClassification(self) -> nanoocp.StepBasic.StepBasic_SecurityClassification:
        """Returns Value as SecurityClassification (or Null if another type)"""

    def ChangeRequest(self) -> StepAP203_ChangeRequest:
        """Returns Value as ChangeRequest (or Null if another type)"""

    def Change(self) -> StepAP203_Change:
        """Returns Value as Change (or Null if another type)"""

    def StartRequest(self) -> StepAP203_StartRequest:
        """Returns Value as StartRequest (or Null if another type)"""

    def StartWork(self) -> StepAP203_StartWork:
        """Returns Value as StartWork (or Null if another type)"""

    def Certification(self) -> nanoocp.StepBasic.StepBasic_Certification:
        """Returns Value as Certification (or Null if another type)"""

    def Contract(self) -> nanoocp.StepBasic.StepBasic_Contract:
        """Returns Value as Contract (or Null if another type)"""

class StepAP203_CcDesignApproval(nanoocp.StepBasic.StepBasic_ApprovalAssignment):
    """Representation of STEP entity CcDesignApproval"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignApproval) -> None: ...

    def Init(self, aApprovalAssignment_AssignedApproval: nanoocp.StepBasic.StepBasic_Approval | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ApprovedItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ApprovedItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ApprovedItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_CertifiedItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type CertifiedItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CertifiedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of CertifiedItem select type
        1 -> SuppliedPartRelationship from StepRepr
        0 else
        """

    def SuppliedPartRelationship(self) -> nanoocp.StepRepr.StepRepr_SuppliedPartRelationship:
        """Returns Value as SuppliedPartRelationship (or Null if another type)"""

class StepAP203_CcDesignCertification(nanoocp.StepBasic.StepBasic_CertificationAssignment):
    """Representation of STEP entity CcDesignCertification"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignCertification) -> None: ...

    def Init(self, aCertificationAssignment_AssignedCertification: nanoocp.StepBasic.StepBasic_Certification | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_CertifiedItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_CertifiedItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_CertifiedItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_ContractedItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ContractedItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_ContractedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ContractedItem select type
        1 -> ProductDefinitionFormation from StepBasic
        0 else
        """

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

class StepAP203_CcDesignContract(nanoocp.StepBasic.StepBasic_ContractAssignment):
    """Representation of STEP entity CcDesignContract"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignContract) -> None: ...

    def Init(self, aContractAssignment_AssignedContract: nanoocp.StepBasic.StepBasic_Contract | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ContractedItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ContractedItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ContractedItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_DateTimeItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type DateTimeItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_DateTimeItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of DateTimeItem select type
        1 -> ProductDefinition from StepBasic
        2 -> ChangeRequest from StepAP203
        3 -> StartRequest from StepAP203
        4 -> Change from StepAP203
        5 -> StartWork from StepAP203
        6 -> ApprovalPersonOrganization from StepBasic
        7 -> Contract from StepBasic
        8 -> SecurityClassification from StepBasic
        9 -> Certification from StepBasic
        0 else
        """

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def ChangeRequest(self) -> StepAP203_ChangeRequest:
        """Returns Value as ChangeRequest (or Null if another type)"""

    def StartRequest(self) -> StepAP203_StartRequest:
        """Returns Value as StartRequest (or Null if another type)"""

    def Change(self) -> StepAP203_Change:
        """Returns Value as Change (or Null if another type)"""

    def StartWork(self) -> StepAP203_StartWork:
        """Returns Value as StartWork (or Null if another type)"""

    def ApprovalPersonOrganization(self) -> nanoocp.StepBasic.StepBasic_ApprovalPersonOrganization:
        """Returns Value as ApprovalPersonOrganization (or Null if another type)"""

    def Contract(self) -> nanoocp.StepBasic.StepBasic_Contract:
        """Returns Value as Contract (or Null if another type)"""

    def SecurityClassification(self) -> nanoocp.StepBasic.StepBasic_SecurityClassification:
        """Returns Value as SecurityClassification (or Null if another type)"""

    def Certification(self) -> nanoocp.StepBasic.StepBasic_Certification:
        """Returns Value as Certification (or Null if another type)"""

class StepAP203_CcDesignDateAndTimeAssignment(nanoocp.StepBasic.StepBasic_DateAndTimeAssignment):
    """Representation of STEP entity CcDesignDateAndTimeAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignDateAndTimeAssignment) -> None: ...

    def Init(self, aDateAndTimeAssignment_AssignedDateAndTime: nanoocp.StepBasic.StepBasic_DateAndTime | None, aDateAndTimeAssignment_Role: nanoocp.StepBasic.StepBasic_DateTimeRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_DateTimeItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_DateTimeItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_DateTimeItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_PersonOrganizationItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type PersonOrganizationItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_PersonOrganizationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of PersonOrganizationItem select type
        1 -> Change from StepAP203
        2 -> StartWork from StepAP203
        3 -> ChangeRequest from StepAP203
        4 -> StartRequest from StepAP203
        5 -> ConfigurationItem from StepRepr
        6 -> Product from StepBasic
        7 -> ProductDefinitionFormation from StepBasic
        8 -> ProductDefinition from StepBasic
        9 -> Contract from StepBasic
        10 -> SecurityClassification from StepBasic
        0 else
        """

    def Change(self) -> StepAP203_Change:
        """Returns Value as Change (or Null if another type)"""

    def StartWork(self) -> StepAP203_StartWork:
        """Returns Value as StartWork (or Null if another type)"""

    def ChangeRequest(self) -> StepAP203_ChangeRequest:
        """Returns Value as ChangeRequest (or Null if another type)"""

    def StartRequest(self) -> StepAP203_StartRequest:
        """Returns Value as StartRequest (or Null if another type)"""

    def ConfigurationItem(self) -> nanoocp.StepRepr.StepRepr_ConfigurationItem:
        """Returns Value as ConfigurationItem (or Null if another type)"""

    def Product(self) -> nanoocp.StepBasic.StepBasic_Product:
        """Returns Value as Product (or Null if another type)"""

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def Contract(self) -> nanoocp.StepBasic.StepBasic_Contract:
        """Returns Value as Contract (or Null if another type)"""

    def SecurityClassification(self) -> nanoocp.StepBasic.StepBasic_SecurityClassification:
        """Returns Value as SecurityClassification (or Null if another type)"""

class StepAP203_CcDesignPersonAndOrganizationAssignment(nanoocp.StepBasic.StepBasic_PersonAndOrganizationAssignment):
    """Representation of STEP entity CcDesignPersonAndOrganizationAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignPersonAndOrganizationAssignment) -> None: ...

    def Init(self, aPersonAndOrganizationAssignment_AssignedPersonAndOrganization: nanoocp.StepBasic.StepBasic_PersonAndOrganization | None, aPersonAndOrganizationAssignment_Role: nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_PersonOrganizationItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_PersonOrganizationItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_PersonOrganizationItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_ClassifiedItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ClassifiedItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_ClassifiedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ClassifiedItem select type
        1 -> ProductDefinitionFormation from StepBasic
        2 -> AssemblyComponentUsage from StepRepr
        0 else
        """

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

    def AssemblyComponentUsage(self) -> nanoocp.StepRepr.StepRepr_AssemblyComponentUsage:
        """Returns Value as AssemblyComponentUsage (or Null if another type)"""

class StepAP203_CcDesignSecurityClassification(nanoocp.StepBasic.StepBasic_SecurityClassificationAssignment):
    """Representation of STEP entity CcDesignSecurityClassification"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignSecurityClassification) -> None: ...

    def Init(self, aSecurityClassificationAssignment_AssignedSecurityClassification: nanoocp.StepBasic.StepBasic_SecurityClassification | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ClassifiedItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ClassifiedItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ClassifiedItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_SpecifiedItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SpecifiedItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_SpecifiedItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SpecifiedItem select type
        1 -> ProductDefinition from StepBasic
        2 -> ShapeAspect from StepRepr
        0 else
        """

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """Returns Value as ShapeAspect (or Null if another type)"""

class StepAP203_CcDesignSpecificationReference(nanoocp.StepBasic.StepBasic_DocumentReference):
    """Representation of STEP entity CcDesignSpecificationReference"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_CcDesignSpecificationReference) -> None: ...

    def Init(self, aDocumentReference_AssignedDocument: nanoocp.StepBasic.StepBasic_Document | None, aDocumentReference_Source: nanoocp.TCollection.TCollection_HAsciiString | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_SpecifiedItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_SpecifiedItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_SpecifiedItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_WorkItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type WorkItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_WorkItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of WorkItem select type
        1 -> ProductDefinitionFormation from StepBasic
        0 else
        """

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

class StepAP203_Change(nanoocp.StepBasic.StepBasic_ActionAssignment):
    """Representation of STEP entity Change"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_Change) -> None: ...

    def Init(self, aActionAssignment_AssignedAction: nanoocp.StepBasic.StepBasic_Action | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_ChangeRequestItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ChangeRequestItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_ChangeRequestItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ChangeRequestItem select type
        1 -> ProductDefinitionFormation from StepBasic
        0 else
        """

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

class StepAP203_ChangeRequest(nanoocp.StepBasic.StepBasic_ActionRequestAssignment):
    """Representation of STEP entity ChangeRequest"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_ChangeRequest) -> None: ...

    def Init(self, aActionRequestAssignment_AssignedActionRequest: nanoocp.StepBasic.StepBasic_VersionedActionRequest | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ChangeRequestItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ChangeRequestItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ChangeRequestItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_StartRequestItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type StartRequestItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_StartRequestItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of StartRequestItem select type
        1 -> ProductDefinitionFormation from StepBasic
        0 else
        """

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

class StepAP203_StartRequest(nanoocp.StepBasic.StepBasic_ActionRequestAssignment):
    """Representation of STEP entity StartRequest"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_StartRequest) -> None: ...

    def Init(self, aActionRequestAssignment_AssignedActionRequest: nanoocp.StepBasic.StepBasic_VersionedActionRequest | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_StartRequestItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_StartRequestItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_StartRequestItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepAP203_StartWork(nanoocp.StepBasic.StepBasic_ActionAssignment):
    """Representation of STEP entity StartWork"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepAP203_StartWork) -> None: ...

    def Init(self, aActionAssignment_AssignedAction: nanoocp.StepBasic.StepBasic_Action | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem]:
        """Returns field Items"""

    def SetItems(self, Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem] | None) -> None:
        """Set field Items"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepAP203
StepAP203_Array1OfApprovedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_ApprovedItem]
StepAP203_Array1OfCertifiedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_CertifiedItem]
StepAP203_Array1OfChangeRequestItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_ChangeRequestItem]
StepAP203_Array1OfClassifiedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_ClassifiedItem]
StepAP203_Array1OfContractedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_ContractedItem]
StepAP203_Array1OfDateTimeItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_DateTimeItem]
StepAP203_Array1OfPersonOrganizationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_PersonOrganizationItem]
StepAP203_Array1OfSpecifiedItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_SpecifiedItem]
StepAP203_Array1OfStartRequestItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_StartRequestItem]
StepAP203_Array1OfWorkItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepAP203.StepAP203_WorkItem]
StepAP203_HArray1OfApprovedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ApprovedItem]
StepAP203_HArray1OfCertifiedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_CertifiedItem]
StepAP203_HArray1OfChangeRequestItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ChangeRequestItem]
StepAP203_HArray1OfClassifiedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ClassifiedItem]
StepAP203_HArray1OfContractedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_ContractedItem]
StepAP203_HArray1OfDateTimeItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_DateTimeItem]
StepAP203_HArray1OfPersonOrganizationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_PersonOrganizationItem]
StepAP203_HArray1OfSpecifiedItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_SpecifiedItem]
StepAP203_HArray1OfStartRequestItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_StartRequestItem]
StepAP203_HArray1OfWorkItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepAP203.StepAP203_WorkItem]
