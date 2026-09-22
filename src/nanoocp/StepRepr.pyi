"""OCCT package StepRepr (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepShape
import nanoocp.TCollection


class StepRepr_ShapeAspect(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ShapeAspect"""

    @overload
    def __init__(self, theOther: StepRepr_ShapeAspect) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aOfShape: StepRepr_ProductDefinitionShape | None, aProductDefinitional: nanoocp.StepData.StepData_Logical) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetOfShape(self, aOfShape: StepRepr_ProductDefinitionShape | None) -> None: ...

    def OfShape(self) -> StepRepr_ProductDefinitionShape: ...

    def SetProductDefinitional(self, aProductDefinitional: nanoocp.StepData.StepData_Logical) -> None: ...

    def ProductDefinitional(self) -> nanoocp.StepData.StepData_Logical: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CompositeShapeAspect(StepRepr_ShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CompositeShapeAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ContinuosShapeAspect(StepRepr_CompositeShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ContinuosShapeAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_AllAroundShapeAspect(StepRepr_ContinuosShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_AllAroundShapeAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_DerivedShapeAspect(StepRepr_ShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_DerivedShapeAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_Apex(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_Apex) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ProductDefinitionUsage(nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship):
    """Representation of STEP entity ProductDefinitionUsage"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ProductDefinitionUsage) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_AssemblyComponentUsage(StepRepr_ProductDefinitionUsage):
    """Representation of STEP entity AssemblyComponentUsage"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_AssemblyComponentUsage) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, hasReferenceDesignator: bool, aReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, hasReferenceDesignator: bool, aReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ReferenceDesignator(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field ReferenceDesignator"""

    def SetReferenceDesignator(self, ReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field ReferenceDesignator"""

    def HasReferenceDesignator(self) -> bool:
        """Returns True if optional field ReferenceDesignator is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_AssemblyComponentUsageSubstitute(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_AssemblyComponentUsageSubstitute) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDef: nanoocp.TCollection.TCollection_HAsciiString | None, aBase: StepRepr_AssemblyComponentUsage | None, aSubs: StepRepr_AssemblyComponentUsage | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Definition(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDefinition(self, aDef: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Base(self) -> StepRepr_AssemblyComponentUsage: ...

    def SetBase(self, aBase: StepRepr_AssemblyComponentUsage | None) -> None: ...

    def Substitute(self) -> StepRepr_AssemblyComponentUsage: ...

    def SetSubstitute(self, aSubstitute: StepRepr_AssemblyComponentUsage | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_BetweenShapeAspect(StepRepr_ContinuosShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_BetweenShapeAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationItem(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a RepresentationItem"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_BooleanRepresentationItem(StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a BooleanRepresentationItem"""

    @overload
    def __init__(self, theOther: StepRepr_BooleanRepresentationItem) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theValue: bool) -> None: ...

    def SetValue(self, theValue: bool) -> None: ...

    def Value(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CentreOfSymmetry(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CentreOfSymmetry) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CharacterizedDefinition(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type CharacterizedDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_CharacterizedDefinition) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of CharacterizedDefinition select type
        1 -> CharacterizedObject from StepBasic
        2 -> ProductDefinition from StepBasic
        3 -> ProductDefinitionRelationship from StepBasic
        4 -> ProductDefinitionShape from StepRepr
        5 -> ShapeAspect from StepRepr
        6 -> ShapeAspectRelationship from StepRepr
        7 -> DocumentFile from StepBasic
        0 else
        """

    def CharacterizedObject(self) -> nanoocp.StepBasic.StepBasic_CharacterizedObject:
        """Returns Value as CharacterizedObject (or Null if another type)"""

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def ProductDefinitionRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship:
        """
        Returns Value as ProductDefinitionRelationship (or Null if another type)
        """

    def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape:
        """Returns Value as ProductDefinitionShape (or Null if another type)"""

    def ShapeAspect(self) -> StepRepr_ShapeAspect:
        """Returns Value as ShapeAspect (or Null if another type)"""

    def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship:
        """Returns Value as ShapeAspectRelationship (or Null if another type)"""

    def DocumentFile(self) -> nanoocp.StepBasic.StepBasic_DocumentFile:
        """Returns Value as DocumentFile (or Null if another type)"""

class StepRepr_Representation(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Representation"""

    @overload
    def __init__(self, theOther: StepRepr_Representation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aContextOfItems: StepRepr_RepresentationContext | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetItems(self, aItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None) -> None: ...

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem]: ...

    def ItemsValue(self, num: int) -> StepRepr_RepresentationItem: ...

    def NbItems(self) -> int: ...

    def SetContextOfItems(self, aContextOfItems: StepRepr_RepresentationContext | None) -> None: ...

    def ContextOfItems(self) -> StepRepr_RepresentationContext: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CharacterizedRepresentation(StepRepr_Representation):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CharacterizedRepresentation) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theContextOfItems: StepRepr_RepresentationContext | None) -> None:
        """Returns a CharacterizedRepresentation"""

    def SetDescription(self, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CompShAspAndDatumFeatAndShAsp(StepRepr_ShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CompShAspAndDatumFeatAndShAsp) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp(StepRepr_CompShAspAndDatumFeatAndShAsp):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CompositeGroupShapeAspect(StepRepr_CompositeShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CompositeGroupShapeAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_CompoundRepresentationItem(StepRepr_RepresentationItem):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_CompoundRepresentationItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, item_element: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None) -> None: ...

    def ItemElement(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem]: ...

    def NbItemElement(self) -> int: ...

    def SetItemElement(self, item_element: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None) -> None: ...

    def ItemElementValue(self, num: int) -> StepRepr_RepresentationItem: ...

    def SetItemElementValue(self, num: int, anelement: StepRepr_RepresentationItem | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ConfigurationDesignItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ConfigurationDesignItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ConfigurationDesignItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ConfigurationDesignItem select type
        1 -> ProductDefinition from StepBasic
        2 -> ProductDefinitionFormation from StepBasic
        0 else
        """

    def ProductDefinition(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

    def ProductDefinitionFormation(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

class StepRepr_ConfigurationDesign(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ConfigurationDesign"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ConfigurationDesign) -> None: ...

    def Init(self, aConfiguration: StepRepr_ConfigurationItem | None, aDesign: StepRepr_ConfigurationDesignItem) -> None:
        """Initialize all fields (own and inherited)"""

    def Configuration(self) -> StepRepr_ConfigurationItem:
        """Returns field Configuration"""

    def SetConfiguration(self, Configuration: StepRepr_ConfigurationItem | None) -> None:
        """Set field Configuration"""

    def Design(self) -> StepRepr_ConfigurationDesignItem:
        """Returns field Design"""

    def SetDesign(self, Design: StepRepr_ConfigurationDesignItem) -> None:
        """Set field Design"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ConfigurationEffectivity(nanoocp.StepBasic.StepBasic_ProductDefinitionEffectivity):
    """Representation of STEP entity ConfigurationEffectivity"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ConfigurationEffectivity) -> None: ...

    def Init(self, aEffectivity_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionEffectivity_Usage: nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship | None, aConfiguration: StepRepr_ConfigurationDesign | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Configuration(self) -> StepRepr_ConfigurationDesign:
        """Returns field Configuration"""

    def SetConfiguration(self, Configuration: StepRepr_ConfigurationDesign | None) -> None:
        """Set field Configuration"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ConfigurationItem(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ConfigurationItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ConfigurationItem) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aItemConcept: StepRepr_ProductConcept | None, hasPurpose: bool, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def ItemConcept(self) -> StepRepr_ProductConcept:
        """Returns field ItemConcept"""

    def SetItemConcept(self, ItemConcept: StepRepr_ProductConcept | None) -> None:
        """Set field ItemConcept"""

    def Purpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Purpose"""

    def HasPurpose(self) -> bool:
        """Returns True if optional field Purpose is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ConstructiveGeometryRepresentation(StepRepr_Representation):
    @overload
    def __init__(self) -> None:
        """Returns a ConstructiveGeometryRepresentation"""

    @overload
    def __init__(self, theOther: StepRepr_ConstructiveGeometryRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationRelationship(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a RepresentationRelationship"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRep1: StepRepr_Representation | None, aRep2: StepRepr_Representation | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasDescription(self) -> bool: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetRep1(self, aRep1: StepRepr_Representation | None) -> None: ...

    def Rep1(self) -> StepRepr_Representation: ...

    def SetRep2(self, aRep2: StepRepr_Representation | None) -> None: ...

    def Rep2(self) -> StepRepr_Representation: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ConstructiveGeometryRepresentationRelationship(StepRepr_RepresentationRelationship):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ConstructiveGeometryRepresentationRelationship) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentedDefinition(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type RepresentedDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentedDefinition) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of RepresentedDefinition select type
        1 -> GeneralProperty from StepBasic
        2 -> PropertyDefinition from StepRepr
        3 -> PropertyDefinitionRelationship from StepRepr
        4 -> ShapeAspect from StepRepr
        5 -> ShapeAspectRelationship from StepRepr
        0 else
        """

    def GeneralProperty(self) -> nanoocp.StepBasic.StepBasic_GeneralProperty:
        """Returns Value as GeneralProperty (or Null if another type)"""

    def PropertyDefinition(self) -> StepRepr_PropertyDefinition:
        """Returns Value as PropertyDefinition (or Null if another type)"""

    def PropertyDefinitionRelationship(self) -> StepRepr_PropertyDefinitionRelationship:
        """
        Returns Value as PropertyDefinitionRelationship (or Null if another type)
        """

    def ShapeAspect(self) -> StepRepr_ShapeAspect:
        """Returns Value as ShapeAspect (or Null if another type)"""

    def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship:
        """Returns Value as ShapeAspectRelationship (or Null if another type)"""

class StepRepr_PropertyDefinitionRepresentation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity PropertyDefinitionRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_PropertyDefinitionRepresentation) -> None: ...

    def Init(self, aDefinition: StepRepr_RepresentedDefinition, aUsedRepresentation: StepRepr_Representation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Definition(self) -> StepRepr_RepresentedDefinition:
        """Returns field Definition"""

    def SetDefinition(self, Definition: StepRepr_RepresentedDefinition) -> None:
        """Set field Definition"""

    def UsedRepresentation(self) -> StepRepr_Representation:
        """Returns field UsedRepresentation"""

    def SetUsedRepresentation(self, UsedRepresentation: StepRepr_Representation | None) -> None:
        """Set field UsedRepresentation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_DataEnvironment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DataEnvironment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_DataEnvironment) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aElements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def Elements(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation]:
        """Returns field Elements"""

    def SetElements(self, Elements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation] | None) -> None:
        """Set field Elements"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_DefinitionalRepresentation(StepRepr_Representation):
    @overload
    def __init__(self) -> None:
        """Returns a DefinitionalRepresentation"""

    @overload
    def __init__(self, theOther: StepRepr_DefinitionalRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_DescriptiveRepresentationItem(StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a DescriptiveRepresentationItem"""

    @overload
    def __init__(self, theOther: StepRepr_DescriptiveRepresentationItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_Extension(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_Extension) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ExternallyDefinedRepresentation(StepRepr_Representation):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ExternallyDefinedRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ShapeAspectRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ShapeAspectRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ShapeAspectRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingShapeAspect: StepRepr_ShapeAspect | None, aRelatedShapeAspect: StepRepr_ShapeAspect | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def RelatingShapeAspect(self) -> StepRepr_ShapeAspect:
        """Returns field RelatingShapeAspect"""

    def SetRelatingShapeAspect(self, RelatingShapeAspect: StepRepr_ShapeAspect | None) -> None:
        """Set field RelatingShapeAspect"""

    def RelatedShapeAspect(self) -> StepRepr_ShapeAspect:
        """Returns field RelatedShapeAspect"""

    def SetRelatedShapeAspect(self, RelatedShapeAspect: StepRepr_ShapeAspect | None) -> None:
        """Set field RelatedShapeAspect"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_FeatureForDatumTargetRelationship(StepRepr_ShapeAspectRelationship):
    """Representation of STEP entity DimensionalLocation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_FeatureForDatumTargetRelationship) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_FunctionallyDefinedTransformation(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a FunctionallyDefinedTransformation"""

    @overload
    def __init__(self, theOther: StepRepr_FunctionallyDefinedTransformation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_GeometricAlignment(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_GeometricAlignment) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationContext(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a RepresentationContext"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationContext) -> None: ...

    def Init(self, aContextIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None, aContextType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetContextIdentifier(self, aContextIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ContextIdentifier(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetContextType(self, aContextType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ContextType(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_GlobalUncertaintyAssignedContext(StepRepr_RepresentationContext):
    @overload
    def __init__(self) -> None:
        """Returns a GlobalUncertaintyAssignedContext"""

    @overload
    def __init__(self, theOther: StepRepr_GlobalUncertaintyAssignedContext) -> None: ...

    def Init(self, aContextIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None, aContextType: nanoocp.TCollection.TCollection_HAsciiString | None, aUncertainty: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_UncertaintyMeasureWithUnit] | None) -> None: ...

    def SetUncertainty(self, aUncertainty: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_UncertaintyMeasureWithUnit] | None) -> None: ...

    def Uncertainty(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_UncertaintyMeasureWithUnit]: ...

    def UncertaintyValue(self, num: int) -> nanoocp.StepBasic.StepBasic_UncertaintyMeasureWithUnit: ...

    def NbUncertainty(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_GlobalUnitAssignedContext(StepRepr_RepresentationContext):
    @overload
    def __init__(self) -> None:
        """Returns a GlobalUnitAssignedContext"""

    @overload
    def __init__(self, theOther: StepRepr_GlobalUnitAssignedContext) -> None: ...

    def Init(self, aContextIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None, aContextType: nanoocp.TCollection.TCollection_HAsciiString | None, aUnits: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_NamedUnit] | None) -> None: ...

    def SetUnits(self, aUnits: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_NamedUnit] | None) -> None: ...

    def Units(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_NamedUnit]: ...

    def UnitsValue(self, num: int) -> nanoocp.StepBasic.StepBasic_NamedUnit: ...

    def NbUnits(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_IntegerRepresentationItem(StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a IntegerRepresentationItem"""

    @overload
    def __init__(self, theOther: StepRepr_IntegerRepresentationItem) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theValue: int) -> None: ...

    def SetValue(self, theValue: int) -> None: ...

    def Value(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ItemDefinedTransformation(nanoocp.Standard.Standard_Transient):
    """Added from StepRepr Rev2 to Rev4"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ItemDefinedTransformation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aTransformItem1: StepRepr_RepresentationItem | None, aTransformItem2: StepRepr_RepresentationItem | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasDescription(self) -> bool: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetTransformItem1(self, aItem: StepRepr_RepresentationItem | None) -> None: ...

    def TransformItem1(self) -> StepRepr_RepresentationItem: ...

    def SetTransformItem2(self, aItem: StepRepr_RepresentationItem | None) -> None: ...

    def TransformItem2(self) -> StepRepr_RepresentationItem: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MakeFromUsageOption(StepRepr_ProductDefinitionUsage):
    """Representation of STEP entity MakeFromUsageOption"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_MakeFromUsageOption) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, aRanking: int, aRankingRationale: nanoocp.TCollection.TCollection_HAsciiString | None, aQuantity: nanoocp.Standard.Standard_Transient | None) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, aRanking: int, aRankingRationale: nanoocp.TCollection.TCollection_HAsciiString | None, aQuantity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Ranking(self) -> int:
        """Returns field Ranking"""

    def SetRanking(self, Ranking: int) -> None:
        """Set field Ranking"""

    def RankingRationale(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field RankingRationale"""

    def SetRankingRationale(self, RankingRationale: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field RankingRationale"""

    def Quantity(self) -> nanoocp.Standard.Standard_Transient:
        """Returns field Quantity"""

    def SetQuantity(self, Quantity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Set field Quantity"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MappedItem(StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a MappedItem"""

    @overload
    def __init__(self, theOther: StepRepr_MappedItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aMappingSource: StepRepr_RepresentationMap | None, aMappingTarget: StepRepr_RepresentationItem | None) -> None: ...

    def SetMappingSource(self, aMappingSource: StepRepr_RepresentationMap | None) -> None: ...

    def MappingSource(self) -> StepRepr_RepresentationMap: ...

    def SetMappingTarget(self, aMappingTarget: StepRepr_RepresentationItem | None) -> None: ...

    def MappingTarget(self) -> StepRepr_RepresentationItem: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MaterialDesignation(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_MaterialDesignation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOfDefinition: StepRepr_CharacterizedDefinition) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetOfDefinition(self, aOfDefinition: StepRepr_CharacterizedDefinition) -> None: ...

    def OfDefinition(self) -> StepRepr_CharacterizedDefinition: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_PropertyDefinition(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity PropertyDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_PropertyDefinition) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aDefinition: StepRepr_CharacterizedDefinition) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def Definition(self) -> StepRepr_CharacterizedDefinition:
        """Returns field Definition"""

    def SetDefinition(self, Definition: StepRepr_CharacterizedDefinition) -> None:
        """Set field Definition"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MaterialProperty(StepRepr_PropertyDefinition):
    """Representation of STEP entity MaterialProperty"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_MaterialProperty) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MaterialPropertyRepresentation(StepRepr_PropertyDefinitionRepresentation):
    """Representation of STEP entity MaterialPropertyRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_MaterialPropertyRepresentation) -> None: ...

    def Init(self, aPropertyDefinitionRepresentation_Definition: StepRepr_RepresentedDefinition, aPropertyDefinitionRepresentation_UsedRepresentation: StepRepr_Representation | None, aDependentEnvironment: StepRepr_DataEnvironment | None) -> None:
        """Initialize all fields (own and inherited)"""

    def DependentEnvironment(self) -> StepRepr_DataEnvironment:
        """Returns field DependentEnvironment"""

    def SetDependentEnvironment(self, DependentEnvironment: StepRepr_DataEnvironment | None) -> None:
        """Set field DependentEnvironment"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MeasureRepresentationItem(StepRepr_RepresentationItem):
    """
    Implements a measure_representation_item entity
    which is used for storing validation properties
    (e.g. area) for shapes
    """

    @overload
    def __init__(self) -> None:
        """Creates empty object"""

    @overload
    def __init__(self, theOther: StepRepr_MeasureRepresentationItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aValueComponent: nanoocp.StepBasic.StepBasic_MeasureValueMember | None, aUnitComponent: nanoocp.StepBasic.StepBasic_Unit) -> None:
        """Init all fields"""

    def SetMeasure(self, Measure: nanoocp.StepBasic.StepBasic_MeasureWithUnit | None) -> None: ...

    def Measure(self) -> nanoocp.StepBasic.StepBasic_MeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_MechanicalDesignAndDraughtingRelationship(StepRepr_RepresentationRelationship):
    @overload
    def __init__(self) -> None:
        """Returns a MechanicalDesignAndDraughtingRelationship"""

    @overload
    def __init__(self, theOther: StepRepr_MechanicalDesignAndDraughtingRelationship) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_NextAssemblyUsageOccurrence(StepRepr_AssemblyComponentUsage):
    """Representation of STEP entity NextAssemblyUsageOccurrence"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_NextAssemblyUsageOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ParallelOffset(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ParallelOffset) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theOfShape: StepRepr_ProductDefinitionShape | None, theProductDefinitional: nanoocp.StepData.StepData_Logical, theOffset: nanoocp.Standard.Standard_Transient | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Offset(self) -> nanoocp.Standard.Standard_Transient:
        """Returns field Offset"""

    def SetOffset(self, theOffset: nanoocp.Standard.Standard_Transient | None) -> None:
        """Set field Offset"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ParametricRepresentationContext(StepRepr_RepresentationContext):
    @overload
    def __init__(self) -> None:
        """Returns a ParametricRepresentationContext"""

    @overload
    def __init__(self, theOther: StepRepr_ParametricRepresentationContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_PerpendicularTo(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_PerpendicularTo) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ProductConcept(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ProductConcept"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ProductConcept) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMarketContext: nanoocp.StepBasic.StepBasic_ProductConceptContext | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def MarketContext(self) -> nanoocp.StepBasic.StepBasic_ProductConceptContext:
        """Returns field MarketContext"""

    def SetMarketContext(self, MarketContext: nanoocp.StepBasic.StepBasic_ProductConceptContext | None) -> None:
        """Set field MarketContext"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ProductDefinitionShape(StepRepr_PropertyDefinition):
    """Representation of STEP entity ProductDefinitionShape"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ProductDefinitionShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_PromissoryUsageOccurrence(StepRepr_AssemblyComponentUsage):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_PromissoryUsageOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_PropertyDefinitionRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity PropertyDefinitionRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_PropertyDefinitionRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingPropertyDefinition: StepRepr_PropertyDefinition | None, aRelatedPropertyDefinition: StepRepr_PropertyDefinition | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def RelatingPropertyDefinition(self) -> StepRepr_PropertyDefinition:
        """Returns field RelatingPropertyDefinition"""

    def SetRelatingPropertyDefinition(self, RelatingPropertyDefinition: StepRepr_PropertyDefinition | None) -> None:
        """Set field RelatingPropertyDefinition"""

    def RelatedPropertyDefinition(self) -> StepRepr_PropertyDefinition:
        """Returns field RelatedPropertyDefinition"""

    def SetRelatedPropertyDefinition(self, RelatedPropertyDefinition: StepRepr_PropertyDefinition | None) -> None:
        """Set field RelatedPropertyDefinition"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_QuantifiedAssemblyComponentUsage(StepRepr_AssemblyComponentUsage):
    """Representation of STEP entity QuantifiedAssemblyComponentUsage"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_QuantifiedAssemblyComponentUsage) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None, aQuantity: nanoocp.Standard.Standard_Transient | None) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None, aQuantity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Quantity(self) -> nanoocp.Standard.Standard_Transient:
        """Returns field Quantity"""

    def SetQuantity(self, Quantity: nanoocp.Standard.Standard_Transient | None) -> None:
        """Set field Quantity"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RealRepresentationItem(StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a RealRepresentationItem"""

    @overload
    def __init__(self, theOther: StepRepr_RealRepresentationItem) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theValue: float) -> None: ...

    def SetValue(self, theValue: float) -> None: ...

    def Value(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationContextReference(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity RepresentationContextReference"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationContextReference) -> None: ...

    def Init(self, theContextIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ContextIdentifier(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field ContextIdentifier"""

    def SetContextIdentifier(self, theContextIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets field ContextIdentifier"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationMap(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a RepresentationMap"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationMap) -> None: ...

    def Init(self, aMappingOrigin: StepRepr_RepresentationItem | None, aMappedRepresentation: StepRepr_Representation | None) -> None: ...

    def SetMappingOrigin(self, aMappingOrigin: StepRepr_RepresentationItem | None) -> None: ...

    def MappingOrigin(self) -> StepRepr_RepresentationItem: ...

    def SetMappedRepresentation(self, aMappedRepresentation: StepRepr_Representation | None) -> None: ...

    def MappedRepresentation(self) -> StepRepr_Representation: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationOrRepresentationReference(nanoocp.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type RepresentationOrRepresentationReference
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationOrRepresentationReference) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of RepresentationOrRepresentationReference select type
        -- 1 -> Representation
        -- 2 -> RepresentationReference
        """

    def Representation(self) -> StepRepr_Representation:
        """Returns Value as Representation (or Null if another type)"""

    def RepresentationReference(self) -> StepRepr_RepresentationReference:
        """Returns Value as RepresentationReference (or Null if another type)"""

class StepRepr_RepresentationReference(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity RepresentationReference"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepRepr_RepresentationReference) -> None: ...

    def Init(self, theId: nanoocp.TCollection.TCollection_HAsciiString | None, theContextOfItems: StepRepr_RepresentationContextReference | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, theId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets field Id"""

    def ContextOfItems(self) -> StepRepr_RepresentationContextReference:
        """Returns field ContextOfItems"""

    def SetContextOfItems(self, theContextOfItems: StepRepr_RepresentationContextReference | None) -> None:
        """Sets field ContextOfItems"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_Transformation(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a Transformation SelectType"""

    @overload
    def __init__(self, theOther: StepRepr_Transformation) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a Transformation Kind Entity that is :
        1 -> ItemDefinedTransformation
        2 -> FunctionallyDefinedTransformation
        0 else
        """

    def ItemDefinedTransformation(self) -> StepRepr_ItemDefinedTransformation:
        """returns Value as a ItemDefinedTransformation (Null if another type)"""

    def FunctionallyDefinedTransformation(self) -> StepRepr_FunctionallyDefinedTransformation:
        """
        returns Value as a FunctionallyDefinedTransformation (Null if another type)
        """

class StepRepr_ShapeRepresentationRelationship(StepRepr_RepresentationRelationship):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ShapeRepresentationRelationship) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_RepresentationRelationshipWithTransformation(StepRepr_ShapeRepresentationRelationship):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_RepresentationRelationshipWithTransformation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRep1: StepRepr_Representation | None, aRep2: StepRepr_Representation | None, aTransf: StepRepr_Transformation) -> None: ...

    def TransformationOperator(self) -> StepRepr_Transformation: ...

    def SetTransformationOperator(self, aTrans: StepRepr_Transformation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ReprItemAndMeasureWithUnit(StepRepr_RepresentationItem):
    """
    Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT,
    REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ReprItemAndMeasureWithUnit) -> None: ...

    def Init(self, aMWU: nanoocp.StepBasic.StepBasic_MeasureWithUnit | None, aRI: StepRepr_RepresentationItem | None) -> None: ...

    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: ...

    def SetMeasureWithUnit(self, aMWU: nanoocp.StepBasic.StepBasic_MeasureWithUnit | None) -> None: ...

    def GetMeasureWithUnit(self) -> nanoocp.StepBasic.StepBasic_MeasureWithUnit: ...

    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ReprItemAndLengthMeasureWithUnit(StepRepr_ReprItemAndMeasureWithUnit):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ReprItemAndLengthMeasureWithUnit) -> None: ...

    def SetLengthMeasureWithUnit(self, aLMWU: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None: ...

    def GetLengthMeasureWithUnit(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ReprItemAndMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnit):
    """
    Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT,
    QUALIFIED_REPRESENTATION_ITEM REPRESENTATION_ITEM,
    LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ReprItemAndMeasureWithUnitAndQRI) -> None: ...

    def Init(self, aMWU: nanoocp.StepBasic.StepBasic_MeasureWithUnit | None, aRI: StepRepr_RepresentationItem | None, aQRI: nanoocp.StepShape.StepShape_QualifiedRepresentationItem | None) -> None: ...

    def SetQualifiedRepresentationItem(self, aQRI: nanoocp.StepShape.StepShape_QualifiedRepresentationItem | None) -> None: ...

    def GetQualifiedRepresentationItem(self) -> nanoocp.StepShape.StepShape_QualifiedRepresentationItem: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnitAndQRI):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI) -> None: ...

    def SetLengthMeasureWithUnit(self, aLMWU: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None: ...

    def GetLengthMeasureWithUnit(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ReprItemAndPlaneAngleMeasureWithUnit(StepRepr_ReprItemAndMeasureWithUnit):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ReprItemAndPlaneAngleMeasureWithUnit) -> None: ...

    def SetPlaneAngleMeasureWithUnit(self, aLMWU: nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit | None) -> None: ...

    def GetPlaneAngleMeasureWithUnit(self) -> nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnitAndQRI):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI) -> None: ...

    def SetPlaneAngleMeasureWithUnit(self, aLMWU: nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit | None) -> None: ...

    def GetPlaneAngleMeasureWithUnit(self) -> nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ShapeAspectDerivingRelationship(StepRepr_ShapeAspectRelationship):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ShapeAspectDerivingRelationship) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ShapeAspectTransition(StepRepr_ShapeAspectRelationship):
    """Representation of STEP entity ShapeAspectTransition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_ShapeAspectTransition) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ShapeDefinition(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ShapeDefinition SelectType"""

    @overload
    def __init__(self, theOther: StepRepr_ShapeDefinition) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ShapeDefinition Kind Entity that is :
        1 -> ProductDefinitionShape
        2 -> ShapeAspect
        3 -> ShapeAspectRelationship
        0 else
        """

    def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape:
        """returns Value as a ProductDefinitionShape (Null if another type)"""

    def ShapeAspect(self) -> StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

    def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship:
        """returns Value as a ShapeAspectRelationship (Null if another type)"""

class StepRepr_ShapeRepresentationRelationshipWithTransformation(StepRepr_RepresentationRelationshipWithTransformation):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ShapeRepresentationRelationshipWithTransformation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_SpecifiedHigherUsageOccurrence(StepRepr_AssemblyComponentUsage):
    """Representation of STEP entity SpecifiedHigherUsageOccurrence"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_SpecifiedHigherUsageOccurrence) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinition | None, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None, aUpperUsage: StepRepr_AssemblyComponentUsage | None, aNextUsage: StepRepr_NextAssemblyUsageOccurrence | None) -> None: ...

    @overload
    def Init(self, aProductDefinitionRelationship_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasProductDefinitionRelationship_Description: bool, aProductDefinitionRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aProductDefinitionRelationship_RelatingProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, aProductDefinitionRelationship_RelatedProductDefinition: nanoocp.StepBasic.StepBasic_ProductDefinitionOrReference, hasAssemblyComponentUsage_ReferenceDesignator: bool, aAssemblyComponentUsage_ReferenceDesignator: nanoocp.TCollection.TCollection_HAsciiString | None, aUpperUsage: StepRepr_AssemblyComponentUsage | None, aNextUsage: StepRepr_NextAssemblyUsageOccurrence | None) -> None:
        """Initialize all fields (own and inherited)"""

    def UpperUsage(self) -> StepRepr_AssemblyComponentUsage:
        """Returns field UpperUsage"""

    def SetUpperUsage(self, UpperUsage: StepRepr_AssemblyComponentUsage | None) -> None:
        """Set field UpperUsage"""

    def NextUsage(self) -> StepRepr_NextAssemblyUsageOccurrence:
        """Returns field NextUsage"""

    def SetNextUsage(self, NextUsage: StepRepr_NextAssemblyUsageOccurrence | None) -> None:
        """Set field NextUsage"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_StructuralResponseProperty(StepRepr_PropertyDefinition):
    """Representation of STEP entity StructuralResponseProperty"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_StructuralResponseProperty) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_StructuralResponsePropertyDefinitionRepresentation(StepRepr_PropertyDefinitionRepresentation):
    """
    Representation of STEP entity StructuralResponsePropertyDefinitionRepresentation
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepRepr_StructuralResponsePropertyDefinitionRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_SuppliedPartRelationship(nanoocp.StepBasic.StepBasic_ProductDefinitionRelationship):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_SuppliedPartRelationship) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_Tangent(StepRepr_DerivedShapeAspect):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_Tangent) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ValueRange(StepRepr_CompoundRepresentationItem):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepRepr_ValueRange) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepRepr_ValueRepresentationItem(StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a ValueRepresentationItem"""

    @overload
    def __init__(self, theOther: StepRepr_ValueRepresentationItem) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theValueComponentMember: nanoocp.StepBasic.StepBasic_MeasureValueMember | None) -> None: ...

    def SetValueComponentMember(self, theValueComponentMember: nanoocp.StepBasic.StepBasic_MeasureValueMember | None) -> None: ...

    def ValueComponentMember(self) -> nanoocp.StepBasic.StepBasic_MeasureValueMember: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepRepr
StepRepr_Array1OfMaterialPropertyRepresentation = nanoocp.NCollection.NCollection_Array1[nanoocp.StepRepr.StepRepr_MaterialPropertyRepresentation]
StepRepr_Array1OfPropertyDefinitionRepresentation = nanoocp.NCollection.NCollection_Array1[nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation]
StepRepr_Array1OfRepresentationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepRepr.StepRepr_RepresentationItem]
StepRepr_Array1OfShapeAspect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepRepr.StepRepr_ShapeAspect]
StepRepr_HArray1OfMaterialPropertyRepresentation = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_MaterialPropertyRepresentation]
StepRepr_HArray1OfPropertyDefinitionRepresentation = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation]
StepRepr_HArray1OfRepresentationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem]
StepRepr_HArray1OfShapeAspect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_ShapeAspect]
