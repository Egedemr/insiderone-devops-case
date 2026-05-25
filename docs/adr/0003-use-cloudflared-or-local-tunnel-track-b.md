# ADR-0003: Use cloudflared or local tunnel Track B
## Status
Accepted
## Context
The main delivery path focuses on local, Docker, and Minikube-based validation. A public demo tunnel can be useful later, but it is not required for the core repository foundation.
## Decision
Treat `cloudflared` or a similar local tunnel as a Track B option for future public demos. Do not make tunnel setup part of the default implementation path in this repository.
## Consequences
The core setup stays smaller and easier to review. A public access option can still be added later without changing the primary deployment workflow.
