#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : systemd-netlogd
Version  : 1.1
Release  : 1
URL      : https://github.com/systemd/systemd-netlogd/archive/v1.1.tar.gz
Source0  : https://github.com/systemd/systemd-netlogd/archive/v1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: systemd-netlogd-config
Requires: systemd-netlogd-license
Requires: systemd-netlogd-man
BuildRequires : Sphinx
BuildRequires : gperf
BuildRequires : libcap-dev
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(libsystemd)
BuildRequires : python3

%description
systemd-netlogd
===================
Forwards messages from the journal to other hosts over the network using
the Syslog Protocol (RFC 5424). It can be configured to send messages to
both unicast and multicast addresses. systemd-netlogd runs with own user
systemd-journal-netlog.  Starts sending logs when network is up and stops
sending as soon as network is down (uses sd-network).

%package config
Summary: config components for the systemd-netlogd package.
Group: Default

%description config
config components for the systemd-netlogd package.


%package license
Summary: license components for the systemd-netlogd package.
Group: Default

%description license
license components for the systemd-netlogd package.


%package man
Summary: man components for the systemd-netlogd package.
Group: Default

%description man
man components for the systemd-netlogd package.


%prep
%setup -q -n systemd-netlogd-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531421396
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/systemd-netlogd
cp LICENSE.LGPL2.1 %{buildroot}/usr/share/doc/systemd-netlogd/LICENSE.LGPL2.1
cp LICENSE.GPL2 %{buildroot}/usr/share/doc/systemd-netlogd/LICENSE.GPL2
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/lib/systemd/systemd-netlogd

%files license
%defattr(-,root,root,-)
/usr/share/doc/systemd-netlogd/LICENSE.GPL2
/usr/share/doc/systemd-netlogd/LICENSE.LGPL2.1

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/systemd-netlogd.1
