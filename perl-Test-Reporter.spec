#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Reporter
Summary:	Test::Reporter - sends test results to cpan-testers@perl.org
Summary(pl.UTF-8):	Test::Reporter - wysyłanie wyników testów na adres cpan-testers@perl.org
Name:		perl-Test-Reporter
Version:	1.5203
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	724d901e4cb86705c364be855d3b205b
URL:		http://search.cpan.org/dist/Test-Reporter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Reporter reports the test results of any given distribution to
the CPAN Testers. Test::Reporter has wide support for various perl5's
and platforms.

%description -l pl.UTF-8
Test::Reporter zgłasza wyniki testów podanego pakietu na listę CPAN
Testers (testerów CPAN). Test::Reporter obsługuje szeroki zakres
wersji Perla 5 i platform.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Reporter
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/cpantest
%{_mandir}/man1/*
