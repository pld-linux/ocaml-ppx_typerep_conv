#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Generation of runtime types from type declarations
Summary(pl.UTF-8):	Generowanie typów uruchomieniowych z deklaracji typów
Name:		ocaml-ppx_typerep_conv
Version:	0.14.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_typerep_conv/tags
Source0:	https://github.com/janestreet/ppx_typerep_conv/archive/v%{version}/ppx_typerep_conv-%{version}.tar.gz
# Source0-md5:	33ce6d705b7323772379712511daac0b
URL:		https://github.com/janestreet/ppx_typerep_conv
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.22.0
BuildRequires:	ocaml-typerep-devel >= 0.14
BuildRequires:	ocaml-typerep-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Automatic generation of runtime types from type definitions.

This package contains files needed to run bytecode executables using
ppx_typerep_conv library.

%description -l pl.UTF-8
Automatyczne generowanie typów uruchomieniowych z definicji typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_typerep_conv.

%package devel
Summary:	Generation of runtime types from type declarations - development part
Summary(pl.UTF-8):	Generowanie typów uruchomieniowych z deklaracji typów - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.22.0
Requires:	ocaml-typerep-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_typerep_conv library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_typerep_conv.

%prep
%setup -q -n ppx_typerep_conv-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_typerep_conv/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_typerep_conv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_typerep_conv
%{_libdir}/ocaml/ppx_typerep_conv/META
%{_libdir}/ocaml/ppx_typerep_conv/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_typerep_conv/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_typerep_conv/*.cmi
%{_libdir}/ocaml/ppx_typerep_conv/*.cmt
%{_libdir}/ocaml/ppx_typerep_conv/*.cmti
%{_libdir}/ocaml/ppx_typerep_conv/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_typerep_conv/ppx_typerep_conv.a
%{_libdir}/ocaml/ppx_typerep_conv/*.cmx
%{_libdir}/ocaml/ppx_typerep_conv/*.cmxa
%endif
%{_libdir}/ocaml/ppx_typerep_conv/dune-package
%{_libdir}/ocaml/ppx_typerep_conv/opam
