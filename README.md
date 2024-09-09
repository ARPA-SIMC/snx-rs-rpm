# RPM packaging files for snx-rs

This GitHub repository is meant to host (unofficial) convenience files for RPM
packaging and vendored dependencies.

See https://github.com/ancwrd1/snx-rs.

## How to release a new version

1. Create the vendor tarball

```
$ git clone https://github.com/ancwrd1/snx-rs
$ cd snx-rs
$ git checkout ${version}
$ cargo vendor
$ tar cvvf snx-rs-${version}-${release}-vendor.tar.gz vendor
```

2. Update version and/or RPM release in `snx-rs.spec`
3. Create a new GitHub release `v${version}-${release}`
4. Upload the tarball as a GitHub release asset

## License

AGLP-3.0
