#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Files
Summary:	Inline::Files Perl module
Summary(cs.UTF-8):	Modul Inline::Files pro Perl
Summary(da.UTF-8):	Perlmodul Inline::Files
Summary(de.UTF-8):	Inline::Files Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::Files
Summary(fr.UTF-8):	Module Perl Inline::Files
Summary(it.UTF-8):	Modulo di Perl Inline::Files
Summary(ja.UTF-8):	Inline::Files Perl モジュール
Summary(ko.UTF-8):	Inline::Files 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::Files
Summary(pl.UTF-8):	Moduł Perla Inline::Files
Summary(pt.UTF-8):	Módulo de Perl Inline::Files
Summary(pt_BR.UTF-8):	Módulo Perl Inline::Files
Summary(ru.UTF-8):	Модуль для Perl Inline::Files
Summary(sv.UTF-8):	Inline::Files Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::Files
Summary(zh_CN.UTF-8):	Inline::Files Perl 模块
Name:		perl-Inline-Files
Version:	0.63
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	460ed656cb55cba677ae774319958fc2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Filter
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Files - Multiple virtual files at the end of your Perl code.

%description -l pl.UTF-8
Moduł Inline::Files - pozwalający na umieszczenie wielu wirtualnych
plików na końcu kodu w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
