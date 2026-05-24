# insiderone-devops-case (Day 1 Foundation)

## Project overview
This repository provides a small, production-minded FastAPI service as the Day 1 foundation for the DevOps internship case study.

## Endpoints
- `GET /ping` → `{"message":"pong"}`
- `GET /healthz` → `{"status":"ok"}`
- `GET /version` → returns `APP_VERSION` or fallback `local-dev`

## Local run instructions
1. Create environment file:
   ```bash
   cp .env.example .env
   ```
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Run app:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Docker run instructions
Build and run with Docker:
```bash
docker build -t insiderone-api:day1 .
docker run --rm -p 8000:8000 --env-file .env insiderone-api:day1
```

Or with docker-compose:
```bash
docker compose up --build
```

## Kubernetes Deployment

### Dev
```bash
helm upgrade --install insiderone-api charts/insiderone-api \
-f charts/insiderone-api/values-dev.yaml
```

### Prod
```bash
helm upgrade --install insiderone-api charts/insiderone-api \
-f charts/insiderone-api/values-prod.yaml
```

## Test instructions
Run tests:
```bash
python -m pytest -q
```

## Architecture philosophy
- Keep the scope intentionally small
- Favor reproducibility and clear defaults
- Use production-minded basics early (healthcheck, non-root container, structured logs)
- Avoid premature complexity

## Why FastAPI
FastAPI is lightweight, fast to start with, easy to test, and fits cleanly into container-first DevOps workflows.

## CI/CD

### CI workflow
GitHub Actions runs on pull requests and pushes to `main`.

The CI pipeline:
- checks out the repository
- sets up Python 3.12
- installs dependencies from `requirements.txt`
- runs `pytest`
- builds the Docker image
- scans the built image with Trivy
- scans the repository for secrets with gitleaks

Trivy is configured to fail the pipeline when `HIGH` or `CRITICAL` vulnerabilities are detected.

### Image publishing
The release workflow publishes the container image to GitHub Container Registry (GHCR) on pushes to `main` and tags matching `v*`.

- `latest` is the rolling tag for the most recent published build.
- `sha-${{ github.sha }}` is the immutable tag used for traceability.
