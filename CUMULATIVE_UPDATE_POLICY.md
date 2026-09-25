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
11. Retire or generalize historical publisher workflows when a release line is superseded so an older workflow cannot overwrite the current stable feed.
12. Keep the private Ed25519 signing key off GitHub. Only the public verification key and signed feed metadata may be committed.

## Current release chain

### AgentNEO 3.0.25
- Formal baseline: `3.0.24`
- Published asset: `AgentNEO.3.0.25.zip`
- SHA-256: `07b7f35f2143712943796a383e5d0c388b810683cfa0b0332449ce8b59bf087d`

### AgentNEO 3.0.26
- Formal baseline: `3.0.25`
- Published asset: `AgentNEO.3.0.26.zip`
- SHA-256: `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6`

### AgentNEO 3.0.27
- Formal baseline: `3.0.26`
- Published asset: `AgentNEO.3.0.27.zip`
- SHA-256: `2aff9fbc19105254ffab49412466acd33d25b42046ab02fb478612422da68df7`
- Real 3.0.26 UpdateManager transaction: PASS.
- Final updater-managed payload hashes: 0 mismatches.

### AgentNEO 3.0.28
- Formal baseline: `3.0.27`
- Published asset: `AgentNEO_v3.0.28_Update_from_v3.0.27.zip`
- SHA-256: `d28bbf63a078d9a9d7bbe4336422928b56f504a19b9c0eef439859164e445caf`
- Real 3.0.27 UpdateManager transaction: PASS.
- Final updater-managed payload hashes: 0 mismatches.

### AgentNEO 3.0.29
- Formal baseline: `3.0.28`
- Published asset: `AgentNEO_v3.0.29_Update_from_v3.0.28.zip`
- SHA-256: `75336210afa6f639e7a2b8b4202c027353873ece40282c72d98e63a291647c69`
- Real 3.0.28 UpdateManager transaction: PASS.
- Additional direct compatibility verification from real 3.0.27 baseline: PASS.
- Additional direct compatibility verification from real 3.0.26 baseline: PASS.
- Final updater-managed payload hashes from all three tested baselines: 0 mismatches.
- The package manifest remains authoritative and formally declares 3.0.28.

The signed stable feed currently points to AgentNEO 3.0.29.
