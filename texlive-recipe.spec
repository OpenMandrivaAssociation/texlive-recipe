# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/recipe
# catalog-date 2008-09-11 15:08:12 +0200
# catalog-license pd
# catalog-version 0.9
Name:		texlive-recipe
Version:	0.9
Release:	1
Summary:	A LaTeX class to typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/recipe
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The layout design is relative straightforward (and traditional:
see 'sample output' under 'documentation'); the class needs
access to Bookman, and to BrushScript-Italic fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
