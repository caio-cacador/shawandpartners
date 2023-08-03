import httpx
from http import HTTPStatus
import os
from typing import List
from api.models.github_user import GithubUserModel, GithubUserReposModel
from api.exceptions.base import ServiceUnavailableError, UserNotFoundError


GITHUB_AUTH_TOKEN = "GITHUB_AUTH_TOKEN"


class GithubConnection:
    
    def __init__(self) -> None:
        self.__base_url = "https://api.github.com"
        self.__auth_token = f"Bearer {os.getenv(GITHUB_AUTH_TOKEN)}"
    
    @property
    def __headers(self):
        return {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": self.__auth_token
        }

    async def get_users(self, since: int) -> List[GithubUserModel]:
        async with httpx.AsyncClient() as client:
            response  = await client.get(
                f"{self.__base_url}/users?since={since}",
                headers=self.__headers
            )
            
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            raise ServiceUnavailableError()

    async def get_user_details(self, username: str) -> GithubUserModel:
        async with httpx.AsyncClient() as client:
            response  = await client.get(
                f"{self.__base_url}/users/{username}",
                headers=self.__headers
            )

        if response.status_code == HTTPStatus.OK:
            return response.json()
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise UserNotFoundError()
        else:
            raise ServiceUnavailableError()

    async def get_user_repos(self, username: str) -> List[GithubUserReposModel]:
        async with httpx.AsyncClient() as client:
            response  = await client.get(
                f"{self.__base_url}/users/{username}/repos",
                headers=self.__headers
            )

        if response.status_code == HTTPStatus.OK:
            return response.json()
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise UserNotFoundError()
        else:
            raise ServiceUnavailableError()
