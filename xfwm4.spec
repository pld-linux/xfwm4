Summary:	Next generation window manager for xfce
Summary(pl):	Zarz±dca okien nowej generacji dla xfce
Name:		xfwm4
Version:	3.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://linux.imp.mx/xfce4/rc2/xfce4-rc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	322758598477192116a6dfa0f79abd38
URL:		http://www.xfce.org/
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 3.99.2
BuildRequires:	libxfcegui4-devel >= 3.99.2
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	xfce-mcs-manager-devel >= 3.99.2
Requires:	libxfce4mcs >= 3.99.2
Requires:	libxfcegui4 >= 3.99.2
Requires:	startup-notification >= 0.4
Requires:	xfce-mcs-manager >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3
and Xfce.

%description -l pl
xfwm4 to zarz±dca okien kompatybilny z GNOME, GNOME2, KDE2, KDE3 oraz
Xfce.

%prep
%setup -q

%build
glib-gettextize --copy --force
intltoolize --copy --force
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO example.xfwm4rc example.gtkrc-2.0
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%dir %{_datadir}/xfwm4
%{_datadir}/xfwm4/defaults
%{_datadir}/xfwm4/themes
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*
