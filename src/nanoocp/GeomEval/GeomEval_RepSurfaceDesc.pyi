"""C++ namespace GeomEval_RepSurfaceDesc (OCCT package GeomEval)"""

import enum

import nanoocp.Geom
import nanoocp.Standard


class Map2d:
    """
    2D diagonal affine parameter map with optional UV swap.
    Without swap: uRep = ScaleU*u + OffsetU, vRep = ScaleV*v + OffsetV.
    With swap:    uRep = ScaleU*v + OffsetU, vRep = ScaleV*u + OffsetV.
    """

    def __init__(self) -> None: ...

    def IsIdentity(self) -> bool: ...

    def IsValid(self) -> bool: ...

    def Map(self, theU: float, theV: float) -> tuple[float, float]: ...

    @property
    def ScaleU(self) -> float: ...

    @ScaleU.setter
    def ScaleU(self, arg: float, /) -> None: ...

    @property
    def OffsetU(self) -> float: ...

    @OffsetU.setter
    def OffsetU(self, arg: float, /) -> None: ...

    @property
    def ScaleV(self) -> float: ...

    @ScaleV.setter
    def ScaleV(self, arg: float, /) -> None: ...

    @property
    def OffsetV(self) -> float: ...

    @OffsetV.setter
    def OffsetV(self, arg: float, /) -> None: ...

    @property
    def SwapUV(self) -> bool: ...

    @SwapUV.setter
    def SwapUV(self, arg: bool, /) -> None: ...

class Domain2d:
    """2D parameter domain."""

    def __init__(self) -> None: ...

    def Contains(self, theU: float, theV: float) -> bool: ...

    @property
    def UFirst(self) -> float: ...

    @UFirst.setter
    def UFirst(self, arg: float, /) -> None: ...

    @property
    def ULast(self) -> float: ...

    @ULast.setter
    def ULast(self, arg: float, /) -> None: ...

    @property
    def VFirst(self) -> float: ...

    @VFirst.setter
    def VFirst(self, arg: float, /) -> None: ...

    @property
    def VLast(self) -> float: ...

    @VLast.setter
    def VLast(self, arg: float, /) -> None: ...

class Base(nanoocp.Standard.Standard_Transient):
    """
    Abstract base descriptor for surface evaluation representation.
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
    def Representation(self) -> nanoocp.Geom.Geom_Surface:
        """geometry used for evaluation"""

    @Representation.setter
    def Representation(self, arg: nanoocp.Geom.Geom_Surface, /) -> None: ...

class Full(Base):
    """
    Fully equivalent descriptor: no derivative limit, no domain, no map.
    Fastest evaluation path - direct delegation to Representation.
    """

    def __init__(self) -> None: ...

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

    def __init__(self) -> None: ...

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
    Mapped descriptor for surface evaluation representation.
    Adds optional bounded domain and diagonal affine parameter map with optional UV swap.
    Evaluation requires: domain check -> map parameters -> evaluate -> scale derivatives.
    Future subclasses can support multi-region descriptors with per-patch UV domains and maps.
    """

    def __init__(self) -> None: ...

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
    def Domain(self) -> Domain2d | None:
        """nullopt = full domain"""

    @Domain.setter
    def Domain(self, arg: Domain2d | None, /) -> None: ...

    @property
    def ParamMap(self) -> Map2d:
        """affine parameter transform"""

    @ParamMap.setter
    def ParamMap(self, arg: Map2d, /) -> None: ...
