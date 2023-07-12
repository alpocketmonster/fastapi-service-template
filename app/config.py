from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    LOG_LEVEL = "DEBUG"
    PORT = 8080

    ECS_LOGGING_USE = False

    SENTRY_USE = False
    SENTRY_DSN = ""

    METRICS_USE = True

    HEALTHCHECK_USE = True
