# AgentNEO Cumulative Stable Update Policy

Every stable AgentNEO updater must support a direct update from every declared supported baseline to the target release. A stable updater is built from the complete current updater-managed application payload, not only the delta from the immediately previous release.

## Required contract

1. Keep the backward-compatible `agentneo-update-v1` format unless the minimum supported client is intentionally raised.
2. Declare `cumulative`, `cumulative_from`, `minimum_supported_version`, and the complete tested baseline list.
3. Include every current updater-managed file required to converge an older supported installation to the target release.
4. Include delete actions for updater-managed files that existed in a supported baseline but no longer exist in the target release.
5. Never replace protected user/runtime state such as settings, permissions, credentials/API keys, model stores, memories, runtimes, workspaces, outputs, logs and user data.
6. Test the exact updater bytes with the real UpdateManager from every supported baseline.
7. Verify transactional apply, final current-file hashes, required deletions, version synchronization, and protected-state preservation for every baseline.
8. Stop publication if any supported baseline fails.
9. Upload the exact updater asset before promoting `latest.json`.
10. Download the published GitHub asset again and verify its SHA-256/ZIP/manifest before promoting the signed stable feed.

## v3.0.22 supported baseline

v3.0.22 retains v3.0.11 as the minimum supported cumulative baseline and was validated for direct upgrades from every release v3.0.11 through v3.0.21.
