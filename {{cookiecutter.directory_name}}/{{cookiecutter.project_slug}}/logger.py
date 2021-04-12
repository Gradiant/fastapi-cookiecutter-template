import sys

from loguru import logger

from .settings import request_logging_settings as settings

LoggerFormat = "<green>{time:YY-MM-DD HH:mm:ss.SSS}</green> | " \
               "<level>{level: <8}</level> | " \
               "<level>{message}</level> | {extra}"

logger.remove()
logger.add(
    sys.stderr,
    level=settings.level.upper(),
    format=LoggerFormat,
    serialize=settings.serialize,
    enqueue=True,  # process logs in background
    diagnose=False  # hide variable values in log backtrace
)
