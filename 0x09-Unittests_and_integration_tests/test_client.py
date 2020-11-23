#!/usr/bin/env python3
"""
Test for client
"""

from unittest import TestCase, mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import requests


class TestGithubOrgClient(TestCase):
    """
    Test for client.GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, name, payload, fn_get):
        """ test case for client.org """
        goc = GithubOrgClient(name)
        fn_get.return_value = payload

        self.assertEqual(payload, goc.org)
        fn_get.assert_called_once()

    def test_public_repos_url(self):
        """
        test for client._public_repos_url
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_obj:
            mock_obj.return_value = {"url": 'http://google.com'}

            r = GithubOrgClient(mock_obj.return_value)._public_repos_url

            self.assertEqual(r, mock_obj.return_value)
            mock_obj.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """
        test for client._has_licence
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)
