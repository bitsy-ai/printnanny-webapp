# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.5
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.pis_api import PisApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestPisApi(unittest.TestCase):
    """PisApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.pis_api.PisApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pis_events_create(self):
        """Test case for pis_events_create

        """
        pass

    def test_pis_events_list(self):
        """Test case for pis_events_list

        """
        pass

    def test_pis_events_list2(self):
        """Test case for pis_events_list2

        """
        pass

    def test_pis_events_retrieve(self):
        """Test case for pis_events_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
