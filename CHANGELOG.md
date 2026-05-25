# Changelog

## v0.1.0
- FastAPI service foundation with `/ping`, `/healthz`, `/version`, and `/metrics`
- Dockerized runtime with non-root user and `HEALTHCHECK`
- Helm chart for Minikube/Kubernetes deployment with dev/prod values
- GitHub Actions CI with tests, Trivy `HIGH/CRITICAL` scan, and gitleaks
- GHCR publishing with `latest` and immutable `sha-...` tags
- Local Prometheus/Grafana observability setup
