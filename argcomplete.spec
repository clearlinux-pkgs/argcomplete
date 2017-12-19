#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8AFAFCD242818A52 (kislyuk@gmail.com)
#
Name     : argcomplete
Version  : 1.9.3
Release  : 29
URL      : https://pypi.python.org/packages/8b/54/4a431fe1dfac0d9ae9adc725d2fe543fad07fb7d87f15bd732ba63672bb4/argcomplete-1.9.3.tar.gz
Source0  : https://pypi.python.org/packages/8b/54/4a431fe1dfac0d9ae9adc725d2fe543fad07fb7d87f15bd732ba63672bb4/argcomplete-1.9.3.tar.gz
Source99 : https://pypi.python.org/packages/8b/54/4a431fe1dfac0d9ae9adc725d2fe543fad07fb7d87f15bd732ba63672bb4/argcomplete-1.9.3.tar.gz.asc
Summary  : Bash tab completion for argparse
Group    : Development/Tools
License  : Apache-2.0
Requires: argcomplete-bin
Requires: argcomplete-legacypython
Requires: argcomplete-python3
Requires: argcomplete-python
Requires: coverage
Requires: flake8
Requires: pexpect
Requires: wheel
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==============================================
        *Tab complete all the things!*
        
        Argcomplete provides easy, extensible command line tab completion of arguments for your Python script.

%package bin
Summary: bin components for the argcomplete package.
Group: Binaries

%description bin
bin components for the argcomplete package.


%package legacypython
Summary: legacypython components for the argcomplete package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the argcomplete package.


%package python
Summary: python components for the argcomplete package.
Group: Default
Requires: argcomplete-legacypython
Requires: argcomplete-python3

%description python
python components for the argcomplete package.


%package python3
Summary: python3 components for the argcomplete package.
Group: Default
Requires: python3-core

%description python3
python3 components for the argcomplete package.


%prep
%setup -q -n argcomplete-1.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510935469
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose test/test.py || :
%install
export SOURCE_DATE_EPOCH=1510935469
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
