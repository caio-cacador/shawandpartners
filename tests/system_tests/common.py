from abc import ABC
from asynctest import case
import httpx
from asyncmock import AsyncMock
from unittest.mock import patch
from main import app
from fastapi.testclient import TestClient


class CommonTestCase(ABC, case.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_client = TestClient(app=app)
        cls.mocked_httpx_get = AsyncMock()
        patch(
            "api.connections.github.httpx.AsyncClient.get",
            cls.mocked_httpx_get
        ).start()

    def mock_httpx_get(self, status_code: int, response: dict):
        self.mocked_httpx_get.return_value = httpx.Response(status_code, json=response)
