Name:		texlive-pgfmorepages
Version:	54770
Release:	2
Summary:	Assemble multiple logical pages onto a physical page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfmorepages
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmorepages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmorepages.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package replaces and extends the pgfpages sub-package of
the PGF system. It provides the capability to arrange multiple
"logical" pages on multiple "physical" pages, for example as
for arranging pages to make booklets.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pgfmorepages
%doc %{_texmfdistdir}/doc/latex/pgfmorepages

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
