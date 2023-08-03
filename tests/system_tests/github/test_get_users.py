import httpx
import json
from asyncmock import AsyncMock
from http import HTTPStatus
from unittest.mock import patch
from tests.system_tests.common import CommonTestCase
from tests.fixtures.github_users import RESPONSE_GET_USERS


class TestGetUsers(CommonTestCase):

    def get_users(self, since: int):
        response = self.test_client.get(f"/api/users?since={since}")
        return response.status_code, json.loads(response.content)

    async def test_get_all_users__happy_case__expect_success(self):
        self.mock_httpx_get(HTTPStatus.OK, RESPONSE_GET_USERS)

        status_code, response = self.get_users(since=0)

        self.assertEqual(HTTPStatus.OK, status_code)
        self.assertDictEqual(response, dict(users=RESPONSE_GET_USERS, next_page=4))

    async def test_get_all_users__without_since_in_query__expect_validation_error(self):
        self.mock_httpx_get(HTTPStatus.OK, RESPONSE_GET_USERS)

        response = self.test_client.get(f"/api/users")
        content_detail = json.loads(response.content)["detail"][0]

        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        self.assertEqual(["query", "since"], content_detail["loc"])
        self.assertEqual("Field required", content_detail["msg"])

    async def test_get_all_users__external_service_unavailable__expect_service_unavailable(self):
        self.mock_httpx_get(HTTPStatus.SERVICE_UNAVAILABLE, "")

        status_code, _ = self.get_users(since=0)

        self.assertEqual(HTTPStatus.SERVICE_UNAVAILABLE, status_code)
