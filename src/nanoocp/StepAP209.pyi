"""OCCT package StepAP209 (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.STEPConstruct
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepFEA
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.XSControl
import nanoocp.StepElement


class StepAP209_Construct(nanoocp.STEPConstruct.STEPConstruct_Tool):
    """Basic tool for working with AP209 model"""

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> None:
        """Creates a tool and initializes it"""

    @overload
    def __init__(self, theOther: StepAP209_Construct) -> None: ...

    def Init(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> bool:
        """Initializes tool; returns True if succeeded"""

    def IsDesing(self, PD: nanoocp.StepBasic.StepBasic_ProductDefinitionFormation | None) -> bool: ...

    def IsAnalys(self, PD: nanoocp.StepBasic.StepBasic_ProductDefinitionFormation | None) -> bool: ...

    @overload
    def FeaModel(self, Prod: nanoocp.StepBasic.StepBasic_Product | None) -> nanoocp.StepFEA.StepFEA_FeaModel: ...

    @overload
    def FeaModel(self, PDF: nanoocp.StepBasic.StepBasic_ProductDefinitionFormation | None) -> nanoocp.StepFEA.StepFEA_FeaModel: ...

    @overload
    def FeaModel(self, PDS: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None) -> nanoocp.StepFEA.StepFEA_FeaModel: ...

    @overload
    def FeaModel(self, PD: nanoocp.StepBasic.StepBasic_ProductDefinition | None) -> nanoocp.StepFEA.StepFEA_FeaModel: ...

    def GetFeaAxis2Placement3d(self, theFeaModel: nanoocp.StepFEA.StepFEA_FeaModel | None) -> nanoocp.StepFEA.StepFEA_FeaAxis2Placement3d: ...

    @overload
    def IdealShape(self, Prod: nanoocp.StepBasic.StepBasic_Product | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    @overload
    def IdealShape(self, PDF: nanoocp.StepBasic.StepBasic_ProductDefinitionFormation | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    @overload
    def IdealShape(self, PD: nanoocp.StepBasic.StepBasic_ProductDefinition | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    @overload
    def IdealShape(self, PDS: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    @overload
    def NominShape(self, Prod: nanoocp.StepBasic.StepBasic_Product | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    @overload
    def NominShape(self, PDF: nanoocp.StepBasic.StepBasic_ProductDefinitionFormation | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    def GetElementMaterial(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_ElementMaterial]: ...

    def GetElemGeomRelat(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.StepFEA.StepFEA_ElementGeometricRelationship]: ...

    def GetElements1D(self, theFeaModel: nanoocp.StepFEA.StepFEA_FeaModel | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.StepFEA.StepFEA_ElementRepresentation]: ...

    def GetElements2D(self, theFEAModel: nanoocp.StepFEA.StepFEA_FeaModel | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.StepFEA.StepFEA_ElementRepresentation]: ...

    def GetElements3D(self, theFEAModel: nanoocp.StepFEA.StepFEA_FeaModel | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.StepFEA.StepFEA_ElementRepresentation]: ...

    def GetCurElemSection(self, ElemRepr: nanoocp.StepFEA.StepFEA_Curve3dElementRepresentation | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementSectionDefinition]:
        """
        Getting list of curve_element_section_definitions
        for given element_representation
        """

    def GetShReprForElem(self, ElemRepr: nanoocp.StepFEA.StepFEA_ElementRepresentation | None) -> nanoocp.StepShape.StepShape_ShapeRepresentation: ...

    def CreateAnalysStructure(self, Prod: nanoocp.StepBasic.StepBasic_Product | None) -> bool:
        """Create empty structure for idealized_analysis_shape"""

    def CreateFeaStructure(self, Prod: nanoocp.StepBasic.StepBasic_Product | None) -> bool:
        """Create fea structure"""

    def ReplaceCcDesingToApplied(self) -> bool:
        """
        Put into model entities Applied... for AP209 instead of
        entities CcDesing... from AP203.
        """

    def CreateAddingEntities(self, AnaPD: nanoocp.StepBasic.StepBasic_ProductDefinition | None) -> bool:
        """
        Create approval.. , date.. , time.. , person.. and
        organization.. entities for analysis structure
        """

    def CreateAP203Structure(self) -> nanoocp.StepData.StepData_StepModel:
        """Create AP203 structure from existing AP209 structure"""

    def CreateAdding203Entities(self, PD: nanoocp.StepBasic.StepBasic_ProductDefinition | None) -> tuple[bool, nanoocp.StepData.StepData_StepModel]:
        """
        Create approval.. , date.. , time.. , person.. and
        organization.. entities for 203 structure
        """
