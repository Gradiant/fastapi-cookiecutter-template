from typing import Optional

from fastapi.testclient import TestClient
from requests import Session, Response

from {{cookiecutter.project_slug}}.app import app


class BaseAPITest:
    """Base API test class that starts a fastapi TestClient (https://fastapi.tiangolo.com/tutorial/testing/)."""
    client: Session

    @classmethod
    def setup_class(cls):
        with TestClient(app) as client:
            # Usage of context-manager to trigger app events when using TestClient:
            # https://fastapi.tiangolo.com/advanced/testing-events/
            cls.client = client

    def _request(self, method: str, endpoint: str, body: Optional[dict] = None, **kwargs) -> Response:
        """Perform a generic HTTP request against an endpoint of the API"""
        return self.client.request(method=method, url=endpoint, json=body, **kwargs)
