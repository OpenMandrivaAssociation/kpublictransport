%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname KPublicTransport
%define devname %mklibname -d KPublicTransport

%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for reading public transport information
Name:		kpublictransport
Version:	23.08.5
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Help)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	osmctools
Requires:	osmctools
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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
%{_libdir}/qt5/qml/org/kde/kpublictransport
%{_datadir}/qlogging-categories5/org_kde_kpublictransport.categories
%{_datadir}/qlogging-categories5/org_kde_kpublictransport_onboard.categories

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
%doc %{_docdir}/qt5/*.{qch,tags}

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
