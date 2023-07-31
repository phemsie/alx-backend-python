#!/usr/bin/env python3
"""unit test for GithubOrgClient
"""
import unittest
import requests
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''unittest for GithubOrgClient.org'''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, orgz: str, mock: unittest.mock.patch):
        '''unittest for org request is called once'''
        test_class = GithubOrgClient(orgz)
        test_class.org()
        mock.assert_called_once_with(
            f'https://api.github.com/orgs/{orgz}'
        )

    def test_public_repos_url(self):
        '''unittest result is based on the mocked payload'''
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "test"}
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, mock.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_j):
        '''test mocked property and the mocked get_json was called once'''
        test_payload = [{"name": "Google"}, {"name": "Facebook"}]
        mock_j.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_p:
            mock_p.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check_payload = [
                {"name": p} for p in result
            ]
            self.assertEqual(check_payload, test_payload)

            mock_j.assert_called_once()
            mock_p.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repos, license_key, expected):
        '''parameterized test GithubOrgClient.has_license'''
        result = GithubOrgClient.has_license(repos, license_key)
        self.assertEqual(result, expected)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        '''integration mock code that sends external requests'''
        @classmethod
        def setUpClass(cls):
            '''instructions to run before test'''
            params = {'return_value.json.side_effect':
                      [
                          cls.org_payload, cls.repos_payload,
                          cls.org_payload, cls.repos_payload
                      ]
                      }
            cls.get_patcher = patch('requests.get', **params)
            cls.mock = cls.get_patcher.start()

        def test_public_repos(self):
            '''to test GithubOrgClient.public_repos'''
            test_class = GithubOrgClient('google')
            self.assertEqual(test_class.org, self.org_payload)
            self.assertEqual(test_class.repos_payload, self.repos_payload)
            self.assertEqual(test_class.public_repos(), self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.mock.assert_called()

        def test_public_repos_with_license(self):
            '''to test the public_repos with the argument apache'''
            test_class = GithubOrgClient('google')

            self.assertEqual(test_class.public_repos(), self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.assertEqual(test_class.public_repos(
                "apache-2.0"), self.apache2_repos)
            self.mock.assert_called()

        @classmethod
        def tearDownClass(cls):
            '''instructions to run after test'''
            cls.get_patcher.stop()
