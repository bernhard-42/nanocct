"""OCCT package StdFail (toolkit TKernel)"""

import nanoocp.Standard


class StdFail_InfiniteSolutions(nanoocp.Standard.Standard_Failure):
    pass

class StdFail_NotDone(nanoocp.Standard.Standard_Failure):
    pass

class StdFail_Undefined(nanoocp.Standard.Standard_Failure):
    pass

class StdFail_UndefinedDerivative(nanoocp.Standard.Standard_DomainError):
    pass

class StdFail_UndefinedValue(nanoocp.Standard.Standard_DomainError):
    pass
