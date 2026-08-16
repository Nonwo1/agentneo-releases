# AgentNEO Releases

Official public distribution repository for compiled AgentNEO releases and update metadata.

This repository is intentionally **binary/release-only**. It must not contain AgentNEO proprietary source code, private signing keys, API credentials, licence-generation keys, customer licence data, development secrets, or internal build material.

## Release naming

- `AgentNEO_vX.Y.Z.exe` — full Windows installer
- `AgentNEO_vX.Y.Z.aneoupdate` — selective application update package when used
- `SHA256SUMS.txt` — published release hashes
- `latest.json` — signed update-feed metadata when enabled

## Security

AgentNEO update clients must verify the expected SHA-256 and publisher signature before installing online updates. Private signing keys are never stored in this repository.

Copyright © 2026 AgentNEO owner. All rights reserved. Third-party components remain subject to their respective licence terms.
