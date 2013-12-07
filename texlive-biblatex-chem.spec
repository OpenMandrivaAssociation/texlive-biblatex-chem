# revision 31874
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-chem
# catalog-date 2013-10-09 23:41:19 +0200
# catalog-license lppl1.3
# catalog-version 1.1l
Name:		texlive-biblatex-chem
Version:	1.1l
Release:	4
Summary:	A set of biblatex implementations of chemistry-related bibliography styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-chem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chem.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle offers a set of styles to allow chemists to use
biblatex. The package has complete styles for: - all ACS
journals; - RSC journals using standard (Chem. Commun.) style;
and - Angewandte Chem. style, thus covering a wide range of
journals. A comprehensive set of examples of use is included.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-acs.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-acs.cbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-angew.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-angew.cbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-biochem.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-biochem.cbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-rsc.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-rsc.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/README
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-acs.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-acs.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-angew.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-angew.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-biochem.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-biochem.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-rsc.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-rsc.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
