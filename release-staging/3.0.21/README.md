# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current stable release

- Version: `3.0.21`
- In-app updater: `AgentNEO_v3.0.21_Update.zip`
- Update type: **cumulative**
- Supported direct upgrade baselines for v3.0.21: `3.0.11` through `3.0.20`
- SHA-256: `90d1fcb01b56482a928b1eac8485a37e3af604e111428cfdf8473d23926be65b`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.21.md`

## Sandbox protocol

v3.0.21 changes Automatic Safe isolation to task-scoped, capability-based routing. Ordinary conversation, planning and read-only AgentNEO diagnostics do not open Windows Sandbox. Generated or untrusted execution and file-processing that genuinely requires isolation use an ephemeral task-scoped sandbox. New isolated tasks are offline by default, user prohibitions are enforced at the tool-dispatch layer, and required isolated execution never silently falls back to the host.

## Cumulative update policy

Stable AgentNEO updater packages must be cumulative across all supported upgrade baselines. A stable updater must contain the complete current updater-managed application state needed to converge a supported older installation directly to the target release; it must not assume that the user is running the immediately previous version.

Before publication, the exact updater ZIP must be tested against every supported baseline using that baseline's real UpdateManager. Validation must cover package inspection, transactional apply, replacement hashes, required deletions/migrations, final version synchronization and preservation of protected user/runtime data.

Protected user-owned data is not replaced by the cumulative application payload unless a specific versioned migration explicitly requires it. This includes user settings, permissions, credentials/API keys, local models, memories, runtimes, workspaces and outputs.

For v3.0.21, direct upgrade validation passed for v3.0.11 through v3.0.20.

## Release naming

- `AgentNEO_vX.Y.Z_Full_Installer.exe` — full Windows installer when published
- `AgentNEO_vX.Y.Z_Update.zip` — cumulative application update package
- `SHA256SUMS.txt` — hashes for the currently published release assets
- `latest.json` — signed automatic-update metadata
- `public-key-v1.txt` — public update-verification key
- `release-notes/vX.Y.Z.md` — release notes for each published version

## GitHub tag convention

AgentNEO release tags in this repository use the numeric form `X.Y.Z` (for example `3.0.21`). The visible release title may be `vX.Y.Z`, but the download URL in `latest.json` must use the exact GitHub tag text.

## Publishing an update

1. Build the target version from the complete updater-managed application payload.
2. Validate the exact package against every supported older baseline.
3. Create the GitHub release using tag `X.Y.Z`.
4. Upload the exact `AgentNEO_vX.Y.Z_Update.zip` without modifying, renaming or recompressing it.
5. Download the published asset and verify its SHA-256 and ZIP integrity.
6. Publish `SHA256SUMS.txt`, release notes and the signed `latest.json` only after the asset verifies.
7. AgentNEO clients verify both SHA-256 and the Ed25519 publisher signature before installation.

Copyright © 2026 AgentNEO owner. All rights reserved. Third-party components remain subject to their respective licence terms.
