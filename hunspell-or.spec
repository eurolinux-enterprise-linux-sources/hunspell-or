%global lang or
%global langrelease 1

Name: hunspell-or
Summary: Oriya hunspell dictionaries
Version: 0.03
Epoch:   1
Release: 2%{?dist}
Group:          Applications/Text
License:        GPLv2+
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  aspell
BuildRequires:  hunspell-devel
Requires:       hunspell
BuildArch: noarch

%description
Oriya hunspell dictionaries.This package contains 
the efforts of aspell-or that is converted by
wordlist2hunspell.

%prep
%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}
prezip-bin -d < or.cwl > or.txt

iconv -f ISO-8859-1 -t UTF-8 Copyright > Copyright.utf8
mv Copyright.utf8 Copyright

%build
export LANG=or_IN.utf8
wordlist2hunspell or.txt or_IN

%install
mkdir -p %{buildroot}%{_datadir}/myspell
cp -p *.dic *.aff %{buildroot}%{_datadir}/myspell

%files
%doc README COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Parag <pnemade AT redhat DOT com> - 1:0.03-1
- Update upstream source

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 20050726-7
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
