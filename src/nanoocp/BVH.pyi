"""OCCT package BVH (toolkit TKMath)"""

import nanoocp.Standard


THE_NODE_MIN_SIZE: float = 1e-05

THE_MORTON_LUT: int = 0

BVH_Constants_MaxTreeDepth: int = 32

BVH_Constants_LeafNodeSizeSingle: int = 1

BVH_Constants_LeafNodeSizeAverage: int = 4

BVH_Constants_LeafNodeSizeDefault: int = 5

BVH_Constants_LeafNodeSizeSmall: int = 8

BVH_Constants_NbBinsOptimal: int = 32

BVH_Constants_NbBinsBest: int = 48

class BVH_TreeBaseTransient(nanoocp.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_TreeBase
    (just to have a named base class).
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BVH_QuadTree:
    """Type corresponding to quad BVH."""

    def __init__(self) -> None: ...

class BVH_BinaryTree:
    """Type corresponding to binary BVH."""

    def __init__(self) -> None: ...

class BVH_BuilderTransient(nanoocp.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_Builder
    (just to have a named base class).
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def MaxTreeDepth(self) -> int:
        """Returns the maximum depth of constructed BVH."""

    def LeafNodeSize(self) -> int:
        """Returns the maximum number of sub-elements in the leaf."""

    def IsParallel(self) -> bool:
        """Returns parallel flag."""

    def SetParallel(self, isParallel: bool) -> None:
        """Set parallel flag controlling possibility of parallel execution."""

class BVH_BuildQueue:
    """Command-queue for parallel building of BVH nodes."""

    def __init__(self) -> None:
        """Creates new BVH build queue."""

    def Size(self) -> int:
        """
        Returns current size of BVH build queue.
        Uses acquire semantics to synchronize with enqueue/dequeue operations.
        """

    def Enqueue(self, theWorkItem: int) -> None:
        """Enqueues new work-item onto BVH build queue."""

    def Fetch(self) -> tuple[int, bool]:
        """Fetches first work-item from BVH build queue."""

    def HasBusyThreads(self) -> bool:
        """
        Checks if there are active build threads.
        Uses acquire semantics to ensure visibility of thread counter updates.
        This is critical for termination detection: threads check this after
        finding an empty queue to determine if they should exit or wait.
        """

class BVH_BuildTool:
    """Tool object to call BVH builder subroutines."""

    def Perform(self, theNode: int) -> None:
        """Performs splitting of the given BVH node."""

class BVH_BuildThread(nanoocp.Standard.Standard_Transient):
    """Wrapper for BVH build thread."""

    def __init__(self, theBuildTool: BVH_BuildTool, theBuildQueue: BVH_BuildQueue) -> None:
        """Creates new BVH build thread."""

    def Run(self) -> None:
        """Starts execution of BVH build thread."""

    def Wait(self) -> None:
        """Waits till the thread finishes execution."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BVH_Properties(nanoocp.Standard.Standard_Transient):
    """Abstract properties of geometric object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BVH_ObjectTransient(nanoocp.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_Object
    (just to have a named base class).
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Properties(self) -> BVH_Properties:
        """Returns properties of the geometric object."""

    def SetProperties(self, theProperties: BVH_Properties) -> None:
        """Sets properties of the geometric object."""

    def IsDirty(self) -> bool:
        """Returns TRUE if object state should be updated."""

    def MarkDirty(self) -> None:
        """Marks object state as outdated (needs BVH rebuilding)."""
