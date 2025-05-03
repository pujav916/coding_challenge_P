import unittest
from unittest.mock import patch, MagicMock
from app.services.github_service import GitHubService

class TestGitHubService(unittest.TestCase):
    
    def setUp(self):
        self.github_service = GitHubService()
    
    @patch('app.services.github_service.requests.get')
    def test_get_organization_profile_success(self, mock_get):
        # Mock responses
        mock_org_response = MagicMock()
        mock_org_response.status_code = 200
        mock_org_response.json.return_value = {"login": "test-org"}
        
        mock_repos_response = MagicMock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [
            {
                "fork": False,
                "watchers_count": 5,
                "languages_url": "https://api.github.com/repos/test-org/repo1/languages",
                "topics": ["python", "api"]
            },
            {
                "fork": True,
                "watchers_count": 3,
                "languages_url": "https://api.github.com/repos/test-org/repo2/languages",
                "topics": ["javascript"]
            }
        ]
        
        mock_lang_response = MagicMock()
        mock_lang_response.status_code = 200
        mock_lang_response.json.return_value = {"Python": 10000, "JavaScript": 5000}
        
        # Configure mock to return different responses for different URLs
        def side_effect(*args, **kwargs):
            url = args[0]
            if "/orgs/" in url:
                return mock_org_response
            elif "/repos/" in url:
                return mock_repos_response
            elif "/languages" in url:
                return mock_lang_response
        
        mock_get.side_effect = side_effect
        
        # Call the method
        result = self.github_service.get_organization_profile("test-org")
        
        # Assertions
        self.assertEqual(result["original_repos"], 1)
        self.assertEqual(result["forked_repos"], 1)
        self.assertEqual(result["watchers"], 8)
        self.assertIn("Python", result["languages"])
        self.assertIn("python", result["topics"])
    
    @patch('app.services.github_service.requests.get')
    def test_get_organization_profile_error(self, mock_get):
        # Mock error response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "Not Found"}
        mock_get.return_value = mock_response
        
        # Assert that exception is raised
        with self.assertRaises(Exception):
            self.github_service.get_organization_profile("non-existent-org")