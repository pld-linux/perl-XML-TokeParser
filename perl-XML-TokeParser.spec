#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	XML
%define		pnam	TokeParser
Summary:	XML::TokeParser - Simplified interface to XML::Parser
Summary(pl.UTF-8):	XML::TokeParser - uproszczony interfejs do modułu XML::Parser
Name:		perl-XML-TokeParser
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a886ac451d99dca522df20d7cf7b28b4
URL:		http://search.cpan.org/dist/XML-TokeParser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Parser >= 2
%endif
Requires:	perl-XML-Parser >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::TokeParser provides a procedural ("pull mode") interface to
XML::Parser in much the same way that Gisle Aas' HTML::TokeParser
provides a procedural interface to HTML::Parser. XML::TokeParser
splits its XML input up into "tokens," each corresponding to an
XML::Parser event.

%description -l pl.UTF-8
XML::TokeParser udostępnia proceduralny (działający w trybie "pull")
interfejs do modułu XML::Parser w podobny sposób, jak moduł Gisle Aasa
HTML::TokeParser udostępnia proceduralny interfejs do modułu
HTML::Parser. XML::TokeParser dzieli wejście XML na "tokeny", z
których każdy odpowiada zdarzeniu modułu XML::Parser.

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
%doc Changes README TODO
%{perl_vendorlib}/XML/TokeParser.pm
%{_mandir}/man3/XML::TokeParser.3pm*
