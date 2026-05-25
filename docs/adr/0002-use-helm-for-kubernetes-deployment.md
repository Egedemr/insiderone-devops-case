# ADR-0002: Use Helm for Kubernetes deployment
## Status
Accepted
## Context
The project needs repeatable Kubernetes deployment with environment-specific values and minimal manual YAML editing. Reviewers also need a clear path to install, upgrade, and roll back releases.
## Decision
Use Helm to package and deploy the Kubernetes resources for `insiderone-api`. Keep defaults simple and use separate values files for dev and prod-oriented settings.
## Consequences
Deployments become easier to reproduce and review across environments. Rollback and release history are also available through standard Helm commands.
