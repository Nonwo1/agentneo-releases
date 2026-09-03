# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and signed update metadata.

## Current stable release

- Version: `3.0.26`
- In-app updater asset: `AgentNEO.3.0.26.zip`
- SHA-256: `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.26.md`
- Formal package baseline: `3.0.25`

AgentNEO 3.0.26 repairs Resource Governor fairness and diagnostic scheduling while preserving the working 3.0.25 GPT-OSS, Ollama endpoint and CUDA speech-runtime fixes.

## Recent update chain

### 3.0.25

- Updater asset: `AgentNEO.3.0.25.zip`
- SHA-256: `07b7f35f2143712943796a383e5d0c388b810683cfa0b0332449ce8b59bf087d`
- Validated baseline: `3.0.24`

### 3.0.26

- Updater asset: `AgentNEO.3.0.26.zip`
- SHA-256: `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6`
- Formal validated baseline: `3.0.25`
- Additional direct compatibility verification with the exact published updater also passed using the real `3.0.22`, `3.0.23` and `3.0.24` UpdateManagers. The package manifest remains authoritative and formally declares `3.0.25`.

Clients verify the exact updater SHA-256 and Ed25519 publisher signature before installation. Historical version-specific publisher workflows have been retired so an older release cannot overwrite the current stable feed.
