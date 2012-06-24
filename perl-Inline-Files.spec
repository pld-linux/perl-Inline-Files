%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Files
Summary:	Inline::Files perl module
Summary(pl):	Modu� perla Inline::Files
Name:		perl-Inline-Files
Version:	0.60
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
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
perl Makefile.PL </dev/null
%{__make}

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
