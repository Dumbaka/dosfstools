Summary:	Utilities to create and check MS-DOS FAT filesystems
Summary(es.UTF-8):	Un programa que crea sistemas de archivo de MS-DOS (FAT) en Linux
Summary(pl.UTF-8):	Narzędzia do tworzenia i sprawdzania systemów plikowych MS-DOS FAT
Summary(pt_BR.UTF-8):	Um programa que cria sistemas de arquivo do MS-DOS (FAT) no Linux
Name:		dosfstools
Version:	3.0.22
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://www.daniel-baumann.ch/files/software/dosfstools/%{name}-%{version}.tar.xz
# Source0-md5:	301f01ca8a734011c0257134bcf475c8
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-pl-man-pages.tar.bz2
# Source1-md5:	28913ed142dac33624b14ce1e1ce8803
URL:		http://www.daniel-baumann.ch/software/dosfstools/
BuildRequires:	rpmbuild(macros) >= 1.402
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	mkdosfs-ygg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Inside of this package there are two utilities to create and to check
MS-DOS FAT filesystems on either harddisks or floppies under Linux.
This version uses the enhanced boot sector/superblock format of DOS
3.3+ as well as provides a default dummy boot sector code.

%description -l es.UTF-8
El programa mkdosfs se usa para crear un sistema de archivos FAT
(MS-DOS) a partir de Linux.

Si su computador necesita usar sistemas de archivo MS-DOS usted debe
instalar el paquete dosfstools.

%description -l pl.UTF-8
W pakiecie znajdują się dwa narzędzia służące do tworzenia i
sprawdzania systemów plików FAT na dyskach twardych lub dyskietkach
pod Linuksem. Wersja ta używa ulepszonego formatu sektora
uruchomieniowego/superbloku używanego w DOS-ie 3.3 i nowszych oraz
obsługuje pusty kod sektora uruchomieniowego.

%description -l pt_BR.UTF-8
O programa mkdosfs é usado para criar um sistema de arquivos FAT
(MS-DOS) a partir do Linux.

O pacote dosfstools deve ser instalado se sua máquina precisa usar
sistemas de arquivo MS-DOS.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install-bin install-man install-symlinks \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	SBINDIR=/sbin \
	MANDIR=%{_mandir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*
%attr(755,root,root) %{_sbindir}/dosfsck
%attr(755,root,root) %{_sbindir}/dosfslabel
%attr(755,root,root) %{_sbindir}/fatlabel
%attr(755,root,root) %{_sbindir}/fsck.fat
%attr(755,root,root) %{_sbindir}/fsck.msdos
%attr(755,root,root) %{_sbindir}/fsck.vfat
%attr(755,root,root) %{_sbindir}/mkdosfs
%attr(755,root,root) %{_sbindir}/mkfs.fat
%attr(755,root,root) %{_sbindir}/mkfs.msdos
%attr(755,root,root) %{_sbindir}/mkfs.vfat
%{_mandir}/man8/dosfsck.8*
%{_mandir}/man8/dosfslabel.8*
%{_mandir}/man8/fatlabel.8*
%{_mandir}/man8/fsck.fat.8*
%{_mandir}/man8/fsck.msdos.8*
%{_mandir}/man8/fsck.vfat.8*
%{_mandir}/man8/mkdosfs.8*
%{_mandir}/man8/mkfs.fat.8*
%{_mandir}/man8/mkfs.msdos.8*
%{_mandir}/man8/mkfs.vfat.8*
%lang(de) %{_mandir}/de/man8/*
%lang(pl) %{_mandir}/pl/man8/*
