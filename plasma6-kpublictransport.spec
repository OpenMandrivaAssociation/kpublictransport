#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname KPublicTransport
%define devname %mklibname -d KPublicTransport

%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for reading public transport information
Name:		plasma6-kpublictransport
Version:	24.05.1
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kpublictransport/-/archive/%{gitbranch}/kpublictransport-%{gitbranchd}.tar.bz2#/kpublictransport-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kpublictransport-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6NetworkManagerQt)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	osmctools
Requires:	osmctools
# For QCH format docs
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)

%description
Public transport application for Plasma.

%package -n %{libname}
Summary:	Library for reading public transport information
Group:		System/Libraries
%rename %mklibname KPublicTransport 20
%rename %mklibname KPublicTransport 21

%description -n %{libname}
Library for reading public transport information.

%files -n %{libname}
%{_libdir}/libKPublicTransport.so.*
%{_libdir}/libKPublicTransportOnboard.so.*
%{_libdir}/qt6/qml/org/kde/kpublictransport
%{_datadir}/qlogging-categories6/org_kde_kpublictransport.categories
%{_datadir}/qlogging-categories6/org_kde_kpublictransport_onboard.categories

%package -n %{devname}
Summary:	Development files for %{libname}
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(zlib)

%description -n %{devname}
Development files for %{libname}.

%files -n %{devname}
%{_includedir}/KPublicTransport
%{_libdir}/cmake/KPublicTransport
%{_libdir}/libKPublicTransport.so
%{_libdir}/libKPublicTransportOnboard.so

%prep
%autosetup -p1 -n kpublictransport-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
