# AgentNEO Releases

Official public distribution repository for AgentNEO release packages and update metadata.

## Release naming

- `AgentNEO_vX.Y.Z.exe` — full Windows installer when published
- `AgentNEO_vX.Y.Z_Update.zip` — selective application update package
- `SHA256SUMS.txt` — hashes for the currently published release assets
- `latest.json` — signed automatic-update metadata
- `public-key-v1.txt` — public update-verification key
- `release-notes/vX.Y.Z.md` — release notes for each published version

## Publishing an update

1. Create the GitHub release for the new version.
2. Upload the exact update ZIP without modifying or recompressing it.
3. Verify its SHA-256.
4. Update `SHA256SUMS.txt`.
5. Update the signed `latest.json` after the release asset is available.

AgentNEO clients verify the expected SHA-256 and publisher signature before installing an online update.

Copyright © 2026 AgentNEO owner. All rights reserved. Third-party components remain subject to their respective licence terms.
