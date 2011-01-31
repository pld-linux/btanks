Summary:	Fast 2D tank arcade game with multiplayer and split-screen modes
Summary(pl.UTF-8):	Szybka gra zręcznościowa z czołgami, trybem dla wielu graczy i podzielonym ekranem
Name:		btanks
Version:	0.9.8083
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/btanks/%{name}-%{version}.tar.bz2
# Source0-md5:	49cb95c0eec47d3436c4fdf65e7c9d12
Source1:	%{name}.desktop
URL:		http://btanks.sourceforge.net/blog/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	expat-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRequires:	smpeg-devel
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battle Tanks is a funny battle on your desk, where you can choose one
of three vehicles and eliminate your enemy using the whole arsenal of
weapons. It has original cartoon-like graphics and cool music, it is
fun and dynamic, it has several network modes for deathmatch and
cooperative - what else is needed to have fun with your friends?

And all is packed and ready for you in Battle Tanks.

%description -l pl.UTF-8
Battle Tanks to zabawna gra, w której można wybrać jeden z trzech
pojazdów i eliminować wrogów przy użyciu całego arsenału broni. Ma
oryginalną grafikę w stylu kreskówek i świetną muzykę; jest zabawna i
dynamiczna, ma kilka trybów sieciowych, pozwalających na grę przeciwko
wszystkim oraz współpracę - cóż więcej potrzeba do zabawy z kolegami?

%prep
%setup -q
# Proper name for our lua
%{__sed} -e 's/lua5.1/lua51/g' -i engine/SConscript

%build
export CXXFLAGS="%{rpmcxxflags} -I/usr/include/SDL"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export CC="%{__cc}"
%scons \
	resources_dir=%{_datadir}/%{name} \
	plugins_dir=%{_libdir}/%{name} \
	lib_dir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a build/release/engine/btanks $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a build/release/editor/bted $RPM_BUILD_ROOT%{_bindir}/bted
cp -a build/release/engine/libbtanks_engine.so $RPM_BUILD_ROOT%{_libdir}
cp -a build/release/mrt/libmrt.so $RPM_BUILD_ROOT%{_libdir}
cp -a build/release/sdlx/libsdlx.so $RPM_BUILD_ROOT%{_libdir}
cp -a build/release/clunk/libclunk.so $RPM_BUILD_ROOT%{_libdir}
cp -a build/release/objects/libbt_objects.so $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a engine/src/bt.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README-*.txt
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/bted
%attr(755,root,root) %{_libdir}/libbtanks_engine.so
%attr(755,root,root) %{_libdir}/libmrt.so
%attr(755,root,root) %{_libdir}/libsdlx.so
%attr(755,root,root) %{_libdir}/libclunk.so
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libbt_objects.so
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
