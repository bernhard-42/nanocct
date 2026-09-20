"""OCCT package Plugin (toolkit TKernel)"""

from typing import overload

import nanoocp.Standard


class Plugin:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Plugin) -> None: ...

    @staticmethod
    def Load(aGUID: nanoocp.Standard.Standard_GUID, theVerbose: bool = True) -> nanoocp.Standard.Standard_Transient: ...

class Plugin_Failure(nanoocp.Standard.Standard_Failure):
    pass
