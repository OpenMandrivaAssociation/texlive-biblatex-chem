%global tl_name biblatex-chem
%global tl_revision 76236

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	A set of BibLaTeX implementations of chemistry-related bibliography styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-chem
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers a set of styles to allow chemists to use BibLaTeX. The
package has complete styles for: all ACS journals; RSC journals using
standard (Chem. Commun.) style; and Angewandte Chem. style, (thus
covering a wide range of journals). A comprehensive set of examples of
use is included.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-chem
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-chem
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-acs.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-acs.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-angew.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-angew.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-biochem.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-biochem.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-rsc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem-rsc.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chem/biblatex-chem.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-acs.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-acs.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-angew.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-angew.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-biochem.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-biochem.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-rsc.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chem/chem-rsc.cbx
