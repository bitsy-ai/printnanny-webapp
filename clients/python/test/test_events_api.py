# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.events_api import EventsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.events_api.EventsApi()  # noqa: E501

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
