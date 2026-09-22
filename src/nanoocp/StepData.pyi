"""OCCT package StepData (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.DESTEP
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Resource
import nanoocp.Standard
import nanoocp.TCollection


class StepData_Logical(enum.IntEnum):
    """A Standard Definition for STEP (which knows Boolean too)"""

    StepData_LFalse = 0

    StepData_LTrue = 1

    StepData_LUnknown = 2

StepData_LFalse: StepData_Logical = StepData_Logical.StepData_LFalse

StepData_LTrue: StepData_Logical = StepData_Logical.StepData_LTrue

StepData_LUnknown: StepData_Logical = StepData_Logical.StepData_LUnknown

class StepData:
    """
    Gives basic data definition for Step Interface.
    Any class of a data model described in EXPRESS Language
    is candidate to be managed by a Step Interface
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData) -> None: ...

    @staticmethod
    def HeaderProtocol() -> StepData_Protocol:
        """
        Returns the recorded HeaderProtocol, which can be :
        - a Null Handle if no Header Protocol was yet defined
        - a simple Protocol if only one was defined
        - a FileProtocol if more than one Protocol was yet defined
        """

    @staticmethod
    def AddHeaderProtocol(headerproto: StepData_Protocol | None) -> None:
        """Adds a new Header Protocol to the Header Definition"""

    @staticmethod
    def Init() -> None:
        """
        Prepares General Data required to work with this package,
        which are the Protocol and Modules to be loaded into Libraries
        """

    @staticmethod
    def Protocol() -> StepData_Protocol:
        """Returns a Protocol from StepData (avoids to create it)"""

class StepData_GeneralModule(nanoocp.Interface.Interface_GeneralModule):
    """Specific features for General Services adapted to STEP"""

    def FillSharedCase(self, casenum: int, ent: nanoocp.Standard.Standard_Transient | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Specific filling of the list of Entities shared by an Entity
        <ent>. Can use the internal utility method Share, below
        """

    def CheckCase(self, casenum: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Specific Checking of an Entity <ent>"""

    def CopyCase(self, casenum: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type)
        by using a TransferControl which provides its working Map.
        Use method Transferred from TransferControl to work
        Specific Copying of Implied References
        A Default is provided which does nothing (must current case !)
        Already copied references (by CopyFrom) must remain unchanged
        Use method Search from TransferControl to work
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_DefaultGeneral(StepData_GeneralModule):
    """
    DefaultGeneral defines a GeneralModule which processes
    Unknown Entity from StepData only
    """

    @overload
    def __init__(self) -> None:
        """Creates a Default General Module"""

    @overload
    def __init__(self, theOther: StepData_DefaultGeneral) -> None: ...

    def FillSharedCase(self, casenum: int, ent: nanoocp.Standard.Standard_Transient | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Specific filling of the list of Entities shared by an Entity
        <ent>, which is an UnknownEntity from StepData.
        """

    def CheckCase(self, casenum: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Specific Checking of an Entity <ent>"""

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """Specific creation of a new void entity"""

    def CopyCase(self, casenum: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type)
        by using a CopyTool which provides its working Map.
        Use method Transferred from TransferControl to work
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_Described(nanoocp.Standard.Standard_Transient):
    """
    General frame to describe entities with Description (Simple or
    Complex)
    """

    def Description(self) -> StepData_EDescr:
        """Returns the Description used to define this entity"""

    def IsComplex(self) -> bool:
        """Tells if a described entity is complex"""

    def Matches(self, steptype: str) -> bool:
        """
        Tells if a step type is matched by <me>
        For a Simple Entity : own type or super type
        For a Complex Entity : one of the members
        """

    def As(self, steptype: str) -> StepData_Simple:
        """
        Returns a Simple Entity which matches with a Type in <me> :
        For a Simple Entity : me if it matches, else a null handle
        For a Complex Entity : the member which matches, else null
        """

    def HasField(self, name: str) -> bool:
        """Tells if a Field brings a given name"""

    def Field(self, name: str) -> StepData_Field:
        """Returns a Field from its name; read-only"""

    def CField(self, name: str) -> StepData_Field:
        """Returns a Field from its name; read or write"""

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """Fills a Check by using its Description"""

    def Shared(self, list: nanoocp.Interface.Interface_EntityIterator) -> None:
        """Fills an EntityIterator with entities shared by <me>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_EDescr(nanoocp.Standard.Standard_Transient):
    """
    This class is intended to describe the authorized form for an
    entity, either Simple or Plex
    """

    def Matches(self, steptype: str) -> bool:
        """Tells if a ESDescr matches a step type : exact or super type"""

    def IsComplex(self) -> bool:
        """Tells if a EDescr is complex (ECDescr) or simple (ESDescr)"""

    def NewEntity(self) -> StepData_Described:
        """Creates a described entity (i.e. a simple one)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_ECDescr(StepData_EDescr):
    """Describes a Complex Entity (Plex) as a list of Simple ones"""

    @overload
    def __init__(self) -> None:
        """Creates an ECDescr, empty"""

    @overload
    def __init__(self, theOther: StepData_ECDescr) -> None: ...

    def Add(self, member: StepData_ESDescr | None) -> None:
        """
        Adds a member
        Warning : members are added in alphabetic order
        """

    def NbMembers(self) -> int:
        """Returns the count of members"""

    def Member(self, num: int) -> StepData_ESDescr:
        """Returns a Member from its rank"""

    def TypeList(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]:
        """Returns the ordered list of types"""

    def Matches(self, steptype: str) -> bool:
        """Tells if a ESDescr matches a step type : exact or super type"""

    def IsComplex(self) -> bool:
        """Returns True"""

    def NewEntity(self) -> StepData_Described:
        """
        Creates a described entity (i.e. a complex one, made of one
        simple entity per member)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_EnumTool:
    """
    This class gives a way of conversion between the value of an
    enumeration and its representation in STEP
    An enumeration corresponds to an integer with reserved values,
    which begin to 0
    In STEP, it is represented by a name in capital letter and
    limited by two dots, e.g. .UNKNOWN.

    EnumTool works with integers, it is just required to cast
    between an integer and an enumeration of required type.

    Its definition is intended to allow static creation in once,
    without having to recreate once for each use.

    It is possible to define subclasses on it, which directly give
    the good list of definition texts, and accepts a enumeration
    of the good type instead of an integer
    """

    @overload
    def __init__(self, e0: str = '', e1: str = '', e2: str = '', e3: str = '', e4: str = '', e5: str = '', e6: str = '', e7: str = '', e8: str = '', e9: str = '', e10: str = '', e11: str = '', e12: str = '', e13: str = '', e14: str = '', e15: str = '', e16: str = '', e17: str = '', e18: str = '', e19: str = '', e20: str = '', e21: str = '', e22: str = '', e23: str = '', e24: str = '', e25: str = '', e26: str = '', e27: str = '', e28: str = '', e29: str = '', e30: str = '', e31: str = '', e32: str = '', e33: str = '', e34: str = '', e35: str = '', e36: str = '', e37: str = '', e38: str = '', e39: str = '') -> None:
        """
        Creates an EnumTool with definitions given by e0 .. e<max>
        Each definition string can bring one term, or several
        separated by blanks. Each term corresponds to one value of the
        enumeration, if dots are not presents they are added

        Such a static constructor allows to build a static description
        as : static StepData_EnumTool myenumtool("e0","e1"...);
        then use it without having to initialise it

        A null definition can be input by given "$" :the corresponding
        position is attached to "null/undefined" value (as one
        particular item of the enumeration list)
        """

    @overload
    def __init__(self, theOther: StepData_EnumTool) -> None: ...

    def AddDefinition(self, term: str) -> None:
        """
        Processes a definition, splits it according blanks if any
        empty definitions are ignored
        A null definition can be input by given "$" :the corresponding
        position is attached to "null/undefined" value (as one
        particular item of the enumeration list)
        See also IsSet
        """

    def IsSet(self) -> bool:
        """
        Returns True if at least one definition has been entered after
        creation time (i.e. by AddDefinition only)

        This allows to build a static description by a first pass :
        static StepData_EnumTool myenumtool("e0" ...);
        ...
        if (!myenumtool.IsSet()) {             for further inits
        myenumtool.AddDefinition("e21");
        ...
        }
        """

    def MaxValue(self) -> int:
        """
        Returns the maximum integer for a suitable value
        Remark : while values begin at zero, MaxValue is the count of
        recorded values minus one
        """

    def Optional(self, mode: bool) -> None:
        """
        Sets or Unsets the EnumTool to accept undefined value (for
        optional field). Ignored if no null value is defined (by "$")
        Can be changed during execution (to read each field),
        Default is True (if a null value is defined)
        """

    def NullValue(self) -> int:
        """
        Returns the value attached to "null/undefined value"
        If none is specified or if Optional has been set to False,
        returns -1
        Null Value has been specified by definition "$\"
        """

    def Text(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the text which corresponds to a given numeric value
        It is limited by dots
        If num is out of range, returns an empty string
        """

    @overload
    def Value(self, txt: str) -> int:
        """
        Returns the numeric value found for a text
        The text must be in capitals and limited by dots
        A non-suitable text gives a negative value to be returned
        """

    @overload
    def Value(self, txt: nanoocp.TCollection.TCollection_AsciiString) -> int:
        """Same as above but works on an AsciiString"""

class StepData_ESDescr(StepData_EDescr):
    """
    This class is intended to describe the authorized form for a
    Simple (not Plex) Entity, as a list of fields
    """

    @overload
    def __init__(self, name: str) -> None:
        """Creates an ESDescr with a type name"""

    @overload
    def __init__(self, theOther: StepData_ESDescr) -> None: ...

    def SetNbFields(self, nb: int) -> None:
        """
        Sets a new count of fields
        Each one is described by a PDescr
        """

    def SetField(self, num: int, name: str, descr: StepData_PDescr | None) -> None:
        """
        Sets a PDescr to describe a field
        A Field is designated by its rank and name
        """

    def SetBase(self, base: StepData_ESDescr | None) -> None:
        """
        Sets an ESDescr as based on another one
        Hence, if there are inherited fields, the derived ESDescr
        cumulates all them, while the base just records its own ones
        """

    def SetSuper(self, super: StepData_ESDescr | None) -> None:
        """
        Sets an ESDescr as "super-type". Applies an a base (non
        derived) ESDescr
        """

    def TypeName(self) -> str:
        """Returns the type name given at creation time"""

    def StepType(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the type name as an AsciiString"""

    def Base(self) -> StepData_ESDescr:
        """Returns the basic ESDescr, null if <me> is not derived"""

    def Super(self) -> StepData_ESDescr:
        """Returns the super-type ESDescr, null if <me> is root"""

    def IsSub(self, other: StepData_ESDescr | None) -> bool:
        """Tells if <me> is sub-type of (or equal to) another one"""

    def NbFields(self) -> int:
        """Returns the count of fields"""

    def Rank(self, name: str) -> int:
        """Returns the rank of a field from its name. 0 if unknown"""

    def Name(self, num: int) -> str:
        """Returns the name of a field from its rank. empty if outofrange"""

    def Field(self, num: int) -> StepData_PDescr:
        """Returns the PDescr for the field <num> (or Null)"""

    def NamedField(self, name: str) -> StepData_PDescr:
        """Returns the PDescr for the field named <name> (or Null)"""

    def Matches(self, steptype: str) -> bool:
        """Tells if a ESDescr matches a step type : exact or super type"""

    def IsComplex(self) -> bool:
        """Returns False"""

    def NewEntity(self) -> StepData_Described:
        """Creates a described entity (i.e. a simple one)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_Factors:
    """Class for using units variables"""

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: StepData_Factors) -> None: ...

    def InitializeFactors(self, theLengthFactor: float, thePlaneAngleFactor: float, theSolidAngleFactor: float) -> None:
        """Initializes the 3 factors for the conversion of units"""

    def SetCascadeUnit(self, theUnit: float) -> None:
        """Sets length unit for current transfer process"""

    def CascadeUnit(self) -> float:
        """Returns length unit for current transfer process (mm by default)"""

    def LengthFactor(self) -> float:
        """
        Returns transient length factor for scaling of shapes
        at one stage of transfer process
        """

    def PlaneAngleFactor(self) -> float:
        """
        Returns transient plane angle factor for conversion of angles
        at one stage of transfer process
        """

    def SolidAngleFactor(self) -> float:
        """
        Returns transient solid angle factor for conversion of angles
        at one stage of transfer process
        """

    def FactorRadianDegree(self) -> float:
        """
        Returns transient factor radian degree for conversion of angles
        at one stage of transfer process
        """

    def FactorDegreeRadian(self) -> float:
        """
        Returns transient factor degree radian for conversion of angles
        at one stage of transfer process
        """

class StepData_Field:
    """
    Defines a generally defined Field for STEP data : can be used
    either in any kind of entity to implement it or in free format
    entities in a "late-binding" mode
    A field can have : no value (or derived), a single value of
    any kind, a list of value : single or double list

    When a field is set, this defines its new kind (Integer etc..)
    A single value is immediately set. A list of value is, firstly
    declared as for a kind (Integer String etc), then declared as
    a list with its initial size, after this its items are set
    Also it can be set in once if the HArray is ready
    """

    @overload
    def __init__(self) -> None:
        """Creates a Field, empty ("no value defined")"""

    @overload
    def __init__(self, other: StepData_Field, copy: bool = False) -> None:
        """
        Creates a Field from another one. If <copy> is True, Handled
        data (Select,String,List, not entities) are copied
        """

    def CopyFrom(self, other: StepData_Field) -> None:
        """Gets the copy of the values of another field"""

    def Clear(self, kind: int = 0) -> None:
        """
        Clears the field, to set it as "no value defined"
        Just before SetList, predeclares it as "any"
        A Kind can be directly set here to declare a type
        """

    def SetDerived(self) -> None:
        """Codes a Field as derived (no proper value)"""

    @overload
    def SetInt(self, val: int) -> None:
        """
        Directly sets the Integer value, if its Kind matches
        Integer, Boolean, Logical, or Enum (does not change Kind)
        """

    @overload
    def SetInt(self, num: int, val: int, kind: int) -> None:
        """Internal access to an Integer Value for a list, plus its kind"""

    @overload
    def SetInteger(self, val: int = 0) -> None:
        """Sets an Integer value (before SetList* declares it as Integer)"""

    @overload
    def SetInteger(self, num: int, val: int) -> None:
        """
        Sets an Integer Value for a list (rank num)
        (recognizes a SelectMember)
        """

    @overload
    def SetBoolean(self, val: bool = False) -> None:
        """Sets a Boolean value (or predeclares a list as boolean)"""

    @overload
    def SetBoolean(self, num: int, val: bool) -> None: ...

    @overload
    def SetLogical(self, val: StepData_Logical = StepData_Logical.StepData_LFalse) -> None:
        """Sets a Logical Value (or predeclares a list as logical)"""

    @overload
    def SetLogical(self, num: int, val: StepData_Logical) -> None: ...

    @overload
    def SetReal(self, val: float = 0.0) -> None:
        """Sets a Real Value (or predeclares a list as Real);"""

    @overload
    def SetReal(self, num: int, val: float) -> None: ...

    @overload
    def SetString(self, val: str = '') -> None:
        """
        Sets a String Value (or predeclares a list as String)
        Does not redefine the Kind if it is already String or Enum
        """

    @overload
    def SetString(self, num: int, val: str) -> None: ...

    @overload
    def SetEnum(self, val: int = -1, text: str = '') -> None:
        """
        Sets an Enum Value (as its integer counterpart)
        (or predeclares a list as Enum)
        If <text> is given , also sets its textual expression
        <val> negative means unknown (known values begin at 0)
        """

    @overload
    def SetEnum(self, num: int, val: int, text: str = '') -> None:
        """
        Sets an Enum Value (Integer counterpart), also its text
        expression if known (if list has been set as "any")
        """

    def SetSelectMember(self, val: StepData_SelectMember | None) -> None:
        """
        Sets a SelectMember (for Integer,Boolean,Enum,Real,Logical)
        Hence, the value of the field is accessed through this member
        """

    @overload
    def SetEntity(self, val: nanoocp.Standard.Standard_Transient | None) -> None:
        """Sets an Entity Value"""

    @overload
    def SetEntity(self) -> None:
        """Predeclares a list as of entity"""

    @overload
    def SetEntity(self, num: int, val: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetList(self, size: int, first: int = 1) -> None:
        """
        Declares a field as a list, with an initial size
        Initial lower is defaulted as 1, can be defined
        The list starts empty, typed by the last Set*
        If no Set* before, sets it as "any" (transient/select)
        """

    def SetList2(self, siz1: int, siz2: int, f1: int = 1, f2: int = 1) -> None:
        """
        Declares a field as an homogeneous square list, with initial
        sizes, and initial lowers
        """

    def Set(self, val: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Sets an undetermined value : can be String, SelectMember,
        HArray(1-2) ... else, an Entity
        In case of an HArray, determines and records its size(s)
        """

    def ClearItem(self, num: int) -> None:
        """
        Declares an item of the list as undefined
        (ignored if list not defined as String,Entity or Any)
        """

    def IsSet(self, n1: int = 1, n2: int = 1) -> bool: ...

    def ItemKind(self, n1: int = 1, n2: int = 1) -> int:
        """
        Returns the kind of an item in a list or double list
        It is the kind of the list, except if it is "Any", in such a
        case the true kind is determined and returned
        """

    def Kind(self, type: bool = True) -> int:
        """
        Returns the kind of the field
        <type> True (D) : returns only the type itself
        else, returns the complete kind
        """

    def Arity(self) -> int: ...

    def Length(self, index: int = 1) -> int: ...

    def Lower(self, index: int = 1) -> int: ...

    def Int(self) -> int: ...

    def Integer(self, n1: int = 1, n2: int = 1) -> int: ...

    def Boolean(self, n1: int = 1, n2: int = 1) -> bool: ...

    def Logical(self, n1: int = 1, n2: int = 1) -> StepData_Logical: ...

    def Real(self, n1: int = 1, n2: int = 1) -> float: ...

    def String(self, n1: int = 1, n2: int = 1) -> str: ...

    def Enum(self, n1: int = 1, n2: int = 1) -> int: ...

    def EnumText(self, n1: int = 1, n2: int = 1) -> str: ...

    def Entity(self, n1: int = 1, n2: int = 1) -> nanoocp.Standard.Standard_Transient: ...

    def Transient(self) -> nanoocp.Standard.Standard_Transient: ...

class StepData_FieldList:
    """
    Describes a list of fields, in a general way
    This basic class is for a null size list
    Subclasses are for 1, N (fixed) or Dynamic sizes
    """

    @overload
    def __init__(self) -> None:
        """Creates a FieldList of 0 Field"""

    @overload
    def __init__(self, theOther: StepData_FieldList) -> None: ...

    def NbFields(self) -> int:
        """Returns the count of fields. Here, returns 0"""

    def Field(self, num: int) -> StepData_Field:
        """Returns the field n0 <num> between 1 and NbFields (read only)"""

    def CField(self, num: int) -> StepData_Field:
        """
        Returns the field n0 <num> between 1 and NbFields, in order to
        modify its content
        """

    def FillShared(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """Fills an iterator with the entities shared by <me>"""

class StepData_FieldList1(StepData_FieldList):
    """Describes a list of ONE field"""

    @overload
    def __init__(self) -> None:
        """Creates a FieldList of 1 Field"""

    @overload
    def __init__(self, theOther: StepData_FieldList1) -> None: ...

    def NbFields(self) -> int:
        """Returns the count of fields. Here, returns 1"""

    def Field(self, num: int) -> StepData_Field:
        """Returns the field n0 <num> between 1 and NbFields (read only)"""

    def CField(self, num: int) -> StepData_Field:
        """
        Returns the field n0 <num> between 1 and NbFields, in order to
        modify its content
        """

class StepData_FieldListD(StepData_FieldList):
    """
    Describes a list of fields, in a general way
    This basic class is for a null size list
    Subclasses are for 1, N (fixed) or Dynamic sizes
    """

    @overload
    def __init__(self, nb: int) -> None:
        """Creates a FieldListD of <nb> Fields"""

    @overload
    def __init__(self, theOther: StepData_FieldListD) -> None: ...

    def SetNb(self, nb: int) -> None:
        """Sets a new count of Fields. Former contents are lost"""

    def NbFields(self) -> int:
        """Returns the count of fields. Here, returns starting <nb>"""

    def Field(self, num: int) -> StepData_Field:
        """Returns the field n0 <num> between 1 and NbFields (read only)"""

    def CField(self, num: int) -> StepData_Field:
        """
        Returns the field n0 <num> between 1 and NbFields, in order to
        modify its content
        """

class StepData_FieldListN(StepData_FieldList):
    """
    Describes a list of fields, in a general way
    This basic class is for a null size list
    Subclasses are for 1, N (fixed) or Dynamic sizes
    """

    @overload
    def __init__(self, nb: int) -> None:
        """Creates a FieldListN of <nb> Fields"""

    @overload
    def __init__(self, theOther: StepData_FieldListN) -> None: ...

    def NbFields(self) -> int:
        """Returns the count of fields. Here, returns starting <nb>"""

    def Field(self, num: int) -> StepData_Field:
        """Returns the field n0 <num> between 1 and NbFields (read only)"""

    def CField(self, num: int) -> StepData_Field:
        """
        Returns the field n0 <num> between 1 and NbFields, in order to
        modify its content
        """

class StepData_Protocol(nanoocp.Interface.Interface_Protocol):
    """
    Description of Basic Protocol for Step
    The class Protocol from StepData itself describes a default
    Protocol, which recognizes only UnknownEntities.
    Sub-classes will redefine CaseNumber and, if necessary,
    NbResources and Resources.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Protocols used as Resource (can be zero)
        Here, No resource
        """

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank. Here, none"""

    def CaseNumber(self, obj: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns a unique positive number for any recognized entity
        Redefined to work by calling both TypeNumber and, for a
        Described Entity (late binding) DescrNumber
        """

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a Case Number, specific of each recognized Type
        Here, only Unknown Entity is recognized
        """

    def SchemaName(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Schema Name attached to each class of Protocol
        To be redefined by each sub-class
        Here, SchemaName returns "(DEFAULT)"
        was C++ : return const
        """

    def NewModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Creates an empty Model for Step Norm"""

    def IsSuitableModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns True if <model> is a Model of Step Norm"""

    def UnknownEntity(self) -> nanoocp.Standard.Standard_Transient:
        """Creates a new Unknown Entity for Step (UndefinedEntity)"""

    def IsUnknownEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e.
        Type UndefinedEntity, status Unknown
        """

    def DescrNumber(self, adescr: StepData_EDescr | None) -> int:
        """
        Returns a unique positive CaseNumber for types described by
        an EDescr (late binding)
        Warning : TypeNumber and DescrNumber must give together a unique
        positive case number for each distinct case, type or descr
        """

    def AddDescr(self, adescr: StepData_EDescr | None, CN: int) -> None:
        """
        Records an EDescr with its case number
        Also records its name for an ESDescr (simple type): an ESDescr
        is then used, for case number, or for type name
        """

    def HasDescr(self) -> bool:
        """
        Tells if a Protocol brings at least one ESDescr, i.e. if it
        defines at least one entity description by ESDescr mechanism
        """

    @overload
    def Descr(self, num: int) -> StepData_EDescr:
        """Returns the description attached to a case number, or null"""

    @overload
    def Descr(self, name: str, anylevel: bool = True) -> StepData_EDescr:
        """
        Returns a description according to its name
        <anylevel> True (D) : for <me> and its resources
        <anylevel> False : for <me> only
        """

    def ESDescr(self, name: str, anylevel: bool = True) -> StepData_ESDescr:
        """Idem as Descr but cast to simple description"""

    def ECDescr(self, names: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString], anylevel: bool = True) -> StepData_ECDescr:
        """
        Returns a complex description according to list of names
        <anylevel> True (D) : for <me> and its resources
        <anylevel> False : for <me> only
        """

    def AddPDescr(self, pdescr: StepData_PDescr | None) -> None:
        """Records an PDescr"""

    def PDescr(self, name: str, anylevel: bool = True) -> StepData_PDescr:
        """
        Returns a parameter description according to its name
        <anylevel> True (D) : for <me> and its resources
        <anylevel> False : for <me> only
        """

    def AddBasicDescr(self, esdescr: StepData_ESDescr | None) -> None:
        """Records an ESDescr, intended to build complex descriptions"""

    def BasicDescr(self, name: str, anylevel: bool = True) -> StepData_EDescr:
        """
        Returns a basic description according to its name
        <anylevel> True (D) : for <me> and its resources
        <anylevel> False : for <me> only
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_FileProtocol(StepData_Protocol):
    """
    A FileProtocol is defined as the addition of several already
    existing Protocols. It corresponds to the definition of a
    SchemaName with several Names, each one being attached to a
    specific Protocol. Thus, a File defined with a compound Schema
    is processed as any other one, once built the equivalent
    compound Protocol, a FileProtocol
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty FileProtocol"""

    @overload
    def __init__(self, theOther: StepData_FileProtocol) -> None: ...

    def Add(self, protocol: StepData_Protocol | None) -> None:
        """
        Adds a Protocol to the definition list of the FileProtocol
        But ensures that each class of Protocol is present only once
        in this list
        """

    def NbResources(self) -> int:
        """
        Gives the count of Protocols used as Resource (can be zero)
        i.e. the count of Protocol recorded by calling the method Add
        """

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank. Here, rank of calling Add"""

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a Case Number, specific of each recognized Type
        Here, NO Type at all is recognized properly : all Types are
        recognized by the resources
        """

    def GlobalCheck(self, G: nanoocp.Interface.Interface_Graph) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """Calls GlobalCheck for each of its recorded resources"""

    def SchemaName(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Schema Name attached to each class of Protocol
        To be redefined by each sub-class
        Here, SchemaName returns "" (empty String)
        was C++ : return const
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_FileRecognizer(nanoocp.Standard.Standard_Transient):
    def Evaluate(self, akey: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Evaluates if recognition has a result, returns it if yes
        In case of success, Returns True and puts result in "res"
        In case of Failure, simply Returns False
        Works by calling deferred method Eval, and in case of failure,
        looks for Added Recognizers to work
        """

    def Result(self) -> nanoocp.Standard.Standard_Transient:
        """Returns result of last recognition (call of Evaluate)"""

    def Add(self, reco: StepData_FileRecognizer | None) -> None:
        """
        Adds a new Recognizer to the Compound, at the end
        Several calls to Add work by adding in the order of calls :
        Hence, when Eval has failed to recognize, Evaluate will call
        Evaluate from the first added Recognizer if there is one,
        and to the second if there is still no result, and so on
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_FreeFormEntity(nanoocp.Standard.Standard_Transient):
    """
    A Free Form Entity allows to record any kind of STEP
    parameters, in any way of typing
    It is implemented with an array of fields
    A Complex entity can be defined, as a chain of FreeFormEntity
    (see Next and As)
    """

    def __init__(self, theOther: StepData_FreeFormEntity) -> None: ...

    def SetStepType(self, typenam: str) -> None:
        """
        Sets the type of an entity
        For a complex one, the type of this member
        """

    def StepType(self) -> str:
        """
        Returns the recorded StepType
        For a complex one, the type of this member
        """

    def SetNext(self, next: StepData_FreeFormEntity | None, last: bool = True) -> None:
        """
        Sets a next member, in order to define or complete a Complex
        entity
        If <last> is True (D), this next will be set as last of list
        Else, it is inserted just as next of <me>
        If <next> is Null, Next is cleared
        """

    def Next(self) -> StepData_FreeFormEntity:
        """
        Returns the next member of a Complex entity
        (remark : the last member has none)
        """

    def IsComplex(self) -> bool:
        """Returns True if a FreeFormEntity is Complex (i.e. has Next)"""

    def Typed(self, typenam: str) -> StepData_FreeFormEntity:
        """
        Returns the member of a FreeFormEntity of which the type name
        is given (exact match, no sub-type)
        """

    def TypeList(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns the list of types (one type for a simple entity),
        as is (non reordered)
        """

    @staticmethod
    def Reorder() -> tuple[bool, StepData_FreeFormEntity]:
        """
        Reorders a Complex entity if required, i.e. if member types
        are not in alphabetic order
        Returns False if nothing done (order was OK or simple entity),
        True plus modified <ent> if <ent> has been reordered
        """

    def SetNbFields(self, nb: int) -> None:
        """Sets a count of Fields, from scratch"""

    def NbFields(self) -> int:
        """Returns the count of fields"""

    def Field(self, num: int) -> StepData_Field:
        """Returns a field from its rank, for read-only use"""

    def CField(self, num: int) -> StepData_Field:
        """Returns a field from its rank, in order to modify it"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_GlobalNodeOfWriterLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty GlobalNode, with no Next"""

    @overload
    def __init__(self, theOther: StepData_GlobalNodeOfWriterLib) -> None: ...

    def Add(self, amodule: StepData_ReadWriteModule | None, aprotocol: StepData_Protocol | None) -> None:
        """
        Adds a Module bound with a Protocol to the list : does
        nothing if already in the list, THAT IS, Same Type (exact
        match) and Same State (that is, IsEqual is not required)
        Once added, stores its attached Protocol in correspondence
        """

    def Module(self) -> StepData_ReadWriteModule:
        """Returns the Module stored in a given GlobalNode"""

    def Protocol(self) -> StepData_Protocol:
        """Returns the attached Protocol stored in a given GlobalNode"""

    def Next(self) -> StepData_GlobalNodeOfWriterLib:
        """
        Returns the Next GlobalNode. If none is defined, returned
        value is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_NodeOfWriterLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty Node, with no Next"""

    @overload
    def __init__(self, theOther: StepData_NodeOfWriterLib) -> None: ...

    def AddNode(self, anode: StepData_GlobalNodeOfWriterLib | None) -> None:
        """
        Adds a couple (Module,Protocol), that is, stores it into
        itself if not yet done, else creates a Next Node to do it
        """

    def Module(self) -> StepData_ReadWriteModule:
        """Returns the Module designated by a precise Node"""

    def Protocol(self) -> StepData_Protocol:
        """Returns the Protocol designated by a precise Node"""

    def Next(self) -> StepData_NodeOfWriterLib:
        """
        Returns the Next Node. If none was defined, returned value
        is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_PDescr(nanoocp.Standard.Standard_Transient):
    """
    This class is intended to describe the authorized form for a
    parameter, as a type or a value for a field

    A PDescr firstly describes a type, which can be SELECT, i.e.
    have several members
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_PDescr) -> None: ...

    def SetName(self, name: str) -> None: ...

    def Name(self) -> str: ...

    def SetSelect(self) -> None:
        """
        Declares this PDescr to be a Select, hence to have members
        <me> itself can be the first member
        """

    def AddMember(self, member: StepData_PDescr | None) -> None:
        """Adds a member to a SELECT description"""

    def SetMemberName(self, memname: str) -> None:
        """
        Sets a name for SELECT member. To be used if a member is for
        an immediate type
        """

    def SetInteger(self) -> None:
        """Sets <me> for an Integer value"""

    def SetReal(self) -> None:
        """Sets <me> for a Real value"""

    def SetString(self) -> None:
        """Sets <me> for a String value"""

    def SetBoolean(self) -> None:
        """Sets <me> for a Boolean value (false,true)"""

    def SetLogical(self) -> None:
        """Sets <me> for a Logical value (false,true,unknown)"""

    def SetEnum(self) -> None:
        """
        Sets <me> for an Enum value
        Then, call AddEnumDef ordered from the first one (value 0)
        """

    def AddEnumDef(self, enumdef: str) -> None:
        """Adds an enum value as a string"""

    def SetType(self, atype: nanoocp.Standard.Standard_Type | None) -> None:
        """Sets <me> for an Entity which must match a Type (early-bound)"""

    def SetDescr(self, dscnam: str) -> None:
        """
        Sets <me> for a Described Entity, whose Description must match
        the type name <dscnam>
        """

    def AddArity(self, arity: int = 1) -> None:
        """
        Adds an arity count to <me>, by default 1
        1 : a simple field passes to a LIST/ARRAY etc
        or a LIST to a LIST OF LIST
        2 : a simple field passes to a LIST OF LIST
        """

    def SetArity(self, arity: int = 1) -> None:
        """
        Directly sets the arity count
        0 : simple field
        1 : LIST or ARRAY etc
        2 : LIST OF LIST
        """

    def SetFrom(self, other: StepData_PDescr | None) -> None:
        """
        Sets <me> as <other> but duplicated
        Hence, some definition may be changed
        """

    def SetOptional(self, opt: bool = True) -> None:
        """Sets/Unsets <me> to accept undefined values"""

    def SetDerived(self, der: bool = True) -> None:
        """Sets/Unsets <me> to be for a derived field"""

    def SetField(self, name: str, rank: int) -> None:
        """
        Sets <me> to describe a field of an entity
        With a name and a rank
        """

    def IsSelect(self) -> bool:
        """Tells if <me> is for a SELECT"""

    def Member(self, name: str) -> StepData_PDescr:
        """
        For a SELECT, returns the member whose name matches <name>
        To this member, the following question can then be asked
        Null Handle if <name> not matched or <me> not a SELECT

        Remark : not to be asked for an entity type
        Hence, following IsInteger .. Enum* only apply on <me> and
        require Member
        While IsType applies on <me> and all Select Members
        """

    def IsInteger(self) -> bool:
        """Tells if <me> is for an Integer"""

    def IsReal(self) -> bool:
        """Tells if <me> is for a Real value"""

    def IsString(self) -> bool:
        """Tells if <me> is for a String value"""

    def IsBoolean(self) -> bool:
        """Tells if <me> is for a Boolean value (false,true)"""

    def IsLogical(self) -> bool:
        """Tells if <me> is for a Logical value (false,true,unknown)"""

    def IsEnum(self) -> bool:
        """
        Tells if <me> is for an Enum value
        Then, call AddEnumDef ordered from the first one (value 0)
        Managed by an EnumTool
        """

    def EnumMax(self) -> int:
        """Returns the maximum integer for a suitable value (count - 1)"""

    def EnumValue(self, name: str) -> int:
        """
        Returns the numeric value found for an enum text
        The text must be in capitals and limited by dots
        A non-suitable text gives a negative value to be returned
        """

    def EnumText(self, val: int) -> str:
        """
        Returns the text which corresponds to a numeric value,
        between 0 and EnumMax. It is limited by dots
        """

    def IsEntity(self) -> bool:
        """Tells if <me> is for an Entity, either Described or CDL Type"""

    def IsType(self, atype: nanoocp.Standard.Standard_Type | None) -> bool:
        """
        Tells if <me> is for an entity of a given CDL type (early-bnd)
        (works for <me> + nexts if <me> is a Select)
        """

    def Type(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the type to match (IsKind), for a CDL Entity
        (else, null handle)
        """

    def IsDescr(self, descr: StepData_EDescr | None) -> bool:
        """
        Tells if <me> is for a Described entity of a given EDescr
        (does this EDescr match description name ?). For late-bnd
        (works for <me> + nexts if <me> is a Select)
        """

    def DescrName(self) -> str:
        """
        Returns the description (type name) to match, for a Described
        (else, empty string)
        """

    def Arity(self) -> int:
        """Returns the arity of <me>"""

    def Simple(self) -> StepData_PDescr:
        """
        For a LIST or LIST OF LIST, Returns the PDescr for the simpler
        PDescr. Else, returns <me>
        This allows to have different attributes for Optional for
        instance, on a field, and on the parameter of a LIST :
        [OPTIONAL] LIST OF [OPTIONAL] ...
        """

    def IsOptional(self) -> bool:
        """Tells if <me> is Optional"""

    def IsDerived(self) -> bool:
        """Tells if <me> is Derived"""

    def IsField(self) -> bool:
        """Tells if <me> is a Field. Else it is a Type"""

    def FieldName(self) -> str: ...

    def FieldRank(self) -> int: ...

    def Check(self, afild: StepData_Field) -> nanoocp.Interface.Interface_Check:
        """
        Semantic Check of a Field : does it complies with the given
        description ?
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_Plex(StepData_Described):
    """
    A Plex (for Complex) Entity is defined as a list of Simple
    Members ("external mapping")
    The types of these members must be in alphabetic order
    """

    @overload
    def __init__(self, descr: StepData_ECDescr | None) -> None:
        """
        Creates a Plex (empty). The complete creation is made by the
        ECDescr itself, by calling Add
        """

    @overload
    def __init__(self, theOther: StepData_Plex) -> None: ...

    def Add(self, member: StepData_Simple | None) -> None:
        """Adds a member to <me>"""

    def ECDescr(self) -> StepData_ECDescr:
        """Returns the Description as for a Plex"""

    def IsComplex(self) -> bool:
        """Returns False"""

    def Matches(self, steptype: str) -> bool:
        """
        Tells if a step type is matched by <me>
        For a Simple Entity : own type or super type
        For a Complex Entity : one of the members
        """

    def As(self, steptype: str) -> StepData_Simple:
        """
        Returns a Simple Entity which matches with a Type in <me> :
        For a Simple Entity : me if it matches, else a null handle
        For a Complex Entity : the member which matches, else null
        """

    def HasField(self, name: str) -> bool:
        """Tells if a Field brings a given name"""

    def Field(self, name: str) -> StepData_Field:
        """Returns a Field from its name; read-only"""

    def CField(self, name: str) -> StepData_Field:
        """Returns a Field from its name; read or write"""

    def NbMembers(self) -> int:
        """Returns the count of simple members"""

    def Member(self, num: int) -> StepData_Simple:
        """Returns a simple member from its rank"""

    def TypeList(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]:
        """Returns the actual list of members types"""

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """Fills a Check by using its Description"""

    def Shared(self, list: nanoocp.Interface.Interface_EntityIterator) -> None:
        """Fills an EntityIterator with entities shared by <me>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_ReadWriteModule(nanoocp.Interface.Interface_ReaderModule):
    """
    Defines basic File Access Module (Recognize, Read, Write)
    That is : ReaderModule (Recognize & Read) + Write for
    StepWriter (for a more centralized description)
    Warning : A sub-class of ReadWriteModule, which belongs to a particular
    Protocol, must use the same definition for Case Numbers (give
    the same Value for a StepType defined as a String from a File
    as the Protocol does for the corresponding Entity)
    """

    def CaseNum(self, data: nanoocp.Interface.Interface_FileReaderData | None, num: int) -> int:
        """
        Translate the Type of record <num> in <data> to a positive
        Case Number, or 0 if failed.
        Works with a StepReaderData, in which the Type of an Entity
        is defined as a String : Reads the RecordType <num> then calls
        CaseNum (this type)
        Warning : The methods CaseStep, StepType and Recognize,
        must be in phase (triplets CaseNum-StepType-Type of Object)
        """

    @overload
    def CaseStep(self, atype: nanoocp.TCollection.TCollection_AsciiString) -> int:
        """
        Defines Case Numbers corresponding to the recognized Types
        Called by CaseNum (data,num) above for a Simple Type Entity
        Warning : CaseStep must give the same Value as Protocol does for the
        Entity type which corresponds to this Type given as a String
        """

    @overload
    def CaseStep(self, types: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> int:
        """
        Same a above but for a Complex Type Entity ("Plex")
        The provided Default recognizes nothing
        """

    def IsComplex(self, CN: int) -> bool:
        """
        Returns True if the Case Number corresponds to a Complex Type
        ("Plex"). Remember that all possible combinations must be
        acknowledged to be processed
        Default is False for all cases. For a Protocol which defines
        possible Plexes, this method must be redefined.
        """

    def StepType(self, CN: int) -> str:
        """
        Function specific to STEP, which delivers the StepType as it
        is recorded in and read from a File compliant with STEP.
        This method is symmetric to the method CaseStep.
        StepType can be different from Dynamic Type's name, but
        belongs to the same class of Object.
        Returns an empty String if <CN> is zero.
        Warning : For a Complex Type Entity, returns an Empty String
        (Complex Type must be managed by users)
        """

    def ShortType(self, CN: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Function specific to STEP. Some STEP Types have a short form
        This method can be redefined to fill it
        By default, returns an empty string, which is then interpreted
        to take normal form from StepType
        """

    def ComplexType(self, CN: int, types: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> bool:
        """
        Function specific to STEP, which delivers the list of types
        which corresponds to a complex type. If <CN> is not for a
        complex type, this method returns False. Else it returns True
        and fills the list in alphabetic order.
        The default returns False. To be redefined as required.
        """

    def Read(self, CN: int, data: nanoocp.Interface.Interface_FileReaderData | None, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check:
        """General Read Function, calls ReadStep"""

    def ReadStep(self, CN: int, data: StepData_StepReaderData | None, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check:
        """Specific Read Function. Works with StepReaderData"""

    def WriteStep(self, CN: int, SW: StepData_StepWriter, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Write Function, switched by CaseNum"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_SelectMember(nanoocp.Standard.Standard_Transient):
    """
    The general form for a Select Member. A Select Member can,
    either define a value of a basic type (such as an integer)
    with an additional information : a name or list of names
    which precise the meaning of this value
    or be an alternate value in a select, which also accepts an
    entity (in this case, the name is not mandatory)

    Several sub-types of SelectMember are defined for integer and
    real value, plus an "universal" one for any, and one more to
    describe a select with several names

    It is also possible to define a specific subtype by redefining
    virtual method, then give a better control

    Remark : this class itself could be deferred, because at least
    one of its virtual methods must be redefined to be usable
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_SelectMember) -> None: ...

    def HasName(self) -> bool:
        """Tells if a SelectMember has a name. Default is False"""

    def Name(self) -> str:
        """Returns the name of a SelectMember. Default is empty"""

    def SetName(self, name: str) -> bool:
        """
        Sets the name of a SelectMember, returns True if done, False
        if no name is allowed
        Default does nothing and returns False
        """

    def Matches(self, name: str) -> bool:
        """
        Tells if the name of a SelectMember matches a given one
        By default, compares the strings, can be redefined (optimised)
        """

    def Kind(self) -> int: ...

    def SetKind(self, kind: int) -> None: ...

    def ParamType(self) -> nanoocp.Interface.Interface_ParamType:
        """
        Returns the Kind of the SelectMember, under the form of an
        enum ParamType
        """

    def Int(self) -> int:
        """
        This internal method gives access to a value implemented by an
        Integer (to read it)
        """

    def SetInt(self, val: int) -> None:
        """
        This internal method gives access to a value implemented by an
        Integer (to set it)
        """

    def Integer(self) -> int:
        """Gets the value as an Integer"""

    def SetInteger(self, val: int) -> None: ...

    def Boolean(self) -> bool: ...

    def SetBoolean(self, val: bool) -> None: ...

    def Logical(self) -> StepData_Logical: ...

    def SetLogical(self, val: StepData_Logical) -> None: ...

    def Real(self) -> float: ...

    def SetReal(self, val: float) -> None: ...

    def String(self) -> str: ...

    def SetString(self, val: str) -> None: ...

    def Enum(self) -> int: ...

    def EnumText(self) -> str: ...

    def SetEnum(self, val: int, text: str = '') -> None: ...

    def SetEnumText(self, val: int, text: str) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_SelectNamed(StepData_SelectMember):
    """
    This select member can be of any kind, and be named
    But its takes more memory than some specialised ones
    This class allows one name for the instance
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_SelectNamed) -> None: ...

    def HasName(self) -> bool: ...

    def Name(self) -> str: ...

    def SetName(self, name: str) -> bool: ...

    def Field(self) -> StepData_Field: ...

    def CField(self) -> StepData_Field: ...

    def Kind(self) -> int: ...

    def SetKind(self, kind: int) -> None: ...

    def Int(self) -> int:
        """
        This internal method gives access to a value implemented by an
        Integer (to read it)
        """

    def SetInt(self, val: int) -> None:
        """
        This internal method gives access to a value implemented by an
        Integer (to set it)
        """

    def Real(self) -> float: ...

    def SetReal(self, val: float) -> None: ...

    def String(self) -> str: ...

    def SetString(self, val: str) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_SelectArrReal(StepData_SelectNamed):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_SelectArrReal) -> None: ...

    def Kind(self) -> int: ...

    def ArrReal(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def SetArrReal(self, arr: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_SelectInt(StepData_SelectMember):
    """
    A SelectInt is a SelectMember specialised for a basic integer
    type in a select which also accepts entities : this one has
    NO NAME.
    For a named select, see SelectNamed
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_SelectInt) -> None: ...

    def Kind(self) -> int: ...

    def SetKind(self, kind: int) -> None: ...

    def Int(self) -> int: ...

    def SetInt(self, val: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_SelectReal(StepData_SelectMember):
    """
    A SelectReal is a SelectMember specialised for a basic real
    type in a select which also accepts entities : this one has
    NO NAME
    For a named select, see SelectNamed
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepData_SelectReal) -> None: ...

    def Kind(self) -> int: ...

    def Real(self) -> float: ...

    def SetReal(self, val: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_SelectType:
    """
    SelectType is the basis used for SELECT_TYPE definitions from
    the EXPRESS form. A SELECT_TYPE in EXPRESS is an enumeration
    of Types, it corresponds in a way to a Super-Type, but with
    no specific Methods, and no exclusivity (a given Type can be
    member of several SELECT_TYPES, plus be itself a SUB_TYPE).

    A SelectType can be field of a Transient Entity or only used
    to control an input Argument

    This class implies to designate each member Type by a Case
    Number which is a positive Integer value (this allows a faster treatment).

    With this class, a specific SelectType can :
    - recognize an Entity as complying or not with its definition,
    - storing it, with the guarantee that the stored Entity complies
    with the definition of the SelectType
    - and (if judged useful) give the stored Entity under the good
    Type rather than simply "Transient".
    """

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes the Type of an Entity. Returns a positive Number
        which identifies the Type in the definition List of the
        SelectType. Returns Zero if its Type in not in this List.
        """

    def Matches(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if the Type of an Entity complies with the
        definition list of the SelectType.
        Also checks for a SelectMember
        Default Implementation looks for CaseNum or CaseMem positive
        """

    def SetValue(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Stores an Entity. This allows to define a specific SelectType
        class with one read method per member Type, which returns the
        Value casted with the good Type.
        """

    def Nullify(self) -> None:
        """Nullifies the Stored Entity"""

    def Value(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the Stored Entity. Can be used to define specific
        read methods (see above)
        """

    def IsNull(self) -> bool:
        """Returns True if there is no Stored Entity (i.e. it is Null)"""

    def Type(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Effective (Dynamic) Type of the Stored Entity
        If it is Null, returns TYPE(Transient)
        """

    def CaseNumber(self) -> int:
        """
        Recognizes the Type of the stored Entity, or zero if it is
        Null or SelectMember. Calls the first method CaseNum on Value
        """

    def Description(self) -> StepData_PDescr:
        """
        Returns the Description which corresponds to <me>
        Null if no specific description to give. This description is
        used to control reading an check validity.
        Default returns a Null Handle, i.e. undefined description
        It can suffice if CaseNum and CaseMem give enough control
        """

    def NewMember(self) -> StepData_SelectMember:
        """
        Returns a preferred SelectMember. Default returns a Null
        By default, a SelectMember can be set according to data type
        and Name : it is a SelectNamed if Name is defined

        This method allows to define, for a specific SelectType, a
        specific SelectMember than SelectNamed. For instance for a
        Real plus a Name, a SelectReal plus a case number is a good
        solution, lighter than SelectNamed which is very multipurpose
        """

    def CaseMem(self, ent: StepData_SelectMember | None) -> int:
        """
        Recognize a SelectMember (kind, name). Returns a positive
        value which identifies the case in the List of immediate cases
        (distinct from the List of Entity Types). Zero if not
        recognizes
        Default returns 0, saying that no immediate value is allowed
        """

    def CaseMember(self) -> int:
        """
        Returns the Type of the stored SelectMember, or zero if it is
        Null or Entity. Calls the method CaseMem on Value
        """

    def Member(self) -> StepData_SelectMember:
        """Returns Value as a SelectMember. Null if not a SelectMember"""

    def SelectName(self) -> str:
        """
        Returns the type name of SelectMember. If no SelectMember or
        with no type name, returns an empty string
        To change it, pass through the SelectMember itself
        """

    def Int(self) -> int:
        """
        This internal method gives access to a value implemented by an
        Integer (to read it)
        """

    def SetInt(self, val: int) -> None:
        """
        This internal method gives access to a value implemented by an
        Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """

    def Integer(self) -> int:
        """Gets the value as an Integer"""

    def SetInteger(self, val: int, name: str = '') -> None:
        """
        Sets a new Integer value, with an optional type name
        Warning : If a SelectMember is already set, works on it : value and
        name must then be accepted by this SelectMember
        """

    def Boolean(self) -> bool: ...

    def SetBoolean(self, val: bool, name: str = '') -> None: ...

    def Logical(self) -> StepData_Logical: ...

    def SetLogical(self, val: StepData_Logical, name: str = '') -> None: ...

    def Real(self) -> float: ...

    def SetReal(self, val: float, name: str = '') -> None: ...

class StepData_Simple(StepData_Described):
    """
    A Simple Entity is defined by a type (which can heve super
    types) and a list of parameters
    """

    @overload
    def __init__(self, descr: StepData_ESDescr | None) -> None:
        """Creates a Simple Entity"""

    @overload
    def __init__(self, theOther: StepData_Simple) -> None: ...

    def ESDescr(self) -> StepData_ESDescr:
        """Returns description, as for simple"""

    def StepType(self) -> str:
        """Returns the recorded StepType (TypeName of its ESDescr)"""

    def IsComplex(self) -> bool:
        """Returns False"""

    def Matches(self, steptype: str) -> bool:
        """
        Tells if a step type is matched by <me>
        For a Simple Entity : own type or super type
        For a Complex Entity : one of the members
        """

    def As(self, steptype: str) -> StepData_Simple:
        """
        Returns a Simple Entity which matches with a Type in <me> :
        For a Simple Entity : me if it matches, else a null handle
        For a Complex Entity : the member which matches, else null
        """

    def HasField(self, name: str) -> bool:
        """Tells if a Field brings a given name"""

    def Field(self, name: str) -> StepData_Field:
        """Returns a Field from its name; read-only"""

    def CField(self, name: str) -> StepData_Field:
        """Returns a Field from its name; read or write"""

    def NbFields(self) -> int:
        """Returns the count of fields"""

    def FieldNum(self, num: int) -> StepData_Field:
        """Returns a field from its rank, for read-only use"""

    def CFieldNum(self, num: int) -> StepData_Field:
        """Returns a field from its rank, in order to modify it"""

    def Fields(self) -> StepData_FieldListN:
        """Returns the entire field list, read-only"""

    def CFields(self) -> StepData_FieldListN:
        """Returns the entire field list, read or write"""

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """Fills a Check by using its Description"""

    def Shared(self, list: nanoocp.Interface.Interface_EntityIterator) -> None:
        """Fills an EntityIterator with entities shared by <me>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_WriterLib:
    @overload
    def __init__(self) -> None:
        """
        Creates an empty Library : it will later by filled by method
        AddProtocol
        """

    @overload
    def __init__(self, aprotocol: StepData_Protocol | None) -> None:
        """
        Creates a Library which complies with a Protocol, that is :
        Same class (criterium IsInstance)
        This creation gets the Modules from the global set, those
        which are bound to the given Protocol and its Resources
        """

    @overload
    def __init__(self, theOther: StepData_WriterLib) -> None: ...

    @staticmethod
    def SetGlobal(amodule: StepData_ReadWriteModule | None, aprotocol: StepData_Protocol | None) -> None:
        """
        Adds a couple (Module-Protocol) into the global definition set
        for this class of Library.
        """

    def AddProtocol(self, aprotocol: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds a couple (Module-Protocol) to the Library, given the
        class of a Protocol. Takes Resources into account.
        (if <aprotocol> is not of type TheProtocol, it is not added)
        """

    def Clear(self) -> None:
        """
        Clears the list of Modules of a library (can be used to
        redefine the order of Modules before action : Clear then
        refill the Library by calls to AddProtocol)
        """

    def SetComplete(self) -> None:
        """
        Sets a library to be defined with the complete Global list
        (all the couples Protocol/Modules recorded in it)
        """

    def Select(self, obj: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, StepData_ReadWriteModule, int]:
        """
        Selects a Module from the Library, given an Object.
        Returns True if Select has succeeded, False else.
        Also Returns (as arguments) the selected Module and the Case
        Number determined by the associated Protocol.
        If Select has failed, <module> is Null Handle and CN is zero.
        (Select can work on any criterium, such as Object DynamicType)
        """

    def Start(self) -> None:
        """Starts Iteration on the Modules (sets it on the first one)"""

    def More(self) -> bool:
        """Returns True if there are more Modules to iterate on"""

    def Next(self) -> None:
        """
        Iterates by getting the next Module in the list
        If there is none, the exception will be raised by Value
        """

    def Module(self) -> StepData_ReadWriteModule:
        """Returns the current Module in the Iteration"""

    def Protocol(self) -> StepData_Protocol:
        """Returns the current Protocol in the Iteration"""

class StepData_StepWriter:
    """
    manages atomic file writing, under control of StepModel (for
    general organisation of file) and each class of Transient
    (for its own parameters) : prepares text to be written then
    writes it
    A stream cannot be used because Step limits line length at 72
    In more, a specific object offers more appropriate functions
    """

    @overload
    def __init__(self, amodel: StepData_StepModel | None) -> None:
        """
        Creates an empty StepWriter from a StepModel. The StepModel
        provides the Number of Entities, as identifiers for File
        """

    @overload
    def __init__(self, theOther: StepData_StepWriter) -> None: ...

    def LabelMode(self) -> int:
        """
        ModeLabel controls how to display entity ids :
        0 (D) gives entity number in the model
        1 gives the already recorded label (else, its number)
        Warning : conflicts are not controlled
        """

    def SetLabelMode(self, theValue: int) -> None:
        """
        Python addition: sets the value LabelMode() returns by reference in C++.
        """

    def TypeMode(self) -> int:
        """
        TypeMode controls the type form to use :
        0 (D) for normal long form
        1 for short form (if a type name has no short form, normal
        long form is then used)
        """

    def SetTypeMode(self, theValue: int) -> None:
        """
        Python addition: sets the value TypeMode() returns by reference in C++.
        """

    def FloatWriter(self) -> nanoocp.Interface.Interface_FloatWriter:
        """
        Returns the embedded FloatWriter, which controls sending Reals
        Use this method to access FloatWriter in order to consult or
        change its options (MainFormat, FormatForRange,ZeroSuppress),
        because it is returned as the address of its field
        """

    def SetScope(self, numscope: int, numin: int) -> None:
        """
        Declares the Entity Number <numscope> to correspond to a Scope
        which contains the Entity Number <numin>. Several calls to the
        same <numscope> add Entities in this Scope, in this order.
        Error if <numin> is already declared in the Scope
        Warning : the declaration of the Scopes is assumed to be consistent,
        i.e. <numin> is not referenced from outside this Scope
        (not checked here)
        """

    def IsInScope(self, num: int) -> bool:
        """Returns True if an Entity identified by its Number is in a Scope"""

    def SendModel(self, protocol: StepData_Protocol | None, headeronly: bool = False) -> None:
        """
        Sends the complete Model, included HEADER and DATA Sections
        Works with a WriterLib defined through a Protocol
        If <headeronly> is given True, only the HEADER Section is sent
        (used to Dump the Header of a StepModel)
        """

    def SendHeader(self) -> None:
        """Begins model header"""

    def SendData(self) -> None:
        """Begins data section; error if EndSec was not set"""

    def SendEntity(self, nument: int, lib: StepData_WriterLib) -> None:
        """
        Send an Entity of the Data Section. If it corresponds to a
        Scope, also Sends the Scope information and contained Items
        """

    def EndSec(self) -> None:
        """sets end of section; to be done before passing to next one"""

    def EndFile(self) -> None:
        """sets end of file; error is EndSec was not set"""

    def NewLine(self, evenempty: bool) -> None:
        """
        flushes current line; if empty, flushes it (defines a new
        empty line) if evenempty is True; else, skips it
        """

    def JoinLast(self, newline: bool) -> None:
        """
        joins current line to last one, only if new length is 72 max
        if newline is True, a new current line begins; else, current
        line is set to the last line (once joined) itself an can be
        completed
        """

    def Indent(self, onent: bool) -> None:
        """
        asks that further indentations will begin at position of
        entity first opening bracket; else they begin at zero (def)
        for each sublist level, two more blancks are added at beginning
        (except for text continuation, which must begin at true zero)
        """

    def SendIdent(self, ident: int) -> None:
        """
        begins an entity with an ident plus '=' (at beginning of line)
        entity ident is its Number given by the containing Model
        Warning : <ident> must be, either Number or Label, according LabelMode
        """

    def SendScope(self) -> None:
        """sets a begin of Scope (ends this line)"""

    def SendEndscope(self) -> None:
        """sets an end of Scope (on a separate line)"""

    def Comment(self, mode: bool) -> None:
        """
        sets a comment mark : if mode is True, begins Comment zone,
        if mode is False, ends Comment zone (if one is begun)
        """

    @overload
    def SendComment(self, text: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """sends a comment. Error if we are not inside a comment zone"""

    @overload
    def SendComment(self, text: str) -> None:
        """same as above but accepts a CString (ex.: "..." directly)"""

    def StartEntity(self, atype: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        sets entity's StepType, opens brackets, starts param no to 0
        params are separated by comma
        Remark : for a Multiple Type Entity (see Express ANDOR clause)
        StartComplex must be called before sending components, then
        each "Component" must be sent separately (one call to
        StartEntity for each one) : the Type which precedes is then
        automatically closed. Once all the components have been sent,
        EndComplex must be called, then and only then EndEntity
        """

    def StartComplex(self) -> None:
        """
        sends the start of a complex entity, which is a simple open
        bracket (without increasing bracket level)
        It must be called JUST AFTER SendEntity and BEFORE sending
        components, each one begins by StartEntity
        """

    def EndComplex(self) -> None:
        """
        sends the end of a complex entity : a simple closed bracket
        It must be called AFTER sending all the components and BEFORE
        the final call to EndEntity
        """

    def SendField(self, fild: StepData_Field, descr: StepData_PDescr | None) -> None:
        """
        Sends the content of a field, controlled by its descriptor
        If the descriptor is not defined, follows the description
        detained by the field itself
        """

    def SendSelect(self, sm: StepData_SelectMember | None, descr: StepData_PDescr | None) -> None:
        """Sends a SelectMember, which cab be named or not"""

    def SendList(self, list: StepData_FieldList, descr: StepData_ESDescr | None) -> None:
        """
        Send the content of an entity as being a FieldList controlled
        by its descriptor. This includes start and end brackets but
        not the entity type
        """

    def OpenSub(self) -> None:
        """open a sublist by a '('"""

    def OpenTypedSub(self, subtype: str) -> None:
        """open a sublist with its type then a '('"""

    def CloseSub(self) -> None:
        """closes a sublist by a ')'"""

    def AddParam(self) -> None:
        """
        prepares adding a parameter (that is, adds ',' except for
        first one); normally for internal use; can be used to send
        a totally empty parameter (with no literal value)
        """

    @overload
    def Send(self, val: int) -> None:
        """sends an integer parameter"""

    @overload
    def Send(self, val: float) -> None:
        """sends a real parameter (works with FloatWriter)"""

    @overload
    def Send(self, val: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """sends a text given as string (it will be set between '...')"""

    @overload
    def Send(self, val: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        sends a reference to an entity (its identifier with '#')
        REMARK 1 : a Null <val> is interpreted as "Undefined"
        REMARK 2 : for an HAsciiString which is not recorded in the
        Model, it is send as its String Content, between quotes
        """

    def SendBoolean(self, val: bool) -> None:
        """
        sends a Boolean as .T. for True or .F. for False
        (it is an useful case of Enum, which is built-in)
        """

    def SendLogical(self, val: StepData_Logical) -> None:
        """
        sends a Logical as .T. or .F. or .U. according its Value
        (it is a standard case of Enum for Step, and is built-in)
        """

    @overload
    def SendString(self, val: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def SendString(self, val: str) -> None:
        """sends a string exactly as it is given"""

    @overload
    def SendEnum(self, val: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        sends an enum given by String (literal expression)
        adds '.' around it if not done
        Remark : val can be computed by class EnumTool from StepData:
        StepWriter.SendEnum (myenum.Text(enumval));
        """

    @overload
    def SendEnum(self, val: str) -> None:
        """
        sends an enum given by String (literal expression)
        adds '.' around it if not done
        """

    def SendArrReal(self, anArr: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """sends an array of real"""

    def SendUndef(self) -> None:
        """sends an undefined (optional absent) parameter (by '$')"""

    def SendDerived(self) -> None:
        """
        sends a "Derived" parameter (by '*'). A Derived Parameter has
        been inherited from a Super-Type then redefined as being
        computed by a function. Hence its value in file is senseless.
        """

    def EndEntity(self) -> None:
        """
        sends end of entity (closing bracket plus ';')
        Error if count of opened-closed brackets is not null
        """

    def CheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the check-list, which has received possible checks :
        for unknown entities, badly loaded ones, null or unknown
        references
        """

    def NbLines(self) -> int:
        """Returns count of Lines"""

    def Line(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns a Line given its rank in the File"""

    def Print(self) -> tuple[bool, str]:
        """
        writes result on an output defined as an OStream
        then clears it
        """

    @staticmethod
    def CleanTextForSend(theText: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Static helper function to prepare text for STEP file output while preserving
        existing ISO 10303-21 control directives.

        This function processes input text and escapes special characters (quotes, backslashes,
        newlines, tabs) for STEP file format compliance, while carefully preserving any existing
        control directives that may already be present in the input string.

        Supported control directive patterns that are preserved:
        - \\X{HH}\\ : Single byte character encoding (U+0000 to U+00FF)
        - \\X2\\{HHHH}...\\X0\\ : UTF-16 character encoding
        - \\X4\\{HHHHHHHH}...\\X0\\ : UTF-32 character encoding
        - \\S\\ : Latin codepoint character with current code page
        - \\P{A-I}\\ : Code page control directive
        - \\N\\ : Newline directive (preserved as-is)
        - \\T\\ : Tab directive (preserved as-is)

        Character escaping performed (only on non-directive content):
        - Single quote (') -> double quote ('')
        - Backslash (\\) -> double backslash (\\\\)
        - Newline character -> \\N\\ directive
        - Tab character -> \\T\\ directive

        Example:
        Input:  "text with \\XA7\\ and 'quotes'"
        Output: "text with \\XA7\\ and ''quotes''"

        @param theText The input text string to be processed
        @return Processed text with preserved control directives and escaped special characters
        """

class StepData_StepDumper:
    """
    Provides a way to dump entities processed through STEP, with
    these features :
    - same form as for writing a STEP File (because it is clear
    and compact enough, even if the names of the fields do not
    appear) : thus, no additional resource is required
    - possibility to look for an entity itself (only its Type or
    with its content), an entity and it shared items (one level)
    or all the entities its refers to, directly or recursively.
    """

    @overload
    def __init__(self, amodel: StepData_StepModel | None, protocol: StepData_Protocol | None, mode: int = 0) -> None:
        """
        Creates a StepDumper, able to work on a given StepModel
        (which defines the total scope for dumping entities) and
        a given Protocol from Step (which defines the authorized
        types to be dumped)
        <mode> commands what is to be displayed (number or label)
        0 for number (and corresponding labels  are displayed apart)
        1 for label  (and corresponding numbers are displayed apart)
        2 for label without anymore
        """

    @overload
    def __init__(self, theOther: StepData_StepDumper) -> None: ...

    def StepWriter(self) -> StepData_StepWriter:
        """
        Gives an access to the tool which is used to work : this allow
        to acts on some parameters : Floating Format, Scopes ...
        """

    @overload
    def Dump(self, ent: nanoocp.Standard.Standard_Transient | None, level: int) -> tuple[bool, str]:
        """
        Dumps a Entity on an Messenger. Returns True if
        success, False, if the entity to dump has not been recognized
        by the Protocol. <level> can have one of these values :
        - 0 : prints the TYPE only, as known in STEP Files (StepType)
        If <ent> has not been regognized by the Protocol, or if its
        type is Complex, the StepType is replaced by the display of
        the cdl type. Complex Type are well processed by level 1.
        - 1 : dumps the entity, completely (whatever it has simple or
        complex type) but alone.
        - 2 : dumps the entity completely, plus the item its refers to
        at first level (a header message designates the starting
        entity of the dump) <Lists Shared and Implied>
        - 3 : dumps the entity and its referred items at any levels

        For levels 1,2,3, the numbers displayed (form #nnn) are the
        numbers of the corresponding entities in the Model
        """

    @overload
    def Dump(self, num: int, level: int) -> tuple[bool, str]:
        """
        Works as Dump with a Transient, but directly takes the
        entity designated by its number in the Model
        Returns False, also if <num> is out of range
        """

class StepData_StepModel(nanoocp.Interface.Interface_InterfaceModel):
    """
    Gives access to
    - entities in a STEP file,
    - the STEP file header.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty STEP model with an empty header."""

    @overload
    def __init__(self, theOther: StepData_StepModel) -> None: ...

    def Entity(self, num: int) -> nanoocp.Standard.Standard_Transient:
        """
        returns entity given its rank.
        Same as InterfaceEntity, but with a shorter name
        """

    def GetFromAnother(self, other: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """gets header from another Model (uses Header Protocol)"""

    def NewEmptyModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns a New Empty Model, same type as <me>, i.e. StepModel"""

    def Header(self) -> nanoocp.Interface.Interface_EntityIterator:
        """returns Header entities under the form of an iterator"""

    def HasHeaderEntity(self, atype: nanoocp.Standard.Standard_Type | None) -> bool:
        """says if a Header entity has a specified type"""

    def HeaderEntity(self, atype: nanoocp.Standard.Standard_Type | None) -> nanoocp.Standard.Standard_Transient:
        """Returns Header entity with specified type, if there is"""

    def ClearHeader(self) -> None:
        """Clears the Header"""

    def AddHeaderEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """Adds an Entity to the Header"""

    def VerifyCheck(self) -> nanoocp.Interface.Interface_Check:
        """Specific Check, checks Header Items with HeaderProtocol"""

    def DumpHeader(self, level: int = 0) -> str:
        """
        Dumps the Header, with the Header Protocol of StepData.
        If the Header Protocol is not defined, for each Header Entity,
        prints its Type. Else sends the Header under the form of
        HEADER Section of an Ascii Step File
        <level> is not used because Header is not so big
        """

    def ClearLabels(self) -> None:
        """erases specific labels, i.e. clears the map (entity-ident)"""

    def SetIdentLabel(self, ent: nanoocp.Standard.Standard_Transient | None, ident: int) -> None:
        """
        Attaches an ident to an entity to produce a label
        (does nothing if <ent> is not in <me>)
        """

    def IdentLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """returns the label ident attached to an entity, 0 if not in me"""

    def PrintLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints label specific to STEP norm for a given entity, i.e.
        if a LabelIdent has been recorded, its value with '#', else
        the number in the model with '#' and between ()
        """

    def StringLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a string with the label attached to a given entity,
        same form as for PrintLabel
        """

    def SourceCodePage(self) -> nanoocp.Resource.Resource_FormatType:
        """
        Return the encoding of STEP file for converting names into UNICODE.
        Initialized from "read.step.codepage" variable by constructor, which is Resource_UTF8 by
        default.
        """

    def SetSourceCodePage(self, theCode: nanoocp.Resource.Resource_FormatType) -> None:
        """Return the encoding of STEP file for converting names into UNICODE."""

    def SetLocalLengthUnit(self, theUnit: float) -> None:
        """Sets local length unit using for transfer process"""

    def LocalLengthUnit(self) -> float:
        """Returns local length unit using for transfer process (1 by default)"""

    def SetWriteLengthUnit(self, theUnit: float) -> None:
        """Sets length unit using for writing process"""

    def WriteLengthUnit(self) -> float:
        """Returns length unit using for writing process (1 by default)"""

    def IsInitializedUnit(self) -> bool:
        """
        Returns the unit initialization flag
        True - the unit was initialized
        False - the unit value was not initialized, the default value is used
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def InternalParameters(self) -> nanoocp.DESTEP.DESTEP_Parameters: ...

    @InternalParameters.setter
    def InternalParameters(self, arg: nanoocp.DESTEP.DESTEP_Parameters, /) -> None: ...

class StepData_StepReaderData(nanoocp.Interface.Interface_FileReaderData):
    """
    Specific FileReaderData for Step
    Contains literal description of entities (for each one : type
    as a string, ident, parameter list)
    provides references evaluation, plus access to literal data
    and specific access methods (Boolean, XY, XYZ)
    """

    @overload
    def __init__(self, nbheader: int, nbtotal: int, nbpar: int, theSourceCodePage: nanoocp.Resource.Resource_FormatType = Resource_FormatType.Resource_FormatType_UTF8) -> None:
        """
        creates StepReaderData correctly dimensioned (necessary at
        creation time, because it contains arrays)
        nbheader is nb of records for Header, nbtotal for Header+Data
        and nbpar gives the total count of parameters
        """

    @overload
    def __init__(self, theOther: StepData_StepReaderData) -> None: ...

    def SetRecord(self, num: int, ident: str, type: str, nbpar: int) -> None:
        """Fills the fields of a record"""

    def AddStepParam(self, num: int, aval: str, atype: nanoocp.Interface.Interface_ParamType, nument: int = 0) -> None:
        """
        Fills the fields of a parameter of a record. This is a variant
        of AddParam, Adapted to STEP (optimized for specific values)
        """

    def RecordType(self, num: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Record Type"""

    def CType(self, num: int) -> str:
        """
        Returns Record Type as a CString
        was C++ : return const
        """

    def RecordIdent(self, num: int) -> int:
        """
        Returns record identifier (Positive number)
        If returned ident is not positive : Sub-List or Scope mark
        """

    def SubListNumber(self, num: int, nump: int, aslast: bool) -> int:
        """
        Returns SubList numero designated by a parameter (nump) in a
        record (num), or zero if the parameter does not exist or is
        not a SubList address. Zero too If aslast is True and nump
        is not for the last parameter
        """

    def IsComplex(self, num: int) -> bool:
        """
        Returns True if <num> corresponds to a Complex Type Entity
        (as can be defined by ANDOR Express clause)
        """

    def ComplexType(self, num: int, types: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Returns the List of Types which correspond to a Complex Type
        Entity. If not Complex, there is just one Type in it
        For a SubList or a Scope mark, <types> remains empty
        """

    def NextForComplex(self, num: int) -> int:
        """
        Returns the Next "Component" for a Complex Type Entity, of
        which <num> is already a Component (the first one or a next one)
        Returns 0 for a Simple Type or for the last Component
        """

    @overload
    def NamedForComplex(self, name: str, num0: int) -> tuple[bool, int, nanoocp.Interface.Interface_Check]:
        """
        Determines the first component which brings a given name, for
        a Complex Type Entity
        <num0> is the very first record of this entity
        <num> is given the last NextNamedForComplex, starts at zero
        it is returned as the newly found number
        Hence, in the normal case, NextNamedForComplex starts by num0
        if <num> is zero, else by NextForComplex(num)
        If the alphabetic order is not respected, it restarts from
        num0 and loops on NextForComplex until finding <name>
        In case of "non-alphabetic order", <ach> is filled with a
        Warning for this name
        In case of "not-found at all", <ach> is filled with a Fail,
        and <num> is returned as zero

        Returns True if alphabetic order, False else
        """

    @overload
    def NamedForComplex(self, theName: str, theShortName: str, num0: int) -> tuple[bool, int, nanoocp.Interface.Interface_Check]:
        """
        Determines the first component which brings a given name, or
        short name for a Complex Type Entity
        <num0> is the very first record of this entity
        <num> is given the last NextNamedForComplex, starts at zero
        it is returned as the newly found number
        Hence, in the normal case, NextNamedForComplex starts by num0
        if <num> is zero, else by NextForComplex(num)
        If the alphabetic order is not respected, it restarts from
        num0 and loops on NextForComplex until finding <name>
        In case of "non-alphabetic order", <ach> is filled with a
        Warning for this name
        In case of "not-found at all", <ach> is filled with a Fail,
        and <num> is returned as zero

        Returns True if alphabetic order, False else
        """

    def CheckNbParams(self, num: int, nbreq: int, mess: str = '') -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        Checks Count of Parameters of record <num> to equate <nbreq>
        If this Check is successful, returns True
        Else, fills <ach> with an Error Message then returns False
        <mess> is included in the Error message if given non empty
        """

    def ReadSubList(self, num: int, nump: int, mess: str, optional: bool = False, lenmin: int = 0, lenmax: int = 0) -> tuple[bool, nanoocp.Interface.Interface_Check, int]:
        """
        reads parameter <nump> of record <num> as a sub-list (may be
        typed, see ReadTypedParameter in this case)
        Returns True if OK. Else (not a LIST), returns false and
        feeds Check with appropriate check
        If <optional> is True and Param is not defined, returns True
        with <ach> not filled and <numsub> returned as 0
        Works with SubListNumber with <aslast> false (no specific case
        for last parameter)
        """

    def ReadSub(self, numsub: int, mess: str, descr: StepData_PDescr | None) -> tuple[int, nanoocp.Interface.Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        reads the content of a sub-list into a transient :
        SelectNamed, or HArray1 of Integer,Real,String,Transient ...
        recursive call if list of list ...
        If a sub-list has mixed types, an HArray1OfTransient is
        produced, it may contain SelectMember
        Intended to be called by ReadField
        The returned status is : negative if failed, 0 if empty.
        Else the kind to be recorded in the field
        """

    def ReadMember(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, StepData_SelectMember]:
        """
        Reads parameter <nump> of record <num> into a SelectMember,
        self-sufficient (no Description needed)
        If <val> is already created, it will be filled, as possible
        And if reading does not match its own description, the result
        will be False
        If <val> is not it not yet created, it will be (SelectNamed)
        useful if a field is defined as a SelectMember, directly
        (SELECT with no Entity as member)
        But SelectType also manages SelectMember (for SELECT with
        some members as Entity, some other not)
        """

    def ReadField(self, num: int, nump: int, mess: str, descr: StepData_PDescr | None, fild: StepData_Field) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        reads parameter <nump> of record <num> into a Field,
        controlled by a Parameter Descriptor (PDescr), which controls
        its allowed type(s) and value
        <ach> is filled if the read parameter does not match its
        description (but the field is read anyway)
        If the description is not defined, no control is done
        Returns True when done
        """

    def ReadList(self, num: int, descr: StepData_ESDescr | None, list: StepData_FieldList) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """reads a list of fields controlled by an ESDescr"""

    def ReadAny(self, num: int, nump: int, mess: str, descr: StepData_PDescr | None) -> tuple[bool, nanoocp.Interface.Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        Reads parameter <nump> of record <num> into a Transient Value
        according to the type of the parameter :
        Named for Integer,Boolean,Logical,Enum,Real : SelectNamed
        Immediate Integer,Boolean,Logical,Enum,Real : SelectInt/Real
        Text  : HAsciiString
        Ident : the referenced Entity
        Sub-List not processed, see ReadSub
        This value is controlled by a Parameter Descriptor (PDescr),
        which controls its allowed type and value
        <ach> is filled if the read parameter does not match its
        description (the select is nevertheless created if possible)

        Warning : val is in out, hence it is possible to predefine a specific
        SelectMember then to fill it. If <val> is Null or if the
        result is not a SelectMember, val itself is returned a new ref
        For a Select with a Name, <val> must then be a SelectNamed
        """

    def ReadXY(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, float, float]:
        """
        reads parameter <nump> of record <num> as a sub-list of
        two Reals X,Y. Returns True if OK. Else, returns false and
        feeds Check with appropriate Fails (parameter not a sub-list,
        not two Reals in the sub-list) composed with "mess" which
        gives the name of the parameter
        """

    def ReadXYZ(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, float, float, float]:
        """
        reads parameter <nump> of record <num> as a sub-list of
        three Reals X,Y,Z. Return value and Check managed as by
        ReadXY (demands a sub-list of three Reals)
        """

    def ReadReal(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, float]:
        """
        reads parameter <nump> of record <num> as a single Real value.
        Return value and Check managed as by ReadXY (demands a Real)
        """

    @overload
    def ReadEntity(self, num: int, nump: int, mess: str, atype: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Interface.Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        Reads parameter <nump> of record <num> as a single Entity.
        Return value and Check managed as by ReadReal (demands a
        reference to an Entity). In Addition, demands read Entity
        to be Kind of a required Type <atype>.
        Remark that returned status is False and <ent> is Null if
        parameter is not an Entity, <ent> remains Not Null is parameter
        is an Entity but is not Kind of required type
        """

    @overload
    def ReadEntity(self, num: int, nump: int, mess: str, sel: StepData_SelectType) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        Same as above, but a SelectType checks Type Matching, and
        records the read Entity (see method Value from SelectType)
        """

    def ReadInteger(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, int]:
        """
        reads parameter <nump> of record <num> as a single Integer.
        Return value & Check managed as by ReadXY (demands an Integer)
        """

    def ReadBoolean(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, bool]:
        """
        reads parameter <nump> of record <num> as a Boolean
        Return value and Check managed as by ReadReal (demands a
        Boolean enum, i.e. text ".T." for True or ".F." for False)
        """

    def ReadLogical(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, StepData_Logical]:
        """
        reads parameter <nump> of record <num> as a Logical
        Return value and Check managed as by ReadBoolean (demands a
        Logical enum, i.e. text ".T.", ".F.", or ".U.")
        """

    def ReadString(self, num: int, nump: int, mess: str) -> tuple[bool, nanoocp.Interface.Interface_Check, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        reads parameter <nump> of record <num> as a String (text
        between quotes, quotes are removed by the Read operation)
        Return value and Check managed as by ReadXY (demands a String)
        """

    def FailEnumValue(self, num: int, nump: int, mess: str) -> nanoocp.Interface.Interface_Check:
        """
        Fills a check with a fail message if enumeration value does
        match parameter definition
        Just a help to centralize message definitions
        """

    def ReadEnum(self, num: int, nump: int, mess: str, enumtool: StepData_EnumTool) -> tuple[bool, nanoocp.Interface.Interface_Check, int]:
        """
        Reads parameter <nump> of record <num> as an Enumeration (text
        between dots) and converts it to an integer value, by an
        EnumTool. Returns True if OK, false if : this parameter is not
        enumeration, or is not recognized by the EnumTool (with fail)
        """

    def ReadTypedParam(self, num: int, nump: int, mustbetyped: bool, mess: str, typ: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, nanoocp.Interface.Interface_Check, int, int]:
        """
        Resolves a parameter which can be enclosed in a type def., as
        TYPE(val). The parameter must then be read normally according
        its type. Parameter to be resolved is <nump> of record <num>
        <mustbetyped> True demands a typed parameter
        <mustbetyped> False accepts a non-typed parameter as option
        mess and ach as usual
        <numr>,<numrp> are the resolved record and parameter numbers
        = num,nump if no type, else numrp=1
        <typ> returns the recorded type, or empty string
        Remark : a non-typed list is considered as "non-typed\"
        """

    def CheckDerived(self, num: int, nump: int, mess: str, errstat: bool = False) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        Checks if parameter <nump> of record <num> is given as Derived
        If this Check is successful (i.e. Param = "*"), returns True
        Else, fills <ach> with a Message which contains <mess> and
        returns False. According to <errstat>, this message is Warning
        if errstat is False (Default), Fail if errstat is True
        """

    def NbEntities(self) -> int:
        """Returns total count of Entities (including Header)"""

    def FindNextRecord(self, num: int) -> int:
        """
        determines the first suitable record following a given one
        that is, skips SCOPE,ENDSCOPE and SUBLIST records
        Note : skips Header records, which are accessed separately
        """

    def SetEntityNumbers(self, withmap: bool = True) -> None:
        """
        determines reference numbers in EntityNumber fields
        called by Prepare from StepReaderTool to prepare later using
        by a StepModel. This method is attached to StepReaderData
        because it needs a massive amount of data accesses to work

        If <withmap> is given False, the basic exploration algorithm
        is activated, otherwise a map is used as far as it is possible
        this option can be used only to test this algorithm
        """

    def FindNextHeaderRecord(self, num: int) -> int:
        """
        determine first suitable record of Header
        works as FindNextRecord, but treats only Header records
        """

    def PrepareHeader(self) -> None:
        """
        Works as SetEntityNumbers but for Header : more simple because
        there are no Reference, only Sub-Lists
        """

    def GlobalCheck(self) -> nanoocp.Interface.Interface_Check:
        """
        Returns the Global Check. It can record Fail messages about
        Undefined References (detected by SetEntityNumbers)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepData_StepReaderTool(nanoocp.Interface.Interface_FileReaderTool):
    """
    Specific FileReaderTool for Step; works with FileReaderData
    provides references evaluation, plus access to literal data
    and specific methods defined by FileReaderTool
    Remarks : works with a ReaderLib to load Entities
    """

    @overload
    def __init__(self, reader: StepData_StepReaderData | None, protocol: StepData_Protocol | None) -> None:
        """
        creates StepReaderTool to work with a StepReaderData according
        to a Step Protocol. Defines the ReaderLib at this time
        """

    @overload
    def __init__(self, theOther: StepData_StepReaderTool) -> None: ...

    @overload
    def Prepare(self, optimize: bool = True) -> None:
        """
        Bounds empty entities to records, uses default Recognition
        provided by ReaderLib and ReaderModule. Also calls computation
        of references (SetEntityNumbers from StepReaderData)
        Works only on data entities (skips header)
        <optimize> given False allows to test some internal algorithms
        which are normally avoided (see also StepReaderData)
        """

    @overload
    def Prepare(self, reco: StepData_FileRecognizer | None, optimize: bool = True) -> None:
        """
        Bounds empty entities to records, works with a specific
        FileRecognizer, stored and later used in Recognize
        Works only on data entities (skips header)
        <optimize : same as above
        """

    def Recognize(self, num: int) -> tuple[bool, nanoocp.Interface.Interface_Check, nanoocp.Standard.Standard_Transient]:
        """
        recognizes records, by asking either ReaderLib (default) or
        FileRecognizer (if defined) to do so. <ach> is to call
        RecognizeByLib
        """

    def PrepareHeader(self, reco: StepData_FileRecognizer | None) -> None:
        """
        bounds empty entities and sub-lists to header records
        works like Prepare + SetEntityNumbers, but for header
        (N.B.: in Header, no Ident and no reference)
        FileRecognizer is to specify Entities which are allowed to be
        defined in the Header (not every type can be)
        """

    def BeginRead(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        fills model's header; that is, gives to it Header entities
        and commands their loading. Also fills StepModel's Global
        Check from StepReaderData's GlobalCheck
        """

    def AnalyseRecord(self, num: int, anent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        fills an entity, given record no; works by using a ReaderLib
        to load each entity, which must be a Transient
        Actually, returned value is True if no fail, False else
        """

    def EndRead(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Ends file reading after reading all the entities
        Here, it binds in the model, Idents to Entities (for checks)
        """

class StepData_UndefinedEntity(nanoocp.Standard.Standard_Transient):
    """
    Undefined entity specific to Step Interface, in which StepType
    is defined at each instance, or is a SubList of another one
    Uses an UndefinedContent, that from Interface is suitable.
    Also an Entity defined by STEP can be "Complex Type" (see
    ANDOR clause in Express).
    """

    @overload
    def __init__(self) -> None:
        """creates an Unknown entity"""

    @overload
    def __init__(self, issub: bool) -> None:
        """
        Creates a SubList of an Unknown entity : it is an Unknown
        Entity with no Type, but flagged as "SUB" if issub is True
        """

    @overload
    def __init__(self, theOther: StepData_UndefinedEntity) -> None: ...

    def UndefinedContent(self) -> nanoocp.Interface.Interface_UndefinedContent:
        """Returns the UndefinedContent which brings the Parameters"""

    def IsSub(self) -> bool:
        """Returns True if an Unndefined Entity is SubPart of another one"""

    def IsComplex(self) -> bool:
        """Returns True if <me> defines a Multiple Type Entity (see ANDOR)"""

    def Next(self) -> StepData_UndefinedEntity:
        """
        For a Multiple Type Entity, returns the Next "Component"
        For more than two Types, iterative definition (Next->Next...)
        Returns a Null Handle for the end of the List
        """

    def StepType(self) -> str:
        """
        gives entity type, read from file
        For a Complex Type Entity, gives the first Type read, each
        "Next" gives its "partial" type
        was C++ : return const
        """

    def ReadRecord(self, SR: StepData_StepReaderData | None, num: int) -> nanoocp.Interface.Interface_Check:
        """
        reads data from StepReaderData (i.e. from file), by filling
        StepType and parameters stored in the UndefinedContent
        """

    def WriteParams(self, SW: StepData_StepWriter) -> None:
        """write data to StepWriter, taken from UndefinedContent"""

    def GetFromAnother(self, other: StepData_UndefinedEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """reads another UndefinedEntity from StepData"""

    def FillShared(self, list: nanoocp.Interface.Interface_EntityIterator) -> None:
        """Fills the list of shared entities"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
