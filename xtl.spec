#
# Conditional build:
%bcond_without	apidocs		# API documentation
#
Summary:	Basic tools (containers, algorithms) used by other quantstack packages
Summary(pl.UTF-8):	Podstawowe narzędzia (kontenery, algorytmy) używane przez inne pakiety quantstack
Name:		xtl
Version:	0.7.7
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/xtensor-stack/xtl/tags
Source0:	https://github.com/xtensor-stack/xtl/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6df56ae8bc30471f6773b3f18642c8ab
URL:		https://xtl.readthedocs.io/
BuildRequires:	cmake >= 3.1
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	nlohmann-json-devel
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtl gathers generic purpose algorithms and containers that are used by
the xtensor stack and the xeus stack.

Some of the features are C++14 backport of C++17 classes and
algorithms, such as "variant" or "any".

%description -l pl.UTF-8
xtl gromadzi algorytmy i kontenery ogólnego zastosowania, używane
przez stosy xtensor oraz xeus.

Niektóre z niech to backport do C++14 klas i algorytmów z C++17,
takich jak "variant" czy "any".

%package devel
Summary:	Basic tools (containers, algorithms) used by other quantstack packages
Summary(pl.UTF-8):	Podstawowe narzędzia (kontenery, algorytmy) używane przez inne pakiety quantstack
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:5

%description devel
xtl gathers generic purpose algorithms and containers that are used by
the xtensor stack and the xeus stack.

Some of the features are C++14 backport of C++17 classes and
algorithms, such as "variant" or "any".

%description devel -l pl.UTF-8
xtl gromadzi algorytmy i kontenery ogólnego zastosowania, używane
przez stosy xtensor oraz xeus.

Niektóre z niech to backport do C++14 klas i algorytmów z C++17,
takich jak "variant" czy "any".

%package apidocs
Summary:	API documentation for xtl library
Summary(pl.UTF-8):	Dokumentacja API biblioteki xtl
Group:		Documentation

%description apidocs
API documentation for xtl library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki xtl.

%prep
%setup -q

%build
install -d build
cd build
# fake LIBDIR so we can create noarch package
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR=%{_datadir}

%{__make}
cd ..

%if %{with apidocs}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/xtl
%{_npkgconfigdir}/xtl.pc
%{_datadir}/cmake/xtl

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_images,_static,*.html,*.js}
%endif
