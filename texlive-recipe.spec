# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/recipe
# catalog-date 2008-09-11 15:08:12 +0200
# catalog-license pd
# catalog-version 0.9
Name:		texlive-recipe
Version:	0.9
Release:	2
Summary:	A LaTeX class to typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/recipe
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The layout design is relative straightforward (and traditional:
see 'sample output' under 'documentation'); the class needs
access to Bookman, and to BrushScript-Italic fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/recipe/recipe.cls
%doc %{_texmfdistdir}/doc/latex/recipe/README
%doc %{_texmfdistdir}/doc/latex/recipe/sample.pdf
%doc %{_texmfdistdir}/doc/latex/recipe/sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
