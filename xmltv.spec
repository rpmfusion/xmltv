Name:           xmltv
Version:        0.5.58
Release:        1%{?dist}
Summary:        A set of utilities to manage your TV viewing

Group:          Development/Libraries
License:        GPLv2+
URL:            http://xmltv.org/wiki/
Source0:        http://downloads.sourceforge.net/xmltv/xmltv-%{version}.tar.bz2
Patch0:         xmltv-0.5.35-noask.patch
Patch1:         xmltv-0.5.58-noutf8simple.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP) >= 5.65, perl(XML::Parser) >= 2.34
BuildRequires: perl(XML::Twig) >= 3.28
BuildRequires: perl(Date::Manip) >= 5.42
BuildRequires: perl(XML::Writer) >= 0.600
BuildRequires: perl(Memoize), perl(Storable) >= 2.04
BuildRequires: perl(File::Slurp)
# Recommended
BuildRequires: perl(Lingua::EN::Numbers::Ordinate)
BuildRequires: perl(Lingua::Preferred) >= 0.2.4
BuildRequires: perl(Term::ProgressBar) >= 2.03
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Unicode::String)
##
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTML::Entities) >= 1.27
BuildRequires: perl(WWW::Mechanize) => 1.16
BuildRequires: perl(HTTP::Cookies) >= 1.39
BuildRequires: perl(HTML::Form)
BuildRequires: perl(HTTP::Cache::Transparent)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(IO::Scalar), perl(Archive::Zip)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(SOAP::Lite) >= 0.67, perl(Term::ReadKey)
%{?_with_text_bidi:BuildRequires: perl(Text::Bidi)}
BuildRequires: perl(Text::Kakasi)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::DOM)
BuildRequires: perl(XML::LibXSLT)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(IO::Stringy)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Tk::TableMatrix)
BuildRequires: perl(CGI)
BuildRequires: perl(HTML::TokeParser), perl(Date::Parse), perl(Time::Local)
BuildRequires: perl(HTML::TableExtract) >= 1.08
BuildRequires: perl(HTML::Parser) >= 3.34
BuildRequires: perl(Log::TraceMessages)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(IO::Select)
#BuildRequires: perl(Linux::DVB) #Not here yet
BuildRequires: perl(Text::Iconv)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(DateTime)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(DateTime::Format::Strptime)


Requires: xmltv-grabbers >= %{version}-%{release}


%description
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

%package -n perl-XMLTV
Summary: Perl modules for managing your TV viewing
Group: System Environment/Libraries
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description -n perl-XMLTV
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the perl modules from xmltv.

%package grabbers
Summary: Backends for xmltv
Group: Applications/Multimedia
Requires: perl-XMLTV >= %{version}-%{release}

%description grabbers
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the backends (grabbers) for xmltv.

%package gui
Summary: Graphical frontends to xmltv
Group: Applications/Multimedia
Requires: perl-XMLTV >= %{version}-%{release}

%description gui
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains graphical frontends to xmltv.

%prep
%setup -q
%patch0 -p1 -b .noask
%patch1 -p1 -b .noutf8simple

# Fix encoding
cp -pr ChangeLog ChangeLog.not-utf8
iconv -f ISO_8859-1 -t UTF8 ChangeLog.not-utf8 > ChangeLog
touch -r ChangeLog.not-utf8 ChangeLog
rm ChangeLog.not-utf8

# We filter theses from perl-XMLTV as it already has the infra
#for the tui/gui test. And then xmltv-gui will request perl(Tk::TableMatrix)
#which last will bring the previously filtered ones.
# Filter unwanted Requires:
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(Tk)/d' | \
  sed -e '/perl(Tk::ProgressBar)/d'

EOF
%define __perl_requires %{_builddir}/xmltv-%{version}/%{name}-req
chmod +x %{name}-req



%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

# Fix perms
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README
%doc doc/*
%{_bindir}/tv_cat
%{_bindir}/tv_extractinfo_en
%{_bindir}/tv_extractinfo_ar
%{_bindir}/tv_grep
%{_bindir}/tv_imdb
%{_bindir}/tv_remove_some_overlapping
%{_bindir}/tv_sort
%{_bindir}/tv_split
%{_bindir}/tv_to_latex
%{_bindir}/tv_to_text
%{_bindir}/tv_to_potatoe
%{_bindir}/tv_find_grabbers
%{_bindir}/tv_validate_file
%{_bindir}/tv_validate_grabber
%{_mandir}/man1/tv_cat.1*
%{_mandir}/man1/tv_extractinfo_en.1*
%{_mandir}/man1/tv_extractinfo_ar.1*
%{_mandir}/man1/tv_grep.1*
%{_mandir}/man1/tv_imdb.1*
%{_mandir}/man1/tv_remove_some_overlapping.1*
%{_mandir}/man1/tv_sort.1*
%{_mandir}/man1/tv_split.1*
%{_mandir}/man1/tv_to_latex.1*
%{_mandir}/man1/tv_to_text.1*
%{_mandir}/man1/tv_to_potatoe.1*
%{_mandir}/man1/tv_find_grabbers.1*
%{_mandir}/man1/tv_validate_file.1*
%{_mandir}/man1/tv_validate_grabber.1*

%files -n perl-XMLTV
%defattr(-,root,root,-)
%{perl_vendorlib}/XMLTV.pm
%{perl_vendorlib}/XMLTV
%{_mandir}/man3/*.3*

%files grabbers
%defattr(-,root,root,-)
%{_bindir}/tv_grab_*
%{_mandir}/man1/tv_grab_*.1*

%files gui
%defattr(-,root,root,-)
%{_bindir}/tv_check
%{_mandir}/man1/tv_check.1*



%changelog
* Thu Oct 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.5.58-1
- Update to 0.5.58

* Sun Jul 11 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.5.57-2
- rebuilt for perl

* Sat May 29 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.5.57-1
- Update to 0.5.57
- Add new BR

* Wed Dec 30 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.5.56-2
- Rebuild for perl

* Sat Sep 19 2009 kwizart < kwizart at gmail.com > - 0.5.56-1
- Update to 0.5.56

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.5.55-2
- rebuild for new F11 features

* Fri Mar 20 2009 kwizart < kwizart at gmail.com > - 0.5.55-1
- Update to 0.5.55

* Thu Feb 19 2009 kwizart < kwizart at gmail.com > - 0.5.54-1
- Update to 0.5.54

* Wed Oct 15 2008 kwizart < kwizart at gmail.com > - 0.5.53-2
- Add "is" (Iceland) grabber support

* Tue Oct 14 2008 kwizart < kwizart at gmail.com > - 0.5.53-1
- Update to 0.5.53
- Remove -gui requirement on main
- filter perl-Tk dependency on perl-XMLTV
- Re-enable make test

* Thu Jul 31 2008 kwizart < kwizart at gmail.com > - 0.5.52-3
- Add BR perl(Log::TraceMessages)
- Fix perms for %%{_bindir}
- Fix Changelog encoding

* Mon Jul 28 2008 kwizart < kwizart at gmail.com > - 0.5.52-2
- Conditionalize make test

* Sun Jul 20 2008 kwizart < kwizart at gmail.com > - 0.5.52-1
- Update to 0.5.52

* Tue May 27 2008 kwizart < kwizart at gmail.com > - 0.5.51-2
- Add patch to remove BR on Unicode::UTF8simple (backport from upstream)

* Wed Apr 30 2008 kwizart < kwizart at gmail.com > - 0.5.51-1
- Initial package for RPMFusion

