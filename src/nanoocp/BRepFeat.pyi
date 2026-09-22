"""OCCT package BRepFeat (toolkit TKFeat)"""

import enum
from typing import overload

import nanoocp.BOPAlgo
import nanoocp.BRepBuilderAPI
import nanoocp.Geom
import nanoocp.LocOpe
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class BRepFeat_StatusError(enum.IntEnum):
    """Describes the error."""

    BRepFeat_OK = 0

    BRepFeat_BadDirect = 1

    BRepFeat_BadIntersect = 2

    BRepFeat_EmptyBaryCurve = 3

    BRepFeat_EmptyCutResult = 4

    BRepFeat_FalseSide = 5

    BRepFeat_IncDirection = 6

    BRepFeat_IncSlidFace = 7

    BRepFeat_IncParameter = 8

    BRepFeat_IncTypes = 9

    BRepFeat_IntervalOverlap = 10

    BRepFeat_InvFirstShape = 11

    BRepFeat_InvOption = 12

    BRepFeat_InvShape = 13

    BRepFeat_LocOpeNotDone = 14

    BRepFeat_LocOpeInvNotDone = 15

    BRepFeat_NoExtFace = 16

    BRepFeat_NoFaceProf = 17

    BRepFeat_NoGluer = 18

    BRepFeat_NoIntersectF = 19

    BRepFeat_NoIntersectU = 20

    BRepFeat_NoParts = 21

    BRepFeat_NoProjPt = 22

    BRepFeat_NotInitialized = 23

    BRepFeat_NotYetImplemented = 24

    BRepFeat_NullRealTool = 25

    BRepFeat_NullToolF = 26

    BRepFeat_NullToolU = 27

BRepFeat_OK: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_OK

BRepFeat_BadDirect: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_BadDirect

BRepFeat_BadIntersect: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_BadIntersect

BRepFeat_EmptyBaryCurve: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_EmptyBaryCurve

BRepFeat_EmptyCutResult: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_EmptyCutResult

BRepFeat_FalseSide: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_FalseSide

BRepFeat_IncDirection: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_IncDirection

BRepFeat_IncSlidFace: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_IncSlidFace

BRepFeat_IncParameter: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_IncParameter

BRepFeat_IncTypes: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_IncTypes

BRepFeat_IntervalOverlap: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_IntervalOverlap

BRepFeat_InvFirstShape: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_InvFirstShape

BRepFeat_InvOption: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_InvOption

BRepFeat_InvShape: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_InvShape

BRepFeat_LocOpeNotDone: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_LocOpeNotDone

BRepFeat_LocOpeInvNotDone: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_LocOpeInvNotDone

BRepFeat_NoExtFace: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoExtFace

BRepFeat_NoFaceProf: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoFaceProf

BRepFeat_NoGluer: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoGluer

BRepFeat_NoIntersectF: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoIntersectF

BRepFeat_NoIntersectU: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoIntersectU

BRepFeat_NoParts: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoParts

BRepFeat_NoProjPt: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NoProjPt

BRepFeat_NotInitialized: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NotInitialized

BRepFeat_NotYetImplemented: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NotYetImplemented

BRepFeat_NullRealTool: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NullRealTool

BRepFeat_NullToolF: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NullToolF

BRepFeat_NullToolU: BRepFeat_StatusError = BRepFeat_StatusError.BRepFeat_NullToolU

class BRepFeat_PerfSelection(enum.IntEnum):
    """
    To declare the type of selection semantics for local operation Perform methods
    -   NoSelection
    -   SelectionFU - selection of a face up to which a
    local operation will be performed
    -   SelectionU - selection of a point up to which a
    local operation will be performed
    -   SelectionSh - selection of a shape on which a
    local operation will be performed
    -   SelectionShU - selection of a shape up to which a
    local operation will be performed.
    """

    BRepFeat_NoSelection = 0

    BRepFeat_SelectionFU = 1

    BRepFeat_SelectionU = 2

    BRepFeat_SelectionSh = 3

    BRepFeat_SelectionShU = 4

BRepFeat_NoSelection: BRepFeat_PerfSelection = BRepFeat_PerfSelection.BRepFeat_NoSelection

BRepFeat_SelectionFU: BRepFeat_PerfSelection = BRepFeat_PerfSelection.BRepFeat_SelectionFU

BRepFeat_SelectionU: BRepFeat_PerfSelection = BRepFeat_PerfSelection.BRepFeat_SelectionU

BRepFeat_SelectionSh: BRepFeat_PerfSelection = BRepFeat_PerfSelection.BRepFeat_SelectionSh

BRepFeat_SelectionShU: BRepFeat_PerfSelection = BRepFeat_PerfSelection.BRepFeat_SelectionShU

class BRepFeat_Status(enum.IntEnum):
    BRepFeat_NoError = 0

    BRepFeat_InvalidPlacement = 1

    BRepFeat_HoleTooLong = 2

BRepFeat_NoError: BRepFeat_Status = BRepFeat_Status.BRepFeat_NoError

BRepFeat_InvalidPlacement: BRepFeat_Status = BRepFeat_Status.BRepFeat_InvalidPlacement

BRepFeat_HoleTooLong: BRepFeat_Status = BRepFeat_Status.BRepFeat_HoleTooLong

class BRepFeat:
    """
    BRepFeat is necessary for the
    creation and manipulation of both form and mechanical features in a
    Boundary Representation framework. Form features can be depressions or
    protrusions and include the following types:
    -          Cylinder
    -          Draft Prism
    -          Prism
    -          Revolved feature
    -          Pipe
    Depending on whether you wish to make a depression or a protrusion,
    you can choose your operation type between the following:
    - removing matter (a Boolean cut: Fuse setting 0)
    - adding matter (Boolean fusion: Fuse setting 1)
    The semantics of form feature creation is based on the
    construction of shapes:
    -          for a certain length in a certain direction
    -          up to a limiting face
    -          from a limiting face at a height
    -          above and/or below a plane
    The shape defining the construction of a feature can be either a
    supporting edge or a concerned area of a face.
    In case of supporting edge, this contour can be attached to a face
    of the basis shape by binding. When the contour is bound to this face,
    the information that the contour will slide on the face becomes
    available to the relevant class methods. In case of the concerned
    area of a face, you could, for example, cut it out and move it at
    a different height, which will define the limiting face of a
    protrusion or depression. Topological definition with local
    operations of this sort makes calculations simpler and faster
    than a global operation. The latter would entail a second phase of
    removing unwanted matter to get the same result.
    Mechanical features include ribs - protrusions - and grooves (or
    slots) - depressions along planar (linear) surfaces or revolution surfaces.
    The semantics of mechanical features is based on giving
    thickness to a contour. This thickness can either be unilateral
    - on one side of the contour - or bilateral - on both sides. As in
    the semantics of form features, the thickness is defined by
    construction of shapes in specific contexts.
    However, in case of mechanical features, development contexts
    differ. Here they include extrusion:
    -          to a limiting face of the basis shape
    -          to or from a limiting plane
    -          to a height.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepFeat) -> None: ...

    @staticmethod
    def SampleEdges(S: nanoocp.TopoDS.TopoDS_Shape, Pt: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> None: ...

    @staticmethod
    def Barycenter(S: nanoocp.TopoDS.TopoDS_Shape, Pt: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def ParametricBarycenter(S: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom.Geom_Curve | None) -> float: ...

    @staticmethod
    def ParametricMinMax(S: nanoocp.TopoDS.TopoDS_Shape, C: nanoocp.Geom.Geom_Curve | None, Ori: bool = False) -> tuple[float, float, float, float, bool]:
        """Ori = True taking account the orientation"""

    @staticmethod
    def IsInside(F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @staticmethod
    def FaceUntil(S: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @staticmethod
    def Tool(SRef: nanoocp.TopoDS.TopoDS_Shape, Fac: nanoocp.TopoDS.TopoDS_Face, Orf: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopoDS.TopoDS_Solid: ...

    @staticmethod
    def Print(SE: BRepFeat_StatusError) -> str:
        """
        Prints the Error description of the State <St> as a String on
        the Stream <S> and returns <S>.
        """

class BRepFeat_Builder(nanoocp.BOPAlgo.BOPAlgo_BOP):
    """
    Provides a basic tool to implement features topological
    operations. The main goal of the algorithm is to perform
    the result of the operation according to the
    kept parts of the tool.
    Input data: a) DS;
    b) The kept parts of the tool;
    If the map of the kept parts of the tool
    is not filled boolean operation of the
    given type will be performed;
    c) Operation required.
    Steps: a) Fill myShapes, myRemoved maps;
    b) Rebuild edges and faces;
    c) Build images of the object;
    d) Build the result of the operation.
    Result: Result shape of the operation required.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepFeat_Builder) -> None: ...

    def Clear(self) -> None:
        """Clears internal fields and arguments."""

    @overload
    def Init(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the object of local boolean operation."""

    @overload
    def Init(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theTool: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the arguments of local boolean operation."""

    @overload
    def SetOperation(self, theFuse: int) -> None:
        """
        Sets the operation of local boolean operation.
        If theFuse = 0 than the operation is CUT, otherwise FUSE.
        """

    @overload
    def SetOperation(self, theFuse: int, theFlag: bool) -> None:
        """
        Sets the operation of local boolean operation.
        If theFlag = TRUE it means that no selection of parts
        of the tool is needed, t.e. no second part. In that case
        if theFuse = 0 than operation is COMMON, otherwise CUT21.
        If theFlag = FALSE SetOperation(theFuse) function is called.
        """

    def PartsOfTool(self, theLT: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Collects parts of the tool."""

    def KeepParts(self, theIm: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Initializes parts of the tool for second step of algorithm.
        Collects shapes and all sub-shapes into myShapes map.
        """

    def KeepPart(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds shape theS and all its sub-shapes into myShapes map."""

    def PerformResult(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Main function to build the result of the
        local operation required.
        """

    def RebuildFaces(self) -> None:
        """Rebuilds faces in accordance with the kept parts of the tool."""

    def RebuildEdge(self, theE: nanoocp.TopoDS.TopoDS_Shape, theF: nanoocp.TopoDS.TopoDS_Face, theME: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aLEIm: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Rebuilds edges in accordance with the kept parts of the tool."""

    def CheckSolidImages(self) -> None:
        """
        Collects the images of the object, that contains in
        the images of the tool.
        """

    @overload
    def FillRemoved(self) -> None:
        """Collects the removed parts of the tool into myRemoved map."""

    @overload
    def FillRemoved(self, theS: nanoocp.TopoDS.TopoDS_Shape, theM: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Adds the shape S and its sub-shapes into myRemoved map."""

class BRepFeat_Form(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Provides general functions to build form features.
    Form features can be depressions or protrusions and include the following types:
    -          Cylinder
    -          Draft Prism
    -          Prism
    -          Revolved feature
    -          Pipe
    In each case, you have a choice of operation type between the following:
    -          removing matter (a Boolean cut: Fuse setting 0)
    -          adding matter (Boolean fusion: Fuse setting 1)
    The semantics of form feature creation is based on the construction of shapes:
    -      along a length
    -      up to a limiting face
    -      from a limiting face to a height
    -      above and/or below a plane
    The shape defining construction of the feature can be either the
    supporting edge or the concerned area of a face.
    In case of the supporting edge, this contour can be attached to a
    face of the basis shape by binding. When the contour is bound to this
    face, the information that the contour will slide on the face
    becomes available to the relevant class methods. In case of the
    concerned area of a face, you could, for example, cut it out and
    move it to a different height which will define the limiting face of a
    protrusion or depression.
    Topological definition with local operations of this sort makes
    calculations simpler and faster than a global operation. The latter
    would entail a second phase of removing unwanted matter to get the same result.
    """

    def Modified(self, F: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """returns the list of generated Faces."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        returns a list of the created faces
        from the shape <S>.
        """

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def FirstShape(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes created at the bottom of
        the created form. It may be an empty list.
        """

    def LastShape(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes created at the top of the
        created form. It may be an empty list.
        """

    def NewEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of the limiting and glueing edges
        generated by the feature. These edges did not originally
        exist in the basis shape.
        The list provides the information necessary for
        subsequent addition of fillets. It may be an empty list.
        """

    def TgtEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of the tangent edges among the limiting
        and glueing edges generated by the feature. These
        edges did not originally exist in the basis shape and are
        tangent to the face against which the feature is built.
        The list provides the information necessary for
        subsequent addition of fillets. It may be an empty list.
        If an edge is tangent, no fillet is possible, and the edge
        must subsequently be removed if you want to add a fillet.
        """

    def BasisShapeValid(self) -> None:
        """
        Initializes the topological construction if the basis shape is present.
        """

    def GeneratedShapeValid(self) -> None:
        """
        Initializes the topological construction if the generated shape S is present.
        """

    def ShapeFromValid(self) -> None:
        """
        Initializes the topological construction if the shape is
        present from the specified integer on.
        """

    def ShapeUntilValid(self) -> None:
        """
        Initializes the topological construction if the shape is
        present until the specified integer.
        """

    def GluedFacesValid(self) -> None:
        """Initializes the topological construction if the glued face is present."""

    def SketchFaceValid(self) -> None:
        """
        Initializes the topological construction if the sketch face
        is present. If the sketch face is inside the basis shape,
        local operations such as glueing can be performed.
        """

    def PerfSelectionValid(self) -> None:
        """
        Initializes the topological construction if the selected face is present.
        """

    def Curves(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

    def CurrentStatusError(self) -> BRepFeat_StatusError: ...

class BRepFeat_Gluer(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    One of the most significant aspects
    of BRepFeat functionality is the use of local operations as opposed
    to global ones. In a global operation, you would first
    construct a form of the type you wanted in your final feature, and
    then remove matter so that it could fit into your initial basis object.
    In a local operation, however, you specify the domain of the feature
    construction with aspects of the shape on which the feature is being
    created. These semantics are expressed in terms of a member
    shape of the basis shape from which - or up to which - matter will be
    added or removed. As a result, local operations make calculations
    simpler and faster than global operations.
    Glueing uses wires or edges of a face in the basis shape. These are
    to become a part of the feature. They are first cut out and then
    projected to a plane outside or inside the basis shape. By
    rebuilding the initial shape incorporating the edges and the
    faces of the tool, protrusion features can be constructed.
    """

    @overload
    def __init__(self) -> None:
        """Initializes an empty constructor"""

    @overload
    def __init__(self, Snew: nanoocp.TopoDS.TopoDS_Shape, Sbase: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initializes the shapes to be glued, the new shape
        Snew and the basis shape Sbase.
        """

    @overload
    def __init__(self, theOther: BRepFeat_Gluer) -> None: ...

    def Init(self, Snew: nanoocp.TopoDS.TopoDS_Shape, Sbase: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initializes the new shape Snew and the basis shape
        Sbase for the local glueing operation.
        """

    @overload
    def Bind(self, Fnew: nanoocp.TopoDS.TopoDS_Face, Fbase: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Defines a contact between Fnew on the new shape
        Snew and Fbase on the basis shape Sbase. Informs
        other methods that Fnew in the new shape Snew is
        connected to the face Fbase in the basis shape Sbase.
        The contact faces of the glued shape must not have
        parts outside the contact faces of the basis shape.
        This indicates that glueing is possible.
        """

    @overload
    def Bind(self, Enew: nanoocp.TopoDS.TopoDS_Edge, Ebase: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        nforms other methods that the edge Enew in the new
        shape is the same as the edge Ebase in the basis
        shape and is therefore attached to the basis shape. This
        indicates that glueing is possible.
        """

    def OpeType(self) -> nanoocp.LocOpe.LocOpe_Operation:
        """Determine which operation type to use glueing or sliding."""

    def BasisShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the basis shape of the compound shape."""

    def GluedShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the resulting compound shape."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        This is called by Shape(). It does nothing but
        may be redefined.
        """

    def IsDeleted(self, F: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns the status of the Face after
        the shape creation.
        """

    def Modified(self, F: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of generated Faces."""

class BRepFeat_MakeCylindricalHole(BRepFeat_Builder):
    """Provides a tool to make cylindrical holes on a shape."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: BRepFeat_MakeCylindricalHole) -> None: ...

    @overload
    def Init(self, Axis: nanoocp.gp.gp_Ax1) -> None:
        """Sets the axis of the hole(s)."""

    @overload
    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, Axis: nanoocp.gp.gp_Ax1) -> None:
        """
        Sets the shape and axis on which hole(s) will be
        performed.
        """

    @overload
    def Perform(self, Radius: float) -> None:
        """
        Performs every hole of radius <Radius>. This
        command has the same effect as a cut operation
        with an infinite cylinder defined by the given
        axis and <Radius>.
        """

    @overload
    def Perform(self, Radius: float, PFrom: float, PTo: float, WithControl: bool = True) -> None:
        """
        Performs every hole of radius <Radius> located
        between PFrom and PTo on the given axis. If
        <WithControl> is set to false no control
        are done on the resulting shape after the
        operation is performed.
        """

    def PerformThruNext(self, Radius: float, WithControl: bool = True) -> None:
        """
        Performs the first hole of radius <Radius>, in the
        direction of the defined axis. First hole signify
        first encountered after the origin of the axis. If
        <WithControl> is set to false no control
        are done on the resulting shape after the
        operation is performed.
        """

    def PerformUntilEnd(self, Radius: float, WithControl: bool = True) -> None:
        """
        Performs every hole of radius <Radius> located
        after the origin of the given axis. If
        <WithControl> is set to false no control
        are done on the resulting shape after the
        operation is performed.
        """

    def PerformBlind(self, Radius: float, Length: float, WithControl: bool = True) -> None:
        """
        Performs a blind hole of radius <Radius> and
        length <Length>. The length is measured from the
        origin of the given axis. If <WithControl> is set
        to false no control are done after the
        operation is performed.
        """

    def Status(self) -> BRepFeat_Status:
        """Returns the status after a hole is performed."""

    def Build(self) -> None:
        """
        Builds the resulting shape (redefined from
        MakeShape). Invalidates the given parts of tools
        if any, and performs the result of the local
        operation.
        """

class BRepFeat_MakeDPrism(BRepFeat_Form):
    """
    Describes functions to build draft
    prism topologies from basis shape surfaces. These can be depressions or protrusions.
    The semantics of draft prism feature creation is based on the
    construction of shapes:
    -          along a length
    -          up to a limiting face
    -          from a limiting face to a height.
    The shape defining construction of the draft prism feature can be
    either the supporting edge or the concerned area of a face.
    In case of the supporting edge, this contour can be attached to a
    face of the basis shape by binding. When the contour is bound to this
    face, the information that the contour will slide on the face
    becomes available to the relevant class methods.
    In case of the concerned area of a face, you could, for example, cut
    it out and move it to a different height which will define the
    limiting face of a protrusion or depression.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Face, Skface: nanoocp.TopoDS.TopoDS_Face, Angle: float, Fuse: int, Modify: bool) -> None:
        """
        A face Pbase is selected in the shape
        Sbase to serve as the basis for the draft prism. The
        draft will be defined by the angle Angle and Fuse offers a choice between:
        - removing matter with a Boolean cut using the setting 0
        - adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine the type of
        operation. If it is inside the basis shape, a local
        operation such as glueing can be performed.
        Initializes the draft prism class
        """

    @overload
    def __init__(self, theOther: BRepFeat_MakeDPrism) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Face, Skface: nanoocp.TopoDS.TopoDS_Face, Angle: float, Fuse: int, Modify: bool) -> None:
        """
        Initializes this algorithm for building draft prisms along surfaces.
        A face Pbase is selected in the basis shape Sbase to
        serve as the basis from the draft prism. The draft will be
        defined by the angle Angle and Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine the type of
        operation. If it is inside the basis shape, a local
        operation such as glueing can be performed.
        """

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, OnFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Indicates that the edge <E> will slide on the face
        <OnFace>.
        Raises ConstructionError if the face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    @overload
    def Perform(self, Height: float) -> None: ...

    @overload
    def Perform(self, Until: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Perform(self, From: nanoocp.TopoDS.TopoDS_Shape, Until: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Assigns one of the following semantics
        -   to a height Height
        -   to a face Until
        -   from a face From to a height Until.
        Reconstructs the feature topologically according to the semantic option chosen.
        """

    def PerformUntilEnd(self) -> None:
        """
        Realizes a semi-infinite prism, limited by the position of the prism base.
        """

    def PerformFromEnd(self, FUntil: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Realizes a semi-infinite prism, limited by the face Funtil."""

    def PerformThruAll(self) -> None:
        """
        Builds an infinite prism. The infinite descendants will not be kept in the result.
        """

    def PerformUntilHeight(self, Until: nanoocp.TopoDS.TopoDS_Shape, Height: float) -> None:
        """
        Assigns both a limiting shape, Until from
        TopoDS_Shape, and a height, Height at which to stop
        generation of the prism feature.
        """

    def Curves(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

    def BossEdges(self, sig: int) -> None:
        """
        Determination of TopEdges and LatEdges.
        sig = 1 -> TopEdges = FirstShape of the DPrism
        sig = 2 -> TOpEdges = LastShape of the DPrism
        """

    def TopEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of TopoDS Edges of the top of the boss."""

    def LatEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of TopoDS Edges of the bottom of the boss."""

class BRepFeat_RibSlot(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Provides functions to build mechanical features.
    Mechanical features include ribs - protrusions and grooves (or slots) - depressions along
    planar (linear) surfaces or revolution surfaces. The semantics of mechanical features is built
    around giving thickness to a contour. This thickness can either be unilateral - on one side
    of the contour - or bilateral - on both sides.
    As in the semantics of form features, the thickness is defined by construction of shapes
    in specific contexts. The development contexts differ, however,in case of mechanical features.
    Here they include extrusion:
    -   to a limiting face of the basis shape
    -   to or from a limiting plane
    -   to a height.
    """

    def __init__(self, theOther: BRepFeat_RibSlot) -> None: ...

    def IsDeleted(self, F: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if F a TopoDS_Shape of type edge or face has been deleted.
        """

    def Modified(self, F: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of generated Faces F. This list may be empty."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list NCollection_List<TopoDS_Shape> of the faces S created in the shape.
        """

    def FirstShape(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes created at the bottom of
        the created form. It may be an empty list.
        """

    def LastShape(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes created at the top of the
        created form. It may be an empty list.
        """

    def FacesForDraft(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of the limiting and glueing faces
        generated by the feature. These faces did not originally exist in the basis shape.
        The list provides the information necessary for
        subsequent addition of a draft to a face. It may be an empty list.
        If a face has tangent edges, no draft is possible, and the tangent edges must
        subsequently be removed if you want to add a draft to the face.
        """

    def NewEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of the limiting and glueing edges
        generated by the feature. These edges did not originally exist in the basis shape.
        The list provides the information necessary for
        subsequent addition of fillets. It may be an empty list.
        """

    def TgtEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of the tangent edges among the
        limiting and glueing edges generated by the
        feature. These edges did not originally exist in
        the basis shape and are tangent to the face
        against which the feature is built.
        The list provides the information necessary for
        subsequent addition of fillets. It may be an empty list.
        If an edge is tangent, no fillet is possible, and
        the edge must subsequently be removed if you want to add a fillet.
        """

    @staticmethod
    def IntPar(C: nanoocp.Geom.Geom_Curve | None, P: nanoocp.gp.gp_Pnt) -> float: ...

    @staticmethod
    def ChoiceOfFaces(faces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], cc: nanoocp.Geom.Geom_Curve | None, par: float, bnd: float, Pln: nanoocp.Geom.Geom_Plane | None) -> nanoocp.TopoDS.TopoDS_Face: ...

    def CurrentStatusError(self) -> BRepFeat_StatusError: ...

class BRepFeat_MakeLinearForm(BRepFeat_RibSlot):
    """
    Builds a rib or a groove along a developable, planar surface.
    The semantics of mechanical features is built around
    giving thickness to a contour. This thickness can either
    be symmetrical - on one side of the contour - or
    dissymmetrical - on both sides. As in the semantics of
    form features, the thickness is defined by construction of
    shapes in specific contexts.
    The development contexts differ, however, in case of
    mechanical features. Here they include extrusion:
    -   to a limiting face of the basis shape
    -   to or from a limiting plane
    -   to a height.
    """

    @overload
    def __init__(self) -> None:
        """initializes the linear form class"""

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, W: nanoocp.TopoDS.TopoDS_Wire, P: nanoocp.Geom.Geom_Plane | None, Direction: nanoocp.gp.gp_Vec, Direction1: nanoocp.gp.gp_Vec, Fuse: int, Modify: bool) -> None:
        """
        contour W, a shape Sbase and a
        plane P are initialized to serve as the basic
        elements in the construction of the rib or groove.
        Direction and Direction1 give The vectors for
        defining the direction(s) in which thickness will be built up.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the
        setting 0 in case of the groove
        -   adding matter with Boolean fusion using the
        setting 1 in case of the rib.
        """

    @overload
    def __init__(self, theOther: BRepFeat_MakeLinearForm) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, W: nanoocp.TopoDS.TopoDS_Wire, P: nanoocp.Geom.Geom_Plane | None, Direction: nanoocp.gp.gp_Vec, Direction1: nanoocp.gp.gp_Vec, Fuse: int, Modify: bool) -> None:
        """
        Initializes this construction algorithm.
        A contour W, a shape Sbase and a plane P are
        initialized to serve as the basic elements in the
        construction of the rib or groove. The vectors for
        defining the direction(s) in which thickness will be built
        up are given by Direction and Direction1.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting
        0 in case of the groove
        -   adding matter with Boolean fusion using the setting 1
        in case of the rib.
        """

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, OnFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Indicates that the edge <E> will slide on the face
        <OnFace>.
        Raises ConstructionError if the face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    def Perform(self) -> None:
        """
        Performs a prism from the wire to the plane along the
        basis shape Sbase. Reconstructs the feature topologically.
        """

    def Propagate(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], F: nanoocp.TopoDS.TopoDS_Face, FPoint: nanoocp.gp.gp_Pnt, LPoint: nanoocp.gp.gp_Pnt) -> tuple[bool, bool]: ...

class BRepFeat_MakePipe(BRepFeat_Form):
    """
    Constructs compound shapes with pipe
    features. These can be depressions or protrusions.
    The semantics of pipe feature creation is based on the construction of shapes:
    -   along a length
    -   up to a limiting face
    -   from a limiting face to a height.
    The shape defining construction of the pipe feature can be either the supporting edge or
    the concerned area of a face.
    In case of the supporting edge, this contour
    can be attached to a face of the basis shape
    by binding. When the contour is bound to this
    face, the information that the contour will
    slide on the face becomes available to the relevant class methods.
    In case of the concerned area of a face, you
    could, for example, cut it out and move it to a
    different height which will define the limiting
    face of a protrusion or depression.
    """

    @overload
    def __init__(self) -> None:
        """initializes the pipe class."""

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Shape, Skface: nanoocp.TopoDS.TopoDS_Face, Spine: nanoocp.TopoDS.TopoDS_Wire, Fuse: int, Modify: bool) -> None:
        """
        A face Pbase is selected in the
        shape Sbase to serve as the basis for the
        pipe. It will be defined by the wire Spine.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
        """

    @overload
    def __init__(self, theOther: BRepFeat_MakePipe) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Shape, Skface: nanoocp.TopoDS.TopoDS_Face, Spine: nanoocp.TopoDS.TopoDS_Wire, Fuse: int, Modify: bool) -> None:
        """
        Initializes this algorithm for adding pipes to shapes.
        A face Pbase is selected in the shape Sbase to
        serve as the basis for the pipe. It will be defined by the wire Spine.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
        """

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, OnFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Indicates that the edge <E> will slide on the face
        <OnFace>. Raises ConstructionError if the face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    @overload
    def Perform(self) -> None: ...

    @overload
    def Perform(self, Until: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Perform(self, From: nanoocp.TopoDS.TopoDS_Shape, Until: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Assigns one of the following semantics
        -   to a face Until
        -   from a face From to a height Until.
        Reconstructs the feature topologically according to the semantic option chosen.
        """

    def Curves(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

class BRepFeat_MakePrism(BRepFeat_Form):
    """
    Describes functions to build prism features.
    These can be depressions or protrusions.
    The semantics of prism feature creation is
    based on the construction of shapes:
    -   along a length
    -   up to a limiting face
    -   from a limiting face to a height.
    The shape defining construction of the prism feature can be
    either the supporting edge or the concerned area of a face.
    In case of the supporting edge, this contour
    can be attached to a face of the basis shape by
    binding. When the contour is bound to this face,
    the information that the contour will slide on the
    face becomes available to the relevant class methods.
    In case of the concerned area of a face, you
    could, for example, cut it out and move it to a
    different height which will define the limiting
    face of a protrusion or depression.
    """

    @overload
    def __init__(self) -> None:
        """
        Builds a prism by projecting a
        wire along the face of a shape. Initializes the prism class.
        """

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Shape, Skface: nanoocp.TopoDS.TopoDS_Face, Direction: nanoocp.gp.gp_Dir, Fuse: int, Modify: bool) -> None:
        """
        Builds a prism by projecting a
        wire along the face of a shape. a face Pbase is selected in
        the shape Sbase to serve as the basis for
        the prism. The orientation of the prism will
        be defined by the vector Direction.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
        Exceptions
        Standard_ConstructionError if the face
        does not belong to the basis or the prism shape.
        """

    @overload
    def __init__(self, theOther: BRepFeat_MakePrism) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Shape, Skface: nanoocp.TopoDS.TopoDS_Face, Direction: nanoocp.gp.gp_Dir, Fuse: int, Modify: bool) -> None:
        """
        Initializes this algorithm for building prisms along surfaces.
        A face Pbase is selected in the shape Sbase
        to serve as the basis for the prism. The
        orientation of the prism will be defined by the vector Direction.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
        """

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, OnFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Indicates that the edge <E> will slide on the face
        <OnFace>. Raises ConstructionError if the face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    @overload
    def Perform(self, Length: float) -> None: ...

    @overload
    def Perform(self, Until: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Perform(self, From: nanoocp.TopoDS.TopoDS_Shape, Until: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Assigns one of the following semantics
        -   to a height Length
        -   to a face Until
        -   from a face From to a height Until.
        Reconstructs the feature topologically according to the semantic option chosen.
        """

    def PerformUntilEnd(self) -> None:
        """
        Realizes a semi-infinite prism, limited by the
        position of the prism base. All other faces extend infinitely.
        """

    def PerformFromEnd(self, FUntil: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Realizes a semi-infinite prism, limited by the face Funtil."""

    def PerformThruAll(self) -> None:
        """
        Builds an infinite prism. The infinite descendants will not be kept in the result.
        """

    def PerformUntilHeight(self, Until: nanoocp.TopoDS.TopoDS_Shape, Length: float) -> None:
        """
        Assigns both a limiting shape, Until from
        TopoDS_Shape, and a height, Length at which to stop generation of the prism feature.
        """

    def Curves(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None:
        """Returns the list of curves S parallel to the axis of the prism."""

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve:
        """Generates a curve along the center of mass of the primitive."""

class BRepFeat_MakeRevol(BRepFeat_Form):
    """Describes functions to build revolved shells from basis shapes."""

    @overload
    def __init__(self) -> None:
        """initializes the revolved shell class."""

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Shape, Skface: nanoocp.TopoDS.TopoDS_Face, Axis: nanoocp.gp.gp_Ax1, Fuse: int, Modify: bool) -> None:
        """
        a face Pbase is selected in the
        shape Sbase to serve as the basis for the
        revolved shell. The revolution will be defined
        by the axis Axis and Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0
        -   adding matter with Boolean fusion using the setting 1.
        The sketch face Skface serves to determine
        the type of operation. If it is inside the basis
        shape, a local operation such as glueing can be performed.
        """

    @overload
    def __init__(self, theOther: BRepFeat_MakeRevol) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Pbase: nanoocp.TopoDS.TopoDS_Shape, Skface: nanoocp.TopoDS.TopoDS_Face, Axis: nanoocp.gp.gp_Ax1, Fuse: int, Modify: bool) -> None: ...

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, OnFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Indicates that the edge <E> will slide on the face
        <OnFace>. Raises ConstructionError if the face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    @overload
    def Perform(self, Angle: float) -> None: ...

    @overload
    def Perform(self, Until: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Perform(self, From: nanoocp.TopoDS.TopoDS_Shape, Until: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Reconstructs the feature topologically."""

    def PerformThruAll(self) -> None:
        """
        Builds an infinite shell. The infinite descendants
        will not be kept in the result.
        """

    def PerformUntilAngle(self, Until: nanoocp.TopoDS.TopoDS_Shape, Angle: float) -> None:
        """
        Assigns both a limiting shape, Until from
        TopoDS_Shape, and an angle, Angle at
        which to stop generation of the revolved shell feature.
        """

    def Curves(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

class BRepFeat_MakeRevolutionForm(BRepFeat_RibSlot):
    """
    MakeRevolutionForm Generates a surface of
    revolution in the feature as it slides along a
    revolved face in the basis shape.
    The semantics of mechanical features is built
    around giving thickness to a contour. This
    thickness can either be unilateral - on one side
    of the contour - or bilateral - on both sides. As
    in the semantics of form features, the thickness
    is defined by construction of shapes in specific contexts.
    The development contexts differ, however,in
    case of mechanical features. Here they include extrusion:
    -   to a limiting face of the basis shape
    -   to or from a limiting plane
    -   to a height.
    """

    @overload
    def __init__(self) -> None:
        """initializes the linear form class."""

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, W: nanoocp.TopoDS.TopoDS_Wire, Plane: nanoocp.Geom.Geom_Plane | None, Axis: nanoocp.gp.gp_Ax1, Height1: float, Height2: float, Fuse: int, Sliding: bool) -> None:
        """
        a contour W, a shape Sbase and a plane P are initialized to serve as
        the basic elements in the construction of the rib or groove. The axis Axis of the
        revolved surface in the basis shape defines the feature's axis of revolution.
        Height1 and Height2 may be used as limits to the construction of the feature.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0 in case of the groove
        -   adding matter with Boolean fusion using the setting 1 in case of the rib.
        """

    @overload
    def __init__(self, theOther: BRepFeat_MakeRevolutionForm) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, W: nanoocp.TopoDS.TopoDS_Wire, Plane: nanoocp.Geom.Geom_Plane | None, Axis: nanoocp.gp.gp_Ax1, Height1: float, Height2: float, Fuse: int) -> bool:
        """
        Initializes this construction algorithm
        A contour W, a shape Sbase and a plane P are initialized to serve as the basic elements
        in the construction of the rib or groove. The axis Axis of the revolved surface in the basis
        shape defines the feature's axis of revolution. Height1 and Height2 may be
        used as limits to the construction of the feature.
        Fuse offers a choice between:
        -   removing matter with a Boolean cut using the setting 0 in case of the groove
        -   adding matter with Boolean fusion using the setting 1 in case of the rib.
        """

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, OnFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Indicates that the edge <E> will slide on the face
        <OnFace>. Raises ConstructionError if the face does not belong to the
        basis shape, or the edge to the prismed shape.
        """

    def Perform(self) -> None:
        """
        Performs a prism from the wire to the plane
        along the basis shape S. Reconstructs the feature topologically.
        """

    def Propagate(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], F: nanoocp.TopoDS.TopoDS_Face, FPoint: nanoocp.gp.gp_Pnt, LPoint: nanoocp.gp.gp_Pnt) -> tuple[bool, bool]: ...

class BRepFeat_SplitShape(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    One of the most significant aspects of BRepFeat functionality is the use of local
    operations as opposed to global ones. In a global operation, you would first construct a
    form of the type you wanted in your final feature, and then remove matter so that it could
    fit into your initial basis object. In a local operation, however, you specify the domain of
    the feature construction with aspects of the shape on which the feature is being created.
    These semantics are expressed in terms of a member shape of the basis shape from which -
    or up to which - matter will be added or removed. As a result, local operations make
    calculations simpler and faster than global operations.
    In BRepFeat, the semantics of local operations define features constructed from a contour or a
    part of the basis shape referred to as the tool. In a SplitShape object, wires or edges of a
    face in the basis shape to be used as a part of the feature are cut out and projected to a plane
    outside or inside the basis shape. By rebuilding the initial shape incorporating the edges and
    the faces of the tool, protrusion or depression features can be constructed.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates the process with the shape <S>."""

    @overload
    def __init__(self, theOther: BRepFeat_SplitShape) -> None: ...

    @overload
    def Add(self, theEdges: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Add splitting edges or wires for whole initial shape
        without additional specification edge->face, edge->edge
        This method puts edge on the corresponding faces from initial shape
        """

    @overload
    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Adds the wire <W> on the face <F>.
        Raises NoSuchObject if <F> does not belong to the original shape.
        """

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Adds the edge <E> on the face <F>."""

    @overload
    def Add(self, Comp: nanoocp.TopoDS.TopoDS_Compound, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Adds the compound <Comp> on the face <F>. The
        compound <Comp> must consist of edges lying on the
        face <F>. If edges are geometrically connected,
        they must be connected topologically, i.e. they
        must share common vertices.

        Raises NoSuchObject if <F> does not belong to the original shape.
        """

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge, EOn: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Adds the edge <E> on the existing edge <EOn>."""

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the process on the shape <S>."""

    def SetCheckInterior(self, ToCheckInterior: bool) -> None:
        """
        Set the flag of check internal intersections
        default value is True (to check)
        """

    def DirectLeft(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the faces which are the left of the
        projected wires.
        """

    def Left(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the faces of the "left" part on the shape.
        (It is build from DirectLeft, with the faces
        connected to this set, and so on...).
        Raises NotDone if IsDone returns <false>.
        """

    def Right(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the faces of the "right" part on the shape."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the cut and the resulting faces and edges as well."""

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the shape has been deleted."""

    def Modified(self, F: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of generated Faces."""
