%global _empty_manifest_terminate_build 0
Name:		python-absl-py
Version:	0.10.0
Release:	2
Summary:	Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
License:	Apache 2.0
URL:		https://github.com/abseil/abseil-py
Source0:	https://files.pythonhosted.org/packages/49/7c/1d9fa17c363b5ff395cc6f5fd03219b9d303f31268983325974570d0d500/absl-py-0.10.0.tar.gz
BuildArch:	noarch

Requires:	python3-six
Requires:	python3-enum34

%description
# Abseil Python Common Libraries

This repository is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

## Features

* Simple application startup
* Distributed commandline flags system
* Custom logging module with additional features
* Testing utilities

## Getting Started

### Installation

To install the package, simply run:

```bash
pip install absl-py
```

Or install from source:

```bash
python setup.py install
```

### Running Tests

To run Abseil tests, you can clone the git repo and run
[bazel](https://bazel.build/):

```bash
git clone https://github.com/abseil/abseil-py.git
cd abseil-py
bazel test absl/...
```

### Example Code

Please refer to
[smoke_tests/sample_app.py](https://github.com/abseil/abseil-py/blob/master/smoke_tests/sample_app.py)
as an example to get started.

## Documentation

See the [Abseil Python Developer Guide](https://abseil.io/docs/python/).

## Future Releases

The current repository includes an initial set of libraries for early adoption.
More components and interoperability with Abseil C++ Common Libraries
will come in future releases.

## License

The Abseil Python library is licensed under the terms of the Apache
license. See [LICENSE](LICENSE) for more information.




%package -n python3-absl-py
Summary:	Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
Provides:	python-absl-py
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-absl-py
# Abseil Python Common Libraries

This repository is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

## Features

* Simple application startup
* Distributed commandline flags system
* Custom logging module with additional features
* Testing utilities

## Getting Started

### Installation

To install the package, simply run:

```bash
pip install absl-py
```

Or install from source:

```bash
python setup.py install
```

### Running Tests

To run Abseil tests, you can clone the git repo and run
[bazel](https://bazel.build/):

```bash
git clone https://github.com/abseil/abseil-py.git
cd abseil-py
bazel test absl/...
```

### Example Code

Please refer to
[smoke_tests/sample_app.py](https://github.com/abseil/abseil-py/blob/master/smoke_tests/sample_app.py)
as an example to get started.

## Documentation

See the [Abseil Python Developer Guide](https://abseil.io/docs/python/).

## Future Releases

The current repository includes an initial set of libraries for early adoption.
More components and interoperability with Abseil C++ Common Libraries
will come in future releases.

## License

The Abseil Python library is licensed under the terms of the Apache
license. See [LICENSE](LICENSE) for more information.




%package help
Summary:	Development documents and examples for absl-py
Provides:	python3-absl-py-doc
%description help
# Abseil Python Common Libraries

This repository is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

## Features

* Simple application startup
* Distributed commandline flags system
* Custom logging module with additional features
* Testing utilities

## Getting Started

### Installation

To install the package, simply run:

```bash
pip install absl-py
```

Or install from source:

```bash
python setup.py install
```

### Running Tests

To run Abseil tests, you can clone the git repo and run
[bazel](https://bazel.build/):

```bash
git clone https://github.com/abseil/abseil-py.git
cd abseil-py
bazel test absl/...
```

### Example Code

Please refer to
[smoke_tests/sample_app.py](https://github.com/abseil/abseil-py/blob/master/smoke_tests/sample_app.py)
as an example to get started.

## Documentation

See the [Abseil Python Developer Guide](https://abseil.io/docs/python/).

## Future Releases

The current repository includes an initial set of libraries for early adoption.
More components and interoperability with Abseil C++ Common Libraries
will come in future releases.

## License

The Abseil Python library is licensed under the terms of the Apache
license. See [LICENSE](LICENSE) for more information.




%prep
%autosetup -n absl-py-0.10.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-absl-py -f filelist.lst
%{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Jun 02 2021 guoqinglan <guoqinglan@uniontech.com> - 0.10.0-2
- clear out the __pycache__ folders after yum remove 

* Sun Oct 04 2020 Python_Bot <Python_Bot@openeuler.org> - 0.10.0-1
- Package Spec generated
