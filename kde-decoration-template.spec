%define		_decoration 	
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0.8
Release:	1
License:	GPL
Group:		Themes
Source0:	%{_decoration}-%{version}.tar.gz
# Source0-md5:	
URL:		
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	qt-devel >= 3.0.5
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_decoration} is an 

%description -l pl
%{_decoration} to 

%prep
%setup -q -n %{_decoration}-%{version}

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop
