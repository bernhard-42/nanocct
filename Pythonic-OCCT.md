# Pythonic addition to the OCCT bindings

**Table of contents**

- [NCollections](#ncollections-support)
- [numpy support](#numpy-support)
- [Iterating over OCCT iterators](#iterating-over-occt-iterators)
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

*Design: [3.1 Naming conventions](docs/Conventions.md#31-naming-conventions), [7a NCollection containers](docs/Binding-Rules.md#7a-ncollection-containers-hand-written-binders)*

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
   43.1 ns ± 0.166 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

   In [9]: %timeit NCollection_Array1[gp_Dir](1, 3)
   78.8 ns ± 0.517 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
   ```

   | Statement                          | Timing             |
   | ---------------------------------- | ------------------ |
   | `NCollection_Array1__gp_Dir(1, 3)` | 43.1 ns ± 0.166 ns |
   | `NCollection_Array1[gp_Dir](1, 3)` | 78.8 ns ± 0.517 ns  |

   Typically, the NCollections don't appear in large loops where the nanoseconds could pile up, but are created once and then filled in a loop. Since both statements create the same type at runtime, accessing the NCollections takes the same time.

### C++ scalar types

A Python type stands for a C++ template argument: `float` for C++ `double`, `int` and `bool`. Python has no own type for five more C++ scalars used in OCCT 8, so `nanocct.NCollection` exports a marker for each:

| Marker      | C++ type             |
| ----------- | -------------------- |
| `float32`   | `float` (32-bit)     |
| `uchar`     | `unsigned char`      |
| `uint`      | `unsigned int`       |
| `ulong`     | `unsigned long`      |
| `ulonglong` | `unsigned long long` |

With them, the containers of nanocct can be spelled generically: `NCollection_Array1`, `Array2`, `HArray1`, `HArray2`, `Sequence`, `HSequence`, `List`, `Map`, `IndexedMap`, `DataMap`, `IndexedDataMap`, `DoubleMap`, `FlatMap`, `FlatDataMap`, `DynamicArray`, `LinearVector`, `LocalArray` and `Shared`. The other NCollection classes, such as `NCollection_Vec3` or `NCollection_Mat3`, have no generic spelling.

```python
In [1]: from nanocct.NCollection import NCollection_Array1, NCollection_HArray1, float32, uchar
   ...: from nanocct.Poly import Poly_Triangulation

In [2]: NCollection_HArray1[float32].__name__, NCollection_HArray1[uchar].__name__
Out[2]: ('NCollection_HArray1__float', 'NCollection_HArray1__unsigned_char')

In [3]: NCollection_Array1[float].__name__
Out[3]: 'NCollection_Array1__double'
```

The markers are only keys: the elements are plain Python numbers (see [Editing array and list elements in place](#editing-array-and-list-elements-in-place)). An array spelled with a marker is the one OCCT takes, e.g. for the normals of a triangulation:

```python
In [4]: normals = NCollection_HArray1[float32](1, 9, 0.0)   # 3 nodes, x y z each
   ...: tri = Poly_Triangulation(3, 1, False, False)
   ...: tri.SetNormals(normals)
   ...: tri.HasNormals()
Out[4]: True
```

For type checkers the markers are aliases of `float` and `int`: precision is not a Python type, the same as for every other C++ `float` or `unsigned int` parameter of the bindings. So a type checker does not tell `NCollection_HArray1[float32]` from `NCollection_HArray1[float]`; handing the wrong one to OCCT fails at runtime with a `TypeError`.

### numpy arrays

`NCollection_Array1` and `NCollection_Array2` of a packed element type (`float`, `int`, `gp_Pnt`, `gp_Vec`, …) support numpy's array protocol:
- `np.asarray(a)` is a zero-copy view of OCCT's memory
- `np.array(a)` is a copy
- `np.copyto(np.asarray(a), pts)` fills an OCCT array from a numpy array or a Python list

While a view lives, a call that would move or free the storage, such as a `Resize()` to another length, raises `BufferError`. See [numpy support](#numpy-support).

### Index access

`a[i]` hands out a copy of the element at OCCT's index. Unlike in a Python list, that index need not start at 0: it is the index the C++ container uses. `NCollection_Array1` counts from `Lower()`, `NCollection_Sequence` and the indexed maps from 1, `NCollection_DynamicArray` and `NCollection_LinearVector` from 0. There are no negative indices and no slices, because a negative index is a real OCCT index for an array like `NCollection_Array1[float](-2, 2)`. `a(i)` and `At(i)` hand out copies too, and `a[i] = p` writes an element; to change one in place, see [Editing array and list elements in place](#editing-array-and-list-elements-in-place).

The first index is the lower bound the array was created with; `At(i)` counts from 0 whatever it is:

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...:
   ...: a = NCollection_Array1[float](1, 3)    # starting from 1
   ...: for i in range(1, 4):
   ...:     a[i] = i * 10.0

In [2]: a[1], a[3], a.At(0)
Out[2]: (10.0, 30.0, 10.0)
```

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...:
   ...: a = NCollection_Array1[float](0, 2)    # starting from 0
   ...: for i in range(3):
   ...:     a[i] = (i + 1) * 10.0

In [2]: a[0], a[2], a.At(0)
Out[2]: (10.0, 30.0, 10.0)
```

For Python-style indexing, use a numpy view or a list:

```python
In [1]: import numpy as np
   ...: from nanocct.NCollection import NCollection_Array1
   ...:
   ...: a = NCollection_Array1[float](1, 8)
   ...: for i in range(1, 9):
   ...:     a[i] = i * 10.0

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
16.9 ns ± 0.073 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [7]: %timeit a[3]
20 ns ± 0.103 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)
```

| Statement    | Timing             |
| ------------ | ------------------ |
| `a.Value(3)` | 16.9 ns ± 0.073 ns  |
| `a[3]`       | 20 ns ± 0.103 ns |

**Note:** nanocct keeps OCCT's C++ contract for index access and adds no checks of its own. Where OCCT checks, a wrong index or an empty container raises an OCCT exception: `Value`/`ChangeValue`/`SetValue` of `NCollection_Array1`, `Sequence` and `LinearVector`, and `At` of `Array1` and `Sequence`, raise `Standard_OutOfRange`, and `First()`/`Last()` of an empty `List` or `Sequence` raise `Standard_NoSuchObject` (of an empty `LinearVector` `Standard_OutOfRange`). `NCollection_Array2` checks the row and the column only in `At(row, col)`: its `Value`, `ChangeValue`, `SetValue`, `a[(row, col)]` and `a(row, col)` check only that the position lies in the storage, so a column past the end of a row reaches the next row (`a.Value(1, 3)` of a 2 × 2 array reads the element at (2, 1)). Where OCCT does not check, it behaves as in C++ and can crash the Python interpreter:

- `First()`, `Last()`, `ChangeFirst()` and `ChangeLast()` of an empty `NCollection_Array1` or `HArray1`: OCCT reads an element of no storage, which, depending on the element type and the member, crashes, returns `None` or returns an object over no memory;
- `Value()` of a default-constructed or exhausted OCCT `Iterator` (`NCollection_List[int].Iterator().Value()`);
- `NCollection_DynamicArray`'s `Value`, `ChangeValue` and `d[i]` past the end: within the first block they return whatever the memory holds (`d[3]` of a 3-element array is `0`), beyond it (`d[256]`) the process crashes; `GetValue(row, col)` of `BVH_Mat4f`/`BVH_Mat4d` (OCCT's `NCollection_Mat4`) past its 4 × 4 elements returns whatever the memory holds;
- `r[i]` of an `ExtremaPC.Result` past `r.NbExt()`: it reads OCCT's `Extrema`, an `NCollection_DynamicArray` with blocks of 8, so of a result with 2 extrema `r[5]` is an `ExtremumResult` of whatever the memory holds, `r[8]` is `None`, and `r[300]` or `r[-1]` crash;
- a constructor whose upper bound lies below the lower one: `NCollection_Array1[float](5, 1)` constructs an array whose `Size()` is 18446744073709551613 (`len()` then raises `ValueError`, and `Init()` crashes), and `NCollection_Array2[float](3, 1, 1, 2).NbRows()` is `-1`.

### Iterating over NCollections

Every NCollection is iterable, and `len()` gives its number of elements. What a `for` loop yields depends on the kind of container:

| Container | `for x in c` yields | Also |
| --------- | ------------------- | ---- |
| `NCollection_Array1`, `Array2` | the elements | |
| `NCollection_Sequence`, `NCollection_List` | the elements | `Iterator`; `List`: `in` |
| `NCollection_Map`, `NCollection_IndexedMap` | the keys | `in`, `Iterator` |
| `NCollection_DataMap`, `NCollection_IndexedDataMap` | the keys, as a `dict` does | `items()` yields `(key, value)` tuples; `in`, `Iterator`; no `keys()` or `values()` |

```python
In [1]: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.NCollection import NCollection_Array1, NCollection_IndexedDataMap, NCollection_List
   ...: from nanocct.TopAbs import TopAbs_ShapeEnum
   ...: from nanocct.TopExp import TopExp
   ...: from nanocct.TopoDS import TopoDS_Shape
   ...: from nanocct.TopTools import TopTools_ShapeMapHasher
   ...:
   ...: a = NCollection_Array1[float](1, 3)
   ...: for i in range(1, 4):
   ...:     a[i] = i * 10.0
   ...: [x for x in a]
Out[1]: [10.0, 20.0, 30.0]

In [2]: box = BRepPrimAPI_MakeBox(1, 2, 3).Shape()
   ...: edge_faces = NCollection_IndexedDataMap[TopoDS_Shape, NCollection_List[TopoDS_Shape], TopTools_ShapeMapHasher]()
   ...: TopExp.MapShapesAndAncestors_s(box, TopAbs_ShapeEnum.TopAbs_EDGE, TopAbs_ShapeEnum.TopAbs_FACE, edge_faces)
   ...: len(edge_faces), {edge.ShapeType().name for edge in edge_faces}
Out[2]: (12, {'TopAbs_EDGE'})

In [3]: {faces.Extent() for edge, faces in edge_faces.items()}
Out[3]: {2}
```

A loop hands out copies, as `a[i]` does; to change elements while looping, see [Editing array and list elements in place](#editing-array-and-list-elements-in-place).

A change of the container during the loop is not refused, but some changes end the loop: after a removal (`Remove`, `RemoveFirst`, `RemoveLast`, `Clear`), a `Resize` to another length, or an `Add` or `Bind` on a hashed map (`NCollection_Map`, `DataMap`), even of a key it already holds, the loop's next step raises `RuntimeError`, as a `dict`'s does after a change of size. An `Append` to a `Sequence` or `List`, an `Add` to an `IndexedMap` or `IndexedDataMap`, or writing `a[i] = x`, lets the loop go on, and it reaches the added elements. An `Iterator` kept in a variable goes stale in the same way, see [Iterating over OCCT iterators](#iterating-over-occt-iterators).

`x in container` is OCCT's lookup where there is one: the maps (`IsBound`/`Contains` by key), and `NCollection_List` where the element type has `operator==` (`Contains`). Elsewhere Python falls back to iterating with its own `==`, which works for numbers and strings but is identity for a class without a value `==`: `gp_Pnt(1, 2, 3) in l` is `False` for a list holding an equal point. Compare explicitly there, `any(p.IsEqual(q, tol) for p in l)`.

Timings:

- 100 `float` element `NCollection`

  ```python
  In [4]: import numpy as np
     ...: from nanocct.NCollection import NCollection_Array1
     ...:
     ...: N = 100
     ...: a = NCollection_Array1[float](1, N)
     ...: for i in range(1, N+1):
     ...:     a[i] = i * 10.0
     ...:

  In [5]: %timeit [a.Value(i) for i in range(1, N + 1)]
  2.08 μs ± 9.8 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

  In [6]: %timeit list(a)
  1.42 μs ± 7.23 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

- 10 `float` element `NCollection`

  ```python
  In [7]: N = 10
     ...: a = NCollection_Array1[float](1, N)
     ...: for i in range(1, N+1):
     ...:     a[i] = i * 10.0
     ...:

  In [8]: %timeit [a.Value(i) for i in range(1, N + 1)]
  236 ns ± 3.9 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

  In [9]: %timeit list(a)
  366 ns ± 2.75 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

| Statement                               | 100 elements      | 10 elements      |
| --------------------------------------- | ----------------- | ---------------- |
| `[a.Value(i) for i in range(1, N + 1)]` | 2.08 μs ± 9.8 ns | 236 ns ± 3.9 ns |
| `list(a)`                               | 1.42 μs ± 7.23 ns | 366 ns ± 2.75 ns |

Below about 25 elements, `list(a)` is slower than the `Value()` loop, because creating the iterator costs about 190 ns.

### Editing array and list elements in place

*Binding rule: R-CONST-TWIN ([Binding rules](docs/Binding-Rules.md#r-const-twin))*

Edit an element in place with the member whose name says so, or change a copy and write it back with `a[i] = p`:

- **`Change…` members** hand out the element itself: `ChangeValue(i)`, `ChangeAt(i)`, `ChangeFirst()`, `ChangeLast()` of `NCollection_Array1`, `Array2` and `Sequence`; `ChangeValue(i)`, `ChangeFirst()` and `ChangeLast()` of `NCollection_DynamicArray` and `NCollection_LinearVector`; `ChangeFind(k)` and `ChangeSeek(k)` of `NCollection_DataMap`; `ChangeFromIndex(i)`, `ChangeFromKey(k)` and `ChangeSeek(k)` of `NCollection_IndexedDataMap`; with their `H` variants.
- **`NCollection_List`** has no index and no `Change…` member of its own: edit through its `Iterator`'s `ChangeValue()`.
- **Write back** with `a[i] = p` or `SetValue(i, p)`.

Examples:

- Arrays of C++ scalars (`NCollection_Array1[float]`, `NCollection_HArray1[float32]`, …)

  An element is a plain Python number: reading it gives the number, and changing that number leaves the array as it is. Scalar elements have no `Change…` member, so they are written with `a[i] = x` (or `SetValue(i, x)`) only. C++ converts the value on the way in, e.g. rounds it to 32 bits:

  ```python
  In [1]: from nanocct.NCollection import NCollection_HArray1, float32
     ...:
     ...: normals = NCollection_HArray1[float32](1, 9, 0.0)
     ...: normals[1] = 0.1
     ...: normals[1]
  Out[1]: 0.10000000149011612
  ```

- Arrays of C++ objects (`NCollection_Array1[gp_Pnt]`, …)

  `a[i]` is a copy, so an edit goes through `ChangeValue(i)` or writes a changed copy back with `a[i] = p`:

  ```python
  In [2]: from nanocct.NCollection import NCollection_Array1, NCollection_List
     ...: from nanocct.gp import gp_Pnt
     ...:
     ...: a = NCollection_Array1[gp_Pnt](1, 3)
     ...: a.ChangeValue(1).SetX(1.0)         # edits the first element of a
     ...: p = a[2]                           # p is a copy (!) of the second element of a
     ...: p.SetX(2.0)                        # edits the copy (!)
     ...: a[2] = p                           # writes the copy back
     ...: for i in range(1, a.Length() + 1):
     ...:     a.ChangeValue(i).SetZ(5.0)     # explicitly asks for the element, not a copy

  In [3]: [(a.Value(i).X(), a.Value(i).Z()) for i in range(1, 4)]
  Out[3]: [(1.0, 5.0), (2.0, 5.0), (0.0, 5.0)]
  ```

- Linked lists (`NCollection_List`)

  Python has no counterpart of a linked list that stores its values in its nodes, so an element is edited in place through OCCT's own `Iterator`, stepping with `More()` and `Next()`:

  ```python
  In [4]: lp = NCollection_List[gp_Pnt]()
     ...: lp.Append(gp_Pnt(1, 0, 0))
     ...: lp.Append(gp_Pnt(2, 0, 0))
     ...:
     ...: it = NCollection_List[gp_Pnt].Iterator(lp)
     ...: while it.More():
     ...:     it.ChangeValue().SetZ(5.0)     # the element itself
     ...:     it.Next()
     ...: [p.Z() for p in lp]
  Out[4]: [5.0, 5.0]
  ```

  A `for` loop over the `Iterator` yields copies, as `for p in lp` does.

### Editing map values in place

*Binding rule: R-CONST-TWIN ([Binding rules](docs/Binding-Rules.md#r-const-twin))*

Map values are edited the same way: with `ChangeFromIndex(i)` in an `NCollection_IndexedDataMap`, whose `m[i]` is by index, or `ChangeFind(k)` in an `NCollection_DataMap`. The values a map's `items()` hands out are copies, so `faces.Append(box)` in `for edge, faces in edge_faces.items()` changes nothing. For a key that is not bound, `m[k]` of an `NCollection_DataMap` raises `KeyError`, as a `dict` does; OCCT's own `m(k)` and `Find(k)` raise `Standard_NoSuchObject`.

```python
In [5]: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.NCollection import NCollection_IndexedDataMap
   ...: from nanocct.TopAbs import TopAbs_ShapeEnum
   ...: from nanocct.TopExp import TopExp
   ...: from nanocct.TopoDS import TopoDS_Shape
   ...: from nanocct.TopTools import TopTools_ShapeMapHasher
   ...:
   ...: box = BRepPrimAPI_MakeBox(1, 2, 3).Shape()
   ...: edge_faces = NCollection_IndexedDataMap[TopoDS_Shape, NCollection_List[TopoDS_Shape], TopTools_ShapeMapHasher]()
   ...: TopExp.MapShapesAndAncestors_s(box, TopAbs_ShapeEnum.TopAbs_EDGE, TopAbs_ShapeEnum.TopAbs_FACE, edge_faces)
   ...: for i in range(1, edge_faces.Extent() + 1):
   ...:     edge_faces.ChangeFromIndex(i).Append(box)
   ...: edge_faces[1].Extent()
Out[5]: 3
```

### Copies and assignments

*Binding rule: R-CONST-TWIN ([Binding rules](docs/Binding-Rules.md#r-const-twin))*

Every read other than through a `Change…` member hands out a copy, as the usual C++ `gp_Pnt p = a(i);` does: `a[i]`, `a(i)`, a `for` loop, the values of a map's `items()`, `First()`/`Last()`, `Value()`, `At()` and the `Find…()` members. A copy can be kept, sorted and swapped like any Python object, and editing it without writing it back leaves the container unchanged:

```python
In [6]: a[1], a[2] = a[2], a[1]          # swaps, as in a Python list
   ...: a.Value(1).X(), a.Value(2).X()
Out[6]: (2.0, 1.0)
```

A subscript on the left of `=` is no read: `a[1] = x` calls `a.__setitem__(1, x)`, which is `SetValue(1, x)`, a write into the array. Every other `a[i]` -- on the right of `=`, or in an expression such as `a[i].SetX(1.0)` -- calls `__getitem__` and hands out a copy. So the swap first reads two copies and then writes them, and `a[i] += x` reads a copy and writes the result back.

**Note for C++ readers:** in C++, `a(i).SetX(1.0)`, `a[i].SetX(1.0)` and `l.First().SetX(1.0)` edit the element, because the non-const overloads return a reference. Python has no const, so nanocct cannot tell which overload a caller means, and binds OCCT's usual by-value use (`gp_Pnt p = a(i);`, `TopoDS_Shape s = l.First();`). In Python these calls edit a copy. An element handed out as a reference for `[]` and the loops would be the slot itself, with C++ reference semantics: `a[1], a[2] = a[2], a[1]` would give two equal elements without an error, and so would writing back a sorted list.

### Holding an element

*Binding rule: R-VIEW-GUARD ([Binding rules](docs/Binding-Rules.md#r-view-guard))*

An element from a `Change…` member is a view into the container's storage, as a numpy view is. A name bound to it -- `faces = edge_faces.ChangeFromIndex(1)` -- holds it as long as the name lives, and while it does, the container refuses a call that would free or move the element with `BufferError`, as `bytearray` refuses to resize while a `memoryview` of it exists. In C++ that reference would be left dangling. Release the name with `faces = None`:

```python
In [7]: faces = edge_faces.ChangeFromIndex(1)
   ...: try:
   ...:     edge_faces.Clear()
   ...: except BufferError as e:
   ...:     msg = str(e)
   ...: msg
Out[7]: 'Clear: 1 live view(s) of this container (element references or numpy arrays) would be invalidated by this call; release them first (BufferError, as bytearray raises while a buffer is exported)'

In [8]: faces = None
   ...: edge_faces.Clear()
   ...: edge_faces.Extent()
Out[8]: 0
```

Which calls refuse while a `Change…` element is held, measured:

| Container | Refused while an element is held | Goes through |
| --------- | -------------------------------- | ------------ |
| `Array1` | `Resize` to another length, `Assign` of another size | `SetValue`, `a[i] = v`, `Init`, `Assign` of the same size, `Resize` to the same length |
| `Sequence` | `Remove`, `Clear` | `Append`, `Prepend`, `InsertAfter`, `SetValue`, `Exchange`, `Reverse` |
| `List` (an element from `Iterator.ChangeValue()`) | `RemoveFirst`, `Remove`, `Clear`, `other.Append(l)` (moves the list's nodes), an OCCT function that takes the list to change it (`BRepLib.SortFaces_s(box, l)`) | `Append`, `Prepend`, `Reverse` |
| `IndexedDataMap` | `RemoveLast`, `Clear`, an OCCT function that takes the map to fill it (`TopExp.MapShapesAndAncestors`) | `Add`, `Substitute`, `Swap` |

The full list per container is in [Design 7a](docs/Binding-Rules.md#calls-that-invalidate-a-containers-views-r-view-guard). A `Remove` of another element of a `Sequence` or `List` is refused too, although C++ keeps the other elements valid: the check counts the views per container, not per element.

In IPython or Jupyter, an element shown as a cell's result stays referenced by the output history (`Out`, `_`) and blocks these calls too, as a numpy view does: take elements inside an expression, or bind them to a name you release.

An element that is itself a container, such as an edge's list of faces, is also protected against being overwritten: while an element of that inner list is held, `Substitute`, `Bind` or `m[k] = v` on its key, and `SetValue` or `a[i] = v` of its slot are refused, because the overwrite destroys the inner list's elements:

```python
In [9]: TopExp.MapShapesAndAncestors_s(box, TopAbs_ShapeEnum.TopAbs_EDGE, TopAbs_ShapeEnum.TopAbs_FACE, edge_faces)
   ...: face = NCollection_List[TopoDS_Shape].Iterator(edge_faces.ChangeFromIndex(1)).ChangeValue()
   ...: try:
   ...:     edge_faces.Substitute(1, edge_faces.FindKey(1), NCollection_List[TopoDS_Shape]())
   ...: except BufferError as e:
   ...:     msg = str(e)
   ...: msg
Out[9]: 'Substitute: 1 live view(s) of this container (element references or numpy arrays) would be invalidated by this call; release them first (BufferError, as bytearray raises while a buffer is exported)'

In [10]: face = None
    ...: edge_faces.Substitute(1, edge_faces.FindKey(1), NCollection_List[TopoDS_Shape]())
    ...: edge_faces.FindFromIndex(1).Extent()
Out[10]: 0
```

Patterns that never run into it:

- **Edit through an expression**, not a name: `a.ChangeValue(i).SetX(1.0)`, `m.ChangeFromIndex(i).Append(shape)`. The element is released at the end of the statement, also in a loop over the indices.
- **Put the loop into a function**: its variables are released when it returns.
- **Release the name** before a `Clear()`, `Remove()` or `Resize()`: `faces = None`.
- **Instead of a `Resize()`** while elements are held, release them and take them again afterwards -- a C++ reference into the array does not survive its `Resize` either.

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

## numpy support

*Binding rule: R-VIEW ([Design 2, Python additions](docs/Design.md#python-additions))*

### Viewing an OCCT array with numpy zero-copy support

The nanocct generator gives `NCollection_Array1` and `NCollection_Array2` (and their `HArray1`/`HArray2` variants) numpy's array protocol, `__array__`, for every element type that is a packed run of numpy scalars: the C++ scalars `double`, `float`, `int`, `bool`, `unsigned char`, `gp_Pnt`, `gp_Vec`, `gp_Dir`, `gp_XYZ`, `gp_Pnt2d`, `gp_Vec2d`, `gp_XY`, `Poly_Triangle` and the `NCollection_Vec2/3/4` types. `Poly_ArrayOfNodes`, `Poly_ArrayOfUVNodes`, `Image_PixMap` and `NCollection_Buffer` have it too. This allows to access large C++ arrays from Python with zero-copy:

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
   ...: print(v)
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

In [3]: v[0, 0] = 42.0
   ...: a.Value(1).X()
Out[3]: 42.0

In [4]: c = np.array(a)
   ...: c[0, 0] = 7.0
   ...: a.Value(1).X()
Out[4]: 42.0
```

A view -- a numpy view, or an element itself as `ChangeValue()` hands it out (see [Holding an element](#holding-an-element)) -- points into the container's storage, which it keeps alive but cannot keep in place. So the container refuses every call that would move or free what a live view points to, as a `bytearray` does while a buffer is exported: a `Resize()` to another length, a `Remove()`, a `Clear()`, or an OCCT function that takes the container to fill it raises `BufferError`. Release the view first, or take it after the change:

```python
In [5]: try:
   ...:     a.Resize(1, 5, True)                 # v is still a view
   ...: except BufferError as e:
   ...:     msg = str(e)
   ...: msg
Out[5]: 'Resize: 1 live view(s) of this container (element references or numpy arrays) would be invalidated by this call; release them first (BufferError, as bytearray raises while a buffer is exported)'

In [6]: v = None
   ...: a.Resize(1, 5, True)
   ...: np.asarray(a).shape
Out[6]: (5, 3)
```

In IPython or Jupyter, a view shown as a cell's result stays referenced by the output history (`Out`, `_`) and blocks these calls too: show views with `print()`, as In [2] does.

A call that keeps the storage in place goes through while a view lives: `SetValue()`, a `Resize()` to the same length, an `Assign()` of an array of the same size. Which call refuses for which container is listed in [Design 7a](docs/Binding-Rules.md#calls-that-invalidate-a-containers-views-r-view-guard).

### Copying numpy data into an OCCT array

A numpy array or a Python list of points goes into an OCCT array with one copy: create the array with OCCT's bounds and copy into its view. The view is a temporary, so it blocks nothing afterwards:

```python
In [7]: from nanocct.gp import gp_Pnt
   ...:
   ...: pts = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0]]
   ...: b = NCollection_Array1[gp_Pnt](1, len(pts))
   ...: np.copyto(np.asarray(b), pts)  # copyto needs b's numpy view: np.asarray (np.array would be a copy)
   ...: b.Value(2).X(), b.Value(3).Y()
Out[7]: (1.0, 1.0)
```

numpy checks the shape (`ValueError: could not broadcast input array from shape (3,3) into shape (2,3)`) and converts the values, e.g. `int` to `float`. The view of an array of `gp_Dir` is read-only (`ValueError: assignment destination is read-only`), because a raw write could store a direction that is not of unit length: write those with `a[i] = gp_Dir(…)`.

### numpy timings

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
99.9 ms ± 917 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [3]: %timeit np.asarray(a)  # zero copy
313 ns ± 1.97 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [4]: %timeit np.array(a)
333 μs ± 2.02 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

| Statement                                       | Timing            |
| ----------------------------------------------- | ----------------- |
| `[a.Value(i).Coord() for i in range(1, N + 1)]` | 99.9 ms ± 917 μs |
| `np.array(a)`                                   | 333 μs ± 2.02 μs  |
| `np.asarray(a)` (zero copy)                     | 313 ns ± 1.97 ns  |

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

## Iterating over OCCT iterators

*Binding rule: R-ITER ([Design 2, Python additions](docs/Design.md#python-additions))*

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

An iterator over an NCollection holds a position inside it. A call that would free that position -- a `Clear()`, a `Remove()`, and for a hashed map (`NCollection_Map`, `DataMap`, `DoubleMap`) an insert, which can grow the table -- goes ahead, and the iterator then raises `RuntimeError` on its next use, as a `dict` iterator does after a change of size. The iterator of a `List`, `Map`, `DataMap` or `DoubleMap` starts again with `Initialize()`; one of a `Sequence`, `IndexedMap` or `IndexedDataMap` has no `Initialize()` and is made anew. Removing through the iterator itself, OCCT's own removal loop, keeps it valid.

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

In [8]: l.Clear()                    # goes ahead
   ...: l.Size()
Out[8]: 0

In [9]: try:
   ...:     it.More()
   ...: except RuntimeError as e:
   ...:     msg = str(e)
   ...: msg
Out[9]: 'Iterator.More: the container changed during iteration; initialise the iterator again (RuntimeError, as dict raises after a change of size during iteration)'
```

### Timings

A compound of 100 boxes (600 faces, 2400 edge visits, 1200 distinct edges):

```python
In [10]: from nanocct.BRep import BRep_Builder
    ...: from nanocct.TopoDS import TopoDS_Compound
    ...:
    ...: builder, comp = BRep_Builder(), TopoDS_Compound()
    ...: builder.MakeCompound(comp)
    ...: for i in range(100):
    ...:     builder.Add(comp, BRepPrimAPI_MakeBox(1, 1, 1).Shape())

In [11]: %%timeit
    ...: ex, out = TopExp_Explorer(comp, EDGE), []
    ...: while ex.More():
    ...:     out.append(ex.Current())
    ...:     ex.Next()
157 μs ± 355 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [12]: %timeit [e for e in TopExp_Explorer(comp, EDGE)]
132 μs ± 1.61 μs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [13]: %timeit list(TopExp_Explorer(comp, EDGE))
124 μs ± 2.31 μs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [14]: %%timeit
    ...: m = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
    ...: TopExp.MapShapes_s(comp, EDGE, m)
    ...: list(m)
110 μs ± 554 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

| Statement                                                                                                         | Timing                              |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `ex, out = TopExp_Explorer(comp, EDGE), []; while ex.More(): out.append(ex.Current()); ex.Next()`                 | 157&nbsp;μs&nbsp;±&nbsp;355&nbsp;ns |
| `[e for e in TopExp_Explorer(comp, EDGE)]`                                                                        | 132&nbsp;μs&nbsp;±&nbsp;1.61&nbsp;μs |
| `list(TopExp_Explorer(comp, EDGE))`                                                                               | 124&nbsp;μs&nbsp;±&nbsp;2.31&nbsp;μs |
| `m = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher](); TopExp.MapShapes_s(comp, EDGE, m); list(m)` | 110&nbsp;μs&nbsp;±&nbsp;554&nbsp;ns |

A `for` loop or `list()` is about 15–20 % faster than a hand-written `More()`/`Next()` loop. `TopExp.MapShapes` is the fastest here, although it also removes the duplicates: the traversal runs in one C++ call, and it returns 1 200 instead of 2 400 shapes.

## Handling of primitive types passed by reference

*Binding rules: R-OUT, R-COLLISION ([Design 3.1](docs/Conventions.md#31-naming-conventions)), R-INOUT ([Design 7](docs/Binding-Rules.md))*

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

*Binding rule: R-REF-PRIMITIVE ([Design 2, Python additions](docs/Design.md#python-additions))*

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

*Binding rules: R-OPERATOR, R-IOP, R-FREE-OP, R-STR ([Design 2, Python additions](docs/Design.md#python-additions))*

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
| `std::hash<gp_Pnt>`      | the bits of the three doubles, summed lossily from their 32-bit halves (`gp_Pnt.hxx`) |


## Strings

Every C++ text type of OCCT is a Python `str`: `const char*` (`Standard_CString`), `std::string_view`, the UTF-16 `const char16_t*` (`Standard_ExtString`), and the single characters `char`, `char16_t` and `char32_t`. A `str` goes to C++ as UTF-8 for the 8-bit types and as UTF-16 for `char16_t`.

Where OCCT overloads a method for several of these types, Python cannot tell them apart, and nanobind calls the first overload that accepts a `str`. nanocct registers them in the order C++ itself picks for a narrow string literal `"..."`: `const char*` first, then `std::string_view`, then `const char16_t*`, then the single characters. An overload that can never be reached this way is not bound, and the generator reports it ([Design 7](docs/Binding-Rules.md), R-WIDTH, R-UNREACHABLE).

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

*Binding rules: R-STREAM-OUT, R-STREAM-IN ([Design 7](docs/Binding-Rules.md))*

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

### Precision of written text

*Binding rule: R-STREAM-OUT ([Binding rules](docs/Binding-Rules.md#r-stream-out))*

A C++ caller sets the precision of the stream it hands to a writer, `stream.precision(17)`. The returned text has no stream to set, so every member that writes text takes the keyword-only `precision_hint`, the precision the binding's stream starts with. The default is 6, the precision of a new C++ stream, so the text is what C++ writes into a new stream:

```python
In [7]: import io
   ...: from nanocct.Geom import Geom_Circle, Geom_TrimmedCurve
   ...: from nanocct.GeomTools import GeomTools
   ...: from nanocct.gp import gp_Ax2, gp_Dir, gp_Pnt
   ...:
   ...: arc = Geom_TrimmedCurve(Geom_Circle(gp_Ax2(gp_Pnt(3, 0, 0), gp_Dir(0, 0, 1)), 2), 18, 23, False, False)
   ...: GeomTools.Write_s(arc).split()[:2], GeomTools.Write_s(arc, precision_hint=17).split()[:2]
Out[7]: (['8', '-16.7168'], ['8', '-16.716814692820414'])

In [8]: def read_back(text):
   ...:     return GeomTools.Read_s__Geom_Curve(io.StringIO(text)).FirstParameter() == arc.FirstParameter()
   ...:
   ...: read_back(GeomTools.Write_s(arc)), read_back(GeomTools.Write_s(arc, precision_hint=17))
Out[8]: (False, True)
```

It is a hint, not a guarantee: a writer that sets its own precision overrides it, exactly as it overrides a C++ caller's. The BREP writer and OCCT's geometry sets always write 15 or 17 digits, whatever the hint says, while `GeomTools.Write_s` above and `DumpJson` use it (`gp_Pnt(0.1, 0, 0).DumpJson(precision_hint=17)` writes `0.10000000000000001`). Python cannot tell which kind a member is, and neither can the binding, so every docstring with the keyword contains a line saying so:

```python
In [9]: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.BRepTools import BRepTools
   ...:
   ...: box = BRepPrimAPI_MakeBox(1, 2, 3).Shape()
   ...: BRepTools.Write_s(box, precision_hint=3) == BRepTools.Write_s(box)
Out[9]: True

In [10]: GeomTools.Write_s.__doc__.splitlines()[-1]
Out[10]: "precision_hint: the precision the stream this binding writes into starts with (std::ostream::precision). A writer that sets its own, such as the BREP and geometry-set writers (15 or 17 digits), overrides it, as it does a C++ caller's stream (nanocct R-STREAM-OUT)."
```

### Reading from memory

A stream parameter takes a text file-like object, so text in memory is wrapped in `io.StringIO`. A plain `str` in its place is taken as a file name: it selects the file-path overload, which finds no such file and returns `False`.

```python
In [11]: import io
    ...: from nanocct.BRep import BRep_Builder
    ...: from nanocct.TopoDS import TopoDS_Shape
    ...:
    ...: text = BRepTools.Write_s(s)
    ...: back = TopoDS_Shape()
    ...: BRepTools.Read_s(back, io.StringIO(text), BRep_Builder())
    ...: back.ShapeType()
Out[11]: TopAbs_ShapeEnum.TopAbs_SOLID

In [12]: BRepTools.Read_s(TopoDS_Shape(), text, BRep_Builder())
Out[12]: False
```

### Reading in steps

*Binding rule: R-STREAM-IN ([Binding rules](docs/Binding-Rules.md#r-stream-in))*

A file-like object moves on by what OCCT read from it, as a C++ stream does: a member that reads one value leaves the object right after that value, so the next call continues there, and what OCCT did not read is still in the object:

```python
In [13]: import io
    ...: from nanocct.GeomTools import GeomTools
    ...:
    ...: stream = io.StringIO("1.25 7 tail")
    ...: GeomTools.GetReal_s(stream), GeomTools.GetReal_s(stream)
Out[13]: (1.25, 7.0)

In [14]: stream.read()
Out[14]: ' tail'
```

The same holds for a file opened for reading and for binary objects (`io.BytesIO`, a file opened `"rb"`). Three details:

- The binding reads the whole object into a C++ stream for the call and puts it back where it was before; after the call it moves it on by what OCCT read. So a call that fails -- an OCCT exception, or arguments that select another overload -- leaves the object where it was.
- An object that cannot seek (a pipe, anything with only a `read()`) cannot be put back: it is read to its end.
- The C++ stream's own state, `fail()` or `width()`, does not exist in Python and ends with the call.

### Binary formats

The packages whose streams carry a binary format use `bytes` instead of `str`: `BinTools` (the binary BRep format) and the OCAF document streams (`PCDM`, `CDF`, the `Bin*` and `Xml*` drivers, `DE`), listed in `generator/overrides.toml` `[stream] binary_packages`. The written data is returned as `bytes`, and a binary file-like object such as `io.BytesIO` is read.

```python
In [15]: from nanocct.BinTools import BinTools
    ...:
    ...: data = BinTools.Write_s(s)
    ...: len(data), data[:24]
Out[15]: (4494, b'\nOpen CASCADE Topology V')

In [16]: back = TopoDS_Shape()
    ...: BinTools.Read_s(back, io.BytesIO(data))
    ...: back.ShapeType()
Out[16]: TopAbs_ShapeEnum.TopAbs_SOLID
```

### Binary curves and surfaces

*Binding rule: R-STREAM-WRAPPER ([Binding rules](docs/Binding-Rules.md#r-stream-wrapper))*

`BinTools_CurveSet.WriteCurve_s`, `BinTools_Curve2dSet.WriteCurve2d_s` and `BinTools_SurfaceSet.WriteSurface_s` write one curve or surface in the binary format and return its `bytes`; `BinTools_ShapeReader.ReadLocation` takes a binary file-like object. (In C++ these take a `BinTools_OStream`/`BinTools_IStream`, a class that only wraps a stream; the binding makes it on its own stream.) Together with reading in steps, several records can go one after the other:

```python
In [17]: import io
    ...: from nanocct.BinTools import BinTools_CurveSet
    ...: from nanocct.Geom import Geom_Circle, Geom_TrimmedCurve
    ...: from nanocct.gp import gp_Ax2
    ...:
    ...: arcs = [Geom_TrimmedCurve(Geom_Circle(gp_Ax2(), r), 0.5, 2.5) for r in (1.0, 2.0)]
    ...: data = b"".join(BinTools_CurveSet.WriteCurve_s(c) for c in arcs)
    ...: type(data).__name__, len(data)
Out[17]: ('bytes', 244)

In [18]: stream = io.BytesIO(data)
    ...: [BinTools_CurveSet.ReadCurve_s(stream).BasisCurve().Radius() for _ in arcs], stream.read()
Out[18]: ([1.0, 2.0], b'')
```

## Enums

*Binding rules: [R-ENUM](docs/Binding-Rules.md#r-enum), [R-ANON-ENUM](docs/Binding-Rules.md#r-anon-enum)*

OCCT's unscoped enums are Python `enum.IntEnum` classes. As in C++, the enumerators of an unscoped enum are also names in the module (`TopAbs.TopAbs_FACE`), and they are integers. As in C++, the conversion goes one way only: an OCCT parameter of an enum type takes its enumerators, not an `int` or a `bool` (`TypeError`); `TopAbs_ShapeEnum(4)` turns an `int` into the enumerator. An `enum class` stays nested in its class and is a plain `enum.Enum`, as in C++ no integer: `gp_Dir.D.NZ == 5` is `False`. An anonymous enum (`enum { … }`) has no type of its own: its enumerators are plain `int` attributes of the module or class (`BVH.BVH_Constants_MaxTreeDepth` is `32`).

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

*Design: [5.2](docs/Runtime.md#52-three-kinds-of-c-types)*

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

A handle that OCCT returns can be null, and nanocct turns a null handle into `None`. The type stubs do not say so: a handle result is typed as its class, not as `X | None`, because OCCT's headers do not say which methods can return a null handle -- most never do, and `| None` on all of them would make a type checker demand a `None` check after every call. A type checker therefore accepts `curve.Value(0.5)` for a `curve` that is `None` at runtime. Where OCCT documents a null result, check it:

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
  Binary file ".../nanocct/.dylibs/libTKTopAlgo.8.0.2.dylib", at _ZN16BRepLib_MakeEdgeC1ERKN11opencascade6handleI10Geom_CurveEE+0x54
  Binary file ".../nanocct/_TKTopAlgo.abi3.so", at PyInit__TKTopAlgo+0x8da4
```

`_ZN16BRepLib_MakeEdgeC1ERKN11opencascade6handleI10Geom_CurveEE` is `BRepLib_MakeEdge::BRepLib_MakeEdge(const opencascade::handle<Geom_Curve>&)`, the constructor that got the null curve.

## Doc strings

The nanocct generator copies the C++ `//!` documentation strings as Python docstrings

```python
In [1]: from nanocct.TopExp import TopExp

In [2]: TopExp.MapShapes_s?

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

*Binding rule: R-ADDON ([Design 2, Python additions](docs/Design.md#python-additions))*

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

Tessellator timings:

For comparison, the same two computations written in Python with OCCT's own calls; they produce identical results.

<details>
<summary>normals_py and edge_segments_py</summary>

```python
from nanocct import BRepAdaptor, BRepGProp, GeomAbs
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
            no_curve = BRep.BRep_Tool.Degenerated_s(edge) or BRep.BRep_Tool.Curve_s(edge)[0] is None
            types.append(GeomAbs.GeomAbs_CurveType.GeomAbs_OtherCurve.value if no_curve
                         else int(BRepAdaptor.BRepAdaptor_Curve(edge).GetType()))
            per_edge.append(0)                      # a placeholder keeps entry i at edge-map index i
            continue
        types.append(int(BRepAdaptor.BRepAdaptor_Curve(edge).GetType()))
        loc = TopLoc.TopLoc_Location()
        tri = BRep.BRep_Tool.Triangulation_s(TopoDS.Face(ancestors.FindFromKey(edge).First()), loc)
        poly = None if tri is None else BRep.BRep_Tool.PolygonOnTriangulation_s(edge, tri, loc)
        if poly is None:
            per_edge.append(0)
            continue
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
85.4 μs ± 625 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [5]: %timeit normals_py(face, uv)
2.26 ms ± 12.1 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [6]: %timeit AddOns.Tessellator.EdgeSegments(boxes)
3.42 ms ± 179 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [7]: %timeit edge_segments_py(boxes)
53.5 ms ± 455 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

| Function                         | AddOn (C++)                          | Python with OCCT calls                | Factor |
| -------------------------------- | ------------------------------------ | ------------------------------------- | ------ |
| `NormalsFromSurface`, 5153 nodes | 85.4&nbsp;μs&nbsp;±&nbsp;625&nbsp;ns | 2.26&nbsp;ms&nbsp;±&nbsp;12.1&nbsp;μs | 26×    |
| `EdgeSegments`, 12000 edges      | 3.42&nbsp;ms&nbsp;±&nbsp;179&nbsp;μs | 53.5&nbsp;ms&nbsp;±&nbsp;455&nbsp;μs  | 16×    |

### ShapeClean

`AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` works around OCCT issue #1541: when OCCT's `ShapeUpgrade_UnifySameDomain` merges a full circle made of two or more arcs on a curved face, it concatenates the curves in the face's parameter space from the wrong end, and the resulting shape is invalid. It also puts back an edge whose curve in the face's parameter space OCCT, after merging the edge from several pieces, recomputes one period away on a periodic face (a hole through a cylindrical face across its period line), which leaves the face invalid too, and it repairs the merge of a face with its mirror image, which OCCT builds as two faces or leaves half done. The AddOn has OCCT's class name and the same signatures for the members it has (the constructor with the shape and the flags, `AllowInternalEdges`, `Build`, `Shape`, `History`), so for code that uses these, switching between the two is an import change. It is removed once OCCT fixes the bug; a test signals that moment. What it does, step by step: [docs/AddOns.md](docs/AddOns.md).

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
