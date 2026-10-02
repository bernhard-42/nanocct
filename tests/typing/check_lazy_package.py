"""`import nanocct` + attribute access type-checks: the package is lazy at runtime (PEP 562), so
nanocct/__init__.pyi has to declare the submodules or a checker rejects nanocct.gp (Design.md 5.1, Binding-Rules.md 6b)."""
import nanocct

p: nanocct.gp.gp_Pnt = nanocct.gp.gp_Pnt(1.0, 2.0, 3.0)
x: float = p.X()
d = nanocct.gp.gp_Dir(1.0, 0.0, 0.0)

bad: str = p.X()              # error: float is not str
nanocct.NoSuchPackage         # error: no such attribute
