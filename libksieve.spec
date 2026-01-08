#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6KSieve
%define devname %mklibname KPim6KSieve -d

Name: libksieve
Version:	25.12.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/libksieve/-/archive/%{gitbranch}/libksieve-%{gitbranchd}.tar.bz2#/libksieve-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/libksieve-%{version}.tar.xz
%endif
Summary: KDE library for Sieve mail filtering
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: boost-devel
BuildRequires: sasl-devel
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6TextAddonsWidgets)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6AkonadiContactCore)
BuildRequires: cmake(KPim6IMAP)
BuildRequires: cmake(KF6TextUtils)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%rename plasma6-libksieve

%description
KDE library for Sieve mail filtering.

%package -n %{libname}
Summary: KDE library for Sieve mail filtering
Group: System/Libraries
Requires: %{name} >= %{EVRD}

%description -n %{libname}
KDE library for Sieve mail filtering.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{mklibname KPim6KManageSieve} = %{EVRD}
Requires: %{mklibname KPim6KSieveUi} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%libpackage KPim6KManageSieve %{major}

%libpackage KPim6KSieveUi %{major}

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libksieve.categories
%{_datadir}/qlogging-categories6/libksieve.renamecategories
%{_datadir}/knsrcfiles/ksieve_script.knsrc
%{_datadir}/sieve

%files -n %{libname}
%{_libdir}/libKPim6KSieveCore.so.%{major}*
%{_libdir}/libKPim6KSieve.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
