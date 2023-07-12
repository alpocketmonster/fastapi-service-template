import os

from aioprometheus import Gauge, Registry

const_labels: dict[str, str] = {"extra": ""}

metrics = []
# create a gauge metrics to track memory usage.
ram_metric = Gauge(
    "memory_usage_bytes", "Memory usage in bytes.", const_labels=const_labels
)
# create a gauge metrics to track CPU.
cpu_metric = Gauge(
    "cpu_usage_percent", "CPU usage percent.", const_labels=const_labels
)

metrics.append(ram_metric)
metrics.append(cpu_metric)


def register_metrics() -> Registry:
    registry = Registry()
    for metric in metrics:
        registry.register(metric)
    return registry
