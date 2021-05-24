#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-TableExtract
Version  : 2.15
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSISK/HTML-TableExtract-2.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSISK/HTML-TableExtract-2.15.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-tableextract-perl/libhtml-tableextract-perl_2.15-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-HTML-TableExtract-license = %{version}-%{release}
Requires: perl-HTML-TableExtract-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Parser)

%description
HTML-TableExtract
-----------------
HTML::TableExtract is a module that simplifies the extraction of
information contained in tables within HTML documents.

%package dev
Summary: dev components for the perl-HTML-TableExtract package.
Group: Development
Provides: perl-HTML-TableExtract-devel = %{version}-%{release}
Requires: perl-HTML-TableExtract = %{version}-%{release}

%description dev
dev components for the perl-HTML-TableExtract package.


%package license
Summary: license components for the perl-HTML-TableExtract package.
Group: Default

%description license
license components for the perl-HTML-TableExtract package.


%package perl
Summary: perl components for the perl-HTML-TableExtract package.
Group: Default
Requires: perl-HTML-TableExtract = %{version}-%{release}

%description perl
perl components for the perl-HTML-TableExtract package.


%prep
%setup -q -n HTML-TableExtract-2.15
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-tableextract-perl_2.15-1.debian.tar.xz
cd %{_builddir}/HTML-TableExtract-2.15
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-TableExtract-2.15/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-TableExtract
cp %{_builddir}/HTML-TableExtract-2.15/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTML-TableExtract/2947c073e37b38625d34a6a565e480dd8033dc0f
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-TableExtract/1c66780e3211e50f3f4019ede6760ba3fa55c006
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::TableExtract.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-TableExtract/1c66780e3211e50f3f4019ede6760ba3fa55c006
/usr/share/package-licenses/perl-HTML-TableExtract/2947c073e37b38625d34a6a565e480dd8033dc0f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTML/TableExtract.pm
