#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Files
Summary:	Inline::Files Perl module
Summary(cs):	Modul Inline::Files pro Perl
Summary(da):	Perlmodul Inline::Files
Summary(de):	Inline::Files Perl Modul
Summary(es):	Módulo de Perl Inline::Files
Summary(fr):	Module Perl Inline::Files
Summary(it):	Modulo di Perl Inline::Files
Summary(ja):	Inline::Files Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Files ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Inline::Files
Summary(pl):	Modu³ Perla Inline::Files
Summary(pt):	Módulo de Perl Inline::Files
Summary(pt_BR):	Módulo Perl Inline::Files
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Files
Summary(sv):	Inline::Files Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Files
Summary(zh_CN):	Inline::Files Perl Ä£¿é
Name:		perl-Inline-Files
Version:	0.62
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	1beb4548be878a28cafb379945c402b8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Filter
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Files - Multiple virtual files at the end of your Perl code.

%description -l pl
Modu³ Inline::Files - pozwalaj±cy na umieszczenie wielu wirtualnych
plików na koñcu kodu w Perlu.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/Files.pm
%{perl_vendorlib}/Inline/Files
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
