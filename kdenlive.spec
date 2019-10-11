#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kdenlive
Version  : 19.08.2
Release  : 5
URL      : https://github.com/KDE/kdenlive/archive/v19.08.2/kdenlive-19.08.2.tar.gz
Source0  : https://github.com/KDE/kdenlive/archive/v19.08.2/kdenlive-19.08.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: kdenlive-bin = %{version}-%{release}
Requires: kdenlive-data = %{version}-%{release}
Requires: kdenlive-lib = %{version}-%{release}
Requires: kdenlive-license = %{version}-%{release}
Requires: kdenlive-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : git
BuildRequires : kfilemetadata-dev
BuildRequires : knotifyconfig-dev
BuildRequires : mlt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(mlt++)
BuildRequires : purpose-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : rttr-dev
BuildRequires : v4l-utils-dev

%description
KISS FFT - A mixed-radix Fast Fourier Transform based up on the principle,
"Keep It Simple, Stupid."

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


%package man
Summary: man components for the kdenlive package.
Group: Default

%description man
man components for the kdenlive package.


%prep
%setup -q -n kdenlive-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570829181
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570829181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdenlive
cp %{_builddir}/kdenlive-19.08.2/COPYING %{buildroot}/usr/share/package-licenses/kdenlive/b1c25bcf0e44653a0ab61b5e3a5b2841414d0033
cp %{_builddir}/kdenlive-19.08.2/src/lib/external/kiss_fft/COPYING %{buildroot}/usr/share/package-licenses/kdenlive/a46324c99fbefcdfe04c19a35296ad219a256efb
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kdenlive
/usr/bin/kdenlive_render

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kdenlive.desktop
/usr/share/config.kcfg/kdenlivesettings.kcfg
/usr/share/icons/hicolor/128x128/actions/kdenlive-select-all.png
/usr/share/icons/hicolor/128x128/apps/kdenlive.png
/usr/share/icons/hicolor/128x128/mimetypes/application-x-kdenlivetitle.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-add-clip.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-add-color-clip.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-add-slide-clip.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-add-text-clip.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-custom-effect.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-deleffect.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-down.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-hide-audio.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-hide-video.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-insert-edit.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-insert-rect.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-insert-unicode.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-lock.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-menu.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-normal-edit.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-object-height.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-object-width.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-overwrite-edit.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-select-all.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-select-images.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-select-rects.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-select-texts.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-select-tool.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-show-audio.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-show-audiothumb.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-show-markers.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-show-video.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-show-videothumb.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-snap.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-spacer-tool.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-split-audio.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-track_has_effect.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-unlock.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-unselect-all.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-up.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-zindex-up.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-zone-end.png
/usr/share/icons/hicolor/16x16/actions/kdenlive-zone-start.png
/usr/share/icons/hicolor/16x16/apps/kdenlive.png
/usr/share/icons/hicolor/22x22/actions/kdenlive-select-all.png
/usr/share/icons/hicolor/22x22/actions/kdenlive-spacer-tool.png
/usr/share/icons/hicolor/22x22/apps/kdenlive.png
/usr/share/icons/hicolor/256x256/apps/kdenlive.png
/usr/share/icons/hicolor/32x32/actions/kdenlive-select-all.png
/usr/share/icons/hicolor/32x32/apps/kdenlive.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-kdenlivetitle.png
/usr/share/icons/hicolor/48x48/actions/kdenlive-select-all.png
/usr/share/icons/hicolor/48x48/apps/kdenlive.png
/usr/share/icons/hicolor/64x64/actions/kdenlive-select-all.png
/usr/share/icons/hicolor/64x64/apps/kdenlive.png
/usr/share/icons/hicolor/64x64/mimetypes/application-x-kdenlivetitle.png
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-bottom.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-hor.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-left.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-none.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-right.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-top.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-align-vert.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-hide-audio-effects.svg
/usr/share/icons/hicolor/scalable/actions/kdenlive-hide-video-effects.svg
/usr/share/icons/hicolor/scalable/actions/kdenlive-insert-rect.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-insert-unicode.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-object-height.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-object-width.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-select-all.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-select-images.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-select-rects.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-select-texts.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-select-tool.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-show-all-effects.svg
/usr/share/icons/hicolor/scalable/actions/kdenlive-show-audio-effects.svg
/usr/share/icons/hicolor/scalable/actions/kdenlive-show-gpu-effects.svg
/usr/share/icons/hicolor/scalable/actions/kdenlive-show-video-effects.svg
/usr/share/icons/hicolor/scalable/actions/kdenlive-spacer-tool.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-unselect-all.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zindex-bottom.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zindex-down.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zindex-top.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zindex-up.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zone-end.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zone-start.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zoom-large.svgz
/usr/share/icons/hicolor/scalable/actions/kdenlive-zoom-small.svgz
/usr/share/icons/hicolor/scalable/apps/kdenlive.svgz
/usr/share/icons/hicolor/scalable/mimetypes/application-x-kdenlive.svgz
/usr/share/icons/hicolor/scalable/mimetypes/application-x-kdenlivetitle.svgz
/usr/share/icons/hicolor/scalable/mimetypes/video-mlt-playlist.svgz
/usr/share/kdenlive/banner.png
/usr/share/kdenlive/effects/acompressor.xml
/usr/share/kdenlive/effects/aecho.xml
/usr/share/kdenlive/effects/agate.xml
/usr/share/kdenlive/effects/audiobalance.xml
/usr/share/kdenlive/effects/audiopan.xml
/usr/share/kdenlive/effects/audiowave.xml
/usr/share/kdenlive/effects/audiowaveform.xml
/usr/share/kdenlive/effects/automask.xml
/usr/share/kdenlive/effects/avfilter_lut3d.xml
/usr/share/kdenlive/effects/boxblur.xml
/usr/share/kdenlive/effects/brightness.xml
/usr/share/kdenlive/effects/channelcopy.xml
/usr/share/kdenlive/effects/charcoal.xml
/usr/share/kdenlive/effects/chroma.xml
/usr/share/kdenlive/effects/chroma_hold.xml
/usr/share/kdenlive/effects/crop.xml
/usr/share/kdenlive/effects/dust.xml
/usr/share/kdenlive/effects/dynamictext.xml
/usr/share/kdenlive/effects/fade_from_black.xml
/usr/share/kdenlive/effects/fade_to_black.xml
/usr/share/kdenlive/effects/fadein.xml
/usr/share/kdenlive/effects/fadeout.xml
/usr/share/kdenlive/effects/freeze.xml
/usr/share/kdenlive/effects/frei0r_alpha0ps.xml
/usr/share/kdenlive/effects/frei0r_alphagrad.xml
/usr/share/kdenlive/effects/frei0r_alphaspot.xml
/usr/share/kdenlive/effects/frei0r_balanc0r.xml
/usr/share/kdenlive/effects/frei0r_baltan.xml
/usr/share/kdenlive/effects/frei0r_bezier_curves.xml
/usr/share/kdenlive/effects/frei0r_brightness.xml
/usr/share/kdenlive/effects/frei0r_c0rners.xml
/usr/share/kdenlive/effects/frei0r_cartoon.xml
/usr/share/kdenlive/effects/frei0r_cluster.xml
/usr/share/kdenlive/effects/frei0r_colgate.xml
/usr/share/kdenlive/effects/frei0r_coloradj_rgb.xml
/usr/share/kdenlive/effects/frei0r_colordistance.xml
/usr/share/kdenlive/effects/frei0r_colortap.xml
/usr/share/kdenlive/effects/frei0r_contrast0r.xml
/usr/share/kdenlive/effects/frei0r_curves.xml
/usr/share/kdenlive/effects/frei0r_d90stairsteppingfix.xml
/usr/share/kdenlive/effects/frei0r_defish0r.xml
/usr/share/kdenlive/effects/frei0r_delay0r.xml
/usr/share/kdenlive/effects/frei0r_delaygrab.xml
/usr/share/kdenlive/effects/frei0r_distort0r.xml
/usr/share/kdenlive/effects/frei0r_edgeglow.xml
/usr/share/kdenlive/effects/frei0r_equaliz0r.xml
/usr/share/kdenlive/effects/frei0r_facebl0r.xml
/usr/share/kdenlive/effects/frei0r_facedetect.xml
/usr/share/kdenlive/effects/frei0r_flippo.xml
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
/usr/share/kdenlive/effects/frei0r_rgbparade.xml
/usr/share/kdenlive/effects/frei0r_saturat0r.xml
/usr/share/kdenlive/effects/frei0r_scale0tilt.xml
/usr/share/kdenlive/effects/frei0r_scanline0r.xml
/usr/share/kdenlive/effects/frei0r_select0r.xml
/usr/share/kdenlive/effects/frei0r_sharpness.xml
/usr/share/kdenlive/effects/frei0r_sobel.xml
/usr/share/kdenlive/effects/frei0r_sopsat.xml
/usr/share/kdenlive/effects/frei0r_squareblur.xml
/usr/share/kdenlive/effects/frei0r_tehroxx0r.xml
/usr/share/kdenlive/effects/frei0r_three_point_balance.xml
/usr/share/kdenlive/effects/frei0r_threelay0r.xml
/usr/share/kdenlive/effects/frei0r_threshold0r.xml
/usr/share/kdenlive/effects/frei0r_timeout.xml
/usr/share/kdenlive/effects/frei0r_tint0r.xml
/usr/share/kdenlive/effects/frei0r_twolay0r.xml
/usr/share/kdenlive/effects/frei0r_vectorscope.xml
/usr/share/kdenlive/effects/frei0r_vertigo.xml
/usr/share/kdenlive/effects/frei0r_vignette.xml
/usr/share/kdenlive/effects/gain.xml
/usr/share/kdenlive/effects/gamma.xml
/usr/share/kdenlive/effects/grain.xml
/usr/share/kdenlive/effects/greyscale.xml
/usr/share/kdenlive/effects/invert.xml
/usr/share/kdenlive/effects/lift_gamma_gain.xml
/usr/share/kdenlive/effects/loudness.xml
/usr/share/kdenlive/effects/luma.xml
/usr/share/kdenlive/effects/mirror.xml
/usr/share/kdenlive/effects/movit_blur.xml
/usr/share/kdenlive/effects/movit_deconvolution_sharpen.xml
/usr/share/kdenlive/effects/movit_diffusion.xml
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
/usr/share/kdenlive/effects/qtblend.xml
/usr/share/kdenlive/effects/region.xml
/usr/share/kdenlive/effects/rotation.xml
/usr/share/kdenlive/effects/rotation_keyframable.xml
/usr/share/kdenlive/effects/rotoscoping.xml
/usr/share/kdenlive/effects/scratchlines.xml
/usr/share/kdenlive/effects/selectivecolor.xml
/usr/share/kdenlive/effects/sepia.xml
/usr/share/kdenlive/effects/sox_band.xml
/usr/share/kdenlive/effects/sox_bass.xml
/usr/share/kdenlive/effects/sox_echo.xml
/usr/share/kdenlive/effects/sox_flanger.xml
/usr/share/kdenlive/effects/sox_gain.xml
/usr/share/kdenlive/effects/sox_phaser.xml
/usr/share/kdenlive/effects/sox_stretch.xml
/usr/share/kdenlive/effects/speed.xml
/usr/share/kdenlive/effects/swapchannels.xml
/usr/share/kdenlive/effects/tcolor.xml
/usr/share/kdenlive/effects/threshold.xml
/usr/share/kdenlive/effects/tracker.xml
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
/usr/share/kdenlive/meta_ffmpeg.png
/usr/share/kdenlive/meta_libav.png
/usr/share/kdenlive/meta_magiclantern.png
/usr/share/kdenlive/metadata.properties
/usr/share/kdenlive/profiles/dci_2160p_2398
/usr/share/kdenlive/profiles/dci_2160p_24
/usr/share/kdenlive/profiles/dci_2160p_25
/usr/share/kdenlive/profiles/dci_2160p_2997
/usr/share/kdenlive/profiles/dci_2160p_30
/usr/share/kdenlive/profiles/dci_2160p_50
/usr/share/kdenlive/profiles/dci_2160p_5994
/usr/share/kdenlive/profiles/dci_2160p_60
/usr/share/kdenlive/timeline_athumbs.png
/usr/share/kdenlive/timeline_avthumbs.png
/usr/share/kdenlive/timeline_nothumbs.png
/usr/share/kdenlive/timeline_vthumbs.png
/usr/share/kdenlive/titles/simple-scroll.kdenlivetitle
/usr/share/kdenlive/titles/simple-with-date.kdenlivetitle
/usr/share/kdenlive/titles/simple.kdenlivetitle
/usr/share/kdenlive/transitions/affine.xml
/usr/share/kdenlive/transitions/composite.xml
/usr/share/kdenlive/transitions/dissolve.xml
/usr/share/kdenlive/transitions/frei0r_cairoaffineblend.xml
/usr/share/kdenlive/transitions/frei0r_cairoblend.xml
/usr/share/kdenlive/transitions/luma.xml
/usr/share/kdenlive/transitions/mix.xml
/usr/share/kdenlive/transitions/qtblend.xml
/usr/share/kdenlive/transitions/region.xml
/usr/share/kdenlive/transitions/slide.xml
/usr/share/kdenlive/transitions/wipe.xml
/usr/share/knotifications5/kdenlive.notifyrc
/usr/share/kservices5/mltpreview.desktop
/usr/share/kxmlgui5/kdenlive/kdenliveui.rc
/usr/share/metainfo/org.kde.kdenlive.appdata.xml
/usr/share/mime-packages/org.kde.kdenlive.xml
/usr/share/mime-packages/westley.xml
/usr/share/qlogging-categories5/kdenlive.categories
/usr/share/xdg/kdenlive_keyboardschemes.knsrc
/usr/share/xdg/kdenlive_renderprofiles.knsrc
/usr/share/xdg/kdenlive_titles.knsrc
/usr/share/xdg/kdenlive_wipes.knsrc

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/doc/Kdenlive/AUTHORS
/usr/share/doc/Kdenlive/COPYING
/usr/share/doc/Kdenlive/README.md

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/mltpreview.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdenlive/a46324c99fbefcdfe04c19a35296ad219a256efb
/usr/share/package-licenses/kdenlive/b1c25bcf0e44653a0ab61b5e3a5b2841414d0033

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/kdenlive.1
/usr/share/man/man1/kdenlive_render.1
