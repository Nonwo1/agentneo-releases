# AgentNEO cumulative update policy

Every stable AgentNEO updater must be cumulative across all supported upgrade baselines.

For a target release, the updater package must contain the complete updater-managed application state required to converge any supported older installation directly to the target version. It must not assume that the user is running the immediately previous release.

Protected user/runtime data must remain untouched unless an explicit, versioned migration is required. This includes user settings, permissions, credentials/API keys, local models, memories, runtimes, workspaces, outputs and other user-owned data.

Before publication, the exact release ZIP must be tested using each supported baseline's real UpdateManager. Each baseline must pass direct old-version -> target-version inspection, transactional apply, payload hash verification, deletion/migration checks, protected-data preservation, and final version synchronization.

For AgentNEO v3.0.20, direct upgrade validation covers v3.0.11 through v3.0.19 -> v3.0.20.
