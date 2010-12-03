%define	version	2.4.2
%define release %mkrel 7
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


