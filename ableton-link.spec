%define short_name Link

Name: ableton-link
Version: 3.1.0
Release: alt1

Summary: Synchronizes musical beat, tempo, and phase across multiple applications
License: GPL-2.0-or-later
Group: Sound
Url: https://github.com/Ableton/link

# Source-url: https://github.com/Ableton/link/archive/refs/tags/%short_name-%version.tar.gz
Source: %name-%version.tar

Patch: abletonlink-3.1.0-devendor_asio_and_catch2-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake make gcc-c++ libc++-devel
BuildRequires: libportaudio2-devel asio-devel pipewire-jack-libs-devel catch2-devel

%description
This is the codebase for Ableton Link, a technology that synchronizes musical beat, tempo, and phase across multiple applications running on one or more devices. Applications on devices connected to a local network discover each other automatically and form a musical session in which each participant can perform independently: anyone can start or stop while still staying in time. Anyone can change the tempo, the others will follow. Anyone can join or leave without disrupting the session.

%prep
%setup
%patch0 -p1

%build
%cmake -DLINK_PLATFORM_LINUX=ON \
        -DLINK_BUILD_JACK=ON \
        -DLINK_BUILD_QT_EXAMPLES=OFF \
        -DCMAKE_EXE_LINKER_FLAGS="-L/usr/lib64/pipewire-0.3/jack" \
        -DCMAKE_INSTALL_PREFIX=%buildroot/usr \
        -Wno-dev

%cmake_build

%install
find include -type f \( -iname "*.ipp" -o -iname "*.hpp" \) -exec install -vDm 644 {} "%buildroot/usr/"{} \;
install -vDm 644 {{README,CONTRIBUTING}.md,*.pdf} -t "%buildroot%_docdir/%name/"
install -vDm 644 cmake_include/AsioStandaloneConfig.cmake -t "%buildroot%_libexecdir/cmake/%name/cmake_include"

rm -rv %buildroot/usr/include/ableton/platforms/{windows,darwin,esp32}/

%files
%_includedir/ableton/*
%_libexecdir/cmake/ableton-link/cmake_include/AsioStandaloneConfig.cmake
%_docdir/ableton-link/*

%changelog
* Thu Jan 25 2024 Ivan Mazhukin <vanomj@altlinux.org> 3.1.0-alt1
- Initial build for Alt Sisyphus

