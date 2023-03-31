%define	version	2.4.2
%define release 21
%define dict_format_version	2.4.2

Summary:	English -> Serbo-Croat Freedict dictionary for StarDict 2
Name:		stardict-freedict-eng-scr
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

# http://freedict.sourceforge.net/download/linux/eng-scr.tar.gz
Source0:	http://deaddog.org/stardict/stardict-dictd_www.freedict.de_eng-scr-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
English -> Serbo-Croat Freedict dictionary in StarDict 2 format
(originally for dictd)

%prep
%setup -q -n stardict-dictd_www.freedict.de_eng-scr-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-8mdv2011.0
+ Revision: 670070
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-7mdv2011.0
+ Revision: 607629
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-6mdv2010.1
+ Revision: 521577
- rebuilt for 2010.1

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-5mdv2009.0
+ Revision: 219631
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Mar 08 2007 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-4mdv2007.1
+ Revision: 137725
- Import stardict-freedict-eng-scr

* Thu Mar 08 2007 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-4mdv2007.1
- use the %%mkrel macro

* Sun Oct 02 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- Rebuild

* Wed Jun 02 2004 Abel Cheung <deaddog@deaddog.org> 2.4.2-2mdk
- Dictionaries require main program as well

