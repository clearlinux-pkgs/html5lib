#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : html5lib
Version  : 1.0.1
Release  : 30
URL      : https://files.pythonhosted.org/packages/85/3e/cf449cf1b5004e87510b9368e7a5f1acd8831c2d6691edd3c62a0823f98f/html5lib-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/3e/cf449cf1b5004e87510b9368e7a5f1acd8831c2d6691edd3c62a0823f98f/html5lib-1.0.1.tar.gz
Summary  : HTML parser based on the WHATWG HTML specification
Group    : Development/Tools
License  : MIT
Requires: html5lib-license = %{version}-%{release}
Requires: html5lib-python = %{version}-%{release}
Requires: html5lib-python3 = %{version}-%{release}
Requires: chardet
Requires: lxml
Requires: six
Requires: webencodings
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
========

%package legacypython
Summary: legacypython components for the html5lib package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the html5lib package.


%package license
Summary: license components for the html5lib package.
Group: Default

%description license
license components for the html5lib package.


%package python
Summary: python components for the html5lib package.
Group: Default
Requires: html5lib-python3 = %{version}-%{release}

%description python
python components for the html5lib package.


%package python3
Summary: python3 components for the html5lib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the html5lib package.


%prep
%setup -q -n html5lib-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540889049
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1540889049
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/html5lib
cp LICENSE %{buildroot}/usr/share/package-licenses/html5lib/LICENSE
cp html5lib/tests/testdata/LICENSE %{buildroot}/usr/share/package-licenses/html5lib/html5lib_tests_testdata_LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/html5lib/LICENSE
/usr/share/package-licenses/html5lib/html5lib_tests_testdata_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
