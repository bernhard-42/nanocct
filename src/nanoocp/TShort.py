"""OCCT package TShort (toolkit TKernel)."""
from nanoocp._TKernel import TShort as _ext
from nanoocp._TKernel.TShort import *  # noqa: F401,F403


def __getattr__(name):
    # NCollection instantiations are added to their home package by whichever toolkit needs them first,
    # possibly after this shim was imported
    return getattr(_ext, name)
