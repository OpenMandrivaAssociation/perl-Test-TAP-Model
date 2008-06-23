%define module   Test-TAP-Model
%define version    0.10
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Accessible (queryable, serializable object) result collector
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires: perl(Method::Alias)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module is a subclass of the Test::Harness::Straps manpage (although in
an ideal world it would really use delegation).

It uses callbacks in the straps object to construct a deep structure, with
all the data known about a test run accessible within.

It's purpose is to ease the processing of test data, for the purpose of
generating reports, or something like that.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Test

