"""OCCT package BRepAlgo (toolkit TKBool)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.TopTools


class BRepAlgo:
    """
    The BRepAlgo class provides the following tools for:
    - Checking validity of the shape;
    - Concatenation of the edges of the wire.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepAlgo) -> None: ...

    @staticmethod
    def ConcatenateWire(Wire: nanoocp.TopoDS.TopoDS_Wire, Option: nanoocp.GeomAbs.GeomAbs_Shape, AngularTolerance: float = 0.0001) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        this method makes a wire whose edges are C1 from
        a Wire whose edges could be G1. It removes a vertex
        between G1 edges.
        Option can be G1 or C1.
        """

    @staticmethod
    def ConcatenateWireC0(Wire: nanoocp.TopoDS.TopoDS_Wire) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        this method makes an edge from a wire.
        Junction points between edges of wire may be sharp,
        resulting curve of the resulting edge may be C0.
        """

    @staticmethod
    def ConvertWire(theWire: nanoocp.TopoDS.TopoDS_Wire, theAngleTolerance: float, theFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Method of wire conversion, calls BRepAlgo_Approx internally.
        @param theWire
        Input Wire object.
        @param theAngleTolerance
        Angle (in radians) defining the continuity of the wire: if two vectors
        differ by less than this angle, the result will be smooth (zero angle of
        tangent lines between curve elements).
        @return
        The new TopoDS_Wire object consisting of edges each representing an arc
        of circle or a linear segment. The accuracy of conversion is defined
        as the maximal tolerance of edges in theWire.
        """

    @staticmethod
    def ConvertFace(theFace: nanoocp.TopoDS.TopoDS_Face, theAngleTolerance: float) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Method of face conversion. The API corresponds to the method ConvertWire.
        This is a shortcut for calling ConvertWire() for each wire in theFace.
        """

    @overload
    @staticmethod
    def IsValid(S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Checks if the shape is "correct". If not, returns
        <false>, else returns <true>.
        """

    @overload
    @staticmethod
    def IsValid(theArgs: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theResult: nanoocp.TopoDS.TopoDS_Shape, closedSolid: bool = False, GeomCtrl: bool = True) -> bool:
        """
        Checks if the Generated and Modified Faces from
        the shapes <arguments> in the shape <result> are
        "correct". The args may be empty, then all faces
        will be checked.
        If <Closed> is True, only closed shape are valid.
        If <GeomCtrl> is False the geometry of new
        vertices and edges are not verified and the
        auto-intersection of new wires are not searched.
        """

    @staticmethod
    def IsTopologicallyValid(S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Checks if the shape is "correct".
        If not, returns FALSE, else returns TRUE.
        This method differs from the previous one in the fact that no geometric controls
        (intersection of wires, pcurve validity) are performed.
        """

class BRepAlgo_AsDes(nanoocp.Standard.Standard_Transient):
    """SD to store descendants and ascendants of Shapes."""

    @overload
    def __init__(self) -> None:
        """Creates an empty AsDes."""

    @overload
    def __init__(self, theOther: BRepAlgo_AsDes) -> None: ...

    def Clear(self) -> None: ...

    @overload
    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape, SS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Stores <SS> as a futur subshape of <S>."""

    @overload
    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape, SS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Stores <SS> as futurs SubShapes of <S>."""

    def HasAscendant(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def HasDescendant(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def Ascendant(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the Shape containing <S>."""

    def Descendant(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns futur subhapes of <S>."""

    def ChangeDescendant(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns futur subhapes of <S>."""

    def Replace(self, theOldS: nanoocp.TopoDS.TopoDS_Shape, theNewS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Replace theOldS by theNewS.
        theOldS disappear from this.
        """

    def Remove(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Remove theS from me."""

    def HasCommonDescendant(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, LC: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Returns True if (S1> and <S2> has common
        Descendants. Stores in <LC> the Commons Descendants.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepAlgo_FaceRestrictor:
    """
    Builds all the faces limited with a set of non
    jointing and planars wires.
    if <ControlOrientation> is false The Wires must have
    correct orientations. Sinon orientation des wires
    de telle sorte que les faces ne soient pas infinies
    et qu'elles soient disjointes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepAlgo_FaceRestrictor) -> None: ...

    def __iter__(self) -> BRepAlgo_FaceRestrictor:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Python addition: see __iter__."""

    def Init(self, F: nanoocp.TopoDS.TopoDS_Face, Proj: bool = False, ControlOrientation: bool = False) -> None:
        """
        the surface of <F> will be the surface of each new
        faces built.
        <Proj> is used to update pcurves on edges if necessary.
        See Add().
        """

    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Add the wire <W> to the set of wires.

        Warning:
        The Wires must be closed.

        The edges of <W> can be modified if they don't have
        pcurves on the surface <S> of <F>. In this case
        if <Proj> is false the first pcurve of the edge
        is positioned on <S>.
        if <Proj> is True, the Pcurve On <S> is the
        projection of the curve 3d on <F>.
        """

    def Clear(self) -> None:
        """Removes all the Wires"""

    def Perform(self) -> None:
        """Evaluate all the faces limited by the set of Wires."""

    def IsDone(self) -> bool: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> nanoocp.TopoDS.TopoDS_Face: ...

class BRepAlgo_Image:
    """
    Stores link between a shape <S> and a shape <NewS>
    obtained from <S>. <NewS> is an image of <S>.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepAlgo_Image) -> None: ...

    def SetRoot(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Bind(self, OldS: nanoocp.TopoDS.TopoDS_Shape, NewS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Bind(self, OldS: nanoocp.TopoDS.TopoDS_Shape, NewS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Links <NewS> as image of <OldS>."""

    @overload
    def Add(self, OldS: nanoocp.TopoDS.TopoDS_Shape, NewS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Add(self, OldS: nanoocp.TopoDS.TopoDS_Shape, NewS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Add <NewS> to the image of <OldS>."""

    def Clear(self) -> None: ...

    def Remove(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Remove <S> to set of images."""

    def RemoveRoot(self, Root: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Removes the root <theRoot> from the list of roots and up and down maps.
        """

    def ReplaceRoot(self, OldRoot: nanoocp.TopoDS.TopoDS_Shape, NewRoot: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Replaces the <OldRoot> with the <NewRoot>, so all images
        of the <OldRoot> become the images of the <NewRoot>.
        The <OldRoot> is removed.
        """

    def Roots(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def IsImage(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def ImageFrom(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the generator of <S>"""

    def Root(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the upper generator of <S>"""

    def HasImage(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def Image(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the Image of <S>.
        Returns <S> in the list if HasImage(S) is false.
        """

    def LastImage(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Stores in <L> the images of images of...images of <S>.
        <L> contains only <S> if HasImage(S) is false.
        """

    def Compact(self) -> None:
        """Keeps only the link between roots and lastimage."""

    def Filter(self, S: nanoocp.TopoDS.TopoDS_Shape, ShapeType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        Deletes in the images the shape of type <ShapeType>
        which are not in <S>.
        Warning: Compact() must be call before.
        """

class BRepAlgo_Loop:
    """Builds the loops from a set of edges on a face."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepAlgo_Loop) -> None: ...

    def Init(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Init with <F> the set of edges must have
        pcurves on <F>.
        """

    def AddEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, LV: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Add E with <LV>. <E> will be copied and trim
        by vertices in <LV>.
        """

    def AddConstEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Add <E> as const edge, E can be in the result."""

    def AddConstEdges(self, LE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Add <LE> as a set of const edges."""

    def SetImageVV(self, theImageVV: BRepAlgo_Image) -> None:
        """Sets the Image Vertex - Vertex"""

    def Perform(self) -> None:
        """Make loops."""

    def UpdateVEmap(self, theVEmap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Update VE map according to Image Vertex - Vertex"""

    def CutEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, VonE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], NE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Cut the edge <E> in several edges <NE> on the
        vertices<VonE>.
        """

    def NewWires(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of wires performed.
        can be an empty list.
        """

    def WiresToFaces(self) -> None:
        """Build faces from the wires result."""

    def NewFaces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of faces.
        Warning: The method <WiresToFaces> as to be called before.
        can be an empty list.
        """

    def NewEdges(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of new edges built from an edge <E>
        it can be an empty list.
        """

    def GetVerticesForSubstitute(self, VerVerMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Returns the datamap of vertices with their substitutes."""

    def VerticesForSubstitute(self, VerVerMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def SetTolConf(self, theTolConf: float) -> None:
        """Set maximal tolerance used for comparing distances between vertices."""

    def GetTolConf(self) -> float:
        """Get maximal tolerance used for comparing distances between vertices."""

class BRepAlgo_NormalProjection:
    """
    This class makes the projection of a wire on a
    shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: BRepAlgo_NormalProjection) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Add(self, ToProj: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Add an edge or a wire to the list of shape to project"""

    def SetParams(self, Tol3D: float, Tol2D: float, InternalContinuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, MaxSeg: int) -> None:
        """
        Set the parameters used for computation
        Tol3d is the required tolerance between the 3d projected
        curve and its 2d representation
        InternalContinuity is the order of constraints
        used for approximation.
        MaxDeg and MaxSeg are the maximum degree and the maximum
        number of segment for BSpline resulting of an approximation.
        """

    def SetDefaultParams(self) -> None:
        """
        Set the parameters used for computation
        in their default values
        """

    def SetMaxDistance(self, MaxDist: float) -> None:
        """
        Sets the maximum distance between target shape and
        shape to project. If this condition is not satisfied then
        corresponding part of solution is discarded.
        if MaxDist < 0 then this method does not affect the algorithm
        """

    def Compute3d(self, With3d: bool = True) -> None:
        """
        if With3d = false the 3dcurve is not computed
        the initial 3dcurve is kept to build the resulting edges.
        """

    def SetLimit(self, FaceBoundaries: bool = True) -> None:
        """Manage limitation of projected edges."""

    def Build(self) -> None:
        """Builds the result as a compound."""

    def IsDone(self) -> bool: ...

    def Projection(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns the result"""

    def Ancestor(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Shape:
        """For a resulting edge, returns the corresponding initial edge."""

    def Couple(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Shape:
        """For a projected edge, returns the corresponding initial face."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    def IsElementary(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> bool: ...

    def BuildWire(self, Liste: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        build the result as a list of wire if possible in --
        a first returns a wire only if there is only a wire.
        """
