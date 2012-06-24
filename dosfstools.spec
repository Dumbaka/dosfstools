Summary:	Utilities to create and check MS-DOS FAT filesystems.
Name:		dosfstools
Version:	2.2
Release:	9
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools/%{name}-%{version}.src.tar.gz
Patch0:		%{name}-llseek.patch
Patch1:		%{name}-288.patch
Patch2:		%{name}-linux24.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mkdosfs-ygg

%define		_sbindir	/sbin

%description
Inside of this package there are two utilities to create and to check
MS-DOS FAT filesystems on either harddisks or floppies under Linux.
This version uses the enhanced boot sector/superblock format of DOS
3.3+ as well as provides a default dummy boot sector code.

%description -l pl
W pakiecie znajduj� si� dwa narz�dzia s�u��ce do tworzenia i
sprawdzania system�w plik�w FAT na dyskach twardych lub dyskietkach
pod Linuksem. Wersja ta u�ywa ulepszonego formatu sektora
uruchomieniowego/superbloku u�ywanego w DOS-ie 3.3 i nowszych oraz
obs�uguje pusty kod sektora uruchomieniowego.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	OPTFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
cp dosfsck/README README.fsck
cp mkdosfs/README README.mkdosfs

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/*.{msdos,vfat}.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.msdos.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.vfat.8
echo ".so mkdosf.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.msdos.8
echo ".so mkdosf.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.vfat.8

gzip -9nf CHANGES TODO README.fsck README.mkdosfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
