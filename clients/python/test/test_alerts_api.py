# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.94.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.alerts_api import AlertsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.alerts_api.AlertsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alerts_create(self):
        """Test case for alerts_create

        """
        pass

    def test_alerts_list(self):
        """Test case for alerts_list

        """
        pass

    def test_alerts_partial_update(self):
        """Test case for alerts_partial_update

        """
        pass

    def test_alerts_recent(self):
        """Test case for alerts_recent

        """
        pass

    def test_alerts_retrieve(self):
        """Test case for alerts_retrieve

        """
        pass

    def test_alerts_seen(self):
        """Test case for alerts_seen

        """
        pass

    def test_alerts_unread(self):
        """Test case for alerts_unread

        """
        pass

    def test_alerts_update(self):
        """Test case for alerts_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
