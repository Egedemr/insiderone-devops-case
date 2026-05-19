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
