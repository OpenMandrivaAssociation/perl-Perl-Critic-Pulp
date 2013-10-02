%define upstream_name    Perl-Critic-Pulp
%define upstream_version 80

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 80
Release:	1

Summary:	Don't use Foo:: style barewords
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-Critic-Pulp-80.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::String)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Pod::MinimumVersion)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Perl::Critic::Policy)
BuildRequires:	perl(Perl::Critic::Utils)
BuildRequires:	perl(Perl::Critic::Utils::PPI)
BuildRequires:	perl(Perl::Critic::Violation)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)

BuildArch:	noarch

%description
This is a collection of add-on policies for 'Perl::Critic', summarized
below. They're under a "pulp" theme plus other themes according to their
purpose (see the Perl::Critic/POLICY THEMES manpage).

Roughly half are code related and half cosmetic. You can always enable or
disable the ones you do or don't want. It's normal to pick and choose
things reported. There's a lot of perlcritic policies both built-in and
add-on and they range from helpful things catching problems through to the
bizarre or restrictive, and in some cases mutually contradictory! Many are
only intended as building blocks for enforcing a house style. If you try to
pass everything then you'll give away big parts of the language, so if
you're not turning off or customizing about half then you're either not
trying or you're much too easily lead!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f *.list
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 62.0.0-1mdv2011
+ Revision: 690306
- update to new version 62

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 61.0.0-1
+ Revision: 684782
- update to new version 61

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 60.0.0-1
+ Revision: 677376
- update to new version 60

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 59.0.0-1
+ Revision: 673859
- update to new version 59
- update to new version 58
- update to new version 57

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 48.0.0-2
+ Revision: 657462
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 48.0.0-1
+ Revision: 643450
- update to new version 48

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 47.0.0-2
+ Revision: 640779
- rebuild to obsolete old packages

* Tue Feb 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 47.0.0-1
+ Revision: 636796
- update to new version 47

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 46.0.0-1
+ Revision: 635211
- update to new version 46

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 45.0.0-1mdv2011.0
+ Revision: 625279
- update to new version 45

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 43.0.0-1mdv2011.0
+ Revision: 595983
- update to new version 43

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 42.0.0-1mdv2011.0
+ Revision: 576299
- update to 42

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 41.0.0-1mdv2011.0
+ Revision: 575427
- import perl-Perl-Critic-Pulp



