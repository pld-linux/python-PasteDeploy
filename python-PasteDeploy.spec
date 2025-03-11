#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define 	module	PasteDeploy
Summary:	Load, configure, and compose WSGI applications and servers
Summary(pl.UTF-8):	Wczytywanie, konfiguracja i łączenie aplikacji i serwerów WSGI
Name:		python-%{module}
# keep 2.x here for python2 support
Version:	2.1.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pastedeploy/
Source0:	https://files.pythonhosted.org/packages/source/P/PasteDeploy/%{module}-%{version}.tar.gz
# Source0-md5:	bc13219866a524626aee97127afa0348
URL:		https://pypi.org/project/PasteDeploy/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools >= 0.6-0.a9.1
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-Paste
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files. Paste Script provides commands to serve applications based on
this configuration file.

%description -l pl.UTF-8
To narzędzie zawiera kod do wczytywania aplikacji i serwerów WSGI z
URI; URI te mogą odnosić się do pakietów Python Egg dla plików
konfiguracyjnych w stylu INI. Paste Script udostępnia polecenia do
obsługi aplikacji w oparciu o ten plik konfiguracyjny.

%package -n python3-%{module}
Summary:	Load, configure, and compose WSGI applications and servers
Summary(pl.UTF-8):	Wczytywanie, konfiguracja i łączenie aplikacji i serwerów WSGI
Group:		Libraries/Python
Requires:	python3-Paste
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files. Paste Script provides commands to serve applications based on
this configuration file.

%description -n python3-%{module} -l pl.UTF-8
To narzędzie zawiera kod do wczytywania aplikacji i serwerów WSGI z
URI; URI te mogą odnosić się do pakietów Python Egg dla plików
konfiguracyjnych w stylu INI. Paste Script udostępnia polecenia do
obsługi aplikacji w oparciu o ten plik konfiguracyjny.

%prep
%setup -q -n PasteDeploy-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst license.txt
%{py_sitescriptdir}/paste/deploy
%{py_sitescriptdir}/PasteDeploy-%{version}-py*.egg-info
%{py_sitescriptdir}/PasteDeploy-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst license.txt
%{py3_sitescriptdir}/paste/deploy
%{py3_sitescriptdir}/PasteDeploy-%{version}-py*.egg-info
%{py3_sitescriptdir}/PasteDeploy-%{version}-py*-nspkg.pth
%endif
