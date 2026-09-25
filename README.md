# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and signed update metadata.

## Current stable release

- Version: `3.0.29`
- In-app updater asset: `AgentNEO_v3.0.29_Update_from_v3.0.28.zip`
- SHA-256: `75336210afa6f639e7a2b8b4202c027353873ece40282c72d98e63a291647c69`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.29.md`
- Formal package baseline: `3.0.28`

AgentNEO 3.0.29 isolates the optional ComfyUI portable CUDA/cuDNN runtime from AgentNEO's Faster-Whisper CUDA DLL paths and adds targeted one-click CUDA/cuDNN recovery with an embedded-PyTorch GPU self-test.

The exact published 3.0.29 updater was revalidated from the formal 3.0.28 baseline and additionally exercised directly against real 3.0.26 and 3.0.27 baselines. All three converged to 3.0.29 with zero updater-managed payload hash mismatches. The package manifest remains authoritative and formally declares 3.0.28.

## Recent update chain

### 3.0.25
- Updater asset: `AgentNEO.3.0.25.zip`
- SHA-256: `07b7f35f2143712943796a383e5d0c388b810683cfa0b0332449ce8b59bf087d`
- Formal baseline: `3.0.24`

### 3.0.26
- Updater asset: `AgentNEO.3.0.26.zip`
- SHA-256: `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6`
- Formal baseline: `3.0.25`

### 3.0.27
- Updater asset: `AgentNEO.3.0.27.zip`
- SHA-256: `2aff9fbc19105254ffab49412466acd33d25b42046ab02fb478612422da68df7`
- Formal baseline: `3.0.26`
- Revalidated with the real 3.0.26 UpdateManager: PASS.

### 3.0.28
- Updater asset: `AgentNEO_v3.0.28_Update_from_v3.0.27.zip`
- SHA-256: `d28bbf63a078d9a9d7bbe4336422928b56f504a19b9c0eef439859164e445caf`
- Formal baseline: `3.0.27`
- Revalidated with the real 3.0.27 UpdateManager: PASS.

### 3.0.29
- Updater asset: `AgentNEO_v3.0.29_Update_from_v3.0.28.zip`
- SHA-256: `75336210afa6f639e7a2b8b4202c027353873ece40282c72d98e63a291647c69`
- Formal baseline: `3.0.28`
- Real 3.0.28 UpdateManager transaction: PASS.
- Additional direct compatibility verification from real 3.0.26 and 3.0.27 baselines: PASS.

Clients verify the exact updater SHA-256 and Ed25519 publisher signature before installation. The repository public verification key remains unchanged. Historical publisher workflows must not overwrite the current stable feed.
