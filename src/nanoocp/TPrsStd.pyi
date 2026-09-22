"""OCCT package TPrsStd (toolkit TKVCAF)"""

from typing import overload

import nanoocp.AIS
import nanoocp.Graphic3d
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.TDataXtd
import nanoocp.V3d


class TPrsStd_AISPresentation(nanoocp.TDF.TDF_Attribute):
    """
    An attribute to associate an
    AIS_InteractiveObject to a label in an AIS viewer.
    This attribute works in collaboration with TPrsStd_AISViewer.
    Note that all the Set... and Unset... attribute
    methods as well as the query methods for
    visualization attributes and the HasOwn... test
    methods are shortcuts to the respective
    AIS_InteractiveObject settings.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TPrsStd_AISPresentation) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID for TPrsStd_AISPresentation attributes."""

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label, driver: nanoocp.Standard.Standard_GUID) -> TPrsStd_AISPresentation:
        """
        Creates or retrieves the presentation attribute on
        the label L, and sets the GUID driver.
        """

    @overload
    @staticmethod
    def Set(master: nanoocp.TDF.TDF_Attribute | None) -> TPrsStd_AISPresentation:
        """
        Creates or retrieves the AISPresentation
        attribute attached to master.
        The GUID of the driver will be the GUID of master.
        master is the attribute you want to display.
        """

    @staticmethod
    def Unset(L: nanoocp.TDF.TDF_Label) -> None:
        """
        Delete (if exist) the presentation attribute associated to the label <L>.
        """

    def SetDisplayed(self, B: bool) -> None: ...

    def Display(self, update: bool = False) -> None:
        """
        Display presentation of object in AIS viewer.
        If <update> = True then AISObject is recomputed and all
        the visualization settings are applied
        """

    def Erase(self, remove: bool = False) -> None:
        """
        Removes the presentation of this AIS
        presentation attribute from the TPrsStd_AISViewer.
        If remove is true, this AIS presentation attribute
        is removed from the interactive context.
        """

    def Update(self) -> None:
        """Recompute presentation of object and apply the visualization settings"""

    def GetDriverGUID(self) -> nanoocp.Standard.Standard_GUID: ...

    def SetDriverGUID(self, guid: nanoocp.Standard.Standard_GUID) -> None: ...

    def IsDisplayed(self) -> bool:
        """Returns true if this AIS presentation attribute is displayed."""

    def GetAIS(self) -> nanoocp.AIS.AIS_InteractiveObject:
        """Returns AIS_InteractiveObject stored in the presentation attribute"""

    def Material(self) -> nanoocp.Graphic3d.Graphic3d_NameOfMaterial:
        """Returns the material setting for this presentation attribute."""

    def SetMaterial(self, aName: nanoocp.Graphic3d.Graphic3d_NameOfMaterial) -> None:
        """Sets the material aName for this presentation attribute."""

    def HasOwnMaterial(self) -> bool:
        """
        Returns true if this presentation attribute already has a material setting.
        """

    def UnsetMaterial(self) -> None:
        """Removes the material setting from this presentation attribute."""

    def SetTransparency(self, aValue: float = 0.6) -> None:
        """
        Sets the transparency value aValue for this
        presentation attribute.
        This value is 0.6 by default.
        """

    def Transparency(self) -> float: ...

    def HasOwnTransparency(self) -> bool:
        """
        Returns true if this presentation attribute already has a transparency setting.
        """

    def UnsetTransparency(self) -> None:
        """Removes the transparency setting from this presentation attribute."""

    def Color(self) -> nanoocp.Quantity.Quantity_NameOfColor: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_NameOfColor) -> None:
        """Sets the color aColor for this presentation attribute."""

    def HasOwnColor(self) -> bool:
        """
        Returns true if this presentation attribute already has a color setting.
        """

    def UnsetColor(self) -> None:
        """Removes the color setting from this presentation attribute."""

    def Width(self) -> float: ...

    def SetWidth(self, aWidth: float) -> None:
        """Sets the width aWidth for this presentation attribute."""

    def HasOwnWidth(self) -> bool:
        """
        Returns true if this presentation attribute already has a width setting.
        """

    def UnsetWidth(self) -> None:
        """Removes the width setting from this presentation attribute."""

    def Mode(self) -> int: ...

    def SetMode(self, theMode: int) -> None: ...

    def HasOwnMode(self) -> bool: ...

    def UnsetMode(self) -> None: ...

    def GetNbSelectionModes(self) -> int:
        """
        Returns selection mode(s) of the attribute.
        It starts with 1 .. GetNbSelectionModes().
        """

    def SelectionMode(self, index: int = 1) -> int: ...

    def SetSelectionMode(self, theSelectionMode: int, theTransaction: bool = True) -> None:
        """
        Sets selection mode.
        If "theTransaction" flag is OFF, modification of the attribute doesn't influence the
        transaction mechanism (the attribute doesn't participate in undo/redo because of this
        modification). Certainly, if any other data of the attribute is modified (display mode, color,
        ...), the attribute will be included into undo/redo.
        """

    def AddSelectionMode(self, theSelectionMode: int, theTransaction: bool = True) -> None: ...

    def HasOwnSelectionMode(self) -> bool: ...

    def UnsetSelectionMode(self) -> None:
        """Clears all selection modes of the attribute."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def BackupCopy(self) -> nanoocp.TDF.TDF_Attribute: ...

    def AfterAddition(self) -> None: ...

    def BeforeRemoval(self) -> None: ...

    def BeforeForget(self) -> None: ...

    def AfterResume(self) -> None: ...

    def BeforeUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool: ...

    def AfterUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """update AIS viewer according to delta"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_AISViewer(nanoocp.TDF.TDF_Attribute):
    """
    The groundwork to define an interactive viewer attribute.
    This attribute stores an interactive context at the root label.
    You can only have one instance of this class per data framework.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TPrsStd_AISViewer) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Has(acces: nanoocp.TDF.TDF_Label) -> bool:
        """
        returns True if there is an AISViewer attribute in
        <acces> Data Framework.
        """

    @overload
    @staticmethod
    def New(access: nanoocp.TDF.TDF_Label, selector: nanoocp.AIS.AIS_InteractiveContext | None) -> TPrsStd_AISViewer:
        """
        create and set an AISViewer at. Raise an exception if
        Has.
        """

    @overload
    @staticmethod
    def New(acces: nanoocp.TDF.TDF_Label, viewer: nanoocp.V3d.V3d_Viewer | None) -> TPrsStd_AISViewer:
        """
        create and set an AISAttribute at root label. The
        interactive context is build. Raise an exception if
        Has.
        """

    @staticmethod
    def Find__TPrsStd_AISViewer(acces: nanoocp.TDF.TDF_Label) -> tuple[bool, TPrsStd_AISViewer]:
        """
        Find__TPrsStd_AISViewer: the C++ overload Find(const TDF_Label &, occ::handle<TPrsStd_AISViewer> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Finds the viewer attribute at the label access, the
        root of the data framework. Calling this function can be used to initialize an AIS viewer
        """

    @staticmethod
    def Find__AIS_InteractiveContext(acces: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveContext]:
        """
        Find__AIS_InteractiveContext: the C++ overload Find(const TDF_Label &, occ::handle<AIS_InteractiveContext> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @staticmethod
    def Find__V3d_Viewer(acces: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.V3d.V3d_Viewer]:
        """
        Find__V3d_Viewer: the C++ overload Find(const TDF_Label &, occ::handle<V3d_Viewer> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @staticmethod
    def Update_s(acces: nanoocp.TDF.TDF_Label) -> None:
        """
        AISViewer methods
        =================
        """

    def Update(self) -> None:
        """
        Updates the viewer at the label access.
        access is the root of the data framework.
        """

    def SetInteractiveContext(self, ctx: nanoocp.AIS.AIS_InteractiveContext | None) -> None:
        """Sets the interactive context ctx for this attribute."""

    def GetInteractiveContext(self) -> nanoocp.AIS.AIS_InteractiveContext:
        """Returns the interactive context in this attribute."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_Driver(nanoocp.Standard.Standard_Transient):
    """
    Driver for AIS
    ==============
    An abstract class, which - in classes inheriting
    from it - allows you to update an
    AIS_InteractiveObject or create one if one does
    not already exist.
    For both creation and update, the interactive
    object is filled with information contained in
    attributes. These attributes are those found on
    the label given as an argument in the method Update.
    true is returned if the interactive object was modified by the update.
    This class provide an algorithm to Build with its default
    values (if Null) or Update (if !Null) an AIS_InteractiveObject.
    Resources are found in attributes associated to a given
    label.
    """

    def Update(self, L: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Updates the interactive object ais with
        information found on the attributes associated with the label L.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_AxisDriver(TPrsStd_Driver):
    """An implementation of TPrsStd_Driver for axes."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty axis driver."""

    @overload
    def __init__(self, theOther: TPrsStd_AxisDriver) -> None: ...

    def Update(self, aLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Build the AISObject (if null) or update it.
        No compute is done.
        Returns <True> if information was found
        and AISObject updated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_ConstraintDriver(TPrsStd_Driver):
    """An implementation of TPrsStd_Driver for constraints."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty constraint driver."""

    @overload
    def __init__(self, theOther: TPrsStd_ConstraintDriver) -> None: ...

    def Update(self, aLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Build the AISObject (if null) or update it.
        No compute is done.
        Returns <True> if information was found
        and AISObject updated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_ConstraintTools:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TPrsStd_ConstraintTools) -> None: ...

    @staticmethod
    def UpdateOnlyValue(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None, anAIS: nanoocp.AIS.AIS_InteractiveObject | None) -> None: ...

    @staticmethod
    def ComputeDistance(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a distance dimension presentation for the given constraint.
        @param[in] aConst the distance constraint
        @return interactive object representing the distance, or null handle on failure
        """

    @staticmethod
    def ComputeDistance__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeDistance__AIS_InteractiveObject: the C++ overload ComputeDistance(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeDistance() returning handle by value instead

        @deprecated Use ComputeDistance() returning handle by value instead.
        """

    @staticmethod
    def ComputeParallel(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a parallel relation presentation for the given constraint.
        @param[in] aConst the parallel constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeParallel__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeParallel__AIS_InteractiveObject: the C++ overload ComputeParallel(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeParallel() returning handle by value instead

        @deprecated Use ComputeParallel() returning handle by value instead.
        """

    @staticmethod
    def ComputeTangent(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a tangent relation presentation for the given constraint.
        @param[in] aConst the tangent constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeTangent__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeTangent__AIS_InteractiveObject: the C++ overload ComputeTangent(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeTangent() returning handle by value instead

        @deprecated Use ComputeTangent() returning handle by value instead.
        """

    @staticmethod
    def ComputePerpendicular(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a perpendicular relation presentation for the given constraint.
        @param[in] aConst the perpendicular constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputePerpendicular__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputePerpendicular__AIS_InteractiveObject: the C++ overload ComputePerpendicular(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputePerpendicular() returning handle by value instead

        @deprecated Use ComputePerpendicular() returning handle by value instead.
        """

    @staticmethod
    def ComputeConcentric(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a concentric relation presentation for the given constraint.
        @param[in] aConst the concentric constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeConcentric__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeConcentric__AIS_InteractiveObject: the C++ overload ComputeConcentric(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeConcentric() returning handle by value instead

        @deprecated Use ComputeConcentric() returning handle by value instead.
        """

    @staticmethod
    def ComputeSymmetry(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a symmetry relation presentation for the given constraint.
        @param[in] aConst the symmetry constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeSymmetry__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeSymmetry__AIS_InteractiveObject: the C++ overload ComputeSymmetry(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeSymmetry() returning handle by value instead

        @deprecated Use ComputeSymmetry() returning handle by value instead.
        """

    @staticmethod
    def ComputeMidPoint(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a midpoint relation presentation for the given constraint.
        @param[in] aConst the midpoint constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeMidPoint__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeMidPoint__AIS_InteractiveObject: the C++ overload ComputeMidPoint(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeMidPoint() returning handle by value instead

        @deprecated Use ComputeMidPoint() returning handle by value instead.
        """

    @staticmethod
    def ComputeAngle(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes an angle dimension presentation for the given constraint.
        @param[in] aConst the angle constraint
        @return interactive object representing the angle, or null handle on failure
        """

    @staticmethod
    def ComputeAngle__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeAngle__AIS_InteractiveObject: the C++ overload ComputeAngle(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeAngle() returning handle by value instead

        @deprecated Use ComputeAngle() returning handle by value instead.
        """

    @staticmethod
    def ComputeRadius(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a radius dimension presentation for the given constraint.
        @param[in] aConst the radius constraint
        @return interactive object representing the radius, or null handle on failure
        """

    @staticmethod
    def ComputeRadius__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeRadius__AIS_InteractiveObject: the C++ overload ComputeRadius(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeRadius() returning handle by value instead

        @deprecated Use ComputeRadius() returning handle by value instead.
        """

    @staticmethod
    def ComputeMinRadius(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a minor radius dimension presentation for the given constraint.
        @param[in] aConst the minor radius constraint
        @return interactive object representing the minor radius, or null handle on failure
        """

    @staticmethod
    def ComputeMinRadius__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeMinRadius__AIS_InteractiveObject: the C++ overload ComputeMinRadius(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeMinRadius() returning handle by value instead

        @deprecated Use ComputeMinRadius() returning handle by value instead.
        """

    @staticmethod
    def ComputeMaxRadius(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a major radius dimension presentation for the given constraint.
        @param[in] aConst the major radius constraint
        @return interactive object representing the major radius, or null handle on failure
        """

    @staticmethod
    def ComputeMaxRadius__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeMaxRadius__AIS_InteractiveObject: the C++ overload ComputeMaxRadius(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeMaxRadius() returning handle by value instead

        @deprecated Use ComputeMaxRadius() returning handle by value instead.
        """

    @staticmethod
    def ComputeEqualDistance(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes an equal distance relation presentation for the given constraint.
        @param[in] aConst the equal distance constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeEqualDistance__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeEqualDistance__AIS_InteractiveObject: the C++ overload ComputeEqualDistance(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeEqualDistance() returning handle by value instead

        @deprecated Use ComputeEqualDistance() returning handle by value instead.
        """

    @staticmethod
    def ComputeEqualRadius(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes an equal radius relation presentation for the given constraint.
        @param[in] aConst the equal radius constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeEqualRadius__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeEqualRadius__AIS_InteractiveObject: the C++ overload ComputeEqualRadius(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeEqualRadius() returning handle by value instead

        @deprecated Use ComputeEqualRadius() returning handle by value instead.
        """

    @staticmethod
    def ComputeFix(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a fix constraint presentation for the given constraint.
        @param[in] aConst the fix constraint
        @return interactive object representing the constraint, or null handle on failure
        """

    @staticmethod
    def ComputeFix__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeFix__AIS_InteractiveObject: the C++ overload ComputeFix(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeFix() returning handle by value instead

        @deprecated Use ComputeFix() returning handle by value instead.
        """

    @staticmethod
    def ComputeDiameter(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a diameter dimension presentation for the given constraint.
        @param[in] aConst the diameter constraint
        @return interactive object representing the diameter, or null handle on failure
        """

    @staticmethod
    def ComputeDiameter__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeDiameter__AIS_InteractiveObject: the C++ overload ComputeDiameter(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeDiameter() returning handle by value instead

        @deprecated Use ComputeDiameter() returning handle by value instead.
        """

    @staticmethod
    def ComputeOffset(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes an offset relation presentation for the given constraint.
        @param[in] aConst the offset constraint
        @return interactive object representing the offset, or null handle on failure
        """

    @staticmethod
    def ComputeOffset__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeOffset__AIS_InteractiveObject: the C++ overload ComputeOffset(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeOffset() returning handle by value instead

        @deprecated Use ComputeOffset() returning handle by value instead.
        """

    @staticmethod
    def ComputePlacement(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a placement relation presentation for the given constraint.
        @param[in] aConst the placement constraint
        @return interactive object representing the placement, or null handle on failure
        """

    @staticmethod
    def ComputePlacement__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputePlacement__AIS_InteractiveObject: the C++ overload ComputePlacement(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputePlacement() returning handle by value instead

        @deprecated Use ComputePlacement() returning handle by value instead.
        """

    @staticmethod
    def ComputeCoincident(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a coincident relation presentation for the given constraint.
        @param[in] aConst the coincident constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeCoincident__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeCoincident__AIS_InteractiveObject: the C++ overload ComputeCoincident(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeCoincident() returning handle by value instead

        @deprecated Use ComputeCoincident() returning handle by value instead.
        """

    @staticmethod
    def ComputeRound(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a round (fillet) relation presentation for the given constraint.
        @param[in] aConst the round constraint
        @return interactive object representing the relation, or null handle on failure
        """

    @staticmethod
    def ComputeRound__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeRound__AIS_InteractiveObject: the C++ overload ComputeRound(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeRound() returning handle by value instead

        @deprecated Use ComputeRound() returning handle by value instead.
        """

    @staticmethod
    def ComputeOthers(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes a presentation for constraint types not handled by specific methods.
        @param[in] aConst the constraint
        @return interactive object representing the constraint, or null handle on failure
        """

    @staticmethod
    def ComputeOthers__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeOthers__AIS_InteractiveObject: the C++ overload ComputeOthers(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeOthers() returning handle by value instead

        @deprecated Use ComputeOthers() returning handle by value instead.
        """

    @staticmethod
    def ComputeTextAndValue(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None, aText: nanoocp.TCollection.TCollection_ExtendedString, anIsAngle: bool) -> float: ...

    @staticmethod
    def ComputeAngleForOneFace(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        Computes an angle dimension presentation for a single-face constraint.
        @param[in] aConst the angle constraint on one face
        @return interactive object representing the angle, or null handle on failure
        """

    @staticmethod
    def ComputeAngleForOneFace__AIS_InteractiveObject(aConst: nanoocp.TDataXtd.TDataXtd_Constraint | None) -> nanoocp.AIS.AIS_InteractiveObject:
        """
        ComputeAngleForOneFace__AIS_InteractiveObject: the C++ overload ComputeAngleForOneFace(const occ::handle<TDataXtd_Constraint> &, occ::handle<AIS_InteractiveObject> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ComputeAngleForOneFace() returning handle by value instead

        @deprecated Use ComputeAngleForOneFace() returning handle by value instead.
        """

class TPrsStd_DriverTable(nanoocp.Standard.Standard_Transient):
    """
    This class is a container to record (AddDriver)
    binding between GUID and TPrsStd_Driver.
    You create a new instance of TPrsStd_Driver
    and use the method AddDriver to load it into the driver table.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: TPrsStd_DriverTable) -> None: ...

    @staticmethod
    def Get() -> TPrsStd_DriverTable:
        """
        Returns the static table.
        If it does not exist, creates it and fills it with standard drivers.
        """

    def InitStandardDrivers(self) -> None:
        """Fills the table with standard drivers"""

    def AddDriver(self, guid: nanoocp.Standard.Standard_GUID, driver: TPrsStd_Driver | None) -> bool:
        """
        Returns true if the driver has been added successfully to the driver table.
        """

    def FindDriver(self, guid: nanoocp.Standard.Standard_GUID) -> tuple[bool, TPrsStd_Driver]:
        """Returns true if the driver was found."""

    def RemoveDriver(self, guid: nanoocp.Standard.Standard_GUID) -> bool:
        """
        Removes a driver with the given GUID.
        Returns true if the driver has been removed successfully.
        """

    def Clear(self) -> None:
        """
        Removes all drivers.
        Returns true if the driver has been removed successfully.
        If this method is used, the InitStandardDrivers method should be
        called to fill the table with standard drivers.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_GeometryDriver(TPrsStd_Driver):
    """This method is an implementation of TPrsStd_Driver for geometries."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty geometry driver."""

    @overload
    def __init__(self, theOther: TPrsStd_GeometryDriver) -> None: ...

    def Update(self, aLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Build the AISObject (if null) or update it.
        No compute is done.
        Returns <True> if information was found
        and AISObject updated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_NamedShapeDriver(TPrsStd_Driver):
    """An implementation of TPrsStd_Driver for named shapes."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty named shape driver."""

    @overload
    def __init__(self, theOther: TPrsStd_NamedShapeDriver) -> None: ...

    def Update(self, aLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Build the AISObject (if null) or update it.
        No compute is done.
        Returns <True> if information was found
        and AISObject updated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_PlaneDriver(TPrsStd_Driver):
    """An implementation of TPrsStd_Driver for planes."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty plane driver."""

    @overload
    def __init__(self, theOther: TPrsStd_PlaneDriver) -> None: ...

    def Update(self, aLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Build the AISObject (if null) or update it.
        No compute is done.
        Returns <True> if information was found
        and AISObject updated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TPrsStd_PointDriver(TPrsStd_Driver):
    """An implementation of TPrsStd_Driver for points."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty point driver."""

    @overload
    def __init__(self, theOther: TPrsStd_PointDriver) -> None: ...

    def Update(self, aLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.AIS.AIS_InteractiveObject]:
        """
        Build the AISObject (if null) or update it.
        No compute is done.
        Returns <True> if information was found
        and AISObject updated.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
