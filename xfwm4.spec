# TODO
# - shouldn't own /usr/share/themes/Default?
%bcond_without	compositor		# without compositor extensions
Summary:	Next generation window manager for Xfce
Summary(pl):	Zarz±dca okien nowej generacji dla Xfce
Name:		xfwm4
Version:	4.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:        http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	a45792df95944d6bd15ff5c23ec26e1b
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3
and Xfce.

%description -l pl
xfwm4 to zarz±dca okien kompatybilny z GNOME, GNOME2, KDE2, KDE3 oraz
Xfce.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po
mv -f po/{nb_NO,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure %{?with_compositor:--enable-compositor}

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
%doc AUTHORS ChangeLog README TODO example.gtkrc-2.0
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so

%{_desktopdir}/*.desktop

%dir %{_datadir}/xfwm4
%{_datadir}/xfwm4/defaults
%{_datadir}/themes/*
%{_iconsdir}/hicolor/*/*/*

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
