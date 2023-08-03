import json
from http import HTTPStatus
from tests.system_tests.common import CommonTestCase
from tests.fixtures.github_user_details import RESPONSE_GET_USER_DETAILS


class TestGetUserDetails(CommonTestCase):

    def get_user_details(self, username: str):
        response = self.test_client.get(f"/api/users/{username}/details")
        return response.status_code, json.loads(response.content)

    async def test_get_user_detail__happy_case__expect_success(self):
        self.mock_httpx_get(HTTPStatus.OK, RESPONSE_GET_USER_DETAILS)

        status_code, response = self.get_user_details("hassox")

        self.assertEqual(HTTPStatus.OK, status_code)
        self.assertDictEqual(response, RESPONSE_GET_USER_DETAILS)

    async def test_get_user_detail__wrong_username__expect_not_found_error(self):
        self.mock_httpx_get(HTTPStatus.NOT_FOUND, '')

        status_code, _ = self.get_user_details("foo")

        self.assertEqual(HTTPStatus.NOT_FOUND, status_code)

    async def test_get_user_detail__external_service_unavailable__expect_service_unavailable_error(self):
        self.mock_httpx_get(HTTPStatus.SERVICE_UNAVAILABLE, '')

        status_code, _ = self.get_user_details("hassox")

        self.assertEqual(HTTPStatus.SERVICE_UNAVAILABLE, status_code)
