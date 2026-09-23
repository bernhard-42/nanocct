"""OCCT package VrmlAPI (toolkit TKDEVRML)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.RWMesh
import nanoocp.Standard
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.Vrml
import nanoocp.VrmlConverter
import nanoocp.Quantity


class VrmlAPI_RepresentationOfShape(enum.IntEnum):
    """
    Identifies the representation of the shape written
    to a VRML file. The available options are :
    -      VrmlAPI_ShadedRepresentation :
    the shape is translated with a shaded representation.
    -      VrmlAPI_WireFrameRepresentation :
    the shape is translated with a wireframe representation.
    -      VrmlAPI_BothRepresentation : the shape is translated
    to VRML format with both representations : shaded and
    wireframe. This is the default option.
    """

    VrmlAPI_ShadedRepresentation = 0

    VrmlAPI_WireFrameRepresentation = 1

    VrmlAPI_BothRepresentation = 2

VrmlAPI_ShadedRepresentation: VrmlAPI_RepresentationOfShape = ...

VrmlAPI_WireFrameRepresentation: VrmlAPI_RepresentationOfShape = ...

VrmlAPI_BothRepresentation: VrmlAPI_RepresentationOfShape = ...

class VrmlAPI:
    """API for writing to VRML 1.0"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlAPI) -> None: ...

    @staticmethod
    def Write(aShape: nanoocp.TopoDS.TopoDS_Shape, aFileName: str, aVersion: int = 2) -> bool:
        """
        With help of this class user can change parameters of writing.
        Converts the shape aShape to VRML format of the passed version and writes it
        to the file identified by aFileName using default parameters.
        """

class VrmlAPI_CafReader(nanoocp.RWMesh.RWMesh_CafReader):
    """The Vrml mesh reader into XDE document."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlAPI_CafReader) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlAPI_Writer:
    """
    Creates and writes VRML files from Open
    CASCADE shapes. A VRML file can be written to
    an existing VRML file or to a new one.
    """

    @overload
    def __init__(self) -> None:
        """Creates a writer object with default parameters."""

    @overload
    def __init__(self, theOther: VrmlAPI_Writer) -> None: ...

    def ResetToDefaults(self) -> None:
        """
        Resets all parameters (representation, deflection)
        to their default values..
        """

    def Drawer(self) -> nanoocp.VrmlConverter.VrmlConverter_Drawer:
        """Returns drawer object"""

    def SetDeflection(self, aDef: float) -> None:
        """
        Sets the deflection aDef of
        the mesh algorithm which is used to compute the shaded
        representation of the translated shape. The default
        value is -1. When the deflection value is less than
        0, the deflection is calculated from the relative
        size of the shaped.
        """

    def SetRepresentation(self, aRep: VrmlAPI_RepresentationOfShape) -> None:
        """
        Sets the representation of the
        shape aRep which is written to the VRML file. The three options are :
        -      shaded
        -      wireframe
        -      both shaded and wireframe (default)
        defined through the VrmlAPI_RepresentationOfShape enumeration.
        """

    def GetRepresentation(self) -> VrmlAPI_RepresentationOfShape:
        """
        Returns the representation of the shape which is
        written to the VRML file. Types of representation are set through the
        VrmlAPI_RepresentationOfShape enumeration.
        """

    def SetTransparencyToMaterial(self, aTransparency: float) -> nanoocp.Vrml.Vrml_Material:
        """
        Deprecated in OCCT: Call Vrml_Material::SetTransparency() directly instead

        @deprecated Call Vrml_Material::SetTransparency() directly instead.
        """

    def SetShininessToMaterial(self, aShininess: float) -> nanoocp.Vrml.Vrml_Material:
        """
        Deprecated in OCCT: Call Vrml_Material::SetShininess() directly instead

        @deprecated Call Vrml_Material::SetShininess() directly instead.
        """

    def SetAmbientColorToMaterial(self, Color: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> nanoocp.Vrml.Vrml_Material:
        """
        Deprecated in OCCT: Call Vrml_Material::SetAmbientColor() directly instead

        @deprecated Call Vrml_Material::SetAmbientColor() directly instead.
        """

    def SetDiffuseColorToMaterial(self, Color: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> nanoocp.Vrml.Vrml_Material:
        """
        Deprecated in OCCT: Call Vrml_Material::SetDiffuseColor() directly instead

        @deprecated Call Vrml_Material::SetDiffuseColor() directly instead.
        """

    def SetSpecularColorToMaterial(self, Color: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> nanoocp.Vrml.Vrml_Material:
        """
        Deprecated in OCCT: Call Vrml_Material::SetSpecularColor() directly instead

        @deprecated Call Vrml_Material::SetSpecularColor() directly instead.
        """

    def SetEmissiveColorToMaterial(self, Color: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> nanoocp.Vrml.Vrml_Material:
        """
        Deprecated in OCCT: Call Vrml_Material::SetEmissiveColor() directly instead

        @deprecated Call Vrml_Material::SetEmissiveColor() directly instead.
        """

    def GetFrontMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetPointsMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetUisoMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetVisoMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetLineMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetWireMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetFreeBoundsMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def GetUnfreeBoundsMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    @overload
    def Write(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aFile: str, aVersion: int = 2) -> bool:
        """
        Converts the shape aShape to
        VRML format of the passed version and writes it to the file identified by aFile.
        """

    @overload
    def Write(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aVersion: int = 2) -> tuple[bool, str]:
        """
        Converts the shape aShape to
        VRML format of the passed version and writes it to the given stream.
        """

    @overload
    def WriteDoc(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theFile: str, theScale: float) -> bool:
        """
        Converts the document to VRML format of the passed version
        and writes it to the file identified by aFile.
        """

    @overload
    def WriteDoc(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theScale: float) -> tuple[bool, str]:
        """
        Converts the document to VRML format of the passed version
        and writes it to the given stream.
        """
