import logging

import ecs_logging
import structlog as structlog

from app.config import Config
from app.constants import LOG_LEVEL_MAP

service_name = "APIService"
_settings = Config()

if _settings.ECS_LOGGING_USE:
    structlog.configure(
        processors=[ecs_logging.StructlogFormatter()],
        wrapper_class=structlog.make_filtering_bound_logger(LOG_LEVEL_MAP.get(_settings.LOG_LEVEL, logging.INFO)),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
    )
    logger = structlog.get_logger(service_name)
    logger = logger.bind(**{
        "service_name": service_name,
    })

    formatter = structlog.stdlib.ProcessorFormatter(
        processors=[ecs_logging.StructlogFormatter()],
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging.basicConfig(handlers=[handler])
else:
    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    )

    logger = logging.getLogger(service_name)
    logger.setLevel(_settings.LOG_LEVEL)
