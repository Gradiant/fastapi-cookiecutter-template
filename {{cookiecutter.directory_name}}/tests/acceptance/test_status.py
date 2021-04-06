from tests.base_test import BaseAPITest


class TestStatus(BaseAPITest):
    def test_get_status(self):
        """Request the status endpoint. Should return status code 200"""
        r = self._request("GET", "/status")
        assert r.status_code == 200
