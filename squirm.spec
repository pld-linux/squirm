Summary:	Squirm - A Squid Web Cache Redirector
Name:		squirm
Version:	1.23
Release:	1
Source0:	http://squirm.foote.com.au/%{name}-%{version}.tgz
Patch0:		%{name}-Makefile-paths.patch
License:	GPL
URL:		http://squirm.foote.com.au/
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	squid

%define		_sysconfdir /etc/squid

%description
Squirm is a fast & configurable redirector for the Squid Internet
Object Cache. It requires the GNU Regex Library (now included in the
Squirm source), and of course, a working Squid. It is available free
under the terms of the GNU GPL.

Squirm has the following features:

- Very, very fast
- Virtually no memory usage
- It can re-read it's config files while running by sending it a HUP
  signal
- Interactive test mode for checking new configs
- Full regular expression matching and replacement
- Config files for patterns and IP addresses.
- If you mess up the config file, Squirm runs in Dodo Mode so your
  squid keeps working :-)

%prep
%setup -q
%patch0 -p1
%build
%{__make} CFLAGS="%{rpmcflags} -funroll-loops -DPREFIX=\\\"/var/log/squid\\\"" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install squirm			$RPM_BUILD_ROOT%{_bindir}
install	squirm.conf.dist	$RPM_BUILD_ROOT%{_sysconfdir}/squirm.conf
install	squirm.patterns.dist	$RPM_BUILD_ROOT%{_sysconfdir}/squirm.patterns

gzip -9nf README

%files
%doc *.gz
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(640,root,squid) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*

%clean
rm -rf $RPM_BUILD_ROOT
