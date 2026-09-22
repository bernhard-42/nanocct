"""OCCT package IGESBasic (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESData
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class IGESBasic:
    """This package represents basic entities from IGES"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynqmic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESBasic_Protocol:
        """Returns the Protocol for this Package"""

class IGESBasic_AssocGroupType(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines AssocGroupType, Type <406> Form <23>
    in package IGESBasic
    Used to assign an unambiguous identification to a Group
    Associativity.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_AssocGroupType) -> None: ...

    def Init(self, nbDataFields: int, aType: int, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        AssocGroupType
        - nbDataFields : number of parameter data fields = 2
        - aType        : type of attached associativity
        - aName        : identifier of associativity of type AType
        """

    def NbData(self) -> int:
        """returns the number of parameter data fields, always = 2"""

    def AssocType(self) -> int:
        """returns the type of attached associativity"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns identifier of instance of specified associativity"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ExternalReferenceFile(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ExternalReferenceFile, Type <406> Form <12>
    in package IGESBasic
    References definitions residing in another file
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_ExternalReferenceFile) -> None: ...

    def Init(self, aNameArray: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        This method is used to set the fields of the class
        ExternalReferenceFile
        - aNameArray : External Reference File Names
        """

    def NbListEntries(self) -> int:
        """returns number of External Reference File Names"""

    def Name(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns External Reference File Name
        raises exception if Index <= 0 or Index > NbListEntries()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ExternalRefFile(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ExternalRefFile, Type <416> Form <1>
    in package IGESBasic
    Used when entire reference file is to be instanced
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_ExternalRefFile) -> None: ...

    def Init(self, aFileIdent: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the field of the class
        ExternalRefFile
        - aFileIdent : External Reference File Identifier
        """

    def FileId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns External Reference File Identifier"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ExternalRefFileIndex(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ExternalRefFileIndex, Type <402> Form <12>
    in package IGESBasic
    Contains a list of the symbolic names used by the
    referencing files and the DE pointers to the
    corresponding definitions within the referenced file
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_ExternalRefFileIndex) -> None: ...

    def Init(self, aNameArray: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, allEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        ExternalRefFileIndex
        - aNameArray  : External Reference Entity symbolic names
        - allEntities : External Reference Entities
        raises exception if array lengths are not equal
        if size of aNameArray is not equal to size of allEntities
        """

    def NbEntries(self) -> int:
        """returns number of index entries"""

    def Name(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns the External Reference Entity symbolic name
        raises exception if Index <= 0 or Index > NbEntries()
        """

    def Entity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the internal entity
        raises exception if Index <= 0 or Index > NbEntries()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ExternalRefFileName(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ExternalRefFileName, Type <416> Form <0-2>
    in package IGESBasic
    Used when single definition from the reference file is
    required or for external logical references where an
    entity in one file relates to an entity in another file
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_ExternalRefFileName) -> None: ...

    def Init(self, aFileIdent: nanoocp.TCollection.TCollection_HAsciiString | None, anExtName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        ExternalRefFileName
        - aFileIdent : External Reference File Identifier
        - anExtName  : External Reference Entity Symbolic Name
        """

    def SetForEntity(self, mode: bool) -> None:
        """
        Changes FormNumber to be 2 if <mode> is True (For Entity)
        or 0 if <mode> is False (For Definition)
        """

    def FileId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns External Reference File Identifier"""

    def ReferenceName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns External Reference Entity Symbolic Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ExternalRefLibName(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ExternalRefLibName, Type <416> Form <4>
    in package IGESBasic
    Used when it is assumed that a copy of the subfigure
    exists in native form in a library on the receiving
    system
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_ExternalRefLibName) -> None: ...

    def Init(self, aLibName: nanoocp.TCollection.TCollection_HAsciiString | None, anExtName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        ExternalRefLibName
        - aLibName  : Name of library in which ExtName resides
        - anExtName : External Reference Entity Symbolic Name
        """

    def LibraryName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns name of library in which External Reference Entity
        Symbolic Name resides
        """

    def ReferenceName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns External Reference Entity Symbolic Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ExternalRefName(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ExternalRefName, Type <416> Form <3>
    in package IGESBasic
    Used when it is assumed that a copy of the subfigure
    exists in native form on the receiving system
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_ExternalRefName) -> None: ...

    def Init(self, anExtName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        ExternalRefName
        - anExtName : External Reference Entity Symbolic Name
        """

    def ReferenceName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns External Reference Entity Symbolic Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESBasic (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESBasic and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESBasic_GeneralModule) -> None: ...

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
        Structure for Groups, Figures & Co
        Description for External Refs
        Auxiliary for other
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_Group(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Group, Type <402> Form <1>
    in package IGESBasic
    The Group Associativity allows a collection of a set
    of entities to be maintained as a single, logical
    entity

    Group, OrderedGroup, GroupWithoutBackP, OrderedGroupWithoutBackP
    share the same definition (class Group), form number changes

    non Ordered, non WithoutBackP : form  1
    non Ordered,     WithoutBackP : form  7
    Ordered, non WithoutBackP : form 14
    Ordered,     WithoutBackP : form 15
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, nb: int) -> None:
        """
        Creates a Group with a predefined count of items
        (which all start as null)
        """

    @overload
    def __init__(self, theOther: IGESBasic_Group) -> None: ...

    def Init(self, allEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class Group
        - allEntities : Used to store pointers to members of
        the Group.
        """

    def SetOrdered(self, mode: bool) -> None:
        """Sets a Group to be, or not to be Ordered (according mode)"""

    def SetWithoutBackP(self, mode: bool) -> None:
        """Sets a Group to be, or not to be WithoutBackP"""

    def IsOrdered(self) -> bool:
        """Returns True if <me> is Ordered"""

    def IsWithoutBackP(self) -> bool:
        """Returns True if <me> is WithoutBackP"""

    def SetUser(self, type: int, form: int) -> None:
        """Enforce a new value for the type and form"""

    def SetNb(self, nb: int) -> None:
        """
        Changes the count of item
        If greater, new items are null
        If lower, old items are lost
        """

    def NbEntities(self) -> int:
        """returns the number of IGESEntities in the Group"""

    def Entity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the specific entity from the Group"""

    def Value(self, Index: int) -> nanoocp.Standard.Standard_Transient:
        """returns the specific entity from the Group"""

    def SetValue(self, Index: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """Sets a new value for item <Index>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_GroupWithoutBackP(IGESBasic_Group):
    """
    defines GroupWithoutBackP, Type <402> Form <7>
    in package IGESBasic
    this class defines a Group without back pointers

    It inherits from Group
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_GroupWithoutBackP) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_HArray1OfHArray1OfIGESEntity(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, low: int, up: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_HArray1OfHArray1OfIGESEntity) -> None: ...

    def Lower(self) -> int: ...

    def Upper(self) -> int: ...

    def Length(self) -> int: ...

    def SetValue(self, num: int, val: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None: ...

    def Value(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_HArray1OfHArray1OfInteger(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, low: int, up: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_HArray1OfHArray1OfInteger) -> None: ...

    def Lower(self) -> int: ...

    def Upper(self) -> int: ...

    def Length(self) -> int: ...

    def SetValue(self, num: int, val: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def Value(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_HArray1OfHArray1OfReal(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, low: int, up: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_HArray1OfHArray1OfReal) -> None: ...

    def Lower(self) -> int: ...

    def Upper(self) -> int: ...

    def Length(self) -> int: ...

    def SetValue(self, num: int, val: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    def Value(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_HArray1OfHArray1OfXY(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, low: int, up: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_HArray1OfHArray1OfXY) -> None: ...

    def Lower(self) -> int: ...

    def Upper(self) -> int: ...

    def Length(self) -> int: ...

    def SetValue(self, num: int, val: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None) -> None: ...

    def Value(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_HArray1OfHArray1OfXYZ(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, low: int, up: int) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_HArray1OfHArray1OfXYZ) -> None: ...

    def Lower(self) -> int: ...

    def Upper(self) -> int: ...

    def Length(self) -> int: ...

    def SetValue(self, num: int, val: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    def Value(self, num: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_Hierarchy(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Hierarchy, Type <406> Form <10>
    in package IGESBasic
    Provides ability to control the hierarchy of each
    directory entry attribute.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_Hierarchy) -> None: ...

    def Init(self, nbPropVal: int, aLineFont: int, aView: int, anEntityLevel: int, aBlankStatus: int, aLineWt: int, aColorNum: int) -> None:
        """
        This method is used to set the fields of the class
        Hierarchy
        - nbPropVal     : Number of Property values = 6
        - aLineFont     : indicates the line font
        - aView         : indicates the view
        - aEntityLevel  : indicates the entity level
        - aBlankStatus  : indicates the blank status
        - aLineWt       : indicates the line weight
        - aColorNum     : indicates the color num
        aLineFont, aView, aEntityLevel, aBlankStatus, aLineWt and
        aColorNum can take 0 or 1.
        0 : The directory entry attribute will apply to entities
        physically subordinate to this entity.
        1 : The directory entry attribute of this entity will not
        apply to physically subordinate entities.
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values, which should be 6"""

    def NewLineFont(self) -> int:
        """returns the line font"""

    def NewView(self) -> int:
        """returns the view"""

    def NewEntityLevel(self) -> int:
        """returns the entity level"""

    def NewBlankStatus(self) -> int:
        """returns the blank status"""

    def NewLineWeight(self) -> int:
        """returns the line weight"""

    def NewColorNum(self) -> int:
        """returns the color number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_Name(nanoocp.IGESData.IGESData_NameEntity):
    """
    defines Name, Type <406> Form <15>
    in package IGESBasic
    Used to specify a user defined name
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_Name) -> None: ...

    def Init(self, nbPropVal: int, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class Name
        - nbPropVal  : Number of property values, always = 1
        - aName      : Stores the Name
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values, which should be 1"""

    def Value(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the user defined Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_OrderedGroup(IGESBasic_Group):
    """
    defines OrderedGroup, Type <402> Form <14>
    in package IGESBasic
    this class defines an Ordered Group with back pointers
    Allows a collection of a set of entities to be
    maintained as a single entity, but the group is
    ordered.
    It inherits from Group
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_OrderedGroup) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_OrderedGroupWithoutBackP(IGESBasic_Group):
    """
    defines OrderedGroupWithoutBackP, Type <402> Form <15>
    in package IGESBasic
    Allows a collection of a set of entities to be
    maintained as a single entity, but the group is
    ordered and there are no back pointers.
    It inherits from Group
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_OrderedGroupWithoutBackP) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESBasic"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, one
        (Protocol from IGESData)
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

class IGESBasic_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines basic File Access Module for IGESBasic (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESBasic_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESBasic"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESBasic"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_SingleParent(nanoocp.IGESData.IGESData_SingleParentEntity):
    """
    defines SingleParent, Type <402> Form <9>
    in package IGESBasic
    It defines a logical structure of one independent
    (parent) entity and one or more subordinate (children)
    entities
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_SingleParent) -> None: ...

    def Init(self, nbParentEntities: int, aParentEntity: nanoocp.IGESData.IGESData_IGESEntity | None, allChildren: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        SingleParent
        - nbParentEntities : Indicates number of Parents, always = 1
        - aParentEntity    : Used to hold the Parent Entity
        - allChildren      : Used to hold the children
        """

    def NbParentEntities(self) -> int:
        """returns the number of Parent Entities, which should be 1"""

    def SingleParent(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """Returns the Parent Entity (inherited method)"""

    def NbChildren(self) -> int:
        """returns the number of children of the Parent"""

    def Child(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the specific child as indicated by Index
        raises exception if Index <= 0 or Index > NbChildren()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_SingularSubfigure(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SingularSubfigure, Type <408> Form <0>
    in package IGESBasic
    Defines the occurrence of a single instance of the
    defined Subfigure.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_SingularSubfigure) -> None: ...

    def Init(self, aSubfigureDef: IGESBasic_SubfigureDef | None, aTranslation: nanoocp.gp.gp_XYZ, hasScale: bool, aScale: float) -> None:
        """
        This method is used to set the fields of the class
        SingularSubfigure
        - aSubfigureDef : the Subfigure Definition entity
        - aTranslation  : used to store the X,Y,Z coord
        - hasScale      : Indicates the presence of scale factor
        - aScale        : Used to store the scale factor
        """

    def Subfigure(self) -> IGESBasic_SubfigureDef:
        """returns the subfigure definition entity"""

    def Translation(self) -> nanoocp.gp.gp_XYZ:
        """returns the X, Y, Z coordinates"""

    def ScaleFactor(self) -> float:
        """
        returns the scale factor
        if hasScaleFactor is False, returns 1.0 (default)
        """

    def HasScaleFactor(self) -> bool:
        """
        returns a boolean indicating whether scale factor
        is present or not
        """

    def TransformedTranslation(self) -> nanoocp.gp.gp_XYZ:
        """returns the Translation after transformation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """
    Defines Services attached to IGES Entities :
    Dump & OwnCorrect, for IGESBasic
    """

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESBasic & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESBasic_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESBasic"""

    def OwnCorrect(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Performs non-ambiguous Corrections on Entities which support
        them (AssocGroupType,Hierarchy,Name,SingleParent)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_SubfigureDef(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SubfigureDef, Type <308> Form <0>
    in package IGESBasic
    This Entity permits a single definition of a detail to
    be utilized in multiple instances in the creation of
    the whole picture
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESBasic_SubfigureDef) -> None: ...

    def Init(self, aDepth: int, aName: nanoocp.TCollection.TCollection_HAsciiString | None, allAssocEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        SubfigureDef
        - aDepth           : It indicates the amount of nesting
        - aName            : the subfigure name
        - allAssocEntities : the associated entities
        """

    def Depth(self) -> int:
        """
        returns depth of the Subfigure
        if theDepth = 0 - No reference to any subfigure instance.
        """

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the name of Subfigure"""

    def NbEntities(self) -> int:
        """returns number of entities. Is greater than or equal to zero."""

    def AssociatedEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the specific entity as indicated by Index
        raises exception if Index <= 0 or Index > NbEntities()
        """

    def Value(self, Index: int) -> nanoocp.Standard.Standard_Transient:
        """
        returns the specific entity as indicated by Index
        raises exception if Index <= 0 or Index > NbEntities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESBasic_ToolAssocGroupType:
    """
    Tool to work on a AssocGroupType. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolAssocGroupType, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolAssocGroupType) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_AssocGroupType | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_AssocGroupType | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_AssocGroupType | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a AssocGroupType <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_AssocGroupType | None) -> bool:
        """
        Sets automatic unambiguous Correction on a AssocGroupType
        (NbData forced to 2)
        """

    def DirChecker(self, ent: IGESBasic_AssocGroupType | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_AssocGroupType | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_AssocGroupType | None, entto: IGESBasic_AssocGroupType | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_AssocGroupType | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolExternalReferenceFile:
    """
    Tool to work on a ExternalReferenceFile. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolExternalReferenceFile, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolExternalReferenceFile) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_ExternalReferenceFile | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_ExternalReferenceFile | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_ExternalReferenceFile | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ExternalReferenceFile <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_ExternalReferenceFile | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_ExternalReferenceFile | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_ExternalReferenceFile | None, entto: IGESBasic_ExternalReferenceFile | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_ExternalReferenceFile | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolExternalRefFile:
    """
    Tool to work on a ExternalRefFile. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolExternalRefFile, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolExternalRefFile) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_ExternalRefFile | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_ExternalRefFile | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_ExternalRefFile | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ExternalRefFile <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_ExternalRefFile | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_ExternalRefFile | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_ExternalRefFile | None, entto: IGESBasic_ExternalRefFile | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_ExternalRefFile | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolExternalRefFileIndex:
    """
    Tool to work on a ExternalRefFileIndex. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolExternalRefFileIndex, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolExternalRefFileIndex) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_ExternalRefFileIndex | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_ExternalRefFileIndex | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_ExternalRefFileIndex | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ExternalRefFileIndex <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_ExternalRefFileIndex | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_ExternalRefFileIndex | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_ExternalRefFileIndex | None, entto: IGESBasic_ExternalRefFileIndex | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_ExternalRefFileIndex | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolExternalRefFileName:
    """
    Tool to work on a ExternalRefFileName. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolExternalRefFileName, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolExternalRefFileName) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_ExternalRefFileName | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_ExternalRefFileName | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_ExternalRefFileName | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ExternalRefFileName <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_ExternalRefFileName | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_ExternalRefFileName | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_ExternalRefFileName | None, entto: IGESBasic_ExternalRefFileName | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_ExternalRefFileName | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolExternalRefLibName:
    """
    Tool to work on a ExternalRefLibName. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolExternalRefLibName, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolExternalRefLibName) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_ExternalRefLibName | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_ExternalRefLibName | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_ExternalRefLibName | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ExternalRefLibName <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_ExternalRefLibName | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_ExternalRefLibName | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_ExternalRefLibName | None, entto: IGESBasic_ExternalRefLibName | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_ExternalRefLibName | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolExternalRefName:
    """
    Tool to work on a ExternalRefName. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolExternalRefName, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolExternalRefName) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_ExternalRefName | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_ExternalRefName | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_ExternalRefName | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ExternalRefName <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_ExternalRefName | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_ExternalRefName | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_ExternalRefName | None, entto: IGESBasic_ExternalRefName | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_ExternalRefName | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolGroup:
    """
    Tool to work on a Group. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolGroup, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolGroup) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_Group | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_Group | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_Group | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Group <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_Group | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Group
        (Null Elements are removed from list)
        """

    def DirChecker(self, ent: IGESBasic_Group | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_Group | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_Group | None, entto: IGESBasic_Group | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_Group | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolGroupWithoutBackP:
    """
    Tool to work on a GroupWithoutBackP. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolGroupWithoutBackP, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolGroupWithoutBackP) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_GroupWithoutBackP | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_GroupWithoutBackP | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_GroupWithoutBackP | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a GroupWithoutBackP <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_GroupWithoutBackP | None) -> bool:
        """
        Sets automatic unambiguous Correction on a GroupWithoutBackP
        (Null Elements are removed from list)
        """

    def DirChecker(self, ent: IGESBasic_GroupWithoutBackP | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_GroupWithoutBackP | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_GroupWithoutBackP | None, entto: IGESBasic_GroupWithoutBackP | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_GroupWithoutBackP | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolHierarchy:
    """
    Tool to work on a Hierarchy. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolHierarchy, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolHierarchy) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_Hierarchy | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_Hierarchy | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_Hierarchy | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Hierarchy <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_Hierarchy | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Hierarchy
        (NbPropertyValues forced to 6)
        """

    def DirChecker(self, ent: IGESBasic_Hierarchy | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_Hierarchy | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_Hierarchy | None, entto: IGESBasic_Hierarchy | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_Hierarchy | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolName:
    """
    Tool to work on a Name. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolName, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolName) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_Name | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_Name | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_Name | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Name <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_Name | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Name
        (NbPropertyValues forced to 1)
        """

    def DirChecker(self, ent: IGESBasic_Name | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_Name | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_Name | None, entto: IGESBasic_Name | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_Name | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolOrderedGroup:
    """
    Tool to work on a OrderedGroup. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolOrderedGroup, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolOrderedGroup) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_OrderedGroup | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_OrderedGroup | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_OrderedGroup | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a OrderedGroup <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_OrderedGroup | None) -> bool:
        """
        Sets automatic unambiguous Correction on an OrderedGroup
        (Null Elements are removed from list)
        """

    def DirChecker(self, ent: IGESBasic_OrderedGroup | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_OrderedGroup | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_OrderedGroup | None, entto: IGESBasic_OrderedGroup | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_OrderedGroup | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolOrderedGroupWithoutBackP:
    """
    Tool to work on a OrderedGroupWithoutBackP. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolOrderedGroupWithoutBackP, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolOrderedGroupWithoutBackP) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_OrderedGroupWithoutBackP | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_OrderedGroupWithoutBackP | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_OrderedGroupWithoutBackP | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a OrderedGroupWithoutBackP <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_OrderedGroupWithoutBackP | None) -> bool:
        """
        Sets automatic unambiguous Correction on an OrderedGroupWithoutBackP
        (Null Elements are removed from list)
        """

    def DirChecker(self, ent: IGESBasic_OrderedGroupWithoutBackP | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_OrderedGroupWithoutBackP | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_OrderedGroupWithoutBackP | None, entto: IGESBasic_OrderedGroupWithoutBackP | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_OrderedGroupWithoutBackP | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolSingleParent:
    """
    Tool to work on a SingleParent. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSingleParent, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolSingleParent) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_SingleParent | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_SingleParent | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_SingleParent | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SingleParent <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESBasic_SingleParent | None) -> bool:
        """
        Sets automatic unambiguous Correction on a SingleParent
        (NbParents forced to 1)
        """

    def DirChecker(self, ent: IGESBasic_SingleParent | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_SingleParent | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_SingleParent | None, entto: IGESBasic_SingleParent | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_SingleParent | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolSingularSubfigure:
    """
    Tool to work on a SingularSubfigure. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSingularSubfigure, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolSingularSubfigure) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_SingularSubfigure | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_SingularSubfigure | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_SingularSubfigure | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SingularSubfigure <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_SingularSubfigure | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_SingularSubfigure | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_SingularSubfigure | None, entto: IGESBasic_SingularSubfigure | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_SingularSubfigure | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESBasic_ToolSubfigureDef:
    """
    Tool to work on a SubfigureDef. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSubfigureDef, ready to work"""

    @overload
    def __init__(self, theOther: IGESBasic_ToolSubfigureDef) -> None: ...

    def ReadOwnParams(self, ent: IGESBasic_SubfigureDef | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESBasic_SubfigureDef | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESBasic_SubfigureDef | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SubfigureDef <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESBasic_SubfigureDef | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESBasic_SubfigureDef | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESBasic_SubfigureDef | None, entto: IGESBasic_SubfigureDef | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESBasic_SubfigureDef | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
IGESBasic_Array1OfLineFontEntity = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESData.IGESData_LineFontEntity]
IGESBasic_Array2OfHArray1OfReal = nanoocp.NCollection.NCollection_Array2[nanoocp.NCollection.NCollection_HArray1[float]]
IGESBasic_HArray1OfLineFontEntity = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_LineFontEntity]
IGESBasic_HArray2OfHArray1OfReal = nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]]
