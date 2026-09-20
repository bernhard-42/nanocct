"""OCCT package Plugin (toolkit TKernel)"""

import nanoocp.Standard


class Plugin:
    def __init__(self) -> None: ...

    @staticmethod
    def Load(aGUID: nanoocp.Standard.Standard_GUID, theVerbose: bool = True) -> nanoocp.Standard.Standard_Transient: ...

class Plugin_Failure(nanoocp.Standard.Standard_Failure):
    pass
