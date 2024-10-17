%define major 5
%define oldlibname %mklibname KF5KSieve 5
%define olddevname %mklibname KF5KSieve -d
%define libname %mklibname KPim5KSieve %{major}
%define devname %mklibname KPim5KSieve -d

Name: libksieve
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
# Used to be in kdepim, got to match
Epoch:		3
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for Sieve mail filtering
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: boost-devel
BuildRequires: sasl-devel
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5AkonadiSearch)
BuildRequires: cmake(KPim5Mime)
BuildRequires: cmake(KPim5PimCommon)
BuildRequires: cmake(KPim5MailTransport)
BuildRequires: cmake(KPim5Libkdepim)
BuildRequires: cmake(KPim5IdentityManagement)
BuildRequires: cmake(KF5PimTextEdit)
BuildRequires: cmake(KPim5AkonadiContact)
BuildRequires: cmake(KPim5IMAP)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

Conflicts: kio-sieve < 3:16.04.3-2
Obsoletes: kio-sieve < %{EVRD}
Provides: kio-sieve = %{EVRD}

%description
KDE library for Sieve mail filtering.

%package -n %{libname}
Summary: KDE library for Sieve mail filtering
Group: System/Libraries
Requires: %{name} >= %{EVRD}
%rename %{oldlibname}
Obsoletes: %{mklibname KF5KManageSieve} < %{EVRD}
Obsoletes: %{mklibname KF5KSieveUi} < %{EVRD}

%description -n %{libname}
KDE library for Sieve mail filtering.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{mklibname KPim5KManageSieve} = %{EVRD}
Requires: %{mklibname KPim5KSieveUi} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%libpackage KPim5KManageSieve %{major}
%libpackage KPim5KSieveUi %{major}

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/libksieve.categories
%{_datadir}/qlogging-categories5/libksieve.renamecategories
%{_datadir}/knsrcfiles/ksieve_script.knsrc
%{_datadir}/sieve

%files -n %{libname}
%{_libdir}/libKPim5KSieve.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}
