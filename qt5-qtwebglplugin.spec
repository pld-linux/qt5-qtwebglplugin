%define		orgname		qtwebglplugin
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qtwebsockets_ver	%{version}
Summary:	The Qt5 WebGL platform plugin
Summary(pl.UTF-8):	Wtyczka platformy Qt5 WebGL
Name:		qt5-%{orgname}
Version:	5.15.9
Release:	1
License:	GPL v3+ or commercial
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	2c10c379f63070d479b94ed905885085
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5DBus-devel >= %{qtbase_ver}
BuildRequires:	Qt5EventDispatcherSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5FontDatabaseSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5ThemeSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5WebSockets-devel >= %{qtwebsockets_ver}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 WebGL platform plugin.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera wtyczkę platformy Qt5 WebGL.

%package -n Qt5Gui-platform-webgl
Summary:	Qt5 Gui WebGL platform plugin
Summary(pl.UTF-8):	Wtyczka platformy WebGL do biblioteki Qt5 Gui
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Requires:	Qt5WebSockets >= %{qtwebsockets_ver}

%description -n Qt5Gui-platform-webgl
Qt5 Gui WebGL platform plugin.

%description -n Qt5Gui-platform-webgl -l pl.UTF-8
Wtyczka platformy WebGL do biblioteki Qt5 Gui.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
%{qmake_qt5}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n Qt5Gui-platform-webgl
%defattr(644,root,root,755)
%doc dist/changes-*
# R: Qt5Core Qt5DBus Qt5Gui Qt5Network Qt5Quick Qt5WebSockets fontconfig freetype glib2
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwebgl.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWebGLIntegrationPlugin.cmake
