#
%define		snap 20040616
#
Summary:	Next generation window manager for XFce
Summary(pl):	Zarz±dca okien nowej generacji dla XFce
Name:		xfwm4
Version:	4.1.0
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	a5d7d4e9bae2337531f081042d7e3e33
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	startup-notification >= 0.4
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3
and XFce.

%description -l pl
xfwm4 to zarz±dca okien kompatybilny z GNOME, GNOME2, KDE2, KDE3 oraz
XFce.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

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

%{_desktopdir}/*.desktop

%dir %{_datadir}/xfwm4
%{_datadir}/xfwm4/defaults
%{_datadir}/themes/*

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C
%lang(fr) %{_datadir}/xfce4/doc/fr
