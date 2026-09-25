# The Linux build environment for nanoOCP: PyPA's manylinux_2_28 (AlmaLinux 8.10, glibc 2.28, gcc 14.2.1, cmake 4.4.3,
# auditwheel 6.8.2) plus the two things it does not ship. A modern compiler against an old glibc/libstdc++ baseline is
# exactly what a wheel needs, and it is the same image GitHub Actions uses, so the local build and CI are one thing.
#
# Deliberately NOT installed: freetype-devel. The image's is 2.9.1 (2018) and macOS and Windows build FreeType from
# source as a static library, so the container does the same -- the three OCCT builds stay comparable and the wheel
# carries no system FreeType.
FROM quay.io/pypa/manylinux_2_28_x86_64

# X11 and GLX: OCCT's own default on Linux is USE_XLIB=ON (its CMakeLists.txt:389 turns it off only for Apple and the
# no-Xlib platforms), and we follow it -- with OFF, OCCT goes through EGL, Xw_Window is a stub, and the viewer does not
# come up at all: "EGL display is unavailable" even on a box with /dev/dri (banach, 2026-09-23). The image already has
# libX11-devel; libXext, libXmu and GL/GLX come from here.
# fontconfig-devel: Font_FontMgr.cxx:86 includes <fontconfig/fontconfig.h> on Linux (macOS uses CoreText, Windows the
# registry), so without it TKService does not compile.
# The wheel must NOT bundle libGL/libGLX/libX11 -- graphics drivers and the window system belong to the host -- so
# `auditwheel repair` needs --exclude for them when the wheels are built.
RUN dnf -y -q install mesa-libGL-devel mesa-libEGL-devel libXext-devel libXmu-devel fontconfig-devel \
 && dnf -q clean all

# xorg-x11-server-Xvfb: the viewer tests need a display (USE_XLIB=ON), so `xvfb-run` has to be in the image --
# otherwise the suite can only run on the host, and Linux is meant to go through the container alone.
#
# mesa-dri-drivers and libglvnd-glx are what make that display usable: mesa-libGL-devel above satisfies the *link*,
# but without the swrast driver and the GLX vendor library the X server has no GLX extension and OCCT stops with
# "OpenGl_GraphicDriver, GLX extension is unavailable" / "couldn't find compatible Visual (RGBA, double-buffered)".
# Found 2026-09-24, the first time `make test` ran inside the container rather than on the host: 3 failed there and
# the same three passed on the host, which has llvmpipe. With these, Xvfb reports "direct rendering: Yes" on
# llvmpipe and test_TKOpenGl passes. glx-utils is only `glxinfo`, kept because it turns this diagnosis into one
# command.
RUN dnf -y -q install xorg-x11-server-Xvfb mesa-dri-drivers libglvnd-glx glx-utils && dnf -q clean all
# the image has no ninja, and powertools' is 1.8.2 (2018); the wheel is current
RUN /opt/python/cp312-cp312/bin/pip install --no-cache-dir -q ninja \
 && ln -s /opt/python/cp312-cp312/bin/ninja /usr/local/bin/ninja

# clang, for the generator only -- nothing here is compiled with it. The pip `libclang` wheel ships the shared library
# without the builtin headers, so a parse dies on `'stddef.h' file not found`; the distribution clang brings both the
# headers and the resource dir that parse.py's _resource_dir() looks for. AlmaLinux 8 has clang 21, the same major as
# the macOS toolchain, so all three platforms parse with a comparable frontend.
RUN dnf -y -q --enablerepo=appstream install clang && dnf -q clean all

# libclang picks the newest GCC it finds under /usr/lib/gcc, which in this image is gcc 8 -- but everything is compiled
# with gcc-toolset-14, whose libstdc++ headers live outside that tree. Without this the generator would read gcc 8's
# standard library while the build uses gcc 14's. parse.clang_args() appends NANOOCP_CLANG_ARGS verbatim.
ENV NANOOCP_CLANG_ARGS="--gcc-install-dir=/opt/rh/gcc-toolset-14/root/usr/lib/gcc/x86_64-redhat-linux/14"
