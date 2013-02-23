#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	libgee - GObject collection library
Summary(pl.UTF-8):	libgee - biblioteka kolekcji oparta na GObject
Name:		libgee
Version:	0.8.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgee/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	922ff20952cdef429d3dab0810761342
URL:		http://live.gnome.org/Libgee
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# not required for stable releases (all generated files are included)
#BuildRequires:	vala >= 2:0.17.5
Requires:	glib2 >= 1:2.12.0
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
Requires:	glib2-devel >= 1:2.12.0

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
Requires:	vala >= 2:0.17.5

%description -n vala-libgee
libgee API for Vala language.

%description -n vala-libgee -l pl.UTF-8
API libgee dla języka Vala.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
