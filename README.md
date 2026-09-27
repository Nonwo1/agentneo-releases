# AgentNEO Releases

Official public distribution repository for **AgentNEO Community Edition** release packages and signed update metadata.

## Current stable release — 3.0.30

AgentNEO v3.0.30 is the first public Community Edition release intended for wider testing, bug reports, feature ideas and community contributions.

AgentNEO is a Windows x64 multi-agent AI environment built around the interactive **Neural Brain Galaxy Command Centre**, with local/online model routing, specialist agents, memory/knowledge, permission-gated tools, voice and screen interaction, Media/ComfyUI integration, sandboxing, recovery tooling and verified selective updates.

### Downloads

- Full installer: `AgentNEO_v3.0.30_Installer.exe`
- Existing v3.0.29 users: `AgentNEO_v3.0.30_Update.zip`
- Community source: `AgentNEO_v3.0.30_Source.zip`
- Stable update feed: `latest.json`
- Release information: `release-notes/v3.0.30.md`

### Published SHA-256

- Installer: `a8b4418cc0457eacf80bc07d95b7556655910c757e81fee7ae4fc5acd8be8748`
- Updater: `0905351ca96e3973594d0a6f62b53dbde552365f22e38f64bdf6ed2d7eaf2ee0`
- Source: `ec0d56a63d31ab7433723820811bb46d33a1fcb41af60123e8a71f4d67e9332a`

## Community Edition licensing

AgentNEO original core code is released under **GNU AGPL v3 or later**.

The original **AgentNEO Neural Brain Galaxy** visual design and identified Galaxy/brand assets remain separately protected under the bundled AgentNEO Neural Brain Galaxy Community Asset Licence. Third-party components remain under their respective licences.

A future paid edition does not revoke rights already granted to a published Community Edition release.

## v3.0.30 validation

The final v3.0.30 build has been exercised on the target Windows system:

- v3.0.29 → v3.0.30 updater: PASS.
- AgentNEO launch after update: PASS.
- clean Full Install into a new folder: PASS.
- launch from the new desktop shortcut: PASS.
- automated regression tests: 284 passed.
- updater-managed final hash mismatches: 0.

The updater feed is signed with AgentNEO's existing Ed25519 publisher key and the exact GitHub-published updater digest is verified before feed promotion.

## Recent chain

| Release | Formal update baseline | Updater SHA-256 |
|---|---|---|
| 3.0.30 | 3.0.29 | `0905351ca96e3973594d0a6f62b53dbde552365f22e38f64bdf6ed2d7eaf2ee0` |
| 3.0.29 | 3.0.28 | `75336210afa6f639e7a2b8b4202c027353873ece40282c72d98e63a291647c69` |
| 3.0.28 | 3.0.27 | `d28bbf63a078d9a9d7bbe4336422928b56f504a19b9c0eef439859164e445caf` |
| 3.0.27 | 3.0.26 | `2aff9fbc19105254ffab49412466acd33d25b42046ab02fb478612422da68df7` |
| 3.0.26 | 3.0.25 | `fb38c504ca77df4cdf220204e07a8ad01d1a302ae1235416afdd7ac335851ad6` |

## Public testing

Bug reports, reproducible diagnostics, feature ideas and contributions are welcome through GitHub Issues.

Contact: **no_nwo1@protonmail.com**

> The Windows installer is not yet signed with a publicly trusted Authenticode certificate, so Windows SmartScreen may display an Unknown Publisher warning.
