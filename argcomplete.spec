#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF9D6EBDE67769E04 (kislyuk@gmail.com)
#
Name     : argcomplete
Version  : 1.5.1
Release  : 22
URL      : http://pypi.debian.net/argcomplete/argcomplete-1.5.1.tar.gz
Source0  : http://pypi.debian.net/argcomplete/argcomplete-1.5.1.tar.gz
Source99 : http://pypi.debian.net/argcomplete/argcomplete-1.5.1.tar.gz.asc
Summary  : Bash tab completion for argparse
Group    : Development/Tools
License  : Apache-2.0
Requires: argcomplete-bin
Requires: argcomplete-python
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


%package python
Summary: python components for the argcomplete package.
Group: Default

%description python
python components for the argcomplete package.


%prep
%setup -q -n argcomplete-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503071859
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose test/test.py || :
%install
export SOURCE_DATE_EPOCH=1503071859
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
/usr/bin/register-python-argcomplete

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
