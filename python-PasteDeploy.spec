%define 	module	PasteDeploy
Summary:	Load, configure, and compose WSGI applications and servers
Summary(pl.UTF-8):	Wczytywanie, konfiguracja i łączenie aplikacji i serwerów WSGI
Name:		python-%{module}
Version:	1.5.0
Release:	3
License:	X11/MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/P/PasteDeploy/%{module}-%{version}.tar.gz
# Source0-md5:	f1a068a0b680493b6eaff3dd7690690f
URL:		http://pythonpaste.org/deploy/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools >= 0.6-0.a9.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
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

%prep
%setup -q -n PasteDeploy-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--single-version-externally-managed \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%dir %{py_sitescriptdir}/paste/deploy
%{py_sitescriptdir}/paste/deploy/*.py[co]
%{py_sitescriptdir}/paste/deploy/paster_templates
%{py_sitescriptdir}/PasteDeploy-%{version}-py*.egg-info
%{py_sitescriptdir}/PasteDeploy-%{version}-py*-nspkg.pth
