Summary: 	Next generation window manager for xfce
Name: 		xfwm4
Version: 	3.90.0
Release: 	0.1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	bd853cd5b1e2bf79e4bd477ab207cf1c
Group: 		X11/Applications
Requires:	libxfce4mcs
Requires:	libxfcegui4
Requires:	xfce-mcs-manager
BuildRequires:	libxfce4mcs-devel
BuildRequires: 	libxfcegui4-devel
BuildRequires:	xfce-mcs-manager-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfwm4 is a window manager compatable with
GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%setup -q

%build
glib-gettextize --copy --force
intltoolize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc example.xfwm4rc example.gtkrc-2.0 README INSTALL TODO COPYING AUTHORS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_libdir}/xfce4/mcs-plugins/*.la
%{_libdir}/xfce4/mcs-plugins/*.a
%{_datadir}/xfwm4/defaults
%{_datadir}/xfwm4/themes
%{_datadir}/xfce4/doc
%{_datadir}/locale
