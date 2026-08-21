# AgentNEO v3.0.21 — Task-Scoped Isolation Protocol

AgentNEO v3.0.21 changes Automatic Safe sandbox orchestration from broad prompt-keyword provisioning to capability-based, task-scoped isolation. The behavior is designed to match the publicly documented and observable ChatGPT/Codex safety model as closely as AgentNEO's Windows Sandbox/Hyper-V architecture allows, without claiming access to OpenAI's private infrastructure or undisclosed implementation details.

## Isolation behavior

- Ordinary conversation, planning, internal AgentNEO state inspection, agent-health diagnostics, model/status queries and other read-only reasoning do not create or open a Windows Sandbox.
- Generated or untrusted code/program execution, compiling, installer execution and requested runtime verification are isolated automatically.
- Uploaded archives/files that require extraction, conversion, programmatic examination, binary inspection or execution are staged into a task-scoped isolated workspace. Only the explicitly attached file may be staged by the attachment bridge.
- Network access inside a new sandbox is OFF by default. DOWNLOAD ONLY is selected only when the task explicitly requires dependency/tool acquisition; wider network access remains an explicit policy choice.
- Sandboxes are EPHEMERAL by default and receive only task-scoped input/work/output mappings. No silent host-execution fallback is permitted when isolation is required.
- Explicit per-task instructions such as “do not open a sandbox” are hard constraints. If execution would be required, AgentNEO performs static/read-only work and reports that the execution portion was skipped rather than violating the restriction.
- Explicit “do not create, modify or delete files” instructions suppress task-owned file mutation tools and task checkpoint/memory persistence for that run.
- AUTOMATIC SAFE no longer runs an extra disposable backend self-test merely because a ready backend is being used for the first time. Explicit Sandbox Lab configure/test operations can still perform real backend self-tests.

## Routing and enforcement

Sandbox routing is now based on required capabilities rather than generic terms such as “test”. The Tool Registry independently enforces task constraints, so a mistaken model/tool request cannot override a user prohibition or silently execute on the host. Sandbox Lab read-only queries remain direct internal state operations.

## Preserved fixes

v3.0.21 includes all cumulative updater-managed application fixes from the supported v3.0.11+ baseline, including v3.0.20 Windows Sandbox readiness/self-test lifecycle repairs, Ollama semantic-progress/model recovery changes, and the earlier universal live transcription/Command Centre dictation fixes.

## Validation

The complete Python unit-test suite is run before packaging. The cumulative updater is built from the complete updater-managed v3.0.21 application state and is intended to converge any supported baseline directly to the current release while protecting user-owned settings, permissions, models, credentials, memories, workspace/output data and external runtimes.
