# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.131.2
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

    def test_alerts_print_job_create(self):
        """Test case for alerts_print_job_create

        """
        pass

    def test_alerts_print_job_list(self):
        """Test case for alerts_print_job_list

        """
        pass

    def test_alerts_print_job_partial_update(self):
        """Test case for alerts_print_job_partial_update

        """
        pass

    def test_alerts_print_job_retrieve(self):
        """Test case for alerts_print_job_retrieve

        """
        pass

    def test_alerts_print_job_update(self):
        """Test case for alerts_print_job_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
