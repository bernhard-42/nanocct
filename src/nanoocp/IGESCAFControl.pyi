"""OCCT package IGESCAFControl (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESControl
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.TDocStd
import nanoocp.XSControl


class IGESCAFControl:
    """
    Provides high-level API to translate IGES file
    to and from DECAF document
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESCAFControl) -> None: ...

    @staticmethod
    def DecodeColor(col: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Provides a tool for writing IGES file
        Converts IGES color index to CASCADE color
        """

    @staticmethod
    def EncodeColor(col: nanoocp.Quantity.Quantity_Color) -> int:
        """
        Tries to Convert CASCADE color to IGES color index
        If no corresponding color defined in IGES, returns 0
        """

class IGESCAFControl_Reader(nanoocp.IGESControl.IGESControl_Reader):
    """
    Provides a tool to read IGES file and put it into
    DECAF document. Besides transfer of shapes (including
    assemblies) provided by IGESControl, supports also
    colors and part names
    IGESCAFControl_Reader reader; Methods for translation of an IGES file:
    reader.ReadFile("filename");
    reader.Transfer(Document); or
    reader.Perform("filename",doc);
    Methods for managing reading attributes.
    Colors
    reader.SetColorMode(colormode);
    bool colormode = reader.GetColorMode();
    Layers
    reader.SetLayerMode(layermode);
    bool layermode = reader.GetLayerMode();
    Names
    reader.SetNameMode(namemode);
    bool namemode = reader.GetNameMode();
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a reader with an empty
        IGES model and sets ColorMode, LayerMode and NameMode to true.
        """

    @overload
    def __init__(self, theWS: nanoocp.XSControl.XSControl_WorkSession | None, FromScratch: bool = True) -> None:
        """
        Creates a reader tool and attaches it to an already existing Session
        Clears the session if it was not yet set for IGES
        """

    @overload
    def __init__(self, theOther: IGESCAFControl_Reader) -> None: ...

    def Transfer(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates currently loaded IGES file into the document
        Returns True if succeeded, and False in case of fail
        """

    @overload
    def Perform(self, theFileName: nanoocp.TCollection.TCollection_AsciiString, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Perform(self, theFileName: str, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translate IGES file given by filename into the document
        Return True if succeeded, and False in case of fail
        """

    def SetColorMode(self, theMode: bool) -> None:
        """Set ColorMode for indicate read Colors or not."""

    def GetColorMode(self) -> bool: ...

    def SetNameMode(self, theMode: bool) -> None:
        """Set NameMode for indicate read Name or not."""

    def GetNameMode(self) -> bool: ...

    def SetLayerMode(self, theMode: bool) -> None:
        """Set LayerMode for indicate read Layers or not."""

    def GetLayerMode(self) -> bool: ...

class IGESCAFControl_Writer(nanoocp.IGESControl.IGESControl_Writer):
    """
    Provides a tool to write DECAF document to the
    IGES file. Besides transfer of shapes (including
    assemblies) provided by IGESControl, supports also
    colors and part names
    IGESCAFControl_Writer writer();
    Methods for writing IGES file:
    writer.Transfer (Document);
    writer.Write("filename") or writer.Write(OStream) or
    writer.Perform(Document,"filename");
    Methods for managing the writing of attributes.
    Colors
    writer.SetColorMode(colormode);
    bool colormode = writer.GetColorMode();
    Layers
    writer.SetLayerMode(layermode);
    bool layermode = writer.GetLayerMode();
    Names
    writer.SetNameMode(namemode);
    bool namemode = writer.GetNameMode();
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a writer with an empty
        IGES model and sets ColorMode, LayerMode and NameMode to true.
        """

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Creates a reader tool and attaches it to an already existing Session
        Clears the session if it was not yet set for IGES
        """

    @overload
    def __init__(self, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theUnit: str) -> None:
        """
        Creates a reader tool and attaches it to an already existing Session
        Clears the session if it was not yet set for IGES
        Sets target Unit for the writing process.
        """

    @overload
    def __init__(self, theOther: IGESCAFControl_Writer) -> None: ...

    @overload
    def Transfer(self, doc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a document to a IGES model
        Returns True if translation is OK
        """

    @overload
    def Transfer(self, labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers labels to a IGES model
        Returns True if translation is OK
        """

    @overload
    def Transfer(self, label: nanoocp.TDF.TDF_Label, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers label to a IGES model
        Returns True if translation is OK
        """

    @overload
    def Perform(self, doc: nanoocp.TDocStd.TDocStd_Document | None, filename: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Perform(self, doc: nanoocp.TDocStd.TDocStd_Document | None, filename: str, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a document and writes it to a IGES file
        Returns True if translation is OK
        """

    def SetColorMode(self, colormode: bool) -> None:
        """Set ColorMode for indicate write Colors or not."""

    def GetColorMode(self) -> bool: ...

    def SetNameMode(self, namemode: bool) -> None:
        """Set NameMode for indicate write Name or not."""

    def GetNameMode(self) -> bool: ...

    def SetLayerMode(self, layermode: bool) -> None:
        """Set LayerMode for indicate write Layers or not."""

    def GetLayerMode(self) -> bool: ...
