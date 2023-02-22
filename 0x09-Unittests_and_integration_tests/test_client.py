#!/usr/bin/env python3
"""
Unit tests for A github org client
"""

from typing import Dict
from unittest import TestCase
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """
    Test class to 'GithubOrgClient'

    Args:
        TestCase (TestCase): Unittest TestCase
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, test_org: str, mock: Mock) -> None:
        """
        This method should test that GithubOrgClient.org
        returns the correct value.

        Args:
            test_org (str): Org name
            mock (Mock): Mock Object of get_json
        """
        test_instance = GithubOrgClient(test_org)
        self.assertEqual(test_instance.org, mock.return_value)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://example_url.com'})
    ])
    def test_public_repos_url(self, name: str,
                              res_url: Dict[str, str]) -> None:
        """
        Test the method '_public_repos_url' from client

        Args:
            name (str): Org name
            res_url (str): Expected url response
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock(return_value=res_url)):
            res = GithubOrgClient(name)._public_repos_url
            self.assertEqual(res, res_url.get("repos_url"))

    @patch('client.get_json',
           return_value={"repos_url": "https://example.com/repos"})
    def test_public_repos(self, mock: Mock) -> None:
        """
        Test "_public_repos_url" private method

        Args:
            mock (Mock): Generated mock of get_json
        """
        mock()
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as _mock:
            _mock.return_value = {"repos_url": "https://example.com/repos"}
            client = GithubOrgClient("example_url")
            self.assertEqual(client._public_repos_url, _mock.return_value)
            mock.assert_called_once()
            _mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected_result: bool) -> None:
        """
        Test the static method has_license of client module.

        Args:
            repo (Dict[str, Dict]): repo with the license data
            license_key (str): Key for the license
            expected_result (bool): Expected result for the
            static method
        """
        result: bool = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    (
        "org_payload",
        "repos_payload",
        "expected_repos",
        "apache2_repos"
    ),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """
    Integration Test for the GithubOrgClient.public_repos method
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Overload setUpClass, from TestCase class.
        For setup the integration test
        """
        cls.get_patcher = patch("requests.get")
        cls.mock = cls.get_patcher.start()
        cls.mock.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Overload tearDownCLass,
        from TestCase class
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Test public repos method of GithubOrgClient
        """
        client = GithubOrgClient("Integration test")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test public repos method using license of GithubOrgClient
        """
        client = GithubOrgClient("Integration test with license")
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)
