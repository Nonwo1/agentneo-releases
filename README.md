# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current stable release

- Version: `3.0.20`
- In-app updater: `AgentNEO_v3.0.20_Update.zip`
- SHA-256: `5ff87d9dc99e71ebb333855586960912305d28547b0c2f80296463dbcd4cbaaf`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.20.md`

## Release naming

- `AgentNEO_vX.Y.Z.exe` — full Windows installer when published
- `AgentNEO_vX.Y.Z_Update.zip` — selective application update package
- `SHA256SUMS.txt` — hashes for the currently published release assets
- `latest.json` — signed automatic-update metadata
- `public-key-v1.txt` — public update-verification key
- `release-notes/vX.Y.Z.md` — release notes for each published version

## GitHub tag convention

AgentNEO release tags in this repository use the numeric form `X.Y.Z` (for example `3.0.12`). The visible release title may be `vX.Y.Z`, but the download URL in `latest.json` must use the exact GitHub tag text. A mismatch such as `v3.0.12` in the URL when the actual tag is `3.0.12` will return HTTP 404.

## Publishing an update

1. Create the GitHub release using tag `X.Y.Z` (for example `3.0.13`).
2. Upload the exact `AgentNEO_vX.Y.Z_Update.zip` without modifying, renaming or recompressing it.
3. Verify its SHA-256.
4. Update `SHA256SUMS.txt`.
5. Generate and sign `latest.json` with a `package_url` that uses the exact release tag and exact asset filename.
6. Publish `latest.json` only after the release asset is available.

AgentNEO clients verify the expected SHA-256 and Ed25519 publisher signature before installing an online update.

Copyright © 2026 AgentNEO owner. All rights reserved. Third-party components remain subject to their respective licence terms.
