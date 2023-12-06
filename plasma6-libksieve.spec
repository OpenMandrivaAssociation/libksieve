%define major 6
%define libname %mklibname KPim6KSieve
%define devname %mklibname KPim6KSieve -d

Name: plasma6-libksieve
Version:	24.01.80
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/libksieve-%{version}.tar.xz
Summary: KDE library for Sieve mail filtering
URL: http://kde.org/
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
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6AkonadiContactCore)
BuildRequires: cmake(KPim6IMAP)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

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
%{_libdir}/libKPim6KManageSieve.so.5*

%libpackage KPim6KSieveUi %{major}
%{_libdir}/libKPim6KSieveUi.so.5*

%prep
%autosetup -p1 -n libksieve-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libksieve.categories
%{_datadir}/qlogging-categories6/libksieve.renamecategories
%{_datadir}/knsrcfiles/ksieve_script.knsrc
%{_datadir}/sieve

%files -n %{libname}
%{_libdir}/libKPim6KSieveCore.so.%{major}*
%{_libdir}/libKPim6KSieveCore.so.5*
%{_libdir}/libKPim6KSieve.so.%{major}*
%{_libdir}/libKPim6KSieve.so.5*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
