"""OCCT package IGESData (toolkit TKDEIGES)"""

import enum
from typing import overload

import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class IGESData_DefType(enum.IntEnum):
    """
    Some fields of an IGES entity may be
    - Undefined
    - Defined as a positive integer
    - Defined as a reference to a specialized entity.
    A typical example of this kind of variation is color.
    This enumeration allows you to identify which of the above is the case.
    The semantics of the terms are as follows:
    - DefVoid indicates that the item contained in the field is undefined
    - DefValue indicates that the item is defined as an immediate
    positive integer value (i.e. not a pointer)
    - DefReference indicates that the item is defined as an entity
    - DefAny indicates the item could not be determined
    - ErrorVal indicates that the item is defined as an integer
    but its value is incorrect (it could be out of range, for example)
    - ErrorRef indicates that the item is defined as an entity but
    is not of the required type.
    """

    IGESData_DefVoid = 0

    IGESData_DefValue = 1

    IGESData_DefReference = 2

    IGESData_DefAny = 3

    IGESData_ErrorVal = 4

    IGESData_ErrorRef = 5

IGESData_DefVoid: IGESData_DefType = IGESData_DefType.IGESData_DefVoid

IGESData_DefValue: IGESData_DefType = IGESData_DefType.IGESData_DefValue

IGESData_DefReference: IGESData_DefType = IGESData_DefType.IGESData_DefReference

IGESData_DefAny: IGESData_DefType = IGESData_DefType.IGESData_DefAny

IGESData_ErrorVal: IGESData_DefType = IGESData_DefType.IGESData_ErrorVal

IGESData_ErrorRef: IGESData_DefType = IGESData_DefType.IGESData_ErrorRef

class IGESData_DefList(enum.IntEnum):
    """
    Some fields of an IGES entity may be
    - Undefined
    - Defined as a single item
    - Defined as a list of items.
    A typical example, which presents this kind of variation,
    is a level number.
    This enumeration allows you to identify which of the above is the case.
    The semantics of the terms is as follows:
    - DefNone indicates that the list is empty (there is not
    even a single item).
    - DefOne indicates that the list contains a single item.
    - DefSeveral indicates that the list contains several items.
    - ErrorOne indicates that the list contains one item, but
    that this item is incorrect
    - ErrorSeveral indicates that the list contains several
    items, but that at least one of them is incorrect.
    """

    IGESData_DefNone = 0

    IGESData_DefOne = 1

    IGESData_DefSeveral = 2

    IGESData_ErrorOne = 3

    IGESData_ErrorSeveral = 4

IGESData_DefNone: IGESData_DefList = IGESData_DefList.IGESData_DefNone

IGESData_DefOne: IGESData_DefList = IGESData_DefList.IGESData_DefOne

IGESData_DefSeveral: IGESData_DefList = IGESData_DefList.IGESData_DefSeveral

IGESData_ErrorOne: IGESData_DefList = IGESData_DefList.IGESData_ErrorOne

IGESData_ErrorSeveral: IGESData_DefList = IGESData_DefList.IGESData_ErrorSeveral

class IGESData_ReadStage(enum.IntEnum):
    """gives successive stages of reading an entity (see ParamReader)"""

    IGESData_ReadDir = 0

    IGESData_ReadOwn = 1

    IGESData_ReadAssocs = 2

    IGESData_ReadProps = 3

    IGESData_ReadEnd = 4

IGESData_ReadDir: IGESData_ReadStage = IGESData_ReadStage.IGESData_ReadDir

IGESData_ReadOwn: IGESData_ReadStage = IGESData_ReadStage.IGESData_ReadOwn

IGESData_ReadAssocs: IGESData_ReadStage = IGESData_ReadStage.IGESData_ReadAssocs

IGESData_ReadProps: IGESData_ReadStage = IGESData_ReadStage.IGESData_ReadProps

IGESData_ReadEnd: IGESData_ReadStage = IGESData_ReadStage.IGESData_ReadEnd

class IGESData_Status(enum.IntEnum):
    IGESData_EntityOK = 0

    IGESData_EntityError = 1

    IGESData_ReferenceError = 2

    IGESData_TypeError = 3

IGESData_EntityOK: IGESData_Status = IGESData_Status.IGESData_EntityOK

IGESData_EntityError: IGESData_Status = IGESData_Status.IGESData_EntityError

IGESData_ReferenceError: IGESData_Status = IGESData_Status.IGESData_ReferenceError

IGESData_TypeError: IGESData_Status = IGESData_Status.IGESData_TypeError

class IGESData:
    """basic description of an IGES Interface"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESData) -> None: ...

    @staticmethod
    def Init() -> None:
        """
        Prepares General dynamic data used for IGESData specifically :
        Protocol and Modules, which treat UndefinedEntity
        """

    @staticmethod
    def Protocol() -> IGESData_Protocol:
        """Returns a Protocol from IGESData (avoids to create it)"""

class IGESData_SpecificLib:
    @overload
    def __init__(self) -> None:
        """
        Creates an empty Library : it will later by filled by method
        AddProtocol
        """

    @overload
    def __init__(self, aprotocol: IGESData_Protocol | None) -> None:
        """
        Creates a Library which complies with a Protocol, that is :
        Same class (criterium IsInstance)
        This creation gets the Modules from the global set, those
        which are bound to the given Protocol and its Resources
        """

    @overload
    def __init__(self, theOther: IGESData_SpecificLib) -> None: ...

    @staticmethod
    def SetGlobal(amodule: IGESData_SpecificModule | None, aprotocol: IGESData_Protocol | None) -> None:
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

    def Select(self, obj: IGESData_IGESEntity | None) -> tuple[bool, IGESData_SpecificModule, int]:
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

    def Module(self) -> IGESData_SpecificModule:
        """Returns the current Module in the Iteration"""

    def Protocol(self) -> IGESData_Protocol:
        """Returns the current Protocol in the Iteration"""

class IGESData_BasicEditor:
    """
    This class provides various functions of basic edition,
    such as :
    - setting header unit (WARNING : DOES NOT convert entities)
    - computation of the status (Subordinate, UseFlag) of entities
    of IGES Entities on a whole model
    - auto correction of IGES Entities, defined both by DirChecker
    and by specific service AutoCorrect
    (this auto correction performs non-ambigious, rather logic,
    editions)
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty Basic Editor which should be initialized via Init() method.
        """

    @overload
    def __init__(self, protocol: IGESData_Protocol | None) -> None:
        """Creates a Basic Editor, with a new IGESModel, ready to run"""

    @overload
    def __init__(self, model: IGESData_IGESModel | None, protocol: IGESData_Protocol | None) -> None:
        """Creates a Basic Editor for IGES Data, ready to run"""

    @overload
    def __init__(self, theOther: IGESData_BasicEditor) -> None: ...

    @overload
    def Init(self, protocol: IGESData_Protocol | None) -> None:
        """Initialize a Basic Editor, with a new IGESModel, ready to run"""

    @overload
    def Init(self, model: IGESData_IGESModel | None, protocol: IGESData_Protocol | None) -> None:
        """Initialize a Basic Editor for IGES Data, ready to run"""

    def Model(self) -> IGESData_IGESModel:
        """Returns the designated model"""

    def SetUnitFlag(self, flag: int) -> bool:
        """
        Sets a new unit from its flag (param 14 of Global Section)
        Returns True if done, False if <flag> is incorrect
        """

    def SetUnitValue(self, val: float) -> bool:
        """
        Sets a new unit from its value in meters (rounded to the
        closest one, max gap 1%)
        Returns True if done, False if <val> is too far from a
        suitable value
        """

    def SetUnitName(self, name: str) -> bool:
        """
        Sets a new unit from its name (param 15 of Global Section)
        Returns True if done, False if <name> is incorrect
        Remark : if <flag> has been set to 3 (user defined), <name>
        is then free
        """

    def ApplyUnit(self, enforce: bool = False) -> None:
        """
        Applies unit value to convert header data : Resolution,
        MaxCoord, MaxLineWeight
        Applies unit only once after SetUnit... has been called,
        if <enforce> is given as True.
        It can be called just before writing the model to a file,
        i.e. when definitive values are finally known
        """

    def ComputeStatus(self) -> None:
        """
        Performs the re-computation of status on the whole model
        (Subordinate Status and Use Flag of each IGES Entity), which
        can have required values according the way they are referenced
        (see definitions of Logical use, Physical use, etc...)
        """

    def AutoCorrect(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Performs auto-correction on an IGESEntity
        Returns True if something has changed, False if nothing done.

        Works with the specific IGES Services : DirChecker which
        allows to correct data in "Directory Part" of Entities (such
        as required values for status, or references to be null), and
        the specific IGES service OwnCorrect, which is specialised for
        each type of entity.
        """

    def AutoCorrectModel(self) -> int:
        """
        Performs auto-correction on the whole Model
        Returns the count of modified entities
        """

    @staticmethod
    def UnitNameFlag(name: str) -> int:
        """
        From the name of unit, computes flag number, 0 if incorrect
        (in this case, user defined entity remains possible)
        """

    @staticmethod
    def UnitFlagValue(flag: int) -> float:
        """From the flag of unit, determines value in MM, 0 if incorrect"""

    @staticmethod
    def UnitFlagName(flag: int) -> str:
        """From the flag of unit, determines its name, "" if incorrect"""

    @staticmethod
    def IGESVersionName(flag: int) -> str:
        """From the flag of IGES version, returns name, "" if incorrect"""

    @staticmethod
    def IGESVersionMax() -> int:
        """Returns the maximum allowed value for IGESVersion Flag"""

    @staticmethod
    def DraftingName(flag: int) -> str:
        """From the flag of drafting standard, returns name, "" if incorrect"""

    @staticmethod
    def DraftingMax() -> int:
        """Returns the maximum allowed value for Drafting Flag"""

    @staticmethod
    def GetFlagByValue(theValue: float) -> int:
        """
        Returns Flag corresponding to the scaling theValue.
        Returns 0 if there's no such flag.
        """

class IGESData_DefSwitch:
    """
    description of a directory component which can be either
    undefined (let Void), defined as a Reference to an entity,
    or as a Rank, integer value addressing a builtin table
    The entity reference is not included here, only reference
    status is kept (because entity type must be adapted)
    """

    @overload
    def __init__(self) -> None:
        """creates a DefSwitch as Void"""

    @overload
    def __init__(self, theOther: IGESData_DefSwitch) -> None: ...

    def SetVoid(self) -> None:
        """sets DefSwitch to "Void" status (in file : Integer = 0)"""

    def SetReference(self) -> None:
        """sets DefSwitch to "Reference" Status (in file : Integer < 0)"""

    def SetRank(self, val: int) -> None:
        """sets DefSwitch to "Rank" with a Value (in file : Integer > 0)"""

    def DefType(self) -> IGESData_DefType:
        """returns DefType status (Void,Reference,Rank)"""

    def Value(self) -> int:
        """returns Value as Integer (sensefull for a Rank)"""

class IGESData_IGESEntity(nanoocp.Standard.Standard_Transient):
    """
    defines root of IGES Entity definition, including Directory
    Part, lists of (optional) Properties and Associativities
    """

    def __init__(self, theOther: IGESData_IGESEntity) -> None: ...

    def IGESType(self) -> IGESData_IGESType:
        """gives IGES typing info (includes "Type" and "Form" data)"""

    def TypeNumber(self) -> int:
        """gives IGES Type Number (often coupled with Form Number)"""

    def FormNumber(self) -> int:
        """
        Returns the form number for that
        type of an IGES entity. The default form number is 0.
        """

    def DirFieldEntity(self, fieldnum: int) -> IGESData_IGESEntity:
        """
        Returns the Entity which has been recorded for a given
        Field Number, i.e. without any cast. Maps with:
        3 : Structure   4 : LineFont     5 : LevelList     6 : View
        7 : Transf(ormation Matrix)      8 : LabelDisplay
        13 : Color.  Other values give a null handle
        It can then be of any kind, while specific items have a Type
        """

    def HasStructure(self) -> bool:
        """
        returns True if an IGESEntity is defined with a Structure
        (it is normally reserved for certain classes, such as Macros)
        """

    def Structure(self) -> IGESData_IGESEntity:
        """
        Returns Structure (used by some types of IGES Entities only)
        Returns a Null Handle if Structure is not defined
        """

    def DefLineFont(self) -> IGESData_DefType:
        """Returns the definition status of LineFont"""

    def RankLineFont(self) -> int:
        """
        Returns LineFont definition as an Integer (if defined as Rank)
        If LineFont is defined as an Entity, returns a negative value
        """

    def LineFont(self) -> IGESData_LineFontEntity:
        """
        Returns LineFont as an Entity (if defined as Reference)
        Returns a Null Handle if DefLineFont is not "DefReference\"
        """

    def DefLevel(self) -> IGESData_DefList:
        """Returns the definition status of Level"""

    def Level(self) -> int:
        """
        Returns the level the entity
        belongs to. Returns -1 if the entity belongs to more than one level.
        """

    def LevelList(self) -> IGESData_LevelListEntity:
        """
        Returns LevelList if Level is
        defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """

    def DefView(self) -> IGESData_DefList:
        """
        Returns the definition status of
        the view. This can be: none, one or several.
        """

    def View(self) -> IGESData_ViewKindEntity:
        """
        Returns the view of this IGES entity.
        This view can be a single view or a list of views.
        Warning A null handle is returned if the view is not defined.
        """

    def SingleView(self) -> IGESData_ViewKindEntity:
        """
        Returns the view as a single view
        if it was defined as such and not as a list of views.
        Warning A null handle is returned if DefView does not have the value DefOne.
        """

    def ViewList(self) -> IGESData_ViewKindEntity:
        """
        Returns the view of this IGES entity as a list.
        Warning A null handle is returned if the
        definition status does not have the value DefSeveral.
        """

    def HasTransf(self) -> bool:
        """Returns True if a Transformation Matrix is defined"""

    def Transf(self) -> IGESData_TransfEntity:
        """
        Returns the Transformation Matrix (under IGES definition)
        Returns a Null Handle if there is none
        for a more complete use, see Location & CompoundLocation
        """

    def HasLabelDisplay(self) -> bool:
        """Returns True if a LabelDisplay mode is defined for this entity"""

    def LabelDisplay(self) -> IGESData_LabelDisplayEntity:
        """
        Returns the Label Display
        Associativity Entity if there is one. Returns a null handle if there is none.
        """

    def BlankStatus(self) -> int:
        """gives Blank Status (0 visible, 1 blanked)"""

    def SubordinateStatus(self) -> int:
        """gives Subordinate Switch (0-1-2-3)"""

    def UseFlag(self) -> int:
        """gives Entity's Use Flag (0 to 5)"""

    def HierarchyStatus(self) -> int:
        """gives Hierarchy status (0-1-2)"""

    def LineWeightNumber(self) -> int:
        """Returns the LineWeight Number (0 not defined), see also LineWeight"""

    def LineWeight(self) -> float:
        """
        Returns the true Line Weight, computed from LineWeightNumber and
        Global Parameter in the Model by call to SetLineWeight
        """

    def DefColor(self) -> IGESData_DefType:
        """Returns the definition status of Color."""

    def RankColor(self) -> int:
        """
        Returns the color definition as
        an integer value if the color was defined as a rank.
        Warning A negative value is returned if the color was defined as an entity.
        """

    def Color(self) -> IGESData_ColorEntity:
        """
        Returns the IGES entity which
        describes the color of the entity.
        Returns a null handle if this entity was defined as an integer.
        """

    def HasShortLabel(self) -> bool:
        """
        Returns true if a short label is defined.
        A short label is a non-blank 8-character string.
        """

    def ShortLabel(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the label value for this IGES entity as a string.
        Warning If the label is blank, this string is null.
        """

    def HasSubScriptNumber(self) -> bool:
        """
        Returns true if a subscript number is defined.
        A subscript number is an integer used to identify a label.
        """

    def SubScriptNumber(self) -> int:
        """
        Returns the integer subscript number used to identify this IGES entity.
        Warning 0 is returned if no subscript number is defined for this IGES entity.
        """

    def InitDirFieldEntity(self, fieldnum: int, ent: IGESData_IGESEntity | None) -> None:
        """
        Initializes a directory field as an Entity of any kind
        See DirFieldEntity for more details
        """

    def InitTransf(self, ent: IGESData_TransfEntity | None) -> None:
        """Initializes Transf, or erases it if <ent> is given Null"""

    def InitView(self, ent: IGESData_ViewKindEntity | None) -> None:
        """Initializes View, or erases it if <ent> is given Null"""

    def InitLineFont(self, ent: IGESData_LineFontEntity | None, rank: int = 0) -> None:
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont,
        else <rank> gives or erases (if zero) RankLineFont
        """

    def InitLevel(self, ent: IGESData_LevelListEntity | None, val: int = 0) -> None:
        """
        Initializes Level : if <ent> is not Null, it gives LevelList,
        else <val> gives or erases (if zero) unique Level
        """

    def InitColor(self, ent: IGESData_ColorEntity | None, rank: int = 0) -> None:
        """
        Initializes Color data : if <ent> is not Null, it gives Color,
        else <rank> gives or erases (if zero) RankColor
        """

    def InitStatus(self, blank: int, subordinate: int, useflag: int, hierarchy: int) -> None:
        """Initializes the Status of Directory Part"""

    def SetLabel(self, label: nanoocp.TCollection.TCollection_HAsciiString | None, sub: int = -1) -> None:
        """
        Sets a new Label to an IGES Entity
        If <sub> is given, it sets value of SubScriptNumber
        else, SubScriptNumber is erased
        """

    def InitMisc(self, str: IGESData_IGESEntity | None, lab: IGESData_LabelDisplayEntity | None, weightnum: int) -> None:
        """
        Initializes various data (those not yet seen above), or erases
        them if they are given as Null (Zero for <weightnum>) :
        <str> for Structure, <lab> for LabelDisplay, and
        <weightnum> for WeightNumber
        """

    def HasOneParent(self) -> bool:
        """
        Returns True if an entity has one and only one parent, defined
        by a SingleParentEntity Type Associativity (explicit sharing).
        Thus, implicit sharing remains defined at model level
        (see class ToolLocation)
        """

    def UniqueParent(self) -> IGESData_IGESEntity:
        """
        Returns the Unique Parent (in the sense given by HasOneParent)
        Error if there is none or several
        """

    def Location(self) -> nanoocp.gp.gp_GTrsf:
        """
        Returns Location given by Transf in Directory Part (see above)
        It must be considered for local definition : if the Entity is
        set in a "Parent", that one can add its one Location, but this
        is not taken in account here : see CompoundLocation for that.
        If no Transf is defined, returns Identity
        If Transf is itself compound, gives the final result
        """

    def VectorLocation(self) -> nanoocp.gp.gp_GTrsf:
        """
        Returns Location considered for Vectors, i.e. without its
        Translation Part. As Location, it gives local definition.
        """

    def CompoundLocation(self) -> nanoocp.gp.gp_GTrsf:
        """
        Returns Location by taking in account a Parent which has its
        own Location : that one will be combined to that of <me>
        The Parent is considered only if HasOneParent is True,
        else it is ignored and CompoundLocation = Location
        """

    def HasName(self) -> bool:
        """
        says if a Name is defined, as Short Label or as Name Property
        (Property is looked first, else ShortLabel is considered)
        """

    def NameValue(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns Name value as a String (Property Name or ShortLabel)
        if SubNumber is defined, it is concatenated after ShortLabel
        as follows label(number). Ignored with a Property Name
        """

    def ArePresentAssociativities(self) -> bool:
        """
        Returns True if the Entity is defined with an Associativity
        list, even empty (that is, file contains its length 0)
        Else, the file contained NO idencation at all about this list.
        """

    def NbAssociativities(self) -> int:
        """gives number of recorded associativities (0 no list defined)"""

    def Associativities(self) -> nanoocp.Interface.Interface_EntityIterator:
        """Returns the Associativity List under the form of an EntityIterator."""

    def NbTypedAssociativities(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """gives how many Associativities have a given type"""

    def TypedAssociativity(self, atype: nanoocp.Standard.Standard_Type | None) -> IGESData_IGESEntity:
        """
        returns the Associativity of a given Type (if only one exists)
        Error if none or more than one
        """

    def Associate(self, ent: IGESData_IGESEntity | None) -> None:
        """Sets "me" in the Associativity list of another Entity"""

    def Dissociate(self, ent: IGESData_IGESEntity | None) -> None:
        """Resets "me" from the Associativity list of another Entity"""

    def ArePresentProperties(self) -> bool:
        """
        Returns True if the Entity is defined with a Property list,
        even empty (that is, file contains its length 0)
        Else, the file contained NO idencation at all about this list
        """

    def NbProperties(self) -> int:
        """Gives number of recorded properties (0 no list defined)"""

    def Properties(self) -> nanoocp.Interface.Interface_EntityIterator:
        """Returns Property List under the form of an EntityIterator"""

    def NbTypedProperties(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """gives how many Properties have a given type"""

    def TypedProperty(self, atype: nanoocp.Standard.Standard_Type | None, anum: int = 0) -> IGESData_IGESEntity:
        """
        returns the Property of a given Type
        Error if none or more than one
        """

    def AddProperty(self, ent: IGESData_IGESEntity | None) -> None:
        """Adds a Property in the list"""

    def RemoveProperty(self, ent: IGESData_IGESEntity | None) -> None:
        """Removes a Property from the list"""

    def SetLineWeight(self, defw: float, maxw: float, gradw: int) -> None:
        """
        computes and sets "true" line weight according IGES rules from
        global data MaxLineWeight (maxv) and LineWeightGrad (gradw),
        or sets it to defw (Default) if LineWeightNumber is null
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_ColorEntity(IGESData_IGESEntity):
    """
    defines required type for Color in directory part
    an effective Color entity must inherits it
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESData_ColorEntity) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_GeneralModule(nanoocp.Interface.Interface_GeneralModule):
    """
    Definition of General Services adapted to IGES.
    This Services comprise : Shared & Implied Lists, Copy, Check
    They are adapted according to the organisation of IGES
    Entities : Directory Part, Lists of Associativities and
    Properties are specifically processed
    """

    def FillSharedCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Fills the list of Entities shared by an IGESEntity <ent>,
        according a Case Number <CN> (formerly computed by CaseNum).
        Considers Properties and Directory Part, and calls
        OwnSharedCase (which is adapted to each Type of Entity)
        """

    def OwnSharedCase(self, CN: int, ent: IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a given IGESEntity <ent>, from
        its specific parameters : specific for each type
        """

    def ListImpliedCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Implied References of <ent>. Here, these are the
        Associativities, plus the Entities defined by OwnSharedCase
        """

    def OwnImpliedCase(self, CN: int, ent: IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Specific list of Entities implied by a given IGESEntity <ent>
        (in addition to Associativities). By default, there are none,
        but this method can be redefined as required
        """

    def CheckCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """
        Semantic Checking of an IGESEntity. Performs general Checks,
        which use DirChecker, then call OwnCheck which does a check
        specific for each type of Entity
        """

    def DirChecker(self, CN: int, ent: IGESData_IGESEntity | None) -> IGESData_DirChecker:
        """
        Returns a DirChecker, specific for each type of Entity
        (identified by its Case Number) : this DirChecker defines
        constraints which must be respected by the DirectoryPart
        """

    def OwnCheckCase(self, CN: int, ent: IGESData_IGESEntity | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check for each type of Entity"""

    def CanCopy(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Specific answer to the question "is Copy properly implemented"
        For IGES, answer is always True
        """

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """Specific creation of a new void entity"""

    def CopyCase(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Copy ("Deep") from <entfrom> to <entto> (same type)
        by using a CopyTool which provides its working Map.
        For IGESEntities, Copies general data (Directory Part, List of
        Properties) and call OwnCopyCase
        """

    def OwnCopyCase(self, CN: int, entfrom: IGESData_IGESEntity | None, entto: IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies parameters which are specific of each Type of Entity"""

    def RenewImpliedCase(self, CN: int, entfrom: nanoocp.Standard.Standard_Transient | None, entto: nanoocp.Standard.Standard_Transient | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Renewing of Implied References.
        For IGESEntities, Copies general data(List of Associativities)
        and calls OwnRenewCase
        """

    def OwnRenewCase(self, CN: int, entfrom: IGESData_IGESEntity | None, entto: IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Renews parameters which are specific of each Type of Entity :
        the provided default does nothing, but this method may be
        redefined as required
        """

    def WhenDeleteCase(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, dispatched: bool) -> None:
        """
        Prepares an IGES Entity for delete : works on directory part
        then calls OwnDeleteCase
        While dispatch requires to copy the entities, <dispatched> is
        ignored, entities are cleared in any case
        """

    def OwnDeleteCase(self, CN: int, ent: IGESData_IGESEntity | None) -> None:
        """
        Specific preparation for delete, acts on own parameters
        Default does nothing, to be redefined as required
        """

    def Name(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the name of an IGES Entity (its NameValue)
        Can be redefined for an even more specific case ...
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_DefaultGeneral(IGESData_GeneralModule):
    """
    Processes the specific case of UndefinedEntity from IGESData
    (Case Number 1)
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a DefaultGeneral and puts it into GeneralLib,
        bound with a Protocol from IGESData
        """

    @overload
    def __init__(self, theOther: IGESData_DefaultGeneral) -> None: ...

    def OwnSharedCase(self, CN: int, ent: IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by an IGESEntity, which must be
        an UndefinedEntity
        """

    def DirChecker(self, CN: int, ent: IGESData_IGESEntity | None) -> IGESData_DirChecker:
        """
        Returns a DirChecker, specific for each type of Entity
        Here, Returns an empty DirChecker (no constraint to check)
        """

    def OwnCheckCase(self, CN: int, ent: IGESData_IGESEntity | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """
        Performs Specific Semantic Check for each type of Entity
        Here, does nothing (no constraint to check)
        """

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """Specific creation of a new void entity (UndefinedEntity only)"""

    def OwnCopyCase(self, CN: int, entfrom: IGESData_IGESEntity | None, entto: IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies parameters which are specific of each Type of Entity"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_SpecificModule(nanoocp.Standard.Standard_Transient):
    """
    This class defines some Services which are specifically
    attached to IGES Entities : Dump
    """

    def OwnDump(self, CN: int, ent: IGESData_IGESEntity | None, dumper: IGESData_IGESDumper, own: int) -> str:
        """
        Specific Dump for each type of IGES Entity : it concerns only
        own parameters, the general data (Directory Part, Lists) are
        taken into account by the IGESDumper
        See class IGESDumper for the rules to follow for <own> and
        <attached> level
        """

    def OwnCorrect(self, CN: int, ent: IGESData_IGESEntity | None) -> bool:
        """
        Specific Automatic Correction on own Parameters of an Entity.
        It works by setting in accordance redundant data, if there are
        when there is no ambiguity (else, it does nothing).
        Remark that classic Corrections on Directory Entry (to set
        void data) are taken into account alsewhere.

        For instance, many "Associativity Entities" have a Number of
        Properties which must have a fixed value.
        Or, a ConicalArc has its Form Number which records the kind of
        Conic, also determined from its coefficients
        But, a CircularArc of which Distances (Center-Start) and
        (Center-End) are not equal cannot be corrected ...

        Returns True if something has been corrected in <ent>
        By default, does nothing. If at least one of the Types
        processed by a sub-class of SpecificModule has a Correct
        procedure attached, this method can be redefined
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_DefaultSpecific(IGESData_SpecificModule):
    """Specific IGES Services for UndefinedEntity, FreeFormatEntity"""

    @overload
    def __init__(self) -> None:
        """Creates a DefaultSpecific and puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESData_DefaultSpecific) -> None: ...

    def OwnDump(self, CN: int, ent: IGESData_IGESEntity | None, dumper: IGESData_IGESDumper, own: int) -> str:
        """
        Specific Dump for UndefinedEntity : it concerns only
        own parameters, the general data (Directory Part, Lists) are
        taken into account by the IGESDumper
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_DirChecker:
    """
    This class centralizes general Checks upon an IGES Entity's
    Directory Part. That is : such field Ignored or Required,
    or Required with a given Value (for an Integer field)
    More precise checks can be performed as necessary, by each
    Entity (method OwnCheck).

    Each class of Entity defines its DirChecker (method DirChecker)
    and the DirChecker is able to perform its Checks on an Entity

    A Required Value or presence of a field causes a Fail Message
    if criterium is not satisfied
    An Ignored field causes a Correction Message if the field is
    not null/zero
    """

    @overload
    def __init__(self) -> None:
        """Returns a DirChecker, with no criterium at all to be checked"""

    @overload
    def __init__(self, atype: int) -> None:
        """Returns a DirChecker, with no criterium except Required Type"""

    @overload
    def __init__(self, atype: int, aform: int) -> None:
        """
        Returns a DirChecker, with no criterium except Required values
        for Type and Form numbers
        """

    @overload
    def __init__(self, atype: int, aform1: int, aform2: int) -> None:
        """
        Returns a DirChecker, with no criterium except Required values
        for Type number (atype), and Required Range for Form number
        (which must be between aform1 and aform2 included)
        """

    @overload
    def __init__(self, theOther: IGESData_DirChecker) -> None: ...

    def IsSet(self) -> bool:
        """
        Returns True if at least one criterium has already been set
        Allows user to store a DirChecker (static variable) then ask
        if it has been set before setting it
        """

    def SetDefault(self) -> None:
        """
        Sets a DirChecker with most current criteria, that is :
        Structure Ignored ( worths call Structure(crit = DefVoid) )
        """

    def Structure(self, crit: IGESData_DefType) -> None:
        """
        Sets Structure criterium.
        If crit is DefVoid, Ignored : should not be defined
        If crit is DefReference, Required : must be defined
        Other values are not taken in account
        """

    def LineFont(self, crit: IGESData_DefType) -> None:
        """
        Sets LineFont criterium
        If crit is DefVoid, Ignored : should not be defined
        If crit is DefAny, Required : must be defined (value or ref)
        If crit is DefValue, Required as a Value (error if Reference)
        Other values are not taken in account
        """

    def LineWeight(self, crit: IGESData_DefType) -> None:
        """
        Sets LineWeight criterium
        If crit is DefVoid, Ignored : should not be defined
        If crit is DefValue, Required
        Other values are not taken in account
        """

    def Color(self, crit: IGESData_DefType) -> None:
        """
        Sets Color criterium
        If crit is DefVoid, Ignored : should not be defined
        If crit is DefAny, Required : must be defined (value or ref)
        Other values are not taken in account
        """

    def GraphicsIgnored(self, hierarchy: int = -1) -> None:
        """
        Sets Graphics data (LineFont, LineWeight, Color, Level, View)
        to be ignored according value of Hierarchy status :
        If hierarchy is not given, they are Ignored any way
        (that is, they should not be defined)
        If hierarchy is given, Graphics are Ignored if the Hierarchy
        status has the value given in argument "hierarchy\"
        """

    def BlankStatusIgnored(self) -> None:
        """
        Sets Blank Status to be ignored
        (should not be defined, or its value should be 0)
        """

    def BlankStatusRequired(self, val: int) -> None:
        """Sets Blank Status to be required at a given value"""

    def SubordinateStatusIgnored(self) -> None:
        """
        Sets Subordinate Status to be ignored
        (should not be defined, or its value should be 0)
        """

    def SubordinateStatusRequired(self, val: int) -> None:
        """Sets Subordinate Status to be required at a given value"""

    def UseFlagIgnored(self) -> None:
        """
        Sets Blank Status to be ignored
        (should not be defined, or its value should be 0)
        """

    def UseFlagRequired(self, val: int) -> None:
        """
        Sets Blank Status to be required at a given value
        Give -1 to demand UseFlag not zero (but no precise value req.)
        """

    def HierarchyStatusIgnored(self) -> None:
        """
        Sets Hierarchy Status to be ignored
        (should not be defined, or its value should be 0)
        """

    def HierarchyStatusRequired(self, val: int) -> None:
        """Sets Hierarchy Status to be required at a given value"""

    def Check(self, ent: IGESData_IGESEntity | None) -> nanoocp.Interface.Interface_Check:
        """
        Performs the Checks on an IGESEntity, according to the
        recorded criteria
        In addition, does minimal Checks, such as admitted range for
        Status, or presence of Error status in some data (Color, ...)
        """

    def CheckTypeAndForm(self, ent: IGESData_IGESEntity | None) -> nanoocp.Interface.Interface_Check:
        """
        Performs a Check only on Values of Type Number and Form Number
        This allows to do a check on an Entity not yet completely
        filled but of which Type and Form Number have been already set
        """

    def Correct(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Corrects the Directory Entry of an IGES Entity as far as it is
        possible according recorded criteria without any ambiguity :
        - if a numeric Status is required a given value, this value is
        enforced
        - if an item is required to be Void, or if it recorded as
        Erroneous, it is cleared (set to Void)
        - Type Number is enforced
        - finally Form Number is enforced only if one and only Value
        is admitted (no range, see Constructors of DirChecker)
        """

class IGESData_DirPart:
    """
    literal/numeric description of an entity's directory section, taken from file
    """

    @overload
    def __init__(self) -> None:
        """creates an empty DirPart, ready to be filled by Init"""

    @overload
    def __init__(self, theOther: IGESData_DirPart) -> None: ...

    def Init(self, i1: int, i2: int, i3: int, i4: int, i5: int, i6: int, i7: int, i8: int, i9: int, i19: int, i11: int, i12: int, i13: int, i14: int, i15: int, i16: int, i17: int, res1: str, res2: str, label: str, subscript: str) -> None:
        """fills DirPart with consistent data read from file"""

    def Type(self) -> IGESData_IGESType:
        """returns "type" and "form" info, used to recognize the entity"""

class IGESData_Protocol(nanoocp.Interface.Interface_Protocol):
    """
    Description of basic Protocol for IGES
    This comprises treatment of IGESModel and Recognition of
    Undefined-FreeFormat-Entity
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESData_Protocol) -> None: ...

    def NbResources(self) -> int:
        """Gives the count of Resource Protocol. Here, none"""

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank. Here, none"""

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a Case Number, specific of each recognized Type
        Here, Undefined and Free Format Entities have the Number 1.
        """

    def NewModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Creates an empty Model for IGES Norm"""

    def IsSuitableModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """Returns True if <model> is a Model of IGES Norm"""

    def UnknownEntity(self) -> nanoocp.Standard.Standard_Transient:
        """Creates a new Unknown Entity for IGES (UndefinedEntity)"""

    def IsUnknownEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e.
        Type UndefinedEntity, status Unknown
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_FileProtocol(IGESData_Protocol):
    """
    This class allows to define complex protocols, in order to
    treat various sub-sets (or the complete set) of the IGES Norm,
    such as Solid + Draw (which are normally independent), etc...
    While it inherits Protocol from IGESData, it admits UndefinedEntity too
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty FileProtocol"""

    @overload
    def __init__(self, theOther: IGESData_FileProtocol) -> None: ...

    def Add(self, protocol: IGESData_Protocol | None) -> None:
        """Adds a resource"""

    def NbResources(self) -> int:
        """Gives the count of Resources : the count of Added Protocols"""

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank (rank of call to Add)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_FileRecognizer(nanoocp.Standard.Standard_Transient):
    def Evaluate(self, akey: IGESData_IGESType) -> tuple[bool, IGESData_IGESEntity]:
        """
        Evaluates if recognition has a result, returns it if yes
        In case of success, Returns True and puts result in "res"
        In case of Failure, simply Returns False
        Works by calling deferred method Eval, and in case of failure,
        looks for Added Recognizers to work
        """

    def Result(self) -> IGESData_IGESEntity:
        """Returns result of last recognition (call of Evaluate)"""

    def Add(self, reco: IGESData_FileRecognizer | None) -> None:
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

class IGESData_UndefinedEntity(IGESData_IGESEntity):
    """
    undefined (unknown or error) entity specific of IGES
    DirPart can be correct or not : if it is not, a flag indicates
    it, and each corrupted field has an associated error flag
    """

    @overload
    def __init__(self) -> None:
        """creates an unknown entity"""

    @overload
    def __init__(self, theOther: IGESData_UndefinedEntity) -> None: ...

    def UndefinedContent(self) -> nanoocp.Interface.Interface_UndefinedContent:
        """Returns own data as an UndefinedContent"""

    def ChangeableContent(self) -> nanoocp.Interface.Interface_UndefinedContent:
        """Returns own data as an UndefinedContent, in order to touch it"""

    def SetNewContent(self, cont: nanoocp.Interface.Interface_UndefinedContent | None) -> None:
        """
        Redefines a completely new UndefinedContent
        Used by a Copy which begins by ShallowCopy, for instance
        """

    def IsOKDirPart(self) -> bool:
        """
        says if DirPart is OK or not (if not, it is erroneous)
        Note that if it is not, Def* methods can return Error status
        """

    def DirStatus(self) -> int:
        """returns Directory Error Status (used for Copy)"""

    def SetOKDirPart(self) -> None:
        """
        Erases the Directory Error Status
        Warning : Be sure that data are consistent to call this method ...
        """

    def DefLineFont(self) -> IGESData_DefType:
        """returns Error status if necessary, else calls original method"""

    def DefLevel(self) -> IGESData_DefList:
        """returns Error status if necessary, else calls original method"""

    def DefView(self) -> IGESData_DefList:
        """returns Error status if necessary, else calls original method"""

    def DefColor(self) -> IGESData_DefType:
        """returns Error status if necessary, else calls original method"""

    def HasSubScriptNumber(self) -> bool:
        """
        returns Error status if necessary, else calls original method
        (that is, if SubScript field is not blank or positive integer)
        """

    def ReadDir(self, IR: IGESData_IGESReaderData | None, DP: IGESData_DirPart) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        Computes the Directory Error Status, to be called before
        standard ReadDir from IGESReaderTool
        Returns True if OK (hence, Directory can be loaded),
        Else returns False and the DirPart <DP> is modified
        (hence, Directory Error Status is non null; and standard Read
        will work with an acceptable DirectoryPart)
        """

    def ReadOwnParams(self, IR: IGESData_IGESReaderData | None, PR: IGESData_ParamReader) -> None:
        """
        reads own parameters from file; PR gives access to them, IR
        detains parameter types and values
        Here, reads all parameters, integers are considered as entity
        reference unless they cannot be; no list interpretation
        No property or associativity list is managed
        """

    def WriteOwnParams(self, IW: IGESData_IGESWriter) -> None:
        """writes parameters to IGESWriter, taken from UndefinedContent"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_FreeFormatEntity(IGESData_UndefinedEntity):
    """
    This class allows to create IGES Entities in a literal form :
    their definition is free, but they are not recognized as
    instances of specific classes.

    This is a way to define test files without having to create
    and fill specific classes of Entities, or creating an IGES
    File ex nihilo, with respect for all format constraints
    (such a way is very difficult to run and to master).

    This class has the same content as an UndefinedEntity, only
    it gives way to act on its content
    """

    @overload
    def __init__(self) -> None:
        """Creates a completely empty FreeFormatEntity"""

    @overload
    def __init__(self, theOther: IGESData_FreeFormatEntity) -> None: ...

    def SetTypeNumber(self, typenum: int) -> None:
        """Sets Type Number to a new Value, and Form Number to Zero"""

    def SetFormNumber(self, formnum: int) -> None:
        """Sets Form Number to a new Value (to called after SetTypeNumber)"""

    def NbParams(self) -> int:
        """Gives count of recorded parameters"""

    def ParamData(self, num: int) -> tuple[bool, nanoocp.Interface.Interface_ParamType, IGESData_IGESEntity, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns data of a Parameter : its type, and the entity if it
        designates en entity ("ent") or its literal value else ("str")
        Returned value (Boolean) : True if it is an Entity, False else
        """

    def ParamType(self, num: int) -> nanoocp.Interface.Interface_ParamType:
        """
        Returns the ParamType of a Param, given its rank
        Error if num is not between 1 and NbParams
        """

    def IsParamEntity(self, num: int) -> bool:
        """
        Returns True if a Parameter is recorded as an entity
        Error if num is not between 1 and NbParams
        """

    def ParamEntity(self, num: int) -> IGESData_IGESEntity:
        """
        Returns Entity corresponding to a Param, given its rank
        Error if out of range or if Param num does not designate
        an Entity
        """

    def IsNegativePointer(self, num: int) -> bool:
        """
        Returns True if <num> is noted as for a "Negative Pointer"
        (see AddEntity for details). Senseful only if IsParamEntity
        answers True for <num>, else returns False.
        """

    def ParamValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns literal value of a Parameter, given its rank
        Error if num is out of range, or if Parameter is not literal
        """

    def NegativePointers(self) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """
        Returns the complete list of Ramks of Parameters which have
        been noted as Negative Pointers
        Warning : It is returned as a Null Handle if none was noted
        """

    @overload
    def AddLiteral(self, ptype: nanoocp.Interface.Interface_ParamType, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Adds a literal Parameter to the list (as such)"""

    @overload
    def AddLiteral(self, ptype: nanoocp.Interface.Interface_ParamType, val: str) -> None:
        """Adds a literal Parameter to the list (builds an HAsciiString)"""

    def AddEntity(self, ptype: nanoocp.Interface.Interface_ParamType, ent: IGESData_IGESEntity | None, negative: bool = False) -> None:
        """
        Adds a Parameter which references an Entity. If the Entity is
        Null, the added parameter will define a "Null Pointer" (0)
        If <negative> is given True, this will command Sending to File
        (see IGESWriter) to produce a "Negative Pointer"
        (Default is False)
        """

    def AddEntities(self, ents: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        Adds a set of Entities, given as a HArray1OfIGESEntity
        Causes creation of : an Integer Parameter which gives count
        of Entities, then the list of Entities of the Array
        Error if an Entity is not an IGESEntity
        All these Entities will be interpreted as "Positive Pointers"
        by IGESWriter
        """

    def AddNegativePointers(self, list: nanoocp.NCollection.NCollection_HSequence[int] | None) -> None:
        """
        Adds a list of Ranks of Parameters to be noted as Negative
        Pointers (this will be taken into account for Parameters
        which are Entities)
        """

    def ClearNegativePointers(self) -> None:
        """
        Clears all information about Negative Pointers, hence every
        Entity kind Parameter will be sent normally, as Positive
        """

    def WriteOwnParams(self, IW: IGESData_IGESWriter) -> None:
        """
        WriteOwnParams is redefined for FreeFormatEntity to take
        into account the supplementary information "Negative Pointer\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_GlobalNodeOfSpecificLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty GlobalNode, with no Next"""

    @overload
    def __init__(self, theOther: IGESData_GlobalNodeOfSpecificLib) -> None: ...

    def Add(self, amodule: IGESData_SpecificModule | None, aprotocol: IGESData_Protocol | None) -> None:
        """
        Adds a Module bound with a Protocol to the list : does
        nothing if already in the list, THAT IS, Same Type (exact
        match) and Same State (that is, IsEqual is not required)
        Once added, stores its attached Protocol in correspondence
        """

    def Module(self) -> IGESData_SpecificModule:
        """Returns the Module stored in a given GlobalNode"""

    def Protocol(self) -> IGESData_Protocol:
        """Returns the attached Protocol stored in a given GlobalNode"""

    def Next(self) -> IGESData_GlobalNodeOfSpecificLib:
        """
        Returns the Next GlobalNode. If none is defined, returned
        value is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_GlobalNodeOfWriterLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty GlobalNode, with no Next"""

    @overload
    def __init__(self, theOther: IGESData_GlobalNodeOfWriterLib) -> None: ...

    def Add(self, amodule: IGESData_ReadWriteModule | None, aprotocol: IGESData_Protocol | None) -> None:
        """
        Adds a Module bound with a Protocol to the list:
        does nothing if already in the list,
        THAT IS, Same Type (exact match) and Same State (that is, IsEqual is not required).
        Once added, stores its attached Protocol in correspondence
        """

    def Module(self) -> IGESData_ReadWriteModule:
        """Returns the Module stored in a given GlobalNode"""

    def Protocol(self) -> IGESData_Protocol:
        """Returns the attached Protocol stored in a given GlobalNode"""

    def Next(self) -> IGESData_GlobalNodeOfWriterLib:
        """
        Returns the Next GlobalNode. If none is defined, returned
        value is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_GlobalSection:
    """
    Description of a global section (corresponds to file header)
    used as well in IGESModel, IGESReader and IGESWriter
    Warning : From IGES-5.1, a parameter is added : LastChangeDate (concerns
    transferred set of data, not the file itself)
    Of course, it can be absent if read from earlier versions
    (a default is then to be set to current date)
    From 5.3, one more : ApplicationProtocol (optional)
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty GlobalSection, ready to be filled,
        Warning : No default value is provided
        """

    @overload
    def __init__(self, theOther: IGESData_GlobalSection) -> None: ...

    def Init(self, params: nanoocp.Interface.Interface_ParamSet | None) -> nanoocp.Interface.Interface_Check:
        """
        Fills GlobalSection from a ParamSet (i.e. taken from file)
        undefined parameters do not change default values when defined
        Fills Check about Corrections or Fails
        """

    def CopyRefs(self) -> None:
        """
        Copies data referenced by Handle (that is, Strings)
        useful to "isolate" a GlobalSection after copy by "="
        (from a Model to another Model for instance)
        """

    def Params(self) -> nanoocp.Interface.Interface_ParamSet:
        """
        Returns all contained data in the form of a ParamSet
        Remark : Strings are given under Hollerith form
        """

    def TranslatedFromHollerith(self, astr: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a string withpout its Hollerith marks (nnnH ahead).
        Remark : all strings stored in GlobalSection are expurged
        from Hollerith information (without nnnH)
        If <astr> is not Hollerith form, it is simply copied
        """

    def Separator(self) -> str:
        """Returns the parameter delimiter character."""

    def EndMark(self) -> str:
        """Returns the record delimiter character."""

    def SendName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the sending system."""

    def FileName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the IGES file."""

    def SystemId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the Native System ID of the system that created the IGES file."""

    def InterfaceVersion(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the pre-processor used to write the IGES file."""

    def IntegerBits(self) -> int:
        """Returns the number of binary bits for integer representations."""

    def MaxPower10Single(self) -> int:
        """
        Returns the maximum power of a decimal representation of a
        single-precision floating point number in the sending system.
        """

    def MaxDigitsSingle(self) -> int: ...

    def MaxPower10Double(self) -> int:
        """
        Returns the maximum power of a decimal representation of a
        double-precision floating point number in the sending system.
        """

    def MaxDigitsDouble(self) -> int: ...

    def ReceiveName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the receiving system."""

    def Scale(self) -> float:
        """Returns the scale used in the IGES file."""

    def CascadeUnit(self) -> float:
        """Returns the system length unit"""

    def UnitFlag(self) -> int:
        """Returns the unit flag that was used to write the IGES file."""

    def UnitName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the unit the IGES file was written in."""

    def LineWeightGrad(self) -> int:
        """Returns the maximum number of line weight gradations."""

    def MaxLineWeight(self) -> float:
        """Returns the of maximum line weight width in IGES file units."""

    def Date(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the IGES file creation date."""

    def Resolution(self) -> float:
        """Returns the resolution used in the IGES file."""

    def MaxCoord(self) -> float:
        """Returns the approximate maximum coordinate value found in the model."""

    def HasMaxCoord(self) -> bool:
        """
        Returns True if the approximate maximum coordinate value found in
        the model is greater than 0.
        """

    def AuthorName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the IGES file author."""

    def CompanyName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the name of the company where the IGES file was written."""

    def IGESVersion(self) -> int:
        """Returns the IGES version that the IGES file was written in."""

    def DraftingStandard(self) -> int: ...

    def LastChangeDate(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the date and time when the model was created or last
        modified (for IGES 5.1 and later).
        """

    def HasLastChangeDate(self) -> bool:
        """
        Returns True if the date and time when the model was created or
        last modified are specified, i.e. not defaulted to NULL.
        """

    @overload
    def SetLastChangeDate(self) -> None: ...

    @overload
    def SetLastChangeDate(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ApplicationProtocol(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasApplicationProtocol(self) -> bool: ...

    @overload
    @staticmethod
    def NewDateString(year: int, month: int, day: int, hour: int, minut: int, second: int, mode: int = -1) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a string built from year,
        month, day, hour, minute and second values. The form of the
        resulting string is defined as follows:
        -      -1: YYMMDD.HHNNSS,
        -       0: YYYYMMDD.HHNNSS,
        -       1: YYYY-MM-DD:HH-NN-SS, where:
        - YYYY or YY is 4 or 2 digit year,
        - HH is hour (00-23),
        - MM is month (01-12),
        - NN is minute (00-59)
        - DD is day (01-31),
        - SS is second (00-59).
        """

    @overload
    @staticmethod
    def NewDateString(date: nanoocp.TCollection.TCollection_HAsciiString | None, mode: int = 1) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Converts the string given in the
        form YYMMDD.HHNNSS or YYYYMMDD.HHNNSS to either
        YYMMDD.HHNNSS, YYYYMMDD.HHNNSS or YYYY-MM-DD:HH-NN-SS.
        """

    def UnitValue(self) -> float:
        """
        Returns the unit value (in
        meters) that the IGES file was written in.
        """

    def SetSeparator(self, val: str) -> None: ...

    def SetEndMark(self, val: str) -> None: ...

    def SetSendName(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetFileName(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetSystemId(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetInterfaceVersion(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetIntegerBits(self, val: int) -> None: ...

    def SetMaxPower10Single(self, val: int) -> None: ...

    def SetMaxDigitsSingle(self, val: int) -> None: ...

    def SetMaxPower10Double(self, val: int) -> None: ...

    def SetMaxDigitsDouble(self, val: int) -> None: ...

    def SetReceiveName(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetCascadeUnit(self, theUnit: float) -> None: ...

    def SetScale(self, val: float) -> None: ...

    def SetUnitFlag(self, val: int) -> None: ...

    def SetUnitName(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetLineWeightGrad(self, val: int) -> None: ...

    def SetMaxLineWeight(self, val: float) -> None: ...

    def SetDate(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetResolution(self, val: float) -> None: ...

    def SetMaxCoord(self, val: float = 0.0) -> None: ...

    def MaxMaxCoord(self, val: float = 0.0) -> None: ...

    def MaxMaxCoords(self, xyz: nanoocp.gp.gp_XYZ) -> None: ...

    def SetAuthorName(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetCompanyName(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetIGESVersion(self, val: int) -> None: ...

    def SetDraftingStandard(self, val: int) -> None: ...

    def SetApplicationProtocol(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

class IGESData_IGESDumper:
    """
    Provides a way to obtain a clear Dump of an IGESEntity
    (distinct from normalized output). It works with tools
    attached to Entities, as for normalized Reade and Write

    For each Entity, displaying data is split in own data
    (specific to each type) and other attached data, which are
    defined for all IGES Types (either from "Directory Entry" or
    from Lists of Associativities and Properties)
    """

    @overload
    def __init__(self, model: IGESData_IGESModel | None, protocol: IGESData_Protocol | None) -> None:
        """
        Returns an IGESDumper ready to work.
        The IGESModel provides the numbering of Entities:
        as for any InterfaceModel, it gives each Entity a number;
        but for IGESEntities, the "Number of Directory Entry"
        according to the definition of IGES Files, is also useful.
        """

    @overload
    def __init__(self, theOther: IGESData_IGESDumper) -> None: ...

    def PrintDNum(self, ent: IGESData_IGESEntity | None) -> str:
        """
        Prints onto an output, the "Number of Directory Entry" which
        corresponds to an IGESEntity in the IGESModel, under the form
        "D#nnn" (a Null Handle gives D#0)
        """

    def PrintShort(self, ent: IGESData_IGESEntity | None) -> str:
        """
        Prints onto an output, the "Number of Directory Entry" (see
        PrintDNum) plus IGES Type and Form Numbers, which gives
        "D#nnn  Type nnn  Form nnn\"
        """

    def Dump(self, ent: IGESData_IGESEntity | None, own: int, attached: int = -1) -> str: ...

    def OwnDump(self, ent: IGESData_IGESEntity | None, own: int) -> str:
        """
        Specific Dump for each IGES Entity, call by Dump (just above)
        <own> is the parameter <own> from Dump
        """

class IGESData_IGESModel(nanoocp.Interface.Interface_InterfaceModel):
    """
    Defines the file header and
    entities for IGES files. These headers and entities result from
    a complete data translation using the IGES data exchange processor.
    Each entity is contained in a single model only and has a
    unique identifier. You can access this identifier using the method Number.
    Gives an access to the general data in the Start and the Global
    sections of an IGES file.
    The IGES file includes the following sections:
    -Start,
    -Global,
    -Directory Entry,
    -Parameter Data,
    -Terminate
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESData_IGESModel) -> None: ...

    def ClearHeader(self) -> None:
        """Erases all data specific to IGES file Header (Start + Global)"""

    def DumpHeader(self, level: int = 0) -> str:
        """
        Prints the IGES file header
        (Start and Global Sections) to the log file. The integer
        parameter is intended to be used as a level indicator but is not used at present.
        """

    def StartSection(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns Model's Start Section (list of comment lines)"""

    def NbStartLines(self) -> int:
        """Returns the count of recorded Start Lines"""

    def StartLine(self, num: int) -> str:
        """
        Returns a line from the IGES file
        Start section by specifying its number. An empty string is
        returned if the number given is out of range, the range being
        from 1 to NbStartLines.
        """

    def ClearStartSection(self) -> None:
        """Clears the IGES file Start Section"""

    def SetStartSection(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None, copy: bool = True) -> None:
        """
        Sets a new Start section from a list of strings.
        If copy is false, the Start section will be shared. Any
        modifications made to the strings later on, will have an effect on
        the Start section. If copy is true (default value),
        an independent copy of the strings is created and used as
        the Start section. Any modifications made to the strings
        later on, will have no effect on the Start section.
        """

    def AddStartLine(self, line: str, atnum: int = 0) -> None:
        """
        Adds a new string to the existing
        Start section at the end if atnum is 0 or not given, or before
        atnumth line.
        """

    def GlobalSection(self) -> IGESData_GlobalSection:
        """Returns the Global section of the IGES file."""

    def ChangeGlobalSection(self) -> IGESData_GlobalSection:
        """Returns the Global section of the IGES file."""

    def SetGlobalSection(self, header: IGESData_GlobalSection) -> None:
        """Sets the Global section of the IGES file."""

    def ApplyStatic(self, param: str = '') -> bool:
        """
        Sets some of the Global section
        parameters with the values defined by the translation
        parameters. param may be:
        - receiver (value read in XSTEP.iges.header.receiver),
        - author (value read in XSTEP.iges.header.author),
        - company (value read in XSTEP.iges.header.company).
        The default value for param is an empty string.
        Returns True when done and if param is given, False if param is
        unknown or empty. Note: Set the unit in the IGES
        file Global section via IGESData_BasicEditor class.
        """

    def Entity(self, num: int) -> IGESData_IGESEntity:
        """Returns an IGES entity given by its rank number."""

    def DNum(self, ent: IGESData_IGESEntity | None) -> int:
        """
        Returns the equivalent DE Number for an Entity, i.e.
        2*Number(ent)-1 , or 0 if <ent> is unknown from <me>
        This DE Number is used for File Writing for instance
        """

    def GetFromAnother(self, other: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """gets Header (GlobalSection) from another Model"""

    def NewEmptyModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns a New Empty Model, same type as <me> i.e. IGESModel"""

    def VerifyCheck(self) -> nanoocp.Interface.Interface_Check:
        """
        Checks that the IGES file Global
        section contains valid data that conforms to the IGES specifications.
        """

    def SetLineWeights(self, defw: float) -> None:
        """
        Sets LineWeights of contained Entities according header data
        (MaxLineWeight and LineWeightGrad) or to a default value for
        undefined weights
        """

    def ClearLabels(self) -> None:
        """erases specific labels, i.e. does nothing"""

    def PrintLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints label specific to IGES norm for a given entity, i.e.
        its directory entry number (2*Number-1)
        """

    def PrintToLog(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints label specific to IGES norm for a given -- --
        entity, i.e. its directory entry number (2*Number-1)
        in the log file format.
        """

    def PrintInfo(self, ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Prints label specific to IGES norm for a given entity, i.e.
        its directory entry number (2*Number-1)
        """

    def StringLabel(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns a string with the label attached to a given entity,
        i.e. a string "Dnn" with nn = directory entry number (2*N-1)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_IGESType:
    """
    taken from directory part of an entity (from file or model),
    gives "type" and "form" data, used to recognize entity's type
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, atype: int, aform: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESData_IGESType) -> None: ...

    def Type(self) -> int:
        """returns "type" data"""

    def Form(self) -> int:
        """returns "form" data"""

    def IsEqual(self, another: IGESData_IGESType) -> bool:
        """compares two IGESTypes, avoiding comparing their fields"""

    def __eq__(self, another: IGESData_IGESType) -> bool: ...

    def Nullify(self) -> None:
        """resets fields (useful when an IGESType is stored as mask)"""

class IGESData_IGESReaderData(nanoocp.Interface.Interface_FileReaderData):
    """
    specific FileReaderData for IGES
    contains header as GlobalSection, and for each Entity, its
    directory part as DirPart, list of Parameters as ParamSet
    Each Item has a DirPart, plus classically a ParamSet and the
    correspondent recognized Entity (inherited from FileReaderData)
    Parameters are accessed through specific objects, ParamReaders
    """

    @overload
    def __init__(self, nbe: int, nbp: int) -> None:
        """
        creates IGESReaderData correctly dimensioned (for arrays)
        <nbe> count of entities, that is, half nb of directory lines
        <nbp> : count of parameters
        """

    @overload
    def __init__(self, theOther: IGESData_IGESReaderData) -> None: ...

    def AddStartLine(self, aval: str) -> None:
        """adds a start line to start section"""

    def StartSection(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns the Start Section in once"""

    def AddGlobal(self, atype: nanoocp.Interface.Interface_ParamType, aval: str) -> None:
        """adds a parameter to global section's parameter list"""

    def SetGlobalSection(self) -> None:
        """
        reads header (as GlobalSection) content from the ParamSet
        after it has been filled by successive calls to AddGlobal
        """

    def GlobalSection(self) -> IGESData_GlobalSection:
        """returns header as GlobalSection"""

    def SetDirPart(self, num: int, i1: int, i2: int, i3: int, i4: int, i5: int, i6: int, i7: int, i8: int, i9: int, i10: int, i11: int, i12: int, i13: int, i14: int, i15: int, i16: int, i17: int, res1: str, res2: str, label: str, subs: str) -> None:
        """
        fills a DirPart, designated by its rank (that is, (N+1)/2 if N
        is its first number in section D)
        """

    def DirPart(self, num: int) -> IGESData_DirPart:
        """returns DirPart identified by record no (half Dsect number)"""

    def DirType(self, num: int) -> IGESData_IGESType:
        """returns "type" and "form" info from a directory part"""

    def NbEntities(self) -> int:
        """Returns count of recorded Entities (i.e. size of Directory)"""

    def FindNextRecord(self, num: int) -> int:
        """
        determines next suitable record from num; that is num+1 except
        for last one which gives 0
        """

    def SetEntityNumbers(self) -> None:
        """
        determines reference numbers in EntityNumber fields (called by
        SetEntities from IGESReaderTool)
        works on "Integer" type Parameters, because IGES does not
        distinguish Integer and Entity Refs : every Integer which is
        odd and less than twice NbRecords can be an Entity Ref ...
        (Ref Number is then (N+1)/2 if N is the Integer Value)
        """

    def GlobalCheck(self) -> nanoocp.Interface.Interface_Check:
        """Returns the recorded Global Check"""

    def SetDefaultLineWeight(self, defw: float) -> None:
        """
        allows to set a default line weight, will be later applied at
        load time, on Entities which have no specified line weight
        """

    def DefaultLineWeight(self) -> float:
        """
        Returns the recorded Default Line Weight, if there is
        (else, returns 0)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_IGESReaderTool(nanoocp.Interface.Interface_FileReaderTool):
    """
    specific FileReaderTool for IGES
    Parameters are accessed through specific objects, ParamReaders
    """

    @overload
    def __init__(self, reader: IGESData_IGESReaderData | None, protocol: IGESData_Protocol | None) -> None:
        """
        creates IGESReaderTool to work with an IGESReaderData and an
        IGES Protocol.
        Actually, no Lib is used
        """

    @overload
    def __init__(self, theOther: IGESData_IGESReaderTool) -> None: ...

    def Prepare(self, reco: IGESData_FileRecognizer | None) -> None:
        """
        binds empty entities to records, works with the Protocol
        (from IGESData) stored and later used
        RQ : Actually, sets DNum into IGES Entities
        Also loads the list of parameters for ParamReader
        """

    def Recognize(self, num: int) -> tuple[bool, nanoocp.Interface.Interface_Check, nanoocp.Standard.Standard_Transient]:
        """recognizes records by asking Protocol (on data of DirType)"""

    def BeginRead(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """fills model's header, that is, its GlobalSection"""

    def AnalyseRecord(self, num: int, anent: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Interface.Interface_Check]:
        """
        fills an entity, given record no; works by calling ReadDirPart
        then ReadParams (with help of a ParamReader), then if required
        ReadProps and ReadAssocs, from IGESEntity
        Returns True if no fail has been recorded
        """

    def EndRead(self, amodel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """after reading entities, true line weights can be computed"""

    def ReadDir(self, ent: IGESData_IGESEntity | None, IR: IGESData_IGESReaderData | None, DP: IGESData_DirPart) -> nanoocp.Interface.Interface_Check:
        """
        Reads directory part components from file; DP is the literal
        directory part, IR detains entities referenced by DP
        """

    def ReadOwnParams(self, ent: IGESData_IGESEntity | None, IR: IGESData_IGESReaderData | None, PR: IGESData_ParamReader) -> None:
        """
        Performs Reading of own Parameters for each IGESEntity
        Works with the ReaderLib loaded with ReadWriteModules for IGES
        In case of failure, tries UndefinedEntity from IGES
        """

    def ReadProps(self, ent: IGESData_IGESEntity | None, IR: IGESData_IGESReaderData | None, PR: IGESData_ParamReader) -> None:
        """
        Reads Property List, if there is (if not, does nothing)
        criterium is : current parameter of PR remains inside params
        list, and Stage is "Own"
        Current parameter must be a positive integer, which value
        gives the length of the list; else, a Fail is produced (into
        Check of PR) and reading process is stopped
        """

    def ReadAssocs(self, ent: IGESData_IGESEntity | None, IR: IGESData_IGESReaderData | None, PR: IGESData_ParamReader) -> None:
        """
        Reads Associativity List, if there is (if not, does nothing)
        criterium is : current parameter of PR remains inside params
        list, and Stage is "Own"
        Same conditions as above; in addition, no parameter must be
        let after the list once read
        Note that "Associated" entities are not declared "Shared\"
        """

class IGESData_IGESWriter:
    """
    manages atomic file writing, under control of IGESModel :
    prepare text to be sent then sends it
    takes into account distinction between successive Sections
    """

    @overload
    def __init__(self) -> None:
        """Default constructor (not used) to satisfy the compiler"""

    @overload
    def __init__(self, amodel: IGESData_IGESModel | None) -> None:
        """
        Creates an IGESWriter, empty ready to work
        (see the methods SendModel and Print)
        """

    @overload
    def __init__(self, other: IGESData_IGESWriter) -> None:
        """Constructor by copy (not used) to satisfy the compiler"""

    def FloatWriter(self) -> nanoocp.Interface.Interface_FloatWriter:
        """
        Returns the embedded FloatWriter, which controls sending Reals
        Use this method to access FloatWriter in order to consult or
        change its options (MainFormat, FormatForRange,ZeroSuppress),
        because it is returned as the address of its field
        """

    def WriteMode(self) -> int:
        """
        Returns the write mode, in order to be read and/or changed
        Write Mode controls the way final print works
        0 (D) : Normal IGES, 10 : FNES
        """

    def SetWriteMode(self, theValue: int) -> None:
        """
        Python addition: sets the value WriteMode() returns by reference in C++.
        """

    def SendStartLine(self, startline: str) -> None:
        """
        Sends an additional Starting Line : this is the way used to
        send comments in an IGES File (at beginning of the file).
        If the line is more than 72 chars long, it is split into
        as many lines as required to send it completely
        """

    def SendModel(self, protocol: IGESData_Protocol | None) -> None:
        """
        Sends the complete IGESModel (Global Section, Entities as
        Directory Entries & Parameter Lists, etc...)
        i.e. fills a list of texts. Once filled, it can be sent by
        method Print
        """

    def SectionS(self) -> None:
        """
        declares sending of S section (only a declaration)
        error if state is not initial
        """

    def SectionG(self, header: IGESData_GlobalSection) -> None:
        """
        prepares sending of header, from a GlobalSection (stores it)
        error if SectionS was not called just before
        takes in account special characters (Separator, EndMark)
        """

    def SectionsDP(self) -> None:
        """
        prepares sending of list of entities, as Sections D (directory
        list) and P (Parameters lists, one per entity)
        Entities will be then processed, one after the other
        error if SectionG has not be called just before
        """

    def SectionT(self) -> None:
        """
        declares sending of T section (only a declaration)
        error if does not follow Entities sending
        """

    def DirPart(self, anent: IGESData_IGESEntity | None) -> None:
        """
        translates directory part of an Entity into a literal DirPart
        Some infos are computed after sending parameters
        Error if not in sections DP or Stage not "Dir\"
        """

    def OwnParams(self, anent: IGESData_IGESEntity | None) -> None:
        """
        sends own parameters of the entity, by sending firstly its
        type, then calling specific method WriteOwnParams
        Error if not in sections DP or Stage not "Own\"
        """

    def Associativities(self, anent: IGESData_IGESEntity | None) -> None:
        """
        sends associativity list, as complement of parameters list
        error if not in sections DP or Stage not "Associativity\"
        """

    def Properties(self, anent: IGESData_IGESEntity | None) -> None:
        """
        sends property list, as complement of parameters list
        error if not in sections DP or Stage not "Property\"
        """

    def EndEntity(self) -> None:
        """declares end of sending an entity (ends param list by ';')"""

    def SendVoid(self) -> None:
        """sends a void parameter, that is null text"""

    @overload
    def Send(self, val: int) -> None:
        """sends an Integer parameter"""

    @overload
    def Send(self, val: float) -> None:
        """sends a Real parameter. Works with FloatWriter"""

    @overload
    def Send(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """sends a Text parameter under Hollerith form"""

    @overload
    def Send(self, val: IGESData_IGESEntity | None, negative: bool = False) -> None:
        """
        sends a Reference to an Entity (if its Number is N, its
        pointer is 2*N-1)
        If <val> is Null, "0" will be sent
        If <negative> is True, "Pointer" is sent as negative
        """

    @overload
    def Send(self, val: nanoocp.gp.gp_XY) -> None:
        """Sends a XY, interpreted as a couple of 2 Reals (X & Y)"""

    @overload
    def Send(self, val: nanoocp.gp.gp_XYZ) -> None:
        """Sends a XYZ, interpreted as a couple of 2 Reals (X , Y & Z)"""

    def SendBoolean(self, val: bool) -> None:
        """sends a Boolean parameter as an Integer value 0(False)/1(True)"""

    def SendString(self, val: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """sends a parameter under its exact form given as a string"""

    def SectionStrings(self, numsec: int) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns the list of strings for a section given its rank
        1 : Start (if not empty)  2 : Global  3 or 4 : Parameters
        RQ: no string list for Directory section
        An empty section gives a null handle
        """

    def Print(self) -> tuple[bool, str]:
        """
        Writes result on an output defined as an OStream
        resolves stored infos at this time; in particular, numbers of
        lines used to address P-section from D-section and final totals
        Takes WriteMode into account
        """

class IGESData_LabelDisplayEntity(IGESData_IGESEntity):
    """
    defines required type for LabelDisplay in directory part
    an effective LabelDisplay entity must inherits it
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESData_LabelDisplayEntity) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_LevelListEntity(IGESData_IGESEntity):
    """
    defines required type for LevelList in directory part
    an effective LevelList entity must inherits it
    """

    def NbLevelNumbers(self) -> int:
        """Must return the count of levels"""

    def LevelNumber(self, num: int) -> int:
        """
        returns the Level Number of <me>, indicated by <num>
        raises an exception if num is out of range
        """

    def HasLevelNumber(self, level: int) -> bool:
        """returns True if <level> is in the list"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_LineFontEntity(IGESData_IGESEntity):
    """
    defines required type for LineFont in directory part
    an effective LineFont entity must inherits it
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESData_LineFontEntity) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_NameEntity(IGESData_IGESEntity):
    """
    a NameEntity is a kind of IGESEntity which can provide a Name
    under alphanumeric (String) form, from Properties list
    an effective Name entity must inherit it
    """

    def Value(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Retyrns the alphanumeric value of the Name, to be defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_NodeOfSpecificLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty Node, with no Next"""

    @overload
    def __init__(self, theOther: IGESData_NodeOfSpecificLib) -> None: ...

    def AddNode(self, anode: IGESData_GlobalNodeOfSpecificLib | None) -> None:
        """
        Adds a couple (Module,Protocol), that is, stores it into
        itself if not yet done, else creates a Next Node to do it
        """

    def Module(self) -> IGESData_SpecificModule:
        """Returns the Module designated by a precise Node"""

    def Protocol(self) -> IGESData_Protocol:
        """Returns the Protocol designated by a precise Node"""

    def Next(self) -> IGESData_NodeOfSpecificLib:
        """
        Returns the Next Node. If none was defined, returned value
        is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_NodeOfWriterLib(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Creates an empty Node, with no Next"""

    @overload
    def __init__(self, theOther: IGESData_NodeOfWriterLib) -> None: ...

    def AddNode(self, anode: IGESData_GlobalNodeOfWriterLib | None) -> None:
        """
        Adds a couple (Module,Protocol), that is, stores it into
        itself if not yet done, else creates a Next Node to do it
        """

    def Module(self) -> IGESData_ReadWriteModule:
        """Returns the Module designated by a precise Node"""

    def Protocol(self) -> IGESData_Protocol:
        """Returns the Protocol designated by a precise Node"""

    def Next(self) -> IGESData_NodeOfWriterLib:
        """
        Returns the Next Node. If none was defined, returned value
        is a Null Handle
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_ParamCursor:
    """
    Auxiliary class for ParamReader.
    It stores commands for a ParamReader to manage the current
    parameter number. Used by methods Read... from ParamReader.
    It allows to define the following commands :
    - read a parameter specified by a precise Number (basic case)
    - read a parameter then set Current Number to follow its number
    - read the current parameter (with Current Number) then
    advance Current Number by one
    - idem with several : read "nb" parameters from one specified,
    included, with or without setting Current Number to follow
    last parameter read
    - read several parameter from the current one, then advance
    Current Number to follow the last one read
    - Read several parameters (as above) but in interlaced lists,
    i.e. from complex items (each one including successively for
    instance, an Integer, a Real, an Entity ...)

    If commands to advance Current Number are not set, it must be
    set by the user (with method SetCurrent from ParamReader)
    ParamReader offers methods which create most useful cases
    """

    @overload
    def __init__(self, num: int) -> None:
        """
        Creates a Cursor to read a precise parameter of ParamReader,
        identified by its number, then set Current Number to "num + 1"
        (this constructor allows to simply give a Number to a method
        Read... from ParamReader, which will be translated into a
        ParamCursor by compiler)
        """

    @overload
    def __init__(self, num: int, nb: int, size: int = 1) -> None:
        """
        Creates a Cursor to read a list of parameters (count "nb")
        starting from a precise one (number "num") included, then
        set Current Number of ParamNumber to the first following one
        ("num + nb")
        If size is given, it means that each parameter is made of more
        than one term. One term is the normal (default) case : for
        instance, a Parameter comprises one Integer, or one Entity ...
        Size gives the complete size of each Item if it is complex.
        To be used ONLY IF it is constant
        """

    @overload
    def __init__(self, theOther: IGESData_ParamCursor) -> None: ...

    def SetTerm(self, size: int, autoadv: bool = True) -> None:
        """
        Defines the size of a term to read in the item : this commands
        ParamReader to read "size" parameters for each item, then
        skip the remainder of the item to the same term of next Item
        (that is, skip "item size" - "term size")

        In addition, Offset from beginning of Item is managed :
        After being created, and for the first call to SetTerm, the
        part of Item to be read begins exactly as the Item begins
        But after a SetTerm, the next read will add an offset which is
        the size of former term.

        autoadv commands Advance management. If it is True (default),
        the last SetTerm (Item size has been covered) calls SetAdvance
        If it is False, SetAdvance must be called directly if necessary

        Error if a SetTerm overpasses the size of the Item
        """

    def SetOne(self, autoadv: bool = True) -> None:
        """Defines a term of one Parameter (very current case)"""

    def SetXY(self, autoadv: bool = True) -> None:
        """Defines a term of two Parameters for a XY (current case)"""

    def SetXYZ(self, autoadv: bool = True) -> None:
        """Defines a term of three Parameters for XYZ (current case)"""

    def SetAdvance(self, advance: bool) -> None:
        """
        Changes command to advance current cursor after reading
        parameters. If "advance" True, sets advance, if "False",
        resets it. ParamCursor is created by default with True.
        """

    def Start(self) -> int:
        """Returns (included) starting number for reading parameters"""

    def Limit(self) -> int:
        """Returns (excluded) upper limit number for reading parameters"""

    def Count(self) -> int:
        """Returns required count of items to be read"""

    def ItemSize(self) -> int:
        """Returns length of item (count of parameters per item)"""

    def TermSize(self) -> int:
        """Returns length of current term (count of parameters) in item"""

    def Offset(self) -> int:
        """Returns offset from which current term must be read in item"""

    def Advance(self) -> bool:
        """Returns True if Advance command has been set"""

class IGESData_ParamReader:
    """
    access to a list of parameters, with management of read stage
    (owned parameters, properties, associativities) and current
    parameter number, read errors (which feed a Check), plus
    convenient facilities to read parameters, in particular :
    - first parameter is ignored (it repeats entity type), hence
    number 1 gives 2nd parameter, etc...
    - lists are not explicit, list-reading methods are provided
    which manage a current param. number
    - interpretation is made as possible (texts, reals, entities ...)
    (in particular, Reading a Real accepts an Integer)
    """

    @overload
    def __init__(self, list: nanoocp.Interface.Interface_ParamList | None, ach: nanoocp.Interface.Interface_Check | None, base: int = 1, nbpar: int = 0, num: int = 0) -> None:
        """
        Prepares a ParamReader, stage "Own", current param = 1
        It considers a part of the list, from <base> (excluded) for
        <nbpar> parameters; <nbpar> = 0 commands to take list length.
        Default is (1 to skip type)
        """

    @overload
    def __init__(self, theOther: IGESData_ParamReader) -> None: ...

    def EntityNumber(self) -> int:
        """Returns the entity number in the file"""

    def Clear(self) -> None:
        """resets state (stage, current param number, check with no fail)"""

    def CurrentNumber(self) -> int:
        """
        returns the current parameter number
        This notion is involved by the organisation of an IGES list of
        parameters: it can be ended by two lists (Associativities and
        Properties), which can be empty, or even absent. Hence, it is
        necessary to know, at the end of specific reading, how many
        parameters have been read : the optional lists follow
        """

    def SetCurrentNumber(self, num: int) -> None:
        """
        sets current parameter number to a new value
        must be done at end of each step : set on first parameter
        following last read one; is done by some Read... methods
        (must be done directly if these method are not used)
        num greater than NbParams means that following lists are empty
        If current num is not managed, it remains at 1, which probably
        will cause error when successive steps of reading are made
        """

    def Stage(self) -> IGESData_ReadStage:
        """gives current stage (Own-Props-Assocs-End, begins at Own)"""

    def NextStage(self) -> None:
        """passes to next stage (must be linked with setting Current)"""

    def EndAll(self) -> None:
        """passes directly to the end of reading process"""

    def NbParams(self) -> int:
        """
        returns number of parameters (minus the first one)
        following method skip the first parameter (1 gives the 2nd)
        """

    def ParamType(self, num: int) -> nanoocp.Interface.Interface_ParamType:
        """
        returns type of parameter; note that "Ident" or "Sub" cannot
        be encountered, they correspond to "Integer", see also below
        """

    def ParamValue(self, num: int) -> str:
        """returns literal value of a parameter, as it was in file"""

    def IsParamDefined(self, num: int) -> bool:
        """
        says if a parameter is defined (not void)
        See also DefinedElseSkip
        """

    def IsParamEntity(self, num: int) -> bool:
        """
        says if a parameter can be regarded as an entity reference
        (see Prepare from IGESReaderData for more explanation)
        Note that such a parameter can seen as be a plain Integer too
        """

    def ParamNumber(self, num: int) -> int:
        """
        returns entity number corresponding to a parameter if there is
        otherwise zero (according criterium IsParamEntity)
        """

    def ParamEntity(self, IR: IGESData_IGESReaderData | None, num: int) -> IGESData_IGESEntity:
        """directly returns entity referenced by a parameter"""

    def Current(self) -> IGESData_ParamCursor:
        """
        Creates a ParamCursor from the Current Number, to read one
        parameter, and to advance Current Number after reading
        """

    def CurrentList(self, nb: int, size: int = 1) -> IGESData_ParamCursor:
        """
        Creates a ParamCursor from the Current Number, to read a list
        of "nb" items, and to advance Current Number after reading
        By default, each item is made of one parameter
        If size is given, it precises the number of params per item
        """

    def DefinedElseSkip(self) -> bool:
        """
        Allows to simply process a parameter which can be defaulted.
        Waits on the Current Number a defined parameter or skips it :
        If the parameter <num> is defined, changes nothing and returns True
        Hence, the next reading with current cursor will concern <num>
        If it is void, advances Current Position by one, and returns False
        The next reading will concern <num+1> (except if <num> = NbParams)

        This allows to process Default values as follows (C++) :
        if (PR.DefinedElseSkip()) {
        .. PR.Read... (current parameter);
        } else {
        <current parameter> = default value
        .. nothing else to do with ParamReader
        }
        For Message
        """

    @overload
    def ReadInteger(self, PC: IGESData_ParamCursor) -> tuple[bool, int]: ...

    @overload
    def ReadInteger(self, PC: IGESData_ParamCursor, mess: str) -> tuple[bool, int]:
        """
        Reads an Integer value designated by PC
        The method Current designates the current parameter and
        advances the Current Number by one after reading
        Note that if a count (not 1) is given, it is ignored
        If it is not an Integer, fills Check with a Fail (using mess)
        and returns False
        """

    @overload
    def ReadBoolean(self, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, exact: bool = True) -> tuple[bool, bool]: ...

    @overload
    def ReadBoolean(self, PC: IGESData_ParamCursor, mess: str, exact: bool = True) -> tuple[bool, bool]:
        """
        Reads a Boolean value from parameter "num"
        A Boolean is given as an Integer value 0 (False) or 1 (True)
        Anyway, an Integer is demanded (else, Check is filled)
        If exact is given True, those precise values are demanded
        Else, Correction is done, as False for 0 or <0, True for >0
        (with a Warning error message, and return is True)
        In case of error (not an Integer, or not 0/1 and exact True),
        Check is filled with a Fail (using mess) and return is False
        """

    @overload
    def ReadReal(self, PC: IGESData_ParamCursor) -> tuple[bool, float]: ...

    @overload
    def ReadReal(self, PC: IGESData_ParamCursor, mess: str) -> tuple[bool, float]:
        """
        Reads a Real value from parameter "num"
        An Integer is accepted (Check is filled with a Warning
        message) and causes return to be True (as normal case)
        In other cases, Check is filled with a Fail and return is False
        """

    @overload
    def ReadXY(self, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, val: nanoocp.gp.gp_XY) -> bool: ...

    @overload
    def ReadXY(self, PC: IGESData_ParamCursor, mess: str, val: nanoocp.gp.gp_XY) -> bool:
        """
        Reads a couple of Real values (X,Y) from parameter "num"
        Integers are accepted (Check is filled with a Warning
        message) and cause return to be True (as normal case)
        In other cases, Check is filled with a Fail and return is False
        """

    @overload
    def ReadXYZ(self, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, val: nanoocp.gp.gp_XYZ) -> bool: ...

    @overload
    def ReadXYZ(self, PC: IGESData_ParamCursor, mess: str, val: nanoocp.gp.gp_XYZ) -> bool:
        """
        Reads a triplet of Real values (X,Y,Z) from parameter "num"
        Integers are accepted (Check is filled with a Warning
        message) and cause return to be True (as normal case)
        In other cases, Check is filled with a Fail and return is False
        For Message
        """

    @overload
    def ReadText(self, thePC: IGESData_ParamCursor, theMsg: nanoocp.Message.Message_Msg) -> tuple[bool, nanoocp.TCollection.TCollection_HAsciiString]: ...

    @overload
    def ReadText(self, PC: IGESData_ParamCursor, mess: str) -> tuple[bool, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Reads a Text value from parameter "num", as a String from
        Collection, that is, Hollerith text without leading "nnnH"
        If it is not a String, fills Check with a Fail (using mess)
        and returns False
        """

    @overload
    def ReadEntity(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, canbenul: bool = False) -> tuple[bool, IGESData_Status, IGESData_IGESEntity]: ...

    @overload
    def ReadEntity(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, mess: str, canbenul: bool = False) -> tuple[bool, IGESData_IGESEntity]:
        """
        Reads an IGES entity from parameter "num"
        An Entity is known by its reference, which has the form of an
        odd Integer Value (a number in the Directory)
        If <canbenul> is given True, a Reference can also be Null :
        in this case, the result is a Null Handle with no Error
        If <canbenul> is False, a Null Reference causes an Error
        If the parameter cannot refer to an entity (or null), fills
        Check with a Fail (using mess) and returns False
        """

    @overload
    def ReadEntity(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, type: nanoocp.Standard.Standard_Type | None, canbenul: bool = False) -> tuple[bool, IGESData_Status, IGESData_IGESEntity]: ...

    @overload
    def ReadEntity(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, mess: str, type: nanoocp.Standard.Standard_Type | None, canbenul: bool = False) -> tuple[bool, IGESData_IGESEntity]:
        """
        Works as ReadEntity without Type, but in addition checks the
        Type of the Entity, which must be "kind of" a given <type>
        Then, gives the same fail cases as ReadEntity without Type,
        plus the case "Incorrect Type"
        (in such a case, returns False and givel <val> = Null)
        """

    @overload
    def ReadInts(self, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[int]]: ...

    @overload
    def ReadInts(self, PC: IGESData_ParamCursor, mess: str, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[int]]:
        """
        Reads a list of Integer values, defined by PC (with a count of
        parameters). PC can start from Current Number and command it
        to advance after reading (use method CurrentList to do this)
        The list is given as a HArray1, numered from "index"
        If all params are not Integer, Check is filled (using mess)
        and return value is False
        """

    @overload
    def ReadReals(self, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[float]]: ...

    @overload
    def ReadReals(self, PC: IGESData_ParamCursor, mess: str, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[float]]:
        """
        Reads a list of Real values defined by PC
        Same conditions as for ReadInts, for PC and index
        An Integer parameter is accepted, if at least one parameter is
        Integer, Check is filled with a "Warning" message
        If all params are neither Real nor Integer, Check is filled
        (using mess) and return value is False
        """

    @overload
    def ReadTexts(self, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]]: ...

    @overload
    def ReadTexts(self, PC: IGESData_ParamCursor, mess: str, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]]:
        """
        Reads a list of Hollerith Texts, defined by PC
        Texts are read as Hollerith texts without leading "nnnH"
        Same conditions as for ReadInts, for PC and index
        If all params are not Text, Check is filled (using mess)
        and return value is False
        """

    @overload
    def ReadEnts(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity]]: ...

    @overload
    def ReadEnts(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, mess: str, index: int = 1) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity]]:
        """
        Reads a list of Entities defined by PC
        Same conditions as for ReadInts, for PC and index
        The list is given as a HArray1, numered from "index"
        If all params cannot be read as Entities, Check is filled
        (using mess) and return value is False
        Remark : Null references are accepted, they are ignored
        (negative pointers too : they provoke a Warning message)
        If the caller wants to check them, a loop on ReadEntity should
        be used
        """

    @overload
    def ReadEntList(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, amsg: nanoocp.Message.Message_Msg, val: nanoocp.Interface.Interface_EntityList, ord: bool = True) -> bool: ...

    @overload
    def ReadEntList(self, IR: IGESData_IGESReaderData | None, PC: IGESData_ParamCursor, mess: str, val: nanoocp.Interface.Interface_EntityList, ord: bool = True) -> bool:
        """
        Reads a list of Entities defined by PC
        Same conditions as for ReadEnts, for PC
        The list is given as an EntityList
        (index has no meaning; the EntityList starts from clear)
        If "ord" is given True (default), entities will be added to
        the list in their original order
        Remark : Negative or Null Pointers are ignored
        Else ("ord" False), order is not guaranteed (faster mode)
        If all params cannot be read as Entities, same as above
        Warning: Give "ord" to False ONLY if order is not significant
        """

    @overload
    def ReadingReal(self, num: int) -> tuple[bool, float]: ...

    @overload
    def ReadingReal(self, num: int, mess: str) -> tuple[bool, float]:
        """
        Routine which reads a Real parameter, given its number
        Same conditions as ReadReal for mess, val, and return value
        """

    @overload
    def ReadingEntityNumber(self, num: int) -> tuple[bool, int]: ...

    @overload
    def ReadingEntityNumber(self, num: int, mess: str) -> tuple[bool, int]:
        """
        Routine which reads an Entity Number (which allows to read the
        Entity in the IGESReaderData by BoundEntity), given its number
        in the list of Parameters
        Same conditions as ReadEntity for mess, val, and return value
        In particular, returns True and val to zero means Null Entity,
        and val not zero means Entity read by BoundEntity
        """

    def SendFail(self, amsg: nanoocp.Message.Message_Msg) -> None: ...

    def SendWarning(self, amsg: nanoocp.Message.Message_Msg) -> None: ...

    @overload
    def AddFail(self, afail: str, bfail: str = '') -> None: ...

    @overload
    def AddFail(self, af: nanoocp.TCollection.TCollection_HAsciiString | None, bf: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """feeds the Check with a new fail (as a String or as a CString)"""

    @overload
    def AddWarning(self, awarn: str, bwarn: str = '') -> None: ...

    @overload
    def AddWarning(self, aw: nanoocp.TCollection.TCollection_HAsciiString | None, bw: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """feeds the Check with a new Warning message"""

    def Mend(self, pref: str = '') -> None: ...

    def HasFailed(self) -> bool:
        """says if fails have been recorded into the Check"""

    def Check(self) -> nanoocp.Interface.Interface_Check:
        """
        returns the Check
        Note that any error signaled above is also recorded into it
        """

    def CCheck(self) -> nanoocp.Interface.Interface_Check:
        """
        returns the check in a way which allows to work on it directly
        (i.e. messages added to the Check are added to ParamReader too)
        """

    def IsCheckEmpty(self) -> bool:
        """
        Returns True if the Check is Empty
        Else, it has to be recorded with the Read Entity
        """

class IGESData_ReadWriteModule(nanoocp.Interface.Interface_ReaderModule):
    """
    Defines basic File Access Module, under the control of
    IGESReaderTool for Reading and IGESWriter for Writing :
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    The common parts (Directory Entry, Lists of Associativities
    and Properties) are processed by IGESReaderTool & IGESWriter

    Each sub-class of ReadWriteModule is used in conjunction with
    a sub-class of Protocol from IGESData and processes several
    types of IGESEntity (typically, them of a package) :
    The Protocol gives a unique positive integer Case Number for
    each type of IGESEntity it recognizes, the corresponding
    ReadWriteModule processes an Entity by using the Case Number
    to known what is to do
    On Reading, the general service NewVoid is used to create an
    IGES Entity the first time

    Warning : Works with an IGESReaderData which stores "DE parts" of Items
    """

    def CaseNum(self, data: nanoocp.Interface.Interface_FileReaderData | None, num: int) -> int:
        """
        Translates the Type of record <num> in <data> to a positive
        Case Number, or 0 if failed.
        Works with IGESReaderData which provides Type & Form Numbers,
        and calls CaseIGES (see below)
        """

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """
        Defines Case Numbers corresponding to the Entity Types taken
        into account by a sub-class of ReadWriteModule (hence, each
        sub-class of ReadWriteModule has to redefine this method)
        Called by CaseNum. Its result will then be used to call
        Read, etc ...
        """

    def Read(self, CN: int, data: nanoocp.Interface.Interface_FileReaderData | None, num: int, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_Check:
        """General Read Function. See IGESReaderTool for more info"""

    def ReadOwnParams(self, CN: int, ent: IGESData_IGESEntity | None, IR: IGESData_IGESReaderData | None, PR: IGESData_ParamReader) -> None:
        """
        Reads own parameters from file for an Entity; <PR> gives
        access to them, <IR> detains parameter types and values
        For each class, there must be a specific action provided
        Note that Properties and Associativities Lists are Read by
        specific methods (see below), they are called under control
        of reading process (only one call) according Stage recorded
        in ParamReader
        """

    def WriteOwnParams(self, CN: int, ent: IGESData_IGESEntity | None, IW: IGESData_IGESWriter) -> None:
        """
        Writes own parameters to IGESWriter; defined for each class
        (to be redefined for other IGES ReadWriteModules)
        Warning : Properties and Associativities are directly managed by
        WriteIGES, must not be sent by this method
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_SingleParentEntity(IGESData_IGESEntity):
    """
    a SingleParentEntity is a kind of IGESEntity which can refer
    to a (Single) Parent, from Associativities list of an Entity
    a effective SingleParent definition entity must inherit it
    """

    def SingleParent(self) -> IGESData_IGESEntity:
        """Returns the parent designated by the Entity, if only one !"""

    def NbChildren(self) -> int:
        """Returns the count of Entities designated as children"""

    def Child(self, num: int) -> IGESData_IGESEntity:
        """Returns a Child given its rank"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_ToolLocation(nanoocp.Standard.Standard_Transient):
    """
    This Tool determines and gives access to effective Locations
    of IGES Entities as defined by the IGES Norm. These Locations
    can be for each Entity :
    - on one part, explicitly defined by a Transf in Directory
    Part (this Transf can be itself compound); if not defined,
    no proper Transformation is defined
    - on the other part, implicitly defined by a reference from
    another Entity : its Parent
    Both implicit and explicit locations are combinable.

    Implicit definition can be itself defined, either through the
    definition of an Entity (i.e. a Composite Curve references
    a list of Curves), or by a specific Associativity, of type
    SingleParentEntity, by which the Location of the Parent is
    applied to the Childs defined by this Associativity.
    Remark that a Transf itself has no Location, but it can be
    compound

    This is a TShared object, then it is easier to use in an
    interactive session
    """

    @overload
    def __init__(self, amodel: IGESData_IGESModel | None, protocol: IGESData_Protocol | None) -> None:
        """
        Creates a ToolLocation on a given Model, filled with the help
        of a Protocol (which allows to known Entities referenced by
        other ones)
        """

    @overload
    def __init__(self, theOther: IGESData_ToolLocation) -> None: ...

    def Load(self) -> None:
        """Does the effective work of determining Locations of Entities"""

    def SetPrecision(self, prec: float) -> None:
        """
        Sets a precision for the Analysis of Locations
        (default by constructor is 1.E-05)
        """

    def SetReference(self, parent: IGESData_IGESEntity | None, child: IGESData_IGESEntity | None) -> None:
        """
        Sets the "Reference" information for <child> as being <parent>
        Sets an Error Status if already set (see method IsAmbiguous)
        """

    def SetParentAssoc(self, parent: IGESData_IGESEntity | None, child: IGESData_IGESEntity | None) -> None:
        """
        Sets the "Associativity" information for <child> as being
        <parent> (it must be the Parent itself, not the Associativity)
        """

    def ResetDependences(self, child: IGESData_IGESEntity | None) -> None:
        """Resets all information about dependences for <child>"""

    def SetOwnAsDependent(self, ent: IGESData_IGESEntity | None) -> None:
        """
        Unitary action which defines Entities referenced by <ent>
        (except those in Directory Part and Associativities List)
        as Dependent (their Locations are related to that of <ent>)
        """

    def IsTransf(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Returns True if <ent> is kind of TransfEntity. Then, it has
        no location, while it can be used to define a Location)
        """

    def IsAssociativity(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Returns True if <ent> is an Associativity (IGES Type 402).
        Then, Location does not apply.
        """

    def HasTransf(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Returns True if <ent> has a Transformation Matrix in proper
        (referenced from its Directory Part)
        """

    def ExplicitLocation(self, ent: IGESData_IGESEntity | None) -> nanoocp.gp.gp_GTrsf:
        """
        Returns the Explicit Location defined by the Transformation
        Matrix of <ent>. Identity if there is none
        """

    def IsAmbiguous(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Returns True if more than one Parent has been determined for
        <ent>, by adding direct References and Associativities
        """

    def HasParent(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Returns True if <ent> is dependent from one and only one other
        Entity, either by Reference or by Associativity
        """

    def Parent(self, ent: IGESData_IGESEntity | None) -> IGESData_IGESEntity:
        """
        Returns the unique Parent recorded for <ent>.
        Returns a Null Handle if there is none
        """

    def HasParentByAssociativity(self, ent: IGESData_IGESEntity | None) -> bool:
        """
        Returns True if the Parent, if there is one, is defined by
        a SingleParentEntity Associativity
        Else, if HasParent is True, it is by Reference
        """

    def ParentLocation(self, ent: IGESData_IGESEntity | None) -> nanoocp.gp.gp_GTrsf:
        """
        Returns the effective Location of the Parent of <ent>, if
        there is one : this Location is itself given as compound
        according dependences on the Parent, if there are some.
        Returns an Identity Transformation if no Parent is recorded.
        """

    def EffectiveLocation(self, ent: IGESData_IGESEntity | None) -> nanoocp.gp.gp_GTrsf:
        """
        Returns the effective Location of an Entity, i.e. the
        composition of its proper Transformation Matrix (returned by
        Transf) and its Parent's Location (returned by ParentLocation)
        """

    def AnalyseLocation(self, loc: nanoocp.gp.gp_GTrsf, result: nanoocp.gp.gp_Trsf) -> bool:
        """
        Analysis a Location given as a GTrsf, by trying to convert it
        to a Trsf (i.e. to a True Location of which effect is
        described by an Isometry or a Similarity)
        Works with the Precision given by default or by SetPrecision
        Calls ConvertLocation (see below)
        """

    @staticmethod
    def ConvertLocation(prec: float, loc: nanoocp.gp.gp_GTrsf, result: nanoocp.gp.gp_Trsf, uni: float = 1.0) -> bool:
        """
        Conversion of a Location, from GTrsf form to Trsf form
        Works with a precision given as argument.
        Returns True if the Conversion is possible, (hence, <result>
        contains the converted location), False else
        <unit>, if given, indicates the unit in which <loc> is defined
        in meters. It concerns the translation part (to be converted.

        As a class method, it can be called separately
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_TransfEntity(IGESData_IGESEntity):
    """
    defines required type for Transf in directory part
    an effective Transf entity must inherits it
    """

    def Value(self) -> nanoocp.gp.gp_GTrsf:
        """
        gives value of the transformation, as a GTrsf
        To be defined by an effective class of Transformation Entity
        Warning : Must take in account Composition : if a TransfEntity has in
        its Directory Part, a Transf, this means that it is Compound,
        Value must return the global result
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_ViewKindEntity(IGESData_IGESEntity):
    """
    defines required type for ViewKind in directory part
    that is, Single view or Multiple view
    An effective ViewKind entity must inherit it and define
    IsSingle (True for Single, False for List of Views),
    NbViews and ViewItem (especially for a List)
    """

    def IsSingle(self) -> bool:
        """says if "me" is a Single View (True) or a List of Views (False)"""

    def NbViews(self) -> int:
        """
        Returns the count of Views for a List of Views. For a Single
        View, may return simply 1
        """

    def ViewItem(self, num: int) -> IGESData_ViewKindEntity:
        """
        Returns the View n0. <num> for a List of Views. For a Single
        Views, may return <me> itself
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESData_WriterLib:
    @overload
    def __init__(self) -> None:
        """
        Creates an empty Library : it will later by filled by method
        AddProtocol
        """

    @overload
    def __init__(self, aprotocol: IGESData_Protocol | None) -> None:
        """
        Creates a Library which complies with a Protocol, that is :
        Same class (criterium IsInstance)
        This creation gets the Modules from the global set, those
        which are bound to the given Protocol and its Resources
        """

    @overload
    def __init__(self, theOther: IGESData_WriterLib) -> None: ...

    @staticmethod
    def SetGlobal(amodule: IGESData_ReadWriteModule | None, aprotocol: IGESData_Protocol | None) -> None:
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

    def Select(self, obj: IGESData_IGESEntity | None) -> tuple[bool, IGESData_ReadWriteModule, int]:
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

    def Module(self) -> IGESData_ReadWriteModule:
        """Returns the current Module in the Iteration"""

    def Protocol(self) -> IGESData_Protocol:
        """Returns the current Protocol in the Iteration"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESData
IGESData_Array1OfIGESEntity = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESData.IGESData_IGESEntity]
IGESData_HArray1OfIGESEntity = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity]
