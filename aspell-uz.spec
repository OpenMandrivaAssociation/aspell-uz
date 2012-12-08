%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.6-0
%define version 0.6.0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Uzbek
%define languagecode uz
%define lc_ctype uz_UZ

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       %version
Release:       %mkrel 11
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}
Provides:      spell-%{languagecode}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv README README.%{languagecode}
chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-9mdv2011.0
+ Revision: 662878
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-8mdv2011.0
+ Revision: 603470
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-7mdv2010.1
+ Revision: 518971
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-6mdv2010.0
+ Revision: 413112
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.6.0-5mdv2009.1
+ Revision: 350127
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-4mdv2009.0
+ Revision: 220458
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.6.0-3mdv2008.1
+ Revision: 182664
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Mar 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-1mdv2007.1
+ Revision: 138951
- new release (#25916)

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-1mdv2007.1
+ Revision: 123388
- Import aspell-uz

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-1mdv2007.1
- use the mkrel macro
- disable debug packages

* Mon Feb 13 2006 Pablo Saratxaga <pablo@mandriva.com> 0.5.0-1mdk
- new release

* Mon Nov 28 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.04.0-1mdk
- new release

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandriva.com> 0.03.0-1mdk
- new release

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandriva.com> 0.02.1-1mdk
- first version

