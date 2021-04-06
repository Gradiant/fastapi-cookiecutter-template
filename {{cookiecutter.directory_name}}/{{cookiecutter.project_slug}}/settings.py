import os

import pydantic


ENV_FILE = os.getenv("ENV_FILE", ".env")


class BaseSettings(pydantic.BaseSettings):
    """Base class for loading settings.
    The setting variables are loaded from environment settings first, then from the defined env_file.

    Different groups/contexts of settings are created using different classes, that can define an env_prefix which
    will be concatenated to the start of the variable name."""
    class Config:
        env_file = ENV_FILE


class APISettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 5000
    title: str = "{{ cookiecutter.app_name }}"
    """Title of the API, as shown in OpenAPI documentation"""

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class RequestLoggingSettings(BaseSettings):
    level: str = "TRACE"
    serialize: bool = False

    class Config(BaseSettings.Config):
        env_prefix = "REQUEST_LOG_"


api_settings = APISettings()
request_logging_settings = RequestLoggingSettings()
