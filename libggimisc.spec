Summary:	LibGGIMisc - extension for misc graphics target features
Summary(pl):	LibGGIMisc - rozszerzenie do ró¿nych cech modu³ów wy¶wietlaj±cych
Name:		libggimisc
Version:	2.1.0
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/current/%{name}-%{version}.src.tar.bz2
# Source0-md5:	44be7b5e01fd9701bd84de4f19be95f0
URL:		http://www.ggi-project.org/packages/libggimisc.html
BuildRequires:	libggi-devel >= 2.1.0
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGIMisc is a place to put support for graphics target features
which are not deserving their own special extensions. Right now this
means basically some VGA adaptor features - getting and waiting for
the raster position, using a hardware horizontal splitline feature,
and loading/unloading font data from hardware text modes.

%description -l pl
LibGGIMisc to miejsce do umieszczania obs³ugi ró¿nych cech modu³ów
wy¶wietlaj±cych nie zas³uguj±cych na w³asne specjalne rozszerzenia.
Aktualnei oznacza to g³ównie niektóre mo¿liwo¶ci kart graficznych VGA,
takie jak odczyt i oczekiwanie na po³o¿enie rastra, u¿ywanie
sprzêtowej linii dziel±cej oraz wczytywanie/usuwanie danych fontów ze
sprzêtowych trybów tekstowych.

%package devel
Summary:	Header files for libggimisc library
Summary(pl):	Pliki nag³ówkowe biblioteki libggimisc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libggi-devel >= 2.1.0

%description devel
Header files for libggimisc library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libggimisc.

%package svgalib
Summary:	svgalib target for libggimisc library
Summary(pl):	Wtyczka svgalib dla biblioteki libggimisc
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description svgalib
svgalib target for libggimisc library.

%description svgalib -l pl
Wtyczka svgalib dla biblioteki libggimisc.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ggi/ggimisc/display/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libggimisc.so.*.*.*
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

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/ggimisc/display/svgalib_ggimisc.so
