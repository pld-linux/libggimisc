#
# Conditional build:
%bcond_with	svga		# svgalib plugin
%bcond_with	static_modules	# build static library AND make all modules builtin (also in shared lib)
#
Summary:	LibGGIMisc - extension for misc graphics target features
Summary(pl.UTF-8):	LibGGIMisc - rozszerzenie do różnych cech modułów wyświetlających
Name:		libggimisc
Version:	2.2.2
Release:	1
License:	BSD-like
Group:		Libraries
# HTTP 403
#Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
Source0:	http://downloads.sourceforge.net/ggi/%{name}-%{version}.src.tar.bz2
# Source0-md5:	8e525280ccee2eaab07946ca7aee159f
URL:		http://www.ggi-project.org/packages/libggimisc.html
BuildRequires:	libggi-devel >= 2.2.2
%{?with_svga:BuildRequires:	svgalib-devel}
Requires:	libggi >= 2.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGIMisc is a place to put support for graphics target features
which are not deserving their own special extensions. Right now this
means basically some VGA adaptor features - getting and waiting for
the raster position, using a hardware horizontal splitline feature,
and loading/unloading font data from hardware text modes.

%description -l pl.UTF-8
LibGGIMisc to miejsce do umieszczania obsługi różnych cech modułów
wyświetlających nie zasługujących na własne specjalne rozszerzenia.
Aktualnie oznacza to głównie niektóre możliwości kart graficznych VGA,
takie jak odczyt i oczekiwanie na położenie rastra, używanie
sprzętowej linii dzielącej oraz wczytywanie/usuwanie danych fontów ze
sprzętowych trybów tekstowych.

%package devel
Summary:	Header files for libggimisc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libggimisc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libggi-devel >= 2.2.2
%if %{with static_modules}
%{?with_svga:Requires:	svgalib-devel}
%endif

%description devel
Header files for libggimisc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libggimisc.

%package static
Summary:	Static libggimisc library
Summary(pl.UTF-8):	Statyczna biblioteka libggimisc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libggimisc library.

%description static -l pl.UTF-8
Statyczna biblioteka libggimisc.

%package svgalib
Summary:	svgalib target for libggimisc library
Summary(pl.UTF-8):	Wtyczka svgalib dla biblioteki libggimisc
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description svgalib
svgalib target for libggimisc library.

%description svgalib -l pl.UTF-8
Wtyczka svgalib dla biblioteki libggimisc.

%prep
%setup -q

%build
%configure \
	%{!?with_dynamic_modules:--disable-static} \
	%{!?with_svga:--disable-svgalib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ggi/ggimisc/display/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libggimisc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggimisc.so.2
%dir %{_libdir}/ggi/ggimisc
%dir %{_libdir}/ggi/ggimisc/display
%attr(755,root,root) %{_libdir}/ggi/ggimisc/display/fbdev_ggimisc.so
%attr(755,root,root) %{_libdir}/ggi/ggimisc/display/pseudo_stubs_ggimisc.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/libggimisc.conf
%{_mandir}/man7/libggimisc.7*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libggimisc.so
%{_libdir}/libggimisc.la
%{_includedir}/ggi/misc*.h
%{_includedir}/ggi/internal/misc.h
%{_mandir}/man3/ggi*.3*

%if %{with static_modules}
%files static
%defattr(644,root,root,755)
%{_libdir}/libggimisc.a
%endif

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/ggimisc/display/svgalib_ggimisc.so
%endif
