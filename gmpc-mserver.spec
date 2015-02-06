Summary:	A microhttpd server plugin for gmpc
Name:		gmpc-mserver
Version:	0.20.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.4
BuildRequires:	libmicrohttpd-devel
BuildRequires:	intltool
Requires:	gmpc

%description
A microhttpd server plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%files
%{_libdir}/gmpc/plugins/gmpcmserverplugin.so
%{_datadir}/gmpc/plugins/gmpc-mserver/gmpc-mserver.png
