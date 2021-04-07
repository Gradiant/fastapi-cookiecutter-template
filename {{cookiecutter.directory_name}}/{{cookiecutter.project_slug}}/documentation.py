{% if cookiecutter.advanced_docs == true %}
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from .routers import TAGS_METADATA
from .settings import api_docs_settings as settings


def _custom_openapi(app: FastAPI):
    """Custom OpenAPI schema generator function, featuring:

    - Cache the schema
    - Use self-hosted files for documentation
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.title,
        version=settings.version,
        routes=app.routes,
        tags=TAGS_METADATA
    )

    if settings.custom_logo:
        openapi_schema["info"]["x-logo"] = dict(url=settings.custom_logo)

    app.openapi_schema = openapi_schema
    return openapi_schema


def setup_documentation(app: FastAPI):
    app.openapi = lambda: _custom_openapi(app)

{% endif %}