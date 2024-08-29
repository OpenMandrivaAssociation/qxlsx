%define oname QXlsx
%define major		0
%define libname		%mklibname qxlsx 
%define devname	%mklibname qxlsx -d

Name:		qxlsx
Version:	1.4.9
Release:	1
Summary:	Excel/XLSX file reader/writer library for Qt
Group:		Office
License:	MIT
URL:		https://github.com/QtExcel/%{oname}
Source0:	https://github.com/QtExcel/QXlsx/archive/v%{version}/%{oname}-%{version}.tar.gz
Patch0:		qlatin1string.patch

BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(xkbcommon)

%description
QXlsx is a reader/writer library for Excel files (*.xlsx).

%package -n %{libname}
Summary:	Library for QXlsx (Qt6)
Group:		System/Libraries

%description -n %{libname}
QXlsx is a reader/writer library for Excel files (*.xlsx).

%package -n %{devname}
Summary:	Development files for QXlsx
Group:		Development/KDE and Qt

Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
QXlsx is a reader/writer library for Excel files (*.xlsx).
This package contains the development files of QXlsx.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
cd %{oname}
%cmake \
	-DQT_VERSION_MAJOR:STRING=6
%make_build

%install
cd %{oname}
%make_install -C build

%files -n %{libname}
%{_libdir}/libQXlsxQt6.so.%{major}*
%{_libdir}/libQXlsxQt6.so.1.4.4

%files -n %{devname}
%license LICENSE
%doc README*
%{_includedir}/QXlsxQt6/
%{_libdir}/cmake/QXlsxQt6
%{_libdir}/libQXlsxQt6.so
