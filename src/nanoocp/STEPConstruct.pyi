"""OCCT package STEPConstruct (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.StepAP203
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.StepVisual
import nanoocp.TCollection
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.XCAFDoc
import nanoocp.XSControl
import nanoocp.gp


class STEPConstruct:
    """
    Defines tools for creation and investigation STEP constructs
    used for representing various kinds of data, such as product and
    assembly structure, unit contexts, associated information
    The creation of these structures is made according to currently
    active schema (AP203 or AP214 CD2 or DIS)
    This is taken from parameter write.step.schema
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPConstruct) -> None: ...

    @overload
    @staticmethod
    def FindEntity(FinderProcess: nanoocp.Transfer.Transfer_FinderProcess | None, Shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """
        Returns STEP entity of the (sub)type of RepresentationItem
        which is a result of the translation of the Shape, or Null if
        no result is recorded
        """

    @overload
    @staticmethod
    def FindEntity(FinderProcess: nanoocp.Transfer.Transfer_FinderProcess | None, Shape: nanoocp.TopoDS.TopoDS_Shape, Loc: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """
        The same as above, but in the case if item not found, repeats
        search on the same shape without location. The Loc corresponds to the
        location with which result is found (either location of the Shape,
        or Null)
        """

    @staticmethod
    def FindShape(TransientProcess: nanoocp.Transfer.Transfer_TransientProcess | None, item: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns Shape resulting from given STEP entity (Null if not mapped)"""

    @staticmethod
    def FindCDSR(ComponentBinder: nanoocp.Transfer.Transfer_Binder | None, AssemblySDR: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None) -> tuple[bool, nanoocp.StepShape.StepShape_ContextDependentShapeRepresentation]:
        """Find CDSR corresponding to the component in the specified assembly"""

class STEPConstruct_AP203Context:
    """
    Maintains context specific for AP203 (required data and
    management information such as persons, dates, approvals etc.)
    It contains static entities (which can be shared), default
    values for person and organisation, and also provides
    tool for creating management entities around specific part (SDR).
    """

    @overload
    def __init__(self) -> None:
        """Creates tool and fills constant fields"""

    @overload
    def __init__(self, theOther: STEPConstruct_AP203Context) -> None: ...

    def DefaultApproval(self) -> nanoocp.StepBasic.StepBasic_Approval:
        """
        Returns default approval entity which
        is used when no other data are available
        """

    def SetDefaultApproval(self, app: nanoocp.StepBasic.StepBasic_Approval | None) -> None:
        """Sets default approval"""

    def DefaultDateAndTime(self) -> nanoocp.StepBasic.StepBasic_DateAndTime:
        """
        Returns default date_and_time entity which
        is used when no other data are available
        """

    def SetDefaultDateAndTime(self, dt: nanoocp.StepBasic.StepBasic_DateAndTime | None) -> None:
        """Sets default date_and_time entity"""

    def DefaultPersonAndOrganization(self) -> nanoocp.StepBasic.StepBasic_PersonAndOrganization:
        """
        Returns default person_and_organization entity which
        is used when no other data are available
        """

    def SetDefaultPersonAndOrganization(self, po: nanoocp.StepBasic.StepBasic_PersonAndOrganization | None) -> None:
        """Sets default person_and_organization entity"""

    def DefaultSecurityClassificationLevel(self) -> nanoocp.StepBasic.StepBasic_SecurityClassificationLevel:
        """
        Returns default security_classification_level entity which
        is used when no other data are available
        """

    def SetDefaultSecurityClassificationLevel(self, sc: nanoocp.StepBasic.StepBasic_SecurityClassificationLevel | None) -> None:
        """Sets default security_classification_level"""

    def RoleCreator(self) -> nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole: ...

    def RoleDesignOwner(self) -> nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole: ...

    def RoleDesignSupplier(self) -> nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole: ...

    def RoleClassificationOfficer(self) -> nanoocp.StepBasic.StepBasic_PersonAndOrganizationRole: ...

    def RoleCreationDate(self) -> nanoocp.StepBasic.StepBasic_DateTimeRole: ...

    def RoleClassificationDate(self) -> nanoocp.StepBasic.StepBasic_DateTimeRole: ...

    def RoleApprover(self) -> nanoocp.StepBasic.StepBasic_ApprovalRole:
        """
        Return predefined PersonAndOrganizationRole and DateTimeRole
        entities named 'creator', 'design owner', 'design supplier',
        'classification officer', 'creation date', 'classification date',
        'approver'
        """

    @overload
    def Init(self, sdr: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None) -> None:
        """
        Takes SDR (part) which brings all standard data around part
        (common for AP203 and AP214) and creates all the additional
        entities required for AP203
        """

    @overload
    def Init(self, SDRTool: STEPConstruct_Part) -> None:
        """
        Takes tool which describes standard data around part
        (common for AP203 and AP214) and creates all the additional
        entities required for AP203

        The created entities can be obtained by calls to methods
        GetCreator(), GetDesignOwner(), GetDesignSupplier(),
        GetClassificationOfficer(), GetSecurity(), GetCreationDate(),
        GetClassificationDate(), GetApproval(),
        GetApprover(), GetApprovalDateTime(),
        GetProductCategoryRelationship()
        """

    @overload
    def Init(self, nauo: nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence | None) -> None:
        """
        Takes NAUO which describes assembly link to component
        and creates the security_classification entity associated to
        it as required by the AP203

        Instantiated (or existing previously) entities concerned
        can be obtained by calls to methods
        GetClassificationOfficer(), GetSecurity(),
        GetClassificationDate(), GetApproval(),
        GetApprover(), GetApprovalDateTime()
        Takes tool which describes standard data around part
        (common for AP203 and AP214) and takes from model (or creates
        if missing) all the additional entities required by AP203
        """

    def GetCreator(self) -> nanoocp.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: ...

    def GetDesignOwner(self) -> nanoocp.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: ...

    def GetDesignSupplier(self) -> nanoocp.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: ...

    def GetClassificationOfficer(self) -> nanoocp.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: ...

    def GetSecurity(self) -> nanoocp.StepAP203.StepAP203_CcDesignSecurityClassification: ...

    def GetCreationDate(self) -> nanoocp.StepAP203.StepAP203_CcDesignDateAndTimeAssignment: ...

    def GetClassificationDate(self) -> nanoocp.StepAP203.StepAP203_CcDesignDateAndTimeAssignment: ...

    def GetApproval(self) -> nanoocp.StepAP203.StepAP203_CcDesignApproval: ...

    def GetApprover(self) -> nanoocp.StepBasic.StepBasic_ApprovalPersonOrganization: ...

    def GetApprovalDateTime(self) -> nanoocp.StepBasic.StepBasic_ApprovalDateTime: ...

    def GetProductCategoryRelationship(self) -> nanoocp.StepBasic.StepBasic_ProductCategoryRelationship:
        """Return entities (roots) instantiated for the part by method Init"""

    def Clear(self) -> None:
        """Clears all fields describing entities specific to each part"""

    def InitRoles(self) -> None:
        """Initializes constant fields (shared entities)"""

    def InitAssembly(self, nauo: nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence | None) -> None:
        """Initializes all missing data which are required for assembly"""

    def InitSecurityRequisites(self) -> None:
        """
        Initializes ClassificationOfficer and ClassificationDate
        entities according to Security entity
        """

    def InitApprovalRequisites(self) -> None:
        """
        Initializes Approver and ApprovalDateTime
        entities according to Approval entity
        """

class STEPConstruct_Assembly:
    """
    This operator creates and checks an item of an assembly, from its
    basic data : a ShapeRepresentation, a Location ...

    Three ways of coding such item from a ShapeRepresentation :
    - do nothing : i.e. information for assembly are ignored
    - create a MappedItem
    - create a RepresentationRelationship (WithTransformation)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPConstruct_Assembly) -> None: ...

    @overload
    def Init(self, aSR: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, SDR0: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, Ax0: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, Loc: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """
        Initialises with starting values
        Ax0 : origin axis (typically, standard XYZ)
        Loc : location to which place the item
        Makes a MappedItem
        Resulting Value is returned by ItemValue
        """

    @overload
    def Init(self, theSR: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, theSDR0: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, theTrsfOp: nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d | None) -> None:
        """
        Initialises with starting values
        theTrsfOp : local transformation to apply, may have scaling factor
        Makes a MappedItem
        Resulting Value is returned by ItemValue
        """

    def MakeRelationship(self) -> None:
        """
        Make a (ShapeRepresentationRelationship,...WithTransformation)
        Resulting Value is returned by ItemValue
        """

    def ItemValue(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Value
        If no Make... has been called, returns the starting SR
        """

    def ItemLocation(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d:
        """Returns the location of the item, computed from starting aLoc"""

    def GetNAUO(self) -> nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence:
        """Returns NAUO object describing the assembly link"""

    @staticmethod
    def CheckSRRReversesNAUO(theGraph: nanoocp.Interface.Interface_Graph, CDSR: nanoocp.StepShape.StepShape_ContextDependentShapeRepresentation | None) -> bool:
        """
        Checks whether SRR's definition of assembly and component contradicts
        with NAUO definition or not, according to model schema (AP214 or AP203)
        """

class STEPConstruct_ContextTool:
    """
    Maintains global context tool for writing.
    Gives access to Product Definition Context (one per Model)
    Maintains ApplicationProtocolDefinition entity (common for all
    products)
    Also maintains context specific for AP203 and provides set of
    methods to work with various STEP constructs as required
    by Actor
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aStepModel: nanoocp.StepData.StepData_StepModel | None) -> None: ...

    @overload
    def __init__(self, theOther: STEPConstruct_ContextTool) -> None: ...

    def SetModel(self, aStepModel: nanoocp.StepData.StepData_StepModel | None) -> None:
        """
        Initialize ApplicationProtocolDefinition by the first
        entity of that type found in the model
        """

    def SetGlobalFactor(self, theGlobalFactor: nanoocp.StepData.StepData_Factors) -> None: ...

    def GetAPD(self) -> nanoocp.StepBasic.StepBasic_ApplicationProtocolDefinition: ...

    def AddAPD(self, enforce: bool = False) -> None: ...

    def IsAP203(self) -> bool:
        """Returns True if APD.schema_name is config_control_design"""

    def IsAP214(self) -> bool:
        """Returns True if APD.schema_name is automotive_design"""

    def IsAP242(self) -> bool:
        """
        Returns True if APD.schema_name is ap242_managed_model_based_3d_engineering
        """

    def GetACstatus(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetACschemaName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetACyear(self) -> int: ...

    def GetACname(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetACstatus(self, status: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetACschemaName(self, schemaName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetACyear(self, year: int) -> None: ...

    def SetACname(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def GetDefaultAxis(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d:
        """Returns a default axis placement"""

    def AP203Context(self) -> STEPConstruct_AP203Context:
        """Returns tool which maintains context specific for AP203"""

    def Level(self) -> int:
        """Returns current assembly level"""

    def NextLevel(self) -> None: ...

    def PrevLevel(self) -> None: ...

    def SetLevel(self, lev: int) -> None:
        """Changes current assembly level"""

    def Index(self) -> int:
        """Returns current index of assembly component on current level"""

    def NextIndex(self) -> None: ...

    def PrevIndex(self) -> None: ...

    def SetIndex(self, ind: int) -> None:
        """Changes current index of assembly component on current level"""

    def GetProductName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Generates a product name basing on write.step.product.name
        parameter and current position in the assembly structure
        """

    def GetRootsForPart(self, SDRTool: STEPConstruct_Part) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Produces and returns a full list of root entities required
        for part identified by SDRTool (including SDR itself)
        """

    def GetRootsForAssemblyLink(self, assembly: STEPConstruct_Assembly) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Produces and returns a full list of root entities required
        for assembly link identified by assembly (including NAUO and CDSR)
        """

class STEPConstruct_Tool:
    """
    Provides basic functionalities for tools which are intended
    for encoding/decoding specific STEP constructs

    It is initialized by WorkSession and allows easy access to
    its fields and internal data such as Model, TP and FP

    NOTE: Call to method Graph() with True (or for a first time,
    if you have updated the model since last computation of model)
    can take a time, so it is recommended to avoid creation of
    this (and derived) tool multiple times
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> None:
        """Creates a tool and loads it with worksession"""

    @overload
    def __init__(self, theOther: STEPConstruct_Tool) -> None: ...

    def WS(self) -> nanoocp.XSControl.XSControl_WorkSession:
        """Returns currently loaded WorkSession"""

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns current model (Null if not loaded)"""

    def Graph(self, recompute: bool = False) -> nanoocp.Interface.Interface_Graph:
        """Returns current graph (recomputing if necessary)"""

    def TransientProcess(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """Returns TransientProcess (reading; Null if not loaded)"""

    def FinderProcess(self) -> nanoocp.Transfer.Transfer_FinderProcess:
        """Returns FinderProcess (writing; Null if not loaded)"""

class STEPConstruct_ExternRefs(STEPConstruct_Tool):
    """
    Provides a tool for analyzing (reading) and creating (writing)
    references to external files in STEP

    It maintains a data structure in the form of sequences
    of relevant STEP entities (roots), allowing either to create
    them by convenient API, or load from existing model and
    investigate
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> None:
        """Creates a tool and initializes it"""

    @overload
    def __init__(self, theOther: STEPConstruct_ExternRefs) -> None: ...

    def Init(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> bool:
        """Initializes tool; returns True if succeeded"""

    def Clear(self) -> None:
        """Clears internal fields (list of defined extern refs)"""

    def LoadExternRefs(self) -> bool:
        """
        Searches current STEP model for external references
        and loads them to the internal data structures
        NOTE: does not clear data structures before loading
        """

    def NbExternRefs(self) -> int:
        """Returns number of defined extern references"""

    def FileName(self, num: int) -> str:
        """
        Returns filename for numth extern reference
        Returns Null if FileName is not defined or bad
        """

    def ProdDef(self, num: int) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """
        Returns ProductDefinition to which numth extern reference
        is associated.
        Returns Null if cannot be detected or if extern reference
        is not associated to SDR in a proper way.
        """

    def DocFile(self, num: int) -> nanoocp.StepBasic.StepBasic_DocumentFile:
        """
        Returns DocumentFile to which numth extern reference
        is associated.
        Returns Null if cannot be detected.
        """

    def Format(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns format identification string for the extern document
        Returns Null handle if format is not defined
        """

    def AddExternRef(self, filename: str, PD: nanoocp.StepBasic.StepBasic_ProductDefinition | None, format: str) -> int:
        """
        Create a new external reference with specified attributes
        attached to a given SDR
        <format> can be Null string, in that case this information
        is not written. Else, it can be "STEP AP214" or "STEP AP203"
        Returns index of a new extern ref
        """

    def checkAP214Shared(self) -> None:
        """Check (create if it is null) all shared entities for the model"""

    def WriteExternRefs(self, num: int) -> int:
        """
        Adds all the currently defined external refs to the model
        Returns number of written extern refs
        """

    def SetAP214APD(self, APD: nanoocp.StepBasic.StepBasic_ApplicationProtocolDefinition | None) -> None:
        """Set the ApplicationProtocolDefinition of the PDM schema"""

    def GetAP214APD(self) -> nanoocp.StepBasic.StepBasic_ApplicationProtocolDefinition:
        """
        Returns the ApplicationProtocolDefinition of the PDM schema
        NOTE: if not defined then create new APD with new Application Context
        """

class STEPConstruct_Part:
    """
    Provides tools for creating STEP structures associated
    with part (SDR), such as PRODUCT, PDF etc., as
    required by current schema
    Also allows to investigate and modify this data
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPConstruct_Part) -> None: ...

    def MakeSDR(self, aShape: nanoocp.StepShape.StepShape_ShapeRepresentation | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, AC: nanoocp.StepBasic.StepBasic_ApplicationContext | None, theStepModel: nanoocp.StepData.StepData_StepModel | None) -> None: ...

    def ReadSDR(self, aShape: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None) -> None: ...

    def IsDone(self) -> bool: ...

    def SDRValue(self) -> nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation:
        """Returns SDR or Null if not done"""

    def SRValue(self) -> nanoocp.StepShape.StepShape_ShapeRepresentation:
        """Returns SDR->UsedRepresentation() or Null if not done"""

    def PC(self) -> nanoocp.StepBasic.StepBasic_ProductContext: ...

    def PCname(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def PCdisciplineType(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPCname(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPCdisciplineType(self, label: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def AC(self) -> nanoocp.StepBasic.StepBasic_ApplicationContext: ...

    def ACapplication(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetACapplication(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def PDC(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionContext: ...

    def PDCname(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def PDCstage(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPDCname(self, label: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPDCstage(self, label: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Product(self) -> nanoocp.StepBasic.StepBasic_Product: ...

    def Pid(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Pname(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Pdescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPid(self, id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPname(self, label: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPdescription(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def PDF(self) -> nanoocp.StepBasic.StepBasic_ProductDefinitionFormation: ...

    def PDFid(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def PDFdescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPDFid(self, id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPDFdescription(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def PD(self) -> nanoocp.StepBasic.StepBasic_ProductDefinition: ...

    def PDdescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPDdescription(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def PDS(self) -> nanoocp.StepRepr.StepRepr_ProductDefinitionShape: ...

    def PDSname(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def PDSdescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPDSname(self, label: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPDSdescription(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def PRPC(self) -> nanoocp.StepBasic.StepBasic_ProductRelatedProductCategory: ...

    def PRPCname(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def PRPCdescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPRPCname(self, label: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPRPCdescription(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

class STEPConstruct_RenderingProperties:
    """
    Class for working with STEP rendering properties.
    Provides functionality to create and manipulate rendering properties
    used for specifying visual appearance in STEP format.
    This class handles both parsing of STEP entities and creation of new ones.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor creating an empty rendering properties object"""

    @overload
    def __init__(self, theRenderingProperties: nanoocp.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties | None) -> None:
        """
        Constructor from STEP rendering properties entity.
        Extracts color, transparency, and other properties from the STEP entity.
        @param[in] theRenderingProperties rendering properties entity
        """

    @overload
    def __init__(self, theRGBAColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """
        Constructor from RGBA color.
        Creates rendering properties with the given color and transparency.
        @param[in] theRGBAColor color with transparency
        """

    @overload
    def __init__(self, theMaterial: nanoocp.XCAFDoc.XCAFDoc_VisMaterialCommon) -> None:
        """
        Constructor from XCAFDoc_VisMaterialCommon.
        Creates rendering properties using material properties from the OCCT material.
        @param[in] theMaterial common visualization material properties
        """

    @overload
    def __init__(self, theMaterial: nanoocp.XCAFDoc.XCAFDoc_VisMaterial | None) -> None:
        """
        Constructor from XCAFDoc_VisMaterial.
        Creates rendering properties using material properties from the OCCT material.
        @param[in] theMaterial visualization material properties
        """

    @overload
    def __init__(self, theSurfaceColor: nanoocp.Quantity.Quantity_Color, theTransparency: float = 0.0) -> None:
        """
        Constructor from surface color, transparency, and rendering method.
        @param[in] theSurfaceColor surface color
        @param[in] theTransparency transparency value
        """

    @overload
    def __init__(self, theColor: nanoocp.StepVisual.StepVisual_Colour | None, theTransparency: float) -> None:
        """
        Constructor from STEP color and transparency value.
        Creates rendering properties with the given color and transparency.
        @param[in] theColor color
        @param[in] theTransparency transparency value
        """

    @overload
    def __init__(self, theOther: STEPConstruct_RenderingProperties) -> None: ...

    @overload
    def Init(self, theRenderingProperties: nanoocp.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties | None) -> None:
        """
        Initializes from STEP rendering properties entity.
        Extracts color, transparency, and other properties from the STEP entity.
        @param[in] theRenderingProperties rendering properties entity
        """

    @overload
    def Init(self, theRGBAColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """
        Initializes from RGBA color.
        @param[in] theRGBAColor color with transparency
        """

    @overload
    def Init(self, theColor: nanoocp.StepVisual.StepVisual_Colour | None, theTransparency: float) -> None:
        """
        Initializes from STEP color and transparency value.
        @param[in] theColor STEP color entity
        @param[in] theTransparency transparency value
        """

    @overload
    def Init(self, theMaterial: nanoocp.XCAFDoc.XCAFDoc_VisMaterialCommon) -> None:
        """
        Initializes from XCAFDoc_VisMaterialCommon.
        @param[in] theMaterial common visualization material properties
        """

    @overload
    def Init(self, theMaterial: nanoocp.XCAFDoc.XCAFDoc_VisMaterial | None) -> None:
        """
        Initializes from XCAFDoc_VisMaterial.
        @param[in] theMaterial visualization material properties
        """

    @overload
    def Init(self, theSurfaceColor: nanoocp.Quantity.Quantity_Color, theTransparency: float = 0.0) -> None:
        """
        Initializes from surface color, transparency and rendering method.
        @param[in] theSurfaceColor surface color
        @param[in] theTransparency transparency value
        """

    def SetAmbientReflectance(self, theAmbientReflectance: float) -> None:
        """
        Sets ambient reflectance value
        @param[in] theAmbientReflectance ambient reflectance value
        """

    def SetAmbientAndDiffuseReflectance(self, theAmbientReflectance: float, theDiffuseReflectance: float) -> None:
        """
        Sets ambient and diffuse reflectance values
        @param[in] theAmbientReflectance ambient reflectance value
        @param[in] theDiffuseReflectance diffuse reflectance value
        """

    def SetAmbientDiffuseAndSpecularReflectance(self, theAmbientReflectance: float, theDiffuseReflectance: float, theSpecularReflectance: float, theSpecularExponent: float, theSpecularColour: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets ambient, diffuse and specular reflectance values
        @param[in] theAmbientReflectance ambient reflectance value
        @param[in] theDiffuseReflectance diffuse reflectance value
        @param[in] theSpecularReflectance specular reflectance value
        @param[in] theSpecularExponent specular exponent value
        @param[in] theSpecularColour specular color
        """

    @overload
    def CreateRenderingProperties(self) -> nanoocp.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties:
        """
        Creates and returns rendering properties entity
        @return created rendering properties entity
        """

    @overload
    def CreateRenderingProperties(self, theRenderColour: nanoocp.StepVisual.StepVisual_Colour | None) -> nanoocp.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties:
        """
        @param[in] theRenderColour color to be used for rendering
        @return created rendering properties entity
        """

    def CreateXCAFMaterial(self) -> nanoocp.XCAFDoc.XCAFDoc_VisMaterialCommon:
        """
        Creates and returns XCAF material entity
        @return created XCAF material entity
        """

    def GetRGBAColor(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """
        Creates the ColorRGBA object from the current color and transparency
        @return ColorRGBA object
        """

    def SurfaceColor(self) -> nanoocp.Quantity.Quantity_Color:
        """
        Returns surface color
        @return surface color
        """

    def Transparency(self) -> float:
        """
        Returns transparency value
        @return transparency value
        """

    def RenderingMethod(self) -> nanoocp.StepVisual.StepVisual_ShadingSurfaceMethod:
        """
        Returns rendering method
        @return rendering method
        """

    def SetRenderingMethod(self, theRenderingMethod: nanoocp.StepVisual.StepVisual_ShadingSurfaceMethod) -> None:
        """
        Sets rendering method
        @param[in] theRenderingMethod rendering method
        """

    def IsDefined(self) -> bool:
        """
        Returns whether the rendering properties are defined
        @return true if defined, false otherwise
        """

    def IsMaterialConvertible(self) -> bool:
        """
        Returns whether material is convertible to STEP
        @return true if fully defined for conversion, false otherwise
        """

    def AmbientReflectance(self) -> float:
        """
        Returns ambient reflectance value
        @return ambient reflectance value
        """

    def IsAmbientReflectanceDefined(self) -> bool:
        """
        Returns whether ambient reflectance is defined
        @return true if defined, false otherwise
        """

    def DiffuseReflectance(self) -> float:
        """
        Returns diffuse reflectance value
        @return diffuse reflectance value
        """

    def IsDiffuseReflectanceDefined(self) -> bool:
        """
        Returns whether diffuse reflectance is defined
        @return true if defined, false otherwise
        """

    def SpecularReflectance(self) -> float:
        """
        Returns specular reflectance value
        @return specular reflectance value
        """

    def IsSpecularReflectanceDefined(self) -> bool:
        """
        Returns whether specular reflectance is defined
        @return true if defined, false otherwise
        """

    def SpecularExponent(self) -> float:
        """
        Returns specular exponent value
        @return specular exponent value
        """

    def IsSpecularExponentDefined(self) -> bool:
        """
        Returns whether specular exponent is defined
        @return true if defined, false otherwise
        """

    def SpecularColour(self) -> nanoocp.Quantity.Quantity_Color:
        """
        Returns specular color
        @return specular color
        """

    def IsSpecularColourDefined(self) -> bool:
        """
        Returns whether specular color is defined
        @return true if defined, false otherwise
        """

class STEPConstruct_Styles(STEPConstruct_Tool):
    """
    Provides a mechanism for reading and writing shape styles
    (such as color) to and from the STEP file
    This tool maintains a list of styles, either taking them
    from STEP model (reading), or filling it by calls to
    AddStyle or directly (writing).
    Some methods deal with general structures of styles and
    presentations in STEP, but there are methods which deal
    with particular implementation of colors (as described in RP)
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> None:
        """Creates a tool and initializes it"""

    @overload
    def __init__(self, theOther: STEPConstruct_Styles) -> None: ...

    def Init(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> bool:
        """Initializes tool; returns True if succeeded"""

    def NbStyles(self) -> int:
        """Returns number of defined styles"""

    def Style(self, i: int) -> nanoocp.StepVisual.StepVisual_StyledItem:
        """Returns style with given index"""

    def NbRootStyles(self) -> int:
        """Returns number of override styles"""

    def RootStyle(self, i: int) -> nanoocp.StepVisual.StepVisual_StyledItem:
        """Returns override style with given index"""

    def ClearStyles(self) -> None:
        """Clears all defined styles and PSA sequence"""

    @overload
    def AddStyle(self, style: nanoocp.StepVisual.StepVisual_StyledItem | None) -> None:
        """Adds a style to a sequence"""

    @overload
    def AddStyle(self, item: nanoocp.StepRepr.StepRepr_RepresentationItem | None, PSA: nanoocp.StepVisual.StepVisual_PresentationStyleAssignment | None, Override: nanoocp.StepVisual.StepVisual_StyledItem | None) -> nanoocp.StepVisual.StepVisual_StyledItem:
        """
        Create a style linking giving PSA to the item, and add it to the
        sequence of stored styles. If Override is not Null, then
        the resulting style will be of the subtype OverridingStyledItem.
        """

    @overload
    def AddStyle(self, Shape: nanoocp.TopoDS.TopoDS_Shape, PSA: nanoocp.StepVisual.StepVisual_PresentationStyleAssignment | None, Override: nanoocp.StepVisual.StepVisual_StyledItem | None) -> nanoocp.StepVisual.StepVisual_StyledItem:
        """
        Create a style linking giving PSA to the Shape, and add it to the
        sequence of stored styles. If Override is not Null, then
        the resulting style will be of the subtype OverridingStyledItem.
        The Sape is used to find corresponding STEP entity by call to
        STEPConstruct::FindEntity(), then previous method is called.
        """

    def CreateMDGPR(self, Context: nanoocp.StepRepr.StepRepr_RepresentationContext | None) -> tuple[bool, nanoocp.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation, nanoocp.StepData.StepData_StepModel]:
        """
        Create MDGPR, fill it with all the styles previously defined,
        and add it to the model
        """

    def CreateNAUOSRD(self, Context: nanoocp.StepRepr.StepRepr_RepresentationContext | None, CDSR: nanoocp.StepShape.StepShape_ContextDependentShapeRepresentation | None, initPDS: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None) -> bool:
        """
        Create MDGPR, fill it with all the styles previously defined,
        and add it to the model
        IMPORTANT: <initPDS> must be null when use for NAUO colors
        <initPDS> initialised only for SHUO case.
        """

    def FindContext(self, Shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.StepRepr.StepRepr_RepresentationContext:
        """
        Searches the STEP model for the RepresentationContext in which
        given shape is defined. This context (if found) can be used
        then in call to CreateMDGPR()
        """

    def LoadStyles(self) -> bool:
        """
        Searches the STEP model for the MDGPR or DM entities
        (which bring styles) and fills sequence of styles
        """

    def LoadInvisStyles(self) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]]:
        """
        Searches the STEP model for the INISIBILITY entities
        (which bring styles) and fills out sequence of styles
        """

    def MakeColorPSA(self, item: nanoocp.StepRepr.StepRepr_RepresentationItem | None, SurfCol: nanoocp.StepVisual.StepVisual_Colour | None, CurveCol: nanoocp.StepVisual.StepVisual_Colour | None, theRenderingProps: STEPConstruct_RenderingProperties, isForNAUO: bool = False) -> nanoocp.StepVisual.StepVisual_PresentationStyleAssignment:
        """
        Create a PresentationStyleAssignment entity which defines
        two colors (for filling surfaces and curves)
        if isForNAUO true then returns PresentationStyleByContext
        """

    def GetColorPSA(self, item: nanoocp.StepRepr.StepRepr_RepresentationItem | None, Col: nanoocp.StepVisual.StepVisual_Colour | None) -> nanoocp.StepVisual.StepVisual_PresentationStyleAssignment:
        """
        Returns a PresentationStyleAssignment entity which defines
        surface and curve colors as Col. This PSA is either created
        or taken from internal map where all PSAs created by this
        method are remembered.
        """

    def GetColors(self, theStyle: nanoocp.StepVisual.StepVisual_StyledItem | None, theRenderingProps: STEPConstruct_RenderingProperties) -> tuple[bool, nanoocp.StepVisual.StepVisual_Colour, nanoocp.StepVisual.StepVisual_Colour, nanoocp.StepVisual.StepVisual_Colour, bool]:
        """
        Extract color definitions from the style entity
        For each type of color supported, result can be either
        NULL if it is not defined by that style, or last
        definition (if they are 1 or more)
        """

    @overload
    @staticmethod
    def EncodeColor(Col: nanoocp.Quantity.Quantity_Color) -> nanoocp.StepVisual.StepVisual_Colour: ...

    @overload
    @staticmethod
    def EncodeColor(Col: nanoocp.Quantity.Quantity_Color, DPDCs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient], ColRGBs: nanoocp.NCollection.NCollection_DataMap[nanoocp.gp.gp_Pnt, nanoocp.Standard.Standard_Transient]) -> nanoocp.StepVisual.StepVisual_Colour:
        """
        Create STEP color entity by given Quantity_Color
        The analysis is performed for whether the color corresponds to
        one of standard colors predefined in STEP. In that case,
        PredefinedColour entity is created instead of RGBColour
        """

    @staticmethod
    def DecodeColor(Colour: nanoocp.StepVisual.StepVisual_Colour | None, Col: nanoocp.Quantity.Quantity_Color) -> bool:
        """
        Decodes STEP color and fills the Quantity_Color.
        Returns True if OK or False if color is not recognized
        """

class STEPConstruct_UnitContext:
    """
    Tool for creation (encoding) and decoding (for writing and reading
    accordingly) context defining units and tolerances (uncerntanties)
    """

    @overload
    def __init__(self) -> None:
        """Creates empty tool"""

    @overload
    def __init__(self, theOther: STEPConstruct_UnitContext) -> None: ...

    def Init(self, Tol3d: float, theModel: nanoocp.StepData.StepData_StepModel | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None:
        """
        Creates new context (units are MM and radians,
        uncertainty equal to Tol3d)
        """

    def IsDone(self) -> bool:
        """Returns True if Init was called successfully"""

    def Value(self) -> nanoocp.StepGeom.StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx:
        """Returns context (or Null if not done)"""

    @overload
    def ComputeFactors(self, aContext: nanoocp.StepRepr.StepRepr_GlobalUnitAssignedContext | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> int:
        """
        Computes the length, plane angle and solid angle conversion factor.
        Returns a status, 0 if OK
        """

    @overload
    def ComputeFactors(self, aUnit: nanoocp.StepBasic.StepBasic_NamedUnit | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> int: ...

    def ComputeTolerance(self, aContext: nanoocp.StepRepr.StepRepr_GlobalUncertaintyAssignedContext | None) -> int:
        """Computes the uncertainty value (for length)"""

    def LengthFactor(self) -> float:
        """Returns the lengthFactor"""

    def PlaneAngleFactor(self) -> float:
        """Returns the planeAngleFactor"""

    def SolidAngleFactor(self) -> float:
        """Returns the solidAngleFactor"""

    def Uncertainty(self) -> float:
        """
        Returns the Uncertainty value (for length)
        It has been converted with LengthFactor
        """

    def AreaFactor(self) -> float:
        """Returns the areaFactor"""

    def VolumeFactor(self) -> float:
        """Returns the volumeFactor"""

    def HasUncertainty(self) -> bool:
        """Tells if a Uncertainty (for length) is recorded"""

    def LengthDone(self) -> bool:
        """
        Returns true if ComputeFactors has calculated
        a LengthFactor
        """

    def PlaneAngleDone(self) -> bool:
        """
        Returns true if ComputeFactors has calculated
        a PlaneAngleFactor
        """

    def SolidAngleDone(self) -> bool:
        """
        Returns true if ComputeFactors has calculated
        a SolidAngleFactor
        """

    def AreaDone(self) -> bool:
        """Returns true if areaFactor is computed"""

    def VolumeDone(self) -> bool:
        """Returns true if volumeFactor is computed"""

    def StatusMessage(self, status: int) -> str:
        """
        Returns a message for a given status (0 - empty)
        This message can then be added as warning for transfer
        """

    @staticmethod
    def ConvertSiPrefix(aPrefix: nanoocp.StepBasic.StepBasic_SiPrefix) -> float:
        """
        Convert SI prefix defined by enumeration to corresponding
        real factor (e.g. 1e6 for mega)
        """

class STEPConstruct_ValidationProps(STEPConstruct_Tool):
    """
    This class provides tools for access (write and read)
    the validation properties on shapes in the STEP file.
    These are surface area, solid volume and centroid.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> None:
        """Creates a tool and loads it with worksession"""

    @overload
    def __init__(self, theOther: STEPConstruct_ValidationProps) -> None: ...

    def Init(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> bool:
        """Load worksession; returns True if succeeded"""

    @overload
    def AddProp(self, Shape: nanoocp.TopoDS.TopoDS_Shape, Prop: nanoocp.StepRepr.StepRepr_RepresentationItem | None, Descr: str, instance: bool = False) -> bool:
        """
        General method for adding (writing) a validation property
        for shape which should be already mapped on writing itself.
        It uses FindTarget() to find target STEP entity
        resulting from given shape, and associated context
        Returns True if success, False in case of fail
        """

    @overload
    def AddProp(self, target: nanoocp.StepRepr.StepRepr_CharacterizedDefinition, Context: nanoocp.StepRepr.StepRepr_RepresentationContext | None, Prop: nanoocp.StepRepr.StepRepr_RepresentationItem | None, Descr: str) -> bool:
        """
        General method for adding (writing) a validation property
        for shape which should be already mapped on writing itself.
        It takes target and Context entities which correspond to shape
        Returns True if success, False in case of fail
        """

    def AddArea(self, Shape: nanoocp.TopoDS.TopoDS_Shape, Area: float) -> bool:
        """
        Adds surface area property for given shape (already mapped).
        Returns True if success, False in case of fail
        """

    def AddVolume(self, Shape: nanoocp.TopoDS.TopoDS_Shape, Vol: float) -> bool:
        """
        Adds volume property for given shape (already mapped).
        Returns True if success, False in case of fail
        """

    def AddCentroid(self, Shape: nanoocp.TopoDS.TopoDS_Shape, Pnt: nanoocp.gp.gp_Pnt, instance: bool = False) -> bool:
        """
        Adds centroid property for given shape (already mapped).
        Returns True if success, False in case of fail
        If instance is True, then centroid is assigned to
        an instance of component in assembly
        """

    def FindTarget(self, S: nanoocp.TopoDS.TopoDS_Shape, target: nanoocp.StepRepr.StepRepr_CharacterizedDefinition, instance: bool = False) -> tuple[bool, nanoocp.StepRepr.StepRepr_RepresentationContext]:
        """
        Finds target STEP entity to which validation props should
        be assigned, and corresponding context, starting from shape
        Returns True if success, False in case of fail
        """

    def LoadProps(self, seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.Standard.Standard_Transient]) -> bool:
        """
        Searches for entities of the type PropertyDefinitionRepresentation
        in the model and fills the sequence by them
        """

    def GetPropNAUO(self, PD: nanoocp.StepRepr.StepRepr_PropertyDefinition | None) -> nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence:
        """
        Returns CDSR associated with given PpD or NULL if not found
        (when, try GetPropSDR)
        """

    def GetPropPD(self, PD: nanoocp.StepRepr.StepRepr_PropertyDefinition | None) -> nanoocp.StepBasic.StepBasic_ProductDefinition:
        """
        Returns SDR associated with given PpD or NULL if not found
        (when, try GetPropCDSR)
        """

    @overload
    def GetPropShape(self, ProdDef: nanoocp.StepBasic.StepBasic_ProductDefinition | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns Shape associated with given SDR or Null Shape
        if not found
        """

    @overload
    def GetPropShape(self, PD: nanoocp.StepRepr.StepRepr_PropertyDefinition | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns Shape associated with given PpD or Null Shape
        if not found
        """

    def GetPropReal(self, item: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> tuple[bool, float, bool]:
        """
        Returns value of Real-Valued property (Area or Volume)
        If Property is neither Area nor Volume, returns False
        Else returns True and isArea indicates whether property
        is area or volume
        """

    def GetPropPnt(self, item: nanoocp.StepRepr.StepRepr_RepresentationItem | None, Context: nanoocp.StepRepr.StepRepr_RepresentationContext | None, Pnt: nanoocp.gp.gp_Pnt, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """Returns value of Centroid property (or False if it is not)"""

    def SetAssemblyShape(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets current assembly shape SDR (for FindCDSR calls)"""
