import requests

class GitHubService:
    """Service to interact with GitHub API"""
    
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_organization_profile(self, org_name):
        """
        Get organization profile data from GitHub
        
        Args:
            org_name (str): GitHub organization name
            
        Returns:
            dict: Organization profile data
        """
        # Get organization data
        org_url = f"{self.base_url}/orgs/{org_name}"
        org_response = requests.get(org_url, headers=self.headers)
        
        if org_response.status_code != 200:
            raise Exception(f"Failed to fetch GitHub organization: {org_response.json().get('message', 'Unknown error')}")
        
        # Get repositories data
        repos_url = f"{self.base_url}/orgs/{org_name}/repos?per_page=100"
        repos_response = requests.get(repos_url, headers=self.headers)
        
        if repos_response.status_code != 200:
            raise Exception(f"Failed to fetch GitHub repositories: {repos_response.json().get('message', 'Unknown error')}")
        
        repos = repos_response.json()
        
        # Process repository data
        original_repos = 0
        forked_repos = 0
        languages = {}
        topics = {}
        watchers = 0
        
        for repo in repos:
            # Count original vs forked repos
            if repo.get("fork", False):
                forked_repos += 1
            else:
                original_repos += 1
            
            # Count watchers/stargazers
            watchers += repo.get("watchers_count", 0)
            
            # Get languages for this repo
            lang_url = repo.get("languages_url")
            if lang_url:
                lang_response = requests.get(lang_url, headers=self.headers)
                if lang_response.status_code == 200:
                    repo_languages = lang_response.json()
                    for lang, bytes_count in repo_languages.items():
                        languages[lang] = languages.get(lang, 0) + 1
            
            # Get topics for this repo
            repo_topics = repo.get("topics", [])
            for topic in repo_topics:
                topics[topic] = topics.get(topic, 0) + 1
        
        return {
            "original_repos": original_repos,
            "forked_repos": forked_repos,
            "watchers": watchers,
            "languages": languages,
            "topics": topics
        }
