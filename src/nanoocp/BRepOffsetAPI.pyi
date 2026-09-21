"""OCCT package BRepOffsetAPI (toolkit TKOffset)"""

from typing import overload

import nanoocp.Approx
import nanoocp.BRepBuilderAPI
import nanoocp.BRepFill
import nanoocp.BRepOffset
import nanoocp.BRepPrimAPI
import nanoocp.Draft
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.GeomFill
import nanoocp.Law
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.TopoDS
import nanoocp.gp


class BRepOffsetAPI_DraftAngle(nanoocp.BRepBuilderAPI.BRepBuilderAPI_ModifyShape):
    """
    Taper-adding transformations on a shape.
    The resulting shape is constructed by defining one face
    to be tapered after another one, as well as the
    geometric properties of their tapered transformation.
    Each tapered transformation is propagated along the
    series of faces which are tangential to one another and
    which contains the face to be tapered.
    This algorithm is useful in the construction of molds or
    dies. It facilitates the removal of the article being produced.
    A DraftAngle object provides a framework for:
    - initializing the construction algorithm with a given shape,
    - acquiring the data characterizing the faces to be tapered,
    - implementing the construction algorithm, and
    - consulting the results.
    Warning
    - This algorithm treats planar, cylindrical and conical faces.
    - Do not use shapes, which with a draft angle added to
    a face would modify the topology. This would, for
    example, involve creation of new vertices, edges or
    faces, or suppression of existing vertices, edges or faces.
    - Any face, which is continuous in tangency with the
    face to be tapered, will also be tapered. These
    connected faces must also respect the above criteria.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm to perform
        taper-adding transformations on faces of a shape.
        Use the Init function to define the shape to be tapered.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initializes an algorithm to perform taper-adding
        transformations on faces of the shape S.
        S will be referred to as the initial shape of the algorithm.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_DraftAngle) -> None: ...

    def Clear(self) -> None:
        """
        Cancels the results of all taper-adding transformations
        performed by this algorithm on the initial shape. These
        results will have been defined by successive calls to the function Add.
        """

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initializes, or reinitializes this taper-adding algorithm with the shape S.
        S will be referred to as the initial shape of this algorithm.
        """

    def Add(self, F: nanoocp.TopoDS.TopoDS_Face, Direction: nanoocp.gp.gp_Dir, Angle: float, NeutralPlane: nanoocp.gp.gp_Pln, Flag: bool = True) -> None:
        """
        Adds the face F, the direction
        Direction, the angle Angle, the plane NeutralPlane, and the flag
        Flag to the framework created at construction time, and with this
        data, defines the taper-adding transformation.
        F is a face, which belongs to the initial shape of this algorithm or
        to the shape loaded by the function Init.
        Only planar, cylindrical or conical faces can be tapered:
        - If the face F is planar, it is tapered by inclining it
        through the angle Angle about the line of intersection between the
        plane NeutralPlane and F.
        Direction indicates the side of NeutralPlane from which matter is
        removed if Angle is positive or added if Angle is negative.
        - If F is cylindrical or conical, it is transformed in the
        same way on a single face, resulting in a conical face if F
        is cylindrical, and a conical or cylindrical face if it is already conical.
        The taper-adding transformation is propagated from the face F along
        the series of planar, cylindrical or conical faces containing F,
        which are tangential to one another.
        Use the function AddDone to check if this taper-adding transformation is successful.
        Warning
        Nothing is done if:
        - the face F does not belong to the initial shape of this algorithm, or
        - the face F is not planar, cylindrical or conical.
        Exceptions
        - Standard_NullObject if the initial shape is not
        defined, i.e. if this algorithm has not been initialized
        with the non-empty constructor or the Init function.
        - Standard_ConstructionError if the previous call to
        Add has failed. The function AddDone ought to have
        been used to check for this, and the function Remove
        to cancel the results of the unsuccessful taper-adding
        transformation and to retrieve the previous shape.
        """

    def AddDone(self) -> bool:
        """
        Returns true if the previous taper-adding
        transformation performed by this algorithm in the last
        call to Add, was successful.
        If AddDone returns false:
        - the function ProblematicShape returns the face
        on which the error occurred,
        - the function Remove has to be used to cancel the
        results of the unsuccessful taper-adding
        transformation and to retrieve the previous shape.
        Exceptions
        Standard_NullObject if the initial shape has not
        been defined, i.e. if this algorithm has not been
        initialized with the non-empty constructor or the .Init function.
        """

    def Remove(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Cancels the taper-adding transformation previously
        performed by this algorithm on the face F and the
        series of tangential faces which contain F, and retrieves
        the shape before the last taper-adding transformation.
        Warning
        You will have to use this function if the previous call to
        Add fails. Use the function AddDone to check it.
        Exceptions
        - Standard_NullObject if the initial shape has not
        been defined, i.e. if this algorithm has not been
        initialized with the non-empty constructor or the Init function.
        - Standard_NoSuchObject if F has not been added
        or has already been removed.
        """

    def ProblematicShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape on which an error occurred after an
        unsuccessful call to Add or when IsDone returns false.
        Exceptions
        Standard_NullObject if the initial shape has not been
        defined, i.e. if this algorithm has not been initialized with
        the non-empty constructor or the Init function.
        """

    def Status(self) -> nanoocp.Draft.Draft_ErrorStatus:
        """
        Returns an error status when an error has occurred
        (Face, Edge or Vertex recomputation problem).
        Otherwise returns Draft_NoError. The method may be
        called if AddDone returns false, or when
        IsDone returns false.
        """

    def ConnectedFaces(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns all the faces which have been added
        together with the face <F>.
        """

    def ModifiedFaces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns all the faces on which a modification has
        been given.
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    def CorrectWires(self) -> None: ...

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

    def ModifiedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the modified shape corresponding to <S>.
        S can correspond to the entire initial shape or to its subshape.
        Raises exceptions
        Standard_NoSuchObject if S is not the initial shape or
        a subshape of the initial shape to which the
        transformation has been applied.
        """

class BRepOffsetAPI_FindContigousEdges:
    """
    Provides methods to identify contiguous boundaries for continuity control (C0, C1, ...)

    Use this function as following:
    - create an object
    - default tolerance 1.E-06
    - with analysis of degenerated faces on
    - define if necessary a new tolerance
    - set if necessary analysis of degenerated shapes off
    - add shapes to be controlled -> Add
    - compute -> Perform
    - output couples of connected edges for control
    - output the problems if any
    """

    @overload
    def __init__(self, tolerance: float = 1e-06, option: bool = True) -> None:
        """
        Initializes an algorithm for identifying contiguous edges
        on shapes with tolerance as the tolerance of contiguity
        (defaulted to 1.0e-6). This tolerance value is used to
        determine whether two edges or sections of edges are coincident.
        Use the function Add to define the shapes to be checked.
        Set option to false. This argument (defaulted to true) will
        serve in subsequent software releases for performing an
        analysis of degenerated shapes.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_FindContigousEdges) -> None: ...

    def Init(self, tolerance: float, option: bool) -> None:
        """
        Initializes this algorithm for identifying contiguous edges
        on shapes using the tolerance of contiguity tolerance.
        This tolerance value is used to determine whether two
        edges or sections of edges are coincident.
        Use the function Add to define the shapes to be checked.
        Sets <option> to false.
        """

    def Add(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Adds the shape shape to the list of shapes to be
        checked by this algorithm.
        Once all the shapes to be checked have been added,
        use the function Perform to find the contiguous edges
        and the function ContigousEdge to return these edges.
        """

    def Perform(self) -> None:
        """
        Finds coincident parts of edges of two or more shapes
        added to this algorithm and breaks down these edges
        into contiguous and non-contiguous sections on copies
        of the initial shapes.
        The function ContigousEdge returns contiguous
        edges. The function Modified can be used to return
        modified copies of the initial shapes where one or more
        edges were broken down into contiguous and non-contiguous sections.
        Warning
        This function must be used once all the shapes to be
        checked have been added. It is not possible to add
        further shapes subsequently and then to repeat the call to Perform.
        """

    def NbContigousEdges(self) -> int:
        """
        Returns the number of contiguous edges found by the
        function Perform on the shapes added to this algorithm.
        """

    def ContigousEdge(self, index: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the contiguous edge of index index found by
        the function Perform on the shapes added to this algorithm.
        Exceptions
        Standard_OutOfRange if:
        - index is less than 1, or
        - index is greater than the number of contiguous
        edges found by the function Perform on the shapes added to this algorithm.
        """

    def ContigousEdgeCouple(self, index: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of edges coincident with the contiguous
        edge of index index found by the function Perform.
        There are as many edges in the list as there are faces
        adjacent to this contiguous edge.
        Exceptions
        Standard_OutOfRange if:
        - index is less than 1, or
        - index is greater than the number of contiguous edges
        found by the function Perform on the shapes added to this algorithm.
        """

    def SectionToBoundary(self, section: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge on the initial shape, of which the
        modified copy contains the edge section.
        section is coincident with a contiguous edge found by
        the function Perform. Use the function
        ContigousEdgeCouple to obtain a valid section.
        This information is useful for verification purposes, since
        it provides a means of determining the surface to which
        the contiguous edge belongs.
        Exceptions
        Standard_NoSuchObject if section is not coincident
        with a contiguous edge. Use the function
        ContigousEdgeCouple to obtain a valid section.
        """

    def NbDegeneratedShapes(self) -> int:
        """Gives the number of degenerated shapes"""

    def DegeneratedShape(self, index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives a degenerated shape"""

    def IsDegenerated(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Indicates if a input shape is degenerated"""

    def IsModified(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the copy of the initial shape shape was
        modified by the function Perform (i.e. if one or more of
        its edges was broken down into contiguous and non-contiguous sections).
        Warning
        Returns false if shape is not one of the initial shapes
        added to this algorithm.
        """

    def Modified(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Gives a modifieded shape
        Raises NoSuchObject if shape has not been modified
        """

    def Dump(self) -> None:
        """Dump properties of resulting shape."""

class BRepOffsetAPI_MakeDraft(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """Build a draft surface along a wire"""

    @overload
    def __init__(self, Shape: nanoocp.TopoDS.TopoDS_Shape, Dir: nanoocp.gp.gp_Dir, Angle: float) -> None:
        """
        Constructs the draft surface object defined by the shape
        Shape, the direction Dir, and the angle Angle.
        Shape must be a TopoDS_Wire, Topo_DS_Face or
        TopoDS_Shell with free boundaries.
        Exceptions
        Standard_NotDone if Shape is not a TopoDS_Wire,
        Topo_DS_Face or TopoDS_Shell with free boundaries.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakeDraft) -> None: ...

    def SetOptions(self, Style: nanoocp.BRepBuilderAPI.BRepBuilderAPI_TransitionMode = ..., AngleMin: float = 0.01, AngleMax: float = 3.0) -> None:
        """
        Sets the options of this draft tool.
        If a transition has to be performed, it can be defined by
        the mode Style as RightCorner or RoundCorner,
        RightCorner being a corner defined by a sharp angle,
        and RoundCorner being a rounded corner.
        AngleMin is an angular tolerance used to detect
        whether a transition has to be performed or not.
        AngleMax sets the maximum value within which a
        RightCorner transition can be performed.
        AngleMin and AngleMax are expressed in radians.
        """

    def SetDraft(self, IsInternal: bool = False) -> None:
        """
        Sets the direction of the draft for this object.
        If IsInternal is true, the draft is internal to the argument
        Shape used in the constructor.
        """

    @overload
    def Perform(self, LengthMax: float) -> None:
        """
        Performs the draft using the length LengthMax as the
        maximum length for the corner edge between two draft faces.
        """

    @overload
    def Perform(self, Surface: nanoocp.Geom.Geom_Surface | None, KeepInsideSurface: bool = True) -> None:
        """
        Performs the draft up to the surface Surface.
        If KeepInsideSurface is true, the part of Surface inside
        the draft is kept in the result.
        """

    @overload
    def Perform(self, StopShape: nanoocp.TopoDS.TopoDS_Shape, KeepOutSide: bool = True) -> None:
        """
        Performs the draft up to the shape StopShape.
        If KeepOutSide is true, the part of StopShape which is
        outside the Draft is kept in the result.
        """

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """
        Returns the shell resulting from performance of the
        draft along the wire.
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

class BRepOffsetAPI_MakeEvolved(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build evolved shapes.
    An evolved shape is built from a planar spine (face or
    wire) and a profile (wire). The evolved shape is the
    unlooped sweep (pipe) of the profile along the spine.
    Self-intersections are removed.
    A MakeEvolved object provides a framework for:
    - defining the construction of an evolved shape,
    - implementing the construction algorithm, and
    - consulting the result.
    Computes an Evolved by
    1 - sweeping a profile along a spine.
    2 - removing the self-intersections.

    The Profile is expected to be planar and can be a line
    (which lies in infinite number of planes).

    The profile is defined in a Referential R. The position of
    the profile at the current point of the spine is given by
    confusing R and the local referential given by (D0, D1
    and the normal of the Spine).

    The coordinate system is determined by theIsAxeProf argument:
    - if theIsAxeProf is true, R is the global coordinate system,
    - if theIsAxeProf is false, R is computed so that:
    * its origin is given by the point on the spine which is
    closest to the profile,
    * its "X Axis" is given by the tangent to the spine at this point, and
    * its "Z Axis" is the normal to the plane which contains the spine.

    theJoinType defines the type of pipe generated by the salient
    vertices of the spine. The default type is GeomAbs_Arc
    where the vertices generate revolved pipes about the
    axis passing along the vertex and the normal to the
    plane of the spine. At present, this is the only
    construction type implemented.

    if <theIsSolid> is TRUE the Shape result is completed to be a
    solid or a compound of solids.

    If theIsProfOnSpine == TRUE then the profile must connect with the spine.

    If theIsVolume option is switched on then self-intersections
    in the result of Pipe-algorithm will be removed by
    BOPAlgo_MakerVolume algorithm. At that the arguments
    "theJoinType", "theIsAxeProf", "theIsProfOnSpine" are not used.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theSpine: nanoocp.TopoDS.TopoDS_Shape, theProfile: nanoocp.TopoDS.TopoDS_Wire, theJoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, theIsAxeProf: bool = True, theIsSolid: bool = False, theIsProfOnSpine: bool = False, theTol: float = 1e-07, theIsVolume: bool = False, theRunInParallel: bool = False) -> None:
        """
        Constructs an evolved shape by sweeping the profile
        (theProfile) along the spine (theSpine).
        theSpine can be shape only of type wire or face.
        See description to this class for detailed information.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakeEvolved) -> None: ...

    def Evolved(self) -> nanoocp.BRepFill.BRepFill_Evolved: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    def GeneratedShapes(self, SpineShape: nanoocp.TopoDS.TopoDS_Shape, ProfShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the shapes created from a subshape
        <SpineShape> of the spine and a subshape
        <ProfShape> on the profile.
        """

    def Top(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return the face Top if <Solid> is True in the constructor."""

    def Bottom(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return the face Bottom if <Solid> is True in the constructor."""

class BRepOffsetAPI_MakeFilling(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    N-Side Filling
    This algorithm avoids to build a face from:
    * a set of edges defining the bounds of the face and some
    constraints the surface of the face has to satisfy
    * a set of edges and points defining some constraints
    the support surface has to satisfy
    * an initial surface to deform for satisfying the constraints
    * a set of parameters to control the constraints.

    The support surface of the face is computed by deformation
    of the initial surface in order to satisfy the given constraints.
    The set of bounding edges defines the wire of the face.

    If no initial surface is given, the algorithm computes it
    automatically.
    If the set of edges is not connected (Free constraint)
    missing edges are automatically computed.

    Limitations:
    * If some constraints are not compatible
    The algorithm does not take them into account.
    So the constraints will not be satisfyed in an area containing
    the incompatibilitries.
    * The constraints defining the bound of the face have to be
    entered in order to have a continuous wire.

    Other Applications:
    * Deformation of a face to satisfy internal constraints
    * Deformation of a face to improve Gi continuity with
    connected faces
    """

    @overload
    def __init__(self, Degree: int = 3, NbPtsOnCur: int = 15, NbIter: int = 2, Anisotropie: bool = False, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1, MaxDeg: int = 8, MaxSegments: int = 9) -> None:
        """
        Constructs a wire filling object defined by
        - the energy minimizing criterion Degree
        - the number of points on the curve NbPntsOnCur
        - the number of iterations NbIter
        - the Boolean Anisotropie
        - the 2D tolerance Tol2d
        - the 3D tolerance Tol3d
        - the angular tolerance TolAng
        - the tolerance for curvature TolCur
        - the highest polynomial degree MaxDeg
        - the greatest number of segments MaxSeg.
        If the Boolean Anistropie is true, the algorithm's
        performance is better in cases where the ratio of the
        length U and the length V indicate a great difference
        between the two. In other words, when the surface is, for
        example, extremely long.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakeFilling) -> None: ...

    def SetConstrParam(self, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1) -> None:
        """
        Sets the values of Tolerances used to control the constraint.
        Tol2d:
        Tol3d:   it is the maximum distance allowed between the support surface
        and the constraints
        TolAng:  it is the maximum angle allowed between the normal of the surface
        and the constraints
        TolCurv: it is the maximum difference of curvature allowed between
        the surface and the constraint
        """

    def SetResolParam(self, Degree: int = 3, NbPtsOnCur: int = 15, NbIter: int = 2, Anisotropie: bool = False) -> None:
        """
        Sets the parameters used for resolution.
        The default values of these parameters have been chosen for a good
        ratio quality/performance.
        Degree:      it is the order of energy criterion to minimize for computing
        the deformation of the surface.
        The default value is 3
        The recommended value is i+2 where i is the maximum order of the
        constraints.
        NbPtsOnCur:  it is the average number of points for discretisation
        of the edges.
        NbIter:      it is the maximum number of iterations of the process.
        For each iteration the number of discretisation points is
        increased.
        Anisotropie:
        """

    def SetApproxParam(self, MaxDeg: int = 8, MaxSegments: int = 9) -> None:
        """
        Sets the parameters used to approximate the filling
        surface. These include:
        - MaxDeg - the highest degree which the polynomial
        defining the filling surface can have
        - MaxSegments - the greatest number of segments
        which the filling surface can have.
        """

    def LoadInitSurface(self, Surf: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Loads the initial surface Surf to
        begin the construction of the surface.
        This optional function is useful if the surface resulting from
        construction for the algorithm is likely to be complex.
        The support surface of the face under construction is computed by a
        deformation of Surf which satisfies the given constraints.
        The set of bounding edges defines the wire of the face.
        If no initial surface is given, the algorithm computes it
        automatically. If the set of edges is not connected (Free constraint),
        missing edges are automatically computed.
        Important: the initial surface must have orthogonal local coordinates,
        i.e. partial derivatives dS/du and dS/dv must be orthogonal
        at each point of surface.
        If this condition breaks, distortions of resulting surface
        are possible.
        """

    @overload
    def Add(self, Constr: nanoocp.TopoDS.TopoDS_Edge, Order: nanoocp.GeomAbs.GeomAbs_Shape, IsBound: bool = True) -> int:
        """
        Adds a new constraint which also defines an edge of the wire
        of the face
        Order: Order of the constraint:
        GeomAbs_C0 : the surface has to pass by 3D representation
        of the edge
        GeomAbs_G1 : the surface has to pass by 3D representation
        of the edge and to respect tangency with the first
        face of the edge
        GeomAbs_G2 : the surface has to pass by 3D representation
        of the edge and to respect tangency and curvature
        with the first face of the edge.
        Raises ConstructionError if the edge has no representation on a face and Order is
        GeomAbs_G1 or GeomAbs_G2.
        """

    @overload
    def Add(self, Constr: nanoocp.TopoDS.TopoDS_Edge, Support: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape, IsBound: bool = True) -> int:
        """
        Adds a new constraint which also defines an edge of the wire
        of the face
        Order: Order of the constraint:
        GeomAbs_C0 : the surface has to pass by 3D representation
        of the edge
        GeomAbs_G1 : the surface has to pass by 3D representation
        of the edge and to respect tangency with the
        given face
        GeomAbs_G2 : the surface has to pass by 3D representation
        of the edge and to respect tangency and curvature
        with the given face.
        Raises ConstructionError if the edge has no 2d representation on the given face
        """

    @overload
    def Add(self, Support: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Adds a free constraint on a face. The corresponding edge has to
        be automatically recomputed. It is always a bound.
        """

    @overload
    def Add(self, Point: nanoocp.gp.gp_Pnt) -> int: ...

    @overload
    def Add(self, U: float, V: float, Support: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """Adds a punctual constraint."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting faces"""

    def IsDone(self) -> bool:
        """Tests whether computation of the filling plate has been completed."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    @overload
    def G0Error(self) -> float:
        """
        Returns the maximum distance between the result and
        the constraints. This is set at construction time.
        """

    @overload
    def G0Error(self, Index: int) -> float:
        """
        Returns the maximum distance attained between the
        result and the constraint Index. This is set at construction time.
        """

    @overload
    def G1Error(self) -> float: ...

    @overload
    def G1Error(self, Index: int) -> float:
        """
        Returns the maximum angle between the result and the
        constraints. This is set at construction time.
        """

    @overload
    def G2Error(self) -> float:
        """
        Returns the maximum angle between the result and the
        constraints. This is set at construction time.
        """

    @overload
    def G2Error(self, Index: int) -> float:
        """
        Returns the greatest difference in curvature found
        between the result and the constraint Index.
        """

class BRepOffsetAPI_MakeOffset(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes algorithms for offsetting wires from a set of
    wires contained in a planar face.
    A MakeOffset object provides a framework for:
    - defining the construction of an offset,
    - implementing the construction algorithm, and
    - consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an algorithm for creating an empty offset"""

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Face, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None:
        """
        Constructs an algorithm for creating an algorithm
        to build parallels to the spine Spine
        """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakeOffset) -> None: ...

    @overload
    def Init(self, Spine: nanoocp.TopoDS.TopoDS_Face, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None:
        """
        Initializes the algorithm to construct parallels to the spine Spine.
        Join defines the type of parallel generated by the
        salient vertices of the spine.
        The default type is GeomAbs_Arc where the vertices generate
        sections of a circle.
        If join type is GeomAbs_Intersection, the edges that
        intersect in a salient vertex generate the edges
        prolonged until intersection.
        """

    @overload
    def Init(self, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None:
        """Initialize the evaluation of Offsetting."""

    def SetApprox(self, ToApprox: bool) -> None:
        """
        Set approximation flag
        for conversion input contours into ones consisting of
        2D circular arcs and 2D linear segments only.
        """

    def AddWire(self, Spine: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Initializes the algorithm to construct parallels to the wire Spine."""

    def Perform(self, Offset: float, Alt: float = 0.0) -> None:
        """
        Computes a parallel to the spine at distance Offset and
        at an altitude Alt from the plane of the spine in relation
        to the normal to the spine.
        Exceptions: StdFail_NotDone if the offset is not built.
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        returns a list of the created shapes
        from the shape <S>.
        """

    @staticmethod
    def ConvertFace(theFace: nanoocp.TopoDS.TopoDS_Face, theAngleTolerance: float) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Converts each wire of the face into contour consisting only of
        arcs and segments. New 3D curves are built too.
        """

class BRepOffsetAPI_MakeOffsetShape(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build a shell out of a shape. The
    result is an unlooped shape parallel to the source shape.
    A MakeOffsetShape object provides a framework for:
    - defining the construction of a shell
    - implementing the construction algorithm
    - consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """Constructor does nothing."""

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakeOffsetShape) -> None: ...

    def PerformBySimple(self, theS: nanoocp.TopoDS.TopoDS_Shape, theOffsetValue: float) -> None:
        """
        Constructs offset shape for the given one using simple algorithm without intersections
        computation.
        """

    def PerformByJoin(self, S: nanoocp.TopoDS.TopoDS_Shape, Offset: float, Tol: float, Mode: nanoocp.BRepOffset.BRepOffset_Mode = BRepOffset_Mode.BRepOffset_Skin, Intersection: bool = False, SelfInter: bool = False, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, RemoveIntEdges: bool = False, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructs a shape parallel to the shape S, where
        - S may be a face, a shell, a solid or a compound of these shape kinds;
        - Offset is the offset value. The offset shape is constructed:
        - outside S, if Offset is positive,
        - inside S, if Offset is negative;
        - Tol defines the coincidence tolerance criterion for generated shapes;
        - Mode defines the construction type of parallels
        applied to the free edges of shape S; currently, only one
        construction type is implemented, namely the one where the free
        edges do not generate parallels; this corresponds to the default
        value BRepOffset_Skin;
        - Intersection specifies how the algorithm must work in
        order to limit the parallels to two adjacent shapes:
        - if Intersection is false (default value), the intersection
        is calculated with the parallels to the two adjacent shapes,
        - if Intersection is true, the intersection is calculated by
        taking all generated parallels into account; this computation method is
        more general as it avoids some self-intersections generated in the
        offset shape from features of small dimensions on shape S, however this
        method has not been completely implemented and therefore is not
        recommended for use;
        - SelfInter tells the algorithm whether a computation
        to eliminate self-intersections must be applied to the resulting
        shape; however, as this functionality is not yet
        implemented, it is recommended to use the default value (false);
        - Join defines how to fill the holes that may appear between
        parallels to the two adjacent faces. It may take values
        GeomAbs_Arc or GeomAbs_Intersection:
        - if Join is equal to GeomAbs_Arc, then pipes are generated
        between two free edges of two adjacent parallels,
        and spheres are generated on "images" of vertices;
        it is the default value,
        - if Join is equal to GeomAbs_Intersection, then the parallels to the
        two adjacent faces are enlarged and intersected,
        so that there are no free edges on parallels to faces.
        RemoveIntEdges flag defines whether to remove the INTERNAL edges
        from the result or not.
        Warnings
        1. All the faces of the shape S should be based on the surfaces
        with continuity at least C1.
        2. The offset value should be sufficiently small to avoid
        self-intersections in resulting shape. Otherwise these
        self-intersections may appear inside an offset face if its
        initial surface is not plane or sphere or cylinder, also some
        non-adjacent offset faces may intersect each other. Also, some
        offset surfaces may "turn inside out".
        3. The algorithm may fail if the shape S contains vertices where
        more than 3 edges converge.
        4. Since 3d-offset algorithm involves intersection of surfaces,
        it is under limitations of surface intersection algorithm.
        5. A result cannot be generated if the underlying geometry of S is
        BSpline with continuity C0.
        Exceptions
        Geom_UndefinedDerivative if the underlying
        geometry of S is BSpline with continuity C0.
        """

    def MakeOffset(self) -> nanoocp.BRepOffset.BRepOffset_MakeOffset:
        """Returns instance of the underlying intersection / arc algorithm."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Does nothing."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of shapes generated from the shape <S>."""

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of shapes Modified from the shape <S>."""

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the shape has been removed from the result."""

    def GetJoinType(self) -> nanoocp.GeomAbs.GeomAbs_JoinType:
        """Returns offset join type."""

class BRepOffsetAPI_MakePipe(nanoocp.BRepPrimAPI.BRepPrimAPI_MakeSweep):
    """
    Describes functions to build pipes.
    A pipe is built a basis shape (called the profile) along
    a wire (called the spine) by sweeping.
    The profile must not contain solids.
    A MakePipe object provides a framework for:
    - defining the construction of a pipe,
    - implementing the construction algorithm, and
    - consulting the result.
    Warning
    The MakePipe class implements pipe constructions
    with G1 continuous spines only.
    """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Constructs a pipe by sweeping the shape Profile along
        the wire Spine.The angle made by the spine with the profile is
        maintained along the length of the pipe.
        Warning
        Spine must be G1 continuous; that is, on the connection
        vertex of two edges of the wire, the tangent vectors on
        the left and on the right must have the same direction,
        though not necessarily the same magnitude.
        Exceptions
        Standard_DomainError if the profile is a solid or a
        composite solid.
        """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Shape, aMode: nanoocp.GeomFill.GeomFill_Trihedron, ForceApproxC1: bool = False) -> None:
        """
        the same as previous but with setting of
        mode of sweep and the flag that indicates attempt
        to approximate a C1-continuous surface if a swept
        surface proved to be C0.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakePipe) -> None: ...

    def Pipe(self) -> nanoocp.BRepFill.BRepFill_Pipe: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the prism."""

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the prism."""

    @overload
    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def Generated(self, SSpine: nanoocp.TopoDS.TopoDS_Shape, SProfile: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ErrorOnSurface(self) -> float: ...

class BRepOffsetAPI_MakePipeShell(nanoocp.BRepPrimAPI.BRepPrimAPI_MakeSweep):
    """
    This class provides for a framework to construct a shell
    or a solid along a spine consisting in a wire.
    To produce a solid, the initial wire must be closed.
    Two approaches are used:
    - definition by section
    - by a section and a scaling law
    - by addition of successive intermediary sections
    - definition by sweep mode.
    - pseudo-Frenet
    - constant
    - binormal constant
    - normal defined by a surface support
    - normal defined by a guiding contour.
    The two global approaches can also be combined.
    You can also close the surface later in order to form a solid.
    Warning: some limitations exist
    -- Mode with auxiliary spine is incompatible with hometetic laws
    -- Mode with auxiliary spine and keep contact produce only CO surface.
    """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Constructs the shell-generating framework defined by the wire Spine.
        Sets an sweep's mode
        If no mode are set, the mode use in MakePipe is used
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakePipeShell) -> None: ...

    @overload
    def SetMode(self, IsFrenet: bool = False) -> None:
        """
        Sets a Frenet or a CorrectedFrenet trihedron
        to perform the sweeping
        If IsFrenet is false, a corrected Frenet trihedron is used.
        """

    @overload
    def SetMode(self, Axe: nanoocp.gp.gp_Ax2) -> None:
        """
        Sets a fixed trihedron to perform the sweeping
        all sections will be parallel.
        """

    @overload
    def SetMode(self, BiNormal: nanoocp.gp.gp_Dir) -> None:
        """
        Sets a fixed BiNormal direction to perform the
        sweeping. Angular relations between the
        section(s) and <BiNormal> will be constant
        """

    @overload
    def SetMode(self, SpineSupport: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Sets support to the spine to define the BiNormal of
        the trihedron, like the normal to the surfaces.
        Warning: To be effective, Each edge of the <spine> must
        have a representation on one face of<SpineSupport>
        """

    @overload
    def SetMode(self, AuxiliarySpine: nanoocp.TopoDS.TopoDS_Wire, CurvilinearEquivalence: bool, KeepContact: nanoocp.BRepFill.BRepFill_TypeOfContact = BRepFill_TypeOfContact.BRepFill_NoContact) -> None:
        """
        Sets an auxiliary spine to define the Normal
        For each Point of the Spine P, an Point Q is evaluated
        on <AuxiliarySpine>
        If <CurvilinearEquivalence>
        Q split <AuxiliarySpine> with the same length ratio
        than P split <Spline>.
        Else the plan define by P and the tangent to the <Spine>
        intersect <AuxiliarySpine> in Q.
        If <KeepContact> equals BRepFill_NoContact: The Normal is defined
        by the vector PQ.
        If <KeepContact> equals BRepFill_Contact: The Normal is defined to
        achieve that the sweeped section is in contact to the
        auxiliarySpine. The width of section is constant all along the path.
        In other words, the auxiliary spine lies on the swept surface,
        but not necessarily is a boundary of this surface. However,
        the auxiliary spine has to be close enough to the main spine
        to provide intersection with any section all along the path.
        If <KeepContact> equals BRepFill_ContactOnBorder: The auxiliary spine
        becomes a boundary of the swept surface and the width of section varies
        along the path.
        Give section to sweep.
        Possibilities are:
        - Give one or several section
        - Give one profile and an homotetic law.
        - Automatic compute of correspondence between spine, and section
        on the sweeped shape
        - correspondence between spine, and section on the sweeped shape
        defined by a vertex of the spine
        """

    def SetDiscreteMode(self) -> None:
        """
        Sets a Discrete trihedron
        to perform the sweeping
        """

    @overload
    def Add(self, Profile: nanoocp.TopoDS.TopoDS_Shape, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Adds the section Profile to this framework. First and last
        sections may be punctual, so the shape Profile may be
        both wire and vertex. Correspondent point on spine is
        computed automatically.
        If WithContact is true, the section is translated to be in
        contact with the spine.
        If WithCorrection is true, the section is rotated to be
        orthogonal to the spine?s tangent in the correspondent
        point. This option has no sense if the section is punctual
        (Profile is of type TopoDS_Vertex).
        """

    @overload
    def Add(self, Profile: nanoocp.TopoDS.TopoDS_Shape, Location: nanoocp.TopoDS.TopoDS_Vertex, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Adds the section Profile to this framework.
        Correspondent point on the spine is given by Location.
        Warning:
        To be effective, it is not recommended to combine methods Add and SetLaw.
        """

    @overload
    def SetLaw(self, Profile: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.Law.Law_Function | None, WithContact: bool = False, WithCorrection: bool = False) -> None: ...

    @overload
    def SetLaw(self, Profile: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.Law.Law_Function | None, Location: nanoocp.TopoDS.TopoDS_Vertex, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Sets the evolution law defined by the wire Profile with
        its position (Location, WithContact, WithCorrection
        are the same options as in methods Add) and a
        homotetic law defined by the function L.
        Warning:
        To be effective, it is not recommended to combine methods Add and SetLaw.
        """

    def Delete(self, Profile: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Removes the section Profile from this framework."""

    def IsReady(self) -> bool:
        """
        Returns true if this tool object is ready to build the
        shape, i.e. has a definition for the wire section Profile.
        """

    def GetStatus(self) -> nanoocp.BRepBuilderAPI.BRepBuilderAPI_PipeError:
        """
        Get a status, when Simulate or Build failed. It can be
        BRepBuilderAPI_PipeDone,
        BRepBuilderAPI_PipeNotDone,
        BRepBuilderAPI_PlaneNotIntersectGuide,
        BRepBuilderAPI_ImpossibleContact.
        """

    def SetTolerance(self, Tol3d: float = 0.0001, BoundTol: float = 0.0001, TolAngular: float = 0.01) -> None:
        """
        Sets the following tolerance values
        - 3D tolerance Tol3d
        - boundary tolerance BoundTol
        - angular tolerance TolAngular.
        """

    def SetMaxDegree(self, NewMaxDegree: int) -> None:
        """Define the maximum V degree of resulting surface"""

    def SetMaxSegments(self, NewMaxSegments: int) -> None:
        """
        Define the maximum number of spans in V-direction
        on resulting surface
        """

    def SetForceApproxC1(self, ForceApproxC1: bool) -> None:
        """
        Set the flag that indicates attempt to approximate
        a C1-continuous surface if a swept surface proved
        to be C0.
        """

    def SetTransitionMode(self, Mode: nanoocp.BRepBuilderAPI.BRepBuilderAPI_TransitionMode = ...) -> None:
        """
        Sets the transition mode to manage discontinuities on
        the swept shape caused by fractures on the spine. The
        transition mode can be BRepBuilderAPI_Transformed
        (default value), BRepBuilderAPI_RightCorner,
        BRepBuilderAPI_RoundCorner:
        -              RepBuilderAPI_Transformed:
        discontinuities are treated by
        modification of the sweeping mode. The
        pipe is "transformed" at the fractures of
        the spine. This mode assumes building a
        self-intersected shell.
        -              BRepBuilderAPI_RightCorner:
        discontinuities are treated like right
        corner. Two pieces of the pipe
        corresponding to two adjacent
        segments of the spine are extended
        and intersected at a fracture of the spine.
        -              BRepBuilderAPI_RoundCorner:
        discontinuities are treated like round
        corner. The corner is treated as rotation
        of the profile around an axis which
        passes through the point of the spine's
        fracture. This axis is based on cross
        product of directions tangent to the
        adjacent segments of the spine at their common point.
        Warnings
        The mode BRepBuilderAPI_RightCorner provides a
        valid result if intersection of two pieces of the pipe
        (corresponding to two adjacent segments of the spine)
        in the neighborhood of the spine?s fracture is
        connected and planar. This condition can be violated if
        the spine is non-linear in some neighborhood of the
        fracture or if the profile was set with a scaling law.
        The last mode, BRepBuilderAPI_RoundCorner, will
        assuredly provide a good result only if a profile was set
        with option WithCorrection = True, i.e. it is strictly
        orthogonal to the spine.
        """

    def Simulate(self, NumberOfSection: int, Result: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Simulates the resulting shape by calculating its
        cross-sections. The spine is divided by this
        cross-sections into (NumberOfSection - 1) equal
        parts, the number of cross-sections is
        NumberOfSection. The cross-sections are wires and
        they are returned in the list Result.
        This gives a rapid preview of the resulting shape,
        which will be obtained using the settings you have provided.
        Raises NotDone if <me> it is not Ready
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    def MakeSolid(self) -> bool:
        """
        Transforms the sweeping Shell in Solid.
        If a propfile is not closed returns False
        """

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the sweep."""

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the sweep."""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of new shapes generated from the shape
        S by the shell-generating algorithm.
        This function is redefined from BRepOffsetAPI_MakeShape::Generated.
        S can be an edge or a vertex of a given Profile (see methods Add).
        """

    def ErrorOnSurface(self) -> float: ...

    def SetIsBuildHistory(self, theIsBuildHistory: bool) -> None:
        """
        Sets the build history flag.
        If set to True, the pipe shell will store the history of the sections
        and the spine, which can be used for further modifications or analysis.
        """

    def IsBuildHistory(self) -> bool:
        """
        Returns the build history flag.
        If True, the pipe shell stores the history of the sections and the spine.
        """

    def Profiles(self, theProfiles: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Returns the list of original profiles"""

    def Spine(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the spine"""

class BRepOffsetAPI_MakeThickSolid(BRepOffsetAPI_MakeOffsetShape):
    """
    Describes functions to build hollowed solids.
    A hollowed solid is built from an initial solid and a set of
    faces on this solid, which are to be removed. The
    remaining faces of the solid become the walls of the
    hollowed solid, their thickness defined at the time of construction.
    the solid is built from an initial
    solid <S> and a set of faces {Fi} from <S>,
    builds a solid composed by two shells closed by
    the {Fi}. First shell <SS> is composed by all
    the faces of <S> expected {Fi}. Second shell is
    the offset shell of <SS>.
    A MakeThickSolid object provides a framework for:
    - defining the cross-section of a hollowed solid,
    - implementing the construction algorithm, and
    - consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """Constructor does nothing."""

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MakeThickSolid) -> None: ...

    def MakeThickSolidBySimple(self, theS: nanoocp.TopoDS.TopoDS_Shape, theOffsetValue: float) -> None:
        """
        Constructs solid using simple algorithm.
        According to its nature it is not possible to set list of the closing faces.
        This algorithm does not support faces removing. It is caused by fact that
        intersections are not computed during offset creation.
        Non-closed shell or face is expected as input.
        """

    def MakeThickSolidByJoin(self, S: nanoocp.TopoDS.TopoDS_Shape, ClosingFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Offset: float, Tol: float, Mode: nanoocp.BRepOffset.BRepOffset_Mode = BRepOffset_Mode.BRepOffset_Skin, Intersection: bool = False, SelfInter: bool = False, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, RemoveIntEdges: bool = False, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructs a hollowed solid from
        the solid S by removing the set of faces ClosingFaces from S, where:
        Offset defines the thickness of the walls. Its sign indicates
        which side of the surface of the solid the hollowed shape is built on;
        - Tol defines the tolerance criterion for coincidence in generated shapes;
        - Mode defines the construction type of parallels applied to free
        edges of shape S. Currently, only one construction type is
        implemented, namely the one where the free edges do not generate
        parallels; this corresponds to the default value BRepOffset_Skin;
        Intersection specifies how the algorithm must work in order to
        limit the parallels to two adjacent shapes:
        - if Intersection is false (default value), the intersection
        is calculated with the parallels to the two adjacent shapes,
        -     if Intersection is true, the intersection is calculated by
        taking account of all parallels generated; this computation
        method is more general as it avoids self-intersections
        generated in the offset shape from features of small dimensions
        on shape S, however this method has not been completely
        implemented and therefore is not recommended for use;
        -     SelfInter tells the algorithm whether a computation to
        eliminate self-intersections needs to be applied to the
        resulting shape. However, as this functionality is not yet
        implemented, you should use the default value (false);
        - Join defines how to fill the holes that may appear between
        parallels to the two adjacent faces. It may take values
        GeomAbs_Arc or GeomAbs_Intersection:
        - if Join is equal to GeomAbs_Arc, then pipes are generated
        between two free edges of two adjacent parallels,
        and spheres are generated on "images" of vertices;
        it is the default value,
        - if Join is equal to GeomAbs_Intersection,
        then the parallels to the two adjacent faces are
        enlarged and intersected, so that there are no free
        edges on parallels to faces.
        RemoveIntEdges flag defines whether to remove the INTERNAL edges
        from the result or not.
        Warnings
        Since the algorithm of MakeThickSolid is based on
        MakeOffsetShape algorithm, the warnings are the same as for
        MakeOffsetShape.
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape
        <S>.
        """

class BRepOffsetAPI_MiddlePath(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build a middle path of a
    pipe-like shape
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, StartShape: nanoocp.TopoDS.TopoDS_Shape, EndShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        General constructor.
        StartShape and EndShape may be
        a wire or a face
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_MiddlePath) -> None: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

class BRepOffsetAPI_NormalProjection(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    A framework to define projection onto a shape
    according to the normal from each point to be projected.
    The target shape is a face, and the source shape is an edge or a wire.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty framework to define projection on
        a shape according to the normal from each point to be
        projected to the shape.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Constructs a framework to define projection onto the
        basis shape S according to the normal from each point
        to be projected from the shape added to this framework by Add.
        Default parameters of the algorithm: Tol3D = 1.e-04, Tol2D =sqr(tol3d)
        , InternalContinuity = GeomAbs_C2, MaxDegree = 14, MaxSeg = 16.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_NormalProjection) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the empty constructor framework with the shape S."""

    def Add(self, ToProj: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Adds the shape ToProj to the framework for calculation
        of the projection by Compute3d.
        ToProj is an edge or a wire and will be projected onto the basis shape.
        Exceptions
        Standard_ConstructionError if ToProj is not added.
        """

    def SetParams(self, Tol3D: float, Tol2D: float, InternalContinuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, MaxSeg: int) -> None:
        """
        Sets the parameters used for computation
        Tol3 is the required tolerance between the 3d projected
        curve and its 2d representation
        InternalContinuity is the order of constraints
        used for approximation
        MaxDeg and MaxSeg are the maximum degree and the maximum
        number of segment for BSpline resulting of an approximation.
        """

    def SetMaxDistance(self, MaxDist: float) -> None:
        """
        Sets the maximum distance between target shape and
        shape to project. If this condition is not satisfied then corresponding
        part of solution is discarded.
        if MaxDist < 0 then this method does not affect the algorithm
        """

    def SetLimit(self, FaceBoundaries: bool = True) -> None:
        """Manage limitation of projected edges."""

    def Compute3d(self, With3d: bool = True) -> None:
        """
        Returns true if a 3D curve is computed. If not, false is
        returned and an initial 3D curve is kept to build the resulting edges.
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Builds the result of the projection as a compound of
        wires. Tries to build oriented wires.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the object was correctly built by the shape
        construction algorithm.
        If at the construction time of the shape, the algorithm
        cannot be completed, or the original data is corrupted,
        IsDone returns false and therefore protects the use of
        functions to access the result of the construction
        (typically the Shape function).
        """

    def Projection(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Performs the projection.
        The construction of the result is performed by Build.
        Exceptions
        StdFail_NotDone if the projection was not performed.
        """

    def Couple(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the initial face corresponding to the projected edge E.
        Exceptions
        StdFail_NotDone if no face was found.
        Standard_NoSuchObject if a face corresponding to
        E has already been found.
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    def Ancestor(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the initial edge corresponding to the edge E
        resulting from the computation of the projection.
        Exceptions
        StdFail_NotDone if no edge was found.
        Standard_NoSuchObject if an edge corresponding to
        E has already been found.
        """

    def BuildWire(self, Liste: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        build the result as a list of wire if possible in --
        a first returns a wire only if there is only a wire.
        """

class BRepOffsetAPI_ThruSections(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build a loft. This is a shell or a
    solid passing through a set of sections in a given
    sequence. Usually sections are wires, but the first and
    the last sections may be vertices (punctual sections).
    """

    @overload
    def __init__(self, isSolid: bool = False, ruled: bool = False, pres3d: float = 1e-06) -> None:
        """
        Initializes an algorithm for building a shell or a solid
        passing through a set of sections, where:
        -          isSolid is set to true if the construction algorithm is
        required to build a solid or to false if it is required to build
        a shell (the default value),
        -          ruled is set to true if the faces generated between
        the edges of two consecutive wires are ruled surfaces or to
        false (the default value) if they are smoothed out by approximation,
        -          pres3d defines the precision criterion used by the
        approximation algorithm; the default value is 1.0e-6.
        Use AddWire and AddVertex to define the
        successive sections of the shell or solid to be built.
        """

    @overload
    def __init__(self, theOther: BRepOffsetAPI_ThruSections) -> None: ...

    def Init(self, isSolid: bool = False, ruled: bool = False, pres3d: float = 1e-06) -> None:
        """
        Initializes this algorithm for building a shell or a solid
        passing through a set of sections, where:
        - isSolid is set to true if this construction algorithm is
        required to build a solid or to false if it is required to
        build a shell. false is the default value;
        - ruled is set to true if the faces generated between the
        edges of two consecutive wires are ruled surfaces or
        to false (the default value) if they are smoothed out by approximation,
        - pres3d defines the precision criterion used by the
        approximation algorithm; the default value is 1.0e-6.
        Use AddWire and AddVertex to define the successive
        sections of the shell or solid to be built.
        """

    def AddWire(self, wire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Adds the wire wire to the set of
        sections through which the shell or solid is built.
        Use the Build function to construct the shape.
        """

    def AddVertex(self, aVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Adds the vertex Vertex (punctual section) to the set of sections
        through which the shell or solid is built. A vertex may be added to the
        set of sections only as first or last section. At least one wire
        must be added to the set of sections by the method AddWire.
        Use the Build function to construct the shape.
        """

    def CheckCompatibility(self, check: bool = True) -> None:
        """
        Sets/unsets the option to
        compute origin and orientation on wires to avoid twisted results
        and update wires to have same number of edges.
        """

    def SetSmoothing(self, UseSmoothing: bool) -> None:
        """Define the approximation algorithm"""

    def SetParType(self, ParType: nanoocp.Approx.Approx_ParametrizationType) -> None:
        """Define the type of parametrization used in the approximation"""

    def SetContinuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Define the Continuity used in the approximation"""

    def SetCriteriumWeight(self, W1: float, W2: float, W3: float) -> None:
        """
        define the Weights associed to the criterium used in
        the optimization.

        if Wi <= 0
        """

    def SetMaxDegree(self, MaxDeg: int) -> None:
        """Define the maximal U degree of result surface"""

    def ParType(self) -> nanoocp.Approx.Approx_ParametrizationType:
        """returns the type of parametrization used in the approximation"""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """returns the Continuity used in the approximation"""

    def MaxDegree(self) -> int:
        """returns the maximal U degree of result surface"""

    def UseSmoothing(self) -> bool:
        """Define the approximation algorithm"""

    def CriteriumWeight(self) -> tuple[float, float, float]:
        """
        returns the Weights associed to the criterium used in
        the optimization.
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the loft if solid"""

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the loft if solid"""

    def GeneratedFace(self, Edge: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        if Ruled
        Returns the Face generated by each edge
        except the last wire
        if smoothed
        Returns the Face generated by each edge of the first wire
        """

    def SetMutableInput(self, theIsMutableInput: bool) -> None:
        """
        Sets the mutable input state.
        If true then the input profile can be modified inside
        the thrusection operation. Default value is true.
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of new shapes generated from the shape
        S by the shell-generating algorithm.
        This function is redefined from BRepBuilderAPI_MakeShape::Generated.
        S can be an edge or a vertex of a given Profile (see methods AddWire and AddVertex).
        """

    def Wires(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of original wires"""

    def IsMutableInput(self) -> bool:
        """Returns the current mutable input state"""

    def GetStatus(self) -> nanoocp.BRepFill.BRepFill_ThruSectionErrorStatus:
        """Returns the status of thrusection operation"""

# C++ typedef aliases
BRepOffsetAPI_Sewing = nanoocp.BRepBuilderAPI.BRepBuilderAPI_Sewing
