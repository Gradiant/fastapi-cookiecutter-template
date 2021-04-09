import sys

from loguru import logger

from .settings import request_logging_settings as settings

LoggerFormat = "<green>{time:YY-MM-DD HH:mm:ss}</green> | " \
               "<level>{level}</level> | " \
               "<level>{message}</level> | " \
               "{extra} {exception}"

logger.remove()
logger.add(
    # TODO Review usage of sys.stderr
    # TODO review format of LoggerFormat
    sys.stderr,
    level=settings.level.upper(),
    format=LoggerFormat,
    serialize=settings.serialize,
    diagnose=False  # hide variable values in log backtrace
)
