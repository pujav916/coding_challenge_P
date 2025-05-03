import unittest
from unittest.mock import patch, MagicMock
from app.services.bitbucket_service import BitbucketService

class TestBitbucketService(unittest.TestCase):
    
    def setUp(self):
        self.bitbucket_service = BitbucketService()
    
    @patch('app.services.bitbucket_service.requests.get')
    def test_get_team_profile_success(self, mock_get):
        # Mock responses
        mock_repos_response = MagicMock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = {
            "values": [
                {
                    "parent": None,
                    "language": "python",
                    "links": {
                        "watchers": {
                            "href": "https://api.bitbucket.org/2.0/repositories/test-team/repo1/watchers"
                        }
                    }
                },
                {
                    "parent": {"full_name": "other/repo"},
                    "language": "javascript",
                    "links": {
                        "watchers": {
                            "href": "https://api.bitbucket.org/2.0/repositories/test-team/repo2/watchers"
                        }
                    }
                }
            ]
        }
        
        mock_watchers_response = MagicMock()
        mock_watchers_response.status_code = 200
        mock_watchers_response.json.return_value = {"size": 5}
        
        # Configure mock to return different responses for different URLs
        def side_effect(*args, **kwargs):
            url = args[0]
            if "/repositories/" in url and not "/watchers" in url:
                return mock_repos_response
            elif "/watchers" in url:
                return mock_watchers_response
        
        mock_get.side_effect = side_effect
        
        # Call the method
        result = self.bitbucket_service.get_team_profile("test-team")
        
        # Assertions
        self.assertEqual(result["original_repos"], 1)
        self.assertEqual(result["forked_repos"], 1)
        self.assertEqual(result["watchers"], 10)  # 5 watchers per repo
        self.assertIn("python", result["languages"])
        self.assertIn("javascript", result["languages"])
    
    @patch('app.services.bitbucket_service.requests.get')
    def test_get_team_profile_error(self, mock_get):
        # Mock error response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": {"message": "Not Found"}}
        mock_get.return_value = mock_response
        
        # Assert that exception is raised
        with self.assertRaises(Exception):
            self.bitbucket_service.get_team_profile("non-existent-team")