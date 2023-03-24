# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.129.1
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

    def test_pis_all_events_list(self):
        """Test case for pis_all_events_list

        """
        pass

    def test_pis_commands_create(self):
        """Test case for pis_commands_create

        """
        pass

    def test_pis_commands_list(self):
        """Test case for pis_commands_list

        """
        pass

    def test_pis_events_commands_list(self):
        """Test case for pis_events_commands_list

        """
        pass

    def test_pis_events_create(self):
        """Test case for pis_events_create

        """
        pass

    def test_pis_events_list(self):
        """Test case for pis_events_list

        """
        pass

    def test_pis_events_retrieve(self):
        """Test case for pis_events_retrieve

        """
        pass

    def test_pis_events_status_list(self):
        """Test case for pis_events_status_list

        """
        pass

    def test_pis_status_create(self):
        """Test case for pis_status_create

        """
        pass

    def test_pis_status_list(self):
        """Test case for pis_status_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
