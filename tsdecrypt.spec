Summary:	MPEG transport stream decryption
Name:		tsdecrypt
Version:	3.0
Release:	6
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://georgi.unixsol.org/programs/tsdecrypt/%{name}-%{version}.tar.bz2
# Source0-md5:	2a04c257306fc769ce0131391af69766
Patch0:		make.patch
URL:		http://georgi.unixsol.org/programs/tsdecrypt/
BuildRequires:	libdvbcsa-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tsdecrypt reads incoming mpeg transport stream over UDP/RTP and then
decrypts it using libdvbcsa and keys obtained from OSCAM or similar
CAM server. tsdecrypt communicates with CAM server using camd35 over
TCP protocol also known as cs378x.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	INSTALL_DOC_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
