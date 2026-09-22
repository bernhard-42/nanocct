"""OCCT package IGESDefs (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESBasic
import nanoocp.IGESData
import nanoocp.IGESGraph
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class IGESDefs:
    """
    To embody general definitions of Entities
    (Parameters, Tables ...)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESDefs_Protocol:
        """Returns the Protocol for this Package"""

class IGESDefs_AssociativityDef(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Associativity Definition Entity, Type <302>
    Form <5001 - 9999> in package IGESDefs.
    This class permits the preprocessor to define an
    associativity schema. i.e., by using it preprocessor
    defines the type of relationship.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_AssociativityDef) -> None: ...

    def Init(self, requirements: nanoocp.NCollection.NCollection_HArray1[int] | None, orders: nanoocp.NCollection.NCollection_HArray1[int] | None, numItems: nanoocp.NCollection.NCollection_HArray1[int] | None, items: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger | None) -> None:
        """
        This method is used to set the fields of the class
        AssociativityDef
        - requirements : Back Pointers requirements
        - orders       : Class Orders
        - numItems     : Number of Items per Class
        - items        : Items in each class
        raises exception if lengths of the arrays are not the same.
        """

    def SetFormNumber(self, form: int) -> None: ...

    def NbClassDefs(self) -> int:
        """returns the Number of class definitions"""

    def IsBackPointerReq(self, ClassNum: int) -> bool:
        """
        returns 1 if the theBackPointerReqs(ClassNum) = 1
        returns 0 if the theBackPointerReqs(ClassNum) = 2
        raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """

    def BackPointerReq(self, ClassNum: int) -> int:
        """
        returns 1 or 2
        raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """

    def IsOrdered(self, ClassNum: int) -> bool:
        """
        returns 1 if theClassOrders(ClassNum) = 1 (ordered class)
        returns 0 if theClassOrders(ClassNum) = 2 (unordered class)
        raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """

    def ClassOrder(self, ClassNum: int) -> int:
        """
        returns 1 or 2
        raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """

    def NbItemsPerClass(self, ClassNum: int) -> int:
        """
        returns no. of items per class entry
        raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """

    def Item(self, ClassNum: int, ItemNum: int) -> int:
        """
        returns ItemNum'th Item of ClassNum'th Class
        raises exception if
        ClassNum <= 0 or ClassNum > NbClassDefs()
        ItemNum <= 0 or ItemNum > NbItemsPerClass(ClassNum)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_AttributeDef(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Attribute Table Definition Entity,
    Type <322> Form [0, 1, 2] in package IGESDefs.
    This is class is used to support the concept of well
    defined collection of attributes, whether it is a table
    or a single row of attributes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_AttributeDef) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aListType: int, attrTypes: nanoocp.NCollection.NCollection_HArray1[int] | None, attrValueDataTypes: nanoocp.NCollection.NCollection_HArray1[int] | None, attrValueCounts: nanoocp.NCollection.NCollection_HArray1[int] | None, attrValues: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None, attrValuePointers: IGESDefs_HArray1OfHArray1OfTextDisplayTemplate | None) -> None: ...

    def HasTableName(self) -> bool:
        """Returns True if a Table Name is defined"""

    def TableName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns the Attribute Table name, or comment
        (default = null, no name : seeHasTableName)
        """

    def ListType(self) -> int:
        """returns the Attribute List Type"""

    def NbAttributes(self) -> int:
        """returns the Number of Attributes"""

    def AttributeType(self, num: int) -> int:
        """
        returns the num'th Attribute Type
        raises exception if num <= 0 or num > NbAttributes()
        """

    def AttributeValueDataType(self, num: int) -> int:
        """
        returns the num'th Attribute value data type
        raises exception if num <= 0 or num > NbAttributes()
        """

    def AttributeValueCount(self, num: int) -> int:
        """
        returns the num'th Attribute value count
        raises exception if num <= 0 or num > NbAttributes()
        """

    def HasValues(self) -> bool:
        """returns false if Values are defined (i.e. for Form = 1 or 2)"""

    def HasTextDisplay(self) -> bool:
        """returns false if TextDisplays are defined (i.e. for Form = 2)"""

    def AttributeTextDisplay(self, AttrNum: int, PointerNum: int) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate: ...

    def AttributeList(self, AttrNum: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the List of Attributes <AttrNum>, as a Transient.
        Its effective Type depends of the Type of Attribute :
        HArray1OfInteger for Integer, Logical(0-1),
        HArray1OfReal for Real, HArray1OfHSaciiString for String,
        HArray1OfIGESEntity for Entity (Pointer)
        See methods AttributeAs... for an accurate access
        """

    def AttributeAsInteger(self, AttrNum: int, ValueNum: int) -> int:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Integer
        Error if Indices out of Range, or no Value defined, or not an Integer
        """

    def AttributeAsReal(self, AttrNum: int, ValueNum: int) -> float:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Real
        Error if Indices out of Range, or no Value defined, or not a Real
        """

    def AttributeAsString(self, AttrNum: int, ValueNum: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns Attribute Value <AttrNum, rank ValueNum> as an Integer"""

    def AttributeAsEntity(self, AttrNum: int, ValueNum: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Entity
        Error if Indices out of Range, or no Value defined, or not a Entity
        """

    def AttributeAsLogical(self, AttrNum: int, ValueNum: int) -> bool:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Boolean
        Error if Indices out of Range, or no Value defined, or not a Logical
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_AttributeTable(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Attribute Table, Type <422> Form <0, 1>
    in package IGESDefs
    This class is used to represent an occurrence of
    Attribute Table. This Class may be independent
    or dependent or pointed at by other Entities.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_AttributeTable) -> None: ...

    def Init(self, attributes: nanoocp.NCollection.NCollection_HArray2[nanoocp.Standard.Standard_Transient] | None) -> None:
        """
        This method is used to set the fields of the class
        AttributeTable
        - attributes : Attribute instances, created as
        (1,NbAttributes,1,NbRows)
        - NbRows = 1 is a particular case (Form 0)
        """

    def SetDefinition(self, def_: IGESDefs_AttributeDef | None) -> None:
        """
        Sets a Definition as Structure information
        (works by calling InitMisc)
        """

    def Definition(self) -> IGESDefs_AttributeDef:
        """
        Return the Structure information in Directory Entry,
        casted as an AttributeDef
        """

    def NbRows(self) -> int:
        """
        returns Number of Rows. Remark that it is always 1 if Form = 0
        It means that the list of Attributes (by their number, and for each
        one its type and ValueCount) is repeated <NbRows> times
        """

    def NbAttributes(self) -> int:
        """returns Number of Attributes"""

    def DataType(self, Atnum: int) -> int:
        """
        returns the Type of an Attribute, given its No. : it is read in the
        Definition.
        (1 : Integer, 2 : Real, 3 : String, 4 : Entity, 6 : Logical)
        """

    def ValueCount(self, Atnum: int) -> int:
        """
        returns the Count of Value for an Attribute, given its No. :
        it is read in the Definition.
        """

    def AttributeList(self, Attribnum: int, Rownum: int) -> nanoocp.Standard.Standard_Transient: ...

    def AttributeAsInteger(self, AtNum: int, Rownum: int, ValNum: int) -> int:
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as an Integer
        Error if Indices out of Range, or no Value defined, or not an Integer
        """

    def AttributeAsReal(self, AtNum: int, Rownum: int, ValNum: int) -> float:
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as a Real
        Error if Indices out of Range, or no Value defined, or not a Real
        """

    def AttributeAsString(self, AtNum: int, Rownum: int, ValNum: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns Attribute Value <AtNum, Rownum, rank ValNum> as an Integer"""

    def AttributeAsEntity(self, AtNum: int, Rownum: int, ValNum: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as an Entity
        Error if Indices out of Range, or no Value defined, or not an Entity
        """

    def AttributeAsLogical(self, AtNum: int, Rownum: int, ValNum: int) -> bool:
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as a Boolean
        Error if Indices out of Range, or no Value defined, or not a Logical
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESDefs (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESDefs and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESDefs_GeneralModule) -> None: ...

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
        Auxiliary for all
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_GenericData(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Generic Data, Type <406> Form <27>
    in package IGESDefs
    Used to communicate information defined by the system
    operator while creating the model. The information is
    system specific and does not map into one of the
    predefined properties or associativities. Properties
    and property values can be defined by multiple
    instances of this property.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_GenericData) -> None: ...

    def Init(self, nbPropVal: int, aName: nanoocp.TCollection.TCollection_HAsciiString | None, allTypes: nanoocp.NCollection.NCollection_HArray1[int] | None, allValues: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """
        This method is used to set the fields of the class
        GenericData
        - nbPropVal : Number of property values
        - aName     : Property Name
        - allTypes  : Property Types
        - allValues : Property Values
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns property name"""

    def NbTypeValuePairs(self) -> int:
        """returns the number of TYPE/VALUE pairs"""

    def Type(self, Index: int) -> int:
        """
        returns the Index'th property value data type
        raises exception if Index <= 0 or Index > NbTypeValuePairs()
        """

    def Value(self, Index: int) -> nanoocp.Standard.Standard_Transient:
        """
        HArray1OfInteger (length 1), HArray1OfReal (length 1) for
        Integer, Real, Boolean (= Integer 0/1),
        HAsciiString for String (the value itself),
        IGESEntity for Entity (the value itself)
        """

    def ValueAsInteger(self, ValueNum: int) -> int:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Integer
        Error if Index out of Range, or not an Integer
        """

    def ValueAsReal(self, ValueNum: int) -> float:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Real
        Error if Index out of Range, or not a Real
        """

    def ValueAsString(self, ValueNum: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns Attribute Value <AttrNum, rank ValueNum> as an Integer"""

    def ValueAsEntity(self, ValueNum: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Entity
        Error if Index out of Range, or not a Entity
        """

    def ValueAsLogical(self, ValueNum: int) -> bool:
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Boolean
        Error if Index out of Range, or not a Logical
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_HArray1OfHArray1OfTextDisplayTemplate(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, low: int, up: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_HArray1OfHArray1OfTextDisplayTemplate) -> None: ...

    def Lower(self) -> int: ...

    def Upper(self) -> int: ...

    def Length(self) -> int: ...

    def SetValue(self, num: int, val: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate] | None) -> None: ...

    def Value(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_MacroDef(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Macro Definition Entity, Type <306> Form <0>
    in package IGESDefs
    This Class specifies the action of a specific MACRO.
    After specification MACRO can be used as necessary
    by means of MACRO class instance entity.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_MacroDef) -> None: ...

    def Init(self, macro: nanoocp.TCollection.TCollection_HAsciiString | None, entityTypeID: int, langStatements: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, endMacro: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        MacroDef
        - macro          : MACRO
        - entityTypeID   : Entity Type ID
        - langStatements : Language Statements
        - endMacro       : END MACRO
        """

    def NbStatements(self) -> int:
        """returns the number of language statements"""

    def MACRO(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the MACRO(Literal)"""

    def EntityTypeID(self) -> int:
        """returns the Entity Type ID"""

    def LanguageStatement(self, StatNum: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def ENDMACRO(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the ENDM(Literal)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESDefs"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, one
        (Protocol from IGESGraph)
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

class IGESDefs_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines Defs File Access Module for IGESDefs (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESDefs_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESDefs"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESDefs"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """Defines Services attached to IGES Entities : Dump, for IGESDefs"""

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESDefs & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESDefs_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESDefs"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_TabularData(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Tabular Data, Type <406> Form <11>,
    in package IGESDefs
    This Class is used to provide a Structure to accommodate
    point form data.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_TabularData) -> None: ...

    def Init(self, nbProps: int, propType: int, typesInd: nanoocp.NCollection.NCollection_HArray1[int] | None, nbValuesInd: nanoocp.NCollection.NCollection_HArray1[int] | None, valuesInd: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfReal | None, valuesDep: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfReal | None) -> None:
        """
        This method is used to set the fields of the class
        TabularData
        - nbProps     : Number of property values
        - propType    : Property Type
        - typesInd    : Type of independent variables
        - nbValuesInd : Number of values of independent variables
        - valuesInd   : Values of independent variables
        - valuesDep   : Values of dependent variables
        raises exception if lengths of typeInd and nbValuesInd are not same
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values (recorded)"""

    def ComputedNbPropertyValues(self) -> int:
        """determines the number of property values required"""

    def OwnCorrect(self) -> bool:
        """
        checks, and correct as necessary, the number of property
        values. Returns True if corrected, False if already OK
        """

    def PropertyType(self) -> int:
        """returns the property type"""

    def NbDependents(self) -> int:
        """returns the number of dependent variables"""

    def NbIndependents(self) -> int:
        """returns the number of independent variables"""

    def TypeOfIndependents(self, num: int) -> int:
        """
        returns the type of the num'th independent variable
        raises exception if num <= 0 or num > NbIndependents()
        """

    def NbValues(self, num: int) -> int:
        """
        returns the number of different values of the num'th indep. variable
        raises exception if num <= 0 or num > NbIndependents()
        """

    def IndependentValue(self, variablenum: int, valuenum: int) -> float: ...

    def DependentValues(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def DependentValue(self, variablenum: int, valuenum: int) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDefs_ToolAssociativityDef:
    """
    Tool to work on a AssociativityDef. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolAssociativityDef, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolAssociativityDef) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_AssociativityDef | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_AssociativityDef | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_AssociativityDef | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a AssociativityDef <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_AssociativityDef | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_AssociativityDef | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_AssociativityDef | None, entto: IGESDefs_AssociativityDef | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_AssociativityDef | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_ToolAttributeDef:
    """
    Tool to work on a AttributeDef. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolAttributeDef, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolAttributeDef) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_AttributeDef | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_AttributeDef | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_AttributeDef | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a AttributeDef <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_AttributeDef | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_AttributeDef | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_AttributeDef | None, entto: IGESDefs_AttributeDef | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_AttributeDef | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_ToolAttributeTable:
    """
    Tool to work on a AttributeTable. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolAttributeTable, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolAttributeTable) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_AttributeTable | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_AttributeTable | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_AttributeTable | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a AttributeTable <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_AttributeTable | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_AttributeTable | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_AttributeTable | None, entto: IGESDefs_AttributeTable | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_AttributeTable | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_ToolGenericData:
    """
    Tool to work on a GenericData. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolGenericData, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolGenericData) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_GenericData | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_GenericData | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_GenericData | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a GenericData <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_GenericData | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_GenericData | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_GenericData | None, entto: IGESDefs_GenericData | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_GenericData | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_ToolMacroDef:
    """
    Tool to work on a MacroDef. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolMacroDef, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolMacroDef) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_MacroDef | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_MacroDef | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_MacroDef | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a MacroDef <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_MacroDef | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_MacroDef | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_MacroDef | None, entto: IGESDefs_MacroDef | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_MacroDef | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_ToolTabularData:
    """
    Tool to work on a TabularData. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTabularData, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolTabularData) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_TabularData | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_TabularData | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_TabularData | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a TabularData <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_TabularData | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_TabularData | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_TabularData | None, entto: IGESDefs_TabularData | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_TabularData | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_ToolUnitsData:
    """
    Tool to work on a UnitsData. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolUnitsData, ready to work"""

    @overload
    def __init__(self, theOther: IGESDefs_ToolUnitsData) -> None: ...

    def ReadOwnParams(self, ent: IGESDefs_UnitsData | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDefs_UnitsData | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDefs_UnitsData | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a UnitsData <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDefs_UnitsData | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDefs_UnitsData | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDefs_UnitsData | None, entto: IGESDefs_UnitsData | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDefs_UnitsData | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDefs_UnitsData(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES UnitsData Entity, Type <316> Form <0>
    in package IGESDefs
    This class stores data about a model's fundamental units.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDefs_UnitsData) -> None: ...

    def Init(self, unitTypes: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, unitValues: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, unitScales: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """
        This method is used to set the fields of the class
        UnitsData
        - unitTypes  : Types of the units being defined
        - unitValues : Unit Values of the units
        - unitScales : Multiplicative Scale Factors
        raises exception if lengths of unitTypes, unitValues and
        unitScale are not same
        """

    def NbUnits(self) -> int:
        """returns the Number of units defined by this entity"""

    def UnitType(self, UnitNum: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns the Type of the UnitNum'th unit being defined
        raises exception if UnitNum <= 0 or UnitNum > NbUnits()
        """

    def UnitValue(self, UnitNum: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns the Units of the UnitNum'th unit being defined
        raises exception if UnitNum <= 0 or UnitNum > NbUnits()
        """

    def ScaleFactor(self, UnitNum: int) -> float:
        """
        returns the multiplicative scale factor to be applied to the
        UnitNum'th unit being defined
        raises exception if UnitNum <= 0 or UnitNum > NbUnits()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESDefs
IGESDefs_Array1OfTabularData = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESDefs.IGESDefs_TabularData]
IGESDefs_HArray1OfTabularData = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDefs.IGESDefs_TabularData]
