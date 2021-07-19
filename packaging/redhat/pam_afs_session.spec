Name: pam_afs_session
Summary: AFS PAG and AFS tokens on login
Version: 2.6
Release: 13%{?dist}
License: MIT
URL: https://www.eyrie.org/~eagle/software/pam-afs-session/
Source: pam-afs-session-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: pam-devel
BuildRequires: krb5-devel
%description
pam-afs-session is a PAM module intended for use with a Kerberos v5 PAM module
to obtain an AFS PAG (Process Authentication Group) and AFS tokens on login. It
puts every new session in a PAG regardless of whether it was authenticated with
Kerberos and runs a configurable external program to obtain tokens.

%define pamdir /%{_lib}/security

%prep
%autosetup -n pam_afs_session-%{version}
# remove non-redhat examples
find examples -mindepth 1 -maxdepth 1 -not -name "redhat" -exec rm -rf {} ';'

%build
%configure --libdir=/%{_lib} --with-aklog=%{_bindir}/aklog
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{pamdir}/*.la

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc NEWS README TODO examples
%{pamdir}/pam_afs_session.so
%{_mandir}/man5/pam_afs_session.5.gz

%changelog
* Mon Jul 19 2021 Jonathan Billings <jsbillings@jsbillings.org> - 2.6-13
- Create RPM spec in source
- Add feature to disable AFS check for kAFS-based builds

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.6-8
- Remove %%{?_isa} on the BuildRequires -devel packages (rhbz#1545203)
- Use HTTPS upstream urls
- Do not remove RPM_BUILD_ROOT in %%install
- Use %%autosetup macro

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6-7
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.6-1
- Update to pam_afs_session 2.6
- Remove unneeded %%defattr
- Use %%license macro

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.5-3
- Remove pam_krb5 requirement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 2 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.5-1
- New upstream release.

* Thu Jun 9 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.4-1
- New upstream release.

* Thu Mar 17 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.2-4
- configure --with-aklog. Your aklog binary better follow the FHS.

* Thu Mar 17 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.2-3
- add dist tag.

* Sun Mar 06 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.2-2
- modify source's examples folder in prep stage

* Sat Mar 05 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.2-1
- New upstream release.
- Only include redhat docs.

* Wed Mar 02 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.1-3
- Rename pam-afs-session to pam_afs_session

* Tue Feb 22 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.1-2
- Add %%{?_isa} on the BuildRequires -devel packages

* Thu Feb 17 2011 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.1-1
- Update to 2.1
- rpmlint fixes

* Fri Sep 10 2010 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.7-1
- basic spec obtained from http://crcmedia.hpcc.nd.edu/wiki/index.php/Automatic_CRC/ND_AFS_cell_setup
- switch out Russ Allbery's pam-krb5 for RedHat's pam_krb5 in Requires
