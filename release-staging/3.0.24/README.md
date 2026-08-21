# AgentNEO 3.0.24 Release Metadata

This directory contains the public release metadata for AgentNEO 3.0.24.

## Update scope

The 3.0.24 updater has been validated for **AgentNEO 3.0.23 -> 3.0.24** with the real transactional `UpdateManager`.

It is not represented as a validated cumulative updater from earlier baselines unless those exact baselines are separately tested.

## In-app update feed

The signed public `latest.json` feed now points to AgentNEO 3.0.24. The feed uses the configured AgentNEO Ed25519 publisher key and the exact updater SHA-256 before installation.

- Version: `3.0.24`
- Package: `AgentNEO_v3.0.24_Update_from_3.0.23.zip`
- SHA-256: `2e53d623c4780812c9ff86546dd30a8c513dc9b147a2ca85b88bf66b91a8669d`
- Minimum validated baseline: `3.0.23`

## Major changes

- Activity-aware long-running Ollama tasks with live stream/context/output activity monitoring.
- Longer resident/cold/resource-pressure stall budgets while work continues.
- Correct idle READY status when optional ComfyUI is stopped.
- ComfyUI **LAUNCH / READY** button and explicit auto-start before generation.
- Automatic image/video model family detection and preset configuration.
- Model setup reports and confirmed model-folder correction.
- API workflow selector plus **GENERATE / DISCOVER API WORKFLOWS**.
- Standard checkpoint, Flux, Flux-GGUF and upscale workflow foundations.
- ComfyUI `/object_info` workflow validation before queueing.
- Specific missing-node/support-file errors instead of generic generation failures.
- No bundled ComfyUI, media model weights, custom-node packs or third-party workflow downloads.
