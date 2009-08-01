%define upstream_name    Test-TAP-Model
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Accessible (queryable, serializable object) result collector
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Method::Alias)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a subclass of the Test::Harness::Straps manpage (although in
an ideal world it would really use delegation).

It uses callbacks in the straps object to construct a deep structure, with
all the data known about a test run accessible within.

It's purpose is to ease the processing of test data, for the purpose of
generating reports, or something like that.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Test/TAP/example.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes example.pl
%{_mandir}/man3/*
%{perl_vendorlib}/Test
