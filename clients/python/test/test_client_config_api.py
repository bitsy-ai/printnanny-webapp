# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.client_config_api import ClientConfigApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestClientConfigApi(unittest.TestCase):
    """ClientConfigApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.client_config_api.ClientConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_client_config_list(self):
        """Test case for client_config_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
