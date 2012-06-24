Summary:	Squirm - A Squid Web Cache Redirector
Summary(pl):	Squirm - przekierowywacz dla Squida
Name:		squirm
Version:	1.23
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	http://squirm.foote.com.au/%{name}-%{version}.tgz
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

%description -l pl
Squirm jest szybkim i konfigurowalnym narz�dziem do przekierowywania
dla Squida (serwera proxy-cache). Wymaga biblioteki GNU Regex
(do��czonej do �r�de�) oraz oczywi�cie dzia�aj�cego Squida.

Ma nast�puj�ce mo�liwo�ci:
- bardzo du�a szybko��
- prawie zerowe zu�ycie pami�ci
- mo�liwo�� ponownego przeczytania konfiguracji w trakcie dzia�ania
  przez wys�anie SIGHUP
- interaktywny tryb testowy do sprawdzania nowych konfiguracji
- pe�ne dopasowywanie i podstawianie z u�yciem wyra�e� regularnych
- pliki konfiguracyjne dla wzorc�w i adres�w IP
- przy zepsutym pliku konfiguracyjnym Squirm dzia�a w trybie Dodo, a
  Squid dzia�a nadal.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -funroll-loops -DPREFIX=\\\"/\\\""

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install squirm			$RPM_BUILD_ROOT%{_bindir}
install	squirm.conf.dist	$RPM_BUILD_ROOT%{_sysconfdir}/squirm.conf
install	squirm.patterns.dist	$RPM_BUILD_ROOT%{_sysconfdir}/squirm.patterns


%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(640,root,squid) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
