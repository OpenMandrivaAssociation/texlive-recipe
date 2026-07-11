%global tl_name recipe
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	A LaTeX class to typeset recipes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/recipe
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The layout design is relatively straightforward (and traditional: see
'sample output' under 'documentation'); the class uses the Bookman and
the BrushScript-Italic fonts.

