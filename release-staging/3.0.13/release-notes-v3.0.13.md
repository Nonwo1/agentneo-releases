# AgentNEO v3.0.13 — Media Studio ComfyUI Workflow Auto-Assignment & Reliability

AgentNEO v3.0.13 expands Media Studio's ComfyUI integration so the application can use the same normal workflow JSON files that ComfyUI saves, automatically pair those workflows with the selected model and its support files, and keep long-running jobs monitored reliably. The earlier v3.0.13 scroll-safe Generation layout and long-job timeout repairs remain included.

## Complete ComfyUI model selectors

- The main **ComfyUI model** selector now lists the complete discovered ComfyUI catalogue rather than only a restricted model subset.
- Adds dedicated **Diffusion model**, **VAE**, and **Text encoder** selectors.
- Each support selector is populated automatically from the correct detected ComfyUI model category. Diffusion also accepts compatible `unet` catalogue entries and Text encoder also accepts compatible `clip` entries.
- Model discovery combines recursive filesystem scanning, the connected ComfyUI `/models` catalogue, and loader COMBO values exposed by `/object_info`. This makes the selector reflect files that the live ComfyUI loaders can actually see, including nested model paths.
- Full model paths remain available through tooltips while the visible selector text stays compact.
- Selecting a primary or support model automatically recalculates the matching workflow/support assignment. The user can still override the three support selectors manually.

## Normal ComfyUI saved/preset workflows now work

- Media Studio no longer requires the user to export a separate API-format workflow for routine custom/video workflows.
- AgentNEO accepts both ComfyUI API prompt JSON and the normal frontend workflow JSON produced by ComfyUI's workflow/preset save system.
- Normal frontend workflows are converted into a runnable API prompt graph immediately before queueing.
- Native ComfyUI subgraphs stored under `definitions.subgraphs` are recursively resolved during conversion, including exposed subgraph inputs and outputs.
- Widget values are mapped using the live `/object_info` definitions so checkpoint, diffusion model, VAE, text encoder, sampler, scheduler, dimensions, seeds, frame controls and custom-node widgets keep their normal ComfyUI values.
- Unknown/custom node classes are preserved in the converted graph so validation reports the exact missing node instead of silently dropping part of the workflow.
- The original frontend workflow is retained as prompt metadata when a converted graph is queued.

## Automatic workflow API scanning and model matching

- AgentNEO scans local Media Workflows folders and supported local ComfyUI user workflow directories.
- It also scans ComfyUI's `/workflow_templates` API and caches server-provided workflow templates for automatic matching.
- It additionally scans the connected ComfyUI `/userdata` workflow API, downloads normal user-saved workflow JSON into a private Media Workflows cache, and makes those workflows available even when ComfyUI is running as a separate local/LAN server.
- Workflow metadata is inspected for embedded checkpoint/diffusion-model, VAE and text-encoder references.
- Workflow candidates are scored against the selected task, selected model, model family, source-image requirement and selected support files.
- A saved/preset workflow that explicitly references the selected model outranks a generic fallback template.
- When the matched workflow identifies compatible support files that are present in the model catalogue, the new Diffusion model / VAE / Text encoder selectors are filled automatically.
- **SELECT WORKFLOW** now accepts either normal ComfyUI workflow JSON or API-format JSON.

## Media Studio layout

- The **Generation** column lives inside its own vertical scroll area so Qt cannot compress rows until text clips at smaller window heights or higher Windows display scaling.
- Backend, task, model, support-model, resolution, step, CFG, seed, denoise, frame and FPS fields use display-scale-aware minimum heights.
- **Model catalogue**, **Workflow status**, and **Generation status** are dedicated selectable, independently scrollable information panels.
- Normal job status uses concise QUEUED / RUNNING / FINALISING messages; raw backend details remain in **Technical Output**.

## ComfyUI timeout / job-monitoring repair

- Individual `/history/{prompt_id}` or `/queue` read timeouts are treated as transient while ComfyUI is under load.
- AgentNEO follows the exact `prompt_id` through `queue_running` and `queue_pending`.
- A prompt that ComfyUI still reports as running or pending is not failed merely because it has exceeded a fixed wall-clock duration.
- After a prompt leaves the queue, AgentNEO waits for its final history record.
- A bounded failure is raised only after the prompt disappears from both queue and history for a meaningful grace period, or the monitoring endpoints remain unreachable for an extended period.
- **CANCEL / INTERRUPT** remains the explicit user-controlled stop action.

## Preserved behaviour

- Standard checkpoint text-to-image and image-to-image automatic graphs remain available as fallbacks.
- Flux2 fallback workflow support remains available using user-installed compatible support weights.
- Source-image upload, universal image/video preview, output import, Save As/Open/Reveal, output history and contextual menus are retained.
- AgentNEO bundles no image/video model weights and does not replace the user's ComfyUI installation or workflow library.

## Update compatibility

The v3.0.13 selective updater is intended for an existing AgentNEO v3.0.12 installation and preserves user models, runtimes, settings, profiles, memories, API credentials, workspaces, ComfyUI workflows and outputs according to the normal AgentNEO update contract.
