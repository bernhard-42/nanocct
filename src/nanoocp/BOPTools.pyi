"""OCCT package BOPTools (toolkit TKBO)"""

from typing import overload

import nanoocp.BRepAdaptor
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.IntTools
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class BOPTools_CoupleOfShape:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_CoupleOfShape) -> None: ...

    def SetShape1(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Shape1(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def SetShape2(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Shape2(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class BOPTools_ConnexityBlock:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_ConnexityBlock) -> None: ...

    def Shapes(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ChangeShapes(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def SetRegular(self, theFlag: bool) -> None: ...

    def IsRegular(self) -> bool: ...

    def Loops(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ChangeLoops(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class BOPTools_AlgoTools:
    """
    Provides tools used in Boolean Operations algorithm:
    - Vertices intersection;
    - Vertex construction;
    - Edge construction;
    - Classification algorithms;
    - Making connexity blocks;
    - Shape validation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_AlgoTools) -> None: ...

    @staticmethod
    def DTolerance() -> float:
        """
        @name Constants
        Additional tolerance (delta tolerance) is used in Boolean Operations
        to ensure that the tolerance of new/old entities obtained
        by intersection of two shapes is slightly bigger than the actual
        distances to these shapes. It helps to avoid numerical instability
        which may occur when comparing distances and tolerances.
        """

    @overload
    @staticmethod
    def ComputeVV(theV: nanoocp.TopoDS.TopoDS_Vertex, theP: nanoocp.gp.gp_Pnt, theTolP: float) -> int:
        """
        @name Intersection of the vertices
        Intersects the vertex <theV1> with the point <theP> with tolerance <theTolP>.
        Returns the error status:
        - 0 - no error, meaning that the vertex intersects the point;
        - 1 - the distance between vertex and point is grater than the sum of tolerances.
        """

    @overload
    @staticmethod
    def ComputeVV(theV1: nanoocp.TopoDS.TopoDS_Vertex, theV2: nanoocp.TopoDS.TopoDS_Vertex, theFuzz: float = 1e-07) -> int:
        """
        Intersects the given vertices with given fuzzy value.
        Returns the error status:
        - 0 - no error, meaning that the vertices interferes with given tolerance;
        - 1 - the distance between vertices is grater than the sum of their tolerances.
        """

    @staticmethod
    def MakeVertex(theLV: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theV: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        @name Vertices construction
        Makes the vertex in the middle of given vertices with
        the tolerance covering all tolerance spheres of vertices.
        """

    @overload
    @staticmethod
    def MakeNewVertex(aP1: nanoocp.gp.gp_Pnt, aTol: float, aNewVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """Make a vertex using 3D-point <aP1> and 3D-tolerance value <aTol>"""

    @overload
    @staticmethod
    def MakeNewVertex(aV1: nanoocp.TopoDS.TopoDS_Vertex, aV2: nanoocp.TopoDS.TopoDS_Vertex, aNewVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """Make a vertex using couple of vertices <aV1, aV2>"""

    @overload
    @staticmethod
    def MakeNewVertex(aE1: nanoocp.TopoDS.TopoDS_Edge, aP1: float, aE2: nanoocp.TopoDS.TopoDS_Edge, aP2: float, aNewVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Make a vertex in place of intersection between two edges
        <aE1, aE2> with parameters <aP1, aP2>
        """

    @overload
    @staticmethod
    def MakeNewVertex(aE1: nanoocp.TopoDS.TopoDS_Edge, aP1: float, aF2: nanoocp.TopoDS.TopoDS_Face, aNewVertex: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Make a vertex in place of intersection between the edge <aE1>
        with parameter <aP1> and the face <aF2>
        """

    @overload
    @staticmethod
    def UpdateVertex(aIC: nanoocp.IntTools.IntTools_Curve, aT: float, aV: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        @name Updating the vertex
        Update the tolerance value for vertex <aV>
        taking into account the fact that <aV> lays on
        the curve <aIC>
        """

    @overload
    @staticmethod
    def UpdateVertex(aE: nanoocp.TopoDS.TopoDS_Edge, aT: float, aV: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Update the tolerance value for vertex <aV>
        taking into account the fact that <aV> lays on
        the edge <aE>
        """

    @overload
    @staticmethod
    def UpdateVertex(aVF: nanoocp.TopoDS.TopoDS_Vertex, aVN: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Update the tolerance value for vertex <aVN>
        taking into account the fact that <aVN> should
        cover tolerance zone of <aVF>
        """

    @staticmethod
    def MakeEdge(theCurve: nanoocp.IntTools.IntTools_Curve, theV1: nanoocp.TopoDS.TopoDS_Vertex, theT1: float, theV2: nanoocp.TopoDS.TopoDS_Vertex, theT2: float, theTolR3D: float, theE: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        @name Edge construction
        Makes the edge based on the given curve with given bounding vertices.
        """

    @staticmethod
    def CopyEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """Makes a copy of <theEdge> with vertices."""

    @staticmethod
    def MakeSplitEdge(aE1: nanoocp.TopoDS.TopoDS_Edge, aV1: nanoocp.TopoDS.TopoDS_Vertex, aP1: float, aV2: nanoocp.TopoDS.TopoDS_Vertex, aP2: float, aNewEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Make the edge from base edge <aE1> and two vertices <aV1,aV2>
        at parameters <aP1,aP2>
        """

    @staticmethod
    def MakeSectEdge(aIC: nanoocp.IntTools.IntTools_Curve, aV1: nanoocp.TopoDS.TopoDS_Vertex, aP1: float, aV2: nanoocp.TopoDS.TopoDS_Vertex, aP2: float, aNewEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Make the edge from 3D-Curve <aIC> and two vertices <aV1,aV2>
        at parameters <aP1,aP2>
        """

    @overload
    @staticmethod
    def ComputeState(thePoint: nanoocp.gp.gp_Pnt, theSolid: nanoocp.TopoDS.TopoDS_Solid, theTol: float, theContext: nanoocp.IntTools.IntTools_Context | None) -> nanoocp.TopAbs.TopAbs_State:
        """
        @name Point/Edge/Face classification relatively solid
        Computes the 3-D state of the point thePoint
        toward solid theSolid.
        theTol - value of precision of computation
        theContext- cached geometrical tools
        Returns 3-D state.
        """

    @overload
    @staticmethod
    def ComputeState(theVertex: nanoocp.TopoDS.TopoDS_Vertex, theSolid: nanoocp.TopoDS.TopoDS_Solid, theTol: float, theContext: nanoocp.IntTools.IntTools_Context | None) -> nanoocp.TopAbs.TopAbs_State:
        """
        Computes the 3-D state of the vertex theVertex
        toward solid theSolid.
        theTol - value of precision of computation
        theContext- cached geometrical tools
        Returns 3-D state.
        """

    @overload
    @staticmethod
    def ComputeState(theEdge: nanoocp.TopoDS.TopoDS_Edge, theSolid: nanoocp.TopoDS.TopoDS_Solid, theTol: float, theContext: nanoocp.IntTools.IntTools_Context | None) -> nanoocp.TopAbs.TopAbs_State:
        """
        Computes the 3-D state of the edge theEdge
        toward solid theSolid.
        theTol - value of precision of computation
        theContext- cached geometrical tools
        Returns 3-D state.
        """

    @overload
    @staticmethod
    def ComputeState(theFace: nanoocp.TopoDS.TopoDS_Face, theSolid: nanoocp.TopoDS.TopoDS_Solid, theTol: float, theBounds: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theContext: nanoocp.IntTools.IntTools_Context | None) -> nanoocp.TopAbs.TopAbs_State:
        """
        Computes the 3-D state of the face theFace
        toward solid theSolid.
        theTol - value of precision of computation
        theBounds - set of edges of <theSolid> to avoid
        theContext- cached geometrical tools
        Returns 3-D state.
        """

    @staticmethod
    def ComputeStateByOnePoint(theShape: nanoocp.TopoDS.TopoDS_Shape, theSolid: nanoocp.TopoDS.TopoDS_Solid, theTol: float, theContext: nanoocp.IntTools.IntTools_Context | None) -> nanoocp.TopAbs.TopAbs_State:
        """
        Computes the 3-D state of the shape theShape
        toward solid theSolid.
        theTol - value of precision of computation
        theContext- cached geometrical tools
        Returns 3-D state.
        """

    @staticmethod
    def GetFaceOff(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theLCEF: nanoocp.NCollection.NCollection_List[nanoocp.BOPTools.BOPTools_CoupleOfShape], theFaceOff: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        @name Face classification relatively solid
        For the face theFace and its edge theEdge
        finds the face suitable to produce shell.
        theLCEF - set of faces to search. All faces
        from theLCEF must share edge theEdge
        """

    @overload
    @staticmethod
    def IsInternalFace(theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace1: nanoocp.TopoDS.TopoDS_Face, theFace2: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Returns True if the face theFace is inside of the
        couple of faces theFace1, theFace2.
        The faces theFace, theFace1, theFace2 must
        share the edge theEdge
        Return values:
        * 0 state is not IN
        * 1 state is IN
        * 2 state can not be found by the method of angles
        """

    @overload
    @staticmethod
    def IsInternalFace(theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge, theLF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Returns True if the face theFace is inside of the
        appropriate couple of faces (from the set theLF).
        The faces of the set theLF and theFace must share
        the edge theEdge
        * 0 state is not IN
        * 1 state is IN
        * 2 state can not be found by the method of angles
        """

    @overload
    @staticmethod
    def IsInternalFace(theFace: nanoocp.TopoDS.TopoDS_Face, theSolid: nanoocp.TopoDS.TopoDS_Solid, theMEF: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theTol: float, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        Returns True if the face theFace is inside the
        solid theSolid.
        theMEF - Map Edge/Faces for theSolid
        theTol - value of precision of computation
        theContext- cached geometrical tools
        """

    @staticmethod
    def MakePCurve(theE: nanoocp.TopoDS.TopoDS_Edge, theF1: nanoocp.TopoDS.TopoDS_Face, theF2: nanoocp.TopoDS.TopoDS_Face, theCurve: nanoocp.IntTools.IntTools_Curve, thePC1: bool, thePC2: bool, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> None:
        """
        @name PCurve construction
        Makes 2d curve of the edge <theE> on the faces <theF1> and <theF2>.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def IsHole(theW: nanoocp.TopoDS.TopoDS_Shape, theF: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        @name Wire classification relatively face
        Checks if the wire is a hole for the face.
        """

    @overload
    @staticmethod
    def IsSplitToReverse(theSplit: nanoocp.TopoDS.TopoDS_Shape, theShape: nanoocp.TopoDS.TopoDS_Shape, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        @name Choosing correct orientation for the split shape
        Checks if the direction of the split shape is opposite to
        the direction of the original shape.
        The method is an overload for (Edge,Edge) and (Face,Face) corresponding
        methods and checks only these types of shapes.
        For faces the method checks if normal directions are opposite.
        For edges the method checks if tangent vectors are opposite.

        In case the directions do not coincide, it returns TRUE, meaning
        that split shape has to be reversed to match the direction of the
        original shape.

        If requested (<theError> is not null), the method returns the status of the operation:
        - 0 - no error;
        - Error from (Edge,Edge) or (Face,Face) corresponding method
        - 100 - bad types.
        In case of any error the method always returns FALSE.

        @param[in] theSplit  Split shape
        @param[in] theShape  Original shape
        @param[in] theContext  cached geometrical tools
        @param[out] theError  Error Status of the operation
        """

    @overload
    @staticmethod
    def IsSplitToReverse(theSplit: nanoocp.TopoDS.TopoDS_Face, theShape: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        Checks if the normal direction of the split face is opposite to
        the normal direction of the original face.
        The normal directions for both faces are taken in the same point -
        point inside the split face is projected onto the original face.
        Returns TRUE if the normals do not coincide, meaning the necessity
        to revert the orientation of the split face to match the direction
        of the original face.

        If requested (<theError> is not null), the method returns the status of the operation:
        - 0 - no error;
        - 1 - unable to find the point inside split face;
        - 2 - unable to compute the normal for the split face;
        - 3 - unable to project the point inside the split face on the original face;
        - 4 - unable to compute the normal for the original face.
        In case of any error the method always returns FALSE.

        @param[in] theSplit  Split face
        @param[in] theShape  Original face
        @param[in] theContext  cached geometrical tools
        @param[out] theError  Error Status of the operation
        """

    @overload
    @staticmethod
    def IsSplitToReverse(theSplit: nanoocp.TopoDS.TopoDS_Edge, theShape: nanoocp.TopoDS.TopoDS_Edge, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        Checks if the tangent vector of the split edge is opposite to
        the tangent vector of the original edge.
        The tangent vectors for both edges are computed in the same point -
        point inside the split edge is projected onto the original edge.
        Returns TRUE if the tangent vectors do not coincide, meaning the necessity
        to revert the orientation of the split edge to match the direction
        of the original edge.

        If requested (<theError> is not null), the method returns the status of the operation:
        - 0 - no error;
        - 1 - degenerated edges are given;
        - 2 - unable to compute the tangent vector for the split edge;
        - 3 - unable to project the point inside the split edge on the original edge;
        - 4 - unable to compute the tangent vector for the original edge;
        In case of any error the method always returns FALSE.

        @param[in] theSplit  Split edge
        @param[in] theShape  Original edge
        @param[in] theContext  cached geometrical tools
        @param[out] theError  Error Status of the operation
        """

    @staticmethod
    def IsSplitToReverseWithWarn(theSplit: nanoocp.TopoDS.TopoDS_Shape, theShape: nanoocp.TopoDS.TopoDS_Shape, theContext: nanoocp.IntTools.IntTools_Context | None, theReport: nanoocp.Message.Message_Report | None = None) -> bool:
        """
        Add-on for the *IsSplitToReverse()* to check for its errors
        and in case of any add the *BOPAlgo_AlertUnableToOrientTheShape*
        warning to the report.
        """

    @staticmethod
    def Sense(theF1: nanoocp.TopoDS.TopoDS_Face, theF2: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Checks if the normals direction of the given faces computed near
        the shared edge coincide.
        Returns the status of operation:
        * 0 - in case of error (shared edge not found or directions are not collinear)
        * 1 - normal directions coincide;
        * -1 - normal directions are opposite.
        """

    @staticmethod
    def MakeConnexityBlock(theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theMapAvoid: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theLSCB: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        @name Making connexity blocks
        For the list of faces theLS build block
        theLSCB in terms of connexity by edges
        theMapAvoid - set of edges to avoid for
        the treatment
        """

    @overload
    @staticmethod
    def MakeConnexityBlocks(theS: nanoocp.TopoDS.TopoDS_Shape, theConnectionType: nanoocp.TopAbs.TopAbs_ShapeEnum, theElementType: nanoocp.TopAbs.TopAbs_ShapeEnum, theLCB: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        For the compound <theS> builds the blocks (compounds) of
        elements of type <theElementType> connected through the shapes
        of the type <theConnectionType>.
        The blocks are stored into the list <theLCB>.
        """

    @overload
    @staticmethod
    def MakeConnexityBlocks(theS: nanoocp.TopoDS.TopoDS_Shape, theConnectionType: nanoocp.TopAbs.TopAbs_ShapeEnum, theElementType: nanoocp.TopAbs.TopAbs_ShapeEnum, theLCB: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]], theConnectionMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        For the compound <theS> builds the blocks (compounds) of
        elements of type <theElementType> connected through the shapes
        of the type <theConnectionType>.
        The blocks are stored into the list of lists <theLCB>.
        Returns also the connection map <theConnectionMap>, filled during operation.
        """

    @overload
    @staticmethod
    def MakeConnexityBlocks(theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theConnectionType: nanoocp.TopAbs.TopAbs_ShapeEnum, theElementType: nanoocp.TopAbs.TopAbs_ShapeEnum, theLCB: nanoocp.NCollection.NCollection_List[nanoocp.BOPTools.BOPTools_ConnexityBlock]) -> None:
        """
        Makes connexity blocks of elements of the given type with the given type of the
        connecting elements. The blocks are checked on regularity (multi-connectivity)
        and stored to the list of blocks <theLCB>.
        """

    @staticmethod
    def OrientEdgesOnWire(theWire: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name Orienting elements in container
        Correctly orients edges on the wire
        """

    @staticmethod
    def OrientFacesOnShell(theShell: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Correctly orients faces on the shell"""

    @staticmethod
    def CorrectTolerances(theS: nanoocp.TopoDS.TopoDS_Shape, theMapToAvoid: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theTolMax: float = 0.0001, theRunParallel: bool = False) -> None:
        """
        @name Methods for shape validation (correction)
        Provides valid values of tolerances for the shape <theS>
        <theTolMax> is max value of the tolerance that can be
        accepted for correction. If real value of the tolerance
        will be greater than <aTolMax>, the correction does not
        perform.
        """

    @staticmethod
    def CorrectCurveOnSurface(theS: nanoocp.TopoDS.TopoDS_Shape, theMapToAvoid: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theTolMax: float = 0.0001, theRunParallel: bool = False) -> None:
        """
        Provides valid values of tolerances for the shape <theS>
        in terms of BRepCheck_InvalidCurveOnSurface.
        """

    @staticmethod
    def CorrectPointOnCurve(theS: nanoocp.TopoDS.TopoDS_Shape, theMapToAvoid: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theTolMax: float = 0.0001, theRunParallel: bool = False) -> None:
        """
        Provides valid values of tolerances for the shape <theS>
        in terms of BRepCheck_InvalidPointOnCurve.
        """

    @staticmethod
    def CorrectShapeTolerances(theS: nanoocp.TopoDS.TopoDS_Shape, theMapToAvoid: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theRunParallel: bool = False) -> None:
        """
        Corrects tolerance values of the sub-shapes of the shape <theS> if needed.
        """

    @staticmethod
    def AreFacesSameDomain(theF1: nanoocp.TopoDS.TopoDS_Face, theF2: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None, theFuzz: float = 1e-07) -> bool:
        """
        Checking if the faces are coinciding
        Checks if the given faces are same-domain, i.e. coincide.
        """

    @staticmethod
    def GetEdgeOff(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theEdgeOff: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        @name Looking for the edge in the face
        Returns True if the face theFace contains
        the edge theEdge but with opposite orientation.
        If the method returns True theEdgeOff is the
        edge founded
        """

    @staticmethod
    def GetEdgeOnFace(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theEdgeOnF: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        For the face theFace gets the edge theEdgeOnF
        that is the same as theEdge
        Returns True if such edge exists
        Returns False if there is no such edge
        """

    @overload
    @staticmethod
    def CorrectRange(aE1: nanoocp.TopoDS.TopoDS_Edge, aE2: nanoocp.TopoDS.TopoDS_Edge, aSR: nanoocp.IntTools.IntTools_Range, aNewSR: nanoocp.IntTools.IntTools_Range) -> None:
        """
        @name Correction of the edges range
        Correct shrunk range <aSR> taking into account 3D-curve
        resolution and corresponding tolerance values of <aE1>, <aE2>
        """

    @overload
    @staticmethod
    def CorrectRange(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aSR: nanoocp.IntTools.IntTools_Range, aNewSR: nanoocp.IntTools.IntTools_Range) -> None:
        """
        Correct shrunk range <aSR> taking into account 3D-curve
        resolution and corresponding tolerance values of <aE>, <aF>
        """

    @staticmethod
    def IsMicroEdge(theEdge: nanoocp.TopoDS.TopoDS_Edge, theContext: nanoocp.IntTools.IntTools_Context | None, theCheckSplittable: bool = True) -> bool:
        """
        @name Checking edge on micro status
        Checks if it is possible to compute shrunk range for the edge <aE>
        Flag <theCheckSplittable> defines whether to take into account
        the possibility to split the edge or not.
        """

    @staticmethod
    def IsInvertedSolid(theSolid: nanoocp.TopoDS.TopoDS_Solid) -> bool:
        """
        @name Solid classification
        Returns true if the solid <theSolid> is inverted
        """

    @staticmethod
    def ComputeTolerance(theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        @name Edge/Face Deviation computation
        Computes the necessary value of the tolerance for the edge
        """

    @staticmethod
    def MakeContainer(theType: nanoocp.TopAbs.TopAbs_ShapeEnum, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name Other methods
        Makes empty container of requested type
        """

    @staticmethod
    def PointOnEdge(aEdge: nanoocp.TopoDS.TopoDS_Edge, aPrm: float, aP: nanoocp.gp.gp_Pnt) -> None:
        """Compute a 3D-point on the edge <aEdge> at parameter <aPrm>"""

    @staticmethod
    def IsBlockInOnFace(aShR: nanoocp.IntTools.IntTools_Range, aF: nanoocp.TopoDS.TopoDS_Face, aE: nanoocp.TopoDS.TopoDS_Edge, aContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        Returns TRUE if PaveBlock <aPB> lays on the face <aF>, i.e
        the <PB> is IN or ON in 2D of <aF>
        """

    @staticmethod
    def Dimensions(theS: nanoocp.TopoDS.TopoDS_Shape) -> tuple[int, int]:
        """Returns the min and max dimensions of the shape <theS>."""

    @staticmethod
    def Dimension(theS: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Returns dimension of the shape <theS>.
        If the shape contains elements of different dimension, -1 is returned.
        """

    @staticmethod
    def TreatCompound(theS: nanoocp.TopoDS.TopoDS_Shape, theList: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theMap: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher] = None) -> None:
        """
        Collects in the output list recursively all non-compound sub-shapes of the first level
        of the given shape theS. The optional map theMap is used to avoid the duplicates in the
        output list, so it will also contain all non-compound sub-shapes.
        """

    @staticmethod
    def IsOpenShell(theShell: nanoocp.TopoDS.TopoDS_Shell) -> bool:
        """Returns true if the shell <theShell> is open"""

class BOPTools_AlgoTools2D:
    """
    The class contains handy static functions
    dealing with the topology
    This is the copy of the BOPTools_AlgoTools2D.cdl
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_AlgoTools2D) -> None: ...

    @staticmethod
    def BuildPCurveForEdgeOnFace(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> None:
        """
        Compute P-Curve for the edge <aE> on the face <aF>.
        Raises exception Standard_ConstructionError if projection algorithm fails.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def EdgeTangent(anE: nanoocp.TopoDS.TopoDS_Edge, aT: float, Tau: nanoocp.gp.gp_Vec) -> bool:
        """Compute tangent for the edge <aE> [in 3D] at parameter <aT>"""

    @staticmethod
    def PointOnSurface(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aT: float, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> tuple[float, float]:
        """
        Compute surface parameters <U,V> of the face <aF>
        for the point from the edge <aE> at parameter <aT>.
        If <aE> has't pcurve on surface, algorithm tries to get it by
        projection and can raise exception
        Standard_ConstructionError if projection algorithm fails.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def CurveOnSurface__Geom2d_Curve__float(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        CurveOnSurface__Geom2d_Curve__float: the C++ overload CurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &, double &, const occ::handle<IntTools_Context> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Get P-Curve <aC> for the edge <aE> on surface <aF>.
        If the P-Curve does not exist, build it using Make2D().
        [aToler] - reached tolerance
        Raises exception Standard_ConstructionError if algorithm Make2D() fails.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def CurveOnSurface__Geom2d_Curve__float__float__float(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]:
        """
        CurveOnSurface__Geom2d_Curve__float__float__float: the C++ overload CurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &, double &, double &, double &, const occ::handle<IntTools_Context> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Get P-Curve <aC> for the edge <aE> on surface <aF>.
        If the P-Curve does not exist, build it using Make2D().
        [aFirst, aLast] - range of the P-Curve
        [aToler] - reached tolerance
        Raises exception Standard_ConstructionError if algorithm Make2D() fails.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def HasCurveOnSurface__Geom2d_Curve__float__float__float(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float, float, float]:
        """
        HasCurveOnSurface__Geom2d_Curve__float__float__float: the C++ overload HasCurveOnSurface(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns TRUE if the edge <aE> has P-Curve <aC>
        on surface <aF>.
        [aFirst, aLast] - range of the P-Curve
        [aToler] - reached tolerance
        If the P-Curve does not exist, aC.IsNull()=TRUE.
        """

    @staticmethod
    def HasCurveOnSurface(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Returns TRUE if the edge <aE> has P-Curve <aC>
        on surface <aF>.
        If the P-Curve does not exist, aC.IsNull()=TRUE.
        """

    @overload
    @staticmethod
    def AdjustPCurveOnFace(theF: nanoocp.TopoDS.TopoDS_Face, theC3D: nanoocp.Geom.Geom_Curve | None, theC2D: nanoocp.Geom2d.Geom2d_Curve | None, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Adjust P-Curve <theC2D> (3D-curve <theC3D>) on surface of the face <theF>.
        <theContext> - storage for caching the geometrical tools
        """

    @overload
    @staticmethod
    def AdjustPCurveOnFace(theF: nanoocp.TopoDS.TopoDS_Face, theFirst: float, theLast: float, theC2D: nanoocp.Geom2d.Geom2d_Curve | None, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Adjust P-Curve <aC2D> (3D-curve <C3D>) on surface <aF>.
        [aT1, aT2] - range to adjust
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def AdjustPCurveOnSurf(aF: nanoocp.BRepAdaptor.BRepAdaptor_Surface, aT1: float, aT2: float, aC2D: nanoocp.Geom2d.Geom2d_Curve | None) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Adjust P-Curve <aC2D> (3D-curve <C3D>) on surface <aF>.
        [aT1, aT2] - range to adjust
        """

    @overload
    @staticmethod
    def IntermediatePoint(aFirst: float, aLast: float) -> float:
        """Compute intermediate value in between [aFirst, aLast]."""

    @overload
    @staticmethod
    def IntermediatePoint(anE: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """Compute intermediate value of parameter for the edge <anE>."""

    @staticmethod
    def Make2D(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float, float]:
        """
        Make P-Curve <aC> for the edge <aE> on surface <aF>.
        [aFirst, aLast] - range of the P-Curve
        [aToler] - reached tolerance
        Raises exception Standard_ConstructionError if algorithm fails.
        <theContext> - storage for caching the geometrical tools
        """

    @overload
    @staticmethod
    def MakePCurveOnFace(aF: nanoocp.TopoDS.TopoDS_Face, C3D: nanoocp.Geom.Geom_Curve | None, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Make P-Curve <aC> for the 3D-curve <C3D> on surface <aF>.
        [aToler] - reached tolerance
        Raises exception Standard_ConstructionError if projection algorithm fails.
        <theContext> - storage for caching the geometrical tools
        """

    @overload
    @staticmethod
    def MakePCurveOnFace(aF: nanoocp.TopoDS.TopoDS_Face, C3D: nanoocp.Geom.Geom_Curve | None, aT1: float, aT2: float, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Make P-Curve <aC> for the 3D-curve <C3D> on surface <aF>.
        [aT1, aT2] - range to build
        [aToler] - reached tolerance
        Raises exception Standard_ConstructionError if projection algorithm fails.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def AttachExistingPCurve(aEold: nanoocp.TopoDS.TopoDS_Edge, aEnew: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aCtx: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Attach P-Curve from the edge <aEold> on surface <aF>
        to the edge <aEnew>
        Returns 0 in case of success
        """

    @staticmethod
    def IsEdgeIsoline(theE: nanoocp.TopoDS.TopoDS_Edge, theF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]:
        """
        Checks if CurveOnSurface of theE on theF matches with isoline of theF surface.
        Sets corresponding values for isTheUIso and isTheVIso variables.

        ATTENTION!!!
        This method is based on the comparison between direction of
        surface (which theF is based on) iso-lines and the direction
        of the edge p-curve (on theF) in middle-point of the p-curve.

        This method should be used carefully
        (e.g. BRep_Tool::IsClosed(...) together) in order to avoid
        false classification some p-curves as isoline (e.g. circle on a plane).
        """

class BOPTools_AlgoTools3D:
    """
    The class contains handy static functions
    dealing with the topology
    This is the copy of BOPTools_AlgoTools3D.cdl file
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_AlgoTools3D) -> None: ...

    @overload
    @staticmethod
    def DoSplitSEAMOnFace(theESplit: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Makes the edge <theESplit> seam edge for the face <theFace> basing on the surface properties
        (U and V periods)
        """

    @overload
    @staticmethod
    def DoSplitSEAMOnFace(theEOrigin: nanoocp.TopoDS.TopoDS_Edge, theESplit: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Makes the split edge <theESplit> seam edge for the face <theFace> basing on the positions
        of 2d curves of the original edge <theEOrigin>.
        """

    @overload
    @staticmethod
    def GetNormalToFaceOnEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aT: float, aD: nanoocp.gp.gp_Dir, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> None:
        """
        Computes normal to the face <aF> for the point on the edge <aE>
        at parameter <aT>.
        <theContext> - storage for caching the geometrical tools
        """

    @overload
    @staticmethod
    def GetNormalToFaceOnEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aD: nanoocp.gp.gp_Dir, theContext: nanoocp.IntTools.IntTools_Context | None = None) -> None:
        """
        Computes normal to the face <aF> for the point on the edge <aE>
        at arbitrary intermediate parameter.
        <theContext> - storage for caching the geometrical tools
        """

    @staticmethod
    def SenseFlag(aNF1: nanoocp.gp.gp_Dir, aNF2: nanoocp.gp.gp_Dir) -> int:
        """
        Returns 1  if scalar product aNF1* aNF2>0.
        Returns 0  if directions aNF1 aNF2 coincide
        Returns -1 if scalar product aNF1* aNF2<0.
        """

    @staticmethod
    def GetNormalToSurface(aS: nanoocp.Geom.Geom_Surface | None, U: float, V: float, aD: nanoocp.gp.gp_Dir) -> bool:
        """
        Compute normal <aD> to surface <aS> in point (U,V)
        Returns TRUE if directions aD1U, aD1V coincide
        """

    @overload
    @staticmethod
    def GetApproxNormalToFaceOnEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aT: float, aPx: nanoocp.gp.gp_Pnt, aD: nanoocp.gp.gp_Dir, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        Computes normal to the face <aF> for the 3D-point that
        belongs to the edge <aE> at parameter <aT>.
        Output:
        aPx  -  the 3D-point where the normal computed
        aD   -  the normal;
        Warning:
        The normal is computed not exactly in the point on the
        edge, but in point that is near to the edge towards to
        the face material (so, we'll have approx. normal);
        The point is computed using PointNearEdge function,
        with the shifting value BOPTools_AlgoTools3D::MinStepIn2d(),
        from the edge, but if this value is too big,
        the point will be computed using Hatcher (PointInFace function).
        Returns TRUE in case of success.
        """

    @overload
    @staticmethod
    def GetApproxNormalToFaceOnEdge(theE: nanoocp.TopoDS.TopoDS_Edge, theF: nanoocp.TopoDS.TopoDS_Face, aT: float, aP: nanoocp.gp.gp_Pnt, aDNF: nanoocp.gp.gp_Dir, aDt2D: float) -> bool:
        """
        Computes normal to the face <aF> for the 3D-point that
        belongs to the edge <aE> at parameter <aT>.
        Output:
        aPx  -  the 3D-point where the normal computed
        aD   -  the normal;
        Warning:
        The normal is computed not exactly in the point on the
        edge, but in point that is near to the edge towards to
        the face material (so, we'll have approx. normal);
        The point is computed using PointNearEdge function
        with the shifting value <aDt2D> from the edge;
        No checks on this value will be done.
        Returns TRUE in case of success.
        """

    @overload
    @staticmethod
    def GetApproxNormalToFaceOnEdge(theE: nanoocp.TopoDS.TopoDS_Edge, theF: nanoocp.TopoDS.TopoDS_Face, aT: float, aDt2D: float, aP: nanoocp.gp.gp_Pnt, aDNF: nanoocp.gp.gp_Dir, theContext: nanoocp.IntTools.IntTools_Context | None) -> bool:
        """
        Computes normal to the face <aF> for the 3D-point that
        belongs to the edge <aE> at parameter <aT>.
        Output:
        aPx  -  the 3D-point where the normal computed
        aD   -  the normal;
        Warning:
        The normal is computed not exactly in the point on the
        edge, but in point that is near to the edge towards to
        the face material (so, we'll have approx. normal);
        The point is computed using PointNearEdge function
        with the shifting value <aDt2D> from the edge,
        but if this value is too big the point will be
        computed using Hatcher (PointInFace function).
        Returns TRUE in case of success.
        """

    @overload
    @staticmethod
    def PointNearEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aT: float, aDt2D: float, aP2D: nanoocp.gp.gp_Pnt2d, aPx: nanoocp.gp.gp_Pnt, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Compute the point <aPx>, (<aP2D>) that is near to
        the edge <aE> at parameter <aT> towards to the
        material of the face <aF>. The value of shifting in
        2D is <aDt2D>
        If the value of shifting is too big the point
        will be computed using Hatcher (PointInFace function).
        Returns error status:
        0 - in case of success;
        1 - <aE> does not have 2d curve on the face <aF>;
        2 - the computed point is out of the face.
        """

    @overload
    @staticmethod
    def PointNearEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aT: float, aDt2D: float, aP2D: nanoocp.gp.gp_Pnt2d, aPx: nanoocp.gp.gp_Pnt) -> int:
        """
        Compute the point <aPx>, (<aP2D>) that is near to
        the edge <aE> at parameter <aT> towards to the
        material of the face <aF>. The value of shifting in
        2D is <aDt2D>. No checks on this value will be done.
        Returns error status:
        0 - in case of success;
        1 - <aE> does not have 2d curve on the face <aF>.
        """

    @overload
    @staticmethod
    def PointNearEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aT: float, aP2D: nanoocp.gp.gp_Pnt2d, aPx: nanoocp.gp.gp_Pnt, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Computes the point <aPx>, (<aP2D>) that is near to
        the edge <aE> at parameter <aT> towards to the
        material of the face <aF>. The value of shifting in
        2D is dt2D=BOPTools_AlgoTools3D::MinStepIn2d()
        If the value of shifting is too big the point will be computed
        using Hatcher (PointInFace function).
        Returns error status:
        0 - in case of success;
        1 - <aE> does not have 2d curve on the face <aF>;
        2 - the computed point is out of the face.
        """

    @overload
    @staticmethod
    def PointNearEdge(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aP2D: nanoocp.gp.gp_Pnt2d, aPx: nanoocp.gp.gp_Pnt, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Compute the point <aPx>, (<aP2D>) that is near to
        the edge <aE> at arbitrary parameter towards to the
        material of the face <aF>. The value of shifting in
        2D is dt2D=BOPTools_AlgoTools3D::MinStepIn2d().
        If the value of shifting is too big the point will be computed
        using Hatcher (PointInFace function).
        Returns error status:
        0 - in case of success;
        1 - <aE> does not have 2d curve on the face <aF>;
        2 - the computed point is out of the face.
        """

    @staticmethod
    def MinStepIn2d() -> float:
        """
        Returns simple step value that is used in 2D-computations
        = 1.e-5
        """

    @staticmethod
    def IsEmptyShape(aS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns TRUE if the shape <aS> does not contain
        geometry information (e.g. empty compound)
        """

    @staticmethod
    def OrientEdgeOnFace(aE: nanoocp.TopoDS.TopoDS_Edge, aF: nanoocp.TopoDS.TopoDS_Face, aER: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Get the edge <aER> from the face <aF> that is the same as
        the edge <aE>
        """

    @overload
    @staticmethod
    def PointInFace(theF: nanoocp.TopoDS.TopoDS_Face, theP: nanoocp.gp.gp_Pnt, theP2D: nanoocp.gp.gp_Pnt2d, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Computes arbitrary point <theP> inside the face <theF>.
        <theP2D> - 2D representation of <theP>
        on the surface of <theF>
        Returns 0 in case of success.
        """

    @overload
    @staticmethod
    def PointInFace(theF: nanoocp.TopoDS.TopoDS_Face, theE: nanoocp.TopoDS.TopoDS_Edge, theT: float, theDt2D: float, theP: nanoocp.gp.gp_Pnt, theP2D: nanoocp.gp.gp_Pnt2d, theContext: nanoocp.IntTools.IntTools_Context | None) -> int:
        """
        Computes a point <theP> inside the face <theF>
        using starting point taken by the parameter <theT>
        from the 2d curve of the edge <theE> on the face <theF>
        in the direction perpendicular to the tangent vector
        of the 2d curve of the edge.
        The point will be distanced on <theDt2D> from the 2d curve.
        <theP2D> - 2D representation of <theP>
        on the surface of <theF>
        Returns 0 in case of success.
        """

    @overload
    @staticmethod
    def PointInFace(theF: nanoocp.TopoDS.TopoDS_Face, theL: nanoocp.Geom2d.Geom2d_Curve | None, theP: nanoocp.gp.gp_Pnt, theP2D: nanoocp.gp.gp_Pnt2d, theContext: nanoocp.IntTools.IntTools_Context | None, theDt2D: float = 0.0) -> int:
        """
        Computes a point <theP> inside the face <theF>
        using the line <theL> so that 2D point
        <theP2D>, 2D representation of <theP>
        on the surface of <theF>, lies on that line.
        Returns 0 in case of success.
        """

class BOPTools_Parallel:
    """Implementation of Functors/Starters"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_Parallel) -> None: ...

class BOPTools_Set:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPTools_Set) -> None:
        """Copy constructor."""

    def Assign(self, Other: BOPTools_Set) -> BOPTools_Set: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Add(self, theS: nanoocp.TopoDS.TopoDS_Shape, theType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None: ...

    def NbShapes(self) -> int: ...

    def IsEqual(self, aOther: BOPTools_Set) -> bool: ...

    def __eq__(self, theOther: BOPTools_Set) -> bool: ...

    def GetSum(self) -> int: ...

    def __hash__(self) -> int: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BOPTools
import nanoocp.TopTools
BOPTools_ListOfConnexityBlock = nanoocp.NCollection.NCollection_List[nanoocp.BOPTools.BOPTools_ConnexityBlock]
BOPTools_ListOfCoupleOfShape = nanoocp.NCollection.NCollection_List[nanoocp.BOPTools.BOPTools_CoupleOfShape]
