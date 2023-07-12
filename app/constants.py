import logging

from app.enums import LogLevel

LOG_LEVEL_MAP = {
    LogLevel.DEBUG.value: logging.DEBUG,
    LogLevel.INFO.value: logging.INFO,
    LogLevel.WARNING.value: logging.WARNING,
    LogLevel.ERROR.value: logging.ERROR,
    LogLevel.FATAL.value: logging.FATAL,
}
