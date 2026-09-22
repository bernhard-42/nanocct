"""OCCT package TDF (toolkit TKLCAF)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


TDF_AttributeValidMsk: int = 1

TDF_AttributeBackupMsk: int = 2

TDF_AttributeForgottenMsk: int = 4

TDF_LabelNodeImportMsk: int = -2147483648

TDF_LabelNodeAttModMsk: int = 1073741824

TDF_LabelNodeMayModMsk: int = 536870912

TDF_LabelNodeFlagsMsk: int = -536870912

class TDF:
    """
    This package provides data framework for binding
    features and data structures.

    The feature structure is a tree used to bind
    semantic information about each feature together.

    The only one concrete attribute defined in this
    package is the TagSource attribute.This attribute
    is used for random creation of child labels under
    a given label. Tags are randomly delivered.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF) -> None: ...

    @staticmethod
    def LowestID() -> nanoocp.Standard.Standard_GUID:
        """
        Returns ID "00000000-0000-0000-0000-000000000000",
        sometimes used as null ID.
        """

    @staticmethod
    def UppestID() -> nanoocp.Standard.Standard_GUID:
        """Returns ID "ffffffff-ffff-ffff-ffff-ffffffffffff"."""

    @staticmethod
    def AddLinkGUIDToProgID(ID: nanoocp.Standard.Standard_GUID, ProgID: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Sets link between GUID and ProgID in hidden DataMap"""

    @staticmethod
    def GUIDFromProgID(ProgID: nanoocp.TCollection.TCollection_ExtendedString, ID: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Returns True if there is GUID for given <ProgID> then GUID is returned in <ID>
        """

    @staticmethod
    def ProgIDFromGUID(ID: nanoocp.Standard.Standard_GUID, ProgID: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns True if there is ProgID for given <ID> then ProgID is returned in <ProgID>
        """

class TDF_Attribute(nanoocp.Standard.Standard_Transient):
    """
    A class each application has to implement. It is
    used to contain the application data.
    This abstract class, alongwith Label,
    is one of the cornerstones of Model Editor.
    The groundwork is to define the root of
    information. This information is to be
    attached to a Label, and could be of any of
    the following types:
    -   a feature
    -   a constraint
    -   a comment

    Contents:
    ---------

    Each software component who'd like to attach its
    own information to a label has to inherit from
    this class and has to add its own information as
    fields of this new class.

    Identification:
    ---------------

    An attribute can be identified by its ID. Every
    attributes used with the same meaning (for
    example: Integer, String, Topology...) have the
    same worldwide unique ID.

    Addition:
    ---------

    An attribute can be added to a label only if there
    is no attribute yet with the same ID. Call-back
    methods are offered, called automatically before
    and after the addition action.

    Removal:
    --------

    An attribute can be removed from a label only if
    there is an attribute yet with the same
    ID. Call-back methods are offered, called
    automatically before and after the removal
    action. A removed attribute cannot be found
    again. After a removal, only an addition of an
    attribute with the sane ID is possible (no
    backup...).

    Modification & Transaction:
    ---------------------------

    An attribute can be backuped before a
    modification. Only one backup attribute by
    transaction is possible. The modification can be
    forgotten (abort transaction) or validated (commit
    transaction).

    BackupCopy and restore are methods used by the backup or
    abort transaction actions. BackupCopy is called by
    Backup to generate an attribute with the same
    contents as the current one. Restore is called
    when aborting a transaction to transfer the
    backuped contents into the current
    attribute. These methods must be implemented by
    end use inheriting classes.

    A standard implementation of BackupCopy is provided, but
    it is not necessary a good one for any use.

    Copy use methods:
    -----------------

    Paste and NewEmpty methods are used by the copy
    algorithms. The goal of "Paste" is to transfer an
    attribute new contents into another attribute. The
    goal of "NewEmpty" is to create an attribute
    without contents, to be further filled with the
    new contents of another one. These 2 methods must
    be implemented by end use inheriting classes.

    AttributeDelta:
    ---------------

    An AttributeDelta is the difference between to
    attribute values states. These methods must be
    implemented by end use inheriting classes, to
    profit from the delta services.
    """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    @overload
    def SetID(self, arg0: nanoocp.Standard.Standard_GUID) -> None:
        """
        Sets specific ID of the attribute (supports several attributes
        of one type at the same label feature).
        """

    @overload
    def SetID(self) -> None:
        """
        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """

    def Label(self) -> TDF_Label:
        """
        Returns the label to which the attribute is
        attached. If the label is not included in a DF,
        the label is null. See Label.
        Warning:
        If the label is not included in a data
        framework, it is null.
        This function should not be redefined inline.
        """

    def Transaction(self) -> int:
        """
        Returns the transaction index in which the
        attribute has been created or modified.
        """

    def UntilTransaction(self) -> int:
        """
        Returns the upper transaction index until which
        the attribute is/was valid. This number may
        vary. A removed attribute validity range is
        reduced to its transaction index.
        """

    def IsValid(self) -> bool:
        """
        Returns true if the attribute is valid; i.e. not a
        backuped or removed one.
        """

    def IsNew(self) -> bool:
        """Returns true if the attribute has no backup"""

    def IsForgotten(self) -> bool:
        """
        Returns true if the attribute forgotten status is
        set.

        ShortCut Methods concerning associated attributes
        =================================================
        """

    def IsAttribute(self, anID: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Returns true if it exists an associated attribute
        of <me> with <anID> as ID.
        """

    def FindAttribute(self, anID: nanoocp.Standard.Standard_GUID) -> tuple[bool, TDF_Attribute]:
        """
        Finds an associated attribute of <me>, according
        to <anID>. the returned <anAttribute> is a valid
        one. The method returns True if found, False
        otherwise. A removed attribute cannot be found using
        this method.
        """

    def AddAttribute(self, other: TDF_Attribute | None) -> None:
        """
        Adds an Attribute <other> to the label of <me>.
        Raises if there is already one of the same GUID
        than <other>.
        """

    def ForgetAttribute(self, aguid: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Forgets the Attribute of GUID <aguid> associated
        to the label of <me>. Be careful that if <me> is
        the attribute of <guid>, <me> will have a null label
        after this call. If the attribute doesn't exist
        returns False. Otherwise returns True.
        """

    def ForgetAllAttributes(self, clearChildren: bool = True) -> None:
        """
        Forgets all the attributes attached to the label
        of <me>. Does it on the sub-labels if
        <clearChildren> is set to true. Of course, this
        method is compatible with Transaction & Delta
        mechanisms. Be careful that if <me> will have a
        null label after this call
        """

    def AfterAddition(self) -> None:
        """Something to do after adding an Attribute to a label."""

    def BeforeRemoval(self) -> None:
        """
        Something to do before removing an Attribute from
        a label.
        """

    def BeforeForget(self) -> None:
        """
        Something to do before forgetting an Attribute to a
        label.
        """

    def AfterResume(self) -> None:
        """
        Something to do after resuming an Attribute from
        a label.
        """

    def AfterRetrieval(self, forceIt: bool = False) -> bool:
        """
        Something to do AFTER creation of an attribute by
        persistent-transient translation. The returned
        status says if AfterUndo has been performed (true)
        or if this callback must be called once again
        further (false). If <forceIt> is set to true, the
        method MUST perform and return true. Does nothing
        by default and returns true.
        """

    def BeforeUndo(self, anAttDelta: TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """
        Something to do before applying <anAttDelta>. The
        returned status says if AfterUndo has been
        performed (true) or if this callback must be
        called once again further (false). If <forceIt> is
        set to true, the method MUST perform and return
        true. Does nothing by default and returns true.
        """

    def AfterUndo(self, anAttDelta: TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """
        Something to do after applying <anAttDelta>. The
        returned status says if AfterUndo has been
        performed (true) or if this callback must be
        called once again further (false). If <forceIt> is
        set to true, the method MUST perform and return
        true. Does nothing by default and returns true.
        """

    def BeforeCommitTransaction(self) -> None:
        """
        A callback.
        By default does nothing.
        It is called by TDF_Data::CommitTransaction() method.
        """

    def Backup(self) -> None:
        """
        Backups the attribute. The backuped attribute is
        flagged "Backuped" and not "Valid".

        The method does nothing:

        1) If the attribute transaction number is equal to
        the current transaction number (the attribute has
        already been backuped).

        2) If the attribute is not attached to a label.
        """

    def IsBackuped(self) -> bool:
        """
        Returns true if the attribute backup status is
        set. This status is set/unset by the
        Backup() method.
        """

    def BackupCopy(self) -> TDF_Attribute:
        """
        Copies the attribute contents into a new other
        attribute. It is used by Backup().
        """

    def Restore(self, anAttribute: TDF_Attribute | None) -> None:
        """
        Restores the backuped contents from <anAttribute>
        into this one. It is used when aborting a
        transaction.
        """

    def DeltaOnAddition(self) -> TDF_DeltaOnAddition:
        """
        Makes an AttributeDelta because <me>
        appeared. The only known use of a redefinition of
        this method is to return a null handle (no delta).
        """

    def DeltaOnForget(self) -> TDF_DeltaOnForget:
        """
        Makes an AttributeDelta because <me> has been
        forgotten.
        """

    def DeltaOnResume(self) -> TDF_DeltaOnResume:
        """
        Makes an AttributeDelta because <me> has been
        resumed.
        """

    @overload
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute | None) -> TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute.
        """

    @overload
    def DeltaOnModification(self, aDelta: TDF_DeltaOnModification | None) -> None:
        """Applies a DeltaOnModification to <me>."""

    def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval:
        """
        Makes a DeltaOnRemoval on <me> because <me> has
        disappeared from the DS.
        """

    def NewEmpty(self) -> TDF_Attribute:
        """
        Returns an new empty attribute from the good end
        type. It is used by the copy algorithm.
        """

    def Paste(self, intoAttribute: TDF_Attribute | None, aRelocationTable: TDF_RelocationTable | None) -> None:
        """
        This method is different from the "Copy" one,
        because it is used when copying an attribute from
        a source structure into a target structure. This
        method may paste the contents of <me> into
        <intoAttribute>.

        The given pasted attribute can be full or empty of
        its contents. But don't make a NEW! Just set the
        contents!

        It is possible to use <aRelocationTable> to
        get/set the relocation value of a source
        attribute.
        """

    def References(self, aDataSet: TDF_DataSet | None) -> None:
        """
        Adds the first level referenced attributes and labels
        to <aDataSet>.

        For this, use the AddLabel or AddAttribute of
        DataSet.

        If there is none, do not implement the method.
        """

    def Dump(self) -> str:
        """
        Dumps the minimum information about <me> on
        <aStream>.
        """

    def ExtendedDump(self, aFilter: TDF_IDFilter, aMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TDF.TDF_Attribute]) -> str:
        """
        Dumps the attribute content on <aStream>, using
        <aMap> like this: if an attribute is not in the
        map, first put add it to the map and then dump it.
        Use the map rank instead of dumping each attribute
        field.
        """

    def Forget(self, aTransaction: int) -> None:
        """
        Forgets the attribute. <aTransaction> is the
        current transaction in which the forget is done. A
        forgotten attribute is also flagged not "Valid".

        A forgotten attribute is invisible. Set also the
        "Valid" status to False. Obviously, DF cannot
        empty an attribute (this has a semantic
        signification), but can remove it from the
        structure. So, a forgotten attribute is NOT an empty
        one, but a soon DEAD one.

        Should be private.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_Label:
    """
    This class provides basic operations to define
    a label in a data structure.
    A label is a feature in the feature hierarchy. A
    label is always connected to a Data from TDF.
    To a label is attached attributes containing the
    software components information.

    Label information:

    It is possible to know the tag, the father, the
    depth in the tree of the label, if the label is
    root, null or equal to another label.

    Comfort methods:
    Some methods useful on a label.

    Attributes:

    It is possible to get an attribute in accordance
    to an ID, or the yougest previous version of a
    current attribute.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty label object."""

    @overload
    def __init__(self, theOther: TDF_Label) -> None: ...

    def Nullify(self) -> None:
        """Nullifies the label."""

    def Data(self) -> TDF_Data:
        """Returns the Data owning <me>."""

    def Tag(self) -> int:
        """
        Returns the tag of the label.
        This is the integer assigned randomly to a label
        in a data framework. This integer is used to
        identify this label in an entry.
        """

    def Father(self) -> TDF_Label:
        """
        Returns the label father. This label may be null
        if the label is root.
        """

    def IsNull(self) -> bool:
        """
        Returns True if the <aLabel> is null, i.e. it has
        not been included in the data framework.
        """

    def Imported(self, aStatus: bool) -> None:
        """
        Sets or unsets <me> and all its descendants as
        imported label, according to <aStatus>.
        """

    def IsImported(self) -> bool:
        """Returns True if the <aLabel> is imported."""

    def IsEqual(self, aLabel: TDF_Label) -> bool:
        """
        Returns True if the <aLabel> is equal to me (same
        LabelNode*).
        """

    def __eq__(self, aLabel: TDF_Label) -> bool: ...

    def IsDifferent(self, aLabel: TDF_Label) -> bool: ...

    def __ne__(self, aLabel: TDF_Label) -> bool: ...

    def IsRoot(self) -> bool: ...

    def IsAttribute(self, anID: nanoocp.Standard.Standard_GUID) -> bool:
        """Returns true if <me> owns an attribute with <anID> as ID."""

    def AddAttribute(self, anAttribute: TDF_Attribute | None, append: bool = True) -> None:
        """
        Adds an Attribute to the current label. Raises if
        there is already one.
        """

    @overload
    def ForgetAttribute(self, anAttribute: TDF_Attribute | None) -> None:
        """
        Forgets an Attribute from the current label,
        setting its forgotten status true and its valid
        status false. Raises if the attribute is not in
        the structure.
        """

    @overload
    def ForgetAttribute(self, aguid: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Forgets the Attribute of GUID <aguid> from the
        current label. If the attribute doesn't exist
        returns False. Otherwise returns True.
        """

    def ForgetAllAttributes(self, clearChildren: bool = True) -> None:
        """
        Forgets all the attributes. Does it on also on the
        sub-labels if <clearChildren> is set to true. Of
        course, this method is compatible with Transaction
        & Delta mechanisms.
        """

    def ResumeAttribute(self, anAttribute: TDF_Attribute | None) -> None:
        """
        Undo Forget action, setting its forgotten status
        false and its valid status true. Raises if the
        attribute is not in the structure.
        """

    @overload
    def FindAttribute(self, anID: nanoocp.Standard.Standard_GUID) -> tuple[bool, TDF_Attribute]:
        """
        Finds an attribute of the current label, according
        to <anID>.
        If anAttribute is not a valid one, false is returned.

        The method returns True if found, False otherwise.

        A removed attribute cannot be found.
        """

    @overload
    def FindAttribute(self, anID: nanoocp.Standard.Standard_GUID, aTransaction: int) -> tuple[bool, TDF_Attribute]:
        """
        Finds an attribute of the current label, according
        to <anID> and <aTransaction>. This attribute
        has/had to be a valid one for the given
        transaction index. So, this attribute is not
        necessarily a valid one.

        The method returns True if found, False otherwise.

        A removed attribute cannot be found nor a backuped
        attribute of a removed one.
        """

    def MayBeModified(self) -> bool:
        """
        Returns true if <me> or a DESCENDANT of <me> owns
        attributes not yet available in transaction 0. It
        means at least one of their attributes is new,
        modified or deleted.
        """

    def AttributesModified(self) -> bool:
        """
        Returns true if <me> owns attributes not yet
        available in transaction 0. It means at least one
        attribute is new, modified or deleted.
        """

    def HasAttribute(self) -> bool:
        """Returns true if this label has at least one attribute."""

    def NbAttributes(self) -> int:
        """Returns the number of attributes."""

    def Depth(self) -> int:
        """
        Returns the depth of the label in the data framework.
        This corresponds to the number of fathers which
        this label has, and is used in determining
        whether a label is root, null or equivalent to another label.
        Exceptions:
        Standard_NullObject if this label is null. This is
        because a null object can have no depth.
        """

    def IsDescendant(self, aLabel: TDF_Label) -> bool:
        """
        Returns True if <me> is a descendant of
        <aLabel>. Attention: every label is its own
        descendant.
        """

    def Root(self) -> TDF_Label:
        """
        Returns the root label Root of the data structure.
        This has a depth of 0.
        Exceptions:
        Standard_NullObject if this label is null. This is
        because a null object can have no depth.
        """

    def HasChild(self) -> bool:
        """Returns true if this label has at least one child."""

    def NbChildren(self) -> int:
        """Returns the number of children."""

    def FindChild(self, aTag: int, create: bool = True) -> TDF_Label:
        """
        Finds a child label having <aTag> as tag. Creates
        The tag aTag identifies the label which will be the parent.
        If create is true and no child label is found, a new one is created.
        Example:
        //creating a label with tag 10 at Root
        TDF_Label lab1 = aDF->Root().FindChild(10);
        //creating labels 7 and 2 on label 10
        TDF_Label lab2 = lab1.FindChild(7);
        TDF_Label lab3 = lab1.FindChild(2);
        """

    def NewChild(self) -> TDF_Label:
        """
        Create a new child label of me using automatic
        delivery tags provided by TagSource.
        """

    def Transaction(self) -> int:
        """Returns the current transaction index."""

    def HasLowerNode(self, otherLabel: TDF_Label) -> bool:
        """
        Returns true if node address of <me> is lower than
        <otherLabel> one. Used to quickly sort labels (not
        on entry criterion).

        -C++: inline
        """

    def HasGreaterNode(self, otherLabel: TDF_Label) -> bool:
        """
        Returns true if node address of <me> is greater
        than <otherLabel> one. Used to quickly sort labels
        (not on entry criterion).

        -C++: inline
        """

    def Dump(self) -> str:
        """
        Dumps the minimum information about <me> on
        <aStream>.
        """

    def ExtendedDump(self, aFilter: TDF_IDFilter, aMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TDF.TDF_Attribute]) -> str:
        """
        Dumps the label on <aStream> and its attributes
        rank in <aMap> if their IDs are kept by <IDFilter>.
        """

    def EntryDump(self) -> str:
        """Dumps the label entry."""

    def __hash__(self) -> int: ...

class TDF_TagSource(TDF_Attribute):
    """
    This attribute manage a tag provider to create
    child labels of a given one.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_TagSource) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Set_s(label: TDF_Label) -> TDF_TagSource:
        """
        Find, or create, a TagSource attribute. the TagSource
        attribute is returned.
        """

    @staticmethod
    def NewChild_s(L: TDF_Label) -> TDF_Label:
        """
        Find (or create) a tagSource attribute located at <L>
        and make a new child label.
        TagSource methods
        =================
        """

    def NewTag(self) -> int: ...

    def NewChild(self) -> TDF_Label: ...

    def Get(self) -> int: ...

    def Set(self, T: int) -> None:
        """
        TDF_Attribute methods
        =====================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> TDF_Attribute: ...

    def Paste(self, Into: TDF_Attribute | None, RT: TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_Data(nanoocp.Standard.Standard_Transient):
    """
    This class is used to manipulate a complete independent,
    self sufficient data structure and its services:

    Access to the root label;

    Opens, aborts, commits a transaction;

    Generation and use of Delta, depending on the time.
    This class uses a special allocator
    (see LabelNodeAllocator() method)
    for more efficient allocation of objects in memory.
    """

    @overload
    def __init__(self) -> None:
        """A new and empty Data structure."""

    @overload
    def __init__(self, theOther: TDF_Data) -> None: ...

    def Root(self) -> TDF_Label:
        """Returns the root label of the Data structure."""

    def Transaction(self) -> int:
        """Returns the current transaction number."""

    def Time(self) -> int:
        """Returns the current tick. It is incremented each Commit."""

    def IsApplicable(self, aDelta: TDF_Delta | None) -> bool:
        """Returns true if <aDelta> is applicable HERE and NOW."""

    def Undo(self, aDelta: TDF_Delta | None, withDelta: bool = False) -> TDF_Delta:
        """
        Apply <aDelta> to undo a set of attribute modifications.

        Optional <withDelta> set to True indicates a
        Delta Set must be generated. (See above)
        """

    def Destroy(self) -> None: ...

    def NotUndoMode(self) -> bool:
        """Returns the undo mode status."""

    def Dump(self) -> str:
        """Dumps the Data on <aStream>."""

    def AllowModification(self, isAllowed: bool) -> None:
        """Sets modification mode."""

    def IsModificationAllowed(self) -> bool:
        """returns modification mode."""

    def SetAccessByEntries(self, aSet: bool) -> None:
        """
        Initializes a mechanism for fast access to the labels by their entries.
        The fast access is useful for large documents and often access to the labels
        via entries. Internally, a table of entry - label is created,
        which allows to obtain a label by its entry in a very fast way.
        If the mechanism is turned off, the internal table is cleaned.
        New labels are added to the table, if the mechanism is on
        (no need to re-initialize the mechanism).
        """

    def IsAccessByEntries(self) -> bool:
        """
        Returns a status of mechanism for fast access to the labels via entries.
        """

    def GetLabel(self, anEntry: nanoocp.TCollection.TCollection_AsciiString, aLabel: TDF_Label) -> bool:
        """
        Returns a label by an entry.
        Returns false, if such a label doesn't exist
        or mechanism for fast access to the label by entry is not initialized.
        """

    def RegisterLabel(self, aLabel: TDF_Label) -> None:
        """
        An internal method. It is used internally on creation of new labels.
        It adds a new label into internal table for fast access to the labels by entry.
        """

    def LabelNodeAllocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator:
        """
        Returns TDF_HAllocator, which is an
        incremental allocator used by
        TDF_LabelNode.
        This allocator is used to
        manage TDF_LabelNode objects,
        but it can also be used for
        allocating memory to
        application-specific data (be
        careful because this
        allocator does not release
        the memory).
        The benefits of this
        allocation scheme are
        noticeable when dealing with
        large OCAF documents, due to:
        1.    Very quick allocation of
        objects (memory heap is not
        used, the algorithm that
        replaces it is very simple).
        2.    Very quick destruction of
        objects (memory is released not
        by destructors of TDF_LabelNode,
        but rather by the destructor of
        TDF_Data).
        3.  TDF_LabelNode objects do not
        fragmentize the memory; they are
        kept compactly in a number of
        arrays of 16K each.
        4.    Swapping is reduced on large
        data, because each document now
        occupies a smaller number of
        memory pages.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_AttributeDelta(nanoocp.Standard.Standard_Transient):
    """
    This class describes the services we need to
    implement Delta and Undo/Redo services.

    AttributeDeltas are applied in an unpredictable
    order. But by the redefinition of the method
    IsNowApplicable, a condition can be verified
    before application. If the AttributeDelta is not
    yet applicable, it is put at the end of the
    AttributeDelta list, to be treated later. If a
    dead lock if found on the list, the
    AttributeDeltas are forced to be applied in an
    unpredictable order.
    """

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    def Label(self) -> TDF_Label:
        """Returns the label concerned by <me>."""

    def Attribute(self) -> TDF_Attribute:
        """Returns the reference attribute."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute concerned by <me>."""

    def Dump(self) -> str:
        """Dumps the contents."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_AttributeIterator:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aLabel: TDF_Label, withoutForgotten: bool = True) -> None: ...

    @overload
    def __init__(self, aLabelNode: "TDF_LabelNode", withoutForgotten: bool = True) -> None: ...

    @overload
    def __init__(self, theOther: TDF_AttributeIterator) -> None: ...

    def __iter__(self) -> TDF_AttributeIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> TDF_Attribute:
        """Python addition: see __iter__."""

    def Initialize(self, aLabel: TDF_Label, withoutForgotten: bool = True) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Value(self) -> TDF_Attribute: ...

    def PtrValue(self) -> TDF_Attribute:
        """
        Provides an access to the internal pointer of the current attribute.
        The method has better performance as not-creating handle.
        """

class TDF_ChildIterator:
    """
    Iterates on the children of a label, at the first
    level only. It is possible to ask the iterator to
    explore all the sub label levels of the given one,
    with the option "allLevels".
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty iterator object to
        explore the children of a label.
        """

    @overload
    def __init__(self, aLabel: TDF_Label, allLevels: bool = False) -> None:
        """
        Constructs the iterator object defined by
        the label aLabel. Iterates on the children of the given label. If
        <allLevels> option is set to true, it explores not
        only the first, but all the sub label levels.
        """

    @overload
    def __init__(self, theOther: TDF_ChildIterator) -> None: ...

    def __iter__(self) -> TDF_ChildIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> TDF_Label:
        """Python addition: see __iter__."""

    def Initialize(self, aLabel: TDF_Label, allLevels: bool = False) -> None:
        """
        Initializes the iteration on the children of the
        given label.
        If <allLevels> option is set to true,
        it explores not only the first, but all the sub
        label levels.
        If allLevels is false, only the first level of
        child labels is explored.
        In the example below, the label is iterated
        using Initialize, More and Next and its
        child labels dumped using TDF_Tool::Entry.
        Example
        void DumpChildren(const
        TDF_Label& aLabel)
        {
        TDF_ChildIterator it;
        TCollection_AsciiString es;
        for
        (it.Initialize(aLabel,true);
        it.More(); it.Next()){
        TDF_Tool::Entry(it.Value(),es);
        std::cout << as.ToCString() << std::endl;
        }
        }
        """

    def More(self) -> bool:
        """
        Returns true if a current label is found in the
        iteration process.
        """

    def Next(self) -> None:
        """Move the current iteration to the next Item."""

    def NextBrother(self) -> None:
        """
        Moves this iteration to the next brother
        label. A brother label is one with the same
        father as an initial label.
        Use this function when the non-empty
        constructor or Initialize has allLevels set to
        true. The result is that the iteration does not
        explore the children of the current label.
        This method is interesting only with
        "allLevels" behavior, because it avoids to explore
        the current label children.
        """

    def Value(self) -> TDF_Label:
        """
        Returns the current label; or, if there is
        none, a null label.
        """

class TDF_ChildIDIterator:
    """
    Iterates on the children of a label, to find
    attributes having ID as Attribute ID.

    Level option works as TDF_ChildIterator.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty iterator."""

    @overload
    def __init__(self, aLabel: TDF_Label, anID: nanoocp.Standard.Standard_GUID, allLevels: bool = False) -> None:
        """
        Iterates on the children of the given label. If
        <allLevels> option is set to true, it explores not
        only the first, but all the sub label levels.
        """

    @overload
    def __init__(self, theOther: TDF_ChildIDIterator) -> None: ...

    def __iter__(self) -> TDF_ChildIDIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> TDF_Attribute:
        """Python addition: see __iter__."""

    def Initialize(self, aLabel: TDF_Label, anID: nanoocp.Standard.Standard_GUID, allLevels: bool = False) -> None:
        """
        Initializes the iteration on the children of the
        given label. If <allLevels> option is set to true,
        it explores not only the first, but all the sub
        label levels.
        """

    def More(self) -> bool:
        """
        Returns True if there is a current Item in the
        iteration.
        """

    def Next(self) -> None:
        """Move to the next Item"""

    def NextBrother(self) -> None:
        """
        Move to the next Brother. If there is none, go up
        etc. This method is interesting only with
        "allLevels" behavior, because it avoids to explore
        the current label children.
        """

    def Value(self) -> TDF_Attribute:
        """Returns the current item; a null handle if there is none."""

class TDF_ClosureMode:
    """This class provides options closure management."""

    @overload
    def __init__(self, aMode: bool = True) -> None:
        """Creates an object with all modes set to <aMode>."""

    @overload
    def __init__(self, theOther: TDF_ClosureMode) -> None: ...

    @overload
    def Descendants(self, aStatus: bool) -> None:
        """
        Sets the mode "Descendants" to <aStatus>.

        "Descendants" mode means we add to the data set
        the children labels of each USER GIVEN label. We
        do not do that with the labels found applying
        UpToFirstLevel option.
        """

    @overload
    def Descendants(self) -> bool:
        """Returns true if the mode "Descendants" is set."""

    @overload
    def References(self, aStatus: bool) -> None:
        """
        Sets the mode "References" to <aStatus>.

        "References" mode means we add to the data set
        the descendants of an attribute, by calling the
        attribute method Descendants().
        """

    @overload
    def References(self) -> bool:
        """Returns true if the mode "References" is set."""

class TDF_ClosureTool:
    """
    This class provides services to build the closure
    of an information set.
    This class gives services around the transitive
    enclosure of a set of information, starting from a
    list of label.
    You can set closure options by using IDFilter
    (to select or exclude specific attribute IDs) and
    CopyOption objects and by giving to Closure
    method.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_ClosureTool) -> None: ...

    @overload
    @staticmethod
    def Closure(aDataSet: TDF_DataSet | None) -> None:
        """
        Builds the transitive closure of label and
        attribute sets into <aDataSet>.
        """

    @overload
    @staticmethod
    def Closure(aDataSet: TDF_DataSet | None, aFilter: TDF_IDFilter, aMode: TDF_ClosureMode) -> None:
        """
        Builds the transitive closure of label and
        attribute sets into <aDataSet>. Uses <aFilter> to
        determine if an attribute has to be taken in
        account or not. Uses <aMode> for various way of
        closing.
        """

    @overload
    @staticmethod
    def Closure(aLabel: TDF_Label, aLabMap: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], anAttMap: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute], aFilter: TDF_IDFilter, aMode: TDF_ClosureMode) -> None:
        """Builds the transitive closure of <aLabel>."""

class TDF_ComparisonTool:
    """
    This class provides services to compare sets of
    information. The use of this tool can works after
    a copy, acted by a CopyTool.

    * Compare(...) compares two DataSet and returns the result.

    * SourceUnbound(...) builds the difference between
    a relocation dictionary and a source set of information.

    * TargetUnbound(...) does the same between a
    relocation dictionary and a target set of information.

    * Cut(aDataSet, anLabel) removes a set of attributes.

    * IsSelfContained(...) returns true if all the
    labels of the attributes of the given DataSet are
    descendant of the given label.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_ComparisonTool) -> None: ...

    @staticmethod
    def Compare(aSourceDataSet: TDF_DataSet | None, aTargetDataSet: TDF_DataSet | None, aFilter: TDF_IDFilter, aRelocationTable: TDF_RelocationTable | None) -> None:
        """
        Compares <aSourceDataSet> with <aTargetDataSet>,
        updating <aRelocationTable> with labels and
        attributes found in both sets.
        """

    @staticmethod
    def SourceUnbound(aRefDataSet: TDF_DataSet | None, aRelocationTable: TDF_RelocationTable | None, aFilter: TDF_IDFilter, aDiffDataSet: TDF_DataSet | None, anOption: int = 2) -> bool:
        """
        Finds from <aRefDataSet> all the keys not bound
        into <aRelocationTable> and put them into
        <aDiffDataSet>. Returns True if the difference
        contains at least one key. (A key is a source
        object).

        <anOption> may take the following values:
        1 : labels treatment only;
        2 : attributes treatment only (default value);
        3 : both labels & attributes treatment.
        """

    @staticmethod
    def TargetUnbound(aRefDataSet: TDF_DataSet | None, aRelocationTable: TDF_RelocationTable | None, aFilter: TDF_IDFilter, aDiffDataSet: TDF_DataSet | None, anOption: int = 2) -> bool:
        """
        Subtracts from <aRefDataSet> all the items bound
        into <aRelocationTable>. The result is put into
        <aDiffDataSet>. Returns True if the difference
        contains at least one item. (An item is a target
        object).

        <anOption> may take the following values:
        1 : labels treatment only;
        2 : attributes treatment only (default value);
        3 : both labels & attributes treatment.
        """

    @staticmethod
    def Cut(aDataSet: TDF_DataSet | None) -> None:
        """Removes attributes from <aDataSet>."""

    @staticmethod
    def IsSelfContained(aLabel: TDF_Label, aDataSet: TDF_DataSet | None) -> bool:
        """
        Returns true if all the labels of <aDataSet> are
        descendant of <aLabel>.
        """

class TDF_IDFilter:
    """This class offers filtering services around an ID list."""

    def __init__(self, ignoreMode: bool = True) -> None:
        """
        Creates an ID/attribute filter based on an ID
        list. The default mode is "ignore all but...".

        This filter has 2 working mode: keep and ignore.

        Ignore/Exclusive mode: all IDs are ignored except
        these set to be kept, using Keep(). Of course, it
        is possible set an kept ID to be ignored using
        Ignore().

        Keep/Inclusive mode: all IDs are kept except these
        set to be ignored, using Ignore(). Of course, it
        is possible set an ignored ID to be kept using
        Keep().
        """

    @overload
    def IgnoreAll(self, ignore: bool) -> None:
        """
        The list of ID is cleared and the filter mode is
        set to ignore mode if <keep> is true; false
        otherwise.
        """

    @overload
    def IgnoreAll(self) -> bool:
        """
        Returns true is the mode is set to "ignore all
        but...".
        """

    @overload
    def Keep(self, anID: nanoocp.Standard.Standard_GUID) -> None:
        """
        An attribute with <anID> as ID is to be kept and
        the filter will answer true to the question
        IsKept(<anID>).
        """

    @overload
    def Keep(self, anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        Attributes with ID owned by <anIDList> are to be kept and
        the filter will answer true to the question
        IsKept(<anID>) with ID from <anIDList>.
        """

    @overload
    def Ignore(self, anID: nanoocp.Standard.Standard_GUID) -> None:
        """
        An attribute with <anID> as ID is to be ignored and
        the filter will answer false to the question
        IsKept(<anID>).
        """

    @overload
    def Ignore(self, anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        Attributes with ID owned by <anIDList> are to be
        ignored and the filter will answer false to the
        question IsKept(<anID>) with ID from <anIDList>.
        """

    @overload
    def IsKept(self, anID: nanoocp.Standard.Standard_GUID) -> bool:
        """Returns true if the ID is to be kept."""

    @overload
    def IsKept(self, anAtt: TDF_Attribute | None) -> bool:
        """Returns true if the attribute is to be kept."""

    @overload
    def IsIgnored(self, anID: nanoocp.Standard.Standard_GUID) -> bool:
        """Returns true if the ID is to be ignored."""

    @overload
    def IsIgnored(self, anAtt: TDF_Attribute | None) -> bool:
        """Returns true if the attribute is to be ignored."""

    def IDList(self, anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        Copies the list of ID to be kept or ignored in
        <anIDList>. <anIDList> is cleared before use.
        """

    def Copy(self, fromFilter: TDF_IDFilter) -> None:
        """
        Copies into <me> the contents of
        <fromFilter>. <me> is cleared before copy.
        """

    def Dump(self) -> str:
        """Writes the contents of <me> to <OS>."""

    def Assign(self, theFilter: TDF_IDFilter) -> None:
        """Assignment"""

class TDF_CopyLabel:
    """This class gives copy of source label hierarchy"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, aSource: TDF_Label, aTarget: TDF_Label) -> None:
        """CopyTool"""

    def Load(self, aSource: TDF_Label, aTarget: TDF_Label) -> None:
        """Loads src and tgt labels"""

    def UseFilter(self, aFilter: TDF_IDFilter) -> None:
        """Sets filter"""

    @overload
    @staticmethod
    def ExternalReferences(Lab: TDF_Label, aExternals: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute], aFilter: TDF_IDFilter) -> bool: ...

    @overload
    @staticmethod
    def ExternalReferences(aRefLab: TDF_Label, Lab: TDF_Label, aExternals: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute], aFilter: TDF_IDFilter) -> TDF_DataSet:
        """Check external references and if exist fills the aExternals Map"""

    def Perform(self) -> None:
        """performs algorithm of selfcontained copy"""

    def IsDone(self) -> bool: ...

    def RelocationTable(self) -> TDF_RelocationTable:
        """returns relocation table"""

class TDF_CopyTool:
    """
    This class provides services to build, copy or
    paste a set of information.

    Copy methods:
    -------------

    * Copy(aSourceDataSet, aTargetLabel,
    aRelocationTable) copies a source DataSet under
    its target place (see below: IMPORTANT NOTICE 1).

    * Copy(aSourceDataSet, anTargetLabel,
    aRelocationTable, aFilter) does the same job as
    the previous method. But <aFilter> gives a list of
    IDs for which a target attribute prevails over a
    source one. In this special case, the source
    attribute will be copied only if there will be no
    target attribute.

    IMPORTANT NOTICE : Label pre-binding
    ------------------

    For it is possible to copy root labels in another
    place in the same Data or in a different one with
    other tags, it is necessary to inform the Copy
    algorithm about the target place. To do so:

    * first get or create new target root labels;

    * then bind them with the source root labels using
    the relocation table method:
    SetRelocation(aSourceLabel, aTargetLabel);

    * finally call Copy(...) with the relocation table
    previously set. In this way, this method will take
    these relocations in account.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_CopyTool) -> None: ...

    @overload
    @staticmethod
    def Copy(aSourceDataSet: TDF_DataSet | None, aRelocationTable: TDF_RelocationTable | None) -> None:
        """
        Copy <aSourceDataSet> with using and updating
        <aRelocationTable>. This method ignores target
        attributes privilege over source ones.
        """

    @overload
    @staticmethod
    def Copy(aSourceDataSet: TDF_DataSet | None, aRelocationTable: TDF_RelocationTable | None, aPrivilegeFilter: TDF_IDFilter) -> None:
        """
        Copy <aSourceDataSet> using and updating
        <aRelocationTable>. Use <aPrivilegeFilter> to give
        a list of IDs for which the target attribute
        prevails over the source one.
        """

    @overload
    @staticmethod
    def Copy(aSourceDataSet: TDF_DataSet | None, aRelocationTable: TDF_RelocationTable | None, aPrivilegeFilter: TDF_IDFilter, aRefFilter: TDF_IDFilter, setSelfContained: bool) -> None:
        """
        Copy <aSourceDataSet> using and updating
        <aRelocationTable>. Use <aPrivilegeFilter> to give
        a list of IDs for which the target attribute
        prevails over the source one. If <setSelfContained>
        is set to true, every TDF_Reference will be
        replaced by the referenced structure
        according to <aRefFilter>.

        NB: <aRefFilter> is used only if <setSelfContained>
        is true.
        Internal root label copy recursive method.
        """

class TDF_DataSet(nanoocp.Standard.Standard_Transient):
    """This class is a set of TDF information like labels and attributes."""

    @overload
    def __init__(self) -> None:
        """Creates an empty DataSet object."""

    @overload
    def __init__(self, theOther: TDF_DataSet) -> None: ...

    def Clear(self) -> None:
        """Clears all information."""

    def IsEmpty(self) -> bool:
        """
        Returns true if there is at least one label or one
        attribute.
        """

    def AddLabel(self, aLabel: TDF_Label) -> None:
        """Adds <aLabel> in the current data set."""

    def ContainsLabel(self, aLabel: TDF_Label) -> bool:
        """Returns true if the label <alabel> is in the data set."""

    def Labels(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """
        Returns the map of labels in this data set.
        This map can be used directly, or updated.
        """

    def AddAttribute(self, anAttribute: TDF_Attribute | None) -> None:
        """Adds <anAttribute> into the current data set."""

    def ContainsAttribute(self, anAttribute: TDF_Attribute | None) -> bool:
        """Returns true if <anAttribute> is in the data set."""

    def Attributes(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]:
        """
        Returns the map of attributes in the current data set.
        This map can be used directly, or updated.
        """

    def AddRoot(self, aLabel: TDF_Label) -> None:
        """Adds a root label to <myRootLabels>."""

    def Roots(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]:
        """Returns <myRootLabels> to be used or updated."""

    def Dump(self) -> str:
        """
        Dumps the minimum information about <me> on
        <aStream>.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DeltaOnModification(TDF_AttributeDelta):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action.

    Applying this AttributeDelta means GOING BACK to
    the attribute previously registered state.
    """

    def __init__(self, theOther: TDF_DeltaOnModification) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DefaultDeltaOnModification(TDF_DeltaOnModification):
    """
    This class provides a default implementation of a
    TDF_DeltaOnModification.
    """

    @overload
    def __init__(self, anAttribute: TDF_Attribute | None) -> None:
        """
        Creates a TDF_DefaultDeltaOnModification.
        <anAttribute> must be the backup copy.
        """

    @overload
    def __init__(self, theOther: TDF_DefaultDeltaOnModification) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DeltaOnRemoval(TDF_AttributeDelta):
    """
    This class provides default services for an
    AttributeDelta on a REMOVAL action.

    Applying this AttributeDelta means ADDING its
    attribute.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DefaultDeltaOnRemoval(TDF_DeltaOnRemoval):
    """
    This class provides a default implementation of a
    TDF_DeltaOnRemoval.
    """

    @overload
    def __init__(self, anAttribute: TDF_Attribute | None) -> None:
        """Creates a TDF_DefaultDeltaOnRemoval."""

    @overload
    def __init__(self, theOther: TDF_DefaultDeltaOnRemoval) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_Delta(nanoocp.Standard.Standard_Transient):
    """
    A set of AttributeDelta for a given transaction
    number and reference time number.
    A delta set is available at <aSourceTime>. If
    applied, it restores the TDF_Data in the state it
    was at <aTargetTime>.
    """

    @overload
    def __init__(self) -> None:
        """Creates a delta."""

    @overload
    def __init__(self, theOther: TDF_Delta) -> None: ...

    def IsEmpty(self) -> bool:
        """Returns true if there is nothing to undo."""

    def IsApplicable(self, aCurrentTime: int) -> bool:
        """
        Returns true if the Undo action of <me> is
        applicable at <aCurrentTime>.
        """

    def BeginTime(self) -> int:
        """Returns the field <myBeginTime>."""

    def EndTime(self) -> int:
        """Returns the field <myEndTime>."""

    def Labels(self, aLabelList: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """
        Adds in <aLabelList> the labels of the attribute deltas.
        Caution: <aLabelList> is not cleared before use.
        """

    def AttributeDeltas(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_AttributeDelta]:
        """Returns the field <myAttDeltaList>."""

    def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns a name associated with this delta."""

    def SetName(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Associates a name <theName> with this delta"""

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DeltaOnAddition(TDF_AttributeDelta):
    """
    This class provides default services for an
    AttributeDelta on an ADDITION action.

    Applying this AttributeDelta means REMOVING its
    attribute.
    """

    @overload
    def __init__(self, anAtt: TDF_Attribute | None) -> None:
        """Creates a TDF_DeltaOnAddition."""

    @overload
    def __init__(self, theOther: TDF_DeltaOnAddition) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DeltaOnForget(TDF_AttributeDelta):
    """
    This class provides default services for an
    AttributeDelta on an Forget action.

    Applying this AttributeDelta means RESUMING its
    attribute.
    """

    @overload
    def __init__(self, anAtt: TDF_Attribute | None) -> None:
        """Creates a TDF_DeltaOnForget."""

    @overload
    def __init__(self, theOther: TDF_DeltaOnForget) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DeltaOnResume(TDF_AttributeDelta):
    """
    This class provides default services for an
    AttributeDelta on an Resume action.

    Applying this AttributeDelta means FORGETTING its
    attribute.
    """

    @overload
    def __init__(self, anAtt: TDF_Attribute | None) -> None:
        """Creates a TDF_DeltaOnResume."""

    @overload
    def __init__(self, theOther: TDF_DeltaOnResume) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_DerivedAttribute:
    """
    Class provides global access (through static methods) to all derived attributes information.
    It is used internally by macros for registration of derived attributes and driver-tables
    for getting this data.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_DerivedAttribute) -> None: ...

    @staticmethod
    def Attribute(theType: str) -> TDF_Attribute:
        """Returns the derived registered attribute by its type."""

    @staticmethod
    def TypeName(theType: str) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the type name of the registered attribute by its type."""

    @staticmethod
    def Attributes(theList: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Attribute]) -> None:
        """Returns all the derived registered attributes list."""

class TDF_Reference(TDF_Attribute):
    """
    This attribute is used to store in the framework a
    reference to an other label.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_Reference) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set_s(I: TDF_Label, Origin: TDF_Label) -> TDF_Reference: ...

    def Set(self, Origin: TDF_Label) -> None: ...

    def Get(self) -> TDF_Label: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> TDF_Attribute: ...

    def Paste(self, Into: TDF_Attribute | None, RT: TDF_RelocationTable | None) -> None: ...

    def References(self, DS: TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_RelocationTable(nanoocp.Standard.Standard_Transient):
    """
    This is a relocation dictionary between source
    and target labels, attributes or any
    transient(useful for copy or paste actions).
    Note that one target value may be the
    relocation value of more than one source object.

    Common behaviour: it returns true and the found
    relocation value as target object; false
    otherwise.

    Look at SelfRelocate method for more explanation
    about self relocation behavior of this class.
    """

    @overload
    def __init__(self, selfRelocate: bool = False) -> None:
        """
        Creates an relocation table. <selfRelocate> says
        if a value without explicit relocation is its own
        relocation.
        """

    @overload
    def __init__(self, theOther: TDF_RelocationTable) -> None: ...

    @overload
    def SelfRelocate(self, selfRelocate: bool) -> None:
        """
        Sets <mySelfRelocate> to <selfRelocate>.

        This flag affects the HasRelocation method
        behavior like this:

        <mySelfRelocate> == False:

        If no relocation object is found in the map, a
        null object is returned

        <mySelfRelocate> == True:

        If no relocation object is found in the map, the
        method assumes the source object is relocation
        value; so the source object is returned as target
        object.
        """

    @overload
    def SelfRelocate(self) -> bool:
        """Returns <mySelfRelocate>."""

    @overload
    def AfterRelocate(self, afterRelocate: bool) -> None: ...

    @overload
    def AfterRelocate(self) -> bool:
        """Returns <myAfterRelocate>."""

    @overload
    def SetRelocation(self, aSourceLabel: TDF_Label, aTargetLabel: TDF_Label) -> None:
        """
        Sets the relocation value of <aSourceLabel> to
        <aTargetLabel>.
        """

    @overload
    def SetRelocation(self, aSourceAttribute: TDF_Attribute | None, aTargetAttribute: TDF_Attribute | None) -> None:
        """
        Sets the relocation value of <aSourceAttribute> to
        <aTargetAttribute>.
        """

    @overload
    def HasRelocation(self, aSourceLabel: TDF_Label, aTargetLabel: TDF_Label) -> bool:
        """
        Finds the relocation value of <aSourceLabel>
        and returns it into <aTargetLabel>.

        (See above SelfRelocate method for more
        explanation about the method behavior)
        """

    @overload
    def HasRelocation(self, aSourceAttribute: TDF_Attribute | None) -> tuple[bool, TDF_Attribute]:
        """
        Finds the relocation value of <aSourceAttribute>
        and returns it into <aTargetAttribute>.

        (See above SelfRelocate method for more
        explanation about the method behavior)
        """

    def SetTransientRelocation(self, aSourceTransient: nanoocp.Standard.Standard_Transient | None, aTargetTransient: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Sets the relocation value of <aSourceTransient> to
        <aTargetTransient>.
        """

    def HasTransientRelocation(self, aSourceTransient: nanoocp.Standard.Standard_Transient | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Finds the relocation value of <aSourceTransient>
        and returns it into <aTargetTransient>.

        (See above SelfRelocate method for more
        explanation about the method behavior)
        """

    def Clear(self) -> None:
        """
        Clears the relocation dictionary, but lets the
        self relocation flag to its current value.
        """

    def TargetLabelMap(self, aLabelMap: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None:
        """
        Fills <aLabelMap> with target relocation
        labels. <aLabelMap> is not cleared before use.
        """

    def TargetAttributeMap(self, anAttributeMap: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]) -> None:
        """
        Fills <anAttributeMap> with target relocation
        attributes. <anAttributeMap> is not cleared before
        use.
        """

    def LabelTable(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TDF.TDF_Label, nanoocp.TDF.TDF_Label]:
        """Returns <myLabelTable> to be used or updated."""

    def AttributeTable(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TDF.TDF_Attribute, nanoocp.TDF.TDF_Attribute]:
        """Returns <myAttributeTable> to be used or updated."""

    def TransientTable(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]:
        """Returns <myTransientTable> to be used or updated."""

    def Dump(self, dumpLabels: bool, dumpAttributes: bool, dumpTransients: bool) -> str:
        """Dumps the relocation table."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDF_Tool:
    """This class provides general services for a data framework."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDF_Tool) -> None: ...

    @staticmethod
    def NbLabels(aLabel: TDF_Label) -> int:
        """
        Returns the number of labels of the tree,
        including <aLabel>. aLabel is also included in this figure.
        This information is useful in setting the size of an array.
        """

    @overload
    @staticmethod
    def NbAttributes(aLabel: TDF_Label) -> int:
        """
        Returns the total number of attributes attached
        to the labels dependent on the label aLabel.
        The attributes of aLabel are also included in this figure.
        This information is useful in setting the size of an array.
        """

    @overload
    @staticmethod
    def NbAttributes(aLabel: TDF_Label, aFilter: TDF_IDFilter) -> int:
        """
        Returns the number of attributes of the tree,
        selected by a<Filter>, including those of
        <aLabel>.
        """

    @overload
    @staticmethod
    def IsSelfContained(aLabel: TDF_Label) -> bool:
        """
        Returns true if <aLabel> and its descendants
        reference only attributes or labels attached to
        themselves.
        """

    @overload
    @staticmethod
    def IsSelfContained(aLabel: TDF_Label, aFilter: TDF_IDFilter) -> bool:
        """
        Returns true if <aLabel> and its descendants
        reference only attributes or labels attached to
        themselves and kept by <aFilter>.
        """

    @overload
    @staticmethod
    def OutReferers(theLabel: TDF_Label, theAtts: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]) -> None:
        """
        Returns in <theAtts> the attributes having out
        references.

        Caution: <theAtts> is not cleared before use!
        """

    @overload
    @staticmethod
    def OutReferers(aLabel: TDF_Label, aFilterForReferers: TDF_IDFilter, aFilterForReferences: TDF_IDFilter, atts: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]) -> None:
        """
        Returns in <atts> the attributes having out
        references and kept by <aFilterForReferers>.
        It considers only the references kept by <aFilterForReferences>.
        Caution: <atts> is not cleared before use!
        """

    @overload
    @staticmethod
    def OutReferences(aLabel: TDF_Label, atts: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]) -> None:
        """
        Returns in <atts> the referenced attributes.
        Caution: <atts> is not cleared before use!
        """

    @overload
    @staticmethod
    def OutReferences(aLabel: TDF_Label, aFilterForReferers: TDF_IDFilter, aFilterForReferences: TDF_IDFilter, atts: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]) -> None:
        """
        Returns in <atts> the referenced attributes and kept by <aFilterForReferences>.
        It considers only the referrers kept by <aFilterForReferers>.
        Caution: <atts> is not cleared before use!
        """

    @staticmethod
    def RelocateLabel(aSourceLabel: TDF_Label, fromRoot: TDF_Label, toRoot: TDF_Label, aTargetLabel: TDF_Label, create: bool = False) -> None:
        """
        Returns the label having the same sub-entry as
        <aLabel> but located as descendant as <toRoot>
        instead of <fromRoot>.

        Example :

        aLabel = 0:3:24:7:2:7
        fromRoot = 0:3:24
        toRoot = 0:5
        returned label = 0:5:7:2:7
        """

    @staticmethod
    def Entry(aLabel: TDF_Label, anEntry: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Returns the entry for the label aLabel in the form
        of the ASCII character string anEntry containing
        the tag list for aLabel.
        """

    @overload
    @staticmethod
    def TagList(aLabel: TDF_Label, aTagList: nanoocp.NCollection.NCollection_List[int]) -> None:
        """
        Returns the entry of <aLabel> as list of integers
        in <aTagList>.
        """

    @overload
    @staticmethod
    def TagList(anEntry: nanoocp.TCollection.TCollection_AsciiString, aTagList: nanoocp.NCollection.NCollection_List[int]) -> None:
        """
        Returns the entry expressed by <anEntry> as list
        of integers in <aTagList>.
        """

    @overload
    @staticmethod
    def Label(aDF: TDF_Data | None, anEntry: nanoocp.TCollection.TCollection_AsciiString, aLabel: TDF_Label, create: bool = False) -> None: ...

    @overload
    @staticmethod
    def Label(aDF: TDF_Data | None, anEntry: str, aLabel: TDF_Label, create: bool = False) -> None: ...

    @overload
    @staticmethod
    def Label(aDF: TDF_Data | None, aTagList: nanoocp.NCollection.NCollection_List[int], aLabel: TDF_Label, create: bool = False) -> None:
        """
        Returns the label expressed by <anEntry>; creates
        the label if it does not exist and if <create> is
        true.
        """

    @staticmethod
    def CountLabels(aLabelList: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label], aLabelMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TDF.TDF_Label, int]) -> None:
        """
        Adds the labels of <aLabelList> to <aLabelMap> if
        they are unbound, or increases their reference
        counters. At the end of the process, <aLabelList>
        contains only the ADDED labels.
        """

    @staticmethod
    def DeductLabels(aLabelList: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label], aLabelMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TDF.TDF_Label, int]) -> None:
        """
        Decreases the reference counters of the labels of
        <aLabelList> to <aLabelMap>, and removes labels
        with null counter. At the end of the process,
        <aLabelList> contains only the SUPPRESSED labels.
        """

    @overload
    @staticmethod
    def DeepDump(aDF: TDF_Data | None) -> str:
        """Dumps <aDF> and its labels and their attributes."""

    @overload
    @staticmethod
    def DeepDump(aLabel: TDF_Label) -> str:
        """Dumps <aLabel>, its children and their attributes."""

    @overload
    @staticmethod
    def ExtendedDeepDump(aDF: TDF_Data | None, aFilter: TDF_IDFilter) -> str:
        """
        Dumps <aDF> and its labels and their attributes,
        if their IDs are kept by <aFilter>. Dumps also the
        attributes content.
        """

    @overload
    @staticmethod
    def ExtendedDeepDump(aLabel: TDF_Label, aFilter: TDF_IDFilter) -> str:
        """
        Dumps <aLabel>, its children and their attributes,
        if their IDs are kept by <aFilter>. Dumps also the
        attributes content.
        """

class TDF_Transaction:
    """
    This class offers services to open, commit or
    abort a transaction in a more secure way than
    using Data from TDF. If you forget to close a
    transaction, it will be automatically aborted at
    the destruction of this object, at the closure of
    its scope.

    In case of catching errors, the effect will be the
    same: aborting transactions until the good current
    one.
    """

    @overload
    def __init__(self, aName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """
        Creates an empty transaction context, unable to be
        opened.
        """

    @overload
    def __init__(self, aDF: TDF_Data | None, aName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """
        Creates a transaction context on <aDF>, ready to
        be opened.
        """

    def Initialize(self, aDF: TDF_Data | None) -> None:
        """
        Aborts all the transactions on <myDF> and sets
        <aDF> to build a transaction context on <aDF>,
        ready to be opened.
        """

    def Open(self) -> int:
        """
        If not yet done, opens a new transaction on
        <myDF>. Returns the index of the just opened
        transaction.

        It raises DomainError if the transaction is
        already open, and NullObject if there is no
        current Data framework.
        """

    def Commit(self, withDelta: bool = False) -> TDF_Delta:
        """
        Commits the transactions until AND including the
        current opened one.
        """

    def Abort(self) -> None:
        """
        Aborts the transactions until AND including the
        current opened one.
        """

    def Data(self) -> TDF_Data:
        """Returns the Data from TDF."""

    def Transaction(self) -> int:
        """Returns the number of the transaction opened by <me>."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the transaction name."""

    def IsOpen(self) -> bool:
        """Returns true if the transaction is open."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TDF
TDF_AttributeDeltaList = nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_AttributeDelta]
TDF_AttributeList = nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Attribute]
TDF_AttributeSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Attribute]
TDF_DeltaList = nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Delta]
TDF_IDList = nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]
TDF_LabelList = nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]
TDF_LabelSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]
