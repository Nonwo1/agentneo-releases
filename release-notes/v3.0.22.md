# AgentNEO v3.0.22 — Capability-Aware Agent Diagnostics

AgentNEO v3.0.22 replaces the generic one-prompt-for-every-agent health test with a deterministic, capability-aware diagnostic runner.

## What changed

- Supervisor, Prompt Architect, Planner, Researchers, Coders, Tester, Reviewer, Writer, System Control and GamerNEO receive short role-specific inference probes.
- PC Doctor uses a bounded inference probe plus read-only system-information checks.
- Vision uses the configured vision path with an in-memory image instead of a text-only test.
- Memory validates its embedding path without storing diagnostic memory.
- Voice checks configured STT/TTS or online-backend readiness without recording or playing audio.
- Screen Monitor uses in-memory capture only and does not save a diagnostic screenshot.
- Media validates configured backend/workflow readiness without creating persistent media.
- Non-applicable probes are reported as `NOT_APPLICABLE` rather than false failures.

## Reliability and performance

- Full-agent diagnostics route directly to the diagnostic engine; the Supervisor no longer re-plans between each agent probe.
- Local model probes use compact context/output settings, hidden thinking disabled, keep-alive reuse, bounded resident/cold-load timeouts and one transient retry for recoverable errors.
- A timeout or backend failure is recorded and the runner continues to the next agent.
- Duplicate Tool/Sandbox event rows caused by same-thread duplicate publication are suppressed without suppressing legitimate high-frequency telemetry.

## Read-only diagnostic behavior

The standard `test all agents` health check is read-only. It does not create a task checkpoint, save a report file, write results into user memory, create permanent media, or open Windows Sandbox just because the user requested a test. The v3.0.21 task-scoped isolation protocol remains unchanged for work that genuinely requires isolated execution.

## Validation and updates

- 222/222 automated regression tests passed.
- The cumulative updater uses `agentneo-update-v1`, targets v3.0.22, and retains v3.0.11 as the minimum supported baseline.
- Direct upgrade validation passed with the real UpdateManager from every supported version v3.0.11 through v3.0.21.
- Protected settings, permissions, credentials, models, memories, runtimes, workspaces, outputs and other user data remain protected.
- Exact updater SHA-256: `653d461311ac40ea6f39e677d092018b482be874845a0666b61e245af2ae8efa`.
