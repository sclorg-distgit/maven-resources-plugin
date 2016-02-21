%global pkg_name maven-resources-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.6
Release:        6.12%{?dist}
Summary:        Maven Resources Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-resources-plugin
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-jar-plugin
BuildRequires: %{?scl_prefix}maven-install-plugin
BuildRequires: %{?scl_prefix}maven-compiler-plugin
BuildRequires: %{?scl_prefix}maven-javadoc-plugin
BuildRequires: %{?scl_prefix}maven-surefire-plugin
BuildRequires: %{?scl_prefix}maven-surefire-provider-junit
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}maven-plugin-testing-harness
BuildRequires: %{?scl_prefix}maven-reporting-impl
BuildRequires: %{?scl_prefix}plexus-interpolation
BuildRequires: %{?scl_prefix}plexus-digest
BuildRequires: %{?scl_prefix}maven-project
BuildRequires: %{?scl_prefix}maven-monitor
BuildRequires: %{?scl_prefix}maven-filtering


%description
The Resources Plugin handles the copying of project resources
to the output directory.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 2.6-6.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.6-6.11
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.6-6.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.6-6.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.6-6
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 2.6-5
- Migrate away from mvn-rpmbuild (Resolves: #997513)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-4
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.6-1
- Update to latest upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Tomas Radej <tradej@redhat.com> - 2.5-4
- Fixed dependency on plexus-container-default

* Tue Aug 30 2011 Tomas Radej <tradej@redhat.com> - 2.5-3
- Added changelog

* Mon Aug 29 2011 Tomas Radej <tradej@redhat.com> - 2.5-1
- Update to 2.5
- Guideline fixes
- Added maven-filtering dep

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4.3-4
- Add several packages to BR/R as stated in pom.xml

* Tue Jun 21 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4.3-3
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

*Thu Sep 09 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.4.3-1
- Update to 2.4.3

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 2.2-6
- delete duplicate maven2-plugin-jar
- delete source1

* Tue May 20 2010 Hui Wang <huwang@redhat.com> - 2.2-5
- Add maven-resources-plugin-demap.xml
- Set maven test ignore

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.2-4
- Add missing obsoletes/provides

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.2-3
- Add missing BR:maven-shared-reporting-impl

* Mon May 17 2010 Hui Wang <huwang@redhat.com> - 2.2-2
- Fixed install -pm 644 pom.xml

* Thu May 13 2010 Hui Wang <huwang@redhat.com> - 2.2-1
- Initial version of the package
