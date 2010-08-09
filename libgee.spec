Summary:	libgee - GObject collection library
Summary(pl.UTF-8):	libgee - GObject collection library
Name:		libgee
Version:	0.5.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgee/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	fc5a36eb5f61154a1456cbb8b1798e41
URL:		http://live.gnome.org/Libgee
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	vala
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%description -l pl.UTF-8
libgee jest zbiorem bibliotek dostarczających interfejs GObject i
klasy powszechnie używanych struktur danych.

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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgee.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgee.so.2
%{_libdir}/girepository-1.0/Gee-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgee.so
%{_libdir}/libgee.la
%{_pkgconfigdir}/gee-1.0.pc
%{_includedir}/gee-1.0
%{_datadir}/vala/vapi/gee-1.0.vapi
%{_datadir}/gir-1.0/Gee-1.0.gir
