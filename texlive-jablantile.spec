Name:		texlive-jablantile
Version:	16364
Release:	2
Summary:	Metafont version of tiles in the style of Slavik Jablan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/jablantile
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jablantile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jablantile.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a small Metafont font to implement the modular tiles
described by Slavik Jablan. For an outline of the theoretical
structure of the tiles, see (for example) Jablan's JMM 2006
Exhibit.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/jablantile/jablantile.mf
%doc %{_texmfdistdir}/doc/fonts/jablantile/README
%doc %{_texmfdistdir}/doc/fonts/jablantile/dearjablan.tex
%doc %{_texmfdistdir}/doc/fonts/jablantile/jablantile.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
