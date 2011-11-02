Name:		texlive-jablantile
Version:	20091210
Release:	1
Summary:	Metafont version of tiles in the style of Slavik Jablan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/jablantile
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jablantile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jablantile.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a small Metafont font to implement the modular tiles
described by Slavik Jablan. For an outline of the theoretical
structure of the tiles, see (for example) Jablan's JMM 2006
Exhibit.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/jablantile/jablantile.mf
%doc %{_texmfdistdir}/doc/fonts/jablantile/README
%doc %{_texmfdistdir}/doc/fonts/jablantile/dearjablan.tex
%doc %{_texmfdistdir}/doc/fonts/jablantile/jablantile.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
