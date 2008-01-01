# TODO:
# - pl description and summary
Summary:	Fast 2d tank arcade game with multiplayer and split-screen modes
Name:		btanks
Version:	0.7.5800
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/btanks/%{name}-%{version}.tar.bz2
# Source0-md5:	538eadf2b78897620f3ef683a4ea423a
Source1:	%{name}.desktop
URL:		http://btanks.sourceforge.net/blog/langswitch_lang/en
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	expat-devel
BuildRequires:	libsigc++-devel
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	scons
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battle Tanks is a funny battle on your desk, where you can choose one
of three vehicles and eliminate your enemy using the whole arsenal of
weapons. It has original cartoon-like graphics and cool music, it is
fun and dynamic, it has several network modes for deathmatch and
cooperative - what else is needed to have fun with your friends?

And all is packed and ready for you in Battle Tanks.

%prep
%setup -q
# Proper name for our lua
sed -e 's/lua5.1/lua51/g' -i SConscript

%build
%scons \
    resources_dir=%{_datadir}/%{name} \
    lib_dir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install bt $RPM_BUILD_ROOT%{_bindir}/%{name}
install *.so $RPM_BUILD_ROOT%{_libdir}
install src/bt.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
cp -r data $RPM_BUILD_ROOT%{_datadir}/%{name}

# Game is looking for those libs in the datadir folder
ln -s %{_libdir}/libbt_objects.so $RPM_BUILD_ROOT%{_datadir}/%{name}/libbt_objects.so
ln -s %{_libdir}/libbt.so $RPM_BUILD_ROOT%{_datadir}/%{name}/libbt.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README-linux.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/*.so
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
