Name:		texlive-recipe
Version:	54080
Release:	2
Summary:	A LaTeX class to typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/recipe
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipe.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
