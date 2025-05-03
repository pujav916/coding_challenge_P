import requests

class BitbucketService:
    """Service to interact with Bitbucket API"""
    
    def __init__(self):
        self.base_url = "https://api.bitbucket.org/2.0"
    
    def get_team_profile(self, team_name):
        """
        Get team profile data from Bitbucket
        
        Args:
            team_name (str): Bitbucket team name
            
        Returns:
            dict: Team profile data
        """
        # Get team repositories
        repos_url = f"{self.base_url}/repositories/{team_name}"
        response = requests.get(repos_url)
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch Bitbucket repositories: {response.json().get('error', {}).get('message', 'Unknown error')}")
        
        repos_data = response.json()
        repos = repos_data.get("values", [])
        
        # Process repository data
        original_repos = 0
        forked_repos = 0
        languages = {}
        topics = {}
        watchers = 0
        
        for repo in repos:
            # Count original vs forked repos
            if repo.get("parent", None):
                forked_repos += 1
            else:
                original_repos += 1
            
            # Get watchers count
            watchers_url = repo.get("links", {}).get("watchers", {}).get("href")
            if watchers_url:
                watchers_response = requests.get(watchers_url)
                if watchers_response.status_code == 200:
                    watchers += watchers_response.json().get("size", 0)
            
            # Get language
            language = repo.get("language")
            if language:
                languages[language] = languages.get(language, 0) + 1
        
        # Bitbucket doesn't have topics like GitHub, but we'll include an empty dict for consistency
        
        return {
            "original_repos": original_repos,
            "forked_repos": forked_repos,
            "watchers": watchers,
            "languages": languages,
            "topics": topics
        }

