# AgentNEO v3.0.19 — Sandbox Introspection & Universal Live Dictation Fix

AgentNEO v3.0.19 fixes two functional regressions reported against v3.0.18: Sandbox Lab read-only queries were being misclassified as software builds, and microphone transcription was not reliably appearing in chat inputs, including Command Centre.

## Sandbox Lab

- Treats requests such as “check if a sandbox is open”, “scan the Sandbox Lab page”, and other status/health reads as internal AgentNEO application introspection. They no longer trigger `sandbox_auto_prepare`, UAC elevation, Windows feature provisioning, or a request for a URL.
- Adds read-only `sandbox_active_sessions` and `sandbox_lab_snapshot` state surfaces and a deterministic supervisor fast path for Sandbox Lab status questions.
- Corrects the Sandbox Lab top capability labels so Hyper-V is only shown as READY when the build-lab backend itself is ready; the presence of the Hyper-V PowerShell module alone is no longer treated as readiness.
- Makes the Windows host probe resilient: CIM/feature failures are retained in `probe_error`, Windows registry/platform fallbacks populate OS/build/architecture, and local CPU/RAM fallbacks prevent misleading zero telemetry.
- Preserves the real elevated Windows optional-feature error in `Sandbox/Setup/last-feature-enable.json`, including category/FQID/HRESULT where Windows supplies them, instead of collapsing failures to “PowerShell command failed”.

## Voice transcription / shared chat draft

- Separates live Whisper preview events from final transcript events so a preview can no longer masquerade as a final utterance and overwrite/duplicate the draft.
- Adds a dictation session model that keeps text already typed in the box, previews the current spoken phrase live, commits final phrases in order, and deduplicates callback/final-event delivery.
- Flushes in-progress microphone audio when STOP is pressed so the last spoken phrase is not silently lost.
- Automatically links every native `ChatInput` discovered on AgentNEO pages to the shared draft, while retaining explicit Chat, Voice Assistant and overlay bindings.
- Makes Command Centre’s web chat textarea bidirectional over QWebChannel: typed text updates the native shared draft, and live/final speech is pushed back into the Command Centre input.
- Synchronizes the Command Centre draft when its bridge becomes ready, so page navigation/reload does not lose the current text.

## Validation

The release is covered by the existing AgentNEO suite plus v3.0.19 regression tests for Sandbox Lab introspection routing, backend readiness labels, feature-enable diagnostics, universal chat draft wiring and preview/final transcription separation. Windows-only UAC, Hyper-V and Windows Sandbox execution still requires final runtime verification on a Windows host; this package does not fabricate a Windows execution pass.
