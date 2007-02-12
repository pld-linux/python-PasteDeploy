Summary:	Load, configure, and compose WSGI applications and servers
Summary(pl.UTF-8):   Wczytywanie, konfiguracja i łączenie aplikacji i serwerów WSGI
Name:		python-PasteDeploy
Version:	1.1
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/PasteDeploy/PasteDeploy-%{version}.tar.gz
# Source0-md5:	e4f16fe735db735c3fc0c6e168e72455
URL:		http://pythonpaste.org/deploy/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%{py_sitescriptdir}/paste/deploy
%{py_sitescriptdir}/Paste*
