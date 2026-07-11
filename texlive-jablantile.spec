%global tl_name jablantile
%global tl_revision 16364

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Metafont version of tiles in the style of Slavik Jablan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/jablantile
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jablantile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jablantile.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a small Metafont font to implement the modular tiles described
by Slavik Jablan. For an outline of the theoretical structure of the
tiles, see (for example) Jablan's JMM 2006 Exhibit.

