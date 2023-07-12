import json
import os
from typing import Callable

import fastapi
import psutil
from aioprometheus import MetricsMiddleware, Registry, render
from fastapi import FastAPI

from app.config import Config
from app.endpoints.router import router
from app.metrics import ram_metric, cpu_metric, register_metrics

_settings = Config()


def check_metrics():
    # update memory metrics
    ram_metric.set({"type": "ram"}, psutil.Process(os.getpid()).memory_info().rss)
    # update cpu metrics
    cpu_metric.set({"cpu": "average"}, psutil.cpu_percent(interval=1))


def get_healthcheck_handler() -> Callable:
    async def handle_healthcheck(request) -> fastapi.Response:
        return fastapi.Response(content=json.dumps({"status": "OK"}))
    return handle_healthcheck


def get_metrics_handler(reg: Registry) -> Callable:
    async def handle_metrics(request) -> fastapi.Response:
        check_metrics()
        content, http_headers = render(
            reg, ["Accept"]
        )
        return fastapi.Response(content=content, headers=http_headers)
    return handle_metrics


app = FastAPI()
app.include_router(router)


if _settings.HEALTHCHECK_USE:
    healthcheck_handler = get_healthcheck_handler()
    app.add_route("/healthcheck", healthcheck_handler, methods=["GET"])
if _settings.METRICS_USE:
    app.add_middleware(MetricsMiddleware)
    registry = register_metrics()
    metrics_handler = get_metrics_handler(registry)
    app.add_route("/metrics", metrics_handler, methods=["GET"])
