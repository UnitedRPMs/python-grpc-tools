%global gitdate 20181122
%global commit0 a933c40e679c5aef7107e7561e827cd12a1008e0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           python-grpc-tools
Version:        1.16.1
Release:        1%{?dist}
Summary:        Python protobuf generator for GRPC

License:        GPLv2+
URL:            https://grpc.io/
Source0:	https://github.com/grpc/grpc/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	%{name}-snapshot

BuildRequires:  python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-Cython
BuildRequires:	dh-python3
BuildRequires:	gcc-c++
BuildRequires:	git
Provides:	python3-grpc-tools

%description
Python protobuf generator for GRPC


%prep

# We need some submodules
%{S:1} -c %{commit0}

%autosetup -T -D -n %{name}-%{shortcommit0} 

find -type f -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build

%py3_build

%install
%py3_install

%check
%{__python3} setup.py test	

%files
%{python3_sitearch}/grpc/
%{python3_sitearch}/grpcio-*.egg-info/


%changelog

* Thu Nov 22 2018 David Va <davidva AT tuta DOT io> 1.16.1-1
- Initial build

