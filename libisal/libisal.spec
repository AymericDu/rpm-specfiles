%define         tarname isa-l

Name:           libisal
Version:        2.14.0
Release:        1%{?dist}
Summary:        Intel(R) Intelligent Storage Acceleration Library

License:        BSD
URL:            https://01.org/intel®-storage-acceleration-library-open-source-version/
Source0:        https://01.org/sites/default/files/downloads/intelr-storage-acceleration-library-open-source-version/isa-l-%{version}.tar.gz

BuildRequires:  yasm-devel
BuildRequires:  automake >= 1.14
Requires:       yasm

%description
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general
Reed-Solomon type encoding for blocks of data that helps protect against
erasure of whole blocks. The general ISA-L library contains an expanded
set of functions used for data protection, hashing, encryption, etc.
.
This package contains the shared library.

%package devel
Summary: Intel(R) Intelligent Storage Acceleration Library - devel files
Requires:       %{name}-common = %{version}
%description devel
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general
Reed-Solomon type encoding for blocks of data that helps protect against
erasure of whole blocks. The general ISA-L library contains an expanded
set of functions used for data protection, hashing, encryption, etc.
.
This package contains the development files needed to build against the shared
library.


%prep
%setup -q -n %{tarname}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
%{_libdir}/*

%files devel
%{_includedir}/*


%changelog
* Wed May 25 2016 Romain Acciari <romain.acciari@openio.io> - 2.14.0
- Initial release
