from typing import List, Optional
from pydantic import BaseModel, Field


class GithubUserModel(BaseModel):
    login: str
    id_: int = Field(..., alias='id')
    node_id: str
    avatar_url: Optional[str]
    gravatar_id: Optional[str]
    url: Optional[str]
    html_url: Optional[str]
    followers_url: Optional[str]
    following_url: Optional[str]
    gists_url: Optional[str]
    starred_url: Optional[str]
    subscriptions_url: Optional[str]
    organizations_url: Optional[str]
    repos_url: Optional[str]
    events_url: Optional[str]
    received_events_url: Optional[str]
    type_: Optional[str] = Field(..., alias='type')
    site_admin: bool


class GithubAllUserResponseModel(BaseModel):
    users: List[GithubUserModel]
    next_page: int


class GithubUserReposModel(BaseModel):
    id_: int = Field(..., alias='id')
    node_id: str
    name: str
    full_name: str
    owner: GithubUserModel
    private: bool
    html_url: str
    description: Optional[str]
    fork: bool
    url: str
    archive_url: Optional[str]
    assignees_url: Optional[str]
    blobs_url: Optional[str]
    branches_url: Optional[str]
    collaborators_url: Optional[str]
    comments_url: Optional[str]
    commits_url: Optional[str]
    compare_url: Optional[str]
    contents_url: Optional[str]
    contributors_url: Optional[str]
    deployments_url: Optional[str]
    downloads_url: Optional[str]
    events_url: Optional[str]
    forks_url: Optional[str]
    git_commits_url: Optional[str]
    git_refs_url: Optional[str]
    git_tags_url: Optional[str]
    git_url: Optional[str]
    issue_comment_url: Optional[str]
    issue_events_url: Optional[str]
    issues_url: Optional[str]
    keys_url: Optional[str]
    labels_url: Optional[str]
    languages_url: Optional[str]
    merges_url: Optional[str]
    milestones_url: Optional[str]
    notifications_url: Optional[str]
    pulls_url: Optional[str]
    releases_url: Optional[str]
    ssh_url: Optional[str]
    stargazers_url: Optional[str]
    statuses_url: Optional[str]
    subscribers_url: Optional[str]
    subscription_url: Optional[str]
    tags_url: Optional[str]
    teams_url: Optional[str]
    trees_url: Optional[str]
    clone_url: Optional[str]
    mirror_url: Optional[str]
    hooks_url: Optional[str]
    svn_url: Optional[str]
    homepage: Optional[str]
    language:Optional[str]
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: Optional[str]
    open_issues_count: int
    is_template: bool
    topics: List[str]
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    has_discussions: bool
    archived: bool
    disabled: bool
    visibility: Optional[str]
    pushed_at: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    permissions:  Optional[dict] = None
    security_and_analysis: Optional[dict] = None
