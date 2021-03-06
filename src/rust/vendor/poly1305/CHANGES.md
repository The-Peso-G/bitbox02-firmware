# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.5.2 (2019-11-14)
### Changed
- Upgrade to `zeroize` 1.0 ([#33])

[#33]: https://github.com/RustCrypto/universal-hashes/pull/33

## 0.5.1 (2019-10-04)
### Added
- Link to `chacha20poly1305` and `xsalsa20poly1305` crates from README.md ([#26])

[#26]: https://github.com/RustCrypto/universal-hashes/pull/26

## 0.5.0 (2019-10-04)
### Changed
- Upgrade to `universal-hash` crate v0.3 ([#22])

[#22]: https://github.com/RustCrypto/universal-hashes/pull/22

## 0.4.1 (2019-10-01)
### Changed
- Upgrade to `zeroize` v1.0.0-pre ([#19])

[#19]: https://github.com/RustCrypto/universal-hashes/pull/19

## 0.4.0 (2019-09-29)
### Changed
- Update to Rust 2018 edition ([#3])
- Use `UniversalHash` trait ([#5])

[#3]: https://github.com/RustCrypto/universal-hashes/pull/3
[#5]: https://github.com/RustCrypto/universal-hashes/pull/5

## 0.3.0 (2019-08-26)
### Changed
- Switch from `MacResult` to built-in `Tag` type ([RustCrypto/MACs#13])

[RustCrypto/MACs#13]: https://github.com/RustCrypto/MACs/pull/13

## 0.2.0 (2019-08-19)
### Added
- `Poly1305::input_padded()` ([#16])

### Changed
- Change output to be a `MacResult` ([RustCrypto/MACs#16])

[RustCrypto/MACs#16]: https://github.com/RustCrypto/MACs/pull/16

## 0.1.0 (2019-08-15)

- Initial release
