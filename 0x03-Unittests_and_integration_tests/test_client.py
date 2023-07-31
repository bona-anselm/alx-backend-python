#!/usr/bin/env python3
""" Defines the TestGithubOrgClient class """
import unittest
from unittest.mock import Mock, MagicMock, patch
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
