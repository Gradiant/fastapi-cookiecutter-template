{% if cookiecutter.advanced_docs == "yes" -%}
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html

from .routers import TAGS_METADATA
from .settings import api_docs_settings as settings


def _custom_openapi(app: FastAPI):
    """Custom OpenAPI schema generator function, supporting:

    - Cache the schema
    - Set custom logo in ReDoc
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


def _setup_docs_with_statics(app: FastAPI):
    from fastapi.staticfiles import StaticFiles
    app.mount("/static", StaticFiles(directory=settings.static_path), name="static")
    app.docs_url = None
    app.redoc_url = None

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
            swagger_favicon_url="/static/favicon.ico"
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @app.get("/redoc", include_in_schema=False)
    async def custom_redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
            redoc_favicon_url="/static/favicon.ico",
            with_google_fonts=False
        )


def setup_documentation(app: FastAPI):
    app.openapi = lambda: _custom_openapi(app)
    if settings.static_path:
        _setup_docs_with_statics(app)

{%- endif %}
