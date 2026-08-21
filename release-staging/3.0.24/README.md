# AgentNEO v3.0.24 Manual Release Staging

This directory contains the public release metadata for AgentNEO v3.0.24.

## Update scope

The v3.0.24 updater has been validated for **AgentNEO v3.0.23 -> v3.0.24** with the real transactional `UpdateManager`.

It is not represented as a cumulative updater from earlier baselines until those exact baselines are separately validated.

## Manual release artifacts

- `AgentNEO_v3.0.24_Update_from_3.0.23.zip`
- `AgentNEO_v3.0.24_Source_Code.zip`
- `AgentNEO_v3.0.24_Full_Installer.exe`
- `AgentNEO_v3.0.24_Full_Installer_Package.zip`
- `AgentNEO_v3.0.24_Validation.txt`
- `SHA256SUMS.txt`

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

The signed stable in-app `latest.json` feed is intentionally not changed by this manual release metadata update.
