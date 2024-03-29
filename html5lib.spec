#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : html5lib
Version  : 1.1
Release  : 55
URL      : https://files.pythonhosted.org/packages/ac/b6/b55c3f49042f1df3dcd422b7f224f939892ee94f22abcf503a9b7339eaf2/html5lib-1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/b6/b55c3f49042f1df3dcd422b7f224f939892ee94f22abcf503a9b7339eaf2/html5lib-1.1.tar.gz
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
BuildRequires : buildreq-distutils3
BuildRequires : chardet
BuildRequires : lxml
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : webencodings

%description
========

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
Provides: pypi(html5lib)
Requires: pypi(six)
Requires: pypi(webencodings)

%description python3
python3 components for the html5lib package.


%prep
%setup -q -n html5lib-1.1
cd %{_builddir}/html5lib-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635740073
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/html5lib
cp %{_builddir}/html5lib-1.1/LICENSE %{buildroot}/usr/share/package-licenses/html5lib/5bd527c7e2297d365b33ea67a400b6ba995e3705
cp %{_builddir}/html5lib-1.1/html5lib/tests/testdata/LICENSE %{buildroot}/usr/share/package-licenses/html5lib/2260a4b28dc3f43e07fa45e20334b7cdcab77588
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/html5lib/2260a4b28dc3f43e07fa45e20334b7cdcab77588
/usr/share/package-licenses/html5lib/5bd527c7e2297d365b33ea67a400b6ba995e3705

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
