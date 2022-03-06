# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.telemetry_api import TelemetryApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestTelemetryApi(unittest.TestCase):
    """TelemetryApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.telemetry_api.TelemetryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_octoprint_events_create(self):
        """Test case for octoprint_events_create

        """
        pass

    def test_octoprint_events_list(self):
        """Test case for octoprint_events_list

        """
        pass

    def test_octoprint_events_retrieve(self):
        """Test case for octoprint_events_retrieve

        """
        pass

    def test_print_job_events_list(self):
        """Test case for print_job_events_list

        """
        pass

    def test_print_job_events_retrieve(self):
        """Test case for print_job_events_retrieve

        """
        pass

    def test_print_nanny_plugin_events_list(self):
        """Test case for print_nanny_plugin_events_list

        """
        pass

    def test_print_nanny_plugin_events_retrieve(self):
        """Test case for print_nanny_plugin_events_retrieve

        """
        pass

    def test_remote_command_events_list(self):
        """Test case for remote_command_events_list

        """
        pass

    def test_remote_command_events_retrieve(self):
        """Test case for remote_command_events_retrieve

        """
        pass

    def test_telemetry_events_create(self):
        """Test case for telemetry_events_create

        """
        pass

    def test_telemetry_events_list(self):
        """Test case for telemetry_events_list

        """
        pass

    def test_telemetry_events_retrieve(self):
        """Test case for telemetry_events_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
