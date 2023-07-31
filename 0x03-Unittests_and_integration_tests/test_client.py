#!/usr/bin/env python3
""" Defines the TestGithubOrgClient class """
import unittest
from unittest.mock import Mock, MagicMock, PropertyMock, patch
from typing import Dict
import client
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
        Provides functionality for testing that GithubOrgClient class
        returns the expected result
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch("client.get_json")
    def test_org(self,
                 org: str,
                 response: Dict,
                 mocked_fn: MagicMock
                 ) -> None:
        """ Tests that GithubOrgClient returns the expected result """
        mocked_fn.return_value = MagicMock(return_value=response)
        git_client = client.GithubOrgClient(org)
        self.assertEqual(git_client.org(), response)
        mocked_fn.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org)
                )

    def test_public_repos_url(self) -> None:
        """ Tests that _public_repos_url produces expected result """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_payload:
            mock_payload.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                client.GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mocked_public_repos:
            mocked_public_repos.return_value = test_payload["repos_url"]
            self.assertEqual(
                client.GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mocked_public_repos.assert_called_once()
        mock_get_json.assert_called_once()
