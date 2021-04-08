import os
{%- if cookiecutter.advanced_docs|tojson %}
from typing import Optional
{% endif %}

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

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class APIDocsSettings(BaseSettings):
    title: str = "{{ cookiecutter.app_name }}"
    """Title of the API"""
    description: Optional[str] = None
    """Description of the API"""
    version: str = "version"
    """Version of the API"""
    {%- if cookiecutter.advanced_docs == "yes" %}
    custom_logo: Optional[str] = None
    """URL of a custom logo to show in ReDoc (if not set, no logo will be shown)"""
    static_path: Optional[str] = None
    """Path where to load static files from, used for the generated documentation.
    If set, both OpenAPI/Swagger and ReDoc will load required files from there, instead of the default CDN.
    More information available in FastAPI documentation:
    https://fastapi.tiangolo.com/advanced/extending-openapi/#download-the-files

    - Swagger UI requires the files "swagger-ui.bundle.js", "swagger-ui.css", "favicon.ico"
    - ReDoc requires the file "redoc.standalone.js", "favicon.ico"
    """
    {%- endif %}

    class Config(BaseSettings.Config):
        env_prefix = "API_DOCS_"


class RequestLoggingSettings(BaseSettings):
    level: str = "TRACE"
    serialize: bool = False

    class Config(BaseSettings.Config):
        env_prefix = "REQUEST_LOG_"


api_settings = APISettings()
api_docs_settings = APIDocsSettings()
request_logging_settings = RequestLoggingSettings()
