"""OCCT package RWPly (toolkit TKDEPLY)"""

from typing import overload

import nanoocp.BVH
import nanoocp.Graphic3d
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.RWMesh
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.XCAFPrs
import nanoocp.gp
import nanoocp.TDF


class RWPly_CafWriter(nanoocp.Standard.Standard_Transient):
    """PLY writer context from XCAF document."""

    @overload
    def __init__(self, theFile: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Main constructor.
        @param[in] theFile path to output PLY file
        """

    @overload
    def __init__(self, theOther: RWPly_CafWriter) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from OCCT to PLY coordinate system."""

    def ChangeCoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from OCCT to PLY coordinate system."""

    def SetCoordinateSystemConverter(self, theConverter: nanoocp.RWMesh.RWMesh_CoordinateSystemConverter) -> None:
        """Set transformation from OCCT to PLY coordinate system."""

    def DefaultStyle(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """
        Return default material definition to be used for nodes with only color defined.
        """

    def SetDefaultStyle(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> None:
        """
        Set default material definition to be used for nodes with only color defined.
        """

    def IsDoublePrecision(self) -> bool:
        """
        Return TRUE if vertex position should be stored with double floating point precision; FALSE by
        default.
        """

    def SetDoublePrecision(self, theDoublePrec: bool) -> None:
        """
        Set if vertex position should be stored with double floating point precision.
        """

    def HasNormals(self) -> bool:
        """Return TRUE if normals should be written; TRUE by default."""

    def SetNormals(self, theHasNormals: bool) -> None:
        """Set if normals are defined."""

    def HasTexCoords(self) -> bool:
        """
        Return TRUE if UV / texture coordinates should be written; FALSE by default.
        """

    def SetTexCoords(self, theHasTexCoords: bool) -> None:
        """Set if UV / texture coordinates should be written."""

    def HasColors(self) -> bool:
        """Return TRUE if point colors should be written; TRUE by default."""

    def SetColors(self, theToWrite: bool) -> None:
        """Set if point colors should be written."""

    def HasPartId(self) -> bool:
        """
        Return TRUE if part Id should be written as element attribute; TRUE by default.
        """

    def SetPartId(self, theSurfId: bool) -> None:
        """
        Set if part Id should be written as element attribute; FALSE by default.
        Cannot be combined with HasFaceId().
        """

    def HasFaceId(self) -> bool:
        """
        Return TRUE if face Id should be written as element attribute; FALSE by default.
        """

    def SetFaceId(self, theSurfId: bool) -> None:
        """
        Set if face Id should be written as element attribute; FALSE by default.
        Cannot be combined with HasPartId().
        """

    @overload
    def Perform(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theRootLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theLabelFilter: nanoocp.NCollection.NCollection_Map[nanoocp.TCollection.TCollection_AsciiString], theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Write PLY file and associated MTL material file.
        Triangulation data should be precomputed within shapes!
        @param[in] theDocument    input document
        @param[in] theRootLabels  list of root shapes to export
        @param[in] theLabelFilter optional filter with document nodes to export,
        with keys defined by XCAFPrs_DocumentExplorer::DefineChildId() and
        filled recursively (leaves and parent assembly nodes at all levels);
        when not NULL, all nodes not included into the map will be ignored
        @param[in] theFileInfo    map with file metadata to put into PLY header section
        @param[in] theProgress    optional progress indicator
        @return FALSE on file writing failure
        """

    @overload
    def Perform(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Write PLY file and associated MTL material file.
        Triangulation data should be precomputed within shapes!
        @param[in] theDocument input document
        @param[in] theFileInfo map with file metadata to put into PLY header section
        @param[in] theProgress optional progress indicator
        @return FALSE on file writing failure
        """

class RWPly_PlyWriterContext:
    """Auxiliary low-level tool writing PLY file."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: RWPly_PlyWriterContext) -> None: ...

    def IsDoublePrecision(self) -> bool:
        """
        @name vertex attributes parameters
        Return TRUE if vertex position should be stored with double floating point precision; FALSE by
        default.
        """

    def SetDoublePrecision(self, theDoublePrec: bool) -> None:
        """
        Set if vertex position should be stored with double floating point precision.
        """

    def HasNormals(self) -> bool:
        """
        Return TRUE if normals should be written as vertex attribute; FALSE by default.
        """

    def SetNormals(self, theHasNormals: bool) -> None:
        """Set if normals should be written."""

    def HasTexCoords(self) -> bool:
        """
        Return TRUE if UV / texture coordinates should be written as vertex attribute; FALSE by
        default.
        """

    def SetTexCoords(self, theHasTexCoords: bool) -> None:
        """Set if UV / texture coordinates should be written."""

    def HasColors(self) -> bool:
        """
        Return TRUE if point colors should be written as vertex attribute; FALSE by default.
        """

    def SetColors(self, theToWrite: bool) -> None:
        """Set if point colors should be written."""

    def HasSurfaceId(self) -> bool:
        """
        @name element attributes parameters
        Return TRUE if surface Id should be written as element attribute; FALSE by default.
        """

    @overload
    def SetSurfaceId(self, theSurfId: bool) -> None:
        """
        Set if surface Id should be written as element attribute; FALSE by default.
        """

    @overload
    def SetSurfaceId(self, theSurfId: int) -> None:
        """Set surface id to write with element."""

    def IsOpened(self) -> bool:
        """
        @name writing into file
        Return TRUE if file has been opened.
        """

    def Open(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Open file for writing."""

    def WriteHeader(self, theNbNodes: int, theNbElems: int, theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> bool:
        """
        Write the header.
        @param[in] theNbNodes number of vertex nodes
        @param[in] theNbElems number of mesh elements
        @param[in] theFileInfo optional comments
        """

    def WriteVertex(self, thePoint: nanoocp.gp.gp_Pnt, theNorm: nanoocp.Quantity.NCollection_Vec3__float, theUV: nanoocp.Poly.NCollection_Vec2__float, theColor: nanoocp.Graphic3d.NCollection_Vec4__unsigned_char) -> bool:
        """
        Write single point with all attributes.
        @param[in] thePoint 3D point coordinates
        @param[in] theNorm  surface normal direction at the point
        @param[in] theUV    surface/texture UV coordinates
        @param[in] theColor RGB color values
        """

    def NbWrittenVertices(self) -> int:
        """Return number of written vertices."""

    def VertexOffset(self) -> int:
        """Return vertex offset to be applied to element indices; 0 by default."""

    def SetVertexOffset(self, theOffset: int) -> None:
        """Set vertex offset to be applied to element indices."""

    def SurfaceId(self) -> int:
        """Return surface id to write with element; 0 by default."""

    def WriteTriangle(self, theTri: nanoocp.BVH.BVH_Vec3i) -> bool:
        """Writing a triangle."""

    def WriteQuad(self, theQuad: nanoocp.BVH.BVH_Vec4i) -> bool:
        """Writing a quad."""

    def NbWrittenElements(self) -> int:
        """Return number of written elements."""

    def Close(self, theIsAborted: bool = False) -> bool:
        """
        Correctly close the file.
        @return FALSE in case of writing error
        """
