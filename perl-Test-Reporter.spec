#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Reporter
Summary:	Test::Reporter - sends test results to cpan-testers@perl.org
#Summary(pl.UTF-8):	
Name:		perl-Test-Reporter
Version:	1.38
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a61f05b45b37074c14db8bfdecfb9659
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Test-Reporter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Reporter reports the test results of any given distribution to the CPAN
Testers. Test::Reporter has wide support for various perl5's and platforms. For
further information visit the below links:

Test::Reporter itself--as a project--also has several links for your visiting
enjoyment:


# %description -l pl.UTF-8
# TODO

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
#%%{perl_vendorlib}/Test/Reporter
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/cpantest
%{_mandir}/man1/*
