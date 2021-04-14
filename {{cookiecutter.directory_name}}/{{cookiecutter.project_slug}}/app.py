import uvicorn
from fastapi import FastAPI

from .middlewares import request_handler
from .routers import setup_routes
{%- if cookiecutter.advanced_docs == "no" %}
from .routers import TAGS_METADATA
{% else %}
from .documentation import setup_documentation
{% endif -%}
from .settings import api_settings, api_docs_settings

{% if cookiecutter.advanced_docs == "yes" -%}
app = FastAPI(
    docs_url="/docs" if not api_docs_settings.static_path else None,
    redoc_url="/redoc" if not api_docs_settings.static_path else None
)
{% else -%}
app = FastAPI(
    title=api_docs_settings.title,
    version=api_docs_settings.version,
    openapi_tags=TAGS_METADATA
)
{% endif -%}
app.middleware("http")(request_handler)
setup_routes(app)
{%- if cookiecutter.advanced_docs == "yes" %}
setup_documentation(app)
{%- endif %}


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=api_settings.host,
        port=api_settings.port
    )
