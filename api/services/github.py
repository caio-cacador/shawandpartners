import httpx
from typing import List
from api.connections.github import GithubConnection
from api.models.github_user import GithubUserModel, GithubUserReposModel


class GithubService:
    
    def __init__(self) -> None:
        self.connection = GithubConnection()
    
    async def get_all_users(self, since: int) -> List[GithubUserModel]:
        users = await self.connection.get_users(since)
        return [GithubUserModel(**user) for user in users]

    async def get_user_details(self, username: str) -> GithubUserModel:
        user_detail = await self.connection.get_user_details(username)
        return GithubUserModel(**user_detail)

    async def get_user_repos(self, username: str) -> List[GithubUserReposModel]:
        user_repos = await self.connection.get_user_repos(username)
        return [GithubUserReposModel(**repo) for repo in user_repos]
