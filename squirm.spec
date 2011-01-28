Summary:	Squirm - A Squid Web Cache Redirector
Summary(pl.UTF-8):	Squirm - przekierowywacz dla Squida
Name:		squirm
Version:	1.26
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://squirm.foote.com.au/%{name}-%{version}.tgz
# Source0-md5:	54ac1d208620ec1e4419f97315d38848
Patch0:		%{name}-Makefile-paths.patch
URL:		http://squirm.foote.com.au/
Requires:	squid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Squirm jest szybkim i konfigurowalnym narzędziem do przekierowywania
dla Squida (serwera proxy-cache). Wymaga biblioteki GNU Regex
(dołączonej do źródeł) oraz oczywiście działającego Squida.

Ma następujące możliwości:
- bardzo duża szybkość
- prawie zerowe zużycie pamięci
- możliwość ponownego przeczytania konfiguracji w trakcie działania
  przez wysłanie SIGHUP
- interaktywny tryb testowy do sprawdzania nowych konfiguracji
- pełne dopasowywanie i podstawianie z użyciem wyrażeń regularnych
- pliki konfiguracyjne dla wzorców i adresów IP
- przy zepsutym pliku konfiguracyjnym Squirm działa w trybie Dodo, a
  Squid działa nadal.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -funroll-loops -DPREFIX=\\\"/\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install squirm			$RPM_BUILD_ROOT%{_bindir}
install	squirm.conf.dist	$RPM_BUILD_ROOT%{_sysconfdir}/squirm.conf
install	squirm.patterns.dist	$RPM_BUILD_ROOT%{_sysconfdir}/squirm.patterns

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_bindir}/*
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
