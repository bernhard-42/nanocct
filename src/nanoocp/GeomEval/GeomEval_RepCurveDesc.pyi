"""C++ namespace GeomEval_RepCurveDesc (OCCT package GeomEval)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.Standard


class Map1d:
    """1D affine parameter map: uRep = Scale * u + Offset."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Map1d) -> None: ...

    def IsIdentity(self) -> bool: ...

    def IsValid(self) -> bool: ...

    def Map(self, theU: float) -> float: ...

    @property
    def Scale(self) -> float: ...

    @Scale.setter
    def Scale(self, arg: float, /) -> None: ...

    @property
    def Offset(self) -> float: ...

    @Offset.setter
    def Offset(self, arg: float, /) -> None: ...

class Domain1d:
    """1D parameter domain interval."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Domain1d) -> None: ...

    def Contains(self, theU: float) -> bool: ...

    @property
    def First(self) -> float: ...

    @First.setter
    def First(self, arg: float, /) -> None: ...

    @property
    def Last(self) -> float: ...

    @Last.setter
    def Last(self, arg: float, /) -> None: ...

class Base(nanoocp.Standard.Standard_Transient):
    """
    Abstract base descriptor for curve evaluation representation.
    Holds the representation handle and a Kind tag for switch-based dispatch.
    """

    class Kind(enum.Enum):
        """Descriptor kind for switch-based dispatch (no RTTI needed)."""

        Full = 0

        DerivBounded = 1

        Mapped = 2

    def GetKind(self) -> Base.Kind:
        """Returns the descriptor kind."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def Representation(self) -> nanoocp.Geom.Geom_Curve:
        """geometry used for evaluation"""

    @Representation.setter
    def Representation(self, arg: nanoocp.Geom.Geom_Curve, /) -> None: ...

class Full(Base):
    """
    Fully equivalent descriptor: no derivative limit, no domain, no map.
    Fastest evaluation path - direct delegation to Representation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Full) -> None: ...

    def GetKind(self) -> Base.Kind: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class DerivBounded(Base):
    """
    Derivative-bounded descriptor: full domain, identity map, limited to MaxDerivOrder.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DerivBounded) -> None: ...

    def GetKind(self) -> Base.Kind: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def MaxDerivOrder(self) -> int:
        """max supported derivative order"""

    @MaxDerivOrder.setter
    def MaxDerivOrder(self, arg: int, /) -> None: ...

class Mapped(Base):
    """
    Mapped descriptor for curve evaluation representation.
    Adds optional bounded domain and affine parameter map.
    Evaluation requires: domain check -> map parameter -> evaluate -> scale derivatives.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Mapped) -> None: ...

    def GetKind(self) -> Base.Kind: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def MaxDerivOrder(self) -> int:
        """max supported derivative order"""

    @MaxDerivOrder.setter
    def MaxDerivOrder(self, arg: int, /) -> None: ...

    @property
    def Domain(self) -> Domain1d | None:
        """nullopt = full domain"""

    @Domain.setter
    def Domain(self, arg: Domain1d | None, /) -> None: ...

    @property
    def ParamMap(self) -> Map1d:
        """affine parameter transform"""

    @ParamMap.setter
    def ParamMap(self, arg: Map1d, /) -> None: ...
