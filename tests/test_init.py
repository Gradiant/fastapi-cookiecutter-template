import requests

from .base import BaseTest


class TestCookiecutterInit(BaseTest):
    def test_create_run_get(self):
        """Create a new project from the template, start running it, and GET the /status endpoint."""
        r = requests.get(f"http://localhost:{self.port}/status")
        assert r.status_code == 200
