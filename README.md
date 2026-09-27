# AgentNEO Community Edition

## AgentNEO is now available for public testing

After a long period of development, rebuilding, testing and debugging, **AgentNEO v3.0.30 Community Edition** is now available for the wider community to download, explore, test and help improve.

AgentNEO is a Windows x64 multi-agent AI environment built around its interactive **Neural Brain Galaxy Command Centre**. It combines local and linked online AI models, specialist agents, memory and knowledge systems, permission-gated tools, voice and screen interaction, Media/ComfyUI integration, sandboxing, recovery tooling and an integrated update system in one desktop application.

This release is the beginning of community testing. Use AgentNEO, experiment with it, report bugs, suggest ideas, improve workflows and help shape future releases.

## Download AgentNEO v3.0.30

### New users

[⬇ Download AgentNEO v3.0.30 Installer RAR](https://github.com/Nonwo1/agentneo-releases/releases/download/3.0.30/AgentNEO_v3.0.30_Installer.rar)

Extract the RAR, then run the included AgentNEO installer.

### Existing AgentNEO v3.0.29 users

[⬇ Download the v3.0.30 Update](https://github.com/Nonwo1/agentneo-releases/releases/download/3.0.30/AgentNEO_v3.0.30_Update.zip)

### Developers / contributors

[⬇ Download the v3.0.30 Source Package](https://github.com/Nonwo1/agentneo-releases/releases/download/3.0.30/AgentNEO_v3.0.30_Source.zip)

[View the complete v3.0.30 release](https://github.com/Nonwo1/agentneo-releases/releases/tag/3.0.30)

## Green Code → Download ZIP

GitHub's green **Code → Download ZIP** button downloads the contents of the current repository branch. To make that path useful for non-technical users, this repository now keeps the current full installer archive in:

`FULL_PROGRAM_DOWNLOAD/AgentNEO_v3.0.30_Installer.rar`

So when somebody uses **Code → Download ZIP**, the downloaded repository ZIP includes the current AgentNEO installer RAR. Extract the GitHub ZIP, open `FULL_PROGRAM_DOWNLOAD`, extract the RAR, and run the installer.

For the quickest download, use the direct installer link above.

## What is AgentNEO?

AgentNEO includes an interactive 3D Neural Brain Galaxy Command Centre, AgentNEO and AgentSMITH dual-brain architecture, specialist AI agents, local and linked online model routing, configurable model inference controls, persistent memory and knowledge, Prompt Architect, Voice Assistant, screen interaction, Media/ComfyUI integration, permission-gated PC/system tools, Sandbox Lab, Recovery Centre, Update Centre and plugin/API support.

## Community Edition licensing

AgentNEO original core code is released under **GNU AGPL v3 or later**.

The original **AgentNEO Neural Brain Galaxy** visual design and identified Galaxy/brand assets remain separately protected under the bundled AgentNEO Neural Brain Galaxy Community Asset Licence. The Galaxy may be used as part of AgentNEO Community Edition under that licence, but it is not licensed for extraction, resale, rebranding or use as the signature interface of another product without permission.

Third-party components remain under their respective licences. A future paid edition does not revoke rights already granted to a published Community Edition release.

## v3.0.30 validation

The final v3.0.30 build was exercised on Windows:

- v3.0.29 → v3.0.30 update: **PASS**
- AgentNEO launch after update: **PASS**
- clean Full Install into a new folder: **PASS**
- launch from the new desktop shortcut: **PASS**
- installation path containing spaces: **PASS**
- automated regression tests: **284 passed**
- updater-managed final hash mismatches: **0**

### Published SHA-256

- Installer RAR: `8ee266153c54a6d98d9fc73ad963281a9d2db36ba416aa7bb4c88f5d23658f5f`
- Updater: `0905351ca96e3973594d0a6f62b53dbde552365f22e38f64bdf6ed2d7eaf2ee0`
- Source: `ec0d56a63d31ab7433723820811bb46d33a1fcb41af60123e8a71f4d67e9332a`

## Help test AgentNEO

Bug reports, reproducible diagnostics, screenshots, feature ideas and contributions are welcome through GitHub Issues. Please remove API keys, passwords and other private information before posting logs publicly.

Contact: **no_nwo1@protonmail.com**

## Windows SmartScreen

The current Windows installer is not yet signed with a publicly trusted Authenticode certificate, so Windows may display an **Unknown Publisher / SmartScreen** warning. The SHA-256 values above can be used to verify the exact published files.

---

Current stable release: **AgentNEO v3.0.30 Community Edition**

Stable update feed: `latest.json`  
Consolidated history: `CHANGELOG.txt`  
Release information: `release-notes/v3.0.30.md`
