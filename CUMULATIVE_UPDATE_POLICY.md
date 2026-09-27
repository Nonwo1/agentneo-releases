# AgentNEO Stable Update Policy

Every stable AgentNEO updater must be published only after the exact release asset is hash-verified and tested with the real UpdateManager from every baseline that the package declares as supported.

## Required contract

1. Keep the backward-compatible `agentneo-update-v1` format unless the minimum supported client is intentionally raised.
2. Declare the intended baseline contract in the package manifest.
3. Include every updater-managed file required to converge a supported installation to the target release.
4. Include delete actions for updater-managed files that existed in a supported baseline but no longer exist in the target release.
5. Never replace protected user/runtime state such as settings, permissions, credentials/API keys, model stores, memories, runtimes, workspaces, outputs, logs and user data during Repair / Upgrade.
6. Test the exact updater bytes with the actual UpdateManager from each declared supported baseline.
7. Verify transactional apply, final target hashes, required deletions, version synchronization and protected-state preservation.
8. Stop publication if a declared baseline fails.
9. Upload the exact updater asset before promoting `latest.json`.
10. Verify the GitHub-published asset digest, ZIP and manifest before promoting the signed stable feed.
11. Keep the private Ed25519 signing key off GitHub. Only the public verification key and signed feed metadata may be committed.
12. For a release containing a Full Installer, perform a clean Windows Full Install smoke test and confirm the installed application launches before calling the installer validated.

## Current release chain

### AgentNEO 3.0.30
- Community Edition public-testing release.
- Formal baseline: `3.0.29`.
- Published updater: `AgentNEO_v3.0.30_Update.zip`.
- Updater SHA-256: `0905351ca96e3973594d0a6f62b53dbde552365f22e38f64bdf6ed2d7eaf2ee0`.
- Published installer SHA-256: `a8b4418cc0457eacf80bc07d95b7556655910c757e81fee7ae4fc5acd8be8748`.
- Published source SHA-256: `ec0d56a63d31ab7433723820811bb46d33a1fcb41af60123e8a71f4d67e9332a`.
- Real v3.0.29 → v3.0.30 Windows update: PASS.
- AgentNEO launch after update: PASS.
- Clean Windows Full Install into a new folder: PASS.
- Launch from newly created desktop shortcut: PASS.
- Updater-managed final hash mismatches: 0.

### AgentNEO 3.0.29
- Formal baseline: `3.0.28`.
- Published updater: `AgentNEO_v3.0.29_Update_from_v3.0.28.zip`.
- SHA-256: `75336210afa6f639e7a2b8b4202c027353873ece40282c72d98e63a291647c69`.
- Real 3.0.28 UpdateManager transaction: PASS.
- Additional direct compatibility verification from real 3.0.27 and 3.0.26 baselines: PASS.

### AgentNEO 3.0.28
- Formal baseline: `3.0.27`.
- SHA-256: `d28bbf63a078d9a9d7bbe4336422928b56f504a19b9c0eef439859164e445caf`.

### AgentNEO 3.0.27
- Formal baseline: `3.0.26`.
- SHA-256: `2aff9fbc19105254ffab49412466acd33d25b42046ab02fb478612422da68df7`.

### AgentNEO 3.0.26
- Formal baseline: `3.0.25`.
- SHA-256: `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6`.

The signed stable feed currently points to AgentNEO 3.0.30.
