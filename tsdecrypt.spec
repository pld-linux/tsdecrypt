Summary:	MPEG transport stream decryption
Summary(pl.UTF-8):	Odszyfrowywanie strumienia transportowego MPEG
Name:		tsdecrypt
Version:	10.0
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	https://georgi.unixsol.org/programs/tsdecrypt/%{name}-%{version}.tar.bz2
# Source0-md5:	a90391fce090e3e8075cd1f2dce1061b
Patch0:		make.patch
URL:		https://georgi.unixsol.org/programs/tsdecrypt/
BuildRequires:	libdvbcsa-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tsdecrypt reads incoming MPEG transport stream over UDP/RTP and then
decrypts it using libdvbcsa and keys obtained from OSCAM or similar
CAM server. tsdecrypt communicates with CAM server using camd35 over
TCP protocol also known as cs378x.

%description -l pl.UTF-8
tsdecrypt czyta przychodzący strumień transportowy MPEG po UDP/RTP, a
następnie odszyfrowuje go z użyciem libdvbcsa i kluczy uzyskanych z
OSCAM lub podobnego CAM. Komunikuje się z serwerem CAM przy użyciu
protokołu cam36 po TCP, znanego także jako cs378x.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	Q=

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
%attr(755,root,root) %{_bindir}/tsdecrypt
%{_mandir}/man1/tsdecrypt.1*
