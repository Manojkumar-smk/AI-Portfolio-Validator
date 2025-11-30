import requests
from app.config import Config

class GitHubScanner:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {Config.GITHUB_TOKEN}"} if Config.GITHUB_TOKEN else {}

    def get_user_profile(self, username):
        """
        Fetches user profile from GitHub.
        """
        # Mock response for now if no token or for testing
        if not Config.GITHUB_TOKEN:
             return {
                "login": username,
                "name": "Mock User",
                "public_repos": 10,
                "followers": 5
            }
        
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None

    def get_user_repos(self, username):
        """
        Fetches user repositories.
        """
        if not Config.GITHUB_TOKEN:
            return [
                {"name": "repo1", "language": "Python", "stargazers_count": 10},
                {"name": "repo2", "language": "JavaScript", "stargazers_count": 5}
            ]

        url = f"{self.base_url}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return []

github_scanner = GitHubScanner()
