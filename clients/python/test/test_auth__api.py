# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import print_nanny_client
from print_nanny_client.api.auth__api import AuthApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.auth__api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_email_create(self):
        """Test case for auth_email_create

        """
        pass

    def test_auth_mobile_create(self):
        """Test case for auth_mobile_create

        """
        pass

    def test_auth_token_create(self):
        """Test case for auth_token_create

        """
        pass

    def test_auth_verify_email_create(self):
        """Test case for auth_verify_email_create

        """
        pass

    def test_auth_verify_mobile_create(self):
        """Test case for auth_verify_mobile_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
