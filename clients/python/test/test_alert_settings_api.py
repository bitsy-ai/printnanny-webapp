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
from printnanny_api_client.api.alert_settings_api import AlertSettingsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestAlertSettingsApi(unittest.TestCase):
    """AlertSettingsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.alert_settings_api.AlertSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alert_settings_create(self):
        """Test case for alert_settings_create

        """
        pass

    def test_alert_settings_list(self):
        """Test case for alert_settings_list

        """
        pass

    def test_alert_settings_partial_update(self):
        """Test case for alert_settings_partial_update

        """
        pass

    def test_alert_settings_update(self):
        """Test case for alert_settings_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
