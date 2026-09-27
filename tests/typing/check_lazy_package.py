"""`import OCP3x` + attribute access type-checks: the package is lazy at runtime (PEP 562), so
OCP3x/__init__.pyi has to declare the submodules or a checker rejects OCP3x.gp (Design.md 5.1, 6b)."""
import OCP3x

p: OCP3x.gp.gp_Pnt = OCP3x.gp.gp_Pnt(1.0, 2.0, 3.0)
x: float = p.X()
d = OCP3x.gp.gp_Dir(1.0, 0.0, 0.0)

bad: str = p.X()              # error: float is not str
OCP3x.NoSuchPackage         # error: no such attribute
