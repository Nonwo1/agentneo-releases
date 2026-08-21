# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current manual release

- Version: `3.0.23`
- Manual updater baseline: **v3.0.22 only**
- Release notes: `release-notes/v3.0.23.md`
- Validation: `release-staging/3.0.23/AgentNEO_v3.0.23_Validation.txt`
- Checksums: `release-staging/3.0.23/SHA256SUMS.txt`

v3.0.23 adds the non-bundled hybrid speech stack and revised model-aware detailed-agent diagnostics. It adds optional Vosk live partial STT, optional Kokoro local TTS, improved barge-in handling, real voice hardware/STT/TTS diagnostics, grouped Ollama model warm-up, separate infrastructure/capability health, better timeout classification, and clearer ComfyUI diagnostics/restart handling.

The v3.0.23 updater has been validated with the real AgentNEO UpdateManager from a clean v3.0.22 baseline. It is **not** currently represented as a cumulative updater from v3.0.11-v3.0.21.

## Current stable in-app release

- Version: `3.0.22`
- In-app updater: `AgentNEO_v3.0.22_Update.zip`
- Update type: **cumulative**
- Supported direct upgrade baselines: `3.0.11` through `3.0.21`
- SHA-256: `653d461311ac40ea6f39e677d092018b482be874845a0666b61e245af2ae8efa`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.22.md`

The signed public `latest.json` feed intentionally remains on v3.0.22 until v3.0.23 has completed older-baseline cumulative-update validation and the normal signing/publisher gate.

Clients using the stable in-app updater verify the exact updater SHA-256 and Ed25519 publisher signature before installation.
