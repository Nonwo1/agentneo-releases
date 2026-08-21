# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current release

- Version: `3.0.24`
- In-app updater: `AgentNEO_v3.0.24_Update_from_3.0.23.zip`
- Validated direct-update baseline: **3.0.23**
- SHA-256: `2e53d623c4780812c9ff86546dd30a8c513dc9b147a2ca85b88bf66b91a8669d`
- Signed feed: `latest.json`
- Release notes: `release-notes/v3.0.24.md`
- Validation: `release-staging/3.0.24/AgentNEO_v3.0.24_Validation.txt`

AgentNEO 3.0.24 adds activity-aware long-task handling for slow local models and a substantially more automatic Media Studio. Active Ollama streams keep tasks alive while context, reasoning, metadata or output-token activity continues. Media Studio adds ComfyUI LAUNCH / READY, automatic model-family presets, model setup reports, API-workflow discovery/generation, and pre-submit ComfyUI node/workflow validation.

The public update feed now points to AgentNEO 3.0.24 and is signed with the configured AgentNEO Ed25519 publisher key. The published updater SHA-256 is checked before installation.

The v3.0.24 updater has been validated with AgentNEO's real transactional UpdateManager from a clean v3.0.23 baseline. Older direct-upgrade baselines have not been claimed as validated for this package.
