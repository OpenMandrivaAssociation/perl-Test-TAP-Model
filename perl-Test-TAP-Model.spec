%define upstream_name    Test-TAP-Model
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Accessible (queryable, serializable object) result collector
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Method::Alias)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::Harness::Straps)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Test/TAP/example.pl

%files
%doc Changes example.pl
%{_mandir}/man3/*
%{perl_vendorlib}/Test

%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 405598
- rebuild using %%perl_convert_version

* Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-2mdv2009.0
+ Revision: 283296
- examples belongs to documentation (fix conflict with perl-Test-TAP-Matrix)

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
+ Revision: 227977
- update to new version 0.10

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 213837
- import perl-Test-TAP-Model


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
- first mdv release
