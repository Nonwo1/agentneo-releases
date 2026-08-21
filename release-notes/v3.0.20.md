# AgentNEO v3.0.20

## Sandbox runtime authority and deterministic control

- Treats successful Windows Sandbox runtime evidence and disposable self-test PASS results as authoritative readiness evidence when optional-feature telemetry is unavailable.
- Fixes the Sandbox Lab contradiction where a launched Windows Sandbox task could coexist with `WINDOWS SANDBOX · UNKNOWN` and `OVERALL · NOT READY`.
- Reworks the Windows Sandbox self-test lifecycle to keep the task registry alive through verification before cleanup.
- Makes sandbox destruction idempotent and retries transient Windows file-lock errors; unresolved handles become `cleanup_pending` instead of causing a false hard failure.
- Adds a deterministic `sandbox_configure_and_test` service path so Sandbox Lab requests can query, configure, test and report on the actual AgentNEO sandbox state without being routed through Prompt Architect.
- Contextual retry commands such as `try again` continue the preceding sandbox operation when the recent conversation is about Sandbox Lab.

## Local model and memory reliability

- Adds a semantic-progress watchdog to streamed local-model generation. Hidden reasoning/metadata can no longer keep a job alive indefinitely while visible answer content remains at zero characters.
- Adds a hard wall-clock generation limit and separate accounting for visible content and model thinking.
- Prompt Architect uses the shorter semantic-progress guard so stalled `gpt-oss:20b` jobs are aborted instead of occupying the GPU for many minutes with `content_chars: 0`.
- Memory embedding now discovers the configured/managed Ollama service instead of hard-coding port 11434.
- Managed AgentNEO Ollama is preferred on `127.0.0.1:11435` when present.
- AUTO embedding resolves a real installed embedding model and supports both `/api/embed` and the legacy `/api/embeddings` API.

## Preserved v3.0.19 fixes

- Keeps the universal microphone/transcription routing added in v3.0.19 for Command Centre and all registered chat/prompt inputs.
- Keeps the existing AgentNEO downloader/update contract and protected user configuration behavior.

## Validation

- 200 automated tests passed.
- The v3.0.20 updater was inspected and applied using the v3.0.19 UpdateManager against a clean v3.0.19 source tree.
- Simulated in-app update result: `Update installed and verified`.
- v3.0.20 updater SHA-256: `5ff87d9dc99e71ebb333855586960912305d28547b0c2f80296463dbcd4cbaaf`.
