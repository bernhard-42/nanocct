"""OCCT package XCAFPrs (toolkit TKXCAF)"""

from typing import overload

import nanoocp.AIS
import nanoocp.Graphic3d
import nanoocp.Image
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.TDocStd
import nanoocp.TPrsStd
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.XCAFDoc


XCAFPrs_DocumentExplorerFlags_None: int = 0

XCAFPrs_DocumentExplorerFlags_OnlyLeafNodes: int = 1

XCAFPrs_DocumentExplorerFlags_NoStyle: int = 2

class XCAFPrs_Style:
    """Represents a set of styling settings applicable to a (sub)shape"""

    @overload
    def __init__(self) -> None:
        """Empty constructor - colors are unset, visibility is TRUE."""

    @overload
    def __init__(self, theOther: XCAFPrs_Style) -> None: ...

    def IsEmpty(self) -> bool:
        """Return TRUE if style is empty - does not override any properties."""

    def Material(self) -> nanoocp.XCAFDoc.XCAFDoc_VisMaterial:
        """Return material."""

    def SetMaterial(self, theMaterial: nanoocp.XCAFDoc.XCAFDoc_VisMaterial | None) -> None:
        """Set material."""

    def IsSetColorSurf(self) -> bool:
        """Return TRUE if surface color has been defined."""

    def GetColorSurf(self) -> nanoocp.Quantity.Quantity_Color:
        """Return surface color."""

    @overload
    def SetColorSurf(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetColorSurf(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Set surface color."""

    def GetColorSurfRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return surface color."""

    def UnSetColorSurf(self) -> None:
        """Manage surface color setting"""

    def IsSetColorCurv(self) -> bool:
        """Return TRUE if curve color has been defined."""

    def GetColorCurv(self) -> nanoocp.Quantity.Quantity_Color:
        """Return curve color."""

    def SetColorCurv(self, col: nanoocp.Quantity.Quantity_Color) -> None:
        """Set curve color."""

    def UnSetColorCurv(self) -> None:
        """Manage curve color setting"""

    def SetVisibility(self, theVisibility: bool) -> None:
        """Assign visibility."""

    def IsVisible(self) -> bool:
        """Manage visibility."""

    def BaseColorTexture(self) -> nanoocp.Image.Image_Texture:
        """Return base color texture."""

    def IsEqual(self, theOther: XCAFPrs_Style) -> bool:
        """
        Returns True if styles are the same
        Methods for using Style as key in maps
        """

    def __eq__(self, theOther: XCAFPrs_Style) -> bool:
        """Returns True if styles are the same."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __hash__(self) -> int: ...

class XCAFPrs:
    """
    Presentation (visualiation, selection etc.) tools for
    DECAF documents
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFPrs) -> None: ...

    @staticmethod
    def CollectStyleSettings(L: nanoocp.TDF.TDF_Label, loc: nanoocp.TopLoc.TopLoc_Location, settings: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.XCAFPrs.XCAFPrs_Style, nanoocp.TopTools.TopTools_ShapeMapHasher], theLayerColor: nanoocp.Quantity.Quantity_ColorRGBA = ...) -> None:
        """
        Collect styles defined for shape on label L
        and its components and subshapes and fills a map of
        shape - style correspondence
        The location <loc> is for internal use, it
        should be Null location for external call
        """

    @staticmethod
    def SetViewNameMode(viewNameMode: bool) -> None:
        """Set ViewNameMode for indicate display names or not."""

    @staticmethod
    def GetViewNameMode() -> bool: ...

class XCAFPrs_AISObject(nanoocp.AIS.AIS_ColoredShape):
    """
    Implements AIS_InteractiveObject functionality for shape in DECAF document.
    """

    @overload
    def __init__(self, theLabel: nanoocp.TDF.TDF_Label) -> None:
        """Creates an object to visualise the shape label."""

    @overload
    def __init__(self, theOther: XCAFPrs_AISObject) -> None: ...

    def GetLabel(self) -> nanoocp.TDF.TDF_Label:
        """Returns the label which was visualised by this presentation"""

    def SetLabel(self, theLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        Assign the label to this presentation
        (but does not mark it outdated with SetToUpdate()).
        """

    def DispatchStyles(self, theToSyncStyles: bool = False) -> None:
        """
        Fetch the Shape from associated Label and fill the map of sub-shapes styles.
        By default, this method is called implicitly within first ::Compute().
        Application might call this method explicitly to manipulate styles afterwards.
        @param theToSyncStyles flag indicating if method ::Compute() should call this method again
        on first compute or re-compute
        """

    def SetMaterial(self, theMaterial: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """
        Sets the material aspect.
        This method assigns the new default material without overriding XDE styles.
        Re-computation of existing presentation is not required after calling this method.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFPrs_DocumentNode:
    """Structure defining document node."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFPrs_DocumentNode) -> None: ...

    def __eq__(self, theOther: XCAFPrs_DocumentNode) -> bool: ...

    def __hash__(self) -> int: ...

    @property
    def Id(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """string identifier"""

    @Id.setter
    def Id(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def Label(self) -> nanoocp.TDF.TDF_Label:
        """label in the document"""

    @Label.setter
    def Label(self, arg: nanoocp.TDF.TDF_Label, /) -> None: ...

    @property
    def RefLabel(self) -> nanoocp.TDF.TDF_Label:
        """reference label in the document"""

    @RefLabel.setter
    def RefLabel(self, arg: nanoocp.TDF.TDF_Label, /) -> None: ...

    @property
    def Style(self) -> XCAFPrs_Style:
        """node style"""

    @Style.setter
    def Style(self, arg: XCAFPrs_Style, /) -> None: ...

    @property
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location:
        """node global transformation"""

    @Location.setter
    def Location(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def LocalTrsf(self) -> nanoocp.TopLoc.TopLoc_Location:
        """node transformation relative to parent"""

    @LocalTrsf.setter
    def LocalTrsf(self, arg: nanoocp.TopLoc.TopLoc_Location, /) -> None: ...

    @property
    def ChildIter(self) -> nanoocp.TDF.TDF_ChildIterator:
        """child iterator"""

    @ChildIter.setter
    def ChildIter(self, arg: nanoocp.TDF.TDF_ChildIterator, /) -> None: ...

    @property
    def IsAssembly(self) -> bool:
        """flag indicating that this label is assembly"""

    @IsAssembly.setter
    def IsAssembly(self, arg: bool, /) -> None: ...

class XCAFPrs_DocumentExplorer:
    """Document iterator through shape nodes."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theFlags: int, theDefStyle: XCAFPrs_Style = ...) -> None:
        """
        Constructor for exploring the whole document.
        @param theDocument document to explore
        @param theFlags    iteration flags
        @param theDefStyle default style for nodes with undefined style
        """

    @overload
    def __init__(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theRoots: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theFlags: int, theDefStyle: XCAFPrs_Style = ...) -> None:
        """
        Constructor for exploring specified list of root shapes in the document.
        @param theDocument  document to explore
        @param theRoots     root labels to explore within specified document
        @param theFlags     iteration flags
        @param theDefStyle  default style for nodes with undefined style
        """

    @overload
    def __init__(self, theOther: XCAFPrs_DocumentExplorer) -> None: ...

    def __iter__(self) -> XCAFPrs_DocumentExplorer:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> XCAFPrs_DocumentNode:
        """Python addition: see __iter__."""

    @staticmethod
    def DefineChildId(theLabel: nanoocp.TDF.TDF_Label, theParentId: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        @name string identification tools
        Construct a unique string identifier for the given label.
        The identifier is a concatenation of label entries (TDF_Tool::Entry() with tailing '.') of
        hierarchy from parent to child joined via '/' and looking like this:
        @code
        0:1:1:1./0:1:1:1:9./0:1:1:5:7.
        @endcode
        This generation scheme also allows finding originating labels using TDF_Tool::Label().
        The tailing dot simplifies parent equality check.
        @param theLabel child label to define id
        @param theParentId parent string identifier defined by this method
        """

    @overload
    @staticmethod
    def FindLabelFromPathId(theDocument: nanoocp.TDocStd.TDocStd_Document | None, theId: nanoocp.TCollection.TCollection_AsciiString, theParentLocation: nanoocp.TopLoc.TopLoc_Location, theLocation: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.TDF.TDF_Label: ...

    @overload
    @staticmethod
    def FindLabelFromPathId(theDocument: nanoocp.TDocStd.TDocStd_Document | None, theId: nanoocp.TCollection.TCollection_AsciiString, theLocation: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.TDF.TDF_Label:
        """
        Find a shape entity based on a text identifier constructed from OCAF labels defining full
        path.
        @sa DefineChildId()
        """

    @staticmethod
    def FindShapeFromPathId(theDocument: nanoocp.TDocStd.TDocStd_Document | None, theId: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Find a shape entity based on a text identifier constructed from OCAF labels defining full
        path.
        @sa DefineChildId()
        """

    @overload
    def Init(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theRoot: nanoocp.TDF.TDF_Label, theFlags: int, theDefStyle: XCAFPrs_Style = ...) -> None:
        """
        Initialize the iterator from a single root shape in the document.
        @param theDocument  document to explore
        @param theRoot      single root label to explore within specified document
        @param theFlags     iteration flags
        @param theDefStyle  default style for nodes with undefined style
        """

    @overload
    def Init(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theRoots: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theFlags: int, theDefStyle: XCAFPrs_Style = ...) -> None:
        """
        Initialize the iterator from the list of root shapes in the document.
        @param theDocument  document to explore
        @param theRoots     root labels to explore within specified document
        @param theFlags     iteration flags
        @param theDefStyle  default style for nodes with undefined style
        """

    def More(self) -> bool:
        """Return TRUE if iterator points to the valid node."""

    @overload
    def Current(self) -> XCAFPrs_DocumentNode:
        """Return current position."""

    @overload
    def Current(self, theDepth: int) -> XCAFPrs_DocumentNode:
        """Return current position within specified assembly depth."""

    def ChangeCurrent(self) -> XCAFPrs_DocumentNode:
        """Return current position."""

    def CurrentDepth(self) -> int:
        """
        Return depth of the current node in hierarchy, starting from 0.
        Zero means Root label.
        """

    def Next(self) -> None:
        """Go to the next node."""

    def ColorTool(self) -> nanoocp.XCAFDoc.XCAFDoc_ColorTool:
        """Return color tool."""

    def VisMaterialTool(self) -> nanoocp.XCAFDoc.XCAFDoc_VisMaterialTool:
        """Return material tool."""

class XCAFPrs_DocumentIdIterator:
    """Auxiliary tool for iterating through Path identification string."""

    @overload
    def __init__(self, thePath: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: XCAFPrs_DocumentIdIterator) -> None: ...

    def __iter__(self) -> XCAFPrs_DocumentIdIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """Return TRUE if iterator points to a value."""

    def Value(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return current value."""

    def Next(self) -> None:
        """Find the next value."""

class XCAFPrs_Driver(nanoocp.TPrsStd.TPrsStd_Driver):
    """
    Implements a driver for presentation of shapes in DECAF
    document. Its the only purpose is to initialize and return
    XCAFPrs_AISObject object on request
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFPrs_Driver) -> None: ...

    def Update(self, L: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """returns GUID of the driver"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFPrs_Texture(nanoocp.Graphic3d.Graphic3d_Texture2D):
    """Texture holder."""

    @overload
    def __init__(self, theImageSource: nanoocp.Image.Image_Texture | None, theUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: XCAFPrs_Texture) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetCompressedImage(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_CompressedPixMap:
        """Image reader."""

    def GetImage(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """Image reader."""

    def GetImageSource(self) -> nanoocp.Image.Image_Texture:
        """Return image source."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopTools
import nanoocp.XCAFPrs
XCAFPrs_IndexedDataMapOfShapeStyle = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.XCAFPrs.XCAFPrs_Style, nanoocp.TopTools.TopTools_ShapeMapHasher]
