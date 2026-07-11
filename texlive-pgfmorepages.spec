%global tl_name pgfmorepages
%global tl_revision 54770

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.20
Release:	%{tl_revision}.1
Summary:	Assemble multiple logical pages onto a physical page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgfmorepages
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmorepages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmorepages.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package replaces and extends the pgfpages sub-package of the PGF
system. It provides the capability to arrange multiple "logical" pages
on multiple "physical" pages, for example as for arranging pages to make
booklets.

