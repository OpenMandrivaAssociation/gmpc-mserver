Summary:	A microhttpd server plugin for gmpc
Name:		gmpc-mserver
Version:	0.18.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	libxml2-devel
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	taglib-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	libmicrohttpd-devel
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A microhttpd server plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/gmpcmserverplugin.la
%{_libdir}/gmpc/plugins/gmpcmserverplugin.so
