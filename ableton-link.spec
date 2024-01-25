%define short_name Link
%define asio_ver 1-28-0

Name: ableton-link
Version: 3.1.0
Release: 1

Summary: This is the codebase for Ableton Link
License: GPL-2.0-or-later
Group: Sound
Url: https://github.com/Ableton/link

# Source-url: https://github.com/Ableton/link/archive/refs/tags/%short_name-%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/chriskohlhoff/asio/archive/refs/tags/asio-%asio_ver.tar.gz
Source1: asio-%asio_ver.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake make clang gcc-c++
BuildRequires: libportaudio2-devel asio-devel

%description
This is the codebase for Ableton Link, a technology that synchronizes musical beat, tempo, and phase across multiple applications running on one or more devices. Applications on devices connected to a local network discover each other automatically and form a musical session in which each participant can perform independently: anyone can start or stop while still staying in time. Anyone can change the tempo, the others will follow. Anyone can join or leave without disrupting the session.

%prep
%setup -a1

%build
%cmake -DLINK_PLATFORM_LINUX=ON -DLINK_BUILD_JACK=ON
%cmake_build
# -DINTERFACE_INCLUDE_DIRECTORIES=%buildroot%_includedir
%install
%cmake_install

%files




%changelog
* Thu Jan 25 2024 Ivan Mazhukin <vanomj@altlinux.org> 3.1.0-1
- new version

* Thu Jan 25 2024 Ivan Mazhukin <vanomj@altlinux.org> 3.1.0-alt1
- Initial build for Alt Sisyphus

