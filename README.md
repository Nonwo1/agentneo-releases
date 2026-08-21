# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current manual release

- Version: `3.0.24`
- Manual updater: `AgentNEO_v3.0.24_Update_from_3.0.23.zip`
- Validated manual-update baseline: **v3.0.23 only**
- Updater SHA-256: `2e53d623c4780812c9ff86546dd30a8c513dc9b147a2ca85b88bf66b91a8669d`
- Release notes: `release-notes/v3.0.24.md`
- Validation: `release-staging/3.0.24/AgentNEO_v3.0.24_Validation.txt`
- Checksums: `release-staging/3.0.24/SHA256SUMS.txt`

v3.0.24 adds activity-aware long-task handling for slow local models and a substantially more automatic Media Studio. Active Ollama streams now keep tasks alive while context, reasoning, metadata or output-token activity continues. Media Studio gains ComfyUI LAUNCH / READY, automatic model-family presets, model setup reports, API-workflow discovery/generation, and pre-submit ComfyUI node/workflow validation.

The v3.0.24 updater was validated with AgentNEO's real transactional UpdateManager from a clean v3.0.23 baseline. It is **not** currently represented as a cumulative updater from older baselines.

## Current stable in-app release

- Version: `3.0.22`
- In-app updater: `AgentNEO_v3.0.22_Update.zip`
- Update type: **cumulative**
- Supported direct upgrade baselines: `3.0.11` through `3.0.21`
- SHA-256: `653d461311ac40ea6f39e677d092018b482be874845a0666b61e245af2ae8efa`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.22.md`

The signed public `latest.json` feed intentionally remains on v3.0.22 until a newer updater has completed older-baseline cumulative-update validation and the normal signing/publisher gate.

Clients using the stable in-app updater verify the exact updater SHA-256 and Ed25519 publisher signature before installation.
