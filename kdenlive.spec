#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdenlive
Version  : 23.08.2
Release  : 52
URL      : https://download.kde.org/stable/release-service/23.08.2/src/kdenlive-23.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.2/src/kdenlive-23.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.2/src/kdenlive-23.08.2.tar.xz.sig
Summary  : A non-linear video editor for Linux using the MLT video framework
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: kdenlive-bin = %{version}-%{release}
Requires: kdenlive-data = %{version}-%{release}
Requires: kdenlive-lib = %{version}-%{release}
Requires: kdenlive-license = %{version}-%{release}
Requires: kdenlive-locales = %{version}-%{release}
Requires: kdenlive-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : kfilemetadata-dev
BuildRequires : knotifyconfig-dev
BuildRequires : mlt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(mlt++-7)
BuildRequires : purpose-dev
BuildRequires : rttr-dev
BuildRequires : v4l-utils-dev

%description
Kdenlive is a Free and Open Source video editing application, based on MLT
Framework and KDE Frameworks 5. It is distributed under the GNU General Public
Licence Version 2.

%package bin
Summary: bin components for the kdenlive package.
Group: Binaries
Requires: kdenlive-data = %{version}-%{release}
Requires: kdenlive-license = %{version}-%{release}

%description bin
bin components for the kdenlive package.


%package data
Summary: data components for the kdenlive package.
Group: Data

%description data
data components for the kdenlive package.


%package doc
Summary: doc components for the kdenlive package.
Group: Documentation
Requires: kdenlive-man = %{version}-%{release}

%description doc
doc components for the kdenlive package.


%package lib
Summary: lib components for the kdenlive package.
Group: Libraries
Requires: kdenlive-data = %{version}-%{release}
Requires: kdenlive-license = %{version}-%{release}

%description lib
lib components for the kdenlive package.


%package license
Summary: license components for the kdenlive package.
Group: Default

%description license
license components for the kdenlive package.


%package locales
Summary: locales components for the kdenlive package.
Group: Default

%description locales
locales components for the kdenlive package.


%package man
Summary: man components for the kdenlive package.
Group: Default

%description man
man components for the kdenlive package.


%prep
%setup -q -n kdenlive-23.08.2
cd %{_builddir}/kdenlive-23.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697410804
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697410804
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdenlive
cp %{_builddir}/kdenlive-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kdenlive/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdenlive/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/kdenlive/f26cccd93362d640ef2c05d1c52b5efe1620a9b2 || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdenlive/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdenlive/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdenlive/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdenlive/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdenlive/49e61f7864169f2e356c11a17422d7d20d74b40f || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdenlive/0d05dfdba8abf9192a31ac7ef555a76c10744d80 || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdenlive/0d05dfdba8abf9192a31ac7ef555a76c10744d80 || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdenlive/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdenlive-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdenlive/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdenlive-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kdenlive/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kdenlive-%{version}/packaging/flatpak/README.md.license %{buildroot}/usr/share/package-licenses/kdenlive/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kdenlive
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kdenlive
/V3/usr/bin/kdenlive_render
/usr/bin/kdenlive
/usr/bin/kdenlive_render

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kdenlive.desktop
/usr/share/config.kcfg/kdenlivesettings.kcfg
/usr/share/icons/hicolor/128x128/apps/kdenlive.png
/usr/share/icons/hicolor/128x128/mimetypes/application-x-kdenlivetitle.png
/usr/share/icons/hicolor/16x16/actions/add-subtitle.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-add.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-disable.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-duplicate.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-next.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-previous.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-record.svg
/usr/share/icons/hicolor/16x16/actions/keyframe-remove.svg
/usr/share/icons/hicolor/16x16/actions/keyframe.svg
/usr/share/icons/hicolor/16x16/apps/kdenlive.png
/usr/share/icons/hicolor/22x22/actions/keyframe-add.svg
/usr/share/icons/hicolor/22x22/actions/keyframe-disable.svg
/usr/share/icons/hicolor/22x22/actions/keyframe-duplicate.svg
/usr/share/icons/hicolor/22x22/actions/keyframe-next.svg
/usr/share/icons/hicolor/22x22/actions/keyframe-previous.svg
/usr/share/icons/hicolor/22x22/actions/keyframe-record.svg
/usr/share/icons/hicolor/22x22/actions/keyframe-remove.svg
/usr/share/icons/hicolor/22x22/actions/keyframe.svg
/usr/share/icons/hicolor/22x22/apps/kdenlive.png
/usr/share/icons/hicolor/256x256/apps/kdenlive.png
/usr/share/icons/hicolor/32x32/apps/kdenlive.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-kdenlivetitle.png
/usr/share/icons/hicolor/48x48/apps/kdenlive.png
/usr/share/icons/hicolor/64x64/apps/kdenlive.png
/usr/share/icons/hicolor/64x64/mimetypes/application-x-kdenlivetitle.png
/usr/share/icons/hicolor/scalable/actions/add-subtitle.svg
/usr/share/icons/hicolor/scalable/apps/kdenlive.svgz
/usr/share/icons/hicolor/scalable/mimetypes/application-x-kdenlive.svgz
/usr/share/icons/hicolor/scalable/mimetypes/application-x-kdenlivetitle.svgz
/usr/share/icons/hicolor/scalable/mimetypes/video-mlt-playlist.svgz
/usr/share/kdenlive/clipjobsettings.rc
/usr/share/kdenlive/effect-templates/secondary_color_correction.xml
/usr/share/kdenlive/effect-templates/shut_off.xml
/usr/share/kdenlive/effects/acompressor.xml
/usr/share/kdenlive/effects/aecho.xml
/usr/share/kdenlive/effects/agate.xml
/usr/share/kdenlive/effects/audiobalance.xml
/usr/share/kdenlive/effects/audiolevelgraph.xml
/usr/share/kdenlive/effects/audiomap.xml
/usr/share/kdenlive/effects/audiopan.xml
/usr/share/kdenlive/effects/audiospectrum.xml
/usr/share/kdenlive/effects/audiowave.xml
/usr/share/kdenlive/effects/audiowaveform.xml
/usr/share/kdenlive/effects/avfilter_acontrast.xml
/usr/share/kdenlive/effects/avfilter_acrusher.xml
/usr/share/kdenlive/effects/avfilter_alimiter.xml
/usr/share/kdenlive/effects/avfilter_allpass.xml
/usr/share/kdenlive/effects/avfilter_aphaser.xml
/usr/share/kdenlive/effects/avfilter_apulsator.xml
/usr/share/kdenlive/effects/avfilter_atadenoise.xml
/usr/share/kdenlive/effects/avfilter_avgblur.xml
/usr/share/kdenlive/effects/avfilter_bandpass.xml
/usr/share/kdenlive/effects/avfilter_bandreject.xml
/usr/share/kdenlive/effects/avfilter_bass.xml
/usr/share/kdenlive/effects/avfilter_bilateral.xml
/usr/share/kdenlive/effects/avfilter_boxblur.xml
/usr/share/kdenlive/effects/avfilter_bs2b.xml
/usr/share/kdenlive/effects/avfilter_bwdif.xml
/usr/share/kdenlive/effects/avfilter_cas.xml
/usr/share/kdenlive/effects/avfilter_chromahold.xml
/usr/share/kdenlive/effects/avfilter_chromanr.xml
/usr/share/kdenlive/effects/avfilter_chromashift.xml
/usr/share/kdenlive/effects/avfilter_colorbalance.xml
/usr/share/kdenlive/effects/avfilter_colorchannelmixer.xml
/usr/share/kdenlive/effects/avfilter_colorcontrast.xml
/usr/share/kdenlive/effects/avfilter_colorcorrect.xml
/usr/share/kdenlive/effects/avfilter_colorhold.xml
/usr/share/kdenlive/effects/avfilter_colorize.xml
/usr/share/kdenlive/effects/avfilter_colorlevels.xml
/usr/share/kdenlive/effects/avfilter_colormatrix.xml
/usr/share/kdenlive/effects/avfilter_colorspace.xml
/usr/share/kdenlive/effects/avfilter_colortemperature.xml
/usr/share/kdenlive/effects/avfilter_compand.xml
/usr/share/kdenlive/effects/avfilter_compensationdelay.xml
/usr/share/kdenlive/effects/avfilter_crossfeed.xml
/usr/share/kdenlive/effects/avfilter_crystalizer.xml
/usr/share/kdenlive/effects/avfilter_datascope.xml
/usr/share/kdenlive/effects/avfilter_dcshift.xml
/usr/share/kdenlive/effects/avfilter_dctdnoiz.xml
/usr/share/kdenlive/effects/avfilter_deband.xml
/usr/share/kdenlive/effects/avfilter_deblock.xml
/usr/share/kdenlive/effects/avfilter_dedot.xml
/usr/share/kdenlive/effects/avfilter_deesser.xml
/usr/share/kdenlive/effects/avfilter_deflate.xml
/usr/share/kdenlive/effects/avfilter_delogo.xml
/usr/share/kdenlive/effects/avfilter_derain.xml
/usr/share/kdenlive/effects/avfilter_despill.xml
/usr/share/kdenlive/effects/avfilter_dilation.xml
/usr/share/kdenlive/effects/avfilter_doubleweave.xml
/usr/share/kdenlive/effects/avfilter_drawbox.xml
/usr/share/kdenlive/effects/avfilter_drawgrid.xml
/usr/share/kdenlive/effects/avfilter_edgedetect.xml
/usr/share/kdenlive/effects/avfilter_elbg.xml
/usr/share/kdenlive/effects/avfilter_epx.xml
/usr/share/kdenlive/effects/avfilter_eq.xml
/usr/share/kdenlive/effects/avfilter_equalizer.xml
/usr/share/kdenlive/effects/avfilter_erosion.xml
/usr/share/kdenlive/effects/avfilter_exposure.xml
/usr/share/kdenlive/effects/avfilter_extrastereo.xml
/usr/share/kdenlive/effects/avfilter_fftdnoiz.xml
/usr/share/kdenlive/effects/avfilter_fftfilt.xml
/usr/share/kdenlive/effects/avfilter_field.xml
/usr/share/kdenlive/effects/avfilter_fieldorder.xml
/usr/share/kdenlive/effects/avfilter_fillborders.xml
/usr/share/kdenlive/effects/avfilter_flanger.xml
/usr/share/kdenlive/effects/avfilter_framestep.xml
/usr/share/kdenlive/effects/avfilter_fspp.xml
/usr/share/kdenlive/effects/avfilter_gblur.xml
/usr/share/kdenlive/effects/avfilter_graphmonitor.xml
/usr/share/kdenlive/effects/avfilter_haas.xml
/usr/share/kdenlive/effects/avfilter_hflip.xml
/usr/share/kdenlive/effects/avfilter_highpass.xml
/usr/share/kdenlive/effects/avfilter_highshelf.xml
/usr/share/kdenlive/effects/avfilter_histeq.xml
/usr/share/kdenlive/effects/avfilter_histogram.xml
/usr/share/kdenlive/effects/avfilter_hqdn3d.xml
/usr/share/kdenlive/effects/avfilter_hqx.xml
/usr/share/kdenlive/effects/avfilter_il.xml
/usr/share/kdenlive/effects/avfilter_inflate.xml
/usr/share/kdenlive/effects/avfilter_kerneldeint.xml
/usr/share/kdenlive/effects/avfilter_kirsch.xml
/usr/share/kdenlive/effects/avfilter_lagfun.xml
/usr/share/kdenlive/effects/avfilter_lenscorrection.xml
/usr/share/kdenlive/effects/avfilter_limiter.xml
/usr/share/kdenlive/effects/avfilter_loudnorm.xml
/usr/share/kdenlive/effects/avfilter_lowpass.xml
/usr/share/kdenlive/effects/avfilter_lowshelf.xml
/usr/share/kdenlive/effects/avfilter_lut3d.xml
/usr/share/kdenlive/effects/avfilter_mcdeint.xml
/usr/share/kdenlive/effects/avfilter_median.xml
/usr/share/kdenlive/effects/avfilter_monochrome.xml
/usr/share/kdenlive/effects/avfilter_negate.xml
/usr/share/kdenlive/effects/avfilter_noise.xml
/usr/share/kdenlive/effects/avfilter_normalize.xml
/usr/share/kdenlive/effects/avfilter_phase.xml
/usr/share/kdenlive/effects/avfilter_photosensitivity.xml
/usr/share/kdenlive/effects/avfilter_prewitt.xml
/usr/share/kdenlive/effects/avfilter_random.xml
/usr/share/kdenlive/effects/avfilter_removegrain.xml
/usr/share/kdenlive/effects/avfilter_rgbashift.xml
/usr/share/kdenlive/effects/avfilter_roberts.xml
/usr/share/kdenlive/effects/avfilter_sab.xml
/usr/share/kdenlive/effects/avfilter_scroll.xml
/usr/share/kdenlive/effects/avfilter_selectivecolor.xml
/usr/share/kdenlive/effects/avfilter_separatefields.xml
/usr/share/kdenlive/effects/avfilter_setrange.xml
/usr/share/kdenlive/effects/avfilter_shear.xml
/usr/share/kdenlive/effects/avfilter_shuffleplanes.xml
/usr/share/kdenlive/effects/avfilter_smartblur.xml
/usr/share/kdenlive/effects/avfilter_sobel.xml
/usr/share/kdenlive/effects/avfilter_sofalizer.xml
/usr/share/kdenlive/effects/avfilter_sr.xml
/usr/share/kdenlive/effects/avfilter_stereo3D.xml
/usr/share/kdenlive/effects/avfilter_stereotools.xml
/usr/share/kdenlive/effects/avfilter_stereowiden.xml
/usr/share/kdenlive/effects/avfilter_tmix.xml
/usr/share/kdenlive/effects/avfilter_transpose.xml
/usr/share/kdenlive/effects/avfilter_unsharp.xml
/usr/share/kdenlive/effects/avfilter_vaguedenoiser.xml
/usr/share/kdenlive/effects/avfilter_vectorscope.xml
/usr/share/kdenlive/effects/avfilter_vflip.xml
/usr/share/kdenlive/effects/avfilter_vibrance.xml
/usr/share/kdenlive/effects/avfilter_vibrato.xml
/usr/share/kdenlive/effects/avfilter_w3fdif.xml
/usr/share/kdenlive/effects/avfilter_waveform.xml
/usr/share/kdenlive/effects/avfilter_weave.xml
/usr/share/kdenlive/effects/avfilter_xbr.xml
/usr/share/kdenlive/effects/avfilter_yadif.xml
/usr/share/kdenlive/effects/avfilter_zoompan.xml
/usr/share/kdenlive/effects/box_blur.xml
/usr/share/kdenlive/effects/boxblur.xml
/usr/share/kdenlive/effects/brightness.xml
/usr/share/kdenlive/effects/channelcopy.xml
/usr/share/kdenlive/effects/charcoal.xml
/usr/share/kdenlive/effects/chroma.xml
/usr/share/kdenlive/effects/chroma_hold.xml
/usr/share/kdenlive/effects/copychannelstostereo.xml
/usr/share/kdenlive/effects/crop.xml
/usr/share/kdenlive/effects/dance.xml
/usr/share/kdenlive/effects/dust.xml
/usr/share/kdenlive/effects/dynamic_loudness.xml
/usr/share/kdenlive/effects/dynamictext.xml
/usr/share/kdenlive/effects/fade_from_black.xml
/usr/share/kdenlive/effects/fade_to_black.xml
/usr/share/kdenlive/effects/fadein.xml
/usr/share/kdenlive/effects/fadeout.xml
/usr/share/kdenlive/effects/freeze.xml
/usr/share/kdenlive/effects/frei0r_B.xml
/usr/share/kdenlive/effects/frei0r_G.xml
/usr/share/kdenlive/effects/frei0r_R.xml
/usr/share/kdenlive/effects/frei0r_alpha0ps.xml
/usr/share/kdenlive/effects/frei0r_alphagrad.xml
/usr/share/kdenlive/effects/frei0r_alphaspot.xml
/usr/share/kdenlive/effects/frei0r_balanc0r.xml
/usr/share/kdenlive/effects/frei0r_baltan.xml
/usr/share/kdenlive/effects/frei0r_bezier_curves.xml
/usr/share/kdenlive/effects/frei0r_bgsubtract0r.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_eq_mask.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_eq_to_rect.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_eq_to_stereo.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_hemi_to_eq.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_rect_to_eq.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_stabilize_360.xml
/usr/share/kdenlive/effects/frei0r_bigsh0t_transform_360.xml
/usr/share/kdenlive/effects/frei0r_brightness.xml
/usr/share/kdenlive/effects/frei0r_c0rners.xml
/usr/share/kdenlive/effects/frei0r_cairogradient.xml
/usr/share/kdenlive/effects/frei0r_cairoimagegrid.xml
/usr/share/kdenlive/effects/frei0r_cartoon.xml
/usr/share/kdenlive/effects/frei0r_cluster.xml
/usr/share/kdenlive/effects/frei0r_colgate.xml
/usr/share/kdenlive/effects/frei0r_coloradj_rgb.xml
/usr/share/kdenlive/effects/frei0r_colordistance.xml
/usr/share/kdenlive/effects/frei0r_colorize.xml
/usr/share/kdenlive/effects/frei0r_colortap.xml
/usr/share/kdenlive/effects/frei0r_contrast0r.xml
/usr/share/kdenlive/effects/frei0r_curves.xml
/usr/share/kdenlive/effects/frei0r_d90stairsteppingfix.xml
/usr/share/kdenlive/effects/frei0r_defish0r.xml
/usr/share/kdenlive/effects/frei0r_delay0r.xml
/usr/share/kdenlive/effects/frei0r_delaygrab.xml
/usr/share/kdenlive/effects/frei0r_distort0r.xml
/usr/share/kdenlive/effects/frei0r_dither.xml
/usr/share/kdenlive/effects/frei0r_edgeglow.xml
/usr/share/kdenlive/effects/frei0r_emboss.xml
/usr/share/kdenlive/effects/frei0r_equaliz0r.xml
/usr/share/kdenlive/effects/frei0r_facebl0r.xml
/usr/share/kdenlive/effects/frei0r_facedetect.xml
/usr/share/kdenlive/effects/frei0r_flippo.xml
/usr/share/kdenlive/effects/frei0r_glitch0r.xml
/usr/share/kdenlive/effects/frei0r_glow.xml
/usr/share/kdenlive/effects/frei0r_hqdn3d.xml
/usr/share/kdenlive/effects/frei0r_hueshift0r.xml
/usr/share/kdenlive/effects/frei0r_iirblur.xml
/usr/share/kdenlive/effects/frei0r_keyspillm0pup.xml
/usr/share/kdenlive/effects/frei0r_lenscorrection.xml
/usr/share/kdenlive/effects/frei0r_letterb0xed.xml
/usr/share/kdenlive/effects/frei0r_levels.xml
/usr/share/kdenlive/effects/frei0r_lightgraffiti.xml
/usr/share/kdenlive/effects/frei0r_luminance.xml
/usr/share/kdenlive/effects/frei0r_mask0mate.xml
/usr/share/kdenlive/effects/frei0r_medians.xml
/usr/share/kdenlive/effects/frei0r_nervous.xml
/usr/share/kdenlive/effects/frei0r_nosync0r.xml
/usr/share/kdenlive/effects/frei0r_pixeliz0r.xml
/usr/share/kdenlive/effects/frei0r_pr0be.xml
/usr/share/kdenlive/effects/frei0r_pr0file.xml
/usr/share/kdenlive/effects/frei0r_primaries.xml
/usr/share/kdenlive/effects/frei0r_rgbnoise.xml
/usr/share/kdenlive/effects/frei0r_rgbparade.xml
/usr/share/kdenlive/effects/frei0r_rgbsplit0r.xml
/usr/share/kdenlive/effects/frei0r_saturat0r.xml
/usr/share/kdenlive/effects/frei0r_scale0tilt.xml
/usr/share/kdenlive/effects/frei0r_scanline0r.xml
/usr/share/kdenlive/effects/frei0r_select0r.xml
/usr/share/kdenlive/effects/frei0r_sharpness.xml
/usr/share/kdenlive/effects/frei0r_sigmoidaltransfer.xml
/usr/share/kdenlive/effects/frei0r_sobel.xml
/usr/share/kdenlive/effects/frei0r_softglow.xml
/usr/share/kdenlive/effects/frei0r_sopsat.xml
/usr/share/kdenlive/effects/frei0r_squareblur.xml
/usr/share/kdenlive/effects/frei0r_tehroxx0r.xml
/usr/share/kdenlive/effects/frei0r_three_point_balance.xml
/usr/share/kdenlive/effects/frei0r_threelay0r.xml
/usr/share/kdenlive/effects/frei0r_threshold0r.xml
/usr/share/kdenlive/effects/frei0r_timeout.xml
/usr/share/kdenlive/effects/frei0r_tint0r.xml
/usr/share/kdenlive/effects/frei0r_transparency.xml
/usr/share/kdenlive/effects/frei0r_twolay0r.xml
/usr/share/kdenlive/effects/frei0r_vectorscope.xml
/usr/share/kdenlive/effects/frei0r_vertigo.xml
/usr/share/kdenlive/effects/frei0r_vignette.xml
/usr/share/kdenlive/effects/gain.xml
/usr/share/kdenlive/effects/gamma.xml
/usr/share/kdenlive/effects/gpstext.xml
/usr/share/kdenlive/effects/grain.xml
/usr/share/kdenlive/effects/greyscale.xml
/usr/share/kdenlive/effects/invert.xml
/usr/share/kdenlive/effects/ladspa_declipper.xml
/usr/share/kdenlive/effects/ladspa_equalizer.xml
/usr/share/kdenlive/effects/ladspa_equalizer_15.xml
/usr/share/kdenlive/effects/ladspa_librnnoise.xml
/usr/share/kdenlive/effects/ladspa_limiter.xml
/usr/share/kdenlive/effects/ladspa_phaser.xml
/usr/share/kdenlive/effects/ladspa_pitch.xml
/usr/share/kdenlive/effects/ladspa_pitch_scale.xml
/usr/share/kdenlive/effects/ladspa_rate_scale.xml
/usr/share/kdenlive/effects/ladspa_reverb.xml
/usr/share/kdenlive/effects/ladspa_room_reverb.xml
/usr/share/kdenlive/effects/ladspa_vinyl.xml
/usr/share/kdenlive/effects/lift_gamma_gain.xml
/usr/share/kdenlive/effects/lightshow.xml
/usr/share/kdenlive/effects/loudness.xml
/usr/share/kdenlive/effects/luma.xml
/usr/share/kdenlive/effects/lumaliftgaingamma.xml
/usr/share/kdenlive/effects/mask_apply.xml
/usr/share/kdenlive/effects/mask_start.xml
/usr/share/kdenlive/effects/mask_start_frei0r_alphaspot.xml
/usr/share/kdenlive/effects/mask_start_frei0r_select0r.xml
/usr/share/kdenlive/effects/mask_start_rotoscoping.xml
/usr/share/kdenlive/effects/mask_start_shape.xml
/usr/share/kdenlive/effects/mirror.xml
/usr/share/kdenlive/effects/mono.xml
/usr/share/kdenlive/effects/movit_blur.xml
/usr/share/kdenlive/effects/movit_deconvolution_sharpen.xml
/usr/share/kdenlive/effects/movit_diffusion.xml
/usr/share/kdenlive/effects/movit_flip.xml
/usr/share/kdenlive/effects/movit_glow.xml
/usr/share/kdenlive/effects/movit_lift_gamma_gain.xml
/usr/share/kdenlive/effects/movit_mirror.xml
/usr/share/kdenlive/effects/movit_opacity.xml
/usr/share/kdenlive/effects/movit_rect.xml
/usr/share/kdenlive/effects/movit_saturation.xml
/usr/share/kdenlive/effects/movit_unsharp_mask.xml
/usr/share/kdenlive/effects/movit_vignette.xml
/usr/share/kdenlive/effects/movit_white_balance.xml
/usr/share/kdenlive/effects/mute.xml
/usr/share/kdenlive/effects/normalise.xml
/usr/share/kdenlive/effects/obscure.xml
/usr/share/kdenlive/effects/oldfilm.xml
/usr/share/kdenlive/effects/pan_zoom.xml
/usr/share/kdenlive/effects/pillar_echo.xml
/usr/share/kdenlive/effects/qtblend.xml
/usr/share/kdenlive/effects/qtcrop.xml
/usr/share/kdenlive/effects/rboctaveshift.xml
/usr/share/kdenlive/effects/rbpitchscale.xml
/usr/share/kdenlive/effects/rotation.xml
/usr/share/kdenlive/effects/rotation_keyframable.xml
/usr/share/kdenlive/effects/rotoscoping.xml
/usr/share/kdenlive/effects/scratchlines.xml
/usr/share/kdenlive/effects/sepia.xml
/usr/share/kdenlive/effects/shape.xml
/usr/share/kdenlive/effects/sox_band.xml
/usr/share/kdenlive/effects/sox_bass.xml
/usr/share/kdenlive/effects/sox_echo.xml
/usr/share/kdenlive/effects/sox_flanger.xml
/usr/share/kdenlive/effects/sox_gain.xml
/usr/share/kdenlive/effects/sox_phaser.xml
/usr/share/kdenlive/effects/sox_stretch.xml
/usr/share/kdenlive/effects/speed.xml
/usr/share/kdenlive/effects/spot_remover.xml
/usr/share/kdenlive/effects/subtitles.xml
/usr/share/kdenlive/effects/swapchannels.xml
/usr/share/kdenlive/effects/tcolor.xml
/usr/share/kdenlive/effects/threshold.xml
/usr/share/kdenlive/effects/timer.xml
/usr/share/kdenlive/effects/tracker.xml
/usr/share/kdenlive/effects/typewriter.xml
/usr/share/kdenlive/effects/update/frei0r.balanc0r.js
/usr/share/kdenlive/effects/update/frei0r.cartoon.js
/usr/share/kdenlive/effects/update/frei0r.curves.js
/usr/share/kdenlive/effects/update/frei0r.levels.js
/usr/share/kdenlive/effects/update/frei0r.lightgraffiti.js
/usr/share/kdenlive/effects/update/frei0r.select0r.js
/usr/share/kdenlive/effects/update/frei0r.sopsat.js
/usr/share/kdenlive/effects/update/frei0r.vertigo.js
/usr/share/kdenlive/effects/vidstab.xml
/usr/share/kdenlive/effects/vignette.xml
/usr/share/kdenlive/effects/volume.xml
/usr/share/kdenlive/effects/wave.xml
/usr/share/kdenlive/encodingprofiles.rc
/usr/share/kdenlive/export/profiles.xml
/usr/share/kdenlive/externalproxies.rc
/usr/share/kdenlive/generators/count.xml
/usr/share/kdenlive/generators/frei0r_test_pat_b.xml
/usr/share/kdenlive/generators/noise.xml
/usr/share/kdenlive/kdenlivedefaultlayouts.rc
/usr/share/kdenlive/kdenliveeffectscategory.rc
/usr/share/kdenlive/kdenlivetranscodingrc
/usr/share/kdenlive/lumas/HD/bi-linear_x.pgm
/usr/share/kdenlive/lumas/HD/bi-linear_y.pgm
/usr/share/kdenlive/lumas/HD/burst.pgm
/usr/share/kdenlive/lumas/HD/checkerboard_small.pgm
/usr/share/kdenlive/lumas/HD/clock.pgm
/usr/share/kdenlive/lumas/HD/cloud.pgm
/usr/share/kdenlive/lumas/HD/curtain.pgm
/usr/share/kdenlive/lumas/HD/horizontal_blinds.pgm
/usr/share/kdenlive/lumas/HD/linear_x.pgm
/usr/share/kdenlive/lumas/HD/linear_y.pgm
/usr/share/kdenlive/lumas/HD/radial-bars.pgm
/usr/share/kdenlive/lumas/HD/radial.pgm
/usr/share/kdenlive/lumas/HD/spiral.pgm
/usr/share/kdenlive/lumas/HD/spiral2.pgm
/usr/share/kdenlive/lumas/HD/square.pgm
/usr/share/kdenlive/lumas/HD/square2-bars.pgm
/usr/share/kdenlive/lumas/HD/square2.pgm
/usr/share/kdenlive/lumas/HD/symmetric_clock.pgm
/usr/share/kdenlive/lumas/PAL/bi-linear_x.pgm
/usr/share/kdenlive/lumas/PAL/bi-linear_y.pgm
/usr/share/kdenlive/lumas/PAL/burst.pgm
/usr/share/kdenlive/lumas/PAL/checkerboard_small.pgm
/usr/share/kdenlive/lumas/PAL/clock.pgm
/usr/share/kdenlive/lumas/PAL/cloud.pgm
/usr/share/kdenlive/lumas/PAL/curtain.pgm
/usr/share/kdenlive/lumas/PAL/horizontal_blinds.pgm
/usr/share/kdenlive/lumas/PAL/linear_x.pgm
/usr/share/kdenlive/lumas/PAL/linear_y.pgm
/usr/share/kdenlive/lumas/PAL/radial-bars.pgm
/usr/share/kdenlive/lumas/PAL/radial.pgm
/usr/share/kdenlive/lumas/PAL/spiral.pgm
/usr/share/kdenlive/lumas/PAL/spiral2.pgm
/usr/share/kdenlive/lumas/PAL/square.pgm
/usr/share/kdenlive/lumas/PAL/square2-bars.pgm
/usr/share/kdenlive/lumas/PAL/square2.pgm
/usr/share/kdenlive/lumas/PAL/symmetric_clock.pgm
/usr/share/kdenlive/luts/BLUE_TINT.cube
/usr/share/kdenlive/luts/CINEMATIC.cube
/usr/share/kdenlive/luts/GREEN_TINT.cube
/usr/share/kdenlive/luts/TEAL_ORANGE.cube
/usr/share/kdenlive/meta_magiclantern.png
/usr/share/kdenlive/profiles/dci_2160p_2398
/usr/share/kdenlive/profiles/dci_2160p_24
/usr/share/kdenlive/profiles/dci_2160p_25
/usr/share/kdenlive/profiles/dci_2160p_2997
/usr/share/kdenlive/profiles/dci_2160p_30
/usr/share/kdenlive/profiles/dci_2160p_50
/usr/share/kdenlive/profiles/dci_2160p_5994
/usr/share/kdenlive/profiles/dci_2160p_60
/usr/share/kdenlive/resourceproviders/archiveorg.json
/usr/share/kdenlive/resourceproviders/freesound.json
/usr/share/kdenlive/resourceproviders/pexels_photo.json
/usr/share/kdenlive/resourceproviders/pexels_video.json
/usr/share/kdenlive/resourceproviders/pixabay_photo.json
/usr/share/kdenlive/scripts/checkgpu.py
/usr/share/kdenlive/scripts/checkpackages.py
/usr/share/kdenlive/scripts/otiointerface.py
/usr/share/kdenlive/scripts/speech.py
/usr/share/kdenlive/scripts/speechtotext.py
/usr/share/kdenlive/scripts/whispertosrt.py
/usr/share/kdenlive/scripts/whispertotext.py
/usr/share/kdenlive/shortcuts/Premiere
/usr/share/kdenlive/slideanimations.rc
/usr/share/kdenlive/titles/simple-scroll.kdenlivetitle
/usr/share/kdenlive/titles/simple-with-date.kdenlivetitle
/usr/share/kdenlive/titles/simple.kdenlivetitle
/usr/share/kdenlive/transitions/affine.xml
/usr/share/kdenlive/transitions/composite.xml
/usr/share/kdenlive/transitions/dissolve.xml
/usr/share/kdenlive/transitions/frei0r_addition.xml
/usr/share/kdenlive/transitions/frei0r_addition_alpha.xml
/usr/share/kdenlive/transitions/frei0r_alphaatop.xml
/usr/share/kdenlive/transitions/frei0r_alphain.xml
/usr/share/kdenlive/transitions/frei0r_alphaout.xml
/usr/share/kdenlive/transitions/frei0r_alphaover.xml
/usr/share/kdenlive/transitions/frei0r_alphaxor.xml
/usr/share/kdenlive/transitions/frei0r_burn.xml
/usr/share/kdenlive/transitions/frei0r_cairoaffineblend.xml
/usr/share/kdenlive/transitions/frei0r_cairoblend.xml
/usr/share/kdenlive/transitions/frei0r_color_only.xml
/usr/share/kdenlive/transitions/frei0r_darken.xml
/usr/share/kdenlive/transitions/frei0r_difference.xml
/usr/share/kdenlive/transitions/frei0r_divide.xml
/usr/share/kdenlive/transitions/frei0r_dodge.xml
/usr/share/kdenlive/transitions/frei0r_grain_extract.xml
/usr/share/kdenlive/transitions/frei0r_grain_merge.xml
/usr/share/kdenlive/transitions/frei0r_hardlight.xml
/usr/share/kdenlive/transitions/frei0r_hue.xml
/usr/share/kdenlive/transitions/frei0r_lighten.xml
/usr/share/kdenlive/transitions/frei0r_multiply.xml
/usr/share/kdenlive/transitions/frei0r_overlay.xml
/usr/share/kdenlive/transitions/frei0r_push-down.xml
/usr/share/kdenlive/transitions/frei0r_push-left.xml
/usr/share/kdenlive/transitions/frei0r_push-right.xml
/usr/share/kdenlive/transitions/frei0r_push-up.xml
/usr/share/kdenlive/transitions/frei0r_saturation.xml
/usr/share/kdenlive/transitions/frei0r_screen.xml
/usr/share/kdenlive/transitions/frei0r_slide-down.xml
/usr/share/kdenlive/transitions/frei0r_slide-left.xml
/usr/share/kdenlive/transitions/frei0r_slide-right.xml
/usr/share/kdenlive/transitions/frei0r_slide-up.xml
/usr/share/kdenlive/transitions/frei0r_softlight.xml
/usr/share/kdenlive/transitions/frei0r_subtract.xml
/usr/share/kdenlive/transitions/frei0r_uvmap.xml
/usr/share/kdenlive/transitions/frei0r_value.xml
/usr/share/kdenlive/transitions/frei0r_wipe-barn-door-h.xml
/usr/share/kdenlive/transitions/frei0r_wipe-barn-door-v.xml
/usr/share/kdenlive/transitions/frei0r_wipe-circle.xml
/usr/share/kdenlive/transitions/frei0r_wipe-down.xml
/usr/share/kdenlive/transitions/frei0r_wipe-left.xml
/usr/share/kdenlive/transitions/frei0r_wipe-rect.xml
/usr/share/kdenlive/transitions/frei0r_wipe-right.xml
/usr/share/kdenlive/transitions/frei0r_wipe-up.xml
/usr/share/kdenlive/transitions/luma.xml
/usr/share/kdenlive/transitions/matte.xml
/usr/share/kdenlive/transitions/mix.xml
/usr/share/kdenlive/transitions/qtblend.xml
/usr/share/kdenlive/transitions/region.xml
/usr/share/kdenlive/transitions/slide.xml
/usr/share/kdenlive/transitions/vqm.xml
/usr/share/kdenlive/transitions/wipe.xml
/usr/share/knotifications5/kdenlive.notifyrc
/usr/share/knsrcfiles/kdenlive_effects.knsrc
/usr/share/knsrcfiles/kdenlive_keyboardschemes.knsrc
/usr/share/knsrcfiles/kdenlive_luts.knsrc
/usr/share/knsrcfiles/kdenlive_renderprofiles.knsrc
/usr/share/knsrcfiles/kdenlive_titles.knsrc
/usr/share/knsrcfiles/kdenlive_wipes.knsrc
/usr/share/metainfo/org.kde.kdenlive.appdata.xml
/usr/share/mime-packages/org.kde.kdenlive.xml
/usr/share/mime-packages/westley.xml
/usr/share/qlogging-categories5/kdenlive.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kdenlive/index.cache.bz2
/usr/share/doc/HTML/ca/kdenlive/index.docbook
/usr/share/doc/HTML/ca/kdenlive/kdenlive_quickstart-renderer.png
/usr/share/doc/HTML/ca/kdenlive/kdenlive_quickstart-save-project.png
/usr/share/doc/HTML/ca/kdenlive/kdenlive_quickstart-timeline-clips.png
/usr/share/doc/HTML/de/kdenlive/index.cache.bz2
/usr/share/doc/HTML/de/kdenlive/index.docbook
/usr/share/doc/HTML/de/kdenlive/kdenlive_quickstart-add-clips.png
/usr/share/doc/HTML/de/kdenlive/kdenlive_quickstart-new-project.png
/usr/share/doc/HTML/de/kdenlive/kdenlive_quickstart-save-project.png
/usr/share/doc/HTML/en/kdenlive/index.cache.bz2
/usr/share/doc/HTML/en/kdenlive/index.docbook
/usr/share/doc/HTML/en/kdenlive/kdenlive-quickstart-add-last-clip.png
/usr/share/doc/HTML/en/kdenlive/kdenlive-quickstart-add-transition.png
/usr/share/doc/HTML/en/kdenlive/kdenlive-quickstart-effectstack.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-add-clips.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-add-effect.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-effect-flag.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-fadeout.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-folder-structure.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-keyframes.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-mainwindow.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-new-project.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-overlap-clips.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-renderer.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-rendering.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-resize-marker.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-save-project.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-timeline-clips.png
/usr/share/doc/HTML/en/kdenlive/kdenlive_quickstart-timelinecursor.png
/usr/share/doc/HTML/es/kdenlive/index.cache.bz2
/usr/share/doc/HTML/es/kdenlive/index.docbook
/usr/share/doc/HTML/fr/kdenlive/Kdenlive-Quickstart-Add-Last-Clip.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive-Quickstart-Add-Transition.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Add-Clips.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Fadeout.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Folder-Structure.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Mainwindow.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Renderer.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Rendering.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Save-Project.png
/usr/share/doc/HTML/fr/kdenlive/Kdenlive_Quickstart-Timeline-Clips.png
/usr/share/doc/HTML/fr/kdenlive/index.cache.bz2
/usr/share/doc/HTML/fr/kdenlive/index.docbook
"/usr/share/doc/HTML/fr/kdenlive/section 1 - screen 2.png"
/usr/share/doc/HTML/id/kdenlive/index.cache.bz2
/usr/share/doc/HTML/id/kdenlive/index.docbook
/usr/share/doc/HTML/it/kdenlive/index.cache.bz2
/usr/share/doc/HTML/it/kdenlive/index.docbook
/usr/share/doc/HTML/nl/kdenlive/index.cache.bz2
/usr/share/doc/HTML/nl/kdenlive/index.docbook
/usr/share/doc/HTML/pt/kdenlive/index.cache.bz2
/usr/share/doc/HTML/pt/kdenlive/index.docbook
/usr/share/doc/HTML/pt_BR/kdenlive/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kdenlive/index.docbook
/usr/share/doc/HTML/ru/kdenlive/index.cache.bz2
/usr/share/doc/HTML/ru/kdenlive/index.docbook
/usr/share/doc/HTML/ru/kdenlive/kdenlive-quickstart-add-last-clip.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive-quickstart-add-transition.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive-quickstart-effectstack.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-add-clips.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-add-effect.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-effect-flag.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-fadeout.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-folder-structure.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-keyframes.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-mainwindow.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-new-project.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-overlap-clips.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-renderer.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-rendering.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-resize-marker.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-save-project.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-timeline-clips.png
/usr/share/doc/HTML/ru/kdenlive/kdenlive_quickstart-timelinecursor.png
/usr/share/doc/HTML/sv/kdenlive/index.cache.bz2
/usr/share/doc/HTML/sv/kdenlive/index.docbook
/usr/share/doc/HTML/uk/kdenlive/index.cache.bz2
/usr/share/doc/HTML/uk/kdenlive/index.docbook
/usr/share/doc/HTML/uk/kdenlive/kdenlive-quickstart-add-last-clip.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive-quickstart-add-transition.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-add-clips.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-add-effect.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-effect-flag.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-fadeout.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-folder-structure.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-mainwindow.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-new-project.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-overlap-clips.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-renderer.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-rendering.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-resize-marker.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-save-project.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-timeline-clips.png
/usr/share/doc/HTML/uk/kdenlive/kdenlive_quickstart-timelinecursor.png
/usr/share/doc/Kdenlive/AUTHORS
/usr/share/doc/Kdenlive/LICENSES/BSD-3-Clause.txt
/usr/share/doc/Kdenlive/LICENSES/BSL-1.0.txt
/usr/share/doc/Kdenlive/LICENSES/CC-BY-SA-4.0.txt
/usr/share/doc/Kdenlive/LICENSES/CC0-1.0.txt
/usr/share/doc/Kdenlive/LICENSES/GPL-2.0-only.txt
/usr/share/doc/Kdenlive/LICENSES/GPL-3.0-only.txt
/usr/share/doc/Kdenlive/LICENSES/GPL-3.0-or-later.txt
/usr/share/doc/Kdenlive/LICENSES/LGPL-3.0-only.txt
/usr/share/doc/Kdenlive/LICENSES/LicenseRef-KDE-Accepted-GPL.txt
/usr/share/doc/Kdenlive/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt
/usr/share/doc/Kdenlive/README.md

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/thumbcreator/mltpreview.so
/usr/lib64/qt5/plugins/kf5/thumbcreator/mltpreview.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdenlive/0d05dfdba8abf9192a31ac7ef555a76c10744d80
/usr/share/package-licenses/kdenlive/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/kdenlive/49e61f7864169f2e356c11a17422d7d20d74b40f
/usr/share/package-licenses/kdenlive/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kdenlive/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdenlive/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f
/usr/share/package-licenses/kdenlive/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kdenlive/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe
/usr/share/package-licenses/kdenlive/f26cccd93362d640ef2c05d1c52b5efe1620a9b2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/kdenlive.1
/usr/share/man/man1/kdenlive_render.1

%files locales -f kdenlive.lang
%defattr(-,root,root,-)

