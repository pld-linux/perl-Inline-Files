#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Files
Summary:	Inline::Files Perl module
Summary(cs):	Modul Inline::Files pro Perl
Summary(da):	Perlmodul Inline::Files
Summary(de):	Inline::Files Perl Modul
Summary(es):	M�dulo de Perl Inline::Files
Summary(fr):	Module Perl Inline::Files
Summary(it):	Modulo di Perl Inline::Files
Summary(ja):	Inline::Files Perl �⥸�塼��
Summary(ko):	Inline::Files �� ����
Summary(no):	Perlmodul Inline::Files
Summary(pl):	Modu� Perla Inline::Files
Summary(pt):	M�dulo de Perl Inline::Files
Summary(pt_BR):	M�dulo Perl Inline::Files
Summary(ru):	������ ��� Perl Inline::Files
Summary(sv):	Inline::Files Perlmodul
Summary(uk):	������ ��� Perl Inline::Files
Summary(zh_CN):	Inline::Files Perl ģ��
Name:		perl-Inline-Files
Version:	0.60
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Filter
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Files - Multiple virtual files at the end of your Perl code.

%description -l pl
Modu� Inline::Files - pozwalaj�cy na umieszczenie wielu wirtualnych
plik�w na ko�cu kodu w Perlu.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL </dev/null
%{__make}
%{!?_without_tests:%{__make} test}

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
%{perl_sitelib}/Inline/Files.pm
%{perl_sitelib}/Inline/Files
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
