# AgentNEO v3.0.23

AgentNEO v3.0.23 combines the new non-bundled hybrid speech stack with revised model-aware detailed-agent diagnostics.

Highlights:
- Faster-Whisper remains authoritative final STT.
- Optional Vosk live partial STT and optional Kokoro local TTS remain separately installable/removable and non-bundled.
- Existing MeloTTS, Qwen VoiceDesign and linked online choices remain selectable.
- Barge-in keeps microphone capture available while AgentNEO is speaking and can cancel TTS.
- Local diagnostic probes are grouped by Ollama model, with one warm-up per model group.
- Cold/resident local diagnostic defaults are 180s / 60s.
- Missing role markers are warnings rather than inference failures.
- Reports separate Infrastructure Health from Agent Capability Health.
- Ollama diagnostics can expose model load time, TTFT, eval count and tokens/sec.
- Voice diagnostics now test actual speech stages rather than only provider/model presence.
- Media diagnostics distinguish stopped/unconfigured/unreachable/online ComfyUI states and Recovery Centre can START/RESTART an installed local ComfyUI instance.

Validation:
- 237/237 automated regression tests PASS.
- 110 Python files parse/compile.
- 86 JSON files validate.
- Source manifest: 380 entries verified.
- Clean v3.0.22 -> v3.0.23 UpdateManager test PASS.
- 23 files updated transactionally; 293 updater-managed hashes verified afterward.
- Protected settings/permissions/agents/models remained unchanged.

Important: the v3.0.23 updater is currently validated from v3.0.22 only. The signed stable in-app feed remains v3.0.22 until older-baseline cumulative validation and the normal signing gate are completed.
