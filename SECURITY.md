# Security

- Do not commit secrets to the repository.
- `.env` is ignored by git.
- `.env.example` is kept as the documented template for local setup.
- The Docker image runs as a non-root user.
- The Dockerfile includes a `HEALTHCHECK` against `/healthz`.
- CI fails on Trivy findings with severity `HIGH` or `CRITICAL`.
- CI runs `gitleaks` to catch committed secrets.
- GHCR publishing uses the GitHub-provided `GITHUB_TOKEN` in Actions.
- The demo endpoints are intentionally unauthenticated; in real deployments `/metrics` should stay internal.
- Dependency policy: keep direct dependencies small, update them regularly, and re-run tests plus CI scans after changes.
