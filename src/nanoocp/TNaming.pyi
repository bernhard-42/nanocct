"""OCCT package TNaming (toolkit TKCAF)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TDF
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class TNaming_Evolution(enum.IntEnum):
    """
    Defines the type of evolution in old shape - new shape pairs.
    The definitions - in the form of the terms of
    the enumeration - are needed by the
    TNaming_NamedShape attribute and
    indicate what entities this attribute records as follows:
    -   PRIMITIVE
    -   New entities; in each pair, old shape is a
    null shape and new shape is a created
    entity.
    -   GENERATED
    -   Entities created from other entities; in
    each pair, old shape is the generator and
    new shape is the created entity.
    -   MODIFY
    -   Split or merged entities, in each pair, old
    shape is the entity before the operation
    and new shape is the new entity after the
    operation.
    -   DELETE
    -   Deletion of entities; in each pair, old
    shape is a deleted entity and new shape is null.
    -   SELECTED
    -   Named topological entities; in each pair,
    the new shape is a named entity and the
    old shape is not used.

    For a split which generates multiple faces, the
    attribute will contain many pairs with the same
    old shape; for a merge, it will contain many
    pairs with the same new shape.
    Finally, an example of delete would be a face
    removed by a Boolean operation.
    """

    TNaming_PRIMITIVE = 0

    TNaming_GENERATED = 1

    TNaming_MODIFY = 2

    TNaming_DELETE = 3

    TNaming_REPLACE = 4

    TNaming_SELECTED = 5

TNaming_PRIMITIVE: TNaming_Evolution = TNaming_Evolution.TNaming_PRIMITIVE

TNaming_GENERATED: TNaming_Evolution = TNaming_Evolution.TNaming_GENERATED

TNaming_MODIFY: TNaming_Evolution = TNaming_Evolution.TNaming_MODIFY

TNaming_DELETE: TNaming_Evolution = TNaming_Evolution.TNaming_DELETE

TNaming_REPLACE: TNaming_Evolution = TNaming_Evolution.TNaming_REPLACE

TNaming_SELECTED: TNaming_Evolution = TNaming_Evolution.TNaming_SELECTED

class TNaming_NameType(enum.IntEnum):
    """to store naming characteristcs"""

    TNaming_UNKNOWN = 0

    TNaming_IDENTITY = 1

    TNaming_MODIFUNTIL = 2

    TNaming_GENERATION = 3

    TNaming_INTERSECTION = 4

    TNaming_UNION = 5

    TNaming_SUBSTRACTION = 6

    TNaming_CONSTSHAPE = 7

    TNaming_FILTERBYNEIGHBOURGS = 8

    TNaming_ORIENTATION = 9

    TNaming_WIREIN = 10

    TNaming_SHELLIN = 11

TNaming_UNKNOWN: TNaming_NameType = TNaming_NameType.TNaming_UNKNOWN

TNaming_IDENTITY: TNaming_NameType = TNaming_NameType.TNaming_IDENTITY

TNaming_MODIFUNTIL: TNaming_NameType = TNaming_NameType.TNaming_MODIFUNTIL

TNaming_GENERATION: TNaming_NameType = TNaming_NameType.TNaming_GENERATION

TNaming_INTERSECTION: TNaming_NameType = TNaming_NameType.TNaming_INTERSECTION

TNaming_UNION: TNaming_NameType = TNaming_NameType.TNaming_UNION

TNaming_SUBSTRACTION: TNaming_NameType = TNaming_NameType.TNaming_SUBSTRACTION

TNaming_CONSTSHAPE: TNaming_NameType = TNaming_NameType.TNaming_CONSTSHAPE

TNaming_FILTERBYNEIGHBOURGS: TNaming_NameType = TNaming_NameType.TNaming_FILTERBYNEIGHBOURGS

TNaming_ORIENTATION: TNaming_NameType = TNaming_NameType.TNaming_ORIENTATION

TNaming_WIREIN: TNaming_NameType = TNaming_NameType.TNaming_WIREIN

TNaming_SHELLIN: TNaming_NameType = TNaming_NameType.TNaming_SHELLIN

class TNaming:
    """
    A topological attribute can be seen as a hook
    into the topological structure. To this hook,
    data can be attached and references defined.
    It is used for keeping and access to
    topological objects and their evolution. All
    topological objects are stored in the one
    user-protected TNaming_UsedShapes
    attribute at the root label of the data
    framework. This attribute contains map with all
    topological shapes, used in this document.
    To all other labels TNaming_NamedShape
    attribute can be added. This attribute contains
    references (hooks) to shapes from the
    TNaming_UsedShapes attribute and evolution
    of these shapes. TNaming_NamedShape
    attribute contains a set of pairs of hooks: old
    shape and new shape (see the figure below).
    It allows not only get the topological shapes by
    the labels, but also trace evolution of the
    shapes and correctly resolve dependent
    shapes by the changed one.
    If shape is just-created, then the old shape for
    accorded named shape is an empty shape. If
    a shape is deleted, then the new shape in this named shape is empty.
    Different algorithms may dispose sub-shapes
    of the result shape at the individual label depending on necessity:
    -  If a sub-shape must have some extra attributes (material of
    each face or color of each edge). In this case a specific sub-shape is
    placed to the separate label (usually, sub-label of the result shape label)
    with all attributes of this sub-shape.
    -  If topological naming is needed, a necessary and sufficient
    (for selected sub-shapes identification) set of sub-shapes is
    placed to the child labels of the result
    shape label. As usual, as far as basic solids and closed shells are
    concerned, all faces of the shape are disposed. Edges and vertices
    sub-shapes can be identified as intersection of contiguous faces.
    Modified/generated shapes may be placed to one named shape and
    identified as this named shape and source named shape that also can be
    identified with used algorithms.
    TNaming_NamedShape may contain a few
    pairs of hooks with the same evolution. In this
    case topology shape, which belongs to the
    named shape, is a compound of new shapes.
    The data model contains both the topology
    and the hooks, and functions handle both
    topological entities and hooks. Consider the
    case of a box function, which creates a solid
    with six faces and six hooks. Each hook is
    attached to a face. If you want, you can also
    have this function create hooks for edges and
    vertices as well as for faces. For the sake of
    simplicity though, let's limit the example.
    Not all functions can define explicit hooks for
    all topological entities they create, but all
    topological entities can be turned into hooks
    when necessary. This is where topological naming is necessary.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming) -> None: ...

    @staticmethod
    def Substitute(labelsource: nanoocp.TDF.TDF_Label, labelcible: nanoocp.TDF.TDF_Label, mapOldNew: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Subtituter les shapes sur les structures de source
        vers cible
        """

    @staticmethod
    def Update(label: nanoocp.TDF.TDF_Label, mapOldNew: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Mise a jour des shapes du label et de ses fils en
        tenant compte des substitutions decrite par
        mapOldNew.

        Warning: le remplacement du shape est fait dans tous
        les attributs qui le contiennent meme si ceux
        ci ne sont pas associees a des sous-labels de <Label>.
        """

    @staticmethod
    def Displace(label: nanoocp.TDF.TDF_Label, aLocation: nanoocp.TopLoc.TopLoc_Location, WithOld: bool = True) -> None:
        """
        Application de la Location sur les shapes du label
        et de ses sous labels.
        """

    @staticmethod
    def ChangeShapes(label: nanoocp.TDF.TDF_Label, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Remplace les shapes du label et des sous-labels
        par des copies.
        """

    @staticmethod
    def Transform(label: nanoocp.TDF.TDF_Label, aTransformation: nanoocp.gp.gp_Trsf) -> None:
        """
        Application de la transformation sur les shapes du
        label et de ses sous labels.
        Warning: le remplacement du shape est fait dans tous
        les attributs qui le contiennent meme si ceux
        ci ne sont pas associees a des sous-labels de <Label>.
        """

    @overload
    @staticmethod
    def Replicate(NS: TNaming_NamedShape | None, T: nanoocp.gp.gp_Trsf, L: nanoocp.TDF.TDF_Label) -> None:
        """
        Replicates the named shape with the transformation <T>
        on the label <L> (and sub-labels if necessary)
        (TNaming_GENERATED is set)
        """

    @overload
    @staticmethod
    def Replicate(SH: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.gp.gp_Trsf, L: nanoocp.TDF.TDF_Label) -> None:
        """
        Replicates the shape with the transformation <T>
        on the label <L> (and sub-labels if necessary)
        (TNaming_GENERATED is set)
        """

    @staticmethod
    def MakeShape(MS: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> nanoocp.TopoDS.TopoDS_Shape:
        """Builds shape from map content"""

    @staticmethod
    def FindUniqueContext(S: nanoocp.TopoDS.TopoDS_Shape, Context: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Find unique context of shape <S>"""

    @staticmethod
    def FindUniqueContextSet(S: nanoocp.TopoDS.TopoDS_Shape, Context: nanoocp.TopoDS.TopoDS_Shape) -> tuple[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_HArray1[nanoocp.TopoDS.TopoDS_Shape]]:
        """
        Find unique context of shape <S>,which is pure concatenation
        of atomic shapes (Compound). The result is concatenation of
        single contexts
        """

    @staticmethod
    def SubstituteSShape(accesslabel: nanoocp.TDF.TDF_Label, From: nanoocp.TopoDS.TopoDS_Shape, To: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Substitutes shape in source structure"""

    @staticmethod
    def OuterWire(theFace: nanoocp.TopoDS.TopoDS_Face, theWire: nanoocp.TopoDS.TopoDS_Wire) -> bool:
        """Returns True if outer wire is found and the found wire in <theWire>."""

    @staticmethod
    def OuterShell(theSolid: nanoocp.TopoDS.TopoDS_Solid, theShell: nanoocp.TopoDS.TopoDS_Shell) -> bool:
        """
        Returns True if outer Shell is found and the found shell in <theShell>.
        Print of TNaming enumeration
        =============================
        """

    @staticmethod
    def IDList(anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        Appends to <anIDList> the list of the attributes
        IDs of this package.
        CAUTION: <anIDList> is NOT cleared before use.
        """

    @overload
    @staticmethod
    def Print(EVOL: TNaming_Evolution) -> str:
        """
        Prints the evolution <EVOL> as a String on the
        Stream <S> and returns <S>.
        """

    @overload
    @staticmethod
    def Print(NAME: TNaming_NameType) -> str:
        """
        Prints the name of name type <NAME> as a String on
        the Stream <S> and returns <S>.
        """

    @overload
    @staticmethod
    def Print(ACCESS: nanoocp.TDF.TDF_Label) -> str:
        """
        Prints the content of UsedShapes private attribute as a String Table on
        the Stream <S> and returns <S>.
        """

class TNaming_Builder:
    """
    A tool to create and maintain topological attributes.
    Constructor creates an empty
    TNaming_NamedShape attribute at the given
    label. It allows adding "old shape" and "new
    shape" pairs with the specified evolution to this
    named shape. One evolution type per one
    builder must be used.
    """

    @overload
    def __init__(self, aLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        Create a Builder.
        Warning: Before Addition copies the current Value, and clear
        """

    @overload
    def __init__(self, theOther: TNaming_Builder) -> None: ...

    @overload
    def Generated(self, newShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Records the shape newShape which was
        generated during a topological construction.
        As an example, consider the case of a face
        generated in construction of a box.
        """

    @overload
    def Generated(self, oldShape: nanoocp.TopoDS.TopoDS_Shape, newShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Records the shape newShape which was
        generated from the shape oldShape during a topological construction.
        As an example, consider the case of a face
        generated from an edge in construction of a prism.
        """

    def Delete(self, oldShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Records the shape oldShape which was deleted from the current label.
        As an example, consider the case of a face removed by a Boolean operation.
        """

    def Modify(self, oldShape: nanoocp.TopoDS.TopoDS_Shape, newShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Records the shape newShape which is a
        modification of the shape oldShape.
        As an example, consider the case of a face split
        or merged in a Boolean operation.
        """

    def Select(self, aShape: nanoocp.TopoDS.TopoDS_Shape, inShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Add a Shape to the current label, This Shape is
        unmodified. Used for example to define a set
        of shapes under a label.
        """

    def NamedShape(self) -> TNaming_NamedShape:
        """Returns the NamedShape which has been built or is under construction."""

class TNaming_CopyShape:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_CopyShape) -> None: ...

    @staticmethod
    def CopyTool(aShape: nanoocp.TopoDS.TopoDS_Shape, aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient], aResult: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Makes copy a set of shape(s), using the aMap"""

    @overload
    @staticmethod
    def Translate(aShape: nanoocp.TopoDS.TopoDS_Shape, aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient], aResult: nanoocp.TopoDS.TopoDS_Shape, TrTool: TNaming_TranslateTool | None) -> None:
        """Translates a Transient shape(s) to Transient"""

    @overload
    @staticmethod
    def Translate(L: nanoocp.TopLoc.TopLoc_Location, aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]) -> nanoocp.TopLoc.TopLoc_Location:
        """
        Translates a Topological Location to an other Top.
        Location
        """

class TNaming_DeltaOnModification(nanoocp.TDF.TDF_DeltaOnModification):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action.

    Applying this AttributeDelta means GOING BACK to
    the attribute previously registered state.
    """

    @overload
    def __init__(self, NS: TNaming_NamedShape | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TNaming_DeltaOnModification) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TNaming_DeltaOnRemoval(nanoocp.TDF.TDF_DeltaOnRemoval):
    @overload
    def __init__(self, NS: TNaming_NamedShape | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TNaming_DeltaOnRemoval) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TNaming_NamedShape(nanoocp.TDF.TDF_Attribute):
    """
    The basis to define an attribute for the storage of
    topology and naming data.
    This attribute contains two parts:
    -   The type of evolution, a term of the
    enumeration TNaming_Evolution
    -   A list of pairs of shapes called the "old"
    shape and the "new" shape. The meaning
    depends on the type of evolution.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_NamedShape) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class method
        ============
        Returns the GUID for named shapes.
        """

    def IsEmpty(self) -> bool: ...

    def Get(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shapes contained in <NS>. Returns a null
        shape if IsEmpty.
        """

    def Evolution(self) -> TNaming_Evolution:
        """Returns the Evolution of the attribute."""

    def Version(self) -> int:
        """Returns the Version of the attribute."""

    def SetVersion(self, version: int) -> None:
        """Set the Version of the attribute."""

    def Clear(self) -> None: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def BackupCopy(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Copies the attribute contents into a new other
        attribute. It is used by Backup().
        """

    def Restore(self, anAttribute: nanoocp.TDF.TDF_Attribute | None) -> None:
        """
        Restores the contents from <anAttribute> into this
        one. It is used when aborting a transaction.
        """

    @overload
    def DeltaOnModification(self, anOldAttribute: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TDF.TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute.
        """

    @overload
    def DeltaOnModification(self, aDelta: nanoocp.TDF.TDF_DeltaOnModification | None) -> None:
        """Applies a DeltaOnModification to <me>."""

    def DeltaOnRemoval(self) -> nanoocp.TDF.TDF_DeltaOnRemoval:
        """
        Makes a DeltaOnRemoval on <me> because <me> has
        disappeared from the DS.
        """

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Returns an new empty attribute from the good end
        type. It is used by the copy algorithm.
        """

    def Paste(self, intoAttribute: nanoocp.TDF.TDF_Attribute | None, aRelocTationable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """
        This method is different from the "Copy" one,
        because it is used when copying an attribute from
        a source structure into a target structure. This
        method pastes the current attribute to the label
        corresponding to the insertor. The pasted
        attribute may be a brand new one or a new version
        of the previous one.
        """

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None:
        """
        Adds the directly referenced attributes and labels
        to <aDataSet>. "Directly" means we have only to
        look at the first level of references.
        """

    def BeforeRemoval(self) -> None: ...

    def BeforeUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """Something to do before applying <anAttDelta>"""

    def AfterUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """Something to do after applying <anAttDelta>."""

    def Dump(self) -> str:
        """Dumps the attribute on <aStream>."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TNaming_Identifier:
    @overload
    def __init__(self, Lab: nanoocp.TDF.TDF_Label, S: nanoocp.TopoDS.TopoDS_Shape, Context: nanoocp.TopoDS.TopoDS_Shape, Geom: bool) -> None: ...

    @overload
    def __init__(self, Lab: nanoocp.TDF.TDF_Label, S: nanoocp.TopoDS.TopoDS_Shape, ContextNS: TNaming_NamedShape | None, Geom: bool) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_Identifier) -> None: ...

    def IsDone(self) -> bool: ...

    def Type(self) -> TNaming_NameType: ...

    def IsFeature(self) -> bool: ...

    def Feature(self) -> TNaming_NamedShape: ...

    def InitArgs(self) -> None: ...

    def MoreArgs(self) -> bool: ...

    def NextArg(self) -> None: ...

    def ArgIsFeature(self) -> bool: ...

    def FeatureArg(self) -> TNaming_NamedShape: ...

    def ShapeArg(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ShapeContext(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def NamedShapeOfGeneration(self) -> TNaming_NamedShape: ...

    def AncestorIdentification(self, Localizer: TNaming_Localizer, Context: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def PrimitiveIdentification(self, Localizer: TNaming_Localizer, NS: TNaming_NamedShape | None) -> None: ...

    def GeneratedIdentification(self, Localizer: TNaming_Localizer, NS: TNaming_NamedShape | None) -> None: ...

    def Identification(self, Localizer: TNaming_Localizer, NS: TNaming_NamedShape | None) -> None: ...

class TNaming_Iterator:
    """
    A tool to visit the contents of a named shape attribute.
    Pairs of shapes in the attribute are iterated, one
    being the pre-modification or the old shape, and
    the other the post-modification or the new shape.
    This allows you to have a full access to all
    contents of an attribute. If, on the other hand, you
    are only interested in topological entities stored
    in the attribute, you can use the functions
    GetShape and CurrentShape in TNaming_Tool.
    """

    @overload
    def __init__(self, anAtt: TNaming_NamedShape | None) -> None:
        """
        Iterates on all the history records in
        <anAtt>.
        """

    @overload
    def __init__(self, aLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        Iterates on all the history records in
        the current transaction
        """

    @overload
    def __init__(self, aLabel: nanoocp.TDF.TDF_Label, aTrans: int) -> None:
        """
        Iterates on all the history records in
        the transaction <aTrans>
        """

    @overload
    def __init__(self, theOther: TNaming_Iterator) -> None: ...

    def More(self) -> bool:
        """
        Returns True if there is a current Item in
        the iteration.
        """

    def Next(self) -> None:
        """Moves the iteration to the next Item"""

    def OldShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the old shape in this iterator object.
        This shape can be a null one.
        """

    def NewShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the new shape in this iterator object."""

    def IsModification(self) -> bool:
        """
        Returns true if the new shape is a modification
        (split, fuse, etc...) of the old shape.
        """

    def Evolution(self) -> TNaming_Evolution: ...

class TNaming_IteratorOnShapesSet:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: TNaming_ShapesSet) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_IteratorOnShapesSet) -> None: ...

    def __iter__(self) -> TNaming_IteratorOnShapesSet:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Python addition: see __iter__."""

    def Init(self, S: TNaming_ShapesSet) -> None:
        """Initialize the iteration"""

    def More(self) -> bool:
        """
        Returns True if there is a current Item in
        the iteration.
        """

    def Next(self) -> None:
        """Move to the next Item"""

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class TNaming_ShapesSet:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, Type: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_ShapesSet) -> None: ...

    def Clear(self) -> None:
        """Removes all Shapes"""

    @overload
    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Adds the Shape <S>"""

    @overload
    def Add(self, Shapes: TNaming_ShapesSet) -> None:
        """Adds the shapes contained in <Shapes>."""

    def Contains(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns True if <S> is in <me>"""

    @overload
    def Remove(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Removes <S> in <me>."""

    @overload
    def Remove(self, Shapes: TNaming_ShapesSet) -> None:
        """Removes in <me> the shapes contained in <Shapes>"""

    def Filter(self, Shapes: TNaming_ShapesSet) -> None:
        """
        Erases in <me> the shapes not
        contained in <Shapes>
        """

    def IsEmpty(self) -> bool: ...

    def NbShapes(self) -> int: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def Map(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

class TNaming_Localizer:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_Localizer) -> None: ...

    def Init(self, US: TNaming_UsedShapes | None, CurTrans: int) -> None: ...

    def SubShapes(self, S: nanoocp.TopoDS.TopoDS_Shape, Type: nanoocp.TopAbs.TopAbs_ShapeEnum) -> nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def Ancestors(self, S: nanoocp.TopoDS.TopoDS_Shape, Type: nanoocp.TopAbs.TopAbs_ShapeEnum) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def FindFeaturesInAncestors(self, S: nanoocp.TopoDS.TopoDS_Shape, In: nanoocp.TopoDS.TopoDS_Shape, AncInFeatures: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def GoBack(self, S: nanoocp.TopoDS.TopoDS_Shape, Lab: nanoocp.TDF.TDF_Label, Evol: TNaming_Evolution, OldS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], OldLab: nanoocp.NCollection.NCollection_List[nanoocp.TNaming.TNaming_NamedShape]) -> None: ...

    def Backward(self, NS: TNaming_NamedShape | None, S: nanoocp.TopoDS.TopoDS_Shape, Primitives: nanoocp.NCollection.NCollection_Map[nanoocp.TNaming.TNaming_NamedShape], ValidShapes: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def FindNeighbourg(self, Cont: nanoocp.TopoDS.TopoDS_Shape, S: nanoocp.TopoDS.TopoDS_Shape, Neighbourg: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def IsNew(S: nanoocp.TopoDS.TopoDS_Shape, NS: TNaming_NamedShape | None) -> bool: ...

    @staticmethod
    def FindGenerator(NS: TNaming_NamedShape | None, S: nanoocp.TopoDS.TopoDS_Shape, theListOfGenerators: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @staticmethod
    def FindShapeContext(NS: TNaming_NamedShape | None, theS: nanoocp.TopoDS.TopoDS_Shape, theSC: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Finds context of the shape <S>."""

class TNaming_Name:
    """store the arguments of Naming."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_Name) -> None: ...

    @overload
    def Type(self, aType: TNaming_NameType) -> None: ...

    @overload
    def Type(self) -> TNaming_NameType: ...

    @overload
    def ShapeType(self, aType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None: ...

    @overload
    def ShapeType(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    @overload
    def Shape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Append(self, arg: TNaming_NamedShape | None) -> None: ...

    @overload
    def StopNamedShape(self, arg: TNaming_NamedShape | None) -> None: ...

    @overload
    def StopNamedShape(self) -> TNaming_NamedShape: ...

    @overload
    def Index(self, I: int) -> None: ...

    @overload
    def Index(self) -> int: ...

    @overload
    def ContextLabel(self, theLab: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def ContextLabel(self) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def Orientation(self, theOrientation: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def Arguments(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TNaming.TNaming_NamedShape]: ...

    def Solve(self, aLab: nanoocp.TDF.TDF_Label, Valid: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> bool: ...

    def Paste(self, into: TNaming_Name, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TNaming_Naming(nanoocp.TDF.TDF_Attribute):
    """
    This attribute store the topological naming of any
    selected shape, when this shape is not already
    attached to a specific label. This class is also used
    to solve it when the arguments of the topological
    naming are modified.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_Naming) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        following code from TDesignStd
        ==============================
        """

    @staticmethod
    def Insert(under: nanoocp.TDF.TDF_Label) -> TNaming_Naming: ...

    @staticmethod
    def Name(where: nanoocp.TDF.TDF_Label, Selection: nanoocp.TopoDS.TopoDS_Shape, Context: nanoocp.TopoDS.TopoDS_Shape, Geometry: bool = False, KeepOrientation: bool = False, BNproblem: bool = False) -> TNaming_NamedShape:
        """
        instance method
        ===============
        """

    def IsDefined(self) -> bool: ...

    def GetName(self) -> TNaming_Name: ...

    def ChangeName(self) -> TNaming_Name: ...

    def Regenerate(self, scope: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> bool:
        """regenerate only the Name associated to me"""

    def Solve(self, scope: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Regenerate recursively the whole name with scope. If
        scope is empty it means that all the labels of the
        framework are valid.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """
        Deferred methods from TDF_Attribute
        ===================================
        """

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def ExtendedDump(self, aFilter: nanoocp.TDF.TDF_IDFilter, aMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TDF.TDF_Attribute]) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TNaming_NamingTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_NamingTool) -> None: ...

    @staticmethod
    def CurrentShape(Valid: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], Forbiden: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], NS: TNaming_NamedShape | None, MS: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def CurrentShapeFromShape(Valid: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], Forbiden: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], Acces: nanoocp.TDF.TDF_Label, S: nanoocp.TopoDS.TopoDS_Shape, MS: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def BuildDescendants(NS: TNaming_NamedShape | None, Labels: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None: ...

class TNaming_NewShapeIterator:
    """Iterates on all the descendants of a shape"""

    @overload
    def __init__(self, anIterator: TNaming_NewShapeIterator) -> None: ...

    @overload
    def __init__(self, anIterator: TNaming_Iterator) -> None:
        """Iterates from the current Shape in <anIterator>"""

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, access: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, Transaction: int, access: nanoocp.TDF.TDF_Label) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Label(self) -> nanoocp.TDF.TDF_Label: ...

    def NamedShape(self) -> TNaming_NamedShape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Warning! Can be a Null Shape if a descendant is deleted."""

    def IsModification(self) -> bool:
        """
        True if the new shape is a modification (split,
        fuse,etc...) of the old shape.
        """

class TNaming_OldShapeIterator:
    """Iterates on all the ascendants of a shape"""

    @overload
    def __init__(self, anIterator: TNaming_OldShapeIterator) -> None: ...

    @overload
    def __init__(self, anIterator: TNaming_Iterator) -> None:
        """Iterates from the current Shape in <anIterator>"""

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, access: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, Transaction: int, access: nanoocp.TDF.TDF_Label) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Label(self) -> nanoocp.TDF.TDF_Label: ...

    def NamedShape(self) -> TNaming_NamedShape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def IsModification(self) -> bool:
        """
        True if the new shape is a modification (split,
        fuse,etc...) of the old shape.
        """

class TNaming_RefShape:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_RefShape) -> None: ...

    @overload
    def Shape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Label(self) -> nanoocp.TDF.TDF_Label: ...

    def NamedShape(self) -> TNaming_NamedShape: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TNaming_SameShapeIterator:
    """
    To iterate on all the label which contained a
    given shape.
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, access: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_SameShapeIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Label(self) -> nanoocp.TDF.TDF_Label: ...

class TNaming_Scope:
    """
    this class manage a scope of labels
    ===================================
    """

    @overload
    def __init__(self) -> None:
        """WithValid = FALSE"""

    @overload
    def __init__(self, WithValid: bool) -> None:
        """
        if <WithValid> the scope is defined by the map. If not
        on the whole framework.
        """

    @overload
    def __init__(self, valid: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None:
        """create a scope with a map. WithValid = TRUE."""

    @overload
    def __init__(self, theOther: TNaming_Scope) -> None: ...

    @overload
    def WithValid(self) -> bool: ...

    @overload
    def WithValid(self, mode: bool) -> None: ...

    def ClearValid(self) -> None: ...

    def Valid(self, L: nanoocp.TDF.TDF_Label) -> None: ...

    def ValidChildren(self, L: nanoocp.TDF.TDF_Label, withroot: bool = True) -> None: ...

    def Unvalid(self, L: nanoocp.TDF.TDF_Label) -> None: ...

    def UnvalidChildren(self, L: nanoocp.TDF.TDF_Label, withroot: bool = True) -> None: ...

    def IsValid(self, L: nanoocp.TDF.TDF_Label) -> bool: ...

    def GetValid(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]: ...

    def ChangeValid(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]: ...

    def CurrentShape(self, NS: TNaming_NamedShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the current value of <NS> according to the
        Valid Scope.
        """

class TNaming_Selector:
    """
    This class provides a single API for selection of shapes.
    This involves both identification and selection of
    shapes in the data framework.
    If the selected shape is modified, this selector will
    solve its identifications.
    This class is the user interface for topological
    naming resources.
    * The <IsIdentified> method returns (if exists)
    the NamedShape which contains a given shape. The
    definition of an identified shape is: a Shape
    handled by a NamedShape (this shape is the only
    one stored), which has the TNaming_PRImITIVE evolution

    * The <Select> method returns ALWAYS a new
    NamedShape at the given label, which contains the
    argument selected shape. When calling this
    method, the sub-hierarchy of <label> is first cleared,
    then a TNaming_NamedShape is ALWAYS created at
    this <label>, with the TNaming_SELECTED evolution.
    The <Naming attribute> is associated to the selected
    shape which store the arguments of the selection.
    If the given selected shape was already identified
    (method IsIdentified), this Naming attribute
    contains the reference (Identity code) to the
    argument shape.

    * The <Solve> method update the current value of
    the NamedShape, according to the <Naming> attribute.
    A boolean status is returned to say if the
    algorithm succeed or not. To read the current
    value of the selected Named Shape use the
    TNaming_Tool::GetShape method, as for any
    NamedShape attribute.
    """

    @overload
    def __init__(self, aLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        Create a selector on this label
        to select a shape.
        ==================
        """

    @overload
    def __init__(self, theOther: TNaming_Selector) -> None: ...

    @staticmethod
    def IsIdentified(access: nanoocp.TDF.TDF_Label, selection: nanoocp.TopoDS.TopoDS_Shape, Geometry: bool = False) -> tuple[bool, TNaming_NamedShape]:
        """
        To know if a shape is already identified (not selected)
        =======================================================

        The label access defines the point of access to the data framework.
        selection is the shape for which we want to know
        whether it is identified or not.
        If true, NS is returned as the identity of selection.
        If Geometry is true, NS will be the named shape
        containing the first appearance of selection and
        not any other shape. In other words, selection
        must be the only shape stored in NS.
        """

    @overload
    def Select(self, Selection: nanoocp.TopoDS.TopoDS_Shape, Context: nanoocp.TopoDS.TopoDS_Shape, Geometry: bool = False, KeepOrientatation: bool = False) -> bool:
        """
        Creates a topological naming on the label
        aLabel given as an argument at construction time.
        If successful, the shape Selection - found in the
        shape Context - is now identified in the named
        shape returned in NamedShape.
        If Geometry is true, NamedShape contains the
        first appearance of Selection.
        This syntax is more robust than the previous
        syntax for this method.
        """

    @overload
    def Select(self, Selection: nanoocp.TopoDS.TopoDS_Shape, Geometry: bool = False, KeepOrientatation: bool = False) -> bool:
        """
        Creates a topological naming on the label
        aLabel given as an argument at construction time.
        If successful, the shape Selection is now
        identified in the named shape returned in NamedShape.
        If Geometry is true, NamedShape contains the
        first appearance of Selection.
        """

    def Solve(self, Valid: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Updates the topological naming on the label
        aLabel given as an argument at construction time.
        The underlying shape returned in the method
        NamedShape is updated.
        To read this shape, use the method TNaming_Tool::GetShape
        """

    def Arguments(self, args: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Attribute]) -> None:
        """
        Returns the attribute list args.
        This list contains the named shape on which the topological naming was built.
        """

    def NamedShape(self) -> TNaming_NamedShape:
        """
        Returns the NamedShape build or under construction,
        which contains the topological naming..
        """

class TNaming_Tool:
    """
    A tool to get information on the topology of a
    named shape attribute.
    This information is typically a TopoDS_Shape object.
    Using this tool, relations between named shapes
    are also accessible.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_Tool) -> None: ...

    @overload
    @staticmethod
    def CurrentShape(NS: TNaming_NamedShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the last Modification of <NS>.
        Returns the shape CurrentShape contained in
        the named shape attribute NS.
        CurrentShape is the current state of the entities
        if they have been modified in other attributes of the same data structure.
        Each call to this function creates a new compound.
        """

    @overload
    @staticmethod
    def CurrentShape(NS: TNaming_NamedShape | None, Updated: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape CurrentShape contained in
        the named shape attribute NS, and present in
        the updated attribute map Updated.
        CurrentShape is the current state of the entities
        if they have been modified in other attributes of the same data structure.
        Each call to this function creates a new compound.
        Warning
        Only the contents of Updated are searched.R
        """

    @overload
    @staticmethod
    def CurrentNamedShape(NS: TNaming_NamedShape | None, Updated: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> TNaming_NamedShape:
        """
        Returns the NamedShape of the last Modification of <NS>.
        This shape is identified by a label.
        """

    @overload
    @staticmethod
    def CurrentNamedShape(NS: TNaming_NamedShape | None) -> TNaming_NamedShape:
        """Returns NamedShape the last Modification of <NS>."""

    @staticmethod
    def NamedShape(aShape: nanoocp.TopoDS.TopoDS_Shape, anAcces: nanoocp.TDF.TDF_Label) -> TNaming_NamedShape:
        """
        Returns the named shape attribute defined by
        the shape aShape and the label anAccess.
        This attribute is returned as a new shape.
        You call this function, if you need to create a
        topological attribute for existing data.
        Example
        class MyPkg_MyClass
        {
        public: bool
        SameEdge(const
        occ::handle<OCafTest_Line>& , const
        occ::handle<CafTest_Line>& );
        };

        bool
        MyPkg_MyClass::SameEdge
        (const occ::handle<OCafTest_Line>& L1
        const occ::handle<OCafTest_Line>& L2)
        { occ::handle<TNaming_NamedShape>
        NS1 = L1->NamedShape();
        occ::handle<TNaming_NamedShape>
        NS2 = L2->NamedShape();

        return
        BRepTools::Compare(NS1->Get(),NS2->Get());
        }
        In the example above, the function SameEdge is
        created to compare the edges having two lines
        for geometric supports. If these edges are found
        by BRepTools::Compare to be within the same
        tolerance, they are considered to be the same.
        Warning
        To avoid sharing of names, a SELECTED
        attribute will not be returned. Sharing of names
        makes it harder to manage the data structure.
        When the user of the name is removed, for
        example, it is difficult to know whether the name
        should be destroyed.
        """

    @staticmethod
    def GetShape(NS: TNaming_NamedShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the entities stored in the named shape attribute NS.
        If there is only one old-new pair, the new shape
        is returned. Otherwise, a Compound is returned.
        This compound is made out of all the new shapes found.
        Each call to this function creates a new compound.
        """

    @staticmethod
    def OriginalShape(NS: TNaming_NamedShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the shape contained as OldShape in <NS>"""

    @staticmethod
    def GeneratedShape(S: nanoocp.TopoDS.TopoDS_Shape, Generation: TNaming_NamedShape | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape generated from S or by a
        modification of S and contained in the named
        shape Generation.
        """

    @staticmethod
    def Collect(NS: TNaming_NamedShape | None, Labels: nanoocp.NCollection.NCollection_Map[nanoocp.TNaming.TNaming_NamedShape], OnlyModif: bool = True) -> None: ...

    @staticmethod
    def HasLabel(access: nanoocp.TDF.TDF_Label, aShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns True if <aShape> appears under a label.(DP)"""

    @staticmethod
    def Label(access: nanoocp.TDF.TDF_Label, aShape: nanoocp.TopoDS.TopoDS_Shape) -> tuple[nanoocp.TDF.TDF_Label, int]:
        """
        Returns the label of the first apparition  of
        <aShape>. Transdef is a value of the transaction
        of the first apparition of <aShape>.
        """

    @staticmethod
    def InitialShape(aShape: nanoocp.TopoDS.TopoDS_Shape, anAcces: nanoocp.TDF.TDF_Label, Labels: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape created from the shape
        aShape contained in the attribute anAcces.
        """

    @staticmethod
    def ValidUntil(access: nanoocp.TDF.TDF_Label, S: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Returns the last transaction where the creation of S
        is valid.
        """

    @staticmethod
    def FindShape(Valid: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], Forbiden: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label], Arg: TNaming_NamedShape | None, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Returns the current shape (a Wire or a Shell) built (in the data framework)
        from the shapes of the argument named shape.
        It is used for IDENTITY name type computation.
        """

class TNaming_TranslateTool(nanoocp.Standard.Standard_Transient):
    """
    tool to copy underlying TShape of a Shape.
    The TranslateTool class is provided to support the
    translation of topological data structures Transient
    to Transient.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_TranslateTool) -> None: ...

    def Add(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeVertex(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeEdge(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeWire(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeFace(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeShell(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeSolid(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeCompSolid(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MakeCompound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def UpdateVertex(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]) -> None: ...

    def UpdateEdge(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]) -> None: ...

    def UpdateFace(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.Standard.Standard_Transient, nanoocp.Standard.Standard_Transient]) -> None: ...

    def UpdateShape(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TNaming_Translator:
    """only for Shape Copy test - to move in DNaming"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TNaming_Translator) -> None: ...

    def Add(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Perform(self) -> None: ...

    def IsDone(self) -> bool: ...

    @overload
    def Copied(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns copied shape"""

    @overload
    def Copied(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """returns DataMap of results; (shape <-> copied shape)"""

    def DumpMap(self, isWrite: bool = False) -> None: ...

class TNaming_UsedShapes(nanoocp.TDF.TDF_Attribute):
    """
    Global attribute located under root label to store all
    the shapes handled by the framework
    Set of Shapes Used in a Data from TDF
    Only one instance by Data, it always
    Stored as Attribute of The Root.
    """

    def __init__(self, theOther: TNaming_UsedShapes) -> None: ...

    def Destroy(self) -> None: ...

    def Map(self) -> "NCollection_DataMap<TopoDS_Shape, TNaming_RefShape*, TopTools_ShapeMapHasher>": ...

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the ID: 2a96b614-ec8b-11d0-bee7-080009dc3333."""

    def BackupCopy(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Copies the attribute contents into a new other
        attribute. It is used by Backup().
        """

    def Restore(self, anAttribute: nanoocp.TDF.TDF_Attribute | None) -> None:
        """
        Restores the contents from <anAttribute> into this
        one. It is used when aborting a transaction.
        """

    def BeforeRemoval(self) -> None:
        """Clears the table."""

    def AfterUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """Something to do after applying <anAttDelta>."""

    def DeltaOnAddition(self) -> nanoocp.TDF.TDF_DeltaOnAddition:
        """this method returns a null handle (no delta)."""

    def DeltaOnRemoval(self) -> nanoocp.TDF.TDF_DeltaOnRemoval:
        """this method returns a null handle (no delta)."""

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Returns an new empty attribute from the good end
        type. It is used by the copy algorithm.
        """

    def Paste(self, intoAttribute: nanoocp.TDF.TDF_Attribute | None, aRelocTationable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """
        This method is different from the "Copy" one,
        because it is used when copying an attribute from
        a source structure into a target structure. This
        method pastes the current attribute to the label
        corresponding to the insertor. The pasted
        attribute may be a brand new one or a new version
        of the previous one.
        """

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None:
        """
        Adds the directly referenced attributes and labels
        to <aDataSet>. "Directly" means we have only to
        look at the first level of references.

        For this, use only the AddLabel() & AddAttribute()
        from DataSet and do not try to modify information
        previously stored in <aDataSet>.
        """

    def Dump(self) -> str:
        """Dumps the attribute on <aStream>."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TNaming
import nanoocp.TopTools
TNaming_ListOfNamedShape = nanoocp.NCollection.NCollection_List[nanoocp.TNaming.TNaming_NamedShape]
