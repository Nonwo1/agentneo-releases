# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current stable release

- Version: `3.0.20`
- In-app updater: `AgentNEO_v3.0.20_Update.zip`
- Update type: **cumulative**
- Supported direct upgrade baselines for v3.0.20: `3.0.11` through `3.0.19`
- SHA-256: `9bca8d2d2f301ba98fb506998d3da9b5fe7842f4bb1dfabea75b64ffdbd7a0c8`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.20.md`

## Cumulative update policy

Stable AgentNEO updater packages must be cumulative across all supported upgrade baselines. A stable updater must contain the complete current updater-managed application state needed to converge a supported older installation directly to the target release; it must not assume that the user is running the immediately previous version.

Before publication, the exact updater ZIP must be tested against every supported baseline using that baseline's real UpdateManager. Validation must cover package inspection, transactional apply, replacement hashes, required deletions/migrations, final version synchronization and preservation of protected user/runtime data.

Protected user-owned data is not replaced by the cumulative application payload unless a specific versioned migration explicitly requires it. This includes user settings, permissions, credentials/API keys, local models, memories, runtimes, workspaces and outputs.

For v3.0.20, direct upgrade validation passed for v3.0.11, v3.0.12, v3.0.13, v3.0.14, v3.0.15, v3.0.16, v3.0.17, v3.0.18 and v3.0.19.

## Release naming

- `AgentNEO_vX.Y.Z.exe` — full Windows installer when published
- `AgentNEO_vX.Y.Z_Update.zip` — cumulative application update package
- `SHA256SUMS.txt` — hashes for the currently published release assets
- `latest.json` — signed automatic-update metadata
- `public-key-v1.txt` — public update-verification key
- `release-notes/vX.Y.Z.md` — release notes for each published version

## GitHub tag convention

AgentNEO release tags in this repository use the numeric form `X.Y.Z` (for example `3.0.20`). The visible release title may be `vX.Y.Z`, but the download URL in `latest.json` must use the exact GitHub tag text. A mismatch such as `v3.0.20` in the URL when the actual tag is `3.0.20` will return HTTP 404.

## Publishing an update

1. Build the target version from the complete updater-managed application payload, not only the immediately previous release delta.
2. Validate the exact package against every supported older baseline.
3. Create the GitHub release using tag `X.Y.Z`.
4. Upload the exact `AgentNEO_vX.Y.Z_Update.zip` without modifying, renaming or recompressing it.
5. Verify its SHA-256.
6. Update `SHA256SUMS.txt`.
7. Generate and sign `latest.json` with a `package_url` that uses the exact release tag and exact asset filename.
8. Publish `latest.json` only after the release asset is available.

AgentNEO clients verify the expected SHA-256 and Ed25519 publisher signature before installing an online update.

Copyright © 2026 AgentNEO owner. All rights reserved. Third-party components remain subject to their respective licence terms.
