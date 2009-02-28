Summary:	Next generation window manager for Xfce
Summary(pl.UTF-8):	Zarządca okien nowej generacji dla Xfce
Name:		xfwm4
Version:	4.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	83cd2f82f2fabfe4ab28a9780fbf309e
URL:		http://www.xfce.org/projects/xfwm4/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfconf-devel >= 4.6.0
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}

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

%docdir %{_datadir}/xfce4/doc
# undermentioned dirs belong to libxfce4util
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(it) %{_datadir}/xfce4/doc/it/*
