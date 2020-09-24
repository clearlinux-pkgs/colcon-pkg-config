#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-pkg-config
Version  : 0.1.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/7c/3f/9979f90a2dc5fe5da4341fab6c3035aaf885f2bf7177fc9de1ea36f3eacb/colcon-pkg-config-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/3f/9979f90a2dc5fe5da4341fab6c3035aaf885f2bf7177fc9de1ea36f3eacb/colcon-pkg-config-0.1.0.tar.gz
Summary  : Extension for colcon adding an environment variable to find pkg-config files.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-pkg-config-python = %{version}-%{release}
Requires: colcon-pkg-config-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
===================

%package python
Summary: python components for the colcon-pkg-config package.
Group: Default
Requires: colcon-pkg-config-python3 = %{version}-%{release}

%description python
python components for the colcon-pkg-config package.


%package python3
Summary: python3 components for the colcon-pkg-config package.
Group: Default
Requires: python3-core
Provides: pypi(colcon_pkg_config)
Requires: pypi(colcon_core)

%description python3
python3 components for the colcon-pkg-config package.


%prep
%setup -q -n colcon-pkg-config-0.1.0
cd %{_builddir}/colcon-pkg-config-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583528413
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
