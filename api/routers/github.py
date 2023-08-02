from typing import List
from fastapi import APIRouter, Query, Path
from fastapi.responses import JSONResponse
from http import HTTPStatus
from api.services.github import GithubService
from api.exceptions.base import UserNotFoundError
from api.models.github_user import (
    GithubUserModel,
    GithubAllUserResponseModel,
    GithubUserReposModel
)


router = APIRouter(prefix='/users', tags=['Proxy API for GitHub users'])

SINCE = dict(example=1)
USERNAME = dict(example="user_123", min_length=1)
RESPONSE_404 = {404: {"description": "Not found"}}
RESPONSE_503 = {503: {"description": "Service Unavailable"}}


@router.get("", responses=RESPONSE_503, response_model=GithubAllUserResponseModel)
async def list_users(since: int = Query(**SINCE)):
    """
    List all users
    """
    users = await GithubService().get_all_users(since)
    return GithubAllUserResponseModel(users=users, next_page=users[-1].id_)


@router.get(
    "/{username}/details", 
    responses={**RESPONSE_404, **RESPONSE_503},
    response_model=GithubUserModel
)
async def get_user_detail(username: str = Path(**USERNAME)):
    """
    Get user details
    """
    try:
        return await GithubService().get_user_details(username)
    except UserNotFoundError:
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={"message": f"User '{username}' not found"},
        )


@router.get(
    "/{username}/repos",
    responses={**RESPONSE_404, **RESPONSE_503},
    response_model=List[GithubUserReposModel]
)
async def get_user_repos(username: str = Path(**USERNAME)):
    """
    Get user repositories
    """
    try:
        return await GithubService().get_user_repos(username)    
    except UserNotFoundError:
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={"message": f"User '{username}' not found"},
        )
