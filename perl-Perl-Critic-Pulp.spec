%define upstream_name    Perl-Critic-Pulp
%define upstream_version 41

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Don't use Foo:: style barewords
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::String)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(PPI)
BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Perl::Critic::Policy)
BuildRequires: perl(Perl::Critic::Utils)
BuildRequires: perl(Perl::Critic::Utils::PPI)
BuildRequires: perl(Perl::Critic::Violation)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f *.list
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


