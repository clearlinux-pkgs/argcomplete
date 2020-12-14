#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8AFAFCD242818A52 (kislyuk@gmail.com)
#
Name     : argcomplete
Version  : 1.12.2
Release  : 66
URL      : https://files.pythonhosted.org/packages/cb/53/d2e3d11726367351b00c8f078a96dacb7f57aef2aca0d3b6c437afc56b55/argcomplete-1.12.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/53/d2e3d11726367351b00c8f078a96dacb7f57aef2aca0d3b6c437afc56b55/argcomplete-1.12.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/cb/53/d2e3d11726367351b00c8f078a96dacb7f57aef2aca0d3b6c437afc56b55/argcomplete-1.12.2.tar.gz.asc
Summary  : Bash tab completion for argparse
Group    : Development/Tools
License  : Apache-2.0
Requires: argcomplete-bin = %{version}-%{release}
Requires: argcomplete-license = %{version}-%{release}
Requires: argcomplete-python = %{version}-%{release}
Requires: argcomplete-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pexpect
BuildRequires : pytest

%description
==============================================
        *Tab complete all the things!*
        
        Argcomplete provides easy, extensible command line tab completion of arguments for your Python script.

%package bin
Summary: bin components for the argcomplete package.
Group: Binaries
Requires: argcomplete-license = %{version}-%{release}

%description bin
bin components for the argcomplete package.


%package license
Summary: license components for the argcomplete package.
Group: Default

%description license
license components for the argcomplete package.


%package python
Summary: python components for the argcomplete package.
Group: Default
Requires: argcomplete-python3 = %{version}-%{release}

%description python
python components for the argcomplete package.


%package python3
Summary: python3 components for the argcomplete package.
Group: Default
Requires: python3-core
Provides: pypi(argcomplete)

%description python3
python3 components for the argcomplete package.


%prep
%setup -q -n argcomplete-1.12.2
cd %{_builddir}/argcomplete-1.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606231728
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose test/test.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/argcomplete
cp %{_builddir}/argcomplete-1.12.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/argcomplete/598f87f072f66e2269dd6919292b2934dbb20492
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/activate-global-python-argcomplete
/usr/bin/python-argcomplete-check-easy-install-script
/usr/bin/python-argcomplete-tcsh
/usr/bin/register-python-argcomplete

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/argcomplete/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
