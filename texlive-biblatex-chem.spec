Name:		texlive-biblatex-chem
Version:	1.1u
Release:	1
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
%{_texmfdistdir}/tex/latex/biblatex-chem
%doc %{_texmfdistdir}/doc/latex/biblatex-chem

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
