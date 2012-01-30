Summary:	Next generation window manager for Xfce
Summary(pl.UTF-8):	Zarządca okien nowej generacji dla Xfce
Name:		xfwm4
Version:	4.8.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfwm4/4.8/%{name}-%{version}.tar.bz2
# Source0-md5:	66cb65797cea8a62563f69b833c7888b
URL:		http://www.xfce.org/projects/xfwm4
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.22.0
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfconf-devel >= 4.8.0
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.2
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfwm4 is a EWMH standard compliant window manager.

%description -l pl.UTF-8
xfwm4 to zarządca okien zgodny ze standardem EWMH.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO example.gtkrc-2.0
%attr(755,root,root) %{_bindir}/xfwm4
%attr(755,root,root) %{_bindir}/xfwm4-settings
%attr(755,root,root) %{_bindir}/xfwm4-tweaks-settings
%attr(755,root,root) %{_bindir}/xfwm4-workspace-settings
%dir %{_libdir}/xfce4/xfwm4
%attr(755,root,root) %{_libdir}/xfce4/xfwm4/helper-dialog

%{_desktopdir}/*.desktop

%dir %{_datadir}/xfwm4
%{_datadir}/xfwm4/defaults
%{_datadir}/themes/*
%{_iconsdir}/hicolor/*/*/*

%dir %{_docdir}/xfwm4
%dir %{_docdir}/xfwm4/html
%{_docdir}/xfwm4/html/C
%{_docdir}/xfwm4/html/*.css
%lang(da) %{_docdir}/xfwm4/html/da
%lang(el) %{_docdir}/xfwm4/html/el
%lang(fr) %{_docdir}/xfwm4/html/fr
%lang(gl) %{_docdir}/xfwm4/html/gl
%lang(it) %{_docdir}/xfwm4/html/it
%lang(sv) %{_docdir}/xfwm4/html/sv
%lang(ug) %{_docdir}/xfwm4/html/ug
