%global debug_package %{nil}

Name:           snx-rs
Version:        2.4.2
Release:        2
Summary:        Rust client for Checkpoint VPN tunnels

License:        AGPL-3.0

URL:            https://github.com/ancwrd1/snx-rs
Source:         https://github.com/ancwrd1/snx-rs/releases/download/v2.4.2/snx-rs-v%{version}-linux-x86_64.tar.xz


%global _description %{expand:
Rust client for Checkpoint VPN tunnels.}

%description %{_description}

%prep
%autosetup -n snx-rs-v%{version}-linux-x86_64

%build

%install
install -D -m 0751 snx-rs %{buildroot}%{_bindir}/snx-rs

%files
%{_bindir}/snx-rs

%changelog
* Fri Oct 18 2024 Daniele Branchini <dbranchini@arpae.it> - 2.4.2-2
- Adapted specfile for epel8

* Mon Oct 14 2024 Daniele Branchini <dbranchini@arpae.it> - 2.4.2-1
- Initial build
