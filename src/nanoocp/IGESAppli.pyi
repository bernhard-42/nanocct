"""OCCT package IGESAppli (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESBasic
import nanoocp.IGESData
import nanoocp.IGESDefs
import nanoocp.IGESDimen
import nanoocp.IGESDraw
import nanoocp.IGESGeom
import nanoocp.IGESGraph
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class IGESAppli:
    """
    This package represents collection of miscellaneous
    entities from IGES
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESAppli_Protocol:
        """Returns the Protocol for this Package"""

class IGESAppli_DrilledHole(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines DrilledHole, Type <406> Form <6>
    in package IGESAppli
    Identifies an entity representing a drilled hole
    through a printed circuit board.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_DrilledHole) -> None: ...

    def Init(self, nbPropVal: int, aSize: float, anotherSize: float, aPlating: int, aLayer: int, anotherLayer: int) -> None:
        """
        This method is used to set the fields of the class
        DrilledHole
        - nbPropVal    : Number of property values = 5
        - aSize        : Drill diameter size
        - anotherSize  : Finish diameter size
        - aPlating     : Plating indication flag
        False = not plating
        True  = is plating
        - aLayer       : Lower numbered layer
        - anotherLayer : Higher numbered layer
        """

    def NbPropertyValues(self) -> int:
        """is always 5"""

    def DrillDiaSize(self) -> float:
        """returns the drill diameter size"""

    def FinishDiaSize(self) -> float:
        """returns the finish diameter size"""

    def IsPlating(self) -> bool:
        """
        Returns Plating Status:
        False = not plating / True = is plating
        """

    def NbLowerLayer(self) -> int:
        """returns the lower numbered layer"""

    def NbHigherLayer(self) -> int:
        """returns the higher numbered layer"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_Node(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Node, Type <134> Form <0>
    in package IGESAppli
    Geometric point used in the definition of a finite element.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_Node) -> None: ...

    def Init(self, aCoord: nanoocp.gp.gp_XYZ, aCoordSystem: nanoocp.IGESGeom.IGESGeom_TransformationMatrix | None) -> None:
        """
        This method is used to set the fields of the class Node
        - aCoord       : Nodal Coordinates
        - aCoordSystem : the Nodal Displacement Coordinate
        System Entity (default 0 is Global
        Cartesian Coordinate system)
        """

    def Coord(self) -> nanoocp.gp.gp_Pnt:
        """returns the nodal coordinates"""

    def System(self) -> nanoocp.IGESData.IGESData_TransfEntity:
        """
        returns TransfEntity if a Nodal Displacement Coordinate
        System Entity is defined
        else (for Global Cartesien) returns Null Handle
        """

    def SystemType(self) -> int:
        """
        Computes & returns the Type of Coordinate System :
        0 GlobalCartesian, 1 Cartesian, 2 Cylindrical, 3 Spherical
        """

    def TransformedNodalCoord(self) -> nanoocp.gp.gp_Pnt:
        """returns the Nodal coordinates after transformation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_FiniteElement(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines FiniteElement, Type <136> Form <0>
    in package IGESAppli
    Used to define a finite element with the help of an
    element topology.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_FiniteElement) -> None: ...

    def Init(self, aType: int, allNodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESAppli.IGESAppli_Node] | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        FiniteElement
        - aType    : Indicates the topology type
        - allNodes : List of Nodes defining the element
        - aName    : Element type name
        """

    def Topology(self) -> int:
        """returns Topology type"""

    def NbNodes(self) -> int:
        """returns the number of nodes defining the element"""

    def Node(self, Index: int) -> IGESAppli_Node:
        """
        returns Node defining element entity
        raises exception if Index <= 0 or Index > NbNodes()
        """

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Element Type Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_ElementResults(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ElementResults, Type <148>
    in package IGESAppli
    Used to find the results of FEM analysis
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_ElementResults) -> None: ...

    def Init(self, aNote: nanoocp.IGESDimen.IGESDimen_GeneralNote | None, aSubCase: int, aTime: float, nbResults: int, aResRepFlag: int, allElementIdents: nanoocp.NCollection.NCollection_HArray1[int] | None, allFiniteElems: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESAppli.IGESAppli_FiniteElement] | None, allTopTypes: nanoocp.NCollection.NCollection_HArray1[int] | None, nbLayers: nanoocp.NCollection.NCollection_HArray1[int] | None, allDataLayerFlags: nanoocp.NCollection.NCollection_HArray1[int] | None, allnbResDataLocs: nanoocp.NCollection.NCollection_HArray1[int] | None, allResDataLocs: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger | None, allResults: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfReal | None) -> None:
        """
        This method is used to set the fields of the class
        ElementResults
        - aNote             : GeneralNote Entity describing analysis
        - aSubCase          : Analysis Subcase number
        - aTime             : Analysis time value
        - nbResults         : Number of result values per FEM
        - aResRepFlag       : Results Reporting Flag
        - allElementIdents  : FEM element number for elements
        - allFiniteElems    : FEM element
        - allTopTypes       : Element Topology Types
        - nbLayers          : Number of layers per result data location
        - allDataLayerFlags : Data Layer Flags
        - allnbResDataLocs  : Number of result data report locations
        - allResDataLocs    : Result Data Report Locations
        - allResults        : List of Result data values of FEM analysis
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes the FormNumber (which indicates Type of Result)
        Error if not in range [0-34]
        """

    def Note(self) -> nanoocp.IGESDimen.IGESDimen_GeneralNote:
        """returns General Note Entity describing analysis case"""

    def SubCaseNumber(self) -> int:
        """returns analysis Subcase number"""

    def Time(self) -> float:
        """returns analysis time value"""

    def NbResultValues(self) -> int:
        """returns number of result values per FEM"""

    def ResultReportFlag(self) -> int:
        """returns Results Reporting Flag"""

    def NbElements(self) -> int:
        """returns number of FEM elements"""

    def ElementIdentifier(self, Index: int) -> int:
        """returns FEM element number for elements"""

    def Element(self, Index: int) -> IGESAppli_FiniteElement:
        """returns FEM element"""

    def ElementTopologyType(self, Index: int) -> int:
        """returns element Topology Types"""

    def NbLayers(self, Index: int) -> int:
        """returns number of layers per result data location"""

    def DataLayerFlag(self, Index: int) -> int:
        """returns Data Layer Flags"""

    def NbResultDataLocs(self, Index: int) -> int:
        """returns number of result data report locations"""

    def ResultDataLoc(self, NElem: int, NLoc: int) -> int:
        """
        returns Result Data Report Locations
        UNFINISHED
        """

    def NbResults(self, Index: int) -> int:
        """returns total number of results"""

    @overload
    def ResultData(self, NElem: int, num: int) -> float:
        """
        returns Result data value for an Element, given its
        order between 1 and <NbResults(NElem)> (direct access)
        For a more comprehensive access, see below
        """

    @overload
    def ResultData(self, NElem: int, NVal: int, NLay: int, NLoc: int) -> float:
        """
        returns Result data values of FEM analysis, according this
        definition :
        - <NElem> : n0 of the Element to be considered
        - <NVal> : n0 of the Value between 1 and NbResultValues
        - <NLay> : n0 of the Layer for this Element
        - <NLoc> : n0 of the Data Location for this Element
        This gives for each Element, the corresponding rank
        computed by ResultRank, in which the leftmost subscript
        changes most rapidly
        """

    def ResultRank(self, NElem: int, NVal: int, NLay: int, NLoc: int) -> int:
        """
        Computes, for a given Element <NElem>, the rank of a
        individual Result Data, given <NVal>,<NLay>,<NLoc>
        """

    def ResultList(self, NElem: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns in once the entire list of data for an Element,
        addressed as by ResultRank (See above)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_Flow(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Flow, Type <402> Form <18>
    in package IGESAppli
    Represents a single signal or a single fluid flow path
    starting from a starting Connect Point Entity and
    including additional intermediate connect points.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_Flow) -> None: ...

    def Init(self, nbContextFlags: int, aFlowType: int, aFuncFlag: int, allFlowAssocs: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allConnectPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDraw.IGESDraw_ConnectPoint] | None, allJoins: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allFlowNames: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, allTextDisps: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate] | None, allContFlowAssocs: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class Flow
        - nbContextFlags    : Count of Context Flags, always = 2
        - aFlowType         : Type of Flow, default = 0
        - aFuncFlag         : Function Flag, default = 0
        - allFlowAssocs     : Flow Associativity Entities
        - allConnectPoints  : Connect Point Entities
        - allJoins          : Join Entities
        - allFlowNames      : Flow Names
        - allTextDisps      : Text Display Template Entities
        - allContFlowAssocs : Continuation Flow Associativity Entities
        """

    def OwnCorrect(self) -> bool:
        """forces NbContextFalgs to 2, returns True if changed"""

    def NbContextFlags(self) -> int:
        """returns number of Count of Context Flags, always = 2"""

    def NbFlowAssociativities(self) -> int:
        """returns number of Flow Associativity Entities"""

    def NbConnectPoints(self) -> int:
        """returns number of Connect Point Entities"""

    def NbJoins(self) -> int:
        """returns number of Join Entities"""

    def NbFlowNames(self) -> int:
        """returns number of Flow Names"""

    def NbTextDisplayTemplates(self) -> int:
        """returns number of Text Display Template Entities"""

    def NbContFlowAssociativities(self) -> int:
        """returns number of Continuation Flow Associativity Entities"""

    def TypeOfFlow(self) -> int:
        """
        returns Type of Flow = 0 : Not Specified (default)
        1 : Logical
        2 : Physical
        """

    def FunctionFlag(self) -> int:
        """
        returns Function Flag = 0 : Not Specified (default)
        1 : Electrical Signal
        2 : Fluid Flow Path
        """

    def FlowAssociativity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Flow Associativity Entity
        raises exception if Index <= 0 or Index > NbFlowAssociativities()
        """

    def ConnectPoint(self, Index: int) -> nanoocp.IGESDraw.IGESDraw_ConnectPoint:
        """
        returns Connect Point Entity
        raises exception if Index <= 0 or Index > NbConnectPoints()
        """

    def Join(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Join Entity
        raises exception if Index <= 0 or Index > NbJoins()
        """

    def FlowName(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns Flow Name
        raises exception if Index <= 0 or Index > NbFlowNames()
        """

    def TextDisplayTemplate(self, Index: int) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate:
        """
        returns Text Display Template Entity
        raises exception if Index <= 0 or Index > NbTextDisplayTemplates()
        """

    def ContFlowAssociativity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Continuation Flow Associativity Entity
        raises exception if Index <= 0 or Index > NbContFlowAssociativities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_FlowLineSpec(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines FlowLineSpec, Type <406> Form <14>
    in package IGESAppli
    Attaches one or more text strings to entities being
    used to represent a flow line
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_FlowLineSpec) -> None: ...

    def Init(self, allProperties: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        This method is used to set the fields of the class
        FlowLineSpec
        - allProperties : primary flow line specification and modifiers
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values"""

    def FlowLineName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns primary flow line specification name"""

    def Modifier(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns specified modifier element
        raises exception if Index <= 1 or Index > NbPropertyValues
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESAppli (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESAppli and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESAppli_GeneralModule) -> None: ...

    def OwnSharedCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a given IGESEntity <ent>, from
        its specific parameters : specific for each type
        """

    def DirChecker(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """
        Returns a DirChecker, specific for each type of Entity
        (identified by its Case Number) : this DirChecker defines
        constraints which must be respected by the DirectoryPart
        """

    def OwnCheckCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check for each type of Entity"""

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """Specific creation of a new void entity"""

    def OwnCopyCase(self, CN: int, entfrom: nanoocp.IGESData.IGESData_IGESEntity | None, entto: nanoocp.IGESData.IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies parameters which are specific of each Type of Entity"""

    def CategoryNumber(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> int:
        """
        Returns a category number which characterizes an entity
        FEA for : ElementResults,FiniteElement,Node&Co
        Piping for : Flow & Co
        Professional for : others (in fact Schematics)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_LevelFunction(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines LevelFunction, Type <406> Form <3>
    in package IGESAppli
    Used to transfer the meaning or intended use of a level
    in the sending system
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_LevelFunction) -> None: ...

    def Init(self, nbPropVal: int, aCode: int, aFuncDescrip: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        LevelFunction
        - nbPropVal    : Number of Properties, always = 2
        - aCode        : Function Description code
        default = 0
        - aFuncDescrip : Function Description
        default = null string
        """

    def NbPropertyValues(self) -> int:
        """is always 2"""

    def FuncDescriptionCode(self) -> int:
        """returns the function description code. Default = 0"""

    def FuncDescription(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns the function description
        Default = null string
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_LevelToPWBLayerMap(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines LevelToPWBLayerMap, Type <406> Form <24>
    in package IGESAppli
    Used to correlate an exchange file level number with
    its corresponding native level identifier, physical PWB
    layer number and predefined functional level
    identification
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_LevelToPWBLayerMap) -> None: ...

    def Init(self, nbPropVal: int, allExchLevels: nanoocp.NCollection.NCollection_HArray1[int] | None, allNativeLevels: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, allPhysLevels: nanoocp.NCollection.NCollection_HArray1[int] | None, allExchIdents: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        This method is used to set the fields of the class
        LevelToPWBLayerMap
        - nbPropVal       : Number of property values
        - allExchLevels   : Exchange File Level Numbers
        - allNativeLevels : Native Level Identifications
        - allPhysLevels   : Physical Layer Numbers
        - allExchIdents   : Exchange File Level Identifications
        raises exception if allExchLevels, allNativeLevels, allPhysLevels
        and all ExchIdents are not of same dimensions
        """

    def NbPropertyValues(self) -> int:
        """returns number of property values"""

    def NbLevelToLayerDefs(self) -> int:
        """returns number of level to layer definitions"""

    def ExchangeFileLevelNumber(self, Index: int) -> int:
        """
        returns Exchange File Level Number
        raises exception if Index <= 0 or Index > NbLevelToLayerDefs
        """

    def NativeLevel(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns Native Level Identification
        raises exception if Index <= 0 or Index > NbLevelToLayerDefs
        """

    def PhysicalLayerNumber(self, Index: int) -> int:
        """
        returns Physical Layer Number
        raises exception if Index <= 0 or Index > NbLevelToLayerDefs
        """

    def ExchangeFileLevelIdent(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_LineWidening(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines LineWidening, Type <406> Form <5>
    in package IGESAppli
    Defines the characteristics of entities when they are
    used to define locations of items.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_LineWidening) -> None: ...

    def Init(self, nbPropVal: int, aWidth: float, aCornering: int, aExtnFlag: int, aJustifFlag: int, aExtnVal: float) -> None:
        """
        This method is used to set the fields of the class
        LineWidening
        - nbPropVal   : Number of property values = 5
        - aWidth      : Width of metalization
        - aCornering  : Cornering codes
        0 = rounded
        1 = squared
        - aExtnFlag   : Extension Flag
        0 = No Extension
        1 = One-half width extension
        2 = Extn set by ExtnVal
        - aJustifFlag : Justification flag
        0 = Center justified
        1 = left justified
        2 = right justified
        - aExtnVal    : Extension value if aExtnFlag = 2
        """

    def NbPropertyValues(self) -> int:
        """
        returns the number of property values
        is always 5
        """

    def WidthOfMetalization(self) -> float:
        """returns the width of metallization"""

    def CorneringCode(self) -> int:
        """
        returns the cornering code
        0 = Rounded  / 1 = Squared
        """

    def ExtensionFlag(self) -> int:
        """
        returns the extension flag
        0 = No extension
        1 = One-half width extension
        2 = Extension set by theExtnVal
        """

    def JustificationFlag(self) -> int:
        """
        returns the justification flag
        0 = Centre justified
        1 = Left justified
        2 = Right justified
        """

    def ExtensionValue(self) -> float:
        """
        returns the Extension Value
        Present only if theExtnFlag = 2
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_NodalConstraint(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines NodalConstraint, Type <418> Form <0>
    in package IGESAppli
    Relates loads and/or constraints to specific nodes in
    the Finite Element Model by creating a relation between
    Node entities and Tabular Data Property that contains
    the load or constraint data
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_NodalConstraint) -> None: ...

    def Init(self, aType: int, aNode: IGESAppli_Node | None, allTabData: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDefs.IGESDefs_TabularData] | None) -> None:
        """
        This method is used to set the fields of the class
        NodalConstraint
        - aType      : Loads / Constraints
        - aNode      : the Node
        - allTabData : Tabular Data Property carrying the load
        or constraint vector
        """

    def NbCases(self) -> int:
        """returns total number of cases"""

    def Type(self) -> int:
        """returns whether Loads (1) or Constraints (2)"""

    def NodeEntity(self) -> IGESAppli_Node:
        """returns the Node"""

    def TabularData(self, Index: int) -> nanoocp.IGESDefs.IGESDefs_TabularData:
        """
        returns Tabular Data Property carrying load or constraint vector
        raises exception if Index <= 0 or Index > NbCases
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_NodalDisplAndRot(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines NodalDisplAndRot, Type <138> Form <0>
    in package IGESAppli
    Used to communicate finite element post processing
    data.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_NodalDisplAndRot) -> None: ...

    def Init(self, allNotes: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_GeneralNote] | None, allIdentifiers: nanoocp.NCollection.NCollection_HArray1[int] | None, allNodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESAppli.IGESAppli_Node] | None, allRotParams: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfXYZ | None, allTransParams: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfXYZ | None) -> None:
        """
        This method is used to set the fields of the class
        NodalDisplAndRot
        - allNotes       : Used to store the general note describing
        the analysis cases
        - allIdentifiers : Used to store the node number
        identifier for the nodes
        - allNodes       : Used to store the nodes
        - allRotParams   : Used to store the rotation for the nodes
        - allTransParams : Used to store the incremental
        displacements for the nodes
        raises exception if Lengths of allIdentifiers, allNodes,
        allRotParams, and allTransParams are not same
        or if length of allNotes and size of each element of allRotParams
        and allTransParam are not same
        """

    def NbCases(self) -> int:
        """returns the number of analysis cases"""

    def NbNodes(self) -> int:
        """returns the number of nodes"""

    def Note(self, Index: int) -> nanoocp.IGESDimen.IGESDimen_GeneralNote:
        """
        returns the General Note that describes the Index analysis case
        raises exception if Index <= 0 or Index > NbCases
        """

    def NodeIdentifier(self, Index: int) -> int:
        """
        returns the node identifier as specified by the Index
        raises exception if Index <= 0 or Index > NbNodes
        """

    def Node(self, Index: int) -> IGESAppli_Node:
        """
        returns the node as specified by the Index
        raises exception if Index <= 0 or Index > NbNodes
        """

    def TranslationParameter(self, NodeNum: int, CaseNum: int) -> nanoocp.gp.gp_XYZ:
        """
        returns the Translational Parameters for the particular Index
        Exception raised if NodeNum <= 0 or NodeNum > NbNodes()
        or CaseNum <= 0 or CaseNum > NbCases()
        """

    def RotationalParameter(self, NodeNum: int, CaseNum: int) -> nanoocp.gp.gp_XYZ:
        """
        returns the Rotational Parameters for Index
        Exception raised if NodeNum <= 0 or NodeNum > NbNodes()
        or CaseNum <= 0 or CaseNum > NbCases()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_NodalResults(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines NodalResults, Type <146>
    in package IGESAppli
    Used to store the Analysis Data results per FEM Node
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_NodalResults) -> None: ...

    def Init(self, aNote: nanoocp.IGESDimen.IGESDimen_GeneralNote | None, aNumber: int, aTime: float, allNodeIdentifiers: nanoocp.NCollection.NCollection_HArray1[int] | None, allNodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESAppli.IGESAppli_Node] | None, allData: nanoocp.NCollection.NCollection_HArray2[float] | None) -> None:
        """
        This method is used to set the fields of the class
        NodalResults
        - aNote              : General Note that describes the
        analysis case
        - aNumber            : Analysis Subcase number
        - aTime              : Analysis time
        - allNodeIdentifiers : Node identifiers for the nodes
        - allNodes           : List of FEM Node Entities
        - allData            : Values of the Finite Element analysis
        result data
        raises exception if Lengths of allNodeIdentifiers, allNodes and
        allData (Cols) are not same
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes the FormNumber (which indicates Type of Result)
        Error if not in range [0-34]
        """

    def Note(self) -> nanoocp.IGESDimen.IGESDimen_GeneralNote:
        """returns the General Note Entity that describes the analysis case"""

    def SubCaseNumber(self) -> int:
        """returns zero if there is no subcase"""

    def Time(self) -> float:
        """
        returns the Analysis time value for this subcase. It is the time
        at which transient analysis results occur in the mathematical
        FEM model.
        """

    def NbData(self) -> int:
        """returns number of real values in array V for a FEM node"""

    def NbNodes(self) -> int:
        """returns number of FEM nodes for which data is to be read."""

    def NodeIdentifier(self, Index: int) -> int:
        """
        returns FEM node number identifier for the (Index)th node
        raises exception if Index <= 0 or Index > NbNodes
        """

    def Node(self, Index: int) -> IGESAppli_Node:
        """
        returns the node as specified by the Index
        raises exception if Index <= 0 or Index > NbNodes
        """

    def Data(self, NodeNum: int, DataNum: int) -> float:
        """
        returns the finite element analysis result value
        raises exception if (NodeNum <= 0 or NodeNum > NbNodes()) or
        if (DataNum <=0 or DataNum > NbData())
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_PartNumber(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines PartNumber, Type <406> Form <9>
    in package IGESAppli
    Attaches a set of text strings that define the common
    part numbers to an entity being used to represent a
    physical component
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_PartNumber) -> None: ...

    def Init(self, nbPropVal: int, aGenName: nanoocp.TCollection.TCollection_HAsciiString | None, aMilName: nanoocp.TCollection.TCollection_HAsciiString | None, aVendName: nanoocp.TCollection.TCollection_HAsciiString | None, anIntName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        PartNumber
        - nbPropVal : number of property values, always = 4
        - aGenName  : Generic part number or name
        - aMilName  : Military Standard (MIL-STD) part number
        - aVendName : Vendor part number or name
        - anIntName : Internal part number
        """

    def NbPropertyValues(self) -> int:
        """returns number of property values, always = 4"""

    def GenericNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Generic part number or name"""

    def MilitaryNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Military Standard (MIL-STD) part number"""

    def VendorNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Vendor part number or name"""

    def InternalNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Internal part number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_PinNumber(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines PinNumber, Type <406> Form <8>
    in package IGESAppli
    Used to attach a text string representing a component
    pin number to an entity being used to represent an
    electrical component's pin
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_PinNumber) -> None: ...

    def Init(self, nbPropVal: int, aValue: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        PinNumber
        - nbPropVal : Number of property values (always = 1)
        - aValue    : Pin Number value
        """

    def NbPropertyValues(self) -> int:
        """
        returns the number of property values
        is always 1
        """

    def PinNumberVal(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the pin number value"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_PipingFlow(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines PipingFlow, Type <402> Form <20>
    in package IGESAppli
    Represents a single fluid flow path
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_PipingFlow) -> None: ...

    def Init(self, nbContextFlags: int, aFlowType: int, allFlowAssocs: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allConnectPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDraw.IGESDraw_ConnectPoint] | None, allJoins: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allFlowNames: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, allTextDisps: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate] | None, allContFlowAssocs: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        PipingFlow
        - nbContextFlags    : Count of Context Flags, always = 1
        - aFlowType         : Type of Flow, default = 0
        - allFlowAssocs     : PipingFlow Associativity Entities
        - allConnectPoints  : Connect Point Entities
        - allJoins          : Join Entities
        - allFlowNames      : PipingFlow Names
        - allTextDispTs     : Text Display Template Entities
        - allContFlowAssocs : Continuation Flow Associativity Entities
        """

    def OwnCorrect(self) -> bool:
        """forces NbContextFalgs to 1, returns True if changed"""

    def NbContextFlags(self) -> int:
        """returns number of Count of Context Flags, always = 1"""

    def NbFlowAssociativities(self) -> int:
        """returns number of Piping Flow Associativity Entities"""

    def NbConnectPoints(self) -> int:
        """returns number of Connect Point Entities"""

    def NbJoins(self) -> int:
        """returns number of Join Entities"""

    def NbFlowNames(self) -> int:
        """returns number of Flow Names"""

    def NbTextDisplayTemplates(self) -> int:
        """returns number of Text Display Template Entities"""

    def NbContFlowAssociativities(self) -> int:
        """returns number of Continuation Piping Flow Associativities"""

    def TypeOfFlow(self) -> int:
        """
        returns Type of Flow = 0 : Not specified,
        1 : Logical,
        2 : Physical
        """

    def FlowAssociativity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Piping Flow Associativity Entity
        raises exception if Index <= 0 or Index > NbFlowAssociativities()
        """

    def ConnectPoint(self, Index: int) -> nanoocp.IGESDraw.IGESDraw_ConnectPoint:
        """
        returns Connect Point Entity
        raises exception if Index <= 0 or Index > NbConnectPoints()
        """

    def Join(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Join Entity
        raises exception if Index <= 0 or Index > NbJoins()
        """

    def FlowName(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns Flow Name
        raises exception if Index <= 0 or Index > NbFlowNames()
        """

    def TextDisplayTemplate(self, Index: int) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate:
        """
        returns Text Display Template Entity
        raises exception if Index <= 0 or Index > NbTextDisplayTemplates()
        """

    def ContFlowAssociativity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Continuation Piping Flow Associativity Entity
        raises exception if Index <= 0 or Index > NbContFlowAssociativities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESAppli"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of direct Resource Protocol. Here, two
        (Protocols from IGESDefs and IGESDraw)
        """

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank."""

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a Case Number, specific of each recognized Type
        This Case Number is then used in Libraries : the various
        Modules attached to this class of Protocol must use them
        in accordance (for a given value of TypeNumber, they must
        consider the same Type as the Protocol defines)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_PWBArtworkStackup(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines PWBArtworkStackup, Type <406> Form <25>
    in package IGESAppli
    Used to communicate which exchange file levels are to
    be combined in order to create the artwork for a
    printed wire board (PWB). This property should be
    attached to the entity defining the printed wire
    assembly (PWA) or if no such entity exists, then the
    property should stand alone in the file.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_PWBArtworkStackup) -> None: ...

    def Init(self, nbPropVal: int, anArtIdent: nanoocp.TCollection.TCollection_HAsciiString | None, allLevelNums: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        PWBArtworkStackup
        - nbPropVal    : number of property values
        - anArtIdent   : Artwork Stackup Identification
        - allLevelNums : Level Numbers
        """

    def NbPropertyValues(self) -> int:
        """returns number of property values"""

    def Identification(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Artwork Stackup Identification"""

    def NbLevelNumbers(self) -> int:
        """returns total number of Level Numbers"""

    def LevelNumber(self, Index: int) -> int:
        """
        returns Level Number
        raises exception if Index <= 0 or Index > NbLevelNumbers
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_PWBDrilledHole(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines PWBDrilledHole, Type <406> Form <26>
    in package IGESAppli
    Used to identify an entity that locates a drilled hole
    and to specify the characteristics of the drilled hole
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_PWBDrilledHole) -> None: ...

    def Init(self, nbPropVal: int, aDrillDia: float, aFinishDia: float, aCode: int) -> None:
        """
        This method is used to set the fields of the class
        PWBDrilledHole
        - nbPropVal  : number of property values, always = 3
        - aDrillDia  : Drill diameter size
        - aFinishDia : Finish diameter size
        - aCode      : Function code for drilled hole
        """

    def NbPropertyValues(self) -> int:
        """returns number of property values, always = 3"""

    def DrillDiameterSize(self) -> float:
        """returns Drill diameter size"""

    def FinishDiameterSize(self) -> float:
        """returns Finish diameter size"""

    def FunctionCode(self) -> int:
        """
        returns Function code for drilled hole
        is 0, 1, 2, 3, 4, 5 or 5001-9999
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines basic File Access Module for IGESAppli (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESAppli_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESAppli"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESAppli"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_ReferenceDesignator(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ReferenceDesignator, Type <406> Form <7>
    in package IGESAppli
    Used to attach a text string containing the value of
    a component reference designator to an entity being
    used to represent a component.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_ReferenceDesignator) -> None: ...

    def Init(self, nbPropVal: int, aText: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        ReferenceDesignator
        - nbPropVal : Number of property values = 1
        - aText     : Reference designator text
        """

    def NbPropertyValues(self) -> int:
        """
        returns the number of property values
        is always 1
        """

    def RefDesignatorText(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the Reference designator text"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_RegionRestriction(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines RegionRestriction, Type <406> Form <2>
    in package IGESAppli
    Defines regions to set an application's restriction
    over a region.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESAppli_RegionRestriction) -> None: ...

    def Init(self, nbPropVal: int, aViasRest: int, aCompoRest: int, aCktRest: int) -> None:
        """
        This method is used to set the fields of the class
        RegionRestriction
        - nbPropVal  : Number of property values, always = 3
        - aViasRest  : Electrical Vias restriction
        - aCompoRest : Electrical components restriction
        - aCktRest   : Electrical circuitry restriction
        """

    def NbPropertyValues(self) -> int:
        """is always 3"""

    def ElectricalViasRestriction(self) -> int:
        """
        returns the Electrical vias restriction
        is 0, 1 or 2
        """

    def ElectricalComponentRestriction(self) -> int:
        """
        returns the Electrical components restriction
        is 0, 1 or 2
        """

    def ElectricalCktRestriction(self) -> int:
        """
        returns the Electrical circuitry restriction
        is 0, 1 or 2
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """
    Defines Services attached to IGES Entities :
    Dump & OwnCorrect, for IGESAppli
    """

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESAppli & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESAppli_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESAppli"""

    def OwnCorrect(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """---Purpose"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESAppli_ToolDrilledHole:
    """
    Tool to work on a DrilledHole. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDrilledHole, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolDrilledHole) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_DrilledHole | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_DrilledHole | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_DrilledHole | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DrilledHole <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_DrilledHole | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DrilledHole
        (NbPropertyValues forced to 5, Level cleared if Subordinate != 0)
        """

    def DirChecker(self, ent: IGESAppli_DrilledHole | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_DrilledHole | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_DrilledHole | None, entto: IGESAppli_DrilledHole | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_DrilledHole | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolElementResults:
    """
    Tool to work on a ElementResults. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolElementResults, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolElementResults) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_ElementResults | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_ElementResults | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_ElementResults | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ElementResults <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_ElementResults | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_ElementResults | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_ElementResults | None, entto: IGESAppli_ElementResults | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_ElementResults | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolFiniteElement:
    """
    Tool to work on a FiniteElement. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolFiniteElement, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolFiniteElement) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_FiniteElement | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_FiniteElement | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_FiniteElement | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a FiniteElement <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_FiniteElement | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_FiniteElement | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_FiniteElement | None, entto: IGESAppli_FiniteElement | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_FiniteElement | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolFlow:
    """
    Tool to work on a Flow. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolFlow, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolFlow) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_Flow | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_Flow | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_Flow | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Flow <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_Flow | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Flow
        (NbContextFlags forced to 2)
        """

    def DirChecker(self, ent: IGESAppli_Flow | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_Flow | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_Flow | None, entto: IGESAppli_Flow | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_Flow | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolFlowLineSpec:
    """
    Tool to work on a FlowLineSpec. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolFlowLineSpec, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolFlowLineSpec) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_FlowLineSpec | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_FlowLineSpec | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_FlowLineSpec | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a FlowLineSpec <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_FlowLineSpec | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_FlowLineSpec | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_FlowLineSpec | None, entto: IGESAppli_FlowLineSpec | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_FlowLineSpec | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolLevelFunction:
    """
    Tool to work on a LevelFunction. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLevelFunction, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolLevelFunction) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_LevelFunction | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_LevelFunction | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_LevelFunction | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LevelFunction <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_LevelFunction | None) -> bool:
        """
        Sets automatic unambiguous Correction on a LevelFunction
        (NbPropertyValues forced to 2)
        """

    def DirChecker(self, ent: IGESAppli_LevelFunction | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_LevelFunction | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_LevelFunction | None, entto: IGESAppli_LevelFunction | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_LevelFunction | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolLevelToPWBLayerMap:
    """
    Tool to work on a LevelToPWBLayerMap. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLevelToPWBLayerMap, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolLevelToPWBLayerMap) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_LevelToPWBLayerMap | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_LevelToPWBLayerMap | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_LevelToPWBLayerMap | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LevelToPWBLayerMap <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_LevelToPWBLayerMap | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_LevelToPWBLayerMap | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_LevelToPWBLayerMap | None, entto: IGESAppli_LevelToPWBLayerMap | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_LevelToPWBLayerMap | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolLineWidening:
    """
    Tool to work on a LineWidening. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLineWidening, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolLineWidening) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_LineWidening | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_LineWidening | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_LineWidening | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LineWidening <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_LineWidening | None) -> bool:
        """
        Sets automatic unambiguous Correction on a LineWidening
        (NbPropertyValues forced to 5, Level cleared if Subordinate != 0)
        """

    def DirChecker(self, ent: IGESAppli_LineWidening | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_LineWidening | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_LineWidening | None, entto: IGESAppli_LineWidening | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_LineWidening | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolNodalConstraint:
    """
    Tool to work on a NodalConstraint. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNodalConstraint, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolNodalConstraint) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_NodalConstraint | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_NodalConstraint | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_NodalConstraint | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NodalConstraint <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_NodalConstraint | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_NodalConstraint | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_NodalConstraint | None, entto: IGESAppli_NodalConstraint | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_NodalConstraint | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolNodalDisplAndRot:
    """
    Tool to work on a NodalDisplAndRot. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNodalDisplAndRot, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolNodalDisplAndRot) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_NodalDisplAndRot | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_NodalDisplAndRot | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_NodalDisplAndRot | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NodalDisplAndRot <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_NodalDisplAndRot | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_NodalDisplAndRot | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_NodalDisplAndRot | None, entto: IGESAppli_NodalDisplAndRot | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_NodalDisplAndRot | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolNodalResults:
    """
    Tool to work on a NodalResults. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNodalResults, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolNodalResults) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_NodalResults | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_NodalResults | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_NodalResults | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NodalResults <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_NodalResults | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_NodalResults | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_NodalResults | None, entto: IGESAppli_NodalResults | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_NodalResults | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolNode:
    """
    Tool to work on a Node. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNode, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolNode) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_Node | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_Node | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_Node | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Node <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_Node | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_Node | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_Node | None, entto: IGESAppli_Node | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_Node | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolPartNumber:
    """
    Tool to work on a PartNumber. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPartNumber, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolPartNumber) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_PartNumber | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_PartNumber | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_PartNumber | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PartNumber <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_PartNumber | None) -> bool:
        """
        Sets automatic unambiguous Correction on a PartNumber
        (NbPropertyValues forced to 4)
        """

    def DirChecker(self, ent: IGESAppli_PartNumber | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_PartNumber | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_PartNumber | None, entto: IGESAppli_PartNumber | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_PartNumber | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolPinNumber:
    """
    Tool to work on a PinNumber. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPinNumber, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolPinNumber) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_PinNumber | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_PinNumber | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_PinNumber | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PinNumber <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_PinNumber | None) -> bool:
        """
        Sets automatic unambiguous Correction on a PinNumber
        (Level cleared in D.E. if Subordinate != 0)
        """

    def DirChecker(self, ent: IGESAppli_PinNumber | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_PinNumber | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_PinNumber | None, entto: IGESAppli_PinNumber | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_PinNumber | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolPipingFlow:
    """
    Tool to work on a PipingFlow. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPipingFlow, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolPipingFlow) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_PipingFlow | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_PipingFlow | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_PipingFlow | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PipingFlow <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_PipingFlow | None) -> bool:
        """
        Sets automatic unambiguous Correction on a PipingFlow
        (NbContextFlags forced to 1)
        """

    def DirChecker(self, ent: IGESAppli_PipingFlow | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_PipingFlow | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_PipingFlow | None, entto: IGESAppli_PipingFlow | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_PipingFlow | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolPWBArtworkStackup:
    """
    Tool to work on a PWBArtworkStackup. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPWBArtworkStackup, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolPWBArtworkStackup) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_PWBArtworkStackup | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_PWBArtworkStackup | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_PWBArtworkStackup | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PWBArtworkStackup <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESAppli_PWBArtworkStackup | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_PWBArtworkStackup | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_PWBArtworkStackup | None, entto: IGESAppli_PWBArtworkStackup | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_PWBArtworkStackup | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolPWBDrilledHole:
    """
    Tool to work on a PWBDrilledHole. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPWBDrilledHole, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolPWBDrilledHole) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_PWBDrilledHole | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_PWBDrilledHole | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_PWBDrilledHole | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PWBDrilledHole <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_PWBDrilledHole | None) -> bool:
        """
        Sets automatic unambiguous Correction on a PWBDrilledHole
        (NbPropertyValues forced to 3)
        """

    def DirChecker(self, ent: IGESAppli_PWBDrilledHole | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_PWBDrilledHole | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_PWBDrilledHole | None, entto: IGESAppli_PWBDrilledHole | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_PWBDrilledHole | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolReferenceDesignator:
    """
    Tool to work on a ReferenceDesignator. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolReferenceDesignator, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolReferenceDesignator) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_ReferenceDesignator | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_ReferenceDesignator | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_ReferenceDesignator | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ReferenceDesignator <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_ReferenceDesignator | None) -> bool:
        """
        Sets automatic unambiguous Correction on a ReferenceDesignator
        (NbPropertyValues forced to 1, Level cleared if Subordinate != 0)
        """

    def DirChecker(self, ent: IGESAppli_ReferenceDesignator | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_ReferenceDesignator | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_ReferenceDesignator | None, entto: IGESAppli_ReferenceDesignator | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_ReferenceDesignator | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESAppli_ToolRegionRestriction:
    """
    Tool to work on a RegionRestriction. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolRegionRestriction, ready to work"""

    @overload
    def __init__(self, theOther: IGESAppli_ToolRegionRestriction) -> None: ...

    def ReadOwnParams(self, ent: IGESAppli_RegionRestriction | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESAppli_RegionRestriction | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESAppli_RegionRestriction | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a RegionRestriction <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESAppli_RegionRestriction | None) -> bool:
        """
        Sets automatic unambiguous Correction on a RegionRestriction
        (NbPropertyValues forced to 3, Level cleared if Subordinate != 0)
        """

    def DirChecker(self, ent: IGESAppli_RegionRestriction | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESAppli_RegionRestriction | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESAppli_RegionRestriction | None, entto: IGESAppli_RegionRestriction | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESAppli_RegionRestriction | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESAppli
IGESAppli_Array1OfFiniteElement = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESAppli.IGESAppli_FiniteElement]
IGESAppli_Array1OfNode = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESAppli.IGESAppli_Node]
IGESAppli_HArray1OfFiniteElement = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESAppli.IGESAppli_FiniteElement]
IGESAppli_HArray1OfNode = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESAppli.IGESAppli_Node]
