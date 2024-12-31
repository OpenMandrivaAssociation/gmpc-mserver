Summary:	A microhttpd server plugin for gmpc
Name:		gmpc-mserver
Version:	0.20.0
Release:	3
License:	GPLv2+
Group:		Sound
# https://repo.or.cz/w/gmpc-mserver.git
Url:		https://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.4
BuildRequires:	libmicrohttpd-devel
BuildRequires:	intltool
BuildSystem:	autotools
Requires:	gmpc

%patchlist
gmpc-mserver-0.20.0-microhttpd-fixes.patch

%description
A microhttpd server plugin for gmpc.

%files
%{_libdir}/gmpc/plugins/gmpcmserverplugin.so
%{_datadir}/gmpc/plugins/gmpc-mserver/gmpc-mserver.png
