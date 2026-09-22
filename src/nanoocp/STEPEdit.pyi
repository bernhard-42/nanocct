"""OCCT package STEPEdit (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.IFSelect
import nanoocp.Interface
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.TCollection


class STEPEdit:
    """
    Provides tools to exploit and edit a set of STEP data :
    editors, selections ..
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPEdit) -> None: ...

    @staticmethod
    def Protocol() -> nanoocp.Interface.Interface_Protocol:
        """Returns a Protocol fit for STEP (creates the first time)"""

    @staticmethod
    def NewModel() -> nanoocp.StepData.StepData_StepModel:
        """
        Returns a new empty StepModel fit for STEP
        i.e. with its header determined from Protocol
        """

    @staticmethod
    def SignType() -> nanoocp.IFSelect.IFSelect_Signature:
        """Returns a SignType fit for STEP (creates the first time)"""

    @staticmethod
    def NewSelectSDR() -> nanoocp.IFSelect.IFSelect_SelectSignature:
        """
        Creates a Selection for ShapeDefinitionRepresentation
        By default searches among root entities
        """

    @staticmethod
    def NewSelectPlacedItem() -> nanoocp.IFSelect.IFSelect_SelectSignature:
        """
        Creates a Selection for Placed Items, i.e. MappedItem or
        ContextDependentShapeRepresentation, which itself refers to a
        RepresentationRelationship with possible subtypes (Shape...
        and/or ...WithTransformation)
        By default in the whole StepModel
        """

    @staticmethod
    def NewSelectShapeRepr() -> nanoocp.IFSelect.IFSelect_SelectSignature:
        """
        Creates a Selection for ShapeRepresentation and its sub-types,
        plus ContextDependentShapeRepresentation (which is not a
        sub-type of ShapeRepresentation)
        By default in the whole StepModel
        """

class STEPEdit_EditContext(nanoocp.IFSelect.IFSelect_Editor):
    """
    EditContext is an Editor fit for
    Product Definition Context (one per Model) , i.e. :
    - ProductDefinition
    - ApplicationProtocolDefinition
    - ProductRelatedProductCategory
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPEdit_EditContext) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Recognize(self, form: nanoocp.IFSelect.IFSelect_EditForm | None) -> bool: ...

    def StringValue(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Apply(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    def Load(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPEdit_EditSDR(nanoocp.IFSelect.IFSelect_Editor):
    """
    EditSDR is an Editor fit for a Shape Definition Representation
    which designates a Product Definition
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPEdit_EditSDR) -> None: ...

    def Label(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Recognize(self, form: nanoocp.IFSelect.IFSelect_EditForm | None) -> bool: ...

    def StringValue(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def Apply(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    def Load(self, form: nanoocp.IFSelect.IFSelect_EditForm | None, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
