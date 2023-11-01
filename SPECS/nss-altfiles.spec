%global commit 89f3f0b390f3bbc58d8964b11a517173ed4eed78
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: NSS module to look up users in /usr/lib/passwd too
Name: nss-altfiles
Version: 2.18.1
Release: 12%{?dist}
#VCS: https://github.com/aperezdc/nss-altfiles
Source0: https://github.com/aperezdc/nss-altfiles/archive/v%{version}.tar.gz
# From pull request: https://github.com/marineam/nss-altfiles/commit/dda5073238b88b4537f2d2707b0ef67bdd11fe06
# FIXME: Change nss-altfiles to not use glibc internal symbols
#Patch0: 0001-Explicitly-link-to-libc.patch
Patch1: ldflags.patch
License: LGPLv2+
URL: https://github.com/aperezdc/nss-altfiles

BuildRequires: glibc-devel

%description
When installed, this package allows looking up users
in %{prefix}/lib/passwd, similarly, groups in %{prefix}/lib/group.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README.md
%{_libdir}/*.so.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Tue Apr 02 2019 Colin Walters <walters@redhat.com> - 2.18.1-12
- Add system LDFLAGS
- Resolves: rhbz#1630609

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.18.1-3
- Build with $RPM_OPT_FLAGS

* Tue Apr 08 2014 Colin Walters <walters@verbum.org>
- Revert patch to link to libc, causes a dep on GLIBC_PRIVATE

* Sat Mar 22 2014 Colin Walters <walters@verbum.org>
- Initial packaging
