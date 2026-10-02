# Pythonic addition to the OCCT bindings

**Table of contents**

- [NCollections](#ncollections-support)
- [Iterating over OCCT iterators](#iterating-over-occt-iterators)
- [numpy zero-copy support in detail](#numpy-zero-copy-support-in-detail)
- [Handling of primitive types passed by reference](#handling-of-primitive-types-passed-by-reference)
- [Mutable primitive references](#mutable-primitive-references)
- [Operators](#operators)
- [Equality in OCCT and Python](#equality-in-occt-and-python)
- [Strings](#strings)
- [Handling of istream and ostream](#handling-of-istream-and-ostream)
- [Enums](#enums)
- [Exceptions](#exceptions)
- [Doc strings](#doc-strings)
- [AddOns](#addons)


## NCollections support

**Design: [2a Naming conventions](Design.md#2a-naming-conventions), [6a NCollection containers](Design.md#6a-ncollection-containers-hand-written-binders)**

### Generics support

Let's look at the C++ example `NCollection_Array1<gp_Dir>`:

The nanocct generator binds this as a class `NCollection_Array1__gp_Dir`

```python
from nanocct.NCollection import NCollection_Array1__gp_Dir

a = NCollection_Array1__gp_Dir(1, 3)
```

and adds a Python generics type definition to it

```python
from nanocct.gp import gp_Dir
from nanocct.NCollection import NCollection_Array1

b = NCollection_Array1[gp_Dir](1, 3)
```

1. The two constructs are the same type

   ```python
   In[1]: NCollection_Array1__gp_Dir is NCollection_Array1[gp_Dir]
   Out[1]: True
   ```

2. Different element types are different classes

   ```python
   In[2]: NCollection_Array1[gp_Dir] is NCollection_Array1[int]
   Out[2]: False
   ```

3. `isinstance` can be used with both types

   ```python
   In[3]: isinstance(a, NCollection_Array1)
   Out[3]: True

   In[4]: isinstance(b, NCollection_Array1)
   Out[4]: True

   In[5]: isinstance(a, NCollection_Array1__gp_Dir)
   Out[5]: True

   In[6]: isinstance(b, NCollection_Array1__gp_Dir)
   Out[6]: True

   In[7]: type(a) is type(b)
   Out[7]: True
   ```

4. There is a minimal overhead using generic types:

   ```python
   In [8]: %timeit NCollection_Array1__gp_Dir(1, 3)
   42.9 ns ± 0.575 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

   In [9]: %timeit NCollection_Array1[gp_Dir](1, 3)
   79.2 ns ± 1.84 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
   ```

   | Statement                          | Timing             |
   | ---------------------------------- | ------------------ |
   | `NCollection_Array1__gp_Dir(1, 3)` | 42.9 ns ± 0.575 ns |
   | `NCollection_Array1[gp_Dir](1, 3)` | 79.2 ns ± 1.84 ns  |

   Typically, the NCollections don't appear in large loops where the nanoseconds could pile up, but are created once and then filled in a loop. Since both statements create the same type at runtime, accessing the NCollections takes the same time.

### C++ scalar types

A Python type stands for a C++ template argument: `float` for C++ `double`, `int`, `bool`, and `str` for `std::string`. Python has no own type for five more C++ scalars used in OCCT 8, so `nanocct.NCollection` exports a marker for each:

| Marker      | C++ type             |
| ----------- | -------------------- |
| `float32`   | `float` (32-bit)     |
| `uchar`     | `unsigned char`      |
| `uint`      | `unsigned int`       |
| `ulong`     | `unsigned long`      |
| `ulonglong` | `unsigned long long` |

With them, every NCollection class of nanocct can be spelled generically:

```python
In [1]: from nanocct.NCollection import NCollection_Array1, NCollection_HArray1, float32, uchar
   ...: from nanocct.Poly import Poly_Triangulation

In [2]: NCollection_HArray1[float32].__name__, NCollection_HArray1[uchar].__name__
Out[2]: ('NCollection_HArray1__float', 'NCollection_HArray1__unsigned_char')

In [3]: NCollection_Array1[float].__name__
Out[3]: 'NCollection_Array1__double'
```

The markers are only keys. The values are plain Python floats and ints, and the C++ class does the conversion, e.g. the rounding to 32 bits:

```python
In [4]: normals = NCollection_HArray1[float32](1, 9, 0.0)   # 3 nodes, x y z each
   ...: normals.SetValue(1, 0.1)
   ...: normals.Value(1)
Out[4]: 0.10000000149011612

In [5]: tri = Poly_Triangulation(3, 1, False, False)
   ...: tri.SetNormals(normals)
   ...: tri.HasNormals()
Out[5]: True
```

For type checkers the markers are aliases of `float` and `int`: precision is not a Python type, the same as for every other C++ `float` or `unsigned int` parameter of the bindings. So a type checker does not tell `NCollection_HArray1[float32]` from `NCollection_HArray1[float]`; handing the wrong one to OCCT fails at runtime with a `TypeError`.

### numpy zero-copy support

The nanocct generator gives e.g. `NCollection_Array1` and `NCollection_Array2` numpy's array protocol, `__array__`, see [details](#numpy-zero-copy-support-in-detail).

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...: from nanocct.gp import gp_Vec
   ...: import numpy as np
   ...:
   ...: a = NCollection_Array1[gp_Vec](1, 3)
   ...:
   ...: a.SetValue(1, gp_Vec(1, 0, 0))
   ...: a.SetValue(2, gp_Vec(0, 1, 0))
   ...: a.SetValue(3, gp_Vec(0, 0, 1))

In [2]: np.asarray(a)
Out[2]:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

This accesses the C++ values from Python without copying them (zero-copy access). A view, like an element reference from `ChangeValue()` or an iterator, points into the container's storage, which it keeps alive but cannot keep in place. So the container refuses every call that would move or free what a live view points to, as a `bytearray` does while a buffer is exported: a `Resize()` to another length, a `Remove()`, a `Clear()`, or an OCCT function that takes the container to fill it raises `BufferError`. Release the view first, or take it after the change:

```python
In [3]: v = np.asarray(a)
   ...: try:
   ...:     a.Resize(1, 5, True)
   ...: except BufferError as e:
   ...:     msg = str(e)
   ...: msg
Out[3]: 'Resize: 1 live view(s) of this container (element references, iterators or numpy arrays) would be invalidated by this call; release them first (BufferError, as bytearray raises while a buffer is exported)'

In [4]: del v
   ...: a.Resize(1, 5, True)
   ...: np.asarray(a).shape
Out[4]: (5, 3)
```

A call that keeps the storage in place goes through while a view lives: `SetValue()`, a `Resize()` to the same length, an `Assign()` of an array of the same size. Which call refuses for which container is listed in [Design 6a](Design.md#views-a-container-refuses-to-invalidate-r-view-guard-2026-10-02).

### Index access

`a[i]` makes OCCT's item access available with OCCT's index, and nothing more: `NCollection_Array1` counts from `Lower()`, `NCollection_Sequence` and the indexed maps from 1, `NCollection_DynamicArray` and `NCollection_LinearVector` from 0. There are no negative indices and no slices, because a negative index is a real OCCT index for an array like `NCollection_Array1[float](-2, 2)`. For Python-style indexing, use a numpy view or a list:

```python
In [1]: import numpy as np
   ...: from nanocct.NCollection import NCollection_Array1
   ...:
   ...: a = NCollection_Array1[float](1, 8)
   ...: for i in range(1, 9):
   ...:     a.SetValue(i, i * 10.0)

In [2]: a[1], a[3]
Out[2]: (10.0, 30.0)

In [3]: a.Last(), np.asarray(a)[-1], list(a)[-1]
Out[3]: (80.0, np.float64(80.0), 80.0)
```

OCCT's own `At(i)` is 0-based like `np.asarray(a)[i]`, and range-checked: `NCollection_Array1`, `NCollection_Array2` (`At(row, col)`) and `NCollection_Sequence` have it, together with their `HArray`/`HSequence` variants. Unlike a numpy view, it works for every element type, e.g. an array of `TopoDS_Shape`. It takes no negative index.

```python
In [4]: a.At(0), a.At(2)
Out[4]: (10.0, 30.0)

In [5]: list(a)[0], np.asarray(a)[2]
Out[5]: (10.0, np.float64(30.0))
```

Timing

```python
In [6]: %timeit a.Value(3)
17 ns ± 0.0779 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [7]: %timeit a[3]
19.7 ns ± 0.257 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
```

| Statement    | Timing             |
| ------------ | ------------------ |
| `a.Value(3)` | 17 ns ± 0.0779 ns  |
| `a[3]`       | 19.7 ns ± 0.257 ns |

**Note:** nanocct keeps OCCT's C++ contract for index access and adds no checks of its own. Where OCCT checks, a wrong index or an empty container raises an OCCT exception: `Value`/`ChangeValue`/`SetValue`/`At` of `NCollection_Array1`, `Array2`, `Sequence` and `LinearVector` raise `Standard_OutOfRange` (`a[0]` above), and `First()`/`Last()` of an empty `List` or `Sequence` raise `Standard_NoSuchObject` (of an empty `LinearVector` `Standard_OutOfRange`). Where OCCT does not check, it behaves as in C++ and can crash the Python interpreter:

- `First()`/`Last()` of an empty `NCollection_Array1` or `HArray1` (OCCT reads the first element of no storage; `ChangeFirst()` there returns `None` instead);
- `Value()` of a default-constructed or exhausted OCCT `Iterator` (`NCollection_List[int].Iterator().Value()`);
- `NCollection_DynamicArray`'s `Value`, `ChangeValue` and `d[i]` past the end: within the first block they return whatever the memory holds (`d[3]` of a 3-element array is `0`), beyond it (`d[256]`) the process crashes; likewise `NCollection_Mat4.GetValue`;
- a constructor whose upper bound lies below the lower one: `NCollection_Array1[float](5, 1)` constructs an array whose `Size()` is 18446744073709551613 (`len()` then raises `ValueError`, and `Init()` crashes), and `NCollection_Array2[float](3, 1, 1, 2).NbRows()` is `-1`.

### Iterating over NCollections

- 100 `float` element `NCollection`

  ```python
  In [1]: import numpy as np
     ...: from nanocct.NCollection import NCollection_Array1
     ...:
     ...: N = 100
     ...: a = NCollection_Array1[float](1, N)
     ...: for i in range(1, N+1):
     ...:     a.SetValue(i, i * 10.0)
     ...:

  In [2]: %timeit [a.Value(i) for i in range(1, N + 1)]
  2.06 μs ± 14.9 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

  In [3]: %timeit list(a)
  1.17 μs ± 11.2 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

- 10 `float` element `NCollection`

  ```python
  In [4]: N = 10
     ...: a = NCollection_Array1[float](1, N)
     ...: for i in range(1, N+1):
     ...:     a.SetValue(i, i * 10.0)
     ...:

  In [5]: %timeit [a.Value(i) for i in range(1, N + 1)]
  248 ns ± 2.55 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

  In [6]: %timeit list(a)
  221 ns ± 2.69 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

| Statement                               | 100 elements      | 10 elements      |
| --------------------------------------- | ----------------- | ---------------- |
| `[a.Value(i) for i in range(1, N + 1)]` | 2.06 μs ± 14.9 ns | 248 ns ± 2.55 ns |
| `list(a)`                               | 1.17 μs ± 11.2 ns | 221 ns ± 2.69 ns |

Below 7 or 8 elements, `list(a)` gets slightly slower due to the creating the iterator.

`x in container` is OCCT's lookup where there is one: the maps (`IsBound`/`Contains` by key), and `NCollection_List` where the element type has `operator==` (`Contains`). Elsewhere Python falls back to iterating with its own `==`, which works for numbers and strings but is identity for a class without a value `==`: `gp_Pnt(1, 2, 3) in l` is `False` for a list holding an equal point. Compare explicitly there, `any(p.IsEqual(q, tol) for p in l)`.

### Uninitialised values

Like in C++, a new array of a scalar type (`float`, `int`, `bool`, `float32`, …) is not initialised: OCCT allocates the memory and leaves it as it is. It often reads as `0.0`, but that is chance, and a larger array can show values left over from earlier allocations. Class elements such as `gp_Vec` are default-constructed. Use OCCT's `Init(value)`, or the fill value of the `NCollection_HArray1` constructor:

```python
In [1]: from nanocct.NCollection import NCollection_Array1, NCollection_HArray1
   ...: from nanocct.gp import gp_Vec
   ...:
   ...: a = NCollection_Array1[float](1, 3)
   ...: a.Init(0.0)
   ...: list(a)
Out[1]: [0.0, 0.0, 0.0]

In [2]: list(NCollection_HArray1[float](1, 3, 0.5))
Out[2]: [0.5, 0.5, 0.5]

In [3]: [v.Coord() for v in NCollection_Array1[gp_Vec](1, 2)]
Out[3]: [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0)]
```

## Iterating over OCCT iterators

**Binding rule: R-ITER ([Design 2c](Design.md#2c-python-additions))**

Every OCCT class with `More()`, `Next()` and a `Current()` or `Value()` is a Python iterable: `TopExp_Explorer`, `TopoDS_Iterator`, `BRepTools_WireExplorer` and the other OCCT iterators, and the `Iterator` classes of the NCollections. A `for` loop runs OCCT's own `More()`/`Next()` loop and yields `Current()` (or `Value()`).

```python
In [1]: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.TopExp import TopExp, TopExp_Explorer
   ...: from nanocct.TopAbs import TopAbs_ShapeEnum
   ...: from nanocct.TopoDS import TopoDS_Iterator, TopoDS_Shape
   ...: from nanocct.TopTools import TopTools_ShapeMapHasher
   ...: from nanocct.NCollection import NCollection_IndexedMap
   ...:
   ...: FACE, EDGE = TopAbs_ShapeEnum.TopAbs_FACE, TopAbs_ShapeEnum.TopAbs_EDGE
   ...: box = BRepPrimAPI_MakeBox(1, 2, 3).Shape()

In [2]: [f.ShapeType().name for f in TopExp_Explorer(box, FACE)]
Out[2]: ['TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE']

In [3]: [c.ShapeType().name for c in TopoDS_Iterator(box)]
Out[3]: ['TopAbs_SHELL']
```

The loop advances the iterator object itself, so it is used up afterwards, like a file. OCCT's `ReInit()` starts it again:

```python
In [4]: ex = TopExp_Explorer(box, FACE)
   ...: len(list(ex)), len(list(ex))
Out[4]: (6, 0)

In [5]: ex.ReInit()
   ...: len(list(ex))
Out[5]: 6
```

An explorer visits a shared sub-shape once for every shape it belongs to: each edge of a box is part of two faces. `TopExp.MapShapes` collects each sub-shape once (OCCT's shape maps compare with `IsSame`):

```python
In [6]: edges = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
   ...: TopExp.MapShapes_s(box, EDGE, edges)
   ...: len(list(TopExp_Explorer(box, EDGE))), edges.Size()
Out[6]: (24, 12)
```

An iterator over an NCollection holds a position inside it. While the iterator is referenced, the container refuses what would free that position -- a `Clear()`, a `Remove()`, and for a hashed map (`NCollection_Map`, `DataMap`, `DoubleMap`) an insert, which can grow the table -- with `BufferError`, like the views [above](#numpy-zero-copy-support). In a `for` loop that is the loop itself; an `Iterator` kept in a variable blocks until it is deleted. Removing through the iterator itself, OCCT's own removal loop, stays allowed:

```python
In [7]: from nanocct.NCollection import NCollection_List
   ...: l = NCollection_List[int]()
   ...: for i in range(4):
   ...:     l.Append(i)
   ...: it = NCollection_List[int].Iterator(l)
   ...: while it.More():
   ...:     if it.Value() % 2 == 1:
   ...:         l.Remove(it)
   ...:     else:
   ...:         it.Next()
   ...: list(l)
Out[7]: [0, 2]

In [8]: try:
   ...:     l.Clear()
   ...: except BufferError as e:
   ...:     err = type(e).__name__
   ...: err
Out[8]: 'BufferError'

In [9]: del it
   ...: l.Clear()
   ...: l.Size()
Out[9]: 0
```

### Timings

A compound of 100 boxes (600 faces, 2400 edge visits, 1200 distinct edges):

```python
In [7]: from nanocct.BRep import BRep_Builder
   ...: from nanocct.TopoDS import TopoDS_Compound
   ...:
   ...: builder, comp = BRep_Builder(), TopoDS_Compound()
   ...: builder.MakeCompound(comp)
   ...: for i in range(100):
   ...:     builder.Add(comp, BRepPrimAPI_MakeBox(1, 1, 1).Shape())

In [8]: %%timeit
   ...: ex, out = TopExp_Explorer(comp, EDGE), []
   ...: while ex.More():
   ...:     out.append(ex.Current())
   ...:     ex.Next()
155 μs ± 929 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [9]: %timeit [e for e in TopExp_Explorer(comp, EDGE)]
122 μs ± 781 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [10]: %timeit list(TopExp_Explorer(comp, EDGE))
114 μs ± 616 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [11]: %%timeit
    ...: m = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
    ...: TopExp.MapShapes_s(comp, EDGE, m)
    ...: list(m)
106 μs ± 735 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

| Statement                                                                                                         | Timing                              |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `ex, out = TopExp_Explorer(comp, EDGE), []; while ex.More(): out.append(ex.Current()); ex.Next()`                 | 155&nbsp;μs&nbsp;±&nbsp;929&nbsp;ns |
| `[e for e in TopExp_Explorer(comp, EDGE)]`                                                                        | 122&nbsp;μs&nbsp;±&nbsp;781&nbsp;ns |
| `list(TopExp_Explorer(comp, EDGE))`                                                                               | 114&nbsp;μs&nbsp;±&nbsp;616&nbsp;ns |
| `m = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher](); TopExp.MapShapes_s(comp, EDGE, m); list(m)` | 106&nbsp;μs&nbsp;±&nbsp;735&nbsp;ns |

A `for` loop or `list()` is about 20–25 % faster than a hand-written `More()`/`Next()` loop. `TopExp.MapShapes` is the fastest here, although it also removes the duplicates: the traversal runs in one C++ call, and it returns 1 200 instead of 2 400 shapes.

## numpy zero-copy support in detail

**Binding rule: R-VIEW ([Design 2c](Design.md#2c-python-additions))**

### Support for the numpy array protocol

The nanocct generator gives `NCollection_Array1` and `NCollection_Array2` (and their `HArray1`/`HArray2` variants) numpy's array protocol, `__array__`, for every element type that is a packed run of numpy scalars: the C++ scalars `double`, `float`, `int`, `bool`, `unsigned char`, `gp_Pnt`, `gp_Vec`, `gp_Dir`, `gp_XYZ`, their 2d counterparts, `Poly_Triangle` and the `NCollection_Vec2/3/4` types. `Poly_ArrayOfNodes`, `Poly_ArrayOfUVNodes`, `Image_PixMap` and `NCollection_Buffer` have it too. This allows to access large C++ arrays from Python with zero-copy:

- `np.asarray(a)` is a view of OCCT's own memory: no copy, and writes go straight into the OCCT array.
- `np.array(a)` is an independent copy.

Collections without a packed element type (an `NCollection_Array1` of `TopoDS_Shape`, maps, lists, sequences) have no `__array__`.

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...: from nanocct.gp import gp_Vec
   ...: import numpy as np
   ...:
   ...: a = NCollection_Array1[gp_Vec](1, 3)
   ...:
   ...: a.SetValue(1, gp_Vec(1, 0, 0))
   ...: a.SetValue(2, gp_Vec(0, 1, 0))
   ...: a.SetValue(3, gp_Vec(0, 0, 1))

In [2]: v = np.asarray(a)
   ...: v
Out[2]:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

In [3]: v[0, 0] = 42.0
   ...: a.Value(1).X()
Out[3]: 42.0

In [4]: c = np.array(a)
   ...: c[0, 0] = 7.0
   ...: a.Value(1).X()
Out[4]: 42.0
```

Let's make a little benchmark

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...: from nanocct.gp import gp_Vec
   ...: import numpy as np
   ...:
   ...: N = 1000000
   ...: a = NCollection_Array1[gp_Vec](1, N)
   ...:
   ...: for i in range(1, N + 1):
   ...:     a.SetValue(i, gp_Vec(i, i/10, i/100))
   ...:
```

To access the vectors as python tuples, one uses:

```python
In [2]: %timeit [a.Value(i).Coord() for i in range(1, N + 1)]
99.9 ms ± 2.47 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [3]: %timeit np.asarray(a)  # zero copy
233 ns ± 1.91 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [4]: %timeit np.array(a)
328 μs ± 6.35 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

| Statement                                       | Timing            |
| ----------------------------------------------- | ----------------- |
| `[a.Value(i).Coord() for i in range(1, N + 1)]` | 99.9 ms ± 2.47 ms |
| `np.array(a)`                                   | 328 μs ± 6.35 μs  |
| `np.asarray(a)` (zero copy)                     | 233 ns ± 1.91 ns  |

`np.asarray(a)` only creates the view, so its time does not depend on the size of the array; `np.array(a)` copies all 24 MB.

Finally, compare some values:

```python
In [5]: p = [a.Value(i).Coord() for i in range(1, N + 1)]
   ...: p[0:3]
Out[5]: [(1.0, 0.1, 0.01), (2.0, 0.2, 0.02), (3.0, 0.3, 0.03)]

In [6]: q = np.asarray(a)
   ...: q[0:3]
Out[6]:
array([[1.  , 0.1 , 0.01],
       [2.  , 0.2 , 0.02],
       [3.  , 0.3 , 0.03]])
```

### Special case: Triangulations

A `Poly_Triangulation` holds four arrays: nodes, triangles, UV nodes and normals. OCCT's own accessors `InternalNodes()`, `InternalTriangles()`, `InternalUVNodes()` and `InternalNormals()` return references to the triangulation's storage, and `np.asarray` turns each into a zero-copy view.

```python
In [1]: import numpy as np
   ...: from nanocct.BRep import BRep_Tool
   ...: from nanocct.BRepMesh import BRepMesh_IncrementalMesh
   ...: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.TopAbs import TopAbs_ShapeEnum
   ...: from nanocct.TopExp import TopExp_Explorer
   ...: from nanocct.TopLoc import TopLoc_Location
   ...: import nanocct.TopoDS as TopoDS
   ...:
   ...: box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
   ...: BRepMesh_IncrementalMesh(box, 0.1)
   ...: face = TopoDS.Face(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE).Current())
   ...: tri = BRep_Tool.Triangulation_s(face, TopLoc_Location())

In [2]: tri.NbNodes(), tri.NbTriangles()
Out[2]: (4, 2)

In [3]: nodes = np.asarray(tri.InternalNodes())
   ...: nodes
Out[3]:
array([[ 0.,  0.,  0.],
       [ 0.,  0., 30.],
       [ 0., 20.,  0.],
       [ 0., 20., 30.]])

In [4]: tris = np.asarray(tri.InternalTriangles())
   ...: tris
Out[4]:
array([[2, 1, 3],
       [2, 3, 4]], dtype=int32)
```

The triangle indices are OCCT's and therefore **1-based**. To correlate them correctly, subtract 1 to index the nodes, e.g. to get the corner coordinates of every triangle:

```python
In [5]: nodes[tris - 1][0]  # align to the 1-based C++ indices
Out[5]:
array([[ 0.,  0., 30.],
       [ 0.,  0.,  0.],
       [ 0., 20.,  0.]])
```

UV nodes and normals are optional. When a triangulation has none, the array is empty, and OCCT's `HasUVNodes()`/`HasNormals()` tell whether they are there:

```python
In [6]: tri.HasUVNodes(), tri.HasNormals()
Out[6]: (True, False)

In [7]: np.asarray(tri.InternalUVNodes())
Out[7]:
array([[  0.,   0.],
       [ 30.,   0.],
       [  0., -20.],
       [ 30., -20.]])

In [8]: np.asarray(tri.InternalNormals())
Out[8]: array([], shape=(0, 3), dtype=float32)
```

Only a non-const reference is zero-copy. An OCCT accessor that returns a `const` reference, such as `Triangles()`, is bound as a copy, so `np.asarray` on it views that copy and writes never reach the triangulation:

```python
In [9]: copy = np.asarray(tri.Triangles())
   ...: copy[0] = [1, 1, 1]
   ...: tri.Triangle(1).Get()
Out[9]: (2, 1, 3)

In [10]: view = np.asarray(tri.InternalTriangles())
    ...: view[0] = [1, 1, 1]
    ...: tri.Triangle(1).Get()
Out[10]: (1, 1, 1)
```

## Handling of primitive types passed by reference

**Binding rules: R-OUT, R-COLLISION ([Design 2a](Design.md#2a-naming-conventions)), R-INOUT ([Design 6](Design.md#6-binding-rules-11-and-the-documented-deviations))**

A non-const reference to a number, a `bool`, an enum or a `handle<T>` is an output in OCCT: nanocct drops it from the parameters and returns it, after the C++ return value if there is one. A reference to a class (`gp_Pnt&`) stays a parameter and is filled in place.

| C++&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Python | real example |
| --- | --- | --- |
| `void f(int a, double& b, double c)`: void, one output | `b = f(a, c)`: the bare value | `extrema.ParOnEdgeS1(1) -> float` |
| `void f(int a, double& b, double& c, int& d)`: void, several outputs | `b, c, d = f(a)`: a tuple in C++ order | `extrema.ParOnFaceS1(1) -> tuple[float, float]` |
| `bool f(int a, double& b, double c)`: non-void, one output | `ok, b = f(a, c)`: a tuple, the return value first | `math_Function.Value(x) -> tuple[bool, float]` |
| `R f(E, double& first, double& last)`: non-void, several outputs | `r, first, last = f(E)` | `BRep_Tool.Curve_s(edge) -> tuple[Geom_Curve, float, float]` |
| `void f(double& x, double& y, double& z)`: read and written (listed in `overrides.toml [inout]`) | `x, y, z = f(x, y, z)`: kept as parameters and returned | `trsf.Transforms(1.0, 1.0, 1.0) -> tuple[float, float, float]` |
| two overloads identical once the outputs are removed | `Name__<types of the outputs>`, e.g. `x, y, z = pnt.Coord__float__float__float()` | `gp_Pnt.Coord__float__float__float()` next to `gp_Pnt.Coord() -> gp_XYZ`; `GeomAPI_IntCS.Parameters__float__float__float` |

## Mutable primitive references

**Binding rule: R-REF-PRIMITIVE ([Design 2c](Design.md#2c-python-additions))**

Many OCCT settings are a method that returns a writable reference to a number, e.g. `int& ShapeFix_Face::FixWireMode()`. In C++ the value is set by assigning to the result, `face.FixWireMode() = 0;`. Python has no references to numbers, so nanocct keeps the getter under its OCCT name and adds a setter: `Set<Name>`, with a `Change` prefix dropped (`ChangeValue` → `SetValue`), unless OCCT already has a method of that name. Its docstring starts with "Python addition".

```python
In [1]: from nanocct.ShapeFix import ShapeFix_Face
   ...: from nanocct.math import math_Matrix
   ...:
   ...: face = ShapeFix_Face()
   ...: face.FixWireMode()
Out[1]: -1

In [2]: face.SetFixWireMode(0)
   ...: face.FixWireMode()
Out[2]: 0
```

Assigning the getter's result to a variable only changes the variable: `x = face.FixWireMode(); x = 1` leaves the face untouched.

The same rule covers references with arguments, like `double& math_Matrix::Value(int, int)`, and the C++ operators `()` and `[]`: their setter is `__setitem__`, with a tuple for several indices.

```python
In [3]: m = math_Matrix(1, 2, 1, 2, 0.0)
   ...: m.SetValue(1, 2, 5.0)
   ...: m.Value(1, 2)
Out[3]: 5.0

In [4]: m[(2, 1)] = 7.0
   ...: m(2, 1), m.Value(2, 1)
Out[4]: (7.0, 7.0)
```

## Operators

**Binding rules: R-OPERATOR, R-IOP, R-FREE-OP, R-STR ([Design 2c](Design.md#2c-python-additions))**

C++ operators become the matching Python special methods, and they keep OCCT's meaning:

| Types                                           | C++                                                   | Python                     | OCCT's meaning                                                                                                           |
| ----------------------------------------------- | ----------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `gp_Vec v, v1, v2`                              | `v1 + v2`, `v * 2.0`, `-v`                            | `v1 + v2`, `v * 2.0`, `-v` | `Added`, `Multiplied`, `Reversed` (a `gp_Vec`)                                                                           |
| `gp_Vec v`                                      | `2.0 * v` (a free `operator*(double, const gp_Vec&)`) | `2.0 * v`                  | `Multiplied` (a `gp_Vec`)                                                                                                |
| `gp_Vec v1, v2`                                 | `v1 * v2`                                             | `v1 * v2`                  | `Dot`: a `double` / `float`, not an element-wise product                                                                 |
| `gp_Vec v1, v2`                                 | `v1 ^ v2`                                             | `v1 ^ v2`                  | `Crossed` (a `gp_Vec`)                                                                                                   |
| `gp_Vec v1, v2`                                 | `v1 += v2` (returns `void`)                           | `v1 += v2`                 | `Add`: changes `v1`, which stays the same object                                                                         |
| `TopoDS_Shape s1, s2`                           | `s1 == s2`                                            | `s1 == s2`                 | `IsEqual`: the same shape, location and orientation, not the same geometry, see [Equality](#equality-in-occt-and-python) |
| `math_Matrix m`, `NCollection_Array1<double> a` | `m(1, 1)`, `a[i]`                                     | `m(1, 1)`, `a[i]`          | OCCT's `operator()`, `operator[]`                                                                                        |
| `math_Matrix m`                                 | `std::cout << m`                                      | `str(m)`, `print(m)`       | OCCT's own text; `repr(m)` stays Python's default                                                                        |

```python
In [1]: from nanocct.gp import gp_Pnt, gp_Vec
   ...: from nanocct.math import math_Matrix
   ...: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...:
   ...: v1, v2 = gp_Vec(1, 2, 3), gp_Vec(4, 5, 6)
   ...: (v1 + v2).Coord(), (2.0 * v1).Coord()
Out[1]: ((5.0, 7.0, 9.0), (2.0, 4.0, 6.0))

In [2]: v1 * v2, (v1 ^ v2).Coord()
Out[2]: (32.0, (-3.0, 6.0, -3.0))

In [3]: v = gp_Vec(1, 1, 1)
   ...: before = id(v)
   ...: v += v2
   ...: v.Coord(), id(v) == before
Out[3]: ((5.0, 6.0, 7.0), True)

In [4]: box = BRepPrimAPI_MakeBox(1, 1, 1).Shape()
   ...: box == box, box == BRepPrimAPI_MakeBox(1, 1, 1).Shape()
Out[4]: (True, False)

In [5]: str(math_Matrix(1, 2, 1, 2, 1.5)).splitlines()[0]
Out[5]: 'math_Matrix of RowNumber = 2 and ColNumber = 2'
```

A class without an OCCT `operator==` compares by identity, as any Python object does. `gp_Pnt` is one of them; OCCT compares points with a tolerance:

```python
In [6]: p1, p2 = gp_Pnt(1, 2, 3), gp_Pnt(1, 2, 3)
   ...: p1 == p2, p1.IsEqual(p2, 1e-7)
Out[6]: (False, True)
```

## Equality in OCCT and Python

### Python level

| Term     | Test      | Meaning                                                                                                                                                |
| -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| identity | `a is b`  | the same _Python object_. nanocct creates a new Python object for every value it returns, so a face fetched twice is two objects: `f2 is f` → `False`. |
| equality | `a == b`  | whatever the class's `__eq__` says. A class without `__eq__` falls back to identity.                                                                   |
| hash     | `hash(a)` | a dict or set first compares hashes, then `==`. Python requires that `a == b` implies `hash(a) == hash(b)`.                                            |

### OCCT, for shapes

A `TopoDS_Shape` is a triple: a pointer to the underlying topology (the `TShape`), a `Location` (a placement) and an `Orientation`.

| Term                                          | Compares                                                                                   |
| --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `IsPartner`                                   | the same `TShape`                                                                          |
| `IsSame`                                      | the same `TShape` and `Location`; orientation may differ                                   |
| `IsEqual` = `operator==`                      | the same `TShape`, `Location` **and** `Orientation`                                        |
| `std::hash<TopoDS_Shape>`                     | `TShape` pointer and `Location`, _not_ orientation, so it fits both `IsSame` and `IsEqual` |
| `TopTools_ShapeMapHasher` (OCCT's shape maps) | that hash, with **`IsSame`** as equality                                                   |

### C++ and Python side by side

Everything except `is` is OCCT's own API, under the same name in both languages; the operators call OCCT's methods.

| Name           | C++ (OCCT)                                                                                    | Python (nanocct)                                                                                                                                                                                                      |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `is`           | — (closest: comparing addresses, `&a == &b`)                                                  | Python's own operator: the same Python object                                                                                                                                                                         |
| `IsPartner`    | `TopoDS_Shape::IsPartner`                                                                     | `f.IsPartner(g)`                                                                                                                                                                                                      |
| `IsSame`       | `TopoDS_Shape::IsSame`                                                                        | `f.IsSame(g)`                                                                                                                                                                                                         |
| `IsEqual`      | `TopoDS_Shape::IsEqual`                                                                       | `f.IsEqual(g)`                                                                                                                                                                                                        |
| `IsNotEqual`   | `TopoDS_Shape::IsNotEqual`                                                                    | `f.IsNotEqual(g)`                                                                                                                                                                                                     |
| `==`           | `operator==`, defined as `IsEqual`                                                            | `f == g`, which calls `IsEqual`                                                                                                                                                                                       |
| `!=`           | `operator!=`, defined as `IsNotEqual`                                                         | `f != g`, which calls `IsNotEqual`                                                                                                                                                                                    |
| hash           | `std::hash<TopoDS_Shape>`, used by `std::unordered_*` containers, an unsigned 64-bit `size_t` | `hash(f)`: the same 64-bit value, read as a signed integer (a value ≥ 2⁶³ shows as negative; CPython reports the one value −1 as −2). It hashes the `TShape` pointer, so it changes from run to run in both languages |
| map membership | `Contains` of an OCCT map with `TopTools_ShapeMapHasher`                                      | `m.Contains(g)`                                                                                                                                                                                                       |

Compared with face `f` of a box:

| `g`, compared with `f`              | `g is f` | `IsPartner` | `IsSame` | `IsEqual`/`==` | same hash |
| ----------------------------------- | -------- | ----------- | -------- | -------------- | --------- |
| the same face, fetched again        | False    | True        | True     | True           | True      |
| `f.Reversed()`                      | False    | True        | True     | False          | True      |
| `f.Moved(loc)`                      | False    | True        | False    | False          | False     |
| the face of a second, identical box | False    | False       | False    | False          | False     |

### Shapes as dict keys and in OCCT maps

A Python dict and OCCT's shape maps (`NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]` and the other `TopTools_ShapeMapHasher` maps) both look up in two steps, first the hash, then an equality test, but not the same one:

| Step        | Python dict (`g in d`)                                                  | OCCT map (`m.Contains(g)`)                                 |
| ----------- | ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1. hash     | `std::hash<TopoDS_Shape>`: `TShape` and `Location`, not the orientation | the same hash (`TopTools_ShapeMapHasher` uses `std::hash`) |
| 2. equality | `==`, i.e. `IsEqual`: the orientation counts                            | `IsSame`: the orientation does not count                   |

So a dict finds `g` if `g == f`, and an OCCT map finds it if `g.IsSame(f)`: a reversed face is a different dict key but the same map entry. A moved face changes the `Location`, which is part of the hash, so neither finds it.

### OCCT, for points

| Term                     | Compares                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------ |
| `gp_Pnt.IsEqual(p, tol)` | distance ≤ `tol`                                                                     |
| `std::equal_to<gp_Pnt>`  | each coordinate within `Epsilon(x)`, about one unit in the last place (`gp_Pnt.hxx`) |
| `std::hash<gp_Pnt>`      | the exact bits of the three doubles                                                  |


## Strings

Every C++ text type of OCCT is a Python `str`: `const char*` (`Standard_CString`), `std::string_view`, the UTF-16 `const char16_t*` (`Standard_ExtString`), and the single characters `char`, `char16_t` and `char32_t`. A `str` goes to C++ as UTF-8 for the 8-bit types and as UTF-16 for `char16_t`.

Where OCCT overloads a method for several of these types, Python cannot tell them apart, and nanobind calls the first overload that accepts a `str`. nanocct registers them in the order C++ itself picks for a narrow string literal `"..."`: `const char*` first, then `std::string_view`, then `const char16_t*`, then the single characters. An overload that can never be reached this way is not bound, and the generator reports it ([Design 6](Design.md#6-binding-rules-11-and-the-documented-deviations), R-WIDTH, R-UNREACHABLE).

For most classes this makes no difference, since all the overloads store the same text. It matters for `TCollection_ExtendedString`: exactly as in C++, its `const char*` constructor reads one byte per character unless `theIsMultiByte` is `True`:

```python
In [1]: from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString

In [2]: TCollection_AsciiString("Größe").ToCString(), TCollection_AsciiString("Größe").Length()
Out[2]: ('Größe', 7)

In [3]: TCollection_ExtendedString("Größe").ToExtString()
Out[3]: 'GrÃ¶Ã\x9fe'

In [4]: TCollection_ExtendedString("Größe", True).ToExtString()
Out[4]: 'Größe'

In [5]: TCollection_ExtendedString(TCollection_AsciiString("Größe")).ToExtString()
Out[5]: 'Größe'
```

`TCollection_AsciiString` holds the UTF-8 bytes (7 for the 5 characters), and `Length()` counts them. So for text that is not ASCII, pass `True` to `TCollection_ExtendedString`, or go through a `TCollection_AsciiString`, whose conversion constructor defaults to multi-byte.

A single `char` is a one-character `str` too, converted as UTF-8 -- so it holds ASCII only. `TCollection_AsciiString.Value(i)` returns the byte at position `i`, and inside a character that takes several UTF-8 bytes that byte is not a character of its own: Python raises `UnicodeDecodeError` (C++ would return the raw byte). Likewise, a `char` parameter accepts only ASCII. For text that is not ASCII, use the string APIs (`ToCString()`), or `TCollection_ExtendedString`, whose `Value(i)` is a `char16_t`, one whole character:

```python
In [6]: s = TCollection_AsciiString("Größe")
   ...: s.Value(1)
Out[6]: 'G'

In [7]: try:
   ...:     s.Value(3)
   ...: except UnicodeDecodeError as e:
   ...:     err = e
   ...: type(err).__name__, err.reason
Out[7]: ('UnicodeDecodeError', 'unexpected end of data')

In [8]: TCollection_ExtendedString("Größe", True).Value(3)
Out[8]: 'ö'
```

## Handling of istream and ostream

**Binding rules: R-STREAM-OUT, R-STREAM-IN ([Design 6](Design.md#6-binding-rules-11-and-the-documented-deviations))**

```python
In [1]: import json
   ...: from nanocct.BRepTools import BRepTools
   ...: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct import TopoDS, TopExp, TopAbs
   ...: 
   ...: s = BRepPrimAPI_MakeBox(1, 2, 3).Shape()
   ...: f = TopoDS.Face(TopExp.TopExp_Explorer(s, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE).Current())
   ...: 
   ...: def dump(shape):
   ...:     return json.loads(f"{{{shape.DumpJson()}}}")
```

### Dumping shapes to json

```python
In [2]: dump(s)
Out[2]: 
{'className': 'TopoDS_Shape',
 'TShape': {'className': 'TopoDS_TShape',
  'this': '0xxa62fb9c40',
  'ShapeType': 2,
  'NbChildren': 1,
  'State': 50,
  'Free': 1,
  'Locked': 0,
  'Modified': 1,
  'Checked': 0,
  'Orientable': 0,
  'Closed': 0,
  'Infinite': 0,
  'Convex': 0},
 'Location': {'className': 'TopLoc_Location',
  'Transformation': {'Location': [0, 0, 0],
   'Matrix': [1, 0, 0, 0, 1, 0, 0, 0, 1],
   'shape': 0,
   'scale': 1},
  'IsIdentity': 1},
 'Orient': 0}

In [3]: dump(f)
Out[3]: 
{'className': 'TopoDS_Shape',
 'TShape': {'className': 'TopoDS_TShape',
  'this': '0xxa5d4c2800',
  'ShapeType': 4,
  'NbChildren': 1,
  'State': 228,
  'Free': 0,
  'Locked': 0,
  'Modified': 1,
  'Checked': 1,
  'Orientable': 1,
  'Closed': 0,
  'Infinite': 0,
  'Convex': 0,
  'Surface': {'className': 'Geom_Geometry',
   'pos': {'Location': [0, 0, 0],
    'Direction': [1, 0, 0],
    'XDirection': [0, 0, 1],
    'YDirection': [0, -1, 0]}},
  'Location': {'className': 'TopLoc_Location',
   'Transformation': {'Location': [0, 0, 0],
    'Matrix': [1, 0, 0, 0, 1, 0, 0, 0, 1],
    'shape': 0,
    'scale': 1},
   'IsIdentity': 1},
  'Tolerance': 1e-07,
  'NaturalRestriction': 0},
 'Location': {'className': 'TopLoc_Location',
  'Transformation': {'Location': [0, 0, 0],
   'Matrix': [1, 0, 0, 0, 1, 0, 0, 0, 1],
   'shape': 0,
   'scale': 1},
  'IsIdentity': 1},
 'Orient': 1}
```

### Writing to memory

Without a file name, the text is returned as a `str`:

```python
In [4]: BRepTools.Write_s(s)
Out[4]: '\nCASCADE Topology V3, (c) Open Cascade\nLocations 0\nCurve2ds 24\n1 0 0 1 0 \n1 0 0 1 0 \n1 3 0 0 -1 \n1 0 0 0 1 \n1 0 -2 1 0 \n1 0 0 1 0 \n1 0 0 0 -1 \n1 0 0 0 1 \n1 0 0 1 0 \n1 0 1 1 0 \n1 3 0 0 -1 \n1 1 0 0 1 \n1 0 -2 1 0 \n1 0 1 1 0 \n1 0 0 0 -1 \n1 1 0 0 1 \n1 0 0 0 1 \n1 0 0 1 0 \n1 3 0 0 1 \n1 0 0 1 0 \n1 0 0 0 1 \n1 0 2 1 0 \n1 3 0 0 1 \n1 0 2 1 0 \nCurves 12\n1 0 0 0 0 0 1 \n1 0 0 3 -0 1 0 \n1 0 2 0 0 0 1 \n1 0 0 0 -0 1 0 \n1 1 0 0 0 0 1 \n1 1 0 3 -0 1 0 \n1 1 2 0 0 0 1 \n1 1 0 0 -0 1 0 \n1 0 0 0 1 0 -0 \n1 0 0 3 1 0 -0 \n1 0 2 0 1 0 -0 \n1 0 2 3 1 0 -0 \nPolygon3D 0\nPolygonOnTriangulations 0\nSurfaces 6\n1 0 0 0 1 0 -0 0 0 1 0 -1 0 \n1 0 0 0 -0 1 0 0 0 1 1 0 -0 \n1 0 0 3 0 0 1 1 0 -0 -0 1 0 \n1 0 2 0 -0 1 0 0 0 1 1 0 -0 \n1 0 0 0 0 0 1 1 0 -0 -0 1 0 \n1 1 0 0 1 0 -0 0 0 1 0 -1 0 \nTriangulations 0\n\nTShapes 34\nVe\n1e-07\n0 0 3\n0 0\n\n0101101\n*\nVe\n1e-07\n0 0 0\n0 0\n\n0101101\n*\nEd\n 1e-07 1 1 0\n1  1 0 0 3\n2  1 1 0 0 3\n2  2 2 0 0 3\n0\n\n0101000\n-34 0 +33 0 *\nVe\n1e-07\n0 2 3\n0 0\n\n0101101\n*\nEd\n 1e-07 1 1 0\n1  2 0 0 2\n2  3 1 0 0 2\n2  4 3 0 0 2\n0\n\n0101000\n-31 0 +34 0 *\nVe\n1e-07\n0 2 0\n0 0\n\n0101101\n*\nEd\n 1e-07 1 1 0\n1  3 0 0 3\n2  5 1 0 0 3\n2  6 4 0 0 3\n0\n\n0101000\n-31 0 +29 0 *\nEd\n 1e-07 1 1 0\n1  4 0 0 2\n2  7 1 0 0 2\n2  8 5 0 0 2\n0\n\n0101000\n-29 0 +33 0 *\nWi\n\n0101100\n-32 0 -30 0 +28 0 +27 0 *\nFa\n0  1e-07 1 0\n\n0111000\n+26 0 *\nVe\n1e-07\n1 0 3\n0 0\n\n0101101\n*\nVe\n1e-07\n1 0 0\n0 0\n\n0101101\n*\nEd\n 1e-07 1 1 0\n1  5 0 0 3\n2  9 6 0 0 3\n2  10 2 0 0 3\n0\n\n0101000\n-24 0 +23 0 *\nVe\n1e-07\n1 2 3\n0 0\n\n0101101\n*\nEd\n 1e-07 1 1 0\n1  6 0 0 2\n2  11 6 0 0 2\n2  12 3 0 0 2\n0\n\n0101000\n-21 0 +24 0 *\nVe\n1e-07\n1 2 0\n0 0\n\n0101101\n*\nEd\n 1e-07 1 1 0\n1  7 0 0 3\n2  13 6 0 0 3\n2  14 4 0 0 3\n0\n\n0101000\n-21 0 +19 0 *\nEd\n 1e-07 1 1 0\n1  8 0 0 2\n2  15 6 0 0 2\n2  16 5 0 0 2\n0\n\n0101000\n-19 0 +23 0 *\nWi\n\n0101100\n-22 0 -20 0 +18 0 +17 0 *\nFa\n0  1e-07 6 0\n\n0111000\n+16 0 *\nEd\n 1e-07 1 1 0\n1  9 0 0 1\n2  17 2 0 0 1\n2  18 5 0 0 1\n0\n\n0101000\n-23 0 +33 0 *\nEd\n 1e-07 1 1 0\n1  10 0 0 1\n2  19 2 0 0 1\n2  20 3 0 0 1\n0\n\n0101000\n-24 0 +34 0 *\nWi\n\n0101100\n-14 0 -22 0 +13 0 +32 0 *\nFa\n0  1e-07 2 0\n\n0111000\n+12 0 *\nEd\n 1e-07 1 1 0\n1  11 0 0 1\n2  21 4 0 0 1\n2  22 5 0 0 1\n0\n\n0101000\n-19 0 +29 0 *\nEd\n 1e-07 1 1 0\n1  12 0 0 1\n2  23 4 0 0 1\n2  24 3 0 0 1\n0\n\n0101000\n-21 0 +31 0 *\nWi\n\n0101100\n-10 0 -18 0 +9 0 +28 0 *\nFa\n0  1e-07 4 0\n\n0111000\n+8 0 *\nWi\n\n0101100\n-27 0 -10 0 +17 0 +14 0 *\nFa\n0  1e-07 5 0\n\n0111000\n+6 0 *\nWi\n\n0101100\n-30 0 -9 0 +20 0 +13 0 *\nFa\n0  1e-07 3 0\n\n0111000\n+4 0 *\nSh\n\n0101100\n-25 0 +15 0 -11 0 +7 0 -5 0 +3 0 *\nSo\n\n1100000\n+2 0 *\n\n+1 0 '
```

With filename parameter written to the file:

```python
In [5]: BRepTools.Write_s(s, "b.brep")
Out[5]: True

In [6]: %cat b.brep
DBRep_DrawableShape

CASCADE Topology V3, (c) Open Cascade
Locations 0
Curve2ds 24
1 0 0 1 0 
1 0 0 1 0 
1 3 0 0 -1 
1 0 0 0 1 
...
```

### Reading from memory

A stream parameter takes a text file-like object, so text in memory is wrapped in `io.StringIO`. A plain `str` in its place is taken as a file name: it selects the file-path overload, which finds no such file and returns `False`.

```python
In [7]: import io
   ...: from nanocct.BRep import BRep_Builder
   ...: from nanocct.TopoDS import TopoDS_Shape
   ...:
   ...: text = BRepTools.Write_s(s)
   ...: back = TopoDS_Shape()
   ...: BRepTools.Read_s(back, io.StringIO(text), BRep_Builder())
   ...: back.ShapeType()
Out[7]: TopAbs_ShapeEnum.TopAbs_SOLID

In [8]: BRepTools.Read_s(TopoDS_Shape(), text, BRep_Builder())
Out[8]: False
```

### Binary formats

The packages whose streams carry a binary format use `bytes` instead of `str`: `BinTools` (the binary BRep format) and the OCAF document streams (`PCDM`, `CDF`, the `Bin*` and `Xml*` drivers, `DE`), listed in `generator/overrides.toml` `[stream] binary_packages`. The written data is returned as `bytes`, and a binary file-like object such as `io.BytesIO` is read.

```python
In [9]: from nanocct.BinTools import BinTools
   ...:
   ...: data = BinTools.Write_s(s)
   ...: len(data), data[:24]
Out[9]: (4494, b'\nOpen CASCADE Topology V')

In [10]: back = TopoDS_Shape()
    ...: BinTools.Read_s(back, io.BytesIO(data))
    ...: back.ShapeType()
Out[10]: TopAbs_ShapeEnum.TopAbs_SOLID
```

## Enums

**Binding rules: R-ENUM, R-ANON-ENUM ([Design 2c](Design.md#2c-python-additions))**

OCCT's enums are Python `enum.IntEnum` classes. As in C++, the enumerators of an unscoped enum are also names in the module (`TopAbs.TopAbs_FACE`), and they are integers. As in C++, the conversion goes one way only: an OCCT parameter of an enum type takes its enumerators, not an `int` or a `bool` (`TypeError`); `TopAbs_ShapeEnum(4)` turns an `int` into the enumerator. An `enum class` stays nested in its class (`gp_Dir.D.NZ`).

```python
In [1]: from nanocct.TopAbs import TopAbs_ShapeEnum, TopAbs_FACE
   ...: from nanocct.Font import Font_FontAspect, Font_FA_Bold

In [2]: TopAbs_FACE is TopAbs_ShapeEnum.TopAbs_FACE, int(TopAbs_FACE), TopAbs_FACE == 4
Out[2]: (True, 4, True)

In [3]: TopAbs_FACE.name, TopAbs_ShapeEnum(4), TopAbs_ShapeEnum["TopAbs_EDGE"]
Out[3]: ('TopAbs_FACE', TopAbs_ShapeEnum.TopAbs_FACE, TopAbs_ShapeEnum.TopAbs_EDGE)

In [4]: [m.name for m in TopAbs_ShapeEnum][:3]
Out[4]: ['TopAbs_COMPOUND', 'TopAbs_COMPSOLID', 'TopAbs_SOLID']
```

OCCT's alias enumerators, like `Font_FA_Bold = Font_FontAspect_Bold`, are equal to the enumerator they stand for but a separate object, so compare enums with `==`, not `is`:

```python
In [5]: Font_FA_Bold == Font_FontAspect.Font_FontAspect_Bold, Font_FA_Bold is Font_FontAspect.Font_FontAspect_Bold
Out[5]: (True, False)
```

## Exceptions

**Design: [4.2](Design.md#42-three-kinds-of-c-types)**

OCCT's C++ exceptions arrive in Python as exception classes with the same names and the same hierarchy as in C++, with OCCT's own message. `Standard_Failure` is the root of all of them and derives from Python's `RuntimeError`. They are not mapped to Python's built-in categories: `Standard_OutOfRange` is not an `IndexError`, so catch OCCT's classes (or `Standard_Failure`).

```python
In [1]: from nanocct.gp import gp_Dir, gp_Pnt
   ...: from nanocct.gce import gce_MakeLin
   ...: from nanocct.Standard import Standard_Failure
   ...: from nanocct.StdFail import StdFail_NotDone

In [2]: try:
   ...:     gp_Dir(0, 0, 0)
   ...: except Standard_Failure as e:
   ...:     err = e
   ...: type(err).__name__, str(err)
Out[2]: ('Standard_ConstructionError', 'gp_Dir() - input vector has zero norm')

In [3]: [c.__name__ for c in type(err).__mro__][:4]
Out[3]: ['Standard_ConstructionError', 'Standard_DomainError', 'Standard_Failure', 'RuntimeError']
```

Many OCCT algorithms report a failure through a status first, and raise only when the missing result is asked for:

```python
In [4]: mk = gce_MakeLin(gp_Pnt(1, 1, 1), gp_Pnt(1, 1, 1))
   ...: mk.IsDone(), mk.Status()
Out[4]: (False, gce_ErrorType.gce_ConfusedPoints)

In [5]: try:
   ...:     mk.Value()
   ...: except StdFail_NotDone as e:
   ...:     msg = str(e)
   ...: msg
Out[5]: 'gce_MakeLin::Value() - no result'
```

### Null handles

A handle that OCCT returns can be null, and nanocct turns a null handle into `None`. The type stubs do not say so: a handle result is typed as its class, not as `X | None`, because OCCT's headers do not say which methods can return a null handle -- most never do (`BRepBuilderAPI_MakeEdge.Edge()`), and `| None` on all of them would make a type checker demand a `None` check after every call. A type checker therefore accepts `curve.Value(0.5)` for a `curve` that is `None` at runtime. Where OCCT documents a null result, check it:

```python
In [1]: from nanocct.BRep import BRep_Builder, BRep_Tool
   ...: from nanocct.TopLoc import TopLoc_Location
   ...: from nanocct.TopoDS import TopoDS_Edge
   ...:
   ...: edge = TopoDS_Edge()
   ...: BRep_Builder().MakeEdge(edge)            # an edge without a 3D curve

In [2]: curve, first, last = BRep_Tool.Curve_s(edge, TopLoc_Location())
   ...: curve is None
Out[2]: True
```

A handle *parameter* is typed `X | None`: passing `None` hands OCCT a null handle, which is how OCCT removes a geometry (`BRep_TFace().Surface(None)`).

### Null shapes and labels

A shape, a label and a few other OCCT value classes can be null too, and ask `IsNull()`. nanocct makes a null one falsy, as a null handle (`None`) and an empty container already are: `__bool__` is `not IsNull()`. This applies to `TopoDS_Shape` (and every shape class derived from it), `TDF_Label`, `BRepGraph`, `StepData_SelectType`, `XCAFDoc_AssemblyItemId`, `Poly_MakeLoops.Link` and `PeriodicInterval`.

```python
In [1]: from nanocct.BRep import BRep_Builder
   ...: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.TopoDS import TopoDS_Compound, TopoDS_Shape

In [2]: shape = TopoDS_Shape()
   ...: bool(shape), shape.IsNull()
Out[2]: (False, True)

In [3]: box = BRepPrimAPI_MakeBox(1, 1, 1).Shape()
   ...: bool(box)
Out[3]: True
```

Truthiness means *not null*, not *has children*: an empty compound is not null, so it is true.

```python
In [4]: empty = TopoDS_Compound()
   ...: BRep_Builder().MakeCompound(empty)
   ...: bool(empty), empty.NbChildren()
Out[4]: (True, 0)
```

### When OCCT crashes instead

OCCT raises only where it checks. A handle or a class pointer accepts `None` (a null handle, a null pointer), because some OCCT methods take one on purpose (`BRep_TFace().Surface(None)` removes the surface). Where OCCT does not expect it, it dereferences the null pointer and the process ends with a segmentation fault, exactly as it does in C++. nanocct does not turn these into exceptions: OCCT's own mechanism for that (`OSD::SetSignal` with `OCC_CATCH_SIGNALS` around each call) works, but would add about 200 ns to every call, which costs about 18 ns today.

Python's `faulthandler` shows where it happened, at no cost until then. Take `edge.py`:

```python
from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeEdge


def make_edge(curve):
    return BRepBuilderAPI_MakeEdge(curve).Edge()


edge = make_edge(None)
```

`python edge.py` prints no more than the shell's `Segmentation fault`. With `python -X faulthandler edge.py` (or `PYTHONFAULTHANDLER=1`, or `faulthandler.enable()` in the code) the Python traceback is printed at the crash, and since Python 3.14 the C stack too, which names the OCCT function (shortened):

```text
Fatal Python error: Segmentation fault

Current thread 0x00000001ef4061c0 (most recent call first):
  File "edge.py", line 5 in make_edge
  File "edge.py", line 8 in <module>

Current thread's C stack trace (most recent call first):
  ...
  Binary file ".../nanocct/.dylibs/libTKTopAlgo.8.0.1.dylib", at _ZN16BRepLib_MakeEdgeC1ERKN11opencascade6handleI10Geom_CurveEE+0x54
  Binary file ".../nanocct/_TKTopAlgo.abi3.so", at PyInit__TKTopAlgo+0x8db8
```

`_ZN16BRepLib_MakeEdgeC1ERKN11opencascade6handleI10Geom_CurveEE` is `BRepLib_MakeEdge::BRepLib_MakeEdge(const opencascade::handle<Geom_Curve>&)`, the constructor that got the null curve.

## Doc strings

The nanocct generator copies the C++ `//!` documentation strings as Python docstrings

```python
In [14]: TopExp.MapShapes_s?

Signature:   TopExp.MapShapes_s(*args, **kwargs)
Type:        nb_func
String form: <nanobind.nb_func object at 0x115e4fa40>
Docstring:
MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, T: nanocct.TopAbs.TopAbs_ShapeEnum, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher) -> None
MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None
MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None

Overloaded function.

1. ``MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, T: nanocct.TopAbs.TopAbs_ShapeEnum, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher) -> None``

Tool to explore a topological data structure.
Stores in the map <M> all the sub-shapes of <S>
of type <T>.

Warning: The map is not cleared at first.

2. ``MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None``

Stores in the map <M> all the sub-shapes of <S>.
- If cumOri is true, the function composes all
sub-shapes with the orientation of S.
- If cumLoc is true, the function multiplies all
sub-shapes by the location of S, i.e. it applies to
each sub-shape the transformation that is associated with S.

3. ``MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None``

Stores in the map <M> all the sub-shapes of <S>.
- If cumOri is true, the function composes all
sub-shapes with the orientation of S.
- If cumLoc is true, the function multiplies all
sub-shapes by the location of S, i.e. it applies to
each sub-shape the transformation that is associated with S.
```

## AddOns

**Binding rule: R-ADDON ([Design 2c](Design.md#2c-python-additions))**

`nanocct.AddOns` is the one package that is not OCCT. Everything under an OCCT package name is a 1:1 binding; what nanocct adds of its own lives here, so that the 1:1 rule holds everywhere else. There are two reasons for an AddOn: a computation where a loop over OCCT calls in Python would dominate (`AddOns.Tessellator`), and a workaround for an OCCT bug that is reported upstream and not fixed yet (`AddOns.ShapeClean`).

### Tessellator

`NormalsFromSurface(face, uv)` evaluates the surface normal for every (u, v) row in C++; OCCT itself offers it one point at a time (`BRepGProp_Face.Normal`). `EdgeSegments(shape)` returns the polylines of all edges of a meshed shape as point pairs, with the segment count and the curve type of each edge.

```python
In [1]: import numpy as np
   ...: from nanocct import AddOns, BRep, BRepMesh, BRepPrimAPI, BRepTools, TopAbs, TopExp, TopLoc, TopoDS, gp
   ...: from nanocct.BRep import BRep_Builder
   ...: from nanocct.TopoDS import TopoDS_Compound
   ...:
   ...: sphere = BRepPrimAPI.BRepPrimAPI_MakeSphere(10.0).Shape()
   ...: BRepMesh.BRepMesh_IncrementalMesh(sphere, 0.01, False, 0.1, True)
   ...: face = TopoDS.Face(TopExp.TopExp_Explorer(sphere, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE).Current())
   ...: tri = BRep.BRep_Tool.Triangulation_s(face, TopLoc.TopLoc_Location())
   ...: u0, u1, v0, v1 = BRepTools.BRepTools.UVBounds_s(face)
   ...: uv = np.ascontiguousarray(np.clip(np.asarray(tri.InternalUVNodes()), [u0, v0], [u1, v1]))

In [2]: normals = AddOns.Tessellator.NormalsFromSurface(face, uv)
   ...: normals.shape, bool(np.allclose(np.linalg.norm(normals, axis=1), 1.0))
Out[2]: ((5153, 3), True)

In [3]: builder, boxes = BRep_Builder(), TopoDS_Compound()
   ...: builder.MakeCompound(boxes)
   ...: for i in range(1000):
   ...:     builder.Add(boxes, BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(2.0 * i, 0, 0), 1, 1, 1).Shape())
   ...: BRepMesh.BRepMesh_IncrementalMesh(boxes, 0.1, False, 0.5, True)
   ...: segments, per_edge, types = AddOns.Tessellator.EdgeSegments(boxes)
   ...: segments.shape, per_edge.shape, int(per_edge.sum())
Out[3]: ((24000, 3), (12000,), 12000)
```

The uv values have to be clamped to the face's bounds first: a mesh node can sit one unit in the last place outside them at a singularity of the surface, where the normal flips.

#### Tessellator timings

For comparison, the same two computations written in Python with OCCT's own calls; they produce identical results.

<details>
<summary>normals_py and edge_segments_py</summary>

```python
from nanocct import BRepAdaptor, BRepGProp
from nanocct.NCollection import NCollection_IndexedDataMap, NCollection_IndexedMap, NCollection_List
from nanocct.TopTools import TopTools_ShapeMapHasher
from nanocct.TopoDS import TopoDS_Shape

EDGE, FACE = TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE, TopAbs.TopAbs_ShapeEnum.TopAbs_FACE


def normals_py(face, uv):
    prop = BRepGProp.BRepGProp_Face(face)
    p, n = gp.gp_Pnt(), gp.gp_Vec()
    out = np.empty((len(uv), 3))
    for i, (u, v) in enumerate(uv):
        prop.Normal(float(u), float(v), p, n)
        if n.SquareMagnitude() > 0:
            n.Normalize()
        out[i] = (n.X(), n.Y(), n.Z())
    return out


def edge_segments_py(shape):
    edges = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
    TopExp.TopExp.MapShapes_s(shape, EDGE, edges)
    ancestors = NCollection_IndexedDataMap[TopoDS_Shape, NCollection_List[TopoDS_Shape], TopTools_ShapeMapHasher]()
    TopExp.TopExp.MapShapesAndAncestors_s(shape, EDGE, FACE, ancestors)
    pts, per_edge, types = [], [], []
    for i in range(1, edges.Extent() + 1):
        edge = TopoDS.Edge(edges.FindKey(i))
        if not ancestors.Contains(edge) or ancestors.FindFromKey(edge).IsEmpty():
            continue
        loc = TopLoc.TopLoc_Location()
        tri = BRep.BRep_Tool.Triangulation_s(TopoDS.Face(ancestors.FindFromKey(edge).First()), loc)
        if tri is None:
            continue
        poly = BRep.BRep_Tool.PolygonOnTriangulation_s(edge, tri, loc)
        if poly is None:
            continue
        types.append(int(BRepAdaptor.BRepAdaptor_Curve(edge).GetType()))
        nodes = np.asarray(tri.InternalNodes())[np.asarray(poly.ChangeNodeArray()) - 1]
        t = loc.Transformation()
        if t.Form() != gp.gp_TrsfForm.gp_Identity:
            m = np.array([[t.Value(r, c) for c in range(1, 5)] for r in range(1, 4)])
            nodes = nodes @ m[:, :3].T + m[:, 3]
        if len(nodes) >= 2:
            pts.append(np.stack([nodes[:-1], nodes[1:]], axis=1).reshape(-1, 3))
        per_edge.append(max(len(nodes) - 1, 0))
    return np.concatenate(pts), np.array(per_edge, dtype=np.int32), np.array(types, dtype=np.int32)
```

</details>

```python
In [4]: %timeit AddOns.Tessellator.NormalsFromSurface(face, uv)
82.9 μs ± 898 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [5]: %timeit normals_py(face, uv)
2.32 ms ± 36.6 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [6]: %timeit AddOns.Tessellator.EdgeSegments(boxes)
3.32 ms ± 140 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [7]: %timeit edge_segments_py(boxes)
50.8 ms ± 551 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

| Function                         | AddOn (C++)                          | Python with OCCT calls                | Factor |
| -------------------------------- | ------------------------------------ | ------------------------------------- | ------ |
| `NormalsFromSurface`, 5153 nodes | 82.9&nbsp;μs&nbsp;±&nbsp;898&nbsp;ns | 2.32&nbsp;ms&nbsp;±&nbsp;36.6&nbsp;μs | 28×    |
| `EdgeSegments`, 12000 edges      | 3.32&nbsp;ms&nbsp;±&nbsp;140&nbsp;μs | 50.8&nbsp;ms&nbsp;±&nbsp;551&nbsp;μs  | 15×    |

### ShapeClean

`AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` works around OCCT issue #1541: when OCCT's `ShapeUpgrade_UnifySameDomain` merges a full circle made of two or more arcs on a curved face, it concatenates the curves in the face's parameter space from the wrong end, and the resulting shape is invalid. The AddOn has OCCT's class name and signatures, so switching between the two is an import change. It is removed once OCCT fixes the bug; a test signals that moment.

```python
In [8]: from nanocct import BRepAlgoAPI, BRepCheck, ShapeUpgrade
   ...: from nanocct.AddOns.ShapeClean import ShapeUpgrade_UnifySameDomain
   ...:
   ...: box = BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(-0.5, -0.5, -0.5), 1.0, 1.0, 1.0).Shape()
   ...: ball = BRepPrimAPI.BRepPrimAPI_MakeSphere(gp.gp_Pnt(-0.894, -0.056, 0.161), 0.5).Shape()
   ...: cut = BRepAlgoAPI.BRepAlgoAPI_Cut(box, ball).Shape()
   ...:
   ...: def unify(cls, shape):
   ...:     u = cls(shape, True, True, True)
   ...:     u.AllowInternalEdges(False)
   ...:     u.Build()
   ...:     return u.Shape()

In [9]: BRepCheck.BRepCheck_Analyzer(unify(ShapeUpgrade.ShapeUpgrade_UnifySameDomain, cut)).IsValid()
Out[9]: False

In [10]: BRepCheck.BRepCheck_Analyzer(unify(ShapeUpgrade_UnifySameDomain, cut)).IsValid()
Out[10]: True
```
