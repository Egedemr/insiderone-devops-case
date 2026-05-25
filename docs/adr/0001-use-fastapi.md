# ADR-0001: Use FastAPI
## Status
Accepted
## Context
The service needed a small HTTP framework with fast startup, easy testing, and first-class API endpoint support. The repository scope favors a lightweight app that fits cleanly into Docker, Kubernetes, and CI workflows.
## Decision
Use FastAPI as the application framework for the API service. It provides simple routing, operationally friendly defaults, and straightforward local development.
## Consequences
The app stays easy to run, test, containerize, and expose with health endpoints. The stack remains Python-centric without adding unnecessary platform complexity.
