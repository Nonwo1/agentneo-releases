# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Current stable release

- Version: `3.0.22`
- In-app updater: `AgentNEO_v3.0.22_Update.zip`
- Update type: **cumulative**
- Supported direct upgrade baselines: `3.0.11` through `3.0.21`
- SHA-256: `653d461311ac40ea6f39e677d092018b482be874845a0666b61e245af2ae8efa`
- Stable feed: `latest.json`
- Release notes: `release-notes/v3.0.22.md`

v3.0.22 adds deterministic capability-aware diagnostics for all registered agents. It uses role-specific backend tests, bounded continue-on-failure timeouts, read-only health checks, and duplicate runtime-event suppression. Normal all-agent diagnostics do not open Windows Sandbox; the task-scoped isolation protocol remains active when isolated execution is actually required.

Stable updater packages are cumulative. v3.0.22 was validated with the real UpdateManager from every supported baseline v3.0.11 through v3.0.21 while preserving protected user/runtime data.

Clients verify the exact updater SHA-256 and Ed25519 publisher signature before installation.
