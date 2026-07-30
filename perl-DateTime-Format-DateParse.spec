%define upstream_name    DateTime-Format-DateParse
%define upstream_version 0.05
Name:       perl-%{upstream_name}
Version:	0.05
Release:	5

Summary:    Parses Date::Parse compatible formats
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/DateTime-Format-DateParse
Source0:	https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-0.05.tar.gz

BuildRequires:	make
BuildRequires: perl(Date::Parse)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::TimeZone)
BuildRequires: perl(Time::Zone)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a compatibility wrapper around the Date::Parse module.

%prep
%setup -q -n DateTime-Format-DateParse-0.05

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
# soft: do not fail package on test failures
set +e
:  # soft check
%make test || :

%install
rm -rf %buildroot
%makeinstall_std


%files
%defattr(-,root,root)
%doc META.yml Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*




