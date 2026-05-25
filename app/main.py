import logging
import os

from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

from app.core.logging import configure_logging

configure_logging()
logger = logging.getLogger("app")
app = FastAPI(title="insiderone-devops-case", version="0.1.0")
Instrumentator().instrument(app).expose(app, endpoint="/metrics")


@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    response = await call_next(request)
    logger.info("request_completed", extra={"path": request.url.path})
    return response


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"message": "pong"}


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": os.getenv("APP_VERSION", "local-dev")}
