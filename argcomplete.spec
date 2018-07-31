#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8AFAFCD242818A52 (kislyuk@gmail.com)
#
Name     : argcomplete
Version  : 1.9.4
Release  : 48
URL      : https://files.pythonhosted.org/packages/3c/21/9741e5e5e63245a8cdafb32ffc738bff6e7ef6253b65953e77933e56ce88/argcomplete-1.9.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/3c/21/9741e5e5e63245a8cdafb32ffc738bff6e7ef6253b65953e77933e56ce88/argcomplete-1.9.4.tar.gz
Source99 : https://files.pythonhosted.org/packages/3c/21/9741e5e5e63245a8cdafb32ffc738bff6e7ef6253b65953e77933e56ce88/argcomplete-1.9.4.tar.gz.asc
Summary  : Bash tab completion for argparse
Group    : Development/Tools
License  : Apache-2.0
Requires: argcomplete-bin
Requires: argcomplete-python3
Requires: argcomplete-license
Requires: argcomplete-python
Requires: coverage
Requires: flake8
Requires: pexpect
Requires: wheel
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
Requires: argcomplete-license

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
%setup -q -n argcomplete-1.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533001465
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose test/test.py || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/argcomplete
cp LICENSE.rst %{buildroot}/usr/share/doc/argcomplete/LICENSE.rst
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
%defattr(-,root,root,-)
/usr/share/doc/argcomplete/LICENSE.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
