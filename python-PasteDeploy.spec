Summary:	Load, configure, and compose WSGI applications and servers
Name:		python-PasteDeploy
Version:	0.4
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/PasteDeploy/PasteDeploy-%{version}.tar.gz
# Source0-md5:	8b44cb47f87ebebffe4afd2e1a8bf258
URL:		http://pythonpaste.org/deploy/
BuildRequires:	python-devel
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool provides code to load WSGI applications and servers from URIs; these
URIs can refer to Python Eggs for INI-style configuration files. Paste Script
provides commands to serve applications based on this configuration file.

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
