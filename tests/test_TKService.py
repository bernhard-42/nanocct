"""Generated bindings for TKService (Visualization: Aspect, Graphic3d, Image, Font, Media, the window packages): the font
manager and FreeType fonts (build123d's text path), materials, vectors with their hidden-friend operators, pixmaps, clip-plane
iteration, the enum aliases OCCT keeps for 7.x code, the in/out FindFont aspect. The OCCT build has no FreeImage/FFmpeg:
Image_AlienPixMap saves PPM only and the Media package is stubs (Design.md 2d)."""
import importlib
import io
import platform
import re
from pathlib import Path

import pytest

from OCP3x import Aspect, Font, Graphic3d, Image, Message, Quantity, TCollection, gp
from OCP3x.NCollection import NCollection_Sequence, NCollection_String

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKService" / "report.txt"


# Xw, Wasm and WNT are built everywhere -- OCCT exports symbols for all three on all three platforms (the counts are
# in overrides.toml [platform]). Cocoa is the one package OCCT compiles on macOS only, so it is generated there only.
@pytest.mark.parametrize("pkg", ["Aspect", "Graphic3d", "Image", "Font", "Media", "Xw", "Wasm", "WNT", "Shaders"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


@pytest.mark.skipif(platform.system() != "Darwin", reason="Cocoa is built on macOS only (overrides.toml [platform])")
def test_cocoa_imports_on_macos():
    assert importlib.import_module("OCP3x.Cocoa").__name__ == "OCP3x.Cocoa"


@pytest.fixture
def quiet_messenger():
    """OCCT's fallback-font warning is unconditional (Font_FontMgr.cxx:1114): raise the printers' trace level for the test."""
    printers = list(Message.Message.DefaultMessenger_s().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


def test_font_manager_finds_system_fonts_and_returns_the_aspect(quiet_messenger):
    mgr = Font.Font_FontMgr.GetInstance_s()
    available = mgr.GetAvailableFonts()
    assert len(available) > 0
    # Which fonts a machine has is its own business: macOS ships Helvetica in a .ttc, AlmaLinux only DejaVu, and
    # banach answered "Helvetica" with Arial (2026-09-23). Asking for a name the manager itself reports keeps the
    # test about what it is meant to test -- the in/out Font_FontAspect& parameter and the path accessor.
    wanted = next(f for f in available if f.HasFontAspect(Font.Font_FA_Regular))
    name = wanted.FontName().ToCString()
    font, aspect = mgr.FindFont(TCollection.TCollection_AsciiString(name), Font.Font_FA_Regular)   # Font_FontAspect& is in/out
    assert font is not None and font.FontName().ToCString() == name and aspect == Font.Font_FontAspect_Regular
    assert Path(font.FontPath(Font.Font_FA_Regular).ToCString()).is_file()
    fallback, aspect = mgr.FindFont(TCollection.TCollection_AsciiString("NoSuchFont-OCP3x"), Font.Font_StrictLevel_Any, Font.Font_FA_Bold, False)
    assert fallback is not None and aspect == Font.Font_FontAspect_Bold           # the fallback keeps the requested aspect
    assert mgr.FindFont(TCollection.TCollection_AsciiString("NoSuchFont-OCP3x"), Font.Font_StrictLevel_Strict, Font.Font_FA_Bold, False)[0] is None


def test_enum_aliases_are_exported_like_the_first_spelling():
    """Font_FA_Bold = Font_FontAspect_Bold in the header: Python's Enum hides the alias from iteration, so nanobind's
    export_values() skipped it (R-ENUM, 2026-09-22); build123d imports Font_FA_Bold."""
    assert Font.Font_FA_Bold is Font.Font_FontAspect.Font_FA_Bold and Font.Font_FA_Bold == Font.Font_FontAspect_Bold
    assert int(Font.Font_FA_Regular) == 0 and int(Font.Font_FA_BoldItalic) == 3
    assert Graphic3d.Graphic3d_HTA_LEFT == Graphic3d.Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT
    assert Aspect.Aspect_TOL_SOLID == Aspect.Aspect_TypeOfLine.Aspect_TOL_SOLID


def test_freetype_font_metrics_and_code_points():
    """Font_FTFont is the FreeType face behind text-to-BRep; its code-point API takes char32_t = a 1-character str (R-CHAR16)."""
    params = Font.Font_FTFontParams()
    params.PointSize = 24
    params.Resolution = 72
    font = Font.Font_FTFont()
    assert font.FindAndInit(TCollection.TCollection_AsciiString("Helvetica"), Font.Font_FA_Regular, params) is True
    assert font.IsValid() and font.PointSize() == 24 and font.Ascender() > 0 > font.Descender()
    assert font.HasSymbol("A") and font.AdvanceX("A", "V") > 0 and font.AdvanceX("W", "W") > font.AdvanceX("i", "i")
    assert Font.Font_FTFont.IsCharFromCJK_s("漢") and not Font.Font_FTFont.IsCharFromCJK_s("A")
    with pytest.raises(TypeError):
        font.HasSymbol(65)                     # a code point is a 1-character str, not an int
    with pytest.raises(TypeError):
        font.HasSymbol("AB")
    fmt = Font.Font_TextFormatter()
    fmt.Append(NCollection_String("ab\ncd"), font)
    fmt.Format()
    assert fmt.LineIndex(3) == 1 and fmt.ResultHeight() > fmt.LineHeight(0) > 0 and fmt.String().ToCString() == "ab\ncd"
    assert fmt.LineWidth(0) == pytest.approx(font.AdvanceX("a", "b") + font.AdvanceX("b", "\n"), abs=1e-3)
    it = Font.Font_TextFormatter.Iterator(fmt)                        # default IterationFilter_None: the nested class sees the outer enum
    assert it.More() and it.Symbol() == "a" and it.SymbolNext() == "b"
    it.Next()
    it.Next()
    assert it.Symbol() == "\n" and it.SymbolPosition() == 2
    hidden = Font.Font_TextFormatter.Iterator(fmt, Font.Font_TextFormatter.IterationFilter_ExcludeInvisible)
    assert [hidden.Symbol(), (hidden.Next(), hidden.Symbol())[1], (hidden.Next(), hidden.Symbol())[1]] == ["a", "b", "c"]   # the LF is skipped


def test_materials_colors_and_vectors():
    m = Graphic3d.Graphic3d_MaterialAspect(Graphic3d.Graphic3d_NameOfMaterial_Gold)
    assert m.StringName().ToCString() == "Gold" and m.Name() == Graphic3d.Graphic3d_NameOfMaterial_Gold
    assert m.Color().Name() == Quantity.Quantity_NOC_GOLDENROD3 and 0.0 < m.Shininess() < 1.0
    m.SetColor(Quantity.Quantity_Color(Quantity.Quantity_NOC_RED))
    assert m.Color().Name() == Quantity.Quantity_NOC_RED
    Vec3 = Quantity.NCollection_Vec3__float             # the 8.0 spelling; Graphic3d_Vec3 is a pre-8.0 alias and not bound
    assert not hasattr(Graphic3d, "Graphic3d_Vec3")
    a, b = Vec3(1.0, 2.0, 3.0), Vec3(4.0, 5.0, 6.0)
    assert (a + b).z() == 9.0 and (b - a).x() == 3.0 and (a * b).y() == 10.0      # hidden friend operators (R-FREE-OP)
    a += b
    assert a.x() == 5.0 and a.Dot(b) == pytest.approx(20 + 35 + 54)
    v4 = Quantity.NCollection_Vec4__float(1.0, 2.0, 3.0, 4.0)
    assert (v4 / Quantity.NCollection_Vec4__float(1.0, 2.0, 3.0, 4.0)).w() == 1.0
    assert Quantity.Quantity_Color(Quantity.Quantity_NOC_RED).Rgb().r() == 1.0  # Quantity_Color -> NCollection_Vec3<float>


def test_pixmap_pixel_access_and_image_io(tmp_path):
    px = Image.Image_PixMap()
    assert px.InitZero(Image.Image_Format_RGB, 4, 3) and (px.Width(), px.Height(), px.SizeBytes()) == (4, 3, 36)
    red = Quantity.Quantity_ColorRGBA(Quantity.Quantity_Color(1.0, 0.0, 0.0, Quantity.Quantity_TOC_RGB), 1.0)
    px.SetPixelColor(1, 2, red)
    c = px.PixelColor(1, 2)
    assert (c.GetRGB().Red(), c.GetRGB().Green(), c.Alpha()) == (1.0, 0.0, 1.0) and px.PixelColor(0, 0).GetRGB().Red() == 0.0
    # Image_AlienPixMap::InitCopy refuses a copy that would need a pixel-format conversion, and on Windows OCCT builds
    # it on the Windows Imaging Component (Image_AlienPixMap.cxx:16 defines HAVE_WINCODEC when FreeImage is absent),
    # whose InitTrash rewrites RGB to BGR -- so an RGB source can never be copied there. BGR is left alone by every
    # backend, which makes the copy work on all three (gauss, 2026-09-24).
    bgr = Image.Image_PixMap()
    assert bgr.InitZero(Image.Image_Format_BGR, 4, 3)
    alien = Image.Image_AlienPixMap()
    assert alien.InitCopy(bgr)
    # Since FreeImage (State.md 8.9, 2026-09-25) every platform writes the format the extension names and can read
    # it back. Before that, macOS and Linux wrote a PPM under *any* extension and returned true while doing it, and
    # Load() failed for everything including that PPM; only Windows, on WIC, behaved.
    for ext, magic in (("png", b"\x89PNG"), ("bmp", b"BM"), ("tiff", b"II*\x00"), ("ppm", b"P6")):
        out = tmp_path / f"x.{ext}"
        assert alien.Save(TCollection.TCollection_AsciiString(str(out))), ext
        assert out.read_bytes().startswith(magic), ext
        back = Image.Image_AlienPixMap()
        assert back.Load(TCollection.TCollection_AsciiString(str(out))), ext
        assert (back.Width(), back.Height()) == (4, 3), ext
    assert alien.AdjustGamma(2.2)                        # FreeImage-only; returned false on every platform before


def test_clip_plane_sequence_iterator_is_declared_after_its_binder_base():
    """Graphic3d_SequenceOfHClipPlane::Iterator derives from NCollection_Sequence<handle<Graphic3d_ClipPlane>>::Iterator, a
    binder's nested class registered in the templates phase (6a, 2026-09-22); the items are protected, so it is the only way in."""
    seq = Graphic3d.Graphic3d_SequenceOfHClipPlane()
    for z in (1.0, 2.0, 3.0):
        assert seq.Append(Graphic3d.Graphic3d_ClipPlane(gp.gp_Pln(gp.gp_Pnt(0, 0, z), gp.gp_Dir(0, 0, 1))))
    assert seq.Size() == 3 and seq.First().ToPlane().Location().Z() == 1.0
    it = Graphic3d.Graphic3d_SequenceOfHClipPlane.Iterator(seq)
    assert isinstance(it, NCollection_Sequence[Graphic3d.Graphic3d_ClipPlane].Iterator)
    assert [p.ToPlane().Location().Z() for p in it] == [1.0, 2.0, 3.0]        # R-ITER through the base
    it = Graphic3d.Graphic3d_SequenceOfHClipPlane.Iterator(seq)
    it.Next()
    seq.Remove(it)
    assert seq.Size() == 2


def test_width_twins_with_out_parameters_keep_the_plain_name():
    """Graphic3d_Vertex::Coord(double&...) / Coord(float&...) are R-WIDTH twins, not an R-COLLISION group (2026-09-22)."""
    v = Graphic3d.Graphic3d_Vertex(1.0, 2.0, 3.0)
    assert v.Coord() == (1.0, 2.0, 3.0) and not hasattr(v, "Coord__float__float__float")
    v.SetCoord(4, 5, 6)
    assert v.X() == 4.0 and Graphic3d.Graphic3d_Vertex(0.0, 0.0, 0.0).Distance(v) == pytest.approx((16 + 25 + 36) ** 0.5)
    tri = Graphic3d.Graphic3d_ArrayOfTriangles(3)
    assert tri.AddVertex(0.0, 0.0, 0.0) == 1 and tri.AddVertex(gp.gp_Pnt(1, 0, 0)) == 2 and tri.AddVertex(Quantity.NCollection_Vec3__float(0.0, 1.0, 0.0)) == 3
    assert tri.VertexNumber() == 3 and tri.Vertice(2).X() == 1.0 and tri.Vertice__float__float__float(2) == (1.0, 0.0, 0.0)


def test_report_lists_the_platform_and_codec_gaps():
    lines = [l for l in REPORT.read_text().splitlines() if not l.startswith("#")]
    cats = {l.split("\t")[0] for l in lines}
    assert "misc" not in cats
    assert any(re.match(r"incomplete\tMedia\tMedia_FormatContext::Stream\(unsigned int\): return: reference to incomplete type", l) for l in lines)   # FFmpeg types
    assert any(l.startswith("incomplete\tXw\tXw_Window::ProcessMessage") for l in lines)                                                        # XEvent
    assert any(l.startswith("override\tWNT\tWNT_Dword.hxx: skipped") for l in lines)                                                            # <windows.h>
    assert not any("Graphic3d_SequenceOfHClipPlane" in l for l in lines)
