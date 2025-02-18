%global debug_package %{nil}

Name:           snx-rs
Version:        2.4.2
Release:        2
Summary:        Rust client for Checkpoint VPN tunnels

License:        AGPL-3.0

URL:            https://github.com/ancwrd1/snx-rs
Source:         https://github.com/ancwrd1/snx-rs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
%if 0%{?fedora}
BuildRequires:  rust-rpm-macros
%else
BuildRequires:  rust-toolset
%endif

%global _description %{expand:
Rust client for Checkpoint VPN tunnels.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version}

%build
%cargo_build

%install
%cargo_install

%files
%{_bindir}/snx-rs

%changelog
* Fri Oct 18 2024 Daniele Branchini <dbranchini@arpae.it> - 2.4.2-2
- Adapted specfile for epel8

* Mon Oct 14 2024 Daniele Branchini <dbranchini@arpae.it> - 2.4.2-1
- Initial build
