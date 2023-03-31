Name:		texlive-subtext
Version:	51273
Release:	2
Summary:	Easy text-style subscripts in math mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subtext
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subtext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subtext.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package gives easy access to text-style subscripts
in math mode by providing an optional argument to _. This is
implemented by using the \text{} command from the amstext
package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/subtext
%doc %{_texmfdistdir}/doc/latex/subtext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
