Name:           xmltv
Version:        0.6.3
Release:        3%{?dist}
Summary:        A set of utilities to manage your TV viewing

License:        GPLv2+
URL:            http://xmltv.org/wiki/
Source0:        https://github.com/XMLTV/xmltv/archive/v%{version}/xmltv-v%{version}.tar.gz

# Upstream patches since release
Patch0001:      0001-Reenable-tv_grab_ch_search.patch
Patch0002:      0002-README.md-update-TOC.patch
Patch0003:      0003-README.md-refresh-req-d-rec-d-modules-list.patch
Patch0004:      0004-tv_imdb-fix-some-typos.patch
Patch0005:      0005-tv_imdb-use-warnings.patch
Patch0006:      0006-tv_imdb-refresh-short-description-POD.patch
Patch0007:      0007-tv_grab_zz_sdjson_sqlite-fix-a-typo.patch
Patch0008:      0008-Update-tv_grab_eu_xmltvse-to-use-SSL-116.patch
Patch0009:      0009-update-version-for-cherry-pick-typo-correction.patch
Patch0010:      0010-programme-detect-parental-level-with-white-space.patch
Patch0011:      0011-Remove-swedb-grabber-117.patch
Patch0012:      0012-ampparit-add-missing-empty-title-check.patch
Patch0013:      0013-telsu-add-missing-empty-title-check.patch
Patch0014:      0014-tv_grab_uk_tvguide-fix-for-missing-form-options-in-c.patch
Patch0015:      0015-avoid-break-when-website-object-missing-125.patch
Patch0016:      0016-fix-UA-page-debug-is-on-stdout-should-be-on-stderr-1.patch
Patch0017:      0017-Fetch-programme-data-via-SSL-avoids-301-redirects.patch
Patch0018:      0018-for-compatability-with-older-versions-of-Perl-122.patch
Patch0019:      0019-download-optional-file-if-its-prepStage-is-specifica.patch
Patch0020:      0020-Unbreak-parsing-of-keywords-file.patch
Patch0021:      0021-Reduce-memory-consumption-in-building-database-63.patch
Patch0022:      0022-replace-spaces-with-tabs-and-prettify-the-code.patch
Patch0023:      0023-iltapulu-fix-channel-parser.patch
Patch0024:      0024-iltapulu-fix-grab-parser.patch
Patch0025:      0025-source-avoid-name-clashes-between-modules.patch
Patch0026:      0026-test.conf-update-to-latest-list-channels-output.patch
Patch0027:      0027-Make-channel-ids-compliant-with-the-DTD.-Use-legacyc.patch
Patch0028:      0028-Change-whitespace-to-tabs.patch
Patch0029:      0029-Add-info-message-about-frozen-IMDb-data.patch
Patch0030:      0030-Add-undocumented-sample-option-to-limit-records-proc.patch
Patch0031:      0031-Reduce-memory-usage-during-final-build-stage.patch
Patch0032:      0032-Remove-tv-episodes-from-intermediate-files.patch
Patch0033:      0033-eu_xmltvse-refresh-test.conf.patch
Patch0034:      0034-dk_dr-disable-grabber-after-source-site-disappeared.patch
Patch0035:      0035-Fix-testsuite-for-the-change-to-episode-handling-63.patch
Patch0036:      0036-update-windows-xmltv.exe-to-use-PAR-Packer-rather-th.patch
Patch0037:      0037-extend-scope-of-title-person-qualifier.patch
Patch0038:      0038-eu-epgdata-Add-channel-IDs.patch
Patch0039:      0039-whitespace-changes.patch
Patch0040:      0040-Reduce-memory-usage-during-database-build-bug-fixes.patch
Patch0041:      0041-bugfixes-in-augment-function.patch
Patch0042:      0042-Add-tests-for-edge-cases.patch
Patch0043:      0043-Use-disc-sort-to-reduce-memory-usage-63.patch
Patch0044:      0044-Option-to-exclude-tv-series-from-the-database-build.patch
Patch0045:      0045-fix-broken-url-to-imdb-website.patch
Patch0046:      0046-fix-minor-typo-in-example.patch
Patch0047:      0047-fix-broken-tests.patch
Patch0048:      0048-Added-option-channel-id-exp-to-filter-by-regex-on-ch.patch
Patch0049:      0049-tv_grep-added-tests-for-new-option-channel-id-exp.patch
Patch0050:      0050-clean-up-windows-xmltv.exe-s-PAR-Packer-based-build-.patch

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ProgressBar)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Search::Dict)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(lib)
BuildRequires:  perl(integer)
BuildRequires:  perl(Unicode::String)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::ProgressBar)
BuildRequires:  perl(Tk::TableMatrix)
BuildRequires:  perl(PerlIO::gzip)
BuildRequires:  perl(Unicode::String)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Lingua::Preferred)
# Grabber use
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Language)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::ISO8601)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  perl(DateTime::Format::SQLite)
%endif
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Cache::Transparent)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::ConnCache)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(LWP::UserAgent::Determined)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Encode)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::TreePP)
BuildRequires:  perl(XML::Twig) >= 3.10
BuildRequires:  perl(XML::Writer)
BuildRequires:  make

Requires:       xmltv-grabbers >= %{version}-%{release}
Requires:       perl(PerlIO::gzip)
Requires:       perl(Unicode::String)

%description
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

%package -n perl-XMLTV
Summary:        Perl modules for managing your TV viewing
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Term::ProgressBar)
Requires:       perl(Lingua::Preferred)

%description -n perl-XMLTV
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the perl modules from xmltv.

%package grabbers
Summary:        Backends for xmltv
Requires:       perl-XMLTV >= %{version}-%{release}
Requires:       perl(JSON::XS)

%description grabbers
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the backends (grabbers) for xmltv.

%package gui
Summary:        Graphical frontends to xmltv
Requires:       perl-XMLTV >= %{version}-%{release}

%description gui
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains graphical frontends to xmltv.


%prep
%autosetup -p1


%build
%{__perl} Makefile.PL -default INSTALLDIRS=vendor
%{make_build}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
make share_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT


%check
make test


%files
%doc Changes README.md
%doc doc/*
%{_bindir}/tv_augment
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
%{_bindir}/tv_augment_tz
%{_bindir}/tv_count
%{_bindir}/tv_merge
%{_mandir}/man1/tv_augment.1*
%{_mandir}/man1/tv_count.1*
%{_mandir}/man1/tv_merge.1*
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
%{_mandir}/man1/tv_augment_tz.1*
%{_datadir}/%{name}

%files -n perl-XMLTV
%{perl_vendorlib}/XMLTV.pm
%{perl_vendorlib}/XMLTV
%{_mandir}/man3/*.3*

%files grabbers
%{_bindir}/tv_grab_*
%{_mandir}/man1/tv_grab_*.1*

%files gui
%{_bindir}/tv_check
%{_mandir}/man1/tv_check.1*


%changelog
* Sat Jan 23 2021 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.3-3
- update to recent upstream patches

* Wed Nov 04 2020 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.3-2
- Add BR make

* Sat Aug 22 2020 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.3-1
- Update to xmltv 0.6.3 release

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Paul Howarth <paul@city-fan.org> - 0.6.1-13
- Perl 5.32 rebuild

* Tue Jun 09 2020 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-12
- use preferred make macro for build

* Tue Jun 09 2020 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-11
- install share files

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-9
- Pull in upstream patches to resolve grabber issues

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-7
- Pull in latest patch from upstream to produce warning message

* Thu May 23 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-6
- Build tv_grab_zz_sdjson_sqlite for el7 now that
  perl-DateTime-Format-SQLite has landed in epel7

* Mon May 13 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-5
- Pull in patches from upstream to resolve various issues and remove
  local fixup for versioning

* Sun May 12 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-4
- Correct permissions of installed files

* Fri May 10 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-3
- Fix el6 dependencies by not building tv_grab_zz_sdjson_sqlite on el6

* Thu May 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-2
- Fix broken requires version (rfbz#5243)

* Mon Apr 01 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> - 0.6.1-1
- Update for XMLTV 0.6.1

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.5.70-4
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.5.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Sérgio Basto <sergio@serjux.com> - 0.5.70-1
- Update xmltv to 0.5.70

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.5.69-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Sérgio Basto <sergio@serjux.com> - 0.5.69-4
- Requires perl(JSON::XS) rfbz(#4563)

* Sun Jun 18 2017 Paul Howarth <paul@city-fan.org> - 0.5.69-3
- Perl 5.26 rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.5.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Richard Shaw <hobbes1069@gmail.com> - 0.5.69-1
- Update to latest upstream release.

* Fri Sep 30 2016 Sérgio Basto <sergio@serjux.com> - 0.5.68-3
- Add perl-generators to get proper requires/provides on F-25 and later

* Fri Sep 30 2016 Sérgio Basto <sergio@serjux.com> - 0.5.68-2
- Rebuild for Perl with locale (buildroot with glibc-all-langpacks)

* Sun Jul 24 2016 Sérgio Basto <sergio@serjux.com> - 0.5.68-1
- Update xmltv to 0.5.68

* Sat Feb 20 2016 Richard Shaw <hobbes1069@gmail.com> - 0.5.67-2
- Add additional build requirements for additional grabbers.
  Fixes BZ#3983.

* Tue Aug 25 2015 Richard Shaw <hobbes1069@gmail.com> - 0.5.67-1
- Update to latest upstream release.

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.5.66-2
- Fix FTBFS (rf#3621)

* Tue Oct 28 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.5.66-1
- Update to 0.5.66.

* Fri May  9 2014 Richard Shaw <hobbes1069@gmail.com> - 0.5.65-1
- Update to latest upstream release:
  http://sourceforge.net/projects/xmltv/files/xmltv/0.5.65/

* Wed Feb 12 2014 Richard Shaw <hobbes1069@gmail.com> - 0.5.64-1
- Update to latest upstream release
- For changes see:
  http://sourceforge.net/projects/xmltv/files/xmltv/0.5.64/

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5.63-3
- Rebuilt

* Sun Aug 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.63-2
- Rebuilt (branching)

* Tue Jul 24 2012 Richard Shaw <hobbes1069@gmail.com> - 0.5.63-1
- Update to 0.5.63

* Mon Aug 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.5.61-1
- Update 0.5.61

* Sat Nov 27 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.5.59-1
- rebuilt

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

