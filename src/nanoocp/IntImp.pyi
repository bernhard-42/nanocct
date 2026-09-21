"""OCCT package IntImp (toolkit TKGeomAlgo)"""

import enum


class IntImp_ConstIsoparametric(enum.IntEnum):
    IntImp_UIsoparametricOnCaro1 = 0

    IntImp_VIsoparametricOnCaro1 = 1

    IntImp_UIsoparametricOnCaro2 = 2

    IntImp_VIsoparametricOnCaro2 = 3

IntImp_UIsoparametricOnCaro1: IntImp_ConstIsoparametric = ...

IntImp_VIsoparametricOnCaro1: IntImp_ConstIsoparametric = ...

IntImp_UIsoparametricOnCaro2: IntImp_ConstIsoparametric = ...

IntImp_VIsoparametricOnCaro2: IntImp_ConstIsoparametric = ...

def ChoixRef(theIndex: int) -> IntImp_ConstIsoparametric: ...
