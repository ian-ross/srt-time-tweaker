# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Updated file reading and writing to use UTF-8 encoding to ensure proper handling of non-ASCII characters in .srt files.

## [1.0.0] - 2025-06-6

### Added

- Shift subtitle timestamps by specified hours, minutes, seconds, and milliseconds.
- Accept delay as a single string in `HH:MM:SS,ms` format.
- Supports adding or subtracting delay to/from timestamps.
- Handles negative timing errors with an option to ignore or raise exceptions.
- Usable both as a command-line tool and as a Python importable function.

[unreleased]: https://github.com/BhagyaJyoti22006/srt-time-tweaker/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/BhagyaJyoti22006/srt-time-tweaker/releases/tag/v1.0.0