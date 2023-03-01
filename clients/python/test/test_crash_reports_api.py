# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.127.2
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.crash_reports_api import CrashReportsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestCrashReportsApi(unittest.TestCase):
    """CrashReportsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.crash_reports_api.CrashReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_crash_reports_create(self):
        """Test case for crash_reports_create

        """
        pass

    def test_crash_reports_list(self):
        """Test case for crash_reports_list

        """
        pass

    def test_crash_reports_partial_update(self):
        """Test case for crash_reports_partial_update

        """
        pass

    def test_crash_reports_retrieve(self):
        """Test case for crash_reports_retrieve

        """
        pass

    def test_crash_reports_update(self):
        """Test case for crash_reports_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
