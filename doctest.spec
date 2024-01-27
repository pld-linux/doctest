#
# Conditional build:
%bcond_with	tests	# building tests/examples

Summary:	Fast, feature-rich C++11/14/17/20/23 single-header testing framework
Summary(pl.UTF-8):	Szybki, bogaty w możliwości szkielet testów C++11/14/17/20/23 w pojedynczym nagłówku
Name:		doctest
Version:	2.4.11
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/doctest/doctest/releases
Source0:	https://github.com/doctest/doctest/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a457ba0e8c8f670bfd4aafaa3d9f5e4d
URL:		https://github.com/doctest/doctest
BuildRequires:	cmake >= 3.0
BuildRequires:	libstdc++-devel >= 6:4.7
Requires:	libstdc++-devel >= 6:4.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
doctest is a new C++ testing framework but is by far the fastest both
in compile times and runtime compared to other feature-rich
alternatives. It brings the ability of compiled languages such as D,
Rust, Nim to have tests written directly in the production code thanks
to a fast, transparent and flexible test runner with a clean
interface.

%description -l pl.UTF-8
doctest to nowy szkielet testów dla C++, obecnie dużo szybszy zarówno
pod względem czasu kompilacji, jak i działania, w porównaniu do
alternatyw o podobnych możliwościach. Pozwala na znaną z języków
kompilowanych, takich jak D, Rust czy Nim możliwość umieszczania
testów bezpośrednio w kodzie produkcyjnym - dzięki szybkiemu,
przezroczystemu i elastycznemu, mającemu czysty interfejs systemowi
uruchamiania testów.

%prep
%setup -q

%build
install -d build
cd build
# use arch-independent LIBDIR for cmake files, so that package can be noarch
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR=%{_datadir} \
	%{!?with_tests:-DDOCTEST_WITH_TESTS=OFF}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.md doc/markdown/*.md
%{_includedir}/doctest
%{_datadir}/cmake/doctest
