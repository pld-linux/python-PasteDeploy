Summary:	Load, configure, and compose WSGI applications and servers
Summary(pl.UTF-8):	Wczytywanie, konfiguracja i łączenie aplikacji i serwerów WSGI
Name:		python-PasteDeploy
Version:	1.3.3
Release:	3
Group:		Libraries/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/PasteDeploy/PasteDeploy-%{version}.tar.gz
# Source0-md5:	0598aa8ab4184ea8087839b811f92284
URL:		http://pythonpaste.org/deploy/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools >= 0.6-0.a9.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{py_sitescriptdir}/paste/deploy
%{py_sitescriptdir}/Paste*
