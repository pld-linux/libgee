#
# Conditional build:
%bcond_without	apidocs		# API documentation (valadoc)
%bcond_without	static_libs	# static library
%bcond_with	bootstrap	# bootstrap without apidocs subpackage (alias for without_apidocs)

%if %{with bootstrap}
%undefine	with_apidocs
%endif
Summary:	libgee - GObject collection library
Summary(pl.UTF-8):	libgee - biblioteka kolekcji oparta na GObject
Name:		libgee
Version:	0.20.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libgee/0.20/%{name}-%{version}.tar.xz
# Source0-md5:	8b9001f47e15ef7a1776ac1f5bb015a0
Patch0:		%{name}-doc.patch
URL:		https://wiki.gnome.org/Projects/Libgee
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
%{?with_apidocs:BuildRequires:	valadoc}
BuildRequires:	xz
# not required for stable releases (all generated files are included)
#BuildRequires:	vala >= 2:0.25.1
Requires:	glib2 >= 1:2.36.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%description -l pl.UTF-8
libgee jest biblioteką udostępniajacą oparte na bibliotece GObject
interfejsy oraz klasy powszechnie używanych struktur danych.

%package devel
Summary:	Header files for libgee library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgee
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36.0

%description devel
Header files for libgee library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgee.

%package static
Summary:	Static libgee library
Summary(pl.UTF-8):	Statyczna biblioteka libgee
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgee library.

%description static -l pl.UTF-8
Statyczna biblioteka libgee.

%package -n vala-libgee
Summary:	libgee API for Vala language
Summary(pl.UTF-8):	API libgee dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.25.1
BuildArch:	noarch

%description -n vala-libgee
libgee API for Vala language.

%description -n vala-libgee -l pl.UTF-8
API libgee dla języka Vala.

%package apidocs
Summary:	API documentation for libgee library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgee
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libgee library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgee.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-doc} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgee-0.8.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgee-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgee-0.8.so.2
%{_libdir}/girepository-1.0/Gee-0.8.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgee-0.8.so
%{_pkgconfigdir}/gee-0.8.pc
%{_includedir}/gee-0.8
%{_datadir}/gir-1.0/Gee-0.8.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgee-0.8.a
%endif

%files -n vala-libgee
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gee-0.8.vapi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/references/gee-0.8
%endif
