Name:		texlive-biblatex-chem
Version:	1.1e
Release:	1
Summary:	Chemistry styles for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-chem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chem.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle offers a set of styles to allow chemists to use
biblatex. The package has complete styles for: - all ACS
journals; - RSC journals using standard (Chem. Commun.) style;
and - Angewandte Chem. style, thus covering a wide range of
journals. A comprehensive set of examples of use is included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
