# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.4
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.moonraker_api import MoonrakerApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestMoonrakerApi(unittest.TestCase):
    """MoonrakerApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.moonraker_api.MoonrakerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_moonraker_create(self):
        """Test case for moonraker_create

        """
        pass

    def test_moonraker_list(self):
        """Test case for moonraker_list

        """
        pass

    def test_moonraker_partial_update(self):
        """Test case for moonraker_partial_update

        """
        pass

    def test_moonraker_retrieve(self):
        """Test case for moonraker_retrieve

        """
        pass

    def test_moonraker_server_update_or_create(self):
        """Test case for moonraker_server_update_or_create

        """
        pass

    def test_moonraker_update(self):
        """Test case for moonraker_update

        """
        pass

    def test_pis_moonraker_server_list(self):
        """Test case for pis_moonraker_server_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
