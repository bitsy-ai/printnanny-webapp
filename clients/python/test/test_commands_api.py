# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.98.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.commands_api import CommandsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestCommandsApi(unittest.TestCase):
    """CommandsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.commands_api.CommandsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_commands_create(self):
        """Test case for commands_create

        """
        pass

    def test_commands_list(self):
        """Test case for commands_list

        """
        pass

    def test_commands_retrieve(self):
        """Test case for commands_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
