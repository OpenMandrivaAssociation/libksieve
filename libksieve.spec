%define major 5
%define libname %mklibname KF5KSieve %{major}
%define devname %mklibname KF5KSieve -d

Name: libksieve
Version:	21.07.80
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
URL: http://kde.org/
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
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5AkonadiSearch)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5PimCommon)
BuildRequires: cmake(KF5MailTransport)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Libkdepim)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5PimTextEdit)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5AkonadiContact)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KF5IMAP)


Conflicts: kio-sieve < 3:16.04.3-2
Obsoletes: kio-sieve < %{EVRD}
Provides: kio-sieve = %{EVRD}

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
Requires: %{mklibname KF5KManageSieve %{major}} = %{EVRD}
Requires: %{mklibname KF5KSieveUi %{major}} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%libpackage KF5KManageSieve %{major}
%libpackage KF5KSieveUi %{major}

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
%{_libdir}/qt5/plugins/kf5/kio/sieve.so

%files -n %{libname}
%{_libdir}/libKF5KSieve.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
