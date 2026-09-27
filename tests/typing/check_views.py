"""The zero-copy accessors (R-VIEW) must type-check with their real dtype, and must be absent where they are
absent at runtime.
"""
import numpy as np
from numpy.typing import NDArray

from OCP3x import Image, NCollection, Poly

# The container accessor is on the concrete class, not on the generic one: its dtype is the element's.
pnts = NCollection.NCollection_Array1__gp_Pnt(1, 3)
xyz: NDArray[np.float64] = pnts.ValuesArray()

tris = NCollection.NCollection_Array1__Poly_Triangle(1, 3)
idx: NDArray[np.int32] = tris.ValuesArray()

grid = NCollection.NCollection_Array2__double(1, 2, 1, 3)
cells: NDArray[np.float64] = grid.ValuesArray()

held = NCollection.NCollection_HArray1__double(1, 3, 0.0)      # inherited from the Array1 sibling
vals: NDArray[np.float64] = held.ValuesArray()

# An element type with nothing packed to view has no accessor, and the stub must say so rather than
# promising one for every NCollection_Array1[_T].
shapes = NCollection.NCollection_Array1__TopoDS_Shape(1, 2)
shapes.ValuesArray()                                            # error: no such attribute

# An accessor that can return None is typed as such, so the checker insists on the guard.
uv = Poly.Poly_Triangulation(3, 1, True, False).UVNodesArray()
uv.shape                                                        # error: None has no attribute

pix = Image.Image_PixMap().DataArray()
if pix is not None:
    pix.shape
