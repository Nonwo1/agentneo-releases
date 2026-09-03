# AgentNEO Stable Update Policy

Every stable AgentNEO updater must be published only after the exact release asset is hash-verified and tested with the real UpdateManager from every baseline that the package declares as supported.

## Required contract

1. Keep the backward-compatible `agentneo-update-v1` format unless the minimum supported client is intentionally raised.
2. Declare the intended baseline contract in the package manifest (`minimum_supported_version`, tested baselines and cumulative metadata when applicable).
3. Include every updater-managed file required to converge a supported installation to the target release.
4. Include delete actions for updater-managed files that existed in a supported baseline but no longer exist in the target release.
5. Never replace protected user/runtime state such as settings, permissions, credentials/API keys, model stores, memories, runtimes, workspaces, outputs, logs and user data.
6. Test the exact updater bytes with the actual UpdateManager from each declared supported baseline.
7. Verify transactional apply, final target hashes, required deletions, version synchronization and protected-state preservation.
8. Stop publication if a declared baseline fails.
9. Upload the exact updater asset before promoting `latest.json`.
10. Verify the GitHub-published asset digest/ZIP/manifest before promoting the signed stable feed.
11. Retire historical publisher workflows when a release line is superseded so an older workflow cannot overwrite the current stable feed.

## Current release chain

### AgentNEO 3.0.25

- Formal baseline: `3.0.24`
- Published asset: `AgentNEO.3.0.25.zip`
- SHA-256: `07b7f35f2143712943796a383e5d0c388b810683cfa0b0332449ce8b59bf087d`
- Real 3.0.24 UpdateManager transaction: PASS

### AgentNEO 3.0.26

- Formal package baseline: `3.0.25`
- Published asset: `AgentNEO.3.0.26.zip`
- SHA-256: `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6`
- Real 3.0.25 UpdateManager transaction: PASS
- Additional direct compatibility verification of the exact published updater with real 3.0.22, 3.0.23 and 3.0.24 UpdateManagers: PASS. The package manifest remains authoritative and formally declares 3.0.25 as the supported baseline.

The stable feed currently points to AgentNEO 3.0.26.
