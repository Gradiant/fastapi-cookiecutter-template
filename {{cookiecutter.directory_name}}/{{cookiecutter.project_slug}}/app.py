import uvicorn
from fastapi import FastAPI

from .middlewares import request_handler
from .routers import setup_routes, TAGS_METADATA
from .settings import api_settings as settings


app = FastAPI(
    title=settings.title,
    openapi_tags=TAGS_METADATA
)
app.middleware("http")(request_handler)
setup_routes(app)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port
    )
