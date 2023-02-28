# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.127.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.settings_api import SettingsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alert_settings_email_create(self):
        """Test case for alert_settings_email_create

        """
        pass

    def test_alert_settings_email_list(self):
        """Test case for alert_settings_email_list

        """
        pass

    def test_alert_settings_email_partial_update(self):
        """Test case for alert_settings_email_partial_update

        """
        pass

    def test_alert_settings_email_retrieve(self):
        """Test case for alert_settings_email_retrieve

        """
        pass

    def test_alert_settings_email_update(self):
        """Test case for alert_settings_email_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
