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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers a set of styles to allow chemists to use BibLaTeX. The
package has complete styles for: all ACS journals; RSC journals using
standard (Chem. Commun.) style; and Angewandte Chem. style, (thus
covering a wide range of journals). A comprehensive set of examples of
use is included.

