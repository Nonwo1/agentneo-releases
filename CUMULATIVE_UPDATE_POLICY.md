# AgentNEO Cumulative Update Policy

Every stable AgentNEO updater must support direct upgrades from every declared supported baseline to the target release. Stable updaters are built from the complete current updater-managed application payload rather than only the delta from the immediately previous version.

## Required release contract

1. The manifest declares the target version, that the package is cumulative, the minimum supported version, and the baseline versions tested.
2. The package contains all updater-managed files required to converge a supported older installation to the target release.
3. Required delete/migration actions from intermediate releases are carried forward where still applicable.
4. User-owned data remains protected unless an explicit versioned migration requires otherwise. Protected data includes settings, permissions, credentials/API keys, local models, memories, runtimes, workspaces, outputs and other user data.
5. Before publication, the exact release ZIP is tested with the real UpdateManager from every supported baseline.
6. Each baseline must pass package inspection, transactional apply, final file hashes, required deletions/migrations, protected-data preservation and final version synchronization.
7. Publication must stop if any supported baseline fails.
8. The release asset is uploaded before `latest.json` is changed. The published SHA-256 and Ed25519 signature must match the exact uploaded ZIP bytes.

## v3.0.21 support matrix

The cumulative v3.0.21 updater was validated for direct upgrades from:

- v3.0.11
- v3.0.12
- v3.0.13
- v3.0.14
- v3.0.15
- v3.0.16
- v3.0.17
- v3.0.18
- v3.0.19
- v3.0.20

All supported baselines above converge directly to v3.0.21 without installing intermediate releases individually.
